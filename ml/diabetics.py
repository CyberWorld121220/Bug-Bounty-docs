import matplotlib.pyplot as plt
import numpy as np
from sklearn import datasets,linear_model
from sklearn.metrics import mean_squared_error

diabetes = datasets.load_diabetes()
#print(diabetes.keys())

# output => dict_keys(['data', 'target', 'frame', 'DESCR', 'feature_names', 'data_filename', 'target_filename', 'data_module'])

#print(diabetes.DESCR)
#print(diabetes.data[:,np.newaxis,5:-1])  # to print the second coloumn
#print(diabetes.data[1])  # to print 2nd row
#print(len(diabetes.data))  # number of cases/ number of rows
#print(diabetes.data) # print entire table 
#print(diabetes.target[-30:]) # print last 30 elements's y [this function will print the value or label or output for given features] / print last 30 rows's output
#print(diabetes.target[0:30]) # print first 30 elements's y 


####################################################numpy basics ################################################################

"""
X = [
      [1 2 3 4]
      [2 3 4 5]
      [3 4 5 6]
      [4 5 6 7]
      [5 6 7 8]
      ]
      
      this is an numpy array or table or matrices, datasets mein features issi type se dete hai 
      iris.data esi table print krega ,and diabetes.data bhi aesa hi hai, model train krna hoto esa hi array hum features mein dalte hai
      
      ## slicing
      
      for slicing hum diabetes.data[rows,coloumn]  => iss type se krte hai
      rows =>   starting_row:(ending_row + 1)   , coloumn => starting_coloumn:(ending_coloumn + 1)


"""







######################################### Building y = mx + c , or model with only one  feature ##################################################################


diabetes_X = diabetes.data[:,np.newaxis,2]  # selecting second coloumn

diabetes_train_x = diabetes_X[:-30]  # getting last 30 features for training
diabetes_train_y =diabetes.target[:-30]  # getting last 30 features's values

diabetes_test_x = diabetes_X[-30:] # getting first 30 features for testing
diabetes_test_y = diabetes.target[-30:] # getting first 30 features's for testing

model = linear_model.LinearRegression()
model.fit(diabetes_train_x,diabetes_train_y)
diabetes_y_predict = model.predict(diabetes_test_x)
print(diabetes_y_predict)
print(diabetes_test_y)

print("mean squared predicted error: ",mean_squared_error(diabetes_test_y,diabetes_y_predict)) 
print("Weights: ",model.coef_)
print("Intercepts: ",model.intercept_)

plt.scatter(diabetes_test_x,diabetes_test_y)
plt.scatter(diabetes_test_x,diabetes_y_predict) # yein line comment krdo toh graph mein line nhi bnegi, sirf dots aayeigne
plt.show()

######################################### Building y = w1x1 + w2x2 ----wnxn , or model with all one  feature ##################################################################


diabetes_X = diabetes.data  # taking all the features together

diabetes_train_x = diabetes_X[:-30]  # getting last 30 features for training
diabetes_train_y =diabetes.target[:-30]  # getting last 30 features's values

diabetes_test_x = diabetes_X[-30:] # getting first 30 features for testing
diabetes_test_y = diabetes.target[-30:] # getting first 30 features's for testing

model = linear_model.LinearRegression()
model.fit(diabetes_train_x,diabetes_train_y)
diabetes_y_predict = model.predict(diabetes_test_x)
print(diabetes_y_predict)
print(diabetes_test_y)

print("mean squared predicted error: ",mean_squared_error(diabetes_test_y,diabetes_y_predict)) 
print("Weights: ",model.coef_)
print("Intercepts: ",model.intercept_)
"""
plt.scatter(diabetes_test_x,diabetes_test_y)
plt.scatter(diabetes_test_x,diabetes_y_predict) # yein line comment krdo toh graph mein line nhi bnegi, sirf dots aayeigne
plt.show() """
