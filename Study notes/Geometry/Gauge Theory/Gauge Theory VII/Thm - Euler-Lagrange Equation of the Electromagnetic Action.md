---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Electromagnetic Lagrangian and Action"
  - "Thm - Properties of the Hodge Star in Arbitrary Signature"
  - "Thm - Stokes' Theorem on Manifolds"
  - "Def - Maxwell Equations in Form Language"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $M$ is an oriented [[Def - Lorentzian Manifold|Lorentzian]] four-manifold: a smooth four-dimensional manifold with a semi-Riemannian metric $\langle\cdot,\cdot\rangle$ of signature $(-,+,+,+)$, so that at every point the metric has [[Def - Generalized Orthonormal Basis, Index, and the Induced Inner Product on Forms|index]] $p=1$ (exactly one negative direction). This is the mathematical model of spacetime; we take the speed of light $c=1$. We work with a principal [[Def - Principal G-Bundle|$U(1)$-bundle]] $\pi:P\to M$ and a [[Def - Connection on a Principal Bundle|connection]] $\omega\in\mathcal C(P)$, where $\mathcal C(P)$ denotes the set of all connections on $P$.

Because $U(1)$ is abelian, the adjoint action $\operatorname{Ad}_g$ is trivial, so the local [[Def - Curvature of a Principal Connection|curvature]] $s^*\Omega$ of $\omega$ is independent of the local section $s$ and assembles into a global two-form $\bar\Omega\in\Omega^2(M;i\mathbb R)$; we write $\bar\Omega=iF$ with the **electromagnetic field strength** $F\in\Omega^2(M;\mathbb R)$, and the [[Thm - Bianchi Identity for a Principal Connection|Bianchi identity]] gives $dF=0$. Relative to a fixed background connection $\omega_0\in\mathcal C(P)$, the **potential** is the section-independent one-form $iA=iA(\omega,\omega_0):=s^*(\omega-\omega_0)\in\Omega^1(M;i\mathbb R)$, with $A\in\Omega^1(M;\mathbb R)$ and $dA=F-F_0$, where $F_0$ is the field strength of $\omega_0$. The **charge–current** is a fixed three-form $J\in\Omega^3(M;\mathbb R)$. All of this is set up on [[Def - U(1) Gauge Field and Electromagnetic Connection|the electromagnetic-connection page]] and [[Def - Charge-Current 3-Form|the charge–current page]].

The symbol $\star$ is the [[Def - Hodge Star in Arbitrary Signature|Hodge star]] of the Lorentzian metric on $M$; $\Omega^k(M;\mathbb R)=\Gamma(\Lambda^kT^*M)$ is the space of smooth real $k$-forms and $\Omega^k_c(M;\mathbb R)$ its compactly supported subspace; $\langle\cdot,\cdot\rangle$ also denotes the induced inner product on $\Lambda^kT^*M$; $\operatorname{vol}\in\Omega^4(M;\mathbb R)$ is the Lorentzian volume form; and $U\Subset M$ means that $U$ is open with compact closure $\bar U\subset M$.

> [!warning] Convention: the Hodge star
> We use Bär's defining relation for the star (`conventions.md`, adopted series-wide): for $\omega\in\Lambda^kT^*_xM$ and $\eta\in\Lambda^{n-k}T^*_xM$,
> $$\omega\wedge\eta=\langle\star\omega,\eta\rangle\,\operatorname{vol},$$
> which on $k$-forms of an index-$p$ space gives $\star\star=(-1)^{k(n-k)+p}$. The other common convention $\alpha\wedge\star\beta=\langle\alpha,\beta\rangle\,\operatorname{vol}$ differs from ours by the factor $(-1)^{k(n-k)}$; the two agree on two-forms in dimension four. The vault's Riemannian page [[Thm - Properties of the Hodge Star|Properties of the Hodge Star]] is the $p=0$ case in the convention $\star_V$, related to ours by $\star_B=(-1)^p\star_V$.

> [!warning] Convention: signs, units, and the component form
> The component-language version of this result in the vault, [[Thm - Maxwell Equations from a Principle of Least Action|Maxwell equations from a principle of least action]] (Special Relativity XXII), is written in signature $(+,-,-,-)$ with SI units and $c$ explicit; the dictionary to our $(-,+,+,+)$, $c=1$ conventions is $g_{\mathrm{SR}}=-g_B$, the same field two-form $F$ and the same fields $\vec E,\vec B$, and $\star^{\mathrm{SR}}_V=-\star_B$ on Minkowski space. The inhomogeneous Maxwell equation is $d\star F+J=0$ throughout this series. Bär prints "$d\star F=J$" once on page 95 (source typo, Appendix B item 21), contradicting his own page-86 derivation $d\star F+J=0$; we use $d\star F+J=0$, which is what the calculation below produces. Bär also lists the target of the Lagrangian as $\Omega^4(M;i\mathbb R)$ (source typo, item 16); the Lagrangian is real-valued, $L:\mathcal C(P)\to\Omega^4(M;\mathbb R)$.

---

# Statement

> **Theorem (Euler–Lagrange equation of the electromagnetic action).** Let $M$ be an oriented Lorentzian four-manifold, $\pi:P\to M$ a principal $U(1)$-bundle, $\omega_0\in\mathcal C(P)$ a fixed background connection, and $J\in\Omega^3(M;\mathbb R)$ a fixed charge–current three-form. Let $L:\mathcal C(P)\to\Omega^4(M;\mathbb R)$ be the electromagnetic Lagrangian
> $$L(\omega)=\tfrac12\,F\wedge\star F+A\wedge J,\qquad A=A(\omega,\omega_0),\quad \bar\Omega=iF.$$
> Then a connection $\omega\in\mathcal C(P)$ is **critical** for $L$ if and only if its field strength satisfies the inhomogeneous Maxwell equation
> $$d\star F+J=0.$$

