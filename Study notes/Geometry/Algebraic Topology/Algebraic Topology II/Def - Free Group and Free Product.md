---
type: definition
subject: algebraic-topology
prereqs:
  - "Def - Group"
  - "Def - Homomorphism"
tags: [geometry, algebraic-topology, algebra, group-theory]
---

# Notation

$F_n = F(a_1, \dots, a_n)$ denotes the **free group on $n$ generators** $a_1, \dots, a_n$. For a set $S$, $F(S)$ is the free group on the elements of $S$. For groups $G$ and $H$, $G \ast H$ denotes their **free product**. More generally, for groups $G_i$ ($i \in I$), $\ast_{i \in I} G_i$ is the free product of the $G_i$. A **reduced word** is a sequence $g_1^{\epsilon_1} g_2^{\epsilon_2} \cdots g_n^{\epsilon_n}$ with $g_i$ in the generators, $\epsilon_i \in \{\pm 1\}$, and no two consecutive terms cancelling (i.e., $g_i^{\epsilon_i} g_{i+1}^{\epsilon_{i+1}} \neq 1$). See [[Algebraic Topology II — Fundamental Group and Covering Spaces]] for the full registry.

This is a compound page: it defines **two interlocking notions** — the free group $F_n$ and the free product $G \ast H$ — because they are introduced together (the free group is the free product of $n$ copies of $\mathbb{Z}$) and neither is fully usable without the other.

---

# Axiom Motivation

What we want from a "free" group $F_n$ is the property of being **maximally non-trivial**: we have $n$ generators, and the only relations forced on them are the ones the group axioms force (the unit law, inverses, associativity). No external relation like $ab = ba$ should hold unless we add it explicitly. This is the algebraic analogue of "letting variables vary without constraint."

The defining property — the **universal property** — should be: a homomorphism out of $F_n$ to any group $G$ is the same as a choice of $n$ elements of $G$ (the images of the generators), with no compatibility conditions. Equivalently: given any $n$ elements $g_1, \dots, g_n$ of any group $G$, there is a *unique* homomorphism $F_n \to G$ sending $a_i \mapsto g_i$. This is the cleanest possible "freedom": the group has no internal structure beyond what the universal property demands.

Why phrase it as a universal property? Because it pins down the group up to canonical isomorphism without needing an explicit description. Any group with this universal property is *the* free group. The explicit construction (reduced words) is one realisation; the universal property is the definition.

For the **free product** $G \ast H$, the analogous universal property is: a homomorphism out of $G \ast H$ to any group $K$ is the same as a *pair* of homomorphisms $G \to K$ and $H \to K$ (with no compatibility), i.e., $\mathrm{Hom}(G \ast H, K) = \mathrm{Hom}(G, K) \times \mathrm{Hom}(H, K)$. This makes $G \ast H$ the **coproduct** of $G$ and $H$ in the category of groups — the dual of the direct product, just as the disjoint union of sets is the dual of the Cartesian product.

What goes wrong with the *direct product* $G \times H$? A homomorphism out of $G \times H$ is the same as a pair of *commuting* homomorphisms — the images of $G$ and $H$ in the target must commute element-wise. This commutativity is an extra constraint, and it is what makes the direct product *less free* than the free product. For groups whose generators are not supposed to commute (the fundamental group of a wedge $X \vee Y$), the free product is the right construction.

Explicit construction. The elements of $F_n$ are **reduced words** $w = a_{i_1}^{\epsilon_1} a_{i_2}^{\epsilon_2} \cdots a_{i_k}^{\epsilon_k}$ in the alphabet $\{a_1^{\pm 1}, \dots, a_n^{\pm 1}\}$, where "reduced" means no two consecutive letters are inverse to each other. Multiplication is concatenation followed by reduction (cancel any inverse pairs at the join). The identity is the empty word. Inverses are obtained by reversing the word and inverting each letter. The free product $G \ast H$ is constructed analogously: words are alternating finite sequences of non-identity elements from $G$ and from $H$, with multiplication by concatenation-and-reduction.

