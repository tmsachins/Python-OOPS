# initiate a class
class employee:
    # special method/magic method/dunder method - constructor
    def __init__(self):
        print("Started executing attributes")
        self.id=123
        self.salary=50000
        self.designation="SDE"
        print("attributes have been initiated")
    def travel(self,destination):
        print("This travel method was called manually")
        print(f"Employee is now travelling to {destination}")

sam=employee()
print(sam.salary)

print(type(sam))
# sam.travel("Delhi")


    # def __init__(self):
    #     # print(id(self))
    #     # print("Started executing attributes/data")
    #     self.id = 123
    #     self.salary = 50000
    #     self.designation = "SDE"
    #     # print("attributes/data have been initiated")

    # def travel(self):
    #     print("This travel method was called manually")
    #     print(f"Employee is now travelling to Delhi")


# create an obj/instance of the class
# sam = employee()

# print("Hi")

# sam.name = "Sam Kumar"
# print(id(sam))
# print(sam.name)

# shaktiman = employee()
# print(id(shaktiman))

# printing the attributes
# print(sam.id)

# calling a method
# sam.travel()

# print(type(sam))