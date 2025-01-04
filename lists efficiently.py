# create a function to find the common elements from 2 lists

def find_common_elements(list1, list2):
    try:
        # checking if both inputs are lists
        if not isinstance(list1, list) or not isinstance(list2, list):
            raise TypeError("Both inputs must be lists.")
        # Find the common elements using set intersection
        common_elements = list(set(list1) & set(list2))

        return  common_elements
    except TypeError as e:
        return f"Error: {e}"

    except Exception as e:
        return f"An unexpected error occurred: {e}"

list1 = [1,2,3,4,5,6,10,80,55,100]
list2 = [2,5,6,80,70,90,100,32,45]
results = find_common_elements(list1, list2)

print(results)