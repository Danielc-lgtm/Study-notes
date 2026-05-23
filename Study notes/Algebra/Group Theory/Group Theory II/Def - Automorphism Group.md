---
type: definition
subject: group-theory
prereqs:
  - "Def - Group"
  - "Def - Subgroup"
  - "Def - Homomorphism"
  - "Def - Isomorphism"
  - "Def - Kernel and Image"
  - "Def - Symmetric Group"
  - "Def - Conjugacy Class"
  - "Def - Centraliser and Centre"
  - "Def - Normal Subgroup"
tags: [algebra, group-theory]
---

# Notation

Throughout, $G$ is a group with identity $e$. An **automorphism** of $G$ is an [[Def - Isomorphism|isomorphism]] $G \to G$. The group of all automorphisms is $\operatorname{Aut}(G)$; the subgroup of **inner** automorphisms is $\operatorname{Inn}(G)$. For $g \in G$ we write $\gamma_g$ (or $c_g$) for the inner automorphism $x \mapsto gxg^{-1}$. We write $H \leq G$ for "$H$ is a [[Def - Subgroup|subgroup]]", $H \trianglelefteq G$ for "$H$ is [[Def - Normal Subgroup|normal]]", $Z(G)$ for the [[Def - Centraliser and Centre|centre]], and $\operatorname{Sym}(G)$ for the [[Def - Symmetric Group|symmetric group]] on the underlying set of $G$. The full symbol registry for this topic is on [[Group Theory II — §1.3–1.4]].

---

# Axiom Motivation

Every other object in this topic is built from a group acting on *something else* — a set, its [[Def - Coset|cosets]], its own elements by conjugation. The automorphism group comes from turning the question inward: instead of asking how $G$ acts on the world, ask **what symmetries $G$ has as a structured object in its own right.**

Here is the discovery path. We have the notion of an [[Def - Isomorphism|isomorphism]] $G \to G'$ — a bijection that preserves multiplication, the statement that two [[Def - Group|groups]] are "the same group, differently labelled". The special case $G' = G$ is an isomorphism of $G$ *with itself*: a relabelling of $G$ that the group structure cannot detect. Call it an automorphism. The first desideratum is simply to *collect* these. Why should the collection be interesting? Because an automorphism is a *symmetry of the group*, in exactly the sense that a symmetry of a triangle is a relabelling of the triangle preserving its shape. A group with many automorphisms is highly symmetric as an algebraic object; a group with few is rigid. We want a single object that records this internal symmetry, and a set is not enough — we want it to be a *group*, so that we can speak of composing symmetries and undoing them.

So the second desideratum: the collection of automorphisms must itself be a group. Check what is needed. Automorphisms are certain bijections $G \to G$, so they live inside the [[Def - Symmetric Group|symmetric group]] $\operatorname{Sym}(G)$ of *all* bijections of the underlying set. To know $\operatorname{Aut}(G)$ is a group it suffices to know it is a [[Def - Subgroup|subgroup]] of $\operatorname{Sym}(G)$ — and this is forced, not assumed. The composite of two structure-preserving bijections is structure-preserving; the identity map preserves structure; and the inverse of an isomorphism is an isomorphism (the inverse of a multiplication-preserving bijection automatically preserves multiplication). So $\operatorname{Aut}(G)$ is closed under composition and inverses and contains the identity: it is a [[Def - Subgroup|subgroup]] of $\operatorname{Sym}(G)$, and that is *why* it is a group. Defining $\operatorname{Aut}(G)$ as "the [[Def - Isomorphism|isomorphisms]] $G \to G$ under composition" is forced by wanting the symmetries of a group to themselves form a group.

