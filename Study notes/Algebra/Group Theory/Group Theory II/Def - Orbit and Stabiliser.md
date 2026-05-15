---
type: definition
subject: group-theory
prereqs:
  - "Def - Group"
  - "Def - Subgroup"
  - "Def - Group Action"
  - "Def - Coset"
tags: [algebra, group-theory]
---

# Notation

Let a group $G$ act on a set $X$ (see [[Def - Group Action]]). For a point $x \in X$:

- the **orbit** of $x$ is $G \cdot x = \{g \cdot x : g \in G\} \subseteq X$ — everywhere $x$ can be sent;
- the **stabiliser** of $x$ is $G_x = \operatorname{Stab}_G(x) = \{g \in G : g \cdot x = x\} \subseteq G$ — everything in $G$ that fixes $x$.

For a group element $g \in G$, the **fixed-point set** is $X^g = \{x \in X : g \cdot x = x\} \subseteq X$ — everything fixed by $g$. The two notations $G_x$ (subscript a *point*, a subset of $G$) and $X^g$ (superscript a *group element*, a subset of $X$) are dual and easy to confuse: $G_x$ collects group elements, $X^g$ collects points. See [[Group Theory II — §1.3–1.4]] for the full notation registry.

---

# Axiom Motivation

Suppose a group $G$ [[Def - Group Action|acts]] on a set $X$. The action is a single global object — a homomorphism $G \to \operatorname{Sym}(X)$ — but to *use* it you must take measurements at individual points. Fix one point $x \in X$ and ask the two most natural questions you could possibly ask about it. **Where can $x$ go?** And **what leaves $x$ alone?** These two questions are not arbitrary; they are *complementary*, and together they exhaust the local information the action carries about $x$. The orbit answers the first, the stabiliser the second, and the entire counting theory of this topic is the discovery that the two answers multiply to $|G|$.

**Inventing the orbit.** "Where can $x$ go" means: collect every point reachable from $x$ by some group element, $\{g \cdot x : g \in G\}$. This set is forced — there is nothing to choose. But notice it is not just any subset of $X$; it has hidden structure that is the real reason it deserves a name. First, $x$ itself is in it ($e \cdot x = x$). Second, if you are anywhere in the orbit you can still get anywhere in the orbit — from $g \cdot x$ you reach $h \cdot x$ by applying $hg^{-1}$. So "being in the same orbit" is an *equivalence relation* on $X$: reflexive (identity), symmetric (inverses), transitive (compatibility) — these are exactly the three [[Def - Group Action|action axioms]] cashed out. An equivalence relation **partitions** the set, and that is the desideratum the orbit is built to satisfy: the orbits chop $X$ into disjoint pieces, each piece a self-contained world the action shuffles internally and never mixes with another. This is why the orbit, not some other subset, is the right object: it is the indecomposable unit of an action. What breaks if you weakened "reachable by *some* $g$" to "reachable by $g$ in some fixed subset $S \subseteq G$"? You would get the set $S \cdot x$, which in general is *not* closed under the action and does *not* partition $X$ — the equivalence-relation structure, hence the partition, hence the entire theory, would be lost. The orbit must use the whole group.

**Inventing the stabiliser.** "What leaves $x$ alone" means: collect every group element fixing $x$, $\{g : g \cdot x = x\}$. Again forced — but again the point is the hidden structure. This set is closed under multiplication (if $g, h$ both fix $x$ then $gh$ fixes $x$), contains $e$, and is closed under inverses (if $g \cdot x = x$ then $g^{-1}\cdot x = x$). Those are exactly the [[Def - Subgroup|subgroup]] axioms: the stabiliser is *always a subgroup of $G$*. That is the desideratum — and it is what makes the stabiliser combine with [[Thm - Lagrange's Theorem|Lagrange's theorem]]. If you weakened "fixes $x$" to "moves $x$ by at most a little" (in a setting where "a little" made sense) you would get a subset that is *not* a subgroup, and the divisibility statement $|G_x| \mid |G|$ — the whole arithmetic payoff — would evaporate. The stabiliser must be the *exact* fixers, because only the exact fixers form a subgroup.

