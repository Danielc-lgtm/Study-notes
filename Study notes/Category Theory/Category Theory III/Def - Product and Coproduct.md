---
type: definition
subject: category-theory
prereqs:
  - "Def - Category"
  - "Def - Initial and Terminal Object"
  - "Def - Universal Property and Universal Arrow"
tags: [category-theory, foundations]
---

# Notation

Throughout, $\mathcal{C}$ is a [[Def - Category|category]], with objects written $A, B, C, X$ and morphisms $f, g, h$. The hom-set of morphisms $A \to B$ is $\mathcal{C}(A, B)$, also written $\mathrm{Hom}_{\mathcal{C}}(A, B)$. The identity on $A$ is $1_A$. A **product** of $A$ and $B$ is written $A \times B$, equipped with **projections** $\pi_1 : A \times B \to A$ and $\pi_2 : A \times B \to B$. A **coproduct** is written $A \sqcup B$ or $A + B$ (or $A \amalg B$), equipped with **injections** $\iota_1 : A \to A + B$ and $\iota_2 : B \to A + B$. For a family $(A_i)_{i \in I}$ we write $\prod_{i \in I} A_i$ and $\coprod_{i \in I} A_i$. The named categories used are $\mathbf{Set}$ (sets and functions), $\mathbf{Grp}$ (groups), $\mathbf{Ab}$ (abelian groups), $\mathbf{Vect}_k$ ($k$-vector spaces), $\mathbf{Top}$ (topological spaces), $\mathbf{CRing}$ (commutative rings with $1$). The full registry is on [[Category Theory III — Limits and Colimits]].

This is a compound page: it defines two interlocking notions — the **product** and the **coproduct** — because they are exact categorical duals, introduced together, and neither is fully understood without the other. The coproduct is nothing but the product computed in the [[Def - Opposite Category and Duality|opposite category]], so every sentence about one has a mirror sentence about the other.

---

# Axiom Motivation

Start with the cartesian product of two sets, $A \times B = \{(a, b) : a \in A,\ b \in B\}$, and ask what *characterises* it — not how it is built from ordered pairs, but what job it does. The answer is the source of the whole definition. The set $A \times B$ comes with two projection functions $\pi_1(a, b) = a$ and $\pi_2(a, b) = b$. Its defining feature is this: to specify a function $X \to A \times B$ is *exactly* the same as to specify a function $X \to A$ together with a function $X \to B$. If you know where each $x$ goes in $A$ and where it goes in $B$, you know its image $(f(x), g(x))$ in the product, and conversely. The product is the object that "packages a pair of outgoing maps into a single outgoing map".

This packaging property is what we promote to a definition. We want an object $P$ with two maps $\pi_1 : P \to A$, $\pi_2 : P \to B$ such that for *any* object $X$ and *any* pair of maps $f : X \to A$, $g : X \to B$, there is one and only one map $\langle f, g \rangle : X \to P$ making the two triangles commute: $\pi_1 \circ \langle f, g \rangle = f$ and $\pi_2 \circ \langle f, g \rangle = g$. The phrase "one and only one" is doing all the work, and it is worth dwelling on why both halves are needed. **Existence** says the product is big enough — every compatible pair of maps factors through it, so it loses no information. **Uniqueness** says it is not too big — there is no slack, no redundant element. Drop uniqueness and the definition is satisfied by far too much: in $\mathbf{Set}$, the disjoint union $A \sqcup B$ admits a map to it from any $X$ given maps to $A$ and $B$ (send $x$ to its $A$-image *or* its $B$-image), but the choice is not forced, so the "product" would not be well-defined. Drop existence and you have no construction at all. The two conditions together are precisely the assertion that the functor $X \mapsto \mathcal{C}(X, A) \times \mathcal{C}(X, B)$ is **representable**, represented by $P$.

