---
type: definition
subject: group-theory
prereqs:
  - "Def - Group"
  - "Def - Subgroup"
  - "Def - Group Action"
  - "Def - Orbit and Stabiliser"
  - "Def - Normal Subgroup"
  - "Def - Symmetric Group"
tags: [algebra, group-theory]
---

# Notation

Throughout, $G$ is a group with identity $e$. For $g, h \in G$, the **conjugate of $g$ by $h$** is the element $hgh^{-1}$. The **conjugacy class** of $g$ is written $\operatorname{ccl}_G(g)$, and some authors write $g^G$ for the same set; in $S_n$ contexts one also sees $[g]$. We write $\operatorname{ord}(g)$ for the order of the element $g$, and $H \trianglelefteq G$ for "$H$ is a [[Def - Normal Subgroup|normal subgroup]] of $G$". The full symbol registry for this topic is on [[Group Theory II — §1.3–1.4]].

---

# Axiom Motivation

To invent the conjugacy class you do not need to be told it exists. You need only one prior idea — that of an [[Def - Group Action|action]] and its [[Def - Orbit and Stabiliser|orbits]] — and one observation about how a group sees its own elements.

Start with the observation. A group element $g$ is an *operation*: it does something. But the same operation can be *described* in many different reference frames. Imagine you and I both look at the rotations of a cube, and you have labelled the faces one way and I have labelled them another. The rotation "turn the front face clockwise" is, abstractly, one and the same motion of the cube — but written in your labels it is some permutation, and written in my labels it is a different permutation. The two permutations are not equal as group elements, yet they are *the same operation viewed in different coordinates*. We would like a notion that collects together exactly those elements which are "the same up to change of description".

Now make "change of description" precise. A change of coordinates on $G$ is a relabelling, an [[Def - Isomorphism|isomorphism]] of $G$ with itself. The cheapest supply of such relabellings is *internal*: pick any $h \in G$ and form the map $x \mapsto hxh^{-1}$. This map relabels the world by $h$, performs $x$, then relabels back. So the element $hgh^{-1}$ is, quite literally, "$g$ performed in the coordinate system that $h$ sets up". Two elements should count as the same up to description exactly when one is $hgh^{-1}$ for some $h$.

That immediately tells us what to capture and what to exclude. We want a set that contains $g$ together with every $hgh^{-1}$, and nothing else — and we want this assignment to *partition* $G$, because "same up to relabelling" ought to be an equivalence relation: reflexive (take $h = e$), symmetric (if $g' = hgh^{-1}$ then $g = h^{-1}g'h$), transitive (compose two relabellings). The desideratum, then, is a partition of $G$ whose blocks are "$g$, in all coordinate systems".

There is a clean way to *get* such a partition for free, rather than checking the equivalence-relation axioms by hand: realise the construction as the orbits of an action. The assignment $h \cdot g := hgh^{-1}$ is an action of $G$ on the *set* $G$, the **conjugation action**. The first axiom $e \cdot g = g$ is immediate. The second, $h_1 \cdot (h_2 \cdot g) = (h_1 h_2)\cdot g$, is the computation $h_1(h_2 g h_2^{-1})h_1^{-1} = (h_1 h_2)g(h_1 h_2)^{-1}$ — note this works *because* the inverse of a product reverses, $(h_1h_2)^{-1} = h_2^{-1}h_1^{-1}$, which is exactly why we conjugate by $hgh^{-1}$ and not by, say, $hg h$. And [[Def - Orbit and Stabiliser|orbits of any action automatically partition]] the set. So defining the conjugacy class as the orbit of $g$ under conjugation hands us the partition with no extra work: this is *why* the definition is phrased as an orbit and not as a free-standing set.

What breaks if we weaken the definition? Suppose we tried to be cheaper and used only $g \mapsto hg$ — relabel by left multiplication. That is also an action (the left-regular action), but its single orbit is all of $G$: left multiplication is too strong, it moves $g$ everywhere, and the partition it induces is trivial. Conjugation is the unique two-sided combination $h(-)h^{-1}$ that *preserves the group structure* — it is the [[Def - Automorphism Group|inner automorphism]] by $h$ — and that is what makes its orbits informative rather than trivial. Weaken to one-sided multiplication and you lose the partition into meaningful blocks.

