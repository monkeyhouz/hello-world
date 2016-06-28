# This is google technical interview test question
# The task is to reverse input string

# input string
inputString = "technical"
outputString = ""


# measure the input string
stringLength = len(inputString)

# form the output string
for i in range(0, stringLength) :
    outputString = outputString + inputString[(stringLength - i) - 1]

# print the result
print (inputString)
print (outputString)