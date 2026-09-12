---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Electromagnetic Lagrangian and Action"
  - "Def - Gauge Transformation"
  - "Thm - Gauge Transformations Act on Connections and Curvature"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $M$ is an oriented Lorentzian $4$-manifold of signature $(-,+,+,+)$, so that its metric $g$ has index $p=1$; we work in geometrised units $c=1$ and take the test charge to be of unit magnitude. We write $\pi\colon P\to M$ for a **[[Def - Principal G-Bundle|principal U(1)-bundle]]** over $M$, with the group $U(1)=\{z\in\mathbb C:\lvert z\rvert=1\}$ acting on $P$ on the right; its Lie algebra is $\mathfrak u(1)=i\mathbb R$, which is abelian ($[X,Y]=0$ for all $X,Y\in i\mathbb R$). The set of **[[Def - Connection on a Principal Bundle|principal connections]]** on $P$ is denoted $\mathcal C(P)$; a connection is a $\mathfrak u(1)$-valued $1$-form $\omega\in\Omega^1(P;i\mathbb R)$ that reproduces the fundamental fields and is $\operatorname{Ad}$-equivariant. The **[[Def - Gauge Transformation|gauge group]]** $\mathcal G(P)$ is the group of bundle automorphisms $\phi\colon P\to P$ that cover the identity of $M$ (so $\pi\circ\phi=\pi$) and are $U(1)$-equivariant ($\phi(p\cdot z)=\phi(p)\cdot z$ for all $p\in P$, $z\in U(1)$).

We fix once and for all a **background connection** $\omega_0\in\mathcal C(P)$ and a **[[Def - Charge-Current 3-Form|charge–current 3-form]]** $J\in\Omega^3(M;\mathbb R)$. To a connection $\omega\in\mathcal C(P)$ the electromagnetic dictionary attaches (all of this is the content of **[[Def - U(1) Gauge Field and Electromagnetic Connection|Def - U(1) Gauge Field and Electromagnetic Connection]]**):

- its **descended curvature** $\bar\Omega\in\Omega^2(M;i\mathbb R)$: because $U(1)$ is abelian the pullback $s^*\Omega$ of the curvature $\Omega=d\omega$ of $\omega$ along a local section $s\colon U\to P$ is independent of $s$ and the local pieces glue to a single global $2$-form $\bar\Omega$ on $M$;
- the **field strength** $F\in\Omega^2(M;\mathbb R)$, defined by $\bar\Omega=iF$; it satisfies $dF=0$ by the Bianchi identity;
- the **potential relative to $\omega_0$**, the real $1$-form $A=A(\omega,\omega_0)\in\Omega^1(M;\mathbb R)$ determined by $iA=s^*(\omega-\omega_0)$ for any local section $s$ (again section-independent), which satisfies $dA=F-F_0$ where $F_0$ is the field strength of $\omega_0$.

The **[[Def - Hodge Star in Arbitrary Signature|Hodge star]]** $\star\colon\Omega^k(M;\mathbb R)\to\Omega^{4-k}(M;\mathbb R)$ is taken in Bär's convention throughout the series: it is the unique linear map with $\alpha\wedge\beta=\langle\star\alpha,\beta\rangle\,\mathrm{vol}$ for all $\alpha\in\Lambda^kT_x^*M$, $\beta\in\Lambda^{4-k}T_x^*M$, where $\langle\cdot,\cdot\rangle$ is the induced (indefinite) inner product on forms and $\mathrm{vol}$ the metric volume form. The **[[Def - Electromagnetic Lagrangian and Action|electromagnetic Lagrangian]]** is
$$L\colon\mathcal C(P)\longrightarrow\Omega^4(M;\mathbb R),\qquad L(\omega)=L_1(\omega)+L_2(\omega),\quad L_1(\omega)=\tfrac12\,F\wedge\star F,\quad L_2(\omega)=A\wedge J,$$
with $F=F(\omega)$ and $A=A(\omega,\omega_0)$ as above. By property (4) of the star in index $p=1$ (below), $L_1(\omega)=\tfrac12(-1)^p\langle F,F\rangle\,\mathrm{vol}=-\tfrac12\langle F,F\rangle\,\mathrm{vol}$, so $L$ is genuinely real-valued.

A connection $\omega$ is called **critical** for $L$ when, for every precompact open set $U\Subset M$ and every $\eta\in\Omega^1(M;\mathbb R)$ with $\operatorname{supp}\eta\subset U$,
$$\frac{d}{dt}\Big|_{t=0}\int_{\bar U}L(\omega_{t,\eta})=0,\qquad\text{where }\omega_{t,\eta}\in\mathcal C(P)\text{ is the connection with }A(\omega_{t,\eta},\omega_0)=A(\omega,\omega_0)+t\eta,$$
so that $F(\omega_{t,\eta})=F(\omega)+t\,d\eta$; the family $\omega_{t,\eta}$ exists because $\mathcal C(P)$ is an affine space modelled on $\Omega^1(M;i\mathbb R)$ (**[[Thm - The Space of Connections is an Affine Space|Thm - The Space of Connections is an Affine Space]]**). The left Maurer–Cartan form of $U(1)$ is $\theta\in\Omega^1(U(1);i\mathbb R)$; for $U(1)\subset\mathbb C^\times$ it is $\theta=z^{-1}\,dz$ (**[[Def - The Maurer-Cartan Form|Def - The Maurer-Cartan Form]]**).

> [!warning] Convention: Hodge star and Lorentzian signature
> This page uses Bär's Hodge star $\star=\star_B$, fixed by $\alpha\wedge\beta=\langle\star\alpha,\beta\rangle\,\mathrm{vol}$, which relates to the vault's Riemannian operator $\star_V$ of **[[Def - The Hodge Star Operator|Def - The Hodge Star Operator]]** by $\star_B=(-1)^p\star_V$ on $k$-forms of a space of index $p$. The other common defining relation $\alpha\wedge\star'\beta=\langle\alpha,\beta\rangle\,\mathrm{vol}$ produces $\star'=(-1)^{k(n-k)}\star_V$, which differs from $\star_B$ in general but agrees with it on $2$-forms in dimension four. Nothing in the gauge-invariance argument depends on the choice: the only property of $\star$ used below is that it is a fixed linear operator determined by the metric $g$, so that $F'=F$ forces $\star F'=\star F$.

