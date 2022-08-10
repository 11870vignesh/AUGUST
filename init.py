
class Library:
    def __init__(self , books):
        self.books = books

    def list_book(self):
        print("Available Books")
        for book in self.books:
            print(book)

    def borrow_book(self, borrow_book):
        if borrow_book in self.books:
            print("Get Your Book Now")
            self.book.remove(borrow_book)
        else:
            print("Book not Available")

    def receive_book(self,review_book):
        print("you Have Returned The book")
        self.books.append(receive_book)      

books = ['C++' , 'Java' , 'Maven']
o = Library(books)


msg = """
  1.Display Book
  2.Borrow Books
  3.Return Books
"""

while True:
    print(msg)
    ch= int(input("Enter your Choice = "))
    if ch==1:
        o.list_book()
    elif ch==2:
        book=input("Enter Book name to Borrow  ")
        o.borrow_book(book) 
    elif ch == 3:
        book=input("Enter Book Name to Return")
        o.receive_book(book)
    else:
        print("Thank You Come Again")
        quit()
