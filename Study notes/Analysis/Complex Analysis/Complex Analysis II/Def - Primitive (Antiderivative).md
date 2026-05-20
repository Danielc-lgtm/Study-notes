---
type: definition
subject: complex-analysis
prereqs:
  - "Def - Holomorphic Function"
  - "Def - Domain in the Complex Plane"
tags: [analysis, complex-analysis]
---

# Notation

$U \subseteq \mathbb{C}$ open; $f : U \to \mathbb{C}$ continuous (or holomorphic, depending on context); $F : U \to \mathbb{C}$ holomorphic with $F'(z) = f(z)$. Full registry on [[Complex Analysis II — Cauchy's Theorem and its Consequences]].

---

# Axiom Motivation

In real analysis, an antiderivative (primitive) of $f$ on an interval is a function $F$ with $F'(x) = f(x)$. Antiderivatives serve two roles: (a) the fundamental theorem of calculus reduces integration to evaluation of the primitive at endpoints; (b) the primitive determines $f$ up to an additive constant.

The complex analog is direct: a primitive of $f$ on an open set is a *holomorphic* function $F$ with $F'(z) = f(z)$. The holomorphic requirement is essential — if $F$ were only continuous or only real-differentiable, the equation $F' = f$ would not even make sense (no complex derivative).

The strong contrast with the real case: in $\mathbb{R}$, every continuous function on an interval has a primitive (just integrate). In $\mathbb{C}$, this is *false*. Primitives need not exist even for very nice continuous (even holomorphic!) functions on a given domain. The canonical example: $f(z) = 1/z$ on the punctured plane $\mathbb{C}^\times$. Locally, primitives exist (branches of $\log$), but globally on $\mathbb{C}^\times$ there is no holomorphic $F$ with $F' = 1/z$ — as shown in [[Ex - Failure of log existence on the punctured plane]].

