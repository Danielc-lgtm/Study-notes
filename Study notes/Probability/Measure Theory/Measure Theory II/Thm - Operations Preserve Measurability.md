---
type: theorem
subject: measure-theory
prereqs:
  - "Def - Measurable Function"
  - "Def - Generated σ-Algebra"
tags: [analysis, measure-theory]
---

# Notation

$(X,\mathcal{A})$ a measurable space; $f,g,f_k:X\to\mathbb{R}$ (or $[-\infty,\infty]$) [[Def - Measurable Function|measurable functions]].

---

# Motivation

Measurability would be a useless notion if it were fragile — if adding two measurable functions, or taking a limit of them, could escape the class. This theorem certifies that it does not: measurable functions form a class closed under *all* the operations of analysis, algebraic and limiting. In particular the *pointwise limit* of measurable functions is measurable — a closure property the continuous functions spectacularly lack, and the single reason measurable functions are the right setting for the [[Thm - Monotone Convergence Theorem|convergence theorems]].

---

# Sources and Targets

**Sources.** The input "$f$ measurable" is broadened by: $f$ continuous $\Rightarrow$ $f$ Borel measurable; $f$ simple with measurable level sets; $f$ a pointwise (or a.e.) limit of measurable functions. Recognising any of these lets the theorem apply.

**Targets.** The conclusion "the class is closed" combines with [[Thm - Approximation by Simple Functions|approximation]] to give: *every* measurable function is a limit of simple ones, so any property proved for simple functions and stable under limits holds for all measurable functions. It also gives measurability of $\limsup f_k$, $\inf f_k$ — used to show $\{f_n\text{ converges}\}$ is a measurable event.

---

# Statement

Let $f,g:X\to\mathbb{R}$ be measurable and $(f_k)$ a sequence of measurable functions.

1. $f+g$, $f\cdot g$, $\alpha f$ ($\alpha\in\mathbb{R}$), $|f|$, $f\wedge g=\min(f,g)$, $f\vee g=\max(f,g)$ are measurable; and $1/g$ where $g\neq0$.
2. $\inf_k f_k$, $\sup_k f_k$, $\liminf_k f_k$, $\limsup_k f_k$ are measurable (as $[-\infty,\infty]$-valued functions).
3. Consequently, if $f_k\to f$ pointwise, $f$ is measurable; and $\{x:\lim_k f_k(x)\text{ exists}\}\in\mathcal{A}$.

---

# Why Is It True

Two mechanisms, one per part.

**Algebraic operations** reduce to *continuity plus composition*. The maps $(s,t)\mapsto s+t$ and $(s,t)\mapsto st$ are continuous $\mathbb{R}^2\to\mathbb{R}$, hence Borel measurable; $x\mapsto(f(x),g(x))$ is measurable into $\mathbb{R}^2$ (each coordinate is); a composition of measurable maps is measurable. So $f+g$, $fg$ are measurable because they are *continuous functions of a measurable pair*. Concretely, $(f+g)^{-1}((-\infty,a))=\bigcup_{r,s\in\mathbb{Q},\,r+s<a}f^{-1}((-\infty,r))\cap g^{-1}((-\infty,s))$ — a countable union of measurable sets, where rationals make the union countable.

**Limiting operations** reduce to the fact that $\sigma$-algebras are closed under *countable* unions and intersections, and $\sup,\inf,\limsup,\liminf$ are all built from countable $\sup/\inf$. The level set unwinds: $\{\inf_k f_k<a\}=\bigcup_k\{f_k<a\}$ — "the inf is small iff *some* $f_k$ is small," a countable union. Then $\sup_k f_k=-\inf_k(-f_k)$, and $\limsup f_k=\inf_l\sup_{k\ge l}f_k$, $\liminf f_k=\sup_l\inf_{k\ge l}f_k$ — each a countable $\sup/\inf$ of measurables. The pointwise limit, when it exists, equals $\limsup=\liminf$, hence is measurable; and $\{\lim\text{ exists}\}=\{\limsup f_k=\liminf f_k\}$ is the measurable set where two measurable functions agree.

The deep point: *measurability survives limits because the $\sigma$-algebra was built to be closed under countable operations, and a pointwise limit is a countable construction.* Continuity fails the analogue precisely because topology has only finite intersection-closure.

---

# What Makes This Hard

Nothing is hard; two devices must be remembered. (i) For $f+g$, the trick is inserting *rationals*: $\{f+g<a\}=\bigcup_{r+s<a,\,r,s\in\mathbb{Q}}\{f<r\}\cap\{g<s\}$ — the rationals make the union *countable*, which is what a $\sigma$-algebra can absorb. (ii) For $\sup/\limsup$ one must rewrite everything as a countable $\sup$ or $\inf$ and translate each into a countable union or intersection of level sets. The common error is forgetting that an *uncountable* sup of measurable functions need *not* be measurable.

