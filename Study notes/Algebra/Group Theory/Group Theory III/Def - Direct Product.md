---
type: definition
subject: group-theory
prereqs:
  - "Def - Group"
  - "Def - Subgroup"
  - "Def - Normal Subgroup"
  - "Def - Order of a Group and of an Element"
  - "Def - Abelian Group"
  - "Def - Isomorphism"
tags: [algebra, group-theory]
---

# Notation

Given two groups $G$ and $H$, their **direct product** is written $G \times H$. Its elements are ordered pairs $(g, h)$ with $g \in G$ and $h \in H$, and its underlying set is the Cartesian product of the underlying sets of $G$ and $H$. The identity of $G \times H$ is the pair $(e_G, e_H)$ of the two identities, written simply $(e, e)$ when no confusion arises. The order $|G \times H|$ is the product $|G|\,|H|$. The same construction extends to any finite list $G_1 \times G_2 \times \cdots \times G_n$ of groups, whose elements are tuples $(g_1, \dots, g_n)$. When $G$ and $H$ are both written additively the product is often called the **direct sum** and written $G \oplus H$, but for finitely many factors the two notions coincide. The cyclic group of order $n$ is $C_n$, so $C_m \times C_n$ is a recurring example. The full notation registry lives on the parent page [[Group Theory III — §1.5–1.7]].

---

# Axiom Motivation

The thing we are trying to build is a way to **glue two groups into one larger group while keeping both of the originals intact and independent inside it**. This is the most basic act of construction in group theory: we have a stock of small groups, and we want a machine that assembles them into bigger ones, so that the structure of the big group is transparently determined by the structure of the pieces. The direct product is that machine in its simplest, purest form — the form where the two pieces do not interact at all.

Begin with the desiderata. We want a group, call it $P$, that "contains a copy of $G$ and a copy of $H$" in a strong sense. What should "strong" mean? Three things. First, $G$ and $H$ should both sit inside $P$ as genuine [[Def - Subgroup|subgroups]] — copies of the originals, not distorted images. Second, the two copies should be **independent**: knowing the $G$-part of an element should tell you nothing about its $H$-part, so every combination of a $G$-element with an $H$-element is a distinct element of $P$, and $P$ has exactly $|G|\,|H|$ elements. Third — and this is the subtle one — the two copies should not interfere when you multiply: an element of the $G$-copy and an element of the $H$-copy should **commute** with each other, and the $G$-copy and the $H$-copy should overlap only in the identity. If these hold, $P$ deserves to be called "$G$ and $H$ side by side", and the whole structure of $P$ is recoverable from $G$ and $H$ alone.

Now ask what operation on pairs $(g, h)$ delivers exactly this. The set must be the Cartesian product $G \times H$, because we want every $g$-with-every-$h$, that is the independence demand, and a set of pairs is the only thing with $|G|\,|H|$ elements parametrised by a $G$-coordinate and an $H$-coordinate. For the operation, the only candidate that respects the independence is **componentwise** multiplication: $(g_1, h_1)(g_2, h_2) = (g_1 g_2,\, h_1 h_2)$. One could ask why not something that mixes the coordinates — why not $(g_1, h_1)(g_2, h_2) = (g_1 g_2,\, h_1 h_2 \cdot \phi(g_1))$ for some twisting map $\phi$? The honest answer is that such a twist is exactly the *semidirect* product, a strictly more general and genuinely useful construction; but it is no longer "$G$ and $H$ independent", because now the $H$-coordinate of a product depends on the $G$-coordinates. The direct product is the choice with **no twist**. Componentwise multiplication is forced the moment you insist the two factors be independent.

Check that the componentwise operation gives a group, and notice that each axiom is inherited coordinate by coordinate. Associativity holds because $G$ and $H$ are each associative and the operation acts in each slot separately. The identity is $(e_G, e_H)$ because $e_G$ neutralises the first slot and $e_H$ the second. The inverse of $(g, h)$ is $(g^{-1}, h^{-1})$, again slot by slot. Nothing new has to be verified — this is the sense in which the direct product is the *free* glue, demanding no compatibility between $G$ and $H$ whatsoever. Contrast this with what would break if we weakened the construction. If we tried to take a *quotient* of $G \times H$ to make it smaller, or to identify some elements of the $G$-copy with elements of the $H$-copy, the two factors would no longer be independent and the order would no longer be $|G|\,|H|$. If we strengthened the construction by demanding $G$ and $H$ be equal, we would get only the "diagonal" copies and lose the ability to combine *different* groups. The direct product is calibrated precisely at "two arbitrary groups, combined with no interaction".

