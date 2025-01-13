def vote(voter_id, candidate, voters, votes):
    if voter_id in voters:
        print(f"Voter {voter_id} has already voted.")
        return False
    else:
        voters.add(voter_id)
        if candidate in votes:
            votes[candidate] += 1
        else:
            votes[candidate] = 1
        print(f"Voter {voter_id} voted for {candidate}.")
        return True

def main():
    voters = set()
    votes = {}

    while True:
        voter_id = input("Enter voter ID (or 'exit' to stop): ")
        if voter_id.lower() == 'exit':
            break
        candidate = input("Enter candidate name: ")
        vote(voter_id, candidate, voters, votes)

    print("\nVoting results:")
    for candidate, count in votes.items():
        print(f"{candidate}: {count} votes")


if __name__ == "__main__":
    main()  