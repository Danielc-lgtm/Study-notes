---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Def - Connection Matrix and Local Form of a Connection"
  - "Def - Connection on a Vector Bundle"
  - "Thm - The Space of Connections is an Affine Space"
tags: [geometry, gauge-theory, connections]
---

# Problem Statement

Let $E \to M$ be a smooth real [[Def - Vector Bundle|vector bundle]] of rank $k$, let $U \subseteq M$ be an open set over which $E$ is trivial, and fix a [[Def - Local Frame|local frame]] $e = (e_1, \dots, e_k)$ of $E$ over $U$ — a row of sections $e_j \in \Gamma(U; E)$ such that $\big(e_1(m), \dots, e_k(m)\big)$ is a basis of the fibre $E_m$ for every $m \in U$.

**Part 1 (the converse to the connection-matrix construction).** Let $A \in \Omega^1(U; \mathfrak{gl}_k(\mathbb{R}))$ be an arbitrary $k \times k$ matrix whose entries $A^i{}_j$ are ordinary smooth $1$-forms on $U$. Define an operator $\nabla = d + A$ on sections of $E|_U$ by the rule that, writing a section $s \in \Gamma(U; E)$ in the frame as $s = e\sigma = \sum_{j=1}^k \sigma^j e_j$ with coefficient column $\sigma = (\sigma^1, \dots, \sigma^k)^{t} \colon U \to \mathbb{R}^k$ smooth,
$$
\nabla s := e\,(d\sigma + A\sigma) = \sum_{i=1}^k e_i \otimes \Big(d\sigma^i + \sum_{j=1}^k A^i{}_j\,\sigma^j\Big).
$$
Prove that $\nabla$ is a [[Def - Connection on a Vector Bundle|connection]] on $E|_U$, and that its [[Def - Connection Matrix and Local Form of a Connection|connection matrix]] with respect to the frame $e$ is exactly $A$. Thus **every** matrix of $1$-forms arises as a connection matrix; a connection over a trivialising set is nothing more or less than a choice of $A$.

**Part 2 (a worked instance on the two-sphere).** Take $E = TS^2$, the tangent bundle of the round sphere $S^2$ with metric $g = d\theta^2 + \sin^2\theta\,d\varphi^2$, and let $U = \{(\theta, \varphi) : \theta \in (0, \pi),\ \varphi \in (0, 2\pi)\}$ be the standard spherical-coordinate chart, with coordinate frame $e = (\partial_\theta, \partial_\varphi)$. Compute the connection matrix $A$ of the [[Def - Levi-Civita Connection|Levi-Civita connection]] $\nabla^{\mathrm{LC}}$ of $g$ in this frame. Then exhibit the **difference tensor** $a := \nabla^{\mathrm{LC}} - d$ between $\nabla^{\mathrm{LC}}$ and the flat connection $d$ of the chart (the connection whose connection matrix in the frame $e$ is the zero matrix), and explain in what precise sense $a$ is a genuine tensor even though the Christoffel symbols individually are not.

**Recall:**

The objects in play are a connection on a vector bundle, its local coefficient matrix, and the affine structure of the space of connections.

