# home/utils.py

from datetime import datetime,time
from django.apps import apps
import re


def get_today_operating_hours():

    # Get current day name (e.g., Monday, Tuesday)
    today_name = datetime.now().strftime('%A')

    # Dynamically get model to avoid circular imports
    DailyOperatingHours = apps.get_model('home', 'DailyOperatingHours')

    try:
        today_hours = DailyOperatingHours.objects.get(day_of_week=today_name)
        return today_hours.open_time, today_hours.close_time
    except DailyOperatingHours.DoesNotExist:
        return None, None

def is_valid_Phone_number(phone):
    pattern = r'^\+?\d{1,3}?[- ]?\d{10,12}$'
    if re.match(pattern,phone):
        return True
    return False

def is_restaurant_open():
    now = datetime.now()
    current_day = now.weekday()
    current_time = now.time()

    # opening hr
    weekday_open = time(9,0)
    weekday_close = time(22,0)

    weekend_open = time(10,0)
    weekend_close = time(23,0)

    if current_day < 5:
        return weekday_open <= current_time <= weekday_close

    else:
        return weekend_open <= current_time <= weekend_close
