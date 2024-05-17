# my_list = ['kibria', 'b', 'c', 'd']
# your_list = ['milon', 'hello', 'how are you']
# # my_string = "".join(my_list)
# # my_string = my_string + "".join(your_list)
# my_string = []
# my_string = my_string + my_list + your_list
# print(my_string) 

# list_1 = [52, 182, 156, 46, 168, 191, 65, 156, 107, 34, 137, 248, 197, 156, 98, 162]
# for i in list_1:
#     print("for ", i, " chr is: ", chr(i))

# text = "4¶.¨¿Ak\"øÅb¢"

# for char in text:
#     print(f"Character: {char}, Unicode Code Point: {ord(char)}")

# for i in range(9, 0, -1):
#     print(i, end=" ")

# Example string with leading and trailing whitespace
my_string = "   Hello   World   "

# Strip leading and trailing whitespace, then split based on whitespace
split_string = my_string.strip()

print(split_string)
