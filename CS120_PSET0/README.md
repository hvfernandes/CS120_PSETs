# CS 120 PSET 0 — Question 1

A binary tree is *size-augmented* when every vertex `u` stores `u.size`, the
number of vertices in the subtree rooted at `u`.

- `solution.py` — parts (a) and (c)
- `part_b_proof.tex` — part (b), the strong-induction proof

## (a) `calculate_sizes(v)`

Sets `u.size` for every `u` in the subtree at `v`, in one post-order pass:
`size(v) = 1 + size(left) + size(right)`.

**O(n):** the recursion runs once per vertex, since a vertex is only reached
through the single edge from its parent, and does constant work per call. The
naive version — recounting each subtree from scratch — is `O(n·h)` instead,
because every vertex gets recounted once per ancestor.

## (c) `find_descendant_of_size(t, v)`

Given `t` and a vertex `v` with `v.size >= 2t+1`, returns a descendant `w` with
`t <= w.size <= 2t-1`, by walking down to the larger child until the size lands
in the window.

**O(h):** each step goes down exactly one level and does two comparisons on
sizes that are already stored. It works because a vertex of size `s` has a child
of size at least `(s-1)/2`, so from a vertex of size `>= 2t` the larger child
has size `>= t` — sizes shrink on the way down but never skip past the window.

## Note

Python's recursion limit is around 1000 frames, so `calculate_sizes` raises
`RecursionError` on a path-shaped tree with more than about 1000 vertices. That
is a Python limit, not an algorithmic one; an explicit stack avoids it.
