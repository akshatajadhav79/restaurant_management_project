from datetime import datetime
def format_datetime(dt):
    if dt is None:
        return ""

    if not isinstance(dt,datetime):
        raise ValueError("input must be a datetime object or None")

    return dt.strftime(%B %d,%Y at %I:%M %p)