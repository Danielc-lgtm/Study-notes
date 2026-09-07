---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Fundamental Vector Field of a Group Action"
  - "Thm - The Space of Vector Fields is a Lie Algebra under the Lie Bracket"
  - "Thm - Ad is a Smooth Representation and its Differential is ad"
  - "Def - Left and Right Translations and Conjugation on a Lie Group"
  - "Def - Left-Invariant Vector Field"
  - "Thm - Naturality of the Exponential Map"
  - "Thm - The Exponential Map is a Local Diffeomorphism at the Origin"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $G$ is a Lie group with Lie algebra $\mathfrak{g}=T_eG$ and identity $e$, and $M$ is a smooth manifold. The series convention is that $\mathfrak{g}$ carries the bracket of left-invariant vector fields: for $\xi\in\mathfrak{g}$ let $\xi^{L}\in\mathfrak{X}(G)$ be the unique **[[Def - Left-Invariant Vector Field|left-invariant vector field]]** with $\xi^{L}(e)=\xi$, given by $\xi^{L}(g)=d_eL_g(\xi)$ where $L_g\colon G\to G$, $L_g(h)=gh$, is left translation; the bracket on $\mathfrak{g}$ is then defined by $[\xi,\eta]:=[\xi^{L},\eta^{L}](e)$, and $[\xi,\eta]^{L}=[\xi^{L},\eta^{L}]$ because the left-invariant fields are closed under the Lie bracket. We also use right translation $\rho_g\colon G\to G$, $\rho_g(h)=hg$; the associated **right-invariant vector field** of $X\in\mathfrak{g}$ is $X^{R}(g):=d_e\rho_g(X)$, with $X^{R}(e)=X$. Conjugation is $\alpha_g\colon G\to G$, $\alpha_g(h)=ghg^{-1}$, and inversion is $\nu\colon G\to G$, $\nu(g)=g^{-1}$. All of this notation is fixed on **[[Def - Left and Right Translations and Conjugation on a Lie Group]]**.

The exponential map $\exp\colon\mathfrak{g}\to G$ satisfies $\tfrac{d}{dt}\big|_0\exp(t\xi)=\xi$ and $\exp(0)=e$. The adjoint representation is $\operatorname{Ad}\colon G\to GL(\mathfrak{g})$, $\operatorname{Ad}_g=d_e\alpha_g$; for a matrix group $\operatorname{Ad}_gX=gXg^{-1}$, so $\operatorname{Ad}_{g^{-1}}X=g^{-1}Xg$. The space of smooth vector fields on $M$ is $\mathfrak{X}(M)$, and $[\cdot,\cdot]$ denotes the Lie bracket of vector fields, $[V,W]f=V(Wf)-W(Vf)$ for $f\in C^\infty(M)$.

A **right action** of $G$ on $M$ is a smooth map $M\times G\to M$, $(p,g)\mapsto p\cdot g$, with $p\cdot e=p$ and $(p\cdot g)\cdot h=p\cdot(gh)$; we write $R_g\colon M\to M$, $R_g(p)=p\cdot g$, for the diffeomorphism "act by $g$", and $r_p\colon G\to M$, $r_p(g)=p\cdot g$, for the orbit map through $p$. A **left action** is a smooth map $G\times M\to M$, $(g,p)\mapsto g\cdot p$, with $e\cdot p=p$ and $g\cdot(h\cdot p)=(gh)\cdot p$; we write $\theta_g\colon M\to M$, $\theta_g(p)=g\cdot p$, and $\ell_p\colon G\to M$, $\ell_p(g)=g\cdot p$, for the orbit map.

