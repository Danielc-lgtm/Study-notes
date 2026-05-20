---
type: exercise
subject: topology
difficulty: "⭐⭐"
prereqs:
  - "Def - Continuous Map"
  - "Def - Homeomorphism"
  - "Def - Subspace Topology"
  - "Def - Open and Closed Sets in a Metric Space"
tags: [analysis, topology]
---

# Problem Statement

Consider the map
$$f : [0, 2\pi) \to S^1, \qquad f(t) = (\cos t, \sin t),$$
where $S^1 = \{(x, y) \in \mathbb{R}^2 : x^2 + y^2 = 1\}$ is the unit circle in $\mathbb{R}^2$ with the [[Def - Subspace Topology|subspace topology]] from $\mathbb{R}^2$, and $[0, 2\pi)$ has the subspace topology from $\mathbb{R}$.

1. Show that $f$ is [[Def - Continuous Map|continuous]] and bijective.
2. Show that the inverse $f^{-1} : S^1 \to [0, 2\pi)$ is *not* continuous — equivalently, exhibit an open set $U \subseteq [0, 2\pi)$ such that $f(U)$ is *not* open in $S^1$.
3. Conclude that $f$ is a continuous bijection but *not* a [[Def - Homeomorphism|homeomorphism]].
4. Briefly explain why the analogous map $\tilde f : [0, 2\pi] \to S^1$, $\tilde f(t) = (\cos t, \sin t)$, becomes a quotient map (not a homeomorphism, since not injective) and how identifying the two endpoints recovers the structure of $S^1$.

**Recall:**

A function $f : X \to Y$ between topological spaces is [[Def - Continuous Map|continuous]] iff $f^{-1}(V) \in \tau_X$ for every $V \in \tau_Y$. It is a [[Def - Homeomorphism|homeomorphism]] iff it is bijective, continuous, and its inverse $f^{-1} : Y \to X$ is also continuous. Equivalently, $f$ is a homeomorphism iff it is a *continuous open bijection*: bijective, continuous, and maps open sets to open sets (sends each open $U \subseteq X$ to an open $f(U) \subseteq Y$).

The [[Def - Subspace Topology|subspace topology]] on $[0, 2\pi) \subseteq \mathbb{R}$ has as open sets the intersections $U \cap [0, 2\pi)$ where $U$ is open in $\mathbb{R}$. In particular, $[0, \varepsilon) = (-\varepsilon, \varepsilon) \cap [0, 2\pi)$ is open in $[0, 2\pi)$.

The subspace topology on $S^1 \subseteq \mathbb{R}^2$ has as open sets the intersections of $S^1$ with open subsets of $\mathbb{R}^2$ — equivalently, the unions of open *arcs* on the circle.

---

# Convergent Strategy

**Problem class.** Demonstrate that a specific continuous bijection fails to be a homeomorphism. This is the canonical illustration of the warning "continuous + bijective ≠ homeomorphism", and the example is one of the foundational counterexamples in topology — the *winding map* of $[0, 2\pi)$ around the circle.

**Assumption pattern.** The source $[0, 2\pi)$ is *not closed* in $\mathbb{R}$ (the right endpoint is missing); the target $S^1$ is compact and connected. The mismatch at $t = 0$ — corresponding to the image point $(1, 0)$, which is the limit of both $f(t)$ as $t \to 0^+$ and as $t \to 2\pi^-$ — is the source of the discontinuity of the inverse.

**Theorem routing.** Step 1: continuity of $f$ follows from continuity of $\cos$ and $\sin$, and the product-into-$\mathbb{R}^2$ universal property — see [[Ex - Generating a topology from a subbasis]]. Bijectivity is by parameterizing the circle and using that $\cos, \sin$ are periodic with period $2\pi$, so the restriction to $[0, 2\pi)$ is bijective onto $S^1$. Step 2: the set $U = [0, 1)$ is open in $[0, 2\pi)$, but $f(U)$ is an arc of $S^1$ that *includes* the point $(1, 0) = f(0)$ but does *not* contain any open neighbourhood of $(1, 0)$ in $S^1$ — because any open neighbourhood of $(1, 0)$ in $S^1$ includes points $f(t)$ for $t$ close to $2\pi^-$, and those are not in $f(U)$.

