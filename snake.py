import tkinter
import random

ROWS = 25
COLS = 25
TILE_SIZE = 25

WINDOW_WIDTH = TILE_SIZE * COLS
WINDOW_HEIGHT = TILE_SIZE * ROWS

class Tile:
    def __init__(self, x, y):
        self.x = x
        self.y = y

#game window
window = tkinter.Tk()
window.title("Snake Game")
window.resizable(False, False)

canvas = tkinter.Canvas(window, width=WINDOW_WIDTH, height=WINDOW_HEIGHT, bg="black", highlightthickness=0, borderwidth=0)
canvas.pack()
window.update()

#center the window
window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

window_x = (screen_width - window_width) // 2
window_y = (screen_height - window_height) // 2

window.geometry(f"{window_width}x{window_height}+{window_x}+{window_y}")

#intialize game
snake = Tile(5 * TILE_SIZE, 5 * TILE_SIZE)
food = Tile(random.randint(0, COLS - 1) * TILE_SIZE, random.randint(0, ROWS - 1) * TILE_SIZE)
snake_body = []
velocityX = 0
velocityY = 0
game_over = False
score = 0

def change_direction(event):
    global velocityX, velocityY, game_over
    if game_over:
        return
    
    if event.keysym == "Up" and velocityY != 1:
        velocityX = 0
        velocityY = -1
    elif event.keysym == "Down" and velocityY != -1:
        velocityX = 0
        velocityY = 1
    elif event.keysym == "Left" and velocityX != 1:
        velocityX = -1
        velocityY = 0
    elif event.keysym == "Right" and velocityX != -1:
        velocityX = 1
        velocityY = 0

def move():
    global snake, food, game_over, snake_body
    if game_over:
        return
    
    prev_x, prev_y = snake.x, snake.y
    
    #move snake
    snake.x += velocityX * TILE_SIZE
    snake.y += velocityY * TILE_SIZE
    
# ...existing code...
    #check for food collision
    if snake.x == food.x and snake.y == food.y:
        # grow snake at the last tail position
        if snake_body:
            last = snake_body[-1]
            snake_body.append(Tile(last.x, last.y))
        else:
            snake_body.append(Tile(prev_x, prev_y))
        # generate new food
        food.x = random.randint(0, COLS - 1) * TILE_SIZE
        food.y = random.randint(0, ROWS - 1) * TILE_SIZE
# ...existing code...
    
    #check for wall collision
    if (snake.x < 0 or snake.x >= WINDOW_WIDTH or 
        snake.y < 0 or snake.y >= WINDOW_HEIGHT):
        game_over = True
        print("Game Over!")
        return
    #check for self collision
    for tile in snake_body:
        if snake.x == tile.x and snake.y == tile.y:
            game_over = True
            print("Game Over! You collided with yourself!")
            return    
    
    # update snake body positions
    if snake_body:
        # move each segment to the position of the previous segment
        for i in range(len(snake_body) - 1, 0, -1):
            snake_body[i].x = snake_body[i - 1].x
            snake_body[i].y = snake_body[i - 1].y
        # first segment follows the previous head position
        snake_body[0].x = prev_x
        snake_body[0].y = prev_y
    
def draw():
    global snake
    move()
    
    canvas.delete("all")  #clear the canvas
    
    #draw food
    canvas.create_rectangle(food.x, food.y, food.x + TILE_SIZE, food.y + TILE_SIZE, fill="red", outline="black")
    
    #draw snake
    canvas.create_rectangle(snake.x, snake.y, snake.x + TILE_SIZE, snake.y + TILE_SIZE, fill="lime green", outline="black")

    #draw snake body
    for tile in snake_body:
        canvas.create_rectangle(tile.x, tile.y, tile.x + TILE_SIZE, tile.y + TILE_SIZE, fill="lime green", outline="black")
    
    window.after(100, draw) #100ms = 1/10 second, 10 FPS
    
draw()


window.bind("<KeyPress>", change_direction)
window.mainloop()
