import numpy as np

steps = np.array([
    [5590, 5200, 4800, 5060, 5370],
    [4670, 6770, 3900, 4200, 4600],
    [6500, 5800, 5650, 8670, 6200]
])

names = ["Me", "Mac", "Ken"]

print("Step Count Summary:\n")

for i in range(len(steps)):
    total = steps[i].sum()
    average = steps[i].mean()
    
    print(names[i], "steps:", steps[i])
    print("Total steps:", total)
    print("Average steps:", round(average, 2))
    print()

max_steps = steps.max()
print("Highest step count recorded:", max_steps)