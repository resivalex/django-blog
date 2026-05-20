import calendar
import datetime


class FormattedMonth:

    def __init__(self, value):
        if value == 'present':
            today = datetime.date.today()
            self.year = today.year
            self.month = today.month
        else:
            parts = value.split('.')
            self.year = int(parts[0])
            self.month = int(parts[1])

    def to_string(self):
        return f'{calendar.month_name[self.month]} {self.year}'
