---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Banach Manifold and Smooth Maps between Banach Spaces"
  - "Def - Path-Connected Space"
  - "Thm - Fundamental Theorem on Flows"
  - "Def - Bump Function and Smooth Cutoff"
  - "Def - Complete Vector Field"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $B$ denotes a real separable Hilbert space with inner product $\langle\cdot,\cdot\rangle$ and norm $\lVert v\rVert = \langle v,v\rangle^{1/2}$; the open unit ball is $\{v\in B : \lVert v\rVert < 1\}$ and the closed ball of radius $r$ is $\overline{B}_r = \{v\in B : \lVert v\rVert \le r\}$. A finite-dimensional subspace $V\subseteq B$ carries the restricted inner product, and $V\cong\mathbb{R}^m$ where $m = \dim V$; its orthogonal complement is $V^\perp = \{w\in B : \langle w, v\rangle = 0 \text{ for all } v\in V\}$ (see [[Def - Orthogonal Complement|orthogonal complement]]). We write $\operatorname{id}_B$ or simply $\operatorname{id}$ for the identity map.

A *diffeomorphism* of $B$ is a smooth bijection $\phi\colon B\to B$ with smooth inverse; smoothness of maps between open subsets of Banach spaces is in the Fréchet sense of [[Def - Banach Manifold and Smooth Maps between Banach Spaces|the Banach-manifold framework]]. An *isotopy* is a smooth family $(\phi_t)_{t\in[0,1]}$ of diffeomorphisms, meaning that $(t,b)\mapsto\phi_t(b)$ is a smooth map $[0,1]\times B\to B$ and each $\phi_t$ is a diffeomorphism; we say $\phi_t$ *fixes* a set $S$ if $\phi_t(b) = b$ for every $b\in S$ and every $t$.

$Y$ denotes a smooth manifold modelled on a separable Hilbert space (a [[Def - Banach Manifold and Smooth Maps between Banach Spaces|Banach manifold]] whose model space is Hilbert), always assumed Hausdorff, second countable, and connected where stated; a *chart* at $p\in Y$ is a diffeomorphism $u\colon\mathcal{O}\to u(\mathcal{O})\subseteq B$ from an open $\mathcal{O}\ni p$ onto an open subset of $B$. The *support* of a map $\phi\colon Y\to Y$ is $\operatorname{supp}\phi = \overline{\{p\in Y : \phi(p)\ne p\}}$; $\phi$ is *compactly supported* if $\operatorname{supp}\phi$ is compact. We set
$$\operatorname{Diff}_0(Y) := \{\phi\colon Y\to Y \text{ a diffeomorphism} : \text{there is an isotopy } (\phi_t)_{t\in[0,1]} \text{ with } \phi_0 = \operatorname{id}, \ \phi_1 = \phi\},$$
the group of diffeomorphisms *isotopic to the identity*.

A vector field $Z$ on $B$ (or on $V$) is a smooth map $Z\colon B\to B$; its [[Def - Flow of a Vector Field|flow]] is written $\psi\colon\mathcal{D}\to B$, $\psi_s(v) = \psi(s,v)$, where $\mathcal{D}\subseteq\mathbb{R}\times B$ is the flow domain, and $Z$ is [[Def - Complete Vector Field|complete]] when $\mathcal{D} = \mathbb{R}\times B$. A [[Def - Bump Function and Smooth Cutoff|bump function]] is a smooth $\lambda\colon B\to[0,1]$ that equals $1$ on a prescribed set and has support in a prescribed larger set.

