def shortestDistance(N,M,A,X,Y):
	from collections import deque
	
	if A[0][0] == 0:
		return -1

	visited = set((0, 0))
	dequee_pipeline = deque([(0,0,0)])
	directions = [ [0,-1], [0, 1], [1,0], [-1,0]]

	while dequee_pipeline:
		cur_i, cur_j, cur_step = dequee_pipeline.popleft()

		if cur_i == X and cur_j == Y:
			return cur_step

		for direction in directions:
			next_i, next_j = cur_i + direction[0], cur_j + direction[1]

			if 0<= next_i < N and 0<= next_j < M and (next_i, next_j) not in visited:
				visited.add( (next_i, next_j))
				dequee_pipeline.append((next_i, next_j, cur_step + 1))

	return -1


N=3
M=4
A=[[1,0,0,0], 
   [1,1,0,1],
   [0,1,1,1]]
X=2
Y=3 

print(shortestDistance(N,M,A,X,Y))