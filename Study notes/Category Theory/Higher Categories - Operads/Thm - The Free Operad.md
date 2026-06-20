---
type: theorem
subject: higher-categories
prereqs:
  - "Def - Operad"
  - "Def - Algebra for an Operad"
  - "Thm - Operads as Monoids in Symmetric Sequences"
  - "Def - Adjunction"
tags: [category-theory, higher-categories, foundations]
---

# Notation

A **symmetric sequence** $E$ assigns to each $n \geq 0$ an object $E(n)$ with a right $S_n$-action; $E(n)$ is thought of as a set (or space, or vector space) of "generating operations of arity $n$". An **(abstract, rooted) tree** with leaves labelled $1, \dots, n$ is a finite rooted tree whose internal vertices each have a set of incoming edges (children) and one outgoing edge; the leaves are the inputs, the root edge is the output. A **$E$-labelled tree** decorates each internal vertex $v$ of arity $|v|$ (number of children) with an element of $E(|v|)$. The **free operad** on $E$ is written $\mathcal{F}(E)$, and the forgetful functor sending an [[Def - Operad|operad]] to its underlying symmetric sequence is $U : \mathrm{Operad}(\mathcal{V}) \to \mathrm{SymSeq}(\mathcal{V})$. The composition product on symmetric sequences (see [[Thm - Operads as Monoids in Symmetric Sequences]]) is $\circ$, with unit $I$. The full notation registry is on [[Higher Categories — Operads and Multicategories]].

---

# Statement

> **Theorem (the free operad).** Let $(\mathcal{V}, \otimes, \mathbb{1})$ be a symmetric monoidal category with countable coproducts over which $\otimes$ distributes (for example $\mathbf{Set}$, $\mathbf{Vect}_k$, $\mathbf{Top}$, or chain complexes). The forgetful functor $U : \mathrm{Operad}(\mathcal{V}) \to \mathrm{SymSeq}(\mathcal{V})$ has a left adjoint $\mathcal{F} : \mathrm{SymSeq}(\mathcal{V}) \to \mathrm{Operad}(\mathcal{V})$, the **free operad** functor. Explicitly, for a symmetric sequence $E$,
> $$\mathcal{F}(E)(n) \;=\; \coprod_{\substack{T \text{ a rooted tree} \\ \text{with } n \text{ leaves}}} \Big( \bigotimes_{v \in T} E(|v|) \Big)\Big/ \sim,$$
> the coproduct over isomorphism classes of $E$-labelled rooted trees with $n$ leaves; operadic composition is **grafting** of trees (attach the root of each $T_i$ to the $i$th leaf of $T$), the unit is the trivial tree (one edge, no internal vertices), and the $S_n$-action permutes the leaf labels. The adjunction unit $\eta_E : E \to U\mathcal{F}(E)$ includes $E(n)$ as the corollas (trees with a single internal vertex of arity $n$).

> **Corollary (universal property).** For any operad $P$, operad morphisms $\mathcal{F}(E) \to P$ are in natural bijection with maps of symmetric sequences $E \to U(P)$: to specify an operad map out of the free operad is to specify, for each generating operation in $E(n)$, an arbitrary operation in $P(n)$, with no constraints.

---

# Motivation

Every algebraic theory worth its name has a notion of "free object": the free group on a set, the free module, the free monoid. The free object is the one with *no relations* — it contains exactly the elements its generators force and nothing more, and its defining feature is a universal property: maps out of it are determined freely by where the generators go. The free operad is this notion for operads. It answers: given a bag of generating operations — a binary operation here, a ternary one there — what is the operad they generate when you are allowed to compose them freely but impose no equations?

The answer is *trees*, and this is the conceptual payoff. Composing operations means plugging outputs into inputs, and a record of "which operation was plugged into which slot of which operation" is exactly a rooted tree with the operations sitting at the vertices. With no relations, two such composites are equal precisely when their trees are isomorphic — nothing collapses them. So the free operad on a set of generators is the set of all formal nestings of those generators, organised by tree shape. This is the operadic generalisation of "the free monoid on $X$ is the set of finite words in $X$": a word is a height-$1$ tree (a linear list), and a general tree is the branching version that arises once operations can have more than one input.

