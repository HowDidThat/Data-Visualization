# Matplotlib

Matplotlib is one of the python libraries that we can use to plot different graphs and the one I will be using for 
creating our graph.

First of all we need matplotlib.pyplot and we will give it the alias *plt*.
```python
import matplotlib.pyplot as plt
```

After importing the library we can check if everything works by creating and showing a plot graph with the following commands:
```python
fig, ax = plt.subplots()
plt.show()
```
This will create an empty plot and will be our canvas for creating our graph.

First of all let's consider the following data witch represents the number of trees planted in millions:
```python
trees = [["North America","Latin America","Africa","Asia and the Pacific","Europe"],
         [10.9           ,4.3            ,2.6     ,5.0                   ,0.6]]
```
We want to plot out the number of planted trees so we will use:
```python
import matplotlib.pyplot as plt
fig, ax = plt.subplots()
trees = [["North America","Latin America","Africa","Asia and the Pacific","Europe"],
         [10.9           ,4.3            ,2.6     ,5.0                   ,0.6]]
numberPoints = len(trees[0])
ax.bar([x for x in range(numberPoints)],trees[1])
plt.show()
```
The first argument of the *ax.bar* function represents the value on the x-axis and the second represents the value on the y-axis.

Now that we have our graph we will change the name of the values on the x-axis as such:
```python
plt.xticks([x for x in range(groups)],cDict['year'],  fontsize='15')
```

Now let's add another row to our dataset, the new row will represent trees planted in 2023.
```python
trees = [["North America","Latin America","Africa","Asia and the Pacific","Europe"],
         [10.9           ,4.3            ,2.6     ,5.0                   ,0.6],
         [12.3           ,6.7            ,3.3     ,6.5                   ,0.7]]
```
Let's try to plot the new values in the new values in the graph.
```python
ax.bar([x for x in range(numberPoints)],trees[2])
```
As you can see we can't see any changes. Why? Well when we specify the points on the x-axis we use the same points so
the graph is rendered on top of each other. If you want to see the change, swap the order in witch we call *ax.bar*.

To set the columns side by side we need to move the bars, one a little to the left, and one a little to the right, and 
add a litle space in between them.
```python
barWidth = 0.2
barGap = 0.05
x_1 = [x-barWidth/2 - barGap/2 for x in range(numberPoints)]
x_2 = [x+barWidth/2 + barGap/2 for x in range(numberPoints)]
ax.bar(x_1,trees[2],label="2020",width=barWidth)
ax.bar(x_2,trees[1],label="2023",width=barWidth)
```
At last, we have our graph plot out and the only thing required is to add a legend. This can be done by adding a label 
to each bar, and calling the *ax.legend* function.
```python
ax.legend()
```

Move the legend around is simple as we can specify the localization by the *loc* parameter, but putting it on the
outside of the graph is a little trickier. We also need to modify the figure size of the initial subplot created and 
the anchor of the legend as such.
```python
fig, ax = plt.subplots(figsize=(12, 8))
...
ax.legend(loc='center left',title="year",bbox_to_anchor=(1, 0.5))
```
Feel free to change function parameters until the graph looks like the one you imagined.

>Exercise 1: Modify the theory from this step to show the data from the theory of the previous step.

>Exercise 2: Use the data that you got from the previous step and plot it.

