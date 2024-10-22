'''coordinate = (1,2,3)
x, y, z = coordinate
print(x,y,z)'''
phone = input("Phone: ")
customer = {
    "1": "one",
    "2": "two" ,
    "3": "three"
}
output = ""
for man in phone:
   output += customer.get(man,"!") + " "
print(output)