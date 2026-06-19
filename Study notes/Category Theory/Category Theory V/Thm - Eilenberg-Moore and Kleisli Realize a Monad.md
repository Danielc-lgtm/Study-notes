---
type: theorem
subject: category-theory
prereqs:
  - "Def - Monad and Comonad"
  - "Def - Algebra for a Monad"
  - "Def - Kleisli Category"
  - "Def - Adjunction"
tags: [category-theory, foundations]
---

# Notation

Throughout, $(T, \eta, \mu)$ is a [[Def - Monad and Comonad|monad]] on a category $\mathcal{C}$. Its [[Def - Algebra for a Monad|Eilenberg–Moore category]] is $\mathcal{C}^T$, with forgetful $U^T : \mathcal{C}^T \to \mathcal{C}$ and free $F^T : \mathcal{C} \to \mathcal{C}^T$; its [[Def - Kleisli Category|Kleisli category]] is $\mathcal{C}_T$, with forgetful $U_T : \mathcal{C}_T \to \mathcal{C}$ and free $F_T : \mathcal{C} \to \mathcal{C}_T$. An **adjunction inducing $T$** is an adjunction $F \dashv U$ with $U : \mathcal{D} \to \mathcal{C}$, $F : \mathcal{C} \to \mathcal{D}$, whose induced monad (by [[Thm - Every Adjunction Gives a Monad]]) is exactly $(T, \eta, \mu)$. The full symbol registry is on [[Category Theory V — Monads, Algebras, and Monoidal Categories]].

---

# Statement

> **Theorem (realization of a monad).** Let $(T, \eta, \mu)$ be a monad on $\mathcal{C}$. Then:
> 1. The free–forgetful pair $F^T \dashv U^T$ for the [[Def - Algebra for a Monad|Eilenberg–Moore category]] is an adjunction inducing $T$.
> 2. The free–forgetful pair $F_T \dashv U_T$ for the [[Def - Kleisli Category|Kleisli category]] is an adjunction inducing $T$.
> 3. The adjunctions inducing $T$ form a category $\mathbf{Adj}(T)$, whose objects are such adjunctions and whose morphisms are comparison functors commuting with the free and forgetful functors. In $\mathbf{Adj}(T)$, the **Kleisli** adjunction is **initial** and the **Eilenberg–Moore** adjunction is **terminal**.

In particular every monad arises from an adjunction, and the two canonical resolutions bracket all others: for any adjunction $F \dashv U$ inducing $T$ there are unique comparison functors $\mathcal{C}_T \to \mathcal{D} \to \mathcal{C}^T$ commuting with the free and forgetful functors.

---

# Motivation

[[Thm - Every Adjunction Gives a Monad|The previous theorem]] showed every adjunction casts a monad as its shadow. The natural converse asks: given a monad, can we find an adjunction casting it? This theorem answers *yes, and canonically twice over*. It matters because it completes the dictionary between monads and adjunctions, and because the *two* answers are not a defect but the most useful part of the statement.

The puzzle the theorem resolves is non-uniqueness. A single monad can come from many different adjunctions — the free-group monad on $\mathbf{Set}$ is induced by $\mathbf{Set} \rightleftarrows \mathbf{Grp}$, but also by other categories with a forgetful functor to $\mathbf{Set}$ that happen to induce the same $UF$. Which adjunction is "the" one? The resolution is that the collection of all of them is organized into a category with a smallest and a largest element. The Kleisli construction is the smallest — it adjoins only the free algebras, the bare minimum the monad forces into existence. The Eilenberg–Moore construction is the largest — it includes every algebra, every object on which $T$ could possibly act. Every concrete category of structured objects inducing $T$ sits in between.

This is why recognizing a category as "$T$-algebras" is the same as recognizing it as the *terminal* resolution: the comparison functor $\mathcal{D} \to \mathcal{C}^T$ is the unique map into the terminal object, and asking whether it is an equivalence is exactly the [[Thm - The Barr-Beck Monadicity Theorem|monadicity]] question.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "a monad." The disguised sources are situations where a monad is present but unnamed.

