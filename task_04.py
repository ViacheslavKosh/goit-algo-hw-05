def input_error(func):                  # Додаємо функцію декоратор для обробки вийнятків
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."
        except KeyError:
            return "There is no such name in my contacts."
        except IndexError:
            return "Give me a contact name please"
    return inner

def parse_input(user_input):
    command, *args = user_input.split()
    command = command.strip().lower()
    return command, *args

@input_error                            # Використовуємо для функції декоратор
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

@input_error                            # Використовуємо для функції декоратор
def change_contact(args, contacts):
    name, phone = args
    if name not in contacts:
        print(f"There is no such name {name} in contacts. Contact was added.")
    contacts[name] = phone
    return "Contact updated successfully."

@input_error                            # Використовуємо для функції декоратор
def show_contact(args, contacts):
        name = args[0]
        return contacts[name]
    
def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break

        elif command == "hello":
            print("How can I help you?")

        elif command == "add":
            print(add_contact(args, contacts))
            
        elif command == "change":
            print(change_contact(args, contacts))

        elif command == "phone":
            print(show_contact(args, contacts))
        
        elif command == "all":
            print(f'All contacts: {contacts}')
        
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()