---

# Rederivation Scaffold

**High-level strategy.** Algebraic part: realise each operation as a continuous function of the measurable pair $(f,g)$, or unwind the level set with rationals. Limiting part: write the operation as a countable $\sup/\inf$ and translate level sets into countable unions/intersections.

**Subgoal decomposition.**

1. **$f+g$ measurable.** $\{f+g<a\}=\bigcup_{r,s\in\mathbb{Q},r+s<a}\{f<r\}\cap\{g<s\}$ — countable union of measurable sets.
2. **$fg$, $|f|$, $f\wedge g$, $f\vee g$.** Use $fg=\tfrac12((f+g)^2-f^2-g^2)$ and continuity of $t\mapsto t^2,|t|$; $f\wedge g=f-(g-f)^+$, $f\vee g=f+(g-f)^+$.
3. **$\inf_k f_k$.** $\{\inf_k f_k<a\}=\bigcup_k\{f_k<a\}$. Then $\sup=-\inf(-\cdot)$.
4. **$\limsup,\liminf,\lim$.** $\limsup f_k=\inf_l\sup_{k\ge l}f_k$; apply step 3 twice. $\{\lim\text{ exists}\}=\{\limsup=\liminf\}$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Sums and products
> **Statement:** $f+g$ and $fg$ are measurable.
>
> > [!note]- Full proof
> > $\{f+g<a\}=\bigcup_{r,s\in\mathbb{Q},\,r+s<a}\{f<r\}\cap\{g<s\}$: if $f(x)+g(x)<a$, density of $\mathbb{Q}$ gives rationals $r>f(x),s>g(x)$ with $r+s<a$; conversely such $r,s$ force $f(x)+g(x)<a$. The right side is a countable union of measurable sets, so $f+g$ is measurable. For $fg$: $t\mapsto t^2$ is continuous hence measurable, so $f^2,g^2,(f+g)^2$ are measurable, and $fg=\tfrac12[(f+g)^2-f^2-g^2]$. $\square$

> [!note]- Lemma 2: Countable suprema and infima
> **Statement:** $\inf_k f_k$ and $\sup_k f_k$ are measurable.
>
> > [!note]- Full proof
> > $\{\inf_k f_k<a\}=\bigcup_k\{f_k<a\}\in\mathcal{A}$, so $\inf_k f_k$ is measurable. Then $\sup_k f_k=-\inf_k(-f_k)$ is measurable since negation preserves measurability. $\square$

> [!note]- Lemma 3: limsup, liminf, and the convergence set
> **Statement:** $\limsup f_k,\liminf f_k$ measurable; $\{\lim f_k\text{ exists}\}\in\mathcal{A}$.
>
> > [!note]- Full proof
> > $\limsup_k f_k=\inf_l(\sup_{k\ge l}f_k)$ and $\liminf_k f_k=\sup_l(\inf_{k\ge l}f_k)$ — each a countable $\sup/\inf$ of measurable functions, so measurable by Lemma 2. $\{\lim\text{ exists}\}=\{\limsup f_k=\liminf f_k\}=(\limsup f_k-\liminf f_k)^{-1}(\{0\})$, the preimage of a Borel set under a measurable function. $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> Lemma 1 gives $f+g,fg$; $|f|$, $f\wedge g$, $f\vee g$, $\alpha f$ follow from continuity of the respective real functions composed with the measurable pair $(f,g)$, and $1/g$ from the explicit level-set formula. Lemma 2 gives $\inf,\sup$; Lemma 3 gives $\limsup,\liminf$ and, when $f_k\to f$ pointwise, $f=\limsup f_k$ is measurable and $\{\lim\text{ exists}\}\in\mathcal{A}$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

In probability this theorem is what makes "$\{X_n\text{ converges}\}$" a genuine *event* — a measurable set — so that statements like the [[Thm - Strong Law of Large Numbers|strong law]] ("$S_n/n$ converges a.s.") are even well-posed. It also underlies the measurability of $\sup_n X_n$, used in [[Thm - Doob's Maximal Inequality|Doob's maximal inequality]].

---

# Bridges

- **[[Thm - Approximation by Simple Functions]]** — the complementary closure fact: measurable functions are not only closed under limits, they are *generated* as limits of simple functions.
- **[[Def - Measurable Function]]** — this theorem is the verification that the class is well-behaved; the rational-insertion trick is the generating-set criterion in action.
