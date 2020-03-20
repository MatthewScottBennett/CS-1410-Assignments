import sys


def createIndex():
    return {}


def recordBook(index, book_isbn, book_title):
    index[book_isbn] = book_title


def findBook(index, book_isbn):
    if book_isbn in index:
        return index[book_isbn]
    else:
        return ''


def listBooks(index):
    book_list = []
    if index:
        i = 1
        for key in index:
            book_list.append(str(i) + ') ' + key + ': ' + index[key])
            i += 1
        return book_list
    else:
        return []


def formatMenu():
    return ['What would you like to do?', '[r] Record a Book', '[f] Find a Book', '[l] List all Books', '[q] Quit']


def formatMenuPrompt():
    return 'Enter an option: '


def getUserChoice(input_prompt):
    user_input = input(input_prompt).strip()
    while user_input == '':
        user_input = input(input_prompt).strip()
    return user_input


def getISBN():
    isbn = getUserChoice('Please enter an ISBN: ')
    return isbn


def getTitle():
    title = getUserChoice('Please enter a book title: ')
    return title


def recordBookAction(index):
    isbn = getISBN()
    title = getTitle()
    recordBook(index, isbn, title)
    return index


def findBookAction(index):
    isbn = getISBN()
    if isbn in index:
        print('Book Found: ' + findBook(index, isbn))
    else:
        print('Book not found!')


def listBooksAction(index):
    if index:
        booklist = listBooks(index)
        for book in booklist:
            print(book)
    else:
        print('No Books Found!')


def quitAction(index):
    print('Bye! See you next time!')
    sys.exit(0)


def applyAction(index, action):
    if action == 'r':
        recordBookAction(index)
    elif action == 'f':
        findBookAction(index)
    elif action == 'l':
        listBooksAction(index)
    elif action == 'q':
        quitAction(index)
    else:
        print('Invalid Input')


def main():
    index = createIndex()
    while True:
        for item in formatMenu():
            print(item)
        action = getUserChoice(formatMenuPrompt())
        applyAction(index, action)


if __name__ == '__main__':
    main()
