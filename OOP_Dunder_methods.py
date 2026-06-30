class Book:
    def __init__(self,title,author,year_of_publication,num_pages):
        self.title = title
        self.author = author
        self.year_of_publication = year_of_publication
        self.num_pages = num_pages
    def __str__(self):
        return f"'{self.title}' by {self.author}"
    def __eq__(self,other):
        return self.title == other.title and self.author == other.author
    def __lt__(self,other):
        return self.num_pages < other.num_pages
    def __gt__(self,other):
        return self.num_pages > other.num_pages
    def __add__(self,other):
        return f"{self.num_pages + other.num_pages}"
    def __contains__(self,keyword):
        return keyword in self.title or keyword in self.author
    def __getitem__(self,key):
        if key == "title":
            return self.title
        elif key == "author":
            return self.author
        elif key == "num_pages":
            return self.num_pages
        else:
            return f"key '{key}' was not found"
book1 = Book("Atomic Habits","James Clear",2018,320)
book2 = Book("The Pragmatic Programmer","Andrew Hunt",1999,352)
book3 = Book("Clean Code","Robert C. Martin",2008,464)
print(book1)
print(book2)
print(book3)
print(book3 > book2)
print(book2 + book3)
print("----------")
print(book1['title'])
print(book1['author'])
print(book1['num_pages'])
print("----------")
print(book2['title'])
print(book2['author'])
print(book2['num_pages'])
print("----------")
print(book3['title'])
print(book3['author'])
print(book3['num_pages'])
