---
type: theorem
subject: gauge-theory
prereqs:
  - "Thm - Chern-Weil Theorem"
  - "Thm - Curvature of a Shifted Connection"
  - "Def - Lie-Algebra-Valued Differential Forms and Their Bracket"
  - "Thm - Graded Antisymmetry and Jacobi Identity for Lie-Algebra-Valued Forms"
  - "Def - Ad-Invariant Polynomial"
  - "Def - Chern-Weil Form of an Invariant Polynomial"
  - "Thm - Bianchi Identity for a Principal Connection"
  - "Thm - Structure Equation for the Curvature"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $\pi\colon P\to M$ is a principal $G$-bundle over a smooth manifold $M$, with $G$ a connected [[Def - Lie Group|Lie group]] and Lie algebra $\mathfrak{g}=T_eG$; for concreteness the reader may keep $G=SU(2)$ or $G=U(r)$ in mind, both of which are connected and are the only groups this chapter uses. A [[Def - Connection on a Principal Bundle|connection]] on $P$ is a $\mathfrak{g}$-valued $1$-form $\omega\in\Omega^1(P;\mathfrak{g})$ with $\omega(\xi_P)=\xi$ for the [[Def - Fundamental Vector Field of a Group Action|fundamental vector field]] $\xi_P$ of every $\xi\in\mathfrak{g}$ and $R_g^*\omega=\operatorname{Ad}_{g^{-1}}\omega$; its [[Def - Curvature of a Principal Connection|curvature]] is $F_\omega=\mathrm{d}\omega+\tfrac12[\omega\wedge\omega]\in\Omega^2(P;\mathfrak{g})$, computed by the [[Thm - Structure Equation for the Curvature|structure equation]]. Here $[\,\cdot\wedge\cdot\,]$ is the [[Def - Lie-Algebra-Valued Differential Forms and Their Bracket|bracket of Lie-algebra-valued forms]]: for $\alpha\in\Omega^p(P;\mathfrak{g})$ and $\beta\in\Omega^q(P;\mathfrak{g})$ written in a basis $\{e_a\}$ of $\mathfrak{g}$ as $\alpha=\alpha^a e_a$, $\beta=\beta^b e_b$ (Einstein summation over $a,b$), one has $[\alpha\wedge\beta]=\alpha^a\wedge\beta^b\,[e_a,e_b]$.

The [[Def - Exterior Covariant Derivative on a Principal Bundle|exterior covariant derivative]] of a $\mathfrak{g}$-valued form $\Phi$ with respect to $\omega$, acting on $\operatorname{Ad}$-equivariant forms, is written $\mathrm{d}^\omega\Phi=\mathrm{d}\Phi+[\omega\wedge\Phi]$. A $\mathfrak{g}$-valued form on $P$ is **tensorial** (equivalently **basic**) if it is horizontal (it vanishes when any argument is vertical) and $\operatorname{Ad}$-equivariant ($R_g^*\Phi=\operatorname{Ad}_{g^{-1}}\Phi$); a tensorial form descends to a unique form on $M$ with values in the [[Def - Associated Bundle|adjoint bundle]] $\operatorname{ad}P=P\times_{\operatorname{Ad}}\mathfrak{g}$, and we write $\Omega^k(M;\operatorname{ad}P)$ for these.

A polynomial $p\in I(G)$ is an [[Def - Ad-Invariant Polynomial|Ad-invariant homogeneous polynomial]] $p\colon\mathfrak{g}\to\mathbb{K}$ (with $\mathbb{K}=\mathbb{R}$ or $\mathbb{C}$) of degree $d$; we identify $p$ with its **polarisation**, the unique symmetric $d$-linear form $p\colon\mathfrak{g}^{\times d}\to\mathbb{K}$ whose restriction to the diagonal is the original polynomial, so that $p(\xi)=p(\xi,\dots,\xi)$. For tensorial $\mathfrak{g}$-valued forms $\Phi_1,\dots,\Phi_d$ we write $p(\Phi_1,\dots,\Phi_d):=p(e_{b_1},\dots,e_{b_d})\,\Phi_1^{b_1}\wedge\cdots\wedge\Phi_d^{b_d}$, an ordinary (scalar-valued) form; it is basic and descends to $M$, and $p(F_\omega):=p(F_\omega,\dots,F_\omega)\in\Omega^{2d}(M)$ is the [[Def - Chern-Weil Form of an Invariant Polynomial|Chern–Weil form]] of $\omega$.

> [!warning] Convention: two symbols read "d"
> The italic $d$ always denotes the degree $\deg p$ of the invariant polynomial, an integer. The upright $\mathrm{d}$ always denotes the exterior derivative, and $\mathrm{d}t$ the Lebesgue measure in the interpolation parameter $t\in[0,1]$. The transgression form carries an integer factor $d$ **and** an outer exterior derivative $\mathrm{d}$; keeping the two typefaces apart is essential to reading the statement.

> [!warning] Convention: signs of the bracket and the structure equation
> We follow the series convention (Haydys): the bracket of two $\mathfrak{g}$-valued $1$-forms satisfies $[\alpha\wedge\beta](X,Y)=[\alpha(X),\beta(Y)]-[\alpha(Y),\beta(X)]$, so $[\alpha\wedge\alpha](X,Y)=2[\alpha(X),\alpha(Y)]$ and the structure equation carries the factor $\tfrac12$, $F_\omega=\mathrm{d}\omega+\tfrac12[\omega\wedge\omega]$. For a matrix group, $\tfrac12[\alpha\wedge\alpha]=\alpha\wedge\alpha$ (matrix multiplication of entries), so on a trivialisation $F_A=\mathrm{d}A+A\wedge A$ with $A$ the local connection form. Sources that write $F=\mathrm{d}A+A\wedge A$ without a $\tfrac12$ have silently used this matrix identity; no numerical value changes.

---

# Statement

> **Theorem (transgression formula).** Let $P\to M$ be a principal $G$-bundle with $G$ connected, let $\omega_0,\omega_1$ be connections on $P$, and set
> $$b:=\omega_1-\omega_0\in\Omega^1(P;\mathfrak{g}),\qquad \omega_t:=\omega_0+tb\ \ (t\in[0,1]),\qquad F_t:=F_{\omega_t}=\mathrm{d}\omega_t+\tfrac12[\omega_t\wedge\omega_t].$$
> Then $b$ is tensorial (so it descends to an element of $\Omega^1(M;\operatorname{ad}P)$), each $\omega_t$ is a connection, and for every $p\in I(G)$ of degree $d$ the Chern–Weil forms of the two endpoints differ by an exact form with an explicit primitive:
> $$p(F_1)-p(F_0)=\mathrm{d}\,Tp(\omega_0,\omega_1),\qquad Tp(\omega_0,\omega_1):=d\int_0^1 p(b,F_t,\dots,F_t)\,\mathrm{d}t\ \in\ \Omega^{2d-1}(M).$$
> The $(2d-1)$-form $Tp(\omega_0,\omega_1)$ is called the **transgression form** (or Chern–Simons transgression) of the pair $(\omega_0,\omega_1)$ and $p$.

> **Corollary (the Chern–Simons $3$-form).** Let $G$ be a matrix group and take the degree-$2$ polynomial $p(\xi)=\operatorname{tr}(\xi^2)$, whose polarisation is $p(\xi,\eta)=\operatorname{tr}(\xi\eta)$. On the trivial bundle $M\times G$ let $\omega_0$ be the product connection (local form $0$) and let $\omega_1$ have local connection form $A\in\Omega^1(M;\mathfrak{g})$. Then $F_0=0$, $F_1=F_A=\mathrm{d}A+A\wedge A$, and the transgression formula specialises to Haydys's identity (97):
> $$\operatorname{tr}(F_A\wedge F_A)=\mathrm{d}\operatorname{tr}\!\Big(A\wedge\mathrm{d}A+\tfrac23\,A\wedge A\wedge A\Big).$$
> The $3$-form
> $$\operatorname{cs}(A):=\operatorname{tr}\!\Big(A\wedge\mathrm{d}A+\tfrac23\,A\wedge A\wedge A\Big)=Tp(\omega_0,\omega_1)$$
> is the **Chern–Simons form** of $A$; the corollary says it transgresses the second Chern–Weil form, $\mathrm{d}\operatorname{cs}(A)=\operatorname{tr}(F_A\wedge F_A)$.

