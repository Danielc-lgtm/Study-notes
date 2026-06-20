---
type: theorem
subject: higher-categories
prereqs:
  - "Def - Unbiased Monoidal Category"
  - "Def - Monoidal Category"
  - "Thm - Mac Lane Coherence Theorem"
  - "Def - Functor"
tags: [category-theory, higher-categories, foundations]
---

# Notation

Let $(\mathcal{C}, (\otimes_n)_{n\geq 0}, \gamma, \iota)$ be an [[Def - Unbiased Monoidal Category|unbiased monoidal category]]: an $n$-ary tensor $\otimes_n : \mathcal{C}^n \to \mathcal{C}$ for each $n$, with $\otimes_0() = I$ the unit, composition isomorphisms $\gamma_{k_1,\dots,k_n}$ comparing nested tensors with flat ones, and a unit isomorphism $\iota : \otimes_1 \cong \mathrm{id}$. A **formal expression** in the objects $A_1, \dots, A_m$ is a term built from those objects by applying the $\otimes_n$ in any nesting; a **canonical map** between two formal expressions is any composite of (instances of) $\gamma^{\pm}$, $\iota^{\pm}$, and identities, applied within larger expressions via the $\otimes_n$. The full registry is on [[Higher Categories — Strict n-Categories and Notions of Monoidal Category]].

---

# Statement

> **Theorem (Coherence, unbiased form).** In any [[Def - Unbiased Monoidal Category|unbiased monoidal category]], every diagram of canonical maps commutes. Equivalently: between any two formal expressions in the same objects $A_1, \dots, A_m$ (in the same order) there is *at most one* canonical map, and it is an isomorphism. Equivalently again, the free unbiased monoidal category on a set $S$ is equivalent to the free *strict* one — the **discrete** unbiased monoidal category whose objects are finite lists from $S$ with concatenation as tensor.

> **Corollary (Mac Lane, biased form).** In any [[Def - Monoidal Category|monoidal category]], every diagram built from associators $\alpha$, unitors $\lambda, \rho$, and identities commutes: see [[Thm - Mac Lane Coherence Theorem]].

The content in one sentence: **all the ways of inserting, removing, and re-bracketing tensors are forced to agree, so "the" canonical comparison between any two parenthesizations is unambiguous.**

---

# Motivation

The reason coherence is the central theorem of monoidal category theory is that without it, the notation is a lie. We routinely write $A \otimes B \otimes C \otimes D$ with no brackets, multiply long strings of objects, and slide units in and out, all as if the tensor were strictly associative and unital. It is not — the associator and unitors are genuine, possibly-nontrivial isomorphisms. The only thing that makes the brackets-free notation honest is the guarantee that *however* you reinsert the brackets and *whatever* sequence of associators and unitors you use to compare two bracketings, you get the **same** map. Coherence is exactly that guarantee.

The unbiased formulation is what makes the guarantee transparent. In the biased world, coherence is a real theorem with a real proof, because the binary tensor over-generates: there are many distinct formal composites of associators between two bracketings, and one must prove they coincide. In the unbiased world, the $\otimes_n$ are primitive and there is **one operation per arity**, so the "many composites" collapse: any canonical map between two expressions with the same leaves is determined by where the leaves go, and there is only one way for them to go. The motivation for studying the unbiased version is precisely this — it relocates coherence from a hard theorem to a near-tautology, and then the biased theorem is recovered by the equivalence of the two presentations.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal input is "an unbiased monoidal category and two formal expressions." The recognition skill is spotting when a problem is secretly asking whether two tensor-comparison maps agree.

The first disguised source is **a computation in a [[Def - Monoidal Category|monoidal category]] involving a string of associators and unitors**. Any time you have two different routes between the same two bracketed tensors — and you want to assert they are equal *without* checking by hand — you are invoking coherence. The non-obvious step is recognising that the messy associator computation never needs to be done: coherence does it. *Example problem:* in a monoidal category, prove that the two evident maps $((A\otimes B)\otimes C)\otimes D \to A\otimes(B\otimes(C\otimes D))$ are equal, by observing both are canonical and citing coherence.