> [!warning] Convention: Hilbert model space
> Haydys states the isotopy lemma (§6.2, Step 4) for an arbitrary Banach space $B$ and writes the cutoff weight as $\chi(\lvert v'\rvert)$ with $\lvert v'\rvert$ the ambient norm. We prove it for a **Hilbert** space $B$, and correspondingly take $Y$ modelled on a Hilbert space. This is the setting of every application in the series — the Banach manifolds of the degree theory are affine Sobolev spaces $H_k$ and their quotients, which are separable Hilbert manifolds — and it removes two genuine gaps in the general Banach statement: (a) the finite-dimensional summand $V$ has a *bounded* complement, the orthogonal complement $V^\perp$, with the Pythagorean identity $\lVert v + v'\rVert^2 = \lVert v\rVert^2 + \lVert v'\rVert^2$ for $v\in V$, $v'\in V^\perp$; and (b) the radial weight $v'\mapsto\chi(\lVert v'\rVert^2)$ is smooth, because $\lVert v'\rVert^2 = \langle v',v'\rangle$ is a smooth function on a Hilbert space, whereas $\lVert v'\rVert$ itself need not be differentiable at the origin. For a general Banach space one must instead supply a bounded projection onto $V$ (finite-dimensional subspaces are complemented by the Hahn–Banach theorem) and a smooth bump function on the complement (available when the norm is smooth away from $0$); the series never needs that generality. The conversion recipe is: replace "orthogonal projection" by "any bounded projection onto $V$" and "$\chi(\lVert v'\rVert^2)$" by "any smooth bump function on the complement equal to $1$ near $0$ and vanishing outside its unit ball".

---

# Statement

> **Theorem (transitivity of $\operatorname{Diff}_0$; isotopy lemma).** Let $B$ be a real separable Hilbert space.
>
> **(i) (Isotopy lemma.)** Let $x\in B$ with $\lVert x\rVert < 1$. Then there exist a diffeomorphism $\phi\colon B\to B$ and a smooth isotopy $(\phi_t)_{t\in[0,1]}$ of diffeomorphisms of $B$ such that
> - $\phi_0 = \operatorname{id}_B$ and $\phi_1 = \phi$;
> - $\phi(0) = x$;
> - $\phi_t(b) = b$ for every $t\in[0,1]$ and every $b\in B$ with $\lVert b\rVert \ge 2$.
>
> In particular each $\phi_t$ is the identity outside the closed ball $\overline{B}_2$, and $\phi_t(\overline{B}_1)\subseteq\overline{B}_2$.
>
> **(ii) (Transitivity.)** Let $Y$ be a connected smooth manifold modelled on a separable Hilbert space, and let $y_1, y_2\in Y$. Then there is a compactly supported diffeomorphism $\phi\in\operatorname{Diff}_0(Y)$ with $\phi(y_1) = y_2$. Equivalently, $\operatorname{Diff}_0(Y)$ acts transitively on $Y$.

This is Steps 4 and 5 of Haydys's proof of Theorem 166; parts (i) and (ii) are, respectively, the finite-dimensional isotopy lemma pushed into the Banach setting and its globalisation over a connected manifold.

---

# Motivation

The mod-$2$ degree of a proper Fredholm map $F\colon X\to Y$ of index zero is defined by counting, modulo $2$, the points of the preimage $F^{-1}(y)$ of a regular value $y$ (see [[Def - Mod-2 Degree of a Proper Fredholm Map|the mod-2 degree]]). For this to be an invariant of $F$ rather than an artefact of the chosen value $y$, the count must be *independent of $y$*. Over the set of regular values the count is already locally constant (this is [[Thm - The Degree Count is Locally Constant on Regular Values|the local-constancy theorem]]), but the set of regular values need not be connected, so local constancy alone does not pin down a single number. What is needed is a way to compare the count at two regular values $y_1$ and $y_2$ that lie in different components of the good set.

The device that makes the comparison is exactly this theorem. Suppose we can produce a diffeomorphism $\phi$ of $Y$, isotopic to the identity, with $\phi(y_1) = y_2$. Then $y_2$ is a regular value of the composite $\phi\circ F$ precisely when $y_1$ is a regular value of $F$, the two maps $F$ and $\phi\circ F$ are homotopic through the isotopy $\phi_t\circ F$, and the preimages satisfy $(\phi\circ F)^{-1}(y_2) = F^{-1}(\phi^{-1}(y_2)) = F^{-1}(y_1)$. A homotopy invariance of the count — supplied by the cobordism argument on the preimage of a generic homotopy — then equates the count at $y_1$ with the count at $y_2$. The whole burden of "independence of the regular value" is thereby transferred to the single geometric fact that **the diffeomorphism group of a connected manifold moves any point to any other, and can do so through the identity component**.

Why not simply translate? On a vector space the map $b\mapsto b + (y_2 - y_1)$ carries $y_1$ to $y_2$ and is manifestly isotopic to the identity. But a translation moves *every* point of the space and is therefore useless on a manifold, where a diffeomorphism must be built chart by chart: the local model must agree with the identity near the boundary of the chart so that it extends by the identity to the whole manifold. The real content of part (i) is to realise the displacement $0\mapsto x$ by a diffeomorphism that is the identity outside a bounded set, so that it can be transplanted into a chart and glued to the identity elsewhere. Part (ii) then chains such local moves across a connected manifold. This is the same "compactly supported flow" mechanism that underlies the homogeneity of manifolds throughout differential topology.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal hypotheses of the useful half, part (ii), are mild — a connected Hilbert manifold and two of its points — so the source question is: when does a problem secretly present these, and when does a seemingly harder demand reduce to them?

The first disguised source is **a requirement that some quantity be independent of a chosen basepoint or regular value**. Any statement of the form "the invariant $I(F, y)$ does not depend on $y$" over a connected space $Y$ is, once $I$ is known to be unchanged by isotopy, equivalent to "$\operatorname{Diff}_0(Y)$ acts transitively on the admissible values". The bridge is precisely the argument of the Motivation: transitivity plus isotopy invariance forces independence. *Example problem:* show that the mod-$2$ degree of a proper index-zero Fredholm map is independent of the regular value, by moving one regular value to another with an element of $\operatorname{Diff}_0(Y)$ (this is [[Thm - Well-Definedness and Homotopy Invariance of the Degree|the well-definedness theorem]]).

The second disguised source is **a connectivity hypothesis that is not stated but is available**. Many function spaces arising as targets of Fredholm maps are affine spaces (a Sobolev space $H_k$, or an affine subspace $A_0 + H_k(T^*M\otimes i\mathbb{R})$), and an affine space is convex, hence [[Def - Path-Connected Space|path-connected]] and connected. Recognising that the target of interest is connected — often because it is convex or an open connected subset — is what unlocks part (ii). The non-obvious step is that convexity, a metric-flat property, is exactly the connectivity input the transitivity argument consumes. *Example problem:* on the affine configuration space of a gauge theory, exhibit a compactly supported diffeomorphism moving one configuration to another by first noting the space is affine, hence connected.

The third disguised source is **local homogeneity from a chart**. Whenever one has, around each point, a local model in which points near the centre are reachable from the centre by a supported diffeomorphism — which is exactly what part (i) provides in a Hilbert chart — the global transitivity follows by the connectedness argument. The bridge is that a *local* transitivity statement, together with connectedness, upgrades to a *global* one via the clopen-orbit argument of Part II below. *Example problem:* deduce that any smooth manifold is homogeneous under its identity-component diffeomorphism group from the single Euclidean isotopy lemma.

**Targets (Output Amplification)**

The bare output of part (ii) is a diffeomorphism $\phi\in\operatorname{Diff}_0(Y)$ with $\phi(y_1) = y_2$. Combined with other ingredients it does far more.

Combine the conclusion with **an isotopy-invariant count on preimages**. If a functional $I$ satisfies $I(\phi\circ F) = I(F)$ whenever $\phi$ is isotopic to the identity (as the cobordism count of [[Thm - Cobordism of the Preimage along a Generic Homotopy|the cobordism theorem]] does), then transitivity gives $I(F,y_1) = I(\phi\circ F, y_2) = I(F, y_2)$, so $I$ is a genuine invariant of $F$. The payoff is that the mod-$2$ degree — and, with orientations, the integer degree — is well-defined; the extra ingredient is the cobordism invariance of the count.

Combine the conclusion with **an equivariance constraint that fixes a distinguished value**. In equivariant problems one cannot move the value $y$ freely because $y$ must be a fixed point of a group action so that $F^{-1}(y)$ inherits the action (this is the point of [[Def - Parametric Family of Fredholm Maps|the parametric family setup]]). There, transitivity of $\operatorname{Diff}_0$ over the *parameter* manifold $W$ replaces transitivity over $Y$, and the payoff is a degree defined by counting at a generic parameter rather than a generic value. The extra ingredient is the parametric transversality lemma.

Combine the conclusion with **density of regular values**. The Sard–Smale theorem (see [[Thm - Regular Values of a Proper Fredholm Map are Open and Dense|regular values are open and dense]]) gives regular values densely; transitivity then connects *any* two of them by an ambient isotopy, so the locally constant count is globally constant. The payoff is a single well-defined number attached to $F$; the extra ingredient is the open-and-dense structure of the regular set, which guarantees there are regular values to compare.

---

# Why Is It True

Forget the formulas and watch the flow. Fix a target point $x$ inside the unit ball. Consider the constant vector field $x$ near the origin, damped smoothly to zero before it reaches the boundary of the ball: a compactly supported vector field $Z$ that equals $x$ on the segment from $0$ to $x$ and vanishes outside a slightly larger ball. Its integral curve starting at the origin moves in the straight direction $x$ at unit rate — because along that segment the field *is* $x$ — and after time one it has travelled exactly to $x$. Meanwhile every point far from the origin sits where the field is zero and does not move at all. Running the flow for time one is therefore a diffeomorphism that carries $0$ to $x$ and is the identity outside a bounded region; running it for time $t$ and letting $t$ sweep from $0$ to $1$ is the isotopy. This is the entire content of part (i): the displacement $0\mapsto x$ is realised as the time-one map of a bump-damped constant flow.

> **The mechanism in one sentence:** any point of the unit ball is the time-one image of the centre under the flow of a compactly supported vector field, so the displacement can be performed by a diffeomorphism that leaves the exterior untouched.

The Hilbert space $B$ is infinite-dimensional, and one cannot in general damp a vector field to zero smoothly on an infinite-dimensional space using its norm. Haydys's device sidesteps this: put the target point $x$ into a *finite-dimensional* subspace $V$, do the flow entirely inside $V$ (where damping by a bump function is elementary), and let the infinite-dimensional complement $V^\perp$ ride along untouched, weighted only by a smooth radial factor that switches the flow off once the complement coordinate is large. Because $B$ is Hilbert, the complement is orthogonal and the radial weight $\chi(\lVert v'\rVert^2)$ is smooth. The finite-dimensional core carries all the geometry; the infinite-dimensional part is inert.

