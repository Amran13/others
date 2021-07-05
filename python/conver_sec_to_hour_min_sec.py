
# Write a C program to convert a given integer (in seconds) 
# to hours, minutes and seconds

seconds = input("Enter the how many seconds :")
seconds = int(seconds)
Hour = int(seconds / (60*60))
Minute = int((seconds - (Hour*3600)) /60)
Sec = int((seconds - (Minute*60) - (Hour*3600)))
print("H : M : S = ",Hour,Minute,Sec)