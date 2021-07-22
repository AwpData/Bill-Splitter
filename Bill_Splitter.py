print("Enter the number of friend joining (including you)")
friend = int(input())
friends = dict()
if friend <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    for i in range(friend):
        friends[str(input())] = 0
    print("Enter the total bill value:")
    total = int(input())
    split_value = round(total / len(friends), 2)
    friends = dict.fromkeys(friends, split_value)
    print(friends)
