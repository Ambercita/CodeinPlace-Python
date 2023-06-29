from karel.stanfordkarel import *

"""
File: PuzzleKarel.py
--------------------
Karel should finish the puzzle by picking up the last beeper 
(puzzle piece) and placing it in the right spot. Karel should 
end in the same position Karel starts in -- the bottom left 
corner of the world.  Jigsaw Karel
"""


def main():
    move_pick_last_beeper()
    put_beeper_in_place()
    return_home()
    
def move_pick_last_beeper():
    while no_beepers_present():
         move()
    pick_beeper()
    
def put_beeper_in_place():
    move()
    turn_left()
    while no_beepers_present():
        move()
    turn_around()
    move()
    put_beeper()
    
def return_home():
    
    while front_is_clear():
        move()
    turn_right()
    while front_is_clear():
        move()
    turn_around()
    
    
def turn_around():
    turn_left()
    turn_left()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()
        
    


# There is no need to edit code beyond this point
if __name__ == '__main__':
    main()
