class Book:

    def __init__(self, title, author, pages):
        
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __len__(self):
        return self.pages

    def __del__(self):
        print(f"{self.title} by {self.author} has been deleted from your computer's memory")


my_book = Book('Learn Python', 'AbstractGhoul05', 250)
print(my_book)
print(len(my_book))
del my_book
