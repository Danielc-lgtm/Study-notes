---
type: topic
subject: topology
chapter: "1-3"
title: "Topology I — §1–3 Metric Spaces, Topological Spaces, Subspaces"
tags: [analysis, topology]
---

# Notation Registry

- $X, Y, Z$ — topological spaces; $A, B, C$ — subsets
- $\tau$ — a topology (collection of open sets) on $X$; $(X, \tau)$ — a topological space
- $d, \rho$ — metrics; $d(x, y)$ — the distance from $x$ to $y$
- $(X, d)$ — a metric space
- $B_\varepsilon(x) = \{y \in X : d(x, y) < \varepsilon\}$ — the open ball of radius $\varepsilon$ about $x$
- $\overline{B_\varepsilon(x)} = \{y : d(x,y) \leq \varepsilon\}$ — the closed ball; in general $\overline{B_\varepsilon(x)} \neq \{y : d(x,y) \leq \varepsilon\}$, but the two coincide in $\mathbb{R}^n$
- $\mathcal{P}(X)$ — the power set of $X$
- $\mathcal{B}$ — a basis for a topology
- $\mathcal{N}(x)$ or $\mathcal{B}_x$ — a neighbourhood basis at $x$
- $\overline{A}$ or $\operatorname{cl}(A)$ — the closure of $A$
- $A^\circ$ or $\operatorname{int}(A)$ — the interior of $A$
- $\partial A$ — the boundary, $\overline{A} \setminus A^\circ$
- $f : X \to Y$ — a function; $f^{-1}(U)$ — the preimage of $U$
- A **map** is a continuous function
- $\mathbb{R}, \mathbb{Q}, \mathbb{Z}, \mathbb{N}$ — reals, rationals, integers, natural numbers
- $\mathbb{R}^n$ — Euclidean $n$-space with the standard topology
- $C^0(X, Y), C(X, Y)$ — continuous maps $X \to Y$
- $C[0,1]$ — continuous real-valued functions on $[0,1]$
- $\lVert f - g\rVert_\infty = \sup_x |f(x) - g(x)|$ — the uniform-norm distance on $C[0,1]$
- $X \cong Y$ — $X$ is homeomorphic to $Y$
- $A \subseteq Y \subseteq X$ — $A$ is a subset of the subspace $Y$
- $\overline{A}^Y$, $\overline{A}^X$ — closure of $A$ taken in $Y$ versus in $X$
- $f|_A$ — the restriction of $f$ to $A$

---

# Motivation

Analysis in $\mathbb{R}^n$ rests on one notion above all others — **continuity** — and the entire structure of the topic is the story of stripping continuity down to the minimum data needed to define it.

The starting point is the $\varepsilon$–$\delta$ definition you learned in a first analysis course. To say $f : \mathbb{R}^n \to \mathbb{R}^k$ is continuous at $x$ is to say: for every $\varepsilon > 0$ there is $\delta > 0$ such that $|x' - x| < \delta$ forces $|f(x') - f(x)| < \varepsilon$. The definition is built out of the *distance function* $|x - y|$, and one might naively think distance is what continuity *means*. It is not. The first observation, due to Hausdorff and Fréchet at the turn of the twentieth century, is that continuity is equivalent to a statement using only the *open sets* of $\mathbb{R}^n$: $f$ is continuous if and only if $f^{-1}(U)$ is open whenever $U$ is. Distance has been *forgotten* — only the collection of open sets matters.

The reason to forget distance is that mathematics is full of spaces that have natural notions of continuity but no natural metric, or many candidate metrics that give the same continuity. The space of continuous functions on $[0,1]$ has at least three reasonable distances (the sup, the $L^1$, and the $L^2$ distance), and they give *different* notions of "close" but the same notion of "continuous" only if we restrict to special classes. A quotient space — say, a circle viewed as $[0,1]$ with the two endpoints identified — has no natural distance from its construction, yet it has an obvious notion of which functions on it are continuous. A space of formal power series, or a set with the Zariski topology from algebraic geometry, may have no compatible metric at all. To talk uniformly about continuity in all these places, we need a notion of space that has open sets and nothing else.

That notion is the **topological space**: a set $X$ together with a distinguished collection $\tau \subseteq \mathcal{P}(X)$ of "open" subsets, closed under finite intersections and arbitrary unions, containing the empty set and $X$ itself. Continuity is then, by *definition*, $f^{-1}(U) \in \tau_X$ for every $U \in \tau_Y$. The axioms are exactly what one needs to verify the standard manipulations of $\varepsilon$–$\delta$ proofs work in the abstract — pulling back unions and intersections, composing continuous functions, taking restrictions. Anything stronger would exclude genuine examples; anything weaker would not support the theory.

