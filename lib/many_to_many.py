
class Book:
    all_books = []

    def __init__(self, title):
        self.title = title
        self.all_books.append(self)

    @classmethod
    def get_all_books(self):
        return self.all_books
    

class Author:
    all_authors = []

    def __init__(self, name, author_contracts=[]):
        self.name = name
        self.all_authors.append(self)
        self.author_contracts = author_contracts
    
    
    def contracts(self):
        return self.author_contracts
    
    #incorrect/not working
    def books(self):
        related_books = []
        for contract in self.author_contracts:
            related_books.append(contract.book)
        return related_books

    def add_contracts(self, contract):
        self.author_contracts.append(contract)



class Contract:

    all_contracts = []

    def __init__(self, author, book, date, royalties=0):
       
        if not isinstance(author, Author):
            raise Exception("Invalid author")
        if not isinstance(book, Book):
            raise Exception("Invalid book")
        if not isinstance(date, str):
            raise Exception("Invalid date")
        if not isinstance(royalties, int) and not isinstance(royalties, float):
            raise Exception("Invalid royalties")
       
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self.all_contracts.append(self)

    @classmethod
    def get_all_contracts(self):
        return self.all_contracts
    
    
     