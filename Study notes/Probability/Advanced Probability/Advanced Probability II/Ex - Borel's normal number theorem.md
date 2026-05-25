---
type: exercise
subject: advanced-probability
difficulty: "⭐⭐"
prereqs:
  - "Thm - Strong Law of Large Numbers"
  - "Def - Lebesgue Measure"
tags: [probability, advanced-probability]
---

# Problem Statement

Call $x\in[0,1]$ **normal in base $2$** if the digit $1$ has asymptotic frequency $\tfrac12$ in its binary expansion: $\frac1n\#\{k\le n:d_k(x)=1\}\to\tfrac12$, where $x=\sum_k d_k(x)2^{-k}$.

**(a)** Realise the binary digits $d_k$ as i.i.d. random variables on $([0,1],\lambda)$.

**(b)** Prove **Borel's normal number theorem**: Lebesgue-almost-every $x\in[0,1]$ is normal in base $2$.

**(c)** Note that this gives a probabilistic proof of a purely deterministic, number-theoretic fact.

**Recall:**

[[Thm - Strong Law of Large Numbers|SLLN]]: for i.i.d. $X_k$, $\frac1n\sum_{k\le n}X_k\to\mathbb{E}[X_1]$ a.s.

---

# Convergent Strategy

**Problem class:** proving an "almost every real number" statement by reading it as an "almost sure" statement on the [[Def - Lebesgue Measure|uniform probability space]].

**Assumption pattern:** on $([0,1],\lambda)$ — a probability space — the binary digits $d_k$ are i.i.d. fair bits. "Frequency of $1$s $\to\tfrac12$" is the [[Thm - Strong Law of Large Numbers|SLLN]] for these bits; "a.s." translates to "Lebesgue-a.e."

---

# Legal Operations Used

1. **Read $[0,1]$ with $\lambda$ as a probability space.**
2. **Identify the digits as i.i.d. fair bits.**
3. **SLLN**; translate "a.s." to "a.e."

---

# Hints

> [!note]- Hint 1
> On $([0,1],\lambda)$, $d_k(x)$ is the $k$-th binary digit. $\{d_k=1\}$ is a union of dyadic intervals of total length $\tfrac12$, so $\mathbb{P}(d_k=1)=\tfrac12$; and the $d_k$ are independent.

> [!note]- Hint 2
> Frequency of $1$s $=\frac1n\sum_{k\le n}d_k$. Apply the SLLN.

---

# Solution

**Step 1 — (a).** Take the probability space $([0,1],\mathcal{B}([0,1]),\lambda)$ — total mass $1$, so genuinely a [[Def - Probability Space|probability space]]. For $x\in[0,1]$ let $d_k(x)\in\{0,1\}$ be the $k$-th binary digit, $x=\sum_k d_k(x)2^{-k}$.

> [!note]- Derivation
> $\{d_k=1\}=\{x:k\text{-th digit is }1\}$ is a union of $2^{k-1}$ dyadic intervals each of length $2^{-k}$, total length $\tfrac12$ — so $\mathbb{P}(d_k=1)=\lambda(\{d_k=1\})=\tfrac12$, i.e. $d_k$ is a fair bit. Moreover the digits are *independent*: $\mathbb{P}(d_1=\varepsilon_1,\dots,d_n=\varepsilon_n)$ is the length of a single dyadic interval, $2^{-n}=\prod_k\mathbb{P}(d_k=\varepsilon_k)$. So $(d_k)_{k\ge1}$ is an i.i.d. sequence of fair bits — the digits of a uniform real are independent fair coin tosses.

**Step 2 — (b).** Each $d_k$ has $\mathbb{E}[d_k]=\tfrac12$. By the [[Thm - Strong Law of Large Numbers|strong law of large numbers]] for the i.i.d. sequence $(d_k)$,
$$\frac1n\sum_{k=1}^n d_k(x)\ \xrightarrow{\text{a.s.}}\ \mathbb{E}[d_1]=\tfrac12.$$
"Almost surely" here means "for $\lambda$-almost every $x\in[0,1]$." The left side is exactly the asymptotic frequency of the digit $1$ in $x$'s binary expansion. Hence for Lebesgue-almost-every $x$, that frequency is $\tfrac12$ — almost every real number is normal in base $2$.

**Step 3 — (c).** "Normal in base $2$" is a *deterministic, number-theoretic* property of a single real number — no probability in its statement. Yet the cleanest proof routes through probability: equip $[0,1]$ with $\lambda$, recognise the digits as i.i.d. fair bits, invoke the SLLN, and read "almost sure" as "almost every." (The same argument in base $b$, with $d_k$ uniform on $\{0,\dots,b-1\}$, shows a.e. $x$ is normal in every base — *absolutely normal*. Exhibiting one *explicit* normal number is by contrast notoriously hard — e.g. it is unknown whether $\pi$ is normal.)

> [!note]- Complete formal solution
> (a) On $([0,1],\lambda)$ the binary digits $d_k$ satisfy $\mathbb{P}(d_k=1)=\tfrac12$ and are independent ($\mathbb{P}(d_1=\varepsilon_1,\dots,d_n=\varepsilon_n)=2^{-n}$). (b) SLLN: $\frac1n\sum_{k\le n}d_k\to\tfrac12$ a.s., i.e. for $\lambda$-a.e. $x$ — a.e. real is base-$2$ normal. (c) A deterministic fact proved via the probabilistic SLLN. $\blacksquare$

---

# Key Takeaways

**A statement about "almost every real number" is a statement about "almost surely" on the [[Def - Lebesgue Measure|uniform probability space]] $([0,1],\lambda)$ — and the SLLN converts digit-frequency questions into one-line theorems.** The binary digits of a uniform real are i.i.d. fair coin tosses; once that is seen, Borel's normal number theorem *is* the strong law. The translation "Lebesgue measure on $[0,1]$ is a probability measure, $\lambda$-a.e. $=$ almost surely" is the bridge — and it works for any digit-statistical property (frequencies of blocks, of patterns) reducible to a law of large numbers.

**Probability proves theorems with no probability in their statement — a recurring and powerful pattern.** Normal numbers, the [[Ex - The strong law via fourth moments|Weierstrass approximation theorem]] (via Bernstein polynomials), and existence results in combinatorics and analysis are all established by *putting a probability measure on the relevant objects and showing the desired property holds almost surely*. The "probabilistic method" trades an explicit construction for an existence-with-probability-one argument — often far easier, as here: almost every number is normal, yet pinning down a single explicit one is hard.
