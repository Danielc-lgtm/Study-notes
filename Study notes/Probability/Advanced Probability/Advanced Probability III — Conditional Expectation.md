---
type: topic
subject: advanced-probability
chapter: "3.1-3.2"
title: "Advanced Probability III — Conditional Expectation"
tags: [probability, advanced-probability]
---

# Notation Registry

- $(\Omega,\mathcal{F},\mathbb{P})$ — a [[Def - Probability Space|probability space]]; $\mathcal{H}\subseteq\mathcal{G}\subseteq\mathcal{F}$ — sub-$\sigma$-algebras
- $\mathbb{E}[X\mid\mathcal{G}]$ — [[Def - Conditional Expectation|conditional expectation]] of $X$ given $\mathcal{G}$ (a $\mathcal{G}$-measurable random variable)
- $\mathbb{E}[X\mid Z]:=\mathbb{E}[X\mid\sigma(Z)]$; $\mathbb{E}[X\mid Z=z]=h(z)$ for the Borel $h$ with $\mathbb{E}[X\mid Z]=h(Z)$
- $\mathbb{P}(B\mid\mathcal{G})=\mathbb{E}[\mathbf{1}_B\mid\mathcal{G}]$ — conditional probability
- $\mathrm{Var}(X\mid\mathcal{G})=\mathbb{E}[X^2\mid\mathcal{G}]-\mathbb{E}[X\mid\mathcal{G}]^2$ — conditional variance
- $f_{V\mid U}=f_{U,V}/f_U$ — the [[Def - Conditional Density|conditional density]]
- $L^2(\mathcal{G})=L^2(\Omega,\mathcal{G},\mathbb{P})$ — the $\mathcal{G}$-measurable square-integrable functions

---

# Motivation

The most subtle and most important construction of advanced probability. Elementary conditional expectation $\mathbb{E}[X\mid B]=\mathbb{E}[X\mathbf{1}_B]/\mathbb{P}(B)$ conditions on a *single positive-probability event* and returns a *number*. The advanced notion conditions on an entire *sub-$\sigma$-algebra* $\mathcal{G}$ — a whole body of information — and returns a *random variable* $\mathbb{E}[X\mid\mathcal{G}]$: "$X$ with the randomness invisible to $\mathcal{G}$ averaged out, the randomness visible to $\mathcal{G}$ retained."

Why the generalisation matters. First, conditioning on a continuous variable $Y$ means conditioning on events $\{Y=y\}$ of probability *zero* — the elementary quotient is "$0/0$." The resolution is to *characterise* $\mathbb{E}[X\mid\mathcal{G}]$ by two properties — $\mathcal{G}$-measurability and the *averaging identity* $\mathbb{E}[\mathbb{E}[X\mid\mathcal{G}]\mathbf{1}_A]=\mathbb{E}[X\mathbf{1}_A]$ for $A\in\mathcal{G}$ — and *prove existence* by [[Thm - Radon-Nikodym Theorem|Radon–Nikodym]] or [[Thm - Conditional Expectation as L2 Projection|$L^2$-projection]]. Conditional expectation is *defined by its characterisation*, not a formula — which is exactly what lets it survive probability-zero conditioning.

Second, conditional expectation is the heart of dynamic probability: iterated along a [[Def - Filtration|filtration]] it *is* a [[Def - Martingale|martingale]] ([[Advanced Probability IV — Martingales in Discrete Time|AP IV]]); it is the best mean-square *predictor* (the regression function of statistics); and its calculus — linearity, the **tower property**, **taking out what is known**, conditional Jensen — is the working language of the whole subject.

---

# Concept Map

## §3.1 Conditional Expectation — Definition and Construction

- **[[Def - Conditional Expectation]]**
	- The random variable $\mathbb{E}[X\mid\mathcal{G}]$, characterised by: $\mathcal{G}$-measurable, and same $\mathcal{G}$-integrals as $X$. Generalises $\mathbb{E}[X\mid B]$ from one event to a $\sigma$-algebra; works for probability-zero conditioning because it is defined by a property, not a quotient. Discretely, the block-average.
- **[[Def - Conditional Density]]**
	- $f_{V\mid U}(v\mid u)=f_{U,V}(u,v)/f_U(u)$ — joint over marginal, the density analogue of $\mathbb{P}(A\mid B)$. Makes $\mathbb{E}[h(V)\mid U]$ a concrete integral; the posterior density of Bayesian inference.
