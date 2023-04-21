## this was yoinked from https://pypi.org/project/ursina/#:~:text=An%20easy%20to%20use%20game%20engine%2Fframework%20for%20python.



from ursina import *           # this will import everything we need from ursina with just one line.

app = Ursina()

player = Entity(
    model = 'sphere' ,           # finds a 3d model by name
    color = color.orange,
    )

def update():                  # update gets automatically called by the engine.
    player.x += held_keys['d'] * .1
    player.x -= held_keys['a'] * .1


app.run() 