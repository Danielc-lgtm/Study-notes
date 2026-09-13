---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - The Hopf Bundle"
  - "Def - Connection on a Principal Bundle"
  - "Def - Horizontal Subspace and Horizontal Lift"
tags: [geometry, gauge-theory]
---

# Notation

Throughout this page $n\ge 1$ is fixed. We identify $\mathbb{C}^{n+1}$ with the real vector space $\mathbb{R}^{2n+2}$ by writing each complex coordinate $z_j=x_{2j}+ix_{2j+1}$, so a point $z=(z_0,\dots,z_n)\in\mathbb{C}^{n+1}$ is the real vector $(x_0,x_1,\dots,x_{2n+1})$. Multiplication by $i$ is then the real-linear map $J\colon\mathbb{R}^{2n+2}\to\mathbb{R}^{2n+2}$ with $J^2=-\operatorname{id}$; we write $iz$ for $Jz$.

We equip $\mathbb{C}^{n+1}\cong\mathbb{R}^{2n+2}$ with the standard **real inner product**
$$\langle u,w\rangle:=\operatorname{Re}\sum_{j=0}^{n}u_j\overline{w_j}\qquad(u,w\in\mathbb{C}^{n+1}),$$
which is exactly the Euclidean inner product on $\mathbb{R}^{2n+2}$; $|u|^2=\langle u,u\rangle$ is the squared Euclidean length. For a subset $S\subset\mathbb{R}^{2n+2}$ the symbol $S^{\perp}$ denotes the real-orthogonal complement with respect to $\langle\cdot,\cdot\rangle$.

The **unit sphere** is $S^{2n+1}:=\{z\in\mathbb{C}^{n+1}:\sum_{j=0}^n|z_j|^2=1\}=\{z\in\mathbb{R}^{2n+2}:|z|=1\}$, with tangent space at $z$ given by
$$T_zS^{2n+1}=\{u\in\mathbb{R}^{2n+2}:\langle u,z\rangle=0\}=z^{\perp},$$
since $S^{2n+1}$ is the level set $\{|z|^2=1\}$ of a function whose gradient at $z$ is $2z$.

The structure group is $G=U(1)=\{\lambda\in\mathbb{C}:|\lambda|=1\}$, acting on the **right** on $S^{2n+1}$ diagonally by complex scalar multiplication,
$$R_\lambda(z)=z\cdot\lambda:=\lambda z=(\lambda z_0,\dots,\lambda z_n),$$
which is the [[Def - The Hopf Bundle|Hopf bundle]] $\pi\colon S^{2n+1}\to\mathbb{CP}^n$, $z\mapsto[z]$. The action is a right action because $U(1)$ is abelian: $(z\cdot\lambda)\cdot\mu=\mu(\lambda z)=(\lambda\mu)z=z\cdot(\lambda\mu)$.

The Lie algebra is $\mathfrak{g}=\mathfrak{u}(1)=T_1U(1)=i\mathbb{R}$, the imaginary axis; a general element is $\xi=si$ with $s\in\mathbb{R}$, and $\exp(t\,si)=e^{tsi}\in U(1)$. Following the series convention, the **fundamental vector field** of $\xi\in\mathfrak{u}(1)$ is
$$\xi_P(z)=\frac{d}{dt}\Big|_{t=0}z\cdot\exp(t\xi)\in T_zS^{2n+1},$$
the infinitesimal generator of the flow of the group action (see [[Def - Fundamental Vector Field of a Group Action]]). We write $v(z):=i_P(z)$ for the fundamental field of the generator $\xi=i$; the computation of Lemma 1 gives $v(z)=iz$.

The candidate connection form is the $\mathfrak{u}(1)$-valued $1$-form $a$ on $S^{2n+1}$ defined by
$$a_z(u):=\langle v(z),u\rangle\,i\qquad(u\in T_zS^{2n+1});$$
since $\langle v(z),u\rangle\in\mathbb{R}$, the value $a_z(u)$ lies in $i\mathbb{R}=\mathfrak{u}(1)$, so $a\in\Omega^1(S^{2n+1};\mathfrak{u}(1))$.

We recall the two defining conditions for a connection form (see [[Def - Connection on a Principal Bundle]]), restated here so the page is self-contained. A form $\omega\in\Omega^1(P;\mathfrak{g})$ on a principal $G$-bundle $P\to M$ is a **connection form** if and only if

1. **(equivariance)** $R_g^{*}\omega=\operatorname{Ad}_{g^{-1}}\omega$ for every $g\in G$; and
2. **(fundamental fields)** $\omega(\xi_P)=\xi$ for every $\xi\in\mathfrak{g}$.

Here $\operatorname{Ad}_g=d_1(h\mapsto ghg^{-1})\colon\mathfrak{g}\to\mathfrak{g}$ is the adjoint representation (see [[Thm - Ad is a Smooth Representation and its Differential is ad]]). The **horizontal subspace** of $\omega$ at $p$ is $H_p:=\ker\omega_p$ (see [[Def - Horizontal Subspace and Horizontal Lift]]).