The non-trivial fact (the **normal form theorem**) is that reduction terminates and produces a unique reduced word for each group element. This is what makes the construction give a group: distinct reduced words represent distinct elements. The proof is delicate — one common approach is van der Waerden's theorem on partial monoid actions, another is to use the construction as automorphisms of a tree (the Cayley graph) and read off equality from the tree structure.

What if we *strengthened* by imposing commutativity? You get the **free abelian group** $\mathbb{Z}^n$ — every reduced word in $\mathbb{Z}^n$ collapses to a tuple of integers (exponents of each generator). The free abelian group is much smaller than the free group: $|F_2|$ is countably infinite with elements that cannot be simplified, while $|\mathbb{Z}^2|$ is countably infinite with elements simplifying to pairs $(m, n)$. The free abelian group is the abelianisation $F_n^{\mathrm{ab}} = \mathbb{Z}^n$.

What if we *dropped* the uniqueness in the universal property? The construction would no longer be free — there would be multiple ways to realise a given assignment of generators, and the group would not be canonically defined.

---

# The Definition

**Free group on $n$ generators.** The **free group $F_n$** on a set $S = \{a_1, \dots, a_n\}$ is the group whose underlying set is the set of **reduced words** $a_{i_1}^{\epsilon_1} \cdots a_{i_k}^{\epsilon_k}$ ($\epsilon_j \in \{\pm 1\}$, no consecutive cancellations) in the alphabet $\{a_1^{\pm 1}, \dots, a_n^{\pm 1}\}$, with multiplication by concatenation followed by free reduction. The identity is the empty word; inverses are obtained by reversal-and-inversion.

**Universal property.** $F_n$ is uniquely characterised (up to canonical isomorphism) by the following: for every group $G$ and every map of sets $\phi : \{a_1, \dots, a_n\} \to G$, there is a unique group homomorphism $\bar\phi : F_n \to G$ extending $\phi$.

**Free product of two groups.** Given groups $G$ and $H$, their **free product** $G \ast H$ is the group whose elements are **reduced words** $g_1 h_1 g_2 h_2 \cdots g_k h_k$ (or starting with $h$, ending with $g$, etc.), where each $g_i \in G \setminus \{1\}$, each $h_i \in H \setminus \{1\}$, and the letters alternate between $G$ and $H$. Multiplication is concatenation followed by reduction (multiplying adjacent letters from the same group, removing identities). The identity is the empty word.

**Universal property of the free product.** $G \ast H$ is characterised by: for every group $K$ and every pair of homomorphisms $\phi_G : G \to K$, $\phi_H : H \to K$, there is a unique homomorphism $\phi : G \ast H \to K$ with $\phi|_G = \phi_G$ and $\phi|_H = \phi_H$. In categorical language, $G \ast H$ is the **coproduct** of $G$ and $H$ in the category of groups.

**Relating the two constructions.** $F_n = \mathbb{Z} \ast \mathbb{Z} \ast \cdots \ast \mathbb{Z}$ ($n$ copies). Each copy contributes one generator (the generator of $\mathbb{Z}$). So the free group on $n$ generators is the free product of $n$ copies of $\mathbb{Z}$.

**Amalgamated free product.** For groups $G, H$ and a third group $A$ with homomorphisms $A \to G$ and $A \to H$, the **amalgamated free product** $G \ast_A H$ is the quotient of $G \ast H$ by the normal subgroup generated by elements of the form $\phi_G(a) \phi_H(a)^{-1}$ for $a \in A$. It is the **pushout** of $G \leftarrow A \to H$ in the category of groups. This is the construction featured in [[Thm - Seifert-van Kampen Theorem (Statement)|Seifert-van Kampen]].

---

# Categorical / Structural Definition

In the category $\mathbf{Grp}$ of groups, the free group functor $F : \mathbf{Set} \to \mathbf{Grp}$ is the **left adjoint** of the forgetful functor $\mathbf{Grp} \to \mathbf{Set}$. The adjunction says
$$
\mathrm{Hom}_{\mathbf{Grp}}(F(S), G) \cong \mathrm{Hom}_{\mathbf{Set}}(S, \mathrm{underlying-set}(G)).
$$
This *is* the universal property. The free group is the "free object on a set" in $\mathbf{Grp}$, in the same way that the free vector space is the free object on a set in $\mathbf{Vect}$.

