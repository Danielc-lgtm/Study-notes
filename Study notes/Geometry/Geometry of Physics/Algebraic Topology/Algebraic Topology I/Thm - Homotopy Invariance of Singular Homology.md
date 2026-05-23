---
type: theorem
subject: algebraic-topology
prereqs:
  - "Def - Singular Homology"
  - "Def - Chain Map and Chain Homotopy"
tags: [geometry, algebraic-topology, homotopy]
---

# Notation

$M, N$ are topological spaces; $f, g : M \to N$ are continuous maps; $H : M \times [0,1] \to N$ is a continuous homotopy from $f$ to $g$ (meaning $H(\cdot, 0) = f$, $H(\cdot, 1) = g$). $C_p$, $\partial$, $H_p$, $f_*$ are as in [[Def - Singular Homology]] and [[Def - Chain Map and Chain Homotopy]].

The cylinder $\Delta^p \times [0,1]$ has dimension $p + 1$, and we will triangulate it into $(p+1)$-simplices to build the prism operator.

---

# Statement

> **Theorem (Homotopy Invariance of Singular Homology).** Let $f, g : M \to N$ be continuous maps that are **homotopic** — there exists a continuous $H : M \times [0,1] \to N$ with $H|_{t=0} = f$ and $H|_{t=1} = g$. Then for every abelian group $G$ and every $p \geq 0$, the induced maps on singular homology are equal:
> $$
> f_* = g_* : H_p(M; G) \to H_p(N; G).
> $$

> **Corollary (Homology is a homotopy invariant).** If $M$ and $N$ are **homotopy equivalent** — there exist continuous maps $f : M \to N$ and $g : N \to M$ with $g \circ f \simeq \mathrm{id}_M$ and $f \circ g \simeq \mathrm{id}_N$ — then $H_p(M; G) \cong H_p(N; G)$ for every $p$ and every $G$. In particular, contractible spaces have $H_0 = G$ and $H_p = 0$ for $p \geq 1$.

The proof constructs an explicit chain homotopy $h : C_p(M) \to C_{p+1}(N)$ such that $g_\# - f_\# = \partial h + h \partial$ at the chain level, by triangulating the prism $\Delta^p \times [0,1]$.

---

# Motivation

Homology is supposed to be a homotopy invariant — that is, it should depend only on the homotopy type of the space, not on the finer-grained topology. Homotopy equivalent spaces look "the same up to continuous deformation," so any topologically meaningful invariant should be the same for both. Singular homology is built from continuous simplices, which can be continuously deformed; so morally, the homology classes should also be invariant under such deformations.

This theorem makes the moral precise: homotopic maps induce the same map on homology. The consequences are immediate and powerful. A contractible space has the homology of a point: $\mathbb{R}^n$, the open ball, the upper half-plane, any star-shaped region — all have $H_0 = G$ and $H_p = 0$ for $p \geq 1$. The Möbius band has the homology of $S^1$ (it deformation-retracts onto its core circle). The cylinder $S^1 \times [0,1]$ has the homology of $S^1$. Any tubular neighborhood of a submanifold has the homology of the submanifold itself.

Homotopy invariance is the second-most-important property of singular homology (after $\partial^2 = 0$). It is what justifies the rule of thumb "compute the homotopy type first, then compute the homology" — the homotopy type fixes the homology completely. It is also the key input to many proofs: most computations of $H_*(M)$ proceed by replacing $M$ with a homotopy-equivalent simpler space (usually a CW complex or a sphere).

The proof has a beautiful geometric structure. Two homotopic maps $f, g : M \to N$ are connected by a continuous "$1$-parameter family of maps" $H : M \times [0,1] \to N$. For each singular $p$-simplex $\sigma : \Delta^p \to M$, the homotopy gives a map $H \circ (\sigma \times \mathrm{id}) : \Delta^p \times [0,1] \to N$ from a $(p+1)$-dimensional prism into $N$. The boundary of this prism consists of three pieces: the top $\Delta^p \times \{1\}$ (which gives $g \circ \sigma$), the bottom $\Delta^p \times \{0\}$ (which gives $f \circ \sigma$, with the boundary orientation forcing a minus sign), and the sides $(\partial \Delta^p) \times [0,1]$ (which give the prism of the boundary $\partial \sigma$).

