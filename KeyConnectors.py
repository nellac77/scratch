# -*- coding: utf-8 -*-
"""
KeyConnectors - A simple exercise to identify key connections within a sample 
                group of coworkers. The request is "what is the average number 
                of connections per user?" Example from Data Science from 
                Scratch, by Joel Grus.
                
Created on Tue May 15 07:39:47 2018

@author: cjohn033
"""

# The data of the workers at the company, with employee ID and first name
users = [
    { "id": 0, "name": "Hero" },
    { "id": 1, "name": "Dunn" },
    { "id": 2, "name": "Sue" },
    { "id": 3, "name": "Chi" },
    { "id": 4, "name": "Thor" },
    { "id": 5, "name": "Clive" },
    { "id": 6, "name": "Hicks" },
    { "id": 7, "name": "Devin" },
    { "id": 8, "name": "Kate" },
    { "id": 9, "name": "Klein" }
]

# The "friendship" data, list of pairs represents who's connected to who by ID
# So the first tuple (0,1) implies Hero is friends with Dunn
friendships = [(0,1), (0,2), (1,2), (1,3), (2,3), (3,4),
               (4,5), (5,6), (5,7), (6,8), (7,8), (8,9)]

# Make a list of friends associated with a single user
# Make the empty list
for user in users:
    user["friends"] = []
    
# Populate the empty list
for i, j in friendships:
    # note that index i corresponds to the user id
    users[i]["friends"].append(users[j]) # make j a friend of i
    users[j]["friends"].append(users[i]) # make i a friend if j

# sum the length of the friends lists to count each user's number of friends
def number_of_friends(user):
    """how many friends does _user_ have"""
    return len(user["friends"])  # length of friend_id list

total_connections = sum(number_of_friends(user) for user in users)  # expect 24

# divide by number of users to obtain the average number of connections
from __future__ import division  # integer division, puh-lease
num_users = len(users)  # length of the users list
avg_connections = total_connections / num_users  # expect 2.4


""" Consider wich user is the most connected - Who has the most friends? """

# Sort users from who has the most firends to who has the least friends
# Make empty list (user_id, number_of_friends)
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]

# Now sort this list
sorted(num_friends_by_id,  # sort it
       key=lambda pair: pair[1],  # by num_friends (pair is the tuple)
       reverse=True)  # largest to smallest


"""Do we know any of these people? Let's suggest folks people should know"""

# How about refering friends-of-friends?
# Collect each user's friends
def friends_of_friend_ids_bad(user):
    # We use "foaf" for "friend of a friend"
    return [foaf["id"]
            for friend in user["friends"]  # for each of user's friends
            for foaf in friend["friends"]]  # get each of _their_ friends