---

# Motivation

The [[Thm - Chern-Weil Theorem|Chern–Weil theorem]] proves two things about the Chern–Weil form $p(F_\omega)$ of an invariant polynomial: that it is closed, and that its de Rham class $[p(F_\omega)]\in H^{2d}_{\mathrm{dR}}(M)$ does not depend on the connection $\omega$. The second statement is what makes $p\mapsto[p(F_\omega)]$ an invariant of the bundle rather than of the connection. But that proof establishes independence *abstractly*: it shows the difference $p(F_{\omega_1})-p(F_{\omega_0})$ is exact by transporting the problem to the cylinder $M\times[0,1]$ and quoting the homotopy invariance of de Rham cohomology. It never writes down the primitive. The present theorem repairs exactly this: it produces the antiderivative in closed form.

Why is an *explicit* primitive worth having when the abstract one already gives the invariance we wanted? Because the primitive is a geometric object in its own right. Once we know $p(F_1)-p(F_0)=\mathrm{d}\,Tp$, three things become possible that the bare exactness statement cannot deliver. First, on a closed manifold Stokes' theorem turns the identity into the numerical statement $\int_M p(F_1)=\int_M p(F_0)$, so the *characteristic numbers* (not just the classes) are connection-independent — this is the mechanism behind the integrality of the second Chern number and the quantisation of instanton charge. Second, on a manifold with boundary the primitive survives as a genuine boundary contribution: the four-dimensional integral $\int_X\operatorname{tr}(F\wedge F)$ collapses to $\int_{\partial X}\operatorname{cs}(A)$, and this boundary term, read on the three-manifold alone, is the [[Def - Chern-Simons Functional|Chern–Simons functional]]. Third, when $\omega_0$ and $\omega_1$ are gauge-equivalent the two Chern–Weil forms are actually equal, so $\mathrm{d}\,Tp=0$ and $Tp$ becomes a *closed* form whose periods are new invariants — the secondary, or Chern–Simons, invariants that measure the gauge transformation.

The corollary isolates the case that dominates the rest of the chapter and all of low-dimensional gauge theory: the second Chern–Weil form $\operatorname{tr}(F\wedge F)$ of a matrix group, and its explicit primitive $\operatorname{cs}(A)=\operatorname{tr}(A\wedge\mathrm{d}A+\tfrac23A^{\wedge3})$. This is the object Haydys writes down when he gives the three-dimensional formula for the Chern–Simons functional (his D3.2.2): the functional is, by definition, the integral of $\operatorname{cs}(A)$ over a three-manifold. Everything the functional does — its gauge variation counting the degree of $g\colon M\to SU(2)$, its critical points being the flat connections, its role as the boundary term of the Yang–Mills action — rests on the single identity $\mathrm{d}\operatorname{cs}(A)=\operatorname{tr}(F_A\wedge F_A)$ proved here.

---

# Sources and Targets

**Sources (Input Broadening).** The literal hypothesis is mild — any two connections and any invariant polynomial — so the skill is recognising when a problem hands you a second connection, or a whole path of connections, without naming one.

The first disguised source is **a bundle equipped with a trivialisation, even a local one**. A trivialisation of $P$ over an open set $U\subseteq M$ singles out a canonical flat connection there, the product connection $\omega_0$ with local form $0$; any other connection $\omega_1$ with local form $A$ is then automatically part of the pair $(\omega_0,\omega_1)$. The non-obvious bridge is that the product connection is *always available on a trivialising set* and its curvature vanishes, so the transgression formula immediately exhibits a local primitive of any Chern–Weil form: $p(F_A)=\mathrm{d}\,Tp$ on $U$. *Example problem:* on the total space of any principal bundle, or on any contractible chart, show that every Chern–Weil form is exact and write the primitive — the answer is $Tp$ against the product connection.

The second disguised source is **a smooth family of connections, or a rescaling**. Whenever a problem produces connections depending on a parameter — a physical coupling $A\mapsto sA$ turned on adiabatically, an interpolation between an ansatz and a solution, a deformation of a flat connection — the affine path $\omega_t=\omega_0+t(\omega_1-\omega_0)$ that the theorem uses is exactly such a family, and $b=\omega_1-\omega_0$ is constant in $t$, so the transgression integral $\int_0^1 p(b,F_t,\dots,F_t)\,\mathrm{d}t$ is a *polynomial in $t$ integrated termwise*. The bridge is that "a family of connections" always contains its two endpoints, and the difference of the endpoint invariants is computed by an elementary one-variable integral. *Example problem:* for the rescaling $\omega_t=t\omega_1$ on a trivial bundle, recover $\operatorname{cs}(A)=\operatorname{tr}(A\wedge\mathrm{d}A+\tfrac23A^{\wedge3})$ by integrating $\int_0^1 t\,\mathrm{d}A+t^2A\wedge A$ against $2\operatorname{tr}(A\wedge\,\cdot\,)$, obtaining the coefficients $\tfrac12$ and $\tfrac23$.

The third disguised source is **two gauge-equivalent connections**. If $\omega_1=\omega_0\cdot g$ is the image of $\omega_0$ under a [[Def - Gauge Transformation|gauge transformation]] $g$, then by [[Thm - Naturality and Isomorphism Invariance of Characteristic Classes|isomorphism invariance]] the two Chern–Weil forms are *equal*, $p(F_1)=p(F_0)$, so $\mathrm{d}\,Tp=0$: the transgression form is closed. The bridge — non-obvious because it turns a triviality ($0=0$ at the level of classes) into content ($Tp$ is a closed form with possibly non-zero periods) — is that the transgression of a pair related by a gauge transformation is a *secondary invariant* whose de Rham class detects the gauge transformation itself. *Example problem:* for $G=SU(2)$ over a closed three-manifold and $\omega_1=\omega_0\cdot g$, show $\int_M Tp$ is an integer multiple of $8\pi^2$ counting the degree of $g\colon M\to SU(2)\cong S^3$; this is the engine of the [[Thm - Gauge Variation of the Chern-Simons Functional|gauge variation]] of the Chern–Simons functional.

**Targets (Output Amplification).** The bare conclusion is one exactness identity. Combined with a single further ingredient it becomes each of the chapter's headline results.

Combine the identity with **Stokes' theorem on a closed manifold**. If $M$ is closed (compact, no boundary), then $\int_M\mathrm{d}\,Tp=0$ by [[Thm - Stokes' Theorem on Manifolds|Stokes' theorem]], so $\int_M p(F_1)=\int_M p(F_0)$: the characteristic *number* is independent of the connection. The extra ingredient is compactness without boundary; the payoff is that $\tfrac1{8\pi^2}\int_M\operatorname{tr}(F_A\wedge F_A)$ is a connection-independent invariant, which the [[Thm - Second Chern Number of an SU(2)-Bundle over a Closed Four-Manifold is the Clutching Degree|clutching theorem]] then identifies with an integer — the second Chern number.

Combine the identity with **a four-manifold with boundary**. If $\partial X=M$ and $A_X$ is a connection on $X$ restricting to $A$ on $M$, then, where $X$ is trivialised, $\int_X\operatorname{tr}(F_{A_X}\wedge F_{A_X})=\int_X\mathrm{d}\operatorname{cs}(A_X)=\int_{\partial X}\operatorname{cs}(A)$ by Stokes. The extra ingredient is a bounding manifold and an extension of the connection; the payoff is the [[Thm - The Four-Dimensional Formula for the Chern-Simons Functional|four-dimensional formula]] $\vartheta(A)\equiv\tfrac1{8\pi^2}\int_X\operatorname{tr}(F_{A_X}\wedge F_{A_X})\pmod{\mathbb{Z}}$, the boundary reading of the Chern–Simons functional.

