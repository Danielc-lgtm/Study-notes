---
type: exercise
subject: algebraic-topology
difficulty: "⭐⭐"
prereqs:
  - "Def - Singular Homology"
  - "Thm - Singular and Simplicial Homology Agree on Triangulable Spaces"
  - "Def - Euler Characteristic"
tags: [geometry, algebraic-topology, torus]
---

# Problem Statement

Compute $H_*(T^2; \mathbb{Z})$ for the $2$-torus $T^2$, using the standard rectangle-with-identifications triangulation (Frankel Figure 13.12). Identify the basis $1$-cycles $A, B$ and verify that $T^2$ is orientable by computing $\partial[T^2] = 0$, where $[T^2]$ is the fundamental class — the sum of all $2$-simplices with consistent orientation. Compute the Euler characteristic $\chi(T^2)$.

**Recall:**

The $2$-torus is the quotient $T^2 = \mathbb{R}^2 / \mathbb{Z}^2$, equivalently the square $[0, 1] \times [0, 1]$ with edges identified: $(0, y) \sim (1, y)$ and $(x, 0) \sim (x, 1)$. Frankel triangulates this square into $18$ oriented triangles (Figure 13.12), with three columns and three rows of "diamond" pairs, where each rectangular cell is split by a diagonal into two triangles.

A [[Def - Singular Chain|singular chain]] $[T^2] = \sum_{i=1}^{18} \tau_i$ summing all the triangles with consistent orientation gives an oriented $2$-chain on $T^2$. Its boundary $\partial[T^2]$ should vanish if the triangulation respects the identifications and the orientation is consistent.

By [[Thm - Singular and Simplicial Homology Agree on Triangulable Spaces]], the simplicial homology of the triangulation equals the singular homology of $T^2$.

---

# Convergent Strategy

**Problem class:** This is a direct simplicial-homology computation on a specific space (the torus) with a specific triangulation. The class is "compute $H_*(M)$ from a chosen triangulation," using the simplicial chain complex and linear algebra on the boundary matrices. The simplicial-to-singular equivalence ([[Thm - Singular and Simplicial Homology Agree on Triangulable Spaces]]) guarantees the answer is the singular homology, independent of the triangulation chosen.

**Assumption pattern:** The torus has a specific triangulation by $18$ triangles (Frankel Figure 13.12) with vertices labelled $Q_0, \dots, Q_8$ (with $Q_0$ at the four corners identified, and $Q_i$ at boundary midpoints and interior points). The orientations of the triangles are chosen so that adjacent triangles induce opposite orientations on their common edges — making the boundary computation tractable.

**Theorem routing:** Use [[Thm - Singular and Simplicial Homology Agree on Triangulable Spaces]] to equate simplicial and singular homology. Compute $\partial[T^2]$ directly — this either vanishes (confirming orientability and giving a non-trivial $2$-cycle) or doesn't (showing non-orientability). Identify the generators of $H_1(T^2)$ by examining $1$-cycles modulo boundaries — the basis turns out to be the two loops $A$ (around the $x$-direction) and $B$ (around the $y$-direction). Compute $H_0, H_1, H_2$ and verify Euler characteristic $\chi(T^2) = 0$.

**Key decision point:** The non-obvious step is recognising that the boundary of $[T^2]$ vanishes because of the edge identifications: each interior edge is shared by two triangles with opposite induced orientations (cancelling in $\partial$), and each boundary edge is identified with another boundary edge in such a way that the boundary contributions also cancel. For the cylinder (non-identified boundary), $\partial[\text{Cyl}] = B + C$ (top + bottom). For the torus (all boundary identified), $\partial[T^2] = A + B - A - B = 0$. The pattern $-A$ comes from the orientation reversal between the two identified copies of the loop $A$.

---

# Legal Operations Used

1. **Triangulate the space and read off the simplicial chain complex** (operation 11 from the topic page). The torus triangulation gives explicit simplicial chains in each degree, with known boundary maps.

2. **Compute the boundary $\partial[T^2]$ explicitly** (operation 3, in the form "use the explicit chain to verify a property"). Sum the contributions from all $18$ triangles, observe interior edges cancel, observe boundary identifications cancel.

3. **Read $H_0$ as the path-component count** (operation 7). $T^2$ is connected, so $H_0 = \mathbb{Z}$.

4. **Read top homology and orientability** (operation 8). $\partial[T^2] = 0$ certifies that $[T^2]$ is a non-trivial $2$-cycle, hence $H_2(T^2; \mathbb{Z}) = \mathbb{Z}$ (orientable).