> [!warning] Convention: the special-relativity pages
> The special-relativity chapters (`Def - The Electromagnetic Field Tensor`, `Def - The Four-Potential`, `Def - The Electric Four-Current`) use signature $(+,-,-,-)$ and SI units with $c$ explicit; the dictionary is $g_B=-g_{\mathrm{SR}}$, the same $2$-form $F$, the same fields $\vec E,\vec B$, and $\star_B=-\star_V$ on Minkowski space. The gauge transformation $A\mapsto A+d\chi$ derived below is exactly the classical gauge freedom of the four-potential recorded there in `Def - Gauge Choice and the Lorenz Gauge`.

> [!warning] Convention: the symbol $g$
> Bär writes the Lagrangian as $L_1(\omega,g)$ to display its dependence on the metric $g$, and simultaneously writes a gauge transformation of an abelian bundle as $p\mapsto p\cdot g(\pi(p))$ with a group-valued function $g$. To avoid the clash we reserve $g$ for the Lorentzian metric and write the $U(1)$-valued function of a gauge transformation as $u\colon M\to U(1)$.

---

# Statement

> **Theorem (gauge invariance of the electromagnetic Lagrangian).** Let $M$ be an oriented Lorentzian $4$-manifold with metric $g$, let $\pi\colon P\to M$ be a principal $U(1)$-bundle, fix a background connection $\omega_0\in\mathcal C(P)$ and a charge–current $3$-form $J\in\Omega^3(M;\mathbb R)$, and let $L=L_1+L_2$ be the electromagnetic Lagrangian. Let $\phi\in\mathcal G(P)$ be a gauge transformation and put $\omega':=\phi^*\omega$, decorating the associated objects with a prime ($\bar\Omega'$, $F'$, $A'=A(\phi^*\omega,\omega_0)$). Then:
>
> **(A) The field strength is gauge-invariant.** $\bar\Omega'=\bar\Omega$, hence $F'=F$; consequently, for every fixed metric $g$,
> $$L_1(\phi^*\omega)=\tfrac12\,F'\wedge\star F'=\tfrac12\,F\wedge\star F=L_1(\omega)\qquad\text{as $4$-forms on }M.$$
>
> **(B) The coupling term changes by an $\omega$-independent closed form.** Writing $\phi(p)=p\cdot u(\pi(p))$ for the unique smooth function $u\colon M\to U(1)$ representing $\phi$, the potential changes by
> $$A(\phi^*\omega,\omega_0)-A(\omega,\omega_0)=\mu_u,\qquad \mu_u:=\tfrac1i\,u^{-1}\,du\in\Omega^1(M;\mathbb R),$$
> where $\mu_u$ is a **closed** real $1$-form that depends only on $u$ — not on $\omega$ and not on $\omega_0$. Hence
> $$L_2(\phi^*\omega)-L_2(\omega)=\mu_u\wedge J.$$
>
> **(C) Criticality is always preserved; the action is invariant for gauge transformations generated by a function.** The connection $\omega$ is critical for $L$ if and only if $\phi^*\omega$ is critical for $L$. If moreover $dJ=0$ and $\phi$ is generated by a function — that is, $\phi(p)=p\cdot e^{i\chi(\pi(p))}$ for some $\chi\in C^\infty(M)$ with $\operatorname{supp}\chi\subset U$ for a precompact open $U\Subset M$ — then $\mu_u=d\chi$ and
> $$\int_{\bar U}L(\phi^*\omega)=\int_{\bar U}L(\omega).$$

---

# Motivation

Electrodynamics is the statement that the electromagnetic field is a connection $\omega$ on a principal $U(1)$-bundle and that the physical laws are the critical points of the action $\int L(\omega)$. But a connection carries more information than the physics can possibly detect: two connections that differ by a gauge transformation $\phi\in\mathcal G(P)$ describe, by construction, the *same* geometry seen through a different bundle automorphism. If the theory is to be about geometry and not about the arbitrary choice of automorphism, the observable content of $L$ — at the very least the equations of motion it produces — must be blind to the replacement $\omega\rightsquigarrow\phi^*\omega$. This theorem is the verification that it is, and the identification of exactly which part of $L$ is invariant on the nose and which part is invariant only after integration.

The result also settles a puzzle that the definition of $L$ deliberately left open. The coupling term $L_2=A\wedge J$ is written with the potential $A$, and $A$ is manifestly *not* gauge-invariant: under $\omega\rightsquigarrow\phi^*\omega$ it acquires an additive term. A naive reader would conclude that the action, and therefore the physics, depends on the unphysical potential. The resolution — and the technical heart of the theorem — is that the extra term $A$ picks up is a *fixed* $1$-form $\mu_u$ determined by $\phi$ alone, so that when we vary $\omega$ to find the critical points the extra term contributes nothing to the variation. The Euler–Lagrange equation, $d\star F+J=0$, is gauge-invariant even though the functional whose critical points it describes is not, in the strict pointwise sense, gauge-invariant. This is the first appearance in the series of a phenomenon that recurs throughout gauge theory and quantum field theory: a Lagrangian that changes by a total derivative under a symmetry still produces a symmetric theory.

Finally, the abelian case is the clean prototype for the non-abelian Yang–Mills theory of §7.4. There the field strength is *not* invariant but only $\operatorname{Ad}$-equivariant, $\bar\Omega'=\operatorname{Ad}_{u^{-1}}\bar\Omega$, and gauge invariance of the Yang–Mills Lagrangian $\tfrac12\lVert\bar\Omega\rVert^2$ rests instead on the $\operatorname{Ad}$-invariance of the inner product on $\mathfrak g$. Seeing here, in the simplest setting, precisely where invariance comes from — the triviality of $\operatorname{Ad}$ for an abelian group — is what makes the non-abelian generalisation legible.

---

# Sources and Targets

**Sources (Input Broadening).** The theorem's literal hypothesis is mild: any $\phi\in\mathcal G(P)$ over any $U(1)$-bundle. The real question is when a problem hands one a gauge transformation, or an object that behaves like one, without saying so.

