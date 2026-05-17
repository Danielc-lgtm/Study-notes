---
type: theorem
subject: measure-theory
prereqs:
  - "Def - Measure and Measure Space"
  - "Def - Algebra and σ-Algebra"
tags: [analysis, measure-theory]
---

# Notation

$(X, \mathcal{A}, \mu)$ is a [[Def - Measure and Measure Space|measure space]]. For sets we write $A \subseteq B$ for inclusion, $B \setminus A = B \cap A^c$, $\bigsqcup$ for disjoint union. "$A_k \uparrow A$" means $A_1 \subseteq A_2 \subseteq \cdots$ with $\bigcup_k A_k = A$; "$A_k \downarrow A$" means $A_1 \supseteq A_2 \supseteq \cdots$ with $\bigcap_k A_k = A$.

---

# Motivation

The definition of a [[Def - Measure and Measure Space|measure]] asks only for two things: $\mu(\emptyset)=0$ and $\sigma$-additivity over *disjoint* sequences. That is a deliberately spartan list. Everything one actually *uses* about measures — that bigger sets are bigger, that size respects monotone limits, that overlapping unions are subadditive — is not assumed but *derived*. This theorem is the derivation: it extracts, from the two axioms, the full working toolkit.

The two continuity statements are the heart of it. $\sigma$-additivity is a statement about disjoint sets; "continuity from below" rephrases it as a statement about *increasing* sequences, $\mu(\bigcup A_k) = \lim \mu(A_k)$, which is the form needed every time one approximates a complicated set by simpler ones. This is the set-level shadow of the [[Thm - Monotone Convergence Theorem|monotone convergence theorem]] for integrals — indeed it *is* MCT applied to indicator functions. "Continuity from above" is the decreasing analogue, and it comes with a finiteness caveat that is genuinely necessary, not a technicality.

---

# Sources and Targets

**Sources (Input Broadening).** The theorem's hypothesis is just "$\mu$ is a measure." The non-obvious sources are the *forms in which a measure arrives*. (i) Any *outer measure restricted to its [[Thm - Carathéodory's σ-Algebra|Carathéodory σ-algebra]]* is a measure, so all five properties hold there. (ii) Any *$\nu(A) = \int_A f\,d\mu$* with $f \geq 0$ is a measure ($\sigma$-additivity is MCT), so densities inherit continuity. (iii) Any *pushforward* $f_*\mu$, any *restriction* $\mu|_A$, any *countable sum* $\sum_n c_n \mu_n$ of measures is again a measure. Recognising these as measures is what lets one *apply* the theorem; the bridge in each case is checking $\sigma$-additivity, after which monotonicity etc. are free.

**Targets (Output Amplification).** Continuity from below, combined with a *uniform bound* $\mu(A_k) \leq M$, yields $\mu(\bigcup A_k) \leq M$ — used to prove a limiting set is null or finite. $\sigma$-subadditivity, combined with *$\sum_k \mu(A_k) < \infty$*, gives the **first Borel–Cantelli lemma**: $\mu(\limsup A_k) = 0$, since $\limsup A_k \subseteq \bigcup_{k \geq n} A_k$ and the tail sum vanishes. Continuity from above, combined with $\mu(A_1) < \infty$ and $A_k \downarrow \emptyset$, gives $\mu(A_k) \to 0$ — the **continuity property** that, conversely, upgrades a finitely additive set function to a genuine measure (this is the engine of the [[Thm - Hahn-Carathéodory Extension Theorem|extension theorem]]).

---

# Formal Statement

Let $(X,\mathcal{A},\mu)$ be a measure space and $A, B, A_k \in \mathcal{A}$.

