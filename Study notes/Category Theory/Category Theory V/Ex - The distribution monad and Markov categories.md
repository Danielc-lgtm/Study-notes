---
type: exercise
subject: category-theory
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Monad and Comonad"
  - "Def - Kleisli Category"
  - "Def - Monoidal Category"
tags: [category-theory, foundations]
---

# Problem Statement

Let $D : \mathbf{Set}\to\mathbf{Set}$ be the **finitely-supported distribution functor**: $D(X)$ is the set of probability distributions on $X$ with finite support, $p : X\to[0,1]$ with $\sum_x p(x) = 1$ and $p(x) = 0$ for all but finitely many $x$. Define $\eta_X(x) = \delta_x$ (the point mass at $x$) and $\mu_X : D(D(X))\to D(X)$ by averaging: $\mu_X(P)(x) = \sum_{p} P(p)\,p(x)$ (the law of total probability).

**(a)** Show $(D, \eta, \mu)$ is a [[Def - Monad and Comonad|monad]].

**(b)** Identify the [[Def - Kleisli Category|Kleisli category]] $\mathbf{Set}_D$ as "sets and stochastic maps," with Kleisli composition the Chapman–Kolmogorov equation.

**(c)** Exhibit the **copy** and **discard** maps making $\mathbf{Set}_D$ a **Markov category**, and explain why this is the categorical foundation of probability.

**Recall:**