What breaks if we *weaken* the definition — allow all bijections, the whole of $\operatorname{Sym}(G)$? Then we have thrown away the group structure of $G$ entirely; $\operatorname{Sym}(G)$ is the automorphism group of $G$ *as a bare set*, and it knows nothing about multiplication. The whole point is the constraint "preserves the operation": that constraint is what makes $\operatorname{Aut}(G)$ a meaningful invariant of $G$ rather than a function only of its cardinality. What breaks if we *strengthen* it — demand the bijection fix some chosen [[Def - Subgroup|subgroup]], or fix every element of the centre, or be inner? We get a *subgroup* of $\operatorname{Aut}(G)$, sometimes an important one, but not the full symmetry group. The unrestricted "all [[Def - Isomorphism|isomorphisms]] $G \to G$" is the right notion because it is the complete symmetry group; any constraint gives a sub-symmetry.

Now the second, subtler half of the page: the **inner** automorphisms, and why they deserve a name. We have already met, on the [[Def - Conjugacy Class|conjugacy class]] page, that for each $g$ the map $\gamma_g : x \mapsto gxg^{-1}$ is an isomorphism of $G$ with itself — conjugation preserves multiplication, $\gamma_g(xy) = (gxg^{-1})(gyg^{-1}) = \gamma_g(x)\gamma_g(y)$. So *every group supplies automorphisms of itself, internally, one for each element*. These are the inner automorphisms. The desideratum that names them is this: we want to compare the automorphisms a group *generates from within* against the automorphisms it has *in total*, because the gap between the two is real structural information. A group where every automorphism is inner ($\operatorname{Aut}(G) = \operatorname{Inn}(G)$, called *complete* when also $Z(G)$ is trivial) is one whose symmetries are all "visible from inside"; a group with *outer* automorphisms has symmetries not realised by any conjugation.

Two facts must hold for inner automorphisms to be the right sub-object, and we should see why each is forced. *First, $\operatorname{Inn}(G)$ must be a subgroup of $\operatorname{Aut}(G)$.* It is, because the assignment $g \mapsto \gamma_g$ is a [[Def - Homomorphism|homomorphism]] $G \to \operatorname{Aut}(G)$: composing conjugations gives $\gamma_g \circ \gamma_h = \gamma_{gh}$, since conjugating by $h$ then by $g$ is conjugating by $gh$. The image of a homomorphism is always a subgroup — so $\operatorname{Inn}(G)$, being the image of $g \mapsto \gamma_g$, is a subgroup of $\operatorname{Aut}(G)$ for free. *Second, $\operatorname{Inn}(G)$ must be **normal** in $\operatorname{Aut}(G)$.* This is the crucial structural fact, and it is what makes the *outer* automorphism group $\operatorname{Out}(G) = \operatorname{Aut}(G)/\operatorname{Inn}(G)$ a well-defined group. It holds because conjugating an inner automorphism by *any* automorphism produces an inner automorphism: for $\varphi \in \operatorname{Aut}(G)$, a direct computation gives $\varphi \circ \gamma_g \circ \varphi^{-1} = \gamma_{\varphi(g)}$. The slogan is "an automorphism carries conjugation-by-$g$ to conjugation-by-$\varphi(g)$" — and *that* is the reason inner automorphisms form not just a subgroup but a normal one. If this failed, "outer automorphism" would have no group structure and the entire classification of automorphism [[Def - Group|groups]] would lose its organising quotient.

Finally, the deepest motivating fact, which jumps ahead to the payoff. The homomorphism $G \to \operatorname{Aut}(G)$, $g \mapsto \gamma_g$, has a kernel: the elements $g$ for which $\gamma_g$ is the *identity* automorphism, i.e. $gxg^{-1} = x$ for all $x$. That is exactly the [[Def - Centraliser and Centre|centre]] $Z(G)$. So the [[Thm - First Isomorphism Theorem|first isomorphism theorem]] gives, with no further work,
$$G/Z(G) \;\cong\; \operatorname{Inn}(G).$$
This single isomorphism is the reason the whole apparatus is set up the way it is. It says the inner automorphisms are not some accident — they are *$G$ itself, with the centre divided out*. The centre is precisely the part of $G$ that conjugation cannot see, and $\operatorname{Inn}(G)$ is the faithful shadow of $G$ inside its own symmetry group. Define $\operatorname{Aut}(G)$ and $\operatorname{Inn}(G)$ as above, and this clean three-term relationship — $Z(G)$ inside $G$ mapping onto $\operatorname{Inn}(G)$ inside $\operatorname{Aut}(G)$ — falls out as a theorem. A different definition of either object would break it.

