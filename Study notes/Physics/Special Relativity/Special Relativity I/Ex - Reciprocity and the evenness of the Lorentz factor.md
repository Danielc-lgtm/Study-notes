---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - The Lorentz Transformation"
  - "Def - Inertial Frame and the Postulates of Special Relativity"
  - "Thm - Uniqueness of the Lorentz Transformation from the Postulates"
tags: [physics, special-relativity]
---

# Problem Statement

In deriving the Lorentz transformation one reaches the spatial relation $x' = \gamma_v(x - vt)$, where the scale factor $\gamma_v$ may in principle depend on the relative velocity $v$. Before the constancy of light is used, $\gamma_v$ is still an unknown function. This exercise establishes the structural constraint $\gamma_v = \gamma_{-v}$ — that $\gamma$ is an *even* function of $v$ — using only the [[Def - Inertial Frame and the Postulates of Special Relativity|principle of relativity]] and the isotropy of space, *without* invoking the second postulate.

1. **The isotropy argument.** Explain why $\gamma_v$ can depend on the velocity only through $v^2 = \mathbf{v}\cdot\mathbf{v}$, and conclude $\gamma_v = \gamma_{-v}$.
2. **The reciprocity argument (independent).** Consider mirror-image frames $\tilde S$, $\tilde S'$ obtained from $S$, $S'$ by measuring the $x$-coordinate in the opposite direction: $\tilde x = -x$, $\tilde x' = -x'$ (with $\tilde t = t$, $\tilde t' = t'$). Show that $\tilde S$ moves at velocity $-v$ relative to $\tilde S'$, derive the transformation in the tilde frames, and compare with the original to force $\gamma_v = \gamma_{-v}$.
3. **The discarded root.** The comparison in part 2 admits, formally, a sign ambiguity $\kappa = \pm 1$. Identify the spurious root $\kappa = -1$, and explain — using the requirement that the transformation reduce to the identity at $v = 0$ — why it must be discarded.
4. **Why it matters.** Show that without evenness, the forward transformation $x' = \gamma_v(x - vt)$ and the inverse $x = \gamma_{-v}(x' + vt')$ would carry *different* scale factors, and explain why this would violate the principle of relativity.

**Recall:**

A frame is **inertial** if free particles move in straight lines; the **principle of relativity** ([[Def - Inertial Frame and the Postulates of Special Relativity|Postulate 1]]) states that no inertial frame is preferred and the laws take the same form in all of them. **Isotropy** of space means no spatial direction is physically distinguished. The relevant intermediate result of the derivation is:

![[Def - The Lorentz Transformation#The Definition]]

The factor $\gamma_v$ is the [[Def - The Lorentz Transformation|Lorentz factor]]; this exercise shows $\gamma_v = \gamma_{-v}$ *before* its value is determined. The full derivation is [[Thm - Uniqueness of the Lorentz Transformation from the Postulates]], whose Lemma 3 this exercise expands.

---

# Convergent Strategy

**Problem class.** This is a *symmetry-constraint* problem: deduce the functional form of an unknown coefficient from invariance principles alone, before any dynamical or numerical input. The [[Special Relativity I — Postulates and Lorentz Transformations#Problem-Solving Strategy|topic strategy]] notes that "a symmetry is given, and the symmetry alone pins down the form of the answer" — here isotropy and the relativity principle pin down that $\gamma$ is even.

**Assumption pattern.** The assumptions are the principle of relativity (the two frames are interchangeable) and isotropy (no preferred spatial direction). Neither the constancy of light nor any specific value of $\gamma$ is used — that is the point: evenness is a *structural* fact, logically prior to the determination of $\gamma$'s value, and the exercise isolates exactly how much follows from symmetry alone.

**Theorem routing.** The route is two independent arguments converging on the same conclusion: isotropy $\Rightarrow$ $\gamma$ depends only on $v^2$ $\Rightarrow$ even; and reciprocity (the reflected-frame construction) $\Rightarrow$ direct comparison forcing $\gamma_v = \gamma_{-v}$. Both feed [[Thm - Uniqueness of the Lorentz Transformation from the Postulates|Lemma 3]], which is then used to give the forward and inverse boosts a common $\gamma$.

**Key decision point.** The crux is constructing the *right* reflected frames in part 2. The natural-but-wrong instinct is to simply swap $S \leftrightarrow S'$, which gives the inverse transformation but not the evenness directly. The productive move is to reflect the *spatial axis* ($\tilde x = -x$, $\tilde x' = -x'$) while keeping the physical motion the same — this turns "$S'$ moves at $+v$" into "$\tilde S$ moves at $-v$ relative to $\tilde S'$" by pure relabelling, so that the *same* physical setup is described with velocity $-v$, and comparing the two descriptions extracts $\gamma_v = \gamma_{-v}$.

---

# Legal Operations Used

1. **Operation 1 from the topic page (apply the Lorentz transformation / use the inverse via $v \to -v$).** Both arguments hinge on the relationship between the forward map and its inverse, and on the fact that reversing the sense of motion reverses the sign of $v$.

2. **Operation 7 from the topic page (exploit a symmetry to constrain the form).** Isotropy and the relativity principle are deployed as symmetries that the unknown $\gamma_v$ must respect, fixing its parity without any computation of its value.

---

# Hints

> [!note]- Hint 1
> For part 1: a scalar quantity attached to the relationship between two frames, in isotropic space, cannot know about the *direction* of the relative velocity — only its magnitude. Magnitude is $|v|$, equivalently $v^2$. A function of $v^2$ is automatically even.

> [!note]- Hint 2
> For part 2: under $\tilde x = -x$, a particle at $x = vt$ (the $S'$ origin) is at $\tilde x = -vt = (-v)\tilde t$, so in the tilde description the origin moves at velocity $-v$. Apply the *same* derivation that gave $x' = \gamma_v(x - vt)$, but now the relative velocity is $-v$, so you get $\tilde x' = \gamma_{-v}(\tilde x + v\tilde t)$.

> [!note]- Hint 3
> Substitute $\tilde x = -x$, $\tilde x' = -x'$ into $\tilde x' = \gamma_{-v}(\tilde x + v\tilde t)$ and simplify. You should get $x' = \gamma_{-v}(x - vt)$. Compare with $x' = \gamma_v(x - vt)$ from the unreflected derivation.

> [!note]- Hint 4
> For the discarded root: when you match two linear transformations you are really matching $y' = \kappa y$ across a reflection, and $\kappa^2 = 1$ gives $\kappa = \pm 1$. The map must become the identity when $v = 0$ (no relative motion = no change of coordinates); $\kappa = -1$ is a reflection, which is *not* the identity, so it is excluded.

---

# Solution

Evenness of $\gamma$ is forced by symmetry alone, two ways. Isotropy says $\gamma$ can depend only on $v^2$, hence is even (Step 1). Independently, reflecting the spatial axis re-describes the same physics with velocity $-v$, and comparing forces $\gamma_v = \gamma_{-v}$ (Step 2); the spurious reflection root is excluded by continuity to the identity (Step 3). Without evenness the forward and inverse boosts would disagree, breaking the relativity principle (Step 4).

**Step 1: Isotropy forces $\gamma_v = \gamma(v^2)$, hence even.**

> [!note]- Derivation
> The factor $\gamma_v$ is a single real number characterising the change of frame between $S$ and $S'$, which move with relative velocity $\mathbf{v} = (v, 0, 0)$. Space is **isotropic**: no direction is physically preferred. A scalar built from the change-of-frame data therefore cannot depend on the *direction* of $\mathbf{v}$ — if it did, that direction would be physically singled out, contradicting isotropy. The only direction-independent information in $\mathbf{v}$ is its magnitude, equivalently $v^2 = \mathbf{v}\cdot\mathbf{v}$. Hence $\gamma_v = \gamma(v^2)$ for some function of one variable. Since $(-v)^2 = v^2$, immediately $\gamma_{-v} = \gamma((-v)^2) = \gamma(v^2) = \gamma_v$. The factor is even. This argument uses *only* isotropy and makes no reference to light or to the value of $\gamma$.

**Step 2: The reflected-frame (reciprocity) argument gives $\gamma_v = \gamma_{-v}$ independently.**

> [!note]- Derivation
> Define $\tilde S$ and $\tilde S'$ to be the *same physical frames* as $S$ and $S'$, but with the spatial coordinate measured in the opposite direction:
> $$\tilde x = -x, \quad \tilde x' = -x', \quad \tilde t = t, \quad \tilde t' = t'.$$
> First find the relative velocity in the tilde description. The spatial origin of $S'$ is the worldline $x = vt$ in $S$; in tilde coordinates it is $\tilde x = -x = -vt = (-v)\tilde t$. So in the tilde frames, the origin of $\tilde S'$ moves at velocity $-v$ relative to $\tilde S$ — equivalently, $\tilde S$ moves at $-v$ relative to $\tilde S'$. The physical motion is unchanged; only the sign convention flipped.
>
> Now apply the *same* structural derivation that produced $x' = \gamma_v(x - vt)$ — linearity plus the moving-origin condition (see [[Thm - Uniqueness of the Lorentz Transformation from the Postulates|Lemmas 1–2]]) — but in the tilde frames, where the relative velocity is $-v$:
> $$\tilde x' = \gamma_{-v}\,(\tilde x - (-v)\tilde t) = \gamma_{-v}(\tilde x + v\tilde t).$$
> Substitute back $\tilde x = -x$, $\tilde x' = -x'$, $\tilde t = t$:
> $$-x' = \gamma_{-v}(-x + vt) \quad\Longrightarrow\quad x' = \gamma_{-v}(x - vt).$$
> But the unreflected derivation gave $x' = \gamma_v(x - vt)$. The two expressions describe the *same* physical transformation between $S$ and $S'$, so their coefficients of $(x - vt)$ must agree:
> $$\gamma_v = \gamma_{-v}.$$
> This argument uses *only* the principle of relativity (the freedom to relabel axes, with no preferred direction) — again no appeal to light.

**Step 3: The spurious root $\kappa = -1$ is excluded by continuity to the identity.**

> [!note]- Derivation
> When matching two linear transformations across a reflection, one is really solving a relation of the schematic form $\kappa^2 = 1$ (the reflection composed with itself is the identity), with solutions $\kappa = +1$ and $\kappa = -1$. The root $\kappa = +1$ gives the comparison of Step 2, yielding $\gamma_v = \gamma_{-v}$. The root $\kappa = -1$ would correspond to *also* flipping the orientation — composing the change of frame with an extra spatial reflection.
>
> This second root is unphysical for a boost, and the clean way to see it is the *continuity-to-identity* requirement. When the relative velocity vanishes, $v = 0$, the two frames coincide and the transformation between them must be the identity: $x' = x$, $t' = t$. The root $\kappa = +1$ branch does this — at $v = 0$ it gives $x' = \gamma_0\, x$ with $\gamma_0 = 1$, the identity. The root $\kappa = -1$ branch gives $x' = -x$ at $v = 0$, a spatial reflection, which is *not* the identity: it would mean that two frames at rest relative to each other disagree about the direction of the $x$-axis, which is absurd. Since the boost is a continuous family connected to the identity at $v = 0$, only the $\kappa = +1$ branch is admissible. (The same logic discards $\kappa = -1$ in the transverse equation $y' = \kappa y$, fixing $y' = y$ — see [[Thm - Uniqueness of the Lorentz Transformation from the Postulates|Lemma 6]].)

**Step 4: Without evenness the forward and inverse boosts would disagree, violating relativity.**

> [!note]- Derivation
> Suppose, contrary to what we proved, that $\gamma_v \ne \gamma_{-v}$. The forward transformation ($S \to S'$, relative velocity $+v$) would be $x' = \gamma_v(x - vt)$. The inverse transformation ($S' \to S$) describes $S$ moving at $-v$ relative to $S'$, so by the same structural derivation it would be $x = \gamma_{-v}(x' + vt')$ — with the *other* scale factor.
>
> Now the [[Def - Inertial Frame and the Postulates of Special Relativity|principle of relativity]] demands that $S$ and $S'$ be on completely equal footing: neither is preferred. But if $\gamma_v \ne \gamma_{-v}$, then the "stretching" of coordinates in going $S \to S'$ would differ in magnitude from the stretching in going $S' \to S$ — observer $O$ would find $O'$'s rulers scaled by $\gamma_v$, while $O'$ would find $O$'s rulers scaled by the *different* factor $\gamma_{-v}$. This asymmetry would let the two observers determine, by comparing scale factors, which of them is "really" moving — a preferred frame, in flat contradiction with the principle of relativity. Composing the forward and inverse maps would also fail to return the identity. Evenness $\gamma_v = \gamma_{-v}$ is exactly the condition that the forward and inverse transformations are mirror versions of one another with the *same* scale, so that the two frames are genuinely symmetric and composition closes. The relativity principle therefore *requires* $\gamma$ to be even, which is why both arguments above are really the same principle wearing two costumes.

> [!note]- Complete formal solution
> *Isotropy.* $\gamma_v$ is a scalar attached to the change of frame between $S$ and $S'$; isotropy of space forbids dependence on the direction of $\mathbf{v}$, so $\gamma_v = \gamma(v^2)$, which is even: $\gamma_{-v} = \gamma_v$.
> *Reciprocity.* Reflecting the spatial axis ($\tilde x = -x$, $\tilde x' = -x'$) leaves the physics unchanged but re-describes the relative velocity as $-v$ (the $S'$ origin $x = vt$ becomes $\tilde x = (-v)\tilde t$). The structural derivation in the tilde frames gives $\tilde x' = \gamma_{-v}(\tilde x + v\tilde t)$; substituting back yields $x' = \gamma_{-v}(x - vt)$, which compared with $x' = \gamma_v(x - vt)$ forces $\gamma_v = \gamma_{-v}$.
> *Discarded root.* The matching admits $\kappa = \pm 1$; $\kappa = -1$ gives a spatial reflection (not the identity) at $v = 0$ and is excluded by continuity of the boost family to the identity, leaving $\kappa = +1$ and $\gamma_v = \gamma_{-v}$.
> *Necessity.* If $\gamma_v \ne \gamma_{-v}$, the forward map $x' = \gamma_v(x-vt)$ and inverse $x = \gamma_{-v}(x'+vt')$ would carry different scales, letting observers detect a preferred frame and breaking the relativity principle; evenness is precisely the condition for forward/inverse symmetry and closure under composition. $\blacksquare$

---

# Key Takeaways

**Parity and functional form can be fixed by symmetry alone, before any equation of motion or numerical input enters.** The lesson that generalises far beyond relativity is that invariance principles constrain the *form* of unknowns cheaply and powerfully. Here, isotropy alone forces $\gamma$ to be even — a strong constraint extracted with no computation, no light postulate, no value of $\gamma$. This is the same move that fixes the form of correlation functions from rotational invariance, the allowed terms in a Lagrangian from gauge symmetry, or the parity of a wavefunction from a reflection symmetry of the potential. The trigger to deploy it: whenever you have an unknown scalar function of a vector (or of any quantity carrying a direction or a sign), ask which symmetries the setup has and demand the unknown respect them — often this alone determines whether it is even, odd, or constant, collapsing an infinite-dimensional search to a finite one.

**"Reciprocity" is the principle of relativity made into a usable equation, and the reflected-frame trick is how you extract it.** The relativity principle is easy to state ("no preferred frame") and easy to underuse. The reflected-frame construction turns it into arithmetic: by re-describing the *identical* physical situation with the spatial axis flipped, you obtain a second expression for the same transformation, and equating the two extracts a constraint. The general technique — describe one situation two ways using a symmetry, then equate — is among the most reliable in physics, and recognising when "the same setup viewed differently" is available is the skill. The reciprocity relation $\gamma_v = \gamma_{-v}$ is what guarantees the forward and inverse boosts share a single $\gamma$, which is the quantitative heart of "the two frames are equivalent"; every later use of "the inverse is just $v \to -v$" silently rests on this exercise.

**Discarding spurious roots by continuity to the identity is a standard and necessary final step.** Algebraic conditions like $\kappa^2 = 1$ routinely produce extra solutions that are mathematically valid but physically wrong, and the disciplined way to prune them is to demand the right limiting behaviour — here, that the transformation become the identity when the relative velocity vanishes. The reflection root $\kappa = -1$ is a perfectly good *element of the Lorentz group* (it is a spatial reflection), but it is not part of the *connected* family of boosts that includes the identity, and the boost we are deriving is connected to the identity by construction. This distinction — between the full group and its identity component — is exactly the distinction between the [[Def - The Lorentz Group|Lorentz group]] $O(1,3)$ and its proper orthochronous subgroup $SO^+(1,3)$, and it recurs throughout the subject. The transferable habit: after solving a symmetry constraint, always check which root survives the $v \to 0$ (or analogous) limit, and discard the rest as belonging to a different component of the symmetry group.
