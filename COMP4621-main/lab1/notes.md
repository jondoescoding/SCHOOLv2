# Lab01 Question

## Question 01
- How to create a python dictionary?

# 1. Basic dictionary creation using curly braces
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

# 2. Using dict() constructor
colors = dict(red="#FF0000", green="#00FF00", blue="#0000FF")

# 3. Creating from list of tuples
items = dict([("apple", 1), ("banana", 2), ("orange", 3)])

# 4. Dictionary comprehension
numbers = {x: x**2 for x in range(5)}  # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}

# 5. Creating an empty dictionary
empty_dict = {}
# or
empty_dict2 = dict()

# 6. Dictionary with mixed data types
mixed = {
    "string": "hello",
    1: 100,
    "list": [1, 2, 3],
    "tuple": (4, 5, 6),
    "dict": {"nested": "value"}
}

# 7. Using fromkeys() to create dictionary with default values
keys = ["a", "b", "c"]
default_dict = dict.fromkeys(keys, 0)  # {'a': 0, 'b': 0, 'c': 0}

---

## Question 02
- How do you create a dataframe within pandas?

# 1. From a dictionary
data_dict = {
    'name': ['John', 'Anna', 'Peter'],
    'age': [28, 22, 35],
    'city': ['New York', 'Paris', 'London']
}
df1 = pd.DataFrame(data_dict)

# 2. From a list of dictionaries
data_list = [
    {'name': 'John', 'age': 28, 'city': 'New York'},
    {'name': 'Anna', 'age': 22, 'city': 'Paris'},
    {'name': 'Peter', 'age': 35, 'city': 'London'}
]
df2 = pd.DataFrame(data_list)

# 3. From a NumPy array
array = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])
df3 = pd.DataFrame(array, columns=['A', 'B', 'C'])

# 4. From a CSV file
df4 = pd.read_csv('filename.csv')

# 5. From Excel file
df5 = pd.read_excel('filename.xlsx')

# 6. Creating an empty DataFrame
df6 = pd.DataFrame()

# 7. From lists
names = ['John', 'Anna', 'Peter']
ages = [28, 22, 35]
df7 = pd.DataFrame(list(zip(names, ages)), columns=['Name', 'Age'])

# 8. With custom index
df8 = pd.DataFrame(data_dict, index=['a', 'b', 'c'])

# 9. Using date_range for time series
dates = pd.date_range('2023-01-01', periods=5)
df9 = pd.DataFrame(np.random.randn(5, 3), 
                  index=dates,
                  columns=['A', 'B', 'C'])

## Question 03
- How do you get the rows and columns within a dataframe

```
rows, columns = df.shape  # Returns a tuple of (rows, columns)
num_rows = len(df)  # Number of rows
num_columns = len(df.columns)  # Number of columns
```

