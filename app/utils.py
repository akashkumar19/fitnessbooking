import pytz

def to_timezone(dt, tz_name="Asia/Kolkata"):
    return dt.astimezone(pytz.timezone(tz_name))
