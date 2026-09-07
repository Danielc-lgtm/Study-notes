---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Principal G-Bundle"
  - "Def - Complex Projective Space as a Quotient"
  - "Thm - Free Proper Actions Give Principal Bundles"
  - "Def - Transition Functions and the Cocycle Condition"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $G$ acts on the **right** on a principal bundle, $R_\lambda(p)=p\cdot\lambda$; this is the standing convention of the series (see [[Def - Principal G-Bundle]]). We write $S^{2n+1}=\{z=(z_0,\dots,z_n)\in\mathbb C^{n+1}:\lVert z\rVert^2=|z_0|^2+\dots+|z_n|^2=1\}$ for the unit sphere in $\mathbb C^{n+1}$, and $\mathbb{CP}^n$ for [[Def - Complex Projective Space as a Quotient|complex projective space]], the quotient of $\mathbb C^{n+1}\setminus\{0\}$ by the scaling action $z\mapsto z\mu$, $\mu\in\mathbb C^\times$; the class of $z$ is written $[z]=[z_0:\dots:z_n]$. The circle group is $U(1)=\{\lambda\in\mathbb C:|\lambda|=1\}$; its Lie algebra is $\mathfrak u(1)=i\mathbb R$. We write $\mathbb H=\{a+bi+cj+dk:a,b,c,d\in\mathbb R\}$ for the quaternions, with $i^2=j^2=k^2=-1$, $ij=k=-ji$, $jk=i=-kj$, $ki=j=-ik$; the conjugate is $\overline{a+bi+cj+dk}=a-bi-cj-dk$ and the norm is $|q|^2=q\bar q=a^2+b^2+c^2+d^2$. The group of unit quaternions is $Sp(1)=\{q\in\mathbb H:|q|=1\}$, and $\mathbb{HP}^n$ is quaternionic projective space, defined below. The symbol $\theta=g^{-1}dg$ denotes the (left) [[Def - The Maurer-Cartan Form|Maurer–Cartan form]] pulled back by a map $g$ into a matrix group, and $\operatorname{tr}$ is the matrix trace in the defining representation.

This is a compound page: it defines the complex Hopf bundle $S^{2n+1}\to\mathbb{CP}^n$, its base-$n=1$ incarnation $S^3\to S^2$ with the explicit local sections and transition function of Bär, the quaternionic Hopf bundles $S^{4n+3}\to\mathbb{HP}^n$, and the ladders of inclusions relating them — because these are one family of principal bundles built by the same quotient construction, and the quaternionic case for $n=0$ furnishes the standing example $SU(2)\cong S^3$ whose orientation fixes the sign conventions of the whole gauge-theory series, recorded here in the `# Sign ledger`.

> [!warning] Convention: orientation of $SU(2)\cong Sp(1)\cong S^3$
> We identify $SU(2)$ with the unit quaternions $Sp(1)$ (see [[Ex - SU(2) is the Group of Unit Quaternions]]) and orient the resulting $3$-sphere as the **boundary of the closed unit ball in $\mathbb H=\mathbb R^4$**, outward normal first: a basis $(v_1,v_2,v_3)$ of $T_pS^3$ is positive if and only if $(p,v_1,v_2,v_3)$ is a positively oriented basis of $\mathbb R^4$ under its standard orientation, the one for which $(1,i,j,k)$ is positive. Every complex manifold, in particular $\mathbb{CP}^n$, carries the **complex orientation** (the one for which $(\partial_x,\partial_y)$ is positive for a holomorphic coordinate $w=x+iy$). All signs on this page are computed under these two choices.

---

# Axiom Motivation

The problem the Hopf bundle solves, historically and conceptually, is this: **produce a principal bundle that is genuinely twisted.** Every construction we have met so far can be trivial — a product $M\times G$ has a global section and its transition functions are all the identity — and a definition of "principal bundle" that admitted only products would be empty. We need a first example of a nontrivial one, and we want it to be as concrete as possible: living inside spheres, with an action written in coordinates, so that its nontriviality can be seen and computed rather than merely asserted.

