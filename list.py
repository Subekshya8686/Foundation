days_list = ['Sunday','Monday','Tuesday','Wednesday','Thrusday','Friday','Saturday']
#index_list = ['0',      '1',        '2',       '3',       '4',      '5',      '6'  ]

my_value = days_list[3]

print(my_value)

# append() method 
#--> It is used to insert data into the existing list
#print(days_list)
#days_list.append("kasmiday")
#print(days_list)

print("Your recent days")
for day in days_list:
  print(day,end=" ")

#pop()
#--> It is used to eject the last element/item from the list and return to us.
print(days_list)
days_list.pop()
print(days_list)