> [!warning] Convention: numbering of the two checks
> Bär's Example 2.3.5 verifies the two conditions in the *opposite order* to the order in which his Definition 2.3.1 lists them, and prints the label "property 2" beside the equivariance computation and "property 1" beside the fundamental-field computation, which is the reverse of his own definition (recorded in the source's typo list). We use the series numbering throughout: **(1)** is equivariance $R_g^{*}\omega=\operatorname{Ad}_{g^{-1}}\omega$ and **(2)** is $\omega(\xi_P)=\xi$. Haydys writes the connection form as $a$ and takes values in $\mathbb{R}i=\mathfrak{u}(1)$; this agrees with our $a$ verbatim.

---

# Statement

> **Theorem (the standard connection on the Hopf bundle).** Let $\pi\colon S^{2n+1}\to\mathbb{CP}^n$ be the Hopf $U(1)$-bundle, with $\mathfrak{u}(1)=i\mathbb{R}$, and let $v(z)=iz$ be the fundamental vector field of the generator $i\in\mathfrak{u}(1)$. Define $a\in\Omega^1(S^{2n+1};\mathfrak{u}(1))$ by
> $$a_z(u):=\langle v(z),u\rangle\,i,\qquad u\in T_zS^{2n+1},$$
> where $\langle\cdot,\cdot\rangle$ is the standard real inner product on $\mathbb{R}^{2n+2}\cong\mathbb{C}^{n+1}$. Then:
>
> **(a)** $a$ is a connection form on the Hopf bundle; that is, $a$ satisfies the equivariance condition $R_\lambda^{*}a=\operatorname{Ad}_{\lambda^{-1}}a$ and the fundamental-field condition $a(\xi_P)=\xi$ for all $\lambda\in U(1)$, $\xi\in\mathfrak{u}(1)$.
>
> **(b)** Its horizontal distribution is $\ker a=v^{\perp}$; explicitly, $H_z=\ker a_z=\{u\in T_zS^{2n+1}:\langle v(z),u\rangle=0\}$, the orthogonal complement of the fibre direction inside the tangent space.
>
> **(c)** $a$ is the **unique** connection form on the Hopf bundle whose horizontal distribution is $v^{\perp}$.

We call $a$ the **standard connection** (or the metric, or round, connection) on the Hopf bundle.

---

# Motivation

A principal bundle by itself has no notion of "the same direction from one fibre to the next": its vertical directions — those tangent to a fibre — are canonically identified with the Lie algebra through the fundamental vector fields, but the horizontal directions are not given. A [[Def - Connection on a Principal Bundle|connection]] is exactly the missing datum, a $G$-invariant choice of horizontal complement, packaged as a $\mathfrak{g}$-valued $1$-form. The general existence theorem produces connections by patching local pieces with a partition of unity, and the resulting forms are not canonical: they depend on the choices made. The question this page answers is whether some bundles carry a connection singled out by their geometry, with no choices at all.

The Hopf bundle is the first and most important case where the answer is yes. The total space $S^{2n+1}$ is a round sphere, and the circle acts on it by isometries — multiplication by a unit complex number rigidly rotates $\mathbb{R}^{2n+2}$. Wherever a group acts on a Riemannian manifold by isometries, the phrase "perpendicular to the orbit" means the same thing at every point of an orbit, so declaring the horizontal directions to be the ones orthogonal to the fibre is automatically group-invariant. This is the whole idea: the round metric chooses the horizontal complement for us, and reading off its vertical part in the Lie algebra produces the form $a$.

The construction matters far beyond its own elegance. The Hopf bundle is the universal example of a nontrivial circle bundle: its curvature (computed in the next section as an exercise) is the area form of the base, and its first Chern number is $\pm 1$, which is why the tautological line bundle $\mathcal{O}(-1)\to\mathbb{CP}^n$ — associated to the Hopf bundle by the standard representation — is nontrivial. Every later statement about Chern classes of line bundles, about instantons on $S^4$, and about the topology of gauge fields is calibrated against this one connection. It is worth having it written down once, correctly and canonically, together with the reason it is the only connection compatible with the round geometry.

We assume the reader knows what a principal $U(1)$-bundle is, has met the Hopf fibration as a bundle, and is comfortable with fundamental vector fields and the two axioms for a connection form; these are recalled at the point of use.

---

# Sources and Targets

**Sources (Input Broadening).** The theorem's literal hypotheses are very specific — the round sphere, the diagonal circle action — but the construction it performs is an instance of a much more general one, and recognising the general pattern in disguise is what lets the same idea be reused.

The first disguised source is **a principal bundle carrying a $G$-invariant Riemannian metric with $G$ acting by isometries**. Whenever $P\to M$ is a principal $G$-bundle and $P$ has a metric preserved by the right action, the pointwise orthogonal complement $H_p:=V_p^{\perp}$ of the vertical space is a smooth distribution with $T_pP=H_p\oplus V_p$, and it is invariant because isometries carry orthogonal complements to orthogonal complements; by the bijection between connections and invariant horizontal distributions this is a connection. The bridge $B\Rightarrow A$ is: *invariant metric on $P$ $\Rightarrow$ invariant horizontal complement $\Rightarrow$ connection*. The Hopf case takes $P=S^{2n+1}$ with the round metric. *Example problem:* on a compact Lie group $K$ acting freely by isometries on a compact Riemannian $P$, average any metric over $K$ to make it invariant, then read off the mechanical connection whose horizontal spaces are metric-orthogonal to the orbits.

