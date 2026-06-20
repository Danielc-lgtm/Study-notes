---
type: exercise
subject: higher-categories
difficulty: "⭐"
prereqs:
  - "Def - Monad Monoid and Module in a Bicategory"
  - "Def - Monad and Comonad"
  - "Def - Functor"
  - "Def - Natural Transformation"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

Let $\mathbf{Cat}$ be the $2$-category of [[Def - Category|categories]], [[Def - Functor|functors]], and [[Def - Natural Transformation|natural transformations]]. Verify that a [[Def - Monad Monoid and Module in a Bicategory|monad in Cat]] is exactly an ordinary [[Def - Monad and Comonad|monad]] $(T, \mu, \eta)$ on a category: the carrier object is a category $\mathcal{A}$, the endo-$1$-cell is an endofunctor $T : \mathcal{A} \to \mathcal{A}$, the multiplication and unit are natural transformations $\mu : TT \Rightarrow T$ and $\eta : 1_{\mathcal{A}} \Rightarrow T$, and the bicategorical monad axioms are the ordinary monad associativity and unit laws. This is the consistency check that licenses the whole bicategorical generalisation.

**Recall:**

![[Def - Monad Monoid and Module in a Bicategory#The Definition]]

An ordinary **[[Def - Monad and Comonad|monad]]** on a category $\mathcal{A}$ is an endofunctor $T : \mathcal{A}\to\mathcal{A}$ with natural transformations $\mu : T^2\Rightarrow T$ (multiplication) and $\eta : 1_{\mathcal{A}}\Rightarrow T$ (unit) satisfying $\mu\circ T\mu = \mu\circ\mu T$ (associativity) and $\mu\circ T\eta = 1_T = \mu\circ\eta T$ (unit laws). In $\mathbf{Cat}$: objects are categories, $1$-cells are functors (composed by $\circ$), and $2$-cells are natural transformations (vertical composition $\cdot$, horizontal/whiskering $\ast$).

---

# Convergent Strategy

**Problem class:** A *dictionary-translation / consistency-check* problem: confirm that the bicategorical definition, read in $\mathbf{Cat}$, reproduces the structure it was modelled on.

**Assumption pattern:** $\mathbf{Cat}$ is the bicategory whose objects, $1$-cells, and $2$-cells are categories, functors, and natural transformations, with $1$-cell composition the ordinary composition of functors. So the transcription is essentially verbatim: "endo-$1$-cell" $=$ "endofunctor", "$2$-cell" $=$ "natural transformation", "$tt$" $=$ "$T^2$".

**Theorem routing:** This is the consistency clause of [[Def - Monad Monoid and Module in a Bicategory]] — the requirement that the generalisation specialise correctly. It must hold or the entire generalisation (and hence [[Thm - Monoids and Modules Form a Bicategory]] specialised to $\mathbf{Cat}$) would be wrong.

**Key decision point:** The only subtlety is matching the horizontal composition $\ast$ of $2$-cells in $\mathbf{Cat}$ with the *whiskering* used to state the ordinary monad laws ($T\mu = 1_T\ast\mu$, $\mu T = \mu\ast 1_T$). Recognising that bicategorical horizontal composition of natural transformations is exactly whiskering is what makes the two axiom-sets coincide letter for letter.

---

# Legal Operations Used

1. **Operation 4 (transcribe the monad notion into $\mathbf{Cat}$).** Write $t = T$, $\mu : TT\Rightarrow T$, $\eta : 1\Rightarrow T$ as functors and natural transformations.

2. **Operation 5 (read via the concrete description).** $1$-cell composition in $\mathbf{Cat}$ is functor composition; horizontal $2$-cell composition is whiskering.

---

# Hints

> [!note]- Hint 1
> Write out the data of a monad in $\mathbf{Cat}$ piece by piece: the object is a category $\mathcal{A}$; the endo-$1$-cell $t : \mathcal{A}\to\mathcal{A}$ is a functor; the $2$-cells $\mu, \eta$ are natural transformations. Compare with the ordinary monad data.

> [!note]- Hint 2
> The bicategorical associativity law is $\mu\cdot(\mu\ast 1_t) = \mu\cdot(1_t\ast\mu)$. In $\mathbf{Cat}$, $\mu\ast 1_t$ is the whiskering $\mu T$ and $1_t\ast\mu$ is $T\mu$. So the law reads $\mu\circ\mu T = \mu\circ T\mu$ — the ordinary monad associativity.

> [!note]- Hint 3
> The unit laws $\mu\cdot(\eta\ast 1_t) = 1_t = \mu\cdot(1_t\ast\eta)$ become $\mu\circ\eta T = 1_T = \mu\circ T\eta$. The bicategory coherence isos are identities in the strict $2$-category $\mathbf{Cat}$, so no coherence bookkeeping intervenes.

---

# Solution

We match data and axioms directly.

**Step 1: Data.**

> [!note]- Derivation
> A [[Def - Monad Monoid and Module in a Bicategory|monad in Cat]] is an object $\mathcal{A}$ — a [[Def - Category|category]] — with an endo-$1$-cell $t : \mathcal{A}\to\mathcal{A}$ — a [[Def - Functor|functor]] $T$ — and $2$-cells $\mu : tt\Rightarrow t$, $\eta : 1_{\mathcal{A}}\Rightarrow t$ — [[Def - Natural Transformation|natural transformations]] $\mu : T^2\Rightarrow T$, $\eta : 1_{\mathcal{A}}\Rightarrow T$. This is exactly the data of an ordinary [[Def - Monad and Comonad|monad]] $(T, \mu, \eta)$ on $\mathcal{A}$.

**Step 2: Axioms, via whiskering.**

> [!note]- Derivation
> In the strict $2$-category $\mathbf{Cat}$, horizontal composition $\ast$ of a natural transformation with an identity is *whiskering*: $\mu\ast 1_T = \mu T$ (whisker on the right by $T$) and $1_T\ast\mu = T\mu$ (whisker on the left by $T$). The coherence isomorphisms of $\mathbf{Cat}$ are identities (it is strict). So the bicategorical associativity law $\mu\cdot(\mu\ast 1_t) = \mu\cdot(1_t\ast\mu)$ reads
> $$\mu\circ\mu T = \mu\circ T\mu,$$
> the ordinary monad associativity, and the unit laws $\mu\cdot(\eta\ast 1_t) = 1_t = \mu\cdot(1_t\ast\eta)$ read
> $$\mu\circ\eta T = 1_T = \mu\circ T\eta,$$
> the ordinary monad unit laws. Data and axioms coincide.

**Step 3: Examples and consistency.**

> [!note]- Derivation
> Concrete monads in $\mathbf{Cat}$ are exactly the familiar ones: the free-monoid monad on $\mathbf{Set}$ (with $\mu$ flattening lists of lists and $\eta$ the singleton), the power-set monad, the free-group monad, and every [[Def - Monad and Comonad|monad from a free–forgetful adjunction]]. Since a monad in $\mathbf{Cat}$ is an ordinary monad, the bicategorical theory specialises correctly, confirming that "monad in a bicategory" is a faithful generalisation. Conversely any ordinary monad is a monad in $\mathbf{Cat}$.

> [!note]- Complete formal solution
> A monad in $\mathbf{Cat}$ is an object $\mathcal{A}$ (a category), an endo-$1$-cell $t = T : \mathcal{A}\to\mathcal{A}$ (an endofunctor), and $2$-cells $\mu : TT\Rightarrow T$, $\eta : 1_{\mathcal{A}}\Rightarrow T$ (natural transformations). In the strict $2$-category $\mathbf{Cat}$, horizontal composition with identities is whiskering ($\mu\ast 1_t=\mu T$, $1_t\ast\mu=T\mu$) and coherence cells are identities, so the bicategorical axioms become $\mu\circ\mu T=\mu\circ T\mu$ and $\mu\circ\eta T=1_T=\mu\circ T\eta$ — exactly the ordinary [[Def - Monad and Comonad|monad]] associativity and unit laws. Hence a monad in $\mathbf{Cat}$ is precisely an ordinary monad, and the correspondence is a bijection. $\blacksquare$

---

# Key Takeaways

**The generalisation must specialise — and here it does, verbatim.** The value of this exercise is methodological: any time you generalise a definition (here, monad from $\mathbf{Cat}$ to an arbitrary bicategory), the first obligation is to check that the new definition *recovers* the old one in the original setting. The recovery is exact because $\mathbf{Cat}$'s objects, $1$-cells, and $2$-cells *are* categories, functors, and natural transformations, and its $1$-cell composition *is* functor composition. The transferable habit: before trusting a generalisation, instantiate it at the motivating example and confirm letter-for-letter agreement. A generalisation that fails this check is wrong, no matter how elegant.

**Whiskering is bicategorical horizontal composition with an identity.** The one technical point worth isolating is that the whiskerings $T\mu$ and $\mu T$ appearing in the ordinary monad laws are exactly the bicategorical horizontal composites $1_T\ast\mu$ and $\mu\ast 1_T$. Recognising this dictionary — "whisker" $=$ "horizontal-compose with an identity $1$-cell/$2$-cell" — is what lets you read any bicategorical axiom as a familiar $\mathbf{Cat}$-statement and vice versa. It is the same dictionary that makes the [[Thm - The Interchange Law|interchange law]] of $\mathbf{Cat}$ a special case of the bicategorical interchange, and it recurs throughout formal monad theory.

**$\mathbf{Cat}$ is the strict, data-rich end of the spectrum.** Placed beside [[Ex - A monad in Span Set is a small category]] and [[Ex - A monad in Rel is a preorder]], this exercise locates ordinary monads as the case where the ambient $2$-category is $\mathbf{Cat}$ — strict (coherence cells are identities) and data-rich ($2$-cells are genuine natural transformations, not mere inclusions). The spectrum is: $\mathbf{Rel}$ (thin, property-like) $\to$ $\mathbf{Span}(\mathbf{Set})$ (sets of arrows, category-like) $\to$ $\mathbf{Cat}$ (functors and natural transformations, monad-like). The unifying lesson is that the *same* monad template populates all three, and the consistency check here is what guarantees the spectrum is anchored at the classical notion it generalises. This anchoring is what makes Street's formal theory of monads a faithful extension of ordinary monad theory rather than a different subject.
