import re
starts_with_hash = 0

# look at each line in the file use a regex to see if it starts with '#' if it does, add 1
# to the count.

with open('D:/大二课件/统计计算/exam4.R','r') as file:
    for line in file:                #遍历每一行
        if re.match("^#",line):
            starts_with_hash += 1
print(starts_with_hash)