- **[[Thm - Existence and Uniqueness of Conditional Expectation]]**
	- $\mathbb{E}[X\mid\mathcal{G}]$ exists (for $X\in L^1$) and is a.s. unique. Two constructions: [[Thm - Radon-Nikodym Theorem|Radon–Nikodym]] derivative on $\mathcal{G}$, or [[Thm - Conditional Expectation as L2 Projection|$L^2$-projection]]. Uniqueness: a $\mathcal{G}$-measurable function with all $\mathcal{G}$-integrals zero is zero.
- **[[Thm - Properties of Conditional Expectation]]**
	- Linearity, positivity, the **tower property**, **taking out what is known**, the independence rule, conditional convergence theorems, conditional Jensen and the $L^p$-contraction. All proved by "verify the two characterising properties, invoke uniqueness."

> [!note] Exercise Index — §3.1
> [[Exercise Index - §3.1 Definition and Construction]]

## §3.2 Computing Conditional Expectations

- **[[Thm - Conditional Expectation as L2 Projection]]**
	- For $X\in L^2$, $\mathbb{E}[X\mid\mathcal{G}]$ is the orthogonal projection of $X$ onto $L^2(\mathcal{G})$ — the best $\mathcal{G}$-measurable mean-square approximation. The averaging identity is orthogonality; the law of total variance is Pythagoras.

> [!note] Exercise Index — §3.2
> [[Exercise Index - §3.2 Computing Conditional Expectations]]

---

# Sources and Targets

**Targets — What do we prove?** (1) *Existence and uniqueness* of $\mathbb{E}[X\mid\mathcal{G}]$. (2) *Identities* — the tower property, taking out what is known, conditional Jensen — each a tool for the next computation. (3) *Explicit formulas* — the discrete block-average, the Gaussian linear regression, the conditional-density integral. (4) *Computations of an expectation* by conditioning on an auxiliary variable. (5) *Variance / prediction* statements — best-predictor, the law of total variance.

**Sources — What do we leverage?** *$X\in L^1$* (or $L^2$) is the basic hypothesis. The two *characterising properties* are the source of every proof: to identify a conditional expectation, exhibit a candidate and verify them. *Independence* of $X$ from $\mathcal{G}$ collapses $\mathbb{E}[X\mid\mathcal{G}]$ to $\mathbb{E}[X]$. *A joint density* routes to the conditional-density formula; *joint Gaussianity* routes to linear regression. *Nested $\sigma$-algebras* $\mathcal{H}\subseteq\mathcal{G}$ route to the tower property.

---

# Legal Operations

1. **Propose and verify.** To find $\mathbb{E}[X\mid\mathcal{G}]$, write down a $\mathcal{G}$-measurable candidate $Y$ and check the averaging identity $\mathbb{E}[Y\mathbf{1}_A]=\mathbb{E}[X\mathbf{1}_A]$ for $A\in\mathcal{G}$ (on a generating $\pi$-system suffices); [[Thm - Existence and Uniqueness of Conditional Expectation|uniqueness]] then forces $Y=\mathbb{E}[X\mid\mathcal{G}]$. *This is the only method.*

2. **Condition–compute–average.** To find a hard $\mathbb{E}[X]$, write $\mathbb{E}[X]=\mathbb{E}[\mathbb{E}[X\mid Z]]$ ([[Thm - Properties of Conditional Expectation|tower property]]); choose $Z$ so that $X$ given $Z$ has deterministic structure; compute the inner expectation; average.

3. **Take out what is known.** A $\mathcal{G}$-measurable factor $Z$ passes through: $\mathbb{E}[ZX\mid\mathcal{G}]=Z\,\mathbb{E}[X\mid\mathcal{G}]$ — known quantities behave as constants under $\mathbb{E}[\cdot\mid\mathcal{G}]$.

4. **Discard independent information.** If $X\perp\mathcal{G}$, $\mathbb{E}[X\mid\mathcal{G}]=\mathbb{E}[X]$; adding a $\sigma$-algebra independent of everything relevant does not change a conditional expectation.

