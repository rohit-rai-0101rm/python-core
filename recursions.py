# def show(n):
#     if n == 0:
#         return 
#     print(n)
#     return show(n - 1)

# show(5)


# def factorial(n):

#     if (n==0 or n==1):
#         return 1
#     else:
#         return n*factorial(n-1)
    
# print(factorial(5))





# def sum(n):
#     if n==0:
#         return 0
#     return n+sum(n-1)

# print(sum(4))








cities=["delhi","gurugram","noida","pune","mumbai"]

def print_list(cities,idx=0):

    if idx == len(cities):
        return
    print(cities[idx])
    print_list(cities,idx+1)

print_list(cities)












