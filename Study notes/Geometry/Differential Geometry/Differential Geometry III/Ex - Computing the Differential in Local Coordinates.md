---
type: exercise
subject: differential-geometry
difficulty: "⭐⭐"
prereqs:
  - "Def - The Differential of a Smooth Map"
  - "Def - Coordinate Tangent Vectors"
  - "Def - Partial Derivatives and the Jacobian Matrix"
  - "Def - Smooth Map between Manifolds"
tags: [geometry, differential-geometry]
---

# Problem Statement

Let $F : M \to N$ be a smooth map between smooth manifolds. Let $(U, \varphi)$ be a smooth chart at $p \in M$ with coordinates $x^{1}, \dots, x^{m}$, and $(V, \psi)$ a smooth chart at $F(p) \in N$ with coordinates $y^{1}, \dots, y^{n}$. Let $\hat{F} = \psi \circ F \circ \varphi^{-1} : \varphi(U \cap F^{-1}(V)) \to \psi(V)$ be the coordinate representative of $F$.

Show that the differential $dF_{p} : T_{p}M \to T_{F(p)}N$ acts on the coordinate basis by
$$dF_{p}\left(\left.\frac{\partial}{\partial x^{i}}\right|_{p}\right) \;=\; \frac{\partial \hat{F}^{j}}{\partial x^{i}}(\varphi(p)) \, \left.\frac{\partial}{\partial y^{j}}\right|_{F(p)},$$
where $\hat{F}^{j}$ is the $j$-th component function of $\hat{F}$ and Einstein summation is in effect. Hence the matrix of $dF_{p}$ in the coordinate bases is the **Jacobian matrix** of $\hat{F}$ at $\varphi(p)$.

**Recall:**

