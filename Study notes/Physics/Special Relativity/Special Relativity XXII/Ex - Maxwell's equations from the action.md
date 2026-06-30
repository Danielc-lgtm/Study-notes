---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - Maxwell Equations from a Principle of Least Action"
  - "Def - The Four-Potential"
  - "Thm - Noether Theorem (Relativistic Particle)"
tags: [physics, special-relativity]
---

# Problem Statement

Derive the inhomogeneous Maxwell equation from the principle of least action, taking the four-potential as the dynamical field.

1. State the electromagnetic action $S = \int(-\tfrac14 F_{\mu\nu}F^{\mu\nu} + A_\mu J^\mu)\,d^4x$ and explain why the free term $-\tfrac14 F^2$ is the unique acceptable choice (Lorentz scalar, quadratic, first-order in $\partial A$).
2. Derive the general Euler–Lagrange field equation $\frac{\partial L}{\partial\varphi_A} - \partial_\alpha(\frac{\partial L}{\partial(\partial_\alpha\varphi_A)}) = 0$ by varying the action and discarding the boundary term.
3. Compute $\frac{\partial\mathcal L}{\partial A_\beta} = J^\beta$ and $\frac{\partial\mathcal L}{\partial(\partial_\alpha A_\beta)} = F^{\beta\alpha}$, and assemble them into $\nabla_\mu F^{\mu\nu} = \mu_0 J^\nu$.
4. Explain why the homogeneous equation $dF = 0$ is automatically satisfied and needs no derivation, and show that the interaction term $\int A_\mu J^\mu$ reduces, for a single particle, to the minimal-coupling term $q\int A\cdot dX$ of topic XV.

**Recall:**

