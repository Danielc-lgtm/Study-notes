---
type: exercise
subject: measure-theory
difficulty: "⭐"
prereqs:
  - "Def - Measurable Function"
  - "Thm - Operations Preserve Measurability"
tags: [analysis, measure-theory]
---

# Problem Statement

Let $(X,\mathcal{A})$ be a measurable space and $(f_n)$ a sequence of measurable functions $X\to\mathbb{R}$.

**(a)** Show that $\sup_n f_n$, $\inf_n f_n$, $\limsup_n f_n$, $\liminf_n f_n$ are measurable (as $[-\infty,\infty]$-valued functions).

**(b)** Show that the **convergence set** $C=\{x:\lim_n f_n(x)\text{ exists in }\mathbb{R}\}$ is measurable.

**(c)** Show that if $f_n\to f$ pointwise on $C$, then $f$ restricted to $C$ is measurable; and that $C$ is the set where $\liminf f_n=\limsup f_n$ is finite.

**Recall:**

[[Thm - Operations Preserve Measurability]]: countable $\sup$, $\inf$, $\limsup$, $\liminf$ of measurable functions are measurable; preimages of Borel sets under measurable functions are measurable.

---

# Convergent Strategy

**Problem class:** showing a set defined by a *limiting condition* is measurable.

**Assumption pattern:** "the limit exists" is not a single set operation but it *unwinds* into countable operations: a limit exists and is finite iff $\liminf=\limsup\in\mathbb{R}$. Both are measurable functions; "two measurable functions agree" is a measurable set.

**Theorem routing:** $\sup,\inf$ measurable via level sets ($\{\sup f_n<a\}=\bigcap\{f_n<a\}$); $\limsup=\inf_l\sup_{k\ge l}$; $C=\{\liminf=\limsup\}\cap\{\text{finite}\}$.

**Key decision point:** expressing "$\lim$ exists" as an *equation between measurable functions*.

---

# Legal Operations Used

1. **Unwind sup/inf into level sets** — countable unions/intersections.
2. **"Two measurable functions agree" is a measurable set** — $\{g=h\}=(g-h)^{-1}(\{0\})$.

---

# Hints

> [!note]- Hint 1
> $\{\inf_n f_n<a\}=\bigcup_n\{f_n<a\}$; $\sup=-\inf(-\cdot)$; $\limsup f_n=\inf_l\sup_{k\ge l}f_k$.

> [!note]- Hint 2
> A real limit exists iff $\liminf f_n=\limsup f_n$ and this common value is finite.

---

# Solution

**Step 1 — (a).** $\{\inf_n f_n<a\}=\bigcup_n\{f_n<a\}\in\mathcal{A}$, so $\inf_n f_n$ is measurable; $\sup_n f_n=-\inf_n(-f_n)$ measurable. Then $\limsup_n f_n=\inf_l\sup_{k\ge l}f_k$ and $\liminf_n f_n=\sup_l\inf_{k\ge l}f_k$ are countable $\sup/\inf$ of measurables, hence measurable.

**Step 2 — (b)–(c).** A sequence $(f_n(x))$ converges in $\mathbb{R}$ iff $\liminf_n f_n(x)=\limsup_n f_n(x)$ and the common value is finite. So, with $g=\liminf f_n$, $h=\limsup f_n$ (both measurable, by (a)),
$$C=\{x:g(x)=h(x)\}\cap\{x:|g(x)|<\infty\}.$$

> [!note]- Derivation
> $\{g=h\}=\{g-h=0\}=(g-h)^{-1}(\{0\})$ is the preimage of a Borel set under a measurable function (where $g-h$ is defined; on the $\pm\infty$ ambiguity sets handle directly) — measurable. $\{|g|<\infty\}=g^{-1}(\mathbb{R})$, measurable. So $C\in\mathcal{A}$. On $C$, $f=\lim f_n=\limsup f_n=h$, the restriction of a measurable function, hence measurable.

> [!note]- Complete formal solution
> (a) $\{\inf f_n<a\}=\bigcup\{f_n<a\}$ measurable; $\sup=-\inf(-\cdot)$; $\limsup=\inf_l\sup_{k\ge l}$, $\liminf=\sup_l\inf_{k\ge l}$ — countable $\sup/\inf$, measurable. (b) $C=\{\liminf f_n=\limsup f_n\}\cap\{\text{finite}\}$, an intersection of preimages of Borel sets under measurable functions, measurable. (c) On $C$, $f=\limsup f_n$, measurable. $\blacksquare$

---

# Key Takeaways

**"The limit exists" is a measurable condition, because it unwinds into a countable combination of measurable operations.** This is not automatic — for *continuous* functions the convergence set need not be open or closed — but measurable functions are closed under all countable limiting operations, so the event "$f_n$ converges" is genuinely a measurable set. This is what makes statements like the [[Thm - Strong Law of Large Numbers|strong law]] ("$S_n/n$ converges almost surely") *well-posed*: the set being assigned probability $1$ is a bona fide event.

**Express limiting conditions as equations between measurable functions.** "$\lim$ exists" becomes "$\liminf=\limsup$, finite"; "$f_n\to f$" becomes "$\limsup|f_n-f|=0$." Translating a verbal limiting statement into an equation among the measurable functions $\liminf,\limsup,\sup$ is the reflex that makes such sets visibly measurable.
