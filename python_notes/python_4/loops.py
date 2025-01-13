# sum of even numbers
def sum_even_numbers(num):
    sum=0
    for i in range(0,num+1,2):
        sum+=i

    return sum


# print(sum_even_numbers(5) )


# multiplacation table upto 10 of a number 

def multipliaction_table(num):
    for i in range(1,11):
        if(i==5):
            continue
        else :
            print(f"{num}*{i}={num*i}")

# multipliaction_table(5)


# reverse string 

def reverse_string (string):
   return string[::-1]

print(reverse_string('ansh'))


items =["apple","banana","cherry","orange","kiwi","apple"]

def remove_duplicates(items):
    # return list(set(items))
    # return list(dict.fromkeys(items))
    
    duplicate=""
    for i in items:
        if items.count(i)>1:
            duplicate=i
            break

    return duplicate

print(remove_duplicates(items))