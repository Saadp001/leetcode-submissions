# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    
    def serialize(self, root):
        string = ""
        def solve(node):
            nonlocal string
            if not node:
                string += '#,'
                return 
    
            string+= str(node.val) + ','
            solve(node.left)
            solve(node.right)
        solve(root)
        return string
        
    def deserialize(self, data):
        idx = 0
        data = data.split(",")
        def solve():
            nonlocal idx
            if not data :
                return None
            if data[idx] == '#':
                idx +=1
                return None        
   
            node = TreeNode(int(data[idx]))
            idx+=1
            node.left = solve()
            node.right = solve()

            return node 
            
        return solve() 