5. **Identify generators of $H_1$ by examining the simplicial $1$-cycles** (analogous to operation 3). The boundary loops $A$ and $B$ are $1$-cycles (their boundaries vanish because of identifications); they are not boundaries (no $2$-chain in $T^2$ has them as boundary alone); they are linearly independent in $H_1$.

---

# Hints

> [!note]- Hint 1
> Set up the rectangle triangulation as in Frankel Figure 13.12. Compute the boundary of one triangle to get a sum of three edges (with signs). When you sum all $18$ triangles, what happens to the interior edges? What about the boundary edges (which are identified in pairs)?

> [!note]- Hint 2
> The interior edges of the triangulation are each shared by exactly two triangles. By choosing orientations consistently, each interior edge appears with opposite signs in the two triangles' boundaries — so they cancel in the total $\partial[T^2]$.
>
> The boundary edges of the rectangle are identified in pairs: the left side of the rectangle equals the right side (let's call this loop $A$), and the top equals the bottom (loop $B$). When you sum $\partial[T^2]$, the boundary contributions become $A + B - A - B = 0$ — the negatives come from the orientation reversal in the identification.

> [!note]- Hint 3
> Now find the $1$-cycles. The loops $A$ (vertical edge) and $B$ (horizontal edge), traversed once each, are $1$-cycles: they go around the torus once and return to their starting point.
>
> To compute $H_1$, identify which $1$-chains are cycles and which are boundaries. The boundaries (images of $2$-chains under $\partial$) are spanned by the boundaries of individual triangles, which by Step 1 sum to zero on the whole $T^2$. Modulo boundaries, the cycles $A$ and $B$ are independent — neither is a boundary, and no integer combination $rA + sB$ is a boundary unless $r = s = 0$.

---

# Solution

The proof breaks into four steps. Step 1 sets up the triangulation and the $2$-chain $[T^2]$. Step 2 computes $\partial[T^2] = 0$, certifying orientability and giving $H_2(T^2; \mathbb{Z}) = \mathbb{Z}$. Step 3 computes $H_0 = \mathbb{Z}$ (connectedness) and $H_1 = \mathbb{Z}^2$ (generated by the loops $A$ and $B$). Step 4 computes $\chi(T^2) = 0$.

**Step 1: Triangulate $T^2$ and form the fundamental chain.**

Following Frankel Figure 13.12, triangulate the unit square (representing $T^2$ via boundary identifications) into $18$ triangles. The triangulation uses vertices $Q_0, Q_1, \dots, Q_8$ where $Q_0$ sits at the four corners (all identified), $Q_1, \dots, Q_4$ at boundary midpoints, $Q_5, \dots, Q_8$ at interior points. Each triangle is a singular $2$-simplex $\tau_i : \Delta^2 \to T^2$, oriented so that adjacent triangles induce opposite orientations on their common edges.

The **fundamental chain** is
$$
[T^2] \;=\; \sum_{i=1}^{18} \tau_i \;\in\; C_2(T^2; \mathbb{Z}).
$$

> [!note]- Derivation
> The triangulation is explicit in Frankel: the unit square $[0, 1] \times [0, 1]$ is divided into a $3 \times 3$ grid of unit-squares (each of side length $1/3$), and each unit-square is split by a diagonal into two triangles. This gives $9 \times 2 = 18$ triangles.
>
> Edge identifications: the left edge $\{0\} \times [0, 1]$ is identified with the right edge $\{1\} \times [0, 1]$ (call this loop $A$); the bottom edge $[0, 1] \times \{0\}$ with the top edge $[0, 1] \times \{1\}$ (call this loop $B$). The four corners are identified to the single vertex $Q_0$.
>
> Vertex labelling: $Q_0$ at the corners; $Q_1, Q_4$ on the top/bottom edges between corners; $Q_2, Q_3$ on the left/right edges (which equal each other after identification, so $Q_2$ and $Q_3$ each become a single vertex on the torus); $Q_5, \dots, Q_8$ in the interior.
>
> Orient each triangle counterclockwise (in the standard $(x, y)$ orientation of the plane). Adjacent triangles within the rectangle share an internal edge; the orientations induce opposite signs on this shared edge (one triangle calls it $(a, b)$, the other calls it $-(a, b)$).
>
> The fundamental chain $[T^2] = \tau_1 + \tau_2 + \cdots + \tau_{18}$ sums all $18$ triangles with their orientation-consistent signs.

**Step 2: Compute $\partial[T^2] = 0$.**

Compute the boundary $\partial[T^2] = \sum_i \partial \tau_i$. The boundary of each $\tau_i$ is the alternating sum of its three edges. When we sum over all $18$ triangles, two cancellation patterns occur:

(i) **Interior edges cancel.** Each interior edge of the triangulation is shared by two adjacent triangles. By the orientation-consistent labelling, the two triangles assign opposite signs to this shared edge, so it cancels in the total.

(ii) **Boundary edges cancel via identifications.** The boundary of the rectangle consists of four edges: top, bottom, left, right. The top edge is identified with the bottom (both are copies of loop $B$); the left edge is identified with the right (both copies of $A$). The boundary contribution of $\sum \tau_i$ on each rectangle-edge gives a copy of the loop ($A$ or $B$, traversed in some direction). The identifications force the top edge's contribution and the bottom edge's contribution to cancel (one is $+B$, the other is $-B$, because the orientations on the identified edges are reversed relative to the rectangle). Similarly $+A - A = 0$.

So $\partial[T^2] = (\text{interior cancellations} = 0) + (A + B - A - B) = 0$. Hence $[T^2]$ is a $2$-cycle, $T^2$ is orientable, and $H_2(T^2; \mathbb{Z}) = \mathbb{Z}$ generated by $[T^2]$.

> [!note]- Derivation
> See Frankel Equation 13.24 for the explicit identification $\partial[T^2] = A + B - A - B = 0$.
>
> For the interior cancellation: take any interior edge $(Q_i, Q_j)$ of the triangulation. It is a face of exactly two adjacent triangles, $\tau_a$ and $\tau_b$. In $\partial \tau_a$, this edge appears with some sign $\pm 1$ (depending on its position as the $0$-th, $1$st, or $2$nd face of $\tau_a$). In $\partial \tau_b$, the same edge appears with the opposite sign (because the orientations of $\tau_a$ and $\tau_b$ are chosen so that the edge is traversed in opposite directions). When we sum $\partial \tau_a + \partial \tau_b$, the interior-edge contributions cancel.
>
> For the boundary-edge identification: the right side of the rectangle is identified with the left side via the map $(1, y) \sim (0, y)$. So the boundary edge on the right of the rectangle becomes the *same* loop $A$ on the torus as the left edge. But the orientations: as we traverse the rectangle counterclockwise, the right edge is traversed *downward* (from $(1, 1)$ to $(1, 0)$) while the left edge is traversed *upward*. In terms of the loop $A$ on the torus, these are opposite directions: right = $-A$, left = $+A$ (or vice versa, depending on sign conventions). So the contributions to $\partial \sum \tau_i$ from the right and left edges sum to $A - A = 0$.
>
> Similarly $B - B = 0$ from the top and bottom edges.
>
> Combining: $\partial[T^2] = 0 + 0 + 0 = 0$. Since $[T^2]$ is a non-trivial chain (sum of $18$ distinct simplices) that is a cycle, the $2$-cycle group $Z_2(T^2; \mathbb{Z}) \neq 0$. There are no $3$-chains in a $2$-dimensional complex, so $B_2 = 0$. Hence $H_2(T^2; \mathbb{Z}) = Z_2 / B_2 = \mathbb{Z}$ generated by $[T^2]$.

**Step 3: Compute $H_0 = \mathbb{Z}$ and $H_1 = \mathbb{Z}^2$.**

*$H_0$:* $T^2$ is path-connected (the unit square is, and the quotient by the identifications preserves connectedness). So $H_0(T^2; \mathbb{Z}) = \mathbb{Z}$, generated by any single vertex.

*$H_1$:* The loops $A$ (around the $x$-direction) and $B$ (around the $y$-direction) are $1$-cycles: $\partial A = Q_0 - Q_0 = 0$ (the loop starts and ends at $Q_0$ after going around); $\partial B = 0$ similarly. They generate $H_1$, as follows.

*Generators:* Any $1$-cycle on $T^2$ can be deformed (using interior boundaries) to a $1$-cycle supported on the boundary of the rectangle. After identifications, the boundary $1$-cycles are spanned by $A$ and $B$.

*Independence:* No integer combination $rA + sB$ is a boundary unless $r = s = 0$. Reason: a $2$-chain with boundary $rA + sB$ would have to be a multiple of $[T^2]$ (the only non-trivial $2$-cycle, up to scalar). But $\partial[T^2] = 0$, so any multiple has zero boundary, ruling out $rA + sB \neq 0$ being a boundary.

Hence $H_1(T^2; \mathbb{Z}) = \mathbb{Z} A \oplus \mathbb{Z} B = \mathbb{Z}^2$.

> [!note]- Derivation
> *$H_0$:* The path components of $T^2$ are determined by the underlying space, which is connected (it is the continuous image of the connected square under the quotient). One can construct a path between any two vertices $Q_i, Q_j$ via the simplicial $1$-cycles in the triangulation. So $H_0(T^2; \mathbb{Z}) = \mathbb{Z}$.
>
> *$H_1$:* The loops $A, B$ are simplicial $1$-cycles by construction — each starts and ends at $Q_0$ (after going around the torus once via the identifications), so $\partial A = Q_0 - Q_0 = 0$ and $\partial B = 0$.
>
> To see they generate $H_1$: any $1$-cycle $c$ in $T^2$ can be written as a combination of edges. By adding boundaries of triangles (i.e. modifying $c$ in its homology class), we can deform $c$ to lie on the rectangle's boundary. The rectangle's boundary, after identifications, consists of copies of $A$ and $B$. So $[c] \in \mathbb{Z}\{A\} + \mathbb{Z}\{B\}$.
>
> To see they are independent: suppose $rA + sB = \partial w$ for some $2$-chain $w$. The $2$-chain $w$ is a sum $\sum n_i \tau_i$ of triangles. $\partial w = \sum n_i \partial \tau_i$. For this to equal $rA + sB$, the interior edges must cancel — which they do exactly when all $n_i$ are equal: $w = n \sum_i \tau_i = n [T^2]$. But $\partial(n [T^2]) = n \cdot 0 = 0$, not $rA + sB$ (unless $r = s = 0$). So $H_1(T^2; \mathbb{Z}) = \mathbb{Z}\{A\} \oplus \mathbb{Z}\{B\} = \mathbb{Z}^2$.

**Step 4: Compute $\chi(T^2) = 0$.**

$\chi(T^2) = \sum_p (-1)^p b_p = 1 - 2 + 1 = 0$. Equivalently from the triangulation: $V - E + F$, where $V = $ number of vertices, $E = $ edges, $F = $ faces in the triangulation, after accounting for identifications. The Frankel triangulation has after-identification counts $V = 9$ (the vertices $Q_0, \dots, Q_8$, with $Q_0$ a single vertex), $E = 27$ (each interior + boundary edge counted once), $F = 18$. Compute $9 - 27 + 18 = 0$. ✓

> [!note]- Derivation
> *From homology:* $b_0 = \dim H_0(T^2; \mathbb{R}) = 1$, $b_1 = \dim H_1(T^2; \mathbb{R}) = 2$, $b_2 = \dim H_2(T^2; \mathbb{R}) = 1$. Alternating sum: $1 - 2 + 1 = 0$.
>
> *From triangulation:* Count vertices, edges, faces of the triangulation after identifications:
> - Vertices: $Q_0, Q_1, Q_2, Q_3, Q_4$ on the boundary + $Q_5, Q_6, Q_7, Q_8$ in the interior = $9$.
> - Edges: each unit-square has $5$ edges ($2$ horizontal, $2$ vertical, $1$ diagonal); there are $9$ unit-squares; but interior edges of the rectangle are shared by two unit-squares, so we don't double-count. Total after identifications: $27$ (this can be verified by direct counting). 
> - Faces (triangles): $18$.
>
> Euler characteristic: $9 - 27 + 18 = 0$. ✓
>
> Both routes give $\chi(T^2) = 0$, consistent with [[Thm - Euler Characteristic via Alternating Betti Numbers|the alternating-Betti-number identity]].

> [!note]- Complete formal solution
> **Theorem.** $H_0(T^2; \mathbb{Z}) = \mathbb{Z}$, $H_1(T^2; \mathbb{Z}) = \mathbb{Z}^2$, $H_2(T^2; \mathbb{Z}) = \mathbb{Z}$. Euler characteristic $\chi(T^2) = 0$.
>
> *Proof.* Triangulate $T^2$ into $18$ oriented triangles (Frankel Figure 13.12), with the $18$ triangles glued along edges in a way respecting the boundary identifications $(0, y) \sim (1, y)$ and $(x, 0) \sim (x, 1)$. Let $[T^2] = \sum_{i=1}^{18} \tau_i$ be the fundamental $2$-chain.
>
> *Compute $\partial[T^2] = 0$.* Interior edges of the triangulation appear with opposite signs in the boundaries of the two triangles sharing them, so they cancel. Boundary edges contribute $A + B - A - B = 0$ via the identifications (right edge = $-$ left edge, top edge = $-$ bottom edge in the boundary contribution). So $\partial[T^2] = 0$.
>
> *$H_2(T^2) = \mathbb{Z}$:* $Z_2 = \mathbb{Z} \cdot [T^2]$ (any $2$-cycle must have all triangles with equal coefficient by edge-cancellation, hence proportional to $[T^2]$). $B_2 = 0$ (no $3$-chains in a $2$-dimensional complex). $H_2 = Z_2 / B_2 = \mathbb{Z}$.
>
> *$H_1(T^2) = \mathbb{Z}^2$:* The loops $A$ and $B$ (boundary edges of the rectangle, going once around in each direction after identification) are $1$-cycles. They generate $H_1$ because any $1$-cycle deformation-retracts to the rectangle boundary, and they are independent because no non-trivial combination is a boundary (the only $2$-cycle is $[T^2]$, with zero boundary). So $H_1 = \mathbb{Z} A \oplus \mathbb{Z} B = \mathbb{Z}^2$.
>
> *$H_0(T^2) = \mathbb{Z}$:* $T^2$ is path-connected.
>
> *Euler characteristic:* $\chi(T^2) = 1 - 2 + 1 = 0$. Cross-check with $V - E + F = 9 - 27 + 18 = 0$. $\qquad\blacksquare$

---

# Key Takeaways

**The boundary $\partial[\text{triangulated manifold}]$ vanishes for orientable closed manifolds.** This is the key calculation: for an orientable closed $n$-manifold $M$ with a triangulation respecting orientation, the fundamental chain $[M] = \sum \tau_i$ has $\partial[M] = 0$, certifying that $M$ is orientable and providing the generator of $H_n(M; \mathbb{Z}) = \mathbb{Z}$. The vanishing comes from two cancellations: interior edges shared by two triangles cancel by orientation consistency; boundary edges of the polygon presentation cancel by the identification pattern (each identified pair contributes $+$ and $-$ orientations). For a non-orientable manifold (like the Klein bottle), one of these cancellations fails — the Klein bottle has $\partial[K^2] = 2B \neq 0$ — and the manifold has $H_n = 0$ with $\mathbb{Z}$ coefficients (but $\mathbb{Z}/2$ coefficients restore the cycle). This is the same pattern that distinguishes orientable from non-orientable surfaces in general.

**The two basis cycles $A, B \in H_1(T^2)$ are the "horizontal" and "vertical" generators, corresponding to the two factors of $T^2 = S^1 \times S^1$.** Each is a $1$-cycle wrapping once around the torus in one direction, and they are independent in $H_1$. This matches the Künneth formula: $H_1(T^2; \mathbb{Z}) = H_1(S^1) \otimes H_0(S^1) \oplus H_0(S^1) \otimes H_1(S^1) = \mathbb{Z}^2$, with the two generators being "loop in first factor" and "loop in second factor." The pattern extends to $T^n$: $H_k(T^n; \mathbb{Z}) = \mathbb{Z}^{\binom{n}{k}}$, with generators indexed by $k$-element subsets of the $n$ directions. The Betti polynomial $P_{T^n}(t) = (1 + t)^n$ is the algebraic shadow of this Künneth product structure.

**De Rham cohomology of the torus matches the singular homology via wedge products.** $H^k_{dR}(T^n) = \bigwedge^k \langle d\theta^1, \dots, d\theta^n \rangle$ (the exterior algebra on the $n$ angular forms), with $\dim H^k_{dR}(T^n) = \binom{n}{k}$. By the [[Thm - The de Rham Theorem (Full Proof)|de Rham theorem]], this matches $\dim H_k(T^n; \mathbb{R})$. The integration pairing: $\int_A d\theta^1 = 2\pi$ and $\int_B d\theta^2 = 2\pi$ (with all other pairings zero), confirming that $d\theta^1/2\pi$ and $d\theta^2/2\pi$ are the cohomology generators dual to the homology generators $A$ and $B$. This is the simplest non-trivial example of the de Rham pairing: see [[Ex - The de Rham Pairing for H^1 of S^1]] for the building block.

**Euler characteristic $\chi(T^2) = 0$ has multiple interpretations.** It's the alternating sum of Betti numbers ($1 - 2 + 1 = 0$); it's the alternating cell count of the triangulation ($9 - 27 + 18 = 0$); it's the topological invariant that vanishes for closed odd-dimensional manifolds *and* for any product of even-dimensional spheres of opposite-parity dimensions; and by Gauss–Bonnet it's the curvature integral on a Riemannian torus. The vanishing reflects a deep symmetry: a closed orientable surface has $\chi = 2 - 2g$, and $\chi = 0$ forces $g = 1$, the topological characterisation of a torus. In higher dimensions, $\chi(T^n) = 0$ for all $n \geq 1$ by the Künneth product: $\chi(T^n) = \chi(S^1)^n = 0^n = 0$, the simplest non-trivial consequence of multiplicativity of $\chi$.
