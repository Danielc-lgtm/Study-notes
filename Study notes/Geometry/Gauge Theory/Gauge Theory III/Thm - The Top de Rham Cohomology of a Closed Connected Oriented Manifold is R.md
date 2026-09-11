---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - de Rham Cohomology"
  - "Def - Orientation of a Smooth Manifold"
  - "Thm - Stokes' Theorem on Manifolds"
  - "Thm - Integration is Well-Defined on Oriented Manifolds"
  - "Thm - Change of Variables for Integration on Manifolds"
  - "Thm - The Poincaré Lemma on a Star-Shaped Region"
  - "Thm - Existence of Smooth Partitions of Unity"
  - "Thm - Existence of Smooth Bump Functions"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $N$ is a smooth manifold that is **closed** — compact and without boundary, $\partial N=\varnothing$ — **connected**, and **oriented**, of dimension $n\ge 1$. The word "closed" is used here in its topological-manifold sense (compact, no boundary); a differential form that satisfies $d\omega=0$ is called a *closed form*, and the two uses are kept apart by always writing "closed form" for the second. An **orientation** of $N$ is a choice of a connected component of the set of nowhere-vanishing $n$-forms modulo positive functions, equivalently an equivalence class of oriented atlases; see [[Def - Orientation of a Smooth Manifold|orientation of a smooth manifold]]. We write $\Omega^p(N)=\Gamma(\Lambda^pT^*N)$ for the smooth $p$-forms and $\Omega^p_c(U)$ for those with compact support inside an open set $U$; the exterior derivative is $d\colon\Omega^p\to\Omega^{p+1}$ with $d\circ d=0$.

The **de Rham cohomology** of $N$ is $H^p_{dR}(N)=\ker\big(d\colon\Omega^p(N)\to\Omega^{p+1}(N)\big)\big/\operatorname{im}\big(d\colon\Omega^{p-1}(N)\to\Omega^p(N)\big)$; a class $[\omega]$ is represented by a closed form $\omega$, and $[\omega]=0$ means $\omega$ is exact, $\omega=d\eta$ for some $\eta\in\Omega^{p-1}(N)$. See [[Def - de Rham Cohomology|de Rham cohomology]]. In top degree $p=n$ every form is closed automatically, because $\Omega^{n+1}(N)=0$, so $H^n_{dR}(N)=\Omega^n(N)/d\Omega^{n-1}(N)$.

The **integral** $\int_N\colon\Omega^n(N)\to\mathbb R$ of a compactly supported top form is defined, independently of the choice of oriented atlas and subordinate partition of unity, by [[Thm - Integration is Well-Defined on Oriented Manifolds|the theorem that integration is well-defined on oriented manifolds]]; on a closed $N$ every $n$-form is compactly supported, so $\int_N$ is defined on all of $\Omega^n(N)$. An **oriented coordinate ball** is an open set $B\subset N$ together with an orientation-preserving diffeomorphism $\varphi\colon B\to\mathbb R^n$ (equivalently onto an open Euclidean ball); on $\mathbb R^n$ we use standard coordinates $(x^1,\dots,x^n)$, the standard orientation, and the volume form $dV=dx^1\wedge\cdots\wedge dx^n$, and $\int_{\mathbb R^n}f\,dV$ denotes the ordinary Lebesgue integral of $f\in C^\infty_c(\mathbb R^n)$.

A form $\alpha\in\Omega^{p}_c(U)$ supported in an open $U\subset N$ is silently identified with its **extension by zero** to $N$, which is smooth because $\alpha$ vanishes on a neighbourhood of $\partial U$ inside $N$; extension by zero commutes with $d$.

The symbol registry for the chapter is on the parent page [[Gauge Theory III — Fibre Bundles, Principal Bundles, and Associated Bundles]].

---

# Statement

> **Theorem (top de Rham cohomology of a closed oriented manifold).** Let $N$ be a closed, connected, oriented smooth manifold of dimension $n\ge 1$. Then the linear map
> $$\textstyle\int_N\colon H^n_{dR}(N)\longrightarrow\mathbb R,\qquad [\omega]\longmapsto\int_N\omega,$$
> is well-defined and is an isomorphism of real vector spaces. In particular $\dim_{\mathbb R}H^n_{dR}(N)=1$.

> **Corollary (integral obstruction to exactness).** Under the same hypotheses, an $n$-form $\omega\in\Omega^n(N)$ is exact if and only if $\int_N\omega=0$.

The corollary is the theorem read on representatives: $\int_N$ is well-defined precisely because it kills exact forms, and it is injective precisely because a top form of integral zero is exact; the two blockquotes are logically equivalent packagings of one fact. It is the corollary form that the downstream degree theory uses.

---

# Motivation

The top de Rham cohomology of a closed oriented manifold is the single number that survives integration, and this theorem is the statement that integration reads it faithfully. Everything in the smooth-topological toolkit of this section — the Brouwer degree, the winding number, the Chern number of a line bundle over a surface — rests on the following being true: on a closed connected oriented $n$-manifold the total integral of a top form is a complete invariant of its cohomology class, changing by nothing when the form is altered by an exact term and taking every real value.

To see why this is the crux, consider how the [[Def - Brouwer Degree of a Map|Brouwer degree]] of a smooth map $f\colon M\to N$ between closed oriented $n$-manifolds is defined: one fixes an $n$-form $\omega$ on $N$ with $\int_N\omega=1$ and sets $\deg f=\int_Mf^*\omega$. For this to be a number attached to $f$ rather than to the arbitrary choice of $\omega$, one needs two things. First, any two normalising forms $\omega,\omega'$ with $\int_N\omega=\int_N\omega'=1$ must be cohomologous, so that $f^*\omega$ and $f^*\omega'$ differ by an exact form and have equal integral over $M$. Second, a normalising form must exist at all. Both are exactly what this theorem provides: $\int_N$ being injective on cohomology forces $\omega-\omega'$ (integral zero) to be exact, and $\int_N$ being surjective produces a form of any prescribed integral. Without the present theorem the degree would not even be well-defined.

There is a second, more structural reading. The theorem says that in top degree the passage from geometry (a differential form, a piece of local data) to topology (a cohomology class, a global invariant) loses everything except one real number. A closed manifold has no boundary to integrate over, so Stokes' theorem makes the total integral immune to any exact correction; connectedness makes it impossible to "store" different amounts of integral in different regions without those regions communicating; and compactness makes the whole manifold reachable by finitely many charts. The interplay of these three hypotheses is the content, and each is genuinely needed — dropping any one breaks the conclusion, as the per-hypothesis discussion below records.

