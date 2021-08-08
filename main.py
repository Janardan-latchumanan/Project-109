import statistics;
import csv;
import pandas as pd;
import random

df = pd.read_csv("StudentsPerformance.csv");
Read_data = df["reading score"].to_list();
Write_data = df["writing score"].to_list();
Math_data = df["math score"].to_list();
data_set = [];

#READING SCORE
for i in range(0,50):
	randInd = random.randint(0,len(Read_data));
	value = Read_data[randInd];
	data_set.append(value);

read_mean = statistics.mean(data_set)
read_std_dev = statistics.stdev(data_set)


#WRITING SCORE 
for i in range(0,50):
	randInd = random.randint(0,len(Write_data));
	value = Write_data[randInd];
	data_set.append(value);

write_mean = statistics.mean(data_set)
write_std_dev = statistics.stdev(data_set)


#MATH SCORE 
for i in range(0,50):
	randInd = random.randint(0,len(Math_data));
	value = Math_data[randInd];
	data_set.append(value);

math_mean = statistics.mean(data_set)
math_std_dev = statistics.stdev(data_set)

'''
print("Mean is :",data_mean )
print("Standard Deviation is :",data_std_dev)
'''

#READING STANDARD DEVIATION 
firstStart , firstEnd = read_mean-read_std_dev,read_mean+read_std_dev;
secondStart , SecondEnd = read_mean-(2* read_std_dev),read_mean+(2* read_std_dev);
list_of_data_within_1_std_deviation = [result for result in Read_data if result > firstStart and result < firstEnd]
print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(Read_data)))


#WRITE STANDARD DEVIATION 
thirdStart , thirdEnd = write_mean-write_std_dev,write_mean+write_std_dev;
fourthStart , fourthEnd = write_mean-(2* write_std_dev),write_mean+(2* write_std_dev);
list_of_data_within_2_std_deviation = [result for result in Write_data if result > thirdStart and result < thirdEnd]
print("{}% of data lies within 2 standard deviation".format(len(list_of_data_within_2_std_deviation)*100.0/len(Write_data)))


#MATH STANDARD DEVIATION
fifthStart , fifthEnd = math_mean-math_std_dev,math_mean+math_std_dev;
sixthStart , sixthEnd = math_mean-(2* math_std_dev),math_mean+(2* math_std_dev);
list_of_data_within_3_std_deviation = [result for result in Math_data if result > fifthStart and result < fifthEnd]
print("{}% of data lies within 3 standard deviation".format(len(list_of_data_within_3_std_deviation)*100.0/len(Math_data)))


