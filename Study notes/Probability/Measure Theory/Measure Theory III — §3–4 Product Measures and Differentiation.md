---
type: topic
subject: measure-theory
chapter: "3.1-4.2"
title: "Measure Theory III — Product Measures, Fubini, Differentiation, Radon–Nikodym"
tags: [analysis, measure-theory, probability]
---

# Notation Registry

- $(X_i,\mathcal{A}_i,\mu_i)$ — measure spaces, usually $\sigma$-finite; $X=X_1\times X_2$
- $\mathcal{A}_1\otimes\mathcal{A}_2$ — the [[Def - Product σ-Algebra|product σ-algebra]]; $\mu_1\otimes\mu_2$ — the [[Thm - Product Measure|product measure]]
- $Z_i$ — coordinate projections; $E_{x_1}=\{x_2:(x_1,x_2)\in E\}$ — the slice of $E$ at $x_1$
- $\mathcal{P}$ — a $\pi$-system; $\mathcal{L}$ — a $\lambda$-system (see [[Thm - Dynkin's π-λ Theorem]])
- $B(x,r)$ — open ball; $\fint_B=\frac1{\lambda(B)}\int_B$ — the average; $f^*$ — the [[Def - Hardy-Littlewood Maximal Function|Hardy–Littlewood maximal function]]
- $L^1_{loc}$ — locally integrable functions
- $\alpha$ — a [[Def - Signed Measure|signed measure]]; $\alpha^+,\alpha^-$ — its Jordan parts; $|\alpha|=\alpha^++\alpha^-$ — total variation
- $\nu\ll\mu$ — [[Def - Absolute Continuity and Density|absolute continuity]]; $\nu\perp\mu$ — [[Def - Mutual Singularity|mutual singularity]]; $\mathrm{d}\nu/\mathrm{d}\mu$ — the Radon–Nikodym derivative
- $\nu=\nu_{ac}+\nu_s$ — the Lebesgue decomposition

---

# Motivation

[[Measure Theory I — §1 Measure Spaces|Measure Theory I]] built measures; [[Measure Theory II — §2 Integration|Measure Theory II]] built the integral. This chapter is the *calculus* of the theory — how to integrate in several variables, how to differentiate, and how one measure relates to another.

**Product measures and Fubini–Tonelli** (§3) answer: how do you integrate a function of two variables? You build a measure $\mu_1\otimes\mu_2$ on the product space — the unique one giving rectangles the product of side-measures — and [[Thm - Fubini-Tonelli Theorem|Fubini–Tonelli]] reduces the double integral to an iterated one, computable a variable at a time. Tonelli handles non-negative integrands with no further hypothesis; Fubini handles signed integrands under absolute integrability. The technical tool that makes both work is [[Thm - Dynkin's π-λ Theorem|Dynkin's π–λ theorem]] — the induction principle that pushes facts from the generating rectangles to the whole product $\sigma$-algebra, and the standard route to uniqueness of measures.

**Differentiation** (§4.1) answers: is the fundamental theorem of calculus true for merely integrable functions? The [[Thm - Lebesgue Differentiation Theorem|Lebesgue differentiation theorem]] says *yes, almost everywhere* — the local averages $\fint_{B(x,r)}f$ recover $f(x)$ a.e. The proof introduces the [[Def - Hardy-Littlewood Maximal Function|Hardy–Littlewood maximal function]] and its weak maximal inequality, the prototype of harmonic analysis and the device that bounds the exceptional set in any a.e.-convergence theorem.

**Radon–Nikodym** (§4.2) answers: when is one measure a *density* times another? A [[Def - Signed Measure|signed measure]] is first decomposed ([[Thm - Hahn and Jordan Decomposition|Hahn/Jordan]]) into positive and negative parts; then the [[Thm - Radon-Nikodym Theorem|Radon–Nikodym theorem]] shows every $\nu\ll\mu$ (with $\mu,\nu$ $\sigma$-finite) has a density $\mathrm{d}\nu/\mathrm{d}\mu$, and every $\nu$ splits canonically into a part with a density and a part [[Def - Mutual Singularity|singular]] to $\mu$. This is the theorem that *constructs* [[Def - Conditional Expectation|conditional expectation]] and gives probability densities and likelihood ratios their meaning — the keystone linking measure theory to probability.

---

# Concept Map

## §3.1 Product Measures

- **[[Def - Product σ-Algebra]]**
	- $\mathcal{A}_1\otimes\mathcal{A}_2=\sigma(\text{measurable rectangles})=\sigma(Z_1,Z_2)$ — the smallest $\sigma$-algebra making the coordinate projections measurable, the categorical product in $\mathbf{Meas}$. Rectangles form a $\pi$-system; slices of product-measurable sets are measurable. $\mathcal{B}(\mathbb{R}^m)\otimes\mathcal{B}(\mathbb{R}^n)=\mathcal{B}(\mathbb{R}^{m+n})$, but Lebesgue $\sigma$-algebras do not multiply (the product is not complete).
- **[[Thm - Dynkin's π-λ Theorem]]**
	- A $\lambda$-system containing a generating $\pi$-system contains the whole $\sigma$-algebra. The induction principle for generated $\sigma$-algebras: it propagates a property checkable on simple generators to all measurable sets. Yields measure uniqueness (agree on a $\pi$-system $\Rightarrow$ agree everywhere) — the form used pervasively in probability.
- **[[Thm - Product Measure]]**
	- For $\sigma$-finite $\mu_i$, a unique measure $\mu_1\otimes\mu_2$ with $(\mu_1\otimes\mu_2)(A_1\times A_2)=\mu_1(A_1)\mu_2(A_2)$, given by integrating the slice measure. Existence is the slice formula plus MCT; uniqueness is $\pi$–$\lambda$. $\lambda_m\otimes\lambda_n=\lambda_{m+n}$.

> [!note] Exercise Index — §3.1
> [[Exercise Index - §3.1 Product Measures]]

## §3.2 Fubini's Theorem

- **[[Thm - Fubini-Tonelli Theorem]]**
	- A double integral equals an iterated integral, in either order. **Tonelli**: for $f\ge0$, unconditionally. **Fubini**: for $f\in L^1(\mu_1\otimes\mu_2)$. Tonelli is the standard machine (indicators $=$ product-measure theorem, simple, $f\ge0$ by MCT); Fubini splits $f=f^+-f^-$. The discipline: Tonelli on $|f|$ first, then Fubini. Without absolute integrability the iterated integrals can disagree.

> [!note] Exercise Index — §3.2
> [[Exercise Index - §3.2 Fubini's Theorem]]

## §4.1 Differentiation of the Lebesgue Integral

- **[[Def - Hardy-Littlewood Maximal Function]]**
	- $f^*(x)=\sup_r\fint_{B(x,r)}|f|$ — the worst-case local average. Measurable, satisfies the weak **maximal inequality** $\lambda(f^*>a)\le\frac{5^n}{a}\|f\|_1$, but $f^*\notin L^1$ (it decays only like $|x|^{-n}$). The prototype of harmonic analysis; the device that bounds exceptional sets.
- **[[Thm - Lebesgue Differentiation Theorem]]**
	- For every $f\in L^1_{loc}(\mathbb{R}^n)$, $\fint_{B(x,r)}f\to f(x)$ for a.e. $x$ — the measure-theoretic fundamental theorem of calculus. Proved by "dense class (continuous functions) + maximal inequality to kill the exceptional set," the maximal inequality itself proved by the Vitali covering lemma. Gives Lebesgue points and the density theorem.

> [!note] Exercise Index — §4.1
> [[Exercise Index - §4.1 Differentiation of the Integral]]

## §4.2 Lebesgue Decomposition and Radon–Nikodym

- **[[Def - Signed Measure]]**
	- A $\sigma$-additive set function of either sign (at most one infinite value). Positive/negative sets are regions of pure charge. The prototype is $\int_A f\,d\mu$ for signed $f$; signed measures form a vector space.
- **[[Def - Mutual Singularity]]**
	- $\mu\perp\nu$: the measures live on disjoint sets. The opposite extreme to [[Def - Absolute Continuity and Density|absolute continuity]]; $\delta_x\perp\lambda$. One of the two poles of the Lebesgue decomposition.
- **[[Thm - Hahn and Jordan Decomposition]]**
	- Every signed measure splits its space into a positive and a negative set (Hahn), equivalently writes as $\alpha=\alpha^+-\alpha^-$ with $\alpha^+\perp\alpha^-$ (Jordan). Proved by taking a maximally-negative set; gives the total-variation measure $|\alpha|$.
- **[[Thm - Radon-Nikodym Theorem]]**
	- For $\sigma$-finite $\mu,\nu$: every $\nu$ splits as $\nu_{ac}+\nu_s$ ($\nu_{ac}\ll\mu$, $\nu_s\perp\mu$, Lebesgue decomposition), and $\nu_{ac}$ has a density $f=\mathrm{d}\nu_{ac}/\mathrm{d}\mu$. If $\nu\ll\mu$ then $\nu=f\mu$. Proved by maximising a sub-density; constructs conditional expectation.

> [!note] Exercise Index — §4.2
> [[Exercise Index - §4.2 Radon-Nikodym]]

---

# Sources and Targets

**Targets — What do we usually try to prove?** (1) *That a measure equals another* — uniqueness of a product measure, of a law, of an extension — proved by agreeing on a generating $\pi$-system and invoking [[Thm - Dynkin's π-λ Theorem|Dynkin]]. (2) *Evaluation of a multiple integral* — reduced to iterated one-variable integrals by [[Thm - Fubini-Tonelli Theorem|Fubini–Tonelli]]. (3) *An almost-everywhere limit statement* — local averages converge, a martingale converges — proved by the dense-class-plus-maximal-inequality template. (4) *That one measure is a density times another*, and the decomposition of a measure into absolutely continuous and singular parts — [[Thm - Radon-Nikodym Theorem|Radon–Nikodym]].

**Sources — What assumptions do we leverage?** *$\sigma$-finiteness* is the omnipresent hypothesis — it makes product measures unique, Fubini–Tonelli valid, and Radon–Nikodym true; without it each fails. *A generating $\pi$-system* routes to Dynkin's theorem. *Non-negativity* of the integrand routes to Tonelli (free); *absolute integrability* to Fubini. *Local integrability* routes to the differentiation theorem. *Absolute continuity $\nu\ll\mu$* (checkable as "$\mu$-null $\Rightarrow\nu$-null") routes to Radon–Nikodym. The recurring recognition skill: spotting the $\pi$-system, or verifying $\sigma$-finiteness and absolute continuity, hidden in a concrete problem.

---

# Legal Operations

1. **Generate-and-propagate via $\pi$–$\lambda$.** To prove a property for all sets of a product (or generated) $\sigma$-algebra, verify it on the generating $\pi$-system and check the good sets form a $\lambda$-system; [[Thm - Dynkin's π-λ Theorem|Dynkin]] does the rest. The route to measure uniqueness and to the slice/section lemmas.

2. **Iterate a double integral.** Convert $\int f\,d(\mu_1\otimes\mu_2)$ to an iterated integral via [[Thm - Fubini-Tonelli Theorem|Fubini–Tonelli]] — *Tonelli on $|f|$ first* to certify integrability, then Fubini on $f$ to interchange.

3. **The standard machine for product integrals.** Prove a two-variable identity for indicators (where it is the [[Thm - Product Measure|product-measure]] theorem), extend to simple functions by linearity, to $f\ge0$ by MCT, to signed $f$ by $f^\pm$.

4. **Slice.** Replace a statement about a product-measurable set or function by statements about its slices, each one variable simpler — the foundation of Fubini.

5. **Dense class + maximal inequality.** To prove an a.e.-convergence theorem: prove it on a dense easy class (continuous functions), then bound the exceptional set for general $f$ by a [[Def - Hardy-Littlewood Maximal Function|maximal inequality]]. The template for the [[Thm - Lebesgue Differentiation Theorem|differentiation theorem]], martingale convergence, the ergodic theorem.

6. **Covering and disjointifying.** From a family of balls covering a set, extract a *disjoint* subfamily whose dilates still cover (Vitali covering lemma) — the geometric engine of the maximal inequality.

7. **Decompose a measure.** Split a [[Def - Signed Measure|signed measure]] into $\alpha^+-\alpha^-$ ([[Thm - Hahn and Jordan Decomposition|Jordan]]); split any measure into $\nu_{ac}+\nu_s$ ([[Thm - Radon-Nikodym Theorem|Lebesgue decomposition]]); extract the density $\mathrm{d}\nu/\mathrm{d}\mu$ when $\nu\ll\mu$.

8. **Recognise a Radon–Nikodym derivative.** When an object is characterised by "$\mathcal{G}$-measurable, and integrates the same as $X$ over $\mathcal{G}$-sets," it *is* a density on $\mathcal{G}$ — the route to [[Def - Conditional Expectation|conditional expectation]].

**Illegal but tempting operations:**

> [!warning] 1. Interchanging the order of integration without integrability
> For *signed* $f$, "$\iint f\,dx\,dy=\iint f\,dy\,dx$" can be false — see [[Ex - Fubini fails without integrability]]. Always run Tonelli on $|f|$ first; only $\iint|f|<\infty$ licenses Fubini.

> [!warning] 2. Applying Fubini–Tonelli without $\sigma$-finiteness
> Tonelli needs *both* measures $\sigma$-finite; counting measure on an uncountable space breaks it, and the iterated integrals diverge — see [[Ex - The diagonal has product measure zero]].

> [!warning] 3. Assuming $\nu\ll\mu$ gives a density without $\sigma$-finiteness
> [[Thm - Radon-Nikodym Theorem|Radon–Nikodym]] needs $\sigma$-finiteness; $\lambda\ll\#$ on $[0,1]$ holds yet $\lambda$ has no density — [[Ex - Radon-Nikodym fails without σ-finiteness]].

> [!warning] 4. Expecting a strong $L^1$ bound on the maximal function
> $f^*\notin L^1$ — only the *weak-type* maximal inequality holds, and it is enough; see [[Ex - The maximal function is not integrable]].

---

# Problem-Solving Strategy

The problems split by the chapter's three themes.

For **product-and-Fubini** problems, the first question is always integrability. To *evaluate* a double integral, reduce it to an iterated one — but for a signed integrand, run [[Thm - Fubini-Tonelli Theorem|Tonelli]] on $|f|$ first, and only if $\iint|f|<\infty$ apply Fubini to interchange. To compute a *product measure* of a region, write it as $\int\mathbf{1}_E\,d(\mu_1\otimes\mu_2)$ and iterate — slicing one way versus the other often yields two formulas for the same number (this is the layer-cake identity, and the squaring trick for the Gaussian integral). To prove *two measures equal*, find a generating $\pi$-system on which they agree and invoke [[Thm - Dynkin's π-λ Theorem|Dynkin]]; never argue set-by-set. Throughout, watch the $\sigma$-finiteness hypothesis — it is what makes uniqueness and Fubini valid.

For **differentiation** problems, the target is an a.e.-limit and the method is fixed: prove it on a dense easy class (continuous functions, where averaging is an $\varepsilon$–$\delta$ triviality), then for a general $f$ split $f=g+(f-g)$ with $g$ a good approximation and bound the exceptional set of $f-g$ by the [[Def - Hardy-Littlewood Maximal Function|maximal inequality]] plus Markov. The maximal inequality is itself proved by a covering argument — disjointify a cover of the level set, pay a dimensional constant for the dilation. This dense-class-plus-maximal-inequality architecture is not specific to the differentiation theorem; it recurs for martingale and ergodic convergence.

For **Radon–Nikodym** problems, the recognitions are: is $\nu\ll\mu$ (check "$\mu$-null $\Rightarrow\nu$-null")? are both $\sigma$-finite? If so, the density $\mathrm{d}\nu/\mathrm{d}\mu$ exists. The most important application is *constructive*: whenever an object is pinned down by "measurable with respect to $\mathcal{G}$, and has the same integral as $X$ over every $\mathcal{G}$-set," it is the Radon–Nikodym derivative of $\int_\cdot X\,d\mathbb{P}$ on $\mathcal{G}$ — i.e. a [[Def - Conditional Expectation|conditional expectation]]. To handle a *signed* $\nu$, [[Thm - Hahn and Jordan Decomposition|Jordan-decompose]] first. To decide whether $\nu$ has a density at all, test for [[Def - Mutual Singularity|singular]] parts — atoms, or mass on a $\mu$-null set, are the obstruction.

---

# Most Reusable Properties

- **[[Thm - Dynkin's π-λ Theorem|Dynkin's π–λ theorem]]**: agree on a generating $\pi$-system $\Rightarrow$ agree on the $\sigma$-algebra. The induction principle for generated $\sigma$-algebras and the universal route to *measure uniqueness*. Typical use: prove two measures (a law and a candidate, a product measure and a construction) coincide by checking them on rectangles, rays, or cylinder sets.

- **[[Thm - Fubini-Tonelli Theorem|Fubini–Tonelli]]**: double integral $=$ iterated integral. The workhorse of multivariable integration. Typical use: evaluate or estimate a double integral; prove the layer-cake formula; compute $\mathbb{E}[XY]$ for [[Def - Independence|independent]] variables; swap a sum and an integral. Always paired with the discipline "Tonelli on $|f|$, then Fubini."

- **The [[Def - Hardy-Littlewood Maximal Function|maximal inequality]]**: $\lambda(f^*>a)\le\frac{C}{a}\|f\|_1$. The device that bounds the exceptional set in a.e.-convergence theorems. Typical use: in any "prove a limit exists a.e." problem, control the bad set of a small perturbation by the maximal inequality.

- **[[Thm - Radon-Nikodym Theorem|Radon–Nikodym theorem]]**: $\nu\ll\mu\Rightarrow\nu=f\mu$. The theorem that turns a *relationship between measures* into a *function*. Typical use: construct [[Def - Conditional Expectation|conditional expectation]], define probability densities and likelihood ratios, perform a change of measure.

- **[[Thm - Hahn and Jordan Decomposition|Jordan decomposition]]**: every signed measure is $\alpha^+-\alpha^-$ with $\alpha^\pm$ singular. Typical use: reduce any signed-measure question to two positive-measure questions; define the total-variation norm and distance.

---

# Bridges

1. **To probability theory.** The [[Thm - Product Measure|product measure]] is the law of an *independent* pair; [[Def - Independence|independence]] of random variables is precisely "joint law $=$ product of marginals," and [[Thm - Fubini-Tonelli Theorem|Fubini]] computes expectations of functions of independent variables. [[Thm - Dynkin's π-λ Theorem|Dynkin's theorem]] is the everyday tool of probability — it shows a law is determined by its [[Def - Distribution Function|distribution function]], that independence need only be checked on $\pi$-systems, and that finite-dimensional distributions determine a process. Above all, [[Thm - Radon-Nikodym Theorem|Radon–Nikodym]] *constructs* [[Def - Conditional Expectation|conditional expectation]] — the central object of [[Advanced Probability III — Conditional Expectation|Advanced Probability]] — and the [[Thm - Lebesgue Differentiation Theorem|differentiation theorem]]'s dense-class + maximal-inequality template is the blueprint for the [[Thm - Almost Sure Martingale Convergence|martingale convergence theorem]] (with [[Thm - Doob's Maximal Inequality|Doob's]] maximal inequality).

2. **To harmonic analysis.** The [[Def - Hardy-Littlewood Maximal Function|maximal function]] and its weak inequality are the cornerstone — the prototype of Calderón–Zygmund theory, interpolation, and the boundedness of singular integrals. The Vitali covering lemma is the basic geometric tool.

3. **To functional analysis.** The space of finite signed measures, with the total-variation norm from the [[Thm - Hahn and Jordan Decomposition|Jordan decomposition]], is a Banach space — and the Riesz representation theorem identifies it as the dual of $C(X)$. The Radon–Nikodym theorem has an operator-theoretic proof via $L^2$ projection (von Neumann), tying it to [[Ex - The Cauchy-Schwarz inequality and L2 geometry|Hilbert-space geometry]].

4. **To the rest of measure theory.** Every "$\sigma$-finite" hypothesis in this chapter traces back to [[Def - σ-Finite Measure|§1.2]]; every limit interchange in the Fubini and Radon–Nikodym proofs is an [[Thm - Monotone Convergence Theorem|MCT]]; the chapter is the calculus erected on the measure (§1) and integral (§2) built before.

---

# Insights

**The unifying tool of §3 is Dynkin's $\pi$–$\lambda$ theorem — the induction principle that finally tames the [[Def - Generated σ-Algebra|non-constructive]] generated $\sigma$-algebra.** One cannot build $\sigma(\mathcal{P})$ explicitly, so one cannot induct up to it directly. But [[Thm - Dynkin's π-λ Theorem|Dynkin]] provides a *surrogate induction*: a property that (i) holds on a $\pi$-system $\mathcal{P}$ and (ii) is preserved by the $\lambda$-system operations (proper differences, increasing unions) automatically holds on all of $\sigma(\mathcal{P})$. The $\lambda$-system axioms are precisely the closure properties of "the set of $A$ where a *finitely-additive* identity persists" — which is why "two measures agree" and "the slice-integral is measurable" are $\lambda$-system statements. Every measurability and uniqueness fact in product-measure theory, and the determination of laws by distribution functions in probability, is this one theorem.

**The deepest architectural pattern of §4.1 is "dense class + maximal inequality," and it is the universal recipe for proving an almost-everywhere limit.** On a dense, well-behaved class (continuous functions) the limit is an $\varepsilon$–$\delta$ triviality. For a general $f$, write $f=g+(f-g)$ with $g$ in the dense class and $f-g$ small in norm; the error is then controlled by a *maximal function* — the supremum of all the relevant quantities — and the *maximal inequality* converts "small norm" into "small exceptional set." This precise template proves the [[Thm - Lebesgue Differentiation Theorem|Lebesgue differentiation theorem]], the [[Thm - Almost Sure Martingale Convergence|martingale convergence theorem]] (Doob's maximal inequality), and the pointwise ergodic theorem (the ergodic maximal inequality). The maximal function is *not* bounded on $L^1$ — and crucially does not need to be: a.e.-convergence consumes only a *weak* (level-set) bound, never a norm bound.

**Radon–Nikodym is the theorem that converts a *relationship between measures* into a *function* — and that conversion is what makes probability density functions, likelihood ratios, and conditional expectation possible.** Two measures can be related in two opposite ways: [[Def - Absolute Continuity and Density|absolutely continuous]] ($\nu$ lives wherever $\mu$ does, has a density) or [[Def - Mutual Singularity|mutually singular]] ($\nu$ and $\mu$ live on disjoint sets, no density). The [[Thm - Radon-Nikodym Theorem|Lebesgue decomposition]] says these are not just two cases but the two *canonical components*: every measure splits uniquely into an absolutely continuous part (with a density) and a singular part. The density $\mathrm{d}\nu/\mathrm{d}\mu$ is obtained, à la [[Thm - Hahn and Jordan Decomposition|Hahn]], by *maximising a sub-density* — the largest function that never overshoots $\nu$ — and whatever mass that maximal density fails to capture is provably singular. The whole construction needs $\sigma$-finiteness, and genuinely fails without it.

**The chapter's measure-decomposition theme — Hahn, Jordan, Lebesgue — is a single idea: a complicated measure is canonically a sum of pure, mutually-disjoint pieces.** A [[Def - Signed Measure|signed measure]] is a positive piece minus a negative piece on disjoint sets (Jordan); a measure is an absolutely-continuous piece plus a singular piece (Lebesgue); and one can iterate the singular part into atomic plus singular-continuous. Each decomposition is *unique*, each is obtained by an extremal construction ("most negative set," "largest sub-density"), and each reduces a hard object to well-understood components. This "decompose into pure parts" philosophy — the spectral theorem of measure theory — is what lets one *classify* measures and distributions, and it is the structural backbone on which conditional expectation, the total-variation metric, and the theory of distribution types are built.