Combine the identity with **the Yang–Mills energy and the Hodge star** (chapter VII). On a closed oriented four-manifold, $|F|^2=|F^+|^2+|F^-|^2$ and $\operatorname{tr}(F\wedge F)$ is a fixed multiple of $(|F^+|^2-|F^-|^2)\,\mathrm{vol}$, so the topological term $\int\operatorname{tr}(F\wedge F)$ — connection-independent by the previous target — splits the Yang–Mills energy $\tfrac12\int|F|^2$ into a topological piece plus a non-negative remainder. The extra ingredient is the self-dual/anti-self-dual decomposition; the payoff is the topological lower bound $\mathcal{YM}(A)\ge 4\pi^2|k|$ with equality for (anti-)self-dual connections, the starting point of instanton theory.

---

# Why Is It True

Forget the cylinder argument of the Chern–Weil theorem and watch the Chern–Weil form move as we slide the connection from $\omega_0$ to $\omega_1$ along the straight path $\omega_t=\omega_0+tb$. The Chern–Weil form $p(F_t)$ is a function of $t$ valued in forms on $M$; the difference $p(F_1)-p(F_0)$ is, by the fundamental theorem of calculus, the integral of its $t$-derivative. So everything comes down to computing $\tfrac{\mathrm d}{\mathrm dt}p(F_t)$ and recognising it as an exact form.

Two facts do all the work. First, the curvature moves by a covariant derivative: $\tfrac{\mathrm d}{\mathrm dt}F_t=\mathrm{d}^{\omega_t}b$. This is not a coincidence; it is the infinitesimal form of the shifted-connection formula, and it says the velocity of the curvature along the path is the covariant derivative of the velocity of the connection. Second, when we differentiate $p(F_t,\dots,F_t)$ by the product rule and use this, we get $d$ equal terms $p(\mathrm{d}^{\omega_t}b,F_t,\dots,F_t)$, and this quantity is *itself* an exact form — its primitive is $p(b,F_t,\dots,F_t)$. The reason it is exact is the interplay of the two structural identities of gauge theory: the **Bianchi identity** $\mathrm{d}^{\omega_t}F_t=0$ says the curvature is covariantly constant, so when we differentiate $p(b,F_t,\dots,F_t)$ the curvature slots contribute nothing; and the **invariance identity** (the infinitesimal $\operatorname{Ad}$-invariance of $p$) says the connection terms hidden inside $\mathrm{d}$ versus $\mathrm{d}^{\omega_t}$ cancel when summed over the slots of $p$. What is left is precisely $p(\mathrm{d}^{\omega_t}b,F_t,\dots,F_t)$.

> **Mechanism in one sentence:** the derivative of the Chern–Weil form along a path of connections is exact because Bianchi makes the curvature invisible to $\mathrm{d}$ and invariance makes the connection invisible to $p$, leaving an honest total derivative that the fundamental theorem of calculus integrates.

The corollary makes this concrete in the smallest case. Take $p=\operatorname{tr}(\cdot^2)$ and slide from the flat product connection ($A_0=0$, $F_0=0$) to $A$. The path is $tA$, its curvature is $t\,\mathrm{d}A+t^2A\wedge A$, and the transgression integral is a pair of elementary moment integrals $\int_0^1 t\,\mathrm{d}t=\tfrac12$ and $\int_0^1 t^2\,\mathrm{d}t=\tfrac13$. The numbers $\tfrac12$ and $\tfrac23$ in $\operatorname{cs}(A)=\operatorname{tr}(A\wedge\mathrm{d}A+\tfrac23A^{\wedge3})$ are literally these moments (the $\tfrac23$ is $2\times\tfrac13$, the factor $2$ coming from the degree $d=2$). The Chern–Simons form is nothing more mysterious than the antiderivative of $\operatorname{tr}(F\wedge F)$ read off by rescaling the connection.

---

# What Makes This Hard

The one genuinely non-obvious step is the identity $\mathrm{d}\,p(b,F_t,\dots,F_t)=p(\mathrm{d}^{\omega_t}b,F_t,\dots,F_t)$: it looks as though differentiating a product of $d$ factors ought to produce $d$ terms, one hitting each factor, yet only the term hitting $b$ survives. The two vanishing mechanisms are different and are easy to conflate — the curvature terms die by the *Bianchi identity* (a property of $\omega_t$), while the discrepancy between the ordinary and the covariant exterior derivative dies by the *invariance identity* (a property of $p$) — and a proof that invokes only one of them is incomplete. The common error is to forget the sign bookkeeping when promoting the pointwise infinitesimal invariance $\sum_j p(\dots,[\xi,\xi_j],\dots)=0$ to $\mathfrak{g}$-valued forms of mixed degree: because $b$ has odd degree $1$ while the $F_t$ have even degree $2$, the graded Leibniz signs $(-1)^{q_1+\cdots+q_{j-1}}$ are not all $+1$, and they must be tracked to see that the form-valued invariance identity is exactly the combination the computation needs. The second subtlety is descent: every form in sight lives a priori on the total space $P$, and one must check that $b$, the $F_t$, and the polynomial expressions are basic before speaking of forms on $M$.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Interpolate linearly between the two connections, differentiate the Chern–Weil form in the interpolation parameter, show the derivative is the exterior derivative of a $t$-dependent primitive, and integrate the parameter out. The whole difficulty is the single algebraic identity that turns the $t$-derivative into a total exterior derivative; it is delivered by the Bianchi identity and the infinitesimal invariance of $p$.

**Subgoal decomposition:**

1. **The path is legitimate and $b$ descends.** Check each $\omega_t$ is a connection and $b=\omega_1-\omega_0$ is tensorial.
   - *Hint:* Connections form an affine space; the difference of two of them kills fundamental vector fields and is $\operatorname{Ad}$-equivariant.
   - *Why needed:* Without this the curvatures $F_t$ and the descended forms on $M$ are not even defined.

2. **Velocity of the curvature.** Show $\tfrac{\mathrm d}{\mathrm dt}F_t=\mathrm{d}^{\omega_t}b$.
   - *Hint:* Expand $F_t$ by the structure equation, or use the shifted-curvature formula, then differentiate in $t$; the bracket term rebuilds the covariant derivative.
   - *Why needed:* It is the only place the specific path enters; it converts a $t$-derivative into a covariant derivative.

3. **Form-valued infinitesimal invariance.** Promote the pointwise identity (83) to $\mathfrak{g}$-valued forms, with the graded signs.
   - *Hint:* Expand every form in a basis of $\mathfrak{g}$, move the scalar $1$-form to the front (this is where the signs come from), and apply (83) to the coefficients.
   - *Why needed:* It is the mechanism that cancels the connection terms in the next subgoal.

4. **The transgression differential identity.** Show $\mathrm{d}\,p(b,F_t,\dots,F_t)=p(\mathrm{d}^{\omega_t}b,F_t,\dots,F_t)$.
   - *Hint:* Apply the graded Leibniz rule; rewrite $\mathrm{d}b=\mathrm{d}^{\omega_t}b-[\omega_t\wedge b]$ and $\mathrm{d}F_t=-[\omega_t\wedge F_t]$ (Bianchi); the bracket terms are exactly subgoal 3.
   - *Why needed:* This is the heart; it makes the derivative of the Chern–Weil form manifestly exact.

5. **Differentiate, assemble, integrate.** Combine subgoals 2 and 4 into $\tfrac{\mathrm d}{\mathrm dt}p(F_t)=\mathrm{d}\big(d\,p(b,F_t,\dots,F_t)\big)$; integrate over $t\in[0,1]$, moving $\mathrm{d}$ outside the integral.
   - *Hint:* Product rule and symmetry of $p$ give the factor $d$; the fundamental theorem of calculus and differentiation under the integral sign finish it.
   - *Why needed:* It produces the stated primitive $Tp$.

