---
type: exercise
subject: measure-theory
difficulty: "⭐"
prereqs:
  - "Def - Measurable Function"
  - "Def - Generated σ-Algebra"
tags: [analysis, measure-theory]
---

# Problem Statement

Let $(X,\mathcal{A})$ and $(Y,\mathcal{A}')$ be measurable spaces and $f:X\to Y$.

**(a)** Show that $\mathcal{G}=\{S\subseteq Y:f^{-1}(S)\in\mathcal{A}\}$ is a $\sigma$-algebra on $Y$.

**(b)** Deduce the **generating-set criterion**: if $\mathcal{E}'$ generates $\mathcal{A}'$, then $f$ is measurable iff $f^{-1}(S)\in\mathcal{A}$ for all $S\in\mathcal{E}'$.

**(c)** Conclude that $f:X\to\mathbb{R}$ is Borel measurable iff $\{f<a\}\in\mathcal{A}$ for every $a\in\mathbb{R}$, and that every continuous $f:\mathbb{R}^n\to\mathbb{R}^m$ is Borel measurable.

**Recall:**

![[Def - Measurable Function#The Definition]]

---

# Convergent Strategy

**Problem class:** reducing an "all measurable sets" verification to a "generators only" verification.

**Assumption pattern:** preimage commutes with all $\sigma$-algebra operations ($f^{-1}(\bigcup S_k)=\bigcup f^{-1}(S_k)$, $f^{-1}(S^c)=f^{-1}(S)^c$). So the family of "good targets" $\mathcal{G}$ is automatically a $\sigma$-algebra; if it contains a generating set it contains everything.

**Theorem routing:** (a) is the [[Def - Generated σ-Algebra|minimality principle]] in action; (b) is its corollary; (c) instantiates with the rays.

**Key decision point:** seeing that the work is done *once*, in (a) — everything after is "$\mathcal{G}$ is a $\sigma$-algebra containing the generators, hence contains $\sigma(\text{generators})$."

---

# Legal Operations Used

1. **Preimage commutes with set operations** — the algebraic identities for $f^{-1}$.
2. **Minimality of $\sigma(\mathcal{C})$** — a $\sigma$-algebra containing generators contains the generated $\sigma$-algebra.

---

# Hints

> [!note]- Hint 1
> $f^{-1}$ commutes with complement and with arbitrary unions. Use this to check the three $\sigma$-algebra axioms for $\mathcal{G}$.

> [!note]- Hint 2
> Once $\mathcal{G}$ is a $\sigma$-algebra: if $\mathcal{E}'\subseteq\mathcal{G}$, then $\sigma(\mathcal{E}')\subseteq\mathcal{G}$ by minimality. What is $\sigma(\mathcal{E}')$?

---

# Solution

**Step 1 — (a) $\mathcal{G}$ is a $\sigma$-algebra.** $f^{-1}(Y)=X\in\mathcal{A}$, so $Y\in\mathcal{G}$. If $S\in\mathcal{G}$, then $f^{-1}(S^c)=f^{-1}(S)^c\in\mathcal{A}$, so $S^c\in\mathcal{G}$. If $S_k\in\mathcal{G}$, then $f^{-1}(\bigcup_k S_k)=\bigcup_k f^{-1}(S_k)\in\mathcal{A}$, so $\bigcup_k S_k\in\mathcal{G}$.

> [!note]- Derivation
> Each axiom transfers because $f^{-1}$ is a Boolean homomorphism: it preserves $Y$, complements, and countable unions, and $\mathcal{A}$ is closed under exactly these.

**Step 2 — (b) Generating-set criterion.** If $f^{-1}(S)\in\mathcal{A}$ for all $S\in\mathcal{E}'$, then $\mathcal{E}'\subseteq\mathcal{G}$. By (a), $\mathcal{G}$ is a $\sigma$-algebra; by [[Def - Generated σ-Algebra|minimality]], $\mathcal{A}'=\sigma(\mathcal{E}')\subseteq\mathcal{G}$, i.e. $f^{-1}(S)\in\mathcal{A}$ for *all* $S\in\mathcal{A}'$ — $f$ is measurable. The converse is trivial.

**Step 3 — (c) Specialisation.** The rays $\{(-\infty,a):a\in\mathbb{R}\}$ generate $\mathcal{B}(\mathbb{R})$, so by (b) $f$ is Borel measurable iff $f^{-1}((-\infty,a))=\{f<a\}\in\mathcal{A}$ for all $a$. For continuous $f:\mathbb{R}^n\to\mathbb{R}^m$: open sets generate $\mathcal{B}(\mathbb{R}^m)$, and $f^{-1}(\text{open})$ is open hence Borel; apply (b).

> [!note]- Complete formal solution
> (a) $f^{-1}$ preserves $Y$, complements, countable unions, so $\mathcal{G}$ inherits the three $\sigma$-algebra axioms from $\mathcal{A}$. (b) $\mathcal{E}'\subseteq\mathcal{G}$ and $\mathcal{G}$ a $\sigma$-algebra force $\sigma(\mathcal{E}')\subseteq\mathcal{G}$; as $\sigma(\mathcal{E}')=\mathcal{A}'$, $f$ is measurable. (c) Rays generate $\mathcal{B}(\mathbb{R})$, giving the $\{f<a\}$ criterion; for continuous $f$, $f^{-1}(\text{open})$ is open, and open sets generate $\mathcal{B}(\mathbb{R}^m)$. $\blacksquare$

---

# Key Takeaways

**To check measurability, never test all measurable target sets — test only a generating family.** The family of "good targets" $\mathcal{G}=\{S:f^{-1}(S)\in\mathcal{A}\}$ is *always* a $\sigma$-algebra, because preimage is a Boolean homomorphism. So containing the generators forces containing everything. This collapses an uncountable verification to a one-parameter one ($\{f<a\}$ for $a\in\mathbb{R}$), and it is the reason continuity implies Borel measurability in a single line.

**This is the [[Def - Generated σ-Algebra|minimality principle]] — "the good objects form a $\sigma$-algebra, hence contain the generated one" — and it is the universal proof skeleton of the subject.** The identical move proves the operations of [[Thm - Operations Preserve Measurability|preserve measurability]], proves Dynkin's $\pi$–$\lambda$ theorem, and proves uniqueness of measures. Whenever you must establish a property "for all Borel sets," form the family of sets having it, show that family is a $\sigma$-algebra containing a generating set, and you are done.
