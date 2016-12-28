numberOfPeople, numberOfTeam = map(int, raw_input().split())

minPairs = 0

peoplePerTeam = numberOfPeople / numberOfTeam
extras = numberOfPeople % numberOfTeam

minPairs += ((peoplePerTeam) * (peoplePerTeam+1)/2) * extras
minPairs += ((peoplePerTeam)*(peoplePerTeam-1)/2) * (numberOfTeam - extras)

numberOfPeople -= (numberOfTeam - 1)

maxPairs = (numberOfPeople * (numberOfPeople - 1)) / 2

print minPairs, maxPairs