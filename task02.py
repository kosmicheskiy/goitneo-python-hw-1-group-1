def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    if(name in contacts):
        contacts[name] = phone
        return "Contact updated."
    else:
        return "Contact cannot be changed, try to add contact first"
    
def show_phone(name, contacts):      
    if(name in contacts):
        phone = contacts[name]
        return phone
    else:
        return "Contact cannot be shown, try to add contact first"
    
def show_all(contacts):
    if (len(contacts) > 0):
        return str(contacts)
    else:
        return "No contacts found"
        

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
            print(show_phone(args, contacts))     
        elif command == "all":
            print(show_all(contacts))   
        elif (command in {"close", "exit"}):
            print("Good bye!")
            break
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
