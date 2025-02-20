 
#%% [markdown]
#%%
# HW Numpy 
# ## By: Jonas Agyekum mintah
# ### Date: 2/19/2025
#


#%%
import numpy as np

# %%
# ######  QUESTION 1      QUESTION 1      QUESTION 1   ##########
# This exercise is to test true/shallow copies, and related concepts. 
# ----------------------------------------------------------------
# 
# ######  Part 1a      Part 1a      Part 1a   ##########

# %% 
list2 = [ [11,12,13], [21,22,23], [31,32,33], [41,42,43] ] # two dimensional list (2-D array)  # (4,3)
nparray2 = np.array(list2)
print("nparray2:", nparray2)

# For details on indices function, see class notes for Lecture 4
idlabels = np.indices( (4,3) ) 
print("idlabels:", idlabels)

i,j = idlabels  # idlabels is a tuple of length 2. We'll call those i and j
nparray2b = 10*i+j+11
print("nparray2b:",nparray2b)

# 1.a) Is nparray2 and nparray2b the "same"? Use the logical "==" test and the "is" test. 
# Write your codes, 
# and describe what you find.
#%%
list2 = [ [11,12,13], [21,22,23], [31,32,33], [41,42,43] ] # two dimensional list (2-D array)  # (4,3)
nparray2 = np.array(list2)
print("nparray2:", nparray2)

idlabels = np.indices( (4,3) ) 
print("idlabels:", idlabels)

i,j = idlabels 
nparray2b = 10*i+j+11
print("nparray2b:",nparray2b)

np.array_equal(nparray2, nparray2b)
print(nparray2 == nparray2b)

nparray2 is nparray2b
print(nparray2 is nparray2b)
#%%

#%% [markdown]
# Since nparray2b was generated using the formula 10*i + j + 11, its values are identical to those in nparray2. 
# As a result, the expression nparray2 == nparray2b evaluates to True, indicating that both arrays contain the same elements.
# However, nparray2b was created as a separate array through NumPy’s indexing operations, meaning it does not occupy the same memory space as nparray2. 
# Consequently, the statement nparray2 is nparray2b returns False, confirming that they are distinct objects in memory. 
# This demonstrates that nparray2b is an independent copy rather than a reference to nparray2.


# %%
# ######  Part 1b      Part 1b      Part 1b   ##########
# 
# 1.b) What kind of object is i, j, and idlabels? Their shapes? Data types? Strides? 
# See the lecture notes for reference.
# write your codes here
#
#%%
print(type(idlabels))
print(type(i))
print(type(j))

print(idlabels.shape)
print(i.shape)
print(j.shape)

print(idlabels.dtype)
print(i.dtype)
print(j.dtype)

print(idlabels.strides)
print(i.strides)
print(j.strides)
# %%


#%%
# ######  Part 1c      Part 1c      Part 1c   ##########
# 
# 1.c) If you change the value of i[0,0] to, say 8, print out the values for i and idlabels, both 
# before and after the change.
# 
# write your codes here
# Describe what you find. Is that what you expect?
#
# Also try to change i[0] = 8. Print out the i and idlabels again.

#%%
import numpy as np

idlabels = np.indices((4, 3))
i, j = idlabels  
print('Before Modification')
print("i:", i)
print("idlabels:", idlabels)

print('After Modification')
i[0, 0] = 8
print("i:", i)
print("idlabels:", idlabels)

i[0] = 8
print("i:", i)
print("idlabels:", idlabels)
#%%

#%% [markdown]
# Before making any modifications, i represents the row indices of a 4×3 array. 
# The idlabels array has a shape of (2, 4, 3). Where:
# idlabels[0] (the first sub-array) corresponds to i and holds row indices.
# idlabels[1] (the second sub-array) corresponds to j and contains column indices.
# After changing i[0,0] to 8, both i and idlabels[0] were updated. 
# The value 8 appears in idlabels[0], confirming that i is merely a view of idlabels[0], 
# not an independent copy. Yes, I expected this outcome because, in NumPy, slicing operations return views rather than separate copies unless explicitly stated.
# %%


