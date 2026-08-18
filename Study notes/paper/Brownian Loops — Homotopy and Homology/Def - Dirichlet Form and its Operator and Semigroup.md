---
type: definition
subject: analysis
prereqs:
  - "Def - Heat Kernel and Heat Semigroup"
  - "Def - Self-Adjoint Operator"
tags: [analysis, functional-analysis, markov-processes, paper-prereq]
source: "Brownian Loops — Homotopy and Homology"
---

# Notation

$(E,m)$ a nice measure space (a locally compact separable metric space $E$ with a Radon measure $m$ of full support — for the paper, $E=X$ the surface and $m=\operatorname{vol}_g$). $L^2(E,m)$ the Hilbert space of square-integrable functions, inner product $\langle u,v\rangle=\int_E u\bar v\,dm$, norm $\|u\|=\langle u,u\rangle^{1/2}$. $\mathcal F\subseteq L^2$ a dense linear subspace (the "domain"). $\mathcal E:\mathcal F\times\mathcal F\to\mathbb{R}$ a bilinear form.

---

# Axiom Motivation

The heat semigroup came from a specific operator, the Laplace–Beltrami operator. But the paper wants to run *many* related diffusions — Brownian motion, killed Brownian motion, $\alpha$-stable jump processes — without rebuilding the theory each time. A **Dirichlet form** is the abstraction that produces, from a single "energy functional", a self-adjoint operator, a heat semigroup, a heat kernel, *and* a Markov process, all at once. It is the machine that guarantees the objects the paper needs exist and fit together.

The idea is to encode a diffusion by its **energy** rather than its generator. For the Laplacian the energy of a function is $\mathcal E(u,u)=\int_X|\nabla u|^2\,d\operatorname{vol}_g$ — the Dirichlet energy, the total "steepness" of $u$. Three properties of this functional turn out to be exactly what is needed. **Symmetry and non-negativity** ($\mathcal E(u,u)\ge0$) make the associated operator self-adjoint and positive, so its spectral calculus (hence $e^{-tA}$) exists. **Closedness** (the domain $\mathcal F$ is complete in the energy norm) makes the operator well-defined rather than merely formal. And the **Markov property** (contracting $u$ towards $[0,1]$ never increases its energy) is precisely the analytic fingerprint of a *probabilistic* process: it is equivalent to the semigroup being positivity-preserving and sub-Markovian, i.e. to $e^{-tA}$ being the transition operator of an honest (possibly killed) random motion. Le Jan's insight, which the paper follows, is that the loop measure can be built purely from this data $(\mathcal E,\mathcal F)$, so *any* such form — not just the Laplacian's — gives a loop measure.

---

# The Definition

> **Definition (regular symmetric Dirichlet form).** A **symmetric Dirichlet form** on $L^2(E,m)$ is a bilinear form $\mathcal E:\mathcal F\times\mathcal F\to\mathbb{R}$ on a dense linear subspace $\mathcal F\subseteq L^2(E,m)$ such that:
> 1. **Symmetric and non-negative:** $\mathcal E(u,v)=\mathcal E(v,u)$ and $\mathcal E(u,u)\ge0$.
> 2. **Closed:** $\mathcal F$ is a Hilbert space under the norm $\|u\|_{\mathcal E}=\big(\mathcal E(u,u)+\|u\|^2\big)^{1/2}$.
> 3. **Markovian (the Dirichlet property):** for every $u\in\mathcal F$, the "clipped" function $u^\#:=(0\vee u)\wedge 1$ (push $u$ into $[0,1]$) is in $\mathcal F$ and $\mathcal E(u^\#,u^\#)\le\mathcal E(u,u)$.
>
> It is **regular** if $\mathcal F\cap C_c(E)$ is dense both in $\mathcal F$ (energy norm) and in $C_c(E)$ (uniform norm) — a compatibility between the form and the topology of $E$.

> **Definition (associated operator, semigroup, kernel).** A symmetric Dirichlet form determines a unique **non-negative self-adjoint operator** $A$ on $L^2(E,m)$ with $\mathcal F=\operatorname{Dom}(A^{1/2})$ and
> $$\mathcal E(u,v)=\langle A^{1/2}u,\,A^{1/2}v\rangle,\qquad \mathcal E(u,v)=\langle Au,v\rangle\ \text{ for } u\in\operatorname{Dom}(A),\,v\in\mathcal F,$$
> hence a **strongly continuous semigroup** $e^{-tA}$. We assume throughout (as the paper does) that this semigroup has a symmetric **transition density** $p^E(t,x,y)$ with respect to $m$: $\big(e^{-tA}f\big)(x)=\int_E p^E(t,x,y)f(y)\,m(dy)$. By the correspondence between regular symmetric Dirichlet forms and symmetric Markov (Hunt) processes, $(\mathcal E,\mathcal F)$ also determines a **Markov process** on $E$ (unique up to negligible sets) whose transition density is $p^E$.