A first disguised source is **a category of algebraic structures over a base**. Given $\mathbf{Grp}, \mathbf{Ring}, \mathbf{Mod}_R$ with their forgetful functors to $\mathbf{Set}$, the induced monad exists by [[Thm - Every Adjunction Gives a Monad|the previous theorem]], and *this* theorem says that category maps canonically into the Eilenberg–Moore category of its monad. The non-obvious step is that the comparison functor exists at all and is unique. *Example problem:* show the comparison $\mathbf{Grp} \to \mathbf{Set}^T$ is well-defined and identify when it is an equivalence.

A second disguised source is **an effectful computation framework**. A programming-language monad (state, exceptions, nondeterminism) presents its effectful maps; the theorem says these maps form the Kleisli category, the initial resolution. The non-obviousness is that "the category of effectful programs" is characterized by a universal property — it is the most economical category in which the effect can be sequenced. *Example problem:* show the category of partial functions is the Kleisli category of the maybe monad and is initial among resolutions.

A third disguised source is **two adjunctions you suspect induce the same monad**. Whenever you have two free–forgetful situations with the same composite $UF$, this theorem provides the comparison functors between them through Kleisli and Eilenberg–Moore. The non-obvious bridge is that "same monad" is detected by factoring both through the universal resolutions. *Example problem:* given two adjunctions inducing the list monad, exhibit the unique comparison between them (see [[Ex - Adjunctions inducing the same monad]]).

**Targets (Output Amplification)**

The conclusion gives the initial and terminal resolutions. Combined with other facts it does more.

Combine with **Barr–Beck**. Terminality of Eilenberg–Moore means there is *one* comparison $\mathcal{D} \to \mathcal{C}^T$ to test for equivalence. The further result is that monadicity is a property of a single canonical functor — you never have to search among adjunctions, only audit the one to the terminal object. This is what makes [[Thm - The Barr-Beck Monadicity Theorem|Barr–Beck]] a clean checklist rather than an existence hunt.

Combine with **idempotency**. If the monad is idempotent (e.g. from a [[Def - Reflective Subcategory|reflection]]), the Kleisli and Eilenberg–Moore categories *coincide* up to equivalence, so the initial and terminal resolutions agree. The further result: idempotent monads have an essentially unique resolution, which is why localizations and sheafifications behave so rigidly.

Combine with **the free-algebra embedding**. The Kleisli category embeds into Eilenberg–Moore as the free algebras. The further result is that the interval $[\mathcal{C}_T, \mathcal{C}^T]$ measures "how many non-free algebras there are" — and a category of structured objects is exactly $\mathcal{C}^T$ when every object is built from free ones by coequalizers, which is the conceptual content of the monadicity theorem's split-coequalizer clause.

---

# Why Is It True

Take the Eilenberg–Moore side first. Given the monad, build the category $\mathcal{C}^T$ of [[Def - Algebra for a Monad|algebras]]; the free functor $F^T : X \mapsto (TX, \mu_X)$ and forgetful $U^T : (A,a)\mapsto A$ are adjoint because a $T$-algebra morphism $(TX, \mu_X) \to (A,a)$ is the same data as a $\mathcal{C}$-morphism $X \to A$ (precompose with $\eta_X$ one way, with the structure map the other). Compute the induced monad: $U^T F^T (X) = TX$, the unit is $\eta$, and the multiplication is $U^T \varepsilon^T F^T$, where the counit $\varepsilon^T_{(A,a)} = a$ is the structure map. At a free algebra this gives $\mu$. So $\mathcal{C}^T$ induces $T$.

Now terminality. Suppose $F \dashv U$ is *any* adjunction inducing $T$, with $U : \mathcal{D} \to \mathcal{C}$. Each object $D \in \mathcal{D}$ has a canonical $T$-algebra structure on $UD$: the structure map is $U\varepsilon_D : TUD = UFUD \to UD$, the whiskered counit. The algebra laws are exactly the triangle identities and counit naturality (the same computation as the previous theorem). This defines the comparison $K : \mathcal{D} \to \mathcal{C}^T$, $D \mapsto (UD, U\varepsilon_D)$, and it is the *unique* functor commuting with the free and forgetful functors — because commuting with $U$ forces the object to be $UD$, and commuting with $F$ and respecting the counit forces the structure map to be $U\varepsilon_D$. So $\mathcal{C}^T$ is terminal.

The Kleisli side is dual in spirit. The Kleisli category is the free algebras, and the comparison goes the *other* way: from $\mathcal{C}_T$ *into* any resolution, sending the free Kleisli object to $FX$. Uniqueness again follows from commuting with the structure functors.

