---
type: exercise
subject: gauge-theory
difficulty: "⭐"
prereqs:
  - "Def - Adjoint Bundles ad P and Ad P"
  - "Def - Associated Bundle"
  - "Def - Principal G-Bundle"
  - "Def - Adjoint Representation"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $\pi\colon P\to M$ be a **principal $G$-bundle** with structure group $G$ **abelian** (that is, $gh=hg$ for all $g,h\in G$), and let $\mathfrak{g}=T_eG$ be its Lie algebra. Recall the two adjoint bundles built from $P$:
$$\operatorname{ad}P:=P\times_{\operatorname{Ad}}\mathfrak{g}=(P\times\mathfrak{g})/G,\qquad\operatorname{Ad}P:=P\times_{\alpha}G=(P\times G)/G,$$
where $\operatorname{Ad}\colon G\to GL(\mathfrak{g})$ is the adjoint representation and $\alpha\colon G\to\operatorname{Aut}(G)$, $\alpha_g(h)=ghg^{-1}$, is the conjugation action of $G$ on itself. The equivalence relation in both quotients is the right $G$-action $(p,v)\cdot g=(p\cdot g,\rho(g^{-1})v)$ for the relevant representation $\rho$ (namely $\operatorname{Ad}$ and $\alpha$), with equivalence classes written $[p,v]$; the fibres of $\operatorname{Ad}P$ carry the group multiplication $[p,h]\cdot[p,h']=[p,hh']$.

Prove:

1. **The adjoint representation is trivial.** $\operatorname{Ad}_g=\operatorname{id}_{\mathfrak{g}}$ for every $g\in G$, and the conjugation action $\alpha_g=\operatorname{id}_G$ for every $g$.
2. **Both adjoint bundles are canonically trivial.** $\operatorname{ad}P\cong M\times\mathfrak{g}$ as vector bundles, and $\operatorname{Ad}P\cong M\times G$ as bundles of groups, by canonical isomorphisms requiring no choice of local section.
3. **Sections are ordinary functions.** $\Gamma(\operatorname{ad}P)\cong C^\infty(M;\mathfrak{g})$ and $\Gamma(\operatorname{Ad}P)\cong C^\infty(M;G)$, the latter an isomorphism of groups.
4. **Gauge transformations of an abelian bundle (recovering Bär, Example 2.7.5).** Every smooth map $g\colon M\to G$ determines a gauge transformation $f(p)=p\cdot g(\pi(p))$, and under the standard identification of the gauge group with $\Gamma(\operatorname{Ad}P)$ these are all of them, so the gauge group of an abelian bundle is $C^\infty(M;G)$.

**Recall:**

The objects in play are the associated bundle construction, the two adjoint bundles $\operatorname{ad}P$ and $\operatorname{Ad}P$, the adjoint representation, and the notion of a trivial (product) bundle.

