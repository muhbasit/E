import statistics

data = [4.1, 4.1, 4.1, 4.2, 4.3, 4.3, 4.4, 4.5, 4.6, 4.6, 4.8, 4.9, 5.1,
        5.1, 5.2, 5.2, 5.3, 5.3, 5.3, 5.4, 5.4, 5.5, 5.6, 5.6, 5.6,
        5.7, 5.8, 5.9, 6.2, 6.2, 6.2,
        6.3, 6.4, 6.4, 6.5,
        6.6,
        6.7,
        6.7,
        6.8,
        6.8]

mean = sum(data) / len(data)
mode = statistics.mode(data)
median = statistics.median(data)

print("Mean:", mean)
print("Mode:", mode)
print("Median:", median)

""" This code uses the statistics module in Python to calculate 
the mean (sum(data) / len(data)), mode (statistics.mode(data)) and 
median (statistics.median(data)) of a list of numbers."""
