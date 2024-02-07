#!/usr/bin/python3
"""This attempts to solve the n-queens problem"""
import sys


def calculate_position(queens, lenght):
    """Calculates all attack moves of a queens"""
    vert = []
    res = []
    hor = []
    diag = []
    diag2 = []
    for i in range(queens[0] + 1, lenght):
        vert.append([i, queens[1]])
    for i in range(queens[0] - 1, -1, -1):
        vert.append([i, queens[1]])
    res.extend(vert)
    for i in range(queens[1] + 1, lenght):
        hor.append([queens[0], i])
    for i in range(queens[1] - 1, -1, -1):
        hor.append([queens[0], i])
    res.extend(hor)
    j = queens[1] + 1
    for i in range(queens[0] + 1, lenght):
        if j < lenght and i < lenght:
            diag.append([i, j])
        else:
            break
        j += 1
    j = queens[1] + 1
    for i in range(queens[0] - 1, -1, -1):
        if j < lenght and i > -1:
            diag.append([i, j])
        else:
            break
        j += 1
    res.extend(diag)
    j = queens[1] - 1
    for i in range(queens[0] - 1, -1, -1):
        if j > -1 and i > -1:
            diag2.append([i, j])
        else:
            break
        j -= 1
    j = queens[1] - 1
    for i in range(queens[0] + 1, lenght):
        if j > -1 and i < lenght:
            diag2.append([i, j])
        else:
            break
        j -= 1
    res.extend(diag2)
    return res


def generator(length):
    """Generates an empty board for visualization
    Args:
        l (int): the board dimensions
    Returns:
        list: a matrix of empty spaces
    """
    return [[" " * 9 for _ in range(length)] for _ in range(length)]


def priB(b):
    """A print function to visualize the placements
    """
    vas = " " * 9
    marker = ("+---------" * len(b)) + "+"
    for line in b:
        print(marker)
        for i in range(3):
            print('|', end="")
            for xa in line:
                y = " " * 9 if i != 1 else xa if xa != 0 else " " * 9
                print(y, end="|")
            print()
    print(marker)


def queen_checker(queens, N, curr):
    """Checks if a queens is in a valid position"""
    for x in queens:
        if curr in (calculate_position(x, N)):
            return False
    return True


def nqueens(board, N, col, queens, res):
    """Finds the number of possible permutations to
    solve the problem
   """
    if col >= N:
        # priB(board) # Uncomment this to see a visualization of the process
        res.append(queens.copy())
        return False
    for i in range(N):
        if queen_checker(queens, N, [i, col]):
            # board[i] [col] = "    Q    " #Uncomment this too
            queens.append([i, col])
            if nqueens(board, N, col + 1, queens, res):
                return True
            board[i][col] = 0
            queens.remove([i, col])
    return False


if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        var = int(sys.argv[1])
        if var < 4:
            print("N must be at least 4")
            sys.exit(1)
        res = []
        b = generator(var)
        nqueens(b, var, 0, [], res)
        for item in res:
            print(item)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
