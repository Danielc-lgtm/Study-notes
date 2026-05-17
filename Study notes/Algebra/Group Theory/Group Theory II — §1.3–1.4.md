---
type: topic
subject: group-theory
chapter: "1.3-1.4"
title: "Group Theory II — Actions, Permutations, and Conjugacy"
tags: [algebra, group-theory]
---

# Notation Registry

- $G, H, K, N$ — groups (finite unless stated otherwise)
- $e$ — identity; $|G|$ — order; $\operatorname{ord}(g)$ — order of an element
- $X$ — a set on which a group acts; $|X|$ — its cardinality
- $\operatorname{Sym}(X)$ — the symmetric group of $X$, all bijections $X \to X$; $S_n = \operatorname{Sym}(\{1,\dots,n\})$
- $A_n$ — the alternating group, the even permutations in $S_n$
- $g \cdot x$ or $g * x$ — the result of $g \in G$ acting on $x \in X$
- $\rho : G \to \operatorname{Sym}(X)$ — the permutation representation of an action
- $G \cdot x = \{g \cdot x : g \in G\}$ — the **orbit** of $x$
- $G_x = \operatorname{Stab}_G(x) = \{g : g \cdot x = x\}$ — the **stabiliser** of $x$
- $X^g = \{x : g \cdot x = x\}$ — the **fixed-point set** of $g$
- $g^G$ or $\operatorname{ccl}_G(g) = \{hgh^{-1} : h \in G\}$ — the **conjugacy class** of $g$
- $hgh^{-1}$ — the conjugate of $g$ by $h$
- $C_G(g) = \{h : hg = gh\}$ — the **centraliser** of $g$
- $Z(G) = \{h : hg = gh \ \forall g\}$ — the **centre** of $G$
- $N_G(H) = \{g : gHg^{-1} = H\}$ — the **normaliser** of $H$ in $G$
- $\operatorname{Aut}(G)$ — the automorphism group; $\operatorname{Inn}(G)$ — the inner automorphisms
- cycle type — the partition of $n$ recording the lengths of the disjoint cycles of a permutation in $S_n$

---

# Motivation

The previous topic, [[Group Theory I — §1.1–1.2]], was about taking groups apart — normal subgroups, quotients, the isomorphism theorems. It treated a group as a static algebraic object to be dissected. This topic is about the opposite stance: a group is not a thing, it is a collection of things you can *do*. The integers act on the number line by translation; the symmetric group acts on a set by permuting it; the rotations of a cube act on the cube's faces, edges, vertices, and diagonals all at once. A **group action** is the precise notion that turns the slogan "a group is a set of symmetries" into a definition.

The first surprise is that this loses no generality. [[Thm - Cayley's Theorem|Cayley's theorem]] says every group whatsoever is a group of permutations of some set — concretely, of itself. The abstract group axioms and the concrete idea "permutations you can compose and undo" describe exactly the same class of objects. So actions are not a special topic; they are group theory viewed from the outside.

The reason actions matter so much in practice is the [[Thm - Orbit-Stabiliser Theorem|orbit-stabiliser theorem]]. It is the single most effective counting tool in finite group theory: it says that if $G$ acts on $X$, the size of the orbit of a point times the size of its stabiliser equals $|G|$. This converts statements about group structure into ordinary arithmetic of dividing integers, and it is the engine behind almost every counting argument in this topic and the next. Whenever you must count something — symmetries of a polyhedron, subgroups of a given type, elements with a given property — the move is to find a group acting and read off orbit and stabiliser sizes.

The second half of the topic, §1.4, applies this to the most important action of all: a group acting **on itself by conjugation**. The orbits of this action are the [[Def - Conjugacy Class|conjugacy classes]], the stabilisers are the [[Def - Centraliser and Centre|centralisers]], and the fixed points are the [[Def - Centraliser and Centre|centre]]. The orbit-stabiliser theorem applied here becomes the **class equation**, an identity that partitions $|G|$ into pieces governed by divisibility. The class equation is what makes the structure of a group visible from the integer $|G|$ alone, and it is the tool that proves, in [[Group Theory III — §1.5–1.7]], that $p$-groups have non-trivial centre and that Sylow's theorems hold. The topic closes with its hardest result — the [[Thm - Simplicity of the Alternating Group|simplicity of Aₙ for n ≥q 5]] — proved entirely by tracking conjugacy classes. This is the first genuinely non-abelian simple group, and its simplicity is ultimately why the general quintic equation cannot be solved by radicals.

