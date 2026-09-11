---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - The Hopf Bundle"
  - "Thm - Sections of a Principal Bundle and Triviality"
  - "Thm - The Mayer-Vietoris Sequence"
  - "Thm - Homotopy Invariance of de Rham Cohomology"
  - "Def - de Rham Cohomology"
  - "Thm - Stokes' Theorem on Manifolds"
  - "Thm - Pull-Back Commutes with the Exterior Derivative"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, manifolds are smooth, Hausdorff and second countable, and "smooth" means $C^\infty$; $\Omega^p(X)$ denotes the space of smooth real $p$-forms on a manifold $X$. Lie groups act on principal bundles on the right, as fixed by the series conventions.

We fix an integer $n\geq1$ and write $m:=2n+1$, so that $m\geq3$. The relevant spaces are the odd sphere $S^{m}=S^{2n+1}=\{z\in\mathbb C^{n+1}:|z|=1\}$, complex projective space $\mathbb{CP}^n=(\mathbb C^{n+1}\setminus\{0\})/\mathbb C^\times$ (see [[Def - Complex Projective Space as a Quotient]]), the unit circle $U(1)=\{\lambda\in\mathbb C:|\lambda|=1\}$, and its underlying manifold the $1$-sphere $S^1$; as manifolds $U(1)=S^1$ literally, the same subset of $\mathbb C$. The map $\pi\colon S^{2n+1}\to\mathbb{CP}^n$, $\pi(z)=[z]$, with the right action $z\cdot\lambda=z\lambda$ and structure group $U(1)$, is the **Hopf bundle** ([[Def - The Hopf Bundle]]).

For a manifold $X$, $H^k_{\mathrm{dR}}(X)$ is its $k$-th de Rham cohomology ([[Def - de Rham Cohomology]]), the quotient $Z^k(X)/B^k(X)$ of closed $k$-forms (those $\alpha$ with $d\alpha=0$) by exact $k$-forms (those $\alpha=d\beta$); $[\alpha]$ denotes the class of a closed form. We repeatedly use that $H^0_{\mathrm{dR}}(X)$ is the space of locally constant functions, so $H^0_{\mathrm{dR}}(X)\cong\mathbb R^{c}$ where $c$ is the number of connected components of $X$; in particular $H^0_{\mathrm{dR}}(X)\cong\mathbb R$ when $X$ is connected. For a smooth map $F\colon X\to Y$, $F^*$ denotes both the pullback of forms $\Omega^\bullet(Y)\to\Omega^\bullet(X)$ and the induced map $H^\bullet_{\mathrm{dR}}(Y)\to H^\bullet_{\mathrm{dR}}(X)$ on cohomology; the two are compatible because pullback commutes with $d$ ([[Thm - Pull-Back Commutes with the Exterior Derivative]]). The projections of a product are $\operatorname{pr}_1\colon X\times Y\to X$ and $\operatorname{pr}_2\colon X\times Y\to Y$. The symbol $\cong$ without qualification means "diffeomorphic"; "isomorphic as bundles" is written out.

The **angle form** $\eta\in\Omega^1(S^1)$ is the restriction to $S^1\subset\mathbb R^2$ of the $1$-form $-y\,dx+x\,dy$, where $(x,y)$ are the standard coordinates of $\mathbb R^2$. It is a globally defined smooth $1$-form (although the angle $\theta$ itself is only a local coordinate on $S^1$), and along the parametrisation $\gamma(\theta)=(\cos\theta,\sin\theta)$ one has $\gamma^*\eta=d\theta$; this justifies the name.

> [!warning] Convention: method of proof differs from the source
> Bär (Example 2.2.16, p. 46) proves the $n=1$ case from the fundamental group: a global section would force $S^3\cong S^2\times S^1$, hence $\{e\}\cong\pi_1(S^3)\cong\pi_1(S^2)\times\pi_1(S^1)\cong\mathbb Z$, a contradiction. This series does not develop enough covering-space theory to compute $\pi_1(S^3)$ and $\pi_1(S^2\times S^1)$ with full rigour at this point, so we replace the argument by one in de Rham cohomology, which the vault has proved (Mayer–Vietoris and homotopy invariance). The de Rham argument works uniformly for every $n\geq1$, not only $n=1$, and yields the stronger conclusion that the two total spaces are not even diffeomorphic.

---

# Statement

> **Theorem (The Hopf bundle is nontrivial).** Fix $n\geq1$ and let $\pi\colon S^{2n+1}\to\mathbb{CP}^n$ be the Hopf bundle, a principal $U(1)$-bundle.
>
> **(a) Non-diffeomorphism.** The manifolds $S^{2n+1}$ and $\mathbb{CP}^n\times S^1$ are not diffeomorphic.
>
> **(b) No global section, hence nontrivial.** The Hopf bundle admits no global smooth section $s\colon\mathbb{CP}^n\to S^{2n+1}$ with $\pi\circ s=\operatorname{id}$. Equivalently, it is not isomorphic to the trivial principal $U(1)$-bundle $\mathbb{CP}^n\times U(1)\to\mathbb{CP}^n$.
>
> **(c) The classical case.** For $n=1$, using the diffeomorphism $\mathbb{CP}^1\cong S^2$, the theorem reads: $S^3$ is not diffeomorphic to $S^2\times S^1$, and the Hopf bundle $S^3\to S^2$ has no global section.

The three parts are logically nested: (a) is the substantive analytic fact, (b) is its bundle-theoretic consequence, and (c) is the specialisation that Bär states. We prove (a) directly by de Rham cohomology, deduce (b) from (a) through the sections-and-triviality theorem, and read off (c).

