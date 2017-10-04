# Definition for a undirected graph node
# class UndirectedGraphNode:
#     def __init__(self, x):
#         self.label = x
#         self.neighbors = []

class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None
        stack = [node]
        root = UndirectedGraphNode(node.label)
        visited = {}
        visited[root.label] = root
        while stack:
            curr = stack[0] 
            del stack[0]
            for i in curr.neighbors:
                if i.label not in visited:
                    visited[i.label] = UndirectedGraphNode(i.label)
                    stack.append(i)
                visited[curr.label].neighbors.append(visited[i.label])            
        return root


#old version:
class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node
    def cloneGraph(self, node):
        if not node:
            return None
        nodes = {}
        stack = [node]
        visited = {}
        while stack:
            curr = stack[0] 
            if curr.label not in nodes:
                new_node = UndirectedGraphNode(curr.label)
                nodes[new_node.label] = new_node
            else:
                new_node = nodes[curr.label]
                
            del stack[0]
            for i in curr.neighbors:
                if i.label not in nodes:
                    t_new = UndirectedGraphNode(i.label)
                    new_node.neighbors.append(t_new)
                    nodes[i.label] = t_new
                else:
                    new_node.neighbors.append(nodes[i.label])
                if i.label not in visited and i.label != curr.label:
                    flag = True
                    for j in stack:
                        if i.label == j.label:
                            flag = False
                    if flag:
                        stack.append(i)
            visited[new_node.label] = 0
            
        for i in nodes:
            return nodes[i]
        return None