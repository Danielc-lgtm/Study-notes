---
type: topic
subject: advanced-probability
chapter: "2.1-2.3"
title: "Advanced Probability II — Modes of Convergence and the Limit Theorems"
tags: [probability, advanced-probability]
---

# Notation Registry

- $(X_n),X$ — random variables; $S_n=X_1+\cdots+X_n$; $\mu=\mathbb{E}X_1$, $\sigma^2=\mathrm{Var}(X_1)$
- $\xrightarrow{\text{a.s.}}$, $\xrightarrow{\mathbb{P}}$, $\xrightarrow{L^p}$, $\xrightarrow{d}$ — the four [[Def - Modes of Convergence|modes of convergence]]
- "UI" — [[Def - Uniform Integrability|uniformly integrable]]
- $\mu_n\Rightarrow\mu$ — [[Def - Weak Convergence|weak convergence]] of measures; $C_b$ — bounded continuous functions
- **tight** — $\forall\varepsilon\,\exists K$ compact, $\sup_n\mu_n(K^c)\le\varepsilon$
- $\varphi_X(t)=\mathbb{E}[e^{itX}]$ — the [[Def - Characteristic Function|characteristic function]]
- $N(m,\sigma^2)$ — Gaussian law; $\Phi$ — standard normal distribution function; $e^{-t^2/2}$ — its characteristic function
- $F_X$ — distribution function; $\xrightarrow{d}$ tested via $F_{X_n}(t)\to F_X(t)$ at continuity points

---

# Motivation

[[Advanced Probability I — Probability Spaces and Random Variables|Advanced Probability I]] built the objects; this chapter studies their *asymptotics* — what happens to $X_1+\cdots+X_n$ as $n\to\infty$. Two questions organise it.

*In what sense do random variables converge?* There is no single answer: a.s., in probability, in $L^p$, in distribution are four genuinely different [[Def - Modes of Convergence|modes]], forming a strict hierarchy. Knowing which mode a theorem delivers, which it needs, and which bridge — [[Def - Uniform Integrability|uniform integrability]], a dominating function, a subsequence — closes a gap is the organising discipline.

*What are the limit theorems?* Three landmark results on the sum $S_n$ of i.i.d. variables. The [[Thm - Weak Law of Large Numbers|weak]] and [[Thm - Strong Law of Large Numbers|strong laws of large numbers]] say the average $S_n/n$ converges to the mean $\mu$ — in probability, resp. almost surely; averaging destroys randomness. The [[Thm - Central Limit Theorem|central limit theorem]] describes the fluctuation the law of large numbers discards: $\frac{S_n-n\mu}{\sigma\sqrt n}$ converges *in distribution* to a **Gaussian**, regardless of the distribution of the summands — universality.

The CLT is a [[Def - Weak Convergence|weak-convergence]] statement, so the chapter develops the apparatus of weak convergence: [[Thm - Prokhorov's Theorem|Prokhorov's theorem]] (tightness $=$ compactness), [[Def - Characteristic Function|characteristic functions]] (Fourier transforms of laws, turning the convolution of independent sums into a product), and [[Thm - Lévy's Continuity Theorem|Lévy's continuity theorem]] (weak convergence $\iff$ pointwise convergence of characteristic functions) — the machine that makes the CLT a one-page Taylor expansion.

---

# Concept Map

## §2.1 Modes of Convergence and Uniform Integrability

- **[[Def - Modes of Convergence]]**
	- Four modes: almost sure, in probability ($=$ in measure), in $L^p$, in distribution ($=$ weak convergence of laws). Strict hierarchy: a.s.$\Rightarrow\mathbb{P}\Rightarrow d$, $L^p\Rightarrow\mathbb{P}$; a.s. and $L^p$ incomparable; no converse holds. Partial converses via subsequences, UI, or a constant limit.
- **[[Def - Uniform Integrability]]**
	- $\sup_i\mathbb{E}[|X_i|\mathbf{1}_{|X_i|>M}]\to0$ — the tail mass is uniformly negligible. The exact condition (with convergence in probability) for $L^1$-convergence ([[Thm - Vitali Convergence Theorem|Vitali]]). Supplied by domination, or $L^p$-boundedness for $p>1$; *not* by $L^1$-boundedness.

> [!note] Exercise Index — §2.1
> [[Exercise Index - §2.1 Modes of Convergence]]

## §2.2 Laws of Large Numbers

