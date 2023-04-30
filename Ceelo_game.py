"""
Name: John Lin  Username: jlin865   ID number: 775811935
Cee-lo game simulation. Simulates a full game of Cee-lo and ends giving the overall statistics.
"""

import random

def main():
    user_name = "jlin865" #Add your username here
    player_wins = 0
    computer_wins = 0
    draws = 0
    player_selection = 1
    display_banner(user_name)
    while player_selection != 0:
        print()
        display_menu()
        player_selection = get_user_input()
        if player_selection == 1:
            player_roll = get_valid_roll()
            computer_roll = get_valid_roll()
            player_score = get_score(player_roll)
            computer_score = get_score(computer_roll)
            print()
            print_separator()
            print_roll("Player", player_roll, player_score)
            print_roll("Computer", computer_roll, computer_score)
            if player_score > computer_score:
                print("Player has won!")
                player_wins += 1
            elif player_score < computer_score:
                print("Computer has won!")
                computer_wins += 1
            else:
                print("It's a draw!")
                draws += 1
            print("Player wins:", player_wins, "Computer wins:", computer_wins, "Draws:", draws)
            print_separator()
    print()
    print_separator()
    print_player_stats(player_wins, computer_wins, draws)
    print_separator()
       
#Paste your completed functions here
#Prints out a line separator
def print_separator():
    print(46 * '*')

#Prints our display banner including the users name
def display_banner(user_name):
    title = 'Cee-lo Game by ' + user_name
    print(len(title) * '*')
    print(title)
    print(len(title) * '*')

#Displaying the menu
def display_menu():
    menu = 'Please select an option:\nEnter 1 to play a Cee-lo game.\nEnter 0 to exit.'
    print(menu)

#Getting user input for menu and error checking
def get_user_input():
    user_input = int(input('Enter your selection: '))
    while user_input != 0 and user_input != 1:
        print('Make a valid selection!')
        user_input = int(input('Enter your selection: '))
    
    return user_input

#Rolls 3 dice and returns them as a string
def roll_three_dice():
    dice_roll_1 = random.randrange(1, 7)
    dice_roll_2 = random.randrange(1, 7)
    dice_roll_3 = random.randrange(1, 7)
    
    dice_string = str(dice_roll_1) + str(dice_roll_2) + str(dice_roll_3)
    
    return dice_string

#Checks if dice rolled is a 456, returns True or False
def is_456(dice_str):

    dice1 = int(dice_str[0])
    dice2 = int(dice_str[1])
    dice3 = int(dice_str[2])

    total = dice1 + dice2 + dice3
    smallest_dice = min(dice1, dice2, dice3)
    largest_dice = max(dice1, dice2, dice3)
    
    if smallest_dice == 4:
        if largest_dice == 6:
            if total - (smallest_dice + largest_dice) == 5:
                output = True
            else:
                output = False
        else:
            output = False
    else:
        output = False
    
    return output

#Checks if dice are 123, returns True or False
def is_123(dice_str):

    dice1 = int(dice_str[0])
    dice2 = int(dice_str[1])
    dice3 = int(dice_str[2])

    total = dice1 + dice2 + dice3
    smallest_dice = min(dice1, dice2, dice3)
    largest_dice = max(dice1, dice2, dice3)
    
    if smallest_dice == 1:
        if largest_dice == 3:
            if total - (smallest_dice + largest_dice) == 2:
                output = True
            else:
                output = False
        else:
            output = False
    else:
        output = False
    
    return output

#Checks if dice are the same (a triple), returns True or False
def is_trip(dice_str):
    
    dice1 = int(dice_str[0])
    dice2 = int(dice_str[1])
    dice3 = int(dice_str[2])
    
    if dice1 == dice2 and dice2 == dice3:
        output = True
    else:
        output = False
    
    return output

#Checks if theres two of the same dice, returns True or False
def is_point(dice_str):
    
    dice1 = int(dice_str[0])
    dice2 = int(dice_str[1])
    dice3 = int(dice_str[2])
    
    if dice1 == dice2 and dice1 != dice3:
        output = True
    elif dice1 == dice3 and dice2 != dice3:
        output = True
    elif dice2 == dice3 and dice1 != dice2:
        output = True
    else:
        output = False
        
    return output

#Checks if the dice rolled are given points(whether its a trips, point, 123, or 456)
def is_valid_roll(dice_str):
    if is_123(dice_str) == True:
        return True
    elif is_456(dice_str) == True:
        return True
    elif is_point(dice_str) == True:
        return True
    elif is_trip(dice_str) == True:
        return True
    else:
        return False

#Keeps rolling dice until a valid dice roll is rolled, returns dice rolled as a string
def get_valid_roll():
    dice_str = roll_three_dice()
    
    while is_valid_roll(dice_str) is False:
        dice_str = roll_three_dice()
    return dice_str

#Checks and outputs what type of dice the player has rolled
def type_of_roll(dice_str, player):
    if is_123(dice_str):
        output = player + ' has rolled a 123'
    elif is_456(dice_str):
        output = player + ' has rolled a 456'
    elif is_point(dice_str):
        output = player + ' has rolled a POINT'
    elif is_trip(dice_str):
        output = player + ' has rolled a TRIP'
    else:
        output = None
    return output

#Gives the points a player gets from a point roll
def get_point_score(dice_str):
    dice1 = int(dice_str[0])
    dice2 = int(dice_str[1])
    dice3 = int(dice_str[2])
    
    if dice1 == dice2:
        point = 10 + dice3
    elif dice2 == dice3:
        point = 10 + dice1
    elif dice1 == dice3:
        point = 10 + dice2
    
    return point

#Gives the points a player gets from a trip roll
def get_trip_score(dice_str):
    dice = int(dice_str[0])
    point = 20 + dice
    
    return point

#Gives the points a player gets from a their roll
def get_score(dice_str):
    if is_456(dice_str):
        return 30
    elif is_123(dice_str):
        return 0
    elif is_point(dice_str):
        return get_point_score(dice_str)
    elif is_trip(dice_str):
        return get_trip_score(dice_str)

#Prints out the score at the end of the round
def print_roll(player_name, player_roll, player_score):
    roll_type = type_of_roll(player_roll, player_name)
    print(player_name, ' has rolled: ', player_roll, sep = '')
    print('(', roll_type, ' for a score of ', player_score, ')', sep = '')

#Prints out the stats of the player at the end of the game
def print_player_stats(player_wins, computer_wins, draws):
    total = player_wins + computer_wins + draws
    if total == 0:
        win_percentage = 0.0
    else:
        win_percentage = round((player_wins / total) * 100, 1)
    
    print('Player wins: ', player_wins, sep = '')
    print('Win percentage: ', win_percentage, '%', sep = '')

main()

