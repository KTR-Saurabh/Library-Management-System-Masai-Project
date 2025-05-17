# member_menu.py
from storage import read_csv
from utils import get_data_file


def search_books():
    books = read_csv('books.csv')
    keyword = input("Enter title or author keyword to search: ").lower()
    found = [book for book in books if keyword in book['Title'].lower() or keyword in book['Author'].lower()]

    if not found:
        print("No books found matching the keyword.")
        return

    print(f"\n{'ISBN':<15}{'Title':<30}{'Author':<25}{'Available':<10}")
    for book in found:
        print(f"{book['ISBN']:<15}{book['Title']:<30}{book['Author']:<25}{book['CopiesAvailable']:<10}")
    print()


def borrow_book(member):
    books = read_csv('books.csv')
    isbn = input("Enter ISBN of the book you want to borrow: ")
    for book in books:
        if book['ISBN'] == isbn:
            if int(book['CopiesAvailable']) > 0:
                # Assuming issue_book function is imported or duplicated here
                from librarian_menu import issue_book
                issue_book()
                return
            else:
                print("❌ No copies available.")
                return
    print("❌ Book not found.")


def view_my_loans(member):
    loans = read_csv('loans.csv')
    my_loans = [loan for loan in loans if loan['MemberID'] == member['MemberID']]

    if not my_loans:
        print("You have no loan records.")
        return

    print("\n=== My Loans ===")
    print(f"{'LoanID':<10}{'ISBN':<15}{'IssueDate':<12}{'DueDate':<12}{'ReturnDate':<12}")
    for loan in my_loans:
        return_date = loan['ReturnDate'] if loan['ReturnDate'] else "Not returned"
        print(f"{loan['LoanID']:<10}{loan['ISBN']:<15}{loan['IssueDate']:<12}{loan['DueDate']:<12}{return_date:<12}")
    print()


def member_menu(data_dir, member):
    while True:
        print(f"""
=== Welcome {member['Name']} ===
1. Search Books
2. Borrow Book
3. My Loans
4. Logout
""")
        choice = input("> ")
        if choice == "1":
            search_books()
        elif choice == "2":
            borrow_book(member)
        elif choice == "3":
            view_my_loans(member)
        elif choice == "4":
            print("Logging out...")
            break
        else:
            print("❌ Invalid choice. Please try again.")