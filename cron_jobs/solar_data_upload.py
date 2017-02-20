# This script is to update hourly data in database.
# Otherwise data will come in django views request
# Model "solar data" in admin panel.


import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


########################################################
from django.core.wsgi import get_wsgi_application
os.environ['DJANGO_SETTINGS_MODULE'] = 'oorjan.settings'
application = get_wsgi_application()
########################################################


from datetime import datetime, timedelta
from oorjan_app.serializers import SolarDataSerializer
from oorjan_app.models import SolarReferenceData, SolarData, SolarMetaData
import random


class SolarDataUpload:

    def __init__(self):
        pass

    def _starter(self):
        self.__insert_data_in_db()


    def __insert_data_in_db(self):


        for i in range(0, 24):

            hour = str(i) if(i>9) else ('0'+str(i))
            # Get this installation key from admin panel
            post_data = {"installation_key":"9d370986-8cc0-4d3d-8ecf-946845f7817b","dc_power":'%.2f'%random.uniform(0.0, 3000.0),"timestamp":'2017-02-20 %s:00:00' % (hour,)}

            try:
                solar_user = SolarMetaData.objects.get(installation_key=post_data['installation_key'])
            except:
                print "Invalid Installation Key"
                exit(0)

            serializer = SolarDataSerializer(data=post_data)
            if serializer.is_valid():
                serializer.save()
            else:
                print "Invalid Serializer"

        # Below commented part will work if we sat up a cron every hour

        """
        # Get this installation key from admin panel
        post_data = {"installation_key":"9d370986-8cc0-4d3d-8ecf-946845f7817b","dc_power":'%.2f'%random.uniform(1.5, 1.9),"timestamp":(datetime.now()-timedelta(hours=1)).strftime('%Y-%m-%d %H:%M:%S')}

        try:
            solar_user = SolarMetaData.objects.get(installation_key=post_data['installation_key'])
        except:
            print "Invalid Installation Key"
            exit(0)

        serializer = SolarDataSerializer(data=post_data)
        if serializer.is_valid():
            serializer.save()
        else:
            print "Invalid Serializer"
        """
           
if __name__ == '__main__':
    obj = SolarDataUpload()
    obj._starter()

