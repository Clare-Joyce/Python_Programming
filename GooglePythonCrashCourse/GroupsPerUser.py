"""
The groups_per_user function receives a dictionary, 
which contains group names with the list of users. 
Users can belong to multiple groups

"""

def groups_per_user(group_dictionary):
    user_groups = {}
    # Go through group_dictionary
    for group in group_dictionary:
        # Now go through the users in the group
        for user in group_dictionary[group]:
            # Now add the group to the the list of
            if user not in user_groups:
                user_groups[user] = [group]
    # groups for this user, creating the entry
    # in the dictionary if necessary
            else:
                user_groups[user].append(group)

    return(user_groups)

print(groups_per_user({"local": ["admin", "userA"],
        "public":  ["admin", "userB"],
        "administrator": ["admin"] }))