str1 = 'AGGTAB'
str2 = 'GXTXAYB'
n = len(str1)
m = len(str2)
# output_matrix = numpy.zeros((n,m))

i = n-1
j = m-1

def lcs(str1,str2):
    while True:
        if len(str1) == 0 or len(str2) ==0:
            return 0    
        elif str1[-1] != str2[-1]:
            return max(lcs(str1[:-1],str2),lcs(str1,str2[:-1])) 
        elif str1[-1] == str2[-1]:
            return lcs(str1[:-1],str2[:-1]) + 1


print(lcs(str1,str2))