from itertools import permutations


def is_valid(board):
    # Проверяет, нет ли ферзей на одной диагонали.
    n = len(board)
    for i in range(n - 1):
        for j in range(i + 1, n):
            # Ферзи на одной диагонали, если разность индексов равна разности значений.
            if abs(board[i] - board[j]) == j - i:
                return False
    return True


def total_options(n):
    # Возвращает количество способов расставить n ферзей на доске n×n.
    count = 0
    for a in permutations(range(n)):
        if is_valid(a):
            count += 1
    return count


n = int(input())
print(total_options(n))

