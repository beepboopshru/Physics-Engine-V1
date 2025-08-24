# main.py

from vector import Vector
from body import Body
from renderer import PygameRenderer

# Define our constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRAVITY = Vector(0, 9.8)
DELTA_TIME = 0.01

# --- Setup ---
renderer = PygameRenderer(SCREEN_WIDTH, SCREEN_HEIGHT)
body = Body(mass=10.0, position=Vector(SCREEN_WIDTH / 2, 50), velocity=Vector(100, 1000))
BODY_RADIUS = 10

# --- Main Simulation Loop ---
running = True
while running:
    # Handle user input and events (like closing the window)
    renderer.check_for_quit()

    # --- Physics update step ---
    body.update(DELTA_TIME, GRAVITY)
    
    # Check for and resolve collisions with the screen boundaries
    body.check_and_resolve_collisions(SCREEN_WIDTH, SCREEN_HEIGHT, BODY_RADIUS)

    # --- Rendering step ---
    # 1. Clear the screen
    renderer.clear_screen()
    
    # 2. Draw all objects
    renderer.draw_body(body, radius=BODY_RADIUS)

    # 3. Update the display to show what we've drawn
    renderer.flip_display()