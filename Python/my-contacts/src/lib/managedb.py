import pathlib
import json

class Managebd:
    __address_file = "{0}/src/db/dbContacts.json".format(pathlib.Path().absolute())
    def read_contact(self):
        with open(self.__address_file, "r") as data:
            return json.loads(data.read())
    
    def write_contact(self, new_data):
        with open(self.__address_file, "w") as data:
            data.write(json.dumps(new_data))