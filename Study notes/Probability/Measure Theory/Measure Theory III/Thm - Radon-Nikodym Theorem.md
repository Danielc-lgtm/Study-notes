---
type: theorem
subject: measure-theory
prereqs:
  - "Def - Absolute Continuity and Density"
  - "Def - Mutual Singularity"
  - "Def - σ-Finite Measure"
  - "Thm - Hahn and Jordan Decomposition"
  - "Thm - Monotone Convergence Theorem"
tags: [analysis, measure-theory, probability]
---

# Notation

$(X,\mathcal{A})$ a measurable space; $\mu,\nu$ $\sigma$-finite measures. $\nu\ll\mu$ — [[Def - Absolute Continuity and Density|absolute continuity]]; $\nu\perp\mu$ — [[Def - Mutual Singularity|mutual singularity]]; $\mathrm{d}\nu/\mathrm{d}\mu$ — the Radon–Nikodym derivative.

---

# Motivation

A non-negative function $f$ turns a measure $\mu$ into a new measure $f\mu$, $A\mapsto\int_A f\,d\mu$ — a [[Def - Absolute Continuity and Density|density measure]]. The Radon–Nikodym theorem is the *converse*: it says every measure that *could* be a density measure (every $\nu\ll\mu$) actually *is* one — there is a function $f=\mathrm{d}\nu/\mathrm{d}\mu$ with $\nu=f\mu$. And the more general **Lebesgue decomposition** says *any* $\sigma$-finite $\nu$ splits canonically into a density part plus a part [[Def - Mutual Singularity|singular]] to $\mu$.

This is the theorem that makes **conditional expectation** exist, that gives probability **densities** their meaning, that defines the **likelihood ratio** of statistics and the change-of-measure factor of stochastic analysis. It converts a *relationship between measures* ($\nu\ll\mu$) into a *function* ($\mathrm{d}\nu/\mathrm{d}\mu$) — the central such conversion in the subject.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal hypothesis is "$\mu,\nu$ are $\sigma$-finite measures with $\nu\ll\mu$." Many problems supply a measure-theoretic object that does not announce itself as a non-negative absolutely continuous measure, and the bridge to Radon-Nikodym is the disguised-source recognition.

The first disguised source is any signed measure $\nu$ absolutely continuous with respect to $\mu$. Radon-Nikodym is stated for non-negative measures, but the bridge to signed $\nu$ is the [[Thm - Hahn and Jordan Decomposition|Jordan decomposition]] $\nu=\nu^+-\nu^-$ into mutually singular non-negative parts. Absolute continuity $\nu\ll\mu$ passes to each piece — both $\nu^\pm\ll\mu$ — so each acquires a density, and the signed density $\mathrm{d}\nu/\mathrm{d}\mu:=\mathrm{d}\nu^+/\mathrm{d}\mu-\mathrm{d}\nu^-/\mathrm{d}\mu$ is well-defined. A concrete example: a finite signed measure $\nu$ on $\mathbb{R}$ given by $\nu(A)=\int_A x\,e^{-x^2}\,dx$ secretly has the integrand $x e^{-x^2}$ as its density relative to Lebesgue. Recognising $\nu\ll\lambda$ and Jordan-decomposing into $\nu^+$ on $\{x>0\}$ and $\nu^-$ on $\{x<0\}$ lets Radon-Nikodym hand back precisely this integrand, separately on each half-line.

The second disguised source is a sub-$\sigma$-algebra problem masquerading as a conditioning problem. Given $X\ge0$ integrable on $(\Omega,\mathcal{F},\mathbb{P})$ and a sub-$\sigma$-algebra $\mathcal{G}\subseteq\mathcal{F}$, the set function $\nu(A):=\int_A X\,d\mathbb{P}$ for $A\in\mathcal{G}$ is a finite measure on $\mathcal{G}$. The bridge: $\mathbb{P}|_\mathcal{G}(A)=0$ forces $\nu(A)=0$ since $X$ is integrable and $A$ is $\mathbb{P}$-null, so $\nu\ll\mathbb{P}|_\mathcal{G}$. Radon-Nikodym produces a $\mathcal{G}$-measurable density, and this density *is* the [[Def - Conditional Expectation|conditional expectation]] $\mathbb{E}[X\mid\mathcal{G}]$. A canonical example: constructing the regular conditional distribution $\mathbb{P}(B\mid\mathcal{G})$ for $B\in\mathcal{F}$ by applying this recipe to $X=\mathbf{1}_B$ and assembling the results into a kernel — the foundational construction of Markov kernels on Polish spaces.

