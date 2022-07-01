# 1.Python program to combine two dictionary adding values for common keys.
# output: ({'a': 400, 'b': 400, 'd': 400, 'c': 300})

# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# d3={}

# for i in d1:
#     for j in d2:
#         if i == j:
#             d3[i] = d1[i] + d2[j]
        
#         if i != j and i not in d3 and j not in d3:
#             d3[i] = d1[i]
#             d3[j] = d2[j]

# print(d3)






# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
# 2.Python program to count the number of characters (character frequency) in a string. (make function)
# e.g 'google.com'
# output:  {'g': 2, 'o': 3, 'l': 1, 'e': 1, '.': 1, 'c': 1, 'm': 1}

# def counter_bot(string):
#     letters=[]
#     output = {}
#     counter=1
#     for letter in string:
#         letters.append(letter)

#     for i in range(0, len(letters)):
#         counter=1
#         for j in range(i+1, len(letters)):
#             if letters[j] == letters[i]:
#                 counter+=1

#         if letters[i] not in output:
#             output[letters[i]] = counter
#     print(output)


# input_data = input("Enter a string : ")
# counter_bot(string = input_data)







# ---------------------------------------------------------------------------------------------------------------------------------------------------------------
# 3.Python program to get a single string from two given strings, separated by a space and swap the first two characters of each string.(slicing concepts)

# Sample String : 'abc', 'xyz'
# Expected Result : 'xyc abz'


# words = []
# slice_one = []
# slice_two = []
# swap = ''
# text_one = input("Enter the first string value : ")
# text_two = input("Enter the second string value : ")
# j=0
# k=0
# for i in text_one:
#     slice_one.append(i)

# for j in text_two:
#     slice_two.append(j)


# for k in range(0, len(text_one)):
#     if k < 2:
#         swap = slice_one[k]
#         slice_one[k] = slice_two[k]
#         slice_two[k] = swap
 
# print(f"{''.join(slice_one)} {''.join(slice_two)}")

