__author__ = 'rray'

def picnicTable(itemDict, leftJust, rightJust):
    print("picnic items :".center(leftJust + rightJust, '-'))
    for k,v  in itemDict.items():
        print(k.ljust(leftJust, '.') + str(v).rjust(rightJust, ' '))

items = {"apples": 10, "Banana": 40, "rose": 9}
picnicTable(items, 10, 10)

