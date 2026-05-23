---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Curvature of a Vector-Bundle Connection"
  - "Def - Connection on a Vector Bundle"
  - "Def - The Lie Bracket of Vector Fields"
tags: [geometry, gauge-theory, curvature, tensoriality]
---

# Notation

$E \to M$ is a smooth vector bundle with a connection $\nabla$ (see [[Def - Connection on a Vector Bundle]]). For $X, Y \in \mathfrak{X}(M)$ and $\sigma \in \Gamma(E)$, the curvature operator is

$$F(X, Y)\sigma := \nabla_X\nabla_Y\sigma - \nabla_Y\nabla_X\sigma - \nabla_{[X, Y]}\sigma.$$

$C^\infty(M)$ is the algebra of smooth functions; $[X, Y]$ is the [[Def - The Lie Bracket of Vector Fields|Lie bracket]] of vector fields. For the parent symbol registry see [[Gauge Theory I — Connections on Vector Bundles and the Electromagnetic Connection]].

---

# Statement

> **Theorem.** Let $\nabla$ be a connection on a smooth vector bundle $E \to M$. The curvature operator $F : \mathfrak{X}(M) \times \mathfrak{X}(M) \times \Gamma(E) \to \Gamma(E)$ defined by $F(X, Y)\sigma = \nabla_X\nabla_Y\sigma - \nabla_Y\nabla_X\sigma - \nabla_{[X, Y]}\sigma$ is $C^\infty(M)$-linear in each of $X$, $Y$, and $\sigma$ separately. Equivalently, for all $f \in C^\infty(M)$:
> - $F(fX, Y)\sigma = fF(X, Y)\sigma$
> - $F(X, fY)\sigma = fF(X, Y)\sigma$
> - $F(X, Y)(f\sigma) = fF(X, Y)\sigma$
>
> Consequently, $F$ defines a section of $\Lambda^2 T^*M \otimes \mathrm{End}(E)$ — a tensor field, specifically an $\mathrm{End}(E)$-valued 2-form on $M$.

The conclusion has structural significance beyond the algebraic statement: it means the value of $F(X, Y)\sigma$ at a point $p$ depends *only on the values* $X(p), Y(p), \sigma(p)$, not on derivatives or neighbourhood behaviour. This is the *defining property of a tensor*.

---

# Motivation

The motivating tension is between the *definition* of curvature and the *expected behaviour* of curvature. By definition $F(X, Y) = \nabla_X\nabla_Y - \nabla_Y\nabla_X - \nabla_{[X, Y]}$ involves *iterated covariant derivatives* — operators that explicitly differentiate the section $\sigma$, so a priori the result should depend on derivatives of $\sigma$, not just on $\sigma$'s value at a point. Likewise, each $\nabla_X$ acts as a derivation in $X$, suggesting non-tensoriality in $X$ as well.

But intuitively, curvature *should* be a tensor. Geometrically it measures "infinitesimal holonomy per unit area of an infinitesimal loop" — a pointwise quantity. Algebraically it should be a 2-form valued in $\mathrm{End}(E)$, because the structure equation $F = d\omega + \omega \wedge \omega$ produces a matrix of 2-forms. The expected behaviour is tensorial; the apparent behaviour from the definition is not.

The theorem reconciles this: by an algebraic miracle, all the derivative terms cancel and what remains is tensorial. The mechanism of cancellation is the *exact reason* the bracket term $\nabla_{[X, Y]}$ is in the definition — it is the term that absorbs the non-cancelling derivatives.

This is a fundamental pattern in geometry. The simplest example is the **Lie bracket** itself: $[X, Y] = XY - YX$ on functions; despite $X, Y$ being derivations, $[X, Y]$ is again a derivation (so a vector field, not a higher-order operator). Curvature is the next instance, with the bracket term added to absorb extra cancellations. Yet another instance is the **torsion** of a connection: $T(X, Y) = \nabla_X Y - \nabla_Y X - [X, Y]$ — again with a bracket term, again tensorial despite the derivative-laden definition.

The theorem also has a downstream consequence: it lets us *define* the curvature as a tensor, $F \in \Omega^2(M; \mathrm{End}(E))$, and then talk about its cohomology class, its integrals over surfaces, its evaluation at points, and all the apparatus of tensor calculus — none of which would make sense for a non-tensorial expression.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis "a connection $\nabla$ on a vector bundle" is bare. Any setting with a connection — Levi-Civita on Riemannian manifolds, EM on a wave-function line bundle, Yang-Mills, the trivial connection on any bundle — satisfies the hypothesis and produces a tensorial curvature.

