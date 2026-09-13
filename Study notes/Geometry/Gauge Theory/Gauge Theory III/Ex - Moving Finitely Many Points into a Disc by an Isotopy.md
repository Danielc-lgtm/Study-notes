---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - Homogeneity Lemma for Connected Manifolds"
  - "Thm - Fundamental Theorem on Flows"
  - "Ex - Compactly Supported Vector Fields are Complete"
  - "Thm - Existence of Smooth Bump Functions"
tags: [geometry, gauge-theory]
---

# Problem Statement

Work on the two-torus $T^2=\mathbb{R}^2/\mathbb{Z}^2$, with the quotient projection $\pi\colon\mathbb{R}^2\to T^2$ and coordinates $(x,y)$ read modulo $1$. Fix three distinct points
$$p_1=\pi(0.1,\,0.1),\qquad p_2=\pi(0.5,\,0.9),\qquad p_3=\pi(0.8,\,0.4),$$
and a small open coordinate disc
$$D=\big\{\pi(z):z\in\mathbb{R}^2,\ |z-c_0|<\rho\big\},\qquad c_0=(0.5,\,0.5),\ \rho=0.1 .$$
(The bound $\rho<\tfrac12$ guarantees that $D$ lifts to a genuine disc in $\mathbb{R}^2$, so $\pi$ restricted to that lifted disc is a diffeomorphism onto $D$.)

**Construct an explicit diffeomorphism $h\colon T^2\to T^2$, smoothly isotopic to the identity, with**
$$h(p_1),\,h(p_2),\,h(p_3)\in D,$$
**writing down the vector fields whose time-one flows compose to give $h$.** Prove every claim: that each building block is a diffeomorphism isotopic to the identity, that it moves the intended point to the intended target, that it fixes the points it must fix, and that the composition therefore lands all three points in $D$ and is itself isotopic to the identity.

This is the explicit, dimension-two instance of the consequence of the [[Thm - Homogeneity Lemma for Connected Manifolds|homogeneity lemma]]: any finite set of points of a connected manifold of dimension at least two can be carried into any prescribed coordinate disc by a diffeomorphism isotopic to the identity. In §3.6 this is the mechanism behind the clutching arguments — it lets a generic section's finite zero set be gathered inside a single trivialising disc before the bundle is cut and reglued.

**Recall.** The tools are the flow of a vector field and its properties, the completeness of a compactly supported field, the existence of smooth bump functions, and the homogeneity lemma whose consequence this exercise realises.

