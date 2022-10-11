# Approach 1:
# real world application is task allocation
# uses directed graph to solve this
# if there is a edge from X to Y then X comes before Y in topological sort
# add jobs that dont have any pre-reqs or the jobs for which all pre-reqs are complete
# to the output first
# start at a node and see if that node has a pre-req
# if it has pre-reqs finish all pre-reqs first 
# and then come back to it
# once all pre-reqs are added, add the current node to the output
# mark nodes as visited if it is added to the output
# we are essentially applying DFS 
# we can start with any node
# if we have a cycle in the graph, 
# it means we dont have a valid topological sort
# O(J+D) time and Space as we are doing a DFS


# Approach 2:
# lets keep a track of no of pre-reqs each node has
# we dump nodes that dont have pre-reqs into an array
# grab the node that has no pre-reqs and use that node as starting point


def topologicalSort(jobs, deps):
	output = []
	dependencies = {}
	noDeps = []
	
	for job in jobs:
		for dep in deps:
			if dep[1] == job:
				if job in dependencies:
					dependencies[job].append(dep[0])
				else:
					dependencies[job] = [dep[0]]
		if job not in dependencies:
			noDeps.append(job)
			
	while len(noDeps) > 0:
		currentJob = noDeps.pop()
		output.append(currentJob)
		for job in dependencies:
			if currentJob in dependencies[job]:
				dependencies[job].remove(currentJob)
				if len(dependencies[job]) == 0:
					noDeps.append(job)
				
	noJobsLeft = True
	for job in dependencies:
		if len(dependencies[job]) != 0:
			noJobsLeft = False	
	
	if noJobsLeft:
		return output 
	else:
		return []





