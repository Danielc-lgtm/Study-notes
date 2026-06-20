---
type: definition
subject: higher-categories
prereqs:
  - "Def - Monad and Comonad"
  - "Def - Category"
  - "Def - Functor"
tags: [category-theory, higher-categories, foundations]
---

# Notation

Throughout, $\mathbb{G}$ is the **globe category**: its objects are the formal symbols $[0], [1], [2], \dots$ (one for each dimension), and its only non-identity arrows are two parallel maps $\sigma, \tau : [n] \to [n+1]$ in each dimension, subject to the **globularity relations** $\sigma\sigma = \tau\sigma$ and $\sigma\tau = \tau\tau$. A **globular set** $X$ is a presheaf on $\mathbb{G}$, that is a functor $X : \mathbb{G}^{op} \to \mathbf{Set}$; concretely it is a sequence of sets $X(0), X(1), X(2), \dots$ of $n$-cells together with **source** and **target** maps $s, t : X(n+1) \to X(n)$ satisfying $ss = ts$ and $st = tt$. I write $[\mathbb{G}^{op}, \mathbf{Set}]$ for the category of globular sets and maps between them. The monad of this page is written $(T, \eta, \mu)$, with $T$ the free-strict-$\omega$-category endofunctor, $\eta : 1 \Rightarrow T$ the unit, and $\mu : T^2 \Rightarrow T$ the multiplication. The terminal globular set $1$ has one cell in every dimension; $T1$ is written $\mathrm{pd}$, the globular set of **pasting diagrams**, with $\mathrm{pd}(m) = (T1)(m)$. The boundary operator on pasting diagrams (the source and target, which coincide on $1$) is written $\partial : \mathrm{pd}(m+1) \to \mathrm{pd}(m)$. The full symbol registry is on the parent page [[Higher Categories — Globular Operads and Weak n-Categories]].

A note on what is *not* hyperlinked here: the definitions of **globular set** and **strict $\omega$-category** belong to an earlier chapter (Leinster 1.2, 1.4) whose pages are not yet in the vault, so they appear in bold rather than as wikilinks; this page restates everything it needs from them so that it stands alone.

---

# Axiom Motivation

The whole programme of Batanin–Leinster weak higher category theory rests on a single piece of machinery: a monad $T$ on globular sets whose free algebras are the strict $\omega$-categories and whose operations are *exactly the pasting diagrams*. Everything downstream — globular operads, contractions, the operad $L$ — is built by perturbing this $T$. So before we can perturb it we must understand precisely what it is and, above all, *why it has to be cartesian*. This page exists to install $T$ as the fixed point of the theory.

Start from the desideratum. A strict $\omega$-category is a globular set in which you can compose cells in every dimension, along every lower-dimensional boundary, and these compositions are strictly associative, strictly unital, and strictly satisfy the interchange law. We want a *free* such structure: given any globular set $X$ of "generating cells", we want the strict $\omega$-category $TX$ that has, as its $m$-cells, all the formal composites you can build out of the cells of $X$ and nothing else — no relations beyond those forced by the strict axioms. The existence of this free construction is what makes $T$ a monad: the unit $\eta_X : X \to TX$ includes the generators as the most basic composites, and the multiplication $\mu_X : T^2 X \to TX$ flattens a composite-of-composites into a single composite, exactly as a free monoid's multiplication concatenates words of words into one word.

The first axiom to motivate is **why $T$ should be described by pasting diagrams at all**. Apply $T$ to the terminal globular set $1$, the one with a single cell in each dimension. A composite built from the cells of $1$ retains no information about *which* cells were composed — there is only one cell of each dimension — but it retains the full information about the *shape* of the composite: how many cells were strung together, in what arrangement, along which boundaries. That shape is precisely a **globular pasting diagram**: a formal arrangement of globes that can legally be pasted together. So $T1 = \mathrm{pd}$, and the cleanest description is recursive. A $0$-pasting diagram is a point: $\mathrm{pd}(0) = 1$. An $(m+1)$-pasting diagram is a *finite sequence* of $m$-pasting diagrams strung head-to-tail: $\mathrm{pd}(m+1) = \mathrm{pd}(m)^{\ast}$, where $(-)^{\ast}$ is the free-monoid (finite-list) functor. A $2$-cell shape like "three $2$-cells stacked vertically over a string of $1$-cells" is literally a list of lists of points. This recursion is not a definition we impose; it is forced by the meaning of "free composite", and it is what Appendix F of Leinster proves rigorously.

