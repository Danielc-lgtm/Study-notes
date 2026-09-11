---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - The Maurer-Cartan Form"
  - "Ex - Volume of the n-Sphere via the Volume Form"
  - "Ex - SU(2) is the Group of Unit Quaternions"
  - "Def - Riemannian Volume Form"
  - "Thm - Classification of Principal SU(2)-Bundles over Four-Manifolds"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $\theta \in \Omega^1(SU(2); \mathfrak{su}(2))$ be the left Maurer–Cartan form of the group $SU(2)$, so that for a matrix group $\theta = g^{-1}\,dg$, and let $\operatorname{tr}$ denote the trace in the defining two-dimensional representation. The three-form
$$\operatorname{tr}(\theta^3) := \operatorname{tr}(\theta \wedge \theta \wedge \theta) \in \Omega^3(SU(2); \mathbb{R})$$
is the bi-invariant three-form that appears — pulled back along a map $g\colon M \to SU(2)$ — in the gauge variation of the Chern–Simons functional and in the winding number $W(g) = \tfrac{1}{24\pi^2}\int_{S^3}\operatorname{tr}((g^{-1}dg)^3)$ that measures the degree of $g$. Its total integral over the group is a single universal constant, and computing that constant is the point of this exercise.

Orient $SU(2)$ as the three-sphere $S^3$: under the identification $SU(2) \cong Sp(1) = \{q \in \mathbb{H} : |q| = 1\}$ with the unit quaternions, $S^3$ carries the orientation **as the boundary of the closed unit ball in $\mathbb{H} = \mathbb{R}^4$, outward normal first** — a basis $(v_1, v_2, v_3)$ of $T_pS^3$ is positive if and only if $(p, v_1, v_2, v_3)$ is a positively oriented basis of $\mathbb{R}^4$ under its standard orientation, the one for which $(1, \mathrm{i}, \mathrm{j}, \mathrm{k})$ is positive. Equip $S^3$ with the round metric of radius $1$, the restriction of the Euclidean metric of $\mathbb{R}^4$, so that $\operatorname{Vol}(S^3) = 2\pi^2$.

**Prove the three assertions:**

1. **(The constant at the identity.)** On the basis $E_a := -\mathrm{i}\sigma_a$ ($a = 1, 2, 3$) of $\mathfrak{su}(2)$, where $\sigma_1, \sigma_2, \sigma_3$ are the Pauli matrices, the three-form $\operatorname{tr}(\theta^3)$ evaluated at the identity satisfies
$$\operatorname{tr}(\theta^3)_e(E_1, E_2, E_3) = -12.$$

2. **(Identification with the volume form.)** As forms on $SU(2)$, $\operatorname{tr}(\theta^3) = -12\,\mathrm{vol}_{S^3}$, where $\mathrm{vol}_{S^3}$ is the Riemannian volume form of the round metric of radius $1$ with the boundary orientation above.

3. **(The total integral.)** Consequently
$$\boxed{\;\int_{SU(2)} \operatorname{tr}(\theta \wedge \theta \wedge \theta) = -24\pi^2\;}$$
and, for a general smooth $g\colon S^3 \to SU(2)$, $\displaystyle\int_{S^3}\operatorname{tr}((g^{-1}dg)^3) = -24\pi^2\,\deg g$, so $W(g) = -\deg g$.

