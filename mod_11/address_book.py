from collections import UserDict
from datetime import date


class AddressBook(UserDict):
    
    def add_record(self, record):
        self.data[record.name.value] = record

    def iterator(self, step=5):
        data = list(self.data.values())
        while data:
            res = data[:step]
            data = data[step:]
            yield res


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
