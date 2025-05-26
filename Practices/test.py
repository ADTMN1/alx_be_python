# # count = 100
# # while count > 0:
# #     print("Countdown:", count)
# #     count -= 1
# # print("Blast off!")
# # age=0
# #
# # while age<18:
# #    int((input("enter your age")))
# # print("you are old enough")
# #
# # secret_number=5
# #
# # guess=0
# # count=0
# #
# # while guess!=secret_number:
# #       count+=1
# #       guess= int(input("enter your guess"))
# # print(f"you found the number in {count
# # } trys")
#
# items = ["apple", "mango", "banana"]
#
# while True:
#     user = input("Enter the item: ")
#     if user in items:
#         print("You got the item!")
#         break
#     else:
#         print("Item not found. Try again.")


row=7

for i in range(0,row):
    for j in range(0,i+4):
        print("*",end="")
    print()

