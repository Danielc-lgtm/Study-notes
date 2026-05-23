---
type: definition
subject: differential-geometry
prereqs:
  - "Def - Smooth Manifold"
  - "Def - Coordinate Chart and Atlas"
  - "Def - Smooth Function on a Manifold"
tags: [geometry, differential-geometry]
---

# Notation

$M, N$ are smooth manifolds of dimensions $m, n$ respectively. A **smooth chart** on $M$ is denoted $(U, \varphi)$ with $\varphi : U \to \widetilde U \subseteq \mathbb{R}^m$; a smooth chart on $N$ is denoted $(V, \psi)$ with $\psi : V \to \widetilde V \subseteq \mathbb{R}^n$. For $F : M \to N$, the **coordinate representation in the chart pair $((U, \varphi), (V, \psi))$** is
$$\widehat F = \psi \circ F \circ \varphi^{-1} : \varphi(U \cap F^{-1}(V)) \to \psi(V),$$
provided this composition makes sense (and the definition will demand $F(U) \subseteq V$, simplifying the domain to $\varphi(U)$). The full registry is on [[Differential Geometry II — Smooth Maps and Partitions of Unity]].

---

# Axiom Motivation

The definition of a smooth function $M \to \mathbb{R}$ in [[Def - Smooth Function on a Manifold]] generalizes immediately to maps between manifolds: where we had one chart on the source and the trivial chart on $\mathbb{R}$, we now have one chart on the source and one chart on the target. The coordinate representation becomes $\widehat F = \psi \circ F \circ \varphi^{-1}$, a map between Euclidean open sets, and we declare $F$ smooth if every $\widehat F$ is smooth.

But there is a subtlety, and addressing it correctly is what distinguishes the right definition from a wrong one. Lee illustrates this with Problem 2-1: define $f : \mathbb{R} \to \mathbb{R}$ by $f(x) = 1$ for $x \geq 0$ and $f(x) = 0$ for $x < 0$. This is a discontinuous step function. Yet at every point $x_0 \in \mathbb{R}$, there is a chart $(U, \varphi)$ containing $x_0$ (a small interval where $f$ is constant) and a chart $(V, \psi)$ containing $f(x_0)$ (a small interval around $0$ or $1$) such that the coordinate representation $\widehat f = \psi \circ f \circ \varphi^{-1}$ is constant — hence smooth. A naive definition "for every $p$, there exist charts such that the coordinate representation is smooth" would declare $f$ smooth, which is absurd.

The fix is to require not just that the coordinate representation be smooth, but that $F(U) \subseteq V$: the source chart must map into the target chart. For the step function above, every chart $U$ containing $0$ contains both positive and negative reals, so $f(U)$ contains both $0$ and $1$; the image cannot be contained in any small chart $V$ around either point. The containment condition rules out exactly the discontinuous candidates.

*Why does the containment condition rule out discontinuity?* Because if $F(U) \subseteq V$ for some open $V \subseteq N$, and $F$ is smooth in the chart pair, then $F|_U = \psi^{-1} \circ \widehat F \circ \varphi$ is a composition of continuous maps (homeomorphism, smooth Euclidean map, homeomorphism), hence continuous on $U$. The continuity is *forced* by the containment plus the chart-smoothness. So the containment is the price of admission, and what it buys is **smoothness $\Rightarrow$ continuity** — a property we want to be automatic. (See [[Thm - Smooth Maps are Continuous]].)

The chart-independence calculation parallels the one for smooth functions, but now with charts changing on both sides. If $\widehat F = \psi \circ F \circ \varphi^{-1}$ is smooth in the chart pair $((U, \varphi), (V, \psi))$ and $((U', \varphi'), (V', \psi'))$ is another chart pair at the same point $p$, then
$$\psi' \circ F \circ \varphi'^{-1} = (\psi' \circ \psi^{-1}) \circ (\psi \circ F \circ \varphi^{-1}) \circ (\varphi \circ \varphi'^{-1}).$$
Both the outer factors are transition maps of the smooth atlases of $N$ and $M$ respectively, hence smooth diffeomorphisms; the middle factor is smooth by assumption; the composition is smooth. So the answer is chart-independent on both sides, with the smooth-atlas axioms of $M$ and $N$ doing the work.

