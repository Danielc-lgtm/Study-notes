---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Chern Classes"
  - "Def - First Chern Class via the Classifying Map"
  - "Thm - Classification of Principal U(1)-Bundles by the First Chern Class"
  - "Thm - The Standard Connection on the Hopf Bundle"
  - "Ex - Curvature of the Standard Hopf Connection"
  - "Thm - The de Rham Cohomology of Complex Projective Space"
  - "Thm - Winding Number of a Map from the Circle to U(1)"
  - "Thm - Stokes' Theorem on Manifolds"
  - "Thm - Flat Connections and Monodromy Representations of the Fundamental Group"
  - "Thm - The Top de Rham Cohomology of a Closed Connected Oriented Manifold is R"
  - "Thm - Chern-Weil Theorem"
  - "Thm - Line Bundles over Compact Manifolds are Pulled Back from Projective Space"
  - "Thm - Naturality and Isomorphism Invariance of Characteristic Classes"
  - "Thm - Trivial Bundles Have Vanishing Characteristic Classes"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $M$ is a smooth compact manifold and $L\to M$ is a complex line bundle — a complex vector bundle of rank one — equipped with a Hermitian structure $\langle\cdot,\cdot\rangle$ (a smoothly varying Hermitian inner product on the fibres) and a **unitary connection** $\nabla$, that is, a connection satisfying $d\langle s,t\rangle=\langle\nabla s,t\rangle+\langle s,\nabla t\rangle$ for all sections $s,t\in\Gamma(L)$. We write $A$ for the local connection potential of $\nabla$ in a local unitary frame (a nowhere-vanishing section $s$ of unit length), so that $\nabla s=s\otimes A$ with $A\in\Omega^1(U;\mathfrak u(1))$ and $\mathfrak u(1)=i\mathbb R$; unitarity forces $A$ to take values in the skew-Hermitian scalars $i\mathbb R$. The **curvature** is $F_\nabla\in\Omega^2(M;i\mathbb R)$; because the structure group $U(1)$ is abelian, the bracket term in the structure equation vanishes and $F_\nabla=dA$ in every local unitary frame, so $F_\nabla$ is a globally defined imaginary-valued $2$-form. We abbreviate $F_A:=F_\nabla$ when a potential $A$ is in view.

The **first Chern class from curvature** is the de Rham class
$$c_1(L):=\Big[\tfrac{i}{2\pi}F_A\Big]\in H^2_{dR}(M),$$
which is real-valued because $\tfrac{i}{2\pi}F_A$ is a real $2$-form ($F_A$ is imaginary), and which is independent of the choice of unitary connection by the [[Thm - Chern-Weil Theorem|Chern–Weil theorem]]; see [[Def - Chern Classes]]. The **topological first Chern class** $c_1^{\mathrm{top}}(L)\in H^2_{dR}(M)$ is the class defined in chapter III by pulling back the generator of $H^2_{dR}(\mathbb{CP}^N)$ along a classifying map; see [[Def - First Chern Class via the Classifying Map]]. The group of isomorphism classes of Hermitian line bundles over $M$ under tensor product is $\operatorname{Pic}(M)$, with identity the trivial bundle $\underline{\mathbb C}=M\times\mathbb C$ and inverse the dual bundle $L^\vee$.

The Hopf bundle is $\pi\colon S^{2N+1}\to\mathbb{CP}^N$, and $\omega_N\in\Omega^2(\mathbb{CP}^N)$ denotes the normalised Fubini–Study generator of [[Thm - The de Rham Cohomology of Complex Projective Space|its second de Rham cohomology]], characterised by $\pi^*\omega_N=\tfrac1\pi\sum_{j=0}^N dx_j\wedge dy_j$ (with $z_j=x_j+iy_j$ the standard coordinates on $\mathbb C^{N+1}\supset S^{2N+1}$) and $\int_{\mathbb{CP}^1}\omega_1=1$. The tautological line bundle is $\mathcal O(-1)\to\mathbb{CP}^N$, the subbundle of $\underline{\mathbb C^{N+1}}$ whose fibre over a line $\ell\in\mathbb{CP}^N$ is $\ell$ itself; it is the line bundle associated to the Hopf bundle through the standard representation of $U(1)$ on $\mathbb C$.

For a closed (compact, boundaryless) connected oriented surface $\Sigma$ and a smooth map $g\colon S^1\to U(1)$, the **winding number** is $w(g):=\tfrac{1}{2\pi i}\oint_{S^1}g^{-1}\,dg\in\mathbb Z$; see [[Thm - Winding Number of a Map from the Circle to U(1)]]. The **degree** $\deg L\in\mathbb Z$ of a line bundle over $\Sigma$ is the clutching winding number of chapter III; see [[Def - First Chern Class via the Classifying Map]] and [[Thm - Classification of Principal U(1)-Bundles by the First Chern Class]].

> [!warning] Convention: the prefactor $\tfrac{i}{2\pi}$ versus $\tfrac{1}{2\pi i}$
> This series normalises the first Chern class by $c_1(L)=\big[\tfrac{i}{2\pi}F_A\big]$, following Haydys. Bär's characteristic-class chapter writes $c_1(P)=\big[\tfrac{1}{2\pi i}\bar\Omega\big]$ for the descended curvature $\bar\Omega=F_A$. Since $\tfrac{1}{2\pi i}=\tfrac{1}{2\pi i}\cdot\tfrac{i}{i}=\tfrac{i}{2\pi i^2}=-\tfrac{i}{2\pi}$, the two prefactors differ by an overall sign, so Bär's $c_1$ is the negative of the series' $c_1$. We adopt $\tfrac{i}{2\pi}$ so that $\int_{\mathbb{CP}^1}c_1(\mathcal O(-1))=-1$ and $\deg\mathcal O(1)=+1$, in agreement with the complex orientation of $\mathbb{CP}^1$ fixed in the series conventions. Bär's non-triviality criterion ($\int_\Sigma\bar\Omega\ne0\Rightarrow$ non-trivial) is insensitive to this sign and transfers unchanged.

> [!warning] Convention: the integration domain in Haydys' Remark 92
> Haydys' Remark 92 (the source of part (b) below) prints the integrality statement as $\tfrac{i}{2\pi}\int_M h^*F_\nabla\in\mathbb Z$ for a map $h\colon\Sigma\to M$. This is a typo: the integral is taken over the two-dimensional domain $\Sigma$, not over $M$ (which may have any dimension). We write $\tfrac{i}{2\pi}\int_\Sigma h^*F_\nabla$ throughout (Appendix B, item 5 of the source content map).

---

# Statement

