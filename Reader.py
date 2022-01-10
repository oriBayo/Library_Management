import datetime
class Reader:
    def __init__(self, id, name) -> None:
        self.__id = id
        self.__name = name
        self.__books = []

    def read_book(self,book_title):       
        date = datetime.datetime.now().strftime('%x')
        self.__books.append({"title":book_title,"date":date})

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_id(self):
        return self.__id

    def set_id(self,id):
        self.__id = id

    def get_books(self):
        return self.__books
    
    def display_reader(self):
        print(f"name:{self.__name}")
        for book in self.__books:
            print(book)
