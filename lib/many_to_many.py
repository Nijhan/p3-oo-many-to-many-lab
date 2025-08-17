class Book:
    all = []

    def __init__(self, title: str):
        if not isinstance(title, str):
            raise Exception("title must be a string")
        self.title = title
        Book.all.append(self)

    def contracts(self):
        return [c for c in Contract.all if c.book is self]

    def authors(self):
        return [c.author for c in self.contracts()]


class Author:
    all = []

    def __init__(self, name: str):
        if not isinstance(name, str):
            raise Exception("name must be a string")
        self.name = name
        Author.all.append(self)

    def contracts(self):
        return [c for c in Contract.all if c.author is self]

    def books(self):
        return [c.book for c in self.contracts()]

    def sign_contract(self, book, date, royalties):
        return Contract(self, book, date, royalties)

    def total_royalties(self):
        return sum(c.royalties for c in self.contracts())


class Contract:
    all = []

    def __init__(self, author, book, date, royalties):
        if not isinstance(author, Author):
            raise Exception("author must be an Author")
        if not isinstance(book, Book):
            raise Exception("book must be a Book")
        if not isinstance(date, str):
            raise Exception("date must be a string")
        if not isinstance(royalties, int):
            raise Exception("royalties must be an int")

        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties

        Contract.all.append(self)

    @classmethod
    def contracts_by_date(cls, date=None):
        """Return contracts sorted by date, or filtered by a given date."""
        sorted_contracts = sorted(cls.all, key=lambda c: c.date)
        if date:
            return [c for c in sorted_contracts if c.date == date]
        return sorted_contracts