**Concrete unpacking.** The template is $E=X$, $m=\operatorname{vol}_g$, $\mathcal E(u,v)=\int_X\langle\nabla u,\nabla v\rangle\,d\operatorname{vol}_g$, $\mathcal F=$ the Sobolev space $H^1(X)$. Then $A=\Delta_X$, $e^{-tA}$ is the heat semigroup, $p^E=p_X$ the [[Def - Heat Kernel and Heat Semigroup|heat kernel]], and the Markov process is [[Def - Brownian Motion on a Riemannian Manifold|Brownian motion]]. The three axioms read: symmetry/positivity ($\int|\nabla u|^2\ge0$, obvious); closedness ($H^1$ is complete); Markov (clipping $u$ into $[0,1]$ flattens it, so $\int|\nabla u^\#|^2\le\int|\nabla u|^2$). Adding a killing term $\kappa\int u^2$ gives the killed form $\mathcal E_\kappa$; this is the paper's Example 2.6.

**Standard names.** **Dirichlet form**, its **generator** $-A$, its **semigroup** $e^{-tA}$, the **Dirichlet–Markov process** correspondence (Fukushima–Ōshima–Takeda, *Dirichlet Forms and Symmetric Markov Processes*). A **Hunt process** is a strong-Markov, right-continuous, quasi-left-continuous process — the precise regularity class the correspondence produces.

---

# Examples and Non-Examples

**Is an instance.** The Dirichlet-energy form $\int_X|\nabla u|^2\,d\operatorname{vol}_g$ ($\to$ Brownian motion). The killed form $\int|\nabla u|^2+\kappa\int u^2$ ($\to$ Brownian motion killed at rate $\kappa$). The subordinate forms $\mathcal E^\phi$ of [[Def - Bernstein Function, Subordinator, and Subordination|subordination]] ($\to$ jump processes).

**Is NOT an instance.** The form $\mathcal E(u,v)=\int u'v''$ is **not** a Dirichlet form — it is neither symmetric nor non-negative, so it corresponds to no self-adjoint operator and no Markov process. Dropping the Markovian axiom 3 keeps a self-adjoint operator but loses the *probabilistic* interpretation (the semigroup need not preserve positivity), which is the whole point here.

**Calibration check.** (1) Verify the Dirichlet energy satisfies all three axioms. (2) From $\mathcal E(u,v)=\langle Au,v\rangle$, recover $A=\Delta_X$ by integration by parts for the energy form. (3) Explain why the Markov axiom is what makes $e^{-tA}$ a *probability* transition operator rather than merely a bounded operator.

---

# Where the paper uses this

§2.2 develops the loop measure for an *arbitrary* regular symmetric Dirichlet form $(\mathcal E,\mathcal F)$ with transition density $p^E$, following Le Jan; every later loop measure (Brownian, killed, subordinate) is an instance. The operator $A$, semigroup $e^{-tA}$, and kernel $p^E$ are exactly the data plugged into the [[Def - Dirichlet Form Loop Measure|Dirichlet-form loop measure]]. Subordination (§2.3) acts on this data by replacing $A$ with $\phi(A)$. **[[Paper - Brownian Loops — Homotopy and Homology — §2 Preliminaries|§2]]**.

---

# Verified against

Fukushima, Ōshima, Takeda, *Dirichlet Forms and Symmetric Markov Processes* (2nd ed.), Ch. 1 (definition: symmetric, closed, Markovian; regularity) and Ch. 7 (Dirichlet form ↔ Hunt process correspondence); Ma–Röckner, *Introduction to the Theory of (Non-Symmetric) Dirichlet Forms*, for the operator/semigroup dictionary $\mathcal F=\operatorname{Dom}(A^{1/2})$, $\mathcal E(u,v)=\langle A^{1/2}u,A^{1/2}v\rangle$. Matches the paper's §2.2 references [FOT11], [Fuk71].