Now the decisive axiom: **$T$ must be cartesian.** A monad $(T, \eta, \mu)$ on a category with pullbacks is cartesian when (a) $T$ preserves pullbacks, and (b) the unit $\eta$ and multiplication $\mu$ are *cartesian* natural transformations, meaning every naturality square
$$
\begin{array}{ccc}
TX & \xrightarrow{\ Tf\ } & TY \\
\downarrow{\scriptstyle\eta_X} & & \downarrow{\scriptstyle\eta_Y} \\
\cdots & & \cdots
\end{array}
$$
is a pullback square (and likewise for $\mu$). Why demand this? Because the entire definition of a **generalized operad** — a globular operad is a $T$-operad — requires it. A $T$-operad is a globular set $P$ equipped with a *cartesian* map $d : P \to T1$ and an operad structure; the cartesianness of $T$ is exactly what guarantees that the slice category over $T1$ inherits a sensible "substitution" monoidal structure in which one can even *state* the operad axioms. Drop cartesianness and the operad framework collapses: there is no associative substitution, no notion of "operations sitting over a pasting diagram", no fibres $P(\pi)$. The cartesian condition is the load-bearing hypothesis, and it is a genuine theorem (Leinster App F, building on the Pasting Lemma) that the free-strict-$\omega$-category monad satisfies it — most monads do not.

What breaks if we weaken "strict" to "weak" in the very definition of $T$? Then $TX$ would not be a *set* of formal composites but a category of composites-and-coherence-isomorphisms, $T$ would be a $2$-monad rather than an ordinary monad, and the clean cartesian theory would be unavailable. The Batanin–Leinster insight is precisely to keep the *base* monad strict — its algebras are the strict $\omega$-categories, which are easy — and to inject weakness later, by replacing the operad $1$ over $T1$ with the larger contractible operad $L$. So the strictness of $T$ is not a limitation; it is the firm ground on which the weak theory is built. And what if we strengthened $T$, say by passing to free *symmetric* or *braided* structures? We would leave globular sets for a richer base and obtain a different periodic-table corner; the globular, non-symmetric $T$ is the one whose operads model $\omega$-categories in the strict-globular sense.

The test of this motivation: a reader who has the recursion $\mathrm{pd}(m+1) = \mathrm{pd}(m)^{\ast}$ and the slogan "$T1$ is the shapes of free composites" should be able to predict that $T$ is cartesian *because* the free-monoid monad on $\mathbf{Set}$ is cartesian and $T$ is assembled, dimension by dimension, out of free-monoid functors — and that prediction is correct.

---

# The Definition

Let $[\mathbb{G}^{op}, \mathbf{Set}]$ be the category of **globular sets**.

> The **free strict $\omega$-category monad** is the monad $(T, \eta, \mu)$ on $[\mathbb{G}^{op}, \mathbf{Set}]$ induced by the free–forgetful adjunction
> $$
> F : [\mathbb{G}^{op}, \mathbf{Set}] \;\rightleftarrows\; \mathbf{Str\text{-}\omega\text{-}Cat} : U,
> \qquad F \dashv U,
> $$
> where $U$ is the forgetful functor sending a strict $\omega$-category to its underlying globular set and $F$ is its left adjoint. Explicitly $T = UF$, the unit $\eta : 1 \Rightarrow T$ is the unit of the adjunction (inclusion of generators), and $\mu : T^2 \Rightarrow T$ is $U\varepsilon F$ for the counit $\varepsilon$. The adjunction is monadic, so strict $\omega$-categories are precisely the $T$-algebras: $\mathbf{Str\text{-}\omega\text{-}Cat} \cong [\mathbb{G}^{op}, \mathbf{Set}]^{T}$.

The endofunctor $T$ is described concretely on the terminal globular set $1$: $T1 = \mathrm{pd}$ is the globular set of **globular pasting diagrams**, given recursively by
$$
\mathrm{pd}(0) = 1, \qquad \mathrm{pd}(m+1) = \mathrm{pd}(m)^{\ast},
$$
where $(-)^{\ast}$ is the free-monoid functor on $\mathbf{Set}$, with boundary $\partial : \mathrm{pd}(m+1) \to \mathrm{pd}(m)$ defined inductively. An element of $\mathrm{pd}(m)$ is an $m$-dimensional pasting diagram, the shape of a formal $m$-fold composite. For a general globular set $X$, an element of $(TX)(m)$ is a pasting diagram $\pi \in \mathrm{pd}(m)$ together with a labelling of each constituent cell of $\pi$ by a cell of $X$ of the matching dimension; the canonical projection $TX \to T1 = \mathrm{pd}$ forgets the labels and remembers the shape.

> The crucial property: $(T, \eta, \mu)$ is a **cartesian monad**, that is $T$ preserves pullbacks and the naturality squares of $\eta$ and $\mu$ are pullback squares. This is a theorem (Leinster, Appendix F), proved via the Pasting Lemma; it is what licenses the entire theory of globular operads in the next page.

---

# Categorical / Structural Definition

