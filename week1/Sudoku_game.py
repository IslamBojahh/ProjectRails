# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 18:42:57 2019

@author: ORCAS_ISLAM
"""
import random 
grid = [[0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0]]


#def initialization(number_fix):
#    test_board=[[0 for i in range(9)] for j in range(9)]
#    x=random.randint(0,8)
#    y=random.randint(0,8)
#    while(True):
#         value=random.randint(1,9)
#         if grid[x][y]==0:
#             if valid(test_board,value,(x,y))==True and (x,y) not in grid :
#                 grid[x][y]=value
#                 test_board[x][y]=value
#                 if check_grid():
#                     return True
#                 elif initialization(number_fix):
#                     return True
#        break
#    grid[x][y]=0
#             
#    print(grid)
#def valid(bord,number,position):
#    x=position[0]
#    y=position[1]
#    #checkRow=False, checkClo=False,checkRec=False
#    #check colum
#    for i in range(len(bord)):
#        if bord[i][y] == number and position[0]!=i:
#            return False
#    #check row     
#    for j in range(len(bord[0])):
#        if bord[x][j] ==number and position[1]!=j:
#            return False
#    #checkBox
#    box_x=x//3
#    box_y=y//3
#    
#    for i in range(box_y*3,box_x*3+3):
#        for j in range(box_x*3,box_y*3+3):
#            if bord[i][j]==number and (i,j)!=position:
#                return False
#           
#        
#    
#    return True

#this function is to print the grid => game board
def print_Grid(arr , fixedArr):
    for row in range(9):
        if row%3==0:
            print('-----------------------\n')
        print('|' , end=(' '))
        for col in range (9):
            if fixedArr[row][col]!=0:
                print('.'+str(arr[row][col]) , end=(''))
            else:
                if arr[row][col]==0:
                    print('  ', end=(''))                
                else:
                    print(' '+str(arr[row][col]) , end=(''))                
            if (col+1)%3==0:
                print('|' , end=(''))
            
        print('\n')
    print('-----------------------')


#return if all field in grid is filled or not
def check_grid():
    for row in range(9):
        for col in range(9):
            if grid[row][col]==0:
                return False
    return True


#genrate sudoko solution
numbers=[1,2,3,4,5,6,7,8,9]
def generate_solvedGrid():
    for i in range(81):
        row=i//9
        col=i%9
        if grid[row][col]==0:
            random.shuffle(numbers)
            for num in numbers:
                if num not in grid[row]:
                    if num not in (grid[0][col] , grid[1][col] ,grid[2][col] , grid[3][col] , grid[4][col] , grid[5][col] , grid[6][col] , grid[7][col] , grid[8][col]):
                        square=[]
                        if row<3:
                            if col<3:
                                square=[grid[i][0:3] for i in range(3)]
                            elif col<6:
                                square=[grid[i][3:6] for i in range(3)]
                            else:
                                square=[grid[i][6:] for i in range(3)]
                        elif row < 6:
                            if col<3:
                                square=[grid[i][0:3] for i in range(3,6)]
                            elif col<6:
                                square=[grid[i][3:6] for i in range(3,6)]
                            else:
                                square=[grid[i][6:] for i in range(3,6)]
                        else:
                            if col<3:
                                square=[grid[i][0:3] for i in range(6,9)]
                            elif col<6:
                                square=[grid[i][3:6] for i in range(6,9)]
                            else:
                                square=[grid[i][6:] for i in range(6,9)]
                                
                        if num not in (square[0]+square[1]+square[2]):
                            grid[row][col]=num
                            if check_grid():
                                return True
                            elif generate_solvedGrid():
                                return True
            break
    grid[row][col]=0
            

def removing_number(grid ,NumberToSolve):
    attempt=NumberToSolve
    while attempt>0:
        row=random.randint(0,8)
        col=random.randint(0,8)
        while grid[row][col]==0:
            row=random.randint(0,8)
            col=random.randint(0,8)
        grid[row][col]=0
        attempt-=1
            
    
def hint_value(x,y):
    numbers=[]
    hint_numbers=[]
    for num in grid[x]:
        if num!=0:
            numbers.append(num)
    for num in (grid[0][y] ,grid[1][y],grid[2][y],grid[3][y],grid[4][y],grid[5][y],grid[6][y],grid[7][y] ,grid[8][y]):
        if num!=0:
            numbers.append(num)
    for num in [0,1,2,3,4,5,6,7,8,9]:
        if num not in numbers:
            hint_numbers.append(num)
    
    print('hint numbers are : ' ,end=('') )
    for num in hint_numbers[:-1]:
        print(num ,' ,' , end=(''))
    print(hint_numbers[-1] ,end=('') )
    print()
        
        
            
def isValidCell(x,y ,fixed_copy):
    if x>=0 and x<9 and y>=0 and y<9 and fixed_copy[x][y]==0:
        return True
    else:
        return False

def isValidNum(num):
    if num in [0,1,2,3,4,5,6,7,8,9]:
        return True
    else:
        return False
    
def main():
    NumberToSolve=int(input('Please Enter the number of cell you want to solve: '))
    generate_solvedGrid()
    grid_copy=[]
    fixed_copy=[]
    for row in grid[:]:
        grid_copy.append(row[:])    
    removing_number(grid ,81-NumberToSolve) 
    for row in grid[:]:
        fixed_copy.append(row[:])
    print_Grid(grid[:] , fixed_copy)
    won=False
    for i in range(81-NumberToSolve):
        cell=int(input('Please enter the number of cells to fill [0-80] : '))
        x=cell//9
        y=cell%9
        if isValidCell(x,y,fixed_copy):
            hint_value(x,y)
            num=int(input('Please Enter the value : '))
            if not isValidNum(num):
                print('Invalid number')
            else:
                if num==0:
                    grid[x][y]=num
                    print_Grid(grid[:] , fixed_copy)
                elif grid_copy[x][y]==num:
                    grid[x][y]=num
                    print_Grid(grid[:] , fixed_copy)
                else:
                    print('error : Invalid number')
        else:
            print("this Cell is inValid")
            
        if check_grid():
            print('Great ! you are won')
            won=True
            break
    if not won:
        print('Game Over !')
                    

if __name__ == '__main__':
    main()
                      
                                
                    
        
            
            
            

        
            

