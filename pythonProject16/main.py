from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController
# from ursina.shaders import lit_with_shadows_shader

import random

import worldsave
import world
import player

app = Ursina()
world = world.WORLD()

player = FirstPersonController()

window.title = 'My Game'
window.exit_button.visible = True
window.fps_counter.enabled = True
window.fullscreen = True

movement_speed = 15

# mouse.locked = True

# EditorCamera()

cube = Entity(model = "cube", scale = (2, 2, 2), position=(0, 0, 0))
ground = Entity(model = "cube", scale = (200, 0.5, 200), position = (0, -3, 0), color = color.gray)

def update():
    cube.rotation_y += time.dt * 100

def look(mouse_pos):
    camera.rotation_y = mouse_pos[0] * 10 # left, right
    camera.rotation_x = mouse_pos[1] * -10 # up, down

def move(held_keys):
    if held_keys['s']:
        camera.position += (0, 0, -time.dt * movement_speed)
    if held_keys['w']:
        camera.position += (0, 0, time.dt * movement_speed)

    if held_keys['d']:
        camera.position += (time.dt * movement_speed, 0, 0)
    if held_keys['a']:
        camera.position += (-time.dt * movement_speed, 0, 0)

def input(key):
    if key == "e":
        cube.color = color.rgb(random.randint(1, 255), random.randint(1, 255), random.randint(1, 255))
move(held_keys)
app.run()