---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Associated Bundle"
  - "Def - Principal G-Bundle"
  - "Def - Representation of a Lie Group"
  - "Def - Section of a Vector Bundle"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $\pi\colon P\to M$ is a smooth [[Def - Principal G-Bundle|principal G-bundle]]: a right $G$-action $P\times G\to P$, $(p,g)\mapsto p\cdot g$, that is **free** (if $p\cdot g=p$ for one $p$ then $g=e$) and **fibre-transitive** (each fibre $P_m:=\pi^{-1}(m)$ is a single orbit), together with the local triviality that gives, over a suitable open cover $\{U_\alpha\}$ of $M$, $G$-equivariant diffeomorphisms $\Phi_\alpha\colon\pi^{-1}(U_\alpha)\to U_\alpha\times G$ with $\Phi_\alpha(p)=(\pi(p),\varphi_\alpha(p))$ and $\varphi_\alpha(p\cdot g)=\varphi_\alpha(p)\,g$. We write $R_g\colon P\to P$, $R_g(p)=p\cdot g$, for the right translation by $g\in G$.

We fix a finite-dimensional real or complex vector space $V$ and a [[Def - Representation of a Lie Group|representation]] $\rho\colon G\to GL(V)$, a smooth group homomorphism. Following both sources (Haydys §2.2, Bär Definition 2.2.12), the associated bundle is built from the **right** $G$-action on $P\times V$

$$(p,v)\cdot g=\big(p\cdot g,\ \rho(g^{-1})v\big),$$

whose orbit space is

$$E:=P\times_\rho V:=(P\times V)/G,$$

the [[Def - Associated Bundle|associated bundle]]. We write $[p,v]$ for the orbit of $(p,v)$ and $\varpi\colon P\times V\to E$, $\varpi(p,v)=[p,v]$, for the quotient projection; the bundle projection $E\to M$ is denoted by the same letter $\pi$, so $\pi[p,v]=\pi(p)$. Its fibre over $m$ is $E_m:=\pi^{-1}(m)$. For $p\in P_m$ we write

$$\iota_p\colon V\to E_m,\qquad \iota_p(v):=[p,v]$$

for the **fibre map**; the defining relation of the equivalence is

$$[p,v]=[p\cdot g,\ \rho(g^{-1})v]\quad\text{equivalently}\quad [p\cdot g,\ v]=[p,\ \rho(g)v]\qquad(\forall g\in G),\tag{$\ast$}$$

the second form obtained from the first by replacing $v$ with $\rho(g)v$.

The object of the theorem is the space of **equivariant functions**

$$C^\infty(P;V)^G:=\big\{\hat s\in C^\infty(P;V)\ :\ \hat s(p\cdot g)=\rho(g^{-1})\,\hat s(p)\ \ \forall p\in P,\ g\in G\big\},$$

a vector subspace of the smooth $V$-valued functions on $P$, and $\Gamma(E)$, the space of smooth [[Def - Section of a Vector Bundle|sections]] of $E$. Both are modules over the ring $C^\infty(M)$ of smooth real-valued functions on $M$: $\Gamma(E)$ by pointwise scaling $(f\cdot s)(m)=f(m)\,s(m)$, and $C^\infty(P;V)^G$ by $(f\cdot\hat s)(p)=f(\pi(p))\,\hat s(p)$. We write $\operatorname{id}_M$ for the identity map of $M$ and $\operatorname{id}$ for the identity representation where needed.

> [!warning] Convention: the inverse in $\rho(g^{-1})$
> Both Haydys and Bär glue $P\times V$ by $\rho(g^{-1})$, never $\rho(g)$; the inverse is forced, because it is exactly what makes $(p,v)\mapsto(p\cdot g,\rho(g^{-1})v)$ a **right** action of $G$ (see the non-example on [[Def - Associated Bundle]]). The equivariance law $\hat s(p\cdot g)=\rho(g^{-1})\hat s(p)$ carries the same inverse, and getting its direction right is the crux of the equivariance computation below. The convention that a section transforms by $\rho(g)$ instead describes the *dual* (contragredient) bundle, not $E$.

> [!warning] Convention: source terminology
> Haydys states this as Proposition 37 (p. 15) with the letters $\hat s$, $\varpi$ used above; his sentence "The letter map is $G$-invariant" is a typographical slip for "The **latter** map is $G$-invariant" (the map $\varpi\circ(\operatorname{id},\hat s)$), which is what he proves and what we use. Haydys writes only "it is straightforward to check that $\hat s$ is equivariant" and does not write the smoothness of the inverse; both are supplied in full below.

---

# Statement

> **Theorem (sections of an associated bundle are equivariant functions).** Let $\pi\colon P\to M$ be a smooth principal $G$-bundle and $\rho\colon G\to GL(V)$ a representation on a finite-dimensional vector space $V$, and let $E=P\times_\rho V$ be the associated bundle. Then the map
> $$\Phi\colon C^\infty(P;V)^G\longrightarrow\Gamma(E),\qquad \Phi(\hat s)=s,$$
> where $s$ is the unique section determined by
> $$s\circ\pi=\varpi\circ(\operatorname{id},\hat s),\qquad\text{that is}\qquad s(\pi(p))=[p,\hat s(p)]\ \ (\forall p\in P),\tag{36}$$
> is a bijection. Its inverse sends a section $s\in\Gamma(E)$ to the function
> $$\hat s\colon P\to V,\qquad \hat s(p)=\text{the unique }v\in V\text{ with }s(\pi(p))=[p,v].$$
> Moreover $\Phi$ is an isomorphism of $C^\infty(M)$-modules: it is additive and satisfies $\Phi(f\cdot\hat s)=f\cdot\Phi(\hat s)$ for every $f\in C^\infty(M)$.

The construction of $s$ from $\hat s$ is recorded by the commuting diagram (Haydys, Remark following equation (36))

