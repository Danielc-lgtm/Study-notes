---
type: theorem
subject: measure-theory
prereqs:
  - "Thm - Hahn-Carathéodory Extension Theorem"
  - "Def - σ-Finite Measure"
  - "Def - Pre-Measure"
tags: [analysis, measure-theory]
---

# Notation

$X$ a set, $\mathcal{A}\subseteq 2^X$ an [[Def - Algebra and σ-Algebra|algebra]], $\widetilde\mu:\mathcal{A}\to[0,\infty]$ a [[Def - Pre-Measure|pre-measure]]. $\mu=\mu^*|_\Sigma$ is the [[Thm - Hahn-Carathéodory Extension Theorem|Hahn–Carathéodory extension]]; $\Sigma$ its Carathéodory $\sigma$-algebra.

---

# Motivation

The [[Thm - Hahn-Carathéodory Extension Theorem|extension theorem]] proves a pre-measure *can* be extended to a measure. But "can" is not "must in only one way." Without further hypotheses, a pre-measure may extend to *genuinely different* measures on $\sigma(\mathcal{A})$ — and then it is meaningless to speak of "*the* Lebesgue measure" or "*the* law of $X$." This theorem supplies the missing word **the**: under [[Def - σ-Finite Measure|σ-finiteness]], the extension is unique. Existence plus uniqueness is what licenses the definite article throughout measure theory and probability.

---

# Sources and Targets

**Sources.** The hypothesis is "$\widetilde\mu$ is $\sigma$-finite." The non-obvious recognitions: a *finite* pre-measure is $\sigma$-finite (take $S_1=X$); *elementary volume on $\mathbb{R}^n$* is $\sigma$-finite (tile by unit cubes); a *pre-measure agreeing with a probability measure on a generating $\pi$-system* is finite, hence covered — this is the form used constantly in probability ([[Thm - Dynkin's π-λ Theorem|Dynkin's lemma]]). The bridge in each case is exhibiting a countable finite-measure exhaustion.

**Targets.** Uniqueness, combined with existence, yields the definite objects: *the* [[Def - Lebesgue Measure|Lebesgue measure]], *the* [[Def - Product σ-Algebra|product measure]], *the* law of a random variable from its [[Def - Distribution Function|distribution function]]. Combined with *translation invariance of elementary volume*, uniqueness gives that Lebesgue measure is **the** unique translation-invariant measure with $\lambda([0,1]^n)=1$ — a characterisation, not just a construction.

---

# Formal Statement

Under the hypotheses of the [[Thm - Hahn-Carathéodory Extension Theorem|extension theorem]], suppose in addition that $\widetilde\mu$ is **$\sigma$-finite**: there exist pairwise disjoint $S_k\in\mathcal{A}$ with $X=\bigsqcup_k S_k$ and $\widetilde\mu(S_k)<\infty$. Then the extension is **unique** in the following sense: if $\nu:2^X\to[0,\infty]$ is any outer measure with $\nu|_\mathcal{A}=\widetilde\mu$, then $\nu|_\Sigma=\mu$.

Equivalently: any two measures on $\sigma(\mathcal{A})$ that agree with $\widetilde\mu$ on the algebra $\mathcal{A}$ coincide on all of $\sigma(\mathcal{A})$.

---

# Why Is It True

Two measures that agree on the algebra $\mathcal{A}$ — why must they agree on the much larger $\sigma(\mathcal{A})$? The mechanism is *approximation from outside plus subtraction*.

First, the easy half. For any $A\in\Sigma$, any algebra-cover $(A_k)$ of $A$ gives $\nu(A)\le\sum\nu(A_k)=\sum\widetilde\mu(A_k)$ by subadditivity; infimising over covers yields $\nu(A)\le\mu^*(A)=\mu(A)$. So *any* extension is $\le$ the Carathéodory one. One inequality is automatic.

Now the reverse, and this is where $\sigma$-finiteness is spent. Suppose first $A$ is contained in a single set $S\in\mathcal{A}$ of finite measure. Apply the easy half to *both* $A$ and its relative complement $S\setminus A$:
$$\nu(A)+\nu(S\setminus A)\le\mu(A)+\mu(S\setminus A)=\mu(S)=\widetilde\mu(S)=\nu(S)\le\nu(A)+\nu(S\setminus A).$$
The two ends are equal, so the chain collapses: every "$\le$" is an "$=$." In particular $\nu(A)=\mu(A)$. The crucial move was *subtraction* — "$\nu(A)=\nu(S)-\nu(S\setminus A)$" — and subtraction of $\infty$ is forbidden, so $S$ *had* to have finite measure. That is the entire role of $\sigma$-finiteness: it guarantees enough finite-measure "windows" $S$.

Finally, a general $A\in\Sigma$ is cut into the pieces $A\cap S_k$, each inside a finite-measure window, each handled above; countable additivity of *both* $\nu$ and $\mu$ reassembles $\nu(A)=\sum\nu(A\cap S_k)=\sum\mu(A\cap S_k)=\mu(A)$.

The failure without $\sigma$-finiteness is real: on an algebra where every nonempty set has infinite pre-measure, the subtraction step is unavailable and distinct extensions coexist.

---

# What Makes This Hard

The only subtle point is *where finiteness is used*: not to make sums converge, but to license the **subtraction** $\nu(A)=\nu(S)-\nu(S\setminus A)$. The common error is to think $\sigma$-finiteness is a technical convenience; in fact uniqueness genuinely *fails* without it, and the proof pinpoints why — an infinite-measure window cannot be subtracted across. The second mild subtlety is remembering that one only proves "$\le$" directly and gets "$=$" by *squeezing*, applying "$\le$" to $A$ and to its complement simultaneously.

