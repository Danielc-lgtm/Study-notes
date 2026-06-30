---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - The Energy-Momentum Tensor"
  - "Thm - Energy-Momentum Conservation"
  - "Def - Observer and Local Rest Space"
tags: [physics, special-relativity]
---

# Problem Statement

The vanishing-divergence law $\nabla_\mu T^{\mu\nu} = 0$ is *one* tensor equation, but its four components are *four* scalar conservation laws — one for energy and three for momentum. The exercise is to perform the splitting and recognise the result as a pair of familiar continuity equations. Working with $c = 1$ except where $c$ is restored for recognisability, and with mostly-minus signature:

1. For an isolated system with energy-momentum tensor $T$ and an inertial observer of four-velocity $U_0$, decompose $T$ relative to that observer:
$$T = \varepsilon\,U_0^\flat\otimes U_0^\flat + c\,\varpi\otimes U_0^\flat + c\,U_0^\flat\otimes\varpi + S,$$
where $\varepsilon = T(U_0,U_0)$, the momentum density $1$-form $\varpi$ and energy flux $\varphi = c^2\varpi$ live in the rest space, and $S$ is the stress tensor.

2. Substitute into $\nabla_\mu T^{\mu\nu} = 0$, use that $U_0$ is *constant* (inertial observer, $\nabla U_0 = 0$), and split the resulting $1$-form equation by projecting along $U_0$ (giving the energy conservation law $\partial_t\varepsilon + c^2\,\vec\nabla\cdot\varpi = 0$) and orthogonal to $U_0$ (giving the momentum conservation law $\partial_t\varpi + \vec\nabla\cdot S = 0$).

3. For a *non-isolated* system $\nabla_\mu T^{\mu\nu} = \mathcal F^\nu$ with four-force density $\mathcal F$, show that the energy equation acquires a source $c\,\langle\mathcal F, U_0\rangle$ (power supplied per unit volume) and the momentum equation a source $\mathcal F\circ\perp_{U_0}$ (force per unit volume).

4. Apply the splitting to the electromagnetic field, with $\mathcal F^\nu = -F^{\nu}{}_\mu J^\mu$, $\varepsilon = \rho_{\text{em}} = \tfrac{\varepsilon_0}{2}(E^2 + c^2B^2)$, and energy flux $\boldsymbol\varphi = \mathbf E\times\mathbf B/\mu_0$ (the Poynting vector). Read off **Poynting's theorem** $\partial_t\rho_{\text{em}} + \vec\nabla\cdot\mathbf S = -\mathbf j\cdot\mathbf E$ and interpret each term.

**Recall:**

The exercise rests on the energy-momentum tensor's observer decomposition and the conservation theorem.

