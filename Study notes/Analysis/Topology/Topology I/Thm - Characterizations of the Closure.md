---
type: theorem
subject: topology
prereqs:
  - "Def - Topological Space"
  - "Def - Closure, Interior, and Boundary"
  - "Def - Neighbourhood and Neighbourhood Basis"
  - "Def - Basis and Subbasis for a Topology"
  - "Def - First and Second Countable"
tags: [analysis, topology]
---

# Notation

$X$ is a topological space, $A \subseteq X$ a subset, and $x \in X$ a point. The closure of $A$ is $\overline{A}$. A **neighbourhood** of $x$ is any $N \subseteq X$ containing an open set $U$ with $x \in U \subseteq N$. A **neighbourhood basis** $\mathcal{B}_x$ at $x$ is a generating family of neighbourhoods; in a metric space, $\{B_{1/n}(x)\}_{n \geq 1}$ is the canonical countable basis. The full notation registry is on [[Topology I — §1–3 Metric and Topological Spaces]].

---

# Statement

> **Theorem (characterizations of the closure).** Let $X$ be a topological space, $A \subseteq X$, and $x \in X$. The following conditions are equivalent:
>
> (i) $x \in \overline{A}$;
> (ii) every **open set** $U \subseteq X$ containing $x$ meets $A$, i.e. $U \cap A \neq \emptyset$;
> (iii) every **neighbourhood** $N$ of $x$ meets $A$;
> (iv) every **basis element** $B$ of the topology of $X$ that contains $x$ meets $A$ (equivalently, every element of any neighbourhood basis $\mathcal{B}_x$ at $x$ meets $A$).
>
> If, in addition, $X$ is **first countable** at $x$ (e.g. $X$ is a metric space), then these are also equivalent to:
>
> (v) there exists a sequence $\{a_n\}_{n \geq 1} \subseteq A$ with $a_n \to x$.
>
> In a general topological space, (v) is **strictly weaker** than (i)–(iv): the sequential closure can be a proper subset of the topological closure.

---

# Motivation

The definition of closure is set-theoretic and global: $\overline{A}$ is the intersection of all closed supersets, equivalently the smallest closed superset. This is the *right* definition — it makes closure exist for every subset of every topological space and reveals its universal-property nature — but it is not the most useful for actual computations. When we want to decide whether a particular point $x$ lies in $\overline{A}$, the global definition tells us to range over *every* closed superset of $A$, which is in general an enormous family. We need a *local* criterion: a condition checkable at $x$ alone, in terms of the open sets near $x$.

This theorem provides that criterion, in several equivalent forms of increasing convenience. The cleanest is: $x \in \overline{A}$ if and only if every open set containing $x$ meets $A$. So one can decide closure membership by examining the open sets containing $x$ — a local question. The further refinements — every neighbourhood, every basis element, every member of a neighbourhood basis — all say the same thing, and the choice among them is purely a matter of what generating family is convenient in context.

The most analytically familiar form is the sequential one: $x \in \overline{A}$ if and only if some sequence in $A$ converges to $x$. This is the statement that closure equals sequential closure, and it is the bridge between topology and the analytic notion of "limit". The catch is that this equivalence holds only in first-countable spaces — sequences are not in general powerful enough to detect closure. In a general topological space one must replace sequences with nets or use the open-set forms. The clean delineation of when sequences suffice is one of the most consequential structural facts in topology.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$x \in \overline{A}$" or its negation. Sources are alternative descriptions of $A$ that are equivalent to closure-membership.

The first disguised source is **$A$ is closed and contains $x$.** Property $B$: $x \in A$ and $A$ is closed. The bridge: closed $\implies A = \overline{A}$, so $x \in A = \overline{A}$. This is the trivial case; the value is that recognizing $A$ is closed lets us skip the characterization argument. *Example:* showing a limit point of a closed set is in the set.

The second source is **a defining sequence approach in a metric space.** Property $B$: there is a sequence $a_n \in A$ with $a_n \to x$. The bridge: in a first-countable space, $x \in \overline{A}$ by the sequential characterization. *Example:* showing $\sqrt{2} \in \overline{\mathbb{Q}}$ in $\mathbb{R}$ by exhibiting a sequence of rational approximations.

