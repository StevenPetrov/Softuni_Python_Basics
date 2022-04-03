needed_book = input()
book_checked = 0

while True:
    book_check = input()
    if book_check == needed_book:
        print(f"You checked {book_checked} books and found it.")
        break
    elif book_check == 'No More Books':
        print(f"The book you search is not here!")
        print(f"You checked {book_checked} books.")
        break
    else:
        book_checked += 1
        continue