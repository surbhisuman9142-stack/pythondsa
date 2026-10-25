def get_neighbors(r,c,R,C):
      neighbors = []
      if r - 1 >= 0:#up
            neighbors.append((r-1,c))
      if r + 1 < R:
            neighbors.append((r+1,c))#down
      if c - 1 >= 0:
            neighbors.append((r, c+1))#up
      return neighbors
print(get_neighbors(1,1,3,4))
print(get_neighbors(0,0,3,4))