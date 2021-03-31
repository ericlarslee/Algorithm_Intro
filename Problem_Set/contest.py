from contestant import Contestant
import random


def winner(entry_list):
    winner_temp = random.choice(list(entry_list.items()))
    return winner_temp


def sweet_steak():
    name_dict = Contest()
    name_dict = name_dict.contestant_list
    winner_id = list(winner(name_dict))
    print(name_dict[winner_id].Contestant.first_name)


class Contest:
    def __init__(self):
        self.contestant_list = {}
        self.populate_dict()

    def populate_dict(self):
        temp_person = Contestant('Jon', 'Johnson', '01201960')
        self.contestant_list[temp_person.id] = {temp_person}
        temp_person = Contestant('Will', 'Willard', '03211983')
        self.contestant_list[temp_person.id] = {temp_person}
        temp_person = Contestant('Bill', 'Billiard', '05211943')
        self.contestant_list[temp_person.id] = {temp_person}
        temp_person = Contestant('Kelly', 'Kurba', '11281993')
        self.contestant_list[temp_person.id] = {temp_person}
        temp_person = Contestant('Will', 'Willard', '05291930')
        self.contestant_list[temp_person.id] = {temp_person}
        temp_person = Contestant('Zoomer', 'McGee', '01222001')
        self.contestant_list[temp_person.id] = {temp_person}
        return self.contestant_list