Triangulating the prism $\Delta^p \times [0,1]$ into $(p+1)$-simplices gives a chain-level formula $g_\# - f_\# = \partial h + h \partial$, where $h$ sends each simplex to the sum of the prism's triangulation simplices (with appropriate signs). This is the **prism operator** — the chain homotopy from $f_\#$ to $g_\#$. By [[Def - Chain Map and Chain Homotopy|chain homotopy]], chain-homotopic chain maps induce equal homology maps, so $f_* = g_*$.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition $A$ is: *$f$ and $g$ are homotopic continuous maps $M \to N$.*

The first disguised source is **a deformation retract**. Property $B$: $M$ admits a deformation retraction onto a subspace $A \subseteq M$ — a continuous family $r_t : M \to M$ with $r_0 = \mathrm{id}_M$, $r_1(M) \subseteq A$, and $r_t|_A = \mathrm{id}_A$. The bridge: the inclusion $i : A \hookrightarrow M$ and the retraction $r = r_1 : M \to A$ satisfy $r \circ i = \mathrm{id}_A$ and $i \circ r \simeq \mathrm{id}_M$ (the homotopy is $r_t$). So $A$ is a strong deformation retract of $M$, which forces $M \simeq A$ in homotopy. *Example application:* the Möbius band deformation-retracts onto its core circle, so $H_*(\text{Möbius}) = H_*(S^1)$. $\mathbb{R}^n \setminus \{0\}$ deformation-retracts onto $S^{n-1}$, so $H_*(\mathbb{R}^n \setminus \{0\}) = H_*(S^{n-1})$.

The second disguised source is **a tubular neighborhood**. Property $B$: a submanifold $A \subseteq M$ has a tubular neighborhood $U$ (an open set diffeomorphic to the normal bundle of $A$ in $M$). The bridge: $U$ deformation-retracts onto $A$ (push every point along the linear path in its normal fiber back to its base point), so $H_*(U) = H_*(A)$. *Example application:* the cohomology of any small open neighborhood of an embedded submanifold equals the cohomology of the submanifold itself — used constantly in Mayer–Vietoris arguments to "thicken" pieces of a cover.

The third disguised source is **a contractible space**. Property $B$: $M$ is contractible — the identity $\mathrm{id}_M$ is homotopic to a constant map. The bridge: by the theorem, $(\mathrm{id}_M)_* = (\text{const})_*$ on homology, but $\mathrm{const}_* = 0$ except in degree zero. So $H_p(M) = 0$ for $p \geq 1$, and $M$ has the homology of a point. *Example application:* $\mathbb{R}^n$, any star-shaped region, any cone over a space — all contractible, all with trivial homology in positive degrees.

The fourth disguised source is **a smooth homotopy**. Property $B$: $f, g$ are smooth maps between smooth manifolds and a smooth homotopy exists between them. The bridge: every smooth homotopy is in particular continuous, so the theorem applies — and conversely (by Whitney approximation) every continuous homotopy can be smoothed. So for smooth manifolds, smooth and continuous homotopy give the same equivalence relation on smooth maps, and the same homology invariants.

**Targets (Output Amplification)**

The conclusion $C$: *$f_* = g_*$ on $H_p$ for all $p$.*

Combine $C$ with **a homotopy equivalence between $M$ and $N$.** Property $D$: there are maps $f : M \to N$ and $g : N \to M$ with $g \circ f \simeq \mathrm{id}_M$ and $f \circ g \simeq \mathrm{id}_N$. Then $(g \circ f)_* = g_* \circ f_* = \mathrm{id}$ on $H_*(M)$ and $f_* \circ g_* = \mathrm{id}$ on $H_*(N)$, so $f_*$ is an isomorphism. The further result $E$: homotopy equivalent spaces have isomorphic homology in every degree. This is the corollary stated above and is the operational content of homotopy invariance.

Combine $C$ with **the homotopy extension property of CW complexes.** $D$: $M$ is a CW complex and any continuous map $f : M \to N$ has a homotopy that extends a given homotopy on a sub-CW-complex. The further result $E$: $f$ can be homotoped to a "cellular" map (sending the $k$-skeleton of $M$ into the $k$-skeleton of $N$), and the cellular map induces the cellular chain map. This is the foundation of **cellular approximation**, the technique that makes the cellular chain complex computationally equivalent to the singular one.

