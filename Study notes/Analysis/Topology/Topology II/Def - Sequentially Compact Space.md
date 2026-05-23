---
type: definition
subject: topology
prereqs:
  - "Def - Topological Space"
  - "Def - Net Convergence"
  - "Def - Compact Space"
  - "Def - First and Second Countable"
tags: [analysis, topology]
---

# Notation

Throughout, $X$ is a topological space, and $\{x_n\}_{n \in \mathbb{N}}$ denotes a sequence in $X$. A **subsequence** of $\{x_n\}$ is a sequence $\{x_{n_k}\}_{k \in \mathbb{N}}$ where $n_1 < n_2 < \ldots$ is a strictly increasing sequence of natural numbers. The space $X$ is **sequentially compact** if every sequence has a convergent subsequence. The full registry of symbols is on [[Topology II — §4–7 Connectivity, Separation, Nets, Compactness]].

---

# Axiom Motivation

Compactness has been defined and characterized in three equivalent forms — open cover, finite intersection property, every net has a convergent subnet (see [[Def - Compact Space]]). The third form is the "true name" of compactness for analysis: when you want to extract a limit, this is the form you reach for. But there is a *sequential* variant that is so natural, and so familiar from $\mathbb{R}^n$, that it deserves to be stated separately: every sequence has a convergent subsequence. We call this **sequential compactness**.

In the metric world this is just the Bolzano–Weierstrass theorem, and it is equivalent to compactness. The Bolzano–Weierstrass statement is the form analysts and probabilists use ninety percent of the time: "by compactness, pass to a convergent subsequence $x_{n_k} \to x_\infty$, and continue with the limit". So why do we have a separate notion at all? Because in the *non-metric* world, sequential compactness and compactness are *not equivalent*, and being careful about which one is in play matters.

The reason they diverge: sequences are *too short* in non-first-countable spaces. A sequence is indexed by $\mathbb{N}$, which has cofinality $\omega$ (countable). In a space where every point has a countable neighbourhood basis (a first-countable space), a sequence can thread the neighbourhood structure of any point completely: any net converging to $x$ has a subsequence converging to $x$, so sequence-level compactness suffices. But in a space without first-countability — say, $\omega_1 + 1$ with the order topology, or a Banach space with the weak topology, or a product $\prod_{\alpha < \omega_1} X_\alpha$ of uncountably many spaces — a sequence cannot thread all neighbourhoods. There are points reachable by nets (indexed by uncountable directed sets) that are *not* reachable by any sequence. Consequently, sequential compactness and compactness can diverge: a space can have every sequence with a convergent subsequence (sequential compactness) yet have a net with no convergent subnet (failing compactness), or vice versa.

Concrete examples of the divergence:

1. **Compact but NOT sequentially compact:** The product space $\{0, 1\}^{[0, 1]}$ — functions from $[0, 1]$ to $\{0, 1\}$ with the product topology. This is compact by Tychonoff. But it is *not* sequentially compact: the sequence $f_n(x) =$ "the $n$-th binary digit of $x$" has no convergent subsequence (one can construct an $x$ whose binary digits are arranged so any subsequence of $f_n(x)$ oscillates). The proof uses a diagonal-style argument.

2. **Sequentially compact but NOT compact:** The first uncountable ordinal $\omega_1$ with the order topology. Every sequence in $\omega_1$ has a sup which is a countable ordinal, hence in $\omega_1$, and the sequence has a convergent subsequence (consisting of suitably chosen elements). So $\omega_1$ is sequentially compact. But it is *not* compact: the cover by $\{[0, \alpha) : \alpha < \omega_1\}$ has no finite subcover.

These pathologies are the technical motivation for being careful: in a general topological space, "compact" and "sequentially compact" are *different* properties, and which one you have or want depends on the problem.

The good news: in *metric spaces* — and more generally in spaces with enough countability — the two notions coincide. Specifically:

- **Metric spaces:** compact ⟺ sequentially compact ⟺ totally bounded + complete (this is the **Heine–Borel–Bolzano–Weierstrass equivalence**, developed in [[Topology III — §8–12 Products, Metric Spaces, Locally Compact, Paracompact|Topology III]]).
- **Second-countable spaces:** compact ⟺ sequentially compact.
- **First-countable spaces:** compact ⇒ sequentially compact (but not vice versa in general, depending on cardinality conditions).

The triple equivalence in metric spaces — compact ⟺ sequentially compact ⟺ totally bounded + complete — is one of the most useful theorems in analysis. The "totally bounded + complete" form is operationally the third "true name" of compactness in the metric setting: total boundedness rules out the *too-many-balls* failure mode (orthonormal basis in Hilbert space), completeness rules out the *escape-to-Cauchy-with-no-limit* failure mode (open interval $(0, 1)$ where Cauchy sequences can approach $0$).