The sign is not a matter of taste: it is fixed by the orientation of $SU(2) \cong S^3$ recorded above. The source (Haydys, Exercise 96(d)) writes the relation $W(g) = \deg g$ without committing to a sign convention; under the orientation fixed for this series the correct constant is $\int_{SU(2)}\operatorname{tr}(\theta^3) = -24\pi^2$ and hence $W(g) = -\deg g$, in agreement with the [[Def - The Hopf Bundle#Sign ledger|sign ledger]] on the Hopf-bundle page, where this same constant is the ledger's item (a).

**Recall:**

The objects in play are the Maurer–Cartan form, the trace and bracket of $\mathfrak{su}(2)$, the round metric and volume of $S^3$, and the identification $SU(2) \cong Sp(1)$.

![[Def - The Maurer-Cartan Form#The Definition]]

The [[Def - The Maurer-Cartan Form|Maurer–Cartan form]] is *left-invariant* ($L_h^*\theta = \theta$ for all $h \in SU(2)$) and satisfies $\theta_e = \operatorname{id}_{\mathfrak{su}(2)}$; both facts are used decisively — left-invariance makes $\operatorname{tr}(\theta^3)$ a left-invariant top-degree form, hence a constant multiple of any left-invariant volume form, and $\theta_e = \operatorname{id}$ makes the constant computable by plugging Lie-algebra elements straight into the trace.

The Pauli matrices and the basis of $\mathfrak{su}(2)$ we use are
$$\sigma_1 = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix},\quad \sigma_2 = \begin{pmatrix} 0 & -\mathrm{i} \\ \mathrm{i} & 0 \end{pmatrix},\quad \sigma_3 = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix},\qquad E_a = -\mathrm{i}\sigma_a.$$
Each $E_a$ is skew-Hermitian ($E_a^* = (-\mathrm{i}\sigma_a)^* = \mathrm{i}\sigma_a = -E_a$) and traceless, so $E_a \in \mathfrak{su}(2)$, and the three of them form a basis of the three-dimensional real vector space $\mathfrak{su}(2)$ of traceless skew-Hermitian $2\times 2$ matrices.

![[Ex - Volume of the n-Sphere via the Volume Form#Problem Statement]]

The volume of the round unit three-sphere is $\operatorname{Vol}(S^3) = 2\pi^2$, computed on [[Ex - Volume of the n-Sphere via the Volume Form|the sphere-volume page]]; this is the only numerical input to the final integral.

![[Def - Riemannian Volume Form#The Definition]]

On an oriented Riemannian manifold the [[Def - Riemannian Volume Form|Riemannian volume form]] $\mathrm{vol}$ is the unique top-degree form taking the value $+1$ on every positively oriented orthonormal frame; equivalently $\mathrm{vol}(v_1, \dots, v_n) = +1$ whenever $(v_1, \dots, v_n)$ is an oriented orthonormal basis. This characterisation is exactly what lets us pass from "$\operatorname{tr}(\theta^3)_e = -12$ on an oriented orthonormal frame" to "$\operatorname{tr}(\theta^3) = -12\,\mathrm{vol}_{S^3}$".

The identification $SU(2) \cong Sp(1)$ we use — proved on [[Ex - SU(2) is the Group of Unit Quaternions|the unit-quaternions page]] — sends the quaternion $q = a + b\,\mathrm{i} + c\,\mathrm{j} + d\,\mathrm{k}$ (with $a,b,c,d \in \mathbb{R}$, $a^2+b^2+c^2+d^2 = 1$) to the matrix
$$q \;\longleftrightarrow\; \begin{pmatrix} a + b\mathrm{i} & c + d\mathrm{i} \\ -c + d\mathrm{i} & a - b\mathrm{i} \end{pmatrix} \in SU(2),$$
a Lie group isomorphism carrying the tangent space $T_1 S^3 = \operatorname{Im}\mathbb{H} = \operatorname{span}_\mathbb{R}(\mathrm{i}, \mathrm{j}, \mathrm{k})$ onto $\mathfrak{su}(2) = T_e SU(2)$.

---

# Convergent Strategy

**Problem class.** This is an *invariant-integration* problem: an integral of a differential form over a compact group, reduced to a single evaluation at the identity by exploiting invariance. The deliverable is a universal constant. The recognisable shape is "a bi-invariant top-degree form on a Lie group is a constant multiple of the volume form, and the constant is read off on one orthonormal frame at the identity." The whole difficulty is compressed into two sub-tasks: an algebraic one (evaluate the trace at $e$) and a geometric one (check that the chosen frame is *oriented* and *orthonormal*, which pins both the magnitude and the sign of the constant).

**Assumption pattern.** Three inputs are used, each once. *Left-invariance of $\theta$* turns the global integral into a pointwise computation at $e$ (a left-invariant three-form on a three-dimensional group is determined by its value on one frame). *The relations of $\mathfrak{su}(2)$* — the brackets $[E_a, E_b] = 2\varepsilon_{abc}E_c$ and the trace form $\operatorname{tr}(E_aE_b) = -2\delta_{ab}$ — deliver the number $-12$. *The orientation and round metric of $S^3$*, through the quaternionic identification, certify that $(E_1, E_2, E_3)$ is a *positively oriented orthonormal* frame, which is precisely the condition that converts $-12$ into $-12\,\mathrm{vol}_{S^3}$ with the correct sign.

**Theorem routing.** The route is: (1) reduce $\operatorname{tr}(\theta^3)(X,Y,Z)$ to the bracket expression $3\operatorname{tr}(X[Y,Z])$ by expanding the wedge over permutations and using cyclicity of the trace; (2) evaluate at $e$ on the frame $(E_1, E_2, E_3)$ using $[E_2, E_3] = 2E_1$ and $\operatorname{tr}(E_1^2) = -2$, giving $-12$; (3) observe via [[Def - The Maurer-Cartan Form|left-invariance]] that $\operatorname{tr}(\theta^3)$ is a constant multiple of the [[Def - Riemannian Volume Form|volume form]], and identify the constant by checking with the quaternionic identification of [[Ex - SU(2) is the Group of Unit Quaternions|SU(2) ≅ Sp(1)]] that $(E_1, E_2, E_3)$ is an oriented orthonormal frame, so the constant is exactly $-12$; (4) integrate, using $\operatorname{Vol}(S^3) = 2\pi^2$ from [[Ex - Volume of the n-Sphere via the Volume Form|the sphere-volume page]], to get $-24\pi^2$; (5) pull back along a general $g$ and use the degree to reach $W(g) = -\deg g$, the constant that enters [[Thm - Classification of Principal SU(2)-Bundles over Four-Manifolds|the SU(2)-bundle classification]].

**Key decision point.** The magnitude $12$ is a routine trace computation; the genuine subtlety — and the reason the exercise is starred rather than routine — is the *sign*, which requires two independent checks that are easy to conflate. The frame $(E_1, E_2, E_3)$ must be shown *orthonormal* (so that $|\operatorname{tr}(\theta^3)| = 12\,\mathrm{vol}$, no other normalisation) *and* *positively oriented* (so that the sign of the constant is the sign of the number $-12$, not its negative). Both checks go through the quaternionic identification $E_a \leftrightarrow -\mathrm{k}, -\mathrm{j}, -\mathrm{i}$; skipping the orientation check, or using the opposite orientation of $S^3$, flips the answer to $+24\pi^2$ and would make the Chern–Simons functional decrease rather than increase under a positive-degree gauge transformation. The decision to compute $\exp(tE_a)$ explicitly, rather than to guess the correspondence, is what makes the sign trustworthy.

---

# Legal Operations Used

This solution deploys the following operations, named descriptively (the §6.4 topic page numbers them; the orchestrator will reconcile the numbering):

1. **Reduce a wedge of a matrix one-form to a bracket via cyclicity.** Expand $\operatorname{tr}(\theta\wedge\theta\wedge\theta)(X,Y,Z)$ over the six permutations of $(X,Y,Z)$ and use $\operatorname{tr}(XYZ) = \operatorname{tr}(YZX)$ to collapse it to $3\operatorname{tr}(X[Y,Z])$.

2. **Evaluate a left-invariant form at the identity on a Lie-algebra frame.** Because $\theta_e = \operatorname{id}_{\mathfrak{su}(2)}$, plug the basis vectors $E_a \in \mathfrak{su}(2)$ directly into the bracket expression.

3. **Use the structure constants and trace form of $\mathfrak{su}(2)$.** Compute $[E_a, E_b] = 2\varepsilon_{abc}E_c$ and $\operatorname{tr}(E_aE_b) = -2\delta_{ab}$ from the Pauli algebra.

4. **Promote a pointwise value to a form identity via left-invariance.** A left-invariant top-degree form on a three-dimensional group is a constant multiple of any left-invariant volume form; determine the constant on one frame.

5. **Certify a frame as oriented orthonormal through the quaternionic model.** Compute the images of $E_a$ under $SU(2)\cong Sp(1)\subset\mathbb{H} = \mathbb{R}^4$, check they are unit and mutually orthogonal (orthonormal) and that the ordered frame has determinant $+1$ against $(\mathrm{i},\mathrm{j},\mathrm{k})$ with outward normal $p=1$ first (positively oriented).

6. **Integrate a constant multiple of the volume form.** $\int_{SU(2)}\operatorname{tr}(\theta^3) = -12\int_{S^3}\mathrm{vol}_{S^3} = -12\operatorname{Vol}(S^3)$.

7. **Transfer the constant to a general map by the degree.** For $g\colon S^3 \to SU(2)$, $\int_{S^3}g^*\operatorname{tr}(\theta^3) = \deg g \cdot \int_{SU(2)}\operatorname{tr}(\theta^3)$.

---

# Hints

> [!note]- Hint 1
> The form $\operatorname{tr}(\theta^3)$ is left-invariant because $\theta$ is. On a three-dimensional group, a left-invariant three-form is completely determined by its single value on one basis of the Lie algebra at the identity. So the whole integral reduces to (i) one number at $e$ and (ii) comparing that number to the volume form. Start by finding a clean formula for $\operatorname{tr}(\theta^3)(X,Y,Z)$ in terms of Lie-algebra operations only.

> [!note]- Hint 2
> Expand $(\theta\wedge\theta\wedge\theta)(X,Y,Z)$ as the signed sum over the six permutations of $(X,Y,Z)$, then take the trace and use $\operatorname{tr}(PQR) = \operatorname{tr}(QRP)$. The three cyclic (even) permutations give $3\operatorname{tr}(XYZ)$ and the three odd ones give $-3\operatorname{tr}(XZY)$; combine them into a single commutator. At the identity $\theta_e = \operatorname{id}$, so you may replace $\theta(X)$ by $X$ itself.

> [!note]- Hint 3
> With $E_a = -\mathrm{i}\sigma_a$, the Pauli relation $\sigma_a\sigma_b = \delta_{ab}I + \mathrm{i}\varepsilon_{abc}\sigma_c$ gives both $[E_a, E_b] = 2\varepsilon_{abc}E_c$ and $\operatorname{tr}(E_aE_b) = -2\delta_{ab}$. Feed these into the bracket formula from Hint 2 with $(X,Y,Z) = (E_1, E_2, E_3)$; you should land on a small negative integer.

> [!note]- Hint 4
> To turn the number into a multiple of $\mathrm{vol}_{S^3}$ you must know that $(E_1, E_2, E_3)$ is *oriented orthonormal*. Compute the one-parameter subgroups $\exp(tE_a)$ and read off, via $SU(2) \cong Sp(1) \subset \mathbb{H}$, which imaginary quaternion each $E_a$ points to. You will find $(E_1, E_2, E_3) \leftrightarrow (-\mathrm{k}, -\mathrm{j}, -\mathrm{i})$: three orthonormal vectors whose ordered frame has determinant $+1$ against $(\mathrm{i},\mathrm{j},\mathrm{k})$, so with the outward normal $p=1$ placed first, the frame is positively oriented under the boundary orientation of $S^3 = \partial B^4$. Hence the constant is exactly the number you computed, and $\int = (\text{constant})\cdot 2\pi^2$.

---

# Solution

The strategy is to make invariance do the heavy lifting: $\operatorname{tr}(\theta^3)$ is left-invariant, so it equals a constant times the volume form, and the constant is a single evaluation at the identity. The algebra of $\mathfrak{su}(2)$ delivers the magnitude $12$, and the quaternionic picture of $SU(2)$ delivers both the orthonormality and the orientation that fix the sign. We then integrate and transfer to a general map by the degree.

**Step 1: Reduce $\operatorname{tr}(\theta^3)$ to a bracket.**

For any $X, Y, Z \in \mathfrak{su}(2)$,
$$\operatorname{tr}(\theta^3)_e(X, Y, Z) = 3\,\operatorname{tr}(X[Y, Z]).$$

> [!note]- Derivation
> By the definition of the wedge of forms, for the three-form $\theta\wedge\theta\wedge\theta$ and tangent vectors $v_1, v_2, v_3$,
> $$(\theta\wedge\theta\wedge\theta)(v_1, v_2, v_3) = \sum_{\pi \in S_3}\operatorname{sgn}(\pi)\,\theta(v_{\pi(1)})\,\theta(v_{\pi(2)})\,\theta(v_{\pi(3)}) \qquad \text{(definition of the wedge of matrix-valued one-forms),}$$
> the product being matrix multiplication. Take the trace and set $(v_1, v_2, v_3) = (X, Y, Z)$; at the identity $\theta_e = \operatorname{id}_{\mathfrak{su}(2)}$, so $\theta_e(v) = v$. Listing the six permutations with their signs,
> $$\operatorname{tr}(\theta^3)_e(X,Y,Z) = \operatorname{tr}(XYZ) + \operatorname{tr}(YZX) + \operatorname{tr}(ZXY) - \operatorname{tr}(YXZ) - \operatorname{tr}(XZY) - \operatorname{tr}(ZYX).$$
> By cyclicity of the matrix trace, $\operatorname{tr}(XYZ) = \operatorname{tr}(YZX) = \operatorname{tr}(ZXY)$ and $\operatorname{tr}(YXZ) = \operatorname{tr}(XZY) = \operatorname{tr}(ZYX)$ (the second triple is the cyclic class of $\operatorname{tr}(XZY)$). Hence
> $$\operatorname{tr}(\theta^3)_e(X,Y,Z) = 3\operatorname{tr}(XYZ) - 3\operatorname{tr}(XZY) = 3\operatorname{tr}\big(X(YZ - ZY)\big) = 3\operatorname{tr}(X[Y,Z]) \qquad \text{(cyclicity, then }[Y,Z] = YZ-ZY\text{).}$$

**Step 2: Evaluate the constant on the basis $(E_1, E_2, E_3)$.**

$\operatorname{tr}(\theta^3)_e(E_1, E_2, E_3) = -12$.

> [!note]- Derivation
> The Pauli matrices satisfy $\sigma_a\sigma_b = \delta_{ab}I + \mathrm{i}\varepsilon_{abc}\sigma_c$ (a direct check on the three matrices, with $\varepsilon_{abc}$ the totally antisymmetric symbol, $\varepsilon_{123} = +1$). With $E_a = -\mathrm{i}\sigma_a$,
> $$[E_a, E_b] = (-\mathrm{i})^2[\sigma_a, \sigma_b] = -[\sigma_a, \sigma_b] = -\big(2\mathrm{i}\varepsilon_{abc}\sigma_c\big) = 2\varepsilon_{abc}(-\mathrm{i}\sigma_c) = 2\varepsilon_{abc}E_c \qquad \text{(}[\sigma_a,\sigma_b] = 2\mathrm{i}\varepsilon_{abc}\sigma_c\text{ from the Pauli products),}$$
> and
> $$\operatorname{tr}(E_aE_b) = (-\mathrm{i})^2\operatorname{tr}(\sigma_a\sigma_b) = -\operatorname{tr}(\delta_{ab}I + \mathrm{i}\varepsilon_{abc}\sigma_c) = -\big(2\delta_{ab} + \mathrm{i}\varepsilon_{abc}\cdot 0\big) = -2\delta_{ab} \qquad \text{(}\operatorname{tr}I = 2,\ \operatorname{tr}\sigma_c = 0\text{).}$$
> Now apply Step 1 with $(X,Y,Z) = (E_1, E_2, E_3)$. Since $[E_2, E_3] = 2\varepsilon_{23c}E_c = 2E_1$ (only $\varepsilon_{231} = +1$ contributes),
> $$\operatorname{tr}(\theta^3)_e(E_1, E_2, E_3) = 3\operatorname{tr}(E_1[E_2, E_3]) = 3\operatorname{tr}(E_1\cdot 2E_1) = 6\operatorname{tr}(E_1^2) = 6\cdot(-2) = -12 \qquad \text{(}[E_2,E_3]=2E_1,\ \operatorname{tr}(E_1^2)=-2\text{).}$$

**Step 3: $\operatorname{tr}(\theta^3)$ is a constant multiple of the volume form, and the constant is $-12$.**

As forms on $SU(2)$, $\operatorname{tr}(\theta^3) = -12\,\mathrm{vol}_{S^3}$.

> [!note]- Derivation
> *A constant multiple.* The form $\theta$ is left-invariant, so $\theta\wedge\theta\wedge\theta$ and hence $\operatorname{tr}(\theta^3)$ are left-invariant three-forms on the three-dimensional group $SU(2)$. The space of three-forms at each point of a three-manifold is one-dimensional, and left translations act transitively on $SU(2)$; therefore a left-invariant three-form is determined by its value at $e$ and equals a *constant* multiple of any nowhere-vanishing left-invariant three-form. The Riemannian volume form $\mathrm{vol}_{S^3}$ of the bi-invariant round metric is such a form (the bi-invariant metric is in particular left-invariant, so its volume form is left-invariant). Hence $\operatorname{tr}(\theta^3) = \lambda\,\mathrm{vol}_{S^3}$ for a constant $\lambda \in \mathbb{R}$, and $\lambda$ is found by evaluating both sides on one frame at $e$.
>
> *The frame is orthonormal.* Consider the metric $\langle X, Y\rangle := -\tfrac12\operatorname{tr}(XY)$ on $\mathfrak{su}(2)$; by Step 2's trace form, $\langle E_a, E_b\rangle = -\tfrac12(-2\delta_{ab}) = \delta_{ab}$, so $(E_1, E_2, E_3)$ is orthonormal for it. To see that this is the round metric of radius $1$, compute the images of the $E_a$ in $\mathbb{H} = \mathbb{R}^4$ under $SU(2) \cong Sp(1)$. Each $E_a$ satisfies $E_a^2 = (-\mathrm{i}\sigma_a)^2 = -\sigma_a^2 = -I$, so the one-parameter subgroup is $\exp(tE_a) = \cos t\, I + \sin t\, E_a$. Reading off the entries against the quaternionic identification $q = a + b\mathrm{i} + c\mathrm{j} + d\mathrm{k} \leftrightarrow \left(\begin{smallmatrix} a+b\mathrm{i} & c+d\mathrm{i} \\ -c+d\mathrm{i} & a-b\mathrm{i}\end{smallmatrix}\right)$:
> $$\exp(tE_1) = \begin{pmatrix} \cos t & -\mathrm{i}\sin t \\ -\mathrm{i}\sin t & \cos t \end{pmatrix} \leftrightarrow (\cos t,\, 0,\, 0,\, -\sin t),\qquad \tfrac{d}{dt}\big|_0 \leftrightarrow (0,0,0,-1) = -\mathrm{k};$$
> $$\exp(tE_2) = \begin{pmatrix} \cos t & -\sin t \\ \sin t & \cos t \end{pmatrix} \leftrightarrow (\cos t,\, 0,\, -\sin t,\, 0),\qquad \tfrac{d}{dt}\big|_0 \leftrightarrow (0,0,-1,0) = -\mathrm{j};$$
> $$\exp(tE_3) = \begin{pmatrix} e^{-\mathrm{i}t} & 0 \\ 0 & e^{\mathrm{i}t} \end{pmatrix} \leftrightarrow (\cos t,\, -\sin t,\, 0,\, 0),\qquad \tfrac{d}{dt}\big|_0 \leftrightarrow (0,-1,0,0) = -\mathrm{i}.$$
> Thus $(E_1, E_2, E_3) \leftrightarrow (-\mathrm{k}, -\mathrm{j}, -\mathrm{i})$, three unit vectors of $\operatorname{Im}\mathbb{H}$, mutually orthogonal in the Euclidean metric of $\mathbb{R}^4$. So $(E_1, E_2, E_3)$ is orthonormal for the round metric of radius $1$ (the restriction of the Euclidean metric), confirming that $\langle\cdot,\cdot\rangle$ is that metric.
>
> *The frame is positively oriented.* Under the $\partial B^4$ orientation, $(v_1, v_2, v_3)$ is positive at $p = 1$ if and only if $(1, v_1, v_2, v_3)$ is positive in $\mathbb{R}^4$ oriented by $(1, \mathrm{i}, \mathrm{j}, \mathrm{k})$. The change-of-basis matrix from $(\mathrm{i}, \mathrm{j}, \mathrm{k})$ to $(E_1, E_2, E_3) = (-\mathrm{k}, -\mathrm{j}, -\mathrm{i})$ has columns $(-\mathrm{k}, -\mathrm{j}, -\mathrm{i})$,
> $$M = \begin{pmatrix} 0 & 0 & -1 \\ 0 & -1 & 0 \\ -1 & 0 & 0 \end{pmatrix},\qquad \det M = (-1)\cdot\big(\!-\!\det\begin{pmatrix} 0 & -1 \\ -1 & 0\end{pmatrix}\big) = (-1)(-(-1)) = +1,$$
> so $(1, E_1, E_2, E_3)$ and $(1, \mathrm{i}, \mathrm{j}, \mathrm{k})$ define the same orientation of $\mathbb{R}^4$: $(E_1, E_2, E_3)$ is a *positively oriented orthonormal* frame of $T_eS^3$.
>
> *The constant.* By the characterisation of the [[Def - Riemannian Volume Form|volume form]], $\mathrm{vol}_{S^3}(E_1, E_2, E_3) = +1$ on this oriented orthonormal frame. Evaluating $\operatorname{tr}(\theta^3) = \lambda\,\mathrm{vol}_{S^3}$ at $e$ on the frame and using Step 2,
> $$-12 = \operatorname{tr}(\theta^3)_e(E_1, E_2, E_3) = \lambda\,\mathrm{vol}_{S^3}(E_1, E_2, E_3) = \lambda\cdot(+1),\qquad\text{so}\qquad \lambda = -12.$$
> Therefore $\operatorname{tr}(\theta^3) = -12\,\mathrm{vol}_{S^3}$ as forms on $SU(2)$.

**Step 4: Integrate over $SU(2)$.**

$\displaystyle\int_{SU(2)}\operatorname{tr}(\theta^3) = -24\pi^2$.

> [!note]- Derivation
> Integrating the form identity of Step 3 over $SU(2)$ with the boundary orientation, and using that the volume form integrates to the total volume,
> $$\int_{SU(2)}\operatorname{tr}(\theta^3) = -12\int_{S^3}\mathrm{vol}_{S^3} = -12\,\operatorname{Vol}(S^3) = -12\cdot 2\pi^2 = -24\pi^2 \qquad \text{(Step 3; }\operatorname{Vol}(S^3) = 2\pi^2\text{ from }[[Ex - Volume of the n-Sphere via the Volume Form|the sphere-volume page]]\text{).}$$

**Step 5: Transfer to a general map by the degree.**

For every smooth $g\colon S^3 \to SU(2)$, $\displaystyle\int_{S^3}\operatorname{tr}((g^{-1}dg)^3) = -24\pi^2\deg g$, and $W(g) = -\deg g$.

> [!note]- Derivation
> Since $g^*\theta = g^{-1}dg$ and pull-back commutes with the wedge and the trace, $g^*\operatorname{tr}(\theta^3) = \operatorname{tr}((g^{-1}dg)^3)$. The three-form $\operatorname{tr}(\theta^3) = -12\,\mathrm{vol}_{S^3}$ is a constant multiple of the volume form; normalising $\omega := \tfrac{1}{-24\pi^2}\operatorname{tr}(\theta^3)$ gives $\int_{SU(2)}\omega = 1$, so by the definition of the [[Thm - The Brouwer Degree is an Integer and a Homotopy Invariant|Brouwer degree]] as $\deg g = \int_{S^3}g^*\omega$ for a normalised top-form $\omega$,
> $$\int_{S^3}\operatorname{tr}((g^{-1}dg)^3) = \int_{S^3}g^*\operatorname{tr}(\theta^3) = -24\pi^2\int_{S^3}g^*\omega = -24\pi^2\deg g \qquad \text{(degree of }g\text{ against the normalised }\omega\text{).}$$
> Dividing by $24\pi^2$, $W(g) = \tfrac{1}{24\pi^2}\int_{S^3}\operatorname{tr}((g^{-1}dg)^3) = -\deg g$.

> [!note]- Complete formal solution
> **Claim.** $\int_{SU(2)}\operatorname{tr}(\theta\wedge\theta\wedge\theta) = -24\pi^2$, with $SU(2) \cong S^3 = \partial B^4$ oriented outward-normal-first and metrised by the round radius-$1$ metric; consequently $W(g) = -\deg g$.
>
> *Bracket reduction.* Expanding $(\theta\wedge\theta\wedge\theta)(X,Y,Z)$ over $S_3$, taking the trace, and using cyclicity of the matrix trace gives $\operatorname{tr}(\theta^3)_e(X,Y,Z) = 3\operatorname{tr}(XYZ) - 3\operatorname{tr}(XZY) = 3\operatorname{tr}(X[Y,Z])$, using $\theta_e = \operatorname{id}$.
>
> *The constant at $e$.* With $E_a = -\mathrm{i}\sigma_a$, the Pauli products give $[E_a,E_b] = 2\varepsilon_{abc}E_c$ and $\operatorname{tr}(E_aE_b) = -2\delta_{ab}$; hence $\operatorname{tr}(\theta^3)_e(E_1,E_2,E_3) = 3\operatorname{tr}(E_1\cdot 2E_1) = 6\operatorname{tr}(E_1^2) = -12$.
>
> *Identification with the volume form.* $\operatorname{tr}(\theta^3)$ is left-invariant (as $\theta$ is), hence a constant multiple $\lambda\,\mathrm{vol}_{S^3}$ of the bi-invariant volume form. The metric $\langle X,Y\rangle = -\tfrac12\operatorname{tr}(XY)$ makes $(E_1,E_2,E_3)$ orthonormal; computing $\exp(tE_a)$ and mapping to $\mathbb{H}$ gives $(E_1,E_2,E_3) \leftrightarrow (-\mathrm{k},-\mathrm{j},-\mathrm{i})$, unit and orthogonal (so the metric is the round radius-$1$ metric) with change-of-basis determinant $+1$ against $(\mathrm{i},\mathrm{j},\mathrm{k})$, so the frame is positively oriented under the $\partial B^4$ convention. Thus $\mathrm{vol}_{S^3}(E_1,E_2,E_3) = +1$ and $\lambda = -12$: $\operatorname{tr}(\theta^3) = -12\,\mathrm{vol}_{S^3}$.
>
> *Integral.* $\int_{SU(2)}\operatorname{tr}(\theta^3) = -12\operatorname{Vol}(S^3) = -12\cdot 2\pi^2 = -24\pi^2$.
>
> *General map.* With $\omega = \tfrac{-1}{24\pi^2}\operatorname{tr}(\theta^3)$ satisfying $\int_{SU(2)}\omega = 1$, $\int_{S^3}\operatorname{tr}((g^{-1}dg)^3) = -24\pi^2\int_{S^3}g^*\omega = -24\pi^2\deg g$, so $W(g) = -\deg g$. $\blacksquare$

> [!warning] Illegal but tempting shortcut: fixing the sign by "$W(\mathrm{id}) = 1$" instead of by the orientation
> It is tempting to declare $W(g) = +\deg g$ because "the identity map has degree $1$." But the identity map $\mathrm{id}\colon S^3 \to SU(2)$ has $W(\mathrm{id}) = \tfrac{1}{24\pi^2}\int_{SU(2)}\operatorname{tr}(\theta^3) = \tfrac{-24\pi^2}{24\pi^2} = -1$, which is *minus* its degree. The sign is not free: once the orientation of $SU(2) \cong S^3$ is fixed (here $\partial B^4$, outward-normal-first), the sign of $\int_{SU(2)}\operatorname{tr}(\theta^3)$ is determined, and it comes out negative. Assuming the opposite sign would make the Chern–Simons functional *decrease* under a positive-degree gauge transformation and would put the Chern number of the quaternionic Hopf bundle on the wrong side; the [[Def - The Hopf Bundle#Sign ledger|sign ledger]] records $\int_{SU(2)}\operatorname{tr}(\theta^3) = -24\pi^2$ and $W(g) = -\deg g$ precisely to prevent this slip across the four sign-sensitive pages of the series.

**Independent sanity check (bi-invariance).** The constant should not depend on which orthonormal frame at $e$ we chose, only on the orientation. Replacing $(E_1, E_2, E_3)$ by any other positively oriented orthonormal frame $(E_1', E_2', E_3') = (E_1, E_2, E_3)R$ with $R \in SO(3)$ multiplies both $\operatorname{tr}(\theta^3)_e$ and $\mathrm{vol}_{S^3}$ by $\det R = +1$, so the ratio $\lambda = -12$ is unchanged; an orientation-reversing $R \in O(3) \setminus SO(3)$ would multiply both by $-1$, again leaving $\lambda$ fixed but flipping the reported sign of the integral if we also reversed the orientation of $S^3$ — consistent with the observation that the answer's sign is exactly the orientation datum. This confirms that $-12$ is intrinsic to the bi-invariant form and the chosen orientation, not an artefact of the particular Pauli basis.

---

# Key Takeaways

**A bi-invariant top-degree form on a compact Lie group is a constant multiple of the volume form, and the constant is one evaluation at the identity.** This is the structural fact the whole exercise turns on, and it recurs whenever one integrates an invariant density over a group: the global integral collapses to a pointwise Lie-algebra computation because invariance forbids the density from varying across the group. The reusable procedure is (i) confirm invariance, (ii) evaluate on one frame at $e$, (iii) compare to the volume form on the *same* frame. The trigger is "an integral over a compact group of a form built naturally from $\theta$"; the reaction is "reduce to the identity." The same mechanism computes the volumes of $SU(n)$ and the total integrals of the higher bi-invariant forms $\operatorname{tr}(\theta^{2k+1})$ that give the primitive generators of $H^*(G;\mathbb{R})$, and it is the reason the winding number $W(g)$ is an integer at all — it is a degree, hence the integral of a normalised invariant form.

**The magnitude of an oriented-volume constant is algebra; the sign is geometry, and the two must be checked separately.** The number $12$ came entirely from the brackets and trace form of $\mathfrak{su}(2)$; the sign came entirely from the orientation of $S^3$, verified by a determinant computation in the quaternionic model. Conflating them — assuming, say, that a positively oriented answer must carry a positive sign — is the single most common error in this kind of computation, and it is exactly the error the series' [[Def - The Hopf Bundle#Sign ledger|sign ledger]] exists to forestall. The diagnostic for spaced practice: whenever a computation produces a signed geometric constant, ask separately "what is its absolute value?" (a metric-and-algebra question) and "what is its sign?" (an orientation question), and answer the second by exhibiting an explicitly oriented frame. Here the sign check is the determinant $+1$ of the frame $(-\mathrm{k}, -\mathrm{j}, -\mathrm{i})$; forget it and the answer flips to $+24\pi^2$.

**This constant is the exchange rate between topology and analysis for $SU(2)$-gauge theory.** The value $\int_{SU(2)}\operatorname{tr}(\theta^3) = -24\pi^2$ is what converts a topological integer — the degree of a gauge transformation, or the clutching degree of a bundle — into an integral of a differential form, and back. It is the constant in $W(g) = -\deg g$ used in [[Thm - Classification of Principal SU(2)-Bundles over Four-Manifolds|the classification of SU(2)-bundles over four-manifolds]] (its part 3), the constant that makes the Chern number $\tfrac{1}{8\pi^2}\int_X\operatorname{tr}(F_A\wedge F_A)$ an integer, and the constant that makes the [[Def - Chern-Simons Functional|Chern–Simons functional]] well defined modulo the integers rather than modulo some other lattice. Whenever a factor of $24\pi^2$, or of $8\pi^2$, appears in these notes, it traces back to this single computation; recognising it as "the volume of $SU(2)$ measured by $\operatorname{tr}(\theta^3)$" is what makes those normalisations memorable rather than arbitrary. This exercise pairs with [[Ex - Well-Definedness of the Chern-Simons Functional under Change of Trivialisation]], which uses $W(g) = -\deg g$ to show $\vartheta$ shifts by an integer, and with [[Ex - The Chern-Simons Form Transgresses the Second Chern Form]], which supplies the companion identity $d\operatorname{cs}(A) = \operatorname{tr}(F_A\wedge F_A)$.
