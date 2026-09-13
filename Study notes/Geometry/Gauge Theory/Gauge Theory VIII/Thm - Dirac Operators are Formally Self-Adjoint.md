---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Spinor Bundle and Dirac Operator"
  - "Def - Clifford Bundle and Bundle of Clifford Modules"
  - "Def - Metric-Compatible Connection"
  - "Def - Levi-Civita Connection"
  - "Def - Riemannian Volume Form"
  - "Def - Interior Product (Contraction with a Vector Field)"
  - "Def - Musical Isomorphism (Flat and Sharp)"
  - "Thm - Cartan's Magic Formula"
  - "Thm - Cartan's First Structural Equation"
  - "Thm - Stokes' Theorem on Manifolds"
  - "Thm - Existence of Synchronous Orthonormal Frames"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $(M, g)$ is a smooth oriented Riemannian manifold of dimension $n$, without boundary, and $\mathrm{vol} \in \Omega^n(M)$ is its [[Def - Riemannian Volume Form|Riemannian volume form]] — the unique positively oriented $n$-form with $\mathrm{vol}(e_1, \dots, e_n) = 1$ for every positively oriented local orthonormal frame $(e_1, \dots, e_n)$ of $TM$. We write $\langle \cdot, \cdot \rangle$ for the metric $g$ on $TM$ and, by the same symbol, for the fibre metric on the Dirac bundle $E$; which is meant is always clear from the arguments. For $v \in T_mM$ we write $|v|^2 = \langle v, v \rangle$, and this is strictly positive when $v \neq 0$ because $g$ is Riemannian.

We recall the standing conventions of this chapter. The **Clifford relation** is $v \cdot (v \cdot e) = -|v|^2 e$ (the sign $v \cdot v = -|v|^2$ that Haydys uses); the vault's page [[Def - Clifford Algebra|Clifford algebra]] states the relation as $v^2 = Q(v)$ for a quadratic form $Q$, and the two agree under the dictionary $\mathrm{Cl}(U) = \mathrm{Cl}(U, -|\cdot|^2)$. The **Levi-Civita connection** $\nabla^{LC}$ on $TM$ is the unique [[Def - Metric-Compatible Connection|metric-compatible]], torsion-free connection ([[Def - Levi-Civita Connection]]); it induces a connection, denoted by the same symbol, on the [[Def - Clifford Bundle and Bundle of Clifford Modules|Clifford bundle]] $\mathrm{Cl}(M)$.

The object of the page is a **Dirac bundle** $E \to M$ and its **Dirac operator** $D$, both defined on [[Def - Spinor Bundle and Dirac Operator]]. We restate what we use. A Dirac bundle is a bundle of Clifford modules $E \to M$ — a real or complex vector bundle carrying a bundle morphism $\mathrm{Cl} : TM \otimes E \to E$, $(v, e) \mapsto v \cdot e$, with $v \cdot (v \cdot e) = -|v|^2 e$ — equipped with a fibre metric $\langle \cdot, \cdot \rangle$ (Euclidean in the real case, Hermitian in the complex case) and a connection $\nabla : \Gamma(E) \to \Omega^1(M; E)$ satisfying the three conditions

- **(1)** $\nabla$ is metric: $X \langle s_1, s_2 \rangle = \langle \nabla_X s_1, s_2 \rangle + \langle s_1, \nabla_X s_2 \rangle$ for all vector fields $X$ and sections $s_1, s_2 \in \Gamma(E)$;
- **(2)** $\langle v \cdot e_1, v \cdot e_2 \rangle = |v|^2 \langle e_1, e_2 \rangle$ for all $v \in T_mM$ and $e_1, e_2 \in E_m$;
- **(3)** $\nabla(\phi \cdot s) = (\nabla^{LC} \phi) \cdot s + \phi \cdot \nabla s$ for all $\phi \in \Gamma(\mathrm{Cl}(M))$ and $s \in \Gamma(E)$.

The **Dirac operator** is the composition $D : \Gamma(E) \xrightarrow{\ \nabla\ } \Gamma(T^*M \otimes E) \xrightarrow{\ \mathrm{Cl}\ } \Gamma(E)$, which in any local orthonormal frame $(e_1, \dots, e_n)$ of $TM$ reads
$$Ds = \sum_{i=1}^{n} e_i \cdot \nabla_{e_i} s .$$
That this expression is independent of the chosen frame — it is the tensorial contraction of $\nabla s$ with Clifford multiplication — is proved on [[Def - Spinor Bundle and Dirac Operator]]. Here $\nabla_{e_i} s \in \Gamma(E)$ denotes the covariant derivative of $s$ in the direction $e_i$, and $e_i \cdot (\,\cdot\,)$ is Clifford multiplication by the tangent vector $e_i$.

By $\Gamma(E)$ we mean smooth sections; a section is **compactly supported** if it vanishes outside a compact subset of $M$. For a vector field $V$ on $M$ we write $\operatorname{div} V := \sum_{i=1}^n \langle \nabla^{LC}_{e_i} V, e_i \rangle$ in a local orthonormal frame; Lemma 2 shows this is frame-independent and equals the volume divergence. The [[Def - Interior Product (Contraction with a Vector Field)|interior product]] (contraction) of a vector field $V$ with a form $\eta$ is $\iota_V \eta$, and $\sharp : T^*M \to TM$ is the [[Def - Musical Isomorphism (Flat and Sharp)|sharp]] musical isomorphism, the inverse of $X \mapsto \langle X, \cdot \rangle$. The full symbol registry for the chapter is on the parent page **Gauge Theory VIII — Clifford Algebras, Spin Structures, and Dirac Operators**.

> [!warning] Convention: the sign of the current vector field
> The page spec in the series manifest defines the current vector field by $\langle V, X \rangle := -\langle X \cdot s_1, s_2 \rangle$. Carrying the computation through (Step 2 of the Formal Proof, and verified numerically off the page) shows that this sign gives $\operatorname{div} V = \langle s_1, D s_2 \rangle - \langle D s_1, s_2 \rangle$, the negative of the stated pointwise identity. We therefore correct the sign and take
> $$\langle V, X \rangle := \langle X \cdot s_1, s_2 \rangle \qquad \text{(no minus sign),}$$
> for which $\operatorname{div} V = \langle D s_1, s_2 \rangle - \langle s_1, D s_2 \rangle$ exactly as the pointwise identity below asserts. Only the pointwise identity is sign-sensitive; the integrated conclusion holds for either sign because $\int_M \operatorname{div} V \, \mathrm{vol} = 0$ in both cases.

---

