---
type: exercise
subject: advanced-probability
difficulty: "⭐⭐"
prereqs:
  - "Def - Modes of Convergence"
tags: [probability, advanced-probability]
---

# Problem Statement

Establish the [[Def - Modes of Convergence|implication hierarchy]] and its sharpness.

**(a)** Prove a.s. $\Rightarrow$ in probability, and $L^p\Rightarrow$ in probability, and in probability $\Rightarrow$ in distribution.

**(b)** Give counterexamples showing none of the converses holds, and that a.s. and $L^p$ are *incomparable*.

**Recall:**

![[Def - Modes of Convergence#The Definition]]

---

# Convergent Strategy

**Problem class:** mapping the relationships between four notions of convergence — proving the true implications and refuting the false ones.

**Assumption pattern:** each implication is a short measure-theoretic fact ([[Thm - Dominated Convergence Theorem|DCT]] or [[Ex - Markov's inequality|Markov]]); each refutation is a *named counterexample* — escaping mass, the typewriter, or i.i.d. non-degeneracy.

---

# Legal Operations Used

1. **DCT / Markov** for the forward implications.
2. **Escape-of-mass, typewriter, i.i.d.** counterexamples.

---

# Hints

> [!note]- Hint 1
> a.s. $\Rightarrow$ in probability: $\mathbf{1}_{\{|X_n-X|>\varepsilon\}}\to0$ a.s., bounded; apply [[Thm - Dominated Convergence Theorem|bounded convergence]].

> [!note]- Hint 2
> $L^p\Rightarrow$ probability: [[Ex - Markov's inequality|Markov]] on $|X_n-X|^p$.

> [!note]- Hint 3
> Counterexamples: $n\mathbf{1}_{[0,1/n]}$ (a.s. not $L^1$); the [[Ex - The typewriter sequence|typewriter]] ($L^p$ not a.s.); i.i.d. non-degenerate (distribution not probability).

---

# Solution

**Step 1 — (a) Forward implications.**

> [!note]- Derivation
> *a.s. $\Rightarrow$ probability.* If $X_n\to X$ a.s., then $\mathbf{1}_{\{|X_n-X|>\varepsilon\}}\to0$ a.s.; it is bounded by $1\in L^1(\mathbb{P})$, so by [[Thm - Dominated Convergence Theorem|bounded convergence]] $\mathbb{P}(|X_n-X|>\varepsilon)=\mathbb{E}[\mathbf{1}_{\{\cdots\}}]\to0$.
> *$L^p\Rightarrow$ probability.* By [[Ex - Markov's inequality|Markov]] applied to $|X_n-X|^p$, $\mathbb{P}(|X_n-X|>\varepsilon)\le\varepsilon^{-p}\mathbb{E}|X_n-X|^p\to0$.
> *probability $\Rightarrow$ distribution.* For bounded uniformly continuous $f$: split $|\mathbb{E}f(X_n)-\mathbb{E}f(X)|$ over $\{|X_n-X|\le\delta\}$ (where $|f(X_n)-f(X)|$ is small by uniform continuity) and its complement (probability $\to0$, $f$ bounded). Both terms $\to0$.

**Step 2 — (b) Sharpness.**

> [!note]- Derivation
> *a.s. $\not\Rightarrow L^1$:* $X_n=n\mathbf{1}_{[0,1/n]}$ on $([0,1],\lambda)$ — $X_n\to0$ a.s. (off $\{0\}$) but $\mathbb{E}X_n=1\not\to0$. Mass escapes into a spike.
> *$L^p\not\Rightarrow$ a.s.:* the [[Ex - The typewriter sequence|typewriter sequence]] $\mathbf{1}_{I_{m,k}}\to0$ in every $L^p$ and in probability, but converges a.s. nowhere.
> *probability $\not\Rightarrow L^p$:* same spike $n\mathbf{1}_{[0,1/n]}$ — $\to0$ in probability, $\not\to0$ in $L^1$.
> *probability $\not\Rightarrow$ a.s.:* the typewriter again.
> *distribution $\not\Rightarrow$ probability:* i.i.d. non-degenerate $X_n$ all have one law, so $X_n\xrightarrow{d}X_1$, but $\mathbb{P}(|X_n-X_1|>\varepsilon)$ is a positive constant.
> So a.s. and $L^p$ each fail to imply the other (spike: a.s. not $L^1$; typewriter: $L^p$ not a.s.) — *incomparable*.

> [!note]- Complete formal solution
> (a) Bounded convergence gives a.s.$\Rightarrow$probability; Markov gives $L^p\Rightarrow$probability; a uniform-continuity split gives probability$\Rightarrow$distribution. (b) $n\mathbf{1}_{[0,1/n]}$ converges a.s. and in probability but not in $L^1$; the typewriter converges in $L^p$ and probability but not a.s.; i.i.d. non-degenerate variables converge in distribution but not in probability. Hence no converse holds and a.s., $L^p$ are incomparable. $\blacksquare$

---

# Key Takeaways

**The four modes form a strict hierarchy — a.s. $\Rightarrow$ probability $\Rightarrow$ distribution, and $L^p\Rightarrow$ probability — with a.s. and $L^p$ mutually incomparable, and *no* converse valid.** Each forward arrow is a one-line measure-theoretic fact (bounded convergence, Markov); each missing arrow has a canonical witness. Knowing this map — and *which mode a theorem delivers versus needs* — is the organising discipline of limit theory: the [[Thm - Strong Law of Large Numbers|SLLN]] delivers a.s., the [[Thm - Weak Law of Large Numbers|WLLN]] only probability, the [[Thm - Central Limit Theorem|CLT]] only distribution.

**The counterexamples are a small, reusable bank: the escaping spike $n\mathbf{1}_{[0,1/n]}$ and the [[Ex - The typewriter sequence|typewriter sequence]].** The spike separates a.s./probability from $L^1$ (mass escapes); the typewriter separates $L^p$/probability from a.s. (the bad set sweeps). To *close* a gap one needs a bridge — [[Def - Uniform Integrability|uniform integrability]] upgrades probability to $L^1$, a subsequence upgrades probability to a.s., a constant limit upgrades distribution to probability — and recognising which bridge a problem needs is the practical skill.
