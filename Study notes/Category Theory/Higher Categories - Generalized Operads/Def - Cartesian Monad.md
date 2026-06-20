---
type: definition
subject: higher-categories
prereqs:
  - "Def - Monad and Comonad"
  - "Def - Pullback and Pushout"
  - "Def - Natural Transformation"
  - "Def - Functor"
tags: [category-theory, higher-categories, foundations]
---

# Notation

Throughout, $\mathcal{E}$ is a category with [[Def - Pullback and Pushout|pullbacks]], and $(T, \eta, \mu)$ is a [[Def - Monad and Comonad|monad]] on $\mathcal{E}$: an endofunctor $T : \mathcal{E} \to \mathcal{E}$, a unit natural transformation $\eta : 1_{\mathcal{E}} \Rightarrow T$ with components $\eta_A : A \to TA$, and a multiplication $\mu : T^2 \Rightarrow T$ with components $\mu_A : T^2 A \to TA$, satisfying the associativity law $\mu \circ T\mu = \mu \circ \mu T$ and the unit laws $\mu \circ T\eta = 1_T = \mu \circ \eta T$. We write $A \times_C B$ for the pullback of a cospan $A \to C \leftarrow B$, and $1$ for a terminal object of $\mathcal{E}$ when one exists. A square is a **pullback square** when it exhibits its top-left corner as the pullback of the cospan formed by its other three corners. The full symbol registry is on the parent page [[Higher Categories — Generalized Operads via Cartesian Monads]].

---

# Axiom Motivation

The reason this definition exists is that we want to build categories whose arrows have not a single object as their source but a *$T$-shaped collection* of objects — a finite list, a tree, a pasting diagram. For that to work, three things must go right, and "cartesian" is exactly the package that makes all three go right at once. The honest way to discover the definition is to try to define a generalized category and watch which properties of $T$ you are forced to demand.

Recall first how composition works in an ordinary [[Def - Category|category]]. You can compose $g$ after $f$ only when $\mathrm{dom}(g) = \mathrm{cod}(f)$, and the set of composable pairs is the [[Def - Pullback and Pushout|pullback]] of $\mathrm{dom}$ against $\mathrm{cod}$. Now in a $T$-multicategory the source of an arrow lives in $T C_0$, not $C_0$, so the composable configurations are a pullback that involves $T$ applied to the object-of-arrows. To even *form* this pullback and have it behave — to know that "$T$ of a composable configuration" is again a composable configuration — we need $T$ to send pullbacks to pullbacks. **First requirement: $T$ preserves pullbacks.** Drop it, and the object $T C_1$ no longer relates to $C_1$ by the pullbacks that composition needs; the grafting of configurations becomes ill-defined because the shapes stop matching. This is not a convenience; without preservation of pullbacks the composition map has no domain to be defined on.

The second and third requirements concern the unit $\eta$ and multiplication $\mu$. A **cartesian natural transformation** $\alpha : F \Rightarrow G$ is one all of whose naturality squares
$$\begin{array}{ccc}
FA & \xrightarrow{\;Ff\;} & FB \\
{\scriptstyle \alpha_A}\big\downarrow & & \big\downarrow{\scriptstyle \alpha_B} \\
GA & \xrightarrow{\;Gf\;} & GB
\end{array}$$
are pullbacks, for every $f : A \to B$. Demanding this of $\eta$ and $\mu$ looks technical until you see what each square *is*. The unit $\eta_A : A \to TA$ embeds the "bare" objects among the $T$-shapes — the singleton list among all lists. Cartesianness of $\eta$ says that the bare objects sit inside $T$ as an *exact* sub-shape: an element of $TA$ is "really just an object of $A$" precisely along a pullback, with no extra identifications. Concretely, for $T = (-)^{*}$ the list monad, cartesianness of $\eta$ encodes that a list maps to a singleton list under $Tf$ if and only if it *was* a singleton, pulled back correctly — the singletons form a clean, full sub-family. **Drop cartesianness of $\eta$** and the identities of your $T$-multicategory stop being well-behaved: the identity arrow on an object would no longer be detectable as "the singleton configuration", and unit laws would fail to pin down identities uniquely.

