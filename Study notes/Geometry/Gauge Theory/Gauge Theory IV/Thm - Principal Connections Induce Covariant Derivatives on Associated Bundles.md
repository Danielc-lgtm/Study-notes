---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Connection on a Principal Bundle"
  - "Def - Associated Bundle"
  - "Thm - Sections of an Associated Bundle are Equivariant Functions"
  - "Thm - Bundle-Valued Forms on the Base are Basic Equivariant Forms on the Total Space"
  - "Def - Representation of a Lie Algebra"
  - "Def - Connection on a Vector Bundle"
  - "Def - Curvature of a Vector-Bundle Connection"
  - "Def - Curvature of a Principal Connection"
  - "Thm - Structure Equation for the Curvature"
  - "Def - Induced Connections on Dual, Hom, and Endomorphism Bundles"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $\pi\colon P\to M$ is a principal $G$-bundle over a smooth manifold $M$, with $G$ a Lie group acting on the **right**, $R_g(p)=p\cdot g$; the **fundamental vector field** of $\xi\in\mathfrak g=T_eG$ is $\xi_P(p)=\frac{d}{dt}\big|_{t=0}\,p\cdot\exp(t\xi)$, a vertical vector field spanning the vertical subspace $V_p=\ker d\pi_p$ as $\xi$ ranges over $\mathfrak g$. A **[[Def - Connection on a Principal Bundle|connection]]** on $P$ is a form $\omega\in\Omega^1(P;\mathfrak g)$ satisfying the two axioms
$$\text{(C1)}\quad R_g^*\omega=\operatorname{Ad}_{g^{-1}}\omega,\qquad\text{(C2)}\quad \omega(\xi_P)=\xi\ \text{ for all }\xi\in\mathfrak g,$$
where $\operatorname{Ad}_g=d_e(h\mapsto ghg^{-1})$ is the adjoint representation of $G$ on $\mathfrak g$. Its horizontal distribution is $H=\ker\omega$, with horizontal projection $\pi_H\colon TP\to H$; its **[[Def - Curvature of a Principal Connection|curvature]]** is the horizontal, $\operatorname{Ad}$-equivariant form $\Omega\in\Omega^2(P;\mathfrak g)$, which descends to $F_\omega\in\Omega^2(M;\operatorname{ad}P)$ with $\pi^*F_\omega=\Omega$; locally, for a section $\sigma$ of $P$ over $U\subseteq M$, the **gauge potential** is $A:=\sigma^*\omega\in\Omega^1(U;\mathfrak g)$ (written $A_\sigma$ on [[Def - Local Connection Form and Gauge Potential]]) and the local curvature is $F_\sigma:=\sigma^*\Omega=dA+\tfrac12[A\wedge A]$.

Let $\rho\colon G\to GL(V)$ be a **[[Def - Representation of a Lie Group|representation]]** of $G$ on a finite-dimensional real or complex vector space $V$, and let
$$\rho_*:=d_e\rho\colon\mathfrak g\longrightarrow\operatorname{End}(V)$$
be its differential, a **[[Def - Representation of a Lie Algebra|Lie algebra representation]]**: $\rho_*[\xi,\eta]=[\rho_*\xi,\rho_*\eta]=\rho_*\xi\,\rho_*\eta-\rho_*\eta\,\rho_*\xi$. The **[[Def - Associated Bundle|associated bundle]]** is $E=P\times_\rho V:=(P\times V)/G$, where $G$ acts by $(p,v)\cdot g=(p\cdot g,\rho(g^{-1})v)$; the class of $(p,v)$ is written $[p,v]$, so
$$[p\cdot g,\rho(g^{-1})v]=[p,v]\qquad\text{for all }g\in G,$$
and $[p,\cdot]\colon V\to E_{\pi(p)}$ is a linear isomorphism onto the fibre over $\pi(p)$.

We use two correspondences from chapter III, both restated at the point of use below:

- **[[Thm - Sections of an Associated Bundle are Equivariant Functions|Equivariant functions]].** Sections of $E$ correspond bijectively to $G$-equivariant maps $\hat s\colon P\to V$, meaning $\hat s(p\cdot g)=\rho(g^{-1})\hat s(p)$; the correspondence is $s(\pi(p))=[p,\hat s(p)]$. We call $\hat s$ the **equivariant lift** of $s$ and write $C^\infty(P;V)^G$ for the space of such maps.
- **[[Thm - Bundle-Valued Forms on the Base are Basic Equivariant Forms on the Total Space|Basic equivariant forms]].** For each $q\ge0$, bundle-valued forms $\alpha\in\Omega^q(M;E)$ correspond bijectively to $V$-valued forms $\hat\alpha\in\Omega^q(P;V)$ that are **horizontal** ($\hat\alpha$ vanishes whenever one argument is vertical) and **equivariant** ($R_g^*\hat\alpha=\rho(g^{-1})\hat\alpha$); the correspondence is $\alpha(d\pi\,\hat v_1,\dots,d\pi\,\hat v_q)=[p,\hat\alpha_p(\hat v_1,\dots,\hat v_q)]$. We call a horizontal equivariant form **basic of type $\rho$**.

For a $\mathfrak g$-valued form and the representation $\rho$, the symbol $\rho_*(\omega)\hat s$ denotes the $V$-valued form $X\mapsto\rho_*(\omega(X))\,\hat s$ (Haydys writes this $a\cdot\hat s$). All connections on a vector bundle are **[[Def - Connection on a Vector Bundle|covariant derivatives]]** $\nabla\colon\Gamma(E)\to\Omega^1(M;E)$ with $\nabla(fs)=df\otimes s+f\nabla s$; in a local frame $e$ the connection matrix is $A(\nabla,e)\in\Omega^1(U;\mathfrak{gl}_k)$ with $\nabla=d+A(\nabla,e)$, and the curvature is $F_\nabla=dA(\nabla,e)+A(\nabla,e)\wedge A(\nabla,e)\in\Omega^2(M;\operatorname{End}E)$.

> [!warning] Convention: sources
> Haydys (source A) writes $a$ for a principal connection and, crucially, writes "$G$-invariant" throughout where the correct condition is "$G$-equivariant" (axiom (C1) and the basic-forms correspondence). Bär (source B) writes $\varrho\colon G\to\operatorname{Aut}(V)$ for the representation and $\omega$ for the connection. Bär's verification of representative-independence in Remark 2.3.9 (item B-T2.3.10) is stated as "a simple computation shows" and the displayed line breaks off at the foot of the page; the full computation is supplied in Step 2 below. The series writes $\omega$ for the connection, $\rho$ for the representation, $\rho_*$ for its differential, $F_\omega\in\Omega^2(M;\operatorname{ad}P)$ and $F_\sigma$ locally. The bracket of $\mathfrak g$-valued forms is normalised so that $[A\wedge A](X,Y)=2[A(X),A(Y)]$, hence $\tfrac12[A\wedge A](X,Y)=[A(X),A(Y)]$; for matrix groups $\tfrac12[A\wedge A]=A\wedge A$.

---

# Statement

