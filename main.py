#str
s="Hello!"
print(s)
print(type(s))

#int
print(3)
print(type(3))

#float
print(5/4)
print(type(5/4))

#complex
print(3+4j)
print(type(3+4j))

print(5//4)
print(5==4)
print(3<6)
print(4>2)

if (7==3):
  print("ir vienadi")
else:
  print("nav vienadi")

if (3==3):
  print("ir vienadi")
else:
  print("nav vienadi")


#list
L=[]
print(type(L))

#tuckle
T=()
print(type(T))

#dictionaries
D={}
print(type(D))

#  0  1   2   3    4   5  6   ...
L=[21,34, 45, 56, 67, 76, 43]
print(L[3])
print(L[0])
L.append(3.2)
L.append("Hi")
L.insert(2,88)
print(L)
print(len(L))

L=[32,54, 73, 12, 42, -2]
print(len(L))
L.sort()
print(L)

T=(33, 44, 66, 33, 45)
print(T)
print(T.count(33))

#  key      value
D={"abols":"apple", "bumbieris": "birne", "pi":"3.14" , "e" : 2.72}
print(D["abols"])
print(D["bumbieris"])
print(D["pi"])
print(D["e"])

D.update({"a":"alpha"})
print(D)
D.update({"T": T})
print(D)
D.update({"L":L})
print(D)

d=[0,1,2,3,4,5]
print(d)
for i in d:
  print(i, i*i)

for i in range(10):
  print(i, i*i,'\t',i*i*i)


print("Start")

a = 3;
i = 0

while(i <a):
  print("Hello")
  i = i+1
  print(i)

print("END")

#no kura, līdz kuram, solis, pa cik iet uz priekšu
for i in range(-3, 10,2):
  print(i)


def g(name):
  print(f"Hello, " + name + "!")

g("Janis")

name= input("Ievadi savu vārdu")
def g(name):
  print(f"Hello, " + name + "!")

g(name)