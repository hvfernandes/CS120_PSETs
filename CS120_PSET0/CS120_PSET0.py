#################
#               #
# Problem Set 0 #
#               #
#################


#
# Setup
#
class BinaryTree:
    def __init__(self, root):
        """
        :param root: the root of the binary tree
        """
        self.root: BTvertex = root
 
class BTvertex:
    def __init__(self, key):
        """
        :param: the key associated with the vertex of the binary tree
        """
        self.parent: BTvertex = None
        self.left: BTvertex = None
        self.right: BTvertex = None
        self.key: int = key
        self.size: int = None


#
# Problem 1a
#

# Input: BTvertex v, the root of a BinaryTree of size n
# Output: int, the size of the subtree rooted at v
# Side effect: sets the size of each vertex n in the
# ... tree rooted at vertex v to the size of that subtree
# Runtime: O(n)

# First intuition: size(v) = 1 + size(left) + size(right). Counting each subtree from scratch would recount every vertex once per ancestor, which is O(n*h)
# So I recurse first and combine after, and return the size (not just store it) so the parent reuses the children's work instead of recomputing it
# Why O(n): the recursion runs once per vertex, since a vertex is only reached through the single edge from its parent, and each call does O(1) work on top of its recursive calls

def calculate_sizes(v):
    # base case: an empty subtree has size 0 and nothing to store
    if v is None:
        return 0

    # recursive case: children first, then combine in O(1)
    # a missing child contributes 0, so vertices with 1 or 0 children need no special handling
    left_size = calculate_sizes(v.left)
    right_size = calculate_sizes(v.right)
    v.size = 1 + left_size + right_size
    return v.size


#
# Problem 1c
#

# Input: a positive integer t, 
# ...BTvertex v, the root of a BinaryTree of size n >= 2t+1
# Output: BTvertex, descendent of v such that its size is between 
# ... t and 2t-1 (inclusive)
# Runtime: O(h) 

# First intuition: the proof from 1b run forwards. Every case of it either stops or moves to the larger child
# Scanning the whole subtree would be O(n). But since a vertex of size s has a larger child of size >= (s-1)/2, then from size >= 2t+1 the larger child has size >= t and I can never undershoot the window
# Why O(h): algorithm moves only downward, so it performs at most h iterations, where h is the height of the subtree rooted at the original v
# There are at most h levels below v, and each iteration does O(1) comparisons on sizes already stored by

def FindDescendantOfSize(t, v):
    # follow the larger child while the current subtree is too large
    while v.size >= 2 * t + 1:
        left_size = 0 if v.left is None else v.left.size
        right_size = 0 if v.right is None else v.right.size

        if left_size >= right_size:
            v = v.left
        else:
            v = v.right

    # now, t <= v.size <= 2t
    # if v.size is 2t, its larger child has size between t and 2t-1
    if v.size == 2 * t:
        left_size = 0 if v.left is None else v.left.size
        right_size = 0 if v.right is None else v.right.size

        if left_size >= right_size:
            v = v.left
        else:
            v = v.right

    return v
