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

Four above-floor prerequisites are used repeatedly below; each gets a three-field recall so the reader can proceed without opening another file.

> [!recall]- Locally compact separable metric space $E$ with a Radon measure $m$ of full support
> **Formally:** $E$ is a metric space that is *locally compact* (every point has a compact neighbourhood) and *separable* (has a countable dense subset). $m:\operatorname{Borel}(E)\to[0,\infty]$ is a *Radon* measure — finite on compacts, inner regular on open sets, outer regular on Borel sets — and has *full support*, meaning $m(U)>0$ for every non-empty open $U\subseteq E$.
> **In words:** a space with a distance function, tame enough that continuous compactly-supported functions form a well-behaved space, together with a way to integrate them (a measure) that assigns positive mass to every open ball.
> **Concretely:** $\mathbb R^n$ with Lebesgue measure; a Riemannian surface with its volume measure $\operatorname{vol}_g$; a countable disjoint union of points with counting measure. **Non-example:** $\mathbb R$ with the Dirac measure $\delta_0$ at $0$ — not full support, since every open set that avoids $0$ has zero mass.

> [!recall]- Self-adjoint operator $A$ on a Hilbert space and its fractional powers $\operatorname{Dom}(A^{1/2})$
> **Formally:** $A:\operatorname{Dom}(A)\to H$ is densely defined, *symmetric* ($\langle Au,v\rangle=\langle u,Av\rangle$ on $\operatorname{Dom}(A)$), and *self-adjoint* ($\operatorname{Dom}(A)=\operatorname{Dom}(A^*)$). When $A\ge 0$, its unique non-negative self-adjoint square root $A^{1/2}$ is defined by the functional calculus: if $A=\int\lambda\,dE_\lambda$ is the spectral resolution, then $A^{1/2}=\int\lambda^{1/2}\,dE_\lambda$, with $\operatorname{Dom}(A^{1/2})=\{u\in H:\int\lambda\,d\langle E_\lambda u,u\rangle<\infty\}$.
> **In words:** the infinite-dimensional analogue of a real symmetric matrix — it has a real spectrum and an orthonormal eigenvector basis (possibly continuous), so any measurable function $f(A)$ makes sense by acting as $f(\lambda_j)$ on the $j$-th coordinate. $A^{1/2}$ is the operator with the *same eigenvectors* but eigenvalues $\sqrt{\lambda_j}$.
> **Concretely:** $A=-\Delta$ on $L^2(\mathbb R^n)$ is self-adjoint with $\operatorname{Dom}(A)=H^2(\mathbb R^n)$; $A^{1/2}=\sqrt{-\Delta}$ is the "positive square root of the Laplacian" appearing in the fractional heat equation $\partial_t u=-A^{1/2}u$, whose Fourier symbol is $|\xi|$ (compare $A$'s symbol $|\xi|^2$).

> [!recall]- Strongly continuous semigroup $e^{-tA}$
> **Formally:** a family $\{e^{-tA}\}_{t\ge 0}$ of bounded operators on $H$ with $e^{0\cdot A}=\operatorname{id}$, the *semigroup law* $e^{-(t+s)A}=e^{-tA}e^{-sA}$ for $t,s\ge0$, and *strong continuity* $\lim_{t\to 0^+}\|e^{-tA}u-u\|=0$ for every $u\in H$ (equivalently, $t\mapsto e^{-tA}u$ is norm-continuous on $[0,\infty)$).
> **In words:** a "one-parameter dynamics" on $H$ that at each time $t$ is a bounded operator, that composes correctly (running for time $t+s$ = running for $t$ then for $s$), and that varies continuously in $t$. It solves the abstract heat equation $\partial_t u=-Au$ with initial datum $u_0$ via $u(t)=e^{-tA}u_0$.
> **Concretely:** for $A=-\Delta$ on $L^2(\mathbb R^n)$, $e^{-tA}$ is convolution with the Gaussian heat kernel $(4\pi t)^{-n/2}\exp(-|x|^2/(4t))$; running it for time $t$ then time $s$ convolves with the two kernels in succession, and the semigroup identity says this equals convolution with the single Gaussian of variance $2(t+s)$.

> [!recall]- Hunt process (used in the Dirichlet-form ↔ Markov-process correspondence)
> **Formally:** a Markov process $(X_t)_{t\ge 0}$ on $E$ with *càdlàg* paths (right-continuous with left limits) whose Markov property survives replacement of a deterministic time $t$ by any stopping time $\tau$: conditional on $X_\tau$, the future $(X_{\tau+s})_{s\ge 0}$ is independent of the past and distributed as the process started from $X_\tau$ (*strong Markov property*).
> **In words:** a random-walking process whose transitions from time $t$ only depend on where it is at time $t$ (memoryless), even when "time $t$" is itself a random time chosen by looking at the process's past.
> **Concretely:** Brownian motion on $\mathbb R^n$; the Poisson process; every Lévy process (independent stationary increments, càdlàg); killed versions of any of these (killed at a fixed rate, or on hitting a set).

---

# Axiom Motivation

The heat semigroup came from a specific operator, the Laplace–Beltrami operator. But the paper wants to run *many* related diffusions — Brownian motion, killed Brownian motion, $\alpha$-stable jump processes — without rebuilding the theory each time. A **Dirichlet form** is the abstraction that produces, from a single "energy functional", a self-adjoint operator, a heat semigroup, a heat kernel, *and* a Markov process, all at once. It is the machine that guarantees the objects the paper needs exist and fit together.

The idea is to encode a diffusion by its **energy** rather than its generator. For the Laplacian the energy of a function is $\mathcal E(u,u)=\int_X|\nabla u|^2\,d\operatorname{vol}_g$ — the Dirichlet energy, the total "steepness" of $u$. Three properties of this functional turn out to be exactly what is needed. **Symmetry and non-negativity** ($\mathcal E(u,u)\ge0$) make the associated operator self-adjoint and positive, so its spectral calculus (which is what lets $e^{-tA}$ be defined; see the recall above) exists. **Closedness** (the domain $\mathcal F$ is complete in the energy norm) makes the operator well-defined rather than merely formal. And the **Markov property** (contracting $u$ towards $[0,1]$ never increases its energy) is precisely the analytic fingerprint of a *probabilistic* process: it is equivalent to the semigroup being positivity-preserving and sub-Markovian, i.e. to $e^{-tA}$ being the transition operator of an honest (possibly killed) random motion. Le Jan's insight, which the paper follows, is that the loop measure can be built purely from this data $(\mathcal E,\mathcal F)$, so *any* such form — not just the Laplacian's — gives a loop measure.

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

**Standard names.** **Dirichlet form**, its **generator** $-A$, its **semigroup** $e^{-tA}$, the **Dirichlet–Markov process** correspondence (Fukushima–Ōshima–Takeda, *Dirichlet Forms and Symmetric Markov Processes*). The correspondence produces a **Hunt process** (as recalled above; the extra technical property "quasi-left-continuous" is a refinement not used in this paper's applications and can be treated as background).

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