The free product $G \ast H$ is the **coproduct** of $G$ and $H$ in $\mathbf{Grp}$, dual to the direct product $G \times H$ (which is the *product*). The universal property of the coproduct is: morphisms out of $G \ast H$ are pairs of morphisms (one from $G$, one from $H$) — no compatibility. By contrast, morphisms out of $G \times H$ are pairs of commuting morphisms — extra compatibility.

The amalgamated free product $G \ast_A H$ is the **pushout** of $G \leftarrow A \to H$. Pushouts in $\mathbf{Grp}$ exist for any pair of maps out of $A$ and produce the universal group "glued" along $A$. The Seifert-van Kampen theorem identifies $\pi_1(X)$ for $X = U \cup V$ as a pushout, leveraging this categorical construction.

---

# Relate to Other Fields / Compression

The free group is the **free object on a set in the category of groups** — the same construction as the free vector space, the free monoid, the free associative algebra, in their respective categories. The pattern is: take a set, allow all formal combinations satisfying the category's axioms, mod out by what those axioms force. The result is the "most non-trivial" object generated by the set.

In topology, $F_n = \pi_1$ of the wedge of $n$ circles. This is why free groups appear naturally: any space that looks like a 1-dimensional cell complex with one vertex and $n$ loops has $F_n$ as its fundamental group. Generalising, a 1-dimensional CW complex has $\pi_1$ a free group (with one generator per loop in a maximal tree complement), and any group is the $\pi_1$ of a 2-dimensional CW complex.

**True name:** the free group is the **set of reduced words modulo no relations**, equivalently the **group with no relations beyond the axioms**, equivalently the **left adjoint to forgetful**, equivalently the **fundamental group of the wedge of circles**. The four characterisations are equivalent, and each is useful in a different context.

---

# Examples / Corollaries

**Is an instance: $F_1 = \mathbb{Z}$.** The free group on one generator is the infinite cyclic group, generated freely by a single generator with no relations. Elements: $a^n$ for $n \in \mathbb{Z}$.

**Is an instance: $F_2 = \langle a, b \rangle$.** The free group on two generators contains *every* finitely generated group as a quotient (every group is a quotient of a free group). It is **non-abelian**: $ab \neq ba$ in $F_2$. Most words like $aba^{-1}b^{-1}a^2bab^{-1}$ do not simplify — the only simplifications are direct inverse cancellations.

**Is an instance: $\mathbb{Z} \ast \mathbb{Z} = F_2$.** The free product of two copies of $\mathbb{Z}$ is the free group on two generators. Words alternate: $a^{n_1}b^{m_1}a^{n_2}b^{m_2}\cdots$ where $a$ generates one $\mathbb{Z}$, $b$ the other.

**Is an instance: $\pi_1(S^1 \vee S^1) = F_2$.** The fundamental group of the figure-eight is the free group on two generators, one for each loop. See [[Ex - The Universal Cover of the Figure-Eight is the Cayley Graph of F_2]].

**Is an instance: $\pi_1(\Sigma_g) = \langle a_1, b_1, \dots, a_g, b_g \mid \prod [a_i, b_i] \rangle$ for a closed orientable surface of genus $g$.** This is a quotient of $F_{2g}$ by the normal subgroup generated by the single commutator relation. So surface groups are "almost free" — close to $F_{2g}$, but with one relation.

**Is an instance: $\mathbb{Z}/2 \ast \mathbb{Z}/2 = D_\infty$, the infinite dihedral group.** Two copies of $\mathbb{Z}/2$ amalgamated freely give the infinite dihedral group, with two generators $a, b$ each of order 2 and no further relations. This is the fundamental group of the Klein bottle minus a point.

**Is an instance: $\mathrm{PSL}_2(\mathbb{Z}) = \mathbb{Z}/2 \ast \mathbb{Z}/3$.** The modular group is the free product of $\mathbb{Z}/2$ and $\mathbb{Z}/3$, with generators of orders 2 and 3 and no further relation. This is one of the most-studied free products outside topology.

