---
type: exercise
subject: measure-theory
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Vitali Convergence Theorem"
  - "Thm - Dominated Convergence Theorem"
  - "Def - Absolute Continuity and Density"
tags: [analysis, measure-theory]
---

# Problem Statement

**(a)** Construct a sequence $f_n\in L^1([0,1],\lambda)$ with $f_n\to0$ in $L^1$ (so $\int|f_n|\,d\lambda\to0$) for which there is **no** $g\in L^1$ with $|f_n|\le g$ for all $n$. Conclude that the [[Thm - Dominated Convergence Theorem|dominated convergence theorem]] is strictly weaker than the [[Thm - Vitali Convergence Theorem|Vitali convergence theorem]].

**(b)** Verify directly that your sequence *is* uniformly integrable and converges in measure, so that Vitali applies even though DCT does not.

**Recall:**

[[Thm - Vitali Convergence Theorem|Vitali]]: on a finite-measure space, $\int|f_n-f|\to0$ iff $f_n\xrightarrow{\mu}f$ and $(f_n)$ is [[Def - Absolute Continuity and Density|uniformly integrable]]. [[Thm - Dominated Convergence Theorem|DCT]] needs a single $g\in L^1$ dominating all $f_n$.

---

# Convergent Strategy

**Problem class:** separating two theorems — showing Vitali strictly subsumes DCT.

**Assumption pattern:** DCT needs $\sup_n|f_n|\in L^1$. To defeat it while keeping $L^1$-convergence, make the *peaks* of $f_n$ wander so that $\sup_n|f_n|$ is large on a big set, yet each individual $f_n$ has small $L^1$ norm.

**Theorem routing:** moving bumps of height $h_n\to\infty$ slowly and width $w_n$ with $h_n w_n\to0$: $\|f_n\|_1=h_n w_n\to0$ ($L^1$-convergence) but $\sup_n f_n$ picks up height $h_n$ at the $n$-th location, and if the locations tile $[0,1]$, $\sup_n f_n$ is unbounded on a full-measure set.

**Key decision point:** balancing $h_n w_n\to0$ (for $L^1$-convergence) against $\sup_n f_n\notin L^1$ (to kill DCT).

---

# Legal Operations Used

1. **Wandering bumps** with controlled height/width.
2. **Compute $\sup_n f_n$** and test its integrability.
3. **Verify UI** via the $L^1$-convergence criterion.

---

# Hints

> [!note]- Hint 1
> Let the bumps march across $[0,1]$: at "step $n$" place a bump of height $h_n$ on an interval $J_n$ of width $w_n$, with the $J_n$ cycling through $[0,1]$ so every point is hit infinitely often.

> [!note]- Hint 2
> Take $h_n\to\infty$ slowly and $w_n$ so that $h_n w_n\to0$. Then $\|f_n\|_1=h_n w_n\to0$.

> [!note]- Hint 3
> Concretely: along the dyadic intervals $I_{m,k}$ (typewriter order), set $f_n=\sqrt{m}\cdot\mathbf{1}_{I_{m,k}}$ where $m=m(n)$. Then $\|f_n\|_1=\sqrt m\,2^{-m}\to0$, but $\sup$ over level-$m$ functions is $\sqrt m$ on all of $[0,1]$.

---

# Solution

**Step 1 — (a) The wandering tall bumps.** Enumerate the dyadic intervals $I_{m,k}=[k2^{-m},(k+1)2^{-m}]$ in typewriter order ($m$ increasing, then $k$), giving $f_1,f_2,\dots$ with $f_n=\sqrt{m(n)}\cdot\mathbf{1}_{I_{m(n),k(n)}}$, where the level $m(n)\to\infty$.

