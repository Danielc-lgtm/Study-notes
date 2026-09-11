---
type: exercise
subject: gauge-theory
prereqs:
  - "Def - Chern Classes"
  - "Thm - Chern-Weil Theorem"
  - "Thm - Naturality and Isomorphism Invariance of Characteristic Classes"
  - "Thm - Trivial Bundles Have Vanishing Characteristic Classes"
  - "Thm - Axioms and Properties of Chern Classes"
difficulty: "⭐"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $E\to M$ be a complex vector bundle of rank $r$ over a smooth manifold $M$, and let
$$c(E)=1+c_1(E)+\cdots+c_r(E)\in H^{\bullet}_{dR}(M)$$
be its total Chern class, defined from the curvature of a unitary connection by $c(E)=\big[\det\!\big(1+\tfrac{i}{2\pi}F\big)\big]$. Prove the two properties Haydys lists as Exercise 88(a) and 88(c):

- **(a) Isomorphism invariance.** If $E\cong E'$ as complex vector bundles over $M$, then $c(E)=c(E')$; that is, the total Chern class depends only on the isomorphism class of $E$.
- **(c) Triviality forces $c=1$.** If $E$ is trivial, meaning $E\cong\underline{\mathbb{C}}^{r}:=M\times\mathbb{C}^{r}$, then $c(E)=1$ (equivalently $c_j(E)=0$ for every $j\ge1$).

The intended route is the one the spec names: deduce (a) from the naturality-and-isomorphism-invariance theorem, and (c) from the trivial-bundle theorem, reducing (c) to (a) by exhibiting a flat connection on the product bundle.

**Recall:**

The objects in play are the Chern classes of a complex vector bundle, the Chern–Weil theorem that makes them independent of the connection, the invariance of characteristic classes under bundle isomorphism, and the vanishing of characteristic classes on bundles carrying a flat connection.

