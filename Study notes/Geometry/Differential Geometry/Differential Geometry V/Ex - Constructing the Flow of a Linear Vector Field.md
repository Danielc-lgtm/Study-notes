---
type: exercise
subject: differential-geometry
difficulty: "⭐⭐"
prereqs:
  - "Def - Smooth Vector Field"
  - "Def - Integral Curve of a Vector Field"
  - "Def - Flow of a Vector Field"
  - "Def - Complete Vector Field"
tags: [geometry, differential-geometry]
---

# Problem Statement

Let $A \in \mathbb{R}^{n \times n}$ be a constant $n \times n$ real matrix, and define the **linear vector field** on $\mathbb{R}^n$

$$X(x) = Ax, \qquad \text{i.e.} \quad X = (Ax)^i \frac{\partial}{\partial x^i}.$$

Show that $X$ is a complete smooth vector field whose flow is

$$\phi^X_t(x) = e^{tA} x,$$

where $e^{tA} = \sum_{k=0}^\infty (tA)^k / k!$ is the matrix exponential. Verify all the flow axioms — smoothness in $(t, x)$, $\phi_0 = \mathrm{id}$, the group law $\phi_t \circ \phi_s = \phi_{t+s}$, and the differential generating $X$.

**Recall:**

A smooth [[Def - Vector Field on a Manifold|vector field]] $X$ on $\mathbb{R}^n$ is a smooth section of the tangent bundle, equivalently a smooth function $\mathbb{R}^n \to \mathbb{R}^n$ (via the canonical identification $T_p \mathbb{R}^n \cong \mathbb{R}^n$). An [[Def - Integral Curve of a Vector Field|integral curve]] starting at $x_0$ is a smooth curve $\gamma : J \to \mathbb{R}^n$ with $\gamma(0) = x_0$ and $\dot\gamma(t) = X(\gamma(t)) = A \gamma(t)$.

A [[Def - Flow of a Vector Field|flow]] is a smooth map $\phi : \mathcal{D} \to \mathbb{R}^n$ on a flow domain $\mathcal{D} \subseteq \mathbb{R} \times \mathbb{R}^n$, satisfying $\phi_0 = \mathrm{id}$ and the group law $\phi_t \circ \phi_s = \phi_{t+s}$.

The matrix exponential is defined by the power series $e^{tA} = \sum_{k=0}^\infty (tA)^k / k!$, which converges absolutely for all $t \in \mathbb{R}$ and all matrices $A$. It satisfies $\frac{d}{dt} e^{tA} = A e^{tA} = e^{tA} A$ and the group law $e^{(t+s)A} = e^{tA} e^{sA}$.

---

# Convergent Strategy

**Problem class:** Construct the flow of a vector field explicitly, by solving the ODE in closed form. The class is "compute a flow"; the route here is the linear-ODE machinery (matrix exponential).

**Assumption pattern:** The vector field is *linear*, $X(x) = Ax$, with $A$ a constant matrix. This is the simplest non-trivial structure for a vector field on $\mathbb{R}^n$, and it has a closed-form solution. The linearity is what makes the matrix-exponential machinery applicable.

**Theorem routing:** Linear ODE theory says $\dot\gamma = A\gamma$ with $\gamma(0) = x_0$ has solution $\gamma(t) = e^{tA} x_0$. The existence of this solution for all $t \in \mathbb{R}$ is what makes $X$ complete; the function $\phi_t(x) = e^{tA} x$ is then the flow.

**Key decision point:** The non-obvious step is recognising that the matrix exponential $e^{tA}$ is the *right* object to construct: it is uniquely characterized by being the matrix solving $\dot M = AM$, $M(0) = I$. Once you have $e^{tA}$, the rest is mechanical (verify each flow axiom). The Picard iteration in matrix-valued form is one route; the power series definition is another. The choice doesn't matter — they give the same answer.

---

# Legal Operations Used

1. **Operation 1 from the topic page (reduce a global problem to a chart).** $\mathbb{R}^n$ is itself a chart, so the global problem here is already in coordinate form.