# ######  Part 1d      Part 1d      Part 1d   ##########
# 
# 1.d) Let us focus on nparray2 now. (It has the same values as nparray2b.) 
# Make a shallow copy nparray2 as nparray2c
# now change nparray2c 1,1 position to 0. Check nparray2 and nparray2c again. 
# Print out the two arrays now. Is that what you expect?
# 
# Also use the "==" operator and "is" operator to test the 2 arrays. 
# write your codes here

#%%
nparray2c = nparray2.view()
nparray2c[1, 1] = 0
print("nparray2:", nparray2)
print("nparray2c:", nparray2c)

print(nparray2 == nparray2c)
print(nparray2 is nparray2c)
#%%

#%% [markdown]
# After modifying nparray2c [1,1] to 0, the change is also reflected in nparray2. 
# This indicates that nparray2c is a shallow copy of nparray2, implying that both arrays reference the same memory.
# This outcome aligns with the expected behavior of shallow copies in NumPy.
#%%


# ######  Part 1e      Part 1e      Part 1e   ##########
# Let us try again this time using the intrinsic .copy() function of numpy array objects. 
nparray2 = np.array(list2) # reset the values. list2 was never changed.
nparray2c = nparray2.copy() 
# now change nparray2c 0,2 position value to -1. Check nparray2 and nparray2c again.
# Are they true copies?
# 
# write your codes here
# Again use the "==" operator and "is" operator to test the 2 arrays. 

#%%
list2 = [ [11,12,13], [21,22,23], [31,32,33], [41,42,43] ]
nparray2 = np.array(list2) 
nparray2c = nparray2.copy()
nparray2c[0, 2] = -1

print("nparray2:", nparray2)
print("nparray2c:", nparray2c)

#%%[markdown]
# After modifying nparray2c[0,2] to -1, the change only affected nparray2c, while nparray2 remained the same. 
# This verifies that nparray2c is a genuine deep copy of nparray2, 
# indicating that they operate independently and do not share memory.

#%%
print(nparray2 == nparray2c)
print(nparray2 is nparray2c)
#%%
 
# ######  END of QUESTION 1    ###   END of QUESTION 1   ##########


# %%
# ######  QUESTION 2      QUESTION 2      QUESTION 2   ##########
# Write NumPy code to test if two arrays are element-wise equal
# within a (standard) tolerance.
# between the pairs of arrays/lists: [1e10,1e-7] and [1.00001e10,1e-8]
# between the pairs of arrays/lists: [1e10,1e-8] and [1.00001e10,1e-9]
# between the pairs of arrays/lists: [1e10,1e-8] and [1.0001e10,1e-9]
# Try to google what function to use to test numpy arrays within a tolerance.

#%%
arr1 = np.array([1e10, 1e-7])
arr2 = np.array([1.00001e10, 1e-8])

arr3 = np.array([1e10, 1e-8])
arr4 = np.array([1.00001e10, 1e-9])

arr5 = np.array([1e10, 1e-8])
arr6 = np.array([1.0001e10, 1e-9])

print("arr1 vs arr2:", np.allclose(arr1, arr2)) 
print("arr3 vs arr4:", np.allclose(arr3, arr4))
print("arr5 vs arr6:", np.allclose(arr5, arr6))
#%%

# ######  END of QUESTION 2    ###   END of QUESTION 2   ##########


# %%
# ######  QUESTION 3      QUESTION 3      QUESTION 3   ##########
# Write NumPy code to reverse (flip) an array (first element becomes last).
# Reference for examples: https://www.askpython.com/python/array/reverse-an-array-in-python
x = np.arange(12, 38)
# write your codes here

#%%
x = np.arange(12, 38)
reversed_array = x[::-1]
print("Old array:", x)
print("New Reversed array:", reversed_array)
#%%

# ######  END of QUESTION 3    ###   END of QUESTION 3   ##########


# %%
# ######  QUESTION 4      QUESTION 4      QUESTION 4   ##########
# First write NumPy code to create an 7x7 array with ones.
# Then change all the "inside" ones to zeros. (Leave the first 
# and last rows untouched, for all other rows, the first and last 
# values untouched.) 
# This way, when the array is finalized and printed out, it looks like 
# a square boundary with ones, and all zeros inside. 
# reference: https://numpy.org/doc/stable/reference/generated/numpy.ones.html
# ----------------------------------------------------------------

