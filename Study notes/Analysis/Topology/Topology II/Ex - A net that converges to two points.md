---
type: exercise
subject: topology
difficulty: "⭐⭐"
prereqs:
  - "Def - Separation Axioms"
  - "Def - Directed Set and Net"
  - "Def - Net Convergence"
  - "Thm - Hausdorff Iff Unique Net Limits"
tags: [analysis, topology, nets, counterexample]
---

# Problem Statement

In a non-Hausdorff space, a convergent net can have more than one limit. Construct an explicit such example as follows. Let $X = \mathbb{N}$ equipped with the cofinite topology (where open sets are $\emptyset$ together with all subsets having finite complement). Then $X$ is $T_1$ but not Hausdorff (as in [[Ex - A T1 space that is not Hausdorff]]).

**Construct an explicit net $\Phi : D \to X$ that converges to two distinct points $0$ and $1$ in $X$.**

Hint: use the directed set $D = \{(U, V) : U, V \text{ are open neighbourhoods of } 0, 1 \text{ in } X\}$, ordered by $(U', V') \geq (U, V)$ iff $U' \subseteq U$ and $V' \subseteq V$. For each $(U, V) \in D$, set $\Phi(U, V)$ to be any element of $U \cap V$. Show $D$ is directed, that such an element exists, and that $\Phi$ converges to both $0$ and $1$.

**Recall:**