Why does this matter beyond aesthetics? Because *every* operad is a quotient of a free one (present it by generators and relations), and free operads are the cofibrant building blocks for operadic homotopy theory. The free operad is also the syntactic engine of universal algebra: $E$-labelled trees are the *terms* of a multi-sorted theory, and the free operad is the operad of terms before any axioms are imposed. Quotienting by the axioms then yields the operad governing the actual theory. So the free operad is both the source of all presentations and the home of pure syntax.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's hypothesis is "$E$ is a symmetric sequence", but the situations that call for it are recognised by the presence of *generators without imposed relations*.

The first disguised source is **an algebraic structure given by a presentation: generating operations and defining equations**. Whenever a structure is described as "a binary product satisfying associativity" or "a bracket satisfying Jacobi", the generators form a symmetric sequence $E$, and the structure's operad is $\mathcal{F}(E)/(\text{relations})$. The free operad is the first half of every such presentation. *Example problem:* present the associative operad as $\mathcal{F}(E)/R$ where $E$ has a single binary generator $\mu$ (so $E(2) = \{\mu\}$, $E(n) = \varnothing$ otherwise) and $R$ is generated by $\mu \circ_1 \mu = \mu \circ_2 \mu$ (associativity of the two height-$2$ binary trees).

The second disguised source is **a recursive or inductive data structure**. Lists, binary trees, syntax trees, and more generally the elements of any "free" inductive type are built by repeatedly applying constructors, and constructors of various arities are exactly a symmetric (or non-symmetric) sequence of generators. The set of all such structures is $\mathcal{F}(E)$ evaluated at the inputs. *Example problem:* show that binary trees with $n$ labelled leaves are $\mathcal{F}(E)(n)$ for $E$ the non-symmetric sequence with one binary generator, and read off the Catalan-number count of arity-$n$ operations.

The third disguised source is **a free algebra you want to describe**. The free $P$-algebra functor for any operad $P$ is $X \mapsto T_P(X) = \coprod_n P(n) \otimes_{S_n} X^{\otimes n}$, and when $P = \mathcal{F}(E)$ is itself free, $T_{\mathcal{F}(E)}(X)$ is the algebra of *all formal expressions* in the generators applied to elements of $X$ — the free algebra of the corresponding theory before relations. *Example problem:* describe the free magma (free non-associative algebra) on a set $X$ as $T_{\mathcal{F}(E)}(X)$ for the one-binary-generator $E$, recovering "all binary bracketings of words in $X$".

**Targets (Output Amplification)**

The conclusion gives a left adjoint $\mathcal{F}$ with the tree description and the universal property. Combined with further structure it does more.

Combine the universal property with **a chosen target operad $P$ and chosen operations in it**. Since operad maps $\mathcal{F}(E) \to P$ are just maps of generators $E \to U(P)$, the free operad is the machine that *builds operad morphisms with no coherence checking*: pick where each generator goes and the morphism exists automatically. The nonobvious result is that verifying a complicated family of operations assembles into a morphism of operads reduces to choosing the generators' images — all compatibility is handled by the freeness. This is how one constructs maps *into* the endomorphism operad, i.e. algebra structures, on the nose.

Combine $\mathcal{F}$ with **a coequaliser presenting relations**. Any operad $P$ is the coequaliser of a pair of maps $\mathcal{F}(R) \rightrightarrows \mathcal{F}(E)$ encoding generators $E$ and relations $R$; this is the operadic analogue of a group presentation $\langle \text{gens} \mid \text{rels}\rangle$. The nonobvious payoff is that the entire operad is reconstructed from two symmetric sequences and two parallel maps, which is the starting point for computing operadic (co)homology and for Koszul duality.