The second disguised source is **a structure on which a tensor is defined by a universal property** (the $n$-fold [[Def - Tensor Product of Vector Spaces|tensor product]], an $n$-fold [[Def - Limit and Colimit|limit]]). The comparison maps are canonical maps of representing objects, so coherence guarantees they assemble unambiguously. The non-obviousness is that universal-property maps are *automatically* the unique canonical maps, so coherence is free here. *Example problem:* show that the canonical iso $(U\otimes V)\otimes W \cong U \otimes (V \otimes W \otimes X)\otimes\cdots$ in $\mathbf{Vect}_k$ assembled in two ways agrees, by uniqueness from the multilinear universal property — which is the concrete shadow of coherence.

The third disguised source is **a string-diagram or pasting computation**. In string-diagram calculus the associators and unitors are *invisible* (the wires are drawn without brackets), and the legitimacy of that invisibility is coherence. The non-obvious recognition is that every string-diagram manipulation tacitly uses coherence to ignore the bracketing. *Example problem:* justify that a string diagram of three composable processes has a well-defined value independent of how it is parsed into binary tensors.

**Targets (Output Amplification)**

The bare conclusion is "every canonical diagram commutes." Combined with other facts it does a great deal of work.

Combine coherence with **the biased/unbiased equivalence**. Transporting unbiased coherence across [[Thm - Biased and Unbiased Monoidal Categories Coincide|the equivalence]] yields [[Thm - Mac Lane Coherence Theorem|Mac Lane's biased coherence theorem]] — every diagram of $\alpha, \lambda, \rho$ commutes. This is the standard modern proof of biased coherence and the reason the unbiased theory is developed first. The combination is nonobvious because it produces a famous hard theorem from a near-trivial one by a change of presentation.

Combine coherence with **the freeness of bracketing-free notation**. Coherence licenses writing $\otimes_n$ for any tensor of $n$ objects and treating all bracketings as literally equal "up to the canonical iso," which is the everyday practice of working with monoidal categories. The further result is the practical theorem that one may *define* maps and structures (e.g. a monoid's multiplication, a Hopf algebra's antipode) using bracket-free expressions and they are automatically well-defined.

Combine coherence with **strictification**. Coherence is the key input to [[Thm - Strictification of Monoidal Categories|strictification]]: because all canonical diagrams commute, one can replace a monoidal category by an equivalent one in which the canonical comparisons *are* identities. The target is the working principle "every monoidal category may be assumed strict," which removes coherence bookkeeping from essentially all calculations.

---

# Why Is It True

The mechanism is the cleanest in the whole chapter. **In the free unbiased monoidal category, a formal expression is just a rooted planar tree whose leaves are the objects in order, and a canonical map is a way of reshaping one tree into another; coherence holds because the As operad has exactly one operation of each arity, so any two reshapings with the same leaf sequence are the same operation.**

Unpack this. A formal expression like $\otimes_2(\otimes_3(A,B,C), \otimes_1(D))$ is a tree: a root with two children, the first child an arity-$3$ node over leaves $A, B, C$, the second an arity-$1$ node over $D$. The $\gamma$'s are exactly the moves that contract or expand internal edges of the tree (composing a node with the nodes above it), and $\iota$ deletes arity-$1$ nodes. A canonical map is a sequence of such moves taking one tree to another. Now the key point: every tree with leaves $A_1, \dots, A_m$ (in order) can be contracted to the single arity-$m$ "corolla" — one node directly over all $m$ leaves — by repeatedly applying $\gamma$. So any two trees with the same leaves are both canonically isomorphic to the corolla, and the unbiased *associativity axiom* says that the contraction to the corolla is independent of the order of contractions. Therefore the canonical map from one tree to another is forced: go up to the corolla, come back down, and the axiom guarantees uniqueness. There is *at most one* canonical map because there is only one arity-$m$ operation to factor through.

This is why the unbiased axioms are so few. The pentagon, in the biased world, is the special case "the two ways of contracting a length-four left-comb to the corolla agree." Mac Lane needed it as a hypothesis because the binary presentation cannot see the corolla directly; the unbiased presentation has the corolla ($\otimes_m$) as primitive, so the pentagon is automatic.

A useful slogan: every parenthesization of a list is canonically the *flat* list, and "canonically" means "in exactly one way" — that one way is $\gamma$.

---

# What Makes This Hard

The difficulty is almost entirely conceptual, not computational. The non-obvious step is realising that one must prove there is *at most one* canonical map, not merely that canonical maps exist — existence is easy (compose $\gamma$'s), uniqueness is the theorem. Beginners conflate the two and think coherence is trivial because they can always *write down* a comparison; the content is that any two such comparisons coincide. The second subtlety, which trips up the biased version, is the **unit**: maps involving $\iota$ and the empty tensor $\otimes_0$ create degenerate cases (inserting and deleting units) that must be handled alongside the associativity moves, and the original proofs of Mac Lane coherence had a gap precisely here. In the unbiased setting the unit is just the arity-$0$ node and the unit coherence axiom dispatches it uniformly, which is one more reason the unbiased proof is cleaner.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Reduce to the free unbiased monoidal category on a set $S$. Show every formal expression (tree) is canonically isomorphic, via $\gamma$, to the flat tensor of its leaves (the corolla), and that this isomorphism is *unique* by the associativity coherence axiom. Then any two expressions with the same leaf list have a unique canonical iso between them, factoring through the corolla. The general (non-free) case follows because the unique-up-to-canonical-iso structure is preserved by the unique strict-monoidal functor out of the free one.

**Subgoal decomposition:**

1. **Reduce to the free case.** It suffices to prove the statement in the free unbiased monoidal category $F(S)$ on a set $S$.
   - *Hint:* Any unbiased monoidal category receives a unique structure-preserving functor from $F(S)$ for $S$ = its objects; a diagram commutes if its preimage does.
   - *Why needed:* It replaces an arbitrary category by a combinatorial one made of trees.

2. **Identify expressions with trees and canonical maps with reshapings.** Formal expressions = rooted planar trees with leaves labelled by $S$ in order; $\gamma$ = edge contraction/expansion; $\iota$ = deletion of arity-$1$ nodes.
   - *Hint:* Draw a few; an arity-$n$ tensor is an $n$-ary node.
   - *Why needed:* It makes "canonical map" a finite combinatorial object you can reason about.

3. **Every tree contracts canonically to the corolla.** Repeatedly applying $\gamma$ collapses any tree on leaves $A_1, \dots, A_m$ to the single arity-$m$ node $\otimes_m(A_1, \dots, A_m)$.
   - *Hint:* Contract internal edges from the top down; each contraction is one $\gamma$.
   - *Why needed:* It provides a common target through which all canonical maps factor.

4. **The contraction is unique — invoke the associativity axiom.** Any two sequences of $\gamma$'s contracting a tree to its corolla give the same isomorphism.
   - *Hint:* This is exactly the two-stage = one-stage associativity coherence axiom of the unbiased structure.
   - *Why needed:* Uniqueness of the contraction forces uniqueness of every canonical map.

5. **Conclude at most one canonical map.** Between two trees with the same leaves, the only canonical map is (contract first to corolla) followed by (expand to the second), and it is unique and invertible.
   - *Hint:* Compose the unique contraction of the source with the inverse of the unique contraction of the target.
   - *Why needed:* "At most one canonical map" is the theorem; isomorphism is automatic since $\gamma, \iota$ are isos.

---

# Lemma Decomposition

> [!note]- Lemma 1: Reduction to the free unbiased monoidal category
> **Statement:** If every diagram of canonical maps commutes in the free unbiased monoidal category $F(S)$ on every set $S$, then it commutes in every unbiased monoidal category.
>
> **Hint:** Use the universal property of $F(S)$: a structure-preserving functor $F(S) \to \mathcal{C}$ is determined by a function $S \to \mathrm{ob}\,\mathcal{C}$, and it sends canonical maps to canonical maps.
>
> **Why needed:** It turns the problem into pure combinatorics of trees (subgoal 1).
>
> > [!note]- Full proof
> > Let $\mathcal{C}$ be unbiased monoidal and let $D$ be a diagram of canonical maps among formal expressions in objects $A_1, \dots, A_m \in \mathcal{C}$. Let $S = \{x_1, \dots, x_m\}$ and let $H : F(S) \to \mathcal{C}$ be the unique strict-monoidal-structure-preserving functor with $H(x_i) = A_i$ (existence and uniqueness are the universal property of the free unbiased monoidal category). Each formal expression in $\mathcal{C}$ is $H$ of the corresponding expression in $F(S)$, and each canonical map in $\mathcal{C}$ is $H$ of a canonical map in $F(S)$, because $H$ preserves $\gamma$ and $\iota$. If the corresponding diagram in $F(S)$ commutes, applying $H$ shows $D$ commutes. Hence the free case implies the general case.
>
> [!note]- Lemma 2: Canonical contraction to the corolla
> **Statement:** In $F(S)$, every formal expression $E$ with leaf list $(A_1, \dots, A_m)$ admits a canonical isomorphism $c_E : E \xrightarrow{\cong} \otimes_m(A_1, \dots, A_m)$ built from $\gamma$ and $\iota$.
>
> **Hint:** Induct on the height of the tree; contract the topmost node into its parent using one $\gamma$, then recurse.
>
> **Why needed:** It exhibits the common target (the corolla) through which all canonical maps will factor (subgoal 3).
>
> > [!note]- Full proof
> > Induct on the number of internal nodes of the tree representing $E$. If $E = \otimes_m(A_1, \dots, A_m)$ is already a corolla, take $c_E = \mathrm{id}$. Otherwise the root is $\otimes_n(E_1, \dots, E_n)$ with each $E_j$ an expression of leaf list $\vec A^j$ and fewer nodes; by induction each has $c_{E_j} : E_j \cong \otimes_{k_j}(\vec A^j)$. Apply $\otimes_n$ of these to get $E \cong \otimes_n(\otimes_{k_1}(\vec A^1), \dots, \otimes_{k_n}(\vec A^n))$, then apply $\gamma_{k_1,\dots,k_n}$ to land at $\otimes_{m}(A_1, \dots, A_m)$ where $m = \sum k_j$. Arity-$1$ nodes are removed by $\iota$. The composite is canonical and invertible.
>
> [!note]- Lemma 3: Uniqueness of the contraction
> **Statement:** The canonical isomorphism $c_E : E \cong \otimes_m(\vec A)$ of Lemma 2 is independent of all choices: any canonical map $E \to \otimes_m(\vec A)$ equals $c_E$.
>
> **Hint:** Two contraction orders differ by an instance of the two-stage versus one-stage associativity coherence axiom.
>
> **Why needed:** Uniqueness is the entire theorem; without it, "at most one canonical map" fails (subgoal 4).
>
> > [!note]- Full proof
> > Any canonical map $E \to \otimes_m(\vec A)$ is a composite of $\gamma$'s and $\iota$'s contracting $E$ to the corolla (an expansion step would increase node count and cannot end at the corolla, except as cancelled by a later contraction; by invertibility we may assume the composite is reduced and purely contracting). Two reduced contractions differ by reordering which internal edge is contracted first. Each such reordering is precisely an instance of the unbiased **associativity coherence** axiom (contracting a doubly-nested expression in two stages versus one) together with **unit coherence** for the $\iota$ steps. By those axioms the two composites are equal. Hence all canonical contractions of $E$ coincide; call the common value $c_E$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 — what must be shown.** We prove: between any two formal expressions $E, E'$ in $F(S)$ with the same leaf list $(A_1, \dots, A_m)$ there is exactly one canonical map, and it is an isomorphism. By Lemma 1 this suffices for all unbiased monoidal categories, and "exactly one" is precisely "every diagram of canonical maps commutes."
>
> **Step 1 — existence.** By Lemma 2, there are canonical isomorphisms $c_E : E \cong \otimes_m(\vec A)$ and $c_{E'} : E' \cong \otimes_m(\vec A)$. Then $c_{E'}^{-1} \circ c_E : E \to E'$ is a canonical isomorphism, so at least one canonical map exists.
>
> **Step 2 — uniqueness.** Let $\phi : E \to E'$ be any canonical map. Then $c_{E'} \circ \phi : E \to \otimes_m(\vec A)$ is a canonical map to the corolla. By Lemma 3 (uniqueness of the contraction), $c_{E'} \circ \phi = c_E$. Therefore $\phi = c_{E'}^{-1} \circ c_E$, the map of Step 1. So the canonical map is unique.
>
> **Step 3 — it is an isomorphism.** $c_{E'}^{-1}\circ c_E$ is a composite of $\gamma$'s and $\iota$'s, all of which are isomorphisms by definition of an unbiased monoidal category; hence it is an isomorphism.
>
> **Step 4 — conclude.** Every diagram of canonical maps among expressions with a fixed leaf list commutes, because all its edges and composites are *the* unique canonical map between their endpoints. By Lemma 1 this holds in every unbiased monoidal category. Finally, the biased corollary follows by transporting along [[Thm - Biased and Unbiased Monoidal Categories Coincide|the equivalence with biased monoidal categories]]: the associator and unitors are canonical maps, so every diagram built from them commutes, which is [[Thm - Mac Lane Coherence Theorem|Mac Lane's coherence theorem]]. $\qquad \blacksquare$

---

# Cross-Field Exercise Suggestions

**Combinatorics — counting bracketings and the associahedron.** The bracketings of an $(n+1)$-fold product are counted by the Catalan number $C_n$, and the associativity pentagon is the $2$-dimensional **associahedron** $K_4$; coherence says the whole associahedron $K_n$ (whose vertices are bracketings and edges are single associators) becomes a single point after passing to the unbiased corolla. Recognising the pentagon as a face of a polytope is a nonobvious geometric reading of coherence.

**Computer science — normalization of parse trees.** A canonical contraction to the corolla is exactly a *normal form* for a parse tree under the associativity rewrite, and Lemma 3 is a confluence (Church–Rosser) statement for that rewriting system. The application is nonobvious: coherence is a confluence theorem in disguise, and the unbiased axiom is the critical-pair lemma.

**Physics — string diagrams and tensor networks.** In a [[Def - Monoidal Category|monoidal category]] modelling a physical process theory, tensor-network and string-diagram calculations draw wires with no brackets; coherence is the precise statement that this is legitimate, so any two parsings of a network compute the same operator. Recognising that every tensor-network identity silently invokes coherence broadens where the theorem applies.

---

# Bridges

- **[[Thm - Mac Lane Coherence Theorem|Mac Lane's coherence theorem]]** — the biased corollary. Mac Lane proved that in a [[Def - Monoidal Category|monoidal category]] every diagram of associators and unitors commutes; the unbiased theorem is the same statement with the binary bias removed, and Mac Lane's version is recovered by transporting along [[Thm - Biased and Unbiased Monoidal Categories Coincide|biased = unbiased]]. The unbiased proof is cleaner because there is one operation per arity, so "at most one canonical map" is immediate.

- **[[Thm - Strictification of Monoidal Categories|Strictification]]** — the operational payoff. Coherence is exactly what is needed to replace a monoidal category by an equivalent strict one: all canonical comparisons commute, so they can be made into identities. "Coherence $\Rightarrow$ may assume strict" is the working mathematician's use of this theorem.

- **[[Def - Unbiased Monoidal Category|The unbiased definition]]** — the source of the simplicity. The whole reason coherence is near-trivial here is the design of the unbiased structure: by taking $\otimes_n$ primitive (one corolla per arity) and demanding only associativity-of-$\gamma$, the theorem is built into the definition. The bridge runs both ways: the definition is engineered so that this theorem is easy.

---

# Unlocked by This

> [!tip] Coherence for All Higher Structures *(from Higher Category Theory)*
> The same tree-contraction argument proves coherence for **braided** and **symmetric** monoidal categories (replace planar trees by braided/symmetric ones), for **bicategories**, and underlies coherence for **tricategories**. The slogan "take all arities primitive and coherence is the operad's associativity" is the general method.

> [!tip] Operads as the Bookkeeping of Coherence *(from Algebra)*
> Coherence theorems are statements that a category is an algebra for a particular operad with contractible spaces of operations. The As operad (one operation per arity) gives monoidal coherence; the $E_\infty$ operad (contractible operation spaces) gives symmetric-monoidal coherence "up to homotopy," the gateway to **$E_\infty$-algebras** and **derived** multiplicative structures.
