# CS 120 PSET 0

Solutions to Question 1(a) and (c). Both are in `CS120_PSET0.py`.

A binary tree is *size-augmented* when every vertex `v` stores `v.size`, the
number of vertices in the subtree rooted at `v`.

## Question 1a

> **(a) (recursive programming)** Write a recursive program `calculate_sizes` that given a vertex `v` of a binary tree `T`, calculates the sizes of all of the subtrees rooted at descendants of `v`. After running your program on `T.root`, every vertex `v` in `T` should have `v.size` set to the size of the subtree rooted at `v`. (Recall that the size attributes are initialized to
> `None`.) We call the resulting tree a *size-augmented* tree.
> Your program should run in time `O(n)` when given the root of a tree with `n`
> vertices. In a sentence or two, informally justify why your program has such a runtime

### Solution

The size of the subtree at `v` is `1` (for `v` itself) plus the sizes of its two
subtrees, so the recursion computes the children first and combines them:

```
size(v) = 1 + size(v.left) + size(v.right)
```

- **Base case:** an empty subtree (`v is None`) has size `0`.
- **Recursive case:** recurse on both children, store `v.size`, and return it

Returning the size, rather than only storing it, is what makes this efficient:
the parent reuses the value instead of recomputing it. Vertices with 1 or 0
children need no special handling, since a missing child contributes `0`

**Runtime `O(n)`:** the recursion is called exactly once per vertex, since a
vertex is only reached through the single edge from its parent, and each call
does constant work on top of its recursive calls. Recounting each subtree from
scratch instead would be `O(n·h)`, because every vertex would be counted once
per ancestor.

## Question 1c

> **(c) (from proofs to algorithms)** Turn your proof from Part 1b into a Python program `FindDescendantOfSize(t,v)` that, given a positive integer `t` and a vertex `v` of a *size-augmented* tree `T` such that `v.size >= 2t+1`, finds and returns a descendant `w` of `v` such that `t <= w.size <= 2t-1`.
> Your algorithm should run in time `O(h)`, where `h` is the height of the subtree rooted at `v`; explain in words why this is the case.

### Solution

This is the proof from Part 1b run forwards. The proof does more than assert
that a vertex with `t <= size <= 2t-1` exists: every case either stops or moves
to the larger child.

The lemma from 1b is what makes walking possible: a vertex of size `s` has a larger child `w` with `size(w) >= (s-1)/2`. So from a vertex
of size `>= 2t+1`, the larger child has size `>= t`

At each step, with `w` the larger child of the current vertex, exactly three cases arise, matching the three cases of the proof:

1. `t <= w.size <= 2t-1` — `w` is good, return it
2. `w.size == 2t` — by the corollary, the larger child of `w` is good, return it
3. `w.size >= 2t+1` — `w` satisfies the precondition, so repeat from `w`

**Runtime `O(h)`:** case 3 is the only one that repeats, and it moves from a vertex to one of its children, so each iteration descends exactly one level. There are at most `h` levels below `v`, and each iteration does a constant number of comparisons on sizes already stored by part (a). Space is `O(1)`, since the loop uses no recursion or stack
