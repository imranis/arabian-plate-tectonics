import pandas as pd
import numpy as np

df = pd.read_csv('test.txt', delim_whitespace=True, header=None)

# Name the columns, 'name' is the last three columns concatenated
df.columns = ['lon', 'lat', 'depth', 'mrr', 'mtt', 'mpp', 'mrt', 'mrp', 'mtp', 'iexp', 'col11', 'col12', 'col13']

df['name'] = df[['col11', 'col12', 'col13']].apply(lambda x: ' '.join(x.dropna().astype(str)), axis=1)

df = df.drop(columns=['col11', 'col12', 'col13'])

# Create a matrix with the sum of individual elements
matrix_elements = ['mtt', 'mtp', 'mrt', 'mtp', 'mpp', 'mrp', 'mrt', 'mrp', 'mrr']
matrix = np.array([df[element].sum() for element in matrix_elements]).reshape(3, 3)

print('Summed Moment Tensor:\n', matrix)

# Print each element of the matrix with its name
for i, element in enumerate(matrix_elements):
    print(f'{element}: {matrix[i//3][i%3]}')