> **Theorem (induced covariant derivative on an associated bundle).** Let $\pi\colon P\to M$ be a principal $G$-bundle, $\omega$ a connection on $P$, and $\rho\colon G\to GL(V)$ a representation with differential $\rho_*\colon\mathfrak g\to\operatorname{End}(V)$. Write $E=P\times_\rho V$ for the associated vector bundle.
>
> **(a) Existence and uniqueness.** There is a unique connection $\nabla=\nabla^\omega$ on $E$ such that, for every section $s\in\Gamma(E)$ with equivariant lift $\hat s\in C^\infty(P;V)^G$, the $E$-valued $1$-form $\nabla s$ corresponds under the basic-forms correspondence to the $V$-valued $1$-form
> $$\pi^*(\nabla s)\ \longleftrightarrow\ d\hat s+\rho_*(\omega)\hat s\in\Omega^1(P;V).$$
>
> **(b) Local formula.** For a local section $\sigma\colon U\to P$ with gauge potential $A=\sigma^*\omega$, and any smooth $v\colon U\to V$,
> $$\nabla_X[\sigma,v]=\big[\sigma,\ \partial_Xv+\rho_*\!\big(A(X)\big)v\big],\qquad X\in T_uU,$$
> and the right-hand side is independent of the representative: replacing $(\sigma,v)$ by $(\sigma g,\rho(g^{-1})v)$ for any $g\colon U\to G$ gives the same element of $E$. Equivalently, in the local frame of $E$ furnished by $\sigma$, the connection matrix of $\nabla^\omega$ is $\rho_*(A)\in\Omega^1(U;\operatorname{End}V)$: locally $\nabla^\omega=d+\rho_*(A)$.
>
> **(c) Curvature.** The curvature of $\nabla^\omega$ is
> $$F_{\nabla^\omega}=\rho_*(F_\omega)\in\Omega^2(M;\operatorname{End}E),$$
> where $\rho_*\colon\operatorname{ad}P\to\operatorname{End}E$ is the fibrewise map $[p,\xi]\mapsto[p,\rho_*(\xi)]$; equivalently $\pi^*F_{\nabla^\omega}$ corresponds to $\rho_*(\Omega)$, and locally $F_{\nabla^\omega}=\rho_*(F_\sigma)$.
>
> **(d) Compatibility with the frame-bundle construction.** If $E$ is a vector bundle of rank $k$, $P=\operatorname{Fr}(E)$ its frame bundle, $G=GL_k(\mathbb R)$ and $\rho$ the standard representation on $V=\mathbb R^k$, then $\nabla^\omega$ has connection matrix $e^*\omega$ in every local frame $e$; consequently $\nabla\mapsto\omega$ (of [[Thm - A Covariant Derivative Determines a Connection on the Frame Bundle|the previous theorem]]) and $\omega\mapsto\nabla^\omega$ are mutually inverse bijections between connections on $E$ and connections on $\operatorname{Fr}(E)$. Moreover the connections induced on $E^*$, $\operatorname{End}E$ and $\Lambda^pE$ through the dual, conjugation, and $p$-th exterior representations coincide with the direct constructions of chapter II.
>
> **(e) The adjoint bundle.** For $\rho=\operatorname{Ad}$ on $V=\mathfrak g$, the associated bundle is $\operatorname{ad}P$ and $\nabla^\omega$ is the connection $\nabla_a$ appearing in the Bianchi identity: locally $\nabla^\omega=d+[A\wedge\,\cdot\,]$, and $F_{\nabla^\omega}=[F_\omega,\,\cdot\,]$.

---

# Motivation

Two notions of connection have been developed in parallel. Chapter II defined a connection on a vector bundle as a covariant derivative, a rule $\nabla$ for differentiating sections that obeys the Leibniz rule; chapter IV defined a connection on a principal bundle as a $\mathfrak g$-valued one-form $\omega$, or equivalently an invariant horizontal distribution. Haydys puts the reader's question directly: "the definitions of a connection on a vector and principal bundle differ significantly and the reader may wonder what is the relation between these two notions." This theorem, together with the frame-bundle theorem preceding it, is the answer. It says the two notions are the same object seen from two sides, and it does so constructively: a principal connection $\omega$ on $P$, together with a choice of representation $\rho$, manufactures an honest covariant derivative $\nabla^\omega$ on every associated vector bundle $E=P\times_\rho V$ at once.

The importance of "at once" is the whole point of the principal-bundle formalism. A single connection $\omega$ on $P$ differentiates sections not only of one bundle but of the entire family of bundles associated to $P$ — the defining bundle $E$, its dual $E^*$, the endomorphism bundle $\operatorname{End}E$, every exterior and tensor power, and the adjoint bundle $\operatorname{ad}P$ in which the curvature itself lives — and it does so compatibly, so that the pairings and products relating these bundles are all parallel. To differentiate a section of $E$ one does not need a separate rule for $E$; one differentiates the underlying scalar data (the equivariant lift $\hat s$) and corrects the answer with $\omega$ so that it becomes tensorial. That is exactly the content of formula (a).

The construction is not an ornament: it is where the two central examples of the whole theory come from. The Levi-Civita connection is the induced connection on $TM=\operatorname{Fr}(TM)\times_\rho\mathbb R^n$ obtained from a principal connection on the orthonormal frame bundle for the standard $O(n)$-representation; spinor fields are sections of a bundle associated to a spin structure through the spin representation, and the spin connection is $\nabla^\omega$ for that representation; and the coupling of a gauge field to matter in Yang–Mills theory is precisely the statement that a matter field is a section of an associated bundle and its covariant derivative is $\nabla^\omega$. Part (c), that the curvature of the induced connection is $\rho_*$ of the principal curvature, is the mechanism by which a single field strength $F_\omega$ governs the curvature felt by matter in every representation. The reader should keep in view that the corrected derivative $d\hat s+\rho_*(\omega)\hat s$ is the same formula, evaluated in different representations, that produces all of these.

We assume the reader is comfortable with principal connections and their curvature (chapter IV), with the two correspondences of chapter III (sections as equivariant functions, bundle-valued forms as basic equivariant forms), and with covariant derivatives on vector bundles and their local connection matrices (chapter II).

---

# Sources and Targets

**Sources (Input Broadening)**

The literal hypotheses are mild — a principal connection and a representation — so the useful question is which problems secretly present those two ingredients.

The first disguised source is **a geometric structure on a vector bundle expressed as a reduction of its frame bundle**. A Riemannian metric on $E$ is the same datum as a reduction of $\operatorname{Fr}(E)$ to the orthogonal frame bundle $\operatorname{Fr}_O(E)$, a principal $O(k)$-bundle; a complex structure and Hermitian metric reduce to $\operatorname{Fr}_U(E)$, a principal $U(k)$-bundle; an orientation reduces to $GL^+$. A connection on the reduced bundle is a principal $O(k)$- or $U(k)$-connection, and the theorem induces from it a metric-compatible covariant derivative on $E$ through the defining representation. The bridge $B\Rightarrow A$ is: "a metric-compatible connection on $E$" is not obviously "a principal connection plus a representation," but the reduction turns it into exactly that, and metric compatibility becomes the statement that $\omega$ takes values in the subalgebra $\mathfrak{o}(k)$ or $\mathfrak u(k)$. *Example problem:* recover the Levi-Civita connection as the induced connection of the unique torsion-free connection on the orthonormal frame bundle of $(M,g)$.

The second disguised source is **a physical matter field carrying a representation of a gauge group**. In Yang–Mills theory one is handed a gauge field, which is a connection $\omega$ on a principal $G$-bundle, and a matter field valued in a representation $\rho$ of $G$ — a section of $P\times_\rho V$. The covariant derivative $D_\mu=\partial_\mu+\rho_*(A_\mu)$ that appears in every gauge-theory Lagrangian is $\nabla^\omega$ written in a local gauge, by part (b). The bridge is the recognition that "$\partial_\mu$ replaced by $\partial_\mu+A_\mu$ acting in a representation" is not an ad hoc minimal-coupling prescription but the local form of a canonical geometric object. *Example problem:* show that the Dirac operator coupled to a $U(1)$ gauge field is built from $\nabla^\omega$ for the charge-$q$ representation $\rho_q(\lambda)=\lambda^q$, so that $\rho_{q*}(A)=qA$ reproduces the electric charge.

The third disguised source is **the adjoint bundle and the curvature itself**. The curvature $F_\omega$ is a two-form valued in $\operatorname{ad}P=P\times_{\operatorname{Ad}}\mathfrak g$, an associated bundle for the adjoint representation. Any statement about differentiating $F_\omega$ — the Bianchi identity, the second-order Yang–Mills equation — is a statement about the induced connection $\nabla^\omega$ on $\operatorname{ad}P$, delivered by part (e). The bridge is that "differentiate the curvature covariantly" is the induced connection for $\rho=\operatorname{Ad}$, so the exterior covariant derivative $d^{\nabla^\omega}$ on $\operatorname{ad}P$-valued forms is available with no extra construction. *Example problem:* derive the local Bianchi identity $dF_\sigma+[A\wedge F_\sigma]=0$ from $d^{\nabla^\omega}F_\omega=0$ using the local form of $\nabla^\omega$ on $\operatorname{ad}P$ given in part (e).

**Targets (Output Amplification)**

Combine the theorem with **the frame-bundle theorem** to obtain the equivalence of the two notions of connection. The previous theorem sends a covariant derivative $\nabla$ on $E$ to a principal connection $\omega$ on $\operatorname{Fr}(E)$; part (d) here sends $\omega$ back to $\nabla^\omega$ and shows $\nabla^\omega=\nabla$. The payoff is that every theorem proved for principal connections (existence, the affine structure of the space of connections, gauge transformations, holonomy, Chern–Weil theory) transfers verbatim to vector-bundle connections, and vice versa; the extra ingredient is only the identification of representations.

