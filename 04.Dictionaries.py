person = {
    "name": "John Doe",
    "age": 30,
    "city": "New York",
}

# Accessing a value using the key
name = person.get("name") # Using get() to avoid KeyError if key doesn't exist
area = person.get("area", "Not specified")  # Default value if key not found
city = person['city']  # Direct access, will raise KeyError if key doesn't exist
print("Name:", name if name else "Not found")
print("Area:", area)
print("City:", city)


# Adding/Updating a key-value pair
person["city"] = "Singapore"  # Update existing key
person["email"] = "test@gmail.com"
print("Updated person dictionary:", person)

# Removing a key-value pair
del person["age"]  # Removes key, Raise error if not exist
person.pop("age", None)  # Removes key and returns value, None if key doesn't exist
print("After removing age:", person)


# Looping Through a dictionary
for key, value in person.items():
    print(f"{key}: {value}")


# Clear, Copy, FromKeys and Get methods
# Clear removes all items from the dictionary
person.clear()
print("After clear, person dictionary:", person)

# Copy creates a shallow copy of the dictionary
person = {"name": "John Doe", "age": 30, "city": "New York"}
person_copy = person.copy()
print("Copied person dictionary:", person_copy)

# FromKeys creates a new dictionary with specified keys and a default value
keys = ["name", "age", "city"]
default_value = "Unknown"
new_person = dict.fromkeys(keys, default_value)
print("New person dictionary from keys:", new_person)

# Get returns the value for a specified key, or a default value if the key is not found
age = person.get("age", "Not specified")
print("Age using get method:", age)


# POP, POPITEMS AND UPDATE methods
# Pop removes a specified key and returns its value
person = {"name": "John Doe", "age": 30, "city": "New York"}
removed_age = person.pop("age", "Not found")
print("Removed age:", removed_age)

# Popitem removes and returns the last inserted key-value pair
last_item = person.popitem()  # Returns a tuple (key, value)
print("Last item removed:", last_item)

# Update merges two dictionaries, updating existing keys and adding new ones
new_info = {"email": "testing",
            "city": "Los Angeles"}  # This will update the city
person.update(new_info) 
print("After update, person dictionary:", person)