Combine $C$ with **the long exact sequence of a pair $(M, A)$.** $D$: $(M, A)$ has homotopy-equivalent homotopy data — the inclusion $A \hookrightarrow M$ factors up to homotopy through some natural simpler map. The further result $E$: the long exact sequence in homology of the pair $(M, A)$ depends only on the homotopy type of the pair, and homotopy equivalent pairs give isomorphic long exact sequences. This is the basis for the **excision** axiom of Eilenberg–Steenrod.

---

# Why Is It True

**The single sentence: a continuous homotopy $H : M \times [0,1] \to N$ provides a "$(p+1)$-dimensional prism construction" $h : C_p(M) \to C_{p+1}(N)$ whose chain-level boundary is $g_\# - f_\#$ — equivalently, $g_\# - f_\# = \partial h + h \partial$ — and chain-homotopic chain maps induce equal homology maps.**

The intuition starts with a single singular simplex $\sigma : \Delta^p \to M$. The homotopy $H : M \times [0,1] \to N$ gives a continuous map $\Phi_\sigma = H \circ (\sigma \times \mathrm{id}_{[0,1]}) : \Delta^p \times [0,1] \to N$. This is a map from a $(p+1)$-dimensional prism into $N$, and we can read off its "interpretation" on each piece of the boundary:

- **Top face $\Delta^p \times \{1\}$:** $\Phi_\sigma|_{t=1} = g \circ \sigma$, a singular $p$-simplex in $N$.
- **Bottom face $\Delta^p \times \{0\}$:** $\Phi_\sigma|_{t=0} = f \circ \sigma$, a singular $p$-simplex in $N$.
- **Side faces $(\partial \Delta^p) \times [0,1]$:** prisms over the boundary of $\sigma$, giving prisms of all the codimension-$1$ faces of $\sigma$.

The boundary of the prism (as a manifold with corners) is "top — bottom + sides." Translated to chains: if we triangulate the prism into $(p+1)$-simplices and let $h(\sigma) \in C_{p+1}(N)$ be the resulting chain, then the boundary of $h(\sigma)$ in $C_p(N)$ equals
$$
\partial h(\sigma) = g \circ \sigma - f \circ \sigma - h(\partial \sigma),
$$
where the minus sign on $f \circ \sigma$ comes from the orientation of the bottom face (opposite to the top), and the $-h(\partial \sigma)$ collects the side contributions. Rearranging:
$$
g_\#(\sigma) - f_\#(\sigma) = \partial h(\sigma) + h(\partial \sigma) = (\partial h + h \partial)(\sigma).
$$

This is exactly the chain-homotopy identity from [[Def - Chain Map and Chain Homotopy]]: $g_\# - f_\# = \partial h + h \partial$. So $g_\#$ and $f_\#$ are chain-homotopic, and by the chain homotopy → equal-on-homology lemma, $f_* = g_*$.

The remaining content is the explicit construction of $h(\sigma)$ as a triangulation of the prism $\Delta^p \times [0,1]$. The standard triangulation of the prism uses $(p+1)$ different $(p+1)$-simplices, one for each "staircase path" from the bottom to the top of the prism. Each simplex has $p + 2$ vertices: a subset of "$p+1$ vertices of $\Delta^p$ at $t = 0$" and "$p+1$ vertices of $\Delta^p$ at $t = 1$," chosen consistently to form a single $(p+1)$-simplex. The alternating signs in $h(\sigma) = \sum_i (-1)^? \tau_i$ are chosen to make the boundary identity work; the calculation is straightforward but tedious.

---

# What Makes This Hard

The proof's hardest step is the **explicit construction of the prism operator** $h(\sigma) \in C_{p+1}(N)$ — choosing the right triangulation of $\Delta^p \times [0,1]$ and the right signs on each simplex. The standard triangulation uses one $(p+1)$-simplex for each "shuffle" of the vertices of the top and bottom $p$-simplex, with signs determined by the shuffle's permutation parity. Most errors come from getting the signs wrong, which can produce a chain that *almost* gives the chain-homotopy identity but with extra terms.

The conceptual obstacle is **recognising that the chain-homotopy formula is exactly the prism's boundary**. The top, bottom, and sides of the prism are the three "natural" parts of its boundary, and the chain-homotopy identity is just "boundary of $h(\sigma)$ = $g \circ \sigma$ (top) $-$ $f \circ \sigma$ (bottom) $-$ $h(\partial \sigma)$ (sides)." Once you see this, the proof is essentially a picture.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Build a chain homotopy $h : C_p(M; G) \to C_{p+1}(N; G)$ between $f_\#$ and $g_\#$ by triangulating the prism $\Delta^p \times [0,1]$ and using the continuous homotopy $H : M \times [0,1] \to N$ to map each triangulation simplex into $N$. Verify $\partial h + h \partial = g_\# - f_\#$ directly. By the chain-homotopy → equal-on-homology lemma, conclude $f_* = g_*$.

