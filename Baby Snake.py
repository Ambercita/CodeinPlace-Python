#BABY SNAKE
from graphics import Canvas
import time
import random
    
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
SIZE = 20

# if you make this larger, the game will go slower
DELAY = 0.1

def place_goal(canvas):
    goal_pos_x = random.randint(0, CANVAS_WIDTH/SIZE - 1) * SIZE
    goal_pos_y = random.randint(0, CANVAS_HEIGHT/SIZE - 1) * SIZE
    goal = canvas.create_rectangle(goal_pos_x, goal_pos_y, goal_pos_x + SIZE, goal_pos_y + SIZE, "red")
    return goal

def move_player(canvas, player, key):
    if key == 'ArrowLeft':
        canvas.move(player, -SIZE, 0)
    elif key == 'ArrowRight':
        canvas.move(player, SIZE, 0)
    elif key == 'ArrowUp':
        canvas.move(player, 0, -SIZE)
    elif key == 'ArrowDown':
        canvas.move(player, 0, SIZE)
    return key
    
def get_pos(canvas, obj):
    x = canvas.get_left_x(obj)
    y = canvas.get_top_y(obj)
    return x, y

def main():
    # define variables
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    player = canvas.create_rectangle(0, 0, SIZE, SIZE, "blue")
    goal = place_goal(canvas)
    key = 'ArrowRight'
    score = 0
    delay = DELAY
    
    # main loop
    while 1:
        # movement
        last_key = canvas.get_last_key_press()
        
        if last_key == 'ArrowRight' or last_key == 'ArrowLeft' or last_key == 'ArrowUp' or last_key == 'ArrowDown': 
            key = last_key
            
        move_player(canvas, player, key)
        
        # check player in bounds
        player_x, player_y = get_pos(canvas, player)
        if (player_x >= CANVAS_WIDTH or player_x < 0 or player_y >= CANVAS_HEIGHT or player_y < 0):
            canvas.clear()
            canvas.create_text(CANVAS_WIDTH/2-120, CANVAS_HEIGHT/2-20, text='You died, score: ' + str(score), font_size=30)
            break;
            
        # check goal
        goal_x, goal_y = get_pos(canvas, goal)
        if (goal_x == player_x and goal_y == player_y):
            canvas.delete(goal)
            goal = place_goal(canvas)
            delay -= delay/10
            score += 1
        
        time.sleep(delay)

if __name__ == '__main__':
    main()
