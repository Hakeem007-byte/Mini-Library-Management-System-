from operations import *
books.clear()
members.clear()
assert add_book("001", "OOP", "John Kargbo", "Non-Fiction", 3) == "Book added successfully."
assert add_book("001", "Duplicate", "Author", "Fiction", 2) == "Book already exists."
assert add_member("M001", "Tunde", "Tundejj23@mail.com") == "Member added successfully."
assert add_member("M001", "Keem Dup", "keem@mail.com") == "Member already exists."
assert borrow_book("M001", "001") == "OOP borrowed successfully."
assert borrow_book("M001", "999") == "Book not found."
assert return_book("M001", "001") == "OOP returned successfully."
assert delete_book("001") == "Book deleted successfully."
print("✅ All tests passed successfully!") 