The first disguised source is **a nowhere-vanishing complex function or a change of local trivialisation**. Whenever electrodynamics is written in a trivialisation of $P$ and one passes to another trivialisation, the transition is exactly multiplication by a smooth $u\colon M\to U(1)$, and the potential picks up $\mu_u=\tfrac1i u^{-1}du$. Recognising a change of trivialisation as an instance of the theorem tells one immediately that the field strength is unchanged and the equations of motion survive. *Example problem:* on the two hemispheres of $S^2$ the Dirac monopole potential is given by two expressions differing by $\tfrac1i u^{-1}du$ with $u=e^{2ig\varphi}$; the theorem guarantees the two local descriptions define one and the same physics, and quantisation of $g$ is the obstruction to $u$ extending to a global function.

The second disguised source is **a symmetry of the physical fields realised by a phase rotation of a matter field**. If a charged field $\psi$ is a section of a bundle associated to $P$ and one applies a pointwise phase $\psi\mapsto e^{i\chi}\psi$, the compatible transformation of the connection is precisely $\omega\rightsquigarrow\phi^*\omega$ with $\phi$ generated by $\chi$. The non-obvious bridge is that a transformation invented on the matter side forces a definite transformation on the gauge side, and this pair is a gauge transformation in the sense of $\mathcal G(P)$. *Example problem:* show that the minimally coupled action $\int(\lvert d^\omega\psi\rvert^2+\tfrac12 F\wedge\star F)$ is invariant under the simultaneous replacement $\psi\mapsto e^{i\chi}\psi$, $A\mapsto A+d\chi$.

The third disguised source is **a closed but non-exact $1$-form on the base**. Given any closed integral real $1$-form $\mu$ on $M$ (that is, $\tfrac1{2\pi}\mu$ has integral periods), there is a smooth $u\colon M\to U(1)$ with $\mu=\tfrac1i u^{-1}du$, hence a gauge transformation with exactly that effect on the potential. The bridge — from a cohomological datum to a bundle automorphism — is the identification of $[M,U(1)]$ with $H^1(M;\mathbb Z)$. *Example problem:* on the spacetime cylinder $S^1\times\mathbb R^3$ produce a "large" gauge transformation whose $\mu_u$ has a nonzero period around the $S^1$, and check that it still preserves criticality even though the action shifts by a nonzero constant.

**Targets (Output Amplification).** The conclusion, combined with further ingredients, does more than protect one Lagrangian.

Combine part (C) with **the Euler–Lagrange equation $d\star F+J=0$** (**[[Thm - Euler-Lagrange Equation of the Electromagnetic Action|Thm - Euler-Lagrange Equation of the Electromagnetic Action]]**). Because criticality is gauge-invariant and criticality is equivalent to Maxwell's inhomogeneous equation, the *space of solutions* of Maxwell's equations is a union of gauge orbits: if $\omega$ solves them so does every $\phi^*\omega$. The amplified statement is that the physically distinct solutions form the quotient $\{\,\omega:d\star F+J=0\,\}/\mathcal G(P)$, which is the first instance of a moduli space of gauge fields.

Combine part (A) with **the Chern–Weil description of the first Chern class** (**[[Thm - First Chern Class of a Line Bundle from Curvature|Thm - First Chern Class of a Line Bundle from Curvature]]**). Since $\bar\Omega'=\bar\Omega$ for every $\phi\in\mathcal G(P)$, the de Rham class $\big[\tfrac1{2\pi}F\big]$ is a gauge invariant, and in fact a topological invariant of $P$ independent even of the choice of connection. The payoff is that the integer $\int_\Sigma\tfrac1{2\pi}F$ over a closed surface $\Sigma$ — the magnetic charge, or the degree of the bundle — cannot be changed by any gauge transformation, which is what makes charge quantisation a robust statement.

Combine part (B) with **conservation of charge, $dJ=0$** (**[[Thm - Continuity Equation and Conservation of Charge|Thm - Continuity Equation and Conservation of Charge]]**). The action shift $\int_{\bar U}\mu_u\wedge J$ then equals $\int_{\bar U}d(\chi J)$ for a function-generated transformation, a pure boundary term; its vanishing for compactly supported $\chi$ is exactly the on-shell gauge invariance of the coupled action. The amplified statement is the equivalence, familiar from Noether's theorem, between the gauge invariance of the matter coupling and the conservation of the current it couples to.

---

# Why Is It True

Strip away the formalism and ask what a gauge transformation of an abelian bundle actually does. Because $U(1)$ is commutative, an automorphism $\phi$ covering the identity is nothing more than "multiply the fibre over $x$ by a phase $u(x)\in U(1)$", uniformly in the fibre direction. A connection is a rule for infinitesimal parallel transport; rescaling every fibre by a phase $u(x)$ tilts that rule by the derivative of the phase, and by nothing else. So the potential — the local record of the connection — shifts by the logarithmic derivative $\tfrac1i u^{-1}du$ of the phase, precisely the classical gauge freedom $A\mapsto A+d\chi$ when $u=e^{i\chi}$.

Now the two halves of the Lagrangian respond to this shift in opposite ways, and the reason is a single algebraic fact. The field strength $F=dA$ (relative to the background) is the derivative of the potential, and the shift $\mu_u=\tfrac1i u^{-1}du$ that the potential absorbs is *closed*: $d\mu_u=0$. A closed shift dies under $d$, so the field strength does not move at all. This is the whole of part (A):

> **Abelian curvature is gauge-invariant on the nose because the gauge shift of the potential is a closed form, and the field strength is the exterior derivative of the potential — which annihilates closed forms.**

The coupling term $L_2=A\wedge J$, by contrast, sees $A$ directly and therefore feels the shift: it changes by $\mu_u\wedge J$. But here the crucial observation is not that this term vanishes — in general it does not — but that it is a *fixed* form, the same for every connection $\omega$, because $\mu_u$ depends only on $\phi$. When we vary $\omega$ to test criticality, a term that does not move with $\omega$ contributes zero to the derivative. So criticality — the physics — cannot tell $\omega$ from $\phi^*\omega$, even though the numerical value of the action can. Only when $\mu_u$ is exact and the current is conserved does the shift $\int\mu_u\wedge J=\int d(\chi J)$ integrate to zero and the action itself become invariant.

