---
type: definition
subject: group-theory
prereqs:
  - "Def - Normal Subgroup"
  - "Def - Coset"
  - "Def - Subgroup"
  - "Def - Order of a Group and of an Element"
tags: [algebra, group-theory]
---

# Notation

$G$ is a group with identity $e$, and $N \trianglelefteq G$ is a [[Def - Normal Subgroup|normal subgroup]]. The set of [[Def - Coset|left cosets]] is written $G/N = \{gN : g \in G\}$, read "$G$ mod $N$"; this set, equipped with the operation below, is the **quotient group**. The number of cosets is the **index** $|G : N|$. The map $g \mapsto gN$ sending each element to its coset is the **quotient map** (or canonical projection) $\pi : G \to G/N$. The full symbol registry is on [[Group Theory I — §1.1–1.2]].

---

# Axiom Motivation

Group theory's central project is to take a complicated group apart into simpler pieces. The arithmetic analogy is exact and worth holding onto: to understand an integer you factor it into primes; to understand a group you want to factor it into smaller groups. The quotient is the "divide" operation. The motivating desideratum is therefore: *given $G$ and a subgroup $N$, build a new group, smaller than $G$, in which the distinctions recorded by $N$ have been erased.*

What should "erasing $N$" mean? It should mean declaring two elements $g$ and $g'$ to be *the same* whenever they differ by an element of $N$ — whenever $g^{-1}g' \in N$. This is an equivalence relation, and its equivalence classes are exactly the [[Def - Coset|cosets]] $gN$. So the underlying *set* of the new group is forced: it must be $G/N$, the set of cosets. There is no choice here; cosets are simply the elements of $G$ after we agree to ignore $N$.

The operation is also forced, up to checking it works. We want the quotient map $g \mapsto gN$ to be a [[Def - Homomorphism|homomorphism]] — that is the whole point, that the new group inherits the multiplication of the old. A homomorphism must send a product to the product of images, so we are *compelled* to define
$$(g_1 N)(g_2 N) := g_1 g_2 N.$$
Nothing else is consistent with the quotient map respecting multiplication. The only remaining question is whether this formula is legitimate — whether the coset on the right depends only on the two cosets on the left, not on the representatives $g_1, g_2$ we used to name them.

And here is the crux, which is also the entire reason [[Def - Normal Subgroup|normality]] exists. If we re-name the first factor as $g_1' = g_1 n$ for $n \in N$, the formula must still give the same answer; the requirement, worked out in the [[Def - Normal Subgroup#Axiom Motivation|normal subgroup motivation]], is precisely $g^{-1} n g \in N$ for all $n \in N, g \in G$ — the definition of normality. **Quotient groups exist exactly for normal subgroups, and the definition of "normal" was reverse-engineered from this very construction.** If $N$ were merely a subgroup and not normal — say $N = \langle (1\,2)\rangle \leq S_3$ — the formula would be ill-defined: $\big((1\,3)N\big)\big((1\,2)N\big)$ would depend on whether the first coset is named via $(1\,3)$ or via $(1\,3)(1\,2) = (1\,3\,2)$, even though those name the *same* coset. The set $G/N$ would still exist; the *group* would not.

Why not weaken the requirement and accept whatever partial structure non-normal $N$ provides? Because the partial structure is not a group, and groups are the objects we can prove theorems about — associativity, the isomorphism theorems, Lagrange — all of which we want to apply to the quotient. Why not strengthen, demanding say that $N$ be central? Then quotients would still be groups, but we would be able to form far fewer of them, losing essential examples like $S_n/A_n$. Normality is exactly the hypothesis that is both necessary (weaker fails) and sufficient (it is all you need), so the quotient construction takes a normal subgroup as input — no more, no less.

---

# The Definition

Let $N \trianglelefteq G$ be a [[Def - Normal Subgroup|normal subgroup]]. The **quotient group** $G/N$ is the set of [[Def - Coset|left cosets]] $\{gN : g \in G\}$ equipped with the multiplication
$$(g_1 N)(g_2 N) := g_1 g_2 N.$$
With this operation $G/N$ is a group:

- the operation is **well-defined** precisely because $N$ is normal;
- it is **associative**, inherited directly from associativity in $G$: $\big((g_1 N)(g_2 N)\big)(g_3 N) = g_1 g_2 g_3 N = (g_1 N)\big((g_2 N)(g_3 N)\big)$;
- the **identity element** is the coset $eN = N$, since $(eN)(gN) = gN = (gN)(eN)$;
- the **inverse** of $gN$ is $g^{-1}N$, since $(gN)(g^{-1}N) = gg^{-1}N = eN = N$.

The **order** of the quotient is the index of $N$:
$$|G/N| = |G : N|,$$
the number of cosets, simply because the elements of $G/N$ *are* the cosets. When $G$ is finite, [[Thm - Lagrange's Theorem|Lagrange's theorem]] gives $|G/N| = |G|/|N|$.

