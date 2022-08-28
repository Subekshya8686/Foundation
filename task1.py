'''num = int(input("Enter number: "))

def number_checker(num):
    odd=[]
    even=[]
    for i in range(num):
        if( i%2 == 0) and (i != 0):
            even.append(i)
        else:
            odd.append(i)

    print(f"Even list is : {even}, odd list is = {odd}")

number_checker(num)'''

odd_list=[]
even_list=[]
[even_list.append(i) if i%2 ==0 else odd_list.append(i) for i in range]