The second disguised source is **a reductive homogeneous space**. If $H\subset K$ is a closed subgroup and the Lie algebra splits as $\mathfrak{k}=\mathfrak{h}\oplus\mathfrak{m}$ with $\operatorname{Ad}(H)\mathfrak{m}\subseteq\mathfrak{m}$, then the principal $H$-bundle $H\to K\to K/H$ carries a canonical connection whose horizontal space at the identity coset is the image of $\mathfrak{m}$, translated around by the left action of $K$. The Hopf bundle realises this pattern: $S^{2n+1}=U(n+1)/U(n)$ and $\mathbb{CP}^n=U(n+1)/(U(1)\times U(n))$, so the projection $\pi$ is the homogeneous fibration $U(n+1)/U(n)\to U(n+1)/(U(1)\times U(n))$ with structure group $U(1)$, and the $\operatorname{Ad}$-invariant orthogonal complement of the isotropy directions under the bi-invariant metric on $\mathfrak{u}(n+1)$ supplies the reductive summand $\mathfrak{m}$; the canonical connection it induces is the Hopf connection $a$. The non-obvious step is to see a given bundle as reductive homogeneous and to identify $\mathfrak{m}$; once seen, the connection is forced.

The third disguised source is **a subbundle of a bundle that already carries a connection**, joined by orthogonal projection. If $E\subset\underline{\mathbb{C}^N}$ is a Hermitian subbundle of a trivial bundle with its flat derivative $d$, then $\nabla s:=\operatorname{pr}_E(ds)$, the Hermitian orthogonal projection of the ambient derivative back into $E$, is a connection on $E$. The tautological bundle $\mathcal{O}(-1)\subset\underline{\mathbb{C}^{n+1}}$ over $\mathbb{CP}^n$ is such a subbundle, and the connection it inherits this way is precisely the one induced from the Hopf connection $a$ (worked out in [[Ex - The Induced Connection on the Tautological Bundle from the Hopf Connection]]). The bridge is: *sub-object of a connected object $\Rightarrow$ projected connection*.

**Targets (Output Amplification).** The theorem is a genuine input to the rest of the series; each downstream use pairs it with one further ingredient.

Combine $a$ with **the structure equation for the curvature** ([[Thm - Structure Equation for the Curvature|structure equation]], $\Omega=d\omega+\tfrac12[\omega\wedge\omega]$, which for an abelian group reduces to $\Omega=d\omega$). The bracket term vanishes because $\mathfrak{u}(1)$ is abelian, so the curvature of $a$ is simply $da$, and a direct computation (carried out in [[Ex - Curvature of the Standard Hopf Connection]]) gives $\pi^{*}F_a=da=2(dx_0\wedge dx_1+dx_2\wedge dx_3)i$ on $S^3$, a nonzero $2$-form. The payoff is that the Hopf connection is not flat: there is no gauge in which it disappears.

Combine $a$ with **Chern–Weil theory** (chapter VI). Feeding $F_a$ into the first Chern form $\tfrac{i}{2\pi}F_a$ and integrating over $\mathbb{CP}^1$ yields the first Chern number of $\mathcal{O}(-1)$, which equals $-1$ under the complex orientation. The payoff is the topological conclusion that the Hopf bundle is the generator of the group of circle bundles over $S^2$; every other $U(1)$-bundle over $S^2$ is a power of it. This is the first quantitative characteristic number in the series.

Combine $a$ with **the Frobenius theorem** ([[Thm - The Frobenius Theorem|Frobenius theorem]]) and the identity that curvature is the vertical part of the bracket of horizontal lifts. Because $F_a\neq 0$, the horizontal [[Def - Distribution on a Manifold|distribution]] $v^{\perp}$ is not involutive, hence not integrable (shown in [[Ex - The Horizontal Distribution of the Hopf Connection is Not Integrable]]): there is no surface through a point everywhere tangent to the horizontal directions. The payoff, developed with holonomy in chapter V, is that horizontally lifting a loop in the base returns to a *different* point of the fibre, rotated by an amount equal to the enclosed area — the geometric origin of the Aharonov–Bohm phase.

---

# Why Is It True

Strip the statement to its mechanism. On the round sphere, every tangent space $T_zS^{2n+1}$ carries an inner product, and the fibre through $z$ is the circle $\{\lambda z:\lambda\in U(1)\}$, whose tangent line at $z$ is spanned by the single vector $v(z)=iz$. A connection has to choose, at each $z$, a horizontal complement to this line and to record, for every tangent vector, how much of it points along the fibre — measured in the Lie algebra $\mathfrak{u}(1)$. Both jobs are done at once by orthogonal projection: split $u\in T_zS^{2n+1}$ into its component along $v(z)$ and its component perpendicular to $v(z)$; the perpendicular part is declared horizontal, and the parallel part is $\langle v(z),u\rangle\,v(z)$ (because $v(z)$ is a *unit* vector), whose coefficient $\langle v(z),u\rangle$, multiplied by the generator $i$, is the Lie-algebra reading. That is the formula $a_z(u)=\langle v(z),u\rangle\,i$.

