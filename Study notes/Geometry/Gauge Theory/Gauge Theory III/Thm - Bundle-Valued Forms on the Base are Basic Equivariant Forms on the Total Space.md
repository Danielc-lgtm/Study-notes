---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Equivariant and Basic Forms on a Principal Bundle"
  - "Def - Associated Bundle"
  - "Thm - Sections of an Associated Bundle are Equivariant Functions"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $\pi\colon P\to M$ is a smooth **principal $G$-bundle** ([[Def - Principal G-Bundle|principal bundle]]): $G$ is a Lie group acting on $P$ smoothly, freely, and fibrewise-transitively on the right, $R_g(p)=p\cdot g$, with $\pi\circ R_g=\pi$; $M$ is the base and $P$ the total space. We write $n:=\dim M$ and $k:=\dim G=\dim\mathfrak g$, so $\dim P=n+k$. Here $\mathfrak g=T_eG$ is the Lie algebra. For $\xi\in\mathfrak g$ the **fundamental vector field** is $\xi_P(p)=\frac{d}{dt}\big|_{0}\,p\cdot\exp(t\xi)$ ([[Def - Fundamental Vector Field of a Group Action|fundamental vector field]]).

We fix a finite-dimensional representation $\rho\colon G\to GL(V)$ and write $E:=P\times_\rho V$ for the **associated vector bundle** ([[Def - Associated Bundle|associated bundle]]): $E=(P\times V)/G$ for the right action $(p,v)\cdot g=(p\cdot g,\rho(g^{-1})v)$, with classes $[p,v]$ and projection $\pi[p,v]=\pi(p)$. For each $p\in P$ the map
$$\iota_p\colon V\to E_{\pi(p)},\qquad \iota_p(v)=[p,v]$$
is a linear isomorphism (established on [[Def - Associated Bundle|the associated-bundle page]]), and it satisfies the **frame-change law**
$$[p\cdot g,\,v]=[p,\,\rho(g)\,v],\qquad\text{equivalently}\qquad \iota_{p\cdot g}=\iota_p\circ\rho(g),\qquad\text{and}\qquad [p\cdot g,\,\rho(g^{-1})v]=[p,v].$$

For a smooth manifold $N$ and a vector space $W$, $\Omega^q(N;W)=\Gamma(\Lambda^q T^*N\otimes W)$ is the space of smooth $W$-valued $q$-forms; $\Omega^q(N;E)=\Gamma(\Lambda^q T^*N\otimes E)$ is the space of smooth forms with values in the vector bundle $E$ ([[Def - Bundle-Valued Differential Forms|bundle-valued forms]]). The pullback along a smooth map is $\pi^*$; the differential of $\pi$ at $p$ is $d\pi_p\colon T_pP\to T_{\pi(p)}M$, surjective because $\pi$ is a submersion. The **vertical subspace** at $p$ is $V_p:=\ker d\pi_p$; by the vertical-subspace description ([[Def - Equivariant and Basic Forms on a Principal Bundle|equivariant and basic forms]]) it equals $\{\xi_P(p):\xi\in\mathfrak g\}$ and $\xi\mapsto\xi_P(p)$ is a linear isomorphism $\mathfrak g\xrightarrow{\sim}V_p$.

A $V$-valued $q$-form $\omega\in\Omega^q(P;V)$ is **$G$-equivariant of type $\rho$** if $R_g^*\omega=\rho(g^{-1})\omega$ for all $g\in G$, and **basic** if $\omega_p(v_1,\dots,v_q)=0$ whenever some $v_j\in V_p$. The subspace of forms that are both is
$$\Omega^q_{\mathrm{bas}}(P;V)^G:=\{\omega\in\Omega^q(P;V):\omega\text{ basic and }R_g^*\omega=\rho(g^{-1})\omega\ \forall g\}.$$
When $\rho$ is the **trivial** representation ($\rho(g)=\operatorname{id}_V$), equivariance reads $R_g^*\omega=\omega$ and $\omega$ is called **invariant**; we then write $\Omega^q_{\mathrm{bas}}(P;V)^G$ for the basic invariant $V$-valued forms.

> [!warning] Convention: the general map is $a\mapsto\hat a$, not literally $a\mapsto\pi^*a$
> Haydys (Proposition 39) writes the correspondence for every representation $\rho$ as "$a\mapsto\pi^*a$". This is a harmless abuse. When $\rho$ is nontrivial, $a\in\Omega^q(M;E)$ takes values in the bundle $E$, not in the fixed vector space $V$, so the literal pullback $\pi^*a$ is a form on $P$ with values in the pulled-back bundle $\pi^*E$, not a $V$-valued form. What is meant, and what we write out below, is the $V$-valued form $\hat a$ obtained from $\pi^*a$ by reading $\pi^*E$ through its canonical trivialisation $\pi^*E\cong P\times V$, $(p,e)\mapsto(p,\iota_p^{-1}e)$; concretely $\hat a$ is characterised by $[p,\hat a_p(\hat v_1,\dots,\hat v_q)]=a_{\pi(p)}(d\pi_p\hat v_1,\dots,d\pi_p\hat v_q)$. **Only** when $\rho$ is trivial does $E=M\times V$, $\iota_p$ becomes the canonical inclusion, and $\hat a=\pi^*a$ literally. We keep the notation $\hat a$ for the general form and reserve $\pi^*a$ for the trivial-representation case.

> [!warning] Convention: fundamental-field symbol
> The vertical subspace and the "basic" condition are stated on the sibling pages with the fundamental-field symbol $\xi_P$; Haydys writes the same field as $K_\xi(p)=\frac{d}{dt}\big|_0 p\cdot\exp(t\xi)$. The two are identical, $\xi_P=K_\xi$; we use $\xi_P$ throughout to match the series.

---

# Statement

> **Theorem (bundle-valued forms on the base are basic equivariant forms on the total space).** Let $\pi\colon P\to M$ be a smooth principal $G$-bundle, $\rho\colon G\to GL(V)$ a finite-dimensional representation, $E=P\times_\rho V$ the associated bundle, and $q\ge 0$ an integer. Define
> $$\Theta\colon\Omega^q(M;E)\longrightarrow\Omega^q_{\mathrm{bas}}(P;V)^G,\qquad \Theta(a)=\hat a,$$
> where $\hat a\in\Omega^q(P;V)$ is the unique $V$-valued $q$-form determined by
> $$\bigl[p,\ \hat a_p(\hat v_1,\dots,\hat v_q)\bigr]\ =\ a_{\pi(p)}\bigl(d\pi_p\,\hat v_1,\dots,d\pi_p\,\hat v_q\bigr)\qquad(p\in P,\ \hat v_1,\dots,\hat v_q\in T_pP).\tag{$\ast$}$$
> Then $\hat a$ is basic and $G$-equivariant of type $\rho$, so $\Theta$ is well defined, and $\Theta$ is a bijection. Its inverse
> $$\Lambda\colon\Omega^q_{\mathrm{bas}}(P;V)^G\longrightarrow\Omega^q(M;E),\qquad \Lambda(\hat a)=a$$
> is given by choosing, for $m\in M$ and $v_1,\dots,v_q\in T_mM$, any $p\in\pi^{-1}(m)$ and any lifts $\hat v_j\in T_pP$ with $d\pi_p\hat v_j=v_j$, and setting
> $$a_m(v_1,\dots,v_q)\ :=\ \bigl[p,\ \hat a_p(\hat v_1,\dots,\hat v_q)\bigr]\ \in\ E_m,\tag{$\ast\ast$}$$
> the right-hand side being independent of the chosen $p$ and lifts. Moreover $\Theta$ and $\Lambda$ are isomorphisms of $C^\infty(M)$-modules, where $C^\infty(M)$ acts on the target by $f\cdot\omega:=(\pi^*f)\,\omega$.
>
> **Trivial-representation case.** If $\rho$ is trivial then $E=M\times V$, the map $\Theta$ is literally the pullback $a\mapsto\pi^*a$, and it is a bijection
> $$\pi^*\colon\Omega^q(M;V)\xrightarrow{\ \sim\ }\Omega^q_{\mathrm{bas}}(P;V)^G$$
> onto the basic invariant $V$-valued $q$-forms; taking $V=\mathbb R$, $\pi^*\colon\Omega^q(M)\xrightarrow{\sim}\Omega^q_{\mathrm{bas}}(P)^G$.

