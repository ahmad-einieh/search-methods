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


# Breadth First Search Method
def BreadthFirstSearch(graph, src, dst):
    count = 0
    q = [(src, [src], 0)]
    visited = {src}
    if src == dst:
        return src, 0, count + 1, len(visited)
    while q:
        # count = count + 1
        (node, path, cost) = q.pop(0)
        for temp in list(graph[node].keys()):
            count = count + 1
            if temp == dst:
                return path + [temp], cost + graph[node][temp], str(count), len(visited)
            else:
                if temp not in visited:
                    visited.add(temp)
                    q.append((temp, path + [temp], cost + graph[node][temp]))


# Depth First Search Method
def DepthFirstSearch(graph, src, dst):
    stack = [(src, [src], 0)]
    visited = {src}
    count = 0
    if src == dst:
        return src, 0, count + 1, len(visited)
    if src == dst:
        return src, 0, count + 1, len(visited)
    while stack:
        (node, path, cost) = stack.pop()
        for temp in list(graph[node].keys()):
            if temp == dst:
                return path + [temp], cost + graph[node][temp], count, len(visited)
            else:
                if temp not in visited:
                    visited.add(temp)
                    stack.append((temp, path + [temp], cost + graph[node][temp]))


# Iterative Deepening Search Method
def IterativeDeepening(graph, src, dst):
    level = 0
    count = 0
    stack = [(src, [src], 0)]
    visited = {src}
    numberCount = 0
    if src == dst:
        return src, 0, count + 1, len(visited)
    while True:
        level += 1
        while stack:
            numberCount = numberCount + 1
            if count <= level:
                count = 0
                (node, path, cost) = stack.pop()
                for temp in list(graph[node].keys()):
                    if temp == dst:
                        return path + [temp], cost + graph[node][temp], numberCount, len(visited)
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
                        if temp == dst:
                            return path + [temp], cost + graph[node][temp], numberCount, len(visited)
                        else:
                            if temp not in visited_bfs:
                                visited_bfs.add(temp)
                                q.append((temp, path + [temp], cost + graph[node][temp]))
                break


def ucsHelper(item):
    return item[2]


def ucs(graph, src, dst):
    count = 0
    q = [(src, [src], 0)]
    visited = {src}
    if src == dst:
        return src, 0, count + 1, len(visited)
    while q:
        # count = count + 1
        (node, path, cost) = q.pop(0)
        for temp in list(graph[node].keys()):
            count = count + 1
            if temp == dst:
                return path + [temp], cost + graph[node][temp], str(count), len(visited)
            else:
                if temp not in visited:
                    visited.add(temp)
                    q.append((temp, path + [temp], cost + graph[node][temp]))
                    q.sort(key=ucsHelper)

# print(BreadthFirstSearch(dict_graph, "Adham", "Tathleeth"))
# n = 1
# print(dict_graph)
# print("------------------------------------------------")
# while n == 1:
#     x = eval(input("enter the type of search you want to do \n1.BFS 2.DFS 3.ID 4.UCS:: \n "))
#     if x == 1:
#         src = input("Enter the source: ")
#         dst = input("Enter the Destination: ")
#         while src not in dict_graph or dst not in dict_graph:
#             print("No such city name")
#             src = input("Enter the correct source (case_sensitive):\n")
#             dst = input("Enter the correct destination(case_sensitive):\n ")
#         print("for BFS")
#         print((BreadthFirstSearch(dict_graph, src, dst)))
#
#     elif x == 2:
#         src = input("Enter the source: ")
#         dst = input("Enter the Destination: ")
#         while src not in dict_graph or dst not in dict_graph:
#             print("No such city name")
#             src = input("Enter the correct source (case_sensitive):\n")
#             dst = input("Enter the correct destination(case_sensitive):\n ")
#         print("for DFS")
#         print((DepthFirstSearch(dict_graph, src, dst)))
#
#     elif x == 3:
#         src = input("Enter the source:")
#         dst = input("Enter the Destination: ")
#         while src not in dict_graph or dst not in dict_graph:
#             print("No such city name")
#             src = input("Enter the correct source (case_sensitive):\n")
#             dst = input("Enter the correct destination(case_sensitive):\n")
#         print("for ID")
#         print((IterativeDeepening(dict_graph, src, dst)))
#     elif x == 4:
#         src = input("Enter the source:")
#         dst = input("Enter the Destination: ")
#         while src not in dict_graph or dst not in dict_graph:
#             print("No such city name")
#             src = input("Enter the correct source (case_sensitive):\n")
#             dst = input("Enter the correct destination(case_sensitive):\n")
#         print("for UCS")
#         print((ucs(dict_graph, src, dst)))
#
#     n = eval(input("enter 1 if you wish to continue:\n"))