A trigger-reaction pattern: when you're working in a metric space and want compactness, the most useful form is *sequential* compactness. When you want to extract a convergent subsequence from a bounded sequence in $\mathbb{R}^n$, this is Bolzano–Weierstrass. When you want to do the same in a Hilbert space (where the unit ball is not compact!), you use *weak* sequential compactness — the unit ball is weakly sequentially compact (by reflexivity), and you extract a *weakly* convergent subsequence. This is the bedrock of variational methods in PDE.

A subtle point about sequential compactness in *non-metric* spaces. Sometimes sequential compactness is what you actually need (for instance, in probability theory, where one cares about almost-sure convergence of subsequences). Sometimes compactness is what you actually need (for instance, to apply the closed-map property or to prove uniform continuity). One needs to know which is which, and which spaces let you have both.

---

# The Definition

Let $X$ be a topological space.

**Sequentially compact space.** $X$ is **sequentially compact** if every sequence $\{x_n\}_{n \in \mathbb{N}}$ in $X$ has a convergent subsequence — that is, there exist a subsequence $\{x_{n_k}\}_{k \in \mathbb{N}}$ (with $n_1 < n_2 < \ldots$) and a point $x \in X$ such that $x_{n_k} \to x$.

**Relation to compactness.** In general:

- **Compactness does NOT imply sequential compactness** (counter-example: $\{0, 1\}^{[0, 1]}$).
- **Sequential compactness does NOT imply compactness** (counter-example: $\omega_1$ with the order topology).

**Equivalence in metric (and second-countable) spaces.** In a metric space — more generally, a second-countable space — the following are equivalent:

1. $X$ is compact.
2. $X$ is sequentially compact.
3. $X$ is totally bounded and complete (metric only).

This is the **Heine–Borel–Bolzano–Weierstrass equivalence**, developed in [[Topology III — §8–12 Products, Metric Spaces, Locally Compact, Paracompact|Topology III]].

**Relative compactness.** A subset $A \subseteq X$ is **relatively (sequentially) compact** if its closure $\overline{A}$ is (sequentially) compact. Equivalently in metric spaces, $A$ is relatively compact iff every sequence in $A$ has a convergent subsequence (with limit in $X$, not necessarily in $A$).

---

# Relate to Other Fields / Compression

The sequence-vs-net distinction is the same distinction as **first countable vs general topological space** in many guises. In **functional analysis**, the weak topology on an infinite-dimensional Banach space is *not* first-countable, so sequential compactness and compactness diverge. The **Eberlein–Šmulian theorem** says that for the *weak* topology on a Banach space, weak compactness and weak sequential compactness coincide (a deep theorem!) — but this is a special property of the weak topology, not a general one.

In **probability theory**, the relevant compactness is the **Prokhorov criterion**: a family of probability measures on a complete separable metric space is precompact in the weak topology iff it is tight. The "Prokhorov compact = tight" characterisation is sequentially flavoured — it gives convergent *subsequences* of measures, which is what one actually uses to prove central limit theorems and martingale CLTs.

In **PDE and calculus of variations**, the workhorse compactness theorems are sequential: **Rellich–Kondrachov** (the embedding $W^{1,p}(\Omega) \hookrightarrow L^p(\Omega)$ for bounded $\Omega$ is sequentially compact), **Aubin–Lions** (compactness in $L^p([0, T]; X)$), **Helly's selection theorem** (sequences of monotone functions have pointwise convergent subsequences). In these settings, the relevant compactness is *sequential*, because PDE solutions are constructed via sequence-based limit-passage arguments.

In **dynamical systems**, the compactness of a phase space is what guarantees the existence of invariant measures (Krylov–Bogolyubov theorem). The proof uses sequential compactness of the space of measures.

---

# Examples / Corollaries

**Is an instance — the unit interval $[0, 1]$ in $\mathbb{R}$.** Both compact and sequentially compact. Every sequence in $[0, 1]$ has a convergent subsequence by Bolzano–Weierstrass: the sequence is bounded, so by the bisection method one can extract a Cauchy subsequence, which converges in the complete space $\mathbb{R}$ to a point in $[0, 1]$ (closure of where the sequence lives).

**Is an instance — any compact metric space.** Every compact metric space is sequentially compact (and conversely). The bridge: every sequence is a net, and in a compact space every net has a convergent subnet. In a metric (first-countable) space, the convergent subnet can be refined to a convergent subsequence.

**Is an instance of sequential compactness but NOT compactness — $\omega_1$ with the order topology.** Every sequence in $\omega_1$ has a countable supremum $\alpha < \omega_1$, hence lives in $[0, \alpha]$ which is compact (closed bounded subset of a well-ordered set), so the sequence has a convergent subsequence. But the cover $\{[0, \beta) : \beta < \omega_1\}$ has no finite subcover.

