---
type: theorem
subject: topology
prereqs:
  - "Def - Topological Space"
  - "Def - Separation Axioms"
  - "Def - Compact Space"
  - "Def - Locally Compact Space"
tags: [analysis, topology]
---

# Notation

$X$ is a locally compact Hausdorff (LCH) space. $X^+ = X \cup \{\infty\}$ adjoins a single new point $\infty \notin X$. Open sets in $X^+$ are: (i) all open subsets of $X$ (regarded as subsets of $X^+$ not containing $\infty$); (ii) sets of the form $X^+ \setminus K$ where $K \subseteq X$ is compact (these are the open neighborhoods of $\infty$). The full registry is on [[Topology III — §8–12 Products, Metric Spaces, Locally Compact, Paracompact]].

---

# Statement

> **One-Point Compactification.** Let $X$ be a **locally compact Hausdorff** space. Define $X^+ = X \cup \{\infty\}$ (where $\infty$ is a new point, not in $X$), with topology
>
> $$\tau^+ = \{U \subseteq X^+ : U \text{ open in } X\} \cup \{X^+ \setminus K : K \subseteq X \text{ compact}\}.$$
>
> Then:
>
> 1. $\tau^+$ is a topology on $X^+$.
> 2. $X^+$ is **compact Hausdorff**.
> 3. The inclusion $X \hookrightarrow X^+$ is an open embedding with dense image (when $X$ is not compact); $X$ is open in $X^+$ and $X^+ \setminus X = \{\infty\}$.
> 4. **Uniqueness.** $X^+$ is the unique (up to canonical homeomorphism) compact Hausdorff space in which $X$ embeds as an open subspace with single-point complement.
>
> **Functoriality.** A continuous map $f : X \to Y$ between LCH spaces is **proper** (preimages of compacts are compact) if and only if $f$ extends to a continuous $f^+ : X^+ \to Y^+$ with $f^+(\infty_X) = \infty_Y$.

---

# Motivation

The motivating problem: take a non-compact LCH space, like $\mathbb{R}^n$, and find a compact space that "completes" it minimally. The intuition: compactify $\mathbb{R}^n$ by adding a single "point at infinity" — a single new point representing the limit of everything escaping to infinity. The resulting space $(\mathbb{R}^n)^+$ should be the sphere $S^n$ (via stereographic projection), turning the open Euclidean space into the closed sphere.

The construction generalizes this to any LCH space. Add a single point $\infty$, declare its neighborhoods to be "complements of compact sets in $X$" — i.e., $\infty$ is "near everything outside any given compact set". This is the minimal way to make $X$ compact: we only need to add enough points (here just one) so that every open cover has a finite subcover, and adding a single point covering the "complement of compacts" suffices.

Why does this work? Because LCH gives us:
- *Hausdorffness*: $\infty$ can be separated from any $x \in X$ by disjoint opens (take a compact neighborhood $K$ of $x$, then $\text{int}(K)$ and $X^+ \setminus K$ separate). This requires the *local compactness*: without it, $x$ has no compact neighborhood and the separation fails.
- *Compactness*: any open cover of $X^+$ must contain a neighborhood of $\infty$, say $X^+ \setminus K$ with $K$ compact; the remaining cover restricted to $K$ is a cover of a compact, hence finite subcover; combined with the original $X^+ \setminus K$, we get a finite subcover of $X^+$. The construction's whole point is to leverage the existing compact sets in $X$.

The uniqueness is striking. There is *exactly one* way to compactify $X$ by adding a single point: any compact Hausdorff space in which $X$ embeds as open with single-point complement is homeomorphic to $X^+$. The reason: the neighborhoods of $\infty$ are forced by the topology — they must be complements of closed-in-compactified, but those are exactly the closed-in-$X$ sets that are *also compact* (since compactness is intrinsic and unchanged by ambient embedding). So the topology is forced.

Contrast with the **Stone–Čech compactification** $\beta X$ (for completely regular $X$): $\beta X$ adds many more points — in fact, $\beta\mathbb{N}$ has cardinality $2^{2^{\aleph_0}}$, vastly larger than $\mathbb{N}^+ = \mathbb{N} \cup \{\infty\}$. The Stone–Čech is the *maximal* compactification, where every bounded continuous function on $X$ extends; the one-point is the *minimal*. They are at opposite ends of a spectrum, and different applications call for different ones.

