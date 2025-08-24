# 3D Physics Engine

A simple 3D physics simulation and rendering engine built from scratch using Python. This project serves as a step-by-step tutorial for understanding core physics and 3D graphics principles without relying on complex game engines.

## Features

- **Custom Vector Class:** A foundational 3D vector class for all position, velocity, and force calculations.
- **Physics Simulation:** Objects fall under the influence of gravity and have their state updated using simple Euler integration.
- **3D Rendering:** Basic 3D scene rendering using Pygame and PyOpenGL.
- **Interactive Camera:** A fully-featured, mouse-controlled "free-look" camera to navigate the 3D world.
- **Collision Detection & Response:**
    - **Floor Collision:** Spheres bounce realistically off a grid-based floor.
    - **Sphere-to-Sphere Collision:** Momentum and velocity are conserved when two spheres collide.
- **Procedural 3D World:** A simple 2D grid is drawn on the XZ-plane to provide visual reference.

## Getting Started

Follow these steps to set up and run the simulation on your local machine.

### Prerequisites

- Python 3.7 or newer
- Git (optional, for version control)

### Installation

1. **Clone the repository** (if you're using Git):
   ```sh
   git clone [https://github.com/beepboopshru/Physics-Engine-V1.git](https://github.com/beepboopshru/Physics-Engine-V1.git)
   cd Physics-Engine-V1
