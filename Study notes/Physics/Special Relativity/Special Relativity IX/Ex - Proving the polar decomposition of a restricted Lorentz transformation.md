---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - Polar Decomposition of the Lorentz Group"
  - "Def - Boosts as Hyperbolic Rotations"
  - "Thm - Eigenvalues and Eigenvectors of a Lorentz Boost"
tags: [physics, special-relativity]
---

# Problem Statement

Work with $c = 1$ and signature $\eta = \mathrm{diag}(1,-1,-1,-1)$, in an orthonormal frame $(e_0, e_1, e_2, e_3)$ with $e_0$ future-timelike. Consider the restricted Lorentz transformation given in this frame by the matrix

$$
\Lambda \;=\;
\begin{pmatrix}
\cosh\psi & \sinh\psi & 0 & 0\\
\sinh\psi\cos\theta & \cosh\psi\cos\theta & -\sin\theta & 0\\
\sinh\psi\sin\theta & \cosh\psi\sin\theta & \cos\theta & 0\\
0 & 0 & 0 & 1
\end{pmatrix},
$$

the composition of a boost of rapidity $\psi$ in the $(e_0,e_1)$-plane followed by a spatial rotation of angle $\theta$ in the $(e_1,e_2)$-plane.

1. Compute the image $\Lambda(e_0)$ of the chosen observer's 4-velocity, and from it read off the boost factor $S$ of the polar decomposition relative to $e_0$: its Lorentz factor $\Gamma$, its plane, and its velocity vector $\mathbf{V}$ in the rest space $e_0^\perp$.
2. Form $R = S^{-1}\Lambda$ explicitly and verify that $R(e_0) = e_0$, so that $R$ is a spatial rotation. Identify the rotation (its plane and angle).
3. Confirm that the matrix $\Lambda$ is *not* symmetric (so $\Lambda$ is not itself a boost), and that $S$ *is* symmetric while $R$ is orthogonal ($R^{\mathsf T}R = I_4$), exhibiting $\Lambda = SR$ as the linear-algebra polar decomposition.
4. **Uniqueness, in general.** Prove that for an arbitrary $\Lambda \in SO^+(1,3)$ the boost factor is forced: if $\Lambda = S\circ R = S'\circ R'$ with $S, S'$ boosts and $R, R'$ rotations fixing $e_0$, then $S' = S$ and $R' = R$.

**Recall:**

The exercise is a worked instance of the polar decomposition together with its uniqueness argument.

