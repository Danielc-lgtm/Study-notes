---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Null Rotations and Four-Screws"
  - "Def - Classification of Restricted Lorentz Transformations"
  - "Thm - Invariant Null Direction of a Restricted Lorentz Transformation"
tags: [physics, special-relativity]
---

# Problem Statement

Prove the characterisation: a restricted Lorentz transformation $\Lambda \in SO^+(1,3)$ is a **four-screw** if and only if it leaves invariant **two distinct null directions**.

1. (Forward.) Show that a four-screw — a boost of a timelike plane $\Pi$ composed with a rotation of $\Pi^\perp$ — fixes exactly the two null directions $\mathrm{Span}(e_0\pm e_1)$ of its plane $\Pi$.
2. (Converse.) Show that if $\Lambda$ leaves invariant two distinct null directions $\mathrm{Span}(\ell)$ and $\mathrm{Span}(k)$, then choosing $\ell\cdot k = 2$ and running the adapted-frame construction forces the parameter $\alpha = 0$, so $\Lambda$ is a four-screw (with $k$ a second null eigenvector). Conclude that the four-screw is the *diagonalisable* type and the null rotation (one null direction) the non-diagonalisable type.

**Recall:**

![[Def - Null Rotations and Four-Screws#The Definition]]

The general restricted transformation in the null basis $(\ell, k, e_2, e_3)$ has the three-parameter form $(\Lambda^*)^\alpha{}_\beta$ with parameters $\psi$ (rapidity), $\theta$ (rotation angle), $\alpha$ (null-rotation shear). The construction starts from a future null eigenvector $\ell$ with $\Lambda(\ell) = e^\psi\ell$, builds $k$ with $\ell\cdot k = 2$, and expands $\Lambda(k)$; the coefficient of $e_2$ in $\Lambda(k)$ is $4\alpha e^{-\psi}$, vanishing iff $\alpha = 0$.

---

# Convergent Strategy

**Problem class.** A *characterisation* (iff) problem from the [[Special Relativity IX — The Lorentz Group, Structure and Classification#Problem-Solving Strategy|topic strategy]]: prove a geometric property (two invariant null directions) is equivalent to a structural type (four-screw), in both directions. The forward direction is a direct count; the converse forces a parameter to vanish.

**Assumption pattern.** A four-screw is block-diagonal (boost block plus rotation block), so its null eigenvectors are exactly the two light-cone generators of the boost plane — the rotation block contributes none (complex eigenvalues). Conversely, two invariant null directions provide both $\ell$ and $k$ as eigenvectors, and a second null eigenvector $k$ is precisely the condition that kills the shear parameter $\alpha$ in the normal form.

**Theorem routing.** Both directions route through the [[Def - Classification of Restricted Lorentz Transformations|normal-form construction]]: the forward direction reads the null eigenvectors off the block-diagonal four-screw matrix; the converse uses that $\Lambda(k) = e^{-\psi}k$ (a second null eigenvalue) forces the $e_2$-coefficient $4\alpha e^{-\psi} = 0$, i.e. $\alpha = 0$, leaving the four-screw form. The diagonalisability conclusion follows from [[Thm - Invariant Null Direction of a Restricted Lorentz Transformation|the existence theorem]] and the eigenvalue structure.

**Key decision point.** The non-obvious step in the converse is recognising that a *second* invariant null direction is not just extra data but a strong constraint: it forces $k$ to be an eigenvector, and in the normal form the only way $k$ can be an eigenvector is $\alpha = 0$ (since $\Lambda(k) = 4\alpha^2 e^{-\psi}\ell + e^{-\psi}k + 4\alpha e^{-\psi}e_2$, which is proportional to $k$ only when both $\alpha$-terms vanish). The natural-but-wrong assumption is that two null directions could coexist with $\alpha \ne 0$; the algebra forbids it.

---

# Legal Operations Used

1. **Count invariant null directions to name the type** (operation 5 from the topic page): two $\Rightarrow$ four-screw, the statement being proved.

2. **Build the adapted frame from a null pair** (operation 4 from the topic page): use $\ell, k$ as the two null eigenvectors and expand $\Lambda(k)$ in the normal form.

3. **Find an invariant null direction** (operation 3 from the topic page): the existence theorem guarantees one; the converse hypothesis supplies a second.

---

# Hints

> [!note]- Hint 1
> Forward: a four-screw is $\mathrm{diag}\big(\begin{smallmatrix}\cosh\psi & \sinh\psi\\ \sinh\psi & \cosh\psi\end{smallmatrix}, \begin{smallmatrix}\cos\theta & -\sin\theta\\ \sin\theta & \cos\theta\end{smallmatrix}\big)$. The boost block fixes $e_0\pm e_1$; the rotation block has complex eigenvalues, so no null directions in $\mathrm{Span}(e_2,e_3)$.

> [!note]- Hint 2
> Converse: take $\ell, k$ the two null eigenvectors, normalised $\ell\cdot k = 2$. Both are eigenvectors. Run the normal-form construction with $e_0 = \tfrac12(\ell+k)$, $e_1 = \tfrac12(\ell-k)$.

> [!note]- Hint 3
> In the normal form, $\Lambda(k) = 4\alpha^2 e^{-\psi}\ell + e^{-\psi}k + 4\alpha e^{-\psi}e_2$. For $k$ to be an eigenvector ($\Lambda(k) \parallel k$), the $\ell$ and $e_2$ components must vanish: $4\alpha^2 e^{-\psi} = 0$ and $4\alpha e^{-\psi} = 0$, both giving $\alpha = 0$.

> [!note]- Hint 4
> With $\alpha = 0$ the normal form is block-diagonal — a four-screw. For diagonalisability: a four-screw has four distinct eigenvalues (or repeated with full eigenbasis), so it is diagonalisable over $\mathbb{C}$; a null rotation (one null direction, $\alpha \ne 0$) has a defective Jordan block.

---

# Solution

The proof is the two implications. The forward direction counts the null directions of a block-diagonal four-screw; the converse forces $\alpha = 0$ from the existence of a second null eigenvector.

**Step 1: Forward — a four-screw has exactly two invariant null directions.**

> [!note]- Derivation
> A four-screw of timelike plane $\Pi = \mathrm{Span}(e_0,e_1)$ has, in the adapted orthonormal basis,
> $$\Lambda = \begin{pmatrix} \cosh\psi & \sinh\psi & 0 & 0 \\ \sinh\psi & \cosh\psi & 0 & 0 \\ 0 & 0 & \cos\theta & -\sin\theta \\ 0 & 0 & \sin\theta & \cos\theta \end{pmatrix}.$$
> *Null directions in $\Pi$.* The boost block fixes $\ell_\pm = e_0\pm e_1$: $\Lambda(e_0\pm e_1) = e^{\pm\psi}(e_0\pm e_1)$ (the rotation block leaves these untouched, as they have no $e_2, e_3$ components). Both $\ell_\pm$ are null, so $\mathrm{Span}(e_0+e_1)$ and $\mathrm{Span}(e_0-e_1)$ are two invariant null directions.
>
> *No others.* Any null direction is $\mathrm{Span}(\ell)$ with $\ell = (1, \mathbf{n})$, $|\mathbf{n}| = 1$. Write $\ell = a(e_0+e_1) + b(e_0-e_1) + ce_2 + de_3$... more directly, an invariant null direction not in $\Pi$ would require the rotation block to fix a direction in $\mathrm{Span}(e_2,e_3)$, but for $\theta \ne 0, \pi$ the rotation block has only complex eigenvalues $e^{\pm i\theta}$ and fixes no real direction there; and a null vector with both $\Pi$ and $\Pi^\perp$ components cannot be an eigenvector because the boost scales its $\Pi$-part by $e^{\pm\psi} \ne 1$ while the rotation rotates its $\Pi^\perp$-part, so the two parts cannot scale by a common factor unless one vanishes. Hence the only invariant null directions are the two in $\Pi$. (Boosts $\theta = 0$ and rotations $\psi = 0$ are the degenerate cases, still with two null directions — for a rotation the two null directions are those of the *fixed* timelike plane $\mathrm{Span}(e_0, e_1)$... here for a pure rotation in $\mathrm{Span}(e_2,e_3)$ the fixed timelike plane is $\mathrm{Span}(e_0,e_1)$ and its null directions $e_0\pm e_1$ are fixed pointwise.)

**Step 2: Converse — two null directions force $\alpha = 0$.**

> [!note]- Derivation
> Suppose $\Lambda$ leaves invariant two distinct null directions $\mathrm{Span}(\ell)$, $\mathrm{Span}(k)$. Both $\ell, k$ are future null (replacing by $-$ if needed; orthochronicity gives positive eigenvalues), non-collinear (distinct directions), so by the reversed Cauchy–Schwarz inequality $\ell\cdot k > 0$, and we rescale to $\ell\cdot k = 2$. Run the [[Def - Classification of Restricted Lorentz Transformations|normal-form construction]] with this $\ell$ (the eigenvector with $\Lambda(\ell) = e^\psi\ell$) and this $k$. The normal form gives
> $$\Lambda(k) = 4\alpha^2 e^{-\psi}\,\ell + e^{-\psi}\,k + 4\alpha e^{-\psi}\,e_2.$$
> But $\mathrm{Span}(k)$ is invariant, so $\Lambda(k) = \mu k$ for some scalar $\mu$. Matching the $\ell$ and $e_2$ components of $\Lambda(k)$ (which must vanish, since $\mu k$ has no $\ell$ or $e_2$ component — $k$ is the second basis vector):
> $$4\alpha^2 e^{-\psi} = 0 \quad\text{and}\quad 4\alpha e^{-\psi} = 0.$$
> Since $e^{-\psi} \ne 0$, both give $\alpha = 0$. With $\alpha = 0$ the normal form reduces to the block-diagonal four-screw matrix (boost in $\mathrm{Span}(e_0,e_1)$, rotation in $\mathrm{Span}(e_2,e_3)$). Hence $\Lambda$ is a **four-screw**, with $k$ the second null eigenvector (eigenvalue $e^{-\psi}$).

**Step 3: Diagonalisable versus non-diagonalisable.**

> [!note]- Derivation
> By [[Thm - Invariant Null Direction of a Restricted Lorentz Transformation|the existence theorem]], every restricted $\Lambda$ has at least one invariant null direction. The dichotomy is by the count:
> - **Two distinct null directions** (Steps 1–2): $\Lambda$ is a four-screw, $\alpha = 0$. Its eigenvalues are $e^{\psi}, e^{-\psi}$ (on the null eigenvectors $\ell, k$) and $e^{\pm i\theta}$ (on complex combinations of $e_2, e_3$) — four eigenvalues with a full eigenbasis, so $\Lambda$ is **diagonalisable over $\mathbb{C}$** (semisimple).
> - **One null direction**: $\Lambda$ is a null rotation, $\alpha \ne 0$, $\psi = \theta = 0$. Its only eigenvalue is $1$, with a defective size-three Jordan block (geometric multiplicity two against algebraic four), so $\Lambda$ is **not diagonalisable** (unipotent with nontrivial nilpotent part).
> - **Three or more null directions**: $\Lambda = \mathrm{Id}$.
>
> So "two invariant null directions $\iff$ four-screw $\iff$ diagonalisable," and the null rotation is exactly the non-diagonalisable parabolic type with a single invariant null direction. $\blacksquare$

> [!note]- Complete formal solution
> *Forward.* A four-screw $\mathrm{diag}\big(\begin{smallmatrix}\cosh\psi & \sinh\psi\\ \sinh\psi & \cosh\psi\end{smallmatrix}, \begin{smallmatrix}\cos\theta & -\sin\theta\\ \sin\theta & \cos\theta\end{smallmatrix}\big)$ fixes the two null directions $\mathrm{Span}(e_0\pm e_1)$ (boost block, eigenvalues $e^{\pm\psi}$) and no others (the rotation block, $\theta\ne 0,\pi$, has only complex eigenvalues; a mixed null vector cannot be an eigenvector since its $\Pi$- and $\Pi^\perp$-parts scale differently).
>
> *Converse.* Two invariant null directions give future null eigenvectors $\ell, k$, rescaled to $\ell\cdot k = 2$. The normal form gives $\Lambda(k) = 4\alpha^2 e^{-\psi}\ell + e^{-\psi}k + 4\alpha e^{-\psi}e_2$; invariance of $\mathrm{Span}(k)$ forces the $\ell$- and $e_2$-components to vanish, so $\alpha = 0$, and $\Lambda$ is a four-screw.
>
> *Dichotomy.* Two null directions $\iff$ four-screw $\iff$ diagonalisable (eigenvalues $e^{\pm\psi}, e^{\pm i\theta}$); one null direction $\iff$ null rotation $\iff$ non-diagonalisable (single Jordan block, eigenvalue $1$). $\blacksquare$

---

# Key Takeaways

**A second invariant null direction is a strong algebraic constraint that kills the shear parameter.** The converse hinges on recognising that demanding $k$ be a second null eigenvector forces the off-diagonal shear $\alpha$ to vanish: in the normal form $\Lambda(k)$ has $\ell$- and $e_2$-components proportional to $\alpha$, and $k$ being an eigenvector means these must be zero. So "two null directions" is not a mild condition — it is exactly the condition $\alpha = 0$ that collapses the general transformation to a four-screw. The reusable principle: when a transformation is required to fix two independent directions of a certain type, this often over-determines its normal form and forces parameters to vanish; here two null eigenvectors leave only the boost and rotation parameters $\psi, \theta$, removing the shear $\alpha$. Counting invariant directions is counting eigenvectors, and extra eigenvectors mean fewer Jordan blocks.

**The four-screw/null-rotation dichotomy is the diagonalisable/non-diagonalisable dichotomy.** A four-screw has a full eigenbasis (two real null eigenvectors plus two complex ones), so it is diagonalisable over $\mathbb{C}$; a null rotation has a defective Jordan block, so it is not. This is the Jordan canonical form specialised to $SO^+(1,3)$: every restricted transformation is either semisimple (a four-screw) or has a nontrivial nilpotent part (a null rotation). The trigger "classify by diagonalisability" maps onto "count invariant null directions": two means diagonalisable (four-screw), one means a Jordan block (null rotation). Through the spinor map this becomes the trace classification of $SL(2,\mathbb{C})$ — $|\mathrm{tr}| \ne 2$ diagonalisable (loxodromic), $\mathrm{tr} = \pm 2$ parabolic — which is the cleanest algebraic statement of the whole taxonomy.

**The forward direction shows why the rotation block contributes no null directions, and that asymmetry organises the classification.** A boost block (timelike plane) contributes *two* real null directions — the asymptotes of its hyperbolas — while a rotation block (spacelike plane) contributes *none*, because its eigenvalues are complex and a Euclidean rotation has no real invariant lines. So all of a four-screw's invariant null directions come from its boost plane, and the rotation plane is "null-direction-free." This asymmetry between the timelike and spacelike planes — hyperbolic versus elliptic, real versus complex eigenvalues — is the structural reason the classification works by counting null directions: the count localises to the boost plane, and the number there (two for a boost or four-screw, fewer for a null rotation) determines the type. The general lesson is that null directions are sensitive to the hyperbolic (boost) content of a transformation and blind to its elliptic (rotation) content.
