---
type: exercise
subject: advanced-probability
difficulty: "⭐⭐"
prereqs:
  - "Def - Independence"
tags: [probability, advanced-probability]
---

# Problem Statement

**(a) (Bernstein's example.)** Let $X,Y$ be independent fair coin tosses (values in $\{0,1\}$, each outcome probability $\tfrac12$) and $Z=|X-Y|$ (equivalently $X\oplus Y$). Show that the three variables $X,Y,Z$ are **pairwise** independent but **not mutually** independent.

**(b)** Conclude that the [[Def - Independence|definition of independence]] genuinely requires the product rule for *every* finite sub-collection, not just for pairs.

**(c)** Show that mutual independence of $X,Y,Z$ *would* follow if one only had to check pairs — and identify exactly which product equation fails.

**Recall:**

![[Def - Independence#The Definition]]

---

# Convergent Strategy

**Problem class:** a counterexample separating two definitions — pairwise vs. mutual independence.

**Assumption pattern:** $Z=X\oplus Y$ is determined by $X,Y$ together but is independent of each *alone* (XOR with an independent fair bit looks fair). The triple fails the product rule because $Z$ is a *function* of the pair.

**Theorem routing:** compute the pairwise products (all factor) and the triple product (does not).

---

# Legal Operations Used

1. **Direct computation** of joint probabilities.
2. **Exhibit the failing product equation.**

---

# Hints

> [!note]- Hint 1
> Each of $X,Y,Z$ is a fair bit: $\mathbb{P}(X=1)=\mathbb{P}(Y=1)=\mathbb{P}(Z=1)=\tfrac12$.

> [!note]- Hint 2
> Pairwise: e.g. $\mathbb{P}(X=1,Z=1)=\mathbb{P}(X=1,Y=0)=\tfrac14=\mathbb{P}(X=1)\mathbb{P}(Z=1)$.

> [!note]- Hint 3
> Triple: $\mathbb{P}(X=1,Y=1,Z=1)$ — but $Z=|X-Y|=0$ when $X=Y=1$.

---

# Solution

**Step 1 — (a) Marginals and pairs.** The four outcomes $(X,Y)\in\{0,1\}^2$ each have probability $\tfrac14$. Then $Z=|X-Y|$: $Z=0$ on $(0,0),(1,1)$, $Z=1$ on $(0,1),(1,0)$ — so $\mathbb{P}(Z=1)=\tfrac12$, and likewise $\mathbb{P}(X=1)=\mathbb{P}(Y=1)=\tfrac12$. Each is a fair bit.

> [!note]- Derivation
> *Pair $(X,Y)$:* independent by hypothesis.
> *Pair $(X,Z)$:* $\mathbb{P}(X=1,Z=1)=\mathbb{P}(X=1,Y=0)=\tfrac14=\tfrac12\cdot\tfrac12=\mathbb{P}(X=1)\mathbb{P}(Z=1)$; the other three value-combinations check identically. So $X,Z$ independent.
> *Pair $(Y,Z)$:* by symmetry, independent.
> All three pairs are independent — $X,Y,Z$ are **pairwise independent**.

**Step 2 — (a) The triple fails.** Mutual independence would require $\mathbb{P}(X=1,Y=1,Z=1)=\mathbb{P}(X=1)\mathbb{P}(Y=1)\mathbb{P}(Z=1)=\tfrac18$. But $Z=|X-Y|$, so $X=1,Y=1$ forces $Z=0$:
$$\mathbb{P}(X=1,Y=1,Z=1)=\mathbb{P}(\emptyset)=0\neq\tfrac18.$$
The triple product rule fails — $X,Y,Z$ are **not mutually independent**.

**Step 3 — (b),(c).** The example shows pairwise independence is *strictly weaker* than mutual: every pair factors, yet the triple does not. So the [[Def - Independence|definition]] must demand the product rule for *all* finite sub-collections — checking pairs is provably insufficient. The failing equation is precisely the *triple* one, $\mathbb{P}(X{=}1,Y{=}1,Z{=}1)\neq\prod$, and the structural reason is that $Z$ is a *deterministic function of the pair $(X,Y)$* — any third variable functionally tied to the first two can be pairwise-independent of each yet mutually dependent.

> [!note]- Complete formal solution
> (a) Each of $X,Y,Z$ is fair; $\mathbb{P}(X{=}i,Z{=}k)=\tfrac14$ for each $(i,k)$ (and symmetrically for $(Y,Z)$, while $(X,Y)$ is independent by hypothesis) — pairwise independent. But $\mathbb{P}(X{=}1,Y{=}1,Z{=}1)=0\neq\tfrac18$ since $X{=}Y{=}1\Rightarrow Z{=}0$ — not mutually independent. (b) Hence the definition must quantify over all finite sub-collections. (c) The triple equation is the one that fails, because $Z=|X-Y|$ is a function of $(X,Y)$. $\blacksquare$

---

# Key Takeaways

**Pairwise independence is strictly weaker than mutual independence — Bernstein's XOR example is the canonical witness, and the definition of [[Def - Independence|independence]] demands the product rule for *every* finite sub-collection precisely because checking pairs is not enough.** The structural mechanism: a third variable that is a *function of the first two* (here $Z=X\oplus Y$) can be independent of each parent alone — XOR with an independent fair bit is itself fair and uncorrelated with the bit — yet is mutually dependent, since knowing both parents pins it down. Whenever a family includes a variable functionally determined by others, suspect mutual dependence even if all pairs check.

**The practical consequence: theorems that need mutual independence cannot be fed pairwise independence.** Some results survive on pairwise independence alone (the [[Ex - Markov's inequality|Chebyshev]]-based weak law, since variance only needs uncorrelatedness; the second [[Thm - Borel-Cantelli Lemmas|Borel–Cantelli lemma]] in a strengthened form) — but the [[Thm - Kolmogorov 0-1 Law|0–1 law]], the [[Thm - Central Limit Theorem|CLT]], and product-measure arguments genuinely require the full mutual product rule. Knowing which theorems need which is part of using independence correctly.
