def push_up(grid):
  "merge grid values upwards"
  
# ******************************
def push_down(grid):
  "merge grid values downwards" 
  # ******************************

def push_left(grid):
  "merge grid values left"
  # ******************************

def push_right(grid):
  "merge grid values right"
  # ***************************

  # Trying to figure it out in test.py 

  grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
]
    # 0[0, 1, 2],
    # 1[3, 4, 5],
    # 2[6, 7, 8],

    # 0[a, b, c],
    # 1[d, e, f],
    # 2[g, h, i],
a = grid[0][0]
b = grid[0][1]
c = grid[0][2]
d = grid[1][0]
e = grid[1][1]
f = grid[1][2]
g = grid[2][0]
h = grid[2][1]
i = grid[2][2]

grid2 = [
    [a + d, b + e, c + f],
    [g + d, h + e, i + f],
    [7, 8, 9],
]
# --------------------------------------
grid3 = [
    [1, 2, 3],
    [a + d, b + e, c + f],
    [d + g, e + h, f + i],
]
# --------------------------------------
grid4 = [
    [a + b, c + b, 3],
    [e + d, f + e, 6],
    [g + h, i + h, 9],
]
# --------------------------------------
grid5 = [
    [1, a + b, b + c],
    [4, d + e, e + f],
    [7, g + h, h + i],
]



print('\nOriginal:')
for row in grid:
    print(row)

print('\nOriginal2:')
for row in grid2:
    print(row)

print('\nOriginal3:')
for row in grid3:
    print(row)

print('\nOriginal4:')
for row in grid4:
    print(row)

print('\nOriginal5:')
for row in grid5:
    print(row)

rolledup = grid2[1:] + grid2[:1]
print('\nRolled up:')
for row in rolledup:
    print(row)


rolledup = grid[1:] + grid[:1]  
print('\nRolled up:')
for row in rolledup:
    print(row)

rolleddown = grid[-1:] + grid[:-1]
print('\nRolled down:')
for row in rolleddown:
    print(row)

rolledleft = [row[1:] + row[:1] for row in grid]
print('\nRolled left:')
for row in rolledleft:
    print(row)

rolledright = [row[-1:] + row[:-1] for row in grid]
print('\nRolled right:')
for row in rolledright:
    print(row)

shiftedup= grid[1:] + [[0] * len(grid[0])]
print('\nShifted up:')
for row in shiftedup:
    print(row)
