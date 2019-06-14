'''
This program asks user for input in kms
and converts it to miles
'''



print("Enter Kms you want to convert to miles")
kms=input();
print(f"ok you said {kms}");
miles=float(kms)/1.60934;
print(f"In miles: {round(miles,2)}");