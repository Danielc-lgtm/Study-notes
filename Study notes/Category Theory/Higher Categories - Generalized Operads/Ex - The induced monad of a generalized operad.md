---
type: exercise
subject: higher-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Algebra for a Generalized Operad"
  - "Def - Generalized Operad"
  - "Def - Algebra for a Monad"
  - "Def - Cartesian Monad"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

Let $P$ be a $T$-[[Def - Generalized Operad|operad]] over a [[Def - Cartesian Monad|cartesian monad]] $(T, \eta, \mu)$ on $\mathcal{E}$ (with terminal object $1$). Define $T_P X = P \times_{T1} TX$ (the pullback of $\mathrm{ar} : P \to T1$ against $T(!_X) : TX \to T1$). Show that $T_P$ carries the structure of a [[Def - Monad and Comonad|monad]] on $\mathcal{E}$, with unit and multiplication built from the operad's unit and composition together with $\eta, \mu$, and that an [[Def - Algebra for a Generalized Operad|algebra for $P$]] is exactly an [[Def - Algebra for a Monad|Eilenberg–Moore algebra]] for $T_P$. Verify, for $\mathcal{E} = \mathbf{Set}$, $T = (-)^{*}$, that $T_P X = \coprod_n P(n) \times X^n$.

**Recall:**

