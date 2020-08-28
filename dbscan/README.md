# DBSCAN2

- Find the blog for the project [here](https://towardsdatascience.com/dbscan-with-python-743162371dca)

- Download the test package [here](https://test.pypi.org/project/dbscan2/)

- Google Colab Notebook [here](https://colab.research.google.com/drive/1rCQl2sc5wEGKx0CgG-hW_Dg959qT3qct?usp=sharing)

```python
# Psuedo Code
from dbscan2 import dbscan2

test = dbscan2(data, epsilon, min_points)
test.fit()
test.predict([[x,y]])

# Make a predicton
labels = test.predict(data)
append(data, labels)
```

