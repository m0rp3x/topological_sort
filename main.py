def topological_sort(items, partial_order):
    def add_node(graph, node):

        if not node in graph:
            graph[node] = [0]

    def add_arc(graph, fromnode, tonode):

        graph[fromnode].append(tonode)

        graph[tonode][0] = graph[tonode][0] + 1

    graph = {}
    for v in items:
        add_node(graph, v)
    for a, b in partial_order:
        add_arc(graph, a, b)

    # Шаг 2 - найти все корни (узлы с нулевым входящих дуг).
    roots = [node for (node, nodeinfo) in graph.items() if nodeinfo[0] == 0]

    sorted = []
    while len(roots) != 0:

        root = roots.pop()
        sorted.append(root)
        for child in graph[root][1:]:
            graph[child][0] = graph[child][0] - 1
            if graph[child][0] == 0:
                roots.append(child)
        del graph[root]
    if len(graph.items()) != 0:
        print("цикл!!!")
        exit()
    return sorted


print(topological_sort(['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j'],
                       [('a', 'c'), ('a', 'd'), ('a', 'g'), ('b', 'e'), ('c', 'f'), ('d', 'b'), ('d', 'h'), ('d', 'i'),
                        ('e', 'i'), ('f', 'g'), ('g', 'd'), ('j', 'f'), ('j', 'i')]))