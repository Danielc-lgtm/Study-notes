---
type: theorem
subject: category-theory
prereqs:
  - "Def - Adjunction"
  - "Def - Unit and Counit of an Adjunction"
  - "Def - Monad and Comonad"
  - "Def - Natural Transformation"
tags: [category-theory, foundations]
---

# Notation

Throughout, $F \dashv U$ is an [[Def - Adjunction|adjunction]] with left adjoint $F : \mathcal{C} \to \mathcal{D}$ and right adjoint $U : \mathcal{D} \to \mathcal{C}$. Its [[Def - Unit and Counit of an Adjunction|unit]] is $\eta : 1_{\mathcal{C}} \Rightarrow UF$ and its **counit** is $\varepsilon : FU \Rightarrow 1_{\mathcal{D}}$, satisfying the triangle identities $U\varepsilon \circ \eta U = 1_U$ and $\varepsilon F \circ F\eta = 1_F$. The induced [[Def - Monad and Comonad|monad]] is $(T, \eta, \mu)$ with $T = UF$; the whiskered counit $U\varepsilon F : UFUF \Rightarrow UF$ serves as the multiplication $\mu$. The full symbol registry is on [[Category Theory V — Monads, Algebras, and Monoidal Categories]].

---

# Statement

> **Theorem (the monad of an adjunction).** Let $F \dashv U$ be an adjunction with $F : \mathcal{C} \to \mathcal{D}$, $U : \mathcal{D} \to \mathcal{C}$, unit $\eta : 1_{\mathcal{C}} \Rightarrow UF$ and counit $\varepsilon : FU \Rightarrow 1_{\mathcal{D}}$. Then the triple
> $$T = UF, \qquad \eta : 1_{\mathcal{C}} \Rightarrow T, \qquad \mu = U\varepsilon F : T^2 = UFUF \Rightarrow UF = T$$
> is a [[Def - Monad and Comonad|monad]] on $\mathcal{C}$.

> **Corollary (the comonad, dual form).** The same adjunction induces a comonad $(G, \varepsilon, \delta)$ on $\mathcal{D}$ with $G = FU$, counit $\varepsilon$, and comultiplication $\delta = F\eta U : FU \Rightarrow FUFU$.

The two statements are exact mirror images: replacing the adjunction by its opposite $U^{op} \dashv F^{op}$ between $\mathcal{D}^{op}$ and $\mathcal{C}^{op}$ turns the monad into the comonad.

---

# Motivation

This theorem is the supply line for the entire theory of monads. Monads are not usually presented by writing down an endofunctor and verifying three coherence diagrams by hand; they *arise*, almost always, from an [[Def - Adjunction|adjunction]] — and adjunctions are everywhere, since every free construction, every reflective subcategory, and every Galois connection is one. The theorem says that the moment you have a free–forgetful pair, you have a monad for free, with no axiom-checking required.

Conceptually, the theorem formalizes the "shadow" picture from the chapter's motivation. An adjunction lives across two categories, $\mathcal{C}$ and $\mathcal{D}$. Standing in $\mathcal{C}$ and refusing to look at $\mathcal{D}$, you can still see the composite $UF$, the unit $\eta$, and one whiskered piece of the counit, $U\varepsilon F$. The theorem says these three pieces of visible data already satisfy the monad axioms — the structure on $\mathcal{C}$ is self-consistent even though the rest of the adjunction is hidden. That is why the monad is "what the forgetful functor remembers": it is precisely the part of the adjunction that survives the projection onto the base category.

The companion comonad explains why comonads, though less famous, are equally natural: they are the *same* shadow cast on the *other* category. Where the monad on $\mathcal{C}$ packages free algebraic structure, the comonad on $\mathcal{D}$ packages the cofree, observational structure that drives descent.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's precondition is "an adjunction." The skill is recognizing adjunctions in disguise, because any of them then hands you a monad.

A first disguised source is **a free construction with a forgetful functor**. Whenever a category $\mathcal{D}$ of structured objects has a forgetful functor $U : \mathcal{D} \to \mathcal{C}$ admitting a left adjoint $F$ (the "free object"), you are in an adjunction. The non-obvious step is recognizing that the universal property of the free object — "maps out of $F X$ correspond to maps out of $X$" — *is* the adjunction isomorphism $\mathcal{D}(FX, D) \cong \mathcal{C}(X, UD)$. *Example problem:* the free group, free module, free monoid each give a forgetful functor with a left adjoint, hence the free-group, free-module, free-monoid monads.