Combine the theorem with **an invariant multilinear operation on representations** to obtain a Leibniz rule on the associated bundles. Part (d) is proved through a compatibility lemma: any $G$-equivariant multilinear map $V_1\times\dots\times V_r\to W$ intertwines the induced connections. Feeding in the evaluation pairing, composition, or wedge gives the product rules for $\nabla^\omega$ on $E^*$, $\operatorname{End}E$, and $\Lambda^pE$. The payoff is that all natural constructions on $E$ automatically carry parallel-compatible connections — this is what makes $d^{\nabla}$ well behaved on bundle-valued forms and underlies the entire calculus of Chern–Weil theory.

Combine the theorem with **the structure equation and the Lie-algebra homomorphism property of $\rho_*$** to obtain part (c), the transfer of curvature. Because $\rho_*[\xi,\eta]=[\rho_*\xi,\rho_*\eta]$, applying $\rho_*$ to the local curvature $dA+\tfrac12[A\wedge A]$ turns the Lie bracket of $\mathfrak g$ into the commutator of endomorphisms, which is exactly the quadratic term of a vector-bundle curvature. The payoff is that one field strength $F_\omega$ determines the curvature in every representation, which is why characteristic classes are computed once on $P$ and read off in every associated bundle.

---

# Why Is It True

Forget the formalism for a moment and ask what it should mean to differentiate a section $s$ of an associated bundle. A section is the same as an equivariant function $\hat s\colon P\to V$: at every point $p$ of the total space it records a vector $\hat s(p)\in V$, and moving along the fibre by $g$ rotates that vector by $\rho(g^{-1})$. The naive thing to do is to differentiate $\hat s$ as an ordinary $V$-valued function, forming $d\hat s$. This fails for a definite reason: $d\hat s$ is not horizontal. If we move in a purely vertical direction — along the fibre, changing $p$ but not its image in $M$ — then $\hat s$ still changes, because equivariance forces it to rotate, and $d\hat s$ picks up that spurious vertical rate of change. A genuine derivative of $s$ on $M$ must not see fibre motion at all.

The fix is to subtract off exactly the vertical rate of change. On a fundamental vector field $\xi_P$, equivariance gives $\hat s(p\exp t\xi)=\rho(\exp(-t\xi))\hat s(p)$, so $d\hat s(\xi_P)=-\rho_*(\xi)\hat s$; the connection form reports the vertical direction as $\omega(\xi_P)=\xi$, so the correction term $\rho_*(\omega)\hat s$ evaluates on $\xi_P$ to $+\rho_*(\xi)\hat s$. The two cancel. The corrected object $d\hat s+\rho_*(\omega)\hat s$ therefore vanishes on vertical vectors — it is horizontal — while still equalling $d\hat s$ on horizontal vectors, where nothing needed fixing. Horizontality plus the equivariance that the correction preserves is precisely what the basic-forms correspondence needs to hand the result back down to $M$ as a form valued in $E$. That descended form is $\nabla s$.

> **Mechanism summary.** The covariant derivative of a section is the ordinary derivative of its equivariant lift, corrected by the connection form so as to become horizontal; the connection contributes exactly the vertical rate of change that equivariance forces on the lift, and subtracting it leaves a derivative that lives on the base.

Two consequences follow with no further ideas. Locally the correction is $\rho_*(A)$ where $A=\sigma^*\omega$ is the gauge potential, so $\nabla^\omega=d+\rho_*(A)$: the same "$\partial+A$" that physicists call minimal coupling. And the curvature, which is $\nabla^\omega$ applied twice, is $\rho_*$ of the principal curvature, because applying the correction twice produces the commutator $[\rho_*A,\rho_*A]$, and $\rho_*$ turns the Lie bracket in $F_\omega=dA+\tfrac12[A\wedge A]$ into exactly that commutator.

---

# What Makes This Hard

The subtle points are three, and all concern well-posedness rather than the computation. First, the correction term must be verified to make the derivative *horizontal* — this is where the connection axiom $\omega(\xi_P)=\xi$ and the equivariance of $\hat s$ are both used, and it is easy to check horizontality while forgetting that the result must also remain equivariant, which requires axiom (C1) together with the naturality identity $\rho_*(\operatorname{Ad}_{g^{-1}}\xi)=\rho(g^{-1})\rho_*(\xi)\rho(g)$. Second, the local formula in part (b) is written using a choice of gauge $\sigma$, so it is not a definition until one proves it is independent of $\sigma$; the change-of-gauge computation is where Bär's exposition breaks off, and the cancellation that saves it turns on the Maurer–Cartan term $g^*\theta$ in the transformation law meeting exactly the term produced by differentiating $\rho(g^{-1})v$. Third, part (d) asserts that two constructions of connections on $E^*$, $\operatorname{End}E$ and $\Lambda^pE$ — the one through representations and the one by direct Leibniz rules — coincide; the clean way to see this is not to compare local matrices case by case but to prove once that induced connections are natural with respect to equivariant multilinear maps, and read off all three product rules from that single lemma.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Define $\nabla^\omega$ on lifts by $\hat s\mapsto d\hat s+\rho_*(\omega)\hat s$; prove this output is horizontal and equivariant so it descends to a form on $M$, and check the Leibniz rule to see the descended operator is a connection; then pull the global formula back along a local gauge to get $d+\rho_*(A)$, verify gauge-independence, read off the curvature from the vector-bundle curvature formula and the structure equation, and finally specialise to the frame bundle and the adjoint representation.

**Subgoal decomposition:**

1. **Naturality of $\rho_*$.** Prove $\rho_*(\operatorname{Ad}_g\xi)=\rho(g)\rho_*(\xi)\rho(g)^{-1}$ and the Lie-algebra homomorphism property $\rho_*[\xi,\eta]=[\rho_*\xi,\rho_*\eta]$.
   - *Hint:* Differentiate $\rho(g\exp(t\xi)g^{-1})=\rho(g)\rho(\exp t\xi)\rho(g)^{-1}$ in $t$; then differentiate the first identity in $g$.
   - *Why needed:* Equivariance of the corrected derivative (Subgoal 2) and the well-definedness of $\rho_*\colon\operatorname{ad}P\to\operatorname{End}E$ in part (c) both use it.

2. **The corrected derivative descends.** Show $\Phi(\hat s):=d\hat s+\rho_*(\omega)\hat s$ is horizontal and $\rho$-equivariant for every equivariant $\hat s$.
   - *Hint:* Evaluate on $\xi_P$ using $d\hat s(\xi_P)=-\rho_*(\xi)\hat s$ and $\omega(\xi_P)=\xi$; for equivariance pull back by $R_g$ using (C1) and Subgoal 1.
   - *Why needed:* Only horizontal equivariant forms descend to $E$-valued forms on $M$; this is what makes $\nabla^\omega s$ exist.

3. **$\nabla^\omega$ is a connection, and unique.** Verify the Leibniz rule and that the defining property determines $\nabla^\omega$.
   - *Hint:* The lift of $fs$ is $(f\circ\pi)\hat s$; expand $\Phi((f\circ\pi)\hat s)$ and use $d(f\circ\pi)=\pi^*df$.
   - *Why needed:* Part (a) claims a *connection*, and a *unique* one.

4. **Local formula and gauge-independence.** Pull $\Phi(\hat s)$ back along $\sigma$ to get $\nabla^\omega=d+\rho_*(A)$; recompute in the gauge $\sigma g$ and check the answer is unchanged.
   - *Hint:* Use $(\sigma g)^*\omega=\operatorname{Ad}_{g^{-1}}A+g^*\theta$ and $\partial_X(\rho(g^{-1})v)=-\rho_*(g^*\theta(X))\rho(g^{-1})v+\rho(g^{-1})\partial_Xv$; watch the $\rho_*(g^*\theta(X))$ terms cancel.
   - *Why needed:* The local formula is the working form and must be a definition, not a gauge-dependent expression.

5. **Curvature.** From $\nabla^\omega=d+\rho_*(A)$ compute $F_{\nabla^\omega}=\rho_*(dA)+\rho_*(A)\wedge\rho_*(A)$ and match it to $\rho_*(dA+\tfrac12[A\wedge A])$ using Subgoal 1.
   - *Hint:* $(\rho_*(A)\wedge\rho_*(A))(X,Y)=[\rho_*A(X),\rho_*A(Y)]=\rho_*([A(X),A(Y)])$.
   - *Why needed:* Part (c).

6. **Frame bundle and adjoint bundle.** Specialise $\rho$ to the standard representation of $GL_k$ (part d) and to $\operatorname{Ad}$ (part e); prove the multilinear-naturality lemma to identify the induced connections on $E^*,\operatorname{End}E,\Lambda^pE$.
   - *Hint:* For the standard representation $\rho_*=\operatorname{id}$, so the local matrix is $e^*\omega=A(\nabla,e)$; for naturality differentiate the equivariance of the multilinear map.
   - *Why needed:* Parts (d) and (e).