Combine $\mathcal{F}$ with the **monad of the adjunction $\mathcal{F} \dashv U$**. The adjunction $\mathcal{F} \dashv U$ generates a monad on $\mathrm{SymSeq}$ whose algebras are operads; the free operad is its free algebra. The nonobvious result is that "operad" is itself an algebra-over-a-monad notion (a monad on symmetric sequences), so the bar resolution of an operad — used to define $A_\infty$ and $E_\infty$ — is the monadic bar resolution of the adjunction $\mathcal{F} \dashv U$, with $\mathcal{F}$ supplying the free replacements at each stage.

---

# Why Is It True

The whole theorem is an instance of a single template: *the free monoid in a monoidal category is the sum of tensor powers of the generator, and operads are monoids in $(\mathrm{SymSeq}, \circ, I)$, so the free operad is the sum of $\circ$-powers of $E$.* Once you accept that operads are monoids ([[Thm - Operads as Monoids in Symmetric Sequences|the previous theorem]]), the existence and shape of the free operad is forced.

Recall the free monoid. In an ordinary monoidal category, the free monoid on an object $M$ — when it exists — is
$$\mathrm{FreeMon}(M) = \coprod_{n \geq 0} M^{\otimes n} = I \sqcup M \sqcup (M \otimes M) \sqcup \dots,$$
with multiplication by concatenation: $M^{\otimes a} \otimes M^{\otimes b} \to M^{\otimes(a+b)}$. The universal property is exactly that a monoid map out of it is determined by where $M$ goes, freely. Now run this *verbatim* in $(\mathrm{SymSeq}, \circ, I)$ with $M = E$:
$$\mathcal{F}(E) = \coprod_{n \geq 0} E^{\circ n} = I \sqcup E \sqcup (E \circ E) \sqcup (E \circ E \circ E) \sqcup \dots$$

So the free operad is the sum of iterated composition products of $E$. The only thing left is to see what $E^{\circ n}$ *is* combinatorially — and that is where the trees come from.

> **Iterating the composition product is iterating substitution, and a record of $n$-fold nested substitution is exactly a rooted tree of height $n$ with the generators at its vertices.**

Look at the terms. $I$ is the trivial tree (one edge, no vertices) — the unit operation. $E$ is the corollas — single-vertex trees, one generator with its leaves. $E \circ E$ is "an $E$-operation with each slot filled by an $E$-operation" — height-$2$ trees, a generator at the root with generators at the next level. $E \circ E \circ E$ is height-$3$, and so on. The coproduct $\coprod_n E^{\circ n}$ collects trees of all heights, and reorganising by *number of leaves* rather than by height gives the stated formula $\mathcal{F}(E)(n) = \coprod_T \bigotimes_v E(|v|)$ over trees with $n$ leaves. Grafting trees is concatenation of $\circ$-words, which is the monoid multiplication, i.e. the operadic composition. And there are no relations because nothing in the free-monoid construction identifies distinct words — distinct trees stay distinct.

The universal property is then the free-monoid universal property translated: a monoid (operad) map out of $\coprod_n E^{\circ n}$ is determined by its restriction to the generators $E$, with the higher terms forced by multiplicativity (grafting). That is precisely "an operad map $\mathcal{F}(E) \to P$ is a map of symmetric sequences $E \to U(P)$".

---

# What Makes This Hard

The conceptual leap is easy once operads are monoids; the technical difficulty is **the convergence and well-definedness of the tree construction**, and the bookkeeping of the symmetric group actions on trees. Concretely, two issues trip people. First, the coproduct is over *isomorphism classes* of trees, and one must take the automorphisms of a tree into account: when $\mathcal{V} = \mathbf{Vect}_k$ or chain complexes, a tree with a symmetry contributes its labelling-object's coinvariants under that symmetry, not the bare tensor product, so $\mathcal{F}(E)(n)$ is $\bigoplus_T (\bigotimes_v E(|v|))_{\mathrm{Aut}(T)}$ — forgetting the automorphism quotient is the standard error. Second, the existence of the free monoid in $(\mathrm{SymSeq}, \circ, I)$ is *not* automatic because $\circ$ does not preserve all colimits in its right variable; one needs the distributivity hypothesis on $\mathcal{V}$ to guarantee that $\coprod_n E^{\circ n}$ is genuinely the free monoid (and that the multiplication, defined level by level, converges). The non-obvious step is recognising that the height-$n$ pieces $E^{\circ n}$ assemble without overlap precisely because grafting strictly increases the number of vertices.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Quote that operads are monoids in $(\mathrm{SymSeq}, \circ, I)$; build the free monoid there as $\coprod_n E^{\circ n}$; identify $E^{\circ n}$ with height-$\leq n$ labelled trees so that the total is "all $E$-labelled rooted trees"; verify grafting is the monoid multiplication; and read off the universal property as the free-monoid universal property.

