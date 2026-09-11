---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - Principal Connections Induce Covariant Derivatives on Associated Bundles"
  - "Thm - The Standard Connection on the Hopf Bundle"
  - "Ex - The Tautological Line Bundle over CP^n is Associated to the Hopf Bundle"
  - "Def - The Hopf Bundle"
  - "Def - Curvature of a Principal Connection"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $\pi\colon S^{2n+1}\to\mathbb{CP}^n$ be the **Hopf bundle**, the principal $U(1)$-bundle carrying the standard **Hopf connection**
$$a_z(u)=\langle v(z),u\rangle\,i,\qquad v(z)=iz,\quad u\in T_zS^{2n+1},$$
where $\langle\cdot,\cdot\rangle$ is the real inner product of $\mathbb{R}^{2n+2}=\mathbb{C}^{n+1}$ and $\mathfrak{u}(1)=i\mathbb{R}$. Let $\mathcal{O}(-1)\to\mathbb{CP}^n$ be the **tautological line bundle**,
$$\mathcal{O}(-1)=\{([z],w)\in\mathbb{CP}^n\times\mathbb{C}^{n+1}\mid w\in\mathbb{C}z\},$$
a complex line subbundle of the trivial bundle $\underline{\mathbb{C}^{n+1}}=\mathbb{CP}^n\times\mathbb{C}^{n+1}$, and let $\varrho_1\colon U(1)\to GL(\mathbb{C})$, $\varrho_1(\lambda)w=\lambda w$, be the standard one-dimensional representation, under which $\mathcal{O}(-1)\cong S^{2n+1}\times_{\varrho_1}\mathbb{C}$.

Equip $\mathcal{O}(-1)$ with the covariant derivative $\nabla=\nabla^a$ induced from the Hopf connection $a$ through the representation $\varrho_1$. Prove:

1. **Projected form.** Under the inclusion $\mathcal{O}(-1)\subset\underline{\mathbb{C}^{n+1}}$, the induced connection is the orthogonal projection of the ambient trivial connection $d$ onto the tautological line:
$$\nabla s=\operatorname{pr}(ds),\qquad\operatorname{pr}_{[z]}\colon\mathbb{C}^{n+1}\to\mathbb{C}z\ \text{the Hermitian orthogonal projection,}$$
where $s\colon\mathbb{CP}^n\to\mathbb{C}^{n+1}$ is a section of $\mathcal{O}(-1)$ (so $s([z])\in\mathbb{C}z$) and $ds$ is its componentwise differential as a $\mathbb{C}^{n+1}$-valued function.
2. **Hermitian.** $\nabla$ is compatible with the Hermitian metric on $\mathcal{O}(-1)$ inherited from the standard Hermitian metric $h$ on $\mathbb{C}^{n+1}$: for all sections $s_1,s_2$,
$$d\,h(s_1,s_2)=h(\nabla s_1,s_2)+h(s_1,\nabla s_2).$$
3. **Curvature.** Using part (c) of the induced-connection theorem, identify the curvature $F_\nabla\in\Omega^2(\mathbb{CP}^n;\operatorname{End}\mathcal{O}(-1))$ as multiplication by the Hopf curvature $F_a\in\Omega^2(\mathbb{CP}^n;i\mathbb{R})$; for $n=1$ evaluate it explicitly.

**Recall:**

The objects in play are the Hopf connection on $S^{2n+1}$, the covariant derivative that a principal connection induces on an associated bundle through equation (47), the tautological line bundle realised as an associated bundle, and the curvature of the induced connection.

