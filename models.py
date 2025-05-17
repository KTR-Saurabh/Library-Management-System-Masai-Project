# models.py
from dataclasses import dataclass

@dataclass
class Book:
    ISBN: str
    Title: str
    Author: str
    CopiesTotal: int
    CopiesAvailable: int

@dataclass
class Member:
    MemberID: str
    Name: str
    PasswordHash: str
    Email: str
    JoinDate: str

@dataclass
class Loan:
    LoanID: str
    MemberID: str
    ISBN: str
    IssueDate: str
    DueDate: str
    ReturnDate: str