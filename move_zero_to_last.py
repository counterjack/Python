

# - List of numbers (including 0) 

# Input: 
# Output: [1, 2, 4, 3, 5, 0,0,0,]


# - No extra space


# _input =   [0, 2, 0, 4, 3, 0, 5, 0]
# # _input = [0,0,0,0,1]
# index_of_zero = 0
# zero_present = False
# zero_at_first_place = _input[0] == 0
# for idx, item in enumerate(_input):
#     print (index_of_zero)
#     if item != 0 and index_of_zero > idx:
#         continue

#     elif item != 0 and index_of_zero < idx and (zero_present or zero_at_first_place):
#         print ("Did i come here")
#         _input[idx] = 0
#         _input[index_of_zero] = item
#         index_of_zero = idx
#         zero_present = True

#     elif item == 0 and index_of_zero == 0 and not zero_at_first_place :
#         print ("I am here?", idx)
#         index_of_zero = idx
#         zero_present = True

# print (_input)




# a = "I am Vinay. I am working in Bluestacks. I work here as full stack developer."
a = "I am Vinay. I am working in Bluestacks. Vinay works in Bluestacks as full stack developer."

a = a.replace(".", "").split(" ")
# output = "am"
# - 2nd highest frequency

dic = {}

for item in a:
    try:
        dic[item] += 1
    except:
        dic[item] = 1
print (dic)
all_frequencies = dic.values()

highest = all_frequencies[0]
second_highest = all_frequencies[0]

for item in all_frequencies:
    if (item  > highest ):
        highest = item
    if item < highest and item > second_highest:
        second_highest = item

sorted_freq = sorted(all_frequencies, reverse=True)


for item in dic:
    if dic[item] == second_highest:
        print (item)




