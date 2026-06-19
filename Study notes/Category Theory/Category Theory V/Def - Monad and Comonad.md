---
type: definition
subject: category-theory
prereqs:
  - "Def - Functor"
  - "Def - Natural Transformation"
  - "Def - Functor Category"
  - "Def - Adjunction"
tags: [category-theory, foundations]
---

# Notation

Throughout, $\mathcal{C}$ is a [[Def - Category|category]] and $T : \mathcal{C} \to \mathcal{C}$ is an [[Def - Functor|endofunctor]] (a functor from $\mathcal{C}$ to itself). We write $T^2 = T \circ T$ and $T^3 = T \circ T \circ T$, $1_{\mathcal{C}}$ for the identity endofunctor, and $1_T$ for the identity [[Def - Natural Transformation|natural transformation]] on $T$. The unit is $\eta : 1_{\mathcal{C}} \Rightarrow T$, with component $\eta_A : A \to TA$; the multiplication is $\mu : T^2 \Rightarrow T$, with component $\mu_A : T^2A \to TA$. For a comonad we use the counit $\varepsilon : G \Rightarrow 1_{\mathcal{C}}$ (component $\varepsilon_A : GA \to A$) and the comultiplication $\delta : G \Rightarrow G^2$ (component $\delta_A : GA \to G^2A$). The **whiskerings** $T\mu$ and $\mu T$ are the two ways of composing $\mu$ with $T$: $T\mu : T^3 \Rightarrow T^2$ has component $T(\mu_A)$, and $\mu T : T^3 \Rightarrow T^2$ has component $\mu_{TA}$. These are different transformations. The full symbol registry is on [[Category Theory V — Monads, Algebras, and Monoidal Categories]].

This is a compound page: it defines two interlocking notions — the **monad** and its formal dual the **comonad** — because they are introduced together, the comonad is obtained from the monad by reversing every arrow, and neither is fully understood without seeing the duality.

---

# Axiom Motivation

The right way to discover the definition of a monad is to ask what survives of an [[Def - Adjunction|adjunction]] when you can only see one of the two categories. Suppose $F \dashv U$ with $F : \mathcal{C} \to \mathcal{D}$ and $U : \mathcal{D} \to \mathcal{C}$ — for concreteness, $U : \mathbf{Grp} \to \mathbf{Set}$ forgets group structure and $F$ forms the free group. Stand inside $\mathbf{Set}$ and pretend $\mathbf{Grp}$ does not exist. What structure on $\mathbf{Set}$ remains visible? You can still see the composite $T = UF$, which sends a set $A$ to the underlying set of the free group on $A$ — a set of formal words. You can see the unit $\eta_A : A \to TA$ of the adjunction, which includes each generator as a length-one word. And although the counit $\varepsilon_A : FUA \to A$ lives in $\mathbf{Grp}$ and is invisible from $\mathbf{Set}$, one whiskered shadow of it survives: $\mu = U\varepsilon F : T^2 \Rightarrow T$, whose component $\mu_A : T^2 A \to TA$ takes a *word of words* and multiplies it out into a single word.

So from the base category we see exactly an endofunctor, a "unit" inserting generators, and a "multiplication" flattening nested formal expressions. The question is: what equations must this triple satisfy? They are forced by what flattening must do.

The **multiplication must be associative** in the sense that flattening a triply-nested expression the same way regardless of order. Given a word-of-words-of-words $w \in T^3 A$, there are two ways to reduce it to a word in $TA$: flatten the *inner* nesting first (apply $T\mu$, multiplying out each inner word-of-words, then $\mu$) or flatten the *outer* nesting first (apply $\mu T$, multiplying out the top level, then $\mu$). For "multiply out the formal expression" to be unambiguous, these must agree:
$$\mu \circ T\mu = \mu \circ \mu T \qquad (\text{as } T^3 \Rightarrow T).$$
Drop this and "evaluate the formal expression" depends on the order of evaluation — there is no well-defined notion of "the product of this nested word," and the would-be algebraic structure collapses. This is exactly the associativity that lets us write $a_1 a_2 a_3$ without brackets in any monoid; the monad axiom is that statement one level up.

