
Liste = []

def add_contact(name, phone_number, email):#done

    Liste.append(name)
    Liste.append(phone_number)
    Liste.append(email)


def display_contacts():#done
    for i in range(0,len(Liste),3):
        print(", ".join(Liste[i:i+3]))
        
    
def delete_contact(contact_to_be_deleted):#done
    
    a = Liste.index(contact_to_be_deleted)
    if "@" not in contact_to_be_deleted:
     Liste.pop(a+1)
     Liste.pop(a)
     Liste.pop(a-1)
    else:
       Liste.pop(a)
       Liste.pop(a-1)
       Liste.pop(a-2)

    display_contacts()
    
def search_contact(name):
    
    index = 0

    while index < len(Liste):
        if Liste[index] == name:
            print(Liste[index:index + 3])
        index += 1
        if name not in Liste:
            print(f"No {name} found.")
            break
        
    
def update_contact(contact_to_be_modified, new_name,new_phone_number, new_email):#done
    
    
    index = 0

    while index < len(Liste):
        if Liste[index] == contact_to_be_modified:
            if "@" in contact_to_be_modified:
                
                print(Liste[index-2:index+1])
                new_name = input("New name: ")
                new_phone_number = input("New number: ")
                new_email = input("New email: ")
                while '@' not in new_email:
                    new_email = input("email again: ")
                
                Liste[index -2] = new_name
                Liste[index - 1] = new_phone_number
                Liste[index] = new_email
                
            else:
                print(Liste[index-1:index+2])
                new_name = input("New name: ")
                new_phone_number = input("New number: ")
                new_email = input("New email: ")
                while '@' not in new_email:
                    new_email = input("email again: ")
                
                Liste[index -1] = new_name
                Liste[index] = new_phone_number
                Liste[index + 1] = new_email
            
        
        index += 1
        
        
        
    display_contacts()
        
        
def display_menu():
    print("\tWelcome to Contact System Management\nAdd Contact(1)\nDisplay Contact(2)\nDelete Contact(3)\nSearch Contact(4)\nUpdate Contact(5)")
    choice = int(input(""))
    
    while choice > 5 or choice < 1:
        choice = int(input("Invalid input. Please enter again: "))
        
    
    while choice >= 1 and choice <= 5:
        if choice == 1:
            print("\tAdd Contact Menu\n")
            name = input("Name; ")
            phone_number = input("number; ")
            email = input("email; ")
            while '@' not in email:
                email = input("email again: ")
            add_contact(name,phone_number,email)
            display_contacts()
            choice = int(input("Exit(0)"))
            if choice == 0:
                display_menu()
            break
        elif choice == 2:
            print("\tContacts\n")
            display_contacts()
            choice = int(input("Exit(0)"))
            if choice == 0:
                display_menu()
            break
        elif choice == 3:
            print("\tContacts\n")
            display_contacts()
            deleted = input("Contact that you want to delete (only number and email): ")
            delete_contact(deleted)
            choice = int(input("Exit(0)"))
            if choice == 0:
                display_menu()
            break
        elif choice == 4:
            print("\tSearching Menu\n")
            searched = input("Contact you looking for: ")
            print("Searching...\n")
            search_contact(searched)
            choice = int(input("Exit(0)"))
            if choice == 0:
                display_menu()
            break
        elif choice == 5:
            print("\tUpdate Menu\n")
            display_contacts()

            updated_name = ""
            updated_number = ""
            updated_email = ""

            updated_contact = input("Contact you want to change (only number and email): ")
            update_contact(updated_contact,updated_name,updated_number,updated_email)
            choice = int(input("Exit(0)"))
            if choice == 0:
                display_menu()
            break

display_menu()