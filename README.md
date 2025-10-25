 Mini Library Management System 
 Name : Abdul Hakeem G Kargbo 
 ID: 905005149
 Class: BIT1101 sem 3 
This project is a simple Mini Library Management System built in Python.  
It demonstrates the use of dictionaries, lists, and tuples, and implements all basic CRUD (Create, Read, Update, Delete) operations, as well as borrow and return functionalities for library members.

 Core Functionalities

| Function | Description |
|-----------|--------------|
| add_book() | Adds a new book if ISBN is unique and genre valid |
| add_member() | Adds a new library member |
| search_books() | Searches books by title or author |
| update_book() / update_member() | Updates record details |
| delete_book() / delete_member() | Deletes record if valid |
| borrow_book() | Allows members to borrow (max 3 books) |
| return_book() | Returns borrowed book and updates stock |
Testing

At least 5 tests are included in tests.py using assert:
- Adding a new book
- Borrowing a book
- Returning a book
- Borrowing with no available copies
- Deleting a borrowed book

Run:
bash
python tests.py
