RUS_TRANSLATIONS = {
   'year': {
     'one': 'год',
     'few': 'года',
     'many': 'лет'
   },
   'month': {
     'one': 'месяц',
     'few': 'месяца',
     'many': 'месяцев'
   }
}

EN_TRANSLATIONS = {
   'year': {
     'one': 'year',
     'many': 'years'
   },
   'month': {
     'one': 'month',
     'many': 'months'
   }
}


class FormattedDuration:

    def __init__(self, months):
        self.months = months

    def to_russian_string(self):
        months = self.months % 12
        years = int((self.months - months) / 12)
        parts = []
        if years > 0:
            parts.append(f'{years} {self.rus_year(years)}')
        if months > 0:
            parts.append(f'{months} {self.rus_month(months)}')

        return ' '.join(parts)

    def to_english_string(self):
        months = self.months % 12
        years = int((self.months - months) / 12)
        parts = []
        if years > 0:
            parts.append(f'{years} {self.en_year(years)}')
        if months > 0:
            parts.append(f'{months} {self.en_month(months)}')

        return ' '.join(parts)

    def rus_month(self, num):
        return RUS_TRANSLATIONS['month'][self.rus_count_category(num)]

    def en_month(self, num):
        return EN_TRANSLATIONS['month'][self.en_count_category(num)]

    def rus_year(self, num):
        return RUS_TRANSLATIONS['year'][self.rus_count_category(num)]

    def en_year(self, num):
        return EN_TRANSLATIONS['year'][self.en_count_category(num)]

    def rus_count_category(self, num):
        num = abs(num)
        if 10 < num % 100 < 20:
            return 'many'
        if num % 10 == 1:
            return 'one'
        if num % 10 in [2, 3, 4]:
            return 'few'

        return 'many'

    def en_count_category(self, num):
        if num == -1 or num == 1:
            return 'one'
        else:
            return 'many'
