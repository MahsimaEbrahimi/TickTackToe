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

def single_game(player):  
    counter=0
    value = [' ' for i in range(9)]  
    position_player = {'X' : [], 'O' : []} 
    while True:  
       try:  
         print("The player",player,"turn. Now you need to choose your block : ", end="")
         chance = int(input())       
       except ValueError:  
         print("This is an Invalid Input!!! Please try again!")  
         continue
       if chance < 1 or chance > 9:  
           print("This is an Invalid Input!!! Please try again!")  
           continue  
       if value[chance - 1] != ' ':  
         print("Oops! The position is already filled. Please try again!")  
         continue   
       position_player[player].append(chance) 
      #  print(position_player[player])
       value[chance - 1]=player
       tictactoe_grid(value)
       if(win_loose(player,position_player)==True):
          break
       counter+=1
       if(counter==9):
        print("equal!!!!!!!!!!!")
        print("game is finished")
        break
       if(player=="X"):
            player="O"
            continue
       player="X"
def win_loose(player,position_player):
  possibility=[[1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[3,5,7],[1,5,9]]
  for i in possibility:
    if(np.isin(i,position_player[player]).all()):
      print("player%s is winner"%player)
      return True
      
single_game("X")