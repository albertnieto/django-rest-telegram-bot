from datetime import datetime
import tzlocal

def unix_to_local_timezone(unix_timestamp):
    local_timezone = tzlocal.get_localzone() # get pytz timezone
    local_time = datetime.fromtimestamp(unix_timestamp, local_timezone)
    return local_time