**The single mechanism: the structure map of a $T$-algebra is a whiskered counit, and a Kleisli arrow is a free-object map — so both comparison functors are forced, one out of Kleisli, one into Eilenberg–Moore.**

---

# What Makes This Hard

Two things. First, the **directions of the comparison functors are opposite**: Kleisli maps *out* (it is initial, so there is a unique functor *from* it), Eilenberg–Moore maps *in* (it is terminal, so there is a unique functor *to* it). Confusing the directions wrecks the universal-property statements. Second, the **counit of an arbitrary resolution must be shown to give an algebra structure**, and this is the same whiskered-counit computation as in [[Thm - Every Adjunction Gives a Monad|the previous theorem]] — people who did not internalize that "$U\varepsilon_D$ is an algebra structure map" get stuck constructing the comparison. The common error is to try to build the comparison from the *unit* rather than the counit.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Show $F^T \dashv U^T$ and $F_T \dashv U_T$ each induce $T$ by direct computation. For terminality of $\mathcal{C}^T$, send each $D \in \mathcal{D}$ to the algebra $(UD, U\varepsilon_D)$ and check this is the unique structure-functor-preserving comparison. For initiality of $\mathcal{C}_T$, build the comparison out of $\mathcal{C}_T$ on free objects and check uniqueness.

**Subgoal decomposition:**

1. **$F^T \dashv U^T$ is an adjunction inducing $T$.**
   - *Hint:* A morphism $(TX,\mu_X) \to (A,a)$ in $\mathcal{C}^T$ corresponds to a $\mathcal{C}$-morphism $X \to A$ via precomposition with $\eta_X$; the induced multiplication is $\mu$ since the counit at a free algebra is $\mu$.
   - *Why needed:* Establishes existence of the terminal resolution.

2. **$F_T \dashv U_T$ is an adjunction inducing $T$.**
   - *Hint:* Kleisli arrows $A \to TB$ are by definition the adjunction hom-set; the composite $U_T F_T$ is $T$ on objects.
   - *Why needed:* Establishes existence of the initial resolution.

3. **The comparison $K : \mathcal{D} \to \mathcal{C}^T$ exists.**
   - *Hint:* Set $K(D) = (UD, U\varepsilon_D)$; verify the algebra laws using the triangle identities and naturality of $\varepsilon$.
   - *Why needed:* It is the candidate unique map to the terminal object.

4. **$K$ is the unique comparison.**
   - *Hint:* Commuting with $U$ forces the underlying object to be $UD$; commuting with $F$ and the counit forces the structure map to be $U\varepsilon_D$.
   - *Why needed:* Establishes terminality.

5. **The Kleisli comparison out of $\mathcal{C}_T$ is unique.**
   - *Hint:* A functor out of $\mathcal{C}_T$ commuting with free functors is determined on objects (as $FX$) and on Kleisli arrows (as the transpose).
   - *Why needed:* Establishes initiality.

---

# Lemma Decomposition

> [!note]- Lemma 1: The Eilenberg–Moore adjunction induces $T$
> **Statement:** $F^T \dashv U^T$, and the induced monad on $\mathcal{C}$ is $(T, \eta, \mu)$.
>
> **Hint:** Show $\mathcal{C}^T((TX,\mu_X),(A,a)) \cong \mathcal{C}(X, A)$ naturally; compute the counit at the free algebra.
>
> **Why needed:** It exhibits the terminal resolution and shows it induces the right monad.
>
> > [!note]- Full proof
> > Define $\Phi : \mathcal{C}^T((TX,\mu_X),(A,a)) \to \mathcal{C}(X,A)$ by $f \mapsto f \circ \eta_X$, and $\Psi : \mathcal{C}(X,A) \to \mathcal{C}^T((TX,\mu_X),(A,a))$ by $g \mapsto a \circ Tg$. We check these are inverse. For $g : X \to A$, $\Phi\Psi(g) = a \circ Tg \circ \eta_X = a \circ \eta_A \circ g = g$, using naturality of $\eta$ ($Tg\circ\eta_X = \eta_A \circ g$) and the algebra unit law $a \circ \eta_A = 1_A$. For an algebra map $f : (TX,\mu_X)\to(A,a)$, $\Psi\Phi(f) = a \circ T(f\circ\eta_X) = a \circ Tf \circ T\eta_X = f \circ \mu_X \circ T\eta_X = f$, using the algebra-morphism square $a\circ Tf = f\circ\mu_X$ and the monad unit law $\mu_X\circ T\eta_X = 1$. So $\Phi$ is a natural bijection: $F^T \dashv U^T$. The composite $U^T F^T (X) = U^T(TX,\mu_X) = TX$, the unit is $\eta$, and the multiplication is $U^T$ of the counit whiskered by $F^T$; the counit at $(A,a)$ is the structure map $a$, so at a free algebra $(TX,\mu_X)$ it is $\mu_X$, giving multiplication $\mu$. Hence the induced monad is $(T,\eta,\mu)$.

