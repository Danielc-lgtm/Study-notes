---
type: exercise
subject: measure-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - Egorov's Theorem"
  - "Def - Almost Everywhere"
tags: [analysis, measure-theory]
---

# Problem Statement

Let $(X,\mathcal{A},\mu)$ be a measure space with $\mu(X)<\infty$ and $f_n\to f$ $\mu$-a.e.

**(a)** Using [[Thm - Egorov's Theorem|Egorov's theorem]], show there is an *increasing* sequence of measurable sets $F_1\subseteq F_2\subseteq\cdots$ with $\mu(X\setminus F_m)\to0$ and $f_n\to f$ uniformly on each $F_m$.

**(b)** Deduce that $f_n\to f$ in [[Def - Convergence in Measure|measure]].

**(c)** Deduce that if additionally $|f_n|\le M$ for a constant $M$, then $\int|f_n-f|\,d\mu\to0$ (**bounded convergence theorem**), directly from (a).

**Recall:**

![[Thm - Egorov's Theorem#Formal Statement]]

A sequence converges **in measure** if $\mu(|f_n-f|>\varepsilon)\to0$ for all $\varepsilon>0$.

---

# Convergent Strategy

**Problem class:** extracting consequences of Egorov — turning "uniform off a small set" into other convergence statements.

**Assumption pattern:** Egorov gives *one* good set per tolerance $\delta$; running $\delta=1/m$ produces a *sequence* of good sets, and they can be made increasing by unioning.

**Theorem routing:** Egorov $\Rightarrow$ good sets $F_m$; on $F_m$ uniform convergence kills $\mu(|f_n-f|>\varepsilon)$ up to $\mu(X\setminus F_m)$; for (c), split $\int|f_n-f|$ over $F_m$ and its complement.

**Key decision point:** the split $\int=\int_{F_m}+\int_{X\setminus F_m}$, with uniform convergence handling the first piece and the *boundedness* $|f_n-f|\le2M$ handling the second.

---

# Legal Operations Used

1. **Run Egorov at $\delta=1/m$**, union the good sets to make them increasing.
2. **Split an integral** over a good set and a small bad set.
3. **Uniform convergence on a finite-measure set** $\Rightarrow$ integral $\to0$ there.

---

# Hints

> [!note]- Hint 1
> Apply Egorov with $\delta=1/m$ to get $E_m$ with $\mu(X\setminus E_m)<1/m$; set $F_m=E_1\cup\cdots\cup E_m$.

> [!note]- Hint 2
> On $F_m$, $f_n\to f$ uniformly. So $\{|f_n-f|>\varepsilon\}\subseteq X\setminus F_m$ for large $n$. Bound its measure.

> [!note]- Hint 3
> For (c): $\int|f_n-f|=\int_{F_m}+\int_{X\setminus F_m}$. First term $\le\mu(X)\sup_{F_m}|f_n-f|\to0$; second $\le2M\,\mu(X\setminus F_m)$.

---

# Solution

**Step 1 — (a).** For each $m$, Egorov ($\delta=1/m$) gives measurable $E_m$ with $\mu(X\setminus E_m)<1/m$ and $f_n\to f$ uniformly on $E_m$. Set $F_m=\bigcup_{k\le m}E_k$. Then $F_m\uparrow$, $\mu(X\setminus F_m)\le\mu(X\setminus E_m)<1/m\to0$, and $f_n\to f$ uniformly on $F_m\supseteq E_m$ (uniform convergence on a superset... wait — on $E_m$, and $F_m\supseteq E_m$; uniform convergence holds on each $E_k$, hence on the finite union $F_m$, since a finite union of sets of uniform convergence is a set of uniform convergence).

**Step 2 — (b).** Fix $\varepsilon>0$. On $F_m$, $\sup_{F_m}|f_n-f|\to0$, so for $n\ge N(m)$, $\{|f_n-f|>\varepsilon\}\cap F_m=\emptyset$, whence $\{|f_n-f|>\varepsilon\}\subseteq X\setminus F_m$ and $\mu(|f_n-f|>\varepsilon)\le\mu(X\setminus F_m)<1/m$. Given any target, choose $m$ then $N(m)$: $\mu(|f_n-f|>\varepsilon)\to0$.

**Step 3 — (c) Bounded convergence.** Fix $\varepsilon>0$, pick $m$ with $\mu(X\setminus F_m)<\varepsilon$. For $n\ge N(m)$, $\sup_{F_m}|f_n-f|<\varepsilon/\mu(X)$ (uniform convergence), so
$$\int|f_n-f|\,d\mu=\int_{F_m}|f_n-f|+\int_{X\setminus F_m}|f_n-f|\le\mu(X)\cdot\frac{\varepsilon}{\mu(X)}+2M\,\mu(X\setminus F_m)<\varepsilon+2M\varepsilon.$$
Since $\varepsilon$ is arbitrary, $\int|f_n-f|\,d\mu\to0$.

> [!note]- Derivation
> The bound $|f_n-f|\le|f_n|+|f|\le2M$ (the a.e. limit $f$ also satisfies $|f|\le M$) controls the bad-set integral; uniform convergence controls the good-set integral. The finiteness $\mu(X)<\infty$ enters twice — in Egorov, and in $\int_{F_m}\le\mu(X)\sup$.

> [!note]- Complete formal solution
> (a) Egorov at $\delta=1/m$ gives $E_m$; $F_m=\bigcup_{k\le m}E_k$ is increasing with $\mu(X\setminus F_m)<1/m$ and uniform convergence on $F_m$. (b) $\{|f_n-f|>\varepsilon\}\subseteq X\setminus F_m$ for $n$ large, so $\mu(|f_n-f|>\varepsilon)\le1/m$; let $m\to\infty$. (c) Split $\int|f_n-f|$ over $F_m$ (uniform convergence, $\le\mu(X)\sup$) and $X\setminus F_m$ ($\le2M\mu(X\setminus F_m)$); both $\to0$. $\blacksquare$

---

# Key Takeaways

**Egorov is the conversion station between modes of convergence: it turns a.e. convergence into "uniform off a small set," from which convergence in measure and (with a bound) $L^1$-convergence follow immediately.** On a finite-measure space, a.e. convergence implies convergence in measure — and this exercise shows the implication *is* Egorov plus a one-line bound. The recurring move: run Egorov at $\delta=1/m$, get a sequence of ever-larger good sets, and prove each desired convergence statement on the good set (where convergence is uniform, hence trivial) while controlling the small bad set separately.

**The bounded convergence theorem is "$L^1$-convergence for a uniformly bounded sequence on a finite-measure space" and falls straight out of the split $\int=\int_{\text{good}}+\int_{\text{bad}}$.** This split — uniform convergence handles the good set, the uniform bound handles the small bad set — is the *same architecture* as the proof of the [[Thm - Vitali Convergence Theorem|Vitali convergence theorem]], where the uniform bound is replaced by the more flexible [[Def - Uniform Integrability|uniform integrability]]. Recognising "split at a good set" as the universal template for upgrading convergence is the transferable skill.
