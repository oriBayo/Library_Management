from Reader import Reader
from Service import Service
from Shelf import Shelf
from Book import Book

class Library:
    def __init__(self) -> None:
        self.__shelves = [Shelf() for i in range(3)] 
        self.__readers = []
        self.init_data()
    
    def init_data(self):
        data = Service.load_from_DB()
        self.library_decoder(data)

    def get_shelves(self):
        return self.__shelves

    def get_readers(self):
        return self.__readers

    def is_there_place_for_new_book(self):
        for shelf in self.__shelves:
            if not shelf.get_is_shelf_full:
                return True
        return False

    def add_new_book(self,book):
        if not self.is_there_place_for_new_book:            
            return False
        else:     
            for shelf in self.__shelves:
                if not shelf.get_is_shelf_full():
                    shelf.add_book(book)
                    return
    
    def delete_book(self,book_title):
        for shelf in self.__shelves:
            shelf.remove_book(book_title)
    
    def change_location(self,book1_title,book2_title):
        index_book1,index_book2 = -1,-1
        shelf_book1,shelf_book2 = -1,-1
        
        for index,shelf in enumerate(self.__shelves):
            book_titles = list(map(lambda book : book.title,shelf.get_books()))
            if book1_title in book_titles:
                shelf_book1 = index
                index_book1 = book_titles.index(book1_title)
           
            if book2_title in book_titles:
                shelf_book2 = index
                index_book2 = book_titles.index(book2_title)
       
        if -1 not in [index_book1,index_book2,shelf_book1,shelf_book2]:
            self.__change_location(index_book1,index_book2,shelf_book1,shelf_book2)
        else:
            return False

    def change_location_in_same_shelf(self,shelf_index,book1_index,book2_index):
        self.__shelves[shelf_index].replace_book(book1_index,book2_index) 


    def __change_location(self,index_book1,index_book2,index_shelf1,index_shelf2):

        book1 = self.__shelves[index_shelf1].get_books()[index_book1]
        book2 = self.__shelves[index_shelf2].get_books()[index_book2]
        
        self.__shelves[index_shelf1].get_books()[index_book1] = book2
        self.__shelves[index_shelf2].get_books()[index_book2] = book1

    def order_books(self):
        for shelf in self.__shelves:
            shelf.order_books()
    
    def register_reader(self,name,id):
        reader = Reader(id,name)
        self.__readers.append(reader)
    
    def remove_reader(self, reader_name):
        reader = list(filter(lambda reader : reader.get_name() == reader_name, self.__readers))
        if len(reader) > 0:
            self.__readers.remove(reader[0])

    def reader_read_book(self, book_title, reader_id):
        reader = list(filter(lambda reader : reader.get_id() == reader_id, self.__readers))
        if len(reader) > 0:
            reader[0].read_book(book_title)

    def search_by_author(self,author_name):
        books_by_author = []
        for shelf in self.__shelves:
            for book in shelf.get_books():
                if book.author == author_name:
                    books_by_author.append(book.title)
        return books_by_author

    def display_data(self):
        print()
        print("Reader")
        for reader in self.__readers:
            reader.display_reader()
        print("Books")
        for index,shelf in enumerate(self.__shelves):
            print(f"Shelf {index + 1}:")
            shelf.display_shelf()
        print()

    def library_encoder(self):
        library_json = {"shelves":[],"readers":[]}
        for shelf in self.__shelves:
            shelf_json = {
                "max_books":shelf.get_max_books(),
                "is_shelf_full":shelf.get_is_shelf_full()
                ,"books":[]
                }
            for book in shelf.get_books():
                shelf_json["books"].append(
                    {
                        "author":book.author,
                        "title": book.title,
                        "num_of_pages":book.num_of_pages
                    })
            library_json["shelves"].append(shelf_json)
        for reader in self.__readers:
            reader_json={
                "id":reader.get_id(),
                "name":reader.get_name(),
                "books":[]
                }
            for book in reader.get_books():
                reader_json["books"].append(book)
            library_json["readers"].append(reader_json)
        
        return library_json

    
    def library_decoder(self,json_file):
        shelves_json = json_file["shelves"]
        for index,shelf in enumerate(shelves_json):
            shelf_data = Shelf()
            shelf_data.set_is_shelf_full(shelf["is_shelf_full"])
            for book in shelf["books"]:
                book_data = Book(book["author"],book["title"],book["num_of_pages"])
                shelf_data.get_books().append(book_data)
            
            self.__shelves[index] = shelf_data
        
        readers_json = json_file["readers"]
        for reader in readers_json:
            readre_data = Reader(reader["id"],reader["name"])
            readre_data.get_books().extend(reader["books"])

            self.__readers.append(readre_data)
        