![[Def - Separation Axioms#The Definition]]

![[Def - Directed Set and Net#The Definition]]

![[Def - Net Convergence#The Definition]]

![[Thm - Hausdorff Iff Unique Net Limits#Formal Statement]]

In the cofinite topology on $\mathbb{N}$, every nonempty open set has finite complement (so contains all but finitely many elements). Intersections of finitely many cofinite sets are cofinite, in particular nonempty.

---

# Convergent Strategy

**Problem class.** Direct construction of a *named counterexample* showing the necessity of Hausdorff for uniqueness of net limits. The construction is a model for "make a directed set out of pairs of neighbourhoods", which is itself a model for the proof of [[Thm - Hausdorff Iff Unique Net Limits]] in the reverse direction.

**Assumption pattern.** The cofinite topology on $\mathbb{N}$ provides a non-Hausdorff space where any two nonempty opens intersect — which is exactly what we need: pick a point in the intersection of any two neighbourhood pairs.

**Theorem routing.** No prior theorems beyond the cofinite topology being non-Hausdorff (proved in [[Ex - A T1 space that is not Hausdorff]]) and the existence of points in intersections of cofinite sets. The construction itself is essentially the construction used in the proof of [[Thm - Hausdorff Iff Unique Net Limits]].

**Key decision point.** The directed set $D$ is ordered by *reverse inclusion in each coordinate*: smaller neighbourhood pairs are "later" in the ordering. This is the canonical way to make a directed set out of neighbourhood pairs: as you go further in the directed set, your pairs of neighbourhoods get smaller and smaller, "closing in" on the two target points simultaneously. The net then is forced to enter both arbitrarily small neighbourhood pairs.

---

# Legal Operations Used

This solution deploys the following legal operations from the [[Topology II — §4–7 Connectivity, Separation, Nets, Compactness#Legal Operations|topic page's Legal Operations]]:

1. **Construct a directed set from a partially-ordered family of "approximations".** Pairs of neighbourhoods of two target points, ordered by joint shrinking, is the canonical directed set for showing simultaneous convergence to both.

2. **Use intersection-nonemptiness in a non-Hausdorff topology.** The defining feature of a non-Hausdorff space is that some pair of points has every pair of their neighbourhoods intersecting. Exploit this to define a net by selection from these nonempty intersections.

3. **Reverse-inclusion ordering on neighbourhoods.** The standard ordering on a neighbourhood basis to make it directed and compatible with convergence is reverse inclusion: smaller neighbourhoods are "later". The net's eventual containment in a fixed small neighbourhood then follows from any later neighbourhood being smaller.

---

# Hints

> [!note]- Hint 1
> Show that the proposed $D$ is a directed set. Given $(U_1, V_1)$ and $(U_2, V_2)$, what is a common upper bound? Take $U_1 \cap U_2$ and $V_1 \cap V_2$ — these are intersections of opens, hence open. Both contain $0$ (resp.~$1$). So $(U_1 \cap U_2, V_1 \cap V_2) \geq (U_1, V_1)$ and $\geq (U_2, V_2)$ in the order.

> [!note]- Hint 2
> Show that $\Phi(U, V) \in U \cap V$ is well-defined: $U$ is a cofinite neighbourhood of $0$ and $V$ is a cofinite neighbourhood of $1$, both are cofinite subsets of $\mathbb{N}$, and the intersection of cofinite subsets of an infinite set is cofinite hence nonempty. So an element exists.

> [!note]- Hint 3
> To show $\Phi \to 0$: take any neighbourhood $W$ of $0$. The element $\alpha_0 = (W, \mathbb{N}) \in D$ has the property that for any $(U, V) \geq (W, \mathbb{N})$, $U \subseteq W$, so $\Phi(U, V) \in U \cap V \subseteq U \subseteq W$. Hence $\Phi$ is eventually in $W$.
>
> By symmetry, $\Phi \to 1$ similarly: take $\alpha_0 = (\mathbb{N}, W)$ for $W$ a neighbourhood of $1$.

---

# Solution

The construction is the canonical "directed set of pairs of neighbourhoods" trick. It is also exactly the construction used in the reverse direction of [[Thm - Hausdorff Iff Unique Net Limits]] — non-Hausdorff implies non-unique net limits.

**Step 1: Verify $D$ is a directed set.**

The set $D = \{(U, V) : U \text{ open neighbourhood of } 0, V \text{ open neighbourhood of } 1\}$, ordered by $(U', V') \geq (U, V)$ iff $U' \subseteq U$ and $V' \subseteq V$, is a directed set.

> [!note]- Derivation
> *Reflexivity and antisymmetry.* The relation is a partial order: reflexive ($U \subseteq U$), antisymmetric (if $U' \subseteq U$ and $U \subseteq U'$ then $U = U'$, similarly for $V$), and transitive.
>
> *Directed.* Given $(U_1, V_1), (U_2, V_2) \in D$. Set $U = U_1 \cap U_2$ and $V = V_1 \cap V_2$. Both intersections are intersections of finitely many open sets, hence open. Both contain $0$ (since $U_1, U_2 \ni 0$) and $1$ (since $V_1, V_2 \ni 1$). So $(U, V) \in D$.
>
> We have $U = U_1 \cap U_2 \subseteq U_1$ and $V = V_1 \cap V_2 \subseteq V_1$, so $(U, V) \geq (U_1, V_1)$. Similarly $(U, V) \geq (U_2, V_2)$. So $(U, V)$ is an upper bound for both, proving $D$ is directed.

**Step 2: The function $\Phi$ is well-defined.**

For each $(U, V) \in D$, the intersection $U \cap V$ is nonempty in the cofinite topology on $\mathbb{N}$, so we can pick $\Phi(U, V) \in U \cap V$.

> [!note]- Derivation
> $U$ is a nonempty open in $\mathbb{N}$ (contains $0$), so its complement is finite; similarly $V$ has finite complement. Then
> $$\mathbb{N} \setminus (U \cap V) = (\mathbb{N} \setminus U) \cup (\mathbb{N} \setminus V)$$
> is a union of two finite sets, hence finite. Since $\mathbb{N}$ is infinite, $U \cap V$ is cofinite, in particular nonempty.
>
> By the axiom of choice (or by an explicit selection: pick the smallest natural number in $U \cap V$), we can define $\Phi(U, V)$ to be some element of $U \cap V$ for every $(U, V) \in D$.

**Step 3: $\Phi$ converges to $0$.**

For every open neighbourhood $W$ of $0$ in $X = \mathbb{N}$, $\Phi$ is eventually in $W$.

> [!note]- Derivation
> Fix any open $W \ni 0$. Take $\alpha_0 = (W, \mathbb{N}) \in D$ (note: $\mathbb{N}$ is an open neighbourhood of $1$, being the whole space).
>
> For any $\beta = (U, V) \in D$ with $\beta \geq \alpha_0$, we have $U \subseteq W$ and $V \subseteq \mathbb{N}$ (the second is automatic). Then $\Phi(\beta) = \Phi(U, V) \in U \cap V \subseteq U \subseteq W$. So $\Phi(\beta) \in W$ for all $\beta \geq \alpha_0$, i.e., $\Phi$ is eventually in $W$.
>
> Since this holds for every open neighbourhood $W$ of $0$, $\Phi$ converges to $0$.

**Step 4: $\Phi$ converges to $1$.**

By the symmetric argument, $\Phi$ converges to $1$.

> [!note]- Derivation
> Fix any open $W \ni 1$. Take $\alpha_0 = (\mathbb{N}, W) \in D$. For $\beta = (U, V) \geq \alpha_0$, $U \subseteq \mathbb{N}$ (automatic) and $V \subseteq W$. Then $\Phi(\beta) \in U \cap V \subseteq V \subseteq W$. So $\Phi$ is eventually in $W$, and converges to $1$.

Hence $\Phi$ converges to both $0$ and $1$, confirming that the cofinite topology on $\mathbb{N}$ is not Hausdorff in the strongest possible sense: even nets have non-unique limits.

> [!note]- Complete formal solution
> Take $X = \mathbb{N}$ with the cofinite topology. Let
> $$D = \{(U, V) : U \text{ open}, 0 \in U, V \text{ open}, 1 \in V\}$$
> with $(U', V') \geq (U, V) \iff U' \subseteq U$ and $V' \subseteq V$.
>
> *D is directed.* The pair $(U_1 \cap U_2, V_1 \cap V_2)$ is an upper bound: both coordinates are open (finite intersection of opens), contain the right base point, and are componentwise smaller, hence above each $(U_i, V_i)$.
>
> *$\Phi$ is well-defined.* For $(U, V) \in D$, $U$ and $V$ are cofinite, so $U \cap V$ is cofinite, hence nonempty. Choose $\Phi(U, V) \in U \cap V$.
>
> *$\Phi \to 0$.* For any open $W \ni 0$, set $\alpha_0 = (W, \mathbb{N})$. For $\beta = (U, V) \geq \alpha_0$, $U \subseteq W$, so $\Phi(\beta) \in U \subseteq W$. Eventually in $W$.
>
> *$\Phi \to 1$.* Symmetric, with $\alpha_0 = (\mathbb{N}, W)$.
>
> Hence $\Phi$ converges to both $0$ and $1$. $\blacksquare$

---

# Key Takeaways

**The directed set of "pairs of shrinking neighbourhoods around two points" is the canonical machine for forcing a net to converge to both points simultaneously.** This construction is one of the most important in net theory. It works whenever the two points cannot be separated by disjoint opens: their pairs of neighbourhoods all intersect, and you can choose a witness point in each intersection. As the neighbourhood pairs shrink (along the directed-set ordering), the chosen points are eventually in every fixed neighbourhood of either base point. The trigger for this construction: any time you want a net converging to multiple specified targets in a non-Hausdorff setting.

**Non-Hausdorff is exactly the property that this kind of multi-limit net can be constructed; the converse is also true (every non-unique-limit net comes from a non-Hausdorff topology).** This is the content of [[Thm - Hausdorff Iff Unique Net Limits]]. The forward direction is easy (in Hausdorff, disjoint neighbourhoods rule out simultaneous eventual containment in both). The reverse — what we have done here — is the construction in this exercise, lifted from the special case ($\mathbb{N}$ with cofinite) to an arbitrary non-Hausdorff space. The exercise is the *prototype proof* of the reverse direction.

**The trigger "want a net with these prescribed limit properties" maps to "take the directed set of conditions, order it consistently, select a witness for each".** This pattern shows up across topology, functional analysis, and set theory whenever you need a net or sequence with structural properties: ordered by inclusion, refinement, or pointwise dominance. The witness selection requires the Axiom of Choice in general (Bredon implicitly uses it for $\Phi$), unless the topology is countable enough to choose witnesses explicitly. In this exercise, the cofinite topology on $\mathbb{N}$ is countable enough that we could select $\Phi(U, V) =$ the smallest element of $U \cap V$ without Choice.

**Reverse-inclusion ordering on a neighbourhood basis is the "convergent" ordering — it makes "small neighbourhoods are late" so that the net catches up to the limit as it advances.** This is structurally why nets work where sequences fail: the indexing set can be ordered by arbitrary refinement, and the net's behaviour at "late" stages reflects its behaviour in "small" neighbourhoods, which is precisely what convergence demands. Sequences are stuck with $\mathbb{N}$, which has only one direction (increasing) and only countably many stages, so they cannot detect uncountable-basis phenomena (see [[Ex - A closure point not reached by any sequence]] for the canonical example). The "directed set of refining approximations" idea is the abstract content that nets exist to capture.