Why this specific definition and not a nearby variant? *Why not* drop the containment $F(U) \subseteq V$? Then smoothness would not imply continuity, and the definition would be useless. *Why not* demand smoothness of $\widehat F$ in *every* chart pair, not just *some*? This would be equivalent (by chart-independence), but harder to verify in practice. *Why not* require $F$ to be globally smooth in a single global chart? Most manifolds do not admit global charts, so this would empty the definition. The definition is forced by the dual constraints of practical verifiability (one chart pair suffices) and good behaviour (continuity follows automatically).

---

# The Definition

Let $M$ and $N$ be smooth manifolds. A map $F : M \to N$ is **smooth at a point $p \in M$** if there exist smooth charts $(U, \varphi)$ on $M$ with $p \in U$ and $(V, \psi)$ on $N$ with $F(p) \in V$ such that
$$F(U) \subseteq V \quad \text{and} \quad \widehat F = \psi \circ F \circ \varphi^{-1} : \varphi(U) \to \psi(V)$$
is smooth in the Euclidean sense (i.e. $C^\infty$) at $\varphi(p)$.

The map $F$ is **smooth on $M$** if it is smooth at every point of $M$.

The set of smooth maps $M \to N$ is denoted $C^\infty(M, N)$.

**Equivalent characterizations** (Lee Proposition 2.5):

(a) For every $p \in M$, there exist smooth charts $(U, \varphi)$ containing $p$ and $(V, \psi)$ containing $F(p)$ such that $U \cap F^{-1}(V)$ is open in $M$ and $\psi \circ F \circ \varphi^{-1}$ is smooth on $\varphi(U \cap F^{-1}(V))$.

(b) $F$ is continuous and there exist smooth atlases $\{(U_\alpha, \varphi_\alpha)\}$ on $M$ and $\{(V_\beta, \psi_\beta)\}$ on $N$ such that for every $\alpha, \beta$, the map $\psi_\beta \circ F \circ \varphi_\alpha^{-1}$ is smooth on $\varphi_\alpha(U_\alpha \cap F^{-1}(V_\beta))$.

(c) For every smooth chart $(U, \varphi)$ on $M$ and every smooth chart $(V, \psi)$ on $N$, the map $\psi \circ F \circ \varphi^{-1}$ is smooth wherever defined.

The chart-independence calculation in the Axiom Motivation shows these are all equivalent to the primary definition.

A real-valued smooth function on $M$ — the object defined in [[Def - Smooth Function on a Manifold]] — is the special case $N = \mathbb{R}$ with $\psi = \operatorname{id}_\mathbb{R}$.

---

# Categorical Definition

Smooth manifolds together with smooth maps form a **category** $\mathbf{Man}^\infty$: objects are smooth manifolds, morphisms are smooth maps, composition is the usual composition of maps (smooth by [[Ex - Composition of Smooth Maps is Smooth]]), and identities are the identity maps (smooth by direct verification). Isomorphisms in this category are the diffeomorphisms (see [[Def - Diffeomorphism]]).

The category $\mathbf{Man}^\infty$ sits inside the category $\mathbf{Top}$ of topological spaces and continuous maps as a *non-full* subcategory: every smooth map is continuous (so morphisms restrict), but not every continuous map between smooth manifolds is smooth (so the subcategory is not full). The "forgetful functor" $\mathbf{Man}^\infty \to \mathbf{Top}$ remembers the underlying topological space but forgets the smooth structure.