#%%
import numpy as np

array_7x7 = np.ones((7, 7), dtype=int)
array_7x7[1:-1, 1:-1] = 0
print(array_7x7)
#%%

# ######  END of QUESTION 4    ###   END of QUESTION 4   ##########


# %%
# ######  QUESTION 5      QUESTION 5      QUESTION 5   ##########
# Broadcasting (https://numpy.org/doc/stable/user/basics.broadcasting.html),
# Boolean arrays and Boolean indexing.
# ----------------------------------------------------------------
i=3642
myarray = np.arange(i,i+6*11).reshape(6,11)
print(myarray)
# 
# a) Obtain a boolean matrix of the same dimension, indicating if 
# the value is divisible by 7. 
# See lecture 4 notes for examples of boolean indexing

# b) Next get the list/array of those values of multiples of 7 in that original array  

#%%
import numpy as np

i = 3642
myarray = np.arange(i, i + 6 * 11).reshape(6, 11)
print(myarray)
 
boolean_matrix = (myarray % 7 == 0)
print(boolean_matrix)

multiples_of_7 = myarray[boolean_matrix]
print(multiples_of_7)
#%%

# ######  END of QUESTION 5    ###   END of QUESTION 5   ##########


#
# The following exercises are  
# from https://www.machinelearningplus.com/python/101-numpy-exercises-python/ 
# and https://www.w3resource.com/python-exercises/numpy/index-array.php
# Complete the following tasks
# 

# ######  QUESTION 6      QUESTION 6      QUESTION 6   ##########

#%%
flatlist = list(range(1,25))
print(flatlist) 
#%%


# 6.1) create a numpy array from flatlist, call it nparray1. What is the shape of nparray1?
# remember to print the result
#
# write your codes here
#%%
import numpy as np

flatlist = list(range(1, 25))
print(flatlist)

nparray1 = np.array(flatlist)
print(nparray1)
print(nparray1.shape)
#%%


#%%
# 6.2) reshape nparray1 into a 3x8 numpy array, call it nparray2
# remember to print the result
#
# write your codes here

#%%
nparray2 = nparray1.reshape(3, 8)
print(nparray2)
#%%


#%%
# 6.3) swap columns 0 and 2 of nparray2, and call it nparray3
# remember to print the result
#
# write your codes here

#%% 
nparray3 = nparray2.copy()
nparray3[:, [0, 2]] = nparray3[:, [2, 0]]  
print(nparray3)
#%%


#%%
# 6.4) swap rows 0 and 1 of nparray3, and call it nparray4
# remember to print the result
#
# write your codes here

#%% 
nparray4 = nparray3.copy() 
nparray4[[0, 1], :] = nparray4[[1, 0], :] 
print(nparray4)
#%%


#%%
# 6.5) reshape nparray4 into a 2x3x4 numpy array, call it nparray3D
# remember to print the result
#
# write your codes here

#%%
nparray3D = nparray4.reshape(2, 3, 4)
print(nparray3D)
print(nparray3D.shape)
#%%


#%%
# 6.6) from nparray3D, create a numpy array with boolean values True/False, whether 
# the value is a multiple of three. Call this nparray5
# remember to print the result
# 
# write your codes here

#%%
nparray5 = (nparray3D % 3 == 0)
print(nparray5)
#%%


#%%
# 6.7) from nparray5 and nparray3D, filter out the elements that are divisible 
# by 3, and save it as nparray6a. What is the shape of nparray6a?
# remember to print the result
#
# write your codes here

#%%
nparray6a = nparray3D[nparray5]
print(nparray6a)
print(nparray6a.shape)
#%%


#%%
# 6.8) Instead of getting a flat array structure, can you try to perform the filtering 
# in 6.7, but resulting in a numpy array the same shape as nparray3D? Say if a number 
# is divisible by 3, keep it. If not, replace by zero. Try.
# Save the result as nparray6b
# remember to print the result
# 
# write your codes here

#%%
nparray6b = np.where(nparray5, nparray3D, 0)
print(nparray6b)
print(nparray6b.shape)
#%%

# ######  END of QUESTION 6    ###   END of QUESTION 6   ##########

#%%
#
