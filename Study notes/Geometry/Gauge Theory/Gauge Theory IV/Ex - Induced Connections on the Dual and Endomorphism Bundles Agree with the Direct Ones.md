---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - Principal Connections Induce Covariant Derivatives on Associated Bundles"
  - "Def - Induced Connections on Dual, Hom, and Endomorphism Bundles"
  - "Def - Connection Matrix and Local Form of a Connection"
  - "Def - Connection on a Vector Bundle"
  - "Def - Representation of a Lie Algebra"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $E\to M$ be a smooth real vector bundle of rank $k$, with frame bundle $\operatorname{Fr}(E)$ — the principal $GL_k(\mathbb R)$-bundle whose fibre over $m$ is the set of bases of $E_m$. Let $\nabla$ be a connection on $E$, with local connection matrix $A=A(\nabla,e)\in\Omega^1(U;\mathfrak{gl}_k(\mathbb R))$ relative to a local frame $e=(e_1,\dots,e_k)$ over $U\subseteq M$, so that $\nabla e_j=\sum_i e_i\,A^{i}{}_{j}$, abbreviated $\nabla e=e\cdot A$; equivalently, for a section $s=e\sigma$ with $\sigma\colon U\to\mathbb R^k$ its column of components, $\nabla s=e\,(d\sigma+A\sigma)$.

The dual bundle $E^{*}$ and the endomorphism bundle $\operatorname{End}(E)=E\otimes E^{*}$ are associated bundles of $\operatorname{Fr}(E)$: they are $\operatorname{Fr}(E)\times_{\rho^{*}}(\mathbb R^{k})^{*}$ and $\operatorname{Fr}(E)\times_{\operatorname{Ad}}\operatorname{End}(\mathbb R^{k})$, where $\rho^{*}$ is the dual (contragredient) representation $\rho^{*}(g)=(g^{-1})^{t}$ of $GL_k(\mathbb R)$ on $(\mathbb R^{k})^{*}$, and $\operatorname{Ad}$ is the conjugation representation $\operatorname{Ad}(g)\Phi=g\Phi g^{-1}$ on $\operatorname{End}(\mathbb R^{k})$. Chapter II also defines connections on $E^{*}$ and $\operatorname{End}(E)$ *directly*, by demanding that the natural pairings be parallel:
$$d\langle\alpha,s\rangle=\langle\nabla\alpha,s\rangle+\langle\alpha,\nabla s\rangle\quad(\alpha\in\Gamma(E^{*}),\ s\in\Gamma(E)),\qquad \nabla(\phi(s))=(\nabla\phi)(s)+\phi(\nabla s)\quad(\phi\in\Gamma(\operatorname{End}E),\ s\in\Gamma(E)).$$

**Prove that the two constructions agree.** Concretely: compute the differential $\rho^{*}_{*}$ of the contragredient representation and the differential $\operatorname{Ad}_{*}$ of the conjugation representation; deduce from the induced-connection theorem that the connection matrices of the *associated-bundle* connections on $E^{*}$ and $\operatorname{End}(E)$ are $-A^{t}$ and $[A,\,\cdot\,]$ respectively; compute the connection matrices of the *directly defined* connections and show they are also $-A^{t}$ and $[A,\,\cdot\,]$; and conclude that the two connections coincide on each bundle. This is the identification clause of Haydys's Exercise 48 together with his corollary that a connection on $E$ induces connections on $E^{*}$, $\operatorname{End}(E)$ "and so on".

**Recall:**

The ingredients are the induced-connection theorem, which produces the associated-bundle connection and its local formula; the direct definitions of the induced connections from chapter II; and the notion of the connection matrix of a connection in a local frame.

