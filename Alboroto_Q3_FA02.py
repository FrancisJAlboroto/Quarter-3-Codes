import numpy as np


steps = np.array([
    [5590, 5200, 4800, 5060, 5370],  # Me
    [4670, 6770, 3900, 4200, 4600],  # Mac
    [6500, 5800, 5650, 8670, 6200]   # Ken
])

print("Ken's steps on Wednesday:", steps[2, 2])

my_steps = steps[0]
print("My steps...", my_steps)

print("Updating my steps on Thursday to 5500.")

steps[0, 3] = 5500
print("My updated steps:", steps[0])