The natural place to look is a sphere with a free circle action. If $U(1)$ acts freely on a compact manifold $P$, then by [[Thm - Free Proper Actions Give Principal Bundles|the free–proper theorem]] the quotient $P/U(1)$ is a manifold and $P\to P/U(1)$ is a principal $U(1)$-bundle; compactness makes the action automatically proper, so freeness is the only thing to check. The odd-dimensional sphere $S^{2n+1}\subset\mathbb C^{n+1}$ carries the scalar action $z\cdot\lambda=z\lambda$ of $U(1)$, and this action is free because $z\lambda=z$ with $z\neq0$ forces $\lambda=1$. Its orbits are the great circles $\{z\lambda:\lambda\in U(1)\}$, and the orbit space is exactly the set of complex lines through the origin meeting the sphere — that is, $\mathbb{CP}^n$. So the sphere fibres over projective space with circle fibres, for free, and the only question left is whether the resulting bundle is trivial.

It is not, and one should ask *what would have to be true* for it to be trivial. A principal bundle is trivial if and only if it has a global section ([[Thm - Sections of a Principal Bundle and Triviality]]). A global section of $S^{2n+1}\to\mathbb{CP}^n$ is a continuous choice, for each complex line $\ell\subset\mathbb C^{n+1}$, of a unit vector spanning $\ell$, varying continuously with $\ell$ and with no sign or phase ambiguity. For $n=1$ the base is $S^2$, and such a choice is a nowhere-vanishing continuous field of unit vectors — precisely the kind of object the hairy-ball theorem forbids on the sphere. The failure is not an accident of one construction; it is the topological content of the bundle. The definition below is engineered so that this failure is *localised* into a single transition function $z/|z|$ whose winding number around the equator is the one invariant that measures the twist.

What must a good definition capture, and what must it exclude? It must capture that the fibres are exactly the $U(1)$-orbits (great circles), so that the bundle projection is the honest quotient map, not some auxiliary map that happens to have circle fibres. It must exclude the degenerate possibility that the action is not free: were we to take, say, $S^{2n+1}$ with the action $z\cdot\lambda=z\lambda^2$, the element $\lambda=-1$ would fix every point, the "orbits" would be circles double-covered, and the quotient map would not be a principal bundle at all (its would-be structure group would act with a stabiliser). And it must be presented concretely enough that the transition function can be written down, because the entire downstream theory — Chern classes, the degree of a line bundle, the classification of $U(1)$- and $SU(2)$-bundles — reads off invariants from exactly that transition function. A reader handed the desiderata "free circle action on a sphere, orbits are the fibres, coordinates explicit" could reconstruct the definition.

The quaternionic version answers a second need. When we replace $\mathbb C$ by $\mathbb H$ and $U(1)$ by $Sp(1)\cong SU(2)$, the same quotient construction gives principal $SU(2)$-bundles $S^{4n+3}\to\mathbb{HP}^n$. The case $n=0$ is trivial as a bundle but not as an object: it *is* the group $SU(2)\cong S^3$, and orienting it fixes every sign in the series. The case $n=1$ gives the generator of $SU(2)$-bundles over $S^4=\mathbb{HP}^1$, the bundle with second Chern number $\pm1$ on which Donaldson theory is built. So the Hopf family is not one example but the seed of the entire subject.

---

# The Definition

**The complex Hopf bundle.** Fix $n\geq1$. Let $U(1)$ act on the right on the unit sphere $S^{2n+1}\subset\mathbb C^{n+1}$ by scalar multiplication,
$$z\cdot\lambda=z\lambda=(z_0\lambda,\dots,z_n\lambda),\qquad z\in S^{2n+1},\ \lambda\in U(1),$$
and let $\pi\colon S^{2n+1}\to\mathbb{CP}^n$, $\pi(z)=[z]$, be the restriction to the sphere of the projection to complex projective space. The **(complex) Hopf bundle** is the principal $U(1)$-bundle
$$\pi\colon S^{2n+1}\longrightarrow\mathbb{CP}^n,\qquad z\cdot\lambda=z\lambda.$$
That this is a principal $U(1)$-bundle is proved in the Examples section below, from [[Thm - Free Proper Actions Give Principal Bundles|the free–proper theorem]]: the action is free and, $U(1)$ being compact, proper, and its orbits are exactly the fibres of $\pi$.

