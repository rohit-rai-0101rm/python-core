# marks=[12 ,23 ,45,"rohit", True,45]
# marks2=[12 ,23 ,45]

# fruits=["apple","banana","leechi"]

# print("marks",marks)

# print("typeof marks",type(marks))

# print("length marks",len(marks))


# print("marks at index 2", marks[1])

# # strings are imuutable , lists are mutable

# marks[0]=97


# print("updated mark",marks)



# print("sliced mark",marks[1:len(marks)])


# print("negative sliced mark",marks[-3:-1])


# marks.append("nitin")

# print("aapended marks",marks)
# print("marks2 sorted",marks2.sort())


# print("marks2 sorted",marks2.sort(reverse=True))


# print("marks 2 sorted result",marks2)

# fruits.sort(reverse=True)
# print("fruits  sorted result",fruits)

# marks.reverse()

# marks.insert(3,"Inserted")
# print("reversed marks list",marks)


# marks.remove("rohit")


# print("removed 45",marks)



movies=[]

movies.append(input("enter first movie "))

movies.append(input("enter second movie "))


movies.append(input("enter third movie "))






print("movie list",movies)

list2=[1,2,3,2,1]


list3=list2.reverse()

if list2==list3:
    print("palindrome")
else:
    print("not palindrome")