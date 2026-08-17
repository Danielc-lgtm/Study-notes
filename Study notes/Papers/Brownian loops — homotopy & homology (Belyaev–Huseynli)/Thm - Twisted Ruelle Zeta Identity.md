---
type: theorem
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Def - Ruelle Zeta Function and its Twist"
  - "Thm - Selberg Zeta Identity (Killing Case)"
tags: [paper, spectral-geometry, zeta-functions, loop-measures]
---

# Notation

- $\rho:\Gamma\to\mathrm{GL}(V_\rho)$ — a finite-dimensional complex representation, not necessarily unitary; $c_\rho$ its abscissa of convergence
- $R_X(s,\rho)=\prod_\gamma\det(I-\rho(\tau)e^{-s\ell_\gamma})$ — the [[Def - Ruelle Zeta Function and its Twist|twisted Ruelle zeta function]]
- $\kappa_-(s):=s(s-1)$ and $\kappa_+(s):=s(s+1)$ — the two killing rates
- $\mu^{\kappa_\pm(s)}_X$ — the corresponding killing loop measures; $L=m\ell_\gamma$
- $\tau$ — a representative of the primitive class of $\gamma$; $\operatorname{tr}\rho(\tau^m)$ its twisted weight

---

# Type card

> [!abstract] Type card — Corollary 4.6 (twisted Ruelle zeta identity)
> **Given.** A finite-dimensional complex representation $\rho:\Gamma\to\mathrm{GL}(V_\rho)$, not necessarily unitary, with abscissa $c_\rho$; and $\operatorname{Re}(s)>\max(c_\rho,\tfrac12)$. Set $\kappa_-(s)=s(s-1)$, $\kappa_+(s)=s(s+1)$, so that for $\operatorname{Re}(s)>\tfrac12$ the principal square root gives $\tfrac12+\sqrt{\tfrac14+\kappa_-(s)}=s$ and $\tfrac12+\sqrt{\tfrac14+\kappa_+(s)}=s+1$.
>
> **Produces.** $-\log R_X(s,\rho)$ as a $\rho$-weighted sum of **differences** $\mu^{\kappa_-(s)}_X-\mu^{\kappa_+(s)}_X$ of loop masses at the two killing rates, equal also to the elementary sum $\sum_{\gamma,m}\operatorname{tr}\rho(\tau^m)e^{-sm\ell_\gamma}/m$.
>
> **Lets you.** See exactly which zeta functions the loop measure reaches, and why the Selberg one is canonical: the Ruelle identity requires a difference of two loop measures at two killing rates, where Selberg requires one.

---

# Statement

> **Corollary 4.6 (twisted Ruelle zeta identity).** Let $\kappa_-(s):=s(s-1)$ and $\kappa_+(s):=s(s+1)$. For $\operatorname{Re}(s)>\tfrac12$ the principal square root satisfies
> $$\tfrac12+\sqrt{\tfrac14+\kappa_-(s)}=s,\qquad \tfrac12+\sqrt{\tfrac14+\kappa_+(s)}=s+1.$$
> Then, for $\operatorname{Re}(s)>\max(c_\rho,\tfrac12)$,
> $$-\log R_X(s,\rho) = \sum_{\gamma\in\mathcal{P}_X}\sum_{m=1}^\infty\operatorname{tr}\rho(\tau^m)\Big[\mu^{\kappa_-(s)}_X\big(\mathcal{C}_X(\gamma^m)\big)-\mu^{\kappa_+(s)}_X\big(\mathcal{C}_X(\gamma^m)\big)\Big] = \sum_{\gamma\in\mathcal{P}_X}\sum_{m=1}^\infty\frac{\operatorname{tr}\rho(\tau^m)\,e^{-sm\ell_\gamma}}{m}.\tag{39}$$

---

# Why it is true

Two independent computations that meet in the middle.

**From the zeta side**, expanding the twisted product: $-\log\det(I-M)=\sum_{m\geq1}\operatorname{tr}(M^m)/m$ applied to $M=\rho(\tau)e^{-s\ell_\gamma}$ gives immediately
$$-\log R_X(s,\rho) = \sum_{\gamma}\sum_{m\geq1}\frac{\operatorname{tr}\rho(\tau^m)}{m}\,e^{-sm\ell_\gamma},$$
which is the right-hand equality of (39). Nothing probabilistic has happened yet.

**From the loop side**, the difference telescopes. By the killing mass formula (26), with $L=m\ell_\gamma$,
$$\mu^{\kappa_-(s)}_X\big(\mathcal{C}_X(\gamma^m)\big) - \mu^{\kappa_+(s)}_X\big(\mathcal{C}_X(\gamma^m)\big) = \frac1m\cdot\frac{e^{(1-s)L}-e^{-sL}}{e^L-1} = \frac{e^{-sL}}{m},$$
because $e^{(1-s)L}-e^{-sL}=e^{-sL}(e^L-1)$ — **the denominator cancels exactly**. Matching term by term gives (39).

**The mechanism in one line: the $1/(e^L-1)$ factor that the Selberg $k$-product creates is annihilated by taking the difference of the loop masses at spectral parameters $s$ and $s+1$, leaving the bare $e^{-sL}/m$ that the Ruelle product wants.**

The structural reading is the one to keep. The Selberg zeta function has an extra product over $k\geq0$, which is what supplies the factor $1/(e^L-1)$; Ruelle has none, so a single loop mass overshoots by exactly that factor. Taking a difference at consecutive spectral parameters is precisely the inverse of summing the geometric series over $k$, since $Z_X(s)=\prod_{k\geq0}R_X(s+k)$ implies $R_X(s)=Z_X(s)/Z_X(s+1)$. **The difference of two loop measures is the probabilistic shadow of dividing $Z_X(s)$ by $Z_X(s+1)$.**