The **unit must be neutral** for the multiplication. Take a word $w \in TA$. There are two ways to view it as a *word of words* and then flatten back: wrap each *letter* as a singleton word (apply $T\eta$, turning $w = a_1\cdots a_n$ into the word $(a_1)(a_2)\cdots(a_n)$ of singletons) or wrap the *whole word* as a single one-element word-of-words (apply $\eta T$, turning $w$ into the length-one word $(w)$). In both cases flattening must return $w$ unchanged:
$$\mu \circ T\eta = 1_T = \mu \circ \eta T.$$
Drop the left equation and inserting trivial nesting at the letter level changes the value; drop the right and wrapping the whole expression once changes it. Either failure means the "unit" is not a unit for the multiplication — it is the monad-level statement that $1 \cdot a = a = a \cdot 1$.

Could a reader invent this from scratch? Yes: demand that "an endofunctor of formal expressions, a way to insert generators, and a way to evaluate nested expressions" form a *consistent* algebra, and you are forced to exactly associativity and two-sided unitality. There is no useful weakening — without associativity evaluation is ambiguous; without unitality the inclusion of generators is not respected. And there is a precise *strengthening* that turns out to name the whole subject: these three axioms are *verbatim* the axioms of a [[Def - Monoid in a Monoidal Category|monoid]], with the tensor product taken to be functor composition. So the definition is not arbitrary — it is "monoid" transplanted into the [[Def - Functor Category|category of endofunctors]].

The **comonad** is the same definition read in a mirror. Reverse every arrow: the unit $\eta : 1 \Rightarrow T$ becomes a counit $\varepsilon : G \Rightarrow 1$ (now $GA$ maps *to* $A$), and the multiplication $\mu : T^2 \Rightarrow T$ becomes a comultiplication $\delta : G \Rightarrow G^2$ (now $GA$ maps *to* $G^2A$). The axioms reverse correspondingly. Where a monad packages "ways to build and evaluate structure" — free algebraic objects — a comonad packages "ways to observe and refine structure" — contexts, streams, and the descent data of geometry.

---

# The Definition

A **monad** on a category $\mathcal{C}$ is a triple $(T, \eta, \mu)$ consisting of:
- an endofunctor $T : \mathcal{C} \to \mathcal{C}$,
- a unit natural transformation $\eta : 1_{\mathcal{C}} \Rightarrow T$,
- a multiplication natural transformation $\mu : T^2 \Rightarrow T$,

such that the following diagrams of natural transformations commute, expressed as equations of the form $X \Rightarrow Y$:

**Associativity** ($T^3 \Rightarrow T$):
$$\mu \circ T\mu \;=\; \mu \circ \mu T.$$

**Left and right unitality** ($T \Rightarrow T$):
$$\mu \circ T\eta \;=\; 1_T \;=\; \mu \circ \eta T.$$

Equivalently, on components: for every object $A$, the square
$$\begin{array}{ccc}
T^3A & \xrightarrow{\;T(\mu_A)\;} & T^2A \\
{\scriptstyle \mu_{TA}}\big\downarrow & & \big\downarrow{\scriptstyle \mu_A} \\
T^2A & \xrightarrow{\;\;\mu_A\;\;} & TA
\end{array}$$
commutes, and the two composites $TA \xrightarrow{T(\eta_A)} T^2A \xrightarrow{\mu_A} TA$ and $TA \xrightarrow{\eta_{TA}} T^2A \xrightarrow{\mu_A} TA$ both equal $1_{TA}$.

A **comonad** on $\mathcal{C}$ is the formal dual: a triple $(G, \varepsilon, \delta)$ with an endofunctor $G : \mathcal{C} \to \mathcal{C}$, a counit $\varepsilon : G \Rightarrow 1_{\mathcal{C}}$, and a comultiplication $\delta : G \Rightarrow G^2$, satisfying **coassociativity** $G\delta \circ \delta = \delta G \circ \delta$ ($G \Rightarrow G^3$) and **counitality** $G\varepsilon \circ \delta = 1_G = \varepsilon G \circ \delta$ ($G \Rightarrow G$). A comonad on $\mathcal{C}$ is precisely a monad on $\mathcal{C}^{op}$.

