#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a) O(n) => Linear Time, where n represents the length of the array. As n increases, performance increases linearly since the number of operations increases with n. As such, it take linear timeto find n.

b) O(n^2) => Quadratic Time, where every element is being compared to every other element. Also, nested for loops are a great indicator of quadratic time.

c) O(n) => Linear Time, where n represents the number of times the function is being called. This was a tricky one since recursive functions are typically Exponential Time O(2^n).

## Exercise II

So, we want to find the floor where the number of eggs broken are minimized.

For this one, I would use merge sort O(n log n) algorithm.

I would split the array (n-stories) into the middle, leaving left & right sub arrays and drop an egg from the middle position. If the eggs break, then I would get rid of everything to the right - since those represent the highest floors and start again with the left array - those representingthe lowest floors.
I'll repeat this process on the left subarray by finding the middle element.

Pseudo Code Attempt:

#store all the floors we've checked into a list => floors = []
#create bases indexes for the left & right arrays
#find the middle_floor/index and drop an egg
#if the egg is broken, get rid of all nums to the right of middle floor
#then repeat the process until we find the floor where the egg is not broken