**A connection arises from minimal coupling.** In gauge theory, the curvature of the EM or Yang-Mills connection on the matter field's bundle is automatically a tensor — independent of the gauge choice, well-defined pointwise. This is what makes the Yang-Mills Lagrangian $\mathcal{L} = -\frac{1}{4}\mathrm{tr}(F_{\mu\nu}F^{\mu\nu})$ a well-defined Lorentz-scalar density, integrable to produce a gauge-invariant action.

**A connection arises from a metric.** The Levi-Civita connection on a Riemannian manifold has tensorial Riemann curvature $R(X, Y)Z$ — the theorem applied with $E = TM$ and $\nabla$ = Levi-Civita. This is what makes the Riemann tensor a well-defined object whose components $R^i{}_{jkl}$ transform tensorially under coordinate changes.

**A connection arises by partition-of-unity gluing.** Even when the connection is "artificially" constructed by gluing trivial connections via a partition of unity (see [[Thm - Existence of Connections via Partitions of Unity]]), its curvature is still a tensor — the construction may produce ugly local expressions, but the *invariant* meaning of $F$ as a tensor is unaffected.

**Targets (Output Amplification)**

The conclusion "curvature is tensorial" combined with other facts gives the apparatus of curvature theory.

**Combined with the existence of a frame:** in any local frame, $F = (F^\alpha{}_\beta)$ is a matrix of 2-forms with $F^\alpha{}_\beta = d\omega^\alpha{}_\beta + \omega^\alpha{}_\gamma \wedge \omega^\gamma{}_\beta$ (the structure equation). The tensoriality means the matrix can be evaluated point by point, so each $F^\alpha{}_\beta(p) \in \Lambda^2 T^*_pM$ is a single 2-form at $p$.

**Combined with change-of-frame:** under $e_V = e_U c$, the curvature matrix transforms as $F_V = c^{-1}F_U c$ — a *tensorial* transformation by conjugation, with no inhomogeneous piece. (This contrasts with the connection $\omega$, which has the inhomogeneous $c^{-1}dc$ term.) The tensoriality of $F$ is exactly what licenses this clean transformation rule.

**Combined with the Bianchi identity** $d_\nabla F = 0$: the curvature satisfies $\nabla_{[X}F_{YZ]} = 0$ as a tensorial identity, generating the conservation laws of geometry — homogeneous Maxwell equations from EM, conservation of stress-energy from gravity's Bianchi.

**Combined with characteristic class theory:** appropriate polynomials in $F$ (Chern, Pontryagin, Euler forms) are closed differential forms whose cohomology classes are independent of $\nabla$. The whole edifice of **Chern-Weil theory** rests on the tensoriality of $F$ — without it, polynomial expressions in $F$ would not even be well-defined.

---

# Why Is It True

**One-line mechanism summary:** **The $\nabla_{[X, Y]}$ term in the definition is precisely the cancellation term needed to absorb the extra Leibniz-rule contributions when $X, Y$ are replaced by $fX, fY$ — the bracket term turns "second derivatives" into "tensorial 2-forms".**

The intuition is best seen by computing $F(fX, Y)\sigma$ explicitly and tracking which terms cancel. Compute:

$$\nabla_{fX}\nabla_Y\sigma = f\nabla_X\nabla_Y\sigma$$

(by $C^\infty(M)$-linearity of $\nabla_\cdot$ in its argument). And:

$$\nabla_Y\nabla_{fX}\sigma = \nabla_Y(f\nabla_X\sigma) = (Yf)\nabla_X\sigma + f\nabla_Y\nabla_X\sigma$$

(by Leibniz on the *outer* $\nabla_Y$). The "extra" term $(Yf)\nabla_X\sigma$ would spoil tensoriality — it's a derivative of $f$, not just multiplication by $f$.

Now the bracket: $[fX, Y] = fXY - YfX = fXY - (Yf)X - fYX = f[X, Y] - (Yf)X$. Hence

$$\nabla_{[fX, Y]}\sigma = \nabla_{f[X, Y] - (Yf)X}\sigma = f\nabla_{[X, Y]}\sigma - (Yf)\nabla_X\sigma.$$