5. **Freeze the known, average the independent.** For $\mathbb{E}[h(X,Y)\mid\mathcal{G}]$ with $X$ $\mathcal{G}$-measurable and $Y\perp\mathcal{G}$: treat $X$ as a parameter, average $Y$, substitute — $g(X)$ with $g(x)=\mathbb{E}[h(x,Y)]$.

6. **Project in $L^2$.** For $X\in L^2$, compute $\mathbb{E}[X\mid\mathcal{G}]$ as the [[Thm - Conditional Expectation as L2 Projection|orthogonal projection]] onto $L^2(\mathcal{G})$ — pin a candidate by making the residual orthogonal to $L^2(\mathcal{G})$.

7. **Integrate against the conditional density.** For jointly-continuous $(U,V)$, $\mathbb{E}[h(V)\mid U=u]=\int h(v)f_{V\mid U}(v\mid u)\,\mathrm{d}v$.

8. **Apply conditional Jensen.** For convex $\varphi$, $\mathbb{E}[\varphi(X)\mid\mathcal{G}]\ge\varphi(\mathbb{E}[X\mid\mathcal{G}])$ — chosen $\varphi$ gives the $L^p$-contraction, the variance decomposition, submartingale properties.

**Illegal but tempting operations:**

> [!warning] 1. Conditioning by the quotient on a probability-zero event
> $\mathbb{E}[X\mid Y=y]$ is *not* $\mathbb{E}[X\mathbf{1}_{Y=y}]/\mathbb{P}(Y=y)$ when $\mathbb{P}(Y=y)=0$. Conditional expectation is defined by its [[Def - Conditional Expectation|characterising properties]]; compute via the [[Def - Conditional Density|conditional density]] or by propose-and-verify.

> [!warning] 2. Treating $\mathbb{E}[X\mid\mathcal{G}]$ as a number
> It is a *random variable* — $\mathcal{G}$-measurable, defined only up to a.s. equality. Only $\mathbb{E}[X\mid\{\emptyset,\Omega\}]=\mathbb{E}[X]$ is a constant.

> [!warning] 3. Taking a non-$\mathcal{G}$-measurable factor "out"
> $\mathbb{E}[ZX\mid\mathcal{G}]=Z\mathbb{E}[X\mid\mathcal{G}]$ holds *only when $Z$ is $\mathcal{G}$-measurable*. For a general $Z$ the factor cannot be pulled out.

> [!warning] 4. Assuming conditional expectation is linear in the conditioning variable
> $\mathbb{E}[X\mid Y]$ is a general (often nonlinear) function of $Y$. It is *linear* only in special cases — notably [[Ex - The Gaussian conditional expectation|jointly Gaussian]] variables.

---

# Problem-Solving Strategy

Every problem here is either *identify a conditional expectation* or *use one to compute*.

To **identify $\mathbb{E}[X\mid\mathcal{G}]$**, there is exactly one method: *propose and verify*. Guess a $\mathcal{G}$-measurable candidate $Y$ — the structure of $\mathcal{G}$ usually dictates the form (constant on partition blocks; linear in a Gaussian conditioner; an integral against the conditional density) — then check the averaging identity $\mathbb{E}[Y\mathbf{1}_A]=\mathbb{E}[X\mathbf{1}_A]$, on a generating $\pi$-system if convenient. [[Thm - Existence and Uniqueness of Conditional Expectation|Uniqueness]] does the rest. For $X\in L^2$ the candidate can instead be pinned geometrically: $\mathbb{E}[X\mid\mathcal{G}]$ is the unique $\mathcal{G}$-measurable $Y$ making the residual $X-Y$ orthogonal to $L^2(\mathcal{G})$.

To **use conditional expectation in a computation**, the master device is *condition–compute–average*: $\mathbb{E}[X]=\mathbb{E}[\mathbb{E}[X\mid Z]]$, where $Z$ is chosen so that "$X$ given $Z$" is tractable (a random sum becomes a fixed sum, a two-stage experiment becomes one stage). Inside the inner expectation, the two conditional rules do the work: *take out what is known* (the $\mathcal{G}$-measurable parts act as constants) and *discard / average independent information* ($\mathbb{E}[Y\mid\mathcal{G}]=\mathbb{E}[Y]$ for $Y\perp\mathcal{G}$). Recognising which quantities are "known to $\mathcal{G}$" and which are "independent of $\mathcal{G}$" — freeze the first, average the second — is the central skill.

