
friends = ["Jim, Jack, Noob"]
#friends is collection you want to loop over
for friend in friends:
    print(friend)


friends = ["Jim, Jack, Noob"]
len(friends)
for index in range(len(friends)):
    print(friends[index])
    

for index in range(3, 10):
    print(index)


friends = ["Jim, Jack, Noob"]
for index in range(5):
    if index == 0:
        print("First Iteration")
    else:
        print("Not first Iteration")