2. **Operation 2 from the topic page (invoke Picard–Lindelöf).** The linear ODE $\dot\gamma = A\gamma$ has globally Lipschitz right-hand side (with Lipschitz constant $|A|$), so Picard–Lindelöf gives a unique smooth solution for all $t$.

3. **Operation 4 from the topic page (differentiate the flow at $t = 0$ to recover the vector field).** Verify that $\frac{d}{dt}\big|_{t=0} e^{tA} x = A x = X(x)$.

4. **Operation 3 from the topic page (use the group law of the flow).** Verify $\phi_t \circ \phi_s = \phi_{t+s}$ by the matrix exponential identity $e^{tA} e^{sA} = e^{(t+s)A}$.

---

# Hints

> [!note]- Hint 1
> The matrix exponential $e^{tA} = \sum_{k \geq 0} (tA)^k / k!$ is defined as a power series that converges absolutely and uniformly on bounded sets in $t$. It satisfies $\frac{d}{dt} e^{tA} = A e^{tA}$ and $e^{(t+s)A} = e^{tA} e^{sA}$ (because $tA$ and $sA$ commute).

> [!note]- Hint 2
> Define $\phi_t(x) := e^{tA} x$. Verify each flow axiom:
> 1. $\phi_0(x) = e^0 x = I \cdot x = x$, so $\phi_0 = \mathrm{id}$.
> 2. $\phi_t \phi_s(x) = e^{tA}(e^{sA} x) = e^{tA} e^{sA} x = e^{(t+s)A} x = \phi_{t+s}(x)$.
> 3. Smoothness in $(t, x)$ from the power-series definition.
> 4. Generator: $\frac{d}{dt}|_{t=0} \phi_t(x) = A x = X(x)$.

> [!note]- Hint 3
> Completeness: $\phi_t(x) = e^{tA} x$ is defined for all $t \in \mathbb{R}$ and all $x \in \mathbb{R}^n$, so the flow domain $\mathcal{D} = \mathbb{R} \times \mathbb{R}^n$, the maximum possible. Hence $X$ is complete.

---

# Solution

The proof has four steps, each verifying one axiom of the flow $\phi_t(x) = e^{tA} x$. Plan: Step 1 verifies the matrix exponential's defining properties; Step 2 checks $\phi_0 = \mathrm{id}$ and smoothness; Step 3 verifies the group law; Step 4 verifies the infinitesimal generator is $X$, and hence the maximal flow.

**Step 1: Define and recall properties of the matrix exponential.**

For an $n \times n$ matrix $A$, define $e^{tA} := \sum_{k=0}^\infty (tA)^k / k!$. The series converges absolutely for all $t$ (by comparison with $\sum |tA|^k / k! = e^{|t| |A|}$), and the convergence is uniform on $\{|t| \leq T\}$ for any $T > 0$. Term-by-term differentiation gives $\frac{d}{dt} e^{tA} = A e^{tA}$, and the matrix product $e^{tA} e^{sA}$ equals $e^{(t+s)A}$ because $tA$ and $sA$ commute (allowing the binomial-style rearrangement).

> [!note]- Derivation (Step 1)
> The power series $\sum_k (tA)^k / k!$ has $k$-th term bounded in operator norm by $|tA|^k / k!$, and $\sum_k |tA|^k / k! = e^{|t| |A|} < \infty$. By the comparison test, the series converges absolutely (in operator norm). Term-by-term differentiation is justified for absolutely convergent power series:
> $$\frac{d}{dt} e^{tA} = \frac{d}{dt} \sum_{k=0}^\infty \frac{(tA)^k}{k!} = \sum_{k=1}^\infty \frac{k t^{k-1} A^k}{k!} = A \sum_{k=0}^\infty \frac{(tA)^k}{k!} = A e^{tA}.$$
>
> Group law: $tA$ and $sA$ are scalar multiples of the same matrix, hence commute. For commuting matrices the BCH (Baker–Campbell–Hausdorff) formula reduces to the binomial-style identity
> $$e^{tA + sA} = e^{tA} e^{sA},$$
> which simplifies to $e^{(t+s)A} = e^{tA} e^{sA}$.

