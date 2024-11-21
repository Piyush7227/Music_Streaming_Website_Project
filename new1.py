# class Human:
#     def eat(self):
#         print("can eat")
#     def work(self):
#         print("can work")
# class Male(Human):
#     def height(self):
#         print("good height")
# male1=Male()
# male1.eat()
# male1.height()

# ### method overwritting
# class Human:
#     def eat(self):
#         print("can eat")
#     def work(self):
#         print("can work")
# class Male(Human):#child class
#     def height(self):
#         print("good height")
#     def work(self):
#         super().work()
#         Human().work()
#         print("can do coding")
# male1=Male()
# male1.eat()


##multiple inheritance
# class Human:
#     def eat(self):
#         print("can eat")
#     def work(self):
#         print("can work")
# class Male(Human):
#     def height(self):
#         print("good height")
# male1=Male()
# male1.eat()
# male1.height()

### method overwritting
# class Human:
#     def eat(self):
#         print("can eat")
#     def work(self):
#         print("can work")
# class Male():#child class
#     def height(self):
#         print("good height")
#     def work(self):
#         print("can do coding")
# male1=Male()
# male1.eat()
# male1.height()
# male1.work()

# class Boy(Human,Male):#child class
#     pass
# boy1=Boy()
# Human.eat1(boy1)
# Male.height(boy1) #from which class.name of method(for which object)

class Human:
    def eat(self):
        print("can eat")
    def work(self):
        print("can work")
class Male(Human):#child class
    def height(self):
        print("good height")
    def work(self):
        print("can do coding")
class Boy(Male):#child class
    def sleep(self):
        print("is sleeping")
    def work(self):
        print("child can also work")
boy1=Boy()
Human.eat(boy1)
Boy.sleep(boy1)