It is worth seeing the desiderata realised concretely inside $P = G \times H$, because this is what the definition is *for*. The copy of $G$ is the subset $\bar G = \{(g, e_H) : g \in G\}$, the elements whose $H$-coordinate is trivial; the copy of $H$ is $\bar H = \{(e_G, h) : h \in H\}$. These are subgroups, they are isomorphic to $G$ and $H$ respectively, and they overlap only in $(e, e)$ because a pair lies in both exactly when both coordinates are trivial. They commute with each other, since $(g, e)(e, h) = (g, h) = (e, h)(g, e)$ — the componentwise operation never lets the slots cross. And crucially **both are [[Def - Normal Subgroup|normal]] in $P$**: conjugating $(g, e_H)$ by any $(x, y)$ gives $(xgx^{-1}, e_H)$, which is back in $\bar G$. These four properties — two normal subgroups, trivial intersection, mutual commuting, and together they generate everything — are not accidental features. They are the *signature* of a direct product, and they are exactly what the recognition criterion below detects.

The reason to get this definition exactly right, rather than a nearby variant, is the [[Thm - Classification of Finite Abelian Groups|classification of finite abelian groups]]. That theorem says every finite [[Def - Abelian Group|abelian]] group is a direct product of cyclic groups. If "direct product" meant the twisted semidirect version, the classification would be false — semidirect products of abelian groups need not be abelian, so they would overshoot the target. If it meant something weaker that allowed the factors to overlap, the uniqueness half of the classification would fail. The untwisted, trivially-intersecting direct product is the precise notion for which "every finite abelian group is a product of cyclic pieces, uniquely" comes out true.

---

# The Definition

Let $(G, \cdot_G, e_G)$ and $(H, \cdot_H, e_H)$ be groups. The **(external) direct product** of $G$ and $H$ is the group

$$G \times H = \bigl(\, G \times H,\ \cdot,\ (e_G, e_H) \,\bigr)$$

whose underlying set is the Cartesian product $\{(g, h) : g \in G,\ h \in H\}$, and whose operation is **componentwise**:

$$(g_1, h_1) \cdot (g_2, h_2) = (g_1 \cdot_G g_2,\ \ h_1 \cdot_H h_2).$$

This is a group: associativity, the identity $(e_G, e_H)$, and the inverse $(g, h)^{-1} = (g^{-1}, h^{-1})$ all hold coordinatewise, inherited from $G$ and $H$. Its order is

$$|G \times H| = |G| \cdot |H|.$$

Inside $G \times H$ sit two distinguished subgroups, the **canonical copies** of the factors,

$$\bar G = \{(g, e_H) : g \in G\}, \qquad \bar H = \{(e_G, h) : h \in H\},$$

with $\bar G \cong G$ and $\bar H \cong H$ via $g \mapsto (g, e_H)$ and $h \mapsto (e_G, h)$. These satisfy three properties simultaneously:

1. **Normality.** $\bar G \trianglelefteq G \times H$ and $\bar H \trianglelefteq G \times H$.
2. **Trivial intersection.** $\bar G \cap \bar H = \{(e_G, e_H)\}$.
3. **They generate, and commute.** Every element factors uniquely as $(g, h) = (g, e_H)(e_G, h)$ with one factor from each copy, and every element of $\bar G$ commutes with every element of $\bar H$.

The construction extends to any finite list: $G_1 \times \cdots \times G_n$ has as elements the tuples $(g_1, \dots, g_n)$ with componentwise multiplication, identity $(e_1, \dots, e_n)$, and order $\prod_i |G_i|$.

**Internal direct product — the recognition criterion.** The definition above *builds* a product from two separately-given groups; the following criterion *recognizes* when a single group $G$ already is one. Let $G$ be a group with subgroups $H$ and $K$. Then $G$ is the **internal direct product** of $H$ and $K$, and the multiplication map

$$H \times K \longrightarrow G, \qquad (h, k) \longmapsto hk$$

is an [[Def - Isomorphism|isomorphism]] $H \times K \cong G$, precisely when all three of the following hold:

1. $H \trianglelefteq G$ and $K \trianglelefteq G$ — both are [[Def - Normal Subgroup|normal subgroups]];
2. $H \cap K = \{e\}$ — they intersect trivially;
3. $G = HK = \{hk : h \in H,\ k \in K\}$ — together they generate $G$.

When these hold one writes $G = H \times K$, treating the internal and external products as the same object. The criterion is the practical face of the definition: it is how a direct-product structure is *detected* in the wild, for instance when one finds normal subgroups of coprime order whose sizes multiply to $|G|$.

---

# Relate to Other Fields / Compression