![[Def - The Differential of a Smooth Map#The Definition]]

![[Def - Coordinate Tangent Vectors#The Definition]]

The **Jacobian matrix** of a smooth map $\hat{F} : \mathbb{R}^{m} \supseteq \hat{U} \to \mathbb{R}^{n}$ at a point $\hat{p} \in \hat{U}$ is the $n \times m$ matrix with entries $\partial \hat{F}^{j}/\partial x^{i}(\hat{p})$; see [[Def - Partial Derivatives and the Jacobian Matrix]].

---

# Convergent Strategy

**Problem class:** This is a *coordinate-translation* problem — convert the abstract precomposition definition of $dF_{p}$ into a concrete matrix in coordinate bases. The general routine is: apply $dF_{p}$ to the coordinate basis vectors $\partial/\partial x^{i}|_{p}$ one at a time, unfold both the differential definition and the coordinate-basis definition in the chart, and read off the result as a sum over the codomain coordinate basis.

**Assumption pattern:** $F$ is smooth, charts $(U, \varphi)$ and $(V, \psi)$ are available, with coordinates $x^{i}$ and $y^{j}$. The coordinate representative $\hat{F}$ is a smooth map between open subsets of Euclidean spaces, where the standard multivariate-calculus Jacobian is defined. The action of $\partial/\partial x^{i}|_{p}$ on a function $f$ is $\partial(f \circ \varphi^{-1})/\partial x^{i}(\varphi(p))$ — differentiation of the coordinate representative.

**Theorem routing:** Apply $dF_{p}(\partial/\partial x^{i}|_{p})$ to an arbitrary function $f \in C^{\infty}(V)$. By the precomposition definition, this is $(\partial/\partial x^{i}|_{p})(f \circ F)$. By the coordinate-tangent definition, this is $\partial(f \circ F \circ \varphi^{-1})/\partial x^{i}(\varphi(p))$. Now write $f \circ F \circ \varphi^{-1} = (f \circ \psi^{-1}) \circ (\psi \circ F \circ \varphi^{-1}) = \hat{f} \circ \hat{F}$ — both functions live on Euclidean space. Differentiate by the multivariate chain rule: $\partial(\hat{f} \circ \hat{F})/\partial x^{i} = \partial \hat{f}/\partial y^{j}|_{\hat{F}(\hat{p})} \cdot \partial \hat{F}^{j}/\partial x^{i}|_{\hat{p}}$. Recognize the first factor as the action of $\partial/\partial y^{j}|_{F(p)}$ on $f$. Read off the formula.

**Key decision point:** The non-obvious move is to **decompose the composite Euclidean function $f \circ F \circ \varphi^{-1}$ as a composition of two Euclidean functions** $(\hat{f}) \circ (\hat{F})$, then apply the standard multivariate chain rule. The temptation is to compute directly without this decomposition, but that obscures the appearance of the Jacobian. The chart-by-chart routing — represent everything as a composition of Euclidean-to-Euclidean maps before differentiating — is the key strategic move.

---

# Legal Operations Used

1. **Push a coordinate basis through $dF_{p}$ to get the Jacobian** (operation 3 from the topic page). Apply $dF_{p}$ to each $\partial/\partial x^{i}|_{p}$ separately. The output is an element of $T_{F(p)}N$, which we expand in the codomain coordinate basis $\partial/\partial y^{j}|_{F(p)}$.

2. **Read off coordinate components** (operation 2). The result $dF_{p}(\partial/\partial x^{i}|_{p}) = c^{j}_{i}\,\partial/\partial y^{j}|_{F(p)}$ has components $c^{j}_{i}$; to identify $c^{j}_{i}$, apply both sides to the coordinate function $y^{j}$.

3. **Use the multivariate chain rule** for the composition $\hat{f} \circ \hat{F}$ in Euclidean spaces. This converts the abstract derivation calculation into a familiar Jacobian computation.

---

# Hints

> [!note]- Hint 1
> Apply $dF_{p}(\partial/\partial x^{i}|_{p})$ to an arbitrary smooth function $f$ on $N$. By the precomposition definition, this is $(\partial/\partial x^{i}|_{p})(f \circ F)$, which by the coordinate-tangent definition is $\partial(f \circ F \circ \varphi^{-1})/\partial x^{i}(\varphi(p))$.

> [!note]- Hint 2
> Write $f \circ F \circ \varphi^{-1} = \hat{f} \circ \hat{F}$ where $\hat{f} = f \circ \psi^{-1}$. Both $\hat{f}$ and $\hat{F}$ are smooth maps between open subsets of Euclidean spaces. Use the multivariate chain rule to differentiate the composition.

> [!note]- Hint 3
> Recognize $\partial \hat{f}/\partial y^{j}|_{\hat{F}(\hat{p})}$ as $(\partial/\partial y^{j}|_{F(p)})(f)$ — by the coordinate-tangent definition applied to the codomain chart.

---

# Solution

The proof proceeds in two stages. Apply $dF_{p}(\partial/\partial x^{i}|_{p})$ to an arbitrary smooth function $f$ and unfold both the precomposition definition of the differential and the coordinate-basis definition. Recognize the result as a Jacobian sum-product using the multivariate chain rule.

**Step 1: Unfold the definitions of $dF_{p}$ and $\partial/\partial x^{i}|_{p}$.**

Compute $dF_{p}(\partial/\partial x^{i}|_{p})(f)$ in terms of partial derivatives of coordinate representatives.

> [!note]- Derivation
> By the precomposition definition of the differential,
> $$\left(dF_{p}\left(\left.\frac{\partial}{\partial x^{i}}\right|_{p}\right)\right)(f) = \left(\left.\frac{\partial}{\partial x^{i}}\right|_{p}\right)(f \circ F).$$
> By the definition of the coordinate tangent vector,
> $$\left(\left.\frac{\partial}{\partial x^{i}}\right|_{p}\right)(f \circ F) = \frac{\partial (f \circ F \circ \varphi^{-1})}{\partial x^{i}}(\varphi(p)).$$

**Step 2: Decompose and apply the multivariate chain rule.**

Write $f \circ F \circ \varphi^{-1}$ as a composition of Euclidean maps and apply the chain rule.

> [!note]- Derivation
> Insert $\psi^{-1} \circ \psi = \mathrm{id}$ to get:
> $$f \circ F \circ \varphi^{-1} = (f \circ \psi^{-1}) \circ (\psi \circ F \circ \varphi^{-1}) = \hat{f} \circ \hat{F},$$
> where $\hat{f} = f \circ \psi^{-1}$ is the codomain coordinate representative of $f$ and $\hat{F} = \psi \circ F \circ \varphi^{-1}$ is the coordinate representative of $F$.
>
> Both $\hat{f} : \psi(V) \to \mathbb{R}$ and $\hat{F} : \varphi(U \cap F^{-1}(V)) \to \psi(V)$ are smooth maps between open subsets of Euclidean spaces. The multivariate chain rule gives
> $$\frac{\partial (\hat{f} \circ \hat{F})}{\partial x^{i}}(\varphi(p)) = \frac{\partial \hat{f}}{\partial y^{j}}(\hat{F}(\varphi(p))) \cdot \frac{\partial \hat{F}^{j}}{\partial x^{i}}(\varphi(p))$$
> (Einstein summation over $j$). The point $\hat{F}(\varphi(p)) = \psi(F(p))$, the codomain chart's representation of $F(p)$.
>
> The first factor $\partial \hat{f}/\partial y^{j}(\hat{F}(\varphi(p)))$ is, by the definition of the coordinate tangent vector $\partial/\partial y^{j}|_{F(p)}$, just $(\partial/\partial y^{j}|_{F(p)})(f)$. So
> $$\left(dF_{p}\left(\left.\frac{\partial}{\partial x^{i}}\right|_{p}\right)\right)(f) = \left(\left.\frac{\partial}{\partial y^{j}}\right|_{F(p)}\right)(f) \cdot \frac{\partial \hat{F}^{j}}{\partial x^{i}}(\varphi(p)).$$

**Step 3: Read off the result.**

Recognize the right-hand side as a linear combination of coordinate basis vectors.

> [!note]- Derivation
> The right-hand side of the equation in Step 2 is the action of the derivation
> $$\frac{\partial \hat{F}^{j}}{\partial x^{i}}(\varphi(p)) \, \left.\frac{\partial}{\partial y^{j}}\right|_{F(p)} \in T_{F(p)}N$$
> on the function $f$. Since this equation holds for every $f \in C^{\infty}(V)$, the two derivations are equal:
> $$dF_{p}\left(\left.\frac{\partial}{\partial x^{i}}\right|_{p}\right) = \frac{\partial \hat{F}^{j}}{\partial x^{i}}(\varphi(p)) \, \left.\frac{\partial}{\partial y^{j}}\right|_{F(p)}.$$
> The matrix of $dF_{p}$ in the coordinate bases $\{\partial/\partial x^{i}|_{p}\}$ and $\{\partial/\partial y^{j}|_{F(p)}\}$ has entry $(j, i)$ equal to $\partial \hat{F}^{j}/\partial x^{i}(\varphi(p))$ — the Jacobian matrix of $\hat{F}$ at $\varphi(p)$.

> [!note]- Complete formal solution
> Let $f \in C^{\infty}(V)$ be a smooth function near $F(p)$. By the precomposition definition of the differential,
> $$\left(dF_{p}\left(\left.\frac{\partial}{\partial x^{i}}\right|_{p}\right)\right)(f) = \left(\left.\frac{\partial}{\partial x^{i}}\right|_{p}\right)(f \circ F) = \frac{\partial (f \circ F \circ \varphi^{-1})}{\partial x^{i}}(\varphi(p))$$
> by the coordinate-tangent definition. Write $f \circ F \circ \varphi^{-1} = (f \circ \psi^{-1}) \circ (\psi \circ F \circ \varphi^{-1}) = \hat{f} \circ \hat{F}$. By the multivariate chain rule on $\mathbb{R}^{m} \to \mathbb{R}^{n} \to \mathbb{R}$:
> $$\frac{\partial (\hat{f} \circ \hat{F})}{\partial x^{i}}(\varphi(p)) = \sum_{j=1}^{n} \frac{\partial \hat{f}}{\partial y^{j}}(\psi(F(p))) \cdot \frac{\partial \hat{F}^{j}}{\partial x^{i}}(\varphi(p)).$$
> The first factor is, by definition, $(\partial/\partial y^{j}|_{F(p)})(f)$. So
> $$\left(dF_{p}\left(\left.\frac{\partial}{\partial x^{i}}\right|_{p}\right)\right)(f) = \sum_{j=1}^{n} \frac{\partial \hat{F}^{j}}{\partial x^{i}}(\varphi(p)) \cdot \left(\left.\frac{\partial}{\partial y^{j}}\right|_{F(p)}\right)(f).$$
> This holds for every $f$, so
> $$dF_{p}\left(\left.\frac{\partial}{\partial x^{i}}\right|_{p}\right) = \frac{\partial \hat{F}^{j}}{\partial x^{i}}(\varphi(p)) \, \left.\frac{\partial}{\partial y^{j}}\right|_{F(p)}.$$
> The matrix of $dF_{p}$ in the coordinate bases is the $n \times m$ matrix with entries $\partial \hat{F}^{j}/\partial x^{i}(\varphi(p))$ — the Jacobian matrix of $\hat{F}$ at $\varphi(p)$. $\qquad\blacksquare$

---

# Key Takeaways

**The Jacobian is the coordinate matrix of $dF_{p}$ — coordinate-free version of multivariate calculus.** This exercise establishes the identification between the abstract manifold differential and the concrete Jacobian matrix from multivariate calculus. The Jacobian is *the* matrix of $dF_{p}$, in any pair of coordinate bases. This is the operational core of differential geometry: every concrete computation reduces, in a chart, to a Jacobian computation, and the abstract framework is what makes the chart computation chart-independent. When you see "compute $dF_{p}$" on an exam, the answer is "write a Jacobian matrix", and the only question is which pair of charts to use. The flexibility to choose charts cleverly is the source of computational power in differential geometry.

**The proof structure is "unfold both definitions in the chart, then apply the multivariate chain rule".** This is the general method for converting abstract identities to coordinate computations. The pattern: (1) unfold the abstract definitions in coordinates, getting an expression involving partial derivatives of coordinate representatives; (2) apply standard multivariate calculus identities to manipulate the expression; (3) recognize the result as a coordinate expression of another abstract object. The pattern recurs throughout differential geometry — in the coordinate formula for the exterior derivative, the coordinate formula for the Lie bracket, the coordinate formula for the connection. Mastering this two-step *(translate to chart, apply Euclidean calculus)* is the basic technical skill of the subject.

**The chain rule for differentials is the chain rule for Jacobians in coordinates.** The abstract chain rule $d(G \circ F) = dG \circ dF$ becomes, in coordinates, the matrix-product chain rule $D(\hat{G} \circ \hat{F}) = D\hat{G} \cdot D\hat{F}$ of multivariate calculus. The matrix product comes from composing linear maps and writing the resulting linear map in the coordinate basis. This is a one-line consequence of the present exercise applied twice, but it illustrates a deep structural fact: the manifold differential is set up *precisely* to make the Jacobian-chain-rule a chart-independent statement. Without the manifold version, one would have to verify the chain rule for Jacobians manually under every coordinate change — which is hard. The abstract framework does this verification once and for all.
