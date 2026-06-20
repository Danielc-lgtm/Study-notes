---
type: exercise
subject: higher-categories
difficulty: "⭐⭐"
prereqs:
  - "Def - Generalized Operad"
  - "Def - Generalized Multicategory"
  - "Def - Cartesian Monad"
tags: [category-theory, higher-categories, foundations]
---

# Problem Statement

Let $T = (-)^{*}$ be the free-monoid (list) monad on $\mathbf{Set}$. Show that a $T$-[[Def - Generalized Operad|operad]] (a $T$-multicategory with object-of-objects $C_0 = 1$) is exactly a classical non-symmetric **operad**: a sequence of sets $P(0), P(1), P(2), \dots$, a unit $\mathrm{id} \in P(1)$, and substitution maps
$$\circ : P(k) \times P(n_1) \times \cdots \times P(n_k) \longrightarrow P(n_1 + \cdots + n_k)$$
satisfying associativity and unitality. In particular, identify the arity map $\mathrm{ar} : P \to T1$ and explain why setting $C_0 = 1$ does **not** collapse the structure to a monoid.

**Recall:**

![[Def - Generalized Operad#The Definition]]

A $T$-operad over a [[Def - Cartesian Monad|cartesian monad]] has an operation-object $P$, an arity $\mathrm{ar} : P \to T1$, a unit $e : 1 \to P$, and a composition $\mathrm{comp} : P \times_{T1} TP \to P$, subject to associativity and unitality.

---

# Convergent Strategy

**Problem class:** An *unwinding to a classical structure* (the second target), now in the one-object case. The routine is to compute $T1$, partition the operations by arity, and recognize substitution.

**Assumption pattern:** Two assumptions drive everything. First, $C_0 = 1$ collapses the *colours* — there are no input/output labels. Second, $T = (-)^{*}$ makes $T1 = 1^{*} = \mathbb{N}$ *non-trivial* — there is a separate arity for each natural number. The interplay (colours collapse, arities survive) is the whole content, and recognizing that the richness lives in $T1$ rather than $C_0$ is the key.

**Theorem routing:** Direct from the [[Def - Generalized Operad|definition of a T-operad]] with $T = (-)^{*}$; this is the operad half of the $(-)^{*}$ row of [[Thm - Generalized Operads Recover Classical Structures]]. The composition pullback $P \times_{T1} TP$ unwinds into the classical substitution domain $\coprod_k P(k) \times P(n_1) \times \cdots \times P(n_k)$.

**Key decision point:** The non-obvious point is to resist the analogy with the *identity* case, where $C_0 = 1$ gives a monoid. Here $C_0 = 1$ does *not* give a monoid, because $T1 = \mathbb{N}$ keeps infinitely many arities alive. Identifying $T1$ correctly — and noticing it is $\mathbb{N}$, not $1$ — is the decision that separates "operad" from "monoid". The tempting alternative ("one object, so it must be a monoid") is exactly the error to avoid.

---

# Legal Operations Used

1. **Operation 6 from the topic page (collapse to the one-object case to get an operad).** Setting $C_0 = 1$ and turning $\mathrm{dom}$ into the arity map $\mathrm{ar} : P \to T1$.
2. **Operation 2 from the topic page (compute $T1$ to find the arity object).** Computing $T1 = 1^{*} = \mathbb{N}$ is the decisive calculation.
3. **Operation 4 from the topic page (form the composable-configuration pullback).** Unwinding $P \times_{T1} TP$ into the classical substitution domain.

---

# Hints

> [!note]- Hint 1
> Compute $T1$ for $T = (-)^{*}$. A list of elements of the one-point set $1 = \{*\}$ is determined by its length, so $T1 = 1^{*} \cong \mathbb{N}$. The arity map $\mathrm{ar} : P \to \mathbb{N}$ then partitions $P$ into fibres.

> [!note]- Hint 2
> Set $P(n) = \mathrm{ar}^{-1}(n)$, the operations of arity $n$. The unit $e : 1 \to P$ lands in $P(1)$ (its arity is the singleton list, length $1$). Where does the composition pullback $P \times_{T1} TP$ live?

> [!note]- Hint 3
> An element of $P \times_{T1} TP$ is "an operation $\theta$ of some arity $k$, together with a length-$k$ list of operations $(\theta_1, \dots, \theta_k)$" — the length matches the arity of $\theta$ via the pullback over $\mathbb{N}$. Its image under composition has arity $n_1 + \cdots + n_k$ where $n_i = \mathrm{ar}(\theta_i)$, because $\mu$ concatenates. This is exactly classical operadic substitution.

---

# Solution

The plan: compute $T1 = \mathbb{N}$ and partition $P$ into the sets $P(n)$ (Step 1); unwind the unit and the composition pullback into the classical unit and substitution maps (Step 2); confirm the axioms and explain why $C_0 = 1$ does not collapse to a monoid (Step 3).

**Step 1: $T1 = \mathbb{N}$ partitions the operations by arity.**

> [!note]- Derivation
> With $T = (-)^{*}$, $T1 = 1^{*} = \coprod_{n \geq 0} 1^n$. A list of $n$ copies of the unique point $* \in 1$ is determined entirely by its length $n$, so $T1 \cong \mathbb{N}$. The arity map $\mathrm{ar} : P \to T1 = \mathbb{N}$ therefore assigns each operation a natural number, its arity, and partitions
> $$P = \coprod_{n \geq 0} P(n), \qquad P(n) = \mathrm{ar}^{-1}(n).$$
> So a $T$-operad's operation-object is exactly a sequence of sets $P(0), P(1), P(2), \dots$ — the classical operad's data. This is where setting $C_0 = 1$ shows its real effect: it removes the colours (no object-labels on inputs) but leaves the arities, because $T1$ is non-trivial.

**Step 2: Unit and composition unwind into the classical operad structure.**

> [!note]- Derivation
> *Unit.* The unit operation $e : 1 \to P$ satisfies $\mathrm{ar} \circ e = \eta_1 : 1 \to T1 = \mathbb{N}$, and $\eta_1(*) = (*)$, the singleton list, whose length is $1$. So $e$ picks out an element $\mathrm{id} \in P(1)$ — the unary identity operation.
>
> *Composition.* The composition is $\mathrm{comp} : P \times_{T1} TP \to P$. The pullback $P \times_{T1} TP$ is the set of pairs $(\theta, \Theta)$ with $\theta \in P$ of arity $k = \mathrm{ar}(\theta)$ and $\Theta \in TP = P^{*}$ a list of operations *whose length equals $k$* (the matching condition over $T1 = \mathbb{N}$): $\Theta = (\theta_1, \dots, \theta_k)$. Writing $n_i = \mathrm{ar}(\theta_i)$, the composite $\mathrm{comp}(\theta, \Theta)$ has arity $\mu_1$ applied to the list of arities, i.e. $n_1 + \cdots + n_k$ (concatenation of lists adds lengths). So composition restricts to
> $$\circ : P(k) \times P(n_1) \times \cdots \times P(n_k) \longrightarrow P(n_1 + \cdots + n_k),$$
> exactly classical operadic substitution: plug $\theta_i$ into the $i$-th input of $\theta$.

**Step 3: Axioms, and why $C_0 = 1$ is not a monoid.**

> [!note]- Derivation
> The [[Def - Generalized Operad|T-operad]] associativity axiom states that grafting a tower of operations is independent of grouping; unwound through Step 2, this is the classical operad associativity $\theta \circ (\theta_1 \circ (\ldots), \dots) = (\theta \circ (\theta_1, \dots)) \circ (\ldots)$. The unitality axiom states that grafting the unit $\mathrm{id} \in P(1)$ on either side returns the operation, the classical operad unit law. So a $T$-operad is precisely a classical non-symmetric operad.
>
> Why is this not a monoid? In the *identity*-monad case, $C_0 = 1$ gives a one-object category, which is a monoid, because $T1 = 1$ provides a single arity. Here $T1 = \mathbb{N}$ provides infinitely many arities, so $P$ is not a single set with a binary operation but an $\mathbb{N}$-graded family $P(n)$ with substitution. The collapse $C_0 = 1$ removed the colours, but the arity object $T1 = \mathbb{N}$ — which depends on $T$, not on $C_0$ — keeps the structure as rich as a full operad. A monoid is the degenerate operad with $P(n) = \emptyset$ for $n \neq 1$ and $P(1)$ a monoid; a general operad is far more.

> [!note]- Complete formal solution
> With $T = (-)^{*}$ and $C_0 = 1$: $T1 = 1^{*} \cong \mathbb{N}$, so $\mathrm{ar} : P \to \mathbb{N}$ partitions $P = \coprod_n P(n)$, $P(n) = \mathrm{ar}^{-1}(n)$. The unit $e$ satisfies $\mathrm{ar}\circ e = \eta_1$, of length $1$, so $\mathrm{id} := e(*) \in P(1)$. The composition pullback $P \times_{T1} TP$ consists of pairs $(\theta, (\theta_1,\dots,\theta_k))$ with $k = \mathrm{ar}(\theta)$, and composition restricts to $P(k) \times P(n_1)\times\cdots\times P(n_k) \to P(n_1+\cdots+n_k)$ ($n_i = \mathrm{ar}(\theta_i)$), classical substitution. The associativity and unitality axioms become the classical operad axioms. Hence a $T$-operad is a classical non-symmetric operad. Setting $C_0 = 1$ collapses colours but not arities, because $T1 = \mathbb{N}$ is non-trivial; this is why the one-object case is a full operad, not a monoid (which would require $T1 = 1$). $\blacksquare$

---

# Key Takeaways

**Compute $T1$ first: it is the arity object, and it alone decides whether the one-object case is a monoid or an operad.** The single calculation $T1 = 1^{*} = \mathbb{N}$ is the entire reason a $(-)^{*}$-operad is rich. The reusable habit is that when you meet any new cartesian monad and want to know what its operads look like, the first thing to compute is $T1$ — it is $1$ for the identity (operads are monoids), $\mathbb{N}$ for the list monad (operads are classical operads), and the globular pasting diagrams for $\mathbb{T}$ (operads are globular operads). This one object converts an abstract question ("what are the operads over $T$?") into a concrete answer, and it is the fastest diagnostic in the chapter.

**Collapsing colours is not collapsing arities — the two live in different objects.** The seductive analogy "one object, so it is a monoid" is correct only when the arity object is trivial. The object-of-objects $C_0$ controls the *colours* (the labels on inputs and outputs); the arity object $T1$ controls the *shapes* (how many inputs, in what configuration). Setting $C_0 = 1$ touches only the colours, leaving $T1$ untouched. The trigger to remember: when you see $C_0 = 1$, do not conclude "monoid"; ask "what is $T1$?", and only if $T1 = 1$ is it a monoid. This distinction is the cleanest way to internalize why operads sit strictly between monoids and multicategories.

**Substitution is the pullback over the arity object, made concrete.** The classical operadic composition $P(k) \times \prod_i P(n_i) \to P(\sum n_i)$ looks like a hand-crafted definition until one sees it as the generalized composition pullback $P \times_{T1} TP$ specialized to $T = (-)^{*}$: the matching-of-lengths is the pullback over $\mathbb{N}$, and the addition of arities is the monad multiplication $\mu$ adding list-lengths. The transferable insight is that every "graft and re-grade" operation in operad theory is an instance of the one generalized composition law, so once you have proved something about $\mathrm{comp}$ generically (e.g. its associativity from cartesianness), you have proved it for classical substitution for free. See [[Ex - A category is an identity-multicategory]] for the same procedure with single objects in place of lists, and [[Thm - Generalized Operads Recover Classical Structures]] for the full set of rows.