---

# The Definition

**Definition (Automorphism group).** Let $G$ be a group. An **automorphism** of $G$ is an [[Def - Isomorphism|isomorphism]] $\varphi : G \to G$ — a bijection satisfying $\varphi(xy) = \varphi(x)\varphi(y)$ for all $x, y \in G$. The **automorphism group** of $G$ is
$$\operatorname{Aut}(G) \;=\; \{\, \varphi \in \operatorname{Sym}(G) : \varphi \text{ is a group isomorphism} \,\},$$
the set of all automorphisms, with composition of maps as the group operation and the identity map $\operatorname{id}_G$ as the identity element. It is a [[Def - Subgroup|subgroup]] of the [[Def - Symmetric Group|symmetric group]] $\operatorname{Sym}(G)$.

**Definition (Inner automorphism).** For each $g \in G$, the **inner automorphism** determined by $g$ is the map
$$\gamma_g : G \to G, \qquad \gamma_g(x) = gxg^{-1}.$$
Each $\gamma_g$ is an automorphism of $G$ (it is the [[Def - Conjugacy Class|conjugation]] by $g$). The set of all inner automorphisms is
$$\operatorname{Inn}(G) \;=\; \{\, \gamma_g : g \in G \,\},$$
and it is a [[Def - Normal Subgroup|normal subgroup]] of $\operatorname{Aut}(G)$, written $\operatorname{Inn}(G) \trianglelefteq \operatorname{Aut}(G)$. An automorphism not in $\operatorname{Inn}(G)$ is called an **outer automorphism**, and the quotient $\operatorname{Out}(G) = \operatorname{Aut}(G)/\operatorname{Inn}(G)$ is the **outer automorphism group**.

**The conjugation homomorphism.** The assignment
$$\gamma : G \to \operatorname{Aut}(G), \qquad g \mapsto \gamma_g$$
is a [[Def - Homomorphism|homomorphism]], because $\gamma_g \circ \gamma_h = \gamma_{gh}$. Its image is $\operatorname{Inn}(G)$ and its kernel is the [[Def - Centraliser and Centre|centre]] $Z(G)$, since $\gamma_g = \operatorname{id}_G$ exactly when $g$ commutes with every element of $G$. By the [[Thm - First Isomorphism Theorem|first isomorphism theorem]],
$$G/Z(G) \;\cong\; \operatorname{Inn}(G).$$
The normality $\operatorname{Inn}(G) \trianglelefteq \operatorname{Aut}(G)$ follows from the identity $\varphi \circ \gamma_g \circ \varphi^{-1} = \gamma_{\varphi(g)}$, valid for every $\varphi \in \operatorname{Aut}(G)$.

---

# Categorical Definition

The automorphism group is a special case of a notion that exists in *every* category, and stating it that way explains why $\operatorname{Aut}$ behaves uniformly across algebra.

In any category $\mathcal{C}$, an object $X$ has a set of *endomorphisms* $\operatorname{End}(X) = \operatorname{Hom}_{\mathcal{C}}(X, X)$, the morphisms from $X$ to itself, which form a monoid under composition (composition is associative and the identity morphism $\operatorname{id}_X$ is a two-sided unit). An **automorphism** of $X$ is an *isomorphism* $X \to X$ — an endomorphism $\varphi$ admitting a two-sided inverse $\varphi^{-1}$ with $\varphi \circ \varphi^{-1} = \varphi^{-1}\circ\varphi = \operatorname{id}_X$. The **automorphism group** $\operatorname{Aut}_{\mathcal{C}}(X)$ is the set of automorphisms of $X$: it is precisely the *group of units* of the endomorphism monoid $\operatorname{End}(X)$, and the units of any monoid form a group.

