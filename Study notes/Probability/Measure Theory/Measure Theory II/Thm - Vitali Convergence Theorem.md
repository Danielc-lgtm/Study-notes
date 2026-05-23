---
type: theorem
subject: measure-theory
prereqs:
  - "Def - Convergence in Measure"
  - "Def - Absolute Continuity and Density"
  - "Thm - Dominated Convergence Theorem"
  - "Thm - Egorov's Theorem"
tags: [analysis, measure-theory, probability]
---

# Notation

$(X,\mathcal{A},\mu)$ a measure space with $\mu(X)<\infty$; $f,f_n\in L^1(\mu)$. $f_n\xrightarrow{\mu}f$ — [[Def - Convergence in Measure|convergence in measure]].

---

# Motivation

The [[Thm - Dominated Convergence Theorem|DCT]] gives $L^1$-convergence under a *sufficient* but not necessary hypothesis: the existence of a dominating $g\in L^1$. Domination is convenient but crude — many $L^1$-convergent sequences have no integrable dominator. The Vitali convergence theorem replaces it with the **exactly right** hypothesis: on a finite-measure space, $f_n\to f$ in $L^1$ **if and only if** $f_n\to f$ in measure *and* the family $(f_n)$ is [[Def - Absolute Continuity and Density|uniformly integrable]]. This is a *characterisation* — necessary and sufficient — so it pinpoints precisely what controls $L^1$-convergence: convergence in measure handles "$f_n$ gets close to $f$," uniform integrability handles "no mass escapes."

---

# Sources and Targets

**Sources.** Hypotheses: $\mu(X)<\infty$, $f_n\xrightarrow{\mu}f$, $(f_n)$ uniformly integrable (UI). Source-broadenings for UI: a dominated family ($|f_n|\le g\in L^1$) is UI — so DCT is a *special case*; an $L^p$-bounded family ($p>1$) is UI; a family of [[Def - Conditional Expectation|conditional expectations]] $\{\mathbb{E}[Z\mid\mathcal{G}]\}$ of a fixed $Z\in L^1$ is UI — the fact that makes [[Thm - Almost Sure Martingale Convergence|martingales]] converge in $L^1$.

**Targets.** The equivalence is the master tool for upgrading weaker convergence to $L^1$: it converts a.s. or in-measure convergence into $L^1$ convergence given UI, and it is the precise criterion behind the [[Thm - Almost Sure Martingale Convergence|L¹ martingale convergence theorem]] (a martingale converges in $L^1$ iff it is UI).

---

# Statement

Let $\mu(X)<\infty$ and $f,f_n\in L^1(\mu)$. The following are equivalent:

1. $f_n\xrightarrow{\mu}f$ in measure, **and** $(f_n)_{n\in\mathbb{N}}$ has [[Def - Absolute Continuity and Density|uniformly absolutely continuous integrals]] (uniform integrability): $\forall\varepsilon>0\,\exists\delta>0$ such that $\mu(A)<\delta\Rightarrow\sup_n\int_A|f_n|\,d\mu<\varepsilon$.
2. $\displaystyle\int_X|f_n-f|\,d\mu\to0$ as $n\to\infty$ (convergence in $L^1$).

---

# Why Is It True

**(2) $\Rightarrow$ (1).** $L^1$-convergence gives convergence in measure by [[Thm - Markov's Inequality|Markov's inequality]] ($\mu(|f_n-f|>\varepsilon)\le\varepsilon^{-1}\int|f_n-f|\to0$). For uniform integrability: $L^1$-convergence makes $(f_n)$ a tail-uniform family — for $n\ge n_0$, $\int_A|f_n|\le\int_A|f|+\int|f_n-f|$ is small, and the *finite* family $\{f,f_1,\dots,f_{n_0}\}$ is automatically UI ([[Def - Absolute Continuity and Density|finitely many L¹ functions are UI]]). Finite family $+$ uniform tail $=$ UI of the whole sequence.

