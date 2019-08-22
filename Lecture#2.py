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


#q4
from datetime import datetime
def event_Report():
    input_file=open('L2_q5_input.txt')
    output_file=open('L2_q5_output.txt' ,'w+')
    lines=input_file.readlines()
    Days={}
    FMT = '%H:%M'
    day=''
    for i in range(len(lines)):
        if lines[i][0:4]=='Day ':
            Days[(lines[i][0:5] , lines[i][6:-1])]=[]
            day=(lines[i][0:5] , lines[i][6:-1])
        elif lines[i][0]=="0" or lines[i][0]=="1" or lines[i][0]=="2":
            if lines[i][6:-1]!='End':
                Days[day].append([lines[i][:5] , lines[i][6:-1]])
            else:
                Days[day].append([lines[i][:5] , lines[i][6:-1]])
    
    total=0
    all_activities={}   
    for day in Days.keys():
        day_activity=Days[day]
        output_file.write(day[0]+':'+day[1]+'\n')
        for i in range(len(day_activity)):
            if day_activity[i][1]!='End':
                tdelta = datetime.strptime(day_activity[i+1][0], FMT) - datetime.strptime(day_activity[i][0], FMT)
                tdelta_min=tdelta.seconds/60
                total+=tdelta_min
                if day_activity[i][1] in all_activities:
                    all_activities[day_activity[i][1]]+=tdelta_min
                else:
                    all_activities[day_activity[i][1]]=tdelta_min
                output_file.write(day_activity[i][0] + '-'+ day_activity[i+1][0] +' ' + day_activity[i][1]+'\n')
        output_file.write('\n')

    output_file.write('Report\n\n')
    for activity in sorted(all_activities.keys()):
        output_file.write(activity +' '+str(int(all_activities[activity]))+' minutes  ' +str(int((all_activities[activity]/total)*100))+'%\n')

    input_file.close()
    output_file.close()
    
     