The **[[Def - Fundamental Vector Field of a Group Action|fundamental vector field]]** of $\xi\in\mathfrak{g}$ is, for a right action,
$$\xi_M(p):=d_e r_p(\xi)=\frac{d}{dt}\Big|_{t=0}p\cdot\exp(t\xi)\in T_pM,$$
and, for a left action,
$$\bar{X}(p):=d_e\ell_p(X)=\frac{d}{dt}\Big|_{t=0}\exp(tX)\cdot p\in T_pM.$$
Both are smooth vector fields on $M$; this is proved on the definition page. (On that page the right fundamental field is written $\xi_P$, following Haydys' $K_\xi$; here we write $\xi_M$ to keep the target manifold $M$ visible in the homomorphism $\mathfrak{g}\to\mathfrak{X}(M)$.)

> [!warning] Convention: which side, and whose symbol
> Bär (Definition 1.5.16, Remark 1.5.17) works with a **left** action, writes the orbit map as $R_p(g)=g\cdot p$ and the fundamental field as $\bar X$, and asserts that $X\mapsto\bar X$ is *the* Lie algebra homomorphism corresponding to $G\to\operatorname{Diff}(M)$. With the standard bracket conventions of this series that assignment is in fact a Lie algebra **anti**-homomorphism; the theorem below states and proves both facts and reconciles them. The series therefore lets $G$ act on principal bundles on the **right**, precisely so that $\xi\mapsto\xi_M$ is an honest homomorphism, which is what makes the local connection and curvature formulas of chapters IV–VI come out with their standard signs. Haydys writes $K_\xi$ for $\xi_M$ and writes "$(R_g)_*K_\xi=K_{\operatorname{ad}_{g^{-1}}\xi}$" (Theorem 46), using the symbol $\operatorname{ad}_g$ for what this series calls the **group** adjoint $\operatorname{Ad}_g$; part (iii) below is that identity with the series' notation.

---

# Statement

> **Theorem (fundamental vector fields and the Lie algebra).** Let $G$ be a Lie group with Lie algebra $\mathfrak{g}$.
>
> **(i) Right actions.** For a smooth right action of $G$ on $M$, the fundamental-vector-field map
> $$\mathfrak{g}\longrightarrow\mathfrak{X}(M),\qquad \xi\longmapsto\xi_M,$$
> is a **Lie algebra homomorphism**: it is linear and
> $$[\xi,\eta]_M=[\xi_M,\eta_M]\qquad\text{for all }\xi,\eta\in\mathfrak{g}.$$
>
> **(ii) Left actions.** For a smooth left action of $G$ on $M$, the map $X\mapsto\bar X$ is linear and is a Lie algebra **anti-homomorphism**:
> $$[\bar X,\bar Y]=-\,\overline{[X,Y]}\qquad\text{for all }X,Y\in\mathfrak{g}.$$
>
> **(iii) Equivariance under the action.** For a right action, the fundamental fields are permuted by the group according to the adjoint representation: for every $g\in G$,
> $$(R_g)_*\,\xi_M=(\operatorname{Ad}_{g^{-1}}\xi)_M,\qquad\text{equivalently}\qquad d_pR_g\big(\xi_M(p)\big)=(\operatorname{Ad}_{g^{-1}}\xi)_M(p\cdot g)\ \ \text{for all }p\in M.$$

The three parts are logically independent statements about the same map; (i) and (ii) are two faces of one computation (which invariant fields on $G$ push forward to the fundamental fields), and (iii) is the infinitesimal shadow of the associativity of the action.

---

# Motivation

A group action is a global object: it tells you where every point of $M$ goes under every element of $G$. A fundamental vector field is its infinitesimal trace: $\xi_M(p)$ is the velocity at which $p$ begins to move when $G$ starts flowing along the one-parameter subgroup $\exp(t\xi)$. Passing from the action to its fundamental fields is the act of differentiating the action at the identity, and this theorem is the statement that this differentiation is *structure-preserving* in the strongest possible sense: the Lie-algebra structure of $\mathfrak{g}$ — its bracket — is carried faithfully onto the Lie-algebra structure of $\mathfrak{X}(M)$.

The importance is that essentially every appearance of a Lie algebra in gauge theory is *through its fundamental fields*. On a principal bundle $P\to M$ the vertical tangent space at $p$ is exactly $\{\xi_P(p):\xi\in\mathfrak{g}\}$, and a connection is a $\mathfrak{g}$-valued one-form $\omega$ that inverts the map $\xi\mapsto\xi_P$ on vertical vectors. The bracket $[\omega\wedge\omega]$ in the structure equation $\Omega=d\omega+\tfrac12[\omega\wedge\omega]$ is the $\mathfrak{g}$-bracket; that it agrees with the bracket of the corresponding vertical fields — the content of part (i) — is what makes the curvature a well-defined equivariant two-form and what makes the Bianchi identity hold. Part (iii) is the identity Bär uses silently when he checks $R_g^*\omega=\operatorname{Ad}_{g^{-1}}\omega$: a connection form must transform by $\operatorname{Ad}_{g^{-1}}$ under $R_g$ precisely because the fundamental fields it reproduces transform that way. So this small theorem is the hinge on which the equivariance conventions of the whole subject turn; getting the side (right, not left) and the sign ($\operatorname{Ad}_{g^{-1}}$, not $\operatorname{Ad}_g$) right here is what makes them come out right everywhere downstream.

---

# Sources and Targets

**Sources (Input Broadening).** The literal hypothesis of part (i) is only "a smooth right action". The skill is to recognise, in a problem that never mentions a group action, that one is present.

The first disguised source is **a manifold carrying a smooth flow, or a family of commuting flows, that one wishes to package as a group.** A single complete vector field $V$ generates a flow $\varphi_t$, which is a smooth right (or left) action of $(\mathbb{R},+)$; a $k$-tuple of commuting complete fields generates an $\mathbb{R}^k$-action. The bridge $B\Rightarrow A$ is that "$V$ is complete" upgrades the flow to a genuine global action, at which point $V$ *is* the fundamental field of the generator $1\in\mathbb{R}=\mathfrak{g}$, and the theorem says the abelian bracket $[1,1]=0$ forces $[V,V]=0$ — trivially true, but for two commuting fields $V,W$ generating an $\mathbb{R}^2$-action it says $[V,W]=0$ is *equivalent* to the flows commuting, recovering the standard flow-commutation criterion. *Example problem:* show that two complete vector fields whose flows commute are the fundamental fields of a torus or cylinder action, and read off $[V,W]=0$.

The second disguised source is **a homogeneous space or a matrix group acting by multiplication.** Whenever $M=G/H$ or $M$ is a sphere, projective space, or Grassmannian presented as an orbit, the transitive action is right-multiplication in disguise; its fundamental fields span each tangent space. The bridge is that a transitive action makes $p\mapsto\xi_M(p)$ surjective onto $T_pM$ as $\xi$ ranges over $\mathfrak{g}$, so a *basis* of $\mathfrak{g}$ gives a spanning set of fields whose brackets are computed once and for all by part (i) as the brackets in $\mathfrak{g}$. *Example problem:* compute the Lie brackets of the three rotational vector fields on $S^2$ by identifying them with the fundamental fields of the $SO(3)$-action and using $[\mathfrak{so}(3),\mathfrak{so}(3)]$.

The third disguised source is **a principal bundle and its vertical fields.** In chapters III–IV every $\xi\in\mathfrak{g}$ produces a vertical field $\xi_P$ on the total space $P$, and any computation with the vertical distribution — the definition of a connection, the curvature two-form, the covariant exterior derivative — is a computation with fundamental fields of the right $G$-action on $P$. The bridge is that "$P$ is a principal $G$-bundle" supplies a *free* right action, so $\xi\mapsto\xi_P(p)$ is injective and identifies $\mathfrak{g}$ with the vertical space; part (i) then transfers the $\mathfrak{g}$-bracket to the bracket of vertical fields. *Example problem:* verify that the vertical fields of a principal bundle are closed under the Lie bracket and that their bracket structure is $\mathfrak{g}$, a prerequisite for the structure equation.

**Targets (Output Amplification).** The bare conclusions become powerful when combined with one further ingredient.

Combine part (i) with **a chosen basis and structure constants of $\mathfrak{g}$.** If $\{\xi_a\}$ is a basis with $[\xi_a,\xi_b]=\sum_c c^{c}_{ab}\xi_c$, then part (i) gives $[(\xi_a)_M,(\xi_b)_M]=\sum_c c^{c}_{ab}(\xi_c)_M$ with the *same* structure constants $c^{c}_{ab}$. The payoff $E$ is that the possibly complicated bracket algebra of vector fields on $M$ is reduced to the finite table of numbers $c^{c}_{ab}$; this is what makes the Maurer–Cartan and structure equations finite-dimensional computations.

Combine part (iii) with **a $G$-invariant tensor on $M$**, or an $\operatorname{Ad}$-equivariant $\mathfrak{g}$-valued form. If a differential form $\alpha$ on the total space is horizontal and one asks how $R_g^*\alpha$ relates to $\alpha$, part (iii) forces the answer to involve $\operatorname{Ad}_{g^{-1}}$ whenever $\alpha$ is built to reproduce fundamental fields. The payoff is the transformation law $R_g^*\omega=\operatorname{Ad}_{g^{-1}}\omega$ for connection one-forms and $R_g^*\Omega=\operatorname{Ad}_{g^{-1}}\Omega$ for curvature — the equivariance that makes local gauge fields patch into a global object.

Combine part (i) with **an invariant inner product on $\mathfrak{g}$** (available when $G$ is compact). The homomorphism $\xi\mapsto\xi_M$ then transports the Killing-type form to a bracket-compatible pairing of vector fields, which is exactly the algebraic input to the Yang–Mills inner product $|F|^2$ and to Chern–Weil theory. The payoff is that $\operatorname{Ad}$-invariant polynomials in the curvature are closed forms, because the homomorphism property makes the relevant derivative a total bracket, which the invariance annihilates.

---

# Why Is It True

Strip away the formalism. A fundamental field is nothing but the image, under the orbit map $r_p\colon g\mapsto p\cdot g$, of a distinguished field on the group. Which field? The one whose flow, pushed through $r_p$, becomes the flow of $\xi_M$. The flow of $\xi_M$ moves $p$ to $p\cdot\exp(t\xi)$, that is, it applies right multiplication by $\exp(t\xi)$ inside the orbit. Inside the group itself, right multiplication by $\exp(t\xi)$ is the flow of the **left-invariant** field $\xi^{L}$ (left-invariant fields commute with left translations, so their flows are right translations). Therefore $\xi^{L}$ on $G$ and $\xi_M$ on $M$ are two views of the same infinitesimal motion, tied together by the orbit map: they are $r_p$-related.

> **The mechanism in one sentence:** the fundamental field $\xi_M$ is the $r_p$-image of the left-invariant field $\xi^{L}$, and because "being related by a map" is preserved by the Lie bracket, the bracket relation among the $\xi^{L}$ — which *is* the bracket of $\mathfrak{g}$ — is copied verbatim onto the brackets of the $\xi_M$.

That is the whole of part (i). The bracket on $\mathfrak{g}$ was *defined* through left-invariant fields, so the homomorphism is not a coincidence but an inheritance: $\xi\mapsto\xi^{L}$ is a bracket-preserving identification $\mathfrak{g}\cong\mathfrak{X}_L(G)$ of $\mathfrak{g}$ with the space $\mathfrak{X}_L(G)$ of left-invariant vector fields on $G$, by construction, and $\xi\mapsto\xi_M$ is that identification followed by the bracket-preserving operation "push forward along $r_p$".

The sign in part (ii) comes from the single asymmetry between left and right. For a *left* action the associativity $g\cdot(h\cdot p)=(gh)\cdot p$ makes the orbit map $\ell_p\colon g\mapsto g\cdot p$ intertwine with **right** translation on $G$: $\ell_p\circ\rho_g=\ell_{g\cdot p}$. So it is the **right-invariant** fields that push forward to the left fundamental fields. And the right-invariant fields carry the *opposite* bracket: $X\mapsto X^{R}$ is an anti-isomorphism $\mathfrak{g}\to\mathfrak{X}_R(G)$ onto the space $\mathfrak{X}_R(G)$ of right-invariant vector fields, because $X^{R}$ is the inversion-pushforward of $-X^{L}$ and inversion reverses the bracket. That single minus sign, inherited from $d_e\nu=-\operatorname{id}$, is the entire difference between (i) and (ii).

Part (iii) is the infinitesimal form of associativity. Flowing $p$ along $\exp(t\xi)$ and then acting by $g$ gives $p\cdot(\exp(t\xi)\,g)$; to read this as a flow *starting at* $p\cdot g$ we must slide $\exp(t\xi)$ to the right past $g$, and $\exp(t\xi)\,g=g\,\exp(t\operatorname{Ad}_{g^{-1}}\xi)$ because conjugating the exponential replaces the direction $\xi$ by $\operatorname{Ad}_{g^{-1}}\xi$. The direction of motion at the new base point is therefore not $\xi$ but $\operatorname{Ad}_{g^{-1}}\xi$; the appearance of $g^{-1}$ (rather than $g$) is dictated by the fact that we move $\exp(t\xi)$ from the *left* of $g$ to the *right* of $g$, which is conjugation by $g^{-1}$.

---

# What Makes This Hard

The single genuine obstacle is that the orbit map $r_p\colon G\to M$ is **not** a diffeomorphism — it is neither injective nor surjective in general — so the familiar "a diffeomorphism pushes brackets to brackets" is unavailable and one needs the more basic fact that the Lie bracket is natural under *any* smooth map, expressed through the notion of related vector fields (Lemma 1). A reader who tries to define a "pushforward $r_{p*}\xi^{L}$" and manipulate it as a field on $M$ will get stuck, because that pushforward is not a well-defined field; the correct statement is the pointwise relatedness $d_g r_p(\xi^{L}(g))=\xi_M(r_p(g))$, which holds for every $g$ even though $r_p$ collapses the stabiliser. The second common error is a sign error in part (ii): forgetting that left actions bring in right-invariant fields, or forgetting that the right-invariant assignment is an anti-homomorphism, silently converts the correct $-\overline{[X,Y]}$ into $+\overline{[X,Y]}$ and is exactly the slip in Bär's Remark 1.5.17.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Prove once that related fields have related brackets (a computation with the derivation characterisation of the bracket). Then show, for a right action, that the left-invariant field $\xi^{L}$ is $r_p$-related to $\xi_M$ for every $p$; feed this into the relatedness-of-brackets fact to get part (i). For a left action, redo the relatedness step and find that the *right*-invariant field appears, then supply the one algebraic fact that the right-invariant assignment reverses the bracket, giving part (ii). Part (iii) is a direct differentiation using $\exp(t\xi)g=g\exp(t\operatorname{Ad}_{g^{-1}}\xi)$.

**Subgoal decomposition:**

1. **Related fields, related brackets.** For a smooth $F\colon N\to M$: if $V_i$ is $F$-related to $W_i$ ($i=1,2$) then $[V_1,V_2]$ is $F$-related to $[W_1,W_2]$.
   - *Hint:* Use $V\ F\text{-related to }W\iff V(f\circ F)=(Wf)\circ F$ for all $f\in C^\infty(M)$; apply the definition of the bracket as a commutator of derivations.
   - *Why needed:* The orbit map is not a diffeomorphism, so this is the only available transport of brackets.

2. **Right-action relatedness.** For a right action, $\xi^{L}$ is $r_p$-related to $\xi_M$ for every $p\in M$: $d_g r_p(\xi^{L}(g))=\xi_M(p\cdot g)$.
   - *Hint:* $r_p\circ L_g=r_{p\cdot g}$ by associativity of the action; differentiate at $e$.
   - *Why needed:* It is the bridge that lets Lemma 1 transfer the bracket from $\mathfrak{X}_L(G)$ to $\mathfrak{X}(M)$.

3. **Assemble part (i).** From subgoals 1 and 2 conclude $[\xi_M,\eta_M]=[\xi,\eta]_M$, and check linearity.
   - *Hint:* $[\xi^{L},\eta^{L}]=[\xi,\eta]^{L}$; both $[\xi^{L},\eta^{L}]$ and its $r_p$-image are pinned down at $g=e$.
   - *Why needed:* This is the homomorphism statement itself.

4. **Left-action relatedness and the sign.** For a left action, $X^{R}$ (right-invariant) is $\ell_p$-related to $\bar X$; and $X\mapsto X^{R}$ reverses the bracket, $[X^{R},Y^{R}]=-[X,Y]^{R}$, giving $[\bar X,\bar Y]=-\overline{[X,Y]}$.
   - *Hint:* $\ell_p\circ\rho_g=\ell_{g\cdot p}$; and $X^{R}=-\nu_*(X^{L})$ with $d_e\nu=-\operatorname{id}$, so pushforward under the diffeomorphism $\nu$ reverses the bracket.
   - *Why needed:* It is part (ii) and locates the minus sign.

5. **Equivariance.** Differentiate $R_g(p\cdot\exp(t\xi))=(p\cdot g)\cdot\exp(t\operatorname{Ad}_{g^{-1}}\xi)$ at $t=0$.
   - *Hint:* $\exp(t\xi)g=g\exp(t\operatorname{Ad}_{g^{-1}}\xi)$ from conjugation-exponential naturality.
   - *Why needed:* It is part (iii), the source of the $\operatorname{Ad}_{g^{-1}}$ transformation law.

---

# Lemma Decomposition

> [!note]- Lemma 1: Related vector fields have related brackets
> **Statement:** Let $F\colon N\to M$ be a smooth map between manifolds, and suppose $V_i\in\mathfrak{X}(N)$ is $F$-related to $W_i\in\mathfrak{X}(M)$ for $i=1,2$, meaning $d_qF(V_i(q))=W_i(F(q))$ for every $q\in N$. Then $[V_1,V_2]$ is $F$-related to $[W_1,W_2]$: $d_qF\big([V_1,V_2](q)\big)=[W_1,W_2](F(q))$ for all $q\in N$.
>
> **Hint:** Translate $F$-relatedness into the functional identity $V(f\circ F)=(Wf)\circ F$ for all $f\in C^\infty(M)$, then expand the bracket as a commutator of derivations.
>
> **Why needed:** The orbit maps $r_p,\ell_p\colon G\to M$ are not diffeomorphisms, so the diffeomorphism-pushforward form of bracket naturality does not apply. This lemma is the general fact that does. It is Lee, *Introduction to Smooth Manifolds*, 2nd ed., Proposition 8.30.
>
> > [!note]- Full proof
> > We first record the functional characterisation of relatedness. Fix a smooth map $F\colon N\to M$, a field $V\in\mathfrak{X}(N)$, and $W\in\mathfrak{X}(M)$.
> >
> > **Claim.** $V$ is $F$-related to $W$ if and only if $V(f\circ F)=(Wf)\circ F$ for every $f\in C^\infty(M)$.
> >
> > *Proof of claim.* For any $q\in N$ and $f\in C^\infty(M)$, the chain rule gives, on evaluating the tangent vector $V(q)$ on the function $f\circ F$,
> > $$\big(V(f\circ F)\big)(q)=V(q)\,(f\circ F)=\big(d_qF(V(q))\big)f \qquad\text{(definition of the differential }d_qF\text{ acting on }f\text{),}$$
> > while
> > $$\big((Wf)\circ F\big)(q)=(Wf)(F(q))=W(F(q))\,f \qquad\text{(definition of the derivation }W\text{ at the point }F(q)\text{).}$$
> > Thus $V(f\circ F)=(Wf)\circ F$ holds for all $f$ if and only if $d_qF(V(q))\,f=W(F(q))\,f$ for all $f$ and all $q$, which — since a tangent vector is determined by its action on smooth functions — is exactly $d_qF(V(q))=W(F(q))$ for all $q$, i.e. $F$-relatedness. This proves the claim.
> >
> > **The bracket computation.** Assume $V_i$ is $F$-related to $W_i$ for $i=1,2$. Let $f\in C^\infty(M)$ be arbitrary. Using the claim for the pair $(V_2,W_2)$ on the function $f$,
> > $$V_2(f\circ F)=(W_2 f)\circ F \qquad\text{(claim applied to }V_2,W_2\text{).}$$
> > Now apply the claim for the pair $(V_1,W_1)$ to the function $W_2 f\in C^\infty(M)$:
> > $$V_1\big((W_2 f)\circ F\big)=\big(W_1(W_2 f)\big)\circ F \qquad\text{(claim applied to }V_1,W_1\text{, with test function }W_2 f\text{).}$$
> > Combining the two displayed lines,
> > $$V_1\big(V_2(f\circ F)\big)=V_1\big((W_2 f)\circ F\big)=\big(W_1 W_2 f\big)\circ F \qquad\text{(substituting the first line into the second).}$$
> > By the same argument with the roles of the indices $1$ and $2$ exchanged,
> > $$V_2\big(V_1(f\circ F)\big)=\big(W_2 W_1 f\big)\circ F.$$
> > Subtracting the last two displays and using the definition $[V_1,V_2]g=V_1(V_2 g)-V_2(V_1 g)$ of the Lie bracket as the commutator of the derivations $V_1,V_2$ (here $g=f\circ F$),
> > $$[V_1,V_2](f\circ F)=\big(W_1 W_2 f-W_2 W_1 f\big)\circ F=\big([W_1,W_2]f\big)\circ F \qquad\text{(definition of }[W_1,W_2]\text{ as the commutator of }W_1,W_2\text{).}$$
> > This is the functional characterisation of "$[V_1,V_2]$ is $F$-related to $[W_1,W_2]$" (the claim, read backwards), valid for all $f\in C^\infty(M)$. Therefore $[V_1,V_2]$ is $F$-related to $[W_1,W_2]$. $\blacksquare$

> [!note]- Lemma 2: For a right action, the left-invariant field is orbit-related to the fundamental field
> **Statement:** Let $G$ act smoothly on $M$ on the right, fix $p\in M$, and let $r_p\colon G\to M$, $r_p(g)=p\cdot g$, be the orbit map. For every $\xi\in\mathfrak{g}$ the left-invariant field $\xi^{L}$ is $r_p$-related to the fundamental field $\xi_M$:
> $$d_g r_p\big(\xi^{L}(g)\big)=\xi_M(p\cdot g)\qquad\text{for every }g\in G.$$
>
> **Hint:** The associativity axiom of the action gives $r_p\circ L_g=r_{p\cdot g}$; differentiate this identity of maps at $e$ and read off both sides.
>
> **Why needed:** It is the exact hypothesis of Lemma 1 that transfers the bracket of $\mathfrak{g}$ (carried by left-invariant fields) onto the bracket of fundamental fields.
>
> > [!note]- Full proof
> > Fix $p\in M$, $\xi\in\mathfrak{g}$, and $g\in G$.
> >
> > **Step 1 — the orbit maps compose by associativity.** For every $h\in G$,
> > $$(r_p\circ L_g)(h)=r_p(gh)=p\cdot(gh)=(p\cdot g)\cdot h=r_{p\cdot g}(h) \qquad\text{(definition of }r_p\text{ and }L_g\text{; associativity }(p\cdot g)\cdot h=p\cdot(gh)\text{ of the right action).}$$
> > Hence $r_p\circ L_g=r_{p\cdot g}$ as smooth maps $G\to M$.
> >
> > **Step 2 — differentiate at the identity.** Recall $\xi^{L}(g)=d_eL_g(\xi)$ (definition of the left-invariant field). Applying $d_g r_p$ and the chain rule,
> > $$d_g r_p\big(\xi^{L}(g)\big)=d_g r_p\big(d_eL_g(\xi)\big)=d_e\big(r_p\circ L_g\big)(\xi) \qquad\text{(chain rule }d_g r_p\circ d_eL_g=d_e(r_p\circ L_g)\text{).}$$
> > By Step 1, $r_p\circ L_g=r_{p\cdot g}$, so
> > $$d_e\big(r_p\circ L_g\big)(\xi)=d_e r_{p\cdot g}(\xi)=\xi_M(p\cdot g) \qquad\text{(Step 1; definition }\xi_M(q)=d_e r_q(\xi)\text{ with }q=p\cdot g\text{).}$$
> > Combining the two displays gives $d_g r_p\big(\xi^{L}(g)\big)=\xi_M(p\cdot g)=\xi_M(r_p(g))$, which is precisely the statement that $\xi^{L}$ is $r_p$-related to $\xi_M$. $\blacksquare$

> [!note]- Lemma 3: For a left action, the right-invariant field is orbit-related to the fundamental field
> **Statement:** Let $G$ act smoothly on $M$ on the left, fix $p\in M$, and let $\ell_p\colon G\to M$, $\ell_p(g)=g\cdot p$, be the orbit map. For every $X\in\mathfrak{g}$ the right-invariant field $X^{R}$ (with $X^{R}(g)=d_e\rho_g(X)$, $\rho_g(h)=hg$) is $\ell_p$-related to the fundamental field $\bar X$:
> $$d_g \ell_p\big(X^{R}(g)\big)=\bar X(g\cdot p)\qquad\text{for every }g\in G.$$
>
> **Hint:** Now associativity gives $\ell_p\circ\rho_g=\ell_{g\cdot p}$; differentiate at $e$.
>
> **Why needed:** It shows that for a left action it is the *right*-invariant fields, not the left-invariant ones, that push to the fundamental fields — the structural fact that produces the sign in part (ii).
>
> > [!note]- Full proof
> > Fix $p\in M$, $X\in\mathfrak{g}$, $g\in G$.
> >
> > **Step 1 — orbit maps compose with right translation.** For every $h\in G$,
> > $$(\ell_p\circ\rho_g)(h)=\ell_p(hg)=(hg)\cdot p=h\cdot(g\cdot p)=\ell_{g\cdot p}(h) \qquad\text{(definition of }\ell_p,\rho_g\text{; associativity }(hg)\cdot p=h\cdot(g\cdot p)\text{ of the left action).}$$
> > Hence $\ell_p\circ\rho_g=\ell_{g\cdot p}$.
> >
> > **Step 2 — differentiate at the identity.** Using $X^{R}(g)=d_e\rho_g(X)$,
> > $$d_g\ell_p\big(X^{R}(g)\big)=d_g\ell_p\big(d_e\rho_g(X)\big)=d_e\big(\ell_p\circ\rho_g\big)(X)=d_e\ell_{g\cdot p}(X)=\bar X(g\cdot p) \qquad\text{(chain rule; Step 1; definition }\bar X(q)=d_e\ell_q(X)\text{).}$$
> > This is $\ell_p$-relatedness of $X^{R}$ and $\bar X$. $\blacksquare$

> [!note]- Lemma 4: The right-invariant assignment reverses the bracket
> **Statement:** The map $\mathfrak{g}\to\mathfrak{X}(G)$, $X\mapsto X^{R}$, sending $X$ to the right-invariant field with $X^{R}(e)=X$, is linear and satisfies
> $$[X^{R},Y^{R}]=-\,[X,Y]^{R}\qquad\text{for all }X,Y\in\mathfrak{g};$$
> equivalently, evaluating at $e$, $[X^{R},Y^{R}](e)=-[X,Y]$. Here $[X,Y]=[X^{L},Y^{L}](e)$ is the Lie algebra bracket, defined through left-invariant fields.
>
> **Hint:** Push a left-invariant field forward through inversion $\nu(g)=g^{-1}$; use $d_e\nu=-\operatorname{id}_{\mathfrak{g}}$ and that a diffeomorphism preserves the bracket.
>
> **Why needed:** It is the algebraic origin of the minus sign in part (ii). Without it, Lemma 3 would give a homomorphism for left actions, which is false.
>
> > [!note]- Full proof
> > Linearity of $X\mapsto X^{R}$ is immediate: $X^{R}(g)=d_e\rho_g(X)$ is linear in $X$ because $d_e\rho_g$ is a linear map, so $(aX+bY)^{R}=aX^{R}+bY^{R}$.
> >
> > We use two imported facts, each proved on its own page and restated here.
> >
> > **Fact A (differential of inversion).** By **[[Thm - The Exponential Map is a Local Diffeomorphism at the Origin]]**, the inversion map $\nu\colon G\to G$, $\nu(g)=g^{-1}$, is a diffeomorphism with $d_e\nu=-\operatorname{id}_{\mathfrak{g}}$.
> >
> > **Fact B (a diffeomorphism preserves the bracket).** By **[[Thm - The Space of Vector Fields is a Lie Algebra under the Lie Bracket]]**, for a diffeomorphism $F\colon N\to N$ and fields $V,W\in\mathfrak{X}(N)$ one has $F_*[V,W]=[F_*V,F_*W]$, where $(F_*V)(g)=d_{F^{-1}(g)}F\big(V(F^{-1}(g))\big)$.
> >
> > **Step 1 — inversion carries the left-invariant field of $X$ to the negative right-invariant field of $X$.** We claim $\nu_*(X^{L})=-X^{R}$. Since $\nu^{-1}=\nu$, the pushforward is
> > $$\big(\nu_*X^{L}\big)(g)=d_{g^{-1}}\nu\big(X^{L}(g^{-1})\big) \qquad\text{(definition of }F_*\text{ with }F=\nu,\ F^{-1}(g)=g^{-1}\text{).}$$
> > Now $X^{L}(g^{-1})=d_eL_{g^{-1}}(X)$ (definition of the left-invariant field). Consider the identity of maps $\nu\circ L_{g^{-1}}=\rho_g\circ\nu$, valid because for every $h\in G$
> > $$\big(\nu\circ L_{g^{-1}}\big)(h)=(g^{-1}h)^{-1}=h^{-1}g=\rho_g(h^{-1})=\big(\rho_g\circ\nu\big)(h) \qquad\text{(the anti-homomorphism property }(ab)^{-1}=b^{-1}a^{-1}\text{ of inversion).}$$
> > Differentiating $\nu\circ L_{g^{-1}}=\rho_g\circ\nu$ at $e$ (chain rule, and $\nu(e)=e$),
> > $$d_{g^{-1}}\nu\circ d_eL_{g^{-1}}=d_e\rho_g\circ d_e\nu=d_e\rho_g\circ(-\operatorname{id}_{\mathfrak{g}}) \qquad\text{(Fact A, }d_e\nu=-\operatorname{id}\text{).}$$
> > Applying both sides to $X$ and using $d_e\rho_g(X)=X^{R}(g)$,
> > $$d_{g^{-1}}\nu\big(d_eL_{g^{-1}}(X)\big)=d_e\rho_g(-X)=-X^{R}(g).$$
> > The left-hand side is $d_{g^{-1}}\nu\big(X^{L}(g^{-1})\big)=\big(\nu_*X^{L}\big)(g)$ by the first display of this step. Hence $\big(\nu_*X^{L}\big)(g)=-X^{R}(g)$ for all $g$, i.e. $\nu_*X^{L}=-X^{R}$, as claimed.
> >
> > **Step 2 — reverse the bracket.** Because the left-invariant fields are closed under the bracket with $[X^{L},Y^{L}]=[X,Y]^{L}$ (the series definition of the $\mathfrak{g}$-bracket), Fact B applied to the diffeomorphism $\nu$ gives
> > $$\nu_*[X^{L},Y^{L}]=[\nu_*X^{L},\nu_*Y^{L}] \qquad\text{(Fact B with }F=\nu\text{).}$$
> > Substituting $\nu_*X^{L}=-X^{R}$ and $\nu_*Y^{L}=-Y^{R}$ from Step 1 on the right, and $[X^{L},Y^{L}]=[X,Y]^{L}$ with $\nu_*[X,Y]^{L}=-[X,Y]^{R}$ (Step 1 applied to the element $[X,Y]\in\mathfrak{g}$) on the left,
> > $$-[X,Y]^{R}=[-X^{R},-Y^{R}]=[X^{R},Y^{R}] \qquad\text{(bilinearity of the bracket: the two minus signs cancel).}$$
> > Therefore $[X^{R},Y^{R}]=-[X,Y]^{R}$. Evaluating at $e$ and using $X^{R}(e)=X$, $[X,Y]^{R}(e)=[X,Y]$ gives $[X^{R},Y^{R}](e)=-[X,Y]$. $\blacksquare$

> [!note]- Lemma 5: Conjugation carries the exponential to the adjoint
> **Statement:** For every $g\in G$ and $\xi\in\mathfrak{g}$,
> $$\alpha_g\big(\exp(t\xi)\big)=g\exp(t\xi)g^{-1}=\exp\big(t\,\operatorname{Ad}_g\xi\big)\qquad\text{for all }t\in\mathbb{R},$$
> and consequently $\exp(t\xi)\,g=g\exp\big(t\,\operatorname{Ad}_{g^{-1}}\xi\big)$.
>
> **Hint:** $\alpha_g$ is a Lie group homomorphism (indeed automorphism) with $d_e\alpha_g=\operatorname{Ad}_g$; apply naturality of $\exp$ under homomorphisms.
>
> **Why needed:** It is the algebraic step in part (iii) that moves $\exp(t\xi)$ from the left of $g$ to the right, converting the direction $\xi$ into $\operatorname{Ad}_{g^{-1}}\xi$.
>
> > [!note]- Full proof
> > Fix $g\in G$. The conjugation $\alpha_g\colon G\to G$, $\alpha_g(h)=ghg^{-1}$, is a Lie group homomorphism (in fact an automorphism), and by definition $\operatorname{Ad}_g=d_e\alpha_g$; this is the definition of the adjoint representation restated from **[[Thm - Ad is a Smooth Representation and its Differential is ad]]**, which establishes that $\operatorname{Ad}\colon G\to GL(\mathfrak{g})$, $\operatorname{Ad}_g=d_e\alpha_g$, is a representation and, for a matrix group, $\operatorname{Ad}_g\xi=g\xi g^{-1}$.
> >
> > **Naturality of the exponential.** By **[[Thm - Naturality of the Exponential Map]]**, for any Lie group homomorphism $\varphi\colon G\to H$ the square
> > $$\varphi\circ\exp_G=\exp_H\circ\,d_e\varphi$$
> > commutes. Apply this with $\varphi=\alpha_g\colon G\to G$ and $d_e\alpha_g=\operatorname{Ad}_g$: for every $\zeta\in\mathfrak{g}$,
> > $$\alpha_g\big(\exp(\zeta)\big)=\exp\big(\operatorname{Ad}_g\zeta\big) \qquad\text{(naturality with }\varphi=\alpha_g,\ d_e\alpha_g=\operatorname{Ad}_g\text{).}$$
> > Taking $\zeta=t\xi$ gives $g\exp(t\xi)g^{-1}=\exp(t\,\operatorname{Ad}_g\xi)$, using that $\operatorname{Ad}_g$ is linear so $\operatorname{Ad}_g(t\xi)=t\operatorname{Ad}_g\xi$.
> >
> > **Consequence.** Replace $g$ by $g^{-1}$ in the identity just proved: $g^{-1}\exp(t\xi)g=\exp(t\,\operatorname{Ad}_{g^{-1}}\xi)$, using $(g^{-1})^{-1}=g$ and $\operatorname{Ad}_{g^{-1}}=d_e\alpha_{g^{-1}}$. Multiplying on the left by $g$ yields
> > $$\exp(t\xi)\,g=g\exp\big(t\,\operatorname{Ad}_{g^{-1}}\xi\big). \qquad\blacksquare$$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $G$ be a Lie group with Lie algebra $\mathfrak{g}=T_eG$, where the bracket $[\xi,\eta]:=[\xi^{L},\eta^{L}](e)$ is defined through left-invariant fields and $[\xi,\eta]^{L}=[\xi^{L},\eta^{L}]$.
>
> **Step 0 — the fundamental fields are genuine smooth fields.** For a right action, $\xi_M(p)=d_e r_p(\xi)$ is a well-defined smooth vector field on $M$, and likewise $\bar X$ for a left action; this is established on **[[Def - Fundamental Vector Field of a Group Action]]** (the field is $d\theta$ applied to the smooth field $(\xi,0)$ on $G\times M$). Thus each of $\xi_M,\bar X$ lies in $\mathfrak{X}(M)$, and the maps $\xi\mapsto\xi_M$, $X\mapsto\bar X$ are well-defined maps $\mathfrak{g}\to\mathfrak{X}(M)$. They are **linear**: $\xi_M(p)=d_e r_p(\xi)$ is linear in $\xi$ because $d_e r_p$ is a linear map, so $(a\xi+b\eta)_M=a\xi_M+b\eta_M$; the same argument with $\ell_p$ gives linearity of $X\mapsto\bar X$.
>
> **Part I — right actions give a homomorphism.** Fix $\xi,\eta\in\mathfrak{g}$ and a point $p\in M$; we show $[\xi_M,\eta_M](p)=[\xi,\eta]_M(p)$.
>
> By **Lemma 2**, the left-invariant field $\xi^{L}$ is $r_p$-related to $\xi_M$, and $\eta^{L}$ is $r_p$-related to $\eta_M$. By **Lemma 1** (related fields have related brackets, applied to $F=r_p$),
> $$[\xi^{L},\eta^{L}]\ \text{is}\ r_p\text{-related to}\ [\xi_M,\eta_M] \qquad\text{(Lemma 1 with }V_i=\xi^L,\eta^L,\ W_i=\xi_M,\eta_M\text{).}$$
> Writing out $r_p$-relatedness at the identity $g=e$, where $r_p(e)=p\cdot e=p$,
> $$d_e r_p\big([\xi^{L},\eta^{L}](e)\big)=[\xi_M,\eta_M]\big(r_p(e)\big)=[\xi_M,\eta_M](p) \qquad\text{(the relatedness identity }d_g r_p([\xi^L,\eta^L](g))=[\xi_M,\eta_M](r_p(g))\text{ at }g=e\text{).}$$
> On the left, $[\xi^{L},\eta^{L}](e)=[\xi,\eta]$ by the definition of the $\mathfrak{g}$-bracket, so
> $$d_e r_p\big([\xi,\eta]\big)=[\xi,\eta]_M(p) \qquad\text{(definition }\zeta_M(p)=d_e r_p(\zeta)\text{ with }\zeta=[\xi,\eta]\text{).}$$
> Combining the last two displays, $[\xi_M,\eta_M](p)=[\xi,\eta]_M(p)$. As $p\in M$ was arbitrary, $[\xi_M,\eta_M]=[\xi,\eta]_M$. Together with linearity (Step 0) this says $\xi\mapsto\xi_M$ is a Lie algebra homomorphism $\mathfrak{g}\to\mathfrak{X}(M)$. This proves **(i)**.
>
> **Part II — left actions give an anti-homomorphism.** Fix $X,Y\in\mathfrak{g}$ and $p\in M$; we show $[\bar X,\bar Y](p)=-\overline{[X,Y]}(p)$.
>
> By **Lemma 3**, the right-invariant field $X^{R}$ is $\ell_p$-related to $\bar X$, and $Y^{R}$ is $\ell_p$-related to $\bar Y$. By **Lemma 1** (with $F=\ell_p$),
> $$[X^{R},Y^{R}]\ \text{is}\ \ell_p\text{-related to}\ [\bar X,\bar Y] \qquad\text{(Lemma 1 with }V_i=X^R,Y^R,\ W_i=\bar X,\bar Y\text{).}$$
> Evaluating the relatedness identity at $g=e$, where $\ell_p(e)=e\cdot p=p$,
> $$d_e\ell_p\big([X^{R},Y^{R}](e)\big)=[\bar X,\bar Y]\big(\ell_p(e)\big)=[\bar X,\bar Y](p) \qquad\text{(relatedness }d_g\ell_p([X^R,Y^R](g))=[\bar X,\bar Y](\ell_p(g))\text{ at }g=e\text{).}$$
> By **Lemma 4**, $[X^{R},Y^{R}](e)=-[X,Y]$. Substituting,
> $$[\bar X,\bar Y](p)=d_e\ell_p\big(-[X,Y]\big)=-\,d_e\ell_p\big([X,Y]\big)=-\,\overline{[X,Y]}(p) \qquad\text{(linearity of }d_e\ell_p\text{; definition }\overline{[X,Y]}(p)=d_e\ell_p([X,Y])\text{).}$$
> As $p$ was arbitrary, $[\bar X,\bar Y]=-\overline{[X,Y]}$. Together with linearity (Step 0), $X\mapsto\bar X$ is a Lie algebra anti-homomorphism. This proves **(ii)**.
>
> **Part III — equivariance under the action.** Fix $g\in G$, $\xi\in\mathfrak{g}$, and $p\in M$; we compute $d_pR_g(\xi_M(p))$, where $R_g(q)=q\cdot g$ is the (diffeomorphism) action of $g$.
>
> **Differentiate through $R_g$.** Since $\xi_M(p)$ is the velocity at $t=0$ of the curve $t\mapsto p\cdot\exp(t\xi)$, and $R_g$ is smooth, the chain rule gives
> $$d_pR_g\big(\xi_M(p)\big)=\frac{d}{dt}\Big|_{0}R_g\big(p\cdot\exp(t\xi)\big)=\frac{d}{dt}\Big|_{0}\big(p\cdot\exp(t\xi)\big)\cdot g \qquad\text{(chain rule; }R_g(q)=q\cdot g\text{).}$$
> **Reassociate and slide $g$ across.** By associativity of the right action and then **Lemma 5** (in the form $\exp(t\xi)\,g=g\exp(t\operatorname{Ad}_{g^{-1}}\xi)$),
> $$\big(p\cdot\exp(t\xi)\big)\cdot g=p\cdot\big(\exp(t\xi)\,g\big)=p\cdot\big(g\exp(t\operatorname{Ad}_{g^{-1}}\xi)\big)=(p\cdot g)\cdot\exp\big(t\operatorname{Ad}_{g^{-1}}\xi\big) \qquad\text{(associativity; Lemma 5; associativity again).}$$
> **Recognise the fundamental field at the new base point.** The last expression is the curve through $p\cdot g$ whose velocity at $t=0$ is the fundamental field of $\operatorname{Ad}_{g^{-1}}\xi$ evaluated at $p\cdot g$:
> $$\frac{d}{dt}\Big|_{0}(p\cdot g)\cdot\exp\big(t\operatorname{Ad}_{g^{-1}}\xi\big)=d_e r_{p\cdot g}\big(\operatorname{Ad}_{g^{-1}}\xi\big)=(\operatorname{Ad}_{g^{-1}}\xi)_M(p\cdot g) \qquad\text{(definition }\zeta_M(q)=d_e r_q(\zeta)\text{ with }\zeta=\operatorname{Ad}_{g^{-1}}\xi,\ q=p\cdot g\text{).}$$
> Combining the three displays,
> $$d_pR_g\big(\xi_M(p)\big)=(\operatorname{Ad}_{g^{-1}}\xi)_M(p\cdot g).$$
> This is the pointwise form of $(R_g)_*\xi_M=(\operatorname{Ad}_{g^{-1}}\xi)_M$: the pushforward field $(R_g)_*\xi_M$ has, at the point $p\cdot g=R_g(p)$, the value $d_pR_g(\xi_M(p))$, which we have just shown equals $(\operatorname{Ad}_{g^{-1}}\xi)_M(p\cdot g)$. This proves **(iii)**.
>
> All three parts are established. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Rotational vector fields on the sphere (Riemannian geometry / classical mechanics).** Let $SO(3)$ act on $S^2\subset\mathbb{R}^3$ by rotations, viewed as a right action $x\cdot A=A^{-1}x$ (the standard trick that turns the natural left action into a right one). The fundamental fields of the standard basis $L_1,L_2,L_3$ of $\mathfrak{so}(3)$ are the three infinitesimal rotations about the coordinate axes. Part (i) says their Lie brackets reproduce $[L_a,L_b]=\varepsilon_{abc}L_c$ with the same structure constants, so the notoriously fiddly bracket computation of the angular-momentum fields is replaced by the finite table of $\mathfrak{so}(3)$. The theorem applies because the rotation action is smooth; it is non-obvious because the fields, written in coordinates on $S^2$, look nothing like matrices.

**Vertical fields on a principal bundle (gauge theory proper).** On a principal $G$-bundle $\pi\colon P\to M$ the right $G$-action is free, so $\xi\mapsto\xi_P(p)$ is a linear isomorphism of $\mathfrak{g}$ onto the vertical space $V_pP=\ker d_p\pi$. Part (i) makes $\{\xi_P\}$ a Lie subalgebra of $\mathfrak{X}(P)$ isomorphic to $\mathfrak{g}$, which is the precise sense in which "the fibre direction carries the group's algebra". This is the input to the definition of a connection and to the structure equation; the application is non-obvious because it identifies an infinite-dimensional bracket (of fields on $P$) with a finite-dimensional one (of $\mathfrak{g}$) on the vertical subalgebra.

**Left-invariant frames and the Maurer–Cartan equation (Lie theory).** Take $M=G$ with the right multiplication action of $G$ on itself; the fundamental fields are exactly the left-invariant fields, so part (i) reduces to $[\xi^{L},\eta^{L}]=[\xi,\eta]^{L}$ — the statement that the left-invariant fields form a copy of $\mathfrak{g}$. Dualising, the Maurer–Cartan form $\theta$ satisfies $d\theta+\tfrac12[\theta\wedge\theta]=0$, whose $\mathfrak{g}$-bracket is exactly the bracket transported by this homomorphism. The theorem applies because right multiplication is a free transitive action; it is non-obvious that the abstract structure equation is a shadow of the fundamental-field homomorphism.

---

# Bridges

- **The structure equation for principal connections.** A connection one-form $\omega\in\Omega^1(P;\mathfrak{g})$ is required to reproduce the fundamental fields, $\omega(\xi_P)=\xi$, and to be equivariant. Part (iii) is what forces the equivariance to read $R_g^*\omega=\operatorname{Ad}_{g^{-1}}\omega$: evaluating $R_g^*\omega$ on a fundamental field and using $(R_g)_*\xi_P=(\operatorname{Ad}_{g^{-1}}\xi)_P$ from part (iii) gives $(R_g^*\omega)(\xi_P)=\operatorname{Ad}_{g^{-1}}\xi=\operatorname{Ad}_{g^{-1}}(\omega(\xi_P))$, which is the equivariance on vertical vectors; horizontality extends it. The curvature's structure equation $\Omega=d\omega+\tfrac12[\omega\wedge\omega]$ then uses part (i): the bracket appearing there is the $\mathfrak{g}$-bracket, which is the bracket of vertical fields exactly because $\xi\mapsto\xi_P$ is a homomorphism.

- **The obstruction to free actions on even spheres.** From the flow statement of the fundamental field (on the definition page), a free action of a positive-dimensional $G$ produces a nowhere-vanishing vector field $\xi_M$ on $M$ (freeness makes $\xi_M(p)=0$ impossible for $\xi\neq0$). Combined with the Poincaré–Hopf theorem this forces $\chi(M)=0$, so no positive-dimensional Lie group acts freely on $S^{2n}$. The homomorphism property here guarantees that the whole algebra $\mathfrak{g}$, not just one generator, embeds as commuting-up-to-bracket fields.

- **From right actions to left actions and back.** The dictionary $p\ast g:=g^{-1}\cdot p$ turns a left action into a right one and reverses which invariant fields appear; part (ii) is exactly part (i) transported through this dictionary, with the anti-homomorphism sign accounting for the inversion $g\mapsto g^{-1}$. This is why the series fixes right actions on bundles: it makes $\xi\mapsto\xi_P$ a homomorphism and removes a pervasive sign.

---

# Unlocked by This

> [!tip] Vertical distribution of a principal bundle *(from Gauge Theory III–IV)*
> Part (i) makes the fundamental fields of the free right $G$-action on a principal bundle a Lie subalgebra of $\mathfrak{X}(P)$ isomorphic to $\mathfrak{g}$; this is the algebra of the **vertical distribution**, the kernel of a connection form. See **Def - Connection on a Principal Bundle**.

> [!tip] The transformation law of connection and curvature forms *(from Gauge Theory IV)*
> Part (iii) is the reason connection forms satisfy $R_g^*\omega=\operatorname{Ad}_{g^{-1}}\omega$ and curvature forms $R_g^*\Omega=\operatorname{Ad}_{g^{-1}}\Omega$; these equivariance laws are what let local gauge fields glue into global geometric objects. See **Thm - The Structure Equation and Equivariance of Curvature**.