- **[[Thm - Weak Law of Large Numbers]]**
	- $S_n/n\xrightarrow{\mathbb{P}}\mu$ for identically distributed, uncorrelated, finite-variance summands. One-line proof: averaging divides variance by $n$, [[Ex - Markov's inequality|Chebyshev]] turns vanishing variance into concentration.
- **[[Thm - Strong Law of Large Numbers]]**
	- $S_n/n\xrightarrow{\text{a.s.}}\mu$ for i.i.d. summands with $\mathbb{E}|X_1|<\infty$ — the rigorous law of averages. The [[Thm - Kolmogorov 0-1 Law|0–1 law]] makes the limit a constant; the [[Def - Martingale|backward-martingale]] structure identifies it as $\mu$. An elementary fourth-moment proof exists.

> [!note] Exercise Index — §2.2
> [[Exercise Index - §2.2 Laws of Large Numbers]]

## §2.3 Weak Convergence and the Central Limit Theorem

- **[[Def - Weak Convergence]]**
	- $\mu_n\Rightarrow\mu$: $\int f\,d\mu_n\to\int f\,d\mu$ for all $f\in C_b$ — convergence of *laws*, tested against continuous observables. Equivalent forms: Portmanteau, distribution functions at continuity points. *Tightness* — no escape of mass — is the companion compactness notion.
- **[[Def - Characteristic Function]]**
	- $\varphi_X(t)=\mathbb{E}[e^{itX}]$ — the Fourier transform of the law. Always defined, determines the law, turns the convolution of independent sums into a product, encodes moments as derivatives at $0$. The Gaussian is self-dual ($\varphi=e^{-t^2/2}$).
- **[[Thm - Prokhorov's Theorem]]**
	- Tightness $\Leftrightarrow$ relative weak compactness — the Bolzano–Weierstrass of probability measures. Proved by Helly selection (diagonalise distribution functions) plus tightness (no mass leaks).
- **[[Thm - Lévy's Continuity Theorem]]**
	- $X_n\xrightarrow{d}X\iff\varphi_{X_n}\to\varphi_X$ pointwise (with the limit continuous at $0$). Reduces weak convergence to a pointwise computation; the bridge from characteristic functions back to probability.
- **[[Thm - Central Limit Theorem]]**
	- $\frac{S_n-n\mu}{\sigma\sqrt n}\xrightarrow{d}N(0,1)$ for i.i.d. finite-variance summands — the Gaussian as universal attractor. Proof: factor $\varphi$ by independence, Taylor-expand to second order, $(1-\frac{t^2}{2n})^n\to e^{-t^2/2}$, Lévy.

> [!note] Exercise Index — §2.3
> [[Exercise Index - §2.3 Weak Convergence and the CLT]]

---

# Sources and Targets

**Targets — What do we prove?** (1) *Convergence in a specified mode* — and the implications between modes. (2) *Laws of large numbers* — averages converge to means, in probability or almost surely. (3) *Distributional limits* — normalised sums converge weakly to a Gaussian (or Poisson, or stable) law. (4) *Existence of a weak limit* — via tightness and [[Thm - Prokhorov's Theorem|Prokhorov]]. (5) *Convergence of expectations*, $\lim\mathbb{E}X_n=\mathbb{E}X$ — via [[Def - Uniform Integrability|uniform integrability]].

**Sources — What do we leverage?** *Finite variance* routes to [[Ex - Markov's inequality|Chebyshev]] and the [[Thm - Weak Law of Large Numbers|weak law]] (and supplies UI). *I.i.d. structure* with a finite mean routes to the [[Thm - Strong Law of Large Numbers|strong law]]; with a finite variance, to the [[Thm - Central Limit Theorem|CLT]]. *A moment bound* routes to *tightness* (via Markov) and to UI. *Uniform integrability* routes to the upgrade probability $\to L^1$. *Independence* makes [[Def - Characteristic Function|characteristic functions]] multiply — the route to the CLT via [[Thm - Lévy's Continuity Theorem|Lévy]]. Recognising which structural hypothesis is present, and engineering the missing one (UI, tightness, a subsequence), is the recurring skill.

---

# Legal Operations

1. **Place the convergence in the hierarchy.** Identify which of the four [[Def - Modes of Convergence|modes]] a hypothesis gives and a goal needs; the implications a.s.$\Rightarrow\mathbb{P}\Rightarrow d$ and $L^p\Rightarrow\mathbb{P}$ are free, the rest need a bridge.

2. **Bridge with uniform integrability.** To upgrade convergence in probability to $L^1$ (hence $\mathbb{E}X_n\to\mathbb{E}X$), verify [[Def - Uniform Integrability|uniform integrability]] — by domination, or $L^p$-boundedness for $p>1$ — and invoke [[Thm - Vitali Convergence Theorem|Vitali]].

3. **Extract an a.s.-convergent subsequence.** From convergence in probability, choose a rapidly convergent subsequence and apply [[Thm - Borel-Cantelli Lemmas|Borel–Cantelli]] — the route from $\mathbb{P}$ to a.s. (for a subsequence).

4. **Average to kill variance.** For a sample mean, $\mathrm{Var}(S_n/n)=\sigma^2/n\to0$ (uncorrelated summands); [[Ex - Markov's inequality|Chebyshev]] converts this to the [[Thm - Weak Law of Large Numbers|weak law]].

5. **Sum a moment bound.** To get a.s. convergence, bound $\mathbb{E}[(\text{error})^{2k}]$ and check $\sum_n$ converges; MCT or Borel–Cantelli then gives the a.s. limit ([[Ex - The strong law via fourth moments|fourth-moment SLLN]]).

6. **Pass to characteristic functions.** Replace a law by its [[Def - Characteristic Function|characteristic function]]; independence makes them multiply, moments are derivatives at $0$, and [[Thm - Lévy's Continuity Theorem|Lévy]] converts pointwise convergence of $\varphi$ back to weak convergence — the CLT route.

7. **Establish tightness, extract a limit.** Bound a moment $\Rightarrow$ ([[Ex - Markov's inequality|Markov]]) tightness $\Rightarrow$ ([[Thm - Prokhorov's Theorem|Prokhorov]]) a weakly convergent subsequence; a uniqueness argument upgrades to full convergence.

8. **Recognise a sample mean.** Many estimators are $\frac1n\sum f(\cdot)$ of i.i.d. terms — apply the SLLN (consistency) and CLT (root-$n$ error) directly.

**Illegal but tempting operations:**

> [!warning] 1. Inferring $\mathbb{E}X_n\to\mathbb{E}X$ from a.s. or in-probability convergence
> Mass can escape — $n\mathbf{1}_{[0,1/n]}\to0$ a.s. but $\mathbb{E}=1$. One needs [[Def - Uniform Integrability|uniform integrability]] (or domination); [[Ex - Uniform integrability upgrades convergence|L¹-boundedness is not enough]].

> [!warning] 2. Treating convergence in distribution as convergence of the variables
> $X_n\xrightarrow{d}X$ constrains only the *laws* — the variables may be unrelated, even independent. The upgrade to convergence in probability holds *only when the limit is constant* ([[Ex - Convergence in distribution to a constant]]).

> [!warning] 3. Applying the CLT without finite variance
> The $\sqrt n$ scaling and Gaussian limit need $\sigma^2<\infty$. Heavy-tailed summands have a different scaling ($n^{1/\alpha}$) and a *stable*, non-Gaussian limit.

> [!warning] 4. Expecting a weak limit without tightness
> $\delta_n$ has no weak limit — mass escapes to infinity. [[Thm - Prokhorov's Theorem|Prokhorov]] needs tightness; a moment bound is the usual way to secure it.

---

# Problem-Solving Strategy

Problems are about *convergence* — establishing it, upgrading it, or identifying the limit.

To **establish a law of large numbers**, ask which mode is wanted. For *in probability* (the weak law), the route is fixed and short: compute $\mathrm{Var}(S_n/n)=\sigma^2/n$ (variance is additive for uncorrelated summands) and apply [[Ex - Markov's inequality|Chebyshev]] — averaging kills variance, Chebyshev converts that to concentration. For *almost surely* (the strong law), more is needed: either bound a higher moment and exploit summability ($\sum n^{-2}<\infty$, the [[Ex - The strong law via fourth moments|fourth-moment proof]]), or invoke the [[Thm - Kolmogorov 0-1 Law|0–1 law]] (limit is constant) and the [[Def - Martingale|backward-martingale]] structure (limit is $\mu$).

To **upgrade a convergence** — from in-probability to $L^1$, or to a.s. — name the gap and the bridge. In-probability to $L^1$: check [[Def - Uniform Integrability|uniform integrability]] and apply [[Thm - Vitali Convergence Theorem|Vitali]]; UI is verified by domination or $L^p$-boundedness ($p>1$), never by an $L^1$ bound alone. In-probability to a.s.: extract a fast subsequence and use [[Thm - Borel-Cantelli Lemmas|Borel–Cantelli]] — only a *subsequence* can be salvaged.

To **prove a distributional limit** (a CLT-type statement), the characteristic-function method is canonical: write the law's [[Def - Characteristic Function|characteristic function]], use independence to factor it into a product, Taylor-expand each factor using the moment property (finite variance gives a second-order expansion), recognise the exponential limit, and invoke [[Thm - Lévy's Continuity Theorem|Lévy's continuity theorem]] to convert pointwise convergence of $\varphi$ into weak convergence. When the limit must instead be *constructed* rather than guessed, the route is tightness: bound a moment to get tightness (via [[Ex - Markov's inequality|Markov]]), apply [[Thm - Prokhorov's Theorem|Prokhorov]] for a convergent subsequence, then show all subsequential limits coincide (again via characteristic functions) to obtain full convergence.

A recurring meta-move: many concrete quantities — estimators, frequencies, empirical averages — are *sample means of i.i.d. terms* in disguise. Spotting this ([[Ex - Monte Carlo integration|Monte Carlo]], [[Ex - Borel's normal number theorem|normal numbers]]) lets the SLLN and CLT apply verbatim, often turning a non-probabilistic problem into a one-line corollary.

---

# Most Reusable Properties

- **[[Thm - Strong Law of Large Numbers|The strong law of large numbers]]**: $S_n/n\to\mu$ a.s. The rigorous law of averages — it makes "probability $=$ long-run frequency" a theorem, underlies the consistency of every statistical estimator, [[Ex - Monte Carlo integration|Monte Carlo]], and (as the i.i.d. case) the ergodic theorem. Typical use: recognise a quantity as a sample mean, conclude a.s. convergence to its expectation.

- **[[Thm - Central Limit Theorem|The central limit theorem]]**: $\frac{S_n-n\mu}{\sigma\sqrt n}\xrightarrow{d}N(0,1)$. The universality of the Gaussian — the fluctuation of any sum of small independent pieces is Gaussian. Typical use: error bars, confidence intervals, the $\sqrt n$ scaling of statistical and Monte Carlo error.

- **[[Ex - Markov's inequality|Chebyshev's inequality]]**: $\mathbb{P}(|X-\mathbb{E}X|>\lambda)\le\mathrm{Var}(X)/\lambda^2$. The bridge from a variance bound to a probability bound — it proves the [[Thm - Weak Law of Large Numbers|weak law]] in one line and yields tightness from a moment bound.

- **[[Def - Uniform Integrability|Uniform integrability]]**: the exact condition upgrading convergence in probability to $L^1$. Typical use: justify $\lim\mathbb{E}X_n=\mathbb{E}\lim X_n$ when no dominating function is at hand; the criterion for $L^1$-convergence of [[Def - Martingale|martingales]].

- **[[Def - Characteristic Function|The characteristic function]]** with [[Thm - Lévy's Continuity Theorem|Lévy's continuity theorem]]: independence $\to$ product, moments $\to$ derivatives, weak convergence $\iff$ pointwise convergence of $\varphi$. Typical use: prove any distributional limit theorem by a Taylor expansion.

---

# Bridges

1. **To measure theory.** The four [[Def - Modes of Convergence|modes]] are the [[Measure Theory II — §2 Integration|measure-theory modes]] (a.e., in measure, $L^p$) plus the genuinely new *weak* convergence; [[Def - Uniform Integrability|uniform integrability]] is [[Def - Absolute Continuity and Density|uniformly absolutely continuous integrals]], and the upgrade probability$\to L^1$ is the [[Thm - Vitali Convergence Theorem|Vitali theorem]]. [[Def - Characteristic Function|Characteristic functions]] are the Fourier transform of [[Measure Theory I — §1 Measure Spaces|measures]]; [[Thm - Prokhorov's Theorem|Prokhorov]] runs on [[Def - Distribution Function|distribution functions]] and Helly selection.

2. **To Advanced Probability I.** The [[Thm - Kolmogorov 0-1 Law|0–1 law]] makes the SLLN's limit constant; [[Thm - Borel-Cantelli Lemmas|Borel–Cantelli]] is the step from summable error bounds to a.s. convergence; [[Def - Independence|independence]] and the [[Ex - Independence and the factorisation of expectation|convolution]] structure of sums are what characteristic functions exploit.

3. **To martingales and stochastic processes.** [[Def - Uniform Integrability|Uniform integrability]] is the criterion for $L^1$-convergence of [[Def - Martingale|martingales]] ([[Advanced Probability IV — Martingales in Discrete Time|AP IV]]); the [[Thm - Strong Law of Large Numbers|SLLN]] is proved by [[Def - Martingale|backward martingales]]; the functional CLT (Donsker) builds Brownian motion as a weak limit of rescaled random walks, with [[Thm - Prokhorov's Theorem|Prokhorov]] supplying tightness in path space.

4. **To statistics and information theory.** The SLLN is the *consistency* of estimators, the CLT their *asymptotic normality* — the foundations of inference. [[Thm - Cramér's Theorem|Large-deviation]] theory refines the laws of large numbers by quantifying the exponentially small probability of an atypical average — the bridge to entropy and the user's algorithmic-thermodynamics interests.

---

# Insights

**The four modes of convergence form a strict hierarchy, and almost every theorem of asymptotic probability is, in part, a statement about *which mode*.** A.s. is strongest, distribution weakest; $L^p$ and a.s. are incomparable; no converse holds. The [[Thm - Strong Law of Large Numbers|SLLN]] *delivers* a.s., the [[Thm - Weak Law of Large Numbers|WLLN]] only in-probability, the [[Thm - Central Limit Theorem|CLT]] only in-distribution — and the gaps between modes are bridged by named devices: [[Def - Uniform Integrability|uniform integrability]] (probability $\to L^1$, the [[Thm - Vitali Convergence Theorem|Vitali]] bridge), a fast subsequence (probability $\to$ a.s., the [[Thm - Borel-Cantelli Lemmas|Borel–Cantelli]] bridge), a constant limit (distribution $\to$ probability). Fluency in the chapter *is* fluency in this map: what a hypothesis gives, what a conclusion needs, what closes the gap.

**The laws of large numbers and the central limit theorem are two halves of one picture — the decomposition $S_n=n\mu+\sigma\sqrt n\cdot(\text{Gaussian})+o(\sqrt n)$.** The law of large numbers extracts the leading term: $S_n/n\to\mu$, the average has no fluctuation in the limit. The CLT extracts the *next* term: the fluctuation $S_n-n\mu$ lives at scale $\sqrt n$, and once rescaled it is Gaussian. They are not competing theorems but successive orders of an asymptotic expansion — the first about the *mean*, the second about the *variance-scale fluctuation*, with [[Thm - Cramér's Theorem|large deviations]] supplying the next order (the exponentially rare excursions).

**Universality is the deepest content of the CLT: the Gaussian limit depends on the summands' distribution *only through its mean and variance*.** Centre and rescale, and the third and higher moments wash out under the $1/\sqrt n$ scaling — every finite-variance distribution flows to the same Gaussian fixed point. The mechanism is visible in the characteristic-function proof: independence makes $\varphi$ a product $\varphi_X(t/\sqrt n)^n$, finite variance gives the second-order expansion $\varphi_X(s)=1-s^2/2+o(s^2)$, and *only the quadratic coefficient survives* the limit $(1-\frac{t^2}{2n})^n\to e^{-t^2/2}$. The Gaussian is the universal attractor because it is the law whose characteristic function has *exactly quadratic* logarithm — the fixed point of "add and rescale." This is why the bell curve is ubiquitous, and it is a probabilistic instance of the renormalisation-group philosophy: microscopic detail is irrelevant; only a few coarse parameters determine the macroscopic limit.

**Weak convergence is the right notion of "convergence of laws," and tightness is its compactness — together they form the analyst's toolkit for probability.** Weak convergence tests against [[Def - Weak Convergence|continuous observables]], ignoring the behaviour on measure-zero boundaries, so $\delta_{1/n}\Rightarrow\delta_0$ as it should. [[Thm - Prokhorov's Theorem|Prokhorov's theorem]] makes *tightness* — uniformly, no mass escapes to infinity — equivalent to relative compactness, the Bolzano–Weierstrass of measures. And [[Def - Characteristic Function|characteristic functions]] *metrise* weak convergence ([[Thm - Lévy's Continuity Theorem|Lévy]]), converting it into pointwise convergence of an ordinary function. The recurring strategy — *bound a moment $\to$ tightness $\to$ subsequential limit $\to$ uniqueness $\to$ full convergence* — is how every weak limit, from the CLT to the construction of Brownian motion, is established. Tightness is to weak convergence what [[Def - Uniform Integrability|uniform integrability]] is to $L^1$-convergence: both forbid an escape (of probability mass, resp. of expected mass), and both are the precise condition for compactness.
