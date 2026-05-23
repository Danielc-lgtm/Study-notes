---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Smooth Manifold"
  - "Def - Smooth Map between Manifolds"
tags: [geometry, differential-geometry, homotopy]
---

# Notation

$M, N$ are smooth manifolds. $I = [0, 1]$ is the closed unit interval. A continuous map $H : M \times I \to N$ is *smooth* if it extends to a smooth map on an open neighborhood of $M \times I$ in $M \times \mathbb{R}$ — equivalently, all partial derivatives in $M$ and in $t$ exist and are continuous up to $t = 0$ and $t = 1$.

This is a compound page: it defines three interlocking notions — **smooth homotopy of maps**, **contractibility**, and **smooth homotopy equivalence** — because they are introduced together and none is fully usable without the others.

---

# Axiom Motivation

The desideratum: we want an equivalence relation on smooth maps $M \to N$ that captures "continuous deformability through smooth maps." The motivating problem is that we want to prove statements like "if you can continuously deform map $F$ to map $G$, they induce the same map on cohomology" — and to do this rigorously in the smooth category, we need a notion of deformation that lives entirely among smooth maps. The challenge is to express "$F$ can be continuously deformed to $G$" as a single smooth object.

The single-object trick is to parameterize the deformation. Instead of saying "for each $t \in [0, 1]$, there is a smooth map $H_t : M \to N$ with $H_0 = F$, $H_1 = G$, and the family $\{H_t\}$ varies smoothly in $t$," we recognize this is just a smooth map of one higher [[Def - Dimension|dimension]]: a function $H : M \times [0, 1] \to N$ with $H(\cdot, 0) = F$ and $H(\cdot, 1) = G$. The product manifold $M \times [0, 1]$ packages the source manifold $M$ together with the deformation parameter $t$, and a single smooth function on the product captures the entire family. This is the bookkeeping that makes the definition workable.

Why smooth instead of continuous? Two reasons. First, in the smooth category we want to apply differential techniques — pullback of forms, integration, Lie derivatives — and these require enough regularity for derivatives to be defined. Second, by the **Whitney approximation theorem**, every continuous homotopy can be perturbed to a smooth one without changing the homotopy class, so restricting to smooth [[Def - Homotopy|homotopies]] makes no difference at the level of homotopy classes. So we lose no generality and gain access to calculus.

Why $[0, 1]$ and not all of $\mathbb{R}$? The interval $[0, 1]$ is the most parsimonious parameterization — only two boundary conditions, at $t = 0$ and $t = 1$. Using all of $\mathbb{R}$ would require us to specify what happens "at $t = \pm \infty$," adding complications without benefits. The interval is compact, which is essential for arguments like "the integral over $t$ from $0$ to $1$ converges" used in the homotopy operator construction.

Why is this an *equivalence* relation? Reflexivity: $F$ is homotopic to itself via the constant homotopy $H(x, t) = F(x)$. Symmetry: if $H$ is a homotopy from $F$ to $G$, then $H'(x, t) := H(x, 1-t)$ is a homotopy from $G$ to $F$. Transitivity: composition of [[Def - Homotopy|homotopies]], using a smooth bump function to glue at $t = 1/2$. So the relation "smoothly homotopic" partitions $C^\infty(M, N)$ into equivalence classes, called **homotopy classes**, denoted $[M, N]$.

Why introduce *contractibility* as a separate concept? Because the homotopy invariance of cohomology forces us to single out the spaces whose identity is homotopic to a constant — these are the spaces where the inclusion of a single point is a homotopy equivalence, and hence (by homotopy invariance) the spaces with trivial cohomology in positive degrees. The Poincaré lemma generalizes from "$\mathbb{R}^n$" to "contractible," and contractibility is the precise local condition that makes the lemma apply.

Why introduce *homotopy equivalence*? Because we want two spaces to be considered "the same from a homotopy-theoretic viewpoint" — and "homeomorphic" is too strong (the Möbius strip and $S^1$ are not homeomorphic but should be cohomologically equivalent), while "have the same cohomology" is too weak (it is a consequence, not a definition). Homotopy equivalence is the right intermediate notion: two maps $F : M \to N$ and $G : N \to M$ such that $F \circ G$ is homotopic to $\mathrm{id}_N$ and $G \circ F$ is homotopic to $\mathrm{id}_M$. This is *symmetric* (unlike "$M$ is homotopic to $N$"), and it forces all homotopy-invariant functors (like cohomology) to send the two spaces to isomorphic objects.

The choice to take "homotopy" rather than the stronger "ambient isotopy" or weaker "weak homotopy equivalence" is forced by what we want to do with it. Homotopy invariance of cohomology fails for weak homotopy equivalence in general but holds for spaces with the homotopy type of a CW complex — including all smooth manifolds, by Whitney's CW-structure theorem. So homotopy is the right notion for cohomology of manifolds, and the smoothness is harmless.