§1–3 of the topic builds this framework. §1 introduces the metric space — distance with three axioms — as the bridge from $\mathbb{R}^n$ to general topology. §2 introduces the topological space itself, with the basis machinery for specifying a topology efficiently, and with the central concept of a homeomorphism (a continuous bijection with continuous inverse — the topology's notion of "the same"). §3 introduces the subspace topology, the way a subset $A \subseteq X$ inherits a topology, and the related notions of closure, interior, and boundary that recover from the abstract axioms the familiar features of a subset of $\mathbb{R}^n$. The payoff is that everything one wants to say about *continuity* in the most general setting becomes statable, and the rest of the topology course — connectedness, compactness, the separation axioms, quotients, homotopy — develops in this language.

The story to keep in mind: the *true name* of a topology is "the data needed to define continuity". The reason the axioms look the way they do is that they capture exactly the properties of open sets in $\mathbb{R}^n$ that the $\varepsilon$–$\delta$ definition actually used. Everything else is downstream of this single design decision.

---

# Concept Map

## §1 Metric Spaces

- **[[Def - Metric Space]]**
	- A **metric** on a set $X$ is a function $d : X \times X \to \mathbb{R}_{\geq 0}$ satisfying positivity ($d(x,y) = 0 \iff x = y$), symmetry, and the triangle inequality $d(x,z) \leq d(x,y) + d(y,z)$. The pair $(X, d)$ is a **metric space**. Euclidean $\mathbb{R}^n$ is the prototype; other examples include $C[0,1]$ with the sup metric, the discrete metric $d(x,y) = 1$ for $x \neq y$, and any subset of a metric space with the induced distance. The axioms are exactly what is needed to develop $\varepsilon$–$\delta$ continuity.

- **[[Def - Open and Closed Sets in a Metric Space]]**
	- An **open ball** is $B_\varepsilon(x) = \{y : d(x,y) < \varepsilon\}$. A set $U$ is **open** if every $x \in U$ has some ball $B_\varepsilon(x) \subseteq U$; a set is **closed** if its complement is open. Open balls are open (triangle inequality), the empty set and $X$ are open, arbitrary unions and finite intersections of open sets are open. The collection of opens depends only on which sequences converge to which limits, not on the particular numerical distances.

- **[[Thm - Continuity via Open Sets (Metric Spaces)]]**
	- For $f : (X, d) \to (Y, \rho)$, the $\varepsilon$–$\delta$ definition of continuity at every point is equivalent to: $f^{-1}(U)$ is open in $X$ whenever $U$ is open in $Y$. This is the bridge from metric data to topological data — it shows that continuity is determined by the open-set structure alone, and licenses the next abstraction. The same map $f$ may be continuous with respect to one metric and not another, but two metrics that produce the same open sets always produce the same continuous functions.

- **[[Def - Equivalent Metrics]]**
	- Two metrics $d_1, d_2$ on the same set $X$ are **topologically equivalent** if they generate the same open sets, equivalently if the identity map $(X, d_1) \to (X, d_2)$ is a homeomorphism, equivalently if every $d_1$-ball contains a $d_2$-ball about the same point and vice versa. On $\mathbb{R}^n$ the three standard metrics — Euclidean $\ell^2$, taxicab $\ell^1$, and sup $\ell^\infty$ — are topologically equivalent, even though their geometries (the shape of balls) differ. The notion of equivalence is what lets one pass freely between metrics that look different but encode the same continuity.

- **[[Ex - Verifying a metric and computing its topology]]** (⭐)
	- Show that $d(x,y) = \int_0^1 |x(t) - y(t)|\, dt$ defines a metric on $C[0,1]$ and identify a neighbourhood basis at the zero function.

- **[[Ex - The discrete metric and topology]]** (⭐)
	- Take any set $X$ and define $d(x,y) = 1$ for $x \neq y$, $d(x,x) = 0$. Verify this is a metric, identify all open and closed sets, and show that every function from $X$ into any space is continuous.

- **[[Ex - Sup metric versus L1 metric on C01]]** (⭐⭐)
	- Show that the sup metric $d_\infty(f,g) = \sup |f - g|$ and the integral metric $d_1(f,g) = \int|f-g|$ on $C[0,1]$ are not topologically equivalent by exhibiting a sequence $f_n$ converging in $d_1$ but not in $d_\infty$.

> [!note] Exercise Index — §1
> [[Exercise Index - §1 Metric Spaces]]

## §2 Topological Spaces

- **[[Def - Topological Space]]**
	- A **topology** on a set $X$ is a collection $\tau \subseteq \mathcal{P}(X)$ such that (i) $\emptyset, X \in \tau$, (ii) finite intersections of elements of $\tau$ are in $\tau$, and (iii) arbitrary unions of elements of $\tau$ are in $\tau$. The pair $(X, \tau)$ is a **topological space** and elements of $\tau$ are **open sets**. Metric spaces are topological spaces; the discrete topology ($\tau = \mathcal{P}(X)$), the indiscrete topology ($\tau = \{\emptyset, X\}$), the cofinite topology, and the Zariski topology give examples beyond metric ones. The axioms are minimal: they hold in every space where the $\varepsilon$–$\delta$ proof techniques work.

- **[[Def - Continuous Map]]**
	- A function $f : X \to Y$ between topological spaces is **continuous** if $f^{-1}(U) \in \tau_X$ for every $U \in \tau_Y$. Equivalently, $f^{-1}(F)$ is closed for every closed $F$. The composition of continuous maps is continuous; constants are continuous; the identity is continuous. A **map** in topology means a continuous function — the word carries this default meaning throughout the subject.

- **[[Def - Homeomorphism]]**
	- A **homeomorphism** $f : X \to Y$ is a continuous bijection whose inverse $f^{-1}$ is also continuous. Spaces related by a homeomorphism are **topologically equivalent** ($X \cong Y$): every topological property of one is shared by the other. A continuous bijection is *not* automatically a homeomorphism — for instance, $[0, 2\pi) \to S^1$ by $t \mapsto e^{it}$ is a continuous bijection but the inverse is discontinuous at $1$. The classification of spaces up to homeomorphism is one of the central problems of topology.

- **[[Def - Basis and Subbasis for a Topology]]**
	- A **basis** $\mathcal{B}$ for a topology on $X$ is a collection of subsets such that (i) every $x \in X$ lies in some $B \in \mathcal{B}$, and (ii) if $x \in B_1 \cap B_2$ for $B_1, B_2 \in \mathcal{B}$ then $x \in B_3 \subseteq B_1 \cap B_2$ for some $B_3 \in \mathcal{B}$. The topology *generated* by $\mathcal{B}$ has as open sets all unions of basis elements. A **subbasis** is any collection of subsets; the topology generated takes finite intersections to form a basis, then unions. Bases give the standard way to *specify* a topology on a set without listing all open sets — the metric ball basis is the prototype.

- **[[Def - Neighbourhood and Neighbourhood Basis]]**
	- A **neighbourhood** of $x \in X$ is any set $N$ containing an open set $U$ with $x \in U \subseteq N$; in particular $N$ need not itself be open. A **neighbourhood basis** at $x$ is a collection $\mathcal{B}_x$ of neighbourhoods of $x$ such that every neighbourhood of $x$ contains some $B \in \mathcal{B}_x$. In a metric space, the balls $B_{1/n}(x)$ form a countable neighbourhood basis at $x$. Neighbourhood bases give the local version of "basis for a topology" and are the natural tool for checking continuity *at a point*.

- **[[Def - First and Second Countable]]**
	- $X$ is **first countable** if every point has a countable neighbourhood basis; this is automatic for metric spaces. $X$ is **second countable** if the whole topology has a countable basis. Second countable implies first countable (a global basis localizes), and second countable spaces are *separable* (have a countable dense subset). $\mathbb{R}^n$ is second countable (rational-radius balls about rational points); the long line is first countable but not second. These countability axioms are how "topology behaves like analysis" is precisely formulated.

- **[[Thm - Continuity via Bases and Neighbourhood Bases]]**
	- $f : X \to Y$ is continuous if and only if $f^{-1}(B)$ is open for every $B$ in some basis (equivalently subbasis) of $Y$; continuity at $x$ is equivalent to: for every $N$ in a neighbourhood basis at $f(x)$, $f^{-1}(N)$ is a neighbourhood of $x$. This is the workhorse for verifying continuity in practice: one rarely checks the preimage of *every* open set; one checks the preimage of a generating family. The basis version is what makes the product, quotient, and weak topologies tractable.

> [!warning] Continuous bijection ≠ homeomorphism
> A continuous bijection need not have a continuous inverse. The standard counterexample is the *winding map* $f : [0, 2\pi) \to S^1$, $f(t) = (\cos t, \sin t)$: continuous, bijective, but the inverse $S^1 \to [0, 2\pi)$ is discontinuous at $f(0) = (1, 0)$ — a small neighbourhood of that point pulls back to a *disconnected* set (the union of $[0, \delta)$ and $(2\pi - \delta, 2\pi)$). The fix that works in many contexts: if $X$ is compact and $Y$ is Hausdorff, a continuous bijection is automatically a homeomorphism (proved in [[Topology II — §4–7 Connectivity, Separation, Nets, Compactness]]).

- **[[Ex - The half-open interval topology on the real line]]** (⭐⭐)
	- Give $\mathbb{R}$ the topology generated by the basis $\{[a, b) : a < b\}$ (the **Sorgenfrey line**). Show that it is finer than the standard topology, that every set $[a, b)$ is clopen, and that the identity map from the Sorgenfrey line to standard $\mathbb{R}$ is continuous but not a homeomorphism.

- **[[Ex - Three equivalent metrics on Rn]]** (⭐)
	- Show that $\ell^1$, $\ell^2$, and $\ell^\infty$ metrics on $\mathbb{R}^n$ are pairwise topologically equivalent by exhibiting explicit ball-containment constants $c_1, c_2$ with $c_1 d_1(x,y) \leq d_2(x,y) \leq c_2 d_1(x,y)$.

- **[[Ex - The cofinite topology]]** (⭐⭐)
	- Define the **cofinite topology** on $X$: a set is open iff it is empty or has finite complement. Show this is a topology, identify all closed sets, and decide when it equals the discrete topology. Show that on an infinite set every continuous function $X \to \mathbb{R}$ with $\mathbb{R}$ Hausdorff must be constant.

- **[[Ex - Generating a topology from a subbasis]]** (⭐⭐)
	- Show that any collection $\mathcal{S} \subseteq \mathcal{P}(X)$ generates a unique smallest topology containing $\mathcal{S}$. Construct it explicitly via finite intersections then arbitrary unions, and verify the resulting collection satisfies the topology axioms.

> [!tip] Unlocked: Borel σ-algebra *(from Measure Theory)*
> Once $X$ has a topology, the σ-algebra generated by the open sets is the **Borel σ-algebra** $\mathcal{B}(X)$ — see **Def - Sigma-Algebra** in measure theory. Borel sets are how the *measurable* world inherits structure from the topological world, and the construction is parallel: a σ-algebra is closed under countable unions and *complementation*, while a topology is closed under arbitrary unions and finite intersections without the complementation axiom. The two axiom systems are sisters, not the same.

> [!tip] Unlocked: Weak Topology *(from Functional Analysis)*
> Given a vector space $V$ and a family of linear functionals $\{\varphi_\alpha\}$, the **weak topology** is the *coarsest* topology making every $\varphi_\alpha$ continuous — concretely, the topology generated by the subbasis $\{\varphi_\alpha^{-1}(U) : U \subseteq \mathbb{R}\text{ open}\}$. The subbasis construction here is exactly the mechanism that gives weak convergence, weak-$*$ convergence, and the Banach–Alaoglu theorem their reason for being.

> [!note] Exercise Index — §2
> [[Exercise Index - §2 Topological Spaces]]

## §3 Subspaces, Closure, and Interior

- **[[Def - Subspace Topology]]**
	- For $Y \subseteq X$ a subset of a topological space, the **subspace topology** on $Y$ has open sets $U \cap Y$ as $U$ ranges over open sets of $X$. This is the unique topology on $Y$ making the inclusion $Y \hookrightarrow X$ continuous *and* making every continuous $f : Z \to X$ with $f(Z) \subseteq Y$ restrict to a continuous $Z \to Y$ (the universal property). On metric spaces it agrees with the metric inherited by restriction. A set may be open in $Y$ but not in $X$: $[0, 1)$ is open in $[0, \infty)$ (it equals $(-\varepsilon, 1) \cap [0, \infty)$) but not in $\mathbb{R}$.

- **[[Def - Closure, Interior, and Boundary]]**
	- The **closure** $\overline{A}$ of $A \subseteq X$ is the smallest closed set containing $A$; equivalently, the intersection of all closed sets $\supseteq A$. The **interior** $A^\circ$ is the largest open set contained in $A$. The **boundary** $\partial A = \overline{A} \setminus A^\circ$ is what is in the closure but not the interior. The space decomposes as a disjoint union $X = A^\circ \sqcup \partial A \sqcup (X \setminus \overline{A})$ — three regions: deeply inside, exactly on the edge, deeply outside.

- **[[Thm - Characterizations of the Closure]]**
	- For $A \subseteq X$: $x \in \overline{A}$ if and only if every open set containing $x$ meets $A$, if and only if every neighbourhood of $x$ meets $A$, if and only if every basis element containing $x$ meets $A$. In a metric space (or any first-countable space), this is equivalent to: there is a sequence in $A$ converging to $x$. Closure is the topological version of "limit point" — every other limit notion in the subject is downstream.

- **[[Def - Dense Subset]]**
	- $A \subseteq X$ is **dense** if $\overline{A} = X$, equivalently every nonempty open set in $X$ meets $A$, equivalently every point of $X$ is the limit of points in $A$ (in first-countable settings). $\mathbb{Q}$ is dense in $\mathbb{R}$; the polynomials are dense in $C[0,1]$ by Stone–Weierstrass; the simple functions are dense in $L^p$. Density is the formal version of "$A$ approximates everything in $X$" and is the strategic engine of approximation arguments throughout analysis.

- **[[Thm - Closure-in-Subspace Formula]]**
	- For $A \subseteq Y \subseteq X$, $\overline{A}^Y = \overline{A}^X \cap Y$. The closure taken in the subspace is the trace of the closure taken in the ambient space. The corresponding statement for interiors is *false* — taking interior in $Y$ may pick up points that are not interior in $X$, because "open in $Y$" is weaker than "open in $X$". This asymmetry is a small but persistent source of bugs in topology arguments.

- **[[Thm - The Pasting Lemma]]**
	- If $X = A \cup B$ with $A, B$ both closed (or both open), $f : A \to Y$ and $g : B \to Y$ continuous with $f|_{A \cap B} = g|_{A \cap B}$, then the function defined by $f$ on $A$ and $g$ on $B$ is continuous on $X$. This is the standard tool for constructing piecewise-defined continuous maps. The agreement condition on the overlap is necessary; the closedness (or openness) hypothesis cannot be dropped — pasting a continuous function on $(0,1]$ to a different one on $\{0\}$ may produce a discontinuous result.

- **[[Ex - Closure of the rationals in different topologies]]** (⭐)
	- Compute $\overline{\mathbb{Q}}$ in (a) the standard topology on $\mathbb{R}$, (b) the discrete topology, (c) the cofinite topology, (d) the Sorgenfrey topology, and explain how each answer reads off the topology.

- **[[Ex - Constructing a continuous map by pasting]]** (⭐⭐)
	- Construct an explicit homeomorphism $[0,1] \cup [1, 2] \to [0,2]$ using the pasting lemma, and identify exactly where the closedness hypothesis is used.

- **[[Ex - A continuous bijection that is not a homeomorphism]]** (⭐⭐)
	- Show explicitly that $f : [0, 2\pi) \to S^1$, $f(t) = (\cos t, \sin t)$, is a continuous bijection but its inverse is discontinuous at $(1, 0)$, by exhibiting an open set whose image is not open.

> [!tip] Unlocked: Submanifold Topology *(from Differential Geometry)*
> A **submanifold** $M \subseteq \mathbb{R}^n$ — see [[Def - Submanifold of Euclidean Space]] — is a topological subspace of $\mathbb{R}^n$ before it is anything else, and almost every property one wants is a property of this subspace topology: that $M$ is locally homeomorphic to $\mathbb{R}^d$, that continuous maps $M \to \mathbb{R}$ are well-defined, that "tangent space" makes sense. The implicit function theorem produces submanifolds; the subspace topology of §3 is what they sit in.

> [!note] Exercise Index — §3
> [[Exercise Index - §3 Subspaces and Closure]]

---

# Sources and Targets

**Targets — What do we usually try to prove?**

Most arguments at this level have one of three goals. The first is **continuity** of a specific map — showing that a function constructed from simpler ones (projections, restrictions, compositions, evaluations, piecewise definitions) is continuous. This is the most common target, and the standard route is to reduce to a basis: prove $f^{-1}(B)$ is open for $B$ in a generating family, rather than for every open set. Continuity-of-a-map proofs ultimately rely on one or two structural results (the pasting lemma, the basis criterion, the universal properties of subspace and product topology) being applied in series.

The second target is **identification of the topology** on some new space: showing that the topology one has constructed (subspace, product, quotient, generated-by-a-basis, induced-by-a-metric) is or is not the same as some other topology one has in mind. The standard route is to show open sets generate each other, often by exhibiting bases: every basis element of one topology contains a basis element of the other about each of its points.

The third target is **a topological invariant** — proving two spaces are or are not homeomorphic. Two spaces are homeomorphic if and only if every topological property is shared, so to prove they are *not* homeomorphic one finds a property held by one and not the other (number of connected components, compactness, presence of points whose complement is disconnected). To prove they *are* homeomorphic, one constructs an explicit map and verifies continuity in both directions.

**Sources — What assumptions do we usually leverage?**

The recurring assumption patterns are: a hypothesis on the *generating data* (a metric, a basis, a subbasis), a hypothesis on the *target* (Hausdorff, metric, $\mathbb{R}^n$), or a *structural* hypothesis (subspace of a known space, image under a continuous map, pasting of two pieces). Almost every theorem in §1–3 routes from one of these source types to one of the three target types above through a single principal theorem: continuity-via-basis, the pasting lemma, the closure characterization, or the subspace universal property.

When the source is a metric, the bridge to the topological setting goes through the open-ball basis: ball-level $\varepsilon$–$\delta$ estimates become open-set arguments via the [[Thm - Continuity via Open Sets (Metric Spaces)|metric-continuity-via-opens]] theorem. When the source is a basis, the bridge to the topological setting goes through "every open set is a union of basis elements". When the source is a subspace or quotient, the bridge is the universal property of that construction. Almost every problem reduces, in two or three steps, to *one* of these bridges.

---

# Legal Operations

The collection of moves available to topology arguments is small but very powerful. Each one is best learned as a "when you see X, do Y" reflex.

1. **Reduce continuity to a basis or subbasis check.** Given $f : X \to Y$, instead of verifying $f^{-1}(U)$ is open for every open $U$, choose a basis $\mathcal{B}$ (or subbasis) for the topology on $Y$ and verify $f^{-1}(B)$ is open for every $B \in \mathcal{B}$. The unions and intersections in the topology assemble automatically. *Trigger:* checking continuity. *Pattern:* use the metric ball basis on $Y$ when $Y$ is metric, the box basis on $Y = \prod Y_\alpha$, or the natural subbasis defining a weak/quotient topology.

2. **Pass between $\varepsilon$–$\delta$ and open sets.** In a metric space, "$f^{-1}(U)$ is open" *is* the $\varepsilon$–$\delta$ definition of continuity at every point, by [[Thm - Continuity via Open Sets (Metric Spaces)]]. So one can freely switch between the two formulations — write the proof in whichever form is shorter. *Trigger:* a metric on either side. *Pattern:* often a continuity proof is easiest when stated in $\varepsilon$–$\delta$ form on one side and open-set form on the other.

3. **Take closures or interiors and use the universal properties.** $\overline{A}$ is the smallest closed set $\supseteq A$, $A^\circ$ is the largest open set $\subseteq A$. So *any* statement of the form "$A$ is contained in a closed set $F$" gives $\overline{A} \subseteq F$; "an open set $U$ is contained in $A$" gives $U \subseteq A^\circ$. The universal property of closure is what lets one conclude $\overline{f(A)} \subseteq f(\overline{A})$ when $f$ is continuous, just by checking the closed-set definition (preimage of a closed set is closed). *Trigger:* a closed-set or open-set bound to upgrade.

4. **Apply the pasting lemma.** Given a function defined piecewise on a finite closed (or open) cover $X = A_1 \cup \dots \cup A_n$ with compatibility on overlaps, the function is continuous if and only if each piece is. *Trigger:* a piecewise definition. *Pattern:* break $X$ into a small number of closed pieces, verify continuity on each piece, check overlaps agree.

5. **Lift to a subspace via the universal property.** A continuous $f : Z \to X$ with $f(Z) \subseteq Y$ automatically defines a continuous $\tilde f : Z \to Y$ — the corestriction is continuous. Conversely a continuous map $Z \to Y$ extends to a continuous $Z \to X$ via the inclusion. This is the defining property of the subspace topology and is used silently in almost every multistep continuity argument. *Trigger:* dropping into or lifting out of a subspace.

6. **Use the closure-as-limit-of-sequences criterion in a first countable space.** In a metric space (or any first countable space), $\overline{A} = \{x : \exists\ \text{sequence}\ a_n \in A,\ a_n \to x\}$. This turns abstract closure statements into concrete sequence-construction problems. *Trigger:* metric space and a closure-containment statement to prove. *Caveat:* fails in general topological spaces — needs the first-countability assumption, replaced by nets in §6 of [[Topology II — §4–7 Connectivity, Separation, Nets, Compactness]].

7. **Compose continuous maps to build new ones.** Composition of continuous functions is continuous, so a complicated map can be decomposed as a chain $X \to Y_1 \to \dots \to Y_n \to Y$ where each link is recognizably continuous. *Trigger:* a continuity proof for a complicated formula. *Pattern:* identify the function as a composition of (i) coordinate projection, (ii) arithmetic operations like sum, product, inverse, (iii) component-wise operations, (iv) restriction or extension.

8. **Construct a homeomorphism explicitly to prove two spaces are equivalent.** To show $X \cong Y$, write down a continuous bijection $f : X \to Y$ and a continuous inverse $g : Y \to X$. To show $X \not\cong Y$, find a topological invariant — number of components, compactness, presence of a cut point, fundamental group — held by one and not the other.

**Illegal but tempting operations:**

> [!warning] 1. Concluding $\overline{A^\circ} = A$
> It is tempting to think the closure of the interior of $A$ recovers $A$, especially when $A$ is "nice". This fails: take $A = \mathbb{Q} \subseteq \mathbb{R}$, then $A^\circ = \emptyset$ (no open interval lies entirely in $\mathbb{Q}$), so $\overline{A^\circ} = \emptyset \neq \mathbb{R} = \overline{A}$. The relations one *does* have are $A^\circ \subseteq A \subseteq \overline{A}$ and $\overline{A^\circ} \subseteq \overline{A}$, $A^\circ \subseteq (\overline{A})^\circ$ — each containment can be strict.

> [!warning] 2. Treating a continuous bijection as a homeomorphism
> "$f$ is continuous and bijective, so $f^{-1}$ is also continuous" is one of the most common errors in topology. The counterexample is the unwinding map $[0, 2\pi) \to S^1$, which is continuous and bijective but whose inverse has a discontinuity at $(1, 0)$. The conclusion *is* valid when $X$ is compact and $Y$ is Hausdorff — but until those hypotheses are in place, the inverse may not be continuous.

> [!warning] 3. Using sequences to determine the closure in a general topological space
> In a metric space, $\overline{A}$ equals the set of limits of sequences in $A$. In a general topological space this is false: there are spaces where $x \in \overline{A}$ but no sequence in $A$ converges to $x$. The correct general-purpose tool is a *net* (§6), or one restricts attention to first-countable spaces (where the metric intuition is valid). Confusing the two is a source of long-running errors when working with, for example, the product topology on uncountable products or the weak topology on an infinite-dimensional Banach space.

> [!warning] 4. Assuming a subspace inherits every property of the ambient space
> The subspace inherits openness (in the relative sense), closure, and the metric (if any), but does *not* inherit compactness, completeness, or local properties without further hypotheses. The interval $(0,1)$ inherits the standard topology from $\mathbb{R}$, but $\mathbb{R}$ is complete and $(0,1)$ is not. The danger is to apply a theorem from the ambient space to the subspace without checking that its hypotheses still hold.

---

# Problem-Solving Strategy

Almost every problem at this level is one of three types: prove a specific map is continuous, identify or compare two topologies on the same set, or compute the closure / interior / boundary of a specific set.

For **continuity problems**, the universal recipe is to reduce to a basis. Choose a basis or subbasis on the target side — a metric ball basis when the target is a metric space, the standard box basis when the target is a product, a defining subbasis when the target is a weak or quotient topology — and check $f^{-1}(B)$ is open for each generator $B$. The minimization is essential: checking the preimage of every open set is rarely tractable, while a basis usually has a simple description. After the basis reduction, the remaining work is either an $\varepsilon$–$\delta$ estimate (if the source is a metric space) or a structural argument (if the source has a basis whose images one can compute). Composition is the second pillar: if $f = g \circ h$ where $g, h$ are recognizably continuous, $f$ is continuous immediately. The trick in practice is to *recognize* the decomposition — to see that "the maximum of $\sin x$ and $\cos x$" is continuous because $\max$ is continuous on $\mathbb{R}^2$ and $(\sin, \cos)$ is continuous into $\mathbb{R}^2$.

For **topology comparison problems**, choose a basis for each topology and prove they refine each other (or one refines the other strictly). Topology $\tau_1$ is *finer* than $\tau_2$ ($\tau_1 \supseteq \tau_2$) if and only if every $\tau_2$-basis element is a union of $\tau_1$-basis elements, equivalently every $\tau_2$-open set is $\tau_1$-open, equivalently the identity $(X, \tau_1) \to (X, \tau_2)$ is continuous. To prove two topologies are *equal*, prove both refinements. This is the central tool when verifying that a constructed topology has the universal property one wanted; it appears every time one passes between metric, basis, and subbasis definitions of the same topology.

For **closure / interior / boundary problems**, work from the characterization $x \in \overline{A} \iff$ every open neighbourhood of $x$ meets $A$. In a metric space, this is "every ball about $x$ meets $A$", which one verifies by an explicit construction of points of $A$ converging to $x$. To compute $A^\circ$, similarly, find every $x$ for which some ball about $x$ lies in $A$. Boundary follows from $\partial A = \overline{A} \setminus A^\circ$. The *strategy of writing $A$ as a known set in disguise* — e.g. showing the rationals in $[0,1]$ have closure $[0,1]$ by writing every real as a limit of rationals — is often the shortest path.

A non-obvious general principle: in any continuity proof, the most useful structural fact is often a *universal property*. The subspace topology is characterized by: continuous maps into a subspace are exactly continuous maps into the ambient space that land in the subspace. The quotient topology, the product topology, and the weak topology each have analogous universal properties. Recognizing that one is in the situation of a universal property lets one *replace* a hands-on continuity check with a one-line argument from the universal property. When stuck, ask: "What is the universal property of this construction, and does my map satisfy its hypothesis?"

---

# Most Reusable Properties

- **[[Thm - Continuity via Open Sets (Metric Spaces)|Continuity ⇔ preimages of opens are open]]**: This is the foundational reformulation that connects $\varepsilon$–$\delta$ analysis to topology and gives the *definition* of continuity in the general setting. The typical use is to verify continuity of an abstractly defined map by checking its preimages on a basis. Recognize it any time the problem says "show $f$ is continuous" — first move is always to identify the basis or subbasis on the target side and check that.

- **[[Thm - The Pasting Lemma|Pasting Lemma]]**: The pasting lemma is the workhorse for constructing piecewise continuous maps and proves a startling number of "obvious" facts that would otherwise be tedious. The setup is: a finite *closed* (or *open*) cover $X = A_1 \cup \dots \cup A_n$, continuous maps on each piece, and agreement on overlaps. Recognize it whenever a function is defined by cases on a partition of $X$ — the proof is almost always "apply pasting".

- **[[Thm - Characterizations of the Closure|Closure characterizations]]**: $x \in \overline{A}$ if and only if every open set (equivalently neighbourhood, equivalently basis element) containing $x$ meets $A$; in first-countable spaces, equivalently, a sequence in $A$ converges to $x$. The typical use is converting between an abstract closure-membership condition and a concrete sequence-construction problem. Reach for this any time the goal is to put a point in or out of a closure.

- **Subspace universal property**: A continuous map into $Y \subseteq X$ is the same data as a continuous map into $X$ with image in $Y$. The typical use is to reduce a continuity question on a complicated subspace to the same question on the ambient space, where the topology is often more familiar. This is the engine for every "is the corestriction continuous?" argument.

- **Basis/subbasis criterion for continuity**: Continuity is checked by preimages of a basis (or subbasis) being open. This appears in essentially every continuity proof — the only choice is *which* basis to use, and the right choice often makes the proof a one-liner.

---

# Bridges

1. **Measure Theory — σ-algebras and Borel sets.** A topology and a σ-algebra are *parallel structures* on a set $X$, each capturing a different kind of "measurability". A topology is closed under arbitrary unions and *finite* intersections; a σ-algebra is closed under *countable* unions and complementation. The link is the **Borel σ-algebra** $\mathcal{B}(X) = \sigma(\tau)$, generated by the open sets — see **Def - Sigma-Algebra** and [[Measure Theory I — §1 Measure Spaces]]. Borel measurable functions are characterized by: preimages of open sets are Borel, parallel to the topological condition that preimages of open sets are open. The asymmetry is that a continuous function is Borel, but a Borel function need not be continuous. The two structures interact further through the **Riesz representation theorem** and through the theory of Radon measures, where a measure-theoretic object is reconstructed from a topological one.

2. **Functional Analysis — weak and weak-$*$ topologies.** On a normed space $V$, the norm gives a metric topology. But $V$ also carries the **weak topology**: the coarsest topology making every continuous linear functional $\varphi : V \to \mathbb{R}$ continuous, generated by the subbasis $\{\varphi^{-1}(U) : \varphi \in V^*, U \subseteq \mathbb{R}\ \text{open}\}$. The subbasis-generated-topology machinery of §2 is exactly the mechanism that produces this. The dual space $V^*$ carries the analogous **weak-$*$** topology with the roles of $V$ and $V^*$ swapped, generated by point-evaluation functionals. The Banach–Alaoglu theorem — the closed unit ball of $V^*$ is weak-$*$ compact — has no statement at all without these subbasis-generated topologies, and it is the centrepiece of the functional analysis course. The weak topologies are also rarely metrizable in infinite dimensions, which is exactly why one needs the abstract topological setup: the metric formalism is insufficient.

3. **Probability — weak convergence and Prokhorov's theorem.** A sequence of probability measures $\mu_n$ on a metric space $X$ converges *weakly* to $\mu$ if $\int f\, d\mu_n \to \int f\, d\mu$ for every bounded continuous $f : X \to \mathbb{R}$ — see [[Def - Weak Convergence]] and [[Thm - Prokhorov's Theorem]]. This is the weak-$*$ topology on the space of probability measures, viewed as functionals on $C_b(X)$. The Portmanteau theorem characterizes weak convergence in five equivalent forms — open-set, closed-set, expectation, distribution-function, and integral forms — each of which is a topological statement about $\mu$ assigning the right mass to the right sets. Tightness, the source criterion for compactness in the space of probabilities, is essentially the statement "no mass escapes" stated in topological language. The whole apparatus of weak convergence in probability is one consistent picture only because the topological notions of §1–3 are available.

