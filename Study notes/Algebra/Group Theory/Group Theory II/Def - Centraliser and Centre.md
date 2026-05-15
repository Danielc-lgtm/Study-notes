---
type: definition
subject: group-theory
prereqs:
  - "Def - Group"
  - "Def - Subgroup"
  - "Def - Group Action"
  - "Def - Orbit and Stabiliser"
  - "Def - Conjugacy Class"
  - "Def - Normal Subgroup"
  - "Def - Abelian Group"
tags: [algebra, group-theory]
---

# Notation

Throughout, $G$ is a group with identity $e$. Two elements $g, h$ **commute** if $gh = hg$. The **centraliser** of $g \in G$ is written $C_G(g)$, and the **centre** of $G$ is written $Z(G)$ — the letter $Z$ is from the German *Zentrum*. We write $H \leq G$ for "$H$ is a [[Def - Subgroup|subgroup]] of $G$", $H \trianglelefteq G$ for "$H$ is [[Def - Normal Subgroup|normal]] in $G$", and $|G : H|$ for the index of $H$ in $G$. The conjugate of $g$ by $h$ is $hgh^{-1}$. The full symbol registry for this topic is on [[Group Theory II — §1.3–1.4]].

This page defines **two** related but distinct objects. The centraliser is attached to a *single chosen element* $g$; the centre is attached to the *whole group*. Each gets its own full definition below, and the relation between them — the centre is the intersection of all centralisers — is recorded after both.

---

# Axiom Motivation

Both objects on this page answer the same kind of question — *how much of $G$ commutes with what?* — and both are most naturally discovered as the [[Def - Orbit and Stabiliser|stabilisers and fixed points]] of the [[Def - Conjugacy Class|conjugation action]]. We motivate them together because they are the two halves of one idea.

**Why the centraliser.** Fix an element $g$ and look at its [[Def - Conjugacy Class|conjugacy class]] $\operatorname{ccl}_G(g) = \{hgh^{-1} : h \in G\}$. We would like to know how *big* this class is — how many distinct elements $g$ is conjugate to. The class is the orbit of $g$ under conjugation, and the [[Thm - Orbit-Stabiliser Theorem|orbit-stabiliser theorem]] says an orbit's size is the index of the corresponding *stabiliser*. So to count the class we are forced to ask: which $h$ fix $g$ under conjugation, i.e. satisfy $hgh^{-1} = g$? Rearranging, $hg = gh$. The stabiliser of $g$ under conjugation is *exactly the set of elements that commute with $g$*. This set is so important that it gets its own name, the centraliser, and the entire reason to define it is that it is the denominator in the class-size formula $|\operatorname{ccl}_G(g)| = |G : C_G(g)|$.

That fixes the definition and excludes the variants. Why not "the set of $h$ with $hg = gh^2$", or some other near-miss relation? Because *that* is not the stabiliser of any action and the orbit-stabiliser machinery would not apply. The defining condition $hg = gh$ is forced on us: it is the literal unwinding of $h * g = g$ for the conjugation action $h * g = hgh^{-1}$. We should also check it is a [[Def - Subgroup|subgroup]] — and it must be, because *stabilisers of an action are always subgroups*, so we get that for free rather than verifying closure, identity, and inverses by hand. (Directly: if $h_1, h_2$ commute with $g$ then so does $h_1 h_2$, since $h_1h_2 g = h_1 g h_2 = g h_1 h_2$, and if $h$ commutes with $g$ then so does $h^{-1}$, by conjugating $hg = gh$ by $h^{-1}$ on both sides.)

What if we weakened the requirement — say, asked only that $hgh^{-1}$ lie in the *cyclic subgroup* $\langle g\rangle$ rather than equal $g$? We would get a larger set (the *normaliser* of $\langle g\rangle$, the subject of [[Def - Normaliser]]), but it would no longer be the stabiliser of the point $g$, only of the subgroup $\langle g\rangle$, and the class-size formula would break. What if we strengthened it — demanded $h$ commute not just with $g$ but with every element of $G$? Then we would have moved from a property *of $h$ relative to $g$* to a property *of $h$ alone*, and we would be defining the centre, not the centraliser. The centraliser is the Goldilocks notion: tied to one element, exactly the conjugation-stabiliser, exactly the class-size denominator.

**Why the centre.** Now run the conjugation action again and look not at one orbit but at the *fixed points* — the elements $h$ that conjugation never moves. An element $g$ is fixed by the *whole* conjugation action when $hgh^{-1} = g$ for *every* $h$, i.e. when $g$ commutes with everything. The set of such elements is the centre $Z(G)$.