**The infinitesimal generator.** The fundamental vector field (see [[Def - Fundamental Vector Field of a Group Action]]) of the generator $i\in\mathfrak u(1)$ is
$$v(z)=\frac{d}{ds}\Big|_{s=0}z\cdot e^{is}=iz=(iz_0,\dots,iz_n),$$
a nowhere-vanishing vector field tangent to $S^{2n+1}$ (it is tangent because $\langle iz,z\rangle_{\mathbb R}=\operatorname{Re}\overline{iz}\cdot z=\operatorname{Re}(-i|z|^2)=0$), and its integral curves are the orbits, the great circles $s\mapsto ze^{is}$.

**The quaternionic Hopf bundles.** Regard $\mathbb H^{n+1}$ as a right $\mathbb H$-module and let $Sp(1)=\{q\in\mathbb H:|q|=1\}$ act on the right on the unit sphere $S^{4n+3}=\{h=(h_0,\dots,h_n)\in\mathbb H^{n+1}:\sum_{i=0}^n|h_i|^2=1\}$ by
$$h\cdot q=(h_0q,\dots,h_nq),\qquad q\in Sp(1).$$
Quaternionic projective space $\mathbb{HP}^n$ is the orbit space of the scaling action $h\mapsto hq$, $q\in\mathbb H^\times$, on $\mathbb H^{n+1}\setminus\{0\}$; equivalently it is $S^{4n+3}/Sp(1)$. The **quaternionic Hopf bundle** is the principal $Sp(1)$-bundle
$$\pi\colon S^{4n+3}\longrightarrow\mathbb{HP}^n,\qquad h\cdot q=hq,$$
principal by the same free–proper argument. Under the isomorphism $Sp(1)\cong SU(2)$ ([[Ex - SU(2) is the Group of Unit Quaternions]]) these are principal $SU(2)$-bundles. The case $n=0$ is $S^3\to\mathbb{HP}^0=\{*\}$, the group $Sp(1)\cong SU(2)\cong S^3$ itself over a point.

**The tautological line bundle.** Over $\mathbb{CP}^n$ the **tautological line bundle** $\mathcal O(-1)$ is the complex line bundle whose fibre over $[z]$ is the line $\mathbb C z\subset\mathbb C^{n+1}$ it names,
$$\mathcal O(-1)=\{([z],w)\in\mathbb{CP}^n\times\mathbb C^{n+1}:w\in\mathbb C z\},$$
a subbundle of the trivial bundle $\mathbb{CP}^n\times\mathbb C^{n+1}$. It is the **associated bundle** $S^{2n+1}\times_{U(1)}\mathbb C$ of the Hopf bundle for the standard representation of $U(1)$ on $\mathbb C$; that identification is proved in §3.4 (see **[[Ex - The Tautological Line Bundle over CP^n is Associated to the Hopf Bundle]]**).

---

# Categorical / Structural Definition

Structurally the Hopf bundle is the universal example of "coordinatising a family of lines by their unit vectors". A point of $\mathbb{CP}^n$ is a complex line $\ell\subset\mathbb C^{n+1}$; the fibre $\pi^{-1}([z])$ is the set of unit vectors spanning $\ell$, a $U(1)$-torsor (a set on which $U(1)$ acts freely and transitively, with no distinguished basepoint). The bundle is thus the total space of the functor sending a line to its unit circle, and its structure group $U(1)$ is exactly the ambiguity — the phase — in choosing a unit vector on a line. In the same language the tautological bundle $\mathcal O(-1)$ is the total space of the tautological functor "the line itself", and passing from the principal bundle to $\mathcal O(-1)$ is the associated-bundle functor $V\mapsto S^{2n+1}\times_{U(1)}V$ applied to the standard representation $V=\mathbb C$. The quaternionic Hopf bundle is the same construction with the division algebra $\mathbb H$ replacing $\mathbb C$ and the torsor now over $Sp(1)$; because $\mathbb H$ is noncommutative, one must fix left versus right scalars, and we use right $\mathbb H$-lines throughout, which is why $Sp(1)$ acts on the right.

---

# Relate to Other Fields / Compression

**True name.** Operationally, the Hopf bundle is *the transition function $z/|z|$*. Every question about it — whether it is trivial, what its Chern number is, what its holonomy can be — is answered by the winding of a single $U(1)$-valued function on the overlap of two charts. The abstract quotient $S^{2n+1}\to\mathbb{CP}^n$ is the invariant object, but the number that distinguishes it from the product bundle is the degree of $z/|z|\colon S^1\to U(1)$ on the equatorial circle, which is $1$. This is the first appearance of the general principle that a bundle over a sphere is a clutching function and its only invariant is a homotopy class of maps of the equator into the structure group.

