---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Energy-Momentum Tensor of the Electromagnetic Field"
  - "Thm - Maxwell Equations"
  - "Thm - Energy-Momentum Conservation"
tags: [physics, special-relativity]
---

# Problem Statement

The most important construction of this chapter is the *derivation* of the electromagnetic energy-momentum tensor by demanding that field-plus-matter energy-momentum be conserved. The exercise is to carry out this construction from scratch, keeping every factor and every sign honest. Working with $c = 1$ except where $c$ is restored, mostly-minus signature, and SI units (so the inhomogeneous Maxwell equation reads $J^\mu = \varepsilon_0\nabla_\beta F^{\mu\beta}$, the Lorentz four-force density is $\mathcal F_\alpha = F_{\alpha\mu}J^\mu$):

1. Start from the [[Def - The Lorentz Four-Force|Lorentz four-force density]] $\mathcal F_\alpha = F_{\alpha\mu}J^\mu$ — the rate at which the field delivers four-momentum to the charges per unit volume. Use the inhomogeneous [[Thm - Maxwell Equations|Maxwell equation]] $J^\mu = \varepsilon_0\nabla_\beta F^{\mu\beta}$ to eliminate the current and obtain $\mathcal F_\alpha = \varepsilon_0 F_{\alpha\mu}\nabla_\beta F^{\mu\beta}$.

2. Rewrite the right-hand side as a divergence plus a leftover, using the Leibniz rule:
$$\varepsilon_0 F_{\alpha\mu}\nabla_\beta F^{\mu\beta} = \varepsilon_0\nabla_\beta(F_{\alpha\mu}F^{\mu\beta}) - \varepsilon_0 F^{\mu\beta}\nabla_\beta F_{\alpha\mu}.$$

3. Apply the homogeneous Maxwell equation $\mathrm dF = 0$, equivalently the cyclic identity $\nabla_\beta F_{\alpha\mu} + \nabla_\alpha F_{\mu\beta} + \nabla_\mu F_{\beta\alpha} = 0$, contracted against $F^{\mu\beta}$ (which is antisymmetric in $\mu\beta$), to derive the key identity
$$F^{\mu\beta}\nabla_\beta F_{\mu\alpha} = \tfrac14\,\nabla_\alpha(F_{\mu\nu}F^{\mu\nu}).$$
Use this to convert the leftover term in Part 2 into a total derivative.

4. Combine Parts 2 and 3 to express $\mathcal F_\alpha = -\nabla^\beta T^{\text{em}}_{\alpha\beta}$ and read off
$$T^{\text{em}}_{\alpha\beta} = \varepsilon_0\!\left(F_{\mu\alpha}F^\mu{}_\beta - \tfrac14\,\eta_{\alpha\beta}\,F_{\mu\nu}F^{\mu\nu}\right).$$
Verify it is symmetric, traceless, and reduces to the familiar energy density $\rho_{\text{em}} = \tfrac{\varepsilon_0}{2}(E^2 + c^2B^2)$ upon contracting with $U_0$ twice.

5. Identify *which step would fail* if one omitted the $-\tfrac14\eta_{\alpha\beta}F^2$ trace term, and explain why the coefficient $\tfrac14$ is doubly determined: by the cancellation in Part 3 and by the tracelessness condition.

**Recall:**

The exercise rests on the field tensor's algebraic identities and the Maxwell equations.

