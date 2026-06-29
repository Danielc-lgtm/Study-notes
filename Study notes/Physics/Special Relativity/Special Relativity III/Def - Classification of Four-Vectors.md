---
type: definition
subject: special-relativity
prereqs:
  - "Def - Minkowski Space and the Metric"
  - "Def - Four-Vector"
  - "Def - The Null Cone and the Time Arrow"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$. A four-vector $X$ has components $X^\mu$ in an orthonormal frame, $\mu = 0,1,2,3$, with $X^0$ its time component. The scalar product is $X\cdot Y = \eta_{\mu\nu}X^\mu Y^\nu = X^0Y^0 - X^1Y^1 - X^2Y^2 - X^3Y^3$, $\eta = \mathrm{diag}(1,-1,-1,-1)$; the scalar square is $X\cdot X = (X^0)^2 - (X^1)^2 - (X^2)^2 - (X^3)^2$; the norm is $\|X\| = \sqrt{|X\cdot X|}$. Full registry on [[Special Relativity III — Minkowski Spacetime and the Metric]].

> [!warning] Convention: signature
> We use **"mostly minus"**, so **timelike $\Leftrightarrow X\cdot X > 0$**, spacelike $\Leftrightarrow X\cdot X < 0$, null $\Leftrightarrow X\cdot X = 0$. Gourgoulhon uses the opposite sign, with timelike $g(v,v) < 0$. Every sign below is in our convention; to read Gourgoulhon's formulas, flip the overall sign of every scalar product.

---

# Axiom Motivation

The indefiniteness of the [[Def - Minkowski Space and the Metric|Minkowski metric]] is not a nuisance to be worked around — it is a feature to be *organised*, and the classification is that organisation. In a Euclidean space the scalar square $X\cdot X$ is always positive (for $X \neq 0$), so there is nothing to classify: every nonzero vector is alike. In Minkowski space $X\cdot X$ can take any sign, and the sign is the single most important invariant attribute of a four-vector. The whole motivation is to give a name to each sign and to recognise that the names are frame-independent.

Why is the sign the right thing to classify by? Because it is a [[Thm - Invariance of the Spacetime Interval|Lorentz invariant]]: $X\cdot X$ has the same value, hence the same sign, in every orthonormal frame. So the trichotomy "positive / zero / negative" cuts the space of four-vectors into three classes that *all observers agree on*, and these classes turn out to carry exactly the physical meaning one would want a causal structure to carry. A timelike vector ($X\cdot X > 0$) points more in time than in space: it can be the displacement between two events one can travel between slower than light, or the tangent to a massive particle's worldline. A null vector ($X\cdot X = 0$, $X \neq 0$) points equally in time and space: it lies on the light cone, the tangent to a light ray. A spacelike vector ($X\cdot X < 0$) points more in space than in time: it connects events no signal can join, and it is the kind of direction an observer calls "purely spatial". The classification *is* the causal structure of spacetime, read off from one sign.

A second, finer invariant refines the timelike and null classes. For these, the sign of the time component $X^0$ is *also* Lorentz invariant (under the orthochronous transformations physics uses), so a timelike or null vector is either **future-pointing** ($X^0 > 0$) or **past-pointing** ($X^0 < 0$), and no boost can change which. This is what gives spacetime a consistent arrow of time for causally-connectible events. The reason it works for timelike and null vectors but *fails* for spacelike ones is the geometry of the light cone: a timelike vector lies strictly inside the cone, so a boost (which scissors the axes towards the light ray but never past it) cannot tip it across to the other sheet; a spacelike vector lies outside the cone, where a boost *can* flip the sign of $X^0$ — which is exactly why the time-ordering of spacelike-separated events is frame-dependent and why such events cannot causally influence each other.

