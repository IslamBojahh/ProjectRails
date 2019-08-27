# -*- coding: utf-8 -*-
"""
Created on Tue Aug 27 23:02:33 2019

@author: ORCAS_ISLAM
"""
#I believe that many of you have dealt with such a problem. One day you are working in the text editor, saving the document and closing it. And the next day you are re-reading the text and realizing that one of the previous versions was better but there is no way to get it back. This thing can be easily handled by the version control system (for example, git), but it’s used mostly by the developers and not the ordinary people who work with texts. In this mission you’ll help the latter by creating a text editor prototype that supports the version control system, which will allow...
#Your task is to create 2 classes: Text and SavedText. The first will works with texts (adding, font changing, etc.), the second will control the versions and save them.

#Class Text should have the next methods:
#(text) - adds (text) to the current text;
#(font name) - sets the chosen font. Font is applied to the whole text, even if it’s added after the font is set. The font is displayed in the square brackets before and after the text: "[Arial]...example...[Arial]". Font can be specified multiple times but only the last variant is displays;
#- returns the current text and font (if is was set);
#(SavedText.get_version(number)) - restores the text of the chosen version.
#Class SavedText should have the next methods:
#(Text) - saves the current text and font. The first saved version has the number 0, the second - 1, and so on;
#(number) - this method works with the 'restore' method and is used for choosing the needed version of the text.
#**
#In this mission you can use the design pattern:
#text = Text()
#saver = SavedText()
#  
#text.write("At the very beginning ")
#saver.save_text(text)
#text.set_font("Arial")
#saver.save_text(text)
#text.write("there was nothing.")
#text.show() == "[Arial]At the very beginning there was nothing.[Arial]"
#  
#text.restore(saver.get_version(0))
#text.show() == "At the very beginning "
#information about the text and saved copies.
#the text after all of the commands.
#To save the object’s previous states with the ability to return to them, in case something goes wrong.
#No more than 10 saved copies.


class Text(object):
    def __init__(self , text='' , font=None):
        self.__text=text
        self.__font=font
    
    def getText(self):
        return self.__text
    def getFont(self):
        return self.__font[-1]
    def setFont(self , font):
        self.__font=font
    def addText(self , text):
        self.__text= self.__text+text
    def show(self):
        return '['+self.__font+']'+self.__text+'['+self.__font+']'
        

class saveText(object):
    lastVersion=0
    versions={}
    def __init__(self , Text):
        saveText.versions[saveText.lastVersion]=[Text.getText() ,Text.getFont()] 
        saveText.lastVersion+=1
    def get_version(version):
        return saveText.versions[version][0]
        

    
    
    
    
text=Text('Hello world' , 'new') 
saveText(text)
print(saveText.get_version(0))
text.addText('new new')
saveText(text)
print(saveText.get_version(1))
text.addText('new new2')
saveText(text)
print(text.show())
print(saveText.get_version(2))
        