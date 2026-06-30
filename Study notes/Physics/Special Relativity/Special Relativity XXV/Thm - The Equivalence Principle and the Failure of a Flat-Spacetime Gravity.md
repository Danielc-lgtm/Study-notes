---
type: theorem
subject: special-relativity
prereqs:
  - "Def - Minkowski Space and the Metric"
  - "Thm - Gravitational Redshift"
  - "Def - Uniformly Accelerated Observer (Hyperbolic Motion)"
tags: [physics, special-relativity]
---

# Notation

We set $c = 1$ and use mostly-minus $\eta_{\mu\nu} = \mathrm{diag}(+1,-1,-1,-1)$, timelike $X\cdot X > 0$. $\Phi$ is the gravitational potential; $\vec g = -\gamma\,\vec e_x$ a uniform gravitational field of magnitude $\gamma > 0$ (here $\gamma$ is a field strength, *not* the Lorentz factor); $\vec a$ the four-acceleration of an observer. Two inertial observers $\mathcal{O}$ (at $x = 0$) and $\mathcal{O}'$ (at altitude $x = x_{\mathrm{em}}$) are mutually at rest in the field; $\mathcal{O}'$ emits a periodic signal of proper period $\Delta t'$, received by $\mathcal{O}$ with proper period $\Delta t$. $\eta_{\mu\nu}$ is the flat metric; $g_{\mu\nu}(x)$ a general position-dependent metric. $A, B, A', B'$ are the spacetime events of two successive emissions and receptions. Full registry on [[Special Relativity XXV — Toward Relativistic Gravitation]].

---

# Statement

> **The equivalence principle and the failure of flat-spacetime gravity.** Assume the **equivalence principle**: as far as physical measurements are concerned, an inertial observer in a uniform gravitational field is equivalent to a uniformly accelerated observer in the absence of gravity. Then:
> 1. *(Redshift.)* Two observers $\mathcal{O}$, $\mathcal{O}'$ mutually at rest at altitudes $0$ and $x_{\mathrm{em}}$ in a uniform field measure unequal periods for a transmitted periodic signal: $\Delta t = \Delta t'/(1 + \gamma\,x_{\mathrm{em}}/c^2) \neq \Delta t'$.
> 2. *(Incompatibility.)* In a static gravitational field the proper time **cannot** be given by the Minkowski metric $\eta_{\mu\nu}$. Indeed, if it were, the time-translation symmetry of the field would force $\Delta t = \Delta t'$, contradicting (1).
>
> Consequently any relativistic theory of gravitation obeying the equivalence principle must abandon the Minkowski metric in favour of a position-dependent metric field $g_{\mu\nu}(x)$ — and that theory is general relativity.

The argument is due to Alfred Schild (1960); the equivalence principle was enunciated by Einstein in 1907, who called it the "happiest thought" of his life.

---

# Motivation

The previous chapters built an entire physics on a single fixed object: the Minkowski metric $\eta_{\mu\nu}$, the same constant indefinite bilinear form at every event, with the [[Def - The Lorentz Group|Lorentz group]] as its global symmetry. The three failed field theories of §25.1 each tried to add gravity *on top of* this fixed stage and failed — scalar gravity gives no light bending, vector gravity has negative energy, tensor gravity either ignores matter or becomes general relativity. Those were "engineering" failures, each specific to a choice of field. This theorem is the *structural* failure: it shows, with no reference to any particular theory of gravity, that the Minkowski metric itself is incompatible with the most basic fact about gravity, the equivalence principle.

The importance is that it converts the question "can gravity be a field on Minkowski space?" from a series of trial-and-error attempts into a single impossibility proof. One does not need to enumerate field theories and reject them one by one; one shows that *any* theory respecting the equivalence principle must give up the flat metric. The equivalence principle is not negotiable — it is the experimentally ironclad equality of inertial and gravitational mass, verified to $10^{-13}$ — so the conclusion is forced. This is the moment special relativity is shown to have a definite boundary, and the moment the necessity of general relativity becomes a theorem rather than a hope.