The extra term $-(Yf)\nabla_X\sigma$ is *exactly* what is needed to cancel the extra $(Yf)\nabla_X\sigma$ from the second term. Putting it together:

$$F(fX, Y)\sigma = f\nabla_X\nabla_Y\sigma - (Yf)\nabla_X\sigma - f\nabla_Y\nabla_X\sigma - [f\nabla_{[X,Y]}\sigma - (Yf)\nabla_X\sigma] = f\,F(X, Y)\sigma.$$

The two $(Yf)\nabla_X\sigma$ terms cancel — and they cancel *because* of the bracket term's contribution. Without $\nabla_{[X, Y]}$, the cancellation would not happen.

The cancellation in $\sigma$: $F(X, Y)(f\sigma) = \nabla_X\nabla_Y(f\sigma) - \nabla_Y\nabla_X(f\sigma) - \nabla_{[X, Y]}(f\sigma)$. Using the Leibniz rule for $\nabla_X$ on $f\sigma$: $\nabla_X(f\sigma) = (Xf)\sigma + f\nabla_X\sigma$. So $\nabla_Y\nabla_X(f\sigma) = \nabla_Y((Xf)\sigma + f\nabla_X\sigma) = (YXf)\sigma + (Xf)\nabla_Y\sigma + (Yf)\nabla_X\sigma + f\nabla_Y\nabla_X\sigma$. Subtracting the symmetric expression $\nabla_X\nabla_Y(f\sigma) = (XYf)\sigma + (Yf)\nabla_X\sigma + (Xf)\nabla_Y\sigma + f\nabla_X\nabla_Y\sigma$:

$$\nabla_X\nabla_Y(f\sigma) - \nabla_Y\nabla_X(f\sigma) = (XY - YX)f\cdot\sigma + f(\nabla_X\nabla_Y - \nabla_Y\nabla_X)\sigma = [X, Y]f\cdot\sigma + f(\ldots)\sigma.$$

And $\nabla_{[X, Y]}(f\sigma) = [X, Y]f \cdot \sigma + f\nabla_{[X, Y]}\sigma$. Subtracting:

$$F(X, Y)(f\sigma) = (\nabla_X\nabla_Y - \nabla_Y\nabla_X - \nabla_{[X, Y]})(f\sigma) = f(\nabla_X\nabla_Y - \nabla_Y\nabla_X - \nabla_{[X, Y]})\sigma + (\text{terms involving } [X,Y]f, XYf, YXf).$$

The non-$f$-only terms work out to $\bigl([X,Y]f - [X,Y]f\bigr)\sigma = 0$. The cancellation again happens because of the bracket term in the definition. Without it, $F(X, Y)(f\sigma) \ne fF(X, Y)\sigma$.

This is the "miracle" of the curvature definition: every derivative of $f$ that could break tensoriality is cancelled by another, and the bracket term $\nabla_{[X, Y]}$ is precisely the mechanism that organizes the cancellation.

---

# What Makes This Hard

The argument is computational — straightforward in retrospect, but easy to make sign errors. The hardest part for many is *believing* the cancellation will work: it looks like there should be too many "stray" derivatives of $f$, and only by careful bookkeeping do they all kill each other. The pedagogical solution is to *guess the form* of the bracket term first (force tensoriality), then verify the answer is indeed the right curvature definition.

Common errors: (i) Forgetting that $\nabla$ is $C^\infty(M)$-linear in the *first* argument (the vector field), but only Leibniz in the *second* (the section). (ii) Confusing the sign of $[fX, Y]$ — the formula $[fX, Y] = f[X, Y] - (Yf)X$ has the *minus* sign because $Y$ acts on $f$ in the rightward expansion of $fXY$. (iii) Trying to prove tensoriality in $X, Y$ together rather than one at a time.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Verify $F(fX, Y) = fF(X, Y)$ by direct computation; the same argument (with $X \leftrightarrow Y$) gives $C^\infty$-linearity in $Y$. Then verify $F(X, Y)(f\sigma) = fF(X, Y)\sigma$ by direct computation, exploiting the cancellations from the bracket term.

**Subgoal decomposition:**

1. **$C^\infty(M)$-linearity in $X$ (and by symmetry in $Y$):** Compute $F(fX, Y)\sigma$ using the Leibniz rule for $\nabla_Y$ and the bracket formula $[fX, Y] = f[X, Y] - (Yf)X$. The extra $(Yf)\nabla_X\sigma$ from the Leibniz on $\nabla_Y$ is cancelled by the $(Yf)\nabla_X\sigma$ from the bracket term.
   - *Hint:* Track each $(Yf)\nabla_X\sigma$ term carefully and confirm they have opposite signs.
   - *Why needed:* This is the first half of the tensoriality.