---

# Motivation

Bundle theory begins with the trivial bundle $M\times G$, the product of the base with the structure group, and the first question one must be able to answer is whether a given bundle is *really* something new or is only the product in disguise. If every bundle were trivial, the subject would collapse: connections would be globally defined $\mathfrak g$-valued forms, characteristic classes would all vanish, and there would be no obstruction to gauge-fixing. The whole apparatus of gauge theory — curvature as a measure of non-triviality, Chern numbers, instantons, the Seiberg–Witten invariants — exists precisely because bundles can fail to be products, and one must have at least one concrete example in hand to know that the failure is real rather than hypothetical.

The Hopf bundle $S^{2n+1}\to\mathbb{CP}^n$ is that first example, and this theorem is the statement that it genuinely fails to be a product. It is the smallest nontrivial principal bundle in the sense that matters: it has abelian structure group $U(1)$, its base and total space are the most familiar of manifolds, and its non-triviality can be detected by the crudest topological invariant, the first de Rham cohomology. Every later obstruction in the series — the degree of a line bundle over a surface, the first Chern class, the second Chern number of an $SU(2)$-bundle over a four-manifold — is a refinement of the phenomenon exhibited here. If one understands why $S^3$ cannot be $S^2\times S^1$, one understands in miniature why $c_1$ and $c_2$ are not always zero.

There is a second reason the result matters for what follows. By the sections-and-triviality theorem, a principal bundle is trivial exactly when it has a global section, and a section of the Hopf bundle would be a *global choice of phase*: a way of picking, continuously over all of $\mathbb{CP}^n$, one point of $\mathbb C^{n+1}$ on each complex line. The theorem says no such global choice exists. This is the geometric heart of the Aharonov–Bohm effect and of the impossibility of a global gauge in electromagnetism over a nontrivial configuration space; the phase can be fixed locally, never globally. The de Rham class we build to obstruct the section is, up to normalisation, the first Chern class of the bundle, so the proof is not merely an existence-of-obstruction argument but the first appearance of the invariant that classifies $U(1)$-bundles.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypothesis of the theorem is bare — one fixed bundle, the Hopf bundle — so the useful "source" question is: which apparently unrelated problems reduce to *this* non-triviality, so that the theorem, once proved, settles them? Each of the following is a disguised instance.

The first disguised source is **"is this odd sphere a product $B\times S^1$?"** whenever $B$ is presented as a quotient of the sphere by a free circle action. A free smooth action of $U(1)$ on $S^{2n+1}$ makes $S^{2n+1}\to S^{2n+1}/U(1)$ a principal $U(1)$-bundle by [[Thm - Free Proper Actions Give Principal Bundles|the free–proper theorem]] (the circle is compact, so a free action is automatically proper), and the same de Rham comparison — $H^1_{\mathrm{dR}}(S^{2n+1})=0$ against $H^1_{\mathrm{dR}}(B\times S^1)\neq0$ — shows the bundle is nontrivial and the sphere is not the product. The bridge $B\Rightarrow A$ is: "a free $U(1)$-action on a simply-connected-looking odd sphere" $\Rightarrow$ "a nontrivial principal $U(1)$-bundle whose total space has vanishing $H^1$". *Example problem:* the Hopf action's cousins, the lens-space quotients, and the question of whether $S^3$ can be a circle bundle over $S^2$ non-trivially, all route through here.

The second disguised source is **any claim that a total space carries no closed non-exact $1$-form**. Whenever one can prove $H^1_{\mathrm{dR}}(P)=0$ for the total space of a principal $S^1$-bundle $P\to B$ — for instance because $P$ is a high-dimensional sphere, or more generally because $P$ is simply connected in a setting where de Rham detects $\pi_1^{\mathrm{ab}}$ — the bundle cannot be a product with $S^1$, because the product would inherit the base circle's angle class. The non-obvious bridge is that the vanishing of a cohomology group of the *total* space forbids a product decomposition, a statement about the *base times fibre*. *Example problem:* showing that the unit tangent bundle of a surface of genus $\geq2$ is nontrivial by computing $H^1$ of its total space and comparing.

The third disguised source is **"no global phase" or "no global frame" problems**. A nowhere-vanishing section of the tautological line bundle $\mathcal O(-1)\to\mathbb{CP}^n$, a global unit-length section of the associated Hermitian line bundle, or a continuous global choice of eigenvector for a family of Hamiltonians parametrised by $\mathbb{CP}^n$ — each of these is exactly a global section of the Hopf bundle (via the associated-bundle identification $\mathcal O(-1)=S^{2n+1}\times_{U(1)}\mathbb C$, proved in §3.4). The bridge $B\Rightarrow A$ turns a physics or linear-algebra statement about global choices of phase into the bundle-theoretic statement "the Hopf bundle has a section". *Example problem:* the impossibility of a smooth global Berry phase gauge on the Bloch sphere $\mathbb{CP}^1$, which is precisely part (c).

**Targets (Output Amplification)**

The conclusion "no section" combines with further ingredients to give more.

Combine with **the classification of $U(1)$-bundles by the first Chern class** (§3.6). Non-triviality of the Hopf bundle upgrades, once $c_1^{\mathrm{top}}$ is available, to the computation $c_1^{\mathrm{top}}(\mathcal O(-1))=-[\omega_N]\neq0$ and $\deg\mathcal O(-1)=-1$ over $\mathbb{CP}^1$: the extra ingredient is the de Rham cohomology of $\mathbb{CP}^n$ (which we begin to build here, since the obstructing class descends from the base), and the payoff is that the Hopf bundle is not merely nontrivial but occupies a specific nonzero slot in the classification group.