The direct product is **the product in the category of groups**, in the exact technical sense of category theory. A *product* of two objects $X$ and $Y$ in a category is an object $P$ together with two projection arrows $\pi_X : P \to X$, $\pi_Y : P \to Y$, with the universal property that any object $T$ with arrows $f : T \to X$, $g : T \to Y$ factors through $P$ via a unique arrow $T \to P$. For groups, $G \times H$ with the projections $\pi_G(g, h) = g$ and $\pi_H(g, h) = h$ satisfies exactly this: a pair of [[Def - Homomorphism|homomorphisms]] from any group $T$ into $G$ and into $H$ assembles into a single homomorphism $T \to G \times H$, $t \mapsto (f(t), g(t))$, and this is the only one compatible with the projections. So "direct product" is not an ad hoc construction but the instance, for groups, of a notion that also produces the product of sets (Cartesian product), of topological spaces (product topology), and of vector spaces (direct sum). The componentwise operation is forced by the universal property; it is not a free choice.

From the linear-algebra side, the direct product of abelian groups **is the direct sum of modules**, specialised to $\mathbb{Z}$-modules. A finite abelian group is exactly a finite module over the ring $\mathbb{Z}$, and the external direct product $A \times B$ of two such is their direct sum $A \oplus B$ as $\mathbb{Z}$-modules. This is why the [[Thm - Classification of Finite Abelian Groups|classification of finite abelian groups]] is literally the structure theorem for finitely generated modules over a principal ideal domain, read at $R = \mathbb{Z}$: "direct product of cyclic groups" becomes "direct sum of cyclic modules $\mathbb{Z}/(d_i)$". The decomposition $V = \bigoplus V_i$ of a vector space into a basis' worth of lines is the same construction over the PID $R = k$.

One sharp way to compress the definition: the direct product is **the semidirect product with the trivial twist**. The semidirect product $H \rtimes_\phi K$ glues $H$ and $K$ using an action $\phi : K \to \operatorname{Aut}(H)$ that lets $K$ permute the elements of $H$; the operation is $(h_1, k_1)(h_2, k_2) = (h_1 \cdot \phi_{k_1}(h_2),\, k_1 k_2)$. When $\phi$ is trivial — every $\phi_k$ is the identity automorphism — the twist disappears and the operation becomes componentwise. So the direct product is the degenerate, interaction-free end of a one-parameter family of gluings, and the recognition criterion's clause "$H$ *and* $K$ both normal" is exactly the condition that pins down the trivial twist: in $H \rtimes K$ only $H$ is forced normal, and demanding $K$ normal as well kills the action.

---

# Examples / Corollaries

**Is an instance: the Klein four-group $V = C_2 \times C_2$.** The direct product of two copies of the cyclic group of order $2$ has four elements $(0,0), (1,0), (0,1), (1,1)$ with componentwise addition modulo $2$. Every non-identity element has order $2$, and it is the smallest non-cyclic group. It is abelian because both factors are, and it is *not* isomorphic to $C_4$ — a contrast that probes the construction, since $|C_2 \times C_2| = |C_4| = 4$ but $C_4$ has an element of order $4$ while $C_2 \times C_2$ does not. The reason is the [[Thm - Chinese Remainder Theorem for Cyclic Groups|coprimality condition]]: $C_m \times C_n \cong C_{mn}$ requires $\gcd(m, n) = 1$, and $\gcd(2, 2) = 2 \neq 1$.

**Is an instance: $C_2 \times C_3 \cong C_6$.** The direct product of $C_2$ and $C_3$ is cyclic of order $6$, because $\gcd(2, 3) = 1$ and the pair (generator of $C_2$, generator of $C_3$) has order $\operatorname{lcm}(2,3) = 6$. This is the [[Thm - Chinese Remainder Theorem for Cyclic Groups|Chinese remainder theorem]] in its smallest non-trivial case, and it shows that whether a direct product of cyclic groups is again cyclic depends entirely on the arithmetic of the factor orders.

**Is an instance: $\mathbb{R}^n = \mathbb{R} \times \cdots \times \mathbb{R}$.** The additive group of $n$-dimensional real space is the $n$-fold direct product of the additive group $(\mathbb{R}, +)$ with itself. Vector addition is componentwise, which is exactly the direct-product operation. This shows the construction is not confined to finite groups.

**Is an instance (internal): a cyclic group of order $6$ is the internal direct product of its subgroups of order $2$ and $3$.** In $C_6 = \{0, 1, 2, 3, 4, 5\}$ under addition mod $6$, the subgroup $H = \{0, 3\}$ has order $2$ and $K = \{0, 2, 4\}$ has order $3$. Both are normal (every subgroup of an abelian group is), $H \cap K = \{0\}$, and $H + K = C_6$. So the internal-product criterion fires and $C_6 = H \times K$, recovering $C_6 \cong C_2 \times C_3$ from the inside. This is the criterion doing its job: detecting a product structure already present in a group given to us whole.

