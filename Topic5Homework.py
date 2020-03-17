Days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
print(Days)
# Creating a List with the days
Your_Day = str(input("Enter the Day"))
#Creating a string input variable asking user to enter the day
if Your_Day == Days[0] or Your_Day == Days[1] or Your_Day == Days[2] or Your_Day == Days[3] or Your_Day == Days[4]:
    print("Its a weekday")
#control flow to check if it is a weekday ie 0-4 in the list
elif Your_Day == Days[5] or Your_Day == Days[6]:
    #Checking to see if input is a weekend ie 5-6 in the list
    print("Its the weekend,yay!")
else:
    print("Please Enter a Day...")
#Will pring the else part if input entered does not match first two control flows ie not in the list