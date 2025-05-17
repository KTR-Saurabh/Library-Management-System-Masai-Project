# test_issue_return.py
import pytest
from storage import read_csv, write_csv, append_csv
from librarian_menu import issue_book, return_book
from utils import get_data_file
import os
import shutil


@pytest.fixture
def setup_test_environment():
    # Setup: create a temporary data directory
    test_dir = get_data_file('')
    backup_dir = test_dir + '_backup'
    if os.path.exists(test_dir):
        shutil.copytree(test_dir, backup_dir)
    os.makedirs(test_dir, exist_ok=True)

    # Create test CSV files
    write_csv('books.csv', [{
        "ISBN": "1234567890",
        "Title": "Test Book",
        "Author": "Author A",
        "CopiesTotal": 1,
        "CopiesAvailable": 1
    }], ['ISBN', 'Title', 'Author', 'CopiesTotal', 'CopiesAvailable'])

    write_csv('members.csv', [{
        "MemberID": "1001",
        "Name": "Test User",
        "PasswordHash": "$2b$12$KIXQ9bHZqJ5GqjP1y0.ePOs3eW8sVwq6zHjR6PuuKQQo5IuHLgZ4C",  # bcrypt hash for 'password'
        "Email": "test@example.com",
        "JoinDate": "2025-05-10"
    }], ['MemberID', 'Name', 'PasswordHash', 'Email', 'JoinDate'])

    write_csv('loans.csv', [], ['LoanID', 'MemberID', 'ISBN', 'IssueDate', 'DueDate', 'ReturnDate'])
    yield
    # Teardown: restore original data
    if os.path.exists(backup_dir):
        shutil.rmtree(test_dir)
        shutil.copytree(backup_dir, test_dir)
        shutil.rmtree(backup_dir)


def test_issue_and_return(setup_test_environment, monkeypatch):
    # Mock inputs for issuing a book
    inputs = iter(["1001", "1234567890"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    issue_book()

    loans = read_csv('loans.csv')
    assert len(loans) == 1
    assert loans[0]['MemberID'] == "1001"
    assert loans[0]['ISBN'] == "1234567890"
    assert loans[0]['ReturnDate'] == ""

    books = read_csv('books.csv')
    assert books[0]['CopiesAvailable'] == "0"

    # Mock inputs for returning a book
    inputs = iter([loans[0]['LoanID']])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    return_book()

    loans = read_csv('loans.csv')
    assert loans[0]['ReturnDate'] != ""

    books = read_csv('books.csv')
    assert books[0]['CopiesAvailable'] == "1"