> **Theorem (first Chern class of a line bundle from curvature).** Let $L\to M$ be a complex line bundle over a smooth compact manifold, with Hermitian structure and unitary connection $A$, curvature $F_A\in\Omega^2(M;i\mathbb R)$. Then:
>
> **(a) Agreement with the topological class.** $c_1(L)=\big[\tfrac{i}{2\pi}F_A\big]$ equals the topological first Chern class $c_1^{\mathrm{top}}(L)$ of chapter III. In particular, for the tautological bundle $\mathcal O(-1)\to\mathbb{CP}^N$ with the connection induced by the Hopf connection,
> $$\tfrac{i}{2\pi}F=-\omega_N\quad\text{as forms},\qquad\text{and}\qquad\int_{\mathbb{CP}^1}\tfrac{i}{2\pi}F=-1.$$
>
> **(b) Integrality and degree.** For every smooth map $h\colon\Sigma\to M$ from a closed connected oriented surface $\Sigma$,
> $$\tfrac{i}{2\pi}\int_\Sigma h^*F_A\in\mathbb Z,\qquad\text{and}\qquad\tfrac{i}{2\pi}\int_\Sigma h^*F_A=\deg(h^*L),$$
> the clutching degree of $h^*L$ from chapter III. In particular, when $M=\Sigma$ is itself a closed oriented surface and $h=\operatorname{id}$,
> $$\tfrac{i}{2\pi}\int_\Sigma F_A=\deg L=\int_\Sigma c_1(L),$$
> so that $\deg\colon\operatorname{Pic}(\Sigma)\to\mathbb Z$ is the map $L\mapsto\int_\Sigma c_1(L)$, and $c_1$ is a **complete invariant** of line bundles over a closed oriented surface: two such bundles are isomorphic if and only if they have equal first Chern class.
>
> **(c) Non-triviality obstruction.** If $c_1(L)\ne0$ then $L$ is non-trivial. More concretely, if there is a smooth $h\colon\Sigma\to M$ with $\int_\Sigma h^*F_A\ne0$ (in particular, if $M=\Sigma$ and $\int_\Sigma F_A\ne0$), then $L$ is non-trivial.
>
> **(d) Injectivity over simply connected bases.** If $M$ is connected and simply connected, then $c_1(L)=0$ implies $L$ is trivial; consequently $c_1\colon\operatorname{Pic}(M)\to H^2_{dR}(M)$ is an injective group homomorphism.

---

# Motivation

The Chern–Weil construction manufactures, out of a connection, a closed form whose de Rham class does not depend on the connection: for a Hermitian line bundle the form is $\tfrac{i}{2\pi}F_A$ and the class is $c_1(L)$. On its own this is a soft, analytic object — an element of a real vector space $H^2_{dR}(M)$, produced by an integral of curvature. The question this theorem answers is why anyone should believe that this analytic gadget carries *topological* information, and in fact carries **all** the topological information there is about a line bundle in low dimensions.

There are two independent constructions of a first Chern class in the notes, and they look nothing alike. The topological class $c_1^{\mathrm{top}}(L)$ of chapter III is built by homotopy theory: every line bundle over a compact base is pulled back from the tautological bundle over projective space by a classifying map $f$, unique up to homotopy, and one sets $c_1^{\mathrm{top}}(L)=-f^*[\omega_N]$. This is manifestly a homotopy invariant and manifestly integral in origin, but it says nothing about curvature. The Chern–Weil class $c_1(L)$ of chapter VI is built by differential geometry: integrate the curvature of any unitary connection. This is manifestly local and computable, but its integrality and its topological meaning are not visible from the definition. Part (a) is the statement that these two constructions produce the same element of $H^2_{dR}(M)$. That is the bridge between the homotopy-theoretic and the differential-geometric halves of the subject: a curvature integral is a homotopy invariant, and a homotopy invariant is computed by an integral of curvature.

Once the bridge is in place, the remaining parts are the payoff. Part (b) says that when one restricts to a surface, the curvature integral $\tfrac{i}{2\pi}\int_\Sigma F_A$ is not merely real but an *integer*, and equals the degree — a purely combinatorial clutching invariant counting how the two trivialisations of $L$ over the two halves of $\Sigma$ fail to match. This integrality is the mathematical content of Dirac's charge quantisation: the total magnetic flux through a closed surface, in the right units, must be a whole number, because it is the winding number of a transition function. Part (c) turns the class into an obstruction: a non-zero curvature integral is a certificate that the bundle cannot be trivial, and this is the standard way one proves a bundle non-trivial — the tangent bundle of the two-sphere, the tautological bundle, the monopole bundle. Part (d) is the converse over a simply connected base: there the class is a *complete* obstruction, so $c_1$ injects $\operatorname{Pic}(M)$ into cohomology. This last clause is what makes $c_1$ the right invariant to detect and classify line bundles on the simply connected four-manifolds of chapters XI and XIII, where $\operatorname{Pic}$ is exactly $H^2$.

---

# Sources and Targets

**Sources (Input Broadening).** The theorem's literal hypotheses are mild — a Hermitian line bundle with a unitary connection over a compact base — so the real question is which problems secretly present such data.

The first disguised source is **any complex line bundle whatsoever, with no connection or metric named**. Every complex line bundle over a compact manifold admits a Hermitian structure, unique up to homotopy, and every Hermitian bundle admits a unitary connection (average an arbitrary connection over a partition of unity, or reduce the structure group to $U(1)$ and use the affine structure of the space of connections). The non-obvious bridge is that the *choice* of these auxiliary data is irrelevant: the class $c_1(L)$ is independent of the connection by the [[Thm - Chern-Weil Theorem|Chern–Weil theorem]] and independent of the Hermitian structure by the convexity argument of [[Def - Chern Classes]]. So a bare line bundle already hands you everything the theorem needs. *Example problem:* given only the tautological bundle $\mathcal O(-1)\to\mathbb{CP}^1$ as a subbundle of the trivial rank-two bundle, produce a curvature and compute its integral, obtaining $-1$.

The second disguised source is **a magnetic field or gauge potential on a physical configuration space**. In electromagnetism a $U(1)$ gauge field on a manifold $M$ is exactly a connection on a Hermitian line bundle, and the field strength $F$ is $-i$ times the curvature. When the physics is set on a base containing a closed surface $\Sigma$ (a sphere surrounding a monopole, a torus threaded by flux), the flux $\int_\Sigma F$ is a curvature integral in disguise, and the theorem forces it to be quantised. The non-obvious step is recognising that the electromagnetic potential, defined only locally away from the monopole, is precisely a connection whose transition functions carry a winding number. *Example problem:* show that the Dirac monopole of charge $g$ lives on the line bundle of degree $2g$ over the sphere enclosing it, so $2g\in\mathbb Z$.

The third disguised source is **an oriented rank-two real vector bundle over a surface, or the tangent bundle of a surface**. An oriented Euclidean plane bundle carries a canonical complex structure — rotation by $+90^\circ$ — turning it into a Hermitian line bundle, and a metric connection becomes a unitary connection. The non-obvious bridge is this identification $SO(2)\cong U(1)$, after which the Euler number of the plane bundle becomes the degree of a line bundle and part (b) applies. *Example problem:* compute $\int_{S^2}\tfrac{i}{2\pi}F$ for $TS^2$ with its Levi-Civita connection, obtaining $2$, and conclude $TS^2$ is non-trivial.

**Targets (Output Amplification).** The bare conclusion is that a curvature integral is an integer computing the degree; combined with other ingredients it does much more.

Combine part (b) with **the classification of line bundles over surfaces**. Chapter III proves that $\deg\colon\operatorname{Pic}(\Sigma)\to\mathbb Z$ is a group isomorphism. Feeding the theorem's identity $\deg L=\int_\Sigma c_1(L)$ into that isomorphism yields the amplified statement that $c_1$ *itself* is a complete isomorphism invariant: line bundles over a closed oriented surface are classified, up to isomorphism, by a single real cohomology class that happens to be integral. The payoff is that a differential-geometric quantity (a curvature integral) decides an isomorphism question, with no homotopy theory needed at the point of use.