> [!note]- Lemma 2: Every $D \in \mathcal{D}$ carries a canonical $T$-algebra structure
> **Statement:** For any adjunction $F \dashv U$ inducing $T$ and any $D \in \mathcal{D}$, the pair $(UD, U\varepsilon_D)$ is a $T$-algebra.
>
> **Hint:** The unit law is a triangle identity whiskered by $U$; the associativity law is naturality of $\varepsilon$ whiskered by $U$.
>
> **Why needed:** It defines the comparison functor $K$ on objects.
>
> > [!note]- Full proof
> > Write $a := U\varepsilon_D : TUD = UFUD \to UD$. Unit law: $a \circ \eta_{UD} = U\varepsilon_D \circ \eta_{UD} = (U\varepsilon \circ \eta U)_D = (1_U)_D = 1_{UD}$, by the triangle identity. Associativity law: we need $a \circ \mu_{UD} = a \circ Ta$, i.e. $U\varepsilon_D \circ U\varepsilon_{FUD} = U\varepsilon_D \circ UFU\varepsilon_D$ (using $\mu = U\varepsilon F$). Applying $U$ to naturality of $\varepsilon$ at the morphism $\varepsilon_D : FUD \to D$, namely $\varepsilon_D \circ FU\varepsilon_D = \varepsilon_D \circ \varepsilon_{FUD}$, gives exactly this. So $(UD, U\varepsilon_D)$ is a $T$-algebra. On morphisms $h : D \to D'$, $Uh$ is an algebra map by naturality of $\varepsilon$, so $K(D) := (UD, U\varepsilon_D)$ is functorial.

> [!note]- Lemma 3: $K$ is the unique structure-preserving comparison (terminality)
> **Statement:** $K : \mathcal{D} \to \mathcal{C}^T$ satisfies $U^T K = U$ and $K F = F^T$, and is the unique functor with these properties.
>
> **Hint:** $U^T K = U$ forces the underlying object; $KF = F^T$ together with respecting the counit forces the structure map.
>
> **Why needed:** It is exactly the statement that $\mathcal{C}^T$ is terminal in $\mathbf{Adj}(T)$.
>
> > [!note]- Full proof
> > By construction $U^T K(D) = U^T(UD, U\varepsilon_D) = UD = U(D)$, and $KF(X) = (UFX, U\varepsilon_{FX}) = (TX, \mu_X) = F^T(X)$ since $U\varepsilon_{FX} = (U\varepsilon F)_X = \mu_X$. For uniqueness, suppose $K'$ also satisfies $U^T K' = U$ and $K' F = F^T$. Then $K'(D) = (UD, a_D)$ for some structure map $a_D$ (forced underlying object). The counit $\varepsilon^T$ of $F^T \dashv U^T$ has component at $(A,a)$ equal to $a$; naturality of comparison functors requires $K'$ to send $\varepsilon_D$ to $\varepsilon^T_{K'(D)}$, which forces $a_D = U\varepsilon_D$. Hence $K' = K$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $(T,\eta,\mu)$ be a monad on $\mathcal{C}$.
>
> **Step 0 — the two resolutions exist.** The Eilenberg–Moore category $\mathcal{C}^T$ and the Kleisli category $\mathcal{C}_T$ are defined (see [[Def - Algebra for a Monad]], [[Def - Kleisli Category]]).
>
> **Step 1 — Eilenberg–Moore induces $T$.** By Lemma 1, $F^T \dashv U^T$ is an adjunction with induced monad $(T,\eta,\mu)$.
>
> **Step 2 — Kleisli induces $T$.** The Kleisli hom-set $\mathcal{C}_T(A,B) = \mathcal{C}(A,TB)$ is by construction the adjunction isomorphism for $F_T \dashv U_T$; the composite $U_T F_T = T$, with unit $\eta$ and multiplication $\mu$ (a direct check from the Kleisli composition law). So $F_T \dashv U_T$ induces $T$.
>
> **Step 3 — terminality of $\mathcal{C}^T$.** By Lemmas 2 and 3, for any adjunction $F \dashv U$ inducing $T$ there is a unique comparison $K : \mathcal{D} \to \mathcal{C}^T$ with $U^T K = U$ and $KF = F^T$. Hence $\mathcal{C}^T$ is terminal in $\mathbf{Adj}(T)$.
>
> **Step 4 — initiality of $\mathcal{C}_T$.** Dually, define $L : \mathcal{C}_T \to \mathcal{D}$ on objects by $L(A) = FA$ and on a Kleisli arrow $f : A \to TB$ by $L(f) = \varepsilon_{FB} \circ Ff : FA \to FB$ (the adjunction transpose). One checks $L$ is functorial, $UL = U_T$, $LF_T = F$, and that $L$ is the unique such functor — commuting with the free functors forces $L$ on objects, and commuting with $U$ forces it on morphisms. Hence $\mathcal{C}_T$ is initial in $\mathbf{Adj}(T)$.
>
> **Step 5 — conclude.** Every monad is induced by an adjunction (in fact by two canonical ones), and in the category of all such adjunctions the Kleisli adjunction is initial and the Eilenberg–Moore adjunction is terminal. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Free algebras as the initial resolution in universal algebra.** For the monad presenting groups, the Kleisli category is "free groups and group homomorphisms between them," and it is initial: any presentation of a group as a quotient of a free group factors through it. The exercise is to see the generators-and-relations presentation of a group as living in the interval between Kleisli (free groups) and Eilenberg–Moore (all groups).