---

# The Definition

**Smooth homotopy.** Two smooth maps $F, G : M \to N$ between smooth manifolds are **smoothly homotopic**, written $F \simeq G$, if there exists a smooth map

$$H : M \times \mathbb{R} \to N$$

(equivalently, defined on a neighborhood of $M \times [0, 1]$ in $M \times \mathbb{R}$ and smooth there) such that $H(x, 0) = F(x)$ and $H(x, 1) = G(x)$ for every $x \in M$. The map $H$ is called a **smooth homotopy from $F$ to $G$**.

The relation $\simeq$ is an equivalence relation on $C^\infty(M, N)$. The equivalence classes are called **smooth homotopy classes**.

**Contractibility.** A smooth manifold $M$ is **contractible** if the identity map $\mathrm{id}_M : M \to M$ is smoothly homotopic to a constant map $c_q : M \to M$, $c_q(x) = q$, for some point $q \in M$. Equivalently, $M$ is contractible iff every smooth map $f : K \to M$ from any manifold $K$ is homotopic to a constant.

**Smooth homotopy equivalence.** A smooth map $F : M \to N$ is a **smooth homotopy equivalence** if there exists a smooth map $G : N \to M$ such that $G \circ F \simeq \mathrm{id}_M$ and $F \circ G \simeq \mathrm{id}_N$. The manifolds $M$ and $N$ are **smoothly homotopy equivalent**, written $M \simeq N$, if such a pair $(F, G)$ exists. Homotopy equivalence is an equivalence relation on smooth manifolds.

---

# Relate to Other Fields / Compression

**True name:** A smooth homotopy is a *smooth path in the space of smooth maps*. The product $M \times I$ is the time axis; the homotopy $H$ is a curve $t \mapsto H_t$ in $C^\infty(M, N)$, where $H_t(x) = H(x, t)$. This view immediately suggests the right calculus: the homotopy operator (used in the proof of homotopy invariance of cohomology) is precisely the integration of the pullback of forms along this curve, $h\omega = \int_0^1 \iota_{\partial_t}(H^*\omega)\,dt$, building a chain homotopy from the geometric homotopy.

**Compression to topology.** A smooth homotopy is just a continuous homotopy that happens to be smooth — and by **Whitney approximation**, every continuous homotopy between smooth maps can be replaced by a smooth one in the same continuous-homotopy class. So at the level of homotopy classes, "smoothly homotopic" and "continuously homotopic" agree on smooth manifolds. This is the bridge that lets us import topological homotopy theory wholesale into the smooth category.

**Compression to algebraic topology.** Homotopy classes $[M, N]$ are a discrete invariant — a set, not a manifold. They form the morphism set of the **homotopy category**, where smooth manifolds are objects and homotopy classes of smooth maps are morphisms. Composition is well-defined: if $F_1 \simeq F_2$ and $G_1 \simeq G_2$, then $G_1 \circ F_1 \simeq G_2 \circ F_2$. Every functor that descends to the homotopy category — like de Rham cohomology, the singular cohomology, the homotopy groups $\pi_k$ — is a "homotopy invariant."

---

# Examples / Corollaries

**Is an instance: any convex subset of $\mathbb{R}^n$ is contractible.** Take $U \subseteq \mathbb{R}^n$ convex, fix $c \in U$, and define $H(x, t) = c + t(x - c)$ — a straight-line homotopy from the constant map $c_c$ (at $t = 0$) to $\mathrm{id}_U$ (at $t = 1$). Smoothness is obvious, and at $t = 0$ we get $H(x, 0) = c$ for every $x$ while $H(x, 1) = x$. So $\mathrm{id}_U \simeq c_c$, proving $U$ contractible.

**Is an instance: any star-shaped subset of $\mathbb{R}^n$ is contractible.** Same construction — if $U$ is star-shaped about $c$, then $H(x, t) = c + t(x - c)$ is the homotopy; star-shapedness ensures the segment stays in $U$ for $t \in [0, 1]$.

**Is an instance: $\mathbb{R}^n \setminus \{x_0\}$ is homotopy equivalent to $S^{n-1}$ for $n \geq 1$.** The radial projection $\pi : x \mapsto (x - x_0)/\|x - x_0\|$ and the inclusion $i : S^{n-1} \hookrightarrow \mathbb{R}^n \setminus \{x_0\}$ (using the unit sphere centered at $x_0$) satisfy $\pi \circ i = \mathrm{id}_{S^{n-1}}$ and $i \circ \pi \simeq \mathrm{id}_{\mathbb{R}^n \setminus \{x_0\}}$ via the homotopy $H(x, t) = (1-t)\frac{x - x_0}{\|x-x_0\|} + tx$ (a straight-line homotopy in $\mathbb{R}^n \setminus \{x_0\}$). This is the key deformation that lets us compute $H^*(\mathbb{R}^n \setminus \{0\}) \cong H^*(S^{n-1})$.