Combine part (a) with **the Whitney sum and tensor formulas**. Part (a) identifies the curvature class with the topological class, which is additive under tensor product; together with the block-diagonal structure of curvature under direct sums, this gives the full computation of $c_1$ for any bundle assembled from line bundles — line-bundle-valued cocycles, determinant line bundles $\det E=\Lambda^{\mathrm{rk}E}E$, and the splitting principle that reduces every Chern-class computation to the line-bundle case. The extra ingredient is the tensor-connection curvature formula, and the payoff is the entire calculus of Chern classes reduced to the single number computed here.

Combine part (c) with **a known model curvature**. Whenever one can write down *any* unitary connection whose curvature has non-zero integral over some surface, part (c) certifies non-triviality without further work. The extra ingredient is an explicit connection — the Levi-Civita connection of a round metric, the Hopf connection, a monopole potential — and the payoff is a non-triviality proof that is a one-line integral, replacing an obstruction-theoretic argument by a computation.

---

# Why Is It True

Strip away the two definitions and look at what a curvature integral over a surface is measuring. Over a closed surface $\Sigma$ a line bundle is never globally trivial in an interesting way, but it is *almost* trivial: it is trivial over the surface with one point removed, and trivial over a small disc around that point, because both pieces are contractible enough to carry a nowhere-vanishing section. The bundle is reconstructed from these two trivial pieces by a single gluing instruction along the circle where they overlap — a map $g$ from that circle to $U(1)$. The one and only topological invariant of such a gluing is how many times $g$ winds around the circle group, its winding number.

Now bring in the curvature. On each trivial piece the curvature is $F=dA_j$, the exterior derivative of the local potential in that piece's frame; a line-bundle curvature is *exact on any patch that carries a frame*. So $\int_\Sigma F$ is the integral of a form that is exact on each half. Stokes' theorem converts each half's integral into a boundary integral over the shared circle, and the two boundary integrals do not cancel: they differ by exactly the difference of the two potentials, which is $g^{-1}dg$, the logarithmic derivative of the gluing map. The integral of $g^{-1}dg$ around the circle is, up to the factor $2\pi i$, the winding number. So the failure of the two potentials to agree — the only place any topology can hide — is measured by the curvature integral, and it is an integer because a winding number is an integer.

> **The curvature of a line bundle is $d$ of the potential on each trivialising piece, and Stokes' theorem turns the failure of the potentials to match into the winding number of the transition function.**

That single mechanism drives every part. Part (a) is the same statement read backwards: to identify the curvature class with the homotopy-theoretic class it suffices to check them on the universal example $\mathcal O(-1)$, and there the curvature is computed explicitly upstairs on the sphere via the Hopf connection and pushed down. Part (c) is the mechanism used as an obstruction: a trivial bundle has a *global* frame, hence a global potential, hence $\int_\Sigma F=\int_\Sigma dA=\oint_{\partial\Sigma}A=0$ because a closed surface has no boundary; a non-zero integral therefore forbids a global frame. Part (d) is the mechanism upgraded by holonomy: if the class vanishes the curvature is globally exact, so one can gauge the connection to be flat, and a flat connection over a simply connected base has trivial holonomy, which by the monodromy correspondence means the bundle is trivial.

---

# What Makes This Hard

The subtle point in part (b) is the **orientation bookkeeping at the shared circle**, where two Stokes applications meet with opposite induced orientations; getting the sign wrong turns $\deg L$ into $-\deg L$, and the only reliable check is to pin the sign against the tautological bundle, whose degree is fixed to $-1$ by the complex orientation. The common error is to forget that the outer piece $\Sigma\setminus D^\circ$ induces on the circle the orientation opposite to the disc's, so that the two boundary integrals add rather than cancel. In part (d) the trap is that vanishing of the *class* $c_1(L)=0$ only gives exactness of $\tfrac{i}{2\pi}F_A$, not flatness of $A$ itself; one must first modify the connection to a genuinely flat one, and only then may the monodromy correspondence be invoked. Finally, part (a) is easy to circularise: one must reduce to $\mathcal O(-1)$ using the naturality of *both* classes and check the base case by an honest curvature computation upstairs on the sphere, never by quoting one definition as if it were the other.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Prove agreement (a) by naturality plus one explicit computation on $\mathcal O(-1)$; prove integrality and degree (b) by trivialising over a disc and its complement and applying Stokes twice; deduce the obstruction (c) from the vanishing of the integral on a trivial bundle; and prove injectivity (d) by gauging a null-cohomologous connection to a flat one and invoking the monodromy correspondence over a simply connected base.

**Subgoal decomposition:**

1. **Pullbacks detect forms.** Show that for a surjective submersion $\pi$, the pullback $\pi^*$ is injective on differential forms, so a form identity on the base may be verified upstairs.
   - *Hint:* use that $d\pi_p$ is surjective at every point to lift tangent vectors.
   - *Why needed:* the curvature of $\mathcal O(-1)$ is only known upstairs on the sphere, so the identity $\tfrac{i}{2\pi}F=-\omega_N$ must be checked after pulling back.

2. **The base case $\mathcal O(-1)$.** Compute $\tfrac{i}{2\pi}F=-\omega_N$ on $\mathbb{CP}^N$ from the Hopf curvature $\pi^*F=2i\sum dx_j\wedge dy_j$ and the normalisation $\pi^*\omega_N=\tfrac1\pi\sum dx_j\wedge dy_j$.
   - *Hint:* $\tfrac{i}{2\pi}\cdot2i=-\tfrac1\pi$; then use subgoal 1.
   - *Why needed:* it is the only computation in part (a); everything else is naturality.

3. **Naturality reduction for (a).** Write $L=f^*\mathcal O(-1)$ and use naturality of $c_1$ and of $c_1^{\mathrm{top}}$ to reduce agreement to the base case.
   - *Hint:* both classes commute with $f^*$; they agree on $\mathcal O(-1)$ by subgoal 2 and the definition of $c_1^{\mathrm{top}}$.
   - *Why needed:* it is the whole of part (a) once the base case is known.

4. **Two-Stokes degree formula.** For $L$ over a closed oriented surface, trivialise over a disc $D$ and its complement $\Sigma_0=\Sigma\setminus D^\circ$, write $F=dA_2$ and $F=dA_1$ on the pieces, and apply Stokes to each with the correct induced orientations to obtain $\tfrac{i}{2\pi}\int_\Sigma F=w(g)$.
   - *Hint:* $\partial\Sigma_0=-\partial D$; the difference of potentials on the overlap is $g^{-1}dg$.
   - *Why needed:* it is the computational heart of parts (b) and (c).

5. **Integer and degree.** Conclude integrality from $w(g)\in\mathbb Z$ and identify $w(g)$ with the chapter-III clutching degree by matching conventions on $\mathcal O(-1)$; extend to $h\colon\Sigma\to M$ by pullback.
   - *Hint:* apply subgoal 4 to $h^*L$.
   - *Why needed:* completes part (b).

6. **Obstruction.** A trivial bundle has a global potential, so its curvature integral over a closed surface vanishes; contrapose.
   - *Hint:* $\int_\Sigma dA=\oint_{\partial\Sigma}A=0$ since $\partial\Sigma=\varnothing$.
   - *Why needed:* part (c).