---

# Categorical / Structural Definition

The structural definition is the slogan made precise: **a monad on $\mathcal{C}$ is a monoid in the strict [[Def - Monoidal Category|monoidal category]] $([\mathcal{C},\mathcal{C}], \circ, 1_{\mathcal{C}})$ of endofunctors of $\mathcal{C}$.**

Unpack this. The [[Def - Functor Category|functor category]] $[\mathcal{C},\mathcal{C}]$ has endofunctors of $\mathcal{C}$ as objects and natural transformations as morphisms. It carries a monoidal structure whose tensor product is *composition of functors*, $F \otimes G := F \circ G$, and whose unit object is the *identity endofunctor* $I := 1_{\mathcal{C}}$. Composition of functors is strictly associative — $F \circ (G \circ H) = (F \circ G) \circ H$ on the nose — and strictly unital, so this is a strict monoidal category (the associator and unitors are identities). A [[Def - Monoid in a Monoidal Category|monoid]] in a monoidal category $(\mathcal{V}, \otimes, I)$ is an object $M$ with a multiplication $m : M \otimes M \to M$ and a unit $e : I \to M$ satisfying associativity and unitality. Specializing: $M = T$ is an endofunctor, $m = \mu : T \circ T \Rightarrow T$ is the multiplication, $e = \eta : 1_{\mathcal{C}} \Rightarrow T$ is the unit, and the monoid axioms become exactly the monad axioms above. Dually, a comonad is a *comonoid* in $([\mathcal{C},\mathcal{C}], \circ, 1)$.

This is not a reformulation for its own sake. It tells you that the theory of monads is the theory of monoids relocated to a new world — see [[Def - Monoid in a Monoidal Category]] for the loop back, and §5.4 of the parent page — and it is why every construction for monoids (acting on objects, bimodules, tensor products) has a monad analogue.

---

# Relate to Other Fields / Compression

In functional programming a monad is the standard tool for sequencing computations that carry an effect: the endofunctor $T$ describes the effect ($\mathtt{Maybe}$ for possible failure, $\mathtt{List}$ for nondeterminism, $\mathtt{State}\,s$ for mutable state), the unit $\eta$ is the trivial effect-free computation (`return`), and the multiplication $\mu$ collapses a computation-of-a-computation into one (`join`, equivalently `bind`). The monad laws are precisely what guarantee that `do`-notation is unambiguous — they are the associativity and unitality of sequencing.

**True name:** a monad is a **monoid in endofunctors** — an associative, unital "multiplication" $\mu : T^2 \Rightarrow T$ together with a unit $\eta : 1 \Rightarrow T$. Operationally, when you meet $(T,\eta,\mu)$ you should not picture three commuting diagrams; you should picture an object you can multiply, with the product being "flatten the nested expression" and the unit being "insert a generator." Everything else follows from treating $T$ as a generalized monoid.

A second compression: a monad is a *one-object 2-categorical monad*, i.e. a [[Def - Monoid in a Monoidal Category|monoid]] in the endo-hom-category of a 2-category at the object $\mathcal{C}$ in $\mathbf{Cat}$. This is the viewpoint that generalizes monads to arbitrary bicategories and underlies the theory of formal monad theory.

---

# Examples / Corollaries

**Is an instance — the power-set monad $P$ on $\mathbf{Set}$.** $P(A)$ is the set of all subsets of $A$; on a function $f : A \to B$, $P(f)$ takes direct images. The unit $\eta_A : A \to P(A)$ is the singleton map $a \mapsto \{a\}$, and the multiplication $\mu_A : P(P(A)) \to P(A)$ is union, $\mathcal{S} \mapsto \bigcup_{S \in \mathcal{S}} S$. Associativity says a triply-nested family unions the same way regardless of grouping; unitality says unioning singletons, or wrapping a set as a one-element family and unioning, both return the original set. This monad comes from the adjunction whose left adjoint is "free sup-lattice"; its algebras are complete lattices (see [[Ex - The power-set monad]]).

