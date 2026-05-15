---
type: definition
subject: group-theory
prereqs:
  - "Def - Group"
  - "Def - Subgroup"
  - "Def - Homomorphism"
  - "Def - Kernel and Image"
tags: [algebra, group-theory]
---

# Notation

For a set $X$, the symmetric group of $X$ is written $\operatorname{Sym}(X)$ — the group of all bijections $X \to X$ under composition. When $X = \{1, 2, \dots, n\}$ this group is abbreviated $S_n$, and it has order $|S_n| = n!$. Its elements are called **permutations**. Permutations are written in **disjoint cycle notation**: the cycle $(a_1\, a_2\, \cdots\, a_k)$ denotes the permutation sending $a_1 \mapsto a_2 \mapsto \cdots \mapsto a_k \mapsto a_1$ and fixing everything else, and a general permutation is a product of cycles on disjoint sets of points, for instance $(1\,2\,3)(4\,5) \in S_5$. Fixed points (cycles of length one) are usually omitted from the notation. A **transposition** is a $2$-cycle $(a\, b)$. The **sign homomorphism** is $\operatorname{sgn} : S_n \to \{\pm 1\}$, and the **alternating group** $A_n = \ker(\operatorname{sgn})$ is the subgroup of even permutations. Composition is read right-to-left, as for functions: $\sigma\tau$ means "do $\tau$, then $\sigma$". See [[Group Theory II — §1.3–1.4]] for the full notation registry.

---

# Axiom Motivation

The thing being captured is **all the ways to rearrange a set, packaged so they can be done one after another and undone**. This is not an arbitrary construction — it is forced. Start from a concrete problem: you have $n$ objects in a row, and you want to study the rearrangements of them. A rearrangement is, precisely, a rule telling you where each object goes. For this rule to be a genuine rearrangement and not a collapse, two different objects must go to two different places (the rule is injective) and every place must be filled (the rule is surjective). So a rearrangement of a set $X$ is exactly a **bijection** $X \to X$, no more and no less. The symmetric group is then not a definition we *choose* but the inevitable collection: take all of them.

Why should this collection be a [[Def - Group|group]]? Run through the axioms and watch each one be satisfied for free. We want to combine two rearrangements into one — do the first, then the second — and the composite of two bijections is again a bijection, so **closure** holds and the operation is composition $\circ$. Composition of functions is **associative** automatically: $(\rho \circ \sigma) \circ \tau$ and $\rho \circ (\sigma \circ \tau)$ both mean "apply $\tau$, then $\sigma$, then $\rho$", so the group axiom of associativity is a theorem about functions, not an imposition. The **identity** is the do-nothing rearrangement, the identity map $\operatorname{id}_X$, which fixes every point. And every bijection has a genuine inverse function which is itself a bijection, so the **inverse** axiom holds. The symmetric group is therefore the canonical example of the slogan that *groups are symmetries*: it is what you get when you take "the symmetries of a bare set" — a set with no structure to preserve — so that *every* bijection counts.

Now, why specifically restrict to **bijections** and not allow arbitrary functions $X \to X$? Because the inverse axiom would fail. The functions $X \to X$ under composition form a [[Def - Group|monoid]] — associative, with identity — but a non-injective function like $1, 2 \mapsto 1$, $3 \mapsto 3$ on $\{1,2,3\}$ has no inverse: nothing composed with it can recover the lost distinction between $1$ and $2$. A non-surjective function misses a point and likewise cannot be undone. Bijectivity is exactly the condition that makes a self-map *reversible*, so it is exactly what the group axioms demand. Weaken "bijection" to "function" and you lose the group; you are left with the transformation monoid, a perfectly real object but unable to model "undo".

What about going the other way — why not restrict *further*, to only *some* bijections? You can, and the result is the notion of a [[Def - Permutation Group|permutation group]], a subgroup of $\operatorname{Sym}(X)$. But $\operatorname{Sym}(X)$ itself is the maximal, universal case, and it must be defined first because it is the ambient group every permutation group lives inside. Taking *all* bijections is what makes $\operatorname{Sym}(X)$ canonical: there is no choice involved, hence nothing to get wrong.