A second disguised source is **a reflective subcategory**. If $\mathcal{D} \hookrightarrow \mathcal{C}$ is a [[Def - Reflective Subcategory|reflective subcategory]] — a full subcategory whose inclusion has a left adjoint (the reflector) — then the inclusion-and-reflector pair is an adjunction, and the induced monad is **idempotent** ($\mu$ is an isomorphism). The non-obviousness is that "localization" or "completion" or "sheafification" are all reflectors, hence all give monads. *Example problem:* sheafification on a site is the reflector into sheaves; the associated monad's algebras are the sheaves.

A third disguised source is **a Galois connection between posets**. An order-preserving pair $f \dashv g$ between posets, with $f(x) \leq y \iff x \leq g(y)$, is an adjunction between the posets viewed as categories. The induced monad is a **closure operator** $gf$: monotone, inflationary, idempotent. The non-obvious bridge is that "closure" in topology, algebra, and logic is uniformly a monad on a poset. *Example problem:* the topological closure operator $\overline{(-)}$ on subsets of a space is the monad of the Galois connection between subsets and closed sets.

**Targets (Output Amplification)**

The bare conclusion is "a monad $(UF, \eta, U\varepsilon F)$." Combined with the rest of the chapter it does much more.

Combine with **the comparison functor**. Once you have the monad $T$, there is a canonical functor $K : \mathcal{D} \to \mathcal{C}^T$ into the [[Def - Algebra for a Monad|Eilenberg–Moore category]] sending $D \mapsto (UD, U\varepsilon_D)$. The further result is the question of **monadicity**: whether $K$ is an equivalence, answered by [[Thm - The Barr-Beck Monadicity Theorem|Barr–Beck]]. So the monad is not just an invariant of the adjunction — it is the gateway to reconstructing $\mathcal{D}$ from $\mathcal{C}$.

Combine with **idempotency detection**. If you can show the multiplication $\mu = U\varepsilon F$ is a natural isomorphism, the monad is idempotent, and idempotent monads correspond exactly to [[Def - Reflective Subcategory|reflective subcategories]]; their algebras are the "local" objects. The further result is that "is this a localization?" reduces to "is $\mu$ invertible?", a checkable condition.

Combine with **the dual comonad and descent**. Applying the theorem to the *same* adjunction on the other side produces a comonad $FU$ on $\mathcal{D}$. The further result, via comonadic [[Thm - The Barr-Beck Monadicity Theorem|Barr–Beck]], is a descent statement: when $U$ is comonadic, $\mathcal{C}$ is recovered as comodules over $FU$. This is how base change along a faithfully flat map yields descent.

---

# Why Is It True

Forget the diagram-chase and picture the list monad coming from $\mathbf{Set} \rightleftarrows \mathbf{Mon}$. The endofunctor $T = UF$ sends a set to the underlying set of formal words. The unit $\eta$ includes generators as one-letter words. The counit $\varepsilon_M : FUM \to M$ at a monoid $M$ is "multiply out a formal word into an actual element of $M$." Whisker it: $U\varepsilon F$ takes a *word of words* (an element of $UFUF\,A = T^2 A$) and multiplies the inner free-monoid structure, producing a single word in $TA$. That is concatenation — the list monad's multiplication. So $\mu = U\varepsilon F$ is "evaluate one level of the free structure," and the monad axioms are the statement that this evaluation is associative and unital.

Why must they hold? Because the counit is *already* coherent — that coherence is exactly the triangle identities of the adjunction, plus the naturality of $\varepsilon$. The associativity of $\mu$ is the statement that the square

$$\begin{array}{ccc}
UFUFUF & \xrightarrow{\;UFU\varepsilon F\;} & UFUF \\
{\scriptstyle U\varepsilon FUF}\big\downarrow & & \big\downarrow{\scriptstyle U\varepsilon F} \\
UFUF & \xrightarrow{\;\;U\varepsilon F\;\;} & UF
\end{array}$$

commutes, and it commutes by the **naturality of the counit** $\varepsilon : FU \Rightarrow 1$ applied to the morphism $\varepsilon F : FUF \Rightarrow F$. The two unit laws of the monad are the two **triangle identities** of the adjunction, whiskered: $\mu \circ \eta T = U\varepsilon F \circ \eta UF$ is $U$ applied to one triangle, and $\mu \circ T\eta = U\varepsilon F \circ UF\eta$ is $U$ applied to the other.