---

# Lemma Decomposition

> [!note]- Lemma 1: Naturality of the differential of a representation
> **Statement:** For a representation $\rho\colon G\to GL(V)$ with differential $\rho_*\colon\mathfrak g\to\operatorname{End}(V)$, every $g\in G$ and $\xi,\eta\in\mathfrak g$,
> $$\rho_*(\operatorname{Ad}_g\xi)=\rho(g)\,\rho_*(\xi)\,\rho(g)^{-1},\qquad\text{hence}\qquad\rho_*(\operatorname{Ad}_{g^{-1}}\xi)=\rho(g^{-1})\,\rho_*(\xi)\,\rho(g),$$
> and $\rho_*[\xi,\eta]=[\rho_*\xi,\rho_*\eta]=\rho_*\xi\,\rho_*\eta-\rho_*\eta\,\rho_*\xi$.
>
> **Hint:** Differentiate the conjugation identity $\rho(g\exp(t\xi)g^{-1})=\rho(g)\rho(\exp t\xi)\rho(g)^{-1}$ in $t$, then the resulting identity in $g$.
>
> **Why needed:** Subgoal 1. Equivariance of the corrected derivative and well-definedness of $\rho_*\colon\operatorname{ad}P\to\operatorname{End}E$ both rely on the first identity; the curvature computation relies on the homomorphism property.
>
> > [!note]- Full proof
> > **Conjugation identity.** Fix $g\in G$ and $\xi\in\mathfrak g$. Since $\operatorname{Ad}_g=d_e(h\mapsto ghg^{-1})$ and $\exp(t\operatorname{Ad}_g\xi)=g\exp(t\xi)g^{-1}$ (the exponential intertwines $\operatorname{Ad}_g$ with conjugation, because $t\mapsto g\exp(t\xi)g^{-1}$ is the one-parameter subgroup with initial velocity $\operatorname{Ad}_g\xi$, by [[Thm - One-Parameter Subgroups are the Integral Curves of Left-Invariant Vector Fields|the characterisation of one-parameter subgroups]]), we compute
> > $$\rho_*(\operatorname{Ad}_g\xi)=\frac{d}{dt}\Big|_{0}\rho\big(\exp(t\operatorname{Ad}_g\xi)\big)=\frac{d}{dt}\Big|_{0}\rho\big(g\exp(t\xi)g^{-1}\big)\qquad\text{(definition of }\rho_*\text{; the intertwining identity).}$$
> > Because $\rho$ is a group homomorphism, $\rho(g\exp(t\xi)g^{-1})=\rho(g)\,\rho(\exp t\xi)\,\rho(g)^{-1}$, and $\rho(g),\rho(g)^{-1}$ are constant, so
> > $$\rho_*(\operatorname{Ad}_g\xi)=\rho(g)\Big(\frac{d}{dt}\Big|_{0}\rho(\exp t\xi)\Big)\rho(g)^{-1}=\rho(g)\,\rho_*(\xi)\,\rho(g)^{-1}\qquad\text{(homomorphism property; definition of }\rho_*\text{).}$$
> > Replacing $g$ by $g^{-1}$ gives $\rho_*(\operatorname{Ad}_{g^{-1}}\xi)=\rho(g^{-1})\rho_*(\xi)\rho(g)$.
> >
> > **Homomorphism property.** Differentiate the conjugation identity $\rho_*(\operatorname{Ad}_g\xi)=\rho(g)\rho_*(\xi)\rho(g)^{-1}$ along $g=\exp(s\eta)$ at $s=0$. The left-hand side gives $\frac{d}{ds}\big|_0\rho_*(\operatorname{Ad}_{\exp s\eta}\xi)=\rho_*\big(\frac{d}{ds}\big|_0\operatorname{Ad}_{\exp s\eta}\xi\big)=\rho_*(\operatorname{ad}_\eta\xi)=\rho_*([\eta,\xi])$, using that $\rho_*$ is linear and that $\frac{d}{ds}\big|_0\operatorname{Ad}_{\exp s\eta}=\operatorname{ad}_\eta$ with $\operatorname{ad}_\eta\xi=[\eta,\xi]$ (this is [[Thm - Ad is a Smooth Representation and its Differential is ad|the theorem that the differential of Ad is ad]]). The right-hand side gives, by the product rule,
> > $$\frac{d}{ds}\Big|_0\Big(\rho(\exp s\eta)\,\rho_*(\xi)\,\rho(\exp(-s\eta))\Big)=\rho_*(\eta)\rho_*(\xi)-\rho_*(\xi)\rho_*(\eta)=[\rho_*\eta,\rho_*\xi]\qquad\text{(product rule; }\tfrac{d}{ds}\big|_0\rho(\exp(\pm s\eta))=\pm\rho_*(\eta)\text{).}$$
> > Hence $\rho_*([\eta,\xi])=[\rho_*\eta,\rho_*\xi]$; renaming $(\eta,\xi)\mapsto(\xi,\eta)$ gives $\rho_*[\xi,\eta]=[\rho_*\xi,\rho_*\eta]$. $\blacksquare$

> [!note]- Lemma 2: The corrected derivative is horizontal and equivariant
> **Statement:** Let $\omega$ be a connection on $P$ and $\hat s\in C^\infty(P;V)^G$. Then the $V$-valued $1$-form
> $$\Phi(\hat s):=d\hat s+\rho_*(\omega)\hat s\in\Omega^1(P;V),\qquad \Phi(\hat s)(X)=d\hat s(X)+\rho_*(\omega(X))\hat s,$$
> is horizontal ($\Phi(\hat s)$ vanishes on vertical vectors) and equivariant ($R_g^*\Phi(\hat s)=\rho(g^{-1})\Phi(\hat s)$); hence it is basic of type $\rho$ and corresponds to a unique $1$-form on $M$ with values in $E$.
>
> **Hint:** Evaluate on the fundamental field $\xi_P$; for equivariance use $R_g^*\omega=\operatorname{Ad}_{g^{-1}}\omega$ and Lemma 1.
>
> **Why needed:** Subgoal 2. This is what makes $\nabla^\omega s$ exist, via the basic-forms correspondence.
>
> > [!note]- Full proof
> > **Horizontality.** The vertical subspace $V_p$ is spanned by the fundamental vectors $\xi_P(p)$, $\xi\in\mathfrak g$, so it suffices to show $\Phi(\hat s)(\xi_P)=0$ for every $\xi$. By $G$-equivariance of $\hat s$, for fixed $p$ we have $\hat s(p\exp t\xi)=\rho\big((\exp t\xi)^{-1}\big)\hat s(p)=\rho(\exp(-t\xi))\hat s(p)$, so differentiating at $t=0$ and using $\xi_P(p)=\frac{d}{dt}\big|_0 p\exp(t\xi)$,
> > $$d\hat s\big(\xi_P(p)\big)=\frac{d}{dt}\Big|_0\hat s(p\exp t\xi)=\frac{d}{dt}\Big|_0\rho(\exp(-t\xi))\hat s(p)=-\rho_*(\xi)\hat s(p)\qquad\text{(equivariance of }\hat s\text{; definition of }\rho_*\text{).}$$
> > By connection axiom (C2), $\omega(\xi_P(p))=\xi$, so $\rho_*(\omega)\hat s\,(\xi_P(p))=\rho_*(\xi)\hat s(p)$. Adding,
> > $$\Phi(\hat s)\big(\xi_P(p)\big)=-\rho_*(\xi)\hat s(p)+\rho_*(\xi)\hat s(p)=0\qquad\text{(the two terms cancel).}$$
> > Thus $\Phi(\hat s)$ vanishes on every vertical vector; it is horizontal.
> >
> > **Equivariance.** We must show $R_g^*\Phi(\hat s)=\rho(g^{-1})\Phi(\hat s)$ for every $g\in G$. Treat the two summands separately. For the first, $R_g^*(d\hat s)=d(R_g^*\hat s)=d(\hat s\circ R_g)$ because the exterior derivative commutes with pullback ([[Thm - Pull-Back Commutes with the Exterior Derivative|pullback commutes with d]]). By equivariance of $\hat s$, $\hat s\circ R_g=\hat s(\cdot\,g)=\rho(g^{-1})\hat s$, and $\rho(g^{-1})$ is a constant linear endomorphism of $V$, so
> > $$R_g^*(d\hat s)=d\big(\rho(g^{-1})\hat s\big)=\rho(g^{-1})\,d\hat s\qquad\text{(pullback commutes with }d\text{; equivariance of }\hat s\text{; }\rho(g^{-1})\text{ constant).}$$
> > For the second summand, using $R_g^*(\rho_*(\omega)\hat s)=\rho_*(R_g^*\omega)\,(R_g^*\hat s)$ and connection axiom (C1) $R_g^*\omega=\operatorname{Ad}_{g^{-1}}\omega$,
> > $$R_g^*\big(\rho_*(\omega)\hat s\big)=\rho_*\big(\operatorname{Ad}_{g^{-1}}\omega\big)\big(\rho(g^{-1})\hat s\big).$$
> > By Lemma 1, $\rho_*(\operatorname{Ad}_{g^{-1}}\omega(X))=\rho(g^{-1})\rho_*(\omega(X))\rho(g)$; applying this endomorphism to $\rho(g^{-1})\hat s$ and using $\rho(g)\rho(g^{-1})=\operatorname{id}$,
> > $$R_g^*\big(\rho_*(\omega)\hat s\big)=\rho(g^{-1})\rho_*(\omega)\rho(g)\rho(g^{-1})\hat s=\rho(g^{-1})\big(\rho_*(\omega)\hat s\big)\qquad\text{(Lemma 1; }\rho(g)\rho(g^{-1})=\operatorname{id}\text{).}$$
> > Adding the two,
> > $$R_g^*\Phi(\hat s)=\rho(g^{-1})\,d\hat s+\rho(g^{-1})\big(\rho_*(\omega)\hat s\big)=\rho(g^{-1})\Phi(\hat s).$$
> > Thus $\Phi(\hat s)$ is horizontal and equivariant, i.e. basic of type $\rho$; by [[Thm - Bundle-Valued Forms on the Base are Basic Equivariant Forms on the Total Space|the basic-forms correspondence]] — for a principal $G$-bundle $P$ and representation $\rho$ the map $\alpha\mapsto\hat\alpha$ is a bijection $\Omega^1(M;E)\to\Omega^1_{\mathrm{bas}}(P;V)^G$ — there is a unique $\alpha\in\Omega^1(M;E)$ with $\pi^*\alpha\leftrightarrow\Phi(\hat s)$. $\blacksquare$