![[Thm - Energy-Momentum Conservation#Statement]]

The energy-momentum tensor $T$ decomposes relative to an observer $U_0$ into energy density $\varepsilon = T(U_0,U_0)$, momentum density $\varpi$ (a $1$-form in the rest space), energy flux $\varphi = c^2\varpi$, and stress $S$; see [[Def - The Energy-Momentum Tensor]]. The four-force density $\mathcal F = \vec\nabla\cdot T$ measures the rate at which the system gains four-momentum from outside (or, with sign, exerts force on something else).

---

# Convergent Strategy

**Problem class.** A *project-a-tensor-conservation-law* problem. The [[Special Relativity XXIII — The Energy-Momentum Tensor and Field Energy#Problem-Solving Strategy|topic strategy]] for conservation laws: substitute the observer decomposition of $T$ into $\nabla_\mu T^{\mu\nu} = 0$, use that the observer's four-velocity is constant (for an inertial observer), and project the resulting $1$-form equation onto $U_0$ and onto the rest space.

**Assumption pattern.** The signpost is "isolated" (or, more generally, "the four-force density is $\mathcal F$"). Isolated means $\nabla_\mu T^{\mu\nu} = 0$; non-isolated means $\nabla_\mu T^{\mu\nu} = \mathcal F^\nu$. An *inertial* observer means $\nabla_\beta U_0^\alpha = 0$, which lets every derivative falling on $U_0^\flat$ drop, dramatically simplifying the calculation.

**Theorem routing.** Part 1: direct substitution of the matrix decomposition into the tensor form. Part 2: take the divergence by the Leibniz rule, use $\nabla U_0 = 0$, and contract the result with $U_0$ or compose with $\perp_{U_0}$. Part 3: identical computation with $\mathcal F$ on the right-hand side. Part 4: substitute the electromagnetic energy density and Poynting vector, recognise $-c\langle F(\,\cdot\,, J), U_0\rangle/c = -\mathbf j\cdot\mathbf E$ as the power dissipated by the field on the charges.

**Key decision point.** The crux is *which projection gives which equation*. Contracting the $1$-form equation $\nabla_\mu T^{\mu\nu} = 0$ with $U_{0\,\nu}$ picks out the time component ($\nu = 0$ in the rest frame) — the *energy* equation. Composing with the spatial projector $\perp_{U_0}$ picks out the spatial components ($\nu = i$) — the *momentum* equation. Two physically distinct laws live in the same tensor equation, and only the projection separates them.

---

# Legal Operations Used

1. **Read off measured quantities by contracting $T$ with the observer's frame** (operation 1 from the topic page): the decomposition $T = \varepsilon\,U_0^\flat\otimes U_0^\flat + c(\varpi\otimes U_0^\flat + U_0^\flat\otimes\varpi) + S$ is precisely this contraction-recipe written in reverse.

2. **Take the divergence and set it to zero (or to $\mathcal F$)** (operation 3): $\nabla_\mu T^{\mu\nu} = 0$ for isolated, $= \mathcal F^\nu$ otherwise.

3. **Project the conservation law along and orthogonal to $U_0$** (operation 4): contraction with $U_0$ gives the energy (Poynting) equation; composition with $\perp_{U_0}$ gives the momentum balance.

4. **Construct $T_{\text{em}}$ by demanding total conservation** (operation 5): used implicitly in Part 4, since $\nabla^\beta T^{\text{em}}_{\alpha\beta} = -F_{\alpha\mu}J^\mu = -\mathcal F_\alpha^{\text{Lorentz}}$.

---

# Hints

> [!note]- Hint 1
> Substitute $T = \varepsilon\,U_0^\flat\otimes U_0^\flat + c(\varpi\otimes U_0^\flat + U_0^\flat\otimes\varpi) + S$ into $\nabla_\mu T^{\mu\nu} = 0$. Use the Leibniz rule, and recall that for an *inertial* observer $\nabla_\alpha U_0^\beta = 0$, so every derivative of $U_0^\flat$ vanishes. The surviving terms are derivatives of the *scalars* and *spatial tensors* $\varepsilon, \varpi, S$.

> [!note]- Hint 2
> The result is a $1$-form equation in the index $\nu$: $(\nabla_{U_0}\varepsilon)\,U_0^\flat + c\,\nabla_{U_0}\varpi + c(\vec\nabla\cdot\varpi)\,U_0^\flat + \vec\nabla\cdot S = 0$. To get the energy equation, *apply this $1$-form to $U_0$ itself* — i.e. contract with $U_0^\nu$. Use $\langle U_0^\flat, U_0\rangle = 1$, $\langle\varpi, U_0\rangle = 0$ (the momentum density lives in the rest space, orthogonal to $U_0$), and $\nabla_{U_0}\varepsilon = c^{-1}\partial_t\varepsilon$ in the observer's frame.

> [!note]- Hint 3
> For the momentum equation, *compose the $1$-form with the spatial projector* $\perp_{U_0}$. The energy-density term $(\nabla_{U_0}\varepsilon)\,U_0^\flat$ vanishes (its dual is $U_0$, killed by $\perp_{U_0}$), the energy-flux divergence term $(\vec\nabla\cdot\varpi)\,U_0^\flat$ vanishes for the same reason, and what remains is $c^{-1}\partial_t\varpi + \vec\nabla\cdot S = 0$ after the rescaling $\nabla_{U_0} = c^{-1}\partial_t$ — i.e. $\partial_t\varpi + c\,\vec\nabla\cdot S = 0$, which in $c=1$ units is $\partial_t\varpi + \vec\nabla\cdot S = 0$.

> [!note]- Hint 4
> For Poynting's theorem, the source is $\mathcal F^\nu = -F^\nu{}_\mu J^\mu$ from the Lorentz four-force; project along $U_0$ to get $c\,\langle\mathcal F, U_0\rangle = c\,(-F^\nu{}_\mu J^\mu)\,U_{0\,\nu}$. Now $F_{\nu\mu}U_0^\nu = -E_\mu$ (the electric field is the $U_0$-contraction of $F$), and contracting $E_\mu J^\mu = -c\,\mathbf E\cdot\mathbf j$ (since $J = (\rho c, \mathbf j)$ and the spatial inner product carries a minus from mostly-minus). The result is $-\mathbf j\cdot\mathbf E$ — the work done by the field on the charges per unit volume.

---

# Solution

The single tensor equation $\nabla_\mu T^{\mu\nu} = 0$ splits, upon projecting onto and orthogonal to an inertial observer's four-velocity, into two scalar continuity equations: energy continuity $\partial_t\varepsilon + c^2\vec\nabla\cdot\varpi = 0$ and momentum continuity $\partial_t\varpi + \vec\nabla\cdot S = 0$. Adding a four-force source $\mathcal F$ gives the same split with power and force terms on the right; applied to the electromagnetic field this is **Poynting's theorem**.

**Step 1: The observer decomposition of $T$ is built from $\varepsilon, \varpi, S$.**

> [!note]- Derivation
> An observer with four-velocity $U_0$ defines a $1+3$ split of spacetime into time (along $U_0$) and space (the orthogonal rest space $\mathcal E_{U_0} = U_0^\perp$). Any symmetric $(0,2)$-tensor $T$ decomposes orthogonally with respect to this split as
> $$T = \varepsilon\,U_0^\flat\otimes U_0^\flat + c\,\varpi\otimes U_0^\flat + c\,U_0^\flat\otimes\varpi + S,$$
> where $\varepsilon = T(U_0,U_0)$ is the time–time component (energy density), $\varpi = -\tfrac1c T(\perp_{U_0}, U_0)$ is the time–space component (momentum density, a $1$-form lying in the rest space, $\langle\varpi, U_0\rangle = 0$), $\varphi = c^2\varpi$ is the energy flux ($\varphi = \varphi_i e^i$), and $S = T(\perp_{U_0},\perp_{U_0})$ is the space–space block (stress tensor). The symmetry $T(X,Y) = T(Y,X)$ guarantees $\varphi = c^2\varpi$ — the off-diagonal blocks are the *same* spatial $1$-form up to a kinematic factor of $c^2$, i.e. the energy current and momentum density are one object. See [[Def - The Energy-Momentum Tensor]].

**Step 2: Energy conservation from projection along $U_0$.**

> [!note]- Derivation
> Take the divergence of the decomposition. Because $U_0$ is the four-velocity of an *inertial* observer, $\nabla_\beta U_0^\alpha = 0$ — its components are constant in inertial coordinates aligned with $\mathcal O$. So $\nabla U_0^\flat = 0$ too, and every derivative falling on $U_0^\flat$ vanishes. By the Leibniz rule,
> $$\nabla_\mu T^{\mu\nu} = (\nabla_{U_0}\varepsilon)\,U_0^{\nu} + c\,(\nabla_{U_0}\varpi)^\nu + c\,(\vec\nabla\cdot\varpi)\,U_0^\nu + (\vec\nabla\cdot S)^\nu = 0,$$
> where $\nabla_{U_0} = U_0^\mu\nabla_\mu$ is the directional derivative along the observer's worldline (in the observer's frame, $\nabla_{U_0}f = c^{-1}\partial_t f$ since $U_0^\mu = (1,\mathbf 0)/c \cdot c = (1,\mathbf 0)$ in those coordinates — i.e. $U_0$ has component $1$ in time and the proper-time derivative equals $\partial_t$ on rest-frame functions, scaling by $c$ when $c$ is restored).
>
> Now apply this $1$-form equation to the vector $U_0$, i.e. lower the free index $\nu$ and contract with $U_0^\nu$. Using $\langle U_0^\flat, U_0\rangle = U_0\cdot U_0 = 1$ and $\langle\varpi, U_0\rangle = 0$ (momentum density orthogonal to $U_0$):
> $$\nabla_{U_0}\varepsilon + c\cdot 0 + c\,(\vec\nabla\cdot\varpi)\cdot 1 + \langle\vec\nabla\cdot S, U_0\rangle = 0.$$
> The last term $\langle\vec\nabla\cdot S, U_0\rangle$ also vanishes: $S$ is a spatial tensor ($S(\perp_{U_0}, \perp_{U_0})$), so $\vec\nabla\cdot S$ takes values in the rest space, orthogonal to $U_0$. Translating $\nabla_{U_0}\varepsilon = c^{-1}\partial_t\varepsilon$,
> $$\frac{1}{c}\partial_t\varepsilon + c\,\vec\nabla\cdot\varpi = 0 \quad\Longleftrightarrow\quad \boxed{\partial_t\varepsilon + c^2\,\vec\nabla\cdot\varpi = 0.}$$
> This is the **energy continuity equation**: the energy density changes at the rate the energy flux $c^2\varpi = \varphi$ flows out. In $c=1$ units it reads $\partial_t\varepsilon + \vec\nabla\cdot\varphi = 0$, where $\varphi = \varpi$.

**Step 3: Momentum conservation from orthogonal projection.**

> [!note]- Derivation
> Compose the same $1$-form equation with the spatial projector $\perp_{U_0}$. The term $(\nabla_{U_0}\varepsilon)\,U_0^\flat$ vanishes (its associated vector is along $U_0$, killed by $\perp_{U_0}$); the term $c(\vec\nabla\cdot\varpi)\,U_0^\flat$ vanishes for the same reason. The surviving terms are
> $$c\,\nabla_{U_0}\varpi + \perp_{U_0}(\vec\nabla\cdot S) = 0.$$
> Since $\varpi$ and $S$ already lie in the rest space, $\perp_{U_0}$ acts as identity on $\vec\nabla\cdot S$ (the divergence taken with respect to spatial coordinates). Translating $\nabla_{U_0}\varpi = c^{-1}\partial_t\varpi$,
> $$\partial_t\varpi + c\,\vec\nabla\cdot S = 0.$$
> In $c=1$ units (where the factor of $c$ inside the decomposition is also $1$) this is
> $$\boxed{\partial_t\varpi + \vec\nabla\cdot S = 0,}$$
> the **momentum continuity equation**: momentum density changes at the rate stress carries momentum across surfaces. This is Newton's second law per unit volume, with stress playing the role of force.

**Step 4: Non-isolated case and Poynting's theorem.**

> [!note]- Derivation
> For a non-isolated system $\nabla_\mu T^{\mu\nu} = \mathcal F^\nu$, the same projections give
> $$\partial_t\varepsilon + c^2\,\vec\nabla\cdot\varpi = c\,\langle\mathcal F, U_0\rangle, \qquad \partial_t\varpi + \vec\nabla\cdot S = \mathcal F\circ\perp_{U_0}.$$
> The right-hand sides are the power supplied per unit volume and the force per unit volume the system receives from outside. (For two interacting subsystems, $\nabla\cdot(T_1+T_2) = 0$ implies $\mathcal F_1 = -\mathcal F_2$ — Newton's third law in field form.)
>
> Apply this to the electromagnetic field with $\nabla^\beta T^{\text{em}}_{\alpha\beta} = -F_{\alpha\mu}J^\mu$ (the field is non-isolated because it does work on the charges). For an inertial observer the contraction
> $$c\,\langle\mathcal F^{\text{em}}, U_0\rangle = c\,(-F_{\alpha\mu}J^\mu)\,U_0^\alpha = -c\,(F_{\alpha\mu}U_0^\alpha)\,J^\mu$$
> uses the identity $F_{\alpha\mu}U_0^\alpha = -E_\mu$ (the electric field is the contraction of $F$ with $U_0$; sign from mostly-minus). With $J^\mu = (\rho c, \mathbf j)$ and the spatial inner product carrying a minus in mostly-minus, $-c E_\mu J^\mu/c = -\mathbf E\cdot\mathbf j$ (the time component $E_0 = 0$ since $\mathbf E\in U_0^\perp$).
>
> With $\varepsilon = \rho_{\text{em}} = \tfrac{\varepsilon_0}{2}(E^2 + c^2B^2)$ and $\varphi = c^2\varpi = \mathbf E\times\mathbf B/\mu_0$ the Poynting vector $\mathbf S$,
> $$\boxed{\partial_t\rho_{\text{em}} + \vec\nabla\cdot\mathbf S = -\mathbf j\cdot\mathbf E.}$$
> This is **Poynting's theorem**: field energy density changes as energy flows out (Poynting vector divergence) and as the field does work $\mathbf j\cdot\mathbf E$ on the charges (the minus sign because $-\mathbf j\cdot\mathbf E$ is the power *gained* by the field from the charges — when $\mathbf j\cdot\mathbf E > 0$, the field is losing energy to charge kinetic energy). The momentum component gives the Maxwell-stress force balance $\partial_t\boldsymbol\varpi_{\text{em}} + \vec\nabla\cdot\mathbf S_{\text{em}} = -(\rho\mathbf E + \mathbf j\times\mathbf B)$, the Lorentz force per unit volume back-reacting on the field's momentum.

> [!note]- Complete formal solution
> The observer decomposition of $T$ is $T = \varepsilon U_0^\flat\otimes U_0^\flat + c(\varpi\otimes U_0^\flat + U_0^\flat\otimes\varpi) + S$. For an inertial observer $\nabla U_0 = 0$, so $\nabla_\mu T^{\mu\nu} = (\nabla_{U_0}\varepsilon)U_0^\nu + c\nabla_{U_0}\varpi^\nu + c(\vec\nabla\cdot\varpi)U_0^\nu + (\vec\nabla\cdot S)^\nu$. Setting this to $\mathcal F^\nu$ and contracting with $U_{0\nu}$ (using $\langle U_0^\flat, U_0\rangle = 1$, $\langle\varpi, U_0\rangle = 0$, $\langle\vec\nabla\cdot S, U_0\rangle = 0$) gives the energy equation $\partial_t\varepsilon + c^2\vec\nabla\cdot\varpi = c\langle\mathcal F, U_0\rangle$; composing with $\perp_{U_0}$ gives the momentum equation $\partial_t\varpi + \vec\nabla\cdot S = \mathcal F\circ\perp_{U_0}$. For $\mathcal F = 0$ (isolated) both right-hand sides vanish. Applied to the electromagnetic field with $\nabla^\beta T^{\text{em}}_{\alpha\beta} = -F_{\alpha\mu}J^\mu$, energy density $\rho_{\text{em}} = \tfrac{\varepsilon_0}{2}(E^2 + c^2B^2)$, and Poynting vector $\mathbf S = \mathbf E\times\mathbf B/\mu_0$, the energy projection yields **Poynting's theorem** $\partial_t\rho_{\text{em}} + \vec\nabla\cdot\mathbf S = -\mathbf j\cdot\mathbf E$: field energy changes as the Poynting flux carries it away and as the field does work on charges. $\blacksquare$

---

# Key Takeaways

**One tensor conservation law is four scalar conservation laws, and projecting along/orthogonal to the observer is how you separate them.** The single equation $\nabla_\mu T^{\mu\nu} = 0$ encodes energy conservation in its $\nu = 0$ component and momentum conservation in its $\nu = i$ components, and the algebraic operation that separates the two is *contraction with $U_0$* (energy) versus *composition with $\perp_{U_0}$* (momentum). This is not a one-time trick: the same projection technique extracts the relativistic Euler equation from $\nabla\cdot T_{\text{fluid}} = 0$, the Lorentz-invariance content of geodesic motion, and the entropy/momentum split for any continuous medium. The trigger is any tensor conservation law in which scalar/vector content needs to be made manifest — contract with $U_0$ for the scalar (energy/entropy) law, compose with $\perp_{U_0}$ for the vector (momentum/force) law. The reusable insight is that "tensor conservation" is shorthand for "several scalar conservations packed together by the four-velocity", and that the observer-dependent split is *how the laboratory sees the physics*.

**Poynting's theorem is the time-projection of energy-momentum conservation applied to the electromagnetic field, and the Maxwell-stress momentum balance is its space-projection.** The nineteenth-century theorems of electromagnetism — Poynting's energy theorem, the Maxwell-stress momentum-balance law — were originally derived by hand, term by term, from the Maxwell equations. They are not separate facts: they are the time and space components of the single covariant law $\nabla^\beta T^{\text{em}}_{\alpha\beta} = -F_{\alpha\mu}J^\mu$, and the projection technique recovers them mechanically. The trigger for using this view is any electromagnetism problem about energy flow or stress: instead of deriving Poynting by hand from $\nabla\times\mathbf B$ and $\nabla\times\mathbf E$, write down $T^{\text{em}}$ and project its conservation. The advantage is that the same technique simultaneously delivers the momentum equation, with no extra work, and explains *why* the energy and momentum equations have the structure they do (they are sharing the same tensor).

**An inertial observer is what makes the projection clean — and the disappearance of $\nabla U_0$ is what lets the decomposition's energy/momentum/stress fields decouple algebraically.** A subtle but reusable point is that the splitting relies on $\nabla_\beta U_0^\alpha = 0$, i.e. on the observer being inertial. For a *non-inertial* observer (accelerated or rotating), $\nabla U_0 \ne 0$ and extra terms appear in the projected equations — these are the *inertial forces* (centrifugal, Coriolis, Euler force) that arise in non-inertial frames. The projection technique still works, but the "stress" measured by a non-inertial observer carries fictitious contributions and the "energy density" carries kinetic energy of the frame's motion. The lesson is to *always identify whether the observer is inertial* before projecting: in inertial frames the split is clean and the four scalar laws are the genuine conservation laws of physics; in non-inertial frames the same split delivers the *apparent* conservation laws including frame-dependent inertial terms, and one must add them by hand when comparing to lab measurements.