For **variance and prediction** questions, the $L^2$-projection picture is the right frame: $\mathbb{E}[X\mid\mathcal{G}]$ is the best $\mathcal{G}$-measurable predictor, the law of total variance is the Pythagorean split into explained and residual variance, and conditional Jensen (with the right convex $\varphi$) gives contractions and submartingale inequalities.

A recurring computation pattern: when conditioning preserves a distributional family — as with [[Ex - The Gaussian conditional expectation|jointly Gaussian]] variables, where the conditional law is again Gaussian with a linear mean — the conditional expectation collapses to a simple closed form, and one should *exploit the family structure* rather than integrate.

---

# Most Reusable Properties

- **The tower property**: $\mathbb{E}[\mathbb{E}[X\mid\mathcal{G}]\mid\mathcal{H}]=\mathbb{E}[X\mid\mathcal{H}]$ for $\mathcal{H}\subseteq\mathcal{G}$. The single most-used identity — it is the *definition* of a [[Def - Martingale|martingale]], the computational engine of *condition–compute–average*, and the link converting conditional identities to unconditional ones. Typical use: split a hard expectation into two stages.

- **Taking out what is known**: $\mathbb{E}[ZX\mid\mathcal{G}]=Z\,\mathbb{E}[X\mid\mathcal{G}]$ for $\mathcal{G}$-measurable $Z$. Known quantities are constants under conditioning. Typical use: simplify conditional expectations of products; the predictable-projection calculus of martingales.

- **The averaging identity / uniqueness**: $\mathbb{E}[Y\mathbf{1}_A]=\mathbb{E}[X\mathbf{1}_A]$ on $\mathcal{G}$ characterises $Y=\mathbb{E}[X\mid\mathcal{G}]$. Typical use: *every* identification of a conditional expectation — propose a candidate, verify, invoke uniqueness.

- **Conditional Jensen** and the **$L^2$-projection**: $\mathbb{E}[\varphi(X)\mid\mathcal{G}]\ge\varphi(\mathbb{E}[X\mid\mathcal{G}])$; $\mathbb{E}[X\mid\mathcal{G}]$ is the best $L^2$-predictor. Typical use: contractions ($\|\mathbb{E}[X\mid\mathcal{G}]\|_p\le\|X\|_p$), the law of total variance, making $|M_n|^p$ a submartingale.

- **The independence rule**: $X\perp\mathcal{G}\Rightarrow\mathbb{E}[X\mid\mathcal{G}]=\mathbb{E}[X]$. Typical use: discard irrelevant information; the key step in the [[Thm - Strong Law of Large Numbers|backward-martingale SLLN]].

---

# Bridges

1. **To martingale theory.** A [[Def - Martingale|martingale]] is conditional expectation iterated along a [[Def - Filtration|filtration]]: $\mathbb{E}[X_{n+1}\mid\mathcal{F}_n]=X_n$ is the tower property in motion. [[Advanced Probability IV — Martingales in Discrete Time|AP IV]] is entirely the dynamics of conditional expectation; conditional Jensen makes $|M_n|^p$ a submartingale, the input to [[Thm - Doob's Maximal Inequality|Doob's inequalities]], and the $L^p$-contraction gives the uniform integrability behind $L^1$-convergence.

2. **To measure theory.** Conditional expectation *is* a [[Thm - Radon-Nikodym Theorem|Radon–Nikodym derivative]] (of $X\,d\mathbb{P}$ restricted to $\mathcal{G}$) and *is* an [[Thm - Conditional Expectation as L2 Projection|orthogonal projection]] in the Hilbert space [[Def - Lp Spaces|$L^2$]]; its existence is one of these two theorems, its calculus the [[Thm - Monotone Convergence Theorem|convergence theorems]] conditionalised. The [[Ex - The σ-algebra generated by a function|Doob–Dynkin lemma]] is what makes $\mathbb{E}[X\mid Z]$ a function of $Z$.

3. **To statistics.** $\mathbb{E}[Y\mid X]$ is the *regression function* — the best predictor of $Y$ from $X$; the [[Ex - The Gaussian conditional expectation|Gaussian case]] is linear regression. The [[Ex - Conditional Jensen and the variance decomposition|law of total variance]] is ANOVA / $R^2$; Rao–Blackwellisation is conditioning on a sufficient statistic; the [[Def - Conditional Density|conditional density]] is the Bayesian posterior. The recursive projection picture is the Kalman filter.

