grid = [['.', '.', '.', '.', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['.', 'O', 'O', 'O', 'O', 'O'],
        ['O', 'O', 'O', 'O', 'O', '.'],
        ['O', 'O', 'O', 'O', '.', '.'],
        ['.', 'O', 'O', '.', '.', '.'],
        ['.', '.', '.', '.', '.', '.']]

res = ''
for y in range(len(grid[0])-1):
    for x in range(len(grid)-1):
        res += grid[x][y]
    res += '\n'
print(res)

res = ''
for y in range(len(grid[0])-1):
    res += ''.join([grid[x][y] for x in range(len(grid)-1)])
    res += '\n'
print(res)

res = '\n'.join([''.join([grid[x][y] for x in range(len(grid)-1)])
                 for y in range(len(grid[0])-1)])
print(res)
