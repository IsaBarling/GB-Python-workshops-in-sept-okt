import json
class record:
    Lastname = ""
    FirstName = ""
    Telephone = ""
    Description = ""
    def __init__(self, lastname, firstname, tel, des):
        
        self.Lastname = lastname
        self.Firstname = firstname
        self.Telephone = tel
        self.Description = des
    def Show(self):
        print(self.Lastname + ", " + self.Firstname + ", " + self.Telephone + ", " + self.Description)
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)