7. **Gauge to flat, then monodromy.** If $c_1(L)=0$ write $\tfrac{i}{2\pi}F_A=d\eta$, shift $A$ by $2\pi i\eta$ to a flat unitary connection, and use the monodromy correspondence over a simply connected base to conclude triviality; deduce injectivity from tensor additivity of $c_1$.
   - *Hint:* the shifted curvature is $F_A+2\pi i\,d\eta=0$; a flat bundle over a simply connected base is trivial.
   - *Why needed:* part (d).

---

# Lemma Decomposition

> [!note]- Lemma 1: Pullback along a surjective submersion is injective on forms
> **Statement:** Let $\pi\colon P\to M$ be a surjective submersion of smooth manifolds and $\alpha\in\Omega^k(M)$. If $\pi^*\alpha=0$ then $\alpha=0$.
>
> **Hint:** At each point of $P$ the differential $d\pi$ is surjective, so any tuple of tangent vectors on $M$ lifts.
>
> **Why needed:** The curvature of $\mathcal O(-1)$ is computed on the total space $S^{2N+1}$ of the Hopf bundle; to read off the identity $\tfrac{i}{2\pi}F=-\omega_N$ downstairs on $\mathbb{CP}^N$ we must know that a form identity is determined by its pullback.
>
> > [!note]- Full proof
> > Fix a point $x\in M$ and tangent vectors $v_1,\dots,v_k\in T_xM$. We show $\alpha_x(v_1,\dots,v_k)=0$; since $x$ and the $v_i$ are arbitrary this gives $\alpha=0$.
> >
> > **Choose a point upstairs.** Because $\pi$ is surjective, there is $p\in P$ with $\pi(p)=x$. Because $\pi$ is a submersion, the differential $d\pi_p\colon T_pP\to T_xM$ is surjective, so for each $i$ we may choose $\tilde v_i\in T_pP$ with $d\pi_p(\tilde v_i)=v_i$.
> >
> > **Evaluate the pullback.** By the definition of the pullback of a differential form,
> > $$(\pi^*\alpha)_p(\tilde v_1,\dots,\tilde v_k)=\alpha_{\pi(p)}\big(d\pi_p(\tilde v_1),\dots,d\pi_p(\tilde v_k)\big)=\alpha_x(v_1,\dots,v_k)\qquad\text{(definition of }\pi^*\text{; }d\pi_p(\tilde v_i)=v_i\text{)}.$$
> > By hypothesis $\pi^*\alpha=0$, so the left-hand side is $0$, whence $\alpha_x(v_1,\dots,v_k)=0$.
> >
> > **Conclusion.** As $x\in M$ and $v_1,\dots,v_k\in T_xM$ were arbitrary, $\alpha=0$. $\blacksquare$

> [!note]- Lemma 2: The curvature identity for the tautological bundle
> **Statement:** Let $\mathcal O(-1)\to\mathbb{CP}^N$ carry the connection induced by the Hopf connection, with curvature $F$. Then $\tfrac{i}{2\pi}F=-\omega_N$ as $2$-forms on $\mathbb{CP}^N$, and consequently $\int_{\mathbb{CP}^1}\tfrac{i}{2\pi}F=-1$.
>
> **Hint:** Pull back to $S^{2N+1}$, where $\pi^*F=2i\sum_{j}dx_j\wedge dy_j$ and $\pi^*\omega_N=\tfrac1\pi\sum_j dx_j\wedge dy_j$; then use Lemma 1.
>
> **Why needed:** This is the single explicit computation underlying part (a); once it is in hand, part (a) follows from naturality.
>
> > [!note]- Full proof
> > **Record the two upstairs formulas.** The induced connection on $\mathcal O(-1)$ is the projection of the trivial connection onto the tautological line, and its curvature $F$ satisfies, by [[Ex - Curvature of the Standard Hopf Connection|the Hopf curvature computation]] and [[Thm - The Standard Connection on the Hopf Bundle|the standard connection on the Hopf bundle]],
> > $$\pi^*F=2i\sum_{j=0}^{N}dx_j\wedge dy_j\Big|_{S^{2N+1}}\qquad(z_j=x_j+iy_j),$$
> > where $\pi\colon S^{2N+1}\to\mathbb{CP}^N$ is the Hopf projection. By [[Thm - The de Rham Cohomology of Complex Projective Space|the de Rham cohomology of complex projective space]], the Fubini–Study generator $\omega_N$ is the unique closed $2$-form with
> > $$\pi^*\omega_N=\tfrac1\pi\sum_{j=0}^N dx_j\wedge dy_j\Big|_{S^{2N+1}},\qquad\int_{\mathbb{CP}^1}\omega_1=1.$$
> >
> > **Compare the pullbacks.** Multiplying the first display by $\tfrac{i}{2\pi}$,
> > $$\pi^*\Big(\tfrac{i}{2\pi}F\Big)=\tfrac{i}{2\pi}\,\pi^*F=\tfrac{i}{2\pi}\cdot2i\sum_{j}dx_j\wedge dy_j=\tfrac{2i^2}{2\pi}\sum_j dx_j\wedge dy_j=-\tfrac1\pi\sum_j dx_j\wedge dy_j\qquad\text{(}i^2=-1\text{)},$$
> > and this equals $-\pi^*\omega_N=\pi^*(-\omega_N)$ (by the second display and linearity of $\pi^*$). Hence $\pi^*\big(\tfrac{i}{2\pi}F+\omega_N\big)=0$.
> >
> > **Descend by injectivity.** The Hopf projection $\pi\colon S^{2N+1}\to\mathbb{CP}^N$ is a surjective submersion, so by Lemma 1 the form $\tfrac{i}{2\pi}F+\omega_N$ vanishes; that is, $\tfrac{i}{2\pi}F=-\omega_N$ on $\mathbb{CP}^N$.
> >
> > **Compute the integral.** Restricting to the standard $\mathbb{CP}^1\subset\mathbb{CP}^N$ (on which the induced generator is $\omega_1$, by the compatibility $\iota^*\omega_N=\omega_1$ of the projective-space theorem),
> > $$\int_{\mathbb{CP}^1}\tfrac{i}{2\pi}F=\int_{\mathbb{CP}^1}(-\omega_1)=-\int_{\mathbb{CP}^1}\omega_1=-1\qquad\text{(by }\int_{\mathbb{CP}^1}\omega_1=1\text{)}.$$
> > $\blacksquare$

