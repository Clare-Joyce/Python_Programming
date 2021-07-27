
import random
def write_quote(quote):
  f = open("quotes.txt", "a")
  f.writelines(quote)
  f.close()
# write_quote("Work hard, dream big\n")
# write_quote("Every moment matters\n")
# write_quote("Trust your instincts\n")
# write_quote("Stay foolish to stay sane\n")
# write_quote("Try again, fail again, fail better\n")
# write_quote("Leave no stone unturned\n")
# write_quote("No guts, no story\n")
# write_quote("She believed she could and so, she did!\n")

def get_quote():
  # print("\nKeep it logically awesome.\n")

  f = open("quotes.txt")
  quotes = f.readlines()
  f.close()

  rnd1 = random.randint(0, len(quotes)-1)
  rnd2 = random.randint(0, len(quotes)-1)

  while rnd1==rnd2:
    rnd2 = random.randint(0, len(quotes)-1)
  
  print(quotes[rnd1].strip("\n"))
  print(quotes[rnd2], end='')

if __name__== "__main__":
  get_quote()
