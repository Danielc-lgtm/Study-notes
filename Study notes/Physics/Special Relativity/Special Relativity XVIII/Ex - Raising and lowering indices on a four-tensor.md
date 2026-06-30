---
type: exercise
subject: special-relativity
difficulty: "⭐"
prereqs:
  - "Def - Metric Duality and Index Manipulation"
  - "Def - Tensor Operations"
  - "Def - Tensors on Minkowski Space"
tags: [physics, special-relativity]
---

# Problem Statement

Work in mostly-minus signature $\eta = \mathrm{diag}(1,-1,-1,-1)$, $c = 1$, in an orthonormal frame.

1. For a four-vector $X^\mu = (X^0, \mathbf X)$, compute the lowered components $X_\mu = \eta_{\mu\nu}X^\nu$, and verify $X^\mu X_\mu = (X^0)^2 - |\mathbf X|^2$.
2. The electromagnetic field strength has lowered components (relative to an observer)
$$
F_{\mu\nu} = \begin{pmatrix} 0 & E_1 & E_2 & E_3 \\ -E_1 & 0 & -B_3 & B_2 \\ -E_2 & B_3 & 0 & -B_1 \\ -E_3 & -B_2 & B_1 & 0 \end{pmatrix}.
$$
Compute the fully raised components $F^{\mu\nu} = \eta^{\mu\alpha}\eta^{\nu\beta}F_{\alpha\beta}$, and confirm the result matches Tong's matrix $G^{\mu\nu}$: the purely-spatial block keeps its sign while the time-space entries (the electric field) flip sign.
3. Compute the mixed-index form $F^\mu{}_\nu = \eta^{\mu\alpha}F_{\alpha\nu}$, and explain why $F^\mu{}_\nu$ is *not* antisymmetric as a matrix even though $F_{\mu\nu}$ is.

**Recall:**