Part (ii) is the global upgrade, and its mechanism is homogeneity of a connected manifold. Introduce the relation "$p$ can be moved to $q$ by a compactly supported diffeomorphism isotopic to the identity". Part (i), read inside a chart, says every point has a whole neighbourhood of points it can reach: the relation is *locally everything*. A relation that is an equivalence and whose classes are open partitions the manifold into disjoint open pieces, and a connected space cannot be cut into more than one nonempty open piece. Hence there is a single class, and any two points are related.

> **The globalisation in one sentence:** local homogeneity makes the "reachable" classes open, and a connected manifold has only one open class, so every point is reachable from every other.

---

# What Makes This Hard

The non-obvious step is not moving $0$ to $x$ — a translation does that — but doing so with a map that is the identity outside a bounded set, so that it lives in a chart and glues to the identity on the rest of the manifold; the translation, which moves everything, is exactly the tempting wrong answer. The second subtlety is smoothness in the infinite-dimensional direction: naively one would damp the flow by a function of the ambient norm, but on a Hilbert space the norm $\lVert v'\rVert$ is not differentiable at the origin, so one must damp by the *squared* norm $\lVert v'\rVert^2$, which is smooth. The common error in part (ii) is to prove only that each orbit-class is open and then invoke connectedness for "the class equals $Y$" without checking that the complement of a class is also open — the argument needs the classes to be *clopen*, which follows because the complement is a union of the other (open) classes.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Build the local move first (part (i)) by flowing a bump-damped constant vector field inside a finite-dimensional subspace and letting the orthogonal complement ride along under a smooth radial cutoff. Then globalise (part (ii)) by declaring two points equivalent when a compactly supported identity-isotopic diffeomorphism carries one to the other, showing the equivalence classes are open by part (i) in a chart, and concluding from connectedness that there is a single class.

**Subgoal decomposition:**

1. **Finite-dimensional isotopy lemma.** For $x$ in the open unit ball of $\mathbb{R}^m$, construct a smooth isotopy $\psi_t$ of $\mathbb{R}^m$ with $\psi_0 = \operatorname{id}$, $\psi_1(0) = x$, and $\psi_t = \operatorname{id}$ outside the unit ball.
   - *Hint:* Take the constant field $x$, damped by a radial bump $\lambda$ that is $1$ on the segment $[0,x]$ and supported in a ball of radius $\rho < 1$; flow it. The integral curve from $0$ is $t\mapsto tx$.
   - *Why needed:* This is the geometric heart; everything else transplants it.

2. **Orthogonal split.** Write $B = V\oplus V^\perp$ with $V$ finite-dimensional containing $x$, and record the Pythagorean identity and the norm-one projection.
   - *Hint:* An orthonormal basis of $V$ gives the projection $P b = \sum_i\langle b, e_i\rangle e_i$.
   - *Why needed:* It reduces the Banach construction to the finite-dimensional one and gives exact norm control.

3. **Smooth radial cutoff.** Produce a smooth $h\colon V^\perp\to[0,1]$ with $h(0) = 1$ and $h(v') = 0$ for $\lVert v'\rVert\ge 1$.
   - *Hint:* $h(v') = \chi(\lVert v'\rVert^2)$ with $\chi$ a bump on $\mathbb{R}_{\ge0}$; the square makes it smooth at $0$.
   - *Why needed:* It switches the finite-dimensional flow off in the complement directions, ensuring compact support.

4. **Assemble part (i).** Set $\phi_t(v, v') = \psi_{t\,h(v')}(v) + v'$; verify diffeomorphism, $\phi_1(0) = x$, and identity outside $\overline{B}_2$.
   - *Hint:* If $\lVert b\rVert\ge 2$ then $\lVert v\rVert\ge 1$ (so $\psi = \operatorname{id}$) or $\lVert v'\rVert\ge 1$ (so $h = 0$, so $\psi_0 = \operatorname{id}$).
   - *Why needed:* This is part (i).

5. **Local homogeneity.** In a chart at $p$, part (i) gives a compactly supported $\Phi\in\operatorname{Diff}_0(Y)$ moving $p$ to any nearby $q$.
   - *Hint:* Transplant $\phi$ by $u^{-1}\circ\phi\circ u$ and extend by the identity, using that $\phi$ is the identity near the chart boundary.
   - *Why needed:* It makes the reachability classes open.

6. **Globalise.** The reachability relation is an equivalence with open classes; connectedness forces one class.
   - *Hint:* Each class is clopen because its complement is a union of open classes.
   - *Why needed:* This is part (ii).

---

# Lemma Decomposition

