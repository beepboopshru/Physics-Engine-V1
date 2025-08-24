import pygame
from pygame.locals import *
from OpenGL.GL import *
from OpenGL.GLU import *
import math
import sys

# --- Your Vector Class (3D) ---
class Vector:
    """A 3D Vector class for position, velocity, and more."""
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    def __rmul__(self, scalar):
        return self.__mul__(scalar)

    def __truediv__(self, scalar):
        return Vector(self.x / scalar, self.y / scalar, self.z / scalar)
    
    def magnitude_squared(self):
        return self.x**2 + self.y**2 + self.z**2

    def magnitude(self):
        return math.sqrt(self.magnitude_squared())
    
    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            return Vector(0, 0, 0)
        return self / mag

    def dot(self, other):
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def cross(self, other):
        x = self.y * other.z - self.z * other.y
        y = self.z * other.x - self.x * other.z
        z = self.x * other.y - self.y * other.x
        return Vector(x, y, z)

    def __repr__(self):
        return f"Vector({self.x:.2f}, {self.y:.2f}, {self.z:.2f})"

# --- Your Body Class (3D) ---
class Body:
    """A 3D physical object with mass, position, and velocity."""
    def __init__(self, mass=1.0, position=Vector(0, 0, 0), velocity=Vector(0, 0, 0), radius=1.0, color=(1, 1, 1)):
        self.mass = float(mass)
        self.position = position
        self.velocity = velocity
        self.force = Vector(0, 0, 0)
        self.radius = radius
        self.color = color

    def apply_force(self, force_vector):
        self.force += force_vector

    def update(self, dt):
        acceleration = self.force / self.mass
        self.velocity += acceleration * dt
        self.position += self.velocity * dt
        self.force = Vector(0, 0, 0)

    def __repr__(self):
        return f"Body(mass={self.mass}, pos={self.position}, vel={self.velocity})"

# --- OpenGL Setup and Drawing Functions ---
def setup_opengl():
    glEnable(GL_DEPTH_TEST)
    glClearColor(0.5, 0.5, 0.5, 1)

    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45, (SCREEN_WIDTH / SCREEN_HEIGHT), 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    
def draw_grid():
    glBegin(GL_LINES)
    glColor3f(0.2, 0.2, 0.2)

    for z in range(-20, 21, 2):
        glVertex3f(-20, 0, z)
        glVertex3f(20, 0, z)

    for x in range(-20, 21, 2):
        glVertex3f(x, 0, -20)
        glVertex3f(x, 0, 20)
    
    glEnd()

def draw_sphere(x, y, z, radius, color):
    glPushMatrix()
    glTranslatef(x, y, z)
    
    glColor3f(color[0], color[1], color[2])
    
    sphere = gluNewQuadric()
    gluQuadricNormals(sphere, GLU_SMOOTH)
    gluSphere(sphere, radius, 32, 32)
    gluDeleteQuadric(sphere)
    
    glPopMatrix()
    
# --- New function for floor collision ---
def resolve_floor_collision(body):
    if body.position.y - body.radius < 0:
        body.velocity.y *= -0.8
        body.position.y = body.radius

# --- Main Simulation Loop ---
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
pygame.init()
pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), DOUBLEBUF | OPENGL)

# Hide and lock the mouse cursor to the window
pygame.mouse.set_visible(False)
pygame.event.set_grab(True)

setup_opengl()
clock = pygame.time.Clock()

# Set up our 3D world with a grid
GRAVITY = Vector(0, -9.8, 0)
bodies = [
    Body(mass=1.0, position=Vector(0, 20, -10), velocity=Vector(0, 0, 0), radius=2, color=(1, 1, 1)),
    Body(mass=1.0, position=Vector(5, 30, -15), velocity=Vector(0, 0, 0), radius=2, color=(1, 0, 0)),
]

# Camera State Variables
camera_pos = Vector(10, 10, 10)
camera_yaw = -135.0
camera_pitch = -30.0
mouse_sensitivity = 0.2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            dx, dy = event.rel
            camera_yaw += dx * mouse_sensitivity
            camera_pitch -= dy * mouse_sensitivity
            if camera_pitch > 89.0: camera_pitch = 89.0
            if camera_pitch < -89.0: camera_pitch = -89.0

    dt = clock.tick(60) / 1000.0

    # Physics update
    for body in bodies:
        body.apply_force(GRAVITY * body.mass)
        body.update(dt)

        # Check for floor collision after each body is updated
        resolve_floor_collision(body)

    # Rendering
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    
    # Calculate the camera's look direction
    yaw_rad = math.radians(camera_yaw)
    pitch_rad = math.radians(camera_pitch)
    
    look_dir = Vector(
        math.cos(yaw_rad) * math.cos(pitch_rad),
        math.sin(pitch_rad),
        math.sin(yaw_rad) * math.cos(pitch_rad)
    )
    
    camera_look_at = camera_pos + look_dir
    gluLookAt(camera_pos.x, camera_pos.y, camera_pos.z,
              camera_look_at.x, camera_look_at.y, camera_look_at.z,
              0, 1, 0)

    # Draw the grid first
    draw_grid()

    # Draw all the bodies
    for body in bodies:
        draw_sphere(body.position.x, body.position.y, body.position.z, body.radius, body.color)

    pygame.display.flip()

pygame.quit()
sys.exit()