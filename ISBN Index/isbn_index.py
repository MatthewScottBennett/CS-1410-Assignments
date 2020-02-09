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
    user_input = input(input_prompt)
    while user_input == '':
        user_input = input(input_prompt)
    return user_input.strip()


def getISBN():
    return


def getTitle():
    return


def recordBookAction(index):
    return


def findBookAction(index):
    return


def listBooksAction(index):
    return


def quitAction(index):
    return


def applyAction(index):
    return


def main():
    return
