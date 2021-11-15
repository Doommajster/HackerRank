#!/usr/bin/python

def displayPathtoPrincess(n,grid):
#print all the moves here
    for number, row in enumerate(grid):
        if "p" in row:
            princes_pos = [number, row.index("p")]
        if "m" in row:
            my_pos = [number, row.index("m")]
    while my_pos[0] != princes_pos[0] and my_pos[1] != princes_pos[1]:        
        if princes_pos[0] > my_pos[0]:
            print("DOWN")
            my_pos[0] += 1
        elif princes_pos[0] < my_pos[0]:
            print("UP")
            my_pos[0] -=1

        if princes_pos[1] > my_pos[1]:
            print("RIGHT")
            my_pos[1] += 1
        elif princes_pos[1] < my_pos[1]:
            print("LEFT")
            my_pos[1] -= 1

m = int(input())
grid = [] 
for i in range(0, m): 
    grid.append(input().strip())

displayPathtoPrincess(m,grid)