![[Thm - Homogeneity Lemma for Connected Manifolds#Statement]]

We use the lemma's **consequence clause** — a finite set can be moved into a prescribed disc — and, rather than quote it as a black box, we reconstruct its proof concretely on $T^2$, so the vector fields are visible.

The flow apparatus we lean on, each proved on its own page and restated where used:

- **Existence, uniqueness, and smoothness of the flow.** For a smooth vector field $X$ on a manifold $M$, through each point passes a unique maximal integral curve, and the flow $\Phi^X\colon\mathcal{D}\to M$ is smooth on its open domain, with $\Phi^X_0=\operatorname{id}$ and $\Phi^X_{s+t}=\Phi^X_s\circ\Phi^X_t$ where defined ([[Thm - Fundamental Theorem on Flows|Fundamental Theorem on Flows]]).
- **Completeness from compact support.** If $X$ has compact support then every integral curve is defined for all time, so $\Phi^X_t$ is a diffeomorphism of $M$ for every $t\in\mathbb{R}$, with inverse $\Phi^X_{-t}$ ([[Ex - Compactly Supported Vector Fields are Complete|compactly supported fields are complete]]).
- **Bump functions.** For any compact $A$ contained in an open $U$ there is a smooth $\psi\colon M\to[0,1]$ with $\psi\equiv1$ on $A$ and $\operatorname{supp}\psi\subset U$ ([[Thm - Existence of Smooth Bump Functions|existence of smooth bump functions]]).

By a **smooth isotopy from the identity** we mean a smooth map $H\colon M\times[0,1]\to M$ with each $H_s:=H(\cdot,s)$ a diffeomorphism, $H_0=\operatorname{id}$, and $H_1=h$; two diffeomorphisms so connected are called **isotopic**.

---

# Convergent Strategy

**Problem class.** This is an *explicit construction* problem: an abstract existence statement (the homogeneity lemma's consequence) must be turned into named objects — three vector fields and their flows — on a concrete manifold. The class of technique is "move a point along a chosen path by flowing a cut-off constant velocity field", the elementary engine inside every homogeneity argument.

**Assumption pattern.** The construction rests on two structural facts about $T^2$ that hold for any connected manifold of dimension $\ge2$. First, between any two nearby points there is a straight coordinate segment along which a constant vector field points. Second, removing finitely many points from a surface leaves it connected, so paths can be routed around the points we must not disturb. The recognisable trigger is "*move specified points without moving certain others*"; the reaction is "*flow a compactly supported field whose support is a thin tube around a path that avoids the forbidden points*". A single translation is tempting but forbidden: translations are rigid and preserve all mutual distances, so three spread-out points can never be squeezed into one small disc by a translation — the problem genuinely requires non-rigid diffeomorphisms.

**Theorem routing.** The route is: (i) pick three distinct targets $q_1,q_2,q_3\in D$ and, for each $i$, a straight segment $S_i$ from $p_i$ to $q_i$ chosen to avoid the other points; (ii) build a bump function $\varphi_i$ equal to $1$ on a thin tube around $S_i$ and supported in a slightly larger tube that still avoids the forbidden points; (iii) form the compactly supported field $X_i=\varphi_i\,v_i$ with $v_i=q_i-p_i$ the constant velocity, so its flow is complete by [[Ex - Compactly Supported Vector Fields are Complete|compact support]] and its time-one map $h_i=\Phi^{X_i}_1$ is a diffeomorphism isotopic to the identity via $s\mapsto\Phi^{X_i}_s$ by the [[Thm - Fundamental Theorem on Flows|flow theorem]]; (iv) compute, using uniqueness of integral curves, that $h_i(p_i)=q_i$ while $h_i$ fixes every point outside its support; (v) compose $h=h_3\circ h_2\circ h_1$ in an order such that each map fixes the points already placed, and connect the three isotopies by $s\mapsto\Phi^{X_3}_s\circ\Phi^{X_2}_s\circ\Phi^{X_1}_s$.

**Key decision point.** The one delicate choice is the *ordering and the tube radii*, which encode the "route around the forbidden points" that the homogeneity lemma hides inside "$M\setminus K$ connected". When we move $p_2$, the point $p_1$ has already been sent to $q_1\in D$, and $p_3$ is still at its original place; the tube for $p_2$ must avoid both $q_1$ and $p_3$. Choosing the targets $q_1,q_2,q_3$ mutually distinct inside $D$ and the tube radius $\delta$ smaller than the least distance from each segment to the finite set of points it must miss makes all three moves independent. Recognising that thin tubes and a good ordering are exactly what turn the connectedness of the punctured surface into a usable construction is the heart of the exercise.

---

# Legal Operations Used

The topic page for §3.5 is assembled after these subpages; the operations are named descriptively until then.

1. **Move a point along a segment by flowing a cut-off constant field.** For a straight segment $S$ from $p$ to $q$ inside a chart, set $v=q-p$ and $X=\varphi\,v$ with $\varphi\equiv1$ on a tube around $S$; the time-one flow sends $p$ to $q$ and fixes the complement of $\operatorname{supp}\varphi$. This is the atomic homogeneity move.

2. **Obtain a diffeomorphism isotopic to the identity as a time-one flow.** A compactly supported field is complete ([[Ex - Compactly Supported Vector Fields are Complete|completeness]]), so its flow $\Phi_t$ consists of diffeomorphisms, and $s\mapsto\Phi_s$ is a smooth isotopy from $\operatorname{id}=\Phi_0$ to $\Phi_1$.

3. **Localise with a bump function to protect forbidden points.** Choose $\varphi$ by [[Thm - Existence of Smooth Bump Functions|the bump-function theorem]] so that its support is a thin tube missing every point that must stay fixed; this realises the "$M\setminus K$ connected" clause of the [[Thm - Homogeneity Lemma for Connected Manifolds|homogeneity lemma]] concretely.

4. **Pin the trajectory by uniqueness of integral curves.** Verify that the explicit line $t\mapsto p+tv$ solves the flow equation of $X$ on $[0,1]$; by uniqueness ([[Thm - Fundamental Theorem on Flows|flow theorem]]) it *is* the flow line through $p$, so $\Phi_1(p)=q$ exactly.

5. **Compose in a protective order and multiply the isotopies.** Sequence the moves so each fixes the already-placed targets; the composite $h_3\circ h_2\circ h_1$ is isotopic to the identity via the pointwise product of the three flows, $s\mapsto\Phi^{X_3}_s\circ\Phi^{X_2}_s\circ\Phi^{X_1}_s$.

---

# Hints

> [!note]- Hint 1
> A translation of the torus moves all three points by the same vector, so it cannot decrease the distance between them. If the three points are far apart, no translation puts them all in a disc of radius $0.1$. You need diffeomorphisms that are the identity outside a small region. What produces such maps? The flow of a vector field that vanishes outside a small set.

> [!note]- Hint 2
> To move one point $p$ to a nearby point $q$ and leave everything far away untouched, take the *constant* field $v=q-p$ and multiply it by a bump function $\varphi$ that equals $1$ near the straight segment from $p$ to $q$ and vanishes outside a slightly larger tube. Why is the time-one flow of $\varphi\,v$ a diffeomorphism at all? Because $\varphi\,v$ has compact support.

> [!note]- Hint 3
> Along the segment $t\mapsto p+tv$ ($t\in[0,1]$) the bump function is identically $1$, so on that segment the field is just the constant $v$. Check that the line $t\mapsto p+tv$ solves the flow equation there, and invoke uniqueness of integral curves to conclude the flow really carries $p$ to $q$ in unit time. Everything outside the support is fixed.

> [!note]- Hint 4
> Do the three points one at a time, $h=h_3\circ h_2\circ h_1$. When you move $p_2$, the point $p_1$ already sits at $q_1\in D$ and $p_3$ is still home; make the tube for $p_2$ thin enough to miss both $q_1$ and $p_3$. Then $h_2$ fixes $q_1$ and $p_3$, so nothing you already arranged is spoiled. Finally, the family $s\mapsto\Phi^{X_3}_s\circ\Phi^{X_2}_s\circ\Phi^{X_1}_s$ is a smooth path of diffeomorphisms from the identity to $h$.

---

# Solution

The plan is to move the three points one at a time along straight coordinate segments into three distinct targets inside $D$, using for each move the time-one flow of a constant velocity field cut off to a thin tube around its segment. Each such flow is a diffeomorphism isotopic to the identity (its field has compact support) that carries the intended point exactly to its target and fixes everything outside a thin tube. By choosing the tubes thin enough to avoid the points that must remain fixed at each stage, the three moves do not interfere, so their composition sends all three points into $D$; the composition is isotopic to the identity because it is the value at time one of the pointwise product of the three flows.

**Step 0: Fix the targets and the segments, and record that they avoid the forbidden points.**

Choose three distinct targets in $D$ and the straight segments to them; verify each segment stays a positive distance from the finitely many points it must not disturb, so a common thin tube radius $\delta$ exists.

> [!note]- Derivation
> Take representatives in $\mathbb{R}^2$ and set the three targets
> $$q_1=(0.45,\,0.5),\qquad q_2=(0.5,\,0.55),\qquad q_3=(0.55,\,0.5).$$
> Each satisfies $|q_i-c_0|=0.05<0.1=\rho$, so $\pi(q_i)\in D$; and they are pairwise distinct, with mutual distances at least $\sqrt{0.05^2+0.05^2}=0.05\sqrt2>0$. We keep the same names $p_i$ for the chosen lifts $(0.1,0.1),(0.5,0.9),(0.8,0.4)$. The straight segments and their constant velocities are
> $$S_i=\{p_i+t\,v_i:t\in[0,1]\},\qquad v_i=q_i-p_i,$$
> $$v_1=(0.35,\,0.4),\qquad v_2=(0,\,-0.35),\qquad v_3=(-0.25,\,0.1).$$
> Because each $|v_i|<\tfrac12$ and each segment lies in a ball of radius $<\tfrac12$, its projection $\pi(S_i)$ embeds in $T^2$ (no wraparound), so working in the lift is legitimate.
>
> We record the separations that the ordering below will need. The move order is $p_1$, then $p_2$, then $p_3$; when $p_i$ is moved, the points that must stay fixed are the already-placed targets and the not-yet-moved originals:
> $$\text{move }p_1:\ \text{fix }\{p_2,p_3\};\qquad \text{move }p_2:\ \text{fix }\{q_1,p_3\};\qquad \text{move }p_3:\ \text{fix }\{q_1,q_2\}.$$
> Each relevant segment stays at positive distance from the finite forbidden set assigned to it:
> - $S_1$ has $x$-coordinate in $[0.1,0.45]$, so it is at distance $\ge0.05$ from $p_2$ (at $x=0.5$) and $\ge0.35$ from $p_3$ (at $x=0.8$).
> - $S_2$ is the vertical segment $x=0.5$, $y\in[0.55,0.9]$, at distance $\ge0.05$ from $q_1$ (at $x=0.45$) and $\ge0.3$ from $p_3$ (at $x=0.8$).
> - $S_3$ has $x$-coordinate in $[0.55,0.8]$, at distance $\ge0.1$ from $q_1$ (at $x=0.45$) and $\ge0.05$ from $q_2$ (at $x=0.5$).
>
> Let $\delta:=0.02$. Then $\delta$ is strictly less than half of every separation listed, so the closed tube of radius $\delta$ around each $S_i$ misses the forbidden set for that move; and $2\delta+\max_i|v_i|<\tfrac12$, so each tube embeds in $T^2$. These are all the geometric facts the construction uses; nothing below depends on the particular numbers beyond these inequalities.

**Step 1: Build the localised field $X_i$ and its bump function explicitly.**

For each $i$ write down a smooth bump $\varphi_i$ that is $1$ on a thin tube around $S_i$ and supported in the radius-$\delta$ tube, and set $X_i=\varphi_i\,v_i$; then $X_i$ has compact support.

> [!note]- Derivation
> Fix $i$ and let $u_i=v_i/|v_i|$ be the unit direction of $S_i$ and $n_i$ a unit normal (rotate $u_i$ by ninety degrees). For $z\in\mathbb{R}^2$ introduce the affine coordinates adapted to the segment,
> $$s_i(z)=\langle z-p_i,\,u_i\rangle\ \ (\text{position along }S_i),\qquad r_i(z)=\langle z-p_i,\,n_i\rangle\ \ (\text{signed distance across }S_i),$$
> both smooth (indeed linear) functions of $z$. Choose two smooth one-variable bumps, by [[Thm - Existence of Smooth Bump Functions|the bump-function theorem]]:
> $$\alpha\colon\mathbb{R}\to[0,1],\quad \alpha\equiv1\text{ on }[-\tfrac\delta2,\tfrac\delta2],\ \operatorname{supp}\alpha\subset(-\delta,\delta);$$
> $$\psi_i\colon\mathbb{R}\to[0,1],\quad \psi_i\equiv1\text{ on }[0,|v_i|],\ \operatorname{supp}\psi_i\subset(-\delta,|v_i|+\delta).$$
> Define, on $\mathbb{R}^2$,
> $$\widetilde\varphi_i(z)=\psi_i\big(s_i(z)\big)\cdot\alpha\big(r_i(z)\big).$$
> This is smooth (a product of smooth functions of the smooth coordinates $s_i,r_i$), equals $1$ on the rectangle $\{0\le s_i\le|v_i|,\ |r_i|\le\tfrac\delta2\}$ — which contains the segment $S_i$ (there $r_i=0$, $s_i\in[0,|v_i|]$) — and is supported in the open rectangle
> $$R_i=\{-\delta<s_i<|v_i|+\delta,\ |r_i|<\delta\},$$
> a set contained in the radius-$\delta$ tube of $S_i$. By Step 0 this tube embeds in $T^2$ and misses the forbidden points, so $\widetilde\varphi_i$ descends to a smooth $\varphi_i:=\widetilde\varphi_i\circ(\pi|_{R_i})^{-1}$ on $T^2$, extended by $0$ outside $\pi(R_i)$; its support $\pi(\overline{R_i})$ is compact.
>
> The vector field is
> $$\boxed{\,X_i=\varphi_i\cdot\big(v_i^1\,\partial_x+v_i^2\,\partial_y\big)\,}\qquad\text{on }T^2,$$
> the constant coordinate field $v_i$ throttled by $\varphi_i$. Since $\varphi_i$ has compact support, so does $X_i$.
>
> Concretely, for $i=1$: $v_1=(0.35,0.4)$, $|v_1|=\sqrt{0.35^2+0.4^2}=\sqrt{0.2825}\approx0.5315$, $u_1\approx(0.658,0.753)$, $n_1\approx(-0.753,0.658)$, and $X_1=\varphi_1(0.35\,\partial_x+0.4\,\partial_y)$ with $\varphi_1(z)=\psi_1(\langle z-p_1,u_1\rangle)\,\alpha(\langle z-p_1,n_1\rangle)$. For $i=2$: $v_2=(0,-0.35)$, so $u_2=(0,-1)$, $n_2=(1,0)$, $s_2(z)=-(z^2-0.9)$, $r_2(z)=z^1-0.5$, and $X_2=-0.35\,\varphi_2\,\partial_y$ with $\varphi_2(z)=\psi_2(0.9-z^2)\,\alpha(z^1-0.5)$. For $i=3$: $v_3=(-0.25,0.1)$, $|v_3|=\sqrt{0.0725}\approx0.2693$, and $X_3=\varphi_3(-0.25\,\partial_x+0.1\,\partial_y)$.

**Step 2: The time-one flow $h_i=\Phi^{X_i}_1$ is a diffeomorphism isotopic to the identity, and fixes the complement of the tube.**

> [!note]- Derivation
> The field $X_i$ is smooth with compact support. By [[Ex - Compactly Supported Vector Fields are Complete|the completeness of compactly supported vector fields]] — a compactly supported smooth field on any manifold is complete, because outside its support integral curves are constant and inside a compact set the escape-lemma bound prevents finite-time blow-up — the flow $\Phi^{X_i}_t$ is defined for all $t\in\mathbb{R}$. By the [[Thm - Fundamental Theorem on Flows|Fundamental Theorem on Flows]], for each fixed $t$ the map $\Phi^{X_i}_t\colon T^2\to T^2$ is smooth with smooth inverse $\Phi^{X_i}_{-t}$ (from the flow law $\Phi^{X_i}_t\circ\Phi^{X_i}_{-t}=\Phi^{X_i}_0=\operatorname{id}$), hence a diffeomorphism. Set
> $$h_i:=\Phi^{X_i}_1 .$$
> The family $H^i\colon T^2\times[0,1]\to T^2$, $H^i(z,s)=\Phi^{X_i}_s(z)$, is smooth (smoothness of the flow in $(s,z)$ jointly, by the same theorem), each $H^i_s$ is a diffeomorphism, $H^i_0=\Phi^{X_i}_0=\operatorname{id}$, and $H^i_1=h_i$. Thus $h_i$ **is isotopic to the identity**.
>
> **It fixes the complement of the support.** If $z\notin\operatorname{supp}X_i$, then $X_i(z)=0$, so the constant curve $t\mapsto z$ solves the flow equation $\dot c=X_i(c)$ with $c(0)=z$; by uniqueness of integral curves ([[Thm - Fundamental Theorem on Flows|flow theorem]]) it is the flow line, whence $\Phi^{X_i}_t(z)=z$ for all $t$. In particular $h_i(z)=z$ for every $z\notin\operatorname{supp}X_i=\pi(\overline{R_i})$.

**Step 3: $h_i$ carries $p_i$ exactly to $q_i$.**

> [!note]- Derivation
> Consider the explicit affine curve in the lift,
> $$c_i(t)=p_i+t\,v_i,\qquad t\in[0,1],$$
> which traces the segment $S_i$. Along $S_i$ we have $r_i(c_i(t))=0\in[-\tfrac\delta2,\tfrac\delta2]$ and $s_i(c_i(t))=t\,|v_i|\in[0,|v_i|]$, so by the plateau properties of $\alpha$ and $\psi_i$,
> $$\varphi_i\big(c_i(t)\big)=\psi_i\big(t|v_i|\big)\,\alpha(0)=1\cdot1=1\qquad(t\in[0,1]).$$
> Hence on this curve $X_i(c_i(t))=\varphi_i(c_i(t))\,v_i=v_i$, and
> $$\dot c_i(t)=v_i=X_i\big(c_i(t)\big)\qquad\text{(since }\varphi_i\equiv1\text{ along }S_i\text{)},\qquad c_i(0)=p_i .$$
> So $c_i$ is an integral curve of $X_i$ through $p_i$ on $[0,1]$. By uniqueness of integral curves ([[Thm - Fundamental Theorem on Flows|Fundamental Theorem on Flows]]), it coincides with the flow line: $\Phi^{X_i}_t(p_i)=c_i(t)$ for $t\in[0,1]$. Evaluating at $t=1$,
> $$h_i(p_i)=\Phi^{X_i}_1(p_i)=c_i(1)=p_i+v_i=q_i .$$
> The point $p_i$ is delivered exactly to the target $q_i$.

**Step 4: Compose in the protective order; all three points land in $D$.**

> [!note]- Derivation
> Set
> $$h:=h_3\circ h_2\circ h_1 ,$$
> a composition of diffeomorphisms, hence a diffeomorphism. We track each point through the composition, using Step 3 (each $h_i$ moves $p_i$ to $q_i$) and Step 2 (each $h_i$ fixes points outside its tube, and by Step 0 the tube of $h_i$ misses the forbidden set for move $i$).
>
> **The point $p_1$.**
> $$h_1(p_1)=q_1\ \text{(Step 3)};\quad h_2(q_1)=q_1\ \text{(}q_1\notin\operatorname{supp}X_2\text{, Step 0/2)};\quad h_3(q_1)=q_1\ \text{(}q_1\notin\operatorname{supp}X_3\text{)} .$$
> Therefore $h(p_1)=h_3(h_2(h_1(p_1)))=h_3(h_2(q_1))=q_1\in D$.
>
> **The point $p_2$.**
> $$h_1(p_2)=p_2\ \text{(}p_2\notin\operatorname{supp}X_1\text{)};\quad h_2(p_2)=q_2\ \text{(Step 3)};\quad h_3(q_2)=q_2\ \text{(}q_2\notin\operatorname{supp}X_3\text{)} .$$
> Therefore $h(p_2)=h_3(h_2(p_2))=h_3(q_2)=q_2\in D$.
>
> **The point $p_3$.**
> $$h_1(p_3)=p_3\ \text{(}p_3\notin\operatorname{supp}X_1\text{)};\quad h_2(p_3)=p_3\ \text{(}p_3\notin\operatorname{supp}X_2\text{)};\quad h_3(p_3)=q_3\ \text{(Step 3)} .$$
> Therefore $h(p_3)=q_3\in D$.
>
> All three images $q_1,q_2,q_3$ lie in $D$ by Step 0, so $h(p_1),h(p_2),h(p_3)\in D$, as required.

**Step 5: $h$ is isotopic to the identity.**

> [!note]- Derivation
> Define $H\colon T^2\times[0,1]\to T^2$ by the pointwise composition of the three flows,
> $$H(z,s)=\big(\Phi^{X_3}_s\circ\Phi^{X_2}_s\circ\Phi^{X_1}_s\big)(z).$$
> Each $\Phi^{X_i}_s$ is a diffeomorphism depending smoothly on $(s,z)$ ([[Thm - Fundamental Theorem on Flows|flow theorem]], as in Step 2), so $H$ is smooth and each $H_s=\Phi^{X_3}_s\circ\Phi^{X_2}_s\circ\Phi^{X_1}_s$ is a composition of diffeomorphisms, hence a diffeomorphism. At the endpoints,
> $$H_0=\Phi^{X_3}_0\circ\Phi^{X_2}_0\circ\Phi^{X_1}_0=\operatorname{id}\circ\operatorname{id}\circ\operatorname{id}=\operatorname{id}\qquad\text{(each }\Phi^{X_i}_0=\operatorname{id}\text{)},$$
> $$H_1=\Phi^{X_3}_1\circ\Phi^{X_2}_1\circ\Phi^{X_1}_1=h_3\circ h_2\circ h_1=h .$$
> Thus $H$ is a smooth isotopy from $\operatorname{id}$ to $h$: the diffeomorphism $h$ is isotopic to the identity. This completes the construction.

> [!note]- Complete formal solution
> **Claim.** With $p_1=\pi(0.1,0.1)$, $p_2=\pi(0.5,0.9)$, $p_3=\pi(0.8,0.4)$ and $D=\{\pi(z):|z-c_0|<0.1\}$, $c_0=(0.5,0.5)$, on $T^2=\mathbb{R}^2/\mathbb{Z}^2$, there is a diffeomorphism $h\colon T^2\to T^2$, isotopic to the identity, with $h(p_i)\in D$ for $i=1,2,3$; it is $h=\Phi^{X_3}_1\circ\Phi^{X_2}_1\circ\Phi^{X_1}_1$ for the fields $X_i$ below.
>
> *Proof.* Choose targets $q_1=(0.45,0.5)$, $q_2=(0.5,0.55)$, $q_3=(0.55,0.5)$, all at distance $0.05<0.1$ from $c_0$, so $\pi(q_i)\in D$, and pairwise distinct. Put $v_i=q_i-p_i$: $v_1=(0.35,0.4)$, $v_2=(0,-0.35)$, $v_3=(-0.25,0.1)$, and let $S_i=\{p_i+tv_i:t\in[0,1]\}$. Set $\delta=0.02$.
>
> For each $i$ let $s_i(z)=\langle z-p_i,u_i\rangle$, $r_i(z)=\langle z-p_i,n_i\rangle$ with $u_i=v_i/|v_i|$ and $n_i=u_i^\perp$, and choose smooth bumps $\alpha$ (equal to $1$ on $[-\tfrac\delta2,\tfrac\delta2]$, supported in $(-\delta,\delta)$) and $\psi_i$ (equal to $1$ on $[0,|v_i|]$, supported in $(-\delta,|v_i|+\delta)$), which exist by [[Thm - Existence of Smooth Bump Functions|the bump-function theorem]]. Let $\widetilde\varphi_i=\psi_i(s_i)\,\alpha(r_i)$; it is smooth, equals $1$ on a neighbourhood of $S_i$, and is supported in the radius-$\delta$ tube $R_i$ of $S_i$. Since $2\delta+\max_i|v_i|<\tfrac12$, each $R_i$ embeds under $\pi$, so $\widetilde\varphi_i$ descends to a smooth $\varphi_i$ on $T^2$ with compact support $\pi(\overline{R_i})$. Set $X_i=\varphi_i\,v_i$ (the constant field $v_i^1\partial_x+v_i^2\partial_y$ scaled by $\varphi_i$), a smooth compactly supported field.
>
> By [[Ex - Compactly Supported Vector Fields are Complete|completeness of compactly supported fields]] the flow $\Phi^{X_i}_t$ exists for all $t$, and by the [[Thm - Fundamental Theorem on Flows|Fundamental Theorem on Flows]] each $\Phi^{X_i}_t$ is a diffeomorphism with inverse $\Phi^{X_i}_{-t}$, jointly smooth in $(t,z)$. If $z\notin\operatorname{supp}X_i$ then $X_i(z)=0$ and the constant curve is the flow line, so $\Phi^{X_i}_t(z)=z$ for all $t$. Along $S_i$ one has $\varphi_i\equiv1$, so $c_i(t)=p_i+tv_i$ satisfies $\dot c_i=v_i=X_i(c_i)$, $c_i(0)=p_i$; by uniqueness of integral curves $\Phi^{X_i}_t(p_i)=c_i(t)$, whence $h_i:=\Phi^{X_i}_1$ satisfies $h_i(p_i)=q_i$.
>
> By construction (with $\delta=0.02$) the tube of $X_1$ misses $\{p_2,p_3\}$, that of $X_2$ misses $\{q_1,p_3\}$, and that of $X_3$ misses $\{q_1,q_2\}$; each is verified from the coordinate ranges of the segments in Step 0. Hence, writing $h=h_3\circ h_2\circ h_1$: $h(p_1)=h_3 h_2(q_1)=q_1$, $h(p_2)=h_3 h_2(p_2)=h_3(q_2)=q_2$, and $h(p_3)=h_3(p_3)=q_3$, using that each later map fixes points outside its tube. Thus $h(p_i)=q_i\in D$ for all $i$.
>
> Finally $H_s=\Phi^{X_3}_s\circ\Phi^{X_2}_s\circ\Phi^{X_1}_s$ is a smooth family of diffeomorphisms with $H_0=\operatorname{id}$ and $H_1=h$, so $h$ is isotopic to the identity. $\blacksquare$

> [!warning] Illegal but tempting: use a single translation of the torus
> The map $T_w\colon\pi(z)\mapsto\pi(z+w)$ is a diffeomorphism of $T^2$ and is isotopic to the identity (via $s\mapsto T_{sw}$), so it is tempting to try to slide all three points into $D$ with one $w$. This **cannot work in general**: a translation is an isometry, so it preserves the distance between any two points, $d(T_w p_i,T_w p_j)=d(p_i,p_j)$. If two of the points are farther apart than the diameter $2\rho=0.2$ of $D$ — as $p_1$ and $p_2$ are here — then no isometry, translation included, can place both inside $D$. The extra condition that would make a rigid motion legal is that the points already lie within a set of diameter $<2\rho$; when they do not, one must use non-rigid diffeomorphisms, which is exactly why the construction flows *localised* fields that compress distances rather than a global translation that preserves them.

> [!note]- Independent check: nothing outside the three tubes moves, and the tubes are disjoint from each other's targets
> A quick consistency check: the total moved region is $\pi(\overline{R_1})\cup\pi(\overline{R_2})\cup\pi(\overline{R_3})$, three thin tubes of radius $0.02$. Their union has area at most $3\cdot(2\delta)\cdot(\max_i|v_i|+2\delta)\le 3\cdot0.04\cdot0.57<0.07$, so more than ninety-three percent of the torus is fixed by $h$; in particular $h$ is the identity near, say, $\pi(0.2,0.7)$, well away from every segment. This matches the intent of a homogeneity move: it is a compactly supported perturbation, invisible outside a small neighbourhood of the paths, not a global reshuffling of the torus.

---

# Key Takeaways

**The atomic homogeneity move is "flow a cut-off constant field along a segment", and it is the concrete content of every abstract statement that a manifold is "homogeneous".** The reusable principle is that to send one point to a nearby point while fixing everything far away, one takes the constant velocity $v=q-p$, throttles it by a bump function equal to $1$ on the segment and vanishing outside a thin tube, and reads off the time-one flow. The trigger condition is any demand of the form "produce a diffeomorphism isotopic to the identity that does something prescribed near a point and nothing elsewhere"; the reaction is to build a compactly supported field, because compact support is exactly what upgrades a vector field to a complete flow and hence to a diffeomorphism. The transferable diagnostic is the plateau check: verify that the bump is identically $1$ along the actual trajectory, so that on the trajectory the field is genuinely constant and the flow line is the visible straight line $t\mapsto p+tv$ — this is what lets uniqueness of integral curves turn a vague "flow moves points" into the exact identity $\Phi_1(p)=q$.

**Ordering and thin tubes are how the connectedness of a punctured surface becomes a construction.** The homogeneity lemma's hypothesis "$M\setminus K$ connected" and its consequence about finite point sets look like existence statements, but the proof is the algorithm carried out here: move the points one at a time, and at each stage make the support of the moving field avoid the points that are already placed and the points not yet touched. On a surface this is always possible because removing finitely many points leaves it connected and, more sharply, because a segment can be surrounded by an arbitrarily thin tube that misses any prescribed finite set. The trigger is "relocate several marked points without disturbing chosen others"; the pattern is "sequence the moves and shrink the tube radius below the least segment-to-forbidden-point distance". This same protective-ordering idea recurs whenever a construction must edit a manifold locally in several places at once — gluing in handles, spreading out a zero set, or, in §3.6, gathering the finitely many zeros of a generic section inside one trivialising disc before clutching.

**Rigid motions preserve distances, so genuine gathering needs non-rigid diffeomorphisms — recognise which symmetries are too rigid for the job.** The instructive negative lesson is that the most symmetric maps available, the translations of the torus, are useless here precisely because they are isometries: they move the whole configuration rigidly and cannot bring far-apart points together. The general diagnostic is to ask what invariants a candidate class of maps preserves, and to check the target against those invariants before attempting a construction; if the goal violates an invariant (here, decreasing a distance below the disc's diameter), that entire class is disqualified and one must reach for maps with fewer invariants — compactly supported flows, which preserve nothing global and can compress, stretch, and reroute at will inside their support. Carrying this question — "what does this class of maps preserve, and does my target respect it?" — prevents wasted effort on symmetric but too-rigid attempts, and it is the same reflex that later separates diffeomorphism-invariant from merely homotopy-invariant data in the classification of bundles.
