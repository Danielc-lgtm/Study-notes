---
type: theorem
subject: gauge-theory
prereqs:
  - "Ex - SU(2) is the Group of Unit Quaternions"
  - "Thm - Generic Sections are Transverse to the Zero Section"
  - "Thm - Homogeneity Lemma for Connected Manifolds"
  - "Thm - Homotopic Maps Pull Back Isomorphic Principal Bundles"
  - "Thm - Clutching Construction for Bundles over a Closed Manifold"
  - "Thm - The Brouwer Degree is an Integer and a Homotopy Invariant"
  - "Thm - Sections of a Principal Bundle and Triviality"
  - "Thm - Vector Bundles are Associated to Their Frame Bundles"
tags: [geometry, gauge-theory]
---

# Notation

$G$ acts on the **right** on principal bundles ([[Def - Principal G-Bundle]]). We identify $SU(2)$ with the unit quaternions $Sp(1)$ ([[Ex - SU(2) is the Group of Unit Quaternions]]) and with the $3$-sphere $S^3$; the orientation of $S^3$ is the boundary orientation of the unit ball in $\mathbb H=\mathbb R^4$, with $\mathbb R^4$ oriented by $(1,i,j,k)$, exactly as fixed on [[Def - The Hopf Bundle#Sign ledger]]. For a smooth $g\colon N\to SU(2)$ into the matrix group we write $\theta=g^{-1}dg\in\Omega^1(N;\mathfrak{su}(2))$ for the pulled-back Maurer–Cartan form ($\mathfrak{su}(2)$ being the traceless skew-Hermitian $2\times2$ matrices), and $\operatorname{tr}$ for the trace in the defining $2\times2$ representation. For maps between closed oriented $n$-manifolds, $\deg$ is the [[Thm - The Brouwer Degree is an Integer and a Homotopy Invariant|Brouwer degree]]. Given a closed connected oriented $4$-manifold $X$ and a closed coordinate disc $D\subset X$ with boundary $S=\partial D\cong S^3$, we write $X_-=X\setminus D^\circ$ and orient $S$ as $\partial D$ (boundary orientation from $D$, matching that of $SU(2)$ through an oriented chart $D\cong B^4$). We set
$$W(g):=\frac1{24\pi^2}\int_{S^3}\operatorname{tr}\big((g^{-1}dg)^{\wedge3}\big)\qquad(g\colon S^3\to SU(2)).$$
The volume $\operatorname{Vol}(S^3)=2\pi^2$ is used from [[Ex - Volume of the n-Sphere via the Volume Form]], and $\int_{SU(2)}\operatorname{tr}(\theta^{\wedge3})=-24\pi^2$ from the sign ledger.

---

# Statement

> **Classification of principal $SU(2)$-bundles.**
> **(A) Low dimensions.** Every principal $SU(2)$-bundle over a compact manifold $M$ of dimension $\dim M\le3$ is trivial.
>
> **(B) Four-manifolds and the Chern number.** Let $X$ be a closed connected oriented $4$-manifold and $P\to X$ a principal $SU(2)$-bundle. Then:
> 1. $P$ is trivial over $X\setminus\{x_0\}$ for every $x_0\in X$; consequently, choosing a coordinate disc $D\ni x_0$, $P$ is trivial over $X_-=X\setminus D^\circ$ and over $D$, and $P\cong P_g$ for a clutching map $g\colon S=\partial D\to SU(2)$ (normalised so the inner trivialisation is the outer one times $g$).
> 2. The integer $k(P):=\deg g$, the **Chern number** of $P$, is independent of the disc, the trivialisations, and the representative $g$, and depends only on the isomorphism class of $P$.
> 3. For every smooth $g\colon S^3\to SU(2)$, $W(g)=-\deg g$; equivalently $\displaystyle\int_{S^3}\operatorname{tr}\big((g^{-1}dg)^{\wedge3}\big)=-24\pi^2\deg g$.
>
> **(C) Realisation and additivity.** For every $k\in\mathbb Z$ there is a principal $SU(2)$-bundle over $X$ with $k(P)=k$ — for instance the clutching bundle $P_{q\mapsto q^k}$ of the power map $q\mapsto q^k$ of unit quaternions — and clutching degrees add: $k(P_{g_1g_2})=k(P_{g_1})+k(P_{g_2})$ for the pointwise product $g_1g_2$.

> **Scope remark (not proved and not used in this series).** That $k$ is a *complete* invariant — that two $SU(2)$-bundles over $X$ with the same Chern number are isomorphic — requires $\pi_3(SU(2))=\pi_3(S^3)\cong\mathbb Z$ (the Hopf degree theorem in dimension three), which the series neither proves nor uses. Nothing in chapters I–VI, nor the later chapters' stated uses, needs more than the **existence** of a bundle with each Chern number and the **invariance** of $k$, both established above.

---

# Motivation

The single most important gauge-theoretic input to four-manifold topology is that principal $SU(2)$-bundles over a closed oriented four-manifold are classified by one integer, their Chern number. Donaldson theory studies the moduli space of anti-self-dual connections on the bundle with $k(P)=1$; the very statement "the bundle with $k=1$" presupposes this classification. The Yang–Mills topological energy bound $\mathcal{YM}(A)\ge8\pi^2|k(P)|$ is a bound in terms of this integer. And the Chern–Simons functional of a connection on a three-manifold is defined precisely because part (A) makes every $SU(2)$-bundle over a three-manifold trivial, so that connections may be treated as honest $\mathfrak{su}(2)$-valued one-forms.

The theorem answers, in order, three questions. First, *when is the twisting invisible?* — and the answer is that below dimension four an $SU(2)$-bundle cannot twist at all, because the fibre $SU(2)$ is three-connected and the obstruction to a section lives in a dimension the base does not reach. Second, *what measures the twisting when it appears?* — and the answer is a single integer, read off as the degree of the map by which one glues the bundle across the boundary of a small ball. Third, *is that integer arbitrary, and does it behave well?* — and the answer is that every value occurs and the values add under the group operation on clutching maps. The identity $W(g)=-\deg g$ is the bridge to analysis: it expresses the topological degree as the integral of a differential form, which is what lets chapter VI recognise the Chern number inside the curvature integral $\frac1{8\pi^2}\int_X\operatorname{tr}(F\wedge F)$.

---

# Sources and Targets

**Sources (Input Broadening).** The theorem's hypothesis is bare — a principal $SU(2)$-bundle over a closed oriented four-manifold, or any compact manifold of dimension at most three — so the skill is to recognise a problem as secretly of this form.

The first disguised source is **a rank-two complex vector bundle with a trivialised determinant.** A Hermitian complex $2$-plane bundle $E$ with $\det E$ trivial (equivalently $c_1(E)=0$ in a form that trivialises the determinant line) has structure group reducible to $SU(2)$: its bundle of special unitary frames is a principal $SU(2)$-bundle. So any statement about such $E$ — for instance a spinor bundle of a spin four-manifold, whose positive part is an $SU(2)$-bundle — is a statement about a principal $SU(2)$-bundle, and its Chern number is $c_2(E)[X]$. The bridge is the reduction-of-structure-group theorem [[Thm - Euclidean and Hermitian Structures are Reductions of the Structure Group]]. *Example problem:* show that the two spinor bundles $S^\pm$ of a spin structure on a closed spin four-manifold are $SU(2)$-bundles and compute their Chern numbers from the signature.

The second disguised source is **a map into $SU(2)$ from a three-manifold, or a clutching datum.** Any smooth $g\colon Y^3\to SU(2)$ manufactures, by clutching over a four-manifold containing $Y^3$ as a separating hypersurface (or over $S^4$ with $Y^3=S^3$ the equator), a principal $SU(2)$-bundle whose Chern number is $\deg g$. The non-obvious step is that a bundle's global twisting is fully encoded in such a boundary map. *Example problem:* build the basic instanton bundle over $S^4$ from the identity map $S^3\to SU(2)$ and confirm its Chern number is $\pm1$.

The third disguised source is **a real oriented rank-four bundle with a quaternionic structure.** A real rank-$4$ bundle $E$ carrying an $\mathbb H$-module structure has structure group $Sp(1)\cong SU(2)$ acting by right quaternion multiplication, so its frame data is a principal $SU(2)$-bundle. The bridge is again reduction of the structure group, now to $Sp(1)$. *Example problem:* recognise the tangent bundle of a hyperkähler four-manifold, or the bundle $\underline{\mathbb H}$ over $\mathbb{HP}^1=S^4$, as carrying an $SU(2)$-bundle of frames.

**Targets (Output Amplification).** The bare conclusion is "$SU(2)$-bundles over $X^4$ are labelled by an integer $k$." Combined with other results it does much more.

Combine the classification with **Chern–Weil theory.** Chapter VI proves $k(P)=\frac1{8\pi^2}\int_X\operatorname{tr}(F_A\wedge F_A)=c_2(P)[X]$ for any connection $A$ (see [[Thm - Second Chern Number of an SU(2)-Bundle over a Closed Four-Manifold is the Clutching Degree]]). The amplified result is that the integral $\frac1{8\pi^2}\int_X\operatorname{tr}(F\wedge F)$ is a topological invariant independent of $A$ and always an integer — a fact invisible from the analysis of connections alone, obtained here by identifying it with a clutching degree.

Combine the classification with **the Yang–Mills functional.** The energy identity $\mathcal{YM}(A)=\frac12\int_X|F_A|^2$ and the inequality $|F|^2\ge\pm\operatorname{tr}(F\wedge F)/\mathrm{vol}$ give $\mathcal{YM}(A)\ge8\pi^2|k(P)|$, with equality exactly for (anti-)self-dual connections. The extra ingredient is the pointwise inequality of chapter VII; the payoff is that the Chern number sets a floor on the energy that only instantons attain.

Combine the classification with **part (A) on three-manifolds.** Triviality of $SU(2)$-bundles over a closed oriented three-manifold $M$ turns the space of connections into the affine space $\Omega^1(M;\mathfrak{su}(2))$, on which the Chern–Simons functional is a cubic polynomial; its critical points are the flat connections, i.e. representations $\pi_1(M)\to SU(2)$. The amplified result is the entire framework of Chern–Simons and instanton Floer theory of three-manifolds, which begins with part (A).

---

# Why Is It True

Picture an $SU(2)$-bundle $P$ over a manifold $M$ and its associated $\mathbb C^2$-bundle $E=P\times_{SU(2)}\mathbb C^2$, a real rank-four bundle. A principal $SU(2)$-bundle is trivial exactly when it has a global section, and a section of $P$ is the same as a nowhere-vanishing unit section of $E$ — because $SU(2)$ acts simply transitively on the unit sphere $S^3\subset\mathbb C^2$, so choosing a unit vector in each fibre is the same as choosing a group element in each fibre. Now count dimensions. A generic section of a rank-four bundle vanishes on a set of codimension four. If $\dim M\le3$ that set is empty for dimension reasons: a generic section is nowhere zero, so $P$ has a section and is trivial. This is the whole of part (A).

> **The bundle is trivial below dimension four because a rank-four bundle generically has no zeros there, and a nonvanishing section of the associated $\mathbb C^2$-bundle is a section of $P$.**

In dimension four the codimension-four zero set of a generic section is a *finite set of points*, each carrying a sign. Away from those points $P$ is trivial; the points can be swept into a single small ball by a homogeneity move; and then $P$ is described by how its two trivialisations — one over the ball, one over the complement — disagree on the boundary three-sphere. That disagreement is a map $g\colon S^3\to SU(2)$, and its only homotopy invariant that survives the freedom to change the two trivialisations is its degree, because changing a trivialisation multiplies $g$ by a map that extends over a bounding four-manifold and hence has degree zero. The Chern number is that degree. The identity $W(g)=-\deg g$ holds because $\operatorname{tr}((g^{-1}dg)^{\wedge3})$ is a bi-invariant top-form on the group $SU(2)=S^3$: a bi-invariant top-form is a constant multiple of the volume form, so its integral over the image counts the degree, and the constant $-24\pi^2$ is the value of the form on the group, computed once in the sign ledger.

---

# What Makes This Hard

Three points are easy to get wrong. First, the reduction of "trivial" to "has a nowhere-vanishing section of $E$" needs the simple transitivity of $SU(2)$ on the unit three-sphere of $\mathbb C^2$ — this is special to $SU(2)$ and $\mathbb C^2$ and fails for a general structure group, so the argument does not generalise verbatim. Second, the *invariance* of the Chern number is the crux, not the *definition*: one must show the clutching degree does not depend on the arbitrary trivialisations, and this rests on the fact that a map extending over a bounding manifold has degree zero, combined with the additivity of degree under pointwise products of $SU(2)$-valued maps — which is itself a non-trivial lemma (Lemma A). Third, the constant in $W(g)=-\deg g$ is genuinely orientation-dependent; the common error is to quote $+\deg g$, which corresponds to the opposite orientation of $S^3$ or the opposite sign of the trace form. Under the conventions fixed here the constant is $-24\pi^2$, and getting the sign right is what makes the downstream identity $c_2[X]=+k$ come out with a plus.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Pass from $P$ to its associated $\mathbb C^2$-bundle $E$. Use genericity of sections of $E$ to find, in dimension $\le3$, a nowhere-vanishing section (hence a section of $P$, hence triviality), and in dimension $4$, a section with finitely many zeros gathered into one disc (hence triviality off the disc). Describe $P$ by clutching across the boundary sphere; identify the invariant with the degree of the clutching map; prove invariance and additivity through the winding form $W$.

**Subgoal decomposition:**

1. **$P$ trivial $\iff$ $E$ has a nowhere-vanishing unit section.** Establish the equivariant-section dictionary.
   - *Hint:* A section of $E=P\times_{SU(2)}\mathbb C^2$ is an equivariant map $\hat u\colon P\to\mathbb C^2$; simple transitivity of $SU(2)$ on $S^3\subset\mathbb C^2$ turns a unit such $\hat u$ into a section of $P$.
   - *Why needed:* It converts a statement about the principal bundle into a transversality statement about a vector bundle.

2. **Part (A): nowhere-vanishing section in dimension $\le3$.** A generic section of a rank-$4$ bundle over $M^{\le3}$ has no zeros.
   - *Hint:* The zero set of a transverse section has codimension $4>\dim M$, so it is empty.
   - *Why needed:* It gives the section of $P$, hence triviality.

3. **Part (B), triviality off a disc.** A generic section over $X^4$ has finitely many zeros; sweep them into a disc.
   - *Hint:* Zeros are isolated and finite; the homogeneity lemma moves a finite set into a coordinate ball by an ambient isotopy.
   - *Why needed:* It exhibits $P$ as trivial over $X_-$ and over $D$, the input to clutching.

4. **The clutching description and the Chern number.** $P\cong P_g$; set $k(P)=\deg g$.
   - *Hint:* The clutching construction turns "trivial over both pieces" into a transition map $g\colon S\to SU(2)$.
   - *Why needed:* It produces the candidate invariant.

5. **Invariance of $k(P)$.** The clutching ambiguity changes $g$ by boundary values of maps extending over $X_-$ and over $D$, which have degree zero.
   - *Hint:* Degree is additive under pointwise products (Lemma A); a map extending over a bounding manifold has degree zero (degree theorem (f)).
   - *Why needed:* It makes $k(P)$ well defined and an isomorphism invariant.

6. **The winding identity $W(g)=-\deg g$.** $\operatorname{tr}(\theta^{\wedge3})$ is bi-invariant, hence proportional to the volume form, with constant $-24\pi^2$.
   - *Hint:* Evaluate the form at the identity on the basis $-i\sigma_a$ (Lemma B), using the sign ledger's orientation computation.
   - *Why needed:* It expresses the degree as a form integral and feeds chapter VI.

7. **Realisation and additivity.** $\deg(q\mapsto q^k)=k$ and $\deg$ additive.
   - *Hint:* $W$ is additive under products (Lemma A) and $W(\mathrm{id})=-1$, so $\deg(q^k)=k$.
   - *Why needed:* Every integer occurs and the invariant is a homomorphism.

---

# Lemma Decomposition

> [!note]- Lemma 1: A principal $SU(2)$-bundle is trivial iff its associated $\mathbb C^2$-bundle has a nowhere-vanishing section
> **Statement:** Let $P\to M$ be a principal $SU(2)$-bundle and $E=P\times_{SU(2)}\mathbb C^2$ its associated bundle for the defining representation, with the $SU(2)$-invariant Hermitian metric descending from the standard metric on $\mathbb C^2$. Then $P$ admits a global section (equivalently, is trivial) if and only if $E$ admits a nowhere-vanishing section.
>
> **Hint:** Sections of $E$ are equivariant maps $P\to\mathbb C^2$; a unit one hits a fixed $e_1\in S^3$ at a unique point of each fibre because $SU(2)$ acts simply transitively on $S^3\subset\mathbb C^2$.
>
> **Why needed:** It converts the principal-bundle triviality question into transversality for a rank-four vector bundle, where dimension counting applies.
>
> > [!note]- Full proof
> > **($\Rightarrow$).** If $P$ has a global section $s\colon M\to P$ then $E=P\times_{SU(2)}\mathbb C^2$ is trivialised by $(m,v)\mapsto[s(m),v]$, and the constant unit section $m\mapsto[s(m),e_1]$ (with $e_1=(1,0)\in\mathbb C^2$, $|e_1|=1$) is nowhere zero. So $E$ has a nowhere-vanishing section.
> >
> > **($\Leftarrow$).** Suppose $u\in\Gamma(E)$ is nowhere zero. Normalising by the Hermitian metric, $\hat u:=u/\lVert u\rVert$ is a unit section, i.e. a section of the sphere bundle with fibre $S^3\subset\mathbb C^2$. By the equivariant-function description of sections of an associated bundle ([[Thm - Sections of an Associated Bundle are Equivariant Functions]]), $\hat u$ corresponds to a smooth map $\varphi\colon P\to S^3\subset\mathbb C^2$ that is $SU(2)$-equivariant in the sense $\varphi(p\cdot q)=q^{-1}\varphi(p)$ for all $q\in SU(2)$ (the defining representation acts by $q\cdot v=qv$, so the associated-bundle convention $[pq,q^{-1}v]=[p,v]$ gives this equivariance).
> >
> > Fix $e_1\in S^3$. **Claim:** for each $m\in M$ there is a unique $p\in P_m$ with $\varphi(p)=e_1$. Indeed, fix any $p_0\in P_m$; every point of $P_m$ is $p_0q$ for a unique $q\in SU(2)$ (freeness and transitivity on the fibre), and $\varphi(p_0q)=q^{-1}\varphi(p_0)$. As $q$ ranges over $SU(2)$, $q^{-1}\varphi(p_0)$ ranges over the $SU(2)$-orbit of $\varphi(p_0)\in S^3$, which is all of $S^3$ because $SU(2)$ acts transitively on the unit sphere of $\mathbb C^2$ (given two unit vectors, extend each to a unitary basis of determinant one; the change of basis is in $SU(2)$ and carries one to the other). It equals $e_1$ for exactly one $q$, because the action is free (if $q^{-1}\varphi(p_0)=\varphi(p_0)$ then $q$ fixes a unit vector, and a determinant-one unitary fixing a unit vector fixes its orthogonal complement's induced generator too, forcing $q=1$). This proves existence and uniqueness of $p=:s(m)$.
> >
> > **Smoothness of $s$.** The set $Z=\varphi^{-1}(e_1)\subset P$ meets each fibre in one point. Near a point $p_\ast\in Z$ choose a local section $\sigma$ of $P$; then $q\mapsto\varphi(\sigma(m)q)=q^{-1}\varphi(\sigma(m))$ is a diffeomorphism $SU(2)\to S^3$ for each $m$ (simple transitivity), depending smoothly on $m$, so the unique $q(m)$ with $\varphi(\sigma(m)q(m))=e_1$ is smooth by the implicit function theorem, and $s(m)=\sigma(m)q(m)$ is a smooth local section; uniqueness makes these agree on overlaps, giving a global smooth section $s\colon M\to P$. By [[Thm - Sections of a Principal Bundle and Triviality]], $P$ is trivial. $\;\blacksquare$

> [!note]- Lemma 2 (Lemma A): The winding number $W$ is additive under pointwise products
> **Statement:** For smooth $g_1,g_2\colon S^3\to SU(2)$ with pointwise product $g_1g_2$, and $\theta_i=g_i^{-1}dg_i$, one has, with $\tilde\theta_1:=g_2^{-1}\theta_1g_2$,
> $$(g_1g_2)^{-1}d(g_1g_2)=\tilde\theta_1+\theta_2,\qquad \operatorname{tr}\big((\tilde\theta_1+\theta_2)^{\wedge3}\big)=\operatorname{tr}(\theta_1^{\wedge3})+\operatorname{tr}(\theta_2^{\wedge3})-3\,d\operatorname{tr}(\tilde\theta_1\wedge\theta_2),$$
> and consequently, integrating over the closed manifold $S^3$, $W(g_1g_2)=W(g_1)+W(g_2)$; also $W(g^{-1})=-W(g)$.
>
> **Hint:** Use $d\theta=-\theta\wedge\theta$, cyclicity of the trace on products of one-forms, and Stokes to kill the exact term.
>
> **Why needed:** Additivity of $W$ (hence of $\deg=-W$) is the engine of both the invariance of the Chern number (Lemma 4) and the realisation statement (C).
>
> > [!note]- Full proof
> > **The product Maurer–Cartan form.** By the Leibniz rule and $d(g_1g_2)=(dg_1)g_2+g_1\,dg_2$,
> > $$(g_1g_2)^{-1}d(g_1g_2)=g_2^{-1}g_1^{-1}\big((dg_1)g_2+g_1\,dg_2\big)=g_2^{-1}(g_1^{-1}dg_1)g_2+g_2^{-1}dg_2=g_2^{-1}\theta_1g_2+\theta_2=\tilde\theta_1+\theta_2.$$
> >
> > **The cubic identity.** Write $a=\tilde\theta_1$, $b=\theta_2$, both $\mathfrak{su}(2)$-valued one-forms. Expanding the wedge-cube and using that the trace of a product of three one-forms is cyclic (moving a degree-$1$ factor past a degree-$2$ product costs $(-1)^{1\cdot2}=+1$), $\operatorname{tr}(a^2b)=\operatorname{tr}(aba)=\operatorname{tr}(ba^2)$ and likewise for $ab^2$, so
> > $$\operatorname{tr}\big((a+b)^{\wedge3}\big)=\operatorname{tr}(a^{\wedge3})+\operatorname{tr}(b^{\wedge3})+3\operatorname{tr}(a^2b)+3\operatorname{tr}(ab^2).$$
> > Since $\operatorname{tr}(a^{\wedge3})=\operatorname{tr}\big((g_2^{-1}\theta_1g_2)^{\wedge3}\big)=\operatorname{tr}(g_2^{-1}\theta_1^{\wedge3}g_2)=\operatorname{tr}(\theta_1^{\wedge3})$ (conjugation invariance of the trace), it remains to identify $3\operatorname{tr}(a^2b)+3\operatorname{tr}(ab^2)$ as an exact form. Compute the exterior derivatives: from $d\theta_2=-\theta_2^{\wedge2}$ we get $db=-b^{\wedge2}$; and, using $d(g_2^{-1})=-\theta_2g_2^{-1}$, $dg_2=g_2\theta_2$ and $d\theta_1=-\theta_1^{\wedge2}$,
> > $$da=d(g_2^{-1}\theta_1g_2)=-\theta_2\tilde\theta_1+g_2^{-1}(-\theta_1^{\wedge2})g_2-\tilde\theta_1\theta_2=-a^2-ba-ab\qquad(\text{since }g_2^{-1}\theta_1^{\wedge2}g_2=a^2).$$
> > Therefore, with $a$ of degree $1$,
> > $$d\operatorname{tr}(a\wedge b)=\operatorname{tr}(da\wedge b)-\operatorname{tr}(a\wedge db)=\operatorname{tr}\big((-a^2-ba-ab)b\big)-\operatorname{tr}\big(a(-b^2)\big).$$
> > Using cyclicity $\operatorname{tr}(bab)=\operatorname{tr}(ab^2)$,
> > $$d\operatorname{tr}(a\wedge b)=-\operatorname{tr}(a^2b)-\operatorname{tr}(ab^2)-\operatorname{tr}(ab^2)+\operatorname{tr}(ab^2)=-\operatorname{tr}(a^2b)-\operatorname{tr}(ab^2),$$
> > so $3\operatorname{tr}(a^2b)+3\operatorname{tr}(ab^2)=-3\,d\operatorname{tr}(a\wedge b)=-3\,d\operatorname{tr}(\tilde\theta_1\wedge\theta_2)$, which is the claimed identity.
> >
> > **Additivity.** Integrating over the closed manifold $S^3$ and applying [[Thm - Stokes' Theorem on Manifolds|Stokes' theorem]] (boundaryless, so $\int_{S^3}d(\cdots)=0$),
> > $$\int_{S^3}\operatorname{tr}\big(((g_1g_2)^{-1}d(g_1g_2))^{\wedge3}\big)=\int_{S^3}\operatorname{tr}(\theta_1^{\wedge3})+\int_{S^3}\operatorname{tr}(\theta_2^{\wedge3}),$$
> > i.e. $24\pi^2W(g_1g_2)=24\pi^2W(g_1)+24\pi^2W(g_2)$, giving $W(g_1g_2)=W(g_1)+W(g_2)$. Taking $g_2=g_1^{-1}$ (so $g_1g_2\equiv e$, whose Maurer–Cartan form vanishes, $W(e)=0$) gives $W(g^{-1})=-W(g)$. $\;\blacksquare$

> [!note]- Lemma 3 (Lemma B): $W(g)=-\deg g$
> **Statement:** For every smooth $g\colon S^3\to SU(2)$, $W(g)=-\deg g$; equivalently $\int_{S^3}\operatorname{tr}((g^{-1}dg)^{\wedge3})=-24\pi^2\deg g$.
>
> **Hint:** $\operatorname{tr}(\theta^{\wedge3})$ is a bi-invariant top-form on $SU(2)=S^3$, hence a constant times the volume form; the constant is computed in the sign ledger.
>
> **Why needed:** It converts the topological degree into a differential-form integral, giving statement (B)3 and the input to the Chern–Weil identification in chapter VI.
>
> > [!note]- Full proof
> > The form $\Xi:=\operatorname{tr}(\theta^{\wedge3})$, with $\theta$ the left Maurer–Cartan form of $SU(2)$, is left-invariant because $\theta$ is, and right-invariant because $R_h^*\theta=\operatorname{Ad}_{h^{-1}}\theta$ and the trace is $\operatorname{Ad}$-invariant: $R_h^*\Xi=\operatorname{tr}((\operatorname{Ad}_{h^{-1}}\theta)^{\wedge3})=\operatorname{tr}(h^{-1}\theta^{\wedge3}h)=\Xi$. A bi-invariant $3$-form on the $3$-dimensional group $SU(2)$ is a constant multiple of the Riemannian volume form of the bi-invariant metric, hence $\Xi=c\,\mathrm{vol}_{S^3}$ with $c=\Xi_e(E_1,E_2,E_3)$ for a positively oriented orthonormal basis $(E_1,E_2,E_3)$. This constant, together with the orientation of $SU(2)\cong S^3=\partial B^4$ and the value $\operatorname{Vol}(S^3)=2\pi^2$, is computed in full on [[Def - The Hopf Bundle#Sign ledger]]:
> > $$\int_{SU(2)}\operatorname{tr}(\theta^{\wedge3})=-24\pi^2,$$
> > obtained from $\Xi_e(E_1,E_2,E_3)=3\operatorname{tr}(E_1[E_2,E_3])=-12$ on the basis $E_a=-i\sigma_a$ (with $[E_2,E_3]=2E_1$, $\operatorname{tr}(E_1^2)=-2$) and the fact, verified there, that $(E_1,E_2,E_3)$ is a positively oriented orthonormal basis of $T_eS^3$.
> >
> > For a general $g\colon S^3\to SU(2)$, both source and target are the oriented three-sphere, and by [[Thm - The Brouwer Degree is an Integer and a Homotopy Invariant|the degree theorem]], $\int_{S^3}g^*\Xi=\deg g\cdot\int_{SU(2)}\Xi$. Hence
> > $$\int_{S^3}\operatorname{tr}\big((g^{-1}dg)^{\wedge3}\big)=\deg g\cdot(-24\pi^2),\qquad W(g)=\frac1{24\pi^2}\cdot(-24\pi^2)\deg g=-\deg g. \qquad\blacksquare$$

> [!note]- Lemma 4: The clutching degree is invariant under the clutching ambiguity
> **Statement:** Let $X$ be a closed connected oriented $4$-manifold, $D\subset X$ a coordinate disc, $S=\partial D$, $X_-=X\setminus D^\circ$. If $g,g'\colon S\to SU(2)$ are related by $g'=(a|_S)\,g\,(b|_S)$ for smooth $a\colon X_-\to SU(2)$ and $b\colon D\to SU(2)$, then $\deg g'=\deg g$.
>
> **Hint:** $\deg$ is additive under pointwise products (Lemma A gives $\deg=-W$ additive), and $a|_S$, $b|_S$ extend over the bounding manifolds $X_-$, $D$, hence have degree zero.
>
> **Why needed:** It is precisely the statement that $k(P)=\deg g$ does not depend on the trivialisations used to define the clutching map, i.e. that the Chern number is well defined.
>
> > [!note]- Full proof
> > By Lemma 3, $\deg=-W$, and by Lemma 2, $W$ is additive under pointwise products; hence $\deg$ is additive under pointwise products of $SU(2)$-valued maps on $S^3$:
> > $$\deg\big((a|_S)\,g\,(b|_S)\big)=\deg(a|_S)+\deg g+\deg(b|_S).$$
> > Now $X_-$ is a compact oriented $4$-manifold with boundary $\partial X_-=S$ (with one of its two orientations), and $a|_S$ is the restriction to $\partial X_-$ of the smooth map $a\colon X_-\to SU(2)$. By clause (f) of [[Thm - The Brouwer Degree is an Integer and a Homotopy Invariant|the degree theorem]] — a map on a closed oriented three-manifold that extends smoothly over a compact oriented four-manifold it bounds has degree zero — we get $\deg(a|_S)=0$. Likewise $D$ is a compact oriented $4$-manifold with boundary $S$, and $b|_S$ extends over it as $b$, so $\deg(b|_S)=0$. Therefore $\deg g'=\deg g$. $\;\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Throughout, $E=P\times_{SU(2)}\mathbb C^2$ is the associated $\mathbb C^2$-bundle for the defining representation, a real rank-$4$ bundle with the invariant Hermitian metric of Lemma 1.
>
> **Part (A): $\dim M\le3\Rightarrow P$ trivial.**
>
> **Step 0 — a metric and a hermitian structure.** The manifold $M$ is compact; equip $E$ with the invariant Hermitian metric of Lemma 1 (it exists because the standard metric on $\mathbb C^2$ is $SU(2)$-invariant and descends).
>
> **Step 1 — a nowhere-vanishing section of $E$.** $E$ is a real vector bundle of rank $r=4$ over the compact manifold $M$ of dimension $m=\dim M\le3<4=r$. By [[Thm - Generic Sections are Transverse to the Zero Section|the generic-sections theorem]] (clause (c): if $r>m$ then $E$ has a nowhere-vanishing section), $E$ has a section $u$ with $u(x)\neq0$ for all $x$.
>
> **Step 2 — conclude triviality.** By Lemma 1 ($\Leftarrow$), a nowhere-vanishing section of $E$ yields a global section of $P$; by [[Thm - Sections of a Principal Bundle and Triviality]], $P$ is trivial. This proves (A). $\;\square$
>
> **Part (B): four-manifolds.**
>
> **Step 0 — genericity setup.** Give $E$ the invariant Hermitian metric. $X$ is a closed (compact, boundaryless) connected oriented $4$-manifold; $E$ has rank $r=4=\dim X=m$.
>
> **Step 1 — a section with finitely many zeros.** By [[Thm - Generic Sections are Transverse to the Zero Section|the generic-sections theorem]] (clause (c) with $r=m$), there is a section $u$ of $E$ transverse to the zero section, whose zero set $Z=\{x:u(x)=0\}$ is therefore a $0$-dimensional compact submanifold, i.e. a finite set of points.
>
> **Step 2 — gather the zeros into a disc.** $X$ is connected and $\dim X=4\ge2$, so by [[Thm - Homogeneity Lemma for Connected Manifolds|the homogeneity lemma]] there is a diffeomorphism $h\colon X\to X$, isotopic to the identity, carrying the finite set $Z$ into the interior of a chosen coordinate disc $D$. Replacing $u$ by $h^*$-transported data (equivalently, replacing $D$ by $h^{-1}(D)$), we may assume all zeros of $u$ lie in $D^\circ$. Then $u$ is nowhere zero on $X_-=X\setminus D^\circ$.
>
> **Step 3 — triviality over the two pieces.** Over $X_-$ the section $u$ is nowhere zero, so by Lemma 1 (applied to $P|_{X_-}$ and $E|_{X_-}$) $P$ is trivial over $X_-$. Over the disc $D$, which is contractible, $P$ is trivial by [[Thm - Homotopic Maps Pull Back Isomorphic Principal Bundles|the homotopy theorem]] (clause (c): every principal bundle over a closed disc is trivial). In particular $P$ is trivial over $X\setminus\{x_0\}$ for $x_0\in D^\circ$, since $X\setminus\{x_0\}$ deformation-retracts onto $X_-$ and triviality is a homotopy-invariant property of the pullback. This proves (B)1's triviality clauses.
>
> **Step 4 — the clutching description.** Fix trivialisations $\Psi_-$ over $X_-$ and $\Psi_+$ over $D$, with local sections $s_-,s_+$. On a collar of $S=\partial D$ the two sections are related by $s_+=s_-\cdot g$ for a unique smooth $g\colon S\to SU(2)$ ([[Def - Transition Functions and the Cocycle Condition|the transition function]]). By [[Thm - Clutching Construction for Bundles over a Closed Manifold|the clutching construction]] (clause (b)), $P\cong P_g$, the bundle glued from $X_-\times SU(2)$ and $D\times SU(2)$ by $g$. Define the **Chern number** $k(P):=\deg g$, with $S$ oriented as $\partial D$.
>
> **Step 5 — invariance of $k(P)$.** A different choice of disc, trivialisations, or representative changes $g$ to $g'=(a|_S)\,g\,(b|_S)$ for smooth $a\colon X_-\to SU(2)$, $b\colon D\to SU(2)$ (the ambiguity in the two trivialisations), possibly composed with the isotopy of Step 2, under which the degree is unchanged by homotopy invariance of the degree. By [[Thm - Clutching Construction for Bundles over a Closed Manifold|the clutching construction]] (clause (c)) this is the full ambiguity, and by Lemma 4, $\deg g'=\deg g$. Since two isomorphic bundles have clutching maps related this way, $k(P)$ depends only on the isomorphism class. This proves (B)2.
>
> **Step 6 — the winding identity.** By Lemma 3, $W(g)=-\deg g$ for every smooth $g\colon S^3\to SU(2)$, equivalently $\int_{S^3}\operatorname{tr}((g^{-1}dg)^{\wedge3})=-24\pi^2\deg g$. This is (B)3. $\;\square$
>
> **Part (C): realisation and additivity.**
>
> **Step 1 — additivity.** For the pointwise product $g_1g_2$ of clutching maps, the clutching bundle satisfies $P_{g_1g_2}\cong P_{g_1}\#\,P_{g_2}$ in the sense that its clutching map is $g_1g_2$; by Lemma 2, $\deg(g_1g_2)=-W(g_1g_2)=-W(g_1)-W(g_2)=\deg g_1+\deg g_2$, so $k(P_{g_1g_2})=k(P_{g_1})+k(P_{g_2})$.
>
> **Step 2 — the power map has degree $k$.** Consider $\pi_k\colon SU(2)\to SU(2)$, $q\mapsto q^k$ (unit quaternions). By Lemma 2 applied repeatedly, $W(\pi_k)=W(\pi_1^{\,k})=kW(\pi_1)=kW(\mathrm{id})$; and $W(\mathrm{id})=-\deg(\mathrm{id})=-1$ by Lemma 3. Hence $W(\pi_k)=-k$, so $\deg(\pi_k)=-W(\pi_k)=k$. (For $k<0$ use $W(g^{-1})=-W(g)$.)
>
> **Step 3 — every integer occurs.** Form the clutching bundle $P_{\pi_k}$ over $X$ using the power map $\pi_k\colon S=\partial D\to SU(2)$ (via the oriented identification $S\cong S^3\cong SU(2)$). By Step 4 of Part (B) and Step 2, $k(P_{\pi_k})=\deg\pi_k=k$. Thus for every $k\in\mathbb Z$ there is a principal $SU(2)$-bundle over $X$ with Chern number $k$. This proves (C). $\;\blacksquare$

> [!warning] Convention: Haydys' proof of (A) versus the series' proof
> Haydys (Proposition 78) proves part (A) for *all* manifolds of dimension $\le3$ using the classifying space $\mathbb{HP}^\infty$ and cellular approximation (a map from a $\le3$-manifold into $\mathbb{HP}^\infty$ deforms into the $0$-skeleton, a point, since the first nontrivial cell of $\mathbb{HP}^\infty$ is in dimension $4$). The series replaces this by the generic-section argument above, which needs $M$ **compact** (for the finiteness and existence in the transversality theorem). Both give triviality; the non-compact case is not claimed here and is not used downstream.

---

# Cross-Field Exercise Suggestions

**Instantons on $S^4$ and the ADHM count.** The bundle $P_{\pi_k}$ over $S^4$ carries anti-self-dual connections whose moduli space has dimension $8k-3$ for $k\ge1$; the classification theorem is what licences indexing these moduli spaces by the single integer $k$. The application is non-obvious because the analytic moduli problem seems to depend on the full bundle geometry, yet its discrete label is exactly the clutching degree computed here.

**Spinors on spin four-manifolds.** On a closed spin four-manifold $X$ the positive spinor bundle $S^+$ is a rank-two complex bundle with structure group $SU(2)$; its Chern number is determined by the signature of $X$ through the index theorem. Recognising $S^+$ as an $SU(2)$-bundle and reading its invariant as a clutching degree connects representation-theoretic spinor data to the topology of $X$; the non-obvious step is the reduction of the spin representation's structure group to $SU(2)$ in dimension four.

**Skyrmions in nuclear physics.** A Skyrme field is a map $g\colon S^3\to SU(2)$ (spacetime compactified to $S^3$), and its baryon number is exactly the degree $\deg g=-W(g)$, computed by the same integral $\frac{1}{24\pi^2}\int\operatorname{tr}((g^{-1}dg)^{\wedge3})$. The theorem's winding identity is the mathematical content of baryon-number conservation; the application is non-obvious because the physical quantity is defined by a field-theoretic Lagrangian, not by bundle theory, yet it is the same topological degree.

---

# Bridges

- **The second Chern number as a curvature integral.** Chapter VI's [[Thm - Second Chern Number of an SU(2)-Bundle over a Closed Four-Manifold is the Clutching Degree]] proves $\frac1{8\pi^2}\int_X\operatorname{tr}(F_A\wedge F_A)=k(P)$ by gluing two local Chern–Simons primitives across $S=\partial D$; the boundary term is exactly $-\frac13\int_S\operatorname{tr}(\theta^{\wedge3})$, which by Lemma 3 is $8\pi^2\deg g$. The clutching degree of this page and the curvature integral of that page are the same integer.

- **The Chern–Simons functional.** Part (A) makes $SU(2)$-bundles over a closed oriented three-manifold trivial, so connections are $\mathfrak{su}(2)$-valued one-forms and the [[Def - Chern-Simons Functional|Chern–Simons functional]] is defined; its well-definedness modulo $\mathbb Z$ is the winding identity of this page transported to three dimensions, [[Thm - Gauge Variation of the Chern-Simons Functional]].

- **The quaternionic Hopf bundle.** The generator with $k=1$ is realised concretely by the quaternionic Hopf bundle $S^7\to S^4=\mathbb{HP}^1$ of [[Def - The Hopf Bundle]]; its clutching map is $q\mapsto q$, of degree $1$, so $k=1$ (or $-1$ with the opposite disc convention). This is the bundle Donaldson theory studies.

- **The winding form and the volume of $SU(2)$.** The constant $-24\pi^2=\int_{SU(2)}\operatorname{tr}(\theta^{\wedge3})$ is $-12\operatorname{Vol}(S^3)$; the factor $12$ is $3\cdot|\operatorname{tr}(E_1^2)|\cdot|\mathrm{structure\ constant}|=3\cdot2\cdot2$, and the volume $2\pi^2$ comes from [[Ex - Volume of the n-Sphere via the Volume Form]]. This ties the topological normalisation to Riemannian geometry.

---

# Unlocked by This

> [!tip] The Yang–Mills topological energy bound *(from Gauge Theory VII)*
> Once $k(P)$ is an integer invariant, the inequality $\mathcal{YM}(A)\ge8\pi^2|k(P)|$ follows, with equality for instantons; this is the **Yang–Mills energy identity and topological bound** of chapter VII.

> [!tip] Donaldson's theorem *(from Gauge Theory XIII)*
> The moduli space of anti-self-dual connections on the bundle with $k(P)=1$ over a definite four-manifold is the input to **Donaldson's diagonalisation theorem** (chapter XIII); existence of that bundle is part (C) of this page.