---

# Concept Map

## §1.3 Actions and Permutations

- **[[Def - Symmetric Group]]**
	- For a set $X$, the **symmetric group** $\operatorname{Sym}(X)$ is the group of all bijections $X \to X$ under composition. When $X = \{1, \dots, n\}$ this is $S_n$, of order $n!$. Permutations are written in disjoint cycle notation, and every permutation factors as a product of transpositions; the parity of the number of transpositions is well-defined and gives the sign homomorphism $\operatorname{sgn} : S_n \to \{\pm 1\}$, whose kernel is the [[Def - Subgroup|subgroup]] $A_n$ of even permutations. The symmetric group is the universal home for actions: every group embeds in some $\operatorname{Sym}(X)$.

- **[[Def - Permutation Group]]**
	- A **permutation group** is a [[Def - Subgroup|subgroup]] of $\operatorname{Sym}(X)$ for some set $X$ — a group given by *some*, not necessarily all, permutations of a set. Its **degree** is $|X|$. The dihedral group acting on the vertices of a polygon and the rotation group of a cube acting on its faces are permutation groups. The definition looks restrictive but is not: by [[Thm - Cayley's Theorem|Cayley's theorem]] every group is isomorphic to a permutation group, so the content of the notion is the *choice* of set $X$, which can make a group's structure vivid or opaque.

- **[[Def - Group Action]]**
	- An **action** of $G$ on a set $X$ is a map $G \times X \to X$, written $(g, x) \mapsto g \cdot x$, satisfying $e \cdot x = x$ and $g_1 \cdot (g_2 \cdot x) = (g_1 g_2) \cdot x$. These axioms say exactly that composing the action of $g_2$ with the action of $g_1$ is the action of $g_1 g_2$, and that the identity does nothing. The associated map sending each $g$ to the permutation $x \mapsto g \cdot x$ is called the **permutation representation** of the action. An action is the formal content of "$G$ is a group of symmetries of $X$".

- **[[Thm - Actions Correspond to Homomorphisms]]**
	- An action of $G$ on $X$ is the same thing as a [[Def - Homomorphism|homomorphism]] $\rho : G \to \operatorname{Sym}(X)$. Given an action, $\rho(g)$ is the permutation $x \mapsto g \cdot x$; given a homomorphism, $g \cdot x := \rho(g)(x)$ is an action; the two constructions are mutually inverse. This is the **true name** of a group action, and it makes the whole machinery of homomorphisms available: the kernel $\ker\rho$ (the elements acting trivially) is a [[Def - Normal Subgroup|normal subgroup]], and by the [[Thm - First Isomorphism Theorem|first isomorphism theorem]] $G/\ker\rho$ embeds in $\operatorname{Sym}(X)$.

