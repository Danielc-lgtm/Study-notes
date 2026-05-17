---
type: exercise
subject: advanced-probability
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Strong Law of Large Numbers"
  - "Thm - Borel-Cantelli Lemmas"
  - "Ex - Markov's inequality"
tags: [probability, advanced-probability]
---

# Problem Statement

Let $(X_n)$ be i.i.d. with $\mathbb{E}[X_1]=0$ and **finite fourth moment** $\mathbb{E}[X_1^4]<\infty$; $S_n=X_1+\cdots+X_n$.

**(a)** Show $\mathbb{E}[S_n^4]=O(n^2)$.

**(b)** Deduce $\mathbb{E}\big[(S_n/n)^4\big]=O(n^{-2})$, hence $\sum_n\mathbb{E}[(S_n/n)^4]<\infty$.

**(c)** Conclude, via [[Thm - Borel-Cantelli Lemmas|Borel–Cantelli]] (or MCT), the **strong law** $S_n/n\to0$ almost surely.

**Recall:**

[[Thm - Strong Law of Large Numbers|SLLN]]: $S_n/n\to\mu$ a.s. for i.i.d. $X_n$ with $\mathbb{E}|X_1|<\infty$.

---

# Convergent Strategy

**Problem class:** proving an *almost-sure* limit by an $L^4$ moment bound and summability — the elementary route to the SLLN.

**Assumption pattern:** a *fourth* moment is far more than the SLLN needs ($\mathbb{E}|X_1|<\infty$ suffices), but it makes the proof a short computation: independence and $\mathbb{E}X=0$ kill most terms of $\mathbb{E}[S_n^4]$, leaving an $O(n^2)$ bound, which divided by $n^4$ is summable — and summability forces a.s. convergence.

---

# Legal Operations Used

1. **Expand $S_n^4$**; kill odd/mixed terms by $\mathbb{E}X=0$ and independence.
2. **Sum the bound** and apply MCT (or Borel–Cantelli).

---

# Hints

> [!note]- Hint 1
> $\mathbb{E}[S_n^4]=\sum_{i,j,k,l}\mathbb{E}[X_iX_jX_kX_l]$. With $\mathbb{E}X=0$ and independence, a term survives only if every index is repeated — types $X_i^4$ and $X_i^2X_j^2$.

> [!note]- Hint 2
> Count: $n$ terms of type $X_i^4$, and $\binom{n}{2}\cdot\binom{4}{2}=3n(n-1)$ of type $X_i^2X_j^2$. So $\mathbb{E}[S_n^4]=n\,\mathbb{E}X_1^4+3n(n-1)(\mathbb{E}X_1^2)^2=O(n^2)$.

> [!note]- Hint 3
> $\sum_n\mathbb{E}[(S_n/n)^4]<\infty\Rightarrow\sum_n(S_n/n)^4<\infty$ a.s. (MCT), so the terms $\to0$.

---

# Solution

**Step 1 — (a).** Expand $\mathbb{E}[S_n^4]=\sum_{i,j,k,l=1}^n\mathbb{E}[X_iX_jX_kX_l]$. By independence and $\mathbb{E}[X_m]=0$, a term vanishes unless *every distinct index appears at least twice* (a lone index $m$ factors out an $\mathbb{E}[X_m]=0$). With four index slots this leaves two patterns: all four equal ($X_i^4$), or two pairs ($X_i^2X_j^2$, $i\neq j$).

> [!note]- Derivation
> There are $n$ all-equal terms, each $\mathbb{E}[X_1^4]$. There are $\binom n2$ choices of pair $\{i,j\}$ and $\binom42=6$ ways to assign the slots, but the two pairs are interchangeable... counting slot-assignments: choosing which $2$ of the $4$ slots are index $i$ gives $\binom42=6$; so $6\binom n2=3n(n-1)$ terms of type $X_i^2X_j^2$, each $\mathbb{E}[X_i^2X_j^2]=(\mathbb{E}X_1^2)^2$ by independence. Hence
> $$\mathbb{E}[S_n^4]=n\,\mathbb{E}[X_1^4]+3n(n-1)(\mathbb{E}[X_1^2])^2\ \le\ Cn^2$$
> for a constant $C$ depending on the second and fourth moments. So $\mathbb{E}[S_n^4]=O(n^2)$.

**Step 2 — (b).** $\mathbb{E}[(S_n/n)^4]=n^{-4}\mathbb{E}[S_n^4]\le Cn^{-2}$. Therefore $\sum_{n\ge1}\mathbb{E}[(S_n/n)^4]\le C\sum_n n^{-2}<\infty$.

**Step 3 — (c).** By [[Thm - Monotone Convergence Theorem|MCT]] applied to the non-negative series, $\mathbb{E}\big[\sum_n(S_n/n)^4\big]=\sum_n\mathbb{E}[(S_n/n)^4]<\infty$, so $\sum_n(S_n/n)^4<\infty$ almost surely. A convergent series has terms $\to0$, so $(S_n/n)^4\to0$ a.s., hence $S_n/n\to0$ a.s. — the [[Thm - Strong Law of Large Numbers|strong law]] for mean-zero i.i.d. variables with a fourth moment. (Equivalently: [[Ex - Markov's inequality|Markov]] gives $\mathbb{P}(|S_n/n|>\varepsilon)\le\varepsilon^{-4}Cn^{-2}$, summable, so [[Thm - Borel-Cantelli Lemmas|Borel–Cantelli]] gives $|S_n/n|>\varepsilon$ only finitely often a.s.)

> [!note]- Complete formal solution
> (a) $\mathbb{E}[S_n^4]=n\mathbb{E}X_1^4+3n(n-1)(\mathbb{E}X_1^2)^2=O(n^2)$, mixed/odd terms killed by independence and $\mathbb{E}X=0$. (b) $\mathbb{E}[(S_n/n)^4]\le Cn^{-2}$, so $\sum_n\mathbb{E}[(S_n/n)^4]<\infty$. (c) MCT $\Rightarrow\sum_n(S_n/n)^4<\infty$ a.s. $\Rightarrow S_n/n\to0$ a.s. $\blacksquare$

---

# Key Takeaways

**A moment bound that is *summable after rescaling* yields almost-sure convergence — this is the elementary route to the strong law.** The chain is rigid: bound $\mathbb{E}[(S_n/n)^4]=O(n^{-2})$, observe $\sum n^{-2}<\infty$, conclude via MCT (or [[Thm - Borel-Cantelli Lemmas|Borel–Cantelli]]) that $S_n/n\to0$ a.s. The fourth power, not the second, is used precisely because $\sum n^{-1}$ *diverges* while $\sum n^{-2}$ *converges* — the higher moment buys a faster decay rate, crossing the summability threshold that turns "in probability" into "almost surely."

**This proof trades generality for simplicity: it assumes a finite *fourth* moment, far more than the SLLN's sharp hypothesis $\mathbb{E}|X_1|<\infty$.** The [[Thm - Strong Law of Large Numbers|sharp strong law]] needs the [[Def - Martingale|backward-martingale]] machinery or a delicate truncation; the fourth-moment proof is the "first course" version — honest, short, and revealing the mechanism (averaging kills high moments fast enough to be summable). The general lesson — *summability of error bounds $\Rightarrow$ a.s. convergence* — is the universal bridge from quantitative ($L^p$) estimates to qualitative (a.s.) limits.