Cartesianness of $\mu$ is the load-bearing one. The multiplication $\mu_A : T^2 A \to TA$ flattens a shape-of-shapes into a shape — a list of lists into a concatenated list, a tree of trees into a tree. Its naturality square being a pullback says that this flattening *loses no information about the constituent pieces*: from the flattened shape together with the abstract shape-of-shapes you can reconstruct exactly which pieces went where, as a pullback. **Drop cartesianness of $\mu$** and the substitution/grafting that defines operadic composition becomes ambiguous: two genuinely different ways of grafting could flatten to the same configuration, and the composition law would not be well-defined. This is exactly the failure for the free-commutative-monoid monad. There, $\mu$ concatenates *unordered* multisets, and a concatenated multiset $\{a, a, b\}$ can arise from $\{a\} \sqcup \{a, b\}$ or $\{a, a\} \sqcup \{b\}$ — the flattening forgets the partition, the square is not a pullback, and there is no clean operadic composition. The symmetric quotient is precisely what breaks cartesianness, which is why this framework delivers *non-symmetric* operads.

Could a reader invent the definition? Yes, by exactly this route: try to define generalized composition, discover you need $T$ to respect the pullbacks of composable configurations (preservation of pullbacks), discover you need identities to be detectable (cartesian $\eta$), and discover you need grafting to be reconstructible (cartesian $\mu$). The three conditions are not a wish-list; they are the three places where the construction would otherwise leak. There is no useful *weakening* — drop any one and the §2 definition of a $T$-multicategory fails to type-check. The natural *strengthening* is to add finiteness or accessibility hypotheses on $T$ (so that free $T$-multicategories exist), but those are orthogonal regularity conditions, not part of "cartesian" itself.

---

# The Definition

Let $\mathcal{E}$ be a category with [[Def - Pullback and Pushout|pullbacks]] and $(T, \eta, \mu)$ a [[Def - Monad and Comonad|monad]] on $\mathcal{E}$.

A natural transformation $\alpha : F \Rightarrow G$ between functors $\mathcal{E} \to \mathcal{E}$ is **cartesian** if for every morphism $f : A \to B$ in $\mathcal{E}$ the naturality square
$$\begin{array}{ccc}
FA & \xrightarrow{\;Ff\;} & FB \\
{\scriptstyle \alpha_A}\big\downarrow & & \big\downarrow{\scriptstyle \alpha_B} \\
GA & \xrightarrow{\;Gf\;} & GB
\end{array}$$
is a pullback. (Equivalently: $\alpha$ is cartesian if and only if it is a cartesian morphism in the functor category for the codomain fibration, i.e. each $\alpha_A$ is the pullback of $\alpha_B$ along $Gf$.)

The monad $(T, \eta, \mu)$ is a **cartesian monad** if:

1. **$T$ preserves pullbacks** — for every pullback square in $\mathcal{E}$, its image under $T$ is again a pullback square;
2. **$\eta$ is cartesian** — every naturality square of $\eta : 1_{\mathcal{E}} \Rightarrow T$ is a pullback;
3. **$\mu$ is cartesian** — every naturality square of $\mu : T^2 \Rightarrow T$ is a pullback.

An equivalent and frequently convenient packaging: $(T, \eta, \mu)$ is cartesian if and only if $T$ preserves pullbacks **and** $T$ preserves the terminal object up to the right comparison maps in a way making $\eta, \mu$ cartesian — but the three-condition form above is the working definition.

---

# Categorical / Structural Definition

