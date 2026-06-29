---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - The Lorentz Group"
  - "Def - Boosts as Hyperbolic Rotations"
tags: [physics, special-relativity]
---

# Problem Statement

Work with $\eta = \mathrm{diag}(1,-1,-1,-1)$.

1. Count the dimension of the [[Def - The Lorentz Group|Lorentz group]] directly from its defining equation: a $4\times 4$ matrix has $16$ entries, and $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$ imposes how many independent constraints? Deduce that $SO^+(1,3)$ is six-dimensional.
2. Exhibit the six parameters concretely: three for spatial [[Def - Boosts as Hyperbolic Rotations|rotations]] $\mathrm{diag}(1, H)$ with $H \in SO(3)$, and three for boosts (one along each axis). Show that a pure boost matrix and a pure rotation matrix each satisfy $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$.
3. Every restricted Lorentz transformation can be written as a rotation, then a standard ($x$-axis) boost, then another rotation: $\Lambda = R(H)\,B_x(\varphi)\,R(H')$ (a *polar-type* decomposition). This parametrisation naively uses $3 + 1 + 3 = 7$ parameters. Reconcile this with the group being six-dimensional (Oxford's Exercise 4): which parameter is redundant, and why?
4. Relate the count to the planes of $\mathbb{R}^4$: show $6 = \binom{4}{2}$ is the number of coordinate planes, and that each plane carries either a rotation (spacelike planes) or a boost (timelike planes).

**Recall:**

