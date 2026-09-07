---
type: exercise
subject: gauge-theory
prereqs:
  - "Def - Operations on Vector Bundles and Pull-Back Bundles"
  - "Def - The Tangent Bundle"
  - "Def - Velocity of a Curve"
  - "Def - Section of a Vector Bundle"
difficulty: "⭐"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $B$ be a smooth manifold and let $\lambda\colon(-\epsilon,\epsilon)\to B$ be a smooth curve. Form the **pull-back of the tangent bundle along $\lambda$**, written $\lambda^{*}TB\to(-\epsilon,\epsilon)$: the vector bundle over the interval $(-\epsilon,\epsilon)$ whose fibre over $t$ is the tangent space $T_{\lambda(t)}B$. Prove the following identification and its consequence.

$$\Gamma(\lambda^{*}TB)\;\cong\;\bigl\{\,V\colon(-\epsilon,\epsilon)\to TB\ \text{ smooth}\ \bigl|\ V(t)\in T_{\lambda(t)}B\ \text{ for all } t\,\bigr\}.$$

That is:

1. Every smooth section $\sigma$ of $\lambda^{*}TB$ determines a smooth map $V\colon(-\epsilon,\epsilon)\to TB$ with $V(t)\in T_{\lambda(t)}B$ for all $t$ (a **vector field along $\lambda$**), and conversely; and these two assignments are mutually inverse, so sections of $\lambda^{*}TB$ are exactly the vector fields along $\lambda$.
2. The **velocity field** $\dot\lambda$ of the curve, $\dot\lambda(t):=d\lambda_{t}\bigl(\partial_{t}|_{t}\bigr)\in T_{\lambda(t)}B$, is one such vector field, hence a distinguished section of $\lambda^{*}TB$.

This is Example 2.1.12 of Bär's lecture notes (item B-E2.1.6). The right-hand side is the object one usually writes down by hand — a curve of tangent vectors based along the moving point $\lambda(t)$ — and the content of the exercise is that this hand-made object is precisely a section of a bundle we already know how to build, namely the pull-back. Once this is established, the whole apparatus of covariant differentiation, parallel transport, and the geodesic and Jacobi equations becomes available for vector fields along curves without any separate foundation.

**Recall.**

The objects in play are the pull-back bundle of a vector bundle along a smooth map, the tangent bundle and its projection, a section of a vector bundle, the velocity of a curve, and (for the smoothness bookkeeping) the local frame of a vector bundle.

![[Def - Operations on Vector Bundles and Pull-Back Bundles#The Definition]]

For a smooth map $f\colon M'\to M$ and a vector bundle $\pi\colon E\to M$, the [[Def - Operations on Vector Bundles and Pull-Back Bundles|pull-back bundle]] $f^{*}E\to M'$ has fibre $(f^{*}E)_{m'}=E_{f(m')}$; concretely it is the fibre-product submanifold
$$f^{*}E=\bigl\{(m',e)\in M'\times E\ \bigl|\ f(m')=\pi(e)\bigr\},\qquad \pi'=\operatorname{pr}_{1}|_{f^{*}E}\colon f^{*}E\to M',$$
and $\operatorname{pr}_{2}\colon f^{*}E\to E$ restricts on each fibre to the linear isomorphism $(f^{*}E)_{m'}\xrightarrow{\ \sim\ }E_{f(m')}$. Over any open $U\subseteq M$ on which $E$ has a [[Def - Local Frame|local frame]] $e=(e_{1},\dots,e_{k})$, the bundle $f^{*}E$ has, over $U':=f^{-1}(U)$, the pulled-back local frame $\bar e=(\bar e_{1},\dots,\bar e_{k})$ with $\bar e_{j}(m')=\bigl(m',e_{j}(f(m'))\bigr)$; equivalently $\operatorname{pr}_{2}\circ\bar e_{j}=e_{j}\circ f$. In this exercise $M'=(-\epsilon,\epsilon)$, $f=\lambda$, and $E=TB$.

