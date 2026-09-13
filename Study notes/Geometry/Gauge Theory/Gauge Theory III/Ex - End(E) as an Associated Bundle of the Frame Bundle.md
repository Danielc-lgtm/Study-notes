---
type: exercise
subject: gauge-theory
prereqs:
  - "Thm - Vector Bundles are Associated to Their Frame Bundles"
  - "Def - Associated Bundle"
  - "Def - Frame Bundle of a Vector Bundle"
  - "Def - Adjoint Bundles ad P and Ad P"
  - "Def - Representation of a Lie Group"
tags: [geometry, gauge-theory]
difficulty: "⭐"
---

# Problem Statement

Let $E\to M$ be a smooth real vector bundle of rank $k$, and let $\operatorname{Fr}(E)$ be its **frame bundle**, the principal $GL_k(\mathbb{R})$-bundle whose fibre over $m\in M$ is the set of linear isomorphisms $e\colon\mathbb{R}^k\to E_m$, with the right action $e\cdot h=e\circ h$ for $h\in GL_k(\mathbb{R})$. Let

$$V=\operatorname{End}(\mathbb{R}^k)=M_k(\mathbb{R})$$

be the space of $k\times k$ real matrices, regarded as a $GL_k(\mathbb{R})$-representation through **conjugation**,

$$\rho\colon GL_k(\mathbb{R})\to GL\big(\operatorname{End}(\mathbb{R}^k)\big),\qquad \rho(g)A=gAg^{-1}.$$

Following the series convention that a principal group acts on the right and that the associated-bundle action carries $\rho(g^{-1})$, form the associated vector bundle

$$\operatorname{Fr}(E)\times_\rho\operatorname{End}(\mathbb{R}^k)=\big(\operatorname{Fr}(E)\times\operatorname{End}(\mathbb{R}^k)\big)\big/GL_k(\mathbb{R}),\qquad (e,A)\cdot h=\big(e\cdot h,\ \rho(h^{-1})A\big)=\big(eh,\ h^{-1}Ah\big),$$

with classes written $[e,A]$.

**Prove** that the map

$$\Phi\colon\operatorname{Fr}(E)\times_\rho\operatorname{End}(\mathbb{R}^k)\longrightarrow\operatorname{End}(E),\qquad [e,A]\longmapsto e\circ A\circ e^{-1},$$

is a well-defined isomorphism of vector bundles over $M$, where $\operatorname{End}(E)$ is the bundle whose fibre over $m$ is the space $\operatorname{End}(E_m)$ of linear endomorphisms of $E_m$. Concretely: show that $\Phi$ is (i) independent of the choice of representative $(e,A)$ of a class, (ii) fibre-preserving over $M$, (iii) a linear isomorphism on each fibre, and (iv) smooth with smooth inverse. Conclude that

$$\operatorname{End}(E)\ \cong\ \operatorname{ad}\operatorname{Fr}(E),$$

the adjoint bundle of the frame bundle.

**Recall:**

The objects in play are the frame bundle of a vector bundle, the associated bundle of a principal bundle and a representation, a Lie-group representation, and the adjoint bundle.