The automorphism group of this page is this construction in the category $\mathbf{Grp}$ of groups and group [[Def - Homomorphism|homomorphisms]]: $\operatorname{Aut}(G) = \operatorname{Aut}_{\mathbf{Grp}}(G)$. The same construction in the category $\mathbf{Set}$ gives the [[Def - Symmetric Group|symmetric group]] $\operatorname{Sym}(X)$ — automorphisms of a bare set are just bijections. In $\mathbf{Vect}$ it gives the general linear group $\mathrm{GL}(V)$. In $\mathbf{Top}$ it gives the self-[[Def - Homeomorphism|homeomorphisms]] of a space. So "automorphism group" is one categorical idea, and $\operatorname{Aut}(G) \leq \operatorname{Sym}(G)$ is the statement that a group-automorphism is in particular a set-automorphism — the forgetful functor $\mathbf{Grp} \to \mathbf{Set}$ induces an inclusion of automorphism groups.

The inner automorphisms have a categorical reading too. Recall a group $G$ is the one-object category $\mathbf{B}G$. A *natural transformation* of the identity functor $\mathbf{B}G \to \mathbf{B}G$ to itself — a *natural automorphism of the identity functor* — is precisely an element of the centre $Z(G)$. And the inner automorphism group $\operatorname{Inn}(G)$ is the image of $G$ under the canonical map into $\operatorname{Aut}(G)$; the quotient $\operatorname{Out}(G)$ measures the automorphisms not coming from this canonical "conjugation" 2-cell. This is the first appearance of the *2-categorical* nature of $\mathbf{Grp}$ — inner automorphisms are the automorphisms that are "naturally isomorphic to the identity".

---

# Relate to Other Fields / Compression

The automorphism group is the group-theoretic instance of **the symmetry group of a mathematical structure** — and since "structure" is everywhere, $\operatorname{Aut}$ is one of the most pervasive constructions in mathematics.

The closest comparison is internal: $\operatorname{Aut}(G)$ is to a *group* exactly what $\operatorname{Sym}(X)$ is to a *set*. The [[Def - Symmetric Group|symmetric group]] $\operatorname{Sym}(X)$ collects all relabellings of a set; $\operatorname{Aut}(G)$ collects all relabellings of a group that respect multiplication. The inclusion $\operatorname{Aut}(G) \leq \operatorname{Sym}(G)$ says the second is the first cut down by the requirement of preserving the operation. This is the same step that takes you from "all permutations of the vertices of a graph" to "the automorphism group of the graph" (permutations preserving the edges), or from all bijections of $\mathbb{R}^n$ to the isometry group (bijections preserving distance).

In **linear algebra** the automorphism group of a vector space $V$ is the general linear group $\mathrm{GL}(V)$ — the invertible linear maps. The analogy is exact: $\operatorname{Aut}(G)$ is to a group as $\mathrm{GL}(V)$ is to a vector space. And $\operatorname{Inn}(G)$ has no non-trivial analogue here, because vector-space addition is commutative — conjugation is trivial in an abelian structure, so an abelian group has $\operatorname{Inn}(G) = \{e\}$ and *all* its automorphisms are outer. This is why automorphism groups of abelian groups (for instance $\operatorname{Aut}(\mathbb{Z}/n) \cong (\mathbb{Z}/n)^\times$, the units mod $n$) are purely "outer" objects.

In **geometry and physics** the automorphism group is the symmetry group of whatever structure is at hand: the isometry group of a Riemannian manifold, the group of symplectomorphisms of a phase space, the gauge group of a principal bundle. A reader with a background in geometric mechanics has met $\operatorname{Aut}$ repeatedly as "the group of structure-preserving transformations", and the distinction between inner and outer automorphisms reappears in gauge theory as the distinction between *gauge transformations* (the inner, locally-realised symmetries) and *global symmetries of the gauge group itself*.