The quotient map $\pi : G \to G/N$, $\pi(g) = gN$, is a surjective [[Def - Homomorphism|homomorphism]], and its [[Def - Kernel and Image|kernel]] is exactly $N$. So every normal subgroup is the kernel of a homomorphism — the converse of the fact that every kernel is normal.

---

# Categorical Definition

The quotient group is characterised — pinned down uniquely, up to isomorphism — by a **universal property**, and unpacking this is worth the effort because the universal property is what the [[Thm - First Isomorphism Theorem|first isomorphism theorem]] really is.

First, what is a universal property? It is a description of an object purely by the maps into or out of it, of the form "$X$ is the *most efficient* object doing such-and-such" — most efficient meaning every other object doing the same thing factors uniquely through $X$. "Factors through" means: any such map can be re-expressed as (the map for $X$) followed by exactly one further map.

For the quotient, the relevant property of a homomorphism is *killing $N$*: say a homomorphism $f : G \to K$ **kills $N$** if $f(n) = e_K$ for every $n \in N$ — equivalently $N \subseteq \ker f$. The quotient map $\pi : G \to G/N$ kills $N$, since $\pi(n) = nN = N$, the identity of $G/N$.

The universal property: **$\pi : G \to G/N$ is the initial (universal) homomorphism out of $G$ that kills $N$.** Precisely — for every group $K$ and every homomorphism $f : G \to K$ that kills $N$, there is a *unique* homomorphism $\bar{f} : G/N \to K$ with $f = \bar{f} \circ \pi$:
$$\begin{array}{ccc} G & \xrightarrow{\ f\ } & K \\ {\scriptstyle\pi}\big\downarrow & \nearrow_{\scriptstyle\bar f} & \\ G/N & & \end{array}$$
The map $\bar f$ is forced: it must send $gN \mapsto f(g)$, and this is well-defined exactly because $f$ kills $N$ (if $gN = g'N$ then $g^{-1}g' \in N$ so $f(g^{-1}g') = e$, hence $f(g) = f(g')$). The content of the property is that $G/N$ is the *cleanest* group through which all $N$-killing maps factor: it kills $N$ and absolutely nothing more. This determines $G/N$ uniquely up to a unique isomorphism — any two groups with this property are canonically isomorphic — so the universal property can be *taken* as the definition, with the coset construction merely exhibiting that such an object exists.

This is also exactly the [[Thm - First Isomorphism Theorem|first isomorphism theorem]] in disguise. Apply the property to $f = \varphi$ itself with $N = \ker\varphi$: the induced $\bar\varphi : G/\ker\varphi \to K$ is injective (it kills nothing beyond $\ker\varphi$) and has image $\operatorname{im}\varphi$, so $G/\ker\varphi \cong \operatorname{im}\varphi$.

In the language of category theory there is an even tighter description: $G/N$ is a **coequaliser**. A coequaliser of two parallel maps $a, b : A \to G$ is the universal object $q : G \to Q$ with $q \circ a = q \circ b$ — the most efficient way to *force two maps to agree*. Take $A = N$, let $a : N \hookrightarrow G$ be the inclusion, and let $b : N \to G$ be the constant map at $e$. A homomorphism $q$ satisfies $q \circ a = q \circ b$ exactly when $q(n) = e$ for all $n \in N$, i.e. exactly when $q$ kills $N$. So the coequaliser of (inclusion, constant) *is* the quotient map $G \to G/N$. The quotient is "the universal way to make the subgroup $N$ collapse to the identity".

---

# Relate to Other Fields / Compression

The quotient group is one instance of the universal *quotient by a congruence*, which appears in every algebraic theory. The quotient ring $R/I$ by an [[Def - Ideal|ideal]], the quotient module $M/M'$ by a submodule, the quotient vector space $V/W$ by a subspace, and the quotient topological space $X/\!\sim$ by an equivalence relation are all the same construction: take the structure, impose an equivalence relation compatible with the operations, and the equivalence classes inherit the structure. In each case the quotient is characterised by the identical universal property — initial among structure-preserving maps that collapse the chosen substructure — and in each case there is a first isomorphism theorem of the same shape. The group case is the prototype; the only feature special to groups is that the compatible equivalence relations correspond to *normal* subgroups rather than to arbitrary subgroups, a subtlety that disappears once the ambient operation is commutative (rings, modules, spaces).

A sharper compression: forming $G/N$ is *deliberate, controlled forgetting*. It throws away the information distinguishing elements that differ by $N$, but the forgetting is controlled — the [[Thm - Correspondence Theorem|correspondence theorem]] guarantees every subgroup of $G$ containing $N$ remains visible inside $G/N$, with its index and normality intact. This is the same move as passing to a quotient ring or a quotient space: forget the structure you do not need, but forget it so that the surviving structure stays faithfully readable. It is what makes "quotient to simplify" a safe step and not a reckless one.

---

# Examples / Corollaries

