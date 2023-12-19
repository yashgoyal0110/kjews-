def save_contact(name, phone):
    with open("contacts.txt","r+") as file:
        file.write(f"{name}/n{phone}")
