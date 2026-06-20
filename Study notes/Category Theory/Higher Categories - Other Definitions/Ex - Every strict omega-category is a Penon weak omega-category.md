---
type: exercise
subject: higher-categories
difficulty: "⭐"
prereqs:
  - "Def - Penon Weak ω-Category"
  - "Def - Monad and Comonad"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

Let $Q$ be a strict ω-category, with underlying reflexive globular set $UQ$. Show that $UQ$ carries the structure of a **[[Def - Penon Weak ω-Category|Penon weak ω-category]]** — that is, exhibit an $H$-algebra structure $\theta : H(UQ) \to UQ$ — and verify the two algebra axioms. Conclude that every strict ω-category is, canonically, a Penon weak ω-category, and that this assignment is functorial.

**Recall:**

A **reflexive globular set** is a sequence of sets $X_0, X_1, \dots$ with source/target maps $s, t : X_{n+1} \to X_n$ satisfying $ss = st$, $ts = tt$, and identity-insertion maps $i : X_n \to X_{n+1}$. A **strict ω-category** is such a thing with strictly associative, strictly unital composition operations in every dimension, satisfying the strict interchange law.

A **[[Def - Penon Weak ω-Category|Penon weak ω-category]]** is an algebra for the **Penon monad** $(H, \eta, \mu)$ on reflexive globular sets. Concretely, $HX$ is the reflexive globular set underlying the *universal stretching* on $X$ — a strict ω-category $Q_X$ together with an identity-on-cells comparison $HX \to Q_X$ equipped with a contraction (chosen connecting cells for parallel cells identified in $Q_X$).

