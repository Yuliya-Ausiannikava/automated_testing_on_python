"""
Programs using the module datetime
"""

from datetime import datetime
from dateutil.relativedelta import relativedelta


def count_days(date_1='', date_2=''):
    """
    Counts the number of days between dates
    :param date_1: string in format YYYY-MM-DD
    :param date_2: string in format YYYY-MM-DD
    :return: relativedelta object
    """
    try:
        format_date_1 = datetime.strptime(date_1, "%Y-%m-%d").date()
        format_date_2 = datetime.strptime(date_2, "%Y-%m-%d").date()
        result = relativedelta(format_date_2, format_date_1)
        print(result)
        return result
    except ValueError:
        print('Error: Invalid date format. Please use format YYYY-MM-DD')
        return None


count_days('2025-09-05', '2025-09-16')
print('___________________________________________________________')


def past_future(date=''):
    """
    Checks whether a date is past or future
    :param date: string in format YYYY-MM-DD
    :return: string
    """
    try:
        format_date = datetime.strptime(date, "%Y-%m-%d").date()
        today = datetime.today().date()
        result = ''
        if today > format_date:
            result = "The date entered is in the past"
        elif today < format_date:
            result = "The date entered is in the future"
        else:
            result = "The date entered is today"
        print(result)
        return result
    except ValueError:
        print('Error: Invalid date format. Please use format YYYY-MM-DD')
        return None


past_future('2024-04-05')
