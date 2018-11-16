# -*-coding:utf-8 -*-
import sys
sys.setrecursionlimit(20000)
class DijkstraExtendPath(object):
    def __init__(self, node_map):
        self.node_map = node_map
        self.node_length = len(node_map)
        self.used_node_list = []
        self.collected_node_dict = {}
    def __call__(self, from_node, to_node):
        self.from_node = from_node
        self.to_node = to_node
        self._init_dijkstra()
        return self._format_path()
    def _init_dijkstra(self):
        self.used_node_list.append(self.from_node)
        self.collected_node_dict[self.from_node] = [0, -1]
        for index1, node1 in enumerate(self.node_map[self.from_node]):
            if node1:
                self.collected_node_dict[index1] = [node1, self.from_node]
        self._foreach_dijkstra()
    def _foreach_dijkstra(self):
        if len(self.used_node_list) == self.node_length - 1:
            return
        for key, val in self.collected_node_dict.items():  # 遍历已有权值节点
            if key not in self.used_node_list and key != to_node:
                self.used_node_list.append(key)
            else:
                continue
            for index1, node1 in enumerate(self.node_map[key]):  # 对节点进行遍历
                # 如果节点在权值节点中并且权值大于新权值
                if node1 and index1 in self.collected_node_dict and self.collected_node_dict[index1][0] > node1 + val[0]:
                    self.collected_node_dict[index1][0] = node1 + val[0] # 更新权值
                    self.collected_node_dict[index1][1] = key
                elif node1 and index1 not in self.collected_node_dict:
                    self.collected_node_dict[index1] = [node1 + val[0], key]
        self._foreach_dijkstra()
    def _format_path(self):
        node_list = []
        temp_node = self.to_node
        node_list.append((temp_node, self.collected_node_dict[temp_node][0]))
        while self.collected_node_dict[temp_node][1] != -1:
            temp_node = self.collected_node_dict[temp_node][1]
            node_list.append((temp_node, self.collected_node_dict[temp_node][0]))
        node_list.reverse()
        return node_list
def set_node_map(node_map, node, node_list):
    for x, y, val in node_list:
        node_map[node.index(x)][node.index(y)] = node_map[node.index(y)][node.index(x)]  =  val
if __name__ == "__main__":
    node = ["JFK","ATL", "CLT", "PHX"]
    node_list = [(node[0], node[1], 760), (node[0], node[2], 360), (node[1], node[3], 960), (node[2], node[3], 200)]
    node_map = [[0 for val in xrange(len(node))] for val in xrange(len(node))]
    set_node_map(node_map, node, node_list)
    # A -->; D
    from_node = node.index("JFK")
    to_node = node.index("PHX")
    dijkstrapath = DijkstraExtendPath(node_map)
    path = dijkstrapath(from_node, to_node)
    print path
    print node_map
