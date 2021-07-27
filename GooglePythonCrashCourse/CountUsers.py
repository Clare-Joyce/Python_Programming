# The count_users function recursively counts the amount of users that belong to a 
# group in the company system, by going through each of the members of a group and
# if one of them is a group, recursively calling the function and counting the 
# members

def count_users(group):
  count = 0
  for member in get_members(group):
    count += 1
    if is_group(member):
      x = count-1
      count = x + count_users(member)
  return count

print(count_users("sales")) # Should be 3
print(count_users("engineering")) # Should be 8
print(count_users("everyone")) # Should be 18