What breaks if we strengthen it — say, demand that $g$ and $g'$ be related by $hgh^{-1}$ only for $h$ in some fixed proper subgroup $H$? Then you get a *finer* partition (the $H$-conjugacy classes), which is sometimes what you want — it is exactly the move that powers the [[Thm - Simplicity of the Alternating Group|simplicity proof for Aₙ]], where $A_n$-conjugacy is strictly finer than $S_n$-conjugacy. But as the *default* notion it is wrong, because the property we are really after is "indistinguishable to $G$", and $G$ has all of itself available as relabellings. Use all of $G$ and you get the canonical equivalence; use a subgroup and you get a refinement that must be invoked deliberately.

Finally, the test that pins down *this* definition rather than a nearby variant. We will want the theorem: **a subgroup is [[Def - Normal Subgroup|normal]] if and only if it is a union of conjugacy classes.** Normality of $N$ means $hNh^{-1} = N$ for all $h$, i.e. $N$ is closed under conjugation by every $h$ — which says precisely that with each element it contains, $N$ contains that element's whole conjugacy class. If we had defined classes with one-sided multiplication, this characterisation would be false and meaningless; if we had defined them with a proper subgroup, it would detect the wrong subgroups. The conjugacy class is the orbit under the *full two-sided* action because that is the orbit whose unions are exactly the normal subgroups.

---

# The Definition

Let $G$ be a group. The **conjugacy class** of an element $g \in G$ is the set
$$\operatorname{ccl}_G(g) \;=\; \{\, hgh^{-1} : h \in G \,\}.$$

Equivalently — and this is the operationally important reformulation — $\operatorname{ccl}_G(g)$ is the [[Def - Orbit and Stabiliser|orbit]] of $g$ under the **conjugation action** of $G$ on the set $G$, the [[Def - Group Action|action]] defined by
$$h * g_1 \;:=\; h g_1 h^{-1}.$$

Two elements $g$ and $g'$ are **conjugate** (written $g \sim g'$) if $g' = hgh^{-1}$ for some $h \in G$, equivalently if $\operatorname{ccl}_G(g) = \operatorname{ccl}_G(g')$. Conjugacy is an equivalence relation, so the conjugacy classes **partition** $G$: every element lies in exactly one class, distinct classes are disjoint, and their union is all of $G$.

The identity always forms a class by itself, $\operatorname{ccl}_G(e) = \{e\}$, since $heh^{-1} = e$ for every $h$. More generally a singleton class $\operatorname{ccl}_G(g) = \{g\}$ occurs exactly when $g$ commutes with every element of $G$, that is, when $g$ lies in the [[Def - Centraliser and Centre|centre]] $Z(G)$.

---

# Categorical Definition

There is no separate categorical definition worth stating: the conjugacy class is already defined as an orbit, and orbits *are* the categorical content of a [[Def - Group Action|group action]]. It is, however, worth recording the one-line categorical placement. A group $G$ is a one-object category $\mathbf{B}G$ whose morphisms are the elements of $G$. A *functor* $F : \mathbf{B}G \to \mathbf{Set}$ is exactly a $G$-set, and the conjugation action is the particular $G$-set in which $F$ sends the single object to the underlying set $G$ and sends a morphism $h$ to the bijection $g_1 \mapsto hg_1h^{-1}$. The conjugacy classes are the connected components of the *category of elements* of this functor. The only genuinely categorical fact here is the one already used: in any $G$-set the orbits partition the set, because "lies in the same orbit" is the equivalence relation generated by the action — and that is a general fact about functors into $\mathbf{Set}$, not special to conjugation.

---

# Relate to Other Fields / Compression

The conjugacy class is one instance of a single pattern that runs through all of mathematics: **the orbit of a point under a symmetry group that acts by structure-preserving transformations**. Specialise the pattern and you recover familiar objects in other fields.

