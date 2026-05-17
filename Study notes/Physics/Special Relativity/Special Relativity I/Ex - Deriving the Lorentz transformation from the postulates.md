---
type: exercise
subject: special-relativity
difficulty: "⭐⭐"
prereqs:
  - "Def - Inertial Frame and the Postulates of Special Relativity"
  - "Def - The Lorentz Transformation"
tags: [physics, special-relativity]
---

# Problem Statement

Two inertial frames $S$ and $S'$ have coincident origins; $S'$ moves at constant velocity $v$ along the $x$-axis of $S$. Working with $c = 1$ and ignoring the transverse coordinates $y, z$, derive the Lorentz transformation
$$x' = \gamma(x - vt), \qquad t' = \gamma(t - vx), \qquad \gamma = \frac{1}{\sqrt{1-v^2}}$$
**from the two postulates of special relativity alone.** Proceed in four steps:

1. Use the law of inertia to argue the transformation $(t,x)\mapsto(t',x')$ must be **linear**.
2. Use the fact that the origin of $S'$ moves at velocity $v$ in $S$ to reduce the spatial law to $x' = \gamma(x - vt)$.
3. Use the principle of relativity (the symmetry between $S$ and $S'$) to argue that the *same* coefficient $\gamma$ appears in the inverse relation $x = \gamma(x' + vt')$, and that $\gamma$ is an even function of $v$.
4. Use the constancy of the speed of light to solve for $\gamma$, and then derive the temporal law $t' = \gamma(t - vx)$.

**Recall:**

The derivation rests entirely on the two postulates and on what an inertial frame is.

![[Def - Inertial Frame and the Postulates of Special Relativity#The Definition]]

The target is the [[Def - The Lorentz Transformation|Lorentz transformation]]: the coordinate change relating two inertial frames. A free particle's history is a straight line in the $(t,x)$-plane (constant velocity), and a light ray is the special straight line $x = t$ (slope $1$, since $c=1$).

---

# Convergent Strategy

**Problem class.** This is a *derive-the-transformation* problem — the foundational construction of §1.1. The topic page's [[Special Relativity I — Lorentz Transformations and Minkowski Space#Problem-Solving Strategy|strategy]] notes that such problems are won by imposing physical constraints one at a time and watching the freedom collapse.

**Assumption pattern.** Nothing is given but the two postulates and the meaning of "inertial frame". The recognisable feature is "derive from postulates", which signals a constraint-counting argument: start with the most general possible transformation and let each postulate eliminate degrees of freedom.

**Theorem routing.** Four constraints, four reductions. Inertia $\Rightarrow$ linearity (a map preserving straight lines is linear). The origin's motion $\Rightarrow$ the form $\gamma(x-vt)$. The relativity principle $\Rightarrow$ the same $\gamma$ both ways and $\gamma$ even in $v$. The constancy of light $\Rightarrow$ the value $\gamma = (1-v^2)^{-1/2}$ and, by back-substitution, the temporal law.

**Key decision point.** The subtle step is step 3: arguing that the coefficient in the inverse transformation is the *same* $\gamma$, not some independent $\gamma'$. This is where the principle of relativity does its real work, and it relies on the symmetry that nothing distinguishes the two frames except the sign of the relative velocity — and that even the sign is a convention, removable by relabelling the $x$-axis.

---

# Legal Operations Used

1. **"A map preserving straight lines is linear."** The law of inertia in both frames forces straight worldlines to straight worldlines; such a map (fixing the origin) is linear. This is step 1.

2. **Impose the motion of the origin.** The point $x' = 0$ has worldline $x = vt$; demanding this gives the form $\gamma(x-vt)$. This is step 2.

3. **Exploit the symmetry of the two frames** (the principle of relativity). The inverse transformation has the same structure with $v \to -v$, and a left–right relabelling shows $\gamma_v = \gamma_{-v}$. This is step 3.

4. **Impose the constancy of light.** A light ray $x = t$ must map to $x' = t'$; this single equation pins down $\gamma$. This is step 4.

---

# Hints

> [!note]- Hint 1
> Why must the transformation be linear? A particle left alone moves at constant velocity in *both* frames (both are inertial), so its worldline is a straight line in the $(t,x)$-plane *and* in the $(t',x')$-plane. A map that carries every straight line to a straight line, and fixes the origin, is by definition a linear map. So write $x' = \alpha_1 x + \alpha_2 t$, $t' = \alpha_3 x + \alpha_4 t$.

> [!note]- Hint 2
> The spatial origin of $S'$ is the locus $x' = 0$. It moves at velocity $v$ in $S$, so it traces the worldline $x = vt$. Demanding "$x = vt \Rightarrow x' = 0$" forces $\alpha_1 x + \alpha_2 t = 0$ whenever $x = vt$, i.e. $\alpha_2 = -v\alpha_1$. Rename $\alpha_1 = \gamma$.

> [!note]- Hint 3
> Run the identical argument from $S'$'s point of view: $S$ moves at $-v$ relative to $S'$, so $x = \gamma'(x' + vt')$ for some $\gamma'$. To see $\gamma' = \gamma$: relabel both $x$-axes to point the other way ($\tilde x = -x$, $\tilde x' = -x'$). This swaps $v \leftrightarrow -v$ but changes no physics, which forces $\gamma_v = \gamma_{-v}$ — $\gamma$ depends only on $|v|$. Hence $\gamma' = \gamma_{-v} = \gamma_v = \gamma$.

> [!note]- Hint 4
> A light ray is $x = t$ in $S$ and $x' = t'$ in $S'$. Substitute $x = t$ into $x' = \gamma(x-vt)$: $x' = \gamma(1-v)t$. Substitute $x' = t'$ into $x = \gamma(x'+vt')$: $x = \gamma(1+v)t'$. Now use $x = t$, $x' = t'$ to get two relations between $t$ and $t'$; multiply or divide them to eliminate $t, t'$ and solve for $\gamma$. You should find $\gamma^2(1-v^2) = 1$.

---

# Solution

The four postulate-driven constraints reduce the most general transformation — four free coefficients — to a single one-parameter family, and the constancy of light fixes the last parameter. The minus sign in $\gamma(x-vt)$ comes from the moving origin; the value of $\gamma$ comes entirely from light.

**Step 1: Linearity. The transformation is $x' = \alpha_1 x + \alpha_2 t$, $t' = \alpha_3 x + \alpha_4 t$.**

> [!note]- Derivation
> A particle subject to no force moves at constant velocity in any [[Def - Inertial Frame and the Postulates of Special Relativity|inertial frame]] — this is the law of inertia, which holds in both $S$ and $S'$. In the $(t,x)$-plane a constant-velocity worldline is a straight line. So the coordinate map $(t,x)\mapsto(t',x')$ carries straight lines to straight lines. A map of $\mathbb{R}^2$ that sends every straight line to a straight line and fixes the origin (the origins coincide) is an invertible linear map. Hence
> $$x' = \alpha_1 x + \alpha_2 t, \qquad t' = \alpha_3 x + \alpha_4 t,$$
> with four real coefficients $\alpha_1, \dots, \alpha_4$, each possibly a function of the relative velocity $v$. (If the map were nonlinear, a free particle's straight worldline could acquire curvature, and $S'$ would not be inertial.)

**Step 2: The moving origin. The spatial law reduces to $x' = \gamma(x - vt)$.**

> [!note]- Derivation
> The spatial origin of $S'$ is, by definition, the set of events with $x' = 0$. This origin moves at velocity $v$ in $S$, so in $S$ it traces the worldline $x = vt$. Therefore every event with $x = vt$ must have $x' = 0$:
> $$0 = \alpha_1 (vt) + \alpha_2 t = (\alpha_1 v + \alpha_2)t \quad\text{for all }t \;\Longrightarrow\; \alpha_2 = -v\,\alpha_1.$$
> Writing $\gamma$ for the remaining coefficient $\alpha_1$,
> $$x' = \gamma(x - vt).$$
> The coefficient $\gamma$ may still depend on $v$; we write $\gamma_v$ when the dependence matters.

**Step 3: Symmetry of the frames. The inverse law is $x = \gamma(x' + vt')$ with the same $\gamma$, and $\gamma$ is even in $v$.**

> [!note]- Derivation
> Apply the same reasoning from $S'$'s standpoint. Relative to $S'$, the frame $S$ moves at velocity $-v$. Steps 1 and 2, repeated, give
> $$x = \gamma'(x' + vt')$$
> for some coefficient $\gamma' = \gamma_{-v}$ (the boost from $S'$ to $S$ has relative velocity $-v$).
>
> Now the principle of relativity: no inertial frame is preferred, and in particular nothing physical distinguishes "$+x$" from "$-x$". Introduce relabelled frames $\tilde S, \tilde S'$ identical to $S, S'$ but with the $x$-axis reversed: $\tilde x = -x$, $\tilde x' = -x'$. In the tilde coordinates, $S'$ moves at velocity $-v$ relative to $S$. Running step 2 in the tilde coordinates gives $\tilde x' = \gamma_{-v}(\tilde x + v t)$, which on substituting $\tilde x = -x$, $\tilde x' = -x'$ becomes $x' = \gamma_{-v}(x - vt)$. Comparing with $x' = \gamma_v(x-vt)$ from step 2,
> $$\gamma_v = \gamma_{-v}: \quad \gamma \text{ is an even function of } v.$$
> Hence $\gamma' = \gamma_{-v} = \gamma_v = \gamma$ — the *same* coefficient $\gamma$ appears in both the forward and the inverse spatial law:
> $$x' = \gamma(x - vt), \qquad x = \gamma(x' + vt').$$

**Step 4: Constancy of light. $\gamma = (1-v^2)^{-1/2}$, and $t' = \gamma(t - vx)$.**

> [!note]- Derivation
> Consider a light ray. In $S$ it satisfies $x = t$; by the second postulate it satisfies $x' = t'$ in $S'$.
>
> Substitute $x = t$ into the forward law: $x' = \gamma(t - vt) = \gamma(1-v)t$. Since $x' = t'$ for the ray, $t' = \gamma(1-v)t$.
>
> Substitute $x' = t'$ into the inverse law: $x = \gamma(t' + vt') = \gamma(1+v)t'$. Since $x = t$, $t = \gamma(1+v)t'$.
>
> Multiply the two boxed relations $t' = \gamma(1-v)t$ and $t = \gamma(1+v)t'$:
> $$t\,t' = \gamma^2(1-v)(1+v)\,t\,t' = \gamma^2(1 - v^2)\,t\,t'.$$
> Cancelling $t\,t'$ gives $\gamma^2(1-v^2) = 1$, hence
> $$\gamma = \frac{1}{\sqrt{1 - v^2}}$$
> (taking the positive root so that $\gamma \to 1$ as $v \to 0$).
>
> Finally the temporal law. Substitute the forward spatial law $x' = \gamma(x-vt)$ into the inverse spatial law $x = \gamma(x' + vt')$:
> $$x = \gamma\big(\gamma(x-vt) + vt'\big) = \gamma^2(x - vt) + \gamma v t'.$$
> Solve for $t'$:
> $$\gamma v t' = x - \gamma^2 x + \gamma^2 v t = x(1 - \gamma^2) + \gamma^2 v t.$$
> Now $1 - \gamma^2 = 1 - \frac{1}{1-v^2} = \frac{-v^2}{1-v^2} = -\gamma^2 v^2$. Substituting,
> $$\gamma v t' = -\gamma^2 v^2 x + \gamma^2 v t = \gamma^2 v(t - vx),$$
> and dividing by $\gamma v$,
> $$t' = \gamma(t - vx).$$

> [!note]- Complete formal solution
> By the law of inertia, holding in both inertial frames, free-particle worldlines (straight lines) map to straight lines, so the origin-fixing coordinate map is linear: $x' = \alpha_1 x + \alpha_2 t$, $t' = \alpha_3 x + \alpha_4 t$. The origin $x'=0$ of $S'$ moves as $x = vt$ in $S$, forcing $\alpha_2 = -v\alpha_1$; write $\alpha_1 = \gamma$, so $x' = \gamma(x-vt)$. The same construction from $S'$ gives $x = \gamma_{-v}(x'+vt')$; a reversal of both $x$-axes shows $\gamma_v = \gamma_{-v}$, so the inverse coefficient equals $\gamma$, giving $x = \gamma(x'+vt')$. A light ray has $x=t$ and $x'=t'$; substituting yields $t' = \gamma(1-v)t$ and $t = \gamma(1+v)t'$, whose product forces $\gamma^2(1-v^2) = 1$, i.e. $\gamma = (1-v^2)^{-1/2}$. Substituting $x' = \gamma(x-vt)$ into $x = \gamma(x'+vt')$ and using $1-\gamma^2 = -\gamma^2 v^2$ gives $t' = \gamma(t-vx)$. Thus
> $$x' = \gamma(x-vt), \qquad t' = \gamma(t-vx), \qquad \gamma = (1-v^2)^{-1/2}. \qquad \blacksquare$$

---

# Key Takeaways

**Derive-from-axioms problems are solved by imposing constraints one at a time and counting lost degrees of freedom.** The transformation began with four free coefficients. Linearity was already used to *get* those four (a fully general map has infinitely many). The moving origin removed one. The relativity principle removed the would-be independence of the inverse coefficient. The constancy of light removed the last. Four physical inputs, four coefficients, a unique answer. This is the universal shape of an axiomatic derivation in physics: enumerate the freedoms, enumerate the constraints, check they match. Whenever a problem says "derive X from first principles", set up the most general X compatible with the cheapest constraint and then spend the remaining constraints one by one — and if the freedoms and constraints do not balance, you have either missed a constraint or smuggled in an assumption.

**The minus sign and the value of $\gamma$ have different origins, and keeping them separate clarifies the whole structure.** The form $x' = \gamma(x - vt)$ — including its minus sign — comes purely from kinematics: the origin of $S'$ moves, and $-vt$ is what tracks it. *Any* theory with a moving frame, Galilean included, has this. What is distinctively relativistic is only the *value* $\gamma = (1-v^2)^{-1/2}$, and that comes from one place and one place only: the constancy of light. If you had imposed absolute time, $t' = t$, instead of the constancy of light, you would have been forced to $\gamma = 1$ and recovered the Galilean transformation. So the entire empirical content of special relativity is concentrated in the single step where the light ray fixes $\gamma$. Recognising which features of a formula are "free" kinematics and which carry the physics is a skill that transfers to every derivation in the subject.

**The symmetry argument — that the inverse transformation uses the same $\gamma$ — is the principle of relativity doing real work, and it is easy to skip.** It is tempting to assume without comment that the boost from $S'$ back to $S$ is just the boost from $S$ to $S'$ with $v \to -v$. But that the *coefficient* is literally the same function $\gamma$, evaluated at $|v|$, is a genuine consequence of there being no preferred frame: if $\gamma_v \ne \gamma_{-v}$, then the two frames would be physically distinguishable by the size of the effect, contradicting Postulate 1. The trick for proving evenness — relabel the spatial axis and watch $v$ flip sign while the physics does not — is a reusable move: whenever you suspect a quantity depends only on a magnitude, find a relabelling that flips the sign of the argument without changing anything physical, and the evenness follows. The same idea shows that transverse lengths are uncontracted and that $\gamma$ cannot depend on the direction of the boost.
