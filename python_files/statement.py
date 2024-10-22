name =input("enter your name")
if len(name) < 3:
    print("name must be at least 3 chracter")
elif len(name) > 50:
    print("name must be a maximum of 50 character")
else:
    print("name looks good")
