spam = ["apples", "bananas", "tofu", "cats"]


def return_string(spam):
    desired_string = ''
    for item in range(len(spam)):
        if item == 0:
            desired_string = desired_string + spam[item]
            continue
        elif item == (len(spam)-1):
            desired_string = desired_string + " and " + spam[item]
            continue
        desired_string = desired_string + " , " + spam[item]
    return desired_string

print(return_string(spam))
