---
type: exercise
subject: measure-theory
difficulty: "⭐"
prereqs:
  - "Def - Measure and Measure Space"
  - "Thm - Properties of Measures"
tags: [analysis, measure-theory]
---

# Problem Statement

Let $(X,\mathcal{A},\mu)$ be a measure space and $A_1\supseteq A_2\supseteq\cdots$ a decreasing sequence in $\mathcal{A}$ with $A_k\downarrow A=\bigcap_k A_k$.

**(a)** Prove that if $\mu(A_1)<\infty$ then $\mu(A_k)\to\mu(A)$.

**(b)** Exhibit a measure space and a decreasing sequence $A_k\downarrow\emptyset$ for which $\mu(A_k)\not\to\mu(\emptyset)=0$. Conclude that the hypothesis $\mu(A_1)<\infty$ in (a) cannot be dropped.

**(c)** Show, more precisely, that it suffices to assume $\mu(A_{k_0})<\infty$ for *some* $k_0$, not necessarily $k_0=1$.

**Recall:**

![[Def - Measure and Measure Space#The Definition]]

[[Thm - Properties of Measures|Continuity from below]]: if $B_k\uparrow B$ then $\mu(B_k)\uparrow\mu(B)$ — this holds with *no* finiteness hypothesis.

---

# Convergent Strategy

**Problem class:** establishing a continuity property of a measure, and locating exactly where a hypothesis is indispensable.

**Assumption pattern:** a *decreasing* sequence. Measures are natively continuous from *below* (increasing); to handle a decreasing sequence one *complements inside a fixed finite-measure set* to convert it to an increasing one. The conversion needs a finite "frame" to complement inside, because the final step is a *subtraction*, and $\infty-\infty$ is undefined.

**Theorem routing:** reduce (a) to [[Thm - Properties of Measures|continuity from below]] applied to $A_1\setminus A_k\uparrow A_1\setminus A$.

**Key decision point:** seeing that the *only* use of finiteness is to license the cancellation $\mu(A_1)-\mu(A_k)$; this is what (b) must break and (c) must exploit.

---

# Legal Operations Used

1. **Complementation inside a frame** — turn a decreasing sequence into an increasing one by $B_k=A_1\setminus A_k$.
2. **Apply continuity from below** to the increasing sequence.
3. **Subtraction of finite measures** — legitimate only when the subtrahend is finite.
4. **Counterexample by escape to infinity** — mass that never leaves a finite stage.

---

# Hints

> [!note]- Hint 1
> Measures like *increasing* sequences. Turn the decreasing $A_k$ into an increasing sequence by complementing inside $A_1$: consider $B_k=A_1\setminus A_k$.

> [!note]- Hint 2
> After applying continuity from below to $B_k\uparrow A_1\setminus A$, you will want to write $\mu(A_1\setminus A_k)=\mu(A_1)-\mu(A_k)$. When is this valid?

> [!note]- Hint 3
> For (b): on $(\mathbb{N},2^{\mathbb{N}},\#)$ with counting measure, what is $A_k=\{k,k+1,k+2,\dots\}$? Its measure, and the measure of $\bigcap_k A_k$?

---

# Solution

**Step 1 — Reduce to continuity from below.** Set $B_k=A_1\setminus A_k$. Since $A_k$ decreases, $B_k$ increases, and $\bigcup_k B_k=A_1\setminus\bigcap_k A_k=A_1\setminus A$. By continuity from below, $\mu(B_k)\uparrow\mu(A_1\setminus A)$.

> [!note]- Derivation
> $A_k\supseteq A_{k+1}\Rightarrow A_1\setminus A_k\subseteq A_1\setminus A_{k+1}$, so $(B_k)$ increases. By De Morgan inside $A_1$, $\bigcup_k(A_1\setminus A_k)=A_1\setminus\bigcap_k A_k=A_1\setminus A$. [[Thm - Properties of Measures|Continuity from below]] (no finiteness needed) gives $\mu(B_k)\to\mu(A_1\setminus A)$.

**Step 2 — Convert to a statement about $\mu(A_k)$, using finiteness.** Because $A\subseteq A_k\subseteq A_1$ and $\mu(A_1)<\infty$, finite additivity gives $\mu(A_1\setminus A_k)=\mu(A_1)-\mu(A_k)$ and $\mu(A_1\setminus A)=\mu(A_1)-\mu(A)$. Substituting into Step 1:
$$\mu(A_1)-\mu(A_k)\ \longrightarrow\ \mu(A_1)-\mu(A).$$
Cancel the *finite* quantity $\mu(A_1)$ to obtain $\mu(A_k)\to\mu(A)$.

> [!note]- Derivation
> $A_k=A\sqcup\cdots$? No — rather $A_1=A_k\sqcup(A_1\setminus A_k)$, a disjoint union, so by finite additivity $\mu(A_1)=\mu(A_k)+\mu(A_1\setminus A_k)$; since $\mu(A_1)<\infty$ every term is finite and $\mu(A_1\setminus A_k)=\mu(A_1)-\mu(A_k)$. Likewise $\mu(A_1\setminus A)=\mu(A_1)-\mu(A)$. The limit from Step 1 reads $\mu(A_1)-\mu(A_k)\to\mu(A_1)-\mu(A)$; subtracting the finite constant $\mu(A_1)$ from both sides and negating gives the claim. The subtraction is the *sole* place finiteness is used.

**Step 3 — (b) Counterexample.** On $(\mathbb{N},2^{\mathbb{N}},\#)$ with $\#$ the counting measure, set $A_k=\{k,k+1,k+2,\dots\}$. Then $A_k\downarrow\emptyset$, yet $\mu(A_k)=\infty$ for every $k$, while $\mu(\emptyset)=0$. So $\mu(A_k)=\infty\not\to 0$.

> [!note]- Derivation
> Each $A_k$ is infinite, so $\#(A_k)=\infty$. The sequence decreases and $\bigcap_k A_k=\emptyset$ (no natural number exceeds all $k$). Continuity from above would demand $\infty\to 0$, which fails. Here $\mu(A_1)=\infty$, so the hypothesis of (a) is violated — and the conclusion fails — showing finiteness is indispensable. The mechanism is *escape to infinity*: the "mass" of $A_k$ never leaves any finite stage; it just slides rightward forever.

**Step 4 — (c) Finiteness at any single stage suffices.** Suppose $\mu(A_{k_0})<\infty$. The tail $(A_k)_{k\ge k_0}$ is a decreasing sequence with finite-measure first term $A_{k_0}$, decreasing to the same limit $A$ (dropping finitely many terms changes neither the intersection nor the limit of $\mu(A_k)$). Apply (a) to this tail.

> [!note]- Complete formal solution
> (a) With $B_k=A_1\setminus A_k\uparrow A_1\setminus A$, continuity from below gives $\mu(B_k)\to\mu(A_1\setminus A)$. Since $\mu(A_1)<\infty$, $\mu(A_1\setminus A_k)=\mu(A_1)-\mu(A_k)$ and $\mu(A_1\setminus A)=\mu(A_1)-\mu(A)$; cancelling the finite $\mu(A_1)$ yields $\mu(A_k)\to\mu(A)$. (b) Counting measure on $\mathbb{N}$, $A_k=\{k,k+1,\dots\}\downarrow\emptyset$, $\mu(A_k)\equiv\infty\not\to 0$. (c) If $\mu(A_{k_0})<\infty$, apply (a) to the decreasing sequence $(A_k)_{k\ge k_0}$, whose first term has finite measure and whose intersection is still $A$; a finite truncation does not affect $\lim_k\mu(A_k)$. $\blacksquare$

---

# Key Takeaways

**A measure is natively continuous from below, not from above; the decreasing case is *derived* by complementing inside a finite frame.** The trigger pattern: whenever you face a *decreasing* sequence of sets and want to pass $\mu$ through the limit, immediately rewrite it as an *increasing* sequence by complementing inside a fixed set, apply the free (hypothesis-light) continuity from below, then translate back by subtraction. The subtraction is the catch: it is legal only when the frame has finite measure. So "continuity from above" should be remembered as "continuity from below, plus a subtraction, plus the finiteness needed to subtract."

**"Escape to infinity" is *the* mechanism by which a limit and a measure fail to commute.** In the counterexample the sets $A_k$ never shrink — their mass simply translates rightward forever, present at every finite stage but absent from the intersection. This same mechanism — mass that moves out rather than dissipating — is exactly what breaks naive limit-swapping for *integrals*: it is why the [[Thm - Dominated Convergence Theorem|dominated convergence theorem]] needs a dominating function (to pin the mass down) and why [[Thm - Fatou's Lemma|Fatou's lemma]] is only an inequality. Recognising "could mass escape to infinity here?" is the single most useful diagnostic when a convergence theorem seems to fail.