Combine with **Chern–Weil theory** (chapter VI). The class we produce, $[\operatorname{pr}_2^*\eta]$, is the pullback of the generator of $H^1_{\mathrm{dR}}(S^1)$; transported to the base through curvature, it becomes $\big[\tfrac{i}{2\pi}F_A\big]=c_1$ of the associated line bundle. The extra ingredient is a connection $A$ on the bundle and the Chern–Weil homomorphism; the payoff is the integral formula $\int_{\mathbb{CP}^1}c_1(\mathcal O(-1))=-1$, a quantitative refinement of "nontrivial".

Combine with **the hairy-ball theorem** (§3.5). For $n=1$ the non-triviality of the Hopf bundle is equivalent, through the frame bundle, to the non-existence of a nowhere-vanishing vector field on $S^2$: the extra ingredient is the identification of the relevant bundle over $S^2$ with a frame bundle, and the payoff is a third, independent proof of the same fact, cross-checking the cohomological one given here.

---

# Why Is It True

Set the formal machinery aside and picture the two candidate spaces. On the right stands $\mathbb{CP}^n\times S^1$, a product; on it there is an unmistakable closed $1$-form, the angle form of the circle factor, $\alpha=\operatorname{pr}_2^*\eta$. This form is closed but not exact, and the way to see it is to run once around a circle $\{x_0\}\times S^1$: the integral of $\alpha$ around that loop is the length in angle of one full turn, namely $2\pi$, whereas the integral of any exact form around a loop is zero (an exact form integrates against the boundary, and a loop has no boundary). So the product remembers its circle: its first cohomology is not zero.

On the left stands the odd sphere $S^{2n+1}$ with $2n+1\geq3$. A sphere of dimension at least two has no closed non-exact $1$-form at all — every closed $1$-form on it is the differential of a function. Intuitively, the sphere is "$1$-connected enough" that there are no interesting loops to integrate over: any loop can be filled in by a disc, and Stokes then forces every closed $1$-form to integrate to zero around it, which is the integral criterion for exactness. Cohomologically, $H^1_{\mathrm{dR}}(S^{2n+1})=0$.

Now the contradiction writes itself. A diffeomorphism between two manifolds carries closed forms to closed forms and exact to exact, so it induces an isomorphism of their de Rham cohomologies. But one side has $H^1=0$ and the other has $H^1\neq0$, and no isomorphism relates the zero vector space to a nonzero one. Therefore the two manifolds are not diffeomorphic. Finally, a global section of the Hopf bundle would trivialise it — a principal bundle with a section is a product — and a product is exactly what part (a) has just excluded.

> **Mechanism in one sentence.** A product with a circle always carries the circle's angle class in its first cohomology, an odd sphere of dimension at least three carries no first cohomology at all, and a diffeomorphism cannot destroy a cohomology class — so the Hopf sphere cannot be the product, and therefore its bundle has no section.

---

# What Makes This Hard

The one genuinely non-obvious move is to *pull the obstruction out of the total space rather than the base*. It is tempting to look for the obstruction on $\mathbb{CP}^n$, where the first Chern class eventually lives; but at this point in the development $c_1$ has not been built, and the clean argument instead compares the two candidate total spaces directly by their first cohomology. The common error is to try to prove non-triviality by "there is no global section" attacked head-on — writing down a would-be section and hoping it fails somewhere — which never terminates, because a single formula cannot see a global obstruction. The correct logic inverts this: assume triviality, deduce a diffeomorphism to a product, and derive a numerical contradiction from an integral. A second, subtler pitfall is dimensional: the vanishing $H^1_{\mathrm{dR}}(S^m)=0$ needs $m\geq2$ (so that the equatorial sphere $S^{m-1}$ used in Mayer–Vietoris is connected); for $m=1$ it is false, $H^1_{\mathrm{dR}}(S^1)\cong\mathbb R$, and indeed the "Hopf bundle" $S^1\to\mathbb{CP}^0=\{*\}$ over a point *is* trivial. The hypothesis $n\geq1$, hence $m=2n+1\geq3$, is exactly what keeps the argument on the right side of this line.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Prove the two total spaces have different first de Rham cohomology — nonzero for the product, zero for the odd sphere — and conclude they are not diffeomorphic; then deduce there is no section, because a section would make the sphere a product.

**Subgoal decomposition:**

1. **The product has $H^1\neq0$.** Exhibit a closed, non-exact $1$-form on $\mathbb{CP}^n\times S^1$.
   - *Hint:* Pull the angle form $\eta$ back along $\operatorname{pr}_2$; integrate over one circle fibre $\{x_0\}\times S^1$ and use Stokes to kill any exact form.
   - *Why needed:* It supplies a nonzero cohomology class that the other side lacks.

2. **The odd sphere has $H^1=0$.** Prove $H^1_{\mathrm{dR}}(S^m)=0$ for all $m\geq2$.
   - *Hint:* Cover $S^m$ by the complements of the two poles; each is diffeomorphic to $\mathbb R^m$ (stereographic) hence contractible, and their intersection retracts to the equatorial $S^{m-1}$, which is connected for $m\geq2$. Read $H^1$ off the Mayer–Vietoris sequence.
   - *Why needed:* It supplies the vanishing group that clashes with subgoal 1.

