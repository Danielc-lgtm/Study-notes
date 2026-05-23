---
type: definition
subject: group-theory
prereqs:
  - "Def - Group"
  - "Def - Subgroup"
  - "Def - Symmetric Group"
  - "Def - Isomorphism"
tags: [algebra, group-theory]
---

# Notation

A **permutation group** is a [[Def - Subgroup|subgroup]] $G \leq \operatorname{Sym}(X)$ of the [[Def - Symmetric Group|symmetric group]] of some set $X$ — a group consisting of *some*, not necessarily all, bijections of $X$, closed under composition and inverses and containing the identity map. The **degree** of the permutation group is $|X|$, the size of the set being permuted. The symbol $\operatorname{Sym}(X)$ denotes all bijections $X \to X$; $S_n$ is $\operatorname{Sym}(\{1,\dots,n\})$. See [[Group Theory II — §1.3–1.4]] for the full notation registry.

---

# Axiom Motivation

The motivation here is not "what structure should this object have" — the structure is already fixed, it is just *being a group* — but "**why carve out this particular class of [[Def - Group|groups]] and give it a name**". The honest answer requires acknowledging something unusual about this definition, which the source lecture notes themselves flag: as an abstract classification of [[Def - Group|groups]] it is *vacuous*, because by [[Thm - Cayley's Theorem|Cayley's theorem]] every group is isomorphic to a permutation group. So the desideratum cannot be "single out a special kind of group". It must be something else, and seeing what makes the definition worth stating is the real content.

Begin with the concrete situation it abstracts. In [[Def - Symmetric Group|the symmetric group]] you take *all* bijections of a set. But that is frequently more than you want. The symmetries of a square are eight specific permutations of its four corners, not all $24$; the rotations of a cube are $24$ specific permutations of its six faces, not all $720$. In each case nature hands you not the whole symmetric group but a sub-collection — the bijections that arise as *actual symmetries of the object in front of you*. We want a word for "a group that comes to us already presented as bijections of a concrete set", and the demand on that word is exactly that the collection be closed under the group operations of $\operatorname{Sym}(X)$: doing two symmetries in succession is a symmetry, undoing a symmetry is a symmetry, doing nothing is a symmetry. That demand is precisely the definition of a [[Def - Subgroup|subgroup]]. So a permutation group is forced to be "a [[Def - Subgroup|subgroup]] of $\operatorname{Sym}(X)$", with no freedom in the definition — the only thing being recorded is *the way the group is presented*.

Now confront the vacuity. Why define a class that contains everything? Because the definition is not really about *which groups* qualify; it is about **the choice of $X$**. [[Thm - Cayley's Theorem|Cayley's theorem]] says every group $G$ is isomorphic to a permutation group, but its proof presents $G$ as permutations of *itself*, a set of size $|G|$ — an enormous and structurally opaque choice. The same abstract group can be presented as a permutation group in many ways, on many different sets, and *those presentations differ wildly in usefulness*. The dihedral group $D_8$ of order $8$ is isomorphic, by Cayley, to a permutation group of degree $8$; but it is far more illuminating to present it as a permutation group of degree $4$, acting on the four corners of a square, where the rotations and reflections are visible at a glance. So the content of the definition — the thing it asks you to supply — is a *good* set $X$, one small enough and structured enough that the group's features become legible. The definition is vacuous as a classification precisely so that all its weight falls on the modelling choice.

This explains every part of the definition by what would break without it. Why insist $X$ be a *set* and the elements be *bijections*, rather than allowing arbitrary functions? Because permutation groups must be *groups*, and only bijections are invertible — non-bijections would violate the [[Def - Group|inverse axiom]] (see [[Def - Symmetric Group]] for this exact point). Why a *subgroup* and not an arbitrary subset of $\operatorname{Sym}(X)$? Because an arbitrary subset of bijections need not be closed under composition: the single transposition $(1\,2)$ together with the identity is closed, but $(1\,2)$ together with $(2\,3)$ alone is not — composing them produces a $3$-cycle that is not in the set — so an arbitrary subset is not a group and the word "group" in "permutation group" would be a lie. Why record the **degree** $|X|$? Because the degree is the one invariant of the *presentation* that matters: it bounds the group, since $G \leq \operatorname{Sym}(X)$ forces $|G| \mid |X|!$, and a presentation of small degree is the whole point. Two presentations of the same abstract group on sets of different sizes are *different* permutation groups even though they are isomorphic as abstract groups, and the degree is what distinguishes them.

