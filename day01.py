import re
total_sum = 0

inputFile = open("input.txt")
outputFile = open('output.txt','w')
resultsFile = open('results.txt', 'w')

fileInput = inputFile.readlines()
for line in fileInput:
  nums = re.findall(r'\d+', line)
  outputFile.write(str(nums) + "\n")

outputFile.close()
outputFile = open('output.txt')
resultsFile = open('results.txt', 'w')

for line in outputFile:
    line = line.strip()
    nums = re.findall(r'\d+', line)
    if len(line) > 2:
        first_digit = (line[2])
        last_digit = int(nums[-1][-1])
    elif len(line) < 2:
        first_digit = (line[2])
    resultsFile.write(str(first_digit) + str(last_digit) + "\n")    

resultsFile = open('results.txt', 'r')

for line in resultsFile:
    value = int(line.strip())
    total_sum += value
print(total_sum)
    