![[Thm - The Standard Connection on the Hopf Bundle#Statement]]

![[Thm - Principal Connections Induce Covariant Derivatives on Associated Bundles#Statement]]

Two conventions of this series are used throughout. The associated bundle $S^{2n+1}\times_{\varrho_1}\mathbb{C}$ is the quotient of $S^{2n+1}\times\mathbb{C}$ by the right action $(z,w)\cdot\lambda=(z\lambda,\varrho_1(\lambda^{-1})w)=(z\lambda,\lambda^{-1}w)$, its points written $[z,w]$; a section $s$ of it corresponds to an **equivariant function** $\hat s\colon S^{2n+1}\to\mathbb{C}$ with $\hat s(z\lambda)=\varrho_1(\lambda^{-1})\hat s(z)=\lambda^{-1}\hat s(z)$, via $s([z])=[z,\hat s(z)]$. The **derivative of the representation** is $\rho_*:=(\varrho_1)_*\colon\mathfrak{u}(1)\to\operatorname{End}(\mathbb{C})=\mathbb{C}$, and since $\varrho_1(e^{it})w=e^{it}w$ we have $\rho_*(it)=it$: the Lie-algebra element $it\in i\mathbb{R}$ acts on $\mathbb{C}$ as multiplication by $it$. Consequently the wedge-action $a\cdot\hat s$ appearing in equation (47) is $\rho_*(a)\hat s=a\hat s$, ordinary scalar multiplication of the $i\mathbb{R}$-valued $1$-form $a$ against $\hat s$.

The identification $\Phi\colon S^{2n+1}\times_{\varrho_1}\mathbb{C}\xrightarrow{\ \sim\ }\mathcal{O}(-1)$ proved in [[Ex - The Tautological Line Bundle over CP^n is Associated to the Hopf Bundle|the tautological-bundle exercise]] is
$$\Phi([z,w])=([z],wz),$$
which is well defined because $[z\lambda,\lambda^{-1}w]\mapsto([z\lambda],\lambda^{-1}w\cdot z\lambda)=([z],wz)$, and is an isomorphism of complex line bundles. Under $\Phi$ the equivariant function $\hat s$ of a section $s$ and the honest $\mathbb{C}^{n+1}$-valued section $\sigma:=\Phi\circ s$ are related by $\sigma([z])=\hat s(z)\,z$.

![[Def - Curvature of a Principal Connection#The Definition]]

The Hermitian metric $h$ on $\mathbb{C}^{n+1}$ is $h(\zeta,\eta)=\sum_{j=0}^n\zeta_j\overline{\eta_j}$, complex-linear in the first argument and conjugate-linear in the second; its real part $\langle\cdot,\cdot\rangle=\operatorname{Re}h$ is the real inner product of $\mathbb{R}^{2n+2}$. For a unit vector $z$ ($h(z,z)=|z|^2=1$) the Hermitian orthogonal projection onto the line $\mathbb{C}z$ is $\operatorname{pr}_z(\eta)=h(\eta,z)\,z$.

---

# Convergent Strategy

**Problem class.** This is a *compute-an-induced-object* problem: the abstract machine of [[Thm - Principal Connections Induce Covariant Derivatives on Associated Bundles|the induced-connection theorem]] takes the Hopf connection on the total space $S^{2n+1}$ and hands back a covariant derivative on the associated line bundle $\mathcal{O}(-1)$, and we are asked to recognise the anonymous output as a concrete, familiar operator — the orthogonal projection of the flat derivative onto a subbundle. Problems of this class are solved by *pulling both descriptions back to the total space*, where the equivariant-function dictionary turns sections into ordinary $V$-valued functions and both candidate connections become explicit $\mathbb{C}^{n+1}$-valued $1$-forms that can be compared line by line.

**Assumption pattern.** The single structural fact that does all the work is that $\mathcal{O}(-1)$ is *simultaneously* an associated bundle of $S^{2n+1}$ (so the induced connection applies) and a subbundle of a trivial bundle (so the projected connection $\operatorname{pr}\circ d$ makes sense). The recognisable trigger is the coincidence, established at the end of Recall, that the Hopf connection form is exactly the Hermitian pairing against the base point: $a_z(u)=h(u,z)$. This one identity is what lets the correction term $a\cdot\hat s$ in equation (47) be read as the tangential-projection correction $h(\,\cdot\,,z)z$ in $\operatorname{pr}(ds)$.

**Theorem routing.** The route is: express a section $s$ through its $\mathbb{C}^{n+1}$-valued avatar $\sigma=\hat s\cdot z$ on $S^{2n+1}$ (Recall); differentiate $\sigma$ by the Leibniz rule to get $d\sigma=(d\hat s)z+\hat s\,dz$; apply the Hermitian projection $\operatorname{pr}_z(\eta)=h(\eta,z)z$ and use $a_z=h(\,\cdot\,,z)$ to obtain $\operatorname{pr}_z(d\sigma)=(d\hat s+a\hat s)\,z$; recognise the bracket as the right-hand side of equation (47) via [[Thm - Principal Connections Induce Covariant Derivatives on Associated Bundles|the induced-connection theorem]]; conclude $\pi^*(\nabla s)=\pi^*(\operatorname{pr}(ds))$ and descend along the submersion $\pi$. For Hermiticity, decompose $ds_i=\nabla s_i+(ds_i)^\perp$ and use that the flat connection $d$ is metric and the perpendicular part is $h$-orthogonal to the fibre. For the curvature, invoke part (c) of the same theorem, which reduces $F_\nabla$ to $\rho_*(F_a)=F_a$, and read the $n=1$ value off [[Ex - Curvature of the Standard Hopf Connection|the Hopf-curvature exercise]].

**Key decision point.** The one genuinely non-obvious move is *lifting everything to $S^{2n+1}$*. On the base $\mathbb{CP}^n$ neither the induced connection nor the projection has a clean formula — $\mathcal{O}(-1)$ has no global frame and the projection $\operatorname{pr}_{[z]}$ depends on the line. Upstairs, the tautological subbundle acquires the tautological *tangential* description $\sigma(z)=\hat s(z)z$, the projection becomes the explicit Hermitian formula $h(\,\cdot\,,z)z$, and the connection form $a$ becomes $h(\,\cdot\,,z)$; all three collapse into a single one-line computation. Recognising that the base-level statement is best proved upstairs, and that the descent is legitimate because $\pi$ is a surjective submersion, is the whole art of the exercise.

---

# Legal Operations Used

This solution deploys the following legal operations of the chapter (named descriptively; the topic page's Legal Operations will fix their numbering):

1. **Translate a section of an associated bundle into an equivariant function on the total space.** A section $s$ of $E=P\times_\rho V$ is encoded by $\hat s\colon P\to V$ with $\hat s(pg)=\rho(g^{-1})\hat s(p)$; here $\hat s(z\lambda)=\lambda^{-1}\hat s(z)$ and $\sigma=\hat s\cdot z$ is its realisation inside $\underline{\mathbb{C}^{n+1}}$.

2. **Compute an induced covariant derivative through equation (47).** For a principal connection $a$ and representation $\rho$, the induced $\nabla$ is the unique connection with $\pi^*(\nabla s)=d\hat s+\rho_*(a)\hat s$ in the sense of the basic-equivariant-form correspondence; this is [[Thm - Principal Connections Induce Covariant Derivatives on Associated Bundles|the induced-connection theorem]], part (a).

3. **Project the ambient flat connection onto a subbundle.** For a subbundle $E\subset\underline{V}$ of a trivial bundle, $\nabla^{\mathrm{pr}}s:=\operatorname{pr}(ds)$ is a connection on $E$; the operation is legal because $\operatorname{pr}$ is $C^\infty$-linear and $d$ is a connection, so $\operatorname{pr}(d(fs))=\operatorname{pr}(df\otimes s+f\,ds)=df\otimes\operatorname{pr}(s)+f\operatorname{pr}(ds)=df\otimes s+f\nabla^{\mathrm{pr}}s$.

4. **Identify the Hopf connection form with a Hermitian pairing.** The real-inner-product formula $a_z(u)=\langle v(z),u\rangle i$ is rewritten as the Hermitian pairing $a_z(u)=h(u,z)$ (proved in Recall / Step 0), converting the equivariant-function correction term into the projection correction term.

5. **Descend an identity of pulled-back objects along a surjective submersion.** Two forms (or sections) on $\mathbb{CP}^n$ that have equal pull-backs under the submersion $\pi$ are equal, because $d\pi$ is surjective and $\pi$ is onto.

6. **Read the curvature of an induced connection off the principal curvature.** By part (c) of the induced-connection theorem, $F_{\nabla^a}=\rho_*(F_a)$; for the standard representation $\rho_*=\mathrm{id}$, so $F_\nabla$ is multiplication by $F_a$.

---

# Hints

> [!note]- Hint 1
> Both connections you must compare live on the base $\mathbb{CP}^n$, where $\mathcal{O}(-1)$ has no global frame. Do not fight this. Every object here is easier one floor up, on $S^{2n+1}$: a section $s$ of $\mathcal{O}(-1)\subset\underline{\mathbb{C}^{n+1}}$ becomes a $\mathbb{C}^{n+1}$-valued function $\sigma=s\circ\pi$, and because $\sigma(z)$ lies in the line $\mathbb{C}z$ you can write $\sigma(z)=\hat s(z)\,z$ for a scalar $\hat s(z)$. What is $\hat s$ in terms of the Hermitian metric, and what equivariance does it satisfy?

> [!note]- Hint 2
> The induced connection is *defined* by equation (47): $\pi^*(\nabla s)=d\hat s+a\cdot\hat s$, and here $a\cdot\hat s=\rho_*(a)\hat s=a\hat s$ because the standard representation has $\rho_*=\mathrm{id}$. The projected connection, pulled back, is $\operatorname{pr}_z(d\sigma)$. Differentiate $\sigma=\hat s\,z$ with the Leibniz rule, then apply $\operatorname{pr}_z(\eta)=h(\eta,z)z$. You will need one small identity connecting $a$ to $h$.

> [!note]- Hint 3
> Prove $a_z(u)=h(u,z)$. Split the Hermitian pairing into real and imaginary parts, $h(u,z)=\langle u,z\rangle+i\langle u,iz\rangle$, use $\langle u,z\rangle=0$ for $u\in T_zS^{2n+1}$, and compare with $a_z(u)=\langle iz,u\rangle i$. Once you have $a_z=h(\,\cdot\,,z)$, the projection of $d\sigma$ becomes $(d\hat s+a\hat s)z$ verbatim.

> [!note]- Hint 4
> For Hermiticity, decompose the ambient derivative $ds_i=\nabla s_i+(ds_i)^\perp$ into its tangential (line) and normal parts. The flat connection $d$ is metric because $h$ is constant, so $d\,h(s_1,s_2)=h(ds_1,s_2)+h(s_1,ds_2)$; now discard the normal parts, which are $h$-orthogonal to the sections. For the curvature, you do not compute anything new — quote part (c) of the induced-connection theorem, $F_\nabla=\rho_*(F_a)$, and for $n=1$ read $F_a$ from the Hopf-curvature exercise.

---

# Solution

The proof lifts the whole comparison to the sphere $S^{2n+1}$, where the tautological subbundle acquires the tangential description $\sigma=\hat s\cdot z$, the induced connection is given verbatim by equation (47), and the Hermitian projection has the explicit formula $h(\,\cdot\,,z)z$. The pivot is the identity $a_z(u)=h(u,z)$: it makes the correction term $a\hat s$ of the induced connection coincide with the correction produced by projecting the flat derivative. Once the two pulled-back connections agree, they descend to the same connection on $\mathbb{CP}^n$ because $\pi$ is a surjective submersion. Hermiticity and the curvature are then short corollaries.

**Step 0: The Hopf connection form is the Hermitian pairing against the base point, $a_z(u)=h(u,z)$.**

This identity is the hinge of the whole argument and must be established before the connections are compared.

> [!note]- Derivation
> **Split the Hermitian pairing into real and imaginary parts.** For $u\in\mathbb{C}^{n+1}$ and the unit vector $z$,
> $$h(u,z)=\operatorname{Re}h(u,z)+i\operatorname{Im}h(u,z)=\langle u,z\rangle+i\operatorname{Im}h(u,z)\qquad(\text{since }\langle\cdot,\cdot\rangle=\operatorname{Re}h).$$
> **Rewrite the imaginary part through the real inner product.** Because $h$ is conjugate-linear in its second slot, $h(u,iz)=\overline{i}\,h(u,z)=-i\,h(u,z)$, hence
> $$\operatorname{Im}h(u,z)=\operatorname{Re}\!\big(-i\,h(u,z)\big)=\operatorname{Re}h(u,iz)=\langle u,iz\rangle\qquad(\text{multiplying by }-i\text{ rotates }\operatorname{Im}\text{ into }\operatorname{Re}).$$
> Therefore
> $$h(u,z)=\langle u,z\rangle+i\,\langle u,iz\rangle.$$
> **Restrict to the tangent space of the sphere.** For $u\in T_zS^{2n+1}=\{u\in\mathbb{C}^{n+1}\mid\langle u,z\rangle=0\}$ the first term vanishes, so, using the symmetry of the real inner product and $v(z)=iz$,
> $$h(u,z)=i\,\langle u,iz\rangle=\langle iz,u\rangle\,i=\langle v(z),u\rangle\,i=a_z(u)\qquad(\text{definition of }a\text{ from }[[Thm - The Standard Connection on the Hopf Bundle]]).$$
> **Consistency check.** On the fundamental field $v(z)=iz$ the identity gives $a_z(v(z))=h(iz,z)=i\,h(z,z)=i$, the Lie-algebra generator, as a connection form must satisfy; and $a_z(u)=h(u,z)=0$ exactly when $u$ is Hermitian-orthogonal to $z$, which within $T_zS^{2n+1}$ is the real orthogonal complement $v^\perp$ of $iz$ — matching $\ker a=v^\perp$. Hence $a_z=h(\,\cdot\,,z)$.

**Step 1: Realise a section on the total space as $\sigma=\hat s\cdot z$, and record its equivariance.**

A section $s$ of $\mathcal{O}(-1)$ pulls back to a $\mathbb{C}^{n+1}$-valued function that is a scalar multiple of the position vector.

> [!note]- Derivation
> Let $s\colon\mathbb{CP}^n\to\mathbb{C}^{n+1}$ be a section of $\mathcal{O}(-1)$, so $s([z])\in\mathbb{C}z$ for all $z$. Set $\sigma:=s\circ\pi\colon S^{2n+1}\to\mathbb{C}^{n+1}$; then $\sigma(z)=s([z])\in\mathbb{C}z$, so there is a unique scalar $\hat s(z)\in\mathbb{C}$ with
> $$\sigma(z)=\hat s(z)\,z,\qquad\hat s(z)=h(\sigma(z),z)\qquad(\text{because }h(\hat s(z)z,z)=\hat s(z)\,h(z,z)=\hat s(z)\text{, as }|z|=1).$$
> **Check equivariance.** Since $\pi(z\lambda)=\pi(z)$ we have $\sigma(z\lambda)=s([z\lambda])=s([z])=\sigma(z)$, hence
> $$\hat s(z\lambda)=h(\sigma(z\lambda),z\lambda)=h(\sigma(z),z\lambda)=\overline{\lambda}\,h(\sigma(z),z)=\lambda^{-1}\hat s(z)\qquad(h\text{ conjugate-linear in slot two; }\overline{\lambda}=\lambda^{-1}\text{ as }|\lambda|=1).$$
> Thus $\hat s$ is the equivariant function of $s$ for the representation $\varrho_1$, matching the correspondence of [[Ex - The Tautological Line Bundle over CP^n is Associated to the Hopf Bundle|the tautological-bundle exercise]]: under $\Phi([z,w])=([z],wz)$ the section $[z]\mapsto[z,\hat s(z)]$ is carried to $[z]\mapsto([z],\hat s(z)z)=([z],\sigma(z))$.

**Step 2: The projection of the flat derivative equals the equation-(47) correction, $\operatorname{pr}_z(d\sigma)=(d\hat s+a\hat s)\,z$.**

Differentiating $\sigma=\hat s\,z$ and projecting onto the line produces exactly the right-hand side of equation (47).

> [!note]- Derivation
> **Differentiate by the Leibniz rule.** Writing $z$ for the inclusion function $S^{2n+1}\hookrightarrow\mathbb{C}^{n+1}$, whose differential is $dz(u)=u$ for $u\in T_zS^{2n+1}$,
> $$d\sigma=d(\hat s\,z)=(d\hat s)\,z+\hat s\,dz,\qquad\text{so}\qquad d\sigma(u)=\big(d\hat s(u)\big)z+\hat s(z)\,u\qquad(\text{Leibniz rule for the }\mathbb{C}\text{-valued }\hat s\text{ times the }\mathbb{C}^{n+1}\text{-valued }z).$$
> **Apply the Hermitian projection** $\operatorname{pr}_z(\eta)=h(\eta,z)z$, using bilinearity of $h$ in the first slot:
> $$\operatorname{pr}_z\big(d\sigma(u)\big)=h\!\big((d\hat s(u))z+\hat s(z)u,\ z\big)\,z=\Big(d\hat s(u)\,h(z,z)+\hat s(z)\,h(u,z)\Big)z\qquad(\text{linearity of }h\text{ in argument one}).$$
> **Insert the two evaluations** $h(z,z)=1$ and $h(u,z)=a_z(u)$ (Step 0):
> $$\operatorname{pr}_z\big(d\sigma(u)\big)=\big(d\hat s(u)+\hat s(z)\,a_z(u)\big)\,z=\big((d\hat s+a\hat s)(u)\big)\,z.$$
> The scalar $1$-form $d\hat s+a\hat s$ is exactly $d\hat s+\rho_*(a)\hat s$ because $\rho_*=\mathrm{id}$ for the standard representation (Recall). Thus
> $$\operatorname{pr}_z(d\sigma)=(d\hat s+a\hat s)\,z.$$

**Step 3: Both connections have the same pull-back, so they are equal.**

The equation-(47) characterisation identifies the left side of Step 2's conclusion with the induced connection and the right side with the projected connection; a submersion descent finishes.

> [!note]- Derivation
> **The induced connection.** By [[Thm - Principal Connections Induce Covariant Derivatives on Associated Bundles|the induced-connection theorem]], part (a), the induced connection $\nabla=\nabla^a$ is the unique connection on $\mathcal{O}(-1)=S^{2n+1}\times_{\varrho_1}\mathbb{C}$ satisfying
> $$\pi^*(\nabla s)\ \longleftrightarrow\ d\hat s+\rho_*(a)\hat s=d\hat s+a\hat s$$
> under the basic-equivariant-form correspondence. Concretely, transporting through $\Phi$ (Step 1), the $\mathbb{C}^{n+1}$-valued $1$-form on $S^{2n+1}$ representing $\pi^*(\nabla s)$ is $(d\hat s+a\hat s)\,z$.
>
> **The projected connection.** Let $\nabla^{\mathrm{pr}}s:=\operatorname{pr}(ds)$. Since $\operatorname{pr}$ is a fibrewise ($C^\infty$-linear) bundle map and $\pi^*(ds)=d(s\circ\pi)=d\sigma$ (naturality of $d$ under pull-back, i.e. the chain rule), and since the fibre of $\mathcal{O}(-1)$ over $[z]$ pulled back to $z$ is again the line $\mathbb{C}z$ on which $\operatorname{pr}_z$ acts,
> $$\pi^*(\nabla^{\mathrm{pr}}s)=\operatorname{pr}\big(\pi^*(ds)\big)=\operatorname{pr}_z(d\sigma)=(d\hat s+a\hat s)\,z\qquad(\text{Step 2}).$$
>
> **Compare and descend.** The two $\mathbb{C}^{n+1}$-valued $1$-forms $\pi^*(\nabla s)$ and $\pi^*(\nabla^{\mathrm{pr}}s)$ on $S^{2n+1}$ coincide, both equal to $(d\hat s+a\hat s)z$. Because $\pi\colon S^{2n+1}\to\mathbb{CP}^n$ is a surjective submersion, its differential $d\pi_z$ is surjective at every $z$ and $\pi$ is onto; hence a section-valued $1$-form on $\mathbb{CP}^n$ is determined by its pull-back, and
> $$\nabla s=\nabla^{\mathrm{pr}}s=\operatorname{pr}(ds)\qquad\text{for every section }s.$$
> This proves part 1: the induced connection is the projected connection $\nabla s=\operatorname{pr}(ds)$.

**Step 4: The projected connection is Hermitian.**

Metric compatibility follows because the ambient flat connection is metric and the discarded normal component is orthogonal to the fibre.

> [!note]- Derivation
> Let $s_1,s_2$ be sections of $\mathcal{O}(-1)$, viewed as $\mathbb{C}^{n+1}$-valued functions with values in the tautological lines, and let $h(s_1,s_2)$ denote the induced Hermitian metric, the restriction of the ambient $h$.
>
> **The flat connection is metric.** With $h(s_1,s_2)=\sum_j (s_1)_j\overline{(s_2)_j}$ a sum of products of scalar functions, the ordinary product rule gives
> $$d\,h(s_1,s_2)=\sum_j\Big(d(s_1)_j\,\overline{(s_2)_j}+(s_1)_j\,\overline{d(s_2)_j}\Big)=h(ds_1,s_2)+h(s_1,ds_2)\qquad(\text{Leibniz rule componentwise; }h\text{ constant}).$$
> **Split the ambient derivative into tangential and normal parts.** Writing $ds_i=\operatorname{pr}(ds_i)+(ds_i)^\perp=\nabla s_i+(ds_i)^\perp$, where $(ds_i)^\perp$ takes values in the Hermitian complement $(\mathbb{C}z)^\perp$ of the fibre, we have
> $$h\big((ds_1)^\perp,s_2\big)=0,\qquad h\big(s_1,(ds_2)^\perp\big)=0\qquad(\text{since }(ds_i)^\perp\perp\mathbb{C}z\ \text{and}\ s_1,s_2\in\mathbb{C}z).$$
> **Combine.** Substituting $ds_i=\nabla s_i+(ds_i)^\perp$ into the metric identity and dropping the two vanishing terms,
> $$d\,h(s_1,s_2)=h(\nabla s_1,s_2)+h(s_1,\nabla s_2).$$
> Thus $\nabla$ is compatible with $h$: the induced connection is Hermitian, proving part 2. (Structurally this is the invariant reason: the standard representation $\varrho_1$ is unitary, so a $U(1)$-connection induces a metric connection; the computation above is that statement made concrete.)

**Step 5: The curvature is multiplication by the Hopf curvature.**

Part (c) of the induced-connection theorem reduces the curvature computation to reading off $F_a$.

> [!note]- Derivation
> By [[Thm - Principal Connections Induce Covariant Derivatives on Associated Bundles|the induced-connection theorem]], part (c), the curvature of the induced connection is
> $$F_{\nabla^a}=\rho_*(F_a)\in\Omega^2\big(\mathbb{CP}^n;\operatorname{End}\mathcal{O}(-1)\big),$$
> where $F_a\in\Omega^2(\mathbb{CP}^n;i\mathbb{R})$ is the curvature of the Hopf connection (the adjoint bundle $\operatorname{ad}P$ is the trivial bundle $\mathbb{CP}^n\times i\mathbb{R}$ because $U(1)$ is abelian). Since $\rho_*=\mathrm{id}$ on $\mathbb{C}=\operatorname{End}(\mathbb{C})$, the endomorphism $\rho_*(F_a)$ is *multiplication by the scalar $2$-form $F_a$*:
> $$F_\nabla=F_a\cdot\qquad\text{(pointwise multiplication of the line by }F_a).$$
> **The case $n=1$.** From [[Ex - Curvature of the Standard Hopf Connection|the Hopf-curvature exercise]], $\pi^*F_a=da=2(dx_0\wedge dx_1+dx_2\wedge dx_3)\,i$ on $S^3$, and $F_a=2\,\mathrm{vol}_{S^2_{1/2}}\,i$ with
> $$\int_{\mathbb{CP}^1}F_a=2\,\operatorname{Vol}(S^2_{1/2})\,i=2\pi i.$$
> Hence the curvature of $\mathcal{O}(-1)\to\mathbb{CP}^1$ is $F_\nabla=2\,\mathrm{vol}_{S^2_{1/2}}\,i$, and $\tfrac{i}{2\pi}\int_{\mathbb{CP}^1}F_\nabla=\tfrac{i}{2\pi}\cdot 2\pi i=-1$; this integer is the first Chern number of the tautological bundle, computed under the Chern normalisation in **chapter VI** (see **Thm - First Chern Class of a Line Bundle from Curvature**), consistent with the orientation ledger's value $\int_{\mathbb{CP}^1}c_1(\mathcal{O}(-1))=-1$.

> [!note]- Complete formal solution
> **Claim.** The connection induced on $\mathcal{O}(-1)=S^{2n+1}\times_{\varrho_1}\mathbb{C}$ by the Hopf connection $a$ is the projected connection $\nabla s=\operatorname{pr}(ds)$; it is Hermitian, and its curvature is multiplication by the Hopf curvature $F_a$.
>
> *Preliminary identity.* For $u\in T_zS^{2n+1}$ and the standard Hermitian metric $h$ on $\mathbb{C}^{n+1}$, split $h(u,z)=\langle u,z\rangle+i\langle u,iz\rangle$ with $\langle\cdot,\cdot\rangle=\operatorname{Re}h$; since $\langle u,z\rangle=0$ on the sphere and $v(z)=iz$, $h(u,z)=\langle iz,u\rangle i=a_z(u)$. So $a_z=h(\,\cdot\,,z)$.
>
> *Projected form.* A section $s$ of $\mathcal{O}(-1)\subset\underline{\mathbb{C}^{n+1}}$ pulls back to $\sigma=s\circ\pi$ with $\sigma(z)=\hat s(z)z$, $\hat s(z)=h(\sigma(z),z)$, and $\hat s(z\lambda)=\lambda^{-1}\hat s(z)$; thus $\hat s$ is the $\varrho_1$-equivariant function of $s$. Differentiating, $d\sigma(u)=(d\hat s(u))z+\hat s(z)u$, and projecting,
> $$\operatorname{pr}_z(d\sigma(u))=h\big((d\hat s(u))z+\hat s(z)u,z\big)z=\big(d\hat s(u)+\hat s(z)a_z(u)\big)z=\big((d\hat s+a\hat s)(u)\big)z.$$
> By the induced-connection theorem, part (a), $\pi^*(\nabla s)$ is represented by $(d\hat s+\rho_*(a)\hat s)z=(d\hat s+a\hat s)z$ (using $\rho_*=\mathrm{id}$); and $\pi^*(\operatorname{pr}(ds))=\operatorname{pr}(d\sigma)=(d\hat s+a\hat s)z$. The two pull-backs agree, and $\pi$ is a surjective submersion, so $\nabla s=\operatorname{pr}(ds)$.
>
> *Hermitian.* For sections $s_1,s_2$, the constant metric gives $d\,h(s_1,s_2)=h(ds_1,s_2)+h(s_1,ds_2)$; writing $ds_i=\nabla s_i+(ds_i)^\perp$ with $(ds_i)^\perp\perp\mathbb{C}z$ kills the normal terms, leaving $d\,h(s_1,s_2)=h(\nabla s_1,s_2)+h(s_1,\nabla s_2)$.
>
> *Curvature.* By the induced-connection theorem, part (c), $F_\nabla=\rho_*(F_a)$; since $\rho_*=\mathrm{id}$, $F_\nabla$ is multiplication by $F_a\in\Omega^2(\mathbb{CP}^n;i\mathbb{R})$. For $n=1$, $F_a=2\,\mathrm{vol}_{S^2_{1/2}}i$ and $\int_{\mathbb{CP}^1}F_a=2\pi i$. $\blacksquare$

> [!warning] Illegal but tempting: projecting in the wrong metric
> It is tempting to define $\operatorname{pr}$ as some *real* orthogonal projection $\mathbb{R}^{2n+2}\to\mathbb{R}\cdot z\oplus\mathbb{R}\cdot iz$ onto the real $2$-plane spanned by $z$ and $iz$. That real projection is not the Hermitian projection onto the complex line $\mathbb{C}z$ unless one is careful: the two agree here only because $\mathbb{C}z=\mathbb{R}z\oplus\mathbb{R}(iz)$ *as a real subspace* and $\operatorname{pr}_z(\eta)=h(\eta,z)z$ already accounts for both real components through the complex scalar $h(\eta,z)$. If one instead projected onto $\mathbb{R}z$ alone (forgetting the $iz$ direction), the result would not be $\mathbb{C}$-linear and would fail to define a connection on the *complex* line bundle. The correct projection is the Hermitian one, $\operatorname{pr}_z(\eta)=h(\eta,z)z$, which is what makes $a_z(u)=h(u,z)$ do its job.

---

# Key Takeaways

**The induced connection on a subbundle of a trivial bundle is the tangential part of the flat derivative, and the principal-bundle machinery is one way of proving it.** The single reusable principle is that when a vector bundle $E$ sits inside a trivial bundle $\underline{V}$ with its constant connection $d$, the formula $\nabla^E s=\operatorname{pr}(ds)$ — differentiate ambiently, then project back into the fibre — always defines a connection on $E$, and it is metric whenever $\operatorname{pr}$ is orthogonal for a parallel ambient metric. This is the *second fundamental form* picture of a subbundle connection, and it is the fastest description to compute with because it needs no local frame. The exercise shows that for $\mathcal{O}(-1)$ this concrete projection coincides with the abstract connection produced by the Hopf principal connection through equation (47). The trigger for reaching for it: you are handed a subbundle of something trivial (or flat) and asked for *the* natural connection — the projected connection is almost always the intended answer, and it is Hermitian for free when the ambient metric restricts to the fibre.

**Lift to the total space when the base has no frame; the equivariant-function dictionary turns sections into ordinary vector-valued functions.** The transferable diagnostic is that a nontrivial associated bundle — one like $\mathcal{O}(-1)$ with no global section, hence no global frame — is almost never the right place to compute a connection. Upstairs on the principal bundle $P$, sections become equivariant functions $\hat s\colon P\to V$, covariant derivatives become the explicit corrected differential $d\hat s+\rho_*(a)\hat s$ of equation (47), and everything is a formula in genuine functions. The descent back to the base is legitimate precisely because the projection $\pi$ is a surjective submersion, so an identity of pull-backs is an identity on the base. Whenever a bundle computation stalls for want of a frame, the reflex should be: pass to the total space, compute with equivariant functions, descend. This same dictionary is what makes the [[Thm - Bianchi Identity for a Principal Connection|Bianchi identity]] and the curvature formula $F_\nabla=\rho_*(F_a)$ transparent.

**A unitary representation induces a metric connection, and an abelian structure group makes the curvature a scalar form.** Two structural inheritances are worth extracting for spaced recall. First, the representation controls the induced connection's compatibilities: because $\varrho_1$ is unitary, the induced $\nabla$ preserves the Hermitian metric — no computation is needed once one recognises the representation is unitary, though the exercise also gives the hands-on proof via the normal/tangential split. Second, because $U(1)$ is abelian, the adjoint bundle $\operatorname{ad}P$ is trivial and the curvature $F_a$ is an honest scalar (here $i\mathbb{R}$-valued) $2$-form on the base rather than a bundle-valued one; the induced curvature $F_\nabla=\rho_*(F_a)$ is then simply multiplication by $F_a$. The $n=1$ evaluation $\tfrac{i}{2\pi}\int_{\mathbb{CP}^1}F_\nabla=-1$ is the first sighting of a characteristic number in the series: the curvature of the tautological bundle integrates to the first Chern number $-1$, the calculation completed in chapter VI. Companion exercises: [[Ex - Curvature of the Standard Hopf Connection]] supplies the value of $F_a$ used here, and [[Ex - Pull-Back of the Hopf Connection along the Inclusion of CP^1 into CP^n]] shows this whole picture restricts consistently along $\mathbb{CP}^1\hookrightarrow\mathbb{CP}^n$.
