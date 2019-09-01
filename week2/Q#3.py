# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 21:24:56 2019

@author: ORCAS_ISLAM
"""

#Each week you are meeting with your friends to spend some quality time together. Usually you're hanging out in a bar on Friday nights, or going out of town on Saturdays, or playing board games on Sundays. You want to simplify the process of gathering people and that's why you've decided to write a program which could automate this process.
#You should create the class Party(place) which will send the invites to all of your friends. Also you should create the class Friend and each friend will be an instance of this class.
#Sometimes the circle of friends is changing - new friends appear, the old ones disappear from your life (for example - move to another town). To form right connections you should create the Party class with the next methods:
#add_friend(Friend(name)) - add friend 'name' to the list of the 'observers' (people, which will get the invitations, when the new party is scheduled).
#del_friend(friend) - remove 'friend' from the 'observers' list.
#send_invites() - send the invites with the right day and time to the each person on the list of 'observers'.
#Class Friend should have the show_invite() method which returns the string with the last invite that the person has received with the right place, day and time. The right place - is the 'place' which is given to the Party instance in the moment of creation. If the person didn't get any invites, this method should return - "No party..."
#Examples:
#party = Party("Midnight Pub")
#nick = Friend("Nick")
#john = Friend("John")
#lucy = Friend("Lucy")
#chuck = Friend("Chuck")
# 
#party.add_friend(nick)
#party.add_friend(john)
#party.add_friend(lucy)
#party.send_invites("Friday,...

People_invitation={}
class Party(object):
    def __init__(self , invitation):
        self.friend=[]
        self.invitation=invitation
    def add_friend(self ,f):
        self.friend.append(f.getName())
    def del_friend(self , f):
        self.friend.remove(f.getName())
    def send_invites(self,details):
        for people in self.friend:
            if people in People_invitation:
                People_invitation[people].insert(0,self.invitation+''+details)
            else:
                People_invitation[people]=[self.invitation+''+details]
        

class Friend(object):
    def __init__(self, name):
        self.__name=name
    
    def getName(self):
        return self.__name
    def show_invite(self):
        if self.__name in People_invitation:
            return People_invitation[self.__name][0]
        else:
            return "No Party"
    

party = Party("test2")
nick = Friend("Nick")
john = Friend("John")
lucy = Friend("Lucy")
chuck = Friend("Chuck")
 
party.add_friend(nick)
party.add_friend(john)
party.add_friend(lucy)

party.del_friend(nick)
party.send_invites("Friday,...")

party2 = Party("test1")
party2.add_friend(nick)
party2.add_friend(john)
party2.send_invites("Tuesday,...")

print(nick.show_invite())
print(john.show_invite())
print(lucy.show_invite())
print(chuck.show_invite())