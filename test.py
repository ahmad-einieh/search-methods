from queue import PriorityQueue
import time
import pyvis.network

#pyvis_graph = pyvis.network.Network(notebook=True, height="100%", width="100%")

dict_graph = {}

# Read the data.txt file
with open('cities.txt', 'r') as f:
    for l in f:
        city_a, city_b, p_cost = l.split()
        if city_a not in dict_graph:
            dict_graph[city_a] = {}
        dict_graph[city_a][city_b] = float(p_cost)
        if city_b not in dict_graph:
            dict_graph[city_b] = {}
        dict_graph[city_b][city_a] = float(p_cost)


def BreadthFirstSearch(graph, src, dst):
    count = 0
    q = [(src, [src], 0)]
    visited = {src}
    while q:
        # count = count + 1
        (node, path, cost) = q.pop(0)
        for temp in list(graph[node].keys()):
            count = count + 1
            if temp == dst:
                return path + [temp], cost + graph[node][temp], str(count), visited
            else:
                if temp not in visited:
                    visited.add(temp)
                    q.append((temp, path + [temp], cost + graph[node][temp]))


def fun(item):
    return item[2]


def ucs(graph, src, dst):
    frontier = [(src, [src], 0)]
    visited = {src}
    while frontier:
        (node, path, cost) = frontier.pop()
        for temp in list(graph[node].keys()):
            if temp == dst:
                return path + [temp], cost + graph[node][temp]
            else:
                if temp not in visited:
                    visited.add(temp)
                    # for k in frontier:
                    # x =(temp, path + [temp], cost + graph[node][temp])
                    frontier.append((temp, path + [temp], cost + graph[node][temp]))
                    frontier.sort(key=fun)


def ucs2(graph, src, dst):
    count = 0
    q = [(src, [src], 0)]
    visited = {src}
    while q:
        # count = count + 1
        (node, path, cost) = q.pop(0)
        for temp in list(graph[node].keys()):
            count = count + 1
            if temp == dst:
                return path + [temp], cost + graph[node][temp], str(count)
            else:
                if temp not in visited:
                    visited.add(temp)
                    q.append((temp, path + [temp], cost + graph[node][temp]))
                    q.sort(key=fun)


def DepthFirstSearch(graph, src, dst):
    stack = [(src, [src], 0)]
    visited = {src}
    while stack:
        (node, path, cost) = stack.pop()
        for temp in list(graph[node].keys()):
            if temp == dst:
                return path + [temp], cost + graph[node][temp]
            else:
                if temp not in visited:
                    visited.add(temp)
                    stack.append((temp, path + [temp], cost + graph[node][temp]))


def IterativeDeepening(graph, src, dst):
    sizer = 0
    level = 0
    count = 0
    stack = [(src, [src], 0)]
    visited = {src}
    while True:
        level += 1
        while stack:
            if count <= level:
                count = 0
                (node, path, cost) = stack.pop()
                for temp in list(graph[node].keys()):
                    sizer = sizer + 1
                    if temp == dst:
                        return path + [temp], cost + graph[node][temp], str(sizer)
                    else:
                        if temp not in visited:
                            visited.add(temp)
                            count += 1
                            stack.append((temp, path + [temp], cost + graph[node][temp]))
            else:
                q = stack
                visited_bfs = {src}
                while q:
                    (node, path, cost) = q.pop(0)
                    for temp in list(graph[node].keys()):
                        sizer = sizer + 1
                        if temp == dst:
                            return path + [temp], cost + graph[node][temp], str(sizer)
                        else:
                            if temp not in visited_bfs:
                                visited_bfs.add(temp)
                                q.append((temp, path + [temp], cost + graph[node][temp]))
                break


xx, yy, zz, newXX = BreadthFirstSearch(dict_graph, "Riyadh", "Abha")
# with open("cities.txt", 'r') as f:
#     for l in f:
#         color = "red"
#         a, b, c = l.split()
#         if a in xx or b in xx:
#             color = "green"
#         pyvis_graph.add_node(a, label=a, title=a, color=color)
#         pyvis_graph.add_node(b, label=b, title=b, color=color)
#         pyvis_graph.add_edge(a, b, label=c, title=c, color=color)
#
# pyvis_graph.force_atlas_2based()
# pyvis_graph.show("graph.html")