---

# Motivation

Gauge theory lives on two manifolds at once. Physical quantities — a connection's curvature, a characteristic form, a matter field — are most naturally *defined* on the total space $P$ of a principal bundle, where the group $G$ acts and where the constructions (the exterior derivative, the bracket of $\mathfrak g$-valued forms, the Maurer–Cartan form) are clean and coordinate-free. But the objects we ultimately want to integrate, to call characteristic numbers, or to feed into a field equation live on the base $M$, the actual spacetime or parameter space. We therefore need a precise dictionary that says which forms upstairs on $P$ are really forms downstairs on $M$, and with what coefficients. This theorem is that dictionary, at the level of differential forms of every degree.

The question it answers is: *given a $V$-valued form $\omega$ on $P$, when does it "come from" a form on $M$, and what does the form on $M$ have coefficients in?* Two obstructions stand between a form on $P$ and a form on $M$. First, $P$ has $k=\dim G$ extra directions — the fibre, or vertical, directions — that $M$ does not; a form on $P$ can feel them, a form on $M$ cannot. Second, a $V$-valued form on $P$ carries a fixed vector space $V$ of coefficients at every point, whereas a form on $M$ with values in the associated bundle $E$ carries the fibre $E_m$, and the identification $V\cong E_m$ is only defined *after choosing a frame $p\in P_m$*. The theorem shows that the two conditions "basic" and "equivariant" remove exactly these two obstructions, and remove nothing more: they cut the space of $V$-valued forms on $P$ down to precisely the image of $\Omega^q(M;E)$.

The degree-zero case is already familiar and is the prototype we generalise. A section of the associated bundle is the same thing as an equivariant function on $P$:

> **Theorem (sections are equivariant functions, $q=0$ case).** ([[Thm - Sections of an Associated Bundle are Equivariant Functions|sections of an associated bundle]]) The map $C^\infty(P;V)^G\to\Gamma(E)$, $\hat s\mapsto s$ with $s(\pi(p))=[p,\hat s(p)]$, is a bijection, indeed an isomorphism of $C^\infty(M)$-modules; its inverse sends $s$ to the unique $\hat s$ with $s(\pi(p))=[p,\hat s(p)]$.

An equivariant function is precisely a basic equivariant $0$-form: a $0$-form has no arguments, so "basic" is vacuous, and equivariance $R_g^*\hat s=\rho(g^{-1})\hat s$ is exactly the defining condition $\hat s(p\cdot g)=\rho(g^{-1})\hat s(p)$ of $C^\infty(P;V)^G$. Thus $\Omega^0_{\mathrm{bas}}(P;V)^G=C^\infty(P;V)^G$ and $\Omega^0(M;E)=\Gamma(E)$, and the present theorem at $q=0$ *is* the sections theorem. The content added here is the extension to $q\ge 1$, where the vertical directions become real arguments of the form and "basic" acquires teeth.

The payoff is immediate and structural: because the curvature of a principal connection is manufactured on $P$ as $d\omega+\tfrac12[\omega\wedge\omega]$, and because that $2$-form turns out to be basic and $\operatorname{Ad}$-equivariant, this theorem is what licenses us to say the curvature *is* a $2$-form on $M$ with values in the adjoint bundle $\operatorname{ad}P$ (chapter IV). The same descent turns Chern–Weil polynomials in the curvature into honest closed forms on $M$ whose integrals are characteristic numbers (chapter VI). Without the dictionary, all of these would be forms on the "wrong" manifold.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal hypothesis of the descent direction $\Lambda$ is that one holds a form on $P$ that is basic and $G$-equivariant. The skill is to recognise that a form arising naturally on $P$ — often built from objects that are *not* themselves basic — is secretly of this type, so that it may be pushed down to $M$.

The first disguised source is **the curvature of a principal connection**. A connection $\omega\in\Omega^1(P;\mathfrak g)$ is by design *not* basic: it reproduces the Lie algebra on vertical vectors, $\omega(\xi_P)=\xi\ne 0$. Nevertheless its curvature $\Omega:=d\omega+\tfrac12[\omega\wedge\omega]\in\Omega^2(P;\mathfrak g)$ *is* basic (its contraction with any $\xi_P$ vanishes, by the structure equation) and is $\operatorname{Ad}$-equivariant, $R_g^*\Omega=\operatorname{Ad}_{g^{-1}}\Omega$. The non-obvious bridge $B\Rightarrow A$ is that the failure of $\omega$ to be basic is exactly cancelled when one antisymmetrises and differentiates; the payoff is that $\Omega=\Theta(F_\omega)$ for a genuine $2$-form $F_\omega\in\Omega^2(M;\operatorname{ad}P)$, the curvature living on the base. *Example problem:* verify that $\iota_{\xi_P}\bigl(d\omega+\tfrac12[\omega\wedge\omega]\bigr)=0$ using Cartan's formula and $\mathcal L_{\xi_P}\omega=-\operatorname{ad}_\xi\omega$, and conclude that $F_\omega$ exists.

The second disguised source is **the difference of two connections**. If $\omega,\omega'\in\mathcal A(P)$ are connections then their difference $b:=\omega-\omega'$ satisfies $b(\xi_P)=\omega(\xi_P)-\omega'(\xi_P)=\xi-\xi=0$, so $b$ is basic; and both connections transform by $R_g^*=\operatorname{Ad}_{g^{-1}}$, so their difference is $\operatorname{Ad}$-equivariant. The bridge is that although a single connection is not in the domain of $\Lambda$, the *affine* difference of two is; the payoff is that $b=\Theta(\beta)$ for a unique $\beta\in\Omega^1(M;\operatorname{ad}P)$, which is exactly the statement that the space of connections is an affine space modelled on $\Omega^1(M;\operatorname{ad}P)$. *Example problem:* deduce from this theorem that $\mathcal A(P)$ is an affine space over $\Omega^1(M;\operatorname{ad}P)$ (chapter IV, Theorem 41).

The third disguised source is **an $\operatorname{Ad}$-invariant polynomial evaluated on the curvature**. Let $p$ be a degree-$d$ $\operatorname{Ad}$-invariant polynomial on $\mathfrak g$, and consider the real-valued $2d$-form $p(\Omega)$ on $P$. Its entries are those of the basic form $\Omega$, so $p(\Omega)$ is basic; the $\operatorname{Ad}$-invariance of $p$ makes $p(\Omega)$ $G$-*invariant*, i.e. equivariant for the trivial representation $V=\mathbb R$. The bridge is that a nonlinear but invariant function of a basic equivariant form is basic and invariant; the payoff, via the trivial-representation case of this theorem, is a form $p(F_\omega)\in\Omega^{2d}(M)$ on the base — the Chern–Weil form. *Example problem:* for $G\subseteq GL_k(\mathbb R)$ and $p(\xi)=\operatorname{tr}(\xi^d)$, show $\operatorname{tr}(\Omega^{\wedge d})$ is basic and invariant, hence descends to $M$ (chapter VI).

**Targets (Output Amplification)**

The bare conclusion is a $C^\infty(M)$-module isomorphism $\Omega^q(M;E)\cong\Omega^q_{\mathrm{bas}}(P;V)^G$. Combined with further structure it does a great deal.

