def analyze_vitory(analyze_player):

    for sequence in sequences:
        valid = 0

        for position in analyze_player:
            if position in sequence:
                valid += 1

        if valid == 3:
            return True

    return False


def hashtag(player_one, player_two):

    cont = 0

    for option in positions:

        cont += 1

        if option in player_one:
            option = 'X'
        elif option in player_two:
            option = 'O'

        print(f' {option} |', end='')
        if cont % 3 == 0:
            print('')

        
def choice(player, what):

    while True:

        position = input(f'Player {what}, your position: ')

        if position.isdecimal():

            if int(position) in positions:
                position = int(position)

                if position not in moves:
                    moves.append(position)
                    player.append(position)

                if analyze_vitory(player):
                    print(f'Player {what} won')
                    return exit()
                
                return player

        print('Enter only available numbers')

positions = (1, 2, 3,
             4, 5, 6,
             7, 8, 9)

sequences = ((1, 2, 3),
             (1, 5, 9),
             (1, 4, 7),
             (2, 5, 8),
             (3, 6, 9),
             (3, 5, 7),
             (4, 5, 6),
             (7, 8, 9))

player_one, player_two, moves = [], [], []

hashtag(player_one, player_two)

while True:

    player_one = choice(player_one, 'one')

    hashtag(player_one, player_two)

    player_two = choice(player_two, 'two')

    hashtag(player_one, player_two)

