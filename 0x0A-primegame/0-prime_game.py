#!/usr/bin/python3

''' Prime Game'''


def isWinner(x, nums):
    """
    Determines the winner of a game played.
    """
    maria_wins = ben_wins = 0
    for _ in range(x):
        # Analyze the current round
        can_maria_move = False
        can_ben_move = False
        for num in nums:
            if is_prime(num):
                # Check if a move is possible for each player
                if num % 2 != 0:
                    can_maria_move = True
                else:
                    can_ben_move = True

                nums = [n for n in nums if n % num != 0 and n != num]
                break
        if can_maria_move:
            maria_wins += 1
        else:
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif ben_wins > maria_wins:
        return "Ben"
    else:
        return None


def is_prime(num):
    """
    Simple prime number check function.
    """
    if num <= 1:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