The mechanism divides cleanly along the abelian/non-abelian line. What makes $F$ invariant *pointwise* is that $\operatorname{Ad}$ is trivial for $U(1)$; when the group is non-abelian the field strength only transforms by $\operatorname{Ad}_{u^{-1}}$, and one must instead invoke the invariance of the fibre inner product to protect the Lagrangian. The abelian case is where the two roles — invariance of the field and invariance of the norm — happen to coincide.

---

# What Makes This Hard

The subtle point is that the Lagrangian is *not* pointwise gauge-invariant, so the honest statement is a statement about criticality, not about the value of the action; conflating the two leads either to a false claim ("$L$ is invariant") or to a false worry ("the physics depends on $A$"). The correct discrimination is that $L_1$ is invariant as a $4$-form while $L_2$ changes by the fixed form $\mu_u\wedge J$, and that this fixed shift drops out of the *variation* precisely because it does not depend on the connection being varied. The second trap is topological: one is tempted to write $u=e^{i\chi}$ globally and treat $\mu_u$ as exact, but a smooth $u\colon M\to U(1)$ need not have a global logarithm — it does so only when its class in $H^1(M;\mathbb Z)$ vanishes — so $\mu_u$ is only closed, not exact, and the action shift $\int\mu_u\wedge J$ can be a nonzero constant for "large" gauge transformations. Recognising that criticality survives even then, while the action value need not, is the crux.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Represent the gauge transformation by a phase function $u\colon M\to U(1)$, compute how the local connection form and hence the potential and the descended curvature change, and read off the three parts. Part (A) is "the shift is closed, and $d$ kills it"; part (B) is "the shift is $\omega$-independent"; part (C) chains (A) and (B) through the definition of criticality, with a Stokes argument for the extra action-invariance clause.

**Subgoal decomposition:**

1. **Represent $\phi$ by a base function.** Show every $\phi\in\mathcal G(P)$ over a $U(1)$-bundle is $\phi(p)=p\cdot u(\pi(p))$ for a unique smooth $u\colon M\to U(1)$, and that $\phi\circ s=s\cdot u$ for any local section $s$.
   - *Hint:* Define $u(p)$ by $\phi(p)=p\cdot u(p)$ using freeness and transitivity of the fibre action; equivariance plus commutativity makes $u$ constant on fibres.
   - *Why needed:* Every later computation is done at the base level through $u$.

2. **Compute the shift of the local connection form.** Show $s^*(\phi^*\omega)=s^*\omega+u^{-1}\,du$, hence $A(\phi^*\omega,\omega_0)-A(\omega,\omega_0)=\mu_u=\tfrac1i u^{-1}du$, and that $\mu_u$ is real and independent of $\omega,\omega_0$.
   - *Hint:* $s^*(\phi^*\omega)=(\phi\circ s)^*\omega=(s\cdot u)^*\omega$; apply the change-of-section law with $\operatorname{Ad}$ trivial.
   - *Why needed:* This is the single computation underlying both (A) and (B).

3. **Show the shift is closed.** Prove $d(u^{-1}du)=0$, so $\mu_u$ is a closed $1$-form.
   - *Hint:* Either differentiate $u^{-1}u=1$, or pull back the Maurer–Cartan structure equation $d\theta=0$ of $U(1)$.
   - *Why needed:* Closedness is exactly what makes the curvature invariant in (A).

4. **Deduce (A) and (B).** From subgoals 2–3: $\bar\Omega'=\bar\Omega$ (curvature is $d$ of the potential locally, and $d\mu_u=0$), hence $F'=F$ and $L_1$ is invariant; and $L_2(\phi^*\omega)-L_2(\omega)=\mu_u\wedge J$.
   - *Hint:* Use the abelian local structure equation $\bar\Omega|_U=d(s^*\omega)$.
   - *Why needed:* These are parts (A) and (B).

5. **Chain into criticality (C).** Show the variation families are intertwined, $A(\phi^*\omega_{t,\eta},\omega_0)=A(\phi^*\omega,\omega_0)+t\eta$, and that $L(\phi^*\omega_{t,\eta})=L(\omega_{t,\eta})+\mu_u\wedge J$ with a $t$-independent last term; differentiate. For the action clause, when $\mu_u=d\chi$ and $dJ=0$ use Stokes on $\chi J$.
   - *Hint:* $\mu_u\wedge J$ carries no $t$, so its $t$-derivative is zero; the two criticality conditions are literally equal.
   - *Why needed:* This is part (C), the physical payoff.

---

# Lemma Decomposition

