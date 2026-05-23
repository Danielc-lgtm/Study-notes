---
type: definition
subject: algebraic-topology
prereqs:
  - "Def - Group"
  - "Def - Homomorphism"
  - "Def - Kernel and Image"
tags: [algebra, algebraic-topology, homological-algebra]
---

# Notation

$G_i$ are groups; $f_i : G_{i-1} \to G_i$ are group homomorphisms. We write the sequence as $\cdots \to G_{i-1} \xrightarrow{f_i} G_i \xrightarrow{f_{i+1}} G_{i+1} \to \cdots$. The **kernel** of $f$ is $\ker f = \{g : f(g) = e\}$; the **image** is $\mathrm{im}\, f = \{f(g) : g \in G\}$. The trivial group with one element is denoted $0$ (in additive notation, for abelian groups) or $1$ (in multiplicative notation, for general groups). See [[Algebraic Topology III — Higher Homotopy and Chern Forms]] for the full notation registry.

---

# Axiom Motivation

The motivating question is: *what is the right algebraic device to record a chain of group relationships where each kernel is the image of the previous map?* This pattern arises constantly: from short exact sequences of vector spaces (rank-nullity), from chain complexes in homology (boundary squares to zero), from the homotopy long exact sequence (sphere maps lifting through a bundle), from the fundamental theorem of homomorphisms ($G/\ker f \cong \mathrm{im}\, f$).

The first design question is: *what is the right "consecutive consistency" condition?* The simplest possibility is the **chain complex** condition: $f_{i+1} \circ f_i = 0$, that is, $\mathrm{im}\, f_i \subseteq \ker f_{i+1}$. This is the bare minimum to have well-defined homology $H_i = \ker f_{i+1} / \mathrm{im}\, f_i$. The condition that **the sequence is exact**, $\mathrm{im}\, f_i = \ker f_{i+1}$, is the *vanishing* of this homology in the middle. So an exact sequence is exactly the data of a chain complex with no homology — every "kernel" is fully exhausted by the "image".

This vanishing is the *useful* condition because it propagates information. From an exact short sequence $0 \to A \xrightarrow{f} B \xrightarrow{g} C \to 0$ we can extract:
- $\ker f = 0$, so $f$ is **injective**;
- $\mathrm{im}\, g = C$, so $g$ is **surjective**;
- $\mathrm{im}\, f = \ker g$, so $C \cong B/A$ in the abelian case (or for normal $A$).

That is the *universal property* of a short exact sequence: it encodes a normal subgroup and its quotient in a single line of algebra.

Why this condition and not a weaker one (like $f_{i+1} \circ f_i = 0$)? The chain-complex condition does not propagate isomorphisms: from $\mathrm{im}\, f_i \subseteq \ker f_{i+1}$ alone we cannot deduce that $f$ is injective or $g$ is surjective. Exact sequences are *stronger* — they are the right tool when you want to conclude things are isomorphisms, kernels are zero, or quotients are equal, all of which propagate cleanly through exactness.

Why not a stronger condition (like the sequence splits)? A split short exact sequence $0 \to A \to B \to C \to 0$ has $B \cong A \oplus C$ — much more information than exactness gives. The trouble is that splitting is a *coincidence* depending on $A, B, C$ jointly; not every short exact sequence splits (e.g., $0 \to \mathbb{Z} \xrightarrow{2} \mathbb{Z} \to \mathbb{Z}/2 \to 0$ does not split). Exactness is the universal condition that always holds in the cases of interest, while splitting is the special case.

For non-abelian groups there is a subtlety. The conclusion "$C \cong B/A$" from a short exact sequence requires $A$ to be a normal subgroup of $B$, which is implicit in the exactness: $A = \ker g \trianglelefteq B$ since kernels of homomorphisms are normal. So exactness automatically gives the normality required for the quotient to exist. But the splitting condition becomes more nuanced — there is no general "semidirect product" decomposition without further data. For abelian groups everything is cleaner, and the long exact sequences in algebraic topology (which produce abelian groups in degree $\geq 2$) are particularly well-behaved.

