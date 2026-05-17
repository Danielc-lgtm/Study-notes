---
type: exercise
subject: measure-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - The Integral"
  - "Def - Lebesgue Measure"
  - "Thm - Dominated Convergence Theorem"
tags: [analysis, measure-theory]
---

# Problem Statement

**(a)** Show that the **Dirichlet function** $\mathbf{1}_{\mathbb{Q}\cap[0,1]}$ is Lebesgue-integrable with $\int\mathbf{1}_{\mathbb{Q}\cap[0,1]}\,d\lambda=0$, but is **not** Riemann-integrable.

**(b)** Exhibit it as a pointwise limit $f_n\uparrow\mathbf{1}_{\mathbb{Q}\cap[0,1]}$ of Riemann-integrable functions with $\int f_n\,dx=0$, illustrating that the Riemann integral does *not* commute with monotone limits.

**(c)** State the general fact: every Riemann-integrable $f$ on $[a,b]$ is Lebesgue-integrable with equal integral, and explain in one sentence why the converse fails.

**Recall:**

[[Def - The Integral|Lebesgue integral]]; [[Def - Lebesgue Measure|$\lambda(\mathbb{Q})=0$]]. A bounded $f$ is Riemann-integrable iff $\sup_P L(f,P)=\inf_P U(f,P)$ over partitions $P$.

---

# Convergent Strategy

**Problem class:** contrasting the two integrals on the canonical example, exhibiting the failure that motivated Lebesgue's theory.

**Assumption pattern:** $\mathbf{1}_\mathbb{Q}$ is $0$ a.e. (since $\lambda(\mathbb{Q})=0$), so its Lebesgue integral is $0$. Its Riemann sums oscillate maximally ($L=0$, $U=1$) because $\mathbb{Q}$ and $\mathbb{Q}^c$ are both dense.

**Theorem routing:** Lebesgue side — $f=0$ a.e. $\Rightarrow\int f\,d\lambda=0$. Riemann side — every partition has $L(f,P)=0$, $U(f,P)=1$.

**Key decision point:** the monotone-limit failure is the *point* — $f_n\uparrow f$, $\int f_n=0$, but $\int_{\text{Riemann}}f$ does not exist, so $\lim\int f_n\neq\int\lim f_n$ has no Riemann meaning.

---

# Legal Operations Used

1. **$f=0$ a.e. $\Rightarrow\int f\,d\lambda=0$.**
2. **Compute Riemann upper/lower sums** using density.
3. **Enumerate a countable set** to build the increasing approximants.

---

# Hints

> [!note]- Hint 1
> $\lambda(\mathbb{Q}\cap[0,1])=0$, so $\mathbf{1}_{\mathbb{Q}\cap[0,1]}=0$ $\lambda$-a.e. What is the Lebesgue integral of a function that is $0$ a.e.?

> [!note]- Hint 2
> For Riemann: on any subinterval, $\inf f=0$ (irrationals are dense) and $\sup f=1$ (rationals are dense). So $L(f,P)=0$, $U(f,P)=1$ for *every* partition.

> [!note]- Hint 3
> Enumerate $\mathbb{Q}\cap[0,1]=\{q_1,q_2,\dots\}$; let $f_n=\mathbf{1}_{\{q_1,\dots,q_n\}}$.

---

# Solution

