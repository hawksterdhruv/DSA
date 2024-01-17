str1 = 'sunday' 
str2 = 'saturday'

n = len(str1)
m = len(str2)

output_matrix = [[0 for a in range(m+1)] for b in range(n+1)]

for i in range(n+1):
    for j in range(m+1):
        if i==0:
            output_matrix[i][j] = j
        elif j == 0:
            output_matrix[i][j] = i
        elif str1[i-1] == str2[j-1]:
            output_matrix[i][j] = output_matrix[i-1][j-1]
        elif str1[i-1] != str2[j-1]:
            output_matrix[i][j] = min(output_matrix[i][j-1],
                                    output_matrix[i-1][j-1],
                                    output_matrix[i-1][j]) + 1

# for debugging purposes
# for a in tabulation_matrix:
    # print(a)


print(tabulation_matrix[-1][-1])