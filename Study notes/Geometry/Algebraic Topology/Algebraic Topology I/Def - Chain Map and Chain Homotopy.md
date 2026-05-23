---
type: definition
subject: algebraic-topology
prereqs:
  - "Def - Singular Chain"
  - "Def - The Boundary Operator"
  - "Def - Homomorphism"
tags: [geometry, algebraic-topology, homological-algebra]
---

# Notation

This is a compound page: it defines two interlocking notions — **chain maps** and **chain homotopies** — because they are introduced together and chain homotopy is defined precisely as the homotopy relation between two chain maps.

$(C_\bullet, \partial)$ and $(C'_\bullet, \partial')$ are chain complexes of abelian groups (in our applications, the singular chain complexes of topological spaces). Each is a sequence
$$
\cdots \to C_{p+1} \xrightarrow{\partial} C_p \xrightarrow{\partial} C_{p-1} \to \cdots
$$
with $\partial^2 = 0$.

$f_\bullet = \{f_p : C_p \to C'_p\}_{p \geq 0}$ is a sequence of homomorphisms. We write $f$ or $f_\bullet$ for the whole sequence, and $f_p$ for the homomorphism in degree $p$.

$h = \{h_p : C_p \to C'_{p+1}\}$ is a sequence of homomorphisms raising degree by one — a **degree-$+1$ map**, or a "homotopy operator." (Note: in cohomology contexts, the convention reverses to degree $-1$.)

---

# Axiom Motivation

We need two algebraic notions to do real work with chain complexes: maps between them (chain maps) and a notion of when two such maps are equivalent (chain homotopy). The motivation is geometric — these are exactly what is needed to make continuous maps induce well-defined maps on homology, and to make homotopic continuous maps induce the *same* map on homology.

**Why chain maps?** Singular homology is supposed to be a functor $\mathbf{Top} \to \mathbf{Ab}$. A continuous map $f : M \to N$ should induce a homomorphism $f_* : H_p(M) \to H_p(N)$. To get there, we first build a chain-level induced map $f_\# : C_p(M) \to C_p(N)$ — pre-compose the singular simplices with $f$. For $f_\#$ to descend to homology, it must satisfy:

1. **It carries cycles to cycles:** $f_\#(\ker \partial) \subseteq \ker \partial'$. This requires $\partial' \circ f_\# = 0$ on $\ker \partial$.
2. **It carries boundaries to boundaries:** $f_\#(\mathrm{im}\,\partial) \subseteq \mathrm{im}\, \partial'$. This requires $f_\# \circ \partial = \partial' \circ f_\#$ on $C_{p+1}$.

Both conditions are encapsulated in the single requirement that $f_\#$ **commutes with the boundary operator**: $f_\# \circ \partial = \partial' \circ f_\#$ on every $C_p$. This is the definition of a chain map. With it, $f_\#$ descends to a well-defined homomorphism on homology $f_* : H_p(C_\bullet) \to H_p(C'_\bullet)$.

The geometric source of $f_\# \circ \partial = \partial \circ f_\#$ is that boundary uses face maps of the *standard simplex*, and post-composition with $f : M \to N$ commutes with pre-composition with the face maps: $(f \circ \sigma) \circ f_k = f \circ (\sigma \circ f_k)$. So at the level of singular homology, naturality of the boundary operator under continuous maps gives the chain-map condition for free.

**Why chain homotopy?** Two continuous maps $f, g : M \to N$ that are homotopic (in the topological sense — there is a continuous $H : M \times [0,1] \to N$ with $H|_{t=0} = f$ and $H|_{t=1} = g$) should induce *equal* maps on homology: $f_* = g_*$. This is the central content of [[Thm - Homotopy Invariance of Singular Homology|homotopy invariance]]. To prove it, we need an algebraic notion that captures "two chain maps differ by something that is killed in homology."

The right algebraic notion is chain homotopy. Two chain maps $f, g : C_\bullet \to C'_\bullet$ are **chain-homotopic** if there exist maps $h_p : C_p \to C'_{p+1}$ (raising degree by one) such that
$$
g_p - f_p = \partial' h_p + h_{p-1} \partial.
$$
If this holds, then on cycles ($\partial c = 0$): $g(c) - f(c) = \partial' h(c) + h(\partial c) = \partial' h(c) + 0 = \partial' h(c)$, which is a boundary. So $g(c)$ and $f(c)$ differ by a boundary, hence represent the same homology class: $f_*[c] = g_*[c]$. Chain homotopy implies equality on homology.

The geometric source of chain homotopy is the **prism operator**. Given a homotopy $H : M \times [0,1] \to N$ between $f$ and $g$, one can construct $h : C_p(M) \to C_{p+1}(N)$ that sends a singular simplex $\sigma : \Delta^p \to M$ to a $(p+1)$-chain built from the prism $\sigma \times [0,1] \to M \times [0,1] \to N$. The boundary of this prism has three pieces: the top ($g \circ \sigma$), the bottom ($-f \circ \sigma$), and the sides (the prism of the boundary $\partial \sigma$). Triangulating the prism with appropriate signs gives the identity $g - f = \partial h + h \partial$ at the chain level.

So chain homotopy is the algebraic abstraction of "the prism operator from a continuous homotopy." Once we have this notion, homotopy invariance of singular homology is a direct corollary.

**Why "raising degree by one"?** Because the prism $\Delta^p \times [0,1]$ has dimension $p + 1$, so any chain-level operation that turns $\sigma : \Delta^p \to M$ into something living in dimension $p + 1$ naturally has degree $+1$. The pattern $\partial h + h \partial$ is exactly the "boundary of the prism = top minus bottom minus prism-of-boundary" decomposition, with $h$ being the prism-construction and $\partial$ acting on either side.

**Why the asymmetric $\partial h + h \partial$ rather than $\partial h - h \partial$?** Both conventions appear in the literature; one is for chain complexes (decreasing degree), the other for cochain complexes (increasing degree). The signs are forced by orientation conventions on the prism — the precise sign comes from the orientation of $\Delta^p \times [0,1]$ relative to $\Delta^p$ and $[0,1]$. The chain-complex convention $g - f = \partial h + h \partial$ has $h$ shifting degree by $+1$ in the *codomain* direction, with both terms having matched degree.

---

# The Definition

**Chain map.** Let $(C_\bullet, \partial)$ and $(C'_\bullet, \partial')$ be two chain complexes of abelian groups. A **chain map** $f : C_\bullet \to C'_\bullet$ is a sequence of homomorphisms $f_p : C_p \to C'_p$ (for each $p \geq 0$) that **commutes with the boundary operators**:
$$
\partial' \circ f_p = f_{p-1} \circ \partial \qquad \text{for all } p.
$$

Equivalently, the diagram
$$
\begin{array}{ccc}
\cdots \to C_{p+1} & \xrightarrow{\partial} & C_p & \xrightarrow{\partial} & C_{p-1} \to \cdots \\
f_{p+1} \downarrow & & f_p \downarrow & & f_{p-1} \downarrow \\
\cdots \to C'_{p+1} & \xrightarrow{\partial'} & C'_p & \xrightarrow{\partial'} & C'_{p-1} \to \cdots
\end{array}
$$
commutes — every square is commutative.