$$
\begin{array}{ccc}
P & \xrightarrow{\ (\operatorname{id},\hat s)\ } & P\times V\\[2pt]
{\scriptstyle\pi}\big\downarrow & & \big\downarrow{\scriptstyle\varpi}\\[2pt]
M & \xrightarrow{\qquad s\qquad} & P\times_\rho V
\end{array}
$$

which says exactly that $s\circ\pi=\varpi\circ(\operatorname{id},\hat s)$.

---

# Motivation

A section of a vector bundle is a global geometric object; an equivariant function is a rule for reading that object off in every local frame at once, together with the law relating the readings in different frames. The theorem says these two descriptions carry identical information: the coordinate-free section and the "components in every gauge, transforming by $\rho$" are the same datum in two languages.

The importance of this is entirely practical. Every computation in gauge theory — a covariant derivative, a curvature, a Yang–Mills field, a Dirac spinor — is eventually done on the total space $P$, where there is a canonical connection form and where the group acts by an honest action, rather than downstairs on $M$, where the associated bundle is a quotient with no preferred fibre coordinates. The theorem is the dictionary that lets one work upstairs and know that the result is a genuine object downstairs: a $V$-valued function on $P$ **is** a section of $E$ precisely when it obeys the equivariance law, and nothing more needs to be checked. Its differential-form analogue, [[Thm - Bundle-Valued Forms on the Base are Basic Equivariant Forms on the Total Space|the basic-equivariant-forms theorem]], extends the same dictionary from functions to $E$-valued forms, and is the tool with which the local connection and curvature forms of chapter IV are recognised as objects on $P$. The theorem is therefore not an isolated curiosity but the identification on which the whole passage between principal-bundle and associated-bundle pictures rests.

The degree-zero case treated here is also the cleanest place to see why the machinery works, because a function has no arguments to feed vertical vectors into, so the "basic" condition of the form-version is automatic and only the equivariance survives. Everything genuinely new in the correspondence — the descent through the quotient, the role of freeness and transitivity, the direction of the $\rho(g^{-1})$ — is already present, and visible, at this level.

---

# Sources and Targets

**Sources (Input Broadening).** The literal hypothesis is only "an equivariant function on $P$", so the source question is: when does a problem hand you an equivariant function without naming one?

The first disguised source is **a physical or geometric field presented by its components in every gauge, with a transformation law**. In gauge theory a matter field is very often specified as "a $V$-valued quantity $\hat s$ that, under a change of local frame $p\mapsto p\cdot g$, transforms as $\hat s\mapsto\rho(g^{-1})\hat s$". That description is verbatim the equivariance condition $\hat s(p\cdot g)=\rho(g^{-1})\hat s(p)$, so the theorem promotes it, with no further work, to a coordinate-free section of the associated bundle $E=P\times_\rho V$; the bridge $B\Rightarrow A$ is "obeys the tensorial transformation law $\Rightarrow$ is an equivariant function". The non-obvious part is that no compatibility across overlapping charts has to be checked separately: the single global equivariance law already encodes all the transition data. *Example problem:* a "colour field" on a $G$-bundle given by its numerical components in each trivialisation with the stated transformation rule defines a section of the associated bundle, and its zero set is therefore a well-defined subset of $M$.

The second disguised source is **a $G$-invariant construction performed on the total space with values in a $G$-representation**. Whenever one builds, from data living on $P$, a smooth map $\hat s\colon P\to V$ into a $G$-representation and can show it is equivariant, one has produced a section of $E$ for free; the bridge is "naturally built on $P$ and equivariant $\Rightarrow$ descends to a section". This is how the difference of two connections, though defined as a form on $P$, becomes a form on $M$ with values in $\operatorname{ad}P$ (the form-level analogue), and how endomorphism fields arise. *Example problem:* given two metric connections on a vector bundle, their difference tensor is manufactured on the frame bundle and shown to be equivariant, hence is a genuine $\operatorname{End}(E)$-valued one-form on $M$.

The third disguised source is **a map out of $P$ that one wishes to push down to $M$**. A smooth map $F\colon P\to N$ descends to a map $M\to N$ exactly when it is constant on the fibres of $\pi$, and for maps into an associated bundle "constant on fibres, in the right sense" is precisely the equivariance $(\ast)$. Recognising that a fibrewise-defined quantity is really an equivariant function is what lets it be treated as an object on the base. *Example problem:* the "position of a section relative to the frame", $p\mapsto\iota_p^{-1}(s(\pi(p)))$, is an equivariant function; that observation is the construction of the inverse map in this very theorem.

**Targets (Output Amplification).** The bare conclusion — a bijection, indeed a $C^\infty(M)$-module isomorphism — becomes far more when combined with further structure.

Combine the theorem with **a chosen connection on $P$ and its form-valued analogue**. The degree-one version of the correspondence identifies $\Omega^1(M;E)$ with the basic equivariant $V$-valued one-forms on $P$, so that a connection's local forms and its curvature, both naturally living on $P$, are recognised as global objects on $M$. The extra ingredient $D$ is [[Thm - Bundle-Valued Forms on the Base are Basic Equivariant Forms on the Total Space|the basic-equivariant-forms theorem]], and the payoff $E$ is that the induced covariant derivative on any associated bundle can be written by the uniform formula $\pi^\ast(\nabla s)=d\hat s+\rho_\ast(a)\,\hat s$ upstairs — the master identity of chapter IV.

Combine the theorem with **the adjoint representation**. Taking $V=\mathfrak g$ and $\rho=\operatorname{Ad}$ gives the adjoint bundle $\operatorname{ad}P=P\times_{\operatorname{Ad}}\mathfrak g$ (see [[Def - Adjoint Bundles ad P and Ad P]]), and the theorem identifies $\Gamma(\operatorname{ad}P)$ with the equivariant $\mathfrak g$-valued functions $\hat\xi(p\cdot g)=\operatorname{Ad}_{g^{-1}}\hat\xi(p)$. The extra ingredient is the differentiated conjugation action; the payoff is that the infinitesimal gauge transformations, which are sections of $\operatorname{ad}P$, acquire their concrete description as equivariant functions on $P$, used throughout chapter V.

