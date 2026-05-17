---
type: exercise
subject: measure-theory
difficulty: "⭐"
prereqs:
  - "Thm - Fatou's Lemma"
  - "Thm - Dominated Convergence Theorem"
tags: [analysis, measure-theory]
---

# Problem Statement

**(a)** On $(\mathbb{R},\lambda)$ exhibit measurable $f_n\ge0$ with $f_n\to0$ pointwise but $\int f_n\,d\lambda\not\to0$, so that [[Thm - Fatou's Lemma|Fatou's lemma]] is *strictly* inequality: $\int\liminf f_n<\liminf\int f_n$. Do this with three mechanisms — escape to infinity, escape to a spike, escape to zero height over an expanding base.

**(b)** For each, identify which hypothesis of the [[Thm - Dominated Convergence Theorem|DCT]] fails, i.e. why no integrable dominator exists.

**Recall:**

![[Thm - Fatou's Lemma#Formal Statement]]

DCT needs a single $g\in L^1$ with $|f_n|\le g$ for all $n$.

---

# Convergent Strategy

**Problem class:** producing counterexamples that probe *how* mass is lost in a limit.

**Assumption pattern:** Fatou is strict exactly when mass *escapes* — present in $\int f_n$ but absent from $\int\liminf f_n$. There are three escape routes, and a good counterexample bank has one of each.

**Key decision point:** for each example, locate the escaping mass and confirm it cannot be capped by an integrable $g$.

---

# Legal Operations Used

1. **Three escape constructions** — translation, vertical spike, horizontal spreading.
2. **Negate domination** — show $\sup_n f_n\notin L^1$.

---

# Hints

> [!note]- Hint 1
> Escape to infinity: $f_n=\mathbf{1}_{[n,n+1]}$. Escape to a spike: $f_n=n\mathbf{1}_{[0,1/n]}$. Escape by spreading: $f_n=\tfrac1n\mathbf{1}_{[0,n]}$.

> [!note]- Hint 2
> In each, $\int f_n=1$ for all $n$, but $f_n\to0$ pointwise. So $\int\liminf f_n=0<1=\liminf\int f_n$.

> [!note]- Hint 3
> $\sup_n f_n$ would have to dominate the family. Compute or bound $\int\sup_n f_n$.

---

# Solution

**Step 1 — (a) Three escapes.** Each $f_n\ge0$ is measurable with $\int f_n\,d\lambda=1$, yet $f_n(x)\to0$ for every $x$, giving $\int\liminf f_n=\int 0=0<1=\liminf\int f_n$.

> [!note]- Derivation
> *Escape to infinity.* $f_n=\mathbf{1}_{[n,n+1]}$: for fixed $x$, $f_n(x)=0$ once $n>x$; $\int f_n=\lambda([n,n+1])=1$. The bump translates rightward forever.
> *Escape to a spike.* $f_n=n\,\mathbf{1}_{[0,1/n]}$: for fixed $x>0$, $f_n(x)=0$ once $1/n<x$; $f_n(0)=n$ but $\{0\}$ is null, so $f_n\to0$ a.e. (indeed pointwise off $0$); $\int f_n=n\cdot\tfrac1n=1$. Mass concentrates into an ever-taller, ever-thinner spike.
> *Escape by spreading.* $f_n=\tfrac1n\mathbf{1}_{[0,n]}$: $f_n(x)\le\tfrac1n\to0$ everywhere; $\int f_n=\tfrac1n\cdot n=1$. Mass flattens out over an expanding base.

**Step 2 — (b) Why no dominator.** In each case the family is *not dominated* by any $g\in L^1$, which is why [[Thm - Dominated Convergence Theorem|DCT]] does not apply (and Fatou, the weaker one-sided survivor, is strict).

> [!note]- Derivation
> *Infinity:* $\sup_n f_n=\mathbf{1}_{[1,\infty)}$, with $\int\sup_n f_n=\infty$ — no integrable cap.
> *Spike:* $\sup_n f_n(x)=\sup\{n:1/n\ge x\}\approx1/x$ for small $x>0$, and $\int_0^1\frac1x\,dx=\infty$ — the pointwise supremum is the non-integrable $1/x$.
> *Spreading:* $\sup_n f_n(x)\ge\tfrac1{\lceil x\rceil}$ for $x$ in $[0,n]$, comparable to $1/x$ at infinity, again non-integrable.
> In all three the would-be dominator $\sup_n f_n$ has infinite integral, so the hypothesis "$\exists g\in L^1$, $f_n\le g$" of DCT fails — and Fatou's one-sided inequality is the best that survives.

> [!note]- Complete formal solution
> (a) $f_n=\mathbf{1}_{[n,n+1]}$, $n\mathbf{1}_{[0,1/n]}$, $\tfrac1n\mathbf{1}_{[0,n]}$ each have $\int f_n=1$ and $f_n\to0$ (pointwise, resp. a.e.), so $\int\liminf f_n=0<1=\liminf\int f_n$. (b) For each, $\sup_n f_n$ has infinite integral ($\mathbf{1}_{[1,\infty)}$, resp. $\sim1/x$ near $0$, resp. $\sim1/x$ at $\infty$), so no $L^1$ dominator exists and DCT does not apply. $\blacksquare$

---

# Key Takeaways

**Fatou's lemma is strict precisely when mass escapes, and mass escapes in exactly three ways: to spatial infinity, into a vertical spike, or by horizontal spreading.** These are the canonical counterexample family — every "the integral did not converge" pathology is one of them. Carrying all three in mind makes one fluent at *predicting* whether a convergence theorem applies: ask "can the mass run off the edge, concentrate, or flatten out?" If yes, expect strict Fatou and look for the missing dominator.

**The common cause of all three failures is the absence of an integrable dominating function** — $\sup_n f_n\notin L^1$. The dominator's job is to *pin the mass in place*; without it, [[Thm - Dominated Convergence Theorem|DCT]] cannot run and only Fatou's one-directional inequality survives. The reaction pattern: when an interchange of limit and integral is in question, compute (or bound) $\sup_n|f_n|$ and test its integrability — that single test decides whether DCT is available.