**Step 2: $\phi_0 = \mathrm{id}$ and smoothness.**

$\phi_0(x) = e^{0 \cdot A} x = I x = x$, so $\phi_0 = \mathrm{id}$. The map $(t, x) \mapsto e^{tA} x$ is smooth in both arguments: the entries of $e^{tA}$ are smooth (in fact, entire) functions of $t$, and the map $x \mapsto e^{tA} x$ is linear (hence smooth).

> [!note]- Derivation (Step 2)
> $e^{0 \cdot A} = \sum_k (0)^k A^k / k! = I + 0 + 0 + \dots = I$, so $\phi_0(x) = I x = x$, i.e. $\phi_0 = \mathrm{id}_{\mathbb{R}^n}$.
>
> Smoothness: $e^{tA}$ is the matrix with entries $(e^{tA})_{ij} = \sum_{k \geq 0} t^k (A^k)_{ij} / k!$, each entry an entire power series in $t$, hence smooth. The product $e^{tA} x = \sum_j (e^{tA})_{ij} x^j$ depends smoothly on $x$ (linear in $x$) and on $t$ (smooth entries). Joint smoothness follows.

**Step 3: Group law.**

$\phi_t(\phi_s(x)) = \phi_t(e^{sA} x) = e^{tA}(e^{sA} x) = (e^{tA} e^{sA}) x = e^{(t+s) A} x = \phi_{t+s}(x)$, using the matrix exponential's group law from Step 1.

> [!note]- Derivation (Step 3)
> For $s, t \in \mathbb{R}$ and $x \in \mathbb{R}^n$:
> $$\phi_t(\phi_s(x)) = \phi_t(e^{sA} x) = e^{tA}(e^{sA} x) \overset{(*)}{=} (e^{tA} e^{sA}) x \overset{(**)}{=} e^{(t+s)A} x = \phi_{t+s}(x),$$
> where (*) is associativity of matrix-vector multiplication and (**) is the matrix exponential group law (Step 1).

**Step 4: Infinitesimal generator and completeness.**

$\frac{d}{dt}\big|_{t=0} \phi_t(x) = \frac{d}{dt}\big|_{t=0} (e^{tA} x) = A e^{0 \cdot A} x = A x = X(x)$, using $\frac{d}{dt} e^{tA} = A e^{tA}$ from Step 1. Hence the infinitesimal generator of $\phi$ is $X$. Completeness: $\phi$ is defined on $\mathbb{R} \times \mathbb{R}^n$ (the matrix exponential exists for all $t$), the maximum possible flow domain. By the [[Thm - Fundamental Theorem on Flows|Fundamental Theorem]], this is *the* maximal flow of $X$, and $X$ is complete.

> [!note]- Derivation (Step 4)
> $\frac{d}{dt}\big|_{t=0} \phi_t(x) = \frac{d}{dt}\big|_{t=0} e^{tA} x$. Since $\frac{d}{dt} e^{tA} = A e^{tA}$, at $t = 0$ this is $A e^{0 \cdot A} = A I = A$. Applied to $x$: $A x = X(x)$. So the infinitesimal generator is $X$.
>
> Completeness: $e^{tA}$ is defined for all $t \in \mathbb{R}$ (the power series converges everywhere), and $e^{tA} x$ is defined for all $x \in \mathbb{R}^n$. So the flow domain of $\phi$ is $\mathbb{R} \times \mathbb{R}^n$, the maximum possible. By the uniqueness clause of [[Thm - Fundamental Theorem on Flows]], $\phi$ is *the* maximal flow of $X$, and the maximal flow is global, so $X$ is complete.

