# Library management ststem 

class Library:
    BooksNo = 0

    def __init__(self):
        self.books = []

    def addBook(self, book):
        self.books.append(book)
        self.BooksNo=len(self.books)

    def showbook(self):
        print(f"The library has {self.BooksNo} books. The books are")
        for book in self.books:
         print(book)


l1 = Library()
l1.addBook(input("add a book:"))
l1.addBook(input("add a book:"))
l1.addBook(input("add a book:"))
l1.showbook()