The deepest design choice is the **infinite sequence**. Once you have a recipe for producing short exact sequences (typically from a short exact sequence of chain complexes), the **snake lemma** and its iterations produce a long exact sequence chaining many short ones together. This is the algebraic engine behind every long exact sequence in cohomology, homology, K-theory, and homotopy theory: it is the systematic way to extract many relationships from one piece of data.

---

# The Definition

A sequence of groups and group homomorphisms

$$\cdots \to G_{i-1} \xrightarrow{f_i} G_i \xrightarrow{f_{i+1}} G_{i+1} \to \cdots$$

is **exact at $G_i$** if $\mathrm{im}\, f_i = \ker f_{i+1}$, that is, if every element of $G_i$ that is sent to the identity by $f_{i+1}$ is the image of some element of $G_{i-1}$ under $f_i$. The sequence is **exact** (without qualification) if it is exact at every interior term.

**Standard special cases:**

A **short exact sequence** is an exact sequence of the form

$$0 \to A \xrightarrow{f} B \xrightarrow{g} C \to 0.$$

The leftmost zero forces $f$ to be **injective** (since $\ker f = \mathrm{im}(0 \to A) = 0$); the rightmost zero forces $g$ to be **surjective** (since $\mathrm{im}\, g = \ker(C \to 0) = C$); the middle exactness gives $\mathrm{im}\, f = \ker g$, hence (for abelian or for $f(A)$ normal) $C \cong B / f(A) \cong B / A$.

A **long exact sequence** is an exact sequence with more than three terms, typically infinite or terminating with zeros.

The notation $1$ (or $0$ for abelian groups) denotes the trivial group with one element. We commonly omit the morphism into and out of the trivial group, writing $0 \to A \to B \to C \to 0$ rather than $0 \xrightarrow{0} A \xrightarrow{f} B \xrightarrow{g} C \xrightarrow{0} 0$.

---

# Categorical / Structural Definition

In an **abelian category** (e.g., the category of abelian groups, modules over a ring, sheaves of abelian groups), a sequence $A \xrightarrow{f} B \xrightarrow{g} C$ is exact at $B$ if and only if the *categorical image* of $f$ equals the *kernel* of $g$. The categorical image is defined as $\ker(\mathrm{coker}\, f)$, which in the category of abelian groups coincides with the set-theoretic image.

A **chain complex** in an abelian category is a sequence $\cdots \to C_{i+1} \xrightarrow{d_{i+1}} C_i \xrightarrow{d_i} C_{i-1} \to \cdots$ with $d_i \circ d_{i+1} = 0$, that is, $\mathrm{im}\, d_{i+1} \subseteq \ker d_i$. The **$i$-th homology** is $H_i = \ker d_i / \mathrm{im}\, d_{i+1}$. The chain complex is **exact** if and only if all $H_i = 0$.

An **exact sequence is a chain complex with zero homology**. This is the cleanest categorical viewpoint, and it explains why exact sequences are the natural objects in homological algebra: they are the chain complexes that contribute nothing to homology.

In a **derived category** $D(\mathcal{A})$, short exact sequences are replaced by **distinguished triangles** $A \to B \to C \to A[1]$, the rotational analogue. The rotation $[1]$ is the suspension/shift functor. Distinguished triangles produce long exact sequences in any cohomological functor applied to them — the modern formulation of the long-exact-sequence machinery.

---

# Relate to Other Fields / Compression

**True name:** an exact sequence is **a chain of group relationships in which each kernel exactly equals the previous image**, expressing simultaneously injectivity, surjectivity, and quotient relations through a single uniform condition. Equivalently, it is a chain complex with no homology — the algebraic embodiment of "no obstructions".

In **linear algebra**, the rank-nullity theorem for a linear map $T : V \to W$ is the short exact sequence $0 \to \ker T \to V \to \mathrm{im}\, T \to 0$, giving $\dim V = \dim\ker T + \dim\mathrm{im}\, T$. Every short exact sequence of finite-dimensional vector spaces splits, so dimension is additive.

In **algebraic topology**, the long exact sequence of a pair $(X, A)$ in homology is the prototypical infinite exact sequence: $\cdots \to H_n(A) \to H_n(X) \to H_n(X, A) \to H_{n-1}(A) \to \cdots$. The same pattern recurs in the long exact sequence of a fibration (see [[Thm - Long Exact Sequence of a Fibration]]) — in fact every "long exact sequence" comes from a short exact sequence of chain complexes via the **snake lemma**.