Combine the isomorphism with **the exterior covariant derivative built on $P$**. A connection $\omega$ defines a covariant exterior derivative $d^\omega$ on $\mathfrak g$-valued (more generally $V$-valued, after applying $\rho_*$) forms on $P$ by $d^\omega\eta:=d\eta+\rho_*(\omega)\wedge\eta$, and $d^\omega$ preserves the basic equivariant subspace. Through $\Theta$ and $\Lambda$ this induces the covariant exterior derivative $d^\nabla$ on $\Omega^q(M;E)$ for the associated connection $\nabla$. The extra ingredient is the connection; the payoff is that computations of $d^\nabla$ on $M$ (Bianchi identity, Yang–Mills equation) may be carried out upstairs on $P$ where the Leibniz rule and $d^2=0$ are elementary (chapter IV).

Combine the isomorphism with **integration over a closed oriented $M$**. Once a Chern–Weil form $p(F_\omega)\in\Omega^{2d}(M)$ has been produced by the trivial-representation case, one may integrate it, $\int_M p(F_\omega)$. The extra ingredient is Stokes' theorem plus the fact (proved elsewhere) that the descended form is closed; the payoff is the connection-independence of the integral, hence a characteristic number depending only on the bundle (chapter VI).

Combine the isomorphism with **the degree-zero sections theorem**. Assembling $q=0$ (sections $=$ equivariant functions) and $q\ge 1$ (bundle-valued forms $=$ basic equivariant forms) gives a single statement: the whole de Rham-type complex $\Omega^\bullet(M;E)$ is realised inside $\Omega^\bullet(P;V)$ as the basic equivariant forms of type $\rho$, closed under the induced covariant differential. The extra ingredient is nothing beyond the two theorems; the payoff is that the algebra of bundle-valued forms on $M$ needs no separate development — it is a subquotient of ordinary $V$-valued calculus on $P$.

---

# Why Is It True

Forget the formulas for a moment and count directions. The total space $P$ sits over $M$ with $k=\dim G$ extra fibre directions at every point. A $q$-form on $P$ can be fed vectors pointing in those extra directions; a $q$-form on $M$ cannot, because those directions do not exist downstairs. So the first thing a form on $P$ must do, if it is to be the shadow of a form on $M$, is to *ignore the fibre directions* — to give the answer $0$ the instant one of its arguments is vertical. That is exactly what "basic" says. A basic form only cares about the horizontal shadow $d\pi_p\hat v$ of each argument, and $d\pi_p$ is precisely the map that forgets the vertical part.

But there is a second obstruction, invisible in the scalar case and central in the bundle-valued case. A $V$-valued form on $P$ assigns, at each point $p$, an answer in the *same* fixed space $V$. A form on $M$ with values in $E$ assigns, at each point $m$, an answer in the fibre $E_m$ — and $E_m$ is identified with $V$ only after we pick a frame $p\in P_m$, via $\iota_p$. Different frames over the same $m$ give different identifications, related by $\iota_{p\cdot g}=\iota_p\circ\rho(g)$. For a $V$-valued form on $P$ to descend, its value at $p\cdot g$ must be the $\rho(g^{-1})$-twist of its value at $p$, so that when we translate back into $E_m$ through the respective frames we get the *same* element of $E_m$. That twisting law $R_g^*\omega=\rho(g^{-1})\omega$ is exactly "equivariant". Equivariance is the compatibility that makes the frame-dependent recipe $[p,\hat a_p(\dots)]$ frame-*independent*.

> **Mechanism in one sentence.** *Basic* kills the vertical (fibre) directions so the form sees only the base, and *equivariant* makes the value transform under a change of frame exactly the way the identification $V\cong E_m$ does, so the frame-dependent recipe descends to a well-defined $E$-valued form on $M$; together they trade a $V$-valued $q$-form on the $(n+k)$-dimensional $P$ for an $E$-valued $q$-form on the $n$-dimensional $M$, losslessly.

Once one sees this, both directions are forced. Going up ($\Theta$): from a form $a$ on $M$, define $\hat a$ by pushing arguments down with $d\pi$, evaluating $a$, and reading the result back into $V$ with $\iota_p^{-1}$; this is automatically basic (because $d\pi$ annihilates vertical vectors) and automatically equivariant (because $\iota_{p\cdot g}=\iota_p\circ\rho(g)$ and $d\pi\circ dR_g=d\pi$). Going down ($\Lambda$): from a basic equivariant $\hat a$, define $a$ by lifting arguments arbitrarily and reading the value into $E_m$ with $\iota_p$; basic-ness makes the answer independent of *which* lift, and equivariance makes it independent of *which* frame $p$. The two recipes are visibly inverse because each is the other read through the isomorphism $\iota_p$.

---

# What Makes This Hard

