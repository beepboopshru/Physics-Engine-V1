import math

class Vector:
    """
    A 3D Vector class for position, velocity, and more.
    """
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

    def __add__(self, other):
        """Vector addition."""
        return Vector(self.x + other.x, self.y + other.y, self.z + other.z)

    def __sub__(self, other):
        """Vector subtraction."""
        return Vector(self.x - other.x, self.y - other.y, self.z - other.z)

    def __mul__(self, scalar):
        """Scalar multiplication."""
        return Vector(self.x * scalar, self.y * scalar, self.z * scalar)

    def __rmul__(self, scalar):
        """Scalar multiplication (reversed)."""
        return self.__mul__(scalar)

    def __truediv__(self, scalar):
        """Scalar division."""
        return Vector(self.x / scalar, self.y / scalar, self.z / scalar)
    
    def magnitude_squared(self):
        """Calculates the squared magnitude (length) of the vector."""
        return self.x**2 + self.y**2 + self.z**2

    def magnitude(self):
        """Calculates the magnitude of the vector."""
        return math.sqrt(self.magnitude_squared())
    
    def normalize(self):
        """Returns a new vector with the same direction but a magnitude of 1."""
        mag = self.magnitude()
        if mag == 0:
            return Vector(0, 0, 0)
        return self / mag

    def dot(self, other):
        """Calculates the dot product of two vectors."""
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def cross(self, other):
        """Calculates the cross product of two vectors."""
        x = self.y * other.z - self.z * other.y
        y = self.z * other.x - self.x * other.z
        z = self.x * other.y - self.y * other.x
        return Vector(x, y, z)

    def __repr__(self):
        """Provides a string representation of the vector."""
        return f"Vector({self.x:.2f}, {self.y:.2f}, {self.z:.2f})"


class Body:
    """
    A simple 3D physical object with mass, position, and velocity.
    """
    def __init__(self, mass=1.0, position=Vector(0, 0, 0), velocity=Vector(0, 0, 0), radius=1.0):
        self.mass = float(mass)
        self.position = position
        self.velocity = velocity
        self.force = Vector(0, 0, 0)
        self.radius = radius

    def apply_force(self, force_vector):
        self.force += force_vector

    def update(self, dt):
        acceleration = self.force / self.mass
        self.velocity += acceleration * dt
        self.position += self.velocity * dt
        self.force = Vector(0, 0, 0)

    def __repr__(self):
        return f"Body(mass={self.mass}, pos={self.position}, vel={self.velocity})"

# --- Let's test our new 3D classes! ---
# Let's set up a simple simulation with 3D gravity
GRAVITY = Vector(0, -9.8, 0) # Gravity acting downwards along the Y-axis

# Create an object with some initial velocity
my_object = Body(mass=10.0, position=Vector(5, 50, 10), velocity=Vector(2, 0, -1))

print("--- Initial State ---")
print(f"Time: 0.0s, State: {my_object}")

# Our simple simulation loop
time_step = 0.1
for i in range(20):
    my_object.apply_force(GRAVITY * my_object.mass)
    my_object.update(time_step)
    print(f"Time: {(i + 1) * time_step:.1f}s, State: {my_object}")