The argument's elegance is that it spends almost nothing. It uses the equivalence principle to import the gravitational redshift from accelerated-frame kinematics — material the reader already has from [[Special Relativity XVI — Accelerated Observers|XVI]] — and then a single symmetry observation (a static field is time-translation invariant) to derive the contradiction. No field equation, no trajectory, no detail of how light propagates: just a redshift and a symmetry. That economy is the source of its power and the reason it is the right capstone for the whole sequence.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's hypothesis is "the equivalence principle holds, in a static field". The point of input broadening is to recognise the disguises this hypothesis wears.

The first disguised source is **"the inertial and gravitational masses of a body are equal"**. This is the experimental content of the equivalence principle, established by Eötvös ($10^{-8}$) and refined to $3\times 10^{-13}$ today. Whenever a problem states or assumes that all bodies fall identically — universality of free fall — it is asserting the equivalence principle, and this theorem applies. The bridge is that equal masses make the free-fall acceleration independent of the body, which is exactly what allows a uniform field to be mimicked by, and removed by, a change of frame. *Example problem:* given that a feather and a hammer fall together on the Moon, deduce that a uniform gravitational field is locally equivalent to an accelerated frame.

The second disguised source is **"a clock's rate depends on its gravitational potential"**. The gravitational redshift, in any of its experimental forms (Pound-Rebka, GPS), *is* the equivalence principle in measurable form. So any datum about clocks running at different rates at different heights is a source for this theorem's conclusion. The bridge is that the redshift is the proper-time inequality $\Delta t \neq \Delta t'$ that the static-metric symmetry then contradicts. *Example problem:* given the measured GPS clock offset of $46\,\mu\mathrm{s}/\mathrm{day}$, argue that proper time is not Minkowskian.

The third disguised source is **"spacetime admits a timelike Killing symmetry"** (a static or stationary field). Whenever the gravitational field does not change with time — a star at rest, a static potential $\Phi(\vec r)$ — successive light signals are time-translates of one another, which is the geometric fact Schild's argument turns against the flat metric. The bridge is that time-translation invariance forces a translation-invariant metric to assign equal lengths to translated curves. *Example problem:* in any static spacetime, show that the ratio of received to emitted frequencies between two fixed observers is constant in time, and use this to constrain the metric.

**Targets (Output Amplification)**

The conclusion is "the metric cannot be $\eta$; it must be a field $g_{\mu\nu}(x)$".

Combine the conclusion with **the requirement that special relativity hold locally**. Although the global metric must vary, the equivalence principle also says that in a freely-falling frame *at one event* the physics is exactly special-relativistic. The further result is the structure of a Lorentzian manifold: at each event there is a tangent space carrying the flat metric $\eta$, and $g_{\mu\nu}(x)$ reduces to $\eta$ there. The combination is the bridge from "the metric varies" to "spacetime is a manifold with a Minkowskian tangent space at each point". *Example:* the construction of locally inertial (Riemann normal) coordinates, in which $g_{\mu\nu} = \eta_{\mu\nu}$ and $\partial_\rho g_{\mu\nu} = 0$ at the chosen event.

Combine the conclusion with **the inhomogeneity of a real field**. A real gravitational field is not uniform, so the equivalence-principle frame removes it only at a point, and the residual — the tidal field — is irreducible. The further result is that the irreducible part of gravity is the *curvature* of $g_{\mu\nu}(x)$, the obstruction to making $g = \eta$ everywhere at once. The combination is nonobvious because it identifies "what is left of gravity after the equivalence principle removes it locally" with a specific geometric invariant. *Example:* geodesic deviation of two nearby freely-falling particles, governed by the Riemann tensor.

