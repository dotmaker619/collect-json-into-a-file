import json
  
# Data to be written
dictionary ={
    "name" : "sathiyajith",
    "rollno" : 56,
    "cgpa" : 8.6,
    "phonenumber" : "9976770500"
}
  
with open("sample-1-1.json", "w") as outfile:
    json.dump(dictionary, outfile)