---
type: definition
subject: algebraic-topology
prereqs:
  - "Def - Singular Simplex"
  - "Def - Singular Chain"
tags: [geometry, algebraic-topology, boundary]
---

# Notation

$M$ is a topological space, $G$ an abelian coefficient group. $\sigma : \Delta^p \to M$ is a [[Def - Singular Simplex|singular $p$-simplex]] in $M$, and $c \in C_p(M; G)$ is a [[Def - Singular Chain|singular $p$-chain]]. The face maps $f_k : \Delta^{p-1} \to \Delta^p$ of the standard simplex are as in [[Def - The Standard p-Simplex]] — the unique affine embeddings sending $P_j \mapsto P_j$ for $j < k$ and $P_j \mapsto P_{j+1}$ for $j \geq k$.

The boundary operator is denoted $\partial$, or $\partial_p$ when the degree needs to be tracked: $\partial_p : C_p(M; G) \to C_{p-1}(M; G)$.

The widehat $\widehat{P_k}$ in a tuple means "omit $P_k$": $(P_0, \dots, \widehat{P_k}, \dots, P_p) = (P_0, \dots, P_{k-1}, P_{k+1}, \dots, P_p)$ — the standard $(p-1)$-simplex obtained by deleting the $k$-th vertex.

---

# Axiom Motivation

The boundary operator is the heart of the singular chain complex. We want a map $\partial : C_p \to C_{p-1}$ that captures the geometric idea "the boundary of a $p$-dimensional region is its $(p-1)$-dimensional edge," and that satisfies $\partial^2 = 0$ (the boundary of a boundary is zero). These two requirements pin down the definition up to overall normalisation.

**Why a sum of all $p+1$ faces?** A $p$-simplex has $p+1$ codimension-one faces, and the boundary should account for all of them — leaving out any face would mean the formal boundary doesn't match the geometric boundary. So the boundary $\partial \Delta^p$ must be some combination of all the faces $\Delta^{p-1}_{(k)}$ for $k = 0, 1, \dots, p$. The question is: with what coefficients?

**Why alternating signs $(-1)^k$?** If all coefficients were $+1$, the boundary of a triangle would be the *sum* of its three edges — but geometrically the boundary of an oriented triangle traverses the edges with consistent orientation, which when one of them is reversed contributes a $-1$. The alternating signs $(-1)^k$ are precisely the bookkeeping that makes the boundary respect orientation.

To see this concretely, consider the boundary of $\Delta^2 = (P_0, P_1, P_2)$, an oriented triangle. Geometrically, the boundary is the loop $P_0 \to P_1 \to P_2 \to P_0$, which traverses three edges. As singular $1$-simplices, these edges are $(P_0, P_1)$, $(P_1, P_2)$, $(P_2, P_0)$. But our notation requires us to write each simplex with vertices in standard order — $(P_0, P_1)$, $(P_1, P_2)$, $(P_0, P_2)$ — and the third edge $(P_2, P_0)$ is then $-(P_0, P_2)$ (the negative is the orientation flip). So the geometric boundary becomes
$$
\partial(P_0, P_1, P_2) = (P_1, P_2) - (P_0, P_2) + (P_0, P_1) = \sum_{k=0}^2 (-1)^k (P_0, \dots, \widehat{P_k}, \dots, P_2).
$$
The alternating signs are not an arbitrary convention; they are forced by the requirement that the chain-boundary equal the geometric boundary on this elementary example. The pattern extrapolates to all dimensions.

**Why does $\partial^2 = 0$ hold?** The boundary of a boundary should be zero because, intuitively, "the boundary of a closed region has no boundary." Algebraically, $\partial \partial \sigma$ expands as a double sum over face-of-face terms, and the cancellation comes from a precise combinatorial identity: for $j < k$, the $j$-th face of the $k$-th face of $\Delta^p$ equals the $(k-1)$-th face of the $j$-th face. The signs $(-1)^j (-1)^k$ and $(-1)^{k-1} (-1)^j$ are negatives of each other, so the two double-sum terms cancel. The full proof is in [[Thm - d-Squared-is-Zero for Singular Boundaries]].

If we had chosen *constant* signs $(+1)$ instead of alternating, $\partial^2$ would not vanish: the boundary of $(P_1, P_2) + (P_0, P_2) + (P_0, P_1)$ is $(P_2 - P_1) + (P_2 - P_0) + (P_1 - P_0) = -2P_0 + 2P_2 \neq 0$. So the alternating signs are *forced* by the requirement $\partial^2 = 0$ — there is no other choice (up to overall sign) that achieves it.