**Key decision point.** The non-obvious move is identifying the open set $U = [0, 1)$ (or any $[0, \varepsilon)$) as the witness. The image $f([0, 1))$ is an open arc *closed on one side* — and the closed side is exactly at $(1, 0)$, the point where the source's "missing endpoint $2\pi$" makes the inverse fail to be continuous.

---

# Legal Operations Used

This solution deploys the following operations from [[Topology I — §1–3 Metric and Topological Spaces#Legal Operations|the topic page's Legal Operations]]:

1. **Continuity via the product universal property.** A map into $\mathbb{R}^2$ is continuous iff each component map is continuous; $t \mapsto \cos t$ and $t \mapsto \sin t$ are continuous from analysis.

2. **Continuity into a subspace.** If $f : Z \to X$ is continuous with image in $Y \subseteq X$, the corestriction $\tilde f : Z \to Y$ is continuous in the subspace topology.

3. **Refute homeomorphism by exhibiting an open set whose image is not open.** A continuous bijection $f$ is a homeomorphism iff it is an *open map*; if $f(U)$ is not open for some open $U$, then $f^{-1}$ is not continuous.

4. **Use the failure-of-compactness intuition.** The fact that $[0, 2\pi)$ is *not compact* (it is bounded but not closed in $\mathbb{R}$) is what allows the failure — the standard "compact-to-Hausdorff" theorem ([[Topology II — §4–7 Connectivity, Separation, Nets, Compactness|in §4]]) says that if the source *were* compact, every continuous bijection to a Hausdorff space would be a homeomorphism.

---

# Hints

> [!note]- Hint 1
> For continuity of $f$, the [[Def - Continuous Map|product continuity criterion]] says a map into $\mathbb{R}^2$ is continuous iff each component is. Both $\cos$ and $\sin$ are continuous from analysis.

> [!note]- Hint 2
> For bijectivity, parameterize: every point of $S^1$ has the form $(\cos t, \sin t)$ for a unique $t \in [0, 2\pi)$ (this is the definition of the angular parameter).

> [!note]- Hint 3
> For the failure of continuity of $f^{-1}$: take a small open set $U = [0, 1) \subseteq [0, 2\pi)$. What does $f(U)$ look like on $S^1$? Is $f(U)$ open in $S^1$?

> [!note]- Hint 4
> The image $f([0, 1))$ is an arc from $(1, 0)$ (going counter-clockwise) up to the point $f(1) = (\cos 1, \sin 1)$, *excluding* the endpoint $f(1)$ but *including* $(1, 0) = f(0)$. Is this an open subset of $S^1$? Picture a small neighbourhood of $(1, 0)$ in $S^1$ — does it lie inside $f([0, 1))$?

---

# Solution

The winding map is continuous and bijective by construction; the failure of $f^{-1}$ to be continuous is the failure of a one-sided open interval in $[0, 2\pi)$ to have an open image — and the geometric reason is that $(1, 0)$ has neighbours in $S^1$ on *both* sides (clockwise and counterclockwise), but only one side comes from the parameterization $[0, 2\pi)$.

**Step 1: $f$ is continuous and bijective.**

Continuity follows from continuity of $\cos, \sin$ and the product universal property. Bijectivity is from the parameterization of the unit circle by $[0, 2\pi)$.

> [!note]- Derivation
> *Continuity.* The map $f : [0, 2\pi) \to \mathbb{R}^2$, $t \mapsto (\cos t, \sin t)$, is continuous because each component $t \mapsto \cos t$ and $t \mapsto \sin t$ is continuous on $\mathbb{R}$ (standard analysis), so the restrictions to $[0, 2\pi)$ are continuous from the [[Def - Subspace Topology|subspace topology]]. By the [[Ex - Generating a topology from a subbasis|product topology criterion]], the combined map into $\mathbb{R}^2$ is continuous. Since the image $f([0, 2\pi)) \subseteq S^1$, the corestriction $f : [0, 2\pi) \to S^1$ (subspace topology) is continuous.
>
> *Bijectivity.* The map $t \mapsto (\cos t, \sin t)$ from $\mathbb{R}$ to $S^1$ is surjective (every point of $S^1$ is of this form by definition of $S^1$ in terms of angle parameterization) and is $2\pi$-periodic. Restricting to $[0, 2\pi)$ gives a fundamental domain: every point of $S^1$ has a unique preimage in $[0, 2\pi)$.

**Step 2: $f^{-1}$ is not continuous — exhibit $U = [0, 1)$ with $f(U)$ not open in $S^1$.**

Take $U = [0, 1) \subseteq [0, 2\pi)$. Then $U$ is open in $[0, 2\pi)$ (it equals $(-1, 1) \cap [0, 2\pi)$). The image $f(U) = \{(\cos t, \sin t) : 0 \leq t < 1\}$ is an arc from $(1, 0)$ (inclusive) counter-clockwise to $(\cos 1, \sin 1)$ (exclusive). This arc is *not* open in $S^1$ — it contains the point $(1, 0)$ but no open neighbourhood of $(1, 0)$ in $S^1$ is contained in $f(U)$. Any open neighbourhood of $(1, 0)$ in $S^1$ contains points $f(t)$ for $t$ close to $2\pi^-$ (i.e., points on the clockwise side of $(1, 0)$), and those points are not in $f(U)$.

> [!note]- Derivation
> *$U$ is open.* $U = [0, 1) = (-1, 1) \cap [0, 2\pi)$ is the intersection of an $\mathbb{R}$-open set with $[0, 2\pi)$, hence open in the subspace topology.
>
> *$f(U)$ as a subset of $S^1$.* $f(U) = \{(\cos t, \sin t) : t \in [0, 1)\}$. This includes $f(0) = (1, 0)$ (since $0 \in U$) and approaches $f(1) = (\cos 1, \sin 1)$ from the counterclockwise side, but does not include $f(1)$.
>
> *Why $f(U)$ is not open in $S^1$.* An open neighbourhood of $(1, 0)$ in $S^1$ has the form $B_\varepsilon((1, 0)) \cap S^1$ for some $\varepsilon > 0$, where $B_\varepsilon$ is the Euclidean ball in $\mathbb{R}^2$. For small $\varepsilon$, this intersection is an arc of $S^1$ centered at $(1, 0)$, containing points $f(t)$ for $t$ in a small interval $(-\delta, \delta)$ in *angular* parameterization, where the negative side corresponds to $t$ slightly less than $2\pi$ in our parameterization $[0, 2\pi)$.
>
> Concretely: for any $\varepsilon > 0$, the point $f(2\pi - \delta) = (\cos(2\pi - \delta), \sin(2\pi - \delta)) = (\cos \delta, -\sin \delta)$ lies within Euclidean distance $\sqrt{(\cos\delta - 1)^2 + \sin^2\delta} = \sqrt{2 - 2\cos\delta}$ of $(1, 0)$, which goes to $0$ as $\delta \to 0$. So for any small $\varepsilon$, the open neighbourhood $B_\varepsilon((1, 0)) \cap S^1$ contains $f(2\pi - \delta)$ for $\delta$ small enough — but $f(2\pi - \delta) \notin f(U)$ since $2\pi - \delta \in (2\pi - \delta, 2\pi) \not\subseteq [0, 1) = U$.
>
> Hence no open neighbourhood of $(1, 0)$ in $S^1$ is contained in $f(U)$, so $(1, 0)$ is not an interior point of $f(U)$, so $f(U)$ is not open in $S^1$.
>
> *Conclusion: $f^{-1}$ is not continuous.* Continuity of $f^{-1} : S^1 \to [0, 2\pi)$ would require $(f^{-1})^{-1}(U) = f(U)$ to be open in $S^1$ for every open $U$ in $[0, 2\pi)$. We have just exhibited $U = [0, 1)$ open in $[0, 2\pi)$ with $f(U)$ not open in $S^1$. So $f^{-1}$ is not continuous.

**Step 3: Conclusion — $f$ is not a homeomorphism.**

A [[Def - Homeomorphism|homeomorphism]] is a continuous bijection whose inverse is continuous. By Steps 1 and 2, $f$ is a continuous bijection but $f^{-1}$ is not continuous. So $f$ is not a homeomorphism.

> [!note]- Derivation
> Equivalently, a homeomorphism is a continuous bijection that is also *open* (sends open sets to open sets). Step 2 produced an open $U \subseteq [0, 2\pi)$ with $f(U)$ not open in $S^1$ — so $f$ is not open, hence not a homeomorphism.
>
> *Why this happens here.* The source space $[0, 2\pi)$ is not compact (not closed in $\mathbb{R}$). The general result that *compactness saves the conclusion* — a continuous bijection from a compact space to a Hausdorff space is automatically a homeomorphism — is proved in [[Topology II — §4–7 Connectivity, Separation, Nets, Compactness]]. The failure here pinpoints exactly that non-compactness is what makes the example interesting.

**Step 4: The quotient version.**

If we extend the domain to $[0, 2\pi]$, the map $\tilde f : [0, 2\pi] \to S^1$, $\tilde f(t) = (\cos t, \sin t)$, is continuous, surjective, and *not* injective — only $0$ and $2\pi$ both map to $(1, 0)$. So $\tilde f$ identifies $\{0, 2\pi\}$ to a single point, and the *quotient* $[0, 2\pi]/(0 \sim 2\pi)$ is homeomorphic to $S^1$.

> [!note]- Derivation
> Define the quotient $Q = [0, 2\pi]/(0 \sim 2\pi)$ — that is, identify the two endpoints. There is a natural map $\bar f : Q \to S^1$ induced by $\tilde f$ (well-defined because $\tilde f(0) = \tilde f(2\pi) = (1, 0)$).
>
> *$\bar f$ is bijective.* On the interior $(0, 2\pi)$, $\tilde f$ is bijective onto $S^1 \setminus \{(1, 0)\}$ as before. The identified class $[0] = [2\pi]$ in $Q$ maps to $(1, 0) \in S^1$. So $\bar f$ is bijective.
>
> *$\bar f$ is continuous.* The quotient topology on $Q$ is defined so that $\bar f$ is continuous iff $\tilde f$ is — and $\tilde f$ is continuous by the same product-universal-property argument as $f$ in Step 1.
>
> *$\bar f$ is a homeomorphism.* The source $Q$ is the image of $[0, 2\pi]$ (compact) under the quotient map, hence compact. The target $S^1$ is Hausdorff (subspace of $\mathbb{R}^2$). A continuous bijection from a compact space to a Hausdorff space is a homeomorphism — see [[Topology II — §4–7 Connectivity, Separation, Nets, Compactness]] (the result is sometimes labeled the "closed map lemma"). So $\bar f$ is a homeomorphism, and $S^1 \cong [0, 2\pi]/(0 \sim 2\pi)$.
>
> This is one of the standard constructions of the circle: starting from the closed interval and gluing the endpoints.

> [!note]- Complete formal solution
> **(1)** $f$ is continuous (each component $\cos t, \sin t$ is continuous; product universal property). Bijective: $[0, 2\pi)$ is a fundamental domain of the $2\pi$-periodic parameterization of $S^1$. **(2)** $U = [0, 1)$ is open in $[0, 2\pi)$, but $f(U)$ is an arc closed at $(1, 0)$ on one side — every $\varepsilon$-ball about $(1, 0)$ contains points $f(2\pi - \delta) \notin f(U)$, so $(1, 0)$ is not an interior point of $f(U)$ in $S^1$. **(3)** $f$ is a continuous bijection but not an open map, hence not a homeomorphism. **(4)** Extending the domain to $[0, 2\pi]$ and identifying $0 \sim 2\pi$ gives a continuous bijection from a compact space to a Hausdorff space — automatically a homeomorphism. So $S^1 \cong [0, 2\pi]/(0 \sim 2\pi)$. $\blacksquare$

---

# Key Takeaways

**A continuous bijection is *not* automatically a homeomorphism — the requirement that the inverse be continuous is genuinely a separate condition.** The winding map $[0, 2\pi) \to S^1$ is the canonical counterexample, and the geometric reason it fails is *topological*: the source is not compact (specifically, it is missing the right endpoint), and the missing endpoint corresponds to a point $(1, 0)$ of the target that has neighbours in $S^1$ on *both* sides but only one side comes from a neighbourhood in $[0, 2\pi)$. The trigger to internalize is: whenever someone claims a continuous bijection is a homeomorphism, look for either compactness of the source or another structural hypothesis. Without one, the claim is false. The most common rescue is the [[Topology II — §4–7 Connectivity, Separation, Nets, Compactness|compact-Hausdorff theorem]]: continuous bijection from compact to Hausdorff is automatically a homeomorphism.

**The structural picture: a continuous bijection is a *continuous coarsening* — it preserves every property that comes from the source's topology but may have a strictly finer topology on the source than the target.** In our example, $[0, 2\pi)$ has the topology where $[0, \varepsilon)$ is a neighbourhood of $0$, but the topology pushed forward to $S^1$ via $f$ would give $(1, 0)$ only "one-sided" neighbourhoods — fewer than $S^1$'s actual topology, which gives $(1, 0)$ two-sided neighbourhoods. The general principle: a continuous bijection $f : X \to Y$ induces a topology on $Y$ pushed forward from $X$, and this pushed-forward topology is *coarser* than $Y$'s native topology (it has fewer open sets). The map is a homeomorphism iff the two topologies coincide. The failure of "continuous bijection $\Rightarrow$ homeomorphism" is exactly the failure of this push-forward to equal the target's topology.

**Identifying the two endpoints $0 \sim 2\pi$ of $[0, 2\pi]$ recovers $S^1$ as a quotient — this is the *quotient construction of the circle* and is the standard mental picture.** Quotients allow building new topological spaces by *gluing* points: starting from a familiar space (here, an interval), specify an equivalence relation (here, only $0 \sim 2\pi$), and take the quotient topology — the finest topology making the quotient projection continuous. The general construction: a Cell complex, a torus from a square via the rule $(x, 0) \sim (x, 1)$ and $(0, y) \sim (1, y)$, a Möbius band from a square via $(x, 0) \sim (1-x, 1)$, projective space $\mathbb{RP}^n$ from the sphere $S^n$ via $x \sim -x$. The trigger: whenever you have a space described by "identifying" or "gluing" certain points or boundaries, the underlying construction is a quotient space, and the quotient topology is the universal-property-defined coarsest topology making the projection continuous.

**The failure happens at *one specific point* — $(1, 0)$ — and not throughout $S^1$, because the parameterization is "locally a homeomorphism" everywhere except at the endpoints.** A general principle: when a global structure fails, the failure is often localized to a small set, and away from that small set the structure is fine. Here, on $(0, 2\pi) \subseteq [0, 2\pi)$, the restriction $f|_{(0, 2\pi)} : (0, 2\pi) \to S^1 \setminus \{(1, 0)\}$ *is* a homeomorphism. The pathology is concentrated at the single point $t = 0$ of the source. This pattern — global failure localized to a thin set, with the complement being well-behaved — recurs throughout topology: branch points of covering maps, singularities of analytic functions, critical points of smooth maps. The lesson: when constructing a homeomorphism between two spaces, the construction often works "almost everywhere" — but the points where it doesn't work are exactly the points that change the topology.
