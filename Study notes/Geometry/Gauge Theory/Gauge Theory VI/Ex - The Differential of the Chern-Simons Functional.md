---
type: exercise
subject: gauge-theory
difficulty: "⭐"
prereqs:
  - "Thm - Critical Points of the Chern-Simons Functional are the Flat Connections"
  - "Def - Chern-Simons Functional"
  - "Def - Curvature of a Principal Connection"
  - "Def - Lie-Algebra-Valued Differential Forms and Their Bracket"
  - "Thm - Stokes' Theorem on Manifolds"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $M$ be a closed oriented smooth three-manifold and let $P \to M$ be a principal $SU(2)$-bundle, which we trivialise once and for all — every such bundle over a three-manifold is trivial, by [[Thm - Classification of Principal SU(2)-Bundles over Four-Manifolds|the classification of SU(2)-bundles]] — so that a connection is recorded by a single Lie-algebra-valued one-form $A \in \Omega^1(M; \mathfrak{su}(2))$. On the affine space $\mathcal{A} = \Omega^1(M; \mathfrak{su}(2))$ of connections the **Chern–Simons functional** is
$$\vartheta(A) = \frac{1}{8\pi^2}\int_M \operatorname{tr}\!\Big(A \wedge dA + \tfrac23\, A \wedge A \wedge A\Big),$$
where $\operatorname{tr}$ is the trace in the defining two-dimensional representation of $\mathfrak{su}(2)$, and the curvature of $A$ is $F_A = dA + A \wedge A$.

Fix $A \in \Omega^1(M; \mathfrak{su}(2))$ and let $a \in \Omega^1(M; \mathfrak{su}(2))$ be an arbitrary variation direction. Because $\mathcal{A}$ is an affine space modelled on $\Omega^1(M;\mathfrak{su}(2))$, the straight path $s \mapsto A + sa$ ($s \in \mathbb{R}$) is a legitimate curve of connections through $A$, and the derivative
$$d\vartheta_A(a) := \frac{d}{ds}\Big|_{s=0} \vartheta(A + sa)$$
is the directional derivative of $\vartheta$ at $A$ along $a$; as $a$ ranges over $\Omega^1(M;\mathfrak{su}(2))$ this assembles into the differential (the first variation) $d\vartheta_A$ of $\vartheta$ at $A$.

**Prove the first-variation formula**
$$\boxed{\;\frac{d}{ds}\Big|_{s=0} \vartheta(A + sa) = \frac{1}{4\pi^2}\int_M \operatorname{tr}(F_A \wedge a)\;}$$
for all $A, a \in \Omega^1(M; \mathfrak{su}(2))$, displaying every integration by parts and every use of the cyclicity of the trace explicitly.

This is exactly part (i) of the critical-point theorem below; the present exercise isolates the computation that proves it as a stand-alone drill.

**Recall:**

The objects in play are the Chern–Simons functional, the curvature of a connection, the bracket and trace of Lie-algebra-valued forms, and Stokes' theorem on a closed manifold.