The third disguised source is a probability law specified only by its distribution function or characteristic function. If $F:\mathbb{R}\to[0,1]$ is a distribution function, the induced Lebesgue-Stieltjes measure $\mu_F$ has a density relative to $\lambda$ precisely when $F$ is absolutely continuous as a real function — and the function-theoretic notion of absolute continuity coincides exactly with the measure-theoretic one on $\mathbb{R}$. The bridge: verify either the function-theoretic condition (controlled total variation under partition refinement) or check directly that the characteristic function $\hat\mu(t)=\int e^{itx}\,d\mu(x)$ lies in $L^1(\mathbb{R})$. A concrete example: in central limit theorem refinements one needs the density of a sum $S_n$, not just the distribution function. Once $\hat\mu_{S_n}\in L^1$ is established (typically via Berry-Esseen bounds), Fourier inversion plus Riemann-Lebesgue gives $\mu_{S_n}\ll\lambda$ with a continuous density, and Radon-Nikodym makes this density explicit.

**Targets (Output Amplification)**

The conclusion is "$\nu$ has a density $f=\mathrm{d}\nu/\mathrm{d}\mu$ relative to $\mu$." Combined with other tools, this single function unlocks structures across probability, statistics, and stochastic analysis.

The first amplification is Radon-Nikodym with the Lebesgue decomposition for signed $\sigma$-finite measures. The decomposition $\nu=\nu_{ac}+\nu_s$ pairs with Radon-Nikodym to give $\nu=f\mu+\nu_s$ with $f$ measurable and $\nu_s\perp\mu$. Amplified further: every $\sigma$-finite signed measure on $\mathbb{R}$ admits the canonical three-way decomposition $\nu=f\lambda+\nu_d+\nu_{sc}$ into absolutely continuous, discrete, and singular continuous parts (apply Lebesgue decomposition iteratively against Lebesgue and counting measures). This is the structural backbone of measure theory on $\mathbb{R}$ — every measure splits uniquely into density-times-Lebesgue, atomic, and Cantor-like pieces. The combination is non-obvious because the singular continuous part is invisible at the level of pointwise inspection; Radon-Nikodym is precisely the instrument that detects what is *not* a density and forces the residual structure into the open.

The second amplification is the chain rule for Radon-Nikodym derivatives. If $\rho\ll\mu\ll\nu$ are all $\sigma$-finite, then $\frac{\mathrm{d}\rho}{\mathrm{d}\nu}=\frac{\mathrm{d}\rho}{\mathrm{d}\mu}\cdot\frac{\mathrm{d}\mu}{\mathrm{d}\nu}$ holds $\nu$-almost everywhere. The combination is non-obvious because the three densities live in different $L^1$ spaces and the equality demands a genuine change-of-variables argument run through Radon-Nikodym uniqueness. This chain rule is the analytic engine behind Girsanov's theorem in stochastic analysis — the change-of-measure factor $\frac{\mathrm{d}\mathbb{Q}}{\mathrm{d}\mathbb{P}}$ on Wiener path space transforms the drift between Brownian motions under different measures — and behind the likelihood ratio statistic in classical statistics, where the Neyman-Pearson lemma identifies the optimal test for $\mathbb{P}_0$ versus $\mathbb{P}_1$ as a threshold on $\mathrm{d}\mathbb{P}_1/\mathrm{d}\mathbb{P}_0$.

