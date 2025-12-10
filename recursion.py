def queens_minimal(n):
    def backtrack(row, positions):
        if row == n: # Все ферзи верно размещены.
            return 1
        count = 0
        for col in range(n):
            if all(positions[i] != col and abs(positions[i] - col) != row - i for i in range(row)):
                positions[row] = col
                count += backtrack(row + 1, positions)
        return count
    return backtrack(0, [0]*n)


n = int(input())
print(queens_minimal(n))

