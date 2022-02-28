# python3
# online_book_reader.py - BookShelf class takes in several Books, 
# which each have several page class that the user can read from.

import re


class Page:

    def __init__(self, page_content, page_num, prev_page=None, next_page=None):
        self.page_content = page_content
        self.page_num = page_num
        self.prev_page = prev_page
        self.next_page = next_page

    
class Book:

    def __init__(self, author, title, num_pages, content=None):
        self.author = author
        self.title = title
        self.num_pages = num_pages
        self.content = self._create_book(content)
        self.curr_page = None
        self.is_open = False

    def _create_book(self, content):
        
        for indx, page in enumerate(content):
            if indx == 0:
                page.prev_page = None
            else:
                page.prev_page = content[indx - 1]

            if indx == len(content) - 1:
                page.next_page = None
            else:
                page.next_page = content[indx + 1]
            
        return content    

    def open_book(self):

        if self.is_open == True:
            return self.curr_page.page_content
        else:
            self.is_open = True
            if self.content != None:
                if self.curr_page != None: 
                    return self.curr_page.page_content
                else:
                    self.curr_page = self.content[0]
            else:
                return print(f"This book: {self.title} does not have any content.")
        
        return self.curr_page.page_content

    def next_page(self):
        if self.is_open == False:
            self.open_book()
        self.curr_page = self.curr_page.next_page
        return self.curr_page.page_content
        
    def prev_page(self):
        if self.is_open == False:
            self.open_book()
        self.curr_page = self.curr_page.prev_page
        return self.curr_page.page_content

    def first_page(self):
        if self.is_open == False:
            self.open_book()
        self.curr_page = self.content[0]
        return self.curr_page.page_content
        
    def last_page(self):
        if self.is_open == False:
            self.open_book()
        self.curr_page = self.content[-1]
        return self.curr_page.page_content
    
    def flip_to_page(self, page):
        if self.is_open == False:
            self.open_book()
        self.curr_page = self.content[page - 1]
        return self.curr_page.page_content

    def next_chapter(self):
        if self.is_open == False:
            self.open_book()

        chapter_match = re.match('Chapter', self.curr_page.page_content)

        while chapter_match == None:
            self.curr_page = self.curr_page.next_page
            chapter_match = re.match('Chapter', self.curr_page.page_content)

        return self.curr_page.page_content

    def prev_chapter(self):
        if self.is_open == False:
            self.open_book()

        chapter_match = re.match('Chapter', self.curr_page.page_content)

        while chapter_match == None:
            self.curr_page = self.curr_page.next_page
            chapter_match = re.match('Chapter', self.curr_page.page_content)

        return self.curr_page.page_content

    def close_book(self):
        if self.is_open == True:
            self.is_open == False
        return print(f"Thank you for reading {self.title}.\nYou are currently on page {self.curr_page.page_num}.\n")


class BookShelf:
    all_books = []

    def __init__(self):
        self.num_books = 0
        
    def add_book(self, book):
        self.all_books.append(book)
        self.num_books += 1

        return print(f"Added {book.title} to the book shelf.")

    def remove_book(self, book_title):
        for indx, book in enumerate(self.all_books):
            if book.title == book_title:
                removed_book = self.all_books.pop(indx)
                self.num_books -= 1
                break
            
        return print(f"{removed_book.title} removed from book shelf.")

    def display_books(self):
        print(f"Book shelf contents: ")
        for book in self.all_books:
            print(f"Title: {book.title}")
            print(f"Author: {book.author}")
            print(f"Number of pages: {book.num_pages}")

    def num_of_books(self):
        return print(f"There are {self.num_books} books in the bookshelf.")

    def search_for_book_by_title(self, book_title):
        """
        Searches through bookshelf for title that matches and returns the book object.
        
        Ex: title_1 = book_shelf.search_for_book_by_title('Title 1')
        """
        for book in self.all_books:
            if book.title == book_title:
                found_book = book
                return found_book
        return print(f"{book_title} was not found in this book shelf.")

    def search_for_books_by_author(self, book_author):
        """
        Searches through bookshelf for title that matches and returns a list of books by that author.
        
        Ex: title_1 = book_shelf.search_for_book_by_title('Title 1')
        """
        books_by_author = []
        for book in self.all_books:
            if book.author == book_author:
                books_by_author.append(book)
        if len(books_by_author) != 0:        
            return books_by_author
        return print(f"There were no books found written by {book_author} in this book shelf.")
    





def example():
    i = 0
    book_shelf = BookShelf()
    book_content = []
    for x in range(1, 300):
        content = f'Page {x}'
        if x % 30 == 0:
            i += 1
            content = f"Chapter {i}"

        page = Page(content, x)
        book_content.append(page)


    for x in range(1, 11):

        book = Book(f'Author {x}', f'Title {x}', len(book_content), book_content)
        book.open_book()
        print(book.next_page())
        print(book.next_page())
        print(book.next_chapter())
        print(book.flip_to_page(123))
        print(book.prev_page())
        print(book.prev_chapter())
        book.close_book()

        
        book_shelf.add_book(book)

    book_11 = Book('Author 2', 'Title 11', len(book_content), book_content)
    book_12 = Book('Author 2', 'Title 12', len(book_content), book_content)
    book_shelf.add_book(book_11)
    book_shelf.add_book(book_12)

    book_shelf.display_books()
    book_shelf.remove_book('Title 4')   
    book_shelf.display_books()
    book_shelf.num_of_books()
    title_7 = book_shelf.search_for_book_by_title('Title 7')
    author_2_books = book_shelf.search_for_books_by_author('Author 2')
    print("Books written by Author 2:")
    for book in author_2_books:
        print(f"{book.title}")


if __name__ == "__main__":
    example()