3. **Cohomology is a diffeomorphism invariant.** A diffeomorphism induces an isomorphism on de Rham cohomology.
   - *Hint:* Pullback commutes with $d$, so it descends to cohomology; functoriality makes $(F^{-1})^*$ the inverse of $F^*$.
   - *Why needed:* It converts "different $H^1$" into "not diffeomorphic".

4. **From non-diffeomorphism to no section.** A global section would trivialise the bundle and hence produce a diffeomorphism to the product, contradicting subgoals 1–3.
   - *Hint:* Use the sections-and-triviality theorem: section $\Leftrightarrow$ triviality $\Rightarrow$ (equivariant, in particular ordinary) diffeomorphism onto $\mathbb{CP}^n\times U(1)=\mathbb{CP}^n\times S^1$.
   - *Why needed:* It delivers the bundle-theoretic conclusion (b) from the manifold statement (a).

---

# Lemma Decomposition

> [!note]- Lemma 1: The product $\mathbb{CP}^n\times S^1$ has nonvanishing first de Rham cohomology
> **Statement:** For every $n\geq0$ the closed $1$-form $\alpha:=\operatorname{pr}_2^*\eta\in\Omega^1(\mathbb{CP}^n\times S^1)$, where $\eta\in\Omega^1(S^1)$ is the angle form and $\operatorname{pr}_2\colon\mathbb{CP}^n\times S^1\to S^1$ the projection, is not exact. Consequently $H^1_{\mathrm{dR}}(\mathbb{CP}^n\times S^1)\neq0$.
>
> **Hint:** Restrict $\alpha$ to one circle $\{x_0\}\times S^1$, on which $\operatorname{pr}_2$ is the identity, and integrate; if $\alpha=df$ the restriction is exact and integrates to $0$ by Stokes, contradicting $\int_{S^1}\eta=2\pi$.
>
> **Why needed:** It is the nonzero cohomology class that the odd sphere will be shown to lack.
>
> > [!note]- Full proof
> > **Goal.** We produce a closed $1$-form on $X:=\mathbb{CP}^n\times S^1$ that is not exact, which by definition of $H^1_{\mathrm{dR}}(X)=Z^1(X)/B^1(X)$ shows $H^1_{\mathrm{dR}}(X)\neq0$.
> >
> > **Step 1 — the angle form is closed with integral $2\pi$.** The angle form $\eta=(-y\,dx+x\,dy)|_{S^1}$ is a smooth $1$-form on the $1$-manifold $S^1$; since $\Omega^2(S^1)=0$ on a $1$-manifold, $d\eta=0$ (there are no nonzero $2$-forms), so $\eta$ is closed. Along the diffeomorphism $\gamma\colon[0,2\pi]\to S^1$, $\gamma(\theta)=(\cos\theta,\sin\theta)$ (an orientation-preserving parametrisation covering $S^1$ once), we compute the pullback
> > $$\gamma^*\eta=-\sin\theta\,d(\cos\theta)+\cos\theta\,d(\sin\theta)=-\sin\theta(-\sin\theta\,d\theta)+\cos\theta(\cos\theta\,d\theta)\qquad\text{(chain rule)}$$
> > $$=(\sin^2\theta+\cos^2\theta)\,d\theta=d\theta\qquad\text{(Pythagorean identity)}.$$
> > Hence, by the definition of the integral of a $1$-form over the oriented curve $S^1$ ([[Thm - Integration is Well-Defined on Oriented Manifolds|integration is well-defined on oriented manifolds]], so the value is independent of the parametrisation),
> > $$\int_{S^1}\eta=\int_0^{2\pi}\gamma^*\eta=\int_0^{2\pi}d\theta=2\pi\qquad\text{(fundamental theorem of calculus)}.$$
> >
> > **Step 2 — $\alpha$ is closed.** With $\alpha=\operatorname{pr}_2^*\eta$,
> > $$d\alpha=d(\operatorname{pr}_2^*\eta)=\operatorname{pr}_2^*(d\eta)=\operatorname{pr}_2^*0=0\qquad\text{(pullback commutes with }d\text{, and }d\eta=0\text{ from Step 1)},$$
> > so $\alpha\in Z^1(X)$; the interchange of $d$ and $\operatorname{pr}_2^*$ is [[Thm - Pull-Back Commutes with the Exterior Derivative|the theorem that pullback commutes with the exterior derivative]].
> >
> > **Step 3 — restriction to a circle recovers $\eta$.** Fix any point $x_0\in\mathbb{CP}^n$ and let $j\colon S^1\to X$, $j(\lambda)=(x_0,\lambda)$, be the smooth embedding of the fibre $\{x_0\}\times S^1$. Then $\operatorname{pr}_2\circ j=\operatorname{id}_{S^1}$, so
> > $$j^*\alpha=j^*\operatorname{pr}_2^*\eta=(\operatorname{pr}_2\circ j)^*\eta=\operatorname{id}_{S^1}^*\eta=\eta\qquad\text{(functoriality of pullback, }(\operatorname{pr}_2\circ j)^*=j^*\operatorname{pr}_2^*).$$
> >
> > **Step 4 — non-exactness by contradiction.** Suppose, for contradiction, that $\alpha$ were exact, $\alpha=df$ for some $f\in C^\infty(X)$. Then
> > $$\eta=j^*\alpha=j^*(df)=d(j^*f)=d(f\circ j)\qquad\text{(Step 3; pullback commutes with }d\text{)},$$
> > so $\eta$ would be the differential of the smooth function $f\circ j\colon S^1\to\mathbb R$. Integrating over the closed $1$-manifold $S^1$ (which has empty boundary, $\partial S^1=\varnothing$), [[Thm - Stokes' Theorem on Manifolds|Stokes' theorem]] gives
> > $$\int_{S^1}\eta=\int_{S^1}d(f\circ j)=\int_{\partial S^1}(f\circ j)=\int_\varnothing(f\circ j)=0.$$
> > This contradicts $\int_{S^1}\eta=2\pi\neq0$ from Step 1. The named contradiction is between the two computed values of $\int_{S^1}\eta$, one equal to $2\pi$ and one equal to $0$.
> >
> > **Conclusion.** No such $f$ exists, so $\alpha$ is closed but not exact; therefore $[\alpha]\neq0$ in $H^1_{\mathrm{dR}}(X)$, and $H^1_{\mathrm{dR}}(\mathbb{CP}^n\times S^1)\neq0$. $\blacksquare$