![[Thm - Principal Connections Induce Covariant Derivatives on Associated Bundles#Statement]]

The two clauses we invoke are the **local formula** and the **frame-bundle normalisation**. For a representation $\sigma\colon GL_k(\mathbb R)\to GL(W)$ with differential $\sigma_{*}=d_1\sigma\colon\mathfrak{gl}_k(\mathbb R)\to\operatorname{End}(W)$, the induced connection $\nabla^{\omega}$ on $\operatorname{Fr}(E)\times_{\sigma}W$ is, in terms of a local section $q$ of $\operatorname{Fr}(E)$ and a map $w\colon U\to W$,
$$\nabla^{\omega}_{X}[q,w]=\big[q,\ \partial_{X}w+\sigma_{*}\!\big(q^{*}\omega(X)\big)\,w\big],$$
where $\omega$ is the principal connection on $\operatorname{Fr}(E)$ corresponding to $\nabla$; and for the standard representation the correspondence between $\nabla$ and $\omega$ is fixed by $e^{*}\omega=A(\nabla,e)$ for every local frame $e$ regarded as a local section of $\operatorname{Fr}(E)$. Taking $q=e$, so that $e^{*}\omega=A$, and a *constant* $w$ (the components of an element of a fixed basis of $W$), the formula reduces to $\nabla^{\omega}[e,w]=[e,\sigma_{*}(A)w]$: **the connection matrix of the induced connection, in the frame $\{[e,w_a]\}$ of the associated bundle, is $\sigma_{*}(A)$.** This is the single output of the theorem that the exercise uses.

![[Def - Induced Connections on Dual, Hom, and Endomorphism Bundles#The Definition]]

The [[Def - Induced Connections on Dual, Hom, and Endomorphism Bundles|direct induced connections]] on $E^{*}$ and $\operatorname{End}(E)$ are the unique connections making the displayed Leibniz identities hold, where $\langle\alpha,s\rangle=\alpha(s)\in C^{\infty}(M)$ is the natural pairing $E^{*}\otimes E\to\underline{\mathbb R}$ and $\phi(s)$ is the pointwise application of the endomorphism $\phi$ to the section $s$. Existence and uniqueness of these connections are established on that page; here we only need the defining Leibniz identities.

![[Def - Connection Matrix and Local Form of a Connection#The Definition]]

The [[Def - Connection Matrix and Local Form of a Connection|connection matrix]] of a connection in a local frame is the matrix-valued $1$-form $A$ with $\nabla(\text{frame})=(\text{frame})\cdot A$; equivalently, in coordinates $\nabla=d+A$. A connection on a bundle is completely determined by its connection matrix relative to any frame covering a neighbourhood, because $\nabla(e\sigma)=e(d\sigma+A\sigma)$ prescribes $\nabla$ on every section over the frame's domain. Two connections that have the same connection matrix relative to the same frame therefore agree over that frame's domain; agreeing on the domains of frames that cover $M$, they are equal.

---

# Convergent Strategy

**Problem class.** This is a *two-descriptions-agree* problem: the same geometric object — a connection on $E^{*}$, and one on $\operatorname{End}(E)$ — is manufactured in two different ways, and the task is to prove the outputs identical. The efficient proof of such a statement is not to chase the constructions abstractly but to compute a single complete local invariant of each output and check the invariants match. For connections that invariant is the connection matrix in a frame, and equality of connection matrices in a covering family of frames is equality of connections.

**Assumption pattern.** The recognisable trigger is that both bundles are associated bundles of the same principal bundle $\operatorname{Fr}(E)$, for explicit representations $\rho^{*}$ and $\operatorname{Ad}$, *and* that both carry an intrinsic Leibniz characterisation. The associated-bundle side hands us the connection matrix for free — it is $\sigma_{*}(A)$, the differential of the representation applied to the base connection matrix. The direct side requires a short computation with the Leibniz rule. The pattern is: whenever a bundle is simultaneously "associated to a principal bundle" and "defined by a universal/Leibniz property", compute the connection matrix from the representation-theoretic side (where it is $\sigma_{*}(A)$) and verify it from the Leibniz side.

**Theorem routing.** For each bundle the route is identical. First, identify the representation ($\rho^{*}$ for $E^{*}$, $\operatorname{Ad}$ for $\operatorname{End}E$) and differentiate it at the identity to get $\sigma_{*}$: for the contragredient representation this yields $\rho^{*}_{*}(X)=-X^{t}$, for conjugation $\operatorname{Ad}_{*}(X)=[X,\,\cdot\,]$. Second, feed $A$ into $\sigma_{*}$ via [[Thm - Principal Connections Induce Covariant Derivatives on Associated Bundles|the induced-connection theorem]] to obtain the associated-bundle connection matrices $-A^{t}$ and $[A,\,\cdot\,]$. Third, compute the direct connection matrices from the Leibniz identities of [[Def - Induced Connections on Dual, Hom, and Endomorphism Bundles|the direct construction]], again obtaining $-A^{t}$ and $[A,\,\cdot\,]$. Fourth, invoke the fact that a connection is determined by its matrix in a covering family of frames to conclude equality.

**Key decision point.** The one move that requires thought is choosing the *right induced frame* on each associated bundle. The construction $\operatorname{Fr}(E)\times_{\sigma}W$ produces, from the frame $e$ of $E$ and a basis $\{w_a\}$ of $W$, the frame $\{[e,w_a]\}$; the whole computation rests on recognising that for $W=(\mathbb R^{k})^{*}$ with the dual standard basis this induced frame is exactly the dual coframe $e^{*}=(e^{1},\dots,e^{k})$, and for $W=\operatorname{End}(\mathbb R^{k})$ with the elementary matrices $E_{ab}$ it is exactly the frame $\{e_a\otimes e^{b}\}$ of $\operatorname{End}(E)$. Matching frames on the two sides is what makes "the connection matrices are equal" a legitimate comparison; comparing matrices in different frames would be meaningless.

---

# Legal Operations Used

This solution deploys the following legal operations, named descriptively; the topic page for Gauge Theory IV lists them under its Legal Operations, and the numbering there will be reconciled with these descriptions.

1. **Differentiate a representation at the identity to obtain the induced Lie-algebra representation.** For $\sigma\colon GL_k(\mathbb R)\to GL(W)$, compute $\sigma_{*}(X)=\frac{d}{dt}\big|_{0}\sigma(\exp tX)$; this is the [[Def - Representation of a Lie Algebra|Lie-algebra representation]] that governs the induced connection.

2. **Read the associated-bundle connection matrix off the theorem as $\sigma_{*}(A)$.** Apply the local formula of [[Thm - Principal Connections Induce Covariant Derivatives on Associated Bundles|the induced-connection theorem]] with $q=e$, $e^{*}\omega=A$, and a constant frame vector, to obtain the connection matrix $\sigma_{*}(A)$.

3. **Compute a connection matrix from a Leibniz identity.** Apply the defining Leibniz rule of the direct construction to a frame element (and its dual) and solve for the matrix entries; this converts the intrinsic characterisation into an explicit matrix.

4. **Match induced frames across the two constructions.** Recognise the associated-bundle frame $\{[e,w_a]\}$ as the dual coframe $e^{*}$ (for $E^{*}$) and as $\{e_a\otimes e^{b}\}$ (for $\operatorname{End}E$), so that the two connection matrices are computed relative to the same frame.

5. **Conclude equality of connections from equality of connection matrices in a covering family of frames.** A connection is determined by its matrix in any frame; equal matrices over the domains of frames covering $M$ give equal connections.

---

# Hints

> [!note]- Hint 1
> Do not compare the two connections directly. Each is completely encoded by its connection matrix in a local frame, and two connections with the same matrix in the same frame are equal. So the whole problem is: compute two connection matrices for each bundle (one from each construction) and check they match.

> [!note]- Hint 2
> The associated-bundle side is almost free. The induced-connection theorem says the induced connection on $\operatorname{Fr}(E)\times_{\sigma}W$ has connection matrix $\sigma_{*}(A)$, where $\sigma_{*}=d_1\sigma$ is the differential of the representation and $A$ is the connection matrix of $\nabla$ on $E$. So you only need to differentiate the representations $\rho^{*}(g)=(g^{-1})^{t}$ and $\operatorname{Ad}(g)\Phi=g\Phi g^{-1}$ at $g=1$.

> [!note]- Hint 3
> Differentiate along $g(t)=\exp(tX)$. For the contragredient, $\rho^{*}(\exp tX)=(\exp(-tX))^{t}=\exp(-tX^{t})$, so $\rho^{*}_{*}(X)=-X^{t}$. For conjugation, $\operatorname{Ad}(\exp tX)\Phi=\exp(tX)\Phi\exp(-tX)$, so $\operatorname{Ad}_{*}(X)\Phi=X\Phi-\Phi X=[X,\Phi]$. Hence the associated-bundle matrices are $-A^{t}$ and $[A,\,\cdot\,]$.

> [!note]- Hint 4
> For the direct side, use the Leibniz identity on frame elements. For $E^{*}$: write $s=e\sigma$, $\alpha=e^{*}\beta$ (with $e^{*}$ the dual coframe), so $\langle\alpha,s\rangle=\beta^{t}\sigma$; expand $d(\beta^{t}\sigma)$ and match against $\langle\nabla\alpha,s\rangle+\langle\alpha,\nabla s\rangle$ to force the dual matrix to be $-A^{t}$. For $\operatorname{End}(E)$: with $\phi\leftrightarrow\Phi$ (so $\phi(e\sigma)=e\Phi\sigma$), compute $\nabla(\phi(s))-\phi(\nabla s)$ in components and read off $d\Phi+[A,\Phi]$. Both match the associated-bundle side; check the frames agree, and conclude.

---

# Solution

The strategy is to compute one complete local invariant — the connection matrix in a frame — for each of the four connections (dual and endomorphism, each in two constructions) and observe that the associated-bundle matrix, which the induced-connection theorem hands us as $\sigma_{*}(A)$, coincides with the Leibniz matrix. The representation-theoretic input is two one-line differentiations: the contragredient representation differentiates to $X\mapsto-X^{t}$ and conjugation to $X\mapsto[X,\,\cdot\,]$. Everything else is bookkeeping in a matched pair of frames.

**Step 1: Differentiate the two representations at the identity.**

The differentials are $\rho^{*}_{*}(X)=-X^{t}$ for the contragredient representation and $\operatorname{Ad}_{*}(X)=[X,\,\cdot\,]$ for conjugation.

> [!note]- Derivation
> For $X\in\mathfrak{gl}_k(\mathbb R)$ set $g(t)=\exp(tX)$, a curve in $GL_k(\mathbb R)$ with $g(0)=1$ and $\dot g(0)=X$.
>
> *Contragredient.* By definition $\rho^{*}(g)=(g^{-1})^{t}$, so
> $$\rho^{*}(\exp tX)=\big(\exp(tX)^{-1}\big)^{t}=\big(\exp(-tX)\big)^{t}=\exp(-tX^{t})\qquad(\exp(tX)^{-1}=\exp(-tX);\ (\exp Y)^{t}=\exp(Y^{t})).$$
> Differentiating at $t=0$,
> $$\rho^{*}_{*}(X)=\frac{d}{dt}\Big|_{0}\exp(-tX^{t})=-X^{t}\qquad(\text{derivative of the matrix exponential at }0).$$
>
> *Conjugation.* By definition $\operatorname{Ad}(g)\Phi=g\Phi g^{-1}$ for $\Phi\in\operatorname{End}(\mathbb R^{k})$, so
> $$\operatorname{Ad}(\exp tX)\Phi=\exp(tX)\,\Phi\,\exp(-tX).$$
> Differentiating at $t=0$ by the product rule,
> $$\operatorname{Ad}_{*}(X)\Phi=\frac{d}{dt}\Big|_{0}\exp(tX)\Phi\exp(-tX)=X\Phi+\Phi(-X)=X\Phi-\Phi X=[X,\Phi]\qquad(\text{Leibniz rule; }\tfrac{d}{dt}\big|_0\exp(\pm tX)=\pm X).$$
> Thus $\operatorname{Ad}_{*}(X)=[X,\,\cdot\,]=\operatorname{ad}_{X}$, the adjoint action of the Lie algebra. Both maps are [[Def - Representation of a Lie Algebra|Lie-algebra representations]], as differentials of Lie-group representations must be.

**Step 2: The associated-bundle connection matrices are $-A^{t}$ and $[A,\,\cdot\,]$.**

Feeding $A$ into the differentials of Step 1 through the induced-connection theorem gives connection matrix $-A^{t}$ on $E^{*}$ and $[A,\,\cdot\,]$ on $\operatorname{End}(E)$.

> [!note]- Derivation
> By the local formula of [[Thm - Principal Connections Induce Covariant Derivatives on Associated Bundles|the induced-connection theorem]], with the frame $e$ as a local section of $\operatorname{Fr}(E)$ and $e^{*}\omega=A$, the connection induced on $\operatorname{Fr}(E)\times_{\sigma}W$ satisfies, for a *constant* $w\in W$,
> $$\nabla^{\omega}[e,w]=\big[e,\ \sigma_{*}(A)\,w\big]\qquad(\partial w=0\text{ for constant }w).$$
> Hence, relative to the induced frame $\{[e,w_a]\}$ of the associated bundle, the connection matrix of $\nabla^{\omega}$ is $\sigma_{*}(A)$.
>
> *Dual bundle.* Here $W=(\mathbb R^{k})^{*}$, $\sigma=\rho^{*}$. The induced frame is $\{[e,\epsilon^{a}]\}$, where $\{\epsilon^{a}\}$ is the dual of the standard basis of $\mathbb R^{k}$; under the canonical isomorphism $\operatorname{Fr}(E)\times_{\rho^{*}}(\mathbb R^{k})^{*}\cong E^{*}$, $[e,\epsilon^{a}]\mapsto\epsilon^{a}\circ e^{-1}=e^{a}$, the $a$-th element of the dual coframe $e^{*}=(e^{1},\dots,e^{k})$ of $E$. By Step 1 the connection matrix in this frame is
> $$\rho^{*}_{*}(A)=-A^{t}.$$
>
> *Endomorphism bundle.* Here $W=\operatorname{End}(\mathbb R^{k})$, $\sigma=\operatorname{Ad}$. The induced frame is $\{[e,E_{ab}]\}$, where $E_{ab}$ is the elementary matrix; under $\operatorname{Fr}(E)\times_{\operatorname{Ad}}\operatorname{End}(\mathbb R^{k})\cong\operatorname{End}(E)$, $[e,E_{ab}]\mapsto e\circ E_{ab}\circ e^{-1}=e_a\otimes e^{b}$ (the endomorphism $x\mapsto e_a\,\langle e^{b},x\rangle$). By Step 1 the connection matrix in this frame is
> $$\operatorname{Ad}_{*}(A)=[A,\,\cdot\,].$$

**Step 3: The directly defined dual connection has connection matrix $-A^{t}$.**

Expanding the pairing Leibniz identity in the frame $e$ and coframe $e^{*}$ forces the dual connection matrix $A^{*}$ to satisfy $A^{*}=-A^{t}$.

> [!note]- Derivation
> Let $A^{*}\in\Omega^{1}(U;\mathfrak{gl}_k)$ be the connection matrix of the directly defined dual connection $\nabla^{E^{*}}$ in the dual coframe $e^{*}$, so that for $\alpha=e^{*}\beta$ with $\beta\colon U\to(\mathbb R^{k})^{*}$ (a column of components),
> $$\nabla^{E^{*}}\alpha=e^{*}\,(d\beta+A^{*}\beta).$$
> For sections $\alpha=e^{*}\beta$ of $E^{*}$ and $s=e\sigma$ of $E$, the natural pairing is
> $$\langle\alpha,s\rangle=\Big\langle\textstyle\sum_i\beta_i e^{i},\ \sum_j\sigma^{j}e_j\Big\rangle=\sum_{i,j}\beta_i\sigma^{j}\langle e^{i},e_j\rangle=\sum_i\beta_i\sigma^{i}=\beta^{t}\sigma\qquad(\langle e^{i},e_j\rangle=\delta^{i}_{j}).$$
> Differentiating the function $\beta^{t}\sigma$,
> $$d\langle\alpha,s\rangle=d(\beta^{t}\sigma)=(d\beta)^{t}\sigma+\beta^{t}\,d\sigma\qquad(\text{Leibniz rule for }d\text{ on a product of functions}). \tag{3.1}$$
> On the other hand, using $\nabla s=e(d\sigma+A\sigma)$ and the expression for $\nabla^{E^{*}}\alpha$,
> $$\langle\nabla^{E^{*}}\alpha,s\rangle+\langle\alpha,\nabla s\rangle=(d\beta+A^{*}\beta)^{t}\sigma+\beta^{t}(d\sigma+A\sigma)=(d\beta)^{t}\sigma+(A^{*}\beta)^{t}\sigma+\beta^{t}d\sigma+\beta^{t}A\sigma. \tag{3.2}$$
> The direct construction demands $(3.1)=(3.2)$. Cancelling the common terms $(d\beta)^{t}\sigma$ and $\beta^{t}d\sigma$,
> $$0=(A^{*}\beta)^{t}\sigma+\beta^{t}A\sigma=\beta^{t}(A^{*})^{t}\sigma+\beta^{t}A\sigma=\beta^{t}\big((A^{*})^{t}+A\big)\sigma\qquad((A^{*}\beta)^{t}=\beta^{t}(A^{*})^{t}).$$
> Since this holds for all component columns $\beta$ and $\sigma$, the matrix in the middle vanishes: $(A^{*})^{t}+A=0$, hence
> $$A^{*}=-A^{t}.$$
> This is exactly the connection matrix found in Step 2 for the associated-bundle dual connection, and it is computed in the same frame — the dual coframe $e^{*}$.

**Step 4: The directly defined endomorphism connection has connection matrix $[A,\,\cdot\,]$.**

Expanding the endomorphism Leibniz identity in components shows the directly defined connection is $d+[A,\,\cdot\,]$.

> [!note]- Derivation
> Represent $\phi\in\Gamma(\operatorname{End}E)$ over $U$ by the matrix-valued function $\Phi\colon U\to\operatorname{End}(\mathbb R^{k})$ defined by $\phi(e_j)=\sum_i e_i\,\Phi^{i}{}_{j}$, so that $\phi(e\sigma)=e\,\Phi\sigma$ for every $\sigma$. Fix a vector field $X$ on $U$; write $\partial_X=X$ acting on component functions and $A=A(X)$ for the value of the connection matrix on $X$ (a matrix-valued function). For a section $s=e\sigma$,
> $$\phi(s)=e\,\Phi\sigma,\qquad \nabla_X(\phi(s))=e\big(\partial_X(\Phi\sigma)+A\,\Phi\sigma\big)=e\big((\partial_X\Phi)\sigma+\Phi\,\partial_X\sigma+A\Phi\sigma\big)\qquad(\nabla=d+A;\ \text{Leibniz}), \tag{4.1}$$
> $$\phi(\nabla_X s)=\phi\big(e(\partial_X\sigma+A\sigma)\big)=e\,\Phi\big(\partial_X\sigma+A\sigma\big)=e\big(\Phi\,\partial_X\sigma+\Phi A\sigma\big). \tag{4.2}$$
> By the direct construction, $(\nabla_X\phi)(s)=\nabla_X(\phi(s))-\phi(\nabla_X s)$. Subtracting $(4.2)$ from $(4.1)$, the terms $\Phi\,\partial_X\sigma$ cancel:
> $$(\nabla_X\phi)(s)=e\big((\partial_X\Phi)\sigma+A\Phi\sigma-\Phi A\sigma\big)=e\big((\partial_X\Phi+[A,\Phi])\sigma\big)\qquad(A\Phi-\Phi A=[A,\Phi]).$$
> Since $(\nabla_X\phi)(s)=e\big((\nabla_X\phi)^{\text{matrix}}\sigma\big)$ for all $\sigma$, the matrix of $\nabla_X\phi$ is $\partial_X\Phi+[A(X),\Phi]$; that is, in the frame $\{e_a\otimes e^{b}\}$,
> $$\nabla^{\operatorname{End}}=d+[A,\,\cdot\,].$$
> This is exactly the connection matrix found in Step 2 for the associated-bundle endomorphism connection, in the same frame $\{e_a\otimes e^{b}\}$.

**Step 5: Conclude that each pair of connections coincides.**

Equal connection matrices in the same covering family of frames give equal connections.

> [!note]- Derivation
> On $E^{*}$, the associated-bundle connection (Step 2) and the direct connection (Step 3) both have connection matrix $-A^{t}$ relative to the dual coframe $e^{*}$ over $U$. On $\operatorname{End}(E)$, the associated-bundle connection (Step 2) and the direct connection (Step 4) both have connection matrix $[A,\,\cdot\,]$ relative to the frame $\{e_a\otimes e^{b}\}$ over $U$. A [[Def - Connection Matrix and Local Form of a Connection|connection is determined by its connection matrix]] in a frame: $\nabla(\text{frame}\cdot c)=\text{frame}\cdot(dc+(\text{matrix})\,c)$ prescribes it on every section over the frame's domain. Hence on each bundle the two connections agree over $U$. Since $M$ is covered by domains of local frames of $E$ (and each such frame induces the dual coframe and the endomorphism frame used above), the two connections agree over all of $M$. Therefore the associated-bundle induced connections on $E^{*}$ and $\operatorname{End}(E)$ are the direct induced connections of chapter II.

> [!note]- Complete formal solution
> **Claim.** For a connection $\nabla$ on a rank-$k$ vector bundle $E$ with local connection matrix $A$, the connection induced on $E^{*}=\operatorname{Fr}(E)\times_{\rho^{*}}(\mathbb R^{k})^{*}$ by the induced-connection theorem equals the direct dual connection ($d\langle\alpha,s\rangle=\langle\nabla\alpha,s\rangle+\langle\alpha,\nabla s\rangle$), and the connection induced on $\operatorname{End}(E)=\operatorname{Fr}(E)\times_{\operatorname{Ad}}\operatorname{End}(\mathbb R^{k})$ equals the direct endomorphism connection ($\nabla(\phi(s))=(\nabla\phi)(s)+\phi(\nabla s)$).
>
> *Proof.* **Differentials of the representations.** With $g(t)=\exp(tX)$: $\rho^{*}(\exp tX)=(\exp(-tX))^{t}=\exp(-tX^{t})$ gives $\rho^{*}_{*}(X)=-X^{t}$; and $\operatorname{Ad}(\exp tX)\Phi=\exp(tX)\Phi\exp(-tX)$ gives $\operatorname{Ad}_{*}(X)\Phi=[X,\Phi]$.
>
> **Associated-bundle matrices.** By the induced-connection theorem, with $e$ a local frame regarded as a section of $\operatorname{Fr}(E)$ and $e^{*}\omega=A$, the induced connection on $\operatorname{Fr}(E)\times_{\sigma}W$ has, relative to the frame $\{[e,w_a]\}$ and a constant basis, connection matrix $\sigma_{*}(A)$. For $E^{*}$ the induced frame $\{[e,\epsilon^{a}]\}$ is the dual coframe $e^{*}$ and the matrix is $\rho^{*}_{*}(A)=-A^{t}$; for $\operatorname{End}(E)$ the induced frame $\{[e,E_{ab}]\}$ is $\{e_a\otimes e^{b}\}$ and the matrix is $\operatorname{Ad}_{*}(A)=[A,\,\cdot\,]$.
>
> **Direct matrices.** Writing $s=e\sigma$, $\alpha=e^{*}\beta$, the pairing is $\langle\alpha,s\rangle=\beta^{t}\sigma$; imposing $d(\beta^{t}\sigma)=(d\beta+A^{*}\beta)^{t}\sigma+\beta^{t}(d\sigma+A\sigma)$ and cancelling forces $(A^{*})^{t}+A=0$, i.e. $A^{*}=-A^{t}$. Writing $\phi\leftrightarrow\Phi$ with $\phi(e\sigma)=e\Phi\sigma$, the identity $(\nabla_X\phi)(s)=\nabla_X(\phi(s))-\phi(\nabla_X s)$ expands to $e(\partial_X\Phi+[A(X),\Phi])\sigma$, so the direct endomorphism connection is $d+[A,\,\cdot\,]$.
>
> **Conclusion.** On $E^{*}$ both connections have matrix $-A^{t}$ in the coframe $e^{*}$; on $\operatorname{End}(E)$ both have matrix $[A,\,\cdot\,]$ in the frame $\{e_a\otimes e^{b}\}$. A connection is determined by its connection matrix in a frame, and such frames cover $M$; hence the associated-bundle and direct connections coincide on each bundle. $\blacksquare$

> [!warning] Illegal but tempting shortcut
> It is tempting to argue "$E^{*}$ is dual to $E$, so its connection matrix is minus the transpose, done", without checking that the induced frame produced by the associated-bundle construction is the *dual coframe* rather than some other frame. If one compared the associated-bundle matrix $\rho^{*}_{*}(A)=-A^{t}$ against the direct matrix computed in an *unrelated* frame of $E^{*}$, the two would generally differ by the gauge term $g^{-1}dg+g^{-1}(-A^{t})g$ of a frame change, and the comparison would be vacuous. The identification $[e,\epsilon^{a}]=e^{a}$ (and $[e,E_{ab}]=e_a\otimes e^{b}$) is what licenses comparing the two matrices at all; it is a load-bearing step, not a formality.

**Independent sanity check (the endomorphism identity section is parallel).** The identity endomorphism $\operatorname{id}_E\in\Gamma(\operatorname{End}E)$ has $\Phi=I$ (the identity matrix) in every frame. The direct connection gives $\nabla^{\operatorname{End}}\operatorname{id}_E\leftrightarrow dI+[A,I]=0+0=0$, so $\operatorname{id}_E$ is parallel; and indeed the Leibniz identity reads $\nabla(\operatorname{id}_E(s))=\nabla s=(\nabla\operatorname{id}_E)(s)+\operatorname{id}_E(\nabla s)=(\nabla\operatorname{id}_E)(s)+\nabla s$, forcing $\nabla\operatorname{id}_E=0$ directly. The associated-bundle side agrees: $\operatorname{Ad}_{*}(A)I=[A,I]=0$. Both constructions make the identity section parallel, as any reasonable induced connection on $\operatorname{End}(E)$ must.

---

# Key Takeaways

**To prove two constructions of a connection agree, compute the connection matrix from each and match them in a common frame.** A connection is a differential operator, and comparing operators abstractly is awkward; but a connection is completely captured by a single local invariant, its connection matrix $A$ with $\nabla=d+A$, and two connections are equal exactly when their matrices agree in frames covering the base. This reduces "the operators are the same map" to "these two matrix-valued one-forms are equal", a computation. The reusable principle: when a bundle carries two candidate connections, do not chase the maps — extract $A$ from each and compare. The one caution, which this exercise makes concrete, is that the comparison is only legitimate in a *common* frame; matrices in different frames differ by a gauge transformation and cannot be compared entry by entry.

**The connection induced on an associated bundle is the base connection matrix pushed through the differential of the representation: $A\mapsto\sigma_{*}(A)$.** This is the single most reusable fact about induced connections. Every natural bundle built from $E$ by a functorial operation is an associated bundle of $\operatorname{Fr}(E)$ for a specific representation, and its induced connection matrix is obtained by differentiating that representation and applying it to $A$. The dictionary is short and worth memorising: the dual $E^{*}$ uses the contragredient representation, whose differential is $X\mapsto-X^{t}$, giving $-A^{t}$; the endomorphism bundle $\operatorname{End}(E)$ uses conjugation, whose differential is $X\mapsto[X,\,\cdot\,]=\operatorname{ad}_X$, giving $[A,\,\cdot\,]$; a tensor product $E\otimes F$ uses $X\mapsto X\otimes 1+1\otimes X$, giving $A_E\otimes 1+1\otimes A_F$; an exterior power $\Lambda^{p}E$ uses the corresponding derivation. The trigger is "a bundle built naturally from $E$"; the reaction is "identify the representation, differentiate it, apply to $A$". The appearance of $\operatorname{ad}_A=[A,\,\cdot\,]$ on $\operatorname{End}(E)$ is exactly why the curvature $F_\nabla\in\Omega^{2}(M;\operatorname{End}E)$ satisfies the Bianchi identity $d^{\nabla}F_\nabla=0$ with $d^{\nabla}=d+[A,\,\cdot\,]$, and why gauge transformations act on $\operatorname{End}(E)$-valued objects by conjugation.

**The transpose and the commutator are the infinitesimal shadows of "inverse-transpose" and "conjugation".** The two differentials computed here, $\rho^{*}_{*}(X)=-X^{t}$ and $\operatorname{Ad}_{*}(X)=[X,\,\cdot\,]$, are worth internalising as instances of a general pattern: differentiating a representation of a matrix group at the identity turns each group-level operation into its linearisation — inversion becomes negation, transpose stays transpose, conjugation becomes the commutator bracket. This is why the Lie algebra of $GL_k$ acts on the dual space by $-X^{t}$ and on itself by $\operatorname{ad}$, and it is the mechanism behind every "the induced connection is $d$ corrected by a bracket" statement in gauge theory. In spaced review, the fact to reconstruct is that the minus-transpose on the dual and the commutator on endomorphisms are not conventions to be memorised in isolation but forced consequences of differentiating the contragredient and conjugation representations — recover the representations and the matrices follow. The companion exercise [[Ex - Induced Connections on the Dual and Endomorphism Bundles]] establishes the same matrices from the direct Leibniz characterisation alone, without the principal bundle; the present exercise is what closes the loop by identifying that direct construction with the associated-bundle one.
