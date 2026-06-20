---
type: definition
subject: higher-categories
prereqs:
  - "Def - Cartesian Monad"
  - "Def - Monad and Comonad"
  - "Def - Pullback and Pushout"
  - "Def - Category"
tags: [category-theory, higher-categories, foundations]
---

# Notation

Throughout, $\mathcal{E}$ is a category with [[Def - Pullback and Pushout|pullbacks]] and a terminal object $1$, and $(T, \eta, \mu)$ is a [[Def - Cartesian Monad|cartesian monad]] on $\mathcal{E}$. A **$T$-multicategory** is also called a **generalized multicategory** or a **$(\mathcal{E}, T)$-multicategory**. Its data are an object-of-objects $C_0 \in \mathcal{E}$ and an object-of-arrows $C_1 \in \mathcal{E}$, with structure maps $\mathrm{dom} : C_1 \to T C_0$ (domain/source), $\mathrm{cod} : C_1 \to C_0$ (codomain/target), $\mathrm{ids} : C_0 \to C_1$ (identities), and $\mathrm{comp}$ (composition). We write $A \times_C B$ for a pullback. The full symbol registry is on the parent page [[Higher Categories — Generalized Operads via Cartesian Monads]].

---

# Axiom Motivation

The cleanest way to arrive at this definition is to write down what a small [[Def - Category|category]] *is* using only objects, arrows, and structure maps, and then change exactly one thing. A small category consists of a set $C_0$ of objects, a set $C_1$ of arrows, source and target maps $\mathrm{dom}, \mathrm{cod} : C_1 \to C_0$, an identity map $\mathrm{ids} : C_0 \to C_1$, and a composition $\mathrm{comp}$ defined on the set of *composable pairs* — the [[Def - Pullback and Pushout|pullback]] $C_1 \times_{C_0} C_1 = \{(g, f) : \mathrm{dom}(g) = \mathrm{cod}(f)\}$ — subject to associativity and unitality. Everything about a category is in these maps and these two laws.

Now make the one change. We want arrows whose *source* is not a single object but a structured collection of objects: a finite list $(a_1, \dots, a_n)$, a tree, a pasting diagram. The structured collections of objects of $C_0$ are exactly the elements of $T C_0$ for the monad $T$ that "forms such collections". So we keep $\mathrm{cod} : C_1 \to C_0$ (an arrow still has a single target) but replace $\mathrm{dom} : C_1 \to C_0$ by $\mathrm{dom} : C_1 \to T C_0$. That is the entire conceptual move; the rest of the definition is forced by demanding that identities and composition still make sense.

Consider what composition must now do. In a category you compose $g$ after $f$ when the single object $\mathrm{cod}(f)$ equals the single object $\mathrm{dom}(g)$. In a $T$-multicategory an arrow $\theta$ with $\mathrm{dom}(\theta) = (a_1, \dots, a_n) \in T C_0$ should be composable with a *family* of arrows $\theta_1, \dots, \theta_n$, one feeding each input $a_i$. A family of arrows is an element of $T C_1$ (a $T$-shape of arrows), and the matching condition is that the *targets* of the family agree with the *inputs* of $\theta$ — that is, $T(\mathrm{cod})$ applied to the family equals $\mathrm{dom}(\theta)$. So composable configurations are the pullback
$$C_1 \times_{T C_0} T C_1 \;=\; \{(\theta, \Theta) : \mathrm{dom}(\theta) = T(\mathrm{cod})(\Theta)\},$$
and $\mathrm{comp}$ is a map out of this pullback into $C_1$. **This is exactly where cartesianness is used.** For the pullback $C_1 \times_{T C_0} T C_1$ to support an associative grafting — for "graft, then graft again" to equal "graft the regrafted" — the monad must respect these pullbacks, and that respect is the content of [[Def - Cartesian Monad|cartesianness]]. Drop cartesianness and the composition law has no well-defined associativity; the iterated grafting depends on how you parenthesize.