The construction recurs across mathematics under different names. In algebraic geometry $\mathcal O(-1)$ is the tautological sheaf and $\mathcal O(1)$ its dual, the hyperplane bundle whose sections are the linear forms; the Hopf bundle is the associated $U(1)$-bundle of the unit-circle subbundle of $\mathcal O(-1)$ for the Fubini–Study metric. In quantum mechanics the $n=1$ Hopf bundle $S^3\to S^2$ is the bundle of normalised state vectors of a two-level system (a qubit) over the space of physical states (the Bloch sphere), and its connection is the source of the Berry phase; the fibre $U(1)$ is the unobservable global phase. In classical mechanics the same $S^3\to S^2$ is the momentum map picture of the Kepler problem and of the isotropic harmonic oscillator. That one object carries all these readings is a compression: it is the minimal nontrivial circle bundle, and every situation with an unremovable phase ambiguity over a two-sphere is a copy of it.

---

# Examples / Corollaries

**Is a principal bundle — the complex Hopf bundle.** We verify the four clauses of the definition of a principal $U(1)$-bundle ([[Def - Principal G-Bundle]]) for $\pi\colon S^{2n+1}\to\mathbb{CP}^n$.
- *Free action.* If $z\cdot\lambda=z$ with $z\in S^{2n+1}$, then $z_j\lambda=z_j$ for every $j$; since $z\neq0$ some $z_j\neq0$, giving $\lambda=1$. So no nonidentity element of $U(1)$ has a fixed point, and by [[Def - Free, Transitive, Effective, and Proper Group Actions|freeness]] the action is free.
- *Proper action.* $U(1)$ is compact and $S^{2n+1}$ is Hausdorff, so the action is automatically proper. Concretely, the action map $\Phi\colon U(1)\times S^{2n+1}\to S^{2n+1}\times S^{2n+1}$, $(\lambda,z)\mapsto(z\lambda,z)$, is a continuous map whose domain $U(1)\times S^{2n+1}$ is compact (a product of compact spaces) and whose codomain is Hausdorff; the preimage $\Phi^{-1}(K)$ of any compact $K\subset S^{2n+1}\times S^{2n+1}$ is closed (continuity, $K$ closed) inside the compact domain, hence compact, so $\Phi$ is proper. Compactness of the acting group $U(1)$ is the property used.
- *Orbits are the fibres.* Two points $z,z'\in S^{2n+1}$ have $[z]=[z']$ if and only if $z'=z\mu$ for some $\mu\in\mathbb C^\times$; taking norms, $|\mu|=1$, so $\mu\in U(1)$ and $z'=z\cdot\mu$ lies in the orbit of $z$. Hence $\pi^{-1}([z])=\{z\cdot\lambda:\lambda\in U(1)\}$, the orbit, which is the great circle $\{ze^{is}:s\in[0,2\pi)\}$.
- *Principal structure.* By [[Thm - Free Proper Actions Give Principal Bundles|the free–proper theorem]], applied to the free proper right action of the compact group $U(1)$ on $S^{2n+1}$, the quotient $S^{2n+1}/U(1)=\mathbb{CP}^n$ is a manifold and $\pi$ is a principal $U(1)$-bundle with equivariant local trivialisations. $\;\checkmark$

**Is an instance — the base is $S^2$ when $n=1$.** For $n=1$ the base $\mathbb{CP}^1$ is diffeomorphic to the round sphere $S^2$ via the Hopf map (proved in [[Thm - CP^1 is Diffeomorphic to S^2 via the Hopf Map|chapter I]]); under this identification $\pi\colon S^3\to S^2$ is the classical Hopf fibration, and it agrees, up to the orientation conventions recorded below, with the topologist's [[Def - The Hopf Map]].

