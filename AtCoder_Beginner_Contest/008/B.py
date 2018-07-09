from collections import defaultdict

def main():
    votes = defaultdict(lambda: 0)

    for i in range(int(input())):
        votes[input()] += 1

    max_vote = -1
    max_name = ""

    for name,vote in votes.items():
        if vote > max_vote:
            max_vote = vote
            max_name = name

    print(max_name)

main()