The finite case $S_n$ deserves its own motivation, because the **sign** structure is genuinely a discovery rather than a definition. Here is the desideratum. Every permutation can be built from transpositions — swaps of two points — since you can sort any arrangement by a sequence of swaps; concretely, a $k$-cycle $(a_1\,\cdots\,a_k) = (a_1\,a_k)(a_1\,a_{k-1})\cdots(a_1\,a_2)$ is a product of $k-1$ transpositions. The number of transpositions used is *not* fixed — you can pad with a swap and its undo, $(a\,b)(a\,b) = \operatorname{id}$ — but, and this is the non-obvious fact, its **parity** is. Every way of writing a given $\sigma$ as a product of transpositions uses an even number, or every way uses an odd number; the two cases never mix. We want a function recording this parity, and we want it to *respect composition* so it can be used as a structural invariant: stacking an even rearrangement onto an even one should give an even one, even onto odd should give odd, exactly the multiplication of $\{\pm 1\}$. That demand — a parity function that is a [[Def - Homomorphism|homomorphism]] — is met by $\operatorname{sgn}$, and the well-definedness of parity is precisely what makes $\operatorname{sgn}$ exist. If parity were not well-defined, every permutation would be expressible with both parities and there would be no consistent function to define; the entire even/odd dichotomy, and the [[Def - Simple Group|simple]] group $A_n$ that grows out of it, would collapse. So the sign homomorphism is the formal shadow of a real theorem, and $A_n = \ker(\operatorname{sgn})$ is then automatically a [[Def - Normal Subgroup|normal subgroup]] of [[Thm - Lagrange's Theorem|index]] $2$.

---

# The Definition

Let $X$ be a set. The **symmetric group** of $X$, written $\operatorname{Sym}(X)$, is the group whose underlying set is the collection of all bijections $X \to X$, with group operation composition of functions, identity element the identity map $\operatorname{id}_X$, and the inverse of a bijection being its inverse function. Its elements are called **permutations** of $X$.

When $X = \{1, 2, \dots, n\}$, the symmetric group is written $S_n$ and called the **symmetric group on $n$ letters**. It is finite of order

$$|S_n| = n!,$$

since a bijection of $\{1,\dots,n\}$ is determined by choosing the image of $1$ ($n$ ways), then of $2$ ($n-1$ ways), and so on.

A **transposition** is a permutation that swaps two points and fixes all others. Every permutation in $S_n$ can be written as a product of transpositions, and although the number of transpositions is not unique, its parity is: a permutation is **even** if it is a product of an even number of transpositions and **odd** if it is a product of an odd number, and no permutation is both. The **sign homomorphism**

$$\operatorname{sgn} : S_n \longrightarrow (\{\pm 1\}, \times, 1), \qquad \operatorname{sgn}(\sigma) = \begin{cases} +1 & \sigma \text{ even} \\ -1 & \sigma \text{ odd} \end{cases}$$

is a [[Def - Homomorphism|homomorphism]], and is surjective for $n \geq 2$. The **alternating group** is its [[Def - Kernel and Image|kernel]],

$$A_n = \ker(\operatorname{sgn}) = \{\sigma \in S_n : \sigma \text{ is even}\}.$$

By the [[Thm - First Isomorphism Theorem|first isomorphism theorem]], $A_n$ is a [[Def - Normal Subgroup|normal subgroup]] of $S_n$, and since $S_n / A_n \cong \{\pm 1\}$ it has [[Thm - Lagrange's Theorem|index]] $2$, hence order $n!/2$ for $n \geq 2$.

---

# Relate to Other Fields / Compression

The symmetric group is **the automorphism group of a set with no structure**. For any mathematical object — a vector space, a graph, a topological space, a field — the structure-preserving bijections of that object to itself form a group, its automorphism group: $\mathrm{GL}_n(\mathbb{R})$ for a vector space, the graph automorphism group for a graph, the Galois group for a field extension. A bare set has *no* structure to preserve, so *every* bijection is structure-preserving, and $\operatorname{Sym}(X)$ is the automorphism group of $X$ regarded as nothing but a set. This is the precise sense in which $\operatorname{Sym}(X)$ is the *largest* possible symmetry group on the points of $X$: every other automorphism group on those points, sitting inside it, is the subgroup of bijections that additionally respect whatever extra structure is present. [[Thm - Cayley's Theorem|Cayley's theorem]] turns this around — every group whatsoever is a subgroup of some $\operatorname{Sym}(X)$ — so $\operatorname{Sym}(X)$ is simultaneously the most special example of a group and, in the union over all $X$, the universal one.

Disjoint cycle notation is the same idea as the **cycle decomposition of a function's orbits**. A permutation $\sigma$ of $X$ partitions $X$ into its orbits under repeated application — the sets $\{x, \sigma(x), \sigma^2(x), \dots\}$ — and on each orbit $\sigma$ acts as a cyclic shift. Writing $\sigma$ in disjoint cycle form is literally listing these orbits. This is the finite, discrete shadow of the orbit decomposition that appears throughout dynamical systems, where the long-run behaviour of a map is organised by its periodic orbits; for a permutation of a finite set every orbit is periodic, so the decomposition is complete and finite.

---

# Examples / Corollaries

**Is an instance: $S_3$, the smallest non-abelian group.** The symmetric group on $\{1,2,3\}$ has $3! = 6$ elements: the identity, three transpositions $(1\,2), (1\,3), (2\,3)$, and two $3$-cycles $(1\,2\,3), (1\,3\,2)$. It is non-abelian — $(1\,2)(1\,3) = (1\,3\,2)$ but $(1\,3)(1\,2) = (1\,2\,3)$ — and is in fact the smallest non-abelian group of all. It is isomorphic to the [[Def - Group|dihedral group]] $D_6$ of symmetries of an equilateral triangle, the triangle's three vertices being the three letters.

**Is an instance: $S_1$ and $S_2$, the degenerate cases.** The group $S_1$ permutes a one-element set and is the trivial group. The group $S_2$ permutes $\{1,2\}$ and has order $2$, its non-identity element the transposition $(1\,2)$; it is the cyclic group $C_2$. These probe the boundary of the sign construction: $\operatorname{sgn}$ is surjective only for $n \geq 2$, since for $n = 1$ there are no transpositions and every permutation is vacuously even, so the image is just $\{+1\}$.

**Is an instance: $A_n$, the alternating group, for any $n$.** As a subgroup of $S_n$ it is itself a group, and being a [[Def - Kernel and Image|kernel]] it is a [[Def - Normal Subgroup|normal subgroup]] of $S_n$. For $n \geq 5$ it is the first family of non-abelian [[Def - Simple Group|simple]] groups; see [[Thm - Simplicity of the Alternating Group]]. Note $A_3 = \{\operatorname{id}, (1\,2\,3), (1\,3\,2)\} \cong C_3$ is cyclic, and $A_4$ has order $12$.

**Is an instance: $\operatorname{Sym}(\mathbb{N})$, the symmetric group of an infinite set.** Bijections of the natural numbers form a group under composition exactly as in the finite case — the definition never used finiteness of $X$. It is an infinite, indeed uncountable, group. It illustrates that "order $n!$" is a fact about $S_n$ specifically, not about symmetric groups in general; cycle notation still describes individual elements but a single permutation may now have infinitely many non-trivial cycles.

**Is NOT an instance: the monoid of all functions $\{1,2,3\} \to \{1,2,3\}$.** There are $3^3 = 27$ such functions, and under composition they form an associative structure with identity $\operatorname{id}$. But this is **not** a symmetric group and not even a group: the constant function $x \mapsto 1$ is not a bijection and has no inverse. The symmetric group $S_3$ is exactly the sub-collection of $6$ bijections among these $27$ functions. This non-example isolates the role of bijectivity: drop it and the inverse axiom dies.

**Is NOT an instance: the rotations of a square, as a purported "$\operatorname{Sym}$".** The four rotations of a square form a group $C_4$, and one is tempted to call it the symmetric group of the four corners. It is not. It is a [[Def - Permutation Group|permutation group]] — a *subgroup* of $S_4$ — but it contains only $4$ of the $4! = 24$ bijections of the corner set; the reflections and the "diagonal swap" permutations are missing precisely because they are not realised by rotations. $\operatorname{Sym}(X)$ means *all* bijections; any proper subcollection is a permutation group, not the symmetric group. This non-example separates the two definitions and is the whole content of why [[Def - Permutation Group]] is a distinct notion.

**Corollary (order of $S_n$).** $|S_n| = n!$. A bijection is built by choosing where $1$ goes ($n$ options), then where $2$ goes among the remaining ($n-1$ options), and so on, giving $n(n-1)\cdots 1 = n!$. *Calibration check:* if you can reproduce this counting argument you have grasped that an element of $S_n$ is data, namely the list of images.

**Corollary (order of $A_n$ for $n \geq 2$).** Since $\operatorname{sgn} : S_n \to \{\pm1\}$ is a surjective [[Def - Homomorphism|homomorphism]] for $n \geq 2$, the [[Thm - First Isomorphism Theorem|first isomorphism theorem]] gives $S_n / A_n \cong \{\pm 1\}$, so $|S_n : A_n| = 2$ and $|A_n| = n!/2$. *Calibration check:* this is the same as observing that, among the $n!$ permutations, exactly half are even — multiplying any odd permutation by a fixed transposition is a bijection between the even and odd ones.

**Corollary (sign of a $k$-cycle).** A $k$-cycle is a product of $k-1$ transpositions, so $\operatorname{sgn}$ of a $k$-cycle is $(-1)^{k-1}$: odd-length cycles are even permutations, even-length cycles are odd. In particular every $3$-cycle is even, which is why $3$-cycles live in $A_n$ and generate it — the starting point of [[Thm - Simplicity of the Alternating Group]].

**Corollary (a permutation's order is the lcm of its cycle lengths).** Disjoint cycles commute and a $k$-cycle has order $k$, so a permutation written as disjoint cycles of lengths $k_1, k_2, \dots$ has order $\operatorname{lcm}(k_1, k_2, \dots)$. *Calibration check:* this shows disjoint cycle notation is not mere bookkeeping — the structure it exposes computes the order directly.

---

# Unlocked by This

> [!tip] Conjugacy Classes of the Symmetric Group *(from Group Theory II, §1.4)*
> Disjoint cycle notation makes the [[Def - Conjugacy Class|conjugacy]] structure of $S_n$ completely transparent: two permutations are conjugate exactly when they have the same **cycle type**, the partition of $n$ recording the cycle lengths. See [[Thm - Conjugacy Classes of the Symmetric Group]].

> [!tip] Determinant and Orientation *(from Linear Algebra)*
> The sign homomorphism $\operatorname{sgn}$ is the combinatorial heart of the determinant: $\det(A) = \sum_{\sigma \in S_n} \operatorname{sgn}(\sigma) \prod_i A_{i,\sigma(i)}$. The well-definedness of parity is exactly what makes the determinant well-defined, and $\operatorname{sgn}$ is what lets a linear map carry a notion of orientation.

> [!tip] Galois Groups and Solvability by Radicals *(from Galois Theory)*
> The Galois group of a degree-$n$ polynomial sits inside $S_n$ as permutations of the roots. Whether the polynomial is solvable by radicals is governed by whether this subgroup is solvable, and the non-solvability of $A_n$ for $n \geq 5$ (via [[Thm - Simplicity of the Alternating Group]]) is exactly why the general quintic is not.