![[Def - Frame Bundle of a Vector Bundle#The Definition]]

A **frame** $e$ over $m\in M$ is an ordered basis $(e_1,\dots,e_k)$ of the fibre $E_m$, equivalently the linear isomorphism $e\colon\mathbb{R}^k\to E_m$ sending the standard basis vector $\epsilon_j$ to $e_j$, so that $e(x)=\sum_{j=1}^k x_j e_j$. The right $GL_k(\mathbb{R})$-action is precomposition, $e\cdot h=e\circ h$; in components $(e\cdot h)_j=\sum_{i=1}^k h_{ij}\,e_i$. Because a frame is invertible, $(eh)^{-1}=h^{-1}e^{-1}$.

![[Def - Associated Bundle#The Definition]]

Given a principal $G$-bundle $\pi\colon P\to M$ and a representation $\rho\colon G\to GL(V)$, the [[Def - Associated Bundle|associated bundle]] $P\times_\rho V$ is the quotient of $P\times V$ by the right action $(p,v)\cdot g=(p\cdot g,\rho(g^{-1})v)$; its point over $m$ are classes $[p,v]$ with $\pi(p)=m$. The fibre over $m$ is a vector space under $[p,v]+[p,v']=[p,v+v']$ and $c\,[p,v]=[p,cv]$ — sums and scalar multiples are formed **using a common representative $p$**, and the definition is independent of that choice. For a local section $s\in\Gamma(U;P)$ the map $\psi_s^{-1}\colon U\times V\to (P\times_\rho V)|_U$, $(m,v)\mapsto[s(m),v]$, is a local trivialisation, so the associated bundle is a smooth vector bundle of rank $\dim V$.

![[Thm - Vector Bundles are Associated to Their Frame Bundles#Statement]]

This exercise supplies, in full and self-contained detail, the $\operatorname{End}(E)$ instance of part (c) of that theorem.

![[Def - Adjoint Bundles ad P and Ad P#The Definition]]

For a principal $G$-bundle $P$ with $G\subset GL_k(\mathbb{R})$ a matrix group, the **adjoint bundle** is $\operatorname{ad}P=P\times_{\operatorname{Ad}}\mathfrak{g}$, the bundle associated to $P$ by the adjoint representation $\operatorname{Ad}_g\xi=g\xi g^{-1}$ on the Lie algebra $\mathfrak{g}$. For the frame bundle the structure group is $G=GL_k(\mathbb{R})$, whose Lie algebra is $\mathfrak{gl}_k(\mathbb{R})=\operatorname{End}(\mathbb{R}^k)$ as a vector space, and its adjoint action $\operatorname{Ad}_g A=gAg^{-1}$ is exactly the representation $\rho$ above.

---

# Convergent Strategy

**Problem class.** This is a *construct-and-verify* problem: exhibit a specific candidate map between two bundles and check it against the four-clause definition of a vector-bundle isomorphism. It belongs to the family of "recover a natural bundle as an associated bundle of the frame bundle", whose paradigm cases — $E$ itself, $E^*$, $\Lambda^pE^*$, $E\otimes F$, $\operatorname{Hom}(E,F)$ — are collected in [[Thm - Vector Bundles are Associated to Their Frame Bundles|the associated-bundles theorem]]. The recurring principle is that *every functorial construction on the standard fibre $\mathbb{R}^k$ that is natural under $GL_k(\mathbb{R})$ transports to a construction on $E$*, and the transport is realised by an associated bundle.

**Assumption pattern.** The single structural fact that makes the whole verification run is that a frame $e$ *is* an isomorphism $\mathbb{R}^k\to E_m$. Every appearance of $e$ in the argument is used as an isomorphism: to conjugate a matrix into an endomorphism, to identify the standard fibre with $E_m$, and to match local trivialisations. The conjugation representation $\rho(g)A=gAg^{-1}$ is chosen precisely so that changing the frame by $h$ and conjugating the matrix by $h^{-1}$ produce the *same* endomorphism of $E_m$ — that cancellation is the content of well-definedness.

**Theorem routing.** The route is: write out the associated-bundle quotient relation $(e,A)\sim(eh,h^{-1}Ah)$; check that $e A e^{-1}$ is invariant under it, which is a two-line matrix cancellation; observe that $\Phi$ covers the identity of $M$; fix a frame in a fibre to see that $\Phi$ is fibrewise the conjugation isomorphism $A\mapsto eAe^{-1}$ of matrix algebras, hence a linear bijection; and finally pass to a local frame $\sigma$ over $U$, where the associated-bundle trivialisation and the frame trivialisation of $\operatorname{End}(E)$ turn $\Phi$ into the identity map $U\times\operatorname{End}(\mathbb{R}^k)\to U\times\operatorname{End}(\mathbb{R}^k)$, settling smoothness of $\Phi$ and of $\Phi^{-1}$ at once. The identification with $\operatorname{ad}\operatorname{Fr}(E)$ is then immediate, because $\rho$ and the adjoint representation of $GL_k(\mathbb{R})$ on $\mathfrak{gl}_k(\mathbb{R})$ are literally the same map.

**Key decision point.** The one genuinely load-bearing choice is *to compute $\Phi$ in matched trivialisations rather than by hand*. A direct estimate of smoothness of the quotient map is awkward; but the local frame $\sigma$ over $U$ gives both a trivialisation $[\sigma(m),A]\leftrightarrow(m,A)$ of the associated bundle and the matrix trivialisation $\phi\leftrightarrow\sigma(m)^{-1}\phi\,\sigma(m)$ of $\operatorname{End}(E)$, and in these two charts $\Phi$ becomes the identity. Recognising that the *same* frame trivialises both sides — so that the conjugations cancel — is what collapses the smoothness clause to a triviality.

---

# Legal Operations Used

This solution deploys the following operations, in the numbering of the topic page's Legal Operations:

1. **Read a frame as an isomorphism of the standard fibre with the bundle fibre** (operation 3 from the topic page). A frame $e$ over $m$ is used as the invertible linear map $e\colon\mathbb{R}^k\to E_m$; conjugation $A\mapsto eAe^{-1}$ transports an endomorphism of $\mathbb{R}^k$ to an endomorphism of $E_m$.

2. **Test a map on classes for well-definedness against the quotient relation** (operation 5 from the topic page). To define a map out of an associated bundle $P\times_\rho V$, one specifies it on representatives $(e,A)$ and checks invariance under $(e,A)\mapsto(eh,h^{-1}Ah)$; the check here is a matrix cancellation.

3. **Recognise a construction on $\mathbb{R}^k$ as a $GL_k(\mathbb{R})$-representation and form its associated bundle** (operation 4 from the topic page). The conjugation action on $\operatorname{End}(\mathbb{R}^k)$ is a representation; forming $\operatorname{Fr}(E)\times_\rho\operatorname{End}(\mathbb{R}^k)$ produces a bundle whose fibre models $\operatorname{End}(E_m)$.

4. **Trivialise an associated bundle from a local section of the principal bundle** (operation 6 from the topic page). A local frame $\sigma$ over $U$ is a local section of $\operatorname{Fr}(E)$; it yields the trivialisation $(m,A)\mapsto[\sigma(m),A]$.

5. **Compute a bundle map in matched trivialisations to read off smoothness** (operation 7 from the topic page). Choosing the *same* local frame to trivialise both sides turns $\Phi$ into a smooth (here, identity) map of product bundles, which is how smoothness of $\Phi$ and $\Phi^{-1}$ is established.

6. **Match a representation with the adjoint representation to identify an associated bundle with an adjoint bundle** (operation 2 from the topic page). Conjugation on $\mathfrak{gl}_k(\mathbb{R})$ *is* the adjoint action of $GL_k(\mathbb{R})$, so the associated bundle *is* $\operatorname{ad}\operatorname{Fr}(E)$.

---

# Hints

> [!note]- Hint 1
> To define $\Phi$ on a class $[e,A]$ you have chosen a representative $(e,A)$. Every other representative of the same class has the form $(eh,h^{-1}Ah)$ for some $h\in GL_k(\mathbb{R})$. Compute $(eh)(h^{-1}Ah)(eh)^{-1}$ and see what cancels.

> [!note]- Hint 2
> Fix a single frame $e$ over $m$. Then *every* class in the fibre over $m$ has exactly one representative of the form $(e,A)$, because the action moves the first coordinate freely and transitively through the fibre of $\operatorname{Fr}(E)$ over $m$. So on that fibre $\Phi$ is just $A\mapsto eAe^{-1}$. What kind of map of $\operatorname{End}(\mathbb{R}^k)$ to $\operatorname{End}(E_m)$ is conjugation by a fixed isomorphism?

> [!note]- Hint 3
> For smoothness, do not fight the quotient. Pick a local frame $\sigma=(\sigma_1,\dots,\sigma_k)$ over an open set $U$. It trivialises the associated bundle by $(m,A)\mapsto[\sigma(m),A]$. It *also* trivialises $\operatorname{End}(E)$: an endomorphism $\phi$ of $E_m$ has a matrix $\sigma(m)^{-1}\phi\,\sigma(m)$ in the basis $\sigma(m)$. Write $\Phi$ in these two charts.

> [!note]- Hint 4
> In the matched charts, $\Phi$ sends $(m,A)$ to $\sigma(m)A\sigma(m)^{-1}$, whose matrix in the frame $\sigma(m)$ is $\sigma(m)^{-1}\big(\sigma(m)A\sigma(m)^{-1}\big)\sigma(m)=A$. So $\Phi$ is the identity of $U\times\operatorname{End}(\mathbb{R}^k)$ — smooth, with smooth inverse. For the last part, compare $\rho$ with the adjoint representation of $GL_k(\mathbb{R})$ on its Lie algebra $\mathfrak{gl}_k(\mathbb{R})=\operatorname{End}(\mathbb{R}^k)$.

---

# Solution

The candidate $\Phi([e,A])=eAe^{-1}$ transports a matrix to an endomorphism of the fibre by conjugating with the frame, viewed as an isomorphism $\mathbb{R}^k\to E_m$. Well-definedness is a single matrix cancellation forced by the conjugation representation; fibrewise bijectivity is the fact that conjugation by an isomorphism is an isomorphism of endomorphism algebras; and smoothness is read off at once by trivialising both sides with the *same* local frame, in which $\Phi$ becomes the identity. The final identification is the observation that conjugation on $k\times k$ matrices is by definition the adjoint action of $GL_k(\mathbb{R})$.

**Step 0: The two fibres over $m$ and the objects to be matched.**

Before defining a map we record what lies over a point $m\in M$ on each side, so that "fibre-preserving" and "linear on fibres" have precise meaning.

> [!note]- Derivation
> On the left, a point of $\operatorname{Fr}(E)\times_\rho\operatorname{End}(\mathbb{R}^k)$ lying over $m$ is a class $[e,A]$ with $e\colon\mathbb{R}^k\to E_m$ a frame over $m$ and $A\in\operatorname{End}(\mathbb{R}^k)$, subject to
> $$[e,A]=[eh,h^{-1}Ah]\qquad\text{for every }h\in GL_k(\mathbb{R}),$$
> which is the defining relation of the [[Def - Associated Bundle|associated bundle]] under the action $(e,A)\cdot h=(eh,h^{-1}Ah)$. The fibre over $m$ is a real vector space with $[e,A]+[e,A']=[e,A+A']$ and $c[e,A]=[e,cA]$ (sums and scalar multiples taken with a *common* first coordinate $e$).
>
> On the right, the fibre of $\operatorname{End}(E)$ over $m$ is $\operatorname{End}(E_m)$, the algebra of linear maps $\phi\colon E_m\to E_m$, a real vector space of dimension $k^2$.
>
> Because a frame is an isomorphism $e\colon\mathbb{R}^k\to E_m$, the composite $eAe^{-1}$ is a linear map $E_m\to E_m$, i.e. an element of $\operatorname{End}(E_m)$. So the formula $[e,A]\mapsto eAe^{-1}$ at least *lands* in the correct fibre once we know it does not depend on the representative — which is Step 1.

**Step 1: $\Phi$ is well defined and fibre-preserving.**

The value $eAe^{-1}$ is unchanged when $(e,A)$ is replaced by another representative $(eh,h^{-1}Ah)$, and it lies in the fibre of $\operatorname{End}(E)$ over $m=\pi(e)$.

> [!note]- Derivation
> Let $(e,A)$ and $(eh,h^{-1}Ah)$ be two representatives of the same class, with $h\in GL_k(\mathbb{R})$. Apply the formula to the second and simplify:
> $$(eh)\,(h^{-1}Ah)\,(eh)^{-1}=(eh)\,(h^{-1}Ah)\,(h^{-1}e^{-1})\qquad\text{(since }(eh)^{-1}=h^{-1}e^{-1}\text{, as }e,h\text{ are invertible)}$$
> $$=e\,(hh^{-1})\,A\,(hh^{-1})\,e^{-1}\qquad\text{(regrouping the composition, associativity)}$$
> $$=e\,A\,e^{-1}\qquad\text{(since }hh^{-1}=\mathrm{id}_{\mathbb{R}^k}\text{).}$$
> Thus the two representatives give the same endomorphism, so $\Phi([e,A]):=eAe^{-1}$ is independent of the representative and $\Phi$ is a genuine map on classes. This is exactly where the **conjugation representation** $\rho(h)A=hAh^{-1}$ is used: had the action on the matrix been anything but conjugation by $h^{-1}$, the two factors of $h$ would not have cancelled.
>
> Finally $\pi(e)=m$ and $eAe^{-1}\in\operatorname{End}(E_m)$, so $\Phi$ carries the fibre over $m$ into the fibre over $m$; that is, $\Phi$ covers the identity map of $M$.

**Step 2: $\Phi$ is a linear isomorphism on each fibre.**

Fixing one frame $e$ over $m$ identifies the left fibre with $\operatorname{End}(\mathbb{R}^k)$, and $\Phi$ becomes conjugation by the isomorphism $e$, which is a linear bijection of endomorphism spaces.

> [!note]- Derivation
> Fix $m\in M$ and a single frame $e\colon\mathbb{R}^k\to E_m$ over $m$. Every class in the left fibre over $m$ has a representative with first coordinate $e$: given any $[e',A']$ over $m$, there is a unique $h\in GL_k(\mathbb{R})$ with $e'=eh$ (the fibre of $\operatorname{Fr}(E)$ over $m$ is a single free transitive $GL_k(\mathbb{R})$-orbit, by the [[Def - Frame Bundle of a Vector Bundle|frame-bundle]] axioms), whence $[e',A']=[eh,A']=[e,hA'h^{-1}]$. Moreover the representative with first coordinate exactly $e$ is unique: $[e,A]=[e,B]$ forces $A=B$, since $[e,A]=[e,B]$ means $(e,B)=(eh,h^{-1}Ah)$ for some $h$, and $eh=e$ gives $h=\mathrm{id}$ (freeness), hence $B=A$.
>
> Therefore the map $A\mapsto[e,A]$ is a linear bijection $\operatorname{End}(\mathbb{R}^k)\to (\text{left fibre over }m)$, and under it $\Phi$ becomes
> $$\Phi([e,A])=eAe^{-1}=:c_e(A),\qquad c_e\colon\operatorname{End}(\mathbb{R}^k)\to\operatorname{End}(E_m).$$
> The map $c_e$ is **linear**:
> $$c_e(A+A')=e(A+A')e^{-1}=eAe^{-1}+eA'e^{-1}=c_e(A)+c_e(A')\qquad\text{(distributivity of composition over addition of linear maps),}$$
> $$c_e(cA)=e(cA)e^{-1}=c\,eAe^{-1}=c\,c_e(A)\qquad\text{(scalars commute with composition).}$$
> It is **bijective** with inverse $\phi\mapsto e^{-1}\phi\,e$: indeed $c_e(e^{-1}\phi e)=e(e^{-1}\phi e)e^{-1}=\phi$ and $e^{-1}(eAe^{-1})e=A$ (using $e^{-1}e=\mathrm{id}$ and $ee^{-1}=\mathrm{id}_{E_m}$). Composing with the linear bijection $A\mapsto[e,A]$, we conclude that $\Phi$ restricted to the fibre over $m$ is a linear isomorphism onto $\operatorname{End}(E_m)$. As $m$ was arbitrary, $\Phi$ is a fibrewise linear isomorphism.

**Step 3: $\Phi$ and $\Phi^{-1}$ are smooth.**

Trivialising both bundles over an open set with the *same* local frame turns $\Phi$ into the identity map of a product, which is smooth in both directions.

> [!note]- Derivation
> Let $\sigma=(\sigma_1,\dots,\sigma_k)$ be a smooth local frame of $E$ over an open set $U\subseteq M$, i.e. a smooth local section $\sigma\colon U\to\operatorname{Fr}(E)$, $\sigma(m)\colon\mathbb{R}^k\to E_m$. Such $\sigma$ exists on some neighbourhood of every point because $E$ is locally trivial.
>
> *Chart on the left.* By the [[Def - Associated Bundle|associated-bundle]] construction, the local section $\sigma$ gives the trivialisation
> $$\alpha\colon U\times\operatorname{End}(\mathbb{R}^k)\to\big(\operatorname{Fr}(E)\times_\rho\operatorname{End}(\mathbb{R}^k)\big)\big|_U,\qquad (m,A)\mapsto[\sigma(m),A],$$
> a diffeomorphism onto the restricted bundle by the definition of the smooth structure on the associated bundle.
>
> *Chart on the right.* The same frame trivialises $\operatorname{End}(E)$. For $\phi\in\operatorname{End}(E_m)$ define its matrix in the basis $\sigma(m)$ by $\operatorname{mat}_\sigma(\phi):=\sigma(m)^{-1}\phi\,\sigma(m)\in\operatorname{End}(\mathbb{R}^k)$; this gives the diffeomorphism
> $$\beta\colon\operatorname{End}(E)|_U\to U\times\operatorname{End}(\mathbb{R}^k),\qquad \phi\mapsto(m,\sigma(m)^{-1}\phi\,\sigma(m)),$$
> which is smooth because the entries of $\sigma(m)^{-1}\phi\,\sigma(m)$ are smooth in $m$ and in $\phi$ (the frame $\sigma$ is smooth and matrix inversion is smooth on $GL_k(\mathbb{R})$).
>
> *Compute $\Phi$ in these charts.* For $(m,A)\in U\times\operatorname{End}(\mathbb{R}^k)$,
> $$\beta\circ\Phi\circ\alpha\,(m,A)=\beta\big(\Phi[\sigma(m),A]\big)=\beta\big(\sigma(m)A\sigma(m)^{-1}\big)\qquad\text{(definitions of }\alpha\text{ and }\Phi\text{)}$$
> $$=\Big(m,\ \sigma(m)^{-1}\big(\sigma(m)A\sigma(m)^{-1}\big)\sigma(m)\Big)\qquad\text{(definition of }\beta\text{)}$$
> $$=(m,A)\qquad\text{(the two }\sigma(m)^{-1}\sigma(m)=\mathrm{id}\text{ cancellations).}$$
> Hence $\beta\circ\Phi\circ\alpha=\mathrm{id}_{U\times\operatorname{End}(\mathbb{R}^k)}$, which is smooth, so $\Phi=\beta^{-1}\circ\mathrm{id}\circ\alpha^{-1}$ is smooth on $\operatorname{Fr}(E)\times_\rho\operatorname{End}(\mathbb{R}^k)|_U$. Since such sets $U$ cover $M$, $\Phi$ is smooth. The same identity shows $\alpha\circ\Phi^{-1}\circ\beta^{-1}=\mathrm{id}$, so $\Phi^{-1}$ is smooth as well.

**Step 4: $\operatorname{End}(E)\cong\operatorname{ad}\operatorname{Fr}(E)$.**

The representation $\rho$ *is* the adjoint representation of $GL_k(\mathbb{R})$ on its Lie algebra, so the associated bundle $\Phi$ trivialises is by definition the adjoint bundle.

> [!note]- Derivation
> The Lie algebra of $G=GL_k(\mathbb{R})$ is $\mathfrak{gl}_k(\mathbb{R})=\operatorname{End}(\mathbb{R}^k)$, the space of all $k\times k$ matrices, and its adjoint representation is $\operatorname{Ad}_g A=gAg^{-1}$ for a matrix group (series convention). This is literally the map $\rho(g)A=gAg^{-1}$ used above. By definition of the [[Def - Adjoint Bundles ad P and Ad P|adjoint bundle]],
> $$\operatorname{ad}\operatorname{Fr}(E)=\operatorname{Fr}(E)\times_{\operatorname{Ad}}\mathfrak{gl}_k(\mathbb{R})=\operatorname{Fr}(E)\times_\rho\operatorname{End}(\mathbb{R}^k).$$
> Combining this equality of bundles with Steps 1–3 gives the chain of isomorphisms
> $$\operatorname{ad}\operatorname{Fr}(E)=\operatorname{Fr}(E)\times_\rho\operatorname{End}(\mathbb{R}^k)\ \xrightarrow{\ \Phi\ }\ \operatorname{End}(E),$$
> so $\operatorname{End}(E)\cong\operatorname{ad}\operatorname{Fr}(E)$ as vector bundles over $M$. In fact $\Phi$ is fibrewise an algebra isomorphism — $c_e(AB)=eABe^{-1}=(eAe^{-1})(eBe^{-1})=c_e(A)c_e(B)$ — so it identifies the Lie-algebra-bundle structure of $\operatorname{ad}\operatorname{Fr}(E)$ (fibrewise commutator) with the commutator bracket on $\operatorname{End}(E)$.

> [!note]- Complete formal solution
> **Claim.** The map $\Phi([e,A])=eAe^{-1}$ is a well-defined vector-bundle isomorphism $\operatorname{Fr}(E)\times_\rho\operatorname{End}(\mathbb{R}^k)\xrightarrow{\ \sim\ }\operatorname{End}(E)$ over $M$, and $\operatorname{End}(E)\cong\operatorname{ad}\operatorname{Fr}(E)$.
>
> A point over $m$ on the left is a class $[e,A]$ with $e\colon\mathbb{R}^k\to E_m$ a frame and $A\in\operatorname{End}(\mathbb{R}^k)$, under the relation $[e,A]=[eh,h^{-1}Ah]$ for $h\in GL_k(\mathbb{R})$. Since $e$ is invertible, $eAe^{-1}\in\operatorname{End}(E_m)$.
>
> *Well-defined and fibre-preserving.* For any $h\in GL_k(\mathbb{R})$,
> $$(eh)(h^{-1}Ah)(eh)^{-1}=(eh)(h^{-1}Ah)(h^{-1}e^{-1})=e(hh^{-1})A(hh^{-1})e^{-1}=eAe^{-1},$$
> using $(eh)^{-1}=h^{-1}e^{-1}$ and $hh^{-1}=\mathrm{id}$; so $\Phi$ is well defined on classes and covers $\mathrm{id}_M$.
>
> *Fibrewise linear isomorphism.* Fix a frame $e$ over $m$. The fibre of $\operatorname{Fr}(E)$ over $m$ is a single free transitive $GL_k(\mathbb{R})$-orbit, so every class over $m$ is $[e,A]$ for a unique $A$, and $A\mapsto[e,A]$ is a linear bijection $\operatorname{End}(\mathbb{R}^k)\to(\text{fibre over }m)$. Under it $\Phi$ is $c_e(A)=eAe^{-1}$, which is linear (composition distributes over $+$ and commutes with scalars) and bijective with inverse $\phi\mapsto e^{-1}\phi e$. Hence $\Phi$ is a linear isomorphism on each fibre.
>
> *Smoothness.* Let $\sigma\colon U\to\operatorname{Fr}(E)$ be a smooth local frame. Then $\alpha(m,A)=[\sigma(m),A]$ trivialises the left bundle and $\beta(\phi)=(m,\sigma(m)^{-1}\phi\,\sigma(m))$ trivialises $\operatorname{End}(E)$, both diffeomorphisms. In these charts
> $$\beta\Phi\alpha(m,A)=\big(m,\ \sigma(m)^{-1}(\sigma(m)A\sigma(m)^{-1})\sigma(m)\big)=(m,A),$$
> so $\beta\Phi\alpha=\mathrm{id}$; thus $\Phi$ and $\Phi^{-1}$ are smooth over each $U$, hence globally.
>
> *Identification.* Since $\mathfrak{gl}_k(\mathbb{R})=\operatorname{End}(\mathbb{R}^k)$ and $\operatorname{Ad}_gA=gAg^{-1}=\rho(g)A$, we have $\operatorname{ad}\operatorname{Fr}(E)=\operatorname{Fr}(E)\times_\rho\operatorname{End}(\mathbb{R}^k)$, and $\Phi$ is an isomorphism onto $\operatorname{End}(E)$. Therefore $\operatorname{End}(E)\cong\operatorname{ad}\operatorname{Fr}(E)$. $\blacksquare$

> [!warning] Illegal but tempting shortcut
> It is tempting to declare $\Phi$ smooth "because it is given by a smooth formula". But $eAe^{-1}$ is a formula on *representatives* in $\operatorname{Fr}(E)\times\operatorname{End}(\mathbb{R}^k)$, not on the quotient; smoothness on the quotient is a statement about the induced map through the projection $\varpi\colon\operatorname{Fr}(E)\times\operatorname{End}(\mathbb{R}^k)\to\operatorname{Fr}(E)\times_\rho\operatorname{End}(\mathbb{R}^k)$, which requires knowing the smooth structure of the target. The legitimate route is Step 3: exhibit charts in which $\Phi$ is smooth. The shortcut would become correct only if accompanied by the remark that $\varpi$ is a smooth surjective submersion and that $eAe^{-1}$ is constant on its fibres — which is precisely Step 1 plus the submersion property, i.e. the same work.

---

# Key Takeaways

**A natural construction on the standard fibre that is equivariant under the structure group is realised as an associated bundle, and the isomorphism is always "apply the frame".** The template of this exercise recurs verbatim for $E^*$, $\Lambda^pE^*$, $E\otimes F$, $\operatorname{Hom}(E,F)$, and every tensor construction: one takes the corresponding $GL_k(\mathbb{R})$-representation on the model space (here conjugation on $\operatorname{End}(\mathbb{R}^k)$), forms the associated bundle, and defines the isomorphism to the geometric bundle by *letting the frame act as an isomorphism $\mathbb{R}^k\to E_m$*. The reusable diagnostic is: whenever a bundle is "the same construction on $E$ that some representation performs on $\mathbb{R}^k$", the map $[e,\,\text{model object}]\mapsto(\text{transport by }e)$ is the canonical isomorphism, and well-definedness is *forced* to be a cancellation because the associated-bundle action was designed to make it so. The trigger to reach for this pattern is any request to "show $E'$ is associated to $\operatorname{Fr}(E)$": identify the representation first, then the transport-by-frame map writes itself.

**The associated-bundle action carries $\rho(g^{-1})$ precisely so that transport-by-frame is representative-independent.** Notice that the entire well-definedness computation is the cancellation $(eh)(h^{-1}Ah)(eh)^{-1}=eAe^{-1}$, and the two inner factors of $h$ survive only because the matrix was conjugated by $h^{-1}$ exactly when the frame was multiplied by $h$. This is not an accident of $\operatorname{End}$; it is the reason the associated-bundle construction uses $(p,v)\cdot g=(pg,\rho(g^{-1})v)$ rather than $(pg,\rho(g)v)$. The lesson for spaced practice: if a transport-by-frame map ever fails to be well defined, the representation on the model fibre has been chosen with the wrong variance, and the fix is to replace $\rho$ by $g\mapsto\rho(g^{-1})^{\mathsf{T}}$ or its dual as the geometry demands. Understanding *why* the $g^{-1}$ is there converts a memorised formula into something one can reconstruct.

**To prove smoothness of a map between associated bundles, trivialise both sides with one section and let the conjugations cancel.** Direct verification of smoothness across a quotient is unpleasant; the efficient move, used in Step 3, is to pick a single local section (here a local frame) that trivialises *both* bundles, so that the frame appearing in the map and the frame appearing in the trivialisation of $\operatorname{End}(E)$ are the same and cancel, leaving the identity. This "one section trivialises everything in sight" tactic is the standard way to handle smoothness for associated, adjoint, and endomorphism bundles, and it also exposes the *transition functions*: the frame trivialisations of $\operatorname{End}(E)$ change by $A\mapsto (g_{UV})A(g_{UV})^{-1}$ across overlaps, which is again $\rho$ applied to the cocycle of $\operatorname{Fr}(E)$ — confirming from the transition-function side that $\operatorname{End}(E)$ is the associated bundle. This exercise is the concrete companion to [[Ex - The Tautological Line Bundle over CP^n is Associated to the Hopf Bundle]], where the same "trivialise with a local section" tactic settles smoothness for a line bundle over projective space.
