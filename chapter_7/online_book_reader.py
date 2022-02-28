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


def example():
    i = 0
    book_content = []
    for x in range(1, 300):
        content = f'Page {x}'
        if x % 30 == 0:
            i += 1
            content = f"Chapter {i}"

        page = Page(content, x)
        book_content.append(page)
        
    book = Book('Author', 'Title', len(book_content), book_content)
    book.open_book()
    print(book.next_page())
    print(book.next_page())
    print(book.next_chapter())
    print(book.flip_to_page(123))
    print(book.prev_page())
    print(book.prev_chapter())
    book.close_book()


if __name__ == "__main__":
    example()