![[Thm - Maxwell Equations from a Principle of Least Action#Statement]]

The [[Def - The Four-Potential|four-potential]] is $A_\mu$, with $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$. The [[Thm - Noether Theorem (Relativistic Particle)|Euler–Lagrange machinery]] for a particle generalises to fields with the worldline parameter replaced by the four spacetime coordinates. The point-charge current is $J = q\int\delta_{X(\tau)}U\,d\tau$, and the [[Def - Lagrangian for a Particle in a Vector Field|minimal-coupling term]] for a particle in a potential is $q\int A\cdot dX$.

---

# Convergent Strategy

**Problem class.** A *derive-the-field-equations-from-an-action* problem, the fifth and capstone target of the [[Special Relativity XXII — Maxwell's Equations#Problem-Solving Strategy|topic strategy]]: write the Lorentz-scalar Lagrangian, vary, and read off Maxwell. The routine is the calculus of variations applied to a field.

**Assumption pattern.** The given is the dynamical field $A$ and the requirement of Poincaré invariance. The signpost is "Lorentz scalar Lagrangian" — the demand for invariance plus simplicity (quadratic, first-order) singles out $-\tfrac14 F^2$ for the free term and $A_\mu J^\mu$ for the interaction. What this unlocks is that varying with respect to $A$ produces the field equation, with the interaction supplying the source.

**Theorem routing.** The route is: action $S = \int(-\tfrac14 F^2 + A\cdot J)\,d^4x \to$ vary, integrate by parts, drop boundary term $\to$ Euler–Lagrange equation (Lemma 1 of [[Thm - Maxwell Equations from a Principle of Least Action]]); compute the two derivatives (Lemmas 2, 3) $\to$ assemble (Lemma 4) $\to \nabla_\mu F^{\mu\nu} = \mu_0 J^\nu$. The homogeneous equation routes through $F = dA \Rightarrow dF = 0$; the interaction reduces to minimal coupling via the point-charge current.

**Key decision point.** The crux is the differentiation $\frac{\partial}{\partial(\partial_\alpha A_\beta)}(F_{\mu\nu}F^{\mu\nu}) = -4F^{\alpha\beta}$, where one must treat $\partial_\alpha A_\beta$ and $\partial_\beta A_\alpha$ as independent variables and account for the antisymmetry of $F$ and the two index-matchings — the factor of $4$ that cancels the $\tfrac14$. Getting this coefficient wrong (a stray factor of $2$) corrupts the field equation. The decision is to differentiate carefully, tracking every way the index pair $(\alpha\beta)$ can match $(\mu\nu)$.

---

# Legal Operations Used

1. **Operation 1 from the topic page (write the field as $F = dA$).** The action uses $F = dA$, so the dynamical variable is $A$ and the homogeneous equation is automatic.

2. **Operation 3 from the topic page (convert $d{\star}F$ to the divergence).** The field equation emerges in divergence form $\nabla_\mu F^{\mu\nu} = \mu_0 J^\nu$, the form the variation naturally produces.

3. **The variational machinery of topic XV.** The general Euler–Lagrange field equation is the field generalisation of the particle [[Thm - Noether Theorem (Relativistic Particle)|Euler–Lagrange equation]], applied to the electromagnetic Lagrangian.

---

# Hints

> [!note]- Hint 1
> The free Lagrangian must be a Lorentz scalar built from $F$ (so the equations are covariant), quadratic in the field (so they are linear), and first-order in derivatives of $A$ (so $F$ appears, not $\partial F$). The only such scalar is $F_{\mu\nu}F^{\mu\nu}$ — the first invariant. (The second invariant $\star F_{\mu\nu}F^{\mu\nu}$ is a total derivative, contributing nothing to the equations of motion.) The coefficient $-\tfrac14$ is a normalisation.

> [!note]- Hint 2
> Vary $S = \int L\,d^4x$: $\delta S = \int(\frac{\partial L}{\partial\varphi}\delta\varphi + \frac{\partial L}{\partial(\partial_\alpha\varphi)}\partial_\alpha\delta\varphi)\,d^4x$. Integrate the second term by parts: $\frac{\partial L}{\partial(\partial_\alpha\varphi)}\partial_\alpha\delta\varphi = \partial_\alpha(\frac{\partial L}{\partial(\partial_\alpha\varphi)}\delta\varphi) - \partial_\alpha(\frac{\partial L}{\partial(\partial_\alpha\varphi)})\delta\varphi$. The total-derivative term integrates to a boundary flux, which vanishes since $\delta\varphi = 0$ on $\partial\mathcal U$.

> [!note]- Hint 3
> Interaction: $\frac{\partial}{\partial A_\beta}(A_\mu J^\mu) = J^\beta$. Free term: $\frac{\partial}{\partial(\partial_\alpha A_\beta)}(-\tfrac14 F_{\mu\nu}F^{\mu\nu})$. Use $\frac{\partial F_{\mu\nu}}{\partial(\partial_\alpha A_\beta)} = \delta_\mu^\alpha\delta_\nu^\beta - \delta_\nu^\alpha\delta_\mu^\beta$ and the chain rule, getting $-\tfrac12 F^{\mu\nu}(\delta_\mu^\alpha\delta_\nu^\beta - \delta_\nu^\alpha\delta_\mu^\beta) = -\tfrac12(F^{\alpha\beta} - F^{\beta\alpha}) = -F^{\alpha\beta} = F^{\beta\alpha}$.

> [!note]- Hint 4
> The dynamical variable is $A$, and $F = dA$ is *defined*, so $dF = d(dA) = 0$ identically — the homogeneous equation is built in, not derived. For the interaction: $\int A_\mu J^\mu\,d^4x$ with $J = q\int\delta_{X(\tau)}U\,d\tau$, integrating over the spatial slice, collapses to $q\int A_\mu\dot X^\mu\,d\tau = q\int A\cdot dX$.

---

# Solution

Maxwell's equations follow from the simplest Lorentz-scalar action. Step 1 fixes the Lagrangian; Step 2 derives the general field equation; Step 3 computes the derivatives and assembles the result; Step 4 explains the automatic homogeneous equation and the minimal-coupling connection. The non-obvious move is in Step 3, the careful differentiation of $F^2$ with respect to $\partial A$.

**Step 1: The action and why $-\tfrac14 F^2$ is forced.**

> [!note]- Derivation
> The electromagnetic action is
> $$S = \int_{\mathcal U}\mathcal L\,d^4x, \qquad \mathcal L = -\frac{1}{4}F_{\mu\nu}F^{\mu\nu} + A_\mu J^\mu,$$
> with $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ and $A$ the dynamical field. **Why this Lagrangian?** The free term must satisfy three demands: (i) it is a **Lorentz scalar**, so the field equations are covariant — this requires building it from $F$ by metric contraction; (ii) it is **quadratic** in the field, so the equations are linear (electromagnetism is a linear theory); (iii) it is **first-order** in derivatives of $A$, so $F$ (not $\partial F$) appears. The only scalar meeting all three is the first invariant $F_{\mu\nu}F^{\mu\nu}$. (The second invariant ${\star}F_{\mu\nu}F^{\mu\nu} = \partial_\mu(\cdots)$ is a total derivative and contributes nothing to the equations of motion.) The coefficient $-\tfrac14$ is a normalisation fixing the field's strength, chosen so the field equation comes out with the standard constants. The interaction term $A_\mu J^\mu$ is the unique Lorentz-scalar linear coupling of the potential to the current.

**Step 2: The general Euler–Lagrange field equation.**

> [!note]- Derivation
> For a Lagrangian $L(\varphi_A, \partial_\alpha\varphi_A)$, vary the action under $\delta\varphi$ vanishing on the boundary:
> $$\delta S = \int_{\mathcal U}\left[\frac{\partial L}{\partial\varphi_A}\delta\varphi_A + \frac{\partial L}{\partial(\partial_\alpha\varphi_A)}\partial_\alpha\delta\varphi_A\right]d^4x.$$
> Integrate the second term by parts: $\frac{\partial L}{\partial(\partial_\alpha\varphi_A)}\partial_\alpha\delta\varphi_A = \partial_\alpha[\frac{\partial L}{\partial(\partial_\alpha\varphi_A)}\delta\varphi_A] - \partial_\alpha[\frac{\partial L}{\partial(\partial_\alpha\varphi_A)}]\delta\varphi_A$. The total-derivative term is a four-divergence $\partial_\alpha V^\alpha$ with $V^\alpha = \frac{\partial L}{\partial(\partial_\alpha\varphi_A)}\delta\varphi_A$; by the four-dimensional [[Thm - Gauss-Ostrogradsky Theorem (3D and 4D)|Gauss theorem]], $\int_{\mathcal U}\partial_\alpha V^\alpha\,d^4x = \oint_{\partial\mathcal U}V^\alpha\,dS_\alpha = 0$ since $\delta\varphi_A = 0$ on $\partial\mathcal U$. So
> $$\delta S = \int_{\mathcal U}\left[\frac{\partial L}{\partial\varphi_A} - \partial_\alpha\!\left(\frac{\partial L}{\partial(\partial_\alpha\varphi_A)}\right)\right]\delta\varphi_A\,d^4x.$$
> Stationarity $\delta S = 0$ for all $\delta\varphi_A$ and all $\mathcal U$ forces the bracket to vanish — the **Euler–Lagrange field equation**.

**Step 3: The two derivatives and the field equation.**

> [!note]- Derivation
> **Interaction term.** $\frac{\partial\mathcal L}{\partial A_\beta} = \frac{\partial}{\partial A_\beta}(A_\mu J^\mu) = J^\mu\delta_\mu^\beta = J^\beta$ (the current is a fixed external source, independent of $A$).
>
> **Free term.** Differentiate $-\tfrac14 F_{\mu\nu}F^{\mu\nu}$ with respect to the independent variable $\partial_\alpha A_\beta$. Since $\frac{\partial F_{\mu\nu}}{\partial(\partial_\alpha A_\beta)} = \delta_\mu^\alpha\delta_\nu^\beta - \delta_\nu^\alpha\delta_\mu^\beta$ (from $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$),
> $$\frac{\partial}{\partial(\partial_\alpha A_\beta)}\!\left(-\tfrac14 F_{\mu\nu}F^{\mu\nu}\right) = -\tfrac14\cdot 2\,F^{\mu\nu}\frac{\partial F_{\mu\nu}}{\partial(\partial_\alpha A_\beta)} = -\tfrac12 F^{\mu\nu}(\delta_\mu^\alpha\delta_\nu^\beta - \delta_\nu^\alpha\delta_\mu^\beta) = -\tfrac12(F^{\alpha\beta} - F^{\beta\alpha}) = -F^{\alpha\beta} = F^{\beta\alpha},$$
> using $F^{\alpha\beta} = -F^{\beta\alpha}$. The factor of $2$ (from the two $F$'s) and the antisymmetry (from the two index-matchings) together cancel the $\tfrac14$, leaving the clean $F^{\beta\alpha}$.
>
> **Assemble.** The Euler–Lagrange equation is $\frac{\partial\mathcal L}{\partial A_\beta} - \partial_\alpha\frac{\partial\mathcal L}{\partial(\partial_\alpha A_\beta)} = J^\beta - \partial_\alpha F^{\beta\alpha} = 0$, i.e.
> $$\partial_\alpha F^{\beta\alpha} = J^\beta \qquad\Longleftrightarrow\qquad \nabla_\mu F^{\mu\nu} = \mu_0 J^\nu$$
> (with $\varepsilon_0 = 1$; restoring constants via $\mathcal L = -\tfrac{\varepsilon_0}{4}F^2 + A\cdot J$ gives $\varepsilon_0\partial_\alpha F^{\beta\alpha} = J^\beta$, i.e. $\partial_\alpha F^{\beta\alpha} = \mu_0 J^\beta$). This is the **inhomogeneous [[Thm - Maxwell Equations|Maxwell equation]]**.

**Step 4: The homogeneous equation is automatic; the interaction is minimal coupling.**

> [!note]- Derivation
> **Homogeneous equation.** The dynamical variable is $A$, and $F = dA$ is *defined*. So $dF = d(dA) = 0$ holds identically — the homogeneous equation is a constraint built into the choice of variable, not an equation of motion, and requires no variation. This is the deep reason the action uses the potential: it makes half of Maxwell automatic, leaving only the inhomogeneous half to derive.
>
> **Minimal coupling.** The interaction term, for a single particle with current $J = q\int\delta_{X(\tau)}U\,d\tau$, is
> $$\int_{\mathcal U}A_\mu J^\mu\,d^4x = \int_{\mathcal U}A_\mu(x)\,q\!\int\delta_{X(\tau)}(x)U^\mu(\tau)\,d\tau\,d^4x = q\int A_\mu(X(\tau))\,U^\mu(\tau)\,d\tau = q\int A\cdot dX,$$
> where the spacetime delta collapses the $d^4x$ integral onto the worldline and $U^\mu d\tau = dX^\mu$. This is exactly the [[Def - Lagrangian for a Particle in a Vector Field|minimal-coupling term]] $q\int A\cdot dX$ of topic XV that produces the Lorentz force. **The field's coupling to its source and the particle's coupling to the field are the same term**, viewed from the field side versus the particle side — the unity of the matter–field system.

> [!note]- Complete formal solution
> The action $S = \int(-\tfrac14 F_{\mu\nu}F^{\mu\nu} + A_\mu J^\mu)\,d^4x$ has the unique Lorentz-scalar, quadratic, first-order free term $-\tfrac14 F^2$ and the unique linear coupling $A\cdot J$. Varying with respect to $A$ and integrating by parts (boundary term dead by the four-dimensional Gauss theorem since $\delta A = 0$ on $\partial\mathcal U$) gives the Euler–Lagrange equation $\frac{\partial\mathcal L}{\partial A_\beta} - \partial_\alpha\frac{\partial\mathcal L}{\partial(\partial_\alpha A_\beta)} = 0$. Computing $\frac{\partial\mathcal L}{\partial A_\beta} = J^\beta$ and $\frac{\partial\mathcal L}{\partial(\partial_\alpha A_\beta)} = F^{\beta\alpha}$ (the $\tfrac14$ cancelled by the factor of $2$ and the antisymmetry) gives $J^\beta - \partial_\alpha F^{\beta\alpha} = 0$, i.e. $\nabla_\mu F^{\mu\nu} = \mu_0 J^\nu$. The homogeneous equation $dF = 0$ is automatic from $F = dA$. The interaction $\int A_\mu J^\mu$ reduces, for a single particle, to $q\int A\cdot dX$, the minimal-coupling term of topic XV. $\blacksquare$

---

# Key Takeaways

**The action is the more fundamental object: postulate the scalar Lagrangian, and the field equations are its variational shadow.** The deep methodological lesson, which reorganises all of physics, is to specify a theory not by its equations of motion but by a single scalar action functional, from which the equations follow by demanding stationarity. This has three advantages: economy (one scalar $\mathcal L$ encodes all dynamics), automatic covariance (requiring $\mathcal L$ to be a Lorentz scalar guarantees Lorentz-covariant equations), and quantisability (the path integral $\int\mathcal D A\,e^{iS/\hbar}$ takes the action as input). The reusable principle: to find a relativistic field theory, write the simplest Lorentz scalar built from the field and its derivatives, then vary. For electromagnetism this is $-\tfrac14 F^2$; for gravity it is the Ricci scalar $R$ (Einstein–Hilbert); for a scalar field it is $\tfrac12(\partial\phi)^2 - V(\phi)$. The action principle is the unifying language in which every fundamental theory is most naturally stated, and the Euler–Lagrange equation is the universal machine turning a Lagrangian into its dynamics.

**Symmetry plus simplicity nearly determines the Lagrangian, and hence the physics.** The striking content of Step 1 is that the form of electromagnetism is almost forced by two requirements: Poincaré invariance (the Lagrangian must be a Lorentz scalar) and renormalisability/simplicity (quadratic, first-order). The only scalar meeting these is $F_{\mu\nu}F^{\mu\nu}$, so the free Lagrangian is essentially unique up to normalisation. The reusable insight is that the symmetries a theory is required to respect, combined with a restriction to the simplest terms, dramatically constrain its possible Lagrangians — often to a unique choice. This "build the most general invariant Lagrangian and keep the leading terms" is the method of effective field theory, and it is why the fundamental interactions take the forms they do: the gauge symmetry forces the $-\tfrac14 F^2$ structure, and generalising the symmetry group from $\mathrm{U}(1)$ to nonabelian groups generates the Standard Model. Recognising "what symmetry must this respect?" is the first step in writing any field theory's action.

**The homogeneous Maxwell equation is automatic because $A$, not $F$, is the dynamical variable — and the field's coupling to its source is the particle's minimal coupling.** Two unifying points close the derivation. First, choosing the potential $A$ as the variable (with $F = dA$ defined) makes $dF = 0$ an identity, so only the inhomogeneous equation must be derived — the same reason, $d^2 = 0$, that makes the homogeneous equation free in the direct treatment of §22.1. This is why every Lagrangian formulation of electromagnetism uses the potential: it builds in half of Maxwell automatically. Second, the interaction term $\int A_\mu J^\mu$ is *identical* to the minimal-coupling term $q\int A\cdot dX$ that gave the Lorentz force for a particle in topic XV — the field interacting with its current and the particle interacting with the field are the same coupling, seen from two sides. The transferable principle: in a complete matter–field action, the same interaction term governs both how the field responds to matter (sourcing $F$) and how matter responds to the field (the Lorentz force), and by Noether's theorem the gauge symmetry of this term is exactly charge conservation. The action unifies the two halves of electromagnetism — field dynamics and particle dynamics — into one variational principle.