The single genuinely subtle point is that the descent map $\Lambda$ is defined by *choices* — a point $p$ in the fibre and lifts $\hat v_j$ of the tangent vectors — and the whole theorem hinges on showing the answer is independent of both, using the two hypotheses in the right places: **basic-ness kills the dependence on the lift** (any two lifts differ by a vertical vector, which the basic form does not see), while **equivariance kills the dependence on the point $p$** (any two points in a fibre differ by a group element, and the twisting law relates the two values so that $\iota_p$ and $\iota_{p\cdot g}$ produce the same element of $E_m$). Confusing which hypothesis handles which choice — or forgetting that there are two independent choices — is the standard error. The second trap is the coefficient bookkeeping: in the nontrivial-representation case $\hat a$ is genuinely a $V$-valued form and $a$ genuinely an $E$-valued form, and one must resist the temptation (encouraged by the source's shorthand "$\pi^*a$") to treat $\hat a$ as a literal pullback, which only makes sense for the trivial representation.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Set up the two maps $\Theta$ (up) and $\Lambda$ (down) by the frame-and-lift recipes. For $\Theta$, check the output is a well-defined $V$-valued form and that it is basic, equivariant, and smooth. For $\Lambda$, check the recipe does not depend on the two choices (lift, then point), and that the output is smooth. Finally check $\Theta$ and $\Lambda$ are mutually inverse and $C^\infty(M)$-linear, and specialise to the trivial representation. Every step is a one-line consequence of exactly one of: "$\iota_p$ is a linear iso with $\iota_{p\cdot g}=\iota_p\circ\rho(g)$", "$V_p=\ker d\pi_p$", "$d\pi\circ dR_g=d\pi$".

**Subgoal decomposition:**

1. **$\Theta$ produces a well-defined $V$-valued form.** For $a\in\Omega^q(M;E)$ and $p\in P$, define $\hat a_p:=\iota_p^{-1}\circ a_{\pi(p)}\circ(d\pi_p\times\cdots\times d\pi_p)$.
   - *Hint:* $\iota_p$ is a linear isomorphism, so $\iota_p^{-1}$ exists; composition of alternating multilinear maps with linear maps is alternating multilinear.
   - *Why needed:* Without knowing $\hat a_p$ is an honest element of $\Lambda^q T_p^*P\otimes V$, nothing downstream is defined.

2. **$\hat a$ is basic.** Show $\hat a_p(\hat v_1,\dots,\hat v_q)=0$ when some $\hat v_j$ is vertical.
   - *Hint:* $V_p=\ker d\pi_p$, so $d\pi_p\hat v_j=0$; then $a_{\pi(p)}(\dots,0,\dots)=0$ by multilinearity, and $\iota_p^{-1}(0)=0$.
   - *Why needed:* Membership of the target space $\Omega^q_{\mathrm{bas}}(P;V)^G$ requires it.

3. **$\hat a$ is $G$-equivariant of type $\rho$.** Show $R_g^*\hat a=\rho(g^{-1})\hat a$.
   - *Hint:* Apply $[\cdot,\cdot]$ at $p\cdot g$, use $d\pi_{p\cdot g}\circ dR_g=d\pi_p$ to collapse to the same value $a_m$, then use $[p\cdot g,w]=[p,\rho(g)w]$ and injectivity of $\iota_p$.
   - *Why needed:* The other half of membership in the target.

4. **$\hat a$ is smooth.** Show $\hat a$ is smooth near every point.
   - *Hint:* Over a trivialising $U$ with section $s$, write $p=s(\pi(p))\cdot g(p)$ with $g$ smooth; derive $\hat a=\rho(g^{-1})\,\pi^*(a^s)$ where $a^s$ is $a$ read in the trivialisation.
   - *Why needed:* Elements of $\Omega^q(P;V)$ are by definition smooth.

5. **$\Lambda$ is independent of the lift.** With $p$ fixed, two lifts of the $v_j$ give the same value.
   - *Hint:* Two lifts differ by a vertical vector; expand by multilinearity; every term with a vertical argument dies because $\hat a$ is basic.
   - *Why needed:* Otherwise $(\ast\ast)$ is not a function.

6. **$\Lambda$ is independent of the point $p$ in the fibre.** Two frames $p,p\cdot g$ give the same value.
   - *Hint:* Transport lifts by $dR_g$; use equivariance to relate $\hat a_{p\cdot g}(dR_g\hat v)$ to $\rho(g^{-1})\hat a_p(\hat v)$; then $[p\cdot g,\rho(g^{-1})w]=[p,w]$.
   - *Why needed:* Otherwise $(\ast\ast)$ is not a function.

7. **$\Lambda$ is smooth, and $\Theta,\Lambda$ are mutually inverse and $C^\infty(M)$-linear.** Read $a$ in a section $s$ as $\iota_{s(\cdot)}\circ s^*\hat a$; compose the two recipes; track $\pi^*f$.
   - *Hint:* $\Lambda(\Theta a)=a$ and $\Theta(\Lambda\hat a)=\hat a$ each follow from $(\ast)$ and $(\ast\ast)$ and injectivity of $\iota_p$ in one line.
   - *Why needed:* Bijectivity and the module statement are the theorem's conclusion.

---

# Lemma Decomposition

> [!note]- Lemma 1: the frame isomorphism and its transformation law
> **Statement:** For each $p\in P$ the map $\iota_p\colon V\to E_{\pi(p)}$, $\iota_p(v)=[p,v]$, is a linear isomorphism, and for every $g\in G$,
> $$\iota_{p\cdot g}=\iota_p\circ\rho(g),\qquad\text{i.e.}\qquad [p\cdot g,\,v]=[p,\,\rho(g)\,v],\qquad\text{equivalently}\qquad [p\cdot g,\,\rho(g^{-1})v]=[p,v].$$
>
> **Hint:** Surjectivity uses transitivity on fibres, injectivity uses freeness; the law is the definition of the equivalence relation on $P\times V$.
>
> **Why needed:** $\iota_p$ and $\iota_p^{-1}$ are the coefficient translators in both $(\ast)$ and $(\ast\ast)$; the transformation law is what carries equivariance across the descent.
>
> > [!note]- Full proof
> > This is established in full on [[Def - Associated Bundle|the associated-bundle page]] (Clause 1 of the definition); we restate the argument for self-containedness.
> >
> > **$\iota_p$ is surjective.** Let $[q,w]\in E_{\pi(p)}$, so $\pi(q)=\pi(p)$, meaning $q$ lies in the fibre $P_{\pi(p)}$. Since $G$ acts **transitively** on that fibre (defining property of a principal bundle), there is $g\in G$ with $q=p\cdot g$. Then
> > $$[q,w]=[p\cdot g,\,w]=[p,\,\rho(g)w]=\iota_p(\rho(g)w)\qquad(\text{frame-change law, proved just below}),$$
> > so $[q,w]\in\operatorname{im}\iota_p$; hence $\iota_p$ is onto $E_{\pi(p)}$.
> >
> > **$\iota_p$ is injective.** Suppose $[p,v]=[p,w]$. By definition of the quotient there is $g\in G$ with $(p,w)=(p,v)\cdot g=(p\cdot g,\rho(g^{-1})v)$. Comparing first components, $p=p\cdot g$, so $g=e$ by **freeness** of the $G$-action; comparing second components, $w=\rho(e^{-1})v=v$. Hence $\iota_p$ is injective. Being a bijection between the vector spaces $V$ and $E_{\pi(p)}$ that is linear for the vector-space structure transported from $V$ (that structure is defined on the associated-bundle page precisely so that $\iota_p$ is linear), $\iota_p$ is a linear isomorphism.
> >
> > **The frame-change law.** For $v\in V$ and $g\in G$, the two pairs $(p\cdot g,v)$ and $(p,\rho(g)v)$ satisfy
> > $$(p,\rho(g)v)\cdot g=\bigl(p\cdot g,\ \rho(g^{-1})\rho(g)v\bigr)=(p\cdot g,\ v)\qquad(\text{action on }P\times V;\ \rho(g^{-1})\rho(g)=\operatorname{id}),$$
> > so they lie in the same $G$-orbit, giving $[p\cdot g,v]=[p,\rho(g)v]$, i.e. $\iota_{p\cdot g}(v)=\iota_p(\rho(g)v)$, i.e. $\iota_{p\cdot g}=\iota_p\circ\rho(g)$. Replacing $v$ by $\rho(g^{-1})v$ gives $[p\cdot g,\rho(g^{-1})v]=[p,v]$. $\blacksquare$

> [!note]- Lemma 2: basic forms do not see vertical changes of argument
> **Statement:** Let $\omega\in\Omega^q(P;V)$ be basic, $p\in P$, and $\hat v_1,\dots,\hat v_q,\,\hat v_1',\dots,\hat v_q'\in T_pP$ with $\hat v_j'-\hat v_j\in V_p=\ker d\pi_p$ for each $j$. Then $\omega_p(\hat v_1,\dots,\hat v_q)=\omega_p(\hat v_1',\dots,\hat v_q')$. Consequently, if $\hat v_j$ and $\hat v_j'$ are two families of lifts of the same vectors $v_1,\dots,v_q\in T_{\pi(p)}M$ (that is $d\pi_p\hat v_j=v_j=d\pi_p\hat v_j'$), then $\omega_p(\hat v_1,\dots,\hat v_q)=\omega_p(\hat v_1',\dots,\hat v_q')$.
>
> **Hint:** Write $\hat v_j'=\hat v_j+u_j$ with $u_j$ vertical, expand $\omega_p$ multilinearly into $2^q$ terms, and use that any term with at least one vertical entry vanishes.
>
> **Why needed:** This is exactly the independence of $(\ast\ast)$ from the choice of lifts.
>
> > [!note]- Full proof
> > **Goal.** Show the value is unchanged, then read off the lift statement. Set $u_j:=\hat v_j'-\hat v_j$; by hypothesis $u_j\in V_p$ for each $j$.
> >
> > **Multilinear expansion.** Since $\omega_p$ is $\mathbb R$-multilinear in its $q$ arguments,
> > $$\omega_p(\hat v_1+u_1,\dots,\hat v_q+u_q)=\sum_{S\subseteq\{1,\dots,q\}}\omega_p(w_1^S,\dots,w_q^S),\qquad w_j^S=\begin{cases}u_j,& j\in S,\\ \hat v_j,& j\notin S,\end{cases}$$
> > the sum ranging over all $2^q$ subsets $S$ (multilinearity, applied slot by slot).
> >
> > **Kill every term with a vertical entry.** If $S\ne\varnothing$, the term $\omega_p(w_1^S,\dots,w_q^S)$ has at least one argument equal to some $u_j\in V_p$, hence vanishes because $\omega$ is **basic** (a basic form is zero whenever any argument is vertical). Therefore only the term $S=\varnothing$ survives:
> > $$\omega_p(\hat v_1',\dots,\hat v_q')=\omega_p(\hat v_1+u_1,\dots,\hat v_q+u_q)=\omega_p(\hat v_1,\dots,\hat v_q)\qquad(\text{only the all-}\hat v\text{ term is nonzero}).$$
> >
> > **The lift statement.** If $d\pi_p\hat v_j=v_j=d\pi_p\hat v_j'$ then $d\pi_p(\hat v_j'-\hat v_j)=v_j-v_j=0$, so $\hat v_j'-\hat v_j\in\ker d\pi_p=V_p$; the displayed equality then gives $\omega_p(\hat v_1,\dots,\hat v_q)=\omega_p(\hat v_1',\dots,\hat v_q')$. $\blacksquare$

> [!note]- Lemma 3: the projection differential is $G$-invariant, $d\pi_{p\cdot g}\circ dR_g=d\pi_p$
> **Statement:** For every $p\in P$ and $g\in G$, the differentials satisfy $d\pi_{p\cdot g}\circ d(R_g)_p=d\pi_p$ as linear maps $T_pP\to T_{\pi(p)}M$. In particular, if $\hat v\in T_pP$ lifts $v\in T_{\pi(p)}M$ (that is $d\pi_p\hat v=v$), then $d(R_g)_p\hat v\in T_{p\cdot g}P$ also lifts $v$.
>
> **Hint:** Differentiate the bundle identity $\pi\circ R_g=\pi$ at $p$ by the chain rule.
>
> **Why needed:** It transports lifts from a frame $p$ to a translated frame $p\cdot g$ (used for equivariance of $\Theta$ and for the point-independence of $\Lambda$).
>
> > [!note]- Full proof
> > **Goal.** Differentiate the $G$-invariance of $\pi$. A principal bundle satisfies $\pi(p\cdot g)=\pi(p)$ for all $p,g$; fixing $g$, this is the identity of smooth maps $\pi\circ R_g=\pi\colon P\to M$.
> >
> > **Chain rule.** Differentiating $\pi\circ R_g=\pi$ at the point $p$,
> > $$d\pi_{R_g(p)}\circ d(R_g)_p=d(\pi\circ R_g)_p=d\pi_p\qquad(\text{chain rule; then }\pi\circ R_g=\pi),$$
> > and $R_g(p)=p\cdot g$, giving $d\pi_{p\cdot g}\circ d(R_g)_p=d\pi_p$.
> >
> > **Lifts transport.** If $d\pi_p\hat v=v$ then $d\pi_{p\cdot g}\bigl(d(R_g)_p\hat v\bigr)=(d\pi_{p\cdot g}\circ d(R_g)_p)\hat v=d\pi_p\hat v=v$ (the identity just proved), so $d(R_g)_p\hat v$ lifts $v$ at $p\cdot g$. $\blacksquare$

> [!note]- Lemma 4: local formula for $\Theta$ and $\Lambda$ via a section
> **Statement:** Let $s\colon U\to P$ be a smooth local section over an open $U\subseteq M$ (these exist because $P$ is locally trivial), and let $g\colon\pi^{-1}(U)\to G$ be the smooth map defined by $p=s(\pi(p))\cdot g(p)$. Write $a^s\in\Omega^q(U;V)$ for the form representing $a\in\Omega^q(M;E)$ in the trivialisation induced by $s$, i.e. $a_m=\iota_{s(m)}\circ a^s_m$ (equivalently $a^s_m=\iota_{s(m)}^{-1}\circ a_m$). Then on $\pi^{-1}(U)$,
> $$\hat a=\rho(g^{-1})\,\pi^*(a^s)\qquad\text{(the map }\Theta\text{)},\qquad\text{and dually}\qquad (\Lambda\hat a)_m=\iota_{s(m)}\bigl((s^*\hat a)_m\bigr)\ \text{ for }m\in U\ \text{(the map }\Lambda\text{)}.$$
>
> **Hint:** Use $p=s(\pi(p))g(p)$ and Lemma 1 to move the frame from $p$ to $s(\pi(p))$; for $\Lambda$ take $p=s(m)$ and lifts $ds_m(v_j)$.
>
> **Why needed:** It exhibits $\hat a$ and $\Lambda\hat a$ as compositions of smooth maps, giving the smoothness clauses in both directions.
>
> > [!note]- Full proof
> > **Existence of $s$ and smoothness of $g$.** Because $P$ is a principal bundle it is locally trivial; over a trivialising $U$ a local trivialisation $\psi_U\colon\pi^{-1}(U)\to U\times G$ gives the local section $s:=\psi_U^{-1}(\cdot,e)$ and, for $p\in\pi^{-1}(U)$, writing $\psi_U(p)=(\pi(p),h(p))$ with $h$ smooth, one has $p=s(\pi(p))\cdot h(p)$, so $g:=h$ is smooth (this is the content of [[Def - Principal G-Bundle|local sections of principal bundles]]).
> >
> > **Formula for $\Theta$.** Fix $p\in\pi^{-1}(U)$, put $m:=\pi(p)$, and let $\hat v_1,\dots,\hat v_q\in T_pP$. By the defining relation $(\ast)$ and then $a_m=\iota_{s(m)}\circ a^s_m$,
> > $$\bigl[p,\hat a_p(\hat v_1,\dots,\hat v_q)\bigr]=a_m(d\pi_p\hat v_1,\dots,d\pi_p\hat v_q)=\bigl[s(m),\,a^s_m(d\pi_p\hat v_1,\dots,d\pi_p\hat v_q)\bigr]\qquad((\ast);\ a_m=\iota_{s(m)}\circ a^s_m).$$
> > Now $p=s(m)\cdot g(p)$, so by Lemma 1 the left side is $[s(m)\cdot g(p),\hat a_p(\dots)]=[s(m),\rho(g(p))\hat a_p(\dots)]$. Equating and applying the injective $\iota_{s(m)}^{-1}$,
> > $$\rho(g(p))\,\hat a_p(\hat v_1,\dots,\hat v_q)=a^s_m(d\pi_p\hat v_1,\dots,d\pi_p\hat v_q)=(\pi^*a^s)_p(\hat v_1,\dots,\hat v_q)\qquad(\text{injectivity of }\iota_{s(m)};\ \text{def. of }\pi^*),$$
> > hence $\hat a_p=\rho(g(p)^{-1})(\pi^*a^s)_p$, that is $\hat a=\rho(g^{-1})\,\pi^*(a^s)$ on $\pi^{-1}(U)$.
> >
> > **Formula for $\Lambda$.** Fix $m\in U$; take the frame $p:=s(m)$ and the lifts $\hat v_j:=ds_m(v_j)$, which are lifts because $d\pi_{s(m)}\circ ds_m=d(\pi\circ s)_m=d(\operatorname{id}_U)_m=\operatorname{id}$ gives $d\pi_{s(m)}(ds_m v_j)=v_j$. Then by $(\ast\ast)$,
> > $$(\Lambda\hat a)_m(v_1,\dots,v_q)=[s(m),\hat a_{s(m)}(ds_m v_1,\dots,ds_m v_q)]=\iota_{s(m)}\bigl((s^*\hat a)_m(v_1,\dots,v_q)\bigr)\qquad((\ast\ast);\ \text{def. of }s^*\text{ and }\iota_{s(m)}).$$
> > $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\pi\colon P\to M$ be a principal $G$-bundle, $\rho\colon G\to GL(V)$ a representation, $E=P\times_\rho V$, and $q\ge 0$. We must show: (I) $\Theta$ is well defined into $\Omega^q_{\mathrm{bas}}(P;V)^G$; (II) $\Lambda$ is well defined into $\Omega^q(M;E)$; (III) $\Theta$ and $\Lambda$ are mutually inverse; (IV) both are $C^\infty(M)$-linear; (V) the trivial-representation case. We use Lemmas 1–4 freely.
>
> **Step 0 — the pieces of the recipes are defined.** By Lemma 1, for each $p$ the map $\iota_p\colon V\to E_{\pi(p)}$ is a linear isomorphism, so $\iota_p^{-1}$ exists. By the vertical-subspace description ([[Def - Equivariant and Basic Forms on a Principal Bundle|equivariant and basic forms]]), $V_p=\ker d\pi_p$, and $d\pi_p\colon T_pP\to T_{\pi(p)}M$ is surjective because $\pi$ is a submersion, so lifts $\hat v_j$ with $d\pi_p\hat v_j=v_j$ exist for every $v_j\in T_{\pi(p)}M$. Both recipes therefore make sense pointwise; we must upgrade "pointwise" to "well-defined smooth form" in each direction.
>
> ---
> **Part I — $\Theta$ is well defined with values in $\Omega^q_{\mathrm{bas}}(P;V)^G$.**
>
> **I.0 — $\hat a$ is a $V$-valued $q$-form.** Fix $a\in\Omega^q(M;E)$ and $p\in P$. Define
> $$\hat a_p(\hat v_1,\dots,\hat v_q):=\iota_p^{-1}\bigl(a_{\pi(p)}(d\pi_p\hat v_1,\dots,d\pi_p\hat v_q)\bigr),\qquad \hat v_1,\dots,\hat v_q\in T_pP,$$
> which is the unique solution of $(\ast)$ because $\iota_p$ is bijective (Lemma 1). As a function of $(\hat v_1,\dots,\hat v_q)$ it is a composition $\iota_p^{-1}\circ a_{\pi(p)}\circ(d\pi_p\times\cdots\times d\pi_p)$: the map $a_{\pi(p)}$ is alternating $\mathbb R$-multilinear (it is the value of a $q$-form), $d\pi_p$ is linear, and $\iota_p^{-1}$ is linear, so $\hat a_p$ is alternating $\mathbb R$-multilinear, i.e. $\hat a_p\in\Lambda^q T_p^*P\otimes V$. Thus $\hat a$ is a (a priori not-yet-smooth) $V$-valued $q$-form on $P$.
>
> **I.1 — $\hat a$ is basic.** Suppose some argument $\hat v_j\in V_p=\ker d\pi_p$. Then $d\pi_p\hat v_j=0$, so
> $$a_{\pi(p)}(d\pi_p\hat v_1,\dots,\underbrace{d\pi_p\hat v_j}_{=0},\dots,d\pi_p\hat v_q)=0\qquad(\text{multilinearity of }a_{\pi(p)}\text{ in the }j\text{-th slot}),$$
> whence $\hat a_p(\hat v_1,\dots,\hat v_q)=\iota_p^{-1}(0)=0$ (linearity of $\iota_p^{-1}$). Hence $\hat a$ is basic.
>
> **I.2 — $\hat a$ is $G$-equivariant of type $\rho$.** Fix $g\in G$, $p\in P$, and $\hat v_1,\dots,\hat v_q\in T_pP$; write $m:=\pi(p)=\pi(p\cdot g)$. We compute $(R_g^*\hat a)_p=\hat a_{p\cdot g}\circ(dR_g\times\cdots\times dR_g)$ and compare with $\rho(g^{-1})\hat a_p$. Apply $\iota_{p\cdot g}=[\,p\cdot g,\,\cdot\,]$ to the value at $p\cdot g$:
> $$\bigl[p\cdot g,\ \hat a_{p\cdot g}(dR_g\hat v_1,\dots,dR_g\hat v_q)\bigr]=a_m\bigl(d\pi_{p\cdot g}dR_g\hat v_1,\dots,d\pi_{p\cdot g}dR_g\hat v_q\bigr)\qquad((\ast)\text{ at }p\cdot g)$$
> $$=a_m(d\pi_p\hat v_1,\dots,d\pi_p\hat v_q)\qquad(\text{Lemma 3: }d\pi_{p\cdot g}\circ dR_g=d\pi_p)$$
> $$=\bigl[p,\ \hat a_p(\hat v_1,\dots,\hat v_q)\bigr]\qquad((\ast)\text{ at }p).$$
> By Lemma 1, $[p,\,w]=[p\cdot g,\,\rho(g^{-1})w]$; applying this to the last line with $w=\hat a_p(\hat v_1,\dots,\hat v_q)$ gives
> $$\bigl[p\cdot g,\ \hat a_{p\cdot g}(dR_g\hat v_1,\dots,dR_g\hat v_q)\bigr]=\bigl[p\cdot g,\ \rho(g^{-1})\,\hat a_p(\hat v_1,\dots,\hat v_q)\bigr]\qquad(\text{combining the two displays and }[p,w]=[p\cdot g,\rho(g^{-1})w]).$$
> Both sides are $\iota_{p\cdot g}$ applied to a vector of $V$, and $\iota_{p\cdot g}$ is injective (Lemma 1), so
> $$\hat a_{p\cdot g}(dR_g\hat v_1,\dots,dR_g\hat v_q)=\rho(g^{-1})\,\hat a_p(\hat v_1,\dots,\hat v_q),\qquad\text{i.e.}\qquad R_g^*\hat a=\rho(g^{-1})\hat a.$$
> Hence $\hat a$ is $G$-equivariant of type $\rho$.
>
> **I.3 — $\hat a$ is smooth.** Smoothness is local, so fix a trivialising open $U\subseteq M$ with a smooth section $s\colon U\to P$ and the associated smooth $g\colon\pi^{-1}(U)\to G$ (Lemma 4). By Lemma 4, on $\pi^{-1}(U)$,
> $$\hat a=\rho(g^{-1})\,\pi^*(a^s),$$
> where $a^s\in\Omega^q(U;V)$ is smooth (it is $a$ read in the smooth trivialisation), $\pi^*(a^s)$ is smooth (pullback of a smooth form along the smooth map $\pi$), $g$ is smooth, and $\rho$ is smooth; the pointwise action $\rho(g^{-1})\cdot$ is a smooth bundle endomorphism. A pointwise-linear action of a smooth $GL(V)$-valued function on a smooth $V$-valued form is smooth, so $\hat a|_{\pi^{-1}(U)}$ is smooth. As the $\pi^{-1}(U)$ cover $P$, $\hat a\in\Omega^q(P;V)$.
>
> Combining I.0–I.3, $\hat a=\Theta(a)\in\Omega^q_{\mathrm{bas}}(P;V)^G$, so $\Theta$ is well defined.
>
> ---
> **Part II — $\Lambda$ is well defined with values in $\Omega^q(M;E)$.**
>
> Fix $\hat a\in\Omega^q_{\mathrm{bas}}(P;V)^G$, $m\in M$, and $v_1,\dots,v_q\in T_mM$. The recipe $(\ast\ast)$ chooses a point $p\in\pi^{-1}(m)$ and lifts $\hat v_j\in T_pP$ with $d\pi_p\hat v_j=v_j$, and returns $[p,\hat a_p(\hat v_1,\dots,\hat v_q)]$. We show this is independent of both choices.
>
> **II.1 — independence of the lifts (uses basic).** Fix $p\in\pi^{-1}(m)$ and let $\hat v_j,\hat v_j'$ be two families of lifts of $v_1,\dots,v_q$, so $d\pi_p\hat v_j=v_j=d\pi_p\hat v_j'$. Since $\hat a$ is basic, Lemma 2 gives
> $$\hat a_p(\hat v_1,\dots,\hat v_q)=\hat a_p(\hat v_1',\dots,\hat v_q')\qquad(\text{Lemma 2, }\hat a\text{ basic}),$$
> hence $[p,\hat a_p(\hat v_1,\dots,\hat v_q)]=[p,\hat a_p(\hat v_1',\dots,\hat v_q')]$. The value does not depend on the lifts.
>
> **II.2 — independence of the point $p$ in the fibre (uses equivariance).** Let $p'\in\pi^{-1}(m)$ be a second frame. By transitivity and freeness of the $G$-action on the fibre, $p'=p\cdot g$ for a unique $g\in G$. Given lifts $\hat v_j$ at $p$, put $\hat v_j':=d(R_g)_p\hat v_j\in T_{p\cdot g}P$; by Lemma 3 these are lifts of the $v_j$ at $p'=p\cdot g$. Because, by II.1, the value at $p'$ may be computed with *any* lifts, we use these. Then
> $$[p',\hat a_{p'}(\hat v_1',\dots,\hat v_q')]=[p\cdot g,\ \hat a_{p\cdot g}(dR_g\hat v_1,\dots,dR_g\hat v_q)]=[p\cdot g,\ \rho(g^{-1})\,\hat a_p(\hat v_1,\dots,\hat v_q)]\qquad(\text{equivariance }R_g^*\hat a=\rho(g^{-1})\hat a)$$
> $$=[p,\ \hat a_p(\hat v_1,\dots,\hat v_q)]\qquad(\text{Lemma 1: }[p\cdot g,\rho(g^{-1})w]=[p,w]).$$
> So the value computed at $p'$ equals the value computed at $p$. Since every frame in the fibre over $m$ is of the form $p\cdot g$, the value is independent of $p$. Together with II.1, $(\ast\ast)$ defines $a_m$ unambiguously.
>
> **II.3 — $a$ is an $E$-valued $q$-form and is smooth.** For fixed $p$ and lifts, $(v_1,\dots,v_q)\mapsto[p,\hat a_p(\hat v_1,\dots,\hat v_q)]$ is alternating $\mathbb R$-multilinear: given $v_j$ and $v_j'$ with common lifts summing appropriately, choose lifts additively (a linear splitting of $d\pi_p$ exists since $d\pi_p$ is onto), so the multilinearity and alternation of $\hat a_p$ and linearity of $\iota_p$ pass through; well-definedness (II.1–II.2) makes the choice immaterial. Hence $a_m\in\Lambda^q T_m^*M\otimes E_m$. For smoothness, work over a trivialising $U$ with section $s$; by Lemma 4,
> $$(\Lambda\hat a)_m=\iota_{s(m)}\bigl((s^*\hat a)_m\bigr)\qquad(m\in U),$$
> where $s^*\hat a\in\Omega^q(U;V)$ is smooth ($s$ and $\hat a$ smooth) and $m\mapsto\iota_{s(m)}$ is the smooth vector-bundle trivialisation $U\times V\xrightarrow{\sim}E|_U$ of the associated bundle. A smooth $V$-valued form composed with a smooth trivialisation is a smooth $E$-valued form, so $a|_U\in\Omega^q(U;E)$; as the $U$ cover $M$, $a=\Lambda(\hat a)\in\Omega^q(M;E)$. Thus $\Lambda$ is well defined.
>
> ---
> **Part III — $\Theta$ and $\Lambda$ are mutually inverse.**
>
> **III.1 — $\Lambda\circ\Theta=\operatorname{id}$.** Let $a\in\Omega^q(M;E)$ and $\hat a:=\Theta(a)$. Fix $m$, $v_1,\dots,v_q\in T_mM$, a frame $p\in\pi^{-1}(m)$, and lifts $\hat v_j$ with $d\pi_p\hat v_j=v_j$. Then
> $$(\Lambda\hat a)_m(v_1,\dots,v_q)=[p,\hat a_p(\hat v_1,\dots,\hat v_q)]=a_{\pi(p)}(d\pi_p\hat v_1,\dots,d\pi_p\hat v_q)=a_m(v_1,\dots,v_q)\qquad((\ast\ast);\ \text{then }(\ast);\ d\pi_p\hat v_j=v_j).$$
> Hence $\Lambda(\Theta(a))=a$.
>
> **III.2 — $\Theta\circ\Lambda=\operatorname{id}$.** Let $\hat a\in\Omega^q_{\mathrm{bas}}(P;V)^G$ and $a:=\Lambda(\hat a)$. Fix $p\in P$, put $m:=\pi(p)$, and let $\hat v_1,\dots,\hat v_q\in T_pP$. By $(\ast)$ applied to $a$, the form $\Theta(a)$ satisfies
> $$[p,\ \Theta(a)_p(\hat v_1,\dots,\hat v_q)]=a_m(d\pi_p\hat v_1,\dots,d\pi_p\hat v_q).$$
> Compute the right-hand side by $(\ast\ast)$, legitimately using the frame $p$ itself and the lifts $\hat v_j$ (which satisfy $d\pi_p\hat v_j=d\pi_p\hat v_j$):
> $$a_m(d\pi_p\hat v_1,\dots,d\pi_p\hat v_q)=[p,\hat a_p(\hat v_1,\dots,\hat v_q)]\qquad((\ast\ast)\text{ with this }p\text{ and these lifts}).$$
> Combining the two displays, $[p,\Theta(a)_p(\hat v_1,\dots,\hat v_q)]=[p,\hat a_p(\hat v_1,\dots,\hat v_q)]$; injectivity of $\iota_p$ (Lemma 1) yields $\Theta(a)_p=\hat a_p$ for every $p$, i.e. $\Theta(\Lambda(\hat a))=\hat a$.
>
> By III.1 and III.2, $\Theta$ is a bijection with inverse $\Lambda$.
>
> ---
> **Part IV — $C^\infty(M)$-linearity.** Both spaces are $C^\infty(M)$-modules: $\Omega^q(M;E)$ by pointwise multiplication $(f\cdot a)_m=f(m)a_m$, and $\Omega^q_{\mathrm{bas}}(P;V)^G$ by $f\cdot\omega:=(\pi^*f)\omega$ (this preserves the subspace: $\pi^*f$ is $G$-invariant, so $(\pi^*f)\omega$ is still equivariant of type $\rho$, and multiplying by a scalar function preserves basic-ness). $\Theta$ is $\mathbb R$-linear because $(\ast)$ is linear in $a$ and $\iota_p^{-1}$ is linear. For $f\in C^\infty(M)$ and $a\in\Omega^q(M;E)$,
> $$[p,\Theta(f a)_p(\hat v_1,\dots,\hat v_q)]=(f a)_{\pi(p)}(d\pi_p\hat v_1,\dots)=f(\pi(p))\,a_{\pi(p)}(d\pi_p\hat v_1,\dots)=f(\pi(p))\,[p,\Theta(a)_p(\hat v_1,\dots)]\qquad((\ast);\ (f a)_m=f(m)a_m;\ (\ast))$$
> $$=[p,\ (\pi^*f)(p)\,\Theta(a)_p(\hat v_1,\dots)]\qquad(\text{linearity of }\iota_p;\ (\pi^*f)(p)=f(\pi(p))),$$
> so by injectivity of $\iota_p$, $\Theta(f a)=(\pi^*f)\,\Theta(a)=f\cdot\Theta(a)$. Thus $\Theta$ is a $C^\infty(M)$-module homomorphism, and being bijective with inverse $\Lambda$, it is a $C^\infty(M)$-module isomorphism (a bijective module homomorphism has a module-homomorphism inverse, by the same argument as for the group case).
>
> ---
> **Part V — the trivial-representation case.** Suppose $\rho(g)=\operatorname{id}_V$ for all $g$. Then the associated-bundle action is $(p,v)\cdot g=(p\cdot g,v)$, so $[p,v]=[p',v]$ whenever $\pi(p)=\pi(p')$ (any two frames over $m$ differ by a $g$, and $[p\cdot g,v]=[p,\rho(g)v]=[p,v]$ by Lemma 1 with $\rho(g)=\operatorname{id}$). Hence $E=P\times_\rho V\cong M\times V$ via $[p,v]\mapsto(\pi(p),v)$, and under this identification $\iota_p(v)=[p,v]=(\pi(p),v)$ is the canonical inclusion $V\hookrightarrow E_{\pi(p)}=\{\pi(p)\}\times V$, independent of $p$. Equation $(\ast)$ then reads
> $$\hat a_p(\hat v_1,\dots,\hat v_q)=a_{\pi(p)}(d\pi_p\hat v_1,\dots,d\pi_p\hat v_q)=(\pi^*a)_p(\hat v_1,\dots,\hat v_q)\qquad(\iota_p=\text{canonical};\ \text{def. of }\pi^*),$$
> i.e. $\Theta(a)=\pi^*a$ literally. Equivariance $R_g^*\omega=\rho(g^{-1})\omega$ becomes invariance $R_g^*\omega=\omega$; so by Parts I–III, $\pi^*\colon\Omega^q(M;V)\to\Omega^q_{\mathrm{bas}}(P;V)^G$ is a bijection onto the basic invariant $V$-valued $q$-forms. Taking $V=\mathbb R$ gives $\pi^*\colon\Omega^q(M)\xrightarrow{\sim}\Omega^q_{\mathrm{bas}}(P)^G$.
>
> Combining Parts I–V, $\Theta$ is a $C^\infty(M)$-module isomorphism $\Omega^q(M;E)\xrightarrow{\sim}\Omega^q_{\mathrm{bas}}(P;V)^G$ with inverse $\Lambda$, and reduces to $a\mapsto\pi^*a$ for the trivial representation. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Descending the curvature (Riemannian and gauge geometry).** Take $P=\operatorname{Fr}(E)$ the frame bundle of a vector bundle with a linear connection, or any principal $G$-bundle with a connection $\omega$. Show that the curvature $\Omega=d\omega+\tfrac12[\omega\wedge\omega]\in\Omega^2(P;\mathfrak g)$ is basic and $\operatorname{Ad}$-equivariant, then apply this theorem (with $\rho=\operatorname{Ad}$, $V=\mathfrak g$, $E=\operatorname{ad}P$) to obtain the base curvature $F_\omega\in\Omega^2(M;\operatorname{ad}P)$. The application is non-obvious because $\omega$ itself is not in the domain — it fails to be basic — yet the specific combination that is the curvature lands squarely in it; recognising *which* forms built from a connection are basic is the whole exercise.