> [!note]- Lemma 1: A gauge transformation of a $U(1)$-bundle is a base-valued phase
> **Statement:** Let $\pi\colon P\to M$ be a principal $U(1)$-bundle and $\phi\in\mathcal G(P)$. Then there is a unique smooth function $u\colon M\to U(1)$ with $\phi(p)=p\cdot u(\pi(p))$ for all $p\in P$. Moreover, for every local section $s\colon U\to P$ one has $\phi\circ s=s\cdot u$ as sections over $U$ (that is, $(\phi\circ s)(x)=s(x)\cdot u(x)$).
>
> **Hint:** Define a fibrewise phase by freeness of the action, then use equivariance and commutativity of $U(1)$ to see it is constant on fibres.
>
> **Why needed:** It converts the automorphism $\phi$ of the total space into a function on the base, so that the whole argument can be run through local connection forms on $M$.
>
> > [!note]- Full proof
> > **Step 0 — the fibrewise phase exists and is unique.** Fix $p\in P$. Since $\phi$ covers the identity, $\pi(\phi(p))=\pi(p)$, so $\phi(p)$ lies in the same fibre as $p$. By the definition of a principal bundle (**[[Def - Principal G-Bundle|Def - Principal G-Bundle]]**) the right action of $U(1)$ on each fibre is free and transitive; hence there is a unique $u(p)\in U(1)$ with
> > $$\phi(p)=p\cdot u(p)\qquad\text{(transitivity gives existence, freeness gives uniqueness).}$$
> >
> > **Step 1 — the phase is constant on fibres.** Let $z\in U(1)$. Applying the defining relation at the point $p\cdot z$ and using equivariance of $\phi$,
> > $$(p\cdot z)\cdot u(p\cdot z)=\phi(p\cdot z)=\phi(p)\cdot z=(p\cdot u(p))\cdot z\qquad\text{(definition of }u\text{; }\phi(p\cdot z)=\phi(p)\cdot z\text{; definition of }u\text{).}$$
> > The two ends are $p\cdot\big(z\,u(p\cdot z)\big)$ and $p\cdot\big(u(p)\,z\big)$ by associativity of the action, so freeness of the action forces
> > $$z\,u(p\cdot z)=u(p)\,z\qquad\text{(freeness).}$$
> > Because $U(1)$ is abelian, $z\,u(p\cdot z)=u(p\cdot z)\,z$, and cancelling $z$ (a group element, hence invertible) gives $u(p\cdot z)=u(p)$. Thus $u$ is constant along each fibre and descends to a function $u\colon M\to U(1)$ with $u(\pi(p))=u(p)$; renaming, $\phi(p)=p\cdot u(\pi(p))$.
> >
> > **Step 2 — smoothness.** The division map $\delta\colon P\times_M P\to U(1)$, sending a pair $(p,q)$ in the same fibre to the unique group element $\delta(p,q)$ with $q=p\cdot\delta(p,q)$, is smooth: this is part of the principal-bundle structure, since in a local trivialisation $P|_U\cong U\times U(1)$ the action is $(x,a)\cdot z=(x,az)$ and $\delta((x,a),(x,b))=a^{-1}b$, a smooth function. For a local section $s\colon U\to P$ we have $u(x)=\delta\big(s(x),\phi(s(x))\big)$, a composite of smooth maps, so $u$ is smooth on $U$; as $U$ was an arbitrary chart of a bundle atlas, $u$ is smooth on $M$.
> >
> > **Step 3 — the section identity.** For $x\in U$, $(\phi\circ s)(x)=\phi(s(x))=s(x)\cdot u(\pi(s(x)))=s(x)\cdot u(x)$, since $\pi\circ s=\operatorname{id}_U$. Therefore $\phi\circ s=s\cdot u$ as sections over $U$. $\blacksquare$

> [!note]- Lemma 2: The potential shifts by $\mu_u=\tfrac1i u^{-1}du$, independently of the connection
> **Statement:** With $\phi\in\mathcal G(P)$ represented by $u\colon M\to U(1)$ as in Lemma 1, and for any connection $\omega\in\mathcal C(P)$ and local section $s\colon U\to P$,
> $$s^*(\phi^*\omega)=s^*\omega+u^{-1}\,du\quad\text{on }U.$$
> Consequently $A(\phi^*\omega,\omega_0)-A(\omega,\omega_0)=\mu_u$, where $\mu_u:=\tfrac1i\,u^{-1}du\in\Omega^1(M;\mathbb R)$ is a real $1$-form depending only on $u$ (not on $\omega$ or $\omega_0$).
>
> **Hint:** Rewrite $s^*(\phi^*\omega)=(\phi\circ s)^*\omega=(s\cdot u)^*\omega$ and use the change-of-section law with $\operatorname{Ad}$ trivial.
>
> **Why needed:** This is the one computation the whole theorem turns on; it feeds both the curvature invariance (A) and the coupling change (B).
>
> > [!note]- Full proof
> > **Step 0 — the transformation law we invoke.** For a principal $G$-bundle, two local sections related by $s'=s\cdot h$ with a smooth $h\colon U\to G$ have connection forms related by
> > $$s'^*\omega=\operatorname{Ad}_{h^{-1}}\!\big(s^*\omega\big)+h^*\theta,$$
> > where $\theta$ is the left Maurer–Cartan form of $G$; this is the statement of **[[Thm - Transformation of Local Connection and Curvature Forms|Thm - Transformation of Local Connection and Curvature Forms]]**. For $G=U(1)$ the adjoint representation is trivial, $\operatorname{Ad}_{h^{-1}}=\operatorname{id}$ (indeed for an abelian group $g h g^{-1}=h$, so $\operatorname{Ad}_g=\operatorname{id}$), and $h^*\theta=h^{-1}\,dh$ because $\theta=z^{-1}dz$ on $U(1)\subset\mathbb C^\times$.
> >
> > **Step 1 — apply it to $s'=s\cdot u$.** By Lemma 1, $\phi\circ s=s\cdot u$. Naturality of pullback under composition gives $s^*(\phi^*\omega)=(\phi\circ s)^*\omega=(s\cdot u)^*\omega$. Taking $h=u$ in Step 0,
> > $$s^*(\phi^*\omega)=(s\cdot u)^*\omega=\operatorname{Ad}_{u^{-1}}\!\big(s^*\omega\big)+u^*\theta=s^*\omega+u^{-1}\,du\qquad\text{(change-of-section law; }\operatorname{Ad}_{u^{-1}}=\operatorname{id}\text{; }u^*\theta=u^{-1}du\text{).}$$
> >
> > **Step 1' — reality of $u^{-1}du$ scaled by $1/i$.** The form $u^{-1}du$ takes values in $\mathfrak u(1)=i\mathbb R$: differentiating $\lvert u\rvert^2=u\bar u=1$ gives $\bar u\,du+u\,d\bar u=0$, so $\overline{u^{-1}du}=\bar u^{-1}d\bar u=u\,d\bar u=-\bar u\,du=-\,u^{-1}du$, i.e. $u^{-1}du$ is purely imaginary. Hence $\mu_u:=\tfrac1i u^{-1}du$ is real, $\mu_u\in\Omega^1(M;\mathbb R)$.
> >
> > **Step 2 — pass to the potential.** By the definition of the potential relative to $\omega_0$ (Notation), $iA(\omega,\omega_0)=s^*(\omega-\omega_0)=s^*\omega-s^*\omega_0$. The same section $s$ computes both potentials, so
> > $$iA(\phi^*\omega,\omega_0)=s^*(\phi^*\omega)-s^*\omega_0=\big(s^*\omega+u^{-1}du\big)-s^*\omega_0=iA(\omega,\omega_0)+u^{-1}\,du\qquad\text{(Step 1).}$$
> > Dividing by $i$, $A(\phi^*\omega,\omega_0)=A(\omega,\omega_0)+\tfrac1i u^{-1}du=A(\omega,\omega_0)+\mu_u$. Thus $A(\phi^*\omega,\omega_0)-A(\omega,\omega_0)=\mu_u$.
> >
> > **Step 3 — $\mu_u$ is $\omega$-independent.** The right-hand side $\mu_u=\tfrac1i u^{-1}du$ is built from $u$ alone, and $u$ depends only on $\phi$ (Lemma 1), not on the connection $\omega$ or the background $\omega_0$. Hence the shift $\mu_u$ is the same for every connection. $\blacksquare$