Alternatively, $\mathbf{Man}^\infty$ embeds as a full subcategory of **ringed spaces**: the manifold $M$ becomes $(M, \mathcal{O}_M^\infty)$ where $\mathcal{O}_M^\infty(U) = C^\infty(U)$, and a smooth map $F : M \to N$ corresponds to the morphism of ringed spaces $(F, F^*)$ where $F^* : \mathcal{O}_N^\infty(V) \to \mathcal{O}_M^\infty(F^{-1}(V))$ is pullback $g \mapsto g \circ F$. The non-trivial direction of this correspondence is Lee's Problem 2-10: a continuous map $F : M \to N$ is smooth if and only if $F^*$ takes smooth functions to smooth functions. This gives a *purely algebraic* characterization of smoothness.

---

# Relate to Other Fields / Compression

This is **literally the same construction** as the definition of holomorphic maps between complex manifolds (chart-representation holomorphic), real-analytic maps between analytic manifolds (chart-representation $C^\omega$), and continuous maps between topological spaces (chart-representation continuous). The choice of "smoothness" criterion on the Euclidean side determines the category; the chart-pulling-back template is the same.

It is also a special case of a more general pattern: any **structure sheaf** on a topological space — smooth functions, polynomials, holomorphic functions, regular functions on an algebraic variety — induces a notion of morphism that is "continuous + preserves the structure sheaf under pullback". Smooth maps between manifolds, holomorphic maps between complex manifolds, morphisms of algebraic varieties, and morphisms of schemes are all instances of this template.

**True name:** *the smooth maps are the morphisms in the category of smooth manifolds*. The operational form is "preserves smoothness under pullback": $F^* C^\infty(N) \subseteq C^\infty(M)$. This algebraic formulation is the one that generalizes — to algebraic geometry, complex analysis, scheme theory.

---

# Examples / Corollaries

**Is an instance: constant maps.** Any constant map $F : M \to N$, $F(p) = q_0$ for all $p$, is smooth. The coordinate representation in any chart pair (with $q_0 \in V$) is the constant Euclidean function — smooth.

**Is an instance: the identity.** $\operatorname{id}_M : M \to M$ is smooth. In any chart pair $((U, \varphi), (U, \varphi))$, the coordinate representation is the identity on $\varphi(U)$.

**Is an instance: the inclusion of an open submanifold.** If $U \subseteq M$ is open with the induced smooth structure, then $\iota : U \hookrightarrow M$ is smooth. See [[Ex - The Inclusion of an Open Submanifold is Smooth]].

**Is an instance: the chart maps themselves.** If $(U, \varphi)$ is a smooth chart on $M$, then $\varphi : U \to \varphi(U) \subseteq \mathbb{R}^m$ is smooth (regarding $\varphi(U)$ as a smooth manifold with the inherited Euclidean structure). The coordinate representation in the chart pair $((U, \varphi), (\varphi(U), \operatorname{id}))$ is the identity. Moreover, $\varphi$ is a diffeomorphism onto its image — the inverse $\varphi^{-1}$ is also smooth by the same argument.

**Is an instance: composition.** If $F : M \to N$ and $G : N \to P$ are smooth, then $G \circ F : M \to P$ is smooth. See [[Ex - Composition of Smooth Maps is Smooth]].

**Is an instance: the exponential $e : \mathbb{R} \to S^1$, $e(t) = e^{2\pi i t}$.** This is smooth. In any angular chart on $S^1$, the coordinate representation is $t \mapsto 2\pi t + c$ for some constant $c$ — a linear function, hence smooth.

**Is an instance: the quotient map $\mathbb{R}^{n+1} \setminus \{0\} \to \mathbb{R}P^n$.** This is smooth. In coordinates from $\mathbb{R}^{n+1} \setminus \{0\}$ and the standard charts on $\mathbb{R}P^n$ (homogeneous coordinates with one coordinate equal to $1$), the coordinate representation is a rational function whose denominator does not vanish on the chart's domain.