**The whole theorem is: the monad axioms are the adjunction's triangle identities and counit-naturality, whiskered down to the base category.** Nothing new is proved; the coherence the adjunction already carried is simply read in the language of $\mathcal{C}$ alone.

---

# What Makes This Hard

The difficulty is entirely notational: keeping the **whiskerings straight**. The multiplication $\mu = U\varepsilon F$ is a natural transformation $UFUF \Rightarrow UF$, and the associativity square involves whiskering it on the left and right by $UF$, producing $UFU\varepsilon F$ versus $U\varepsilon FUF$ — two transformations $UFUFUF \Rightarrow UFUF$ that look almost identical but act on different layers. Most people stall by losing track of *where* in the string $UFUFUF$ the counit is being applied. The fix is to write each transformation as $U(\text{something})F$ and identify the "something" as a whiskering of $\varepsilon$, then apply naturality of $\varepsilon$ to the explicit morphism. The unit laws are easier but trip people who forget that the monad's unit *is* the adjunction's unit and the multiplication is built from the *counit*, not the unit.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Set $T = UF$, $\mu = U\varepsilon F$, keep $\eta$ as the adjunction unit. Prove the associativity square commutes by naturality of $\varepsilon$, and prove the two unit triangles commute by whiskering the adjunction's triangle identities with $U$ (on the left) and $F$ (on the right). Every step is "apply $U$ or whisker by $F$ to something the adjunction already gives you."

**Subgoal decomposition:**

1. **$T = UF$ is an endofunctor and $\mu, \eta$ are natural transformations of the right type.**
   - *Hint:* $UF : \mathcal{C} \to \mathcal{C}$; $\eta : 1 \Rightarrow UF$ is given; $U\varepsilon F$ whiskers $\varepsilon : FU \Rightarrow 1$ to $UFUF \Rightarrow UF$.
   - *Why needed:* The data must typecheck before any axiom can be stated.

2. **Associativity $\mu \circ T\mu = \mu \circ \mu T$.**
   - *Hint:* Both sides are transformations $UFUFUF \Rightarrow UF$. Write $T\mu = UF(U\varepsilon F) = UFU\varepsilon F$ and $\mu T = U\varepsilon FUF$; apply naturality of $\varepsilon$ to the morphism $\varepsilon F$.
   - *Why needed:* This is the first monad axiom.

3. **Left unit $\mu \circ T\eta = 1_T$.**
   - *Hint:* $T\eta = UF\eta$, so $\mu \circ T\eta = U\varepsilon F \circ UF\eta = U(\varepsilon F \circ F\eta) = U(1_F)$ by the triangle identity $\varepsilon F \circ F\eta = 1_F$.
   - *Why needed:* The first unit law.

4. **Right unit $\mu \circ \eta T = 1_T$.**
   - *Hint:* $\eta T = \eta UF$, so $\mu \circ \eta T = U\varepsilon F \circ \eta UF = (U\varepsilon \circ \eta U)F = (1_U)F$ by the triangle identity $U\varepsilon \circ \eta U = 1_U$.
   - *Why needed:* The second unit law; together with step 3 it completes the monad axioms.

---

# Lemma Decomposition

> [!note]- Lemma 1: Whiskering produces the multiplication of the right type
> **Statement:** $\mu := U\varepsilon F$ is a natural transformation $UFUF \Rightarrow UF$, i.e. $T^2 \Rightarrow T$ with $T = UF$.
>
> **Hint:** The counit $\varepsilon : FU \Rightarrow 1_{\mathcal{D}}$ whiskered on the left by $U$ and on the right by $F$ gives $U \varepsilon F : U(FU)F \Rightarrow U(1)F$, i.e. $UFUF \Rightarrow UF$.
>
> **Why needed:** Establishes that the multiplication is well-typed before the axioms are checked.
>
> > [!note]- Full proof
> > The counit is a natural transformation $\varepsilon : FU \Rightarrow 1_{\mathcal{D}}$ between endofunctors of $\mathcal{D}$, with component $\varepsilon_D : FUD \to D$. Whiskering on the right by $F : \mathcal{C} \to \mathcal{D}$ gives $\varepsilon F : FUF \Rightarrow F$ with component $(\varepsilon F)_A = \varepsilon_{FA} : FUFA \to FA$. Whiskering on the left by $U : \mathcal{D} \to \mathcal{C}$ gives $U\varepsilon F : UFUF \Rightarrow UF$ with component $(U\varepsilon F)_A = U(\varepsilon_{FA}) : UFUFA \to UFA$. Since $T = UF$, this is a natural transformation $T^2 \Rightarrow T$, as required. Naturality is inherited from naturality of $\varepsilon$ and functoriality of $U, F$.

