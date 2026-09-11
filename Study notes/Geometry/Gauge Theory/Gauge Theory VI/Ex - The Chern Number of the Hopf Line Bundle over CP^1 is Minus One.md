---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - First Chern Class of a Line Bundle from Curvature"
  - "Def - The Hopf Bundle"
  - "Ex - Connection Forms of the Hopf Connection in the Two Local Sections"
  - "Thm - Winding Number of a Map from the Circle to U(1)"
  - "Thm - Stokes' Theorem on Manifolds"
  - "Thm - Structure Equation for the Curvature"
tags: [geometry, gauge-theory, characteristic-classes, hopf, chern-number]
---

# Problem Statement

Let $L=\mathcal{O}(-1)\to\mathbb{CP}^1$ be the tautological (Hopf) line bundle, the complex line bundle associated to the Hopf $U(1)$-bundle $\pi\colon S^3\to\mathbb{CP}^1$ by the standard representation, and let $F=F_a\in\Omega^2(\mathbb{CP}^1;i\mathbb{R})$ be the curvature of the connection induced by the standard Hopf connection. Cover $\mathbb{CP}^1$ by the two affine charts $U_1=\{[z_0:z_1]:z_0\ne0\}$ and $U_2=\{z_1\ne0\}$, with the standard unitary local sections $s_1,s_2$ of the Hopf bundle and local potentials $A_1=s_1^*a$, $A_2=s_2^*a$ computed in chapter IV.

Compute the **first Chern number** of $L$,
$$\frac{i}{2\pi}\int_{\mathbb{CP}^1}F\ \in\ \mathbb{Z},$$
using only the two local potentials $A_1,A_2$, Stokes' theorem, and the winding number of the Hopf transition function. Show that the answer is
$$\frac{i}{2\pi}\int_{\mathbb{CP}^1}F=-\,w\!\left(\frac{z}{|z|}\right)=-1,$$
where $w$ is the winding number of the transition function $z/|z|$ around the boundary of the trivialising disc.

**Recall:**

The objects in play are the Hopf line bundle and its transition function, the two local potentials of the Hopf connection, the abelian gauge law relating them, the winding number of a circle map, Stokes' theorem, and the curvature-to-Chern-class normalisation.

*The Hopf bundle and its transition function.* By [[Def - The Hopf Bundle|the Hopf-bundle definition]], $\pi\colon S^3\to\mathbb{CP}^1$, $z\mapsto[z]$, is the principal $U(1)$-bundle with right action $z\cdot\lambda=z\lambda$; its associated line bundle by the standard representation is the tautological bundle $\mathcal{O}(-1)$, whose fibre over $[z]$ is the complex line $\mathbb{C}\cdot z\subset\mathbb{C}^2$. On the overlap $U_1\cap U_2$ the two standard sections are related by $s_2=s_1\cdot g_{12}$ with transition function $g_{12}=z/|z|$ (in the affine coordinate $z$ centred on the trivialising disc; the misprint "$|z|/z$" in the source is corrected on the Hopf-bundle page). Restricted to the equatorial circle, $z/|z|$ is the identity map $z\mapsto z$, so it has winding number $1$.

*The two local potentials (chapter IV).* By [[Ex - Connection Forms of the Hopf Connection in the Two Local Sections|the chapter-IV potential exercise]], in the affine coordinate $\zeta=z_1/z_0$ on $U_1$ the potential is
$$A_1=s_1^*a=\frac{\operatorname{Im}(\bar\zeta\,d\zeta)}{1+|\zeta|^2}\,i,$$
smooth on all of $U_1$; symmetrically $A_2=s_2^*a=\dfrac{\operatorname{Im}(\bar z\,dz)}{1+|z|^2}\,i$ in the coordinate $z=z_0/z_1$ on $U_2$, smooth on all of $U_2$. They obey the abelian gauge law
$$A_2=A_1+g_{12}^{-1}\,dg_{12}=A_1+i\,d(\arg z),$$
the second equality because $g_{12}=z/|z|=e^{i\arg z}$ and $g_{12}^{-1}dg_{12}=i\,d(\arg z)$.