**Is an instance — $\mathbb{Z}/n\mathbb{Z}$, modular arithmetic.** Take $G = (\mathbb{Z}, +)$ and $N = n\mathbb{Z}$, the multiples of $n$. Since $\mathbb{Z}$ is [[Def - Abelian Group|abelian]], $n\mathbb{Z}$ is automatically normal, and the quotient $\mathbb{Z}/n\mathbb{Z}$ is the group of integers modulo $n$. Its elements are the $n$ cosets $0 + n\mathbb{Z}, 1 + n\mathbb{Z}, \dots, (n-1) + n\mathbb{Z}$, the coset operation is addition mod $n$, and $|\mathbb{Z}/n\mathbb{Z}| = |\mathbb{Z} : n\mathbb{Z}| = n$. "Reduction mod $n$" is the quotient map. This is the most familiar quotient in mathematics, and it shows the construction is not exotic — it is arithmetic.

**Is an instance — $S_n / A_n \cong C_2$.** The alternating group $A_n \trianglelefteq S_n$ has index $2$, so the quotient $S_n/A_n$ has order $2$: its two elements are "the even permutations" $A_n$ and "the odd permutations". The quotient remembers only the parity of a permutation and forgets everything else. It is the cyclic group $C_2$, and the quotient map is the sign homomorphism $\operatorname{sgn}$.

**Is an instance — $G/\{e\}$ and $G/G$, the degenerate quotients.** Quotienting by the trivial subgroup, $G/\{e\}$, collapses nothing: each coset $g\{e\} = \{g\}$ is a single element, and $G/\{e\} \cong G$. Quotienting by all of $G$, the quotient $G/G$ has a single coset and is the trivial group. These bracket the construction: $G/N$ interpolates between an exact copy of $G$ (when $N$ is small) and the trivial group (when $N$ is all of $G$).

**Is NOT an instance — "$S_3$ modulo $\langle(1\,2)\rangle$".** There is no quotient group here, because $\langle(1\,2)\rangle$ is not [[Def - Normal Subgroup|normal]] in $S_3$. The set of three cosets exists, but no group structure does; the proposed coset multiplication is ill-defined. This is the boundary of the construction: a quotient *group* requires a *normal* subgroup, full stop.

**Is NOT an instance — the quotient is not a subgroup of $G$.** It is a common slip to picture $G/N$ as sitting inside $G$. It does not: its *elements are cosets*, which are subsets of $G$, not elements of $G$. For instance $\mathbb{Z}/3\mathbb{Z}$ has $3$ elements while $\mathbb{Z}$ is infinite; the quotient is a genuinely new, smaller group, not a piece of the old one.

**Corollary — quotient of an abelian group is abelian.** If $G$ is [[Def - Abelian Group|abelian]] then $(g_1 N)(g_2 N) = g_1 g_2 N = g_2 g_1 N = (g_2 N)(g_1 N)$, so $G/N$ is abelian. More generally any property defined by an equation in the group operation (abelian, exponent dividing $m$, etc.) passes to quotients, because the quotient map is a surjective homomorphism.

**Corollary — $G/N$ remembers sizes but not the gluing.** From $|G/N| = |G:N|$ and $|N|$ one recovers $|G|$, so the quotient remembers the *orders* of the pieces. It does *not* remember how $G$ was assembled: $C_4$ and $C_2 \times C_2$ both have a normal $C_2$ with quotient $C_2$, yet are not isomorphic. Reconstructing $G$ from $N$ and $G/N$ is the *extension problem*, and it genuinely has many answers — in particular $G \not\cong N \times (G/N)$ in general.

**Calibration check.** Confirm that the quotient map $\pi : G \to G/N$ is a surjective homomorphism with $\ker\pi = N$ exactly. Confirm that $|G/N| = 1$ iff $N = G$, and $|G/N| = |G|$ iff $N = \{e\}$. If you can also explain why $\bar f(gN) := f(g)$ in the universal property is well-defined precisely when $f$ kills $N$, you have understood both the definition and its categorical content.

---

# Unlocked by This

> [!tip] First Isomorphism Theorem *(from this topic)*
> The [[Thm - First Isomorphism Theorem|first isomorphism theorem]] — $G/\ker\varphi \cong \operatorname{im}\varphi$ — is the quotient's universal property applied to a general [[Def - Homomorphism|homomorphism]]. It is the master tool for *identifying* an unknown quotient.

> [!tip] Composition Series *(from Group Theory III)*
> Repeated quotienting by maximal normal subgroups produces a [[Thm - Composition Series|composition series]] with [[Def - Simple Group|simple]] factors — the group-theoretic prime factorisation. The quotient is the operation that runs the factorisation.

> [!tip] Quotient Ring, Quotient Module, Quotient Space *(from Ring Theory, Module Theory, Topology)*
> Every "modulo" construction downstream — $R/I$, $M/M'$, $V/W$, $X/\!\sim$ — is this same universal quotient in a different category. Master it once here.
