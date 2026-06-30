---
type: exercise
subject: special-relativity
difficulty: "⭐⭐⭐"
prereqs:
  - "Thm - The Equivalence Principle and the Failure of a Flat-Spacetime Gravity"
  - "Thm - Gravitational Redshift"
  - "Def - Minkowski Space and the Metric"
tags: [physics, special-relativity]
---

# Problem Statement

This is Schild's argument, and it is the cleanest impossibility proof in physics. It uses only the gravitational redshift (which the previous exercise derived) and the time-translation symmetry of a static field to derive a contradiction with the Minkowski metric — forcing the metric to become a position-dependent field $g_{\mu\nu}(x)$, which is the founding step of general relativity.

Consider a *static* uniform gravitational field $\vec g = -\gamma\vec e_x$ ($\gamma > 0$), with two observers $\mathcal{O}$ (at altitude $0$, receiver) and $\mathcal{O}'$ (at altitude $x_{\mathrm{em}}$, emitter), mutually at rest. The emitter sends a periodic electromagnetic signal of proper period $\Delta t'$; the receiver measures it with proper period $\Delta t = \Delta t'/(1 + \gamma x_{\mathrm{em}}/c^2) \neq \Delta t'$ (gravitational redshift, from the previous exercise).

1. *Set up the two successive signal crests.* Label the events of the first crest's emission $A'$ and reception $A$, the second crest's emission $B'$ and reception $B$. Indicate them on a spacetime diagram (in any chosen inertial frame).
2. *Use staticity.* Because the field is *static*, the worldlines and history of the second crest are obtained from those of the first crest by a *time translation* $\tau_{T}: t \mapsto t + T$ for some $T$. Argue precisely that the curve $B'B$ is the time-translate of the curve $A'A$ by $T = \Delta t' = \Delta t$ (in the chosen inertial frame, where the observers are static).
3. *Assume the Minkowski metric.* Suppose the proper time along a worldline is given by the Minkowski metric $\eta_{\mu\nu}$, as it has been throughout the preceding 24 chapters. The Minkowski metric is *itself* time-translation invariant: $\eta_{\mu\nu}$ is the same constant array at every event. Show this implies the proper-time interval of the emitter's worldline between $A'$ and $B'$ equals the proper-time interval of the receiver's worldline between $A$ and $B$.
4. *Derive the contradiction.* Combine step 3 with the redshift result $\Delta t \neq \Delta t'$. Conclude that the Minkowski metric *cannot* correctly measure proper time in a gravitational field.
5. *Identify the escape.* The contradiction forces one of the assumptions to be abandoned. Argue that the equivalence principle is non-negotiable (experimental, $10^{-13}$), that staticity is satisfied by definition for the configuration considered, and that the redshift is a robust consequence. Conclude that the metric itself must be a position-dependent field $g_{\mu\nu}(x)$, breaking the time-translation symmetry of the metric while preserving it for the geometry. State the resolution: a metric of the form $g_{00}(x)\,dt^2 + (\text{spatial})$ with $g_{00}$ depending on altitude can correctly account for the redshift while keeping the *configuration* static.

**Recall:**