> [!note]- Lemma 3: The gauge shift is a closed $1$-form
> **Statement:** For every smooth $u\colon M\to U(1)$, the $\mathfrak u(1)$-valued $1$-form $u^{-1}du$ is closed, $d(u^{-1}du)=0$; equivalently $d\mu_u=0$.
>
> **Hint:** Differentiate $u^{-1}u=1$, or pull back the Maurer–Cartan structure equation of $U(1)$.
>
> **Why needed:** Closedness of the shift is exactly what makes the field strength gauge-invariant in part (A).
>
> > [!note]- Full proof
> > **Direct computation.** Since $U(1)\subset\mathbb C^\times$ and $\lvert u\rvert=1$, we have $u^{-1}=\bar u$, so $u^{-1}du=\bar u\,du$. Differentiating the identity $\bar u\,u=1$ gives $d\bar u\,u+\bar u\,du=0$, hence $d\bar u=-\bar u^2\,du=-\bar u\,(\bar u\,du)$. Therefore
> > $$d(u^{-1}du)=d(\bar u\,du)=d\bar u\wedge du+\bar u\,d(du)=d\bar u\wedge du\qquad\text{(Leibniz rule; }d(du)=0\text{ since }d^2=0\text{).}$$
> > Here $d(du)=0$ is the identity $d^2=0$ (**[[Thm - d-Squared-is-Zero|Thm - d-Squared-is-Zero]]**).
> > Substituting $d\bar u=-\bar u\,(\bar u\,du)$,
> > $$d\bar u\wedge du=-\bar u^2\,(du\wedge du)=0\qquad\text{(since }du\wedge du=0\text{: any $1$-form wedged with itself vanishes).}$$
> > Thus $d(u^{-1}du)=0$, and $d\mu_u=\tfrac1i d(u^{-1}du)=0$.
> >
> > **Remark (the structural reason).** Intrinsically $u^{-1}du=u^*\theta$ is the pullback of the left Maurer–Cartan form $\theta$ of $U(1)$, which satisfies the Maurer–Cartan structure equation $d\theta+\tfrac12[\theta\wedge\theta]=0$. As $U(1)$ is abelian the bracket term vanishes, so $d\theta=0$; since pullback commutes with the exterior derivative, $d(u^*\theta)=u^*(d\theta)=0$. The direct computation above is this fact written out in the standard coordinate of $\mathbb C$. $\blacksquare$

