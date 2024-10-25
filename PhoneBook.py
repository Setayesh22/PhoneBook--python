class PhoneBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        self.contacts[name] = phone
        print(f"Contact {name} added with phone number {phone}.")

    def display_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return
        print("Contacts:")
        for name, phone in self.contacts.items():
            print(f"{name}: {phone}")

    def search_contact(self, name):
        if name in self.contacts:
            print(f"{name}: {self.contacts[name]}")
        else:
            print(f"Contact {name} not found.")

def main():
    phone_book = PhoneBook()

    while True:
        print("nMenu:")
        print("1. Add Contact")
        print("2. Display Contacts")
        print("3. Search Contact")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            phone_book.add_contact(name, phone)
        elif choice == '2':
            phone_book.display_contacts()
        elif choice == '3':
            name = input("Enter name to search: ")
            phone_book.search_contact(name)
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