**Subgoal decomposition:**

1. **Reduce to free monoids.** Use [[Thm - Operads as Monoids in Symmetric Sequences|operads = monoids in SymSeq]] to restate "free operad on $E$" as "free monoid on the symmetric sequence $E$ for the product $\circ$".
   - *Hint:* Free objects for a forgetful functor are computed in the algebraic structure; the algebraic structure here is "monoid in $(\mathrm{SymSeq}, \circ, I)$".
   - *Why needed:* It converts an operad construction into a known monoidal construction.

2. **Construct the free monoid as a sum of $\circ$-powers.** Set $\mathcal{F}(E) = \coprod_{n \geq 0} E^{\circ n}$ with concatenation multiplication, and verify the distributivity hypothesis makes this converge and be associative/unital.
   - *Hint:* Multiplication $E^{\circ a} \circ E^{\circ b} \to E^{\circ(a+b)}$ is the identity after reassociating; the unit is the $n = 0$ term $E^{\circ 0} = I$.
   - *Why needed:* This is the actual object; everything else is interpretation.

3. **Identify $E^{\circ n}$ with labelled trees.** Show by induction that an element of $E^{\circ n}$ is an $E$-labelled rooted tree of height $n$ (with leaves), and that $\coprod_n E^{\circ n}$ collects all $E$-labelled rooted trees, regraded by leaf count.
   - *Hint:* $E \circ (-)$ adds one layer of generators at the root; iterating builds the tree top-down. Track the $S_n$-action on leaves through the inductions in $\circ$.
   - *Why needed:* It produces the explicit tree formula and exposes the $\mathrm{Aut}(T)$ coinvariants.

4. **Verify grafting is the operad composition.** Show the monoid multiplication, read in tree terms, is grafting trees onto leaves, and the unit is the trivial tree.
   - *Hint:* Concatenating $\circ$-words corresponds to attaching the root of one tree to a leaf of another.
   - *Why needed:* Confirms the operad structure matches the claimed one.

5. **Establish the universal property / adjunction.** Show operad maps $\mathcal{F}(E) \to P$ correspond to symmetric-sequence maps $E \to U(P)$, naturally, giving $\mathcal{F} \dashv U$.
   - *Hint:* A monoid map out of a free monoid is determined by its value on generators; the higher trees are forced by multiplicativity (grafting), with no constraints because there are no relations.
   - *Why needed:* The universal property is the theorem's usable content.

---

# Lemma Decomposition

> [!note]- Lemma 1: Free monoids for $\circ$ are sums of $\circ$-powers
> **Statement:** In a monoidal category $(\mathcal{A}, \otimes, I)$ with countable coproducts over which $\otimes$ distributes on both sides, the free monoid on an object $M$ exists and equals $\coprod_{n \geq 0} M^{\otimes n}$, with multiplication by concatenation and unit the $n=0$ summand.
>
> **Hint:** Define multiplication summand-wise $M^{\otimes a} \otimes M^{\otimes b} \cong M^{\otimes(a+b)}$; associativity and unitality are immediate from those of $\otimes$. For freeness, extend a map $M \to N$ to $M^{\otimes n} \to N^{\otimes n} \to N$ using the monoid structure of $N$.
>
> **Why needed:** This is the general fact specialised in the proof to $\mathcal{A} = \mathrm{SymSeq}$, $\otimes = \circ$.
>
> > [!note]- Full proof
> > Let $F = \coprod_n M^{\otimes n}$. Distributivity gives $F \otimes F = \coprod_{a,b} M^{\otimes a} \otimes M^{\otimes b} = \coprod_{a,b} M^{\otimes(a+b)}$, and the fold map onto $\coprod_c M^{\otimes c}$ (sending the $(a,b)$ summand to $c = a+b$) is the multiplication $\mu$. Associativity of $\mu$ reduces to $M^{\otimes a} \otimes M^{\otimes b} \otimes M^{\otimes c} \cong M^{\otimes(a+b+c)}$ computed two ways, equal by associativity of $\otimes$. The unit is the inclusion of $M^{\otimes 0} = I$. Given a monoid $(N, m, e)$ and a map $f : M \to N$, define $\bar f$ on $M^{\otimes n}$ as the composite $M^{\otimes n} \xrightarrow{f^{\otimes n}} N^{\otimes n} \xrightarrow{m^{(n)}} N$ (iterated multiplication, with $\bar f|_{M^{\otimes 0}} = e$); this is the unique monoid map restricting to $f$, since multiplicativity forces its value on every $M^{\otimes n}$.