**Step 1 — (a) Lebesgue side.** $\lambda(\mathbb{Q}\cap[0,1])=0$ ([[Def - Lebesgue Measure|countable set]]), so $\mathbf{1}_{\mathbb{Q}\cap[0,1]}=0$ $\lambda$-a.e. Hence it is measurable, non-negative, and $\int\mathbf{1}_{\mathbb{Q}\cap[0,1]}\,d\lambda=0$ ([[Ex - Markov's inequality|the integral of an a.e.-zero function is $0$]]).

*Riemann side.* For any partition $P$ of $[0,1]$ and any subinterval $[t_{i-1},t_i]$: $\inf f=0$ (it contains an irrational) and $\sup f=1$ (it contains a rational). So the lower sum $L(f,P)=\sum(t_i-t_{i-1})\cdot0=0$ and the upper sum $U(f,P)=\sum(t_i-t_{i-1})\cdot1=1$. Thus $\sup_P L=0\neq1=\inf_P U$ — $f$ is **not Riemann-integrable**.

**Step 2 — (b) Monotone-limit failure.** Enumerate $\mathbb{Q}\cap[0,1]=\{q_1,q_2,\dots\}$ and set $f_n=\mathbf{1}_{\{q_1,\dots,q_n\}}$. Each $f_n$ is a finite indicator, with only finitely many discontinuities, hence **Riemann-integrable**, and $\int_0^1 f_n\,dx=0$. Clearly $0\le f_1\le f_2\le\cdots$ and $f_n(x)\to\mathbf{1}_{\mathbb{Q}\cap[0,1]}(x)$ for every $x$. So $f_n\uparrow f$ with $f_n$ Riemann-integrable, $\int f_n=0$, yet the limit $f$ is *not* Riemann-integrable: the would-be identity "$\lim\int f_n=\int\lim f_n$" has no Riemann meaning. The Lebesgue integral, by contrast, gives $\int f_n\,d\lambda=0\to0=\int f\,d\lambda$ — consistent with [[Thm - Monotone Convergence Theorem|MCT]].

**Step 3 — (c) General fact.** Every Riemann-integrable $f$ on $[a,b]$ is Lebesgue-integrable with $\int f\,d\lambda=\int_a^b f(x)\,dx$ (Riemann sums are integrals of step functions, which are simple; the common limit is the Lebesgue integral). The converse fails because **the Riemann-integrable functions are not closed under pointwise (even monotone) limits** — exactly the defect (b) exhibits — whereas the Lebesgue-integrable functions are, by the convergence theorems.

> [!note]- Complete formal solution
> (a) $\mathbf{1}_{\mathbb{Q}\cap[0,1]}=0$ $\lambda$-a.e., so $\int\,d\lambda=0$; every Riemann partition has $L=0$, $U=1$, so it is not Riemann-integrable. (b) $f_n=\mathbf{1}_{\{q_1,\dots,q_n\}}\uparrow\mathbf{1}_{\mathbb{Q}\cap[0,1]}$, each Riemann-integrable with integral $0$, limit not Riemann-integrable. (c) Riemann-integrable $\Rightarrow$ Lebesgue-integrable with equal value; converse fails because Riemann-integrability is not closed under monotone limits. $\blacksquare$

---

# Key Takeaways

**The Lebesgue integral's decisive advantage is closure under limits, and the Dirichlet function is the minimal witness that the Riemann integral lacks it.** A pointwise-increasing sequence of perfectly nice (Riemann-integrable) functions can have a limit the Riemann theory cannot even integrate. The Lebesgue theory was *built* to fix this: its class of integrable functions is closed under monotone, dominated, and a.e. limits by the [[Thm - Monotone Convergence Theorem|MCT]]/[[Thm - Dominated Convergence Theorem|DCT]]/[[Thm - Fatou's Lemma|Fatou]] trio. This closure is the entire reason the Lebesgue integral, not the Riemann integral, is the foundation of $L^p$ spaces, Fourier analysis, and probability.

**"Equal a.e. to $0$ $\Rightarrow$ integral $0$" makes the Lebesgue integral blind to negligible sets — which is both its power and the reason it needs the [[Def - Almost Everywhere|a.e.]] framework.** The Riemann integral, tied to the *domain* partition, cannot ignore the dense set $\mathbb{Q}$; the Lebesgue integral, tied to the *measure*, sees $\mathbb{Q}$ as nothing. This is why two functions differing on a null set are interchangeable for all Lebesgue purposes, and why $L^p$ spaces are spaces of a.e.-equivalence classes.