The third source is **$x$ is a boundary point.** Property $B$: $x \in \partial A$. The bridge: $\partial A \subseteq \overline{A}$ (the boundary lies in the closure), so $x \in \overline{A}$. Boundary points are the closure points not interior to $A$ — they are the topologically interesting ones, and they reside in $\overline{A}$ by definition.

The fourth source is **$x$ is a limit point.** Property $B$: every open set containing $x$ meets $A \setminus \{x\}$ — i.e., $x$ has points of $A$ other than itself arbitrarily close. The bridge: a limit point of $A$ is in $\overline{A}$, since every open neighbourhood meets $A$ (in particular meets $A \setminus \{x\}$). Note: $\overline{A} = A \cup \{\text{limit points of } A\}$ is another standard characterization, decomposing the closure into the original set plus its accumulation.

**Targets (Output Amplification)**

The conclusion is the membership $x \in \overline{A}$, which one can amplify by combining with other structural facts.

Combine with **continuity of a function.** Property $D$: $f : X \to Y$ is continuous. The amplified result $E$: $f(x) \in \overline{f(A)}$ — continuous functions preserve closure-containment in the form $f(\overline{A}) \subseteq \overline{f(A)}$. This is what licenses passing limits of sequences in $A$ through $f$ to get limits of sequences in $f(A)$.

Combine with **agreement on a dense subset.** Property $D$: two continuous functions $f, g : X \to Y$ agree on $A$, and $A$ is dense in $X$ ($\overline{A} = X$). The amplified result $E$: if $Y$ is Hausdorff, then $f = g$ on all of $X$. The set $\{x : f(x) = g(x)\}$ is closed (preimage of the diagonal in $Y \times Y$, which is closed in Hausdorff $Y$), contains $A$, hence contains $\overline{A} = X$. So density plus continuity plus Hausdorff target forces uniqueness.

Combine with **a separation hypothesis on $X$.** Property $D$: $X$ is $T_1$ (singletons are closed). The amplified result $E$: $\overline{\{x\}} = \{x\}$, and "$y$ is a limit point of $A$" means $y \in \overline{A \setminus \{y\}}$, sharpening the limit-point characterization. In Hausdorff spaces, the closure of any singleton is itself, and limits of sequences are unique — a sharper version of the closure characterization.

---

# Why Is It True

The set-theoretic definition says $\overline{A} = \bigcap\{F : F \supseteq A, F\ \text{closed}\}$. The point $x$ fails to be in this intersection if and only if it is excluded by *some* closed superset $F$ — i.e., $A \subseteq F$ and $x \notin F$. Setting $U = X \setminus F$, this is equivalent to: there is an open set $U$ with $x \in U$ and $U \cap A = \emptyset$. So "$x \notin \overline{A}$" is exactly "some open neighbourhood of $x$ misses $A$", and by negation "$x \in \overline{A}$" is exactly "every open set containing $x$ meets $A$".

This is the core insight: the bijection between closed supersets of $A$ excluding $x$ and open sets containing $x$ missing $A$ is the complement bijection — closed and open are dual, $A$-containing and $A$-avoiding are dual, and the characterization simply unfolds the definition through this duality.

The other equivalent forms (neighbourhood, basis-element, neighbourhood-basis-element) are immediate weakenings: every open set containing $x$ is in particular a neighbourhood; every neighbourhood contains an open set containing $x$ (definition of neighbourhood); every basis element containing $x$ is an open set containing $x$, and every open set containing $x$ contains a basis element containing $x$ (definition of basis). So "every open meets $A$" iff "every neighbourhood meets $A$" iff "every basis element containing $x$ meets $A$" — and similarly for any neighbourhood basis.

The sequential characterization in first-countable spaces requires one more step. The forward direction: if $x_n \in A$ converges to $x$, then every neighbourhood of $x$ eventually contains $x_n$, hence meets $A$. So $x \in \overline{A}$. The reverse direction is the construction that uses first countability: take a countable, decreasing neighbourhood basis $\{B_n\}$ at $x$ and pick $x_n \in B_n \cap A$ (nonempty by hypothesis); then $x_n \to x$ because every neighbourhood of $x$ contains some $B_N$, hence contains $x_n$ for all $n \geq N$.

The reason the sequential characterization fails in non-first-countable spaces: without a countable basis at $x$, there is no way to construct a sequence whose tails are eventually inside *every* neighbourhood of $x$. The right substitute is a **net** — a generalization indexed by a directed set rather than $\mathbb{N}$ — but sequences alone are insufficient.

