print("Enter the number of friend joining (including you)")
friend = int(input())
if friend <= 0:
    print("No one is joining for the party")
else:
    friends = dict()
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(friend):
        friends[str(input())] = 0

    print(friends)