The classification must be stated for *nonzero* vectors: the zero vector has $X\cdot X = 0$ but is not called null (Gourgoulhon's Remark 1.10 — null vectors are not the zero vector). Excluding zero from the null class is not pedantry: the null vectors form the *cone minus its apex*, a genuine geometric object (two sheets, asymptotic to the unit hyperboloids), and including the apex would conflate the boundary of causality with the trivial vector.

---

# The Definition

Let $X$ be a nonzero [[Def - Four-Vector|four-vector]] with scalar square $X\cdot X = (X^0)^2 - (X^1)^2 - (X^2)^2 - (X^3)^2$ under the [[Def - Minkowski Space and the Metric|Minkowski metric]]. Then $X$ is:
- **timelike** if $X\cdot X > 0$;
- **spacelike** if $X\cdot X < 0$;
- **null** (lightlike, or isotropic) if $X\cdot X = 0$.

A four-vector that is timelike or null is called **causal**. The classification is **Lorentz invariant**: since $X\cdot X$ is the same in every orthonormal frame, so is its sign, hence the class of $X$.

A **unit vector** is one with $\|X\| = 1$, i.e.
- **timelike unit**: $X\cdot X = +1$ — these form a two-sheeted hyperboloid $\{(X^0)^2 - |\mathbf{X}|^2 = 1\}$;
- **spacelike unit**: $X\cdot X = -1$ — these form a one-sheeted hyperboloid $\{(X^0)^2 - |\mathbf{X}|^2 = -1\}$;

both hyperboloids being asymptotic to the [[Def - The Null Cone and the Time Arrow|null cone]] $\{(X^0)^2 - |\mathbf{X}|^2 = 0\}$.

For a **causal** vector (timelike or null), the sign of the time component $X^0$ is also Lorentz invariant under orthochronous transformations, giving a further split:
- **future-pointing** (future-directed) if $X^0 > 0$ — equivalently, $X$ lies in the future sheet $\mathcal{I}^+$;
- **past-pointing** (past-directed) if $X^0 < 0$ — equivalently, $X$ lies in the past sheet $\mathcal{I}^-$.

For a **spacelike** vector the sign of $X^0$ is *not* invariant — a boost can change it — so spacelike vectors admit no future/past distinction.

---

# Relate to Other Fields / Compression

The classification is the **causal type** of a vector, and it is the local data from which all of causal structure — light cones, chronological and causal futures, the impossibility of faster-than-light signalling — is assembled. In the language of quadratic forms, it is the partition of $\mathbb{R}^4$ by the sign of an indefinite form: the positive cone (timelike), the null cone (the zero set), and the negative region (spacelike). For a Euclidean form there is only the positive region; the existence of three regions is precisely the signature being $(1,3)$ rather than $(4,0)$.

Applied to physical four-vectors, the classification becomes physics. The four-velocity of any massive particle is timelike and future-pointing. The four-momentum of a massive particle is timelike ($P\cdot P = m^2 > 0$); of a photon, null ($P\cdot P = 0$); a hypothetical tachyon would have spacelike momentum. A worldline is physically allowed exactly when its tangent is everywhere timelike or null (causal): this is the statement that nothing travels faster than light.

**True name:** the classification is *the sign of $X\cdot X$, refined for causal vectors by the sign of $X^0$* — two invariant signs that between them encode the entire causal character of a four-vector. The operational reflex: to decide any causal question, compute the one scalar square and read the sign.

---

# Examples / Corollaries

**Is an instance — a future-pointing timelike vector.** $X = (2,1,0,0)$ has $X\cdot X = 4 - 1 = 3 > 0$ (timelike) and $X^0 = 2 > 0$ (future-pointing). It could be the displacement between two events a massive particle travels between, or four-velocity (after normalising to $X\cdot X = 1$).

**Is an instance — a null vector.** $X = (1,1,0,0)$ has $X\cdot X = 1 - 1 = 0$ with $X \neq 0$: null, and future-pointing since $X^0 = 1 > 0$. It is the tangent to a light ray moving in the $+x$ direction.

**Is an instance — a spacelike vector with frame-dependent time sign.** $X = (1,2,0,0)$ has $X\cdot X = 1 - 4 = -3 < 0$: spacelike. Its time component is $X^0 = 1 > 0$ in this frame, but a boost with $v > 1/2$ along $x$ makes $X^0{}' = \gamma(1 - 2v) < 0$ — the sign of the time component flips, confirming that spacelike vectors have no invariant time-orientation.

**Is NOT an instance of "null" — the zero vector.** $X = 0$ has $X\cdot X = 0$ but is *not* null: the null class is defined for nonzero vectors only (Remark 1.10). The null vectors form the cone *minus* its apex; the apex is the zero vector, excluded.

**Corollary — sum of future timelike vectors is future timelike.** If $U, V$ are future-pointing timelike, then $U\cdot V > 0$ ([[Thm - Two Lemmas on Causal Vectors|Lemma 1]]) and $(U+V)\cdot(U+V) = U\cdot U + 2U\cdot V + V\cdot V > 0$, so $U + V$ is timelike; and its time component $U^0 + V^0 > 0$, so it is future-pointing. The future-timelike vectors form a convex cone.

**Corollary — the hyperboloid of unit timelike vectors has two sheets.** The equation $X\cdot X = +1$, i.e. $(X^0)^2 - |\mathbf{X}|^2 = 1$, has solutions with $X^0 \geq 1$ (future sheet) and $X^0 \leq -1$ (past sheet), disconnected — unlike the Euclidean unit sphere, which is connected. This two-sheetedness is the geometric image of the future/past split.

**Calibration check.** If you have understood the definition you can: (i) classify $(0,1,1,1)$ as spacelike ($0 - 3 = -3 < 0$) and $(3,1,1,1)$ as timelike ($9 - 3 = 6 > 0$); (ii) exhibit a boost that flips the time-sign of a given spacelike vector but explain why none can flip the time-sign of a timelike one; (iii) state why the zero vector is excluded from the null class.

---

# Unlocked by This

> [!tip] The Light Cone and Causal Structure *(from §3.3)*
> The null vectors assemble into the [[Def - The Null Cone and the Time Arrow|null cone]], whose two sheets give the future and past; the classification is the local statement of which side of the cone a vector lies on, and the [[Thm - Two Lemmas on Causal Vectors|lemmas on causal vectors]] turn it into the convexity of the future-causal cone — the algebraic backbone of the [[Thm - The Reversed Triangle Inequality|reversed triangle inequality]] and the twin paradox.

> [!tip] Massive versus Massless Particles *(from Relativistic Dynamics)*
> Applied to the [[Def - Four-Momentum and Rest Mass|four-momentum]] $P$, the classification is the divide between massive particles ($P$ timelike, $P\cdot P = m^2 > 0$) and massless ones ($P$ null, $P\cdot P = 0$, photons); see [[Def - The Four-Momentum of a Photon]]. The future-pointing condition is the statement that energy $P^0 > 0$ — physical particles carry positive energy — and is preserved under the orthochronous Lorentz group.
