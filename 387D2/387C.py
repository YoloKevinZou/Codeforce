n,q=map(int,raw_input().split())

tasks = []

availableServer = [0 for _ in xrange(n+1)]

for i in xrange(q):
	time, numberOfServerNeeded, timeToComplete =map(int,raw_input().split())	

	usedServer = []

	# Get servers to use
	for j in xrange(1, len(availableServer)):
		if availableServer[j] <= time:
			usedServer.append(j)

		if len(usedServer) == numberOfServerNeeded:
			break
			
	if len(usedServer) != numberOfServerNeeded:
		print("-1")
	else:
		print(sum(usedServer))
		for server in usedServer:
			availableServer[server] = time + timeToComplete