# Impressed by the power of this number, Kostya has begun to look for occurrences of four anywhere. He has a list of T integers, for each of them he wants to calculate the number of occurrences of the digit 4 in the decimal representation. He is too busy now, so please help him.

# Input
# The first line of input consists of a single integer T, denoting the number of integers in Kostya's list.

# Then, there are T lines, each of them contain a single integer from the list.

# Output
# Output T lines. Each of these lines should contain the number of occurences of the digit 4 in the respective integer from Kostya's list.

# Constraints
# 1 ≤ T ≤ 105
# (Subtask 1): 0 ≤ Numbers from the list ≤ 9 - 33 points.
# (Subtask 2): 0 ≤ Numbers from the list ≤ 109 - 67 points.
# Sample Input 1 
# 5
# 447474
# 228
# 6664
# 40
# 81
# Sample Output 1 
# 4
# 0
# 1
# 1
# 0


for i in range(int(input())):
    num = input()
    cnt=0
    for i in num:
        if i=='4':
            cnt+=1
    print(cnt)