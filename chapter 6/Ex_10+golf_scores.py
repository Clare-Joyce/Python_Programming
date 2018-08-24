#exercise 10, part 2\n",
# reading the players records\n",
def main():
    #open the file\n",
    count = 0
    players_file = open('golf.txt', 'r')
    name = players_file.readline()
    while name != '':
        score = int(players_file.readline())
        name = name.rstrip('\n')
        count = count + 1
        print('Player #', count)
        print('Name:', name)
        print('Score = ', score)
        name = players_file.readline()
    players_file.close()
#call the main function\n",
main()