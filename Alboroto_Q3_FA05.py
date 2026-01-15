import numpy as np

names = ["Me", "Mac", "Ken"]
steps = np.array([
    [5590, 5200, 4800, 5060, 5370],  # Me
    [4670, 6770, 3900, 4200, 4600],  # Mac
    [6500, 5800, 5650, 8670, 6200]   # Ken
])

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

total_a_day = []
for i in range(steps.shape[1]):  
    day_total = steps[:, i].sum()
    total_a_day.append(day_total)
    print(days[i] + ":", day_total)

most_active_index = total_a_day.index(max(total_a_day))
print("Most active day overall:", days[most_active_index])