class Shelf:
    def __init__(self) -> None:
        self.__maxBooks = 5
        self.__books = []
        self.__is_shelf_full = False
        

    def add_book(self, book):
        if len(self.__books) < self.__maxBooks:
            self.__books.append(book)
        elif len(self.__books) == self.__maxBooks:
            self.__is_shelf_full = True

    
    def replace_book(self,pos1,pos2):
        if  1 <= pos1 >= 5 and 1 <= pos2 >= 5 :
            try:
                temp = self.__books[pos1]
                self.__books[pos1] = self.__books[pos2]
                self.__books[pos2] = temp    
            except:
                print("Error - there are not book in this shelf")           
        else:
            print("Error - type invalid value")

    def order_books(self):
        self.__books.sort(key=lambda book : book.num_of_pages)

    def remove_book(self,book_title):
        for book in self.__books:
            if book.title == book_title:
                self.__books.remove(book)
                return
    
    def get_books(self):
        return self.__books

    def get_is_shelf_full(self):
        return self.__is_shelf_full
    
    def set_is_shelf_full(self,shelf_full):
        self.__is_shelf_full = shelf_full
    
    def get_max_books(self):
        return self.__maxBooks

    def set_max_books(self,max_books):
        self.__maxBooks = max_books

    def display_shelf(self):
        for book in self.__books:
            print(book)