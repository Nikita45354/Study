class Data:
    def __init__(self, data):
        self.data = data.split('-')

    @classmethod
    def type(cls, data):
        try:
            day, month, year = [int(i) for i in data.split('-')]
            return f"{type(day), day}\n{type(month), month}\n{type(year), year}"
        except ValueError:
            return 'неверная дата!'

    @staticmethod
    def valid(data):
        try:
            day, month, year = data.split('-')
            date(int(year), int(month), int(day))
            return 'Дата верна!'
        except ValueError:
            return 'неверная дата!'


print(Data.valid('15.03.2020'))
print(Data.type('25-02'))
