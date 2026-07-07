# class TreeNode(object):
 #    def __init__(self, val=0, left=None, right=None):
   #      self.val = val
    #     self.left = left
      #   self.right = right


class Solution(object):
    def createBinaryTree(self, descriptions):
        nodes = {}
        children = set()
        
        def get_node(val):
            if val not in nodes:
                nodes[val] = TreeNode(val)
            return nodes[val]  
        
        for parent, child, isLeft in descriptions:
            p_node = get_node(parent)
            c_node = get_node(child)
            if isLeft:
                p_node.left = c_node
            else:
                p_node.right = c_node
            children.add(child)
        
        for val, node in nodes.items():
            if val not in children:
                return node
        