2. **$C^\infty(M)$-linearity in $\sigma$:** Compute $F(X, Y)(f\sigma)$ using the Leibniz rule for both $\nabla_X$ and $\nabla_Y$. The terms involving $XYf$ and $YXf$ assemble into $[X, Y]f\cdot\sigma$, which is cancelled by the $[X, Y]f\cdot\sigma$ from $\nabla_{[X, Y]}(f\sigma)$.
   - *Hint:* Use $XYf - YXf = [X, Y]f$; the cross-derivative terms cancel directly.
   - *Why needed:* This is the second half of the tensoriality.

3. **Conclude that $F$ defines a section of $\Lambda^2 T^*M \otimes \mathrm{End}(E)$.** A $C^\infty(M)$-multilinear and antisymmetric map (antisymmetric since $F(X, Y) = -F(Y, X)$ by inspection) corresponds canonically to a section of the appropriate tensor bundle.
   - *Hint:* This is the standard correspondence between tensors and $C^\infty(M)$-multilinear maps.
   - *Why needed:* Packages the result in the geometrically meaningful form.

---

# Lemma Decomposition

> [!note]- Lemma 1: $C^\infty$-linearity in $X$
> **Statement:** $F(fX, Y)\sigma = fF(X, Y)\sigma$ for all $f \in C^\infty(M)$, $X, Y \in \mathfrak{X}(M)$, $\sigma \in \Gamma(E)$.
>
> **Hint:** Track the $(Yf)\nabla_X\sigma$ terms — one from $\nabla_Y(f\nabla_X\sigma)$, another from $\nabla_{[fX, Y]}$ via $[fX, Y] = f[X, Y] - (Yf)X$. These cancel exactly.
>
> **Why needed:** First half of the tensoriality; the symmetric argument gives $C^\infty$-linearity in $Y$.
>
> > [!note]- Full proof
> > Compute each term:
> >
> > **$\nabla_{fX}\nabla_Y\sigma = f\nabla_X\nabla_Y\sigma$** by $C^\infty$-linearity of $\nabla_\cdot$ in its argument.
> >
> > **$\nabla_Y\nabla_{fX}\sigma = \nabla_Y(f\nabla_X\sigma)$**, and by Leibniz:
> > $\nabla_Y(f\nabla_X\sigma) = (Yf)\nabla_X\sigma + f\nabla_Y\nabla_X\sigma$.
> >
> > **$\nabla_{[fX, Y]}\sigma$**: using $[fX, Y] = f[X, Y] - (Yf)X$,
> > $\nabla_{[fX, Y]}\sigma = \nabla_{f[X, Y] - (Yf)X}\sigma = f\nabla_{[X, Y]}\sigma - (Yf)\nabla_X\sigma$.
> >
> > Putting it together:
> > $$F(fX, Y)\sigma = f\nabla_X\nabla_Y\sigma - [(Yf)\nabla_X\sigma + f\nabla_Y\nabla_X\sigma] - [f\nabla_{[X, Y]}\sigma - (Yf)\nabla_X\sigma]$$
> > $$= f(\nabla_X\nabla_Y\sigma - \nabla_Y\nabla_X\sigma - \nabla_{[X, Y]}\sigma) - (Yf)\nabla_X\sigma + (Yf)\nabla_X\sigma = fF(X, Y)\sigma. \quad\square$$