Why phrase it through maps *into* $P$ rather than describing $P$'s elements? Because most categories have no useful notion of "element". In $\mathbf{Top}$ the product topology is not determined by the underlying set of pairs alone — it is determined by which functions into it are continuous, and that is exactly the universal property. In $\mathbf{Grp}$ the relevant structure is which group homomorphisms land in $P$. The universal property is the one description that survives the passage from $\mathbf{Set}$ to every other category, and it is the reason the *same word* "product" names the cartesian product of sets, the direct product of groups, the product topology, and the meet in a poset.

Now dualise. Reverse every arrow. Instead of an object receiving a map from $X$ given maps into $A$ and $B$, ask for an object $C$ *emitting* a map to $X$ given maps *out of* $A$ and $B$. This is the **coproduct**: an object with injections $\iota_1 : A \to C$, $\iota_2 : B \to C$ such that any pair of maps $f : A \to X$, $g : B \to X$ factors uniquely as $[f, g] : C \to X$ with $[f, g] \circ \iota_1 = f$ and $[f, g] \circ \iota_2 = g$. Where the product packages two maps *in*, the coproduct packages two maps *out* — it is the universal object you can map out of by specifying what to do on each piece separately, with no compatibility required between the pieces because they are kept disjoint. The reason this deserves a name and is not automatically the product is that in most categories the two constructions are genuinely different objects: in $\mathbf{Set}$ the product is the cartesian product and the coproduct is the disjoint union, and $|A \times B| = |A| \cdot |B|$ while $|A \sqcup B| = |A| + |B|$.

The last thing to motivate is why the empty case matters. The product of *no* objects is the [[Def - Initial and Terminal Object|terminal object]] $1$ (the empty family of projections, and a unique map $X \to 1$ from everything), and the coproduct of no objects is the [[Def - Initial and Terminal Object|initial object]] $0$. This is not a degenerate curiosity: it forces the terminal and initial objects into the same framework as products and coproducts, and it is the reason a category "with all finite products" is required to have a terminal object as the nullary case.

---

# The Definition

Let $\mathcal{C}$ be a category and $A, B \in \mathcal{C}$.

A **product** of $A$ and $B$ is an object $A \times B$ together with two morphisms, the **projections**
$$\pi_1 : A \times B \to A, \qquad \pi_2 : A \times B \to B,$$
satisfying the following universal property: for every object $X$ and every pair of morphisms $f : X \to A$ and $g : X \to B$, there exists a *unique* morphism $\langle f, g \rangle : X \to A \times B$ such that
$$\pi_1 \circ \langle f, g \rangle = f \qquad \text{and} \qquad \pi_2 \circ \langle f, g \rangle = g.$$
The morphism $\langle f, g \rangle$ is called the morphism **induced** by $f$ and $g$.

Dually, a **coproduct** of $A$ and $B$ is an object $A + B$ together with two morphisms, the **injections** (or **coprojections**)
$$\iota_1 : A \to A + B, \qquad \iota_2 : B \to A + B,$$
satisfying: for every object $X$ and every pair of morphisms $f : A \to X$ and $g : B \to X$, there exists a *unique* morphism $[f, g] : A + B \to X$ such that
$$[f, g] \circ \iota_1 = f \qquad \text{and} \qquad [f, g] \circ \iota_2 = g.$$

The definition extends verbatim to an arbitrary family $(A_i)_{i \in I}$: the **product** $\prod_{i \in I} A_i$ carries projections $\pi_i : \prod_j A_j \to A_i$ and is universal among objects mapping compatibly into all the $A_i$; the **coproduct** $\coprod_{i \in I} A_i$ carries injections $\iota_i : A_i \to \coprod_j A_j$ and is universal among objects receiving maps from all the $A_i$. The product of the empty family is a [[Def - Initial and Terminal Object|terminal object]]; the coproduct of the empty family is an initial object. When all binary products (and a terminal object) exist, $\mathcal{C}$ is said to **have finite products**; similarly for finite coproducts.

