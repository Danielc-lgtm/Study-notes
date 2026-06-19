---
type: definition
subject: category-theory
prereqs:
  - "Def - Monad and Comonad"
  - "Def - Algebra for a Monad"
  - "Def - Functor"
  - "Def - Category"
tags: [category-theory, foundations]
---

# Notation

Throughout, $(T, \eta, \mu)$ is a [[Def - Monad and Comonad|monad]] on a [[Def - Category|category]] $\mathcal{C}$. The **Kleisli category** is written $\mathcal{C}_T$ (subscript), distinguishing it from the [[Def - Algebra for a Monad|Eilenberg–Moore category]] $\mathcal{C}^T$ (superscript). A morphism of $\mathcal{C}_T$ from $A$ to $B$ — a **Kleisli arrow** — is a $\mathcal{C}$-morphism $A \to TB$; to mark the distinction we sometimes write it $A \rightsquigarrow B$. Its Kleisli composition with $g : B \rightsquigarrow C$ is denoted $g \diamond f$. The full symbol registry is on [[Category Theory V — Monads, Algebras, and Monoidal Categories]].

---

# Axiom Motivation

Many maps in mathematics and computation are not honest functions $A \to B$ but functions that produce a *$T$-decorated* output: a partial function returns "an element of $B$, or nothing"; a nondeterministic map returns "a set of possible elements of $B$"; a stochastic map returns "a probability distribution over $B$." In each case the target is not $B$ but $TB$ for the appropriate [[Def - Monad and Comonad|monad]] $T$ — $(-)+1$, the power set $P$, the distribution monad $D$. We would like to *compose* such maps as if they were ordinary functions $A \to B$, building a category in which they are the morphisms. The Kleisli category is exactly that category, and its composition law is forced by what "compose two effectful maps" must mean.

Suppose $f : A \to TB$ and $g : B \to TC$. We want their composite to be an effectful map $A \to TC$. We cannot simply compose $g \circ f$ — that would be a map $A \to TB$ followed by $B \to TC$, and the types do not match, since $f$ lands in $TB$, not $B$. The natural fix uses the monad structure. First push $g$ through $T$: $Tg : TB \to T^2 C$. Now $Tg \circ f : A \to T^2C$ produces a *nested* effect — a distribution of distributions, a set of sets. The monad's multiplication is precisely the tool to flatten it: $\mu_C : T^2C \to TC$. So define
$$g \diamond f := \mu_C \circ Tg \circ f : A \to TC.$$
This is the only composition that uses exactly the data of a monad and produces the right type. Read for the distribution monad it is the Chapman–Kolmogorov / law-of-total-probability formula; for the power-set monad it is relational composition; for the maybe monad it is composition of partial functions.

What must the unit be? An identity Kleisli arrow $A \rightsquigarrow A$ must be an effect-free map $A \to TA$ that is neutral for $\diamond$. The monad unit $\eta_A : A \to TA$ — "produce the trivial decoration" — is the candidate, and it works precisely because of the monad's *unit laws*. The left identity $\eta_B \diamond f = f$ unwinds to $\mu_B \circ T\eta_B \circ f = f$, which holds by $\mu \circ T\eta = 1$; the right identity $f \diamond \eta_A = f$ unwinds to $\mu_B \circ Tf \circ \eta_A = f$, which holds by naturality of $\eta$ followed by $\mu \circ \eta T = 1$. So the monad's unit axioms are exactly the identity laws of $\mathcal{C}_T$.

And associativity of $\diamond$? It unwinds to the monad's *associativity* axiom $\mu \circ T\mu = \mu \circ \mu T$ — flattening a triply-effectful map the same way regardless of order. So the three monad axioms are not abstract baggage: they are precisely the three category axioms (two identity laws and associativity) of $\mathcal{C}_T$. A reader could *invent* the monad axioms by demanding that effectful maps compose into a category.

Why not just use the [[Def - Algebra for a Monad|Eilenberg–Moore category]] instead? Because $\mathcal{C}_T$ is the *minimal* resolution: it contains only the objects of $\mathcal{C}$ and the free algebras, nothing more. When all you want is "compose effectful maps," you do not need the full category of algebras; you need exactly the free ones, and that is $\mathcal{C}_T$.

