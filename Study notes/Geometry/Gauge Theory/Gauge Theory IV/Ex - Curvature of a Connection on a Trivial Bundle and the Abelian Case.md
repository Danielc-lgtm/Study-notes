---
type: exercise
subject: gauge-theory
prereqs:
  - "Thm - Structure Equation for the Curvature"
  - "Def - Connection on a Principal Bundle"
  - "Def - Local Connection Form and Gauge Potential"
  - "Def - Lie-Algebra-Valued Differential Forms and Their Bracket"
difficulty: "⭐"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $G$ be a Lie group with Lie algebra $\mathfrak{g}$, let $M$ be a smooth manifold, and consider the trivial principal $G$-bundle
$$\pi = \operatorname{pr}_1\colon P = M \times G \longrightarrow M, \qquad R_h(m, g) = (m, g h),$$
with $\operatorname{pr}_2\colon M \times G \to G$ the second projection and $\theta \in \Omega^1(G; \mathfrak{g})$ the (left) Maurer–Cartan form. Fix a $\mathfrak{g}$-valued $1$-form $A \in \Omega^1(M; \mathfrak{g})$ and let $s_0\colon M \to P$, $s_0(m) = (m, e)$, be the canonical global section, so that $A = s_0^* \omega$ is the local connection form (gauge potential) of the connection $\omega$ under study.

**The task has three parts.**

1. For a connection $\omega$ on $M \times G$ with $s_0^* \omega = A$ — for abelian $G$ this is exactly $\omega = \operatorname{pr}_2^* \theta + \pi^* A$ — compute the curvature and show that its single global local form is
$$F = dA + \tfrac12[A \wedge A] \in \Omega^2(M; \mathfrak{g}),$$
and, for a matrix group, $F = dA + A \wedge A$.

2. Show that when $G$ is abelian the curvature reduces to $F = dA$, that $F$ is then automatically closed, $dF = 0$, and that the assignment $A \mapsto F$ is $\mathbb{R}$-linear.

3. Explain Bär's remark that the local structure equation $F = dA + \tfrac12[A \wedge A]$ is, read as an equation for $A$, "a semilinear partial differential equation of first order", and that it degenerates to a *linear* equation in the abelian case.

**Recall:**

The objects in play are the trivial principal bundle and its product connection, the local connection form and the structure equation, the Maurer–Cartan form, and the bracket of Lie-algebra-valued forms.

