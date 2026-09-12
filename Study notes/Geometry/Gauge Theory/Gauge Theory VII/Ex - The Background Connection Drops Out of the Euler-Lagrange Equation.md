---
type: exercise
subject: gauge-theory
difficulty: "⭐"
prereqs:
  - "Def - Electromagnetic Lagrangian and Action"
  - "Thm - Euler-Lagrange Equation of the Electromagnetic Action"
  - "Thm - The Space of Connections is an Affine Space"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $M$ be an oriented Lorentzian $4$-manifold of signature $(-,+,+,+)$, $P \to M$ a principal $U(1)$-bundle, and $J \in \Omega^3(M; \mathbb{R})$ a fixed charge-current $3$-form. The electromagnetic Lagrangian assigns to a connection $\omega \in \mathcal{C}(P)$ the real $4$-form
$$L(\omega) := \tfrac{1}{2}\, F \wedge \star F \;+\; A \wedge J,$$
where $F \in \Omega^2(M;\mathbb{R})$ is the (background-independent) field strength of $\omega$ defined by $\bar\Omega = iF$, and $A = A(\omega, \omega_0) \in \Omega^1(M;\mathbb{R})$ is the **potential of $\omega$ relative to a chosen background connection $\omega_0 \in \mathcal{C}(P)$**, defined by
$$i\, A(\omega,\omega_0) := s^*(\omega - \omega_0)$$
for any local section $s$ of $P$ — a definition that does not depend on $s$ because, for the abelian group $U(1)$, the difference of two connections is a global $i\mathbb{R}$-valued $1$-form on $M$. The first summand $L_1(\omega) := \tfrac12 F \wedge \star F$ depends only on $\omega$ (through $F$); the second summand $L_2(\omega) := A(\omega,\omega_0) \wedge J$ visibly depends on the arbitrary choice of $\omega_0$.

This is uncomfortable: the Lagrangian, which is supposed to encode the physics, contains an arbitrary reference connection $\omega_0$ that no experiment can fix. **Prove that this arbitrariness is harmless at the level of the equations of motion.** Precisely, let $\tilde\omega_0 \in \mathcal{C}(P)$ be a *second* background connection, and write $\tilde L(\omega) := \tfrac12 F \wedge \star F + A(\omega,\tilde\omega_0) \wedge J$ for the Lagrangian built from it. Show:

1. **The difference is a fixed $4$-form.** For every $\omega \in \mathcal{C}(P)$,
   $$L(\omega) - \tilde L(\omega) = A(\tilde\omega_0, \omega_0) \wedge J,$$
   and the $1$-form $A(\tilde\omega_0,\omega_0)$ depends only on the two background connections, not on $\omega$.

2. **The difference term has vanishing variation.** For every open $U \Subset M$ and every variation $\omega_{t,\eta}$ with $A(\omega_{t,\eta},\omega_0) = A(\omega,\omega_0) + t\eta$ (where $\eta \in \Omega^1(M;\mathbb{R})$, $\operatorname{supp}\eta \subset U$),
   $$\frac{d}{dt}\Big|_{0} \int_{\bar U} \big(L(\omega_{t,\eta}) - \tilde L(\omega_{t,\eta})\big) = 0.$$

3. **Criticality is background-independent.** Conclude that $\omega$ is critical for $L$ if and only if it is critical for $\tilde L$; in particular both Lagrangians yield the same Euler–Lagrange equation $d\star F + J = 0$, which contains no reference to any background connection.

> [!warning] Convention:
> We use Bär's electrodynamics conventions: signature $(-,+,+,+)$, $c = 1$, $\mathrm{vol} = dt\wedge dx\wedge dy\wedge dz$, and Bär's Hodge star, so that $L_1 = \tfrac12 F\wedge\star F = -\tfrac12\langle F,F\rangle\,\mathrm{vol}$ on a Lorentzian manifold (index $p=1$, by property $\omega\wedge\star\eta = (-1)^p\langle\omega,\eta\rangle\,\mathrm{vol}$). Bär's source (p. 85) prints the target of $L$ as $\Omega^4(M;i\mathbb{R})$; $L$ is real-valued and we write $\Omega^4(M;\mathbb{R})$. Bär treats this background-independence in one line (p. 86); the exercise supplies the argument in full.

