class Book:
    def __init__(self,author,title,num_of_pages) -> None:
        self.author = author
        self.title = title
        self.num_of_pages = num_of_pages

    def __str__(self):
        return f"\tAuthor:{self.author}\t Title:{self.title}\t NumPages:{self.num_of_pages}"

