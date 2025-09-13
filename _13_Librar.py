class Library:
    def __init__(self):
        self.books = []
        self.no_of_books = 0

    def addBook(self, book):
        self.books.append(book)
        self.no_of_books = len(self.books)

    def ShowInfo(self):
        print(f"Libray Has {self.no_of_books} Books. Books List : ")
        for i in self.books:
            print(i, end = "\n")

a = Library()
a.addBook("Harry Potter 1")
a.addBook("Harry Potter 2")
a.addBook("Harry Potter 3")
a.addBook("Harry Potter 4")
a.addBook("Harry Potter 5")
a.ShowInfo()




#     books = ["Atomic Habit", "Show Your Work", "Linux Basix For Hacker", "Sapiens", "Chess Basic"]
#     no_of_books = 5

#     def info(self):
#         print(f"Total Number of Books is {self.no_of_books} and Book name are {self.books}")

#     def check(self):
        
#         if self.no_of_books == len(self.books):
#             print("Correct Library")
#         else:
#             print("Wrong Library")

# a = Library()
# a.check()
# a.info()

