import sys
import os

import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


########################################################
from django.core.wsgi import get_wsgi_application
os.environ['DJANGO_SETTINGS_MODULE'] = 'oorjan.settings'
application = get_wsgi_application()
########################################################


import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta
from helpers.emailing import send_email
from oorjan_app.models import SolarReferenceData, SolarData, ReportAnalyzer


class EmailReport:

    def __init__(self):
        pass

    def _starter(self):
        receiver_email_list = self.__get_receiver_email_id()
        if not receiver_email_list:
            print "receiver email not available"
            return 0
        else:
            data_to_email = self.__calculate_report()
            if data_to_email:
                self.__send_email_to_analyzer(data_to_email, receiver_email_list)

    def __get_receiver_email_id(self):
        receiver_email_list = []
        try:
            receiver_email_data = ReportAnalyzer.objects.all()
            receiver_email_list = [i.email_to for i in receiver_email_data]
        except:
            pass

        return receiver_email_list

    def __calculate_report(self):
        

        today_min = datetime.datetime.combine(datetime.date.today()-timedelta(days=0), datetime.time.min)
        today_max = datetime.datetime.combine(datetime.date.today()-timedelta(days=0), datetime.datetime.strptime('19:00', '%H:%M').time())

        # get today's data
        today_data = SolarData.objects.filter(timestamp__range=(today_min, today_max)).order_by('timestamp')

        today_ref_min = datetime.datetime.combine(datetime.date.today()-relativedelta(years=2)-timedelta(days=0), datetime.time.min)
        today_ref_max = datetime.datetime.combine(datetime.date.today()-relativedelta(years=2)-timedelta(days=0), datetime.datetime.strptime('19:00', '%H:%M').time())

        # get reference data
        today_ref_data = SolarReferenceData.objects.filter(timestamp__range=(today_ref_min, today_ref_max)).order_by('timestamp')

        hours_in_demand, hours_to_plot = [], []
        data_to_mail = 'Solar Power usage data\n\nNote: Hours with (*) have less power than 80% of reference data of that particular hour.\n\n| Hour   |      Usage(watt)      |\n'

        for d, r in zip( today_data, today_ref_data ):

            # add all the hours and power usage in list
            hours_to_plot.append((d.timestamp.hour, str('%.2f'%d.dc_power)))

            if float(d.dc_power) < (0.80*float(r.dc_power)):
                # hours in demand are hours where usage is less than 80% of reference data
                hours_in_demand.append(d.timestamp.hour)
                data_to_mail = data_to_mail + '|    *'  + str(d.timestamp.hour) + '  |       ' + str('%.2f'%d.dc_power)
            else:
                data_to_mail = data_to_mail + '|    '  + str(d.timestamp.hour) + '  |       ' + str('%.2f'%d.dc_power)


            data_to_mail = data_to_mail + '     |\n'

        if hours_to_plot:
            return data_to_mail
        else:
            return ''

    def __send_email_to_analyzer(self, data_to_mail, receiver_email_list):
            send_email( receiver_email_list, data_to_mail, "Solar Power Usage Report", is_html = False )


if __name__ == '__main__':
    obj = EmailReport()
    obj._starter()