**Why extend $G$-linearly?** The boundary on a single simplex gives an integer chain. To make $\partial$ defined on chains with coefficients in an arbitrary abelian group $G$ (not just $\mathbb{Z}$), we extend by $G$-linearity:
$$
\partial \left( \sum_i g_i \sigma_i \right) \;=\; \sum_i g_i \cdot \partial \sigma_i.
$$
This uses the action of $\mathbb{Z}$ on $G$ (every abelian group is a $\mathbb{Z}$-module): the integer signs in $\partial \sigma_i = \sum_k (-1)^k (\sigma_i \circ f_k)$ act on the coefficient $g_i \in G$ via $\pm g_i$. The extension is automatic from the universal property of the free $G$-module.

The boundary operator is the unique morphism $C_p \to C_{p-1}$ that (i) is $G$-linear, (ii) on a singular simplex equals the alternating sum of its faces. The two demands together force the definition, and the cancellation $\partial^2 = 0$ is then a (combinatorial) consequence rather than an additional axiom.

---

# The Definition

Let $M$ be a topological space and $G$ an abelian group. For $p \geq 1$, the **boundary operator** $\partial : C_p(M; G) \to C_{p-1}(M; G)$ is defined as follows.

On a single singular $p$-simplex $\sigma : \Delta^p \to M$,
$$
\partial \sigma \;=\; \sum_{k=0}^{p} (-1)^k\, (\sigma \circ f_k) \;\in\; C_{p-1}(M; G),
$$
where $f_k : \Delta^{p-1} \to \Delta^p$ is the $k$-th [[Def - The Standard p-Simplex|face map]] of the standard simplex. The composition $\sigma \circ f_k : \Delta^{p-1} \to M$ is the $k$-th face of $\sigma$, a singular $(p-1)$-simplex.

Extended $G$-linearly to all chains: for $c = \sum_i g_i \sigma_i \in C_p(M; G)$,
$$
\partial c \;=\; \sum_i g_i\, \partial \sigma_i \;=\; \sum_i g_i \sum_{k=0}^{p} (-1)^k (\sigma_i \circ f_k).
$$

For $p = 0$, the boundary is the zero map: $\partial : C_0(M; G) \to C_{-1}(M; G) = 0$, so $\partial \sigma = 0$ for every $0$-simplex $\sigma$. (Every point is a $0$-cycle.) Some treatments augment the chain complex with $C_{-1} = G$ and an "augmentation" map $\partial : C_0 \to G$ summing coefficients; this gives [[Def - Augmentation and Reduced Homology|reduced homology]] but is otherwise inessential.

The key algebraic property — proved in [[Thm - d-Squared-is-Zero for Singular Boundaries]] — is
$$
\partial \circ \partial = 0 : C_p(M; G) \to C_{p-2}(M; G).
$$