**Chern–Weil descent (algebraic topology of bundles).** Let $p$ be a degree-$d$ $\operatorname{Ad}$-invariant polynomial on $\mathfrak g$. Show that $p(\Omega)\in\Omega^{2d}(P)$ is basic (its entries are those of the basic $\Omega$) and $G$-invariant (invariance of $p$), and use the trivial-representation case to descend it to $p(F_\omega)\in\Omega^{2d}(M)$. This is the mechanism by which characteristic forms are defined on the base; the non-obvious point is that a *nonlinear* invariant of a basic equivariant form is again basic and invariant, so the theorem applies even though $p$ is not linear.

**The affine structure of the space of connections (infinite-dimensional geometry).** Given two connections $\omega,\omega'$ on $P$, show their difference $b=\omega-\omega'$ is basic and $\operatorname{Ad}$-equivariant, and apply this theorem to identify $b$ with an element of $\Omega^1(M;\operatorname{ad}P)$. Conclude that $\mathcal A(P)$ is an affine space modelled on $\Omega^1(M;\operatorname{ad}P)$ — the fact that underlies the entire variational theory of gauge fields. It is non-obvious because a single connection is emphatically *not* a tensorial object on $M$; only differences are, and this theorem is what makes that precise.

---

# Bridges

- **[[Thm - Sections of an Associated Bundle are Equivariant Functions|Sections of an associated bundle are equivariant functions]]** — this theorem is the degree-$q\ge 1$ continuation of that degree-$0$ statement. There, $\Omega^0_{\mathrm{bas}}(P;V)^G=C^\infty(P;V)^G$ (basic is vacuous for a $0$-form) and $\Omega^0(M;E)=\Gamma(E)$, and the correspondence $\hat s\mapsto s$ with $s(\pi(p))=[p,\hat s(p)]$ is exactly $(\ast\ast)$ with $q=0$. The two together say that the entire complex $\Omega^\bullet(M;E)$ is the basic equivariant part of $\Omega^\bullet(P;V)$.