1. **(Monotonicity)** $A \subseteq B \implies \mu(A) \leq \mu(B)$.
2. **(Finite additivity)** If $A_1, \dots, A_n$ are pairwise disjoint, $\mu\!\left(\bigsqcup_{k=1}^n A_k\right) = \sum_{k=1}^n \mu(A_k)$.
3. **(Continuity from below)** If $A_k \uparrow A$, then $\mu(A) = \lim_{k\to\infty} \mu(A_k) = \sup_k \mu(A_k)$.
4. **(Continuity from above)** If $A_k \downarrow A$ **and $\mu(A_1) < \infty$**, then $\mu(A) = \lim_{k\to\infty}\mu(A_k) = \inf_k \mu(A_k)$.
5. **($\sigma$-subadditivity)** If $A \subseteq \bigcup_{k=1}^\infty A_k$, then $\mu(A) \leq \sum_{k=1}^\infty \mu(A_k)$.

---

# Why Is It True

Picture filling a region with water. **Monotonicity** is obvious: a sub-region holds no more than the whole, because the whole is the sub-region *plus the rest*, and "the rest" has non-negative measure. That is the entire idea — write $B = A \sqcup (B\setminus A)$ and additivity does the work.

**Continuity from below** is the statement that a measure cannot "lose mass in the limit" of a growing sequence. If $A_k$ swells up to $A$, the only mass in $A$ is mass that entered at some finite stage; nothing materialises only "at infinity." Make this precise by chopping $A$ into the disjoint *annuli* $\widetilde A_k = A_k \setminus A_{k-1}$ — the new mass added at step $k$. Then $A = \bigsqcup \widetilde A_k$, and $\sigma$-additivity says the total is the sum of the annuli, while $\mu(A_m) = \sum_{k\le m}\mu(\widetilde A_k)$ is the partial sum. "Sum equals limit of partial sums" *is* continuity from below. So continuity from below is not a new fact — it is $\sigma$-additivity wearing different clothes.

**Continuity from above** is the mirror image, obtained by complementing inside $A_1$: $A_1 \setminus A_k$ increases up to $A_1 \setminus A$, apply continuity from below, then subtract. The subtraction is legal *only* if $\mu(A_1) < \infty$ — you cannot cancel $\infty - \infty$. The finiteness hypothesis is exactly the licence to subtract, and without it the conclusion is false: on $(\mathbb{N}, \text{counting measure})$, $A_k = \{k, k+1, \dots\}$ decreases to $\emptyset$, yet $\mu(A_k) = \infty$ for all $k$ while $\mu(\emptyset) = 0$.

**$\sigma$-subadditivity** handles *overlapping* covers. A measure is additive only over disjoint sets, but a cover need not be disjoint. Disjointify it: replace $A_k$ by $\widetilde A_k = A_k \setminus (A_1 \cup \cdots \cup A_{k-1})$, which is disjoint, has the same union, and satisfies $\widetilde A_k \subseteq A_k$. Then $\mu(A) \leq \mu(\bigsqcup \widetilde A_k) = \sum \mu(\widetilde A_k) \leq \sum \mu(A_k)$ — additivity on the disjointified sets, monotonicity to undo the disjointification.

---

# What Makes This Hard

Nothing here is deep, but two points trip people up. First, the **disjointification trick** ($\widetilde A_k = A_k \setminus \bigcup_{j<k} A_j$) is the single recurring device — it converts every "union" statement into a "disjoint union" statement so that $\sigma$-additivity applies; failing to see that this is the *same* trick in (3) and (5) is the common confusion. Second, the **finiteness hypothesis in (4)** is not decoration: the most common error is to apply continuity from above to a decreasing sequence of infinite-measure sets and conclude something false.

---

# Rederivation Scaffold

**High-level strategy.** Property (2) is $\sigma$-additivity with all but finitely many $A_k$ empty. Everything else routes through (2) or through disjointification + $\sigma$-additivity.

**Subgoal decomposition.**

1. **Finite additivity (2).** Set $A_k = \emptyset$ for $k > n$ in the $\sigma$-additivity axiom; the tail terms vanish since $\mu(\emptyset)=0$.
   - *Why needed:* base case for monotonicity.
