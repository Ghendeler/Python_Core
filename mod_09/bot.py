phone_book = {"John": '0953658952',
              "Mary": '9563215898',
              }


# decorator
def input_error(func):
    def inner(*args):
        try:
            result = func(*args)
        except IndexError:
            result = 'Wrong command'
        except ValueError:
            result = 'Give me name and phone please'
        except KeyError:
            result = 'Enter name please'
        return result
    return inner


def pars_request(string):
    key = None
    for i in ACTION.keys():
        if string.lower().startswith(i):
            key = i
            string = string[len(key):].strip()
            break   
    string = string.strip().split(' ') if len(string) else [0]
    if not key:
        return {}
    else:
        return {key: string[:2]}
  

@input_error
def hello(x):
    return "How can I help you?"


@input_error
def add(name=None, phone=None):
    if not name:
        raise KeyError
    elif not phone:
        raise ValueError
    phone_book[name] = phone
    return "Adding name and phone number"


@input_error
def change(name=None, phone=None):
    if not name:
        raise KeyError
    elif not phone:
        raise ValueError
    phone_book[name] = phone
    return "Change phone number"


@input_error
def phone(name=None):
    if not name:
        raise KeyError
    result = phone_book[name]
    return "Asked phone number " + result


@input_error
def show_all(x):
    result = ''
    for k, v in phone_book.items():
        result += f'{k}: {v}\n' 
    return result[:-2]


@input_error
def help(x):
    return '''"hello" for greating
"add"\n"change"\n"phone"
"show all"\n"help"
"good bye", "close" or "exit" for end'''

@input_error
def exit(x):
    raise SystemExit


ACTION = {
    "hello": hello,
    "add": add,
    "change": change,
    "phone": phone,
    "show all": show_all,
    "help": help,
    "good bye": exit,
    "close": exit,
    "exit": exit
}


def get_action_handler(action):
    return ACTION.get(action)


@input_error
def action(data):
    parsed = pars_request(data)
    if parsed == {}:
        raise IndexError
    for k, v in parsed.items():
        action_handler = get_action_handler(k)
        result = action_handler(*v)
    return result


def main():
    while True:
        r = input('> ')
        answer = action(r)
        print(answer)
    
    
if __name__ == "__main__":
    main()