# question 1
# method - function -
# declare a function called
# 1 - def user_name():
#     2- def user_name
#     3 def user_name()
#     4 def void user_name()
#     5 user_name()
#     - takes user name
# - displays welcome user name back to user in same line

def user_name():
    username = input("please enter username: ")
    return f"welcome {username} "
print(user_name())