**Why they are complementary, and why this is the point.** Here is the desideratum that *forces* studying orbit and stabiliser *together*. Two group elements $g_1, g_2$ send $x$ to the *same* place exactly when $g_2^{-1}g_1$ fixes $x$, i.e. exactly when $g_1, g_2$ lie in the same left [[Def - Coset|coset]] of the stabiliser $G_x$. So the map $g \mapsto g \cdot x$ is constant on cosets of $G_x$ and distinguishes different cosets — it descends to a *bijection* between the cosets $G/G_x$ and the orbit $G\cdot x$. The orbit and the stabiliser are therefore not two independent measurements; they are two readings of one structure, related by $|\text{orbit}| = |G : G_x|$. This is the [[Thm - Orbit-Stabiliser Theorem|orbit-stabiliser theorem]], and it is the reason a single page defines both: "how far $x$ moves" and "how much of $G$ ignores $x$" are *the same information counted two ways*, and $|G \cdot x|\cdot|G_x| = |G|$ is the conservation law between them. Defining the orbit without the stabiliser, or conversely, would hide exactly the relationship that makes either one useful.

**Inventing the fixed-point set.** The stabiliser fixes a *point* and varies the group element; turn the roles around. Fix a group element $g$ and ask which *points* it leaves alone: $X^g = \{x : g \cdot x = x\}$. This is the natural dual of the stabiliser — $g \in G_x$ and $x \in X^g$ are *the same statement*, $g \cdot x = x$, read with one or the other argument held fixed. The fixed-point set is the right object whenever you want to average or count over the group rather than over a single point: summing $|X^g|$ over all $g$ counts incidences $\{(g,x) : g\cdot x = x\}$, and that double count is the content of Burnside's lemma. The desideratum for naming $X^g$ separately is that point-data and element-data are genuinely different slices of the same incidence relation, and problems come in both flavours.

---

# The Definition

Throughout, let the group $G$ act on the set $X$, with the action written $(g, x) \mapsto g \cdot x$.

### Orbit

The **orbit** of a point $x \in X$ under the action of $G$ is the subset of $X$

$$G \cdot x \ = \ \{\, g \cdot x \ : \ g \in G \,\} \ \subseteq \ X,$$

the set of all points to which $x$ can be moved by some element of $G$. The orbits form a **partition** of $X$: every point lies in its own orbit, and two orbits are either equal or disjoint, because "$y$ lies in the orbit of $x$" is an equivalence relation on $X$. The action is **transitive** when there is exactly one orbit, i.e. $G \cdot x = X$ for some (equivalently every) $x$.

### Stabiliser

The **stabiliser** of a point $x \in X$ under the action of $G$ is the subset of $G$

$$G_x \ = \ \operatorname{Stab}_G(x) \ = \ \{\, g \in G \ : \ g \cdot x = x \,\} \ \subseteq \ G,$$

the set of all group elements that fix $x$. The stabiliser is always a [[Def - Subgroup|subgroup]] of $G$: it contains the identity (since $e \cdot x = x$), is closed under multiplication (if $g \cdot x = x$ and $h \cdot x = x$ then $(gh)\cdot x = g\cdot(h\cdot x) = g \cdot x = x$), and is closed under inverses (if $g \cdot x = x$ then $g^{-1}\cdot x = g^{-1}\cdot(g\cdot x) = (g^{-1}g)\cdot x = x$). It need not be a [[Def - Normal Subgroup|normal]] subgroup.

### Fixed-point set

For a group element $g \in G$, the **fixed-point set** of $g$ is the subset of $X$

$$X^g \ = \ \{\, x \in X \ : \ g \cdot x = x \,\} \ \subseteq \ X,$$

the set of all points fixed by $g$. It is the "transpose" of the stabiliser: $x \in X^g \iff g \in G_x \iff g\cdot x = x$.

### The relations among them

Two facts tie the definitions together, both proved in [[Thm - Orbit-Stabiliser Theorem]].

1. **Orbit-stabiliser correspondence.** The map $g\,G_x \mapsto g \cdot x$ is a well-defined bijection from the set of left [[Def - Coset|cosets]] $G/G_x$ to the orbit $G \cdot x$. Hence, for finite $G$,
$$|G \cdot x| \ = \ |G : G_x| \ = \ \frac{|G|}{|G_x|}, \qquad\text{so}\qquad |G| \ = \ |G \cdot x|\cdot|G_x|.$$
2. **Stabilisers along an orbit are conjugate.** If $y = g \cdot x$ lies in the orbit of $x$, then
$$G_y \ = \ G_{g\cdot x} \ = \ g\,G_x\,g^{-1}.$$
In particular all points of a single orbit have *conjugate*, hence [[Def - Isomorphism|isomorphic]], stabilisers — they need not be equal.

---

# Relate to Other Fields / Compression