In [[Def - Symmetric Group|symmetric groups]] the pattern becomes completely concrete. Conjugating a permutation $\sigma$ by $\tau$ produces the permutation $\tau\sigma\tau^{-1}$, whose effect is to take the cycle decomposition of $\sigma$ and *rename every entry* by $\tau$: if $\sigma$ sends $i \mapsto j$ then $\tau\sigma\tau^{-1}$ sends $\tau(i)\mapsto\tau(j)$. Renaming entries cannot change the *shape* of the cycle decomposition, only the labels — so the conjugacy class of a permutation is exactly its **cycle type**, and the classes of $S_n$ are in bijection with the partitions of $n$ (see [[Thm - Conjugacy Classes of the Symmetric Group]]). This is the cleanest illustration of the slogan "conjugation is change of coordinates": in $S_n$ the coordinates are literal labels on points.

In **linear algebra** the same construction is *similarity of matrices*. Two matrices $A, B$ are similar when $B = PAP^{-1}$ for an invertible $P$ — they are conjugate in the group $\mathrm{GL}_n$. Here $P$ is a change of basis, and the conjugacy class of a matrix is the set of all matrices representing the same linear map in different bases. The invariants of the class — eigenvalues, characteristic polynomial, Jordan form — are exactly the basis-independent data of the linear map, just as the order of a group element is the description-independent data of the element. Conjugacy classes in $\mathrm{GL}_n$ *are* the Jordan canonical forms.

In **Lie theory and differential geometry** conjugacy classes of a Lie group $G$ are the orbits of $G$ acting on itself, and they are smooth submanifolds whose geometry encodes representation-theoretic data; the *adjoint orbits* in the Lie algebra (the linearised version, $X \mapsto \operatorname{Ad}(h)X$) carry canonical symplectic structures and are the phase spaces of the coadjoint-orbit method in geometric quantisation. The reader with a background in geometric mechanics has already met conjugacy classes there under the name *adjoint orbits*.

So the compression is: a conjugacy class is "an equivalence class under change of internal coordinates", and the diversity of names — cycle type, similarity class, Jordan form, adjoint orbit — is the single notion specialised to the category in which the group is acting.

---

# Examples / Corollaries

**Is an instance — the classes of $S_3$.** The symmetric group $S_3$ has six elements and exactly three conjugacy classes, organised by cycle type. The identity forms its own class $\{e\}$. The three transpositions $(1\,2), (1\,3), (2\,3)$ form a single class of size $3$ — they are all conjugate, for instance $(1\,3) = (2\,3)(1\,2)(2\,3)^{-1}$. The two $3$-cycles $(1\,2\,3), (1\,3\,2)$ form a class of size $2$. The class sizes $1 + 3 + 2 = 6 = |S_3|$, confirming that the classes partition the group.

**Is an instance — every element of an abelian group.** If $G$ is [[Def - Abelian Group|abelian]] then $hgh^{-1} = hh^{-1}g = g$ for every $h$, so $\operatorname{ccl}_G(g) = \{g\}$ — every conjugacy class is a singleton, and there are $|G|$ of them. This is the degenerate extreme: an abelian group has the maximum possible number of classes, and conjugacy carries no information. The conjugacy class is interesting precisely to the extent that $G$ is *non-abelian*.