In **field theory** the automorphism group of a field extension $L/K$ that fixes $K$ pointwise is the *Galois group* — the central object of Galois theory — and the entire correspondence between subfields and subgroups is a statement about this automorphism group.

So the compression is: $\operatorname{Aut}(G)$ is "the symmetry group of $G$ regarded as a structured object", the units of the endomorphism monoid; specialise the structure and it becomes $\operatorname{Sym}(X)$, $\mathrm{GL}(V)$, an isometry group, or a Galois group. The inner/outer split is special to non-commutative structure and measures which symmetries are realised by conjugation from within.

---

# Examples / Corollaries

**Is an instance — automorphisms of a cyclic group.** For the cyclic group $\mathbb{Z}/n$, an automorphism is determined by where it sends a generator $1$, and it must send $1$ to another generator, i.e. to a unit mod $n$. Hence $\operatorname{Aut}(\mathbb{Z}/n) \cong (\mathbb{Z}/n)^\times$, the multiplicative group of units modulo $n$, of order $\phi(n)$. For example $\operatorname{Aut}(\mathbb{Z}/8) \cong (\mathbb{Z}/8)^\times \cong \mathbb{Z}/2 \times \mathbb{Z}/2$. Since $\mathbb{Z}/n$ is [[Def - Abelian Group|abelian]] its centre is everything, so $\operatorname{Inn}(\mathbb{Z}/n) \cong (\mathbb{Z}/n)/(\mathbb{Z}/n)$ is trivial — *every* automorphism of a cyclic group is outer.

**Is an instance — inner automorphisms of $S_3$.** The symmetric group $S_3$ has trivial [[Def - Centraliser and Centre|centre]] (no non-identity permutation commutes with all others), so $G/Z(G) = S_3/\{e\} \cong S_3$, giving $\operatorname{Inn}(S_3) \cong S_3$, a group of order $6$. In fact every automorphism of $S_3$ is inner: $\operatorname{Aut}(S_3) = \operatorname{Inn}(S_3) \cong S_3$, so $\operatorname{Out}(S_3)$ is trivial. The symmetries of $S_3$ are all visible from inside as conjugations.

**Is an instance — an outer automorphism of $S_6$.** The symmetric group $S_n$ has $\operatorname{Aut}(S_n) = \operatorname{Inn}(S_n) \cong S_n$ for *every* $n$ except $n = 6$. The group $S_6$ possesses a genuinely **outer** automorphism — one not realised by any conjugation — and $\operatorname{Out}(S_6) \cong \mathbb{Z}/2$. This famous exception (it swaps the two conjugacy classes of order-$6$ elements, or equivalently transpositions with triple transpositions) is the reason $S_6$ is singled out in the theory: it is the unique symmetric group with an outer automorphism.

**Is NOT an instance — a non-bijective endomorphism.** The map $\mathbb{Z} \to \mathbb{Z}$, $x \mapsto 2x$, is a [[Def - Homomorphism|homomorphism]] of the additive group $\mathbb{Z}$ — it preserves addition — but it is *not* an automorphism, because it is not surjective (odd integers are not in the image). It is an *endomorphism* but not an *automorphism*. The lesson: $\operatorname{Aut}(G)$ requires *iso*morphisms; the larger monoid $\operatorname{End}(G)$ of all self-[[Def - Homomorphism|homomorphisms]] is not a group, and $\operatorname{Aut}(G)$ is exactly its group of units. For an infinite group, an injective or surjective endomorphism need not be bijective.

**Is NOT an instance — conjugation is not an automorphism of $\operatorname{Aut}(G)$ in general.** It is tempting to think that because $\operatorname{Inn}(G) \trianglelefteq \operatorname{Aut}(G)$, the inner automorphisms behave like the centre of $\operatorname{Aut}(G)$. They do not: $\operatorname{Inn}(G)$ is normal in $\operatorname{Aut}(G)$ but is generally *not central* there, and not every automorphism of $G$ commutes with every inner one. The identity $\varphi\gamma_g\varphi^{-1} = \gamma_{\varphi(g)}$ shows the conjugate of an inner automorphism is inner — normality — but $\gamma_{\varphi(g)} \neq \gamma_g$ unless $\varphi$ fixes $g$ modulo the centre, so $\operatorname{Inn}(G)$ is normal without being central.