> [!note]- Lemma 2: The first de Rham cohomology of a sphere of dimension at least two vanishes
> **Statement:** For every integer $m\geq2$, $H^1_{\mathrm{dR}}(S^m)=0$. In particular $H^1_{\mathrm{dR}}(S^{2n+1})=0$ for every $n\geq1$.
>
> **Hint:** Apply Mayer–Vietoris to $U=S^m\setminus\{N\}$ and $V=S^m\setminus\{S\}$, both diffeomorphic to $\mathbb R^m$ (hence contractible) with $U\cap V\simeq S^{m-1}$ (connected for $m\geq2$); the map $H^0(U)\oplus H^0(V)\to H^0(U\cap V)$ is surjective, so $H^1(S^m)$, its cokernel, is $0$.
>
> **Why needed:** It is the vanishing group that, set against Lemma 1, forbids the diffeomorphism.
>
> > [!note]- Full proof
> > **Goal.** For $m\geq2$ we show every closed $1$-form on $S^m$ is exact, i.e. $H^1_{\mathrm{dR}}(S^m)=0$, by locating $H^1_{\mathrm{dR}}(S^m)$ in the Mayer–Vietoris sequence of a two-set cover and showing the relevant map is a cokernel that vanishes.
> >
> > **Step 0 — the cover and its pieces.** Let $N=(0,\dots,0,1)$ and $S=(0,\dots,0,-1)$ be the north and south poles of $S^m\subset\mathbb R^{m+1}$, and set the open cover
> > $$U:=S^m\setminus\{N\},\qquad V:=S^m\setminus\{S\},\qquad U\cup V=S^m,\qquad U\cap V=S^m\setminus\{N,S\}.$$
> > Stereographic projection from $N$,
> > $$\sigma_N\colon U\longrightarrow\mathbb R^m,\qquad \sigma_N(x_1,\dots,x_{m+1})=\frac{1}{1-x_{m+1}}(x_1,\dots,x_m),$$
> > is a diffeomorphism (its smooth inverse is the standard inverse stereographic formula); likewise $\sigma_S$ from $S$ is a diffeomorphism $V\to\mathbb R^m$. Since $\mathbb R^m$ is convex it is contractible ([[Def - Homotopy Equivalence and Contractible Space|contractible space]]), so $U$ and $V$ are contractible.
> >
> > **Step 1 — cohomology of $U$ and $V$.** By [[Thm - Homotopy Invariance of de Rham Cohomology|homotopy invariance of de Rham cohomology]] — homotopy-equivalent manifolds have isomorphic de Rham cohomology, and a contractible manifold is homotopy-equivalent to a point — we have
> > $$H^0_{\mathrm{dR}}(U)\cong H^0_{\mathrm{dR}}(V)\cong H^0_{\mathrm{dR}}(\mathrm{pt})=\mathbb R,\qquad H^1_{\mathrm{dR}}(U)=H^1_{\mathrm{dR}}(V)=H^1_{\mathrm{dR}}(\mathrm{pt})=0.$$
> >
> > **Step 2 — the intersection retracts to the equator.** Transport $U\cap V$ through the diffeomorphism $\sigma_N$; since $\sigma_N(S)=0$, we get $\sigma_N(U\cap V)=\mathbb R^m\setminus\{0\}$. The map
> > $$R\colon(\mathbb R^m\setminus\{0\})\times[0,1]\to\mathbb R^m\setminus\{0\},\qquad R(w,t)=(1-t)\,w+t\,\frac{w}{|w|},$$
> > is smooth and nowhere zero (for $t\in[0,1]$ it is a positive combination $\big((1-t)+t/|w|\big)w$ of $w$ with a positive coefficient, hence nonzero), so it is a deformation retraction of $\mathbb R^m\setminus\{0\}$ onto the unit sphere $S^{m-1}$. Thus $U\cap V\simeq\mathbb R^m\setminus\{0\}\simeq S^{m-1}$. Because $m\geq2$, the sphere $S^{m-1}$ is connected, so by homotopy invariance
> > $$H^0_{\mathrm{dR}}(U\cap V)\cong H^0_{\mathrm{dR}}(S^{m-1})=\mathbb R\qquad(\text{one connected component}).$$
> >
> > **Step 3 — the Mayer–Vietoris segment.** [[Thm - The Mayer-Vietoris Sequence|The Mayer–Vietoris sequence]] for the cover $S^m=U\cup V$ is the long exact sequence
> > $$\cdots\to H^{k}_{\mathrm{dR}}(S^m)\xrightarrow{(i_U^*,\,i_V^*)}H^{k}_{\mathrm{dR}}(U)\oplus H^{k}_{\mathrm{dR}}(V)\xrightarrow{\;\rho\;}H^{k}_{\mathrm{dR}}(U\cap V)\xrightarrow{\;\delta\;}H^{k+1}_{\mathrm{dR}}(S^m)\to\cdots,$$
> > where $i_U,i_V$ are the inclusions of $U,V$ into $S^m$, $\rho=j_U^*-j_V^*$ is the difference of the restriction maps to $U\cap V$, and $\delta$ is the connecting homomorphism. We use the portion around $H^1$:
> > $$H^0_{\mathrm{dR}}(U)\oplus H^0_{\mathrm{dR}}(V)\xrightarrow{\;\rho\;}H^0_{\mathrm{dR}}(U\cap V)\xrightarrow{\;\delta\;}H^1_{\mathrm{dR}}(S^m)\xrightarrow{(i_U^*,\,i_V^*)}H^1_{\mathrm{dR}}(U)\oplus H^1_{\mathrm{dR}}(V).$$
> >
> > **Step 4 — the right end vanishes, so $\delta$ is onto.** By Step 1 the last term $H^1_{\mathrm{dR}}(U)\oplus H^1_{\mathrm{dR}}(V)=0$. Exactness at $H^1_{\mathrm{dR}}(S^m)$ says $\operatorname{im}\delta=\ker\big((i_U^*,i_V^*)\big)=H^1_{\mathrm{dR}}(S^m)$ (the kernel of a map into the zero space is everything), so $\delta$ is surjective. Exactness at $H^0_{\mathrm{dR}}(U\cap V)$ says $\ker\delta=\operatorname{im}\rho$. Combining, the first isomorphism theorem for the linear map $\delta$ gives
> > $$H^1_{\mathrm{dR}}(S^m)=\operatorname{im}\delta\cong H^0_{\mathrm{dR}}(U\cap V)/\ker\delta=H^0_{\mathrm{dR}}(U\cap V)/\operatorname{im}\rho=\operatorname{coker}\rho.$$
> >
> > **Step 5 — $\rho$ is surjective.** Recall $H^0_{\mathrm{dR}}$ is the space of locally constant functions ([[Def - de Rham Cohomology]]). As $U$ and $V$ are connected, $H^0_{\mathrm{dR}}(U)=\mathbb R\cdot 1_U$ and $H^0_{\mathrm{dR}}(V)=\mathbb R\cdot 1_V$, the constant functions; as $U\cap V$ is connected (Step 2, using $m\geq2$), $H^0_{\mathrm{dR}}(U\cap V)=\mathbb R\cdot 1_{U\cap V}$. On constants the restriction maps are the identity on the value, so
> > $$\rho(a\cdot 1_U,\;b\cdot 1_V)=(a\cdot 1_U)|_{U\cap V}-(b\cdot 1_V)|_{U\cap V}=(a-b)\,1_{U\cap V}.$$
> > Given any $c\cdot 1_{U\cap V}\in H^0_{\mathrm{dR}}(U\cap V)$, take $a=c$, $b=0$; then $\rho(c\cdot 1_U,0)=c\cdot 1_{U\cap V}$. Hence $\rho$ is surjective, and $\operatorname{coker}\rho=0$.
> >
> > **Conclusion.** By Steps 4 and 5, $H^1_{\mathrm{dR}}(S^m)\cong\operatorname{coker}\rho=0$ for every $m\geq2$. In particular, since $m=2n+1\geq3\geq2$ for $n\geq1$, we have $H^1_{\mathrm{dR}}(S^{2n+1})=0$. $\blacksquare$