> [!note]- Lemma 3: Induced connections are natural for equivariant multilinear maps
> **Statement:** Let $V_1,\dots,V_r,W$ be representations of $G$ (with differentials $\rho_{i*}$, $\rho_{W*}$) and $\beta\colon V_1\times\dots\times V_r\to W$ a $G$-equivariant multilinear map, meaning $\beta(\rho_1(g)v_1,\dots,\rho_r(g)v_r)=\rho_W(g)\beta(v_1,\dots,v_r)$. Write $E_i=P\times_{\rho_i}V_i$, $E_W=P\times_{\rho_W}W$, and let $\underline\beta\colon E_1\times_M\dots\times_M E_r\to E_W$, $\underline\beta([p,v_1],\dots,[p,v_r])=[p,\beta(v_1,\dots,v_r)]$, be the induced fibrewise multilinear bundle map. Then for sections $s_i\in\Gamma(E_i)$,
> $$\nabla^\omega\,\underline\beta(s_1,\dots,s_r)=\sum_{i=1}^r\underline\beta(s_1,\dots,\nabla^\omega s_i,\dots,s_r).$$
>
> **Hint:** Lift everything to $P$; differentiate the equivariance identity of $\beta$ at $g=1$ to get its infinitesimal form; apply the multilinear Leibniz rule to $\Phi$.
>
> **Why needed:** Subgoal 6. Instantiating $\beta$ at the evaluation pairing, evaluation of endomorphisms, and the wedge product yields the product rules that characterise the induced connections on $E^*$, $\operatorname{End}E$ and $\Lambda^pE$, giving part (d).
>
> > [!note]- Full proof
> > **Well-definedness of $\underline\beta$.** For fixed $p$ the map $[p,\cdot]\colon V_i\to (E_i)_{\pi(p)}$ is an isomorphism, and replacing $(p,v_i)$ by $(pg,\rho_i(g^{-1})v_i)$ leaves $\underline\beta$ unchanged: $[pg,\beta(\rho_1(g^{-1})v_1,\dots)]=[pg,\rho_W(g^{-1})\beta(v_1,\dots)]=[p,\beta(v_1,\dots)]$, by equivariance of $\beta$ (with $g^{-1}$) and the associated-bundle relation. So $\underline\beta$ is a well-defined bundle map, and the lift of $\underline\beta(s_1,\dots,s_r)$ is $\widehat{\underline\beta(s_\bullet)}=\beta(\hat s_1,\dots,\hat s_r)$, which is equivariant because $\beta$ is.
> >
> > **Infinitesimal equivariance of $\beta$.** Differentiating $\beta(\rho_1(\exp t\xi)v_1,\dots,\rho_r(\exp t\xi)v_r)=\rho_W(\exp t\xi)\beta(v_1,\dots,v_r)$ at $t=0$, and using the multilinear product rule on the left, gives
> > $$\sum_{i=1}^r\beta\big(v_1,\dots,\rho_{i*}(\xi)v_i,\dots,v_r\big)=\rho_{W*}(\xi)\,\beta(v_1,\dots,v_r)\qquad(\ast)$$
> > for all $\xi\in\mathfrak g$.
> >
> > **The computation.** By Lemma 2 applied in the representation $W$, $\pi^*\nabla^\omega\underline\beta(s_\bullet)\leftrightarrow d\beta(\hat s_\bullet)+\rho_{W*}(\omega)\beta(\hat s_\bullet)$. The exterior derivative obeys the multilinear Leibniz rule (evaluate on a vector $X$, differentiate the multilinear function $\beta(\hat s_1,\dots,\hat s_r)$ of the several arguments):
> > $$d\beta(\hat s_1,\dots,\hat s_r)(X)=\sum_{i=1}^r\beta\big(\hat s_1,\dots,d\hat s_i(X),\dots,\hat s_r\big)\qquad\text{(multilinear Leibniz rule for }d\text{).}$$
> > For the correction term, apply $(\ast)$ with $\xi=\omega(X)$ and $v_i=\hat s_i$:
> > $$\rho_{W*}(\omega(X))\beta(\hat s_1,\dots,\hat s_r)=\sum_{i=1}^r\beta\big(\hat s_1,\dots,\rho_{i*}(\omega(X))\hat s_i,\dots,\hat s_r\big)\qquad\text{(by }(\ast)\text{).}$$
> > Adding the last two displays and grouping the $i$-th summands,
> > $$\big(d\beta(\hat s_\bullet)+\rho_{W*}(\omega)\beta(\hat s_\bullet)\big)(X)=\sum_{i=1}^r\beta\big(\hat s_1,\dots,\,d\hat s_i(X)+\rho_{i*}(\omega(X))\hat s_i,\,\dots,\hat s_r\big)=\sum_{i=1}^r\beta\big(\hat s_1,\dots,\Phi(\hat s_i)(X),\dots,\hat s_r\big).$$
> > By Lemma 2 in each representation $V_i$, $\Phi(\hat s_i)\leftrightarrow\pi^*\nabla^\omega s_i$, so the right-hand side is $\big(\sum_i\underline\beta(s_1,\dots,\nabla^\omega s_i,\dots,s_r)\big)$ read on lifts. Since the basic-forms correspondence is a bijection, the descended forms agree:
> > $$\nabla^\omega\underline\beta(s_1,\dots,s_r)=\sum_{i=1}^r\underline\beta(s_1,\dots,\nabla^\omega s_i,\dots,s_r).\qquad\blacksquare$$

---

# Formal Proof

