seached_book = input()
book_counter = 0
next_book = input()
while next_book != "No More Books" and next_book != seached_book:
    book_counter += 1
    next_book = input()
if next_book == seached_book: #if book is found == True
         print(f"You checked {book_counter} books and found it.")
else:
         print("The book you search is not here!")
         print(f"You checked {book_counter} books.")