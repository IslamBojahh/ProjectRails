# -*- coding: utf-8 -*-
"""
Created on Fri Aug 23 16:38:08 2019

@author: ORCAS_ISLAM
"""
#q1

#Solve these exercises using (one liners only):
#Find all the numbers between 1 and 1000 that are divisible by 7.
DividedBy7= lambda :[num for num in range(1,1000) if num%7==0]

#Find all of the numbers from 1-1000 that have a 3 in them
NumberHave3= lambda :[num for num in range(1,1000) if num//10==3 or num%10==3 or num//100==3 or (num%100)%10==3 or (num%100)//10==3 ]

#Remove all of the vowels in a string
RemoveVowels=lambda word :''.join([char for char in word if char not in ['a','o','u','i','e']])

#Find all of the words in a string that are less than 4 letters
ShortWords=lambda text:[word for word in text.split(' ') if len(word)<4]

#Find all the numbers between 1 and 1000 that are divisible by any digit besides 1 (2-9).
DvisibleBy2_9=lambda : set([num for num in range(1,1000)for divisor in [2,3,5,7] if num%divisor==0])

#BTW, there’s dictionary comprehension too:
#Write a function that takes a string and returns a dictionary that contains all the words in the string as keys, and their length as values.
#E.g: func(“I love noodles and recursion”)= {“I”:1, “noodles”:7,”love”:4,”and”:3,”recursion”:9}.

def string_word_dic(text):
    word_dic={}
    for word in text.split(' '):
        if word not in word_dic:
            word_dic[word]=len(word)
    return(word_dic)
    

#q2
#Write a function that takes two numbers and randomly performs one of these functions between them:
#Add
#Multiply
#Modulo
#Division
#In order to choose a function randomly you must use random.choice() function.
#Hint: in Python, almost anything is an object.
import random
def num_operation(x,y):
    operations=['+','-','/','*']
    return eval(str(x)+random.choice(operations)+str(y))


 #q3
#Write a function that calculates the Nth number in Fibonacci sequence. Use recursion.    
def fib(n , Dic):
    if n==1 or n==2:
        return 1
    else:
        fn_1=fib(n-1,Dic)
        Dic[n-1]=fn_1
        fn_2=fib(n-2 ,Dic )
        Dic[n-2]=fn_2
        Dic[n]=fn_1+fn_2
        return Dic[n]

#q4
#A classic job interview question ahead. Remember, you can do it:
#Given a value N, if we want to make change for N cents, and we have an infinite 
#supply of each of S = { S1, S2, .. , Sm} valued coins, how many ways can we make the change? The order of coins doesn’t matter.
#For example, for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},{2,2},{1,3}.
# So output should be 4. For N = 10 and S = {2, 5, 3, 6}, there are five solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}. So the output should be 5.

#describtion 
# this question solved by  dynamic programmin , knapsack problem 
def number_changes(coins , total):
    if total==0:
        return 1
    if total<0:
        return 0
    if len(coins)==0 and total>0:
        return 0
    
    return number_changes(coins[:-1] , total) + number_changes(coins[:] , total-coins[-1])
    

def isInMatrix(x,y,matrix):
    if x < 0 or x>=len(matrix) or y<0 or y>=len(matrix[0]):
        return False
    else:
        return True



#q5
#You are given a table (2d matrix) with n rows and m columns. The top left corner has the coordinates (0,0), and the bottom right corner has the coordinates (n-1,m-1). A path {cell_0,cell_1,cell_2...cell_n} is legal if:
#All the cells in it contain 0.
#Cell_i and cell_i+1 share a side (the movement is in straight lines).
#Create a function that takes a table and returns whether or not there’s a legal path from (0,0) to (n-1,m-1).

def simple_path(maps , x , y , path=[]):
    if x==len(maps)-1 and y==len(maps[0])-1:
        return True     
    if maps[x][y]==0:
        path.append((x,y))
        p1=False
        p2=False
        p3=False
        p4=False
        if(x-1,y) not in path and isInMatrix(x-1,y , maps):
            p1=simple_path(maps ,x-1,y )
            if p1==True:
                path.append((x-1,y))
        if(x+1,y) not in path and isInMatrix(x+1,y , maps):
            p2 =simple_path(maps ,x+1,y )
            if p2==True:
                path.append((x+1,y))
        if(x,y-1) not in path and isInMatrix(x,y-1 , maps):
            p3=simple_path(maps ,x,y-1 )
            if p3==True:
                path.append((x,y-1))
        if(x,y+1) not in path and isInMatrix(x,y+1 , maps):
            p4=simple_path(maps ,x,y+1 )
            if p4==True:
                path.append((x,y+1))

        
        return p1 or p2 or p3 or p4
    else:
        return False





    
    
    