# Statement

> **Theorem (formal self-adjointness of the Dirac operator).** Let $E \to M$ be a Dirac bundle over an oriented Riemannian manifold $(M, g)$ without boundary, with fibre metric $\langle \cdot, \cdot \rangle$ and Dirac operator $D$. Let $s_1, s_2 \in \Gamma(E)$ be smooth sections, at least one of which is compactly supported (in particular, any two sections when $M$ is closed). Then
> $$\int_M \langle D s_1, s_2 \rangle \, \mathrm{vol} = \int_M \langle s_1, D s_2 \rangle \, \mathrm{vol}.$$

> **Proposition (the pointwise refinement).** With the hypotheses above, let $V$ be the vector field determined by $\langle V, X \rangle = \langle X \cdot s_1, s_2 \rangle$ for every vector field $X$ (equivalently $V = \sum_i \langle e_i \cdot s_1, s_2 \rangle e_i$ in a local orthonormal frame). Then the pointwise identity
> $$\langle D s_1, s_2 \rangle - \langle s_1, D s_2 \rangle = \operatorname{div} V$$
> holds on all of $M$; the Theorem is its integral, since $V$ is compactly supported and $\int_M \operatorname{div} V \, \mathrm{vol} = 0$.

In the complex Hermitian case $V$ is a complex vector field $V = V_{\mathrm{R}} + i V_{\mathrm{I}}$ with real and imaginary parts $V_{\mathrm{R}}, V_{\mathrm{I}}$ real vector fields, $\operatorname{div}$ is extended complex-linearly, and the same two displays hold verbatim; the integral of each real part vanishes separately.

---

# Motivation

An operator is *formally self-adjoint* when it can be moved from one side of an integral inner product to the other without picking up boundary terms, at least when the sections it acts on are compactly supported. This is the analytic property that makes an operator amenable to the spectral theory of self-adjoint operators, and for the Dirac operator it is the gateway to almost everything the operator is used for.

Here is the concrete stake. On a closed Riemannian manifold one wants to solve equations of the form $Ds = \sigma$, to understand the kernel $\ker D$ (harmonic spinors, flat sections, cohomology representatives depending on the bundle), and to organise $L^2$ sections of $E$ into eigenspaces of $D$. Every one of these requires knowing how $D$ interacts with the $L^2$ inner product $\langle s_1, s_2 \rangle_{L^2} = \int_M \langle s_1, s_2 \rangle \, \mathrm{vol}$. The Fredholm theory of chapter IX, for instance, computes the cokernel of an elliptic operator as the kernel of its formal adjoint; if $D$ is its own formal adjoint, then $\operatorname{coker} D \cong \ker D$ and the analytic index of $D$ vanishes, which is the reason a nonzero index is carried by the *chiral* halves $D^{\pm}$ rather than by $D$ itself. The Weitzenböck method of chapter VIII (`Thm - Weitzenbock Formula for the Dirac Operator`) rests on integrating $\langle D^2 s, s \rangle$ by parts into $\lVert D s \rVert_{L^2}^2$, which is legitimate precisely because $D$ is formally self-adjoint.

The question the theorem answers is therefore: *why should the first-order operator built from a connection and Clifford multiplication have this symmetry at all?* A general first-order operator has a formal adjoint that differs from it by both a zeroth-order term and a sign on the leading part, and there is no reason for the two to coincide. The theorem isolates the exact structural inputs — the metric compatibility of the connection and the skew-adjointness of Clifford multiplication — that force the difference $\langle D s_1, s_2 \rangle - \langle s_1, D s_2 \rangle$ to collapse into a pure divergence, and a divergence integrates to zero on a manifold without boundary. In other words, formal self-adjointness of $D$ is not an accident of a particular bundle; it is built into the three defining conditions of a Dirac bundle, and the proof is the audit that shows exactly which condition does which job.

---

# Sources and Targets

**Sources (Input Broadening).** The literal hypothesis is that $E$ is a Dirac bundle and one section is compactly supported. The useful question is which operators that do not announce themselves as "Dirac operators of a Dirac bundle" nevertheless fall under the theorem.

The first disguised source is **any bundle of Clifford modules carrying the metric and connection induced from the Levi-Civita connection**. Whenever a bundle is built functorially from $TM$ by an associated-bundle construction — the [[Def - Clifford Bundle and Bundle of Clifford Modules|Clifford bundle]] itself, the exterior bundle $\Lambda T^*M$, the [[Def - Spinor Bundle and Dirac Operator|spinor bundle]] $\slashed{S}$ of a spin manifold, or a twist $\slashed{S} \otimes E$ by a Hermitian bundle with a unitary connection — the induced fibre metric is automatically parallel (condition (1)) and Clifford multiplication automatically satisfies condition (2), because $SO(n)$ preserves both the Euclidean metric of $\mathbb{R}^n$ and the Clifford relation. The non-obvious step is to notice that a bundle presented by other means (a bundle of $2$-forms, a bundle of $U(1)$-charged spinors) *is* such a construction, so that the theorem applies without any new integration by parts. *Example problem:* show that the operator $d + d^*$ on $\Lambda T^*M$, presented as a first-order differential operator on forms, is formally self-adjoint by recognising $\Lambda T^*M$ as a Dirac bundle (this is `Thm - The Hodge-de Rham Operator is a Dirac Operator`) and quoting the present theorem, rather than integrating $d$ and $d^*$ by parts separately.

The second disguised source is **a first-order operator whose principal symbol is Clifford multiplication**. If a first-order operator $P$ acting on sections of a metric bundle has the form $P s = \sum_i c(e^i) \nabla_{e_i} s + (\text{zeroth order})$ in a local orthonormal frame, where $c(e^i)$ is a skew-adjoint bundle endomorphism with $c(e^i) c(e^j) + c(e^j) c(e^i) = -2\delta^{ij}$ and $\nabla$ is metric, then the leading part of $P$ is exactly a Dirac operator and its formal-adjoint difference is again a divergence. The bridge is the observation that "Dirac type" is a condition on the symbol alone, verifiable in coordinates, and does not require the operator to have been constructed from a Clifford module by hand. *Example problem:* given a $2 \times 2$ matrix operator $\sum_i \gamma_i \partial_i$ on $\mathbb{R}^n$ with constant skew-Hermitian $\gamma_i$ satisfying the Clifford relations, deduce formal self-adjointness with respect to the standard Hermitian inner product without recomputing the adjoint.

