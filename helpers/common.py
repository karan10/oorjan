
class Common:

    def  __init__( self ) :
        pass

    @staticmethod
    def local_time_to_utc(time_obj):
        import pytz, datetime
        local = pytz.timezone ("Asia/Kolkata")
        local_dt = local.localize(time_obj, is_dst=None)
        return local_dt.astimezone (pytz.utc)

