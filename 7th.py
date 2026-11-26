# Find max, second max, min, second min

arr = [10, 3, 45, 6, 8, 23, 42, 56, 38]

max = min = arr[0]

smin = smax = arr[0]

for num in arr:

    if num > max:
        smax = max
        max = num

    elif num > smax and num != max:
        smax = num

    if num < min:
        smin = min
        min = num

    elif num < smin and num != min:
        smin = num

print("Maximum:", max)
print("Second Maximum:", smax)
print("Minimum:", min)
print("Second Minimum:", smin)