*Curvature of an abelian connection.* By [[Thm - Structure Equation for the Curvature|the structure equation]], the local curvature is $F=dA_j+\tfrac12[A_j\wedge A_j]$; since $U(1)$ is abelian the bracket term vanishes, so
$$F=dA_1\ \text{on }U_1,\qquad F=dA_2\ \text{on }U_2,$$
and $F$ is a single globally defined $2$-form on $\mathbb{CP}^1$ with values in $i\mathbb{R}$.

*The winding number.* By [[Thm - Winding Number of a Map from the Circle to U(1)|the winding-number theorem]], for a smooth $g\colon S^1\to U(1)$,
$$w(g)=\frac{1}{2\pi i}\int_{S^1}g^{-1}\,dg\in\mathbb{Z},\qquad w(z\mapsto z^k)=k,$$
$w$ is a homotopy invariant, and $w(g_1g_2)=w(g_1)+w(g_2)$. In particular $w(z/|z|)=1$.

*The theorem being confirmed (chapter VI).* The series convention $c_1(L)=[\tfrac{i}{2\pi}F]$ (see [[Def - Chern Classes|Chern classes]]) makes the quantity above the value of $c_1(\mathcal{O}(-1))$ on the fundamental class of $\mathbb{CP}^1$.

![[Thm - First Chern Class of a Line Bundle from Curvature#Statement]]

> [!warning] Convention: orientation and the transition disc
> $\mathbb{CP}^1$ carries the **complex orientation** (in the affine coordinate $\zeta=\xi+i\eta$, the orientation $d\xi\wedge d\eta$). We write $\mathbb{CP}^1=D\cup D'$, where $D$ is the closed disc $\{|z|\le1\}$ around $[0:1]$ in the coordinate $z=z_0/z_1$ (the *distinguished* disc, carrying the section $s_2$ and potential $A_2$), and $D'=\{|\zeta|\le1\}$ is the closed disc around $[1:0]$ carrying $s_1,A_1$; they meet along the equator $C=\{|z|=1\}=\{|\zeta|=1\}$. The winding number $w(z/|z|)=1$ is measured around $\partial D=C$ in the boundary orientation induced by $D$ (counter-clockwise in $z$). This is the disc convention of [[Def - The Hopf Bundle|the Hopf-bundle page]] and its sign ledger; every quantity below is coordinate-independent, so the final integer does not depend on this bookkeeping.

---

# Convergent Strategy

**Problem class.** This is a *compute a characteristic number by Stokes* problem — the archetype for the degree of a line bundle over a closed oriented surface. The curvature $F$ is a globally defined closed $2$-form, but it is *not* globally exact (that is the whole point: its integral is a nonzero topological invariant). The strategy exploits that $F$ *is* exact on each of two trivialising discs, $F=dA_j$, so Stokes turns the surface integral into a boundary integral of the difference $A_2-A_1$, which the gauge law identifies with $g_{12}^{-1}dg_{12}$ — a pure winding number.

**Assumption pattern.** The recognisable trigger is: a closed $2$-form whose de Rham class is to be evaluated on a closed surface, together with an open cover on which the form is exact with *explicit* primitives. Whenever local primitives exist but no global one does, the invariant lives entirely in how the primitives fail to agree on overlaps. For a line bundle the mismatch $A_2-A_1$ is exactly $g^{-1}dg$ (abelian gauge law), so the invariant is the winding number of the transition function. The hypothesis "abelian structure group" is used twice: once to kill $\tfrac12[A\wedge A]$ so that $F=dA_j$, and once to make the gauge law additive, $A_2-A_1=g^{-1}dg$.

**Theorem routing.** The route is: (i) split $\mathbb{CP}^1=D\cup D'$ along the equator $C$, with $F=dA_2$ on $D$ and $F=dA_1$ on $D'$ ([[Thm - Structure Equation for the Curvature|structure equation]], abelian); (ii) apply [[Thm - Stokes' Theorem on Manifolds|Stokes]] on each disc, noting $\partial D=C$ and $\partial D'=-C$; (iii) add to get $\int_{\mathbb{CP}^1}F=\oint_C(A_2-A_1)$; (iv) substitute the abelian gauge law $A_2-A_1=g_{12}^{-1}dg_{12}$ from [[Ex - Connection Forms of the Hopf Connection in the Two Local Sections|the chapter-IV potential exercise]]; (v) recognise $\oint_C g_{12}^{-1}dg_{12}=2\pi i\,w(g_{12})$ with $w(z/|z|)=1$ ([[Thm - Winding Number of a Map from the Circle to U(1)|winding-number theorem]]); (vi) apply the normalisation $\tfrac{i}{2\pi}$. The output confirms part (a) of [[Thm - First Chern Class of a Line Bundle from Curvature|the first-Chern-class theorem]].

**Key decision point.** The one move that must be made correctly is the *orientation bookkeeping of the two boundaries*. Both discs induce the complex orientation on $\mathbb{CP}^1$, so their shared boundary $C$ appears with opposite induced orientations: $\partial D=C$ but $\partial D'=-C$. This is what produces the *difference* $A_2-A_1$ rather than a sum, and it is the difference — the failure of the potentials to glue — that carries the topology. Getting either boundary orientation wrong flips the sign of the answer; the check that the result is $-1$ (and not $+1$), consistent with the geometric computation on [[Ex - Curvature of the Hopf Connection and the Round Metric of Radius One Half|the round-metric companion]], is what pins it.

---

# Legal Operations Used

This solution deploys the following operations (numbered as on [[Gauge Theory VI — Chern–Weil Theory, Characteristic Classes, and the Chern–Simons Functional#Legal Operations|the topic page's Legal Operations]]; where the topic page is not yet assembled the operation is named descriptively and the orchestrator will reconcile numbers).

1. **Split a closed surface into two trivialising discs along a common circle.** Cover $\mathbb{CP}^1$ by the two charts on which the Hopf bundle trivialises and cut it into the discs $D,D'$ meeting on the equator $C$, so that the curvature is exact on each piece.

2. **Reduce curvature to $dA_j$ using an abelian structure group.** From the structure equation, $F=dA_j+\tfrac12[A_j\wedge A_j]=dA_j$ since $U(1)$ is abelian, giving an explicit primitive on each disc.

3. **Apply Stokes on each piece and combine with induced boundary orientations.** Convert $\int_{D}dA_2$ and $\int_{D'}dA_1$ into boundary integrals over $\partial D=C$ and $\partial D'=-C$, and add to obtain $\oint_C(A_2-A_1)$.

4. **Replace a potential difference by the logarithmic derivative of the transition function.** Use the abelian gauge law $A_2-A_1=g_{12}^{-1}dg_{12}$ to turn the boundary integral into $\oint_C g_{12}^{-1}dg_{12}$.

5. **Identify a logarithmic-derivative integral with a winding number.** Recognise $\oint_C g_{12}^{-1}dg_{12}=2\pi i\,w(g_{12})$ and evaluate $w(z/|z|)=1$.

6. **Apply the Chern normalisation to read off the integer.** Multiply by $\tfrac{i}{2\pi}$ to obtain $\int_{\mathbb{CP}^1}c_1(L)=-w(z/|z|)=-1$.

---

# Hints

> [!note]- Hint 1
> The curvature $F$ is closed but not exact on all of $\mathbb{CP}^1$ — if it were, its integral would vanish by Stokes, and the answer would be $0$, which it is not. But $F$ *is* exact on each affine chart, where you already have explicit primitives $A_1,A_2$ from chapter IV. Cut $\mathbb{CP}^1$ into two discs so that a single primitive is available on each.

> [!note]- Hint 2
> Why is $F=dA_j$ and not $F=dA_j+\tfrac12[A_j\wedge A_j]$? Because the structure group is $U(1)$, which is abelian, so the bracket term is zero. This is the first of two places the abelian hypothesis is essential.

> [!note]- Hint 3
> Apply Stokes to $\int_D dA_2$ and $\int_{D'}dA_1$ separately. The two discs share the boundary circle $C$, but with opposite induced orientations ($\partial D=C$, $\partial D'=-C$), because both are oriented by the complex orientation of $\mathbb{CP}^1$. When you add, you get the *difference* $\oint_C(A_2-A_1)$, not a sum. The difference is where the topology hides.

> [!note]- Hint 4
> The difference $A_2-A_1$ is not something you must recompute: the abelian gauge law gives $A_2-A_1=g_{12}^{-1}dg_{12}$ directly, with $g_{12}=z/|z|$ the Hopf transition function. So $\oint_C(A_2-A_1)=\oint_C g_{12}^{-1}dg_{12}$. What is $\tfrac{1}{2\pi i}\oint_C g^{-1}dg$ called, and what is its value for $g=z/|z|$ on the unit circle?

> [!note]- Hint 5
> $\tfrac{1}{2\pi i}\oint_C g^{-1}dg=w(g)$ is the winding number, and $w(z/|z|)=1$ because on $|z|=1$ the map $z/|z|$ is just $z\mapsto z$. So $\int_{\mathbb{CP}^1}F=2\pi i\cdot1=2\pi i$. Finish by multiplying by $\tfrac{i}{2\pi}$: the answer is $i^2=-1=-w(z/|z|)$.

---

# Solution

The plan is to cut $\mathbb{CP}^1$ into two trivialising discs, use the abelian structure group to write the curvature as $dA_j$ on each, apply Stokes to convert the surface integral into a boundary integral of $A_2-A_1$, and finish by recognising that difference — via the gauge law — as $2\pi i$ times the winding number of the transition function $z/|z|$. Every ingredient is an off-the-shelf chapter-IV computation; the only genuine care is the orientation of the two boundaries, which turns the sum of two disc integrals into a single winding number and fixes the sign.

**Step 1: split $\mathbb{CP}^1$ and write $F=dA_j$ on each disc.**

$\mathbb{CP}^1=D\cup D'$ with $D,D'$ the two closed trivialising discs meeting on the equator $C$; on $D$, $F=dA_2$, and on $D'$, $F=dA_1$.

> [!note]- Derivation
> Let $D=\{[z_0:z_1]:|z_0/z_1|\le1\}$ be the closed disc around $[0:1]$ in the coordinate $z=z_0/z_1$, contained in $U_2$; and $D'=\{|z_1/z_0|\le1\}$ the closed disc around $[1:0]$ in $\zeta=z_1/z_0=1/z$, contained in $U_1$. Their union is all of $\mathbb{CP}^1$, and they meet exactly in the equatorial circle
> $$C=\{|z|=1\}=\{|\zeta|=1\},\qquad\text{on which }\zeta=1/z=\bar z.$$
> Each is an embedded closed disc with boundary $C$, hence a smooth compact manifold with boundary ([[Def - Manifold with Boundary and Induced Orientation|manifold with boundary]]).
>
> On $U_2\supseteq D$ the curvature has the primitive $A_2$: by [[Thm - Structure Equation for the Curvature|the structure equation]], $F=dA_2+\tfrac12[A_2\wedge A_2]$, and since the structure group $U(1)$ is abelian its Lie algebra $\mathfrak{u}(1)=i\mathbb{R}$ has trivial bracket, so $[A_2\wedge A_2]=0$ and
> $$F=dA_2\quad\text{on }D.$$
> Identically, $F=dA_1$ on $D'$. The potential $A_2=\tfrac{\operatorname{Im}(\bar z\,dz)}{1+|z|^2}\,i$ is smooth on all of $U_2$, in particular on the closed disc $D$ (including its centre $[0:1]$), and $A_1$ is smooth on the closed disc $D'$; this is what will make Stokes applicable on each piece.

**Step 2: apply Stokes on each disc and combine.**

Stokes on $D$ and $D'$, with their induced boundary orientations, gives $\int_{\mathbb{CP}^1}F=\oint_C(A_2-A_1)$.

> [!note]- Derivation
> Both charts induce the complex orientation on $\mathbb{CP}^1$: the change of coordinate $\zeta=1/z$ is holomorphic, hence orientation-preserving, so orienting $D$ by $d(\operatorname{Re}z)\wedge d(\operatorname{Im}z)$ and $D'$ by $d(\operatorname{Re}\zeta)\wedge d(\operatorname{Im}\zeta)$ agrees on the overlap. Consequently the decomposition is orientation-consistent and
> $$\int_{\mathbb{CP}^1}F=\int_{D}F+\int_{D'}F=\int_{D}dA_2+\int_{D'}dA_1 \qquad\text{(Step 1; the two discs overlap only in }C\text{, a set of measure zero).}$$
> Apply [[Thm - Stokes' Theorem on Manifolds|Stokes' theorem]] to each disc, with the boundary carrying the orientation induced by the disc:
> $$\int_{D}dA_2=\oint_{\partial D}A_2,\qquad \int_{D'}dA_1=\oint_{\partial D'}A_1.$$
> As boundaries of the two discs, $C$ appears with opposite orientations: $\partial D=C$ oriented counter-clockwise in $z$, while $\partial D'$ is $C$ oriented counter-clockwise in $\zeta=1/z=\bar z$ on $C$, which is clockwise in $z$; hence $\partial D'=-C$. Therefore
> $$\int_{\mathbb{CP}^1}F=\oint_{C}A_2+\oint_{-C}A_1=\oint_{C}A_2-\oint_{C}A_1=\oint_{C}\big(A_2-A_1\big).$$
> The opposite boundary orientations are exactly what convert the two disc integrals into the *difference* of the potentials — the mismatch that carries the topological content.

**Step 3: replace $A_2-A_1$ by the transition function and integrate.**

The abelian gauge law turns $A_2-A_1$ into $g_{12}^{-1}dg_{12}$, whose integral over $C$ is $2\pi i$ times the winding number of $g_{12}=z/|z|$.

> [!note]- Derivation
> By [[Ex - Connection Forms of the Hopf Connection in the Two Local Sections|the chapter-IV potential exercise]], the two potentials are related by the abelian gauge law
> $$A_2-A_1=g_{12}^{-1}\,dg_{12},\qquad g_{12}=\frac{z}{|z|},$$
> which for the abelian group $U(1)$ is additive (there is no $\operatorname{Ad}$-twist). Substituting into Step 2,
> $$\int_{\mathbb{CP}^1}F=\oint_{C}g_{12}^{-1}\,dg_{12}.$$
> Parametrise $C=\partial D$ counter-clockwise in $z$ by $z=e^{i\psi}$, $\psi\in[0,2\pi]$; there $g_{12}=z/|z|=e^{i\psi}$, so
> $$g_{12}^{-1}\,dg_{12}=e^{-i\psi}\,d\big(e^{i\psi}\big)=e^{-i\psi}\big(ie^{i\psi}\big)\,d\psi=i\,d\psi,$$
> and hence
> $$\oint_{C}g_{12}^{-1}\,dg_{12}=\int_{0}^{2\pi}i\,d\psi=2\pi i.$$
> Equivalently, by [[Thm - Winding Number of a Map from the Circle to U(1)|the winding-number theorem]],
> $$\oint_{C}g_{12}^{-1}\,dg_{12}=2\pi i\,w(g_{12}),\qquad w(g_{12})=w\!\left(\frac{z}{|z|}\right)=1,$$
> the value $1$ because $z/|z|$ restricted to $C=\{|z|=1\}$ is the identity map $z\mapsto z$, which has winding number $1$. Thus $\int_{\mathbb{CP}^1}F=2\pi i$.

**Step 4: read off the Chern number.**

Applying the normalisation $\tfrac{i}{2\pi}$ gives $-w(z/|z|)=-1$.

> [!note]- Derivation
> With the series convention $c_1(L)=\big[\tfrac{i}{2\pi}F\big]$ ([[Def - Chern Classes|Chern classes]]),
> $$\int_{\mathbb{CP}^1}c_1(\mathcal{O}(-1))=\frac{i}{2\pi}\int_{\mathbb{CP}^1}F=\frac{i}{2\pi}\cdot2\pi i\,w(g_{12})=i^2\,w\!\left(\frac{z}{|z|}\right)=-w\!\left(\frac{z}{|z|}\right)=-1.$$
> This is exactly part (a) of [[Thm - First Chern Class of a Line Bundle from Curvature|the first-Chern-class theorem]]: the tautological bundle over $\mathbb{CP}^1$ has Chern number $-1$. In particular $c_1(\mathcal{O}(-1))\ne0$, so $\mathcal{O}(-1)$ — equivalently the Hopf $U(1)$-bundle — is nontrivial, recovering the nontriviality of the Hopf bundle from a curvature integral.

> [!note]- Complete formal solution
> **Claim.** $\dfrac{i}{2\pi}\displaystyle\int_{\mathbb{CP}^1}F=-w\!\left(\dfrac{z}{|z|}\right)=-1$.
>
> Write $\mathbb{CP}^1=D\cup D'$, where $D=\{|z|\le1\}$ (coordinate $z=z_0/z_1$, section $s_2$, potential $A_2$) is the closed disc around $[0:1]$ and $D'=\{|\zeta|\le1\}$ (coordinate $\zeta=z_1/z_0=1/z$, section $s_1$, potential $A_1$) is the closed disc around $[1:0]$; they meet in the equator $C=\{|z|=1\}$. Since $U(1)$ is abelian, the structure equation gives $F=dA_2$ on $D$ and $F=dA_1$ on $D'$, with each potential smooth on its closed disc.
>
> Both charts induce the complex orientation, so
> $$\int_{\mathbb{CP}^1}F=\int_D dA_2+\int_{D'}dA_1=\oint_{\partial D}A_2+\oint_{\partial D'}A_1=\oint_C A_2-\oint_C A_1=\oint_C(A_2-A_1),$$
> using Stokes on each disc and $\partial D=C$, $\partial D'=-C$. The abelian gauge law $A_2-A_1=g_{12}^{-1}dg_{12}$ with $g_{12}=z/|z|$ gives
> $$\int_{\mathbb{CP}^1}F=\oint_C g_{12}^{-1}dg_{12}=2\pi i\,w(g_{12})=2\pi i,$$
> since $w(z/|z|)=1$ (on $C$ the map is $z\mapsto z$). Finally
> $$\frac{i}{2\pi}\int_{\mathbb{CP}^1}F=\frac{i}{2\pi}\cdot2\pi i=i^2=-1=-w\!\left(\frac{z}{|z|}\right).\qquad\blacksquare$$

> [!warning] Illegal but tempting shortcut
> One is tempted to write $\int_{\mathbb{CP}^1}F=\int_{\mathbb{CP}^1}dA_1$ and conclude it is $0$ by Stokes on the *closed* manifold $\mathbb{CP}^1$. This is illegal: $A_1$ is **not** a global $1$-form on $\mathbb{CP}^1$ — it is singular at $[0:1]$, the one point of $U_2$ missing from $U_1$ — so $F$ is not globally exact and Stokes on the closed surface does not apply to it. The nonvanishing of $\int F$ is precisely the obstruction to gluing $A_1$ and $A_2$ into a global primitive; the winding number $w(z/|z|)=1$ measures that obstruction. The two-disc computation is legal because each potential is genuinely smooth on its own closed disc, and it is legal to apply Stokes there.

> [!note]- Companion comparison and independent check
> The algebraic-topology companion [[Ex - The Chern Number of the Hopf Line Bundle over CP^1|"The Chern Number of the Hopf Line Bundle over CP^1"]] obtains the same integer $-1$ by the Fubini–Study curvature and by the classifying-space classification $\operatorname{Pic}(\mathbb{CP}^1)\cong\mathbb{Z}$. Its normalisation is stated as $c_1(L)=[F/(2\pi)]$ with $F$ written as a *real* $2$-form (the curvature of the real connection $1$-form); the series here writes the curvature as an $i\mathbb{R}$-valued form and normalises by $\tfrac{i}{2\pi}$. The two conventions differ only by whether the factor of $i$ is absorbed into $F$ or displayed, and they give the identical value $c_1(\mathcal{O}(-1))[\mathbb{CP}^1]=-1$. The geometric route on [[Ex - Curvature of the Hopf Connection and the Round Metric of Radius One Half|the round-metric companion]] gives $\int_{\mathbb{CP}^1}F=2\pi i$ independently — from the area $\operatorname{Vol}(S^2_{1/2})=\pi$ rather than from a winding number — confirming the present Stokes computation.

---

# Key Takeaways

**When a closed form has explicit local primitives but no global one, its integral is the winding number of the gluing data.** The curvature $F$ of a nontrivial line bundle is the canonical example: it is closed, so it defines a de Rham class, but it is not exact, so that class is nonzero. The technique for evaluating $\int_\Sigma F$ is never to find a global primitive — none exists — but to find primitives on the pieces of a trivialising cover and measure how they fail to agree on the overlaps. For a line bundle over a surface, cutting into two discs reduces the entire integral to $\oint_C(A_2-A_1)$ over one equatorial circle, and the abelian gauge law turns that mismatch into $\oint_C g^{-1}dg=2\pi i\,w(g)$. The reusable principle: *a characteristic number is an obstruction to gluing, and Stokes localises the obstruction onto the overlap.* This is the surface prototype of the general Chern–Weil statement that a characteristic class is the cohomological measure of a bundle's failure to be trivial, and it recurs verbatim for the degree of any $U(1)$-bundle over any closed oriented surface.

**The abelian hypothesis is used twice, and both uses are load-bearing.** First, it kills the quadratic term in the structure equation, so $F=dA_j$ with a genuine primitive on each chart; for a nonabelian group $F=dA+\tfrac12[A\wedge A]$ has no such simple primitive, and the corresponding computation (for $c_2$ of an $SU(2)$-bundle over a $4$-manifold) requires the Chern–Simons transgression form instead of a bare potential. Second, it makes the gauge law additive, $A_2-A_1=g^{-1}dg$, with no $\operatorname{Ad}$-conjugation, so the overlap integral is literally the logarithmic derivative of the transition function and hence a winding number. The transferable diagnostic: when you see "$U(1)$" or "line bundle", expect the invariant to be a single winding/degree integer computed by exactly this two-disc Stokes argument; when the group is nonabelian, expect a transgression form and a more elaborate boundary term. Recognising which regime you are in tells you immediately whether the answer is "a winding number" or "an integral of $\operatorname{tr}(A\,dA+\tfrac23A^3)$".

**Orientation bookkeeping of the two boundaries is the whole sign of the answer, and a second computation is the cheapest guard.** The single subtle point is that both discs induce the complex orientation on $\mathbb{CP}^1$, so their common boundary $C$ appears with opposite orientations, producing the difference $A_2-A_1$ rather than a sum. Reverse either induced orientation and the answer flips to $+1$. Because the sign of $c_1$ propagates into the signs of $c_2$, of instanton numbers, and of the Chern–Simons variation throughout gauge theory, it must be pinned unambiguously; the reliable method is to compute the same invariant by a manifestly different route and demand agreement. Here the winding-number route ($-w(z/|z|)=-1$) agrees with the area route on [[Ex - Curvature of the Hopf Connection and the Round Metric of Radius One Half|the round-metric companion]] ($\tfrac{i}{2\pi}\cdot2\pi i=-1$), and both agree with the classifying-space count on the algebraic-topology page. Whenever a normalisation-sensitive integer can be reached two ways, do both: it is the only cheap defence against a dropped factor of $i$ or a reversed circle.
