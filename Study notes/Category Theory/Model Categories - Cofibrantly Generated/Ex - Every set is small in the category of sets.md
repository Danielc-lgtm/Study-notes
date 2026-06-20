---
type: exercise
subject: model-categories
difficulty: "⭐"
prereqs:
  - "Def - Transfinite Composition and Smallness"
  - "Def - Limit and Colimit"
tags: [category-theory, homotopy-theory, foundations]
---

# Problem Statement

Prove that in $\mathbf{Set}$, every object $A$ is [[Def - Transfinite Composition and Smallness|small]] relative to the class of all morphisms. Specifically, show that $A$ is $\kappa$-small with $\kappa = |A|^+$ (the successor cardinal of the cardinality of $A$): for every regular cardinal $\lambda\geq\kappa$ and every $\lambda$-sequence of sets $X_0\to X_1\to\cdots$, the canonical map
$$\mathrm{colim}_{\beta<\lambda}\,\mathbf{Set}(A, X_\beta)\longrightarrow \mathbf{Set}\big(A,\,\mathrm{colim}_{\beta<\lambda} X_\beta\big)$$
is a bijection. Identify exactly where the regularity of $\lambda$ is used, and explain why $\kappa$ must exceed $|A|$ rather than equal it.

**Recall:**

![[Def - Transfinite Composition and Smallness#The Definition]]

A cardinal $\lambda$ is **regular** if it is not the supremum of fewer than $\lambda$ ordinals each smaller than $\lambda$ — equivalently, a union of $<\lambda$ sets each of cardinality $<\lambda$ has cardinality $<\lambda$. A filtered colimit of sets is computed as the disjoint union of the stages modulo the relation "eventually equal": $\mathrm{colim}_\beta X_\beta = \big(\coprod_\beta X_\beta\big)/\!\sim$, where $x_\beta\sim x_{\beta'}$ if they have a common image at some later stage.

---

# Convergent Strategy

**Problem class:** This is a smallness-certification problem in its purest, cardinality-driven form — the algebraic counterpart to the topological compactness argument. It establishes the fact that makes every presheaf category small-object-argument-friendly.

**Assumption pattern:** The decisive assumptions are the cardinality bound $|A| < \kappa\leq\lambda$ and the regularity of $\lambda$. The cardinality bound says $A$ has *few* elements relative to $\lambda$; regularity says that few elements cannot reach cofinally far up the tower. Together they force every function $A\to\mathrm{colim}$ to be "bounded."

**Theorem routing:** The route is direct: a function $A\to\mathrm{colim}_\beta X_\beta$ assigns each of the $<\lambda$ elements of $A$ a value living at some stage; regularity bounds the supremum of these $<\lambda$ stages below $\lambda$; so the function factors through that bounded stage (surjectivity). Injectivity is the same argument applied to the (also $<\lambda$ many) coincidences that must be realized.

**Key decision point:** The non-obvious choice is the threshold $\kappa = |A|^+$ rather than $|A|$. If $\lambda = |A|$ exactly, then $A$ has $\lambda$-many elements and a function can use one stage per element, reaching cofinally up the tower of length $\lambda$ — escape to infinity. Bumping to $\kappa = |A|^+$ guarantees $|A| < \lambda$ strictly, so regularity applies. Choosing the threshold too low is the standard error.

---

# Legal Operations Used

1. **Operation 5 from the topic page (certify smallness by cardinality).** This exercise is the cardinality version of smallness certification: bound $|A|$, use regularity of $\lambda$ to bound the supremum of the per-element stages.

2. **Operation 1 from the topic page (form the closures of a set).** Smallness here is relative to all maps, the most demanding class, so the conclusion is the strongest form ($A$ small simpliciter).

---

# Hints

> [!note]- Hint 1
> A function $f : A\to\mathrm{colim}_\beta X_\beta$ is determined by where it sends each $a\in A$. Each value $f(a)$ is represented by an element of some stage $X_{\beta(a)}$. You have $|A|$ many such stages $\beta(a)$, one per element.

> [!note]- Hint 2
> Let $\beta^* = \sup_{a\in A}\beta(a)$. You want $\beta^* < \lambda$, so that all values live by stage $\beta^*$. This is a supremum of $\leq|A| < \lambda$ ordinals each $<\lambda$ — and regularity of $\lambda$ says such a supremum stays below $\lambda$.

> [!note]- Hint 3
> With $\beta^* < \lambda$, lift each $f(a)$ to $X_{\beta^*}$ (push each representative forward along the tower to the common stage $\beta^*$); this defines $f_{\beta^*} : A\to X_{\beta^*}$ with $f = (X_{\beta^*}\to\mathrm{colim})\circ f_{\beta^*}$. That is surjectivity.

> [!note]- Hint 4
> For injectivity: if $f_\beta, f_{\beta'} : A\to X$ become equal in the colimit, each element's two values are identified at some stage; take the sup of those $<\lambda$ stages (regularity again) to find one stage where $f_\beta = f_{\beta'}$. For the role of $\kappa = |A|^+$: if $\lambda = |A|$, a bijection $A\to\lambda$ composed into a tower can send the $a$-th element to stage $a$, with sup $=\lambda$, escaping.

---

# Solution

The proof is a two-part supremum argument. Surjectivity: a function out of $A$ uses $\leq|A|<\lambda$ stages, whose sup is $<\lambda$ by regularity, so the function factors there (Step 1). Injectivity: two factorizations agreeing at infinity realize $\leq|A|<\lambda$ coincidences, whose sup is again $<\lambda$, so they agree at a stage (Step 2). The threshold $\kappa = |A|^+$ is what guarantees the strict inequality $|A|<\lambda$ that regularity needs (Step 3).

**Step 1: Surjectivity — every $f : A\to\mathrm{colim}_\beta X_\beta$ factors through a bounded stage.**

> [!note]- Derivation
> Compute the colimit as $\mathrm{colim}_\beta X_\beta = (\coprod_\beta X_\beta)/\!\sim$. For each $a\in A$, the value $f(a)$ is the $\sim$-class of some $x_a\in X_{\beta(a)}$. Set $\beta^* = \sup_{a\in A}\beta(a)$. Since $|A| < \kappa\leq\lambda$ and $\lambda$ is regular, this is a supremum of fewer than $\lambda$ ordinals below $\lambda$, hence $\beta^* < \lambda$. Push each $x_a$ forward along the tower to its image $x_a^*\in X_{\beta^*}$ (well-defined since $\beta(a)\leq\beta^*$). The assignment $a\mapsto x_a^*$ is a function $f_{\beta^*} : A\to X_{\beta^*}$, and its image in the colimit is $f$ (each $x_a^*$ is $\sim$-equivalent to $x_a$, representing $f(a)$). So $f$ factors through $X_{\beta^*}$.

**Step 2: Injectivity — two stage-factorizations agreeing in the colimit agree at a stage.**

> [!note]- Derivation
> Suppose $f_\beta : A\to X_\beta$ and $f_{\beta'} : A\to X_{\beta'}$ have the same image in $\mathrm{colim}$. For each $a$, the elements $f_\beta(a)$ and $f_{\beta'}(a)$ are $\sim$-equivalent, so they have a common image at some stage $\gamma(a)\geq\max(\beta,\beta')$. Set $\gamma = \sup_{a\in A}\gamma(a)$; again $|A| < \lambda$ regular gives $\gamma < \lambda$. Pushing both $f_\beta$ and $f_{\beta'}$ forward to $X_\gamma$, they agree on every $a$, so they become equal in $X_\gamma$. Hence the two represent the same element of $\mathrm{colim}_\beta\,\mathbf{Set}(A, X_\beta)$. Combined with Step 1, the canonical map is a bijection.

**Step 3: Why $\kappa = |A|^+$ and not $|A|$.**

> [!note]- Derivation
> The supremum arguments need $|A| < \lambda$ *strictly*, so that "$\leq|A|$ ordinals" is "$<\lambda$ ordinals," which is the input to regularity. Taking $\kappa = |A|^+$ ensures every $\lambda\geq\kappa$ satisfies $\lambda > |A|$. If instead one allowed $\lambda = |A|$: let $A$ have cardinality $\lambda$ and fix a bijection $A\cong\lambda$; build the $\lambda$-sequence $X_\gamma = \gamma$ (each $X_\gamma$ the set of ordinals $<\gamma$, with inclusions), whose colimit is $\lambda$. The identity-like function $A\cong\lambda\to\lambda = \mathrm{colim}$ sends the $\gamma$-th element to $\gamma\in X_{\gamma+1}$, so its per-element stages are cofinal in $\lambda$ and $\beta^* = \lambda$: it factors through no bounded stage. Smallness fails at $\lambda = |A|$. The successor $\kappa = |A|^+$ is exactly the fix.

> [!note]- Complete formal solution
> Let $A\in\mathbf{Set}$, $\kappa = |A|^+$, $\lambda\geq\kappa$ regular, and $X_0\to\cdots$ a $\lambda$-sequence with colimit $X_\infty = (\coprod_\beta X_\beta)/\!\sim$.
>
> *Surjectivity.* Given $f : A\to X_\infty$, represent $f(a)$ by $x_a\in X_{\beta(a)}$. Then $\beta^* := \sup_a\beta(a)$ is a sup of $\leq|A|<\lambda$ ordinals $<\lambda$, so $\beta^*<\lambda$ by regularity. Pushing the $x_a$ to $X_{\beta^*}$ gives $f_{\beta^*} : A\to X_{\beta^*}$ representing $f$.
>
> *Injectivity.* If $f_\beta, f_{\beta'}$ represent the same $f$, each pair $f_\beta(a), f_{\beta'}(a)$ coincides at a stage $\gamma(a)$; $\gamma := \sup_a\gamma(a) < \lambda$ by regularity, and $f_\beta = f_{\beta'}$ in $X_\gamma$.
>
> Hence $\mathrm{colim}_\beta\,\mathbf{Set}(A,X_\beta)\to\mathbf{Set}(A,X_\infty)$ is a bijection, so $A$ is $|A|^+$-small relative to all maps. Regularity is used in both suprema; $\kappa = |A|^+$ (not $|A|$) is needed to ensure $|A|<\lambda$ strictly, without which the identity $A\cong\lambda\to\lambda$ on the tower $X_\gamma = \gamma$ escapes to infinity. $\blacksquare$

---

# Key Takeaways

**Smallness in algebraic categories is a counting argument: few elements cannot reach far.** Where the topological proof used compactness, the set-theoretic proof uses cardinality plus regularity, and the two are the same phenomenon — an object built from $<\kappa$ data cannot be spread across a $\kappa$-long tower. This is why every presheaf category (and every locally presentable category) has all objects small: each object is built from a set of generators of bounded cardinality, and regularity of large $\lambda$ bounds the reach. The transferable diagnostic is: to certify smallness in a combinatorial category, bound the "size" of $A$ (number of elements, generators, simplices, basis vectors) and invoke regularity at a threshold above that size.

**Regularity is exactly the closure-under-small-sups property, and it is non-negotiable.** The entire argument is two suprema of $<\lambda$ ordinals, and regularity is precisely the statement that such suprema stay below $\lambda$. Drop regularity — work at a singular $\lambda$ like $\aleph_\omega$ — and a function out of even a countable $A$ can be assembled cofinally and escape, as the cofinality counterexample on [[Def - Transfinite Composition and Smallness]] shows. Recognizing "I need a sup of few things to stay bounded, so I need a regular cardinal" is the trigger that should fire whenever a transfinite construction must terminate; it is the same regularity used in forcing to ensure generic filters meet dense sets boundedly.

**The threshold $\kappa$ must strictly exceed the size of the object, and off-by-one errors here are real bugs.** It is tempting to take $\kappa = |A|$, but the strict inequality $|A| < \lambda$ is what converts "$\leq|A|$ stages" into "$<\lambda$ stages," the input to regularity; at $\lambda = |A|$ the identity map on the tower of ordinals escapes. The general lesson is that smallness thresholds are about *strict* domination, and when invoking the small object argument one must choose the length $\lambda$ strictly above the common smallness threshold of all generator domains. This single off-by-one is the most common subtle error in setting up the small object argument, and this exercise is the clean place to internalize it.
