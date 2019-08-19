# -*- coding: utf-8 -*-
"""
Created on Mon Aug 19 19:33:50 2019

@author: ORCAS_ISLAM
"""

# q1
#Check what happens when you print (0.1 + 0.2 == 0.3).
# Think, based on what was discussed in the classroom and using the internet, why.

print(0.1+0.2==0.30000000000000004)
# answer we cannot compare float number with python

# q2
#Write a function that takes two strings, and prints them interlaced in one another.
#examples: 
#func(“abc”,”be”) returns “abbec”.
#func(“aaaa”,”bb”) returns ababaa”.

def interlaced (s1 , s2):
    s=''
    if len(s1) < len(s2):
        for i in range(0,len(s1)):
            s+=s1[i]+s2[i]
        s+=s2[len(s1):]
        return(s)
    elif len(s2) < len(s1):
        for i in range(0,len(s2)):
            s+=s1[i]+s2[i]
        s+=s1[len(s2):]
        return(s)
    else:
        for i in range(0,len(s2)):
            s+=s1[i]+s2[i]
        return s

#another solution
def interlaced1 (s1 , s2):
    s=list(zip(s1 , s2));
    final=''
    print(s)
    for i in range(len(s)):
        final+=s[i][0]+s[i][1]
        
    if len(s1)==len(s2):
        return final
    elif len(s1)<len(s2):
        final+=s2[len(s):]
        return(final)
    else:
        final+=s1[len(s):]
        return final
   

#q3
#Write an implementation to two string functions you’ve learned in class:
#upper
#Split

s='Hello world' 
print(s.upper())           
print(s.split(' '))



#q5
#Create a hangman game following these rules:
#The game starts by printing a title (choose whatever you like).
#The game asks for a secret word from the user (use the input function).
#The user starts with x lives. At the beginning of each turn,the program prints the secret word, such that each unguessed character is replaced with a “_”.
#In each turn, the user guesses a character: 
#If the user guesses correctly, the “_” representing the character are replaced with the right character. All other unguessed characters remain the same.
#If the user doesn’t guess correctly, he loses one life.
#If the user guesses the whole word, the program prints the full word and exits.
#If the user loses all his lives, the program prints “you lose” and exits.


def hangman():
    print ('############## you are welcome to hangmane game ################')
    x=input('enter the secret word: ')
    inChar=[]
    lives=8
    success=False
    while lives>0 and success==False:            
        char=input('guess char: ')
        inChar.append(char)
        if char in x:
            print ('Guseed')
        s=''
        for c in x:
            if c in inChar:
                s+=c
            else:
                s+=' _ '
        if s==x:
            success==True
            print('Great you guess it !! ',s , end=(' '))
            break
        
        print(s)
        lives-=1

    if success==False and lives==0:
        print('Good luck you lose')