**Is NOT an instance: the step function $f : \mathbb{R} \to \mathbb{R}$, $f(x) = 1$ for $x \geq 0$, $0$ otherwise** (Lee Problem 2-1). This map is *not* smooth in the sense of our definition, even though at every individual point one can find a chart pair where $\widehat f$ is constant. The reason is that for any chart $U$ containing $0$, $f(U) = \{0, 1\}$ cannot be contained in any small chart $V \subseteq \mathbb{R}$ around either point. The containment requirement $F(U) \subseteq V$ rules this out — and this is exactly what forces continuity.

**Is NOT an instance: a continuous map that fails smoothness at one point.** $F : \mathbb{R} \to \mathbb{R}$, $F(x) = x|x|$ is continuous, even differentiable once, but its second derivative does not exist at $0$. The coordinate representation in the identity chart is $x|x|$, not $C^\infty$ at $0$.

**Corollary (smoothness is local).** $F$ is smooth iff every point has a neighbourhood where $F$ is smooth. Immediate from the definition (each smoothness check is local in $M$).

**Corollary (smoothness $\Rightarrow$ continuity).** Smooth maps are continuous. See [[Thm - Smooth Maps are Continuous]]. The proof is a one-liner using the containment $F(U) \subseteq V$.

**Corollary (composition is smooth).** Smooth $\circ$ smooth = smooth. See [[Ex - Composition of Smooth Maps is Smooth]] for the verification.

**Corollary (gluing on open covers).** If $\{U_\alpha\}$ is an open cover of $M$ and $F_\alpha : U_\alpha \to N$ are smooth maps that agree on overlaps, then they glue to a unique smooth $F : M \to N$ with $F|_{U_\alpha} = F_\alpha$. This is Lee's Corollary 2.8.

**Calibration check.** Verify the following: (i) the inclusion $\iota : \mathbb{R} \to \mathbb{R}^2$, $\iota(x) = (x, 0)$ is smooth — write the coordinate representation in the identity charts on both sides. (ii) The map $F : \mathbb{R} \to S^1$, $F(t) = (\cos t, \sin t)$ is smooth — in stereographic coordinates on $S^1$ from the south pole, $\widehat F(t) = \sin t / (1 + \cos t)$, smooth on the open set where $\cos t \neq -1$. (iii) The "absolute value" map $\mathbb{R} \to \mathbb{R}$ is *not* smooth — verify by writing the coordinate representation in the identity chart.

---

# Unlocked by This

> [!tip] Diffeomorphisms and the Smooth Category *(from Differential Geometry)*
> The natural notion of *equivalence* in the category of smooth manifolds is **diffeomorphism**: a smooth bijection with smooth inverse. See [[Def - Diffeomorphism]]. Two manifolds are diffeomorphic exactly when they are interchangeable as smooth objects, and the central question of smooth manifold theory is the classification of manifolds up to diffeomorphism.

> [!tip] The Differential / Pushforward of a Smooth Map *(from Differential Geometry)*
> A smooth map $F : M \to N$ induces, at each point $p \in M$, a linear map $dF_p : T_p M \to T_{F(p)} N$ between tangent spaces — the **differential** (or *pushforward*) of $F$ at $p$. The local Jacobian of the coordinate representation $\widehat F$ is the matrix of $dF_p$ in chart-induced bases. Developed in [[Differential Geometry III — Tangent Vectors and the Differential|DG III]].

> [!tip] Pullback of Functions, Forms, and Tensors *(from Differential Geometry)*
> A smooth map $F : M \to N$ allows *pullback* of covariant objects from $N$ to $M$: a function $g$ on $N$ pulls back to $g \circ F$ on $M$ (this is the ring homomorphism $F^* : C^\infty(N) \to C^\infty(M)$); a differential form $\omega$ on $N$ pulls back to $F^*\omega$ on $M$ (in [[Differential Geometry VIII — Differential Forms|DG VIII]]); a covariant tensor field on $N$ pulls back similarly (in [[Differential Geometry VII — Tensors and Tensor Fields|DG VII]]). Pullback is contravariant: $(G \circ F)^* = F^* \circ G^*$.