---

# Rederivation Scaffold

**High-level strategy.** Prove every extension is $\le$ the Carathéodory one (subadditivity). Upgrade to "$=$" on finite-measure windows by applying that inequality to a set and its complement and squeezing. Globalise via the $\sigma$-finite decomposition and countable additivity.

**Subgoal decomposition.**

1. **Any extension $\nu$ satisfies $\nu\le\mu$ on $\Sigma$.** For $A\in\Sigma$ and an algebra-cover $(A_k)$, $\nu(A)\le\sum\widetilde\mu(A_k)$; infimise.
   - *Why needed:* one half for free; reused for $A$ and for $S\setminus A$.
2. **$\nu=\mu$ on sets inside a finite window.** For $A\subseteq S$, $S\in\mathcal{A}$, $\widetilde\mu(S)<\infty$: apply step 1 to $A$ and $S\setminus A$, use $\nu(S)=\mu(S)$, squeeze.
   - *Hint:* the chain of inequalities has equal endpoints — collapse it.
3. **Globalise.** Decompose $A=\bigsqcup_k(A\cap S_k)$ via $\sigma$-finiteness; apply step 2 to each piece; sum by countable additivity.

---

# Lemma Decomposition

> [!note]- Lemma 1: Every extension is dominated by the Carathéodory extension
> **Statement:** If $\nu$ is an outer measure with $\nu|_\mathcal{A}=\widetilde\mu$, then $\nu(A)\le\mu(A)$ for all $A\in\Sigma$.
>
> **Hint:** Subadditivity of $\nu$ over an algebra-cover, then infimise.
>
> > [!note]- Full proof
> > Let $A\in\Sigma$ and $A_k\in\mathcal{A}$ with $A\subseteq\bigcup_k A_k$. By subadditivity of the outer measure $\nu$, $\nu(A)\le\sum_k\nu(A_k)=\sum_k\widetilde\mu(A_k)$. Taking the infimum over all such algebra-covers gives $\nu(A)\le\mu^*(A)=\mu(A)$. $\square$

> [!note]- Lemma 2: Agreement on a finite window
> **Statement:** If $A\in\Sigma$, $S\in\mathcal{A}$, $A\subseteq S$, $\widetilde\mu(S)<\infty$, then $\nu(A)=\mu(A)$.
>
> **Hint:** Apply Lemma 1 to $A$ and to $S\setminus A$; the inequalities are forced to equalities.
>
> > [!note]- Full proof
> > Both $A$ and $S\setminus A$ lie in $\Sigma$. By Lemma 1, $\nu(A)\le\mu(A)$ and $\nu(S\setminus A)\le\mu(S\setminus A)$. Adding and using finite additivity of $\mu$ and of $\nu$,
> > $$\nu(S)=\nu(A)+\nu(S\setminus A)\le\mu(A)+\mu(S\setminus A)=\mu(S).$$
> > But $\nu(S)=\widetilde\mu(S)=\mu(S)$ since $S\in\mathcal{A}$. So the inequality is an equality, forcing $\nu(A)=\mu(A)$ (and $\nu(S\setminus A)=\mu(S\setminus A)$). The cancellation $\nu(A)=\nu(S)-\nu(S\setminus A)$ is legitimate because $\nu(S)=\widetilde\mu(S)<\infty$. $\square$

> [!note]- Lemma 3: Globalisation
> **Statement:** $\nu(A)=\mu(A)$ for all $A\in\Sigma$.
>
> **Hint:** Cut $A$ by the $\sigma$-finite exhaustion; sum.
>
> > [!note]- Full proof
> > Write $X=\bigsqcup_k S_k$ with $S_k\in\mathcal{A}$, $\widetilde\mu(S_k)<\infty$. Then $A=\bigsqcup_k(A\cap S_k)$, each $A\cap S_k\subseteq S_k$ a finite window, so $\nu(A\cap S_k)=\mu(A\cap S_k)$ by Lemma 2. By $\sigma$-additivity of $\nu$ and of $\mu$, $\nu(A)=\sum_k\nu(A\cap S_k)=\sum_k\mu(A\cap S_k)=\mu(A)$. $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> Lemmas 1–3. Lemma 3 is the assertion $\nu|_\Sigma=\mu$. In particular any two measures on $\sigma(\mathcal{A})\subseteq\Sigma$ that restrict to $\widetilde\mu$ on $\mathcal{A}$ agree on $\sigma(\mathcal{A})$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

Uniqueness is what makes *characterisation* theorems possible. **Lebesgue measure is the unique translation-invariant Borel measure with $\lambda([0,1]^n)=1$**: any such measure agrees with $\lambda$ on dyadic boxes by translation invariance, the dyadic boxes generate, and uniqueness finishes. In probability, **a law is determined by its [[Def - Distribution Function|distribution function]]** (or its [[Def - Characteristic Function|characteristic function]]) for exactly this reason — two laws agreeing on the generating $\pi$-system of rays $(-\infty,t]$ must coincide. The $\pi$-system version is [[Thm - Dynkin's π-λ Theorem|Dynkin's lemma]].

---

# Bridges

- **[[Thm - Dynkin's π-λ Theorem]]** — the "agree on a $\pi$-system $\Rightarrow$ agree everywhere" uniqueness principle, which is the form of this theorem used pervasively in probability; it makes the $\sigma$-finite hypothesis into "$X$ is a countable union of $\pi$-system sets of finite measure."
- **[[Thm - Hahn-Carathéodory Extension Theorem]]** — supplies existence; this theorem supplies uniqueness; together: "*the*" measure.
- **[[Def - Lebesgue Measure]]**, **[[Def - Distribution Function]]** — the definite objects this theorem licenses.