Here criticality is the following condition, transcluded from [[Def - Electromagnetic Lagrangian and Action]]:

![[Def - Electromagnetic Lagrangian and Action#The Definition]]

In words: for every relatively compact open set $U\Subset M$ and every compactly supported test one-form $\eta\in\Omega^1(M;\mathbb R)$ with $\operatorname{supp}\eta\subset U$, the connection $\omega_{t,\eta}\in\mathcal C(P)$ with potential $A(\omega_{t,\eta},\omega_0)=A+t\eta$ satisfies
$$\frac{d}{dt}\Big|_{t=0}\int_{\bar U}L(\omega_{t,\eta})=0.$$
Such a family $\omega_{t,\eta}$ exists because $\mathcal C(P)$ is an affine space over $\Omega^1(M;\mathrm{ad}P)\cong\Omega^1(M;i\mathbb R)$; see [[Thm - The Space of Connections is an Affine Space|the affine-space theorem]]. Its field strength is $F(\omega_{t,\eta})=F+t\,d\eta$, because varying the potential by $t\eta$ varies the field by $d(t\eta)=t\,d\eta$.

The homogeneous Maxwell equation $dF=0$ is not part of this statement: it holds automatically for every connection, as an instance of the Bianchi identity, and is recorded on [[Def - Maxwell Equations in Form Language|the Maxwell-equations page]]. The content of the present theorem is that the **remaining, inhomogeneous** equation $d\star F+J=0$ is precisely the condition for $\omega$ to make the action stationary.

---

# Motivation

The first two Maxwell equations, Gauss's law for magnetism and Faraday's law, arrive for free: they are the coordinate reading of $dF=0$, and $dF=0$ is the Bianchi identity for any $U(1)$-connection. So half of electrodynamics is a geometric identity, true of every field configuration whatsoever. The question this theorem answers is where the *other* half — Coulomb's law and Ampère's law, the two equations that actually involve the sources — comes from. They cannot be identities, because they are the equations the sources have to satisfy; they must instead be equations of motion, singled out among all conceivable fields by a variational principle.

The theorem says exactly that. One writes down the simplest gauge-invariant, first-order, quadratic action a two-form field can have, adds the simplest possible coupling to the sources, and asks which fields make it stationary under compactly supported variations. The answer is $d\star F+J=0$, the inhomogeneous Maxwell equation. This is the mathematical statement that electrodynamics is a field theory derivable from a principle of least action, and it is the template for every gauge theory that follows: replacing the abelian curvature $F$ by the curvature of a non-abelian connection and $\tfrac12 F\wedge\star F$ by the Yang–Mills density $\tfrac12\langle F\wedge\star F\rangle$ turns this exact calculation into the derivation of the [[Def - Maxwell Equations in Form Language|Yang–Mills equation]] $d^A\star F_A=0$ of section 7.4. The whole subject rests on knowing that varying a quadratic action in the field produces a first-order equation in the star of the field, and this is the page where that mechanism is isolated in its cleanest, abelian form.

---

# Sources and Targets

**Sources (Input Broadening).** The theorem is stated for the electromagnetic action, but its engine is generic, so the useful question is which other problems secretly present the same variational structure.

The first disguised source is **any first-order, quadratic, gauge-invariant action built from a curvature and its Hodge dual**. Whenever a field theory has an action of the shape $\int(\tfrac12\,\Phi\wedge\star\Phi+\text{linear coupling})$, where $\Phi$ is the curvature of the field being varied and the variation of $\Phi$ is the exterior derivative of the variation of the potential, the same three moves apply: expand the quadratic term, use the symmetry of the star pairing to combine the two cross terms, and integrate by parts to move $d$ off the test form. The bridge $B\Rightarrow A$ is the recognition that "quadratic in a curvature, linear in a potential, first order" is precisely the hypothesis under which the Euler–Lagrange computation below goes through verbatim. *Example problem:* derive the field equation of a free real two-form gauge field (a "Kalb–Ramond field") $B$ with action $\tfrac12\int H\wedge\star H$, $H=dB$; the same steps give $d\star H=0$.

The second disguised source is **a scalar-field or $p$-form Lagrangian written in the language of forms**. A massless scalar field $\phi$ on $M$ with action $\tfrac12\int d\phi\wedge\star d\phi$ has $d\phi$ playing the role of the curvature; varying $\phi$ by $t\psi$ varies $d\phi$ by $t\,d\psi$, exactly as $F$ is varied by $t\,d\eta$ here. The bridge is that $d\phi$ is a "field strength" whose variation is again a total derivative of the variation of the potential $\phi$. The non-obvious point is that the fundamental lemma one needs is the degree-$0$/degree-$n$ pairing rather than the $1$/$(n-1)$ pairing, but the argument is identical. *Example problem:* show that $\phi$ is critical for $\tfrac12\int d\phi\wedge\star d\phi-\int\phi\,\rho$ (with $\rho\in\Omega^n$) if and only if $d\star d\phi+\rho=0$, the wave/Poisson equation.

The third disguised source is **a variational problem whose stationarity is tested against compactly supported perturbations of a section of an affine bundle**. Any time the configuration space is an affine space (connections, metrics up to a fixed background, sections of an affine bundle) and criticality is defined by localized perturbations, the machinery of "differentiate the action along an affine ray, integrate by parts, apply the fundamental lemma" produces the field equation. The bridge $B\Rightarrow A$ is that affineness supplies the straight-line family $\omega_{t,\eta}$ needed to define the derivative, and compact support supplies the vanishing boundary term. *Example problem:* the Hilbert action of general relativity, varied against compactly supported metric perturbations, yields the Einstein equations by the same skeleton (see [[Thm - Hilbert's Variational Principle Yields Einstein Equations|Hilbert's variational principle]]).

**Targets (Output Amplification).** The bare conclusion is an equivalence between criticality and $d\star F+J=0$. Combined with further ingredients it does more.

Combine the conclusion with **the nilpotence $d^2=0$**. Applying $d$ to the critical equation $d\star F+J=0$ gives $d(d\star F)+dJ=dJ$, and $d(d\star F)=0$, so $dJ=0$: **charge is automatically conserved on shell**. The extra ingredient is $d^2=0$ and the payoff is the [[Thm - Continuity Equation and Conservation of Charge|continuity equation]] $\partial_t\varrho+\operatorname{div}\vec j=0$; conservation of charge is thus not an independent physical law but a consequence of the equations of motion. This is a genuine amplification: a single field equation forces an infinite family of integral conservation laws.

Combine the conclusion with **the coordinate expression of $d$ and $\star$ on Minkowski space**. Writing $F=E_x\,dx\wedge dt+\dots+B_z\,dx\wedge dy$ and computing $\star F$ from the Minkowski star table turns $d\star F+J=0$ into the two vector equations $\operatorname{div}\vec E=\varrho$ (Coulomb) and $\operatorname{rot}\vec B-\partial_t\vec E=\vec j$ (Ampère). The extra ingredient is the star table of [[Thm - Maxwell Equations in Coordinates|the coordinate page]] and the payoff is that the abstract field equation reproduces exactly the two inhomogeneous Maxwell equations of the physics literature.

Combine the conclusion with **background-independence**. The Lagrangian depends on the arbitrary choice of $\omega_0$, but the coupling term changes only by $A(\tilde\omega_0,\omega_0)\wedge J$, a form that does not depend on $\omega$, when the background is changed. The extra ingredient is the affine structure of $\mathcal C(P)$ and the payoff is that the Euler–Lagrange equation is independent of $\omega_0$ (proved as an example on [[Def - Electromagnetic Lagrangian and Action|the Lagrangian page]] and drilled in [[Ex - The Background Connection Drops Out of the Euler-Lagrange Equation|the background-independence exercise]]); the physics does not see the reference connection.

---

# Why Is It True

Set aside the formalism and picture what varying the action does. The action has two pieces. The quadratic piece $\tfrac12\int F\wedge\star F$ measures the "size" of the field, weighted by the metric through the star. The linear piece $\int A\wedge J$ is how the field couples to whatever charges and currents are present. We wiggle the connection along a straight line $\omega_{t,\eta}$, which wiggles the potential by $t\eta$ and hence the field by $t\,d\eta$, and we ask that the action not change to first order in $t$.

The quadratic piece has two cross terms when expanded, $d\eta\wedge\star F$ and $F\wedge\star d\eta$, and the first mechanism is that **these two are equal, because the wedge pairing through the star is symmetric**: $\alpha\wedge\star\beta=\beta\wedge\star\alpha$. So the first variation of the quadratic piece is simply $\int d\eta\wedge\star F$ — the test field's derivative wedged against the star of the actual field. Now the second and decisive mechanism: $d\eta$ carries a derivative that lands on the test form $\eta$, and we cannot conclude anything about a pointwise equation while the derivative is stuck on the arbitrary test form. Integration by parts moves it. Because $\eta$ has compact support, the boundary term produced by Stokes vanishes, and the derivative reappears on $\star F$:
$$\int_M d\eta\wedge\star F=\int_M\eta\wedge d\star F.$$
What multiplies the arbitrary test form $\eta$ is now $d\star F$, and adding the linear piece's contribution $\int\eta\wedge J$ leaves $\int_M\eta\wedge(d\star F+J)$. A quantity that pairs to zero against *every* compactly supported test form must vanish identically — this is the fundamental lemma of the calculus of variations, in its form-valued incarnation. Hence $d\star F+J=0$.

> **The mechanism in one sentence: variation moves the exterior derivative off the test form by Stokes, and what is left multiplying the arbitrary test form is $d\star F$, so stationarity forces $d\star F+J=0$.**

The reason $F$ appears only through its star, and only through $d\star F$ rather than $F$ itself, is worth stating: the field enters the action wedged with $\star F$, and integration by parts converts the derivative on the *variation* into a derivative on $\star F$. The homogeneous equation $dF=0$ needed no variation at all — it is the Bianchi identity — and this is why exactly one of the two Maxwell pairs is dynamical while the other is kinematical.

---

# What Makes This Hard

The subtle steps are three. First, the definition of criticality involves integrating over $\bar U$, and Bär's own derivation invokes Stokes on $\bar U$ "with $\eta|_{\partial U}=0$", but $\bar U$ need not be a manifold with boundary — its topological boundary can be irregular. The correct move is to notice that $\eta\wedge\star F$ is compactly supported inside $U$, so its integral over all of $M$ (a boundaryless manifold) is zero by Stokes for compactly supported forms, and no boundary regularity is ever needed. Second, the fundamental lemma for the wedge pairing is genuinely more delicate in Lorentzian signature than in Riemannian signature: the naive test form $\eta=f\star\beta$ produces $\int f\langle\beta,\beta\rangle\operatorname{vol}$, which can vanish identically for a nonzero *null* three-form $\beta$, so this test form is blind to null fields; one must instead argue coefficient by coefficient using the fact that the wedge pairing $\Lambda^1\times\Lambda^{n-1}\to\Lambda^n$ is perfect independently of the metric. Third, the interchange of $\frac{d}{dt}$ with $\int_{\bar U}$ must be justified, not assumed; here it is trivial once one observes that the integrand is a genuine polynomial in $t$, but the observation has to be made.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Expand the action along the affine ray $\omega_{t,\eta}$ as a polynomial in $t$; its linear coefficient is the first variation. Simplify that coefficient using the symmetry of the star pairing so that only $\int d\eta\wedge\star F$ survives from the quadratic term; integrate by parts (Stokes, compact support) to convert it to $\int\eta\wedge d\star F$; add the linear term $\int\eta\wedge J$; then invoke the fundamental lemma to pass from "the pairing vanishes for all $\eta$" to "$d\star F+J=0$".

**Subgoal decomposition:**

1. **Expand the action as a polynomial in $t$.** Substitute $F+t\,d\eta$ and $A+t\eta$ into $L$ and collect powers of $t$.
   - *Hint:* $F\wedge\star F$ expands into a constant, two linear cross terms, and a $t^2$ term; $A\wedge J$ into a constant and one linear term.
   - *Why needed:* it turns the derivative $\frac{d}{dt}|_0$ into "read off the coefficient of $t$", and simultaneously justifies interchanging the derivative and the integral, because the integral of a $t$-polynomial family is a polynomial in $t$.

2. **Combine the two cross terms.** Show $F\wedge\star d\eta=d\eta\wedge\star F$, so the linear coefficient of the quadratic term is $d\eta\wedge\star F$, not $\tfrac12(d\eta\wedge\star F+F\wedge\star d\eta)$ left unsimplified.
   - *Hint:* this is the symmetry $\alpha\wedge\star\beta=\beta\wedge\star\alpha$, property (4) of the Hodge star.
   - *Why needed:* without it the coefficient is not manifestly of the form "test-form-derivative wedge star-of-field", and the integration by parts of subgoal 3 does not apply cleanly.

3. **Integrate by parts.** Prove $\int_M d\eta\wedge\star F=\int_M\eta\wedge d\star F$ for compactly supported $\eta$.
   - *Hint:* graded Leibniz gives $d(\eta\wedge\star F)=d\eta\wedge\star F-\eta\wedge d\star F$; integrate and kill the exact term by Stokes for compactly supported forms.
   - *Why needed:* it moves the derivative off the arbitrary test form so that the fundamental lemma can be applied.

4. **Assemble the first variation.** Combine subgoals 1–3 with the linear term of $A\wedge J$ to get $\frac{d}{dt}|_0\int_{\bar U}L(\omega_{t,\eta})=\int_M\eta\wedge(d\star F+J)$.
   - *Hint:* the linear coefficient of $A\wedge J$ is $\eta\wedge J$.
   - *Why needed:* it reduces criticality to the vanishing of a single wedge pairing.

5. **Apply the fundamental lemma both ways.** If $d\star F+J=0$ the pairing is zero for every $\eta$, so $\omega$ is critical; conversely if $\omega$ is critical the pairing vanishes for every $\eta$, and the fundamental lemma forces the three-form $d\star F+J$ to vanish.
   - *Hint:* for the converse, if the three-form were nonzero at a point, build a bump test form detecting it through the perfect wedge pairing.
   - *Why needed:* it is the exact bridge between "stationary for all localized variations" and "a pointwise partial differential equation".

---

# Lemma Decomposition

> [!note]- Lemma 1: Fundamental lemma of the calculus of variations for the wedge pairing
> **Statement:** Let $M$ be an oriented smooth $n$-manifold and $\beta\in\Omega^{n-1}(M;\mathbb R)$ a smooth $(n-1)$-form. If
> $$\int_M\eta\wedge\beta=0\qquad\text{for every }\eta\in\Omega^1_c(M;\mathbb R),$$
> then $\beta=0$. (We use it with $n=4$, so $\beta$ is a three-form.)
>
> **Hint:** Suppose $\beta(p)\neq0$; the pointwise pairing $\Lambda^1T^*_pM\times\Lambda^{n-1}T^*_pM\to\Lambda^nT^*_pM$, $(\alpha,\gamma)\mapsto\alpha\wedge\gamma$, is perfect, so some covector $\alpha$ has $\alpha\wedge\beta(p)\neq0$; freeze $\alpha$, multiply by a bump function, and integrate.
>
> **Why needed:** it is the step that converts "the first variation vanishes for every localized test one-form" into the pointwise equation $d\star F+J=0$. It replaces, in a metric-free way, the naive $\eta=f\star\beta$ test form, which fails on null three-forms in Lorentzian signature.
>
> > [!note]- Full proof
> > We argue by contraposition: assuming $\beta\neq0$, we produce a compactly supported one-form $\eta$ with $\int_M\eta\wedge\beta\neq0$.
> >
> > **Step 1 — a point where $\beta$ is nonzero and a chart around it.** Since $\beta\neq0$, there is a point $p\in M$ with $\beta(p)\neq0$ (by definition, a form is zero precisely when it is zero at every point). Choose an oriented smooth chart $(U,x^1,\dots,x^n)$ around $p$ in which $\operatorname{vol}=v\,dx^1\wedge\dots\wedge dx^n$ with a smooth function $v>0$ (an oriented chart exists because $M$ is oriented, and the volume form is a positive multiple of the coordinate top-form there).
> >
> > **Step 2 — the pointwise wedge pairing is perfect.** Consider the bilinear map
> > $$B_p:\Lambda^1T^*_pM\times\Lambda^{n-1}T^*_pM\longrightarrow\Lambda^nT^*_pM,\qquad B_p(\alpha,\gamma)=\alpha\wedge\gamma.$$
> > We claim that for the fixed nonzero $\gamma:=\beta(p)$ there is an $\alpha$ with $\alpha\wedge\gamma\neq0$. Expand $\gamma$ in the basis of $(n-1)$-forms $dx^{\hat\imath}:=dx^1\wedge\dots\wedge\widehat{dx^i}\wedge\dots\wedge dx^n$ (omit the $i$-th factor), $\gamma=\sum_{i=1}^n c_i\,dx^{\hat\imath}$ with $c_i\in\mathbb R$. Because $\gamma\neq0$, some coefficient $c_m\neq0$. Take $\alpha=dx^m$. Then $dx^m\wedge dx^{\hat\imath}=0$ for $i\neq m$ (a repeated factor $dx^m$ occurs), while
> > $$dx^m\wedge dx^{\hat m}=(-1)^{m-1}\,dx^1\wedge\dots\wedge dx^n\qquad\text{(moving }dx^m\text{ past the }m-1\text{ factors before its slot)},$$
> > so $\alpha\wedge\gamma=(-1)^{m-1}c_m\,dx^1\wedge\dots\wedge dx^n\neq0$. Thus $B_p(\alpha,\beta(p))\neq0$ for this $\alpha$. Replacing $\alpha$ by $-\alpha$ if necessary, we may assume $\alpha\wedge\beta(p)=h(p)\,\operatorname{vol}_p$ with $h(p)>0$, where $h$ is the smooth function defined below.
> >
> > **Step 3 — freeze $\alpha$ and use continuity.** Extend $\alpha$ to the constant-coefficient one-form $\alpha=dx^m$ on the chart $U$. Then $\alpha\wedge\beta$ is a smooth $n$-form on $U$; write $\alpha\wedge\beta=h\,\operatorname{vol}$ with $h\in C^\infty(U)$ (possible since $\Lambda^nT^*M|_U$ is spanned by $\operatorname{vol}$). By Step 2, $h(p)>0$. By continuity of $h$ there is an open neighbourhood $V\subset U$ of $p$, with $\bar V\subset U$ compact, on which $h>0$.
> >
> > **Step 4 — a bump test form.** Choose $f\in C^\infty_c(V)$ with $f\geq0$, $f(p)>0$ (a bump function supported in $V$; such functions exist on any smooth manifold). Define $\eta:=f\,\alpha\in\Omega^1_c(M;\mathbb R)$, extended by zero outside $V$; it is smooth and compactly supported. Then
> > $$\int_M\eta\wedge\beta=\int_V f\,(\alpha\wedge\beta)=\int_V f\,h\,\operatorname{vol}.$$
> > On $V$ we have $f\geq0$, $h>0$, and $\operatorname{vol}=v\,dx^1\wedge\dots\wedge dx^n$ with $v>0$, so the integrand $f\,h\,v$ is nonnegative and strictly positive on a neighbourhood of $p$ (where $f>0$). Hence $\int_V f\,h\,\operatorname{vol}>0$, so $\int_M\eta\wedge\beta\neq0$.
> >
> > **Conclusion.** We have produced $\eta\in\Omega^1_c(M;\mathbb R)$ with $\int_M\eta\wedge\beta\neq0$, contradicting the hypothesis. Therefore $\beta=0$. $\blacksquare$

> [!note]- Lemma 2: Integration by parts for the star pairing
> **Statement:** Let $M$ be an oriented smooth $n$-manifold without boundary, $F\in\Omega^2(M;\mathbb R)$, and $\eta\in\Omega^1_c(M;\mathbb R)$ compactly supported. Then
> $$\int_M d\eta\wedge\star F=\int_M\eta\wedge d\star F.$$
>
> **Hint:** apply the graded Leibniz rule to $d(\eta\wedge\star F)$ and integrate; the exact term integrates to zero by Stokes because $\eta\wedge\star F$ is compactly supported.
>
> **Why needed:** it is the integration-by-parts step that transfers the derivative from the arbitrary test form $\eta$ onto $\star F$, exposing $d\star F$ as the multiplier of $\eta$.
>
> > [!note]- Full proof
> > **Step 1 — graded Leibniz.** The [[Def - Exterior Derivative on a Manifold|exterior derivative]] is a graded derivation: for $\alpha\in\Omega^k(M)$ and $\gamma\in\Omega^\ell(M)$, $d(\alpha\wedge\gamma)=d\alpha\wedge\gamma+(-1)^k\alpha\wedge d\gamma$ (this is property 3 in the definition of $d$). Apply it with $\alpha=\eta\in\Omega^1$ ($k=1$) and $\gamma=\star F\in\Omega^{n-2}$:
> > $$d(\eta\wedge\star F)=d\eta\wedge\star F+(-1)^1\,\eta\wedge d(\star F)=d\eta\wedge\star F-\eta\wedge d\star F.$$
> > Rearranging,
> > $$d\eta\wedge\star F=d(\eta\wedge\star F)+\eta\wedge d\star F.\qquad(\ast)$$
> >
> > **Step 2 — the exact term integrates to zero.** The form $\eta\wedge\star F$ has support contained in $\operatorname{supp}\eta$, which is compact, so $\eta\wedge\star F\in\Omega^{n-1}_c(M;\mathbb R)$. By [[Thm - Stokes' Theorem on Manifolds|Stokes's theorem]] — for an oriented manifold $M$ with boundary and a compactly supported $(n-1)$-form $\alpha$, $\int_M d\alpha=\int_{\partial M}\alpha$, and when $\partial M=\emptyset$ the right-hand side is $0$ — applied to the boundaryless manifold $M$,
> > $$\int_M d(\eta\wedge\star F)=0.$$
> >
> > **Step 3 — integrate $(\ast)$.** Integrating the identity $(\ast)$ over $M$ and using Step 2,
> > $$\int_M d\eta\wedge\star F=\int_M d(\eta\wedge\star F)+\int_M\eta\wedge d\star F=0+\int_M\eta\wedge d\star F=\int_M\eta\wedge d\star F.$$
> > Every integral here is finite because each integrand is compactly supported (all factors after $d\eta$ are multiplied by something supported in $\operatorname{supp}\eta$; $d\eta$ itself is supported in $\operatorname{supp}\eta$). This is the claimed identity. $\blacksquare$

> [!note]- Lemma 3: Symmetry of the star pairing
> **Statement:** Let $V$ be an oriented $n$-dimensional real vector space with a non-degenerate symmetric bilinear form of index $p$. For $\omega,\eta\in\Lambda^kV^*$,
> $$\omega\wedge\star\eta=\eta\wedge\star\omega=(-1)^p\langle\omega,\eta\rangle\,\operatorname{vol}.$$
> Pointwise on the Lorentzian four-manifold $M$ ($p=1$) this gives, for two-forms $\alpha,\beta$, $\alpha\wedge\star\beta=\beta\wedge\star\alpha$.
>
> **Hint:** this is exactly property (4) of [[Thm - Properties of the Hodge Star in Arbitrary Signature|the properties-of-the-star theorem]]; no new work is needed beyond quoting it and reading off the two-form specialization.
>
> **Why needed:** it identifies the two cross terms $d\eta\wedge\star F$ and $F\wedge\star d\eta$ in the first variation of the quadratic part, so that their sum is $2\,d\eta\wedge\star F$ and the factor $\tfrac12$ cancels.
>
> > [!note]- Full proof
> > The identity is part (4) of the fully proved theorem [[Thm - Properties of the Hodge Star in Arbitrary Signature]], whose statement we restate: for $\omega,\eta\in\Lambda^kV^*$ on an oriented index-$p$ space, $\omega\wedge\star\eta=\eta\wedge\star\omega=(-1)^p\langle\omega,\eta\rangle\operatorname{vol}$. We reproduce the derivation so the page is self-contained. Starting from the defining relation of the star, $\mu\wedge\nu=\langle\star\mu,\nu\rangle\operatorname{vol}$ for $\mu\in\Lambda^k$, $\nu\in\Lambda^{n-k}$, put $\mu=\omega$ and $\nu=\star\eta\in\Lambda^{n-k}$:
> > $$\omega\wedge\star\eta=\langle\star\omega,\star\eta\rangle\operatorname{vol}\qquad\text{(defining relation with }\nu=\star\eta\text{)}.$$
> > By part (3) of the same theorem, $\langle\star\omega,\star\eta\rangle=(-1)^p\langle\omega,\eta\rangle$ (the star is an isometry up to the sign of the index), so
> > $$\omega\wedge\star\eta=(-1)^p\langle\omega,\eta\rangle\operatorname{vol}.$$
> > The right-hand side is symmetric in $\omega$ and $\eta$ because the induced inner product $\langle\cdot,\cdot\rangle$ is symmetric; therefore $\omega\wedge\star\eta=(-1)^p\langle\eta,\omega\rangle\operatorname{vol}=\eta\wedge\star\omega$. Specializing to $n=4$, $k=2$, $p=1$ on each tangent space of $M$ gives $\alpha\wedge\star\beta=\beta\wedge\star\alpha$ for two-forms. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Fix the oriented Lorentzian four-manifold $M$, the $U(1)$-bundle $P\to M$, the background connection $\omega_0$, and the charge–current $J\in\Omega^3(M;\mathbb R)$. Let $\omega\in\mathcal C(P)$ be arbitrary with field strength $F$ ($\bar\Omega=iF$) and potential $A=A(\omega,\omega_0)$. We prove: $\omega$ is critical for $L$ $\iff$ $d\star F+J=0$.
>
> **Step 0 — the variation is well-posed.** Fix $U\Subset M$ and a test form $\eta\in\Omega^1(M;\mathbb R)$ with $\operatorname{supp}\eta\subset U$. Since $\mathcal C(P)$ is an affine space modelled on $\Omega^1(M;\mathrm{ad}P)$ and $\mathrm{ad}P\cong M\times i\mathbb R$ is trivial for the abelian group $U(1)$ (so $\Omega^1(M;\mathrm{ad}P)\cong\Omega^1(M;i\mathbb R)$), there is for each $t\in\mathbb R$ a connection $\omega_{t,\eta}\in\mathcal C(P)$ with $A(\omega_{t,\eta},\omega_0)=A+t\eta$; this is [[Thm - The Space of Connections is an Affine Space|the affine-space theorem]] applied to the model form $it\eta$. Its field strength is
> $$F(\omega_{t,\eta})=F_0+d\big(A(\omega_{t,\eta},\omega_0)\big)=F_0+d(A+t\eta)=F+t\,d\eta\qquad\text{(since }dA=F-F_0\text{ and }d\text{ is }\mathbb R\text{-linear).}$$
> Thus $F(\omega_{t,\eta})=F+t\,d\eta$ and $A(\omega_{t,\eta},\omega_0)=A+t\eta$, the two facts driving the computation.
>
> **Step 1 — expand the action as a polynomial in $t$.** Split $L=L_1+L_2$ with $L_1(\omega)=\tfrac12 F\wedge\star F$ and $L_2(\omega)=A\wedge J$. Substituting and using $\mathbb R$-linearity of $\star$,
> $$L_1(\omega_{t,\eta})=\tfrac12(F+t\,d\eta)\wedge\star(F+t\,d\eta)=\tfrac12\Big(F\wedge\star F+t\,(d\eta\wedge\star F+F\wedge\star d\eta)+t^2\,d\eta\wedge\star d\eta\Big).$$
> By Lemma 3 (symmetry of the star pairing, property (4) with $p=1$ on two-forms), $F\wedge\star d\eta=d\eta\wedge\star F$, so the two linear cross terms coincide and
> $$L_1(\omega_{t,\eta})=\tfrac12 F\wedge\star F+t\,(d\eta\wedge\star F)+\tfrac{t^2}{2}\,d\eta\wedge\star d\eta\qquad\text{(Lemma 3; the factor }\tfrac12\text{ cancels against the doubled cross term).}$$
> For the coupling term,
> $$L_2(\omega_{t,\eta})=(A+t\eta)\wedge J=A\wedge J+t\,(\eta\wedge J)\qquad\text{(distributivity of }\wedge\text{).}$$
> Adding,
> $$L(\omega_{t,\eta})=\underbrace{\big(\tfrac12 F\wedge\star F+A\wedge J\big)}_{=\,L(\omega)}+t\,\underbrace{\big(d\eta\wedge\star F+\eta\wedge J\big)}_{=:\,\xi}+t^2\,\underbrace{\big(\tfrac12 d\eta\wedge\star d\eta\big)}_{=:\,\theta},$$
> where $\xi,\theta\in\Omega^4(M;\mathbb R)$ are fixed forms, each supported in $\operatorname{supp}\eta\subset U$ (every summand carries a factor supported there).
>
> **Step 2 — differentiate under the integral.** Integrating over $\bar U$ (all integrands smooth and compactly supported, so all integrals are finite),
> $$\int_{\bar U}L(\omega_{t,\eta})=\int_{\bar U}L(\omega)+t\int_{\bar U}\xi+t^2\int_{\bar U}\theta,$$
> which is a genuine quadratic polynomial in $t$ with constant real coefficients $\int_{\bar U}L(\omega)$, $\int_{\bar U}\xi$, $\int_{\bar U}\theta$. No convergence theorem is needed to differentiate a polynomial: its $t$-derivative at $t=0$ is the linear coefficient. Hence
> $$\frac{d}{dt}\Big|_{t=0}\int_{\bar U}L(\omega_{t,\eta})=\int_{\bar U}\xi=\int_{\bar U}\big(d\eta\wedge\star F+\eta\wedge J\big).$$
>
> **Step 3 — extend to $M$ and integrate by parts.** Both summands of $\xi$ are supported in $\operatorname{supp}\eta\subset U\subset\bar U$, so integrating over $\bar U$ equals integrating over $M$:
> $$\int_{\bar U}\xi=\int_M d\eta\wedge\star F+\int_M\eta\wedge J.$$
> By Lemma 2 (integration by parts for the star pairing, using that $M$ is boundaryless and $\eta$ is compactly supported), $\int_M d\eta\wedge\star F=\int_M\eta\wedge d\star F$. Therefore
> $$\frac{d}{dt}\Big|_{t=0}\int_{\bar U}L(\omega_{t,\eta})=\int_M\eta\wedge d\star F+\int_M\eta\wedge J=\int_M\eta\wedge\big(d\star F+J\big),\qquad(\dagger)$$
> the last equality by distributivity of the wedge product over addition. Note that $(\dagger)$ holds for every choice of $U\Subset M$ and every $\eta\in\Omega^1(M;\mathbb R)$ with $\operatorname{supp}\eta\subset U$; since every compactly supported one-form has its support inside some such $U$ (take $U$ a relatively compact open neighbourhood of the support), $(\dagger)$ holds for every $\eta\in\Omega^1_c(M;\mathbb R)$.
>
> **Direction 1 ($\Leftarrow$): if $d\star F+J=0$ then $\omega$ is critical.** Suppose $d\star F+J=0$. Then for every $\eta\in\Omega^1_c(M;\mathbb R)$ the right-hand side of $(\dagger)$ is $\int_M\eta\wedge0=0$, so the first variation vanishes for every admissible $U$ and $\eta$. By definition $\omega$ is critical for $L$.
>
> **Direction 2 ($\Rightarrow$): if $\omega$ is critical then $d\star F+J=0$.** Suppose $\omega$ is critical. Then by definition the left-hand side of $(\dagger)$ is zero for every admissible $U$ and $\eta$, hence
> $$\int_M\eta\wedge\big(d\star F+J\big)=0\qquad\text{for every }\eta\in\Omega^1_c(M;\mathbb R).$$
> Set $\beta:=d\star F+J\in\Omega^3(M;\mathbb R)$ (a three-form on the four-manifold $M$). The displayed identity is exactly the hypothesis of Lemma 1 (the fundamental lemma for the wedge pairing, with $n=4$), so Lemma 1 gives $\beta=0$, that is, $d\star F+J=0$.
>
> **Conclusion.** Both directions hold, so $\omega$ is critical for $L$ if and only if $d\star F+J=0$. This is the inhomogeneous Maxwell equation of [[Def - Maxwell Equations in Form Language|the Maxwell-equations page]]. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The scalar wave equation from a variational principle.** On an oriented Lorentzian manifold consider a real scalar field $\phi$ with action $S(\phi)=\int_M\big(\tfrac12\,d\phi\wedge\star d\phi-\phi\,\rho\big)$, where $\rho\in\Omega^n(M;\mathbb R)$ is a fixed source top-form. Varying $\phi$ by $t\psi$ ($\psi\in C^\infty_c(M)$) reproduces the present skeleton with $d\phi$ in the role of $F$: the quadratic term contributes $\int d\psi\wedge\star d\phi=\int\psi\,d\star d\phi$ after integration by parts, and the fundamental lemma in degrees $0/n$ yields $d\star d\phi-\rho=0$, the covariant wave (or, in Riemannian signature, Poisson) equation. The theorem applies because the configuration space is affine (a vector space of functions) and the field strength $d\phi$ varies by the exact form $t\,d\psi$; it is non-obvious because the "gauge potential" is now a mere function, yet the same Stokes-plus-fundamental-lemma argument is what produces the second-order operator $d\star d$.

**The Yang–Mills equation as the non-abelian copy.** Replace the $U(1)$-bundle by a principal $G$-bundle with a compact structure group carrying an $\operatorname{Ad}$-invariant inner product on its Lie algebra, and the action by $\mathcal{YM}(A)=\tfrac12\int_M\langle F_A\wedge\star F_A\rangle$. Now the curvature varies non-linearly, $F_{A+t a}=F_A+t\,d^A a+O(t^2)$, so the exterior derivative that lands on the test form is the *covariant* one $d^A$, and integration by parts uses the covariant Stokes identity; the Euler–Lagrange equation is $d^A\star F_A=0$. The present theorem is exactly the abelian specialization, where $d^A=d$ and the invariant inner product is a constant multiple of the identity; the point of the exercise is to see which steps survive the non-abelian generalization (the symmetry of the star pairing, the fundamental lemma) and which acquire connection terms (the integration by parts).

**Harmonic forms as critical points of the Dirichlet energy.** On a closed Riemannian manifold, the Dirichlet energy of a $k$-form is $E(\alpha)=\tfrac12\int_M\big(d\alpha\wedge\star d\alpha+\delta\alpha\wedge\star\delta\alpha\big)$, where $\delta$ is the codifferential. Varying $\alpha$ by $t\gamma$ and integrating by parts (now with $\delta$ as the formal adjoint of $d$) produces the Euler–Lagrange equation $(d\delta+\delta d)\alpha=0$, that is, $\Delta\alpha=0$: critical forms are harmonic. This is the same machine — quadratic action in a first-order derivative of the field, vary, integrate by parts, apply the fundamental lemma — and the exercise is to run it carefully and recognize the Hodge Laplacian as the operator produced, the elliptic cousin of the hyperbolic $d\star d$ of electrodynamics.

---

# Bridges

- **The homogeneous versus inhomogeneous split.** The two Maxwell pairs sit on opposite sides of a single conceptual divide that this page makes precise. The homogeneous pair $dF=0$ (Gauss for magnetism, Faraday) is the [[Thm - Bianchi Identity for a Principal Connection|Bianchi identity]], true of every connection with no variation required; the inhomogeneous pair $d\star F+J=0$ (Coulomb, Ampère) is the Euler–Lagrange equation, singled out by stationarity of the action. The construction is: write $F$ as a curvature so that $dF=0$ is automatic, then impose $d\star F+J=0$ dynamically. The coordinate translation of both is carried out on [[Thm - Maxwell Equations in Coordinates|the coordinate page]].

- **Charge conservation as a corollary.** Applying $d$ to the field equation gives $dJ=-d(d\star F)=0$ by $d^2=0$. This is the whole content of [[Thm - Continuity Equation and Conservation of Charge|the continuity-equation page]]: the current is closed on shell, which in coordinates is $\partial_t\varrho+\operatorname{div}\vec j=0$, and integrating over a spatial region with Stokes gives conservation of total charge. The bridge is that the dynamical equation forces its own source to be conserved, so consistency of Maxwell's equations with an arbitrary non-conserved current is impossible.

- **From the field equation to the Lorentz force.** This page governs how the field responds to sources; its companion [[Thm - The Lorentz Force Law from the Equation of Motion|Lorentz-force page]] governs how a charged particle responds to the field, via the equation of motion $\frac{\nabla}{d\tau}c'+F(c',\cdot)^\sharp=0$. Together they close the loop of classical electrodynamics: fields determine trajectories through the Lorentz force, and charges determine fields through the Euler–Lagrange equation derived here.

- **The component-language derivation.** The same result, phrased with indices and the field tensor $F_{\mu\nu}$, is [[Thm - Maxwell Equations from a Principle of Least Action|Maxwell equations from a principle of least action]] in Special Relativity XXII; that page varies $\int(-\tfrac1{4\mu_0}F_{\mu\nu}F^{\mu\nu}+A_\mu j^\mu)$ and obtains $\partial_\mu F^{\mu\nu}=\mu_0 j^\nu$. The construction bridging the two is the Hodge-star dictionary $\star_B=-\star_V$ on Minkowski together with the signature change $g_B=-g_{\mathrm{SR}}$; the abstract $d\star F+J=0$ and the indexed $\partial_\mu F^{\mu\nu}=\mu_0 j^\nu$ are the same equation read in the two languages.

---

# Unlocked by This

> [!tip] Yang–Mills Equation *(from Gauge Theory)*
> Replacing the abelian curvature $F$ by the curvature $F_A$ of a connection on a principal $G$-bundle and the density $\tfrac12 F\wedge\star F$ by $\tfrac12\langle F_A\wedge\star F_A\rangle$ with an $\operatorname{Ad}$-invariant inner product, the same variational argument, with $d$ upgraded to the covariant $d^A$, produces the Yang–Mills equation $d^A\star F_A=0$. The abelian case proved here is the model whose every step the non-abelian derivation imitates. See **Yang–Mills Fields and Instantons** (§7.4).

> [!tip] Field Equations of Any First-Order Quadratic Theory *(from Field Theory)*
> The three-move template isolated here — expand the quadratic action as a polynomial in the variation parameter, use the symmetry of the star pairing to combine cross terms, integrate by parts and invoke the fundamental lemma — derives the field equation of any Lagrangian of the shape $\int(\tfrac12\,\Phi\wedge\star\Phi+\text{linear source coupling})$ with $\Phi$ a curvature. It is the reason such theories are always second order in the potential and first order in the star of the curvature.