![[Def - Penon Weak ω-Category#The Definition]]

An algebra for a **[[Def - Monad and Comonad|monad]]** $(H,\eta,\mu)$ is an object $X$ with a map $\theta : HX \to X$ satisfying the unit law $\theta \circ \eta_X = \mathrm{id}_X$ and the associativity law $\theta \circ H\theta = \theta \circ \mu_X$.

---

# Convergent Strategy

**Problem class:** This is a "the rigid object is a special weak object" problem — the higher-categorical analogue of "every abelian group is a group" or "every strict monoidal category is a monoidal category". The routine is to take the strict operations as the source of the chosen weak composites, and to send all the genuinely-weak coherence data (the contraction cells) to identities, which is exactly what strictness makes possible.

**Assumption pattern:** The crucial assumption is that $Q$ is *strict*: its composites are honest values and its associativity/unit/interchange laws are *equalities*, not coherence cells. This is what lets the contraction cells — which exist precisely to witness *inequalities* that become equalities in the strict world — be sent to identities. Strictness is doing all the work.

**Theorem routing:** The route is to use the universal property of the universal stretching. By construction $H(UQ) \to Q_{UQ}$ is the universal stretching on $UQ$; but $Q$ *itself* is a strict ω-category receiving an identity-on-cells map from $UQ$ (the identity), so by universality there is a unique map of stretchings from the universal one to the stretching $(UQ, \mathrm{id}, UQ \to Q)$. The underlying globular-set map is the desired $\theta : H(UQ) \to UQ$. The algebra axioms are then forced by the uniqueness in the universal property.

**Key decision point:** The non-obvious choice is to realise that $Q$, viewed as a stretching *over its own underlying globular set* (with the comparison map the identity), is a legitimate target for the universal property — and that the resulting structure map is automatically an $H$-algebra. The naive alternative, "write down a formula for $\theta$ on each freely-generated composite", works but is laborious; the universal-property route gives the axioms for free.

---

# Legal Operations Used

1. **Operation 4 from the topic page (take algebras for a monad).** We produce a Penon weak ω-category by exhibiting the $H$-algebra structure on $UQ$, i.e. a structure map $H(UQ) \to UQ$ satisfying the algebra laws.

2. **Operation 3 from the topic page (build a contraction), in degenerate form.** The contraction on the universal stretching is sent, under $\theta$, to *identity* cells, because in the strict $Q$ all parallel cells that are identified really are equal, so no nontrivial connecting cell is needed.

3. **Operation 8 from the topic page (truncate / specialise to a known case).** Recognising that the strict ω-categories are the "all coherence cells are identities" special case of the weak ones is the conceptual content.

---

# Hints

> [!note]- Hint 1
> Every algebra-for-a-monad question can be answered by a universal property if the monad is a *free* construction. The Penon monad $H$ comes from the *universal* (free) stretching. What strict ω-category, equipped with an identity-on-cells comparison from $UQ$, is staring you in the face?

> [!note]- Hint 2
> Use $Q$ itself. The pair $(UQ \xrightarrow{\mathrm{id}} UQ \to Q)$ — where the second map is $\mathrm{id}_{UQ}$ viewed as identity-on-cells into the strict $Q$ — is a stretching over $UQ$, with the contraction sending each "to-be-connected" pair of parallel cells (equal in $Q$) to an identity. Map the *universal* stretching into it.

> [!note]- Hint 3
> The unit and associativity axioms for $\theta$ are both consequences of *uniqueness* in the universal property: $\theta \circ \eta_{UQ}$ and $\mathrm{id}_{UQ}$ are both maps of stretchings out of the universal one with the same underlying behaviour, so they coincide; similarly $\theta \circ H\theta$ and $\theta \circ \mu_{UQ}$ are forced equal.

---

# Solution

The proof has three steps. Step 1 presents $Q$ as a stretching over its own underlying globular set. Step 2 extracts $\theta$ from the universal property and identifies it concretely as "evaluate the formal composite, send coherence cells to identities". Step 3 deduces the algebra axioms from uniqueness. The whole argument is the observation that strictness collapses the contraction data to identities.

**Step 1: $Q$ is a stretching over $UQ$, with trivial contraction.**

> [!note]- Derivation
> A stretching over a reflexive globular set $X$ is a triple $(M, X \to M, M \to Q')$ with $Q'$ a strict ω-category, $M \to Q'$ identity-on-cells, and a contraction. Take $X = M = UQ$, the map $X \to M$ the identity, and $M \to Q'$ the identity-on-cells map $UQ \to Q$ (which is literally the identity on the underlying globular set, since $UQ$ *is* the underlying globular set of $Q$). For the contraction: whenever two parallel cells $a, b \in UQ_n$ become equal in $Q$ — but $UQ \to Q$ is the identity on cells, so "equal in $Q$" means $a = b$ already — the required connecting cell is the *identity* (degenerate) cell $i(a) = i(b)$ on $a = b$. Thus $(UQ, \mathrm{id}, UQ \to Q)$ is a genuine stretching over $UQ$, with the contraction entirely degenerate. This is where strictness is used: in a *weak* target the cells $a, b$ could be distinct yet identified, forcing a nondegenerate connecting cell; strictness makes them equal, so the connecting cell is an identity.

**Step 2: $\theta : H(UQ) \to UQ$ is the universal comparison.**

> [!note]- Derivation
> By definition $H(UQ)$ is the reflexive globular set underlying the *universal* (initial) stretching $(\,UQ \xrightarrow{\eta} H(UQ) \to Q_{UQ}\,)$ over $UQ$. Initiality means: for *any* stretching over $UQ$, there is a unique morphism of stretchings from the universal one to it. Applying this to the stretching from Step 1 yields a unique map of stretchings, whose underlying globular-set map is
> $$\theta : H(UQ) \longrightarrow UQ.$$
> Concretely $\theta$ does exactly what one expects: a cell of $H(UQ)$ is a formal weak composite of cells of $UQ$ together with coherence data; $\theta$ evaluates the formal composite using the *strict* operations of $Q$ (which exist and are unambiguous), and sends each coherence/contraction cell to the corresponding identity in $UQ$ (legitimate because the cells it connects are equal in $Q$).

**Step 3: the algebra axioms hold.**

> [!note]- Derivation
> *Unit law $\theta \circ \eta_{UQ} = \mathrm{id}_{UQ}$.* The map $\eta_{UQ} : UQ \to H(UQ)$ is the universal insertion (the unit of the monad), and it includes a cell as its own formal composite. Then $\theta(\eta_{UQ}(x))$ evaluates the trivial formal composite of $x$, which is $x$ itself. So $\theta \circ \eta_{UQ} = \mathrm{id}_{UQ}$.
>
> *Associativity law $\theta \circ H\theta = \theta \circ \mu_{UQ}$.* Both sides are maps $HH(UQ) \to UQ$. The left composite first evaluates the inner formal composites (via $H\theta$) and then the outer one (via $\theta$); the right composite first flattens the doubly-formal composite into a single formal composite (via the monad multiplication $\mu_{UQ}$) and then evaluates (via $\theta$). Because the strict operations of $Q$ are *strictly associative*, evaluating in two stages and evaluating after flattening give the same element of $UQ$. Formally, both are morphisms of stretchings out of the universal stretching on $H(UQ)$ realising the same underlying behaviour, so by the *uniqueness* clause of initiality they coincide. This is the only place strict associativity of $Q$ is needed; for a weak $Q$ the two evaluations would differ by a (nondegenerate) coherence cell and the law would fail on the nose.

> [!note]- Complete formal solution
> Let $Q$ be a strict ω-category with underlying reflexive globular set $UQ$.
>
> **(1)** Form the stretching $\Sigma := (UQ,\ \mathrm{id}_{UQ},\ p)$ over $UQ$, where $p : UQ \to Q$ is the identity-on-cells map (the identity of the underlying globular set), equipped with the *degenerate* contraction: for parallel $a,b \in UQ_n$ with $p(a) = p(b)$ — equivalently $a = b$, since $p$ is the identity on cells — the chosen connecting $(n{+}1)$-cell is the degenerate cell $i(a)$. Globularity and the identity axioms make this a valid stretching, and it uses strictness only through the fact that "identified in $Q$" means "equal".
>
> **(2)** The Penon monad has $H(UQ)$ underlying the *initial* stretching $\Sigma_0 = (UQ \xrightarrow{\eta} H(UQ) \to Q_{UQ})$ over $UQ$. By initiality there is a unique morphism of stretchings $\Sigma_0 \to \Sigma$; let $\theta : H(UQ) \to UQ$ be its underlying globular-set map. Explicitly, $\theta$ evaluates each formal weak composite by the strict operations of $Q$ and sends each contraction cell to an identity.
>
> **(3)** *Unit:* $\theta \circ \eta_{UQ}$ evaluates the trivial formal composite, giving $\mathrm{id}_{UQ}$. *Associativity:* $\theta \circ H\theta$ and $\theta \circ \mu_{UQ}$ are both morphisms of stretchings out of the initial stretching on $H(UQ)$ inducing the same underlying map (evaluate-then-evaluate $=$ flatten-then-evaluate, by strict associativity of $Q$); by uniqueness they are equal. Hence $\theta$ is an $H$-algebra structure, and $(UQ, \theta)$ is a Penon weak ω-category.
>
> **(4)** *Functoriality:* a strict ω-functor $Q \to Q'$ induces a map $UQ \to UQ'$ compatible with the structure maps (it is again forced by initiality), so the assignment $Q \mapsto (UQ, \theta)$ is a functor from strict ω-categories to Penon weak ω-categories. $\blacksquare$

---

# Key Takeaways

**The rigid objects are the "all coherence cells are identities" weak objects.** The single transferable idea is that a strict structure is a weak structure in which every piece of coherence data happens to be trivial. This is the same pattern that makes a strict monoidal category a monoidal category, an abelian group a group, and a discrete category a category: in each case the weak/general notion has extra coherence data (associators, the order of multiplication, nontrivial morphisms) that the strict/special notion forces to be trivial. Whenever you meet a "weak" definition and want to feed it a known rigid example, the move is always the same — exhibit the structure map and send the coherence data to identities. The trigger is "show this rigid thing is an instance of that weak definition", and the reaction is "use the rigid operations for the chosen composites and trivialise the coherence cells".

**Universal properties hand you algebra axioms for free.** When a monad is built as a *free* or *universal* construction, you should almost never verify algebra axioms by direct computation; instead, realise the desired target as an object the universal property maps into, and let the *uniqueness* clause force the unit and associativity laws. Here the entire verification of $\theta \circ \eta = \mathrm{id}$ and $\theta \circ H\theta = \theta \circ \mu$ reduced to "two maps out of an initial object agree". This is a reusable diagnostic: if a monad came from an adjunction or a universal construction, look for the universal property before computing, because it converts a multi-line axiom check into a one-line uniqueness argument.

**Strictness is exactly the collapse of the contraction.** The exercise pinpoints *where* strictness is used: it is the single fact that two parallel cells identified in the target are actually *equal*, so their connecting contraction cell can be an identity. This is worth internalising because it tells you precisely what is lost when you weaken — the contraction cells become genuinely nondegenerate, recording the homotopies that strictness pretended did not exist. The same diagnostic applies across the chapter: in a Segal space the strict-vs-weak distinction is "bijection vs equivalence" of the Segal map; in a quasi-category it is "unique vs merely-existing" inner-horn fillers; in Penon it is "degenerate vs nondegenerate" contraction cells. They are three faces of one phenomenon, and recognising it lets you translate freely among the definitions.