**Subgoal decomposition:**

1. **Triangulate the prism $\Delta^p \times [0,1]$.** Find a canonical decomposition of $\Delta^p \times [0,1]$ into $(p+1)$ $(p+1)$-simplices, parameterised by "staircase paths" from the bottom-left to the top-right of the prism.
   - *Hint:* Each simplex corresponds to choosing a subset of $\{0, 1, \dots, p\}$ that determines which vertices "go up first." Explicitly, the simplex $\tau_k$ has vertices $(P_0, 0), \dots, (P_k, 0), (P_k, 1), \dots, (P_p, 1)$.
   - *Why needed:* This triangulation is the geometric source of the prism operator $h$.

2. **Define the prism operator $h$.** For a singular $p$-simplex $\sigma : \Delta^p \to M$, set $h(\sigma) = \sum_{k=0}^p (-1)^k H \circ (\sigma \times \mathrm{id}_{[0,1]}) \circ \tau_k$, where $\tau_k$ are the prism simplices and the alternating signs come from the orientation bookkeeping.
   - *Hint:* Each $\tau_k$ is a $(p+1)$-simplex, so $H \circ (\sigma \times \mathrm{id}) \circ \tau_k$ is a singular $(p+1)$-simplex in $N$.
   - *Why needed:* This is the candidate chain homotopy.

3. **Verify $\partial h + h \partial = g_\# - f_\#$.** Compute the boundary $\partial h(\sigma)$ as a sum over the boundary faces of the $\tau_k$, and identify which faces collapse to $g \circ \sigma$ (top), which to $f \circ \sigma$ (bottom), and which to $h(\partial \sigma)$ (sides).
   - *Hint:* The boundary of each $\tau_k$ consists of $p+2$ codimension-$1$ faces. Some are "internal" to the prism (and cancel with neighboring $\tau_{k \pm 1}$); some are on the top, bottom, or sides.
   - *Why needed:* This is the chain-homotopy identity.

4. **Apply the chain-homotopy → equal-on-homology lemma.** Chain-homotopic chain maps induce equal maps on homology. Conclude $f_* = g_*$.
   - *Hint:* This is the content of [[Def - Chain Map and Chain Homotopy]] — on a cycle $c$, $(g - f)(c) = \partial h(c) + h(\partial c) = \partial h(c) + 0 = \partial h(c)$, a boundary, so $[g(c)] = [f(c)]$.
   - *Why needed:* This is the final step.

---

# Lemma Decomposition

> [!note]- Lemma 1: Standard Triangulation of the Prism
> **Statement:** The prism $\Delta^p \times [0,1]$ decomposes into $p+1$ $(p+1)$-simplices $\tau_0, \tau_1, \dots, \tau_p$, where $\tau_k$ has vertices (in order) $(P_0, 0), (P_1, 0), \dots, (P_k, 0), (P_k, 1), (P_{k+1}, 1), \dots, (P_p, 1)$.
>
> **Hint:** Visualise the prism as the convex hull of $2(p+1)$ vertices (the $p+1$ bottom vertices and the $p+1$ top vertices). The simplex $\tau_k$ uses the bottom vertices $(P_0, 0), \dots, (P_k, 0)$ and the top vertices $(P_k, 1), \dots, (P_p, 1)$ — a total of $p+2$ vertices, hence a $(p+1)$-simplex. The $(p+1)$ simplices tile the prism.
>
> **Why needed:** This combinatorial decomposition is the foundation of the prism operator.
>
> > [!note]- Full proof
> > *Existence of the decomposition:* The vertices of the prism are the $2(p+1)$ points $(P_i, t)$ for $i = 0, \dots, p$ and $t \in \{0, 1\}$. For each $k = 0, \dots, p$, the convex hull of $(P_0, 0), \dots, (P_k, 0), (P_k, 1), \dots, (P_p, 1)$ is a $(p+1)$-simplex $\tau_k$ — these $p+2$ vertices are affinely independent (since their projections to the $\Delta^p$ factor give a non-degenerate $p$-simplex, and the $[0,1]$ factor distinguishes $(P_k, 0)$ from $(P_k, 1)$).
> >
> > *Tiling:* Any point $(x, t) \in \Delta^p \times [0, 1]$ with barycentric coordinates $x = (x_0, \dots, x_p)$ (so $x_i \geq 0$, $\sum x_i = 1$) lies in $\tau_k$ if and only if the partial sums $x_0 + \cdots + x_{k-1} \leq 1 - t \leq x_0 + \cdots + x_k$. This condition partitions the prism by the "staircase index" $k$, giving the decomposition. Adjacent $\tau_k$ and $\tau_{k+1}$ share a common codimension-$1$ face (the simplex containing $(P_k, 0)$ and $(P_k, 1)$ but not $(P_{k+1}, 0)$ or $(P_{k+1}, 1)$ in the staircase).

