import player


def getUserString(input_prompt):
    user_input = input(input_prompt)
    return user_input.strip()


def getUserInt(input_prompt):
    user_input = ''
    while user_input == '':
        user_input = input(input_prompt).strip()
        try:
            int(user_input)
            if int(user_input) <= 0:
                user_input = ''
        except ValueError:
            print('Invalid Arguments')
            user_input = ''
    return int(user_input)


def formatPrompt():
    return 'Enter a word to play (or press enter to pass) '


def getPlayers():
    player_count = getUserInt('How many players are there: ')
    player_list = []
    for i in range(1, player_count+1):
        player_name = getUserString('Enter in a name for Player #' + str(i) + ': ')
        player_list.append(player.Player(player_name))
    return player_list


def play(player_list):
    while True:
        for ply in player_list:
            print(ply.getName() + ', it is your turn!')
            print('Your letters are: ' + ply.printLetters())
            user_input = getUserString(formatPrompt())
            if user_input == '':
                letter = ply.drawLetter()
                print('You drew the letter: ' + letter + '\n')
            else:
                if ply.checkWord(user_input):
                    print('Great job!\n')
                else:
                    print('Check your letters and try again!\n')
                if not ply.getLetters():
                    print(ply.getName() + ' wins!')
                    return False


def main():
    print('Welcome! Time to play! Try to use all of your letters.')
    print('The first player that uses all of their letters wins!\n')
    player_list = getPlayers()
    print('\nGreat! Now we can play!\n')
    play(player_list)


if __name__ == '__main__':
    main()
