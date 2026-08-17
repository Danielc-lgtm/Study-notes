---
type: construction
paper: "BH26"
subject: brownian-loops
prereqs:
  - "Constr - The Subordinate Brownian Loop Measure"
  - "Def - The Space of Unrooted Unparametrised Loops"
tags: [paper, probability, loop-measures]
---

# Signature

| symbol | type |
|---|---|
| $\mathcal{L}$ | the measurable space of unrooted unparametrised loops on $X$ (càdlàg loops when $\phi$ has jumps) |
| $\mu^\phi_X$ | a $\sigma$-finite measure on $\mathcal{L}$ — [[Constr - The Subordinate Brownian Loop Measure\|the subordinate loop measure]] |
| $c$ | $\in(0,\infty)$ — the **intensity** of the soup |
| $\mathcal{L}_c$ | a Poisson point process on $\mathcal{L}$ with intensity $c\,\mu^\phi_X$; a random countable multiset of loops |
| $N_A$ | $:=\#\{\eta\in\mathcal{L}_c:\eta\in A\}$ for $A\subseteq\mathcal{L}$ measurable; $\mathbb{Z}_{\geq0}\cup\{\infty\}$-valued |
| $\lambda$ | alternative name for $c$, used in §6.3 |

---

# Construction

> **Definition 3.7 (subordinate Brownian loop soup).** Fix $\phi$ Bernstein satisfying [[Constr - Assumption 2.3 (Strictly Increasing Subordinator)|Assumption 2.3]] and $c>0$. Let
> $$\mathcal{L}_c:=\text{Poisson point process on }\mathcal{L}\text{ with intensity measure }c\,\mu^\phi_X.$$

> **(P1) Well-posedness.** A Poisson point process exists for **any** $\sigma$-finite intensity. $\sigma$-finiteness of $\mu^\phi_X$ is the only hypothesis needed, and it is [[Constr - The Subordinate Brownian Loop Measure|(P2)]] there. *Consumer:* everything below.
>
> **(P2) Counts.** $\mu^\phi_X(A)<\infty\;\Rightarrow\;N_A\sim\mathrm{Poisson}\big(c\,\mu^\phi_X(A)\big)$. *Consumer:* [[Thm - Poissonian Structure of Homotopy Classes]].
>
> **(P3) Independence.** $A_1,\dots,A_k$ pairwise disjoint $\Rightarrow$ $N_{A_1},\dots,N_{A_k}$ independent. *Consumer:* Proposition 3.8, and the product form in §6.3.
>
> **(P4) Marked version for jump processes.** If $\phi$ has jumps then $\mathcal{C}_X(\gamma^m)$ is **not** a measurable subset of $\mathcal{L}$ (Remark 3.1). Replace $\mathcal{L}_c$ by the Poisson point process of **marked** loops carrying the pair $(B,S)$ — Brownian path plus subordinator — on which the monodromy class is measurable, with the same intensity $c\,\mu^\phi_X(\mathcal{C}_X(\gamma^m))$. *Consumer:* [[Thm - Poissonian Structure of Homotopy Classes]] for jump $\phi$.

> [!warning] The soup is not a measure on loops, and the mass is not a probability
> $\mu^\phi_X$ is $\sigma$-finite and **infinite**: $\mu^\phi_X(\mathcal{L})=\infty$, so $\mathcal{L}_c$ has infinitely many loops almost surely, and most of them are tiny. What is finite is $\mu^\phi_X$ on a *fixed non-trivial class*. Normalising to a probability measure is a separate construction, and requires the total over non-trivial classes to be finite — see [[Thm - Finiteness of the Total Mass|Cor 4.7]] and [[Constr - The Probability Measure on Free Homotopy Classes]].

---

# Type card

> [!abstract] Type card — the loop soup
> **Given.** **(H1)** $\phi$ Bernstein with Assumption 2.3. **(H2)** $c>0$. **(H3)** $\mu^\phi_X$ $\sigma$-finite on $\mathcal{L}$.
>
> **Produces.** A random countable multiset $\mathcal{L}_c\subseteq\mathcal{L}$, i.e. a point process, with $\mathbb{E}[N_A]=c\,\mu^\phi_X(A)$ for every measurable $A$.
>
> **Lets you.** Promote **every mass computed in §3–§4 to a distribution**: a number $\mu^\phi_X(A)$ becomes the mean of an explicit Poisson variable. This is what makes §6 statements about *random* topology rather than about expectations.

---

# Depends on

- [[Constr - The Subordinate Brownian Loop Measure]] — the intensity, and its $\sigma$-finiteness
- [[Def - The Space of Unrooted Unparametrised Loops]] — the state space, and its $\sigma$-algebra
- [[Ext - Lawler–Werner Restriction and Conformal Invariance]] — the soup construction follows Lawler–Werner; see also Le Jan
- 🟢 Poisson point processes, existence for $\sigma$-finite intensity — *Advanced Probability* (7,9)

---

# Consumed by

- [[Thm - Poissonian Structure of Homotopy Classes]] — (P2),(P3),(P4)
- [[Ext - Exponential Formula for Poisson Point Processes]] — its precondition is exactly (H1)–(H3)
- [[Thm - Distribution of the Total Homology of the Loop Soup]] — $\mathcal{L}^*_\lambda$, the non-contractible non-peripheral part
- [[§3.3 The Loop Soup and its Poissonian Structure]]
- [[§6 Probability Measures on Homotopy and Homology Classes]] §6.3

---

# Commentary

> [!note]- Commentary (skippable)
> The step is cheap and the payoff is large. Nothing about $\mu^\phi_X$ changes; the soup is a bookkeeping device that turns the sentence "the mass of class $\mathcal{C}$ is $\frac1m\frac{e^{(1-s)L}}{e^L-1}$" into "the number of loops in $\mathcal{C}$ is Poisson with that mean, independently across classes". Independence across classes is free — distinct free homotopy classes are disjoint sets of loops — and it is exactly what §6.3 needs to factor a character expectation into a product over $(\gamma,m)$, which is where the Selberg $L$-function comes from.
>
> The parameter $c$ (called $\lambda$ in §6.3) is a genuine parameter of the model, not a normalisation: it scales every mass linearly, hence scales $-\log Z_X$ linearly, hence appears as the exponent $Z_X^{-\lambda}$ in the §6.3 identities.
>
> (P4) is the one technical wrinkle. For jump processes a càdlàg loop does not have a well-defined homotopy class — the jumps can cross anything — so the class is only measurable after remembering *which* Brownian path the jumps were sampled from. Carrying the pair $(B,S)$ solves it, and the intensity is unchanged, so the wrinkle costs nothing beyond a sentence.