---

# What Makes This Hard

The non-obvious step is the *equivalence between the set-theoretic definition (smallest closed superset) and the local condition (every open meets $A$)* — it is easy to use both formulations as if they were obviously the same, when in fact the equivalence is precisely the content of the theorem. The most common slip is **assuming the sequential characterization in a general topological space**: one writes "$x \in \overline{A}$, so there is a sequence in $A$ converging to $x$" without checking first countability, then bases a proof on this false statement. The fix is to either restrict attention to first-countable spaces, in which the sequential characterization is correct, or to upgrade to nets.

---

# Rederivation Scaffold

**High-level strategy:**
The chain of equivalences is purely complementation and definition-unwinding for the open-set, neighbourhood, basis, and neighbourhood-basis forms. The sequential form requires first countability and a diagonal-extraction construction.

**Subgoal decomposition:**

1. **(a)$\iff$(b): $x \in \overline{A}$ iff every open containing $x$ meets $A$.**
   - *Hint:* Negate both sides and observe the complement bijection between closed supersets of $A$ excluding $x$ and open sets containing $x$ missing $A$.
   - *Why needed:* Core equivalence; the others are repackagings.

2. **(b)$\iff$(c): every open meets $A$ iff every neighbourhood meets $A$.**
   - *Hint:* Every neighbourhood contains an open neighbourhood; every open containing $x$ is a neighbourhood.
   - *Why needed:* Linking the open-set form to the neighbourhood form.

3. **(c)$\iff$(d): every neighbourhood meets $A$ iff every basis-element containing $x$ meets $A$.**
   - *Hint:* Every basis element containing $x$ is open hence a neighbourhood; every neighbourhood contains an open containing $x$, which contains a basis element containing $x$.
   - *Why needed:* Refining the open-set test to a basis-level test, which is the practical form.

4. **(d)$\iff$(e) under first countability: every basis-element meets $A$ iff some sequence in $A$ converges to $x$.**
   - *Hint:* Forward — if $a_n \to x$, every neighbourhood eventually contains $a_n$, so meets $A$. Reverse — take a decreasing countable basis $B_n$ at $x$ and pick $a_n \in B_n \cap A$.
   - *Why needed:* The analytic / sequential characterization, conditional on first countability.

---

# Lemma Decomposition

> [!note]- Lemma 1: $X \setminus \overline{A} = (X \setminus A)^\circ$ — interior-closure duality
> **Statement:** $X \setminus \overline{A}$ is the *largest open subset of $X$ disjoint from $A$*.
>
> **Hint:** Both are characterized by "open and disjoint from $A$" with maximality.
>
> **Why needed:** Provides the bijection between closed supersets of $A$ excluding $x$ and open sets containing $x$ missing $A$.
>
> > [!note]- Full proof
> > Let $V = X \setminus \overline{A}$. Then $V$ is open (complement of closed) and disjoint from $A$ (since $V \subseteq X \setminus A$). For maximality, let $U$ be any open set disjoint from $A$. Then $X \setminus U$ is a closed set containing $A$, so it contains $\overline{A}$, so $U \subseteq X \setminus \overline{A} = V$. Hence $V$ is the largest such $U$, which is the definition of $(X \setminus A)^\circ$.

> [!note]- Lemma 2: Diagonal extraction in a first-countable space
> **Statement:** In a first-countable space, if $x$ has every neighbourhood meeting $A$, then there is a sequence $a_n \in A$ with $a_n \to x$.
>
> **Hint:** Take a *decreasing* countable basis at $x$ (obtainable by intersecting successive elements) and pick one element from $A$ in each.
>
> **Why needed:** It is the construction at the heart of the sequential characterization.
>
> > [!note]- Full proof
> > By first countability, there is a countable neighbourhood basis $\{B_n\}_{n \geq 1}$ at $x$. Replace $B_n$ by $\tilde B_n = B_1 \cap B_2 \cap \dots \cap B_n$ — still a neighbourhood of $x$ (finite intersection of neighbourhoods) and now decreasing. Each $\tilde B_n$ meets $A$ by hypothesis; pick $a_n \in \tilde B_n \cap A$.
> >
> > Claim $a_n \to x$. Let $N$ be any neighbourhood of $x$; it contains some $\tilde B_{n_0}$. For $n \geq n_0$, $a_n \in \tilde B_n \subseteq \tilde B_{n_0} \subseteq N$. So $a_n$ is eventually in $N$, which is the definition of convergence.