**The state monad and stateful computation.** In programming, the state monad $S \mapsto (S \times -)^S$ has a Kleisli category of "stateful functions," which is the initial resolution. The exercise is to verify that this category is exactly the semantics of imperative programs over a fixed store, and that the Eilenberg–Moore category (state-machine algebras) is the terminal one.

**Idempotent monads and localization.** For a localization (e.g. inverting a set of primes in abelian groups), the monad is idempotent and Kleisli $\simeq$ Eilenberg–Moore. The exercise is to confirm that the initial and terminal resolutions coincide, explaining why a localization has an essentially unique universal property.

---

# Bridges

- **[[Thm - Every Adjunction Gives a Monad|Every adjunction gives a monad]]** — the converse direction. That theorem produces a monad from an adjunction; this one produces (two canonical) adjunctions from a monad. The structure map of a $T$-algebra is the whiskered counit appearing there, which is why the comparison functor is forced.

- **[[Thm - The Barr-Beck Monadicity Theorem|Barr–Beck monadicity]]** — the sharpening. Terminality says there is one comparison $\mathcal{D} \to \mathcal{C}^T$; Barr–Beck says exactly when it is an equivalence. So this theorem reduces "is $\mathcal{D}$ a category of algebras?" to auditing a single canonical functor.

- **[[Def - Kleisli Category|Kleisli embeds in Eilenberg–Moore]]** — the interval. The initial resolution is the free algebras inside the terminal one; the gap between them is the non-free algebras. Recognizing a category as sitting in this interval is recognizing it as $T$-algebras.

- **[[Def - Reflective Subcategory|Idempotent monads and reflections]]** — the degenerate case. When $\mu$ is invertible the two resolutions coincide; such monads are exactly the reflectors onto reflective subcategories, with a unique resolution.

---

# Unlocked by This

> [!tip] Distributive Laws and Composite Monads *(from Higher Algebra)*
> Comparing resolutions of $TS$ versus $ST$ for two monads $S, T$ leads to **distributive laws** $ST \Rightarrow TS$, which is how composite effects (e.g. nondeterministic-stateful computation) are built and when they are well-defined.

> [!tip] Monadic Descent and the Bar Construction *(from Algebraic Geometry)*
> The terminal resolution is the setting for the **bar construction** that computes monadic cohomology and, comonadically, organizes **descent** of modules and sheaves along covers.