> [!note]- Lemma 2: Associativity from naturality of the counit
> **Statement:** $U\varepsilon F \circ UFU\varepsilon F = U\varepsilon F \circ U\varepsilon FUF$ as transformations $UFUFUF \Rightarrow UF$.
>
> **Hint:** Apply the naturality square of $\varepsilon : FU \Rightarrow 1$ to the morphism $\varepsilon_{FA} : FUFA \to FA$ (equivalently to $\varepsilon F$), then whisker by $U$.
>
> **Why needed:** This is exactly the monad associativity axiom $\mu \circ T\mu = \mu \circ \mu T$.
>
> > [!note]- Full proof
> > Naturality of $\varepsilon$ at a morphism $h : D \to D'$ says $\varepsilon_{D'} \circ FUh = h \circ \varepsilon_D$. Take $h = \varepsilon_{FA} : FUFA \to FA$. Then naturality gives
> > $$\varepsilon_{FA} \circ FU(\varepsilon_{FA}) = \varepsilon_{FA} \circ \varepsilon_{FUFA}.$$
> > The left side is $(\varepsilon F)_A \circ (FU\varepsilon F)_A$ and the right side is $(\varepsilon F)_A \circ (\varepsilon FUF)_A$, both morphisms $FUFUFA \to FA$. Applying $U$ (which preserves composition) to this equation yields
> > $$U\varepsilon_{FA} \circ UFU\varepsilon_{FA} = U\varepsilon_{FA} \circ U\varepsilon_{FUFA},$$
> > which is precisely $(U\varepsilon F \circ UFU\varepsilon F)_A = (U\varepsilon F \circ U\varepsilon FUF)_A$, i.e. $\mu \circ T\mu = \mu \circ \mu T$ at $A$.

> [!note]- Lemma 3: Unit laws from the triangle identities
> **Statement:** $\mu \circ T\eta = 1_T = \mu \circ \eta T$.
>
> **Hint:** Whisker the two triangle identities $\varepsilon F \circ F\eta = 1_F$ and $U\varepsilon \circ \eta U = 1_U$ by $U$ and $F$ respectively.
>
> **Why needed:** These are the two monad unit axioms.
>
> > [!note]- Full proof
> > For the left unit law, $T\eta = UF\eta$ and so
> > $$\mu \circ T\eta = U\varepsilon F \circ UF\eta = U(\varepsilon F \circ F\eta) = U(1_F) = 1_{UF} = 1_T,$$
> > using the triangle identity $\varepsilon F \circ F\eta = 1_F$ and functoriality of $U$.
> >
> > For the right unit law, $\eta T = \eta UF$ and so
> > $$\mu \circ \eta T = U\varepsilon F \circ \eta UF = (U\varepsilon \circ \eta U)F = (1_U)F = 1_{UF} = 1_T,$$
> > using the triangle identity $U\varepsilon \circ \eta U = 1_U$ and that whiskering preserves identities.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $F \dashv U$ with unit $\eta : 1_{\mathcal{C}} \Rightarrow UF$ and counit $\varepsilon : FU \Rightarrow 1_{\mathcal{D}}$, satisfying the triangle identities
> $$U\varepsilon \circ \eta U = 1_U, \qquad \varepsilon F \circ F\eta = 1_F.$$
>
> **Step 0 — the data.** Set $T = UF : \mathcal{C} \to \mathcal{C}$, take $\eta : 1_{\mathcal{C}} \Rightarrow T$ as given, and define $\mu = U\varepsilon F : T^2 \Rightarrow T$. By Lemma 1 these are natural transformations of the stated types.
>
> **Step 1 — associativity.** We must show $\mu \circ T\mu = \mu \circ \mu T$ as transformations $T^3 \Rightarrow T$. By Lemma 2, this follows from naturality of $\varepsilon$ applied to $\varepsilon F$, whiskered by $U$. Explicitly, for each object $A$, naturality of $\varepsilon$ at $\varepsilon_{FA}$ gives $\varepsilon_{FA} \circ FU\varepsilon_{FA} = \varepsilon_{FA}\circ \varepsilon_{FUFA}$; applying $U$ yields the associativity equation at $A$.
>
> **Step 2 — unit laws.** By Lemma 3, $\mu \circ T\eta = U(\varepsilon F \circ F\eta) = U(1_F) = 1_T$ and $\mu \circ \eta T = (U\varepsilon \circ \eta U)F = (1_U)F = 1_T$, each a whiskered triangle identity.
>
> **Step 3 — conclude.** Associativity and both unit laws hold, so $(T, \eta, \mu) = (UF, \eta, U\varepsilon F)$ is a monad on $\mathcal{C}$.
>
> **Dual statement.** Applying the above to the opposite adjunction (or dualizing directly) shows $(FU, \varepsilon, F\eta U)$ is a comonad on $\mathcal{D}$: coassociativity is naturality of $\eta$ whiskered by $F$, and the counit laws are the same triangle identities whiskered the other way. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The double-dualization monad in linear algebra.** The functor $V \mapsto V^{**}$ on [[Def - Vector Space|vector spaces]] arises from the adjunction $(-)^* \dashv (-)^*$ (the dual-space functor is adjoint to itself, contravariantly). The induced monad's unit is the canonical map $V \to V^{**}$, and its algebras are the reflexive spaces. The non-obvious recognition is that a self-adjoint contravariant functor still produces a (covariant) monad on the double composite.

