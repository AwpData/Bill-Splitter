import random

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

    print("Do you want to use the \"Who is lucky?\" feature? Write Yes/No")
    choice = str(input())
    if choice == "Yes":
        lucky_person = random.choice(list(friends.keys()))
        print("{} is the lucky one!".format(lucky_person))
        split_value = round(total / (len(friends) - 1), 2)
        for key in friends:
            if key == lucky_person:
                friends[key] = 0
            else:
                friends[key] = split_value
    else:
        print("No one is going to be lucky")
        split_value = round(total / len(friends), 2)
        friends = dict.fromkeys(friends, split_value)
    print(friends)