> [!note]- Lemma 4: A total derivative against a closed current integrates to zero
> **Statement:** Let $\chi\in C^\infty(M)$ with $\operatorname{supp}\chi\subset U$ for a precompact open $U\Subset M$, and let $J\in\Omega^3(M;\mathbb R)$ satisfy $dJ=0$. Then $d\chi\wedge J=d(\chi J)$ and
> $$\int_{\bar U}d\chi\wedge J=\int_M d(\chi J)=0.$$
>
> **Hint:** Leibniz plus $dJ=0$ gives the first identity; Stokes for a compactly supported form gives the second.
>
> **Why needed:** It is the final step of the action-invariance clause of part (C), turning the coupling shift into a boundary term that vanishes.
>
> > [!note]- Full proof
> > **Step 1 — the Leibniz identity.** For a function $\chi$ (a $0$-form) and a $3$-form $J$, the graded Leibniz rule reads $d(\chi J)=d\chi\wedge J+\chi\,dJ$. Since $dJ=0$ by hypothesis, $d(\chi J)=d\chi\wedge J$.
> >
> > **Step 2 — the integral vanishes.** The form $\chi J$ is a $3$-form on the $4$-manifold $M$ with $\operatorname{supp}(\chi J)\subset\operatorname{supp}\chi\subset U$, hence compactly supported. For a compactly supported $(n-1)$-form $\alpha$ on an oriented $n$-manifold without boundary, Stokes' theorem gives $\int_M d\alpha=0$: extend $\alpha$ by zero outside its support and apply **[[Thm - Stokes' Theorem on Manifolds|Thm - Stokes' Theorem on Manifolds]]** on a large coordinate ball $B$ containing $\operatorname{supp}\alpha$ in its interior, so that $\int_M d\alpha=\int_B d\alpha=\int_{\partial B}\alpha=0$ because $\alpha$ vanishes on $\partial B$. Applying this with $\alpha=\chi J$ and $n=4$,
> > $$\int_M d(\chi J)=0.$$
> > Finally, $\int_{\bar U}d\chi\wedge J=\int_{\bar U}d(\chi J)$ by Step 1, and since $\chi J$ is supported inside $U$ the integral over $\bar U$ equals the integral over all of $M$, which is $0$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\phi\in\mathcal G(P)$ and $\omega\in\mathcal C(P)$, and set $\omega'=\phi^*\omega$. By **[[Thm - Gauge Transformations Act on Connections and Curvature|Thm - Gauge Transformations Act on Connections and Curvature]]** the pullback $\phi^*\omega$ is again a principal connection, so $\omega'\in\mathcal C(P)$ and all associated objects $\bar\Omega'$, $F'$, $A'=A(\phi^*\omega,\omega_0)$ are defined. By Lemma 1 write $\phi(p)=p\cdot u(\pi(p))$ with $u\colon M\to U(1)$ smooth.
>
> **Step 0 — the objects are well-posed.** The descended curvature $\bar\Omega$, the field strength $F$ ($\bar\Omega=iF$) and the potential $A(\omega,\omega_0)$ are section-independent global forms on $M$ because $U(1)$ is abelian (Notation, and **[[Def - U(1) Gauge Field and Electromagnetic Connection|Def - U(1) Gauge Field and Electromagnetic Connection]]**); the same holds for the primed objects, so every equality below is between honest global forms on $M$.
>
> **Part (A) — the field strength is gauge-invariant.** Fix a local section $s\colon U\to P$. By the abelian local structure equation (**[[Thm - Structure Equation for the Curvature|Thm - Structure Equation for the Curvature]]** with the bracket term $\tfrac12[s^*\omega\wedge s^*\omega]=0$, since $\mathfrak u(1)$ is abelian), the descended curvature restricts on $U$ to
> $$\bar\Omega|_U=s^*\Omega=d(s^*\omega),\qquad\text{and likewise}\qquad\bar\Omega'|_U=s^*\Omega'=d\big(s^*(\phi^*\omega)\big).$$
> By Lemma 2, $s^*(\phi^*\omega)=s^*\omega+u^{-1}du$, so
> $$\bar\Omega'|_U=d\big(s^*\omega+u^{-1}du\big)=d(s^*\omega)+d(u^{-1}du)=d(s^*\omega)+0=\bar\Omega|_U\qquad\text{(linearity of }d\text{; Lemma 3).}$$
> As $U$ ranges over a cover of $M$ this shows $\bar\Omega'=\bar\Omega$ globally, and dividing by $i$ gives $F'=F$. Since the Hodge star $\star$ is a fixed linear operator determined by the metric $g$ (Notation), $F'=F$ implies $\star F'=\star F$, whence
> $$L_1(\phi^*\omega)=\tfrac12\,F'\wedge\star F'=\tfrac12\,F\wedge\star F=L_1(\omega)\qquad\text{as $4$-forms on }M.$$
> This is part (A).
>
> **Part (B) — the coupling term changes by an $\omega$-independent closed form.** By Lemma 2, $A(\phi^*\omega,\omega_0)-A(\omega,\omega_0)=\mu_u$ with $\mu_u=\tfrac1i u^{-1}du\in\Omega^1(M;\mathbb R)$, and $\mu_u$ depends only on $u$, hence only on $\phi$, not on $\omega$ or $\omega_0$ (Lemma 2, Step 3); it is closed by Lemma 3. Therefore
> $$L_2(\phi^*\omega)-L_2(\omega)=A(\phi^*\omega,\omega_0)\wedge J-A(\omega,\omega_0)\wedge J=\big(A(\phi^*\omega,\omega_0)-A(\omega,\omega_0)\big)\wedge J=\mu_u\wedge J\qquad\text{(bilinearity of }\wedge\text{; Lemma 2).}$$
> This is part (B).
>
> **Part (C) — criticality is preserved, and the action is invariant for a function-generated $\phi$.**
>
> *The variation families are intertwined.* Fix $U\Subset M$ and $\eta\in\Omega^1(M;\mathbb R)$ with $\operatorname{supp}\eta\subset U$, and let $\omega_{t,\eta}$ be the variation with $A(\omega_{t,\eta},\omega_0)=A(\omega,\omega_0)+t\eta$. Because the shift $\mu_u$ is the *same* for every connection (part (B)), applying part (B) to the connection $\omega_{t,\eta}$ gives
> $$A(\phi^*\omega_{t,\eta},\omega_0)=A(\omega_{t,\eta},\omega_0)+\mu_u=A(\omega,\omega_0)+t\eta+\mu_u=A(\phi^*\omega,\omega_0)+t\eta\qquad\text{(part (B) at }\omega_{t,\eta}\text{ and at }\omega\text{).}$$
> Hence the family $t\mapsto\phi^*\omega_{t,\eta}$ is exactly the variation of $\phi^*\omega$ in the direction $\eta$; that is, $(\phi^*\omega)_{t,\eta}=\phi^*(\omega_{t,\eta})$.
>
> *The two variations of the action agree.* Combining parts (A) and (B) at the connection $\omega_{t,\eta}$,
> $$L(\phi^*\omega_{t,\eta})=L_1(\phi^*\omega_{t,\eta})+L_2(\phi^*\omega_{t,\eta})=L_1(\omega_{t,\eta})+\big(L_2(\omega_{t,\eta})+\mu_u\wedge J\big)=L(\omega_{t,\eta})+\mu_u\wedge J\qquad\text{(part (A) and part (B) at }\omega_{t,\eta}\text{).}$$
> Integrating over $\bar U$ and differentiating at $t=0$, and using that $\mu_u\wedge J$ does not depend on $t$,
> $$\frac{d}{dt}\Big|_{0}\int_{\bar U}L(\phi^*\omega_{t,\eta})=\frac{d}{dt}\Big|_{0}\int_{\bar U}L(\omega_{t,\eta})+\frac{d}{dt}\Big|_{0}\underbrace{\int_{\bar U}\mu_u\wedge J}_{\text{constant in }t}=\frac{d}{dt}\Big|_{0}\int_{\bar U}L(\omega_{t,\eta}).$$
> Since $(\phi^*\omega)_{t,\eta}=\phi^*(\omega_{t,\eta})$, the left-hand side is the variation of the action at $\phi^*\omega$ in the direction $\eta$. As $U$ and $\eta$ were arbitrary, the criticality condition for $\phi^*\omega$ holds if and only if it holds for $\omega$. Therefore $\omega$ is critical for $L$ if and only if $\phi^*\omega$ is critical for $L$.
>
> *The action itself, for a function-generated $\phi$.* Suppose in addition $dJ=0$ and $\phi(p)=p\cdot e^{i\chi(\pi(p))}$ with $\chi\in C^\infty(M)$, $\operatorname{supp}\chi\subset U\Subset M$. Then $u=e^{i\chi}$, so $u^{-1}du=e^{-i\chi}\cdot i e^{i\chi}\,d\chi=i\,d\chi$ and $\mu_u=\tfrac1i u^{-1}du=d\chi$. Using part (A) and part (B),
> $$\int_{\bar U}L(\phi^*\omega)-\int_{\bar U}L(\omega)=\int_{\bar U}\big(L_1(\phi^*\omega)-L_1(\omega)\big)+\int_{\bar U}\big(L_2(\phi^*\omega)-L_2(\omega)\big)=0+\int_{\bar U}\mu_u\wedge J=\int_{\bar U}d\chi\wedge J.$$
> By Lemma 4 (with this $\chi$ and $J$, using $dJ=0$), $\int_{\bar U}d\chi\wedge J=0$. Hence $\int_{\bar U}L(\phi^*\omega)=\int_{\bar U}L(\omega)$. This is part (C).
>
> All three parts are established. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Aharonov–Bohm phase and holonomy.** On $M=\mathbb R^{1,3}\setminus(\text{a timelike line})$ with a flat $U(1)$-connection carrying nonzero holonomy around the removed line, apply the theorem to a gauge transformation with $\mu_u$ having a nonzero period around a spatial loop. The exercise is to see that although $F=0$ everywhere and the local potential can be gauged to zero on any simply connected patch, the holonomy $\exp\big(i\oint A\big)$ is gauge-invariant — because $\oint\mu_u\in 2\pi\mathbb Z$ leaves $\exp\big(i\oint A\big)$ fixed. The theorem applies because a flat connection is still a connection with its full gauge freedom; the non-obvious point is that a quantity built from the *non*-invariant $A$ can nonetheless be gauge-invariant once exponentiated around a closed loop.