Combine the theorem with **the conjugation action on the group itself**. The gauge group — the automorphisms of $P$ covering the identity — is in bijection with the sections of the group bundle $P\times_{\mathrm{conj}}G$, equivalently with the equivariant maps $\hat g\colon P\to G$ satisfying $\hat g(p\cdot h)=h^{-1}\hat g(p)\,h$; this is the group-valued form of the same correspondence, and **the gauge group appears as sections of the associated (adjoint) bundle** rather than as a mysterious infinite-dimensional group. The extra ingredient $D$ is the (nonlinear) conjugation action; the payoff $E$, developed in chapter V, is that the gauge group and its Lie algebra $\Gamma(\operatorname{ad}P)$ are handled by exactly the machinery of this theorem.

---

# Why Is It True

Forget the quotient for a moment and picture the frame-bundle case, which is the origin of the whole idea. Let $E$ be a rank-$k$ real vector bundle, $P=\operatorname{Fr}(E)$ its bundle of frames, $G=GL_k(\mathbb R)$, and $\rho=\operatorname{id}$ the defining representation on $V=\mathbb R^k$; a point $p\in P_m$ is an ordered basis of $E_m$, that is, a linear isomorphism $p\colon\mathbb R^k\to E_m$, and the right action $p\cdot A=p\circ A$ changes the frame by $A\in GL_k(\mathbb R)$. A section $s$ of $E$ assigns to each frame $p$ the coordinate vector of $s(m)$ in that frame, namely $\hat s(p)=p^{-1}\big(s(m)\big)\in\mathbb R^k$. Under a change of frame $p\mapsto p\cdot A=p\circ A$ the coordinates change by $\hat s(p\cdot A)=(p\circ A)^{-1}s(m)=A^{-1}p^{-1}s(m)=A^{-1}\hat s(p)=\rho(A^{-1})\hat s(p)$. That last line **is** the equivariance law. So a section is nothing but its tuple of components in every frame, and the tensorial transformation rule of classical differential geometry is exactly the equivariance condition.

> A section of $E$ and a $\rho$-equivariant function on $P$ are the same object seen from two sides: the section is the frame-independent value, the equivariant function is its list of components in every frame, and the equivariance law is the change-of-frame rule that makes the list consistent.

The general case is this picture with $\iota_p$ in place of "coordinates in the frame $p$". For each $p\in P_m$ the fibre map $\iota_p\colon V\to E_m$, $v\mapsto[p,v]$, is a linear **isomorphism** — injective because the action is free, surjective because the fibre is a single orbit — so $p$ plays the role of a "generalised frame" identifying the abstract model space $V$ with the concrete fibre $E_m$. Given a section $s$, define $\hat s(p)=\iota_p^{-1}(s(\pi(p)))$: the components of $s$ read through the frame $p$. Changing the frame within the fibre, $p\mapsto p\cdot g$, changes the identification by exactly $\rho(g^{-1})$, because $\iota_{p\cdot g}=\iota_p\circ\rho(g)$ is precisely what relation $(\ast)$ asserts; hence $\hat s(p\cdot g)=\rho(g^{-1})\hat s(p)$. Conversely, an equivariant $\hat s$ has, at each fibre, a value $[p,\hat s(p)]$ that does not depend on which $p$ in the fibre is used — the $\rho(g^{-1})$ in the equivariance and the $\rho(g)$ in $(\ast)$ cancel — so it names a single element of $E_m$ and defines a section. The two constructions undo each other because both are "read the components through a frame" and "reassemble the value from its components". No cleverness is needed once the fibre map is seen as a frame.

---

# What Makes This Hard

The conceptual content is easy; the three places where a careless proof breaks are all about rigour, not idea. First, the **direction of the inverse**: the equivariance law and the equivalence relation both involve $\rho(g^{-1})$, and it is genuinely necessary to track which is which, because writing $\rho(g)$ where $\rho(g^{-1})$ is meant produces the dual bundle and a false theorem. Second, **well-definedness through the quotient**: the value $s(\pi(p))=[p,\hat s(p)]$ is computed at a chosen representative $p$ of the fibre, and one must verify it is independent of that choice — this is where freeness (so that the only ambiguity in $p$ is a right translation) and equivariance (so that the translation is absorbed) are both used, and skipping the check leaves $s$ undefined. Third, **smoothness**: the quotient $E$ has no a priori coordinates, so the smoothness of $s$ and of the inverse $\hat s$ cannot be read off the formulas directly; it must be extracted from a local section and the associated local trivialisation, and for the inverse one additionally needs that the "$G$-coordinate" of a point relative to a local section is a smooth function of the point. The common error is to prove the set-theoretic bijection and declare victory, leaving all three smoothness statements — and often the equivariance of the inverse — asserted rather than shown, which is exactly the gap in the source.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Establish that each fibre map $\iota_p\colon V\to E_m$ is a linear isomorphism (freeness for injectivity, transitivity for surjectivity), so that $p$ is a "frame". Then build both maps explicitly — $\Phi$ sends $\hat s$ to the section whose value is $[p,\hat s(p)]$, and $\Psi$ sends $s$ to the components $\hat s(p)=\iota_p^{-1}(s(\pi p))$ — check each lands where claimed (well-defined, smooth section; equivariant, smooth function), verify they are two-sided inverses, and finally note both are $C^\infty(M)$-linear so that $\Phi$ is a module isomorphism.

**Subgoal decomposition:**