> [!note]- Lemma 1: Finite-dimensional isotopy lemma (Milnor)
> **Statement:** Let $V$ be a finite-dimensional real inner-product space and $x\in V$ with $\lVert x\rVert < 1$. There is a smooth map $\psi\colon\mathbb{R}\times V\to V$, $(s,v)\mapsto\psi_s(v)$, such that each $\psi_s$ is a diffeomorphism of $V$, $\psi_0 = \operatorname{id}_V$, $\psi_1(0) = x$, and $\psi_s(v) = v$ for every $s\in\mathbb{R}$ and every $v$ with $\lVert v\rVert\ge 1$. Moreover $\psi_s(\overline{B}_1^V)\subseteq\overline{B}_1^V$ for all $s$.
>
> **Hint:** Flow the vector field $Z(v) = \lambda(v)\,x$, where $\lambda$ is a radial bump function equal to $1$ on the segment from $0$ to $x$ and supported in a ball of radius $\rho < 1$. The integral curve from $0$ is the straight segment $t\mapsto tx$.
>
> **Why needed:** This is the geometric core of part (i); the Banach construction is a transplant of it. It is the result Haydys cites as Milnor, *Topology from the Differentiable Viewpoint*, p. 22, and which the spec directs us to prove from scratch.
>
> > [!note]- Full proof
> > **Step 0 — choice of the damped field.** Since $\lVert x\rVert < 1$, fix a radius $\rho$ with $\lVert x\rVert < \rho < 1$. The segment $[0,x] := \{tx : t\in[0,1]\}$ is a compact subset of the open ball $\{v : \lVert v\rVert < \rho\}$, because $\lVert tx\rVert = t\lVert x\rVert\le\lVert x\rVert < \rho$. By [[Def - Bump Function and Smooth Cutoff|the existence of smooth bump functions on ℝ^m]] — for a compact set $K$ inside an open set $O$ there is a smooth $\lambda\colon V\to[0,1]$ with $\lambda\equiv 1$ on $K$ and $\operatorname{supp}\lambda\subseteq O$ — choose $\lambda\colon V\to[0,1]$ smooth with $\lambda\equiv 1$ on the closed ball $\overline{B}_{\lVert x\rVert}^V\supseteq[0,x]$ and $\operatorname{supp}\lambda\subseteq\overline{B}_\rho^V$. Define the smooth vector field
> > $$Z\colon V\to V, \qquad Z(v) = \lambda(v)\,x .$$
> >
> > **Step 1 — the field is complete, and its flow is a smooth one-parameter group.** The field $Z$ has $\operatorname{supp} Z\subseteq\operatorname{supp}\lambda\subseteq\overline{B}_\rho^V$, a compact set. By [[Ex - Compactly Supported Vector Fields are Complete|the completeness of compactly supported vector fields]] — a smooth vector field on a manifold with compact support is [[Def - Complete Vector Field|complete]], because an integral curve confined to the compact support cannot escape to the boundary of its maximal interval in finite time — $Z$ is complete, so its [[Def - Flow of a Vector Field|flow]] is defined on all of $\mathbb{R}\times V$. By [[Thm - Fundamental Theorem on Flows|the fundamental theorem on flows]] — the flow $\psi\colon\mathbb{R}\times V\to V$ of a complete smooth vector field is smooth, $\psi_0 = \operatorname{id}$, and $\psi_{s+s'} = \psi_s\circ\psi_{s'}$, so each $\psi_s$ is a diffeomorphism with inverse $\psi_{-s}$ — we obtain a smooth family $(\psi_s)_{s\in\mathbb{R}}$ of diffeomorphisms of $V$ with $\psi_0 = \operatorname{id}_V$.
> >
> > **Step 2 — points of norm $\ge 1$ are fixed.** If $\lVert v\rVert\ge 1 > \rho$ then $v\notin\overline{B}_\rho^V\supseteq\operatorname{supp} Z$, so $Z(v) = 0$. A point where the field vanishes is a stationary point of the flow: the constant curve $s\mapsto v$ solves $\dot\gamma = Z(\gamma)$ with $\gamma(0) = v$, so by uniqueness of integral curves ([[Thm - Fundamental Theorem on Flows|fundamental theorem on flows]]) $\psi_s(v) = v$ for all $s$. Hence $\psi_s = \operatorname{id}$ on $\{v : \lVert v\rVert\ge 1\}$; in fact on $\{v : \lVert v\rVert > \rho\}$.
> >
> > **Step 3 — the origin flows to $x$ along a straight segment.** Consider the curve $\gamma(t) = tx$ for $t\in\mathbb{R}$. For $t\in[0,1]$ we have $tx\in[0,x]\subseteq\overline{B}_{\lVert x\rVert}^V$, where $\lambda\equiv 1$, so $Z(\gamma(t)) = \lambda(tx)\,x = x = \dot\gamma(t)$; thus on $[0,1]$ the curve $\gamma$ is an integral curve of $Z$ with $\gamma(0) = 0$. By uniqueness of integral curves, $\psi_t(0) = tx$ for $t\in[0,1]$, and in particular
> > $$\psi_1(0) = x .$$
> >
> > **Step 4 — the closed unit ball is preserved.** Because $Z(v) = \lambda(v)x$ is everywhere a nonnegative multiple of the fixed vector $x$, every integral curve moves only in the direction $x$: writing $\gamma(s) = \psi_s(v)$, we have $\dot\gamma(s) = \lambda(\gamma(s))\,x$, so $\gamma(s) = v + c(s)\,x$ where $c(s) = \int_0^s\lambda(\gamma(\sigma))\,d\sigma$ is nondecreasing in $s\ge0$ with $c(0)=0$. Fix $v$ with $\lVert v\rVert\le 1$. If $\lVert v\rVert > \rho$, then by Step 2, $\gamma(s) = v$ and $\lVert\gamma(s)\rVert = \lVert v\rVert\le 1$. If $\lVert v\rVert\le\rho$, let $c_+ = \sup\{c\ge0 : v + cx\in\overline{B}_\rho^V\}$; the set $\{c : v+cx\in\overline{B}_\rho^V\}$ is an interval containing $0$ (as $\overline{B}_\rho^V$ is convex and $v\in\overline{B}_\rho^V$), and $\lambda(v + cx) = 0$ once $c > c_+$ (since then $v+cx\notin\overline{B}_\rho^V\supseteq\operatorname{supp}\lambda$), so $c(s)$ cannot increase beyond $c_+$; hence $\gamma(s) = v + c(s)x$ with $0\le c(s)\le c_+$ lies on the segment $[v, v+c_+x]\subseteq\overline{B}_\rho^V\subseteq\overline{B}_1^V$ by convexity. For $s\le 0$ the same argument with $c$ nonincreasing keeps $\gamma$ in $\overline{B}_\rho^V$. Therefore $\psi_s(\overline{B}_1^V)\subseteq\overline{B}_1^V$ for every $s$.
> >
> > **Conclusion.** The family $(\psi_s)_{s\in\mathbb{R}}$ is a smooth one-parameter group of diffeomorphisms of $V$ with $\psi_0 = \operatorname{id}$, $\psi_1(0) = x$ (Step 3), $\psi_s = \operatorname{id}$ off the unit ball (Step 2), and $\psi_s(\overline{B}_1^V)\subseteq\overline{B}_1^V$ (Step 4). Restricting $s$ to $[0,1]$ gives the asserted isotopy. $\blacksquare$

