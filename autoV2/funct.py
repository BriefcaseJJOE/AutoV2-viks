import random 
import controls as move
import map_config as map
import time


def to_right_tp(player_x_postion, player_y_postion):
    ''' 
    this party handles player moving to the right teleporter 
    and pressing up on it 
    
    '''
    if player_x_postion > map.CHECK_POINTS["right_tp_right_bound"] and player_y_postion >= map.CHECK_POINTS["ground"]-1 : 
        move.hold_left()
        
    
    elif player_x_postion < map.CHECK_POINTS["right_tp_left_bound"] and player_x_postion > 0 and player_y_postion >= map.CHECK_POINTS["ground"]-1: 
        move.hold_right()


    elif player_x_postion > map.CHECK_POINTS["right_tp_left_bound"] and player_x_postion < map.CHECK_POINTS["right_tp_right_bound"] and player_y_postion >= map.CHECK_POINTS["ground"]-1:
        
        move.up()
        move.release_all()
        print(f'moving_to_right_TP {player_x_postion}, {player_y_postion}')

    else:
        return  
    
        


def genesis(player_x_postion,player_y_postion):
    """
    this will triiger attacking sequence on the top 
    platform 
    """
     
    if player_y_postion <= map.CHECK_POINTS["middle_platform"] and player_x_postion < 0:
            
            print(f'Gen_L {player_x_postion}, {player_y_postion}')

            move.top_left_action()
            time.sleep(0.5)
            move.ult()
            time.sleep(2.5)
            move.down_jump()
    else:
         return           
            


def to_left_tp(player_x_postion,player_y_postion):
    """
    this part will only trigger on the left side of the map
    and moving towards left teleporter and using it
    center of the map == 0 , left side will be negative number
    
    small ledgers on the ground adding 10 to the y axis
    to account for it.
    """
     
        #(left bound =-490    left_tp = -480  right bound = -470       )
    if player_x_postion > map.CHECK_POINTS["left_tp_right_bound"] and player_x_postion < 0 and player_y_postion >= map.CHECK_POINTS["ground"]-10: 
        move.hold_left()
        
    
    elif player_x_postion < map.CHECK_POINTS["left_tp_left_bound"] and  player_y_postion >= map.CHECK_POINTS["ground"]-10: 
        move.hold_right()
        if player_x_postion*-1 - map.CHECK_POINTS["left_tp_left_bound"]*-1  > 250:
            move.tele()

    elif player_x_postion > map.CHECK_POINTS["left_tp_left_bound"] and player_x_postion < map.CHECK_POINTS["left_tp_right_bound"] and  player_y_postion >= map.CHECK_POINTS["ground"]-1:
        move.up()
        move.release_all()
        print(f'left_TP {player_x_postion}, {player_y_postion}')
    else:
         return            

def gen_right(player_x_postion,player_y_postion):
    """
    attacking sequence on the right 

    """
     
    if player_y_postion < map.CHECK_POINTS["middle_platform"] - 50 and player_x_postion > 0 :
         
        print(f'Gen_R {player_x_postion}, {player_y_postion}')
        move.down_jump()
        time.sleep(0.5)
        move.ult()
        time.sleep(2.5)
        
        
    else:
         return   


            
    
def to_rope(player_x_postion,player_y_postion):
    """
    player will move to the x cord of the rope and
    in between the middle platform and the ground. 
    
    """

    if player_x_postion < map.CHECK_POINTS["rope"] and player_y_postion == map.CHECK_POINTS["middle_platform"] and player_x_postion > 0:
        move.hold_right()
        move.hold_down()
        
        
    elif player_x_postion > map.CHECK_POINTS["rope"] and player_y_postion == map.CHECK_POINTS["middle_platform"] and player_x_postion > 0:
        move.hold_left()
        move.hold_down()
        
    
    else:
         return   
    



def buff(player_y_postion,round):
    """
    taking in player Y cord and stop inbetween the middle plat
    and the ground to give buffs dis mounting after buffs
    """
    
     
    if player_y_postion == random.randint(map.CHECK_POINTS["rope_upper_bound"],map.CHECK_POINTS["rope_lower_bound"]) :
           
          
        move.down_release()
        move.left_release()  
        move.right_release()
        
        if round == 2:
            move.buff()
            time.sleep(3.2)
            move.left_jump()
            
            return 1
        
        move.left_jump()

        return 1
    else:
         return 0  
    

def unstuck(player_position):
    move.release_all()
    if player_position > 0:
        move.left_jump()
    else:
        move.right_jump()    


def feed_pet(pet_info):
    """
    feeding pets >:)
    """
    if pet_info < 30:
        move.feed_pet()