The structural heart of the definition is the **cartesianness**, and it is worth isolating because it is the property that propagates. A natural transformation $\alpha : F \Rightarrow G$ between functors $\mathcal{C} \to \mathcal{D}$ is **cartesian** if for every morphism $f : X \to Y$ in $\mathcal{C}$ the naturality square
$$
\begin{array}{ccc}
FX & \xrightarrow{\;Ff\;} & FY\\
{\scriptstyle\alpha_X}\big\downarrow & & \big\downarrow{\scriptstyle\alpha_Y}\\
GX & \xrightarrow{\;Gf\;} & GY
\end{array}
$$
is a [[Def - Pullback and Pushout|pullback]] in $\mathcal{D}$. A monad $(T, \eta, \mu)$ on a category $\mathcal{C}$ with pullbacks is a **cartesian monad** when $T$ preserves pullbacks and both $\eta$ and $\mu$ are cartesian natural transformations. (These pages call such a $T$ a **cartesian monad**; the page for the general notion belongs to an earlier chapter and is not yet in the vault.)

Why this is the right structural level. A cartesian monad $T$ on $\mathcal{C}$ is exactly the data needed to define a bicategory of **$T$-spans** (or "$T$-graphs"): an object is given by a span $T C_0 \xleftarrow{d} C_1 \xrightarrow{c} C_0$, and the cartesianness makes the composition of such spans (via pullback) associative and unital up to canonical iso. A **monad** in this bicategory of $T$-spans is precisely a **generalized multicategory** for $T$; a one-object such monad is a **generalized operad**. So the single structural fact "$T$ is cartesian" unlocks the whole operadic machinery uniformly: classical operads come from $T = (-)^{\ast}$ on $\mathbf{Set}$, classical categories from $T = \mathrm{id}$ on $\mathbf{Set}$, $fc$-multicategories from the free-category monad on graphs, and globular operads from *this* $T$. The point of singling out cartesianness is that it is the one hypothesis these wildly different examples share.

There is also a slick description of the *operations* of $T$ that the categorical viewpoint makes transparent: the elements of $T1$ are the operations of the monad, the elements of $T(T1)$ are the formal composites of operations, and $\mu_1 : T(T1) \to T1$ tells you the actual composite. For this $T$, "operations" are pasting diagrams and "$\mu$" is the operation of pasting a pasting-diagram-of-pasting-diagrams into one pasting diagram — the globular analogue of concatenating a list of words into a single word.

---

# Relate to Other Fields / Compression

The monad $T$ is the globular member of a family of "free-algebraic-structure" monads, all sharing the cartesian property, and recognizing the family is the most compressive way to hold it in memory. The prototypes live on $\mathbf{Set}$. The **free-monoid monad** $(-)^{\ast}$, sending a set $A$ to the set $A^{\ast}$ of finite words, is cartesian; its $T$-operads are the classical (non-symmetric) **operads**, and its algebras are monoids. The **identity monad** on $\mathbf{Set}$ is trivially cartesian; its $T$-operads are ordinary small **categories** (one-object, this is a monoid). Moving to directed graphs, the **free-category monad** $fc$ is cartesian; its $T$-multicategories are the $fc$-multicategories that subsume bicategories and double categories. Our $T$ is the same idea one rung up: it lives on globular sets, and its operations are pasting diagrams instead of words or paths.

**True name:** *the free-strict-$\omega$-category monad is "the free-monoid monad, iterated through every dimension by the recursion $\mathrm{pd}(m+1) = \mathrm{pd}(m)^{\ast}$."* This is the operational characterisation: whenever you need to know what $T$ does in dimension $m+1$, you reach for "a finite list of dimension-$m$ data", and whenever you need to know why $T$ is cartesian, you reach for "the free-monoid monad is cartesian and lists-of-lists pull back". You almost never need the abstract monadicity statement; you need the list recursion.

The compression to free algebras over an arbitrary cartesian theory is the deepest one. Any finitary algebraic theory whose operations are "tree-like" (no genuine symmetry or duplication of variables) generates a cartesian monad, and a cartesian monad is the exact input to the generalized-operad construction. So $T$ is not special; it is one coordinate of a general dictionary "cartesian monad $\rightsquigarrow$ theory of higher structures of a given shape". The Batanin–Leinster definition is the assertion that the right shape for $\omega$-categories is the globular one, encoded by this $T$.

---

# Examples / Corollaries

**Is an instance — $T1 = \mathrm{pd}$, the pasting diagrams.** Applying $T$ to the terminal globular set $1$ yields the globular set of pasting diagrams. In dimension $0$ there is a single pasting diagram, the point. In dimension $1$ the pasting diagrams are the "string of $k$ arrows" shapes $\bullet \to \bullet \to \cdots \to \bullet$, one for each $k \geq 0$ (the case $k=0$ being a single degenerate point, an identity), so $\mathrm{pd}(1)$ is in bijection with $\mathbb{N}$. In dimension $2$ the pasting diagrams are the various ways of stacking and side-pasting $2$-cells over an underlying string of $1$-cells. This is the canonical example to keep in mind: $T$ is "the machine whose output shapes are pasting diagrams."

