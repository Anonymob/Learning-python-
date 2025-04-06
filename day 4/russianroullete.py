import random

friends = ["affan","raiyan","Khushi","Zaida","Umar","Aayan","hashir"]
random_friend_no = random.randint(0,len(friends))
print(friends[random_friend_no])


#2nd option-

print(random.choice(friends))