Two facts make this projection a genuine connection rather than an arbitrary $1$-form. First, the normalisation is exact: $v(z)=iz$ has $|v(z)|=|z|=1$, so when $u=\xi_P=s\,v(z)$ is itself vertical the projection returns $s\,|v(z)|^2\,i=si=\xi$, which is precisely the fundamental-field axiom — the connection reads a purely vertical vector as the Lie-algebra element that generated it, with no scaling error. Second, "perpendicular" is a $U(1)$-invariant notion here, because $U(1)$ acts by isometries: rotating $z$ and $u$ by the same $\lambda$ leaves $\langle v(z),u\rangle$ unchanged, so the form is invariant, and since the group is abelian, invariance is exactly the required equivariance ($\operatorname{Ad}$ is trivial). Uniqueness is then automatic, because a connection form is completely pinned down by its kernel: it must vanish on the horizontal space and, by the fundamental-field axiom, take prescribed values on the vertical line, so specifying the horizontal distribution leaves no freedom.

> **Mechanism in one sentence.** The Hopf connection is orthogonal projection onto the fibre direction, expressed in the Lie algebra through the unit fundamental field; it is a connection because the circle acts by isometries (making "horizontal $=$ perpendicular" invariant) and because $iz$ has unit length (making the vertical normalisation exact).

---

# What Makes This Hard

The genuinely delicate points are two, and both are places where a careless reading gives a wrong or unjustified statement. The first is the **normalisation constant**: the fundamental-field axiom demands $a(\xi_P)=\xi$ on the nose, and this works only because we took the *generator* $\xi=i$, whose fundamental field $v(z)=iz$ is a *unit* vector; if one used a non-unit fibre vector, or forgot that $|iz|=1$, the axiom would fail by a scalar and $a$ would not be a connection. The second is the reduction **equivariance $=$ invariance**: this identity holds only because $U(1)$ is abelian, so $\operatorname{Ad}_{\lambda^{-1}}=\operatorname{id}$; for a nonabelian isometric action the orthogonal complement is still a valid connection, but the algebraic form transforms with a nontrivial adjoint twist and the naive computation "$R_g^{*}a=a$" is simply false. A common third slip is to write $\ker a=v^{\perp}$ as an equation in the ambient $\mathbb{R}^{2n+2}$; it is an equation *inside the tangent space* $T_zS^{2n+1}=z^{\perp}$, so $H_z=\{z,iz\}^{\perp}$ has dimension $2n$, not $2n+1$, and one must keep the constraint $\langle u,z\rangle=0$ in view.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Compute the fundamental vector field to identify $v(z)=iz$ and check it is a unit vector tangent to the sphere. Verify the two connection axioms by direct substitution, using that $U(1)$ acts by isometries (equivariance) and that $|v(z)|^2=1$ (fundamental-field normalisation), and note that the abelian group makes $\operatorname{Ad}$ trivial so equivariance is just invariance. Read off the kernel, and get uniqueness from the fact that a connection form is determined by its horizontal distribution.

**Subgoal decomposition:**

1. **Identify the fibre direction.** Show the fundamental field of $\xi=si\in\mathfrak{u}(1)$ is $\xi_P(z)=s\,iz$, that $v(z)=iz$ satisfies $|v(z)|=1$, and that $v(z)\in T_zS^{2n+1}$.
   - *Hint:* Differentiate $z\cdot e^{tsi}=e^{tsi}z$ at $t=0$; for tangency compute $\langle iz,z\rangle$; for the norm use that $u\mapsto iu$ is an isometry.
   - *Why needed:* The whole form is built from $v(z)$, and the vertical normalisation depends on $|v(z)|=1$.

2. **Fundamental-field axiom.** Show $a(\xi_P)=\xi$ for every $\xi\in\mathfrak{u}(1)$.
   - *Hint:* Substitute $\xi_P=s\,v(z)$ into $a$; the coefficient is $s|v(z)|^2=s$.
   - *Why needed:* It is condition (2) for a connection.

3. **Equivariance axiom.** Show $R_\lambda^{*}a=a$, and that this equals $\operatorname{Ad}_{\lambda^{-1}}a$.
   - *Hint:* $dR_\lambda(u)=\lambda u$ and $v(\lambda z)=\lambda v(z)$; then use that multiplication by $\lambda$ preserves $\langle\cdot,\cdot\rangle$; finally, $\operatorname{Ad}$ is trivial for an abelian group.
   - *Why needed:* It is condition (1); the abelian reduction is the only reason the plain invariance computation suffices.

4. **Kernel.** Identify $\ker a_z=\{u\in T_zS^{2n+1}:\langle v(z),u\rangle=0\}=v^{\perp}$.
   - *Hint:* $a_z(u)=0\iff\langle v(z),u\rangle=0$, since $i\neq 0$.
   - *Why needed:* Part (b), and the input to uniqueness.

5. **Uniqueness.** Show any connection form with the same kernel equals $a$.
   - *Hint:* Two connection forms vanish on the common horizontal space and agree on the vertical line by axiom (2); use $T_zS^{2n+1}=H_z\oplus V_z$.
   - *Why needed:* Part (c).

---

# Lemma Decomposition