**Corollary — $G/Z(G) \cong \operatorname{Inn}(G)$, and a structural consequence.** The first isomorphism theorem applied to $\gamma : G \to \operatorname{Aut}(G)$ gives $G/Z(G) \cong \operatorname{Inn}(G)$ at once, since $\ker\gamma = Z(G)$ and $\operatorname{im}\gamma = \operatorname{Inn}(G)$. A non-obvious corollary: if $\operatorname{Inn}(G)$ is cyclic then $G/Z(G)$ is cyclic, which by the standard lemma forces $G$ to be [[Def - Abelian Group|abelian]] — and then $\operatorname{Inn}(G)$ is trivial. So $\operatorname{Inn}(G)$ can never be a non-trivial cyclic group: the inner automorphism group of any group is either trivial or non-cyclic.

**Corollary — an abelian group has trivial inner automorphism group.** If $G$ is [[Def - Abelian Group|abelian]] then $\gamma_g(x) = gxg^{-1} = x$ for every $g$, so every inner automorphism is the identity and $\operatorname{Inn}(G) = \{\operatorname{id}_G\}$. Consistently, $Z(G) = G$ so $G/Z(G)$ is trivial. For abelian groups all the automorphism content lives in $\operatorname{Out}(G) = \operatorname{Aut}(G)$.

**Corollary — the centre is the kernel, so conjugation is faithful if and only if $Z(G) = \{e\}$.** The conjugation homomorphism $\gamma : G \to \operatorname{Aut}(G)$ is injective exactly when its kernel $Z(G)$ is trivial. So a group acts faithfully on itself by conjugation precisely when it has trivial centre — such a group embeds into its own automorphism group as $\operatorname{Inn}(G) \cong G$. This is the calibration check linking this page to [[Def - Centraliser and Centre]]: the centre is the exact obstruction to conjugation being faithful.

---

# Unlocked by This

> [!tip] Semidirect Products *(from Group Theory III)*
> Building a group from a normal subgroup $N$ and a complement $H$ requires an action of $H$ on $N$ — that is, a [[Def - Homomorphism|homomorphism]] $H \to \operatorname{Aut}(N)$. The *semidirect product* $N \rtimes H$ is the construction that turns such a homomorphism into a group, and it is how all groups that are not direct products of their pieces are assembled. The automorphism group is the indispensable input.

> [!tip] The Outer Automorphism Group and $\operatorname{Out}(S_6)$ *(from Group Theory III)*
> The quotient $\operatorname{Out}(G) = \operatorname{Aut}(G)/\operatorname{Inn}(G)$ is a well-defined group precisely because $\operatorname{Inn}(G)$ is normal. Its computation is a delicate structural question — the celebrated fact that $\operatorname{Out}(S_n)$ is trivial for all $n \neq 6$ and equals $\mathbb{Z}/2$ for $n = 6$ is a highlight of the theory of symmetric groups.

> [!tip] Galois Groups *(from Field Theory)*
> The Galois group of a field extension $L/K$ is the automorphism group of $L$ consisting of those automorphisms that fix $K$ pointwise — an automorphism group constrained to fix a substructure. The Galois correspondence between intermediate fields and subgroups is the central theorem built on this idea.

> [!tip] Characteristic Subgroups *(from Group Theory III)*
> A subgroup is *characteristic* when it is invariant under *every* automorphism in $\operatorname{Aut}(G)$, not merely the inner ones — strictly stronger than [[Def - Normal Subgroup|normal]] (which is invariance under $\operatorname{Inn}(G)$). Characteristic subgroups are exactly what is needed to make normality transfer up a tower, repairing the non-transitivity of the normal relation.