Combine the conclusion with **a least-action principle for the metric**. Once $g_{\mu\nu}(x)$ is the dynamical variable, demanding it obey a generally-covariant field equation derived from a Lagrangian (the simplest being the scalar curvature $R$) singles out the **Einstein equation**. The further result is the specific dynamics of general relativity. The combination is the bridge from "the metric is a field" to "the metric is *this* field, sourced by $T_{\mu\nu}$". *Example:* varying the Einstein-Hilbert action $\int R\sqrt{-g}\,d^4x$ to obtain $R_{\mu\nu} - \tfrac12 R g_{\mu\nu} = \tfrac{8\pi G}{c^4}T_{\mu\nu}$.

---

# Why Is It True

The whole argument is a clash between a measurement (the redshift) and a symmetry (the static field), and it is worth seeing why each is unavoidable.

First, *why is there a redshift?* The equivalence principle says the two observers $\mathcal{O}$ and $\mathcal{O}'$, at rest in a uniform field, are physically indistinguishable from two uniformly accelerated observers in flat spacetime. But for accelerated observers a frequency shift is elementary and has nothing to do with gravity: while a light signal travels from the lower observer to the higher one, the higher observer has *accelerated away*, so the signal arrives Doppler-shifted. This is pure special-relativistic kinematics in an accelerated frame ([[Special Relativity XVI — Accelerated Observers|XVI]]), and it gives a definite, nonzero shift $\Delta t = \Delta t'/(1 + \gamma x_{\mathrm{em}}/c^2)$. By the equivalence principle the *same* shift must occur in the gravitational field. So the redshift is forced by accelerated-frame kinematics, which the reader already trusts.

Second, *why does the static metric forbid this?* Suppose, for contradiction, that the proper time were given by the Minkowski metric, as it was throughout the preceding chapters. Consider two successive crests of the periodic signal: the first emitted at event $A'$ and received at $A$, the second emitted at $B'$ and received at $B$. Because the field is **static** — nothing about the spacetime changes with time — the entire history of the second crest is just the history of the first crest *translated forward in time* by the emission period. The worldline $A' \to A$ and the worldline $B' \to B$ are time-translates of one another. Now, the Minkowski metric is itself time-translation invariant — $\eta_{\mu\nu}$ is the same constant array at every event — so it must assign the *same* length to a curve and its time-translate. The proper-time interval along the emitter's worldline between $A'$ and $B'$ equals that along the receiver's worldline between $A$ and $B$: in symbols $\Delta t = \Delta t'$. But that contradicts the redshift, which says $\Delta t \neq \Delta t'$. Something assumed is false, and the only thing assumed was that proper time is Minkowskian.

**The contradiction is between a measurement that the field is asymmetric (clocks run at different rates) and a metric that is symmetric (translation-invariant) — a static field with a redshift cannot be measured by a translation-invariant metric.** The escape is to let the metric *depend on position*: a metric $g_{\mu\nu}(x)$ that is larger at high altitude than at low altitude can assign different proper times to the two heights while still being static (time-independent), and so accommodate the redshift. The price is that the metric is no longer the constant $\eta$ — it is a field, and that field is gravity.

