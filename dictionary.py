info={
    "key":"value",
    "name":"Rohit",
    "learning":"coding",
    "age":29,
    "is_adult":False,

    "subjects":["python","javascript","react native"],

    "topic":("dictionary","set"),
    12:"number check",

}

print("dictionairy",info)

print("dictionairy type",type(info))


print("access values",info["subjects"])

print("access values",info["age"])


info["name"]="Rohit Rai"

info["food"]="spicey"

print("info name changed",info)


null_dict={}

null_dict["name"]="Shradhha"
print("empty dict",null_dict)



# nested dictionary


student={

    "name":"Rahul kumar",
    "subjects":{
        "physics":90,
        "chem":65,
        "maths":40
    }
}



print("nested student dict",student)


print("nested student dict subjects",student["subjects"])

print("nested student dict subjects chemestry marks",student["subjects"]["chem"])



# keys

print("keys in student",student.keys())

# listing
print("dict typecaSTED T LIST",list(info.keys()))


print("length of dictionary",len(info))


# values in dict

print("values in dict",student.values())

# items


print("itrms in tuple",student.items())

# key method


print("key vlue return",student.get("name"))


# update dict
new_dict={
    "city":"Mumbai" ,
    "name":"Akshay"
}

student.update(
  new_dict
)

print("updated student",student)


# practise

word_meanings={
    "table":[" a peice of furniture","list of facts and figures"],
    "cat":"small animal"
}


print("word meaning",word_meanings)


marks_dict={}

marks=int(input("Enter first marks: "))

marks_dict.update({"phy":marks})

marks=int(input("Enter second marks: "))

marks_dict.update({"chem":marks})

marks=int(input("Enter third marks: "))

marks_dict.update({"bio":marks})


print("subject dict",marks_dict)









