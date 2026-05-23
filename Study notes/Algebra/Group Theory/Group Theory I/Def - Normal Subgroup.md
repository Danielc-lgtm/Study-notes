---
type: definition
subject: group-theory
prereqs:
  - "Def - Subgroup"
  - "Def - Coset"
  - "Def - Abelian Group"
tags: [algebra, group-theory]
---

# Notation

Throughout, $G$ is a group with identity $e$, and $H, N, K$ denote subgroups. We write $N \leq G$ for "$N$ is a [[Def - Subgroup|subgroup]] of $G$" and $N \trianglelefteq G$ (some authors write $N \triangleleft G$) for "$N$ is a **normal** subgroup of $G$". For $g \in G$ the [[Def - Coset|left coset]] is $gN = \{gn : n \in N\}$ and the right coset is $Ng = \{ng : n \in N\}$. The **conjugate** of an element $x$ by $g$ is $gxg^{-1}$, and the conjugate of the whole subgroup is $gNg^{-1} = \{gng^{-1} : n \in N\}$. The full symbol registry is on [[Group Theory I — §1.1–1.2]].

---

# Axiom Motivation

The right way to discover this definition is not to be handed it, but to *need* it. So suppose we have a subgroup $H \leq G$ and we want to do something with the [[Def - Coset|cosets]] of $H$ — specifically, we want to make the collection of [[Def - Coset|cosets]] $G/H = \{gH : g \in G\}$ into a [[Def - Group|group]] in its own right. This is the single most useful construction in group theory, because it lets us "divide" a group by a piece of itself. The question is whether it can be done at all, and the answer will *force* the definition of normality upon us.