> [!note]- Lemma 3: Counterexample — closure exceeds sequential closure in $\omega_1 + 1$
> **Statement:** Let $X = \omega_1 + 1 = [0, \omega_1]$ be the space of ordinals up to and including the first uncountable, with the order topology. Let $A = [0, \omega_1)$ be the proper initial segment. Then $\omega_1 \in \overline{A}$ (so $\overline{A} = X$), but no sequence in $A$ converges to $\omega_1$.
>
> **Hint:** A countable sequence of countable ordinals has a countable supremum, strictly less than $\omega_1$.
>
> **Why needed:** It shows first countability is necessary for the sequential characterization. The space $\omega_1 + 1$ is not first countable at $\omega_1$ — it has no countable neighbourhood basis there.
>
> > [!note]- Full proof
> > *$\omega_1 \in \overline{A}$.* Every neighbourhood of $\omega_1$ in the order topology contains an interval $(\alpha, \omega_1]$ for some $\alpha < \omega_1$; this interval contains ordinals $\beta \in (\alpha, \omega_1)$, which are in $A$. So every neighbourhood of $\omega_1$ meets $A$, and $\omega_1 \in \overline{A}$.
> >
> > *No sequence in $A$ converges to $\omega_1$.* Suppose $\{a_n\} \subseteq A$ is a sequence with $a_n \to \omega_1$. Each $a_n < \omega_1$ is a countable ordinal, so $\sup_n a_n$ is the countable supremum of countable ordinals, which is itself a countable ordinal, say $\sigma < \omega_1$. The interval $(\sigma, \omega_1]$ is an open neighbourhood of $\omega_1$, and no $a_n$ is in it (each $a_n \leq \sigma$). So $a_n$ does not converge to $\omega_1$, a contradiction. Hence no sequence in $A$ converges to $\omega_1$.
> >
> > This is the canonical first-not-second-countable failure: $\omega_1 + 1$ is *compact Hausdorff* but not first countable at $\omega_1$, and the sequential closure of $A$ is $A$ itself while the topological closure is $X$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $X$ be a topological space, $A \subseteq X$, $x \in X$.
>
> **(a)$\iff$(b).** ($\Rightarrow$) Suppose $x \in \overline{A}$ and let $U$ be an open set containing $x$. If $U \cap A = \emptyset$ then $X \setminus U$ is closed and contains $A$, so $\overline{A} \subseteq X \setminus U$, i.e. $x \notin U$, contradicting $x \in U$. So $U \cap A \neq \emptyset$. ($\Leftarrow$) Suppose every open set containing $x$ meets $A$. If $x \notin \overline{A}$, the open set $X \setminus \overline{A}$ contains $x$ and misses $A$ (since $A \subseteq \overline{A}$), contradiction. So $x \in \overline{A}$.
>
> **(b)$\iff$(c).** ($\Rightarrow$) A neighbourhood $N$ of $x$ contains an open $U$ with $x \in U$; $U \cap A \neq \emptyset$ by (b), and $U \cap A \subseteq N \cap A$. So $N \cap A \neq \emptyset$. ($\Leftarrow$) An open set $U$ containing $x$ is itself a neighbourhood of $x$.
>
> **(c)$\iff$(d).** ($\Rightarrow$) A basis element $B$ containing $x$ is open hence a neighbourhood of $x$; $B \cap A \neq \emptyset$ by (c). ($\Leftarrow$) Let $N$ be a neighbourhood of $x$; it contains an open $U$ with $x \in U$, and $U$ is a union of basis elements, one of which $B$ contains $x$ and is $\subseteq U$. $B \cap A \neq \emptyset$ by (d), and $B \cap A \subseteq U \cap A \subseteq N \cap A$.
>
> **First countable: (c)$\iff$(e), where (e) is "some sequence in $A$ converges to $x$".**
> ($\Leftarrow$) If $a_n \in A$ and $a_n \to x$, then for any neighbourhood $N$ of $x$, $a_n \in N$ for all $n \geq N_0$, so $N \cap A \neq \emptyset$.
> ($\Rightarrow$) By first countability and Lemma 2, the construction $a_n \in \tilde B_n \cap A$ on a decreasing countable basis gives the required sequence.
> $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Compute $\overline{\mathbb{Q}}$ in the Sorgenfrey line.** The Sorgenfrey topology has basis $\{[a, b) : a < b\}$. To check $x \in \overline{\mathbb{Q}}$: every basis element $[a, b)$ containing $x$ has $a \leq x < b$, and any such interval contains a rational. So $\overline{\mathbb{Q}} = \mathbb{R}$ in the Sorgenfrey topology — same answer as in the standard topology. The application battle-tests the basis-element form of the characterization in a different topology.

