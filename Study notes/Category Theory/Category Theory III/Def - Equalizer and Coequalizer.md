---
type: definition
subject: category-theory
prereqs:
  - "Def - Category"
  - "Def - Product and Coproduct"
  - "Def - Isomorphism, Monomorphism, Epimorphism"
tags: [category-theory, foundations]
---

# Notation

Throughout, $\mathcal{C}$ is a [[Def - Category|category]]. A **parallel pair** is a pair of morphisms $f, g : A \rightrightarrows B$ with common domain $A$ and common codomain $B$. An **equalizer** of $f, g$ is a morphism $e : E \to A$ written $\mathrm{eq}(f, g)$; a **coequalizer** is a morphism $q : B \to Q$ written $\mathrm{coeq}(f, g)$. The named categories are $\mathbf{Set}$, $\mathbf{Grp}$, $\mathbf{Ab}$, $\mathbf{Vect}_k$, $\mathbf{Top}$. The full registry is on [[Category Theory III — Limits and Colimits]].

This is a compound page: it defines two interlocking notions — the **equalizer** and the **coequalizer** — because they are exact categorical duals (the coequalizer is the equalizer in the [[Def - Opposite Category and Duality|opposite category]]), and the pair together captures the categorical meaning of "the subobject where two maps agree" and "the quotient that forces two maps to agree".

---

# Axiom Motivation

The product solved "package two outgoing maps into one". The equalizer solves a different and equally fundamental problem: **carve out the part of an object where two maps agree**. In $\mathbf{Set}$, given two functions $f, g : A \to B$, the set $\{a \in A : f(a) = g(a)\}$ is the natural object — the locus of agreement, the solution set of the equation $f = g$. Almost every "subset cut out by an equation" in mathematics is of this form: the unit circle is where $x^2 + y^2$ agrees with the constant $1$; the kernel of a homomorphism is where $\varphi$ agrees with the zero map; a fixed-point set is where $h$ agrees with the identity. We want a definition of this locus that uses only arrows, so it makes sense in $\mathbf{Top}$, $\mathbf{Grp}$, and everywhere else.

The arrow-only characterisation comes from asking what maps *into* the agreement-locus look like. A map $z : Z \to A$ factors through $\{a : f(a) = g(a)\}$ exactly when its image lands in that set, which is to say exactly when $f \circ z = g \circ z$ — every point $z(w)$ satisfies the equation. So the agreement-locus is the universal object $E$ equipped with a map $e : E \to A$ satisfying $f \circ e = g \circ e$, through which every other map satisfying that same equation factors uniquely. The clause "$f \circ e = g \circ e$" says $E$ *lies in* the agreement-locus; the universality says $E$ *is all* of it, with no slack.

Why insist on uniqueness of the factorisation? Without it, the definition is satisfied by anything large enough to map onto the locus, and the equalizer would not be pinned down. Uniqueness is what forces $e$ to be a **monomorphism** — and this is the first theorem about equalizers, that every equalizer is monic. The intuition is exactly the set-theoretic picture: $E$ is a *subobject* of $A$, an honest inclusion, because the agreement-locus sits inside $A$ without folding. If you dropped uniqueness you could equalize through a set with repeated points, and $e$ would no longer be an inclusion. So uniqueness is not bookkeeping; it is the condition that makes "equalizer" mean "subobject cut out by an equation".

Now dualise, and something initially surprising happens. Reverse all the arrows: instead of the universal object mapping *into* $A$ on which $f$ and $g$ already agree, we want the universal object *receiving* a map from $B$ that *forces* $f$ and $g$ to become equal. This is the **coequalizer**: a map $q : B \to Q$ with $q \circ f = q \circ g$, universal among all maps out of $B$ that coequalize the pair. In $\mathbf{Set}$ this is the quotient of $B$ by the smallest equivalence relation that identifies $f(a)$ with $g(a)$ for every $a \in A$. Where the equalizer *selects* a subobject, the coequalizer *collapses* by an imposed relation. The reason this is the right dual is the same reason as before, read backwards: factoring a map $z : B \to Z$ through the quotient $Q$ is possible exactly when $z$ already respects the identifications, i.e. when $z \circ f = z \circ g$.

The single most important consequence to keep in view while learning the definition is what the dual pair specialises to in algebra. A **kernel** is an equalizer (of $\varphi$ and the zero map), and a **quotient** is a coequalizer. The first isomorphism theorem — every map factors as a quotient followed by an injection — is, categorically, the statement that the coequalizer of the kernel-pair reconstructs the image. So these two definitions are not new machinery bolted onto algebra; they are algebra's kernels and quotients stated so they apply to spaces, sheaves, and schemes as well.