> [!note]- Complete formal solution
> Let $X(x) = Ax$ on $\mathbb{R}^n$ and define $\phi_t(x) := e^{tA} x$ on $\mathbb{R} \times \mathbb{R}^n$.
>
> **(1) Matrix exponential properties.** $e^{tA} := \sum_{k=0}^\infty (tA)^k / k!$ converges absolutely for all $t$, is smooth (entire) in $t$, and satisfies $\frac{d}{dt} e^{tA} = A e^{tA}$ and $e^{(t+s)A} = e^{tA} e^{sA}$ (the last by commutativity of $tA$ and $sA$).
>
> **(2) $\phi$ is smooth.** $(t, x) \mapsto e^{tA} x$ is smooth: $e^{tA}$ is smooth in $t$ entrywise, and the map $x \mapsto e^{tA} x$ is linear, hence smooth.
>
> **(3) $\phi_0 = \mathrm{id}$.** $\phi_0(x) = e^0 x = I x = x$.
>
> **(4) Group law.** $\phi_t \phi_s(x) = e^{tA}(e^{sA} x) = (e^{tA} e^{sA}) x = e^{(t+s)A} x = \phi_{t+s}(x)$.
>
> **(5) Infinitesimal generator is $X$.** $\frac{d}{dt}\big|_{t=0} \phi_t(x) = A e^{0 \cdot A} x = A x = X(x)$.
>
> **(6) Completeness.** $\phi$ is defined on all of $\mathbb{R} \times \mathbb{R}^n$, so the flow domain is maximal. By the uniqueness clause of [[Thm - Fundamental Theorem on Flows]], $\phi$ is the unique maximal flow of $X$, and it is global. Hence $X$ is complete.
>
> $\qquad\blacksquare$

---

# Key Takeaways

**Linear vector fields on $\mathbb{R}^n$ have closed-form flows via the matrix exponential.** This is the cleanest non-trivial example of a flow in differential geometry, and the matrix exponential is the canonical answer. The trigger pattern: "vector field linear in $x$, want the flow"; the action: "compute the matrix exponential $e^{tA}$, the flow is $\phi_t(x) = e^{tA} x$". This is the prototype for the **exponential map on a Lie group**: $\exp : \mathfrak{g} \to G$ sends a Lie algebra element to the time-1 flow of the corresponding left-invariant vector field, and for matrix [[Def - Group|groups]] this is the matrix exponential — see [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map]].

**Linear vector fields are always complete.** Because the matrix exponential converges for all $t \in \mathbb{R}$, the integral curves of a linear vector field are defined for all time, and the flow is global. More generally, a vector field of *sublinear growth* on $\mathbb{R}^n$ is complete (by a Grönwall argument); the linear case is the boundary, with quadratic growth ($x^2 \partial_x$) being the first incomplete example. The trigger: any linear vector field on $\mathbb{R}^n$ is complete by inspection.

**The group law of the matrix exponential mirrors the group law of the flow.** $e^{tA} e^{sA} = e^{(t+s)A}$ on the matrix side is the same identity as $\phi_t \circ \phi_s = \phi_{t+s}$ on the flow side. This is the structural reason linear flows make Lie theory natural: a one-parameter subgroup of $\mathrm{GL}(n)$ — the matrices $\{e^{tA} : t \in \mathbb{R}\}$ — is the flow of the corresponding left-invariant vector field. The bijection between linear vector fields and one-parameter [[Def - Subgroup|subgroups]] of $\mathrm{GL}(n)$ is the prototype of the bijection between left-invariant vector fields on a Lie group and one-parameter subgroups of the group.

**The matrix exponential's local expression gives the local Taylor expansion of the flow.** For small $t$, $\phi_t(x) = e^{tA} x = (I + tA + t^2 A^2 / 2 + O(t^3)) x = x + tAx + t^2 A^2 x / 2 + O(t^3)$. The first-order term $tAx = tX(x)$ recovers the vector field; the second-order term $t^2 A^2 x / 2$ involves "applying $X$ twice", which is the second-order behaviour of the flow. For nonlinear vector fields the same Taylor expansion exists but is not given by a simple matrix exponential; the second-order behaviour involves brackets, and recursive iterations generate higher-order terms. The linear case is the only one where everything collapses to a clean closed form.
