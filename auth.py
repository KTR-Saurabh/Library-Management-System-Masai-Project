# auth.py
import bcrypt
import datetime
from storage import read_csv, append_csv
from utils import get_data_file

def hash_password(password):
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt()).decode()

def verify_password(password, hashed):
    return bcrypt.checkpw(password.encode(), hashed.encode())

def register_member():
    members = read_csv('members.csv')
    member_id = input("Enter Member ID: ")
    if any(m['MemberID'] == member_id for m in members):
        print("❌ Member ID already exists.")
        return

    name = input("Enter Name: ")
    email = input("Enter Email: ")
    password = input("Enter Password: ")
    hashed_pw = hash_password(password)
    join_date = datetime.date.today().isoformat()

    new_member = {
        "MemberID": member_id,
        "Name": name,
        "PasswordHash": hashed_pw,
        "Email": email,
        "JoinDate": join_date
    }

    append_csv('members.csv', new_member, ['MemberID', 'Name', 'PasswordHash', 'Email', 'JoinDate'])
    print("✅ Member registered successfully.")

def login(role):
    if role == "librarian":
        password = input("Enter librarian password: ")
        # For demonstration, password is hardcoded. In production, handle securely.
        if password == "admin123":
            print("✅ Librarian login successful.")
            return {"role": "librarian"}
        else:
            print("❌ Incorrect librarian password.")
            return None
    elif role == "member":
        members = read_csv('members.csv')
        member_id = input("Enter Member ID: ")
        password = input("Enter Password: ")
        for member in members:
            if member["MemberID"] == member_id and verify_password(password, member["PasswordHash"]):
                print(f"✅ Welcome, {member['Name']}!")
                return member
        print("❌ Login failed. Check Member ID and Password.")
        return None