In **K-theory**, the long exact sequence of a pair becomes the **Mayer–Vietoris sequence** for an open cover, and globally the **Bass exact sequence** $K_1(A) \to K_1(B) \to K_1(B/A) \to K_0(A) \to \cdots$ connecting algebraic $K$-theory of a ring $A$ with that of a quotient.

In **representation theory**, the **five-term exact sequence** $0 \to H^1(G/N, M^N) \to H^1(G, M) \to H^1(N, M)^{G/N} \to H^2(G/N, M^N) \to H^2(G, M)$ is the start of the Hochschild–Serre spectral sequence for group cohomology — another instance of long exact sequences encoding structural relationships.

---

# Examples / Corollaries

**Example: $0 \to 2\mathbb{Z} \to \mathbb{Z} \to \mathbb{Z}/2 \to 0$.** The inclusion of even integers into integers, followed by reduction mod 2. Exactness at $\mathbb{Z}$ says $\mathrm{im}(2\mathbb{Z} \hookrightarrow \mathbb{Z}) = 2\mathbb{Z} = \ker(\mathbb{Z} \twoheadrightarrow \mathbb{Z}/2)$, both clearly true. This is the simplest non-split short exact sequence: there is no surjection $\mathbb{Z} \to 2\mathbb{Z}$ splitting the inclusion, since any homomorphism $\mathbb{Z} \to \mathbb{Z}$ is multiplication by an integer.

**Example: $0 \to \mathbb{Z} \xrightarrow{\exp(2\pi i \cdot)} \mathbb{R} \to S^1 \to 0$.** Wait, $S^1$ is not a group additively. The exact sequence is $0 \to \mathbb{Z} \to \mathbb{R} \xrightarrow{\exp(2\pi i \cdot)} S^1 \to 1$ where $S^1$ is the multiplicative circle group of unit complex numbers. The kernel of exponentiation is $\mathbb{Z}$, and exponentiation is surjective, so we have a short exact sequence exhibiting $S^1 = \mathbb{R}/\mathbb{Z}$.

**Example: the first isomorphism theorem.** Every group homomorphism $\varphi : G \to H$ gives a short exact sequence

$$1 \to \ker\varphi \to G \to \mathrm{im}\,\varphi \to 1.$$

Exactness is built in. By [[Thm - First Isomorphism Theorem|the first isomorphism theorem]], $\mathrm{im}\,\varphi \cong G/\ker\varphi$.

**Example: split exact sequence.** $0 \to A \to A \oplus B \to B \to 0$ with the obvious inclusion and projection. This always splits — the projection $A \oplus B \to A$ provides a left inverse to the inclusion, and the inclusion $B \hookrightarrow A \oplus B$ provides a right inverse to the projection. So $A \oplus B$ is determined by $A$ and $B$.

**Example: long exact sequence of a pair in homology.** For $(X, A)$ a pair of topological spaces,
$$\cdots \to H_n(A) \to H_n(X) \to H_n(X, A) \xrightarrow{\partial} H_{n-1}(A) \to \cdots$$
The boundary map $\partial$ comes from the snake lemma applied to the short exact sequence of singular chain complexes $0 \to C_*(A) \to C_*(X) \to C_*(X)/C_*(A) \to 0$.

**Example: a non-exact chain.** $0 \to \mathbb{Z}/4 \to \mathbb{Z}/4 \to \mathbb{Z}/2 \to 0$ where the first map is multiplication by 2 and the second is reduction mod 2. The image of the first is $2\mathbb{Z}/4 \cong \mathbb{Z}/2$, the kernel of the second is also $2\mathbb{Z}/4 \cong \mathbb{Z}/2$, so this is exact. But $0 \to \mathbb{Z}/4 \xrightarrow{2} \mathbb{Z}/4$ alone: the image of $2$ is $\{0, 2\}$, and there is nothing on the left to compare. The sequence is "exact at $\mathbb{Z}/4$" only if you start with $0 \to \mathbb{Z}/4 \to \mathbb{Z}/4$ — meaning $\ker(2) = 0$, but $\ker(2 : \mathbb{Z}/4 \to \mathbb{Z}/4) = \{0, 2\} \neq 0$. So the sequence is *not* exact at $\mathbb{Z}/4$. This shows that exactness is a stringent condition.

