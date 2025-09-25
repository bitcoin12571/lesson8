x = int(input("enter a number "))
if x%2 ==2:
    print("number is even")
else:
    print("Number is odd")
x = float(input("enter a number "))
y = float(input("enter second number"))
c = x+y
print(c)

a = float(input("enter the temperature "))
if a<= 0:
    print("freezing")
else:
    print("good temperature")

enter_fruis = input("youtr fav fruit")
enter_fruis.lower().strip()
match enter_fruis:
    case "banana":
        print("yellow ")
    case "apple":
        print("red")
    case "grape":
        print("good")
    case _ :
        print(" your fruit is " , enter_fruis)


mynum = "4"
guess = int(input("guess my number"))
if guess == mynum:
    print("You got it")
elif guess >mynum:
    print("too high")
elif guess <mynum:
    print( "Too low")
else:
    print("nothing")

for i in range(1,10):
    print(i)


for i in range (2,10):
    print (i)


for i in range(5,0 ,-1):
    print(i)
    
letters = ["a","b","c"]
for letter in letters:
    print(letter)
word = "world "
for letter in word:
    print(letter)

items = ["pen","book","eraser"]
for item in items:
    print(f"pached a {item}")
animals = ("cow","dog","cat")
for animal in animals:
    print(f"animals{animals}")


student ={
    "name ":"David ",
    "age":"4",
    "sex":"male"

}
for key,value in student.items():
    print(key,"=",value)

player = {
    "username":"max99",
    "level":5,
    "score":380
}

subjects = { "math","history","bilogy"}
for i in subjects:
    print(i)
data = ("alex",13, "B+")
for i in data:
    print(f"Data{i}")

names = ["ana","tom","mia"]
ages = {"ana":10
    ,"tom":11,
        "mia":12}
for name in names:
    print(f"{name} is {ages[name]}")

