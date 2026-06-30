---
type: topic
subject: category-theory
chapter: "5.1-5.4"
title: "Category Theory V — Monads, Algebras, and Monoidal Categories"
tags: [category-theory, foundations]
---

# Notation Registry

Throughout this chapter $\mathcal{C}, \mathcal{D}, \mathcal{E}$ are categories, $A, B, C, X, Y$ are objects, and $f, g, h$ are morphisms. We write $\mathcal{C}(A,B)$ for the hom-set, $1_A$ for the identity, and $g \circ f$ for composition. Functors are $F, G, H$; natural transformations are $\alpha, \beta, \eta, \varepsilon, \mu, \lambda, \rho$. We write $F \dashv G$ for "$F$ is left adjoint to $G$". The functor category is $[\mathcal{C}, \mathcal{D}]$. One **standing convention**: a natural transformation between composite functors is built by *whiskering*. If $\theta : F \Rightarrow G$ is a natural transformation between $F, G : \mathcal{C} \to \mathcal{D}$ and $H : \mathcal{D} \to \mathcal{E}$ is a functor, then $H\theta : HF \Rightarrow HG$ has components $H(\theta_X)$; and if $K : \mathcal{B} \to \mathcal{C}$, then $\theta K : FK \Rightarrow GK$ has components $\theta_{KX}$. We write $T\mu$ and $\mu T$ for the two whiskerings of $\mu : T^2 \Rightarrow T$ along $T$; they are *different* transformations and keeping them straight is the whole game in the monad axioms.

- $T : \mathcal{C} \to \mathcal{C}$ — an **endofunctor**; for a monad it is the underlying functor. $T^2 = T \circ T$, $T^3 = T \circ T \circ T$.
- $\eta : 1_{\mathcal{C}} \Rightarrow T$ — the **unit** of a monad (component $\eta_A : A \to TA$)
- $\mu : T^2 \Rightarrow T$ — the **multiplication** of a monad (component $\mu_A : T^2A \to TA$)
- $(T, \eta, \mu)$ — a monad; dually $(G, \varepsilon, \delta)$ a comonad with **counit** $\varepsilon : G \Rightarrow 1$ and **comultiplication** $\delta : G \Rightarrow G^2$
- $\varepsilon : FU \Rightarrow 1_{\mathcal{D}}$ — the **counit** of an adjunction $F \dashv U$; $\eta : 1_{\mathcal{C}} \Rightarrow UF$ its unit
- $(A, a)$ — a **$T$-algebra**: an object $A$ with a **structure map** $a : TA \to A$
- $\mathcal{C}^T$ — the **Eilenberg–Moore category** of $T$-algebras; $U^T : \mathcal{C}^T \to \mathcal{C}$ forgetful, $F^T : \mathcal{C} \to \mathcal{C}^T$ free
- $\mathcal{C}_T$ — the **Kleisli category**: same objects as $\mathcal{C}$, with $\mathcal{C}_T(A,B) = \mathcal{C}(A, TB)$
- $(\mathcal{C}, \otimes, I)$ — a **monoidal category**: tensor $\otimes : \mathcal{C} \times \mathcal{C} \to \mathcal{C}$, unit object $I$
- $\alpha_{A,B,C} : (A \otimes B) \otimes C \xrightarrow{\sim} A \otimes (B \otimes C)$ — the **associator**
- $\lambda_A : I \otimes A \xrightarrow{\sim} A$, $\rho_A : A \otimes I \xrightarrow{\sim} A$ — the left and right **unitors**
- $\beta_{A,B} : A \otimes B \xrightarrow{\sim} B \otimes A$ — the **braiding** (in a braided/symmetric monoidal category)
- $(M, m, e)$ — a **monoid** in a monoidal category: $m : M \otimes M \to M$, $e : I \to M$
- $\mathbf{Set}, \mathbf{Grp}, \mathbf{Ab}, \mathbf{Ring}, \mathbf{CRing}, \mathbf{Mod}_R, \mathbf{Vect}_k, \mathbf{Top}, \mathbf{Cat}, \mathbf{Rel}$ — the usual named categories
- $A^*$ — the set of finite lists (words) of elements of $A$; $P(A)$ — the power set of $A$; $R[A]$ — the free $R$-module on $A$

---

# Motivation

Here is the chapter in one sentence: **a monad is the algebra a forgetful functor leaves behind, and a monoidal category is the ambient world in which the word "algebra" makes sense at all.** These two ideas are secretly the same idea, and the punchline of the chapter — *a monad is a monoid in the category of endofunctors* — is the bridge that joins §5.1 to §5.4.

The story starts with [[Def - Adjunction|adjunctions]], the subject of the previous chapter. An adjunction $F \dashv U$ between $\mathcal{C}$ and $\mathcal{D}$ — think of $U : \mathbf{Grp} \to \mathbf{Set}$ forgetting the group structure and $F$ building the free group — is a rich piece of data living across two categories. Now stand inside $\mathcal{C} = \mathbf{Set}$ and forget that $\mathbf{Grp}$ exists. What can you still see? You see the composite endofunctor $T = UF : \mathbf{Set} \to \mathbf{Set}$, which sends a set to the underlying set of the free group on it. You see the unit $\eta : 1 \Rightarrow T$, the inclusion of generators. And from the counit you can salvage one whiskered piece, $\mu = U\varepsilon F : T^2 \Rightarrow T$. This triple $(T, \eta, \mu)$ is the **shadow** the adjunction casts on $\mathbf{Set}$, and the axioms it satisfies are exactly the axioms of a monad. The first miracle of the chapter is that this shadow contains enough information to *reconstruct* $\mathbf{Grp}$, as the category of "sets on which $T$ acts coherently" — its **algebras**.

The structural backbone of the chapter is the diagram of forgetful functors and what they remember:

$$\text{adjunction } F \dashv U \;\rightsquigarrow\; \text{monad } T = UF \;\rightsquigarrow\; \text{algebras } \mathcal{C}^T \;\overset{?}{\simeq}\; \mathcal{D}.$$

The question mark is **monadicity**: when is $\mathcal{D}$ really recovered as $\mathcal{C}^T$? The answer is the [[Thm - The Barr-Beck Monadicity Theorem|Barr–Beck theorem]], and it draws a sharp line through mathematics. [[Def - Group|Groups]], [[Def - Ring|rings]], [[Def - Module|modules]], lattices, compact Hausdorff spaces — all *algebraic* over $\mathbf{Set}$, all monadic. Topological spaces and fields are *not* monadic, and the theorem explains precisely why: topology is not described by operations and equations, and a field cannot be presented by a monad because you cannot freely adjoin a multiplicative inverse.

Then comes the reframing. The monad axioms — associativity $\mu \circ T\mu = \mu \circ \mu T$ and unitality $\mu \circ T\eta = \mu \circ \eta T = 1_T$ — are *literally* the axioms of a monoid, with the multiplication $\otimes$ taken to be composition of endofunctors and the unit object taken to be the identity functor $1_{\mathcal{C}}$. To say that out loud we need the notion of a [[Def - Monoidal Category|monoidal category]] $(\mathcal{C}, \otimes, I)$: a category with a tensor product, an associator, and unitors satisfying [[Thm - Mac Lane Coherence Theorem|Mac Lane's pentagon and triangle]]. A [[Def - Monoid in a Monoidal Category|monoid]] in $(\mathbf{Ab}, \otimes)$ is a [[Def - Ring|ring]]; a monoid in $(\mathbf{Vect}_k, \otimes)$ is a $k$-algebra; a monoid in $([\mathcal{C},\mathcal{C}], \circ)$ is a monad. The chapter closes the loop: the abstract machinery of §5.1 was an instance of the abstract machinery of §5.4 all along.

This chapter assumes you are comfortable with the previous four. You should have refreshed [[Def - Adjunction|adjunctions]], especially the [[Def - Unit and Counit of an Adjunction|unit/counit/triangle-identity]] formulation and [[Def - Free-Forgetful Adjunction|free–forgetful adjunctions]]; [[Def - Functor|functors]] and [[Def - Natural Transformation|natural transformations]], including whiskering and the [[Def - Functor Category|functor category]] $[\mathcal{C},\mathcal{C}]$; and [[Def - Equalizer and Coequalizer|coequalizers]] together with the general [[Def - Limit and Colimit|limit/colimit]] vocabulary, which the monadicity theorem leans on. From outside category theory you should know what a [[Def - Group|group]], a [[Def - Ring|ring]], a [[Def - Module|module]], and a [[Def - Vector Space|vector space]] are, since these are the running examples of algebras.

---

# Concept Map

## §5.1 Monads and Comonads

- **[[Def - Monad and Comonad]]**
	- A **monad** on $\mathcal{C}$ is a triple $(T, \eta, \mu)$ with $T : \mathcal{C} \to \mathcal{C}$ an endofunctor, $\eta : 1_{\mathcal{C}} \Rightarrow T$ the unit, $\mu : T^2 \Rightarrow T$ the multiplication, satisfying associativity $\mu \circ T\mu = \mu \circ \mu T$ and unitality $\mu \circ T\eta = \mu \circ \eta T = 1_T$. These are exactly the monoid axioms with $\otimes = \circ$ and unit object $1_{\mathcal{C}}$ — hence the slogan **a monad is a monoid in the category of endofunctors** (made precise in §5.4). A **comonad** $(G, \varepsilon, \delta)$ is the dual: $\varepsilon : G \Rightarrow 1$, $\delta : G \Rightarrow G^2$. Examples: the power-set monad $P$ on $\mathbf{Set}$ (unit = singleton, multiplication = union), the list monad $A \mapsto A^*$, the free-group monad $UF$, and the maybe monad $(-) + 1$.

- **[[Thm - Every Adjunction Gives a Monad]]**
	- Every adjunction $F \dashv U$ with $F : \mathcal{C} \to \mathcal{D}$, $U : \mathcal{D} \to \mathcal{C}$, unit $\eta$ and counit $\varepsilon$, induces a monad on $\mathcal{C}$ with $T = UF$, unit $\eta$, and multiplication $\mu = U\varepsilon F : UFUF \Rightarrow UF$. The monad axioms fall out of the triangle identities and the naturality of $\varepsilon$. Dually the same adjunction induces a **comonad** $FU$ on $\mathcal{D}$. This is where almost every monad in nature comes from — the monad is the part of the adjunction visible from the base category alone.

> [!tip] Unlocked: The Probability Monad and Markov Categories *(from Categorical Probability)*
> The free-convex-combination construction is a monad: the **distribution monad** $D$ on $\mathbf{Set}$ sends $X$ to the set of finitely-supported probability distributions on $X$, with $\eta$ the point mass and $\mu$ averaging a distribution-of-distributions. Its measure-theoretic cousin is the **Giry monad** on measurable spaces. Once you have monads, the entire framework of **categorical probability** opens: stochastic maps are the morphisms of the Kleisli category (§5.2), and the resulting **Markov categories** are the categorical foundation of probability and agent foundations.

> [!note] Exercise Index — §5.1
> [[Exercise Index - §5.1 Monads and Comonads]]

- **[[Ex - The power-set monad]]** (⭐⭐)
	- Verify that $P : \mathbf{Set} \to \mathbf{Set}$ with $\eta_X(x) = \{x\}$ and $\mu_X(\mathcal{S}) = \bigcup \mathcal{S}$ satisfies the monad axioms, and identify the adjunction it comes from.

- **[[Ex - The free monoid monad]]** (⭐⭐)
	- Show $A \mapsto A^*$ (finite lists) is a monad with unit = singleton list and multiplication = concatenation/flattening, arising from the free–forgetful adjunction $\mathbf{Set} \rightleftarrows \mathbf{Mon}$.

- **[[Ex - Adjunctions inducing the same monad]]** (⭐⭐⭐)
	- Exhibit two genuinely different adjunctions that induce the *same* monad, previewing the theorem that Eilenberg–Moore and Kleisli are the terminal and initial such adjunctions.

## §5.2 Algebras Eilenberg-Moore and Kleisli

- **[[Def - Algebra for a Monad]]**
	- A **$T$-algebra** (Eilenberg–Moore algebra) is a pair $(A, a)$ with $a : TA \to A$ a structure map satisfying the *unit law* $a \circ \eta_A = 1_A$ and the *associativity law* $a \circ \mu_A = a \circ Ta$. A morphism $(A,a) \to (B,b)$ is a map $f : A \to B$ with $f \circ a = b \circ Tf$. These assemble into the Eilenberg–Moore category $\mathcal{C}^T$, with a forgetful $U^T : \mathcal{C}^T \to \mathcal{C}$ and a free $F^T \dashv U^T$. Algebras for the list monad are exactly [[Def - Monoid in a Monoidal Category|monoids]]; algebras for the free-group monad are [[Def - Group|groups]]; algebras for the free-$R$-module monad are [[Def - Module|modules]]; algebras for the power-set monad are complete (sup-)lattices.

- **[[Def - Kleisli Category]]**
	- The **Kleisli category** $\mathcal{C}_T$ has the same objects as $\mathcal{C}$ but $\mathcal{C}_T(A,B) = \mathcal{C}(A, TB)$ — a Kleisli arrow $A \rightsquigarrow B$ is a $\mathcal{C}$-arrow $A \to TB$. Composition of $f : A \to TB$ and $g : B \to TC$ is $\mu_C \circ Tg \circ f$, and identities are the units $\eta_A$. The Kleisli category is isomorphic to the full subcategory of $\mathcal{C}^T$ on the **free algebras**. Kleisli of the power-set monad is $\mathbf{Rel}$ (sets and relations); of the maybe monad, sets and partial functions; of the distribution monad, sets and stochastic maps.

- **[[Thm - Eilenberg-Moore and Kleisli Realize a Monad]]**
	- Every monad $T$ arises from an adjunction: both $F^T \dashv U^T$ (Eilenberg–Moore) and $F_T \dashv U_T$ (Kleisli) induce $T$. Moreover, in the category of *all* adjunctions inducing $T$, the Eilenberg–Moore adjunction is **terminal** and the Kleisli adjunction is **initial**. So the two universal solutions bracket every other resolution of $T$ into an adjunction: Kleisli is the smallest (free algebras only), Eilenberg–Moore the largest (all algebras).

> [!tip] Unlocked: Lawvere Theories and Universal Algebra *(from Algebra)*
> Algebras for a monad on $\mathbf{Set}$ are precisely models of an (possibly infinitary) **algebraic theory** — a signature of operations and equations. This is the categorical face of **universal algebra**: groups, rings, modules, lattices, Boolean algebras are all "$T$-algebras for some $T$", which is why they share a forgetful functor with a left adjoint, free objects, and quotients-by-relations. The finitary case is captured by **Lawvere theories**, and the monad/Lawvere-theory dictionary is the entry point to that subject.

> [!note] Exercise Index — §5.2
> [[Exercise Index - §5.2 Algebras Eilenberg-Moore and Kleisli]]

- **[[Ex - Algebras for the free-group monad are groups]]** (⭐⭐⭐)
	- Prove that the Eilenberg–Moore category of the free-group monad $T = UF$ on $\mathbf{Set}$ is equivalent to **[[Def - Group|Grp]]**: a structure map $TA \to A$ is exactly a group multiplication, and the algebra laws are exactly the group axioms.

- **[[Ex - The Kleisli category of the powerset monad is Rel]]** (⭐⭐)
	- Show $\mathbf{Set}_P \cong \mathbf{Rel}$: a Kleisli arrow $A \to P(B)$ is a relation, and Kleisli composition is relational composition.

- **[[Ex - Algebras for the free-vector-space monad]]** (⭐⭐)
	- Identify the algebras for the free-$k$-vector-space monad $X \mapsto k[X]$ on $\mathbf{Set}$ as $k$-vector spaces, reading the structure map as "evaluate a formal linear combination."

## §5.3 Monadicity and the Barr-Beck Theorem

- **[[Thm - The Barr-Beck Monadicity Theorem]]**
	- A functor $U : \mathcal{D} \to \mathcal{C}$ is **monadic** (the comparison $\mathcal{D} \to \mathcal{C}^T$ is an equivalence) if and only if: (i) $U$ has a left adjoint, (ii) $U$ is **conservative** (reflects [[Def - Isomorphism|isomorphisms]]), and (iii) $U$ **creates coequalizers of $U$-split pairs**. The forgetful functors from $\mathbf{Grp}, \mathbf{Ring}, \mathbf{Mod}_R$, $\mathbf{CABool}$, and compact Hausdorff spaces to $\mathbf{Set}$ are monadic; $\mathbf{Top} \to \mathbf{Set}$ is **not** (its induced monad is the identity, whose algebras are bare sets — topology is not algebraic). The dual, **comonadic** version powers descent.

> [!tip] Unlocked: Faithfully Flat Descent *(from Algebraic Geometry)*
> The comonadic dual of Barr–Beck is the engine of **descent**: for a faithfully flat ring map $R \to S$, the base-change functor $S \otimes_R -$ is comonadic, so an $R$-module is the same data as an $S$-module equipped with **descent data** (an isomorphism over $S \otimes_R S$ satisfying a cocycle condition). Geometrically this lets you build objects on a **scheme** by building them on a cover and gluing — the categorical payoff of monadicity in **algebraic geometry**.

> [!note] Exercise Index — §5.3
> [[Exercise Index - §5.3 Monadicity and the Barr-Beck Theorem]]

- **[[Ex - Which forgetful functors are monadic]]** (⭐⭐⭐)
	- Decide monadicity for $\mathbf{Grp} \to \mathbf{Set}$, $\mathbf{Ring} \to \mathbf{Set}$ (yes) versus $\mathbf{Top} \to \mathbf{Set}$ and $\mathbf{Field} \to \mathbf{Set}$ (no), pinning the failure to conservativity / the missing left adjoint.

- **[[Ex - Recognizing a category of algebras]]** (⭐⭐)
	- Use Barr–Beck to certify that a concrete category (e.g. $M$-sets for a fixed monoid $M$, or pointed sets) is the Eilenberg–Moore category of an explicitly identified monad.

- **[[Ex - Descent via comonadicity]]** (⭐⭐⭐)
	- Prove faithfully-flat descent for modules: $S \otimes_R -$ is comonadic, hence $\mathbf{Mod}_R \simeq$ comodules / modules-with-descent-data over $\mathbf{Mod}_S$.

## §5.4 Monoidal and Symmetric Monoidal Categories

- **[[Def - Monoidal Category]]**
	- A **monoidal category** $(\mathcal{C}, \otimes, I, \alpha, \lambda, \rho)$ has a tensor functor $\otimes$, a unit object $I$, and natural isomorphisms — associator $\alpha$, unitors $\lambda, \rho$ — subject to the **pentagon** and **triangle** coherence axioms. It is **braided** if it has $\beta_{A,B} : A \otimes B \xrightarrow{\sim} B \otimes A$ satisfying two hexagon axioms, and **symmetric** if additionally $\beta_{B,A} \circ \beta_{A,B} = 1_{A \otimes B}$. Examples: $(\mathbf{Set}, \times)$, $(\mathbf{Vect}_k, \otimes)$, $(\mathbf{Ab}, \otimes)$, $(\mathbf{Mod}_R, \otimes_R)$, $(\mathbf{Cat}, \times)$ are symmetric; the endofunctor category $([\mathcal{C},\mathcal{C}], \circ, 1)$ is monoidal but **not** symmetric.

- **[[Thm - Mac Lane Coherence Theorem]]**
	- In any monoidal category, *every* diagram built from $\alpha, \lambda, \rho$ (and their inverses, identities, and $\otimes$) commutes. Equivalently, every monoidal category is monoidally equivalent to a **strict** one in which $\alpha, \lambda, \rho$ are identities. The content is that all ways of re-bracketing a tensor product $A_1 \otimes \cdots \otimes A_n$ agree via a *unique* canonical isomorphism — so we may drop parentheses with impunity.

- **[[Def - Monoid in a Monoidal Category]]**
	- A **monoid** in $(\mathcal{C}, \otimes, I)$ is $(M, m : M \otimes M \to M, e : I \to M)$ with $m$ associative (via $\alpha$) and unital (via $\lambda, \rho$). A monoid in $(\mathbf{Set}, \times)$ is an ordinary monoid; in $(\mathbf{Ab}, \otimes)$ a [[Def - Ring|ring]]; a *commutative* monoid in $(\mathbf{Ab}, \otimes)$ a commutative ring; in $(\mathbf{Vect}_k, \otimes)$ a $k$-algebra; in $(\mathbf{Mod}_R, \otimes_R)$ an $R$-algebra; and in $([\mathcal{C},\mathcal{C}], \circ)$ a **monad** — closing the loop with §5.1.

> [!tip] Unlocked: TQFT, [[Def - Operad|Operads]], and Curry–Howard *(from Mathematical Physics, Algebra, Logic)*
> Symmetric monoidal categories are where "processes that run in parallel" live. A symmetric monoidal functor $\mathrm{Cob}_n \to \mathbf{Vect}_k$ from the cobordism category to vector spaces is exactly a **topological quantum field theory** — the Atiyah–Segal axioms in one line. Monoids-with-extra-arities generalize to **operads**. And the monoidal structure of a closed category models the tensor/par of linear logic, an instance of the **Curry–Howard** correspondence between proofs and programs.

> [!tip] Unlocked: Compositional Game Theory and Categorical Systems Theory *(from Agent Foundations)*
> Once tensor product means "side-by-side composition" and morphisms compose in series, you can draw and compute with string diagrams of interacting open systems. This is the substrate of **compositional game theory** and **categorical systems theory**: open games, lenses, and parametrized maps are morphisms in (symmetric) monoidal categories, and their wiring diagrams are exactly monoidal-category expressions. This is the formal home of the agent-foundations program.

> [!note] Exercise Index — §5.4
> [[Exercise Index - §5.4 Monoidal and Symmetric Monoidal Categories]]

- **[[Ex - Monoids in Vect are algebras and in Ab are rings]]** (⭐⭐)
	- Unwind the monoid-object axioms in $(\mathbf{Vect}_k, \otimes)$ to recover the definition of a unital associative $k$-algebra, and in $(\mathbf{Ab}, \otimes)$ to recover a [[Def - Ring|ring]].

- **[[Ex - The distribution monad and Markov categories]]** (⭐⭐⭐)
	- Build the distribution monad $D$ on $\mathbf{Set}$, identify its Kleisli category as "sets and stochastic maps," and show the copy-discard structure that makes it a **Markov category**.

- **[[Ex - Braidings and symmetry]]** (⭐⭐)
	- Distinguish braided from symmetric: show $(\mathbf{Vect}_k, \otimes)$ is symmetric, that the endofunctor category is not even braided in general, and that a one-object symmetric monoidal category is a commutative monoid.

---

# Sources and Targets

**Targets — what do we usually try to prove?**

The questions of this chapter cluster into five recurring goals. The first and most pervasive is **"is this category a category of algebras?"** — given a forgetful-looking functor $U : \mathcal{D} \to \mathcal{C}$, decide whether $\mathcal{D} \simeq \mathcal{C}^T$ for the induced monad. The second is **"what are the algebras of this monad?"**, the reverse direction: given a monad you can write down, identify $\mathcal{C}^T$ as a familiar category (monoids, groups, lattices). The third is **"realize this monad by an adjunction,"** which is always solvable in at least two canonical ways (Kleisli and Eilenberg–Moore) and the interesting content is their universal property. The fourth is **"identify the monoids in this monoidal category"** — rings, algebras, monads themselves all arise as the answer. The fifth is **coherence**: proving that a diagram of structural isomorphisms commutes, which Mac Lane's theorem reduces to a triviality. These five — recognize algebras, identify algebras, resolve into an adjunction, identify monoids, certify coherence — are the targets, and they recur because each pins down one of the two dual viewpoints (a structure as *operations on objects* versus a structure as *a single object in a structured category*).

**Sources — what assumptions do we usually leverage?**

The assumptions are equally stereotyped. **An adjunction is given or can be built** — this is the richest source, because [[Thm - Every Adjunction Gives a Monad|every adjunction immediately yields a monad]] $T = UF$ and a comparison functor into $\mathcal{C}^T$. **A forgetful functor with free objects** signals a candidate monadic situation and routes straight to [[Thm - The Barr-Beck Monadicity Theorem|Barr–Beck]]: check conservativity and creation of split coequalizers. **A presentation by operations and equations** — "a thing with a binary operation satisfying associativity" — is exactly the data of a monad, and the algebras are the models. **A tensor product is given** — on $\mathbf{Ab}$, $\mathbf{Vect}_k$, $\mathbf{Mod}_R$, or endofunctors — turns "find the monoids" into a concrete unwinding of the [[Def - Monoid in a Monoidal Category|monoid-object]] axioms. **A faithfully flat or otherwise "covering" map** routes to the comonadic dual of Barr–Beck and hence to descent. The recurring move is to convert a source to a target: an adjunction routes through the induced monad to a recognition or identification theorem; a tensor product routes through the monoid-object definition to rings and algebras; a covering map routes through comonadicity to descent.

---

# Legal Operations

These are the moves nearly every problem in this chapter is assembled from. When stuck, scan the list. Everything is self-contained: a reader who has only just met monads should be able to follow each operation from its description.

**Legal operations:**

1. **Read a monad off an adjunction.** Given any [[Def - Adjunction|adjunction]] $F \dashv U$, set $T = UF$, $\eta$ = the adjunction unit, $\mu = U\varepsilon F$. This is [[Thm - Every Adjunction Gives a Monad|the canonical source of monads]]: the moment you spot a free–forgetful pair, you have a monad for free, and you never need to check the monad axioms by hand. *Trigger:* a free construction (free group, free module, free monoid, free convex combination) appears. *Pattern:* "let $T$ be the monad of this adjunction; its algebras are…"

2. **Check the monad axioms via whiskering.** To verify $(T, \eta, \mu)$ is a monad directly, draw the associativity square ($\mu \circ T\mu = \mu \circ \mu T$ between $T^3 \Rightarrow T$) and the two unit triangles ($\mu \circ T\eta = \mu \circ \eta T = 1_T$). The only subtlety is keeping $T\mu$ (whisker $\mu$ on the left by $T$, component $\mu_{TA}$… careful: $T(\mu_A)$) distinct from $\mu T$ (component $\mu_{TA}$). *Trigger:* a candidate monad given by an explicit endofunctor (power set, lists) rather than by an adjunction.

3. **Build the structure map of an algebra.** A $T$-algebra is an object $A$ with $a : TA \to A$ obeying $a\circ\eta_A = 1_A$ and $a\circ\mu_A = a\circ Ta$. To exhibit a familiar structure (a group multiplication, a vector-space evaluation) *as* a $T$-algebra, write down the map that "performs the formal operation": $a$ takes a formal word/sum/distribution and actually multiplies/adds/averages it. *Trigger:* "show that $\mathcal{C}^T \simeq$ [known category]." *Pattern:* free generators map identically (unit law), and re-flattening a nested expression agrees with evaluating it (associativity law).

4. **Pass to the Kleisli category to model effectful maps.** When morphisms in your problem are "maps that produce a $T$-decorated output" — partial functions ($T = (-)+1$), nondeterministic maps ($T = P$), stochastic maps ($T = D$) — recognize them as [[Def - Kleisli Category|Kleisli arrows]] $A \to TB$ and compose them with the Kleisli rule $\mu_C \circ Tg \circ f$. *Trigger:* morphisms that "do something extra" on the way from $A$ to $B$.

5. **Apply Barr–Beck to recognize algebras.** To prove $U : \mathcal{D} \to \mathcal{C}$ is monadic, verify the three [[Thm - The Barr-Beck Monadicity Theorem|Barr–Beck]] conditions: a left adjoint exists, $U$ is conservative (an arrow is iso as soon as its image is), and $U$ creates coequalizers of $U$-split pairs. *Trigger:* a "structure-forgetting" functor whose fibres look algebraic. *Pattern:* conservativity is usually a one-liner; the split-coequalizer condition is where the work is.

6. **Dualize to a comonad for descent.** Every operation above has a dual: an adjunction induces a [[Def - Monad and Comonad|comonad]] $FU$ on the *other* category, coalgebras replace algebras, and the comonadic Barr–Beck recognizes descent situations. *Trigger:* a base-change or pullback-along-a-cover functor, e.g. $S \otimes_R -$ for a **faithfully flat** $R \to S$.

7. **Unwind a monoid object in a monoidal category.** To identify "monoids in $(\mathcal{C}, \otimes, I)$", write the multiplication $m : M \otimes M \to M$ and unit $e : I \to M$, then translate the associativity (mediated by $\alpha$) and unit (mediated by $\lambda, \rho$) diagrams into the concrete category. *Trigger:* "what is a monoid in $\mathcal{C}$?" *Pattern:* in $(\mathbf{Ab},\otimes)$ a bilinear $m$ is a ring multiplication; in $([\mathcal{C},\mathcal{C}],\circ)$ it is $\mu$ and a monad falls out.

8. **Invoke coherence to drop parentheses.** By [[Thm - Mac Lane Coherence Theorem|Mac Lane coherence]], any diagram of associators and unitors commutes, so you may treat $\otimes$ as strictly associative and unital, writing $A_1 \otimes \cdots \otimes A_n$ without brackets. *Trigger:* a computation in a monoidal category where re-bracketing threatens to multiply your bookkeeping. *Pattern:* "by coherence, suppress $\alpha, \lambda, \rho$."

9. **Recognize the free algebra / free–Kleisli embedding.** The [[Def - Kleisli Category|Kleisli category]] is the full subcategory of free algebras $(TA, \mu_A)$ inside $\mathcal{C}^T$. To compare two adjunctions inducing the same monad, route them through this embedding and the [[Thm - Eilenberg-Moore and Kleisli Realize a Monad|initiality of Kleisli / terminality of Eilenberg–Moore]]. *Trigger:* "are these the same monad?" or "compare these two resolutions."

**Illegal but tempting operations:**

> [!warning] 1. Treating every endofunctor with a unit as a monad
> It is tempting to think that any $T$ with a natural $\eta : 1 \Rightarrow T$ is "monad-like." But a monad needs a *multiplication* $\mu : T^2 \Rightarrow T$ satisfying associativity, and not every functor admits one. The squaring functor $T(A) = A \times A$ on $\mathbf{Set}$ has an obvious unit (the diagonal) but no associative $\mu : (A\times A)\times(A\times A) \to A\times A$ that is natural and unital — there is no canonical way to collapse four copies to two. The repair: a monad is precisely a [[Def - Monoid in a Monoidal Category|monoid]] in $([\mathcal{C},\mathcal{C}],\circ)$, so the missing ingredient is an associative, unital multiplication, not merely a unit.

> [!warning] 2. Assuming every forgetful functor is monadic
> Forgetful functors *usually* are monadic, which makes the failures easy to overlook. But $\mathbf{Top} \to \mathbf{Set}$ is **not** monadic: it is not conservative-plus-creating in the right way, and concretely its induced monad is the *identity* monad (the left adjoint is the discrete-space functor, so $UF = 1_{\mathbf{Set}}$), whose only algebras are bare sets — the topology is invisible to the monad. Likewise $\mathbf{Field} \to \mathbf{Set}$ fails because there is no free field, so no left adjoint at all. The repair condition is exactly the three [[Thm - The Barr-Beck Monadicity Theorem|Barr–Beck]] hypotheses; a functor that fails any one is not monadic.

> [!warning] 3. Confusing $T\mu$ with $\mu T$
> The associativity axiom $\mu \circ T\mu = \mu \circ \mu T$ involves two *different* whiskerings of $\mu : T^2 \Rightarrow T$. The transformation $T\mu : T^3 \Rightarrow T^2$ has component $T(\mu_A)$ (apply $T$ to the multiplication map), while $\mu T : T^3 \Rightarrow T^2$ has component $\mu_{TA}$ (the multiplication at the object $TA$). Swapping them silently breaks every proof. Concretely, for the list monad $T\mu$ flattens the *inner* lists of a list-of-lists-of-lists while $\mu T$ flattens the *outer* layer; both then flatten again and must agree. The fix is to always write the components out before manipulating.

> [!warning] 4. Expecting a monoidal category to be symmetric
> Having a tensor product does not give you a braiding, and having a braiding does not make it a symmetry. The endofunctor category $([\mathcal{C},\mathcal{C}],\circ)$ is monoidal but admits no natural isomorphism $F \circ G \cong G \circ F$ — composition of functors is genuinely non-commutative. Even when a braiding exists it can fail $\beta^2 = 1$: in the category of representations of a quantum group the braiding is a genuine non-symmetric solution of the Yang–Baxter equation. The repair: only invoke $\beta_{B,A}\circ\beta_{A,B} = 1$, swap-freely-reorder-tensor-factors moves, after verifying the category is actually **symmetric**, not merely monoidal.

---

# Problem-Solving Strategy

Begin by deciding which of the two dual viewpoints the problem lives in: are you handed an **adjunction / forgetful functor** (the "operations on objects" view) or a **monoidal category** (the "object in a structured world" view)? The chapter is built so that these two views meet in the middle, and naming your starting point tells you which machinery to reach for.

If the problem **gives you an adjunction, or a free construction**, the first move is automatic: form the monad $T = UF$ by [[Thm - Every Adjunction Gives a Monad|Lemma 5.1.3]]. You now own an endofunctor $T$, a unit, and a multiplication without any verification. The next question is which of three things the problem wants. If it wants you to **identify the algebras** $\mathcal{C}^T$, write down a general structure map $a : TA \to A$ and read it as "perform the formal operation"; the unit law says the operation is trivial on generators and the associativity law says nested operations flatten consistently — together they will reproduce the axioms of whatever structure $\mathcal{C}^T$ turns out to be (monoids for lists, groups for free groups, modules for free modules). If it wants you to **recognize a given category as monadic**, route to [[Thm - The Barr-Beck Monadicity Theorem|Barr–Beck]]: conservativity is nearly always immediate (a structure map that is bijective underneath is invertible as a homomorphism), and the real content is the creation of coequalizers of $U$-split pairs, which holds for "algebraic" categories and fails for topology. If it wants you to **realize a given monad by an adjunction**, you already have two canonical answers, [[Def - Kleisli Category|Kleisli]] and [[Def - Algebra for a Monad|Eilenberg–Moore]]; the interesting content is that these are the [[Thm - Eilenberg-Moore and Kleisli Realize a Monad|initial and terminal]] resolutions, so any other resolution factors uniquely between them.

If the problem **gives you a monoidal category and asks for its monoids**, write the multiplication $m : M \otimes M \to M$ and unit $e : I \to M$, then translate the [[Def - Monoid in a Monoidal Category|monoid-object diagrams]] into the concrete category. The skill is recognizing that a $\otimes$-bilinear multiplication on an [[Def - Abelian Group|abelian group]] is exactly a [[Def - Ring|ring]] multiplication, that a $\otimes_k$-bilinear one on a vector space is a $k$-algebra, and — the punchline — that an associative unital "multiplication" with respect to *composition* of endofunctors is exactly a monad. When the problem instead involves a **diagram of structural isomorphisms** that you fear might not commute, do not chase it by hand; invoke [[Thm - Mac Lane Coherence Theorem|Mac Lane coherence]] and pass to the strict model, where $\alpha, \lambda, \rho$ are identities and the diagram collapses.

If the problem **smells of geometry or gluing** — base change along a cover, modules over a faithfully flat extension, sheaves assembled from local data — dualize. The relevant object is a [[Def - Monad and Comonad|comonad]], the relevant recognition theorem is comonadic Barr–Beck, and the conclusion is a descent statement: the global category is equivalent to the category of local objects equipped with descent data. The reason this is worth trying whenever "local-to-global" appears is that descent is *literally* comonadicity, and comonadicity is a checklist.

The single unifying question of this chapter is: **"what does this forgetful functor remember, and is it everything?"** A monad is the precise record of what is remembered; monadicity is the statement that nothing else was lost; and the monoidal reframing says that "remembering an algebraic structure" and "being a monoid in a structured category" are two names for one phenomenon.

---

# Most Reusable Properties

- **[[Thm - Every Adjunction Gives a Monad|Adjunction ⟹ Monad]]**: $T = UF$, $\eta$ the unit, $\mu = U\varepsilon F$. This is the most-used fact in the chapter because it is *free*: it manufactures a monad the instant an adjunction is in sight, and adjunctions are everywhere (every free construction, every reflective subcategory, every Galois connection). Reach for it whenever a problem mentions "free" anything. Its most powerful disguised use is the reverse reading — when you want to *understand* a complicated category $\mathcal{D}$, find a forgetful functor to a simple base $\mathcal{C}$, form the monad, and study $\mathcal{C}^T$ instead.

- **[[Def - Algebra for a Monad|The Eilenberg–Moore algebra recipe]]**: $(A, a : TA \to A)$ with $a\circ\eta = 1$, $a\circ\mu = a\circ Ta$. This is the workhorse for *identification*: nearly every "what is the category of algebras" problem is solved by writing the structure map as "evaluate the formal expression" and matching the two laws against the target's axioms. The recognizable setup is "free generators plus relations," and the algebra laws are exactly "generators map identically" and "evaluation is associative." Internalizing this turns an opaque monad into a concrete algebraic theory.

- **[[Thm - The Barr-Beck Monadicity Theorem|Barr–Beck]]**: monadic ⟺ left adjoint + conservative + creates $U$-split coequalizers. Its typical use is to *certify* that a category of structured objects is exactly a category of algebras, which then hands you free objects, presentations by generators-and-relations, and a clean construction of limits and colimits. Recognize its applicability whenever a forgetful functor has a left adjoint; the only real labour is the split-coequalizer clause. Its negative use — proving non-monadicity, as for $\mathbf{Top}$ — is equally valuable: it explains *why* some categories behave non-algebraically.

- **[[Def - Monoid in a Monoidal Category|Monoid object]]**: $(M, m, e)$ in $(\mathcal{C}, \otimes, I)$. This single definition unifies monoids, rings, $k$-algebras, $R$-algebras, and monads — they are monoid objects in $\mathbf{Set}, \mathbf{Ab}, \mathbf{Vect}_k, \mathbf{Mod}_R$, and $[\mathcal{C},\mathcal{C}]$ respectively. Its reusable power is compression: prove something about monoid objects once and it specializes to all five. The typical use is to recognize a familiar algebraic structure as "a monoid in disguise," which immediately tells you what its modules, its bimodules, and its tensor-of-algebras should be.

- **[[Thm - Mac Lane Coherence Theorem|Coherence]]**: all diagrams of $\alpha, \lambda, \rho$ commute; equivalently every monoidal category strictifies. Its typical use is bookkeeping relief: it licenses dropping parentheses and unit isomorphisms in any monoidal computation, which is the difference between a tractable string-diagram calculation and an unreadable nest of associators. It is the reason the slogan "a monad is a monoid in endofunctors" can be taken literally despite composition of functors being only weakly unital in general.

---

# Bridges

1. **Universal algebra and Lawvere theories — monads *are* algebraic theories.** A monad $T$ on $\mathbf{Set}$ encodes a collection of operations of various arities together with the equations they satisfy, and a $T$-algebra is a *model* of that theory: a set with actual operations obeying the equations. The free-monoid monad encodes "one binary operation, associative, with a unit," and its algebras are monoids; the free-group monad adds inverses, and its algebras are [[Def - Group|groups]]. This is why every variety of algebras in the sense of universal algebra (groups, rings, lattices, modules) comes with a free functor, a forgetful functor, and a notion of presentation: each is the Eilenberg–Moore category of a monad. The finitary monads correspond exactly to **Lawvere theories**, small categories with finite products whose product-preserving functors to $\mathbf{Set}$ are the models.

2. **Algebraic geometry — descent is comonadicity.** Start from the dictionary that a commutative [[Def - Ring|ring]] $R$ has a geometric avatar, its prime spectrum, and that a ring map $R \to S$ is a map of geometric objects in the other direction. When $R \to S$ is **faithfully flat** — flat (so $S \otimes_R -$ is exact) and faithful (so it detects whether a module is zero) — the base-change functor $S \otimes_R - : \mathbf{Mod}_R \to \mathbf{Mod}_S$ is comonadic. The comonadic Barr–Beck theorem then says an $R$-module is *the same data* as an $S$-module $N$ together with **descent data**: an isomorphism $\theta : S \otimes_R N \cong N \otimes_R S$ over $S \otimes_R S$ satisfying a cocycle condition over $S \otimes_R S \otimes_R S$. Geometrically, you build a module (or a sheaf, or a **scheme**) on a space by building it on a cover and specifying how the pieces glue, with the cocycle condition guaranteeing the gluing is consistent on triple overlaps. This is the categorical heart of faithfully flat descent and the reason it works.

3. **Mathematical physics — symmetric monoidal functors are field theories.** Let $\mathrm{Cob}_n$ be the category whose objects are closed $(n-1)$-manifolds and whose morphisms are $n$-dimensional cobordisms between them, with disjoint union as tensor product. This is a symmetric [[Def - Monoidal Category|monoidal category]]. A **topological quantum field theory** is, by the Atiyah–Segal axioms, exactly a symmetric monoidal functor $Z : \mathrm{Cob}_n \to \mathbf{Vect}_k$: it assigns a vector space to each spatial slice and a linear map to each spacetime, with disjoint union of regions going to tensor product of spaces (so independent regions have independent states) and gluing of cobordisms going to composition of linear maps. The monoidal structure is doing real work: it is the statement that the physics of a disjoint union is the tensor product of the physics of the pieces.

4. **Categorical probability and agent foundations — Kleisli arrows are channels.** The distribution monad $D$ (and its measurable cousin, the **Giry monad**) has Kleisli category "$\mathbf{Set}$ with stochastic maps": a [[Def - Kleisli Category|Kleisli arrow]] $A \to D(B)$ is a Markov kernel, a family of probability distributions on $B$ indexed by $A$, and Kleisli composition is the Chapman–Kolmogorov equation. Equipping this category with copy-and-discard maps (a comonoid on every object) makes it a **Markov category**, the setting in which conditional independence, sufficient statistics, and Bayesian inversion can be defined diagrammatically. This is the formal substrate for **categorical probability** and the **compositional game theory / categorical systems theory** program in agent foundations, where agents and environments are open stochastic processes wired together as morphisms in a symmetric monoidal category.

---

# Insights

**The unifying frame: structure is what a forgetful functor forgets, and a monad is the record of it.** The deepest reorientation of this chapter is to stop thinking of a group as "a set with extra stuff" and start thinking of it as "a set together with the data of how the *free* group on it acts." That data is a structure map $TA \to A$, and the coherence it must satisfy is exactly the algebra laws. Once you see structure this way, the forgetful functor $\mathbf{Grp} \to \mathbf{Set}$ is not throwing away an opaque blob of "group-ness"; it is forgetting a specific, recoverable action of a specific monad. Monadicity is then the sharp question of whether the forgetting was lossless, and Barr–Beck is the answer. This frame is what lets category theory treat groups, rings, modules, lattices, and compact Hausdorff spaces with a single theorem instead of one ad hoc construction per subject.

**The true name of a monad is "monoid in endofunctors."** The official definition — an endofunctor with a unit and a multiplication satisfying three coherence diagrams — is the right thing to *check* but the wrong thing to *think*. The associativity diagram $\mu \circ T\mu = \mu \circ \mu T$ and the unit diagrams $\mu \circ T\eta = \mu \circ \eta T = 1$ are, symbol for symbol, the monoid axioms with the tensor product taken to be composition $\circ$ in the [[Def - Functor Category|functor category]] $[\mathcal{C},\mathcal{C}]$ and the unit object taken to be $1_{\mathcal{C}}$. So whenever you see a monad, do not picture three commuting squares; picture a monoid — an object you can multiply, with an associative product and a unit — living in the monoidal category of endofunctors. Everything about monads (free algebras, the bar construction, distributive laws) becomes the familiar algebra of monoids transplanted to a new ambient category. This is why §5.4 had to exist: it is the sentence that makes the slogan a theorem.

**Kleisli and Eilenberg–Moore are the two ends of one interval.** A single monad can be resolved into an adjunction in many ways, and at first this looks like a defect — which one is "the" adjunction? The resolution is that the collection of all such adjunctions is itself a category, and it has a smallest and a largest element. Kleisli ($\mathcal{C}_T$, just the free algebras) is **initial**: it is the most economical resolution, using only the objects the monad forces into existence. Eilenberg–Moore ($\mathcal{C}^T$, all algebras) is **terminal**: it is the most generous, including every object on which $T$ could conceivably act. Every other resolution — every concrete category of structured objects with a forgetful functor inducing $T$ — sits between them, mapping out of Kleisli and into Eilenberg–Moore. Recognizing a category as "between Kleisli and Eilenberg–Moore" is exactly recognizing it as a category of $T$-algebras, possibly missing some.

**Coherence is the permission to be sloppy, earned by a hard theorem.** It is tempting to treat $A \otimes (B \otimes C)$ and $(A \otimes B) \otimes C$ as literally equal and to drop unit isomorphisms, and in practice everyone does. Mac Lane's coherence theorem is what makes this *legitimate*: it proves that all the canonical isomorphisms you would ever insert to fix up bracketing and units are uniquely determined and mutually compatible, so no contradiction can arise from suppressing them. The surprising depth is that the proof connects to cut-elimination in proof theory — the "all diagrams commute" statement is a normalization result in disguise, where the canonical isomorphism between two bracketings is the unique normal-form rewriting between two expressions. The everyday consequence is mundane and indispensable: string-diagram and tensor-network calculations are valid precisely because coherence says the parenthesization you suppressed never mattered.