2. **Monotonicity (1).** Write $B = A \sqcup (B \setminus A)$, apply (2) with $n=2$, drop the non-negative term $\mu(B\setminus A)$.
   - *Why needed:* used to compare measures of approximants throughout.
3. **Continuity from below (3).** Disjointify: $\widetilde A_k = A_k \setminus A_{k-1}$ (with $A_0 = \emptyset$). Then $A = \bigsqcup \widetilde A_k$; apply $\sigma$-additivity; recognise partial sums as $\mu(A_m)$.
4. **Continuity from above (4).** Apply (3) to $A_1 \setminus A_k \uparrow A_1 \setminus A$. Get $\mu(A_1) - \mu(A) = \lim(\mu(A_1) - \mu(A_k))$; cancel $\mu(A_1) < \infty$.
   - *Hint:* the cancellation is the *only* place finiteness is used.
5. **$\sigma$-subadditivity (5).** Disjointify the cover into $\widetilde A_k \subseteq A_k$ with $\bigsqcup\widetilde A_k \supseteq A$; chain $\sigma$-additivity and monotonicity.

---

# Lemma Decomposition

> [!note]- Lemma 1: Finite additivity and monotonicity
> **Statement:** For pairwise disjoint $A_1,\dots,A_n$, $\mu(\bigsqcup A_k) = \sum\mu(A_k)$; and $A \subseteq B \implies \mu(A)\le\mu(B)$.
>
> **Hint:** Pad the disjoint sequence with empty sets; for monotonicity split $B$ into $A$ and $B\setminus A$.
>
> **Why needed:** Monotonicity is invoked in the proofs of (3), (4), (5).
>
> > [!note]- Full proof
> > In $\sigma$-additivity take $A_k = \emptyset$ for $k > n$; since $\mu(\emptyset)=0$ the infinite series collapses to $\sum_{k=1}^n\mu(A_k)$, giving (2). For (1): $A$ and $B\setminus A = B \cap A^c$ are disjoint measurable sets with union $B$, so by (2) $\mu(B) = \mu(A) + \mu(B\setminus A) \geq \mu(A)$ since $\mu(B\setminus A) \geq 0$.

> [!note]- Lemma 2: Continuity from below
> **Statement:** $A_k \uparrow A \implies \mu(A_k) \to \mu(A)$.
>
> **Hint:** Disjointify into annuli $\widetilde A_k = A_k \setminus A_{k-1}$.
>
> **Why needed:** This is the set-level monotone convergence theorem; (4) reduces to it.
>
> > [!note]- Full proof
> > Set $A_0 = \emptyset$, $\widetilde A_k = A_k \setminus A_{k-1} \in \mathcal{A}$. The $\widetilde A_k$ are pairwise disjoint (if $j<k$ then $\widetilde A_k \cap A_j \subseteq \widetilde A_k \cap A_{k-1} = \emptyset$) and $\bigsqcup_{k=1}^m \widetilde A_k = A_m$, $\bigsqcup_{k=1}^\infty \widetilde A_k = A$. By $\sigma$-additivity $\mu(A) = \sum_{k=1}^\infty \mu(\widetilde A_k) = \lim_{m\to\infty}\sum_{k=1}^m\mu(\widetilde A_k) = \lim_{m\to\infty}\mu(A_m)$, the last step by finite additivity. The limit equals the sup since $\mu(A_k)$ is non-decreasing by monotonicity.

