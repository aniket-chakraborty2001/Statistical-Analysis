# Statistical_analysis_in_python
Here i consider a score data and conduct a T test on the Math scores between two groups. The groups are Math score of males and Math score of females.
# Introduction to the project:
In this project we will see how to use some python libraries to conduct some statistical tests in python. For this purpose we have the **scores.csv** file which is given in the GitHub files section. This file is aloso available in the Kaggle website. In this data we consider two arrays Math score for females and Math score of males and conduct a T test in order to compare them. 

Here we discuss the basics steps of the project, which we came across in completing the project.

## Environment setup:
In this step we set up the environment by importing packages, reading the .csv file and by understanding the data. The steps are discussed below in detail:

### 1. Importing packages:
It is the first step of this project. In this step we import very strong packahes like pandas, numpy, os, stats from scipy etc. This will help us to real, load and do the required statistical operation on the csv file.

### 2. Reading and loading file:
In order to read and load the file, we first connect google colab to drive as we store the .csv file in drive. To do this we use the **drive.mount()** function. After connecting we use the **read_csv()** function that comes under pandas library and input the path of the file as a parameter of read_csv() function. We store the result in a variable called df.

### 3. Basic data understanding:
After loading it is very important to know the data. For this purpose we use the **.head()** method. We also can use the .**columns()** method to know the column names. Here we use the .**shape()** method that comes under pandas library to know the dimensions (number of rows and columns) of the data frame df.

## Starting of the project:
From here we start the project. The steps include:

### 1. Selecting the resources:
In this step we select the Math score of females and males differently as numpy array using the **.loc method**. We store them in the variables called fm_maths and m_maths. For confirmation we check the type and print the respective numpy arrays. We also use the **.size()** method to know the number of samples in the arrays.

### 2. Defining a function and setting parameters:
Here we define a function called **computeTandP()** using the **def** keyword. We also set the parameters that help us to calculate the T and P value for the hypothesis. Here we consider the following as the parameter:
* Mean
* Standard deviation
* Sample size
* Variance
* Pooled standard deviation
* Standard error
* Degrees of freedom

### 3. Removing the Outliers:
After finding the T and P value, We can conclude the result of our hypothesis test. But before that we define a **removeOutliers()** function that fix the outliers and select our input data in a conditioned way so that we can eliminate the outliers. To confirm our code runs properly, we check the number of samples in the filtered arrays and observe that number of sample reduces.


### NOTE:
**In this section w did not cover why we use the expressions to cover the standard error, deviation and pooled variance. In the files section there is a file called **Additioanl Details**. This contain the basics things of T test. Do check it out for better understanding.


## Extension:
There is another file named **Conducting T test Stepwise** which shows additional details about this project. The first thinh we have to chech is the Normality of the data. Without this condition we can not conduct T test. So first we conduct Normality test using the Shapiro test. According to the data asd p value is less than 0.05, we failed the test. Next to check Normality we conduct Kolmogorov test. The above mentioned two tests are example of parametric tests.This test also fails. Lastly we have the option to conduct Mann-Whitney U test which is a non-parametric test. In this case the p value is less than 0.05, indicating that there is difference between the data we consider in terms of central tendency.
