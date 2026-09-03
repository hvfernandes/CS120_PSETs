"""CS 120 PSET 0 -- Question 1, parts (a) and (c)."""


class Vertex:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.parent = None
        self.size = None


# --- (a) calculate_sizes ---------------------------------------------------
#
# First idea: for each vertex, walk its subtree and count. That's O(n*h),
# because each vertex gets recounted once per ancestor.
#
# Fix: don't throw the children's counts away. Go bottom-up and combine them in
# O(1): size(v) = 1 + size(left) + size(right). Returning the size (not just
# storing it) is what lets the parent reuse the child's work.
#
# O(n): the recursion runs once per vertex, since a vertex is only reached
# through the single edge from its parent, and does O(1) work per call.

def calculate_sizes(v):
    """Set u.size for every u in the subtree rooted at v. Returns v's size."""
    if v is None:
        return 0
    v.size = 1 + calculate_sizes(v.left) + calculate_sizes(v.right)
    return v.size


# --- (c) find_descendant_of_size -------------------------------------------
#
# First idea: part (b) only says a vertex in the window [t, 2t-1] exists, not
# where, so scan the whole subtree and check t <= u.size <= 2t-1 on each vertex.
# O(n), and it wastes the augmentation: the sizes are directions, not labels.
#
# Fix: from part (b), a vertex of size s has a child of size >= (s-1)/2, so
# sizes at least halve going down and can't skip the window. From a vertex of
# size >= 2t, the larger child has size >= ceil((2t-1)/2) = t, so we never
# undershoot. Walk down to the larger child until the size lands in the window.
#
# O(h): each step goes down one level and does two comparisons on stored sizes.

def find_descendant_of_size(t, v):
    """Return a descendant w of v with t <= w.size <= 2t-1.

    Assumes a size-augmented tree and v.size >= 2t+1.
    """
    u = v
    while u.size > 2 * t - 1:                 # i.e. while u.size >= 2t
        left = u.left.size if u.left else 0
        right = u.right.size if u.right else 0
        u = u.left if left >= right else u.right
    return u