The third amplification is Radon-Nikodym inside martingale convergence. Given a filtration $(\mathcal{F}_n)$ and measures $\mathbb{Q}\ll\mathbb{P}$ on each $\mathcal{F}_n$, the densities $M_n:=\frac{\mathrm{d}\mathbb{Q}|_{\mathcal{F}_n}}{\mathrm{d}\mathbb{P}|_{\mathcal{F}_n}}$ form a non-negative $\mathbb{P}$-martingale by the tower property — itself a Radon-Nikodym identity in disguise. Combined with Doob's martingale convergence theorem, the result is: $M_n\to M_\infty$ $\mathbb{P}$-almost surely, and when the martingale is uniformly integrable $M_\infty=\frac{\mathrm{d}\mathbb{Q}}{\mathrm{d}\mathbb{P}}$ on $\mathcal{F}_\infty$. This is the Doob-Dynkin machinery used to construct the Itô integral as a martingale $L^2$-limit, to prove Kakutani's dichotomy for product measures, and to establish the existence of regular conditional probabilities on Polish spaces by exhibiting them as almost-sure limits of finite-$\sigma$-algebra densities.

---

# Statement

**(Lebesgue decomposition.)** Let $\mu,\nu$ be $\sigma$-finite measures on $(X,\mathcal{A})$. There is a *unique* pair of measures with
$$\nu=\nu_{ac}+\nu_s,\qquad \nu_{ac}\ll\mu,\qquad \nu_s\perp\mu.$$

**(Radon–Nikodym.)** Moreover $\nu_{ac}$ has a density: there is a measurable $f:X\to[0,\infty]$, unique up to $\mu$-a.e. equality, with $\nu_{ac}(A)=\int_A f\,d\mu$ for all $A$. In particular, **if $\nu\ll\mu$ then $\nu_s=0$ and**
$$\nu(A)=\int_A f\,d\mu\quad\text{for all }A\in\mathcal{A},\qquad f=:\frac{\mathrm{d}\nu}{\mathrm{d}\mu}.$$

---

# Why Is It True

