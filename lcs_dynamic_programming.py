str1 = 'If last characters of both sequences match (or X[m-1] == Y[n-1]) then'
str2 = 'If last characters of both sequences do not match (or X[m-1] != Y[n-1]) then'
n = len(str1)
m = len(str2)
tabulation_matrix = [[0 for a in range(m+1)] for a in range(n+1)]

# for debugging purposes
# print(tabulation_matrix)

for i in range(n+1):
    for j in range(m+1):
        if i == 0 or j ==0:
            tabulation_matrix[i][j] == 0  
        elif str1[i-1] == str2[j-1]:
            tabulation_matrix[i][j] = tabulation_matrix[i-1][j-1] + 1
        elif str1[i-1] != str2[j-1]:
            tabulation_matrix[i][j] = max(tabulation_matrix[i][j-1],tabulation_matrix[i-1][j])

# for debugging purposes
# for a in tabulation_matrix:
    # print(a)

print(tabulation_matrix[-1][-1])
