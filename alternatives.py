#RANGE
'''print(list(range(11))) #range with upper bound value only
print(list(range(0,11))) #range with lower & upper bound values
print(list(range(0,11,2))) #range with lower bound, upper bound and skip size values'''

#DICTIONARIES
personal_details = {"name":"smith", "age":26, "nationality":"Kenyan", "ID":123456}
#print the whole dictionary
print(personal_details)
#print the keys
print(personal_details.keys())
#print the values
print(personal_details.values())
#get a value by its key
print(personal_details.get("name"))
print(personal_details["name"]) #same but pops an error if the key is not found
# Add several items to the dictionary at once
personal_details.update({"county":"nairobi","gender":"male"})
print(personal_details)
personal_details["name"] = "john"
print(personal_details)