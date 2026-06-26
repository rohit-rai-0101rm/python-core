# # class Student:
# #     college_name="Fatima"
# #     def __init__(self,fullName,marks):
# #         self.name=fullName
# #         self.marks=marks
# #     def hello(self):
# #         print("welcome student",self.name)
# #     def get_marks(self):
# #         return self.marks



# # s1=Student("Rohit",45)

# # s2=Student("Astuti",45)


# # print(s1.name,s1.marks,s1.college_name)

# # print(s2.name,s2.marks,s1.college_name)


# # s1.hello()

# # print(s1.get_marks())





# # # class Car:
# # #     color="blue"
# # #     brand="mercedeze"

# # # car1=Car()

# # # print(car1.color)
# # # print(car1.brand)



# class Student:
#     @staticmethod
#     def college():
#         print("Fatima")

#     def __init__(self,name,marks):
#         self.name=name
#         self.marks=marks



#     def get_avg(self):
#         sum=0
#         for val in self.marks:
#             sum+=val
#         print(f"hi ,{self.name} your avg marks is {sum/3}")



# s1=Student("tony stark",[99,98,97])

# s1.get_avg()












# abstraction


# class Car:
#     def __init__(self):
#         self.acc=False
#         self.brk=False
#         self.clutch=False
#     def start(self):
#         self.clutch=True
#         self.acc=True
#         print("car started")


# car1=Car()


# car1.start()






class Account:

    def __init__(self,balance,accountNo):
        self.balance=balance
        self.accountNo=accountNo

    # debit
    def debit(self,amount):
        self.balance-=amount
        print(f"Rs {amount} was debited")
        print(f" total balance is  {self.get_balance()} ")

    # credit

    def credit(self,amount):
        self.balance+=amount
        print(f" total balance is  {self.get_balance()} ")


    def get_balance(self):
        return self.balance



acc1=Account(10000,12345678)

acc1.debit(1000)

acc1.credit(400)

acc1.get_balance()