> [!note]- Complete formal proof
> Fix the principal bundle $\pi\colon P\to M$, the connection $\omega$, the representation $\rho\colon G\to GL(V)$, and the associated bundle $E=P\times_\rho V$.
>
> **Step 0 — the objects are well-posed.** The equivariant-function correspondence $\Gamma(E)\cong C^\infty(P;V)^G$ and the basic-forms correspondence $\Omega^q(M;E)\cong\Omega^q_{\mathrm{bas}}(P;V)^G$ are bijections of $C^\infty(M)$-modules ([[Thm - Sections of an Associated Bundle are Equivariant Functions|sections as equivariant functions]]; [[Thm - Bundle-Valued Forms on the Base are Basic Equivariant Forms on the Total Space|basic-forms correspondence]]). The differential $\rho_*\colon\mathfrak g\to\operatorname{End}(V)$ exists and is a Lie-algebra homomorphism (Lemma 1). These are all we invoke without re-deriving.
>
> **Step 1 — part (a): existence, the Leibniz rule, and uniqueness.**
>
> **Define the operator.** For $s\in\Gamma(E)$ with equivariant lift $\hat s$, set $\Phi(\hat s):=d\hat s+\rho_*(\omega)\hat s\in\Omega^1(P;V)$. By **Lemma 2** the form $\Phi(\hat s)$ is horizontal and equivariant, hence basic of type $\rho$, so there is a unique $\nabla^\omega s\in\Omega^1(M;E)$ with $\pi^*(\nabla^\omega s)\leftrightarrow\Phi(\hat s)$. This defines a map $\nabla^\omega\colon\Gamma(E)\to\Omega^1(M;E)$; it is $\mathbb R$-linear because $\hat s\mapsto\Phi(\hat s)$ is linear and the correspondence is linear.
>
> **Leibniz rule.** Let $f\in C^\infty(M)$. The lift of $fs$ is $\widehat{fs}=(f\circ\pi)\hat s$: indeed $f\circ\pi$ is $G$-invariant (constant on fibres), so $(f\circ\pi)\hat s$ is equivariant, and $(fs)(\pi(p))=f(\pi(p))\,[p,\hat s(p)]=[p,(f\circ\pi)(p)\hat s(p)]$. Then
> $$\Phi\big((f\circ\pi)\hat s\big)=d\big((f\circ\pi)\hat s\big)+\rho_*(\omega)(f\circ\pi)\hat s=d(f\circ\pi)\otimes\hat s+(f\circ\pi)\,d\hat s+(f\circ\pi)\,\rho_*(\omega)\hat s\qquad\text{(Leibniz rule for }d\text{; }\rho_*(\omega)\text{ is }C^\infty\text{-linear in }\hat s\text{),}$$
> $$=\pi^*(df)\otimes\hat s+(f\circ\pi)\,\Phi(\hat s)\qquad\text{(since }d(f\circ\pi)=\pi^*df\text{).}$$
> Under the basic-forms correspondence, $\pi^*(df)\otimes\hat s\leftrightarrow df\otimes s$ (the form $df\otimes s$ on $M$ lifts to $\pi^*df\otimes\hat s$) and multiplication by $f\circ\pi$ corresponds to multiplication by $f$. Therefore $\nabla^\omega(fs)=df\otimes s+f\,\nabla^\omega s$. With $\mathbb R$-linearity, $\nabla^\omega$ is a connection on $E$.
>
> **Uniqueness.** Suppose $\nabla'$ is any connection on $E$ with $\pi^*(\nabla's)\leftrightarrow\Phi(\hat s)$ for every $s$. Then for each $s$ the forms $\nabla's$ and $\nabla^\omega s$ correspond to the same basic form $\Phi(\hat s)$; since the basic-forms correspondence is a bijection, $\nabla's=\nabla^\omega s$. As this holds for all $s$, $\nabla'=\nabla^\omega$. This proves part (a).
>
> **Step 2 — part (b): the local formula and its independence of the gauge.**
>
> **Local formula.** Let $\sigma\colon U\to P$ be a local section with gauge potential $A=\sigma^*\omega\in\Omega^1(U;\mathfrak g)$, and let $v\colon U\to V$ be smooth. The section $s=[\sigma,v]\in\Gamma(E|_U)$ has equivariant lift determined by $\hat s(\sigma(u))=v(u)$. For $X\in T_uU$, the vector $d\sigma(X)\in T_{\sigma(u)}P$ satisfies $d\pi(d\sigma(X))=d(\pi\circ\sigma)(X)=X$, since $\pi\circ\sigma=\operatorname{id}_U$. Evaluating the defining relation $\pi^*(\nabla^\omega s)\leftrightarrow\Phi(\hat s)$ at $\sigma(u)$ on $d\sigma(X)$,
> $$(\nabla^\omega s)(X)=\big[\sigma(u),\ \Phi(\hat s)_{\sigma(u)}\big(d\sigma(X)\big)\big]=\big[\sigma(u),\ (\sigma^*\Phi(\hat s))(X)\big].$$
> Now $\sigma^*\Phi(\hat s)=\sigma^*(d\hat s)+\sigma^*(\rho_*(\omega)\hat s)=d(\hat s\circ\sigma)+\rho_*(\sigma^*\omega)(\hat s\circ\sigma)=dv+\rho_*(A)v$, using $\hat s\circ\sigma=v$ and that pullback commutes with $d$ and with the pointwise action $\rho_*$. Therefore
> $$\nabla^\omega_X[\sigma,v]=\big[\sigma,\ \partial_Xv+\rho_*(A(X))v\big],$$
> which is the claimed formula. In particular, in the local frame of $E$ given by $\sigma$ — the trivialisation $E|_U\cong U\times V$, $[\sigma(u),w]\mapsto(u,w)$ — the covariant derivative is $\nabla^\omega=d+\rho_*(A)$, so the connection matrix of $\nabla^\omega$ in this frame is $\rho_*(A)\in\Omega^1(U;\operatorname{End}V)$.
>
> **Independence of the representative.** The same section can be written $s=[\sigma',v']$ with $\sigma'=\sigma g$ for a smooth $g\colon U\to G$ and $v'=\rho(g^{-1})v$ (because $[\sigma g,\rho(g^{-1})v]=[\sigma,v]$). We must show the formula computed in the gauge $\sigma'$ agrees with the one computed in $\sigma$; because the formula is what will be *taken* as the working definition, this well-definedness is essential. Write $g_0=g(u_0)$ and $\xi_X:=g^*\theta(X)\in\mathfrak g$ for the pullback of the [[Def - The Maurer-Cartan Form|Maurer–Cartan form]] $\theta$, so that $g^*\theta(X)=(dL_{g_0^{-1}})(dg_{u_0}(X))$ (for matrix groups $g^*\theta(X)=g_0^{-1}\partial_Xg$). We use two identities.
>
> First, the gauge potential transforms by [[Ex - The Pull-Back of the Maurer-Cartan Form along a Product of Maps|the Maurer–Cartan product rule]] $(g_1g_2)^*\theta=\operatorname{Ad}_{g_2^{-1}}(g_1^*\theta)+g_2^*\theta$, applied to $\sigma'{}^*\omega=(\sigma g)^*\omega$ as in [[Thm - Transformation of Local Connection and Curvature Forms|the transformation law for local connection forms]] — for $\sigma'=\sigma g$, $A'=\sigma'{}^*\omega=\operatorname{Ad}_{g^{-1}}A+g^*\theta$. At $u_0$ and on $X$,
> $$A'(X)=\operatorname{Ad}_{g_0^{-1}}\big(A(X)\big)+\xi_X.\qquad(\text{i})$$
>
> Second, we differentiate $v'=\rho(g^{-1})v$. Choose a curve $u(t)$ with $u(0)=u_0$, $\dot u(0)=X$, and write $g(t)=g(u(t))$, $M(t)=\rho(g(t))\in GL(V)$. Then $\frac{d}{dt}\big|_0\rho(g(t))=\rho(g_0)\rho_*(\xi_X)$: indeed $\rho(g(t))=\rho(g_0)\rho(g_0^{-1}g(t))$ and $\frac{d}{dt}\big|_0 g_0^{-1}g(t)=dL_{g_0^{-1}}(\dot g(0))=\theta_{g_0}(\dot g(0))=\xi_X$, so $\frac{d}{dt}\big|_0\rho(g_0^{-1}g(t))=\rho_*(\xi_X)$. Hence, differentiating $\rho(g(t)^{-1})=\rho(g(t))^{-1}=M(t)^{-1}$ with $\frac{d}{dt}M^{-1}=-M^{-1}\dot MM^{-1}$,
> $$\frac{d}{dt}\Big|_0\rho(g(t)^{-1})=-\rho(g_0)^{-1}\big(\rho(g_0)\rho_*(\xi_X)\big)\rho(g_0)^{-1}=-\rho_*(\xi_X)\rho(g_0)^{-1}\qquad\text{(derivative of a matrix inverse).}$$
> Therefore, by the product rule,
> $$\partial_Xv'=\frac{d}{dt}\Big|_0\rho(g(t)^{-1})v(u(t))=-\rho_*(\xi_X)\rho(g_0^{-1})v+\rho(g_0^{-1})\partial_Xv.\qquad(\text{ii})$$
>
> Now compute the correction term in the gauge $\sigma'$. Using (i) and Lemma 1 ($\rho_*(\operatorname{Ad}_{g_0^{-1}}\zeta)=\rho(g_0^{-1})\rho_*(\zeta)\rho(g_0)$),
> $$\rho_*(A'(X))=\rho_*\big(\operatorname{Ad}_{g_0^{-1}}A(X)\big)+\rho_*(\xi_X)=\rho(g_0^{-1})\rho_*(A(X))\rho(g_0)+\rho_*(\xi_X)\qquad\text{(by (i); Lemma 1),}$$
> and applying this to $v'=\rho(g_0^{-1})v$, with $\rho(g_0)\rho(g_0^{-1})=\operatorname{id}$,
> $$\rho_*(A'(X))v'=\rho(g_0^{-1})\rho_*(A(X))v+\rho_*(\xi_X)\rho(g_0^{-1})v.\qquad(\text{iii})$$
> Adding (ii) and (iii), the terms $\mp\rho_*(\xi_X)\rho(g_0^{-1})v$ cancel:
> $$\partial_Xv'+\rho_*(A'(X))v'=\rho(g_0^{-1})\partial_Xv+\rho(g_0^{-1})\rho_*(A(X))v=\rho(g_0^{-1})\big(\partial_Xv+\rho_*(A(X))v\big)\qquad\text{(the }\rho_*(\xi_X)\rho(g_0^{-1})v\text{ terms cancel).}$$
> Consequently
> $$\big[\sigma'(u_0),\,\partial_Xv'+\rho_*(A'(X))v'\big]=\big[\sigma(u_0)g_0,\,\rho(g_0^{-1})\big(\partial_Xv+\rho_*(A(X))v\big)\big]=\big[\sigma(u_0),\,\partial_Xv+\rho_*(A(X))v\big],$$
> using the associated-bundle relation $[pg,\rho(g^{-1})w]=[p,w]$. The two gauges give the same element of $E$, so the local formula is independent of the representative. This proves part (b), completing Bär's Remark 2.3.9, whose printed computation stops at this cancellation.
>
> **Step 3 — part (c): the curvature.** By Step 2, in the local frame furnished by a section $\sigma$ the connection $\nabla^\omega$ has connection matrix $B:=\rho_*(A)\in\Omega^1(U;\operatorname{End}V)$, so $\nabla^\omega=d+B$ locally. By [[Thm - Local Formula for the Curvature of a Connection|the local curvature formula for a vector-bundle connection]] — for $\nabla=d+B$ in a frame, $F_\nabla=dB+B\wedge B$, where $(B\wedge B)(X,Y)=B(X)B(Y)-B(Y)B(X)$ — we have
> $$F_{\nabla^\omega}=d\big(\rho_*(A)\big)+\rho_*(A)\wedge\rho_*(A)=\rho_*(dA)+\rho_*(A)\wedge\rho_*(A)\qquad\text{(since }\rho_*\text{ is a constant linear map, }d\rho_*(A)=\rho_*(dA)\text{).}$$
> For the quadratic term, evaluate on $X,Y$ and use that $\rho_*$ is a Lie-algebra homomorphism (Lemma 1):
> $$\big(\rho_*(A)\wedge\rho_*(A)\big)(X,Y)=\rho_*(A(X))\rho_*(A(Y))-\rho_*(A(Y))\rho_*(A(X))=\big[\rho_*(A(X)),\rho_*(A(Y))\big]=\rho_*\big([A(X),A(Y)]\big).$$
> By the bracket convention $\tfrac12[A\wedge A](X,Y)=[A(X),A(Y)]$, the right-hand side equals $\rho_*\big(\tfrac12[A\wedge A](X,Y)\big)$, so $\rho_*(A)\wedge\rho_*(A)=\rho_*\big(\tfrac12[A\wedge A]\big)$. Therefore
> $$F_{\nabla^\omega}=\rho_*(dA)+\rho_*\big(\tfrac12[A\wedge A]\big)=\rho_*\big(dA+\tfrac12[A\wedge A]\big)=\rho_*(F_\sigma),$$
> where $F_\sigma=dA+\tfrac12[A\wedge A]$ is the local curvature of $\omega$ by [[Thm - Structure Equation for the Curvature|the structure equation]] ($\Omega=d\omega+\tfrac12[\omega\wedge\omega]$, hence $F_\sigma=\sigma^*\Omega=dA+\tfrac12[A\wedge A]$). Finally $\rho_*\colon\operatorname{ad}P\to\operatorname{End}E$, $[p,\xi]\mapsto[p,\rho_*(\xi)]$, is a well-defined bundle map: it is independent of the representative because $\rho_*(\operatorname{Ad}_g\xi)=\rho(g)\rho_*(\xi)\rho(g)^{-1}$ (Lemma 1) is exactly the transformation law of $\operatorname{End}E=P\times_{\operatorname{conj}}\operatorname{End}V$. Since $F_\omega$ restricts locally to $[\sigma,F_\sigma]$, the identities $F_{\nabla^\omega}=\rho_*(F_\sigma)$ glue to the global equality $F_{\nabla^\omega}=\rho_*(F_\omega)\in\Omega^2(M;\operatorname{End}E)$. This proves part (c).
>
> **Step 4 — part (d): compatibility with the frame-bundle construction.**
>
> **The frame bundle.** Let $E$ have rank $k$, $P=\operatorname{Fr}(E)$, $G=GL_k(\mathbb R)$, and $\rho$ the standard representation on $V=\mathbb R^k$; then $E\cong\operatorname{Fr}(E)\times_\rho\mathbb R^k$ canonically ([[Thm - Vector Bundles are Associated to Their Frame Bundles|vector bundles are associated to their frame bundles]]). A local frame $e=(e_1,\dots,e_k)$ of $E$ is the same as a local section of $\operatorname{Fr}(E)$, and it furnishes the frame of $E$ in which Step 2 computed the connection matrix of $\nabla^\omega$ to be $\rho_*(e^*\omega)$. For the standard representation of $GL_k$ the differential is the identity, $\rho_*=\operatorname{id}\colon\mathfrak{gl}_k\to\operatorname{End}(\mathbb R^k)=\mathfrak{gl}_k$, so the connection matrix of $\nabla^\omega$ in the frame $e$ is exactly $e^*\omega$.
>
> **Mutual inverses.** By [[Thm - A Covariant Derivative Determines a Connection on the Frame Bundle|the frame-bundle theorem]], a connection $\nabla$ on $E$ determines the unique connection $\omega$ on $\operatorname{Fr}(E)$ with $e^*\omega=A(\nabla,e)$ for every local frame $e$. Applying the construction of the present theorem to that $\omega$ produces $\nabla^\omega$ whose connection matrix in each frame $e$ is $e^*\omega=A(\nabla,e)$, the connection matrix of $\nabla$; two connections on $E$ with the same connection matrix in every local frame are equal, so $\nabla^\omega=\nabla$. Conversely, starting from a connection $\omega$ on $\operatorname{Fr}(E)$, the induced $\nabla^\omega$ has connection matrices $e^*\omega$, and the frame-bundle theorem sends $\nabla^\omega$ back to the unique connection on $\operatorname{Fr}(E)$ with those connection matrices, which is $\omega$ itself. Hence $\nabla\mapsto\omega$ and $\omega\mapsto\nabla^\omega$ are mutually inverse bijections between connections on $E$ and connections on $\operatorname{Fr}(E)$.
>
> **The dual, endomorphism, and exterior bundles.** These are the associated bundles of $\operatorname{Fr}(E)$ for the dual representation $\rho^*$ on $V^*$ (with $\langle\rho^*(g)\alpha,\rho(g)v\rangle=\langle\alpha,v\rangle$), the conjugation representation on $\operatorname{End}(V)$ ($g\cdot\phi=\rho(g)\phi\rho(g)^{-1}$), and the exterior representation $\Lambda^p\rho$ on $\Lambda^pV$. Apply **Lemma 3**:
> - *Dual.* The evaluation pairing $\beta=\langle\cdot,\cdot\rangle\colon V^*\times V\to\mathbb R$ is $G$-equivariant into the trivial representation, on whose associated bundle $\underline{\mathbb R}$ the induced connection is $d$ (there $\rho_*=0$, so $\Phi(\hat f)=d\hat f$). Lemma 3 gives $d\langle\alpha,s\rangle=\langle\nabla^\omega\alpha,s\rangle+\langle\alpha,\nabla^\omega s\rangle$ for $\alpha\in\Gamma(E^*)$, $s\in\Gamma(E)$. This is exactly the identity that characterises the direct induced connection on $E^*$ uniquely ([[Def - Induced Connections on Dual, Hom, and Endomorphism Bundles|the direct construction]]), so the two connections on $E^*$ coincide.
> - *Endomorphisms.* The evaluation $\beta\colon\operatorname{End}(V)\times V\to V$, $(\psi,v)\mapsto\psi(v)$, is $G$-equivariant. Lemma 3 gives $\nabla^\omega(T(s))=(\nabla^\omega T)(s)+T(\nabla^\omega s)$ for $T\in\Gamma(\operatorname{End}E)$, $s\in\Gamma(E)$, which is the characterising identity of the direct induced connection on $\operatorname{End}E$; the two coincide.
> - *Exterior powers.* The wedge $\beta\colon V\times\dots\times V\to\Lambda^pV$, $(v_1,\dots,v_p)\mapsto v_1\wedge\dots\wedge v_p$, is $G$-equivariant. Lemma 3 gives $\nabla^\omega(s_1\wedge\dots\wedge s_p)=\sum_i s_1\wedge\dots\wedge\nabla^\omega s_i\wedge\dots\wedge s_p$, the characterising Leibniz rule of the direct induced connection on $\Lambda^pE$; the two coincide.
>
> This proves part (d).
>
> **Step 5 — part (e): the adjoint bundle.** Take $\rho=\operatorname{Ad}\colon G\to GL(\mathfrak g)$, so $V=\mathfrak g$ and $E=P\times_{\operatorname{Ad}}\mathfrak g=\operatorname{ad}P$. The differential is $\operatorname{Ad}_*=\operatorname{ad}\colon\mathfrak g\to\operatorname{End}(\mathfrak g)$, $\operatorname{ad}_\xi\eta=[\xi,\eta]$ ([[Thm - Ad is a Smooth Representation and its Differential is ad|the differential of Ad is ad]]). By Step 2, the local form of $\nabla^\omega$ on $\operatorname{ad}P$ is
> $$\nabla^\omega_X[\sigma,\eta]=[\sigma,\ \partial_X\eta+\operatorname{ad}_{A(X)}\eta]=[\sigma,\ \partial_X\eta+[A(X),\eta]],$$
> i.e. $\nabla^\omega=d+[A\wedge\,\cdot\,]$ in the local gauge. This is precisely the connection $\nabla_a$ on $\operatorname{ad}P$ whose exterior covariant derivative acts on $\operatorname{ad}P$-valued forms as $d+[A\wedge\,\cdot\,]$ and which appears in the [[Thm - Bianchi Identity for a Principal Connection|Bianchi identity]] $d^{\nabla_a}F_\omega=0$, whose local form is $dF_\sigma+[A\wedge F_\sigma]=0$. Its curvature, by part (c), is $F_{\nabla^\omega}=\operatorname{ad}(F_\omega)=[F_\omega,\,\cdot\,]\in\Omega^2(M;\operatorname{End}(\operatorname{ad}P))$. This proves part (e).
>
> All five parts are established. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Riemannian geometry: the Levi-Civita connection as an induced connection.** Take $(M,g)$ and its orthonormal frame bundle $\operatorname{Fr}_O(TM)$, a principal $O(n)$-bundle, and let $\omega$ be the Levi-Civita connection viewed as an $\mathfrak{o}(n)$-valued connection form. The induced connection $\nabla^\omega$ on $TM=\operatorname{Fr}_O(TM)\times_\rho\mathbb R^n$ (standard representation) is the Levi-Civita covariant derivative, and part (d) says its Christoffel symbols in a coordinate frame are the entries of $e^*\omega$. The theorem applies because a metric is a reduction of the structure group; the exercise is non-obvious because the reader must recognise metric compatibility of $\nabla$ as the statement that $\omega$ is $\mathfrak{o}(n)$-valued, and part (c) then identifies the Riemann curvature tensor with $\rho_*(F_\omega)$.

**Gauge theory: minimal coupling and conserved charge.** For a $U(1)$ gauge field $\omega$ (electromagnetism) and the charge-$q$ representation $\rho_q(\lambda)=\lambda^q$ of $U(1)$ on $\mathbb C$, the induced covariant derivative on the associated line bundle is $\nabla^\omega=d+q\,iA$ locally, since $\rho_{q*}(iA)=qiA$. The theorem applies because a charged matter field is a section of $P\times_{\rho_q}\mathbb C$; the exercise is non-obvious because it shows the integer $q$ that labels the representation is exactly the electric charge appearing in the coupled Dirac or Klein–Gordon operator, and part (c) shows every charge sector feels the same field strength $F_\omega$ scaled by $q$.

**Representation theory: why the adjoint bundle is special.** Show, using part (e) and Lemma 1, that the induced connection on $\operatorname{ad}P$ is the unique one making the bracket $\operatorname{ad}P\times\operatorname{ad}P\to\operatorname{ad}P$ parallel and making the Killing form (when $G$ is semisimple) covariantly constant. The theorem applies because the bracket $[\cdot,\cdot]\colon\mathfrak g\times\mathfrak g\to\mathfrak g$ is $\operatorname{Ad}$-equivariant; the exercise is non-obvious because it uses Lemma 3 with $\beta=[\cdot,\cdot]$ to turn the Jacobi identity into the parallelism of the bracket, which is the geometric root of the Bianchi identity.

---

# Bridges

- **[[Thm - A Covariant Derivative Determines a Connection on the Frame Bundle|The frame-bundle theorem]].** That theorem builds the principal connection from a covariant derivative; this one builds a covariant derivative from a principal connection. Part (d) proves the two constructions are mutually inverse, so "a connection on the rank-$k$ vector bundle $E$" and "a connection on the principal $GL_k$-bundle $\operatorname{Fr}(E)$" are literally interchangeable data. Every later chapter uses this to move a construction to whichever side is more convenient.

- **[[Thm - Structure Equation for the Curvature|The structure equation]].** The local curvature $F_\sigma=dA+\tfrac12[A\wedge A]$ enters part (c) through the structure equation, and the passage from the Lie bracket $\tfrac12[A\wedge A]$ to the commutator $\rho_*(A)\wedge\rho_*(A)$ is what makes $\rho_*(F_\omega)$ the curvature of $\nabla^\omega$. This is the precise sense in which the field strength on $P$ controls the curvature felt in every representation.

- **[[Thm - Bianchi Identity for a Principal Connection|The Bianchi identity]].** Part (e) identifies $\nabla^\omega$ on $\operatorname{ad}P$ with the connection $\nabla_a$ used to state the Bianchi identity $d^{\nabla_a}F_\omega=0$; the local form $\nabla^\omega=d+[A\wedge\,\cdot\,]$ makes the identity's local expression $dF_\sigma+[A\wedge F_\sigma]=0$ a statement about the induced adjoint connection rather than an ad hoc formula. The comparison of exterior covariant derivatives on $P$ and on associated bundles (chapter IV) refines this: $d^{\nabla^\omega}$ corresponds to the horizontal-projection operator $D^\omega$ on basic forms.

- **[[Def - Induced Connections on Dual, Hom, and Endomorphism Bundles|The direct induced connections of chapter II]].** Chapter II built connections on $E^*$, $\operatorname{End}E$ and $\Lambda^pE$ by imposing Leibniz-type compatibility with the natural pairings and products. Lemma 3 shows those product rules are the shadow on $M$ of a single fact upstairs on $P$: the corrected derivative commutes with any equivariant multilinear operation. The two constructions therefore agree, and the associated-bundle formalism explains *why* the direct product rules had to hold.

---

# Unlocked by This

> [!tip] Spinor connections *(from Spin Geometry, chapter VIII)*
> A spin structure is a principal $\operatorname{Spin}(n)$-bundle $P$ with an equivariant double cover $P\to\operatorname{Fr}_{SO}(TM)$; spinor fields are sections of $P\times_{\rho}\Sigma$ for the spin representation $\rho$. The theorem induces the spin connection $\nabla^\omega$ from the Levi-Civita connection lifted to $P$, and part (c) gives its curvature as $\rho_*(F_\omega)$ — the input to the Weitzenböck formula for the Dirac operator. See **Dirac operators on spin manifolds**.

> [!tip] Yang–Mills coupling to matter *(from Yang–Mills theory, chapter VII)*
> A matter field is a section of an associated bundle $P\times_\rho V$, and its kinetic term is built from the induced covariant derivative $\nabla^\omega=d+\rho_*(A)$. The theorem is what turns the choice of representation $\rho$ into the coupling of the gauge field to that matter, and part (c) is why the same curvature $F_\omega$ governs the field equations in every matter sector. See **the Yang–Mills–Higgs functional**.