> [!note]- Lemma 2: Prism Boundary Identity (one simplex)
> **Statement:** For a singular $p$-simplex $\sigma : \Delta^p \to M$ and the homotopy $H : M \times [0,1] \to N$, define $h(\sigma) = \sum_{k=0}^p (-1)^k H \circ (\sigma \times \mathrm{id}) \circ \tau_k \in C_{p+1}(N)$. Then $\partial h(\sigma) + h(\partial \sigma) = g_\#(\sigma) - f_\#(\sigma)$ in $C_p(N)$.
>
> **Hint:** Expand $\partial h(\sigma) = \sum_k (-1)^k \partial(\Phi \circ \tau_k)$, where $\Phi = H \circ (\sigma \times \mathrm{id})$. Each $\partial(\Phi \circ \tau_k)$ is an alternating sum of $p + 2$ faces. Group these faces by type: "top face," "bottom face," "side face that cancels with a side face of $\tau_{k \pm 1}$," "side face that contributes to $h(\partial \sigma)$." After cancellations, the net contributions are top minus bottom and the prism of the boundary.
>
> **Why needed:** This is the chain-level form of the chain-homotopy identity.
>
> > [!note]- Sketch
> > The detailed sign and index bookkeeping is standard but tedious. See Hatcher §2.1, Theorem 2.10, for the full calculation. The key combinatorial fact: each "interior" face of the prism triangulation appears twice with cancelling signs (once as a face of $\tau_k$, once as a face of $\tau_{k+1}$), so interior faces cancel. The "boundary" faces of the prism triangulation correspond either to the top $\Delta^p \times \{1\}$ (one simplex per $\tau_k$, contributing $(-1)^k \cdot (-1)^{k+1} g \circ \sigma$ in total which sums to $-g \circ \sigma$ — but with the overall negative from boundary orientation, gives $+g \circ \sigma$), to the bottom $\Delta^p \times \{0\}$ (analogously giving $-f \circ \sigma$), or to side faces $(\partial_j \Delta^p) \times [0,1]$ (which are themselves prisms of the $j$-th face of $\sigma$, contributing to $h(\partial \sigma)$). The total is $\partial h(\sigma) = g \circ \sigma - f \circ \sigma - h(\partial \sigma)$, giving the desired identity.