The argument's robustness deserves emphasis. It never used the *shape* of the light rays' worldlines — they need not be straight, they need not be anything in particular. It used only that the field is static (so crest 2 is crest 1 translated) and that $\eta$ is translation-invariant (so it can't tell them apart). A conclusion that depends only on symmetry, not on dynamical detail, is exactly the kind that cannot be evaded by adjusting a theory.

---

# What Makes This Hard

The hard step is not any calculation — the redshift formula is imported and the rest is one symmetry observation — but seeing that the *static* nature of the field is what does the work, and that the conclusion is therefore independent of the photons' trajectories. The common error is to think the argument is about how light propagates (and to get tangled in the curved photon paths of the accelerated frame), when in fact it is about the time-translation symmetry of successive signals; the photon worldlines can be left completely unspecified. A second subtlety is the direction of the inequality and the sign conventions (whether high-to-low is red or blue shift), which is easy to flip; the physical anchor is that a signal climbing *out* of a potential well loses energy, hence is redshifted.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:**
Use the equivalence principle to import the accelerated-frame redshift, giving $\Delta t \neq \Delta t'$ between two altitudes. Then assume, for contradiction, that proper time is Minkowskian; use the static (time-translation) symmetry of the field to argue that successive signals are time-translates, so a translation-invariant metric must give them equal lengths, $\Delta t = \Delta t'$. The contradiction forces the metric to be position-dependent.

**Subgoal decomposition:**

1. **Import the redshift.** By the equivalence principle, replace the field by an acceleration $\vec a = (\gamma/c^2)\vec e_x$ and quote the accelerated-frame period relation.
   - *Hint:* This is the spectral-shift result of [[Special Relativity XVI — Accelerated Observers|XVI]]; the answer is $\Delta t = \Delta t'/(1+\gamma x_{\mathrm{em}}/c^2)$.
   - *Why needed:* It establishes the measured inequality $\Delta t \neq \Delta t'$ that the symmetry argument will contradict.

2. **Set up the two successive signals.** Label the emission/reception events of two crests $A', A$ and $B', B$.
   - *Hint:* The signal is periodic; crest 2 follows crest 1 by the emission period.
   - *Why needed:* It is the configuration on which time-translation acts.

3. **Use staticity: crest 2 is crest 1 translated in time.** Because the field is static, the worldline $B' \to B$ is the time-translate of $A' \to A$.
   - *Hint:* "Static" means nothing in the spacetime depends on $t$, so any process repeats identically when shifted in time.
   - *Why needed:* It is the symmetry the flat metric must respect.

4. **Apply translation-invariance of $\eta$ and reach the contradiction.** A time-translation-invariant metric assigns equal proper times to a curve and its translate, so the Minkowski assumption gives $\Delta t = \Delta t'$, contradicting step 1.
   - *Hint:* $\eta_{\mu\nu}$ is the same constant array everywhere, hence invariant under $t \to t + $ const.
   - *Why needed:* The contradiction is the theorem; the only false assumption is that proper time is Minkowskian.

---

# Lemma Decomposition

> [!note]- Lemma 1: The accelerated-frame (hence gravitational) redshift
> **Statement:** Two observers $\mathcal{O}$, $\mathcal{O}'$ at rest at altitudes $0$ and $x_{\mathrm{em}}$ in a uniform field $\vec g = -\gamma\vec e_x$ measure periods related by $\Delta t = \Delta t'/(1+\gamma x_{\mathrm{em}}/c^2)$.
>
> **Hint:** By the equivalence principle they are uniformly accelerated observers with $\vec a = (\gamma/c^2)\vec e_x$; quote the accelerated-frame period relation.
>
> **Why needed:** It supplies the inequality $\Delta t \neq \Delta t'$ that the staticity argument contradicts under the Minkowski assumption.
>
> > [!note]- Full proof
> > By the equivalence principle, the situation of two observers at rest in the uniform field $\vec g = -\gamma\vec e_x$ is physically identical to two uniformly accelerated observers in flat spacetime with four-acceleration $\vec a = (\gamma/c^2)\vec e_x$ (the Newtonian-limit identification of field strength with proper acceleration). For uniformly accelerated observers the relation between the proper period $\Delta t'$ of a signal emitted at the abscissa $x_{\mathrm{em}}$ and the proper period $\Delta t$ at which it is received at the origin is, from the accelerated-observer kinematics of [[Special Relativity XVI — Accelerated Observers|XVI]] (the spectral shift between Rindler observers),
> > $$\Delta t = \frac{\Delta t'}{1 + a\,x_{\mathrm{em}}} = \frac{\Delta t'}{1 + \gamma x_{\mathrm{em}}/c^2}.$$
> > For $x_{\mathrm{em}} > 0$ this gives $\Delta t < \Delta t'$ (a blueshift downward, equivalently a redshift for a signal sent upward). A nonvanishing field $\gamma \neq 0$ makes $\Delta t \neq \Delta t'$. $\blacksquare$

> [!note]- Lemma 2: In a static field, successive signals are time-translates
> **Statement:** If the gravitational field is static, the worldline of the second signal crest ($B' \to B$) is the image of the first ($A' \to A$) under a time translation $t \mapsto t + \Delta t_{\mathrm{em}}$.
>
> **Hint:** "Static" means the spacetime geometry and the field are independent of $t$; a process repeated after a delay traces a time-translated history.
>
> **Why needed:** It is the symmetry that a translation-invariant metric must respect, generating the equality that contradicts Lemma 1.
>
> > [!note]- Full proof
> > A static field is one in which nothing depends on the time coordinate $t$: the gravitational potential $\Phi(\vec r)$, the positions of the source and the two observers, and the propagation conditions for light are all independent of $t$. The first signal crest is emitted by $\mathcal{O}'$ at event $A'$ and received by $\mathcal{O}$ at event $A$, tracing some worldline $A' \to A$. The second crest is emitted one emission-period later, at $B' = A' + \Delta t_{\mathrm{em}}\,\vec e_t$. Because every condition governing propagation is time-independent, the second crest experiences an identical history shifted forward by $\Delta t_{\mathrm{em}}$: its worldline is exactly $A' \to A$ translated by $\Delta t_{\mathrm{em}}\vec e_t$, and it is received at $B = A + \Delta t_{\mathrm{em}}\vec e_t$. Thus $B' \to B$ is the time-translate of $A' \to A$, and the emitter's segment $A'B'$ and the receiver's segment $AB$ are both translations by $\Delta t_{\mathrm{em}}\vec e_t$ of the respective emission/reception events. $\blacksquare$

> [!note]- Lemma 3: Translation-invariance of $\eta$ forces equal periods, contradicting the redshift
> **Statement:** If proper time is measured by the Minkowski metric, then the receiver's period equals the emitter's, $\Delta t = \Delta t'$ — contradicting Lemma 1.
>
> **Hint:** $\eta_{\mu\nu}$ is the same constant array everywhere, so it is invariant under time translation and assigns equal lengths to a segment and its translate.
>
> **Why needed:** It is the contradiction; the only assumption that can be false is that proper time is Minkowskian.
>
> > [!note]- Full proof
> > Suppose proper time along worldlines is given by the Minkowski metric $\eta_{\mu\nu} = \mathrm{diag}(1,-1,-1,-1)$, as assumed throughout [[Special Relativity III — Minkowski Spacetime and the Metric|the preceding chapters]]. The proper period the emitter $\mathcal{O}'$ measures between crests is the Minkowski length of the segment of its worldline from $A'$ to $B'$; call it $c\,\Delta t'$. The proper period the receiver $\mathcal{O}$ measures is the Minkowski length from $A$ to $B$; call it $c\,\Delta t$. By Lemma 2, the segment $AB$ is the time-translate of the segment $A'B'$ shifted to the receiver's location — and more directly, both the emitter's and the receiver's worldlines are at-rest (vertical) segments of equal coordinate duration $\Delta t_{\mathrm{em}}$, because in a static field both observers sit at fixed spatial positions. Since $\eta_{\mu\nu}$ is constant — manifestly invariant under the time translation $t \mapsto t + \Delta t_{\mathrm{em}}$ — the Minkowski length of a vertical segment depends only on its coordinate duration, not on where it sits. Both segments have coordinate duration $\Delta t_{\mathrm{em}}$ in their respective worldlines, and the time-translation relating the two crests preserves Minkowski length, so the two proper periods are equal:
> > $$c\,\Delta t = c\,\Delta t' \quad\Longrightarrow\quad \Delta t = \Delta t'.$$
> > This contradicts Lemma 1, which gave $\Delta t = \Delta t'/(1+\gamma x_{\mathrm{em}}/c^2) \neq \Delta t'$. The contradiction shows the supposition is false: proper time cannot be given by the Minkowski metric. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 1 (redshift, Lemma 1).** Two observers $\mathcal{O}$ and $\mathcal{O}'$ are mutually at rest at altitudes $0$ and $x_{\mathrm{em}}$ in a uniform gravitational field $\vec g = -\gamma\vec e_x$, $\gamma > 0$. By the equivalence principle this is physically identical to two uniformly accelerated observers in flat spacetime with proper acceleration $a = \gamma/c^2$. The accelerated-frame relation between the emitted and received periods of a periodic signal ([[Special Relativity XVI — Accelerated Observers|XVI]]) is
> $$\Delta t = \frac{\Delta t'}{1 + \gamma x_{\mathrm{em}}/c^2},$$
> so $\Delta t \neq \Delta t'$ whenever $\gamma \neq 0$. This is the **gravitational redshift** ([[Thm - Gravitational Redshift]]).
>
> **Step 2 (staticity, Lemma 2).** Assume the field is static: nothing depends on $t$. The first signal crest, emitted at $A'$ and received at $A$, and the second crest, emitted at $B' = A' + \Delta t_{\mathrm{em}}\vec e_t$ and received at $B = A + \Delta t_{\mathrm{em}}\vec e_t$, trace worldlines related by the time translation $t \mapsto t + \Delta t_{\mathrm{em}}$. Both observers remain at fixed spatial positions, so each measures the period as the length of a vertical (at-rest) worldline segment of coordinate duration $\Delta t_{\mathrm{em}}$.
>
> **Step 3 (contradiction, Lemma 3).** Suppose proper time is measured by the Minkowski metric $\eta_{\mu\nu}$. Then each period is the Minkowski length of a vertical segment: $c\Delta t'$ for the emitter, $c\Delta t$ for the receiver. Since $\eta_{\mu\nu}$ is constant and hence invariant under time translation, the Minkowski length of a vertical segment depends only on its coordinate duration, which is $\Delta t_{\mathrm{em}}$ for both. Therefore $c\Delta t = c\Delta t'$, i.e. $\Delta t = \Delta t'$ — contradicting Step 1.
>
> **Step 4 (conclusion).** The contradiction shows that in a static gravitational field obeying the equivalence principle, proper time cannot be given by the Minkowski metric. The resolution is to let the metric depend on position: a static but position-dependent metric $g_{\mu\nu}(\vec r)$ assigns different proper times to vertical segments at different altitudes, accommodating the redshift while remaining time-independent. Since the equivalence principle is experimentally ironclad and applies to *any* theory of gravity, every relativistic theory of gravity must replace $\eta_{\mu\nu}$ by such a field $g_{\mu\nu}(x)$. That theory is general relativity. Note the argument never used the shape of the photons' worldlines — only the static symmetry and the translation-invariance of $\eta$ — so it cannot be evaded by any choice of light-propagation dynamics. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Thermodynamics — a redshift argument forbidding a gravitational perpetual-motion machine.** Einstein's original 1911 reasoning was thermodynamic: if a photon climbing out of a potential well did *not* lose energy, one could build a perpetual-motion machine by converting mass to a photon low down, sending it up, and reconverting it to a (heavier) mass high up. Demanding energy conservation forces the redshift $\Delta\nu/\nu = -\Delta\Phi/c^2$. The application is out-of-distribution because it derives a *kinematic* law of spacetime from the *thermodynamic* prohibition of perpetual motion. See [[Thm - Mass-Energy Equivalence]].

**Condensed matter — analogue gravity and acoustic horizons.** In a flowing fluid, sound waves obey a wave equation with an effective metric $g_{\mu\nu}^{\mathrm{acoustic}}$ built from the flow velocity and sound speed — a position-dependent metric on a flat lab spacetime. When the flow exceeds the sound speed, an "acoustic horizon" forms, the analogue of a black-hole horizon, complete with an analogue redshift. The application is striking because it realises this theorem's lesson — that a position-dependent metric encodes "gravity" — in a system with no gravity at all, only a moving fluid.

**Geodesy and metrology — the relativistic definition of height.** Because clocks tick faster at higher gravitational potential, a network of atomic clocks can measure potential differences directly: comparing clock rates *defines* height to centimetre precision (chronometric levelling). The application inverts the theorem — instead of using a known field to predict a redshift, one measures the redshift to map the field — and is now an operational tool in precision geodesy. See [[Thm - Gravitational Redshift]].

---

# Bridges

- **[[Thm - Gravitational Redshift]]** — this theorem *uses* the redshift as its first premise and then weaponises it: the redshift establishes the proper-time inequality $\Delta t \neq \Delta t'$, and the staticity argument shows the flat metric cannot produce it. The redshift theorem derives the effect; this theorem draws the structural conclusion that the metric must therefore be a field.

- **[[Def - Minkowski Space and the Metric]]** — this theorem is precisely the negation of the central assumption of [[Special Relativity III — Minkowski Spacetime and the Metric|Special Relativity III]], that proper time is measured by the constant metric $\eta_{\mu\nu}$. It identifies the exact point at which the affine-space-plus-fixed-metric picture breaks: as soon as gravity (hence the equivalence principle) is present, the constant $\eta$ must become a variable $g_{\mu\nu}(x)$. Minkowski space survives only as the tangent-space approximation at each event.

- **[[Def - Uniformly Accelerated Observer (Hyperbolic Motion)]]** and **[[Def - Rindler Coordinates and the Accelerated Frame]]** — the engine of the redshift is the kinematics of accelerated observers from [[Special Relativity XVI — Accelerated Observers|XVI]]. The equivalence principle *is* the statement that an observer at rest in a uniform field behaves exactly like a uniformly accelerated (hyperbolic-motion) observer, so the Rindler-frame spectral shift transfers directly to the gravitational redshift. The accelerated frame is where the redshift can be computed without any theory of gravity at all.

- **General relativity — the theory this theorem necessitates** — the conclusion "$\eta$ must become $g_{\mu\nu}(x)$" *is* the founding step of general relativity. The variable metric is the dynamical field, sourced by energy-momentum through the Einstein equation; freely-falling bodies follow its geodesics; and the obstruction to removing it globally is the curvature. The vault's [[General Relativity I — Einstein's Equations and Schwarzschild]] is the destination, and [[Def - Semi-Riemannian Metric and Signature]] is the geometric definition of the variable metric this theorem forces into existence.