Several desiderata pin this down. First, the centre should measure *how far $G$ is from being [[Def - Abelian Group|abelian]]*: a group is abelian exactly when every pair commutes, which is exactly when *every* element is central, i.e. $Z(G) = G$; and the centre shrinks to $\{e\}$ when no non-identity element commutes with all others. So $Z(G)$ is a dial reading abelian-ness, and we want the definition to make $Z(G) = G \iff G$ abelian come out as a tautology — which the condition "commutes with all $g$" does.

Second, the centre should be a [[Def - Normal Subgroup|normal subgroup]], because we will want to *quotient by it*: forming $G/Z(G)$ is the standard way to "kill the abelian part" and the construction $G/Z(G) \cong \operatorname{Inn}(G)$ depends on $Z(G)$ being normal. The definition delivers this. Centrality is itself a conjugation-invariant property — if $g$ commutes with everything, so does any conjugate of $g$ (in fact $g$'s conjugacy class is just $\{g\}$) — so $Z(G)$ is a union of singleton classes, hence closed under conjugation, hence normal. Even better, the centre is *abelian* as a group, since any two of its elements commute with everything and so with each other.

What breaks on weakening? If we asked only that $g$ commute with the *generators* of $G$ we would, in fact, still get the centre (commuting with generators forces commuting with all products) — that is a useful computational shortcut, not a different object. But if we asked only that $g$ commute with *some* element we would get nothing structured at all. What breaks on strengthening? If we demanded $g$ be fixed by *all* [[Def - Automorphism Group|automorphisms]] and not merely the inner ones, we would not get the centre — we would get a possibly smaller characteristic subgroup. The centre is exactly "fixed by all *inner* automorphisms", and that "inner" is essential: it is what makes the centre the kernel of the map $G \to \operatorname{Aut}(G)$.

The deepest justification pins the centre down completely: the centre is exactly the **kernel** of the conjugation homomorphism $G \to \operatorname{Aut}(G)$, $g \mapsto (x \mapsto gxg^{-1})$. An element is in the kernel when conjugation by it is the *identity* automorphism, i.e. $gxg^{-1} = x$ for all $x$ — the defining condition of the centre. Defining $Z(G)$ as "commutes with everything" and discovering it equals a kernel is the payoff: kernels are automatically normal, which is why $Z(G) \trianglelefteq G$, and the [[Thm - First Isomorphism Theorem|first isomorphism theorem]] then gives $G/Z(G) \cong \operatorname{Inn}(G)$ with no further work.

---

# The Definition

**Definition (Centraliser).** Let $G$ be a group and $g \in G$. The **centraliser** of $g$ in $G$ is
$$C_G(g) \;=\; \{\, h \in G : hg = gh \,\} \;=\; \{\, h \in G : hgh^{-1} = g \,\},$$
the set of all elements of $G$ that commute with $g$. It is the [[Def - Orbit and Stabiliser|stabiliser]] of $g$ under the [[Def - Conjugacy Class|conjugation action]] $h * g_1 = hg_1h^{-1}$ of $G$ on itself, and is therefore a [[Def - Subgroup|subgroup]] of $G$. By the [[Thm - Orbit-Stabiliser Theorem|orbit-stabiliser theorem]], its index is the size of the conjugacy class:
$$|\operatorname{ccl}_G(g)| \;=\; |G : C_G(g)|.$$
One always has $g \in C_G(g)$ and indeed $\langle g\rangle \leq C_G(g)$, since every power of $g$ commutes with $g$. The centraliser need not be normal in $G$.

**Definition (Centre).** Let $G$ be a group. The **centre** of $G$ is
$$Z(G) \;=\; \{\, h \in G : hg = gh \ \text{ for all } g \in G \,\},$$
the set of elements that commute with *every* element of $G$. Three equivalent descriptions, each illuminating a different aspect:

1. **As an intersection of centralisers.** $Z(G) = \bigcap_{g \in G} C_G(g)$. To commute with everything is to commute with each $g$ separately, so the centre is the intersection of all centralisers — and an intersection of subgroups is a subgroup, confirming $Z(G) \leq G$.

2. **As the fixed points of conjugation.** $Z(G)$ is the set of elements whose [[Def - Conjugacy Class|conjugacy class]] is a singleton, $\operatorname{ccl}_G(z) = \{z\}$ — the points fixed by the entire conjugation action.

3. **As a kernel.** $Z(G) = \ker\big(G \to \operatorname{Aut}(G)\big)$, the kernel of the [[Def - Homomorphism|homomorphism]] sending $g$ to conjugation-by-$g$; see [[Def - Automorphism Group]].

The centre is a [[Def - Normal Subgroup|normal subgroup]] of $G$ (being a kernel, or being a union of singleton conjugacy classes), and it is **abelian** as a group. One has $Z(G) = G$ if and only if $G$ is [[Def - Abelian Group|abelian]], and at the other extreme $Z(G)$ may be the trivial group $\{e\}$.

---

# Relate to Other Fields / Compression

The centraliser and centre are the group-theoretic instances of a pattern that appears wherever one has an algebra of operators: **the things that commute with a given operator, and the things that commute with everything.**

In **linear algebra and operator theory** the centraliser of a matrix $A$ inside the matrix algebra is its *commutant* $\{B : AB = BA\}$ — the operators sharing $A$'s invariant structure. The centre of the full matrix algebra $M_n$ is the scalar matrices $\lambda I$: the only operators commuting with *every* matrix are the scalars. This is the linchpin of **Schur's lemma** in representation theory, which says the centraliser of an irreducible representation is exactly the scalars — a statement that an irreducible has the smallest possible centraliser. The reader who knows the **Heisenberg uncertainty principle** has met the centraliser idea physically: two observables can be simultaneously measured exactly when they commute, so the centraliser of an observable is the algebra of quantities compatible with it, and a *central* observable (a multiple of the identity, a $c$-number) is compatible with everything and carries no quantum information.

In **ring theory** the same two definitions reappear verbatim: the centre of a ring $R$ is $\{r : rs = sr \ \forall s\}$, and it is over its centre that $R$ is naturally an algebra. A *central simple algebra* — a ring whose centre is just the base field and which has no two-sided ideals — is the ring-theoretic analogue of a group with trivial centre and no normal subgroups, and the Brauer group is built from exactly these.

In **Lie theory** the centraliser of an element $X$ in a Lie algebra $\mathfrak{g}$ is $\{Y : [X,Y] = 0\}$ and the centre is $\{Z : [Z, Y] = 0 \ \forall Y\}$ — the bracket replaces the commutator $gh - hg$. A *semisimple* Lie algebra has trivial centre; an *abelian* one is its own centre. The dimension of the centraliser of a generic element is the *rank* of the Lie algebra.

So the compression is: the centraliser is "the commutant of one element", the centre is "the commutant of the whole structure", and the slogan "the centre is what commutes with everything, hence what carries no relational information" specialises to scalars in matrix algebras, $c$-numbers in quantum mechanics, and the base field in a central simple algebra.

---

# Examples / Corollaries

**Is an instance — centralisers in $S_3$.** Take $g = (1\,2)$ in $S_3$. Which elements commute with it? The identity does, and $(1\,2)$ commutes with itself, so $\{e, (1\,2)\} \leq C_{S_3}((1\,2))$. No $3$-cycle commutes with $(1\,2)$, and the other transpositions do not either — e.g. $(1\,3)(1\,2) = (1\,2\,3)$ but $(1\,2)(1\,3) = (1\,3\,2)$. So $C_{S_3}((1\,2)) = \{e, (1\,2)\}$, of order $2$. Check against the class-size formula: $|\operatorname{ccl}((1\,2))| = |S_3 : C_{S_3}((1\,2))| = 6/2 = 3$, and indeed there are three transpositions.

**Is an instance — the centre of a $p$-group.** Every finite group whose order is a power of a prime $p$ has *non-trivial* centre, $Z(G) \neq \{e\}$. This is one of the most important consequences of the [[Thm - The Class Equation|class equation]]: each non-central conjugacy class has size divisible by $p$, the classes partition $G$, and $|G|$ is divisible by $p$, so the number of singleton classes — which is $|Z(G)|$ — must also be divisible by $p$, hence at least $p$. The centre being non-trivial is the foundation of the entire theory of $p$-groups in [[Group Theory III — §1.5–1.7]].

**Is an instance — the centre of $\mathrm{GL}_n$.** The centre of the general linear group $\mathrm{GL}_n(\mathbb{R})$ is the group of nonzero scalar matrices $\{\lambda I : \lambda \neq 0\}$. A matrix commuting with *every* invertible matrix must commute with every matrix at all (the non-invertible ones are limits, or one argues directly with elementary matrices), and the only such matrices are scalars. So $Z(\mathrm{GL}_n) \cong \mathbb{R}^\times$, and the quotient $\mathrm{GL}_n / Z(\mathrm{GL}_n) = \mathrm{PGL}_n$ is the projective linear group.

**Is NOT an instance — the centre of $S_n$ for $n \geq 3$.** The symmetric group $S_n$ has *trivial* centre once $n \geq 3$: $Z(S_n) = \{e\}$. Any non-identity permutation $\sigma$ moves some point $i$ to a different point $j$; pick a third point $k$ (available since $n \geq 3$) and the transposition $(j\,k)$ then fails to commute with $\sigma$, because conjugating $\sigma$ by $(j\,k)$ changes where $i$ is sent. So no non-identity permutation is central. This shows the centre can be as small as possible even for a large group — $S_n$ is "maximally non-abelian" in this sense.

**Is NOT an instance — a centraliser need not be normal.** It is tempting, having learned that the *centre* is always normal, to expect *centralisers* to be normal too. They are not. In $S_3$, the centraliser $C_{S_3}((1\,2)) = \{e, (1\,2)\}$ is *not* a [[Def - Normal Subgroup|normal subgroup]]: conjugating $(1\,2)$ by $(1\,3)$ gives $(2\,3) \notin \{e,(1\,2)\}$. The centraliser is the *stabiliser* of a point, and stabilisers of points in the same orbit are only conjugate to one another, not equal — so a centraliser is normal only in special circumstances. What *is* always true is $C_G(g) \trianglelefteq N_G(\langle g\rangle)$ and that conjugate elements have conjugate centralisers, $C_G(hgh^{-1}) = h\,C_G(g)\,h^{-1}$.

**Is NOT an instance — the centre is not the set of elements commuting with the centre.** A subtle non-example: one might guess $Z(G)$ could be described as $\{h : h \text{ commutes with every element of } Z(G)\}$. But *every* element of $G$ commutes with every element of the centre — that is what centrality means — so that description gives all of $G$, not $Z(G)$. The centre is defined by commuting with *all of $G$*, not with *all of $Z(G)$*; the quantifier ranges over the whole group.

**Corollary — $g$ is central if and only if its conjugacy class is a singleton.** The element $g$ lies in $Z(G)$ exactly when $\operatorname{ccl}_G(g) = \{g\}$, equivalently (by orbit-stabiliser) when $C_G(g) = G$. This is the bridge to the [[Thm - The Class Equation|class equation]]: the singleton classes are precisely the central elements, so the class equation isolates $|Z(G)|$ as the sum of the size-$1$ classes.

**Corollary — $G$ abelian if and only if $Z(G) = G$ if and only if every centraliser is all of $G$.** A group is [[Def - Abelian Group|abelian]] exactly when every pair commutes, i.e. every element commutes with every element, i.e. $C_G(g) = G$ for all $g$, i.e. $\bigcap_g C_G(g) = Z(G) = G$. The three conditions are restatements of one another, and verifying their equivalence is the calibration check for understanding both definitions.

**Corollary — $G/Z(G)$ cyclic forces $G$ abelian.** A famous and useful consequence: if the quotient $G/Z(G)$ is [[Def - Cyclic Group|cyclic]], then $G$ is abelian (so in fact $G/Z(G)$ was trivial). The reason is that if $G/Z(G) = \langle gZ(G)\rangle$, every element of $G$ has the form $g^k z$ with $z$ central, and any two such elements commute because powers of $g$ commute with each other and central elements commute with everything. The contrapositive is the working form: a non-abelian group can *never* have cyclic central quotient — so for a non-abelian group of order $p^3$, the centre has order exactly $p$, not $p^2$.

---

# Unlocked by This

> [!tip] The Class Equation *(from this topic)*
> The centraliser is the denominator in the class-size formula $|\operatorname{ccl}_G(g)| = |G : C_G(g)|$, and the centre collects the singleton classes. Putting these together gives the [[Thm - The Class Equation|class equation]] $|G| = |Z(G)| + \sum_i |G : C_G(x_i)|$, the identity that proves $p$-groups have non-trivial centre and underpins the Sylow theorems.

> [!tip] Inner Automorphisms and $G/Z(G) \cong \operatorname{Inn}(G)$ *(from this topic)*
> The centre is the kernel of the conjugation homomorphism $G \to \operatorname{Aut}(G)$. By the [[Thm - First Isomorphism Theorem|first isomorphism theorem]] the image — the group $\operatorname{Inn}(G)$ of [[Def - Automorphism Group|inner automorphisms]] — satisfies $G/Z(G) \cong \operatorname{Inn}(G)$. The centre is precisely the obstruction to $G$ acting faithfully on itself by conjugation.

> [!tip] Schur's Lemma and Central Characters *(from Representation Theory)*
> For an irreducible representation $\rho : G \to \mathrm{GL}(V)$, Schur's lemma says the centraliser of $\rho(G)$ in the matrix algebra is just the scalars. Consequently every central element acts as a scalar — the *central character* — and the centre $Z(G)$ controls how representations decompose.
