# import pygame
# import random

# pygame.init()
# done = None

# while not done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True

#     pygame.display.flip()

# pygame.quit()

# '''↓↓↓ YOUR CODE HERE ↓↓↓'''
# star_numbers = 50 # Should it be an integer or a float number? You will be able to change the decision later
# speed = 3.5 # Should it be an integer or a float number? You will be able to change the decision later
# # Each star consists of an X-coordinate, a Y-coordinate, a Z-distance (distance to the star), and a color. 
# # What structure will you use to store the stars? What object will store information about the star? Tuple, list, dictionary? Justify your choices
# stars = []
# '''↑↑↑ YOUR CODE HERE ↑↑↑'''

# import random

# def new_star() -> list:
#     '''↓↓↓ YOUR CODE HERE ↓↓↓'''
#     center_x = screen_width // 2
#     center_y = screen_height // 2
#     x = random.randint(-center_x, center_x)
#     y = random.randint(-center_y, center_y)
#     z_distance = 256
#     color = 0
#     star = [x, y, z_distance, color]
#     '''↑↑↑ YOUR CODE HERE ↑↑↑'''
    
#     return star

# for i in range(star_numbers):
#     stars.append(new_star())

# for i in range(100):
#     star_sample = new_star()
#     assert len(star_sample) == 4, 'The star is defined by 4 numbers'
#     assert -(screen_width // 2) <= star_sample[0] <= screen_width // 2, 'coordinates should have coordinates in the intervals (- screen width: + screen width, - screen height, + screen height)'
#     assert -(screen_height // 2) <= star_sample[1] <= screen_height // 2 , 'coordinates should have coordinates in the intervals (- screen width: + screen width, - screen height, + screen height)'
#     assert star_sample[2] == 256, 'Z coordinate has to be equal 256'
#     assert star_sample[3] == 0, 'Start color has to be equal to 0'
# print('Seems fine, good job!')

# def move_and_check(star:list) -> list:
    
#     '''↓↓↓ YOUR CODE HERE ↓↓↓'''
#     center_x = screen_width // 2
#     center_y = screen_height // 2
#     x = center_x + (star[0] * (center_x / star[2]))
#     y = center_y + (star[1] * (center_y / star[2]))
#     star[2] -= speed

#     # If the coordinates go beyond the screen, we generate a new star.
#     if x < 0 or x > screen_width or y < 0 or y > screen_height:
#         star = new_star()
    
#     # If the color has not reached maximum brightness, increase the color.
#     if star[3] < 255:
#         star[3] += 0.15
    
#     #  If suddenly the color becomes more than acceptable, then set it to 255
#     if star[3] > 255:			# Если вдруг цвет стал больше допустимого, то выставляем его как 255
#         star[3] = 255
    
#     '''↑↑↑ YOUR CODE HERE ↑↑↑'''
#     return star

# stars = [new_star() for _ in range(50)]
# for i in range(1000):
#     for star in stars:
#         move_and_check(star)
# print('Seems good!')

# def draw_star(star:list) -> None:
#     '''↓↓↓ YOUR CODE HERE ↓↓↓'''
#     x = center_x + (star[0] * (center_x / star[2]))
#     y = center_y + (star[1] * (center_y / star[2]))
#     '''↑↑↑ YOUR CODE HERE ↑↑↑'''
#     pygame.draw.circle(screen, (star[3], star[3], star[3]), (x, y), 3)


import pygame
import random

'''↓↓↓ YOUR CODE HERE ↓↓↓'''
screen_width = screen_height = 1444
'''↑↑↑ YOUR CODE HERE ↑↑↑'''

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
done = False

'''↓↓↓ YOUR CODE HERE ↓↓↓'''
number_of_stars = 50
speed =	1.5	
stars = []

def new_star() -> list:
    '''↓↓↓ YOUR CODE HERE ↓↓↓'''
    center_x = screen_width // 2
    center_y = screen_height // 2
    x = random.randint(-center_x, center_x)
    y = random.randint(-center_y, center_y)
    z_distance = 256
    color = 0
    star = [x, y, z_distance, color]
    '''↑↑↑ YOUR CODE HERE ↑↑↑'''
    
    return star

def move_and_check(star:list) -> list:
    
    '''↓↓↓ YOUR CODE HERE ↓↓↓'''
    center_x = screen_width // 2
    center_y = screen_height // 2
    x = center_x + (star[0] * (center_x / star[2]))
    y = center_y + (star[1] * (center_y / star[2]))
    star[2] -= speed

    # If the coordinates go beyond the screen, we generate a new star.
    if x < 0 or x > screen_width or y < 0 or y > screen_height:
        star = new_star()
    
    # If the color has not reached maximum brightness, increase the color.
    if star[3] < 255:
        star[3] += 0.15
    
    #  If suddenly the color becomes more than acceptable, then set it to 255
    if star[3] > 255:			# Если вдруг цвет стал больше допустимого, то выставляем его как 255
        star[3] = 255
    
    '''↑↑↑ YOUR CODE HERE ↑↑↑'''
    return star

def draw_star(star:list) -> None:
    '''↓↓↓ YOUR CODE HERE ↓↓↓'''
    center_x = screen_width // 2
    center_y = screen_height // 2
    x = center_x + (star[0] * (center_x / star[2]))
    y = center_y + (star[1] * (center_y / star[2]))
    '''↑↑↑ YOUR CODE HERE ↑↑↑'''
    pygame.draw.circle(screen, (star[3], star[3], star[3]), (x, y), 3)

# def new_star():
#     return [random.uniform(-1, 1), random.uniform(-1, 1), 1, random.randint(100, 255)]
'''↑↑↑ YOUR CODE HERE ↑↑↑'''

for i in range(number_of_stars):		
    stars.append(new_star())

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((0, 0, 0))  

    for i in range(number_of_stars):		
        s = stars[i]			    		
        
        '''↓↓↓ YOUR CODE HERE ↓↓↓'''
        s[0] += speed * s[2]
        s[1] += speed * s[2]
        '''↑↑↑ YOUR CODE HERE ↑↑↑'''

        # if abs(s[0]) > 1 or abs(s[1]) > 1:
        if abs(s[0]) > 1 or abs(s[1]) > 1:
            stars[i] = new_star()
        '''↓↓↓ YOUR CODE HERE ↓↓↓'''
        draw_star(s)
        '''↑↑↑ YOUR CODE HERE ↑↑↑'''

    pygame.display.flip()
pygame.quit()