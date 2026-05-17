---
type: exercise
subject: measure-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Convergence in Measure"
  - "Def - Almost Everywhere"
tags: [analysis, measure-theory, probability]
---

# Problem Statement

On $([0,1],\lambda)$ define the **typewriter sequence**: enumerate the dyadic intervals $I_{m,k}=[k2^{-m},(k+1)2^{-m}]$, $m\ge0$, $0\le k<2^m$, in order of increasing $m$ and then increasing $k$, and let $f_1,f_2,\dots$ be their indicators.

**(a)** Show $f_n\xrightarrow{\lambda}0$ in [[Def - Convergence in Measure|measure]].

**(b)** Show $f_n(x)\not\to0$ for **any** $x\in[0,1]$ — the sequence converges a.e. nowhere.

**(c)** Show that nevertheless a subsequence converges to $0$ a.e., consistent with the general theorem "convergence in measure $\Rightarrow$ a.e.-convergent subsequence."

**Recall:**

![[Def - Convergence in Measure#The Definition]]

---

# Convergent Strategy

**Problem class:** separating the modes of convergence by an explicit witness.

**Assumption pattern:** the dyadic indicators have $\lambda(\{f_n>0\})=2^{-m}\to0$ — so the *bad set shrinks*, giving convergence in measure. But the bad set, though shrinking, *sweeps over every point repeatedly* — so no point converges.

**Theorem routing:** (a) $\lambda(\{f_n>\varepsilon\})\le2^{-m(n)}\to0$; (b) each $x$ lies in some $I_{m,k}$ for every $m$, so $f_n(x)=1$ infinitely often; (c) pick one interval per level $m$.

**Key decision point:** the distinction between "the bad *set* shrinks" (measure) and "each *point* is eventually good" (a.e.) — the typewriter has the first, not the second.

---

# Legal Operations Used

1. **Compute the measure of the support** of each $f_n$.
2. **Track a fixed point** through the sweeping intervals.
3. **Extract a subsequence** by selecting one interval per dyadic level.

---

# Hints

> [!note]- Hint 1
> The $n$-th function is $\mathbf{1}_{I_{m,k}}$ for some $m=m(n)\to\infty$. So $\lambda(\{f_n>\varepsilon\})=\lambda(I_{m,k})=2^{-m}$ for $\varepsilon<1$.

> [!note]- Hint 2
> Fix $x$. At every level $m$, $x$ lies in some interval $I_{m,k}$, so $f_n(x)=1$ for that $n$. As $m\to\infty$ there are infinitely many such $n$.

> [!note]- Hint 3
> For (c): from each level $m$ pick the *one* interval containing a fixed point, or just take $f_{n_m}=\mathbf{1}_{I_{m,0}}=\mathbf{1}_{[0,2^{-m}]}$.

---

# Solution

**Step 1 — (a) Convergence in measure.** The $n$-th function is $f_n=\mathbf{1}_{I_{m(n),k(n)}}$ where the level $m(n)\to\infty$ as $n\to\infty$ (each level $m$ contributes only $2^m$ functions, finitely many). For $0<\varepsilon<1$,
$$\lambda(\{f_n>\varepsilon\})=\lambda(I_{m(n),k(n)})=2^{-m(n)}\xrightarrow[n\to\infty]{}0.$$
So $f_n\xrightarrow{\lambda}0$ in measure.

**Step 2 — (b) No pointwise convergence.** Fix any $x\in[0,1]$. For every level $m$, $x$ belongs to exactly one (or a boundary pair of) dyadic interval $I_{m,k}$, and the corresponding $f_n$ has $f_n(x)=1$. Since there is such an $n$ for every $m$, and $m\to\infty$, $f_n(x)=1$ for *infinitely many* $n$. Also $f_n(x)=0$ for infinitely many $n$ (most intervals miss $x$). So $(f_n(x))$ has both $0$ and $1$ as subsequential limits — it does not converge, for *any* $x$. The sequence converges almost nowhere.

**Step 3 — (c) An a.e.-convergent subsequence.** Take $f_{n_m}=\mathbf{1}_{[0,2^{-m}]}$ (the first interval of level $m$). Then for any fixed $x>0$, $f_{n_m}(x)=0$ once $2^{-m}<x$, so $f_{n_m}(x)\to0$ for every $x\in(0,1]$ — convergence everywhere except the null set $\{0\}$, hence a.e.

> [!note]- Derivation
> This realises the general principle: $f_n\xrightarrow{\mu}0$ lets one extract $n_m$ with $\lambda(\{f_{n_m}>2^{-m}\})<2^{-m}$; the [[Ex - The first Borel-Cantelli lemma|first Borel–Cantelli lemma]] then forces $f_{n_m}\to0$ a.e. The typewriter shows the *full* sequence cannot be salvaged — only a subsequence.

> [!note]- Complete formal solution
> (a) $f_n=\mathbf{1}_{I_{m(n),k(n)}}$ with $m(n)\to\infty$; $\lambda(\{f_n>\varepsilon\})=2^{-m(n)}\to0$, so $f_n\xrightarrow{\lambda}0$. (b) Every $x$ lies in some level-$m$ interval for each $m$, so $f_n(x)=1$ infinitely often and $f_n(x)=0$ infinitely often — no limit. (c) $f_{n_m}=\mathbf{1}_{[0,2^{-m}]}\to0$ on $(0,1]$, i.e. a.e. $\blacksquare$

---

# Key Takeaways

**Convergence in measure and a.e. convergence are genuinely different, and the typewriter sequence is the canonical separating example: the bad *set* can shrink to nothing while no *point* ever settles down.** Convergence in measure tracks $\lambda(\{f_n\text{ bad}\})$; a.e. convergence tracks each point's trajectory. The typewriter's bad set $I_{m,k}$ shrinks ($2^{-m}\to0$) but *sweeps*, revisiting every point infinitely often — so it converges in measure yet nowhere pointwise. Keeping "shrinking bad set" and "each point eventually good" mentally separate is essential.

**Convergence in measure always rescues an a.e.-convergent *subsequence* — never the whole sequence.** This is the standard repair: from $f_n\xrightarrow{\mu}f$ extract $n_k$ with $\mu(\{|f_{n_k}-f|>2^{-k}\})<2^{-k}$, then the [[Ex - The first Borel-Cantelli lemma|first Borel–Cantelli lemma]] gives $f_{n_k}\to f$ a.e. The subsequence trick is what makes convergence in measure usable in proofs (e.g. of the [[Thm - Vitali Convergence Theorem|Vitali theorem]]): one cannot assume the full sequence converges a.e., but one can always pass to a subsequence that does. In probability this is the relation between [[Def - Modes of Convergence|convergence in probability and almost-sure convergence]].
