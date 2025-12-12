class BinomialTree:
    def __init__(self, key = None):
        self.key = key
        self.degree = 0
        self.parent = None
        self.child = None
        self.sibling = None
        
    
    def __merge__(self, other):
        if self.key is None:
            return other
        if other.key is None:
            return self
        if self.key <= other.key:
            result = self
            child_tree = other
        else:
            result = other
            child_tree = self
    
        child_tree.parent = result
        child_tree.sibling = result.child
        result.child = child_tree
        result.key += 1
        
        return result


    def __insert__(self, knot):
        new_tree = BinomialTree(knot)
        return self.__merge__(new_tree)
