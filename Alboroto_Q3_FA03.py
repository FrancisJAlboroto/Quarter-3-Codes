
import numpy as np

names = ["Me", "Mac", "Ken"]
steps = np.array([
    [5590, 5200, 4800, 5060, 5370],  # Me
    [4670, 6770, 3900, 4200, 4600],  # Mac
    [6500, 5800, 5650, 8670, 6200]   # Ken
])
total_steps = steps.sum(axis=1)

print("Total steps for each person:")
for i in range(len(names)):
    print(names[i] + ":", total_steps[i])

max_index = total_steps.argmax()
print("Person with highest steps:", names[max_index], "with", total_steps[max_index], "steps")

difference = total_steps.max() - total_steps.min()
print("Difference between highest and lowest total:", difference)