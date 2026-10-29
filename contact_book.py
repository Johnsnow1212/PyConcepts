contact = {
    "John": ["672354", "john@gmail.com"],
    "Mauve": ["230987", "mauve@gmail.com"],
    "melissa": ["200312", "melissa@gmail.com"]
}

search = input("Enter name to search details: ")
found = False

for name in contact:
    if search.lower() == name.lower():
        print(f"Name: {name} \nPhone: {contact[name][0]} \nEmail: {contact[name][1]}")
        found = True
        break

if not found:
    print("Contact not found.")

    print(f"Name: {search} \nPhone: {phone} \nEmail: {email}")