**The ultrafilter monad and compact Hausdorff spaces.** The functor $\beta : \mathbf{Set} \to \mathbf{Set}$ sending a set to its set of ultrafilters is a monad (the codensity monad of the inclusion of finite sets, or the monad of the adjunction with compact Hausdorff spaces). Its algebras are exactly compact Hausdorff spaces — a striking instance where a purely set-theoretic monad reconstructs a topological category. Recognizing $\beta$ as monadic is the content of Manes' theorem.

**Closure operators in logic and topology.** Any Galois connection — between subsets and closed sets, between sets of formulas and their consequences, between subgroups and fixed fields — is an adjunction of posets, and the induced monad is the corresponding closure operator (topological closure, deductive closure, Galois closure). The exercise is to recognize that "closure" across these fields is one construction, the monad of a Galois connection.

---

# Bridges

- **[[Thm - Eilenberg-Moore and Kleisli Realize a Monad|Eilenberg–Moore and Kleisli realize a monad]]** — the converse. This theorem says every adjunction gives a monad; the converse says every monad *comes from* an adjunction, in two canonical ways (Kleisli and Eilenberg–Moore), which are the initial and terminal resolutions. Together they make "monad" and "adjunction-up-to-resolution" two views of one phenomenon.

- **[[Thm - The Barr-Beck Monadicity Theorem|Barr–Beck monadicity]]** — the next question. Given the monad $T = UF$, there is a comparison $\mathcal{D} \to \mathcal{C}^T$; Barr–Beck decides when it is an equivalence, i.e. when $\mathcal{D}$ is *recovered* from the monad. The present theorem builds the monad; Barr–Beck audits how much it remembers.

- **[[Def - Reflective Subcategory|Reflective subcategories]] and idempotent monads** — a special case. When the adjunction is a reflection (the right adjoint is a fully faithful inclusion), the counit is an isomorphism, so $\mu = U\varepsilon F$ is invertible and the monad is idempotent. Idempotent monads correspond exactly to reflective subcategories, and their algebras are the local objects (sheaves, complete objects, localizations).

- **[[Thm - Right Adjoints Preserve Limits|Right adjoints preserve limits]]** — a companion fact about $U$. Since $U$ is a right adjoint it preserves limits, which is why the forgetful functor $U^T : \mathcal{C}^T \to \mathcal{C}$ creates limits and the Eilenberg–Moore category inherits limits from the base — the structural reason algebra categories are complete.

---

# Unlocked by This

> [!tip] Descent and Comonadicity *(from Algebraic Geometry)*
> The dual comonad $FU$ is the engine of **descent**: for a faithfully flat ring map, base change is comonadic, and modules descend along it. The present theorem manufactures the comonad whose coalgebras are the descent data.

> [!tip] The Bar Construction and Monadic Cohomology *(from Higher Algebra)*
> Iterating the multiplication of $T = UF$ produces the **bar resolution**, a simplicial object whose totalization computes derived functors and monadic (co)homology — the entry point to **derived** and homotopical algebra.