> [!note]- Lemma 3: The two-Stokes degree formula
> **Statement:** Let $L\to\Sigma$ be a Hermitian line bundle with unitary connection over a closed connected oriented surface, curvature $F_A\in\Omega^2(\Sigma;i\mathbb R)$. Choose a closed disc $D\subset\Sigma$ (oriented as a subset of $\Sigma$) so small that $L$ is trivial over $D$ and admits a nowhere-vanishing section $s_1$ over the complement $\Sigma_0:=\Sigma\setminus D^\circ$, let $s_2$ be a trivialising section over $D$, and let $g\colon\partial D\to U(1)$ be the transition function defined on the overlap by $s_1=s_2\cdot g$. Then
> $$\tfrac{i}{2\pi}\int_\Sigma F_A=w(g)\in\mathbb Z.$$
>
> **Hint:** Write $F_A=dA_j$ in each frame; the outer piece $\Sigma_0$ induces on $\partial D$ the orientation opposite to the disc's, so the two boundary integrals add.
>
> **Why needed:** It is the computational core of parts (b) and (c): it produces the integer, identifies it as a winding number, and does so with the correct sign.
>
> > [!note]- Full proof
> > **Step 0 — the trivialising data exist.** Since $\Sigma$ is a closed surface, a Hermitian line bundle over it admits, over the complement of a single point, a nowhere-vanishing section: an oriented rank-two real bundle over a surface has a generic section with finitely many zeros, which can be gathered into a single coordinate disc $D$ by the homogeneity lemma, as proved in [[Thm - Classification of Principal U(1)-Bundles by the First Chern Class|the classification of principal U(1)-bundles]]. Over $\Sigma_0$ the normalised section $s_1:=s/|s|$ is a unit-length nowhere-vanishing section, hence a unitary frame. Over the disc $D$, which is contractible, the bundle $L$ is trivial — a Hermitian line bundle over a contractible base admits a global unit section — so a unitary frame $s_2$ exists there as well. On the annular overlap (a collar of $\partial D$) both frames are defined and, being unit sections of a line, differ by a phase: $s_1=s_2\cdot g$ with a smooth $g\colon\partial D\to U(1)$.
> >
> > **Step 1 — the potential difference is $g^{-1}dg$.** Let $A_1,A_2\in\Omega^1(\,\cdot\,;i\mathbb R)$ be the connection potentials in the frames $s_1,s_2$, so $\nabla s_j=s_j\otimes A_j$. On the overlap, using $s_1=s_2 g$ and the Leibniz rule,
> > $$\nabla s_1=\nabla(s_2\,g)=(\nabla s_2)\,g+s_2\,dg=s_2\,A_2\,g+s_2\,dg=s_2\big(A_2 g+dg\big)\qquad\text{(Leibniz rule; }\nabla s_2=s_2 A_2\text{)}.$$
> > Rewriting the right-hand side through $s_2=s_1 g^{-1}$ and using that $U(1)$ is abelian (scalars commute),
> > $$\nabla s_1=s_1\,g^{-1}\big(A_2 g+dg\big)=s_1\big(A_2+g^{-1}dg\big)\qquad\text{(}g^{-1}A_2 g=A_2\text{ since scalar)}.$$
> > Comparing with $\nabla s_1=s_1 A_1$ gives
> > $$A_1=A_2+g^{-1}dg,\qquad\text{that is}\qquad A_2-A_1=-\,g^{-1}dg.$$
> >
> > **Step 2 — curvature is exact on each frame.** Because $U(1)$ is abelian, the structure equation for the curvature reduces to $F_A=dA_j+\tfrac12[A_j\wedge A_j]=dA_j$ in each frame ($\tfrac12[A_j\wedge A_j]=0$ for $\mathfrak u(1)$-valued forms, the bracket on the abelian $i\mathbb R$ vanishing identically). Thus $F_A=dA_1$ on $\Sigma_0$ and $F_A=dA_2$ on $D$.
> >
> > **Step 3 — split the integral and apply Stokes on each piece.** Since $\Sigma=\Sigma_0\cup D$ with $\Sigma_0\cap D=\partial D$ of measure zero,
> > $$\int_\Sigma F_A=\int_{\Sigma_0}F_A+\int_D F_A=\int_{\Sigma_0}dA_1+\int_D dA_2.$$
> > By [[Thm - Stokes' Theorem on Manifolds|Stokes' theorem]], for a compact oriented manifold-with-boundary $W$ and $\beta\in\Omega^{\dim W-1}(W)$ one has $\int_W d\beta=\int_{\partial W}\beta$ with $\partial W$ carrying the induced (outward-normal-first) orientation. The disc $D$ induces on $\partial D$ its standard boundary orientation, while the complementary piece $\Sigma_0$ induces the *opposite* orientation, because the outward normal of $\Sigma_0$ along the shared circle points into $D$: as oriented $1$-manifolds, $\partial\Sigma_0=-\partial D$. Therefore
> > $$\int_{\Sigma_0}dA_1=\int_{\partial\Sigma_0}A_1=\int_{-\partial D}A_1=-\oint_{\partial D}A_1,\qquad\int_D dA_2=\oint_{\partial D}A_2\qquad\text{(Stokes on each piece; }\partial\Sigma_0=-\partial D\text{)}.$$
> >
> > **Step 4 — assemble and identify the winding number.** Adding the two boundary integrals and inserting Step 1,
> > $$\int_\Sigma F_A=\oint_{\partial D}A_2-\oint_{\partial D}A_1=\oint_{\partial D}(A_2-A_1)=-\oint_{\partial D}g^{-1}dg\qquad\text{(by }A_2-A_1=-g^{-1}dg\text{)}.$$
> > By [[Thm - Winding Number of a Map from the Circle to U(1)|the winding-number theorem]], for $g\colon\partial D\to U(1)$ (with $\partial D$ its standard boundary orientation, a circle) the winding number is $w(g)=\tfrac{1}{2\pi i}\oint_{\partial D}g^{-1}dg\in\mathbb Z$, so $\oint_{\partial D}g^{-1}dg=2\pi i\,w(g)$. Hence
> > $$\tfrac{i}{2\pi}\int_\Sigma F_A=\tfrac{i}{2\pi}\Big(-\oint_{\partial D}g^{-1}dg\Big)=-\tfrac{i}{2\pi}\cdot2\pi i\,w(g)=-i^2\,w(g)=w(g)\qquad\text{(}i^2=-1\text{)}.$$
> > Since $w(g)\in\mathbb Z$, the left-hand side is an integer.
> >
> > **Conclusion.** $\tfrac{i}{2\pi}\int_\Sigma F_A=w(g)\in\mathbb Z$. $\blacksquare$