> [!note]- Lemma 2: $C^\infty$-linearity in $\sigma$
> **Statement:** $F(X, Y)(f\sigma) = fF(X, Y)\sigma$ for all $f \in C^\infty(M)$, $X, Y \in \mathfrak{X}(M)$, $\sigma \in \Gamma(E)$.
>
> **Hint:** The cross-derivative terms $(Xf)\nabla_Y\sigma$ and $(Yf)\nabla_X\sigma$ from Leibniz cancel between $\nabla_X\nabla_Y(f\sigma)$ and $\nabla_Y\nabla_X(f\sigma)$. The remaining terms involving $XYf$ and $YXf$ assemble into $[X, Y]f\cdot\sigma$, which is exactly cancelled by $\nabla_{[X, Y]}(f\sigma) - f\nabla_{[X, Y]}\sigma$.
>
> **Why needed:** Second half of tensoriality.
>
> > [!note]- Full proof
> > Compute:
> > $$\nabla_X\nabla_Y(f\sigma) = \nabla_X[(Yf)\sigma + f\nabla_Y\sigma] = (XYf)\sigma + (Yf)\nabla_X\sigma + (Xf)\nabla_Y\sigma + f\nabla_X\nabla_Y\sigma.$$
> >
> > Similarly,
> > $$\nabla_Y\nabla_X(f\sigma) = (YXf)\sigma + (Xf)\nabla_Y\sigma + (Yf)\nabla_X\sigma + f\nabla_Y\nabla_X\sigma.$$
> >
> > Subtracting:
> > $$\nabla_X\nabla_Y(f\sigma) - \nabla_Y\nabla_X(f\sigma) = (XY - YX)f\cdot\sigma + f(\nabla_X\nabla_Y - \nabla_Y\nabla_X)\sigma = [X, Y]f\cdot\sigma + f(\nabla_X\nabla_Y - \nabla_Y\nabla_X)\sigma.$$
> >
> > And:
> > $$\nabla_{[X, Y]}(f\sigma) = ([X, Y]f)\sigma + f\nabla_{[X, Y]}\sigma.$$
> >
> > Therefore:
> > $$F(X, Y)(f\sigma) = [X, Y]f\cdot\sigma + f(\nabla_X\nabla_Y - \nabla_Y\nabla_X)\sigma - [X, Y]f\cdot\sigma - f\nabla_{[X, Y]}\sigma = fF(X, Y)\sigma. \quad\square$$

---

# Formal Proof

> [!note]- Complete formal proof
> **Setup.** Let $\nabla$ be a connection on a smooth vector bundle $E \to M$. Define $F : \mathfrak{X}(M) \times \mathfrak{X}(M) \times \Gamma(E) \to \Gamma(E)$ by $F(X, Y)\sigma = \nabla_X\nabla_Y\sigma - \nabla_Y\nabla_X\sigma - \nabla_{[X, Y]}\sigma$.
>
> **$\mathbb{R}$-trilinearity** is immediate from $\mathbb{R}$-linearity of $\nabla$ and the Lie bracket.
>
> **$C^\infty(M)$-linearity in $X$:** Lemma 1 gives $F(fX, Y)\sigma = fF(X, Y)\sigma$.
>
> **$C^\infty(M)$-linearity in $Y$:** Use $F(X, Y) = -F(Y, X)$ (immediate from the definition) and apply Lemma 1: $F(X, fY)\sigma = -F(fY, X)\sigma = -fF(Y, X)\sigma = fF(X, Y)\sigma$.
>
> **$C^\infty(M)$-linearity in $\sigma$:** Lemma 2 gives $F(X, Y)(f\sigma) = fF(X, Y)\sigma$.
>
> **Antisymmetry in $(X, Y)$:** $F(X, Y) = -F(Y, X)$ — interchange swaps the first two terms and negates the bracket term, with $[X, Y] = -[Y, X]$.
>
> **Conclusion:** $F$ is $C^\infty(M)$-multilinear (linear in each argument over $C^\infty(M)$) and antisymmetric in the first two arguments. By the standard correspondence between $C^\infty(M)$-multilinear antisymmetric maps and sections of $\Lambda^2 T^*M \otimes \mathrm{End}(E)$, $F$ defines a section of this bundle — an $\mathrm{End}(E)$-valued 2-form on $M$.
> ▪

---

# Cross-Field Exercise Suggestions

**Riemannian geometry: Riemann tensor tensoriality.** Apply this theorem to the Levi-Civita connection on $TM$. The resulting curvature operator $R(X, Y)Z = \nabla_X\nabla_Y Z - \nabla_Y\nabla_X Z - \nabla_{[X, Y]}Z$ is the **Riemann curvature tensor**, and by the present theorem it is a tensor: $R \in \Gamma(\Lambda^2 T^*M \otimes \mathrm{End}(TM))$. The components $R^i{}_{jkl}$ are then guaranteed to transform tensorially under coordinate changes — a non-trivial fact that follows from the algebraic structure of the definition.