---

# The Definition

Let $(T, \eta, \mu)$ be a monad on $\mathcal{C}$. The **Kleisli category** $\mathcal{C}_T$ is defined by:

- **Objects:** the same objects as $\mathcal{C}$.
- **Morphisms:** $\mathcal{C}_T(A, B) = \mathcal{C}(A, TB)$. A Kleisli arrow $f : A \rightsquigarrow B$ is a $\mathcal{C}$-morphism $f : A \to TB$.
- **Composition:** for $f : A \rightsquigarrow B$ (i.e. $f : A \to TB$) and $g : B \rightsquigarrow C$ (i.e. $g : B \to TC$),
$$g \diamond f \;=\; \mu_C \circ Tg \circ f \;:\; A \to TC.$$
- **Identities:** $1_A^{\mathcal{C}_T} = \eta_A : A \to TA$.

The category axioms (associativity of $\diamond$, left and right identity) hold if and only if $(T, \eta, \mu)$ satisfies the monad axioms.

There is an adjunction $F_T \dashv U_T$ between $\mathcal{C}$ and $\mathcal{C}_T$, the **Kleisli adjunction**, inducing the monad $T$. The free functor $F_T : \mathcal{C} \to \mathcal{C}_T$ is the identity on objects and sends $h : A \to B$ to the Kleisli arrow $\eta_B \circ h : A \to TB$; the forgetful functor $U_T : \mathcal{C}_T \to \mathcal{C}$ sends $A \mapsto TA$ and a Kleisli arrow $f : A \to TB$ to $\mu_B \circ Tf : TA \to TB$.

**Equivalent description as free algebras.** The Kleisli category is isomorphic to the full subcategory of the Eilenberg–Moore category $\mathcal{C}^T$ on the **free algebras** $(TA, \mu_A)$: the assignment $A \mapsto (TA, \mu_A)$ on objects extends to a fully faithful, identity-on-the-free-algebras functor, and the Kleisli hom-set $\mathcal{C}(A, TB)$ matches the $T$-algebra hom-set $\mathcal{C}^T\big((TA,\mu_A),(TB,\mu_B)\big)$ via the free–forgetful adjunction. So
$$\mathcal{C}_T \;\cong\; \{\text{free $T$-algebras}\} \;\hookrightarrow\; \mathcal{C}^T.$$

---

# Categorical / Structural Definition

The structural definition is that **$\mathcal{C}_T$ is the initial resolution of $T$ into an adjunction.** By [[Thm - Eilenberg-Moore and Kleisli Realize a Monad]], the adjunctions $F \dashv U$ with $\mathcal{C}$ as the codomain of $U$ that induce a fixed monad $T = UF$ form a category, and the Kleisli adjunction $F_T \dashv U_T$ is its **initial object**: for any other such adjunction there is a unique comparison functor *out of* $\mathcal{C}_T$ commuting with the free and forgetful functors. Dually, the Eilenberg–Moore adjunction is terminal. So $\mathcal{C}_T$ is characterized, up to unique isomorphism, as the smallest category through which the monad's adjunction factors — built from $\mathcal{C}$ by freely adjoining the morphisms the monad demands and nothing else.

This is why $\mathcal{C}_T \cong \{\text{free algebras}\}$: the free algebras are exactly the objects the monad forces to exist, with no room for the "non-free" algebras that the larger, terminal Eilenberg–Moore category accommodates.

---

# Relate to Other Fields / Compression

The Kleisli category is the standard semantics of **effectful computation**. A program with effect $T$ is a Kleisli arrow $A \to TB$, and sequencing two programs is Kleisli composition (`bind`). The maybe monad gives partial functions / exceptions, the list monad gives nondeterminism, the state monad gives stateful computation, and the distribution monad gives probabilistic programs. This is the reason monads are ubiquitous in functional programming: the Kleisli category is where effectful programs live and compose.

