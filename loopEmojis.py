for i in range(10):  
  print("\U0001f600 "*i)

#conditional approach  
for num in range(10):
    count=0
    smileys=""
    while(count<=num):
      smileys+="\U0001f600 "
      count+=1
    print(smileys);  