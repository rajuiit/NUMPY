# Masked arrays are a data structure used in programming and data analysis to handle missing or invalid values in an array. They are particularly useful when working with numerical data where some elements may be missing or have invalid values.

# In a masked array, each element of the array is associated with a mask value that indicates whether the element is valid or not. The mask is typically a Boolean value where True indicates that the element is masked (invalid or missing) and False indicates that the element is valid.

# Masked arrays allow you to perform operations on arrays while automatically handling the masked elements. When performing operations, the masked elements are typically ignored or treated in a special way, depending on the specific implementation or library being used

import numpy as np
import numpy.ma as ma

# Create a regular NumPy array
data = np.array([1, 2, -999, 4, 5])

# Create a masked array by specifying a mask for invalid values
masked_data = ma.masked_values(data, -999)

# Perform operations on the masked array
print(masked_data.mean())  # Calculate the mean, ignoring the masked element

# Output: 3.0