**Is NOT an instance: $\mathbb{Z}^n$ is the *free abelian group* on $n$ generators, *not* the free group.** The free group $F_n$ is strictly larger than $\mathbb{Z}^n$: words like $aba^{-1}b^{-1}$ are non-trivial in $F_2$ but equal $0$ in $\mathbb{Z}^2$. The relation is $\mathbb{Z}^n = F_n^{\mathrm{ab}} = F_n / [F_n, F_n]$ — abelianisation kills the difference.

**Is NOT an instance: $\mathbb{Z} \times \mathbb{Z}$ is the *direct product*, not the free product.** $\mathbb{Z} \times \mathbb{Z}$ is abelian; $\mathbb{Z} \ast \mathbb{Z} = F_2$ is non-abelian. The direct product enforces commutativity; the free product does not.

**Is NOT an instance: $\mathbb{Z}/2 \times \mathbb{Z}/2$ is the Klein 4-group, not $\mathbb{Z}/2 \ast \mathbb{Z}/2 = D_\infty$.** Order 4 vs infinite. The first abelianises both generators; the second leaves them free to combine into infinitely many elements.

**Corollary (every group is a quotient of a free group):** for any group $G$ with generating set $S$, there is a surjective homomorphism $F(S) \twoheadrightarrow G$ (by universal property, sending generators to themselves), with kernel $R$ the **relations** of $G$. So $G \cong F(S)/R$, a **presentation**.

**Corollary (subgroup of free group is free — Nielsen-Schreier):** every subgroup of a free group is free. This is non-trivial but true. For $F_n$ and a subgroup of index $k$, the subgroup is free of rank $k(n-1) + 1$.

**Corollary (rank is well-defined):** the number of free generators $n$ is an invariant of $F_n$ — $F_n \cong F_m$ implies $n = m$. Proof: abelianise; $F_n^{\mathrm{ab}} = \mathbb{Z}^n$, and the rank of $\mathbb{Z}^n$ is the dimension of $\mathbb{Z}^n \otimes \mathbb{Q} = \mathbb{Q}^n$.

**Calibration check.** If you can (a) state the universal property of the free group, (b) explain the difference between $F_2$, $\mathbb{Z}^2$, $\mathbb{Z}/2 \ast \mathbb{Z}/2$, and $\mathbb{Z}/2 \times \mathbb{Z}/2$, and (c) write down a reduced word in $F_2$ and verify it does not simplify, you have understood the definition. Bonus: prove (using the universal property only) that $F(\emptyset)$ is the trivial group.

---

# Unlocked by This

> [!tip] Group Presentations *(from Combinatorial Group Theory)*
> Every group has a **presentation** $G = \langle S \mid R \rangle$ — generators $S$ and relators $R$ — corresponding to $G = F(S) / \langle\langle R \rangle\rangle$ where $\langle\langle R \rangle\rangle$ is the normal closure of $R$ in $F(S)$. This is the standard input format for almost all questions in computational group theory. The **word problem** (decide if two words represent the same element) and the **isomorphism problem** (decide if two presentations give isomorphic groups) are both undecidable in general — a deep theorem of Novikov-Boone (word problem) and Adyan-Rabin (isomorphism problem).

> [!tip] Bass-Serre Theory *(from Geometric Group Theory)*
> Free products, amalgamated free products, and **HNN extensions** are the building blocks of **Bass-Serre theory**: every group acting on a tree without inversions decomposes as a free product with amalgamation or an HNN extension along the edge stabilisers. This gives a "tree-of-groups" picture for any group acting on a simply-connected 1-complex, and is the algebraic counterpart of the topological gluing constructions in Seifert-van Kampen.

> [!tip] The Cayley Graph and Geometric Group Theory *(from Geometric Group Theory)*
> The **Cayley graph** of a group $G$ with generating set $S$ is the graph with vertices $G$ and edges $\{(g, gs) : g \in G, s \in S\}$. The Cayley graph of $F_n$ is the $2n$-valent infinite tree; the Cayley graph of $\mathbb{Z}^n$ is the integer lattice. **Geometric group theory** studies groups by the geometry of their Cayley graphs — coarse geometric properties (hyperbolicity, growth rate, ends) become group-theoretic invariants. The universal cover picture for $\pi_1$ is the geometric origin of this subject.