![[Def - The Lorentz Group#The Definition]]

The defining equation $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$ equates two *symmetric* $4\times 4$ matrices. A symmetric $n \times n$ matrix has $n(n+1)/2$ independent entries. The rotation group $SO(3)$ is three-dimensional. A boost along a chosen axis is the [[Def - Boosts as Hyperbolic Rotations|hyperbolic rotation]] $\begin{pmatrix} \cosh\varphi & \sinh\varphi \\ \sinh\varphi & \cosh\varphi \end{pmatrix}$ in the time–axis plane.

---

# Convergent Strategy

**Problem class.** A *structural / dimension-counting* problem: determine the number of parameters of a matrix group from its defining equation and exhibit them. The fourth target of the [[Special Relativity IV — The Invariant Interval, Rapidity and the Lorentz Group#Problem-Solving Strategy|topic strategy]].

**Assumption pattern.** The defining equation $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$ with both sides *symmetric*. The key recognition is that a symmetric-matrix equation imposes only $n(n+1)/2$ constraints, not $n^2$ — the redundancy of the symmetric condition is what makes the count come out to $6$ rather than $0$.

**Theorem routing.** Part 1 is the constraint count $16 - 10 = 6$; Part 2 exhibits a spanning set of one-parameter subgroups; Part 3 is the redundancy in the polar decomposition; Part 4 is the $\binom{4}{2}$ planes interpretation. The route is: count constraints $\to$ exhibit generators $\to$ reconcile the redundant parametrisation $\to$ interpret as rotation/boost planes.

**Key decision point.** The crux of Part 1 is realising that $\Lambda^{\mathsf T}\eta\,\Lambda$ is *automatically symmetric*, so the equation $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$ only constrains the $10$ independent entries of a symmetric matrix, not all $16$. The crux of Part 3 is identifying *which* of the $7$ polar parameters is redundant: the rotation about the boost axis can be absorbed, because a boost commutes with rotations about its own axis.

---

# Legal Operations Used

1. **Count constraints from a symmetric matrix equation.** $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$ is an equation between symmetric matrices, contributing $10$ constraints; $16 - 10 = 6$.

2. **Exhibit one-parameter subgroups (operation: switch to rapidity / build from rotations and boosts).** The six parameters are realised as three rotation angles and three rapidities, each a one-parameter subgroup.

3. **Decompose into rotation and boost (operation: the polar-type factorisation).** Writing $\Lambda = R\,B_x\,R'$ exhibits the structure and exposes the redundancy.

---

# Hints

> [!note]- Hint 1
> The product $\Lambda^{\mathsf T}\eta\,\Lambda$ is symmetric for *any* $\Lambda$ (check: $(\Lambda^{\mathsf T}\eta\Lambda)^{\mathsf T} = \Lambda^{\mathsf T}\eta^{\mathsf T}\Lambda = \Lambda^{\mathsf T}\eta\Lambda$ since $\eta^{\mathsf T} = \eta$). So the equation $\Lambda^{\mathsf T}\eta\Lambda = \eta$ equates two symmetric $4\times 4$ matrices, which is $4\cdot 5/2 = 10$ scalar equations, not $16$.

> [!note]- Hint 2
> A rotation $\mathrm{diag}(1, H)$, $H \in SO(3)$: it fixes $t$ and preserves $|\mathbf{x}|^2$, hence $t^2 - |\mathbf{x}|^2$. A boost along $x$: check $\begin{pmatrix} \cosh\varphi & \sinh\varphi \\ \sinh\varphi & \cosh\varphi \end{pmatrix}^{\mathsf T}\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}\begin{pmatrix} \cosh\varphi & \sinh\varphi \\ \sinh\varphi & \cosh\varphi \end{pmatrix}$ equals $\mathrm{diag}(1,-1)$.

> [!note]- Hint 3
> In $\Lambda = R(H)B_x(\varphi)R(H')$, the boost $B_x$ commutes with rotations about the $x$-axis (its own axis). So a rotation of $R'$ about the $x$-axis can be moved through $B_x$ and absorbed into $R$. This removes one of the three angles of $R'$, leaving $3 + 1 + 3 - 1 = 6$.

> [!note]- Hint 4
> A rotation lives in a *spacelike* coordinate plane ($xy$, $yz$, $zx$ — three of them). A boost lives in a *timelike* coordinate plane ($tx$, $ty$, $tz$ — three of them). Total $3 + 3 = 6 = \binom{4}{2}$, the number of coordinate planes in $\mathbb{R}^4$.

---

# Solution

The exercise counts the six parameters four ways and shows they all agree. Step 1 counts constraints. Step 2 exhibits the six one-parameter subgroups. Step 3 resolves the apparent over-counting in the polar decomposition. Step 4 interprets six as the number of planes. The throughline is that the Lorentz group is the "rotation group of $\mathbb{R}^4$ with an indefinite metric", and six is $\binom{4}{2}$.

**Step 1: the constraint count gives dimension six.**

> [!note]- Derivation
> The matrix $\Lambda$ has $4 \times 4 = 16$ real entries. The defining equation is $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$. The left-hand side is symmetric for *every* $\Lambda$:
> $$(\Lambda^{\mathsf T}\eta\,\Lambda)^{\mathsf T} = \Lambda^{\mathsf T}\eta^{\mathsf T}(\Lambda^{\mathsf T})^{\mathsf T} = \Lambda^{\mathsf T}\eta\,\Lambda,$$
> using $\eta^{\mathsf T} = \eta$. So the equation equates two *symmetric* $4\times 4$ matrices, and a symmetric $4\times 4$ matrix has $4\cdot 5/2 = 10$ independent entries. Therefore the defining equation imposes $10$ independent scalar constraints, and the solution set has dimension
> $$16 - 10 = 6.$$
> Hence $O(1,3)$ (and its identity component $SO^+(1,3)$) is a six-dimensional manifold — a six-parameter Lie group. (If one had mistakenly counted $16$ constraints, expecting the all-entries equation, one would wrongly conclude dimension $0$; the symmetry of the product is exactly what saves six dimensions.)

**Step 2: the six one-parameter subgroups.**

> [!note]- Derivation
> *Three rotations.* For $H \in SO(3)$ (so $H^{\mathsf T}H = I$, $\det H = 1$), the block matrix $\Lambda = \mathrm{diag}(1, H) = \begin{pmatrix} 1 & 0 \\ 0 & H \end{pmatrix}$ satisfies
> $$\Lambda^{\mathsf T}\eta\,\Lambda = \begin{pmatrix} 1 & 0 \\ 0 & H^{\mathsf T} \end{pmatrix}\begin{pmatrix} 1 & 0 \\ 0 & -I \end{pmatrix}\begin{pmatrix} 1 & 0 \\ 0 & H \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & -H^{\mathsf T}H \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & -I \end{pmatrix} = \eta.$$
> $SO(3)$ is three-dimensional (rotations about the three axes), contributing three parameters.
>
> *Three boosts.* The boost along $x$ in the $(t,x)$ block is $B_x(\varphi) = \begin{pmatrix} \cosh\varphi & \sinh\varphi \\ \sinh\varphi & \cosh\varphi \end{pmatrix}$ (identity on $y, z$). Check:
> $$\begin{pmatrix} \cosh\varphi & \sinh\varphi \\ \sinh\varphi & \cosh\varphi \end{pmatrix}\begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}\begin{pmatrix} \cosh\varphi & \sinh\varphi \\ \sinh\varphi & \cosh\varphi \end{pmatrix} = \begin{pmatrix} \cosh\varphi & -\sinh\varphi \\ \sinh\varphi & -\cosh\varphi \end{pmatrix}\begin{pmatrix} \cosh\varphi & \sinh\varphi \\ \sinh\varphi & \cosh\varphi \end{pmatrix} = \begin{pmatrix} \cosh^2\varphi - \sinh^2\varphi & 0 \\ 0 & \sinh^2\varphi - \cosh^2\varphi \end{pmatrix} = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}.$$
> Boosts along $y$ and $z$ are analogous, contributing three more parameters (one rapidity per axis). Three rotations $+$ three boosts $= 6$, matching Step 1.

**Step 3: the redundant seventh parameter in the polar decomposition.**

> [!note]- Derivation
> Oxford's claim is that every restricted Lorentz transformation factors as $\Lambda = R(H)\,B_x(\varphi)\,R(H')$ with $H, H' \in SO(3)$ and $\varphi$ a rapidity. Naively this is $3 + 1 + 3 = 7$ parameters, one more than the group's dimension. The resolution: **the boost $B_x(\varphi)$ commutes with rotations about the $x$-axis**, since a rotation in the $yz$-plane leaves the $(t,x)$ block untouched and $B_x$ leaves the $yz$ block untouched. So if $R_x(\alpha)$ is a rotation about the $x$-axis,
> $$B_x(\varphi)\,R_x(\alpha) = R_x(\alpha)\,B_x(\varphi).$$
> Write $R(H') = R_x(\alpha)\,R'(H'')$, splitting off the $x$-axis rotation $R_x(\alpha)$ from $R'$. Then
> $$\Lambda = R(H)\,B_x(\varphi)\,R_x(\alpha)\,R'(H'') = R(H)\,R_x(\alpha)\,B_x(\varphi)\,R'(H'') = \big[R(H)R_x(\alpha)\big]\,B_x(\varphi)\,R'(H''),$$
> and the $x$-axis rotation $R_x(\alpha)$ has been absorbed into the left rotation. So one of the three angles of $R(H')$ is redundant — it can always be moved through the boost and merged with $R(H)$ — leaving $3 + 1 + 3 - 1 = 6$ independent parameters, in agreement with Steps 1–2. (Equivalently: the boost direction is specified by $2$ angles plus a rapidity $= 3$ boost parameters, and the spatial frame of the boosted observer by $3$ rotation parameters; the rotation about the boost axis is shared between "specifying the boost direction" and "orienting the frame", hence counted once, not twice.)

**Step 4: six as the number of planes.**

> [!note]- Derivation
> The number of coordinate planes in $\mathbb{R}^4$ is $\binom{4}{2} = 6$: the planes $tx, ty, tz$ (each containing the time axis) and $xy, yz, zx$ (purely spatial). The Lorentz group is the "rotation group" of $\mathbb{R}^4$ with the indefinite metric, and it acts in each plane:
> - In a **spacelike** plane ($xy, yz, zx$ — both axes spacelike, metric $\mathrm{diag}(-1,-1)$), the isometry is an ordinary rotation, parametrised by an *angle* — three of these.
> - In a **timelike** plane ($tx, ty, tz$ — one timelike, one spacelike axis, metric $\mathrm{diag}(1,-1)$), the isometry is a [[Def - Boosts as Hyperbolic Rotations|boost]] (hyperbolic rotation), parametrised by a *rapidity* — three of these.
>
> So $6 = \binom{4}{2} = 3\ \text{rotations} + 3\ \text{boosts}$, and each generator of the [[Def - Lie Algebra of the Lorentz Group|Lie algebra]] $\mathfrak{so}(1,3)$ corresponds to one plane: the three $J_i$ (rotation generators) to the spacelike planes, the three $K_i$ (boost generators) to the timelike planes. The signature of each plane (definite or indefinite) decides whether its isometry is a circular rotation or a hyperbolic boost — the same definite-vs-indefinite distinction as in [[Def - Boosts as Hyperbolic Rotations]], now plane by plane.

> [!note]- Complete formal solution
> *Dimension.* $\Lambda^{\mathsf T}\eta\Lambda$ is symmetric for all $\Lambda$ (since $\eta^{\mathsf T} = \eta$), so $\Lambda^{\mathsf T}\eta\Lambda = \eta$ is an equation between symmetric $4\times 4$ matrices, i.e. $10$ constraints; $\dim = 16 - 10 = 6$. *Generators.* $\mathrm{diag}(1, H)$ with $H \in SO(3)$ satisfies the defining equation ($-H^{\mathsf T}H = -I$), giving $3$ rotation parameters; the boost $B_x(\varphi)$ satisfies it ($\cosh^2 - \sinh^2 = 1$), giving (with $y, z$) $3$ boost parameters; total $6$. *Polar decomposition.* $\Lambda = R(H)B_x(\varphi)R(H')$ is naively $7$ parameters, but $B_x$ commutes with rotations $R_x$ about its own axis, so the $x$-axis part of $R(H')$ moves through $B_x$ and merges with $R(H)$, removing one parameter: $7 - 1 = 6$. *Planes.* $6 = \binom{4}{2}$ coordinate planes of $\mathbb{R}^4$; the three spacelike planes carry rotations, the three timelike planes carry boosts, the signature of each plane fixing circular vs hyperbolic. $\blacksquare$

> [!warning] Illegal but tempting alternative route
> One might count constraints by treating $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$ as $16$ scalar equations (one per matrix entry) and conclude the group is $0$-dimensional — a single point. This is wrong because the equation is *not* $16$ independent conditions: both sides are symmetric, so the $6$ off-diagonal equations above the diagonal duplicate the $6$ below it, leaving only $10$ independent conditions. Forgetting that $\Lambda^{\mathsf T}\eta\,\Lambda$ is automatically symmetric is the standard error in dimension-counting for orthogonal-type groups, and it gives the wrong dimension for $O(n)$ too ($n(n-1)/2$, not $0$). Always check whether the matrix equation is between symmetric (or antisymmetric) matrices before counting.

---

# Key Takeaways

**Count constraints by the symmetry type of the defining equation, not the number of entries.** The reusable technique for finding the dimension of a matrix group $\{\Lambda : \Lambda^{\mathsf T} g\,\Lambda = g\}$ is to notice that $\Lambda^{\mathsf T} g\,\Lambda$ is automatically symmetric (when $g$ is), so the equation imposes only $n(n+1)/2$ constraints, giving $\dim = n^2 - n(n+1)/2 = n(n-1)/2$. For $n = 4$ this is $6$ — the dimension of every $O(p, q)$ with $p + q = 4$, including the Lorentz group $O(1,3)$, the Euclidean $O(4)$, and the split $O(2,2)$, all six-dimensional. The signature affects the *geometry* (which planes carry boosts) but not the *dimension*. The trigger to apply this: any group defined by preserving a symmetric form, where the naive "one equation per entry" count gives a nonsensically small dimension.

**The six parameters are the six coordinate planes, with signature deciding rotation versus boost.** The deepest organising picture is that the Lorentz group is the rotation group of $\mathbb{R}^4$ under an indefinite metric, and a "rotation" lives in a plane: there are $\binom{4}{2} = 6$ coordinate planes, and the metric restricted to each is either definite (spacelike planes $\to$ ordinary rotations, three of them) or indefinite (timelike planes $\to$ boosts, three of them). This plane-by-plane decomposition is exactly the split of the [[Def - Lie Algebra of the Lorentz Group|Lie algebra]] into three rotation generators $J_i$ and three boost generators $K_i$, and it explains structurally why there are precisely three rotations and three boosts. The same counting applies to any $SO(p, q)$: the number of generators is $\binom{p+q}{2}$, split into $\binom{p}{2} + \binom{q}{2}$ rotations (within the timelike and within the spacelike blocks) and $pq$ boosts (mixing the two blocks). For $SO(1,3)$: $\binom{1}{2} + \binom{3}{2} = 0 + 3 = 3$ rotations and $1 \cdot 3 = 3$ boosts.

**A redundant parametrisation signals a commuting subgroup absorbed into a factor.** The reconciliation of the $7$-parameter polar decomposition with the $6$-dimensional group teaches a general lesson: when a factorisation has more parameters than the group's dimension, the excess comes from a subgroup that commutes with one of the factors and can be absorbed. Here the rotation about the boost axis commutes with the boost and merges into the adjacent rotation, removing one parameter. This is the same phenomenon as the redundancy in Euler-angle-type decompositions and in the $KAK$ (Cartan) decomposition of Lie group theory, where the compact factors overlap. Whenever you meet an over-determined parametrisation, look for the commuting subgroup that links two factors; absorbing it gives the true parameter count and reveals the genuine degrees of freedom — here, the boost direction (two angles plus a rapidity) and the spatial orientation of the boosted frame (three angles), sharing the rotation about the boost axis.