![[Def - Connection on a Vector Bundle#The Definition]]

![[Def - Connection Matrix and Local Form of a Connection#The Definition]]

That a local frame exists over $U$ is equivalent to $E$ being trivial over $U$, and every section of $E|_U$ has a unique smooth coefficient column with respect to the frame — this is [[Thm - Local Frames Span Sections|the fact that a local frame spans sections]]: for $s \in \Gamma(U; E)$ there are unique $\sigma^1, \dots, \sigma^k \in C^\infty(U)$ with $s = \sum_j \sigma^j e_j$, and each $\sigma^j$ is smooth because $s$ and the frame are.

The face of the affine-space theorem this problem uses is the *difference clause*:

![[Thm - The Space of Connections is an Affine Space#Statement]]

Concretely, for any two connections $\nabla, \hat\nabla$ on $E$ the difference $\nabla - \hat\nabla \colon \Gamma(E) \to \Omega^1(M; E)$ is not merely $\mathbb{R}$-linear but $C^\infty(M)$-linear, hence is given by a single $a \in \Omega^1(M; \operatorname{End} E)$ acting by $s \mapsto a\cdot s$; this is what makes the difference of two connections an honest tensor field.

The Christoffel symbols of the round metric in these coordinates were computed in [[Ex - Christoffel Symbols of the Round Metric on the Sphere|the Riemannian-geometry exercise]]; the nonzero ones are
$$
\Gamma^\theta_{\varphi\varphi} = -\sin\theta\cos\theta, \qquad \Gamma^\varphi_{\theta\varphi} = \Gamma^\varphi_{\varphi\theta} = \cot\theta,
$$
with all other symbols zero, and they are defined by $\nabla^{\mathrm{LC}}_{\partial_k}\partial_j = \sum_i \Gamma^i_{kj}\,\partial_i$ (see [[Riemannian Geometry I/Def - Christoffel Symbols|the definition of the Christoffel symbols]]).

> [!warning] Convention:
> This series follows Haydys's row-vector convention $\nabla e = e \cdot A$, in which the frame $e = (e_1, \dots, e_k)$ is a *row* of sections and the connection matrix multiplies it on the right, so that $\nabla e_j = \sum_i e_i\,A^i{}_j$ and the entry $A^i{}_j$ carries the upper index as its row index. The Riemannian-geometry pages write the same matrix as connection $1$-forms $\omega^i{}_j = A^i{}_j$ via $\nabla e_j = e_i \otimes \omega^i{}_j$; the two are identical objects. Throughout, $d$ denotes the componentwise exterior derivative of the coefficient column, and $A\sigma$ is ordinary matrix–column multiplication with the wedge of a $1$-form against a $0$-form (a function) reducing to the product.

---

# Convergent Strategy

**Problem class.** Part 1 is a *verify-this-is-a-connection* problem: an operator is written down in a local frame and one must check the two defining axioms of a covariant derivative, $\mathbb{R}$-linearity and the Leibniz rule, together with a Step-0 well-definedness check that the formula does not depend on any illegitimate choice. Part 2 is a *compute-the-local-representative* problem followed by a conceptual identification, in the spirit of the topic page's recurring task of translating between the invariant object $\nabla$ and its coordinate avatar $A$. The two parts are two faces of the same coin: Part 1 says the coordinate avatar can be anything, and Part 2 reads off a specific avatar and interprets it.

**Assumption pattern.** The standing hypothesis is that $U$ is a *trivialising* open set — a frame $e$ exists over it. This is exactly what makes the coefficient-column description $s = e\sigma$ available and unique, and every step of Part 1 runs through that description. Nothing about the global topology of $E$ or $M$ enters: the statement is purely local, which is why it can be proved by a bare computation in one frame. In Part 2 the extra structure is a Riemannian metric, but the metric enters only through the already-computed Christoffel symbols; the connection-matrix bookkeeping itself is metric-blind.

**Theorem routing.** Part 1 needs no external theorem beyond the definitions: it is a direct check of [[Def - Connection on a Vector Bundle|the connection axioms]] against the formula, using only the Leibniz rule for the exterior derivative $d$ on functions and the bilinearity of matrix multiplication. Part 2 routes through [[Ex - Christoffel Symbols of the Round Metric on the Sphere|the Christoffel-symbol computation]] to get the entries of $A$ via $A^i{}_j = \sum_k \Gamma^i_{kj}\,dx^k$, and then through the difference clause of [[Thm - The Space of Connections is an Affine Space|the affine-space theorem]] to certify that $\nabla^{\mathrm{LC}} - d$ is a tensor.

**Key decision point.** In Part 1 the one move that carries the proof is recognising that the *inhomogeneous* term of the Leibniz rule, the $df \otimes s$ piece, is produced entirely by the $d\sigma$ term of the formula and not at all by the $A\sigma$ term: when $f$ multiplies a section, $d(f\sigma) = df\,\sigma + f\,d\sigma$ contributes the $df$, while $A(f\sigma) = f\,A\sigma$ contributes nothing new because $A$ multiplies the scalar $f$ through linearly. Isolating which term supplies the derivative-of-$f$ is the whole content. In Part 2 the decisive realisation is that "flat connection of the chart" means the connection with $A = 0$ in the coordinate frame, so the difference tensor's matrix is simply $A$ itself — the connection matrix *is* the difference tensor once a flat reference is fixed.

---

# Legal Operations Used

The topic page for this chapter is written after its subpages, so the operations below are named descriptively; the orchestrator reconciles them with the numbered Legal Operations of the chapter's topic page.

1. **Pass to the coefficient column in a frame** (the operation "trivialise locally and compute with $\sigma \colon U \to \mathbb{R}^k$"). Every section over the trivialising set $U$ is written $s = e\sigma$ with a unique smooth column $\sigma$, by [[Thm - Local Frames Span Sections]]; all of Part 1 is carried out on columns, where a connection becomes the concrete operator $\sigma \mapsto d\sigma + A\sigma$.

2. **Read a connection matrix off a connection, and build a connection from a matrix** (the operation $\nabla \leftrightarrow A$ of [[Def - Connection Matrix and Local Form of a Connection]]). Part 1 is precisely the "build from a matrix" direction, and the final line of Part 1 runs the "read off" direction on the constructed $\nabla$ to confirm the round trip returns $A$.

3. **Subtract two connections to obtain a tensor** (the difference clause of [[Thm - The Space of Connections is an Affine Space]]). In Part 2 the difference $\nabla^{\mathrm{LC}} - d$ is certified to be an $\operatorname{End} E$-valued $1$-form by this operation, which is what upgrades the frame-dependent connection matrix into a genuine tensor relative to the fixed flat reference $d$.

4. **Convert Christoffel symbols to a connection matrix** (the operation $A^i{}_j = \Gamma^i_{kj}\,dx^k$ tying the tangent-bundle language of Riemannian geometry to the vector-bundle language of the series). This is how Part 2 imports the sphere computation.

---

# Hints

> [!note]- Hint 1
> For Part 1, do not try to work invariantly. Fix the frame $e$ and work entirely with coefficient columns: a section is a smooth map $\sigma \colon U \to \mathbb{R}^k$, and $\nabla$ is the operator $\sigma \mapsto d\sigma + A\sigma$. First check that this is even well-defined — that every section really does have a unique such $\sigma$ — before checking the axioms.

> [!note]- Hint 2
> The two axioms of a connection are $\mathbb{R}$-linearity, $\nabla(as + bt) = a\nabla s + b\nabla t$ for constants $a, b \in \mathbb{R}$, and the Leibniz rule $\nabla(fs) = df \otimes s + f\nabla s$ for $f \in C^\infty(U)$. For the Leibniz rule, apply the exterior derivative's own Leibniz rule componentwise: $d(f\sigma^j) = df\,\sigma^j + f\,d\sigma^j$. Track where the $df$ comes from.

> [!note]- Hint 3
> To confirm the connection matrix of your $\nabla$ is $A$, feed it the frame sections themselves. The section $e_j$ has coefficient column $\sigma = \epsilon_j$, the constant $j$-th standard basis vector, so $d\sigma = 0$ and $A\sigma$ is the $j$-th column of $A$. Read off $\nabla e_j$.

> [!note]- Hint 4
> For Part 2, the connection matrix and the Christoffel symbols are related by $A^i{}_j = \sum_k \Gamma^i_{kj}\,dx^k$ with $x^1 = \theta$, $x^2 = \varphi$. Assemble the four entries from the three nonzero Christoffel symbols. The flat connection $d$ has $A = 0$, so the difference tensor's matrix is $A$ verbatim — the only remaining task is to say why that matrix is a tensor.

---

# Solution

The plan is as follows. For Part 1 we first discharge well-definedness (Step 0), then verify $\mathbb{R}$-linearity (Step 1) and the Leibniz rule (Step 2), and finally read the connection matrix off the constructed operator (Step 3). For Part 2 we assemble the connection matrix from the Christoffel symbols (Step 4) and identify the difference tensor together with its tensorial meaning (Step 5). The economy in Part 1 comes from noticing that the derivative of the multiplier $f$ is produced solely by the $d\sigma$ term; the economy in Part 2 comes from the flat reference having zero connection matrix, so no subtraction of matrices is needed.

**Step 0: The operator $\nabla$ is well-defined and lands in $\Omega^1(U; E)$.**

Every section of $E|_U$ has a unique smooth coefficient column in the frame $e$, so the input to the formula is unambiguous; and each output entry is a genuine $1$-form, so $\nabla s \in \Omega^1(U; E)$.

> [!note]- Derivation
> **Uniqueness of the input.** Let $s \in \Gamma(U; E)$. By [[Thm - Local Frames Span Sections]] — since $\big(e_1(m), \dots, e_k(m)\big)$ is a basis of $E_m$ for every $m \in U$ — there are unique functions $\sigma^1, \dots, \sigma^k$ with $s(m) = \sum_j \sigma^j(m)\,e_j(m)$ for all $m$, and each $\sigma^j$ is smooth because expressing $s$ in a local trivialisation is a smooth operation. Hence the column $\sigma = (\sigma^1, \dots, \sigma^k)^t$ is determined by $s$, and the formula $\nabla s = e(d\sigma + A\sigma)$ assigns to $s$ a single unambiguous value.
>
> **The output is a bundle-valued $1$-form.** Fix $i$. The $i$-th coefficient of the output is
> $$
> (d\sigma + A\sigma)^i = d\sigma^i + \sum_{j=1}^k A^i{}_j\,\sigma^j.
> $$
> Here $d\sigma^i \in \Omega^1(U)$ is the exterior derivative of a smooth function, and each $A^i{}_j\,\sigma^j$ is the product of the $1$-form $A^i{}_j \in \Omega^1(U)$ with the function $\sigma^j \in C^\infty(U)$, again a smooth $1$-form. A finite sum of smooth $1$-forms is a smooth $1$-form, so $(d\sigma + A\sigma)^i \in \Omega^1(U)$. Therefore
> $$
> \nabla s = \sum_{i=1}^k e_i \otimes (d\sigma + A\sigma)^i \in \Gamma\big(U;\ T^*U \otimes E\big) = \Omega^1(U; E),
> $$
> which is [[Def - Bundle-Valued Differential Forms|the space of $E$-valued $1$-forms on $U$]]. So $\nabla \colon \Gamma(U; E) \to \Omega^1(U; E)$ is a well-defined map of the correct type.

**Step 1: $\nabla$ is $\mathbb{R}$-linear.**

Because the coefficient column of a real-linear combination of sections is the same real-linear combination of the columns, and both $d$ and $\sigma \mapsto A\sigma$ are $\mathbb{R}$-linear, $\nabla$ is $\mathbb{R}$-linear.

> [!note]- Derivation
> Let $s = e\sigma$, $t = e\tau$ be sections of $E|_U$ with coefficient columns $\sigma, \tau$, and let $a, b \in \mathbb{R}$ be constants. The section $as + bt$ has coefficient column $a\sigma + b\tau$, by uniqueness of coefficient columns (Step 0) and the fact that $a s + b t = e(a\sigma + b\tau)$. Then
> $$
> \nabla(as + bt) = e\big(d(a\sigma + b\tau) + A(a\sigma + b\tau)\big) \qquad \text{(definition of } \nabla \text{ on the column } a\sigma + b\tau\text{)}
> $$
> $$
> = e\big(a\,d\sigma + b\,d\tau + a\,A\sigma + b\,A\tau\big) \qquad \text{(} \mathbb{R}\text{-linearity of } d \text{ on functions, bilinearity of matrix–column multiplication over } \mathbb{R}\text{)}
> $$
> $$
> = a\,e(d\sigma + A\sigma) + b\,e(d\tau + A\tau) = a\,\nabla s + b\,\nabla t \qquad \text{(regrouping; definition of } \nabla\text{).}
> $$
> Since $a, b \in \mathbb{R}$ and $s, t$ were arbitrary, $\nabla$ is $\mathbb{R}$-linear.

**Step 2: $\nabla$ satisfies the Leibniz rule.**

For $f \in C^\infty(U)$ the derivative of the multiplier is produced by the $d\sigma$ term alone, yielding exactly the inhomogeneous $df \otimes s$ term of the Leibniz rule, while the $A\sigma$ term reproduces $f\nabla s$.

> [!note]- Derivation
> Let $f \in C^\infty(U)$ and $s = e\sigma$. The section $fs$ has coefficient column $f\sigma = (f\sigma^1, \dots, f\sigma^k)^t$, again by uniqueness of coefficient columns, since $fs = e(f\sigma)$. Apply the definition of $\nabla$ to this column:
> $$
> \nabla(fs) = e\big(d(f\sigma) + A(f\sigma)\big).
> $$
> Compute the two terms inside separately. For the first, the exterior derivative obeys the Leibniz rule componentwise on the function $f\sigma^j$:
> $$
> d(f\sigma)^j = d(f\sigma^j) = df\,\sigma^j + f\,d\sigma^j \qquad \text{(Leibniz rule for } d \text{ on the product of functions } f \text{ and } \sigma^j\text{)},
> $$
> so $d(f\sigma) = (df)\,\sigma + f\,d\sigma$, where $(df)\sigma$ is the column with entries $df\,\sigma^j$. For the second, $f$ is a scalar function and matrix multiplication is $C^\infty(U)$-linear in the column, so
> $$
> A(f\sigma) = f\,(A\sigma) \qquad \text{(the entry } \textstyle\sum_j A^i{}_j (f\sigma^j) = f \sum_j A^i{}_j \sigma^j \text{, pulling the scalar } f \text{ out).}
> $$
> Substituting,
> $$
> \nabla(fs) = e\big((df)\sigma + f\,d\sigma + f\,A\sigma\big) = e\big((df)\sigma\big) + e\big(f(d\sigma + A\sigma)\big) \qquad \text{(splitting the sum; } d(f\sigma) + A(f\sigma) = (df)\sigma + f(d\sigma + A\sigma)\text{).}
> $$
> The first summand is the inhomogeneous term: since $(df)\sigma$ has entries $df\,\sigma^i$,
> $$
> e\big((df)\sigma\big) = \sum_{i=1}^k e_i \otimes (df\,\sigma^i) = df \otimes \sum_{i=1}^k \sigma^i e_i = df \otimes s \qquad \text{(pulling the common } 1\text{-form } df \text{ out of the tensor slot; } s = \textstyle\sum_i \sigma^i e_i\text{).}
> $$
> The second summand is homogeneous: because $f$ is a scalar it commutes past the frame row,
> $$
> e\big(f(d\sigma + A\sigma)\big) = f\,e(d\sigma + A\sigma) = f\,\nabla s \qquad \text{(definition of } \nabla s\text{).}
> $$
> Adding the two, $\nabla(fs) = df \otimes s + f\,\nabla s$, which is the Leibniz rule. Together with Step 1 this verifies both axioms of [[Def - Connection on a Vector Bundle|a connection]], so $\nabla = d + A$ is a connection on $E|_U$.

**Step 3: The connection matrix of $\nabla$ is $A$.**

Feeding $\nabla$ the frame sections returns the columns of $A$, so $\nabla e = e\cdot A$ and the connection matrix is $A$ — the construction inverts the reading-off of a connection matrix.

> [!note]- Derivation
> The frame section $e_j$ is written in the frame $e$ with the constant coefficient column $\sigma = \epsilon_j$, the $j$-th standard basis vector of $\mathbb{R}^k$ (whose entries are $\delta^i_j$). Hence $d\sigma = d\epsilon_j = 0$ (the exterior derivative of a constant vanishes) and
> $$
> A\sigma = A\epsilon_j = \big(A^i{}_j\big)_{i=1}^k \qquad \text{(the } j\text{-th column of } A\text{).}
> $$
> Therefore
> $$
> \nabla e_j = e(d\epsilon_j + A\epsilon_j) = e\,(A\epsilon_j) = \sum_{i=1}^k e_i\,A^i{}_j \qquad \text{(definition of } \nabla \text{ on the column } \epsilon_j\text{; } d\epsilon_j = 0\text{).}
> $$
> Collecting these for $j = 1, \dots, k$ into the row equation $\nabla e = e \cdot A$, we read off from [[Def - Connection Matrix and Local Form of a Connection|the definition of the connection matrix]] that the connection matrix of $\nabla$ with respect to $e$ is exactly $A$. This proves the converse claim: an arbitrary $A \in \Omega^1(U; \mathfrak{gl}_k(\mathbb{R}))$ is realised as the connection matrix of the connection $d + A$, so every matrix of $1$-forms is a connection matrix. $\blacksquare$

**Step 4: The Levi-Civita connection matrix on $TS^2$ in the coordinate frame.**

Converting the Christoffel symbols by $A^i{}_j = \sum_k \Gamma^i_{kj}\,dx^k$ gives a $2 \times 2$ matrix of $1$-forms that is *not* skew-symmetric — as it must be, since the coordinate frame is not orthonormal.

> [!note]- Derivation
> Index the coordinates $x^1 = \theta$, $x^2 = \varphi$, so $dx^1 = d\theta$ and $dx^2 = d\varphi$, and the frame is $e = (e_1, e_2) = (\partial_\theta, \partial_\varphi)$. The connection matrix is defined by $\nabla^{\mathrm{LC}} e_j = \sum_i e_i\,A^i{}_j$, while the Christoffel symbols are defined by $\nabla^{\mathrm{LC}}_{\partial_k}\partial_j = \sum_i \Gamma^i_{kj}\,\partial_i$. Since $\nabla^{\mathrm{LC}}\partial_j = \sum_k dx^k \otimes \nabla^{\mathrm{LC}}_{\partial_k}\partial_j = \sum_{i} \partial_i \otimes \big(\sum_k \Gamma^i_{kj}\,dx^k\big)$, comparison gives
> $$
> A^i{}_j = \sum_{k} \Gamma^i_{kj}\,dx^k \qquad \text{(matching the coefficient of } \partial_i \text{ in the two expressions for } \nabla^{\mathrm{LC}}\partial_j\text{).}
> $$
> The nonzero Christoffel symbols from [[Ex - Christoffel Symbols of the Round Metric on the Sphere|the sphere computation]] are $\Gamma^\theta_{\varphi\varphi} = -\sin\theta\cos\theta$ and $\Gamma^\varphi_{\theta\varphi} = \Gamma^\varphi_{\varphi\theta} = \cot\theta$. Assemble the four entries:
> $$
> A^\theta{}_\theta = \Gamma^\theta_{\theta\theta}\,d\theta + \Gamma^\theta_{\varphi\theta}\,d\varphi = 0 \qquad \text{(both symbols vanish),}
> $$
> $$
> A^\theta{}_\varphi = \Gamma^\theta_{\theta\varphi}\,d\theta + \Gamma^\theta_{\varphi\varphi}\,d\varphi = -\sin\theta\cos\theta\,d\varphi \qquad \text{(only } \Gamma^\theta_{\varphi\varphi} \neq 0\text{),}
> $$
> $$
> A^\varphi{}_\theta = \Gamma^\varphi_{\theta\theta}\,d\theta + \Gamma^\varphi_{\varphi\theta}\,d\varphi = \cot\theta\,d\varphi \qquad \text{(only } \Gamma^\varphi_{\varphi\theta} \neq 0\text{),}
> $$
> $$
> A^\varphi{}_\varphi = \Gamma^\varphi_{\theta\varphi}\,d\theta + \Gamma^\varphi_{\varphi\varphi}\,d\varphi = \cot\theta\,d\theta \qquad \text{(only } \Gamma^\varphi_{\theta\varphi} \neq 0\text{).}
> $$
> Hence, with rows and columns indexed $(\theta, \varphi)$,
> $$
> A = \begin{pmatrix} A^\theta{}_\theta & A^\theta{}_\varphi \\[2pt] A^\varphi{}_\theta & A^\varphi{}_\varphi \end{pmatrix} = \begin{pmatrix} 0 & -\sin\theta\cos\theta\,d\varphi \\[2pt] \cot\theta\,d\varphi & \cot\theta\,d\theta \end{pmatrix} \in \Omega^1\big(U;\ \mathfrak{gl}_2(\mathbb{R})\big).
> $$
> This matrix is a general element of $\mathfrak{gl}_2(\mathbb{R})$-valued $1$-forms — it is not skew-symmetric, because $A^\theta{}_\varphi = -\sin\theta\cos\theta\,d\varphi$ and $A^\varphi{}_\theta = \cot\theta\,d\varphi$ are not negatives of each other. That is exactly what to expect: a metric connection has a skew connection matrix only in an *orthonormal* frame, and the coordinate frame is not orthonormal here, since $g(\partial_\varphi, \partial_\varphi) = \sin^2\theta \neq 1$.

**Step 5: The difference tensor between the Levi-Civita and flat chart connections.**

The flat connection $d$ of the chart has connection matrix $0$, so the difference tensor $a = \nabla^{\mathrm{LC}} - d$ has connection matrix $A$; and $a$ is a genuine section of $T^*U \otimes \operatorname{End}(TU)$ by the difference clause of the affine-space theorem, even though the individual Christoffel symbols are not tensor components.

> [!note]- Derivation
> **The flat reference.** The flat connection $d$ of the chart is the connection on $TU$ that differentiates componentwise in the coordinate frame: $d(e\sigma) = e\,d\sigma$, i.e. $d$ has connection matrix $A(d, e) = 0$. (By Part 1 this really is a connection — it is $d + 0$.) It is flat in the sense that its curvature vanishes, because its connection matrix is zero and the local curvature is $dA + A \wedge A = 0$; but the only property we use here is that its connection matrix is the zero matrix.
>
> **The difference is a tensor.** By the difference clause of [[Thm - The Space of Connections is an Affine Space|the affine-space theorem]] — for any two connections on $E$, the difference $\nabla^{\mathrm{LC}} - d$ is $C^\infty(U)$-linear and hence equals the action of a unique
> $$
> a \in \Omega^1\big(U;\ \operatorname{End}(TU)\big), \qquad (\nabla^{\mathrm{LC}} - d)s = a\cdot s,
> $$
> the difference is a genuine $\operatorname{End}(TU)$-valued $1$-form, an honest tensor field on $U$.
>
> **Its matrix is $A$.** In the coordinate frame $e$, connection matrices subtract: the connection matrix of $\nabla^{\mathrm{LC}} - d$ is $A(\nabla^{\mathrm{LC}}, e) - A(d, e) = A - 0 = A$. Concretely, for $s = e\sigma$,
> $$
> a\cdot s = \nabla^{\mathrm{LC}}s - ds = e(d\sigma + A\sigma) - e(d\sigma) = e(A\sigma) \qquad \text{(Part 1 formula for each connection; the } d\sigma \text{ terms cancel),}
> $$
> so $a$ acts on the frame by $a(\partial_j) = \sum_i (A^i{}_j)\,\partial_i$, that is, $a$ is the endomorphism-valued $1$-form whose matrix in the frame $(\partial_\theta, \partial_\varphi)$ is
> $$
> a \ \longleftrightarrow\ \begin{pmatrix} 0 & -\sin\theta\cos\theta\,d\varphi \\[2pt] \cot\theta\,d\varphi & \cot\theta\,d\theta \end{pmatrix}.
> $$
>
> **Why this is consistent with the non-tensoriality of $\Gamma$.** The Christoffel symbols $\Gamma^i_{kj}$ are *not* the components of a tensor: under a change of coordinates they acquire an inhomogeneous term coming from the second derivatives of the coordinate transition, precisely because $\nabla^{\mathrm{LC}}$ is being compared with the moving flat connection of whatever chart is in use, and that flat connection changes from chart to chart. Fixing *one* chart fixes *one* flat connection $d$, and against that fixed reference the difference $\nabla^{\mathrm{LC}} - d$ is a bona fide tensor on the chart domain $U$ — its matrix $A$ is a legitimate frame-representative of the tensor $a$, transforming by conjugation (not by an inhomogeneous rule) under changes of frame *that keep the same $d$*. The inhomogeneous transformation law reappears only when one also changes the flat reference, i.e. changes charts. In short: the connection matrix of $\nabla^{\mathrm{LC}}$ relative to a fixed chart's flat connection is a tensor; the connection matrix relative to "whatever chart you happen to use" is not, and that ambiguity is the non-tensoriality of $\Gamma$. $\blacksquare$

> [!note]- Complete formal solution
> **Part 1.** Fix a frame $e = (e_1, \dots, e_k)$ of $E$ over the trivialising set $U$ and $A \in \Omega^1(U; \mathfrak{gl}_k(\mathbb{R}))$. Define $\nabla s := e(d\sigma + A\sigma)$ for $s = e\sigma$.
>
> *Well-defined.* By [[Thm - Local Frames Span Sections]] each $s \in \Gamma(U; E)$ has a unique smooth coefficient column $\sigma \colon U \to \mathbb{R}^k$, so the input is unambiguous; and each output entry $d\sigma^i + \sum_j A^i{}_j\sigma^j$ is a smooth $1$-form, so $\nabla s \in \Omega^1(U; E)$.
>
> *$\mathbb{R}$-linear.* For $a, b \in \mathbb{R}$, the column of $as + bt$ is $a\sigma + b\tau$, and $d(a\sigma + b\tau) + A(a\sigma + b\tau) = a(d\sigma + A\sigma) + b(d\tau + A\tau)$ by $\mathbb{R}$-linearity of $d$ and bilinearity of matrix multiplication; hence $\nabla(as + bt) = a\nabla s + b\nabla t$.
>
> *Leibniz.* For $f \in C^\infty(U)$, the column of $fs$ is $f\sigma$, and
> $$
> \nabla(fs) = e\big(d(f\sigma) + A(f\sigma)\big) = e\big((df)\sigma + f\,d\sigma + f\,A\sigma\big) = df \otimes s + f\,\nabla s,
> $$
> using $d(f\sigma^j) = df\,\sigma^j + f\,d\sigma^j$ (Leibniz rule for $d$), $A(f\sigma) = f\,A\sigma$ (scalar pulls through matrix multiplication), and $e\big((df)\sigma\big) = df \otimes \sum_i \sigma^i e_i = df \otimes s$. So $\nabla$ is a connection.
>
> *Its connection matrix is $A$.* The section $e_j$ has constant column $\epsilon_j$, so $\nabla e_j = e(d\epsilon_j + A\epsilon_j) = e(A\epsilon_j) = \sum_i e_i A^i{}_j$; thus $\nabla e = e\cdot A$ and the connection matrix is $A$. Every $A \in \Omega^1(U; \mathfrak{gl}_k(\mathbb{R}))$ is therefore a connection matrix.
>
> **Part 2.** On $TS^2$ with $g = d\theta^2 + \sin^2\theta\,d\varphi^2$ over the chart $U$, the nonzero Christoffel symbols are $\Gamma^\theta_{\varphi\varphi} = -\sin\theta\cos\theta$ and $\Gamma^\varphi_{\theta\varphi} = \Gamma^\varphi_{\varphi\theta} = \cot\theta$. Using $A^i{}_j = \sum_k \Gamma^i_{kj}\,dx^k$ with $x^1 = \theta$, $x^2 = \varphi$,
> $$
> A = \begin{pmatrix} 0 & -\sin\theta\cos\theta\,d\varphi \\[2pt] \cot\theta\,d\varphi & \cot\theta\,d\theta \end{pmatrix} \in \Omega^1\big(U;\ \mathfrak{gl}_2(\mathbb{R})\big),
> $$
> which is not skew-symmetric because the coordinate frame is not orthonormal.
>
> The flat connection $d$ of the chart has connection matrix $0$. By the difference clause of [[Thm - The Space of Connections is an Affine Space|the affine-space theorem]], $a := \nabla^{\mathrm{LC}} - d$ is a section of $T^*U \otimes \operatorname{End}(TU)$, i.e. an honest tensor, with $a\cdot(e\sigma) = e(A\sigma)$; its matrix in the frame $(\partial_\theta, \partial_\varphi)$ is $A$. This is consistent with the Christoffel symbols not being tensor components: fixing the chart fixes the flat reference $d$, and the difference against a *fixed* reference is a tensor, whereas the inhomogeneous transformation law of $\Gamma$ appears only when the chart, and with it $d$, is changed. $\blacksquare$

> [!warning] Illegal but tempting: reading skew-symmetry into the connection matrix
> One is tempted to expect the Levi-Civita connection matrix to be skew-symmetric because the connection is metric. It is skew *only in an orthonormal frame*. In the coordinate frame $(\partial_\theta, \partial_\varphi)$ the vectors have unequal lengths, $|\partial_\theta|^2 = 1$ and $|\partial_\varphi|^2 = \sin^2\theta$, so the frame is not orthonormal and the matrix $A$ above is not skew — indeed $A^\varphi{}_\varphi = \cot\theta\,d\theta \neq 0$ sits on the diagonal, which a skew matrix forbids. The extra condition that restores skewness is orthonormality of the frame; passing to $\tfrac{1}{\sin\theta}\partial_\varphi$ in place of $\partial_\varphi$ makes the frame orthonormal and the connection matrix skew.

---

# Key Takeaways

**A connection over a trivialising set is exactly a matrix of one-forms — no more, no less.** The pair of results (a connection determines its connection matrix, and every matrix of $1$-forms is a connection matrix) says that over an open set $U$ where the bundle is trivial, the map $\nabla \mapsto A(\nabla, e)$ is a *bijection* between connections on $E|_U$ and elements of $\Omega^1(U; \mathfrak{gl}_k(\mathbb{R}))$, once a frame $e$ is fixed. This is the local coordinate model that all hands-on computation with connections runs through: to specify a connection locally, write down $k^2$ one-forms; to compute with it, use $\nabla = d + A$ on coefficient columns. The trigger for reaching for this model is any local question about a connection — curvature in a frame, gauge transformations, parallel transport equations — where the invariant formulation is unwieldy. The diagnostic that you have set it up correctly is the round trip of Step 3: building $\nabla$ from $A$ and then reading its connection matrix must return $A$. The same bijection, frame by frame, is what makes the global space of connections an affine space over $\Omega^1(M; \operatorname{End} E)$, because the transition between two frames conjugates and shifts $A$ by the rule $A' = g^{-1}Ag + g^{-1}dg$, an affine action.

**The inhomogeneous term of the Leibniz rule is produced by the flat part, and the matrix part is a pure tensor.** In the decomposition $\nabla = d + A$, it is the $d$ that supplies the offending $df \otimes s$ term — the term that makes $\nabla$ fail to be $C^\infty$-linear and hence fail to be a tensor — while $A$ contributes only the homogeneous $C^\infty$-linear piece $s \mapsto A\cdot s$. This is why differences of connections are tensors: subtracting two connections cancels the shared $d$ and leaves a difference of matrix parts, which is $C^\infty$-linear. The reusable principle is that a covariant derivative is an *affine* object whose "linear part" is the tensor $A$ relative to a chosen flat background; whenever one needs a genuine tensor out of connection data, one forms a *difference* — of two connections, of a connection with a fixed reference, or of a connection with its own value under a gauge transformation. This is the mechanism behind the second-fundamental-form tensor, the difference tensor of two metrics' Levi-Civita connections, and the gauge potential's transformation law.

**Christoffel symbols are the connection matrix of the Levi-Civita connection relative to the chart's flat connection, and their non-tensoriality is the frame-dependence of that flat reference.** The sphere computation makes concrete a fact that is often stated abstractly: the array $\Gamma^i_{kj}$ is literally the matrix $A^i{}_j = \sum_k \Gamma^i_{kj}\,dx^k$ of the tangent-bundle connection in the coordinate frame. Individually the $\Gamma$'s are not tensor components because the object they encode is a *difference against the chart's own flat connection $d$*, and that reference changes when the chart changes, injecting the second-derivative inhomogeneous term into their transformation law. But against a *fixed* chart, the difference $\nabla^{\mathrm{LC}} - d$ is a perfectly good $\operatorname{End}(TU)$-valued $1$-form. The transferable diagnostic: whenever a "connection-like" array transforms inhomogeneously, look for the hidden flat reference it is being compared against; fix that reference and the inhomogeneity disappears, revealing a tensor. This is also the cleanest way to see why curvature — built from $\nabla$ in a way that cancels the reference — is a tensor while the connection itself is not, and it is the conceptual seed of the whole gauge-theoretic viewpoint, in which the connection is a potential and only its differences and curvature are invariant data.