**(1) $\Rightarrow$ (2)** is the substance. Suppose, for contradiction, $\int|f_n-f|\not\to0$. Pass to a subsequence along which $\int|f_n-f|$ stays bounded away from $0$, and (by the [[Def - Convergence in Measure|subsequence principle]]) along which additionally $f_n\to f$ **a.e.** Split the integral at a threshold set $F$:
$$\int|f_n-f|=\int_F|f_n-f|+\int_{X\setminus F}|f_n-f|.$$
Choose $F$ so the *off-$F$* part is small: UI of $(f_n)$ and of $f$ gives $\delta$ with $\int_A|f_n|,\int_A|f|<\varepsilon$ whenever $\mu(A)<\delta$; [[Thm - Egorov's Theorem|Egorov's theorem]] supplies a set $F$ with $\mu(X\setminus F)<\delta$ on which $f_n\to f$ **uniformly**. On $F$ the uniform convergence kills $\int_F|f_n-f|\le\mu(X)\sup_F|f_n-f|\to0$ — *here $\mu(X)<\infty$ is spent*. Off $F$, uniform integrability bounds $\int_{X\setminus F}|f_n-f|\le\int_{X\setminus F}|f_n|+\int_{X\setminus F}|f|<2\varepsilon$. Total $<3\varepsilon$ — contradicting the subsequence staying bounded away from $0$.

The mechanism: **Egorov splits $X$ into a good set $F$ (uniform convergence) and a small bad set; uniform integrability guarantees the sequence carries negligible mass on the small bad set; finite total measure converts uniform convergence on $F$ into a small integral.** Convergence in measure $\to$ a.e. on a subsequence $\to$ Egorov; uniform integrability controls the leftover. The two hypotheses are exactly the two halves: closeness, and no escape.

---

# What Makes This Hard

The proof of (1)$\Rightarrow$(2) is a *three-way split* and one must see why each piece needs which hypothesis. The non-obvious choreography: argue by contradiction along a subsequence; *promote* convergence in measure to a.e. convergence (subsequence principle) so that Egorov becomes available; use Egorov to manufacture the good set $F$; then deploy uniform integrability *only* on the small complement. The classic confusion is thinking UI alone, or convergence in measure alone, suffices — neither does, and the moving-spike examples ($f_n=n\mathbf{1}_{[0,1/n]}$: converges in measure to $0$, not UI, not $L^1$-convergent) show each hypothesis is independently necessary.

---

# Rederivation Scaffold

**High-level strategy.** (2)$\Rightarrow$(1): Markov for in-measure; finite-family-UI plus uniform tail for UI. (1)$\Rightarrow$(2): contradiction along a subsequence converging a.e.; Egorov splits $X$; uniform convergence on $F$ (using $\mu(X)<\infty$) and uniform integrability off $F$ make $\int|f_n-f|$ small.

**Subgoal decomposition.**

1. **(2)$\Rightarrow$(1).** Markov $\Rightarrow$ in-measure. UI: tail $n\ge n_0$ controlled by $\int|f_n-f|$, head a finite UI family.
2. **(1)$\Rightarrow$(2), setup.** Assume $\int|f_n-f|\not\to0$; subsequence with $\int|f_n-f|\ge c>0$ and (subsequence principle) $f_n\to f$ a.e.
3. **Egorov split.** $\delta$ from UI; $F$ from Egorov with $\mu(X\setminus F)<\delta$, $f_n\to f$ uniformly on $F$.
4. **Three-piece bound.** $\int_F|f_n-f|\le\mu(X)\sup_F|f_n-f|\to0$; $\int_{X\setminus F}|f_n-f|\le\int_{X\setminus F}(|f_n|+|f|)<2\varepsilon$. Contradiction.

---

# Lemma Decomposition