> [!warning] Convention: Bär's stereographic normalisation of $S^2$
> Bär coordinatises the base $S^2\subset\mathbb C\times\mathbb R$ as $\{(z,t):|z|^2+t^2=1\}$ with charts $U_1=S^2\setminus\{(0,-1)\}$ (all but the south pole) and $U_2=S^2\setminus\{(0,1)\}$ (all but the north pole), the stereographic projections being taken from the poles $(0,\pm1)$. The algebraic-topology page [[Def - The Hopf Map]] uses a different normalisation of the identification $\mathbb{CP}^1\cong S^2$. The two differ by an orientation-preserving diffeomorphism of $S^2$ and a possible reflection of the equatorial circle; the resulting transition functions therefore agree up to complex conjugation, i.e. up to the sign of the winding number, which is why the recorded value $z/|z|$ and its conjugate $\bar z/|z|$ both occur in the literature. The magnitude of the winding number, $1$, is convention-independent, and it is all that the nontriviality and Chern-number statements use.

**Local sections and the transition function ($n=1$).** On $U_1$ and $U_2$ Bär's local sections of $\pi\colon S^3\to S^2$ are
$$s_1(z,t)=\Big(\tfrac{4|z|^2}{(1+t)^2}+1\Big)^{-1/2}\Big(\tfrac{2z}{1+t},\,1\Big),\qquad
s_2(z,t)=\Big(1+\tfrac{|z|^2/4}{(1-t)^2}\Big)^{-1/2}\Big(1,\,\tfrac{z/2}{1-t}\Big),$$
with the Hopf map written $\operatorname{Hopf}(w_1,w_2)=\dfrac{(4w_1\bar w_2,\;4|w_2|^2-|w_1|^2)}{4|w_2|^2+|w_1|^2}$. We check $s_1$ is a genuine section, i.e. $\operatorname{Hopf}(s_1(z,t))=(z,t)$, using the sphere relation $|z|^2=1-t^2=(1-t)(1+t)$. With $w_1=N_1^{-1}\tfrac{2z}{1+t}$, $w_2=N_1^{-1}$ and $N_1^2=\tfrac{4|z|^2}{(1+t)^2}+1$, the first Hopf coordinate is
$$\frac{4w_1\bar w_2}{4|w_2|^2+|w_1|^2}=\frac{8z/(1+t)}{4+4|z|^2/(1+t)^2}=\frac{2z(1+t)}{(1+t)^2+|z|^2}\overset{(\ast)}{=}\frac{2z(1+t)}{2(1+t)}=z,$$
where $(\ast)$ uses $(1+t)^2+|z|^2=(1+t)^2+(1-t)(1+t)=(1+t)\big[(1+t)+(1-t)\big]=2(1+t)$; and the second coordinate is
$$\frac{4|w_2|^2-|w_1|^2}{4|w_2|^2+|w_1|^2}=\frac{4-4|z|^2/(1+t)^2}{4+4|z|^2/(1+t)^2}=\frac{(1+t)^2-|z|^2}{(1+t)^2+|z|^2}=\frac{2t(1+t)}{2(1+t)}=t,$$
so $\operatorname{Hopf}(s_1(z,t))=(z,t)$ and $s_1$ is a unit section over $U_1$. The same computation for $s_2$, using $(1-t)^2+|z|^2=2(1-t)$, gives $\operatorname{Hopf}(s_2(z,t))=(\bar z,t)$; the appearance of $\bar z$ is precisely the complex-conjugation ambiguity noted in the convention callout above, arising because $s_2$ is written in the conjugate stereographic coordinate. Comparing the two unit sections over a common fibre, they differ by a unit complex scalar, and following Bär's normalisation this scalar is
$$s_1\cdot g_{12}=s_2,\qquad g_{12}(z,t)=\frac{z}{|z|}\colon U_{12}=S^2\setminus\{(0,\pm1)\}\longrightarrow U(1).$$

> [!warning] Source misprint (Bär, Ex. 2.2.17)
> The source additionally prints "$g_{12}=|z|/z$", which contradicts the displayed relation $s_1\cdot(z/|z|)=s_2$ derived from the same identities $(1-t)(1+t)=|z|^2$ and $(1+t)^2=|z|^4/(1-t)^2$. The correct value consistent with $s_1\cdot g_{12}=s_2$ is $g_{12}=z/|z|$; we use it. ⚠️ In our own recomputation of the literal formulas above the section $s_2$ came out over $(\bar z,t)$, so with these exact formulas the transition is $z/|z|$ or its conjugate $\bar z/|z|$ according to the stereographic conjugation convention; both have winding number $\pm1$ around the equator, which is the only feature used downstream.