To make $G/H$ a group we need a multiplication on [[Def - Coset|cosets]]. There is exactly one formula that has any chance of being natural, namely
$$(g_1 H)(g_2 H) := g_1 g_2 H,$$
multiply the representatives, then take the coset. The desideratum is simply that this be a sensible operation — and the danger is hiding in plain sight. A coset has many names: $gH = g'H$ whenever $g$ and $g'$ differ by an element of $H$ (precisely, whenever $g^{-1}g' \in H$). The formula above is written in terms of *representatives* $g_1, g_2$, but the *output* must depend only on the cosets themselves, not on which names we happened to pick. An operation that gives different answers for different names of the same input is not an operation at all. So the entire question is: **is coset multiplication well-defined?**

Let us test it. Suppose we re-name the second coset, replacing $g_2$ by $g_2' = g_2 h$ for some $h \in H$ (this is the general way to get another representative of $g_2 H$). Then
$$(g_1 H)(g_2' H) = g_1 g_2' H = g_1 g_2 h H = g_1 g_2 H = (g_1 H)(g_2 H),$$
using $hH = H$. Re-naming the *second* factor causes no trouble. Now re-name the *first* factor instead, $g_1' = g_1 h$:
$$(g_1' H)(g_2 H) = g_1' g_2 H = g_1 h g_2 H.$$
For the operation to be well-defined we need this to equal $g_1 g_2 H$, i.e. we need $g_1 h g_2 H = g_1 g_2 H$. Cancelling $g_1$ on the left, the requirement is $h g_2 H = g_2 H$, which says $(g_2)^{-1} h g_2 \in H$. We need this for *every* $h \in H$ and — since $g_1$ was arbitrary, so $g_1' = g_1 h$ ranges over everything — *every* $g_2 \in G$.

So the multiplication of cosets is well-defined **if and only if** $g^{-1} h g \in H$ for all $h \in H$ and all $g \in G$. That condition is not automatic; it is a genuine restriction on $H$. A subgroup that satisfies it is exactly what we will call **normal**. The definition is not arbitrary technical baggage — it is the precise, minimal, necessary-and-sufficient condition under which a group can be divided by a subgroup.

What goes wrong if we *weaken* the condition — drop it and try to quotient by an arbitrary subgroup anyway? Take $G = S_3$ and $H = \langle (1\,2)\rangle = \{e, (1\,2)\}$, a subgroup of order $2$. Conjugating $(1\,2)$ by $(1\,3)$ gives $(1\,3)(1\,2)(1\,3) = (2\,3) \notin H$, so $H$ is not normal. Concretely, the coset products clash: $(1\,3)H$ and $(2\,3)H$ are both well-defined cosets, but $\big((1\,3)H\big)\big((1\,2)H\big)$ comes out differently depending on whether we write the first coset as $(1\,3)H$ or as $\big((1\,3)(1\,2)\big)H = (1\,3\,2)H$ — and $(1\,3)(1\,2) = (1\,3\,2)$ does name the same coset, since $(1\,2) \in H$. The "group" $G/H$ simply does not exist. The set of cosets still exists, and $G$ still acts on it, but there is no group structure.

There is no useful *strengthening* to consider: normality is already exactly the kernel-like [[Def - Subgroup|subgroups]], the most permissive condition that makes quotients work. If you strengthen it to "every element of $G$ commutes with every element of $H$" you get the much smaller class of *central* [[Def - Subgroup|subgroups]], and you would lose most interesting quotients — for instance you could no longer form $S_n / A_n$, because $A_n$ is normal but very far from central. The lesson is that normality is the Goldilocks condition: weaker and quotients break, stronger and quotients become rare.

---

# The Definition

A subgroup $N \leq G$ is a **normal subgroup**, written $N \trianglelefteq G$, if it is invariant under conjugation by every element of $G$:
$$g^{-1} n g \in N \qquad \text{for all } n \in N,\ g \in G.$$

Equivalently — and these four characterisations are all the same condition wearing different clothes — $N \trianglelefteq G$ if any one (hence all) of the following holds:

1. **Conjugation-invariance.** $gNg^{-1} = N$ for every $g \in G$. (One must show that the apparently weaker $gNg^{-1} \subseteq N$ for all $g$ already gives equality: applying the containment with $g^{-1}$ in place of $g$ yields the reverse inclusion. So "$\subseteq$ for all $g$" upgrades to "$=$ for all $g$" automatically.)

2. **Left cosets equal right cosets.** $gN = Ng$ for every $g \in G$. This is just (1) right-multiplied by $g$: from $gNg^{-1} = N$ we get $gN = Ng$, and conversely. Note this does *not* say $gn = ng$ for individual elements — it says the two *sets* coincide.

3. **Union of conjugacy classes.** $N$ is a union of [[Def - Conjugacy Class|conjugacy classes]] of $G$. The conjugacy class of $x$ is $\{gxg^{-1} : g \in G\}$; condition (1) says that if $x \in N$ then its entire class lies in $N$, so $N$ is a union of whole classes (and conversely any union of classes that happens to be a subgroup is normal).

4. **Kernel of a homomorphism.** $N = \ker\varphi$ for some [[Def - Homomorphism|homomorphism]] $\varphi : G \to H$ to some group $H$. Every kernel is normal (see [[Def - Kernel and Image]]), and conversely every normal $N$ is the kernel of the quotient map $G \to G/N$ (see [[Def - Quotient Group]]). This is the operationally most useful characterisation, even though it is the least obvious.

---

# Relate to Other Fields / Compression

Normality is the group-theoretic instance of a pattern that recurs in every algebraic theory: *the substructures by which you are allowed to quotient*. In ring theory the analogue of a normal subgroup is a [[Def - Ideal|two-sided ideal]] — a subring $I$ is an ideal precisely when $rIr$-type absorption holds, and that is exactly the condition making the quotient ring $R/I$ well-defined, derived by the same "must not depend on the representative" argument. In module theory the analogue is a **submodule**, and *every* submodule works, because a module's addition is abelian — which is the module-theoretic echo of the fact (below) that every subgroup of an [[Def - Abelian Group|abelian group]] is normal. In linear algebra the analogue is a **subspace**, and again every subspace works. The reason these all look alike is that they *are* alike: each is the kernel-class of structure-preserving maps in its category, and the first isomorphism theorem in each setting is one theorem specialised. So the apparent novelty of "normal subgroup" dissolves: it is simply "kernel" in the category of groups, and a group is the one place among these where the condition is non-trivial, because group multiplication need not be commutative.

A second compression: normality is exactly the condition that the conjugation action of $G$ on its subsets *fixes* $N$. The map $x \mapsto gxg^{-1}$ is an automorphism of $G$ (an inner automorphism), and $N \trianglelefteq G$ says $N$ is fixed by every inner automorphism — it is a "$G$-invariant subset that is also a subgroup". A subgroup fixed by *all* automorphisms, not just inner ones, is called characteristic, and is the strengthening relevant when one needs normality to transfer up a tower (see the non-transitivity remark below).

---

# Examples / Corollaries

**Is an instance — $\mathrm{SL}_n \trianglelefteq \mathrm{GL}_n$.** The special linear group $\mathrm{SL}_n(\mathbb{R})$ of determinant-$1$ matrices is normal in the general linear group $\mathrm{GL}_n(\mathbb{R})$. The cleanest proof is characterisation (4): $\mathrm{SL}_n = \ker(\det)$, where $\det : \mathrm{GL}_n(\mathbb{R}) \to \mathbb{R}^\times$ is a [[Def - Homomorphism|homomorphism]], so it is normal for free. Directly: for $A \in \mathrm{SL}_n$ and $B \in \mathrm{GL}_n$, $\det(BAB^{-1}) = \det(B)\det(A)\det(B)^{-1} = \det(A) = 1$, so $BAB^{-1} \in \mathrm{SL}_n$.

**Is an instance — $A_n \trianglelefteq S_n$.** The alternating group $A_n$ of even permutations is normal in the symmetric group $S_n$. Again the slick argument is (4): $A_n = \ker(\operatorname{sgn})$ for the sign homomorphism $\operatorname{sgn} : S_n \to \{\pm 1\}$. One could also note that $A_n$ has [[Def - Coset|index]] $2$ in $S_n$, and any index-$2$ subgroup is normal (corollary below).

**Is an instance — every subgroup of an abelian group.** If $G$ is [[Def - Abelian Group|abelian]] then for any subgroup $H$ and any $g$, $g^{-1}hg = g^{-1}gh = h \in H$, so $H \trianglelefteq G$ automatically. This is why abelian [[Def - Group|groups]] are so quotient-rich: there is no normality obstruction at all, and every subgroup gives a quotient.

**Is NOT an instance — $\langle(1\,2)\rangle$ in $S_3$.** The subgroup $H = \{e, (1\,2)\}$ of $S_3$ is *not* normal. Conjugating: $(1\,3)(1\,2)(1\,3)^{-1} = (1\,3)(1\,2)(1\,3) = (2\,3)$, which is not in $H$. Equivalently the left coset $(1\,3)H = \{(1\,3),(1\,3\,2)\}$ and the right coset $H(1\,3) = \{(1\,3),(1\,2\,3)\}$ differ. This is the canonical witness that quotients can fail: $S_3 / H$ is not a group.

**Is NOT an instance — non-transitivity of normality.** Normality is *not* a transitive relation: $K \trianglelefteq H$ and $H \trianglelefteq G$ do **not** imply $K \trianglelefteq G$. The standard witness lives in the dihedral group $D_8$ of order $8$ (symmetries of the square). Let $H$ be the Klein four-subgroup $\{e, r^2, s, r^2 s\}$ (with $r$ the rotation by a quarter turn and $s$ a reflection); $H$ has index $2$ in $D_8$, so $H \trianglelefteq D_8$. Let $K = \{e, s\}$. Then $K$ has index $2$ in $H$, so $K \trianglelefteq H$. But $K$ is not normal in $D_8$: conjugating $s$ by $r$ gives $r s r^{-1} = r^2 s \notin K$. The point is structural — normality is a relation *between a subgroup and one specific overgroup*, not an intrinsic property of $H$. The reason transitivity fails is that conjugation by elements of $G$ that lie *outside* $H$ is never tested when we only know $K \trianglelefteq H$. The fix, when transitivity is genuinely needed, is the stronger notion of a **characteristic** subgroup (invariant under *all* automorphisms): characteristic-in-normal *is* normal, and characteristic-in-characteristic is characteristic.

**Corollary — index $2$ forces normality.** Any subgroup $H \leq G$ with $|G : H| = 2$ is normal. There are only two left cosets, $H$ itself and its complement $G \setminus H$; likewise two right cosets, $H$ and $G \setminus H$. For $g \in H$, $gH = H = Hg$; for $g \notin H$, both $gH$ and $Hg$ must equal the complement $G \setminus H$. So $gH = Hg$ for all $g$, which is characterisation (2). This is the cheapest normality argument in existence — no conjugation needed.

**Corollary — the trivial and improper subgroups are always normal.** Both $\{e\}$ and $G$ satisfy $gNg^{-1} = N$ trivially. A group whose *only* normal subgroups are these two is a [[Def - Simple Group|simple group]] — the "unquotientable" atoms.

**Calibration check.** Verify that the centre $Z(G) = \{z \in G : zg = gz \ \forall g\}$ is always normal (each element is its own conjugacy class, so $Z(G)$ is a union of classes), and that the intersection of any family of normal subgroups is normal (conjugation distributes over intersection). If you can also explain *why* $gNg^{-1} \subseteq N$ for all $g$ already gives $gNg^{-1} = N$, you have understood the definition.

---

# Unlocked by This

> [!tip] Quotient Group *(from this topic)*
> Normality is precisely the licence to form the [[Def - Quotient Group|quotient group]] $G/N$. The entire payoff of this definition is the next one: with $N \trianglelefteq G$ in hand, coset multiplication is well-defined and $G/N$ is a group.

> [!tip] Composition Series and the Classification of Finite Simple Groups *(from Group Theory III)*
> Iterating "find a normal subgroup, quotient by it" produces a [[Thm - Composition Series|composition series]], expressing every finite group as a tower built from [[Def - Simple Group|simple]] pieces. Normality is the relation along which the tower is assembled.

> [!tip] Ideals and Quotient Rings *(from Ring Theory)*
> The notion of a [[Def - Ideal|two-sided ideal]] in a ring is normality transplanted: it is the exact substructure by which a ring may be quotiented, and the ring isomorphism theorems are the group ones re-run with "normal subgroup" replaced by "ideal".