![[Def - Metric Duality and Index Manipulation#The Definition]]

The metric $\eta = \mathrm{diag}(1,-1,-1,-1)$ is its own inverse matrix, so $\eta^{\mu\nu} = \eta_{\mu\nu}$ numerically. Lowering an index leaves the time component and flips the spatial components ($X_0 = X^0$, $X_i = -X^i$); see [[Def - Tensor Operations|tensor operations]]. The field strength $F$ is a [[Def - Alternate Forms and the Exterior Product|2-form]], hence antisymmetric: $F_{\mu\nu} = -F_{\nu\mu}$.

---

# Convergent Strategy

**Problem class.** A *compute-a-tensor-operation* problem — the most basic kind in the chapter — exercising [[Def - Metric Duality and Index Manipulation|raising and lowering]] indices with the metric. The [[Special Relativity XVIII — Tensors, Alternate Forms and Hodge Duality#Problem-Solving Strategy|topic strategy]] says: name the index structure, then grind, working in an orthonormal frame where $\eta$ is diagonal.

**Assumption pattern.** Everything is given in an orthonormal frame, so $\eta_{\mu\nu}$ and $\eta^{\mu\nu}$ are both $\mathrm{diag}(1,-1,-1,-1)$. The only fact needed is that each index raised or lowered with a spatial value picks up a factor $-1$, and a time-valued index picks up $+1$. The number of spatial indices being flipped determines the overall sign of each component.

**Theorem routing.** Part 1 is one application of lowering. Part 2 is two applications (one per index): an entry $F_{\mu\nu}$ becomes $F^{\mu\nu} = \eta^{\mu\mu}\eta^{\nu\nu}F_{\mu\nu}$ (no sum), so the sign is $\eta^{\mu\mu}\eta^{\nu\nu}$. Part 3 raises one index only, so the sign is $\eta^{\mu\mu}$ alone, which breaks the matrix antisymmetry.

**Key decision point.** The non-obvious point is in part 3: antisymmetry is a statement about the *abstract tensor* $F_{\mu\nu} = -F_{\nu\mu}$, not about any particular matrix of components. Raising one index with the indefinite metric mixes a $+1$ (time) and a $-1$ (space) asymmetrically between the two slots, so the *matrix* $F^\mu{}_\nu$ loses the visible antisymmetry even though the tensor is unchanged. Recognising that "antisymmetric" refers to the tensor, not the mixed-index matrix, is the lesson.

---

# Legal Operations Used

1. **Operation 1 from the topic page (lower/raise with the metric).** Applied in all three parts: multiply by $\eta_{\mu\nu}$ to lower (part 1) and by $\eta^{\mu\nu}$ to raise (parts 2, 3). In an orthonormal frame this just multiplies each component by $\pm1$ according to how many spatial indices it carries.

2. **Operation 2 from the topic page (contract an upper against a lower index).** Used in part 1 to form the invariant $X^\mu X_\mu$, a legal up–down contraction.

---

# Hints

> [!note]- Hint 1
> In an orthonormal frame, lowering or raising an index with $\eta$ multiplies the component by $\eta$'s diagonal entry for that index value: $+1$ if the index is $0$ (time), $-1$ if it is $1, 2, 3$ (space). Count the spatial indices to get the sign.

> [!note]- Hint 2
> For $F^{\mu\nu} = \eta^{\mu\alpha}\eta^{\nu\beta}F_{\alpha\beta}$ in an orthonormal frame, the sums collapse (diagonal $\eta$): $F^{\mu\nu} = \eta^{\mu\mu}\eta^{\nu\nu}F_{\mu\nu}$ (no sum on $\mu, \nu$). An entry with one time and one space index gets one $+1$ and one $-1$, net $-1$; an entry with two space indices gets $(-1)(-1) = +1$.

> [!note]- Hint 3
> The electric entries $F_{0i}$ have one time, one space index → flip sign when both are raised. The magnetic entries $F_{ij}$ have two space indices → keep their sign. So $\mathbf E \to -\mathbf E$ and $\mathbf B \to \mathbf B$ in passing from $F_{\mu\nu}$ to $F^{\mu\nu}$.

---

# Solution

The computation is pure sign-counting in an orthonormal frame: each index raised or lowered through a spatial value flips the component's sign. The plan: lower $X^\mu$ (one index), raise both indices of $F$ (sign = product of two $\eta$ entries), then raise one index of $F$ to see the antisymmetry break.

**Step 1: $X_\mu = (X^0, -\mathbf X)$ and $X^\mu X_\mu = (X^0)^2 - |\mathbf X|^2$.**

> [!note]- Derivation
> Lowering with $\eta = \mathrm{diag}(1,-1,-1,-1)$: $X_0 = \eta_{0\nu}X^\nu = \eta_{00}X^0 = X^0$, and $X_i = \eta_{i\nu}X^\nu = \eta_{ii}X^i = -X^i$ (no sum). So
> $$X_\mu = (X^0, -X^1, -X^2, -X^3) = (X^0, -\mathbf X).$$
> The invariant is the [[Def - Tensor Operations|contraction]]
> $$X^\mu X_\mu = X^0 X_0 + X^i X_i = (X^0)(X^0) + X^i(-X^i) = (X^0)^2 - |\mathbf X|^2.$$
> This is the Minkowski norm-squared, a Lorentz scalar. The "illegal" $X^\mu X^\mu = (X^0)^2 + |\mathbf X|^2$ is the Euclidean norm, not invariant.

**Step 2: raising both indices of $F$ flips the electric field's sign, $\mathbf E \to -\mathbf E$, $\mathbf B \to \mathbf B$.**

> [!note]- Derivation
> In an orthonormal frame, $F^{\mu\nu} = \eta^{\mu\alpha}\eta^{\nu\beta}F_{\alpha\beta} = \eta^{\mu\mu}\eta^{\nu\nu}F_{\mu\nu}$ (no sum, diagonal $\eta$).
> - **Electric entries** $F^{0i} = \eta^{00}\eta^{ii}F_{0i} = (+1)(-1)F_{0i} = -F_{0i} = -E_i$ (and $F^{i0} = -F_{i0} = +E_i$).
> - **Magnetic entries** $F^{ij} = \eta^{ii}\eta^{jj}F_{ij} = (-1)(-1)F_{ij} = +F_{ij}$, unchanged.
>
> So the raised matrix is
> $$F^{\mu\nu} = \begin{pmatrix} 0 & -E_1 & -E_2 & -E_3 \\ E_1 & 0 & -B_3 & B_2 \\ E_2 & B_3 & 0 & -B_1 \\ E_3 & -B_2 & B_1 & 0 \end{pmatrix},$$
> which is exactly Tong's $G^{\mu\nu}$ (with $c = 1$): the spatial $\mathbf B$-block is identical to $F_{\mu\nu}$'s, while the $\mathbf E$-entries in the first row and column have flipped sign. The matrix remains antisymmetric, $F^{\mu\nu} = -F^{\nu\mu}$, because both indices are in the same (upper) position.

**Step 3: $F^\mu{}_\nu$ is not an antisymmetric matrix, because antisymmetry is a property of the tensor, not the mixed-index matrix.**

> [!note]- Derivation
> Raise only the first index: $F^\mu{}_\nu = \eta^{\mu\alpha}F_{\alpha\nu} = \eta^{\mu\mu}F_{\mu\nu}$ (no sum). The first row ($\mu = 0$) is multiplied by $\eta^{00} = +1$; the spatial rows ($\mu = i$) are multiplied by $\eta^{ii} = -1$:
> $$F^\mu{}_\nu = \begin{pmatrix} 0 & E_1 & E_2 & E_3 \\ E_1 & 0 & B_3 & -B_2 \\ E_2 & -B_3 & 0 & B_1 \\ E_3 & B_2 & -B_1 & 0 \end{pmatrix}.$$
> This matrix is **not** antisymmetric: e.g. the $(0,1)$ entry is $+E_1$ and the $(1,0)$ entry is also $+E_1$. The reason is that "antisymmetric" means the *tensor* satisfies $F_{\mu\nu} = -F_{\nu\mu}$ — a statement with both indices in the *same* position. Raising one index with the *indefinite* metric multiplies row $\mu$ by $\eta^{\mu\mu}$ but does nothing to the column index $\nu$, breaking the symmetry between the two slots. The tensor is unchanged; only its mixed-index *presentation* is no longer an antisymmetric array. (In Tong's words, $F_{\mu\nu}$ "is more natural than $F^\mu{}_\nu$ since the former is antisymmetric.")

> [!note]- Complete formal solution
> In an orthonormal frame with $\eta = \mathrm{diag}(1,-1,-1,-1) = \eta^{-1}$:
> **(1)** $X_\mu = \eta_{\mu\mu}X^\mu = (X^0, -\mathbf X)$ (no sum), so $X^\mu X_\mu = (X^0)^2 - |\mathbf X|^2$, the invariant Minkowski norm.
> **(2)** $F^{\mu\nu} = \eta^{\mu\mu}\eta^{\nu\nu}F_{\mu\nu}$: electric entries ($F^{0i}$) get one time and one space factor, $(+1)(-1) = -1$, flipping $\mathbf E \to -\mathbf E$; magnetic entries ($F^{ij}$) get two space factors, $(-1)(-1) = +1$, leaving $\mathbf B$ unchanged. The result is Tong's $G^{\mu\nu}$, still antisymmetric since both indices are up.
> **(3)** $F^\mu{}_\nu = \eta^{\mu\mu}F_{\mu\nu}$ multiplies row $\mu$ by $\eta^{\mu\mu}$ but not the column, breaking the matrix antisymmetry; the underlying tensor is unchanged, and antisymmetry $F_{\mu\nu} = -F_{\nu\mu}$ is a property of the tensor's equal-position components, not of the mixed matrix. $\blacksquare$

---

# Key Takeaways

**Lowering and raising is sign-counting in an orthonormal frame, and the count is "one minus per spatial index."** The entire mechanics of [[Def - Metric Duality and Index Manipulation|index manipulation]] in an orthonormal frame reduces to a bookkeeping rule: each index raised or lowered through a spatial value ($1,2,3$) contributes a factor $-1$, each through the time value ($0$) a factor $+1$. To raise or lower a tensor's components, look at each component, count how many spatial indices change position, and multiply by $(-1)$ to that power. This is why the field strength's electric part (one time index) flips when both indices are raised while the magnetic part (two space indices) does not — a fact one uses constantly in electromagnetism, and which is the algebraic root of the asymmetry between how $\mathbf E$ and $\mathbf B$ sit in the field tensor. The trigger: any time you see indices moved through the metric, count spatial indices for the sign.

**Antisymmetry is a property of the tensor, not of the mixed-index matrix.** The most instructive part of the exercise is that $F^\mu{}_\nu$ fails to look antisymmetric while $F_{\mu\nu}$ and $F^{\mu\nu}$ both do. The resolution is that "antisymmetric" means the abstract tensor satisfies $F_{\dots} = -F_{\dots\text{(swapped)}}$ when the two swapped indices are in the *same* position (both up or both down). Raising one index of a two-index tensor with the indefinite metric treats the two slots asymmetrically — it multiplies by $\eta^{\mu\mu}$ on one index only — so the resulting mixed matrix need not display the symmetry, even though the tensor it represents is exactly the same object. The transferable lesson: when checking a symmetry of a tensor, put all the relevant indices in the same position first; a mixed-index matrix can hide a symmetry that is really there. This is why Tong calls $F_{\mu\nu}$ "more natural" than $F^\mu{}_\nu$.

**The Euclidean instinct $X^\mu X^\mu$ is the canonical illegal move.** The invariant is $X^\mu X_\mu$ — one index up, one down — equal to $(X^0)^2 - |\mathbf X|^2$. The expression $X^\mu X^\mu$, summing two upper indices, is the Euclidean norm $(X^0)^2 + |\mathbf X|^2$, which is frame-dependent and therefore meaningless in relativity. The diagnostic to internalise is that a legal, frame-independent contraction *always* pairs one upper with one lower index; if you find yourself summing two indices in the same position, you have made an error, and the fix is to lower (or raise) one of them with the metric first. This single rule — Tong's "illegal to write $X^\mu X^\mu$" — is the most common source of sign errors and non-invariant nonsense in the entire subject, and catching it is the first line of defence when a "scalar" turns out to depend on the frame.
