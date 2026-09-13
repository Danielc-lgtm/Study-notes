---
type: theorem
subject: gauge-theory
prereqs:
  - "Thm - Transgression Formula and the Chern-Simons Form"
  - "Thm - Gauge Action on Connection Matrices"
  - "Thm - The Brouwer Degree is an Integer and a Homotopy Invariant"
  - "Thm - Classification of Principal SU(2)-Bundles over Four-Manifolds"
  - "Thm - Stokes' Theorem on Manifolds"
tags: [geometry, gauge-theory]
---

# Notation

$M$ is a closed (compact, boundaryless) oriented $3$-manifold. We identify $SU(2)$ with $S^3$, oriented as $\partial B^4$ with $\mathbb R^4=(1,i,j,k)$, exactly as fixed on [[Def - The Hopf Bundle#Sign ledger]]. A connection on the (trivial, by [[Thm - Classification of Principal SU(2)-Bundles over Four-Manifolds|part (A)]]) $SU(2)$-bundle over $M$ is written in the trivialisation as $A\in\Omega^1(M;\mathfrak{su}(2))$, with $\mathfrak{su}(2)$ the traceless skew-Hermitian $2\times2$ matrices and $\operatorname{tr}$ the trace in the defining representation. A **gauge transformation** is a smooth map $g\colon M\to SU(2)$; it acts on connections by
$$A^g:=A\cdot g=g^{-1}Ag+g^{-1}dg\qquad(\text{[[Thm - Gauge Action on Connection Matrices|gauge action on connection matrices]]}).$$
We abbreviate $\theta:=g^{-1}dg$ and $\bar\theta:=dg\,g^{-1}=g\theta g^{-1}$ for the left and right Maurer–Cartan forms pulled back by $g$; both are $\mathfrak{su}(2)$-valued one-forms. The **Chern–Simons three-form** of $A$ is
$$\operatorname{cs}(A):=\operatorname{tr}\Big(A\wedge dA+\tfrac23A\wedge A\wedge A\Big)\in\Omega^3(M),$$
and the **Chern–Simons functional** is $\vartheta(A):=\tfrac1{8\pi^2}\int_M\operatorname{cs}(A)$, taken modulo $\mathbb Z$ (see [[Def - Chern-Simons Functional]]). Throughout, juxtaposition of forms denotes the wedge product. We use two facts recorded elsewhere: the sign-ledger value $\int_{SU(2)}\operatorname{tr}(\theta^{\wedge3})=-24\pi^2$, and $\deg g$ the [[Thm - The Brouwer Degree is an Integer and a Homotopy Invariant|Brouwer degree]] of $g\colon M\to SU(2)\cong S^3$.

We will repeatedly use the **Maurer–Cartan structure equations** and the cyclicity of the trace on forms. From $g^{-1}g=1$ we get $d(g^{-1})=-g^{-1}dg\,g^{-1}=-\theta g^{-1}$ and $dg=g\theta$, whence
$$d\theta=d(g^{-1}dg)=d(g^{-1})\wedge dg=-\theta g^{-1}\wedge g\theta=-\theta\wedge\theta,\qquad d\bar\theta=d(dg\,g^{-1})=-dg\wedge d(g^{-1})=\bar\theta\wedge\bar\theta.$$
For $\mathfrak{su}(2)$-valued one-forms $\alpha,\beta,\gamma$, the trace of a product of three of them is cyclic, $\operatorname{tr}(\alpha\beta\gamma)=\operatorname{tr}(\beta\gamma\alpha)$ (moving a degree-$1$ factor past a degree-$2$ product costs $(-1)^{1\cdot2}=+1$).

---

# Statement

> **Theorem (gauge variation of the Chern–Simons form and functional).** Let $M$ be a closed oriented $3$-manifold, $A\in\Omega^1(M;\mathfrak{su}(2))$, and $g\colon M\to SU(2)$ smooth, with $A^g=g^{-1}Ag+g^{-1}dg$ and $\theta=g^{-1}dg$. Then:
>
> **(1) The pointwise identity.**
> $$\operatorname{cs}(A^g)=\operatorname{cs}(A)-\tfrac13\operatorname{tr}\big(\theta\wedge\theta\wedge\theta\big)-d\operatorname{tr}\big(dg\,g^{-1}\wedge A\big).$$
>
> **(2) The integral identity.**
> $$\frac1{8\pi^2}\int_M\operatorname{cs}(A^g)=\frac1{8\pi^2}\int_M\operatorname{cs}(A)-\frac1{24\pi^2}\int_M\operatorname{tr}(\theta^{\wedge3})=\frac1{8\pi^2}\int_M\operatorname{cs}(A)+\deg g.$$
>
> **(3) The gauge law and well-definedness.** Consequently $\vartheta(A\cdot g)=\vartheta(A)+\deg g$ in $\mathbb R$, so $\vartheta$ changes by the integer $\deg g$ under a gauge transformation, and the Chern–Simons functional $\vartheta\colon\mathcal A(P)\to\mathbb R/\mathbb Z$ is well defined — independent of the trivialisation and invariant under the gauge group — as a map to $\mathbb R/\mathbb Z$.

> [!warning] Convention: the sign of $\deg g$
> The value of $\int_{SU(2)}\operatorname{tr}(\theta^{\wedge3})$ is orientation-dependent. Under the series conventions (fixed on [[Def - The Hopf Bundle#Sign ledger]]) it equals $-24\pi^2$, so $\frac1{24\pi^2}\int_M\operatorname{tr}(\theta^{\wedge3})=-\deg g$ and the functional *increases* by $\deg g$: $\vartheta(A\cdot g)=\vartheta(A)+\deg g$. This is the sign recorded by Haydys (Exercise 96(d)). With the opposite orientation of $S^3$ every sign in this callout flips, and the gauge law reads $\vartheta(A\cdot g)=\vartheta(A)-\deg g$; only the class in $\mathbb R/\mathbb Z$ is convention-free.

---

# Motivation

The Chern–Simons functional is the three-dimensional counterpart of the second Chern number: where $\frac1{8\pi^2}\int_X\operatorname{tr}(F\wedge F)$ measures the topology of a bundle over a four-manifold, $\vartheta(A)=\frac1{8\pi^2}\int_M\operatorname{cs}(A)$ measures the "secondary" geometry of a connection over a three-manifold. But there is a catch, and this theorem is its resolution. On a four-manifold $\operatorname{tr}(F\wedge F)$ is gauge invariant, being built from the curvature; on a three-manifold $\operatorname{cs}(A)$ is built from the connection *matrix* $A$, which is not gauge invariant, and neither is $\operatorname{cs}(A)$. So $\vartheta$ appears to depend on the arbitrary choice of trivialisation.

The theorem says the dependence is by an integer only. The Chern–Simons form is not gauge invariant, but its gauge variation is the sum of an exact term — which integrates to zero over the closed three-manifold — and the pull-back of the bi-invariant three-form $\operatorname{tr}(\theta^{\wedge3})$ of $SU(2)$, whose integral counts the degree of the gauge transformation. Since the degree is an integer, $\vartheta$ is well defined in $\mathbb R/\mathbb Z$. This is exactly what is needed for $\vartheta$ to descend to the space of connections modulo gauge, and hence to serve as a functional whose critical points are the flat connections and whose gradient flow is the instanton equation. Every use of Chern–Simons theory — from the Chern–Simons quantum field theory to instanton Floer homology to the Casson invariant — begins with the fact proved here: the ambiguity is integral.

> **The Chern–Simons form is not gauge invariant; its variation is an exact term plus the pull-back of the bi-invariant three-form of $SU(2)$, whose integral over the closed three-manifold counts the degree of the gauge transformation.**

---

# Sources and Targets

**Sources (Input Broadening).** The hypothesis is a connection on a closed oriented three-manifold together with a gauge transformation; the disguised inputs are the situations that produce such data.

The first disguised source is **a change of trivialisation of an $SU(2)$-bundle over $M^3$.** Since every such bundle is trivial ([[Thm - Classification of Principal SU(2)-Bundles over Four-Manifolds|part (A)]]), two trivialisations differ by a gauge transformation $g\colon M\to SU(2)$, and the connection's coordinate expressions differ by $A\mapsto A^g$. The theorem then measures how the coordinate-dependent $\vartheta$ changes: by $\deg g$. The bridge is the sections–trivialisations correspondence. *Example problem:* show two trivialisations of the trivial $SU(2)$-bundle over $S^3$ that differ by $g=\mathrm{id}$ change $\vartheta$ by $1$.

The second disguised source is **a based loop of connections, or a connection on $M\times[0,1]$ with gauge-related ends.** A path $A_t$ from $A_0$ to $A_0^g$ closes up modulo gauge; its "action" is the four-dimensional integral $\frac1{8\pi^2}\int_{M\times[0,1]}\operatorname{tr}(F\wedge F)$, which by Stokes equals $\vartheta(A_0^g)-\vartheta(A_0)=\deg g$. The non-obvious step is that a gauge transformation with nonzero degree obstructs closing the path at the level of $\vartheta$, not just modulo $\mathbb Z$. *Example problem:* compute the spectral flow around such a loop.

The third disguised source is **a representation $\pi_1(M)\to SU(2)$ deformed by conjugation.** Flat connections correspond to such representations; conjugating a representation is a gauge transformation, and the theorem shows the Chern–Simons invariant of a flat connection is a well-defined element of $\mathbb R/\mathbb Z$ attached to the conjugacy class. The bridge is the flat-connection–monodromy correspondence. *Example problem:* the Chern–Simons invariant of a flat connection on a Seifert-fibred space.

**Targets (Output Amplification).** The conclusion "the ambiguity is $\deg g\in\mathbb Z$" combines with other results.

Combine it with **the four-dimensional formula.** For a compact oriented four-manifold $X$ with $\partial X=M$ and a connection extending $A$, Stokes and the local exactness of $\operatorname{tr}(F\wedge F)$ give $\vartheta(A)\equiv\frac1{8\pi^2}\int_X\operatorname{tr}(F\wedge F)\pmod{\mathbb Z}$; the well-definedness modulo $\mathbb Z$ that this theorem provides is what makes that formula consistent across different fillings $X$. The extra ingredient is a bounding four-manifold; the payoff is the boundary interpretation of Chern–Simons.

Combine it with **the first variation of $\vartheta$.** Because $\vartheta$ is gauge invariant modulo $\mathbb Z$, its differential $d\vartheta_A(a)=\frac1{4\pi^2}\int_M\operatorname{tr}(F_A\wedge a)$ is gauge invariant, so it descends to the quotient $\mathcal A/\mathcal G$ and its zeros — the flat connections — form a gauge-invariant critical set. The extra ingredient is the variational computation; the payoff is that flat connections are the critical points of a function on $\mathcal A/\mathcal G$.

Combine it with **the degree homomorphism.** Since $g\mapsto\deg g$ is a homomorphism from the gauge group $\operatorname{Map}(M,SU(2))$ to $\mathbb Z$ (additivity of degree under pointwise products), the map $\vartheta\colon\mathcal A\to\mathbb R$ descends to a principal $\mathbb R/\mathbb Z$-bundle picture over $\mathcal A/\mathcal G$. The extra ingredient is the additivity lemma; the payoff is the geometric quantisation of Chern–Simons theory.

---

# Why Is It True

The connection matrix $A$ transforms inhomogeneously under a gauge transformation, $A^g=g^{-1}Ag+g^{-1}dg$: besides the conjugation $g^{-1}Ag$ there is the inhomogeneous term $\theta=g^{-1}dg$, the pull-back of the Maurer–Cartan form. The Chern–Simons form is cubic in the connection, so substituting $A^g=g^{-1}Ag+\theta$ produces, besides the conjugation-invariant piece $\operatorname{cs}(g^{-1}Ag)$, a collection of mixed terms and a pure $\theta$-cubic term $-\frac13\operatorname{tr}(\theta^{\wedge3})$. The conjugation piece is not itself $\operatorname{cs}(A)$ — because $g^{-1}Ag$ has the "wrong" differential — but the discrepancy is exactly cancelled by some of the mixed terms, and the remaining mixed terms assemble into an exact form $-d\operatorname{tr}(\bar\theta\wedge A)$. What is left over is the pure Maurer–Cartan cubic.

Now the pure cubic is universal: $\operatorname{tr}(\theta^{\wedge3})$ is the pull-back by $g$ of the bi-invariant three-form on $SU(2)$, and a bi-invariant top-form on the group $S^3$ is a multiple of the volume form. Its integral over $M$ therefore counts how many times $g$ covers $SU(2)$ — the degree — times the total mass $\int_{SU(2)}\operatorname{tr}(\theta^{\wedge3})=-24\pi^2$. Dividing by $24\pi^2$ turns this into $-\deg g$, and the sign in the Chern–Simons variation turns it into $+\deg g$. The exact term is invisible after integrating over the closed manifold. So the whole non-invariance of $\vartheta$ is the single integer $\deg g$.

---

# What Makes This Hard

The difficulty is entirely bookkeeping, and there are two places to slip. First, the mixed terms: after substituting $A^g=g^{-1}Ag+\theta$ one gets terms like $\operatorname{tr}(B^2\theta)$ and $\operatorname{tr}(\theta\,dB)$ with $B=g^{-1}Ag$, and one must show the non-exact ones cancel while the rest form $-d\operatorname{tr}(\bar\theta\wedge A)$; a single sign error in $dB=g^{-1}(dA)g-\theta B-B\theta$ or in the cyclicity of the trace derails the cancellation. Second, the coefficient $-\frac13$ of the cubic and the total constant $-24\pi^2$ must both be right, and the second is orientation-dependent; the frequent error of writing $+24\pi^2$ (opposite $S^3$-orientation) flips the sign of the gauge law. The remedy is to carry every term explicitly, as below, and to import the orientation constant from the one place it is computed, the sign ledger.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Substitute $A^g=B+\theta$ with $B=g^{-1}Ag$ into $\operatorname{cs}$, expand using $d\theta=-\theta^2$ and $dB=g^{-1}(dA)g-\theta B-B\theta$, collect terms with cyclicity of the trace, show the conjugation piece differs from $\operatorname{cs}(A)$ by $-2\operatorname{tr}(B^2\theta)$ that cancels, and recognise the leftover as $-\frac13\operatorname{tr}(\theta^{\wedge3})-d\operatorname{tr}(\bar\theta\wedge A)$. Then integrate, kill the exact term by Stokes, and evaluate the cubic by the sign ledger.

**Subgoal decomposition:**

1. **Expand $\operatorname{cs}(A^g)$ in $B$ and $\theta$.** Get $\operatorname{cs}(B)+\operatorname{tr}(\theta\,dB)+\operatorname{tr}(B\theta^2)+2\operatorname{tr}(B^2\theta)-\frac13\operatorname{tr}(\theta^{\wedge3})$.
   - *Hint:* $dA^g=dB-\theta^2$; expand $\operatorname{tr}(A^g dA^g)$ and $\frac23\operatorname{tr}((A^g)^3)$ and combine coefficients.
   - *Why needed:* It isolates the cubic and the mixed terms.

2. **Reduce the conjugation piece.** Show $\operatorname{cs}(B)=\operatorname{cs}(A)-2\operatorname{tr}(B^2\theta)$.
   - *Hint:* $\operatorname{tr}(B^3)=\operatorname{tr}(A^3)$, and $\operatorname{tr}(B\,dB)=\operatorname{tr}(A\,dA)-2\operatorname{tr}(B^2\theta)$ using $dB$.
   - *Why needed:* Its $B^2\theta$ term cancels the one from Step 1.

3. **Assemble the exact term.** Show $\operatorname{tr}(\theta\,dB)+\operatorname{tr}(B\theta^2)=-d\operatorname{tr}(\bar\theta\wedge A)$.
   - *Hint:* Rewrite in $\bar\theta=g\theta g^{-1}$ and use $d\bar\theta=\bar\theta^2$.
   - *Why needed:* It identifies the remaining mixed terms as exact.

4. **Integrate.** Stokes kills the exact term; the cubic integrates to $-24\pi^2\deg g$.
   - *Hint:* $\operatorname{tr}(\theta^{\wedge3})$ is bi-invariant; the sign ledger gives its total integral.
   - *Why needed:* It yields the gauge law and well-definedness.

---

# Lemma Decomposition

> [!note]- Lemma 1: the pointwise gauge-variation identity
> **Statement:** With $A^g=g^{-1}Ag+g^{-1}dg$, $B=g^{-1}Ag$, $\theta=g^{-1}dg$, $\bar\theta=dg\,g^{-1}$,
> $$\operatorname{cs}(A^g)=\operatorname{cs}(A)-\tfrac13\operatorname{tr}(\theta^{\wedge3})-d\operatorname{tr}(\bar\theta\wedge A).$$
>
> **Hint:** Expand with $dA^g=dB-\theta^2$ and $dB=g^{-1}(dA)g-\theta B-B\theta$; collect via cyclicity.
>
> **Why needed:** It is the entire pointwise content; parts (2) and (3) are integration and interpretation.
>
> > [!note]- Full proof
> > We use $dA^g=d(B+\theta)=dB+d\theta=dB-\theta\wedge\theta$ (since $d\theta=-\theta^{\wedge2}$) and $dB=g^{-1}(dA)g-\theta B-B\theta$ (Leibniz rule, with $d(g^{-1})=-\theta g^{-1}$, $dg=g\theta$). All traces below are of products of one-forms and hence cyclic.
> >
> > **Step 1 — expand the quadratic part.**
> > $$\operatorname{tr}\big(A^g\,dA^g\big)=\operatorname{tr}\big((B+\theta)(dB-\theta^2)\big)=\operatorname{tr}(B\,dB)-\operatorname{tr}(B\theta^2)+\operatorname{tr}(\theta\,dB)-\operatorname{tr}(\theta^3)\qquad(\text{multiply out; }\theta\theta^2=\theta^3).$$
> >
> > **Step 2 — expand the cubic part.** Expanding $(B+\theta)^{\wedge3}$ and using cyclicity ($\operatorname{tr}(B^2\theta)=\operatorname{tr}(B\theta B)=\operatorname{tr}(\theta B^2)$, and likewise for $B\theta^2$),
> > $$\operatorname{tr}\big((A^g)^{\wedge3}\big)=\operatorname{tr}(B^3)+3\operatorname{tr}(B^2\theta)+3\operatorname{tr}(B\theta^2)+\operatorname{tr}(\theta^3),$$
> > so $\tfrac23\operatorname{tr}((A^g)^{\wedge3})=\tfrac23\operatorname{tr}(B^3)+2\operatorname{tr}(B^2\theta)+2\operatorname{tr}(B\theta^2)+\tfrac23\operatorname{tr}(\theta^3)$.
> >
> > **Step 3 — combine.** Adding Steps 1 and 2 and collecting the coefficient of each monomial ($\theta^3$: $-1+\tfrac23=-\tfrac13$; $B\theta^2$: $-1+2=+1$),
> > $$\operatorname{cs}(A^g)=\underbrace{\operatorname{tr}(B\,dB)+\tfrac23\operatorname{tr}(B^3)}_{=\operatorname{cs}(B)}+\operatorname{tr}(\theta\,dB)+\operatorname{tr}(B\theta^2)+2\operatorname{tr}(B^2\theta)-\tfrac13\operatorname{tr}(\theta^3).$$
> >
> > **Step 4 — reduce the conjugation piece $\operatorname{cs}(B)$.** Since $B=g^{-1}Ag$, conjugation invariance of the trace gives $\operatorname{tr}(B^3)=\operatorname{tr}(g^{-1}A^3g)=\operatorname{tr}(A^3)$. For the quadratic part, substitute $dB=g^{-1}(dA)g-\theta B-B\theta$:
> > $$\operatorname{tr}(B\,dB)=\operatorname{tr}\big(Bg^{-1}(dA)g\big)-\operatorname{tr}(B\theta B)-\operatorname{tr}(B^2\theta)=\operatorname{tr}(A\,dA)-2\operatorname{tr}(B^2\theta),$$
> > using $\operatorname{tr}(Bg^{-1}(dA)g)=\operatorname{tr}(g^{-1}A\,dA\,g)=\operatorname{tr}(A\,dA)$ and $\operatorname{tr}(B\theta B)=\operatorname{tr}(B^2\theta)$ (cyclicity). Hence
> > $$\operatorname{cs}(B)=\operatorname{tr}(B\,dB)+\tfrac23\operatorname{tr}(B^3)=\operatorname{tr}(A\,dA)+\tfrac23\operatorname{tr}(A^3)-2\operatorname{tr}(B^2\theta)=\operatorname{cs}(A)-2\operatorname{tr}(B^2\theta).$$
> >
> > **Step 5 — cancel the $B^2\theta$ terms.** Substituting Step 4 into Step 3, the $-2\operatorname{tr}(B^2\theta)$ from $\operatorname{cs}(B)$ cancels the $+2\operatorname{tr}(B^2\theta)$:
> > $$\operatorname{cs}(A^g)=\operatorname{cs}(A)+\operatorname{tr}(\theta\,dB)+\operatorname{tr}(B\theta^2)-\tfrac13\operatorname{tr}(\theta^3).$$
> >
> > **Step 6 — assemble the exact term.** Substitute $dB=g^{-1}(dA)g-\theta B-B\theta$ once more:
> > $$\operatorname{tr}(\theta\,dB)=\operatorname{tr}\big(\theta g^{-1}(dA)g\big)-\operatorname{tr}(\theta^2 B)-\operatorname{tr}(\theta B\theta)=\operatorname{tr}(\bar\theta\,dA)-2\operatorname{tr}(B\theta^2),$$
> > where $\operatorname{tr}(\theta g^{-1}(dA)g)=\operatorname{tr}(g\theta g^{-1}dA)=\operatorname{tr}(\bar\theta\,dA)$ and $\operatorname{tr}(\theta B\theta)=\operatorname{tr}(\theta^2 B)=\operatorname{tr}(B\theta^2)$ (cyclicity). Therefore
> > $$\operatorname{tr}(\theta\,dB)+\operatorname{tr}(B\theta^2)=\operatorname{tr}(\bar\theta\,dA)-\operatorname{tr}(B\theta^2)=\operatorname{tr}(\bar\theta\,dA)-\operatorname{tr}(A\bar\theta^2),$$
> > the last equality because $\operatorname{tr}(B\theta^2)=\operatorname{tr}(g^{-1}Ag\,\theta^2)=\operatorname{tr}(A\,g\theta^2g^{-1})=\operatorname{tr}(A\bar\theta^2)$. Now compute the exterior derivative of $\operatorname{tr}(\bar\theta\wedge A)$ using $d\bar\theta=\bar\theta^{\wedge2}$ and that $\bar\theta$ has degree $1$:
> > $$d\operatorname{tr}(\bar\theta\wedge A)=\operatorname{tr}(d\bar\theta\wedge A)-\operatorname{tr}(\bar\theta\wedge dA)=\operatorname{tr}(\bar\theta^2 A)-\operatorname{tr}(\bar\theta\,dA)=\operatorname{tr}(A\bar\theta^2)-\operatorname{tr}(\bar\theta\,dA),$$
> > using cyclicity $\operatorname{tr}(\bar\theta^2 A)=\operatorname{tr}(A\bar\theta^2)$. Comparing, $\operatorname{tr}(\bar\theta\,dA)-\operatorname{tr}(A\bar\theta^2)=-d\operatorname{tr}(\bar\theta\wedge A)$.
> >
> > **Step 7 — conclude.** Substituting Step 6 into Step 5,
> > $$\operatorname{cs}(A^g)=\operatorname{cs}(A)-\tfrac13\operatorname{tr}(\theta^{\wedge3})-d\operatorname{tr}(\bar\theta\wedge A)=\operatorname{cs}(A)-\tfrac13\operatorname{tr}\big((g^{-1}dg)^{\wedge3}\big)-d\operatorname{tr}\big(dg\,g^{-1}\wedge A\big). \qquad\blacksquare$$
> >
> > *(Consistency check.* Applying $d$ to both sides, the left is $\operatorname{tr}(F_{A^g}\wedge F_{A^g})=\operatorname{tr}(F_A\wedge F_A)$ (gauge invariance of the curvature integrand), the right is $\operatorname{tr}(F_A\wedge F_A)-\tfrac13d\operatorname{tr}(\theta^{\wedge3})$, and $d\operatorname{tr}(\theta^{\wedge3})=3\operatorname{tr}(d\theta\,\theta^2)=-3\operatorname{tr}(\theta^{\wedge4})=0$ since $d\theta=-\theta^2$ and the trace of four one-forms vanishes by cyclicity; the two sides agree.)*

> [!note]- Lemma 2: the Maurer–Cartan cubic integrates to $-24\pi^2\deg g$
> **Statement:** For smooth $g\colon M\to SU(2)$ on a closed oriented $3$-manifold, $\displaystyle\int_M\operatorname{tr}\big((g^{-1}dg)^{\wedge3}\big)=-24\pi^2\deg g$.
>
> **Hint:** $\operatorname{tr}(\theta^{\wedge3})$ is bi-invariant on $SU(2)=S^3$ with total integral $-24\pi^2$ (sign ledger); apply the degree theorem.
>
> **Why needed:** It converts the cubic term into $\deg g$, giving parts (2) and (3).
>
> > [!note]- Full proof
> > The form $\Xi=\operatorname{tr}(\theta^{\wedge3})$, $\theta$ the Maurer–Cartan form of $SU(2)$, is bi-invariant (left-invariance is built into $\theta$; right-invariance uses $R_h^*\theta=\operatorname{Ad}_{h^{-1}}\theta$ and $\operatorname{Ad}$-invariance of the trace), hence a constant multiple of the volume form on $SU(2)\cong S^3$; its total integral is computed in the sign ledger on [[Def - The Hopf Bundle#Sign ledger]]:
> > $$\int_{SU(2)}\operatorname{tr}(\theta^{\wedge3})=-24\pi^2.$$
> > For $g\colon M\to SU(2)$ with $M$ a closed oriented $3$-manifold, $\operatorname{tr}((g^{-1}dg)^{\wedge3})=g^*\Xi$, and by [[Thm - The Brouwer Degree is an Integer and a Homotopy Invariant|the degree theorem]] $\int_M g^*\Xi=\deg g\cdot\int_{SU(2)}\Xi=-24\pi^2\deg g$. $\;\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> **Part (1) — the pointwise identity.** This is Lemma 1: $\operatorname{cs}(A^g)=\operatorname{cs}(A)-\tfrac13\operatorname{tr}(\theta^{\wedge3})-d\operatorname{tr}(dg\,g^{-1}\wedge A)$, with every cancellation displayed there.
>
> **Part (2) — the integral identity.** Integrate Part (1) over $M$ and divide by $8\pi^2$:
> $$\frac1{8\pi^2}\int_M\operatorname{cs}(A^g)=\frac1{8\pi^2}\int_M\operatorname{cs}(A)-\frac1{24\pi^2}\int_M\operatorname{tr}(\theta^{\wedge3})-\frac1{8\pi^2}\int_M d\operatorname{tr}(dg\,g^{-1}\wedge A).$$
> Since $M$ is closed (boundaryless), [[Thm - Stokes' Theorem on Manifolds|Stokes' theorem]] gives $\int_M d\operatorname{tr}(dg\,g^{-1}\wedge A)=0$. By Lemma 2, $\int_M\operatorname{tr}(\theta^{\wedge3})=-24\pi^2\deg g$, so $-\frac1{24\pi^2}\int_M\operatorname{tr}(\theta^{\wedge3})=+\deg g$. Hence
> $$\frac1{8\pi^2}\int_M\operatorname{cs}(A^g)=\frac1{8\pi^2}\int_M\operatorname{cs}(A)+\deg g.$$
>
> **Part (3) — the gauge law and well-definedness.** By definition $\vartheta(A)=\tfrac1{8\pi^2}\int_M\operatorname{cs}(A)$, so Part (2) reads $\vartheta(A\cdot g)=\vartheta(A)+\deg g$ in $\mathbb R$. Because $\deg g\in\mathbb Z$ ([[Thm - The Brouwer Degree is an Integer and a Homotopy Invariant|degree theorem]]), the class of $\vartheta(A)$ in $\mathbb R/\mathbb Z$ is unchanged by the gauge transformation $g$. 
>
> It remains to see this makes $\vartheta$ well defined on the (trivial) $SU(2)$-bundle $P\to M$ independently of trivialisation. By [[Thm - Classification of Principal SU(2)-Bundles over Four-Manifolds|part (A)]], $P$ is trivial, and any two trivialisations differ by a gauge transformation $g\colon M\to SU(2)$; the connection's two coordinate expressions are $A$ and $A\cdot g$ ([[Thm - Gauge Action on Connection Matrices|gauge action]]). By the above, their Chern–Simons values differ by the integer $\deg g$, so
> $$\vartheta(A)\in\mathbb R/\mathbb Z\quad\text{is independent of the trivialisation,}$$
> and, applied to gauge transformations of a fixed trivialisation, $\vartheta$ is invariant under the gauge group $\mathcal G(P)=\operatorname{Map}(M,SU(2))$ modulo $\mathbb Z$. Therefore $\vartheta$ descends to a well-defined map $\mathcal A(P)/\mathcal G(P)\to\mathbb R/\mathbb Z$. This proves the theorem. $\;\blacksquare$

---

# Cross-Field Exercise Suggestions

**The Chern–Simons action in physics.** The three-dimensional Chern–Simons action $S[A]=\frac{k}{4\pi}\int_M\operatorname{tr}(A\,dA+\frac23A^3)$ (level $k\in\mathbb Z$) must be gauge invariant modulo $2\pi$ for the path integral $e^{iS}$ to be defined; this theorem is exactly that statement, with the level quantisation forced by the integrality of $\deg g$. The application is non-obvious because the physical consistency condition (well-defined amplitude) is the mathematical statement that the ambiguity is integral.

**Spectral flow and the eta invariant.** For a path of connections $A_t$ from $A$ to $A^g$, the spectral flow of the associated family of Dirac-type operators equals $\deg g$ times a constant, matching the jump $\vartheta(A^g)-\vartheta(A)$; the theorem's integral identity is the topological half of the Atiyah–Patodi–Singer index computation on $M\times[0,1]$. The non-obvious link is between an analytic count of eigenvalue crossings and the degree of a gauge transformation.

**The Casson invariant.** For a homology three-sphere, counting flat $SU(2)$-connections with signs (the Casson invariant) uses that the Chern–Simons functional is a well-defined $\mathbb R/\mathbb Z$-valued Morse function on $\mathcal A/\mathcal G$ whose critical points are the flat connections; the well-definedness proved here is the starting point. The application is non-obvious because a signed count of representations is organised by the critical-point theory of exactly this functional.

---

# Bridges

- **The second Chern number.** The same gauge-variation identity, applied across the clutching sphere of a four-manifold rather than integrated over a closed three-manifold, produces the Chern number: [[Thm - Second Chern Number of an SU(2)-Bundle over a Closed Four-Manifold is the Clutching Degree]] uses Lemma 1 with $\int_{S^3}$ in place of $\int_M$. The two theorems are the same computation read in three and four dimensions.

- **The transgression formula.** The Chern–Simons form $\operatorname{cs}(A)$ is the transgression of $\operatorname{tr}(F\wedge F)$: on a trivial bundle $d\operatorname{cs}(A)=\operatorname{tr}(F_A\wedge F_A)$, proved on [[Thm - Transgression Formula and the Chern-Simons Form]]. The consistency check in Lemma 1 uses exactly this, and the definition of $\vartheta$ rests on it.

- **The critical points of $\vartheta$.** Because $\vartheta$ is gauge invariant modulo $\mathbb Z$, its differential descends and its critical set is gauge invariant; the first variation $d\vartheta_A(a)=\frac1{4\pi^2}\int_M\operatorname{tr}(F_A\wedge a)$ shows the critical points are the flat connections, developed on **[[Thm - Critical Points of the Chern-Simons Functional are the Flat Connections]]**.

- **The sign ledger.** The gauge law $\vartheta(A\cdot g)=\vartheta(A)+\deg g$ is item (c) of [[Def - The Hopf Bundle#Sign ledger]]; its sign follows from $\int_{SU(2)}\operatorname{tr}(\theta^{\wedge3})=-24\pi^2$ (item (a)) and is shared with the four-dimensional Chern-number sign (item (b)).

---

# Unlocked by This

> [!tip] The Chern–Simons functional as an $\mathbb R/\mathbb Z$-valued function *(from Gauge Theory VI §6.4)*
> This theorem is exactly the well-definedness clause of **[[Def - Chern-Simons Functional]]**; without it $\vartheta$ would depend on the arbitrary trivialisation.

> [!tip] Flat connections as vacua *(from Gauge Theory VI §6.4)*
> Gauge invariance of $\vartheta$ modulo $\mathbb Z$ makes its critical set — the flat connections, i.e. representations $\pi_1(M)\to SU(2)$ — a gauge-invariant object; see **[[Thm - Critical Points of the Chern-Simons Functional are the Flat Connections]]**.