1. **The fibre map is a linear isomorphism, and $(\ast)$ holds.** Show $\iota_p$ is injective (freeness), surjective (single-orbit fibre), and linear (the fibrewise vector-space structure), and derive $\iota_{p\cdot g}=\iota_p\circ\rho(g)$.
   - *Hint:* Injectivity: $[p,v]=[p,w]$ forces $p\cdot g=p$, hence $g=e$ by freeness, hence $v=w$. Surjectivity: any $[q,w]$ in $E_m$ has $q=p\cdot g$ by transitivity, so $[q,w]=\iota_p(\rho(g)w)$.
   - *Why needed:* This is the "frame" structure that both maps use; without the isomorphism there is no $\iota_p^{-1}$ and no components.

2. **$\Phi$ is well-defined into $\Gamma(E)$.** Show $s(m):=[p,\hat s(p)]$ is independent of $p\in P_m$, is a section, and is smooth.
   - *Hint:* Independence: change $p$ to $p\cdot g$, use equivariance then $(\ast)$ to return to $[p,\hat s(p)]$. Smoothness: on a trivialising $U$ with local section $\sigma$, read $s$ in the trivialisation as $m\mapsto(m,\hat s(\sigma(m)))$.
   - *Why needed:* Until independence is checked $s$ is not a function; until smoothness is checked $s\notin\Gamma(E)$.

3. **$\Psi$ is well-defined into $C^\infty(P;V)^G$.** Show $\hat s(p):=\iota_p^{-1}(s(\pi p))$ is equivariant and smooth.
   - *Hint:* Equivariance: from $[p\cdot g,\hat s(p\cdot g)]=s(\pi p)=[p,\hat s(p)]=[p\cdot g,\rho(g^{-1})\hat s(p)]$ and injectivity of $\iota_{p\cdot g}$. Smoothness: write $p=\sigma(\pi p)\cdot\varphi(p)$ with $\varphi$ smooth and use equivariance to reduce to the trivialisation.
   - *Why needed:* This is the map the source leaves unproved; it is the content beyond the set bijection.

4. **$\Phi$ and $\Psi$ are mutual inverses.** Show $\Psi\circ\Phi=\operatorname{id}$ and $\Phi\circ\Psi=\operatorname{id}$.
   - *Hint:* Both directions are uniqueness statements: $\iota_p$ injective forces the component of $[p,\hat s(p)]$ to be $\hat s(p)$, and forces the section with value $[p,\hat s(p)]$ to be the given one.
   - *Why needed:* Bijectivity is the theorem's core claim.

5. **$\Phi$ is $C^\infty(M)$-linear.** Show $\Phi$ is additive and commutes with multiplication by $f\in C^\infty(M)$.
   - *Hint:* Use linearity of $\iota_p$: $[p,v]+[p,w]=[p,v+w]$ and $c[p,v]=[p,cv]$, with $c=f(\pi p)$.
   - *Why needed:* Upgrades the bijection to a module isomorphism, which is how the result is used.

---

# Lemma Decomposition

> [!note]- Lemma 1: The fibre map is a linear isomorphism, and $\iota_{p\cdot g}=\iota_p\circ\rho(g)$
> **Statement:** For each $p\in P$ with $\pi(p)=m$, the fibre map $\iota_p\colon V\to E_m$, $\iota_p(v)=[p,v]$, is a linear isomorphism onto $E_m$. Moreover $\iota_{p\cdot g}=\iota_p\circ\rho(g)$ for all $g\in G$; equivalently, $\iota_{p\cdot g}^{-1}=\rho(g^{-1})\circ\iota_p^{-1}$.
>
> **Hint:** Injectivity uses freeness, surjectivity uses fibre-transitivity, linearity is the fibrewise vector-space structure of the associated bundle; the identity $\iota_{p\cdot g}=\iota_p\circ\rho(g)$ is a restatement of $(\ast)$.
>
> **Why needed:** It supplies the "frame" $\iota_p$ used to define components and to reassemble values, together with the exact way the frame changes under the group; every later step invokes it.
>
> > [!note]- Full proof
> > Fix $p\in P$ with $\pi(p)=m$.
> >
> > **$\iota_p$ is injective (by freeness).** Suppose $\iota_p(v)=\iota_p(w)$, that is $[p,v]=[p,w]$. By the definition of the orbit relation there is $g\in G$ with $(p,w)=(p,v)\cdot g=(p\cdot g,\rho(g^{-1})v)$. Comparing first coordinates gives $p\cdot g=p$, so $g=e$ because the $G$-action on $P$ is **free**; comparing second coordinates then gives $w=\rho(e^{-1})v=\rho(e)v=v$. Hence $v=w$ and $\iota_p$ is injective.
> >
> > **$\iota_p$ is surjective (by transitivity on fibres).** Let $x\in E_m$. Choose a representative, $x=[q,w]$ with $q\in P$, $w\in V$; since $\pi[q,w]=\pi(q)$ and $x\in E_m$, we have $\pi(q)=m$, so $q\in P_m$. Because the fibre $P_m$ is a single $G$-orbit (**fibre-transitivity**), there is $g\in G$ with $q=p\cdot g$. Then, using relation $(\ast)$ in its second form $[p\cdot g,w]=[p,\rho(g)w]$,
> > $$x=[q,w]=[p\cdot g,w]=[p,\rho(g)w]=\iota_p\big(\rho(g)w\big)\qquad(\text{by }(\ast)),$$
> > so $x$ is in the image of $\iota_p$. Hence $\iota_p$ is surjective.
> >
> > **$\iota_p$ is linear.** By the construction of the associated bundle, each fibre $E_m$ carries the vector-space structure defined by $[p,v]+[p,w]:=[p,v+w]$ and $c\,[p,v]:=[p,cv]$, shown well-defined (independent of the representative $p$) on [[Def - Associated Bundle|the associated-bundle page, Clause 1]]. With that structure, $\iota_p(v)+\iota_p(w)=[p,v]+[p,w]=[p,v+w]=\iota_p(v+w)$ and $c\,\iota_p(v)=c[p,v]=[p,cv]=\iota_p(cv)$ for all $v,w\in V$ and scalars $c$. Thus $\iota_p$ is linear, and being a linear bijection it is a linear isomorphism.
> >
> > **The change-of-frame identity.** For $g\in G$ and $v\in V$, relation $(\ast)$ gives
> > $$\iota_{p\cdot g}(v)=[p\cdot g,v]=[p,\rho(g)v]=\iota_p(\rho(g)v)=(\iota_p\circ\rho(g))(v)\qquad(\text{by }(\ast)),$$
> > so $\iota_{p\cdot g}=\iota_p\circ\rho(g)$. Inverting both sides (each factor is a linear isomorphism) gives $\iota_{p\cdot g}^{-1}=\rho(g)^{-1}\circ\iota_p^{-1}=\rho(g^{-1})\circ\iota_p^{-1}$, since $\rho$ is a homomorphism and $\rho(g)^{-1}=\rho(g^{-1})$. $\blacksquare$

