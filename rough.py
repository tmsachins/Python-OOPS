lst = [1,2,3]
my_str = "mlops playlist"
my_int = 155

# print(type(lst))
# print(type(my_str))
# print(type(my_int))
# # lst.capitalize()
# my_str = my_str.capitalize()

# print(my_str)

from oops_proj import chatbook
user1 = chatbook()

print(user1.id)

# Using static method directly from class rather than obj
chatbook.set_id(10)

user2 = chatbook()
# print(user2.user_id)
print(user2.id)

user3 = chatbook()
# print(user3.user_id)
print(user3.id)



# getter and setter
# print(user1.get_name())
# user1.set_name("Agent X")
# print(user1.get_name())




# # function vs method below
# lst = [1,2,3]

# # # function
# a1 = len(lst)
# print(a1)

# # method
# user1 = chatbook()
# # user1.sendmsg()
# print(user1.get_name())
# user1.set_name("Agent X")
# print(user1.get_name())

