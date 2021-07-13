import datetime


MONTH_CODES = {
   1: 'january',
   2: 'february',
   3: 'march',
   4: 'april',
   5: 'may',
   6: 'june',
   7: 'july',
   8: 'august',
   9: 'september',
   10: 'october',
   11: 'november',
   12: 'december',
}

EN_MONTHS = {
   'january': 'January',
   'february': 'February',
   'march': 'March',
   'april': 'April',
   'may': 'May',
   'june': 'June',
   'july': 'July',
   'august': 'August',
   'september': 'September',
   'october': 'October',
   'november': 'November',
   'december': 'December',
}

RUS_MONTHS = {
   'january': 'Январь',
   'february': 'Февраль',
   'march': 'Март',
   'april': 'Апрель',
   'may': 'Май',
   'june': 'Июнь',
   'july': 'Июль',
   'august': 'Август',
   'september': 'Сентябрь',
   'october': 'Октябрь',
   'november': 'Ноябрь',
   'december': 'Декабрь',
}


class FormattedMonth:

    def __init__(self, str):
        if str == 'present':
            today = datetime.date.today()
            self.year = today.year
            self.month = today.month
        else:
            parts = str.split('.')
            self.year = int(parts[0])
            self.month = int(parts[1])

    def to_russian_string(self):
        return f'{RUS_MONTHS[MONTH_CODES[self.month]]} {self.year}'

    def to_english_string(self):
        return f'{EN_MONTHS[MONTH_CODES[self.month]]} {self.year}'
