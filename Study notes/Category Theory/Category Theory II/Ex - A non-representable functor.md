---
type: exercise
subject: category-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Hom-Functor and Representable Functor"
  - "Def - Category of Elements"
  - "Def - Limit and Colimit"
tags: [category-theory, foundations]
---

# Problem Statement

1. Show that the **covariant power-set functor** $\mathcal{P} : \mathbf{Set} \to \mathbf{Set}$ — sending a set $X$ to its power set $\mathcal{P}(X)$ and a function $f : X \to Y$ to the *direct-image* map $\mathcal{P}(f)(S) = f(S)$ — is **not representable**.
2. Give two independent proofs: (a) a cardinality / limit-preservation argument; (b) a category-of-elements argument showing $\int \mathcal{P}$ has no initial object.
3. Contrast with the *contravariant* power-set functor (using preimages), which **is** representable by the two-element set.

**Recall:**

![[Def - Hom-Functor and Representable Functor#The Definition]]

A functor $F : \mathcal{C} \to \mathbf{Set}$ is [[Def - Hom-Functor and Representable Functor|representable]] if $F \cong \mathcal{C}(A, -)$ for some $A$. A representable functor preserves all [[Def - Limit and Colimit|limits]] (it is continuous). By the [[Def - Category of Elements|category-of-elements]] criterion, $F$ is representable iff $\int F$ has an initial object (covariant case).

---

# Convergent Strategy

**Problem class:** This is a *non-representability* exercise — a refutation rather than a construction. The topic page's strategy for refutations is to find a structural property that every representable functor must have and exhibit that the given functor violates it; the two standard obstructions are limit-preservation and the existence of an initial object in the category of elements.

**Assumption pattern:** The functor $\mathcal{P}$ acts by *direct image*, which is the assumption that breaks everything: direct image does not preserve the limits a hom-functor would, and it forbids a generic element from generating all subsets by pushforward. The pattern to recognize is "the functor's action is a pushforward / image, not a pullback", which is exactly when covariant set-valued functors tend to fail representability.

**Theorem routing:** Two routes. (a) A representable $\mathbf{Set}(A, -)$ preserves limits and has $|\mathbf{Set}(A, X)| = |X|^{|A|}$; comparing with $|\mathcal{P}(X)| = 2^{|X|}$ across varying $X$ rules out any fixed $A$. (b) By the [[Def - Category of Elements]] criterion, representability is equivalent to $\int \mathcal{P}$ having an initial object; we show none exists by exhibiting an object with no morphism out, or two with no common factorization.

**Key decision point:** The crux is choosing the right obstruction and the right test sets. The cardinality argument needs you to vary $X$ so that $2^{|X|}$ outruns $|X|^{|A|}$ for every fixed $A$. The category-of-elements argument needs you to see that a "generic subset" $(A, S_0)$ would have to push forward, under direct image, to *every* subset of *every* set uniquely — and direct images cannot do this, because direct image can only ever produce a subset of size at most $|S_0|$.

---

# Legal Operations Used

1. **Operation 4 from the topic page (refute representability via a broken limit or a cardinality count).** A representable functor preserves limits and has hom-set cardinality $|X|^{|A|}$; $\mathcal{P}$ violates this.

2. **Operation 7 from the topic page (test representability via the category of elements).** We use that $F$ is representable iff $\int F$ has an initial object, and show $\int \mathcal{P}$ has none.

---

# Hints

> [!note]- Hint 1
> Suppose $\mathcal{P} \cong \mathbf{Set}(A, -)$. Then $|\mathcal{P}(X)| = |\mathbf{Set}(A, X)|$ for all $X$. Compute both as functions of $|X|$.

> [!note]- Hint 2
> $|\mathcal{P}(X)| = 2^{|X|}$ and $|\mathbf{Set}(A, X)| = |X|^{|A|}$. Can a single cardinal $|A|$ make $|X|^{|A|} = 2^{|X|}$ for *all* $X$? Test $|X| = 1$ and $|X| = 2$.

> [!note]- Hint 3
> Category-of-elements route: an object of $\int \mathcal{P}$ is a pair $(X, S)$ with $S \subseteq X$. An initial object $(A, S_0)$ would give, for each $(X, S)$, a *unique* $f : A \to X$ with the direct image $f(S_0) = S$. Why is this impossible?

> [!note]- Hint 4
> Direct image $f(S_0)$ has cardinality at most $|S_0|$. So no fixed $(A, S_0)$ can hit arbitrarily large subsets $S$; and even for small $S$ uniqueness fails. Contrast: preimage $f^{-1}$ can produce any subset, which is why the *contravariant* power-set functor is representable by $\{0,1\}$.

---

# Solution

The plan is to assume representability and derive a contradiction two ways. The cardinality argument shows no fixed $A$ can match $2^{|X|}$ across all $X$. The category-of-elements argument shows the generic subset would have to generate every subset by direct image, which is impossible. The contravariant functor escapes both obstructions because preimage is flexible enough.

**Step 1: Cardinality / limit obstruction.**

> [!note]- Derivation
> Suppose $\mathcal{P} \cong \mathbf{Set}(A, -)$ for some set $A$. Comparing cardinalities at each $X$, $2^{|X|} = |\mathcal{P}(X)| = |\mathbf{Set}(A, X)| = |X|^{|A|}$. Test $|X| = 1$: left side $2^1 = 2$, right side $1^{|A|} = 1$. Already $2 \neq 1$, a contradiction. (Equivalently, $\mathcal{P}$ fails to preserve the terminal object: $\mathcal{P}(\{*\}) = \{\emptyset, \{*\}\}$ has two elements, but a representable functor sends the terminal object $\{*\}$ to $\mathbf{Set}(A, \{*\})$, a singleton. A representable functor preserves limits, in particular terminal objects; $\mathcal{P}$ does not.) Hence $\mathcal{P}$ is not representable.

**Step 2: Category-of-elements obstruction.**

> [!note]- Derivation
> By the [[Def - Category of Elements]] criterion, $\mathcal{P}$ is representable iff $\int \mathcal{P}$ has an initial object. Objects of $\int \mathcal{P}$ are pairs $(X, S)$ with $S \subseteq X$; a morphism $(X, S) \to (Y, T)$ is a function $f : X \to Y$ with $\mathcal{P}(f)(S) = f(S) = T$. An initial object $(A, S_0)$ would provide, for every $(X, S)$, a unique $f : A \to X$ with $f(S_0) = S$. But the direct image $f(S_0)$ has cardinality at most $|S_0|$, so any $S$ with $|S| > |S_0|$ cannot be hit — existence fails. (And if $|S_0| \geq 1$, mapping $S_0$ onto a one-element $S$ can be done by many distinct $f$, so uniqueness fails too.) Thus $\int \mathcal{P}$ has no initial object, and $\mathcal{P}$ is not representable.

**Step 3: The contravariant power-set functor is representable.**

> [!note]- Derivation
> Let $\mathcal{P} : \mathbf{Set}^{op} \to \mathbf{Set}$ act by *preimage*: $\mathcal{P}(f)(T) = f^{-1}(T)$ for $f : X \to Y$. It is representable by $\Omega = \{0, 1\}$: a subset $S \subseteq X$ corresponds to its characteristic function $\chi_S : X \to \Omega$ with $\chi_S^{-1}(\{1\}) = S$, giving a natural bijection $\mathbf{Set}(X, \Omega) \cong \mathcal{P}(X)$. The escape from the obstructions: preimage $f^{-1}(\{1\})$ can be *any* subset of the domain (choose $\chi$ freely), so the universal element $\{1\} \in \mathcal{P}(\Omega)$ does generate every subset uniquely. This is exactly the difference between pushforward (rigid, bounded in size) and pullback (flexible). See [[Ex - Universal element of the power-set functor]].

> [!note]- Complete formal solution
> If $\mathcal{P} \cong \mathbf{Set}(A, -)$ then $2^{|X|} = |X|^{|A|}$ for all $X$; at $|X| = 1$ this is $2 = 1$, false — equivalently $\mathcal{P}$ fails to preserve the terminal object, which every representable functor preserves. Independently, $\int \mathcal{P}$ has no initial object: a candidate $(A, S_0)$ cannot push $S_0$ forward by direct image onto subsets larger than $|S_0|$ (existence fails) and pushes onto small subsets non-uniquely (uniqueness fails). So the covariant power-set functor is not representable. By contrast the contravariant power-set functor, acting by preimage, is representable by $\Omega = \{0,1\}$ via characteristic functions, because preimage can realize any subset uniquely. $\blacksquare$

---

# Key Takeaways

**To refute representability, hit it with limit-preservation or the category-of-elements criterion.** Representable functors are continuous (they preserve all limits) and have a generic element generating everything; a functor failing either is not representable. The fastest refutation is usually "does it preserve the terminal object?" — a representable functor sends $\{*\}$ to a singleton, so a functor with $|F(\{*\})| \geq 2$ is immediately disqualified. The covariant power set fails this on sight: $\mathcal{P}(\{*\})$ has two elements. The trigger is any covariant $\mathbf{Set}$-valued functor whose value at a one-point set is bigger than a point; the reaction is "not representable".

**Covariance + pushforward is the danger zone; contravariance + pullback is the safe zone.** The single structural reason the covariant power-set functor fails while the contravariant one succeeds is that direct image $f(S)$ is *rigid* — bounded in cardinality by $|S|$, and often non-unique — whereas preimage $f^{-1}(T)$ is *flexible* — able to produce any subset uniquely by choosing the classifying function. This is a recurring pattern: functors that act by pulling structure back (preimage, restriction, substitution) tend to be representable, while functors that push structure forward (image, quotient, free generation) tend to be the *left adjoints* whose representability you should not expect. When deciding whether to even attempt a representation, check the variance and the direction of the action first.

**Non-representability is informative, not a dead end — it points toward an adjoint or a colimit.** The covariant power set is not representable, but it is the underlying functor of a monad (the power-set monad) and is closely tied to colimits and free constructions. A failure of representability often means the functor is better understood as a left adjoint, or as preserving *colimits* rather than limits. Recognizing "this functor preserves colimits but not limits, so look for a right adjoint or a representing object on the opposite side" reorients you productively, and is the bridge from this exercise to the adjunctions developed in Category Theory IV.
