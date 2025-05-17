# main.py
import argparse
from auth import login, register_member
from librarian_menu import librarian_menu
from member_menu import member_menu

def main():
    parser = argparse.ArgumentParser(description="Library Management System")
    parser.add_argument('--data-dir', default='./data', help='Directory for CSV data files')
    args = parser.parse_args()

    print("== Welcome to the Library Management System ==")
    while True:
        print("""
Login as:
1. Librarian
2. Member
3. Register as Member
4. Exit
""")
        choice = input("> ")
        if choice == '1':
            user = login("librarian")
            if user:
                librarian_menu(args.data_dir)
        elif choice == '2':
            member = login("member")
            if member:
                member_menu(args.data_dir, member)
        elif choice == '3':
            register_member()
        elif choice == '4':
            print("Exiting the system. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.")

if _name_ == "_main_":
    main()