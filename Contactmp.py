class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}"


class ContactManagementSystem:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        if name in self.contacts:
            print(f"Contact with name {name} already exists.")
        else:
            self.contacts[name] = Contact(name, phone)
            print(f"Contact {name} added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available.")
            return
        for contact in self.contacts.values():
            print(contact)

    def update_contact(self, name, new_phone):
        if name in self.contacts:
            self.contacts[name].phone = new_phone
            print(f"Contact {name} updated successfully.")
        else:
            print(f"Contact with name {name} does not exist.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact {name} deleted successfully.")
        else:
            print(f"Contact with name {name} does not exist.")

    def run(self):
        while True:
            print("\nContact Management System")
            print("1. Add Contact")
            print("2. View Contacts")
            print("3. Update Contact")
            print("4. Delete Contact")
            print("5. Exit")

            choice = input("Choose an option: ")
            if choice == '1':
                name = input("Enter contact name: ")
                phone = input("Enter contact phone: ")
                self.add_contact(name, phone)
            elif choice == '2':
                self.view_contacts()
            elif choice == '3':
                name = input("Enter contact name to update: ")
                new_phone = input("Enter new phone number: ")
                self.update_contact(name, new_phone)
            elif choice == '4':
                name = input("Enter contact name to delete: ")
                self.delete_contact(name)
            elif choice == '5':
                print("Exiting the system.")
                break
            else:
                print("Invalid option. Please try again.")


if __name__ == "__main__":
    cms = ContactManagementSystem()
    cms.run()