# This program prints a list of list in tabular form which is right justified
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'mose', 'goose']]

for y in range(len(tableData)):
    for x in range(len(tableData[y])):
        print(tableData[y][x], sep='', end='')
    print()

# TODO Need to figure out way to generate output of table

"""output should be

  apples Alice  dogs
 oranges   Bob  cats
cherries Carol moose
  banana David goose
"""