Classical examples:
- $(\mathbb{R})^+ = S^1$ (the circle).
- $(\mathbb{R}^n)^+ = S^n$ via stereographic projection.
- $(\mathbb{C})^+ = \widehat{\mathbb{C}} = S^2$ = Riemann sphere, the standard setting for complex analysis on $\mathbb{C}$.
- If $X$ is already compact, $X^+$ is $X$ plus an isolated point — not interesting.
- $(\mathbb{N})^+ =$ a convergent sequence with its limit, the simplest infinite compact Hausdorff space.

---

# Sources and Targets

**Sources (Input Broadening)**

The precondition is "$X$ is LCH". The skill is to recognize when an LCH space is in play, sometimes implicitly.

The first source is **$\mathbb{R}^n$ or a manifold**. Property $B$: a smooth or topological manifold without boundary. The bridge: manifolds are LCH (Hausdorff + second countable + locally Euclidean implies locally compact). So $X^+$ exists and is compact Hausdorff. *Example:* $(\mathbb{R}^n)^+ = S^n$ is the prototypical example.

The second source is **an open subset of a compact Hausdorff space**. Property $B$: $X = Y \setminus C$ where $Y$ is compact Hausdorff and $C \subseteq Y$ is closed. The bridge: open subsets of compact Hausdorff spaces are LCH (locally closed in a compact Hausdorff is LCH). So $X^+$ exists. *Example:* $X = \mathbb{R}^n = (S^n) \setminus \{p\}$ is LCH; its $X^+$ is $S^n$, recovering the compactification.

The third source is **a locally compact topological group**. Property $B$: $G$ a topological group with compact neighborhood of identity. The bridge: locally compact + Hausdorff (groups are automatically Hausdorff with closed identity, or we add Hausdorff). So $G^+$ exists. *Example:* the additive group $\mathbb{R}$ has $\mathbb{R}^+ = S^1$ (topologically; group structure does not extend to $S^1$ canonically, though).

**Targets (Output Amplification)**

The conclusion is "$X^+$ is compact Hausdorff with $X$ embedded as open dense with single-point complement".

Combine the conclusion with **the embedding into $X^+$**. Property $D$: a continuous bounded function $f : X \to \mathbb{R}$ such that $f$ "extends by $0$" at infinity (i.e., $\lim_{x \to \infty} f(x) = 0$, in the sense that for every $\varepsilon > 0$, the set $\{|f| \geq \varepsilon\}$ is compact). The amplified result $E$: $f$ extends continuously to $\hat f : X^+ \to \mathbb{R}$ with $\hat f(\infty) = 0$. The combination characterizes the space $C_0(X)$ of continuous functions vanishing at infinity as $\{f \in C(X^+) : f(\infty) = 0\}$.

Combine the conclusion with **the compactness of $X^+$ for arguments**. Property $D$: any continuous function $f : X^+ \to \mathbb{R}$ (i.e., a continuous function on $X$ extending to $\infty$). The amplified result $E$: $f$ attains its max and min on the compact $X^+$, hence is bounded on $X$. The combination is the standard "extend by infinity, work in $X^+$, restrict back" pattern.

Combine the conclusion with **proper maps and functoriality**. Property $D$: a proper map $f : X \to Y$ between LCH spaces (preimages of compacts are compact). The amplified result $E$: $f$ extends to a continuous $f^+ : X^+ \to Y^+$ with $f^+(\infty_X) = \infty_Y$. The combination is the **functoriality of $(\cdot)^+$**: $(\cdot)^+$ is a functor from LCH with proper maps to compact Hausdorff with continuous maps.

---

# Why Is It True

The intuition: $X^+$ adds the *single point* "at infinity" needed to close up $X$, with the neighborhoods of $\infty$ being exactly the complements of compact sets — the sets where "everything except a compact piece is" — and the open sets of $X$ remain open in $X^+$.