> [!note]- Lemma 4: The Chern–Weil first Chern class is additive under tensor product
> **Statement:** For Hermitian line bundles $L_1,L_2\to M$, $c_1(L_1\otimes L_2)=c_1(L_1)+c_1(L_2)$ in $H^2_{dR}(M)$, and $c_1(L^\vee)=-c_1(L)$; thus $c_1\colon\operatorname{Pic}(M)\to H^2_{dR}(M)$ is a group homomorphism.
>
> **Hint:** The tensor product of two unitary connections has, in a product frame, potential $A_1+A_2$; take curvatures.
>
> **Why needed:** Part (d) upgrades "$c_1(L)=0\Rightarrow L$ trivial" to injectivity of $c_1$, which requires $c_1$ to be a homomorphism.
>
> > [!note]- Full proof
> > **Construct the tensor connection.** Let $\nabla^1,\nabla^2$ be unitary connections on $L_1,L_2$. Define $\nabla$ on $L_1\otimes L_2$ by the Leibniz rule $\nabla(s_1\otimes s_2)=(\nabla^1 s_1)\otimes s_2+s_1\otimes(\nabla^2 s_2)$; this is a connection, and it is unitary for the tensor Hermitian structure $\langle s_1\otimes s_2,t_1\otimes t_2\rangle=\langle s_1,t_1\rangle\langle s_2,t_2\rangle$ (both factors preserve their metrics, so the product rule preserves the product metric). Choose local unit frames $s_1,s_2$ with $\nabla^j s_j=s_j\otimes A_j$, $A_j\in\Omega^1(U;i\mathbb R)$. Then $s_1\otimes s_2$ is a local unit frame of $L_1\otimes L_2$ and
> > $$\nabla(s_1\otimes s_2)=(s_1 A_1)\otimes s_2+s_1\otimes(s_2 A_2)=(s_1\otimes s_2)\,(A_1+A_2)\qquad\text{(scalars }A_j\text{ commute past the tensor factors)},$$
> > so the tensor connection has potential $A_1+A_2$.
> >
> > **Take curvatures.** By Step 2 of Lemma 3 (abelian structure group), the curvature in a unit frame is the exterior derivative of the potential, so
> > $$F_{L_1\otimes L_2}=d(A_1+A_2)=dA_1+dA_2=F_{L_1}+F_{L_2}\qquad\text{(linearity of }d\text{)}.$$
> > Multiplying by $\tfrac{i}{2\pi}$ and passing to cohomology classes,
> > $$c_1(L_1\otimes L_2)=\Big[\tfrac{i}{2\pi}(F_{L_1}+F_{L_2})\Big]=\Big[\tfrac{i}{2\pi}F_{L_1}\Big]+\Big[\tfrac{i}{2\pi}F_{L_2}\Big]=c_1(L_1)+c_1(L_2).$$
> >
> > **The dual.** The dual bundle $L^\vee$ carries the dual connection, whose potential in the dual frame is $-A$ (from $d\langle s,s^\vee\rangle=0$ for the pairing of a frame with its dual), so $F_{L^\vee}=d(-A)=-F_L$ and $c_1(L^\vee)=-c_1(L)$. Since $L\otimes L^\vee\cong\underline{\mathbb C}$ is trivial with $c_1(\underline{\mathbb C})=0$, this is consistent: $c_1$ sends the group $\operatorname{Pic}(M)$ (tensor product, dual as inverse, trivial bundle as identity) to $H^2_{dR}(M)$ preserving the operations. $\blacksquare$