6. **The corollary.** Specialise to $p=\operatorname{tr}(\cdot^2)$, $\omega_0$ the product connection, and read off $\operatorname{cs}(A)$; verify the identity independently by direct expansion.
   - *Hint:* $F_0=0$, $F_1=F_A$; the moment integrals $\int_0^1 t\,\mathrm{d}t$, $\int_0^1 t^2\,\mathrm{d}t$ give the coefficients; for the check, expand $\mathrm{d}\operatorname{cs}(A)$ and $\operatorname{tr}(F_A\wedge F_A)$ using cyclicity and $\operatorname{tr}(A^{\wedge4})=0$.
   - *Why needed:* It is the form of the theorem the chapter actually uses, and Haydys's (97).

---

# Lemma Decomposition

> [!note]- Lemma 1: Each $\omega_t$ is a connection and $b$ is tensorial
> **Statement:** With $\omega_0,\omega_1$ connections and $b=\omega_1-\omega_0$, every $\omega_t=\omega_0+tb$ ($t\in[0,1]$) is a connection on $P$, and $b$ is horizontal and $\operatorname{Ad}$-equivariant, hence descends to $b\in\Omega^1(M;\operatorname{ad}P)$.
>
> **Hint:** Subtract the two defining conditions of a connection; the fundamental-field condition becomes $b(\xi_P)=0$ and the equivariance conditions subtract to give equivariance of $b$. Convex combinations then satisfy both connection conditions.
>
> **Why needed:** It licenses the curvatures $F_t$ and the descent of every form in the proof to $M$.
>
> > [!note]- Full proof
> > **Horizontality of $b$.** For $\xi\in\mathfrak{g}$ with fundamental vector field $\xi_P$, both connections satisfy $\omega_0(\xi_P)=\xi$ and $\omega_1(\xi_P)=\xi$ (defining property of a connection). Subtracting, $b(\xi_P)=\omega_1(\xi_P)-\omega_0(\xi_P)=\xi-\xi=0$ (definition of $b$). Since the vertical subspace $V_pP$ is spanned by the values $\xi_P(p)$ of fundamental vector fields ($p\mapsto\xi_P(p)$ is an isomorphism $\mathfrak{g}\to V_pP$), $b$ vanishes on all vertical vectors, so $b$ is horizontal.
> >
> > **Equivariance of $b$.** Each connection satisfies $R_g^*\omega_i=\operatorname{Ad}_{g^{-1}}\omega_i$ ($i=0,1$; defining property). Subtracting, $R_g^*b=R_g^*\omega_1-R_g^*\omega_0=\operatorname{Ad}_{g^{-1}}\omega_1-\operatorname{Ad}_{g^{-1}}\omega_0=\operatorname{Ad}_{g^{-1}}b$ (linearity of $\operatorname{Ad}_{g^{-1}}$ and of pull-back). Thus $b$ is $\operatorname{Ad}$-equivariant. A horizontal $\operatorname{Ad}$-equivariant $\mathfrak{g}$-valued form is tensorial and descends to a unique $\operatorname{ad}P$-valued form on $M$ (this is the defining property of the [[Def - Associated Bundle|adjoint bundle]] $\operatorname{ad}P=P\times_{\operatorname{Ad}}\mathfrak{g}$).
> >
> > **Each $\omega_t$ is a connection.** Write $\omega_t=(1-t)\omega_0+t\omega_1$, a convex combination. For the fundamental-field condition, $\omega_t(\xi_P)=(1-t)\omega_0(\xi_P)+t\omega_1(\xi_P)=(1-t)\xi+t\xi=\xi$. For equivariance, $R_g^*\omega_t=(1-t)R_g^*\omega_0+tR_g^*\omega_1=(1-t)\operatorname{Ad}_{g^{-1}}\omega_0+t\operatorname{Ad}_{g^{-1}}\omega_1=\operatorname{Ad}_{g^{-1}}\omega_t$. Both connection conditions hold, so $\omega_t$ is a connection. (Equivalently: the [[Thm - The Space of Connections is an Affine Space|space of connections is affine]] over $\Omega^1(M;\operatorname{ad}P)$, and $\omega_t=\omega_0+tb$ with $b$ tensorial is a point of it.) $\ \blacksquare$

> [!note]- Lemma 2: Velocity of the curvature along the path
> **Statement:** $\dfrac{\mathrm d}{\mathrm dt}F_t=\mathrm{d}^{\omega_t}b:=\mathrm{d}b+[\omega_t\wedge b]$.
>
> **Hint:** Expand $F_t$ by the structure equation and differentiate; $\tfrac{\mathrm d}{\mathrm dt}\tfrac12[\omega_t\wedge\omega_t]=[\omega_t\wedge b]$ because the bracket of two $\mathfrak{g}$-valued $1$-forms is graded-symmetric.
>
> **Why needed:** It is the sole point where the affine path enters, converting the $t$-derivative into a covariant exterior derivative.
>
> > [!note]- Full proof
> > **Expand the curvature.** By the [[Thm - Structure Equation for the Curvature|structure equation]], $F_t=\mathrm{d}\omega_t+\tfrac12[\omega_t\wedge\omega_t]$. Differentiate in $t$, using $\tfrac{\mathrm d}{\mathrm dt}\omega_t=b$ (definition of $\omega_t=\omega_0+tb$) and that $\mathrm{d}$ (exterior derivative on $P$) commutes with $\tfrac{\mathrm d}{\mathrm dt}$ (they act on different variables):
> > $$\frac{\mathrm d}{\mathrm dt}F_t=\mathrm{d}\Big(\frac{\mathrm d}{\mathrm dt}\omega_t\Big)+\frac12\,\frac{\mathrm d}{\mathrm dt}[\omega_t\wedge\omega_t]=\mathrm{d}b+\frac12\frac{\mathrm d}{\mathrm dt}[\omega_t\wedge\omega_t]\qquad(\text{Leibniz in }t;\ \tfrac{\mathrm d}{\mathrm dt}\omega_t=b).$$
> >
> > **Differentiate the bracket.** The bracket is bilinear in its two form-arguments, so $\tfrac{\mathrm d}{\mathrm dt}[\omega_t\wedge\omega_t]=[b\wedge\omega_t]+[\omega_t\wedge b]$. For two $\mathfrak{g}$-valued $1$-forms the bracket is graded-symmetric: by [[Thm - Graded Antisymmetry and Jacobi Identity for Lie-Algebra-Valued Forms|graded antisymmetry]], $[\alpha\wedge\beta]=-(-1)^{pq}[\beta\wedge\alpha]$ with $p=q=1$, giving $[\alpha\wedge\beta]=[\beta\wedge\alpha]$, so $[b\wedge\omega_t]=[\omega_t\wedge b]$. Hence
> > $$\frac12\frac{\mathrm d}{\mathrm dt}[\omega_t\wedge\omega_t]=\frac12\big([b\wedge\omega_t]+[\omega_t\wedge b]\big)=\frac12\cdot 2[\omega_t\wedge b]=[\omega_t\wedge b]\qquad(\text{graded symmetry of the bracket on }1\text{-forms}).$$
> >
> > **Assemble.** Combining the two displays,
> > $$\frac{\mathrm d}{\mathrm dt}F_t=\mathrm{d}b+[\omega_t\wedge b]=\mathrm{d}^{\omega_t}b\qquad(\text{definition }\mathrm{d}^{\omega_t}\Phi=\mathrm{d}\Phi+[\omega_t\wedge\Phi]).$$
> > As a cross-check consistent with the [[Thm - Curvature of a Shifted Connection|shifted-curvature formula]] $F_{\omega_0+tb}=F_{\omega_0}+t\,\mathrm{d}^{\omega_0}b+\tfrac{t^2}{2}[b\wedge b]$: differentiating the right-hand side in $t$ gives $\mathrm{d}^{\omega_0}b+t[b\wedge b]$, and since $\mathrm{d}^{\omega_t}b=\mathrm{d}b+[\omega_0\wedge b]+t[b\wedge b]=\mathrm{d}^{\omega_0}b+t[b\wedge b]$, the two agree. $\ \blacksquare$