There is one more thing the definition is built to make available, and it is the deepest reason the notion is not idle. A permutation group is a group that *already knows how to act* — it comes with a canonical [[Def - Group Action|action]] on $X$, the "tautological" action $g \cdot x = g(x)$ where $g$, being a bijection, is literally a function you can evaluate. For an abstract group, an action on a set $X$ is extra data you must construct. For a permutation group of degree $n$, the action on the $n$ points is *given for free* by the definition. So defining the class is the bridge from the abstract theory of [[Group Theory I — §1.1–1.2]] to the concrete, computational, orbit-and-stabiliser theory of this topic: it names the groups for which the action machinery requires no setup.

---

# The Definition

A group $G$ is a **permutation group** if it is a [[Def - Subgroup|subgroup]] of the [[Def - Symmetric Group|symmetric group]] $\operatorname{Sym}(X)$ for some set $X$:

$$G \leq \operatorname{Sym}(X).$$

That is, the elements of $G$ are bijections $X \to X$, the group operation is composition, and $G$ contains the identity map and is closed under composition and under taking inverses of its elements.

The **degree** of the permutation group $G \leq \operatorname{Sym}(X)$ is the cardinality $|X|$ of the set being permuted. A permutation group of degree $n$ is a subgroup of $\operatorname{Sym}(X)$ for a set $X$ with $|X| = n$; up to relabelling the points, this is a subgroup of $S_n$.

Two remarks fix the status of the notion. First, the definition is not a restrictive one: by [[Thm - Cayley's Theorem|Cayley's theorem]] **every** group is [[Def - Isomorphism|isomorphic]] to a permutation group, so the class of permutation groups is, up to isomorphism, the class of all groups. The content of the definition is therefore not *which* groups but the supplementary data of the set $X$ and the way $G$ permutes it. Second, the degree is a property of the *presentation* $G \leq \operatorname{Sym}(X)$, not of the abstract group: the same abstract group is a permutation group of many different degrees, according to which set one chooses to let it permute.

---

# Relate to Other Fields / Compression

A permutation group is **the image of a [[Def - Group Action|group action]]**, viewed as a subobject of $\operatorname{Sym}(X)$. By [[Thm - Actions Correspond to Homomorphisms]], an action of an abstract group $G$ on a set $X$ is the same as a [[Def - Homomorphism|homomorphism]] $\rho : G \to \operatorname{Sym}(X)$; the image $\rho(G) = G^X$ is then, by the [[Thm - First Isomorphism Theorem|first isomorphism theorem]], a permutation group [[Def - Isomorphism|isomorphic]] to $G / \ker\rho$. So "permutation group" and "faithful image of a group action" are two names for the same thing: a permutation group is precisely a group that *is* — not merely *acts on* — a set of permutations. The abstract group plus a choice of action produces a permutation group; the permutation group plus forgetting which abstract group it came from is just a group again. This is the exact relationship that makes [[Def - Group Action|actions]] and permutation groups interchangeable viewpoints.

The definition is the group-theoretic instance of a general pattern: **a concrete category versus an abstract one**. In many parts of mathematics one has an abstract object and, separately, a *representation* of it as transformations of something. A Lie algebra is abstract; a Lie algebra of vector fields is a concrete realisation. A $C^*$-algebra is abstract; an algebra of bounded operators on a Hilbert space is a concrete one, and the Gelfand–Naimark theorem says every $C^*$-algebra has such a realisation — exactly parallel to [[Thm - Cayley's Theorem|Cayley's theorem]] saying every group is a permutation group. In each case the abstract–concrete distinction is, formally, vacuous (the representation theorem closes the gap) but practically essential, because the concrete realisation is where computation happens.

---

# Examples / Corollaries

