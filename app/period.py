from .formatted_month import FormattedMonth
from .formatted_duration import FormattedDuration


class Period:
 
    def __init__(self, month_from, month_to):
        self.month_from = month_from
        self.month_to = month_to

    def to_russian_string(self):
        from_str = FormattedMonth(self.month_from).to_russian_string()
        if self.month_to == 'present':
            to_str = 'по настоящее время'
        else:
            to_str = (FormattedMonth(self.month_to)).to_russian_string()
        return f'{from_str} - {to_str}'

    def to_english_string(self):
        from_str = self.__formatted_month_from().to_english_string()
        if self.month_to == 'present':
            to_str = 'Present'
        else:
            to_str = self.__formatted_month_to().to_english_string()
        return f'{from_str} - {to_str}'

    def to_russian_duration(self):
        return (FormattedDuration(self.__duration_in_months())).to_russian_string()

    def to_english_duration(self):
        return (FormattedDuration(self.__duration_in_months())).to_english_string()
    
    def __duration_in_months(self):
        return (self.__formatted_month_to().year - self.__formatted_month_from().year) * 12 + \
               (self.__formatted_month_to().month - self.__formatted_month_from().month) + 1
    
    def __formatted_month_from(self):
        return FormattedMonth(self.month_from)
    
    def __formatted_month_to(self):
        return FormattedMonth(self.month_to)