**Field theory: gauge invariance of the Yang-Mills action.** The Yang-Mills Lagrangian $\mathcal{L} = -\frac{1}{4}\mathrm{tr}(F_{\mu\nu}F^{\mu\nu})$ is a scalar density only because $F$ is a tensor. The tensoriality is what licenses contracting $F_{\mu\nu}$ with the metric and taking the trace — operations that would be ill-defined for a non-tensorial expression.

**Quantum mechanics: Berry curvature on parameter space.** When a quantum system depends on slowly varying parameters $\lambda \in M$, the **Berry connection** $A_{\mathrm{Berry}} = i\langle\psi|d\psi\rangle$ on the line bundle of energy eigenstates over parameter space has a curvature $F_{\mathrm{Berry}} = dA_{\mathrm{Berry}}$. The present theorem ensures this is a 2-form on parameter space — a tensorial object that can be integrated over closed loops to give Berry phases and integrated over closed surfaces to give Chern numbers (topological quantization).

**Stochastic differential geometry: stochastic parallel transport.** In the theory of Brownian motion on Riemannian manifolds, the stochastic differential of a horizontally lifted process is given by curvature terms; the tensoriality of the curvature is what makes the resulting stochastic equations well-defined intrinsically.

---

# Bridges

- **[[Def - Curvature of a Vector-Bundle Connection|Curvature of a Vector-Bundle Connection]]** — This theorem is the foundational fact about curvature: it ensures the operator $F$ is a tensor, hence has well-defined components, can be integrated over surfaces, can be evaluated pointwise, can have its cohomology class taken. Without tensoriality, "curvature" would not be a meaningful geometric object — just an operator on sections with no further structure.

- **[[Thm - Bianchi Identity for a Vector-Bundle Connection|Bianchi Identity]]** — The fact that $d_\nabla F = 0$ is a tensorial identity is a consequence of $F$ being tensorial: tensorial expressions have tensorial covariant derivatives, and the Bianchi identity is the statement that this particular derivative vanishes. The tensoriality of the present theorem is the prerequisite that makes the Bianchi identity sensible.

- **Torsion is a tensor** *(from [[Riemannian Geometry I — Connections and Covariant Differentiation]])* — The same algebraic mechanism, applied to the **torsion** $T(X, Y) = \nabla_X Y - \nabla_Y X - [X, Y]$, shows torsion is also tensorial. The proof is essentially identical: tracking the $(Xf)Y$ and $(Yf)X$ terms from the Leibniz expansion against the bracket term $[fX, Y] = f[X, Y] - (Yf)X$, all extra derivatives of $f$ cancel.

- **Lie derivative tensoriality** *(from [[Differential Geometry V — Vector Fields, Flows, and the Lie Bracket]])* — The Lie bracket $[X, Y]$ is the simplest instance of this kind of cancellation: $[X, Y]$ is itself a vector field (not a second-order differential operator) because the second-derivative terms in $XY - YX$ cancel. Curvature is the natural higher-order analogue, with the bracket *added* to the definition to play the role of cancellation.

---

# Unlocked by This

> [!tip] Chern-Weil Theory and Characteristic Classes *(from Algebraic Topology)*
> The tensoriality of the curvature $F$ is the prerequisite for all of **Chern-Weil theory**: only because $F$ is a tensor can we form polynomial expressions like $\mathrm{tr}(F^k)$ and $\det(I + F)$ that are *closed differential forms* representing topological invariants. Specifically, $\mathrm{tr}(F^k)$ is a closed $2k$-form (the **Chern character form** up to factors), and its de Rham cohomology class is independent of $\nabla$, defining the *Chern classes* $c_k(E) \in H^{2k}(M, \mathbb{R})$ (integral via the cocycle condition). The whole edifice of characteristic class theory rests on the present theorem.

> [!tip] Tensoriality Pattern Across Geometry *(from Differential Geometry)*
> The cancellation pattern of this theorem — "second-derivative terms cancel due to the bracket structure" — recurs throughout differential geometry. Examples: the **torsion** $T(X, Y) = \nabla_X Y - \nabla_Y X - [X, Y]$ is tensorial by the same mechanism; the **Lie derivative** $\mathcal{L}_X Y = [X, Y]$ being a vector field (first-order, not second) is a degenerate case; the **second covariant differential** $\nabla^2\sigma$ has its symmetric and antisymmetric parts both well-defined (the antisymmetric being the curvature). This pattern reflects the fundamental fact that **Lie-bracket-corrected commutators of differential operators are tensors**, the foundation of the modern algebra of connections.