> [!note]- Lemma 3: A diffeomorphism induces an isomorphism on de Rham cohomology
> **Statement:** If $F\colon X\to Y$ is a diffeomorphism of smooth manifolds, then the induced map $F^*\colon H^k_{\mathrm{dR}}(Y)\to H^k_{\mathrm{dR}}(X)$ is a linear isomorphism for every $k$, with inverse $(F^{-1})^*$.
>
> **Hint:** Pullback commutes with $d$, so $F^*$ descends to cohomology; functoriality $(G\circ F)^*=F^*\circ G^*$ and $\operatorname{id}^*=\operatorname{id}$ then make $(F^{-1})^*$ a two-sided inverse.
>
> **Why needed:** It converts the numerical discrepancy of Lemmas 1 and 2 into the statement that the two manifolds are not diffeomorphic.
>
> > [!note]- Full proof
> > **Goal.** We show $F^*$ is well-defined on cohomology and has $(F^{-1})^*$ as a two-sided inverse.
> >
> > **Step 1 — $F^*$ descends to cohomology.** For any smooth map $F$, pullback commutes with the exterior derivative, $F^*(d\beta)=d(F^*\beta)$ ([[Thm - Pull-Back Commutes with the Exterior Derivative]]). Hence $F^*$ sends closed forms to closed forms (if $d\beta=0$ then $d(F^*\beta)=F^*(d\beta)=0$) and exact forms to exact forms (if $\beta=d\gamma$ then $F^*\beta=F^*d\gamma=d(F^*\gamma)$). Therefore $F^*$ maps $Z^k(Y)$ into $Z^k(X)$ and $B^k(Y)$ into $B^k(X)$, so it induces a well-defined linear map on the quotients $F^*\colon H^k_{\mathrm{dR}}(Y)\to H^k_{\mathrm{dR}}(X)$, $[\beta]\mapsto[F^*\beta]$.
> >
> > **Step 2 — functoriality.** Pullback is contravariantly functorial: $(G\circ F)^*=F^*\circ G^*$ for composable smooth maps (this is the chain rule for pullback of forms), and $\operatorname{id}_X^*=\operatorname{id}$ on forms, hence on cohomology.
> >
> > **Step 3 — inversion.** Since $F$ is a diffeomorphism, $F^{-1}$ is smooth and $F\circ F^{-1}=\operatorname{id}_Y$, $F^{-1}\circ F=\operatorname{id}_X$. Applying Step 2,
> > $$(F^{-1})^*\circ F^*=(F\circ F^{-1})^*=\operatorname{id}_Y^*=\operatorname{id}_{H^k_{\mathrm{dR}}(Y)},\qquad F^*\circ(F^{-1})^*=(F^{-1}\circ F)^*=\operatorname{id}_X^*=\operatorname{id}_{H^k_{\mathrm{dR}}(X)}.$$
> > So $F^*$ is a linear bijection with inverse $(F^{-1})^*$.
> >
> > **Conclusion.** $F^*\colon H^k_{\mathrm{dR}}(Y)\to H^k_{\mathrm{dR}}(X)$ is an isomorphism for every $k$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Fix $n\geq1$ and write $m=2n+1\geq3$. Let $\pi\colon S^{2n+1}\to\mathbb{CP}^n$ be the Hopf bundle, the principal $U(1)$-bundle with total space $S^{2n+1}$, base $\mathbb{CP}^n$, projection $\pi(z)=[z]$ and right action $z\cdot\lambda=z\lambda$ ([[Def - The Hopf Bundle]]).
>
> **Part I — $S^{2n+1}$ and $\mathbb{CP}^n\times S^1$ are not diffeomorphic (claim (a)).**
>
> **Step 0 — the two cohomology groups.** By Lemma 1, $H^1_{\mathrm{dR}}(\mathbb{CP}^n\times S^1)\neq0$, witnessed by the closed non-exact form $\alpha=\operatorname{pr}_2^*\eta$. By Lemma 2, since $m=2n+1\geq3\geq2$, $H^1_{\mathrm{dR}}(S^{2n+1})=0$.
>
> **Step 1 — assume a diffeomorphism and reach a contradiction.** Suppose, for contradiction, that there is a diffeomorphism $F\colon S^{2n+1}\to\mathbb{CP}^n\times S^1$. By Lemma 3 applied with $X=S^{2n+1}$ and $Y=\mathbb{CP}^n\times S^1$, the induced map
> $$F^*\colon H^1_{\mathrm{dR}}(\mathbb{CP}^n\times S^1)\longrightarrow H^1_{\mathrm{dR}}(S^{2n+1})$$
> is a linear isomorphism. Its domain is nonzero (Step 0, Lemma 1) and its codomain is the zero space (Step 0, Lemma 2). But a linear isomorphism from a vector space $W$ onto $\{0\}$ forces $W=0$ (it is injective, so $\dim W\leq\dim\{0\}=0$). This contradicts $H^1_{\mathrm{dR}}(\mathbb{CP}^n\times S^1)\neq0$. The named contradiction is between "$H^1_{\mathrm{dR}}(\mathbb{CP}^n\times S^1)$ is isomorphic to $0$" and "$H^1_{\mathrm{dR}}(\mathbb{CP}^n\times S^1)\neq0$".
>
> **Step 2 — conclude Part I.** No diffeomorphism $F$ exists; therefore $S^{2n+1}$ is not diffeomorphic to $\mathbb{CP}^n\times S^1$. This proves (a).
>
> **Part II — the Hopf bundle has no global section and is nontrivial (claim (b)).**
>
> **Step 3 — a section would trivialise the bundle.** Suppose, for contradiction, that the Hopf bundle admitted a global smooth section $s\colon\mathbb{CP}^n\to S^{2n+1}$ with $\pi\circ s=\operatorname{id}_{\mathbb{CP}^n}$. By [[Thm - Sections of a Principal Bundle and Triviality|the sections-and-triviality theorem]] — for a principal $G$-bundle $P\to M$, $P$ is trivial if and only if it admits a global section, the trivialisation being the $G$-equivariant diffeomorphism $\Psi\colon P\to M\times G$, $\Psi^{-1}(u,g)=s(u)\cdot g$ — the Hopf bundle is trivial: there is a $U(1)$-equivariant diffeomorphism
> $$\Psi\colon S^{2n+1}\longrightarrow\mathbb{CP}^n\times U(1),\qquad \Psi^{-1}(u,\lambda)=s(u)\cdot\lambda .$$
>
> **Step 4 — a trivialisation is in particular a diffeomorphism to the product.** The map $\Psi$ is, forgetting its equivariance, a diffeomorphism of smooth manifolds $S^{2n+1}\to\mathbb{CP}^n\times U(1)$. As manifolds $U(1)=S^1$ (the same unit circle in $\mathbb C$), so $\mathbb{CP}^n\times U(1)=\mathbb{CP}^n\times S^1$, and $\Psi$ is a diffeomorphism $S^{2n+1}\cong\mathbb{CP}^n\times S^1$. This contradicts Part I (Step 2). The named contradiction is between the existence of $\Psi$ and the non-existence of any diffeomorphism $S^{2n+1}\to\mathbb{CP}^n\times S^1$.
>
> **Step 5 — conclude Part II.** Hence the Hopf bundle admits no global section. By the sections-and-triviality theorem (the "only if" direction, restated in Step 3), a principal bundle with no global section is not trivial; therefore the Hopf bundle is not isomorphic to $\mathbb{CP}^n\times U(1)$ as a principal $U(1)$-bundle. This proves (b).
>
> **Part III — the classical case $n=1$ (claim (c)).**
>
> **Step 6 — specialise.** For $n=1$ the base is $\mathbb{CP}^1$, and [[Thm - CP^1 is Diffeomorphic to S^2 via the Hopf Map|ℂP¹ is diffeomorphic to S²]]; call the diffeomorphism $\Phi\colon\mathbb{CP}^1\to S^2$. Composing with $\Phi\times\operatorname{id}_{S^1}$ turns any diffeomorphism $S^3\cong\mathbb{CP}^1\times S^1$ into one $S^3\cong S^2\times S^1$, and conversely; so by (a) with $n=1$, $S^3$ is not diffeomorphic to $S^2\times S^1$. By (b) with $n=1$, the Hopf bundle $S^3\to\mathbb{CP}^1\cong S^2$ has no global section. This proves (c).
>
> Combining Parts I, II and III proves the theorem for every $n\geq1$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Berry phase and the impossibility of a global gauge (quantum mechanics).** Consider a family of quantum Hamiltonians parametrised by the projective space of states $\mathbb{CP}^1$, with a nondegenerate ground state whose ray traces out the tautological line $\mathcal O(-1)$. A smooth global choice of normalised ground-state vector is a global section of the Hopf bundle. The theorem applies because that bundle is exactly $S^3\to S^2$, and it is non-obvious to a physicist that the local freedom to fix the phase can never be globalised — the Berry phase around a loop enclosing the degeneracy is the integral of the connection whose curvature is the obstructing class built here.

