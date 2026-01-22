#  print 1 to 100
i =1
while i<=100:
    print(i)
    i+=1

#  print 100 to 1   

i =100
while i>=1:
    print(i)
    i-=1

    # print the multiplication table in the end 

i =1
n =int(input("enter the value of n")) 
while i<=10:
    print(n*i)
    i+=1

    # print the list

nums= [1,4,9,16,25,36,49,64,81,100]
idx = 0
while idx <len(nums) :
 print(nums[idx])
 idx+=1    

#   number found at tuple

nums= (1,4,9,16,25,36,49,64,81,100)

x = 36
i=0
while i<len(nums):
   if(nums[i] == x):
      print("found at idx",i)
      i+=1