We assume the reader is comfortable with de Rham cohomology, integration of forms on oriented manifolds, Stokes' theorem, and partitions of unity; these are recalled in the Notation section and restated at each point of use. The one input that is not merely quoted but genuinely reproved on this page is the compactly supported Poincaré lemma on $\mathbb R^n$, because it is the analytic engine of the whole result and its compact-support refinement is exactly the subtlety the ordinary Poincaré lemma does not address.

---

# Sources and Targets

**Sources (Input Broadening).** The literal hypothesis — a closed connected oriented $n$-manifold — is checked so routinely that the useful skill is recognising the disguises in which it arrives.

The first disguised source is **a compact Lie group, or a homogeneous space $G/H$ with $G$ compact connected**. A compact Lie group is a closed manifold (compact, no boundary), it is orientable because it is parallelisable (a left-invariant frame trivialises the tangent bundle, and a global frame orients), and it is connected exactly when it is the identity component; so $SU(2)\cong S^3$, $U(1)\cong S^1$, $SO(3)\cong\mathbb{RP}^3$, and every torus $T^k$ present the hypothesis without the words "closed oriented manifold" ever appearing. The bridge $B\Rightarrow A$ is: *parallelisable $\Rightarrow$ orientable*, together with *compact Lie group $\Rightarrow$ compact without boundary*. This is how the theorem enters the computation that $\tfrac1{24\pi^2}\int_{SU(2)}\operatorname{tr}\big((g^{-1}dg)^{\wedge3}\big)$ is an integer: the bi-invariant $3$-form is a top form on the closed connected oriented $3$-manifold $SU(2)$, and its class is pinned by one number. *Example problem:* show that a bi-invariant top form on a compact connected Lie group $G$ is determined up to an exact form by its integral, hence that two bi-invariant volume forms of equal total volume are cohomologous.

The second disguised source is **the boundary of a compact oriented manifold-with-boundary**, read one component at a time. If $W$ is a compact oriented manifold-with-boundary of dimension $n+1$, then $\partial W$ is a closed oriented $n$-manifold with the induced orientation ([[Def - Manifold with Boundary and Induced Orientation|induced boundary orientation]]); it need not be connected, but the theorem applies to each connected component, and the sum-over-components refinement handles $\partial W$ as a whole. The bridge $B\Rightarrow A$ is: *manifold-with-boundary, compact, oriented $\Rightarrow$ its boundary is closed and oriented*, with connectedness supplied component-wise. This is precisely the input to the cobordism half of degree theory: a map that extends over $W$ has degree zero on $\partial W$. *Example problem:* deduce from the theorem, applied to the components of $\partial W$, that if $\omega$ is a top form on $\partial W$ extending to a closed form on $W$ then $\int_{\partial W}\omega=0$.

The third disguised source is **a closed oriented surface, or a projective space of the right parity**. A closed connected oriented surface $\Sigma_g$ of genus $g$ meets the hypothesis in dimension $n=2$, so its top cohomology $H^2_{dR}(\Sigma_g)$ is one-dimensional; complex projective space $\mathbb{CP}^N$ is compact, connected, and canonically oriented by its complex structure, of real dimension $2N$, so $H^{2N}_{dR}(\mathbb{CP}^N)$ is one-dimensional. The bridge $B\Rightarrow A$ here is *a complex manifold carries a canonical orientation* together with *projective space is compact and connected*. This is the top rung of the ladder that computes the de Rham cohomology of $\mathbb{CP}^N$ (source item A-I3.1.3 of this chapter). *Example problem:* using only this theorem, show that on a closed connected oriented surface a $2$-form is exact if and only if its integral vanishes, and conclude that the space of "areas" $H^2_{dR}(\Sigma)$ is a line.

**Targets (Output Amplification).** The bare conclusion — one number classifies a top class — becomes powerful when combined with a second ingredient.

Combine the theorem with **the naturality of pull-back and Stokes' theorem**, and it produces the entire well-posedness of the [[Def - Brouwer Degree of a Map|Brouwer degree]]. The extra ingredient $D$ is the identity $f^*(d\eta)=d(f^*\eta)$; the payoff $E$ is that $\deg f=\int_Mf^*\omega$ is independent of the normalising form $\omega$ (any two differ by an exact form, whose pull-back integrates to zero) and that a normalising form exists (surjectivity). This is developed on [[Thm - The Brouwer Degree is an Integer and a Homotopy Invariant|the degree theorem]].

Combine the theorem with **a partition of the manifold into finitely many charts and the change-of-variables formula**, and it yields the *localisation of the degree at a regular value*: $\deg f=\sum_{x\in f^{-1}(y)}\operatorname{sign}\det df_x$. The extra ingredient $D$ is a normalising form supported near a regular value $y$, and the payoff $E$ is the integrality of the degree and its combinatorial meaning as a signed count of preimages — a bridge from an integral to a finite sum that is invisible without the freedom to move the class into a small ball, which this theorem grants.

Combine the theorem with **a Chern–Weil curvature representative on a closed oriented surface**, and it makes the *integral of a characteristic form the only invariant*. The extra ingredient $D$ is that the curvature $2$-form of a connection is closed and its class is independent of the connection; the payoff $E$ (developed in chapter VI) is that $\int_\Sigma c_1(L)$ is a single integer completely determining the topological line bundle over $\Sigma$, because $H^2_{dR}(\Sigma)=\mathbb R$ and integration reads it off.

---

# Why Is It True

Picture a top form on $N$ as a distribution of signed mass: $\int_N\omega$ is the total mass, and adding $d\eta$ redistributes mass without changing the total, because on a manifold with no boundary Stokes' theorem says $\int_Nd\eta=0$ — mass leaks only across boundaries, and there are none. So the total mass is a genuine invariant of the cohomology class; the only question is whether it is a *complete* invariant.

It is, and the reason is that mass can be **freely transported and locally annihilated**. Two chunks of mass sitting in different coordinate balls with the same total can be moved into a common ball by pushing them along a chain of overlapping charts — this is where connectedness enters, guaranteeing the chain exists — and inside a single ball, which looks like $\mathbb R^n$, a top form whose total mass is zero can be written as $d$ of something *with compact support*, so it is exact by a genuinely local construction. Compactness enters to make the number of chunks finite, so that a partition of unity reduces any form to a finite sum of chart-supported pieces, each transportable into one reference ball.

> **The mechanism in one sentence: a closed manifold cannot leak integral through a boundary (Stokes), a connected manifold can transport integral freely between charts (chain of balls), and a Euclidean ball can annihilate any integral-zero top form by an explicit compactly supported primitive (the compactly supported Poincaré lemma) — so the total integral is the one and only invariant of a top cohomology class.**

