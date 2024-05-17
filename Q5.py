a = int(input("enter marks of 1st subject"))
b = int(input("enter marks of 1st subject"))
c = int(input("enter marks of 1st subject"))

average = (a+b+c)/3
print(f"average = {average}")

if average >= 90:
    print("grade A")
elif average >= 80:
    print("grade B")
elif average >= 70:
    print("grade C")
elif average >= 60:
    print("grade D")
else:
    print("grade F")