---

# The Definition

Let $f, g : A \rightrightarrows B$ be a parallel pair of morphisms in $\mathcal{C}$.

An **equalizer** of $f$ and $g$ is an object $E$ together with a morphism $e : E \to A$ satisfying $f \circ e = g \circ e$, and universal with this property: for every morphism $z : Z \to A$ with $f \circ z = g \circ z$, there exists a *unique* morphism $u : Z \to E$ such that $e \circ u = z$.
$$E \xrightarrow{\;e\;} A \;\underset{g}{\overset{f}{\rightrightarrows}}\; B, \qquad f \circ e = g \circ e.$$

Dually, a **coequalizer** of $f$ and $g$ is an object $Q$ together with a morphism $q : B \to Q$ satisfying $q \circ f = q \circ g$, and universal: for every $z : B \to Z$ with $z \circ f = z \circ g$, there exists a *unique* $u : Q \to Z$ such that $u \circ q = z$.
$$A \;\underset{g}{\overset{f}{\rightrightarrows}}\; B \xrightarrow{\;q\;} Q, \qquad q \circ f = q \circ g.$$

Two basic facts follow immediately from universality, and are part of the definition's content:

- **Every equalizer is a monomorphism.** If $e \circ u = e \circ u'$ then $u = u'$, because both $u, u'$ are factorisations of the same map $e \circ u$ through $e$, and the factorisation is unique.
- **Every coequalizer is an epimorphism.** Dually.

---

# Categorical / Structural Definition

The equalizer is the [[Def - Limit and Colimit|limit]] of a diagram of a specific shape, and the coequalizer its colimit. Let $J$ be the category with two objects $\bullet, \bullet$ and exactly two non-identity arrows $\bullet \rightrightarrows \bullet$ both pointing the same way (the "parallel pair" shape). A functor $D : J \to \mathcal{C}$ is exactly a parallel pair $f, g : A \rightrightarrows B$. A [[Def - Cone and Cocone|cone]] over $D$ with apex $Z$ is a pair of maps $Z \to A$ and $Z \to B$ commuting with both $f$ and $g$ — but the leg $Z \to B$ is forced to equal $f \circ (Z \to A) = g \circ (Z \to A)$, so the data reduces to a single map $z : Z \to A$ with $f z = g z$. The limit of $D$ — the terminal such cone — is precisely the equalizer. Dually the coequalizer is the colimit.

There is a clean reduction of equalizers to [[Def - Pullback and Pushout|pullbacks]] and products that is worth recording, because it shows equalizers are not independent data. In a category with binary products, the equalizer of $f, g : A \rightrightarrows B$ is obtained as the pullback of the diagonal $\Delta = \langle 1_B, 1_B \rangle : B \to B \times B$ against the map $\langle f, g \rangle : A \to B \times B$:
$$\mathrm{eq}(f,g) \;=\; A \times_{B \times B} B.$$
A map into this pullback is a map $z : Z \to A$ such that $\langle f, g\rangle \circ z$ factors through the diagonal, which says exactly $f z = g z$. This is the structural reason that a category with finite products and pullbacks already has all finite limits.

---

# Relate to Other Fields / Compression

The equalizer is the categorical face of "solution set of an equation" and the coequalizer of "quotient by relations". In every algebraic category the kernel is a disguised equalizer: for a [[Def - Homomorphism|homomorphism]] $\varphi : A \to B$ of [[Def - Abelian Group|abelian groups]] (or modules, or vector spaces), $\ker\varphi$ is the equalizer of $\varphi$ and the zero map $0 : A \to B$, because $\mathrm{eq}(\varphi, 0) = \{a : \varphi(a) = 0(a) = 0\}$. Dually the quotient $B / \mathrm{im}(\varphi)$ — and more pointedly the [[Def - Quotient Group|quotient group]] $G/N$ — is a coequalizer.

**True name:** an equalizer is "the largest subobject of $A$ on which $f$ and $g$ become equal"; a coequalizer is "the largest quotient of $B$ on which $f$ and $g$ become equal". The mnemonic is that equalizers live *over $A$* (the domain) as subobjects, while coequalizers live *under $B$* (the codomain) as quotients — agreement enforced by restriction versus agreement enforced by collapse.

---

# Examples / Corollaries