The cleanest route (von Neumann's) packages everything into one $L^2$ projection; the more elementary route builds the density as a *supremum*. Here is the supremum argument, which exposes the mechanism.

Assume $\mu,\nu$ finite (the $\sigma$-finite case splits $X$ into finite pieces and sums). Consider the family
$$\mathcal{G}=\Big\{g:X\to[0,\infty]\text{ measurable}:\int_A g\,d\mu\le\nu(A)\ \forall A\in\mathcal{A}\Big\}$$
of "candidate densities that never overshoot $\nu$." This family is **closed under pairwise maxima** ($g\vee h\in\mathcal{G}$ — split $A$ into $\{g>h\}$ and $\{g\le h\}$). Let $M=\sup_{g\in\mathcal{G}}\int g\,d\mu\le\nu(X)<\infty$, take $g_n\in\mathcal{G}$ with $\int g_n\to M$, and set $f=\lim_n(g_1\vee\cdots\vee g_n)$ — an increasing limit, so $f\in\mathcal{G}$ by [[Thm - Monotone Convergence Theorem|MCT]], and $\int f\,d\mu=M$ is the *largest possible*. This $f$ is the density of $\nu_{ac}$.

Now $\nu_s:=\nu-f\mu$ is a non-negative measure (since $f\in\mathcal{G}$). The claim is $\nu_s\perp\mu$. If not, a lemma (proved via [[Thm - Hahn and Jordan Decomposition|Hahn decomposition]] of $\nu_s-\varepsilon\mu$) produces $\varepsilon>0$ and a set $E$ with $\mu(E)>0$ on which $\nu_s\ge\varepsilon\mu$. But then $f+\varepsilon\mathbf{1}_E$ would *still* lie in $\mathcal{G}$ and have integral $M+\varepsilon\mu(E)>M$ — contradicting the maximality of $M$. So $\nu_s\perp\mu$, and $\nu=f\mu+\nu_s$ is the decomposition.

The slogan: **the density is the *largest* function whose integral never exceeds $\nu$; whatever mass of $\nu$ this largest density fails to capture cannot be "spread over $\mu$" at all — it must be singular**, for otherwise the density was not maximal. Maximality is the entire lever, exactly as it was for [[Thm - Hahn and Jordan Decomposition|Hahn]].

If $\nu\ll\mu$: any singular $\nu_s$ lives on a $\mu$-null set $A^c$; absolute continuity then forces $\nu_s$, being $\le\nu$, to vanish there too, so $\nu_s=0$ and $\nu=f\mu$.

Uniqueness: two decompositions' difference $\nu_{ac}-\nu_{ac}'=\nu_s'-\nu_s$ is simultaneously $\ll\mu$ and $\perp\mu$, hence $0$; densities agree $\mu$-a.e. because $\int_A(f-g)d\mu=0$ for all $A$ forces $f=g$ a.e.

---

# What Makes This Hard

Two non-obvious moves. (i) The **right object to maximise**: not "a density" directly but the family $\mathcal{G}$ of *sub-densities* (those never overshooting $\nu$), and one maximises $\int g\,d\mu$ over it — the density emerges as the optimum, à la Hahn. (ii) The **singularity of the remainder**: showing $\nu_s\perp\mu$ is *by contradiction with maximality*, and the contradiction needs an auxiliary [[Thm - Hahn and Jordan Decomposition|Hahn-decomposition]] argument on $\nu_s-\varepsilon\mu$ to find a set where one could enlarge the density. The role of **$\sigma$-finiteness** is the third subtlety — it is what lets the finite-case argument be assembled piecewise, and the theorem genuinely fails without it.

---

# Rederivation Scaffold

**High-level strategy.** Maximise $\int g\,d\mu$ over the sub-densities $g$ (those with $g\mu\le\nu$); the optimum $f$ is the density; the leftover $\nu-f\mu$ must be singular, else $f$ was not maximal.

**Subgoal decomposition.**

1. **Reduce to $\mu,\nu$ finite** via a $\sigma$-finite decomposition of $X$.
2. **$\mathcal{G}=\{g\ge0:g\mu\le\nu\}$ is closed under $\vee$.** Split $A$ by $\{g>h\}$.
3. **Maximiser exists.** $M=\sup_{\mathcal{G}}\int g\,d\mu<\infty$; $f=\lim(g_1\vee\cdots\vee g_n)\in\mathcal{G}$ by MCT, $\int f=M$.
4. **$\nu_s=\nu-f\mu\perp\mu$.** Else Hahn-decompose $\nu_s-\varepsilon\mu$, find $E$ with $\mu(E)>0$, $\nu_s\ge\varepsilon\mu$ on $E$; then $f+\varepsilon\mathbf{1}_E\in\mathcal{G}$ beats $M$ — contradiction.
5. **$\nu\ll\mu\Rightarrow\nu_s=0$; uniqueness** ($\ll$ and $\perp$ simultaneously $\Rightarrow0$).

---

# Lemma Decomposition

> [!note]- Lemma 1: The sub-density family has a maximiser
> **Statement:** $\mathcal{G}=\{g\ge0:\int_A g\,d\mu\le\nu(A)\,\forall A\}$ is closed under $\vee$, and $f:=\lim_n(g_1\vee\cdots\vee g_n)$ with $\int g_n\to M=\sup_\mathcal{G}\int g\,d\mu$ satisfies $f\in\mathcal{G}$, $\int f\,d\mu=M$.
>
> **Hint:** Closure under $\vee$ follows by splitting the integration domain along $\{g>h\}$ and $\{g\le h\}$; then take a maximising sequence, replace it by its running maxima (still in $\mathcal{G}$, still bounded by $\nu$), and pass to the limit via MCT.
>
> **Why needed:** This produces the candidate density $f$ — the largest "sub-density" of $\nu$ relative to $\mu$. Once $f$ is in hand, the remainder $\nu-f\mu$ must be singular (Lemma 2), giving the Lebesgue decomposition with $f$ as the Radon-Nikodym derivative of the absolutely continuous part.
>
> > [!note]- Full proof
> > For $g,h\in\mathcal{G}$, $\int_A(g\vee h)=\int_{A\cap\{g>h\}}g+\int_{A\cap\{g\le h\}}h\le\nu(A\cap\{g>h\})+\nu(A\cap\{g\le h\})=\nu(A)$, so $g\vee h\in\mathcal{G}$. The functions $h_n=g_1\vee\cdots\vee g_n$ increase, lie in $\mathcal{G}$, with $\int h_n\ge\int g_n\to M$; by [[Thm - Monotone Convergence Theorem|MCT]], $f=\lim h_n$ has $\int_A f=\lim\int_A h_n\le\nu(A)$, so $f\in\mathcal{G}$, and $\int f=M$. $\square$

> [!note]- Lemma 2: The remainder is singular
> **Statement:** $\nu_s=\nu-f\mu$ satisfies $\nu_s\perp\mu$.
>
> **Hint:** If not, Hahn-decompose $\nu_s-\varepsilon\mu$ to find a set on which the density can be enlarged.
>
> **Why needed:** Once $\nu_s\perp\mu$, the decomposition $\nu=f\mu+\nu_s$ is the Lebesgue decomposition of $\nu$ into an absolutely-continuous-with-respect-to-$\mu$ part (with density $f$) and a singular part. Under the hypothesis $\nu\ll\mu$ of Radon-Nikodym, the singular part vanishes and $\nu=f\mu$.
>
> > [!note]- Full proof
> > $\nu_s\ge0$ since $f\in\mathcal{G}$. Suppose $\nu_s\not\perp\mu$. For each $n$ let $(P_n,N_n)$ be a [[Thm - Hahn and Jordan Decomposition|Hahn decomposition]] of the signed measure $\nu_s-\tfrac1n\mu$, and $P=\bigcup_n P_n$. On $N=\bigcap N_n=P^c$, $\nu_s\le\tfrac1n\mu$ for all $n$, so $\nu_s(N)=0$; if also $\mu(P)=0$ then $\nu_s\perp\mu$ — contrary to assumption. So $\mu(P)>0$, hence $\mu(P_{n_0})>0$ for some $n_0$, and on $P_{n_0}$, $\nu_s\ge\tfrac1{n_0}\mu$. Then $f+\tfrac1{n_0}\mathbf{1}_{P_{n_0}}$ still lies in $\mathcal{G}$ (its excess over $f\mu$ on any $A$ is $\le\nu_s(A\cap P_{n_0})$), yet has integral $M+\tfrac1{n_0}\mu(P_{n_0})>M$ — contradicting maximality. So $\nu_s\perp\mu$. $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> Reduce to $\mu,\nu$ finite by a common $\sigma$-finite decomposition. Lemma 1 produces $f\in\mathcal{G}$ with $\int f\,d\mu=M$ maximal; set $\nu_{ac}=f\mu$, $\nu_s=\nu-f\mu\ge0$. Lemma 2 gives $\nu_s\perp\mu$, so $\nu=\nu_{ac}+\nu_s$ is a Lebesgue decomposition with $\nu_{ac}\ll\mu$ having density $f$. If $\nu\ll\mu$: $\nu_s\le\nu\ll\mu$ and $\nu_s\perp\mu$ force $\nu_s=0$. Uniqueness: a difference of two decompositions is both $\ll\mu$ and $\perp\mu$, hence $0$; and $\int_A(f-g)\,d\mu=0\ \forall A\Rightarrow f=g$ $\mu$-a.e. $\blacksquare$

---

# Cross-Field Exercise Suggestions

The headline application is **[[Def - Conditional Expectation|conditional expectation]]**: for $X\ge0$ integrable and a sub-$\sigma$-algebra $\mathcal{G}$, the set function $\nu(A)=\int_A X\,d\mathbb{P}$ on $\mathcal{G}$ satisfies $\nu\ll\mathbb{P}|_\mathcal{G}$, and its Radon–Nikodym derivative *is* $\mathbb{E}[X\mid\mathcal{G}]$ — Radon–Nikodym is one of the two standard constructions of conditional expectation (the other being $L^2$ projection). In statistics, $\mathrm{d}\mathbb{P}_\theta/\mathrm{d}\mathbb{P}_{\theta_0}$ is the **likelihood ratio**; in stochastic analysis the Girsanov change of measure is a Radon–Nikodym derivative on path space.

---

# Bridges

- **[[Def - Conditional Expectation]]** *(Advanced Probability)* — conditional expectation is a Radon–Nikodym derivative against a restricted measure.
- **[[Thm - Hahn and Jordan Decomposition]]** — supplies the auxiliary decomposition in Lemma 2, and the extension to *signed* $\nu$.
- **[[Def - Absolute Continuity and Density]]** — this theorem is the converse promised there: $\nu\ll\mu\Rightarrow\nu$ has a density.
