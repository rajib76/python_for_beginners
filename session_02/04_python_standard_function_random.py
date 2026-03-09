import random

# Generate a random integer between 1 and 10 (inclusive)
random_number = random.randint(1, 10)

# Generate a random floating-point number between 0 and 1
random_float = random.random()

# Shuffle a list randomly
my_list = [1, 2, 3, 4, 5]
random.shuffle(my_list)

# Select a random item from a list
random_item = random.choice(my_list)

# Generate a random sample of unique values from a range
random_sample = random.sample(range(1, 11), 3)

print("Random Integer:", random_number)
print("Random Float:", random_float)
print("Shuffled List:", my_list)
print("Random Choice:", random_item)
print("Random Sample:", random_sample)


