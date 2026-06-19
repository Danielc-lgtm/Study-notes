---
type: exercise
subject: category-theory
difficulty: "⭐"
prereqs:
  - "Def - Functor"
  - "Def - Opposite Category and Duality"
tags: [category-theory, foundations]
---

# Problem Statement

Verify that the two power-set constructions are [[Def - Functor|functors]], with opposite variance.

1. **Covariant power set.** $P : \mathbf{Set} \to \mathbf{Set}$, with $P(X)$ the set of subsets of $X$, and for $f : X \to Y$ the map $P(f) : P(X) \to P(Y)$ given by **direct image** $A \mapsto f(A) = \{f(a) : a \in A\}$. Show $P$ preserves identities and composition.

2. **Contravariant power set.** $P^{\bullet} : \mathbf{Set}^{\mathrm{op}} \to \mathbf{Set}$, with $P^{\bullet}(X) = P(X)$ and for $f : X \to Y$ the map $P^{\bullet}(f) : P(Y) \to P(X)$ given by **preimage** $B \mapsto f^{-1}(B) = \{x : f(x) \in B\}$. Show $P^{\bullet}$ preserves identities and reverses composition, $P^{\bullet}(g \circ f) = P^{\bullet}(f) \circ P^{\bullet}(g)$.

Explain why preimage gives a *contravariant* functor while direct image gives a *covariant* one.

**Recall:**