![[Def - Associated Bundle#The Definition]]

Given a [[Def - Principal G-Bundle|principal $G$-bundle]] $P\to M$ and a representation $\rho\colon G\to GL(V)$, the [[Def - Associated Bundle|associated bundle]] is $P\times_\rho V=(P\times V)/G$ with $(p,v)\sim(p\cdot g,\rho(g^{-1})v)$; class $[p,v]$. Its fibre over $m$ is $\{[p,v]:v\in V\}$ for any chosen $p\in\pi^{-1}(m)$, and the map $v\mapsto[p,v]$ is a vector-space isomorphism $V\to(P\times_\rho V)_m$. The relation rearranges to
$$[p\cdot g,w]=[p,\rho(g)w]\qquad(g\in G,\ w\in V),$$
and for a local section $s\colon U\to P$ the map $\tau_s\colon U\times V\to (P\times_\rho V)|_U$, $\tau_s(m,v)=[s(m),v]$, is a smooth local trivialisation with smooth inverse.

![[Def - Adjoint Bundles ad P and Ad P#The Definition]]

The [[Def - Adjoint Bundles ad P and Ad P|adjoint vector bundle]] $\operatorname{ad}P=P\times_{\operatorname{Ad}}\mathfrak{g}$ is the associated bundle for $\rho=\operatorname{Ad}$; the [[Def - Adjoint Bundles ad P and Ad P|adjoint group bundle]] $\operatorname{Ad}P=P\times_\alpha G$ is the associated *fibre bundle of groups* for the conjugation action $\alpha$, with fibrewise multiplication $[p,h][p,h']=[p,hh']$ (well defined because $\alpha$ is by group automorphisms) and each fibre isomorphic to $G$; $\Gamma(\operatorname{Ad}P)$ is a group under pointwise multiplication.

The one representation-theoretic fact needed is the definition of $\operatorname{Ad}$.

![[Def - Adjoint Representation#The Definition]]

The [[Def - Adjoint Representation|adjoint representation]] is $\operatorname{Ad}\colon G\to GL(\mathfrak{g})$, $\operatorname{Ad}_g=d_e c_g$, the differential at the identity of the conjugation map $c_g=\alpha_g\colon G\to G$, $c_g(h)=ghg^{-1}$. For a matrix group $G\subseteq GL_k$ one has $\operatorname{Ad}_g\xi=g\xi g^{-1}$.

Finally, a **trivial** (or **product**) bundle over $M$ with fibre $F$ is $M\times F$ with projection $\operatorname{pr}_M$; a section of $M\times F$ is exactly a smooth map $m\mapsto(m,\varphi(m))$, i.e. a smooth $\varphi\colon M\to F$, so $\Gamma(M\times F)\cong C^\infty(M;F)$.

---

# Convergent Strategy

**Problem class.** This is a *degenerate-case collapse* problem: a general construction (the associated bundle, which twists the fibre by a representation as one moves along a fibre of $P$) is fed a hypothesis (abelian $G$) that makes the twist trivial, and the task is to show the construction collapses to the untwisted product. Such problems are won by isolating the *single quantity that carries the nontriviality* — here, the representation $\rho$ appearing in the equivalence relation — showing the hypothesis kills it, and then invoking a general "trivial representation gives trivial associated bundle" lemma.

**Assumption pattern.** The abelian hypothesis is used in exactly one place and in exactly one way: it makes conjugation $c_g$ the identity map of $G$, hence makes both $\alpha_g=\operatorname{id}_G$ and its differential $\operatorname{Ad}_g=\operatorname{id}_{\mathfrak{g}}$. Every subsequent step is representation-independent bookkeeping. The recognisable trigger is that the bundles in question are associated to $P$ *via conjugation*, and "abelian" is precisely the statement that conjugation is trivial.

**Theorem routing.** The route is: (i) prove $\operatorname{Ad}_g=\operatorname{id}$ and $\alpha_g=\operatorname{id}$ directly from commutativity; (ii) prove once, as a lemma, that if $\rho$ is the *trivial* representation then $P\times_\rho V\cong M\times V$ canonically, checking well-definedness, bijectivity, and smoothness in both directions through the [[Def - Associated Bundle|local trivialisations]] $\tau_s$; (iii) apply the lemma to $\rho=\operatorname{Ad}$ (vector-bundle version) and to $\alpha$ (group-bundle version, additionally checking the isomorphism respects fibrewise multiplication); (iv) read off sections; (v) specialise to the gauge group.

**Key decision point.** The only decision with any content is to prove the *trivial-representation lemma* in general rather than to manipulate $\operatorname{ad}P$ and $\operatorname{Ad}P$ by hand. Both bundles are instances of one construction differing only in the fibre ($\mathfrak{g}$ versus $G$) and in what extra structure (linear versus group) must be preserved; proving the collapse once, cleanly, and then applying it twice avoids repeating the well-definedness and smoothness checks and makes transparent that the *same* mechanism trivialises both. The second, subtler point is that the resulting trivialisation is *canonical* — it does not depend on choosing a section of $P$, even though $P$ itself may be nontrivial — because the trivial representation makes the class $[p,v]$ independent of which $p$ over a given base point is used.

---

# Legal Operations Used

The solution deploys the following operations; where the §3.4 topic page numbers its Legal Operations, these correspond to the operations for computing an associated bundle from its representation and for recognising a trivial associated bundle.

1. **Reduce the adjoint action to conjugation and kill it with commutativity.** Since $\operatorname{Ad}_g=d_ec_g$ and $c_g(h)=ghg^{-1}=h$ when $G$ is abelian, $c_g=\operatorname{id}_G$ and hence $\operatorname{Ad}_g=d_e(\operatorname{id}_G)=\operatorname{id}_{\mathfrak{g}}$.

2. **Recognise a bundle associated to a trivial representation as a product.** When $\rho(g)=\operatorname{id}_V$ for all $g$, the equivalence $[p,v]=[p\cdot g,v]$ shows the class depends only on $\pi(p)$ and $v$, so $[p,v]\mapsto(\pi(p),v)$ is a well-defined isomorphism onto $M\times V$.

3. **Transport extra fibre structure across the isomorphism.** For $\operatorname{ad}P$ the map is fibrewise linear; for $\operatorname{Ad}P$ it additionally sends $[p,h][p,h']=[p,hh']$ to $(m,h)(m,h')=(m,hh')$, so it is a fibrewise group isomorphism.

4. **Verify smoothness through the associated-bundle local trivialisations.** Composing the candidate isomorphism with $\tau_s(m,v)=[s(m),v]$ yields the identity of $U\times V$, which is smooth, and exhibits the inverse as $\tau_s$; hence the isomorphism is a diffeomorphism.

5. **Read sections of a product bundle as functions.** $\Gamma(M\times F)=C^\infty(M;F)$, transported back through the isomorphisms to $\Gamma(\operatorname{ad}P)$ and $\Gamma(\operatorname{Ad}P)$.

---

# Hints

> [!note]- Hint 1
> Every nontrivial feature of $\operatorname{ad}P$ and $\operatorname{Ad}P$ enters through the representation used to glue the fibres — the adjoint representation $\operatorname{Ad}$ for the first, the conjugation action $\alpha$ for the second. Compute both when $G$ is abelian. What is $ghg^{-1}$ when $g$ and $h$ commute?

> [!note]- Hint 2
> Once you know $\operatorname{Ad}_g=\operatorname{id}_{\mathfrak{g}}$ and $\alpha_g=\operatorname{id}_G$, both bundles are associated to $P$ via a *trivial* representation. Prove a single lemma: if $\rho\colon G\to GL(V)$ is trivial then $P\times_\rho V\cong M\times V$. What does the equivalence relation $[p,v]=[p\cdot g,\rho(g^{-1})v]$ become when $\rho(g^{-1})=\operatorname{id}$?

> [!note]- Hint 3
> The candidate map is $\Phi([p,v])=(\pi(p),v)$. Check it is well defined (independent of the representative $(p,v)$), bijective, and — using transitivity of $G$ on fibres — that its inverse over a base point $m$ sends $(m,v)$ to $[p,v]$ for any $p\in\pi^{-1}(m)$. For smoothness, compose $\Phi$ with the associated-bundle trivialisation $\tau_s(m,v)=[s(m),v]$ over a trivialising open set.

> [!note]- Hint 4
> For $\operatorname{Ad}P$ you must additionally check $\Phi$ preserves the fibrewise group law: $\Phi([p,h][p,h'])=\Phi([p,hh'])=(m,hh')$. For part 4, verify directly that $f(p):=p\cdot g(\pi(p))$ is a gauge transformation — the abelian law is exactly what makes $f(p\cdot h)=f(p)\cdot h$ hold — and cite the identification $\mathcal{G}(P)\cong\Gamma(\operatorname{Ad}P)\cong C^\infty(M;G)$ for the converse.

---

# Solution

The argument has one idea and four verifications. The idea is that the adjoint bundles are built by twisting a fixed fibre ($\mathfrak{g}$ or $G$) with conjugation as one slides along a fibre of $P$, and for an abelian group conjugation does nothing, so no twisting occurs and the bundle is a product. The verifications are: that conjugation is trivial (Step 1), that a trivially-twisted associated bundle is a product (Step 2, proved once and reused), that the two bundles satisfy the lemma's hypotheses with their extra structure preserved (Step 3), and that this reads off on sections and on the gauge group (Steps 4–5).

**Step 1: For abelian $G$, conjugation and the adjoint representation are trivial.**

We show $\alpha_g=\operatorname{id}_G$ and $\operatorname{Ad}_g=\operatorname{id}_{\mathfrak{g}}$ for every $g\in G$.

> [!note]- Derivation
> Let $g\in G$. The conjugation automorphism is $\alpha_g=c_g\colon G\to G$, $c_g(h)=ghg^{-1}$. Because $G$ is **abelian**, $gh=hg$, so
> $$c_g(h)=ghg^{-1}=hgg^{-1}=h\qquad\text{for all }h\in G\qquad\text{(commutativity }gh=hg\text{).}$$
> Hence $c_g=\alpha_g=\operatorname{id}_G$, the identity map of $G$.
>
> The [[Def - Adjoint Representation|adjoint representation]] is $\operatorname{Ad}_g=d_ec_g$, the differential at $e$ of $c_g$. Since $c_g=\operatorname{id}_G$ and the differential of the identity map is the identity linear map,
> $$\operatorname{Ad}_g=d_e(\operatorname{id}_G)=\operatorname{id}_{T_eG}=\operatorname{id}_{\mathfrak{g}}\qquad\text{(differential of the identity is the identity).}$$
>
> **Concrete check (matrix / $U(1)$ case).** If $G\subseteq GL_k$ is a matrix group then $\operatorname{Ad}_g\xi=g\xi g^{-1}$. For abelian $G$ the group elements commute; differentiating $g\exp(t\xi)g^{-1}=\exp(t\xi)$ (valid because $\exp(t\xi)\in G$ commutes with $g$) at $t=0$ gives $g\xi g^{-1}=\xi$, i.e. $\operatorname{Ad}_g=\operatorname{id}$. For the simplest instance $G=U(1)$, with $g=\lambda\in U(1)\subset\mathbb{C}^\times$ and $\xi\in\mathfrak{u}(1)=i\mathbb{R}$, one has $\operatorname{Ad}_\lambda\xi=\lambda\xi\lambda^{-1}=\xi$ since complex scalars commute — consistent with the general statement.

**Step 2: A bundle associated to a trivial representation is canonically a product.**

We prove the lemma once, for an arbitrary representation that happens to be trivial, and apply it twice in Step 3.

> [!note]- Derivation
> **Lemma.** Let $P\to M$ be a principal $G$-bundle and $\rho\colon G\to GL(V)$ a representation with $\rho(g)=\operatorname{id}_V$ for all $g\in G$. Then
> $$\Phi\colon P\times_\rho V\longrightarrow M\times V,\qquad\Phi([p,v])=(\pi(p),v),$$
> is a well-defined isomorphism of vector bundles.
>
> **Well-defined.** Two pairs represent the same class iff $(p',v')=(p\cdot g,\rho(g^{-1})v)$ for some $g$. Then, using $\rho(g^{-1})=\operatorname{id}_V$ and $\pi(p\cdot g)=\pi(p)$ (fibre-preservation),
> $$\Phi([p',v'])=(\pi(p\cdot g),\rho(g^{-1})v)=(\pi(p),v)=\Phi([p,v])\qquad\text{(triviality of }\rho\text{; fibre-preservation).}$$
> So $\Phi$ does not depend on the representative; it is well defined.
>
> **Bijective.** *Injective:* suppose $\Phi([p,v])=\Phi([p',v'])$, i.e. $\pi(p)=\pi(p')=:m$ and $v=v'$. Since $G$ acts **transitively** on the fibre over $m$, there is $g\in G$ with $p'=p\cdot g$; then, using the rearranged relation $[p\cdot g,w]=[p,\rho(g)w]$ with $\rho(g)=\operatorname{id}$,
> $$[p',v']=[p\cdot g,v]=[p,\rho(g)v]=[p,v]\qquad\text{(transitivity; triviality of }\rho\text{),}$$
> so the two classes coincide. *Surjective:* given $(m,v)\in M\times V$, choose any $p\in\pi^{-1}(m)$ (nonempty since $\pi$ is surjective); then $\Phi([p,v])=(m,v)$.
>
> **Fibrewise linear.** Over $m$, the fibre of $P\times_\rho V$ is $\{[p,v]:v\in V\}$ for a fixed $p\in\pi^{-1}(m)$, with vector-space operations $[p,v]+[p,w]=[p,v+w]$ and $\lambda[p,v]=[p,\lambda v]$ (the [[Def - Associated Bundle|associated-bundle fibre structure]]). Then $\Phi([p,v]+[p,w])=\Phi([p,v+w])=(m,v+w)=(m,v)+(m,w)$, and similarly for scalars, so $\Phi_m$ is linear; being a linear bijection $V\to V$ (in the second coordinate), it is a linear isomorphism.
>
> **Smooth in both directions.** Let $s\colon U\to P$ be a local section over a trivialising open set $U\subseteq M$; the [[Def - Associated Bundle|associated-bundle local trivialisation]] $\tau_s\colon U\times V\to(P\times_\rho V)|_U$, $\tau_s(m,v)=[s(m),v]$, is a diffeomorphism. Composing,
> $$(\Phi\circ\tau_s)(m,v)=\Phi([s(m),v])=(\pi(s(m)),v)=(m,v),$$
> because $\pi\circ s=\operatorname{id}_U$. Thus $\Phi\circ\tau_s=\operatorname{id}_{U\times V}$, which is smooth; and $\Phi|_U=\tau_s^{-1}$, while $(\Phi|_U)^{-1}=\tau_s$ is smooth. As $M$ is covered by such $U$, $\Phi$ is a diffeomorphism. Together with fibrewise linearity and $\operatorname{pr}_M\circ\Phi=\pi$ (covering $\operatorname{id}_M$), $\Phi$ is an isomorphism of vector bundles. Moreover $\Phi$ used *no* choice of section in its definition, so it is **canonical**. $\square$

**Step 3: Apply the lemma to $\operatorname{ad}P$ and $\operatorname{Ad}P$.**

We deduce $\operatorname{ad}P\cong M\times\mathfrak{g}$ and $\operatorname{Ad}P\cong M\times G$.

> [!note]- Derivation
> **The vector bundle $\operatorname{ad}P$.** By definition $\operatorname{ad}P=P\times_{\operatorname{Ad}}\mathfrak{g}$, the associated bundle for $\rho=\operatorname{Ad}$ on $V=\mathfrak{g}$. By **Step 1**, $\operatorname{Ad}_g=\operatorname{id}_{\mathfrak{g}}$ for all $g$, so $\operatorname{Ad}$ is the trivial representation on $\mathfrak{g}$. The **Lemma of Step 2** applies verbatim and gives a canonical vector-bundle isomorphism
> $$\Phi\colon\operatorname{ad}P\xrightarrow{\ \sim\ }M\times\mathfrak{g},\qquad\Phi([p,\xi])=(\pi(p),\xi).$$
>
> **The group bundle $\operatorname{Ad}P$.** By definition $\operatorname{Ad}P=P\times_\alpha G$, associated to the conjugation action $\alpha$ on the manifold $G$. By **Step 1**, $\alpha_g=\operatorname{id}_G$ for all $g$, so $\alpha$ is the trivial action. The set-and-smoothness content of the Lemma of Step 2 applies with $V$ replaced by the manifold $G$ (linearity is not asserted, only that $\Phi([p,h])=(\pi(p),h)$ is a well-defined diffeomorphism onto $M\times G$ — the well-definedness, bijectivity, and smoothness arguments used only that the representation is trivial and that $\tau_s$ is a diffeomorphism, both of which hold here). It remains to check that $\Phi$ respects the **fibrewise group structure**. Over $m=\pi(p)$, using the multiplication $[p,h][p,h']=[p,hh']$,
> $$\Phi\big([p,h]\cdot[p,h']\big)=\Phi([p,hh'])=(m,hh')=(m,h)\cdot(m,h')=\Phi([p,h])\cdot\Phi([p,h']),$$
> where $M\times G$ carries the fibrewise product $(m,h)(m,h')=(m,hh')$. Hence $\Phi$ is an isomorphism of bundles of groups,
> $$\operatorname{Ad}P\cong M\times G.$$
> Both isomorphisms are canonical, requiring no section of $P$, even when $P$ itself is a nontrivial principal bundle.

**Step 4: Sections are ordinary functions.**

We read off $\Gamma(\operatorname{ad}P)\cong C^\infty(M;\mathfrak{g})$ and $\Gamma(\operatorname{Ad}P)\cong C^\infty(M;G)$.

> [!note]- Derivation
> A section of the product bundle $M\times F$ is a smooth map $\sigma\colon M\to M\times F$ with $\operatorname{pr}_M\circ\sigma=\operatorname{id}_M$, hence of the form $\sigma(m)=(m,\varphi(m))$ for a unique smooth $\varphi\colon M\to F$; conversely each such $\varphi$ gives a section. Thus $\Gamma(M\times F)\cong C^\infty(M;F)$. Transporting through the isomorphisms of **Step 3**,
> $$\Gamma(\operatorname{ad}P)\cong\Gamma(M\times\mathfrak{g})\cong C^\infty(M;\mathfrak{g}),\qquad\Gamma(\operatorname{Ad}P)\cong\Gamma(M\times G)\cong C^\infty(M;G).$$
> The second is an isomorphism of **groups**: pointwise multiplication of sections of $\operatorname{Ad}P$ corresponds under $\Phi$ to pointwise multiplication of $G$-valued functions, since $\Phi$ is a fibrewise group isomorphism (Step 3). Concretely, a section of $\operatorname{ad}P$ is a smooth $\mathfrak{g}$-valued function on $M$, and a section of $\operatorname{Ad}P$ is a smooth $G$-valued function on $M$.

**Step 5: The gauge group of an abelian bundle is $C^\infty(M;G)$.**

We verify the construction $f(p)=p\cdot g(\pi(p))$ gives a gauge transformation and record the converse.

> [!note]- Derivation
> Let $g\colon M\to G$ be smooth and define $f\colon P\to P$ by $f(p):=p\cdot g(\pi(p))$. This is smooth (a composition of the smooth action with the smooth map $p\mapsto(p,g(\pi(p)))$), and it covers $\operatorname{id}_M$ because $\pi(f(p))=\pi(p\cdot g(\pi(p)))=\pi(p)$ (fibre-preservation). It is $G$-equivariant: for $h\in G$,
> $$f(p\cdot h)=(p\cdot h)\cdot g(\pi(p\cdot h))=(p\cdot h)\cdot g(\pi(p))=p\cdot\big(h\,g(\pi(p))\big)=p\cdot\big(g(\pi(p))\,h\big)=f(p)\cdot h,$$
> where $\pi(p\cdot h)=\pi(p)$ was used, then associativity of the action, and then the **abelian law** $h\,g(\pi(p))=g(\pi(p))\,h$ — this is the one and only place commutativity of $G$ is needed for the construction. Its inverse is $p\mapsto p\cdot g(\pi(p))^{-1}$, so $f$ is a diffeomorphism. Hence $f$ is a [[Def - Gauge Transformation|gauge transformation]] of $P$.
>
> For the converse — that *every* gauge transformation of an abelian bundle arises this way — recall the general identification of the [[Def - Gauge Transformation|gauge group]] with sections of the adjoint group bundle, $\mathcal{G}(P)\cong\Gamma(\operatorname{Ad}P)$, developed in **Gauge Theory V**. Composing it with **Step 4**,
> $$\mathcal{G}(P)\cong\Gamma(\operatorname{Ad}P)\cong C^\infty(M;G),$$
> and unwinding the identification sends a smooth $g\colon M\to G$ to the gauge transformation $f(p)=p\cdot g(\pi(p))$ just constructed. So for abelian $G$ these exhaust the gauge group. This recovers Bär's Example 2.7.5 (and its remark that for non-abelian $G$ the same formula gives a gauge transformation only when $g$ takes values in the centre $Z(G)$, precisely because the abelian law above then fails outside $Z(G)$).

> [!note]- Complete formal solution
> **Claim.** For a principal $G$-bundle $P\to M$ with $G$ abelian, $\operatorname{ad}P\cong M\times\mathfrak{g}$ canonically as vector bundles, $\operatorname{Ad}P\cong M\times G$ canonically as group bundles, $\Gamma(\operatorname{ad}P)\cong C^\infty(M;\mathfrak{g})$ and $\Gamma(\operatorname{Ad}P)\cong C^\infty(M;G)$ (the latter as groups), and $\mathcal{G}(P)\cong C^\infty(M;G)$.
>
> *Triviality of conjugation.* For abelian $G$ and any $g$, $c_g(h)=ghg^{-1}=h$, so $\alpha_g=c_g=\operatorname{id}_G$ and $\operatorname{Ad}_g=d_ec_g=\operatorname{id}_{\mathfrak{g}}$.
>
> *Trivial-representation lemma.* If $\rho\colon G\to GL(V)$ is trivial, then $\Phi([p,v])=(\pi(p),v)$ is a well-defined bijection $P\times_\rho V\to M\times V$: well-defined because $[p,v]=[p\cdot g,v]$ (as $\rho(g^{-1})=\operatorname{id}$) and $\pi(p\cdot g)=\pi(p)$; injective because equal images give $p'=p\cdot g$ (transitivity) and then $[p',v]=[p\cdot g,v]=[p,v]$; surjective because $\pi$ is onto. It is fibrewise linear and, via a local section $s$, satisfies $\Phi\circ\tau_s=\operatorname{id}_{U\times V}$, so it is a smooth vector-bundle isomorphism, defined without any section.
>
> *Application.* $\operatorname{ad}P=P\times_{\operatorname{Ad}}\mathfrak{g}$ with $\operatorname{Ad}$ trivial gives $\operatorname{ad}P\cong M\times\mathfrak{g}$. $\operatorname{Ad}P=P\times_\alpha G$ with $\alpha$ trivial gives, by the same well-definedness/bijectivity/smoothness argument, $\Phi([p,h])=(\pi(p),h)$ a diffeomorphism onto $M\times G$; it respects fibrewise products, $\Phi([p,h][p,h'])=\Phi([p,hh'])=(m,hh')=\Phi([p,h])\Phi([p,h'])$, so $\operatorname{Ad}P\cong M\times G$ as group bundles.
>
> *Sections.* $\Gamma(M\times F)\cong C^\infty(M;F)$, so $\Gamma(\operatorname{ad}P)\cong C^\infty(M;\mathfrak{g})$ and $\Gamma(\operatorname{Ad}P)\cong C^\infty(M;G)$, the latter as groups (pointwise multiplication corresponds under the fibrewise group isomorphism $\Phi$).
>
> *Gauge group.* Each smooth $g\colon M\to G$ gives $f(p)=p\cdot g(\pi(p))$, which covers $\operatorname{id}_M$ and is $G$-equivariant because $f(p\cdot h)=p\cdot h\,g(\pi(p))=p\cdot g(\pi(p))\,h=f(p)\cdot h$ using the abelian law; so $f\in\mathcal{G}(P)$. By the identification $\mathcal{G}(P)\cong\Gamma(\operatorname{Ad}P)$ (chapter V) and the above, $\mathcal{G}(P)\cong C^\infty(M;G)$, and these are all gauge transformations. $\blacksquare$

> [!warning] Illegal but tempting shortcut
> It is tempting to say "$P$ trivialises because $\operatorname{ad}P$ and $\operatorname{Ad}P$ do." This is **false**: an abelian principal bundle need not be trivial — the Hopf bundle $S^3\to S^2$ is a nontrivial $U(1)$-bundle, yet $U(1)$ is abelian, so by this exercise its adjoint bundles $\operatorname{ad}P=S^2\times i\mathbb{R}$ and $\operatorname{Ad}P=S^2\times U(1)$ are trivial while $P$ is not. The triviality of the adjoint bundles reflects only the triviality of the *conjugation* action, which forgets everything about how the fibres of $P$ are glued together globally; it says nothing about the triviality of $P$ as a principal bundle. The extra condition that *would* make $P$ trivial is the existence of a global section, an entirely separate matter.

---

# Key Takeaways

**In an associated bundle, all the twisting lives in the representation; kill the representation and the bundle is a product.** The associated bundle $P\times_\rho V$ glues copies of $V$ along the fibres of $P$ using $\rho$ to reconcile different choices of point $p$ over the same base point: the class $[p,v]$ equals $[p\cdot g,\rho(g^{-1})v]$, so moving from $p$ to $p\cdot g$ *relabels* $v$ by $\rho(g^{-1})$. This relabelling is the sole source of nontriviality contributed by the representation (the base bundle $P$ contributes its own, separately). When $\rho$ is trivial the relabelling is the identity, the class depends only on $(\pi(p),v)$, and the bundle is canonically $M\times V$. The reusable diagnostic: whenever a bundle is presented as $P\times_\rho V$ and you can show $\rho$ is trivial on the whole group — because $G$ is abelian, or because $\rho$ factors through the trivial quotient, or because the relevant elements act as scalars that cancel — conclude *immediately* that the bundle is a canonical product, and note that the trivialisation needs no section of $P$. This is the exact mechanism by which, for a $U(1)$-bundle, the curvature and the gauge potential become genuine $\mathbb{R}$-valued (rather than $\operatorname{ad}P$-valued) two- and one-forms on the base, which is what makes abelian gauge theory — electromagnetism — so much simpler than the non-abelian case.

**Abelian means conjugation is trivial, and conjugation is the only way the group ever acts on itself and on its Lie algebra in these constructions.** The single hypothesis does all the work through one identity, $ghg^{-1}=h$, which trivialises the conjugation action $\alpha$ and its derivative $\operatorname{Ad}$ in one stroke. It is worth internalising that $\operatorname{ad}P$ and $\operatorname{Ad}P$ are built *only* from conjugation data: $\operatorname{ad}P$ from $\operatorname{Ad}=d_e(\text{conjugation})$, and $\operatorname{Ad}P$ from conjugation itself. So "abelian" is not merely one convenient hypothesis among many — it is precisely the hypothesis these two bundles are designed to detect the failure of. The general trigger for spaced practice: when a construction is manifestly built from the adjoint representation or from inner automorphisms, the abelian case is always the trivial case, and the *size of the deviation from triviality* in the non-abelian case is measured by exactly how far $\operatorname{Ad}$ is from the identity — which is the infinitesimal statement $\operatorname{ad}_\xi\eta=[\xi,\eta]$, the Lie bracket. This is the same collapse seen in the companion **[[Ex - Vertical Vectors are Exactly the Fundamental Vector Fields]]**, whose closing remark shows the vertical bundle assembles into $\operatorname{ad}P$ precisely because of the $\operatorname{Ad}$-twist; here that twist is switched off.

**Trivial adjoint bundles do not imply a trivial principal bundle: the two triviality questions are independent.** It is a common and costly error to slide from "$\operatorname{ad}P$ and $\operatorname{Ad}P$ are trivial" to "$P$ is trivial." The Hopf bundle is the standing counterexample: it is a nontrivial $U(1)$-bundle over $S^2$, yet abelian, so its adjoint bundles are products while $P$ has no global section. The reason the implication fails is structural: the adjoint bundles remember only the conjugation action, which for an abelian group is blind to the global gluing of $P$; triviality of $P$ is instead equivalent to the existence of a global section, a genuinely stronger and unrelated condition. The transferable principle is to keep separate the two axes along which a principal bundle can be simple — the *structure group's internal geometry* (abelian, semisimple, and so on), which controls the associated tensor bundles, and the *global topology of $P$* (its characteristic classes, whether it has sections), which controls $P$ itself. Abelian structure groups make the first axis trivial while leaving the second — the entire content of the classification of $U(1)$-bundles by the first Chern class — completely intact.
