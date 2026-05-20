---
type: theorem
subject: complex-analysis
prereqs:
  - "Thm - Liouville's Theorem"
  - "Def - Holomorphic Function"
tags: [analysis, complex-analysis]
---

# Notation

$p(z) = a_n z^n + \ldots + a_1 z + a_0 \in \mathbb{C}[z]$ a polynomial of degree $n \geq 1$ ($a_n \neq 0$). Full registry on [[Complex Analysis II — Cauchy's Theorem and its Consequences]].

---

# Statement

> **Theorem (fundamental theorem of algebra).** Every non-constant polynomial $p(z) = a_n z^n + \cdots + a_1 z + a_0 \in \mathbb{C}[z]$ with $n \geq 1$ and $a_n \neq 0$ has a root in $\mathbb{C}$: there exists $z_0 \in \mathbb{C}$ with $p(z_0) = 0$.
>
> Equivalently, $\mathbb{C}$ is **algebraically closed**: every degree-$n$ polynomial factors as $p(z) = a_n \prod_{i=1}^n (z - z_i)$ for some $z_1, \dots, z_n \in \mathbb{C}$ (counted with multiplicity).

---

# Motivation

The Fundamental Theorem of Algebra (FTA): **every non-constant polynomial with complex coefficients has a complex root**. From this, every degree-$n$ polynomial factors as $a_n(z - z_1)(z - z_2)\ldots(z - z_n)$ for some $z_1, \ldots, z_n \in \mathbb{C}$ (allowing repeats). Algebraically: $\mathbb{C}$ is **algebraically closed**.

The theorem is purely algebraic in statement but has no purely algebraic proof; the cleanest proof uses Liouville's theorem from complex analysis. There are also topological proofs (via the winding number) and analytic proofs (via maximum modulus). The complex-analytic proof is the *simplest* known.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem assumes "$p \in \mathbb{C}[z]$, non-constant".

**Targets (Output Amplification)**

The conclusion is "$p$ has a complex root".

Combine with **iteration.** Property $D$: factor out $(z - z_1)$, get a degree-$(n-1)$ polynomial. The amplified result: $p$ factors completely: $p(z) = a_n \prod_{i=1}^n (z - z_i)$. So every polynomial *splits* over $\mathbb{C}$.

Combine with **rational function theory.** Property $D$: a rational $f = p/q$. The amplified result: partial fraction decomposition exists, since $q$ factors into linear factors.

---

# Why Is It True

Suppose for contradiction $p$ has no roots. Then $1/p$ is entire (no poles to worry about). Show it is bounded: as $|z| \to \infty$, $|p(z)| \sim |a_n||z|^n \to \infty$, so $|1/p(z)| \to 0$. So $1/p$ is bounded for $|z| \geq R$ for some $R$, and by continuity bounded on the compact disc $|z| \leq R$. Hence $1/p$ is bounded entire.

By [[Thm - Liouville's Theorem]], $1/p$ is constant. So $p$ is constant — contradiction with the hypothesis $\deg p \geq 1$. Therefore $p$ has a root.

---

# What Makes This Hard

The proof is short — but each step relies on prior results: Liouville is built on Cauchy estimates, which use CIF, which uses Cauchy's theorem on a star-shaped domain, which uses Goursat. The FTA is the *capstone* of complex analysis, sitting on top of a tall tower. The conceptual difficulty is that there is no easy purely algebraic route — every known proof uses some non-algebraic input (analysis or topology).

---

# Rederivation Scaffold

**High-level strategy:**
Assume no root. Show $1/p$ is bounded entire. By Liouville, $1/p$ is constant, hence $p$ is constant — contradiction.

**Subgoal decomposition:**

1. **If $p$ has no roots, $1/p$ is entire.** Quotient rule, no zeros to worry about.

2. **$1/p$ is bounded.** Use $|p(z)| \to \infty$ as $|z| \to \infty$ to bound outside a disc, continuity inside.

3. **Liouville.** $1/p$ is constant.

4. **Contradiction.** $p$ constant means $\deg p = 0$, contradicting hypothesis.

---

# Lemma Decomposition

> [!note]- Lemma 1: $|p(z)| \to \infty$ as $|z| \to \infty$ for a non-constant polynomial
> **Statement:** For $p(z) = a_n z^n + \ldots + a_0$ with $n \geq 1, a_n \neq 0$: there is $R > 0$ such that $|p(z)| > 1$ for all $|z| > R$.
>
> **Hint:** Factor out $a_n z^n$ and use that the remaining factor tends to $1$.
>
> > [!note]- Full proof
> > $p(z) = a_n z^n (1 + a_{n-1}/(a_n z) + \ldots + a_0/(a_n z^n))$. The parenthetical factor tends to $1$ as $|z| \to \infty$, so its modulus exceeds $1/2$ for $|z|$ large. Hence $|p(z)| \geq |a_n||z|^n/2 \to \infty$. In particular $|p(z)| > 1$ for $|z|$ large enough. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Suppose for contradiction that $p$ has no roots. Then $1/p$ is holomorphic on $\mathbb{C}$ (entire).
>
> By Lemma 1, there is $R$ with $|p(z)| > 1$ for $|z| > R$. So $|1/p(z)| < 1$ for $|z| > R$. On the compact disc $|z| \leq R$, $|1/p|$ is continuous (no zeros) and hence bounded — say $|1/p(z)| \leq M$ on $|z| \leq R$. Combining, $|1/p(z)| \leq \max(M, 1)$ for all $z \in \mathbb{C}$.
>
> So $1/p$ is bounded entire. By [[Thm - Liouville's Theorem]], $1/p$ is constant, hence $p$ is constant — contradicting $\deg p \geq 1$.
>
> Therefore $p$ has a complex root. $\blacksquare$
>
> **Corollary: every polynomial of degree $n$ has $n$ roots (counted with multiplicity).** Inductively: $p$ has a root $z_1$; factor $p(z) = (z - z_1) q(z)$ with $\deg q = n - 1$; apply FTA to $q$ iteratively.

---

# Cross-Field Exercise Suggestions

**Topological proof.** An alternative proof: as $|z|$ runs over a large circle $|z| = R$, $p(z)/|a_n z^n|$ traces out a curve close to $1$ (so winding number around $0$ is $0$); but $p(z)/|a_n||R^n|$ winds around $0$ exactly $n$ times (the leading term). By continuity, somewhere between, $p$ must hit $0$. This uses winding number from algebraic topology.

**Algebraic closure.** FTA is the statement that $\mathbb{C}$ is *algebraically closed*: every non-constant polynomial splits. This is a structural fact about $\mathbb{C}$ as a field. There is no analogous statement for $\mathbb{R}$ (which has the polynomial $x^2 + 1$ with no real root), and for $\mathbb{Q}$, algebraic closure is a different field (the algebraic closure $\bar{\mathbb{Q}}$).

**Galois theory.** The algebraic-closure structure of $\mathbb{C}$ underlies the Galois correspondence: extensions of $\mathbb{Q}$ inside $\bar{\mathbb{Q}}$ are classified by their Galois groups, the symmetries of root sets.

---

# Bridges

- **[[Thm - Liouville's Theorem]]** — the direct tool.

- **[[Thm - Cauchy Estimates]]** — the deeper source via Liouville.

- **[[Ex - Cauchy estimates bound polynomial degree]]** — a generalization: entire functions of polynomial growth are polynomials.
