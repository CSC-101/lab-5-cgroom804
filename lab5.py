from cmath import sqrt

import data

# Write your functions for each part in the space below.

# Part 1
   # The function for Part 1 should be within the class in data.py.


# Part 2
   # The function for Part 2 should be within the class in data.py.


# Part 3
def time_add(time1: data.Time, time2: data.Time) -> data.Time: # arguments time1 and time2 are expected to be instances of the class Time, and the function is expected to output an instance of class Time
    seconds = time1.second + time2.second #calculates total seconds
    minutes = time1.minute + time2.minute + seconds//60 #calculates total minutes
    hours = time1.hour + time2.hour + minutes//60 # calculates total hours
    seconds %= 60 # calculates remaining seconds
    minutes %= 60 # calculates remaining minutes
    return data.Time(hours, minutes, seconds) # returns the added time as an instance of class Time

# Part 4
def is_descending(lst: list[float]) -> bool: # the argument lst is expected to be a list containing floats, and the function is expected to output a bool
    return True if lst == sorted(lst,reverse = True) else False # returns true if the lst is the same as the lst in descending order, otherwise returns false


# Part 5
def largest_between(lst:list[int], lower:int, upper:int) -> int | None: # The arguments lst, is expected to be a list containing integers, while lower and upper are expected to be integers, and the function is expected to output an integer
    if lower > upper: # if an invalid range is provided
        return None

    lower = max(0, lower) # sets lower to 0 if lower is out of range of lst
    upper = min(len(lst) - 1, upper) # sets upper to the last number in lst if upper is out of range of lst

    if lower > upper: # if lower is now greater than upper, the provided range is completely outside lst
        return None

    largest = lower #sets the variable largest to the value of argument lower

    for i in range(lower, upper + 1): # repeats for the number of numbers in lst
        if lst[i] > lst[largest]: #if the next number is greater than the current largest number
            largest = i # set the variable largest equal to the next number
    return largest #returns the largest number within the provided valid range of lst


# Part 6
def furthest_from_origin(points: list[data.Point]) -> int|None:

    if not points:
        return None

    # Initialize with the first point as the furthest point
    furthest_index = 0
    max_distance = abs(complex(points[0].x ** 2 + points[0].y ** 2))

    # Loop through all points to find the furthest one
    for i in range(1, len(points)):
        distance = abs(complex(points[i].x ** 2 + points[i].y ** 2))
        if distance > max_distance:
            max_distance = distance
            furthest_index = i

    return furthest_index