> [!note]- Lemma 5: A null-cohomologous curvature can be gauged flat
> **Statement:** Let $L\to M$ be a Hermitian line bundle with unitary connection $A$. If $c_1(L)=\big[\tfrac{i}{2\pi}F_A\big]=0$, then there is a real $1$-form $\eta\in\Omega^1(M;\mathbb R)$ with $\tfrac{i}{2\pi}F_A=d\eta$, and the shifted connection $A':=A+2\pi i\,\eta$ is a unitary connection on $L$ with $F_{A'}=0$; that is, $A'$ is flat.
>
> **Hint:** The shift by an imaginary-valued global $1$-form keeps the connection unitary; its curvature changes by $d$ of the shift.
>
> **Why needed:** Part (d) needs a genuinely flat connection before the monodromy correspondence can be applied; vanishing of the class only gives exactness of the curvature form.
>
> > [!note]- Full proof
> > **Extract the primitive.** By hypothesis the class $\big[\tfrac{i}{2\pi}F_A\big]\in H^2_{dR}(M)$ is zero, which by the definition of exactness in de Rham cohomology means the closed real $2$-form $\tfrac{i}{2\pi}F_A$ is exact: there exists $\eta\in\Omega^1(M;\mathbb R)$ with
> > $$\tfrac{i}{2\pi}F_A=d\eta,\qquad\text{equivalently}\qquad F_A=\tfrac{2\pi}{i}\,d\eta=-2\pi i\,d\eta\qquad\big(\tfrac1i=-i\big).$$
> >
> > **Shift the connection unitarily.** The endomorphism bundle of a line bundle is canonically trivial, $\operatorname{End}(L)=\underline{\mathbb C}$, and the skew-Hermitian endomorphisms are the imaginary scalars $i\mathbb R$; hence for any global $\alpha\in\Omega^1(M;i\mathbb R)$ the affine shift $A\mapsto A+\alpha$ produces another *unitary* connection $A'$ on $L$ (it differs from $A$ by a skew-Hermitian-valued form, so it still satisfies the metric-compatibility identity). Take $\alpha:=2\pi i\,\eta$, which is imaginary-valued because $\eta$ is real, and set $A':=A+2\pi i\,\eta$.
> >
> > **Compute the shifted curvature.** By Step 2 of Lemma 3 the curvature of a unitary line-bundle connection is $d$ of its potential, so shifting the potential by a *global* $1$-form $\alpha$ shifts the curvature by $d\alpha$:
> > $$F_{A'}=d(A+2\pi i\,\eta)=dA+2\pi i\,d\eta=F_A+2\pi i\,d\eta\qquad\text{(linearity of }d\text{; }F_A=dA\text{)}.$$
> > Inserting $d\eta=\tfrac{i}{2\pi}F_A$ from the first step,
> > $$F_{A'}=F_A+2\pi i\cdot\tfrac{i}{2\pi}F_A=F_A+i^2 F_A=F_A-F_A=0\qquad\text{(}i^2=-1\text{)}.$$
> >
> > **Conclusion.** $A'$ is a unitary connection on $L$ with $F_{A'}=0$, hence flat. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Throughout, $c_1(L)=\big[\tfrac{i}{2\pi}F_A\big]$ is independent of the unitary connection $A$ by the [[Thm - Chern-Weil Theorem|Chern–Weil theorem]] and independent of the Hermitian structure by [[Def - Chern Classes|the construction of the Chern classes]], so we are free to choose whichever connection is convenient in each part.
>
> **Part (a) — agreement with the topological class.**
>
> **Step 0 — the base case.** By Lemma 2, the tautological bundle $\mathcal O(-1)\to\mathbb{CP}^N$ with the connection induced by the Hopf connection has curvature satisfying $\tfrac{i}{2\pi}F=-\omega_N$ as forms, so
> $$c_1(\mathcal O(-1))=\big[\tfrac{i}{2\pi}F\big]=[-\omega_N]=-[\omega_N].$$
> On the other hand, by [[Def - First Chern Class via the Classifying Map|the definition of the topological first Chern class]] (whose classifying map for $\mathcal O(-1)$ is the identity of $\mathbb{CP}^N$), $c_1^{\mathrm{top}}(\mathcal O(-1))=-[\omega_N]$. Hence the two classes agree on $\mathcal O(-1)$:
> $$c_1(\mathcal O(-1))=c_1^{\mathrm{top}}(\mathcal O(-1))=-[\omega_N].$$
>
> **Step 1 — reduce a general bundle to the base case.** Let $L\to M$ be any Hermitian line bundle over a compact manifold. By [[Thm - Line Bundles over Compact Manifolds are Pulled Back from Projective Space|the classifying-map theorem]], there is $N<\infty$ and a smooth map $f\colon M\to\mathbb{CP}^N$ with $L\cong f^*\mathcal O(-1)$. We may choose on $L$ the pulled-back connection $f^*\nabla$; its curvature is $f^*F$.
>
> **Step 2 — apply naturality of both classes.** By [[Thm - Naturality and Isomorphism Invariance of Characteristic Classes|naturality of the Chern–Weil classes]], $c_1(f^*\mathcal O(-1))=f^*c_1(\mathcal O(-1))$. By [[Thm - Classification of Principal U(1)-Bundles by the First Chern Class|the classification theorem, part (B)]], the topological class is natural too: $c_1^{\mathrm{top}}(f^*\mathcal O(-1))=f^*c_1^{\mathrm{top}}(\mathcal O(-1))$. Combining these with Step 0,
> $$c_1(L)=f^*c_1(\mathcal O(-1))=f^*\big(-[\omega_N]\big)=f^*c_1^{\mathrm{top}}(\mathcal O(-1))=c_1^{\mathrm{top}}(L).$$
> This proves the agreement $c_1(L)=c_1^{\mathrm{top}}(L)$; the displayed curvature identity and integral for $\mathcal O(-1)$ are Lemma 2. Part (a) is complete.
>
> **Part (b) — integrality and degree.**
>
> **Step 0 — the case $M=\Sigma$.** Let $L\to\Sigma$ be a Hermitian line bundle over a closed connected oriented surface, with unitary connection $A$. By Lemma 3, choosing a disc $D\subset\Sigma$ and trivialising sections $s_1$ over $\Sigma_0=\Sigma\setminus D^\circ$ and $s_2$ over $D$ with transition $g\colon\partial D\to U(1)$ ($s_1=s_2 g$),
> $$\tfrac{i}{2\pi}\int_\Sigma F_A=w(g)\in\mathbb Z.$$
>
> **Step 1 — identify the integer with the degree.** The frames $s_1$ over $\Sigma_0$ and $s_2$ over $D$ constructed in Lemma 3, with $s_1=s_2 g$ on $\partial D$, exhibit $g\colon\partial D\to U(1)$ as a clutching function of $L$ in the sense of chapter III. By [[Def - First Chern Class via the Classifying Map|the definition of the degree]] and [[Thm - Classification of Principal U(1)-Bundles by the First Chern Class|the classification theorem, part (C)]] — under which $\deg L=w(g)$ is well defined, independent of the choice of clutching data — the degree is the winding number of any such clutching function, provided the boundary orientation of $\partial D$ and the ordering of the two pieces are those chapter III fixes. Lemma 3 uses precisely those conventions (the disc $D$ carries its standard boundary orientation and $s_1=s_2 g$ with $s_2$ the inner frame), and the resulting sign is confirmed on the tautological bundle: for $\mathcal O(-1)\to\mathbb{CP}^1$ the classification page fixes $\deg\mathcal O(-1)=-1$, while Lemma 2 with Step 0 gives $\tfrac{i}{2\pi}\int_{\mathbb{CP}^1}F=w(g)=-1$, so no sign discrepancy is introduced. Because this matching of conventions depends only on the orientation rules and not on the surface, $w(g)=\deg L$ for the clutching function of every line bundle over every closed connected oriented surface. Therefore
> $$\tfrac{i}{2\pi}\int_\Sigma F_A=w(g)=\deg L.$$
>
> **Step 2 — the general map $h\colon\Sigma\to M$.** For a smooth $h\colon\Sigma\to M$, the pullback $h^*L\to\Sigma$ is a Hermitian line bundle over a closed oriented surface with unitary connection $h^*A$ whose curvature is $h^*F_A$ (pullback commutes with the exterior derivative and with the connection, by [[Thm - Naturality and Isomorphism Invariance of Characteristic Classes|naturality]]). Applying Steps 0–1 to $h^*L$,
> $$\tfrac{i}{2\pi}\int_\Sigma h^*F_A=\deg(h^*L)\in\mathbb Z.$$
>
> **Step 3 — completeness of $c_1$ over a surface.** Take $M=\Sigma$ and $h=\operatorname{id}$. By [[Thm - The Top de Rham Cohomology of a Closed Connected Oriented Manifold is R|the top-cohomology theorem]], integration $\int_\Sigma\colon H^2_{dR}(\Sigma)\to\mathbb R$ is a well-defined isomorphism, so $\int_\Sigma c_1(L)$ depends only on the class $c_1(L)$ and equals $\tfrac{i}{2\pi}\int_\Sigma F_A=\deg L$. Thus the composite
> $$\operatorname{Pic}(\Sigma)\xrightarrow{\ c_1\ }H^2_{dR}(\Sigma)\xrightarrow{\ \int_\Sigma\ }\mathbb R$$
> is exactly the degree map $L\mapsto\deg L$, which by [[Thm - Classification of Principal U(1)-Bundles by the First Chern Class|the classification theorem, part (C)]] is a group isomorphism onto $\mathbb Z\subset\mathbb R$. Since $\int_\Sigma$ is injective and the composite $\int_\Sigma\circ\,c_1$ is injective, $c_1$ is injective on $\operatorname{Pic}(\Sigma)$: equal first Chern class forces the two bundles isomorphic. The converse direction — isomorphic bundles have equal first Chern class — is the isomorphism invariance of the Chern–Weil class ([[Thm - Naturality and Isomorphism Invariance of Characteristic Classes|naturality, part (c)]], which makes $c_1$ a well-defined function on $\operatorname{Pic}(\Sigma)$ in the first place). Hence two line bundles over a closed connected oriented surface are isomorphic if and only if they have equal first Chern class. Part (b) is complete.
>
> **Part (c) — non-triviality obstruction.**
>
> **Step 0 — a trivial bundle has vanishing class.** Suppose first, for the contrapositive, that $L$ is trivial. Then $L$ admits the product connection, which is flat, so $c_1(L)=\big[\tfrac{i}{2\pi}\cdot0\big]=0$; equivalently, by [[Thm - Trivial Bundles Have Vanishing Characteristic Classes|the vanishing theorem for trivial bundles]], every characteristic class of a trivial bundle in positive degree is zero. Contraposing: if $c_1(L)\ne0$ then $L$ is non-trivial.
>
> **Step 1 — the concrete surface criterion.** Suppose there is a smooth $h\colon\Sigma\to M$ with $\int_\Sigma h^*F_A\ne0$. If $L$ were trivial then $h^*L$ would be trivial, hence would admit a global unit section $s$ and a global potential $A_0$ with $h^*F_A=dA_0$, and by [[Thm - Stokes' Theorem on Manifolds|Stokes' theorem]] on the boundaryless $\Sigma$,
> $$\int_\Sigma h^*F_A=\int_\Sigma dA_0=\int_{\partial\Sigma}A_0=0\qquad\text{(}\partial\Sigma=\varnothing\text{)},$$
> contradicting $\int_\Sigma h^*F_A\ne0$. Therefore $L$ is non-trivial. (Taking $h=\operatorname{id}$ when $M=\Sigma$ gives the stated special case.) Part (c) is complete.
>
> **Part (d) — injectivity over a simply connected base.**
>
> **Step 0 — gauge to a flat connection.** Assume $M$ is connected and simply connected and $c_1(L)=0$. By Lemma 5 there is a real $1$-form $\eta$ with $\tfrac{i}{2\pi}F_A=d\eta$, and the shifted unitary connection $A':=A+2\pi i\,\eta$ satisfies $F_{A'}=0$, that is, $A'$ is flat.
>
> **Step 1 — read off the monodromy.** By [[Thm - Flat Connections and Monodromy Representations of the Fundamental Group|the flat-connection/monodromy correspondence]], a flat unitary connection on $L$ over the connected base $M$ determines a monodromy (holonomy) representation $\rho\colon\pi_1(M,x_0)\to U(1)$, and the flat bundle $(L,A')$ is isomorphic, as a bundle with flat connection, to the associated flat bundle $\widetilde M\times_\rho\mathbb C$ built from $\rho$ over the universal cover.
>
> **Step 2 — triviality over a simply connected base.** Since $M$ is simply connected, $\pi_1(M,x_0)=\{1\}$, so the only representation $\rho$ is trivial, and the associated flat bundle is the trivial bundle $\underline{\mathbb C}=M\times\mathbb C$ with the product connection. Hence $(L,A')\cong(\underline{\mathbb C},d)$ as bundles with connection; in particular $L\cong\underline{\mathbb C}$ is trivial.
>
> **Step 3 — conclude injectivity.** By Lemma 4, $c_1\colon\operatorname{Pic}(M)\to H^2_{dR}(M)$ is a group homomorphism. Suppose $c_1(L_1)=c_1(L_2)$. Then, using Lemma 4,
> $$c_1(L_1\otimes L_2^\vee)=c_1(L_1)+c_1(L_2^\vee)=c_1(L_1)-c_1(L_2)=0.$$
> By Steps 0–2 applied to $L_1\otimes L_2^\vee$, this bundle is trivial, i.e. $L_1\otimes L_2^\vee\cong\underline{\mathbb C}$; tensoring with $L_2$ gives $L_1\cong L_2$. Hence $c_1$ has trivial kernel and is injective. Part (d) is complete. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Magnetic monopoles and charge quantisation (mathematical physics).** Model a magnetic monopole of charge $g$ at the origin of $\mathbb R^3$ by a $U(1)$ gauge field on the sphere $S^2$ enclosing it; the field strength $F$ is a real closed $2$-form with $\int_{S^2}F=4\pi g$ (Gauss's law for magnetic charge). The field strength is $-i$ times the imaginary-valued line-bundle curvature $F_\nabla$, so $F_\nabla=iF$; applying the integrality of part (b) to the curvature gives $\tfrac{i}{2\pi}\int_{S^2}F_\nabla=\tfrac{i}{2\pi}\int_{S^2}iF=-\tfrac{1}{2\pi}\int_{S^2}F=-2g\in\mathbb Z$, hence $2g\in\mathbb Z$: magnetic charge is quantised in half-integer units. The application is non-obvious because the physical input — a singular field in three-space — must first be recognised as a smooth connection on a non-trivial line bundle over the enclosing sphere, at which point the theorem is a one-line integrality statement.

**Non-triviality of the tangent bundle of the sphere (differential geometry).** Equip $TS^2$ with the complex structure "rotation by $90^\circ$" and the Levi-Civita connection of the round metric; this is a Hermitian line bundle with a unitary connection whose curvature is $F=-iK\,dA$ for the Gaussian curvature $K$ and the area form $dA$ (the sign is fixed by the convention $c_1(TS^2)[S^2]=e(TS^2)[S^2]=2$ of the series). By part (c) it suffices to compute $\int_{S^2}\tfrac{i}{2\pi}F=\tfrac1{2\pi}\int_{S^2}K\,dA=2\ne0$ — the round sphere has $\int_{S^2}K\,dA=4\pi$ by the Gauss–Bonnet theorem — to conclude $TS^2$ is non-trivial, recovering the hairy-ball phenomenon by an integral rather than by a fixed-point argument. The non-obvious step is the identification of an oriented plane bundle with a line bundle, which lets a curvature integral decide a triviality question.

**Line bundles on a Riemann surface and the degree (algebraic geometry).** For a compact Riemann surface $\Sigma$ of genus $\gamma$, the holomorphic line bundles form the Picard group, and part (b) shows the smooth degree $\deg L=\tfrac{i}{2\pi}\int_\Sigma F_A$ agrees with the algebraic degree (number of zeros minus poles of a meromorphic section). Over a surface the degree is a complete *smooth* invariant, so the Picard group's failure to be $\mathbb Z$ — its continuous Jacobian part — is invisible to $c_1$ and lives entirely in the kernel that the theorem's part (d) would detect were $\Sigma$ simply connected (it is not, for $\gamma\ge1$). The application is non-obvious because it locates precisely where the smooth classification and the holomorphic classification diverge: in $\pi_1(\Sigma)$.

---

# Bridges

- **The Chern–Weil theorem and naturality.** This theorem is the first substantive *identification* of a Chern–Weil class with a topological invariant, and it rests entirely on the soft properties established earlier: that $c_1(L)=\big[\tfrac{i}{2\pi}F_A\big]$ is connection-independent ([[Thm - Chern-Weil Theorem|Chern–Weil]]) and functorial ([[Thm - Naturality and Isomorphism Invariance of Characteristic Classes|naturality]]). The bridge is the reduction principle: once a class is natural, it is determined by its value on the universal example $\mathcal O(-1)$, so a single curvature computation on projective space settles the general case.

- **The classification of $U(1)$-bundles over surfaces.** Chapter III proves, by clutching, that $\deg\colon\operatorname{Pic}(\Sigma)\to\mathbb Z$ is an isomorphism; this theorem's part (b) supplies the differential-geometric formula $\deg L=\int_\Sigma c_1(L)$ for that isomorphism. Together they say that over a closed oriented surface the topological classification (clutching functions up to homotopy), the homotopy classification (maps to $\mathbb{CP}^\infty$), and the differential classification (curvature integrals) are one and the same integer.

- **The Euler class of an oriented plane bundle.** For an oriented rank-two real bundle $E\to\Sigma$, the identification $SO(2)\cong U(1)$ makes $E$ a Hermitian line bundle, and the Euler class becomes the first Chern class, $e(E)=c_1(E)$, so this theorem computes the Euler number as a curvature integral. Specialised to $E=T\Sigma$ this is the differential-geometric half of the Gauss–Bonnet theorem: $\int_\Sigma e(T\Sigma)$ is a curvature integral that equals an integer, the Euler characteristic. The series proves the identity only for $S^2$; the general Gauss–Bonnet statement is recorded as a bridge to Riemannian geometry.

- **Dirac quantisation and the Chern–Simons functional (chapter VII).** The integrality of part (b) is exactly the statement that abelian magnetic flux is quantised, and it is the seed of the higher-degree integrality results: the second Chern number of an $SU(2)$-bundle over a closed four-manifold is an integer by the same clutching-plus-Stokes mechanism applied to the Chern–Simons transgression form, and the gauge variation of the Chern–Simons functional is quantised for the same reason. This theorem is the one-dimensional-lower model in which the whole argument is visible.

---

# Unlocked by This

> [!tip] Dirac charge quantisation *(from mathematical physics)*
> Part (b) is the mathematical content of Dirac's argument that the existence of a single magnetic monopole forces electric charge to be quantised: the monopole bundle over the enclosing sphere has an integer degree, and that integer is the product of electric and magnetic charges in natural units. See chapter VII.

> [!tip] The Picard group of a simply connected four-manifold *(from four-manifold topology)*
> Part (d) shows that over a simply connected base $c_1$ injects $\operatorname{Pic}(M)$ into $H^2_{dR}(M)$. For the simply connected four-manifolds of chapters XI and XIII, where line bundles are detected exactly by their first Chern class, this is what makes $c_1$ the correct label on the $\operatorname{Spin}^c$ structures and reducible Seiberg–Witten solutions. See **Gauge Theory XI — Seiberg–Witten Theory**.
