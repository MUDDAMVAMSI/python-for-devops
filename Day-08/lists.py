my_family= ["Ram mohan", "Saraswathi", "Nikhila","Vamsi Kumar"]
print(my_family)
print("my_family") #see the difference
print(type(my_family))

my_family.append("Nikhila_Husband") #works only for one argument
#my_family.append("Nikhila_Husband", "Vamsi Kumar_Wife") #get error if two arguments removed
print(my_family)

my_family.remove("Nikhila_Husband") #works only for one argument
#my_family.remove("Nikhila","Nikhila_Husband") #get error if two arguments removed
print(my_family)

print(my_family[3]) #Indexing 
print(len(my_family)) #length of list
print(my_family[0:3]) #slicing print [0,1,2] elements

numbers=[5,10,15,3,4,1,8]
numbers.sort() #by default it gives in ascending order 
print(numbers)
numbers.sort(reverse=True) #descending order
print(numbers)

print(my_family[0]+ "--"+ my_family[1]) #concatenation

#output
'''
$ python lists.py 
['Ram mohan', 'Saraswathi', 'Nikhila', 'Vamsi Kumar']
my_family
<class 'list'>
['Ram mohan', 'Saraswathi', 'Nikhila', 'Vamsi Kumar', 'Nikhila_Husband']
['Ram mohan', 'Saraswathi', 'Nikhila', 'Vamsi Kumar']
Vamsi Kumar
4
['Ram mohan', 'Saraswathi', 'Nikhila']
[1, 3, 4, 5, 8, 10, 15]
[15, 10, 8, 5, 4, 3, 1]
Ram mohan--Saraswathi
'''
