def highest_even(li):
    winner = 0
    for item in li:
        if item % 2 == 0 and item > winner:
            winner = item
    return winner


print(highest_even([10, 2, 3, 4, 8, 11, 102]))
