Q1)
n=4
for i in range(1,n+1):
        for j in range(1, i + 1):
            print(j, end='')
        print()
Output=
1
12
123
1234
--------------------------------------------------------------------------------------------------------------------------------------
Q2)
for i in range(1,5+1):
        for j in range(1, i + 1):
            print("*", end='')
        print()

Output=
*
**
***
****
*****
---------------------------------------------------------------------------------------------------------------------------------------
Q3)
for i in range(1,5):
        for j in range(1, i + 1):
            print(i, end='')
        print()
1
22
333
4444
-------------------------------------------------------------------------------------------------------------------------------
q4)
n = 1
for i in range(1,6,1):
    for j in range(1,i):
        print(n,end=" ")
        n += 1
    print(" ")
Output
1  
2 3  
4 5 6  
7 8 9 10  
----------------------------------------------------------------------------------------------------------------------------
Q5)
n=4    
for i in range(1, n + 1):
    for j in range(65, 65 + i):
        print(chr(j), end="")
    print()
Output=
A
AB
ABC
ABCD
----------------------------------------------------------------------------------------------------------------------------------------------
Q6)
for i in range(5,0,-1):
    for j in range(1,i+1):
        print("*",end="")
    print(" ")

Ouput=

***** 
**** 
*** 
** 
* 
---------------------------------------------------------------------------------------------------------------------------------------------------------
for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    print(" ")
=>
12345 
1234 
123 
12 
1 
------------------------------------------------------------------------------------------------------------------------------------------------------------------
Q8)
4321
432
43
4

for i in range(4,0,-1): 
  for j in range(0,i): 
    print(4-j, end = " ") 
  print() 



4 3 2 1 
4 3 2 
4 3 
4
--------------------------------------------------------------------------------------------------
Q9)
for i in range(4, 0 ,-1): 
  for j in range(1,i+1): 
    print(chr(64 + j) , end = " ") 
  print() 
Output=
A B C D 
A B C 
A B 
A 
-------------------------------------------------------------------------------------------------
Q10)
for i in range(6, 0 ,-1): 
  for j in range(1,i+1): 
    print(chr(71- j) , end = " ") 
  print() 

Output=
F E D C B A 
F E D C B
F E D C
F E D
F E
F

-----------------------------------------------------------------------------------------------------------


Q11)


n = 5
for i in range(n):
     print(' ' * i, end='')
     print('*' * (n - i))

Output=

*****
 ****
  ***
   **
    *

-------------------------------------------------------------------------------------------


Q12)

for i in range(4, 0, -1):
		for j in range(1, i + 1):
			print("* ", end="")
		print("")
Output=

* * * * 
* * * 
* * 
* 
-------------------------------------------------------------------------------------------

Q13)

10
11  12
13  14  15


n = 10
for i in range(1,5,1):
    for j in range(1,i):
        print(n,end=" ")
        n += 1
    print(" ")


Output=


10  
11 12
13 14 15

-------------------------------------------------------------------------------------------

Q14)


D
DC
DCB
DCBA


n = 'D'
for i in range(4):
        ch=''
        for j in range(i + 1):
            ch += chr(ord(n) - j)
        print(ch)

Output=

D
DC
DCB
DCBA


---------------------------------------------------------------------------------------------

Q15)


10
10 11 
10 11 12
10 11 12 13 14

for i in range(1, 4 + 1):
    
    for j in range(1, i + 1):
        print(10 + j - 1, end=' ')
    print()  

Output=


10 
10 11
10 11 12
10 11 12 13
------------------------------------------------------------------------------------------------

Q16)



A
AB
ABC
ABCD


n=4    
for i in range(1, n + 1):
    for j in range(65, 65 + i):
        print(chr(j), end="")
    print()


Output=
A
AB
ABC
ABCD
--------------------------------------------------------------------------------------------
Q17)

DCBA
DCB
DC
D

for i in range(4, 0 ,-1): 
  for j in range(1,i+1): 
    print(chr(69- j) , end = " ") 
  print() 

Output=
D C B A 
D C B
D C
D
-----------------------------------------
Q18)
1
12
121
1212
12121
for i in range(1,6):
  for j in range(1, i + 1):
        if j <= i:
            print(1 if j == 1 or j == i else 2, end="")
  print()

-----------------------------------------------------------
Q19

F
HJ
LNP
RTVR

n = 70
for i in range(0, 4):
    for j in range(0, i + 1):
        r = chr(n)
        print(r, end=' ')
        n += 2
    print(" ")


Output=

F  
H J
L N P
R T V X
--------------------------------------------------------------------
Q20)
****
 ***
  **
   *
for i in range(4):
    for j in range(i):
        print(' ', end='')
    for k in range(4 - i):
        print('*', end='')
    print()

Output=
****
 ***
  **
   *

--------------------------------------------------------------------
Q21)
1234*
567**
89***
c= 1
for i in range(4):
    
    for j in range(4 - i):
        print(c, end='')
        c=c+ 1

    for k in range(i + 1):
        print('*', end='')
    print()


Output=

1234*
567**
89***
--------------------------------------------------------------------------
Q22)

*****
 ***
  *

n = 3
for i in range(1, n + 1):
	
	for j in range(1, i):
		print(" ", end="")

	for j in range(1, 2 * (n - i) + 2):
		print("*", end="")
	
	
	print()
Output=
*****
 ***
  *
----------------------------------------------------------------------------
Q23)
ABCD1
ABC12
AB123
A1234	

for i in range (1,5):
     for k in range (1,5):
          print( chr(65+(k-i)) ,end ="  ")
     for j in range(1,i+1):
      print(j , end="")
      
     print("") 
--------------------------------------------------------
Q24)
   A
  BC
 DEF
GHIJ

n=1
for i in range (1,6):
     for k in range (1,6-i):
          print("",end ="  ")
     for j in range(1,i):
      print(chr(64+n),end=" ")
      n=n+1
     print("") 
Output=
      A
    B C
  D E F
G H I J
-----------------------------------------------
Q25)
ABCD1
EFG23
HI456
J78910

row=4
n=1
for i in range(row):
    s= chr(ord('A') + i)
    for j in range(i + 1):
        print(chr(ord(s) + j), end='')
    for k in range(i + 1):
        print(n, end='')
        n+= 1
    print()