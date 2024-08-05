
class Book:
    all_books = []

    def __init__(self, title):
        self.title = title
        self.all_books.append(self)

    @classmethod
    def get_all_books(self):
        return self.all_books
    
    def contracts(self):
        return [contract for contract in Contract.get_all_contracts() if contract.book == self]
    
    def authors(self):
        return [contract.author for contract in self.contracts()]

class Author:
    all_authors = []

    def __init__(self, name, author_contracts=None):
        self.name = name
        self.all_authors.append(self)
        self.author_contracts = author_contracts or []

    def contracts(self):
        return self.author_contracts
    
    def add_contracts(self, contract):
        self.author_contracts.append(contract)

    def books(self):
        return [contract.book for contract in self.author_contracts]

    def sign_contract(self, book, date, royalties):
        contract = Contract(self, book, date, royalties)
        self.add_contracts(contract)
        return contract
    
    def total_royalties(self):
        return sum(contract.royalties for contract in self.author_contracts)

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

        author.add_contracts(self)

    @classmethod
    def get_all_contracts(cls):
        return cls.all_contracts
    
    @classmethod
    def contracts_by_date(cls, date):
        return sorted(cls.all_contracts, key=lambda contract: contract.date)

   