The construction is forced. To compactify $X$ by adding a single point, we need to declare which sets are neighborhoods of $\infty$. The constraint: any open cover of $X^+$ must have a finite subcover. Among the cover, one open neighborhood of $\infty$ — say $X^+ \setminus K$ — must be present; for the cover to be finite, the rest of the cover restricted to $K$ must have a finite subcover, which is exactly the compactness of $K$. So neighborhoods of $\infty$ should be "complements of compact $K$" — that is the only choice consistent with compactness.

Why does this give a topology? Two checks:
- **Empty and whole are open**: $\emptyset$ is open (in $X$ or as $X^+ \setminus X^+$ which is not of the cited form; in fact $\emptyset$ is open as $\emptyset = \emptyset$ open in $X$). $X^+$ itself is $X^+ \setminus \emptyset$, and $\emptyset$ is compact, so $X^+$ is open. ✓
- **Finite intersections are open**: An open in $X$ intersected with an open in $X$ is open in $X$ (X-topology is closed under finite intersection). An open in $X$ intersected with $X^+ \setminus K$ is (open in $X$) $\cap$ $(X \setminus K)$ (when $\infty \notin$ first set), which is open in $X$ since $X \setminus K$ is open ($K$ compact hence closed in Hausdorff $X$). Two opens of the form $X^+ \setminus K_1$, $X^+ \setminus K_2$ intersect to $X^+ \setminus (K_1 \cup K_2)$, and $K_1 \cup K_2$ is compact (finite union of compacts). ✓
- **Arbitrary unions are open**: Union of opens in $X$ is open in $X$. Union of an open in $X$ with $X^+ \setminus K$ is $X^+ \setminus (K \setminus U)$ where $U$ is the open in $X$; $K \setminus U$ is closed in $K$, hence compact. ✓ Union of $X^+ \setminus K_\alpha$'s is $X^+ \setminus \bigcap K_\alpha$, and intersection of compacts in Hausdorff is closed in any $K_{\alpha_0}$, hence compact. ✓

**Hausdorffness.** Two distinct points $x, y \in X$ are separated by Hausdorffness of $X$. Distinct $x \in X$ and $\infty$: by local compactness, $x$ has a compact neighborhood $K$; $\text{int}(K)$ is open in $X$, $X^+ \setminus K$ is open in $X^+$, and they are disjoint and contain $x, \infty$ respectively.

**Compactness.** Take an open cover of $X^+$. One element must contain $\infty$, so has form $X^+ \setminus K$ for compact $K$. The other elements cover $K$ (or some of them do); restrict to opens in $X$ if necessary; by compactness of $K$, finite subcover. Add $X^+ \setminus K$ back, get finite subcover of $X^+$.

**Uniqueness.** Let $Y$ be another compact Hausdorff space with $X$ embedded as open with $Y \setminus X = \{*\}$. Define $h : X^+ \to Y$ by $h|_X =$ embedding, $h(\infty) = *$. The map is continuous: open sets in $Y$ are either contained in $X$ (open in $X$, mapped to open in $X \subseteq X^+$) or of the form $Y \setminus K$ with $K$ closed; $K \subseteq Y$ compact (since closed in compact $Y$); under $h$, $K$ is identified with a closed subset of $X$ that is compact (compactness is intrinsic), so $h^{-1}(Y \setminus K) = X^+ \setminus K$ open. Hence $h$ is a continuous bijection from compact to Hausdorff, hence a homeomorphism.

**Stereographic projection.** The explicit homeomorphism $(\mathbb{R}^n)^+ \cong S^n$ is constructed via stereographic projection from the north pole $N$ of $S^n$: each point of $S^n \setminus \{N\}$ projects to a unique point of $\mathbb{R}^n$ (the line through $N$ and the sphere point hits the equatorial hyperplane at a unique point); $N$ corresponds to $\infty$. The map is a continuous bijection from compact $S^n$ to Hausdorff $(\mathbb{R}^n)^+$, hence a homeomorphism.

---

# What Makes This Hard

The non-obvious step is the **uniqueness**: convincing oneself that the topology on $X^+$ is the *only* possible topology making $X^+$ compact Hausdorff with $X$ open and single-point complement. The argument requires recognizing that compactness of subsets is intrinsic (unchanged by ambient embedding) and so the open neighborhoods of $\infty$ are forced. The most common error in the existence proof is to forget that **complements of compacts are open by definition** in the construction — this is what makes the topology well-defined; without this, $\infty$ would have insufficient neighborhoods and Hausdorffness would fail. Another slip is forgetting that local compactness is *essential* for Hausdorffness — without it, $\infty$ cannot be separated from points of $X$.