**Corollary — nontriviality.** Restricted to the equatorial circle $\{|z|=1,\ t=0\}$, the transition function is $z\mapsto z/|z|=z=e^{i\phi}$, which winds once around $U(1)$: its winding number is $1\neq0$. A trivial bundle over $S^2$ has a transition function that is a coboundary $g_{12}=h_1h_2^{-1}$ with $h_i\colon U_i\to U(1)$ defined over the two contractible charts, so $g_{12}$ extends continuously over the disc $U_1$ and is therefore null-homotopic as a map of the equatorial circle into $U(1)$, forcing winding number $0$; since the winding number here is $1$, the Hopf bundle $S^3\to S^2$ is **not** trivial. Consequently $S^3$ is not the product bundle $S^2\times S^1$, and more generally $S^{2n+1}\to\mathbb{CP}^n$ is nontrivial. The complete argument, replacing Bär's $\pi_1$ computation by the de Rham obstruction, is [[Thm - The Hopf Bundle is Nontrivial|the next theorem]].

**Is NOT trivial — restated as a non-example of a product.** The map $\pi\colon S^3\to S^2$ is a surjective submersion with circle fibres, exactly like the projection $S^2\times S^1\to S^2$, yet it is not isomorphic to it: no global section exists, because a global section would be a nowhere-vanishing continuous unit-vector choice over $S^2$, forbidden by the hairy-ball phenomenon. This is the standing example of a fibre bundle without a global section.

**The ladders of inclusions.** The standard inclusions $\mathbb C^{n+1}\hookrightarrow\mathbb C^{n+2}$, $z\mapsto(z,0)$, and $\mathbb H^{n+1}\hookrightarrow\mathbb H^{n+2}$ restrict to commuting squares of bundle maps
$$\begin{array}{ccc}S^{2n+1}&\hookrightarrow&S^{2n+3}\\ \downarrow&&\downarrow\\ \mathbb{CP}^n&\hookrightarrow&\mathbb{CP}^{n+1}\end{array}\qquad\text{and}\qquad\begin{array}{ccc}S^{4n+3}&\hookrightarrow&S^{4n+7}\\ \downarrow&&\downarrow\\ \mathbb{HP}^n&\hookrightarrow&\mathbb{HP}^{n+1},\end{array}$$
each vertical arrow a Hopf bundle and each horizontal arrow equivariant (the inclusion commutes with the $U(1)$- respectively $Sp(1)$-action), so the diagrams commute. The direct limits are the ladders $S^3\subset S^5\subset\cdots$ over $\mathbb{CP}^1\subset\mathbb{CP}^2\subset\cdots$ and $S^7\subset S^{11}\subset\cdots$ over $\mathbb{HP}^1\subset\mathbb{HP}^2\subset\cdots$, whose colimits $S^\infty\to\mathbb{CP}^\infty$ and $S^\infty\to\mathbb{HP}^\infty$ are the classifying bundles of $U(1)$ and $Sp(1)$ (§3.6).

**Calibration check.** Two verifications the reader can carry out from the page. First, on the equator $\{|z|=1,t=0\}$ the transition function is $g_{12}(z,0)=z/|z|=z$, a full turn of $U(1)$ as $z$ runs once around $S^1$: winding number $1$. Second, the cocycle condition $g_{12}g_{21}=1$ holds because $s_2\cdot g_{21}=s_1$ forces $g_{21}=g_{12}^{-1}=\overline{z/|z|}=\bar z/|z|$, and indeed $\frac{z}{|z|}\cdot\frac{\bar z}{|z|}=\frac{|z|^2}{|z|^2}=1$, consistent with the cocycle identity $g_{\alpha\beta}=g_{\beta\alpha}^{-1}$ ([[Def - Transition Functions and the Cocycle Condition]]).

---

# Sign ledger

**This section computes, once and for all, the three orientation-dependent signs that the four sign-sensitive pages of the series share, under the two orientation conventions fixed in the Notation callout above** ($SU(2)\cong Sp(1)\cong S^3=\partial B^4$ with $\mathbb R^4$ oriented by $(1,i,j,k)$; complex manifolds with the complex orientation). Every other page that needs one of these signs wikilinks this section rather than re-deriving it. Throughout, $g\colon S^3\to SU(2)$ is smooth, $\theta=g^{-1}dg\in\Omega^1(S^3;\mathfrak{su}(2))$ is the pulled-back Maurer–Cartan form, $\operatorname{tr}$ is the trace in the defining $2\times2$ representation, and $\deg g$ is the [[Thm - The Brouwer Degree is an Integer and a Homotopy Invariant|Brouwer degree]] computed with the fixed orientation on both source and target copies of $S^3$.

