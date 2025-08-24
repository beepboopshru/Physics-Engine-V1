from vector import Vector

class Body:
    """
    A simple physical object with mass, position, and velocity.
    """
    def __init__(self, mass=1.0, position=Vector(0, 0), velocity=Vector(0, 0)):
        self.mass = float(mass)
        self.position = position
        self.velocity = velocity
        # We'll use a `force` vector to accumulate all forces in one time step
        self.force = Vector(0, 0)

    def apply_force(self, force_vector):
        """
        Adds a force to the body for this time step.
        """
        self.force += force_vector

    def update(self, dt):
        """
        Updates the body's state based on forces, velocity, and time step.
        """
        # Calculate acceleration from the accumulated force and mass
        acceleration = self.force / self.mass

        # Update velocity based on acceleration
        self.velocity += acceleration * dt

        # Update position based on the new velocity
        self.position += self.velocity * dt

        # Reset the force vector for the next time step
        self.force = Vector(0, 0)

    def __repr__(self):
        return f"Body(mass={self.mass}, pos={self.position}, vel={self.velocity})"

# --- Let's set up a simple simulation with gravity! ---
# Create a gravity vector. The value 9.8 is an approximation of gravity on Earth.
GRAVITY = Vector(0, 9.8)

# Create an object with some initial velocity
my_object = Body(mass=10.0, position=Vector(0, 0), velocity=Vector(5, -1))

print("--- Initial State ---")
print(f"Time: 0.0s, State: {my_object}")

# Our main simulation loop
time_step = 0.1  # A small time step for more accurate simulation
total_time = 0.0

for i in range(20):  # Simulate for 20 steps
    # Apply gravity to the object
    my_object.apply_force(GRAVITY * my_object.mass)

    # Update the object's state
    my_object.update(time_step)

    # Update total time and print the current state
    total_time += time_step
    print(f"Time: {total_time:.1f}s, State: {my_object}")
