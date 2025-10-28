def main():
    """
    Main Function
    """
    contacts = {}
    print("Welcome to the assistant bot!")

    while True:
        user_input = input("Enter a command: ")
        command, args = parse_input(user_input)

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
            
        elif command is None: # for empty command
            continue

        else:
            print("Invalid command, please check available commands.")

def add_contact(args, contacts):
    """
    Add new contact to the dictionary
    2 and only 2 args expected: Name and phone number, separated by space
    All names are stored from capital
    """
    try:
        name, phone = args
        contacts[name.capitalize()] = phone
        return "Contact added."
    except ValueError:
        return "Invalid command. Usage: add [name] [phone]"

def change_contact(args, contacts):
    """
    Updates number for already existing contact.
    requires name and phone number.
    """
    try:
        name, phone = args
        name_cap = name.capitalize()
        if name_cap in contacts:
            contacts[name_cap] = phone
            return "Contact updated."
        else:
            return "Contact not found."
    except ValueError:
        return "Invalid command. Usage: change [name] [phone]"

def show_phone(args, contacts):
    """
    Shows phone number if requested contact exists.
    requires name, that matches with available in contacts.
    """
    try:
        name = args[0]
        name_cap = name.capitalize()
        if name_cap in contacts:
            return contacts[name_cap]
        else:
            return "Contact not found."
    except IndexError:
        return "Invalid command. Usage: phone [name]"

def show_all(contacts):
    """
    Shows all contacts and their numbers saved during session 
    """
    if not contacts:
        return "No contacts found."
    
    # Collecting data for display in row
    output_lines = []
    for name, phone in contacts.items():
        output_lines.append(f"{name}: {phone}")
    
    return "\n".join(output_lines)

def parse_input(user_input):
    """
    Divides input to commands and arguments.
    Commands are transformed to the lower register.
    """
    # stripping
    cleaned_input = user_input.strip()
    if not cleaned_input:
        return None, [] # None for empty inputs

    parts = cleaned_input.split()
    cmd = parts[0].lower()
    args = parts[1:]
    
    return cmd, args

if __name__ == "__main__":
    main()