What breaks if we drop the **identity** map? Then there is no notion of the "do-nothing" arrow on an object, and the unit laws have nothing to assert; the structure degenerates to a $T$-graph (the data without identities or composition), which is genuinely weaker — it is the underlying signature, not a multicategory. What breaks if we drop **associativity**? Then grafting a tall stack of configurations is ambiguous, and the structure fails to model anything composable; for $T = (-)^{*}$ this is exactly the failure of operadic substitution to be unambiguous. What breaks if we drop **unitality**? Then the identities, even if present, do not act as identities, and one cannot recover ordinary categories (where the unit laws $f \circ \mathrm{id} = f = \mathrm{id} \circ f$ are non-negotiable) as the $T = \mathrm{id}$ case. Each axiom is the generalization of an axiom that is already indispensable for $T = \mathrm{id}$; the framework simply carries them along with $T$ woven in.

Could a reader invent this? Yes: write a category as structure maps over a composable-pairs pullback, replace "single-object domain" by "$T$-shape domain", and ask what the composition pullback and the laws must become. Cartesianness is then not an extra axiom on the multicategory but the precondition on $T$ that makes the resulting definition coherent — which is why §1 comes before §2.

---

# The Definition

Let $(T, \eta, \mu)$ be a [[Def - Cartesian Monad|cartesian monad]] on a category $\mathcal{E}$ with pullbacks.

A **$T$-multicategory** $C$ consists of:

- an object $C_0 \in \mathcal{E}$ (the **object-of-objects**),
- an object $C_1 \in \mathcal{E}$ (the **object-of-arrows**),
- a morphism $\mathrm{dom} : C_1 \to T C_0$ (the **domain**),
- a morphism $\mathrm{cod} : C_1 \to C_0$ (the **codomain**),
- a morphism $\mathrm{ids} : C_0 \to C_1$ (the **identities**),
- a morphism $\mathrm{comp} : C_1 \times_{T C_0} T C_1 \to C_1$ (the **composition**), where the pullback is of $\mathrm{dom} : C_1 \to T C_0$ against $T(\mathrm{cod}) \circ (\text{flatten}) : T C_1 \to T C_0$,

subject to source/target compatibility, **associativity**, and **left and right unitality**. In span-and-monoid form (below) these axioms are the standard monoid laws; spelled out on components, composition of a tower of configurations is independent of the order of grafting (associativity), and grafting the identity configurations on either side returns the original arrow (unitality).

A **$T$-multicategory** with $C_0 = 1$ (terminal) is a **$T$-operad**; see [[Def - Generalized Operad]].

A **morphism of $T$-multicategories** $C \to C'$ is a pair of maps $f_0 : C_0 \to C_0'$, $f_1 : C_1 \to C_1'$ commuting with all four structure maps (so $\mathrm{dom}' \circ f_1 = T f_0 \circ \mathrm{dom}$, $\mathrm{cod}' \circ f_1 = f_0 \circ \mathrm{cod}$, and similarly for identities and composition). These form the category $(\mathcal{E}, T)\text{-}\mathbf{Multicat}$.

---

# Categorical / Structural Definition

The structural definition is the slogan: **a $T$-multicategory is a monoid in the bicategory $\mathrm{Span}_T(\mathcal{E})$ of $T$-spans.**

