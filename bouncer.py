#Ask for age and than check if they can be allowed in a bar
age=input("Tell me what's your age")
if age:
   age=int(age); 
   if age>=21 and age<60:
	   print("go inside and enjoy drinks")
   elif age>=60:
     	print("woooah you are an eligible person go enjoy")
   elif age>=18 and age<21:
    	print("show us the wrist bands")
   else:
	   print("you cant enter little one")       
else:
	print("hey!!! please enter an age")			
	