> [!note]- Lemma 3: Form-valued infinitesimal invariance of $p$
> **Statement:** Let $p$ be a symmetric $\operatorname{Ad}$-invariant $d$-linear form on $\mathfrak{g}$, $\psi\in\Omega^1(P;\mathfrak{g})$, and $\Phi_1,\dots,\Phi_d$ homogeneous $\mathfrak{g}$-valued forms of degrees $q_1,\dots,q_d$. Then
> $$\sum_{j=1}^d(-1)^{q_1+\cdots+q_{j-1}}\,p\big(\Phi_1,\dots,[\psi\wedge\Phi_j],\dots,\Phi_d\big)=0.$$
>
> **Hint:** Expand in a basis $\{e_a\}$ of $\mathfrak{g}$; pull the scalar $1$-form coefficient of $\psi$ to the front — this generates exactly the sign $(-1)^{q_1+\cdots+q_{j-1}}$ — and recognise the coefficient as the pointwise identity (83).
>
> **Why needed:** It is the exact cancellation that removes the connection terms in Lemma 4, and it is where the graded signs are forced.
>
> > [!note]- Full proof
> > **The pointwise identity.** Because $p$ is $\operatorname{Ad}$-invariant and $G$ is connected, differentiating the identity $p(\operatorname{Ad}_{\exp(s\xi)}\xi_1,\dots,\operatorname{Ad}_{\exp(s\xi)}\xi_d)=p(\xi_1,\dots,\xi_d)$ at $s=0$ (using $\tfrac{\mathrm d}{\mathrm ds}\big|_0\operatorname{Ad}_{\exp(s\xi)}\eta=[\xi,\eta]$) yields the infinitesimal invariance identity
> > $$\sum_{j=1}^d p(\xi_1,\dots,[\xi,\xi_j],\dots,\xi_d)=0\qquad\text{for all }\xi,\xi_1,\dots,\xi_d\in\mathfrak{g},\tag{83}$$
> > which is proved on [[Def - Ad-Invariant Polynomial|the Ad-invariant polynomial page]] and which we restate and use here.
> >
> > **Expand in a basis.** Fix a basis $\{e_a\}_{a=1}^{n}$ of $\mathfrak{g}$ and write $\psi=\psi^a e_a$ and $\Phi_j=\Phi_j^{b_j}e_{b_j}$ with $\psi^a\in\Omega^1(P)$ and $\Phi_j^{b_j}\in\Omega^{q_j}(P)$ ordinary forms (summation over repeated indices). By definition of the bracket of Lie-algebra-valued forms, $[\psi\wedge\Phi_j]=\psi^a\wedge\Phi_j^{b_j}\,[e_a,e_{b_j}]$, and by $d$-linearity of $p$,
> > $$p\big(\Phi_1,\dots,[\psi\wedge\Phi_j],\dots,\Phi_d\big)=\Phi_1^{b_1}\wedge\cdots\wedge\big(\psi^a\wedge\Phi_j^{b_j}\big)\wedge\cdots\wedge\Phi_d^{b_d}\ \cdot\ p\big(e_{b_1},\dots,[e_a,e_{b_j}],\dots,e_{b_d}\big).$$
> >
> > **Move the scalar $1$-form to the front.** The factor $\psi^a$ is a $1$-form sitting in the $j$-th position, preceded by $\Phi_1^{b_1},\dots,\Phi_{j-1}^{b_{j-1}}$ of total degree $q_1+\cdots+q_{j-1}$. Commuting it to the front costs the sign $(-1)^{q_1+\cdots+q_{j-1}}$ (graded commutativity of the wedge of ordinary forms). Therefore
> > $$(-1)^{q_1+\cdots+q_{j-1}}\,p\big(\Phi_1,\dots,[\psi\wedge\Phi_j],\dots,\Phi_d\big)=\psi^a\wedge\Phi_1^{b_1}\wedge\cdots\wedge\Phi_d^{b_d}\ \cdot\ p\big(e_{b_1},\dots,[e_a,e_{b_j}],\dots,e_{b_d}\big),$$
> > where the scalar form $\psi^a\wedge\Phi_1^{b_1}\wedge\cdots\wedge\Phi_d^{b_d}$ no longer depends on $j$.
> >
> > **Sum over $j$ and apply (83).** Summing over $j=1,\dots,d$ and over the basis indices $a,b_1,\dots,b_d$,
> > $$\sum_{j=1}^d(-1)^{q_1+\cdots+q_{j-1}}p\big(\Phi_1,\dots,[\psi\wedge\Phi_j],\dots,\Phi_d\big)=\sum_{a,b_1,\dots,b_d}\psi^a\wedge\Phi_1^{b_1}\wedge\cdots\wedge\Phi_d^{b_d}\underbrace{\sum_{j=1}^d p\big(e_{b_1},\dots,[e_a,e_{b_j}],\dots,e_{b_d}\big)}_{=\,0\text{ by (83) with }\xi=e_a,\ \xi_i=e_{b_i}}.$$
> > Each inner sum vanishes by (83), so the whole expression is $0$. $\ \blacksquare$

> [!note]- Lemma 4: The transgression differential identity
> **Statement:** On $P$, for each $t$, $\mathrm{d}\,p(b,F_t,\dots,F_t)=p\big(\mathrm{d}^{\omega_t}b,F_t,\dots,F_t\big)$, where $b$ occupies one slot and $F_t$ the remaining $d-1$ slots.
>
> **Hint:** Graded Leibniz gives $d$ terms; the $F_t$-terms carry $\mathrm{d}F_t$, which the Bianchi identity turns into $-[\omega_t\wedge F_t]$, and together with the $\mathrm{d}b$-term the connection contributions form exactly the combination Lemma 3 annihilates.
>
> **Why needed:** It is the identity that makes the derivative of the Chern–Weil form manifestly exact.
>
> > [!note]- Full proof
> > **Graded Leibniz.** Since $p$ is a constant (coefficient-independent) symmetric multilinear map, the exterior derivative passes through it by the graded Leibniz rule for the wedge product, the arguments having degrees $q_1=1$ (for $b$) and $q_2=\cdots=q_d=2$ (for the $F_t$):
> > $$\mathrm{d}\,p(b,F_t,\dots,F_t)=p(\mathrm{d}b,F_t,\dots,F_t)+\sum_{j=2}^d(-1)^{1+2(j-2)}\,p(b,F_t,\dots,\underset{(j)}{\mathrm{d}F_t},\dots,F_t).$$
> > The sign is $(-1)^{1+2(j-2)}=(-1)^{1}=-1$ for every $j\ge2$, so
> > $$\mathrm{d}\,p(b,F_t,\dots,F_t)=p(\mathrm{d}b,F_t,\dots,F_t)-\sum_{j=2}^d p(b,F_t,\dots,\underset{(j)}{\mathrm{d}F_t},\dots,F_t).\tag{$\ast$}$$
> >
> > **Replace ordinary by covariant derivatives.** By the definition of the covariant exterior derivative, $\mathrm{d}b=\mathrm{d}^{\omega_t}b-[\omega_t\wedge b]$. By the [[Thm - Bianchi Identity for a Principal Connection|Bianchi identity]] $\mathrm{d}^{\omega_t}F_t=0$, i.e. $\mathrm{d}F_t+[\omega_t\wedge F_t]=0$, so $\mathrm{d}F_t=-[\omega_t\wedge F_t]$. Substituting into $(\ast)$,
> > $$\mathrm{d}\,p(b,F_t,\dots,F_t)=p(\mathrm{d}^{\omega_t}b,F_t,\dots,F_t)-\Big[\,p([\omega_t\wedge b],F_t,\dots,F_t)-\sum_{j=2}^d p(b,F_t,\dots,\underset{(j)}{[\omega_t\wedge F_t]},\dots,F_t)\Big].$$
> >
> > **The bracket terms vanish.** The bracketed quantity is exactly the left-hand side of Lemma 3 with $\psi=\omega_t$, $\Phi_1=b$ (degree $q_1=1$) and $\Phi_j=F_t$ (degree $q_j=2$) for $j\ge2$: the $j=1$ term is $(-1)^{0}p([\omega_t\wedge b],F_t,\dots,F_t)$, and for $j\ge2$ the sign is $(-1)^{1+2(j-2)}=-1$, giving $-p(b,\dots,[\omega_t\wedge F_t]^{(j)},\dots)$. Hence the bracketed quantity equals $\sum_{j=1}^d(-1)^{q_1+\cdots+q_{j-1}}p(\Phi_1,\dots,[\omega_t\wedge\Phi_j],\dots,\Phi_d)=0$ by Lemma 3. Therefore
> > $$\mathrm{d}\,p(b,F_t,\dots,F_t)=p(\mathrm{d}^{\omega_t}b,F_t,\dots,F_t).\qquad\blacksquare$$

