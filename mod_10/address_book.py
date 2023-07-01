from collections import UserDict


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record


class Record:
    
    def __init__(self, name) -> None:
        self.name = name
        self.phones = []

    def add_phone(self, phone):
        self.phones.append(phone)

    def edit_phone(self, phone, new_phone):
        i = self.phones.index(phone)
        self.phones[i] = new_phone
    
    def del_phone(self, phone):
        self.phones.remove(phone)
    


class Field:
    pass


class Name(Field):

    def __init__(self, value) -> None:
        self.value = value


class Phone(Field):

    def __init__(self, value) -> None:
        self.value = value