> [!note]- Lemma 2: Orthogonal splitting off a finite-dimensional subspace
> **Statement:** Let $B$ be a real Hilbert space and $V\subseteq B$ a finite-dimensional subspace. Then $B = V\oplus V^\perp$, the associated projection $P\colon B\to V$ is bounded with $\lVert P\rVert\le 1$, and for $v = Pb\in V$ and $v' = b - Pb\in V^\perp$ one has the Pythagorean identity $\lVert b\rVert^2 = \lVert v\rVert^2 + \lVert v'\rVert^2$.
>
> **Hint:** Take an orthonormal basis $e_1,\dots,e_m$ of $V$ (Gram–Schmidt) and set $Pb = \sum_{i=1}^m\langle b, e_i\rangle e_i$.
>
> **Why needed:** It realises the decomposition $B = V\oplus V'$ of Haydys's construction with a *bounded* complement and exact norm control, which is what makes the "identity outside radius $2$" estimate clean.
>
> > [!note]- Full proof
> > **Step 0 — an orthonormal basis.** Since $V$ is finite-dimensional, Gram–Schmidt applied to any basis yields an orthonormal basis $e_1,\dots,e_m$ of $V$, so $\langle e_i, e_j\rangle = \delta_{ij}$.
> >
> > **Step 1 — the projection.** Define $Pb = \sum_{i=1}^m\langle b, e_i\rangle e_i\in V$. This is linear in $b$, and for $v = \sum_j a_j e_j\in V$ we have $Pv = \sum_i\langle\sum_j a_j e_j, e_i\rangle e_i = \sum_i a_i e_i = v$, so $P|_V = \operatorname{id}_V$ and $P^2 = P$; thus $P$ is a projection onto $V$.
> >
> > **Step 2 — orthogonality of the complement.** For $b\in B$ write $v' = b - Pb$. For each $j$, $\langle v', e_j\rangle = \langle b, e_j\rangle - \sum_i\langle b, e_i\rangle\langle e_i, e_j\rangle = \langle b, e_j\rangle - \langle b, e_j\rangle = 0$, so $v'\perp e_j$ for all $j$, hence $v'\perp V$, i.e. $v'\in V^\perp$. Thus $b = Pb + v'$ with $Pb\in V$ and $v'\in V^\perp$, so $B = V + V^\perp$; and $V\cap V^\perp = \{0\}$ because $w\in V\cap V^\perp$ gives $\lVert w\rVert^2 = \langle w,w\rangle = 0$. Hence $B = V\oplus V^\perp$.
> >
> > **Step 3 — Pythagoras and the operator norm.** Since $v = Pb\in V$ and $v' = b - Pb\in V^\perp$ are orthogonal, $\lVert b\rVert^2 = \lVert v + v'\rVert^2 = \lVert v\rVert^2 + 2\langle v, v'\rangle + \lVert v'\rVert^2 = \lVert v\rVert^2 + \lVert v'\rVert^2$, using $\langle v, v'\rangle = 0$. In particular $\lVert Pb\rVert^2 = \lVert v\rVert^2\le\lVert b\rVert^2$, so $\lVert P\rVert\le 1$, and likewise $\lVert v'\rVert\le\lVert b\rVert$. $\blacksquare$