![[Def - Functor#The Definition]]

A [[Def - Functor|contravariant functor]] $\mathbf{Set} \to \mathbf{Set}$ is a functor $\mathbf{Set}^{\mathrm{op}} \to \mathbf{Set}$, sending $f : X \to Y$ to a map $P(Y) \to P(X)$ and reversing composition.

---

# Convergent Strategy

**Problem class:** This is a "verify functoriality" exercise — checking the two functor axioms (identities, composition) for a given object-and-morphism assignment, while diagnosing the variance.

**Assumption pattern:** Everything is a computation with sets and functions. Direct image composes covariantly because applying $g$ to $f(A)$ gives $(g \circ f)(A)$; preimage reverses because pulling $B$ back through $g$ then $f$ gives $(g \circ f)^{-1}(B)$ but in the order $f^{-1}(g^{-1}(B))$.

**Theorem routing:** No external theorem; the proof is the two set-identities $g(f(A)) = (gf)(A)$ and $f^{-1}(g^{-1}(B)) = (gf)^{-1}(B)$, plus the trivial identity-preservation.

**Key decision point:** The conceptual content is reading off the variance from the *order in which composition unwinds*: forward maps push subsets forward in the same direction (covariant); preimage pulls subsets backward, and chaining two pullbacks reverses the order (contravariant). The decision is to track which direction the subset travels.

---

# Legal Operations Used

1. **Operation: check the two functor axioms** (topic page, Legal Operation 7). For each construction, verify $F(1) = 1$ and the composition law (covariant or contravariant).

2. **Operation: diagnose variance from composition order** (topic page, Legal Operation 8). The order in which the chained map unwinds determines covariant versus contravariant.

---

# Hints

> [!note]- Hint 1
> For $P$: compute $P(g \circ f)(A) = (g \circ f)(A)$ and compare with $P(g)(P(f)(A)) = g(f(A))$. Are they equal?

> [!note]- Hint 2
> For $P^{\bullet}$: compute $(g \circ f)^{-1}(B)$ and compare with $f^{-1}(g^{-1}(B))$. Note the order of $f^{-1}$ and $g^{-1}$.

> [!note]- Hint 3
> Variance is about *which way the subset travels*. Direct image of $A \subseteq X$ lands in $Y$ (forward, covariant). Preimage of $B \subseteq Y$ lands in $X$ (backward, contravariant).

---

# Solution

The plan: verify identity-preservation for both (trivial), then the composition law for $P$ (covariant, via $g(f(A)) = (gf)(A)$) and for $P^{\bullet}$ (contravariant, via $f^{-1}(g^{-1}(B)) = (gf)^{-1}(B)$). The variance is read off the composition order.

**Step 1: $P$ is a covariant functor.**

> [!note]- Derivation
> *Identities.* $P(1_X)(A) = 1_X(A) = \{1_X(a) : a \in A\} = A$, so $P(1_X) = 1_{P(X)}$. *Composition.* For $f : X \to Y$, $g : Y \to Z$, and $A \subseteq X$,
> $$P(g \circ f)(A) = (g \circ f)(A) = \{g(f(a)) : a \in A\} = g\big(\{f(a) : a \in A\}\big) = g(f(A)) = P(g)\big(P(f)(A)\big).$$
> So $P(g \circ f) = P(g) \circ P(f)$, the covariant composition law. Hence $P : \mathbf{Set} \to \mathbf{Set}$ is a [[Def - Functor|functor]].

**Step 2: $P^{\bullet}$ is a contravariant functor.**

> [!note]- Derivation
> *Identities.* $P^{\bullet}(1_X)(A) = 1_X^{-1}(A) = A$, so $P^{\bullet}(1_X) = 1_{P(X)}$. *Composition (reversed).* For $f : X \to Y$, $g : Y \to Z$, and $B \subseteq Z$,
> $$P^{\bullet}(g \circ f)(B) = (g \circ f)^{-1}(B) = \{x : g(f(x)) \in B\} = \{x : f(x) \in g^{-1}(B)\} = f^{-1}\big(g^{-1}(B)\big) = P^{\bullet}(f)\big(P^{\bullet}(g)(B)\big).$$
> So $P^{\bullet}(g \circ f) = P^{\bullet}(f) \circ P^{\bullet}(g)$ — composition reverses. This is exactly functoriality of $P^{\bullet} : \mathbf{Set}^{\mathrm{op}} \to \mathbf{Set}$ (in $\mathbf{Set}^{\mathrm{op}}$ the composite of $f$ and $g$ is taken in reversed order, so $P^{\bullet}$ preserves *that* composition).

**Step 3: Why the variances differ.**

> [!note]- Derivation
> A subset $A \subseteq X$ is "data living on $X$". Direct image transports data *along* the map $f : X \to Y$ — forward — so chaining $X \to Y \to Z$ transports forward through both, in the same order: covariant. Preimage transports data *against* the map — a subset of the codomain is pulled back to the domain — so chaining $X \to Y \to Z$ pulls a subset of $Z$ first back to $Y$ (via $g^{-1}$) then back to $X$ (via $f^{-1}$), reversing the order: contravariant. The general principle: *evaluation/pushforward is covariant, pullback/precomposition is contravariant.*

> [!note]- Complete formal solution
> *Covariant $P$:* $P(1_X) = 1_{P(X)}$ since $1_X(A) = A$; and $P(gf)(A) = (gf)(A) = g(f(A)) = P(g)P(f)(A)$.
>
> *Contravariant $P^{\bullet}$:* $P^{\bullet}(1_X) = 1_{P(X)}$ since $1_X^{-1}(A) = A$; and $P^{\bullet}(gf)(B) = (gf)^{-1}(B) = f^{-1}(g^{-1}(B)) = P^{\bullet}(f)P^{\bullet}(g)(B)$, so composition reverses.
>
> Direct image transports subsets forward (covariant); preimage transports them backward, reversing chained composition (contravariant). $\blacksquare$

---

# Key Takeaways

**Pushforward is covariant, pullback is contravariant — memorize the slogan.** The single most transferable lesson is the variance heuristic: any construction that *moves data along* a map (direct image, induced map on homology, the functor $\mathcal{C}(A, -)$ given by post-composition) is covariant, while any construction that *pulls data back against* a map (preimage, the [[Def - Dual Space|dual space]] via precomposition, restriction of functions, [[Def - Functor|Spec]]) is contravariant. When you meet a new assignment and need its variance, ask "does a map $X \to Y$ send my data forward to $Y$ or backward to $X$?" The forward answer is covariant, the backward answer contravariant; this resolves the question instantly and almost never fails.

**Preimage is the better-behaved of the two operations.** A practical and deep point: $P^{\bullet}$ (preimage) commutes with unions, intersections, and complements — $f^{-1}(\bigcup B_i) = \bigcup f^{-1}(B_i)$, $f^{-1}(B^c) = f^{-1}(B)^c$ — whereas the direct image $P$ only respects unions, not intersections or complements. This is why preimage is the operation that appears in the definition of continuity, measurability, and pullback of sheaves: the contravariant power set is a lattice homomorphism while the covariant one is not. When a construction needs to respect Boolean structure, it will be the contravariant pullback, not the covariant pushforward.

**Variance is forced by the construction, not chosen.** Beginners sometimes imagine variance is a stylistic convention; it is not. The power-set example shows that the *same* underlying object-assignment $X \mapsto P(X)$ supports two genuinely different functors of opposite variance, distinguished entirely by what they do to morphisms. The lesson is that "functor" is morphism-data first and object-data second, and a construction's variance is dictated by the only sensible way its morphism-action can be defined. Whenever an object-assignment admits an action on maps in one direction but not the other, the variance is determined, and trying to force the wrong variance produces a non-functor.
