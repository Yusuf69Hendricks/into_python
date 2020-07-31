
def create_grid(grid):
  # create a 4x4 array of zeroes within grid
  grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
  
  return grid
# ******************************************
def print_grid(grid):
  # print out a 4x4 grid in 5-width columns withnin a box 
    print("\n".join("".join(map(str, row)) for row in grid))
#****************************************
def check_lost (grid):
  # return True if there are no 0 values and there are no adjacent values that are equal, otherwise False
  if  grid[0][0] == grid[0][1] == grid[0][2] == grid[0][3] == grid[1][0] == grid[1][1] == grid[1][2] == grid[1][3] ==grid[2][0] == grid[2][1] == grid[2][2] == grid[2][3] == grid[3][0] == grid[3][1] == grid[3][2] == grid[3][3]:
    print("False") 
  # --------------------------------------
  elif 0 in grid[0]:
    print("False")
  #-------------------------------------- 
  elif 0 in grid[1]:
    print("False")
  #------------------------------------  
  elif 0 in grid[2]:
    print("False")
  #-------------------------------------  
  elif 0 in grid[3]:
    print("False")
  #-------------------------------------- 
  else:
    print("True")

#*****************************************
def check_won(grid):
  # return True if a value >=32 is found in the grid, otherwise False
  check = False
  for row in grid:
      for a in row:
          if a >= 32:
              check = True
              break
  print(check)
#*****************************************
def copy_grid (grid):
#   # return a copy the given grid
  return [row[:] for row in grid]
  
#****************************************
def grid_equal (grid1,grid2):
  # check if 2 grids are equal - return boolean value
    if grid1 == grid2:
      print("True")
    else:
      print("False")
  # ****************************************