> [!note]- Lemma 5: Descent to $M$ and interchange of $\mathrm{d}$ with $\int_0^1$
> **Statement:** For each $t$ the forms $p(F_t,\dots,F_t)$ and $p(b,F_t,\dots,F_t)$ are basic and descend to forms on $M$ depending smoothly on $t$; the descended families satisfy $\int_0^1\frac{\mathrm d}{\mathrm dt}p(F_t)\,\mathrm{d}t=p(F_1)-p(F_0)$ and $\mathrm{d}\int_0^1 p(b,F_t,\dots,F_t)\,\mathrm{d}t=\int_0^1\mathrm{d}\,p(b,F_t,\dots,F_t)\,\mathrm{d}t$.
>
> **Hint:** Tensoriality of $b$ and $F_t$ plus $\operatorname{Ad}$-invariance of $p$ make the polynomial expressions basic; the fundamental theorem of calculus and differentiation under the integral sign do the rest, both valid because $[0,1]$ is compact and the integrand is smooth.
>
> **Why needed:** It moves the whole computation from $P$ down to $M$ and lets the exterior derivative pass through the parameter integral, producing the primitive $Tp$.
>
> > [!note]- Full proof
> > **Basic-ness and descent.** By Lemma 1, $b$ is tensorial, and each $F_t$ is tensorial (a [[Def - Curvature of a Principal Connection|principal curvature]] is horizontal and $\operatorname{Ad}$-equivariant). For tensorial $\mathfrak{g}$-valued forms $\Phi_1,\dots,\Phi_d$ and an $\operatorname{Ad}$-invariant symmetric $p$, the scalar form $p(\Phi_1,\dots,\Phi_d)$ is horizontal (each $\Phi_i$ is) and $G$-invariant (by $\operatorname{Ad}$-invariance of $p$ and $\operatorname{Ad}$-equivariance of the $\Phi_i$: $R_g^*p(\Phi_1,\dots,\Phi_d)=p(\operatorname{Ad}_{g^{-1}}\Phi_1,\dots,\operatorname{Ad}_{g^{-1}}\Phi_d)=p(\Phi_1,\dots,\Phi_d)$), hence basic; a basic form on $P$ is the pull-back $\pi^*$ of a unique form on $M$, and $\pi^*$ is injective and commutes with $\mathrm{d}$ (this is the descent mechanism used on the [[Thm - Chern-Weil Theorem|Chern–Weil]] and [[Def - Chern-Weil Form of an Invariant Polynomial|Chern–Weil-form]] pages, restated here). Applying this with all slots $F_t$, and with one slot $b$ and the rest $F_t$, gives the two descended families on $M$; they are smooth in $t$ because $F_t=F_0+t\,\mathrm{d}^{\omega_0}b+\tfrac{t^2}{2}[b\wedge b]$ is polynomial in $t$ (Lemma 2's cross-check), so the $p(\cdots)$ are polynomial in $t$ with form coefficients.
> >
> > **Fundamental theorem of calculus.** For each fixed point of $M$ and each fixed multi-index of a coordinate chart, $t\mapsto p(F_t)$ is a smooth $\mathbb{K}$-valued function of $t\in[0,1]$, so $\int_0^1\frac{\mathrm d}{\mathrm dt}p(F_t)\,\mathrm{d}t=p(F_1)-p(F_0)$ by the fundamental theorem of calculus applied coefficientwise.
> >
> > **Differentiation under the integral sign.** In any coordinate chart of $M$, $p(b,F_t,\dots,F_t)=\sum_I c_I(x,t)\,\mathrm{d}x^I$ with each coefficient $c_I$ smooth in $(x,t)$ on a set with $t$ ranging over the compact interval $[0,1]$. The exterior derivative on $M$ differentiates the $c_I$ in the $x$-variables only, while $\int_0^1(\cdot)\,\mathrm{d}t$ integrates in $t$; since $\partial_{x^k}c_I$ is continuous on the compact $t$-interval, differentiation under the integral sign applies to each coefficient, giving $\partial_{x^k}\int_0^1 c_I\,\mathrm{d}t=\int_0^1\partial_{x^k}c_I\,\mathrm{d}t$, and hence $\mathrm{d}\int_0^1 p(b,F_t,\dots,F_t)\,\mathrm{d}t=\int_0^1\mathrm{d}\,p(b,F_t,\dots,F_t)\,\mathrm{d}t$. $\ \blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\omega_0,\omega_1$ be connections on $P\to M$ with $G$ connected, $b=\omega_1-\omega_0$, $\omega_t=\omega_0+tb$, $F_t=F_{\omega_t}$, and $p\in I(G)$ of degree $d$ with polarisation the symmetric $d$-linear form also written $p$. We must show $p(F_1)-p(F_0)=\mathrm{d}\,Tp(\omega_0,\omega_1)$ with $Tp(\omega_0,\omega_1)=d\int_0^1 p(b,F_t,\dots,F_t)\,\mathrm{d}t$, and then read off the corollary.
>
> **Step 0 — well-posedness.** By **Lemma 1**, each $\omega_t$ is a connection, so $F_t$ is defined, and $b$ is tensorial, so it descends to $\Omega^1(M;\operatorname{ad}P)$. By **Lemma 5**, the scalar forms $p(F_t,\dots,F_t)\in\Omega^{2d}(M)$ and $p(b,F_t,\dots,F_t)\in\Omega^{2d-1}(M)$ are well-defined descended forms, smooth in $t$; in particular $Tp(\omega_0,\omega_1)$ is a well-defined element of $\Omega^{2d-1}(M)$. All identities below are proved on $P$ and hold on $M$ because $\pi^*$ is injective and commutes with $\mathrm{d}$ (Lemma 5).
>
> **Step 1 — differentiate the Chern–Weil form.** Because $p$ is symmetric and $d$-linear, the product rule in $t$ gives
> $$\frac{\mathrm d}{\mathrm dt}\,p(F_t,\dots,F_t)=\sum_{j=1}^d p\Big(F_t,\dots,\underset{(j)}{\tfrac{\mathrm d}{\mathrm dt}F_t},\dots,F_t\Big)=d\,p\Big(\tfrac{\mathrm d}{\mathrm dt}F_t,\,F_t,\dots,F_t\Big)\qquad(\text{symmetry of }p:\text{ all }d\text{ terms are equal}).$$
> By **Lemma 2**, $\tfrac{\mathrm d}{\mathrm dt}F_t=\mathrm{d}^{\omega_t}b$, so
> $$\frac{\mathrm d}{\mathrm dt}\,p(F_t)=d\,p\big(\mathrm{d}^{\omega_t}b,\,F_t,\dots,F_t\big)\qquad(\text{Lemma 2}),$$
> writing $p(F_t):=p(F_t,\dots,F_t)$.
>
> **Step 2 — recognise the right-hand side as exact.** By **Lemma 4**, $p(\mathrm{d}^{\omega_t}b,F_t,\dots,F_t)=\mathrm{d}\,p(b,F_t,\dots,F_t)$. Multiplying by the integer $d$ and combining with Step 1,
> $$\frac{\mathrm d}{\mathrm dt}\,p(F_t)=d\,\mathrm{d}\,p(b,F_t,\dots,F_t)=\mathrm{d}\big(d\,p(b,F_t,\dots,F_t)\big)\qquad(\text{Lemma 4; }\ d\text{ is a constant, }\mathrm{d}\text{ is linear}).$$
>
> **Step 3 — integrate over the parameter.** Integrate both sides over $t\in[0,1]$. On the left, the fundamental theorem of calculus (**Lemma 5**) gives $\int_0^1\tfrac{\mathrm d}{\mathrm dt}p(F_t)\,\mathrm{d}t=p(F_1)-p(F_0)$. On the right, differentiation under the integral sign (**Lemma 5**) lets $\mathrm{d}$ pass out of the parameter integral:
> $$\int_0^1\mathrm{d}\big(d\,p(b,F_t,\dots,F_t)\big)\,\mathrm{d}t=\mathrm{d}\Big(d\int_0^1 p(b,F_t,\dots,F_t)\,\mathrm{d}t\Big)=\mathrm{d}\,Tp(\omega_0,\omega_1).$$
> Equating the two sides,
> $$p(F_1)-p(F_0)=\mathrm{d}\,Tp(\omega_0,\omega_1),\qquad Tp(\omega_0,\omega_1)=d\int_0^1 p(b,F_t,\dots,F_t)\,\mathrm{d}t\in\Omega^{2d-1}(M).$$
> This is the transgression formula. (The degree count: $p(b,F_t,\dots,F_t)$ has degree $1+2(d-1)=2d-1$, so $Tp$ is a $(2d-1)$-form, and $\mathrm{d}\,Tp$ a $2d$-form, matching $p(F_i)\in\Omega^{2d}(M)$.)
>
> **Step 4 — the corollary: the Chern–Simons $3$-form.** Take $G$ a matrix group, $p(\xi)=\operatorname{tr}(\xi^2)$, degree $d=2$, with polarisation $p(\xi,\eta)=\operatorname{tr}(\xi\eta)$ (indeed $p(\xi+\eta,\xi+\eta)=\operatorname{tr}((\xi+\eta)^2)=\operatorname{tr}(\xi^2)+2\operatorname{tr}(\xi\eta)+\operatorname{tr}(\eta^2)$ by cyclicity $\operatorname{tr}(\xi\eta)=\operatorname{tr}(\eta\xi)$, so the symmetric bilinear part is $\operatorname{tr}(\xi\eta)$), and $\operatorname{Ad}$-invariant since $\operatorname{tr}((g\xi g^{-1})^2)=\operatorname{tr}(g\xi^2g^{-1})=\operatorname{tr}(\xi^2)$. On the trivial bundle $M\times G$ take $\omega_0$ the product connection (local form $A_0=0$) and $\omega_1$ with local form $A\in\Omega^1(M;\mathfrak{g})$. Then $b$ descends to $A$, and on the trivialisation $\omega_t$ has local form $tA$, so by the structure equation (matrix form $F=\mathrm{d}A+A\wedge A$)
> $$F_t=\mathrm{d}(tA)+(tA)\wedge(tA)=t\,\mathrm{d}A+t^2\,A\wedge A,\qquad F_0=0,\qquad F_1=F_A=\mathrm{d}A+A\wedge A.$$
> The transgression form is
> $$Tp=2\int_0^1 p(A,F_t)\,\mathrm{d}t=2\int_0^1\operatorname{tr}\big(A\wedge(t\,\mathrm{d}A+t^2A\wedge A)\big)\,\mathrm{d}t\qquad(d=2;\ p(A,F_t)=\operatorname{tr}(A\wedge F_t)).$$
> Pulling the $t$-independent forms out of the integral,
> $$Tp=2\Big(\operatorname{tr}(A\wedge\mathrm{d}A)\!\int_0^1\! t\,\mathrm{d}t+\operatorname{tr}(A\wedge A\wedge A)\!\int_0^1\! t^2\,\mathrm{d}t\Big)=2\Big(\tfrac12\operatorname{tr}(A\wedge\mathrm{d}A)+\tfrac13\operatorname{tr}(A^{\wedge3})\Big)=\operatorname{tr}\!\Big(A\wedge\mathrm{d}A+\tfrac23A^{\wedge3}\Big)=\operatorname{cs}(A).$$
> Since $p(F_0)=\operatorname{tr}(0)=0$ and $p(F_1)=\operatorname{tr}(F_A\wedge F_A)$, the transgression formula gives
> $$\operatorname{tr}(F_A\wedge F_A)=p(F_1)-p(F_0)=\mathrm{d}\,Tp=\mathrm{d}\operatorname{cs}(A)=\mathrm{d}\operatorname{tr}\!\Big(A\wedge\mathrm{d}A+\tfrac23A\wedge A\wedge A\Big),$$
> which is Haydys's identity (97). Thus $\operatorname{cs}(A)=\operatorname{tr}(A\wedge\mathrm{d}A+\tfrac23A^{\wedge3})$ transgresses the second Chern–Weil form. $\ \blacksquare$

> [!note]- Independent verification of the corollary by direct expansion
> We verify $\mathrm{d}\operatorname{cs}(A)=\operatorname{tr}(F_A\wedge F_A)$ without the transgression machinery, giving a second, self-contained proof of (97). Throughout, $\operatorname{tr}$ commutes with $\mathrm{d}$, the exterior derivative obeys the graded Leibniz rule, and the trace of matrix-valued forms is graded-cyclic: $\operatorname{tr}(\alpha\wedge\beta)=(-1)^{|\alpha||\beta|}\operatorname{tr}(\beta\wedge\alpha)$ (from $\operatorname{tr}(MN)=\operatorname{tr}(NM)$ on entries and the [[Thm - Wedge Product Properties|graded commutativity of the wedge]]).
>
> **The quadratic term.** With $A$ a $1$-form and $\mathrm{d}(\mathrm{d}A)=0$,
> $$\mathrm{d}\operatorname{tr}(A\wedge\mathrm{d}A)=\operatorname{tr}\big(\mathrm{d}A\wedge\mathrm{d}A-A\wedge\mathrm{d}(\mathrm{d}A)\big)=\operatorname{tr}(\mathrm{d}A\wedge\mathrm{d}A)\qquad(\text{graded Leibniz; }\mathrm{d}^2=0).$$
>
> **The cubic term.** By graded Leibniz, $\mathrm{d}(A\wedge A\wedge A)=\mathrm{d}A\wedge A\wedge A-A\wedge\mathrm{d}A\wedge A+A\wedge A\wedge\mathrm{d}A$. Take the trace of each summand and reduce to $T:=\operatorname{tr}(\mathrm{d}A\wedge A\wedge A)$ using cyclicity: for the third, $\operatorname{tr}(A\wedge A\wedge\mathrm{d}A)=(-1)^{2\cdot2}\operatorname{tr}(\mathrm{d}A\wedge A\wedge A)=T$ (moving the $2$-form $\mathrm{d}A$ past the $2$-form $A\wedge A$); for the second, $\operatorname{tr}(A\wedge\mathrm{d}A\wedge A)=(-1)^{1\cdot3}\operatorname{tr}(\mathrm{d}A\wedge A\wedge A)=-T$ (moving the leading $1$-form $A$ past the $3$-form $\mathrm{d}A\wedge A$). Hence
> $$\mathrm{d}\operatorname{tr}(A^{\wedge3})=T-(-T)+T=3T=3\operatorname{tr}(\mathrm{d}A\wedge A\wedge A),\qquad\text{so}\qquad \tfrac23\mathrm{d}\operatorname{tr}(A^{\wedge3})=2\operatorname{tr}(\mathrm{d}A\wedge A\wedge A).$$
>
> **The right-hand side.** Expand $F_A\wedge F_A=(\mathrm{d}A+A\wedge A)\wedge(\mathrm{d}A+A\wedge A)$ and take the trace:
> $$\operatorname{tr}(F_A\wedge F_A)=\operatorname{tr}(\mathrm{d}A\wedge\mathrm{d}A)+\operatorname{tr}(\mathrm{d}A\wedge A\wedge A)+\operatorname{tr}(A\wedge A\wedge\mathrm{d}A)+\operatorname{tr}(A^{\wedge4}).$$
> Here $\operatorname{tr}(A\wedge A\wedge\mathrm{d}A)=T$ (shown above) and $\operatorname{tr}(A^{\wedge4})=(-1)^{1\cdot3}\operatorname{tr}(A^{\wedge4})=-\operatorname{tr}(A^{\wedge4})$ (moving the leading $1$-form $A$ past the $3$-form $A^{\wedge3}$), whence $\operatorname{tr}(A^{\wedge4})=0$. Therefore $\operatorname{tr}(F_A\wedge F_A)=\operatorname{tr}(\mathrm{d}A\wedge\mathrm{d}A)+2T$.
>
> **Assemble.** Adding the two term computations,
> $$\mathrm{d}\operatorname{cs}(A)=\mathrm{d}\operatorname{tr}(A\wedge\mathrm{d}A)+\tfrac23\mathrm{d}\operatorname{tr}(A^{\wedge3})=\operatorname{tr}(\mathrm{d}A\wedge\mathrm{d}A)+2T=\operatorname{tr}(F_A\wedge F_A).$$
> The two independent routes agree. $\ \blacksquare$

---

# Cross-Field Exercise Suggestions

**Rescaling and the Chern–Simons coefficients (representation of Lie groups).** On a trivial bundle, run the transgression with the rescaling path $\omega_t=t\omega_1$ (rather than the general affine path) and any homogeneous $p$ of degree $d$: because $F_t=t\,\mathrm{d}A+t^2A\wedge A$, the integrand $p(A,F_t,\dots,F_t)$ is a polynomial in $t$ whose coefficients are the beta-function moments $\int_0^1 t^k(1-t)^{\ell}\,\mathrm{d}t$. The theorem applies because the product connection is a genuine second connection with vanishing curvature; the non-obvious point is that the transgression form of a *degree-$d$* polynomial is a universal linear combination of the $2d-1$ Chern–Simons-type words in $A$ and $\mathrm{d}A$, with rational coefficients fixed once and for all by these moments — for $d=3$ this reproduces the five-form $\operatorname{tr}(A(\mathrm{d}A)^2+\tfrac32A^3\mathrm{d}A+\tfrac35A^5)$.

**Secondary characteristic classes of flat connections (de Rham cohomology).** If both $\omega_0$ and $\omega_1$ are flat ($F_0=F_1=0$) then $p(F_1)-p(F_0)=0$, so $\mathrm{d}\,Tp=0$ and $Tp$ is a closed $(2d-1)$-form whose de Rham class is a *secondary* invariant of the pair of flat connections — a Chern–Simons invariant. The theorem applies because flatness of the endpoints is no obstruction to running the path through non-flat $\omega_t$ in between; the non-obvious content is that the class $[Tp]\in H^{2d-1}_{\mathrm{dR}}(M)$ can be non-zero even though both curvature-polynomials vanish, detecting how the flat connections are linked through the space of connections. This is the mechanism behind the Chern–Simons invariants of flat connections on three-manifolds.

**The Wess–Zumino term and the degree of a map (algebraic topology).** For $A=g^{-1}\mathrm{d}g$ a pure-gauge connection with $g\colon M\to G$ and $M$ a closed $(2d-1)$-manifold, the curvature $F_A=\mathrm{d}A+A\wedge A$ vanishes (the Maurer–Cartan equation), so $\operatorname{cs}(A)$ reduces to $-\tfrac13\operatorname{tr}((g^{-1}\mathrm{d}g)^{\wedge3})$ for $d=2$, the pull-back by $g$ of the bi-invariant $3$-form of $G$. The transgression theorem is what identifies this word as a transgression, hence closed with quantised periods; the non-obvious payoff is that $\int_M\operatorname{cs}(g^{-1}\mathrm{d}g)$ computes the degree of $g$ when $\dim M=\dim G$, the topological quantisation underlying the Wess–Zumino term and the [[Thm - Gauge Variation of the Chern-Simons Functional|gauge variation]] of the Chern–Simons functional.

---

# Bridges

- **The Chern–Weil theorem, made explicit.** The [[Thm - Chern-Weil Theorem|Chern–Weil theorem]] asserts that $p(F_{\omega_1})-p(F_{\omega_0})$ is exact; this page names the primitive. The bridge is the cylinder-versus-path duality: Chern–Weil proves exactness by pulling back to $M\times[0,1]$ and quoting homotopy invariance, whereas here we integrate the interpolation parameter out directly, and the two produce the same de Rham class. Where the Chern–Weil page needs only "some primitive exists," every place downstream that needs the actual boundary term (the Chern–Simons functional, the four-dimensional formula) needs $Tp$.

- **The Chern–Simons functional.** On a closed oriented three-manifold $M$ with $G=SU(2)$ and a trivialisation, the [[Def - Chern-Simons Functional|Chern–Simons functional]] is $\vartheta(A)=\tfrac1{8\pi^2}\int_M\operatorname{cs}(A)$, the integral of exactly the $3$-form transgressed here. The bridge is that $\operatorname{cs}(A)$ is well-defined as a $3$-form on the trivialised bundle even though $\operatorname{tr}(F\wedge F)$ vanishes identically in dimension three; the functional is the "leftover" boundary data of the four-dimensional Chern–Weil integral. Its behaviour under a change of trivialisation, and hence its true home in $\mathbb{R}/\mathbb{Z}$, is the content of the [[Thm - Gauge Variation of the Chern-Simons Functional|gauge-variation theorem]].

- **Integrality of the second Chern number.** On a closed oriented four-manifold, gluing two local Chern–Simons primitives of $\operatorname{tr}(F\wedge F)$ across a separating three-sphere, via Stokes, expresses $\tfrac1{8\pi^2}\int_X\operatorname{tr}(F_A\wedge F_A)$ as the winding number of the clutching map — an integer. The bridge is that the local exactness $\operatorname{tr}(F\wedge F)=\mathrm{d}\operatorname{cs}(A)$ proved here is precisely what lets Stokes convert a bulk integral into a boundary integral of $\operatorname{cs}$; the [[Thm - Second Chern Number of an SU(2)-Bundle over a Closed Four-Manifold is the Clutching Degree|clutching theorem]] carries this out.

- **The Yang–Mills energy identity (chapter VII).** The topological term $\int_X\operatorname{tr}(F\wedge F)$, connection-independent by transgression plus Stokes, is what separates from the Yang–Mills energy $\tfrac12\int|F|^2$ to give the instanton bound. The bridge is the identity $|F|^2\,\mathrm{vol}=(\text{const})\,(\operatorname{tr}(F\wedge F)\text{-part})+|F^{\mp}|^2\,\mathrm{vol}$ built from the Hodge star; transgression guarantees the first summand integrates to a topological constant, so minimising energy in a fixed topological sector means killing $F^{\mp}$, i.e. solving the (anti-)self-duality equation.

---

# Unlocked by This

> [!tip] Secondary (Chern–Simons) characteristic classes *(from Differential Topology)*
> When the primary characteristic form vanishes — for flat connections, or for two connections with equal curvature-polynomials — the transgression form becomes closed and its de Rham class is a *secondary* invariant living one degree below the primary class. These Chern–Simons classes refine characteristic classes and detect data invisible to them, such as the framing of a three-manifold or the linking of flat connections. See **Chern–Simons theory as a topological quantum field theory**.

> [!tip] The Wess–Zumino–Witten term *(from Mathematical Physics)*
> The pure-gauge value $-\tfrac13\operatorname{tr}((g^{-1}\mathrm{d}g)^{\wedge3})$ of the Chern–Simons form is the integrand of the Wess–Zumino term of a sigma model into a Lie group; the transgression identity is what makes its variation a total derivative, so that the term is well-defined modulo the quantised periods of the bi-invariant $3$-form. This is the origin of the quantisation of the Wess–Zumino–Witten level.