**Is an instance — the free-monoid (list) monad.** $T A = A^* = \coprod_{n \geq 0} A^n$ is the set of finite words; $\eta_A$ sends $a$ to the one-letter word $(a)$; $\mu_A$ concatenates a word of words into a single word. This is the monad of the free–forgetful [[Def - Free-Forgetful Adjunction|adjunction]] $\mathbf{Set} \rightleftarrows \mathbf{Mon}$ (see [[Ex - The free monoid monad]]).

**Is an instance — the free-group monad $T = UF$.** $F : \mathbf{Set} \to \mathbf{Grp}$ is the [[Def - Free Group and Free Product|free group]] functor, $U$ the forgetful functor; $T A$ is the set of reduced words in the alphabet $A \cup A^{-1}$. The unit includes generators; the multiplication multiplies a word of words and re-reduces. Its algebras are exactly [[Def - Group|groups]] (see [[Ex - Algebras for the free-group monad are groups]]).

**Is an instance — the maybe monad $(-) + 1$.** $T A = A + \{*\}$ adjoins a fresh point; $\eta_A$ is the inclusion of $A$; $\mu_A : (A + 1) + 1 \to A + 1$ collapses the two adjoined points to one. Its Kleisli category is sets and partial functions. The same construction "adjoin a copy of a fixed object" works in any category with coproducts.

**Is NOT an instance — the squaring functor with the diagonal.** Let $T(A) = A \times A$ on $\mathbf{Set}$, with $\eta_A : A \to A \times A$ the diagonal $a \mapsto (a,a)$. There is *no* natural, associative, unital multiplication $\mu : T^2 \Rightarrow T$, i.e. $\mu_A : (A\times A)\times(A\times A) \to A \times A$: any natural candidate (e.g. project to two of the four coordinates) fails one of the two unit laws. So an endofunctor with a unit need not be a monad — the multiplication is the substantive datum.

**Is NOT an instance — a non-coassociative comultiplication.** Dually, an endofunctor with a counit need not be a comonad. If you equip $G(A) = A \times A$ with the obvious projection counit but a comultiplication that duplicates inconsistently, coassociativity fails, and the "ways to observe" do not refine coherently.

**Corollary — every adjunction yields a monad and a comonad.** By [[Thm - Every Adjunction Gives a Monad]], $F \dashv U$ gives the monad $UF$ on the domain of $F$ and, dually, the comonad $FU$ on the domain of $U$. Most monads in nature are produced this way rather than verified axiom-by-axiom.

**Calibration check.** Verify, for the power-set monad, that $\mu \circ T\eta = 1$ by unioning singletons; verify that $T\mu$ and $\mu T$ are genuinely different on a triply-nested set by writing out their components; and confirm that reversing all the arrows in the monad diagrams produces exactly the comonad axioms (so a comonad on $\mathcal{C}$ is a monad on $\mathcal{C}^{op}$).

---

# Unlocked by This

> [!tip] Algebras and the Eilenberg–Moore / Kleisli Categories *(from this chapter)*
> A monad is only half the story; its [[Def - Algebra for a Monad|algebras]] are the structured objects it describes, and the [[Def - Kleisli Category|Kleisli category]] is the category of its free algebras. These two constructions resolve the monad back into an adjunction.

> [!tip] The Probability Monad and Markov Categories *(from Categorical Probability)*
> The finitely-supported **distribution monad** $D$ and the measure-theoretic **Giry monad** are monads whose Kleisli morphisms are stochastic maps. Their Kleisli categories, equipped with copy-and-discard structure, are **Markov categories** — the categorical foundation of probability and a substrate for agent foundations.

> [!tip] Distributive Laws and the Bar Construction *(from Higher Algebra)*
> Two monads $S, T$ compose to a monad $TS$ exactly when there is a **distributive law** $ST \Rightarrow TS$; iterating the multiplication produces the **bar construction**, a simplicial object that computes derived functors and is the entry point to monadic cohomology and **derived category** machinery.