> [!note]- Lemma 1: The diagonal circle action is isometric, and the fundamental field of $i$ is $v(z)=iz$, a unit vertical vector
> **Statement:** For $\lambda\in U(1)$ let $m_\lambda\colon\mathbb{R}^{2n+2}\to\mathbb{R}^{2n+2}$, $m_\lambda(u)=\lambda u$, be complex multiplication by $\lambda$. Then (i) $m_\lambda$ is a linear isometry of $(\mathbb{R}^{2n+2},\langle\cdot,\cdot\rangle)$ commuting with multiplication by $i$; (ii) the right action $R_\lambda(z)=\lambda z$ restricts to $S^{2n+1}$ and $dR_\lambda|_z=m_\lambda$; (iii) the fundamental vector field of $\xi=si\in\mathfrak{u}(1)$ is $\xi_P(z)=s\,iz$, so $v(z)=i_P(z)=iz$; (iv) $v(z)\in T_zS^{2n+1}$ and $|v(z)|=1$; and (v) $v(\lambda z)=\lambda\,v(z)$.
>
> **Hint:** For (i) use $|\lambda|=1$ on the Hermitian product and take real parts; for (iii) differentiate $e^{tsi}z$; for (iv) compute $\langle iz,z\rangle$ and $|iz|$; for (v) note $i(\lambda z)=\lambda(iz)$.
>
> **Why needed:** It supplies every geometric fact the two axioms are built from: the differential of the action (for equivariance), the fundamental field and its unit length (for the fundamental-field axiom and for identifying the vertical line), and the intertwining $v(\lambda z)=\lambda v(z)$.
>
> > [!note]- Full proof
> > **(i) $m_\lambda$ is an isometry commuting with $i$.** The map $m_\lambda(u)=\lambda u$ is real-linear (multiplication by a fixed complex scalar is $\mathbb{R}$-linear). For $u,w\in\mathbb{C}^{n+1}$, the Hermitian product satisfies
> > $$\sum_{j}(\lambda u_j)\overline{(\lambda w_j)}=\lambda\overline{\lambda}\sum_j u_j\overline{w_j}=|\lambda|^2\sum_j u_j\overline{w_j}=\sum_j u_j\overline{w_j}\qquad(\text{since }|\lambda|=1).$$
> > Taking real parts, $\langle m_\lambda u,m_\lambda w\rangle=\operatorname{Re}\sum_j(\lambda u_j)\overline{(\lambda w_j)}=\operatorname{Re}\sum_j u_j\overline{w_j}=\langle u,w\rangle$, so $m_\lambda$ is an isometry. It commutes with $i$ because complex multiplication is commutative: $m_\lambda(iu)=\lambda(iu)=i(\lambda u)=i\,m_\lambda(u)$.
> >
> > **(ii) $R_\lambda$ preserves $S^{2n+1}$ and has differential $m_\lambda$.** If $|z|=1$ then $|R_\lambda z|=|\lambda z|=|z|=1$ by (i), so $R_\lambda$ maps $S^{2n+1}$ to itself. As the restriction of the real-linear map $m_\lambda$, its differential at every point is $m_\lambda$ itself: $dR_\lambda|_z(u)=m_\lambda(u)=\lambda u$ for $u\in T_zS^{2n+1}$.
> >
> > **(iii) The fundamental field of $\xi=si$.** By definition and the right action $z\cdot g=gz$,
> > $$\xi_P(z)=\frac{d}{dt}\Big|_{t=0}z\cdot\exp(t\,si)=\frac{d}{dt}\Big|_{t=0}e^{tsi}z=si\,e^{0}z=s\,iz\qquad(\text{chain rule, }\tfrac{d}{dt}e^{tsi}=si\,e^{tsi}).$$
> > In particular the generator $\xi=i$ (that is, $s=1$) gives $v(z)=i_P(z)=iz$.
> >
> > **(iv) $v(z)$ is a unit tangent vector.** Tangency: $\langle iz,z\rangle=\operatorname{Re}\sum_j(iz_j)\overline{z_j}=\operatorname{Re}\Big(i\sum_j|z_j|^2\Big)=\operatorname{Re}(i\cdot 1)=0$ (using $\sum_j|z_j|^2=|z|^2=1$), so $v(z)\in z^{\perp}=T_zS^{2n+1}$. Length: $|v(z)|^2=|iz|^2=|z|^2=1$ because multiplication by $i$ is an isometry (case $\lambda=i$ of (i)). Hence $|v(z)|=1$.
> >
> > **(v) Intertwining.** $v(\lambda z)=i(\lambda z)=\lambda(iz)=\lambda\,v(z)$, using commutativity of complex multiplication.

> [!note]- Lemma 2: The adjoint representation of an abelian Lie group is trivial
> **Statement:** If $G$ is an abelian Lie group with Lie algebra $\mathfrak{g}$, then $\operatorname{Ad}_g=\operatorname{id}_{\mathfrak{g}}$ for every $g\in G$. In particular $\operatorname{Ad}_{\lambda^{-1}}=\operatorname{id}$ on $\mathfrak{u}(1)$ for every $\lambda\in U(1)$.
>
> **Hint:** Conjugation is the identity map on an abelian group; differentiate it.
>
> **Why needed:** It is what turns the required equivariance $R_\lambda^{*}a=\operatorname{Ad}_{\lambda^{-1}}a$ into the plain invariance $R_\lambda^{*}a=a$ that the isometric action delivers.
>
> > [!note]- Full proof
> > By definition $\operatorname{Ad}_g=d_1 c_g$, where $c_g\colon G\to G$ is the conjugation $c_g(h)=ghg^{-1}$ (see [[Thm - Ad is a Smooth Representation and its Differential is ad|the adjoint representation]]). Since $G$ is abelian, $ghg^{-1}=hgg^{-1}=h$ for all $h$, so $c_g=\operatorname{id}_G$ is the identity map. The differential of the identity map at the identity element is the identity linear map, so $\operatorname{Ad}_g=d_1(\operatorname{id}_G)=\operatorname{id}_{\mathfrak{g}}$. Applying this to $G=U(1)$ (abelian) and $g=\lambda^{-1}$ gives $\operatorname{Ad}_{\lambda^{-1}}=\operatorname{id}_{\mathfrak{u}(1)}$.

