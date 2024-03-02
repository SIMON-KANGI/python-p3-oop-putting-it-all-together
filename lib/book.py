class Book:
    def __init__(self, title="River and the Source", page_count=69):
        self._title = title
        self._page_count = page_count
        self._turn_page = 0  
        
    @property
    def title(self):
        return self._title
    
    @title.setter   
    def title(self, title):
        self._title = title
        
    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter   
    def page_count(self, page_count):
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            print("page_count must be an integer")
            
     
    def turn_page(self):
        self._turn_page = 1
        print("Flipping the page...wow, you read fast!")
    
book = Book(title="River and the Source", page_count=69)

book.title = "The Rational Male"
book.page_count = 1000

print(book.title)
print(book.page_count)


book.turn_page = 3