**Lattice gauge theory.** Replace $M$ by a cubical lattice, $U(1)$-connections by phases $u_e\in U(1)$ on oriented edges $e$, and $F$ by the plaquette product $\prod_{e\in\partial P}u_e$. A gauge transformation is a phase $u_v\in U(1)$ at each vertex acting by $u_e\mapsto u_{v_-}^{-1}u_e\,u_{v_+}$. The exercise is to check that the plaquette product (the discrete field strength) is gauge-invariant while an edge phase is not, mirroring parts (A) and (B) exactly; the discrete analogue of "$d\mu_u$ closed" is that a vertex gauge factor telescopes around any closed plaquette. This is non-obvious because the continuum proof used the calculus identity $d^2=0$, and one must find its combinatorial shadow.

**Superconductivity and the London equation.** In the Ginzburg–Landau description a superconductor is modelled by a charged scalar $\psi$ coupled to a $U(1)$-connection, and physical observables must be invariant under $\psi\mapsto e^{i\chi}\psi$, $A\mapsto A+d\chi$. The exercise is to identify the gauge-invariant combination $\big(d\chi\text{-corrected momentum}\big)$ — namely $d\psi-iA\psi$ — and to explain, using part (A), why the magnetic field $F$ and hence the flux through a hole in the superconductor is quantised. The theorem applies because the coupling is precisely $L_2$-type; the subtlety is that the *matter* transformation and the *gauge* transformation must be locked together for invariance, which is exactly the "generated by a function" clause.

---

# Bridges

- **[[Thm - Yang-Mills Action is Half the Squared L2 Norm of the Curvature and is Gauge Invariant|Gauge invariance of the Yang–Mills action]]** — the non-abelian sequel. For a general compact structure group $G$ the same pullback $\omega'=\phi^*\omega$ no longer fixes the field strength; instead $\bar\Omega'=\operatorname{Ad}_{u^{-1}}\bar\Omega$, where now $u\colon P\to G$ is the *equivariant* representing map (which descends to a section of the group bundle, not to a function on $M$, unless $G$ is abelian). The Yang–Mills density $\tfrac12\lVert\bar\Omega\rVert^2\,\mathrm{vol}$ is invariant because the inner product $\lVert\cdot\rVert^2$ on $\mathfrak g$ is chosen $\operatorname{Ad}$-invariant, so $\lVert\operatorname{Ad}_{u^{-1}}\bar\Omega\rVert=\lVert\bar\Omega\rVert$. The present theorem is the special case where $\operatorname{Ad}$ is trivial and the two mechanisms — invariance of the field and invariance of the norm — coincide; comparing them shows precisely which structural fact of $U(1)$ was doing the work.

- **[[Thm - Euler-Lagrange Equation of the Electromagnetic Action|Euler–Lagrange equation of the electromagnetic action]]** — the reason part (C) matters. That theorem identifies criticality with Maxwell's inhomogeneous equation $d\star F+J=0$. Chaining it with part (C) here gives at once that the solution set of Maxwell's equations is gauge-invariant, so that the physically distinct solutions are the gauge orbits; this is the construction that, in the non-abelian and elliptic setting of later chapters, becomes the instanton moduli space.

- **[[Thm - First Chern Class of a Line Bundle from Curvature|First Chern class from curvature]]** — the topological shadow of part (A). Because $\bar\Omega$ is gauge-invariant *and*, by Chern–Weil, its de Rham class is independent of the connection, the class $\big[\tfrac1{2\pi}F\big]\in H^2_{\mathrm{dR}}(M)$ is a genuine invariant of the bundle $P$. Integrated over a closed surface it is an integer — the degree of the line bundle, equivalently the magnetic charge — which no gauge transformation and no deformation of the connection can alter. This is the bridge from the analytic statement here to Dirac's charge quantisation.

- **Classical gauge freedom of the four-potential** — the physics dictionary. In the special-relativity chapters the electromagnetic potential is defined up to $A\mapsto A+d\chi$ (`Def - Gauge Choice and the Lorenz Gauge`), and Maxwell's equations are checked to be invariant under it. Part (B), specialised to a function-generated transformation, reproduces exactly this freedom, now derived from the bundle picture rather than postulated: the ambiguity $d\chi$ is the descent of a genuine automorphism $\phi(p)=p\cdot e^{i\chi(\pi(p))}$ of $P$.

---

# Unlocked by This

> [!tip] Gauge orbits and the configuration space *(from Gauge Theory)*
> Part (C) shows the physics lives on the quotient $\mathcal C(P)/\mathcal G(P)$ rather than on $\mathcal C(P)$. The geometry of this quotient — its singularities at reducible connections, its tangent spaces, the slices that make it a manifold away from the reducibles — is the arena of Donaldson and Seiberg–Witten theory. See **Def - The Gauge Orbit Space** and **Thm - Slice Theorem for the Gauge Action**.

> [!tip] Anomalies *(from Quantum Field Theory)*
> The clause of part (C) that criticality is preserved while the *value* of the action can shift by $\int\mu_u\wedge J$ is the classical seed of the notion of an anomaly: a symmetry of the equations of motion that fails to be a symmetry of the (effective) action. When the shift cannot be removed even after quantisation one has a genuine gauge anomaly, an obstruction to consistency of the theory. See **Def - Gauge Anomaly**.