> [!note]- Lemma 3: Continuity from above
> **Statement:** $A_k \downarrow A$ and $\mu(A_1)<\infty \implies \mu(A_k)\to\mu(A)$.
>
> **Hint:** Complement inside $A_1$ and apply Lemma 2.
>
> **Why needed:** The decreasing case; the finiteness hypothesis lives entirely here.
>
> > [!note]- Full proof
> > Put $B_k = A_1 \setminus A_k$. Then $B_k \uparrow A_1 \setminus A$, so by Lemma 2, $\mu(A_1 \setminus A) = \lim_k\mu(A_1\setminus A_k)$. Since $A \subseteq A_k \subseteq A_1$ and $\mu(A_1)<\infty$, every set here has finite measure, so by finite additivity $\mu(A_1\setminus A_k) = \mu(A_1)-\mu(A_k)$ and $\mu(A_1\setminus A) = \mu(A_1)-\mu(A)$. Substituting: $\mu(A_1)-\mu(A) = \lim_k(\mu(A_1)-\mu(A_k))$. Cancel the finite quantity $\mu(A_1)$ to get $\mu(A) = \lim_k\mu(A_k)$.

> [!note]- Lemma 4: σ-subadditivity
> **Statement:** $A \subseteq \bigcup_k A_k \implies \mu(A) \leq \sum_k\mu(A_k)$.
>
> **Hint:** Disjointify the cover, intersect with $A$.
>
> > [!note]- Full proof
> > Set $\widetilde A_k = A \cap A_k \cap A_1^c \cap \cdots \cap A_{k-1}^c$. These are pairwise disjoint, $\widetilde A_k \subseteq A_k$, and $\bigsqcup_k \widetilde A_k = A \cap \bigcup_k A_k = A$. By $\sigma$-additivity and monotonicity, $\mu(A) = \sum_k\mu(\widetilde A_k) \leq \sum_k\mu(A_k)$.

---

# Formal Proof

> [!note]- Complete formal proof
> Combine Lemmas 1–4. (2) and (1) are Lemma 1; (3) is Lemma 2; (4) is Lemma 3; (5) is Lemma 4. Each uses only the two measure axioms ($\mu(\emptyset)=0$, $\sigma$-additivity) plus, where indicated, the previously established item. $\blacksquare$

---

# Cross-Field Exercise Suggestions

Apply continuity from below to *probability*: if $A_k \uparrow A$ are events, $\mathbb{P}(A_k) \to \mathbb{P}(A)$ — used to compute $\mathbb{P}(\text{a sequence eventually does } X)$. Apply $\sigma$-subadditivity to get the **first Borel–Cantelli lemma** in [[Thm - Borel-Cantelli Lemmas|Advanced Probability]]: $\sum\mathbb{P}(A_k)<\infty \Rightarrow \mathbb{P}(\limsup A_k)=0$. Apply continuity from above to *escape-to-infinity* phenomena: the failure of (4) without finiteness is the exact mechanism by which mass "leaks to $\infty$," the same mechanism that breaks naive limit-swapping in [[Thm - Dominated Convergence Theorem|DCT]].

---

# Bridges

- **[[Thm - Monotone Convergence Theorem]]** — continuity from below is precisely MCT specialised to indicator functions $\mathbf{1}_{A_k} \uparrow \mathbf{1}_A$. The set theorem and the function theorem are the same theorem at two levels of generality.
- **[[Thm - Hahn-Carathéodory Extension Theorem]]** — the *continuity property* (the contrapositive of (4): finitely additive set function with $A_k \downarrow\emptyset \Rightarrow \mu(A_k)\to 0$) is exactly the hypothesis that lets a pre-measure extend to a measure.
- **[[Thm - Borel-Cantelli Lemmas]]** — the first lemma is a one-line corollary of $\sigma$-subadditivity.

---

# Unlocked by This

> [!tip] Continuity of probability *(from [[Advanced Probability I — Probability Spaces and Random Variables|Advanced Probability]])*
> For events, continuity from below/above says $\mathbb{P}$ is sequentially continuous along monotone sequences. This is what makes "$\mathbb{P}(X_n \to X)$" and tail events tractable, and underlies the [[Thm - Borel-Cantelli Lemmas|Borel–Cantelli lemmas]].
