import Queue

DEBUG = True


class Graph:
    def __init__(self):
        self.vertexes = []
        self.edges = []

    def add_vertex(self, payload):
        v = Vertex(payload)
        self.vertexes.append(v)
        return v

    def add_edge(self, begin, end):
        e = Edge()
        e.connect_begin(begin)
        e.connect_end(end)

        if e.begin is not None and e.end is not None:
            begin.add_edge(e)
            end.add_edge(e)
            self.edges.append(e)

    def breadth_first_search(self, item):
        q = Queue.Queue()

        q.put(self.vertexes[0])

        while not q.empty():
            # Dequeue to get a node
            v = q.get()
            if DEBUG:
                self.print_status(q, v)
            # Check if the node matches what we need
            if v.payload == item:
                self._reset_graph()
                return v

            # If the node has not been explored we will
            for e in v.edges:
                if e.begin != v and not e.begin.explored:
                    q.put(e.begin)
                elif e.end != v and not e.end.explored:
                    q.put(e.end)

            v.explored = True

        self._reset_graph()

        return None

    def depth_first_search(self, item):
        s = Stack()

        s.push(self.vertexes[0])

        while not s.empty():
            # Dequeue to get a node
            v = s.pop()

            if DEBUG:
                self.print_status(s, v)

            # Check if the node matches what we need
            if v.payload == item:
                self._reset_graph()
                return v

            v.explored = True

            # If the node has not been explored we will
            for e in v.edges:
                if e.begin != v and not e.begin.explored:
                    s.push(e.begin)
                elif e.end != v and not e.end.explored:
                    s.push(e.end)

        self._reset_graph()

        return None

    def _reset_graph(self):
        q = Queue.Queue()

        q.put(self.vertexes[0])

        while not q.empty():
            v = q.get()

            if DEBUG:
                self.print_status(q, v)

            # If the node has not been explored we will
            for e in v.edges:
                if e.begin != v and e.begin.explored:
                    q.put(e.begin)
                elif e.end != v and e.end.explored:
                    q.put(e.end)

            v.explored = False

    def _unexplored_nodes(self):
        return len([x for x in self.vertexes if x.explored == False])

    def print_status(self, q, v):
        print "Node: {}\t\tUnexplored nodes: {}\tTasks: {}".format(str(v.payload),str(self._unexplored_nodes()), str(q.unfinished_tasks))

class Vertex:
    def __init__(self, payload):
        self.edges = []
        self.explored = False
        self.payload = payload

    def __unicode__(self):
        return self.payload

    def __str__(self):
        return self.payload

    def add_edge(self, edge):
        self.edges.append(edge)


class Edge:
    def __init__(self):
        self.begin = None
        self.end = None

    def connect_begin(self, vertex):
        if vertex != self.end:
            self.begin = vertex

    def connect_end(self, vertex):
        if vertex != self.begin:
            self.end = vertex


class Stack:
    def __init__(self):
        self.__storage = []

    def empty(self):
        return len(self.__storage) == 0

    def push(self, p):
        self.__storage.append(p)

    def pop(self):
        return self.__storage.pop()

    def unfinished_tasks(self):
        return len(self.__storage)