A chain map $f : C_\bullet \to C'_\bullet$ carries cycles to cycles ($f_p(Z_p) \subseteq Z'_p$) and boundaries to boundaries ($f_p(B_p) \subseteq B'_p$), hence descends to an **induced map on homology**
$$
f_* : H_p(C_\bullet) \to H_p(C'_\bullet), \qquad f_*[z] = [f_p(z)].
$$
Chain maps compose: if $f : C_\bullet \to C'_\bullet$ and $g : C'_\bullet \to C''_\bullet$ are chain maps, so is $g \circ f$, and $(g \circ f)_* = g_* \circ f_*$. The identity chain map $\mathrm{id}_C$ induces the identity on homology.

**Chain homotopy.** Let $f, g : C_\bullet \to C'_\bullet$ be two chain maps. A **chain homotopy** from $f$ to $g$ is a sequence of homomorphisms $h_p : C_p \to C'_{p+1}$ (degree $+1$) such that
$$
g_p - f_p = \partial' h_p + h_{p-1} \partial \qquad \text{for all } p.
$$

We say $f$ and $g$ are **chain-homotopic**, written $f \simeq g$, if a chain homotopy between them exists. Chain homotopy is an equivalence relation on chain maps.

**Key consequence.** If $f, g : C_\bullet \to C'_\bullet$ are chain-homotopic, then they induce the *same* map on homology:
$$
f_* = g_* : H_p(C_\bullet) \to H_p(C'_\bullet).
$$
Indeed, for a cycle $c \in Z_p$ (so $\partial c = 0$),
$$
g(c) - f(c) = \partial' h(c) + h(\partial c) = \partial' h(c) \in B'_p,
$$
so $[g(c)] = [f(c)]$ in $H_p(C'_\bullet)$.

**Chain homotopy equivalence.** Two chain complexes are **chain homotopy equivalent** if there exist chain maps $f : C_\bullet \to C'_\bullet$ and $g : C'_\bullet \to C_\bullet$ with $g \circ f \simeq \mathrm{id}_{C_\bullet}$ and $f \circ g \simeq \mathrm{id}_{C'_\bullet}$. Chain-homotopy-equivalent complexes have isomorphic homology in every degree.

---

# Relate to Other Fields / Compression

A chain map is the **morphism in the category of chain complexes** — the level at which one can speak of "maps between chain complexes" preserving the structure. The category $\mathbf{Ch}(\mathbf{Ab})$ of chain complexes has chain maps as morphisms; chain homotopy is the standard 2-morphism structure making $\mathbf{Ch}(\mathbf{Ab})$ a 2-category (or, after quotienting by chain homotopy, the **homotopy category** $K(\mathbf{Ab})$ of chain complexes).

Chain maps are the algebraic version of **continuous maps between topological spaces**: the topological notion "continuous map" corresponds at the level of singular chains to "chain map," and at the level of homology to "homomorphism." The functor $\mathbf{Top} \to \mathbf{Ch}(\mathbf{Ab})$ sends continuous maps to chain maps, preserving composition.

Chain homotopies are the algebraic version of **continuous homotopies between continuous maps**: a continuous homotopy $H : M \times [0,1] \to N$ produces a chain homotopy via the prism operator, and chain-homotopic chain maps induce equal homology homomorphisms. The functor preserves homotopies up to chain homotopy.

**True name:** a chain map is a **commuting square of boundary operators**, $\partial' f = f \partial$. A chain homotopy is a **deficit relation** $g - f = \partial h + h \partial$, expressing the difference of two chain maps as a "coboundary" in the chain-level $\mathrm{Hom}$-complex. Both notions are the simplest invariants of the categorical structure on chain complexes.

---

# Examples / Corollaries

**Is an instance: a chain map from a topological inclusion.** For an inclusion $i : A \hookrightarrow M$ of a subspace, the induced map $i_\# : C_p(A; G) \to C_p(M; G)$ — sending a singular simplex $\sigma : \Delta^p \to A$ to the same map viewed as a singular simplex in $M$ — is a chain map. Naturality of $\partial$ gives $i_\# \circ \partial = \partial \circ i_\#$. The induced map $i_* : H_p(A; G) \to H_p(M; G)$ on homology is one of the most basic operations in algebraic topology.

**Is an instance: the chain map of a continuous map.** For $f : M \to N$ continuous, $f_\# : C_p(M; G) \to C_p(N; G)$, $\sigma \mapsto f \circ \sigma$, is a chain map. This is the standard chain-level induced map; its descent to homology $f_* : H_p(M) \to H_p(N)$ is the functoriality of singular homology.

**Is an instance: the chain homotopy of a continuous homotopy (the prism operator).** For a continuous homotopy $H : M \times [0,1] \to N$ from $f$ to $g$, the prism operator $P : C_p(M; G) \to C_{p+1}(N; G)$ sends a singular simplex $\sigma : \Delta^p \to M$ to a triangulation of the prism $\sigma \times \mathrm{id}_{[0,1]} : \Delta^p \times [0,1] \to M \times [0,1] \to N$. The signed alternating sum of the resulting $(p+1)$-simplices gives a chain homotopy from $f_\#$ to $g_\#$, proving $f_* = g_*$ on homology — this is the proof of [[Thm - Homotopy Invariance of Singular Homology]].

**Is an instance: the de Rham–Stokes pairing.** The integration map $\int : \Omega^p(M) \to C^p(M; \mathbb{R})$, $\omega \mapsto (\sigma \mapsto \int_\sigma \omega)$, intertwines the exterior derivative $d$ with the singular coboundary $\delta$ via Stokes's theorem: $\delta \int \omega = \int d\omega$. This makes $\int$ a *cochain* map — the cohomology analogue of a chain map — and it descends to the de Rham homomorphism $H^p_{dR}(M) \to H^p(M; \mathbb{R})$ in cohomology.

**Is an instance: the chain map from a refinement of triangulations.** If $K$ is a triangulation of $M$ and $K'$ is a refinement (each simplex of $K$ subdivided into smaller simplices), there is a natural chain map $C_\bullet(K) \to C_\bullet(K')$ sending each simplex to the sum of its subdivisions. The chain-homotopy class of this map is well-defined, and the induced map on homology is the identity — reflecting that refining a triangulation does not change the simplicial homology.

**Is NOT an instance: a graded homomorphism that doesn't commute with $\partial$.** For instance, define $f : C_\bullet(\mathbb{R}; \mathbb{Z}) \to C_\bullet(\mathbb{R}; \mathbb{Z})$ by $f_0(\sigma) = 2\sigma$ in degree zero but $f_p = \mathrm{id}$ in higher degrees. The square $f_0 \circ \partial = \partial \circ f_1$ becomes $f_0(\partial \gamma) = 2(\gamma(1) - \gamma(0))$ versus $\partial(f_1(\gamma)) = \partial \gamma = \gamma(1) - \gamma(0)$ — these disagree by a factor of $2$, so $f$ is not a chain map.

**Is NOT an instance: a chain map that doesn't lift to a chain homotopy equivalence.** The zero chain map $C_\bullet \to 0$ is a chain map but not a chain homotopy equivalence unless $C_\bullet$ is contractible (chain homotopic to the zero complex). For a non-contractible $C_\bullet$, the zero map induces zero on homology, but the identity does not, so they are not chain-homotopic — the zero map is not a homotopy equivalence.

**Corollary (chain homotopy is an equivalence relation).** Reflexivity: $f \simeq f$ via $h = 0$. Symmetry: if $g - f = \partial h + h \partial$ then $f - g = \partial(-h) + (-h)\partial$. Transitivity: chain homotopies compose by adding.

**Corollary (chain homotopy classes form a group under addition).** $[f] + [g] = [f + g]$ is well-defined modulo chain homotopy. The set of chain-homotopy classes of chain maps $C_\bullet \to C'_\bullet$ is an abelian group, denoted $[C_\bullet, C'_\bullet]$ in the homotopy category.

**Corollary (composition of homotopies).** If $f \simeq g$ via $h$ and $f' : C'_\bullet \to C''_\bullet$ is any chain map, then $f' \circ f \simeq f' \circ g$ via $f' \circ h$. Similarly $g' \circ f \simeq g' \circ g$ for any $g'$. So chain homotopy is preserved under pre- and post-composition with chain maps.

**Calibration check.** If you have understood the definitions you should be able to: (1) verify that for a continuous map $f : M \to N$, $f_\# \circ \partial = \partial \circ f_\#$ on a singular simplex $\sigma$, using $(f \circ \sigma) \circ f_k = f \circ (\sigma \circ f_k)$; (2) write down explicitly the chain homotopy formula $g - f = \partial h + h \partial$ on a cycle $c$ (so $\partial c = 0$) and verify it forces $f_*[c] = g_*[c]$; (3) explain why the prism operator construction has degree $+1$ (going from $C_p(M)$ to $C_{p+1}(N)$).

---

# Unlocked by This

> [!tip] Homotopy Invariance of Singular Homology *(from Algebraic Topology — this same topic)*
> Two topologically homotopic continuous maps $f, g : M \to N$ induce chain-homotopic chain maps $f_\#, g_\# : C_\bullet(M) \to C_\bullet(N)$, via the prism operator. Hence $f_* = g_*$ on homology. See [[Thm - Homotopy Invariance of Singular Homology]]. This is the algebraic core of why singular homology is a homotopy invariant.

> [!tip] The Homotopy Category of Chain Complexes *(from Homological Algebra)*
> Quotienting $\mathbf{Ch}(\mathbf{Ab})$ by chain homotopy gives the **homotopy category** $K(\mathbf{Ab})$, the natural arena for homological algebra. Further quotienting by **quasi-isomorphisms** (chain maps inducing isomorphism on homology) gives the **derived category** $D(\mathbf{Ab})$, the foundation of modern algebraic geometry and representation theory.

> [!tip] **Quasi-Isomorphism** *(from Homological Algebra)*
> A chain map $f : C_\bullet \to C'_\bullet$ is a **quasi-isomorphism** if $f_* : H_p(C_\bullet) \to H_p(C'_\bullet)$ is an isomorphism for every $p$. Chain homotopy equivalences are quasi-isomorphisms, but the converse fails in general. The derived category inverts all quasi-isomorphisms, making them isomorphisms — this is the setting in which homological algebra "really" lives.

> [!tip] **Spectral Sequences as Successive Chain-Homotopy Approximations** *(from Homological Algebra)*
> A spectral sequence computes the homology of a complicated chain complex by successive approximations, each of which is a chain complex of "higher-order" cycles modulo "higher-order" boundaries. The pages of the spectral sequence are linked by differentials (chain maps) and quasi-isomorphisms (chain homotopy equivalences). The bookkeeping of chain homotopy makes the entire spectral-sequence machinery work.
