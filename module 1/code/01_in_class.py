import random

def game_show(n, switch_or_keep):
    '''
    calculates probability of a win (i.e. player choosing the door with 
    the car in a classic monte hall problem setup) given:
        - number of simulations 
        - if for all simulations the player kept their door choice, or made a switch 
    '''

    # initializing win counter 
    n_wins = 0

    # running the simulation for n number of times 
    for i in range(n):

        # choosing a random integer between 1-3 to simulate player door selection 
        player_choice = random.randint(1, 3)

        # implementing door switching logic if player chose to switch doors 
        if switch_or_keep == True:

            # if player chose door 1, then door 2 is revealed and player switches to door 3
            if player_choice == 1:

                player_choice = 3

            # if player chose door 2, then door 1 is revealed and player switches to door 3
            elif player_choice == 2:

                player_choice = 3

            # last option is that the player selected the correct door (door 3) 
            # the player will now switch to an incorrect door randomly assigned either 1 or 2
            else:

                player_choice = random.randint(1,2)
            
        # if player choice is correct (i.e. player chooses door 3 where the car is)
        if player_choice == 3:

            # increment win counter 
            n_wins += 1

    # returning percentage of times player wins the game
    return (n_wins / n)*100

# calling the function to get probability of wins when not switching doors 
print("\nProbability of winning when not switching doors:\n{}".format(game_show(100000, False)))

# calling the function to get probability of wins when switching door 
print("\nProbability of winning when switching doors:\n{}".format(game_show(100000, True)))