The failure mechanism the hypotheses rule out is instructive. If $N$ had a boundary, exact forms could carry nonzero integral and the total mass would not descend to cohomology. If $N$ were disconnected, mass could be lodged separately in each component and the class would remember one number per component, not one number total, so $\int_N$ would have a kernel. If $N$ were non-orientable, integration of top forms would not be defined at all (no consistent sign), and indeed the top de Rham cohomology of a closed connected non-orientable manifold is zero, not $\mathbb R$. The theorem is exactly the statement that, with all three hypotheses in place, none of these degeneracies occurs and the total integral is faithful.

---

# What Makes This Hard

The single non-obvious step is that the primitive can be taken **compactly supported**. The ordinary [[Thm - The Poincaré Lemma on a Star-Shaped Region|Poincaré lemma on a star-shaped region]] already tells us that every closed form on $\mathbb R^n$ — in particular every top form, all of which are closed — is exact, so a primitive $\eta$ with $d\eta=\omega$ always exists on $\mathbb R^n$; but that $\eta$ generically fails to have compact support, so it cannot be extended by zero across the ball into the rest of $N$, and it is therefore useless for a global conclusion. The whole difficulty is that compactly supported exactness is a strictly stronger property, and it is available *only* when $\int_{\mathbb R^n}\omega=0$: the integral is the precise obstruction. Reproving the compactly supported version — by induction on dimension, integrating out one variable at a time and correcting the remainder by a bump form of unit integral — is the technical heart of the argument and the step beginners skip by wrongly invoking the ordinary Poincaré lemma. The two other common errors are forgetting that the transport-into-one-ball move must *preserve the integral* at every hop (otherwise the final integral-zero conclusion is unjustified), and forgetting to check that each partition-of-unity piece is genuinely compactly supported inside its chart, which uses compactness of $N$.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Show $\int_N$ descends to cohomology and is onto (easy, via Stokes and one bump form). For injectivity — the content — reduce an arbitrary integral-zero top form to a single Euclidean ball by a partition of unity and a connectedness argument that preserves the integral, then kill it there with the compactly supported Poincaré lemma, whose compact-support refinement is what makes the local primitive extend globally.

**Subgoal decomposition:**

1. **Integration descends and vanishes on exact forms.** Show $\int_Nd\eta=0$ and conclude $\int_N$ is a well-defined linear map on $H^n_{dR}(N)$.
   - *Hint:* Stokes' theorem with $\partial N=\varnothing$.
   - *Why needed:* Without this the map on cohomology does not exist, and half of the corollary ("exact $\Rightarrow$ integral zero") is exactly this.

2. **Surjectivity.** Produce one $n$-form with nonzero integral.
   - *Hint:* A nonnegative bump function times the Euclidean volume form in an oriented chart; positivity plus change of variables.
   - *Why needed:* It shows $H^n_{dR}(N)\ne0$ and that $\int_N$ hits all of $\mathbb R$; it also produces normalising forms for the degree.

3. **Compactly supported Poincaré lemma on $\mathbb R^n$.** A compactly supported $n$-form on $\mathbb R^n$ is $d$ of a compactly supported $(n-1)$-form if and only if its integral vanishes.
   - *Hint:* Induct on $n$. Split $\omega=f\,dV$ as $f=(f-g\,b)+g\,b$ where $g$ is the fibre integral over the last variable and $b$ is a fixed unit-integral bump in the last variable; the first summand has zero fibre integral (primitive by integrating in the last variable), the second reduces to dimension $n-1$.
   - *Why needed:* This is the only place the integral obstruction is discharged, and the compact-support refinement is what lets the local primitive extend by zero.

4. **Same-ball lemma.** Two forms compactly supported in one oriented coordinate ball with equal integrals are cohomologous on $N$.
   - *Hint:* Their difference is compactly supported in a copy of $\mathbb R^n$ with integral zero; apply subgoal 3 and extend the primitive by zero.
   - *Why needed:* It is the atomic transport step, used repeatedly along a chain.

5. **Chain-of-balls lemma.** Every form compactly supported in some oriented coordinate ball is cohomologous to a form compactly supported in a fixed reference ball $B_0$, with the same integral.
   - *Hint:* Connectedness gives a finite chain of overlapping balls from the given ball to $B_0$; in each overlap place a bump form of the common integral and hop from one to the next by subgoal 4.
   - *Why needed:* It concentrates any chart-supported piece into one ball where subgoal 3 applies.

6. **Assemble injectivity.** Given $\int_N\omega=0$: partition $\omega$ into chart-supported pieces (subgoal, compactness), transport each into $B_0$ preserving integral (subgoal 5), sum to a single form in $B_0$ of integral $0$, kill it (subgoal 3), and read off that $\omega$ is exact.
   - *Hint:* Integrals add; the transported sum has integral $\int_N\omega=0$.
   - *Why needed:* This is the "integral zero $\Rightarrow$ exact" direction, i.e. injectivity of $\int_N$ on cohomology.

---

# Lemma Decomposition