**Ledger item (a): $\displaystyle\int_{SU(2)}\operatorname{tr}(\theta\wedge\theta\wedge\theta)=-24\pi^2$, equivalently $W(g)=-\deg g$ for $W(g):=\tfrac1{24\pi^2}\int_{S^3}\operatorname{tr}(\theta^{\wedge3})$.**

We first reduce the wedge-cube of the trace to a bracket. For a matrix-valued $1$-form $\theta$, expanding $\operatorname{tr}(\theta\wedge\theta\wedge\theta)$ over the six permutations of three vectors and using cyclicity of the trace (moving a degree-$1$ factor past a degree-$2$ product costs $(-1)^{1\cdot2}=+1$),
$$\operatorname{tr}(\theta\wedge\theta\wedge\theta)(X,Y,Z)=3\big[\operatorname{tr}(\theta(X)\theta(Y)\theta(Z))-\operatorname{tr}(\theta(X)\theta(Z)\theta(Y))\big]=3\operatorname{tr}\!\big(\theta(X)[\theta(Y),\theta(Z)]\big).$$
At the identity $e\in SU(2)$, $\theta_e=\mathrm{id}_{\mathfrak{su}(2)}$, so for $X,Y,Z\in\mathfrak{su}(2)$ this reads $\operatorname{tr}(\theta^{\wedge3})_e(X,Y,Z)=3\operatorname{tr}(X[Y,Z])$. The form $\operatorname{tr}(\theta^{\wedge3})$ is bi-invariant (left-invariance is built into $\theta$; right-invariance follows from $\operatorname{Ad}$-invariance of $\operatorname{tr}$), hence a constant multiple of the Riemannian volume form of the bi-invariant metric.

Take the basis $E_a=-i\sigma_a$ of $\mathfrak{su}(2)$, where $\sigma_1,\sigma_2,\sigma_3$ are the Pauli matrices; these are skew-Hermitian and traceless, so $E_a\in\mathfrak{su}(2)$, and a direct computation gives $[E_a,E_b]=2\varepsilon_{abc}E_c$ and $E_a^2=-I$, whence $\operatorname{tr}(E_a^2)=-2$ and $\langle X,Y\rangle:=-\tfrac12\operatorname{tr}(XY)$ makes $(E_1,E_2,E_3)$ orthonormal. This is the round metric of the **unit** $3$-sphere: under $SU(2)\cong Sp(1)\subset\mathbb H=\mathbb R^4$ the images of $E_1,E_2,E_3$ are the imaginary quaternions $-k,-j,-i$ respectively, and $\{i,j,k\}$ is the standard orthonormal basis of $T_1S^3=\operatorname{Im}\mathbb H$. Evaluating,
$$\operatorname{tr}(\theta^{\wedge3})_e(E_1,E_2,E_3)=3\operatorname{tr}(E_1[E_2,E_3])=3\operatorname{tr}(E_1\cdot2E_1)=6\operatorname{tr}(E_1^2)=6(-2)=-12\qquad\text{(since }[E_2,E_3]=2E_1\text{)}.$$
Now the orientation. In $\operatorname{Im}\mathbb H=\operatorname{span}(i,j,k)$ the basis $(E_1,E_2,E_3)=(-k,-j,-i)$ has, relative to $(i,j,k)$, the change-of-basis matrix with columns $-k,-j,-i$, whose determinant is $+1$; hence $(1,E_1,E_2,E_3)$ and $(1,i,j,k)$ agree in orientation, so **$(E_1,E_2,E_3)$ is a positively oriented orthonormal basis** of $T_eS^3$ under the $\partial B^4$ convention. Therefore $\operatorname{tr}(\theta^{\wedge3})=-12\,\mathrm{vol}_{S^3}$ as forms, and with $\operatorname{Vol}(S^3)=2\pi^2$ (from [[Ex - Volume of the n-Sphere via the Volume Form|the sphere-volume computation]]),
$$\int_{SU(2)}\operatorname{tr}(\theta\wedge\theta\wedge\theta)=-12\operatorname{Vol}(S^3)=-12\cdot2\pi^2=-24\pi^2.$$
For a general $g\colon S^3\to SU(2)$, the degree theorem gives $\int_{S^3}g^*\operatorname{tr}(\theta^{\wedge3})=\deg g\cdot\int_{SU(2)}\operatorname{tr}(\theta^{\wedge3})=-24\pi^2\deg g$, so $W(g)=-\deg g$. $\;\blacksquare$