The boundary operator is **natural** with respect to continuous maps: for $f : M \to N$ continuous, the induced chain map $f_\# : C_p(M; G) \to C_p(N; G)$ satisfies $\partial \circ f_\# = f_\# \circ \partial$. Equivalently, the diagram
$$
\begin{array}{ccc}
C_p(M; G) & \xrightarrow{f_\#} & C_p(N; G) \\
\partial \downarrow & & \partial \downarrow \\
C_{p-1}(M; G) & \xrightarrow{f_\#} & C_{p-1}(N; G)
\end{array}
$$
commutes.

---

# Relate to Other Fields / Compression

The boundary operator is the **singular analogue of the exterior derivative $d$**. The parallel is exact: $d : \Omega^k \to \Omega^{k+1}$ raises degree by one and squares to zero ($d^2 = 0$); $\partial : C_p \to C_{p-1}$ lowers degree by one and squares to zero ($\partial^2 = 0$). The chain complex $(C_\bullet, \partial)$ is a *homology* complex (lowering degree); the de Rham complex $(\Omega^\bullet, d)$ is a *cohomology* complex (raising degree). Dualising the chain complex via $\mathrm{Hom}(-, G)$ gives the singular cochain complex with coboundary $\delta$, which raises degree like $d$ and is the direct algebraic analogue of $d$.

The "boundary of a boundary is zero" is the homological version of the statement that the boundary of any compact manifold with boundary itself has no boundary: $\partial(\partial M) = 0$ when $\partial M$ is interpreted as a topological boundary. This is not a coincidence — for an oriented compact manifold with boundary, the chain $[M]$ has $\partial[M] = [\partial M]$, and $\partial([\partial M]) = 0$ because $\partial M$ is a closed manifold (no boundary).

**True name:** $\partial$ is the **alternating sum of faces** — the unique $\mathbb{Z}$-linear extension of "alternate-signed sum of codimension-one faces" from individual simplices to all chains. The alternating signs are the orientation bookkeeping; the linearity is the embedding of geometry into algebra.

---

# Examples / Corollaries

**Boundary of a $0$-simplex:** $\partial \sigma_0 = 0$ for every singular $0$-simplex $\sigma_0$ — a point has no boundary. (Indeed, $C_{-1} = 0$, so the boundary map starting from $C_0$ is forced to be zero.)

**Boundary of a $1$-simplex (a path):** For a continuous path $\sigma : \Delta^1 = [0, 1] \to M$ with $\sigma(0) = p$ and $\sigma(1) = q$,
$$
\partial \sigma = (-1)^0 (\sigma \circ f_0) + (-1)^1 (\sigma \circ f_1) = q - p,
$$
where $f_0 : \Delta^0 \to \Delta^1$ sends the single point to $P_1 = 1 \in \Delta^1$ (so $\sigma \circ f_0 = q$) and $f_1$ sends it to $P_0 = 0$ (so $\sigma \circ f_1 = p$). Wait — the convention is that $f_k$ omits the $k$-th vertex, so $f_0$ has image the face *opposite* $P_0$, which contains $P_1$. So $f_0$ sends $P_0$ (the single vertex of $\Delta^0$) to $P_1$ of $\Delta^1$, hence $\sigma \circ f_0 = \sigma(P_1) = q$. Similarly $f_1$ sends $P_0$ of $\Delta^0$ to $P_0$ of $\Delta^1$, giving $\sigma \circ f_1 = p$. So
$$
\partial \sigma = q - p,
$$
matching the geometric expectation: the boundary of a path is its endpoint minus its starting point.

**Boundary of a $2$-simplex (a triangle):** For the identity $\sigma = (P_0, P_1, P_2) : \Delta^2 \to \Delta^2$,
$$
\partial(P_0, P_1, P_2) = (P_1, P_2) - (P_0, P_2) + (P_0, P_1),
$$
the alternating sum of the three edges of the triangle (with the third edge appearing with a $-$ sign to match the orientation reversal).

**Boundary of a $3$-simplex (a tetrahedron):** For the identity $\sigma = (P_0, P_1, P_2, P_3) : \Delta^3 \to \Delta^3$,
$$
\partial(P_0, P_1, P_2, P_3) = (P_1, P_2, P_3) - (P_0, P_2, P_3) + (P_0, P_1, P_3) - (P_0, P_1, P_2),
$$
the alternating sum of the four triangular faces of the tetrahedron.

**Boundary of a constant simplex:** For a constant singular $p$-simplex $\sigma_p : \Delta^p \to \{q\}$, every face $\sigma_p \circ f_k$ is again the constant map to $q$, namely $\sigma_{p-1}$. So $\partial \sigma_p = \sum_{k=0}^p (-1)^k \sigma_{p-1} = (\sum_{k=0}^p (-1)^k) \sigma_{p-1}$. The alternating sum $\sum_{k=0}^p (-1)^k$ equals $1$ if $p$ is even and $0$ if $p$ is odd. So:
$$
\partial \sigma_p = \begin{cases} \sigma_{p-1} & \text{if } p \text{ is even} \\ 0 & \text{if } p \text{ is odd}. \end{cases}
$$
Consequence: in the chain complex of a point, every odd-degree boundary map is zero and every even-degree boundary map (for $p \geq 2$) is the identity. The homology is $\mathbb{Z}$ in degree zero and zero elsewhere — as expected.

**Boundary of a $2$-chain (the torus):** For the standard triangulation of $T^2$ into eighteen oriented triangles, the chain $[T^2] = \sum_{i=1}^{18} \tau_i$ has boundary
$$
\partial[T^2] = A + B - A - B = 0,
$$
where $A$ and $B$ are the two generating $1$-cycles (the "$a$-loop" and "$b$-loop" of the torus). The interior edges of the triangulation cancel in pairs because each interior edge is shared by two triangles with opposite induced orientations; only the boundary loops $A$ and $B$ survive, and they appear twice each with opposite signs, summing to zero. The torus is therefore a $2$-cycle.

**Boundary of the Möbius band:** For the analogous triangulation of the Möbius band (Frankel Figure 13.7), $[Mö] = \sum \tau_i$ has boundary
$$
\partial[Mö] = B + C + 2A,
$$
where $B + C$ is the topological edge of the band and $A$ is the seam, traversed twice with the same orientation. This non-zero boundary (with $\mathbb{Z}$ coefficients) reflects the non-orientability of the Möbius band — the orientation bookkeeping fails because no consistent orientation on all simplices is possible. With $\mathbb{Z}/2$ coefficients, $2A = 0$ and $[Mö]$ becomes a non-trivial cycle.

**Corollary ($\partial$ is $G$-linear).** $\partial(g \cdot \sigma) = g \cdot \partial(\sigma)$ for $g \in G$, by the extension formula. This makes $\partial$ a homomorphism of abelian groups (or a $G$-module map).

**Corollary (naturality).** For $f : M \to N$ continuous and any $\sigma \in C_p(M; G)$, $\partial(f_\# \sigma) = f_\#(\partial \sigma)$. This is because the boundary uses face maps of the *standard simplex* (intrinsic to $\Delta^p$, not depending on $M$ or $N$), and $f$ post-composes after these face maps: $(f \circ \sigma) \circ f_k = f \circ (\sigma \circ f_k)$.

**Corollary (boundary of a sum).** $\partial(c_1 + c_2) = \partial c_1 + \partial c_2$, by $G$-linearity. This makes $\partial$ a homomorphism of chain groups.

**Calibration check.** If you have understood the definition you should be able to: (1) compute $\partial \partial (P_0, P_1, P_2, P_3) = 0$ by expanding and cancelling face-of-face terms; (2) verify that the boundary of the triangulated $2$-sphere (two oriented triangles glued along their common edges) is zero, certifying $S^2$ as a $2$-cycle; (3) explain why a constant $p$-simplex has non-zero boundary for even $p$ but zero for odd $p$.

---

# Unlocked by This

> [!tip] The Singular Chain Complex *(from Algebraic Topology — this same topic)*
> Together with $\partial^2 = 0$ ([[Thm - d-Squared-is-Zero for Singular Boundaries]]), the chain groups $C_\bullet$ and boundary maps $\partial$ form a **chain complex**: a sequence of abelian groups and homomorphisms with composition zero. The homology of this chain complex is the singular homology — see [[Def - Singular Homology]].

> [!tip] Singular Cohomology *(from Algebraic Topology — this same topic)*
> Dualising via $\mathrm{Hom}(-, G)$ converts the boundary operator $\partial : C_p \to C_{p-1}$ into the **coboundary operator** $\delta : C^{p-1} \to C^p$ raising degree by one. The resulting singular cochain complex has its own cohomology, which is singular cohomology $H^p(M; G)$ — see [[Def - Singular Cohomology]]. The coboundary $\delta$ is the direct algebraic analogue of the exterior derivative $d$.

> [!tip] The de Rham Pairing via Stokes' Theorem *(from Differential Geometry / Algebraic Topology)*
> Stokes's theorem $\int_{\partial c} \omega = \int_c d\omega$ identifies the boundary operator $\partial$ on chains with the exterior derivative $d$ on forms, via integration. This is the *single* identity that makes the de Rham pairing $\langle [\omega], [c] \rangle = \int_c \omega$ well-defined on cohomology classes — see [[Thm - The de Rham Theorem (Full Proof)]].

> [!tip] **Differential Graded Algebras and Stokes' Theorem in General Categories** *(from Homological Algebra)*
> The pattern "linear operator $\partial$ on graded objects with $\partial^2 = 0$" is the defining feature of a **differential graded module** or **chain complex**. Every cohomology theory in mathematics — singular, de Rham, sheaf, group cohomology, Lie algebra cohomology, Hochschild cohomology — is built by writing down a chain complex with $\partial^2 = 0$ (or $d^2 = 0$) and taking $\ker / \mathrm{im}$. The singular boundary operator is the prototype.