> [!note]- Lemma 3: A connection form is determined by its horizontal distribution
> **Statement:** Let $P\to M$ be a principal $G$-bundle and let $\omega,\omega'\in\Omega^1(P;\mathfrak{g})$ be connection forms with $\ker\omega_p=\ker\omega'_p$ for every $p\in P$. Then $\omega=\omega'$.
>
> **Hint:** Split each tangent space as horizontal plus vertical; the two forms agree on the horizontal part (both vanish) and on the vertical part (both are fixed by the fundamental-field axiom).
>
> **Why needed:** It is the injectivity of the correspondence between connection forms and invariant horizontal distributions, and it is exactly what makes the standard connection the *unique* one with horizontal distribution $v^{\perp}$.
>
> > [!note]- Full proof
> > Fix $p\in P$ and write $V_p:=\ker(d\pi_p)$ for the vertical space (the tangent space to the fibre) and $H_p:=\ker\omega_p=\ker\omega'_p$ for the common horizontal space. Because $\omega$ is a connection form, the fundamental-field axiom (2) says $\omega_p(\xi_P(p))=\xi$ for all $\xi\in\mathfrak{g}$; since the map $\xi\mapsto\xi_P(p)$ is a linear isomorphism of $\mathfrak{g}$ onto $V_p$ (the fibre is a free orbit, so this map is injective, and $\dim V_p=\dim\mathfrak{g}$), the restriction $\omega_p|_{V_p}$ is the inverse of $\xi\mapsto\xi_P(p)$, and the same statement holds for $\omega'$. Therefore
> > $$\omega_p|_{V_p}=(\xi\mapsto\xi_P(p))^{-1}=\omega'_p|_{V_p}.\qquad(\ast)$$
> > This forces $H_p\cap V_p=0$: if $w\in H_p\cap V_p$ then $w=\xi_P(p)$ for some $\xi$, and $0=\omega_p(w)=\xi$ by $(\ast)$, so $w=0_P(p)=0$. For the dimensions themselves: $(\ast)$ shows $\omega_p$ already maps $V_p$ onto all of $\mathfrak{g}$, so $\omega_p\colon T_pP\to\mathfrak{g}$ is surjective, and the rank–nullity theorem gives $\dim H_p=\dim\ker\omega_p=\dim T_pP-\dim\mathfrak{g}=\dim P-\dim G=\dim M$ (using $\dim P=\dim M+\dim G$ for a principal $G$-bundle). Combined with $\dim V_p=\dim\mathfrak{g}=\dim G$ from the isomorphism above,
> > $$\dim H_p+\dim V_p=\dim M+\dim G=\dim P\qquad(\text{rank–nullity for }\omega_p\text{; }\dim V_p=\dim G),$$
> > which together with $H_p\cap V_p=0$ gives the internal direct sum
> > $$T_pP=H_p\oplus V_p.$$
> > Now take any $u\in T_pP$ and decompose $u=u_H+u_V$ with $u_H\in H_p$, $u_V\in V_p$. Then
> > $$\omega_p(u)=\omega_p(u_H)+\omega_p(u_V)=0+\omega_p(u_V)=\omega'_p(u_V)=\omega'_p(u_H)+\omega'_p(u_V)=\omega'_p(u),$$
> > where the first zero is because $u_H\in H_p=\ker\omega_p$, the middle equality is $(\ast)$, and the last zero (absorbed into $\omega'_p(u_H)=0$) is because $u_H\in H_p=\ker\omega'_p$. Since $u$ and $p$ were arbitrary, $\omega=\omega'$.

---

# Formal Proof

> [!note]- Complete formal proof
> We prove the three assertions in turn. Throughout, $\langle\cdot,\cdot\rangle$ is the real inner product on $\mathbb{R}^{2n+2}\cong\mathbb{C}^{n+1}$, $v(z)=iz$, and $a_z(u)=\langle v(z),u\rangle\,i$ for $u\in T_zS^{2n+1}$.
>
> **Step 0 — the objects are well-posed.** The Hopf bundle $\pi\colon S^{2n+1}\to\mathbb{CP}^n$ with the diagonal right $U(1)$-action is a principal $U(1)$-bundle (its bundle structure is established on [[Def - The Hopf Bundle]]). By Lemma 1(iii), $v(z)=iz$ is the fundamental field of the generator $i\in\mathfrak{u}(1)$, and by Lemma 1(iv) it is a unit vector in $T_zS^{2n+1}$. The assignment $z\mapsto v(z)=iz$ is the restriction to $S^{2n+1}$ of the linear (hence smooth) vector field $z\mapsto iz$ on $\mathbb{R}^{2n+2}$, and $u\mapsto\langle v(z),u\rangle$ is a smooth family of linear functionals; multiplying by the constant $i$ shows $a$ is a smooth $\mathfrak{u}(1)$-valued $1$-form, $a\in\Omega^1(S^{2n+1};\mathfrak{u}(1))$. Thus $a$ is a legitimate candidate connection form, and the two axioms below are meaningful.
>
> **Step 1 — the fundamental-field axiom $a(\xi_P)=\xi$.** Let $\xi=si\in\mathfrak{u}(1)$ be arbitrary, $s\in\mathbb{R}$. By Lemma 1(iii) its fundamental field is $\xi_P(z)=s\,iz=s\,v(z)$. Substituting into $a$ and using bilinearity of the inner product,
> $$a_z(\xi_P(z))=a_z\big(s\,v(z)\big)=s\,\langle v(z),v(z)\rangle\,i=s\,|v(z)|^2\,i\qquad(\text{definition of }a\text{; }\langle v(z),v(z)\rangle=|v(z)|^2)$$
> $$=s\cdot 1\cdot i=si=\xi\qquad(\text{by Lemma 1(iv), }|v(z)|^2=1).$$
> Hence $a(\xi_P)=\xi$ for every $\xi\in\mathfrak{u}(1)$: axiom (2) holds. (Because both $\xi\mapsto\xi_P$ and $a$ are linear in $\xi$, checking the generator $\xi=i$ would already suffice; we verified the general case directly.)
>
> **Step 1 uses** Lemma 1(iii) and Lemma 1(iv). **Its role:** it is condition (2) for a connection form, and the exact equality (no scalar error) is where the unit length of $v(z)$ is consumed.
>
> **Step 2 — the equivariance axiom $R_\lambda^{*}a=\operatorname{Ad}_{\lambda^{-1}}a$.** Fix $\lambda\in U(1)$, $z\in S^{2n+1}$, and $u\in T_zS^{2n+1}$. By definition of pullback and Lemma 1(ii) ($dR_\lambda|_z(u)=\lambda u$),
> $$(R_\lambda^{*}a)_z(u)=a_{R_\lambda(z)}\big(dR_\lambda|_z(u)\big)=a_{\lambda z}(\lambda u)=\langle v(\lambda z),\lambda u\rangle\,i\qquad(\text{definition of }a\text{ at the point }\lambda z).$$
> By Lemma 1(v), $v(\lambda z)=\lambda\,v(z)$, so $\langle v(\lambda z),\lambda u\rangle=\langle\lambda\,v(z),\lambda u\rangle$. Since $m_\lambda$ is an isometry (Lemma 1(i)),
> $$\langle\lambda\,v(z),\lambda u\rangle=\langle v(z),u\rangle\qquad(\text{multiplication by }\lambda\text{ preserves }\langle\cdot,\cdot\rangle).$$
> Combining the last two displays,
> $$(R_\lambda^{*}a)_z(u)=\langle v(z),u\rangle\,i=a_z(u),$$
> so $R_\lambda^{*}a=a$. Finally, because $U(1)$ is abelian, Lemma 2 gives $\operatorname{Ad}_{\lambda^{-1}}=\operatorname{id}_{\mathfrak{u}(1)}$, so $\operatorname{Ad}_{\lambda^{-1}}a=a$ as well. Therefore
> $$R_\lambda^{*}a=a=\operatorname{Ad}_{\lambda^{-1}}a,$$
> which is axiom (1) for every $\lambda\in U(1)$.
>
> **Step 2 uses** Lemma 1(i), (ii), (v) and Lemma 2. **Its role:** it is condition (1); the abelian reduction (Lemma 2) is the sole reason the plain invariance $R_\lambda^{*}a=a$ delivered by the isometric action is already the required equivariance.
>
> **Conclusion of (a).** By Step 0 the form $a$ is a smooth $\mathfrak{u}(1)$-valued $1$-form, and by Steps 1 and 2 it satisfies both defining conditions for a connection form. Hence $a$ is a connection form on the Hopf bundle. This proves (a).
>
> **Step 3 — the horizontal distribution, proving (b).** For $u\in T_zS^{2n+1}$,
> $$a_z(u)=0\iff\langle v(z),u\rangle\,i=0\iff\langle v(z),u\rangle=0\qquad(\text{since }i\neq 0\text{ in }\mathbb{C}),$$
> so $H_z=\ker a_z=\{u\in T_zS^{2n+1}:\langle v(z),u\rangle=0\}$, the orthogonal complement of $v(z)$ taken *inside* the tangent space. Because $v(z)\in T_zS^{2n+1}$ (Lemma 1(iv)) and $T_zS^{2n+1}=z^{\perp}$, this is $H_z=\{z,\,iz\}^{\perp}=v^{\perp}$, of real dimension $2n$. This proves (b). (The vertical line is $V_z=\mathbb{R}\,v(z)$, the tangent to the fibre circle, and $T_zS^{2n+1}=H_z\oplus V_z$ is an orthogonal decomposition.)
>
> **Step 4 — uniqueness, proving (c).** Suppose $\omega$ is any connection form on the Hopf bundle with $\ker\omega=v^{\perp}=\ker a$. Both $\omega$ and $a$ are connection forms (the latter by part (a)) with the same kernel at every point, so by Lemma 3 they are equal: $\omega=a$. Hence $a$ is the unique connection form whose horizontal distribution is $v^{\perp}$. This proves (c), and completes the proof. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Riemannian submersions and O'Neill's formula.** The projection $\pi\colon(S^{2n+1},\text{round})\to(\mathbb{CP}^n,\text{Fubini–Study})$ is a Riemannian submersion whose vertical distribution is the fibre tangent line and whose horizontal distribution is exactly $v^{\perp}$. O'Neill's curvature formulas express the base curvature in terms of the total-space curvature and the "A-tensor" $A_XY=$ vertical part of $[\,X,Y\,]$ for horizontal $X,Y$; the Hopf connection is the connection whose horizontal spaces are the O'Neill horizontal spaces, and its curvature *is* the A-tensor. The theorem applies because the horizontal distribution of a Riemannian submersion with isometric structure group is precisely $V^{\perp}$; the non-obvious content is that the gauge-theoretic curvature $2$-form and the differential-geometric A-tensor are the same object.

**Berry phase in quantum mechanics.** A normalised state vector in $\mathbb{C}^{n+1}$ is a point of $S^{2n+1}$, and two states differing by a global phase — a point of $\mathbb{CP}^n$, the space of physical states — are related by the $U(1)$-action. The Hopf connection $a$ is the connection whose holonomy around a loop of physical states is the Berry phase. The theorem applies because the physical state space is exactly the Hopf base and the phase ambiguity is exactly the circle fibre; the non-obvious step is recognising that the adiabatic phase acquired by a slowly varying Hamiltonian is the parallel transport of $a$, so the enclosed Fubini–Study area gives the phase.

**Magnetic monopoles and the Dirac quantisation condition.** For $n=1$ the base is $S^2$ and the Hopf connection is the vector potential of a magnetic monopole of unit charge sitting at the centre; its curvature integrates to $2\pi i$, which is the statement that the total flux is quantised. The theorem applies because a monopole potential is a connection on the nontrivial $U(1)$-bundle over $S^2$, and the Hopf bundle *is* that bundle; the non-obvious point, which the pairing with Chern–Weil makes precise, is that the integrality of the Chern number is the same fact as Dirac's charge quantisation.

---

# Bridges

- **The product connection and the failure of triviality.** On a *trivial* bundle $M\times G$ the canonical connection is $\operatorname{pr}_2^{*}\theta$, the pullback of the [[Def - The Maurer-Cartan Form|Maurer–Cartan form]], and it is flat. The Hopf connection is the analogue for a bundle that is *not* trivial, and the contrast is instructive: because there is no global section of the Hopf bundle, there is no global "identity gauge" in which the connection form vanishes, and its curvature cannot be made zero. The construction here — orthogonal projection using an invariant metric — is precisely the tool that supplies a connection when the trivialisation-based construction is unavailable.

- **Local connection forms in the two standard sections.** Restricting $a$ to the two standard local sections $s_1,s_2$ of the Hopf bundle over $S^2$ produces two gauge potentials $A_1=s_1^{*}a$ and $A_2=s_2^{*}a$ that differ by the pure-gauge term of the transition function $g_{12}(z,t)=z/|z|$, namely $A_2=A_1+g_{12}^{-1}dg_{12}=A_1+i\,d\arg z$; this concrete computation is carried out in [[Ex - Connection Forms of the Hopf Connection in the Two Local Sections]] and is the smallest nontrivial instance of the general transformation law for local connection forms.

- **The tautological line bundle.** The associated bundle $S^{2n+1}\times_{U(1)}\mathbb{C}$ is canonically the tautological line bundle $\mathcal{O}(-1)\to\mathbb{CP}^n$, and the connection induced on it by $a$ is the Hermitian connection obtained by projecting the flat ambient derivative onto the tautological line. This is the bridge from a principal connection to a covariant derivative on a genuine vector bundle, developed in [[Ex - The Induced Connection on the Tautological Bundle from the Hopf Connection]]; it is how the Hopf connection enters the theory of holomorphic line bundles and Chern classes.

---

# Unlocked by This

> [!tip] Curvature and the first Chern number *(from Chern–Weil theory)*
> Because $U(1)$ is abelian, the curvature of $a$ is simply $\Omega=da$, a closed $\mathfrak{u}(1)$-valued $2$-form; on $S^3$ it equals $2(dx_0\wedge dx_1+dx_2\wedge dx_3)i$, and its integral over $\mathbb{CP}^1$ computes the first Chern number of $\mathcal{O}(-1)$. This is the first characteristic number of the series and identifies the Hopf bundle as the generator of the circle bundles over $S^2$. See [[Ex - Curvature of the Standard Hopf Connection]] and chapter VI.

> [!tip] Non-integrability and holonomy *(from the theory of distributions)*
> The horizontal distribution $v^{\perp}$ is not involutive — the bracket of two horizontal lifts has a nonzero vertical part equal to the curvature — so by the [[Thm - The Frobenius Theorem|Frobenius theorem]] it is not integrable, and horizontal transport around a base loop returns to the fibre rotated by the enclosed area. This is the geometric content of holonomy, developed in chapter V, and the reason the Hopf connection carries physical information. See [[Ex - The Horizontal Distribution of the Hopf Connection is Not Integrable]].