---

# Rederivation Scaffold

**High-level strategy:**
Define the topology on $X^+$ as the disjoint union of "opens in $X$" and "complements of compacts containing $\infty$". Verify the topology axioms. Verify Hausdorffness using local compactness. Verify compactness directly from the cover structure. Verify uniqueness by noting that the topology is forced.

**Subgoal decomposition:**

1. **Verify $\tau^+$ is a topology.** Show closure under finite intersection and arbitrary union.
   - *Hint:* The "$X^+ \setminus K$" form is closed under finite intersection (union of compacts is compact) and arbitrary union (intersection of compacts in Hausdorff is compact); the mixed case is direct.
   - *Why needed:* Establishes the construction.

2. **Verify $X^+$ is Hausdorff.** Separate distinct points.
   - *Hint:* For $x, y \in X$, use Hausdorffness of $X$. For $x \in X$ and $\infty$, use local compactness of $X$ to find a compact neighborhood of $x$ disjoint from $\infty$.
   - *Why needed:* Half of the conclusion (compactness is the other half).

3. **Verify $X^+$ is compact.** Show every open cover has a finite subcover.
   - *Hint:* Some cover element contains $\infty$, so contains $X^+ \setminus K$ for $K$ compact; cover $K$ with finitely many of the rest.
   - *Why needed:* The main conclusion.

4. **Verify $X \hookrightarrow X^+$ is open dense.** Show $X$ is open in $X^+$ (true by definition) and dense (when $X$ is not compact, every neighborhood of $\infty$ meets $X$).
   - *Why needed:* Completes the structural description.

5. **Verify uniqueness.** Show any compact Hausdorff space $Y$ with $X$ embedded as open with single-point complement is homeomorphic to $X^+$.
   - *Hint:* Define a continuous bijection $X^+ \to Y$ and use compact-to-Hausdorff continuous bijection is homeomorphism.
   - *Why needed:* Characterization of $X^+$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Verification of topology axioms
