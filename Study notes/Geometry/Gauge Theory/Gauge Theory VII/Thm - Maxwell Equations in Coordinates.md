---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Maxwell Equations in Form Language"
  - "Def - Hodge Star in Arbitrary Signature"
  - "Thm - Coordinate Expression for the Exterior Derivative"
tags: [geometry, gauge-theory, electrodynamics]
---

# Notation

We work on **Minkowski space** $M=\mathbb R^{1,3}$: the manifold $\mathbb R^4$ with the flat Lorentzian metric of signature $(-,+,+,+)$ and index $p=1$, in standard global coordinates $(t,x,y,z)$ for which the coordinate vector fields are orthogonal with $\langle\partial_t,\partial_t\rangle=-1$ and $\langle\partial_x,\partial_x\rangle=\langle\partial_y,\partial_y\rangle=\langle\partial_z,\partial_z\rangle=+1$. We use units in which the speed of light is $c=1$, following Bär, §3.2. The orientation is the standard one, and the Riemannian, or here pseudo-Riemannian, **volume form** is
$$\mathrm{vol}=dt\wedge dx\wedge dy\wedge dz.$$
The dual coframe $(dt,dx,dy,dz)$ is a generalized orthonormal basis in the sense of [[Def - Generalized Orthonormal Basis, Index, and the Induced Inner Product on Forms|the §7.1 definition]], with signs $\epsilon_t=-1$, $\epsilon_x=\epsilon_y=\epsilon_z=+1$.

The **electromagnetic field strength** is the real $2$-form $F\in\Omega^2(M;\mathbb R)$ obtained from the curvature of a $U(1)$-connection, $\bar\Omega=iF$ (see [[Def - U(1) Gauge Field and Electromagnetic Connection]]). In these coordinates we write it, following [[Def - U(1) Gauge Field and Electromagnetic Connection|the field-strength definition]], as
$$F=E_x\,dx\wedge dt+E_y\,dy\wedge dt+E_z\,dz\wedge dt+B_x\,dy\wedge dz+B_y\,dz\wedge dx+B_z\,dx\wedge dy,$$
where $E_x,E_y,E_z,B_x,B_y,B_z\in C^\infty(M)$. The (in general time-dependent) spatial vector fields $\vec E=(E_x,E_y,E_z)$ and $\vec B=(B_x,B_y,B_z)$ are the **electric** and **magnetic fields**; their split into a triple of components depends on the coordinate system, whereas $F$ does not.

The **charge–current $3$-form** is $J\in\Omega^3(M;\mathbb R)$, defined on [[Def - Charge-Current 3-Form]] by
$$J=\varrho\,dx\wedge dy\wedge dz-j_x\,dt\wedge dy\wedge dz-j_y\,dt\wedge dz\wedge dx-j_z\,dt\wedge dx\wedge dy,$$
with **charge density** $\varrho\in C^\infty(M)$ and **current density** $\vec j=(j_x,j_y,j_z)$.

The **Hodge star** $\star=\star_B:\Lambda^k\to\Lambda^{n-k}$ is the operator of [[Def - Hodge Star in Arbitrary Signature]], the unique linear map with
$$\omega\wedge\eta=\langle\star\omega,\eta\rangle\,\mathrm{vol}\qquad\text{for all }\omega\in\Lambda^k,\ \eta\in\Lambda^{n-k},$$
where $\langle\cdot,\cdot\rangle$ is the induced inner product on forms. Here $n=4$, $p=1$.

