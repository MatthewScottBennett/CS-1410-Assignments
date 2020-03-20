import sys


def milesPerGallon(miles, gallons):
    if gallons == 0:
        return 0
    return float(miles / gallons)


def createNotebook():
    return []


def recordTrip(notebook, date, miles, gallons):
    dictionary = {'date': date, 'miles': miles, 'gallons': gallons}
    notebook.append(dictionary)
    return notebook


def listTrips(notebook):
    formatted_notebook = []
    if notebook:
        for trip in notebook:
            formatted_notebook.append('On ' + trip['date'] + ': ' + str(trip['miles']) + ' miles traveled using ' +
                                      str(trip['gallons']) + ' gallons. Gas mileage: ' +
                                      str(milesPerGallon(trip['miles'], trip['gallons'])) + ' MPG')
    return formatted_notebook


def calculateMPG(notebook):
    if notebook:
        total_miles = 0.0
        total_gallons = 0.0
        for trip in notebook:
            total_miles += trip['miles']
            total_gallons += trip['gallons']
        return milesPerGallon(total_miles, total_gallons)
    return 0.0


def formatMenu():
    return ['What would you like to do?', '[r] Record Gas Consumption', '[l] List Mileage History',
            '[c] Calculate Gas Mileage', '[q] Quit']


def formatMenuPrompt():
    return 'Enter an option: '


def getUserString(input_prompt):
    user_input = input(input_prompt).strip()
    while user_input == '':
        user_input = input(input_prompt).strip()
    return user_input


def getUserFloat(input_prompt):
    user_input = ''
    while user_input == '':
        user_input = input(input_prompt).strip()
        try:
            float(user_input)
            if float(user_input) <= 0.0:
                user_input = ''
        except ValueError:
            print('Invalid Arguments')
            user_input = ''
    return float(user_input)


def getDate():
    date = getUserString('What is the date: ')
    return date


def getMiles():
    miles = getUserFloat('How many miles did you drive since last filling up: ')
    return miles


def getGallons():
    gallons = getUserFloat('How many gallons of gas did you add to your tank: ')
    return gallons


def recordTripAction(notebook):
    date = getDate()
    miles = getMiles()
    gallons = getGallons()
    recordTrip(notebook, date, miles, gallons)
    print('Saved!')


def listTripsAction(notebook):
    if notebook:
        notebooklist = listTrips(notebook)
        for trip in notebooklist:
            print(trip)
    else:
        print('No trips found!')


def calculateMPGAction(notebook):
    if notebook:
        print('Average gas mileage: ' + str(calculateMPG(notebook)) + ' MPG')
    else:
        print('No trips found!')


def quitAction(notebook):
    print('Bye! See you next time!')
    sys.exit(0)


def applyAction(notebook, action):
    if action == 'r':
        recordTripAction(notebook)
    elif action == 'l':
        listTripsAction(notebook)
    elif action == 'c':
        calculateMPGAction(notebook)
    elif action == 'q':
        quitAction(notebook)
    else:
        print('Invalid Input')


def main():
    notebook = createNotebook()
    while True:
        for item in formatMenu():
            print(item)
        action = getUserString(formatMenuPrompt())
        applyAction(notebook, action)


if __name__ == '__main__':
    main()
