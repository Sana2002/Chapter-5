# Create a list to store dictionaries of pets
pets = []

# Create a dictionary for a pet cat
cat = {
    # Set the key 'kind' to the value 'Cat'
    'kind': 'Cat',
    # Set the key 'owner' to the value 'Afrah'
    'owner': 'Afrah'
}
# Add the cat dictionary to the pets list
pets.append(cat)

# Create a dictionary for a pet Dog
dog = {
    # Set the key 'kind' to the value 'Dog'
    'kind': 'Dog',
    # Set the key 'owner' to the value 'Ahmed'
    'owner': 'Ahmed'
}
# Add the dog dictionary to the pets list
pets.append(dog)

# Create a dictionary for a pet Fish
fish = {
    # Set the key 'kind' to the value 'Fish'
    'kind': 'Fish',
    # Set the key 'owner' to the value 'Sara'
    'owner': 'Sara'
}
# Add the fish dictionary to the pets list
pets.append(fish)

# Loop through the pets list and print information about each pet
for pet in pets:
    print("Kind: " + pet['kind'])
    print("Owner: " + pet['owner'])

