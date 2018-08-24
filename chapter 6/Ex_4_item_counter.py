#exercise 4\n",
# Item counter\n",
def main():
    #initialize a counter
    count = 0
    #open the file
    #i use friends.txt coz i have that file
    friends_count = open('Friends.txt', 'r')
    # read everyline and increment the counter
  
    for line in friends_count:
        friends_name = line
        count = count + 1
    friends_count.close()
    print('You have a total of ', count, ' friends.')
#call the main function
main()