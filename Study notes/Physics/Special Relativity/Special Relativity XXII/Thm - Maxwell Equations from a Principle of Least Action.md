---
type: theorem
subject: special-relativity
prereqs:
  - "Thm - Maxwell Equations"
  - "Def - The Four-Potential"
  - "Thm - Noether Theorem (Relativistic Particle)"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use the signature $\eta = \mathrm{diag}(1,-1,-1,-1)$. The dynamical field is the [[Def - The Four-Potential|four-potential]] $A$, components $A_\mu$, with $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ and $F^{\mu\nu} = \eta^{\mu\alpha}\eta^{\nu\beta}F_{\alpha\beta}$. The [[Def - The Electric Four-Current|four-current]] is $J$, components $j^\mu$ (or $J^\mu$). The **Lagrangian density** is $\mathcal L$, a scalar field; the **action** is $S = \int_{\mathcal U}\mathcal L\,d^4x$ over a four-dimensional domain $\mathcal U$ with $\partial\mathcal U$ the boundary. A general tensor field is $\varphi$ with components $\varphi_A$ (multi-index $A$). The field variation is $\delta\varphi$, vanishing on $\partial\mathcal U$. The constants satisfy $\varepsilon_0\mu_0 = 1$. Full registry on [[Special Relativity XXII — Maxwell's Equations]].

---

# Statement

> **Theorem (Maxwell from least action).** The inhomogeneous [[Thm - Maxwell Equations|Maxwell equation]] $\nabla_\mu F^{\mu\nu} = \mu_0 J^\nu$ is the Euler–Lagrange field equation of the action
> $$S = \int_{\mathcal U}\mathcal L\,d^4x, \qquad \mathcal L = -\frac{1}{4}\,F_{\mu\nu}F^{\mu\nu} + A_\mu J^\mu$$
> (or, with $\varepsilon_0$ explicit, $\mathcal L = -\tfrac{\varepsilon_0}{4}F_{\mu\nu}F^{\mu\nu} + A_\mu J^\mu$), with the four-potential $A$ taken as the dynamical field and $F = dA$.
> The homogeneous Maxwell equation $dF = 0$ is **automatically** satisfied, since it is built into the assumption $F = dA$.

> **The field equation.** For a general field theory with Lagrangian density $\mathcal L = L(\varphi_A, \partial_\alpha\varphi_A)$ and action $S = \int\mathcal L\,d^4x$, stationarity $\delta S = 0$ under variations $\delta\varphi$ vanishing on $\partial\mathcal U$ gives the **Euler–Lagrange field equations**
> $$\frac{\partial L}{\partial\varphi_A} - \frac{\partial}{\partial x^\alpha}\!\left(\frac{\partial L}{\partial(\partial_\alpha\varphi_A)}\right) = 0.$$
> Applied to the electromagnetic Lagrangian with $\varphi = A$, this yields $\partial_\alpha F^{\beta\alpha} = \mu_0 j^\beta$, i.e. $\nabla_\mu F^{\mu\nu} = \mu_0 J^\nu$.

---

# Motivation

This theorem closes the logical circle of the chapter. Maxwell's equations were introduced in §22.1 as a *postulate* — the law was simply asserted. But there is a deeper way to do physics: postulate not the equations of motion but an **action**, a single scalar functional, and *derive* the equations of motion as the condition that the action be stationary. This is the principle of least action, and it is the modern foundation of all of physics, from particle mechanics to quantum field theory to general relativity. The theorem shows that electromagnetism fits this framework: there is an action whose Euler–Lagrange equations are precisely Maxwell's equations.

Why prefer an action to the equations themselves? Three reasons, all profound. First, **economy**: a single scalar $\mathcal L$ encodes all the dynamics, and the requirement that it be a Lorentz scalar automatically guarantees the equations are Lorentz-covariant — invariance is built in, not checked afterward. Second, **Noether's theorem**: every continuous symmetry of the action yields a conserved quantity, so the action organises the conservation laws (charge conservation here corresponds to the gauge symmetry $A \to A + d\chi$). Third, **quantisation**: the path-integral formulation of quantum field theory takes the action as its fundamental input, $e^{iS/\hbar}$ weighting each field configuration, so the classical action *is* the bridge to the quantum theory. The action is not a convenience; it is the more fundamental object, and the field equations are its shadow.

The form of the Lagrangian is nearly forced, and seeing why is the conceptual heart of the theorem. The free term must be a Lorentz scalar built from the field, quadratic (so the equations are linear) and first-order in derivatives of $A$; the *only* such scalar is $F_{\mu\nu}F^{\mu\nu}$, the first electromagnetic invariant. The coefficient $-\tfrac14$ is a normalisation fixing the strength. The interaction term must couple the field to its source as a Lorentz scalar; the unique linear coupling is $A_\mu J^\mu$, the contraction of the potential with the current — and this term is not new, for a single particle it reduces to the [[Def - Lagrangian for a Particle in a Vector Field|minimal-coupling term]] $q\!\int\!A\cdot dX$ that produced the Lorentz force in topic XV. So the electromagnetic action is the simplest Lorentz-invariant functional one can write, and that simplicity is the modern statement of why electromagnetism has the form it does.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's precondition is "the dynamical field is $A$, with action $S = \int(-\tfrac14 F^2 + A\cdot J)\,d^4x$".

The first disguised source is **"a Lorentz-scalar Lagrangian quadratic in the field strength is given"**. Any field theory whose free Lagrangian is the unique quadratic scalar in a field strength yields, by the same variation, a Maxwell-type equation. The bridge is that the Euler–Lagrange machinery cares only about the functional form, not the physical interpretation. The nonobviousness is that "write the simplest scalar Lagrangian and vary" reconstructs the dynamics. *Example problem:* given a free Lagrangian $-\tfrac14 F^2$ for some field strength, derive its source-free equation of motion.

The second disguised source is **"a minimal-coupling interaction $A_\mu J^\mu$ between a gauge field and a current"**. Whenever a gauge field couples to a conserved current through the term $A_\mu J^\mu$, varying $A$ produces a source term $J^\nu$ in the field equation. The bridge is $\partial\mathcal L/\partial A_\beta = j^\beta$ from the interaction term. *Example problem:* show that adding $A_\mu J^\mu$ to the free action puts the current on the right-hand side of the field equation.

The third disguised source is **"the field theory must be invariant under the Poincaré group"**. Demanding Poincaré invariance restricts the Lagrangian to scalars built from $F$ and $J$ by metric contractions; the simplest such scalar is $-\tfrac14 F^2 + A\cdot J$, so Poincaré invariance plus simplicity *forces* electromagnetism. The bridge is the requirement that $\mathcal L$ be a Lorentz scalar. *Example problem:* enumerate the Lorentz scalars available from $F$ and $A$ and identify the unique renormalisable choice.

**Targets (Output Amplification)**

The conclusion is "$\nabla_\mu F^{\mu\nu} = \mu_0 J^\nu$ is the Euler–Lagrange equation of the electromagnetic action".

Combine the conclusion with **Noether's theorem and the gauge symmetry**. The action is invariant under $A \to A + d\chi$ (up to a boundary term, given $\nabla\cdot J = 0$); by Noether's theorem this gauge symmetry corresponds to charge conservation. The further result is that charge conservation is the Noether identity of the gauge symmetry — a second derivation of $\nabla\cdot J = 0$. The combination ties the gauge redundancy to the conservation law. *Example:* derive charge conservation from the gauge invariance of the action.

Combine the conclusion with **the energy–momentum tensor**. Varying the action with respect to the *metric* (or applying Noether to translations) gives the electromagnetic energy–momentum tensor $T^{\mu\nu} = F^{\mu\alpha}F^\nu{}_\alpha - \tfrac14\eta^{\mu\nu}F^2$. The further result is the energy and momentum carried by the field, the source of gravity. The combination is the bridge to [[Special Relativity XXIII — The Energy-Momentum Tensor and Field Energy|topic XXIII]]. *Example:* obtain the field energy density from the action by metric variation.

Combine the conclusion with **the nonabelian generalisation**. Replacing the abelian $F = dA$ by the nonabelian curvature $F = dA + A\wedge A$ and the scalar $F_{\mu\nu}F^{\mu\nu}$ by $\mathrm{tr}(F_{\mu\nu}F^{\mu\nu})$ gives the Yang–Mills action, whose field equation $D_\mu F^{\mu\nu} = J^\nu$ is nonlinear. The further result is the gauge theory of the strong and weak interactions. The combination shows electromagnetism is the abelian seed of the Standard Model. *Example:* write the Yang–Mills action and vary to get the nonabelian field equation.

---

# Why Is It True

The bolded mechanism: **varying $-\tfrac14 F_{\mu\nu}F^{\mu\nu}$ with respect to $A_\beta$ brings down $\partial L/\partial(\partial_\alpha A_\beta) = -F^{\beta\alpha}$, so the Euler–Lagrange divergence term is $\partial_\alpha F^{\beta\alpha}$; varying $A_\mu J^\mu$ gives $\partial L/\partial A_\beta = j^\beta$; setting the Euler–Lagrange combination to zero is exactly $\partial_\alpha F^{\beta\alpha} = \mu_0 j^\beta$.** The whole derivation is one differentiation of the Lagrangian with respect to the field and one with respect to its gradient.

Take the general field-equation step first, because it is the engine. For a Lagrangian $L(\varphi_A, \partial_\alpha\varphi_A)$, the variation of the action under $\delta\varphi$ is $\delta S = \int(\frac{\partial L}{\partial\varphi_A}\delta\varphi_A + \frac{\partial L}{\partial(\partial_\alpha\varphi_A)}\delta\partial_\alpha\varphi_A)\,d^4x$. Integrate the second term by parts: $\frac{\partial L}{\partial(\partial_\alpha\varphi_A)}\partial_\alpha\delta\varphi_A = \partial_\alpha(\frac{\partial L}{\partial(\partial_\alpha\varphi_A)}\delta\varphi_A) - \partial_\alpha(\frac{\partial L}{\partial(\partial_\alpha\varphi_A)})\delta\varphi_A$. The total-derivative term integrates to a boundary flux that vanishes because $\delta\varphi = 0$ on $\partial\mathcal U$ (by the four-dimensional Gauss theorem). What remains is $\delta S = \int[\frac{\partial L}{\partial\varphi_A} - \partial_\alpha(\frac{\partial L}{\partial(\partial_\alpha\varphi_A)})]\delta\varphi_A\,d^4x$. For this to vanish for *every* variation $\delta\varphi_A$ and *every* domain $\mathcal U$, the bracket must vanish pointwise — that is the Euler–Lagrange equation. This is the field-theory version of the particle Euler–Lagrange equation from [[Thm - Noether Theorem (Relativistic Particle)|topic XV]], with the single evolution parameter $\lambda$ replaced by the four coordinates $x^\alpha$ and the coordinates $\varphi$ replaced by the field components.

Now apply it to electromagnetism. The Lagrangian is $\mathcal L = -\tfrac14 F_{\mu\nu}F^{\mu\nu} + A_\mu j^\mu$, with $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$, so $\mathcal L$ depends on $A$ (through the interaction term) and on $\partial A$ (through $F$). The interaction term gives $\partial\mathcal L/\partial A_\beta = j^\beta$ immediately. The free term requires differentiating $F_{\mu\nu}F^{\mu\nu}$ with respect to $\partial_\alpha A_\beta$: since $F_{\mu\nu}F^{\mu\nu} = (\partial_\mu A_\nu - \partial_\nu A_\mu)F^{\mu\nu}$ and $F$ is antisymmetric, the derivative is $\frac{\partial}{\partial(\partial_\alpha A_\beta)}(-\tfrac14 F_{\mu\nu}F^{\mu\nu}) = -F^{\alpha\beta} = F^{\beta\alpha}$ (the factor $-\tfrac14$ and the two ways the index pair appears combine to remove the $\tfrac14$). Plugging into Euler–Lagrange: $\frac{\partial\mathcal L}{\partial A_\beta} - \partial_\alpha\frac{\partial\mathcal L}{\partial(\partial_\alpha A_\beta)} = j^\beta - \partial_\alpha F^{\beta\alpha} = 0$, i.e. $\partial_\alpha F^{\beta\alpha} = j^\beta$ (with $\varepsilon_0 = 1$; restoring it, $\partial_\alpha F^{\beta\alpha} = \mu_0 j^\beta$). This is $\nabla_\mu F^{\mu\nu} = \mu_0 J^\nu$.

Why is the homogeneous equation automatic? Because the dynamical variable is $A$, not $F$, and $F$ is *defined* as $dA$. So $dF = d(dA) = 0$ holds identically, before any variation — it is a constraint built into the choice of dynamical field, not an equation of motion. This is the deep reason the action principle uses the potential: it makes half of Maxwell automatic, leaving only the inhomogeneous half to be derived, exactly as in the direct treatment of §22.1. The potential is the right variable precisely because it trivialises the homogeneous equation.

---

# What Makes This Hard

The conceptual hurdle is the shift from "postulate the equations" to "postulate the action and derive the equations" — and recognising that the action is the more fundamental object, the one that quantises. The technical crux is the differentiation $\frac{\partial}{\partial(\partial_\alpha A_\beta)}(F_{\mu\nu}F^{\mu\nu})$: one must carefully treat $\partial_\alpha A_\beta$ and $\partial_\beta A_\alpha$ as independent variables, account for the antisymmetry of $F$, and track that the index pair $(\mu\nu)$ matches $(\alpha\beta)$ in two ways, which is what cancels the $\tfrac14$ and leaves $F^{\beta\alpha}$; dropping the factor of two here gives the wrong coefficient. A secondary subtlety is that the homogeneous equation is *not* derived — it is assumed via $F = dA$ — and students sometimes expect both equations to fall out of the variation.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Derive the general Euler–Lagrange field equation by varying the action and integrating by parts (boundary term dies). Then compute the two derivatives of the electromagnetic Lagrangian: $\partial\mathcal L/\partial A_\beta = j^\beta$ from the interaction term, and $\partial\mathcal L/\partial(\partial_\alpha A_\beta) = F^{\beta\alpha}$ from the free term. Plug in: the field equation is $\partial_\alpha F^{\beta\alpha} = \mu_0 j^\beta$. Note $dF = 0$ is automatic from $F = dA$.

**Subgoal decomposition:**

1. **Derive the general field equation.** Vary $S = \int L\,d^4x$, integrate the gradient term by parts, drop the boundary flux.
   - *Hint:* $\delta\varphi = 0$ on $\partial\mathcal U$ kills the total-derivative term by the four-dimensional Gauss theorem; arbitrariness of $\delta\varphi$ forces the bracket to vanish.
   - *Why needed:* It gives the Euler–Lagrange equation $\partial L/\partial\varphi_A - \partial_\alpha[\partial L/\partial(\partial_\alpha\varphi_A)] = 0$.

2. **Differentiate the interaction term.** Compute $\partial\mathcal L/\partial A_\beta$ from $A_\mu j^\mu$.
   - *Hint:* $\partial(A_\mu j^\mu)/\partial A_\beta = j^\beta$ ($j$ does not depend on $A$).
   - *Why needed:* It supplies the source $j^\beta$ on the right.

3. **Differentiate the free term.** Compute $\partial\mathcal L/\partial(\partial_\alpha A_\beta)$ from $-\tfrac14 F_{\mu\nu}F^{\mu\nu}$.
   - *Hint:* Treat $\partial_\alpha A_\beta$ as independent; the antisymmetry of $F$ and the two index-matchings give $-F^{\alpha\beta} = F^{\beta\alpha}$, the $\tfrac14$ cancelling.
   - *Why needed:* It supplies the divergence $\partial_\alpha F^{\beta\alpha}$.

4. **Assemble and note the automatic homogeneous equation.** Combine into $\partial_\alpha F^{\beta\alpha} = \mu_0 j^\beta$; observe $dF = 0$ from $F = dA$.
   - *Hint:* The Euler–Lagrange combination is $j^\beta - \partial_\alpha F^{\beta\alpha} = 0$.
   - *Why needed:* It produces the inhomogeneous Maxwell equation; the homogeneous one needs no derivation.

---

# Lemma Decomposition

> [!note]- Lemma 1: The general Euler–Lagrange field equation
> **Statement:** Stationarity of $S = \int_{\mathcal U}L(\varphi_A, \partial_\alpha\varphi_A)\,d^4x$ under $\delta\varphi$ vanishing on $\partial\mathcal U$ gives $\frac{\partial L}{\partial\varphi_A} - \partial_\alpha(\frac{\partial L}{\partial(\partial_\alpha\varphi_A)}) = 0$.
>
> **Hint:** Vary, integrate the gradient term by parts, discard the boundary flux.
>
> **Why needed:** It is the machine that turns any Lagrangian into its field equation.
>
> > [!note]- Full proof
> > Under $\varphi_A \to \varphi_A + \delta\varphi_A$, $\delta S = \int_{\mathcal U}[\frac{\partial L}{\partial\varphi_A}\delta\varphi_A + \frac{\partial L}{\partial(\partial_\alpha\varphi_A)}\partial_\alpha\delta\varphi_A]\,d^4x$ (using $\delta\partial_\alpha\varphi_A = \partial_\alpha\delta\varphi_A$). Rewrite the second term: $\frac{\partial L}{\partial(\partial_\alpha\varphi_A)}\partial_\alpha\delta\varphi_A = \partial_\alpha[\frac{\partial L}{\partial(\partial_\alpha\varphi_A)}\delta\varphi_A] - \partial_\alpha[\frac{\partial L}{\partial(\partial_\alpha\varphi_A)}]\delta\varphi_A$. The first piece is a four-divergence $\partial_\alpha V^\alpha$ with $V^\alpha = \frac{\partial L}{\partial(\partial_\alpha\varphi_A)}\delta\varphi_A$; by the four-dimensional [[Thm - Gauss-Ostrogradsky Theorem (3D and 4D)|Gauss theorem]], $\int_{\mathcal U}\partial_\alpha V^\alpha\,d^4x = \oint_{\partial\mathcal U}V^\alpha\,dS_\alpha = 0$ because $\delta\varphi_A = 0$ on $\partial\mathcal U$. Hence $\delta S = \int_{\mathcal U}[\frac{\partial L}{\partial\varphi_A} - \partial_\alpha(\frac{\partial L}{\partial(\partial_\alpha\varphi_A)})]\delta\varphi_A\,d^4x$. For $\delta S = 0$ for all $\delta\varphi_A$ and all $\mathcal U$, the bracket must vanish pointwise. $\blacksquare$

> [!note]- Lemma 2: The interaction-term derivative
> **Statement:** $\partial(A_\mu j^\mu)/\partial A_\beta = j^\beta$.
>
> **Hint:** $j^\mu$ is independent of $A_\mu$ (it is the prescribed external source).
>
> **Why needed:** It places the current on the right-hand side of the field equation.
>
> > [!note]- Full proof
> > The interaction term is $A_\mu j^\mu = A_\mu \eta^{\mu\nu}j_\nu$ (or simply the contraction $A_\mu j^\mu$). Treating $j^\mu$ as a fixed source independent of $A$, $\frac{\partial}{\partial A_\beta}(A_\mu j^\mu) = j^\mu\frac{\partial A_\mu}{\partial A_\beta} = j^\mu\delta_\mu^\beta = j^\beta$. The term contributes nothing to $\partial\mathcal L/\partial(\partial_\alpha A_\beta)$ since it has no derivatives of $A$. $\blacksquare$

> [!note]- Lemma 3: The free-term derivative
> **Statement:** $\frac{\partial}{\partial(\partial_\alpha A_\beta)}(-\tfrac14 F_{\mu\nu}F^{\mu\nu}) = F^{\beta\alpha}$.
>
> **Hint:** Write $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$, treat $\partial_\alpha A_\beta$ as independent, use antisymmetry.
>
> **Why needed:** It produces the divergence $\partial_\alpha F^{\beta\alpha}$ in the field equation.
>
> > [!note]- Full proof
> > Write $-\tfrac14 F_{\mu\nu}F^{\mu\nu}$ with $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$. Differentiate with respect to the independent variable $\partial_\alpha A_\beta$: $\frac{\partial F_{\mu\nu}}{\partial(\partial_\alpha A_\beta)} = \delta_\mu^\alpha\delta_\nu^\beta - \delta_\nu^\alpha\delta_\mu^\beta$. Then $\frac{\partial}{\partial(\partial_\alpha A_\beta)}(-\tfrac14 F_{\mu\nu}F^{\mu\nu}) = -\tfrac14\cdot 2\,F^{\mu\nu}\frac{\partial F_{\mu\nu}}{\partial(\partial_\alpha A_\beta)} = -\tfrac12 F^{\mu\nu}(\delta_\mu^\alpha\delta_\nu^\beta - \delta_\nu^\alpha\delta_\mu^\beta) = -\tfrac12(F^{\alpha\beta} - F^{\beta\alpha}) = -F^{\alpha\beta} = F^{\beta\alpha}$, using the antisymmetry $F^{\alpha\beta} = -F^{\beta\alpha}$. The factor of $2$ (from the two $F$'s) cancels half the $\tfrac14$, and the antisymmetry doubles again, leaving $F^{\beta\alpha}$ with no fractional coefficient. $\blacksquare$

> [!note]- Lemma 4: Assembling the field equation
> **Statement:** The Euler–Lagrange equation for $\mathcal L = -\tfrac14 F^2 + A\cdot J$ is $\partial_\alpha F^{\beta\alpha} = \mu_0 j^\beta$, equivalently $\nabla_\mu F^{\mu\nu} = \mu_0 J^\nu$.
>
> **Hint:** Plug Lemmas 2 and 3 into Lemma 1.
>
> **Why needed:** It is the inhomogeneous Maxwell equation, the theorem's conclusion.
>
> > [!note]- Full proof
> > By Lemma 1, the field equation is $\frac{\partial\mathcal L}{\partial A_\beta} - \partial_\alpha\frac{\partial\mathcal L}{\partial(\partial_\alpha A_\beta)} = 0$. By Lemma 2, $\frac{\partial\mathcal L}{\partial A_\beta} = j^\beta$. By Lemma 3, $\frac{\partial\mathcal L}{\partial(\partial_\alpha A_\beta)} = F^{\beta\alpha}$. So $j^\beta - \partial_\alpha F^{\beta\alpha} = 0$, i.e. $\partial_\alpha F^{\beta\alpha} = j^\beta$ (with $\varepsilon_0 = 1$). Restoring constants with the Lagrangian $\mathcal L = -\tfrac{\varepsilon_0}{4}F^2 + A\cdot J$, the free-term derivative carries a factor $\varepsilon_0$, giving $\varepsilon_0\partial_\alpha F^{\beta\alpha} = j^\beta$, i.e. $\partial_\alpha F^{\beta\alpha} = \mu_0 j^\beta$ since $\varepsilon_0^{-1} = \mu_0$ with $c = 1$. Renaming indices, $\nabla_\mu F^{\mu\nu} = \mu_0 J^\nu$. The homogeneous equation $dF = 0$ holds automatically because $F = dA$ and $d^2 = 0$, requiring no variation. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 — the dynamical setup.** Take the [[Def - The Four-Potential|four-potential]] $A_\mu$ as the dynamical field, with $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$ a *defined* quantity. Because $F = dA$, the homogeneous Maxwell equation $dF = d(dA) = 0$ holds identically — it is a constraint built into the choice of variable, not an equation of motion, and needs no derivation.
>
> **General field equation.** By Lemma 1, stationarity of $S = \int_{\mathcal U}\mathcal L\,d^4x$ under $\delta A$ vanishing on $\partial\mathcal U$ gives the Euler–Lagrange equation $\frac{\partial\mathcal L}{\partial A_\beta} - \partial_\alpha\frac{\partial\mathcal L}{\partial(\partial_\alpha A_\beta)} = 0$ (the boundary term dies by the four-dimensional [[Thm - Gauss-Ostrogradsky Theorem (3D and 4D)|Gauss theorem]] since $\delta A = 0$ on the boundary).
>
> **The two derivatives.** By Lemma 2, the interaction term gives $\frac{\partial\mathcal L}{\partial A_\beta} = j^\beta$. By Lemma 3, the free term gives $\frac{\partial\mathcal L}{\partial(\partial_\alpha A_\beta)} = F^{\beta\alpha}$ (the $\tfrac14$ cancelled by the antisymmetry and the index-matchings).
>
> **Assembly.** By Lemma 4, substituting gives $j^\beta - \partial_\alpha F^{\beta\alpha} = 0$, i.e. $\nabla_\mu F^{\mu\nu} = \mu_0 J^\nu$ — the inhomogeneous [[Thm - Maxwell Equations|Maxwell equation]]. Together with the automatic $dF = 0$, the full Maxwell system is recovered from the single action $S = \int(-\tfrac14 F_{\mu\nu}F^{\mu\nu} + A_\mu J^\mu)\,d^4x$.
>
> **Remark on the interaction term.** For a single particle, $\int A_\mu J^\mu\,d^4x$ with $J = q\int\delta_{X(\tau)}U\,d\tau$ reduces, on integrating over the spatial slice, to $q\int A_\mu\,\dot X^\mu\,d\tau = q\int A\cdot dX$ — exactly the [[Def - Lagrangian for a Particle in a Vector Field|minimal-coupling term]] of topic XV that produces the Lorentz force. The field action and the particle action share the same coupling. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The Proca action and massive vector fields.** Adding a mass term $\tfrac12 m^2 A_\mu A^\mu$ to the Lagrangian gives the **Proca action**, whose field equation $\nabla_\mu F^{\mu\nu} + m^2 A^\nu = \mu_0 J^\nu$ describes a massive spin-$1$ field (the $W$ and $Z$ bosons before symmetry breaking). The mass term breaks gauge invariance, and the field equation no longer implies charge conservation automatically; recognising why is nonobvious because it shows the deep link between masslessness, gauge invariance, and charge conservation.

**The Einstein–Hilbert action.** General relativity is derived from the action $S = \frac{1}{16\pi G}\int R\sqrt{-g}\,d^4x + S_{\mathrm{matter}}$, whose Euler–Lagrange equation (varying the metric) is the Einstein field equation $G^{\mu\nu} = 8\pi G\,T^{\mu\nu}$. This is the gravitational analogue of the present theorem, with the metric as dynamical field and $R$ as the scalar Lagrangian; the application is out-of-distribution because curvature replaces field strength, but the variational logic is identical.

**Effective field theory and higher-derivative terms.** Beyond $-\tfrac14 F^2$, Lorentz invariance permits higher-order terms like $(F_{\mu\nu}F^{\mu\nu})^2$ (Euler–Heisenberg, from QED vacuum polarisation), which produce nonlinear corrections to Maxwell — light-by-light scattering. Recognising these as additional scalars in the action is surprising because classical electromagnetism is exactly linear, yet quantum effects generate nonlinear terms that the same variational framework handles.

---

# Bridges

- **[[Thm - Maxwell Equations]]** — this theorem *derives* the inhomogeneous Maxwell equation $\nabla_\mu F^{\mu\nu} = \mu_0 J^\nu$ from an action, where §22.1 *postulated* it. The two routes are complementary: the action is the more fundamental starting point (it quantises, it organises symmetries), and Maxwell's equations are its classical Euler–Lagrange shadow. The homogeneous equation is automatic in both treatments, from $F = dA$.

- **[[Thm - Noether Theorem (Relativistic Particle)]]** — the Euler–Lagrange field equation is the field-theory generalisation of the particle Euler–Lagrange equation, with the worldline parameter replaced by four spacetime coordinates and the particle coordinates by field components. Noether's theorem applies: the gauge symmetry $A \to A + d\chi$ of the action yields charge conservation, and translation invariance yields the energy–momentum tensor.

- **[[Def - Lagrangian for a Particle in a Vector Field]]** — the interaction term $\int A_\mu J^\mu$ reduces, for a single particle, to the minimal-coupling term $q\int A\cdot dX$ that gave the Lorentz force in topic XV. The field's coupling to its source and the particle's coupling to the field are the *same* term, viewed from the field side versus the particle side; this is the unity of the matter–field system.

- **[[Gauge Theory VII — The Hodge Star, Electrodynamics, and Yang–Mills Theory]]** — the action $-\tfrac14\int F^2$ is the abelian Yang–Mills action. Replacing $F = dA$ by the nonabelian curvature $F = dA + A\wedge A$ and $F^2$ by $\mathrm{tr}(F^2)$ gives the full Yang–Mills action, whose field equation $D_\mu F^{\mu\nu} = J^\nu$ is nonlinear (the field carries its own charge). Electromagnetism's action is the $\mathrm{U}(1)$ term of the Standard Model Lagrangian; the variational derivation here is the template for every gauge theory.

---

# Unlocked by This

> [!tip] The Energy–Momentum Tensor of the Field *(from §23)*
> Varying the electromagnetic action with respect to the metric (or applying Noether to spacetime translations) gives the **energy–momentum tensor** $T^{\mu\nu} = F^{\mu\alpha}F^\nu{}_\alpha - \tfrac14\eta^{\mu\nu}F_{\alpha\beta}F^{\alpha\beta}$, whose components are the field's energy density, momentum density, and stress (the Maxwell stress tensor). Its conservation $\nabla_\mu T^{\mu\nu} = 0$ is the field's energy–momentum conservation, and it is the source of gravity in general relativity — the subject of [[Special Relativity XXIII — The Energy-Momentum Tensor and Field Energy|topic XXIII]].

> [!tip] The Path Integral and Quantum Electrodynamics *(from QFT)*
> The action $S = \int(-\tfrac14 F^2 + A\cdot J)\,d^4x$ is the input to the **path integral** $\int\mathcal D A\,e^{iS/\hbar}$ that defines quantum electrodynamics: each field configuration is weighted by $e^{iS/\hbar}$, and the classical Maxwell equations emerge as the stationary-phase (saddle-point) condition. The gauge redundancy $A \to A + d\chi$ must be fixed (Faddeev–Popov procedure) to make the path integral well-defined, and the resulting QED is the most precisely tested theory in physics. The classical action derived here is the bridge to the quantum theory.

> [!tip] The Yang–Mills Action and the Standard Model *(from Gauge Theory)*
> Generalising $-\tfrac14 F_{\mu\nu}F^{\mu\nu}$ to $-\tfrac14\mathrm{tr}(F_{\mu\nu}F^{\mu\nu})$ with a nonabelian curvature gives the **Yang–Mills action**, the foundation of the Standard Model's $\mathrm{SU}(3)\times\mathrm{SU}(2)\times\mathrm{U}(1)$ gauge theory. The nonabelian field strength $F = dA + A\wedge A$ makes the field equations nonlinear — the gauge field carries its own charge, so gluons interact with gluons — which is the origin of confinement and asymptotic freedom in the strong interaction. Electromagnetism is the abelian seed from which the entire edifice grows.
