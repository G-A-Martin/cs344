# Gavin Martin
# CS344
# Homework 3

# Import required libraries.

# Import dataset.
import tensorflow
from keras.datasets import boston_housing
import pandas
import numpy as np

(train_data, train_targets), (test_data, test_targets) = boston_housing.load_data()



# ----------------------------- COLUMN LEGEND --------------------------------
# 0 - Crime: crime per capita
# 1 - Zoning: Proportion of residential land zoned for lots over 25,000 sq. ft
# 2 - Indus: Proportion of non-retail business acres per town
# 3 - Chas: Charles River dummy variable (= 1 if tract bounds river; 0 otherwise)
# 4 - Nitrogen_Oxide: Nitric oxide concentration (parts per 10 million)
# 5 - Avgerage_Rooms: Average number of rooms per dwelling
# 6 - Age: Proportion of owner-occupied units built prior to 1940
# 7 - Distances: Weighted distances to five Boston employment centers
# 8 - Radial: Index of accessibility to radial highways
# 9 - Tax: Full-value property tax rate per $10,000
# 10 - Pupil_Teacher: Pupil-teacher ratio by town
# 11 - Black: 1000(Bk — 0.63)², where Bk is the proportion of [people of African American descent] by town
# 12 - Low_Status: Percentage of lower status of the population
# 13 - Median_Val: Median value of owner-occupied homes in $1000s


# I Split it 20% validation data and 80% Training data given that it was 404 rows total
validation_dataset = train_data[:82]
train_dataset = train_data[82:]



print("Data Structure Dimensions: ")
print("\tTrain Data Dimensions: " + str(train_dataset.ndim))
print("\tTrain Data Shape: " + str(train_dataset.shape))
print("\tValidation Data Dimensions: " + str(validation_dataset.ndim))
print("\tValidation Data Shape: " + str(validation_dataset.shape))
print("\tTest Data Dimensions: " + str(test_data.ndim))
print("\tTest Data Shape: " + str(test_data.shape))


validation_dataframe = pandas.DataFrame(validation_dataset)
# Shuffles dataframe
validation_dataframe = validation_dataframe.reindex(np.random.permutation(validation_dataframe.index))

training_dataframe = pandas.DataFrame(train_dataset)
# Shuffles dataframe
training_dataframe = training_dataframe.reindex(np.random.permutation(training_dataframe.index))

testing_dataframe = pandas.DataFrame(test_data)
# Shuffles dataframe
testing_dataframe = testing_dataframe.reindex(np.random.permutation(testing_dataframe.index))

print("\nValidation dataframe: ")
print(validation_dataframe.describe())
print("\nTraining dataframe: ")
print(training_dataframe.describe())
print("\nTesting dataframe: ")
print(testing_dataframe.describe())

# Synthentic Variable: I want to predict the median value of owner occupied homes Median_Val using
#   (Tax / Crime Rate) because I believe the crime rate will have some effect on the median value of housing in the area
#   A Decreasing value for tax/crime rate, should and likely would in my opinion indicate a decreasing median home value
#
#

property_tax_crime_rate_train = training_dataframe[9] / training_dataframe[0]
training_dataframe['property_tax_crime_rate'] = property_tax_crime_rate_train

property_tax_crime_rate_validation = validation_dataframe[9] / validation_dataframe[0]
validation_dataframe['property_tax_crime_rate'] = property_tax_crime_rate_validation

property_tax_per_crime_rate_test = testing_dataframe[9] / testing_dataframe[0]
testing_dataframe['property_tax_crime_rate'] = property_tax_per_crime_rate_test



print("\nValidation dataframe: ")
print(validation_dataframe.describe())
print("\nTraining dataframe: ")
print(training_dataframe.describe())
print("\nTesting dataframe: ")
print(testing_dataframe.describe())