**Is NOT an instance: $S^1$ is *not* contractible.** If it were, then $H^1_{dR}(S^1)$ would be zero (by homotopy invariance, equal to $H^1$ of a point); but $\int_{S^1} d\theta = 2\pi \neq 0$ shows that the closed form $d\theta$ is not exact, so $H^1_{dR}(S^1) \neq 0$. The contrapositive: $S^1$ is not contractible. This is the prototype non-example, and it is why "topology of the circle" is the first interesting topological problem.

**Is NOT an instance: the constant map $c : \mathbb{R}^2 \to \mathbb{R}^2 \setminus \{0\}$ at $(1, 0)$ is *not* a homotopy equivalence.** A homotopy equivalence between $\mathbb{R}^2$ (contractible) and $\mathbb{R}^2 \setminus \{0\}$ (not contractible — homotopy equivalent to $S^1$) cannot exist: they have non-isomorphic cohomology. This probes the difference between "homotopic to" (which the inclusion is — to the constant) and "homotopy equivalent" (which requires a two-way inverse up to homotopy).

**Corollary (homotopy is independent of basepoint).** If $H_1 : F \simeq G$ and $H_2 : G \simeq K$, then $F \simeq K$ — concretely via the homotopy $H(x, t) = H_1(x, 2t)$ for $t \in [0, 1/2]$ and $H_2(x, 2t - 1)$ for $t \in [1/2, 1]$. The juncture at $t = 1/2$ needs smoothing — done via a smooth bump function that reparameterizes the homotopies near the boundaries. *Calibration:* this shows $\simeq$ is transitive, and it is the technical reason smoothness in $t$ never causes problems.

**Corollary (contractibility forces $H^k_{dR} = 0$ for $k \geq 1$).** If $M$ is contractible, the inclusion of a point is a homotopy equivalence, and by [[Thm - Homotopy Invariance of de Rham Cohomology|homotopy invariance]] $H^k_{dR}(M) \cong H^k_{dR}(\text{point}) = 0$ for $k \geq 1$. This corollary is the conceptual upgrade of the Euclidean Poincaré lemma to general manifolds.

**Calibration check.** If you have understood the definition you should be able to (i) write down explicitly a homotopy from the identity on $\mathbb{R}^2$ to a constant map, (ii) explain why $S^n$ is *not* contractible (using a non-zero integral of a closed form), and (iii) verify that the relation "smoothly homotopic" is symmetric.

---

# Unlocked by This

> [!tip] **Homotopy invariance of de Rham cohomology** *(from `Differential Geometry X`)*
> Once you have smooth homotopy, the [[Thm - Homotopy Invariance of de Rham Cohomology|homotopy invariance theorem]] says smoothly homotopic maps induce equal maps on $H^*_{dR}$. This is the workhorse of every cohomology computation: replace $M$ with a homotopy-equivalent simpler space before computing. The proof constructs a chain homotopy $h$ between the pullback maps using the homotopy's smooth structure.

> [!tip] **Homotopy groups** *(from Algebraic Topology)*
> The set $[S^k, M]$ of pointed homotopy classes of smooth maps from the $k$-sphere into $M$ is a group (the **$k$-th homotopy group** $\pi_k(M)$), abelian for $k \geq 2$. Smooth homotopies are the data that define these groups; their computation for spheres ($\pi_k(S^n)$) is one of the deepest open problems in topology, and the answer for $k > n$ — the **stable homotopy groups of spheres** — is governed by the Adams spectral sequence and remains incompletely understood.

> [!tip] **CW complex structure on manifolds** *(from Algebraic Topology)*
> Every smooth manifold is homotopy equivalent to a **CW complex** — a space built by attaching cells of increasing dimension. This is **Whitney's theorem on triangulability**, and it lets one transfer combinatorial cellular computations of cohomology into the smooth setting. The de Rham theorem is one consequence: cellular cohomology with real coefficients equals de Rham cohomology.

> [!tip] **Differentiability is irrelevant for homotopy classes** *(from algebraic topology of smooth manifolds)*
> By **Whitney approximation**, $[M, N]^{\text{smooth}} = [M, N]^{\text{continuous}}$ for smooth manifolds. This says the smooth-versus-continuous distinction matters for the *forms* you can write down, but not for the homotopy-theoretic invariants those forms detect. Every smooth-manifold cohomology theory therefore has both a smooth-and-a-topological description, and we use whichever is computationally easier.