4. **To information theory.** A sub-$\sigma$-algebra is a resolution of information; conditional expectation averages out the unresolved part. Conditional entropy $H(V\mid U)$ is built on the [[Def - Conditional Density|conditional density]] — a bridge to the user's algorithmic-information interests.

---

# Insights

**Conditional expectation is *defined by a characterisation, not a formula* — and this is precisely what lets it handle conditioning on probability-zero events.** The elementary $\mathbb{E}[X\mid B]=\mathbb{E}[X\mathbf{1}_B]/\mathbb{P}(B)$ breaks the instant $\mathbb{P}(B)=0$, as it must whenever one conditions on a continuous variable. The advanced notion sidesteps the quotient entirely: $\mathbb{E}[X\mid\mathcal{G}]$ is *whatever $\mathcal{G}$-measurable variable has the same $\mathcal{G}$-integrals as $X$* — a description, guaranteed to be realised by an [[Thm - Existence and Uniqueness of Conditional Expectation|existence theorem]] ([[Thm - Radon-Nikodym Theorem|Radon–Nikodym]] or [[Thm - Conditional Expectation as L2 Projection|$L^2$-projection]]) and pinned down by uniqueness. Every computation is then "propose a candidate, verify the two properties" — and the [[Def - Conditional Density|conditional density]] is simply the candidate-producing device in the jointly-continuous case. Defining an object by *what it does* rather than *how to build it* is a recurring mathematical move, and conditional expectation is its decisive probabilistic instance.

**Conditional expectation has three faces — a measure (Radon–Nikodym derivative), a geometry (orthogonal projection), and an information-average — and each illuminates a different part of the theory.** As a [[Thm - Radon-Nikodym Theorem|Radon–Nikodym derivative]] on $\mathcal{G}$, it exists for all of $L^1$ and connects to densities and change of measure. As an [[Thm - Conditional Expectation as L2 Projection|orthogonal projection]] onto $L^2(\mathcal{G})$, it is the best mean-square predictor, with the law of total variance as the Pythagorean theorem and the $L^p$-contraction as "projections shrink norms." As an *average over the information not in $\mathcal{G}$*, it is the block-average in the discrete picture and the intuition for the tower property. The same object, viewed three ways — and a problem becomes easy the moment one picks the right view.

**The tower property is the deepest structural fact, and it says that information forms a *consistent hierarchy*: a finer average, re-averaged coarsely, is the coarse average.** $\mathbb{E}[\mathbb{E}[X\mid\mathcal{G}]\mid\mathcal{H}]=\mathbb{E}[X\mid\mathcal{H}]$ for $\mathcal{H}\subseteq\mathcal{G}$ — the intermediate refinement is invisible to the coarser one. This is what makes conditional expectation *dynamically* coherent: as information accumulates along a [[Def - Filtration|filtration]], the successive conditional expectations form a [[Def - Martingale|martingale]], and the tower property *is* the martingale identity. It is also the computational workhorse — "condition on an auxiliary variable, compute, average back" — and the reason the law of large numbers can be proved by [[Thm - Strong Law of Large Numbers|backward martingales]]. Information that nests, averages consistently; that single principle organises all of dynamic probability.

**Conditioning is a *smoothing* operation — it never increases variance, never increases an $L^p$-norm, and replaces $X$ by its best predictor given partial information.** Conditional [[Thm - Jensen's Inequality|Jensen]] yields the $L^p$-contraction $\|\mathbb{E}[X\mid\mathcal{G}]\|_p\le\|X\|_p$; the [[Ex - Conditional Jensen and the variance decomposition|law of total variance]] shows $\mathrm{Var}(\mathbb{E}[X\mid\mathcal{G}])\le\mathrm{Var}(X)$, with the deficit being the "unexplained" residual variance. Intuitively, averaging out the randomness invisible to $\mathcal{G}$ can only *reduce* spread — and the more information $\mathcal{G}$ carries, the closer $\mathbb{E}[X\mid\mathcal{G}]$ is to $X$ itself, interpolating between the constant $\mathbb{E}[X]$ (no information) and $X$ (total information). This monotone "information $\to$ resolution" picture is why conditional expectation is the right model of prediction, of partial observation, and — iterated in time — of a fair game.
