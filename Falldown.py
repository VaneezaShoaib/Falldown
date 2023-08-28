#VANEEZA SHOAIB, ZHW9ZC

import uvage
camera= uvage.Camera(800, 600)

screen_width = 800
screen_height= 600
box = uvage.from_color(400, 300, "green", 50, 50)
box_velocity = 15
player_speed= 14
score = 0
game_on = True

ticker = 0

top = uvage.from_color(screen_width / 2, screen_height + 5, "black", screen_width, 10)
floor = uvage.from_color(screen_width / 2, screen_height - 5, "black", screen_width, 10)
walls = [
    uvage.from_color(0, screen_height / 2, 'black', 50, screen_height),
    uvage.from_color(600, screen_height / 2, 'black', 50, screen_height),
]
platforms = [
    uvage.from_color(200, 200, 'blue', 400 , 30),
    uvage.from_color(675, 200,'blue', 290 , 30),
    uvage.from_color(125, 400,'blue', 400 , 30),
    uvage.from_color(650, 400,'blue', 300 , 30),
    uvage.from_color(250, 600, 'blue', 500, 30),
    uvage.from_color(750, 600, 'blue', 200, 30),
]

box.yspeed = box_velocity


def tick():
    ''' game execution'''
    global game_on
    global score
    if game_on == True:
        box.move_speed()
        score += .5

    if uvage.is_pressing("space"):
        game_on = True
    if uvage.is_pressing("left arrow"):
        box.x -= player_speed
    if uvage.is_pressing("right arrow"):
        box.x += player_speed

    for platform in platforms:
        if game_on:
            if box.touches(platform):
                box.yspeed = 0
                box.move_to_stop_overlapping(platform)
            platform.y -= 4

    box.yspeed += 1
    if box.bottom_touches(floor):
        box.yspeed = 0
    box.move_speed()

    camera.clear("black")
    if box.y < 0:
        box.yspeed= 0
        camera.draw(uvage.from_text(300, 300, "GAME OVER", 70, "blue", bold = False))
        game_on = False


    camera.draw(uvage.from_text(300, 50, str(int(score)), 50, "Red", bold=True))

    for wall in walls:
        camera.draw(wall)

    for platform in platforms:
        if platform.y <= 0:
            platform.y = 600
        camera.draw(platform)

    camera.draw(box)

    camera.display()


uvage.timer_loop(30, tick)