Unpack it in stages. First, ordinary [[Def - Pullback and Pushout|spans]]. A span from $A$ to $B$ in $\mathcal{E}$ is a diagram $A \xleftarrow{\;p\;} S \xrightarrow{\;q\;} B$; spans compose by pullback, $(A \leftarrow S \to B)$ then $(B \leftarrow S' \to C)$ giving $A \leftarrow S \times_B S' \to C$. This makes $\mathrm{Span}(\mathcal{E})$ a bicategory whose objects are those of $\mathcal{E}$, whose 1-cells are spans, and whose 2-cells are maps of spans. **Burroni's observation** is that a [[Def - Category|category internal to $\mathcal{E}$]] is exactly a *monad in $\mathrm{Span}(\mathcal{E})$*: an object $C_0$, an endo-span $C_0 \xleftarrow{\mathrm{dom}} C_1 \xrightarrow{\mathrm{cod}} C_0$, a unit 2-cell $\mathrm{ids}$ (identities), and a multiplication 2-cell $\mathrm{comp}$ (composition) over the composable-pairs pullback, satisfying the monad laws (which are exactly associativity and unitality).

Now make the spans **$T$-shaped**. A **$T$-span** from $A$ to $B$ is a diagram $T A \xleftarrow{\;p\;} S \xrightarrow{\;q\;} B$ — the left leg lands in $T A$, not $A$. These compose using the multiplication $\mu$ of the monad together with pullbacks, and *cartesianness of $T$ is precisely what makes this composition associative and unital*, so that $\mathrm{Span}_T(\mathcal{E})$ is a genuine bicategory. A **monoid** (= monad) in $\mathrm{Span}_T(\mathcal{E})$ on the object $C_0$ is then an endo-$T$-span $T C_0 \xleftarrow{\mathrm{dom}} C_1 \xrightarrow{\mathrm{cod}} C_0$ with a unit and a multiplication — which is exactly the data and axioms of a $T$-multicategory above.

This is not a reformulation for its own sake. It reduces every structural proof to a monoid calculation: associativity of generalized composition is *the* associativity axiom of a monoid, proved once in the span bicategory and inherited by every $T$. It also exhibits the whole framework as Burroni's "category = monad in spans" with the single edit "$\mathrm{Span} \rightsquigarrow \mathrm{Span}_T$", which is why $T = \mathrm{id}$ recovers internal categories on the nose: $\mathrm{Span}_{\mathrm{id}} = \mathrm{Span}$.

---

# Relate to Other Fields / Compression

A $T$-multicategory is, in one phrase, *a category whose arrows have $T$-shaped sources*. This compresses a long list of structures into one parameterized definition. In computer science the same shape appears as a **multi-sorted algebraic signature** with structured arities: the objects are sorts, the arrows are operation symbols, and the $T$-shape of the domain is the arity (a list of input sorts for $T = (-)^{*}$). In the theory of [[Def - Pullback and Pushout|polynomial functors]], a $T$-multicategory for a polynomial monad $T$ is a coloured collection of polynomial operations closed under substitution. In differential and combinatorial settings, the tree-shaped arities give the **dendroidal** and operadic structures used to model homotopy-coherent algebra.

**True name:** *a $T$-multicategory is a monoid in $T$-spans* — equivalently a monad in the bicategory $\mathrm{Span}_T(\mathcal{E})$. When you must verify associativity or unitality, do not push pullbacks around by hand; invoke the monoid axioms in the span bicategory, where they hold for formal reasons. When you must *identify* a given structure as a $T$-multicategory, read off "what is the domain of an arrow allowed to be?" — a single object means $T = \mathrm{id}$, a list means $T = (-)^{*}$, a tree means the free-multicategory monad, a pasting diagram means $\mathbb{T}$.

---

# Examples / Corollaries

**Is an instance — a small category ($T = \mathrm{id}$).** With $T$ the identity monad, $T C_0 = C_0$, so $\mathrm{dom} : C_1 \to C_0$ is an ordinary source map, the composable pairs $C_1 \times_{C_0} C_1$ are the ordinary composable pairs, and the axioms are exactly associativity and unitality. A $\mathrm{id}$-multicategory in $\mathbf{Set}$ is a small category; a $\mathrm{id}$-multicategory in a general $\mathcal{E}$ is a category internal to $\mathcal{E}$. This is the base case that anchors all intuition.

**Is an instance — a classical [[Def - Multicategory|multicategory]] ($\mathcal{E} = \mathbf{Set}$, $T = (-)^{*}$).** Here $T C_0 = C_0^{*}$ is the set of finite lists of objects, so an arrow $\theta \in C_1$ has $\mathrm{dom}(\theta) = (a_1, \dots, a_n)$ a list of objects and $\mathrm{cod}(\theta) = b$ a single object — a multimap $(a_1, \dots, a_n) \to b$. The composition pullback graft a list of multimaps into one, exactly the classical operadic composition. The associativity and unitality axioms become the classical multicategory axioms. A [[Def - Multicategory|multicategory]] is also called a **coloured [[Def - Operad|operad]]**; the colours are the objects $C_0$.

**Is an instance — an $fc$-multicategory ($\mathcal{E} = \mathbf{Gph}$, $T = fc$).** Taking the free-category monad on directed graphs gives a structure with objects, vertical arrows, horizontal arrows, and 2-cells whose source is a *path* of horizontal arrows (the $fc$-shape) and whose target is a single horizontal arrow. These subsume bicategories, monoidal categories, double categories, and plain multicategories (HC5).

**Is NOT an instance — a "symmetric multicategory" via the multiset monad.** One might hope to get symmetric multicategories by using the free-commutative-monoid monad $M$, so that the domain of an arrow is an *unordered* multiset of objects. But $M$ is **not** [[Def - Cartesian Monad|cartesian]] (the symmetric quotient breaks the multiplication pullback), so $M$-spans do not form a bicategory and "$M$-multicategory" is not defined by this recipe. Symmetric multicategories exist, but they are *not* generalized multicategories for the multiset monad; they require the separate symmetric-sequences technology.

**Is NOT an instance — a mere $T$-graph.** A $T$-graph is the data $(C_0, C_1, \mathrm{dom} : C_1 \to T C_0, \mathrm{cod} : C_1 \to C_0)$ *without* identities or composition. It is the underlying signature of a $T$-multicategory but is not itself one — there is nothing to compose. The forgetful functor from $T$-multicategories to $T$-graphs has a left adjoint, the free $T$-multicategory (see [[Thm - The Free Multicategory Monad]]).

**Calibration check.** With $T = \mathrm{id}$, verify that the composition pullback $C_1 \times_{C_0} C_1$ is the set of composable pairs and that associativity reduces to the usual category axiom. With $T = (-)^{*}$, verify that an arrow's domain is a finite list of objects and write out the composition of a binary multimap with two unary ones. If you can state in one sentence why cartesianness of $T$ is what makes the composition pullback associative, you have understood the definition.

---

# Unlocked by This

> [!tip] T-Operads and Algebras *(from this chapter)*
> Restricting to $C_0 = 1$ gives a **[[Def - Generalized Operad|$T$-operad]]**, the single-sorted case, whose operations are classified by $T1$. A $T$-operad acts on objects of $\mathcal{E}$, and the structures it acts on are its **[[Def - Algebra for a Generalized Operad|algebras]]** — the §3 payoff, recovering monoids, operad-algebras, and weak higher categories.

> [!tip] Opetopes via Iterated Slicing *(from Higher Category Theory)*
> The free $T$-multicategory construction can be applied to the *terminal* $T$-operad and then iterated. Each iteration produces a new generalized multicategory whose arrows are the pasting diagrams of the previous one; the cells obtained this way are the **opetopes**, and presheaves on them are **opetopic sets** — the Baez–Dolan / Hermida–Makkai–Power route to weak $n$-categories (HC6).

> [!tip] Enriched and Internal Generalizations *(from Categorical Algebra)*
> Varying the ambient $\mathcal{E}$ (to a topos, a slice category, or an enriched setting) while keeping $T$ cartesian yields enriched and internal generalized multicategories, the setting in which topological operads (whose algebras include loop spaces, via **May's recognition principle**) and dg-operads (whose algebras include $A_\infty$-algebras) live.