> [!note]- Lemma 2: The forward map lands in $\Gamma(E)$
> **Statement:** Let $\hat s\in C^\infty(P;V)^G$. The rule $s(m):=[p,\hat s(p)]$ for any $p\in P_m$ defines a map $s\colon M\to E$ that is independent of the choice of $p\in P_m$, satisfies $\pi\circ s=\operatorname{id}_M$, and is smooth. Hence $s\in\Gamma(E)$, and it is the unique map with $s\circ\pi=\varpi\circ(\operatorname{id},\hat s)$.
>
> **Hint:** Independence of $p$ combines equivariance with $(\ast)$; smoothness is read in a local trivialisation coming from a local section of $P$.
>
> **Why needed:** It shows $\Phi(\hat s)=s$ is actually a smooth section, not merely a set-map, and pins down $s$ by equation (36).
>
> > [!note]- Full proof
> > Fix $\hat s\in C^\infty(P;V)^G$ and $m\in M$.
> >
> > **Independence of the representative.** Let $p,p'\in P_m$. By fibre-transitivity there is $g\in G$ with $p'=p\cdot g$. Then
> > $$[p',\hat s(p')]=[p\cdot g,\ \hat s(p\cdot g)]=[p\cdot g,\ \rho(g^{-1})\hat s(p)]\qquad(\text{equivariance of }\hat s),$$
> > and applying relation $(\ast)$ in its second form $[p\cdot g,w]=[p,\rho(g)w]$ with $w=\rho(g^{-1})\hat s(p)$,
> > $$[p\cdot g,\ \rho(g^{-1})\hat s(p)]=[p,\ \rho(g)\rho(g^{-1})\hat s(p)]=[p,\ \hat s(p)]\qquad(\text{by }(\ast)\text{ and }\rho(g)\rho(g^{-1})=\rho(e)=\operatorname{id}_V).$$
> > Combining the two displays, $[p',\hat s(p')]=[p,\hat s(p)]$, so $s(m)$ does not depend on which point of $P_m$ is used. This is precisely the statement that $p\mapsto[p,\hat s(p)]=\varpi(p,\hat s(p))$ is constant on each fibre of $\pi$, so $s$ is the unique set-map with $s\circ\pi=\varpi\circ(\operatorname{id},\hat s)$, i.e. equation (36).
> >
> > **$s$ is a section.** For any $p\in P_m$, $\pi(s(m))=\pi([p,\hat s(p)])=\pi(p)=m$ (definition of the projection of $E$). Hence $\pi\circ s=\operatorname{id}_M$.
> >
> > **$s$ is smooth.** Fix $m_0\in M$. Choose a trivialising open set $U\ni m_0$ on which $P$ admits a smooth local section $\sigma\colon U\to P$ with $\pi\circ\sigma=\operatorname{id}_U$ (such $\sigma$ exists over any trivialising set: set $\sigma(m)=\Phi_\alpha^{-1}(m,e)$; this is the content of [[Thm - Sections of a Principal Bundle and Triviality|local sections exist over trivialising sets]]). By the construction of the associated bundle, this $\sigma$ yields a local trivialisation
> > $$\psi_U\colon\pi^{-1}(U)\subseteq E\longrightarrow U\times V,\qquad \psi_U^{-1}(m,v)=[\sigma(m),v],$$
> > a diffeomorphism (proved on [[Def - Associated Bundle]], Clause 2). By the independence just shown we may compute $s(m)$ with the representative $p=\sigma(m)\in P_m$:
> > $$s(m)=[\sigma(m),\ \hat s(\sigma(m))]=\psi_U^{-1}\big(m,\ \hat s(\sigma(m))\big),\qquad\text{so}\qquad \psi_U\big(s(m)\big)=\big(m,\ \hat s(\sigma(m))\big).$$
> > The right-hand side is smooth in $m$ on $U$, because $\sigma$ is smooth and $\hat s$ is smooth, so their composite $\hat s\circ\sigma$ is smooth. As $\psi_U$ is a diffeomorphism, $s$ is smooth on $U$. Since $m_0$ was arbitrary and such $U$ cover $M$, $s$ is smooth on all of $M$. Therefore $s\in\Gamma(E)$. $\blacksquare$