- **[[Def - Adjoint Bundles ad P and Ad P|The adjoint bundle ad P]]** — the most-used instance takes $\rho=\operatorname{Ad}$, $V=\mathfrak g$, so $E=\operatorname{ad}P=P\times_{\operatorname{Ad}}\mathfrak g$. Under this specialisation the theorem reads $\Omega^q(M;\operatorname{ad}P)\cong\Omega^q_{\mathrm{bas}}(P;\mathfrak g)^{G}$ with $\operatorname{Ad}$-equivariance, which is the exact form in which the curvature $F_\omega$, the difference of connections, and the covariant exterior derivative $d^\omega$ are handled in chapter IV.

- **Curvature of a principal connection (chapter IV).** The curvature is *defined* by descending $d\omega+\tfrac12[\omega\wedge\omega]$: one proves that $2$-form on $P$ is basic and $\operatorname{Ad}$-equivariant, and then $F_\omega:=\Lambda(d\omega+\tfrac12[\omega\wedge\omega])\in\Omega^2(M;\operatorname{ad}P)$ by this theorem. The Bianchi identity $d^\omega F_\omega=0$ is likewise a downstairs shadow of the elementary upstairs identity $d(d\omega+\tfrac12[\omega\wedge\omega])$ contracted appropriately.

- **Chern–Weil theory (chapter VI).** The trivial-representation case, $\pi^*\colon\Omega^{2d}(M)\xrightarrow{\sim}\Omega^{2d}_{\mathrm{bas}}(P)^G$, is what allows an $\operatorname{Ad}$-invariant polynomial in the curvature, built on $P$, to be regarded as a closed form on $M$ whose de Rham class is a characteristic class; this theorem supplies the descent, and closedness plus connection-independence are proved on top of it.