**Circle actions and free quotients (dynamical systems / Lie theory).** Take any smooth free action of $U(1)$ on a compact odd-dimensional sphere $S^{2n+1}$; the orbit space is a manifold and the quotient map is a principal $U(1)$-bundle. The theorem's method — compare $H^1$ of the total space with $H^1$ of "base times circle" — shows the bundle is nontrivial whenever the total space is a sphere of dimension $\geq3$. The step that repays thought is verifying that the action being free and the group being compact are exactly the hypotheses that make the quotient a principal bundle at all, before non-triviality is even a meaningful question.

**Line bundles on Riemann surfaces (complex geometry).** Restrict the tautological bundle to a projective line inside $\mathbb{CP}^n$ and ask whether the resulting holomorphic line bundle on $\mathbb{CP}^1$ is holomorphically, or even smoothly, trivial. The theorem, through the associated-bundle identification, says it is not even smoothly trivial. This is non-obvious because holomorphic and smooth triviality are usually very different questions, yet here the crude smooth obstruction already suffices, and it foreshadows the degree/first-Chern-number classification of line bundles over surfaces in §3.6.

---

# Bridges

- **[[Thm - Sections of a Principal Bundle and Triviality|Sections and triviality]]** — the hinge between the two halves of the proof. That theorem turns the manifold-level statement "$S^{2n+1}$ is not a product" into the bundle-level statement "the Hopf bundle has no section", by the equivalence *section $\Leftrightarrow$ triviality $\Leftrightarrow$ existence of an equivariant diffeomorphism to $M\times G$*. Without it, non-diffeomorphism and non-triviality would be separate facts; with it, they are the same fact read two ways.