> [!note]- Lemma 2: $E^{\circ n}$ is the symmetric sequence of $E$-labelled trees of height $n$
> **Statement:** For a symmetric sequence $E$, the $n$-fold composition power $E^{\circ n}$ is naturally isomorphic to the symmetric sequence whose arity-$m$ part is $\coprod_{T} (\bigotimes_{v \in T} E(|v|))_{\mathrm{Aut}(T)}$, summed over (iso classes of) rooted trees $T$ of height exactly $n$ with $m$ leaves.
>
> **Hint:** Induct on $n$. $E^{\circ 1} = E$ is the corollas (height $1$). $E^{\circ(n+1)} = E \circ E^{\circ n}$ adds one generator-layer at the root of each height-$n$ tree.
>
> **Why needed:** It converts the abstract $\circ$-powers into the explicit tree description and exhibits the automorphism coinvariants.
>
> > [!note]- Full proof
> > Base case $n = 1$: $E^{\circ 1} = E$, and a single generator of arity $m$ is a corolla (one internal vertex, $m$ leaves), height $1$; the $S_m$-action on $E(m)$ is the leaf relabelling. Inductive step: $E^{\circ(n+1)}(m) = (E \circ E^{\circ n})(m) = \coprod_k E(k) \otimes_{S_k} \mathrm{Ind}\big(\bigotimes_{i=1}^k E^{\circ n}(m_i)\big)$ over $m_1 + \dots + m_k = m$. By induction each $E^{\circ n}(m_i)$ is a sum over height-$n$ trees with $m_i$ leaves; the outer $E(k)$ is a root vertex of arity $k$, and grafting the $k$ height-$n$ trees onto its slots yields a height-$(n+1)$ tree with $m$ leaves. The $\otimes_{S_k}$ identifies trees differing by permuting the root's $k$ subtrees, and the induction supplies the leaf $S_m$-action; together these realise the automorphism coinvariants $(\bigotimes_v E(|v|))_{\mathrm{Aut}(T)}$. Summing over $k$ and the $m_i$ ranges over all height-$(n+1)$ trees.

> [!note]- Lemma 3: Grafting is the monoid multiplication
> **Statement:** Under the identification of $\coprod_n E^{\circ n}$ with all $E$-labelled rooted trees, the free-monoid multiplication restricts to grafting: composing a tree $T$ (with $k$ leaves) with trees $T_1, \dots, T_k$ attaches the root of each $T_i$ to the $i$th leaf of $T$, and the unit is the trivial tree.
>
> **Hint:** The free-monoid product is concatenation of $\circ$-words; in tree terms, concatenating $E^{\circ a}$ with $E^{\circ b}$ stacks one tree on the leaves of another.
>
> **Why needed:** Confirms the monoid structure of $\mathcal{F}(E)$ is the intended operadic (grafting) composition, so $\mathcal{F}(E)$ is the right operad.
>
> > [!note]- Full proof
> > The composition product is associative (Lemma 1 of [[Thm - Operads as Monoids in Symmetric Sequences|the previous theorem]]), so $E^{\circ a} \circ E^{\circ b} \cong E^{\circ(a+b)}$ canonically; this isomorphism, read on trees, takes a height-$a$ tree and a height-$b$ tree filling one of its leaves to the combined tree. The monoid multiplication $\mathcal{F}(E) \circ \mathcal{F}(E) \to \mathcal{F}(E)$ is the fold of these isomorphisms, which on a $P$-operation $T$ with its leaves filled by $T_1, \dots, T_k$ is exactly the grafted tree. The unit $I = E^{\circ 0}$ is the trivial single-edge tree, and grafting it does nothing, giving the operad unit law.