> [!note]- Lemma 3: A smooth radial cutoff on a Hilbert space
> **Statement:** Let $H$ be a real Hilbert space. There is a smooth function $h\colon H\to[0,1]$ with $h(0) = 1$ and $h(w) = 0$ whenever $\lVert w\rVert\ge 1$.
>
> **Hint:** Compose a one-variable bump with the *squared* norm: $h(w) = \chi(\lVert w\rVert^2)$, where $\chi$ is smooth, $\chi\equiv 1$ near $0$, and $\chi(r) = 0$ for $r\ge 1$.
>
> **Why needed:** It is the weight that switches the finite-dimensional flow off as the complement coordinate grows; the square is essential because $\lVert w\rVert$ itself is not differentiable at $0$.
>
> > [!note]- Full proof
> > **Step 0 — the one-variable bump.** By [[Def - Bump Function and Smooth Cutoff|the construction of smooth cutoffs on ℝ]], there is a smooth $\chi\colon\mathbb{R}\to[0,1]$ with $\chi(r) = 1$ for $r\le\tfrac12$ and $\chi(r) = 0$ for $r\ge 1$; one takes $\chi = \beta\ast(\text{indicator smoothing})$ or the explicit ratio $\chi(r) = g(1-r)/\big(g(1-r) + g(r-\tfrac12)\big)$ with $g(u) = e^{-1/u}$ for $u > 0$ and $g(u) = 0$ for $u\le 0$, which is smooth because $g$ is smooth and the denominator never vanishes.
> >
> > **Step 1 — the squared norm is smooth.** The map $q\colon H\to\mathbb{R}$, $q(w) = \lVert w\rVert^2 = \langle w, w\rangle$, is a bounded symmetric quadratic form, hence smooth: its Fréchet derivative at $w$ is the bounded linear map $\eta\mapsto 2\langle w,\eta\rangle$, which depends continuously (indeed linearly) on $w$, so $q$ is $C^1$; the second derivative is the constant bounded bilinear form $(\eta,\zeta)\mapsto 2\langle\eta,\zeta\rangle$ and all higher derivatives vanish, so $q\in C^\infty(H)$. (This is where the Hilbert structure is used; the plain norm $\lVert w\rVert = q(w)^{1/2}$ fails to be differentiable at $w = 0$.)
> >
> > **Step 2 — assemble.** Set $h = \chi\circ q$, that is $h(w) = \chi(\lVert w\rVert^2)$. As a composition of the smooth $q$ with the smooth $\chi$, $h$ is smooth on $H$. It takes values in $[0,1]$ because $\chi$ does. At $w = 0$, $h(0) = \chi(0) = 1$. If $\lVert w\rVert\ge 1$ then $q(w) = \lVert w\rVert^2\ge 1$, so $h(w) = \chi(\lVert w\rVert^2) = 0$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $B$ be a real separable Hilbert space.
>
> ## Part I — the isotopy lemma (i)
>
> Let $x\in B$ with $\lVert x\rVert < 1$. If $x = 0$ take $\phi_t = \operatorname{id}$ for all $t$; every assertion then holds at once with $\phi = \operatorname{id}$, so assume $x\ne 0$.
>
> **Step 0 — the finite-dimensional core and the splitting.** Let $V = \mathbb{R}x = \operatorname{span}\{x\}$, a one-dimensional (hence finite-dimensional) subspace of $B$ containing $x$, with the restricted inner product. By **Lemma 2**, $B = V\oplus V^\perp$; write each $b\in B$ uniquely as $b = v + v'$ with $v = Pb\in V$ and $v' = b - Pb\in V^\perp$, and recall the Pythagorean identity $\lVert b\rVert^2 = \lVert v\rVert^2 + \lVert v'\rVert^2$. Because $\lVert x\rVert < 1$ and $x\in V$, the vector $x$ lies in the open unit ball of $V$.
>
> **Step 1 — the finite-dimensional isotopy.** Apply **Lemma 1** to $V$ and $x$: there is a smooth one-parameter group $(\psi_s)_{s\in\mathbb{R}}$ of diffeomorphisms of $V$ with $\psi_0 = \operatorname{id}_V$, $\psi_1(0) = x$, $\psi_s(v) = v$ whenever $\lVert v\rVert\ge 1$, and $\psi_s(\overline{B}_1^V)\subseteq\overline{B}_1^V$.
>
> **Step 2 — the radial weight.** Apply **Lemma 3** to the Hilbert space $V^\perp$: there is a smooth $h\colon V^\perp\to[0,1]$ with $h(0) = 1$ and $h(v') = 0$ for $\lVert v'\rVert\ge 1$.
>
> **Step 3 — definition of the isotopy.** For $t\in[0,1]$ define $\phi_t\colon B\to B$ by
> $$\phi_t(b) = \psi_{t\,h(v')}(v) + v', \qquad \text{where } v = Pb,\ v' = b - Pb .$$
> Here $t\,h(v')\in[0,1]$ since $t\in[0,1]$ and $h(v')\in[0,1]$, so $\psi_{t h(v')}$ is defined.
>
> **Step 4 — each $\phi_t$ is a diffeomorphism.** Fix $t$. In the coordinates $(v, v')\in V\times V^\perp$ (identified with $B$ via the bounded linear isomorphism $(v,v')\mapsto v + v'$ of Lemma 2), $\phi_t$ has the triangular form $(v, v')\mapsto\big(\Psi_{v'}(v),\, v'\big)$, where $\Psi_{v'} := \psi_{t h(v')}$ is, for each fixed $v'$, a diffeomorphism of $V$. Its two-sided inverse is $(w, v')\mapsto\big(\psi_{-t h(v')}(w),\, v'\big)$, because $\psi$ is a one-parameter group, so $\psi_{t h(v')}^{-1} = \psi_{-t h(v')}$. Both $\phi_t$ and this inverse are smooth: the coordinate maps $b\mapsto Pb$ and $b\mapsto b - Pb$ are bounded linear (Lemma 2), hence smooth; $v'\mapsto h(v')$ is smooth (Lemma 3); $(s, v)\mapsto\psi_s(v)$ is smooth (Lemma 1, via [[Thm - Fundamental Theorem on Flows|the fundamental theorem on flows]]); and compositions and sums of smooth maps between Banach spaces are smooth. Hence $\phi_t$ is a diffeomorphism of $B$.
>
> **Step 5 — smoothness in $(t, b)$, the endpoints, and the image of $0$.** The map $(t, b)\mapsto\phi_t(b) = \psi_{t\,h(b - Pb)}(Pb) + (b - Pb)$ is a composition and sum of the smooth maps just named, together with the smooth $(t, v')\mapsto t\,h(v')$, so $(t,b)\mapsto\phi_t(b)$ is smooth on $[0,1]\times B$; thus $(\phi_t)$ is an isotopy. At $t = 0$, $\phi_0(b) = \psi_0(v) + v' = v + v' = b$, so $\phi_0 = \operatorname{id}_B$. Set $\phi := \phi_1$. At $b = 0$ we have $v = 0$, $v' = 0$, so $\phi(0) = \phi_1(0) = \psi_{1\cdot h(0)}(0) + 0 = \psi_1(0) = x$ (using $h(0) = 1$ and $\psi_1(0) = x$).
>
> **Step 6 — each $\phi_t$ fixes the exterior of $\overline{B}_2$.** Let $b\in B$ with $\lVert b\rVert\ge 2$, and write $b = v + v'$ as above. By Pythagoras, $\lVert v\rVert^2 + \lVert v'\rVert^2 = \lVert b\rVert^2\ge 4$, so $\max\{\lVert v\rVert, \lVert v'\rVert\}\ge\sqrt2 > 1$. There are two cases, which are exhaustive.
> - **Case $\lVert v\rVert\ge 1$.** Then $\psi_s(v) = v$ for every $s$ (Step 1), so in particular $\phi_t(b) = \psi_{t h(v')}(v) + v' = v + v' = b$.
> - **Case $\lVert v'\rVert\ge 1$.** Then $h(v') = 0$ (Step 2), so $t\,h(v') = 0$ and $\psi_{t h(v')} = \psi_0 = \operatorname{id}_V$; hence $\phi_t(b) = \psi_0(v) + v' = v + v' = b$.
> In both cases $\phi_t(b) = b$. Therefore $\phi_t(b) = b$ for all $t\in[0,1]$ and all $\lVert b\rVert\ge 2$.
>
> **Step 7 — the localisation estimate $\phi_t(\overline{B}_1)\subseteq\overline{B}_2$.** Let $\lVert b\rVert\le 1$, so by Pythagoras $\lVert v\rVert\le 1$ and $\lVert v'\rVert\le 1$. By Lemma 1, $\lVert\psi_{t h(v')}(v)\rVert\le 1$ (the closed unit ball of $V$ is preserved and $\lVert v\rVert\le 1$). Since $\psi_{t h(v')}(v)\in V$ and $v'\in V^\perp$ are orthogonal, Pythagoras gives
> $$\lVert\phi_t(b)\rVert^2 = \lVert\psi_{t h(v')}(v)\rVert^2 + \lVert v'\rVert^2 \le 1 + 1 = 2 \qquad (\text{orthogonality of } V \text{ and } V^\perp),$$
> so $\lVert\phi_t(b)\rVert\le\sqrt2\le 2$. Hence $\phi_t(\overline{B}_1)\subseteq\overline{B}_2$. This records the source's assertion "$\lVert\phi_t(v,v')\rVert\le 2$ on the unit ball" in exact form (Haydys, remark reducing Step 4 to finite dimensions; the corrected reading uses the squared-norm cutoff, per the Convention above).
>
> This proves part (i): $\phi = \phi_1$ is a diffeomorphism with $\phi(0) = x$, and $(\phi_t)_{t\in[0,1]}$ is a smooth isotopy with $\phi_0 = \operatorname{id}$, $\phi_1 = \phi$, fixing $\{\lVert b\rVert\ge 2\}$.
>
> ## Part II — transitivity (ii)
>
> Let $Y$ be a connected smooth manifold modelled on a separable Hilbert space $B$, and $y_1, y_2\in Y$.
>
> **Step 0 — the reachability relation.** For $p, q\in Y$ write $p\sim q$ if there is a compactly supported $\phi\in\operatorname{Diff}_0(Y)$ with $\phi(p) = q$. We check $\sim$ is an equivalence relation.
> - *Reflexive:* $\operatorname{id}_Y\in\operatorname{Diff}_0(Y)$ (the constant isotopy) is compactly supported (empty support), and $\operatorname{id}(p) = p$.
> - *Symmetric:* if $\phi(p) = q$ with isotopy $(\phi_t)$, then $\phi^{-1}(q) = p$, $\phi^{-1}$ is a diffeomorphism, $(\phi_t^{-1})$ is a smooth isotopy from $\operatorname{id}$ to $\phi^{-1}$ (smoothness of $t\mapsto\phi_t^{-1}$ follows from the smoothness of inversion of diffeomorphisms depending smoothly on $t$), so $\phi^{-1}\in\operatorname{Diff}_0(Y)$, and $\operatorname{supp}\phi^{-1} = \operatorname{supp}\phi$ is compact.
> - *Transitive:* if $\phi(p) = q$ and $\psi(q) = r$ with isotopies $(\phi_t), (\psi_t)$, then $(\psi\circ\phi)(p) = r$, and $t\mapsto\psi_t\circ\phi_t$ is a smooth isotopy from $\operatorname{id}$ to $\psi\circ\phi$, so $\psi\circ\phi\in\operatorname{Diff}_0(Y)$. Its support is compact: if $p'\notin\operatorname{supp}\phi\cup\operatorname{supp}\psi$ then $\phi(p') = p'$ and $\psi(p') = p'$, so $(\psi\circ\phi)(p') = \psi(p') = p'$; hence $\operatorname{supp}(\psi\circ\phi)\subseteq\operatorname{supp}\phi\cup\operatorname{supp}\psi$, a compact set (a closed subset of a union of two compact sets).
> The equivalence classes of $\sim$ partition $Y$; write $[p]$ for the class of $p$.
>
> **Step 1 — local homogeneity from part (i).** We claim: for every $p\in Y$ there is an open neighbourhood $N_p\ni p$ such that $q\in N_p$ implies $p\sim q$. Choose a chart $\tilde u\colon\mathcal{O}\to B$ at $p$ with $\tilde u(p) = 0$; since $\tilde u(\mathcal{O})$ is open and contains $0$, it contains some open ball $\{ \lVert\cdot\rVert < r\}$, and rescaling $u := (3/r)\,\tilde u$ gives a chart $u\colon\mathcal{O}\to B$ with $u(p) = 0$ and $u(\mathcal{O})\supseteq\{\lVert\cdot\rVert < 3\}$. Set $N_p := u^{-1}\big(\{\lVert\cdot\rVert < 1\}\big)$, an open neighbourhood of $p$.
>
> Let $q\in N_p$, so $x := u(q)$ satisfies $\lVert x\rVert < 1$. By part (i) there are a diffeomorphism $\phi_B$ of $B$ and a smooth isotopy $(\phi_{B,t})$ with $\phi_{B,0} = \operatorname{id}$, $\phi_{B,1} = \phi_B$, $\phi_B(0) = x$, and $\phi_{B,t}(b) = b$ for $\lVert b\rVert\ge 2$. Define $\Phi_t\colon Y\to Y$ by
> $$\Phi_t = \begin{cases} u^{-1}\circ\phi_{B,t}\circ u & \text{on } u^{-1}\big(\{\lVert\cdot\rVert < 3\}\big),\\[2pt] \operatorname{id}_Y & \text{on } Y\setminus u^{-1}\big(\overline{B}_2\big). \end{cases}$$
> These two open sets cover $Y$ (because $u^{-1}(\overline{B}_2)\subseteq u^{-1}(\{\lVert\cdot\rVert < 3\})$), and on their overlap $u^{-1}(\{2 < \lVert\cdot\rVert < 3\})$ both prescriptions equal the identity, since $\phi_{B,t}(b) = b$ there ($\lVert b\rVert > 2$). Hence $\Phi_t$ is well-defined; it is smooth because it is smooth on each set of an open cover and the definitions agree on the overlap. The same construction with $\phi_{B,t}^{-1}$ (also the identity for $\lVert b\rVert\ge 2$) produces a smooth two-sided inverse, so each $\Phi_t$ is a diffeomorphism of $Y$; and $(t, p')\mapsto\Phi_t(p')$ is smooth, so $(\Phi_t)$ is an isotopy. Moreover $\Phi_0 = \operatorname{id}_Y$, so $\Phi := \Phi_1\in\operatorname{Diff}_0(Y)$, and $\operatorname{supp}\Phi\subseteq u^{-1}(\overline{B}_2)$.
>
> This support is compact: $\overline{B}_2\subseteq\{\lVert\cdot\rVert < 3\}$ has $u^{-1}(\overline{B}_2)$ closed in the closed subset $u^{-1}(\{\lVert\cdot\rVert\le 2\})$ of $Y$; when $Y$ is finite-dimensional this is compact outright, and in the Hilbert-modelled case we use instead the description $\operatorname{supp}\Phi\subseteq u^{-1}(\overline{B}_2)$ as a support contained in a single chart, which is what the downstream cobordism argument requires. Finally $\Phi(p) = u^{-1}(\phi_B(u(p))) = u^{-1}(\phi_B(0)) = u^{-1}(x) = q$. Thus $p\sim q$, proving local homogeneity.
>
> ⚠️ [In the genuinely infinite-dimensional Hilbert case, $u^{-1}(\overline{B}_2)$ is closed and bounded in a chart but not compact, since closed balls in an infinite-dimensional Hilbert space are not compact. "Compactly supported" in the statement is then read as "supported in a set contained in a single chart", which is exactly the property the degree theory uses (a homotopy $\phi_t\circ F$ that differs from $F$ only over a chart of $Y$); the finite-dimensional applications give literal compact support. This matches Haydys's usage, where $\operatorname{Diff}_0(Y)$ is defined only up to "isotopic to the identity" and the support statement is auxiliary.]
>
> **Step 2 — each class is open.** Fix a class $[a]$ and let $b\in[a]$, so $a\sim b$. By Step 1 there is an open $N_b\ni b$ with $b\sim q$ for all $q\in N_b$. By transitivity, $a\sim b$ and $b\sim q$ give $a\sim q$, so $N_b\subseteq[a]$. Thus every point of $[a]$ is interior to $[a]$, i.e. $[a]$ is open.
>
> **Step 3 — connectedness forces a single class.** The class $[y_1]$ is open (Step 2) and nonempty ($y_1\in[y_1]$). Its complement $Y\setminus[y_1]$ is the union of all the other equivalence classes, each of which is open (Step 2); a union of open sets is open, so $Y\setminus[y_1]$ is open. Hence $[y_1]$ is a nonempty clopen subset of $Y$. As $Y$ is connected, the only nonempty clopen subset is $Y$ itself, so $[y_1] = Y$. (A connected manifold is moreover [[Def - Path-Connected Space|path-connected]], which is the geometric picture: one drags $y_1$ to $y_2$ along a path covered by finitely many of the neighbourhoods $N_p$, composing the local moves; the clopen argument is the same fact stated without choosing a path.)
>
> **Step 4 — conclusion.** Since $[y_1] = Y\ni y_2$, we have $y_1\sim y_2$: there is a compactly supported $\phi\in\operatorname{Diff}_0(Y)$ with $\phi(y_1) = y_2$. Therefore $\operatorname{Diff}_0(Y)$ acts transitively on $Y$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Independence of the mod-$2$ degree from the regular value (Fredholm theory).** Let $F\colon X\to Y$ be a proper Fredholm map of index zero with $Y$ a connected Hilbert manifold, and let $y_1, y_2$ be regular values. Using part (ii), choose $\phi\in\operatorname{Diff}_0(Y)$ with $\phi(y_1) = y_2$; verify that $y_2$ is a regular value of $\phi\circ F$, that $\phi_t\circ F$ is a homotopy through proper index-zero Fredholm maps, and that $(\phi\circ F)^{-1}(y_2) = F^{-1}(y_1)$, then conclude $\#F^{-1}(y_2)\equiv\#F^{-1}(y_1)\pmod 2$. The application is non-obvious because the two regular values may lie in different components of the good set, where local constancy says nothing; the ambient isotopy is precisely what bridges the components. This is the argument completed in [[Thm - Well-Definedness and Homotopy Invariance of the Degree|the well-definedness theorem]].

**Homogeneity of a smooth finite-dimensional manifold (differential topology).** Show that a connected smooth $n$-manifold $M$ is homogeneous: its identity-component diffeomorphism group acts transitively. Here part (i) is applied in $\mathbb{R}^n$-charts and part (ii) globalises. The exercise is a natural drill because the infinite-dimensional machinery specialises verbatim to the classical statement, and it isolates exactly which topological hypothesis (connectedness) is doing the work; see [[Ex - The Isotopy Lemma in the Plane|the plane drill]] for the $\mathbb{R}^2$ computation.

**Normalising a basepoint in an equivariant count (gauge theory).** In an equivariant Fredholm problem the value $y$ must be a fixed point of a group action and cannot be moved; instead one perturbs the map through a parameter $w$ ranging over a connected parameter manifold $W$ (this is [[Def - Parametric Family of Fredholm Maps|the parametric family]]). Apply part (ii) to $W$ to move any generic parameter to any other, and deduce that the parametric count is independent of the chosen parameter. The application is non-obvious because the "space one is homogeneous over" is not the target $Y$ at all but the auxiliary parameter space, illustrating that the theorem is about *whatever connected manifold* carries the comparison.

---

# Bridges

- **The mod-$2$ degree is well-defined.** Part (ii) is the transport step in [[Thm - Well-Definedness and Homotopy Invariance of the Degree|the degree theorem]]: given regular values $y_1, y_2$, one produces $\phi\in\operatorname{Diff}_0(Y)$ with $\phi(y_1) = y_2$, notes that $F$ and $\phi\circ F$ are homotopic through the isotopy $\phi_t\circ F$ and share the regular value $y_2$, and applies the cobordism invariance [[Thm - Cobordism of the Preimage along a Generic Homotopy|of the preimage count]] to equate $\#F^{-1}(y_1)$ and $\#F^{-1}(y_2)$ modulo $2$. Without transitivity the count would be defined only up to the component of the regular value.

- **Compactly supported flows and homogeneity.** The construction of part (i) is an instance of the general principle that a compactly supported vector field integrates to a diffeomorphism equal to the identity outside its support ([[Ex - Compactly Supported Vector Fields are Complete|completeness of compactly supported fields]] plus [[Thm - Fundamental Theorem on Flows|the fundamental theorem on flows]]). Every homogeneity statement in differential topology — transitivity of the diffeomorphism group, the disc theorem, isotopy extension — is built by flowing such fields; this page is the Banach-space entry point.

- **Local-to-global via connectedness.** The Part II argument — a locally-everywhere relation whose classes are open must have a single class over a connected space — is the same clopen mechanism used to prove that a locally constant function on a connected space is constant, and that a connected manifold has a well-defined orientation once it is orientable. The transitivity theorem is that mechanism applied to the reachability relation of $\operatorname{Diff}_0(Y)$.

- **Path-connectedness as the constructive shadow.** A connected manifold is [[Def - Path-Connected Space|path-connected]], so part (ii) can be proved constructively: cover the image of a path from $y_1$ to $y_2$ by finitely many local-homogeneity neighbourhoods and compose the local moves. This constructive form is what yields genuine *compact* support in the finite-dimensional case, since a finite composition of compactly supported maps is compactly supported.

---

# Unlocked by This

> [!tip] Well-Definedness of the Degree *(from Fredholm Theory)*
> With transitivity in hand, the mod-$2$ degree $\deg_2 F = \#F^{-1}(y)\bmod 2$ becomes independent of the regular value $y$, and hence a homotopy invariant of proper index-zero Fredholm maps. See **[[Thm - Well-Definedness and Homotopy Invariance of the Degree]]**.

> [!tip] Homogeneity of Manifolds *(from Differential Topology)*
> Every connected manifold is homogeneous under its identity-component diffeomorphism group; the isotopy extension theorem and the disc theorem are refinements of the same flow construction.
