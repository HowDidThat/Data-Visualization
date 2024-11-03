# Comma separated values (CSV)

Let's say that we have a dataset containing games from over the years on different platforms, and we want to see the
difference between critic score and user score for each platform.

First of all lets talk a little about our dataset. Our dataset is a csv file that contains more data than we need.
At first, we need to load the file and see how python handles it. Lucky python comes with a build in csv reader:
```python
import csv
```
We can use the following code to read and print the lines of the csv:

```python
import csv

allData = []
with open('../dataset.csv', newline='') as csvFile:
    csvData = csv.reader(csvFile, delimiter=',')
    for row in csvData:
        allData.append(row)
print(allData)
```
Note: if you want to run the program from the root folder using VSCode, the path changes to 'dataset.csv'.

Now we can see that the csv reader reads the file line by line and creates a list with the respective values and the 
first entry is the table column names.

After reading the name of the columns that are provided in the dataset, we decide to remove the ones that do not
interest us, and we will remain only with the columns : *year_of_release*, *critic_score* and *user_score*. With the
next lines of code we will also remove the head of the csv. 
````python
parsedData = []
for row in allData[1:]:
    parsedData.append([row[2],row[10],row[12]])
print(parsedData)
````
Now that we have trimmed our dataset, we will also need to remove any row that has missing values and turn our numbers 
from strings to floats as the default reading operation for a csv turns all elements into strings.
```python
# C1
# Removing entries that are empty
data = []
for row in parsedData:
    if "" not in row :
        data.append(row)
```
```python
# C2
# Turning values of columns 1 and 2 into floats
for row in data:
    try:
        row[0] = int(row[0])
        row[1] = float(row[1])
        row[2] = float(row[2])
    except:
        # This will print the rows in witch there are errors
        print(row)
```
>Exercise: use the code in C2 to search for other inconsistent values and modify the C1 code to remove all bad rows.

Now that we have our data let's normalize it. As you can see the critic scores range from 0 to 100 and the user scores 
are from 0 to 10.
```python
for row in data:
    row[2] *= 10
```
Now what we are left with is a bidimensional matrix 

As we want to plot side by side the average user review vs the average critic review, we will need to take our data and
compress it into a smaller table that will contain the year, average critic reviews and average user reviews. 

>Exercise: Separate the data such that each entry contains only the platform and the sales amount for the 3 regions na_sales, eu_sales, jp_sales. Remove any row that contains empty values and normalize the values if necessary.

After sorting our data we need to calculate the averages for the user and critic reviews. First we need to see what years does our data cover, we can do this using code or an array if we want the data to be organised in a certain way:
```python
availableYears = []
for row in data:
    if row[0] not in availableYears:
        availableYears.append(row[0])
```

Create a dictionary that will have the following structure:
key : [numberRewies, total_critic_reviews, total_user_reviews].
```python
dataDict = {}
for year in availableYears:
    dataDict[year] = [0,0,0]
```

Fill the dictionary:
```python
for row in data:
    year = row[0]
    dataDict[year][0] += 1
    dataDict[year][1] += row[1]
    dataDict[year][2] += row[2]
```

Find the critic_average_score and user_average_score:
```python
for year in dataDict.keys():
    dataDict[year][1] //= dataDict[year][0]
    dataDict[year][2] //= dataDict[year][0]
    # removing the number of games from the table as we do not need it any more
    dataDict[year].pop(0)
```

Now that we have our data we need to turn it 90° (this will make sense when we start to plot the data):
```python
cData = dict()
keys = ["year","critic_review","user_review"]
for key in keys:
    cData[key] = []
for key in dataDict.keys():
    cData["year"].append(key)
    cData["critic_review"].append(dataDict[key][0])
    cData["user_review"].append(dataDict[key][1])
```

>Exercise: Create a dictionary similar to the one above having the name of the platforms and the total sales amount for each region.
