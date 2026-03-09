# Dunder (Magic) Methods — __str__, __repr__, __len__, __eq__, __lt__
# "Dunder" = Double UNDERscore on both sides
# Python calls these automatically in certain situations
# They let your custom objects work like built-in types

# ============================================================
# The Problem without dunder methods
# ============================================================

class BookBad:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

bad_book = BookBad("Python Crash Course", "Eric Matthes", 544)
print(bad_book)
# Output: <__main__.BookBad object at 0x...> — useless!
# We can't compare, print meaningfully, or use len()

# ============================================================
# The Solution — implementing dunder methods
# ============================================================

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    # __str__ — called by print() and str()
    # Should return a human-friendly, readable string
    def __str__(self):
        return f"'{self.title}' by {self.author}"

    # __repr__ — called in the Python shell and for debugging
    # Should return an unambiguous, developer-friendly string
    # Ideally: enough info to recreate the object
    def __repr__(self):
        return f"Book(title='{self.title}', author='{self.author}', pages={self.pages})"

    # __len__ — called by len()
    def __len__(self):
        return self.pages

    # __eq__ — called by the == operator
    # Two books are equal if they have the same title and author
    def __eq__(self, other):
        return self.title == other.title and self.author == other.author

    # __lt__ — called by the < operator (less than)
    # Compare books by number of pages
    def __lt__(self, other):
        return self.pages < other.pages

    # __gt__ — called by the > operator (greater than)
    def __gt__(self, other):
        return self.pages > other.pages


book1 = Book("Python Crash Course", "Eric Matthes", 544)
book2 = Book("Automate the Boring Stuff", "Al Sweigart", 504)
book3 = Book("Python Crash Course", "Eric Matthes", 544)  # same as book1

# __str__ — used by print()
print(book1)                        # 'Python Crash Course' by Eric Matthes
print(str(book1))                   # same

# __repr__ — used by repr() and shown in the Python REPL
print(repr(book1))                  # Book(title='Python Crash Course', ...)

# __len__ — used by len()
print(len(book1))                   # 544
print(len(book2))                   # 504

# __eq__ — used by ==
print(book1 == book3)               # True  (same title and author)
print(book1 == book2)               # False

# __lt__ and __gt__ — used by < and >
print(book2 < book1)                # True  (504 < 544)
print(book1 > book2)                # True  (544 > 504)

# Because we defined __lt__, we can sort a list of Book objects
books = [book1, book2]
books.sort()                        # sorts by pages (shortest first)
for book in books:
    print(book)

# ============================================================
# Summary — which dunder triggers which operation
# ============================================================
# __str__   → print(obj), str(obj)
# __repr__  → repr(obj), shown in Python shell
# __len__   → len(obj)
# __eq__    → obj1 == obj2
# __lt__    → obj1 <  obj2
# __gt__    → obj1 >  obj2
# __add__   → obj1 +  obj2
# __init__  → Book(...)  — the constructor