4. **Group Theory — topological groups.** A **topological group** is a group $G$ that is simultaneously a topological space, such that multiplication $G \times G \to G$ and inversion $G \to G$ are continuous. Group-theoretic constructions then have to respect topology: a subgroup gets the subspace topology, a quotient by a normal subgroup gets the quotient topology, and morphisms must be continuous homomorphisms. Many of the most important examples — $\mathbb{R}, S^1, \operatorname{GL}_n(\mathbb{R}), \operatorname{SO}(n)$, Lie groups generally — are topological groups, and the algebraic story you learned in [[Group Theory I — §1.1–1.2]] becomes richer when the topology is included. The connected component of the identity is a normal subgroup; the closure of a subgroup is a subgroup; a discrete subgroup of a Lie group acts as a "lattice". These are downstream facts that depend on the §1–3 vocabulary — open, closed, continuous, subspace — being in place.

5. **Multivariable Analysis — submanifolds and the inverse function theorem.** A submanifold $M \subseteq \mathbb{R}^n$ — see [[Def - Submanifold of Euclidean Space]] — is, before being any kind of smooth object, a topological subspace of $\mathbb{R}^n$. The local-graph property guaranteed by the [[Thm - The Implicit Function Theorem|implicit function theorem]] is a topological property: an open subset of $M$ is homeomorphic to an open subset of $\mathbb{R}^d$. The local triviality, the well-definedness of dimension, the continuity of restrictions of ambient continuous functions — all are topological. The §1–3 vocabulary is the bedrock on which the smooth structure of [[Multivariate Analysis II — Inverse and Implicit Function Theorems]] is erected.

