---
type: exercise
subject: riemannian-geometry
difficulty: "⭐⭐"
prereqs:
  - "Def - Affine Connection on a Vector Bundle"
  - "Def - Torsion Tensor"
  - "Def - The Lie Bracket of Vector Fields"
tags: [geometry, riemannian-geometry, connections, lie-groups]
---

# Problem Statement

Let $G$ be a Lie group. Define a connection $\nabla$ on $TG$ by declaring all **left-invariant vector fields to be parallel**: $\nabla X = 0$ for every left-invariant vector field $X$, and extend by Leibniz to general vector fields.

(a) Verify that this prescription uniquely determines a connection on $TG$ (called the **Weitzenböck connection** or the **(-)-Cartan-Schouten connection**).

(b) Compute its **torsion tensor**: show that for left-invariant $X, Y$, $T(X, Y) = -[X, Y]$ (the negative Lie bracket).

(c) Compute its **curvature tensor**: show that the curvature is identically zero, $R \equiv 0$.

(d) Conclude that $\nabla$ is a **flat connection with nonzero torsion** on every non-abelian Lie group.

**Recall:**

A **Lie group** $G$ is a smooth manifold with a smooth group operation and inverse. A vector field $X$ on $G$ is **left-invariant** if $(L_g)_* X = X$ for all $g \in G$, where $L_g : G \to G$, $h \mapsto gh$ is left translation. Left-invariant vector fields form a Lie algebra $\mathfrak{g}$ (closed under the Lie bracket) of dimension equal to $\dim G$, and there is a canonical isomorphism $\mathfrak{g} \cong T_eG$.

