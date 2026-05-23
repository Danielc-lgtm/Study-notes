---
type: exercise
subject: differential-geometry
difficulty: "⭐⭐"
prereqs:
  - "Def - Smooth Manifold"
  - "Def - Partition of Unity on a Manifold"
  - "Def - Bump Function and Smooth Cutoff"
  - "Thm - Existence of Smooth Bump Functions"
tags: [geometry, differential-geometry]
---

# Problem Statement

Let $M$ be a smooth manifold and let $\{U_1, U_2, \ldots, U_k\}$ be a *finite* open cover of $M$ (where we further assume that $M$ is compact, or that the supports of the eventual bumps will be compactly contained in some larger set, so that the finiteness is meaningful).

Construct an explicit smooth partition of unity $\{\psi_1, \psi_2, \ldots, \psi_k\}$ subordinate to this cover.

**Recall:**

A smooth partition of unity subordinate to $\{U_\alpha\}$ is:

![[Def - Partition of Unity on a Manifold#The Definition]]

The smooth bump function existence theorem (which we will use as a black box):

![[Thm - Existence of Smooth Bump Functions#Statement]]

This is a finite-cover version of the general existence theorem [[Thm - Existence of Smooth Partitions of Unity]], stripped of the paracompactness / refinement / re-indexing machinery. The construction is "bump-and-normalize" in its purest form.

---

# Convergent Strategy

**Problem class:** Construction of a partition of unity in the finite case — the canonical "bump-and-normalize" construction without the technical refinement step needed for infinite covers. This is the simplest non-trivial instance of [[Thm - Existence of Smooth Partitions of Unity]], chosen to expose the construction without the paracompactness machinery.

**Assumption pattern:** We have a finite open cover $\{U_1, \ldots, U_k\}$. Compactness of $M$ (or finiteness of the cover with a slight extra condition) makes the cover locally finite automatically. We need bumps on a closed shrinking — closed sets $C_i \subseteq U_i$ that still cover $M$.

**Theorem routing:** Step 1: shrink the cover to closed sets $C_i \subseteq U_i$ with $\bigcup_i C_i = M$ (using normality of $M$, which follows from paracompact Hausdorff). Step 2: build a smooth bump $\rho_i$ for $C_i$ supported in $U_i$ (using [[Thm - Existence of Smooth Bump Functions]]). Step 3: sum $\rho = \sum_i \rho_i$, observe it is smooth (finite sum) and positive (each $p \in C_i$ for some $i$, giving $\rho_i(p) = 1$, so $\rho \geq 1$). Step 4: normalize $\psi_i = \rho_i / \rho$ and verify the partition-of-unity axioms.

**Key decision point:** The non-obvious move is the *closed shrinking* (Step 1). The naive approach — directly apply the bump-function theorem to $U_i$ itself — fails because there is no closed subset of $U_i$ to bump up on, and so the resulting bump might not produce a positive sum. The closed shrinking is what makes $\sum_i \rho_i \geq 1$, hence positive, hence allows normalization. The shrinking step is the same as in the topological partition-of-unity proof (Lemma 1 of [[Thm - Paracompact Has Partitions of Unity]]). For *finite* covers, the shrinking is much simpler than in the general case (no Zorn's lemma needed), but it is still the key step.

---

# Legal Operations Used

1. **Apply the smooth partition of unity existence theorem to globalize (operation 5 from the topic page).** In this exercise we construct the partition explicitly rather than invoking the theorem, but the construction *is* the proof of the theorem in the finite case.

2. **Construct smooth real-valued functions via the $e^{-1/t}$ germ (operation 4 from the topic page).** The bump functions $\rho_i$ are built from this germ.

3. **Use bump functions to localize / cut off (operation 7 from the topic page).** Each $\rho_i$ localizes the partition to the closed shrinkage $C_i$, supported in $U_i$.

---

# Hints

> [!note]- Hint 1
> The key step is the closed shrinking. Given the open cover $\{U_i\}$, find closed $C_i \subseteq U_i$ with $\bigcup_i C_i = M$. The naive choice $C_i = U_i$ doesn't satisfy "closed inside $U_i$"; you need to slightly shrink each $U_i$ to a closed set. Normality of $M$ (Hausdorff + paracompact) makes this possible.

> [!note]- Hint 2
> Once you have $C_i \subseteq U_i$ closed with $\bigcup_i C_i = M$, apply [[Thm - Existence of Smooth Bump Functions]] to each pair $(C_i, U_i)$: get a smooth bump $\rho_i : M \to [0, 1]$ with $\rho_i \equiv 1$ on $C_i$ and $\operatorname{supp}(\rho_i) \subseteq U_i$.

> [!note]- Hint 3
> Now sum $\rho = \sum_{i=1}^k \rho_i$. This is smooth (finite sum of smooth functions) and positive: every $p \in M$ is in some $C_i$, where $\rho_i(p) = 1$, so $\rho(p) \geq 1$.

> [!note]- Hint 4
> Normalize: $\psi_i = \rho_i / \rho$. Verify the partition-of-unity axioms: smooth (ratio of smooth functions, denominator positive), in $[0, 1]$ (each $\rho_i \leq \rho$), supports in $U_i$ (same as $\rho_i$), sum to $1$ (computation), locally finite (only finitely many functions in the family).

---

# Solution

The construction is "shrink + bump + sum + normalize", in four explicit steps. The non-obvious step is the closed shrinking; once you have it, the rest is direct calculation. The smoothness of the partition comes from the smoothness of the bumps and the positivity of the denominator.

**Step 1: closed shrinking.**

Construct closed sets $C_i \subseteq U_i$ for $i = 1, \ldots, k$ such that $\bigcup_i C_i = M$. We do this by induction on $i$.

*Base case ($i = 1$):* the set $\overline{M \setminus (U_2 \cup \cdots \cup U_k)} \subseteq U_1$ is closed and inside $U_1$, since outside $U_2 \cup \cdots \cup U_k$, the only cover element containing the points is $U_1$. Set $C_1' = \overline{M \setminus (U_2 \cup \cdots \cup U_k)} \subseteq U_1$. (More precisely, the set $\{p \in M : p \notin U_2 \cup \cdots \cup U_k\}$ is closed, contained in $U_1$, and disjoint from $U_2 \cup \cdots \cup U_k$.)

Set $C_1$ to be a closed neighbourhood of $C_1'$ in $U_1$ — by normality of $M$, find an open $V_1$ with $C_1' \subseteq V_1 \subseteq \overline{V_1} \subseteq U_1$, set $C_1 = \overline{V_1}$.

*Inductive step:* having constructed $C_1, \ldots, C_{i-1}$ with $C_j \subseteq U_j$ closed and $\bigcup_{j=1}^{i-1} C_j \cup \bigcup_{j=i}^k U_j = M$ (still covering with the remaining $U_j$'s), construct $C_i \subseteq U_i$ closed such that $\bigcup_{j=1}^{i} C_j \cup \bigcup_{j=i+1}^k U_j = M$. The construction is parallel to the base case: $C_i' = M \setminus (\bigcup_{j=1}^{i-1} C_j \cup \bigcup_{j=i+1}^k U_j)$ is closed and contained in $U_i$ (by the covering property of the previous step). Find a closed neighbourhood $C_i$ via normality.

After $k$ steps, $\bigcup_{j=1}^k C_j = M$.

> [!note]- Derivation
> The shrinking construction relies on normality of $M$, which holds because $M$ is Hausdorff and paracompact (paracompact Hausdorff $\Rightarrow$ normal — see [[Thm - Paracompact Implies Normal]]). For each step, normality lets us insert an open set $V_i$ with $C_i' \subseteq V_i \subseteq \overline{V_i} \subseteq U_i$ — separating the closed set $C_i'$ from the closed complement $M \setminus U_i$.
>
> The key invariant maintained throughout the induction: $\bigcup_{j=1}^{i-1} C_j \cup \bigcup_{j=i}^k U_j = M$. This is the "still covering with the remaining cover elements" property. It holds at $i = 1$ (the remaining union is the original cover, which covers $M$). It is maintained at each step: $C_i$ contains $C_i' = M \setminus (\bigcup_{j=1}^{i-1} C_j \cup \bigcup_{j=i+1}^k U_j)$, so adding $C_i$ to the union (and removing $U_i$ from the right side) keeps the union equal to $M$.
>
> After $k$ steps, the union $\bigcup_j C_j$ alone (with no more $U_j$'s on the right) covers $M$.

**Step 2: bump functions.**

For each $i$, apply [[Thm - Existence of Smooth Bump Functions]] to the pair $(C_i, U_i)$: obtain a smooth $\rho_i : M \to [0, 1]$ with $\rho_i \equiv 1$ on $C_i$ and $\operatorname{supp}(\rho_i) \subseteq U_i$.

> [!note]- Derivation
> Direct application of the bump-function theorem to each closed-open pair. Each $C_i$ is closed (constructed in Step 1), $U_i$ is open by hypothesis, and $C_i \subseteq U_i$. The theorem produces the smooth bump.

**Step 3: sum and verify positivity.**

Set $\rho = \sum_{i=1}^k \rho_i$. This is smooth (finite sum of smooth functions). For every $p \in M$, $p$ is in some $C_i$ (by Step 1), so $\rho_i(p) = 1$, hence $\rho(p) \geq \rho_i(p) = 1 > 0$.

> [!note]- Derivation
> Smoothness of $\rho$: a finite sum of smooth functions is smooth (no convergence issues, sum is pointwise finite by construction). Pointwise: $\rho(p) = \rho_1(p) + \cdots + \rho_k(p) \in \mathbb{R}$.
>
> Positivity: for any $p \in M$, $p \in C_j$ for some $j$. Then $\rho_j(p) = 1$, and all other $\rho_i(p) \geq 0$ (since $\rho_i$ takes values in $[0, 1]$). So $\rho(p) = \sum_i \rho_i(p) \geq \rho_j(p) = 1$.

**Step 4: normalize.**

Set $\psi_i = \rho_i / \rho$ for each $i$. Verify the partition-of-unity axioms:

1. **Smoothness:** $\psi_i = \rho_i / \rho$ is a ratio of smooth functions with positive denominator (from Step 3), hence smooth.

2. **Values in $[0, 1]$:** $0 \leq \rho_i \leq \rho$ (each term of the sum is at most the sum), so $0 \leq \psi_i \leq 1$.

3. **Support in $U_i$:** $\operatorname{supp}(\psi_i) = \operatorname{supp}(\rho_i / \rho)$. Since $\rho > 0$ everywhere, the zeros of $\psi_i$ are exactly the zeros of $\rho_i$. So $\{ \psi_i \neq 0\} = \{\rho_i \neq 0\}$, hence $\operatorname{supp}(\psi_i) = \overline{\{\psi_i \neq 0\}} = \overline{\{\rho_i \neq 0\}} = \operatorname{supp}(\rho_i) \subseteq U_i$.

4. **Local finiteness:** the family $\{\operatorname{supp}(\psi_i)\}_{i=1}^k$ is finite, hence locally finite trivially (any neighbourhood meets at most $k$ supports, a finite number).

5. **Sum to $1$:** $\sum_i \psi_i = \sum_i \rho_i / \rho = (\sum_i \rho_i)/\rho = \rho/\rho = 1$.

> [!note]- Derivation
> Each axiom verification:
>
> 1. The ratio $\rho_i / \rho$ is smooth on $M$ because both $\rho_i$ and $\rho$ are smooth, $\rho > 0$ everywhere, and division by a nonzero smooth function is a smooth operation.
>
> 2. For each $p \in M$, $\rho_i(p) \in [0, 1] \subseteq [0, \rho(p)]$ (since $\rho(p) \geq 1 \geq \rho_i(p)$). So $\psi_i(p) \in [0, 1]$.
>
> 3. Since $\rho(p) > 0$ for all $p$, $\psi_i(p) = 0 \Leftrightarrow \rho_i(p) = 0$. So the non-vanishing sets coincide, hence so do their closures (supports). Support of $\rho_i$ is in $U_i$ by Step 2, so support of $\psi_i$ is in $U_i$.
>
> 4. Trivial for finite families.
>
> 5. Pointwise computation: at each $p$, $\sum_i \psi_i(p) = \sum_i \rho_i(p)/\rho(p) = (\sum_i \rho_i(p))/\rho(p) = \rho(p)/\rho(p) = 1$.

> [!note]- Complete formal solution
> **Claim.** Let $M$ be a smooth manifold with a finite open cover $\{U_1, \ldots, U_k\}$. Then there exists a smooth partition of unity $\{\psi_1, \ldots, \psi_k\}$ subordinate to this cover.
>
> *Proof.*
>
> *Step 1: closed shrinking.* By induction on $i$, construct closed sets $C_i \subseteq U_i$ such that $\bigcup_{j=1}^i C_j \cup \bigcup_{j=i+1}^k U_j = M$ at every stage.
>
> At step $i$: the set $C_i' = M \setminus (\bigcup_{j=1}^{i-1} C_j \cup \bigcup_{j=i+1}^k U_j)$ is closed (complement of an open union) and contained in $U_i$ (since the previous union, together with $U_i$, covers $M$ by inductive hypothesis). By normality of $M$ (which follows from paracompact Hausdorff via [[Thm - Paracompact Implies Normal]]), find an open $V_i$ with $C_i' \subseteq V_i \subseteq \overline{V_i} \subseteq U_i$. Set $C_i = \overline{V_i}$. Then $C_i \supseteq V_i \supseteq C_i'$, so $\bigcup_{j=1}^i C_j \cup \bigcup_{j=i+1}^k U_j \supseteq C_i' \cup (\bigcup_{j=1}^{i-1} C_j \cup \bigcup_{j=i+1}^k U_j) = M$.
>
> After $k$ steps, $\bigcup_{j=1}^k C_j = M$.
>
> *Step 2: smooth bumps.* For each $i$, by [[Thm - Existence of Smooth Bump Functions]] applied to $(C_i, U_i)$, there exists a smooth $\rho_i : M \to [0, 1]$ with $\rho_i \equiv 1$ on $C_i$ and $\operatorname{supp}(\rho_i) \subseteq U_i$.
>
> *Step 3: sum.* Set $\rho = \sum_{i=1}^k \rho_i$, a smooth function. For every $p \in M$, $p \in C_j$ for some $j$, so $\rho(p) \geq \rho_j(p) = 1 > 0$.
>
> *Step 4: normalize.* Set $\psi_i = \rho_i / \rho$. Then:
> - Each $\psi_i$ is smooth (ratio with positive denominator);
> - $\psi_i \in [0, 1]$ (since $\rho_i \leq \rho$);
> - $\operatorname{supp}(\psi_i) = \operatorname{supp}(\rho_i) \subseteq U_i$ (since $\rho > 0$);
> - The family is finite, hence locally finite;
> - $\sum_i \psi_i = (\sum_i \rho_i)/\rho = \rho/\rho = 1$.
>
> So $\{\psi_1, \ldots, \psi_k\}$ is the required smooth partition of unity. $\quad\blacksquare$

---

# Key Takeaways

**The closed shrinking is the key step in any partition-of-unity construction.** The naive approach — apply bumps directly to the open cover — fails because the resulting sum may not be positive everywhere. The closed shrinking ensures that every point of $M$ is in some $C_i$ where $\rho_i = 1$, guaranteeing $\sum \rho_i \geq 1 > 0$ and licensing normalization. This step is finite and easy in the finite-cover case (using normality directly), but in the general case it requires Zorn's lemma (Bredon Proposition 12.9 in [[Thm - Paracompact Has Partitions of Unity]]). The reaction pattern for any partition-of-unity construction is: "I have an open cover; I need a *closed* shrinkage to apply bumps; shrinkage exists by normality (finite case: direct; infinite case: Zorn)".

**Normality is the topological precondition.** The closed shrinking step uses normality (separation of disjoint closed sets by disjoint open sets, or equivalently, insertion of an open with closure in a given open). Normality is automatic on smooth manifolds (paracompact Hausdorff $\Rightarrow$ normal), so we don't have to verify it separately, but it is the topological ingredient that makes the construction possible. Without normality, no separation, no shrinking, no partition of unity. The trigger to recognize this: any partition-of-unity-like construction on a topological space depends on the space being normal.

**Bump + normalize is the universal pattern.** Build bumps on the closed shrinkage, sum, divide by the sum. The smoothness of each $\psi_i$ comes from the smoothness of the bumps and the positivity of the denominator. The "sum to $1$" property is automatic from the division by the sum. The "supports in $U_i$" condition is preserved because dividing by a positive function doesn't change where the function vanishes. This three-step pattern — bumps, sum, divide — is the canonical construction; any partition-of-unity construction in any setting (manifold, sheaf, distribution) uses some version of it. The recognition trigger is having a family of "$1$-on-closed-$0$-off-open" functions; the reaction is to sum and normalize.

This exercise is the prototype for the full [[Thm - Existence of Smooth Partitions of Unity]] argument. In the general case, the extra work is (a) refining the cover to be locally finite via paracompactness, and (b) Zorn-style closed shrinking; these handle the technical complications of infinite covers but the conceptual structure is the same: shrink, bump, sum, normalize. Companion exercises: [[Ex - Constructing a Bump Function on Euclidean Space]] provides the building block; [[Ex - Composition of Smooth Maps is Smooth]] is the smoothness-verification routine. The application of this partition of unity to construct a Riemannian metric on $M$ is forwarded to [[Differential Geometry XII — Riemannian and Semi-Riemannian Manifolds|DG XII]].
