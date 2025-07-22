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
velocityX = 0
velocityY = 0



def draw():
    global snake
    
    #draw snake
    canvas.create_rectangle(snake.x, snake.y, snake.x + TILE_SIZE, snake.y + TILE_SIZE, fill="lime green", outline="black")
    
    #draw food
    canvas.create_rectangle(food.x, food.y, food.x + TILE_SIZE, food.y + TILE_SIZE, fill="red", outline="black")
    
    window.after(100, draw) #100ms = 1/10 second, 10 FPS
    
draw()


window.bind("<KeyPress>")
window.mainloop()