---

# Categorical / Structural Definition

The product and coproduct are the two simplest [[Def - Limit and Colimit|limits and colimits]], and stating them in that language is the cleanest way to see the duality. Let $J$ be a **discrete category** on the index set $I$ — a category with objects $I$ and no morphisms except identities. A functor $D : J \to \mathcal{C}$ is then just a choice of an object $D_i = A_i$ for each $i$, with no relations to satisfy. A [[Def - Cone and Cocone|cone]] over $D$ with apex $X$ is a family of maps $(X \to A_i)_{i}$ — and because $J$ has no non-identity morphisms, there are *no* commutativity conditions to impose. The product $\prod_i A_i$ is precisely the [[Def - Limit and Colimit|limit]] of $D$: the universal (terminal) such cone. Dually the coproduct $\coprod_i A_i$ is the **colimit** of $D$: the universal cocone, a family of maps $(A_i \to C)_i$ initial among all such.

There is a second, sharper structural reading via representability. The product represents the functor
$$X \;\longmapsto\; \mathcal{C}(X, A) \times \mathcal{C}(X, B) : \mathcal{C}^{op} \to \mathbf{Set},$$
meaning there is a natural isomorphism $\mathcal{C}(X, A \times B) \cong \mathcal{C}(X, A) \times \mathcal{C}(X, B)$. This is the bijection "a map into the product is a pair of maps", and naturality in $X$ is automatic. The coproduct represents
$$X \;\longmapsto\; \mathcal{C}(A, X) \times \mathcal{C}(B, X) : \mathcal{C} \to \mathbf{Set},$$
giving $\mathcal{C}(A + B, X) \cong \mathcal{C}(A, X) \times \mathcal{C}(B, X)$ — "a map out of the coproduct is a pair of maps". These two isomorphisms are the operational heart of the definitions and the reason [[Thm - Representable Functors Preserve Limits|representable functors preserve limits]].

---

# Relate to Other Fields / Compression

The product is the categorical distillation of every "pairing" construction in mathematics, and the coproduct of every "free combination". In $\mathbf{Set}$, product is cartesian product and coproduct is disjoint union — the multiplicative and additive structures on cardinalities. In a [[Def - Category|poset viewed as a category]] (one arrow $a \to b$ whenever $a \le b$), the product of $a$ and $b$ is their **greatest lower bound** $a \wedge b$ (meet) and the coproduct is their **least upper bound** $a \vee b$ (join): the universal property "$x \le a$ and $x \le b$ iff $x \le a \wedge b$" is exactly the product property with arrows being $\le$. In $\mathbf{Vect}_k$ the finite product and finite coproduct *coincide* — both are the direct sum $\bigoplus$ — which is the categorical shadow of the fact that $\mathbf{Vect}_k$ is an **abelian category** where finite biproducts exist.

**True name:** a product is "the object whose maps-in are pairs of maps-in"; a coproduct is "the object whose maps-out are pairs of maps-out". When solving a problem, do not picture the elements of $A \times B$ — picture the bijection $\mathcal{C}(X, A \times B) \cong \mathcal{C}(X, A) \times \mathcal{C}(X, B)$ and read off what you need.

---

# Examples / Corollaries

**Is an instance — products and coproducts in $\mathbf{Set}$.** The product is the cartesian product $A \times B = \{(a,b)\}$ with $\pi_1, \pi_2$ the coordinate projections; given $f, g$ the induced map is $\langle f, g\rangle(x) = (f(x), g(x))$, manifestly the unique function with the right projections. The coproduct is the **disjoint union** $A \sqcup B$, the set of all elements of $A$ and all of $B$ kept distinct (formally $\{0\} \times A \cup \{1\} \times B$); the injections are the inclusions, and $[f,g]$ is "apply $f$ on the $A$-part, $g$ on the $B$-part". These differ: a pair of functions *into* $A$ and $B$ glues into one function into $A \times B$; a pair of functions *out of* $A$ and $B$ glues into one function out of $A \sqcup B$.