**Is NOT an instance — a single coset.** It is tempting, having met the partition of $G$ into [[Def - Coset|cosets]] of a subgroup, to think a conjugacy class is some kind of coset. It is not. A left coset $gH$ always has size exactly $|H|$ (cosets all have the same size, by [[Thm - Lagrange's Theorem|Lagrange]]); conjugacy classes generally have *different* sizes within the same group — in $S_3$ the sizes are $1, 2, 3$, which are not all equal and need not even divide each other. Both are partitions of $G$, but a coset partition comes from a subgroup and has equal blocks, whereas the conjugacy partition comes from an action on $G$ and has blocks of assorted sizes governed by [[Thm - The Class Equation|the class equation]].

**Is NOT an instance — the set $\{hgh : h \in G\}$.** Dropping the inverse and using $hgh$ instead of $hgh^{-1}$ does *not* define a conjugacy class, and in general does not even define an orbit of an action — the assignment $h * g := hgh$ fails the action axiom because $h_1 *(h_2 * g) = h_1 h_2 g h_2 h_1 \neq (h_1h_2)g(h_1h_2)$ in a non-abelian group. The inverse is not decoration; it is what makes conjugation an [[Def - Automorphism Group|automorphism]] and hence an action.

**Corollary — conjugate elements have the same order.** If $g' = hgh^{-1}$ then $(g')^k = (hgh^{-1})^k = hg^kh^{-1}$, because all the interior $h^{-1}h$ pairs cancel. Hence $(g')^k = e$ if and only if $g^k = e$, so $g$ and $g'$ have the same order. Order is therefore a *class invariant* — a function constant on conjugacy classes. The converse fails (see the non-example below), so equal order is necessary but not sufficient for conjugacy.

**Corollary — same cycle type in $S_n$.** Specialising the previous remark to $S_n$, conjugate permutations have the same cycle type, since conjugation only renames the points (see [[Thm - Conjugacy Classes of the Symmetric Group]]). Here the converse *does* hold: cycle type is a complete invariant for conjugacy in $S_n$. Cycle type is strictly finer than order: in $S_5$ the permutation $(1\,2)(3\,4)$ and the $3$-cycle $(1\,2\,3)$ are not conjugate because their cycle types differ, but more pointedly $(1\,2\,3)(4\,5)$ has order $6$ and so does the $6$-cycle in $S_6$ — equal order, different cycle type, hence different classes. Order alone cannot separate classes; cycle type can.

**Corollary — a subgroup is normal exactly when it is a union of conjugacy classes.** A subgroup $N \leq G$ is [[Def - Normal Subgroup|normal]] if and only if $hNh^{-1} = N$ for all $h$, i.e. $N$ is closed under conjugation, i.e. with each element $N$ contains that element's entire conjugacy class. So normal subgroups are precisely the subgroups assembled from whole classes. This is the calibration check that confirms understanding: in $S_3$ the only subsets that are both subgroups and unions of classes are $\{e\}$, the $3$-cycles together with $e$ (giving $A_3$), and all of $S_3$ — and indeed those are exactly the normal subgroups of $S_3$.

**Corollary — conjugation by $h$ is an automorphism.** For each fixed $h$, the map $\gamma_h : x \mapsto hxh^{-1}$ is a bijection $G \to G$ (inverse $\gamma_{h^{-1}}$) and satisfies $\gamma_h(xy) = hxyh^{-1} = (hxh^{-1})(hyh^{-1}) = \gamma_h(x)\gamma_h(y)$, so it is an [[Def - Isomorphism|isomorphism]] of $G$ with itself — an [[Def - Automorphism Group|inner automorphism]]. The conjugacy class of $g$ is thus the union of the images $\gamma_h(g)$ over all $h$: it is "the $G$-orbit of $g$ under the inner automorphisms". This is the bridge from this page to [[Def - Automorphism Group]].

---

# Unlocked by This

> [!tip] The Class Equation *(from this topic)*
> Since each conjugacy class size equals the index $|G : C_G(g)|$ of a [[Def - Centraliser and Centre|centraliser]] (by the [[Thm - Orbit-Stabiliser Theorem|orbit-stabiliser theorem]] applied to conjugation), summing the class sizes and isolating the singletons gives the [[Thm - The Class Equation|class equation]] $|G| = |Z(G)| + \sum_i |G : C_G(x_i)|$ — the central counting identity of finite group theory.

> [!tip] Conjugacy Classes of the Symmetric Group *(from this topic)*
> The conjugacy classes of $S_n$ are exactly the cycle types, hence in bijection with partitions of $n$; see [[Thm - Conjugacy Classes of the Symmetric Group]]. This makes $S_n$ the one infinite family whose conjugacy structure is fully transparent, and it is the combinatorial input to the [[Thm - Simplicity of the Alternating Group|simplicity of Aₙ]].

> [!tip] Characters and Class Functions *(from Representation Theory)*
> A *character* of a representation $G \to \mathrm{GL}(V)$ is the function $g \mapsto \operatorname{tr}\rho(g)$, and because trace is conjugation-invariant it is constant on conjugacy classes — a [[Def - Conjugacy Class|class function]]. The number of irreducible representations of a finite group equals the number of conjugacy classes, so the partition of $G$ defined here is literally the indexing set of representation theory.