**Is NOT an instance: the symmetric group $S_3$ is not a direct product of $C_3$ and $C_2$.** The group $S_3$ has order $6$, it contains a normal subgroup $A_3 \cong C_3$ (the rotations) and a subgroup $\langle \tau \rangle \cong C_2$ (a single reflection) with $A_3 \cap \langle \tau \rangle = \{e\}$ and $A_3 \cdot \langle \tau \rangle = S_3$ — so two of the three criterion clauses hold. But $\langle \tau \rangle$ is **not normal**, and indeed it must not be: if both factors were normal the product would be a direct product, hence isomorphic to $C_3 \times C_2 \cong C_6$, which is abelian, whereas $S_3$ is not. Concretely the two factors do not commute: a rotation followed by a reflection differs from the reflection followed by the rotation. $S_3$ is a *semidirect* product $C_3 \rtimes C_2$ with a non-trivial twist. This non-example isolates clause 1 of the recognition criterion: dropping the normality of *one* factor takes you out of direct products entirely.

**Is NOT an instance: $C_4$ is not the internal direct product of any two proper subgroups.** The only proper non-trivial subgroup of $C_4$ is $\{0, 2\} \cong C_2$. To write $C_4 = H \times K$ internally one would need two subgroups with trivial intersection whose orders multiply to $4$, forcing $|H| = |K| = 2$ — but there is only *one* subgroup of order $2$, so $H = K$ and $H \cap K = H \neq \{0\}$. The trivial-intersection clause fails. $C_4$ is **indecomposable**: it is a single cyclic prime-power piece, an atom of the [[Thm - Classification of Finite Abelian Groups|classification]], and cannot be split further. This probes clause 2.

**Corollary (order of a tuple).** In $G \times H$, the order of an element $(g, h)$ is $\operatorname{lcm}(\operatorname{ord}(g), \operatorname{ord}(h))$. Indeed $(g, h)^k = (g^k, h^k)$ equals $(e, e)$ exactly when $g^k = e$ and $h^k = e$, i.e. when $k$ is a common multiple of the two orders; the least such $k$ is the least common multiple. *Calibration check:* this single fact is the engine of the [[Thm - Chinese Remainder Theorem for Cyclic Groups|Chinese remainder theorem]] — if you can reproduce it you have understood that the operation is componentwise.

**Corollary ($G \times H$ is abelian if and only if both factors are).** Since $(g_1, h_1)(g_2, h_2) = (g_1 g_2, h_1 h_2)$ and $(g_2, h_2)(g_1, h_1) = (g_2 g_1, h_2 h_1)$, the two products are equal for all elements exactly when $g_1 g_2 = g_2 g_1$ for all $g$ in $G$ and $h_1 h_2 = h_2 h_1$ for all $h$ in $H$. Commutativity, like every other axiom-level property, is checked coordinatewise. *Calibration check:* this is why the classification can speak of products of cyclic groups and stay within the [[Def - Abelian Group|abelian]] world.

**Corollary (the projections are homomorphisms with kernels the opposite factor).** The map $\pi_G : G \times H \to G$, $(g, h) \mapsto g$, is a surjective [[Def - Homomorphism|homomorphism]] with kernel $\bar H = \{(e_G, h)\}$. By the [[Thm - First Isomorphism Theorem|first isomorphism theorem]], $(G \times H)/\bar H \cong G$ — quotienting a direct product by one factor returns the other. This is the structural shadow of "the factors are independent".

---

# Unlocked by This

> [!tip] Structure Theorem for Modules over a PID *(from Rings and Modules)*
> Once the direct product is in hand, the [[Thm - Classification of Finite Abelian Groups|classification of finite abelian groups]] becomes the statement "every finite abelian group is a direct product of cyclic pieces". Read with $\mathbb{Z}$ replaced by a general principal ideal domain $R$, and "direct product" replaced by "direct sum of modules", this is the structure theorem $M \cong \bigoplus R/(d_i)$ for finitely generated $R$-modules — the master theorem behind rational and Jordan canonical forms.

> [!tip] Semidirect Product *(from Group Theory IV — Group Extensions)*
> The direct product is the trivial-twist end of a family. Allowing one factor to act on the other by automorphisms gives the **semidirect product** $H \rtimes K$, the construction needed to build and classify the non-abelian groups — for instance $D_{2n} \cong C_n \rtimes C_2$ and $S_3 \cong C_3 \rtimes C_2$ — that are *not* direct products.
