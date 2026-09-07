---
type: theorem
subject: gauge-theory
prereqs:
  - "Thm - Classification of Principal SU(2)-Bundles over Four-Manifolds"
  - "Thm - Transgression Formula and the Chern-Simons Form"
  - "Thm - Gauge Transformations Act on Connections and Curvature"
  - "Thm - Stokes' Theorem on Manifolds"
  - "Def - Chern Classes"
  - "Ex - The Coefficients of the Characteristic Polynomial are Ad-Invariant"
tags: [geometry, gauge-theory]
---

# Notation

$G$ acts on the **right** on principal bundles; $SU(2)$ is identified with the unit quaternions and with $S^3$, oriented as $\partial B^4$ with $\mathbb R^4=(1,i,j,k)$, and $X$ carries a fixed orientation, all as fixed on [[Def - The Hopf Bundle#Sign ledger]]. For a principal $SU(2)$-bundle $P\to X$ with connection $A$ we write $F_A\in\Omega^2(X;\operatorname{ad}P)$ for its curvature; in a local trivialisation $A$ is an $\mathfrak{su}(2)$-valued one-form and $F_A=dA+A\wedge A$ ([[Def - Curvature of a Principal Connection]]). Here $\mathfrak{su}(2)$ is the traceless skew-Hermitian $2\times2$ matrices and $\operatorname{tr}$ is the trace in the defining representation; on $\mathfrak{su}(2)$ one has $\operatorname{tr}(\xi^2)=-2\det\xi$ ([[Ex - The Coefficients of the Characteristic Polynomial are Ad-Invariant]]). The **Chern–Simons form** of a local connection matrix $A$ is
$$\operatorname{cs}(A):=\operatorname{tr}\Big(A\wedge dA+\tfrac23A\wedge A\wedge A\Big)\in\Omega^3(\text{local }X),$$
and $\theta=g^{-1}dg$ is the pulled-back Maurer–Cartan form of a transition map $g$. We write $D\subset X$ for a closed coordinate disc, $S=\partial D\cong S^3$ oriented as the boundary of $D$, $X_-=X\setminus D^\circ$, and $k(P)$ for the clutching degree of [[Thm - Classification of Principal SU(2)-Bundles over Four-Manifolds]]. The normalisation of Chern classes is $c(E)=\det(1+\tfrac{i}{2\pi}F)$; thus for an $SU(2)$-bundle $c_2(P)=\big[\tfrac1{8\pi^2}\operatorname{tr}(F_A\wedge F_A)\big]$ (derived below). We use $\int_{SU(2)}\operatorname{tr}(\theta^{\wedge3})=-24\pi^2$ from the sign ledger.

> [!warning] Convention: the Haydys and series normalisations of $c_2$
> Haydys (Remark 93, equation (94)) records $c_2(P)=\frac1{8\pi^2}[\operatorname{tr}(F_A\wedge F_A)]$ for $SU(2)$-bundles, using $\operatorname{tr}\xi^2=-2\det\xi$ on $\mathfrak{su}(2)$. This matches the series normalisation $c(E)=\det(1+\tfrac{i}{2\pi}F)$: for a traceless $2\times2$ skew-Hermitian $\xi$, $\det(1+\tfrac{i}{2\pi}\xi)=1-\tfrac1{4\pi^2}\det\xi$, so the degree-$4$ part is $c_2(\xi)=-\tfrac1{4\pi^2}\det\xi=\tfrac1{8\pi^2}\operatorname{tr}(\xi^2)$. The apparent sign discrepancy with the algebraic-topology convention "$-\tfrac1{8\pi^2}$" is the sign of $\operatorname{tr}(\xi^2)\le0$ for skew-Hermitian $\xi$; the series uses $c_2(P)=\tfrac1{8\pi^2}[\operatorname{tr}(F_A\wedge F_A)]$ throughout.

---

# Statement

> **Theorem (second Chern number is the clutching degree).** Let $X$ be a closed connected oriented $4$-manifold and $P\to X$ a principal $SU(2)$-bundle with connection $A$. Then, with the normalisation $\operatorname{tr}(\xi^2)=-2\det\xi$ on $\mathfrak{su}(2)$,
> $$c_2(P)=\Big[\tfrac1{8\pi^2}\operatorname{tr}(F_A\wedge F_A)\Big]\in H^4_{dR}(X),\qquad
> \frac1{8\pi^2}\int_X\operatorname{tr}(F_A\wedge F_A)=k(P)\in\mathbb Z,$$
> where $k(P)$ is the clutching degree (Chern number) of [[Thm - Classification of Principal SU(2)-Bundles over Four-Manifolds]]. In particular the integral is an integer, is independent of the connection $A$, and takes every integer value as $P$ ranges over the principal $SU(2)$-bundles over $X$.

---

# Motivation

Chapter III attached to every principal $SU(2)$-bundle over a closed oriented four-manifold a purely topological integer, the clutching degree $k(P)$, defined by how the bundle is glued across the boundary of a small ball. Chapter VI attaches to every bundle-with-connection an analytic quantity, the curvature integral $\frac1{8\pi^2}\int_X\operatorname{tr}(F_A\wedge F_A)$. This theorem says the two are the same number. That identification is the hinge of gauge theory: it makes a differential-geometric integral compute a topological invariant, and conversely makes a topological invariant control an analytic quantity.

The consequences are immediate and used everywhere downstream. Because the right-hand side is a topological integer, the left-hand side does not depend on the connection — a fact that would be laborious to see directly from the space of connections, obtained here for free. Because the left-hand side is a curvature integral, the topological number bounds the Yang–Mills energy, giving the instanton energy floor $8\pi^2|k|$. And because the definition of the Chern–Simons functional on a three-manifold requires exactly this integrality — the functional is well defined modulo $\mathbb Z$ precisely because $\frac1{8\pi^2}\int\operatorname{tr}(F\wedge F)$ over a closed four-manifold is an integer — this theorem is what makes the three-dimensional theory of chapter VI §6.4 consistent.

The mechanism is worth stating in one line, because the proof is its unfolding.

> **$\operatorname{tr}(F\wedge F)$ is locally exact — it is $d$ of the Chern–Simons form in any trivialisation — and gluing two local primitives across the three-sphere $S=\partial D$ produces the winding number of the clutching map.**

---

# Sources and Targets

**Sources (Input Broadening).** The hypothesis is a principal $SU(2)$-bundle with connection over a closed oriented four-manifold; the disguised inputs are the ways such a datum arises.

The first disguised source is **a rank-two Hermitian bundle with a unitary connection and trivial determinant.** Such an $E$ is an $SU(2)$-bundle, and its curvature $F$ is $\mathfrak{su}(2)$-valued; the theorem then computes $c_2(E)[X]$ as a curvature integral. The bridge is that $c_2(E)=[\frac1{8\pi^2}\operatorname{tr}(F\wedge F)]$ once $c_1(E)=0$. *Example problem:* compute $c_2$ of the positive spinor bundle of a spin four-manifold from a spin connection's curvature.

The second disguised source is **any Yang–Mills field configuration.** A solution, or indeed any connection, of an $SU(2)$ gauge theory on $X$ carries a curvature whose "instanton number" $\frac1{8\pi^2}\int\operatorname{tr}(F\wedge F)$ is the object physicists call the topological charge; the theorem identifies it with the bundle's clutching degree. The non-obvious step is that this seemingly connection-dependent integral is a bundle invariant. *Example problem:* verify that the BPST instanton on $S^4$ has topological charge $1$.

The third disguised source is **a bundle presented by a clutching map $g\colon S^3\to SU(2)$.** Here the topological side $k(P)=\deg g$ is given, and the theorem *predicts* the value of any curvature integral: it must equal $\deg g$. The bridge runs backward, from topology to analysis. *Example problem:* given the clutching bundle $P_{q\mapsto q^2}$, predict $\frac1{8\pi^2}\int_X\operatorname{tr}(F\wedge F)=2$ for every connection.

**Targets (Output Amplification).** The conclusion "curvature integral $=$ clutching integer" combines with other results.

Combine it with **the Cauchy–Schwarz/pointwise inequality of chapter VII.** From $|F|^2\pm\operatorname{tr}(F\wedge F)/\mathrm{vol}\ge0$ one gets $\mathcal{YM}(A)=\frac12\int|F|^2\ge8\pi^2|k(P)|$, with equality iff $F$ is (anti-)self-dual. The extra ingredient is the Hodge-theoretic inequality; the payoff is the instanton energy floor.

Combine it with **Stokes on a four-manifold with boundary.** If $X$ has boundary $M=\partial X$, the same local-exactness argument gives $\frac1{8\pi^2}\int_X\operatorname{tr}(F\wedge F)\equiv\vartheta(A|_M)\pmod{\mathbb Z}$, the boundary Chern–Simons invariant. The extra ingredient is the boundary term; the payoff is the four-dimensional formula for the Chern–Simons functional.

Combine it with **the classification's realisation statement.** Since every integer $k$ occurs as some $k(P)$, every integer occurs as a value of the curvature integral; in particular the moduli problem on the bundle with $k=1$ is non-empty. The extra ingredient is part (C) of the classification; the payoff is the starting bundle of Donaldson theory.

---

# Why Is It True

Forget the formula and picture the two-form $\operatorname{tr}(F\wedge F)$ living on $X$. It is a closed four-form (Bianchi identity), and it is globally defined because $\operatorname{tr}$ is conjugation-invariant, so it does not see the trivialisation. Its integral is therefore a number attached to $(P,A)$. Now the key local fact: in any trivialisation, $\operatorname{tr}(F\wedge F)$ is *exact*, equal to $d\operatorname{cs}(A)$ for the Chern–Simons three-form. So if $P$ were globally trivial the integral would vanish by Stokes. The integral is nonzero exactly to the extent that $P$ fails to be globally trivial — and that failure is concentrated at the clutching sphere.

Cut $X$ into the disc $D$ and its complement $X_-$. On each piece the bundle is trivial and $\operatorname{tr}(F\wedge F)=d\operatorname{cs}(A_i)$, so each piece's integral is a boundary integral over $S=\partial D$. The two pieces induce opposite orientations on $S$, so the total integral is the *difference* $\int_S(\operatorname{cs}(A_2)-\operatorname{cs}(A_1))$ of the two Chern–Simons primitives. But $A_1$ and $A_2$ are two trivialisation-expressions of the *same* connection, related by the gauge transformation $g$ that is the clutching map; the difference $\operatorname{cs}(A_2)-\operatorname{cs}(A_1)$ is therefore the gauge variation of the Chern–Simons form, which is $-\frac13\operatorname{tr}(\theta^{\wedge3})$ up to an exact term that dies over the closed sphere. Integrating, the number is $-\frac13\int_S\operatorname{tr}(\theta^{\wedge3})$, and since $\operatorname{tr}(\theta^{\wedge3})$ is a bi-invariant top-form on $SU(2)=S^3$, this counts the degree of $g$. The constants align to give exactly $8\pi^2\deg g$.

The connection-independence is now automatic: the answer is the topological degree of the clutching map, which knows nothing about $A$. This is the deep point — an analytic integral has been shown to equal a homotopy invariant.

---

# What Makes This Hard

The subtle steps are three. First, one must resist the temptation to apply Stokes globally: $\operatorname{tr}(F\wedge F)=d\operatorname{cs}(A)$ holds only *locally*, in a trivialisation, because $\operatorname{cs}(A)$ is built from the connection matrix $A$, which does not exist globally on a nontrivial bundle. The whole content is that the two local primitives fail to agree, and their disagreement is the answer. Second, the two induced orientations on the gluing sphere are opposite, and dropping that minus sign gives $0$ instead of $2k$. Third, the constant $-\frac13\int_S\operatorname{tr}(\theta^{\wedge3})=+8\pi^2\deg g$ requires the orientation-sensitive value $\int_{SU(2)}\operatorname{tr}(\theta^{\wedge3})=-24\pi^2$; the common error of quoting $+24\pi^2$ flips the sign of the final identity. Under the conventions fixed in the sign ledger the answer is $+k(P)$.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Write the global four-form $\operatorname{tr}(F\wedge F)$; observe it is locally $d\operatorname{cs}(A)$; split $X$ into $X_-$ and $D$; apply Stokes on each with the induced (opposite) boundary orientations; reduce the boundary integral to the gauge variation of $\operatorname{cs}$ across the clutching map; evaluate it with the winding identity of chapter III.

**Subgoal decomposition:**

1. **The four-form is global and locally exact.** $\operatorname{tr}(F\wedge F)$ is well defined on $X$ and equals $d\operatorname{cs}(A_i)$ in each trivialisation.
   - *Hint:* Conjugation-invariance of $\operatorname{tr}$ makes it global; the transgression formula gives local exactness.
   - *Why needed:* It turns the bulk integral into boundary integrals.

2. **Split and apply Stokes.** $\int_X=\int_{X_-}+\int_D$, each a boundary integral over $S$ with opposite orientation.
   - *Hint:* Splitting a manifold along a hypersurface gives opposite induced orientations, so $\partial X_-=-S$, $\partial D=+S$.
   - *Why needed:* It produces the difference $\int_S(\operatorname{cs}(A_2)-\operatorname{cs}(A_1))$.

3. **Reduce to the gauge variation.** On $S$, $A_2=g^{-1}A_1g+g^{-1}dg$, and $\operatorname{cs}(A_2)-\operatorname{cs}(A_1)=-\frac13\operatorname{tr}(\theta^{\wedge3})-d(\cdots)$.
   - *Hint:* $A_1,A_2$ express the same connection; use the gauge-variation identity.
   - *Why needed:* It isolates the winding form.

4. **Kill the exact term and evaluate the degree.** Over the closed $S=S^3$ the exact term integrates to zero, and $\int_S\operatorname{tr}(\theta^{\wedge3})=-24\pi^2\deg g$.
   - *Hint:* Stokes on the closed sphere; the sign ledger's constant.
   - *Why needed:* It yields $\frac1{8\pi^2}\int_X\operatorname{tr}(F\wedge F)=\deg g=k(P)$.

---

# Lemma Decomposition

> [!note]- Lemma 1: $\operatorname{tr}(F_A\wedge F_A)$ is a global closed four-form, locally $d\operatorname{cs}(A)$
> **Statement:** For a principal $SU(2)$-bundle $P\to X$ with connection $A$, the four-form $\operatorname{tr}(F_A\wedge F_A)$ is well defined on all of $X$, is closed, and in any local trivialisation with connection matrix $A_i$ satisfies $\operatorname{tr}(F_{A_i}\wedge F_{A_i})=d\operatorname{cs}(A_i)$ with $\operatorname{cs}(A_i)=\operatorname{tr}(A_i\wedge dA_i+\tfrac23A_i^{\wedge3})$.
>
> **Hint:** Conjugation-invariance of $\operatorname{tr}$ makes the four-form independent of the trivialisation; the transgression formula supplies the primitive.
>
> **Why needed:** It is the local exactness that lets Stokes convert the bulk integral into a boundary term.
>
> > [!note]- Full proof
> > **Globality.** Under a change of trivialisation the connection matrix transforms as $A'=g^{-1}Ag+g^{-1}dg$ and the curvature as $F_{A'}=g^{-1}F_Ag$ ([[Thm - Gauge Transformations Act on Connections and Curvature|the gauge-transformation theorem]]). Hence $\operatorname{tr}(F_{A'}\wedge F_{A'})=\operatorname{tr}(g^{-1}F_A\wedge F_Ag)=\operatorname{tr}(F_A\wedge F_A)$ by conjugation-invariance of the trace, so the locally defined four-forms agree on overlaps and glue to a global four-form on $X$ (this is the Chern–Weil form of the invariant polynomial $\xi\mapsto\operatorname{tr}(\xi^2)$; see [[Def - Chern-Weil Form of an Invariant Polynomial]]).
> >
> > **Local exactness.** In a trivialisation the connection is a matrix-valued one-form $A_i$ with $F_{A_i}=dA_i+A_i\wedge A_i$. By [[Thm - Transgression Formula and the Chern-Simons Form|the transgression formula]] (the trivial-bundle case with $p(\xi)=\operatorname{tr}(\xi^2)$),
> > $$\operatorname{tr}(F_{A_i}\wedge F_{A_i})=d\operatorname{tr}\Big(A_i\wedge dA_i+\tfrac23A_i\wedge A_i\wedge A_i\Big)=d\operatorname{cs}(A_i).$$
> > (For completeness, one verifies directly $d\operatorname{cs}(A)=\operatorname{tr}(dA\,dA)+2\operatorname{tr}(A^2dA)$ and $\operatorname{tr}(F^{\wedge2})=\operatorname{tr}(dA\,dA)+2\operatorname{tr}(A^2dA)$, using $\operatorname{tr}(A^{\wedge4})=0$ from cyclicity of the trace on four one-forms.)
> >
> > **Closedness.** Locally $\operatorname{tr}(F\wedge F)=d\operatorname{cs}(A_i)$ is exact hence closed; closedness is a local condition, so the global form is closed. $\;\blacksquare$

> [!note]- Lemma 2: gauge variation of the Chern–Simons form (restated)
> **Statement:** For $A\in\Omega^1(U;\mathfrak{su}(2))$ and smooth $g\colon U\to SU(2)$ with $A^g=g^{-1}Ag+g^{-1}dg$ and $\theta=g^{-1}dg$,
> $$\operatorname{cs}(A^g)=\operatorname{cs}(A)-\tfrac13\operatorname{tr}(\theta^{\wedge3})-d\operatorname{tr}(dg\,g^{-1}\wedge A).$$
>
> **Hint:** Expand $\operatorname{cs}(A^g)$ using $A^g=g^{-1}Ag+\theta$, $d\theta=-\theta^{\wedge2}$, and cyclicity; the mixed terms assemble into the stated exact form.
>
> **Why needed:** It reduces the difference $\operatorname{cs}(A_2)-\operatorname{cs}(A_1)$ across the clutching sphere to the winding form.
>
> > [!note]- Full proof
> > This is the identity proved in full on [[Thm - Gauge Variation of the Chern-Simons Functional]]; we restate the computation. Write $A^g=B+\theta$ with $B=g^{-1}Ag$, so $dB=g^{-1}(dA)g-\theta B-B\theta$ and $d\theta=-\theta^{\wedge2}$. Expanding $\operatorname{cs}(A^g)=\operatorname{tr}(A^g\,dA^g+\tfrac23(A^g)^{\wedge3})$ and using cyclicity of the trace on products of one-forms, the terms quadratic in $B$ and $\theta$ collect to
> > $$\operatorname{cs}(A^g)=\operatorname{cs}(B)+\operatorname{tr}(\theta\,dB)+\operatorname{tr}(B\theta^{\wedge2})-\tfrac13\operatorname{tr}(\theta^{\wedge3}),$$
> > and, using $\operatorname{tr}(B^{\wedge3})=\operatorname{tr}(A^{\wedge3})$, $\operatorname{tr}(B\,dB)=\operatorname{tr}(A\,dA)-2\operatorname{tr}(B^2\theta)$, one finds $\operatorname{cs}(B)=\operatorname{cs}(A)-2\operatorname{tr}(B^2\theta)$. Substituting and cancelling the $B^2\theta$ terms leaves $\operatorname{cs}(A^g)=\operatorname{cs}(A)+\operatorname{tr}(\theta\,dB)+\operatorname{tr}(B\theta^{\wedge2})-\tfrac13\operatorname{tr}(\theta^{\wedge3})$. Writing $\bar\theta=dg\,g^{-1}=g\theta g^{-1}$ (so $d\bar\theta=\bar\theta^{\wedge2}$), the middle two terms equal $\operatorname{tr}(\bar\theta\,dA)-\operatorname{tr}(A\bar\theta^{\wedge2})=-d\operatorname{tr}(\bar\theta\wedge A)$, whence
> > $$\operatorname{cs}(A^g)=\operatorname{cs}(A)-\tfrac13\operatorname{tr}(\theta^{\wedge3})-d\operatorname{tr}(dg\,g^{-1}\wedge A).$$
> > The full term-by-term expansion, with every cancellation displayed, is on the linked page. $\;\blacksquare$

> [!note]- Lemma 3: the winding integral over the clutching sphere
> **Statement:** For the clutching map $g\colon S=\partial D\to SU(2)$ of $P$, with $S$ oriented as $\partial D$, $\displaystyle\int_S\operatorname{tr}\big((g^{-1}dg)^{\wedge3}\big)=-24\pi^2\deg g=-24\pi^2\,k(P)$.
>
> **Hint:** $\operatorname{tr}(\theta^{\wedge3})$ is a bi-invariant top-form on $SU(2)=S^3$ with total integral $-24\pi^2$ (sign ledger), and the degree theorem transports it.
>
> **Why needed:** It supplies the numerical constant that turns the boundary term into $8\pi^2k(P)$.
>
> > [!note]- Full proof
> > By [[Thm - Classification of Principal SU(2)-Bundles over Four-Manifolds]] (statement (B)3) and the sign ledger computation on [[Def - The Hopf Bundle#Sign ledger]], $W(g)=\frac1{24\pi^2}\int_{S^3}\operatorname{tr}((g^{-1}dg)^{\wedge3})=-\deg g$, since $\operatorname{tr}(\theta^{\wedge3})$ is bi-invariant with $\int_{SU(2)}\operatorname{tr}(\theta^{\wedge3})=-24\pi^2$ and the degree theorem gives $\int_{S^3}g^*\operatorname{tr}(\theta^{\wedge3})=\deg g\cdot(-24\pi^2)$. The orientation on $S=\partial D$ matches that of $SU(2)$ through an oriented chart $D\cong B^4$, so $\deg g=k(P)$. Therefore $\int_S\operatorname{tr}((g^{-1}dg)^{\wedge3})=-24\pi^2k(P)$. $\;\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> **Step 0 — the cohomology class.** By [[Def - Chern Classes|the definition of Chern classes]] with $c(E)=\det(1+\tfrac{i}{2\pi}F)$ and the identity $\operatorname{tr}(\xi^2)=-2\det\xi$ on $\mathfrak{su}(2)$ ([[Ex - The Coefficients of the Characteristic Polynomial are Ad-Invariant]]), the degree-four part of the total Chern form of an $SU(2)$-connection is $c_2(F_A)=-\tfrac1{4\pi^2}\det F_A=\tfrac1{8\pi^2}\operatorname{tr}(F_A\wedge F_A)$, so $c_2(P)=\big[\tfrac1{8\pi^2}\operatorname{tr}(F_A\wedge F_A)\big]\in H^4_{dR}(X)$; by [[Thm - Chern-Weil Theorem|the Chern–Weil theorem]] this de Rham class is independent of $A$. It remains to evaluate its integral.
>
> **Step 1 — the four-form and its local primitives.** By Lemma 1, $\operatorname{tr}(F_A\wedge F_A)$ is a global closed four-form on $X$, and in the two trivialisations of $P$ over $X_-=X\setminus D^\circ$ and over $D$ — which exist by [[Thm - Classification of Principal SU(2)-Bundles over Four-Manifolds]] (B)1 — it equals $d\operatorname{cs}(A_1)$ and $d\operatorname{cs}(A_2)$ respectively, where $A_1,A_2$ are the connection matrices of $A$ in the two trivialisations.
>
> **Step 2 — split and apply Stokes.** Since $X=X_-\cup D$ with $X_-\cap D=S$,
> $$\int_X\operatorname{tr}(F_A\wedge F_A)=\int_{X_-}d\operatorname{cs}(A_1)+\int_D d\operatorname{cs}(A_2).$$
> By [[Thm - Stokes' Theorem on Manifolds|Stokes' theorem]], $\int_{X_-}d\operatorname{cs}(A_1)=\int_{\partial X_-}\operatorname{cs}(A_1)$ and $\int_D d\operatorname{cs}(A_2)=\int_{\partial D}\operatorname{cs}(A_2)$. Splitting $X$ along the hypersurface $S$ induces opposite boundary orientations on the two pieces ([[Def - Manifold with Boundary and Induced Orientation]]): $\partial D=S$ (boundary orientation from $D$) while $\partial X_-=-S$. Hence
> $$\int_X\operatorname{tr}(F_A\wedge F_A)=-\int_S\operatorname{cs}(A_1)+\int_S\operatorname{cs}(A_2)=\int_S\big(\operatorname{cs}(A_2)-\operatorname{cs}(A_1)\big).$$
>
> **Step 3 — the two primitives differ by a gauge transformation.** On the collar of $S$ the two trivialisations of the same connection $A$ are related by the clutching map $g$, i.e. $A_2=g^{-1}A_1g+g^{-1}dg=A_1^{\,g}$ ([[Thm - Gauge Transformations Act on Connections and Curvature|the gauge action]], local form). By Lemma 2 with $A=A_1$,
> $$\operatorname{cs}(A_2)-\operatorname{cs}(A_1)=\operatorname{cs}(A_1^{\,g})-\operatorname{cs}(A_1)=-\tfrac13\operatorname{tr}\big((g^{-1}dg)^{\wedge3}\big)-d\operatorname{tr}(dg\,g^{-1}\wedge A_1).$$
>
> **Step 4 — integrate over the closed sphere.** Since $S=S^3$ is closed (boundaryless), Stokes kills the exact term: $\int_S d\operatorname{tr}(dg\,g^{-1}\wedge A_1)=0$. Therefore
> $$\int_X\operatorname{tr}(F_A\wedge F_A)=-\tfrac13\int_S\operatorname{tr}\big((g^{-1}dg)^{\wedge3}\big).$$
>
> **Step 5 — evaluate the winding integral.** By Lemma 3, $\int_S\operatorname{tr}((g^{-1}dg)^{\wedge3})=-24\pi^2k(P)$. Combining with Step 4,
> $$\int_X\operatorname{tr}(F_A\wedge F_A)=-\tfrac13\cdot(-24\pi^2k(P))=8\pi^2k(P).$$
>
> **Step 6 — conclude.** Dividing by $8\pi^2$,
> $$\frac1{8\pi^2}\int_X\operatorname{tr}(F_A\wedge F_A)=k(P)\in\mathbb Z.$$
> Since $k(P)$ is a topological invariant of $P$ independent of $A$, so is the integral; and since every integer occurs as some $k(P)$ ([[Thm - Classification of Principal SU(2)-Bundles over Four-Manifolds]] (C)), every integer occurs as a value of the integral. Together with Step 0 this proves the theorem. Therefore the second Chern number of an $SU(2)$-bundle over a closed oriented four-manifold, computed analytically as $\frac1{8\pi^2}\int_X\operatorname{tr}(F_A\wedge F_A)$, equals the topological clutching degree $k(P)$. $\;\blacksquare$

---

# Cross-Field Exercise Suggestions

**The BPST instanton.** The basic anti-self-dual $SU(2)$ connection on $S^4$, written in quaternionic coordinates as $A=\operatorname{Im}\frac{\bar x\,dx}{1+|x|^2}$, has $\frac1{8\pi^2}\int_{S^4}\operatorname{tr}(F\wedge F)=1$; the theorem predicts this equals the clutching degree of the quaternionic Hopf bundle $S^7\to S^4$, namely $1$. The application is non-obvious because the analytic charge and the topological gluing degree are computed by entirely different routes yet must agree.

**Topological charge in lattice gauge theory.** Numerical gauge theory measures the topological charge of a field configuration by a discretisation of $\frac1{8\pi^2}\int\operatorname{tr}(F\wedge F)$; the theorem guarantees this converges to an integer, the bundle's Chern number, which is why "charge quantisation" is exact in the continuum limit. The subtlety is that the discretised integral need not be an integer, but its continuum value is forced to be one.

**Second Chern number of a Calabi–Yau surface's tangent bundle.** For a complex surface the tangent bundle is a $U(2)$-bundle; when $c_1=0$ (Calabi–Yau) it reduces to $SU(2)$ and $c_2[X]=\frac1{8\pi^2}\int_X\operatorname{tr}(F\wedge F)=\chi(X)$ by Gauss–Bonnet. The application links the gauge-theoretic integral to the Euler characteristic; the non-obvious step is the reduction of the structure group to $SU(2)$ using the Calabi–Yau condition.

---

# Bridges

- **The clutching classification.** The integer $k(P)=\deg g$ is defined and shown invariant on [[Thm - Classification of Principal SU(2)-Bundles over Four-Manifolds]]; this page shows that same integer is computed by any curvature. The two pages are the topological and analytic faces of one invariant.

- **The gauge variation of Chern–Simons.** The boundary term $\operatorname{cs}(A_2)-\operatorname{cs}(A_1)$ is exactly the gauge variation studied on [[Thm - Gauge Variation of the Chern-Simons Functional]]; over a closed three-manifold it makes the Chern–Simons functional multivalued by integers, and over the clutching sphere it produces the Chern number here.

- **The Yang–Mills bound.** Since $\frac1{8\pi^2}\int_X\operatorname{tr}(F\wedge F)=k(P)$ and $\operatorname{tr}(F\wedge F)$ compares pointwise with $|F|^2\,\mathrm{vol}$, chapter VII's **[[Thm - Energy Identity and the Topological Bound for Yang-Mills]]** turns this identity into the instanton energy floor $\mathcal{YM}(A)\ge8\pi^2|k(P)|$.

- **The sign ledger.** The plus sign in $c_2[X]=+k(P)$ is a consequence of $\int_{SU(2)}\operatorname{tr}(\theta^{\wedge3})=-24\pi^2$ (item (a) of [[Def - The Hopf Bundle#Sign ledger]]) combined with the two minus signs of Steps 2 and 4; changing the orientation of $S^3$ would flip all three and preserve the plus.

---

# Unlocked by This

> [!tip] The Chern–Simons functional is $\mathbb R/\mathbb Z$-valued *(from Gauge Theory VI §6.4)*
> Integrality of $\frac1{8\pi^2}\int_X\operatorname{tr}(F\wedge F)$ over closed four-manifolds is exactly what makes **[[Def - Chern-Simons Functional]]** well defined modulo $\mathbb Z$ on a three-manifold.

> [!tip] Instanton moduli on the $k=1$ bundle *(from Gauge Theory XIII)*
> The bundle with $\frac1{8\pi^2}\int\operatorname{tr}(F\wedge F)=1$ carries the anti-self-dual moduli space at the heart of **[[Thm - Donaldson Diagonalisation Theorem]]**.