What this costs: the object expressed is a *signed* combination, so nothing about it is a mass. The [[Thm - Poissonian Structure of Homotopy Classes|Poissonian interpretation]] does not survive a difference — one cannot speak of the number of loops in a class whose mass is $\mu^{\kappa_-}-\mu^{\kappa_+}$. That is the concrete content of the paper's judgement that dynamical-zeta identities are "more difficult to use in a meaningful way".

What the difference *does* mean: passing from $\kappa_-$ to $\kappa_+$ suppresses longer loops more strongly (larger killing rate, faster decay), so the difference isolates the **net contribution of each homotopy class between the two rates**.

---

# Strategy

**Strategy.** Expand $-\log\det(I-M)=\sum_{m\geq1}\operatorname{tr}(M^m)/m$ on the twisted product; separately compute the difference of the two killing masses from (26), observing that $e^{(1-s)L}-e^{-sL}=e^{-sL}(e^L-1)$ cancels the denominator; match term by term.

> [!note]- Proof (skippable)
> Expanding the logarithm of (38) via $-\log\det(I-M)=\sum_{m\geq1}\operatorname{tr}(M^m)/m$ with $M=\rho(\tau)e^{-s\ell_\gamma}$,
> $$-\log R_X(s,\rho) = \sum_{\gamma\in\mathcal{P}_X}\sum_{m=1}^\infty\frac{\operatorname{tr}\rho(\tau^m)\,e^{-sm\ell_\gamma}}{m}.$$
>
> By (26), and writing $L=m\ell_\gamma$,
> $$\mu^{\kappa_-(s)}_X\big(\mathcal{C}_X(\gamma^m)\big)-\mu^{\kappa_+(s)}_X\big(\mathcal{C}_X(\gamma^m)\big) = \frac1m\cdot\frac{e^{(1-s)L}-e^{-sL}}{e^{L}-1} = \frac{e^{-sL}}{m},$$
> since $e^{(1-s)L}-e^{-sL}=e^{-sL}(e^L-1)$. The spectral parameters attached to $\kappa_-(s)$ and $\kappa_+(s)$ are $s$ and $s+1$ respectively, by the stated square-root identities, so the two masses are $\frac1m\frac{e^{(1-s)L}}{e^L-1}$ and $\frac1m\frac{e^{-sL}}{e^L-1}$.
>
> Matching term by term gives (39), and absolute convergence for $\operatorname{Re}(s)>\max(c_\rho,\tfrac12)$ follows from that of the product. $\;\square$

---

# What this assumes, and where to climb

**The twisted product and its convergence** — [[Def - Ruelle Zeta Function and its Twist]]. The abscissa $c_\rho$ is governed by $\|\rho(\tau)\|\leq C_\rho e^{c\ell_\gamma}$; for unitary $\rho$ one may take $c_\rho=\delta$, but a non-unitary twist can push the convergence region to the right, which is why the hypothesis is $\operatorname{Re}(s)>\max(c_\rho,\tfrac12)$ rather than $\operatorname{Re}(s)>\delta$.

**The killing mass formula (26)** — [[Thm - Selberg Zeta Identity (Killing Case)]] and, upstream, [[Thm - Mass of the Subordinate Brownian Loop Measure on Surfaces|Theorem 3.5]]. Note the corollary uses the *formula*, not the zeta identity: both loop masses are evaluated class-by-class, and no sum over classes is inverted.

**$\operatorname{Re}(s)>\tfrac12$**, needed so that the principal square root gives $\tfrac12+\sqrt{\tfrac14+s(s-1)}=s$ rather than $1-s$. This is a branch condition, not a convergence condition, and it is the reason $\tfrac12$ appears in the hypothesis alongside $c_\rho$.

**$\kappa_+(s)=s(s+1)$ is a legitimate killing rate**, being positive for $\operatorname{Re}(s)>0$; $\kappa_-(s)=s(s-1)$ is $\geq-\tfrac14$ for real $s$, consistent with Remark 3.7's extended range. Both masses are therefore covered by the formula.

---

# What consumes this

Nothing downstream. The corollary is a terminal result of §4.1.2, and its role is diagnostic: it delimits the family of zeta functions the loop measure reaches, and shows that the Selberg one is reached *directly* while everything else is reached through signed combinations.

It does, however, prefigure §6.2. Both are instances of [[§3.2 Euclidean Quantum Mechanics and the Path Integral|Remark 3.3]]'s twisting: here by a general finite-dimensional $\rho$ of $\Gamma$, there by a one-dimensional unitary character of $H_1(X,\mathbb{Z})$. The §6.2 case works cleanly precisely because it twists the *Selberg* product rather than the Ruelle one, so no difference is needed and the result remains a genuine mass — see [[Def - Selberg L-Function]] and [[Thm - Selberg L-Function Identity|Corollary 6.4]].

---

# Reading it against the rest of the paper

Read alongside [[Thm - Selberg Zeta Criterion|Lemma 4.2]], this corollary marks the boundary of the criterion. Lemma 4.2 says: a mass of the shape $\frac{C}{m}\frac{e^{(1-s)L}}{e^L-1}$ gives a Selberg identity. Corollary 4.6 says: to reach a shape *without* the $1/(e^L-1)$ factor, one must subtract. And §7 shows a third possibility — a mass of a shape, $\frac1m|e^{mL_\gamma}-1|^{-2}$, that neither the criterion nor a difference reaches, leaving the right zeta function for a hyperbolic 3-manifold open.

The paper's own framing: the loop-measure link "yields, in principle, an identity for any zeta function built from the length spectrum. The Selberg zeta identity is the most natural of these." Corollary 4.6 is the evidence for the second sentence.
