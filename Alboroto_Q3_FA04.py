import numpy as np

steps = np.array([
    [5590, 5200, 4800, 5060, 5370],  # Me
    [4670, 6770, 3900, 4200, 4600],  # Mac
    [6500, 5800, 5650, 8670, 6200]   # Ken
])

for i, classmate_steps in enumerate(steps, start=1):
    total = np.sum(classmate_steps)
    average = np.mean(classmate_steps)
    min_steps = np.min(classmate_steps)
    max_steps = np.max(classmate_steps)
    print(f"Classmate {i} - Total Steps: {total} | Average: {average:.1f} | Min: {min_steps} | Max: {max_steps}")

overall_min = np.min(steps)
overall_max = np.max(steps)
print(f"\nOverall Min Steps: {overall_min}")
print(f"Overall Max Steps: {overall_max}")