> [!note]- Lemma 3: The inverse map lands in $C^\infty(P;V)^G$
> **Statement:** Let $s\in\Gamma(E)$. The rule $\hat s(p):=\iota_p^{-1}\big(s(\pi(p))\big)$, that is, the unique $v\in V$ with $s(\pi(p))=[p,v]$, defines a map $\hat s\colon P\to V$ that is $\rho$-equivariant, $\hat s(p\cdot g)=\rho(g^{-1})\hat s(p)$, and smooth. Hence $\hat s\in C^\infty(P;V)^G$.
>
> **Hint:** Equivariance is the change-of-frame identity of Lemma 1 read backwards; smoothness reduces to a trivialisation via the smooth $G$-coordinate $\varphi$ of a point relative to a local section.
>
> **Why needed:** This is the map the source only sketches; equivariance and smoothness of $\hat s$ are the two statements Haydys leaves unwritten, and they are what make $\Psi\colon s\mapsto\hat s$ a legitimate inverse.
>
> > [!note]- Full proof
> > Fix $s\in\Gamma(E)$. The value $\hat s(p)$ is well-defined because $\iota_p\colon V\to E_{\pi(p)}$ is a bijection (Lemma 1), so there is exactly one $v$ with $\iota_p(v)=s(\pi(p))$.
> >
> > **$\hat s$ is equivariant.** Fix $p\in P$ and $g\in G$; write $m=\pi(p)=\pi(p\cdot g)$. By definition of $\hat s$ applied at the point $p\cdot g$,
> > $$s(m)=\big[p\cdot g,\ \hat s(p\cdot g)\big]=\iota_{p\cdot g}\big(\hat s(p\cdot g)\big).$$
> > By definition of $\hat s$ at $p$ together with the change-of-frame identity $\iota_p=\iota_{p\cdot g}\circ\rho(g^{-1})$ (invert $\iota_{p\cdot g}=\iota_p\circ\rho(g)$ from Lemma 1),
> > $$s(m)=\iota_p\big(\hat s(p)\big)=\iota_{p\cdot g}\big(\rho(g^{-1})\hat s(p)\big)\qquad(\text{by Lemma 1: }\iota_p=\iota_{p\cdot g}\circ\rho(g^{-1})).$$
> > Equating the two expressions for $s(m)$ gives $\iota_{p\cdot g}(\hat s(p\cdot g))=\iota_{p\cdot g}(\rho(g^{-1})\hat s(p))$, and since $\iota_{p\cdot g}$ is injective (Lemma 1),
> > $$\hat s(p\cdot g)=\rho(g^{-1})\,\hat s(p).$$
> > Thus $\hat s$ satisfies the equivariance law with the correct inverse.
> >
> > **$\hat s$ is smooth.** Fix $p_0\in P$ and set $m_0=\pi(p_0)$. Choose a trivialising open set $U\ni m_0$ with smooth local section $\sigma\colon U\to P$ and the associated trivialisation $\psi_U$ of $E$ as in Lemma 2, and let $\Phi_\alpha\colon\pi^{-1}(U)\to U\times G$, $\Phi_\alpha(p)=(\pi(p),\varphi_\alpha(p))$, be the $G$-equivariant trivialisation of $P$ over $U$ (with $\sigma(m)=\Phi_\alpha^{-1}(m,e)$, so $\varphi_\alpha\circ\sigma\equiv e$). The map $\varphi_\alpha\colon\pi^{-1}(U)\to G$ is smooth, being a component of the diffeomorphism $\Phi_\alpha$. For every $p\in\pi^{-1}(U)$ we have
> > $$\Phi_\alpha\big(\sigma(\pi(p))\cdot\varphi_\alpha(p)\big)=\big(\pi(p),\ \varphi_\alpha(\sigma(\pi(p)))\,\varphi_\alpha(p)\big)=\big(\pi(p),\ e\cdot\varphi_\alpha(p)\big)=\big(\pi(p),\varphi_\alpha(p)\big)=\Phi_\alpha(p),$$
> > using equivariance $\varphi_\alpha(q\cdot g)=\varphi_\alpha(q)g$ and $\varphi_\alpha(\sigma(\pi p))=e$; since $\Phi_\alpha$ is injective,
> > $$p=\sigma(\pi(p))\cdot\varphi_\alpha(p)\qquad(\forall\,p\in\pi^{-1}(U)).\tag{$\dagger$}$$
> > Next, writing $s$ in the trivialisation $\psi_U$ as $\psi_U(s(m))=(m,f(m))$ defines a smooth map $f\colon U\to V$ (smooth because $s$ is smooth and $\psi_U$ is a diffeomorphism), and then $s(m)=\psi_U^{-1}(m,f(m))=[\sigma(m),f(m)]$, so by uniqueness of components (Lemma 1 for the frame $\sigma(m)$),
> > $$\hat s(\sigma(m))=f(m)\qquad(\forall\,m\in U).$$
> > Combining this with equivariance and $(\dagger)$, for every $p\in\pi^{-1}(U)$,
> > $$\hat s(p)=\hat s\big(\sigma(\pi p)\cdot\varphi_\alpha(p)\big)=\rho\big(\varphi_\alpha(p)^{-1}\big)\,\hat s(\sigma(\pi p))=\rho\big(\varphi_\alpha(p)^{-1}\big)\,f(\pi(p))\qquad(\text{equivariance and }(\dagger)).$$
> > Every factor on the right is smooth in $p$: $\varphi_\alpha$ is smooth, inversion $G\to G$ is smooth, $\rho\colon G\to GL(V)$ is smooth, the evaluation $GL(V)\times V\to V$ is smooth (bilinear), and $f\circ\pi$ is smooth. Hence $\hat s$ is smooth on $\pi^{-1}(U)$. Since $p_0$ was arbitrary and such sets cover $P$, $\hat s$ is smooth. Therefore $\hat s\in C^\infty(P;V)^G$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\pi\colon P\to M$ be a principal $G$-bundle, $\rho\colon G\to GL(V)$ a representation, and $E=P\times_\rho V$ the associated bundle. Write
> $$\Phi\colon C^\infty(P;V)^G\to\Gamma(E),\quad \Phi(\hat s)=s\ \text{ with }\ s(\pi p)=[p,\hat s(p)],\qquad
> \Psi\colon\Gamma(E)\to C^\infty(P;V)^G,\quad \Psi(s)=\hat s\ \text{ with }\ \hat s(p)=\iota_p^{-1}(s(\pi p)).$$
>
> **Step 0 — the maps are well-defined into the stated spaces.** By Lemma 2, for $\hat s\in C^\infty(P;V)^G$ the element $s=\Phi(\hat s)$ is a well-defined smooth section of $E$, uniquely characterised by equation (36); so $\Phi$ maps into $\Gamma(E)$. By Lemma 3, for $s\in\Gamma(E)$ the function $\hat s=\Psi(s)$ is a well-defined smooth $\rho$-equivariant function; so $\Psi$ maps into $C^\infty(P;V)^G$. (Lemma 1, used by both, provides the fibre isomorphisms $\iota_p$ that make $\iota_p^{-1}$ meaningful.)
>
> **Step 1 — $\Psi\circ\Phi=\operatorname{id}$ on $C^\infty(P;V)^G$.** Take $\hat s\in C^\infty(P;V)^G$ and put $s=\Phi(\hat s)$, so $s(\pi p)=[p,\hat s(p)]=\iota_p(\hat s(p))$ for all $p$. Then $\Psi(s)$ is by definition the function $p\mapsto\iota_p^{-1}(s(\pi p))$, and
> $$(\Psi\circ\Phi)(\hat s)(p)=\iota_p^{-1}\big(s(\pi p)\big)=\iota_p^{-1}\big(\iota_p(\hat s(p))\big)=\hat s(p)\qquad(\text{since }\iota_p^{-1}\circ\iota_p=\operatorname{id}_V,\ \text{Lemma 1}).$$
> As $p$ was arbitrary, $(\Psi\circ\Phi)(\hat s)=\hat s$.
>
> **Step 2 — $\Phi\circ\Psi=\operatorname{id}$ on $\Gamma(E)$.** Take $s\in\Gamma(E)$ and put $\hat s=\Psi(s)$, so by definition $s(\pi p)=[p,\hat s(p)]$ for all $p$. Let $s'=\Phi(\hat s)$; by equation (36), $s'$ is the unique section with $s'(\pi p)=[p,\hat s(p)]$ for all $p$. But $s$ itself satisfies $s(\pi p)=[p,\hat s(p)]$ for all $p$, and $\pi$ is surjective, so $s$ and $s'$ agree at every point of $M$. By the uniqueness clause of Lemma 2, $s'=s$. Hence $(\Phi\circ\Psi)(s)=s$.
>
> **Step 3 — $\Phi$ is a bijection.** Steps 1 and 2 exhibit $\Psi$ as a two-sided inverse of $\Phi$; therefore $\Phi$ is a bijection with $\Phi^{-1}=\Psi$.
>
> **Step 4 — $\Phi$ is additive.** Let $\hat s_1,\hat s_2\in C^\infty(P;V)^G$; their sum $\hat s_1+\hat s_2$ is again equivariant (equivariance is a linear condition: $\rho(g^{-1})$ is linear). For every $p\in P$, writing $m=\pi(p)$ and using the fibrewise linearity of $\iota_p$ (Lemma 1),
> $$\Phi(\hat s_1+\hat s_2)(m)=\big[p,\ \hat s_1(p)+\hat s_2(p)\big]=[p,\hat s_1(p)]+[p,\hat s_2(p)]=\Phi(\hat s_1)(m)+\Phi(\hat s_2)(m)\quad(\text{fibrewise addition in }E_m).$$
> Since this holds at every $m$ (with any representative $p\in P_m$), $\Phi(\hat s_1+\hat s_2)=\Phi(\hat s_1)+\Phi(\hat s_2)$.
>
> **Step 5 — $\Phi$ is $C^\infty(M)$-linear.** Let $f\in C^\infty(M)$ and $\hat s\in C^\infty(P;V)^G$; the function $f\cdot\hat s$, $(f\cdot\hat s)(p)=f(\pi p)\hat s(p)$, is equivariant because $(f\cdot\hat s)(p\cdot g)=f(\pi p)\rho(g^{-1})\hat s(p)=\rho(g^{-1})\big(f(\pi p)\hat s(p)\big)$ (the scalar $f(\pi p)$ commutes with the linear map $\rho(g^{-1})$, and $\pi(p\cdot g)=\pi(p)$). For every $p\in P$ with $m=\pi(p)$, using the fibrewise scalar multiplication of $\iota_p$ (Lemma 1) with $c=f(m)$,
> $$\Phi(f\cdot\hat s)(m)=\big[p,\ f(m)\hat s(p)\big]=f(m)\,[p,\hat s(p)]=f(m)\,\Phi(\hat s)(m)=(f\cdot\Phi(\hat s))(m).$$
> Hence $\Phi(f\cdot\hat s)=f\cdot\Phi(\hat s)$. Together with Step 4, $\Phi$ is a homomorphism of $C^\infty(M)$-modules.
>
> **Step 6 — conclusion.** $\Phi$ is a bijective homomorphism of $C^\infty(M)$-modules (Steps 3–5). Its inverse $\Psi$ is then automatically $C^\infty(M)$-linear: for $s_1,s_2\in\Gamma(E)$ and $f\in C^\infty(M)$, applying the injective $\Phi$ to $\Psi(f\cdot s_1+s_2)$ and to $f\cdot\Psi(s_1)+\Psi(s_2)$ gives the same value $f\cdot s_1+s_2$ (using Steps 4–5 and $\Phi\circ\Psi=\operatorname{id}$), so the two arguments are equal. Therefore
> $$\Phi\colon C^\infty(P;V)^G\xrightarrow{\ \cong\ }\Gamma(E)$$
> is an isomorphism of $C^\infty(M)$-modules, with inverse $\Psi(s)=\big(p\mapsto\iota_p^{-1}(s(\pi p))\big)$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Tensor fields as equivariant functions on the frame bundle (Riemannian geometry).** Take $P=\operatorname{Fr}(TM)$ the frame bundle of the tangent bundle, $G=GL_n(\mathbb R)$, and $\rho$ the representation of $GL_n(\mathbb R)$ on the space $V=(\mathbb R^n)^{\otimes p}\otimes((\mathbb R^n)^\ast)^{\otimes q}$ of $(p,q)$-tensors. The theorem says a $(p,q)$-tensor field on $M$ is the same as a smooth $V$-valued function on $\operatorname{Fr}(TM)$ transforming by $\rho(A^{-1})$ under a change of frame by $A$ — which is exactly the classical index transformation law $T'^{i_1\cdots}_{\ j_1\cdots}=A^{-1}\!\cdots A\cdots\,T^{\cdots}_{\cdots}$. The exercise applies because the classical "object that transforms tensorially" is verbatim an equivariant function; it is non-obvious that the correspondence needs no separate patching between charts, because the single global equivariance already encodes all transitions.

