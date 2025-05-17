# librarian_menu.py
from storage import read_csv, write_csv, append_csv
from models import Book, Loan
from utils import get_data_file
from datetime import datetime, timedelta


def add_book(data_dir):
    isbn = input("Enter ISBN: ")
    title = input("Enter Title: ")
    author = input("Enter Author: ")
    try:
        copies_total = int(input("Enter total copies: "))
        if copies_total < 0:
            raise ValueError
    except ValueError:
        print("❌ Invalid number of copies.")
        return

    books = read_csv('books.csv')
    for book in books:
        if book['ISBN'] == isbn:
            print("❌ Book with this ISBN already exists.")
            return

    new_book = {
        "ISBN": isbn,
        "Title": title,
        "Author": author,
        "CopiesTotal": copies_total,
        "CopiesAvailable": copies_total
    }
    append_csv('books.csv', new_book, ['ISBN', 'Title', 'Author', 'CopiesTotal', 'CopiesAvailable'])
    print("✅ Book added successfully.")


def remove_book():
    isbn = input("Enter ISBN of the book to remove: ")
    books = read_csv('books.csv')
    updated_books = [book for book in books if book['ISBN'] != isbn]
    if len(updated_books) == len(books):
        print("❌ Book not found.")
        return
    write_csv('books.csv', updated_books, ['ISBN', 'Title', 'Author', 'CopiesTotal', 'CopiesAvailable'])
    print("✅ Book removed successfully.")


def issue_book():
    member_id = input("Enter Member ID: ")
    isbn = input("Enter ISBN of the book to issue: ")
    books = read_csv('books.csv')
    for book in books:
        if book['ISBN'] == isbn:
            if int(book['CopiesAvailable']) > 0:
                book['CopiesAvailable'] = str(int(book['CopiesAvailable']) - 1)
                due_date = (datetime.today() + timedelta(days=14)).strftime('%Y-%m-%d')
                loan_id = str(int(datetime.now().timestamp()))
                new_loan = {
                    "LoanID": loan_id,
                    "MemberID": member_id,
                    "ISBN": isbn,
                    "IssueDate": datetime.today().strftime('%Y-%m-%d'),
                    "DueDate": due_date,
                    "ReturnDate": ""
                }
                append_csv('loans.csv', new_loan, ['LoanID', 'MemberID', 'ISBN', 'IssueDate', 'DueDate', 'ReturnDate'])
                write_csv('books.csv', books, ['ISBN', 'Title', 'Author', 'CopiesTotal', 'CopiesAvailable'])
                print(f"✔ Book issued successfully. Due on {due_date}.")
                return
            else:
                print("❌ No copies available.")
                return
    print("❌ Book not found.")


def return_book():
    loan_id = input("Enter Loan ID to return: ")
    loans = read_csv('loans.csv')
    books = read_csv('books.csv')
    for loan in loans:
        if loan['LoanID'] == loan_id and loan['ReturnDate'] == "":
            loan['ReturnDate'] = datetime.today().strftime('%Y-%m-%d')
            # Update book availability
            for book in books:
                if book['ISBN'] == loan['ISBN']:
                    book['CopiesAvailable'] = str(int(book['CopiesAvailable']) + 1)
                    break
            write_csv('loans.csv', loans, ['LoanID', 'MemberID', 'ISBN', 'IssueDate', 'DueDate', 'ReturnDate'])
            write_csv('books.csv', books, ['ISBN', 'Title', 'Author', 'CopiesTotal', 'CopiesAvailable'])
            print("✔ Book returned successfully.")
            return
    print("❌ Loan ID not found or already returned.")


def view_overdue():
    loans = read_csv('loans.csv')
    today = datetime.today().date()
    overdue_loans = [loan for loan in loans if
                     loan['ReturnDate'] == "" and datetime.strptime(loan['DueDate'], "%Y-%m-%d").date() < today]

    if not overdue_loans:
        print("No overdue loans.")
        return

    print("\n=== Overdue Loans ===")
    print(f"{'LoanID':<10}{'MemberID':<10}{'ISBN':<15}{'DueDate':<12}")
    for loan in overdue_loans:
        print(f"{loan['LoanID']:<10}{loan['MemberID']:<10}{loan['ISBN']:<15}{loan['DueDate']:<12}")
    print()


def librarian_menu(data_dir):
    while True:
        print("""
=== Librarian Dashboard ===
1. Add Book
2. Remove Book
3. Issue Book
4. Return Book
5. View Overdue List
6. Logout
""")
        choice = input("> ")
        if choice == "1":
            add_book(data_dir)
        elif choice == "2":
            remove_book()
        elif choice == "3":
            issue_book()
        elif choice == "4":
            return_book()
        elif choice == "5":
            view_overdue()
        elif choice == "6":
            print("Logging out...")
            break
        else:
            print("❌ Invalid choice. Please try again.")