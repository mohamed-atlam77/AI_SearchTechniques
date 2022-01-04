adj_list={
        'A':['B','C'],
        'B':['D','E'],
        'C':['B','F'],
        'D':[],
        'E':['F'],
        'F':[]
        }

color={}
parent={}
traverse_time={}
dfs_traverse_output=[]
time=0
for node in adj_list:
    color[node]='w'
    parent[node]=None
    traverse_time[node]=[-1,-1]

print(color)
print(parent)
print(traverse_time)

def dfs(u):
    global time
    color[u]='G'
    traverse_time[u][0]=time
    dfs_traverse_output.append(u)
    for v in adj_list[u]:
        if color[v]=='w':
            parent[v]=u
            dfs(v)
    color[u]='B'
    traverse_time[u][1]=time
    time+=1


dfs('A')



for node in adj_list:
    print(node,'-->', traverse_time[node])

print(color)
