# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it.
print("Try programiz.pro")
shape=input("What shape do you want square,rectangle,triangle,trapezoid,circle").lower()
if shape=="rectangle":
    side=input("What is the length")
    if not sideto.isdigit():
        print("Not a number")
    sideto=input("What is the width")
    if not sideto.isdigit():
        print("Not a number")
    else:
        conv=int(side)
        gyat=int(sideto)
        print("The area is", conv*gyat)
    print("The area is", side*sideto)
elif shape=="square":
    side=input("What is the length")
    if not side.isdigit():
        print("Not a number")
    else:
        conv=int(side)
        print("The area is", conv**2)

elif shape=="triangle":
    side=input("What is the breadth")
    if not side.isdigit():
        print("Not a number")
    sideto=input("What is the height")
    if not sideto.isdigit():
        print("Not a number")
    else:
        conv=int(side)
        gyat=int(sideto)
        print("The area is", 0.5*conv*gyat)
elif shape=="trapezoid":
    side=input("What is the base1")
    if not side.isdigit():
        print("Not a number")
    sideto=input("What is the base2")
    if not sideto.isdigit():
        print("Not a number")
    gyat=input("What is the height")
    if not gyat.isdigit():
        print("Not a number")
    else:
        conv=int(side)
        gyat=int(sideto)
        ohio=int(gyat)
        print("The area is", ((conv*gyat)/2)*(ohio))
    print("The area is", (gyat)*(conv+gyat)/2)
elif shape=="circle":
    side=input("What is the radius")
    if not side.isdigit():
        print("Not a number")
    else:
        conv=int(side)
        print("The area is", (3.14)*(conv**2))
 
else:
    print("Your listed shape isn't on this list or what you've entered is not a shape")