**Ledger item (b): the clutching degree equals $+c_2$.** Let $X$ be a closed connected oriented $4$-manifold and $P\to X$ a principal $SU(2)$-bundle, trivial over $X\setminus D^\circ$ and over a coordinate disc $D$ with clutching (transition) map $g\colon S=\partial D\to SU(2)$ normalised by $s_+=s_-\cdot g$ (inner trivialisation $=$ outer trivialisation times $g$). Define the **clutching degree** $k(P):=\deg g$, computed with $S=\partial D$ carrying the boundary orientation from $D$ (which matches the $\partial B^4$ orientation of $SU(2)$ through an oriented chart $D\cong B^4$). Then, as proved on [[Thm - Second Chern Number of an SU(2)-Bundle over a Closed Four-Manifold is the Clutching Degree]] using item (a) and item (c),
$$c_2(P)[X]=\frac1{8\pi^2}\int_X\operatorname{tr}(F_A\wedge F_A)=+\deg g=+k(P).$$
That is, **with the fixed conventions the clutching degree is $+c_2$, not $-c_2$**; no sign flip is needed, and the instanton number $k(P)=\int_X c_2(P)$ agrees with $\deg g$.

**Ledger item (c): $\vartheta(A\cdot g)-\vartheta(A)=+\deg g$.** For the [[Def - Chern-Simons Functional|Chern–Simons functional]] $\vartheta(A)=\tfrac1{8\pi^2}\int_M\operatorname{tr}(A\wedge dA+\tfrac23A^{\wedge3})$ on a closed oriented $3$-manifold $M$ and a gauge transformation $g\colon M\to SU(2)$, the gauge-variation identity (proved on [[Thm - Gauge Variation of the Chern-Simons Functional]]) together with item (a) gives
$$\vartheta(A\cdot g)-\vartheta(A)=-\frac1{24\pi^2}\int_M\operatorname{tr}(\theta^{\wedge3})=-W(g)=+\deg g.$$
So **the Chern–Simons functional increases by $+\deg g$ under the gauge transformation $g$**, and $\vartheta$ is well defined in $\mathbb R/\mathbb Z$.

**Summary of the ledger.**

| Quantity | Value under the fixed conventions |
|---|---|
| $\displaystyle\int_{SU(2)}\operatorname{tr}(\theta\wedge\theta\wedge\theta)$ | $-24\pi^2$ |
| $W(g)=\tfrac1{24\pi^2}\int_{S^3}\operatorname{tr}(\theta^{\wedge3})$ | $-\deg g$ |
| clutching degree $k(P)=\deg g$ versus $c_2(P)[X]$ | $k(P)=+c_2(P)[X]$ |
| $\vartheta(A\cdot g)-\vartheta(A)$ | $+\deg g$ |

---

# Unlocked by This

> [!tip] The classification of principal $SU(2)$-bundles *(from Gauge Theory III §3.6)*
> The quaternionic Hopf bundle $S^7\to S^4=\mathbb{HP}^1$ is the clutching bundle of $q\mapsto q$ and generates all $SU(2)$-bundles over $S^4$; the general classification over a closed $4$-manifold by the clutching degree is [[Thm - Classification of Principal SU(2)-Bundles over Four-Manifolds]].

> [!tip] The first Chern class of $\mathcal O(-1)$ *(from Gauge Theory VI §6.2)*
> The tautological bundle has $\int_{\mathbb{CP}^1}c_1(\mathcal O(-1))=-1$ under the complex orientation, computed from the Hopf connection's curvature on **[[Thm - First Chern Class of a Line Bundle from Curvature]]**; the transition function $z/|z|$ of this page is what makes the integral $\pm1$.

> [!tip] The Chern–Simons functional *(from Gauge Theory VI §6.4)*
> The sign $\int_{SU(2)}\operatorname{tr}(\theta^{\wedge3})=-24\pi^2$ recorded here is exactly the constant that makes **[[Def - Chern-Simons Functional]]** well defined modulo the integers.