**Is an instance — $T$ applied to a parallel pair.** Let $X$ be the globular set with two $0$-cells $a, b$, two parallel $1$-cells $f, g : a \to b$, and nothing higher. Then $(TX)(1)$ consists of all formal composable strings of the $1$-cells $f$ and $g$ — but $f$ and $g$ are not composable (both go $a \to b$), so the only $1$-cells of $TX$ are $f$, $g$, and the formal identities $1_a, 1_b$; while $(TX)(2)$ adds the formal whiskerings and the identity $2$-cells but no genuine new $2$-cells, since $X$ has none. The labelled-pasting-diagram description makes this immediate: a $2$-cell of $TX$ is a pasting diagram of dimension $2$ with cells labelled by cells of $X$, and $X$ supplies no $2$-cell labels.

**Is an instance — the cartesian square that defines fibres.** Because $T$ is cartesian, for any globular set $X$ the square
$$
\begin{array}{ccc}
TX & \to & T1\\
\downarrow & & \downarrow\\
X & \to & 1
\end{array}
$$
exhibits $TX$ as fibred over $T1 = \mathrm{pd}$: the fibre over a pasting diagram $\pi$ is the set of labellings of $\pi$ by cells of $X$. This corollary is exactly the structural fact the [[Def - Globular Operad|globular operad]] definition exploits.

**Is NOT an instance — the free-strict-$\omega$-category monad is not the free-*symmetric* monoidal monad.** A common slip is to picture $T$'s operations as carrying symmetric-group actions, as classical symmetric operads do. They do not. The pasting diagrams have *no* symmetry: there is no permutation acting on the constituent cells of $\pi$, because globular composition is inherently ordered (you paste along oriented boundaries). This is exactly why globular operads are "plain" (non-symmetric) $T$-operads, and it is the structural reason the resulting $\omega$-categories are directed rather than symmetric-monoidal-flavoured.

**Is NOT an instance — a non-cartesian monad.** The free *commutative* monoid monad on $\mathbf{Set}$ (sending $A$ to finite multisets over $A$) is *not* cartesian: its multiplication squares fail to be pullbacks because forgetting order loses the information a pullback would need to reconstruct. Consequently there is no good theory of "commutative-monoid operads" by this route. The contrast sharpens why $T$ being cartesian is a real and useful theorem, not a formality — most naturally occurring monads fail it.

**Calibration check.** Verify that $\mathrm{pd}(1) \cong \mathbb{N}$ by counting "string of $k$ composable arrows" shapes, and that the boundary $\partial : \mathrm{pd}(2) \to \mathrm{pd}(1)$ sends a $2$-dimensional pasting diagram to the underlying $1$-dimensional string of its source/target $1$-cells. Then confirm that a $T$-algebra structure on a globular set $X$ — a map $TX \to X$ over $T1$ satisfying the monad-algebra laws — is exactly a choice of composite for every labelled pasting diagram, associatively and unitally: that is the definition of a **strict $\omega$-category**. If you can also state in one sentence why cartesianness of $T$ is needed to define globular operads ("so that the slice over $T1$ has an associative substitution product"), you have the definition.

---

# Unlocked by This

> [!tip] Globular Operad *(from this chapter)*
> A **globular operad** is precisely a **generalized operad** for this monad $T$ — a globular set $P$ with a cartesian map $P \to T1$ and operad structure. The cartesianness of $T$ proved here is the hypothesis that makes that definition coherent. See [[Def - Globular Operad]].

> [!tip] The Batanin–Leinster Operad and Weak ω-Categories *(from this chapter)*
> Replacing the terminal operad $1$ over $T1$ by the initial *contractible* operad $L$ over $T1$ turns "strict composite of every labelled pasting diagram" into "a coherent system of weak composites and coherence cells". A **weak ω-category** is then an $L$-algebra. This monad $T$ is the substrate on which $L$ is grown; see [[Def - Weak ω-Category and Weak n-Category (Batanin-Leinster)]].

> [!tip] The Cartesian-Monad Recipe for Higher Structures *(from Higher Operads)*
> The pattern "cartesian monad $T$ on a presheaf category $\rightsquigarrow$ theory of $T$-shaped higher categories" is uniform. **Batanin's original definition** of weak $\omega$-category and the later refinements (with a **system of compositions** and a **coherence**) are all variations on choosing the operad over this same $T1$. The globular $T$ is the canonical input; cubical and opetopic analogues swap it for the free strict $n$-tuple-category monad or the slice construction.