There is a one-line structural reformulation that explains the name. A monad on $\mathcal{E}$ is, by the slogan, a [[Def - Monoid in a Monoidal Category|monoid]] in the strict monoidal category $([\mathcal{E}, \mathcal{E}], \circ, 1_{\mathcal{E}})$ of endofunctors of $\mathcal{E}$ (see [[Def - Monad and Comonad#Categorical / Structural Definition]]). Inside the larger 2-category $\mathbf{Cat}$, there is a notion of a **cartesian object** and a **cartesian morphism**: an endofunctor is "cartesian" when it preserves pullbacks, and a 2-cell (natural transformation) is "cartesian" when its components form pullback squares. A cartesian monad is then exactly a **monoid in the sub-monoidal-category of pullback-preserving endofunctors and cartesian natural transformations** — a monoid object that lives entirely inside the cartesian part of $[\mathcal{E}, \mathcal{E}]$.

The deeper structural statement is the **Carboni–Johnstone characterization**. When $\mathcal{E}$ is a presheaf category (or more generally a suitable topos), a finitary monad $T$ is cartesian if and only if its endofunctor is **familially representable**: there is a small family of objects $(C_i)_{i \in I}$ with a natural isomorphism
$$TX \;\cong\; \coprod_{i \in I} \mathcal{E}(C_i, X).$$
Read this as "$T X$ is the set of *operations*, where an operation is a choice of arity $i \in I$ together with a way $C_i \to X$ of filling that arity from $X$". The objects $C_i$ are the **arities** of $T$, and cartesianness is precisely the rigidity of this family — that arities have no internal symmetry collapsing them. This is the structural reason the free-monoid monad is cartesian (arities = finite ordinals, $C_n = \{1, \dots, n\}$, no symmetry) and the free-commutative-monoid monad is not (the would-be arities are quotiented by $S_n$).

---

# Relate to Other Fields / Compression

Cartesianness is the categorical incarnation of a single idea that appears whenever one wants to *substitute* structured pieces into structured slots without losing track of which piece went where. In rewriting and in the theory of algebraic effects, the same condition is what guarantees that "plug a term into a context" is unambiguous and reconstructible. In the theory of [[Def - Pullback and Pushout|polynomial functors]] and dependent type theory, cartesian monads are precisely the *polynomial monads*: a polynomial functor is built from a span $I \leftarrow E \to B \to J$ by the pullback–pushforward–composition recipe, and the cartesianness of the resulting monad is automatic from the fibrewise construction. So a cartesian monad on a slice category $\mathbf{Set}/I$ is the same data as a polynomial monad on $I$-sorted operations, which is the same data as a (coloured, non-symmetric) operad's substitution.

**True name:** *a cartesian monad is a monad whose operations form a rigid, symmetry-free family of arities* — equivalently $TX \cong \coprod_i \mathcal{E}(C_i, X)$ with the $C_i$ having no collapsing automorphisms. When you want to decide cartesianness, do not draw pullback squares; ask "what are the arities, and does any symmetry quotient them?". If a symmetric group acts and is divided out, the monad is not cartesian; if the arities are ordered/rigid (lists, trees, pasting diagrams), it is.

---

# Examples / Corollaries

**Is an instance — the identity monad.** On any category $\mathcal{E}$ with pullbacks, the identity monad $T = 1_{\mathcal{E}}$, $\eta = \mu = \mathrm{id}$, is cartesian: the identity functor preserves all limits, and the naturality squares of the identity transformation are squares with two parallel identity edges, which are trivially pullbacks. This is the floor of the framework; its $T$-multicategories are ordinary internal [[Def - Category|categories]].

**Is an instance — the free-monoid (list) monad.** On $\mathbf{Set}$, $T X = X^{*} = \coprod_{n \geq 0} X^n$, with $\eta_X(x) = (x)$ the singleton list and $\mu_X$ the concatenation of a list of lists. This is cartesian. Its arities are the finite ordinals $\{1, \dots, n\}$ with no symmetry, so by the familial-representability picture it is familially representable, hence cartesian. Concretely, the multiplication square is a pullback because from a concatenated list together with the abstract list-of-lists shape you can recover exactly which sublist each entry came from. Its $T$-operads are the classical **non-symmetric [[Def - Operad|operads]]** (see [[Def - Generalized Operad]]).

**Is an instance — the free-category monad on directed graphs.** On the category $\mathbf{Gph}$ of directed graphs, $fc$ sends a graph to the graph with the same vertices and *paths* as edges; $\eta$ inserts length-one paths, $\mu$ concatenates paths-of-paths. It is cartesian, and its $T$-multicategories are the [[Def - fc-Multicategory|$fc$-multicategories]] of HC5. The arities here are the finite linear graphs $\bullet \to \bullet \to \cdots \to \bullet$, again rigid and symmetry-free.

**Is NOT an instance — the free-commutative-monoid (multiset) monad.** On $\mathbf{Set}$, $M X = \coprod_n X^n / S_n$, the finite multisets over $X$. This is **not cartesian**. Take the unique map $f : \{a, b\} \to \{*\}$. The multiset $\{*, *\} \in M\{*\}$ has, in the pullback $\{a,b\}^2/\text{(naive)}$ sense, the preimages it ought to have under $Mf$; but tracing the multiplication square shows that the flattening $\mu$ of $\{\{a\}, \{a, b\}\}$ and of $\{\{a, a\}, \{b\}\}$ to multisets cannot be distinguished by their image, so the relevant naturality square fails the pullback universal property — two distinct elements of the would-be pullback map to one. The culprit is the quotient by $S_n$, which identifies orderings that the pullback keeps separate. This is why **symmetric** operads do not arise as $M$-operads and require the separate symmetric-sequences machinery.

**Is NOT an instance — the powerset monad.** On $\mathbf{Set}$, the [[Def - Algebra for a Monad|powerset]] monad $P X = \{S : S \subseteq X\}$ with $\eta_X(x) = \{x\}$ and $\mu_X$ = union is not cartesian: $P$ does not preserve pullbacks (the image of a pullback under "take all subsets" overcounts), and the union multiplication merges subsets irreversibly, breaking the pullback condition on $\mu$. Its algebras (complete sup-lattices) form a perfectly good Eilenberg–Moore category, but the monad sits outside this chapter's framework.

**Calibration check.** Verify that the identity monad's $\eta$ and $\mu$ squares are pullbacks (they have parallel identity edges). Verify that for the list monad, the unit square for a map $f : A \to B$ — relating singleton lists in $A^{*}$ and $B^{*}$ — is a pullback, i.e. a list $\ell \in A^{*}$ maps to a singleton in $B^{*}$ exactly when $\ell$ is itself a singleton. If you can also state in one sentence *why* the multiset monad fails (the $S_n$-quotient forgets the partition that the pullback remembers), you have understood the definition.

---

# Unlocked by This

> [!tip] T-Multicategories and T-Operads *(from this chapter)*
> A cartesian monad is exactly the input the next two definitions need. With $T$ cartesian, a **[[Def - Generalized Multicategory|$T$-multicategory]]** is a monoid in $T$-spans, and a **[[Def - Generalized Operad|$T$-operad]]** is the one-object case. Cartesianness is the licence that makes the composable-configuration pullbacks and the grafting law well-defined.

> [!tip] The Free Strict ω-Category Monad and Globular Operads *(from Higher Category Theory)*
> The fact that powers the entire Batanin–Leinster definition of weak $\omega$-categories is that the **free strict ω-category monad** on globular sets is cartesian. Its arities are the **globular pasting diagrams**, and because they are rigid (no symmetry), the monad is cartesian, so **globular operads** exist as $\mathbb{T}$-operads. Without this single cartesianness fact there would be no algebraic definition of a weak higher category of this kind (HC7).

> [!tip] Polynomial Functors and Polynomial Monads *(from Categorical Logic)*
> Cartesian monads on slice categories are exactly the **polynomial monads**, built from a span $I \leftarrow E \to B \to J$ by pullback, dependent product, and composition. This identifies the chapter's machinery with the theory of dependent polynomials and with $W$-types in type theory, where the initial algebra of a polynomial functor is the type of well-founded trees of a given signature.