> [!note]- Derivation
> *$L^1$-convergence:* $\|f_n\|_1=\sqrt{m(n)}\cdot\lambda(I_{m(n),k(n)})=\sqrt{m(n)}\cdot2^{-m(n)}\to0$, since $\sqrt m\,2^{-m}\to0$. So $\int|f_n-0|\,d\lambda\to0$.
> *No dominator:* suppose $g\in L^1$ with $|f_n|\le g$ for all $n$. At each level $m$, the $2^m$ functions $\sqrt m\,\mathbf{1}_{I_{m,k}}$ tile $[0,1]$, so $\sup_{n:m(n)=m}f_n=\sqrt m$ *everywhere* on $[0,1]$. Hence $g\ge\sqrt m$ on $[0,1]$ for *every* $m$, forcing $g=\infty$ everywhere — not in $L^1$. So no integrable dominator exists, and DCT cannot be applied to this $L^1$-convergent sequence.

This proves DCT is strictly weaker than Vitali: here the conclusion ($L^1$-convergence) holds, but DCT's hypothesis (a dominator) fails.

**Step 2 — (b) Vitali applies.** By the [[Thm - Vitali Convergence Theorem|Vitali theorem]] itself, $L^1$-convergence is *equivalent* to "convergence in measure $+$ uniform integrability," so the sequence must have both — but verify directly.

> [!note]- Derivation
> *Convergence in measure:* for $0<\varepsilon$, $\lambda(\{f_n>\varepsilon\})\le\lambda(I_{m(n),k(n)})=2^{-m(n)}\to0$.
> *Uniform integrability:* $\int_A|f_n|\,d\lambda=\sqrt{m(n)}\,\lambda(A\cap I_{m(n),k(n)})\le\sqrt{m(n)}\,\min(\lambda(A),2^{-m(n)})$. For large $m(n)$ this is $\le\sqrt{m}\,2^{-m}$, small; for the finitely many small $m(n)$, the corresponding $f_n$ form a finite family, automatically UI. Combining: $\sup_n\int_A|f_n|$ is small once $\lambda(A)$ is small. So $(f_n)$ is UI.
> Vitali (in measure $+$ UI) then *predicts* $L^1$-convergence — consistent with Step 1, and reached without any dominator.

> [!note]- Complete formal solution
> (a) $f_n=\sqrt{m(n)}\mathbf{1}_{I_{m(n),k(n)}}$ in typewriter order: $\|f_n\|_1=\sqrt m\,2^{-m}\to0$, so $f_n\to0$ in $L^1$; but at each level $m$ the bumps tile $[0,1]$ at height $\sqrt m$, so any dominator $g\ge\sqrt m$ everywhere for all $m$, forcing $g\equiv\infty\notin L^1$ — DCT inapplicable. (b) $\lambda(\{f_n>\varepsilon\})\le2^{-m(n)}\to0$ (in measure); $\int_A|f_n|\le\sqrt m\min(\lambda(A),2^{-m})$ is uniformly small for small $\lambda(A)$ (UI). So Vitali applies. $\blacksquare$

---

# Key Takeaways

**The Vitali convergence theorem strictly contains the dominated convergence theorem: domination is sufficient but not necessary for $L^1$-convergence; uniform integrability is the *exact* condition.** DCT demands a single integrable function capping the whole sequence — a rigid, often unavailable requirement. A sequence of *wandering tall bumps* can converge in $L^1$ while its pointwise supremum is non-integrable, killing DCT. [[Thm - Vitali Convergence Theorem|Vitali]] replaces "dominated" with "[[Def - Uniform Integrability|uniformly integrable]]," which (being equivalent to $L^1$-convergence given convergence in measure) is precisely what is needed — no more, no less.

**The design pattern for "$L^1$-convergent but not dominated": let the peaks wander and grow slowly.** Mass $\to0$ (so $L^1$-convergence) while peak height $\to\infty$ at locations that sweep the whole space (so $\sup_n|f_n|=\infty$, no dominator). The same pattern — wandering, slowly-growing spikes — is what makes an $L^1$-bounded [[Def - Martingale|martingale]] fail to be UI, and recognising it is the diagnostic for "is this convergence dominated, or merely uniformly integrable?"
