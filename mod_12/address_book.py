from collections import UserDict
from datetime import date
import pickle


class AddressBook(UserDict):

    filename = 'addressbook.dump'

    def add_record(self, record):
        self.data[record.name.value] = record

    def iterator(self, step=5):
        data = list(self.data.values())
        while data:
            res = data[:step]
            data = data[step:]
            yield res

    def save_to_file(self):
        with open(self.filename, "wb") as file:
            pickle.dump(self, file)

    def read_from_file(self):
        with open(self.filename, "rb") as file:
            content = pickle.load(file)
        return content

    def find(self, string):
        res = []
        for k, v in self.data.items():
            if k.find(string) >= 0:
                res.append((k, v)) 
            else:
                for phone in v.phones:
                    if phone.find(string):
                        res.append((k, v))
        return res


class Record:
    
    def __init__(self, name):
        self.name = name
        self.phones = []
        self.birthday = None

    def add_phone(self, phone):
        self.phones.append(phone)

    def edit_phone(self, phone, new_phone):
        i = self.phones.index(phone)
        self.phones[i] = new_phone
    
    def del_phone(self, phone):
        self.phones.remove(phone)
    
    def add_birthday(self, birthday):
        self.birthday = birthday
    

    def days_to_birthday(self):
        if not self.birthday:
            return None
        cur_date = date.today()
        y = cur_date.year
        cur_birthday = self.birthday.replace(year=y)
        if cur_birthday < cur_date:
            cur_birthday = self.birthday.replace(year=y+1)
        days = cur_birthday - cur_date
        return days.days


class Field:

    def __init__(self):
        self.__value = None

    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value):
        self.__value = value


class Name(Field):
    pass


class Phone(Field):

    @property
    def value(self):
        return super().__value

    @value.setter
    def value(self, value):
        self.__value = self.sanitize_phone_number(value)

    def sanitize_phone_number(self, value):
        return (
            value.strip()
                .removeprefix("+")
                .replace("(", "")
                .replace(")", "")
                .replace("-", "")
                .replace(" ", "")
        )


class Birthday(Field):

    @property
    def value(self):
        return super().__value

    @value.setter
    def value(self, value):
        self.__value = date.fromisoformat(value)