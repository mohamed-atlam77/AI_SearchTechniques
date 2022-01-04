adj = {
  '5' : ['3','7'],
  '3' : ['2', '4'],
  '7' : ['8'],
  '2' : [],
  '4' : ['8'],
  '8' : []
}

visited = {'5':False, '3':False, '7':False, '2':False, '4':False, '8':False} # List for visited nodes.
queue = []     #Initialize a queue

def bfs(adj, initial_state): #function for BFS
  visited[initial_state]=True
  queue.append(initial_state)

  while queue:          # Creating loop to visit each node
    m=queue.pop(0)
    print(m, end=' ')

    for neighbour in adj[m]:
      if visited[neighbour] == visited:
        visited[neighbour]=True
        queue.append(neighbour)



# Driver Code
print("Following is the Breadth-First Search")
bfs(adj, '5')
print(queue)
