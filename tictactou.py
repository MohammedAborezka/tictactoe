# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 14:38:28 2024

@author: MOHAMMED
"""
from functools import reduce


def print_sheet(sheet):
    for x in sheet:
        for y in x :
            print(y,end="")
        print()

def move(symbol,sheet):
        possible_numbers =[1,2,3]
        while True:
            try:
                x = int(input("in which row you would like to insert your symbol"))
                while x not in possible_numbers :
                    print("number put of range please enter vavlid number from 1 to 3")
                    x = int(input("in which row you would like to insert your symbol"))
                y = int(input("in which column you would like to insert your symbol"))
                while y not in possible_numbers or x == None:
                    print("number put of range please enter vavlid number from 1 to 3")
                    y = int(input("in which column you would like to insert your symbol"))
                if sheet[x-1][y-1]=="x" or sheet[x-1][y-1]=="o":
                    print("that pleace is already played")
                    continue
                sheet[x-1][y-1]=symbol
                break
            except:
                print("please enter a number from 1 to 3")
            
            
            
def check_tie(sheet):
    for row in sheet:
        for column in row:
            if column=="#":
                return False
            else:
                continue
    return True
def check_winner(sheet,symbol):
    win = False
    elements = [row for row in sheet]
    """
        res=reduce(lambda a,b: a if a==b else False,row)
    
        if res==symbol:
            win = True 
            print(symbol)
            return
    """
    res = map(lambda x,y,z: x==symbol and x==y==z,sheet[0],sheet[1],sheet[2])
    if True in list(res):
        win == True
        return(symbol)
    dignal1 = [sheet[i][i] for i in range(len(sheet))]
    elements.append(dignal1)
    """
    res=reduce(lambda a,b: a if a==b else False,dignal1)
    if res==symbol:
        win = True 
        return(symbol)
    """
    lis = []
    for x in sheet:
        lis.extend(x)
    dignal2_index = list(range(len(lis)))[2:len(lis)-1:2]
    dignal2_numbers = [lis[i] for i in dignal2_index]
    elements.append(dignal2_numbers)
    """
    res=reduce(lambda a,b: a if a==b else False,dignal2_numbers)
    if res==symbol:
        win = True 
        return(symbol)
    return win
"""
    for row in elements:
        res = reduce(lambda a,b: a if a==b else False, row)
        if res == symbol:
            win =True
            return(symbol)
    return win
    
      
sheet = [["#","#","#"],["#","#","#"],["#","#","#"]]
players = {"x":"player1","o":"player2"}
print("player 1 is x player 2 is o")
while(True):
    if check_tie(sheet):
        print("tie")
        break
    print_sheet(sheet)
    symbol ="x"
    print("player 1 move")
    move(symbol, sheet)
    if check_winner(sheet, symbol)==symbol:
        print_sheet(sheet)
        print(players[symbol]+" win")
        break
    print_sheet(sheet)
    if check_tie(sheet):
        print("tie")
        break
    symbol="o"
    print("player 2 move")
    move(symbol, sheet)
    if check_winner(sheet, symbol)==symbol:
        print_sheet(sheet)
        print(players[symbol]+" win")
        break
    """
if check_tie(sheet) and check_winner(sheet,"x")==False and check_winner(sheet,"o")==False:
    print("tie")
    """
    

