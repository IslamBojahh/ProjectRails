# -*- coding: utf-8 -*-
"""
Created on Tue Aug 20 19:18:08 2019

@author: ORCAS_ISLAM
"""
#q1
#Write a function that takes a string and returns a dictionary that counts how many times each character appears in the string.

def word_char_count(word):
    word_char={}
    for char in word:
        if char in word_char:
            word_char[char]+=1
        else:
            word_char[char]=1
    return(word_char)


#q2
#Write a function that takes a list that can have nested lists in it and returns a flat list. A flat list is a list without any nested lists in it.
#I.e: func([1,2,[3,[4,5],6,7,[8,9]]]) returns [1,2,3,4,5,6,7,8,9].

def nested_list(nes_list):
    unNested_list=[]
    for item in nes_list:
        if type(item).__name__=='int':
            unNested_list.append(item)
        elif type(item).__name__=='list':
            rec_unNested_lis=nested_list(item)
            unNested_list+=rec_unNested_lis
    return unNested_list

#q3
#Write a simple URL parser. The parser takes a full string of url and returns a dictionary that contains 3 values: “scheme”, which is the URL scheme specifier, “netloc” which is the net location of the website, and “path” which is the Hierarchical path.
#i.e: https://google.com/ProjectRails/KISS/ returns {“scheme”:”https”,”netloc”:”google.com”,”path”:”ProjectRails/Kiss”}.
def URL_parser(url):
    url_dic={}
    schema=url.find(':')
    url_dic['scheme']=url[:schema]
    netloc=schema+3+url[schema+3:].find('/')
    url_dic['netloc']=url[schema+3:netloc]
    url_dic['path']=url[netloc+1:-1]
    return url_dic
    
    
