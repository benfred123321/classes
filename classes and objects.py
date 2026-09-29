class Food :
    def __init__(self,s,t,a,x,r,n):
        self.size = s
        self.taste = t
        self.aroma = a
        self.texture =  x
        self.rating = r
        self.name = n
        print("creating object")
    def show_details(self):
        print(self.size,self.taste,self.aroma,self.texture,self.rating,self.name)
    def change_taste(self,t):
        self.taste = t
    def rejuce_rating(self):
        self.rating = self.rating - 1



obs1 = Food(20,8,8,10,36,"apple")
obs1.show_details()
obs1.change_taste(10)
obs1.rejuce_rating()
obs1.show_details()
print(obs1.taste)
class Fruit (Food):
    def __init__(self,s,t,a,x,r,n,colour):
        super().__init__(s,t,a,x,r,n)
        self.colour = colour    


banana= Fruit(30,9,6,8,27,"banana","yellow")
banana.show_details()
print(banana.colour)
class Dog:
    def sound(self):
        print("woof")
class Cat :
    def sound(self):
        print("meow")
dog = Dog()
cat=Cat()
cat.sound()
dog.sound()