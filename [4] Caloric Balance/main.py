import caloric_balance
import sys


def formatMenu():
    return ['What would you like to do?', '[f] Record Food Consumption', '[a] Record Physical Activity', '[q] Quit']


def formatMenuPrompt():
    return 'Enter an option: '


def formatActivityMenu():
    return ['Choose an activity to record', '[j] Jump rope', '[r] Running', '[s] Sitting', '[w] Walking']


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


def createCaloricBalance():
    gender = getUserString('Please specfy your gender [m/f]: ')
    age = getUserFloat('Please enter your age: ')
    height = getUserFloat('Please enter your height: ')
    weight = getUserFloat('Please enter your weight: ')
    return caloric_balance.CaloricBalance(gender, age, height, weight)


def recordActivityAction(caloric_bal):
    for item in formatActivityMenu():
        print(item)
    user_input = getUserString(formatMenuPrompt())
    if user_input == 'j':
        minutes = getUserFloat('For how many minutes did you perform this activity? ')
        caloric_bal.recordActivity(.074, minutes)
        print('Awesome! Your caloric balance is now ' + str(caloric_bal.balance))
    if user_input == 'r':
        minutes = getUserFloat('For how many minutes did you perform this activity? ')
        caloric_bal.recordActivity(.095, minutes)
        print('Awesome! Your caloric balance is now ' + str(caloric_bal.balance))
    if user_input == 's':
        minutes = getUserFloat('For how many minutes did you perform this activity? ')
        caloric_bal.recordActivity(.009, minutes)
        print('Awesome! Your caloric balance is now ' + str(caloric_bal.balance))
    if user_input == 'w':
        minutes = getUserFloat('For how many minutes did you perform this activity? ')
        caloric_bal.recordActivity(.036, minutes)
        print('Awesome! Your caloric balance is now ' + str(caloric_bal.balance))
    else:
        print('Invalid Argument')
        return


def eatFoodAction(caloric_bal):
    calories = getUserFloat('How many calories did you eat: ')
    caloric_bal.eatFood(calories)
    print('Your caloric balance is now ' + str(caloric_bal.balance))


def quitAction(caloric_bal):
    print('Bye! See you next time!')
    sys.exit(0)


def applyAction(caloric_bal, action):
    if action == 'f':
        eatFoodAction(caloric_bal)
    elif action == 'a':
        recordActivityAction(caloric_bal)
    elif action == 'q':
        quitAction(caloric_bal)
    else:
        print('Invalid Input')


def main():
    createCaloricBalance()
    while True:
        for item in formatMenu():
            print(item)
        action = getUserString(formatMenuPrompt())
        applyAction(caloric_balance, action)


if __name__ == '__main__':
    main()