The orbit is **the equivalence class of $x$ under the "reachability" relation**, and the partition of $X$ into orbits is one more instance of the universal fact that an equivalence relation partitions a set into classes. What makes the group case special is that the equivalence relation is *generated by a group*: $x \sim y$ if and only if some $g$ carries $x$ to $y$. This is the same construction as the partition of a group into [[Def - Coset|cosets]] of a subgroup — there the acting group is the subgroup $H$ acting by translation, and the orbits are the cosets — so "orbits partition $X$" and "cosets partition $G$" are literally the same theorem, [[Thm - Orbit-Stabiliser Theorem|orbit-stabiliser]] containing [[Thm - Lagrange's Theorem|Lagrange]] as the special case of the regular action.

The stabiliser is the group-theoretic shadow of the **isotropy** or **little group** of physics, and of the **kernel of a map at a point**. In a continuous symmetry — say the rotation group acting on space — the stabiliser of a point is the subgroup of rotations fixing it, the "little group" at that point; in physics this is exactly how the rotation group sorts the points of space into orbits (spheres) each carrying its own isotropy ($SO(2)$ at a generic point, $SO(3)$ at the origin). More abstractly, the stabiliser is what you get from the [[Def - Kernel and Image|kernel]] idea localised: $\ker$ of the global action is $\bigcap_x G_x$, the elements fixing *every* point, and $G_x$ is the one-point version.

The fixed-point set $X^g$ is the discrete-group analogue of the **fixed-point set of a dynamical map** and the object measured by **fixed-point theorems**. For a single transformation, $X^g$ is the set of equilibria; the Lefschetz fixed-point theorem, the Brouwer theorem, and Burnside's orbit-counting lemma are all statements about the size or non-emptiness of fixed-point sets. The orbit-counting lemma in particular — number of orbits equals $\frac{1}{|G|}\sum_g |X^g|$ — *is* a fixed-point theorem: it extracts a global invariant (orbit count) from fixed-point data.

---

# Examples / Corollaries

**Is an instance: orbits of a rotation.** Let $G = C_n$ act on the plane $\mathbb{R}^2$ by rotation about the origin through multiples of $2\pi/n$. The orbit of a point $x \neq 0$ is the set of $n$ vertices of a regular $n$-gon through $x$; the orbit of the origin is $\{0\}$, a single point. The stabiliser of $x \neq 0$ is the trivial subgroup $\{e\}$ (only the identity rotation fixes a non-central point), while the stabiliser of the origin is all of $C_n$. This single example shows orbits of one action come in different sizes and stabilisers of different points differ — see the non-examples below.

**Is an instance: the conjugation action.** Let $G$ act on its own underlying set by $g \cdot x = gxg^{-1}$. The orbit of $x$ is its [[Def - Conjugacy Class|conjugacy class]] $\{gxg^{-1} : g \in G\}$; the stabiliser of $x$ is its [[Def - Centraliser and Centre|centraliser]] $C_G(x) = \{g : gx = xg\}$; the fixed-point set $X^g$ is $\{x : gxg^{-1} = x\} = \{x : gx = xg\}$, again a centraliser. The points whose orbit is a singleton are exactly the central elements, and the [[Thm - The Class Equation|class equation]] is orbit-stabiliser for this action summed over orbits.

**Is an instance: $S_n$ on $\{1,\dots,n\}$, the transitive case.** The [[Def - Symmetric Group|symmetric group]] acting by $\sigma \cdot i = \sigma(i)$ has a single orbit — any point can be sent to any other — so the action is **transitive**, $G \cdot 1 = \{1,\dots,n\}$. The stabiliser of the point $n$ is the set of permutations fixing $n$, namely a copy of $S_{n-1}$, and orbit-stabiliser reads $n! = |G\cdot n|\cdot|G_n| = n \cdot (n-1)!$ — a sanity check.

**Is an instance: $D_8$ on the corners of a square.** The dihedral group of order $8$ acts on the $4$ corners. The action is transitive (orbit of any corner is all $4$ corners). The stabiliser of a fixed corner is the order-$2$ subgroup $\{e, r\}$ where $r$ is the reflection in the diagonal through that corner; orbit-stabiliser gives $8 = 4 \cdot 2$. The stabilisers of *different* corners are different order-$2$ subgroups — conjugate, not equal.

**Is NOT an instance of an orbit: an arbitrary $G$-invariant subset.** Take $C_4$ acting on the four corners of a square, and let $Y$ be a pair of *opposite* corners. The set $Y$ is invariant under the subgroup $\{e, r^2\}$, and one might mistake it for an orbit. It is **not** an orbit of $C_4$: the orbit of any corner under the full $C_4$ is all four corners, since the generating rotation cycles them. $Y$ is a union of... no — $Y$ is not even a union of $C_4$-orbits, since the only $C_4$-orbit here is the whole set. An orbit is reachability under the *whole* group; an invariant subset for a *subgroup* is a different and weaker thing. This non-example isolates that the orbit uses all of $G$.

**Is NOT an instance of a stabiliser: the set of elements moving $x$ "a little".** The notion of stabiliser is *exact*: $G_x$ is the elements fixing $x$ outright. In $S_4$ acting on $\{1,2,3,4\}$, the set of permutations sending $1$ to $1$ *or* to $2$ is $\{\sigma : \sigma(1) \in \{1,2\}\}$; this is **not** a stabiliser and **not a subgroup** — it contains $(1\,2)$ and $(2\,3)$ but their product $(1\,2)(2\,3) = (1\,2\,3)$ sends $1 \mapsto 2$... actually sends $1\mapsto 2 \in \{1,2\}$, but it also contains $(1\,2)$ and the transposition $(1\,2)(1\,3)=(1\,3\,2)$ sends $1 \mapsto 3 \notin\{1,2\}$, so the set is not closed. The stabiliser $G_1$, the *exact* fixers of $1$, is the genuine subgroup $S_{\{2,3,4\}}\cong S_3$. This non-example pins down why the stabiliser must be the exact fixers — only then is it a subgroup.

**Corollary (stabiliser is a subgroup).** $G_x \leq G$ for every $x$, by the identity / closure / inverse check in [[#The Definition]]. *Calibration check:* this is what licenses applying [[Thm - Lagrange's Theorem|Lagrange's theorem]] to $G_x$ and concluding $|G_x| \mid |G|$.

**Corollary (orbits partition $X$).** The relation "$x \sim y$ if and only if $y \in G \cdot x$" is reflexive, symmetric, and transitive — one consequence of each of the [[Def - Group Action|action axioms]] together with group inverses — so $X$ is the disjoint union of its orbits. *Calibration check:* this is why one may count $|X|$ by summing orbit sizes, the structural form of the [[Thm - The Class Equation|class equation]].

**Corollary (orbit size divides $|G|$).** For finite $G$, $|G \cdot x| = |G : G_x|$ divides $|G|$, by the orbit-stabiliser correspondence. *Calibration check:* an action of a group of order $12$ can have orbits of size $1, 2, 3, 4, 6, 12$ but never of size $5$ — orbit sizes are constrained before any other information is used.

**Corollary (stabilisers in one orbit are conjugate).** If $y = g\cdot x$ then $G_y = gG_xg^{-1}$: if $h$ fixes $x$ then $ghg^{-1}$ fixes $g\cdot x = y$, and conversely. *Calibration check:* one may speak of "the stabiliser type" of a transitive action — a single conjugacy class of subgroups — but never of "the stabiliser" as one fixed subgroup, unless the stabiliser happens to be [[Def - Normal Subgroup|normal]].

**Corollary ($G_x$ and $X^g$ are transposes).** For all $g \in G$, $x \in X$: $g \in G_x \iff x \in X^g$. Hence $\sum_{x \in X}|G_x| = \sum_{g \in G}|X^g|$, both sides counting the incidence set $\{(g,x) : g\cdot x = x\}$. This double count is the proof of Burnside's orbit-counting lemma.

**Corollary (faithful action $\iff$ stabilisers intersect trivially).** The action is [[Def - Group Action|faithful]] exactly when $\bigcap_{x \in X} G_x = \{e\}$, since an element fixing every point lies in every stabiliser and acts as the identity permutation. The global kernel of the action is the intersection of all stabilisers.

---

# Unlocked by This

> [!tip] Orbit-Stabiliser Theorem *(from Group Theory II, §1.3)*
> With orbit and stabiliser in hand, the [[Thm - Orbit-Stabiliser Theorem|orbit-stabiliser theorem]] $|G| = |G\cdot x|\cdot|G_x|$ becomes available — the master counting theorem of finite group theory, and the engine behind the [[Thm - The Class Equation|class equation]] and the Sylow theorems.

> [!tip] Burnside's Orbit-Counting Lemma *(from Enumerative Combinatorics)*
> Averaging the fixed-point counts, $\#(\text{orbits}) = \frac{1}{|G|}\sum_{g\in G}|X^g|$, turns the orbit concept into a counting engine for configurations up to symmetry — necklaces, coloured polyhedra, isomers — and generalises to Pólya enumeration.

> [!tip] Orbifolds and Quotient Spaces *(from Differential Geometry)*
> When a group acts on a geometric space, the set of orbits $X/G$ is itself a space — a quotient manifold when the action is free and proper, an orbifold in general — and the stabilisers record the singular points. The orbit space is how symmetry reduces the dimension of a problem.
