# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 18:08:24 2019

@author: ORCAS_ISLAM
"""


import sqlite3
conn = sqlite3.connect('chinook.db')
c = conn.cursor()

def Add_track():
    Name= input('Enter Track name: ')
    AlbumId=input('Enter track Album ID: ')
    MediaTypeId=input('Enter track Media Type Id: ')
    GenreId=input('Enter track GenerId: ')
    Composer=input('Enter track Composer: ')
    Milliseconds=input('Enter track millisecond: ')
    Bytes=input('Enter track Bytes: ')
    UnitPrice=input('Enter track unit price: ')
    
    c.execute("INSERT INTO tracks (Name,AlbumId,MediaTypeId ,GenreId ,Composer,Milliseconds,Bytes,UnitPrice) VALUES (?,?,?,?,?,?,?,?)"
              ,(Name,AlbumId,MediaTypeId,GenreId ,Composer,Milliseconds,Bytes,UnitPrice))

def Get_playlist():
    c.execute("SELECT * FROM playlists ")
    conn.commit()
    Names = c.fetchall()
    for name in Names:
        print(name[1])   
        
def Create_playlist():
    c.execute("CREATE TABLE playlist(playlistId  INTEGER PRIMARY KEY AUTOINCREMENT, name varchar(255))")
    

def add_song():
    songName=input('Enter Song Name: ')
    c.execute("INSERT INTO playlist (Name) VALUES (?)" ,(songName,))
    
def Add_employee():
    FirstName=input('Enter Employee FirstName: ')
    LastName=input('Enter Employee LastName: ')
    Title=input('Enter Employee Title: ')
    ReportsTo=input('Enter Employee ReportsTo: ')
    BirthDate=input('Enter Employee BirthDate: ')
    HireDate=input('Enter Employee HireDate: ')
    Address=input('Enter Employee Address: ')
    City=input('Enter Employee City: ')
    State=input('Enter Employee State: ')
    Country=input('Enter Employee Country: ')
    PostalCode=input('Enter Employee PostalCode: ')
    Phone=input('Enter Employee Phone: ')
    Fax=input('Enter Employee Fax: ')
    Email=input('Enter Employee Email: ')
    c.execute("INSERT INTO employees(FirstName, LastName,Title,ReportsTo,BirthDate,HireDate,Address,City,State,Country,PostalCode,Phone,Fax,Email) VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?)",
              (LastName,FirstName,Title,ReportsTo,BirthDate,HireDate,Address,City,State,Country,PostalCode,Phone,Fax,Email))

def Delete_employee():
    Employee_id=int(input('Enter employee id: '))
    c.execute("DELETE FROM employees WHERE EmployeeId=?" ,(Employee_id,))
    
    
    
def main():
    print('This programe is to manage a record store In the Drive folder')
    print("0:Add_track,\n"
          "1:Get_playlist\n"
          "2:Create_playlist\n"
          "3:add_song\n"
          "4:Add_employee\n"
          "5:Delete_employee\n"
          "8:Exit"
            )
    x=int(input('Choose the function you want: '))
    switcher ={
        0:Add_track,
        1:Get_playlist,
        2:Create_playlist,
        3:add_song,
        4:Add_employee,
        5:Delete_employee
        }    
    while x <8 and x>=0:
        switcher[x]()
        print('done')
        print("0:Add_track,\n"
              "1:Get_playlist\n"
              "2:Create_playlist\n"
              "3:add_song\n"
              "4:Add_employee\n"
              "5:Delete_employee\n"
              "8:Exit"
            )
        x=int(input('Choose the function you want: '))
    print('You Exit the program.')

    

if __name__ == '__main__':
    print(main())
    conn.commit()
    conn.close()