---

# Insights

The **unifying frame** of §1–3 is that continuity is the data the open sets must carry. The axioms for a topology — closure under arbitrary unions and finite intersections — are not arbitrary; they are exactly what one needs in order for $f^{-1}$ to preserve opens whenever finite intersections and arbitrary unions are taken. The story of forgetting more and more structure — from $\mathbb{R}^n$ to metric space to topological space — is the story of identifying which axioms continuity actually uses and discarding the rest. Once the question is framed this way, every further generalization (the Grothendieck topology in algebraic geometry, the coverage of a site, the uniform space) is just the same exercise carried one step further: identify the *minimal data needed for the property of interest*, axiomatize it, and forget everything else.

The **true name** of "topology" is "the data of which sets are open". The true name of "continuous" is "preimage-of-open-is-open". The true name of "homeomorphism" is "an isomorphism of topological spaces" — a structure-preserving bijection whose inverse also preserves the structure. These names are the ones that survive every generalization and every reformulation, and they are the names to remember when returning after months of absence. The metric-space $\varepsilon$–$\delta$ definitions are intuitive but parochial; the open-set definitions are correct in all settings.

A **density-as-strategy** observation worth holding throughout: the rationals, the polynomials, the simple functions, the smooth compactly supported functions are dense in their respective ambient spaces, and the entire workhorse engine of "prove it for nice things and pass to the limit" depends on density. The dense-subset strategy threads through analysis, probability, and PDE; §1–3 is where its topological prerequisite — the notion of *closure* — is set up. The link between density and approximation is the closure characterization: every point of $\overline{A}$ is approximable by points of $A$. Recognize this whenever a problem says "show $X$ has the same property as the dense subset" — closure plus continuity does the work.

A **trigger-reaction pattern** to internalize: when verifying continuity of a map into a space with a non-obvious topology (subspace, product, quotient, weak), the first move is to invoke the *universal property* of that topology, not to chase open sets. Subspace: a map into $Y \subseteq X$ is continuous if and only if its composition with the inclusion is continuous. Product: a map into $\prod Y_\alpha$ is continuous if and only if every component is. Quotient: a map out of $X/\sim$ is continuous if and only if its lift to $X$ is. These three universal properties solve perhaps half of the continuity problems one will ever face, and they each turn a hard topological check into a one-line algebraic check.

A final observation, important for the rest of the topology course: every refinement of the topology axioms — first countable, second countable, Hausdorff, regular, normal, locally compact — is the *price* paid for one specific theorem to become true. First countability buys the "closure = sequential closure" theorem; second countability buys metrizability when combined with regularity (Urysohn); Hausdorff buys uniqueness of limits; normal buys the existence of Urysohn's bump functions. When a theorem fails for general topological spaces, the question is always "what is the cheapest separation or countability axiom that makes it work?", and the answer organizes the rest of the subject.