> [!note]- Lemma 3: Chain-Homotopic Chain Maps Induce Equal Maps on Homology
> **Statement:** If $f_\bullet, g_\bullet : C_\bullet \to C'_\bullet$ are chain-homotopic chain maps — there exist $h_p : C_p \to C'_{p+1}$ with $g_p - f_p = \partial' h_p + h_{p-1} \partial$ — then $f_* = g_*$ on every $H_p$.
>
> **Hint:** For a cycle $z \in Z_p$, compute $g(z) - f(z) = \partial' h(z) + h(\partial z)$. Use $\partial z = 0$ to drop the second term and conclude $g(z) - f(z) = \partial' h(z) \in B'_p$.
>
> **Why needed:** This is the algebraic core that connects the chain-level prism operator to the homology-level equality.
>
> > [!note]- Full proof
> > For $z \in Z_p$ (so $\partial z = 0$),
> > $$
> > g(z) - f(z) = (\partial' h + h \partial)(z) = \partial' h(z) + h(\partial z) = \partial' h(z) + h(0) = \partial' h(z) \in B'_p.
> > $$
> > So $g(z) - f(z)$ is a boundary, meaning $g(z)$ and $f(z)$ represent the same homology class: $[g(z)] = [f(z)]$ in $H_p(C'_\bullet)$. Hence $g_*[z] = f_*[z]$ for every homology class, i.e. $f_* = g_*$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Theorem.** Let $f, g : M \to N$ be continuous and let $H : M \times [0,1] \to N$ be a continuous homotopy with $H_0 = f$ and $H_1 = g$. Then $f_* = g_* : H_p(M; G) \to H_p(N; G)$ for every $p$ and every $G$.
>
> *Proof.*
>
> **Step 1 — define the prism operator.** Triangulate the prism $\Delta^p \times [0,1]$ into the $p+1$ simplices $\tau_0, \dots, \tau_p$ described in Lemma 1. For each $\tau_k$, treat it as a singular $(p+1)$-simplex $\tau_k : \Delta^{p+1} \to \Delta^p \times [0,1]$ by linearly parameterising its $p+2$ vertices in order.
>
> For a singular $p$-simplex $\sigma : \Delta^p \to M$, define
> $$
> h(\sigma) \;=\; \sum_{k=0}^p (-1)^k\, H \circ (\sigma \times \mathrm{id}_{[0,1]}) \circ \tau_k \;\in\; C_{p+1}(N; G).
> $$
> Extend $G$-linearly: $h\bigl(\sum_i a_i \sigma_i\bigr) = \sum_i a_i h(\sigma_i)$. This gives a homomorphism $h : C_p(M; G) \to C_{p+1}(N; G)$.
>
> **Step 2 — verify the chain-homotopy identity.** By Lemma 2 (applied simplex-by-simplex and extended by linearity),
> $$
> \partial h(c) + h(\partial c) = g_\#(c) - f_\#(c) \qquad \text{for every } c \in C_p(M; G).
> $$
> So $h$ is a chain homotopy from $f_\#$ to $g_\#$.
>
> **Step 3 — descend to homology.** By Lemma 3, chain-homotopic chain maps induce equal maps on homology. Hence $f_* = g_* : H_p(M; G) \to H_p(N; G)$ for every $p$ and every $G$. $\qquad\blacksquare$
>
> **Corollary.** Homotopy equivalent spaces have isomorphic singular homology.
>
> *Proof.* If $M \simeq N$ with maps $f : M \to N$ and $g : N \to M$ such that $g \circ f \simeq \mathrm{id}_M$ and $f \circ g \simeq \mathrm{id}_N$, apply the theorem to each homotopy: $(g \circ f)_* = g_* \circ f_* = (\mathrm{id}_M)_* = \mathrm{id}_{H_*(M)}$ and similarly $f_* \circ g_* = \mathrm{id}_{H_*(N)}$. So $f_*$ and $g_*$ are mutually inverse isomorphisms. $\qquad\blacksquare$

---

# Cross-Field Exercise Suggestions

**Homotopy invariance of de Rham cohomology.** The de Rham version of this theorem is [[Thm - Homotopy Invariance of de Rham Cohomology]] in `Differential Geometry X`. The proof there uses a "homotopy operator" $h$ on differential forms satisfying $dh + hd = G^* - F^*$ (the cohomological version of $\partial h + h \partial$). The two homotopy invariance theorems are dual — singular for chains, de Rham for forms — and both rely on the prism construction.

**Brouwer fixed point theorem.** A continuous map $f : D^n \to D^n$ from the closed disk to itself has a fixed point. The proof uses homotopy invariance: if $f$ had no fixed point, one could continuously deform $f$ to a retraction $D^n \to S^{n-1}$, contradicting $H_{n-1}(D^n) = 0$ (the disk is contractible, hence has trivial reduced homology). This is one of the most-applied consequences of homotopy invariance.

**Topological degree of maps $S^n \to S^n$.** Continuous maps $f : S^n \to S^n$ are classified up to homotopy by an integer, the **degree** $\deg f \in \mathbb{Z}$. This integer is determined by $f_* : H_n(S^n; \mathbb{Z}) \to H_n(S^n; \mathbb{Z})$, multiplication by $\deg f$. Homotopy invariance ensures $\deg f$ depends only on the homotopy class. Many topological theorems (the fundamental theorem of algebra, the Lefschetz fixed point theorem, the Hopf invariant) are statements about degrees.

**No retraction from the disk to its boundary.** There is no continuous map $r : D^n \to S^{n-1}$ with $r|_{S^{n-1}} = \mathrm{id}$. Proof: such an $r$ together with the inclusion $i : S^{n-1} \hookrightarrow D^n$ would satisfy $r \circ i = \mathrm{id}_{S^{n-1}}$, giving $r_* \circ i_* = \mathrm{id}$ on $H_{n-1}(S^{n-1}) = \mathbb{Z}$. But $H_{n-1}(D^n) = 0$ (the disk is contractible), so $i_* = 0$, making $r_* \circ i_* = 0 \neq \mathrm{id}$. Contradiction. This is the standard one-line proof of Brouwer's fixed point theorem from homotopy invariance.

---

# Bridges

- **[[Thm - Homotopy Invariance of de Rham Cohomology|Homotopy invariance of de Rham cohomology]]** — the de Rham version of this theorem. Both proofs use a "prism operator": singular uses the prism of a simplex, de Rham uses the integration $\int_0^1$ along the $[0,1]$ factor of a homotopy. By the [[Thm - The de Rham Theorem (Full Proof)|de Rham theorem]], both invariants agree on smooth manifolds, and the two prism operators are dual to each other under integration of forms over chains.

- **[[Thm - Mayer-Vietoris for Singular Homology|Mayer–Vietoris]]** — the proof of Mayer–Vietoris uses homotopy invariance via barycentric subdivision: every singular simplex on $M$ can be subdivided (which does not change its homology class, by homotopy invariance) into smaller simplices each contained in one of the cover elements $U$, $V$. The cover-restricted chain complex is then chain-homotopy equivalent to the full chain complex.

- **The Eilenberg–Steenrod Homotopy Axiom** — homotopy invariance is one of the five axioms characterising any "ordinary" homology theory. By the Eilenberg–Steenrod uniqueness theorem, any functor $\mathbf{Top} \to \mathbf{Ab}$ satisfying homotopy invariance, the long exact sequence of a pair, excision, additivity, and the dimension axiom must agree with singular homology on CW complexes.

- **Whitney approximation theorem** — for smooth manifolds, the Whitney approximation theorem says every continuous map is homotopic to a smooth one, and every continuous homotopy is homotopic to a smooth homotopy. Combined with homotopy invariance, this means the smooth and continuous singular homologies of a smooth manifold are isomorphic — used in the proof of the de Rham theorem to reduce continuous singular cycles to smooth ones.

---

# Unlocked by This

> [!tip] Mayer–Vietoris for Singular Homology *(from Algebraic Topology — this same topic)*
> The proof of Mayer–Vietoris uses **barycentric subdivision** as a chain-homotopy equivalence between the full chain complex and the subcomplex of "small" simplices (each contained in a cover element). Homotopy invariance is what justifies this — see [[Thm - Mayer-Vietoris for Singular Homology]].

> [!tip] Brouwer Fixed Point Theorem *(from Algebraic Topology)*
> Every continuous map $f : D^n \to D^n$ has a fixed point. Proof: if not, $f$ defines a retraction $D^n \to S^{n-1}$, contradicting the homotopy-invariant fact that $H_{n-1}(D^n) = 0$ while $H_{n-1}(S^{n-1}) = \mathbb{Z}$.

> [!tip] **Degree of a Map** *(from Algebraic Topology / Differential Topology)*
> A continuous map $f : S^n \to S^n$ has a well-defined **degree** $\deg f \in \mathbb{Z}$ determined by $f_* : H_n(S^n) \to H_n(S^n)$ being multiplication by $\deg f$. Two maps are homotopic iff they have the same degree. This is the simplest case of the classification of maps by their action on homology — the foundation of obstruction theory and homotopy classification.

> [!tip] **Hurewicz Theorem** *(from Algebraic Topology)*
> For a simply connected space $M$ with $\pi_p(M) = 0$ for $p < n$ and $\pi_n(M) \neq 0$, the Hurewicz homomorphism $\pi_n(M) \to H_n(M; \mathbb{Z})$ is an isomorphism. The proof uses homotopy invariance: a representative $f : S^n \to M$ of a $\pi_n$ class induces $f_* : H_n(S^n) \to H_n(M)$, and homotopic $f$'s give equal $f_*$.

> [!tip] **Cellular Approximation** *(from Algebraic Topology)*
> Every continuous map between CW complexes is homotopic to a **cellular map** — one that sends each $k$-skeleton into the $k$-skeleton of the target. This allows computation of induced maps on homology using only the cellular structure, dramatically simplifying calculations. The proof uses homotopy invariance plus an inductive cell-by-cell construction.