**Is an instance — in $\mathbf{Grp}$ and $\mathbf{Ab}$ the product and coproduct part ways.** The product of groups is the [[Def - Direct Product|direct product]] $G \times H$ with componentwise multiplication and the obvious projections — this is the product in both $\mathbf{Grp}$ and $\mathbf{Ab}$. The coproduct, however, depends on the category. In $\mathbf{Ab}$, the coproduct of $A$ and $B$ is the [[Def - Direct Sum of Modules|direct sum]] $A \oplus B$, which for finitely many summands equals the direct product; the injections are $a \mapsto (a, 0)$ and $b \mapsto (0, b)$, and a pair of homomorphisms $A \to X$, $B \to X$ glues because in an abelian target the two images commute. In $\mathbf{Grp}$, the coproduct is the [[Def - Free Group and Free Product|free product]] $G * H$ — the group of reduced words alternating between $G$ and $H$ with *no* commutation imposed — which is infinite and non-abelian whenever both factors are non-trivial. The contrast is sharp: $C_2 \sqcup C_2$ in $\mathbf{Ab}$ is the Klein four-group $C_2 \oplus C_2$ of order $4$, while $C_2 * C_2$ in $\mathbf{Grp}$ is the infinite dihedral group.

**Is an instance — in $\mathbf{Top}$, the product topology and the disjoint union topology.** The product $X \times Y$ carries the [[Def - Product Topology|product topology]], whose defining feature is precisely the universal property: it is the coarsest topology making both projections continuous, equivalently the topology for which a map $Z \to X \times Y$ is continuous iff both components $Z \to X$, $Z \to Y$ are. The coproduct carries the **disjoint union topology**, in which a set is open iff it meets each summand in an open set, so that a map out of $X \sqcup Y$ is continuous iff its restrictions to $X$ and $Y$ are. This is the universal-property origin of the product topology — it is *forced* by demanding the limit characterisation, not chosen by fiat.

**Is an instance — in $\mathbf{CRing}$ the coproduct is the tensor product.** The coproduct of two commutative rings $R_1, R_2$ (over the base $\mathbb{Z}$, or over a common subring $S$) is the [[Def - Tensor Product of Modules|tensor product]] $R_1 \otimes_{\mathbb{Z}} R_2$ (resp. $R_1 \otimes_S R_2$), with the injections $r \mapsto r \otimes 1$ and $r \mapsto 1 \otimes r$. A pair of ring maps $R_1 \to T$, $R_2 \to T$ glues into a single map $R_1 \otimes R_2 \to T$, $r_1 \otimes r_2 \mapsto$ (product of images), precisely because the images commute in the commutative ring $T$. This is the algebraic reason that, geometrically, *gluing* affine schemes corresponds to *tensoring* rings — see the algebraic geometry callout below.

**Is NOT an instance — the union of two subsets is not their coproduct in $\mathbf{Set}$.** It is tempting to think the coproduct of $A$ and $B$ is the ordinary union $A \cup B$. It is not, unless $A$ and $B$ are disjoint. If $A = B = \{*\}$ then $A \cup B = \{*\}$ has one element, but the coproduct $A \sqcup B$ has two, because the universal property requires the injections $\iota_1, \iota_2$ to be jointly able to separate a pair of maps that disagree on the shared point — a single shared point would force $f(*) = g(*)$, violating universality. The coproduct *keeps the copies distinct*; overlap is exactly what it refuses.

**Is NOT an instance — in $\mathbf{Field}$, products need not exist.** The product of two fields of different characteristic, say $\mathbb{Q}$ and $\mathbb{F}_2$, does not exist in the category of fields, because the would-be product $\mathbb{Q} \times \mathbb{F}_2$ (as rings) is not a field — it has zero divisors. This shows that "has products" is a genuine hypothesis on a category, not a theorem: $\mathbf{Set}$, $\mathbf{Grp}$, $\mathbf{Top}$ have all products, but $\mathbf{Field}$ does not even have binary ones.

