# create a function to find the common elements from 2 tuples

def concat_tuples(tuple1, tuple2):
    try:
        # checking if both inputs are tuples
        if not isinstance(tuple1, tuple) or not isinstance(tuple2, tuple):
            raise TypeError("Both inputs must be tuples.")
        # Concatenate the tuples using + sign
        concatenated_tuple = tuple1 + tuple2

        return  concatenated_tuple

    except TypeError as e:
        return f"Error: {e}"

    except Exception as e:
        return f"An unexpected error occurred: {e}"

tuple1 = (1,2,3,4,5,6,10,80,55,100)
tuple2 = (2,5,6,80,70,90,100,32,45)

results = concat_tuples(tuple1, tuple2)

print(results)