**The gauge group and its Lie algebra (mathematical physics).** With $V=\mathfrak g$ and $\rho=\operatorname{Ad}$, the theorem identifies the sections of $\operatorname{ad}P$ with the equivariant functions $\hat\xi\colon P\to\mathfrak g$, $\hat\xi(p\cdot g)=\operatorname{Ad}_{g^{-1}}\hat\xi(p)$; these are the infinitesimal gauge transformations. The nonlinear analogue, with $V$ replaced by the group $G$ under conjugation, presents the gauge group itself as sections of the group bundle. The theorem applies because both the adjoint action and conjugation are $G$-actions on a "model fibre", and it is non-obvious that an infinite-dimensional group of bundle automorphisms is captured by so concrete a description as "equivariant $G$-valued functions on $P$".

**Associated line bundles and charged fields (complex geometry / electromagnetism).** Take $G=U(1)$, $P$ a principal circle bundle, and $\rho=\rho_k\colon e^{i\theta}\mapsto e^{ik\theta}$ acting on $V=\mathbb C$. A section of the associated line bundle $L^{\otimes k}=P\times_{\rho_k}\mathbb C$ is an equivariant function $\hat s(p\cdot e^{i\theta})=e^{-ik\theta}\hat s(p)$, that is, a complex field of "charge $k$". The theorem applies because the charge-$k$ transformation rule is exactly $\rho_k$-equivariance; it is non-obvious that the topology of $L^{\otimes k}$ (its degree, its zeros) is entirely encoded in these scalar equivariant functions on the circle bundle, which is the starting point for the Chern-class computations of later chapters.

