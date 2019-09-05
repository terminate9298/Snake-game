from initialisers import *
from classes import *
import pygame
import random
import tkinter as tk
from tkinter import messagebox
def drawGrid(surface):
    sizeBtwn = int(WINDOW_WIDTH//ROWS)

    x=0
    y=0
    for l in range(ROWS):
        x += sizeBtwn
        y += sizeBtwn

        pygame.draw.line(surface , BLACK , (x,0) , (x,WINDOW_WIDTH))
        pygame.draw.line(surface , BLACK , (0,y) , (WINDOW_HEIGHT,y))

def randomSnack(ROWS , snake):
        position  = snake.body
        while True:
                x = random.randrange(ROWS)
                y = random.randrange(ROWS)
                if len(list(filter(lambda z: z.pos == (x,y) , position))) > 0:
                        continue
                else:
                        break
        return (x,y)

def message_box(subject , content):
	root = tk.Tk()
	root.attribute("-topmost" , True)
	root.withdraw()
	messagebox.showinfo(subject , content)
	try:
		root.destroy()
	except:
		pass


def reDrawWindow(win,s,snack):
    win.fill(WHITE)
    s.draw(win)
    drawGrid(win)
    snack.draw(win)
    pygame.display.update()

def main():
	win = pygame.display.set_mode((WINDOW_WIDTH , WINDOW_HEIGHT))
	s = snake(RED , (SNAKE_START_COLUMN,SNAKE_START_ROW))
	snack = cube(randomSnack(ROWS , s) , color = GREEN)
	clock = pygame.time.Clock()
	while flag:
		pygame.time.delay(50)
		clock.tick(10)
		s.move()
		if s.body[0].pos ==snack.pos:
			s.addCube()
			snack = cube(randomSnack(ROWS , s ), color = GREEN)
		for x in range(len(s.body)):
			if s.body[x].pos in list(map(lambda z:z.pos , s.body[x+1 :])):
				message_box('You Lost..' , 'Play Again.!!!')
				s.reset((SNAKE_START_COLUMN,SNAKE_START_ROW))
				break
		reDrawWindow(win,s ,snack)