**Is an instance — equalizers in $\mathbf{Set}$.** For $f, g : A \to B$, the equalizer is the inclusion $\{a \in A : f(a) = g(a)\} \hookrightarrow A$. Concretely, with $f, g : \mathbb{R}^2 \to \mathbb{R}$ given by $f(x,y) = x^2 + y^2$ and $g(x,y) = 1$, the equalizer is the unit circle $\{(x,y) : x^2 + y^2 = 1\}$ included into the plane. Every "level set" is an equalizer.

**Is an instance — the kernel as an equalizer in $\mathbf{Ab}$.** For homomorphisms $f, g : A \to B$ of abelian groups, $f(a) = g(a) \iff (f - g)(a) = 0$, so the equalizer of $f$ and $g$ equals the equalizer of $f - g$ and the zero map, which is $\ker(f - g)$. In particular the kernel of a single homomorphism $\varphi$ is $\mathrm{eq}(\varphi, 0)$. This is the categorical source of kernels.

**Is an instance — coequalizers in $\mathbf{Set}$ are quotients.** For $f, g : A \to B$, the coequalizer is the quotient $B / {\sim}$, where $\sim$ is the *smallest equivalence relation* containing all pairs $(f(a), g(a))$ for $a \in A$, with $q$ the quotient map. The need to *generate* an equivalence relation (closing $\{(f(a), g(a))\}$ under reflexivity, symmetry, transitivity) is the content: the coequalizer forces $f$ and $g$ equal and then forces whatever follows by equivalence.

**Is an instance — coequalizers in $\mathbf{Grp}$ and the role of normal closure.** In $\mathbf{Grp}$, the coequalizer of $f, g : A \rightrightarrows B$ is the quotient $B / N$, where $N$ is the **normal closure** of the subgroup $\{f(a)g(a)^{-1} : a \in A\}$ — the smallest [[Def - Normal Subgroup|normal subgroup]] forcing $f(a) = g(a)$. The reason it is the *normal* closure rather than the subgroup itself is that only [[Def - Quotient Group|quotients by normal subgroups]] are groups, so the universal group-quotient must normalise. Taking $g$ to be constant at the identity, the coequalizer of $f$ and the trivial map is $B$ modulo the normal closure of $\mathrm{im}(f)$.

**Is NOT an instance — a non-injective map is not an equalizer.** An equalizer is always a monomorphism, so a map that is not monic cannot be an equalizer of any pair. In $\mathbf{Set}$ the map $\{0, 1\} \to \{*\}$ is not an equalizer of anything, because it is not injective. This is the diagnostic: if a candidate "agreement-locus map" fails to be monic, the construction has gone wrong.

**Is NOT an instance — the set-theoretic image of $f - g$ is not the coequalizer.** It is tempting to think the coequalizer of $f, g : A \to B$ in $\mathbf{Set}$ is $B$ minus the points where $f$ and $g$ disagree, or some subset. It is not a subset at all — it is a quotient, and it is generally *smaller* than $B$ only after transitive closure. For $A = \{1, 2\}$, $B = \{x, y, z\}$, $f(1) = x, g(1) = y, f(2) = y, g(2) = z$, the generated equivalence glues $x \sim y \sim z$, so the coequalizer is a single point, not two.

**Calibration check.** Verify that the equalizer of $f$ with itself ($f = g$) is the identity $1_A$ (everything agrees), and dually the coequalizer of $f$ with itself is $1_B$. Check that in $\mathbf{Ab}$ the cokernel $\mathrm{coker}(\varphi) = B/\mathrm{im}\,\varphi$ is the coequalizer of $\varphi$ and $0$. If you can also explain why generating an equivalence relation (not just the relation itself) is forced in the $\mathbf{Set}$ coequalizer, you have understood the universality.

---

# Unlocked by This

> [!tip] Kernels, Cokernels, and Abelian Categories *(from Homological Algebra)*
> When the equalizer of $(\varphi, 0)$ is taken in a category with a zero object it is called a **kernel**, and its dual the **cokernel**. A category where every map has a kernel and cokernel, finite biproducts exist, and every mono is a kernel and every epi a cokernel, is an **abelian category** — the home of chain complexes, exact sequences, and **derived functors** (**Ext**, **Tor**).

> [!tip] Regular and Exact Categories *(from Categorical Logic)*
> A category in which every morphism factors as a (regular epi)-then-mono using coequalizers of **kernel pairs** is a **regular category**; adding effective equivalence relations gives an **exact category**. This is the categorical engine behind the first isomorphism theorem holding uniformly, and it underpins the internal logic of a **topos**.