![[Def - The Tangent Bundle#The Definition]]

The [[Def - The Tangent Bundle|tangent bundle]] $\pi_{TB}\colon TB\to B$ is the vector bundle whose fibre over $b$ is the tangent space $T_{b}B$; over a chart $(U,x=(x^{1},\dots,x^{n}))$ of $B$ it has the coordinate frame $(\partial_{1},\dots,\partial_{n})$ and the associated local trivialization
$$\Psi_{U}\colon \pi_{TB}^{-1}(U)\to U\times\mathbb{R}^{n},\qquad w\mapsto\bigl(\pi_{TB}(w),\,(dx^{1}(w),\dots,dx^{n}(w))\bigr),$$
which is a fibrewise linear isomorphism. Thus $w\in T_{b}B$ is recorded by its components $(dx^{i}(w))_{i}$ in this frame.

![[Def - Section of a Vector Bundle#The Definition]]

A [[Def - Section of a Vector Bundle|section]] of a vector bundle $\pi'\colon\lambda^{*}TB\to(-\epsilon,\epsilon)$ is a smooth map $\sigma\colon(-\epsilon,\epsilon)\to\lambda^{*}TB$ with $\pi'\circ\sigma=\operatorname{id}$; the space of all such is $\Gamma(\lambda^{*}TB)$. Because $\lambda^{*}TB$ is the fibre-product submanifold above, a set-theoretic section has the form $\sigma(t)=(t,w(t))$ with $w(t)\in T_{\lambda(t)}B$; the constraint $\pi'\circ\sigma=\operatorname{id}$ is exactly the first-coordinate identity, and the base-point constraint $\pi_{TB}(w(t))=\lambda(t)$ is exactly membership in $\lambda^{*}TB$.

![[Def - Velocity of a Curve#The Definition]]

The [[Def - Velocity of a Curve|velocity]] of $\lambda$ at $t$ is $\dot\lambda(t)=d\lambda_{t}(\partial_{t}|_{t})\in T_{\lambda(t)}B$, the image of the standard unit tangent vector $\partial_{t}|_{t}\in T_{t}(-\epsilon,\epsilon)$ under the [[Def - The Differential of a Smooth Map|differential]] of $\lambda$; in a chart $(U,x)$ of $B$ around $\lambda(t)$ it reads $\dot\lambda(t)=\sum_{i}\dfrac{d(x^{i}\circ\lambda)}{dt}(t)\,\partial_{i}|_{\lambda(t)}$.

The bundle $\lambda^{*}TB$ exists as a genuine vector bundle over $(-\epsilon,\epsilon)$ by the [[Thm - Vector Bundle Construction Lemma|Vector Bundle Construction Lemma]] applied to the pull-back data — this is proved on **[[Def - Operations on Vector Bundles and Pull-Back Bundles]]**, and we take it as given here; the present exercise identifies its sections.

---

# Convergent Strategy

**Problem class.** This is an *identify-two-descriptions-of-the-same-object* problem: a bundle-theoretic description (a section of $\lambda^{*}TB$) and a hand-built description (a smooth curve of tangent vectors based along $\lambda$). Problems of this shape are solved by exhibiting an explicit bijection and then checking that it and its inverse *preserve smoothness*, because both sides carry a smoothness requirement and the entire subtlety lives there. The set-level bijection is immediate from the definition of the pull-back; the work is the smoothness equivalence.

**Assumption pattern.** The only structural input is that $\lambda^{*}TB$ is the fibre-product submanifold $\{(t,w):\lambda(t)=\pi_{TB}(w)\}$ together with its bundle local frames pulled back from $TB$. The recognisable trigger is that a section is by definition a map *into* the total space, whereas a vector field along the curve is a map *into $TB$*; the map $\operatorname{pr}_{2}$ (fibrewise an isomorphism) is precisely the device that converts one into the other. Whenever a pull-back appears and one wants to compare its sections with maps into the original bundle, $\operatorname{pr}_{2}$ is the bridge.

**Theorem routing.** The route is: unpack the fibre-product definition of $\lambda^{*}TB$ to read off that any section is $\sigma(t)=(t,V(t))$ with $V(t)\in T_{\lambda(t)}B$, so $V:=\operatorname{pr}_{2}\circ\sigma$ and $\sigma\mapsto V$, $V\mapsto(t\mapsto(t,V(t)))$ are inverse set maps; then verify smoothness in both directions using the pulled-back local frame $\bar e$ over $U'=\lambda^{-1}(U)$ from **[[Def - Operations on Vector Bundles and Pull-Back Bundles]]**, matching the component functions of $\sigma$ in $\bar e$ with the component functions of $V$ in the coordinate frame of $TB$; finally instantiate $V=\dot\lambda$, whose chart components $\tfrac{d(x^{i}\circ\lambda)}{dt}$ are smooth by the smoothness of $\lambda$, to get the velocity as a section.

**Key decision point.** The single non-obvious move is to *check smoothness in a local frame rather than fight the submanifold topology of $\lambda^{*}TB\subseteq(-\epsilon,\epsilon)\times TB$ directly*. In a pulled-back frame the section $\sigma$ and the vector field $V$ have literally the same coordinate representation — the tuple of component functions $(\sigma^{1}(t),\dots,\sigma^{n}(t))$ — so "$\sigma$ is smooth" and "$V$ is smooth" reduce to the *same* condition, "all $\sigma^{i}\in C^{\infty}(U')$", and the equivalence is not merely true but tautological once the frames are aligned. Choosing the frame is what collapses the problem.

---

# Legal Operations Used

The topic page for this chapter is not yet assembled; the operations are named descriptively and will be reconciled with its numbered Legal Operations list.

1. **Unpack a pull-back as a fibre-product submanifold.** Replace the abstract fibre prescription $(\lambda^{*}TB)_{t}=T_{\lambda(t)}B$ by the concrete total space $\{(t,w):\lambda(t)=\pi_{TB}(w)\}\subseteq(-\epsilon,\epsilon)\times TB$ with $\pi'=\operatorname{pr}_{1}$; this makes "section" a completely explicit condition on a pair-valued map.

2. **Read a section off its two coordinates.** From $\pi'\circ\sigma=\operatorname{id}$ deduce that a section has first coordinate the identity, $\sigma(t)=(t,w(t))$, and from membership in the fibre product deduce the base-point constraint $\pi_{TB}(w(t))=\lambda(t)$, i.e. $w(t)\in T_{\lambda(t)}B$.

3. **Use $\operatorname{pr}_{2}$ as the fibrewise isomorphism bridging sections and maps into $TB$.** Set $V:=\operatorname{pr}_{2}\circ\sigma$; because $\operatorname{pr}_{2}$ is a linear isomorphism on each fibre, this is a bijection between sections and their second coordinates, with explicit inverse $V\mapsto(t\mapsto(t,V(t)))$.

4. **Check bundle smoothness in a local frame.** Trivialise $\lambda^{*}TB$ over $U'=\lambda^{-1}(U)$ by the frame $\bar e$ pulled back from a coordinate frame of $TB$ over a chart $U$ of $B$; a section is smooth if and only if its components in $\bar e$ are smooth, and the same components describe $V$ in the coordinate frame of $TB$, so the two smoothness conditions coincide.

5. **Instantiate the general identification at a specific field.** Apply the identification to the velocity $\dot\lambda$, whose chart components are the derivatives $\tfrac{d(x^{i}\circ\lambda)}{dt}$, smooth because $\lambda$ is smooth.

---

# Hints

> [!note]- Hint 1
> Write out what $\lambda^{*}TB$ *is* as a set: a point of it is a pair $(t,w)$ with $t\in(-\epsilon,\epsilon)$, $w\in TB$, and $\pi_{TB}(w)=\lambda(t)$. Now what does $\pi'\circ\sigma=\operatorname{id}$ force the first coordinate of $\sigma(t)$ to be, and what does membership in the fibre product force about the second coordinate?

> [!note]- Hint 2
> A section is a map into the total space $\lambda^{*}TB$; a vector field along $\lambda$ is a map into $TB$. The projection $\operatorname{pr}_{2}\colon\lambda^{*}TB\to TB$ turns the first into the second. Because $\operatorname{pr}_{2}$ is a *linear isomorphism on each fibre*, it is invertible fibrewise; write down the inverse map $V\mapsto\sigma$ explicitly and check the two are mutually inverse at the level of sets before worrying about smoothness.

> [!note]- Hint 3
> To settle smoothness, do not wrestle with the submanifold topology directly — trivialise. Choose a chart $(U,x)$ of $B$; over $U$, $TB$ has the coordinate frame $(\partial_{1},\dots,\partial_{n})$, and over $U'=\lambda^{-1}(U)$ the pull-back $\lambda^{*}TB$ has the frame $\bar e_{j}(t)=(t,\partial_{j}|_{\lambda(t)})$. Expand both $\sigma$ and $V$ in these frames. What relation do the component functions satisfy?

> [!note]- Hint 4
> You will find $\sigma(t)=\sum_{j}\sigma^{j}(t)\,\bar e_{j}(t)$ and $V(t)=\operatorname{pr}_{2}(\sigma(t))=\sum_{j}\sigma^{j}(t)\,\partial_{j}|_{\lambda(t)}$ — the *same* coefficient functions $\sigma^{j}$. A section is smooth iff its $\sigma^{j}$ are smooth; and $V$, read in the trivialization of $TB$, is $t\mapsto(\lambda(t),(\sigma^{1}(t),\dots,\sigma^{n}(t)))$, smooth iff the $\sigma^{j}$ are smooth (since $\lambda$ already is). For the velocity, compute the $\sigma^{j}$ for $V=\dot\lambda$ in the chart.

---

# Solution

The plan is to make the pull-back concrete, extract the set bijection from its two coordinates, and then reduce smoothness on both sides to the smoothness of one common tuple of component functions by expanding in a pulled-back local frame. The velocity field then falls out by computing that common tuple for $V=\dot\lambda$. Throughout, $n=\dim B$, $\pi_{TB}\colon TB\to B$ is the tangent-bundle projection, and $\pi'=\operatorname{pr}_{1}\colon\lambda^{*}TB\to(-\epsilon,\epsilon)$.

**Step 1: Make the pull-back concrete and read off the shape of a section.**

Every section $\sigma\in\Gamma(\lambda^{*}TB)$ has the form $\sigma(t)=(t,V(t))$ with $V(t)\in T_{\lambda(t)}B$, and this is forced by the definitions.

> [!note]- Derivation
> By the fibre-product description of the pull-back (item 1 of Legal Operations, and the Recall transclusion of **[[Def - Operations on Vector Bundles and Pull-Back Bundles]]**),
> $$\lambda^{*}TB=\bigl\{(t,w)\in(-\epsilon,\epsilon)\times TB\ \bigl|\ \lambda(t)=\pi_{TB}(w)\bigr\},\qquad \pi'=\operatorname{pr}_{1}|_{\lambda^{*}TB}.$$
> Let $\sigma\colon(-\epsilon,\epsilon)\to\lambda^{*}TB$ be any section, so $\pi'\circ\sigma=\operatorname{id}$. Write $\sigma(t)=(a(t),w(t))\in(-\epsilon,\epsilon)\times TB$ for its two coordinates. Then
> $$a(t)=\operatorname{pr}_{1}(\sigma(t))=\pi'(\sigma(t))=t\qquad\text{(since }\pi'\circ\sigma=\operatorname{id}\text{)},$$
> so the first coordinate is the identity. Membership $\sigma(t)\in\lambda^{*}TB$ is the constraint $\lambda(t)=\pi_{TB}(w(t))$ (definition of the fibre product), i.e.
> $$w(t)\in\pi_{TB}^{-1}(\lambda(t))=T_{\lambda(t)}B.$$
> Setting $V:=w=\operatorname{pr}_{2}\circ\sigma$, we have exhibited $\sigma(t)=(t,V(t))$ with $V(t)\in T_{\lambda(t)}B$ for every $t$, as claimed.

**Step 2: The two assignments are mutually inverse bijections of sets.**

The maps $\Phi\colon\sigma\mapsto\operatorname{pr}_{2}\circ\sigma$ and $\Psi\colon V\mapsto(t\mapsto(t,V(t)))$ are inverse bijections between the *set-theoretic* sections of $\lambda^{*}TB$ and the *set-theoretic* vector fields along $\lambda$ (smoothness deferred to Step 3).

> [!note]- Derivation
> Let $\mathcal S$ denote maps $\sigma\colon(-\epsilon,\epsilon)\to\lambda^{*}TB$ with $\pi'\circ\sigma=\operatorname{id}$ (sections as maps of sets), and $\mathcal V$ the maps $V\colon(-\epsilon,\epsilon)\to TB$ with $V(t)\in T_{\lambda(t)}B$ for all $t$ (vector fields along $\lambda$, as maps of sets).
>
> *$\Phi$ lands in $\mathcal V$.* For $\sigma\in\mathcal S$, Step 1 gives $\sigma(t)=(t,V(t))$ with $V(t)=\operatorname{pr}_{2}(\sigma(t))\in T_{\lambda(t)}B$; so $\Phi(\sigma)=V\in\mathcal V$.
>
> *$\Psi$ lands in $\mathcal S$.* For $V\in\mathcal V$, the value $(t,V(t))$ satisfies $\pi_{TB}(V(t))=\lambda(t)$ (definition of $\mathcal V$), hence $(t,V(t))\in\lambda^{*}TB$; and $\operatorname{pr}_{1}(t,V(t))=t$, so $\pi'\circ\Psi(V)=\operatorname{id}$; thus $\Psi(V)\in\mathcal S$.
>
> *$\Psi\circ\Phi=\operatorname{id}$.* For $\sigma\in\mathcal S$, $(\Psi\circ\Phi)(\sigma)(t)=\Psi(\operatorname{pr}_{2}\circ\sigma)(t)=(t,\operatorname{pr}_{2}(\sigma(t)))=(t,V(t))=\sigma(t)$, using $\sigma(t)=(t,V(t))$ from Step 1. Hence $\Psi\circ\Phi=\operatorname{id}$.
>
> *$\Phi\circ\Psi=\operatorname{id}$.* For $V\in\mathcal V$, $(\Phi\circ\Psi)(V)(t)=\operatorname{pr}_{2}\bigl((t,V(t))\bigr)=V(t)$. Hence $\Phi\circ\Psi=\operatorname{id}$.
>
> Therefore $\Phi$ and $\Psi$ are mutually inverse bijections $\mathcal S\leftrightarrow\mathcal V$.

**Step 3: The bijection restricts to smooth sections and smooth vector fields.**

Under $\Phi$ and $\Psi$, a section $\sigma$ is smooth (as a map into $\lambda^{*}TB$) if and only if the corresponding $V=\Phi(\sigma)$ is smooth (as a map into $TB$). Hence the set bijection of Step 2 restricts to a bijection $\Gamma(\lambda^{*}TB)\cong\{$smooth vector fields along $\lambda\}$.

> [!note]- Derivation
> Smoothness is local, so fix $t_{0}\in(-\epsilon,\epsilon)$, put $b_{0}=\lambda(t_{0})$, and choose a chart $(U,x=(x^{1},\dots,x^{n}))$ of $B$ with $b_{0}\in U$. Set $U':=\lambda^{-1}(U)$, an open neighbourhood of $t_{0}$ in $(-\epsilon,\epsilon)$; since $\lambda$ is continuous this is open, and $\lambda(U')\subseteq U$.
>
> **The local frames.** Over $U$, the tangent bundle $TB$ has the coordinate [[Def - Local Frame|local frame]] $(\partial_{1},\dots,\partial_{n})$ and the trivialization $\Psi_{U}(w)=(\pi_{TB}(w),(dx^{i}(w))_{i})$ recalled above. By the pull-back's frame description (Recall, and item 4 of Legal Operations), over $U'$ the bundle $\lambda^{*}TB$ has the frame
> $$\bar e_{j}(t):=\bigl(t,\ \partial_{j}|_{\lambda(t)}\bigr)\in(\lambda^{*}TB)_{t},\qquad j=1,\dots,n,$$
> so that $\operatorname{pr}_{2}(\bar e_{j}(t))=\partial_{j}|_{\lambda(t)}$. These are pointwise a basis of $(\lambda^{*}TB)_{t}=T_{\lambda(t)}B$ because $(\partial_{j}|_{\lambda(t)})_{j}$ is a basis of $T_{\lambda(t)}B$ and $\operatorname{pr}_{2}$ is a fibrewise isomorphism.
>
> **Common component functions.** Let $\sigma\in\mathcal S$ and $V=\Phi(\sigma)=\operatorname{pr}_{2}\circ\sigma$. Over $U'$ expand $\sigma$ in the frame $\bar e$: there are unique functions $\sigma^{j}\colon U'\to\mathbb{R}$ with
> $$\sigma(t)=\sum_{j=1}^{n}\sigma^{j}(t)\,\bar e_{j}(t)\qquad\text{(existence and uniqueness of frame coefficients)}.$$
> Applying the fibrewise-linear map $\operatorname{pr}_{2}$ term by term,
> $$V(t)=\operatorname{pr}_{2}(\sigma(t))=\sum_{j=1}^{n}\sigma^{j}(t)\,\operatorname{pr}_{2}(\bar e_{j}(t))=\sum_{j=1}^{n}\sigma^{j}(t)\,\partial_{j}|_{\lambda(t)}\qquad(\operatorname{pr}_{2}\text{ linear on fibres, }\operatorname{pr}_{2}\bar e_{j}=\partial_{j}\circ\lambda).$$
> So $\sigma$ and $V$ carry the *same* coefficient functions $(\sigma^{j})_{j}$ over $U'$; this is the crux.
>
> **Direction ($\Rightarrow$): $\sigma$ smooth implies $V$ smooth.** A section of a vector bundle is smooth if and only if its coefficient functions in a local frame are smooth (characterisation of smooth sections, [[Def - Section of a Vector Bundle]]). Assuming $\sigma$ smooth, each $\sigma^{j}\in C^{\infty}(U')$. Reading $V$ through the trivialization $\Psi_{U}$ of $TB$,
> $$\Psi_{U}\circ V\colon\ t\longmapsto\bigl(\lambda(t),\ (\sigma^{1}(t),\dots,\sigma^{n}(t))\bigr)\in U\times\mathbb{R}^{n}\qquad\text{(since }dx^{i}(\partial_{j})=\delta^{i}_{j}\text{, so the components of }V(t)\text{ are the }\sigma^{i}(t)),$$
> whose first coordinate $\lambda|_{U'}$ is smooth (hypothesis: $\lambda$ is a smooth curve) and whose remaining coordinates $\sigma^{i}$ are smooth. Hence $\Psi_{U}\circ V$ is smooth; as $\Psi_{U}$ is a diffeomorphism onto $U\times\mathbb{R}^{n}$, $V|_{U'}$ is smooth. Since $t_{0}$ was arbitrary, $V$ is smooth on all of $(-\epsilon,\epsilon)$.
>
> **Direction ($\Leftarrow$): $V$ smooth implies $\sigma$ smooth.** Assume $V\in\mathcal V$ is smooth. Then $\Psi_{U}\circ V=(\lambda,(V^{1},\dots,V^{n}))$ is smooth with $V^{i}(t)=dx^{i}(V(t))$; comparing with the expansion above gives $\sigma^{j}=V^{j}$, so each $\sigma^{j}=dx^{j}\circ V\in C^{\infty}(U')$ (composition of smooth maps). By the same characterisation of smooth sections, the section $\sigma=\Psi(V)$, having smooth coefficient functions $\sigma^{j}$ in the frame $\bar e$ over every such $U'$, is smooth on $(-\epsilon,\epsilon)$.
>
> Both directions hold on a neighbourhood of each point, and smoothness is a local property, so $\Phi$ maps $\Gamma(\lambda^{*}TB)$ onto the smooth vector fields along $\lambda$ and $\Psi$ maps back; combined with the set-bijection of Step 2, this is the claimed identification.

**Step 4: The velocity field is a section.**

The velocity $\dot\lambda$, defined by $\dot\lambda(t)=d\lambda_{t}(\partial_{t}|_{t})\in T_{\lambda(t)}B$, is a smooth vector field along $\lambda$; under $\Psi$ it is the section $t\mapsto(t,\dot\lambda(t))$ of $\lambda^{*}TB$.

> [!note]- Derivation
> By construction $\dot\lambda(t)=d\lambda_{t}(\partial_{t}|_{t})$ is the [[Def - The Differential of a Smooth Map|differential]] of $\lambda$ applied to the standard basis vector of $T_{t}(-\epsilon,\epsilon)$; the differential $d\lambda_{t}\colon T_{t}(-\epsilon,\epsilon)\to T_{\lambda(t)}B$ has codomain $T_{\lambda(t)}B$, so indeed $\dot\lambda(t)\in T_{\lambda(t)}B$ and the base-point constraint $\pi_{TB}(\dot\lambda(t))=\lambda(t)$ holds. Thus $\dot\lambda\in\mathcal V$ at the level of sets.
>
> *Smoothness.* In the chart $(U,x)$ around $\lambda(t_{0})$, the chain rule for the differential gives the components of the velocity as the ordinary derivatives of the coordinate curve $x\circ\lambda$:
> $$dx^{i}(\dot\lambda(t))=dx^{i}\bigl(d\lambda_{t}(\partial_{t}|_{t})\bigr)=\partial_{t}\bigl(x^{i}\circ\lambda\bigr)(t)=\frac{d(x^{i}\circ\lambda)}{dt}(t)\qquad\text{(chain rule, }d(x^{i})\circ d\lambda=d(x^{i}\circ\lambda)).$$
> Each $x^{i}\circ\lambda\colon U'\to\mathbb{R}$ is smooth (composition of the smooth chart map $x^{i}$ with the smooth curve $\lambda$), hence so is its derivative $\tfrac{d(x^{i}\circ\lambda)}{dt}$. Therefore $\Psi_{U}\circ\dot\lambda=\bigl(\lambda,\ (\tfrac{d(x^{1}\circ\lambda)}{dt},\dots,\tfrac{d(x^{n}\circ\lambda)}{dt})\bigr)$ is smooth, so $\dot\lambda$ is a smooth vector field along $\lambda$.
>
> By Step 3, $\dot\lambda$ corresponds to the smooth section $\Psi(\dot\lambda)\colon t\mapsto(t,\dot\lambda(t))$ of $\lambda^{*}TB$, whose components in the frame $\bar e$ over $U'$ are exactly $\sigma^{j}(t)=\tfrac{d(x^{j}\circ\lambda)}{dt}(t)$. This is the distinguished section named in the problem.

> [!note]- Complete formal solution
> **Claim.** For a smooth curve $\lambda\colon(-\epsilon,\epsilon)\to B$, the map $\Phi\colon\sigma\mapsto\operatorname{pr}_{2}\circ\sigma$ is a bijection from $\Gamma(\lambda^{*}TB)$ to the set of smooth vector fields along $\lambda$, with inverse $\Psi\colon V\mapsto(t\mapsto(t,V(t)))$; the velocity field $\dot\lambda$ corresponds to a section.
>
> Realise the pull-back as the fibre-product submanifold $\lambda^{*}TB=\{(t,w)\in(-\epsilon,\epsilon)\times TB:\lambda(t)=\pi_{TB}(w)\}$ with $\pi'=\operatorname{pr}_{1}$ and $\operatorname{pr}_{2}$ a fibrewise linear isomorphism $(\lambda^{*}TB)_{t}\to T_{\lambda(t)}B$.
>
> *Set bijection.* If $\sigma$ is a section, then $\operatorname{pr}_{1}\sigma(t)=\pi'\sigma(t)=t$, so $\sigma(t)=(t,V(t))$; and $\sigma(t)\in\lambda^{*}TB$ forces $\pi_{TB}(V(t))=\lambda(t)$, i.e. $V(t)\in T_{\lambda(t)}B$. Thus $\Phi(\sigma)=V$ is a vector field along $\lambda$. Conversely, for $V(t)\in T_{\lambda(t)}B$ the pair $(t,V(t))$ lies in $\lambda^{*}TB$ and has first coordinate $t$, so $\Psi(V)$ is a section. The computations $(\Psi\Phi\sigma)(t)=(t,\operatorname{pr}_{2}\sigma(t))=\sigma(t)$ and $(\Phi\Psi V)(t)=\operatorname{pr}_{2}(t,V(t))=V(t)$ show $\Phi,\Psi$ are mutually inverse.
>
> *Smoothness equivalence.* Fix $t_{0}$, a chart $(U,x)$ of $B$ around $\lambda(t_{0})$, and $U'=\lambda^{-1}(U)$. Over $U$, $TB$ has the coordinate frame $(\partial_{i})$ and trivialization $\Psi_{U}(w)=(\pi_{TB}(w),(dx^{i}(w))_{i})$; over $U'$, $\lambda^{*}TB$ has the pulled-back frame $\bar e_{j}(t)=(t,\partial_{j}|_{\lambda(t)})$, and $\operatorname{pr}_{2}\bar e_{j}=\partial_{j}\circ\lambda$. Writing $\sigma=\sum_{j}\sigma^{j}\bar e_{j}$ over $U'$, linearity of $\operatorname{pr}_{2}$ on fibres gives $V=\operatorname{pr}_{2}\sigma=\sum_{j}\sigma^{j}\,\partial_{j}\circ\lambda$, so $\sigma$ and $V$ share the coefficient tuple $(\sigma^{j})$. A section is smooth iff its frame coefficients are smooth; $V$ read through $\Psi_{U}$ is $t\mapsto(\lambda(t),(\sigma^{1}(t),\dots,\sigma^{n}(t)))$, smooth iff the $\sigma^{j}$ are smooth (as $\lambda$ is smooth). Hence $\sigma\in C^{\infty}\iff V\in C^{\infty}$ on $U'$; being local, this holds globally, so $\Phi$ restricts to the asserted bijection of smooth objects.
>
> *Velocity.* The differential gives $\dot\lambda(t)=d\lambda_{t}(\partial_{t}|_{t})\in T_{\lambda(t)}B$ with chart components $dx^{i}(\dot\lambda(t))=\tfrac{d(x^{i}\circ\lambda)}{dt}(t)$ by the chain rule; these are smooth because $x^{i}\circ\lambda$ is smooth. So $\dot\lambda$ is a smooth vector field along $\lambda$, and $\Psi(\dot\lambda)\colon t\mapsto(t,\dot\lambda(t))$ is a smooth section of $\lambda^{*}TB$. $\blacksquare$

> [!warning] Illegal but tempting shortcut
> One is tempted to declare $\sigma$ smooth "because $t\mapsto(t,V(t))$ is smooth into the product $(-\epsilon,\epsilon)\times TB$" and stop there. This is not yet a proof that $\sigma$ is smooth *as a map into the submanifold* $\lambda^{*}TB$: smoothness into an ambient manifold does not in general descend to smoothness into an arbitrary subset. It descends here only because $\lambda^{*}TB$ is an [[Def - Embedded Submanifold|embedded submanifold]], for which smoothness into the ambient space and into the submanifold coincide. The frame computation in Step 3 sidesteps this by checking smoothness *intrinsically*, in the bundle's own local trivialization, and is what makes the argument self-contained. If one prefers the ambient route, the missing ingredient to cite is exactly the embedded-submanifold property, established on **[[Def - Embedded Submanifold]]**.

---

# Key Takeaways

**A pull-back turns "along" into "over": a field defined along a map becomes a field over the domain.** The recurring difficulty with a vector field along a curve is that it is not a section of any bundle over the curve's *image* — the curve may self-intersect, so at a crossing point the field wants two values — and it is not a vector field on $B$ either, since it is only defined at the points $\lambda(t)$. The pull-back $\lambda^{*}TB$ resolves this by re-basing the tangent spaces over the *parameter* $t$ rather than over the point $\lambda(t)$: the fibre at $t$ is $T_{\lambda(t)}B$, and distinct parameters with the same image get distinct fibres. The trigger to reach for a pull-back is precisely this pattern — an object indexed by the domain of a map but valued in fibres of a bundle over the codomain. Once recognised, the object is a genuine section and every section-level construction (covariant derivative, parallel transport, the space $\Gamma$ as a $C^{\infty}$-module) applies verbatim.

**The projection $\operatorname{pr}_{2}$ of a pull-back is the universal translator between sections and maps into the original bundle, and smoothness is settled in a pulled-back frame.** Every identification of this kind runs through the same two facts: $\operatorname{pr}_{2}\colon f^{*}E\to E$ is a fibrewise isomorphism, so it bijects sections with their $E$-valued shadows; and $f^{*}E$ inherits a local frame $\bar e_{j}=(\,\cdot\,,e_{j}\circ f)$ from any local frame $e_{j}$ of $E$, in which a section and its shadow have *identical component functions*. This second fact is what makes the smoothness equivalence trivial rather than delicate: instead of comparing two different smoothness notions, one observes that both reduce to the smoothness of one tuple of real functions. The transferable diagnostic: when asked whether two descriptions of a field agree smoothly, align their local frames first; if the components coincide, the smoothness statements coincide automatically.

**Reparametrisation-invariant differential geometry is built on this identification.** The velocity field is the first and most important section of $\lambda^{*}TB$, and reading it as such is what lets one write the geodesic equation $\tfrac{\nabla}{dt}\dot\lambda=0$ and the Jacobi equation as equations *for sections of a bundle*, to which the exterior covariant derivative and curvature of later sections apply. A **[[Def - Jacobi Field|Jacobi field]]** along a geodesic $\lambda$ is exactly such a section — a smooth vector field along $\lambda$ solving $\tfrac{\nabla^{2}}{dt^{2}}J+R(J,\dot\lambda)\dot\lambda=0$, arising as the variation field of a family of geodesics — and its home is $\Gamma(\lambda^{*}TB)$, made precise by the present exercise. More generally the variation field of any smooth homotopy of curves is a vector field along the base curve, hence a section of the corresponding pull-back; this is the setting in which the second variation of arc length and the theory of conjugate points are developed. The pattern to carry forward: whenever a curve of tangent vectors appears — velocity, acceleration, a variation field, a Jacobi field — name it as a section of the pull-back and let the bundle machinery act.
