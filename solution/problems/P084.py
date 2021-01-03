import random
from typing import List
from solution.libs.numbers_properties import num_size
from tqdm import trange

def ans():
    # board:
    board_size = 40
    square_count = [0] * board_size
    # number of iterations
    number_of_iterations = 10 ** 6
    # special squares
    cc_squares = [2, 17, 33]
    ch_squares = [7, 22, 36]
    r_squares = [5, 15, 25, 35]
    u_squares = [12, 28]
    g2j_squares = [30]
    jail_location = 10
    go_location = 0
    # card piles:
    cc_pile: List = [None] * 14 + [go_location, jail_location]
    ch_pile: List = [None] * 6 + [go_location, jail_location, 11, 24, 39, 5, "R", "R", "U", "M3"]
    random.shuffle(cc_pile)
    random.shuffle(ch_pile)
    # dice range:
    dice_max_number = 4
    # player location
    player_location = 0

    # function for card movement:
    def next_location(card, curr_player_location):
        if card is None:
            return curr_player_location
        if card == "R":
            r_squares.append(curr_player_location)
            r_squares.sort()
            next_loc = r_squares[(r_squares.index(curr_player_location) + 1) % len(r_squares)]
            r_squares.remove(curr_player_location)
            return next_loc
        if card == "U":
            u_squares.append(curr_player_location)
            u_squares.sort()
            next_loc = u_squares[(u_squares.index(curr_player_location) + 1) % len(u_squares)]
            u_squares.remove(curr_player_location)
            return next_loc
        if card == "M3":
            return (board_size + curr_player_location - 3) % board_size
        if type(card) is int:
            return card
        raise Exception("got an unknown card:", card)

    def is_in_special_location(curr_player_location):
        return curr_player_location in g2j_squares or curr_player_location in cc_squares or curr_player_location in ch_squares

    def next_location_after_special_location(curr_player_location):
        if curr_player_location in g2j_squares:
            return jail_location
        if curr_player_location in cc_squares:
            # take one card
            card = cc_pile[0]
            # put it back at the end of the pile
            cc_pile.pop(0)
            cc_pile.append(card)
            # do what the card says:
            return next_location(card, curr_player_location)
        if curr_player_location in ch_squares:
            # take one card
            card = ch_pile[0]
            # put it back at the end of the pile
            ch_pile.pop(0)
            ch_pile.append(card)
            # do what the card says:
            return next_location(card, curr_player_location)
        else:
            raise Exception("not in special location, yet in special location movement function", curr_player_location)

    # play the game:
    for i in trange(number_of_iterations):
        # arrived here, add 1 to this place
        square_count[player_location] += 1
        # roll dice
        d1 = random.randint(1, dice_max_number)
        d2 = random.randint(1, dice_max_number)
        # go forward
        player_location += d1 + d2
        player_location %= board_size
        prev_location = -1
        while is_in_special_location(
                player_location) and player_location != prev_location:  # may pull M3 card and go back to another special location
            prev_location = player_location
            player_location = next_location_after_special_location(player_location)
    # get stats of placing:
    final_stats = []
    for i in range(board_size):
        final_stats.append((square_count[i] / number_of_iterations, i))
    final_stats.sort()
    final_stats.reverse()
    three_most_visited = [final_stats[0][1], final_stats[1][1], final_stats[2][1]]
    # finish up
    result_str = ""
    for i in three_most_visited:
        if num_size(i) == 1:
            result_str += "0" + str(i)
        else:
            result_str += str(i)
    return result_str