---

# Unlocked by This

> [!tip] The Curved Metric of General Relativity — from η to g(x) to Curvature *(from General Relativity)*
> This theorem is the hinge of the entire special-relativity-to-general-relativity transition, and it is worth following the whole arc it opens, from the flat metric of [[Def - Minkowski Space and the Metric|Special Relativity III]] through the equivalence principle to the curved metric of general relativity.
>
> The starting point is the metric $\eta_{\mu\nu} = \mathrm{diag}(+1,-1,-1,-1)$ — the single fixed, constant, indefinite bilinear form on which every previous chapter was built. It is a *background*: the same array at every event, unaffected by anything, not itself a physical variable. The Lorentz group is its global symmetry; a Lorentz transformation is a global linear isometry relating the inertial frames of two distant observers.
>
> The equivalence principle breaks this picture in one stroke. Because all bodies fall the same way (the equality of inertial and gravitational mass), a uniform gravitational field is locally indistinguishable from a uniformly accelerated frame — and this theorem shows that this local indistinguishability, applied to a static field, *forbids* the metric from being the constant $\eta$. The gravitational redshift, an inevitable consequence of the equivalence principle and the accelerated-frame kinematics of [[Special Relativity XVI — Accelerated Observers|Special Relativity XVI]], cannot be carried by a translation-invariant metric. The only escape is to let the metric vary from point to point: $\eta_{\mu\nu}$ becomes a **field** $g_{\mu\nu}(x)$, a different symmetric bilinear form at each event, larger high in a potential well than low in it, so that clocks at different altitudes genuinely run at different rates.
>
> Promoting the metric to a field reorganises the whole of spacetime geometry. Spacetime is no longer the affine space $\mathbb{R}^4$ but a **differentiable manifold** $\mathscr{E}$; there is no longer one vector space of displacements but a separate **tangent space** $E_A$ at each event $A$, with $E_A \neq E_B$ for $A \neq B$. The metric $g$ is a tensor field assigning to each tangent space a bilinear form $g(A)$ of signature $(+,-,-,-)$ — the [[Def - Semi-Riemannian Metric and Signature|semi-Riemannian (Lorentzian) metric]] of differential geometry. There is in general no global inertial coordinate system; one cannot make $g_{\mu\nu} = \eta_{\mu\nu}$ everywhere at once.
>
> But the equivalence principle leaves a precise residue of special relativity: at *any one* event one can choose coordinates — the frame of a freely-falling observer, a **locally inertial frame** — in which $g_{\mu\nu}$ equals $\eta_{\mu\nu}$ and its first derivatives vanish. So special relativity holds *exactly* at each event, in the tangent space, and approximately in a small neighbourhood. The relation is exactly that of a curved surface to its tangent plane: at each point of the surface there is a flat tangent plane matching it to first order, and at each event of curved spacetime there is a flat Minkowski tangent space, carrying $\eta_{\mu\nu}$, that the curved metric reduces to. **Minkowski space is the universal local model of every spacetime** — which is why all of special relativity remains valid, locally, forever.
>
> What cannot be removed by going to a locally inertial frame are the *second* derivatives of $g_{\mu\nu}$. Their irreducible part is the **curvature**, encoded in the Riemann tensor, and curvature is the true, frame-independent gravitational field. Operationally it is the **tidal field**: two freely-falling particles released side by side in a real (inhomogeneous) field accelerate toward each other (geodesic deviation), an effect no single acceleration can mimic and no choice of frame can remove. In Minkowski space, where geodesics are straight lines of the affine space, initially-parallel geodesics stay parallel — curvature vanishes — so there is no gravity; this is the precise sense in which special relativity is the *flat, zero-curvature* chapter of Lorentzian geometry. Freely-falling bodies follow **geodesics** of $g$ (timelike for massive particles, null for photons), generalising the inertial straight worldlines of special relativity.
>
> Finally the metric becomes *dynamical*. It is no longer a fixed background but a physical field with its own equation of motion, sourced by energy and momentum: the **Einstein equation**
> $$R_{\mu\nu} - \tfrac12 R\,g_{\mu\nu} = \frac{8\pi G}{c^4}\,T_{\mu\nu},$$
> relating the Ricci curvature to the energy-momentum tensor. At the Newtonian limit one component reduces to Poisson's equation $\Delta\Phi = 4\pi G\rho$ and the other nine to identities; in the weak field $g = \eta + h$ the linearised equation is exactly the Fierz-Pauli equation of the [[Def - Vector and Tensor Theories of Gravity|tensor theory]] of §25.1. The full theory — its Schwarzschild solution, its black holes, its cosmology — is developed in the vault's [[General Relativity I — Einstein's Equations and Schwarzschild]].
>
> So the single idea this theorem seeds is the promotion of the metric from a fixed background $\eta_{\mu\nu}$ to a dynamical field $g_{\mu\nu}(x)$, and gravitation is precisely the deviation of that field from the flat $\eta$. The indefinite signature $(+,-,-,-)$ fixed back in [[Def - Minkowski Space and the Metric|Special Relativity III]] is carried over unchanged — $g_{\mu\nu}(x)$ has signature $(+,-,-,-)$ everywhere — which is the exact sense in which gravity never disturbs the *local* structure of time and space, only their global fitting-together. Special relativity is the theory of the flat metric; general relativity is the theory of the metric allowed to bend; and this theorem is the proof that the bending is not optional.