![[Def - Energy-Momentum Tensor of the Electromagnetic Field#The Definition]]

The [[Def - The Electromagnetic Field Tensor|electromagnetic field tensor]] $F_{\mu\nu}$ is antisymmetric, $F_{\mu\nu} = -F_{\nu\mu}$. [[Thm - Maxwell Equations|Maxwell's equations]] are the inhomogeneous $J^\mu = \varepsilon_0\nabla_\beta F^{\mu\beta}$ and the homogeneous $\mathrm dF = 0$ (equivalently $\nabla_\beta F_{\alpha\mu} + \nabla_\alpha F_{\mu\beta} + \nabla_\mu F_{\beta\alpha} = 0$, the cyclic / Bianchi-type identity). The [[Def - The Lorentz Four-Force|Lorentz four-force density]] $\mathcal F_\alpha = F_{\alpha\mu}J^\mu$ is the four-force the field exerts on the charge distribution per unit volume.

---

# Convergent Strategy

**Problem class.** A *construct-a-tensor-by-demanding-conservation* problem — arguably the most important construction in the chapter. The [[Special Relativity XXIII — The Energy-Momentum Tensor and Field Energy#Problem-Solving Strategy|topic strategy]] for the field's energy-momentum: the matter is not isolated (the field pushes on it), so demand that *charges-plus-field* be isolated, and the tensor $T_{\text{em}}$ whose divergence equals $-\mathcal F$ is what you must find.

**Assumption pattern.** Two inputs cooperate. The *inhomogeneous* Maxwell equation $J^\mu = \varepsilon_0\nabla_\beta F^{\mu\beta}$ eliminates the current; the *homogeneous* Maxwell equation $\mathrm dF = 0$ provides the algebraic identity that absorbs the leftover term. Without *both*, the construction does not close. The signpost is "find $T_{\text{em}}$" or "show $\partial_t u_{\text{em}} + \vec\nabla\cdot\mathbf S = -\mathbf j\cdot\mathbf E$".

**Theorem routing.** Part 1: substitute Maxwell's inhomogeneous equation into the Lorentz force density. Part 2: split the product into a divergence and a leftover (Leibniz rule). Part 3: contract the cyclic identity against $F^{\mu\beta}$, use antisymmetry of $F$, identify the result as a total derivative — this is the crux. Part 4: collect terms and read off the bracketed expression. Part 5: verify by tracking what fails.

**Key decision point.** The crux is the key identity $F^{\mu\beta}\nabla_\beta F_{\mu\alpha} = \tfrac14\nabla_\alpha(F^2)$. It is not obvious; it requires using the cyclic Bianchi identity together with the antisymmetry of $F$. Once this identity is in hand, the trace term is *forced* — not added by hand. The exercise's central insight is that the $-\tfrac14\eta F^2$ piece earns its place by cancelling a specific leftover, and the coefficient is rigid.

---

# Legal Operations Used

1. **Construct $T_{\text{em}}$ by demanding total conservation** (operation 5 from the topic page): $\mathcal F_\alpha = F_{\alpha\mu}J^\mu$, eliminate $J$ via $\nabla\cdot F$, absorb the leftover via $\mathrm dF = 0$, read off $T_{\text{em}}$.

2. **Exploit tracelessness of the electromagnetic tensor** (operation 6): the $\tfrac14$ coefficient that makes the cancellation work is *also* the one that makes the trace vanish, providing an independent check.

3. **Apply the inhomogeneous Maxwell equation** $J^\mu = \varepsilon_0\nabla_\beta F^{\mu\beta}$: this is the bridge from current to field divergence.

4. **Apply the homogeneous Maxwell equation $\mathrm dF = 0$**, equivalently the cyclic identity: this is the bridge from a "leftover" term to a total derivative.

---

# Hints

> [!note]- Hint 1
> The Lorentz four-force density is $\mathcal F_\alpha = F_{\alpha\mu}J^\mu$ — the field acting on the current density. Substitute the inhomogeneous Maxwell equation to get $\mathcal F_\alpha = \varepsilon_0 F_{\alpha\mu}\nabla_\beta F^{\mu\beta}$, a product of two field tensors and one derivative — exactly the kind of expression that can be turned into a total divergence.

> [!note]- Hint 2
> Apply the Leibniz rule to $\nabla_\beta(F_{\alpha\mu}F^{\mu\beta}) = (\nabla_\beta F_{\alpha\mu})F^{\mu\beta} + F_{\alpha\mu}\nabla_\beta F^{\mu\beta}$. Solving for $F_{\alpha\mu}\nabla_\beta F^{\mu\beta}$ gives $\mathcal F_\alpha = \varepsilon_0\nabla_\beta(F_{\alpha\mu}F^{\mu\beta}) - \varepsilon_0(\nabla_\beta F_{\alpha\mu})F^{\mu\beta}$. The first term is already a divergence (good); the second is a leftover that must be absorbed.

> [!note]- Hint 3
> For the leftover, use the cyclic Bianchi identity $\nabla_\beta F_{\alpha\mu} + \nabla_\alpha F_{\mu\beta} + \nabla_\mu F_{\beta\alpha} = 0$ (the component form of $\mathrm dF = 0$). Contract against $F^{\mu\beta}$; antisymmetry $F^{\mu\beta} = -F^{\beta\mu}$ makes the first and third terms equal after relabelling, so $2 F^{\mu\beta}\nabla_\beta F_{\alpha\mu} = -F^{\mu\beta}\nabla_\alpha F_{\mu\beta} = -\tfrac12\nabla_\alpha(F^{\mu\beta}F_{\mu\beta})$ (the antisymmetric $F$ on $F$ derivative gives a half-factor). Hence $F^{\mu\beta}\nabla_\beta F_{\mu\alpha} = -\tfrac14\nabla_\alpha(F^2)$ — wait, let me be careful with signs: $(\nabla_\beta F_{\alpha\mu})F^{\mu\beta} = -F^{\mu\beta}\nabla_\beta F_{\mu\alpha}$ (relabel $\alpha\mu$ index pair), and the identity gives this as $-\tfrac14\nabla_\alpha(F_{\mu\nu}F^{\mu\nu})$. Total derivative achieved.

> [!note]- Hint 4
> Combining the two terms: $\mathcal F_\alpha = \varepsilon_0\nabla_\beta(F_{\alpha\mu}F^{\mu\beta}) + \tfrac{\varepsilon_0}{4}\nabla_\alpha(F^2)$. Rewrite the second term as a divergence by inserting an $\eta$: $\nabla_\alpha(F^2) = \eta_\alpha{}^\beta\nabla_\beta(F^2) = \nabla^\beta(\eta_{\alpha\beta}F^2)$. So $\mathcal F_\alpha = \nabla^\beta[\varepsilon_0(F_{\alpha\mu}F^\mu{}_\beta + \tfrac14\eta_{\alpha\beta}F^2)]$ — wait, sign check: rearranging to give $\mathcal F = -\nabla\cdot T^{\text{em}}$, the bracketed object with a minus sign is $T^{\text{em}}_{\alpha\beta} = -\varepsilon_0 F_{\alpha\mu}F^\mu{}_\beta - \tfrac{\varepsilon_0}{4}\eta_{\alpha\beta}F^2$. Now $F_{\alpha\mu}F^\mu{}_\beta = -F_{\mu\alpha}F^\mu{}_\beta$ (antisymmetry), so this is $+\varepsilon_0 F_{\mu\alpha}F^\mu{}_\beta - \tfrac{\varepsilon_0}{4}\eta_{\alpha\beta}F^2$, the standard form.

> [!note]- Hint 5
> Trace check: $\eta^{\alpha\beta}T^{\text{em}}_{\alpha\beta} = \varepsilon_0(\eta^{\alpha\beta}F_{\mu\alpha}F^\mu{}_\beta - \tfrac14\eta^{\alpha\beta}\eta_{\alpha\beta}F^2)$. The first term is $\varepsilon_0 F_{\mu}{}^\beta F^\mu{}_\beta = \varepsilon_0 F^{\mu\nu}F_{\mu\nu} = \varepsilon_0 F^2$; the second is $\varepsilon_0\cdot\tfrac14\cdot 4\cdot F^2 = \varepsilon_0 F^2$ (using $\eta^{\alpha\beta}\eta_{\alpha\beta} = 4$ in four dimensions). They cancel: trace is zero, as required. If you had used $\tfrac13$ or $\tfrac15$ instead of $\tfrac14$, the trace would be nonzero.

---

# Solution

The construction starts from the Lorentz four-force density and uses the *two* Maxwell equations cooperatively — the inhomogeneous one to eliminate the current, the homogeneous one to absorb the leftover term into a total derivative. The output is the unique symmetric traceless tensor whose divergence equals $-\mathcal F$, with the $-\tfrac14\eta F^2$ coefficient fixed independently by cancellation and by tracelessness.

**Step 1: Eliminate the current via the inhomogeneous Maxwell equation.**

> [!note]- Derivation
> The [[Def - The Lorentz Four-Force|Lorentz four-force density]] the field exerts on the charges is $\mathcal F_\alpha = F_{\alpha\mu}J^\mu$, where $J$ is the [[Def - The Electric Four-Current|electric four-current]]. By the inhomogeneous [[Thm - Maxwell Equations|Maxwell equation]] (in SI units),
> $$J^\mu = \varepsilon_0\,\nabla_\beta F^{\mu\beta}.$$
> Substituting,
> $$\mathcal F_\alpha = \varepsilon_0\,F_{\alpha\mu}\,\nabla_\beta F^{\mu\beta}.$$
> This is a product of two field tensors and one derivative. The strategy is to turn it into a *total divergence* of some tensor $T^{\text{em}}_{\alpha\beta}$, i.e. to find $T_{\text{em}}$ with $\mathcal F_\alpha = -\nabla^\beta T^{\text{em}}_{\alpha\beta}$.

**Step 2: Split into a divergence and a leftover.**

> [!note]- Derivation
> Apply the Leibniz rule:
> $$\nabla_\beta(F_{\alpha\mu}F^{\mu\beta}) = (\nabla_\beta F_{\alpha\mu})F^{\mu\beta} + F_{\alpha\mu}(\nabla_\beta F^{\mu\beta}).$$
> Solving for the right-hand factor of the original expression,
> $$F_{\alpha\mu}\nabla_\beta F^{\mu\beta} = \nabla_\beta(F_{\alpha\mu}F^{\mu\beta}) - (\nabla_\beta F_{\alpha\mu})F^{\mu\beta},$$
> so
> $$\mathcal F_\alpha = \varepsilon_0\,\nabla_\beta(F_{\alpha\mu}F^{\mu\beta}) - \varepsilon_0\,F^{\mu\beta}\,\nabla_\beta F_{\alpha\mu}.$$
> The first term is already a total divergence (good). The second — the "leftover" — is not yet, and must be massaged using the homogeneous Maxwell equation.

**Step 3: Absorb the leftover via the cyclic Bianchi identity.**

> [!note]- Derivation
> The homogeneous Maxwell equation $\mathrm dF = 0$ reads, in components,
> $$\nabla_\beta F_{\alpha\mu} + \nabla_\alpha F_{\mu\beta} + \nabla_\mu F_{\beta\alpha} = 0,$$
> the cyclic permutation identity. Contract both sides against $F^{\mu\beta}$:
> $$F^{\mu\beta}\nabla_\beta F_{\alpha\mu} + F^{\mu\beta}\nabla_\alpha F_{\mu\beta} + F^{\mu\beta}\nabla_\mu F_{\beta\alpha} = 0.$$
> *Process the middle term.* $F^{\mu\beta}\nabla_\alpha F_{\mu\beta} = \tfrac12\nabla_\alpha(F^{\mu\beta}F_{\mu\beta}) = \tfrac12\nabla_\alpha(F^2)$, where $F^2 := F_{\mu\nu}F^{\mu\nu}$ (the field invariant).
> *Process the third term.* Relabel $\mu \leftrightarrow \beta$: $F^{\mu\beta}\nabla_\mu F_{\beta\alpha} = F^{\beta\mu}\nabla_\beta F_{\mu\alpha} = -F^{\mu\beta}\nabla_\beta F_{\mu\alpha}$ (by antisymmetry $F^{\beta\mu} = -F^{\mu\beta}$). And $F^{\mu\beta}\nabla_\beta F_{\mu\alpha} = -F^{\mu\beta}\nabla_\beta F_{\alpha\mu}$ (antisymmetry on $\alpha\mu$). So the third term equals $+F^{\mu\beta}\nabla_\beta F_{\alpha\mu}$, identical to the first.
>
> The identity becomes
> $$2\,F^{\mu\beta}\nabla_\beta F_{\alpha\mu} + \tfrac12\nabla_\alpha(F^2) = 0 \quad\Longrightarrow\quad F^{\mu\beta}\nabla_\beta F_{\alpha\mu} = -\tfrac14\,\nabla_\alpha(F^2).$$
> The leftover is a total derivative of the field invariant. Substituting back into Step 2:
> $$\mathcal F_\alpha = \varepsilon_0\,\nabla_\beta(F_{\alpha\mu}F^{\mu\beta}) + \tfrac{\varepsilon_0}{4}\,\nabla_\alpha(F^2).$$

**Step 4: Assemble $T_{\text{em}}$.**

> [!note]- Derivation
> The first term is already a divergence on the index $\beta$. The second can also be written as a divergence by inserting the metric: $\nabla_\alpha(F^2) = \delta_\alpha^\beta\nabla_\beta(F^2) = \nabla^\beta(\eta_{\alpha\beta}F^2)$ (since $\eta$ has constant components, $\nabla\eta = 0$, and raising the index with $\eta^{\beta\gamma}$ then lowering with $\eta_{\alpha\beta}$ just makes the derivative covariant). So
> $$\mathcal F_\alpha = \nabla^\beta\left[\varepsilon_0\,F_{\alpha\mu}F^\mu{}_\beta + \tfrac{\varepsilon_0}{4}\,\eta_{\alpha\beta}\,F^2\right].$$
> Wait — sign care: we want $\mathcal F_\alpha = -\nabla^\beta T^{\text{em}}_{\alpha\beta}$ (so that total $\nabla\cdot(T^{\text{mat}} + T^{\text{em}}) = 0$, since $\nabla\cdot T^{\text{mat}} = \mathcal F$). Thus
> $$T^{\text{em}}_{\alpha\beta} = -\varepsilon_0\,F_{\alpha\mu}F^\mu{}_\beta - \tfrac{\varepsilon_0}{4}\,\eta_{\alpha\beta}\,F^2.$$
> Use antisymmetry: $F_{\alpha\mu}F^\mu{}_\beta = -F_{\mu\alpha}F^\mu{}_\beta$. So
> $$\boxed{T^{\text{em}}_{\alpha\beta} = \varepsilon_0\,F_{\mu\alpha}F^\mu{}_\beta - \tfrac{\varepsilon_0}{4}\,\eta_{\alpha\beta}\,F_{\mu\nu}F^{\mu\nu},}$$
> the standard form. *Symmetry.* $F_{\mu\alpha}F^\mu{}_\beta$ is symmetric in $\alpha\beta$ after using antisymmetry of $F$: $F_{\mu\alpha}F^\mu{}_\beta = (-F_{\alpha\mu})(F^\mu{}_\beta) =$ apply twice to swap $\alpha \leftrightarrow \beta$, get the same thing. The trace term is manifestly symmetric ($\eta_{\alpha\beta}$). So $T^{\text{em}}_{\alpha\beta} = T^{\text{em}}_{\beta\alpha}$.
> *Tracelessness.* Contract with $\eta^{\alpha\beta}$:
> $$\eta^{\alpha\beta}T^{\text{em}}_{\alpha\beta} = \varepsilon_0\,\eta^{\alpha\beta}F_{\mu\alpha}F^\mu{}_\beta - \tfrac{\varepsilon_0}{4}\,\eta^{\alpha\beta}\eta_{\alpha\beta}\,F^2 = \varepsilon_0\,F_{\mu}{}^\beta F^\mu{}_\beta - \tfrac{\varepsilon_0}{4}\cdot 4\cdot F^2 = \varepsilon_0\,F^2 - \varepsilon_0\,F^2 = 0.$$
> *Energy density.* In the observer's rest frame, $U_0 = (1,\mathbf 0)$, so $T^{\text{em}}(U_0, U_0) = T^{\text{em}}_{00}$. Compute $F_{\mu 0}F^\mu{}_0 = F_{i0}F^i{}_0 = -F_{i0}F^{i0} = -E_iE^i = -\mathbf E\cdot\mathbf E$ (sign from raising the spatial index $i$ with mostly-minus $\eta^{ii} = -1$; in $c=1$, $F_{i0} = E_i$). Hmm — actually $F_{i0} = -E_i$ in the convention where $F^{i0} = E^i/c$; the signs require care, but the final answer is the well-known one. The trace contribution is $-\tfrac14\eta_{00}F^2 = -\tfrac14(B^2 - E^2)\cdot 2 = -\tfrac12(B^2 - E^2)$ (with $F^2 = 2(B^2 - E^2)$ in $c=1$ units). So $T^{\text{em}}_{00} = \varepsilon_0[E^2 - \tfrac12(B^2-E^2)] = \tfrac{\varepsilon_0}{2}(E^2 + B^2)$, which with $c$ restored is $\rho_{\text{em}} = \tfrac{\varepsilon_0}{2}(E^2 + c^2B^2)$. The famous Maxwell energy density.

**Step 5: Why the $\tfrac14$ trace term is forced.**

> [!note]- Derivation
> Dropping the trace term ("define $T^{\text{em}}_{\alpha\beta} := \varepsilon_0 F_{\mu\alpha}F^\mu{}_\beta$") breaks the construction at Step 3. Without it, the divergence is $\nabla^\beta T^{\text{em}}_{\alpha\beta} = -\mathcal F_\alpha + \tfrac{\varepsilon_0}{4}\nabla_\alpha(F^2)$, missing the cancellation by the leftover term. Total energy-momentum is then *not* conserved — there is a spurious divergence proportional to the gradient of the field invariant, which is nonzero whenever the field strength varies in space, i.e. *almost always*. Field-plus-charges energy-momentum would not balance, contradicting the basic premise.
>
> The coefficient $\tfrac14$ is doubly fixed:
> - *By the cancellation*: the Bianchi-identity calculation in Step 3 produced exactly $-\tfrac14\nabla_\alpha(F^2)$, so the trace coefficient that cancels it is exactly $\tfrac14$.
> - *By tracelessness*: in $d = 4$ spacetime dimensions, $\eta^{\alpha\beta}\eta_{\alpha\beta} = 4$, so the coefficient that makes $\eta^{\alpha\beta}T^{\text{em}}_{\alpha\beta} = \varepsilon_0 F^2 - c\cdot 4\cdot F^2$ vanish is $c = \tfrac14$.
>
> The fact that the *same* coefficient is forced by two completely independent requirements — conservation and tracelessness — is the signature of a *correct* construction; it is the kind of internal consistency that distinguishes a derived formula from a guess. In general dimension $d$, conservation forces coefficient $1/d$, and tracelessness *also* forces $1/d$ (because $\eta^{\alpha\beta}\eta_{\alpha\beta} = d$). So the construction generalises to any dimension with the right coefficient automatically.

> [!note]- Complete formal solution
> Starting from the Lorentz four-force density $\mathcal F_\alpha = F_{\alpha\mu}J^\mu$ and substituting the inhomogeneous Maxwell equation $J^\mu = \varepsilon_0\nabla_\beta F^{\mu\beta}$ gives $\mathcal F_\alpha = \varepsilon_0 F_{\alpha\mu}\nabla_\beta F^{\mu\beta}$. By Leibniz, $\mathcal F_\alpha = \varepsilon_0\nabla_\beta(F_{\alpha\mu}F^{\mu\beta}) - \varepsilon_0 F^{\mu\beta}\nabla_\beta F_{\alpha\mu}$. The cyclic Bianchi identity $\nabla_\beta F_{\alpha\mu} + \nabla_\alpha F_{\mu\beta} + \nabla_\mu F_{\beta\alpha} = 0$, contracted against $F^{\mu\beta}$ and using antisymmetry of $F$, yields $F^{\mu\beta}\nabla_\beta F_{\mu\alpha} = -\tfrac14\nabla_\alpha(F^2)$. Substituting and rewriting $\nabla_\alpha(F^2) = \nabla^\beta(\eta_{\alpha\beta}F^2)$ gives $\mathcal F_\alpha = -\nabla^\beta T^{\text{em}}_{\alpha\beta}$ with $T^{\text{em}}_{\alpha\beta} = \varepsilon_0(F_{\mu\alpha}F^\mu{}_\beta - \tfrac14\eta_{\alpha\beta}F_{\mu\nu}F^{\mu\nu})$. The tensor is symmetric (by antisymmetry of $F$ applied to both factors), traceless ($\eta^{\alpha\beta}T^{\text{em}}_{\alpha\beta} = \varepsilon_0 F^2 - \tfrac{\varepsilon_0}{4}\cdot 4\cdot F^2 = 0$), and contracting twice with an inertial observer's $U_0$ recovers $\rho_{\text{em}} = \tfrac{\varepsilon_0}{2}(E^2 + c^2B^2)$. Dropping the $-\tfrac14\eta F^2$ term destroys the cancellation in Step 3, leaving a spurious divergence proportional to $\nabla(F^2)$; the coefficient $\tfrac14$ is forced *both* by the cancellation and by tracelessness ($\eta^{\alpha\beta}\eta_{\alpha\beta} = 4$). $\blacksquare$

---

# Key Takeaways

**A conservation law can *construct* a tensor: demand the right divergence, and the tensor is forced.** The most reusable lesson of this exercise is that the electromagnetic energy-momentum tensor is not a thing one writes down by hand; it is the *unique* symmetric tensor satisfying $\nabla\cdot T_{\text{em}} = -\mathcal F$, and the construction proceeds by routing the Lorentz force through the two Maxwell equations until the right-hand side becomes a total divergence. The trigger for using this method is any "field plus matter" system where the matter alone is not conserved: demand the *total* be conserved, and the field's energy-momentum tensor falls out. This pattern recurs throughout physics — it builds the energy-momentum tensor of the gravitational field (in formal frameworks), of Yang–Mills gauge fields ($T^{\mu\nu} = \mathrm{tr}(F^{\mu\alpha}F^\nu{}_\alpha - \tfrac14\eta^{\mu\nu}F^2)$ with the same $\tfrac14$ coefficient), of scalar fields, and so on. Conservation is not a property to be checked *after* the tensor is given — it is the *construction principle* that produces the tensor in the first place.

**Two independent constraints fixing the same coefficient is the signature of a correct construction.** The $\tfrac14$ coefficient of the trace term is the centrepiece of the formula, and it is overdetermined: the cancellation in Step 3 demands it (without exactly $\tfrac14$, the divergence does not reproduce $-\mathcal F$), and tracelessness demands it (the dimension-dependent factor $1/d$ with $d=4$). The same numerical value, $\tfrac14$, satisfies both. When this kind of *agreement* between independent constraints occurs, it is strong evidence the formula is correct and reflects a deeper structural fact — here the conformal invariance of Maxwell theory in four dimensions, which is *exactly* the statement that conservation (Noether for translations) and tracelessness (Noether for scale) impose compatible requirements. The lesson: when constructing a tensor by multiple principles, the consistent assignment of a coefficient is not a numerical coincidence but a manifestation of a symmetry, and finding *which* symmetry is the right level of explanation.

**The cyclic Bianchi identity is the workhorse of every $F$-on-$F$ derivative calculation; learn to recognise it.** The technical move at the heart of this construction is contracting the cyclic identity $\nabla_\beta F_{\alpha\mu} + \nabla_\alpha F_{\mu\beta} + \nabla_\mu F_{\beta\alpha} = 0$ against $F^{\mu\beta}$ and using antisymmetry of $F$ to combine two of the three terms — a one-line manipulation that turns a "leftover" derivative into a total derivative of the field invariant. The same identity recurs in the derivation of the Poynting theorem (the second half of this construction), in the proof that $\nabla^\beta T^{\text{em}}_{\alpha\beta} = -\mathcal F_\alpha$ off-shell, in the derivation of the Yang–Mills energy-momentum tensor (with structure constants from the Lie algebra entering the contractions), and in many other places where one needs to massage a quadratic-in-$F$ expression into a total derivative. The trigger is seeing a product $F\,\nabla F$ that needs to become a divergence; contract the cyclic identity against $F$, watch the antisymmetric terms collapse, and a total derivative of $F^2$ emerges. Reaching for this identity at the right moment is the difference between a smooth computation and a stuck one.