**Functions agreeing on a dense subset.** If $f, g : \mathbb{R} \to \mathbb{R}$ are continuous and agree on $\mathbb{Q}$, then $f = g$ on all of $\mathbb{R}$. Use the closure characterization plus the fact that the equalizer set $\{x : f(x) = g(x)\}$ is closed (preimage of the closed diagonal in $\mathbb{R}^2$). This is the standard "density-as-strategy" application of the characterization.

**Closure under group operations.** In a topological group $G$, the closure of a subgroup $H \leq G$ is itself a subgroup. *Proof:* the map $G \times G \to G$, $(x, y) \mapsto xy^{-1}$, is continuous; using $f(\overline{A} \times \overline{A}) \subseteq \overline{f(A \times A)}$ (a consequence of the closure characterization applied to the continuous image), $\overline{H} \cdot \overline{H}^{-1} \subseteq \overline{H \cdot H^{-1}} \subseteq \overline{H}$, so $\overline{H}$ is closed under the group operation. This is the topological algebraic input to the theory of Lie subgroups.

**Closure equals closure of a sequential dense subset.** In a first-countable space, if $A$ is dense, then for every $x \in X$ there is a sequence $a_n \in A$ converging to $x$. Use this to prove that the Lebesgue integral of a continuous function on $[0, 1]$ equals the Riemann integral, by approximating $f$ by step functions on rationals and using the sequential characterization to pass to the limit.

---

# Bridges

- **[[Def - Closure, Interior, and Boundary]]** — the definitions being characterized. The characterization theorem is the operational extension of the definition.

- **[[Def - Dense Subset]]** — a set $A$ is dense iff $\overline{A} = X$, iff every nonempty open set meets $A$. This characterization-of-density via the open-set form of closure is the most-used reformulation of density.

- **[[Def - First and Second Countable]]** — first countability is precisely the condition that makes the sequential characterization valid. The dependence is exact: sequential closure = closure iff first countable (in the sense of *needing* first countability, not just it being sufficient at any point).

- **[[Thm - Closure-in-Subspace Formula]]** — uses the basis-element characterization to derive the formula $\overline{A}^Y = \overline{A}^X \cap Y$ for the closure of $A$ in a subspace.

- **[[Topology I — §1–3 Metric and Topological Spaces|Net convergence in §6 of Topology II]]** — the substitute for sequences in non-first-countable spaces. Nets recover the sequential-style characterization without any first-countability hypothesis.

---

# Unlocked by This

> [!tip] Density-Continuity Uniqueness *(in this topic)*
> Two continuous functions agreeing on a dense subset of $X$ agree on all of $X$, provided the target is Hausdorff. This is one of the most-used corollaries: density plus continuity forces global determination. The closure characterization is the engine — the set where the functions agree is closed and contains the dense subset, hence contains the closure of the dense subset, hence everything.

> [!tip] Nets and Filter Convergence *(from Topology II, §6)*
> When first countability fails, the sequential characterization of closure also fails. The remedy is a generalization of sequences: **nets** (Moore–Smith sequences) or, equivalently, filters. A net is a function from a directed set into $X$, and net convergence captures closure in *any* topological space. See [[Topology II — §4–7 Connectivity, Separation, Nets, Compactness]] §6.

> [!tip] Stone–Čech Compactification *(from Topology III)*
> The **Stone–Čech compactification** $\beta X$ of a Tychonoff space $X$ is the "biggest" compactification, characterized by the universal property that every continuous map from $X$ into a compact Hausdorff space extends uniquely to $\beta X$. The points of $\beta X \setminus X$ are limits of "ultrafilters" on $X$, not of sequences — $\beta X$ is highly non-first-countable, and many of the boundary points have no sequence in $X$ converging to them. The Stone–Čech construction is the most-used non-first-countable example in advanced topology.