**Is an instance: the dihedral group as permutations of polygon vertices.** The dihedral group $D_{2n}$ of symmetries of a regular $n$-gon is a permutation group of degree $n$: each of its $2n$ symmetries permutes the $n$ vertices, and these $2n$ permutations form a subgroup of $S_n$. This is the *good* presentation — the rotations are the $n$-cycles' powers, the reflections are the order-$2$ elements — and it is far more transparent than the degree-$2n$ presentation Cayley's theorem would give.

**Is an instance: the symmetric group $S_n$ itself.** Trivially $S_n \leq S_n$, so $S_n$ is a permutation group of degree $n$ — the maximal one, since it contains *all* bijections. Likewise $A_n \leq S_n$ is a permutation group of degree $n$. Every [[Def - Symmetric Group|symmetric group]] and every [[Def - Symmetric Group|alternating group]] is a permutation group; the notion of permutation group is the closure of "symmetric group" under passing to [[Def - Subgroup|subgroups]].

**Is an instance: the rotation group of the cube, two ways.** The rotational symmetries of a cube form a group of order $24$. Letting it permute the $6$ faces presents it as a permutation group of degree $6$; letting it permute the $4$ space diagonals presents the *same* abstract group as a permutation group of degree $4$, and in fact realises the isomorphism with $S_4$. One abstract group, two permutation groups of different degrees — a clean illustration that degree is a feature of the presentation.

**Is an instance (via Cayley): the cyclic group $C_3$ as a degree-$3$ permutation group.** The group $C_3 = \{e, g, g^2\}$ acting on itself by left multiplication realises $C_3$ as the subgroup $\{\operatorname{id}, (1\,2\,3), (1\,3\,2)\}$ of $S_3$. This is the Cayley presentation, and for $C_3$ it happens to be a small and reasonable one; for larger groups Cayley's presentation is usually far too big to be useful, which is the whole point of the [[#Axiom Motivation]].

**Is NOT an instance, as stated: an abstract group with no chosen action.** A group $G$ defined purely by a presentation $\langle \text{generators} \mid \text{relations}\rangle$, or by its multiplication table, is not *literally* a permutation group — its elements are abstract symbols, not bijections of any set. It only *becomes* a permutation group once you supply a set $X$ and an action; until then "is a permutation group" is false on the nose, even though it is true up to isomorphism. This non-example pins down that the definition is about a *realisation*, not an isomorphism class.

**Is NOT an instance: a non-closed set of permutations.** The subset $\{\operatorname{id}, (1\,2), (2\,3)\} \subseteq S_3$ is a collection of three bijections of $\{1,2,3\}$, but it is **not** a permutation group: it is not closed under composition, since $(1\,2)(2\,3) = (1\,2\,3)$ is not in the set, and it does not contain the inverse-closure or the missing $3$-cycles needed to be a [[Def - Subgroup|subgroup]]. A permutation group must be a *subgroup* of $\operatorname{Sym}(X)$; an arbitrary set of permutations is just a set of permutations. This non-example isolates the closure requirement.

**Corollary (degree bounds order).** If $G$ is a permutation group of degree $n$, then $|G| \mid n!$, because $G \leq S_n$ and [[Thm - Lagrange's Theorem|Lagrange's theorem]] forces $|G|$ to divide $|S_n| = n!$. *Calibration check:* this is why a small degree is valuable — it caps the group's order and constrains its structure.

**Corollary (every group is a permutation group up to isomorphism).** By [[Thm - Cayley's Theorem|Cayley's theorem]], for any group $G$ the left-regular action embeds $G$ as a permutation group of degree $|G|$. Hence the abstract notion "group" and the concrete notion "permutation group" coincide up to [[Def - Isomorphism|isomorphism]] — which is exactly why the definition's value lies in the *choice* of the set, not in the class it defines.

**Corollary (minimal degree is an invariant).** Although every group is *some* permutation group, the *smallest* degree on which a given group $G$ can be faithfully presented is a genuine isomorphism invariant of $G$, the **minimal faithful degree**. For $S_n$ it is $n$ (for $n \neq 6$, with $6$ a famous exception), for $C_p$ it is $p$, and computing it for a given group is a real and sometimes hard problem. This corollary is the precise sense in which "the choice of $X$" has objective content.