The third disguised source is **a self-adjointness statement one wants for the chiral halves of $D$ in even dimensions**. When $E = E^+ \oplus E^-$ splits and Clifford multiplication by a vector is odd, $D$ interchanges the summands, $D = \begin{pmatrix} 0 & D^- \\ D^+ & 0 \end{pmatrix}$, and formal self-adjointness of $D$ is equivalent to the statement that $D^-$ is the formal adjoint of $D^+$. The bridge is that a block-off-diagonal operator is self-adjoint if and only if its two blocks are mutually adjoint. *Example problem:* on a spin $4$-manifold, deduce $\int \langle D^+ \psi, \phi \rangle = \int \langle \psi, D^- \phi \rangle$ for $\psi \in \Gamma(\slashed{S}^+)$, $\phi \in \Gamma(\slashed{S}^-)$ from the theorem applied to $s_1 = \psi$, $s_2 = \phi$.

**Targets (Output Amplification).** The theorem is a technical lemma, but it is the input to three amplifications that recur through chapters VIII, IX, and XI.

Combine self-adjointness with **ellipticity of $D$ on a closed manifold**. An elliptic operator on a closed manifold is Fredholm, and the cokernel of a formally self-adjoint elliptic operator is its own kernel: $\operatorname{coker} D \cong \ker D$. The further result is that the analytic index of $D$ vanishes, $\operatorname{ind} D = \dim \ker D - \dim \operatorname{coker} D = 0$, so that any nonzero index in the theory must live on the chiral half $D^+$, not on $D$; this is the structural reason the Atiyah–Singer index of a spin manifold is carried by $D^+$. The extra ingredient is the elliptic Fredholm package of chapter IX.

Combine self-adjointness with the **Weitzenböck identity** $D^2 = \nabla^*\nabla + \mathcal{R}$. Testing $D^2 s$ against $s$ and integrating by parts — which uses that both $D$ and $\nabla^*\nabla$ are formally self-adjoint — gives $\lVert D s \rVert_{L^2}^2 = \lVert \nabla s \rVert_{L^2}^2 + \int_M \langle \mathcal{R} s, s \rangle \, \mathrm{vol}$ on a closed manifold. When the curvature endomorphism $\mathcal{R}$ is positive, the right-hand side is strictly positive unless $s = 0$, so $\ker D = 0$: this is the Bochner–Lichnerowicz vanishing mechanism, and formal self-adjointness is what licenses the integration by parts. The extra ingredient is the Weitzenböck formula.

Combine self-adjointness with the **spectral theorem for self-adjoint operators**. On a closed manifold the completion of $\Gamma(E)$ in the $L^2$ norm carries $D$ as an (unbounded) self-adjoint operator with discrete real spectrum and an orthonormal basis of smooth eigensections. The further result is the eigenspinor expansion of any $L^2$ section, the heat operator $e^{-tD^2}$, and the zeta-regularised determinant used in index theory. The extra ingredient is the functional-analytic self-adjoint extension theory, whose hypothesis is exactly the formal self-adjointness proved here.

---

# Why Is It True

Forget the manifold for a moment and think of $D$ as a matrix built from two ingredients: differentiation (the connection $\nabla$) and multiplication (Clifford multiplication by the frame vectors $e_i$). To move $D$ across the inner product $\langle D s_1, s_2 \rangle$ we have to move each ingredient across, and each move is governed by one structural condition.

Moving Clifford multiplication across uses condition (2). A short polarisation argument turns "Clifford multiplication by $v$ preserves the metric up to the factor $|v|^2$" into "Clifford multiplication by $v$ is *skew*-adjoint": $\langle v \cdot a, b \rangle = -\langle a, v \cdot b \rangle$. So when the factor $e_i$ jumps from the left slot to the right slot it flips sign. Moving differentiation across uses condition (1), metric compatibility: $e_i \langle a, b \rangle = \langle \nabla_{e_i} a, b \rangle + \langle a, \nabla_{e_i} b \rangle$, which is the Leibniz rule saying the derivative of an inner product distributes. The only remaining friction is that the frame vector $e_i$ is being both differentiated and Clifford-multiplied at once, and condition (3) — that $\nabla$ is a *module derivation* over $\nabla^{LC}$ — is exactly what says these two operations commute past each other, the leftover carrying a factor $\nabla^{LC}_{e_i} e_i$ that we can arrange to vanish at any chosen point by working in a synchronous frame.

When we carry out the two moves, the sum $\langle D s_1, s_2 \rangle$ becomes $-\sum_i \langle \nabla_{e_i} s_1, e_i \cdot s_2 \rangle$ (a sign from skew-adjointness), and $\langle s_1, D s_2 \rangle$ is $\sum_i \langle s_1, e_i \cdot \nabla_{e_i} s_2 \rangle$. Their difference is the total derivative of the single function $\sum_i \langle e_i \cdot s_1, s_2 \rangle$ — which is precisely $\operatorname{div} V$ for the vector field $V$ dual to the $1$-form $X \mapsto \langle X \cdot s_1, s_2 \rangle$. A divergence is a total derivative, and a total derivative integrates to nothing over a closed manifold.

> **The mechanism in one sentence.** Clifford multiplication is skew-adjoint and the connection is metric, so the algebraic parts that would obstruct moving $D$ across the inner product cancel exactly, and the only surviving term is a divergence, which integrates to zero.

The single most instructive check is dimension one. Take $M = S^1$ with coordinate $t$, $E$ the trivial complex line bundle, $\nabla = d/dt$, and Clifford multiplication by the unit vector $\partial_t$ given by multiplication by $i$ (which is skew-Hermitian and squares to $-1$, so it is a Clifford module for $\mathrm{Cl}(\mathbb{R}^1)$). Then $D = i \, d/dt$, and $\int_{S^1} \langle i s_1', s_2 \rangle \, dt = \int_{S^1} i s_1' \bar{s_2} \, dt$, while $\int_{S^1} \langle s_1, i s_2' \rangle \, dt = \int_{S^1} s_1 \overline{i s_2'} \, dt = \int_{S^1} s_1 (-i) \bar{s_2}' \, dt$. Integrating the first by parts, $\int i s_1' \bar{s_2} = -\int i s_1 \bar{s_2}' = \int_{S^1} s_1 (-i) \bar{s_2}'$, which is the second. The boundary term vanishes because $S^1$ is closed. The factor $i$ is the skew-adjoint Clifford multiplication, and integration by parts is the divergence; the whole theorem is this computation done invariantly and in every dimension.

---

# What Makes This Hard