> [!note]- Lemma 4: The universal property
> **Statement:** For every operad $P$, restriction along the unit $\eta_E : E \to U\mathcal{F}(E)$ gives a natural bijection $\mathrm{Operad}(\mathcal{F}(E), P) \cong \mathrm{SymSeq}(E, U(P))$.
>
> **Hint:** This is the freeness from Lemma 1 specialised to $\circ$: a monoid map out of a free monoid is determined freely by its restriction to generators.
>
> **Why needed:** It is the adjunction $\mathcal{F} \dashv U$, the theorem's usable form.
>
> > [!note]- Full proof
> > Given $g : E \to U(P)$, define $\bar g : \mathcal{F}(E) \to P$ by sending an $E$-labelled tree to the $P$-operation obtained by replacing each vertex-label $e \in E(|v|)$ by $g(e) \in P(|v|)$ and performing the corresponding grafting in $P$ (using $P$'s composition $\gamma$). This is well-defined on iso classes (grafting in $P$ respects tree isomorphism by associativity and equivariance of $\gamma$), is an operad map (it intertwines grafting with $\gamma$), and restricts to $g$ on corollas. Uniqueness: any operad map out of $\mathcal{F}(E)$ is determined on corollas by multiplicativity, since every tree is a grafting of corollas. Naturality in $E$ and $P$ is immediate. Hence $\mathcal{F} \dashv U$.

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 — hypotheses.** Assume $\mathcal{V}$ symmetric monoidal with countable coproducts over which $\otimes$ distributes, so that $(\mathrm{SymSeq}(\mathcal{V}), \circ, I)$ is monoidal ([[Thm - Operads as Monoids in Symmetric Sequences|previous theorem]]) and $\circ$ distributes over countable coproducts in each variable enough for free monoids to exist.
>
> **Step 1 — reduce to a free monoid.** By the previous theorem, $\mathrm{Operad}(\mathcal{V})$ is the category of monoids in $(\mathrm{SymSeq}, \circ, I)$, and $U$ is the underlying-object functor. A left adjoint to $U$ is exactly a free-monoid functor for $\circ$.
>
> **Step 2 — build it.** By Lemma 1, the free monoid on $E$ is $\mathcal{F}(E) = \coprod_{n \geq 0} E^{\circ n}$ with concatenation multiplication and unit $E^{\circ 0} = I$.
>
> **Step 3 — identify with trees.** By Lemma 2, $E^{\circ n}$ is the symmetric sequence of $E$-labelled rooted trees of height $n$ (with the $\mathrm{Aut}(T)$ coinvariants), so $\mathcal{F}(E)(m) = \coprod_{T : m \text{ leaves}} (\bigotimes_{v} E(|v|))_{\mathrm{Aut}(T)}$, summed over all rooted trees.
>
> **Step 4 — verify the operad structure.** By Lemma 3, the monoid multiplication is grafting and the unit is the trivial tree; the $S_m$-action permutes leaves. These are the claimed operad data.
>
> **Step 5 — universal property.** By Lemma 4, $\mathrm{Operad}(\mathcal{F}(E), P) \cong \mathrm{SymSeq}(E, U(P))$ naturally, so $\mathcal{F} \dashv U$. The adjunction unit $\eta_E : E \to U\mathcal{F}(E)$ is the inclusion of corollas. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Universal algebra and term rewriting.** The free operad on the operation-symbols of a signature is the operad of *terms* of that signature; quotienting by the equational axioms gives the operad of the theory. Use this to recast the word problem for an equational theory as an equality problem in $\mathcal{F}(E)/R$, and observe that confluent terminating rewriting systems give normal-form representatives for the operad's operations. This is the operadic face of the Knuth–Bendix completion procedure.

**Enumerative combinatorics of trees.** When $E$ has $a_k$ generators of arity $k$, the dimension/cardinality sequence of $\mathcal{F}(E)$ satisfies a functional equation $f(x) = x + \sum_k a_k\, f(x)^k$ (in the non-symmetric case) by the tree recursion. Use this to derive the Catalan generating function for the one-binary-generator free operad and the more general Fuss–Catalan numbers for one $d$-ary generator, recovering classical tree-counting identities from the free-operad formula.

**Syntax and abstract binding trees in programming-language theory.** The abstract syntax of a language is the free (multi-sorted, hence coloured) operad on its constructors; the colours are the syntactic categories (expressions, types, patterns) and the generators are the production rules. Use the universal property to show that an interpreter — a map assigning a semantic operation to each constructor — extends uniquely to all of syntax, which is the categorical content of "evaluation is the unique homomorphism out of the term algebra".

---

# Bridges

- **[[Thm - Operads as Monoids in Symmetric Sequences|Operads as monoids in symmetric sequences]]** — this theorem is the free-monoid construction transported through that one. "The free monoid on $M$ is $\coprod_n M^{\otimes n}$" becomes "the free operad on $E$ is $\coprod_n E^{\circ n}$", and the iterated composition powers $E^{\circ n}$ unwind to height-$n$ labelled trees. Without the monoid identification, the free operad would have to be built by hand and its universal property checked tree-by-tree; with it, both are corollaries of a general monoidal fact.

- **[[Def - Algebra for an Operad|Algebras over the free operad]]** — the free $\mathcal{F}(E)$-algebra on an object $X$ is the algebra of *all formal expressions* in the generators $E$ applied to elements of $X$: $T_{\mathcal{F}(E)}(X)$ is the set of $E$-labelled trees with leaves decorated by elements of $X$. For one binary generator this is the free magma; for the appropriate $E$ it is the free associative, commutative, or Lie algebra after one further quotient by relations.

- **Free groups, free monoids, free modules** — the free operad is the operadic member of the family of free constructions, all sharing the universal property "maps out are determined freely by the generators". The free monoid on a set is the special case where the operad is concentrated in a way that allows only height-$1$ linear trees (words); the branching of general trees is exactly what distinguishes the operadic case, and it appears because operations can have several inputs rather than one.

- **[[Def - Adjunction|Adjunction]] $\mathcal{F} \dashv U$** — the free operad is the left adjoint to the forgetful functor $U : \mathrm{Operad} \to \mathrm{SymSeq}$, exactly as free groups are left adjoint to the forgetful functor $\mathbf{Grp} \to \mathbf{Set}$. The induced monad on $\mathrm{SymSeq}$ is the "operad monad", and its bar resolution is the engine behind the homotopy-coherent resolutions $A_\infty$ and $E_\infty$.

---

# Unlocked by This

> [!tip] Operadic Presentations and Koszul Duality *(from Operadic Homotopy Theory)*
> Every operad is a coequaliser $\mathcal{F}(R) \rightrightarrows \mathcal{F}(E) \to P$ — a presentation by generators $E$ and relations $R$. **Quadratic** presentations (relations in arity related to two generators) are the ones admitting **Koszul duality**, which produces the minimal $A_\infty$/$E_\infty$ resolution and the dual operad ($\mathrm{Comm}^! = \mathrm{Lie}$). The free operad is the raw material of every presentation.

> [!tip] Cofibrant Operads and W-Construction *(from Operadic Homotopy Theory)*
> Free operads are cofibrant, and Boardman–Vogt's **W-construction** thickens the free operad on the generators of $P$ by inserting lengths on the tree edges, producing a cofibrant resolution $W(P) \to P$ whose algebras are the **homotopy $P$-algebras**. The tree description from this theorem is exactly what the W-construction decorates.
