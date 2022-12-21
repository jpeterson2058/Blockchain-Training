# Imports
import hashlib

# Create an instance of the sha256 hashing function
sha = hashlib.sha256()

# Create the data input to be hashed
my_data = "Nothing in the world can take the place of persistence. Talent will not; nothing is more common than unsuccessful men with talent. Genius will not; unrewarded genius is almost a proverb. Education will not; the world is full of educated derelicts. Persistence and determination alone are omnipotent. The slogan Press On! has solved and always will solve the problems of the human race."

# Encode the data using the encode function
encoded_data = my_data.encode()

# Hash the encoded data
sha.update(encoded_data)

# Print the hash code
print(sha.hexdigest())
