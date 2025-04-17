import random

players = {
    "Player 1" : 0,
    "Player 2":0,
    "Player 3" : 0
}

players_history = {
    "Player 1" : [],
    "Player 2": [],
    "Player 3" : []
}

player_roll_dice_hist = {
     "Player 1" : [],
    "Player 2": [],
    "Player 3" : []
}

player_pos_history = {
     "Player 1" : [],
    "Player 2": [],
    "Player 3" : []
}

def print_board(n):
    board = [[" " for _ in range(n)] for _ in range(n)]
    position_map = {}
    for player, pos in players.items():
        if pos > 0:
            if pos not in position_map:
                position_map[pos] = []
            position_map[pos] = f"P{player.split()[1]}"
    num = 1
    for i in range(n):
        row = i
        for j in range(n):
            col = j if row % 2 == 0 else n-1-j
            title_lable = f"{num:02}"
            if num in position_map:
                player_str = position_map[num]
                board[row][col] = f"{player_str}({title_lable})"
            else:
                board[row][col] = title_lable
            num +=1

    for row in range(n-1,-1,-1):
        print(" | ".join(f"{cell:>6}" for cell in board[row]))
        print("-" *(n*8))

def roll_dice():
    return random.randint(1,6)

def check_position(players, current_player):
    flag = False
    cutted_player = None
    for i in players:
        if i != current_player:
            if players[current_player] == players[i]:
                flag = True
                cutted_player = i
    return flag, cutted_player
    
def check_winner(position, board_size):
    return position == board_size

def move_player(player, position, board_size, n):
    dice = roll_dice()
    player_roll_dice_hist[player].append(dice)
    print(f"{player} rolled the dice and got : {dice}")
    position += dice
    
    if position > board_size:
        position -= dice
    player_pos_history[player].append(position)
    print(f"{player} move to {position}")

    if position>0:
        row = (position -1) // n
        col = (position - 1) % n
        if row % 2 !=0 :
            col = n-1-col
        # players_history[player].append((row, col))
        players_history[player].append((col, row))

    return position

def display_hist(obj, name):
    print(name)
    for player, moves in obj.items():
        formatted = [f"{r}" for r in moves]
        print(f"{player} : {'->'.join(formatted)}")

def display_players_history(name):
    print(name)
    for player, moves in players_history.items():
        formatted = [f"({r},{c})" for r, c in moves]
        print(f"{player} : {'->'.join(formatted)}")

def play_game():
    n = int(input("Please enter the grid size"))
    board_size = n*n
    # print(board_size)
    print_board(n)
    turn = 0
    while True:
        current_player = list(players.keys())[turn % len(players)]
        # (input(f"Player {current_player}, Please press enter to play the game"))
        players[current_player] = move_player(current_player, players[current_player], board_size, n)
        val, cutted_player =  check_position(players, current_player)
        if val == True:
            print(f"{current_player} is at the position of {cutted_player}, so {cutted_player} moving to 0 again!")
            players[cutted_player] = 0
            # continue
        print_board(n)
        display_hist(player_roll_dice_hist, "Roll dice history")
        display_hist(player_pos_history, "Position history")
        display_players_history("cordinates histort")
        if check_winner(players[current_player], board_size):
            print(f"{current_player} won the game!")
            break
        turn+=1
        print("*"*70)

if __name__ == "__main__":
    play_game()

# harjas@ascendeum.com