**Is an instance of compactness but NOT sequential compactness — $\{0, 1\}^{[0, 1]}$.** The product is compact by Tychonoff. But the sequence $f_n(x) =$ "$n$-th binary digit of $x$" has no convergent subsequence: given any subsequence $\{f_{n_k}\}$, construct $x \in [0, 1]$ with binary expansion arranged so $f_{n_k}(x) = 0$ for $k$ even and $1$ for $k$ odd — then $f_{n_k}(x)$ does not converge. Hence no subsequence converges pointwise everywhere, and pointwise convergence is what convergence means in the product topology.

**Is NOT an instance of either — the open interval $(0, 1)$.** Sequential compactness fails: $x_n = 1/n$ has no convergent subsequence in $(0, 1)$ (every subsequence converges to $0 \notin (0, 1)$). Compactness fails similarly. So compactness and sequential compactness fail *together* in this case.

**Is NOT an instance of either — the unit ball of $\ell^2$ in the norm topology.** The orthonormal basis $\{e_n\}$ has no convergent subsequence: $\|e_n - e_m\| = \sqrt{2}$ for $n \neq m$, so no subsequence is Cauchy. Hence the closed unit ball is not sequentially compact in norm. (It is sequentially compact in the *weak* topology, by reflexivity and Eberlein–Šmulian.)

**Corollary — sequential compactness is preserved by continuous images in first-countable spaces.** If $f : X \to Y$ is continuous, $X$ sequentially compact, and $Y$ first-countable, then $f(X)$ is sequentially compact. (Take a sequence $\{y_n\}$ in $f(X)$, lift to $\{x_n\}$ via choice; extract a convergent subsequence $x_{n_k} \to x$; then $y_{n_k} = f(x_{n_k}) \to f(x)$.)

**Corollary — sequential compactness + Hausdorff ⇒ unique limit.** If $\{x_n\}$ has a convergent subsequence in a Hausdorff space, the limit is unique. (Standard from [[Thm - Hausdorff Iff Unique Net Limits]].)

**Corollary — relative sequential compactness in $\mathbb{R}^n$.** A subset $A \subseteq \mathbb{R}^n$ is relatively sequentially compact (every sequence in $A$ has a convergent subsequence in $\mathbb{R}^n$) iff $A$ is bounded. This is Bolzano–Weierstrass in pure form.

**Calibration check.** Verify the following:

(i) In $\mathbb{R}^n$, the three notions "compact", "sequentially compact", and "closed and bounded" are equivalent. The bridge to "closed" is Hausdorffness ($\mathbb{R}^n$ is Hausdorff, so compact subsets are closed), and the bridge to "bounded" is the compactness of $[-N, N]^n$ for large enough $N$.

(ii) In a metric space, "sequentially compact" is equivalent to "totally bounded + complete". A space is **totally bounded** if for every $\varepsilon > 0$ there is a finite cover by $\varepsilon$-balls. The bridge: sequential compactness gives Cauchy subsequences (from bounded sequences), which give convergent subsequences via completeness. See [[Topology III — §8–12 Products, Metric Spaces, Locally Compact, Paracompact|Topology III]] for the full theorem.

(iii) Weak sequential compactness is the relevant compactness in PDE: bounded sequences in a reflexive Banach space have weakly convergent subsequences. This is *not* the same as norm sequential compactness — the unit ball is weakly sequentially compact but never norm sequentially compact in infinite dimensions.

---

# Unlocked by This

> [!tip] **Heine–Borel–Bolzano–Weierstrass Equivalence** *(from Topology III)*
> In metric spaces, the three notions **compact**, **sequentially compact**, and **totally bounded + complete** all coincide. See [[Topology III — §8–12 Products, Metric Spaces, Locally Compact, Paracompact|Topology III]]. This triple characterization is the foundation of metric-space analysis.

> [!tip] **Bolzano–Weierstrass Theorem** *(from Real Analysis)*
> Every bounded sequence in $\mathbb{R}^n$ has a convergent subsequence. This is the sequential compactness of bounded sets in $\mathbb{R}^n$, and it is the bedrock of every "extract a convergent subsequence" argument in real analysis.

> [!tip] **Eberlein–Šmulian Theorem** *(from Functional Analysis)*
> In the weak topology on a Banach space, **weak compactness** and **weak sequential compactness** coincide. This is remarkable because the weak topology is not first-countable, so the equivalence is not automatic — it relies on special properties of the weak topology.

> [!tip] **Rellich–Kondrachov Theorem** *(from PDE / Functional Analysis)*
> The embedding of the Sobolev space $W^{1,p}(\Omega)$ into $L^p(\Omega)$ for a bounded domain $\Omega \subseteq \mathbb{R}^n$ is **compact** (and hence sequentially compact). This is the workhorse compactness result in PDE: bounded $W^{1,p}$ sequences have $L^p$-convergent subsequences.
