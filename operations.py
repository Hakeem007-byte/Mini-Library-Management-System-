GENRES = ("Fiction", "Non-Fiction", "Sci-Fi", "Romance", "Mystery")
books = {}
members = []
def find_member(member_id):
    for m in members:
        if m["member_id"] == member_id:
            return m
    return None

def add_book(isbn, title, author, genre, total_copies):
    if isbn in books:
        return "Book already exists."
    if genre not in GENRES:
        return "Invalid genre."
    books[isbn] = {
        "title": title,
        "author": author,
        "genre": genre,
        "total_copies": total_copies
    }
    return "Book added successfully."
def update_book(isbn, title=None, author=None, genre=None, total_copies=None):
    if isbn not in books:
        return "Book not found."
    if genre and genre not in GENRES:
        return "Invalid genre."
    if title:
        books[isbn]["title"] = title
    if author:
        books[isbn]["author"] = author
    if genre:
        books[isbn]["genre"] = genre
    if total_copies is not None:
        books[isbn]["total_copies"] = total_copies
    return "Book updated successfully."
def delete_book(isbn):
    if isbn not in books:
        return "Book not found."

    for m in members:
        if isbn in m["borrowed_books"]:
            return "Cannot delete — book is currently borrowed."
    del books[isbn]
    return "Book deleted successfully."


def search_books(keyword):

    results = []
    for isbn, info in books.items():
        if keyword.lower() in info["title"].lower() or keyword.lower() in info["author"].lower():
            results.append((isbn, info))
    return results or "No matches found."


def add_member(member_id, name, email):

    if find_member(member_id):
        return "Member already exists."
    members.append({
        "member_id": member_id,
        "name": name,
        "email": email,
        "borrowed_books": []
    })
    return "Member added successfully."


def update_member(member_id, name=None, email=None):

    m = find_member(member_id)
    if not m:
        return "Member not found."
    if name:
        m["name"] = name
    if email:
        m["email"] = email
    return "Member updated successfully."


def delete_member(member_id):

    m = find_member(member_id)
    if not m:
        return "Member not found."
    if m["borrowed_books"]:
        return "Cannot delete — member still has borrowed books."
    members.remove(m)
    return "Member deleted successfully."
def borrow_book(member_id, isbn):

    m = find_member(member_id)
    if not m:
        return "Member not found."
    if isbn not in books:
        return "Book not found."
    if len(m["borrowed_books"]) >= 3:
        return "Borrow limit reached (max 3)."
    if books[isbn]["total_copies"] <= 0:
        return "No copies available."
    books[isbn]["total_copies"] -= 1
    m["borrowed_books"].append(isbn)
    return f"{books[isbn]['title']} borrowed successfully."
def return_book(member_id, isbn):

    m = find_member(member_id)
    if not m:
        return "Member not found."
    if isbn not in m["borrowed_books"]:
        return "Book not borrowed by member."
    m["borrowed_books"].remove(isbn)
    books[isbn]["total_copies"] += 1
    return f"{books[isbn]['title']} returned successfully."