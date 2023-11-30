import numpy as np
def tictactoe_grid(value):  
    print("\t      |      |")  
    print("\t    {} |  {}   |  {}".format(value[0], value[1], value[2]))  
    print('\t______|______|______')  
    print("\t      |      |") 

    print("\t   {}  |  {}   |  {}".format(value[3], value[4], value[5]))  
    print('\t______|______|______')  
    print("\t      |      |")   
    print("\t  {}   |  {}   |  {}".format(value[6], value[7], value[8]))  
    print("\t      |      |")  


posision_player={"X":[],"O":[]}
possibility=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[3,5,7],[1,5,9]]
filled_space=[]
value=[" " for i in range(9)]
counter=1

def is_winner(player,posision_player):
    for i in possibility:
        if(np.isin(i,posision_player[player]).all()):
            print(f"user{player} is winner")
            return True 
               
def can_move(mve):
    if(mve in range(1,10) and mve not in filled_space ):
         return True
    else:
        return "the posision is filled or sth is wrong"
    
def make_move(mve,player):
    if can_move(mve)==True :
        return True
    else:
        return " there is an error ocured"


def start(player):
    while True:
         print("The player",player,"turn. Now you need to choose your block : ", end="")

         chance=int(input())
         if(make_move(chance,player))==True:
             posision_player[player].append(chance)
             value[chance-1]=player
             filled_space.append(chance)
             tictactoe_grid(value)       
             global counter
             counter +=1
             print(counter)
             if(counter==10):
                 print("equal")
                 break
             if is_winner(player,posision_player)==True:
                 break           
             if(player=="X"):
                player="O"   
                continue
             player="X"      
         else:
             print(make_move(chance,player))
   
start("X")
