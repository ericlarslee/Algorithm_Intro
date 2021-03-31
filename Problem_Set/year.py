from months import Month


def year_function():
    temp_year = Year()
    year = tuple(temp_year.month_list)

    entry = int(input('which number month are you looking for a holiday in?')) - 1
    if year[entry].holidays is not None:
     print(f'{year[entry].name} has {year[entry].holiday_name} on {year[entry].holidays}')
    else:
     print('this month does not have holidays')



class Year:
    def __init__(self):
        self.month_list = []
        self.make_month_list()


    def make_month_list(self):
        self.month_list.append(Month("January", 1, 31, None, None))
        self.month_list.append(Month("February", 2, 28, None, None))
        self.month_list.append(Month("March", 3, 31, 14, "Pi Day"))
        self.month_list.append(Month("April", 4, 30, None, None))
        self.month_list.append(Month("May", 5, 31, None, None))
        self.month_list.append(Month("June", 6, 30, None, None))
        self.month_list.append(Month("July", 7, 31, None, None))
        self.month_list.append(Month("August", 8, 31, None, None))
        self.month_list.append(Month("September", 9, 30, None, None))
        self.month_list.append(Month("October", 10, 31, None, None))
        self.month_list.append(Month("November", 11, 30, None, None))
        self.month_list.append(Month("December", 12, 31, None, None))

    def find_holiday(self, entry):
        search = entry
        while True:
            print(f'{self.month_list[search].name} has {self.month_list[search].holiday_name}')



