# Search methods

import search

ab = search.GPSProblem('M', 'F'
                       , search.romania)

print(search.breadth_first_graph_search(ab).path())
print("---------------------------------------------")
print(search.depth_first_graph_search(ab).path())
print("---------------------------------------------")
#------------------------NUESTRO----------------------
print(search.branch_and_bounds_graph_search(ab).path())
print("---------------------------------------------")
print(search.metodo_subestimacion(ab).path())
print("---------------------------------------------")

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450