![[Def - Affine Connection on a Vector Bundle#The Definition]]

![[Def - Torsion Tensor#The Definition]]

The **Riemann curvature tensor** of a connection $\nabla$ is $R(X, Y)Z := \nabla_X\nabla_Y Z - \nabla_Y\nabla_X Z - \nabla_{[X, Y]}Z$.

---

# Convergent Strategy

**Problem class:** A structural exercise in connection theory: construct a connection by prescribing it on a specific frame (here, the left-invariant frame on a Lie group) and analyse the resulting torsion and curvature. The aim is to exhibit a connection that is *flat* (curvature zero) but has *nonzero torsion* — demonstrating that flatness and torsion-freeness are independent.

**Assumption pattern:** The Lie group $G$ provides a global frame for $TG$: any basis $(X_1, \ldots, X_n)$ of $\mathfrak{g}$ (the Lie algebra) extends to a global left-invariant frame $(X_1, \ldots, X_n)$ on $G$. This means $TG$ is trivialisable as a vector bundle — $G$ is **parallelisable**. The Weitzenböck connection is defined by declaring this trivialisation to be the "constant frame".

**Theorem routing:** (a) Use the existence-uniqueness: given a global frame, define $\nabla X_a = 0$ for each frame member; the connection axioms extend uniquely to general $Y = Y^a X_a$ by the Leibniz rule, giving $\nabla_X Y = X(Y^a)X_a$. (b) Compute the torsion directly from the definition $T(X, Y) = \nabla_X Y - \nabla_Y X - [X, Y]$ on left-invariant fields, using $\nabla_X Y = 0$ for left-invariant $X, Y$. (c) Compute the curvature directly: $R(X, Y)Z = 0$ on left-invariant $X, Y, Z$ because all covariant derivatives of left-invariant fields vanish.

**Key decision point:** The non-obvious point is recognising the distinction between **flatness** and **torsion-freeness**. The Weitzenböck connection illustrates that you can have one without the other: flat ($R = 0$) yet with substantial torsion ($T(X, Y) = -[X, Y]$). This breaks the intuition that "trivial connection = both zero", and prepares for the recognition that the [[Def - Levi-Civita Connection|Levi-Civita connection]] requires *both* torsion-freeness *and* metric-compatibility to be uniquely determined.

---

# Legal Operations Used

1. **Operation 11 from the topic page (Recognise a connection on a vector bundle as more general than a connection on $TM$).** The Weitzenböck connection is a connection on $TG$ defined via a global frame — illustrating the freedom in choosing a connection beyond the Levi-Civita default. On a generic manifold this construction is unavailable (no global frame exists), but on a parallelisable manifold like a Lie group it is canonical.

2. **Operation 10 from the topic page (Use torsion-freeness to convert antisymmetric covariant derivatives into Lie brackets).** The reverse application: since the Weitzenböck connection has $\nabla_X Y = 0 = \nabla_Y X$ on left-invariant fields, the difference $\nabla_X Y - \nabla_Y X = 0$, but the Lie bracket $[X, Y]$ is generally nonzero. The torsion $T(X, Y) = 0 - 0 - [X, Y] = -[X, Y]$ is the explicit measure of the failure of the Lie bracket to vanish on left-invariant fields — i.e., a measure of the non-abelianness of $G$.

---

# Hints

> [!note]- Hint 1
> Pick a basis $(X_1, \ldots, X_n)$ of $\mathfrak{g}$ (the Lie algebra of $G$). These extend to global left-invariant vector fields on $G$, forming a global frame for $TG$. Declare $\nabla X_a = 0$ for each $a$, and extend by Leibniz.

> [!note]- Hint 2
> For a general vector field $Y = Y^a X_a$ (with smooth functions $Y^a$ on $G$): $\nabla_X Y = \nabla_X(Y^a X_a) = X(Y^a)X_a + Y^a \nabla_X X_a = X(Y^a)X_a + 0 = X(Y^a)X_a$. So $\nabla_X Y$ is the "directional derivative of components".

> [!note]- Hint 3
> For *left-invariant* $X, Y$, the components $Y^a$ are constants (left-invariant fields are uniquely determined by their value at $e$, expressed in the frame). So $X(Y^a) = 0$ and $\nabla_X Y = 0$. Then $T(X, Y) = \nabla_X Y - \nabla_Y X - [X, Y] = 0 - 0 - [X, Y] = -[X, Y]$.

> [!note]- Hint 4
> For curvature on left-invariant $X, Y, Z$: $R(X, Y)Z = \nabla_X\nabla_Y Z - \nabla_Y\nabla_X Z - \nabla_{[X, Y]}Z$. The first two terms vanish since $\nabla_Y Z = \nabla_X Z = 0$ for left-invariant $Y, X, Z$. The third term $\nabla_{[X, Y]}Z$ also vanishes since $Z$ is left-invariant (any covariant derivative of a left-invariant field is zero). So $R(X, Y)Z = 0$. Since left-invariant fields span $TG$ pointwise, $R \equiv 0$.

---

# Solution

**Plan paragraph.** The solution has four steps. Step 1 constructs the connection by prescribing it on the left-invariant frame and verifying the connection axioms. Step 2 computes the torsion on left-invariant fields, getting $T(X, Y) = -[X, Y]$. Step 3 computes the curvature on left-invariant fields, getting $R \equiv 0$. Step 4 contrasts with the Levi-Civita connection on a bi-invariantly-metric Lie group, where $\nabla^{LC}_X Y = \tfrac{1}{2}[X, Y]$ and the torsion vanishes but the curvature is generally nonzero — the opposite extreme.

**Step 1: Construct the Weitzenböck connection.**

Pick any basis $(X_1, \ldots, X_n)$ of $\mathfrak{g} \cong T_eG$. These extend uniquely to global left-invariant vector fields on $G$ via $X_a(g) := (dL_g)_e(X_a|_e)$. The $X_a$ form a global frame for $TG$ (linearly independent at every point because they form a basis of $T_eG$ and left translation is a diffeomorphism).

Define $\nabla X_a := 0$ for each $a = 1, \ldots, n$. Extend to general $Y = Y^a X_a$ by the Leibniz axiom:
$$
\nabla_X Y := X(Y^a) X_a + Y^a \nabla_X X_a = X(Y^a) X_a.
$$

This satisfies the connection axioms: $C^\infty(M)$-linearity in $X$ ($\nabla_{fX} Y = (fX)(Y^a)X_a = fX(Y^a)X_a = f\nabla_X Y$) and Leibniz in $Y$ ($\nabla_X(fY) = X(fY^a)X_a = X(f)Y^a X_a + fX(Y^a)X_a = X(f)Y + f\nabla_X Y$). So $\nabla$ is an honest connection on $TG$, called the **Weitzenböck connection** (also "(-)-Cartan-Schouten" in some references).

> [!note]- Derivation
> The construction is the standard "define on a frame, extend by Leibniz" procedure for connections. The connection axioms are easy to verify because the formula $\nabla_X Y = X(Y^a)X_a$ is the same as the componentwise derivative in the chosen frame — so it inherits the algebraic properties of the directional derivative. The frame need not be a *coordinate* frame; it just needs to be a global smooth frame on $G$, which exists because $G$ is parallelisable (the left-invariant frame trivialises $TG$).

**Step 2: Compute the torsion.**

For left-invariant $X, Y$, the components $X^a, Y^a$ in the left-invariant frame are constant functions (left-invariance forces this). So $\nabla_X Y = X(Y^a)X_a = 0$ and similarly $\nabla_Y X = 0$.

The Lie bracket $[X, Y]$ of two left-invariant fields is again left-invariant, with components given by the structure constants: $[X_a, X_b] = c^c_{ab}X_c$. For general left-invariant $X = X^a X_a, Y = Y^b X_b$ with constant $X^a, Y^b$: $[X, Y] = X^a Y^b [X_a, X_b] = X^a Y^b c^c_{ab} X_c$, with constant coefficients $X^a Y^b c^c_{ab}$.

The torsion: $T(X, Y) = \nabla_X Y - \nabla_Y X - [X, Y] = 0 - 0 - [X, Y] = -[X, Y]$.

In components on the left-invariant frame: $T(X_a, X_b) = -[X_a, X_b] = -c^c_{ab}X_c$, so $T^c_{ab} = -c^c_{ab}$. The torsion of the Weitzenböck connection on a Lie group is *the negative of the Lie bracket structure constants*.

> [!note]- Derivation
> Left-invariant fields have constant components in the left-invariant frame: if $X$ is left-invariant and $X(e) = X^a X_a(e) = X^a X_a|_e$, then by left-invariance $X(g) = (dL_g)_e X(e) = (dL_g)_e (X^a X_a|_e) = X^a (dL_g)_e X_a|_e = X^a X_a(g)$. So the components $X^a$ are the same at every point — constant. Hence the derivative of a constant is zero: $X(Y^a) = 0$ for left-invariant $X, Y$. Same for $Y(X^a)$. The torsion is then $T(X, Y) = -[X, Y]$ directly. On the frame: $[X_a, X_b] = c^c_{ab}X_c$ by definition of the structure constants, so $T(X_a, X_b) = -c^c_{ab}X_c$, i.e., $T^c_{ab} = -c^c_{ab}$.

**Step 3: Compute the curvature.**

For left-invariant $X, Y, Z$: $\nabla_X\nabla_Y Z = \nabla_X(0) = 0$ (since $\nabla_Y Z = 0$ for left-invariant $Y, Z$), and similarly $\nabla_Y\nabla_X Z = 0$. The third term $\nabla_{[X, Y]}Z$: $[X, Y]$ is left-invariant (Lie algebra closes), $Z$ is left-invariant, so $\nabla_{[X, Y]}Z = 0$.

Therefore $R(X, Y)Z = 0 - 0 - 0 = 0$ on left-invariant fields.

Since left-invariant fields span $T_pG$ for every $p$ (they form a frame), and $R$ is a tensor (depends on values at $p$ only), $R \equiv 0$ everywhere.

The Weitzenböck connection is **flat**.

> [!note]- Derivation
> Direct from the definition $R(X, Y)Z := \nabla_X\nabla_Y Z - \nabla_Y\nabla_X Z - \nabla_{[X, Y]}Z$ applied to left-invariant fields: every term vanishes because covariant derivatives of left-invariant fields are zero. Since $R$ is $C^\infty(M)$-multilinear (a tensor), its vanishing on the left-invariant frame implies vanishing on every triple of vector fields. So $R \equiv 0$ globally.

**Step 4: Contrast with the Levi-Civita connection.**

On a Lie group with bi-invariant Riemannian metric (which exists iff $G$ is compact or abelian), the Levi-Civita connection on left-invariant fields is $\nabla^{LC}_X Y = \tfrac{1}{2}[X, Y]$ (from the Koszul formula, see [[Thm - Koszul Formula]]). The torsion of this is $T(X, Y) = \nabla^{LC}_X Y - \nabla^{LC}_Y X - [X, Y] = \tfrac{1}{2}[X, Y] - \tfrac{1}{2}[Y, X] - [X, Y] = \tfrac{1}{2}[X, Y] + \tfrac{1}{2}[X, Y] - [X, Y] = 0$ — torsion-free as expected.

The curvature of the Levi-Civita: $R(X, Y)Z = \nabla_X(\tfrac{1}{2}[Y, Z]) - \nabla_Y(\tfrac{1}{2}[X, Z]) - \nabla_{[X, Y]}Z = \tfrac{1}{4}[X, [Y, Z]] - \tfrac{1}{4}[Y, [X, Z]] - \tfrac{1}{2}[[X, Y], Z]$. Using the Jacobi identity $[X, [Y, Z]] + [Y, [Z, X]] + [Z, [X, Y]] = 0$, rearrange: $\tfrac{1}{4}[X, [Y, Z]] - \tfrac{1}{4}[Y, [X, Z]] - \tfrac{1}{2}[[X, Y], Z] = \tfrac{1}{4}([X, [Y, Z]] + [Y, [Z, X]]) - \tfrac{1}{2}[[X, Y], Z] = -\tfrac{1}{4}[Z, [X, Y]] - \tfrac{1}{2}[[X, Y], Z] = \tfrac{1}{4}[[X, Y], Z] - \tfrac{1}{2}[[X, Y], Z] = -\tfrac{1}{4}[[X, Y], Z]$. So $R(X, Y)Z = -\tfrac{1}{4}[[X, Y], Z]$. For non-abelian $G$ this is generically non-zero — the Levi-Civita is *not* flat.

**Summary contrast:**
| Connection | Torsion $T$ | Curvature $R$ |
|---|---|---|
| Weitzenböck | $-[X, Y]$ (nonzero for non-abelian $G$) | $0$ (flat) |
| Levi-Civita (bi-invariant metric) | $0$ (torsion-free) | $-\tfrac{1}{4}[[X, Y], Z]$ (nonzero for non-abelian $G$) |

This illustrates that **flatness and torsion-freeness are independent**: each connection has one but not the other.

> [!note]- Complete formal solution
> **The Weitzenböck connection.** Define $\nabla$ on $TG$ by $\nabla X = 0$ for every left-invariant vector field $X$, extended by Leibniz to $\nabla_X Y = X(Y^a)X_a$ for $Y = Y^a X_a$ in the left-invariant frame. This is a connection on $TG$.
>
> **Torsion.** For left-invariant $X, Y$ (constant components), $\nabla_X Y = \nabla_Y X = 0$. So $T(X, Y) = \nabla_X Y - \nabla_Y X - [X, Y] = -[X, Y]$. On the left-invariant frame: $T(X_a, X_b) = -[X_a, X_b] = -c^c_{ab}X_c$. The torsion is the negative of the Lie bracket of $\mathfrak{g}$.
>
> **Curvature.** For left-invariant $X, Y, Z$: all covariant derivatives vanish ($\nabla_Y Z = 0$, $\nabla_X Z = 0$, $\nabla_{[X, Y]}Z = 0$ since $[X, Y]$ is left-invariant and $Z$ is left-invariant). So $R(X, Y)Z = 0$. Since $R$ is a tensor and left-invariant fields span $T_pG$ at every $p$, $R \equiv 0$.
>
> **Conclusion.** The Weitzenböck connection is flat (zero curvature) with nonzero torsion (proportional to the Lie bracket structure constants) on every non-abelian Lie group. $\blacksquare$

---

# Key Takeaways

**Flatness and torsion-freeness are completely independent.** The Weitzenböck connection on a non-abelian Lie group is the standard counterexample to the intuition that "a 'simple' connection should have both zero curvature and zero torsion". On non-abelian compact Lie groups like $SU(2) \cong S^3$, the Weitzenböck connection is flat but has substantial torsion, while the Levi-Civita connection of the bi-invariant metric is torsion-free but has substantial curvature. Each is a valid affine connection on $TG$, with different geometric content. The Levi-Civita's uniqueness theorem [[Thm - Fundamental Theorem of Riemannian Geometry (Full Proof)]] selects it as the unique connection that has *both* zero torsion *and* metric-compatibility — and it is the geometric default precisely because of this uniqueness.

**Parallelisable manifolds have a canonical "trivial" connection.** Any parallelisable manifold $M$ (i.e., $TM$ is a trivial bundle, equivalently has a global frame) admits a canonical flat connection: declare the global frame to be parallel. This is the Weitzenböck connection on a Lie group, but the same construction works for any global frame on any parallelisable manifold. Examples: $\mathbb{R}^n$ (Cartesian frame), $S^1, S^3, S^7$ (only spheres that are parallelisable, by Adams' theorem; $S^3 = SU(2), S^7 = $ unit octonions), all Lie groups. The conceptual takeaway: parallelisability has a strong "flatness" consequence — a canonical flat (but possibly torsionful) connection.

**The torsion of the Weitzenböck connection measures non-commutativity.** $T(X, Y) = -[X, Y]$ on left-invariant fields. So the torsion is literally the Lie bracket (with a sign), and it vanishes iff the Lie group is abelian. For $SU(2) \cong S^3$ with the standard Pauli-matrix basis, the structure constants are $c^k_{ij} = \varepsilon_{ijk}$ (the Levi-Civita symbol), so the torsion components are $T^k_{ij} = -\varepsilon_{ijk}$ — a single antisymmetric tensor field carrying the entire non-commutativity of $SU(2)$. The torsion encodes the "twist" of parallel transport on a non-abelian group: walking around an infinitesimal closed quadrilateral spanned by two left-invariant directions does not return to the starting point but is displaced by an amount proportional to the Lie bracket.

**The Levi-Civita-on-bi-invariant-Lie-group formula $\nabla_X Y = \tfrac{1}{2}[X, Y]$ is the opposite extreme.** On a compact Lie group with bi-invariant metric, the Levi-Civita connection is $\nabla_X Y = \tfrac{1}{2}[X, Y]$ on left-invariant fields. The torsion vanishes (a quick check), and the curvature is $R(X, Y)Z = -\tfrac{1}{4}[[X, Y], Z]$ (using the Jacobi identity). So the Levi-Civita is torsion-free but curved, while the Weitzenböck is flat but with torsion. The two together span the "$\nabla_X Y = \lambda[X, Y]$" family: $\lambda = 0$ gives Weitzenböck (flat, torsion $-[X, Y]$), $\lambda = \tfrac{1}{2}$ gives Levi-Civita (torsion-free, curvature nonzero), and $\lambda = 1$ gives the (+)-Cartan-Schouten connection (also flat, with torsion $+[X, Y]$). All three are valid connections on the Lie group; each has different geometric properties. This is the prototype of the "affine space of connections" — different choices give different connections with different torsion/curvature properties.

**This construction is the prototype of "gauge-equivalent connections".** Two connections $\nabla, \nabla'$ on the same bundle differ by a tensor field $A := \nabla' - \nabla \in \Gamma(T^*M \otimes \mathrm{End}\,TM)$. For the Weitzenböck and the Levi-Civita on a bi-invariant Lie group, $A(X, Y) = \tfrac{1}{2}[X, Y]$ — the *Lie bracket itself* is the difference. This is the prototype of "different connections on the same bundle with different geometric content". In gauge theory, choosing a connection is a gauge choice, and different gauge choices give different equivalent descriptions of the same physical theory; the physical content lives in gauge-invariant quantities (curvature integrals, holonomy classes). The Lie-group example illustrates this concretely: the Weitzenböck connection (flat, with torsion) and the Levi-Civita connection (torsion-free, curved) are gauge-equivalent in the sense that both describe the same underlying bundle, but they emphasise different geometric features.