- **[[Thm - The Mayer-Vietoris Sequence|Mayer–Vietoris]] and [[Thm - Homotopy Invariance of de Rham Cohomology|homotopy invariance]]** — the two computational engines. Covering the sphere by two contractible pieces glued along an equatorial sphere, and knowing that contractible pieces carry only their zeroth cohomology, reduces $H^1(S^m)$ to a single cokernel of constants. This exact pattern, run inductively over dimension, computes the whole cohomology ring of spheres and, in §3.6, of $\mathbb{CP}^n$; the present lemma is its first instance.

- **The first Chern class (§3.6 and chapter VI).** The obstructing class $[\operatorname{pr}_2^*\eta]$ is, transported to the base by a connection, a multiple of $c_1$ of the associated line bundle. The construction here — find a closed form that integrates nontrivially over a circle — becomes, one dimension up, "find a closed $2$-form that integrates nontrivially over $\mathbb{CP}^1$", which is the definition of the degree of a line bundle over a surface. The Hopf bundle's non-triviality is the seed of the entire Chern-class classification.

- **The hairy-ball theorem ([[Thm - Hairy Ball Theorem|§3.5]]).** For $n=1$ the same non-triviality is equivalent to the impossibility of combing $S^2$: a section of the relevant $SO(2)$-frame bundle would be a nowhere-vanishing vector field. The two proofs — cohomological here, degree-theoretic there — are independent, and their agreement is a consistency check on the machinery. The exercise **[[Ex - The Hopf Bundle is Nontrivial via the Winding Number of its Transition Function]]** gives yet a third route, through the winding number of the transition function $z/|z|$.

---

# Unlocked by This

> [!tip] The first nontrivial principal bundle *(from Gauge Theory)*
> With this result the series has a concrete bundle that is not a product, so the notions of connection, curvature, and characteristic class have something to measure. Every later obstruction — **degree of a line bundle over a surface**, **first Chern class**, **second Chern number of an $SU(2)$-bundle** — refines the phenomenon proved here.

> [!tip] Cohomology as a diffeomorphism (indeed homotopy) invariant *(from Differential Topology)*
> Lemma 3 is the general principle that de Rham cohomology cannot distinguish diffeomorphic manifolds and, by homotopy invariance, cannot distinguish homotopy-equivalent ones. It is the standard tool for proving two manifolds are *not* the same: compute an invariant on each and compare. See [[Thm - Homotopy Invariance of de Rham Cohomology]].