**Recall:**

The objects in play are the electromagnetic Lagrangian, the affine structure on the space of connections that makes the variation $\omega_{t,\eta}$ meaningful, and the Euler–Lagrange equation the variation produces.

![[Def - Electromagnetic Lagrangian and Action#The Definition]]

![[Thm - The Space of Connections is an Affine Space#Statement]]

The affine-space theorem, [[Thm - The Space of Connections is an Affine Space|The Space of Connections is an Affine Space]], is what gives meaning to "$A(\omega_{t,\eta},\omega_0) = A(\omega,\omega_0) + t\eta$": the set $\mathcal{C}(P)$ of connections is an affine space modelled on $\Omega^1(M; \operatorname{ad} P)$, which for $U(1)$ is $\Omega^1(M; i\mathbb{R}) \cong \Omega^1(M;\mathbb{R})$ (via division by $i$). Concretely, for any $\omega \in \mathcal{C}(P)$ and any $\beta \in \Omega^1(M;i\mathbb{R})$ there is a unique connection $\omega + \pi^*\beta$; differences of connections are such global $i\mathbb{R}$-valued $1$-forms, and adding $t\cdot i\eta$ to $\omega$ realises the variation $\omega_{t,\eta}$.

![[Thm - Euler-Lagrange Equation of the Electromagnetic Action#Statement]]

The Euler–Lagrange theorem, [[Thm - Euler-Lagrange Equation of the Electromagnetic Action|Euler-Lagrange Equation of the Electromagnetic Action]], is the payoff: $\omega$ is critical for $L$ if and only if $d\star F + J = 0$. We do not reprove it; we show that the two Lagrangians $L$ and $\tilde L$ share it because they share all their variations.

---

# Convergent Strategy

**Problem class.** This is a *gauge-of-the-functional* problem — not a gauge transformation of the field, but a change in an auxiliary reference built into the action. It belongs to the general class "an action functional contains an arbitrary choice; show the equations of motion do not see it". The universal mechanism is that the choice enters the action only through a term that, when the choice is changed, shifts the action by a *field-independent constant* (or by a term whose variation vanishes identically). Since critical points depend only on the *derivative* of the action along variations, a field-independent additive shift is invisible to them. This is the same principle by which a total-derivative (boundary) term or an additive constant may be dropped from a Lagrangian without changing its Euler–Lagrange equations.

**Assumption pattern.** The structure we exploit is the *affine* structure of $\mathcal{C}(P)$ together with the *additivity of relative potentials*. The recognisable trigger is that the reference $\omega_0$ enters $L$ only through $A(\omega,\omega_0)$, and that relative potentials satisfy a cocycle identity $A(\omega,\omega_0) = A(\omega,\tilde\omega_0) + A(\tilde\omega_0,\omega_0)$ — the analogue of "differences add", $\;(\omega - \omega_0) = (\omega - \tilde\omega_0) + (\tilde\omega_0 - \omega_0)$. Whenever a quantity depends on a reference point only through a difference from that reference, changing the reference shifts the quantity by a term independent of the variable, and this is exactly what makes the dependence disappear from a derivative.

**Theorem routing.** The route is: (1) unfold the definition $iA(\cdot,\cdot) = s^*(\cdot - \cdot)$ and prove the additivity $A(\omega,\omega_0) = A(\omega,\tilde\omega_0) + A(\tilde\omega_0,\omega_0)$ from the linearity of pullback; (2) subtract the two Lagrangians, noting $L_1$ is common (it uses only $F$, which is background-free), so only $L_2$ differs, and the difference is $A(\tilde\omega_0,\omega_0)\wedge J$; (3) observe $A(\tilde\omega_0,\omega_0)$ does not depend on $\omega$, so along any variation $\omega_{t,\eta}$ the difference $4$-form is constant in $t$ and its $t$-derivative is zero; (4) conclude the two functionals $\int_{\bar U}L$ and $\int_{\bar U}\tilde L$ have identical first variations, hence identical critical points, and route to [[Thm - Euler-Lagrange Equation of the Electromagnetic Action|the Euler–Lagrange equation]] $d\star F + J = 0$, which is manifestly background-free.

**Key decision point.** The one insight that makes the problem trivial once seen is: *the field strength $F$, and therefore the entire $L_1$ term, does not know about $\omega_0$ at all.* Bär's definition attaches $F$ to $\omega$ via the descended curvature $\bar\Omega = iF$; the background $\omega_0$ enters only as the base point from which the potential $A$ is measured. So the change $\omega_0 \mapsto \tilde\omega_0$ can only touch $L_2 = A\wedge J$, and there it acts by the additive shift of $A$. The temptation to be resisted is treating $A$ as "the potential of the field" (an object one might expect to carry physical content) rather than as "the coordinate of $\omega$ in the affine chart centred at $\omega_0$"; the second reading makes the reference-dependence, and its irrelevance, obvious.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Gauge Theory VII — The Hodge Star, Electrodynamics, and Yang–Mills Theory#Legal Operations|the topic page's Legal Operations]] (named descriptively where the topic page is not yet assembled):

1. **Unfold the relative potential to a pullback of a difference.** Replace $A(\omega,\omega_0)$ by $\tfrac{1}{i}s^*(\omega-\omega_0)$, so that identities among potentials become identities among pulled-back differences of connections, where the linearity of $s^*$ is available.

2. **Add differences by the cocycle identity.** From $(\omega-\omega_0) = (\omega-\tilde\omega_0) + (\tilde\omega_0-\omega_0)$ and linearity of $s^*$, derive $A(\omega,\omega_0) = A(\omega,\tilde\omega_0) + A(\tilde\omega_0,\omega_0)$.

3. **Isolate the reference-dependent summand.** Recognise that $L_1 = \tfrac12 F\wedge\star F$ uses only the background-free field strength $F$, so $L$ and $\tilde L$ agree on $L_1$ and differ only in $L_2 = A\wedge J$.

4. **Subtract to a fixed form.** Compute $L(\omega)-\tilde L(\omega) = \big(A(\omega,\omega_0)-A(\omega,\tilde\omega_0)\big)\wedge J = A(\tilde\omega_0,\omega_0)\wedge J$, a $4$-form independent of $\omega$.

5. **Differentiate a constant-in-$t$ integrand to zero.** Along any variation $\omega_{t,\eta}$, the difference form $A(\tilde\omega_0,\omega_0)\wedge J$ does not vary with $t$, so $\tfrac{d}{dt}\big|_0\int_{\bar U}(\cdots) = 0$.

6. **Equate critical sets of functionals differing by a variation-free term.** Since the first variations of $\int_{\bar U}L$ and $\int_{\bar U}\tilde L$ coincide for every admissible $\eta$, their critical points coincide, and both reduce to [[Thm - Euler-Lagrange Equation of the Electromagnetic Action|the same Euler–Lagrange equation]].

---

# Hints

> [!note]- Hint 1
> Where, exactly, does the background connection $\omega_0$ enter $L(\omega) = \tfrac12 F\wedge\star F + A(\omega,\omega_0)\wedge J$? The field strength $F$ is defined from the descended curvature $\bar\Omega = iF$ of $\omega$ alone — it does not mention $\omega_0$. So the *only* $\omega_0$-dependent piece is $A(\omega,\omega_0)\wedge J$. Focus there.

> [!note]- Hint 2
> Write $iA(\omega,\omega_0) = s^*(\omega-\omega_0)$. Insert $\pm\tilde\omega_0$: $\;\omega-\omega_0 = (\omega-\tilde\omega_0) + (\tilde\omega_0-\omega_0)$. Now pull back by $s$ and use that $s^*$ is linear. What identity relating $A(\omega,\omega_0)$, $A(\omega,\tilde\omega_0)$, $A(\tilde\omega_0,\omega_0)$ do you get?

> [!note]- Hint 3
> Subtract the two Lagrangians. The $L_1$ terms are identical (both use $F$). For the $L_2$ terms, use the identity from Hint 2: $A(\omega,\omega_0) - A(\omega,\tilde\omega_0) = A(\tilde\omega_0,\omega_0)$. So $L - \tilde L = A(\tilde\omega_0,\omega_0)\wedge J$. Does the $1$-form $A(\tilde\omega_0,\omega_0)$ contain $\omega$ anywhere?

> [!note]- Hint 4
> The difference form $A(\tilde\omega_0,\omega_0)\wedge J$ is built from the two backgrounds and the fixed current $J$ — it has no $\omega$ in it. Under the variation $\omega \mapsto \omega_{t,\eta}$ only $\omega$ moves, so this form is *constant in $t$*. Therefore $\tfrac{d}{dt}\big|_0\int_{\bar U}(L(\omega_{t,\eta}) - \tilde L(\omega_{t,\eta})) = \tfrac{d}{dt}\big|_0(\text{constant}) = 0$. Two functionals whose first variations agree for every $\eta$ have the same critical points.

---

# Solution

The heart of the matter is that changing the background connection changes the Lagrangian only in its coupling term $A\wedge J$, and there only by the fixed $1$-form $A(\tilde\omega_0,\omega_0)$ wedged with $J$ — a term with no dependence on the connection being varied. Because criticality is a statement about the *derivative* of the action along variations, and the derivative of an $\omega$-independent term is zero, the two Lagrangians have exactly the same critical connections. We first establish the additivity of relative potentials, then subtract, then differentiate.

**Step 1: Relative potentials add — the cocycle identity.**

For any three connections $\omega, \omega_0, \tilde\omega_0 \in \mathcal{C}(P)$,
$$A(\omega,\omega_0) = A(\omega,\tilde\omega_0) + A(\tilde\omega_0,\omega_0).$$

> [!note]- Derivation
> Fix a local section $s$ of $P$ over an open set. By definition,
> $$iA(\omega,\omega_0) = s^*(\omega-\omega_0), \qquad iA(\omega,\tilde\omega_0) = s^*(\omega-\tilde\omega_0), \qquad iA(\tilde\omega_0,\omega_0) = s^*(\tilde\omega_0-\omega_0).$$
> As elements of $\Omega^1(P;i\mathbb{R})$, the connection $1$-forms satisfy the algebraic identity
> $$\omega - \omega_0 = (\omega - \tilde\omega_0) + (\tilde\omega_0 - \omega_0) \qquad \text{(add and subtract } \tilde\omega_0\text{).}$$
> Pull back along $s$ and use that the pullback $s^* : \Omega^1(P;i\mathbb{R}) \to \Omega^1(U;i\mathbb{R})$ is $\mathbb{R}$-linear:
> $$s^*(\omega-\omega_0) = s^*(\omega-\tilde\omega_0) + s^*(\tilde\omega_0-\omega_0) \qquad \text{(linearity of } s^*\text{).}$$
> Dividing by $i$,
> $$A(\omega,\omega_0) = A(\omega,\tilde\omega_0) + A(\tilde\omega_0,\omega_0).$$
> **Section-independence.** Each of the three relative potentials is independent of the chosen section $s$: for $U(1)$ the adjoint action is trivial, so the difference of two connections is a horizontal, $\operatorname{Ad}$-invariant $i\mathbb{R}$-valued $1$-form on $P$ and therefore descends to a well-defined global $1$-form on $M$ (this is the same descent that defines $F$ from $\bar\Omega$, recorded on [[Def - U(1) Gauge Field and Electromagnetic Connection|the electromagnetic-connection page]]). Concretely, under a change of section $s' = s\cdot e^{i\chi}$ the differences $\omega-\omega_0$ etc. all transform the same way — their gauge shifts $d(i\chi)$ cancel in the difference — so all three $A$'s in the identity are unambiguous, and the identity holds globally on $M$. In particular $A(\tilde\omega_0,\omega_0)$ is a single, well-defined $1$-form on $M$ that depends on $\tilde\omega_0$ and $\omega_0$ but on nothing else.

**Step 2: The two Lagrangians differ by a fixed $4$-form.**

$$L(\omega) - \tilde L(\omega) = A(\tilde\omega_0,\omega_0) \wedge J, \qquad \text{with } A(\tilde\omega_0,\omega_0) \text{ independent of } \omega.$$

> [!note]- Derivation
> Write out both Lagrangians, using that the field strength $F$ is defined from $\omega$ alone (through $\bar\Omega = iF$) and hence is the *same* in both:
> $$L(\omega) = \tfrac12 F\wedge\star F + A(\omega,\omega_0)\wedge J, \qquad \tilde L(\omega) = \tfrac12 F\wedge\star F + A(\omega,\tilde\omega_0)\wedge J.$$
> Subtract; the identical $L_1 = \tfrac12 F\wedge\star F$ terms cancel:
> $$L(\omega) - \tilde L(\omega) = \big(A(\omega,\omega_0) - A(\omega,\tilde\omega_0)\big)\wedge J \qquad \text{(the } L_1 \text{ terms are equal and cancel).}$$
> By the cocycle identity of Step 1, $A(\omega,\omega_0) - A(\omega,\tilde\omega_0) = A(\tilde\omega_0,\omega_0)$, so
> $$L(\omega) - \tilde L(\omega) = A(\tilde\omega_0,\omega_0)\wedge J \qquad \text{(by Step 1).}$$
> By the section-independence established in Step 1, the $1$-form $A(\tilde\omega_0,\omega_0)$ is a fixed object built from the two backgrounds; $J$ is fixed by hypothesis; hence the right-hand side is a $4$-form on $M$ that **does not depend on $\omega$**.

**Step 3: The difference term has zero variation.**

Along any admissible variation $\omega_{t,\eta}$, the difference $4$-form is constant in $t$, so its variation vanishes.

> [!note]- Derivation
> Fix an open $U \Subset M$ and $\eta \in \Omega^1(M;\mathbb{R})$ with $\operatorname{supp}\eta \subset U$, and let $\omega_{t,\eta} \in \mathcal{C}(P)$ be the variation with $A(\omega_{t,\eta},\omega_0) = A(\omega,\omega_0) + t\eta$, which exists and is a genuine curve of connections by [[Thm - The Space of Connections is an Affine Space|the affine-space theorem]] (add $t\cdot i\eta \in \Omega^1(M;i\mathbb{R})$ to $\omega$). Apply Step 2 with $\omega_{t,\eta}$ in place of $\omega$:
> $$L(\omega_{t,\eta}) - \tilde L(\omega_{t,\eta}) = A(\tilde\omega_0,\omega_0)\wedge J \qquad \text{(Step 2, valid for every connection, in particular } \omega_{t,\eta}\text{).}$$
> The right-hand side does not depend on $t$: neither $A(\tilde\omega_0,\omega_0)$ (it is built from the fixed backgrounds) nor $J$ (fixed) involves the varied connection. Integrate over $\bar U$ and differentiate:
> $$\frac{d}{dt}\Big|_0 \int_{\bar U}\big(L(\omega_{t,\eta}) - \tilde L(\omega_{t,\eta})\big) = \frac{d}{dt}\Big|_0 \int_{\bar U} A(\tilde\omega_0,\omega_0)\wedge J = \frac{d}{dt}\Big|_0\, C = 0,$$
> where $C := \int_{\bar U} A(\tilde\omega_0,\omega_0)\wedge J \in \mathbb{R}$ is a constant independent of $t$ (a fixed number, being the integral of a fixed compactly-restricted $4$-form over the fixed region $\bar U$), and the derivative of a constant is zero. This is claim 2.

**Step 4: Criticality is background-independent.**

$\omega$ is critical for $L$ if and only if it is critical for $\tilde L$; both give $d\star F + J = 0$.

> [!note]- Derivation
> By linearity of the derivative and of the integral, for every admissible $U$ and $\eta$,
> $$\frac{d}{dt}\Big|_0 \int_{\bar U} L(\omega_{t,\eta}) = \frac{d}{dt}\Big|_0 \int_{\bar U} \tilde L(\omega_{t,\eta}) + \frac{d}{dt}\Big|_0 \int_{\bar U}\big(L(\omega_{t,\eta}) - \tilde L(\omega_{t,\eta})\big) = \frac{d}{dt}\Big|_0 \int_{\bar U}\tilde L(\omega_{t,\eta}) + 0,$$
> the last term vanishing by Step 3. Hence the first variation of $L$ equals the first variation of $\tilde L$ *for every* choice of $U \Subset M$ and every compactly supported $\eta$. By the definition of criticality — $\omega$ is critical for a Lagrangian if and only if all these first variations vanish — the two conditions "$\omega$ critical for $L$" and "$\omega$ critical for $\tilde L$" are the same condition. By [[Thm - Euler-Lagrange Equation of the Electromagnetic Action|the Euler–Lagrange theorem]], each is equivalent to
> $$d\star F + J = 0,$$
> an equation on $M$ that contains only the field strength $F$ (equivalently the descended curvature $\bar\Omega = iF$) and the fixed current $J$, and no background connection whatsoever. Therefore the equation of motion is independent of the arbitrary choice of $\omega_0$. $\blacksquare$

> [!note]- Complete formal solution
> **Claim.** Replacing the background connection $\omega_0$ by $\tilde\omega_0$ changes the electromagnetic Lagrangian by the $\omega$-independent $4$-form $A(\tilde\omega_0,\omega_0)\wedge J$, whose first variation vanishes; consequently the two Lagrangians have the same critical connections and the same Euler–Lagrange equation $d\star F + J = 0$.
>
> Fix a local section $s$ of $P$. From $iA(\cdot,\cdot) = s^*(\cdot-\cdot)$ and the linearity of $s^*$ applied to $\omega-\omega_0 = (\omega-\tilde\omega_0)+(\tilde\omega_0-\omega_0)$,
> $$A(\omega,\omega_0) = A(\omega,\tilde\omega_0) + A(\tilde\omega_0,\omega_0);$$
> all three relative potentials are section-independent because, $U(1)$ being abelian, differences of connections descend to global $1$-forms on $M$, so $A(\tilde\omega_0,\omega_0)$ is a fixed $1$-form on $M$.
>
> Since $F$ is defined from $\omega$ alone, $L_1 = \tfrac12 F\wedge\star F$ is common to $L$ and $\tilde L$, and
> $$L(\omega)-\tilde L(\omega) = \big(A(\omega,\omega_0)-A(\omega,\tilde\omega_0)\big)\wedge J = A(\tilde\omega_0,\omega_0)\wedge J,$$
> a $4$-form independent of $\omega$.
>
> For an admissible variation $\omega_{t,\eta}$ (which exists by the affine structure of $\mathcal{C}(P)$), applying the previous line with $\omega_{t,\eta}$ shows $L(\omega_{t,\eta})-\tilde L(\omega_{t,\eta}) = A(\tilde\omega_0,\omega_0)\wedge J$ is constant in $t$, so
> $$\frac{d}{dt}\Big|_0\int_{\bar U}\big(L(\omega_{t,\eta})-\tilde L(\omega_{t,\eta})\big) = 0.$$
> Hence $\tfrac{d}{dt}|_0\int_{\bar U}L(\omega_{t,\eta}) = \tfrac{d}{dt}|_0\int_{\bar U}\tilde L(\omega_{t,\eta})$ for all $U,\eta$, so $\omega$ is critical for $L$ iff critical for $\tilde L$. By the Euler–Lagrange theorem each is equivalent to $d\star F + J = 0$, which mentions no background connection. $\blacksquare$

> [!warning] Illegal but tempting: "the coupling term is gauge, so just drop it"
> One might try to argue more crudely — "$A\wedge J$ is not gauge-invariant, so it is unphysical and can be discarded, and then there is no $\omega_0$ to worry about". This is wrong on two counts. First, $A\wedge J$ cannot simply be dropped: its variation $\tfrac{d}{dt}|_0\int(A+t\eta)\wedge J = \int\eta\wedge J$ is precisely what produces the source term $+J$ in the field equation $d\star F + J = 0$; without it one would obtain the *vacuum* equation $d\star F = 0$ and lose all coupling to charges. What is genuinely reference-independent is not the term but the *difference* between two choices of reference, and only because that difference is $\omega$-independent. Second, the correct statement is not that $L_2$ is negligible but that its background-dependent part shifts the action by a constant; the physical, variation-carrying part of $L_2$ survives. The extra condition that makes the naive "drop it" legal is exactly what we proved: the discarded piece must be independent of the field being varied. Retain $A\wedge J$; discard only $A(\tilde\omega_0,\omega_0)\wedge J$, and only after verifying it does not depend on $\omega$.

---

# Key Takeaways

**A choice built into an action is invisible to the equations of motion precisely when changing it shifts the action by a term independent of the field being varied.** This is the reusable principle, and it is worth stating in its general form: if an action $S_c(\phi)$ depends on an auxiliary choice $c$ (a reference point, a fiducial background, a boundary datum) only in such a way that $S_c(\phi) - S_{c'}(\phi)$ is independent of the field $\phi$, then the first variation $\tfrac{d}{dt}|_0 S_c(\phi_t)$ is the same for all $c$, and hence the critical points — the physical solutions — do not depend on $c$. Criticality is a first-derivative condition, and additive terms with zero derivative are simply not seen by it. The trigger condition to watch for is any action that names an arbitrary reference in its definition; the diagnostic is to compute the difference between two references and check that the field has dropped out of it. Here the reference is the background connection $\omega_0$, the field is $\omega$, and the difference is $A(\tilde\omega_0,\omega_0)\wedge J$, which contains no $\omega$. The same principle licenses dropping total-derivative terms (their variations are boundary integrals that vanish for compactly supported variations), additive constants, and reference-energy offsets throughout physics.

**Relative potentials are affine coordinates, and their reference-dependence obeys a cocycle identity that makes differences telescope.** The object $A(\omega,\omega_0)$ is best understood not as "the potential of the field" but as "the coordinate of the connection $\omega$ in the affine chart whose origin is $\omega_0$" — the connections form an affine space, and choosing a background connection is choosing an origin, which turns the affine space into a vector space. Changing the origin from $\omega_0$ to $\tilde\omega_0$ shifts every coordinate by the *same* constant vector $A(\tilde\omega_0,\omega_0)$, exactly as translating the origin of Euclidean coordinates shifts every position vector by a fixed amount. The identity $A(\omega,\omega_0) = A(\omega,\tilde\omega_0) + A(\tilde\omega_0,\omega_0)$ is the cocycle (or "chain") relation that all such reference-differences satisfy; it is why the $\omega$-dependence cancels in the subtraction. Recognising an object as an affine coordinate — connections here, but also potentials in electromagnetism, gauges in fibre bundles, and reference frames in relativity — immediately predicts that only *differences* of such coordinates, never the coordinates themselves, can be physical. When a computation produces a bare potential, look for the reference it is measured against and ask whether the final answer depends on that reference.

**The field strength carries the physics; the potential carries a choice — and separating the two is the recurring discipline of gauge theory.** The cleanest way to see that $\omega_0$ is harmless is to notice that it never touches $F$: the term $L_1 = \tfrac12 F\wedge\star F$, which is the genuinely dynamical, gauge-invariant part of the Lagrangian, is defined from the descended curvature $\bar\Omega = iF$ of $\omega$ with no reference to any background at all. Only the coupling term $L_2 = A\wedge J$ measures $\omega$ against $\omega_0$, and it does so through the potential, which is reference-dependent by construction. This split — curvature is physical and reference-free, potential is auxiliary and reference-dependent — is the organising fact of the whole subject: it is why gauge transformations change $A$ but not $F$ (the abelian case is [[Thm - Gauge Invariance of the Electromagnetic Lagrangian|gauge invariance of the electromagnetic Lagrangian]]), why the Aharonov–Bohm effect is felt through holonomy (an integral of $A$ around a loop, which is gauge-invariant) rather than through $A$ pointwise, and why the non-abelian Yang–Mills action in §7.4 is again built from the curvature $\bar\Omega$ and not from the gauge potential. Whenever a construction in gauge theory involves a potential, the transferable question is: does the final, physical statement depend only on the curvature and on gauge-invariant combinations, and is every apparent dependence on a potential or a reference an artefact that cancels? This exercise is the smallest instance where the answer is worked out in full.
