---
type: exercise
subject: topology
difficulty: "⭐⭐"
prereqs:
  - "Def - Directed Set and Net"
  - "Def - Subnet and Universal Net"
tags: [analysis, topology, nets]
---

# Problem Statement

A sequence $\{x_n\}_{n \in \mathbb{N}}$ in a topological space $X$ is a net indexed by the directed set $\mathbb{N}$ with the usual order. The net is **universal** if for every subset $A \subseteq X$, the net is eventually in $A$ or eventually in $X \setminus A$.

Show that a sequence $\{x_n\}$ in any topological space $X$ is universal if and only if it is eventually constant — that is, there exist $N$ and $c \in X$ such that $x_n = c$ for all $n \geq N$.

**Recall:**

![[Def - Directed Set and Net#The Definition]]

![[Def - Subnet and Universal Net#The Definition]]

A net $\Phi : D \to X$ is **eventually in $A$** if there exists $\alpha_0 \in D$ such that $\Phi(\beta) \in A$ for all $\beta \geq \alpha_0$. It is **frequently in $A$** if for every $\alpha \in D$ there is $\beta \geq \alpha$ with $\Phi(\beta) \in A$.

For a sequence (the case $D = \mathbb{N}$), "eventually in $A$" means "there is $N$ such that $x_n \in A$ for all $n \geq N$"; "frequently in $A$" means "infinitely many $x_n$ are in $A$".

---

# Convergent Strategy

**Problem class.** A *both-directions* characterization: showing that for sequences, the universal property collapses to triviality. This is a *negative* result about the power of universal nets when restricted to sequences, and it is the motivation for introducing nets at all.

**Assumption pattern.** Forward direction: assume universality; derive eventual constancy. Reverse direction: assume eventual constancy; verify universality. The forward direction is the substantive one — we extract the eventual constant from the universal property.

**Theorem routing.** No external theorems needed; just the definitions of "universal" and "eventually constant", and basic logic about "eventually" vs. "frequently" for sequences.

**Key decision point.** For the forward direction, the move is to consider the set $A = \{c\}$ for various candidate $c$. If the sequence takes infinitely many distinct values, then for some value $c$ taken infinitely often, the sequence is frequently in $\{c\}$ but also frequently in the complement (since other values are also taken infinitely often). Then *neither* eventually-in-$\{c\}$ nor eventually-in-$X\setminus\{c\}$ holds — contradicting universality.

---

# Legal Operations Used

This solution deploys the following legal operations from the [[Topology II — §4–7 Connectivity, Separation, Nets, Compactness#Legal Operations|topic page's Legal Operations]]:

1. **Use the dichotomy "frequently in $A$ XOR eventually in $X \setminus A$".** For *any* net, the statements "eventually in $A$" and "frequently in $X \setminus A$" are complementary: a net is *not* eventually in $A$ iff it is frequently in $X \setminus A$.

2. **Test universality against a probing set.** Universality means "for *every* set $A$, dichotomy holds". To violate it, exhibit a single set against which it fails. To use it, pick a strategically chosen set.

3. **Reduce to value sets in a discrete sequence.** A sequence's values form a (possibly small) subset of $X$; the question of "is eventually in $A$" reduces to a question about indices $n$ such that $x_n \in A$. This converts a topological question into a purely set-theoretic one about how the values are distributed across $\mathbb{N}$.

---

# Hints

> [!note]- Hint 1
> Reverse direction first (easier): if $x_n = c$ for $n \geq N$, then for any $A \subseteq X$, either $c \in A$ (the sequence is eventually in $A$, with witness $N$) or $c \in X \setminus A$ (the sequence is eventually in $X \setminus A$, with witness $N$). So the sequence is universal.

> [!note]- Hint 2
> Forward direction. Suppose the sequence is universal and *not* eventually constant. Then for every value $c$, the sequence is *not* eventually equal to $c$. Show this implies there is a value $c$ such that the sequence is frequently in $\{c\}$ and frequently in $X \setminus \{c\}$ — and use this to violate universality.

> [!note]- Hint 3
> If the sequence is not eventually constant, two cases: (i) it takes infinitely many distinct values, (ii) it takes finitely many distinct values but no single value is the eventual one.
>
> *Case (i).* Pick any value $c$ taken by the sequence. The complement values are also taken — and either $\{c\}$ is hit infinitely often or it isn't. By a pigeonhole-style argument, two distinct values are both hit infinitely often. Pick $c$ to be one of them: the sequence is frequently in $\{c\}$ (infinitely often $x_n = c$) and frequently in $X \setminus \{c\}$ (infinitely often $x_n \neq c$). So neither eventually-in-$\{c\}$ nor eventually-in-$X \setminus \{c\}$ — contradiction.
>
> *Case (ii).* Finitely many values, no eventual one. Then at least *two* values are taken infinitely often (else, the one infinitely-often value would be the eventual one). The same argument as case (i) applies.

---

# Solution

The point of this exercise is to show that for sequences, the universal net property is vacuous: it forces the sequence to be eventually constant, and then there is nothing more for the "universal" structure to say. This is why universal subnets — but not universal subsequences — are needed for the convergent-subnet characterization of compactness.

**Step 1: Reverse direction — eventually constant $\Rightarrow$ universal.**

Suppose $x_n = c$ for all $n \geq N$. For any $A \subseteq X$, either $c \in A$ or $c \in X \setminus A$. In the first case the sequence is eventually in $A$ (with witness $N$); in the second case it is eventually in $X \setminus A$ (with witness $N$).

> [!note]- Derivation
> Take any $A \subseteq X$. Two cases:
>
> *$c \in A$.* For all $n \geq N$, $x_n = c \in A$. So the sequence is eventually in $A$.
>
> *$c \notin A$, i.e., $c \in X \setminus A$.* For all $n \geq N$, $x_n = c \in X \setminus A$. So the sequence is eventually in $X \setminus A$.
>
> In either case the universal dichotomy holds, so the sequence is universal.

**Step 2: Forward direction — assume universal, show eventually constant.**

Suppose $\{x_n\}$ is universal but *not* eventually constant. We will derive a contradiction by exhibiting a set $A$ for which neither "eventually in $A$" nor "eventually in $X \setminus A$" holds.

> [!note]- Derivation
> Since the sequence is not eventually constant, for every $c \in X$ and every $N$, there is some $n \geq N$ with $x_n \neq c$. Equivalently: for every $c$ and every $N$, $\{n \geq N : x_n \neq c\} \neq \emptyset$.
>
> *Substep 1: Some value is taken infinitely often.* Consider the set of values $V = \{x_n : n \in \mathbb{N}\}$. If $V$ is finite, then by pigeonhole, some value $c \in V$ is taken infinitely often. If $V$ is infinite, then the sequence cannot be eventually constant either — but it may not have any value taken infinitely often (e.g., $x_n = n$ in $\mathbb{N}$). We handle both cases together below.
>
> *Substep 2: Locate a value $c$ where the dichotomy fails.* We want to find a single set $A$ for which the universal dichotomy is violated. Consider any value $c$ taken infinitely often (if one exists) — set $A = \{c\}$. Then:
>
> - The sequence is *frequently* in $\{c\}$ (infinitely often), so it is *not eventually* in $X \setminus \{c\}$.
> - We claim the sequence is *not eventually* in $\{c\}$ either, because of the not-eventually-constant assumption: there is no $N$ such that $x_n = c$ for all $n \geq N$ (else the sequence would be eventually constant equal to $c$).
>
> So the dichotomy "eventually in $\{c\}$ or eventually in $X \setminus \{c\}$" fails for this $A = \{c\}$, contradicting universality.
>
> *Handling the case where no value is taken infinitely often.* If no value $c$ is taken infinitely often, then for every $c$ the set $\{n : x_n = c\}$ is finite. List the values in order of first appearance: $v_1 = x_{n_1}, v_2 = x_{n_2}, \ldots$, with $n_1 < n_2 < \ldots$ chosen as the first index where each new distinct value appears. The set $A = \{v_1, v_3, v_5, \ldots\}$ (every other value) gives a sequence frequently in $A$ (infinitely often, at indices where one of these values appears) and frequently in $X \setminus A$ (at indices for the even-indexed values $v_2, v_4, \ldots$). So neither eventually-in-$A$ nor eventually-in-$X \setminus A$ holds — contradicting universality.
>
> In every case we have a contradiction. So a universal sequence must be eventually constant.

> [!note]- Complete formal solution
> *Reverse:* If $x_n = c$ for $n \geq N$, then for any $A$, either $c \in A$ (eventually in $A$, with $N$) or $c \notin A$ (eventually in $X \setminus A$, with $N$). So the sequence is universal.
>
> *Forward:* Suppose $\{x_n\}$ is universal and not eventually constant. Two cases.
>
> *Case A: some value $c$ is taken infinitely often.* Set $A = \{c\}$. Since $x_n = c$ for infinitely many $n$, the sequence is *frequently* in $\{c\}$, hence *not eventually* in $X \setminus \{c\}$. Since the sequence is not eventually constant, $\{n : x_n \neq c\}$ is infinite, so the sequence is *frequently* in $X \setminus \{c\}$, hence *not eventually* in $\{c\}$. Both fail, contradicting universality.
>
> *Case B: every value is taken finitely often.* List distinct values $v_1, v_2, \ldots$ by first appearance (their number is infinite by case-A negation). Set $A = \{v_1, v_3, v_5, \ldots\}$. Since each $v_{2k+1}$ is taken at least once (at index $n_{2k+1}$), the sequence is frequently in $A$; since each $v_{2k}$ is taken at least once, frequently in $X \setminus A$. Both fail.
>
> Both cases contradict universality. Hence universal $\Rightarrow$ eventually constant. $\blacksquare$

---

# Key Takeaways

**Universality is a strong property — strong enough that it forces a sequence to be eventually constant, which is essentially trivial.** This is *why* nets exist: the universal net property is genuinely useful only in the broader directed-set indexing. With $\mathbb{N}$ as the indexing set, the universal property captures only the most boring sequences (eventually constant), and so universal *subsequences* are useless for proving anything non-trivial. Universal *subnets*, by contrast, exist for every net (Bredon's Theorem 6.13, using Zorn's lemma) and are the linchpin of the convergent-subnet characterization of compactness in non-metric spaces. The lesson: when the source axiom is too restrictive in a given indexing, the *fix* is to enrich the indexing — directed sets over $\mathbb{N}$ is the canonical such fix, and the payoff is that universality becomes a useful tool.

**The dichotomy "eventually in $A$ or eventually in $X \setminus A$" is *not* a tautology for general sets and general nets; it is a strong commitment.** The standard logical dichotomy is "every $x$ is in $A$ or in $X \setminus A$". But for a *sequence's behaviour*, the analogous dichotomy is "the sequence is eventually in $A$ XOR eventually in $X \setminus A$" — and this fails as soon as the sequence is frequently in both $A$ and $X \setminus A$ (which is the typical case for non-trivial sequences). The universal net property demands that this dichotomy hold for *every* $A$, which is what makes it so strong. Recognizing this structural difference — between "every term is in $A$ or $X \setminus A$" and "the sequence is eventually in $A$ or eventually in $X \setminus A$" — is essential for working with universal nets.

**The trigger "want to make every set-question dichotomous" maps to "extract a universal subnet".** When solving compactness or convergence problems via subnets, the discipline is: take an arbitrary net, extract a universal subnet (existence guaranteed by Bredon's theorem), and from then on every subset $A \subseteq X$ provides a dichotomy. This converts open-cover questions into convergence questions, because the universal subnet either converges (to some point in $X$) or fails to do so in a very specific way (it is eventually in the complement of every open neighbourhood of every point, which contradicts compactness). The universal subnet is the *one* tool that makes the cover-vs-net equivalence work cleanly.

**Universal nets generalize selectors / ultrafilters, and the same trick (using Zorn's lemma) provides both.** A universal net on $X$ corresponds to an ultrafilter on $X$: the collection $\{A \subseteq X : \text{net is eventually in } A\}$ forms an ultrafilter, and conversely every ultrafilter gives rise to a universal net. The construction is the same: take the maximal filter (collection of sets the net is frequently in), and the universal-net dichotomy is exactly the ultrafilter property "for every $A$, $A$ or $X \setminus A$ is in the filter". This is why universal nets are equivalent (in their construction) to the existence of ultrafilters, which is equivalent to the Axiom of Choice. The same Zorn-lemma move appears in the existence of maximal ideals, in Tychonoff's theorem (via universal nets), and in the Hahn-Banach theorem — recognize the pattern across functional analysis, algebra, and topology.