The classical differential operators of vector calculus on the spatial slice, applied to a time-dependent spatial vector field $\vec a=(a_x,a_y,a_z)$ and to the same for $\vec b$, are the **divergence**
$$\operatorname{div}\vec b=\partial_x b_x+\partial_y b_y+\partial_z b_z\in C^\infty(M),$$
and the **curl** (written $\operatorname{rot}$, Bär's notation for $\nabla\times$)
$$\operatorname{rot}\vec a=\big(\partial_y a_z-\partial_z a_y,\ \partial_z a_x-\partial_x a_z,\ \partial_x a_y-\partial_y a_x\big),$$
with $\partial_t$ the coordinate time derivative and $\partial_t\vec b=(\partial_t b_x,\partial_t b_y,\partial_t b_z)$. The symbols $\partial_x,\partial_y,\partial_z,\partial_t$ denote partial derivatives with respect to the four coordinates.

> [!warning] Convention: signature, units, and the two star operators
> Three conventions collide at this page and must be kept straight.
> - **Bär's convention (used here).** Signature $(-,+,+,+)$, index $p=1$, $c=1$, unit charge and mass, and the Hodge star $\star_B$ defined by $\omega\wedge\eta=\langle\star\omega,\eta\rangle\,\mathrm{vol}$. The inhomogeneous law is $d\star F+J=0$.
> - **The special-relativity chapter.** The pages [[Thm - Maxwell Equations]] and [[Def - The Electromagnetic Field Tensor]] (Special Relativity XXII) use signature $(+,-,-,-)$, SI units with $c$ and $\mu_0$ explicit, and the vault's Riemannian-style star $\star_V$. The dictionary between the two is: the metrics differ by an overall sign, $g_B=-g_{SR}$; the $2$-form $F$ and the fields $\vec E,\vec B$ are the same objects; and on Minkowski $2$-forms $\star_B=-\star_V$. Consequently Bär's $d\star_B F+J=0$ and the special-relativity form $d\star_V F=\mu_0\star_V j$ describe the identical physics once the sign of the star and the $J$-versus-$j$ sign of [[Def - Charge-Current 3-Form]] are inserted.
> - **The general-signature star $\star'$.** The alternative convention $\alpha\wedge\star'\beta=\langle\alpha,\beta\rangle\,\mathrm{vol}$ satisfies $\star'=(-1)^{k(n-k)}\star_V$; it agrees with $\star_V$ on $2$-forms in dimension $4$. It is not the operator used here.
>
> The two computations that appear elsewhere in the vault in the *other* signature are [[Ex - Maxwell's equations in three-dimensional form]] (Special Relativity XXII) and [[Ex - Maxwell's Equations as Two Form Equations on Minkowski Space]] (Differential Geometry IX): they are the same coefficient-by-coefficient computation carried out with $\star_V$ and $(+,-,-,-)$, and reaching the same four laws.

---

# Statement

> **Theorem (Maxwell's equations in coordinates).** Let $M=\mathbb R^{1,3}$ be Minkowski space with the coordinates, orientation, and volume form $\mathrm{vol}=dt\wedge dx\wedge dy\wedge dz$ fixed above. Let $F$ be the electromagnetic field strength written $F=E_x\,dx\wedge dt+E_y\,dy\wedge dt+E_z\,dz\wedge dt+B_x\,dy\wedge dz+B_y\,dz\wedge dx+B_z\,dx\wedge dy$, and let $J$ be the charge–current $3$-form. Then the following three coordinate identities hold, and with them the stated equivalences.
>
> **(i) The exterior derivative of $F$.**
> $$dF=(\partial_xB_x+\partial_yB_y+\partial_zB_z)\,dx\wedge dy\wedge dz+(\partial_yE_z-\partial_zE_y+\partial_tB_x)\,dt\wedge dy\wedge dz$$
> $$\qquad\qquad+(\partial_zE_x-\partial_xE_z+\partial_tB_y)\,dt\wedge dz\wedge dx+(\partial_xE_y-\partial_yE_x+\partial_tB_z)\,dt\wedge dx\wedge dy.$$
> Consequently $dF=0$ if and only if
> $$\operatorname{div}\vec B=0\quad\text{(Gauss's law for magnetism, (3.7))}\qquad\text{and}\qquad\partial_t\vec B+\operatorname{rot}\vec E=0\quad\text{(Faraday's law, (3.8))}.$$
>
> **(ii) The Hodge dual of $F$.**
> $$\star F=-E_x\,dy\wedge dz-E_y\,dz\wedge dx-E_z\,dx\wedge dy+B_x\,dx\wedge dt+B_y\,dy\wedge dt+B_z\,dz\wedge dt.$$
> Equivalently, $\star F$ is again a field strength of the same shape, with electric field $\vec B$ and magnetic field $-\vec E$; the star sends $(\vec E,\vec B)\mapsto(\vec B,-\vec E)$.
>
> **(iii) The exterior derivative of $\star F$ and the inhomogeneous law.**
> $$d\star F=(-\operatorname{div}\vec E)\,dx\wedge dy\wedge dz+(\operatorname{rot}\vec B-\partial_t\vec E)_x\,dt\wedge dy\wedge dz$$
> $$\qquad\qquad+(\operatorname{rot}\vec B-\partial_t\vec E)_y\,dt\wedge dz\wedge dx+(\operatorname{rot}\vec B-\partial_t\vec E)_z\,dt\wedge dx\wedge dy.$$
> Consequently $d\star F+J=0$ if and only if
> $$\operatorname{div}\vec E=\varrho\quad\text{(Coulomb's / Gauss's law, (3.9))}\qquad\text{and}\qquad\operatorname{rot}\vec B-\partial_t\vec E=\vec j\quad\text{(Ampère's law, (3.10))}.$$
>
> Together, the two form equations $dF=0$ and $d\star F+J=0$ — the [[Def - Maxwell Equations in Form Language|Maxwell equations in form language]] — are equivalent, in any inertial coordinate frame on Minkowski space, to the four classical Maxwell equations (3.7)–(3.10).

---

# Motivation

The chapter has already given the electromagnetic field a coordinate-free identity: $F$ is $-i$ times the curvature of a connection on a $U(1)$-principal bundle, the homogeneous equation $dF=0$ is the [[Thm - Bianchi Identity for a Principal Connection|Bianchi identity]] worn as a physical law, and the inhomogeneous equation $d\star F+J=0$ is the [[Thm - Euler-Lagrange Equation of the Electromagnetic Action|Euler–Lagrange equation]] of the action $\int(\tfrac12 F\wedge\star F+A\wedge J)$. Both equations are single lines, both are manifestly independent of any choice of coordinates or observer, and both are opaque to anyone who learned electromagnetism as four vector equations for $\vec E$ and $\vec B$.

This page is the translation. It answers one question: *what do the two form equations say once an inertial observer splits spacetime into time and space?* The answer is that they say exactly Maxwell's four equations — Gauss's law for magnetism, Faraday's law, Coulomb's law, and Ampère's law with Maxwell's displacement-current term — no more and no less. The translation is not a re-derivation of physics; the physics was settled by the Bianchi identity and the variational principle. It is the demonstration that the compact geometric formulation and the classical vector-calculus formulation are the same content in two languages, and that the passage between them is a single mechanical computation: the exterior derivative of a $2$-form in four coordinates.

The importance of doing this once, carefully, is twofold. First, it certifies that the gauge-theoretic packaging of electromagnetism has lost nothing: every classical law is recovered, with the correct signs. Second, it exhibits the mechanism — divergence and curl are the two pieces of $d$ acting on a $2$-form under a time-plus-space split — that recurs verbatim for the non-abelian Yang–Mills field in §7.4, where $d\star F$ is replaced by the covariant $d^A\star F$ but the coordinate skeleton is the same. A reader who has watched the four Maxwell equations fall out of $dF=0$ and $d\star F+J=0$ knows precisely which part of the Yang–Mills equation is "divergence of the electric field" and which is "curl of the magnetic field".

---

# Sources and Targets

**Sources (Input Broadening)**

The literal hypothesis is only that we are on Minkowski space with a $2$-form $F$ of the stated electric–magnetic shape and a $3$-form $J$. The question worth asking is when a problem hands us that data without saying so.

The first disguised source is **any closed $2$-form on an oriented Lorentzian $4$-manifold together with a choice of time coordinate**. The property $B$ here is "$F$ is the curvature of a $U(1)$-connection". The bridge $B\Rightarrow A$ is the abelian [[Thm - Bianchi Identity for a Principal Connection|Bianchi identity]]: for an abelian structure group the curvature descends to a global real $2$-form and satisfies $dF=0$ automatically, so part (i) of the theorem immediately reads off Gauss's law for magnetism and Faraday's law as *identities*, before any equation of motion is imposed. The non-obvious step is that half of Maxwell's equations are true of every field strength whatsoever and carry no information about sources. *Example problem:* given only that a spacetime $2$-form is exact, $F=dA$, conclude $\operatorname{div}\vec B=0$ and $\partial_t\vec B+\operatorname{rot}\vec E=0$ with no further hypotheses.

The second disguised source is **a $2$-form presented as the Hodge dual of another $2$-form**. Part (ii) shows that $\star F$ is again a field strength of the same six-coefficient shape, with electric field $\vec B$ and magnetic field $-\vec E$. The bridge is that the electric–magnetic decomposition is stable under $\star$ in dimension four, so the very same coordinate computation for $dF$ applies unchanged to $d\star F$. The non-obviousness is that the inhomogeneous law $d\star F+J=0$ needs no new machinery: it is the homogeneous computation run a second time on a relabelled field. *Example problem:* deduce Coulomb's and Ampère's laws from Gauss's and Faraday's laws by applying the same lemma to $\star F$ in place of $F$.

The third disguised source is **an antisymmetric rank-two tensor field $F_{\mu\nu}$ on Minkowski space**, the form in which physics texts present the field strength. The bridge is the identification $F=\tfrac12 F_{\mu\nu}\,dx^\mu\wedge dx^\nu$ with $F_{i0}=E_i$ and the spatial block the components of $\vec B$; once this identification is made, the tensor problem becomes the present differential-form problem. The non-obvious step is recognising that "raise the indices and take the divergence $\partial^\mu F_{\mu\nu}$" is exactly "$d\star F$" up to the sign of the metric. *Example problem:* show that $\partial^\mu F_{\mu\nu}=j_\nu$ in a physics text is the component form of $d\star F+J=0$.

**Targets (Output Amplification)**

The bare conclusion is the four classical equations. Combined with one further ingredient each, it produces more.

Combine part (iii) with **the charge–current $3$-form and the nilpotence of $d$** ($d^2=0$, from [[Thm - d-Squared-is-Zero]]). Applying $d$ to $d\star F+J=0$ gives $dJ=0$, and part (i)'s computation applied to $J$ yields the continuity equation $\partial_t\varrho+\operatorname{div}\vec j=0$: charge is conserved. The extra ingredient is $d^2=0$; the payoff is that conservation of charge is not an extra postulate but a corollary of the inhomogeneous law, proved on [[Thm - Continuity Equation and Conservation of Charge]].

Combine parts (i)–(iii) with **the vacuum condition $J=0$ and a plane-wave ansatz**. Setting $\varrho=0$, $\vec j=0$ and substituting fields of the form $\vec E=\vec E_0\cos(k z-\omega t)$ into the four equations forces $|\vec k|=\omega$ (with $c=1$) and $\vec E_0\perp\vec B_0\perp\vec k$: electromagnetic waves travel at the speed of light and are transverse. The extra ingredient is the ansatz; the payoff is the existence and structure of light, worked in [[Ex - Maxwell's Equations on Minkowski Space from the Two Form Equations]].

Combine part (ii) with **the wedge pairing $F\wedge\star F$**. Because $\star$ carries $(\vec E,\vec B)$ to $(\vec B,-\vec E)$, the Lagrangian density $\tfrac12 F\wedge\star F$ evaluates on Minkowski space to $\tfrac12(|\vec E|^2-|\vec B|^2)\,\mathrm{vol}$, the classical electromagnetic Lagrangian. The extra ingredient is the pairing property (4) of the star; the payoff is that the geometric action reproduces the textbook Lagrangian, the starting point of [[Def - Electromagnetic Lagrangian and Action]].

---

# Why Is It True

Strip away the physics and look at what the exterior derivative does to a $2$-form on $\mathbb R^4$ once the coordinates are split into one time direction and three space directions. A $2$-form has six independent components. Three of them pair a spatial direction with time — these are the $dx\wedge dt$, $dy\wedge dt$, $dz\wedge dt$ slots, where the electric field sits — and three are purely spatial — the $dy\wedge dz$, $dz\wedge dx$, $dx\wedge dy$ slots, where the magnetic field sits. Now apply $d$. The exterior derivative differentiates a coefficient and wedges the resulting $1$-form onto the two directions already present. There are only two kinds of $3$-form it can produce: the purely spatial $3$-form $dx\wedge dy\wedge dz$, and the three $3$-forms containing exactly one $dt$.

Ask which derivatives land in the purely spatial slot. Only a spatial derivative of a purely spatial component can, because a $dt$ anywhere would spoil "purely spatial". So the coefficient of $dx\wedge dy\wedge dz$ is built from $\partial_x,\partial_y,\partial_z$ acting on the magnetic components — and it assembles into exactly $\partial_xB_x+\partial_yB_y+\partial_zB_z=\operatorname{div}\vec B$. Ask which derivatives land in a mixed slot such as $dt\wedge dy\wedge dz$. Two sources feed it: a *time* derivative of a purely spatial component (here $\partial_tB_x$), and a *spatial* derivative of an electric (space–time) component, which is precisely how the curl of $\vec E$ is built. The mixed slots therefore hold $\partial_t\vec B+\operatorname{rot}\vec E$.

> **The mechanism in one sentence: on a $2$-form in four coordinates split into time and space, the exterior derivative $d$ is the divergence of the spatial part in the all-spatial slot and the time-derivative-plus-curl of the two parts in the mixed slots — divergence and curl are the two faces of $d$.**

This is the [[Def - Frankel Dictionary (Forms vs Vector Calculus)|Frankel dictionary]] made spacetime-sized: in three Euclidean dimensions that dictionary says $d$ on a $2$-form is the divergence and $d$ on a $1$-form is the curl; adding a time direction interleaves the two, so that a single four-dimensional $d$ on a $2$-form carries a divergence and a curl at once. Part (iii) is then forced with no new idea: since $\star F$ has the same shape as $F$ with the roles of electric and magnetic fields swapped (and one sign flipped), running the identical computation on $\star F$ produces $-\operatorname{div}\vec E$ where it produced $\operatorname{div}\vec B$, and $\operatorname{rot}\vec B-\partial_t\vec E$ where it produced $\partial_t\vec B+\operatorname{rot}\vec E$. The homogeneous and inhomogeneous laws are the same computation applied to $F$ and to its dual.

---

# What Makes This Hard

The content is a bookkeeping computation, and the difficulty is entirely bookkeeping: there are eighteen elementary terms in $dF$ (three derivatives surviving on each of six coefficients), and each must be reordered to a chosen basis $3$-form with the correct sign, so a single dropped transposition corrupts a Maxwell equation. The one genuinely non-mechanical point is the sign in the star table: because the time direction has $\langle\partial_t,\partial_t\rangle=-1$, the entries $\star(dy\wedge dz)=-dt\wedge dx$ carry a minus sign that the Euclidean intuition does not supply, and it is this minus that makes $\star$ send $(\vec E,\vec B)$ to $(\vec B,-\vec E)$ rather than to $(\vec B,\vec E)$ — the difference between recovering Ampère's law with the correct sign and getting it wrong. The common error, beyond miscounting a transposition, is to import the Riemannian star $\star_V$ (which differs from Bär's $\star_B$ by an overall sign on Minkowski $2$-forms) and thereby flip every sign in $\star F$ at once. Two printing errors in the source compound the trap and are corrected explicitly below.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Prove one general lemma — the coordinate exterior derivative of an arbitrary $2$-form written in the electric–magnetic decomposition is a divergence in the spatial slot and a time-derivative-plus-curl in the mixed slots. Prove a second general lemma — the Minkowski Hodge star of such a $2$-form is again such a $2$-form, with electric field $\vec b$ and magnetic field $-\vec a$. Then part (i) is the first lemma applied to $F$; part (ii) is the second lemma applied to $F$; part (iii) is the first lemma applied to $\star F$. Read off the equivalences slot by slot.

**Subgoal decomposition:**

1. **Exterior derivative of a generic decomposed $2$-form.** Compute $dG$ for $G=a_x\,dx\wedge dt+a_y\,dy\wedge dt+a_z\,dz\wedge dt+b_x\,dy\wedge dz+b_y\,dz\wedge dx+b_z\,dx\wedge dy$.
   - *Hint:* Use the coordinate formula $d(f\,\alpha)=df\wedge\alpha$ on each of the six terms, keep only the surviving derivatives, and reorder to the four basis $3$-forms $dx\wedge dy\wedge dz,\ dt\wedge dy\wedge dz,\ dt\wedge dz\wedge dx,\ dt\wedge dx\wedge dy$.
   - *Why needed:* Both $dF$ (part i) and $d\star F$ (part iii) are instances of this one formula; proving it once avoids doing the eighteen-term computation twice.

2. **The Minkowski star table.** Establish $\star(dt\wedge dx)=dy\wedge dz$, $\star(dy\wedge dz)=-dt\wedge dx$, and the four remaining entries, from the defining relation $\omega\wedge\eta=\langle\star\omega,\eta\rangle\,\mathrm{vol}$.
   - *Hint:* For each basis $2$-form $\omega$, the only basis $\eta$ with $\omega\wedge\eta\neq0$ is its complement; solve $\langle\star\omega,\eta\rangle=(\omega\wedge\eta)/\mathrm{vol}$ using the inner-product values $\langle dt\wedge d\xi,dt\wedge d\xi\rangle=-1$, $\langle\text{spatial}\rangle=+1$.
   - *Why needed:* Part (ii) is exactly this table applied coefficient by coefficient to $F$; the timelike sign is where the physics-critical minus enters.

3. **Assemble.** Apply subgoal 1 to $F$ (with $\vec a=\vec E$, $\vec b=\vec B$); apply subgoal 2 to $F$ to get $\star F$; apply subgoal 1 to $\star F$ (with $\vec a=\vec B$, $\vec b=-\vec E$).
   - *Hint:* In each part, set each of the four coefficients to zero (or, in part iii, equal to the matching coefficient of $-J$) and translate.
   - *Why needed:* This is where the three abstract identities become the four named laws.

---

# Lemma Decomposition

> [!note]- Lemma 1: The exterior derivative of a $2$-form in electric–magnetic decomposition is divergence plus curl
> **Statement:** Let $G=a_x\,dx\wedge dt+a_y\,dy\wedge dt+a_z\,dz\wedge dt+b_x\,dy\wedge dz+b_y\,dz\wedge dx+b_z\,dx\wedge dy$ be a smooth $2$-form on Minkowski space, with $a_i,b_i\in C^\infty(M)$ and $\vec a=(a_x,a_y,a_z)$, $\vec b=(b_x,b_y,b_z)$. Then
> $$dG=(\operatorname{div}\vec b)\,dx\wedge dy\wedge dz+(\partial_t\vec b+\operatorname{rot}\vec a)_x\,dt\wedge dy\wedge dz+(\partial_t\vec b+\operatorname{rot}\vec a)_y\,dt\wedge dz\wedge dx+(\partial_t\vec b+\operatorname{rot}\vec a)_z\,dt\wedge dx\wedge dy.$$
>
> **Hint:** Apply $d(f\,\alpha)=df\wedge\alpha$ to each term, discard terms with a repeated coordinate, and reorder every surviving $3$-form to one of the four basis forms, tracking the sign of each reordering.
>
> **Why needed:** It is the single computation behind both $dF$ (part i) and $d\star F$ (part iii); once it is in hand, those parts are substitutions.
>
> > [!note]- Full proof
> > We compute $dG$ term by term. For a coefficient function $f\in C^\infty(M)$ and constant-coefficient basis $2$-form $\alpha$, the [[Thm - Coordinate Expression for the Exterior Derivative|coordinate expression for the exterior derivative]] — which states that $d(f\,dx^{i_1}\wedge\cdots\wedge dx^{i_k})=df\wedge dx^{i_1}\wedge\cdots\wedge dx^{i_k}$ with $df=\partial_t f\,dt+\partial_x f\,dx+\partial_y f\,dy+\partial_z f\,dz$ — gives $d(f\,\alpha)=df\wedge\alpha$. In each wedge $df\wedge\alpha$, any term of $df$ along a coordinate already present in $\alpha$ vanishes, because a $1$-form wedged with itself is zero.
> >
> > **The three electric terms** (those built from $\vec a$, each an $a_i$ times a $d\xi_i\wedge dt$).
> > $$d(a_x\,dx\wedge dt)=\partial_y a_x\,dy\wedge dx\wedge dt+\partial_z a_x\,dz\wedge dx\wedge dt\qquad\text{(only }\partial_y,\partial_z\text{ survive; }\partial_x,\partial_t\text{ repeat a factor)},$$
> > $$d(a_y\,dy\wedge dt)=\partial_x a_y\,dx\wedge dy\wedge dt+\partial_z a_y\,dz\wedge dy\wedge dt,$$
> > $$d(a_z\,dz\wedge dt)=\partial_x a_z\,dx\wedge dz\wedge dt+\partial_y a_z\,dy\wedge dz\wedge dt.$$
> >
> > **The three magnetic terms** (those built from $\vec b$, each a $b_i$ times a purely spatial $2$-form).
> > $$d(b_x\,dy\wedge dz)=\partial_t b_x\,dt\wedge dy\wedge dz+\partial_x b_x\,dx\wedge dy\wedge dz\qquad\text{(only }\partial_t,\partial_x\text{ survive)},$$
> > $$d(b_y\,dz\wedge dx)=\partial_t b_y\,dt\wedge dz\wedge dx+\partial_y b_y\,dy\wedge dz\wedge dx,$$
> > $$d(b_z\,dx\wedge dy)=\partial_t b_z\,dt\wedge dx\wedge dy+\partial_z b_z\,dz\wedge dx\wedge dy.$$
> >
> > **Collect the coefficient of $dx\wedge dy\wedge dz$.** The three contributing terms are $\partial_x b_x\,dx\wedge dy\wedge dz$, $\partial_y b_y\,dy\wedge dz\wedge dx$, and $\partial_z b_z\,dz\wedge dx\wedge dy$. The reorderings $dy\wedge dz\wedge dx=dx\wedge dy\wedge dz$ and $dz\wedge dx\wedge dy=dx\wedge dy\wedge dz$ are each a cyclic permutation of three factors, an even permutation, so each carries sign $+1$ (a cyclic shift of three elements is two transpositions). Hence the coefficient is $\partial_x b_x+\partial_y b_y+\partial_z b_z=\operatorname{div}\vec b$.
> >
> > **Collect the coefficient of $dt\wedge dy\wedge dz$.** The contributing terms are $\partial_y a_z\,dy\wedge dz\wedge dt$, $\partial_z a_y\,dz\wedge dy\wedge dt$, and $\partial_t b_x\,dt\wedge dy\wedge dz$. Reordering $dy\wedge dz\wedge dt$: moving $dt$ from the last position to the first is two transpositions (past $dz$, past $dy$), an even permutation, so $dy\wedge dz\wedge dt=+dt\wedge dy\wedge dz$; its contribution is $+\partial_y a_z$. Reordering $dz\wedge dy\wedge dt$: move $dt$ to the front (two transpositions, $\,+dt\wedge dz\wedge dy$), then swap $dz$ and $dy$ (one transposition, sign $-1$), giving $dz\wedge dy\wedge dt=-dt\wedge dy\wedge dz$; its contribution is $-\partial_z a_y$. The last term is already $+\partial_t b_x\,dt\wedge dy\wedge dz$. Hence the coefficient is $\partial_y a_z-\partial_z a_y+\partial_t b_x=(\operatorname{rot}\vec a)_x+\partial_t b_x=(\partial_t\vec b+\operatorname{rot}\vec a)_x$.
> >
> > **Collect the coefficient of $dt\wedge dz\wedge dx$.** The contributing terms are $\partial_z a_x\,dz\wedge dx\wedge dt$, $\partial_x a_z\,dx\wedge dz\wedge dt$, and $\partial_t b_y\,dt\wedge dz\wedge dx$. Reordering $dz\wedge dx\wedge dt$: move $dt$ to the front (two transpositions), giving $+dt\wedge dz\wedge dx$; contribution $+\partial_z a_x$. Reordering $dx\wedge dz\wedge dt$: move $dt$ to the front (two transpositions, $\,+dt\wedge dx\wedge dz$), then swap $dx$ and $dz$ (sign $-1$), giving $-dt\wedge dz\wedge dx$; contribution $-\partial_x a_z$. The last term is $+\partial_t b_y\,dt\wedge dz\wedge dx$. Hence the coefficient is $\partial_z a_x-\partial_x a_z+\partial_t b_y=(\operatorname{rot}\vec a)_y+\partial_t b_y=(\partial_t\vec b+\operatorname{rot}\vec a)_y$.
> >
> > **Collect the coefficient of $dt\wedge dx\wedge dy$.** The contributing terms are $\partial_x a_y\,dx\wedge dy\wedge dt$, $\partial_y a_x\,dy\wedge dx\wedge dt$, and $\partial_t b_z\,dt\wedge dx\wedge dy$. Reordering $dx\wedge dy\wedge dt$: move $dt$ to the front (two transpositions), $+dt\wedge dx\wedge dy$; contribution $+\partial_x a_y$. Reordering $dy\wedge dx\wedge dt$: move $dt$ to the front (two transpositions, $\,+dt\wedge dy\wedge dx$), then swap $dy$ and $dx$ (sign $-1$), $-dt\wedge dx\wedge dy$; contribution $-\partial_y a_x$. The last term is $+\partial_t b_z\,dt\wedge dx\wedge dy$. Hence the coefficient is $\partial_x a_y-\partial_y a_x+\partial_t b_z=(\operatorname{rot}\vec a)_z+\partial_t b_z=(\partial_t\vec b+\operatorname{rot}\vec a)_z$.
> >
> > There are no other basis $3$-forms present, since every one of the eighteen elementary terms lands in one of these four slots. Assembling the four coefficients gives the claimed formula. $\blacksquare$

> [!note]- Lemma 2: The Minkowski Hodge star table on $2$-forms
> **Statement:** With $\mathrm{vol}=dt\wedge dx\wedge dy\wedge dz$ and signature $(-,+,+,+)$, the Hodge star $\star_B$ acts on the six basis $2$-forms by
> $$\star(dt\wedge dx)=dy\wedge dz,\quad\star(dt\wedge dy)=dz\wedge dx,\quad\star(dt\wedge dz)=dx\wedge dy,$$
> $$\star(dy\wedge dz)=-dt\wedge dx,\quad\star(dz\wedge dx)=-dt\wedge dy,\quad\star(dx\wedge dy)=-dt\wedge dz.$$
>
> **Hint:** Each $2$-form $\omega$ wedges to a nonzero multiple of $\mathrm{vol}$ with exactly one basis $2$-form, its coordinate complement; the defining relation and the orthogonality of the induced inner product then pin down $\star\omega$.
>
> **Why needed:** Part (ii) of the theorem is this table applied to the six coefficients of $F$; the minus signs on the spatial rows are the timelike sign $\langle\partial_t,\partial_t\rangle=-1$.
>
> > [!note]- Full proof
> > By [[Thm - Existence and Uniqueness of the Hodge Star|existence and uniqueness of the Hodge star]], for each $\omega\in\Lambda^2$ there is a unique $\star\omega\in\Lambda^2$ with $\omega\wedge\eta=\langle\star\omega,\eta\rangle\,\mathrm{vol}$ for all $\eta\in\Lambda^2$. We use two standing facts about the induced inner product on $\Lambda^2$, both from [[Thm - The Induced Inner Product and Volume Form are Well-Defined|the induced-inner-product theorem]], part (ii): the six basis $2$-forms are pairwise orthogonal, and each squares to the product of the two $\epsilon$'s of its indices,
> > $$\langle dt\wedge dx,dt\wedge dx\rangle=\epsilon_t\epsilon_x=(-1)(+1)=-1$$
> > (and likewise $\langle dt\wedge dy,dt\wedge dy\rangle=\langle dt\wedge dz,dt\wedge dz\rangle=-1$), while the purely spatial ones give
> > $$\langle dy\wedge dz,dy\wedge dz\rangle=\epsilon_y\epsilon_z=(+1)(+1)=+1$$
> > (and likewise for $dz\wedge dx$ and $dx\wedge dy$). We use one elementary fact of linear algebra: in an orthogonal basis $\{\beta_a\}$ with $\langle\beta_a,\beta_a\rangle=g_a\neq0$, any vector $\gamma$ satisfies $\gamma=\sum_a\frac{\langle\gamma,\beta_a\rangle}{g_a}\,\beta_a$, because pairing both sides with $\beta_b$ and using orthogonality recovers $\langle\gamma,\beta_b\rangle$ on each side.
> >
> > **Row $\star(dt\wedge dx)$.** For each basis $\eta$, compute $(dt\wedge dx)\wedge\eta$. This vanishes unless $\eta=dy\wedge dz$, since any other basis $2$-form repeats $dt$ or $dx$. For $\eta=dy\wedge dz$, $(dt\wedge dx)\wedge(dy\wedge dz)=dt\wedge dx\wedge dy\wedge dz=\mathrm{vol}$. Thus $\langle\star(dt\wedge dx),\eta\rangle\,\mathrm{vol}$ equals $\mathrm{vol}$ for $\eta=dy\wedge dz$ and $0$ for every other basis $\eta$. By the orthogonal-expansion formula, the only nonzero component of $\star(dt\wedge dx)$ is along $dy\wedge dz$, with value $\langle\star(dt\wedge dx),dy\wedge dz\rangle/\langle dy\wedge dz,dy\wedge dz\rangle=1/(+1)=1$. Hence $\star(dt\wedge dx)=dy\wedge dz$.
> >
> > **Row $\star(dt\wedge dy)$.** Only $\eta=dz\wedge dx$ gives a nonzero wedge: $(dt\wedge dy)\wedge(dz\wedge dx)=dt\wedge dy\wedge dz\wedge dx$. Reordering $(t,y,z,x)$ to $(t,x,y,z)$ fixes $t$ and cyclically shifts $(y,z,x)\to(x,y,z)$, an even permutation, so this equals $+\mathrm{vol}$. Since $\langle dz\wedge dx,dz\wedge dx\rangle=+1$, the component is $1/(+1)=1$ and $\star(dt\wedge dy)=dz\wedge dx$.
> >
> > **Row $\star(dt\wedge dz)$.** Only $\eta=dx\wedge dy$ contributes: $(dt\wedge dz)\wedge(dx\wedge dy)=dt\wedge dz\wedge dx\wedge dy$; reordering $(t,z,x,y)$ to $(t,x,y,z)$ cyclically shifts $(z,x,y)\to(x,y,z)$, even, so $+\mathrm{vol}$. With $\langle dx\wedge dy,dx\wedge dy\rangle=+1$, the component is $1$ and $\star(dt\wedge dz)=dx\wedge dy$.
> >
> > **Row $\star(dy\wedge dz)$.** Only $\eta=dt\wedge dx$ contributes: $(dy\wedge dz)\wedge(dt\wedge dx)=dy\wedge dz\wedge dt\wedge dx$. Reordering $(y,z,t,x)$ to $(t,x,y,z)$: move $t$ (position $3$) to the front past $z,y$ (two transpositions), giving $(t,y,z,x)$; then move $x$ (position $4$) to the second slot past $z,y$ (two transpositions), giving $(t,x,y,z)$; total four transpositions, even, so this equals $+\mathrm{vol}$. Now $\langle dt\wedge dx,dt\wedge dx\rangle=-1$, so the component of $\star(dy\wedge dz)$ along $dt\wedge dx$ is $1/(-1)=-1$, and $\star(dy\wedge dz)=-dt\wedge dx$.
> >
> > **Row $\star(dz\wedge dx)$.** Only $\eta=dt\wedge dy$ contributes: $(dz\wedge dx)\wedge(dt\wedge dy)=dz\wedge dx\wedge dt\wedge dy$. Reordering $(z,x,t,y)$ to $(t,x,y,z)$: move $t$ (position $3$) to the front past $x,z$ (two transpositions), giving $(t,z,x,y)$; then cyclically shift $(z,x,y)\to(x,y,z)$ (even), giving $(t,x,y,z)$; total even, so $+\mathrm{vol}$. With $\langle dt\wedge dy,dt\wedge dy\rangle=-1$, the component is $-1$ and $\star(dz\wedge dx)=-dt\wedge dy$.
> >
> > **Row $\star(dx\wedge dy)$.** Only $\eta=dt\wedge dz$ contributes: $(dx\wedge dy)\wedge(dt\wedge dz)=dx\wedge dy\wedge dt\wedge dz$. Reordering $(x,y,t,z)$ to $(t,x,y,z)$: move $t$ (position $3$) to the front past $y,x$ (two transpositions), giving $(t,x,y,z)$; total even, so $+\mathrm{vol}$. With $\langle dt\wedge dz,dt\wedge dz\rangle=-1$, the component is $-1$ and $\star(dx\wedge dy)=-dt\wedge dz$.
> >
> > All six rows are established. As a consistency check, applying the table twice on $dt\wedge dx$ gives $\star\star(dt\wedge dx)=\star(dy\wedge dz)=-dt\wedge dx$, agreeing with the general sign $\star\star=(-1)^{k(n-k)+p}=(-1)^{2\cdot2+1}=-1$ for $k=2$, $n=4$, $p=1$. $\blacksquare$

> [!note]- Lemma 3: The Hodge dual of the field strength
> **Statement:** With $F$ as in the Notation, $\star F=-E_x\,dy\wedge dz-E_y\,dz\wedge dx-E_z\,dx\wedge dy+B_x\,dx\wedge dt+B_y\,dy\wedge dt+B_z\,dz\wedge dt$. Equivalently, $\star F$ is a field strength with electric field $\vec B$ and magnetic field $-\vec E$.
>
> **Hint:** Rewrite each of $F$'s six terms with its basis $2$-form in the orientation used by the star table (flipping a sign for each transposition), apply Lemma 2 by linearity, and collect.
>
> **Why needed:** It is part (ii) of the theorem, and it is what lets Lemma 1 be reused to compute $d\star F$ in part (iii).
>
> > [!note]- Full proof
> > The star is $\mathbb R$-linear, so we apply Lemma 2 to each term of $F$, first orienting each basis $2$-form to match the table. For the three electric terms, $dx\wedge dt=-\,dt\wedge dx$, $dy\wedge dt=-\,dt\wedge dy$, $dz\wedge dt=-\,dt\wedge dz$, so by Lemma 2 and linearity
> > $$\star(E_x\,dx\wedge dt)=-E_x\,\star(dt\wedge dx)=-E_x\,dy\wedge dz\qquad\text{(Lemma 2, first row)},$$
> > $$\star(E_y\,dy\wedge dt)=-E_y\,\star(dt\wedge dy)=-E_y\,dz\wedge dx,\qquad\star(E_z\,dz\wedge dt)=-E_z\,\star(dt\wedge dz)=-E_z\,dx\wedge dy.$$
> > For the three magnetic terms, the basis $2$-forms are already oriented as in the table, so
> > $$\star(B_x\,dy\wedge dz)=B_x\,\star(dy\wedge dz)=-B_x\,dt\wedge dx=B_x\,dx\wedge dt\qquad\text{(Lemma 2, fourth row; then }dt\wedge dx=-dx\wedge dt),$$
> > $$\star(B_y\,dz\wedge dx)=B_y\,\star(dz\wedge dx)=-B_y\,dt\wedge dy=B_y\,dy\wedge dt,\qquad\star(B_z\,dx\wedge dy)=B_z\,\star(dx\wedge dy)=-B_z\,dt\wedge dz=B_z\,dz\wedge dt.$$
> > Summing the six contributions,
> > $$\star F=-E_x\,dy\wedge dz-E_y\,dz\wedge dx-E_z\,dx\wedge dy+B_x\,dx\wedge dt+B_y\,dy\wedge dt+B_z\,dz\wedge dt.$$
> > Comparing with the general shape $G=a_x\,dx\wedge dt+\cdots+b_x\,dy\wedge dz+\cdots$: the coefficients of $dx\wedge dt,dy\wedge dt,dz\wedge dt$ are $B_x,B_y,B_z$, so the electric field of $\star F$ is $\vec B$; the coefficients of $dy\wedge dz,dz\wedge dx,dx\wedge dy$ are $-E_x,-E_y,-E_z$, so the magnetic field of $\star F$ is $-\vec E$. Hence $\star$ carries $(\vec E,\vec B)\mapsto(\vec B,-\vec E)$. $\blacksquare$
>
> > [!warning] Source correction (Bär, p. 86)
> > Bär's printed formula for $\star F$ ends "$-B_z\,dz\wedge dt$". By the star table (Lemma 2, sixth row) the coefficient of $dz\wedge dt$ must be $+B_z$: indeed $\star(B_z\,dx\wedge dy)=-B_z\,dt\wedge dz=+B_z\,dz\wedge dt$. The correct term is $+B_z\,dz\wedge dt$, as written above; the printed minus sign is a typographical error. (This is item 17 of the source-typo appendix.)

---

# Formal Proof

> [!note]- Complete formal proof
> We must establish the three coordinate identities (i)–(iii) and, in each case, the equivalence with the named classical laws. We work throughout in the fixed coordinates and orientation of the Notation, on Minkowski space with $\mathrm{vol}=dt\wedge dx\wedge dy\wedge dz$ and index $p=1$.
>
> **Step 0 — the objects are well-posed.** The field strength $F=E_x\,dx\wedge dt+E_y\,dy\wedge dt+E_z\,dz\wedge dt+B_x\,dy\wedge dz+B_y\,dz\wedge dx+B_z\,dx\wedge dy$ is a smooth real $2$-form, being a $C^\infty$-linear combination of constant basis $2$-forms; likewise $J$ is a smooth $3$-form and, by [[Thm - Existence and Uniqueness of the Hodge Star|existence and uniqueness of the Hodge star]], $\star F$ is a well-defined smooth $2$-form. The operators $d$ and $\star$ are the exterior derivative and the Hodge star fixed above.
>
> **Part (i) — the exterior derivative of $F$ and the homogeneous laws.** Apply **Lemma 1** to $G=F$, that is, with electric field $\vec a=\vec E$ and magnetic field $\vec b=\vec B$. The lemma gives
> $$dF=(\operatorname{div}\vec B)\,dx\wedge dy\wedge dz+(\partial_t\vec B+\operatorname{rot}\vec E)_x\,dt\wedge dy\wedge dz+(\partial_t\vec B+\operatorname{rot}\vec E)_y\,dt\wedge dz\wedge dx+(\partial_t\vec B+\operatorname{rot}\vec E)_z\,dt\wedge dx\wedge dy,$$
> which, spelled out with $\operatorname{div}\vec B=\partial_xB_x+\partial_yB_y+\partial_zB_z$ and $(\operatorname{rot}\vec E)_x=\partial_yE_z-\partial_zE_y$, is exactly the displayed formula in statement (i). Because the four $3$-forms $dx\wedge dy\wedge dz,\ dt\wedge dy\wedge dz,\ dt\wedge dz\wedge dx,\ dt\wedge dx\wedge dy$ are linearly independent, $dF=0$ holds if and only if all four coefficients vanish. The first, $\operatorname{div}\vec B=0$, is Gauss's law for magnetism, equation (3.7). The remaining three are the three components of the vector equation $\partial_t\vec B+\operatorname{rot}\vec E=0$, Faraday's law of induction, equation (3.8). This proves part (i).
>
> **Part (ii) — the Hodge dual of $F$.** This is precisely **Lemma 3**:
> $$\star F=-E_x\,dy\wedge dz-E_y\,dz\wedge dx-E_z\,dx\wedge dy+B_x\,dx\wedge dt+B_y\,dy\wedge dt+B_z\,dz\wedge dt,$$
> and, as shown there, $\star F$ is a field strength of the same shape with electric field $\vec B$ and magnetic field $-\vec E$, so $\star$ acts as $(\vec E,\vec B)\mapsto(\vec B,-\vec E)$. This proves part (ii).
>
> **Part (iii) — the exterior derivative of $\star F$ and the inhomogeneous laws.** By part (ii), $\star F$ is a $2$-form of the decomposition shape of Lemma 1 with electric field $\vec a=\vec B$ and magnetic field $\vec b=-\vec E$. Apply **Lemma 1** to $G=\star F$ with these fields:
> $$d\star F=(\operatorname{div}(-\vec E))\,dx\wedge dy\wedge dz+(\partial_t(-\vec E)+\operatorname{rot}\vec B)_x\,dt\wedge dy\wedge dz+(\partial_t(-\vec E)+\operatorname{rot}\vec B)_y\,dt\wedge dz\wedge dx+(\partial_t(-\vec E)+\operatorname{rot}\vec B)_z\,dt\wedge dx\wedge dy.$$
> Since $\operatorname{div}(-\vec E)=-\operatorname{div}\vec E$ and $\partial_t(-\vec E)+\operatorname{rot}\vec B=\operatorname{rot}\vec B-\partial_t\vec E$ (both by linearity of $\operatorname{div}$, $\operatorname{rot}$, and $\partial_t$), this is
> $$d\star F=(-\operatorname{div}\vec E)\,dx\wedge dy\wedge dz+(\operatorname{rot}\vec B-\partial_t\vec E)_x\,dt\wedge dy\wedge dz+(\operatorname{rot}\vec B-\partial_t\vec E)_y\,dt\wedge dz\wedge dx+(\operatorname{rot}\vec B-\partial_t\vec E)_z\,dt\wedge dx\wedge dy,$$
> the displayed formula of statement (iii). Now add $J=\varrho\,dx\wedge dy\wedge dz-j_x\,dt\wedge dy\wedge dz-j_y\,dt\wedge dz\wedge dx-j_z\,dt\wedge dx\wedge dy$, matching the four basis $3$-forms:
> $$d\star F+J=(\varrho-\operatorname{div}\vec E)\,dx\wedge dy\wedge dz+\big((\operatorname{rot}\vec B-\partial_t\vec E)_x-j_x\big)\,dt\wedge dy\wedge dz$$
> $$\qquad\qquad+\big((\operatorname{rot}\vec B-\partial_t\vec E)_y-j_y\big)\,dt\wedge dz\wedge dx+\big((\operatorname{rot}\vec B-\partial_t\vec E)_z-j_z\big)\,dt\wedge dx\wedge dy.$$
> By linear independence of the four basis $3$-forms, $d\star F+J=0$ holds if and only if all four coefficients vanish. The first gives $\operatorname{div}\vec E=\varrho$, Coulomb's (Gauss's) law, equation (3.9). The remaining three give the three components of $\operatorname{rot}\vec B-\partial_t\vec E=\vec j$, Ampère's law with Maxwell's displacement current, equation (3.10). This proves part (iii).
>
> **Conclusion.** The homogeneous form equation $dF=0$ is equivalent to (3.7) and (3.8), and the inhomogeneous form equation $d\star F+J=0$ is equivalent to (3.9) and (3.10). Hence the two [[Def - Maxwell Equations in Form Language|Maxwell equations in form language]] are equivalent, in any inertial coordinate frame on Minkowski space, to the four classical Maxwell equations. $\blacksquare$

> [!warning] Source correction (Bär, p. 84)
> In Bär's printed computation of $dF$, the coefficient of $dt\wedge dy\wedge dz$ appears as "$-\partial_yE_z+\partial_yE_z+\partial_tB_x$", in which the first two terms cancel and leave only $\partial_tB_x$. This is a typographical error: as computed in Lemma 1, the correct coefficient is $\partial_yE_z-\partial_zE_y+\partial_tB_x=(\operatorname{rot}\vec E)_x+\partial_tB_x$, so that the mixed slot carries the full $x$-component of Faraday's law and not merely $\partial_tB_x$. We have used the corrected coefficient throughout. (This is item 15 of the source-typo appendix; a companion misprint, the basis $3$-form of the third mixed slot printed as $dt\wedge dz\wedge dy$ rather than the correctly oriented $dt\wedge dz\wedge dx$, is likewise corrected in Lemma 1 and the statement.)

---

# Cross-Field Exercise Suggestions

**Riemannian magnetostatics on a $3$-manifold.** Drop the time direction and work on oriented Riemannian $\mathbb R^3$ with a $2$-form $\beta=\iota_{\vec B}\,dV$. Here the four-dimensional Lemma 1 degenerates to the purely spatial statement $d\beta=(\operatorname{div}\vec B)\,dV$, one instance of the [[Def - Frankel Dictionary (Forms vs Vector Calculus)|Frankel dictionary]]. The theorem applies because the electric–magnetic split is exactly the split of $\Lambda^2$ into time-mixed and purely spatial parts; it is non-obvious that the four-dimensional divergence-and-curl formula contains the three-dimensional one as its zero-time-derivative shadow. This is a good drill on why $\operatorname{div}\vec B=0$ is the statement "$\vec B$ is a closed flux $2$-form".

**General relativity: the source-free Maxwell equations on a curved spacetime.** On a general oriented Lorentzian $4$-manifold, $dF=0$ still holds by the Bianchi identity, but $d\star F$ now involves the metric through $\star$. The theorem's part (i) transfers verbatim in a local inertial frame, while part (iii) acquires curvature corrections; the exercise is to see which of the four laws is frame-independent (the homogeneous pair) and which mixes with the geometry (the inhomogeneous pair). It is non-obvious that half of electromagnetism is insensitive to gravity while the other half couples to the metric precisely through the Hodge star.

**Cohomology and the Aharonov–Bohm effect.** On $\mathbb R^{1,3}$ minus a timelike line (an idealised infinite solenoid), a field strength with $dF=0$ need not be exact: its de Rham class in $H^2$ can be nontrivial. Part (i) guarantees the homogeneous laws hold, yet no global potential $A$ with $F=dA$ need exist. The theorem is the tool that certifies $dF=0$ locally; the exercise is to combine it with [[Thm - The Poincaré Lemma on a Star-Shaped Region|the Poincaré lemma]] to show potentials exist locally but the obstruction to a global one is cohomological. It is non-obvious that the same closed field strength that satisfies every classical law can still detect the topology of the region.

---

# Bridges

- **The homogeneous laws are the Bianchi identity.** Part (i) says $dF=0$ decodes into Gauss's law for magnetism and Faraday's law. On [[Def - Maxwell Equations in Form Language]] and [[Thm - Bianchi Identity for a Principal Connection]] it is shown that $dF=0$ is automatic for any $U(1)$-curvature, because the abelian Bianchi identity $d^\omega\Omega=0$ reduces to $d\bar\Omega=0$ when the adjoint action is trivial. This page is the bridge that turns that structural identity into two of the four experimentally famous laws: the construction is to write the descended curvature in a frame and apply Lemma 1.

- **The inhomogeneous law is the Euler–Lagrange equation.** Part (iii) decodes $d\star F+J=0$ into Coulomb's and Ampère's laws. On [[Thm - Euler-Lagrange Equation of the Electromagnetic Action]] this form equation is derived as the critical-point condition of the action $\int(\tfrac12 F\wedge\star F+A\wedge J)$, with the Hodge-star pairing property moving the variation onto $d\star F$. The bridge is that "the field is critical for the action" and "the field obeys Coulomb and Ampère" are the same statement, connected by the present coordinate translation.

- **Charge conservation is the closedness of $J$.** Applying $d$ to $d\star F+J=0$ and using $d^2=0$ ([[Thm - d-Squared-is-Zero]]) gives $dJ=0$, which by the coordinate computation of Lemma 1 applied to the $3$-form $J$ is the continuity equation $\partial_t\varrho+\operatorname{div}\vec j=0$. The full construction, including the integral form of charge conservation via Stokes' theorem, is [[Thm - Continuity Equation and Conservation of Charge]]; the bridge is that conservation of charge is forced by the inhomogeneous law and the nilpotence of $d$, needing no independent postulate.

- **The same computation in the opposite signature.** The special-relativity chapter proves the identical equivalence with signature $(+,-,-,-)$, SI units, and the Riemannian-style star $\star_V$, in [[Ex - Maxwell's equations in three-dimensional form]] and [[Thm - Maxwell Equations]]; the differential-geometry chapter does it as a forms exercise in [[Ex - Maxwell's Equations as Two Form Equations on Minkowski Space]]. The bridge between them is the dictionary $g_B=-g_{SR}$, $\star_B=-\star_V$ on Minkowski $2$-forms, and the $J$-versus-$j$ sign of [[Def - Charge-Current 3-Form]]; every sign that differs between the two treatments is accounted for by that dictionary, and the four laws obtained are the same.

- **The abelian rehearsal for Yang–Mills.** In §7.4 the field strength becomes $\mathfrak g$-valued and the inhomogeneous equation becomes the covariant $d^A\star F=0$ ([[Thm - Yang-Mills Equation from the Action Principle]]). The coordinate skeleton — divergence in the spatial slot, curl plus time derivative in the mixed slots — is exactly the present one; only the flat $d$ is upgraded to the covariant $d^A$ and the coefficients take values in $\mathfrak g$. The bridge is that Maxwell's equations are the $U(1)$, hence linear, case of the Yang–Mills equation, and this page is where the reader sees the linear skeleton bare.

---

# Unlocked by This

> [!tip] Electromagnetic duality *(from Mathematical Physics)*
> Part (ii)'s statement that $\star$ acts on Minkowski $2$-forms by $(\vec E,\vec B)\mapsto(\vec B,-\vec E)$ is the infinitesimal generator of the **duality rotation** $(\vec E,\vec B)\mapsto(\vec E\cos\theta+\vec B\sin\theta,\ \vec B\cos\theta-\vec E\sin\theta)$ that maps vacuum solutions of Maxwell's equations to vacuum solutions. Because $\star^2=-1$ on Minkowski $2$-forms (Lemma 2's consistency check), $\star$ plays the role of the imaginary unit, and the duality group is a circle. This is the seed of $S$-duality in gauge theory. See **Self-dual and anti-self-dual fields** in §7.1.

> [!tip] The wave equation for light *(from Electrodynamics)*
> Setting $J=0$ and combining the four laws from parts (i) and (iii) — take the curl of Faraday's law and substitute Ampère's — yields $\partial_t^2\vec E-\Delta\vec E=0$, the wave equation with propagation speed $c=1$. The theorem is the step that makes the four scalar equations available for this manipulation; the plane-wave solutions are constructed in **[[Ex - Maxwell's Equations on Minkowski Space from the Two Form Equations]]**.