![[Thm - Structure Equation for the Curvature#Statement]]

For a connection $\omega$ on a principal $G$-bundle with curvature form $\Omega$, the structure equation is $\Omega = d\omega + \tfrac12[\omega \wedge \omega]$; pulling it back by a local section $s$ gives the local structure equation $F = dA + \tfrac12[A \wedge A]$ for $A = s^* \omega$, and for matrix groups $\tfrac12[A \wedge A] = A \wedge A$. See [[Thm - Structure Equation for the Curvature]].

![[Def - The Maurer-Cartan Form#The Definition]]

The Maurer–Cartan form $\theta \in \Omega^1(G; \mathfrak{g})$ is $\theta_g = d_g L_{g^{-1}}\colon T_g G \to T_e G = \mathfrak{g}$; it satisfies $\theta(\tilde\xi) = \xi$ on left-invariant fields, $R_h^* \theta = \operatorname{Ad}_{h^{-1}} \theta$, and (Maurer–Cartan equation) $d\theta + \tfrac12[\theta \wedge \theta] = 0$; for matrix groups $\theta = g^{-1} dg$. See [[Def - The Maurer-Cartan Form]] and [[Thm - The Maurer-Cartan Equation]].

![[Def - Lie-Algebra-Valued Differential Forms and Their Bracket#The Definition]]

For $\mathfrak{g}$-valued $1$-forms, the bracket satisfies $[\alpha \wedge \beta](X, Y) = [\alpha(X), \beta(Y)] - [\alpha(Y), \beta(X)]$, so $[A \wedge A](X, Y) = 2[A(X), A(Y)]$; for matrix Lie algebras $[A \wedge A] = 2\, A \wedge A$, which is why the structure equation's $\tfrac12$ becomes a coefficient $1$ in matrix notation. When $\mathfrak{g}$ is abelian all brackets vanish. See [[Def - Lie-Algebra-Valued Differential Forms and Their Bracket]].

The **product (canonical flat) connection** on $M \times G$ is $\omega_0 = \operatorname{pr}_2^* \theta$; it is a genuine connection ([[Def - Connection on a Principal Bundle]]) with $s_0^* \omega_0 = 0$, and its curvature vanishes, as recalled in [[Ex - The Product Connection on a Trivial Bundle and Pure Gauge Potentials]].

> [!warning] Convention: the global form of a connection on $M \times G$
> For a *nonabelian* group the naive expression $\omega = \operatorname{pr}_2^* \theta + \pi^* A$ is **not** $\operatorname{Ad}$-equivariant and hence not a connection; the correct global reconstruction from the gauge potential $A$ is
> $$\omega_{(m, g)} = \operatorname{Ad}_{g^{-1}}\big(\pi^* A\big)_{(m, g)} + \big(\operatorname{pr}_2^* \theta\big)_{(m, g)},$$
> which does satisfy $R_h^* \omega = \operatorname{Ad}_{h^{-1}} \omega$ and still has $s_0^* \omega = A$. Because $\operatorname{Ad}$ is trivial for an abelian group, this reduces to $\omega = \operatorname{pr}_2^* \theta + \pi^* A$ exactly in the abelian case named in the problem. The curvature computation below is carried out on the local form $A$, so it is valid for every $G$; the explicit total-space form is needed only for the abelian direct check.

---

# Convergent Strategy

**Problem class.** This is a *specialise-the-general-formula* problem: we take the local structure equation, which was proved in general in [[Thm - Structure Equation for the Curvature]], and read what it says on the one bundle where there is nothing to glue — the trivial bundle, covered by a single global section. The pedagogical point is to see the curvature as an explicit second-order object built from a first-order gauge potential, and to isolate the two regimes (abelian, linear; nonabelian, quadratic) that organise all of gauge theory.

**Assumption pattern.** Two hypotheses do the work. *Triviality* of the bundle means one section $s_0$ covers all of $M$, so the local curvature form $F = s_0^* \Omega$ is globally defined and there are no transition functions to check; this is why the answer is a single form rather than a family. *Commutativity* of $G$, when assumed, annihilates the bracket $\tfrac12[A \wedge A]$ and turns the structure equation into the linear relation $F = dA$. The recognisable trigger for the second is again "abelian structure group $\Rightarrow$ curvature linear in the potential".

**Theorem routing.** The route is short: pull the [[Thm - Structure Equation for the Curvature|structure equation]] $\Omega = d\omega + \tfrac12[\omega \wedge \omega]$ back by $s_0$, using that [[Thm - Pull-Back Commutes with the Exterior Derivative|pull-back commutes with $d$]] and with the bracket, to obtain $F = dA + \tfrac12[A \wedge A]$. Then specialise: abelian $\Rightarrow [A \wedge A] = 0 \Rightarrow F = dA$; and $dF = d(dA) = 0$ by [[Thm - d-Squared-is-Zero|$d^2 = 0$]]. For the abelian direct check one also uses the [[Thm - The Maurer-Cartan Equation|Maurer–Cartan equation]] to see $d(\operatorname{pr}_2^* \theta) = 0$.

**Key decision point.** The one conceptual decision is *whether to compute on the total space or on the base*. Computing $\Omega$ directly on $M \times G$ forces one to differentiate $\operatorname{pr}_2^* \theta$ and to track the mixed terms; pulling back by $s_0$ first is far cleaner and, because the bundle is trivial, loses no information. We take the pull-back route for the general statement and reserve the total-space computation for the abelian sanity check, where the Maurer–Cartan equation kills the $\theta$-terms cleanly.

---

# Legal Operations Used

This solution deploys the following legal operations of the chapter (see the topic page's Legal Operations; numbers to be reconciled with the topic page once written):

1. **Pull back the structure equation by a section to obtain the local form.** Apply $s^*$ to $\Omega = d\omega + \tfrac12[\omega \wedge \omega]$ and use $s^* d = d\, s^*$ and $s^*[\alpha \wedge \beta] = [s^*\alpha \wedge s^*\beta]$ to get $F = dA + \tfrac12[A \wedge A]$.

2. **Use a global section to make a local form global on a trivial bundle.** On $M \times G$ the section $s_0(m) = (m, e)$ is defined on all of $M$, so its pulled-back curvature is a globally defined $2$-form, and no transition functions arise.

3. **Reduce the bracket term to zero for an abelian group.** On a commutative Lie algebra every bracket vanishes, so $\tfrac12[A \wedge A] = 0$ and $F = dA$.

4. **Apply $d^2 = 0$ to conclude closedness.** From $F = dA$ deduce $dF = d(dA) = 0$.

5. **Read off linearity of a differential operator.** The exterior derivative is $\mathbb{R}$-linear, so $A \mapsto dA$ is linear; the quadratic bracket term is what breaks linearity in general.

---

# Hints

> [!note]- Hint 1
> The structure equation $\Omega = d\omega + \tfrac12[\omega \wedge \omega]$ holds on any principal bundle. What is the cleanest way to turn it into a statement on the base $M$? The trivial bundle has a section defined on *all* of $M$; pull the equation back along it.

> [!note]- Hint 2
> Pull-back is natural: $s_0^*(d\omega) = d(s_0^* \omega)$ and $s_0^*[\omega \wedge \omega] = [s_0^* \omega \wedge s_0^* \omega]$. Since $s_0^* \omega = A$, what does $s_0^* \Omega$ become? Because $s_0$ is global, that pulled-back form *is* the curvature everywhere on $M$.

> [!note]- Hint 3
> Now assume $G$ abelian. What is $[A \wedge A]$ when the Lie bracket of $\mathfrak{g}$ is identically zero? Once $F = dA$, apply the exterior derivative again and use $d \circ d = 0$.

> [!note]- Hint 4
> For "semilinear first order", write $A = A_\mu\, dx^\mu$ with $A_\mu\colon M \to \mathfrak{g}$ and expand $F = \tfrac12 F_{\mu\nu}\, dx^\mu \wedge dx^\nu$ with $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu + [A_\mu, A_\nu]$. How many derivatives of $A$ appear? Which part of the expression is linear in $A$, and which is nonlinear but derivative-free?

---

# Solution

The computation is a one-line pull-back followed by two specialisations. Because $M \times G$ is trivial, the section $s_0$ covers all of $M$, so the local structure equation *is* the global answer; assuming commutativity then kills the quadratic term and leaves the linear, closed field strength $F = dA$ of abelian gauge theory. Throughout, $A = s_0^* \omega \in \Omega^1(M; \mathfrak{g})$ is the gauge potential and $F = s_0^* \Omega \in \Omega^2(M; \mathfrak{g})$ the field strength.

**Step 1: Pull the structure equation back to the base.**

Applying $s_0^*$ to the structure equation and using naturality of $d$ and of the bracket gives $F = dA + \tfrac12[A \wedge A]$.

> [!note]- Derivation
> By the [[Thm - Structure Equation for the Curvature|structure equation]], the curvature form of $\omega$ on the total space $P = M \times G$ is
> $$\Omega = d\omega + \tfrac12[\omega \wedge \omega] \qquad \text{(structure equation).}$$
> Apply the pull-back $s_0^*$ along the canonical section $s_0(m) = (m, e)$. The exterior derivative is natural under pull-back ([[Thm - Pull-Back Commutes with the Exterior Derivative|$s_0^* d = d\, s_0^*$]]), and the bracket of Lie-algebra-valued forms is defined value-by-value from the Lie bracket of $\mathfrak{g}$, so it too commutes with pull-back, $s_0^*[\omega \wedge \omega] = [s_0^* \omega \wedge s_0^* \omega]$ ([[Def - Lie-Algebra-Valued Differential Forms and Their Bracket|naturality of the bracket]]). Hence
> $$F = s_0^* \Omega = s_0^*(d\omega) + \tfrac12 s_0^*[\omega \wedge \omega] = d(s_0^* \omega) + \tfrac12[s_0^* \omega \wedge s_0^* \omega] \qquad \text{(naturality of } d \text{ and of the bracket).}$$
> Since $s_0^* \omega = A$ by definition of the gauge potential ([[Def - Local Connection Form and Gauge Potential]]),
> $$F = dA + \tfrac12[A \wedge A].$$
> For a matrix group, $[A \wedge A] = 2\, A \wedge A$ ([[Def - Lie-Algebra-Valued Differential Forms and Their Bracket|bracket of matrix-valued $1$-forms]]), so the same identity reads
> $$F = dA + A \wedge A \qquad \text{(matrix groups).}$$
> Because the trivial bundle is covered by the single section $s_0$ defined on all of $M$, there are no overlaps and no transition functions: this $F$ is a *globally defined* $2$-form on $M$, not merely a local representative.

**Step 2: The abelian case gives $F = dA$, closed and linear in $A$.**

When $G$ is abelian the bracket term vanishes, leaving $F = dA$; then $dF = 0$ and $A \mapsto F$ is $\mathbb{R}$-linear.

> [!note]- Derivation
> Suppose $G$ is abelian, so its Lie algebra $\mathfrak{g}$ is commutative: $[\xi, \eta] = 0$ for all $\xi, \eta \in \mathfrak{g}$. Then $[A \wedge A](X, Y) = 2[A(X), A(Y)] = 0$ for all vector fields $X, Y$, so $[A \wedge A] = 0$ identically, and Step 1 gives
> $$F = dA \qquad \text{(}\mathfrak{g} \text{ abelian, so } [A \wedge A] = 0\text{).}$$
> *Closedness.* Applying the exterior derivative,
> $$dF = d(dA) = 0 \qquad \text{(by [[Thm - d-Squared-is-Zero|}d \circ d = 0\text{]]).}$$
> Thus the abelian field strength is a closed $2$-form; this is the Bianchi identity in the abelian case, and it is what makes $[F]$ a de Rham cohomology class (the first Chern class, up to a constant) in the next chapter.
> *Linearity.* The exterior derivative is $\mathbb{R}$-linear on forms: for $A, A' \in \Omega^1(M; \mathfrak{g})$ and $\lambda \in \mathbb{R}$,
> $$d(A + \lambda A') = dA + \lambda\, dA' \qquad \text{(linearity of } d\text{),}$$
> so the map $A \mapsto F = dA$ is a linear map $\Omega^1(M; \mathfrak{g}) \to \Omega^2(M; \mathfrak{g})$. In the nonabelian case this fails: $A \mapsto dA + \tfrac12[A \wedge A]$ is affine-plus-quadratic, so the sum of two connections' curvatures is not the curvature of the sum.

> [!note]- Derivation (abelian direct check on the total space)
> As a consistency check, compute $\Omega$ directly for the abelian connection $\omega = \operatorname{pr}_2^* \theta + \pi^* A$ (legitimate for abelian $G$ by the Convention callout). Since $\mathfrak{g}$ is abelian, $[\omega \wedge \omega] = 0$, so $\Omega = d\omega$. Now
> $$d\omega = d(\operatorname{pr}_2^* \theta) + d(\pi^* A) = \operatorname{pr}_2^*(d\theta) + \pi^*(dA) \qquad \text{(naturality of } d\text{).}$$
> By the [[Thm - The Maurer-Cartan Equation|Maurer–Cartan equation]] $d\theta = -\tfrac12[\theta \wedge \theta] = 0$ (abelian $\mathfrak{g}$), so $\operatorname{pr}_2^*(d\theta) = 0$ and
> $$\Omega = d\omega = \pi^*(dA).$$
> Pulling back by $s_0$ (with $\pi \circ s_0 = \operatorname{id}_M$) recovers $F = s_0^* \Omega = s_0^* \pi^*(dA) = dA$, in agreement with Step 2.

**Step 3: The structure equation as a semilinear first-order PDE for $A$.**

Writing the structure equation in coordinates shows that $F = dA + \tfrac12[A \wedge A]$ involves only first derivatives of $A$, with the top-order part linear and the bracket part nonlinear but derivative-free; hence it is semilinear of first order, and linear when $G$ is abelian.

> [!note]- Derivation
> Choose local coordinates $x^1, \dots, x^n$ on $M$ and write $A = A_\mu\, dx^\mu$ with components $A_\mu\colon M \to \mathfrak{g}$ (sum over $\mu$ understood). Expanding $F = dA + \tfrac12[A \wedge A]$ and collecting the coefficient of $dx^\mu \wedge dx^\nu$ for $\mu < \nu$, so that $F = \sum_{\mu < \nu} F_{\mu\nu}\, dx^\mu \wedge dx^\nu = \tfrac12 F_{\mu\nu}\, dx^\mu \wedge dx^\nu$ with $F_{\mu\nu} = -F_{\nu\mu}$, gives
> $$F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu + [A_\mu, A_\nu] \qquad \text{(coefficient of } dx^\mu \wedge dx^\nu \text{ in } dA + \tfrac12[A \wedge A]\text{).}$$
> Read this as an equation for the unknown $A$ (given $F$, or as the defining relation of the field strength). Classify it by the standard terminology for partial differential equations:
> - **First order.** Only first partial derivatives $\partial_\mu A_\nu$ of the unknown appear; there are no second derivatives. So the equation is of first order.
> - **Semilinear.** The highest-order (here first-order) part is $\partial_\mu A_\nu - \partial_\nu A_\mu$, which is *linear* in $A$ and whose coefficients ($\pm 1$) do not depend on $A$. A first-order equation whose principal (top-derivative) part is linear with unknown-independent coefficients, but which contains genuinely nonlinear lower-order terms, is called *semilinear*. Here the lower-order term is $[A_\mu, A_\nu]$: it involves no derivatives (it is of order zero) and is quadratic — hence nonlinear — in $A$.
> - **Abelian degeneration.** When $\mathfrak{g}$ is abelian, $[A_\mu, A_\nu] = 0$, the nonlinear term disappears, and $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ is fully *linear* in $A$. This is the precise sense of Bär's remark ([[Def - Local Connection Form and Gauge Potential|Bär, Remark 2.4.1]]): in general the local structure equation is semilinear first-order, and it becomes linear exactly in the abelian case.
>
> The physical reading is that the quadratic term $[A_\mu, A_\nu]$ is the *self-interaction* of a nonabelian gauge field: the potential $A$ acts as its own source, which is why Yang–Mills theory is nonlinear, whereas abelian (Maxwell) theory, with $[A_\mu, A_\nu] = 0$, obeys the superposition principle.

> [!note]- Complete formal solution
> **Claim.** On the trivial bundle $P = M \times G$, a connection with gauge potential $A = s_0^* \omega$ has curvature $F = dA + \tfrac12[A \wedge A] \in \Omega^2(M; \mathfrak{g})$ (for matrix groups $F = dA + A \wedge A$). If $G$ is abelian then $F = dA$, which is closed and linear in $A$; and read as an equation for $A$ the structure equation is semilinear of first order, degenerating to linear in the abelian case.
>
> Apply $s_0^*$ to the structure equation $\Omega = d\omega + \tfrac12[\omega \wedge \omega]$. Since $s_0^* d = d\, s_0^*$ and the bracket of Lie-algebra-valued forms commutes with pull-back, and $s_0^* \omega = A$,
> $$F = s_0^* \Omega = d(s_0^* \omega) + \tfrac12[s_0^* \omega \wedge s_0^* \omega] = dA + \tfrac12[A \wedge A].$$
> Because $s_0$ is defined on all of $M$, this $F$ is a globally defined $2$-form. For matrix groups $[A \wedge A] = 2\, A \wedge A$, so $F = dA + A \wedge A$.
>
> If $G$ is abelian, $[\xi, \eta] = 0$ for all $\xi, \eta \in \mathfrak{g}$, so $[A \wedge A] = 0$ and $F = dA$. Then $dF = d(dA) = 0$ by $d \circ d = 0$, and $A \mapsto dA$ is $\mathbb{R}$-linear by linearity of the exterior derivative. (Directly: for $\omega = \operatorname{pr}_2^* \theta + \pi^* A$ one has $\Omega = d\omega = \operatorname{pr}_2^*(d\theta) + \pi^*(dA) = \pi^*(dA)$ because $d\theta = -\tfrac12[\theta \wedge \theta] = 0$, and $s_0^* \Omega = dA$.)
>
> In coordinates $A = A_\mu\, dx^\mu$, the field strength has components $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu + [A_\mu, A_\nu]$. Only first derivatives of $A$ occur, and the first-order part $\partial_\mu A_\nu - \partial_\nu A_\mu$ is linear with constant coefficients while the derivative-free term $[A_\mu, A_\nu]$ is quadratic; hence the equation is semilinear of first order, and linear precisely when $G$ is abelian. $\blacksquare$

> [!warning] Illegal but tempting shortcut
> It is tempting to assert that "every connection on $M \times G$ is $\operatorname{pr}_2^* \theta + \pi^* A$", drop the $\operatorname{Ad}$-conjugation, and compute in general. For a nonabelian group this expression fails $\operatorname{Ad}$-equivariance, $R_h^*(\pi^* A) = \pi^* A \neq \operatorname{Ad}_{h^{-1}} \pi^* A$, and so is not a connection at all (see the Convention callout). The pull-back argument of Step 1 avoids the trap because it works with the gauge potential $A = s_0^* \omega$ of an *actual* connection $\omega$ and never needs the total-space formula. The extra condition that makes the naive expression legal is exactly commutativity of $G$ (or, more generally, $A$ taking values in the centre of $\mathfrak{g}$).

---

# Key Takeaways

**On a trivial bundle the curvature is just the pulled-back structure equation, and triviality is what makes the local form global.** The single move — apply $s_0^*$ to $\Omega = d\omega + \tfrac12[\omega \wedge \omega]$ — works because a trivial bundle has a section over all of $M$, so there is one gauge and nothing to glue. The reusable principle is that whenever a bundle is trivial (or one works inside a single trivialising chart), the geometry collapses to ordinary calculus with $\mathfrak{g}$-valued forms on the base, and the field strength is the explicit expression $dA + \tfrac12[A \wedge A]$. The diagnostic to carry away: the presence or absence of transition functions is the entire difference between local and global here; on the trivial bundle the "local" curvature form is already the honest global curvature, whereas on a nontrivial bundle the same expression is only a chart-dependent representative that must be checked to transform as $F_\beta = \operatorname{Ad}_{g_{\alpha\beta}^{-1}} F_\alpha$.

**The bracket term $\tfrac12[A \wedge A]$ is the exact location of all nonlinearity, and its vanishing for abelian groups is why electromagnetism is linear and Yang–Mills is not.** Abelian $\Rightarrow$ $F = dA$, which is linear in $A$ and automatically closed; nonabelian $\Rightarrow$ the quadratic self-coupling $[A_\mu, A_\nu]$ appears, the map $A \mapsto F$ ceases to be linear, and the field sources itself. The trigger condition is simply commutativity of the structure group. This single term controls a cascade of downstream facts: whether the field strength is closed on the nose (abelian) or only covariantly closed via the Bianchi identity $d^\nabla F = 0$ (general); whether curvatures superpose; and whether the Yang–Mills equations are linear or nonlinear. When reading any gauge-theoretic formula, locate the bracket term first — it tells you at a glance which regime you are in.

**Classifying the structure equation as a semilinear first-order PDE names the two features that matter: it constrains only first derivatives of the potential, and its nonlinearity is derivative-free.** "First order" says the field strength sees only $\partial_\mu A_\nu$, never second derivatives — so a potential is determined by its field only up to the gauge freedom that the first-order kernel encodes. "Semilinear" says the top-order part $\partial_\mu A_\nu - \partial_\nu A_\mu$ is linear with fixed coefficients, so the equation's principal symbol is that of the abelian theory; the nonabelian complications sit entirely in the zeroth-order quadratic term. This classification is not idle taxonomy: it is what tells the analyst that the linearisation of the Yang–Mills or Seiberg–Witten operator at a connection has the same leading symbol as the abelian model, which is precisely the input to the elliptic theory of later chapters, where the Fredholm and index properties of the linearised equations are established. Recognising an equation as semilinear first-order is the standing cue that its hard analysis is governed by its linear principal part while its geometry lives in the lower-order nonlinearity.
