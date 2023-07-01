from collections import UserDict


class AddressBook(UserDict):
    
    def __init__(self) -> None:
        pass

    def add_record(self, Record):
        self.data[Record.name.value] = Record


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

    def __init__(self) -> None:
        pass


class Name(Field):

    def __init__(self, value) -> None:
        self.value = value


class Phone(Field):

    def __init__(self, value) -> None:
        self.value = value