- **[[Thm - Cayley's Theorem]]**
	- Every group $G$ is isomorphic to a subgroup of $\operatorname{Sym}(G)$. The proof is the **left-regular action** of $G$ on itself, $g \cdot x = gx$; its permutation representation $\rho : G \to \operatorname{Sym}(G)$ has trivial kernel, because $g$ acting trivially fixes $e$ and hence equals $e$, so by the [[Thm - First Isomorphism Theorem|first isomorphism theorem]] $G \cong \operatorname{im}\rho$. The theorem says abstract groups and permutation groups are the same class of object — though for a group of order $n$ it only embeds $G$ into the enormous $S_n$, so it is more a statement of principle than a practical tool.

- **[[Thm - Coset Action and the Normal Core]]**
	- For $H \leq G$, the group $G$ acts on the set of left cosets $G/H$ by $g \cdot (xH) = gxH$. The kernel of this action is $\bigcap_{x \in G} xHx^{-1}$, the **normal core** of $H$ — the largest [[Def - Normal Subgroup|normal subgroup]] of $G$ contained in $H$. Consequently a subgroup of index $n$ yields a normal subgroup $K \leq H$ with $G/K$ embedding in $S_n$, so $|G/K|$ divides $n!$. Applied to a non-abelian [[Def - Simple Group|simple]] group, this forces every proper subgroup to have index at least $5$ — a remarkably strong constraint extracted from nothing but a counting action.

- **[[Def - Orbit and Stabiliser]]**
	- For an action of $G$ on $X$ and a point $x \in X$, the **orbit** $G \cdot x = \{g \cdot x : g \in G\}$ is everywhere $x$ can be sent, and the **stabiliser** $G_x = \{g : g \cdot x = x\}$ is everything in $G$ that fixes $x$. The stabiliser is always a [[Def - Subgroup|subgroup]]; the orbits partition $X$ into disjoint pieces. An action is **transitive** when there is a single orbit, and **faithful** when only $e$ fixes every point. Orbit and stabiliser are complementary measurements — how far $x$ moves, and how much of $G$ ignores it.

- **[[Thm - Orbit-Stabiliser Theorem]]**
	- If $G$ acts on $X$, then for each $x$ the map $g G_x \mapsto g \cdot x$ is a bijection between the cosets of the stabiliser and the orbit; hence for finite $G$, $|G| = |G_x| \cdot |G \cdot x|$. In particular every orbit size divides $|G|$. This is the master counting theorem: it is [[Thm - Lagrange's Theorem|Lagrange's theorem]] for actions, and it converts any structural question that can be phrased as "how big is this orbit" into a divisibility statement. The art of using it is the choice of the set $X$ and the action.

> [!tip] Unlocked: Burnside's Lemma *(from Enumerative Combinatorics)*
> Averaging the fixed-point counts $|X^g|$ over $g \in G$ gives the number of orbits. This turns the orbit-stabiliser theorem into a counting engine for colourings up to symmetry — necklaces, cube colourings, chemical isomers — and generalises to the Pólya enumeration theorem.

> [!note] Exercise Index — §1.3
> [[Exercise Index - §1.3 Actions and Permutations]]

## §1.4 Conjugacy Classes, Centralisers, and Normalisers

- **[[Def - Automorphism Group]]**
	- An **automorphism** of $G$ is an [[Def - Isomorphism|isomorphism]] $G \to G$, and the automorphisms form a group $\operatorname{Aut}(G)$ under composition. Each $g \in G$ gives an **inner automorphism** $x \mapsto gxg^{-1}$; these form a normal subgroup $\operatorname{Inn}(G) \trianglelefteq \operatorname{Aut}(G)$, and the map $g \mapsto (x \mapsto gxg^{-1})$ is a homomorphism $G \to \operatorname{Aut}(G)$ with kernel the [[Def - Centraliser and Centre|centre]], so $G/Z(G) \cong \operatorname{Inn}(G)$. The automorphism group measures the internal symmetry of $G$ itself.

- **[[Def - Conjugacy Class]]**
	- The **conjugacy class** of $g \in G$ is $\operatorname{ccl}_G(g) = \{hgh^{-1} : h \in G\}$ — the orbit of $g$ under the action of $G$ on itself by conjugation. Conjugate elements are "the same element viewed in different coordinates": they have the same order, and in [[Def - Symmetric Group|symmetric groups]] the same cycle type. Conjugacy classes partition $G$, and a [[Def - Normal Subgroup|subgroup is normal exactly when it is a union of conjugacy classes]] — which is why conjugacy is the right language for detecting normal subgroups.

- **[[Def - Centraliser and Centre]]**
	- The **centraliser** $C_G(g) = \{h : hg = gh\}$ is the set of elements commuting with $g$ — the stabiliser of $g$ under conjugation. The **centre** $Z(G) = \{h : hg = gh \text{ for all } g\} = \bigcap_g C_G(g)$ is the set of elements commuting with everything. The centre is always a [[Def - Normal Subgroup|normal]] (indeed abelian) subgroup, equal to the kernel of $G \to \operatorname{Aut}(G)$; it measures how far $G$ is from being [[Def - Abelian Group|abelian]], with $Z(G) = G$ exactly when $G$ is abelian.

- **[[Thm - The Class Equation]]**
	- By the [[Thm - Orbit-Stabiliser Theorem|orbit-stabiliser theorem]] applied to conjugation, $|\operatorname{ccl}_G(g)| = |G : C_G(g)|$ — every conjugacy class size divides $|G|$. Summing over classes and separating the singletons (which are exactly the central elements) gives the **class equation** $|G| = |Z(G)| + \sum_i |G : C_G(x_i)|$, the sum running over non-central class representatives. This single identity is the workhorse of finite group theory: it is the lever that proves a [[Group Theory III — §1.5–1.7|p-group has non-trivial centre]] and underpins the Sylow theorems.

- **[[Def - Normaliser]]**
	- The **normaliser** of a subgroup $H \leq G$ is $N_G(H) = \{g : gHg^{-1} = H\}$ — the stabiliser of $H$ under the conjugation action of $G$ on its own subgroups. It is the largest subgroup of $G$ in which $H$ is [[Def - Normal Subgroup|normal]]: always $H \trianglelefteq N_G(H) \leq G$, with $H$ normal in $G$ precisely when $N_G(H) = G$. By [[Thm - Orbit-Stabiliser Theorem|orbit-stabiliser]], the number of conjugates of $H$ equals $|G : N_G(H)|$, which is how one counts subgroups of a given type.

- **[[Thm - Conjugacy Classes of the Symmetric Group]]**
	- Two permutations in $S_n$ are conjugate if and only if they have the same **cycle type**, so the conjugacy classes of $S_n$ are in bijection with the partitions of $n$. Conjugating $\sigma$ by $\tau$ simply relabels the points $\sigma$ permutes, leaving the cycle lengths unchanged. The class of cycle type $1^{a_1}2^{a_2}\cdots$ has size $n! / \prod_k k^{a_k} a_k!$. This makes $S_n$ the one infinite family of groups whose conjugacy structure is completely transparent, and it is the combinatorial input to the simplicity proof for $A_n$.

- **[[Thm - Simplicity of the Alternating Group]]**
	- The alternating group $A_n$ is [[Def - Simple Group|simple]] for all $n \geq 5$ (and trivially for $n = 2, 3$; $A_4$ is *not* simple). The proof shows $A_n$ is generated by $3$-cycles, that all $3$-cycles are conjugate within $A_n$ once $n \geq 5$, and that any non-trivial [[Def - Normal Subgroup|normal subgroup]] must contain a $3$-cycle — whence it is everything. $A_5$, of order $60$, is the smallest non-abelian simple group, and the non-solvability of $A_n$ for $n \geq 5$ is the group-theoretic reason the general quintic has no solution in radicals.

> [!tip] Unlocked: Linear Representation and Character *(from Representation Theory)*
> Replacing the set $X$ by a vector space turns an action into a [[Def - Homomorphism|homomorphism]] $G \to \mathrm{GL}(V)$ — a linear representation. Functions constant on [[Def - Conjugacy Class|conjugacy classes]] (characters) become the central objects, and the number of irreducible representations equals the number of conjugacy classes.

> [!note] Exercise Index — §1.4
> [[Exercise Index - §1.4 Conjugacy Classes and Centralisers]]

---

# Sources and Targets

**Targets — what do we usually try to prove?**

The exercises of this topic pursue a recognizable set of goals. The most pervasive is **counting**: the order of a group of symmetries, the number of elements in an orbit or a conjugacy class, the number of subgroups conjugate to a given one, the number of colourings of an object up to symmetry. A second target is **producing a normal subgroup** — and hence proving a group is not [[Def - Simple Group|simple]] — by exhibiting an action whose kernel is proper and non-trivial. A third is **proving an embedding**: showing one group sits inside another, almost always inside a [[Def - Symmetric Group|symmetric group]] via some action. A fourth, characteristic of §1.4, is **locating the centre or analysing commutativity** — showing $Z(G)$ is non-trivial, or that a group is or is not abelian. A fifth is **classifying conjugacy** — deciding when two elements are conjugate, which in $S_n$ is completely answered by cycle type. These targets recur because each is a way of pinning down how a group sits in relation to a set it acts on, and the structure of a finite group is largely encoded in its actions.

**Sources — what assumptions do we usually leverage?**

The assumptions are equally stereotyped. **A set with symmetry is given** — a polygon, a polyhedron, a collection of cosets, the group itself — and the move is to let the group act and apply [[Thm - Orbit-Stabiliser Theorem|orbit-stabiliser]]. **A subgroup of known index is given**, which routes through the [[Thm - Coset Action and the Normal Core|coset action]] to an embedding in a symmetric group. **The order $|G|$ is given with its factorization**, which combines with orbit sizes dividing $|G|$ to force orbits to be small or large. **An element or subgroup is given and its conjugates are of interest**, routing through the centraliser or [[Def - Normaliser|normaliser]] and the [[Thm - The Class Equation|class equation]]. **The group is a symmetric or alternating group**, where cycle type makes conjugacy explicit. The unifying observation is that every source in this topic is converted to a target by the same two-step move: find the right action, then apply orbit-stabiliser. The difficulty is never the theorem; it is the choice of what set to act on.

---

# Legal Operations

These are the moves almost every problem in this topic is built from. When stuck, scan the list. Everything is self-contained: a reader with no group theory background should follow each operation from its description.

**Legal operations:**

1. **Let the group act on a cleverly chosen set.** This is the master operation. To extract information about $G$, find a set $X$ that $G$ naturally permutes — the vertices of a shape, the cosets of a subgroup, the elements of $G$ itself, the subgroups of a given order, the subsets of a given size — and study the [[Def - Group Action|action]]. Almost every other operation here is a way of exploiting an action once you have chosen one. The trigger is any question about the size or structure of $G$; the skill is the choice of $X$.

2. **Apply the orbit-stabiliser theorem.** Once $G$ acts on $X$, every point $x$ satisfies $|G| = |G \cdot x| \cdot |G_x|$. Use this to compute $|G|$ when you know an orbit and a stabiliser, to compute an orbit size when you know $|G|$ and the stabiliser, or to prove an orbit size divides $|G|$. The trigger is any counting question once an action is in hand; this is the [[Thm - Orbit-Stabiliser Theorem|orbit-stabiliser theorem]] and it is the reason actions are worth setting up.

3. **Convert an action into a homomorphism and take its kernel.** An [[Def - Group Action|action]] on $X$ *is* a [[Def - Homomorphism|homomorphism]] $G \to \operatorname{Sym}(X)$. Its kernel is a [[Def - Normal Subgroup|normal subgroup]] — the elements acting invisibly — and its image is a permutation group. The trigger: you want to produce a normal subgroup, or to embed $G$ into a symmetric group. This is how the [[Thm - Coset Action and the Normal Core|coset action]] manufactures normal subgroups out of nothing but a subgroup.

4. **Act on the cosets of a subgroup.** Given $H \leq G$ of index $n$, the action on $G/H$ produces a homomorphism $G \to S_n$ whose kernel lies inside $H$. The trigger is a subgroup of small index: this operation converts "small index" into "embeds in a small symmetric group", and the divisibility constraint $|G/K| \mid n!$ is often immediately decisive.

5. **Act on the group itself by conjugation.** The conjugation action $g \cdot x = gxg^{-1}$ has orbits the [[Def - Conjugacy Class|conjugacy classes]], stabilisers the [[Def - Centraliser and Centre|centralisers]], and fixed points the centre. The trigger is any question about commutativity, the centre, or normal subgroups — because normal subgroups are unions of conjugacy classes. This operation turns the internal structure of $G$ into an orbit-counting problem.

6. **Write down the class equation.** Partitioning $G$ into conjugacy classes and recording each size as $|G : C_G(x)|$ gives $|G| = |Z(G)| + \sum |G : C_G(x_i)|$. The trigger is a problem where $|G|$ has special divisibility — above all when $|G|$ is a prime power, since then every non-central class size is divisible by $p$. This is the [[Thm - The Class Equation|class equation]] and it is the bridge from §1.4 into all of [[Group Theory III — §1.5–1.7]].

7. **Count conjugates by the index of a normaliser or centraliser.** The number of conjugates of an element $g$ is $|G : C_G(g)|$; the number of conjugate subgroups to $H$ is $|G : N_G(H)|$. The trigger: you need to count how many objects are equivalent to a given one under conjugation. This is orbit-stabiliser specialised to the conjugation action, with the [[Def - Centraliser and Centre|centraliser]] or [[Def - Normaliser|normaliser]] as the stabiliser.

8. **Read conjugacy in $S_n$ off cycle type.** Two permutations are conjugate in $S_n$ if and only if they have the same cycle type, and conjugating by $\tau$ relabels the entries by $\tau$. The trigger is any concrete problem in a symmetric or alternating group: cycle type makes conjugacy classes, centraliser sizes, and class sizes all computable by hand.

**Illegal but tempting operations:**

> [!warning] 1. Assuming every orbit has the same size
> Orbit-stabiliser guarantees each orbit size *divides* $|G|$, and orbits of the *same* transitive action of $G$ — there is only one — coincide, but a single action generally has orbits of many different sizes. The conjugation action is the standard example: its orbits are conjugacy classes, and they range from singletons (central elements) to large classes. Only for a *transitive* action is there one orbit; in general $X$ is a disjoint union of orbits of assorted sizes, and the [[Thm - The Class Equation|class equation]] is precisely the bookkeeping of that variation.

> [!warning] 2. Believing the stabilisers of different points are equal
> It is tempting to speak of "the stabiliser" of an action. But stabilisers of points in the same orbit are only *conjugate*: $G_{g \cdot x} = g\, G_x\, g^{-1}$. They have the same order but are usually different subgroups. Treating them as identical silently assumes the action is something special; the safe statement is that points of one orbit have conjugate, hence isomorphic, stabilisers.

> [!warning] 3. Concluding two elements are conjugate because they have the same order
> Conjugate elements always share the same order, so it is tempting to use sameness of order as a test for conjugacy. The converse fails: in $C_p \times C_p$ every non-identity element has order $p$, yet the group is [[Def - Abelian Group|abelian]] so every conjugacy class is a singleton — no two distinct elements are conjugate. Same order is necessary, never sufficient. (In $S_n$ the correct invariant is cycle type, which is strictly finer than order.)

> [!warning] 4. Forgetting that $A_4$ has no subgroup of index 2
> Having proved $A_n$ simple for $n \geq 5$, it is tempting to imagine $A_4$ behaves similarly, or to apply "index $2$ forces normality" in reverse and expect a subgroup of order $6$. But $A_4$, of order $12$, has *no* subgroup of order $6$ at all — this is the standard refutation of the converse of [[Thm - Lagrange's Theorem|Lagrange's theorem]]. The small alternating groups $A_2, A_3, A_4$ are genuinely exceptional, and arguments about $A_n$ for $n \geq 5$ must not be extrapolated downward.

---

# Problem-Solving Strategy

Every problem in this topic begins with the same question, and you should ask it explicitly before anything else: **what set should the group act on?** The entire topic is the theory of group actions, and essentially every solution is the choice of a good action followed by the [[Thm - Orbit-Stabiliser Theorem|orbit-stabiliser theorem]]. So the strategic skill being trained is not the deployment of a theorem — there is really only one theorem — but the identification of the right set $X$. The candidates form a short list, and you should run through it deliberately.

If the problem **asks you to count the order of a group of symmetries** — the rotations of a polyhedron, the symmetries of a graph or a configuration — let the group act on the most concrete features of the object: its faces, its vertices, its edges, its diagonals. Pick a feature, find the orbit (usually the action is transitive, so the orbit is all the features of that kind) and the stabiliser (the symmetries fixing one chosen feature, a smaller and more tractable group), and multiply. The reason this works is that orbit-stabiliser turns the unknown $|G|$ into a product of two numbers you can see directly.

If the problem **gives you a subgroup of small index** $n$ and asks for a structural conclusion — normality, an embedding, a divisibility constraint — the set to act on is the cosets $G/H$. The [[Thm - Coset Action and the Normal Core|coset action]] produces a homomorphism $G \to S_n$; its kernel is a normal subgroup inside $H$, and $|G/K|$ divides $n!$. This is the standard route from "small index" to a contradiction or a normal subgroup, and it is how one shows, for instance, that a subgroup whose index is the smallest prime dividing $|G|$ must be normal.

If the problem **concerns the centre, commutativity, or the existence of a normal subgroup**, the set to act on is $G$ itself, by conjugation. Then write down the [[Thm - The Class Equation|class equation]]. The class equation is most powerful when $|G|$ has restricted divisibility: when $|G|$ is a power of a prime, every non-central conjugacy class has size divisible by $p$, so the equation forces $p \mid |Z(G)|$ and the centre cannot be trivial. The general principle is that the class equation transmits divisibility information from $|G|$ to $|Z(G)|$, and that transmission is the whole engine of $p$-group theory in the next topic.

If the problem **asks whether two elements are conjugate, or to count a conjugacy class**, and the group is a [[Def - Symmetric Group|symmetric group]], use cycle type — conjugacy is sameness of cycle type and nothing more. If the group is general, use that the class size is the index $|G : C_G(g)|$ of the [[Def - Centraliser and Centre|centraliser]], so the problem reduces to computing how many elements commute with $g$. If instead the problem is about how many subgroups are conjugate to a given $H$, the count is the index $|G : N_G(H)|$ of the [[Def - Normaliser|normaliser]].

Finally, if the problem **asks you to prove a group is not simple**, your target is a proper non-trivial normal subgroup, and the productive sources of normal subgroups in this topic are kernels of actions. So look for an action of $G$ on a small set: on the cosets of a subgroup, or on a naturally occurring small collection. If the set has size $n$ with $|G| \nmid n!$, the kernel cannot be trivial; if the action is non-trivial, the kernel cannot be all of $G$; either way you have produced the normal subgroup. To prove a group *is* simple is much harder and is done, as for [[Thm - Simplicity of the Alternating Group|Aₙ]], by a direct and delicate analysis of conjugacy classes — there is no shortcut, and the proof must be learned as a specific argument.

---

# Most Reusable Properties

- **[[Thm - Orbit-Stabiliser Theorem|Orbit-Stabiliser Theorem]]**: $|G| = |G \cdot x|\,|G_x|$. This is the most-used theorem in the topic and one of the most-used in all of finite group theory. The recognizable setup is any counting question: whenever you must determine the size of a set acted on by a group, or the order of a group acting on a known set, set up the action and read off two of the three quantities to get the third. Its disguised uses are the [[Thm - The Class Equation|class equation]] (conjugation action), the conjugate-counting formula $|G : N_G(H)|$ (action on subgroups), and [[Thm - Lagrange's Theorem|Lagrange's theorem]] itself (left-regular action restricted to a subgroup).

- **The class equation**: $|G| = |Z(G)| + \sum |G : C_G(x_i)|$. Reach for it whenever $|G|$ has special arithmetic — above all, prime-power order. Its power is that it forces information about $|Z(G)|$, an object hard to access directly, out of the much more visible factorization of $|G|$. It is the single most important inheritance from this topic into [[Group Theory III — §1.5–1.7]], where it proves $p$-groups have non-trivial centre.

- **An action is a homomorphism $G \to \operatorname{Sym}(X)$**: this equivalence ([[Thm - Actions Correspond to Homomorphisms]]) is reusable as a *conversion device*. Every time you have an action you may instead think "homomorphism" and deploy kernels, images, and the [[Thm - First Isomorphism Theorem|first isomorphism theorem]]; every time you have a homomorphism into a symmetric group you may think "action" and deploy orbits and stabilisers. Fluently switching viewpoints is what makes the [[Thm - Coset Action and the Normal Core|coset action]] arguments feel automatic.

- **[[Def - Normal Subgroup|Normal subgroups are unions of conjugacy classes]]**: this characterisation is the reusable bridge between §1.4 and the search for normal subgroups. To test or construct a normal subgroup, you may work class by class: a normal subgroup must contain, with any element, its entire [[Def - Conjugacy Class|conjugacy class]]. This is exactly the principle that drives the [[Thm - Simplicity of the Alternating Group|simplicity proof for Aₙ]] and the conjugacy-counting proofs of non-simplicity in the next topic.

- **[[Def - Normaliser|Normaliser]] as "largest overgroup in which $H$ is normal"**: $H \trianglelefteq N_G(H) \leq G$. The typical use is twofold — to *count* conjugate subgroups as $|G : N_G(H)|$, and to *create* a setting in which a non-normal subgroup becomes normal, so that a quotient can be formed locally. The normaliser is the standard repair when a subgroup fails to be normal in all of $G$.

---

# Bridges

1. **Enumerative combinatorics — Burnside's lemma and Pólya counting.** The number of orbits of a finite group action equals the average number of fixed points, $\frac{1}{|G|}\sum_{g} |X^g|$. This identity, the Cauchy–Frobenius–Burnside lemma, is proved by counting the set $\{(g, x) : g \cdot x = x\}$ two ways and applying the [[Thm - Orbit-Stabiliser Theorem|orbit-stabiliser theorem]]. It turns "count configurations up to symmetry" — necklaces, coloured polyhedra, molecular isomers — into a finite sum, and its weighted refinement is the Pólya enumeration theorem. Orbit-stabiliser is thus not only a structural tool but the foundation of a whole branch of counting.

2. **Representation theory — linear actions and characters.** A [[Def - Group Action|group action]] on a set becomes a linear representation when the set is replaced by a vector space: a representation is a [[Def - Homomorphism|homomorphism]] $G \to \mathrm{GL}(V)$, exactly the construction of [[Thm - Actions Correspond to Homomorphisms]] with $\operatorname{Sym}(X)$ replaced by $\mathrm{GL}(V)$. The [[Def - Conjugacy Class|conjugacy classes]] of §1.4 reappear as the indexing set for irreducible characters: the number of irreducible representations of a finite group equals the number of conjugacy classes, so the class analysis done here is literally the bookkeeping of representation theory.

3. **Sylow theory — actions as the proof technique.** The whole of [[Group Theory III — §1.5–1.7|Sylow theory]] is proved by choosing the right action and applying [[Thm - Orbit-Stabiliser Theorem|orbit-stabiliser]]: $G$ acts on the set of its $p^a$-element subsets to produce a Sylow subgroup, and a $p$-group acts on the set of Sylow subgroups to force the congruence $n_p \equiv 1 \pmod p$. The [[Thm - The Class Equation|class equation]] is the special case of conjugation. This topic is, in a precise sense, the toolkit that the next topic spends entirely.

4. **Algebraic topology — covering spaces and deck transformations.** A [[Def - Group Action|group action]] on a topological space, when suitably free, has an orbit space that is again a space, and the original space is a covering of it. For the universal cover the acting group is the fundamental group $\pi_1$, the action is by deck transformations, and the [[Thm - Orbit-Stabiliser Theorem|orbit-stabiliser]] correspondence becomes the dictionary between subgroups of $\pi_1$ and connected covering spaces. The abstract orbit and stabiliser of this topic acquire there a direct geometric meaning.

---

# Insights

**The unifying frame: every theorem in this topic is the orbit-stabiliser theorem in disguise.** It is worth saying plainly. [[Thm - Lagrange's Theorem|Lagrange's theorem]] is orbit-stabiliser for the regular action restricted to a subgroup. [[Thm - Cayley's Theorem|Cayley's theorem]] is the regular action with its kernel computed. The [[Thm - Coset Action and the Normal Core|coset action]] embedding is orbit-stabiliser plus the [[Thm - First Isomorphism Theorem|first isomorphism theorem]]. The [[Thm - The Class Equation|class equation]] is orbit-stabiliser for the conjugation action, summed. The conjugate-counting formula $|G:N_G(H)|$ is orbit-stabiliser for the action on subgroups. Once you see this, the topic stops being a list of theorems and becomes a single theorem applied to a list of well-chosen sets. The intellectual work is always relocated to the same place: the choice of $X$.

**The true name of a group action is "a homomorphism to a symmetric group".** The definition with its two axioms is the right thing to *verify*, but the operational understanding is that an action is a homomorphism $\rho : G \to \operatorname{Sym}(X)$. This is not a minor reformulation; it is what lets the entire apparatus of [[Group Theory I — §1.1–1.2]] — kernels, images, the isomorphism theorems — descend onto actions. The kernel of $\rho$ is "the part of $G$ the action cannot see", the image is "$G$ as actually realised on $X$", and faithfulness is injectivity. When you are handed an action, immediately ask what its kernel is; that question has produced more normal subgroups than any other in finite group theory.

**Conjugation is change of coordinates.** The element $gxg^{-1}$ is "$x$, performed in the coordinate system that $g$ sets up": relabel the world by $g$, do $x$, relabel back. This is why conjugate elements share every intrinsic property — order, cycle type, whether they are a rotation or a reflection — and differ only in description. It explains why [[Def - Conjugacy Class|conjugacy classes]] are the natural unit of structure: a class is "one element, all coordinate systems". It explains why the [[Def - Centraliser and Centre|centre]] is interesting — central elements look the same in every coordinate system — and why class functions are the right invariants. In $S_n$ the metaphor is literal: conjugating a permutation renames the points it moves, so conjugacy classes are cycle types exactly.

**Simplicity is detected one conjugacy class at a time.** A [[Def - Normal Subgroup|normal subgroup]] must be a union of [[Def - Conjugacy Class|conjugacy classes]] including $\{e\}$. This single observation reduces the question "is $G$ simple" to pure arithmetic: list the class sizes, and ask whether any sub-collection that includes the singleton $\{e\}$ can sum to a proper divisor of $|G|$. For $A_5$ the class sizes are $1, 12, 12, 15, 20$ and no proper sub-sum containing the $1$ divides $60$ — so $A_5$ is simple, and the proof is a finite check. The general [[Thm - Simplicity of the Alternating Group|simplicity of Aₙ]] is the same idea made uniform: control the classes, and normality has nowhere to hide. The same counting, run in reverse, is how the next topic proves groups of many specific orders *fail* to be simple.
