def achatar(array):
  
    if array == [] :

        return []     
             
    elif isinstance(array[0], list):

        return achatar(array[0]) + achatar(array[1:])

    else:

        return [array[0]] + achatar(array[1:])
      
array = [1, 2, [4, 2], 5, [2, [1, 2, 3], [[1]]], 8]
print(achatar(array))