![[Def - Kleisli Category#The Definition]]

A [[Def - Monad and Comonad|monad]] needs associativity $\mu\circ D\mu = \mu\circ\mu D$ and unitality $\mu\circ D\eta = \mu\circ\eta D = 1$. A [[Def - Kleisli Category|Kleisli arrow]] $A\to B$ is a function $A\to DB$, composed by $g\diamond f = \mu_C\circ Dg\circ f$.

---

# Convergent Strategy

**Problem class:** A "build a probability monad and recognize its Kleisli category" problem — the categorical-probability bridge (legal operation 4). Part (c) adds the copy-discard structure that names the **Markov category**.

**Assumption pattern:** A stochastic map "$a$ produces a distribution over outcomes $b$" is a Kleisli arrow $A\to DB$ (operation 4). The averaging multiplication is the law of total probability; recognizing this is the assumption that turns abstract Kleisli composition into Chapman–Kolmogorov.

**Theorem routing:** Route part (a) through the monad axioms (operation 2), checking that averaging is associative and point masses are units. Route (b) through [[Def - Kleisli Category]], unwinding $g\diamond f$ into the marginalization sum. Route (c) through the [[Def - Monoidal Category|symmetric monoidal]] structure: the Cartesian product on $\mathbf{Set}$ lifts to a tensor on $\mathbf{Set}_D$ (product of distributions), and copy/discard are the comonoid maps.

**Key decision point:** The crux of (c) is that copy $X\to X\times X$ in $\mathbf{Set}_D$ — "sample once, output the same value twice" — is **not** natural in stochastic maps: copying after a random map gives correlated outputs, while a random map after copying gives independent ones. This asymmetry is exactly what distinguishes probability from determinism, and it is the defining feature of a Markov (non-Cartesian) monoidal category.

---

# Legal Operations Used

1. **Operation 4 from the topic page (pass to the Kleisli category to model effectful maps).** Stochastic maps are Kleisli arrows for $D$, composed by Chapman–Kolmogorov.

2. **Operation 2 from the topic page (check the monad axioms via whiskering).** Part (a) verifies associativity (law of total probability is associative) and unit laws (point masses).

3. **Operation 7 from the topic page (unwind a monoid/comonoid object in a monoidal category).** Part (c) identifies copy/discard as the comonoid structure on each object of the symmetric monoidal Kleisli category.

---

# Hints

> [!note]- Hint 1
> For (a), $\mu_X$ takes a distribution $P$ over distributions and averages: the probability it assigns to $x$ is $\sum_p P(p)p(x)$. Associativity $\mu\circ D\mu = \mu\circ\mu D$ is the associativity of iterated averaging — both sides compute $\sum P''(P')P'(p)p(x)$-style triple sums.

> [!note]- Hint 2
> Unit laws: averaging a distribution-of-point-masses ($D\eta$) returns it; treating a distribution as a single point mass over distributions ($\eta D$) and averaging returns it.

> [!note]- Hint 3
> For (b), a Kleisli arrow $f : A\to DB$ is a **Markov kernel** $f(b\mid a)$. Kleisli composition $(g\diamond f)(c\mid a) = \mu_C(Dg(f(a)))(c) = \sum_b f(b\mid a)\,g(c\mid b)$ — Chapman–Kolmogorov.

> [!note]- Hint 4
> For (c), the Cartesian product lifts to a tensor on $\mathbf{Set}_D$ (product distributions for independent components). **Discard** $X\to 1$ is the unique map (marginalize everything away); **copy** $X\to X\times X$ is "duplicate the sampled value," the diagonal made stochastic. Crucially, copy is *not natural*: a random map followed by copy gives correlated outputs, unlike in a Cartesian category.

---

# Solution

The plan: verify $D$ is a monad via associativity of averaging (Step 1); unwind Kleisli composition into Chapman–Kolmogorov (Step 2); lift the Cartesian product to a tensor and exhibit copy/discard, noting copy's non-naturality (Step 3). The crux is that the failure of copy to be natural *is* the probabilistic content.

**Step 1 (a): $D$ is a monad.**

> [!note]- Derivation
> *Associativity.* Let $\Pi \in D(D(D(X)))$, a distribution over distributions-over-distributions. Both $\mu_X\circ D\mu_X$ and $\mu_X\circ\mu_{DX}$ compute, for $x \in X$,
> $$\sum_{P}\sum_{p}\sum \Pi(\cdots)\,P(p)\,p(x),$$
> the fully averaged probability of $x$. They agree because finite sums commute and multiply associatively (the law of total probability composed with itself). So $\mu\circ D\mu = \mu\circ\mu D$.
>
> *Unit laws.* For $p \in D(X)$: $D\eta_X(p)$ is the distribution over point masses $\{\delta_x\}$ with weights $p(x)$; averaging gives $\sum_x p(x)\delta_x = p$. And $\eta_{DX}(p) = \delta_p$, the point mass at $p$; averaging gives $p$. So $\mu\circ D\eta = 1 = \mu\circ\eta D$. Hence $(D,\eta,\mu)$ is a monad.

**Step 2 (b): Kleisli = stochastic maps.**

> [!note]- Derivation
> A Kleisli arrow $f : A\to DB$ assigns to each $a$ a distribution $f(a) \in DB$; writing $f(b\mid a) := f(a)(b)$, this is a **Markov kernel** (a conditional distribution / stochastic matrix). Kleisli composition of $f : A\to DB$ and $g : B\to DC$ is
> $$(g\diamond f)(a) = \mu_C\big(Dg(f(a))\big), \qquad (g\diamond f)(c\mid a) = \sum_b f(b\mid a)\,g(c\mid b),$$
> the **Chapman–Kolmogorov** equation (matrix product of stochastic matrices). The Kleisli identity $\eta_A(a) = \delta_a$ is the deterministic identity kernel. So $\mathbf{Set}_D$ is the category of sets and stochastic maps, $\mathbf{FinStoch}$.

**Step 3 (c): The Markov category structure.**

> [!note]- Derivation
> The Cartesian product on $\mathbf{Set}$ lifts to a symmetric monoidal tensor $\otimes$ on $\mathbf{Set}_D$: on objects $A\otimes B = A\times B$, and a tensor of kernels $f\otimes g$ produces the *product* (independent) distribution. The monoidal unit is the one-point set $1$.
>
> *Discard.* For each object $X$, $\mathrm{del}_X : X\to 1$ is the unique Kleisli arrow to the unit (the point mass at $*$); it marginalizes $X$ away.
>
> *Copy.* $\mathrm{copy}_X : X\to X\otimes X$ is the deterministic kernel $x\mapsto\delta_{(x,x)}$: "sample once, output the value twice." Together $(\mathrm{copy}, \mathrm{del})$ make every object a commutative comonoid, and $\mathbf{Set}_D$ a **Markov category**.
>
> The crucial feature: **copy is not natural** with respect to general (random) Kleisli arrows. For a random $f : A\to DB$, $\mathrm{copy}_B\diamond f$ produces *correlated* pairs (the same sample twice), whereas $(f\otimes f)\diamond\mathrm{copy}_A$ produces *independent* pairs (two independent samples). In a Cartesian category these coincide; in $\mathbf{Set}_D$ they differ, and that difference is exactly the distinction between "use one random outcome twice" and "draw two independent outcomes." This non-Cartesianness is what makes $\mathbf{Set}_D$ a genuine probability theory rather than a deterministic one.

> [!note]- Complete formal solution
> **(a)** $\mu_X$ averages a distribution-over-distributions. Associativity is the associativity of iterated averaging (commuting finite sums); unit laws hold since averaging a distribution of point masses, or a point mass over distributions, returns the original. So $D$ is a monad.
>
> **(b)** A Kleisli arrow $A\to DB$ is a Markov kernel $f(b\mid a)$; Kleisli composition is $\sum_b f(b\mid a)g(c\mid b)$, the Chapman–Kolmogorov equation. Hence $\mathbf{Set}_D = \mathbf{FinStoch}$, sets and stochastic maps.
>
> **(c)** The Cartesian product lifts to a symmetric monoidal $\otimes$ (product distributions). Discard $\mathrm{del}_X : X\to 1$ marginalizes; copy $\mathrm{copy}_X : x\mapsto\delta_{(x,x)}$ duplicates. These comonoid maps make $\mathbf{Set}_D$ a Markov category; copy is *not* natural for random maps (copy-after-random is correlated, random-after-copy is independent), encoding probabilistic correlation. $\blacksquare$

> [!tip] Why this grounds agent foundations
> In a Markov category, conditional independence, sufficient statistics, and Bayesian inversion are all definable from copy and discard alone, diagrammatically. Agents-and-environments are open stochastic processes — morphisms in (an extension of) such a symmetric monoidal category — and their interactions are wiring diagrams. This is the categorical substrate of **categorical probability**, **compositional game theory**, and **categorical systems theory**.

---

# Key Takeaways

**The Kleisli category of the distribution monad is probability theory, and its composition is Chapman–Kolmogorov.** The reusable principle is that "a map producing a distribution over outcomes" is a Kleisli arrow for $D$, and composing two such maps — propagating uncertainty through a chain — is *automatically* the law of total probability, falling out of the monad multiplication $\mu$ (averaging). You never have to posit Chapman–Kolmogorov separately; it is forced by the monad structure, exactly as relational composition was forced for the [[Ex - The Kleisli category of the powerset monad is Rel|power-set monad]]. The trigger is "stochastic / probabilistic maps"; the reaction is "Kleisli category of the probability monad, composition = marginalize over the intermediate."

**The failure of copy to be natural is the entire content of probability.** The single deepest insight is that in a deterministic (Cartesian) category, copying commutes with everything — duplicating then mapping equals mapping then duplicating — but in the stochastic Kleisli category these differ, because copying a random value gives a *correlated* pair while sampling twice gives an *independent* pair. This asymmetry, formalized as the non-naturality of the copy map, is precisely what makes a Markov category non-Cartesian and is the abstract signature of randomness. The diagnostic for recognizing a "genuinely probabilistic" structure is exactly this: copy and discard exist (every object is a comonoid) but copy is not natural. This is the dividing line between deterministic and stochastic process theories.

**Copy and discard turn a monoidal category into a probability theory you can compute with diagrammatically.** The transferable lesson is that equipping a symmetric monoidal category with coherent copy and discard maps (a comonoid on every object) is *the* abstract way to do probability: conditional independence becomes a diagrammatic equation, marginalization is composition with discard, and Bayesian inversion is a categorical operation. This is why Markov categories are the foundation of **categorical probability** and the agent-foundations program — they replace measure-theoretic bookkeeping with string-diagram manipulation, valid by [[Thm - Mac Lane Coherence Theorem|coherence]]. When a problem involves composing uncertain processes, the move is to work in the appropriate Markov category and reason graphically. See [[Ex - Braidings and symmetry]] for the symmetric-monoidal structure that copy/discard build on, and the chapter's Bridges for the route to compositional game theory.
