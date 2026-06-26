# f=open("demo.txt","r")

# # data=f.read()
# # data=f.read(5)


# line1=f.readline()
# # print("file data",data,type(data))

# print("line1",line1)

# f.close()


# f=open("demo.txt","a")

# f.write("\nthis is a new line javascript")



# f.close()


# f=open("sample.txt","w")


# f.close()



# add content start of the file
# f=open("demo.txt","r+")

# f.write("abc")

# f.close()



# f=open("demo.txt","w+")

# print(f.read())
# f.write("abc")
# f.close()


# with open("demo.txt","r") as f:
#     data=f.read()

#     print(data)



# with open("demo.txt","w") as f:
#     f.write("new data")

#     print(data)



# import os

# os.remove("demo.txt")




# with open("practise.txt","w") as f:
#     f.write("Hi Everyone\nwe are learning File I/O\nusing java\nI like programming in java")




# with open("practise.txt","r") as f:
#     data=f.read()
#     new_data=data.replace("java","python")




# with open("practise.txt","w") as f:
#     f.write(new_data)


# with open("practise.txt","r") as f:
#     data=f.read()
#     if(data.find("learnindddg")!=-1):
#         print("found")
#     else:
#         print("not found")




# def check_for_line():
#     word="learning"
#     data=True
#     line_no=1
#     with open("practise.txt","r") as f:
#         while data:
#             data=f.readline()
#             if(word in data):
#                 print(line_no)
#             line_no+=1
#     return -1



# check_for_line()










even_count = 0
odd_count = 0

with open("numbers.txt", "r") as f:
    data = f.read()
    numbers = data.split(',')

for num in numbers:
    num = int(num)
    
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1

print("Even numbers:", even_count)
print("Odd numbers:", odd_count)























































