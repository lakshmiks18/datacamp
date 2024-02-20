circ_parab = dict()

for x in range_x:
    for y in range_y:       
        # Calculate the value for z
        z = x**2 + y**2
        # Create a new key for the dictionary
        key = (x, y)
        # Create a new key-value pair      
        circ_parab[key] = z
