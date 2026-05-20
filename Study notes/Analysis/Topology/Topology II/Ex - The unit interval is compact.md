---
type: exercise
subject: topology
difficulty: "⭐⭐"
prereqs:
  - "Def - Compact Space"
  - "Def - Topological Space"
tags: [analysis, topology, compactness]
---

# Problem Statement

Show that the closed unit interval $[0, 1] \subseteq \mathbb{R}$, with its standard subspace topology, is **compact**.

The classical hint, due to Bredon: let $\mathcal{U} = \{U_\alpha\}$ be an open cover of $[0, 1]$. Define
$$S = \{t \in [0, 1] : [0, t] \text{ admits a finite subcover from } \mathcal{U}\}.$$
Let $b = \sup S$. Show that $b > 0$, that $b = 1$, and that $1 \in S$ (i.e., the sup is attained).

**Recall:**

![[Def - Compact Space#The Definition]]

An **open cover** of a topological space $X$ is a collection $\{U_\alpha\}_{\alpha \in I}$ of open subsets whose union is $X$. A **subcover** is a subfamily $\{U_\alpha\}_{\alpha \in J}$, $J \subseteq I$, still covering $X$. A **finite subcover** is one where $J$ is finite.

The space is **compact** if every open cover has a finite subcover.

A subset $U \subseteq [0, 1]$ is **open** in the subspace topology if and only if for every $x \in U$ there is $\varepsilon > 0$ with $[0, 1] \cap (x - \varepsilon, x + \varepsilon) \subseteq U$.

---

# Convergent Strategy

**Problem class.** Direct verification of compactness from the open-cover definition. The route is the order-completeness of $\mathbb{R}$: define a set $S$ of "well-covered" prefixes of $[0, 1]$, take its sup, and propagate by openness.

**Assumption pattern.** Given: any open cover $\mathcal{U}$ of $[0, 1]$. Goal: produce a finite subcover.

**Theorem routing.** No prior theorems beyond the order-completeness of $\mathbb{R}$ (existence of suprema for bounded sets) and the openness condition in the subspace topology. The single key fact is: if a point $b$ is in some open set $U_\beta$, openness gives an interval around $b$ contained in $U_\beta$.

**Key decision point.** The non-obvious moves are:
1. Define $S$ to be the *set of right-endpoints of well-covered prefixes*, not the set of covered points. This converts a question about all of $[0, 1]$ into a question about how far the "finite cover" extends.
2. Take $b = \sup S$; the goal is to show $b = 1$ and $1 \in S$.
3. The same supremum-pushing argument works *twice*: once to show $b = 1$ (else $b$ would not be the sup), and once to show $1 \in S$ (the finite cover extending up to $b$ can be extended slightly further by adding one more open set).

---

# Legal Operations Used

This solution deploys the following legal operations from the [[Topology II — §4–7 Connectivity, Separation, Nets, Compactness#Legal Operations|topic page's Legal Operations]]:

1. **Direct subcover extraction via supremum of "good prefixes".** When proving compactness directly in an order-complete space, the move is to define the set of "well-covered" prefixes, take its supremum, and use openness around the supremum to push it further.

2. **Use order-completeness of $\mathbb{R}$ to extract a critical point.** $\sup S$ exists because $S$ is bounded above (by $1$) and nonempty (contains $0$, since $\{0\}$ is covered by any single $U_\alpha \ni 0$).

3. **Exploit openness to find an interval around a critical point inside some basis element.** When $b$ is in $U_\beta$, openness gives an interval around $b$ inside $U_\beta$. This is the "breathing room" of openness that lets the finite cover extend.

---

# Hints

> [!note]- Hint 1
> Let $\mathcal{U} = \{U_\alpha\}$ be an open cover of $[0, 1]$. Define $S = \{t \in [0, 1] : [0, t] \text{ has a finite subcover from } \mathcal{U}\}$. Show $0 \in S$ (pick $U_{\alpha_0} \ni 0$; then $\{U_{\alpha_0}\}$ is a finite subcover of $\{0\} = [0, 0]$). So $S$ is nonempty. It is bounded above by $1$. Let $b = \sup S$.

> [!note]- Hint 2
> Show $b > 0$. Pick $U_\beta \ni 0$. By openness in the subspace topology, $[0, 1] \cap [0, \delta) \subseteq U_\beta$ for some $\delta > 0$. So for any $t \in [0, \delta/2]$, $[0, t]$ is covered by the single open $U_\beta$, hence $t \in S$. So $\delta/2 \in S$ and $b \geq \delta/2 > 0$.

> [!note]- Hint 3
> Show $b = 1$. Suppose for contradiction $b < 1$. Pick $U_\beta \ni b$. By openness, $[0, 1] \cap (b - \varepsilon, b + \varepsilon) \subseteq U_\beta$ for some $\varepsilon > 0$ (small enough that $b + \varepsilon < 1$). By definition of $\sup$, some $t \in S$ has $t > b - \varepsilon$. Take a finite subcover $U_{\alpha_1}, \ldots, U_{\alpha_n}$ of $[0, t]$; add $U_\beta$ to get a finite subcover of $[0, t] \cup [b - \varepsilon, b + \varepsilon) \supseteq [0, b + \varepsilon/2]$. So $b + \varepsilon/2 \in S$, contradicting $b = \sup S$.

> [!note]- Hint 4
> Show $1 \in S$. We have $b = 1$. We want a finite subcover of $[0, 1]$. Pick $U_\gamma \ni 1$. By openness, $[0, 1] \cap (1 - \delta, 1] \subseteq U_\gamma$ for some $\delta > 0$. By definition of $\sup$, some $t \in S$ has $t > 1 - \delta$. Take a finite subcover $U_{\alpha_1}, \ldots, U_{\alpha_n}$ of $[0, t]$; add $U_\gamma$. Then $\{U_{\alpha_1}, \ldots, U_{\alpha_n}, U_\gamma\}$ covers $[0, t] \cup [1 - \delta, 1] = [0, 1]$.

---

# Solution

The proof has three identical motifs: each time the supremum is supposed to push further, openness around the supremum point lets us extend by one more open set. The only delicate point is that the supremum must be *attained* — there is no "above the supremum" left to push toward, but we can still extend the finite cover at the top.

**Step 1: Set up $S$ and show $0 \in S$.**

Let $\mathcal{U} = \{U_\alpha\}$ be an open cover of $[0, 1]$. Define
$$S = \{t \in [0, 1] : [0, t] \text{ has a finite subcover from } \mathcal{U}\}.$$
Then $0 \in S$: pick any $U_{\alpha_0} \ni 0$ (it exists since $\mathcal{U}$ covers $[0, 1]$); then $\{U_{\alpha_0}\}$ is a finite subcover of $[0, 0] = \{0\}$. So $S$ is nonempty. Bounded by $1$. Let $b = \sup S \in [0, 1]$.

> [!note]- Derivation
> Since $\mathcal{U}$ is an open cover of $[0, 1]$, there is some $U_{\alpha_0} \in \mathcal{U}$ with $0 \in U_{\alpha_0}$. The set $[0, 0] = \{0\}$ is a single point, covered by the single set $U_{\alpha_0}$, hence has a finite subcover from $\mathcal{U}$ — so $0 \in S$.
>
> Hence $S \subseteq [0, 1]$ is nonempty and bounded above by $1$. By the order completeness of $\mathbb{R}$, $b = \sup S$ exists and lies in $[0, 1]$.

**Step 2: Show $b > 0$.**

Pick $U_\beta \ni 0$. By openness, there is $\delta > 0$ with $[0, 1] \cap [0, \delta) \subseteq U_\beta$. Then for any $t \in [0, \delta/2]$, $[0, t]$ is covered by $\{U_\beta\}$, so $t \in S$. Hence $\delta/2 \in S$ and $b \geq \delta/2 > 0$.

> [!note]- Derivation
> $\mathcal{U}$ covers $[0,1]$, so some $U_\beta \in \mathcal{U}$ contains $0$. By the definition of openness in the subspace topology, there is $\delta > 0$ with $[0, 1] \cap (-\delta, \delta) = [0, \delta) \subseteq U_\beta$.
>
> Then for $t \in [0, \delta/2] \subseteq [0, \delta)$, $[0, t] \subseteq [0, \delta) \subseteq U_\beta$, so $\{U_\beta\}$ is a finite subcover of $[0, t]$, hence $t \in S$. In particular $\delta/2 \in S$. So $b = \sup S \geq \delta/2 > 0$.

**Step 3: Show $b = 1$.**

Suppose for contradiction $b < 1$. Pick $U_\beta \ni b$. By openness, there is $\varepsilon > 0$ with $[0, 1] \cap (b - \varepsilon, b + \varepsilon) \subseteq U_\beta$. Shrink $\varepsilon$ so that $b + \varepsilon < 1$. By definition of $\sup$, some $t \in S$ has $b - \varepsilon < t \leq b$. Let $U_{\alpha_1}, \ldots, U_{\alpha_n}$ be a finite subcover of $[0, t]$. Then $\{U_{\alpha_1}, \ldots, U_{\alpha_n}, U_\beta\}$ covers $[0, t] \cup [b - \varepsilon, b + \varepsilon) \supseteq [0, b + \varepsilon/2]$, so $b + \varepsilon/2 \in S$, contradicting $b = \sup S$.

> [!note]- Derivation
> Suppose $b < 1$. The open cover $\mathcal{U}$ has some $U_\beta \ni b$. By openness, $[0, 1] \cap (b - \varepsilon, b + \varepsilon) \subseteq U_\beta$ for some $\varepsilon > 0$. Shrink $\varepsilon$ so that $\varepsilon < 1 - b$, i.e., $b + \varepsilon < 1$.
>
> By definition of $b = \sup S$, there is $t \in S$ with $b - \varepsilon < t$. (Since $t \leq b$ for any $t \in S$, $t \in (b - \varepsilon, b]$.) By definition of $S$, there are finitely many $U_{\alpha_1}, \ldots, U_{\alpha_n} \in \mathcal{U}$ with $[0, t] \subseteq U_{\alpha_1} \cup \cdots \cup U_{\alpha_n}$.
>
> Now form the family $\{U_{\alpha_1}, \ldots, U_{\alpha_n}, U_\beta\}$. We claim this covers $[0, b + \varepsilon/2]$:
> - $[0, t]$ is covered by the $U_{\alpha_i}$'s.
> - $[t, b + \varepsilon/2] \subseteq (b - \varepsilon, b + \varepsilon) \subseteq U_\beta$ (since $t > b - \varepsilon$ and $b + \varepsilon/2 < b + \varepsilon$).
>
> Together, $[0, b + \varepsilon/2]$ is covered. So $b + \varepsilon/2 \in S$, but $b + \varepsilon/2 > b = \sup S$ — contradiction. Hence $b = 1$.

**Step 4: Show $1 \in S$ (the sup is attained).**

The sup $b = 1$ might still not be in $S$. To show $1 \in S$: pick $U_\gamma \ni 1$. By openness, $[0, 1] \cap (1 - \delta, 1] \subseteq U_\gamma$ for some $\delta > 0$. By definition of $\sup$, some $t \in S$ has $t > 1 - \delta$. Take a finite subcover $\{U_{\alpha_1}, \ldots, U_{\alpha_n}\}$ of $[0, t]$. Then $\{U_{\alpha_1}, \ldots, U_{\alpha_n}, U_\gamma\}$ covers $[0, 1]$.

> [!note]- Derivation
> We have $b = 1$. Pick $U_\gamma \ni 1$. By openness, $[0, 1] \cap (1 - \delta, 1] \subseteq U_\gamma$ for some $\delta > 0$.
>
> By definition of $\sup S = 1$, there is $t \in S$ with $t > 1 - \delta$. Take a finite subcover $U_{\alpha_1}, \ldots, U_{\alpha_n}$ of $[0, t]$.
>
> Then $\{U_{\alpha_1}, \ldots, U_{\alpha_n}, U_\gamma\}$ is a finite subfamily of $\mathcal{U}$ covering $[0, 1]$: $[0, t]$ is covered by the $U_{\alpha_i}$'s, $[t, 1] \subseteq (1 - \delta, 1] \subseteq U_\gamma$. So $1 \in S$.
>
> Hence $\mathcal{U}$ has a finite subcover of $[0, 1]$, and $[0, 1]$ is compact.

> [!note]- Complete formal solution
> Let $\mathcal{U} = \{U_\alpha\}$ be an open cover of $[0, 1]$. Define $S = \{t \in [0, 1] : [0, t] \text{ has a finite subcover from } \mathcal{U}\}$. The set $S$ is nonempty (any $U_\alpha \ni 0$ gives $0 \in S$) and bounded by $1$, so $b = \sup S$ exists.
>
> *$b > 0$:* pick $U_\beta \ni 0$, with $[0, \delta) \subseteq U_\beta$ by openness; then $\delta/2 \in S$, $b \geq \delta/2$.
>
> *$b = 1$:* if $b < 1$, pick $U_\beta \ni b$ with $(b - \varepsilon, b + \varepsilon) \subseteq U_\beta$, $\varepsilon < 1 - b$. By sup, some $t \in S \cap (b - \varepsilon, b]$ exists with finite cover of $[0, t]$; adding $U_\beta$ covers $[0, b + \varepsilon/2]$, so $b + \varepsilon/2 \in S$ — contradicting $b = \sup S$. Hence $b = 1$.
>
> *$1 \in S$:* pick $U_\gamma \ni 1$ with $(1 - \delta, 1] \subseteq U_\gamma$ by openness. By sup, some $t \in S \cap (1 - \delta, 1]$ exists; adding $U_\gamma$ to a finite cover of $[0, t]$ covers $[0, 1]$. So $1 \in S$.
>
> Hence $\mathcal{U}$ has a finite subcover, and $[0, 1]$ is compact. $\blacksquare$

---

# Key Takeaways

**The "sup of well-behaved prefixes" technique converts compactness verifications in $\mathbb{R}$ into supremum-pushing arguments, and is the prototype for every compactness proof in $\mathbb{R}^n$.** The exact same shape — define a set of well-behaved values, take its supremum, push it to the maximum using openness — proves compactness of $[a, b]$ in $\mathbb{R}$, the existence of zeros in the intermediate value theorem (a related "sup of points below the zero" argument), and is the engine of Cantor's intersection theorem and the Bolzano-Weierstrass theorem in their order-theoretic versions. The pattern is order-complete-specific: it uses the existence of suprema and is the order-theoretic substitute for compactness in $\mathbb{R}$. Once $[0, 1]$ is compact, every other compactness statement in $\mathbb{R}^n$ follows by:
- Scaling and translation ($[a, b] \cong [0, 1]$);
- Tychonoff for finite products ($[0, 1]^n$ is compact);
- Closed-subset-of-compact-is-compact (closed and bounded subsets of $\mathbb{R}^n$ are closed in some $[a, b]^n$).

This single proof unlocks Heine-Borel, the extreme value theorem, and most of classical real analysis.

**The two pushes — "$b = 1$" and "$1 \in S$" — are structurally distinct and both are needed; missing the second is the most common error in proving compactness of closed intervals.** Naively, students prove $b = \sup S = 1$ but forget to show $1 \in S$. But "the sup is achieved" is a separate claim from "the sup is $1$"; for the *open* interval $(0, 1)$, the sup of well-behaved prefixes is also $1$, but $1$ is not in the open interval, so the analogous argument never reaches $1$, and indeed $(0, 1)$ is *not* compact. The closedness of $[0, 1]$ on the right is exactly what allows the second push to work: $1 \in [0, 1]$ means $\mathcal{U}$ has some $U_\gamma \ni 1$, and openness at $1$ extends the cover. Recognize the trigger: any time you are pushing a supremum to a boundary point, ask whether the boundary point is in your set, and whether it is in the open cover.

**Compactness is "topological finiteness" — finitely many open sets capture everything — but the proof in $\mathbb{R}$ is fundamentally an order-completeness argument, not a topological one.** This dichotomy is important: compactness of $[0, 1]$ depends crucially on $\mathbb{R}$'s order completeness (the sup exists). In a non-order-complete totally ordered field (e.g., the rationals $\mathbb{Q}$), the interval $[0, 1] \cap \mathbb{Q}$ is *not* compact, even though "closed and bounded" makes sense — because the supremum of "well-behaved prefixes" might not exist in $\mathbb{Q}$. The deep reason $\mathbb{R}^n$ is the right setting for classical analysis is the interaction of order completeness with topology: order completeness gives compactness, compactness gives all the basic theorems.

**The trigger "want a finite subcover of an interval" maps to "well-order, take sup, propagate by openness".** This pattern shows up beyond $[0, 1]$: in lifting paths, in extension theorems (Tietze), in the proof of the Schoenflies theorem in low-dimensional topology, in the proof of the Jordan curve theorem. The general technique: define a set of "good" prefixes or initial segments, take the supremum, show the supremum is the goal, and show the supremum is in the good set. Mastery of this pattern in the simplest case prepares for every harder instance.
