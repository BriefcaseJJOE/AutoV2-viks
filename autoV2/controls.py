
import pydirectinput as pag
import time




def hold_left():
    pag.keyDown("left")

def left_release():
    
    pag.keyUp("left")
 

def hold_right():
    pag.keyDown("right")

def right_release():
    
    pag.keyUp("right")

    
def hold_down():
    pag.keyDown('down')

def down_release():
    
    pag.keyUp('down') 
   

def hold_up():
    pag.keyDown("up")

def up_release():
    
    pag.keyUp("up")

def up():
    pag.press("up",2)


#########################
#         JUMP          #
#########################


def jump():
    pag.press('space',3)

def rope_jump():
    pag.press('space')

def hold_jump():
    pag.keyDown('space')

def jump_release():
    pag.keyUp('space')

def left_jump():
    hold_left()
    jump()
    left_release()

def right_jump():
    hold_right()
    jump()
    right_release()


def down_jump():
    
    hold_down()
    jump()
    down_release()

##########################
#       Presses          #  
##########################

def left():
    pag.press("left")

 

def feed_pet():
    pag.press("pagedown")

def buff():
    pag.press('l')
    pag.press('v')

def ult():
    pag.press('x',3)

def tele():
    pag.press('d',2)




def top_left_action():
    hold_left()
    tele()
    left_release()
    down_jump() 

def release_all():
    down_release()
    up_release()
    left_release()
    right_release()

