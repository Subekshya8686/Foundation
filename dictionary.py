"""
It is always represents in the form of:
my_dictionary = {"key":"Value"}
"""

# Why we need dictionary?
#--> To overcome the problem exist in list.
#For eg:
#user_detail=["Kasmi","Thapa",20,["English","Nepali","Japanese"],9845141112,["Burger","Pizza","Mo Mo"]]

user_details = {
    "first_name":"Kasmi",
    "last_name":"Thapa",
    "Language_spoken":["English","Nepali","Japanese"],
    "contact":9845141112,
    "fav_food":["Burger","Pizza","Mo mo"]
}

print(user_details["first_name"])


for key,value in user_details.items():
    print(f"The key is:{key} and its value is: {value}")

#for key,value in user_details.items():
    #print(f"The key is:{key} ")

#for key,value in user_details.items():
    #print(f"The key is:{key} ")