- **The canonical trivialisation of $\pi^*E$.** The identity $(\ast)$ says $\hat a$ is the pullback $\pi^*a$ read through the canonical isomorphism $\pi^*E\cong P\times V$, $(p,e)\mapsto(p,\iota_p^{-1}e)$. This is the precise sense of Kobayashi–Nomizu's "tensorial forms of type $(\rho,V)$": a basic equivariant $V$-valued form on $P$ is the coordinate expression, in the tautological frame provided by $P$ itself, of a bundle-valued form on $M$.

---

# Unlocked by This

> [!tip] Tensorial forms *(from the theory of connections, Kobayashi–Nomizu)*
> The space $\Omega^q_{\mathrm{bas}}(P;V)^G$ is classically called the space of **tensorial $q$-forms of type $(\rho,V)$** on $P$. This theorem is the statement that tensorial forms on the total space are the same as bundle-valued forms on the base — the identification under which all covariant calculus on associated bundles is carried out. See **Kobayashi–Nomizu, *Foundations of Differential Geometry* I, Ch. II §5**.

> [!tip] Basic differential forms and equivariant cohomology *(from the theory of group actions)*
> For the trivial representation, $\Omega^\bullet_{\mathrm{bas}}(P)^G\cong\Omega^\bullet(M)$ identifies the basic subcomplex of a free action's total space with the de Rham complex of the quotient; this is the geometric seed of the Cartan model of equivariant cohomology, where basic forms in the Weil algebra play the role of forms on the (possibly singular) quotient. See **Def - de Rham Cohomology** and the Chern–Weil chapter.
