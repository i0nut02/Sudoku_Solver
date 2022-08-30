
class lru_cache(object):

    def __init__(self):
        self.nodes = {} # pos : node
        self.start_node = None
        self.last_node = None
        self.pointer = self.start_node
        
    def add(self, ID):
        node = Double_linked_node(ID)

        if self.start_node == None:
            self.start_node = node
            self.last_node = node
            self.pointer = self.start_node
        else:
            self.last_node.next = node
            node.prev = self.last_node
            self.last_node = node

        self.nodes[ID] = node


    def remove(self, ID):
        if not ID in self.nodes:
            return None

        node = self.nodes[ID]
        prev_node = node.prev
        next_node = node.next

        if next_node != None:
            next_node.prev = prev_node
        
        if prev_node != None:
            prev_node.next = next_node

        if node == self.start_node:
            self.start_node = next_node
        
        if node == self.last_node:
            self.last_node = prev_node

        del self.nodes[ID]
        node = None
        self.pointer = self.start_node
    
    def get(self):
        out = self.pointer

        if out == None:
            return None

        self.pointer = self.pointer.next
        return out.ID
    
    def go_back(self):
        if not self.pointer == None:    
            self.pointer = self.pointer.prev


class Double_linked_node(object):

    def __init__(self, pos, prev = None, next = None):
        self.ID = pos
        self.prev = prev
        self.next = next
    
    
