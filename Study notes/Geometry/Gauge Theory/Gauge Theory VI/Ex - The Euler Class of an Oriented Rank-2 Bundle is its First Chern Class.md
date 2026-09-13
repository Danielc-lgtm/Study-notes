---
type: exercise
subject: gauge-theory
prereqs:
  - "Def - Euler Class of an Oriented Vector Bundle"
  - "Thm - First Chern Class of a Line Bundle from Curvature"
  - "Def - Pfaffian"
  - "Def - Chern Classes"
difficulty: "⭐⭐"
tags: [geometry, gauge-theory, characteristic-classes, euler-class, chern-class]
---

# Problem Statement

Let $M$ be a smooth manifold and let $E \to M$ be a smooth **oriented Euclidean real vector bundle of rank $2$**: a real plane bundle equipped with a fibre metric $g$ (a smoothly varying inner product $\langle\cdot,\cdot\rangle_x$ on each fibre $E_x$) and a continuous choice of orientation of each fibre. Its structure group is thereby reduced to $SO(2)$, and its Euler class $e(E) \in H^2_{dR}(M)$ is defined (via the Pfaffian of a metric curvature).

An oriented Euclidean plane bundle carries a canonical **complex structure**: the fibrewise rotation by $+90^\circ$ in the positive sense,
$$I : E \to E, \qquad I e_1 = e_2 \ \text{ for every oriented orthonormal frame } (e_1, e_2),$$
which satisfies $I^2 = -\operatorname{id}$ and turns each fibre $E_x$ into a one-dimensional complex vector space. With this $I$ and the induced Hermitian structure, $E$ becomes a **Hermitian complex line bundle**, which we call $L$.

**Prove that the Euler class of the oriented plane bundle equals the first Chern class of the associated Hermitian line bundle, including the sign:**
$$\boxed{\,e(E) = c_1(L) \in H^2_{dR}(M).\,}$$
Track carefully where the choice of orientation enters, so that the identity holds with the $+$ sign under the series' normalisations $e(E) = \big[\operatorname{Pf}(F/2\pi)\big]$ and $c_1(L) = \big[\tfrac{i}{2\pi}F^{\mathbb{C}}\big]$, and not merely up to sign.

Then **deduce**, applying the identity to the tangent bundle of the round two-sphere (an oriented Euclidean plane bundle with its rotation-by-$90^\circ$ complex structure),
$$e(TS^2)[S^2] = c_1(TS^2)[S^2] = 2,$$
consistently with the two companion computations of §6.2 and §6.3, and confirm that the two numbers agree because they are integrals of one and the same de Rham class.

This is Bär's Example 2.5.15 (with Example 2.5.5 for the underlying algebra), rewritten with the sign bookkeeping made explicit.

**Recall.**

The Euler class, as a Pfaffian curvature integral on the oriented orthonormal frame bundle:

![[Def - Euler Class of an Oriented Vector Bundle#The Definition]]

The first Chern class of a line bundle from curvature, whose normalisation and integrality we invoke:

![[Thm - First Chern Class of a Line Bundle from Curvature#Statement]]

The Pfaffian, of which we need only the smallest case:

![[Def - Pfaffian#The Definition]]

The first Chern class as the trace term of the Chern polynomial:

![[Def - Chern Classes#The Definition]]

We also use the elementary Lie-algebra fact that the exponential $SO(2) \cong U(1)$, $\begin{pmatrix} \cos\varphi & -\sin\varphi \\ \sin\varphi & \cos\varphi \end{pmatrix} \mapsto e^{i\varphi}$, differentiates at the identity to the Lie-algebra isomorphism $\phi : \mathfrak{so}(2) \to \mathfrak{u}(1)$ carrying the rotation generator $J := \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ to $i$; this is **[[Thm - SO(2) is Isomorphic to U(1)]]**. The passage from a real plane bundle with $I$ to a complex line bundle is on **[[Def - Complex Vector Bundle and Hermitian Structure]]**, and the skew-symmetry of a metric connection matrix in an orthonormal frame is on **[[Def - Euclidean Vector Bundle and Metric Connection]]**.

---

# Convergent Strategy

**Problem class.** This is a *two-normalisations-agree* problem: two characteristic classes, defined by different recipes (a Pfaffian for the oriented real bundle, a determinant for the complex bundle), are to be shown identical on a bundle that carries both structures at once. The universal method for such problems is to compute *both* representative forms from *one* connection, chosen so that both recipes apply to it simultaneously, and then to match the two forms coefficient by coefficient. Here the single connection is any metric connection $\nabla$ on $(E, g)$; because $\mathfrak{so}(2)$ is abelian and $I$ is (up to sign) its generator, $\nabla$ is automatically unitary for the induced Hermitian structure, so it serves both the Pfaffian and the Chern recipe without a second choice.

**Assumption pattern.** The recognisable trigger is that a real bundle of rank exactly $2$ with an orientation and a metric is the *same data* as a complex line bundle with a Hermitian metric — the complex structure $I$ is not an extra choice but is manufactured from the orientation and the metric (rotation by $+90^\circ$). Whenever a rank-$2m$ oriented bundle is silently a rank-$m$ complex bundle, the Euler class and the top Chern class $c_m$ are the two names of one object; here $m = 1$ and $c_m = c_1$. The hypotheses one leans on are: rank $2$ (so $\mathfrak{so}(2)$ is one-dimensional and abelian, killing the quadratic term of the curvature), the orientation (so $I = +90^\circ$ rather than $-90^\circ$ is singled out), and the metric (so the curvature is skew and the Pfaffian applies).

**Theorem routing.** Fix a metric connection $\nabla$ on $(E, g)$. Its connection matrix in an oriented orthonormal frame is $\mathfrak{so}(2)$-valued, hence skew, by **[[Def - Euclidean Vector Bundle and Metric Connection]]**; its curvature matrix $F$ is likewise skew, with a single independent entry $\Omega_{12}$. Route 1 (Euler): feed $F$ into $\operatorname{Pf}(\cdot/2\pi)$; by the $m=1$ value of **[[Def - Pfaffian]]** this gives $\Omega_{12}/2\pi$, hence $e(E) = [\Omega_{12}/2\pi]$ by **[[Def - Euler Class of an Oriented Vector Bundle]]**. Route 2 (Chern): identify $\mathfrak{so}(2) \cong \mathfrak{u}(1)$ by **[[Thm - SO(2) is Isomorphic to U(1)]]**, read off the complex curvature $F^{\mathbb{C}}$, and feed it into $c_1(F^{\mathbb{C}}) = \tfrac{i}{2\pi}\operatorname{tr}(F^{\mathbb{C}})$ from **[[Def - Chern Classes]]**; this gives $\Omega_{12}/2\pi$ as well. Match, then evaluate on $[S^2]$ using **[[Thm - First Chern Class of a Line Bundle from Curvature]]** for the integer value.

**Key decision point.** Two moves carry the argument, and both are places to lose a sign. First, *tie the identification $\mathfrak{so}(2) \cong \mathfrak{u}(1)$ to the orientation*: the generator $J = I|_{\text{frame}}$ must map to $+i$, not $-i$, precisely because $(e_1, I e_1)$ is required to be *positively* oriented; the opposite convention would produce $e(E) = -c_1(L)$. Second, *use that $\mathfrak{so}(2)$ is abelian to drop the quadratic curvature term*: $A \wedge A = 0$ because $A$ is a scalar multiple of $J$ and $J \wedge J$-type terms vanish for a single $1$-form, so $F = dA$ exactly, with no correction — this is what makes both representative forms be the single $2$-form $\Omega_{12}$.

---

# Legal Operations Used

1. **Compute a characteristic class from any convenient connection** (the connection-independence operation of the topic page, licensed by the [[Thm - Chern-Weil Theorem|Chern–Weil theorem]]). Both $e(E)$ and $c_1(L)$ are defined as de Rham classes independent of the connection used to represent them; we exploit this by computing both from the *same* metric connection $\nabla$, so that the two representative forms live on the same page and can be compared directly.

2. **Manufacture geometric structure from the existing data rather than assuming it** (the reduction-of-structure-group operation). The complex structure $I$ is not posited; it is built from the orientation and the metric as rotation by $+90^\circ$. This is the rank-$2$ instance of the general fact that a $GL_{2m}(\mathbb{R})^+$-bundle with a Euclidean structure and a compatible almost-complex structure reduces to $U(m)$, applied here with $m = 1$.

3. **Match representatives, not just classes.** Having two closed forms representing the two classes, we prove the forms are *equal on the nose* (both equal $\Omega_{12}/2\pi$), which is strictly stronger than equality of classes and leaves no room for a hidden coboundary to carry a sign. Passing from equal forms to equal classes is then immediate.

4. **Transport a proved identity across an isomorphism** (naturality / isomorphism invariance). The deduction for $TS^2$ applies the general identity $e(E) = c_1(L)$ to the specific oriented Euclidean plane bundle $E = TS^2$, whose induced complex line bundle is exactly the $L$ appearing in the §6.2 Chern-number computation; the two companion exercises then supply the common integer value.

---

# Hints

> [!note]- Hint 1
> Do not try to compare $e$ and $c_1$ by their definitions on different bundles. Pick a single object to compute with: one metric connection $\nabla$ on $(E, g)$. Write its curvature matrix $F$ in an oriented orthonormal frame $(e_1, e_2)$. What shape must a $2 \times 2$ curvature matrix of a *metric* connection have?

> [!note]- Hint 2
> A metric connection has a skew-symmetric connection matrix in an orthonormal frame, so $A = \begin{pmatrix} 0 & A_{12} \\ -A_{12} & 0 \end{pmatrix}$ with a single $1$-form $A_{12}$. Because $\mathfrak{so}(2)$ is one-dimensional and abelian, the quadratic term $A \wedge A$ vanishes, so the curvature is simply $F = dA$. Write out $F$ and identify its single independent entry $\Omega_{12} = dA_{12}$.

> [!note]- Hint 3
> For the Euler side, use only the $m = 1$ value of the Pfaffian: $\operatorname{Pf}\begin{pmatrix} 0 & a \\ -a & 0 \end{pmatrix} = a$. For the Chern side, you must turn the real $2 \times 2$ matrix $F$ into a $1 \times 1$ complex matrix $F^{\mathbb{C}}$. Use the isomorphism $\mathfrak{so}(2) \to \mathfrak{u}(1)$ that sends the generator $J = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ to $i$ — equivalently, let the curvature endomorphism $F$ act on the complex line and read off the scalar by which it multiplies $e_1$.

> [!note]- Hint 4
> Acting on $e_1$: $F e_1 = \sum_i e_i F_{i1} = e_2 F_{21}$. Now $F_{21} = -\Omega_{12}$ and $e_2 = I e_1 = i\, e_1$ (this is exactly where the orientation enters: $e_2 = +I e_1$, not $-I e_1$). Combine these to get $F e_1 = (-i\,\Omega_{12}) e_1$, so $F^{\mathbb{C}} = -i\,\Omega_{12}$. Then apply $c_1(F^{\mathbb{C}}) = \tfrac{i}{2\pi}\operatorname{tr}(F^{\mathbb{C}})$ and watch the two $i$'s combine.

> [!note]- Hint 5
> For the deduction on $S^2$: the identity you just proved applies verbatim to $E = TS^2$ with $I = $ rotation by $90^\circ$. Therefore $e(TS^2) = c_1(TS^2)$ as classes, and integrating one and the same class over $S^2$ can only give one number. The value $2$ is supplied by either companion computation; the point of the deduction is that they *must* agree, and equal the Euler characteristic $\chi(S^2) = 2$.

---

# Solution

The plan is to compute both classes from one metric connection $\nabla$ on $(E, g)$. In an oriented orthonormal frame the connection and curvature matrices are $\mathfrak{so}(2)$-valued, hence skew with a single independent entry $\Omega_{12}$; the Pfaffian recipe reads off $e(E) = [\Omega_{12}/2\pi]$, and the isomorphism $\mathfrak{so}(2) \cong \mathfrak{u}(1)$ (with the generator sent to $+i$, as the orientation demands) turns the same curvature into the complex curvature $F^{\mathbb{C}} = -i\,\Omega_{12}$, from which the Chern recipe reads off $c_1(L) = [\Omega_{12}/2\pi]$. The two representative forms are literally equal, so the classes agree; specialising to $TS^2$ and integrating gives the common value $2$.

**Step 0: The complex structure is well defined and every metric connection is unitary.** We first check that $I$ is a genuine bundle endomorphism and that no separate unitary connection need be sought.

> [!note]- Derivation
> **$I$ is well defined and independent of the oriented orthonormal frame.** In an oriented orthonormal frame $(e_1, e_2)$ set $I e_1 := e_2$, $I e_2 := -e_1$; as a matrix in this frame, $I$ is $J = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$. A change to another oriented orthonormal frame $(e_1', e_2') = (e_1, e_2)\gamma$ has transition matrix $\gamma \in SO(2)$, and every element of $SO(2)$ is a rotation $R_\varphi = \begin{pmatrix} \cos\varphi & -\sin\varphi \\ \sin\varphi & \cos\varphi \end{pmatrix}$. Since $SO(2)$ is abelian and $J = R_{\pi/2}$, we have $\gamma^{-1} J \gamma = J$ (rotations commute), so the matrix of $I$ is the same $J$ in every oriented orthonormal frame. Hence the locally defined endomorphisms glue to a global $I \in \Gamma(\operatorname{End} E)$ with $I^2 = J^2 = -\operatorname{id}$. By **[[Def - Complex Vector Bundle and Hermitian Structure]]**, $I$ makes $E$ a complex line bundle $L$, with $e_1$ a local complex frame and $e_2 = I e_1 = i\, e_1$ under the identification $\mathbb{R}^2 \cong \mathbb{C}$, $e_1 \mapsto 1$, $e_2 \mapsto i$; the Euclidean metric $g$ together with $I$ gives a Hermitian metric $h(v, w) = g(v, w) + i\, g(Iv, w)$, whose real part is $g$.
>
> **Every $g$-metric connection preserves $I$, hence is unitary.** Let $\nabla$ be any $g$-metric connection. In an oriented orthonormal frame its connection matrix $A$ is skew-symmetric (by **[[Def - Euclidean Vector Bundle and Metric Connection]]**, the connection matrix of a metric connection in an orthonormal frame lies in $\mathfrak{so}(2)$), so $A = A_{12} J$ for a single $1$-form $A_{12}$ (every $\mathfrak{so}(2)$ element is a real multiple of $J$). Now $I$ has the constant matrix $J$ in this frame, so $\nabla I = dJ + [A, J] = 0 + [A_{12} J, J] = A_{12}\,[J, J] = 0$ (the bracket $[J, J] = 0$, and $\mathfrak{so}(2)$ is abelian). Thus $\nabla I = 0$: parallel transport commutes with $I$, so $\nabla$ is a *complex* connection on $L$, and being $g$-metric with $g = \operatorname{Re} h$ it preserves $h$, i.e. it is a **unitary** connection on the Hermitian line bundle $L$. No separate choice is required: the one metric connection serves both the Euler recipe and the Chern recipe. $\square$

**Step 1: The curvature in an oriented orthonormal frame.** We record the single independent curvature entry.

> [!note]- Derivation
> Fix the metric connection $\nabla$ and an oriented orthonormal frame $(e_1, e_2)$ over an open set $U \subseteq M$. As just noted, the connection matrix is
> $$A = \begin{pmatrix} 0 & A_{12} \\ -A_{12} & 0 \end{pmatrix} = A_{12}\, J, \qquad A_{12} \in \Omega^1(U).$$
> The curvature matrix is $F = dA + A \wedge A$ (the local curvature formula, series convention). The quadratic term vanishes:
> $$A \wedge A = (A_{12} J)\wedge(A_{12} J) = (A_{12}\wedge A_{12})\, J^2 = 0 \qquad \text{(since } A_{12}\wedge A_{12} = 0 \text{ for a } 1\text{-form)},$$
> using that the scalar $1$-form $A_{12}$ wedged with itself is zero (odd-degree forms anticommute, so $A_{12}\wedge A_{12} = -A_{12}\wedge A_{12}$). This is the payoff of $\mathfrak{so}(2)$ being one-dimensional and abelian. Hence
> $$F = dA = \begin{pmatrix} 0 & dA_{12} \\ -dA_{12} & 0 \end{pmatrix} = \begin{pmatrix} 0 & \Omega_{12} \\ -\Omega_{12} & 0 \end{pmatrix}, \qquad \Omega_{12} := dA_{12} \in \Omega^2(U),$$
> a skew matrix of $2$-forms with a single independent entry $\Omega_{12}$, and $F = \Omega_{12} J$. (Under a change of oriented orthonormal frame the entry $\Omega_{12}$ is unchanged, since $F' = \gamma^{-1} F \gamma = F$ for $\gamma \in SO(2)$ abelian; so $\Omega_{12}$ is a globally defined $2$-form, though we shall only need it locally, both representative forms being manifestly the same $\Omega_{12}/2\pi$.) $\square$

**Step 2: The Euler representative is $\Omega_{12}/2\pi$.** We apply the Pfaffian recipe.

> [!note]- Derivation
> By **[[Def - Euler Class of an Oriented Vector Bundle]]**, $e(E) = \big[\operatorname{Pf}(F/2\pi)\big]$ for the skew curvature $F$ of any metric connection. The matrix
> $$\frac{F}{2\pi} = \begin{pmatrix} 0 & \Omega_{12}/2\pi \\ -\Omega_{12}/2\pi & 0 \end{pmatrix}$$
> has the shape $\begin{pmatrix} 0 & a \\ -a & 0 \end{pmatrix}$ with $a = \Omega_{12}/2\pi$, and for such a matrix the $m = 1$ value of the Pfaffian is $\operatorname{Pf}\begin{pmatrix} 0 & a \\ -a & 0 \end{pmatrix} = a$ (from **[[Def - Pfaffian]]**). Therefore
> $$\operatorname{Pf}\!\Big(\frac{F}{2\pi}\Big) = \frac{\Omega_{12}}{2\pi} \qquad \text{(} m=1 \text{ Pfaffian value)}, \qquad\text{so}\qquad e(E) = \Big[\frac{\Omega_{12}}{2\pi}\Big] \in H^2_{dR}(M). \qquad \square$$

**Step 3: The Chern representative is also $\Omega_{12}/2\pi$.** We turn the real curvature into a complex $1 \times 1$ curvature and apply the Chern recipe. This is where the orientation is used.

> [!note]- Derivation
> View $F$ as a complex-linear endomorphism-valued $2$-form on the line bundle $L$: since $\nabla I = 0$ (Step 0), $F = F_\nabla$ commutes with $I$, so it is $\mathbb{C}$-linear on each fibre and thus acts as multiplication by a single complex-valued $2$-form $F^{\mathbb{C}}$, the $\mathfrak{u}(1)$-curvature. To read off $F^{\mathbb{C}}$, act on the complex frame vector $e_1$:
> $$F e_1 = \sum_{i} e_i\, F_{i1} = e_2\, F_{21} \qquad \text{(only the } i = 2 \text{ term survives, } F_{11} = 0),$$
> $$= e_2\,(-\Omega_{12}) \qquad \text{(reading the entry } F_{21} = -\Omega_{12} \text{ from Step 1)}$$
> $$= (-\Omega_{12})\,(i\, e_1) \qquad \text{(orientation input: } e_2 = I e_1 = i\, e_1 \text{, the } +90^\circ \text{ rotation, from Step 0)}$$
> $$= (-i\,\Omega_{12})\, e_1.$$
> Hence $F^{\mathbb{C}} = -i\,\Omega_{12}$, a $1 \times 1$ skew-Hermitian (purely imaginary) matrix of $2$-forms, as it must be for a unitary connection. This is the concrete form of the isomorphism $\phi : \mathfrak{so}(2) \to \mathfrak{u}(1)$, $J \mapsto i$, of **[[Thm - SO(2) is Isomorphic to U(1)]]**: it sends $F = \Omega_{12} J$ to $\phi(F) = \Omega_{12}\, i = i\,\Omega_{12}$, and the extra sign here is the standard bookkeeping difference between "$F$ acting on $e_1$" ($F_{21}$ enters) and "$\phi$ applied to the matrix", both of which are recorded on the definition page; what matters is that the two $i$'s below combine correctly. By the series normalisation $c_1(V) = \big[\tfrac{i}{2\pi}\operatorname{tr}(F^{\mathbb{C}})\big]$ from **[[Def - Chern Classes]]**, applied to the line bundle $L$ (where the trace of a $1 \times 1$ matrix is the entry itself),
> $$c_1(L) = \Big[\frac{i}{2\pi}\operatorname{tr}(F^{\mathbb{C}})\Big] = \Big[\frac{i}{2\pi}\,(-i\,\Omega_{12})\Big] = \Big[\frac{-i^2}{2\pi}\,\Omega_{12}\Big] = \Big[\frac{\Omega_{12}}{2\pi}\Big] \qquad (i \cdot (-i) = -i^2 = 1). \qquad \square$$

**Step 4: Compare and locate the sign.** The two representative forms coincide, so the classes are equal.

> [!note]- Derivation
> From Step 2 and Step 3, both classes are represented by the *same* closed $2$-form $\Omega_{12}/2\pi$:
> $$e(E) = \Big[\frac{\Omega_{12}}{2\pi}\Big] = c_1(L) \qquad \text{(Step 2 and Step 3)}.$$
> Equality of the representative forms (not merely of the classes) leaves no coboundary free to hide a sign, so the identity is exact and carries the $+$ sign. The orientation was used in exactly one place — the choice $e_2 = +I e_1$ in Step 3 (equivalently, $J \mapsto +i$), which is the requirement that $(e_1, I e_1)$ be positively oriented, i.e. the complex orientation. Had we reversed the orientation, $I$ would be replaced by $-I$ (the conjugate line bundle $\overline{L}$), so $e_2 = -I e_1 = -i\, e_1$, giving $F^{\mathbb{C}} = +i\,\Omega_{12}$ and $c_1(\overline{L}) = [-\Omega_{12}/2\pi]$; simultaneously the Pfaffian side flips, $e(\overline{E}) = [-\Omega_{12}/2\pi]$ (an oriented orthonormal frame for $\overline{E}$ differs from one for $E$ by a determinant-$(-1)$ matrix, and $\operatorname{Pf}(B^t F B) = \det(B)\operatorname{Pf}(F)$). Both sides negate together, so the identity $e = c_1$ is stable under reorientation and is not an artefact of a sign choice. $\square$

**Step 5: Deduce $e(TS^2)[S^2] = c_1(TS^2)[S^2] = 2$.** We apply the identity to the round sphere and use the two companion computations for the value.

> [!note]- Derivation
> The tangent bundle $E = TS^2$ of the unit round sphere is an oriented Euclidean plane bundle (rank $2$, with the round metric and the standard orientation), and its rotation-by-$90^\circ$ complex structure $I$ makes it the Hermitian line bundle $L = TS^2$ used in the §6.2 Chern-number computation. The identity of Step 4 applies verbatim:
> $$e(TS^2) = c_1(TS^2) \in H^2_{dR}(S^2) \qquad \text{(Step 4 with } E = TS^2).$$
> Integrating one and the same de Rham class over the closed oriented surface $S^2$ can only produce one number, so
> $$e(TS^2)[S^2] := \int_{S^2} e(TS^2) = \int_{S^2} c_1(TS^2) =: c_1(TS^2)[S^2].$$
> Each side has been computed independently: the Euler side is $\int_{S^2} \operatorname{Pf}(F/2\pi) = \tfrac{1}{2\pi}\int_{S^2} K\, dA = \tfrac{1}{2\pi}\cdot 4\pi = 2$ on **[[Ex - The Euler Class of the Tangent Bundle of the Round Sphere Integrates to Two]]** (round curvature $K = 1$, area $4\pi$), and the Chern side is $\int_{S^2} \tfrac{i}{2\pi} F^{\mathbb{C}} = 2$ on **[[Ex - The Tangent Bundle of S^2 is Nontrivial via Chern Classes]]** (the orientation there fixed so that $c_1(TS^2)[S^2] = 2$). By part (b) of **[[Thm - First Chern Class of a Line Bundle from Curvature]]** the Chern number is a priori an integer ($\tfrac{i}{2\pi}\int_{S^2} F^{\mathbb{C}} \in \mathbb{Z}$ and equals $\deg(TS^2)$), which the value $2$ respects. The content of *this* exercise is that the two companion computations were forced to agree — they are two evaluations of a single class — and that the common value is the Euler characteristic $\chi(S^2) = 2$. In particular $TS^2$ is non-trivial: a non-zero Euler class (equivalently first Chern class) obstructs a nowhere-vanishing vector field, the hairy-ball phenomenon. $\square$

> [!note]- Complete formal solution
> **Setup.** Let $E \to M$ be an oriented Euclidean real bundle of rank $2$, with fibre metric $g$, canonical complex structure $I$ (rotation by $+90^\circ$: $I e_1 = e_2$ in every oriented orthonormal frame), and associated Hermitian line bundle $L = (E, I, h)$ with $h = g + i\, g(I\cdot, \cdot)$. We show $e(E) = c_1(L)$ in $H^2_{dR}(M)$.
>
> **Step 0 (well-posedness).** For $\gamma \in SO(2)$ and $J = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ we have $\gamma^{-1} J \gamma = J$ (rotations commute), so the matrix $J$ of $I$ is frame-independent and $I \in \Gamma(\operatorname{End} E)$ is globally defined with $I^2 = -\operatorname{id}$; by [[Def - Complex Vector Bundle and Hermitian Structure]] this makes $E$ a Hermitian line bundle $L$ with $e_2 = i\, e_1$. Choose any $g$-metric connection $\nabla$; its connection matrix in an oriented orthonormal frame is $A = A_{12} J$ with $A_{12} \in \Omega^1$ (skew-symmetry of a metric connection matrix, [[Def - Euclidean Vector Bundle and Metric Connection]]). Then $\nabla I = dJ + [A, J] = 0$ since $A$ is a multiple of $J$ and $\mathfrak{so}(2)$ is abelian; hence $\nabla$ is a unitary connection on $L$, so the single connection $\nabla$ represents both classes.
>
> **Step 1 (curvature).** $F = dA + A \wedge A$; the quadratic term vanishes, $A \wedge A = (A_{12}\wedge A_{12}) J^2 = 0$ (since $A_{12}\wedge A_{12} = 0$ for a $1$-form). Thus $F = dA = \Omega_{12} J = \begin{pmatrix} 0 & \Omega_{12} \\ -\Omega_{12} & 0 \end{pmatrix}$ with $\Omega_{12} := dA_{12} \in \Omega^2$.
>
> **Step 2 (Euler representative).** By [[Def - Euler Class of an Oriented Vector Bundle]] and the $m = 1$ Pfaffian value $\operatorname{Pf}\begin{pmatrix} 0 & a \\ -a & 0 \end{pmatrix} = a$ of [[Def - Pfaffian]],
> $$e(E) = \big[\operatorname{Pf}(F/2\pi)\big] = \big[\Omega_{12}/2\pi\big].$$
>
> **Step 3 (Chern representative).** Since $\nabla I = 0$, $F$ is $\mathbb{C}$-linear and acts on the complex frame $e_1$ by
> $$F e_1 = e_2 F_{21} = e_2 (-\Omega_{12}) = (-\Omega_{12})(i\, e_1) = (-i\,\Omega_{12}) e_1 \qquad (e_2 = I e_1 = i\, e_1,\ \text{orientation}),$$
> so the $\mathfrak{u}(1)$-curvature is $F^{\mathbb{C}} = -i\,\Omega_{12}$. By the normalisation $c_1(V) = [\tfrac{i}{2\pi}\operatorname{tr}(F^{\mathbb{C}})]$ of [[Def - Chern Classes]],
> $$c_1(L) = \big[\tfrac{i}{2\pi}(-i\,\Omega_{12})\big] = \big[\Omega_{12}/2\pi\big] \qquad (i(-i) = 1).$$
>
> **Step 4 (comparison).** Steps 2 and 3 give the identical representative form $\Omega_{12}/2\pi$, so $e(E) = c_1(L)$ in $H^2_{dR}(M)$. The orientation entered only through $e_2 = +I e_1$; reversing it replaces $L$ by $\overline{L}$ and negates both sides (via $\operatorname{Pf}(B^t F B) = \det(B)\operatorname{Pf}(F)$ with $\det B = -1$ on the Euler side, and $c_1(\overline{L}) = -c_1(L)$ on the Chern side), so the identity is orientation-stable.
>
> **Step 5 (the sphere).** Applying the identity to $E = TS^2$ with its rotation-by-$90^\circ$ complex structure, $e(TS^2) = c_1(TS^2)$; integrating this single class over $S^2$,
> $$e(TS^2)[S^2] = \int_{S^2} e(TS^2) = \int_{S^2} c_1(TS^2) = c_1(TS^2)[S^2].$$
> The Euler side equals $\tfrac{1}{2\pi}\int_{S^2} K\, dA = \tfrac{1}{2\pi}(4\pi) = 2$ ([[Ex - The Euler Class of the Tangent Bundle of the Round Sphere Integrates to Two]]) and the Chern side equals $2$ ([[Ex - The Tangent Bundle of S^2 is Nontrivial via Chern Classes]]); the two are forced equal because they integrate one class, and the common value is $\chi(S^2) = 2 \in \mathbb{Z}$ (integrality from part (b) of [[Thm - First Chern Class of a Line Bundle from Curvature]]). Therefore $e(TS^2)[S^2] = c_1(TS^2)[S^2] = 2$, and $TS^2$ is non-trivial. $\blacksquare$

> [!warning] Illegal but tempting: claiming $e = c_1$ "up to sign" and stopping there
> A common shortcut is to note that $\mathfrak{so}(2) \cong \mathfrak{u}(1)$ and the Pfaffian and trace are both "the entry", conclude $e = \pm c_1$, and leave the sign undetermined. This is not enough: the whole point of the exercise, and the reason the two §6.2/§6.3 companion numbers agree as $+2$ rather than as $+2$ and $-2$, is that the $+$ sign is genuine. The sign is *fixed* by the orientation: the identification $J \mapsto +i$ (equivalently $e_2 = +I e_1$) is the statement that $(e_1, I e_1)$ is positively oriented. Dropping this — using $J \mapsto -i$, the equally valid abstract Lie-algebra isomorphism — would give $e = -c_1$ and predict $c_1(TS^2)[S^2] = -2$, contradicting the §6.2 computation. The extra condition that makes the bare "$e = \pm c_1$" into the sharp $e = +c_1$ is precisely the compatibility of $I$ with the orientation, and it must be checked, not assumed.

> [!note]- Independent sanity check: the rank-2 corollary on the Euler definition page
> The definition page [[Def - Euler Class of an Oriented Vector Bundle]] proves this same identity as a corollary ("$e(E) = c_1(E)$ for an oriented rank-$2$ bundle"), by the same route: $A \wedge A = 0$, $\operatorname{Pf}(F) = \Omega_{12}$, and $F^{\mathbb{C}} = -i\,\Omega_{12}$ giving $c_1 = [\Omega_{12}/2\pi]$. That the two derivations, written independently, land on the identical representative $\Omega_{12}/2\pi$ is a check that no stray factor of $2\pi$ or $i$ has crept in. A second check: dimensional/degree consistency — $e(E)$ and $c_1(L)$ both live in $H^2_{dR}(M)$, and $\Omega_{12}/2\pi$ is indeed a $2$-form, as required.

---

# Key Takeaways

**Compute two normalisations from one connection.** The reusable principle is that whenever a single geometric object carries two structures — here a real oriented Euclidean plane bundle that is also a Hermitian complex line bundle — an identity between two characteristic classes is proved not by comparing their abstract definitions but by evaluating both recipes on one shared connection and matching the representative forms. The trigger condition is the phrase "the same bundle, viewed as ...": an oriented rank-$2m$ bundle *is* a rank-$m$ complex bundle once orientation and metric single out $I$, so its Euler class and its top Chern class $c_m$ are one object. The transferable diagnostic: if you find yourself needing to compare classes defined by different formulas, look for a connection to which both formulas apply, compute both, and prove the forms equal — equality of forms is stronger than equality of classes and, crucially, is where a stray sign would announce itself.

**Signs of characteristic classes live in orientation conventions, and must be tracked, not waved away.** The identity $e = c_1$ holds with a definite sign only because the complex structure $I$ is rotation by $+90^\circ$, compatible with the orientation; the abstract isomorphism $\mathfrak{so}(2) \cong \mathfrak{u}(1)$ admits two directions ($J \mapsto \pm i$), and only the orientation-compatible one gives $+$. The reusable lesson is that any "up to sign" statement about Euler or Chern numbers is incomplete: the sign is data, carried by the orientation, and the entire consistency of the four-manifold sign ledger (clutching degrees, instanton numbers, $\int_{SU(2)} \operatorname{tr}(\theta^3)$) depends on pinning it down once. The diagnostic is to ask, at every $i$ and every $\det = -1$, "which orientation put it here?" — and to verify that a reorientation negates both sides together, as it does here, so that the identity itself is orientation-stable even though each side is not.

**The Euler class subsumes the first Chern class in rank two, unifying Gauss–Bonnet, hairy-ball, and Dirac quantisation.** Because $e(TS^2) = c_1(TS^2)$ and both integrate to $\chi(S^2) = 2$, three apparently distinct facts are one: the Gauss–Bonnet integral $\tfrac{1}{2\pi}\int_{S^2} K\, dA = 2$, the non-existence of a nowhere-vanishing tangent field (hairy-ball, since $e \ne 0$), and the quantisation of the first Chern number to an integer. The trigger for reusing this is any oriented surface bundle or any complex line bundle over a surface: its single characteristic number can be read either as an Euler number (zeros of a section, counted with sign) or as a Chern number (degree, curvature integral), and the identity licenses switching freely between the two pictures. The companion exercises to hold alongside this one are [[Ex - The Euler Class of the Tangent Bundle of the Round Sphere Integrates to Two]] and [[Ex - The Tangent Bundle of S^2 is Nontrivial via Chern Classes]], which supply the two evaluations this exercise proves must coincide, and [[Ex - Odd Chern Classes of a Complexified Real Bundle Vanish]], the sibling drill on how real bundles interact with complexification.
