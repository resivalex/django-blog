class FormattedDuration:

    def __init__(self, months):
        self.months = months

    def to_string(self):
        months = self.months % 12
        years = int((self.months - months) / 12)
        parts = []
        if years > 0:
            parts.append(f'{years} {self.pluralize("year", years)}')
        if months > 0:
            parts.append(f'{months} {self.pluralize("month", months)}')

        return ' '.join(parts)

    def pluralize(self, word, num):
        return word if num == 1 else f'{word}s'