![[Def - Chern Classes#The Definition]]

Concretely, for a complex vector bundle $E$ of rank $r$ we fix a Hermitian structure $h$, take any connection $\nabla$ compatible with $h$ (a **unitary connection**, whose connection matrix $A\in\Omega^1(U;\mathfrak{u}(r))$ is skew-Hermitian in a unitary frame), form its curvature $F=F_\nabla\in\Omega^2(M;\operatorname{End}E)$, and set
$$c(E)=\Big[\det\!\Big(1+\tfrac{i}{2\pi}F\Big)\Big],\qquad c_j(E)=\big[c_j(F)\big],$$
where $c_j(F)$ is the degree-$j$ part of $\det(1+\tfrac{i}{2\pi}F)$, a closed real-valued $2j$-form. The page **[[Def - Chern Classes]]** proves that this class is independent of the choice of unitary connection and of the Hermitian structure $h$; both facts are used below.

![[Thm - Chern-Weil Theorem#Statement]]

The **[[Thm - Chern-Weil Theorem|Chern–Weil theorem]]** supplies the two facts the definition rests on: for an $\operatorname{Ad}$-invariant polynomial $p$ of degree $d$ and a connection with curvature $F$, the form $p(F)$ is closed, and its de Rham class is independent of the connection. The coefficients $c_j$ of $\det(\lambda\,1+\tfrac{i}{2\pi}\xi)$ are such $\operatorname{Ad}$-invariant polynomials on $\mathfrak{u}(r)$; in particular $c_j(g\xi g^{-1})=c_j(\xi)$ for every $g\in U(r)$ (indeed every $g\in GL_r(\mathbb{C})$), because $\det(\lambda\,1+\tfrac{i}{2\pi}g\xi g^{-1})=\det\!\big(g(\lambda\,1+\tfrac{i}{2\pi}\xi)g^{-1}\big)=\det(\lambda\,1+\tfrac{i}{2\pi}\xi)$.

![[Thm - Naturality and Isomorphism Invariance of Characteristic Classes#Statement]]

The **[[Thm - Naturality and Isomorphism Invariance of Characteristic Classes|isomorphism-invariance theorem]]** states, among its parts, that if $\phi\colon P\to P'$ is an isomorphism of principal $G$-bundles over $M$ then $c_p(P)=c_p(P')$ for every invariant polynomial $p$; hence a characteristic class depends only on the isomorphism class of the bundle. This is the principal-bundle statement standing behind part (a); the work in the solution is to turn a *complex-vector-bundle* isomorphism into a principal-$U(r)$-bundle isomorphism.

![[Thm - Trivial Bundles Have Vanishing Characteristic Classes#Statement]]

The **[[Thm - Trivial Bundles Have Vanishing Characteristic Classes|trivial-bundle theorem]]** states that if a principal bundle $P$ is trivial — or, more generally, admits a flat connection — then $c_p(P)=0$ for every invariant polynomial $p$ of positive degree. The mechanism is that a flat connection has $F=0$, so $p(F)=p(0)=0$ already at the level of forms whenever $\deg p\ge1$.

The bridge that makes both parts run is the passage from a bundle to a connection whose curvature we can control: an isomorphism lets us *transport* a connection, and triviality lets us *choose* the flat product connection.

---

# Convergent Strategy

**Problem class.** Both parts are instances of a single manoeuvre: *deduce a property of a curvature-defined invariant from the two independence properties built into its definition* — independence of the connection (Chern–Weil) and independence of the Hermitian structure. The Chern class is defined by a choice (a metric, a connection), so every general property of it is proved by making the *cleverest* choice and then invoking independence to say the answer did not depend on the choice. Part (a) makes the choice "transport a connection across the isomorphism"; part (c) makes the choice "use the flat product connection".

**Assumption pattern.** In (a) the only hypothesis is an isomorphism $\phi\colon E\to E'$; the recognisable trigger is that an isomorphism can carry *all auxiliary data* — a Hermitian metric, a connection — from one bundle to the other, so that the two bundles are compared with matched data. In (c) the only hypothesis is triviality, $E\cong\underline{\mathbb{C}}^{r}$; the trigger is that the product bundle has a canonical *flat* connection (the exterior derivative acting componentwise), whose curvature vanishes identically, which is exactly the hypothesis of the trivial-bundle theorem.

**Theorem routing.** For (a): transport the Hermitian structure of $E'$ back along $\phi$ so that $\phi$ becomes a *unitary* isomorphism; a unitary isomorphism of Hermitian bundles induces an isomorphism of unitary frame bundles $\operatorname{Fr}_U(E)\to\operatorname{Fr}_U(E')$; apply **[[Thm - Naturality and Isomorphism Invariance of Characteristic Classes]]** to conclude $c_j(\operatorname{Fr}_U(E))=c_j(\operatorname{Fr}_U(E'))$; then use Hermitian-structure independence from **[[Def - Chern Classes]]** to identify these with $c_j(E)$ and $c_j(E')$. For (c): the product bundle carries the flat product connection, so by **[[Thm - Trivial Bundles Have Vanishing Characteristic Classes]]** its Chern classes vanish in positive degree, giving $c(\underline{\mathbb{C}}^{r})=1$; then a general trivial $E\cong\underline{\mathbb{C}}^{r}$ has $c(E)=c(\underline{\mathbb{C}}^{r})=1$ by part (a).

**Key decision point.** The one non-obvious move in (a) is *transporting the metric before comparing the classes*: without matched Hermitian structures, the isomorphism $\phi$ is not unitary and does not directly give a principal-$U(r)$-bundle isomorphism, so the packaged theorem does not apply on the nose. The one non-obvious move in (c) is recognising that "trivial" is precisely "isomorphic to a bundle carrying a flat connection", so that part (c) is not an independent computation but a *corollary of (a) plus one flat example*. Seeing (c) as "(a) applied to the flat model" is the whole point; it is why the two parts belong on the same page.

---

# Legal Operations Used

This solution deploys the following legal operations from **[[Gauge Theory VI — Chern–Weil Theory, Characteristic Classes, and the Chern–Simons Functional#Legal Operations|the topic page's Legal Operations]]** (numbering to be reconciled when the topic page is assembled):

1. **Transport auxiliary data along a bundle isomorphism.** Given $\phi\colon E\to E'$ and a Hermitian structure $h'$ on $E'$, pull it back to $h:=\phi^{*}h'$ on $E$, so that $\phi$ becomes a *unitary* isomorphism $(E,h)\to(E',h')$. This is the standard "pull structure back along an iso" operation, applied to a fibre metric.

2. **Pass from a compatible unitary isomorphism to an isomorphism of unitary frame bundles.** A unitary isomorphism of Hermitian bundles sends unitary frames to unitary frames and commutes with the right $U(r)$-action, hence descends to an isomorphism $\operatorname{Fr}_U(E)\to\operatorname{Fr}_U(E')$ of principal $U(r)$-bundles.

3. **Invoke isomorphism invariance of characteristic classes.** Apply **[[Thm - Naturality and Isomorphism Invariance of Characteristic Classes]]** to the induced principal-bundle isomorphism to equate the Chern–Weil classes.

4. **Use independence of the defining choices (Chern–Weil and Hermitian-structure independence).** Read $c_j(\operatorname{Fr}_U(E,h))=c_j(E)$ off **[[Def - Chern Classes]]**, which proves the class is the same for any Hermitian structure and any compatible connection.

5. **Exhibit and use a flat connection on the product bundle.** On $\underline{\mathbb{C}}^{r}=M\times\mathbb{C}^{r}$ the componentwise exterior derivative $d$ is a connection with vanishing curvature; feed it to **[[Thm - Trivial Bundles Have Vanishing Characteristic Classes]]**.

6. **Reduce a general trivial bundle to the product model by isomorphism invariance.** Combine operation 3–4 (part (a)) with operation 5 to move from $\underline{\mathbb{C}}^{r}$ to any $E\cong\underline{\mathbb{C}}^{r}$.

---

# Hints

> [!note]- Hint 1
> The Chern class is defined by *choosing* a Hermitian metric and a compatible connection, and the definition comes with a guarantee that the answer does not depend on those choices. For a general property, do not compute — instead *make the smartest choice* and let the independence do the talking. In (a) the smart choice is a connection related across the isomorphism; in (c) it is a connection whose curvature you already know.

> [!note]- Hint 2
> For (a): an isomorphism $\phi\colon E\to E'$ can carry the metric of $E'$ back to $E$. Once the two metrics match, $\phi$ becomes a *unitary* isomorphism. What does a unitary isomorphism do to unitary frames, and hence to the unitary frame bundles $\operatorname{Fr}_U(E)$ and $\operatorname{Fr}_U(E')$?

> [!note]- Hint 3
> For (a), once $\phi$ induces an isomorphism $\operatorname{Fr}_U(E)\cong\operatorname{Fr}_U(E')$ of principal $U(r)$-bundles, the theorem [[Thm - Naturality and Isomorphism Invariance of Characteristic Classes]] equates their characteristic classes on the nose. All that remains is to remember, from [[Def - Chern Classes]], that $c_j(E)$ is defined as $c_j(\operatorname{Fr}_U(E))$ for *any* Hermitian structure — so the metric transport in Hint 2 did not change the answer.

> [!note]- Hint 4
> For (c): the product bundle $\underline{\mathbb{C}}^{r}=M\times\mathbb{C}^{r}$ has the connection $d$ acting componentwise. Its connection matrix is $A=0$, so its curvature is $F=dA+A\wedge A=0$. A connection with vanishing curvature is *flat*. Now read the trivial-bundle theorem: a flat connection has $c_j(F)=c_j(0)=0$ for $j\ge1$. What does that give for $c(\underline{\mathbb{C}}^{r})$, and how does part (a) finish a general trivial $E$?

---

# Solution

The Chern class is manufactured from a Hermitian metric and a compatible connection, and the definition guarantees the result is independent of both. Part (a) exploits that independence twice: transport the metric of $E'$ back to $E$ so the isomorphism is unitary, obtain an isomorphism of unitary frame bundles, and apply isomorphism invariance; the metric transport is harmless because the class does not depend on the metric. Part (c) then falls out: the product bundle carries the flat connection $d$ with $F=0$, so its Chern classes vanish in positive degree, and any bundle isomorphic to the product bundle inherits $c=1$ by part (a).

**Step 1 (part (a)): Transport the Hermitian structure so that $\phi$ is a unitary isomorphism.**

Let $\phi\colon E\to E'$ be an isomorphism of complex vector bundles over $M$. Choose a Hermitian structure $h'$ on $E'$ and set $h:=\phi^{*}h'$ on $E$; then $h$ is a Hermitian structure and $\phi\colon(E,h)\to(E',h')$ is fibrewise unitary.

> [!note]- Derivation
> We are given a $\mathbb{C}$-linear bundle isomorphism $\phi\colon E\to E'$ over the identity of $M$; we must produce matched metrics under which $\phi$ preserves the inner product.
>
> **Choose a metric on $E'$ and pull it back.** Every complex vector bundle admits a Hermitian structure (a fibrewise Hermitian inner product varying smoothly with the base point), so fix one, $h'$, on $E'$. Define, for $u,v\in E_m$,
> $$h_m(u,v):=h'_m\big(\phi_m u,\ \phi_m v\big)\qquad\text{(definition of the pulled-back metric }h:=\phi^{*}h').$$
> **Check $h$ is a Hermitian structure.** For each $m$, $\phi_m\colon E_m\to E'_m$ is a $\mathbb{C}$-linear isomorphism, and $h'_m$ is a Hermitian inner product; the composite $h_m(u,v)=h'_m(\phi_m u,\phi_m v)$ is therefore linear in $u$, conjugate-linear in $v$ (inherited slot by slot from $h'_m$), and Hermitian-symmetric; it is positive definite because $h_m(u,u)=h'_m(\phi_m u,\phi_m u)>0$ for $u\neq0$ (since $\phi_m u\neq0$ by injectivity of $\phi_m$ and positive definiteness of $h'_m$). Smoothness in $m$ follows from smoothness of $\phi$ and of $h'$. Hence $h$ is a Hermitian structure on $E$.
> **Read off that $\phi$ is unitary.** By the very definition of $h$, for all $u,v\in E_m$,
> $$h'_m(\phi_m u,\phi_m v)=h_m(u,v)\qquad\text{(rearranging the definition of }h),$$
> which is precisely the statement that $\phi_m\colon(E_m,h_m)\to(E'_m,h'_m)$ is a unitary map. Thus $\phi\colon(E,h)\to(E',h')$ is a unitary isomorphism of Hermitian bundles.

**Step 2 (part (a)): The unitary isomorphism induces an isomorphism of unitary frame bundles, and isomorphism invariance gives $c(E)=c(E')$.**

The unitary isomorphism $\phi$ carries unitary frames of $(E,h)$ to unitary frames of $(E',h')$, defining an isomorphism $\Phi\colon\operatorname{Fr}_U(E)\to\operatorname{Fr}_U(E')$ of principal $U(r)$-bundles; isomorphism invariance of characteristic classes and Hermitian-structure independence then yield $c_j(E)=c_j(E')$ for every $j$.

> [!note]- Derivation
> We must turn the fibrewise-unitary $\phi$ of Step 1 into a genuine isomorphism of the $U(r)$-frame bundles and then quote the invariance theorem.
>
> **Construct the induced frame-bundle map.** Recall that the unitary frame bundle $\operatorname{Fr}_U(E)$ has, as its fibre over $m$, the set of unitary bases $e=(e_1,\dots,e_r)$ of $(E_m,h_m)$, with $U(r)$ acting on the right by $e\cdot g=\big(\sum_i e_i g_{i1},\dots,\sum_i e_i g_{ir}\big)$. Define
> $$\Phi(e):=\phi\circ e=(\phi_m e_1,\dots,\phi_m e_r)\qquad\text{(post-compose each frame vector with }\phi_m).$$
> **Check $\Phi$ lands in unitary frames.** Since $\phi_m$ is unitary (Step 1), it sends the unitary basis $(e_1,\dots,e_r)$ of $(E_m,h_m)$ to a unitary basis $(\phi_m e_1,\dots,\phi_m e_r)$ of $(E'_m,h'_m)$: unitarity preserves inner products, hence orthonormality, and preserves linear independence, hence the basis property. So $\Phi(e)\in\operatorname{Fr}_U(E')_m$.
> **Check $\Phi$ is $U(r)$-equivariant.** For $g\in U(r)$,
> $$\Phi(e\cdot g)=\phi\circ(e\cdot g)=(\phi\circ e)\cdot g=\Phi(e)\cdot g\qquad\text{(because }\phi_m\text{ is }\mathbb{C}\text{-linear, so it commutes with the linear-combination action of }g).$$
> $\Phi$ covers the identity of $M$ (it preserves fibres) and is a diffeomorphism with inverse $e'\mapsto\phi^{-1}\circ e'$; hence $\Phi\colon\operatorname{Fr}_U(E)\to\operatorname{Fr}_U(E')$ is an isomorphism of principal $U(r)$-bundles over $M$.
> **Apply isomorphism invariance.** By **[[Thm - Naturality and Isomorphism Invariance of Characteristic Classes]]** — restated: *an isomorphism of principal $G$-bundles over $M$ induces equality $c_p(P)=c_p(P')$ of Chern–Weil classes for every invariant polynomial $p$* — applied to $\Phi$ and to each Chern polynomial $c_j\in I(U(r))$,
> $$c_j\big(\operatorname{Fr}_U(E)\big)=c_j\big(\operatorname{Fr}_U(E')\big)\qquad\text{(isomorphism invariance for }\Phi).$$
> **Discharge the metric choice.** By **[[Def - Chern Classes]]**, the Chern class of a complex vector bundle is defined as $c_j(E):=c_j(\operatorname{Fr}_U(E,h))$ for *any* Hermitian structure, and that page proves the value is independent of the Hermitian structure chosen. Therefore $c_j(\operatorname{Fr}_U(E,h))=c_j(E)$ and $c_j(\operatorname{Fr}_U(E',h'))=c_j(E')$, and the displayed equality becomes
> $$c_j(E)=c_j(E')\qquad(j=0,1,\dots,r).$$
> **Mechanism, made explicit at the curvature level.** The same conclusion can be seen directly: transporting a unitary connection $\nabla'$ on $(E',h')$ to $\nabla:=\phi^{-1}\circ\nabla'\circ\phi$ on $(E,h)$ gives a unitary connection whose curvature is the conjugate $F_\nabla=\phi^{-1}F_{\nabla'}\phi$, and by the $\operatorname{Ad}$-invariance of $c_j$ recorded in the Recall, $c_j(F_\nabla)=c_j(\phi^{-1}F_{\nabla'}\phi)=c_j(F_{\nabla'})$ *as $2j$-forms*; taking classes and using connection independence from **[[Thm - Chern-Weil Theorem]]** gives $c_j(E)=[c_j(F_\nabla)]=[c_j(F_{\nabla'})]=c_j(E')$. Summing over $j$ in either derivation, $c(E)=c(E')$. This proves part (a).

**Step 3 (part (c)): The product bundle has $c=1$, via the flat product connection.**

On $\underline{\mathbb{C}}^{r}=M\times\mathbb{C}^{r}$ the componentwise exterior derivative $d$ is a connection with vanishing curvature; by the trivial-bundle theorem its Chern classes vanish in positive degree, so $c(\underline{\mathbb{C}}^{r})=1$.

> [!note]- Derivation
> We must produce a flat connection on the product bundle and feed it to the vanishing theorem.
>
> **Write down the product connection.** In the global frame $e=(e_1,\dots,e_r)$ of $\underline{\mathbb{C}}^{r}$ given by the constant sections $e_i(m)=(m,\varepsilon_i)$ (with $\varepsilon_1,\dots,\varepsilon_r$ the standard basis of $\mathbb{C}^{r}$), define $\nabla^{0}s:=ds$ componentwise: if $s=\sum_i s^i e_i$ with $s^i\in C^\infty(M)$, then $\nabla^{0}s=\sum_i (ds^i)\otimes e_i$. This satisfies the Leibniz rule $\nabla^{0}(fs)=df\otimes s+f\,\nabla^{0}s$ (the product rule for $d$ applied to each component), so it is a connection. Its connection matrix in the frame $e$ is $A=0$, because $\nabla^{0}e_i=d(1)\otimes e_i=0$ for each constant frame vector.
> **Compute the curvature.** By the local curvature formula (series convention $F=dA+A\wedge A$),
> $$F_{\nabla^{0}}=dA+A\wedge A=d0+0\wedge0=0\qquad\text{(since }A=0).$$
> Thus $\nabla^{0}$ is a **flat** connection: its curvature vanishes identically. Equivalently, the product bundle is a trivial bundle in the sense of the vanishing theorem.
> **Apply the trivial-bundle theorem.** By **[[Thm - Trivial Bundles Have Vanishing Characteristic Classes]]** — restated: *if a principal bundle is trivial, or more generally admits a flat connection, then $c_p=0$ for every invariant polynomial $p$ of positive degree* — applied to the unitary frame bundle of $\underline{\mathbb{C}}^{r}$ with its standard Hermitian structure and the flat connection $\nabla^{0}$ (which is unitary for that structure, since the constant frame is unitary and parallel), we get $c_j(\underline{\mathbb{C}}^{r})=0$ for all $j\ge1$. Directly, this is visible from the curvature: $c_j(F_{\nabla^{0}})=c_j(0)=0$ for $j\ge1$, because $c_j$ is homogeneous of degree $j\ge1$ and so vanishes at the zero matrix. Since $c_0(E)=1$ for any bundle (it is the degree-zero, constant term $\det(1+\tfrac{i}{2\pi}\cdot0)=1$), we conclude
> $$c(\underline{\mathbb{C}}^{r})=1+0+\cdots+0=1.$$

**Step 4 (part (c)): A general trivial bundle inherits $c=1$ by part (a).**

If $E$ is trivial, then $E\cong\underline{\mathbb{C}}^{r}$, and part (a) gives $c(E)=c(\underline{\mathbb{C}}^{r})=1$.

> [!note]- Derivation
> By definition, $E$ **trivial** means there is an isomorphism of complex vector bundles $\psi\colon E\to\underline{\mathbb{C}}^{r}$ over $M$. Applying part (a) — proved in Steps 1–2, restated: *isomorphic complex vector bundles have equal total Chern class* — to $\psi$,
> $$c(E)=c(\underline{\mathbb{C}}^{r})\qquad\text{(part (a) for the isomorphism }\psi).$$
> Combining with Step 3, $c(\underline{\mathbb{C}}^{r})=1$, we obtain
> $$c(E)=1,$$
> that is, $c_j(E)=0$ for every $j\ge1$. This is exactly part (c).

> [!note]- Complete formal solution
> **Claim.** For a complex vector bundle $E\to M$ of rank $r$: (a) if $E\cong E'$ then $c(E)=c(E')$; (c) if $E$ is trivial then $c(E)=1$.
>
> **Part (a).** Let $\phi\colon E\to E'$ be a $\mathbb{C}$-linear bundle isomorphism over $M$. Fix a Hermitian structure $h'$ on $E'$ and set $h:=\phi^{*}h'$, $h_m(u,v):=h'_m(\phi_m u,\phi_m v)$. Then $h$ is a Hermitian structure on $E$ (linear/conjugate-linear/Hermitian slotwise from $h'$; positive definite by injectivity of $\phi_m$; smooth), and $\phi\colon(E,h)\to(E',h')$ is fibrewise unitary since $h'_m(\phi_m u,\phi_m v)=h_m(u,v)$.
>
> Define $\Phi\colon\operatorname{Fr}_U(E)\to\operatorname{Fr}_U(E')$ by $\Phi(e_1,\dots,e_r)=(\phi e_1,\dots,\phi e_r)$. Unitarity of $\phi_m$ sends unitary frames to unitary frames; $\mathbb{C}$-linearity of $\phi_m$ gives $U(r)$-equivariance $\Phi(e\cdot g)=\Phi(e)\cdot g$; $\Phi$ covers $\mathrm{id}_M$ and has inverse $e'\mapsto\phi^{-1}\circ e'$. Hence $\Phi$ is an isomorphism of principal $U(r)$-bundles. By [[Thm - Naturality and Isomorphism Invariance of Characteristic Classes]], $c_j(\operatorname{Fr}_U(E))=c_j(\operatorname{Fr}_U(E'))$ for all $j$. By [[Def - Chern Classes]] (Hermitian-structure independence), $c_j(\operatorname{Fr}_U(E,h))=c_j(E)$ and $c_j(\operatorname{Fr}_U(E',h'))=c_j(E')$. Therefore $c_j(E)=c_j(E')$ for all $j$, i.e. $c(E)=c(E')$.
>
> **Part (c).** On $\underline{\mathbb{C}}^{r}=M\times\mathbb{C}^{r}$, the componentwise exterior derivative $\nabla^{0}=d$ is a connection with connection matrix $A=0$ in the constant unitary frame, so $F_{\nabla^{0}}=dA+A\wedge A=0$. Then $c_j(F_{\nabla^{0}})=c_j(0)=0$ for $j\ge1$ (homogeneity of degree $j$), while $c_0=1$; hence $c(\underline{\mathbb{C}}^{r})=1$. Equivalently, $\nabla^{0}$ is flat, so [[Thm - Trivial Bundles Have Vanishing Characteristic Classes]] gives $c_j(\underline{\mathbb{C}}^{r})=0$ for $j\ge1$.
>
> If $E$ is trivial, there is an isomorphism $\psi\colon E\to\underline{\mathbb{C}}^{r}$; by part (a), $c(E)=c(\underline{\mathbb{C}}^{r})=1$. $\blacksquare$

> [!warning] Illegal but tempting shortcut
> One might try to prove (a) by simply declaring "$c_j$ is defined from curvature, and isomorphic bundles have the same curvature". This is false as stated: $E$ and $E'$ carry *different* connections with *different* curvature forms; there is no canonical identification of $\Omega^2(M;\operatorname{End}E)$ with $\Omega^2(M;\operatorname{End}E')$ until an isomorphism is fixed. What is true — and what the derivation uses — is that once $\phi$ is fixed, the transported curvatures are *conjugate*, $F_\nabla=\phi^{-1}F_{\nabla'}\phi$, and it is the $\operatorname{Ad}$-invariance of the Chern polynomial $c_j$, not any equality of the curvatures themselves, that makes $c_j(F_\nabla)=c_j(F_{\nabla'})$. The extra condition that legitimises the shortcut is precisely "the polynomial evaluated on curvature is conjugation-invariant"; drop $\operatorname{Ad}$-invariance and the argument collapses.

---

# Key Takeaways

**A curvature-defined invariant is proved to have a general property by making the cleverest choice of connection (or metric) and then invoking the independence guarantees.** The Chern class is not a single form but a *class* that the definition certifies to be independent of the connection (Chern–Weil) and of the Hermitian structure. This turns every structural theorem about Chern classes into an exercise in *choosing well*: for isomorphism invariance, choose a connection transported across the isomorphism, so the two curvatures become conjugate; for triviality, choose the flat product connection, so the curvature is literally zero. The reusable principle is that the freedom in the definition is not a nuisance to be tolerated but a lever: whenever an invariant is defined "pick any $X$; the answer is independent of $X$", you may pick the $X$ that makes the property you want transparent, and the independence clause retroactively removes the choice. The trigger condition is any invariant advertised with an "independent of the choice" theorem; the diagnostic is to ask "which choice makes this hypothesis visible in the curvature?"

**Isomorphism invariance of Chern classes rests on $\operatorname{Ad}$-invariance of the Chern polynomial, not on any sameness of the curvature forms.** It is worth isolating *why* isomorphic bundles have equal Chern classes, because the naive reason is wrong. Transporting a connection along $\phi$ produces curvatures that are conjugate, $F_\nabla=\phi^{-1}F_{\nabla'}\phi$, and conjugate matrices are generally different; what saves the day is that $c_j$ is built from $\det(1+\tfrac{i}{2\pi}\xi)$, which is unchanged under $\xi\mapsto g\xi g^{-1}$. This is the same reason $\operatorname{tr}$ and $\det$ descend from matrices to endomorphisms, and it is the reason characteristic classes exist at all: they are the invariant polynomials in the curvature. The transferable diagnostic is that any quantity you hope depends only on an isomorphism class must be assembled from *conjugation-invariant* data; if your candidate is not conjugation-invariant, it is basis-dependent and cannot be an isomorphism invariant. The whole theory of characteristic classes is the systematic exploitation of $I(G)$, the ring of $\operatorname{Ad}$-invariant polynomials, for exactly this reason.

**Vanishing on trivial bundles is the first and most-used obstruction: a nonzero Chern class proves nontriviality.** Part (c) is small to prove but large in consequence. Its contrapositive, *if $c_j(E)\neq0$ for some $j\ge1$ then $E$ is not trivial*, is the working form of the entire subject: one detects that a bundle is twisted by computing a curvature integral and finding it nonzero. This is how the tangent bundle of $S^2$ is shown nontrivial (its Euler/first Chern number is $2$, see **[[Ex - The Tangent Bundle of S^2 is Nontrivial via Chern Classes]]**), how the tautological bundle $\mathcal{O}(-1)\to\mathbb{CP}^1$ is shown nontrivial (its first Chern number is $-1$, see **[[Ex - The Chern Number of the Hopf Line Bundle over CP^1 is Minus One]]**), and how instanton numbers obstruct triviality of $SU(2)$-bundles over four-manifolds. The reason the obstruction works is exactly the argument of this page: triviality supplies a flat connection, a flat connection has $F=0$, and every positive-degree invariant polynomial annihilates $0$. The trigger for reaching for this tool is any question of the form "is this bundle trivial?"; the reaction is "compute a characteristic number and hope it is nonzero." A companion drill for the flat-connection half is **[[Ex - Chern-Weil Forms of the Flat Product Connection Vanish]]**, and the vanishing-above-the-rank refinement is **[[Ex - Chern Classes Vanish above the Rank of the Non-Trivial Summand]]**.
