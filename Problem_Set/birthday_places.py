def birthday_bash():
    birthday = populate_set()
    for location in birthday:
        print(location.location_name)

def populate_set():
    temp_list = [BirthdayLocale('Nogales'), BirthdayLocale('Power & Lights District'), BirthdayLocale('KCK'),
                     BirthdayLocale('Duluth'), BirthdayLocale('Mendota Heights'), BirthdayLocale('Tucson')]
    return set(temp_list)


class BirthdayLocale:
    def __init__(self, name):
        self.location_name = name