> [!note]- Lemma 1: Integration descends to $H^n_{dR}$ and kills exact forms
> **Statement:** Let $N$ be a closed oriented $n$-manifold. For every $\eta\in\Omega^{n-1}(N)$ one has $\int_Nd\eta=0$. Consequently the map $\int_N\colon\Omega^n(N)\to\mathbb R$ descends to a well-defined linear map $[\omega]\mapsto\int_N\omega$ on $H^n_{dR}(N)=\Omega^n(N)/d\Omega^{n-1}(N)$.
>
> **Hint:** Apply Stokes' theorem and use $\partial N=\varnothing$.
>
> **Why needed:** It is the existence and well-definedness of the map in the theorem, and it is the "exact $\Rightarrow$ integral zero" half of the corollary.
>
> > [!note]- Full proof
> > **Setup.** Fix $\eta\in\Omega^{n-1}(N)$. Since $N$ is closed it is compact, so $\eta$ and $d\eta$ are automatically compactly supported and $\int_N$ is defined on them by [[Thm - Integration is Well-Defined on Oriented Manifolds|the well-definedness of integration on oriented manifolds]], which states that on an oriented $n$-manifold the integral $\int_N\alpha$ of a compactly supported $\alpha\in\Omega^n(N)$ is independent of the oriented atlas and the subordinate partition of unity used to compute it.
> >
> > **Apply Stokes' theorem.** By [[Thm - Stokes' Theorem on Manifolds|Stokes' theorem]], which states that for a compactly supported $(n-1)$-form $\eta$ on an oriented $n$-manifold-with-boundary $N$ one has $\int_Nd\eta=\int_{\partial N}\iota^*\eta$ where $\iota\colon\partial N\hookrightarrow N$ is the inclusion with the induced boundary orientation,
> > $$\textstyle\int_Nd\eta=\int_{\partial N}\iota^*\eta\qquad\text{(by Stokes' theorem)}.$$
> > **Use the hypothesis $\partial N=\varnothing$.** Because $N$ is closed, $\partial N=\varnothing$, and an integral over the empty manifold is $0$:
> > $$\textstyle\int_{\partial N}\iota^*\eta=\int_{\varnothing}=0\qquad(\text{since }\partial N=\varnothing).$$
> > Combining the two displayed lines, $\int_Nd\eta=0$.
> >
> > **Descent.** The map $\int_N\colon\Omega^n(N)\to\mathbb R$ is linear (integration is linear, by the well-definedness theorem). If $\omega'$ and $\omega$ represent the same class, then $\omega'-\omega=d\eta$ for some $\eta\in\Omega^{n-1}(N)$, whence $\int_N\omega'-\int_N\omega=\int_Nd\eta=0$ by the previous paragraph, so $\int_N\omega'=\int_N\omega$. Therefore $[\omega]\mapsto\int_N\omega$ is well-defined on $H^n_{dR}(N)$, and it is linear because $\int_N$ and the quotient map are. In particular every exact $n$-form has integral zero. $\blacksquare$

> [!note]- Lemma 2: There is a top form with nonzero integral
> **Statement:** On a nonempty oriented $n$-manifold $N$ ($n\ge1$) there exists $\omega\in\Omega^n(N)$ with compact support and $\int_N\omega>0$. Consequently, on a closed connected oriented $N$ the map $\int_N\colon H^n_{dR}(N)\to\mathbb R$ is surjective.
>
> **Hint:** A nonnegative bump function times the pulled-back Euclidean volume form of an oriented chart; positivity and the change-of-variables formula.
>
> **Why needed:** Surjectivity of $\int_N$, and the existence of normalising forms used downstream by the degree.
>
> > [!note]- Full proof
> > **Choose an oriented chart.** Pick a point $p\in N$ and an oriented coordinate ball $(B,\varphi)$ around $p$, so $\varphi\colon B\to\mathbb R^n$ is an orientation-preserving diffeomorphism; such a chart exists by the definition of an oriented smooth manifold ([[Def - Orientation of a Smooth Manifold|orientation of a smooth manifold]]), which furnishes an atlas of orientation-preserving charts.
> >
> > **Build a bump top form.** By [[Thm - Existence of Smooth Bump Functions|the existence of smooth bump functions]], there is $b\in C^\infty(\mathbb R^n)$ with $0\le b\le1$, $b\equiv1$ on a neighbourhood of the origin, and $\operatorname{supp}b$ a compact subset of $\mathbb R^n$; in particular $b\not\equiv0$ and $\int_{\mathbb R^n}b\,dV>0$ because $b$ is nonnegative and positive on an open set. Define
> > $$\omega:=\varphi^*\big(b\,dV\big)\in\Omega^n(B),\qquad dV=dx^1\wedge\cdots\wedge dx^n,$$
> > and extend $\omega$ by zero to $N$; the extension is smooth because $\operatorname{supp}\omega=\varphi^{-1}(\operatorname{supp}b)$ is a compact subset of $B$, hence closed in $N$ and disjoint from a neighbourhood of $N\setminus B$.
> >
> > **Compute the integral.** Since $\omega$ is supported in the single oriented chart $B$, its integral is computed in that chart, and because $\varphi$ is orientation-preserving the [[Thm - Change of Variables for Integration on Manifolds|change-of-variables formula]] — which states $\int_B\varphi^*\alpha=\int_{\varphi(B)}\alpha$ for an orientation-preserving diffeomorphism $\varphi$ and a compactly supported top form $\alpha$ — gives
> > $$\textstyle\int_N\omega=\int_B\varphi^*(b\,dV)=\int_{\mathbb R^n}b\,dV>0\qquad\text{(change of variables; positivity of }b\text{)}.$$
> > **Surjectivity.** The class $[\omega]\in H^n_{dR}(N)$ (every top form is closed) has $\int_N[\omega]=\int_N\omega=c>0$. For any $r\in\mathbb R$, the class $(r/c)[\omega]$ has integral $r$. Hence $\int_N\colon H^n_{dR}(N)\to\mathbb R$ is onto. $\blacksquare$

> [!note]- Lemma 3: Compactly supported Poincaré lemma on $\mathbb R^n$
> **Statement:** Let $\omega\in\Omega^n_c(\mathbb R^n)$ be a compactly supported $n$-form, $n\ge1$. Then there exists $\eta\in\Omega^{n-1}_c(\mathbb R^n)$ with $d\eta=\omega$ if and only if $\int_{\mathbb R^n}\omega=0$.
>
> **Hint:** The "only if" is Stokes on a large ball. For the "if", induct on $n$: with $\omega=f\,dV$ and $t=x^n$, let $g(x')=\int_{\mathbb R}f(x',t)\,dt$ and $b$ a unit-integral bump in $t$; then $f-g\,b$ has zero integral in $t$ for each $x'$ (primitive by integrating in $t$), while $g\,b$ reduces to dimension $n-1$.
>
> **Why needed:** This is the sole source of the integral obstruction, and the compact-support refinement is what makes local primitives extend by zero. It is genuinely stronger than the [[Thm - The Poincaré Lemma on a Star-Shaped Region|ordinary Poincaré lemma]], which gives a primitive with no support control.
>
> > [!note]- Full proof
> > Write points of $\mathbb R^n$ as $x=(x^1,\dots,x^n)$ and $dV=dx^1\wedge\cdots\wedge dx^n$. Every $\omega\in\Omega^n_c(\mathbb R^n)$ is $\omega=f\,dV$ for a unique $f\in C^\infty_c(\mathbb R^n)$, and $\int_{\mathbb R^n}\omega=\int_{\mathbb R^n}f\,dV$ (standard orientation).
> >
> > **Direction ($\Rightarrow$): a compactly supported primitive forces integral zero.** Suppose $\omega=d\eta$ with $\eta\in\Omega^{n-1}_c(\mathbb R^n)$. Choose $R>0$ so large that $\operatorname{supp}\eta\subset\{|x|<R\}$, and let $\overline{B_R}$ be the closed ball of radius $R$, a compact oriented $n$-manifold-with-boundary. Then $\eta$ vanishes on a neighbourhood of $\partial\overline{B_R}$, so
> > $$\textstyle\int_{\mathbb R^n}\omega=\int_{\overline{B_R}}d\eta=\int_{\partial\overline{B_R}}\iota^*\eta=0\qquad\text{(Stokes' theorem; }\eta\equiv0\text{ near the boundary sphere)}.$$
> >
> > **Direction ($\Leftarrow$): integral zero yields a compactly supported primitive.** We argue by induction on $n$.
> >
> > **Base case $n=1$.** Here $\omega=f\,dx^1$ with $f\in C^\infty_c(\mathbb R)$ and $\int_{\mathbb R}f\,dx^1=0$. Define $\eta:=g$, the $0$-form
> > $$g(x^1):=\int_{-\infty}^{x^1}f(s)\,ds.$$
> > Then $g$ is smooth with $g'=f$ (fundamental theorem of calculus), so $d\eta=g'\,dx^1=f\,dx^1=\omega$. It remains to check compact support. Choose $R$ with $\operatorname{supp}f\subset(-R,R)$. For $x^1<-R$ the integrand vanishes, so $g(x^1)=0$; for $x^1>R$,
> > $$g(x^1)=\int_{-\infty}^{x^1}f=\int_{\mathbb R}f=0\qquad(\text{by the hypothesis }\textstyle\int_{\mathbb R}f=0).$$
> > Hence $\operatorname{supp}g\subset[-R,R]$ is compact and $\eta\in\Omega^0_c(\mathbb R)$, as required.
> >
> > **Inductive step.** Let $n\ge2$ and assume the ($\Leftarrow$) statement holds on $\mathbb R^{n-1}$. Write $x=(x',t)$ with $x'=(x^1,\dots,x^{n-1})\in\mathbb R^{n-1}$ and $t=x^n\in\mathbb R$, and let $p\colon\mathbb R^n\to\mathbb R^{n-1}$, $p(x',t)=x'$, be the projection. Let $\omega=f\,dV$, $f\in C^\infty_c(\mathbb R^n)$, $\int_{\mathbb R^n}f\,dV=0$.
> >
> > **Fix a unit bump in the last variable.** By [[Thm - Existence of Smooth Bump Functions|the existence of smooth bump functions]] choose $b\in C^\infty_c(\mathbb R)$ with $\int_{\mathbb R}b\,dt=1$; set $\gamma:=b(t)\,dt\in\Omega^1_c(\mathbb R)$, pulled back to $\mathbb R^n$ (still written $\gamma$), and note $d\gamma=b'(t)\,dt\wedge dt=0$.
> >
> > **Form the fibre integral.** Define $g\colon\mathbb R^{n-1}\to\mathbb R$ by
> > $$g(x'):=\int_{\mathbb R}f(x',t)\,dt.$$
> > Because $f$ is smooth and compactly supported, differentiation under the integral sign is licensed (the $x'$-derivatives of $f$ are continuous and supported in one fixed compact set, providing an integrable dominating function on the compact $t$-support), so $g\in C^\infty(\mathbb R^{n-1})$ with $\partial_{x^i}g(x')=\int_{\mathbb R}\partial_{x^i}f(x',t)\,dt$. Its support is contained in $p(\operatorname{supp}f)$, the image of a compact set under a continuous map, hence compact; thus $g\in C^\infty_c(\mathbb R^{n-1})$. By the Fubini theorem for the compactly supported smooth (hence Lebesgue-integrable) function $f$,
> > $$\textstyle\int_{\mathbb R^{n-1}}g\,dx^1\wedge\cdots\wedge dx^{n-1}=\int_{\mathbb R^{n-1}}\!\Big(\int_{\mathbb R}f(x',t)\,dt\Big)dx'=\int_{\mathbb R^n}f\,dV=0\qquad\text{(Fubini; the hypothesis }\textstyle\int f=0).$$
> >
> > **Split $\omega$ into a "vertical" and a "horizontal" part.** Set $h(x',t):=f(x',t)-g(x')\,b(t)$. For each fixed $x'$,
> > $$\int_{\mathbb R}h(x',t)\,dt=\int_{\mathbb R}f(x',t)\,dt-g(x')\int_{\mathbb R}b(t)\,dt=g(x')-g(x')\cdot1=0\qquad(\text{definition of }g\text{; }\textstyle\int b=1).$$
> > Correspondingly $\omega=f\,dV=h\,dV+(g\,b)\,dV$, and we produce a compactly supported primitive for each summand.
> >
> > **Primitive of the vertical part $h\,dV$.** Define
> > $$H(x',t):=\int_{-\infty}^{t}h(x',s)\,ds,$$
> > smooth in $(x',t)$ by the same differentiation-under-the-integral argument, with $\partial_tH=h$. Choose $R$ with $\operatorname{supp}f\cup\big(\operatorname{supp}g\times\operatorname{supp}b\big)\subset\{|x'|\le R\}\times[-R,R]$, so $\operatorname{supp}h\subset\{|x'|\le R\}\times[-R,R]$. Then: if $t<-R$ the integrand is zero so $H(x',t)=0$; if $t>R$,
> > $$H(x',t)=\int_{-\infty}^{t}h(x',s)\,ds=\int_{\mathbb R}h(x',s)\,ds=0\qquad(\text{the vertical integral of }h\text{ vanishes)};$$
> > and if $|x'|>R$ then $h(x',\cdot)\equiv0$ so $H(x',t)=0$. Hence $H\in C^\infty_c(\mathbb R^n)$. Put
> > $$\eta_1:=(-1)^{n-1}H\,dx^1\wedge\cdots\wedge dx^{n-1}\in\Omega^{n-1}_c(\mathbb R^n).$$
> > Computing its exterior derivative, only the $\partial_t H\,dt$ term of $dH$ survives the wedge with $dx^1\wedge\cdots\wedge dx^{n-1}$ (a repeated $dx^i$ kills the rest):
> > $$d\eta_1=(-1)^{n-1}\,\partial_tH\;dt\wedge dx^1\wedge\cdots\wedge dx^{n-1}=(-1)^{n-1}(-1)^{n-1}\,\partial_tH\;dV=h\,dV,$$
> > where the middle equality moves $dt$ past the $n-1$ factors $dx^1,\dots,dx^{n-1}$, contributing $(-1)^{n-1}$, and $\partial_tH=h$.
> >
> > **Primitive of the horizontal part $(g\,b)\,dV$.** The $(n-1)$-form $\alpha:=g\,dx^1\wedge\cdots\wedge dx^{n-1}\in\Omega^{n-1}_c(\mathbb R^{n-1})$ has $\int_{\mathbb R^{n-1}}\alpha=0$ by the fibre-integral computation, so by the inductive hypothesis there is $\beta\in\Omega^{n-2}_c(\mathbb R^{n-1})$ with $d\beta=\alpha$. Pull $\beta$ back to $\mathbb R^n$ by $p$ and set
> > $$\eta_2:=p^*\beta\wedge\gamma\in\Omega^{n-1}(\mathbb R^n).$$
> > Its support lies in $p^{-1}(\operatorname{supp}\beta)\cap\{t\in\operatorname{supp}b\}$, which is compact because it is bounded in $x'$ (by $\operatorname{supp}\beta$) and in $t$ (by $\operatorname{supp}b$); so $\eta_2\in\Omega^{n-1}_c(\mathbb R^n)$. Since $d(p^*\beta)=p^*(d\beta)=p^*\alpha=g\,dx^1\wedge\cdots\wedge dx^{n-1}$ and $d\gamma=0$,
> > $$d\eta_2=d(p^*\beta)\wedge\gamma+(-1)^{n-2}p^*\beta\wedge d\gamma=\big(g\,dx^1\wedge\cdots\wedge dx^{n-1}\big)\wedge\big(b\,dt\big)=(g\,b)\,dV\qquad(\text{Leibniz; }d\gamma=0).$$
> >
> > **Combine.** Set $\eta:=\eta_1+\eta_2\in\Omega^{n-1}_c(\mathbb R^n)$. Then
> > $$d\eta=d\eta_1+d\eta_2=h\,dV+(g\,b)\,dV=\big(h+g\,b\big)\,dV=f\,dV=\omega\qquad(\text{since }h=f-g\,b).$$
> > This completes the inductive step and the proof. $\blacksquare$

> [!note]- Lemma 4: Same-ball lemma
> **Statement:** Let $N$ be an oriented $n$-manifold and $B\subset N$ an oriented coordinate ball, $\varphi\colon B\to\mathbb R^n$ orientation-preserving. If $\mu,\mu'\in\Omega^n(N)$ are compactly supported inside $B$ with $\int_N\mu=\int_N\mu'$, then $\mu-\mu'=d\eta$ for some $\eta\in\Omega^{n-1}(N)$ compactly supported inside $B$; in particular $[\mu]=[\mu']$ in $H^n_{dR}(N)$.
>
> **Hint:** Push the difference to $\mathbb R^n$ by $\varphi$; it has integral zero; apply Lemma 3 and pull the compactly supported primitive back, extending by zero.
>
> **Why needed:** It is the single transport step used repeatedly along the chain of balls.
>
> > [!note]- Full proof
> > **Transfer to $\mathbb R^n$.** The form $\mu-\mu'$ is compactly supported inside $B$, so $\varphi_*(\mu-\mu'):=(\varphi^{-1})^*(\mu-\mu')\in\Omega^n_c(\mathbb R^n)$ is a compactly supported top form on $\mathbb R^n$. Because $\varphi$ is orientation-preserving, [[Thm - Change of Variables for Integration on Manifolds|change of variables]] gives
> > $$\textstyle\int_{\mathbb R^n}\varphi_*(\mu-\mu')=\int_B(\mu-\mu')=\int_N\mu-\int_N\mu'=0\qquad(\text{change of variables; the hypothesis }\textstyle\int_N\mu=\int_N\mu').$$
> > **Kill it in $\mathbb R^n$.** By Lemma 3 there is $\zeta\in\Omega^{n-1}_c(\mathbb R^n)$ with $d\zeta=\varphi_*(\mu-\mu')$.
> >
> > **Pull back and extend by zero.** Set $\eta:=\varphi^*\zeta\in\Omega^{n-1}(B)$; it is compactly supported inside $B$ because $\operatorname{supp}\eta=\varphi^{-1}(\operatorname{supp}\zeta)$ is compact in $B$, so it extends by zero to a smooth global $(n-1)$-form on $N$, again written $\eta$. Since pull-back commutes with $d$,
> > $$d\eta=\varphi^*(d\zeta)=\varphi^*\varphi_*(\mu-\mu')=\mu-\mu'\qquad\text{on }B,$$
> > and both sides vanish outside $B$, so $d\eta=\mu-\mu'$ on all of $N$. Therefore $[\mu]=[\mu']$ in $H^n_{dR}(N)$. $\blacksquare$

> [!note]- Lemma 5: Chain-of-balls lemma
> **Statement:** Let $N$ be a connected oriented $n$-manifold and fix an oriented coordinate ball $B_0\subset N$. Then for every $n$-form $\mu\in\Omega^n(N)$ compactly supported inside some oriented coordinate ball $B$ there is an $n$-form $\sigma$ compactly supported inside $B_0$ with $[\mu]=[\sigma]$ in $H^n_{dR}(N)$ and $\int_N\sigma=\int_N\mu$.
>
> **Hint:** Connectedness gives a finite chain of overlapping oriented coordinate balls $B=U_0,U_1,\dots,U_k=B_0$; in each overlap place a bump $n$-form of integral $\int_N\mu$ and hop with Lemma 4.
>
> **Why needed:** It concentrates any chart-supported piece into the single reference ball where Lemma 3 can be applied.
>
> > [!note]- Full proof
> > Write $c:=\int_N\mu$.
> >
> > **Every oriented coordinate ball is chain-connected to $B_0$.** Call an oriented coordinate ball $U$ *good* if there is a finite sequence of oriented coordinate balls $B_0=V_0,V_1,\dots,V_r=U$ with $V_{i-1}\cap V_i\ne\varnothing$ for each $i$. Let $S:=\bigcup\{U:U\text{ good}\}$. Then $S$ is open, being a union of open balls, and nonempty since $B_0$ is good. It is also closed: if $q\in\overline S$, choose any oriented coordinate ball $U_q\ni q$ (one exists by the oriented atlas); since $q\in\overline S$, $U_q$ meets $S$, so $U_q$ meets some good ball $V$, giving $U_q\cap V\ne\varnothing$, so appending $U_q$ to a chain for $V$ shows $U_q$ is good, whence $q\in U_q\subset S$. As $N$ is connected and $S$ is nonempty, open, and closed, $S=N$. Now let $B$ be an arbitrary oriented coordinate ball; pick $p\in B$; then $p\in S=N$ lies in some good ball $V$, so $B\cap V\ni p$ is nonempty and $B$, appended to a chain for $V$, is good. Thus **every** oriented coordinate ball, in particular the $B$ containing $\operatorname{supp}\mu$, is chain-connected to $B_0$.
> >
> > **Set up the chain and the bump forms.** Fix a chain of oriented coordinate balls $B=U_0,U_1,\dots,U_k=B_0$ with $U_{i-1}\cap U_i\ne\varnothing$. For each $i=1,\dots,k$ choose a point $q_i\in U_{i-1}\cap U_i$ and, exactly as in Lemma 2 (a bump function times the Euclidean volume form in a chart, scaled), an $n$-form $\nu_i$ compactly supported inside the open set $U_{i-1}\cap U_i$ with $\int_N\nu_i=c$: take a nonnegative bump form of positive integral $c_i>0$ supported in $U_{i-1}\cap U_i$ and multiply by $c/c_i$ (if $c=0$, take $\nu_i=0$). Note $\nu_i$ is compactly supported inside $U_{i-1}$ and, separately, inside $U_i$.
> >
> > **Hop along the chain.** We compare consecutive forms in a common ball, applying Lemma 4 each time:
> > - In $U_0=B$: $\mu$ and $\nu_1$ are both compactly supported inside $U_0$ (for $\nu_1$, because $\operatorname{supp}\nu_1\subset U_0\cap U_1\subset U_0$) with $\int_N\mu=c=\int_N\nu_1$, so $[\mu]=[\nu_1]$ by Lemma 4.
> > - In $U_i$ for $1\le i\le k-1$: $\nu_i$ and $\nu_{i+1}$ are both compactly supported inside $U_i$ (since $\operatorname{supp}\nu_i\subset U_{i-1}\cap U_i\subset U_i$ and $\operatorname{supp}\nu_{i+1}\subset U_i\cap U_{i+1}\subset U_i$) with equal integral $c$, so $[\nu_i]=[\nu_{i+1}]$ by Lemma 4.
> >
> > Chaining these equalities, $[\mu]=[\nu_1]=[\nu_2]=\cdots=[\nu_k]$ in $H^n_{dR}(N)$.
> >
> > **Conclude.** The last bump form $\nu_k$ is compactly supported inside $U_{k-1}\cap U_k\subset U_k=B_0$, so $\sigma:=\nu_k$ is compactly supported inside $B_0$, satisfies $[\sigma]=[\mu]$, and has $\int_N\sigma=c=\int_N\mu$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $N$ be a closed, connected, oriented smooth manifold of dimension $n\ge1$.
>
> **Step 0 — the map exists and is linear.** By Lemma 1, $\int_Nd\eta=0$ for every $\eta\in\Omega^{n-1}(N)$, so $\int_N$ descends to a well-defined linear map
> $$\textstyle\int_N\colon H^n_{dR}(N)\longrightarrow\mathbb R,\qquad[\omega]\longmapsto\int_N\omega.$$
> (Recall $H^n_{dR}(N)=\Omega^n(N)/d\Omega^{n-1}(N)$ because every $n$-form is closed.) We must show this map is surjective and injective.
>
> **Step 1 — surjectivity.** By Lemma 2 there is a compactly supported $\omega_\ast\in\Omega^n(N)$ with $\int_N\omega_\ast=c>0$; for any $r\in\mathbb R$ the class $\tfrac rc[\omega_\ast]$ has integral $r$. Hence $\int_N$ is onto $\mathbb R$, and in particular $H^n_{dR}(N)\ne0$.
>
> **Step 2 — injectivity, reduction to a single chart.** It suffices to show: if $\omega\in\Omega^n(N)$ satisfies $\int_N\omega=0$, then $\omega$ is exact (for then $\ker\int_N=0$ on cohomology). Because $N$ is compact, cover it by finitely many oriented coordinate balls $B_1,\dots,B_m$. By [[Thm - Existence of Smooth Partitions of Unity|the existence of smooth partitions of unity]] — which produces, for the finite open cover $\{B_j\}$ of the compact manifold $N$, smooth functions $\rho_1,\dots,\rho_m$ with $0\le\rho_j\le1$, $\operatorname{supp}\rho_j\subset B_j$, and $\sum_j\rho_j\equiv1$ — write
> $$\omega=\sum_{j=1}^m\rho_j\,\omega.$$
> Each $\rho_j\omega$ is compactly supported inside $B_j$: its support is contained in $\operatorname{supp}\rho_j$, which is closed in the compact $N$ hence compact, and contained in the open set $B_j$, hence a compact subset of $B_j$.
>
> **Step 3 — transport every piece into one reference ball.** Fix the reference oriented coordinate ball $B_0:=B_1$. By Lemma 5, for each $j$ there is $\sigma_j\in\Omega^n(N)$ compactly supported inside $B_0$ with
> $$[\rho_j\omega]=[\sigma_j]\quad\text{and}\quad\textstyle\int_N\sigma_j=\int_N\rho_j\omega.$$
> Put $\sigma:=\sum_{j=1}^m\sigma_j$, an $n$-form compactly supported inside $B_0$. Then, summing the cohomology equalities,
> $$[\omega]=\sum_{j=1}^m[\rho_j\omega]=\sum_{j=1}^m[\sigma_j]=[\sigma]\qquad(\text{Lemma 5, applied to each }j),$$
> and summing the integral equalities and using linearity of $\int_N$,
> $$\textstyle\int_N\sigma=\sum_{j=1}^m\int_N\sigma_j=\sum_{j=1}^m\int_N\rho_j\omega=\int_N\!\Big(\sum_{j=1}^m\rho_j\omega\Big)=\int_N\omega=0\qquad(\text{partition of unity; the hypothesis }\textstyle\int_N\omega=0).$$
>
> **Step 4 — annihilate the concentrated form.** The form $\sigma$ is compactly supported inside the oriented coordinate ball $B_0$ with $\int_N\sigma=0$. Pushing to $\mathbb R^n$ by the orientation-preserving chart $\varphi_0\colon B_0\to\mathbb R^n$, the form $\varphi_{0\ast}\sigma\in\Omega^n_c(\mathbb R^n)$ has $\int_{\mathbb R^n}\varphi_{0\ast}\sigma=\int_{B_0}\sigma=0$ (change of variables), so by Lemma 3 there is $\zeta\in\Omega^{n-1}_c(\mathbb R^n)$ with $d\zeta=\varphi_{0\ast}\sigma$; then $\tau:=\varphi_0^*\zeta$, compactly supported inside $B_0$ and extended by zero to $N$, satisfies $d\tau=\sigma$ on $N$. Hence $[\sigma]=0$ in $H^n_{dR}(N)$.
>
> **Step 5 — conclude injectivity.** Combining Steps 3 and 4, $[\omega]=[\sigma]=0$, so $\omega$ is exact. Therefore the kernel of $\int_N$ on $H^n_{dR}(N)$ is trivial and $\int_N$ is injective.
>
> **Step 6 — assemble.** By Step 0 the map $\int_N\colon H^n_{dR}(N)\to\mathbb R$ is well-defined and linear, by Step 1 it is surjective, and by Steps 2–5 it is injective; hence it is an isomorphism, and $\dim_{\mathbb R}H^n_{dR}(N)=\dim_{\mathbb R}\mathbb R=1$.
>
> **Corollary.** For $\omega\in\Omega^n(N)$: if $\omega=d\eta$ is exact then $\int_N\omega=0$ by Lemma 1; conversely if $\int_N\omega=0$ then $\omega$ is exact by Steps 2–5. So $\omega$ is exact if and only if $\int_N\omega=0$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Winding number as a top-degree integral on the circle.** Regard $S^1$ as a closed connected oriented $1$-manifold. A smooth map $g\colon S^1\to U(1)$ pulls back the normalised angle form to $g^*(d\theta/2\pi)\in\Omega^1(S^1)$, and this theorem says its class in $H^1_{dR}(S^1)\cong\mathbb R$ is determined by its integral, the winding number. The theorem applies because $S^1$ satisfies all three hypotheses; it is non-obvious as an application because the object of interest is a *map*, not a form, and the reduction of homotopy information to a single integral is exactly the one-dimensionality of the top cohomology. This is developed on [[Thm - Winding Number of a Map from the Circle to U(1)|the winding-number theorem]].

**Areas on a closed surface are a single number.** On a closed connected oriented surface $\Sigma$, two area forms (nowhere-vanishing positive $2$-forms) that enclose the same total area are cohomologous, by the corollary applied to their difference. The theorem applies with $n=2$; the non-obvious content is that there is no local invariant distinguishing two total-area-equal $2$-forms — the entire cohomological difference is the number $\int_\Sigma(\omega-\omega')=0$. This underlies the statement that a symplectic form on a closed surface is determined up to exact perturbation by its total area.

**Cobordism kills the degree.** Let $W$ be a compact oriented $3$-manifold-with-boundary and $\partial W=\Sigma$ a closed oriented surface (possibly disconnected). If a $2$-form on $\Sigma$ extends to a closed form on $W$, then applying this theorem component-by-component to $\Sigma$ together with Stokes shows the form has integral zero on each component. The theorem applies to each connected component of $\partial W$; the subtlety is that connectedness is needed *per component*, and the sum-over-components refinement is what makes the boundary of a bounding manifold have total degree zero — the mechanism behind "a map extending over a bounding manifold has degree zero".

---

# Bridges

- **The analytic route through Hodge theory.** On a closed oriented *Riemannian* manifold, Hodge theory represents each cohomology class by a unique harmonic form, and Poincaré duality then identifies $H^n_{dR}(N)$ with $H^0_{dR}(N)$, which is $\mathbb R$ for a connected manifold because the only harmonic functions on a closed connected manifold are the constants. This gives the same conclusion — $H^n_{dR}(N)\cong\mathbb R$ — by an entirely different, elliptic-analytic mechanism, with the integration pairing realised as the $L^2$ pairing against the constant function. The construction is carried out on [[Thm - Poincare Duality via Hodge Star|Poincaré duality via the Hodge star]]; the present theorem is the metric-free, hands-on version that suffices for degree theory and does not require choosing a metric or invoking elliptic regularity.

- **The degree of a map.** The theorem is the exact foundation on which the [[Def - Brouwer Degree of a Map|Brouwer degree]] is built: fixing $\omega$ with $\int_N\omega=1$ (surjectivity) and using that any two such choices are cohomologous (injectivity) makes $\deg f=\int_Mf^*\omega$ a well-defined real number, and the localisation-at-a-regular-value argument then shows it is an integer. This is [[Thm - The Brouwer Degree is an Integer and a Homotopy Invariant|the degree theorem]], whose statement (a)–(g) opens by invoking exactly the well-definedness this page proves.

- **The cohomology of complex projective space.** The Mayer–Vietoris induction that computes $H^\bullet_{dR}(\mathbb{CP}^N)$ terminates, in top degree $2N$, in the statement that $H^{2N}_{dR}(\mathbb{CP}^N)\cong\mathbb R$ because $\mathbb{CP}^N$ is a closed connected oriented $2N$-manifold; the present theorem supplies that terminal fact and the integration pairing that pins down the generator. See [[Thm - The de Rham Cohomology of Complex Projective Space|the de Rham cohomology of complex projective space]], where the class $[\omega_N]^N$ is shown nonzero precisely because its integral over $\mathbb{CP}^N$ is nonzero.

- **The Mayer–Vietoris and homotopy machinery.** The alternative computation of $H^n_{dR}(S^n)\cong\mathbb R$ proceeds by induction using [[Thm - The Mayer-Vietoris Sequence|the Mayer–Vietoris sequence]] and [[Thm - Homotopy Invariance of de Rham Cohomology|homotopy invariance of de Rham cohomology]], recovering the sphere case of this theorem from the connecting homomorphism; the present theorem generalises the outcome from spheres to arbitrary closed connected oriented manifolds by a transport argument rather than an exact sequence, and the two agree on their common ground $N=S^n$ (compare [[Ex - The de Rham Cohomology of R^n is Trivial in Positive Degrees|the triviality of the de Rham cohomology of $\mathbb R^n$]], which is the non-compact contrast: without compactness the top cohomology can vanish).

---

# Unlocked by This

> [!tip] Normalised volume form and the degree pairing *(from Differential Topology)*
> Because $\int_N$ is an isomorphism, there is, for any chosen orientation, a distinguished generator of $H^n_{dR}(N)$: the class of any $\omega$ with $\int_N\omega=1$. Fixing it turns "compute a cohomology class in top degree" into "compute one integral", which is the computational engine of degree theory and of the Chern-number calculations in chapter VI.

> [!tip] Top cohomology detects orientability *(from Algebraic Topology)*
> The same transport argument shows that for a closed connected *non-orientable* manifold the top de Rham cohomology vanishes, because integration is no longer defined and integral-zero is automatic. Thus $H^n_{dR}(N)$ being $\mathbb R$ rather than $0$ is a cohomological detector of orientability, a fact used when reading off orientability from the top Betti number.
