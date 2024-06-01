from classes import Reader 
import keyboard as k
import funct as f


if __name__=="__main__":
    player = Reader()
    buff = 0
    
   

    while True :

       
        f.to_right_tp(player.read_x(),player.read_y())
                
        f.genesis(player.read_x(),player.read_y())
        
        f.to_left_tp(player.read_x(),player.read_y())
                
        f.gen_right(player.read_x(),player.read_y())
                    
        f.to_rope(player.read_x() ,player.read_y())

        f.buff(player.read_y(), buff)

        f.feed_pet(player.read_pets())
        
        
        buff += int(f.buff(player.read_y(), buff))

        if buff >= 3:
            buff = 0  

        

        if k.is_pressed('esc'):
            break
        
        print(f'player_new_position {player.read_x()}')
       
           

       