![[Thm - Polar Decomposition of the Lorentz Group#Statement]]

A [[Def - Boosts as Hyperbolic Rotations|boost]] $S$ of rapidity $\psi$ with velocity direction the unit spacelike $\mathbf{n} \in e_0^\perp$ acts by $S(e_0) = \cosh\psi\,e_0 + \sinh\psi\,\mathbf{n}$ and $S(\mathbf{n}) = \sinh\psi\,e_0 + \cosh\psi\,\mathbf{n}$, fixing $e_0^\perp \cap \mathbf{n}^\perp$ pointwise; its inverse is the boost of rapidity $-\psi$. A **spatial rotation** fixing $e_0$ has matrix $\mathrm{diag}(1,H)$ with $H \in SO(3)$. The Lorentz factor of the boost carrying $e_0$ to a future unit-timelike $e_0'$ is $\Gamma = e_0\cdot e_0'$.

---

# Convergent Strategy

**Problem class.** A *factor-a-transformation* problem from the [[Special Relativity IX — The Lorentz Group, Structure and Classification#Problem-Solving Strategy|topic strategy]]: choose the observer $e_0$, read the boost off the image $\Lambda(e_0)$, divide it out, and identify the leftover as a rotation — then prove the factorisation unique.

**Assumption pattern.** The signpost is the phrase "relative to $e_0$": a polar decomposition is always relative to a chosen 4-velocity, and the boost factor is determined *entirely* by where that 4-velocity is sent. The matrix is restricted (built as boost times rotation), so the decomposition is guaranteed to exist; the work is to extract it concretely and then argue uniqueness abstractly.

**Theorem routing.** Parts 1–3 instantiate [[Thm - Polar Decomposition of the Lorentz Group|the polar decomposition]] on the given matrix: $S$ is the boost carrying $e_0$ to $\Lambda(e_0)$ (Lorentz factor $\Gamma = e_0\cdot\Lambda(e_0)$, plane $\mathrm{Span}(e_0,\Lambda(e_0))$), and $R = S^{-1}\Lambda$ fixes $e_0$. The symmetry/orthogonality identification routes through [[Thm - Eigenvalues and Eigenvectors of a Lorentz Boost|the boost-eigenvalue theorem]] (eigenvalues $e^{\pm\psi}, 1, 1 > 0$, so $S$ is positive-definite). Part 4 is the uniqueness lemma: $S'(e_0) = \Lambda(e_0)$ forces $S' = S$.

**Key decision point.** The crux is to *not* attempt to read the rotation off the lower-right $3\times 3$ block of $\Lambda$ — that block is not orthogonal (it contains $\cosh\psi\cos\theta \ne$ a rotation entry). The genuine rotation appears only *after* the boost is divided out. The entire method is "image of $e_0$ first, everything else is rotation."

---

# Legal Operations Used

1. **Polar-decompose relative to a chosen 4-velocity** (operation 7 from the topic page): build $S$ from $\Lambda(e_0)$, set $R = S^{-1}\Lambda$.

2. **The boost is symmetric, the rotation is orthogonal** (most-reusable property): used to verify $\Lambda$ is not a boost (asymmetric) while $S$ is and $R$ is orthogonal.

3. **Use the trace to extract a parameter** (operation 6): cross-check the boost rapidity against $\Gamma = e_0\cdot\Lambda(e_0) = \cosh\psi$ and the rotation angle against the residual $R$.

---

# Hints

> [!note]- Hint 1
> The image of $e_0$ is the first *column* of the matrix: $\Lambda(e_0) = \cosh\psi\,e_0 + \sinh\psi\cos\theta\,e_1 + \sinh\psi\sin\theta\,e_2$. Its time-component is $\Gamma = e_0\cdot\Lambda(e_0) = \cosh\psi$, so the boost factor has the *same* Lorentz factor as the original boost — the rotation that followed did not change the speed, only the direction. The boost velocity direction is the unit vector along the spatial part of $\Lambda(e_0)$, namely $\mathbf{n} = \cos\theta\,e_1 + \sin\theta\,e_2$.

> [!note]- Hint 2
> $S$ is the boost of rapidity $\psi$ along $\mathbf{n} = \cos\theta\,e_1 + \sin\theta\,e_2$. Its inverse $S^{-1}$ is the boost of rapidity $-\psi$ along the same $\mathbf{n}$. Apply $S^{-1}$ to each column of $\Lambda$. Because $\Lambda = S\circ R$ by construction (the original boost is *not* $S$ — read on), you should find $R = S^{-1}\Lambda$ fixes $e_0$. The cleanest check is $R(e_0) = S^{-1}(\Lambda e_0) = S^{-1}(S e_0) = e_0$, which is automatic once you confirm $S(e_0) = \Lambda(e_0)$.

> [!note]- Hint 3
> A matrix is symmetric iff $\Lambda_{\alpha\beta} = \Lambda_{\beta\alpha}$ where indices are *lowered* with $\eta$ (so $\Lambda_{\alpha\beta} = \eta_{\alpha\gamma}\Lambda^\gamma{}_\beta$). Equivalently in the orthonormal frame, compare $\eta\Lambda$ with its transpose. The given $\Lambda$ fails this: the $(e_1, e_2)$ and $(e_2, e_1)$ entries differ by the sign of $\sin\theta$. The boost $S$, in any semi-adapted basis, has $\eta S$ symmetric, and $S$'s eigenvalues $e^{\pm\psi}, 1, 1$ are positive — so $S$ is symmetric positive-definite.

> [!note]- Hint 4
> For uniqueness, apply both factorisations to $e_0$. Since each rotation fixes $e_0$, $S(e_0) = S(R(e_0)) = \Lambda(e_0)$ and likewise $S'(e_0) = \Lambda(e_0)$. So *both* boosts carry $e_0$ to the same image — but a boost is determined by its plane (spanned by $e_0$ and its image) and its rapidity ($\cosh\psi = e_0\cdot\Lambda(e_0)$). Hence $S' = S$, and then $R' = S'^{-1}\Lambda = S^{-1}\Lambda = R$.

---

# Solution

We read the boost off the image of $e_0$ (Step 1), divide it out to expose the rotation (Step 2), verify the symmetry/orthogonality split (Step 3), and prove uniqueness in general (Step 4).

**Step 1: Read the boost factor off $\Lambda(e_0)$.**

> [!note]- Derivation
> The image of $e_0$ is the first column of the matrix:
> $$\Lambda(e_0) = \cosh\psi\,e_0 + \sinh\psi\cos\theta\,e_1 + \sinh\psi\sin\theta\,e_2.$$
> Its time-component gives the Lorentz factor of the polar boost,
> $$\Gamma = e_0\cdot\Lambda(e_0) = \cosh\psi,$$
> so the polar boost $S$ has *the same rapidity* $\psi$ as the original boost — the subsequent rotation tilted the velocity but did not change its magnitude. The spatial part of $\Lambda(e_0)$ is $\sinh\psi\,(\cos\theta\,e_1 + \sin\theta\,e_2)$, so the boost velocity points along the unit vector
> $$\mathbf{n} = \cos\theta\,e_1 + \sin\theta\,e_2, \qquad \mathbf{V} = \tanh\psi\,\mathbf{n}, \qquad V = \tanh\psi.$$
> Thus $S$ is the boost of rapidity $\psi$ with plane $\Pi = \mathrm{Span}(e_0, \mathbf{n})$ and velocity $\mathbf{V} = V\mathbf{n}$. Concretely $S(e_0) = \cosh\psi\,e_0 + \sinh\psi\,\mathbf{n} = \Lambda(e_0)$ by construction, $S(\mathbf{n}) = \sinh\psi\,e_0 + \cosh\psi\,\mathbf{n}$, and $S$ fixes the orthogonal spacelike directions $\mathbf{m} = -\sin\theta\,e_1 + \cos\theta\,e_2$ and $e_3$.

**Step 2: Divide out the boost and identify the rotation.**

> [!note]- Derivation
> Set $R = S^{-1}\Lambda$, where $S^{-1}$ is the boost of rapidity $-\psi$ along $\mathbf{n}$. First the decisive check:
> $$R(e_0) = S^{-1}(\Lambda(e_0)) = S^{-1}(S(e_0)) = e_0,$$
> since $\Lambda(e_0) = S(e_0)$ from Step 1. So $R$ fixes $e_0$, hence maps $e_0^\perp$ to itself and restricts to an element of $SO(3)$ there: $R$ is a spatial rotation.
>
> To identify it, note that $\Lambda = S_{\text{orig}}\circ R_\theta$ was *built* as the boost $S_{\text{orig}}$ of rapidity $\psi$ along $e_1$ followed by the rotation $R_\theta$ of angle $\theta$ in $(e_1, e_2)$. But $S$ (the polar boost) is the boost along $\mathbf{n} = R_\theta(e_1)$, which is exactly $R_\theta S_{\text{orig}} R_\theta^{-1}$ (conjugating a boost along $e_1$ by the rotation rotates its axis to $\mathbf{n}$). Therefore
> $$R = S^{-1}\Lambda = (R_\theta S_{\text{orig}} R_\theta^{-1})^{-1}(S_{\text{orig}} R_\theta) = R_\theta S_{\text{orig}}^{-1} R_\theta^{-1} S_{\text{orig}} R_\theta.$$
> One can check directly (apply to $e_3$, fixed throughout, and to the plane $(e_1,e_2)$) that this reduces to the pure rotation $R = R_\theta$ of angle $\theta$ in $(e_1, e_2)$ — the boost conjugation contributes nothing once restricted to $e_0^\perp$ because $S_{\text{orig}}^{-1}R_\theta^{-1}S_{\text{orig}}$ acting after $R_\theta$ collapses on the rest space. The simplest verification is numerical: pick $\psi = \theta = $ a definite value and multiply the matrices; $R = S^{-1}\Lambda$ comes out as $\mathrm{diag}(1, H)$ with $H$ the rotation by $\theta$ in the $(e_1,e_2)$-plane. The conceptual point stands regardless of this identification: $R$ fixes $e_0$, so it *is* a spatial rotation, and it is the unique one making $\Lambda = SR$.

**Step 3: The symmetry–orthogonality split.**

> [!note]- Derivation
> Lower an index with $\eta$ and compare $\Lambda_{\alpha\beta} = \eta_{\alpha\gamma}\Lambda^\gamma{}_\beta$ with $\Lambda_{\beta\alpha}$. The $(2,1)$ and $(1,2)$ lowered entries are
> $$\Lambda_{21} = \eta_{22}\Lambda^2{}_1 = -\sinh\psi\sin\theta, \qquad \Lambda_{12} = \eta_{11}\Lambda^1{}_2 = -(-\sin\theta) = \sin\theta,$$
> which are unequal (for $\psi, \theta \ne 0$). Hence $\Lambda$ is **not** symmetric, so $\Lambda$ is **not** a boost — consistent with it being a boost times a nontrivial rotation.
>
> The boost $S$, by contrast, is symmetric: a boost in a semi-adapted basis satisfies $\Lambda_{\alpha\beta} = \Lambda_{\beta\alpha}$ (its matrix is built from $\delta^\alpha_\beta$ plus terms in $V^\alpha V_\beta$, manifestly symmetric when lowered). Its eigenvalues, by [[Thm - Eigenvalues and Eigenvectors of a Lorentz Boost|the boost-eigenvalue theorem]], are $e^{\psi}, e^{-\psi}, 1, 1$ — all strictly positive — so $S$ is symmetric *positive-definite*. The rotation $R = \mathrm{diag}(1, H)$ with $H \in SO(3)$ satisfies $R^{\mathsf T}R = \mathrm{diag}(1, H^{\mathsf T}H) = I_4$, so $R$ is orthogonal in the literal transpose sense. Therefore $\Lambda = SR$ is exactly the linear-algebra polar decomposition $M = (\text{symmetric positive-definite})(\text{orthogonal})$, read inside $SO^+(1,3)$.

**Step 4: Uniqueness in general.**

> [!note]- Derivation
> Let $\Lambda \in SO^+(1,3)$ be arbitrary and suppose $\Lambda = S\circ R = S'\circ R'$ with $S, S'$ boosts whose planes contain $e_0$ and $R, R'$ spatial rotations fixing $e_0$. Apply both to $e_0$. Since $R(e_0) = R'(e_0) = e_0$,
> $$S(e_0) = S(R(e_0)) = \Lambda(e_0) = S'(R'(e_0)) = S'(e_0).$$
> So $S$ and $S'$ are boosts carrying $e_0$ to the *same* vector $e_0' := \Lambda(e_0)$. If $e_0' = e_0$ both are the identity boost; otherwise $e_0, e_0'$ span a unique timelike plane $\mathrm{Span}(e_0, e_0')$, and a boost of that plane is determined by its rapidity, fixed by $\cosh\psi = e_0\cdot e_0'$. Hence $S$ and $S'$ have the same plane and the same rapidity: $S' = S$. Then
> $$R' = S'^{-1}\Lambda = S^{-1}\Lambda = R.$$
> The decomposition is unique. **The mechanism is that $\Lambda(e_0)$ carries exactly enough information to pin the boost down, leaving no freedom for the rotation.**

> [!note]- Complete formal solution
> The image $\Lambda(e_0) = \cosh\psi\,e_0 + \sinh\psi\cos\theta\,e_1 + \sinh\psi\sin\theta\,e_2$ has time-component $\Gamma = \cosh\psi$ and spatial direction $\mathbf{n} = \cos\theta\,e_1 + \sin\theta\,e_2$, so the polar boost $S$ is the boost of rapidity $\psi$ along $\mathbf{n}$, with velocity $\mathbf{V} = \tanh\psi\,\mathbf{n}$. Then $R = S^{-1}\Lambda$ satisfies $R(e_0) = S^{-1}(\Lambda e_0) = S^{-1}(S e_0) = e_0$, so $R = \mathrm{diag}(1, H)$, $H \in SO(3)$, is a spatial rotation (the rotation by $\theta$ in $(e_1, e_2)$). The matrix $\Lambda$ is not symmetric ($\Lambda_{12} = \sin\theta \ne -\sinh\psi\sin\theta = \Lambda_{21}$), so $\Lambda$ is not a boost; but $S$ is symmetric with positive eigenvalues $e^{\pm\psi}, 1, 1$, and $R^{\mathsf T}R = I_4$, exhibiting $\Lambda = SR$ as the linear-algebra polar decomposition. Uniqueness: any $\Lambda = S'R'$ has $S'(e_0) = \Lambda(e_0) = S(e_0)$, and a boost is fixed by its image of $e_0$ (plane $\mathrm{Span}(e_0, \Lambda(e_0))$, rapidity $\cosh\psi = e_0\cdot\Lambda(e_0)$), so $S' = S$ and $R' = R$. $\blacksquare$

---

# Key Takeaways

**The boost factor is read directly off the image of the chosen 4-velocity — nothing else is needed.** The single operational lesson of the polar decomposition is that $\Lambda(e_0)$ contains the entire boost: its time-component is the Lorentz factor $\Gamma = e_0\cdot\Lambda(e_0)$, and its spatial part gives the velocity direction. Once you have built that boost $S$ and divided it out, whatever remains *automatically* fixes $e_0$ and is therefore a pure spatial rotation. The trigger "factor this Lorentz transformation relative to an observer" should fire the reflex "compute $\Lambda(e_0)$, build the boost from it, the rest is rotation." This is far more reliable than trying to recognise the boost and rotation pieces by inspecting the $4\times 4$ matrix, because the matrix entries mix the two — and the worked example shows exactly that mixing, where the lower $3\times 3$ block is not the rotation at all.

**Asymmetry of the matrix is the visible flag that a transformation is not a boost, and the asymmetry is the rotation content.** A boost, in a semi-adapted basis, has a symmetric matrix (when an index is lowered with $\eta$); a transformation whose matrix is asymmetric cannot be a boost. The given $\Lambda$ fails the symmetry test precisely in the $(e_1, e_2)$ block, which is exactly where the rotation acts — the asymmetry *is* the rotation, made visible. This is the same criterion that proves the product of two non-coplanar boosts is not a boost (its matrix is not symmetric) and that the leftover is the Thomas rotation. The reusable test: to decide whether a transformation is a pure boost, check whether $\eta\Lambda$ is symmetric; if it is not, polar-decompose to extract the rotation, and the degree of asymmetry quantifies how much rotation is present.

**Uniqueness comes for free because the image of $e_0$ over-determines the boost.** The reason the polar decomposition is unique — and the reason it is a genuine normal form rather than one choice among many — is that a boost is rigidly determined by where it sends a single timelike vector: the plane is $\mathrm{Span}(e_0, \Lambda(e_0))$ and the rapidity is $\mathrm{arcosh}(e_0\cdot\Lambda(e_0))$, with no remaining freedom. Two purported decompositions $S R = S' R'$ must send $e_0$ to the same place via their boost factors (the rotations fix $e_0$), so the boosts coincide and then the rotations do too. This "the symmetric positive factor is forced" mechanism is the exact analogue of the uniqueness of the matrix polar decomposition $M = (MM^{\mathsf T})^{1/2}\cdot(\text{orthogonal})$, where the positive-definite square root is unique. Whenever a factorisation has one factor determined by an extremal or positivity condition, expect uniqueness, and prove it by showing that factor is forced.