> [!note]- Lemma 1: $L^1$-convergence implies uniform integrability
> **Statement:** If $\int|f_n-f|\to0$, then $(f_n)$ is uniformly integrable.
>
> **Hint:** Split the tail at a fixed index $n_0$: the finitely many functions $\{f,f_1,\dots,f_{n_0}\}$ are automatically UI, and the late terms borrow UI from $f$ plus the small $L^1$-error.
>
> **Why needed:** This is the easy direction (1)$\Leftarrow$(2) of the Vitali equivalence — once Markov's inequality gives in-measure convergence, this lemma supplies the missing UI piece so the pair (in-measure + UI) is established.
>
> > [!note]- Full proof
> > Given $\varepsilon$, pick $n_0$ with $\int|f_n-f|<\varepsilon/2$ for $n\ge n_0$. The finite family $\{f,f_1,\dots,f_{n_0}\}\subseteq L^1$ is UI ([[Def - Absolute Continuity and Density|finite families are UI]]), giving $\delta$ with $\mu(A)<\delta\Rightarrow\int_A(|f|\vee\max_{n\le n_0}|f_n|)<\varepsilon/2$. For $n>n_0$, $\int_A|f_n|\le\int_A|f|+\int|f_n-f|<\varepsilon/2+\varepsilon/2$. So $\sup_n\int_A|f_n|<\varepsilon$. $\square$

> [!note]- Lemma 2: Uniform integrability + in-measure ⇒ $L^1$
> **Statement:** If $\mu(X)<\infty$, $f_n\xrightarrow{\mu}f$, $(f_n)$ UI, then $\int|f_n-f|\to0$.
>
> **Hint:** Argue by contradiction along a subsequence so that $f_n\to f$ a.e.; then Egorov gives a "good set" $F$ where convergence is uniform, while UI controls the "bad set" $X\setminus F$ of small measure.
>
> **Why needed:** This is the substantive direction (1)$\Rightarrow$(2) — it is where uniform integrability does its work, converting in-measure convergence (which is too weak for $L^1$) into actual $L^1$-convergence by killing the escape-to-infinity mode.
>
> > [!note]- Full proof
> > Suppose not: a subsequence has $\int|f_n-f|\ge c>0$; refine it ([[Def - Convergence in Measure|subsequence principle]]) so $f_n\to f$ a.e. Fix $\varepsilon>0$; let $\delta$ witness UI of $(f_n)\cup\{f\}$. [[Thm - Egorov's Theorem|Egorov]] gives measurable $F$, $\mu(X\setminus F)<\delta$, $f_n\to f$ uniformly on $F$. Then $\int_F|f_n-f|\le\mu(F)\sup_F|f_n-f|\le\mu(X)\sup_F|f_n-f|\to0$, and $\int_{X\setminus F}|f_n-f|\le\int_{X\setminus F}|f_n|+\int_{X\setminus F}|f|<2\varepsilon$ by choice of $\delta$. So $\limsup\int|f_n-f|\le2\varepsilon$; $\varepsilon\downarrow0$ contradicts $\ge c$. $\square$

---

# Formal Proof

> [!note]- Complete formal proof
> (2)$\Rightarrow$(1): Markov's inequality gives in-measure convergence; Lemma 1 gives UI. (1)$\Rightarrow$(2): Lemma 2. $\blacksquare$

---

# Cross-Field Exercise Suggestions

Vitali is the engine of the **$L^1$ [[Def - Martingale|martingale]] convergence theorem**: a [[Def - Martingale|martingale]] $(X_n)$ converges in $L^1$ iff it is uniformly integrable, because the family $\{\mathbb{E}[Z\mid\mathcal{F}_n]\}$ of conditional expectations of a fixed $Z\in L^1$ is automatically UI. It is also the right tool whenever a.s. convergence must be upgraded to $L^1$ without a dominating function — the typical situation in [[Thm - Strong Law of Large Numbers|laws of large numbers]] and ergodic theory.

---

# Bridges

- **[[Thm - Dominated Convergence Theorem]]** — DCT is the special case "dominated $\Rightarrow$ UI"; Vitali is the sharp generalisation.
- **[[Thm - Egorov's Theorem]]** — supplies the good set on which convergence is uniform.
- **[[Def - Uniform Integrability]]** *(Advanced Probability)* — uniform integrability, the exact compactness condition controlling $L^1$-convergence.
