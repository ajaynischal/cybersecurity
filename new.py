def span(values):
    span_len = 1
    j = len(values) - 1
    while (j > 0):
        i = 0
        while (i < len(values)):
            if (values[i] == values[j]) :
                if (j-i +1 > span_len):
                    span_len = j-i+1                
                i = i +1
            j= j - 1
    print(span_len)
    
print(span([ 1, 2, 1, 1, 3]))
print(span([1, 4, 2, 1, 4, 4, 4 ]))
print(span([1, 4, 2, 1, 4, 4, 4 ]))
print(span([ 1, 2, 3, 4, 5, 6]))
