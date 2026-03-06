# home/utils.py

from datetime import datetime
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