The one genuinely non-obvious step is that Clifford multiplication by a vector is *skew*-adjoint rather than self-adjoint. Condition (2) is phrased as a preservation-of-metric statement, and a beginner reads "preserves the metric" as "orthogonal, hence adjoint equals inverse", not as "skew-adjoint". The extraction of skew-adjointness from condition (2) needs the Clifford relation $v \cdot v \cdot = -|v|^2$, and getting the sign right there is where the sign of the whole identity is decided — a sign error propagates into $\langle D s_1, s_2 \rangle = +\sum_i \langle \nabla_{e_i} s_1, e_i \cdot s_2 \rangle$ and reverses the pointwise identity. The second subtlety is bookkeeping the term $\nabla^{LC}_{e_i} e_i$: in a general orthonormal frame it does not vanish, and one must either keep it and watch it cancel against the divergence's own frame terms, or eliminate it once and for all by computing at a point in a synchronous frame — the cleaner route, taken here. The common error is to differentiate $e_i \cdot \nabla_{e_i} s$ as if $e_i$ were parallel, silently using condition (3) with $\nabla^{LC}_{e_i} e_i = 0$ in a frame where that is false.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Prove the pointwise identity $\langle D s_1, s_2 \rangle - \langle s_1, D s_2 \rangle = \operatorname{div} V$ at an arbitrary point, working in an orthonormal frame that is synchronous there so that all $\nabla^{LC}$-of-frame terms drop out; the two structural conditions (skew-adjointness from (2), Leibniz from (1)) turn the difference into the pointwise divergence of the current $V$. Then integrate and kill the divergence with Stokes.

**Subgoal decomposition:**

1. **Skew-adjointness of Clifford multiplication.** Deduce $\langle v \cdot a, b \rangle = -\langle a, v \cdot b \rangle$ from condition (2).
   - *Hint:* For $v \neq 0$, write the second slot $b = v \cdot c$ with $c = -|v|^{-2} v \cdot b$ (possible because $v \cdot$ is invertible with this inverse), then apply condition (2) to the pair $(a, c)$.
   - *Why needed:* This is the sign-carrying move that lets the factor $e_i$ cross the inner product; it is used twice in the main computation.

