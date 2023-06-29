from karel.stanfordkarel import *

"""
File: main.py
--------------------
When you finish writing this file, Karel should have repaired 
each of the columns in the temple  -----  Stone Mason Karel
"""

def main():
    for i in range(4):
        build_each_column()
        reset()
    

    
def build_each_column():
    turn_left()
    put_beeper()
    while front_is_clear():
       move()
       put_beeper()
    
    
def turn_around():
    turn_left()
    turn_left()
    
def reset():
    turn_around()
    while front_is_clear():
        move()
    turn_left()
    if front_is_clear():
     for i in range(4):
        move()
    


if __name__ == '__main__':
    main()