![[Thm - The Equivalence Principle and the Failure of a Flat-Spacetime Gravity#Statement]]

![[Thm - Gravitational Redshift#Statement]]

The exercise's key inputs are: (i) the gravitational redshift, an established consequence of the equivalence principle; (ii) the time-translation symmetry of a *static* field (one that does not depend on $t$); (iii) the time-translation symmetry of the Minkowski metric, which is constant at every event. The contradiction extracts itself from these three facts.

---

# Convergent Strategy

**Problem class.** An *impossibility proof by clash of two symmetries against one measurement*. The setup is: a symmetry the metric possesses (time-translation invariance), a symmetry the configuration possesses (staticity, so successive signals are time-translates), and a measurement that distinguishes them (the redshift). When the two symmetries together force a definite answer that the measurement contradicts, one of the assumptions must go — and the argument's power is that it points at exactly which one.

**Assumption pattern.** Three ingredients: a static field (so successive periodic signals are time-translates of each other), the gravitational redshift (so the periods differ), and the Minkowski metric (so the metric is time-translation invariant). The three are inconsistent. Removing the Minkowski metric — letting it become a position-dependent field — is the unique consistent option, because the staticity is by hypothesis and the redshift is empirically forced.

**Theorem routing.** Part 1 is setup. Part 2 exploits the static symmetry of the field: any time-translation maps each observer's worldline to itself, and maps the entire history of the first signal crest to that of the second. Part 3 exploits the time-translation symmetry of $\eta$: a translation-invariant metric assigns equal lengths to a curve and its time-translate. Part 4 combines them: the metric must give $\Delta t' = \Delta t$, but the redshift gives $\Delta t \neq \Delta t'$. Part 5 identifies what gives way: the metric loses its constancy and becomes a field.

**Key decision point.** The crux is the recognition that the argument *never uses the detail of the photons' worldlines*. The photons might travel along curved paths, along null geodesics of some metric, or however one wishes — the argument cares only about the *staticity* of the configuration and the *constancy* of the metric. This independence from photon dynamics is what makes the conclusion airtight: it is forced by symmetry, not by any specific model.

---

# Legal Operations Used

1. **Use a static field to impose time-translation symmetry on successive signals** (operation 5 from the topic page): the heart of the argument — successive light signals are time-translates of one another because the field does not change with time.

2. **Derive the redshift from the accelerated-frame spectral shift** (operation 6 from the topic page): the redshift is an input; it has been imported from the previous exercise via the equivalence principle.

3. **Invoke the equivalence principle to swap a gravitational field for an accelerated frame** (operation 2 from the topic page): the source of the redshift, which is the measurement that contradicts the metric.

---

# Hints

> [!note]- Hint 1
> Draw spacetime in the inertial frame where $\mathcal{O}$ is at the origin and $\mathcal{O}'$ is at altitude $x_{\mathrm{em}}$. Both observers' worldlines are vertical lines at $x = 0$ and $x = x_{\mathrm{em}}$ (they are mutually at rest). The first crest leaves $A'$ on the upper worldline and arrives at $A$ on the lower; the second leaves $B'$ on the upper and arrives at $B$ on the lower. The four events form a rough parallelogram, with $A'$ vertically above $A$ and $B'$ vertically above $B$.

> [!note]- Hint 2
> Static = "no dependence on $t$". Time translation $\tau_T: (t, x) \mapsto (t+T, x)$ sends the upper worldline to itself and the lower worldline to itself. It sends the first crest's emission event $A'$ to $\tau_T(A') = B'$ if $T = \Delta t'$ (the emission period). The photon's null worldline from $A'$, propagating under the *same* (static) field, is mapped by $\tau_T$ to the null worldline from $B'$ — the second crest's. Both arrive at $A$ and $B$ respectively, with $\tau_T(A) = B$ iff $T = \Delta t$ (the reception period). For these to be consistent, since the *same* translation maps both, we need $\Delta t' = T = \Delta t$ — but only if the staticity argument doesn't break.

> [!note]- Hint 3
> The Minkowski metric is $\eta_{\mu\nu} = \mathrm{diag}(+1, -1, -1, -1)$ at every event $x \in \mathscr{E}$. Under translation $\tau_T$, it pulls back to itself: $(\tau_T^*\eta)_{\mu\nu}(x) = \eta_{\mu\nu}(\tau_T^{-1}(x)) = \eta_{\mu\nu}$. So the proper-time integral $\int\sqrt{\eta_{\mu\nu}\dot x^\mu\dot x^\nu}\,d\lambda$ along a curve is invariant under $\tau_T$. The emitter's worldline from $A'$ to $B'$ is mapped by $\tau_T$ to its time-translate; but $\mathcal{O}'$ is *itself* a static worldline, so $\tau_T$ maps it to itself, and the part from $A'$ to $B'$ is mapped to the part from $\tau_T(A')$ to $\tau_T(B')$. Identifying $\tau_T(A') = B'$ and $\tau_T(B') = $ next emission gives that the emitter's $A'\to B'$ proper time equals... well, the emitter's worldline parametrised consistently. The cleaner statement: the *photon* worldlines from $A'$ to $A$ and from $B'$ to $B$ are related by $\tau_T$, so their *Minkowski lengths* are equal. But both photon worldlines are null, so they have zero length — not useful directly. The useful Minkowski lengths are those of the *observer* worldline segments $A'B'$ (emitter) and $AB$ (receiver), each parametrising the period. Since $\tau_T$ maps each to itself and preserves the metric, the segments have the same Minkowski length, hence $\Delta t_{\mathrm{em}}^{(\eta)} = \Delta t_{\mathrm{rec}}^{(\eta)}$, where superscript $(\eta)$ means "measured by $\eta$".

> [!note]- Hint 4
> Step 3 gave: if proper time is measured by $\eta$, then $\Delta t' = \Delta t$ (the emitter and receiver, related by the translation $\tau_T$, must measure equal proper-time periods for translated portions of their static worldlines, because the metric is itself translation-invariant). But the redshift (from the equivalence principle) gives $\Delta t = \Delta t'/(1 + \gamma x_{\mathrm{em}}/c^2) \neq \Delta t'$. The two are inconsistent: $\Delta t = \Delta t'$ and $\Delta t \neq \Delta t'$ cannot both hold. Hence the assumption that proper time is measured by $\eta$ is false.

> [!note]- Hint 5
> The equivalence principle has been experimentally tested to $3\times 10^{-13}$ — it is non-negotiable. The staticity is by hypothesis (we can choose to consider a static field, and the contradiction must hold there). The redshift follows from the equivalence principle alone. So the casualty is the Minkowski metric. The natural replacement is a metric that *itself depends on position*: $g_{\mu\nu}(x)$. Specifically, a static metric of the form $g_{\mu\nu}(x) = g_{\mu\nu}(\vec r)$ (no $t$-dependence in the metric coefficients) is still time-translation symmetric as a geometric structure, but the actual numerical values of $g_{00}, g_{ij}$ depend on altitude. For example $g_{00} = 1 + 2\Phi(\vec r)/c^2$ in the weak-field limit gives different clock rates at different altitudes, exactly the redshift, without needing to break staticity. The metric becomes a *field*, and that is general relativity.

---

# Solution

This is Schild's argument (1960), the cleanest impossibility proof in physics and the structural reason general relativity is forced. It uses only what the previous exercise established (the redshift) and one symmetry observation (the time-translation invariance of a static field, plus that of the Minkowski metric) to derive a contradiction. The escape — letting the metric become a position-dependent field — is the founding step of general relativity.

**Step 1: Set up the two crests.**

> [!note]- Derivation
> Work in the inertial frame in which $\mathcal{O}$ and $\mathcal{O}'$ are both static. Their worldlines are vertical lines: $\mathcal{O}$ at $x = 0$, $\mathcal{O}'$ at $x = x_{\mathrm{em}}$. Both stretch from past to future infinity.
>
> *First crest:* emitted at event $A'$ on $\mathcal{O}'$'s worldline at coordinate time $t_{A'}$; propagates as a (possibly curved-in-this-frame, possibly straight) null worldline; received at event $A$ on $\mathcal{O}$'s worldline at coordinate time $t_A$.
>
> *Second crest:* emitted at $B'$ on $\mathcal{O}'$'s worldline at coordinate time $t_{B'} = t_{A'} + \Delta t'$ (one emission period later, as measured by $\mathcal{O}'$'s proper time, which in this frame is the same as coordinate time since $\mathcal{O}'$ is static); received at $B$ on $\mathcal{O}$'s worldline at $t_B = t_A + \Delta t$ (one reception period later, by the same argument).
>
> By the redshift, $\Delta t \neq \Delta t'$.
>
> *Spacetime diagram* (in this chosen frame): the four events $A', A, B', B$ form a quadrilateral with $A'$ above $A$ (separated by $x_{\mathrm{em}}$ in space), $B'$ above $B$ (separated by $x_{\mathrm{em}}$), and the two vertical worldline segments $A'B'$, $AB$ of lengths $\Delta t', \Delta t$ respectively (the proper times of the observers between successive crests).

**Step 2: Staticity makes the second crest the time-translate of the first.**

> [!note]- Derivation
> "Static" means that nothing about the configuration depends on the coordinate time $t$. Specifically:
> - The gravitational field $\vec g = -\gamma \vec e_x$ does not depend on $t$.
> - The two observers' worldlines (vertical lines $x = 0, x_{\mathrm{em}}$) are translation invariant in $t$.
> - The laws of physics that govern photon propagation in the field (whatever they are — they need not be specified) do not depend on $t$.
>
> Now apply the time-translation $\tau_T: (t, x) \mapsto (t + T, x)$ with $T = \Delta t'$ (the emitter's period). The translation maps:
> - $\mathcal{O}'$'s worldline to itself (because the worldline is translation invariant);
> - $\mathcal{O}$'s worldline to itself (likewise);
> - The event $A'$ at $(t_{A'}, x_{\mathrm{em}})$ to $\tau_T(A') = (t_{A'} + T, x_{\mathrm{em}}) = (t_{B'}, x_{\mathrm{em}}) = B'$;
> - The first crest's null worldline $A' \to A$ to a translated null worldline starting at $B'$. By staticity (laws of propagation are translation-invariant), this translated worldline *is* the second crest's worldline. So $\tau_T(A) = B$.
>
> From $\tau_T(A) = B$ and $T = \Delta t'$, in the coordinate time of $\mathcal{O}$'s worldline: $t_B = t_A + T = t_A + \Delta t'$. But $\mathcal{O}$'s coordinate time and proper time coincide (she is static at the origin), and we defined $t_B = t_A + \Delta t$. Therefore — *if staticity holds for the entire propagation* — we must have $\Delta t = \Delta t'$.
>
> Wait. The redshift gives $\Delta t \neq \Delta t'$. So if we trust the redshift *and* the staticity, we are forced to deny something else. What was assumed in deriving $\Delta t = \Delta t'$ from staticity? The reduction "coordinate time = proper time" — which is true for $\mathcal{O}$ in this inertial frame *iff* proper time is measured by $\eta$. That is the assumption being smuggled in.

**Step 3: Minkowski metric is time-translation invariant.**

> [!note]- Derivation
> The Minkowski metric $\eta_{\mu\nu} = \mathrm{diag}(+1, -1, -1, -1)$ is the *same constant array* at every event $x \in \mathscr{E}$. Under translation $\tau_T: (t, x^i) \mapsto (t+T, x^i)$,
> $$(\tau_T^*\eta)_{\mu\nu}(x) = \eta_{\mu\nu}(\tau_T^{-1}(x)) = \eta_{\mu\nu}.$$
> So translation is an *isometry* of $\eta$: it preserves the metric exactly.
>
> Consequence: the *length* of any curve, computed with $\eta$, is invariant under translation. For a worldline segment $\gamma(\lambda)$, $\lambda \in [0, 1]$,
> $$L_\eta(\gamma) = \int_0^1 \sqrt{\eta_{\mu\nu}\dot\gamma^\mu\dot\gamma^\nu}\,d\lambda,$$
> and $L_\eta(\tau_T \circ \gamma) = L_\eta(\gamma)$, because the integrand is point-wise preserved.
>
> *Application to our segments.* The segment of $\mathcal{O}'$'s worldline from $A'$ to $B'$ (proper time $\Delta t'$ by definition) is mapped by $\tau_{\Delta t'}$ to a translated segment — which, since $\mathcal{O}'$'s worldline maps to itself, is the segment from $B'$ to the next emission event. So $L_\eta(A'B') = L_\eta(B'C')$ where $C'$ is the next emission — but that just says the *emitter* takes equal Minkowski-proper-time periods between successive emissions, which is consistent.
>
> The *useful* application: compare the *photon* worldlines. The first crest's worldline $\gamma_1: A' \to A$ has some shape; the second's $\gamma_2: B' \to B$ is its time-translate, $\gamma_2 = \tau_T \circ \gamma_1$ with $T = \Delta t'$. By the isometry property, $L_\eta(\gamma_1) = L_\eta(\gamma_2)$. But both photon worldlines are null, $L_\eta(\gamma_1) = L_\eta(\gamma_2) = 0$. So this comparison gives $0 = 0$ — trivially true, not useful directly.
>
> But the relation $\tau_T(A) = B$ from Step 2 (where $T = \Delta t'$) plus the fact that $\mathcal{O}$'s worldline is mapped to itself, means: travelling along $\mathcal{O}$'s static worldline from $A$ to $\tau_T(A) = B$, the Minkowski-proper-time elapsed is *exactly* $T = \Delta t'$ (by translation invariance of the metric along a static worldline). But the actual $\mathcal{O}$-proper-time from $A$ to $B$ is $\Delta t$. If proper time *is* measured by $\eta$, then $\Delta t = \Delta t'$.

**Step 4: Contradiction.**

> [!note]- Derivation
> Combining:
> - From the symmetry (Steps 2 + 3, *assuming proper time is measured by $\eta$*): $\Delta t = \Delta t'$.
> - From the redshift (the previous exercise, derived from the equivalence principle): $\Delta t = \Delta t'/(1 + \gamma x_{\mathrm{em}}/c^2) \neq \Delta t'$.
>
> These are incompatible. Something assumed is false. The only assumption *that can be false* is the boxed one: proper time is *not* measured by the Minkowski metric $\eta$ in a gravitational field. (The staticity is by hypothesis; the equivalence principle is empirically rock-solid; the redshift follows from these.)
>
> $\blacksquare$ *Schild's contradiction.*
>
> Note: this argument did *not* use the shape of the photons' worldlines, the speed of light in any frame, or any field equation. It used only (a) staticity, (b) the redshift, and (c) translation invariance of $\eta$. The conclusion is therefore airtight — it cannot be evaded by any clever choice of photon trajectory or field-theory mechanism.

**Step 5: The escape — a position-dependent metric $g_{\mu\nu}(x)$.**

> [!note]- Derivation
> The contradiction forces one assumption to give way. Audit them:
>
> *Can we drop the equivalence principle?* It is experimentally verified to $3\times 10^{-13}$ in the Eötvös-type and MICROSCOPE experiments. Dropping it would require a discovery of universal-mass-ratio dependence in free fall, which has never been observed. Verdict: not negotiable.
>
> *Can we drop staticity?* It was a hypothesis of the problem, chosen to make the argument work. A real planet's field is static or nearly so, and laboratory experiments (Pound-Rebka in the Earth's static field) confirm the redshift. Verdict: by construction.
>
> *Can we drop the redshift?* It is a derived consequence of the equivalence principle (the previous exercise) and is experimentally confirmed (Pound-Rebka 1960 to $1\%$; modern atomic clocks to $10^{-17}$). Dropping it would mean both the equivalence principle and direct measurement are wrong. Verdict: empirically forced.
>
> *Can we drop "proper time is measured by $\eta$"?* Yes — and there is no experimental or principled obstacle. The Minkowski metric was *introduced* in [[Special Relativity III — Minkowski Spacetime and the Metric|chapter III]] as a postulate, supported by all of special relativity's success. But that success was in the absence of gravity; the equivalence principle now tells us gravity exists and forces a contradiction with $\eta$. So $\eta$ must be replaced.
>
> *What replaces it?* A position-dependent metric $g_{\mu\nu}(x)$: a different symmetric bilinear form at each event, varying smoothly. The proper time along a worldline is now
> $$d\tau = \sqrt{g_{\mu\nu}(x)\,\dot x^\mu\dot x^\nu}\,d\lambda.$$
> Specifically, a *static* gravitational field can be accommodated by a *static* metric:
> $$ds^2 = g_{00}(\vec r)\,dt^2 - g_{ij}(\vec r)\,dx^i dx^j,$$
> in which $g_{\mu\nu}$ does not depend on $t$ (so the configuration is still translation symmetric) but does depend on $\vec r$ (so different altitudes have different clock rates). In the weak-field limit,
> $$g_{00}(\vec r) = 1 + \frac{2\Phi(\vec r)}{c^2},$$
> with $\Phi$ the Newtonian potential. A static observer at altitude $\vec r$ has proper time $d\tau = \sqrt{g_{00}(\vec r)}\,dt$, so two static observers at different altitudes have *different* clock rates, with ratio
> $$\frac{d\tau(\vec r_1)}{d\tau(\vec r_2)} = \sqrt{\frac{g_{00}(\vec r_1)}{g_{00}(\vec r_2)}} \approx 1 + \frac{\Phi(\vec r_1) - \Phi(\vec r_2)}{c^2} = 1 + \frac{\Delta\Phi}{c^2}.$$
> This is exactly the redshift — recovered structurally, as a property of the metric, with no contradiction with staticity (because the metric is time-translation invariant *as a tensor field*, but its values vary spatially).
>
> *General relativity.* The metric $g_{\mu\nu}(\vec r)$ is now the dynamical variable; it obeys an equation of motion (Einstein's equation) sourced by energy and momentum; freely-falling observers follow its geodesics; the obstruction to making it equal $\eta$ everywhere at once is the *curvature*. Special relativity survives as the tangent-space limit at each event, where the metric reduces to $\eta$ to leading order. The vault's [[General Relativity I — Einstein's Equations and Schwarzschild]] develops this in full, and the relevant differential geometry is in [[Def - Semi-Riemannian Metric and Signature]] and [[Riemannian Geometry III — Riemann Curvature and Topology]]. *Schild's argument is what makes general relativity necessary, not just possible.*

> [!note]- Complete formal solution
> *Setup.* Two static observers in static field $\vec g = -\gamma\vec e_x$, emitter $\mathcal{O}'$ at altitude $x_{\mathrm{em}}$, receiver $\mathcal{O}$ at $0$. Periodic signal: first crest events $A'$, $A$; second $B'$, $B$. Redshift (from equivalence principle) gives $\Delta t \neq \Delta t'$. *Staticity argument.* The configuration is invariant under $\tau_T: (t, x) \mapsto (t+T, x)$. With $T = \Delta t'$, $\tau_T(A') = B'$, and (by translation-invariance of the physical laws and the field) the first crest's worldline maps to the second's, so $\tau_T(A) = B$. *Metric-invariance argument.* Assuming proper time is measured by $\eta$, which is itself translation invariant ($\tau_T^*\eta = \eta$), the Minkowski-proper-time from $A$ to $\tau_T(A) = B$ along $\mathcal{O}$'s static worldline equals $T = \Delta t'$. But $\mathcal{O}$'s actual proper time from $A$ to $B$ is $\Delta t$. So $\Delta t = \Delta t'$, contradicting the redshift. *Verdict.* The equivalence principle is empirically forced ($10^{-13}$); the redshift follows; the staticity is by hypothesis; the casualty is "proper time measured by $\eta$". *Resolution.* The metric must be position-dependent, $g_{\mu\nu}(\vec r)$. A static metric $g_{00}(\vec r) = 1 + 2\Phi(\vec r)/c^2$ (weak field) gives static configurations with altitude-dependent clock rates, $d\tau \propto \sqrt{g_{00}}\,dt$, recovering the redshift $\Delta\nu/\nu = -\Delta\Phi/c^2$ structurally without contradiction. The metric becomes a field, sourced by energy-momentum, obeying Einstein's equation; freely-falling worldlines are its geodesics; the obstruction to flatness is curvature. *That is general relativity.* The argument never used photon dynamics, only staticity + redshift + translation-invariance of the metric — its robustness is its power. $\blacksquare$

---

# Key Takeaways

**Schild's argument is the cleanest impossibility proof in physics, and its power is that it needs almost nothing.** What this exercise teaches more than any individual technical move is the *form* of a great no-go theorem: a contradiction extracted from a minimal set of robust assumptions, immune to model details. Here the inputs are (i) the equivalence principle (experimentally rock-solid at $10^{-13}$), (ii) a static field (by hypothesis), and (iii) the time-translation invariance of the Minkowski metric (a property of the metric, not of any dynamics). From these three, in three lines, comes the contradiction that ends special relativity's claim to describe gravity. No field equation, no trajectory, no detail of how light propagates: just a redshift and a symmetry. The reusable pattern, of the highest leverage, is this: when you suspect a structure is impossible, look for a *symmetry* it would have to respect and a *measurement* that would have to violate it. The clash of the two is the proof. Schild used a static field's time-translation symmetry against the redshift, and in three lines killed flat-spacetime gravity. This pattern recurs throughout physics — Bell's theorem against local hidden variables, the Coleman-Mandula theorem against trivial extensions of spacetime symmetry, the No-Cloning theorem against quantum cloning — each is a symmetry-versus-measurement clash, each is robust to model details for the same reason Schild's argument is.

**The metric must be a *field* — varying smoothly from event to event — and that is the founding step of general relativity.** The structural escape from Schild's contradiction is unique: the only assumption that can be dropped consistent with experiment is "proper time is measured by $\eta$". The replacement, $g_{\mu\nu}(x)$, is a *symmetric bilinear form depending on position* — a tensor *field* on spacetime, not a fixed background. This is the single most consequential shift in conceptual physics: the metric, which throughout special relativity was a static piece of geometric furniture, becomes a dynamical object. Spacetime becomes a *manifold* (the appropriate setting for a varying metric); freely-falling observers follow geodesics of this manifold; the obstruction to making the metric flat globally — the curvature — is the gravitational field. The vault's [[General Relativity I — Einstein's Equations and Schwarzschild]] develops the dynamics (Einstein's equation), and [[Def - Semi-Riemannian Metric and Signature]] develops the differential geometry. From the special-relativity side, *the entire 24-chapter edifice now has a ceiling*: it is the chapter of Lorentzian geometry in which the metric is allowed to be indefinite but must be constant; once it is also allowed to vary, one is in general relativity. The arc of the subject is the loosening of two assumptions about the metric — first its definiteness, then its constancy — and each loosening is a new physics.

**The argument's independence from photon dynamics is what makes it airtight, and is the model for any "no-go theorem" worth trusting.** A subtle but crucial feature of Schild's argument is what it does *not* use: it does not assume light travels in straight lines, on null geodesics of any specific metric, at constant speed, or in any particular pattern. The photon worldlines from $A'$ to $A$ and from $B'$ to $B$ are simply called "worldlines", with no shape attached. The argument uses only that they exist and that the *configuration as a whole* (field plus observers plus photons) is invariant under time translation. This independence from the details of light propagation is what makes the conclusion immune to attempts to evade it by, say, postulating that gravity affects light's speed or that photons follow curved worldlines in a modified flat-spacetime theory. Any such modification still gives a static configuration, and Schild's argument still applies: the conclusion follows from symmetry alone, not from any detail of the dynamics. *This is the signature of every no-go theorem worth trusting* — its dependence on robust, model-independent inputs and its insensitivity to the specifics of how one wants to wriggle out. The reusable lesson is to construct one's no-go arguments to depend only on symmetries and minimal empirical inputs; any reliance on detailed dynamics is a weakness that the next theorist will exploit to evade the conclusion.
