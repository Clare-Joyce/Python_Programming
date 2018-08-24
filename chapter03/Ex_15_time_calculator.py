#calculating and displaying the number of days, 
#hours, minutes and seconds from a given number of seconds.

#prompt user for number of second,
time_in_seconds = int(input("Enter number of seconds: ")) # whole numbers required.

if time_in_seconds <60:
	print(time_in_seconds, "seconds is less then 1 min.")


elif time_in_seconds<=3600:
	print(int(time_in_seconds/60), "minutes,", time_in_seconds%60, "seconds.")

	
elif time_in_seconds<= 86400:
	print(int(time_in_seconds/3600), "hours,", int((time_in_seconds%3600)/60), 
		"minutes,", (time_in_seconds%3600)%60, "seconds.")
	
else:
	print(int(time_in_seconds/86400), "days,", int((time_in_seconds%86400)/3600),
	 "hours,", int(((time_in_seconds%86400)%3600)/60),
	 "minutes,", ((time_in_seconds%86400)%3600)%60, "seconds.")
	
