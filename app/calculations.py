from math import factorial
from itertools import combinations


def nck(n, k):
    if k > n:
        return 0
    return factorial(n) / factorial(k) / factorial(n - k)


def get_total(total_val, num_of_vars):
    return nck(total_val + (num_of_vars - 1), num_of_vars - 1)


def get_magnitude(total_val, val_list, num_of_vars):
    subtracted_sum = sum(val_list) + len(val_list)
    top = (total_val - subtracted_sum) + (num_of_vars - 1)
    if top < 0:
        return 0
    else:
        return nck(top, num_of_vars - 1)


def get_total_magnitude(total, values, size, num_of_vars):
    magnitude = 0
    combos = combinations(values, size)
    for combo in combos:
        magnitude += get_magnitude(total, combo, num_of_vars)

    return magnitude


#  num_of_vars is set by the user at the start (1st page)
#  the total and values are set as entry points (2nd page)
def num_solutions(values, total, num_of_vars):
    total_solutions = get_total(total, num_of_vars)
    sum_of_intersections = 0

    for i in range(1, num_of_vars + 1):
        magnitude = get_total_magnitude(total, values, i, num_of_vars)
        if i % 2 == 0:
            sum_of_intersections -= magnitude
        else:
            sum_of_intersections += magnitude

    return total_solutions - sum_of_intersections


#  x1 + x2 + x3 = 20
#  x1 <= 1, x2 <= 19, x3 <= 2
#  expecting 5

#  x1 + x2 = 8
#  x1 <= 3, x2 <= 6 ====> 2
#  x1 <= 3, x2 <= 7 ==> 3
def main():

    print("answer", num_solutions([3, 7], 8, 2))


#  main()
