## List comprehension
- Filtered Comprehension
```py
filtered_ls = [x for x in range(10) if x%2=0]
len(filtered_ls) <= len(range(10))
```
- Conditional Comprehension
	- `else` has to be included
```py
conditional_ls = [x if x%2=0 else x*2 for x in range(10)]
len(conditional_ls) == len(range(10))
```
# NumPy (np)
## Array
NumPy ndarray
- Defined from a list (list-alike)
	- `arr3D = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])`
- Elements are all same types; otherwise, upcast if possible (unlike list)
	- If incompatible (number and string), NumPy defaults to `dtype=object`, storing references to Python objects, which avoid errors but sacrifices performance benefits.

### Multidimensional Array
- Access using a comma-separated tuples of indices (**Different from list**)
	- `arr3D[1,1,1]`
	- `arr3D[:1, :2, 1:3]` left included; right excluded
	- `list3D[1][1][1]`
### Create an Array
![[Ust_Note/Attachment/Pasted image 20250527005628.png]]
#### Random Number Generators
![[Ust_Note/Attachment/Pasted image 20250527005731.png]]
### Operation with Array
- Element-wise Computation
- Aggregation
- Transpose
#### Element-wise Computation
- Python automatically converts all elements to the most compatible data type with the highest precision.
- The upcasting follows this hierarchy of data types: int → float → complex → string
#### Aggregation
`np.method(array)` is equivalent to `array.method()`

![[Ust_Note/Attachment/Pasted image 20250527010201.png]]
##### Axis
- Axis 0: by Depth/Layers
- Axis 1: by column
- Axis 2: by row

It aligns with the order of tuple argument when creating an array.
The **sum(axis=n)** operation collapses the specified axis, aggregating values along that dimension. The resulting array's shape loses the summed axis.

![[Ust_Note/Attachment/Pasted image 20250527010225.png]]
- Use `keepdims=True` to retain the original array's dimensionality

![[Ust_Note/Attachment/Pasted image 20250527011714.png]]
#### Transpose
Extra
# SciPy (sp)
Built on [[Ust_Note/yr1_spring/ISOM2600/Cheat sheet#NumPy|NumPy]]
## Statistics Computation
### p-value
![[Ust_Note/Attachment/Pasted image 20250527022101.png]]
### Critical Value
![[Ust_Note/Attachment/Pasted image 20250527022204.png]]
# Matplotlib (plt)
Built on [[Ust_Note/yr1_spring/ISOM2600/Cheat sheet#NumPy (np)|NumPy]] and [[Ust_Note/yr1_spring/ISOM2600/Cheat sheet#SciPy (sp)|SciPy]] for *Data Visualization*
## Line Plot
![[Ust_Note/Attachment/Pasted image 20250527022301.png]]
## Histogram
![[Ust_Note/Attachment/Pasted image 20250527022327.png]]
`Density=True` shows the relative frequency.

![[Ust_Note/Attachment/Pasted image 20250527022426.png]]
`bins=30` set the number of sliders to be 30
## Scatterplot
![[Ust_Note/Attachment/Pasted image 20250527022654.png]]
## Figure as an Object
Extra
# Pandas
## DataFrame
2-dimensional data structure with index and columns
![[Ust_Note/Attachment/Pasted image 20250527171006.png]]
## Series
- 1-dimensional array. No column attribute. Only Index and Value
- `aSeries = df["column"]`
## Data Summarization
![[Ust_Note/Attachment/Pasted image 20250527171243.png]]
![[Ust_Note/Attachment/Pasted image 20250527171222.png]]
- `df["column"].value counts(dropna=True).head(5)`
	- default in descending order (`ascemding=True`)
- `df.sort_values(by='column', ascending=False)`
## Axes
the directions along which operations are performed.
- axis 0: row
	- `axis = 0` moves down the rows for each column
	- most common for EDA
- axis 1: column
	- `axis = 1` moves across the columns for each row
	- often meaningless
## Built-in Plotting Method
### Histogram
![[Ust_Note/Attachment/Pasted image 20250527172121.png]]
### Boxplot
![[Ust_Note/Attachment/Pasted image 20250527172200.png]]
### Line Chart
![[Ust_Note/Attachment/Pasted image 20250527172223.png]]
## Data Slicing
### Selection
usually for columns
#### Column Selection
- Select one column
	- `df["column"]`
- Select multiple columns
	- Take a **list** as argument
	- `df[['column1','column2']]`
#### Row Selection
- selects based on index names
	- `df.loc["index_name"]`
- selects based on integer position
	- `df.iloc[0]`
	- `df.iloc[[0,1,2]]`
### Slicing
usually for rows
- `df.loc["index_name1":"index_name2"]`
	- right **inclusive**
- `df.iloc[0:3]`
	- right **exclusive**
#### Mixed Slicing
- `df.iloc[:3,:2]`
	- return the first three rows and the first two columns
## Making Changes
### Add and Update New Columns/Rows
![[Ust_Note/Attachment/Pasted image 20250527182727.png]]
- **No `elif`**, but `else ... if ...`
### Drop
Declare the axis to be dropped
- Drop Columns
	- axis = 1
- Drop Rows
	- axis = 0
## Standardization
$$
\frac{x-\text{sample mean}}{\text{sample std}}
$$
# Handle Missing Value
## Count Missing Value
![[Ust_Note/Attachment/Pasted image 20250527183800.png]]
```py
# df.sum() with no axis specified sum by default axis = 0, i.e., sum for each column
missing_rate = rawdata.isnull().sum().sum()/(rawdata.shape[0] * rawdata.shape[1])
```
## Impute NaN Values
### Replaced by Fixed Number
**Without assignment, the original dataframe is unchanged**
```py
df1 = rawdata.fillna(0)
df2 = rawdata.fillna(rawdata["column"].mean())
```
### Forward Imputation
```py
newdf.fillna(method="ffill")
```
Suitable for time series data
### Backward Imputation
```py
newdf.fillna(method="bfill")
```
## Drop NaN
- Drop Row with NaN
	- `newdf.dropna(axis=0)`
- Drop columns with NaN
	- `newdf.dropna(axis=1)`
# Time Series
## Rolling Method
- 3 is the width of the sliding window.
-  The mean() is applied to value in the window
- can be min()/max()
```py

df.["RollMean3"] = df["column"].rolling(3).mean()
```
## Cumulative Methods
- the function is applied to value from the start
```py
dailysales['Cumulative Sales'] = dailysales['Sales'].cumsum()
```
# Simple Linear Model
## Scatterplot
have a basic sense of the data
## Correlation
![[Ust_Note/Attachment/Pasted image 20250527212019.png]]
## Train and Test Split
$$RMSE_{Train}\leq RMSE_{Test}$$
## Build Model with Statsmodels (sm)
Always start with model with intercept
![[Ust_Note/Attachment/Pasted image 20250527212357.png]]
## Hypothesis Testing
`model.summary()` show t-statistic and p-value for every coefficient and intercept with $H_{0}:\beta_{n}=0$ by default
## Prediction
```py
model.predict([1, 0.05])
```
[1, 0.05] as input since we added constant term to the independent variable. It is consistent with the model we built.
Similarly, 
```py
model.predict(sm.add_constant(train['SP500']))
```
which is equivalent to
```py
model.fittedvalues
```
## Residual Analysis
```py
train['Residuals'] = model.resid
```
![[Ust_Note/Attachment/Pasted image 20250527213341.png]]
### R-Square
`model.rsquared`