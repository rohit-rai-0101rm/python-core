collection={1,2,3,4,"rohit",3}

print("collection",collection)

print("type",type(collection))

print("length of collections",len(collection))


# create an empty state
col=set()

print("empty set",type(col))

col.add("rohit")

col.add("ai")

col.add("mumbai")


col.add((1,2,3,4,5,6,7,8,9))





print("add value to set ",col)


col.remove("rohit")



print("remove value to set ",col)

# liat cant be added to set unhashable type list 
# immutable can be added to set not mutable


# clear set

# col.clear()

# print("set cleared",col)
col.pop()

print("popped collection set",col)


# union and intersection

set1={1,2,3}

set2={2,3,4,5}

print(set1.union(set2))

print(set1.intersection(set2))


# practise

unique_subjects={"python","java","C","C++","javascript","python"}

print("number of uniwue subjects",len(unique_subjects))

values={
    ("float",9.0),
    ("int",9)
        
        }


print("values",values)