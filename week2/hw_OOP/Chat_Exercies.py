import random
import string 
class Chat(object):
    def __init__(self):
        self.__human=None
        self.__robot=None
        self.vowels=['i','o','u','e','a']
        self.allOtherChar=self.charcter()
        
    def charcter(self):
        allChar=string.ascii_letters
        charWithoutVowels=''
        for char in allChar:
            if char in self.vowels:
                continue
            else:
                charWithoutVowels+=char
        return list(charWithoutVowels+string.punctuation+' ')
        
        
                
    def connect_human(self,human):
        self.__human=human
    def connect_robot(self,robot):
        self.__robot=robot
    def show_human_dialoge(self):
        robot_message=self.__robot.getMessage()
        robot_message_encrypted=''
        for char in robot_message:
            if char=='0':
                robot_message_encrypted+=random.choice(['i','o','u','e','a'])
            else:
                robot_message_encrypted+=random.choice(self.allOtherChar)
        
        print(self.__human.getName()+' said: '+self.__human.getMessage())
        print(self.__robot.getSerialNumber()+' said: '+robot_message_encrypted)
        
    def show_robot_dialoge(self):
        human_message=self.__human.getMessage()
        human_message_encrepted=''
        for char in human_message:
            if char in 'ioueaIOUEA':
                human_message_encrepted+='0'
            else:
                human_message_encrepted+='1'
        print(self.__human.getName()+' said: '+human_message_encrepted)
        print(self.__robot.getSerialNumber()+' said: '+self.__robot.getMessage())
        
                
class Human(object):
    def __init__(self,name):
        self.__name=name
        self.__message=''
    def getName(self):
        return self.__name
    def send(self,message):
        self.__message=message
    def getMessage(self):
        return self.__message

class Robot(object):
    def __init__(self, serialNumber):
        self.__serialNumber=serialNumber
    def getSerialNumber(self):
        return self.__serialNumber
    def send(self,message):
        self.__message=message
    def getMessage(self):
        return self.__message
        
chat = Chat()
karl = Human("Karl")
bot = Robot("R2D2")
chat.connect_human(karl)
chat.connect_robot(bot)
karl.send("Hi!...")
bot.send("1101100011")
chat.show_human_dialoge()
chat.show_robot_dialoge()