---

# Bridges

- **The basic-equivariant-forms theorem.** The natural next step raises the correspondence from functions to forms: for each $q$, [[Thm - Bundle-Valued Forms on the Base are Basic Equivariant Forms on the Total Space|the basic-equivariant-forms theorem]] gives an isomorphism $\Omega^q(M;E)\cong\Omega^q_{\mathrm{bas}}(P;V)^G$ between $E$-valued $q$-forms on $M$ and the basic (vanishing on vertical vectors) equivariant $V$-valued $q$-forms on $P$. The present theorem is the case $q=0$, where "basic" is vacuous because a function has no arguments; the general construction pulls a form back along $\pi$ and recognises the pullback by its equivariance and horizontality. This is the form in which local connection and curvature forms are transported between $P$ and $M$.

- **The adjoint bundle.** Specialising the model space to the Lie algebra with the adjoint action produces $\operatorname{ad}P=P\times_{\operatorname{Ad}}\mathfrak g$ (constructed on [[Def - Adjoint Bundles ad P and Ad P]]); this theorem then reads $\Gamma(\operatorname{ad}P)$ as the equivariant $\mathfrak g$-valued functions on $P$. The construction is the same associated-bundle machinery with a distinguished representation, and it is the bundle in which the difference of two principal connections, the curvature seen on the base, and the infinitesimal gauge transformations all live.

- **Recovering a vector bundle from its frame bundle.** When $P=\operatorname{Fr}(E)$ and $\rho$ is the standard representation, the associated bundle is $E$ itself ([[Thm - Vector Bundles are Associated to Their Frame Bundles|the frame-bundle theorem]]), and the equivariant-function description becomes "a section is its components in every frame, transforming tensorially". This bridge is the reason the abstract statement here is the honest generalisation of the classical component-and-transformation-law picture of tensor calculus.

- **The universal property of the quotient.** The uniqueness of $s$ in equation (36) is an instance of the universal property of the quotient map $\varpi$ (equivalently $\pi$): a smooth map out of the total space that is constant on $G$-orbits descends uniquely and smoothly to the quotient, because $\pi$ is a surjective submersion with the orbits as fibres, which is exactly what [[Thm - Free Proper Actions Give Principal Bundles|the free-proper-action theorem]] establishes. Every "descend to the base" argument in the series — including the well-definedness of the induced covariant derivative — runs through this same property.

---

# Unlocked by This

> [!tip] Induced covariant derivatives on associated bundles *(from Gauge Theory IV)*
> A connection on $P$ is a $\mathfrak g$-valued equivariant one-form $a$; through this theorem and its form-version, it induces on every associated bundle $E=P\times_\rho V$ a covariant derivative characterised upstairs by $\pi^\ast(\nabla s)=d\hat s+\rho_\ast(a)\hat s$, where $\hat s$ is the equivariant function corresponding to $s$. The equivariant-function language is what makes this single formula work uniformly across all associated bundles. See **Thm - Principal Connections Induce Covariant Derivatives on Associated Bundle**.

> [!tip] The gauge group as sections of a bundle *(from Gauge Theory V)*
> The group of gauge transformations of $P$ is identified with the sections of the associated group bundle $P\times_{\mathrm{conj}}G$, equivalently the equivariant maps $\hat g\colon P\to G$ with $\hat g(p\cdot h)=h^{-1}\hat g(p)h$; its Lie algebra is $\Gamma(\operatorname{ad}P)=C^\infty(P;\mathfrak g)^G$. This is the nonlinear and infinitesimal shadow of the present theorem, and it is how the gauge group is given a manageable description. See **Def - Gauge Transformation**.
