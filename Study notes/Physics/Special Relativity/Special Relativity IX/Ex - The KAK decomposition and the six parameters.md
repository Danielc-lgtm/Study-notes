---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - Polar Decomposition of the Lorentz Group"
  - "Def - Boosts as Hyperbolic Rotations"
  - "Def - Subgroups and Components of the Lorentz Group"
tags: [physics, special-relativity]
---

# Problem Statement

Work with $c = 1$, signature $\eta = \mathrm{diag}(1,-1,-1,-1)$, and a fixed orthonormal frame with future-timelike $e_0$ and rest space $E = e_0^\perp$. Let $K = SO(3)$ denote the spatial rotations fixing $e_0$ (block form $\mathrm{diag}(1, H)$, $H \in SO(3)$) and let $A = \{B[V] : V \in (-1,1)\}$ denote the one-parameter group of boosts along the fixed axis $e_1$.

1. **Existence.** Show that every restricted Lorentz transformation $\Lambda \in SO^+(1,3)$ can be written as
$$
\Lambda = R(H)\,B[V]\,R(H'), \qquad H, H' \in SO(3),\ V \in [0,1),
$$
a rotation, a standard boost along $e_1$, and a second rotation — the **Cartan $KAK$ decomposition** $G = KAK$. (Start from the polar decomposition $\Lambda = S\circ R'$ and standardise the boost's axis with a rotation.)
2. Express the boost speed $V$ (equivalently the rapidity, equivalently $\Gamma = \cosh\psi$) directly through $\Lambda$, with no reference to $H, H'$. Conclude that $V$ is an invariant of the double coset $K\Lambda K$.
3. **The parameter count.** The data $(H, V, H')$ is two $SO(3)$ matrices (three parameters each) plus one rapidity, apparently *seven* numbers. But $SO^+(1,3)$ is *six*-dimensional. Locate the one-parameter redundancy: find a one-parameter family of pairs $(H, H')$ that leave $R(H)B[V]R(H')$ unchanged, for generic $V \ne 0$.
4. Verify the dimension bookkeeping $\dim K + \dim A + \dim K - (\text{redundancy}) = 3 + 1 + 3 - 1 = 6 = \dim SO^+(1,3)$, and explain why the redundancy is exactly one-dimensional (the stabiliser of the boost axis inside $K$).

**Recall:**

The exercise refines the polar decomposition into a two-sided rotation–boost–rotation factorisation.

![[Thm - Polar Decomposition of the Lorentz Group#Statement]]

A [[Def - Boosts as Hyperbolic Rotations|boost]] $B[V]$ along $e_1$ has matrix with $\Lambda^0{}_0 = \Lambda^1{}_1 = \cosh\psi = \Gamma$, $\Lambda^0{}_1 = \Lambda^1{}_0 = \sinh\psi = \Gamma V$, fixing $e_2, e_3$. Conjugating a boost along $e_1$ by a rotation $R(H)$ rotates its axis: $R(H)\,B[V]_{e_1}\,R(H)^{-1}$ is the boost of the same speed $V$ along $H e_1$. The restricted group $SO^+(1,3)$ is six-dimensional ([[Def - Subgroups and Components of the Lorentz Group]]).

---

# Convergent Strategy

**Problem class.** A *factor-a-transformation* problem from the [[Special Relativity IX — The Lorentz Group, Structure and Classification#Problem-Solving Strategy|topic strategy]], here producing the two-sided $KAK$ (Cartan) form by peeling a rotation off each side of the polar boost to standardise it along a coordinate axis.

**Assumption pattern.** The signpost is "standardise the boost along a fixed axis." The polar decomposition already gives boost-times-rotation; the boost has an *arbitrary* axis, and one rotation on the left rotates that axis to $e_1$. This is the standard route from polar ($\Lambda = S\circ R$, one rotation) to Cartan ($\Lambda = K A K$, two rotations).

**Theorem routing.** Part 1 starts from [[Thm - Polar Decomposition of the Lorentz Group|the polar decomposition]] $\Lambda = S\circ R'$, then writes the boost $S$ of axis $\mathbf{n}$ as $S = R(H) B[V] R(H)^{-1}$ (conjugation rotating $e_1 \to \mathbf{n}$), giving $\Lambda = R(H) B[V] (R(H)^{-1} R')$, which is $KAK$. Part 2 routes through the trace/Lorentz-factor invariants. Parts 3–4 are dimension counting against $\dim SO^+(1,3) = 6$ ([[Def - Subgroups and Components of the Lorentz Group]]).

**Key decision point.** The crux of the parameter count is recognising that the boost along $e_1$ is *fixed* by rotations about $e_1$ — the stabiliser of the axis $e_1$ in $SO(3)$ is a circle $SO(2)$. That one-parameter stabiliser is the redundancy: you can insert $R(C)$ (rotation about $e_1$) on the right of $B[V]$ and $R(C)^{-1}$ on the left without changing the product. The naive-but-wrong move is to treat all seven parameters as independent.

---

# Legal Operations Used

1. **Polar-decompose relative to a chosen 4-velocity** (operation 7): $\Lambda = S\circ R'$, the starting point.

2. **Use the trace/Lorentz factor to extract the boost parameter** (operation 6, most-reusable property): the boost speed $V$ is a coset invariant, computed from $\Lambda$ alone.

3. **Conjugate a boost by a rotation to rotate its axis**: write $S$ (boost along $\mathbf{n}$) as $R(H)B[V]R(H)^{-1}$, the device that standardises the axis.

---

# Hints

> [!note]- Hint 1
> Polar-decompose: $\Lambda = S\circ R'$ with $S$ a boost of some axis $\mathbf{n}$ and $R'$ a rotation fixing $e_0$. Pick $H \in SO(3)$ with $H e_1 = \mathbf{n}$. Then $S = R(H)\,B[V]\,R(H)^{-1}$ (conjugation rotates the boost axis from $e_1$ to $\mathbf{n}$). Substitute: $\Lambda = R(H)\,B[V]\,\big(R(H)^{-1} R'\big)$, and set $H'$ by $R(H') = R(H)^{-1}R'$. That is the $KAK$ form.

> [!note]- Hint 2
> The boost speed is rotation-invariant on both sides, because rotations fix $e_0$ and preserve the Euclidean structure of the rest space. The cleanest invariant is the time–time component combined with the trace: $\Gamma = \cosh\psi$ relates to $\Lambda$ through $\Lambda(e_0)\cdot\Lambda(e_0')$-type contractions, but most directly, the boost speed equals the speed of the polar boost $S$, which is $\Gamma = e_0\cdot S(e_0)$; and $S(e_0) = \Lambda R'^{-1}(e_0) = \Lambda(e_0)$ since $R'$ fixes $e_0$. So $\Gamma = e_0\cdot\Lambda(e_0) = \Lambda^0{}_0$. The boost speed is read off the single entry $\Lambda^0{}_0 = \cosh\psi$.

> [!note]- Hint 3
> Insert the identity $R(C)^{-1}R(C)$ between $B[V]$ and $R(H')$, where $R(C)$ is a rotation *about the boost axis* $e_1$. Since $R(C)$ commutes with $B[V]$ (a rotation about the boost axis leaves the boost invariant: $R(C)B[V] = B[V]R(C)$), you get
> $$R(H)B[V]R(H') = R(H)R(C)^{-1}\,B[V]\,R(C)R(H') = R(HC^{-1})\,B[V]\,R(CH').$$
> So $(H, H') \mapsto (HC^{-1}, CH')$ for any rotation $C$ about $e_1$ gives the *same* $\Lambda$. That is the one-parameter redundancy.

> [!note]- Hint 4
> The stabiliser of the boost axis $e_1$ inside $K = SO(3)$ is the circle of rotations about $e_1$, namely $SO(2)$, which is one-dimensional. The genuine parameters are therefore $H$ modulo this $SO(2)$ on the right ($\dim = 3 - 1 = 2$, a point of $S^2$ — the boost *direction*), plus the speed $V$ ($\dim 1$), plus the full $H'$ ($\dim 3$): total $2 + 1 + 3 = 6$. Equivalently $3 + 1 + 3 - 1 = 6$.

---

# Solution

We build the $KAK$ form from the polar decomposition (Step 1), extract the boost speed as a coset invariant (Step 2), locate the one-parameter redundancy (Step 3), and balance the dimensions (Step 4).

**Step 1: From polar to $KAK$.**

> [!note]- Derivation
> By [[Thm - Polar Decomposition of the Lorentz Group|the polar decomposition]] relative to $e_0$, write
> $$\Lambda = S\circ R',$$
> with $S$ a boost (axis $\mathbf{n}$, a unit vector in the rest space $E$, speed $V$, rapidity $\psi$) and $R'$ a spatial rotation fixing $e_0$. Choose any $H \in SO(3)$ with $H e_1 = \mathbf{n}$ (such $H$ exists since $SO(3)$ acts transitively on unit vectors). Conjugating the standard boost along $e_1$ by $R(H)$ rotates its axis to $\mathbf{n}$:
> $$S = R(H)\,B[V]\,R(H)^{-1}.$$
> Substituting,
> $$\Lambda = R(H)\,B[V]\,R(H)^{-1}\,R' = R(H)\,B[V]\,R(H'), \qquad R(H') := R(H)^{-1}R'.$$
> Here $H' \in SO(3)$ because $R(H)^{-1}$ and $R'$ both fix $e_0$ and have block form, so their product does. This is the Cartan decomposition $\Lambda = R(H)\,B[V]\,R(H') \in K A K$. Existence is established for every $\Lambda \in SO^+(1,3)$.

**Step 2: The boost speed is a coset invariant.**

> [!note]- Derivation
> The two flanking rotations fix $e_0$. Hence
> $$\Lambda(e_0) = R(H)\,B[V]\,R(H')(e_0) = R(H)\,B[V](e_0) = R(H)\big(\cosh\psi\,e_0 + \sinh\psi\,e_1\big),$$
> and taking the time-component (rotations preserve it),
> $$\Lambda^0{}_0 = e_0\cdot\Lambda(e_0) = \cosh\psi = \Gamma = \frac{1}{\sqrt{1 - V^2}}.$$
> So the boost speed is read off the single matrix entry $\Lambda^0{}_0$, which is manifestly unchanged if we replace $\Lambda$ by $R(H_1)\Lambda R(H_2)$ for any rotations $H_1, H_2$ (both fix $e_0$, both preserve its time-component). Therefore $V$ (equivalently $\Gamma = \Lambda^0{}_0$, equivalently $\psi = \mathrm{arcosh}\,\Lambda^0{}_0$) is an invariant of the *double coset* $K\Lambda K$. This is the abelian "$A$-part" of the Cartan decomposition: it is the genuine geometric content, the magnitude of the velocity, with the two rotations carrying only orientation information.

**Step 3: The one-parameter redundancy.**

> [!note]- Derivation
> A rotation $R(C)$ *about the boost axis* $e_1$ commutes with the boost $B[V]$: the boost acts only in the $(e_0, e_1)$-plane and fixes $(e_2, e_3)$, while $R(C)$ acts only in the $(e_2, e_3)$-plane and fixes $(e_0, e_1)$, so the two act on complementary subspaces and commute,
> $$R(C)\,B[V] = B[V]\,R(C).$$
> Therefore, for any such $C$ (a one-parameter family, $C \in SO(2)$ = rotations about $e_1$),
> $$R(H)\,B[V]\,R(H') = R(H)\,\underbrace{R(C)^{-1}R(C)}_{=\,\mathrm{Id}}\,B[V]\,R(H') = R(HC^{-1})\,B[V]\,\big(R(C)R(H')\big) = R(HC^{-1})\,B[V]\,R(CH').$$
> So the *distinct* pairs $(H, H')$ and $(HC^{-1}, CH')$ produce the **same** $\Lambda$. The map $(H, V, H') \mapsto \Lambda$ has a one-parameter fibre over each generic $\Lambda$ (generic meaning $V \ne 0$, so the axis $e_1$ is genuinely distinguished). This is the redundancy that reconciles seven parameters with a six-dimensional group.

**Step 4: Dimension bookkeeping.**

> [!note]- Derivation
> The raw parameter count is
> $$\dim K + \dim A + \dim K = 3 + 1 + 3 = 7.$$
> The redundancy is the stabiliser of the boost axis $e_1$ inside $K = SO(3)$ — the rotations about $e_1$ — which is the circle $SO(2)$, of dimension $1$. Subtracting,
> $$3 + 1 + 3 - 1 = 6 = \dim SO^+(1,3).$$
> The bookkeeping balances. Conceptually: the left rotation $H$ is only defined up to the choice of how to map $e_1$ to the boost axis $\mathbf{n}$, and that choice is free by a rotation about $\mathbf{n}$ (equivalently about $e_1$ before conjugation). So the honest parameters are: the boost *direction* $\mathbf{n} = H e_1 \in S^2$ ($\dim 2$, this is $H$ modulo the right $SO(2)$), the boost *speed* $V$ ($\dim 1$), and the second rotation $H'$ ($\dim 3$), totalling $2 + 1 + 3 = 6$. The redundancy is one-dimensional precisely because a boost has a one-dimensional axial symmetry group — rotations about its own axis leave it invariant — which is the same reason a boost is determined by a point of $S^2$ (direction) and a scalar (speed), four numbers, rather than by a generic element of the group.

> [!note]- Complete formal solution
> Polar-decompose $\Lambda = S\circ R'$ (boost $S$ of axis $\mathbf{n}$, speed $V$; rotation $R'$ fixing $e_0$). Choosing $H \in SO(3)$ with $He_1 = \mathbf{n}$, conjugation gives $S = R(H)B[V]R(H)^{-1}$, so $\Lambda = R(H)B[V]R(H')$ with $R(H') = R(H)^{-1}R'$: the Cartan $KAK$ form. Since the flanking rotations fix $e_0$, $\Lambda^0{}_0 = e_0\cdot\Lambda(e_0) = \cosh\psi = \Gamma = (1-V^2)^{-1/2}$, so $V$ is a $K\Lambda K$ double-coset invariant. The redundancy: rotations $R(C)$ about $e_1$ commute with $B[V]$, so $R(H)B[V]R(H') = R(HC^{-1})B[V]R(CH')$ for all $C \in SO(2)$, a one-parameter family of pairs giving the same $\Lambda$. Hence $3 + 1 + 3 - 1 = 6 = \dim SO^+(1,3)$: the honest parameters are the boost direction $\mathbf{n} \in S^2$ ($2$), the speed $V$ ($1$), and $H' \in SO(3)$ ($3$). $\blacksquare$

---

# Key Takeaways

**The $KAK$ decomposition reduces every Lorentz computation to a boost along a single fixed axis.** The Cartan form $\Lambda = R(H)\,B[V]\,R(H')$ standardises the boost to lie along $e_1$, absorbing all directional information into the two flanking rotations. The payoff is enormous in practice: any quantity that depends only on the boost magnitude — the Lorentz factor, the proper-time relation, the energy of a particle in the boosted frame — can be computed for the standard axial boost $B[V]$ and then dressed with rotations. This is the relativistic instance of the general $G = KAK$ decomposition of a semisimple Lie group ($K$ maximal compact, $A$ abelian), the same structure that lets spherical harmonics diagonalise rotation-invariant operators. The reusable move: when a problem involves a generic Lorentz transformation but the physics is rotation-invariant, $KAK$-decompose and work with the axial boost alone.

**A boost magnitude is a double-coset invariant: it survives rotations on both sides.** The single entry $\Lambda^0{}_0 = \cosh\psi$ is unchanged by $\Lambda \mapsto R_1 \Lambda R_2$ for any spatial rotations, because rotations fix $e_0$ and preserve its time-component. This makes the boost speed the genuine, frame-orientation-independent content of a Lorentz transformation — the "$A$-part" of the Cartan decomposition — while the rotations carry only orientation. The trigger "what is invariant about this transformation under change of spatial axes" should fire "the boost magnitude $\Lambda^0{}_0 = \Gamma$." This is why $\Lambda^0{}_0$ appears so often as the fundamental scalar (it is the relative Lorentz factor of the two observers), and why classification by trace and by $\Lambda^0{}_0$ is rotation-robust.

**Over-counting parameters is resolved by the symmetry group of the standardised object — here the axial symmetry of a boost.** The apparent seven parameters of $(H, V, H')$ exceed the group's dimension by one, and the excess is exactly the one-parameter stabiliser of the boost axis: rotations about $e_1$ commute with $B[V]$ and can be shuffled between the two flanking rotations without changing $\Lambda$. This is a completely general principle for redundant parametrisations: whenever you write a group element through a standardised piece flanked by symmetry transformations, the redundancy equals the dimension of the standardised piece's stabiliser. A boost has a one-dimensional stabiliser (the circle of rotations about its axis), so the $KAK$ redundancy is one-dimensional, and a boost is honestly specified by four numbers (direction on $S^2$ plus speed) rather than by a generic group element. Recognising the stabiliser is the way to make any over-complete coordinate system honest.