> **Statement:** The collection $\tau^+ = \{U \subseteq X^+ : U \subseteq X, U \text{ open in } X\} \cup \{X^+ \setminus K : K \subseteq X \text{ compact}\}$ is a topology on $X^+$.
>
> **Hint:** Check $\emptyset, X^+ \in \tau^+$; closure under finite intersection (compactness of finite unions); closure under arbitrary union (using closedness of compact sets in Hausdorff $X$).
>
> **Why needed:** Verifies the construction is well-defined.
>
> > [!note]- Full proof
> > $\emptyset \in \tau^+$ (open in $X$). $X^+ = X^+ \setminus \emptyset$ with $\emptyset$ compact, so $X^+ \in \tau^+$. ✓
> >
> > Finite intersection: Let $U_1, U_2 \in \tau^+$.
> > - Both open in $X$: $U_1 \cap U_2$ open in $X$ ($X$'s topology). ✓
> > - $U_1$ open in $X$, $U_2 = X^+ \setminus K$: $U_1 \cap U_2 = U_1 \cap (X \setminus K)$. Since $K$ compact in Hausdorff $X$, $K$ closed in $X$, so $X \setminus K$ open in $X$, so $U_1 \cap (X \setminus K)$ open in $X$. ✓
> > - Both $X^+ \setminus K_i$: $\bigcap (X^+ \setminus K_i) = X^+ \setminus (K_1 \cup K_2)$, and $K_1 \cup K_2$ compact (finite union of compacts). ✓
> >
> > Arbitrary union: Let $\{U_\alpha\} \subseteq \tau^+$.
> > - Indices split into "open in $X$" (set $A$) and "$X^+ \setminus K_\alpha$" (set $B$).
> > - $\bigcup_{\alpha \in A} U_\alpha$ open in $X$.
> > - $\bigcup_{\alpha \in B} (X^+ \setminus K_\alpha) = X^+ \setminus \bigcap_{\alpha \in B} K_\alpha$. $\bigcap K_\alpha$ closed in $X$ (intersection of closed in Hausdorff $X$, since $K_\alpha$ closed); contained in any $K_{\alpha_0}$, compact (closed in compact is compact). So $X^+ \setminus \bigcap K_\alpha \in \tau^+$.
> > - The total union is $(\bigcup_{\alpha \in A} U_\alpha) \cup (X^+ \setminus \bigcap_{\alpha \in B} K_\alpha)$, a union of an "open in $X$" with an "$X^+ \setminus K$"; we need this in $\tau^+$. Setting $V = \bigcup_{\alpha \in A} U_\alpha$ open in $X$ and $W = X^+ \setminus \bigcap_{\alpha \in B} K_\alpha$, we have $V \cup W = X^+ \setminus (X^+ \setminus V) \cap (X^+ \setminus W) = X^+ \setminus ((X \setminus V) \cap \bigcap K_\alpha)$. The set $(X \setminus V) \cap \bigcap K_\alpha$ is closed in any $K_\alpha$, hence compact. So $V \cup W \in \tau^+$. ✓

> [!note]- Lemma 2: Continuous bijection from compact to Hausdorff is homeomorphism
> **Statement:** If $f : X \to Y$ is a continuous bijection from a compact space $X$ to a Hausdorff space $Y$, then $f$ is a homeomorphism.
>
> **Hint:** Show $f$ is closed: $f^{-1}$ continuous iff $f$ is open iff $f$ is closed (for bijections); closed subsets of compact are compact, continuous images of compact are compact, compact subsets of Hausdorff are closed.
>
> **Why needed:** Uniqueness of $X^+$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $X$ be LCH. Define $X^+ = X \cup \{\infty\}$ with $\tau^+$ as above.
>
> **(1) Topology.** By Lemma 1, $\tau^+$ is a topology.
>
> **(2.a) Hausdorff.** Two points $x, y \in X$: by Hausdorff of $X$, find disjoint opens $U, V$ in $X$; they remain disjoint opens in $X^+$.
>
> A point $x \in X$ and $\infty$: by local compactness, $x$ has a compact neighborhood $K \subseteq X$, with $\text{int}(K)$ open in $X$, $x \in \text{int}(K)$. Then $\text{int}(K)$ and $X^+ \setminus K$ are disjoint opens in $X^+$ separating $x$ from $\infty$.
>
> **(2.b) Compact.** Let $\{W_\alpha\}$ be an open cover of $X^+$. $\infty \in W_{\alpha_0}$ for some $\alpha_0$; by definition $W_{\alpha_0}$ contains $\infty$, so $W_{\alpha_0} = X^+ \setminus K$ for some compact $K \subseteq X$ (the form including $\infty$).
>
> Restrict the remaining cover to $K$: each $W_\alpha$ ($\alpha \neq \alpha_0$) intersects $K$ in an open subset (in either case, open in $X$, hence open in $K$). So $\{W_\alpha \cap K : \alpha \neq \alpha_0\}$ is an open cover of $K$, and by compactness of $K$, a finite subcover $W_{\alpha_1} \cap K, \dots, W_{\alpha_n} \cap K$ covers $K$. Then $W_{\alpha_0}, W_{\alpha_1}, \dots, W_{\alpha_n}$ cover $X^+$ (everything except $K$ is in $W_{\alpha_0}$; $K$ is covered by the others).
>
> **(3) Open dense embedding.** The inclusion $X \hookrightarrow X^+$ takes open in $X$ to open in $X^+$ (by the very definition of $\tau^+$), hence is an open map and continuous. Injective. So it is an open embedding.
>
> For density (when $X$ is non-compact): every neighborhood of $\infty$ is $X^+ \setminus K$ for some compact $K \subsetneq X$ (proper since $X$ non-compact), so contains $X \setminus K \neq \emptyset$, i.e., meets $X$. Hence $\infty \in \overline X$, and $\overline X = X^+$.
>
> **(4) Uniqueness.** Let $Y$ be a compact Hausdorff space with an open embedding $X \hookrightarrow Y$ such that $Y \setminus X = \{*\}$. Define $h : X^+ \to Y$ by $h|_X =$ embedding, $h(\infty) = *$.
>
> $h$ is bijective by construction. Continuous: open sets in $Y$ either lie in $X$ (open in $X \subseteq X^+$ — open in $X^+$) or contain $*$. An open in $Y$ containing $*$ is $Y \setminus C$ for some closed $C \subseteq Y$, with $* \notin C$, so $C \subseteq X$; $C$ closed in $Y$ compact, hence compact; under $h$, $C$ corresponds to the same compact subset of $X$; so $h^{-1}(Y \setminus C) = X^+ \setminus C$, open in $X^+$. So $h$ is continuous.
>
> By Lemma 2, $h$ is a homeomorphism. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The Riemann sphere $\widehat{\mathbb{C}} = \mathbb{C}^+$.** Identify $\widehat{\mathbb{C}} = S^2$ via stereographic projection. Complex analysis is naturally done on $\widehat{\mathbb{C}}$ — meromorphic functions become continuous functions $\widehat{\mathbb{C}} \to \widehat{\mathbb{C}}$, with poles mapped to $\infty$. The Riemann sphere is the standard target for the chordal metric and the natural setting for the theory of rational functions. The one-point compactification turns the "uncompleted" $\mathbb{C}$ into a compact Riemann surface.

**Alexandroff compactification of $\mathbb{Z}$.** $\mathbb{Z}^+ = \mathbb{Z} \cup \{\infty\}$ is a countable compact Hausdorff space — in fact, homeomorphic to the convergent sequence $\{1/n : n \in \mathbb{N}\} \cup \{0\}$ in $\mathbb{R}$. This is the "simplest" infinite compact Hausdorff space (after finite ones), and it appears as a test case for measure-theoretic and functional-analytic constructions.

**Locally compact abelian groups and Pontryagin duality.** For an LCAG $G$, the dual group $\hat G$ is also an LCAG. Pontryagin duality says $\hat{\hat G} \cong G$ canonically. The one-point compactification plays a role: a function $f : G \to \mathbb{C}$ vanishing at infinity (i.e., $f \in C_0(G)$) extends to a continuous function $G^+ \to \mathbb{C}$ with value $0$ at $\infty$. The Fourier transform on $C_0(G)$ is the bridge to harmonic analysis.

---

# Bridges

- **[[Def - Locally Compact Space]]** — the precondition; LCH is exactly the right setting for one-point compactification.

- **[[Thm - Stone–Čech Compactification]]** — the *maximal* compactification, at the opposite end of the spectrum. One-point is minimal; Stone–Čech adds maximally many points. Different problems call for different compactifications.

- ****LCH implies completely regular**** — LCH implies completely regular (proved via the one-point compactification: the compact $X^+$ is normal, restrict separating functions back).

- **[[Def - Compact Space]]** — the property gained by $X^+$.

- **Functoriality of $(\cdot)^+$** — proper maps extend to maps of one-point compactifications fixing $\infty$.

---

# Unlocked by This

> [!tip] Riemann Sphere *(from Complex Analysis)*
> $\widehat{\mathbb{C}} = \mathbb{C} \cup \{\infty\} = S^2$ is the one-point compactification of $\mathbb{C}$. It is the natural setting for the theory of rational functions, meromorphic functions, and Möbius transformations.

> [!tip] $C_0(X)$ as a Closed Ideal *(from Functional Analysis)*
> The space $C_0(X)$ of continuous functions on an LCH space vanishing at infinity is naturally identified with $\{f \in C(X^+) : f(\infty) = 0\}$ — a closed ideal in $C(X^+)$. Pointwise convergence in $C_0(X)$ corresponds to pointwise convergence in $C(X^+)$ with the value $0$ at $\infty$.

> [!tip] Borel–Moore Homology *(from Algebraic Topology)*
> The **Borel–Moore homology** of an LCH space $X$ is the relative homology of the pair $(X^+, \infty)$. The one-point compactification provides the "closed at infinity" structure needed for this dual theory.

> [!tip] Spectral Theory of $C_0(X)$ *(from Functional Analysis)*
> The commutative $C^*$-algebra $C_0(X)$ for $X$ LCH has spectrum (maximal ideal space) equal to $X$. The maximal ideal at infinity is the kernel of evaluation at $\infty$ in $C(X^+)$.