**True name:** $\mathcal{C}_T$ is the **category of $T$-effectful maps** — objects of $\mathcal{C}$, with a morphism $A \to B$ being "a $\mathcal{C}$-map into the $T$-decorated $B$," composed by flattening. Equivalently, it is the **category of free $T$-algebras**, the minimal adjunction realizing $T$.

The compression is that "a map that does something extra on the way" is not a new primitive but a Kleisli arrow for the monad measuring the "extra." Recognizing partial functions, relations, and stochastic maps as Kleisli arrows for $(-)+1$, $P$, and $D$ collapses three apparently different theories of "non-functional maps" into one.

---

# Examples / Corollaries

**Is an instance — the Kleisli category of the power-set monad is $\mathbf{Rel}$.** A Kleisli arrow $A \to P(B)$ assigns to each $a \in A$ a subset of $B$ — equivalently a **relation** $R \subseteq A \times B$. Kleisli composition $g \diamond f = \mu_C \circ Tg \circ f$ computes, for $a \in A$, the set $\bigcup_{b \in f(a)} g(b)$, which is exactly relational composition $\{c : \exists b,\ aRb \wedge bSc\}$. The unit $\eta_A(a) = \{a\}$ is the identity relation. So $\mathbf{Set}_P \cong \mathbf{Rel}$, the category of sets and relations (full proof in [[Ex - The Kleisli category of the powerset monad is Rel]]).

**Is an instance — the Kleisli category of the maybe monad is partial functions.** A Kleisli arrow $A \to B + 1$ is a function defined on a subset of $A$, returning $*$ ("undefined") elsewhere — a **partial function**. Kleisli composition is composition of partial functions: the composite is defined exactly where both stages are. The unit is the everywhere-defined inclusion.

**Is an instance — the Kleisli category of the distribution monad is stochastic maps.** A Kleisli arrow $A \to D(B)$ assigns to each $a$ a probability distribution on $B$ — a **Markov kernel** / stochastic map. Kleisli composition is the law of total probability $(g \diamond f)(c \mid a) = \sum_b g(c \mid b)\, f(b \mid a)$. This is the category of "sets and channels," the entry point to **categorical probability** and **Markov categories** (see [[Ex - The distribution monad and Markov categories]]).

**Is NOT an instance — an arbitrary subcategory of $\mathcal{C}^T$.** Not every full subcategory of the Eilenberg–Moore category is a Kleisli category. $\mathcal{C}_T$ is *specifically* the free algebras $(TA, \mu_A)$; the subcategory of, say, all *finite* algebras is generally neither initial nor closed under the free functor, so it is not $\mathcal{C}_T$. The Kleisli category is the free algebras and only those.

**Corollary — the comparison functor.** The inclusion of free algebras $\mathcal{C}_T \hookrightarrow \mathcal{C}^T$ is the unique functor commuting with the free and forgetful functors; it is fully faithful but not in general essentially surjective. Its essential image is the full subcategory of free algebras, and $\mathcal{C}_T \simeq \mathcal{C}^T$ exactly when every algebra is (a retract of) a free one.

**Calibration check.** Verify the left identity $\eta_B \diamond f = f$ using $\mu \circ T\eta = 1$; check on the power-set monad that $g \diamond f$ reproduces relational composition; and confirm that the Kleisli hom-set $\mathcal{C}(A,TB)$ matches $\mathcal{C}^T((TA,\mu_A),(TB,\mu_B))$ via the free–forgetful adjunction, so that $\mathcal{C}_T$ really is the free algebras.

---

# Unlocked by This

> [!tip] Markov Categories and Categorical Probability *(from Categorical Probability)*
> The Kleisli category of the **distribution / Giry monad** has stochastic maps as morphisms. Adding copy-and-discard structure makes it a **Markov category**, the diagrammatic foundation of conditional independence, Bayesian inversion, and sufficient statistics — and a substrate for **categorical systems theory** and agent foundations.

> [!tip] Monad Transformers and Effect Handlers *(from Programming Language Theory)*
> Stacking monads via distributive laws builds composite effects; the Kleisli categories of the resulting monads are the semantics of **effect handlers** and monad transformers in functional programming.
