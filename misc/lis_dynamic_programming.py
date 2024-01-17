import numpy

input_string = '0 8 4 12 2 10 6 14 1 9 5 13 3 11 7 15'
input_numbers = numpy.array(list(map(int,input_string.split())))

output_array = numpy.array([])
for idx,a in enumerate(input_numbers):
    if idx ==0 :
        output_array = numpy.append(output_array,1)
    else:
        k = max(output_array[numpy.where(input_numbers[:idx]<a)]+1)
        output_array = numpy.append(output_array,k)
    print(output_array)

print(max(output_array))