**Example: long exact sequence of a fibration.** For $F \to E \to B$ a fibration,
$$\cdots \to \pi_k(F) \to \pi_k(E) \to \pi_k(B) \xrightarrow{\partial} \pi_{k-1}(F) \to \cdots \to \pi_1(B).$$
See [[Thm - Long Exact Sequence of a Fibration]].

**Is NOT an instance: $\mathbb{Z}/2 \to \mathbb{Z}/4 \to \mathbb{Z}/2 \to 0$ with the inclusion and reduction mod 2.** The image of the inclusion is $\{0, 2\} \subset \mathbb{Z}/4$, equal to the kernel of reduction. So this is exact at $\mathbb{Z}/4$. Continuing: the inclusion is injective, so $\ker(\mathbb{Z}/2 \to \mathbb{Z}/4) = 0$, so we would need $0$ on the left for exactness at the first $\mathbb{Z}/2$. The sequence $0 \to \mathbb{Z}/2 \to \mathbb{Z}/4 \to \mathbb{Z}/2 \to 0$ is exact and is the **non-split short exact sequence** that exhibits $\mathbb{Z}/4$ as a non-trivial extension.

**Corollary: $0 \to A \to B \to 0$ exact implies $A \cong B$.** Exactness at $B$ says $\mathrm{im}(A \to B) = B$ (surjective) and exactness at $A$ says $\ker(A \to B) = 0$ (injective). An injective surjective homomorphism is an isomorphism. So a four-term exact sequence with zeros on the ends collapses to an isomorphism.

**Corollary: snake lemma.** Given a commutative diagram of short exact sequences of abelian groups,
$$
\begin{array}{ccccccccc}
0 & \to & A & \to & B & \to & C & \to & 0 \\
& & \downarrow f & & \downarrow g & & \downarrow h & & \\
0 & \to & A' & \to & B' & \to & C' & \to & 0
\end{array}
$$
there is a long exact sequence
$$0 \to \ker f \to \ker g \to \ker h \xrightarrow{\partial} \mathrm{coker}\, f \to \mathrm{coker}\, g \to \mathrm{coker}\, h \to 0.$$
This is the basic machine that produces long exact sequences from short ones. The boundary map $\partial$ is constructed by diagram-chasing.

**Calibration check.** If you understand the definition you should be able to: (i) decide whether the sequence $0 \to \mathbb{Z}/2 \to \mathbb{Z}/4 \to \mathbb{Z}/2 \to 0$ (with multiplication by 2, reduction mod 2) is exact; (ii) write the first isomorphism theorem as a short exact sequence; (iii) recognise that an exact sequence is a chain complex with no homology.

---

# Unlocked by This

> [!tip] Long Exact Sequence Machinery *(from Homological Algebra)*
> Every short exact sequence of chain complexes $0 \to A_* \to B_* \to C_* \to 0$ produces a long exact sequence in homology
> $$\cdots \to H_n(A) \to H_n(B) \to H_n(C) \xrightarrow{\partial} H_{n-1}(A) \to \cdots$$
> via the **snake lemma**. The boundary $\partial$ is constructed by lifting a cycle in $C_n$ to a chain in $B_n$, taking its boundary in $B_{n-1}$, and observing that this boundary lies in $A_{n-1}$ and is a cycle. This is the *one machine* that produces every long exact sequence in topology, homological algebra, and algebraic geometry: long exact sequences of pairs, of fibrations, of sheaves, of triples, of derived functors — all instances.

> [!tip] Derived Functors *(from Homological Algebra)*
> A functor $F$ between abelian categories is **exact** if it preserves exact sequences. Most natural functors (tensor, Hom, fixed points under a group) are only **left** or **right** exact. The **derived functors** $L^i F$, $R^i F$ measure the failure of exactness: an exact sequence $0 \to A \to B \to C \to 0$ produces a long exact sequence $\cdots \to L^1 F(C) \to F(A) \to F(B) \to F(C) \to 0$ (for right-exact $F$) with the derived functors at the front. This is the foundation of all sheaf cohomology, Ext, Tor, and group cohomology.
