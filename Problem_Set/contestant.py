class Contestant:
    def __init__(self, fname, lname, dob):
        self.first_name = fname
        self.last_name = lname
        self.dob = dob
        self.id = self.first_name + self.last_name + self.dob