![[Thm - Critical Points of the Chern-Simons Functional are the Flat Connections#Statement]]

![[Def - Chern-Simons Functional#The Definition]]

The [[Def - Chern-Simons Functional|Chern–Simons functional]] $\vartheta$ takes values in $\mathbb{R}/\mathbb{Z}$; its differential $d\vartheta_A$, however, is a genuine $\mathbb{R}$-valued linear functional on $\Omega^1(M;\mathfrak{su}(2))$, because passing to a nearby connection $A + sa$ and differentiating in $s$ is insensitive to the integer ambiguity — the ambiguity is locally constant along the affine line $A + sa$, so it drops out of $\tfrac{d}{ds}$.

![[Def - Curvature of a Principal Connection#The Definition]]

In the fixed trivialisation the curvature of $A \in \Omega^1(M;\mathfrak{su}(2))$ is the local curvature two-form
$$F_A = dA + \tfrac12[A \wedge A] = dA + A \wedge A \in \Omega^2(M; \mathfrak{su}(2)),$$
where for the matrix group $SU(2)$ the graded bracket of the $\mathfrak{su}(2)$-valued one-form $A$ with itself is $\tfrac12[A \wedge A] = A \wedge A$, the wedge of matrix-valued forms formed by matrix multiplication of the coefficients (see [[Def - Lie-Algebra-Valued Differential Forms and Their Bracket|the page on Lie-algebra-valued forms and their bracket]]).

![[Thm - Stokes' Theorem on Manifolds#Statement]]

Since $M$ is closed (compact without boundary), Stokes' theorem specialises to the statement that the integral of an exact form vanishes: $\int_M d\beta = 0$ for every $\beta \in \Omega^{2}(M;\mathbb{R})$, because $\partial M = \varnothing$. This is the only analytic input to the computation, and it is what makes the integration by parts a clean equality rather than an equality up to a boundary term.

The one purely algebraic fact used throughout — *the graded cyclicity of the trace of matrix-valued forms*:
$$\operatorname{tr}(\alpha \wedge \beta) = (-1)^{pq}\,\operatorname{tr}(\beta \wedge \alpha) \qquad \text{for } \alpha \in \Omega^p(M; \mathfrak{gl}_n),\ \beta \in \Omega^q(M; \mathfrak{gl}_n).$$
This is proved once, in the Solution, and reused; it is the identity that lets the three cubic terms collapse to one and the integration by parts land back on $a$.

---

# Convergent Strategy

**Problem class.** This is a *first-variation* (calculus-of-variations) computation for a functional defined by an integral of a polynomial in a field and its derivative. The deliverable is not a number but an identity of linear functionals: we must recognise $d\vartheta_A$ as *integration against a fixed two-form*, and identify that two-form as the curvature $F_A$. The recognisable shape is "differentiate a cubic action, integrate by parts to move all derivatives off the variation $a$, read off the Euler–Lagrange density." The pay-off — that the density is $F_A$ — is the reason the critical points of $\vartheta$ are exactly the flat connections.

**Assumption pattern.** Two hypotheses do all the work, and each is used exactly once. *Closedness of $M$* is used only to discard the boundary term in the single integration by parts (Stokes with $\partial M = \varnothing$). *The matrix-group identity $F_A = dA + A\wedge A$* is used only at the very end, to package $dA + A \wedge A$ into $F_A$. Everything between these two is bookkeeping with the graded cyclicity of the trace. The trigger to reach for cyclicity is the appearance of trace-of-wedge terms in more than one order ($a\wedge A\wedge A$, $A\wedge a\wedge A$, $A\wedge A\wedge a$, and later $A \wedge da$ versus $dA \wedge a$).

**Theorem routing.** The route is linear and forced: (1) substitute $A + sa$ into the Chern–Simons density and extract the coefficient of $s^1$ — this is the definition of $\tfrac{d}{ds}\big|_0$ for a polynomial dependence; (2) use [[Def - Lie-Algebra-Valued Differential Forms and Their Bracket|graded cyclicity of the trace]] to collapse the three cubic variation terms $a\wedge A\wedge A + A\wedge a\wedge A + A\wedge A\wedge a$ into $3\,\operatorname{tr}(a\wedge A\wedge A)$; (3) integrate the term $\operatorname{tr}(A\wedge da)$ by parts using [[Thm - Stokes' Theorem on Manifolds|Stokes' theorem]] on the closed manifold $M$, turning it into $\operatorname{tr}(a \wedge dA)$; (4) assemble the surviving terms as $2\operatorname{tr}(a\wedge(dA + A\wedge A)) = 2\operatorname{tr}(a\wedge F_A)$ using the [[Def - Curvature of a Principal Connection|curvature identity]], divide by $8\pi^2$, and one more application of cyclicity puts it in the stated form $\tfrac{1}{4\pi^2}\int_M\operatorname{tr}(F_A\wedge a)$.

**Key decision point.** The single non-obvious move is *which* trace term to integrate by parts and in which direction. The variation of the quadratic part produces $\operatorname{tr}(a\wedge dA) + \operatorname{tr}(A\wedge da)$; the first term already has all its derivatives on $A$, but the second has the derivative on $a$. The whole point of the integration by parts is to move the derivative *off the variation $a$ and onto $A$*, so that the final answer is $a$ paired against a fixed density built from $A$ alone. Integrating $\operatorname{tr}(A\wedge da)$ by parts accomplishes exactly this, and — after cyclicity — makes it a second copy of $\operatorname{tr}(a\wedge dA)$, which is why the factor $\tfrac18$ becomes $\tfrac14$. Recognising that the two quadratic terms are equal after integration by parts is the crux; a solver who integrates the wrong term by parts, or forgets that $M$ is closed, will not reach the clean factor.

---

# Legal Operations Used

This solution deploys the following operations, each named descriptively (the topic page for §6.4 numbers them; the orchestrator will reconcile the numbering):

1. **Extract the first-order term of a polynomial variation.** Because $\vartheta(A + sa)$ is a cubic polynomial in $s$ with form-valued coefficients, $\tfrac{d}{ds}\big|_0\vartheta(A+sa)$ is exactly the coefficient of $s^1$; compute it by expanding each of the two summands of the density and keeping the linear part.

2. **Apply graded cyclicity of the trace of matrix-valued forms.** For $\alpha \in \Omega^p$, $\beta \in \Omega^q$ with matrix coefficients, $\operatorname{tr}(\alpha\wedge\beta) = (-1)^{pq}\operatorname{tr}(\beta\wedge\alpha)$; use it to identify the three cubic terms and to move one-forms past two-forms.

3. **Collapse repeated cubic trace terms.** The three terms produced by varying $A^{\wedge3}$ are all equal by operation 2, so their sum is three times any one of them; combined with the coefficient $\tfrac23$ this yields $2\,\operatorname{tr}(a\wedge A\wedge A)$.

4. **Integrate by parts on a closed manifold using Stokes.** From $d\operatorname{tr}(A\wedge a) = \operatorname{tr}(dA\wedge a) - \operatorname{tr}(A\wedge da)$ and $\int_M d(\cdots) = 0$ (closed $M$, [[Thm - Stokes' Theorem on Manifolds|Stokes]]), deduce $\int_M\operatorname{tr}(A\wedge da) = \int_M\operatorname{tr}(dA\wedge a)$.

5. **Repackage the curvature.** Recognise $dA + A\wedge A = F_A$ ([[Def - Curvature of a Principal Connection|the local curvature]] of the matrix group $SU(2)$) to write the density as a pairing of $a$ against $F_A$.

---

# Hints

> [!note]- Hint 1
> You are differentiating a functional along the straight line $A + sa$. The density $\operatorname{tr}(A\wedge dA + \tfrac23 A\wedge A\wedge A)$ is a polynomial in $A$ of degree at most three, so $\vartheta(A+sa)$ is a genuine cubic polynomial in the real variable $s$. Its derivative at $s=0$ is just the coefficient of $s$. Substitute $A \mapsto A + sa$, expand, and collect the terms linear in $s$ — nothing subtler than the product rule is needed at this stage.

> [!note]- Hint 2
> Varying the cubic term $\tfrac23\operatorname{tr}(A\wedge A\wedge A)$ produces three pieces: $\operatorname{tr}(a\wedge A\wedge A)$, $\operatorname{tr}(A\wedge a\wedge A)$, $\operatorname{tr}(A\wedge A\wedge a)$. These look different but are equal. The reason is the cyclicity of the trace, adapted to forms: for matrix-valued forms, moving a factor of degree $p$ past a factor of degree $q$ costs a sign $(-1)^{pq}$, and $\operatorname{tr}(XY) = \operatorname{tr}(YX)$ for the coefficients. A one-form moved past a two-form costs $(-1)^{1\cdot 2} = +1$. Use this to show all three are equal.

> [!note]- Hint 3
> After the cubic terms collapse, you are left with $\operatorname{tr}(a\wedge dA) + \operatorname{tr}(A\wedge da)$ from the quadratic part and $2\operatorname{tr}(a\wedge A\wedge A)$ from the cubic. The term $\operatorname{tr}(A\wedge da)$ has its derivative on the *variation* $a$, and you want it on $A$. Integrate by parts: differentiate the two-form $\operatorname{tr}(A\wedge a)$, note that its integral over the closed manifold $M$ vanishes by Stokes, and solve for $\int_M\operatorname{tr}(A\wedge da)$. Watch the sign that comes from $d$ acting across the one-form $A$.

> [!note]- Hint 4
> Once the integration by parts turns $\int_M\operatorname{tr}(A\wedge da)$ into $\int_M\operatorname{tr}(dA\wedge a) = \int_M\operatorname{tr}(a\wedge dA)$, you have two equal copies of $\operatorname{tr}(a\wedge dA)$ and the cubic $2\operatorname{tr}(a\wedge A\wedge A)$. Factor out a $2$ and an $a$: the bracket is $dA + A\wedge A$, which is precisely $F_A$. All that remains is one more cyclicity swap to write $\operatorname{tr}(a\wedge F_A) = \operatorname{tr}(F_A\wedge a)$ and to track the constant $\tfrac{1}{8\pi^2}\cdot 2 = \tfrac{1}{4\pi^2}$.

---

# Solution

The computation is a textbook first variation: substitute the perturbed connection, keep the linear order, use cyclicity of the trace to tidy the algebra, and integrate by parts once to move the lone derivative off the variation. The only place the geometry enters is at the end, where $dA + A\wedge A$ is recognised as the curvature; everything before that is the calculus of forms on a closed manifold. We first record the cyclicity identity, then run the four steps.

**Step 0: Graded cyclicity of the trace of matrix-valued forms.**

For $\alpha \in \Omega^p(M;\mathfrak{gl}_n)$ and $\beta \in \Omega^q(M;\mathfrak{gl}_n)$, $\operatorname{tr}(\alpha\wedge\beta) = (-1)^{pq}\operatorname{tr}(\beta\wedge\alpha)$.

> [!note]- Derivation
> Write $\alpha = \sum_I \alpha_I\,dx^I$ and $\beta = \sum_J \beta_J\,dx^J$ in local coordinates, where $I$ ranges over increasing $p$-multi-indices and $J$ over increasing $q$-multi-indices, $\alpha_I, \beta_J$ are matrix-valued functions, and $dx^I, dx^J$ are the corresponding basis forms. The wedge of matrix-valued forms multiplies the coefficient matrices and wedges the scalar forms:
> $$\alpha\wedge\beta = \sum_{I,J} \alpha_I\beta_J\,dx^I\wedge dx^J \qquad \text{(definition of the wedge of matrix-valued forms)}.$$
> Taking the trace and using $\operatorname{tr}(\alpha_I\beta_J) = \operatorname{tr}(\beta_J\alpha_I)$ (cyclicity of the ordinary matrix trace) gives
> $$\operatorname{tr}(\alpha\wedge\beta) = \sum_{I,J}\operatorname{tr}(\beta_J\alpha_I)\,dx^I\wedge dx^J \qquad \text{(linearity of }\operatorname{tr}\text{, cyclicity of the matrix trace).}$$
> The scalar forms anticommute according to their degrees, $dx^I\wedge dx^J = (-1)^{pq}\,dx^J\wedge dx^I$ (a $p$-form past a $q$-form), so
> $$\operatorname{tr}(\alpha\wedge\beta) = (-1)^{pq}\sum_{I,J}\operatorname{tr}(\beta_J\alpha_I)\,dx^J\wedge dx^I = (-1)^{pq}\operatorname{tr}(\beta\wedge\alpha) \qquad \text{(reindexing the sum as the trace of }\beta\wedge\alpha\text{).}$$
> This is the claimed identity. In particular, a one-form past a two-form ($p=1$, $q=2$) costs $(-1)^{1\cdot2} = +1$, and a one-form past a one-form ($p=q=1$) costs $(-1)^{1\cdot1} = -1$.

**Step 1: Extract the first-order term of $\vartheta(A + sa)$.**

Substituting $A + sa$ into the density and keeping the coefficient of $s$ gives
$$8\pi^2\, d\vartheta_A(a) = \int_M \operatorname{tr}\!\big(a\wedge dA + A\wedge da + 2\,a\wedge A\wedge A\big) + \big[\text{cubic collapse, Step 2}\big].$$

> [!note]- Derivation
> Write the density as $\operatorname{cs}(A) = \operatorname{tr}(A\wedge dA) + \tfrac23\operatorname{tr}(A\wedge A\wedge A)$, so that $\vartheta(A) = \tfrac{1}{8\pi^2}\int_M\operatorname{cs}(A)$. Substitute $A \mapsto A + sa$; since $d$ is linear, $d(A+sa) = dA + s\,da$.
>
> *Quadratic part.* Expanding the product,
> $$(A + sa)\wedge d(A+sa) = A\wedge dA + s\,(a\wedge dA + A\wedge da) + s^2\, a\wedge da \qquad \text{(bilinearity of }\wedge\text{, }d(A+sa)=dA+s\,da).$$
> The coefficient of $s^1$ is $a\wedge dA + A\wedge da$.
>
> *Cubic part.* Expanding $(A+sa)^{\wedge 3} = (A+sa)\wedge(A+sa)\wedge(A+sa)$ and keeping only the terms with exactly one factor of $a$,
> $$\big[(A+sa)^{\wedge3}\big]_{s^1} = a\wedge A\wedge A + A\wedge a\wedge A + A\wedge A\wedge a \qquad \text{(the three ways to place one }a\text{ among three factors).}$$
>
> Taking traces, differentiating $\vartheta(A+sa)$ in $s$ at $s=0$ (which for a polynomial in $s$ returns the coefficient of $s^1$), and multiplying by $8\pi^2$,
> $$8\pi^2\, d\vartheta_A(a) = \int_M \operatorname{tr}(a\wedge dA + A\wedge da) + \tfrac23\int_M \operatorname{tr}(a\wedge A\wedge A + A\wedge a\wedge A + A\wedge A\wedge a).$$
> The three cubic trace terms are treated in Step 2.

**Step 2: Collapse the three cubic terms.**

The three cubic trace terms are equal, so $\tfrac23\operatorname{tr}(a\wedge A\wedge A + A\wedge a\wedge A + A\wedge A\wedge a) = 2\,\operatorname{tr}(a\wedge A\wedge A)$.

> [!note]- Derivation
> Apply graded cyclicity (Step 0) with a one-form and a two-form. First, group $A\wedge A$ as a single two-form:
> $$\operatorname{tr}(a\wedge A\wedge A) = \operatorname{tr}\big(a\wedge (A\wedge A)\big) = (-1)^{1\cdot 2}\operatorname{tr}\big((A\wedge A)\wedge a\big) = \operatorname{tr}(A\wedge A\wedge a) \qquad \text{(Step 0, }p=1,\,q=2).$$
> Second, group the last two factors of $\operatorname{tr}(A\wedge a\wedge A)$:
> $$\operatorname{tr}(A\wedge a\wedge A) = \operatorname{tr}\big(A\wedge(a\wedge A)\big) = (-1)^{1\cdot2}\operatorname{tr}\big((a\wedge A)\wedge A\big) = \operatorname{tr}(a\wedge A\wedge A) \qquad \text{(Step 0, }p=1,\,q=2).$$
> Hence all three cubic terms equal $\operatorname{tr}(a\wedge A\wedge A)$, and their sum is $3\,\operatorname{tr}(a\wedge A\wedge A)$. Multiplying by $\tfrac23$,
> $$\tfrac23\cdot 3\,\operatorname{tr}(a\wedge A\wedge A) = 2\,\operatorname{tr}(a\wedge A\wedge A).$$
> Substituting into Step 1,
> $$8\pi^2\, d\vartheta_A(a) = \int_M \operatorname{tr}(a\wedge dA) + \int_M\operatorname{tr}(A\wedge da) + 2\int_M\operatorname{tr}(a\wedge A\wedge A).$$

**Step 3: Integrate the term $\operatorname{tr}(A\wedge da)$ by parts.**

On the closed manifold $M$, $\displaystyle\int_M\operatorname{tr}(A\wedge da) = \int_M\operatorname{tr}(a\wedge dA)$.

> [!note]- Derivation
> The one-form $\operatorname{tr}(A\wedge a) \in \Omega^2(M;\mathbb{R})$ is an ordinary real two-form. Its exterior derivative, using that $\operatorname{tr}$ is linear and commutes with $d$ and the Leibniz rule for $d$ across the one-form $A$, is
> $$d\,\operatorname{tr}(A\wedge a) = \operatorname{tr}\big(d(A\wedge a)\big) = \operatorname{tr}(dA\wedge a) - \operatorname{tr}(A\wedge da) \qquad \text{(}d\text{ commutes with }\operatorname{tr}\text{; }d(A\wedge a)=dA\wedge a-A\wedge da\text{ as }A\text{ is a one-form).}$$
> Integrate over $M$. Because $M$ is closed, $\partial M = \varnothing$, so [[Thm - Stokes' Theorem on Manifolds|Stokes' theorem]] gives $\int_M d\,\operatorname{tr}(A\wedge a) = \int_{\partial M}\operatorname{tr}(A\wedge a) = 0$. Therefore
> $$0 = \int_M \operatorname{tr}(dA\wedge a) - \int_M\operatorname{tr}(A\wedge da),\qquad\text{i.e.}\qquad \int_M\operatorname{tr}(A\wedge da) = \int_M\operatorname{tr}(dA\wedge a) \qquad \text{(Stokes, }\partial M=\varnothing).$$
> Finally, move the one-form $a$ in front of the two-form $dA$ by graded cyclicity (Step 0, $p=2$, $q=1$, sign $(-1)^{2\cdot1}=+1$):
> $$\int_M\operatorname{tr}(dA\wedge a) = \int_M\operatorname{tr}(a\wedge dA),\qquad\text{so}\qquad \int_M\operatorname{tr}(A\wedge da) = \int_M\operatorname{tr}(a\wedge dA).$$

**Step 4: Assemble and recognise the curvature.**

Combining Steps 2 and 3 and packaging $dA + A\wedge A = F_A$ yields the first-variation formula.

> [!note]- Derivation
> Substitute the result of Step 3 into the expression from Step 2; the two quadratic integrals become identical:
> $$8\pi^2\, d\vartheta_A(a) = \int_M\operatorname{tr}(a\wedge dA) + \int_M\operatorname{tr}(a\wedge dA) + 2\int_M\operatorname{tr}(a\wedge A\wedge A) \qquad \text{(Step 2 and Step 3).}$$
> Collect the factor of $2$ and combine the two-form densities under one trace, using linearity of $\operatorname{tr}$ and of $\wedge$ in the second slot:
> $$8\pi^2\, d\vartheta_A(a) = 2\int_M \operatorname{tr}\big(a\wedge dA + a\wedge A\wedge A\big) = 2\int_M\operatorname{tr}\big(a\wedge(dA + A\wedge A)\big) \qquad \text{(linearity).}$$
> By the [[Def - Curvature of a Principal Connection|curvature identity]] for the matrix group $SU(2)$, $dA + A\wedge A = F_A$, so
> $$8\pi^2\, d\vartheta_A(a) = 2\int_M\operatorname{tr}(a\wedge F_A) \qquad \text{(}F_A = dA + A\wedge A\text{).}$$
> One last cyclicity swap moves the one-form $a$ past the two-form $F_A$ (Step 0, $p=1$, $q=2$, sign $+1$):
> $$\int_M\operatorname{tr}(a\wedge F_A) = \int_M\operatorname{tr}(F_A\wedge a),$$
> whence, dividing by $8\pi^2$,
> $$d\vartheta_A(a) = \frac{2}{8\pi^2}\int_M\operatorname{tr}(F_A\wedge a) = \frac{1}{4\pi^2}\int_M\operatorname{tr}(F_A\wedge a).$$
> This is the required formula.

> [!note]- Complete formal solution
> **Claim.** For a closed oriented three-manifold $M$ and $A, a \in \Omega^1(M;\mathfrak{su}(2))$,
> $$\frac{d}{ds}\Big|_{s=0}\vartheta(A+sa) = \frac{1}{4\pi^2}\int_M\operatorname{tr}(F_A\wedge a),\qquad F_A = dA + A\wedge A.$$
>
> *Cyclicity.* For matrix-valued forms $\alpha\in\Omega^p$, $\beta\in\Omega^q$, writing them in coordinates and using $\operatorname{tr}(\alpha_I\beta_J)=\operatorname{tr}(\beta_J\alpha_I)$ and $dx^I\wedge dx^J=(-1)^{pq}dx^J\wedge dx^I$ gives $\operatorname{tr}(\alpha\wedge\beta)=(-1)^{pq}\operatorname{tr}(\beta\wedge\alpha)$.
>
> *First order.* With $\operatorname{cs}(A)=\operatorname{tr}(A\wedge dA)+\tfrac23\operatorname{tr}(A\wedge A\wedge A)$ and $d(A+sa)=dA+s\,da$, the coefficient of $s^1$ in $\operatorname{cs}(A+sa)$ is
> $$\operatorname{tr}(a\wedge dA)+\operatorname{tr}(A\wedge da)+\tfrac23\operatorname{tr}(a\wedge A\wedge A + A\wedge a\wedge A + A\wedge A\wedge a).$$
> Differentiating $\vartheta(A+sa)$ in $s$ at $0$ returns the integral of this coefficient over $M$, divided by $8\pi^2$.
>
> *Cubic collapse.* By cyclicity ($p=1$, $q=2$, sign $+1$), $\operatorname{tr}(a\wedge A\wedge A)=\operatorname{tr}(A\wedge a\wedge A)=\operatorname{tr}(A\wedge A\wedge a)$, so the three cubic terms sum to $3\operatorname{tr}(a\wedge A\wedge A)$ and $\tfrac23\cdot 3 = 2$.
>
> *Integration by parts.* Since $\operatorname{tr}$ commutes with $d$ and $A$ is a one-form, $d\operatorname{tr}(A\wedge a)=\operatorname{tr}(dA\wedge a)-\operatorname{tr}(A\wedge da)$; integrating over the closed manifold $M$ and using $\int_M d(\cdots)=0$ (Stokes, $\partial M=\varnothing$) gives $\int_M\operatorname{tr}(A\wedge da)=\int_M\operatorname{tr}(dA\wedge a)=\int_M\operatorname{tr}(a\wedge dA)$ (the last by cyclicity, $p=2$, $q=1$, sign $+1$).
>
> *Assembly.* Therefore
> $$8\pi^2\frac{d}{ds}\Big|_0\vartheta(A+sa)=2\int_M\operatorname{tr}(a\wedge dA)+2\int_M\operatorname{tr}(a\wedge A\wedge A)=2\int_M\operatorname{tr}\big(a\wedge(dA+A\wedge A)\big)=2\int_M\operatorname{tr}(a\wedge F_A).$$
> A final cyclicity swap ($p=1$, $q=2$, sign $+1$) gives $\int_M\operatorname{tr}(a\wedge F_A)=\int_M\operatorname{tr}(F_A\wedge a)$, and dividing by $8\pi^2$,
> $$\frac{d}{ds}\Big|_0\vartheta(A+sa)=\frac{1}{4\pi^2}\int_M\operatorname{tr}(F_A\wedge a). \qquad \blacksquare$$

> [!warning] Illegal but tempting shortcut: dropping the boundary term without checking $\partial M = \varnothing$
> The integration by parts in Step 3 is an *equality*, not an equality up to boundary, precisely because $M$ is closed. On a manifold *with* boundary the same computation gives $\int_M\operatorname{tr}(A\wedge da) = \int_M\operatorname{tr}(dA\wedge a) - \int_{\partial M}\operatorname{tr}(A\wedge a)$, and the surface term $\int_{\partial M}\operatorname{tr}(A\wedge a)$ does not vanish in general. Retaining it is exactly what turns the Chern–Simons functional on a manifold with boundary into a functional whose variation has a boundary contribution — the origin of the boundary conditions in Chern–Simons gauge theory. Here $M$ is closed, so the term is legitimately zero; asserting that on any manifold is the error to guard against.

**Independent sanity check (abelian toy model).** Restrict to a connection valued in a fixed one-dimensional subalgebra, $A = \mathrm{i}\, \alpha\, T$ with $T \in \mathfrak{su}(2)$ a fixed traceless element and $\alpha \in \Omega^1(M;\mathbb{R})$; then $A\wedge A = \alpha\wedge\alpha\, T^2 = 0$ (a real one-form wedged with itself vanishes), so $F_A = dA = \mathrm{i}\, d\alpha\, T$, and the density degenerates to the quadratic term. The formula predicts $d\vartheta_A(a) = \tfrac{1}{4\pi^2}\int_M\operatorname{tr}(F_A\wedge a)$; taking a variation $a = \mathrm{i}\,\beta\,T$ in the same subalgebra, $\operatorname{tr}(F_A\wedge a) = \operatorname{tr}(T^2)\, (-\,d\alpha\wedge\beta)$, a multiple of $\int_M d\alpha\wedge\beta$. Directly, $\vartheta(A + s a) = \tfrac{1}{8\pi^2}\operatorname{tr}(T^2)\int_M (-1)(\alpha + s\beta)\wedge d(\alpha+s\beta)$, whose $s$-derivative at $0$ is $\tfrac{-\operatorname{tr}(T^2)}{8\pi^2}\int_M(\beta\wedge d\alpha + \alpha\wedge d\beta) = \tfrac{-\operatorname{tr}(T^2)}{8\pi^2}\cdot 2\int_M\beta\wedge d\alpha = \tfrac{-\operatorname{tr}(T^2)}{4\pi^2}\int_M\beta\wedge d\alpha$, using $\int_M\alpha\wedge d\beta = \int_M\beta\wedge d\alpha$ (Stokes on the closed $M$, $\alpha,\beta$ one-forms). This matches the boxed formula term by term, confirming the factor $\tfrac{1}{4\pi^2}$ and the sign.

---

# Key Takeaways

**The first variation of a gauge functional is read off by integrating all derivatives onto a single density, and that density is the Euler–Lagrange equation.** The mechanical content of the computation is universal to variational problems: substitute the perturbed field, keep the linear order, and integrate by parts until the variation $a$ stands alone, wedged against a fixed form. Whatever that fixed form is, setting it to zero is the equation for critical points. Here the fixed form is the curvature $F_A$, so the critical points of Chern–Simons are the connections with $F_A = 0$ — the flat connections, as [[Thm - Critical Points of the Chern-Simons Functional are the Flat Connections|the critical-point theorem]] records. The trigger for this whole pattern is "a functional given by an integral of a polynomial in a field and its derivatives"; the reaction is "vary, integrate by parts, read off the density." The same reflex applied to $\mathcal{YM}(A) = \tfrac12\int_M|F_A|^2$ produces the Yang–Mills equation $d^A\star F_A = 0$, and applied to the action of a scalar field produces its wave equation. Recognising the shape saves rediscovering the method each time.

**Cyclicity of the trace, graded by form degree, is the workhorse identity of gauge-theory computations, and the signs are governed by a single rule.** Every step of tidying above was an instance of $\operatorname{tr}(\alpha\wedge\beta) = (-1)^{pq}\operatorname{tr}(\beta\wedge\alpha)$: the collapse of the three cubic terms (one-form past two-form, sign $+1$), and the two repackagings of $\operatorname{tr}(F_A\wedge a)$ (again $+1$). The diagnostic to internalise is that a one-form past a two-form is free ($+1$) while a one-form past a one-form flips sign ($-1$); this is why $\operatorname{tr}(A\wedge A) = 0$ for a single one-form $A$ (it equals its own negative), whereas $\operatorname{tr}(A\wedge A\wedge A)$ need not vanish. When a computation in these notes seems to produce several trace terms that "ought" to be the same, the move is almost always to group factors so that a one-form crosses an even-degree block and the sign is $+1$; when instead a term should vanish, look for a one-form crossing an odd-degree block. The cyclicity rule, with its degree-graded sign, is the first thing to reach for.

**Closedness of the base is what makes integration by parts an exact identity, and its failure is physically meaningful.** The entire computation used $M$ closed exactly once, to kill the boundary term in Step 3, and this single hypothesis is what makes $d\vartheta_A$ integration against $F_A$ with no correction. On a manifold with boundary the surface term $\int_{\partial M}\operatorname{tr}(A\wedge a)$ survives and changes the variational problem, which is the reason Chern–Simons theory on a manifold with boundary is inseparable from a choice of boundary conditions and, ultimately, from a boundary conformal field theory. For spaced practice the lesson is procedural: whenever an integration by parts is invoked, name the boundary and state why its contribution is zero (here: $\partial M = \varnothing$). A proof that silently discards a boundary term has hidden a hypothesis, and in gauge theory that hidden hypothesis is often the most interesting part. This exercise pairs naturally with [[Ex - The Chern-Simons Form Transgresses the Second Chern Form]], where the same density $\operatorname{cs}(A)$ is differentiated rather than varied, and with [[Ex - The Chern-Simons Functional along a Path of Connections]], where the variation is integrated along a path to recover the four-dimensional formula.