**Calibration check.** Verify that the projection $\pi_1 : A \times B \to A$ together with $\langle 1_A, 1_A \rangle$ shows the diagonal map exists; that $\langle \pi_1, \pi_2 \rangle = 1_{A \times B}$ (uniqueness applied to the identity); and that in a poset the product of $a$ and $b$ existing for all pairs is the statement that the poset is a meet-semilattice. If you can also explain why the coproduct in $\mathbf{Ab}$ but not in $\mathbf{Grp}$ coincides with the product for two summands, you have understood the role of commutativity in gluing maps out.

---

# Unlocked by This

> [!note]- Algebraic geometry background
> A **commutative ring** is a set with addition and multiplication satisfying the usual axioms, with $1 \cdot x = x$ and $xy = yx$; examples are $\mathbb{Z}$, the polynomial ring $k[x,y]$, and quotients like $\mathbb{Z}[x,y]/(y^2 - x^3 + 1)$. Classical algebraic geometry studies solution sets of polynomial equations. The modern **functor of points** viewpoint packages a geometric object $X$ as a functor $X : \mathbf{CRing} \to \mathbf{Set}$ sending each ring $R$ to "the set of $R$-points of $X$" — for the curve $y^2 = x^3 - 1$, this is $R \mapsto \{(a,b) \in R^2 : b^2 = a^3 - 1\}$. An **affine scheme** is such a functor that is *representable*: it equals $\mathbf{CRing}(R, -)$ for some ring $R$, written $\mathrm{Spec}\,R$. The assignment $R \mapsto \mathrm{Spec}\,R$ is the **spectrum functor** $\mathrm{Spec} : \mathbf{CRing}^{op} \to \mathbf{AffSch}$, which is a contravariant equivalence — it is the [[Def - The Yoneda Embedding|Yoneda embedding]] of $\mathbf{CRing}^{op}$, hence fully faithful.
>
> Here is the payoff for *this* page. The coproduct in $\mathbf{CRing}$ is the tensor product $R_1 \otimes_S R_2$. Because $\mathrm{Spec}$ is a contravariant equivalence (a Yoneda embedding), it turns coproducts of rings into products of schemes — and more generally **pushouts of rings into pullbacks of schemes**:
> $$\mathrm{Spec}(R_1 \otimes_S R_2) \;\cong\; \mathrm{Spec}\,R_1 \times_{\mathrm{Spec}\,S} \mathrm{Spec}\,R_2.$$
> So the **fibre product of schemes** — the central construction for intersections, fibres of a morphism, and base change — *is* a categorical [[Def - Pullback and Pushout|pullback]], and it is computed by tensoring rings. The universal property of the product/coproduct you have just learned, run through the Yoneda embedding $\mathrm{Spec}$, is what makes algebraic geometry's gluing-equals-tensoring dictionary precise. This is developed fully on the page [[Ex - Fibre products of schemes are pullbacks]].

> [!tip] Biproducts and Abelian Categories *(from Homological Algebra)*
> When finite products and coproducts coincide (as in $\mathbf{Ab}$ and $\mathbf{Vect}_k$), the common object $A \oplus B$ is a **biproduct**, and the existence of all finite biproducts together with kernels and cokernels is the backbone of an **abelian category** — the setting in which homological algebra, **derived functors**, and **Ext/Tor** live.

> [!tip] Markov Categories *(from Categorical Probability)*
> A **Markov category** is a symmetric monoidal category whose tensor is a categorical product *only up to* copy-and-discard structure; the failure of the monoidal product to be a genuine product is exactly the presence of randomness. Understanding products as the universal "copy without loss" object is the entry point to the categorical formulation of probability and **compositional game theory**.