The obstruction is *topological*: by the [[Thm - Existence of a Primitive iff Closed Integrals Vanish|existence theorem]], $f$ has a primitive on a domain $U$ iff $\int_\gamma f\,dz = 0$ for every closed curve $\gamma$ in $U$. For $1/z$ on $\mathbb{C}^\times$, the unit circle gives $\int_{|z|=1} dz/z = 2\pi i \neq 0$, so no primitive. For *simply connected* $U \subseteq \mathbb{C}$ and $f$ holomorphic, the closed integrals vanish (Cauchy's theorem) and primitives exist.

This is the *operational* lift of the real one-variable theorem: in $\mathbb{R}$, an interval is automatically simply connected, so the topological obstruction never appears, and every continuous $f$ has a primitive. In $\mathbb{C}$, the existence of primitives is contingent on the topology of the domain.

Two primitives on a connected domain differ by a constant — by [[Thm - Constant on a Domain if Derivative is Zero]]: if $F_1, F_2$ both have derivative $f$, then $(F_1 - F_2)' = 0$, so $F_1 - F_2$ is constant on the connected $U$. This is the *uniqueness up to constant* of primitives, identical to the real case.

---

# The Definition

Let $U \subseteq \mathbb{C}$ be open and $f : U \to \mathbb{C}$ a continuous function.

**Primitive (antiderivative).** A **primitive** of $f$ on $U$ is a holomorphic function $F : U \to \mathbb{C}$ such that
$$F'(z) = f(z) \quad \text{for all } z \in U.$$

**Uniqueness up to constant.** If $U$ is a connected domain and $F_1, F_2$ are both primitives of $f$ on $U$, then $F_1 - F_2$ is a constant function on $U$. (By [[Thm - Constant on a Domain if Derivative is Zero]].)

**Existence is contingent.** Not every continuous (or even holomorphic) function has a primitive on a given domain. By [[Thm - Existence of a Primitive iff Closed Integrals Vanish]], $f$ has a primitive on a domain $U$ iff $\int_\gamma f\,dz = 0$ for every closed piecewise $C^1$ curve $\gamma$ in $U$.

---

# Relate to Other Fields / Compression

In **real one-variable analysis**, the antiderivative is the inverse of differentiation, related to integration via the fundamental theorem of calculus. The complex version is *less* automatic because the topology of the domain plays a role.

In **differential forms theory**, a primitive corresponds to a *potential* for the 1-form $f(z)\,dz$: an $F$ with $dF = f(z)\,dz$. The existence of such an $F$ is exactly the closedness/exactness distinction in de Rham cohomology. For a 1-form to have a global primitive, it must be exact; closedness ($d(f\,dz) = 0$, equivalent to $f$ holomorphic) is necessary but not sufficient — the obstruction is precisely $H^1_{dR}(U)$, the first de Rham cohomology of $U$. On simply connected $U$, $H^1_{dR} = 0$, so closed forms are exact, and primitives exist.

In **integration on manifolds**, the same dichotomy: on a simply connected manifold, every closed form has a primitive; on a non-simply-connected one, the obstruction lives in cohomology.

---

# Examples / Corollaries

**Is an instance — primitive of $z^n$ for $n \geq 0$.** $F(z) = z^{n+1}/(n+1)$ on all of $\mathbb{C}$. Entire and primitive.

**Is an instance — primitive of $z^n$ for $n \leq -2$.** $F(z) = z^{n+1}/(n+1)$ on $\mathbb{C}^\times$. Holomorphic on the punctured plane (the singularity at $0$ is excluded), primitive of $z^n$ there.

**Is an instance — local primitives of $1/z$.** On any simply connected domain $U \subseteq \mathbb{C}^\times$ (e.g., the slit plane), a branch $\lambda$ of $\log$ is a primitive of $1/z$: $\lambda'(z) = 1/z$.

**Is NOT an instance — primitive of $1/z$ on $\mathbb{C}^\times$.** No global primitive exists: $\int_{|z|=1} dz/z = 2\pi i \neq 0$ would force the integral around any closed curve to be zero, contradiction. The obstruction is the loop around $0$.

**Is NOT an instance — primitive of $\bar z$ anywhere.** $\bar z$ is not holomorphic, so no holomorphic $F$ can have $F' = \bar z$ (since $F' = \bar z$ would mean $\bar z$ is the derivative of a holomorphic function, hence holomorphic itself — but $\bar z$ is not). Continuous functions in general do not need to have holomorphic primitives.

**Corollary — primitives propagate via the fundamental theorem.** If $F$ is a primitive of $f$ on $U$ and $\gamma$ is a curve in $U$ from $z_1$ to $z_2$, then $\int_\gamma f\,dz = F(z_2) - F(z_1)$ (independent of the curve). See [[Thm - Fundamental Theorem of Contour Integration]].

**Calibration check.** Verify $F(z) = z^2/2$ is a primitive of $f(z) = z$ on $\mathbb{C}$, $F(z) = -\cos z$ is a primitive of $\sin z$ on $\mathbb{C}$, $F(z) = e^z$ is a primitive of $e^z$ on $\mathbb{C}$. For non-existence: explain why $f(z) = z/\bar z$ (defined on $\mathbb{C}^\times$ and continuous there) has no holomorphic primitive (because $f$ itself is not holomorphic).

---

# Unlocked by This

> [!tip] Fundamental Theorem of Contour Integration *(from this topic)*
> The cleanest evaluation of contour integrals: if a primitive exists, the integral equals the endpoint difference. See [[Thm - Fundamental Theorem of Contour Integration]].

> [!tip] Existence Criterion *(from this topic)*
> [[Thm - Existence of a Primitive iff Closed Integrals Vanish]] characterizes when primitives exist: exactly when all closed-loop integrals vanish.

> [!tip] De Rham Cohomology *(from Differential Geometry)*
> The space of "obstructions to primitives" of closed 1-forms is the first de Rham cohomology $H^1_{dR}(U; \mathbb{R})$. For $\mathbb{C}^\times$, $H^1_{dR} \cong \mathbb{R}$, generated by $dz/z$ — the obstruction.
