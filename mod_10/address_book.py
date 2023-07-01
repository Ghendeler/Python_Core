from collections import UserDict


class AddressBook(UserDict):

    def add_record(self, record):
        self.data[record.name.value] = record


class Record:
    
    def __init__(self, name) -> None:
        self.name = name
        self.phones = []

    def add_phone(self, phone):
        pass

    def edit_phone(self, phone):
        pass
    
    def del_phone(self, phone):
        pass
    


class Field:
    pass


class Name(Field):

    def __init__(self, value) -> None:
        self.value = value


class Phone(Field):

    def __init__(self, value) -> None:
        self.value = value