![[Def - Algebra for a Generalized Operad#Categorical / Structural Definition]]

A [[Def - Monad and Comonad|monad]] is $(S, \eta^S, \mu^S)$ with $\eta^S : 1 \Rightarrow S$, $\mu^S : S^2 \Rightarrow S$ satisfying associativity and unitality. An [[Def - Algebra for a Monad|Eilenberg–Moore algebra]] is an object $X$ with $h : SX \to X$ satisfying $h \circ \eta^S_X = 1_X$ and $h \circ \mu^S_X = h \circ Sh$.

---

# Convergent Strategy

**Problem class:** A *construct-the-monad* problem (the fourth target), establishing the structural bridge between operads and monads. The routine is to build $\eta^{T_P}, \mu^{T_P}$ from the operad data, check the monad laws follow from the operad laws, and identify the two algebra notions.

**Assumption pattern:** The decisive inputs are the operad's unit $e$ and composition $\mathrm{comp}$, plus the cartesianness of $T$ (so the relevant pullbacks behave). The assumption to exploit is that the operad axioms are *exactly* the monad axioms in disguise: operad-unit gives monad-unit, operad-associativity gives monad-associativity. Recognizing this dictionary is the whole problem.

**Theorem routing:** From the [[Def - Generalized Operad|operad definition]] (supplying $e, \mathrm{comp}$) and the [[Def - Monad and Comonad|monad definition]] (the target axioms), with [[Def - Cartesian Monad|cartesianness]] ensuring the pullback $P \times_{T1} TX$ is functorial and the multiplication is well-defined. The algebra identification is the content of [[Def - Algebra for a Generalized Operad#Categorical / Structural Definition|the categorical definition]].

**Key decision point:** The non-obvious construction is the *multiplication* $\mu^{T_P} : T_P T_P X \to T_P X$. One must combine the operad composition $\mathrm{comp}$ (to compose the operations) with the monad multiplication $\mu_X$ (to flatten the $T$-shapes of inputs) in the right order, over the right pullback. Getting the bookkeeping right — operations compose via $\mathrm{comp}$, input-shapes flatten via $\mu$ — is the heart of the exercise. The tempting error is to flatten with $\mu$ alone, forgetting that the *operations* must also be composed.

---

# Legal Operations Used

1. **Operation 7 from the topic page (turn an operad into a monad and read its algebras).** This exercise constructs that monad explicitly and proves the algebra identification.
2. **Operation 4 from the topic page (form the composable-configuration pullback).** Both $T_P X$ and the multiplication domain are such pullbacks.
3. **Operation 9 from the topic page (recognize a pullback as a fibre of $T$).** $T_P X = P \times_{T1} TX$ is a fibre product, computed using cartesianness.

---

# Hints

> [!note]- Hint 1
> $T_P X = P \times_{T1} TX$ is "an operation of $P$ together with a $T$-shape of $X$-elements of matching arity". The unit $\eta^{T_P}_X : X \to T_P X$ should use the operad unit $e$ (the do-nothing operation) and $\eta_X$ (the singleton $T$-shape).

> [!note]- Hint 2
> The multiplication takes an operation decorated by a $T$-shape of (operation-decorated $T$-shapes of $X$) and must return a single operation decorated by a $T$-shape of $X$. Compose the operations with $\mathrm{comp}$; flatten the nested $T$-shapes of $X$ with $\mu_X$. Both happen over $T1$, using cartesianness.

> [!note]- Hint 3
> The monad unit law for $T_P$ is the operad unit law; the monad associativity is the operad associativity (composing operations) combined with the monad associativity of $T$ (flattening shapes). For the algebra identification, a map $h : T_P X = P \times_{T1} TX \to X$ is exactly an operad action, and the two pairs of axioms coincide line for line.

---

# Solution

The plan: define the unit and multiplication of $T_P$ from the operad data and $\eta, \mu$ (Step 1); verify the monad laws follow from the operad laws (Step 2); identify $P$-algebras with $T_P$-Eilenberg–Moore algebras and compute the $\mathbf{Set}$, $(-)^{*}$ case (Step 3).

**Step 1: Define the monad structure on $T_P$.**

> [!note]- Derivation
> Set $T_P X = P \times_{T1} TX$, the pullback of $\mathrm{ar} : P \to T1$ against $T(!_X) : TX \to T1$. Cartesianness of $T$ makes $X \mapsto T_P X$ a functor (the pullback is functorial in $X$).
>
> *Unit.* Define $\eta^{T_P}_X : X \to T_P X$ as the pairing $\langle e \circ !_X, \eta_X \rangle$: it picks the operad unit $e$ (arity = singleton shape, via $\mathrm{ar} \circ e = \eta_1$) together with the singleton $T$-shape $\eta_X(x)$. The arities match ($\eta_1$ on both sides), so this lands in the pullback.
>
> *Multiplication.* An element of $T_P T_P X = P \times_{T1} T(P \times_{T1} TX)$ is an operation $\theta$ together with a $T$-shape $\Theta$ of pairs (operation, $T$-shape of $X$). Define $\mu^{T_P}_X : T_P T_P X \to T_P X$ by: compose the operations using operad composition $\mathrm{comp}(\theta, T(\pi_P)(\Theta))$ to get a single operation, and flatten the nested $T$-shapes of $X$ using $\mu_X \circ T(\pi_{TX})(\Theta)$ to get a single $T$-shape of $X$. The two outputs have matching arity (operad composition and $\mu$ produce the same flattened shape, by cartesianness), so the pair lands in $T_P X$.

**Step 2: The monad laws follow from the operad laws.**

> [!note]- Derivation
> *Unitality of $T_P$.* The left and right unit laws $\mu^{T_P} \circ T_P \eta^{T_P} = 1 = \mu^{T_P} \circ \eta^{T_P} T_P$ unwind to: composing an operation with the unit operation $e$ returns it (operad unitality), while $\mu_X$ composed with $\eta$ returns the original shape (monad unitality of $T$). Both halves hold by hypothesis, so $T_P$ is unital.
>
> *Associativity of $T_P$.* The law $\mu^{T_P} \circ T_P \mu^{T_P} = \mu^{T_P} \circ \mu^{T_P} T_P$ splits into two independent associativities running in parallel: the *operations* compose associatively because $\mathrm{comp}$ satisfies operad associativity, and the *input-shapes* flatten associatively because $\mu$ satisfies the monad associativity $\mu \circ T\mu = \mu \circ \mu T$ of $T$. Cartesianness guarantees the two streams stay aligned over $T1$ throughout. Hence $T_P$ is associative, and $(T_P, \eta^{T_P}, \mu^{T_P})$ is a monad.

**Step 3: Algebras coincide, and the $\mathbf{Set}$ computation.**

> [!note]- Derivation
> An [[Def - Algebra for a Generalized Operad|algebra for $P$]] is an object $X$ with an action $h : P \times_{T1} TX \to X$ satisfying the operad-unit and operad-associativity laws. But $P \times_{T1} TX = T_P X$, so $h : T_P X \to X$, and the operad-unit law is exactly $h \circ \eta^{T_P}_X = 1_X$ while the operad-associativity law is exactly $h \circ \mu^{T_P}_X = h \circ T_P h$ — the [[Def - Algebra for a Monad|Eilenberg–Moore]] axioms. So $P\text{-}\mathbf{Alg} \cong \mathcal{E}^{T_P}$, with the same morphisms (a $P$-algebra map is a map commuting with $h$, i.e. a $T_P$-algebra map).
>
> *The $\mathbf{Set}$, $(-)^{*}$ case.* Here $T1 = \mathbb{N}$, $\mathrm{ar} : P \to \mathbb{N}$ slices $P$ into $P(n)$, and $TX = X^{*} = \coprod_n X^n$ with $T(!_X)$ recording length. The pullback over $\mathbb{N}$ matches an operation of arity $n$ with a length-$n$ tuple of $X$-elements:
> $$T_P X = P \times_{\mathbb{N}} X^{*} = \coprod_{n \geq 0} P(n) \times X^n,$$
> the classical operad-monad. Its algebras are sets $X$ with maps $P(n) \times X^n \to X$ coherent under substitution — classical operad-algebras — confirming the general identification.

> [!note]- Complete formal solution
> Define $T_P X = P \times_{T1} TX$ (functorial by cartesianness of $T$). The unit $\eta^{T_P}_X = \langle e\circ !_X, \eta_X\rangle$ pairs the operad unit with the singleton shape; the multiplication $\mu^{T_P}_X$ composes operations via $\mathrm{comp}$ and flattens shapes via $\mu_X$, landing in $T_P X$ by arity-matching (cartesianness). The monad unit laws reduce to operad unitality and $T$-unitality; the monad associativity reduces to operad associativity (operations) running in parallel with $T$-associativity (shapes). So $(T_P, \eta^{T_P}, \mu^{T_P})$ is a monad. Since $T_P X = P \times_{T1} TX$, an operad action $h : P \times_{T1} TX \to X$ is a map $T_P X \to X$, and the operad-unit and operad-associativity laws are precisely the Eilenberg–Moore axioms, so $P\text{-}\mathbf{Alg} \cong \mathcal{E}^{T_P}$. For $\mathbf{Set}$, $T = (-)^{*}$: $T_P X = P \times_{\mathbb{N}} X^{*} = \coprod_n P(n) \times X^n$, the classical operad-monad. $\blacksquare$

---

# Key Takeaways

**Every operad is secretly a monad, and the translation is the most useful single fact about operad-algebras.** The construction $P \mapsto T_P$ converts an operad into a monad whose Eilenberg–Moore algebras are the operad-algebras, which means the entire mature theory of [[Def - Algebra for a Monad|monad-algebras]] — completeness of the algebra category, the free–forgetful adjunction, monadicity criteria, the bar resolution — becomes available for operad-algebras for free. The reusable technique is "to study the algebras of an operad, build its monad and recognize the Eilenberg–Moore category". This is exactly how [[Ex - Algebras for the associative operad are monoids|$\mathrm{Assoc}$-algebras]] are seen to be monoids: $T_{\mathrm{Assoc}} = (-)^{*}$ is the free-monoid monad. The trigger is any question of the form "what are the algebras of this operad?".

**The monad multiplication runs two flattenings in parallel: operations compose, shapes flatten, and cartesianness keeps them aligned.** The subtle part of the construction is that $\mu^{T_P}$ does *two* things at once — it composes the operations with $\mathrm{comp}$ and flattens the input-shapes with $\mu$ — and these must stay coordinated over the arity object $T1$. This is the structural reason cartesianness is indispensable even at the level of algebras: it is what guarantees the operation-stream and the shape-stream produce the same flattened arity, so the multiplication is well-defined. The transferable insight is that whenever you see a "compose and flatten" operation in higher algebra, expect two coordinated streams and a coherence condition (here, cartesianness) ensuring their alignment.

**The operad axioms are the monad axioms in disguise, which is why the algebra notions are *equal*, not merely analogous.** The proof's economy comes from the dictionary: operad-unit $\leftrightarrow$ monad-unit, operad-associativity $\leftrightarrow$ monad-associativity. Because the dictionary is exact, the two definitions of algebra do not just resemble each other — they are literally the same maps satisfying the same equations. The lesson to carry forward is that "operad" and "monad with a particular shape of operations" are two presentations of one idea, and the choice between them is a matter of convenience: operads make the *arities* explicit and combinatorial, monads make the *algebras* and their category theory explicit. Knowing how to pass between them, as this exercise does, lets you use whichever presentation makes the current problem easiest. See [[Def - Algebra for a Generalized Operad]] for the conceptual statement and [[Ex - Reading the unifying table across three monads]] for how this populates the algebra column of the table.
