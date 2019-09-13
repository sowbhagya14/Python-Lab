Python 3.7.3 (default, Aug 20 2019, 17:04:43) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>>d = {} 
print(d)  
{}
>>> d = {1:'name',2:'place',3:'animal',4:'thing'} 
print(d) 
{1: 'name', 2: 'place', 3: 'animal', 4: 'thing'}
>>>d = {1:'name',2:'place',3:'animal',4:'thing',5:{10,20,0,40,50}}
print(d) 
{1: 'name', 2: 'place', 3: 'animal', 4: 'thing', 5: {0, 40, 10, 50, 20}}
>>>d = {1:'name',2:'place',3:'animal',4:'thing',5:{10,20,0,40,50}}
del d[3]
print(d)
{1: 'name', 2: 'place', 4: 'thing', 5: {0, 40, 10, 50, 20}}
>>>d = {1:'name',2:'place',3:'animal',4:'thing',5:{10,20,0,40,50}}
d.popitem() 
print(d) 
{1: 'name', 2: 'place', 3: 'animal', 4: 'thing'}
>>>d = {1:'name',2:'place',3:'animal',4:'thing',5:{10,20,0,40,50}}
d.clear()
print(d) 
{}
>>>d = {1:'name',2:'place',3:'animal',4:'thing',5:{10,20,0,40,50}}
d.update()
print(d) 
{1: 'name', 2: 'place', 3: 'animal', 4: 'thing', 5: {0, 40, 10, 50, 20}}
 

