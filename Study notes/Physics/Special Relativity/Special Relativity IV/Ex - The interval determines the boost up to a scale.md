---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Thm - Invariance of the Spacetime Interval"
  - "Def - The Lorentz Group"
  - "Def - The Spacetime Interval"
tags: [physics, special-relativity]
---

# Problem Statement

Work in $1+1$ dimensions with $c = 1$, coordinates $(t, x)$, interval $\Delta s^2 = \Delta t^2 - \Delta x^2$.

1. Suppose a linear map $\Lambda$ of the $(t,x)$-plane carries every light ray to a light ray — that is, it preserves the *light cone* $\{\Delta s^2 = 0\}$, i.e. the two lines $t = \pm x$. Show that $\Lambda$ must scale the interval by a single factor: $\Delta s'^2 = \kappa\,\Delta s^2$ for some constant $\kappa$ depending on $\Lambda$ (not on the event).
2. Now impose the **principle of relativity**: the map from frame $S$ to $S'$ and its inverse from $S'$ to $S$ are physically equivalent, so $\kappa(v)\kappa(-v) = 1$, and $\kappa$ depends only on the *magnitude* of the relative velocity, so $\kappa(v) = \kappa(-v)$. Deduce $\kappa = 1$, hence $\Lambda$ preserves the interval exactly and is a [[Def - The Lorentz Group|Lorentz transformation]].
3. Identify the larger group obtained if one drops the relativity-principle constraint and keeps only "preserves the light cone". What is the extra one-parameter family of maps, and why are they excluded from physics?

**Recall:**

