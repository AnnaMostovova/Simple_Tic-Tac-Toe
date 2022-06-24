def print_grid(grid):
    print('---------')
    for r in grid:
        print(f'| {r[0]} {r[1]} {r[2]} |')
    print('---------')


def check_wins(grid):
    win00 = grid[0].count(grid[0][0]) == 3 or grid[0][0] == grid[1][0] == grid[2][0]
    win22 = grid[2].count(grid[2][2]) == 3 or grid[0][2] == grid[1][2] == grid[2][2]
    win11 = any([grid[1][0] == grid[1][1] == grid[1][2], grid[0][1] == grid[1][1] == grid[2][1],
                 grid[0][0] == grid[1][1] == grid[2][2], grid[0][2] == grid[1][1] == grid[2][0]])

    res = ''
    res += 'X' if any([grid[0][0] == 'X' and win00, grid[2][2] == 'X' and win22, grid[1][1] == 'X' and win11]) else ''
    res += 'O' if any([grid[0][0] == 'O' and win00, grid[2][2] == 'O' and win22, grid[1][1] == 'O' and win11]) else ''
    return res


cells = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
print_grid(cells)

end = False
count_fill = 0
while count_fill < 9 and not end:
    coordinates = input().split(' ')
    if not (coordinates[0].isdigit() and coordinates[1].isdigit()):
        print('You should enter numbers!')
        continue
    row = int(coordinates[0])
    column = int(coordinates[1])
    if not (0 < row < 4 and 0 < column < 4):
        print('Coordinates should be from 1 to 3!')
    elif cells[row - 1][column - 1] != ' ':
        print('This cell is occupied! Choose another one!')
    else:
        cells[row - 1][column - 1] = 'X' if count_fill % 2 == 0 else 'O'
        print_grid(cells)
        who_wins = check_wins(cells)
        if who_wins != '':
            end = True
            print(f'{who_wins} wins')