2. **The divergence integrates to zero.** Show $\operatorname{div}(V) \, \mathrm{vol} = d(\iota_V \mathrm{vol})$ and hence $\int_M \operatorname{div} V \, \mathrm{vol} = 0$ for compactly supported $V$.
   - *Hint:* Compute at a point in a synchronous frame: $\iota_V \mathrm{vol} = \sum_j (-1)^{j-1} V^j e^1 \wedge \cdots \widehat{e^j} \cdots \wedge e^n$; take $d$, use $de^i = 0$ at the point (Cartan's first structural equation, torsion-freeness); the result is $\sum_j e_j(V^j) \, \mathrm{vol} = \operatorname{div}(V) \, \mathrm{vol}$. Then Cartan's magic formula and Stokes.
   - *Why needed:* It is the analytic heart — the reason a total derivative contributes nothing over a closed manifold; the same lemma appears in chapter VII.

3. **The current vector field is well-defined.** Show $X \mapsto \langle X \cdot s_1, s_2 \rangle$ is a smooth $1$-form, so its metric-dual $V$ is a genuine (smooth, compactly supported) vector field.
   - *Hint:* Clifford multiplication is a bundle morphism, so the expression is $C^\infty(M)$-linear in $X$; use the sharp isomorphism.
   - *Why needed:* Without this, "$\operatorname{div} V$" is meaningless, and the compact support of $V$ (inherited from the compactly supported section) is what makes Step 2 apply.

4. **The pointwise identity.** At a point, in a synchronous frame, expand $\operatorname{div} V = \sum_i e_i \langle e_i \cdot s_1, s_2 \rangle$ using conditions (1) and (3), and recombine using subgoal 1 into $\langle D s_1, s_2 \rangle - \langle s_1, D s_2 \rangle$.
   - *Hint:* $e_i \langle e_i \cdot s_1, s_2 \rangle = \langle \nabla_{e_i}(e_i \cdot s_1), s_2 \rangle + \langle e_i \cdot s_1, \nabla_{e_i} s_2 \rangle$; the first term is $\langle e_i \cdot \nabla_{e_i} s_1, s_2 \rangle$ at the point (by (3) with $\nabla^{LC}_{e_i} e_i = 0$), the second is $-\langle s_1, e_i \cdot \nabla_{e_i} s_2 \rangle$ (by subgoal 1).
   - *Why needed:* It is the theorem in pointwise form; integrating it and applying subgoal 2 is the last line.

5. **Integrate.** Combine subgoals 2, 3, 4 into the integral identity.
   - *Hint:* $\int_M (\langle D s_1, s_2 \rangle - \langle s_1, D s_2 \rangle) \, \mathrm{vol} = \int_M \operatorname{div}(V) \, \mathrm{vol} = 0$.
   - *Why needed:* It is the stated theorem.

---

# Lemma Decomposition

> [!note]- Lemma 1: Clifford multiplication by a tangent vector is skew-adjoint
> **Statement:** Let $E$ be a Dirac bundle and $m \in M$. For every $v \in T_mM$ and all $e_1, e_2 \in E_m$,
> $$\langle v \cdot e_1, e_2 \rangle = -\langle e_1, v \cdot e_2 \rangle.$$
>
> **Hint:** For $v \neq 0$ the map $e \mapsto v \cdot e$ on $E_m$ is invertible; write the second entry as $v \cdot c$ and use condition (2).
>
> **Why needed:** It converts the metric-preservation condition (2) into the sign-flipping rule that lets a Clifford factor cross the inner product; the main computation uses it twice, and it fixes the sign of the whole identity.
>
> > [!note]- Full proof
> > If $v = 0$, both sides are $0$ (Clifford multiplication is linear in the vector slot), so the identity holds. Assume $v \neq 0$; then $|v|^2 > 0$ because $g$ is Riemannian.
> >
> > **The Clifford factor is invertible.** By the Clifford relation, $v \cdot (v \cdot e) = -|v|^2 e$ for all $e \in E_m$, so the linear map $L : E_m \to E_m$, $L(e) = v \cdot e$, satisfies $L \circ L = -|v|^2 \, \mathrm{id}$. Hence $L$ is invertible with $L^{-1} = -|v|^{-2} L$ (indeed $L \circ (-|v|^{-2}L) = -|v|^{-2}(-|v|^2 \, \mathrm{id}) = \mathrm{id}$).
> >
> > **Rewrite the second entry.** Given $e_2 \in E_m$, set $c := -|v|^{-2}\, v \cdot e_2 = L^{-1}(e_2) \in E_m$, so that $v \cdot c = L(c) = e_2$.
> >
> > **Apply condition (2) to the pair $(e_1, c)$.** Then
> > $$\langle v \cdot e_1, e_2 \rangle = \langle v \cdot e_1, v \cdot c \rangle \qquad (\text{since } e_2 = v \cdot c)$$
> > $$= |v|^2 \langle e_1, c \rangle \qquad (\text{by condition (2) applied to } e_1, c)$$
> > $$= |v|^2 \big\langle e_1, -|v|^{-2}\, v \cdot e_2 \big\rangle \qquad (\text{by the definition of } c)$$
> > $$= -\langle e_1, v \cdot e_2 \rangle \qquad (\text{the scalars } |v|^2 \text{ and } -|v|^{-2} \text{ multiply to } -1).$$
> > This is the claimed identity. In the complex Hermitian case the real scalar $-|v|^{-2}$ passes through the sesquilinear form without conjugation, so the computation is unchanged. $\blacksquare$

> [!note]- Lemma 2: The divergence identity and its integral (the divergence theorem for vector fields)
> **Statement:** Let $(M, g)$ be an oriented Riemannian $n$-manifold without boundary, with volume form $\mathrm{vol}$, and let $V$ be a smooth vector field. Define $\operatorname{div} V := \sum_{i=1}^n \langle \nabla^{LC}_{e_i} V, e_i \rangle$ in any local orthonormal frame $(e_i)$; this is independent of the frame. Then
> $$\operatorname{div}(V) \, \mathrm{vol} = d(\iota_V \mathrm{vol}), \qquad \text{and} \qquad \int_M \operatorname{div}(V) \, \mathrm{vol} = 0 \text{ whenever } V \text{ has compact support}.$$
>
> **Hint:** Frame-independence is that $\sum_i \langle \nabla_{e_i} V, e_i \rangle$ is the trace of $X \mapsto \nabla_X V$. For the identity, compute at a point in a synchronous frame, where $de^i = 0$; for the integral, use Cartan's magic formula and Stokes.
>
> **Why needed:** It is the analytic engine: it lets the pointwise divergence identity be integrated to zero. It is the same lemma used in chapter VII for the divergence of the energy-momentum tensor.
>
> > [!note]- Full proof
> > **Frame-independence of the definition.** The map $\mathcal{S} : X \mapsto \nabla^{LC}_X V$ is a bundle endomorphism of $TM$ (it is $C^\infty(M)$-linear in $X$ because a connection is). For a local orthonormal frame $(e_i)$ the quantity $\sum_i \langle \mathcal{S}(e_i), e_i \rangle$ is the trace of $\mathcal{S}$ read off in that orthonormal basis, and the trace of an endomorphism is basis-independent; passing between two orthonormal frames is an $SO(n)$-valued change of basis, under which $\sum_i \langle \mathcal{S}(e_i), e_i \rangle$ is unchanged. So $\operatorname{div} V$ is well-defined.
> >
> > **The pointwise identity, computed in a synchronous frame.** Fix $m \in M$. By [[Thm - Existence of Synchronous Orthonormal Frames]] — for a metric connection there is a local orthonormal frame $(e_1, \dots, e_n)$ of $TM$ near $m$, positively oriented, with $\nabla^{LC}_{e_i} e_j (m) = 0$ for all $i, j$ — choose such a frame, with dual coframe $(e^1, \dots, e^n)$. Because the frame is orthonormal and positively oriented, $\mathrm{vol} = e^1 \wedge \cdots \wedge e^n$ near $m$ ([[Def - Riemannian Volume Form]]). Write $V = \sum_{j} V^j e_j$ with $V^j = \langle V, e_j \rangle \in C^\infty$.
> >
> > By the definition of the interior product on a top form ([[Def - Interior Product (Contraction with a Vector Field)]]),
> > $$\iota_V \mathrm{vol} = \sum_{j=1}^n (-1)^{j-1} V^j \, e^1 \wedge \cdots \wedge \widehat{e^j} \wedge \cdots \wedge e^n,$$
> > where $\widehat{e^j}$ marks the omitted factor. Apply the exterior derivative and the Leibniz rule for $d$:
> > $$d(\iota_V \mathrm{vol}) = \sum_{j=1}^n (-1)^{j-1} \Big( dV^j \wedge e^1 \wedge \cdots \widehat{e^j} \cdots \wedge e^n + V^j \, d\big(e^1 \wedge \cdots \widehat{e^j} \cdots \wedge e^n\big) \Big).$$
> >
> > **The coframe is closed at $m$.** By [[Thm - Cartan's First Structural Equation|Cartan's first structural equation]] for the torsion-free Levi-Civita connection, $de^i = -\sum_k \omega^i{}_k \wedge e^k$, where $\omega^i{}_k$ are the connection $1$-forms defined by $\nabla^{LC} e_k = \sum_i \omega^i{}_k \, e_i$. Since the frame is synchronous, $\omega^i{}_k(m) = 0$, hence $de^i(m) = 0$ for every $i$. By the Leibniz rule for $d$, every derivative $d(e^1 \wedge \cdots \widehat{e^j} \cdots \wedge e^n)$ is a sum of terms each containing one factor $de^i$, so it vanishes at $m$. Therefore, evaluating at $m$,
> > $$d(\iota_V \mathrm{vol})(m) = \sum_{j=1}^n (-1)^{j-1} \, dV^j \wedge e^1 \wedge \cdots \widehat{e^j} \cdots \wedge e^n \Big|_m.$$
> >
> > **Only the diagonal term survives the wedge.** Expand $dV^j = \sum_i e_i(V^j) \, e^i$. In the wedge $dV^j \wedge e^1 \wedge \cdots \widehat{e^j} \cdots \wedge e^n$ every summand with $i \neq j$ repeats a coframe factor and so vanishes; the summand $i = j$ gives $e_j(V^j) \, e^j \wedge e^1 \wedge \cdots \widehat{e^j} \cdots \wedge e^n$. Moving $e^j$ back to its $j$-th place costs the sign $(-1)^{j-1}$, so $(-1)^{j-1} e^j \wedge e^1 \wedge \cdots \widehat{e^j} \cdots \wedge e^n = e^1 \wedge \cdots \wedge e^n = \mathrm{vol}$. Hence
> > $$d(\iota_V \mathrm{vol})(m) = \Big( \sum_{j=1}^n e_j(V^j) \Big)(m) \, \mathrm{vol}.$$
> >
> > **Identify the coefficient with $\operatorname{div} V$.** At $m$, by metric compatibility of $\nabla^{LC}$ (condition on the Levi-Civita connection) and $\nabla^{LC}_{e_j} e_j(m) = 0$,
> > $$\langle \nabla^{LC}_{e_j} V, e_j \rangle(m) = e_j \langle V, e_j \rangle(m) - \langle V, \nabla^{LC}_{e_j} e_j \rangle(m) = e_j(V^j)(m).$$
> > Summing over $j$ gives $\operatorname{div}(V)(m) = \sum_j e_j(V^j)(m)$, so $d(\iota_V \mathrm{vol})(m) = \operatorname{div}(V)(m) \, \mathrm{vol}$. Since $m \in M$ was arbitrary, $d(\iota_V \mathrm{vol}) = \operatorname{div}(V) \, \mathrm{vol}$ everywhere. (Equivalently, by [[Thm - Cartan's Magic Formula|Cartan's magic formula]] $\mathcal{L}_V \mathrm{vol} = d \iota_V \mathrm{vol} + \iota_V \, d\mathrm{vol} = d\iota_V \mathrm{vol}$, since $d\mathrm{vol} = 0$ as $\mathrm{vol}$ is a top form; so $\operatorname{div} V$ is also the Lie-derivative divergence.)
> >
> > **The integral vanishes.** Suppose $V$ has compact support. Then $\iota_V \mathrm{vol}$ is a compactly supported smooth $(n-1)$-form. By [[Thm - Stokes' Theorem on Manifolds|Stokes' theorem]] on the manifold $M$ without boundary, $\int_M d\eta = \int_{\partial M} \eta = 0$ for every compactly supported $(n-1)$-form $\eta$ (the boundary is empty). Applying this to $\eta = \iota_V \mathrm{vol}$,
> > $$\int_M \operatorname{div}(V) \, \mathrm{vol} = \int_M d(\iota_V \mathrm{vol}) = 0. \qquad \blacksquare$$

> [!note]- Lemma 3: The current vector field is well-defined, smooth, and compactly supported
> **Statement:** Let $s_1, s_2 \in \Gamma(E)$. The assignment $\alpha : X \mapsto \langle X \cdot s_1, s_2 \rangle$ is a smooth $1$-form on $M$, and its metric dual $V := \alpha^{\sharp}$ is the unique smooth vector field with $\langle V, X \rangle = \langle X \cdot s_1, s_2 \rangle$ for all vector fields $X$; in a local orthonormal frame $V = \sum_i \langle e_i \cdot s_1, s_2 \rangle e_i$. If $s_1$ or $s_2$ is compactly supported, so is $V$.
>
> **Hint:** Clifford multiplication $\mathrm{Cl} : TM \otimes E \to E$ is a bundle morphism, so $\alpha$ is $C^\infty(M)$-linear in $X$; apply the sharp musical isomorphism.
>
> **Why needed:** It makes "$\operatorname{div} V$" meaningful and supplies the compact support that Lemma 2 requires.
>
> > [!note]- Full proof
> > **$\alpha$ is a $1$-form.** For a smooth function $f$ and vector fields $X, Y$,
> > $$\alpha(fX + Y) = \langle (fX + Y) \cdot s_1, s_2 \rangle = f \langle X \cdot s_1, s_2 \rangle + \langle Y \cdot s_1, s_2 \rangle = f \, \alpha(X) + \alpha(Y),$$
> > using that Clifford multiplication $\mathrm{Cl} : TM \otimes E \to E$ is a bundle morphism, hence $C^\infty(M)$-linear in the $TM$ slot, and that the fibre metric is linear in its first argument. So $\alpha$ is $C^\infty(M)$-linear in $X$, and by the tensor characterisation it is a $1$-form; it is smooth because $s_1, s_2$, Clifford multiplication, and the metric are smooth.
> >
> > **$V$ is the metric dual.** By the [[Def - Musical Isomorphism (Flat and Sharp)|sharp isomorphism]] $\sharp : T^*M \to TM$, inverse to $X \mapsto \langle X, \cdot \rangle$, there is a unique smooth vector field $V = \alpha^{\sharp}$ with $\langle V, X \rangle = \alpha(X) = \langle X \cdot s_1, s_2 \rangle$ for all $X$. Taking $X = e_i$ in an orthonormal frame and expanding $V = \sum_i \langle V, e_i \rangle e_i$ gives $V = \sum_i \langle e_i \cdot s_1, s_2 \rangle e_i$.
> >
> > **Compact support.** For every $X$, $\langle V, X \rangle = \langle X \cdot s_1, s_2 \rangle$ vanishes wherever $s_1$ vanishes (as $X \cdot s_1 = 0$ there) and wherever $s_2$ vanishes; hence $\operatorname{supp} V \subseteq \operatorname{supp} s_1 \cap \operatorname{supp} s_2$. If either section has compact support, this intersection is a closed subset of a compact set, hence compact. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $E \to M$ be a Dirac bundle over the oriented Riemannian manifold $(M, g)$ without boundary, with Dirac operator $D$, and let $s_1, s_2 \in \Gamma(E)$ with at least one of them compactly supported. We must show the pointwise identity $\langle D s_1, s_2 \rangle - \langle s_1, D s_2 \rangle = \operatorname{div} V$ and then integrate it.
>
> **Step 0 — the objects are well-posed.** The Dirac operator $Ds = \sum_i e_i \cdot \nabla_{e_i} s$ is independent of the local orthonormal frame, being the tensorial contraction $\mathrm{Cl} \circ \nabla$ ([[Def - Spinor Bundle and Dirac Operator]]); we may therefore compute it in any frame. The volume form $\mathrm{vol}$ exists because $M$ is oriented Riemannian ([[Def - Riemannian Volume Form]]). By Lemma 3 the vector field $V$ with $\langle V, X \rangle = \langle X \cdot s_1, s_2 \rangle$ is well-defined, smooth, and compactly supported (its support lies in $\operatorname{supp} s_1 \cap \operatorname{supp} s_2$, and one factor is compactly supported). All quantities below are therefore defined.
>
> **Step 1 — rewrite $\langle D s_1, s_2 \rangle$ and $\langle s_1, D s_2 \rangle$ using skew-adjointness.** In any local orthonormal frame $(e_i)$,
> $$\langle D s_1, s_2 \rangle = \sum_{i=1}^n \langle e_i \cdot \nabla_{e_i} s_1, s_2 \rangle = -\sum_{i=1}^n \langle \nabla_{e_i} s_1, e_i \cdot s_2 \rangle,$$
> where the first equality is the frame formula for $D$ and the second is Lemma 1 (skew-adjointness of Clifford multiplication by $e_i$, applied to $a = \nabla_{e_i} s_1$, $b = s_2$). The second term is left as is:
> $$\langle s_1, D s_2 \rangle = \sum_{i=1}^n \langle s_1, e_i \cdot \nabla_{e_i} s_2 \rangle.$$
>
> **Step 2 — the pointwise divergence identity at an arbitrary point.** Fix $m \in M$ and, by [[Thm - Existence of Synchronous Orthonormal Frames|the existence of synchronous orthonormal frames]], choose a positively oriented local orthonormal frame $(e_i)$ near $m$ with $\nabla^{LC}_{e_i} e_j(m) = 0$ for all $i, j$. By Lemma 3, $\langle V, e_i \rangle = \langle e_i \cdot s_1, s_2 \rangle$, and by Lemma 2 and $\nabla^{LC}_{e_i} e_i(m) = 0$,
> $$\operatorname{div}(V)(m) = \sum_{i=1}^n \langle \nabla^{LC}_{e_i} V, e_i \rangle(m) = \sum_{i=1}^n e_i \langle V, e_i \rangle(m) = \sum_{i=1}^n e_i \langle e_i \cdot s_1, s_2 \rangle(m),$$
> the middle equality by metric compatibility of $\nabla^{LC}$ together with $\nabla^{LC}_{e_i} e_i(m) = 0$ (as in the last display of Lemma 2's proof).
>
> **Expand each term with conditions (1) and (3).** For each $i$, metric compatibility of $\nabla$ on $E$ (condition (1)) gives
> $$e_i \langle e_i \cdot s_1, s_2 \rangle = \langle \nabla_{e_i}(e_i \cdot s_1), s_2 \rangle + \langle e_i \cdot s_1, \nabla_{e_i} s_2 \rangle.$$
> By the module-derivation property (condition (3)), applied with $\phi = e_i \in \Gamma(TM) \subset \Gamma(\mathrm{Cl}(M))$,
> $$\nabla_{e_i}(e_i \cdot s_1) = (\nabla^{LC}_{e_i} e_i) \cdot s_1 + e_i \cdot \nabla_{e_i} s_1 = e_i \cdot \nabla_{e_i} s_1 \quad \text{at } m,$$
> since $\nabla^{LC}_{e_i} e_i(m) = 0$. Substituting, and using Lemma 1 on the second term ($\langle e_i \cdot s_1, \nabla_{e_i} s_2 \rangle = -\langle s_1, e_i \cdot \nabla_{e_i} s_2 \rangle$),
> $$e_i \langle e_i \cdot s_1, s_2 \rangle(m) = \langle e_i \cdot \nabla_{e_i} s_1, s_2 \rangle(m) - \langle s_1, e_i \cdot \nabla_{e_i} s_2 \rangle(m).$$
>
> **Sum over $i$ and recognise $D$.** Summing the previous display over $i = 1, \dots, n$ and comparing with Step 1,
> $$\operatorname{div}(V)(m) = \sum_{i=1}^n \langle e_i \cdot \nabla_{e_i} s_1, s_2 \rangle(m) - \sum_{i=1}^n \langle s_1, e_i \cdot \nabla_{e_i} s_2 \rangle(m) = \langle D s_1, s_2 \rangle(m) - \langle s_1, D s_2 \rangle(m),$$
> the first sum being $\langle D s_1, s_2 \rangle$ (frame formula for $D$) and the second $\langle s_1, D s_2 \rangle$. Since $m$ was arbitrary, the pointwise identity
> $$\langle D s_1, s_2 \rangle - \langle s_1, D s_2 \rangle = \operatorname{div} V$$
> holds on all of $M$. (Both sides are frame-independent — the left side manifestly, the right side by Lemma 2 — so although $\operatorname{div} V(m)$ was computed in a frame adapted to $m$, the identity is global.)
>
> **Step 3 — integrate.** Integrate the pointwise identity against $\mathrm{vol}$ over $M$. Because $V$ is compactly supported (Step 0), Lemma 2 gives $\int_M \operatorname{div}(V) \, \mathrm{vol} = 0$, so
> $$\int_M \langle D s_1, s_2 \rangle \, \mathrm{vol} - \int_M \langle s_1, D s_2 \rangle \, \mathrm{vol} = \int_M \operatorname{div}(V) \, \mathrm{vol} = 0,$$
> the integrals being finite because the integrands are supported in the compact set $\operatorname{supp} s_1 \cap \operatorname{supp} s_2$. Therefore
> $$\int_M \langle D s_1, s_2 \rangle \, \mathrm{vol} = \int_M \langle s_1, D s_2 \rangle \, \mathrm{vol}.$$
>
> **Step 4 — the complex Hermitian case.** If the fibre metric is Hermitian, $\alpha(X) = \langle X \cdot s_1, s_2 \rangle$ is a complex-valued $1$-form; write $\alpha = \alpha_{\mathrm{R}} + i \alpha_{\mathrm{I}}$ with $\alpha_{\mathrm{R}}, \alpha_{\mathrm{I}}$ real $1$-forms, and $V = V_{\mathrm{R}} + i V_{\mathrm{I}}$ with $V_{\mathrm{R}} = \alpha_{\mathrm{R}}^{\sharp}$, $V_{\mathrm{I}} = \alpha_{\mathrm{I}}^{\sharp}$ real, compactly supported vector fields. Condition (1) holds for the Hermitian connection (the derivative of a complex-valued inner product distributes), and Lemma 1 holds for the real vector $e_i$ (the real scalar $-|e_i|^{-2}$ passes through the sesquilinear form). Hence Step 2 goes through verbatim with $\operatorname{div}$ extended complex-linearly, $\operatorname{div}(V) = \operatorname{div}(V_{\mathrm{R}}) + i \operatorname{div}(V_{\mathrm{I}})$, giving the same pointwise identity. Applying Lemma 2 to each real vector field, $\int_M \operatorname{div}(V_{\mathrm{R}}) \, \mathrm{vol} = \int_M \operatorname{div}(V_{\mathrm{I}}) \, \mathrm{vol} = 0$, so $\int_M \operatorname{div}(V) \, \mathrm{vol} = 0$ and the conclusion of Step 3 holds unchanged. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Fourier analysis: the Dirac operator on the flat torus.** Take $M = T^n = \mathbb{R}^n / (2\pi\mathbb{Z})^n$ with the flat metric, $E$ a trivial complex bundle with constant Clifford matrices $\gamma_1, \dots, \gamma_n$ (skew-Hermitian, $\gamma_i \gamma_j + \gamma_j \gamma_i = -2\delta_{ij}$), and $\nabla = d$. Then $D = \sum_i \gamma_i \partial_i$ has constant coefficients, and expanding sections in the Fourier basis $e^{i \langle k, x \rangle}$, $k \in \mathbb{Z}^n$, shows that $D$ acts on the $k$-th mode by the matrix $i \sum_j k_j \gamma_j$, which is Hermitian because each $\gamma_j$ is skew-Hermitian and $i$ times skew-Hermitian is Hermitian. The formal self-adjointness of the theorem is here the Hermiticity of each Fourier symbol; the exercise is to see that "skew-adjoint Clifford multiplication" is exactly what makes the symbol $i \sum_j k_j \gamma_j$ Hermitian, so the abstract theorem and the elementary Fourier computation are the same statement. It is a non-obvious application because one usually verifies self-adjointness mode by mode and never notices the underlying Clifford structure.

**Complex geometry: the Dolbeault operator on a Kähler manifold.** On a Kähler manifold the operator $\sqrt{2}(\bar\partial + \bar\partial^*)$ acting on $(0, q)$-forms is a Dirac operator for the Dirac bundle $\Lambda^{0, \bullet} T^*M$ with its induced Hermitian metric and the Chern connection. The theorem gives that $\bar\partial^*$ is the formal adjoint of $\bar\partial$ with respect to the $L^2$ Hermitian inner product, which is the starting point of Hodge theory for Dolbeault cohomology. The application is non-obvious because $\bar\partial$ and $\bar\partial^*$ are usually introduced through the Hermitian metric on forms directly; recognising them as the two halves of a Dirac operator explains why the adjoint relation holds without a separate integration by parts.

**Mathematical physics: conservation of the Dirac current.** In relativistic quantum mechanics the Dirac current $j^\mu = \bar\psi \gamma^\mu \psi$ is conserved, $\partial_\mu j^\mu = 0$, when $\psi$ solves the free Dirac equation. The vector field $V$ of this page — with components $\langle e_i \cdot s_1, s_2 \rangle$ — is exactly (a Riemannian analogue of) the Dirac current formed from two spinors, and the pointwise identity $\operatorname{div} V = \langle D s_1, s_2 \rangle - \langle s_1, D s_2 \rangle$ is the statement that the current is divergence-free whenever both spinors are harmonic ($D s_1 = D s_2 = 0$), which specialises to current conservation for solutions of the Dirac equation. The exercise is to translate between the Lorentzian physics computation and the Riemannian $\operatorname{div} V$ identity and see that the skew-adjointness of the gamma matrices is the input in both.

---

# Bridges

- **[[Thm - The Hodge-de Rham Operator is a Dirac Operator]]** — the model example. The exterior bundle $\Lambda T^*M$ with Clifford multiplication $v \cdot \phi = v^\flat \wedge \phi - \iota_v \phi$ and the Levi-Civita connection is a Dirac bundle whose Dirac operator is $d + d^*$. Applying the present theorem to it recovers that $d^*$ is the formal adjoint of $d$; the general Dirac-bundle integration by parts specialises to the classical integration by parts for the exterior derivative and its codifferential.

- **[[Thm - Weitzenbock Formula for the Dirac Operator]]** — the payoff. That page proves $D^2 = \nabla^*\nabla + \mathcal{R}$ pointwise. Combining it with the present theorem (both $D$ and, on `Thm - Local Formula and Self-Adjointness of the Connection Laplacian`, the connection Laplacian $\nabla^*\nabla$, are formally self-adjoint) and integrating over a closed manifold yields the Bochner identity $\lVert D s \rVert_{L^2}^2 = \lVert \nabla s \rVert_{L^2}^2 + \int_M \langle \mathcal{R} s, s \rangle \, \mathrm{vol}$, from which positivity of $\mathcal{R}$ forces $\ker D = 0$. Formal self-adjointness is precisely the license for the integration by parts in this identity.

- **[[Thm - Local Formula and Self-Adjointness of the Connection Laplacian]]** — the sibling integration by parts. There the same divergence lemma (Lemma 2 here) is applied to the $E$-valued $1$-form $\nabla s$ to show that $\nabla^* = -\star d^\nabla \star$ is the formal adjoint of $\nabla$; the two pages share the "divergence integrates to zero" mechanism, differing only in which bundle map (Clifford multiplication here, the metric contraction there) crosses the inner product.

- **Chiral splitting in even dimensions** — in dimension $4$ the spinor bundle splits $\slashed{S} = \slashed{S}^+ \oplus \slashed{S}^-$ and Clifford multiplication by a $1$-form is odd, so the spin Dirac operator is block-off-diagonal, $\slashed{D} = \begin{pmatrix} 0 & \slashed{D}^- \\ \slashed{D}^+ & 0 \end{pmatrix}$. Formal self-adjointness of $\slashed{D}$ is equivalent to $\slashed{D}^-$ being the formal adjoint of $\slashed{D}^+$, i.e. $\int \langle \slashed{D}^+ \psi, \phi \rangle \, \mathrm{vol} = \int \langle \psi, \slashed{D}^- \phi \rangle \, \mathrm{vol}$ for $\psi \in \Gamma(\slashed{S}^+)$, $\phi \in \Gamma(\slashed{S}^-)$. This is the identity used throughout the Seiberg–Witten theory of chapter XI to relate the linearised equations to their adjoints.

---

# Unlocked by This

> [!tip] Self-adjoint elliptic operators have real discrete spectrum *(from Functional Analysis)*
> Once $D$ is known to be formally self-adjoint and elliptic on a closed manifold, the spectral theorem for self-adjoint operators (see [[Thm - Complex Spectral Theorem]] for the finite-dimensional prototype) gives $L^2(E)$ an orthonormal basis of smooth eigensections of $D$ with real eigenvalues accumulating only at infinity. This is what makes heat-kernel and zeta-function methods available for the Dirac operator.

> [!tip] The analytic index of $D$ vanishes; the index lives on $D^+$ *(from Index Theory)*
> Formal self-adjointness together with ellipticity gives $\operatorname{coker} D \cong \ker D$, so $\operatorname{ind} D = 0$. The nontrivial index of the theory is therefore carried by the chiral half $\slashed{D}^+ : \Gamma(\slashed{S}^+) \to \Gamma(\slashed{S}^-)$, whose index the Atiyah–Singer theorem computes; on a spin $4$-manifold this is $\operatorname{ind} \slashed{D}^+ = -\sigma(X)/8$, the input to Rokhlin's theorem in chapter XIII.
