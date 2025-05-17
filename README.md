# Library-Management-System-Masai-Project

📚 Library Management System (Console-Based)
This is a console-based mini library management system developed in Python. It uses CSV files for data storage and supports librarian and member roles, password-hashed authentication, book borrowing/returning, due date logic, and overdue reporting.

🚀 Features
👤 Roles
Librarian

Add/Delete Books

Register Members

Issue/Return Books

View Overdue Books

Member

Search Books

Borrow Books

View Loan History

🔐 Authentication
Secure password hashing using bcrypt.

Role-based login.

📂 CSV-Based Data Storage
books.csv

members.csv

loans.csv

⚙️ CRUD & Logic
14-day borrowing period.

Overdue detection.

Proper inventory updates during issue/return.

Input validation and error handling.

🗂️ Project Structure
graphql
Copy
Edit
LibraryManagementSystem/
│
├── auth.py              # User registration and login
├── librarian_menu.py    # Librarian actions
├── member_menu.py       # Member actions
├── models.py            # Dataclass models
├── storage.py           # CSV read/write helpers
├── utils.py             # Utilities (e.g., file path resolution)
├── test_issue_return.py # Unit test for issue/return logic
├── main.py              # Entry point with argparse support
├── data/                # Directory containing CSV files
│   ├── books.csv
│   ├── members.csv
│   └── loans.csv
📥 Installation & Setup
Clone this repository:

bash
Copy
Edit
git clone https://github.com/yourusername/library-system.git
cd library-system
Install required packages:

bash
Copy
Edit
pip install bcrypt pytest
Create a data directory and sample CSVs:

bash
Copy
Edit
mkdir data
touch data/books.csv data/members.csv data/loans.csv
Or unzip the provided Data.zip archive into the ./data directory.

🏁 Running the Application
bash
Copy
Edit
python main.py --data-dir ./data
This opens a text-based interface to log in as a librarian or member, register, and manage books and loans.

🧪 Running Tests
Use pytest to run the automated test suite:

bash
Copy
Edit
pytest test_issue_return.py
It ensures that issuing and returning a book correctly updates book availability.

📝 Sample CSV Schema
📘 books.csv

ISBN	Title	Author	CopiesTotal	CopiesAvailable
9780132350884	Clean Code	Robert C. Martin	5	3

👤 members.csv

MemberID	Name	PasswordHash	Email	JoinDate
1001	Ananya Singh	$2b$12$...Q3	ananya@mail.com	2025-05-10

📄 loans.csv

LoanID	MemberID	ISBN	IssueDate	DueDate	ReturnDate
42	1001	9780132350884	2025-05-15	2025-05-29	

⚠️ Validation Rules
Unique Member IDs

No negative book copies

Password match check

Valid ISBN checks

🛠️ Developer Notes
Uses argparse for --data-dir

All CSV operations go through storage.py

Passwords hashed via bcrypt

Code tested via pytest

📧 Contact
For any issues or suggestions, please contact: saurabhkatiyar8544@gmail.com
