#exercise 10\n",
# golf series records\n",
#this program gets player's data from the user and \n",
#saves it as record in the golf.txt file\n",
def main():
    #get number of players record to create\n",
    num_players = int(input('how many players: '))
    #open a file to write the records to\n",
    players_file = open('golf.txt', 'w')
    #get each employees data and write it to the file\n",
    for count in range(1, num_players + 1):
        # get the data from an employee\n",
        print('Player #', str(count), sep=' ')
        name = input('Name: ')
        golf_score = int(input('Score: '))
        #write the data as a record to the file\n",
        players_file.write(name + '\n')
        players_file.write(str(golf_score) + '\n')
        #display a blank line\n",
        print()
     #close the file\n",
    players_file.close()
    print('Employees records written to file')
#call the main function\n",
main()