![[Thm - Invariance of the Spacetime Interval#Statement]]

The light cone through the origin is the set of [[Def - Classification of Four-Vectors|null]] vectors, $\{(t,x) : t^2 - x^2 = 0\} = \{t = x\} \cup \{t = -x\}$. A [[Def - The Lorentz Group|Lorentz transformation]] satisfies $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$ with $\eta = \mathrm{diag}(1,-1)$; a *conformal* (light-cone-preserving) map satisfies the weaker $\Lambda^{\mathsf T}\eta\,\Lambda = \kappa\,\eta$ for some scalar $\kappa > 0$.

---

# Convergent Strategy

**Problem class.** An *establish-the-characterisation* problem: derive the [[Def - The Lorentz Group|Lorentz group]] from a weaker geometric hypothesis (light-cone preservation) plus a physical symmetry (relativity). It is the converse half of the [[Thm - Invariance of the Spacetime Interval|interval-invariance theorem]] made into a constructive derivation, and it is exactly the argument used in that theorem's "Why Is It True".

**Assumption pattern.** Two hypotheses, used in sequence. First, "preserves the light cone" — a *linear* map fixing the zero set of a quadratic form. The standard fact that two quadratic forms (in two variables) with the same zero locus are proportional turns this into "$\Lambda$ scales the form by $\kappa$". Second, the relativity principle, supplying the two constraints $\kappa(v)\kappa(-v) = 1$ and $\kappa(v) = \kappa(-v)$, which pin $\kappa = 1$.

**Theorem routing.** Step 1 is the proportionality-of-quadratic-forms lemma applied to $\Delta s^2$ and its image; Step 2 is the algebra $\kappa^2 = 1$, $\kappa > 0 \Rightarrow \kappa = 1$; Step 3 names the conformal group $\{\kappa\Lambda\}$. The route converts a geometric condition (cone) into an algebraic one ($\Lambda^{\mathsf T}\eta\Lambda = \kappa\eta$) and then uses physics to fix the residual scalar.

**Key decision point.** The crux is recognising that "preserves the light cone" is *strictly weaker* than "preserves the interval" — it leaves a one-parameter scaling ambiguity $\kappa$ — and that the relativity principle, not any further geometry, is what removes it. A reader who assumes the cone determines the metric outright skips the $\kappa$ and misses the role of relativity entirely.

---

# Legal Operations Used

1. **Classify by the sign of the norm / use the light cone (operation 9 from the topic page).** The hypothesis is phrased through the null set $\Delta s^2 = 0$, the light cone, and the whole derivation tracks what a linear map can do to it.

2. **Compute an invariant in the convenient frame (operation 7 from the topic page).** The constancy of $c$ — that light rays go to light rays — is the invariant that the argument leverages to constrain $\Lambda$.

3. **Use the relativity principle's left–right symmetry.** The two conditions on $\kappa$ come from the first postulate: the relation between $S$ and $S'$ is symmetric, and nothing distinguishes $+v$ from $-v$ except the sign of the velocity.

---

# Hints

> [!note]- Hint 1
> A linear change of variables sends the quadratic form $\Delta s^2 = \Delta t^2 - \Delta x^2$ to another quadratic form $Q(\Delta t, \Delta x)$. If $Q$ vanishes exactly where $\Delta s^2$ vanishes (the same two lines $t = \pm x$), what is the relationship between $Q$ and $\Delta s^2$?

> [!note]- Hint 2
> Two quadratic forms in two variables with the same zero locus (a pair of lines) are scalar multiples of each other. So $\Delta s'^2 = \Lambda^{\mathsf T}$-image $= \kappa\,\Delta s^2$ for a single constant $\kappa$. The factor cannot depend on the event because $\Lambda$ is linear.

> [!note]- Hint 3
> Apply the boost from $S$ to $S'$ (factor $\kappa(v)$), then the inverse boost back (factor $\kappa(-v)$). The composite is the identity, so $\kappa(v)\kappa(-v) = 1$. By the relativity principle nothing depends on the sign of $v$, so $\kappa(v) = \kappa(-v)$. Combine.

> [!note]- Hint 4
> From $\kappa(v)\kappa(-v) = 1$ and $\kappa(v) = \kappa(-v)$ you get $\kappa^2 = 1$. Which root is physical? At $v = 0$ the map is the identity, so $\kappa(0) = 1$; by continuity $\kappa$ cannot jump to $-1$.

---

# Solution

The derivation has two movements. Step 1 shows that preserving the light cone forces $\Lambda$ to rescale the interval by a single constant $\kappa$ — geometry alone gets you this far but no further. Step 2 brings in the relativity principle, whose two symmetry constraints force $\kappa = 1$, upgrading "preserves the cone" to "preserves the interval", i.e. Lorentz. Step 3 names the gap: without relativity you get the conformal group, larger by exactly the scalings, which are excluded because they change rest masses.

**Step 1: light-cone preservation forces $\Delta s'^2 = \kappa\,\Delta s^2$.**

> [!note]- Derivation
> Let $\Lambda$ be linear and suppose it carries the light cone to itself: $\Delta s^2 = 0 \iff \Delta s'^2 = 0$, where $\Delta s'^2 = (\Lambda\,\Delta X)^{\mathsf T}\eta\,(\Lambda\,\Delta X) = \Delta X^{\mathsf T}(\Lambda^{\mathsf T}\eta\,\Lambda)\Delta X =: Q(\Delta X)$ is the image quadratic form. Both $\Delta s^2 = \Delta t^2 - \Delta x^2$ and $Q$ are quadratic forms in the two variables $(\Delta t, \Delta x)$, and by hypothesis they have the *same* zero set: the pair of lines $\Delta t = \pm\Delta x$.
>
> A quadratic form in two variables factors over $\mathbb{R}$ when its zero set is a pair of real lines: $\Delta s^2 = (\Delta t - \Delta x)(\Delta t + \Delta x)$. Any other quadratic form vanishing on those same two lines must have the same two linear factors up to scalars, hence must be $Q = \kappa\,(\Delta t - \Delta x)(\Delta t + \Delta x) = \kappa\,\Delta s^2$ for a single constant $\kappa$. (Concretely: $Q = a\,\Delta t^2 + 2b\,\Delta t\Delta x + c\,\Delta x^2$; vanishing on $\Delta t = \Delta x$ gives $a + 2b + c = 0$ and on $\Delta t = -\Delta x$ gives $a - 2b + c = 0$, so $b = 0$ and $a = -c$, i.e. $Q = a(\Delta t^2 - \Delta x^2) = a\,\Delta s^2$ with $\kappa = a$.) Since $\Lambda$ is linear, $\kappa$ is a constant independent of the event. Equivalently $\Lambda^{\mathsf T}\eta\,\Lambda = \kappa\,\eta$.

**Step 2: the relativity principle forces $\kappa = 1$.**

> [!note]- Derivation
> Let $\kappa(v)$ be the scale factor of the boost taking $S$ to $S'$, where $S'$ moves at velocity $v$. The inverse boost, from $S'$ back to $S$, takes velocity $-v$ and has scale factor $\kappa(-v)$. Composing the two returns to $S$, the identity, whose scale factor is $1$:
> $$\kappa(v)\,\kappa(-v) = 1.$$
> By the **principle of relativity**, the two frames are equivalent and no direction is preferred, so the scale factor can depend only on the *speed* $|v|$, not on the sign of $v$:
> $$\kappa(v) = \kappa(-v).$$
> Substituting, $\kappa(v)^2 = 1$, so $\kappa(v) = \pm 1$. At $v = 0$ the transformation is the identity with $\kappa(0) = 1$, and $\kappa$ is continuous in $v$ (the boost depends continuously on $v$), so $\kappa$ cannot jump to $-1$: $\kappa(v) = +1$ for all $v$.
>
> Hence $\Lambda^{\mathsf T}\eta\,\Lambda = \eta$ exactly, which is the defining condition of a [[Def - The Lorentz Group|Lorentz transformation]]. The interval is preserved, not merely the cone.

**Step 3: the conformal group, and why scalings are excluded.**

> [!note]- Derivation
> Dropping the relativity principle and keeping only "preserves the light cone" leaves the larger set $\{\Lambda : \Lambda^{\mathsf T}\eta\,\Lambda = \kappa\,\eta,\ \kappa > 0\}$. This is the **conformal group** of the $(t,x)$-plane (its linear part): every such $\Lambda$ is a Lorentz transformation composed with a *dilation* $x \mapsto \lambda x$, $t \mapsto \lambda t$ (which has $\kappa = \lambda^2$). The extra one-parameter family is exactly the dilations, the uniform rescalings of all of spacetime.
>
> These are excluded from physics because a dilation changes the [[Thm - Invariance of the Spacetime Interval|interval]] of every pair of events by the factor $\lambda$, and hence changes every proper time, every rest mass ($m = \|P\|$), and every physical length. The principle of relativity forbids this: two inertial observers must agree on a particle's rest mass and on proper times along worldlines, which is precisely the statement $\kappa = 1$. Light-cone preservation is the *causal* structure (who can signal whom); the full interval is the *metric* structure (how much proper time elapses), and physics requires the metric, not merely the causal cone. The relativity principle is what promotes a causal symmetry to a metric one.

> [!note]- Complete formal solution
> Let $\Lambda$ be a linear map of the $(t,x)$-plane preserving the light cone $\{t = \pm x\}$. The image of $\Delta s^2 = \Delta t^2 - \Delta x^2 = (\Delta t - \Delta x)(\Delta t + \Delta x)$ under $\Lambda$ is a quadratic form $Q = \Delta X^{\mathsf T}(\Lambda^{\mathsf T}\eta\Lambda)\Delta X$ with the same zero set; writing $Q = a\Delta t^2 + 2b\Delta t\Delta x + c\Delta x^2$ and imposing vanishing on $\Delta t = \pm\Delta x$ gives $b = 0$, $a = -c$, so $Q = \kappa\,\Delta s^2$, i.e. $\Lambda^{\mathsf T}\eta\Lambda = \kappa\eta$ for a constant $\kappa$. The principle of relativity gives $\kappa(v)\kappa(-v) = 1$ (the boost and its inverse compose to the identity) and $\kappa(v) = \kappa(-v)$ ($\kappa$ depends only on speed), whence $\kappa^2 = 1$; continuity from $\kappa(0) = 1$ forces $\kappa = +1$. Thus $\Lambda^{\mathsf T}\eta\Lambda = \eta$ and $\Lambda$ is Lorentz. Without the relativity principle one obtains the larger conformal group $\{\kappa\Lambda : \kappa > 0\}$, whose extra elements are dilations $x \mapsto \lambda x$, $t \mapsto \lambda t$; these are excluded because they rescale every interval, proper time and rest mass, violating the agreement between inertial observers. $\blacksquare$

> [!warning] Illegal but tempting alternative route
> It is tempting to conclude from "preserves the light cone" that $\Lambda$ preserves the interval *directly*, skipping the scale factor $\kappa$. This is wrong: the cone determines the quadratic form only *up to a positive multiple*, and the dilations show the multiple is genuinely free until the relativity principle removes it. Forgetting $\kappa$ amounts to silently assuming the conclusion. The whole subtlety — and the reason the relativity principle is logically necessary, not just light-constancy — lives in that one scalar.

---

# Key Takeaways

**Preserving a quadratic form's zero set determines the form only up to scale.** The reusable fact is that a linear map fixing the *null cone* of a quadratic form rescales the form by a constant rather than preserving it — the cone is the conformal data, not the metric data. This is why "the speed of light is the same for everyone" (a statement about the null cone) is *weaker* than "the interval is invariant" (a statement about the metric), and why the second does not follow from the first without an extra input. The trigger for this pattern is any hypothesis phrased as "carries [the zero set] to [the zero set]": expect a residual scalar, and look for the physical principle that fixes it. The same structure appears in conformal field theory, where preserving the causal/null structure leaves the full conformal group and only additional dynamics select a metric.

**The relativity principle is what upgrades causal symmetry to metric symmetry.** The deep point of the exercise is that the constancy of light alone gives the *conformal* group; it is the principle of relativity — the equivalence of frames and the indifference to the sign of velocity — that cuts the conformal group down to the Lorentz group by forcing $\kappa = 1$. Both postulates are needed, and they do different jobs: light-constancy fixes the *shape* of the invariant (its null cone is the light cone), relativity fixes its *scale*. Whenever you derive the Lorentz transformation, watch for these two distinct roles; conflating them (or omitting relativity) produces either too large a group (the conformal group) or an unjustified jump.

**Dilations are the physically forbidden symmetry, and rest mass is why.** The concrete content of $\kappa = 1$ is that uniform rescalings of spacetime are not symmetries of physics, because they change rest masses and proper times — quantities all inertial observers must agree on. This is a useful diagnostic in reverse: any proposed "symmetry" that rescales the interval is suspect, because it cannot preserve the invariant mass $m = \|P\|$ of a particle. The exclusion of dilations is the special-relativistic statement that there is an absolute scale of mass and time, set by the metric; only in a theory with no massive particles and no intrinsic length (a conformal field theory) is the dilation symmetry restored.
