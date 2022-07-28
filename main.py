import  json

#tells if num 1 and num2 is same or diffrent
num1 = input("put num1: ") 
num2 = input("put num2: ") 

def numdif (num1,num2) :
  if num1 == num2 :
    print("same nums")
  else :
    print("nums not same")

numdif (num1,num2)
#Python program to convert JSON data to Python object
json_obj =  '{ "Name":"David", "Class":"I", "Age":6 }'
python_obj = json.loads(json_obj)
print("\nJSON data:")
print(python_obj)
print("\nName: ",python_obj["Name"])
print("Class: ",python_obj["Class"])
print("Age: ",python_obj["Age"]) 