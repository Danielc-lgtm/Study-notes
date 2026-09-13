---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Reduction and Extension of the Structure Group"
  - "Def - Euclidean Vector Bundle and Metric Connection"
  - "Def - Complex Vector Bundle and Hermitian Structure"
  - "Def - Frame Bundle of a Vector Bundle"
  - "Def - Principal G-Bundle"
  - "Thm - Gram-Schmidt Procedure"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $E\to M$ is a smooth real [[Def - Vector Bundle|vector bundle]] of rank $k$ over a smooth manifold $M$, and $\operatorname{Fr}(E)$ is its **[[Def - Frame Bundle of a Vector Bundle|frame bundle]]**, the principal $GL_k(\mathbb R)$-bundle whose fibre over $m\in M$ is the set $\operatorname{Fr}(E_m)$ of ordered bases of $E_m$. We identify an ordered basis $(b_1,\dots,b_k)$ of $E_m$ with the linear isomorphism $p\colon\mathbb R^k\to E_m$ determined by $p(e_i)=b_i$, where $e_1,\dots,e_k$ is the standard basis of $\mathbb R^k$; thus $p(x)=\sum_{i=1}^k x_i\,b_i$ for $x=(x_1,\dots,x_k)^t\in\mathbb R^k$. The group $GL_k(\mathbb R)$ acts on $\operatorname{Fr}(E)$ **on the right** by $p\cdot h=p\circ h$, so that $(p\cdot h)(x)=p(hx)$; this is the series convention (right actions on principal bundles).

For a closed (hence embedded) Lie subgroup $G\le GL_k(\mathbb R)$, a $G$-structure (see **[[Def - Reduction and Extension of the Structure Group|reduction of the structure group]]**) on $E$ is a $G$-subbundle $P\subset\operatorname{Fr}(E)$: an embedded submanifold, invariant under the right $G$-action, that is itself a principal $G$-bundle over $M$ (so each fibre $P_m:=P\cap\operatorname{Fr}(E_m)$ is a single $G$-orbit). We write $x^t$ for the transpose of $x\in\mathbb R^k$, $\bar x$ for the entrywise complex conjugate of $x\in\mathbb C^m$, $x^*=\bar x^t$ for the conjugate transpose, and $\delta_{ij}$ for the Kronecker delta. The named subgroups are
$$O(k)=\{h\in GL_k(\mathbb R):h^th=\mathbb 1\},\quad SL_k(\mathbb R)=\{h:\det h=1\},\quad GL_k^+(\mathbb R)=\{h:\det h>0\},$$
$$GL_m(\mathbb C)=\{A\in GL_{2m}(\mathbb R):A\,I_{\mathrm{st}}=I_{\mathrm{st}}\,A\},\quad U(m)=O(2m)\cap GL_m(\mathbb C),$$
where $\mathbb 1$ is the identity matrix and $I_{\mathrm{st}}$ is the **standard complex structure** on $\mathbb R^{2m}$,
$$I_{\mathrm{st}}(x_1,y_1,\dots,x_m,y_m)=(-y_1,x_1,\dots,-y_m,x_m),\qquad I_{\mathrm{st}}^2=-\mathbb 1.$$
A **[[Def - Euclidean Vector Bundle and Metric Connection|Euclidean structure]]** on $E$ is a smooth family $\langle\cdot,\cdot\rangle=(\langle\cdot,\cdot\rangle_m)_{m\in M}$ of inner products on the fibres (smoothness meaning that $m\mapsto\langle s_1(m),s_2(m)\rangle_m$ is smooth for all smooth sections $s_1,s_2$). A **fibrewise volume form** is a nowhere-vanishing section $\mu\in\Gamma(\Lambda^kE^*)$. A **[[Def - Complex Vector Bundle and Hermitian Structure|complex structure]]** on $E$ (for $k=2m$ even) is a section $I\in\Gamma(\operatorname{End}E)$ with $I^2=-\mathbb 1$; a **[[Def - Complex Vector Bundle and Hermitian Structure|Hermitian structure]]** on such a complex bundle is a smooth family of Hermitian inner products (sesquilinear, positive definite, and $\mathbb C$-compatible: $\langle Iv,w\rangle=i\langle v,w\rangle$). An **[[Def - Orientation of a Smooth Manifold|orientation]]** of $E$ is a choice of orientation of each fibre such that every point has a neighbourhood carrying a local frame that is positively oriented at every point.

> [!warning] Convention: rank versus complex dimension
> Haydys writes the complex cases with the letter $k$ for the *complex* dimension, so his groups read $GL_k(\mathbb C)\subset GL_{2k}(\mathbb R)$ and $U(k)$. We reserve $k=\operatorname{rk}_{\mathbb R}E$ for the real rank throughout and write $k=2m$ in the complex cases, so the complex rank is $m=k/2$ and the groups are $GL_m(\mathbb C)$ and $U(m)$. The two conventions agree under $k_{\text{Haydys}}\leftrightarrow m_{\text{ours}}$. Bär's table (Example 2.2.6) uses $n=\operatorname{rk}_{\mathbb K}$ and lists $GL(n;\mathbb K),O(n),U(n),GL^+(n;\mathbb R),SO(n)$; his $U(n)$ is our $U(m)$ with $n=m$.

The full symbol registry for the chapter is on [[Gauge Theory III — Fibre Bundles, Principal Bundles, and Associated Bundles]].

---

# Statement

> **Theorem (extra fibre structure $=$ reduction of the structure group).** Let $E\to M$ be a smooth real vector bundle of rank $k$, with frame bundle $\operatorname{Fr}(E)$. Then there are natural bijections between geometric structures on $E$ and reductions of its structure group, as follows.
>
> 1. **(Euclidean $\leftrightarrow$ $O(k)$.)** Euclidean structures $\langle\cdot,\cdot\rangle$ on $E$ correspond bijectively to $O(k)$-structures $P\subset\operatorname{Fr}(E)$, by
> $$\langle\cdot,\cdot\rangle\ \longmapsto\ O(E):=\{p\in\operatorname{Fr}(E):p\text{ is orthonormal}\},\qquad P\ \longmapsto\ \big(\langle p x_1,p x_2\rangle:=x_1^tx_2,\ p\in P_m\big).$$
> 2. **(Volume form $\leftrightarrow$ $SL_k(\mathbb R)$.)** Fibrewise volume forms $\mu\in\Gamma(\Lambda^kE^*)$ correspond bijectively to $SL_k(\mathbb R)$-structures, by $\mu\mapsto\{p:\mu(pe_1,\dots,pe_k)=1\}$ and, conversely, $P\mapsto\mu_m:=(p^{-1})^*(e^1\wedge\cdots\wedge e^k)$ for any $p\in P_m$.
> 3. **(Complex structure $\leftrightarrow$ $GL_m(\mathbb C)$.)** For $k=2m$, complex structures $I\in\Gamma(\operatorname{End}E)$ ($I^2=-\mathbb 1$) correspond bijectively to $GL_m(\mathbb C)$-structures, by $I\mapsto\{p:p\,I_{\mathrm{st}}=I\,p\}$ and, conversely, $P\mapsto I_m:=p\,I_{\mathrm{st}}\,p^{-1}$ for any $p\in P_m$.
> 4. **(Orientation $\leftrightarrow$ $GL_k^+(\mathbb R)$.)** Orientations of $E$ correspond bijectively to $GL_k^+(\mathbb R)$-structures, by sending an orientation to the open subbundle $\operatorname{Fr}^+(E)$ of positively oriented frames, and a $GL_k^+$-structure $P$ to the orientation whose positive frames are exactly those in $P$.
> 5. **(Hermitian $\leftrightarrow$ $U(m)$.)** If $E$ carries a complex structure $I$ (so $k=2m$), Hermitian structures on $(E,I)$ correspond bijectively to $U(m)$-structures $P\subset\operatorname{Fr}(E)$; every such $P$ satisfies $P\subset\{p:p\,I_{\mathrm{st}}=I\,p\}$, so a $U(m)$-reduction refines the $GL_m(\mathbb C)$-reduction determined by $I$.
>
> In each case the two displayed maps are mutually inverse. Moreover every real vector bundle over a manifold admits a Euclidean structure, so every rank-$k$ real bundle admits an $O(k)$-reduction.

---

# Motivation

A vector bundle in the sense of the frame bundle is a *bare* object: its structure group is the whole of $GL_k(\mathbb R)$, meaning that at each point every ordered basis is on an equal footing with every other, and the transition functions of the bundle are allowed to be arbitrary invertible matrices. Most bundles that arise in geometry are not bare. The tangent bundle of a Riemannian manifold has a length in every fibre; a complex line bundle has a way of multiplying by $i$; an oriented surface has a consistent sense of rotation. Each of these is an *extra structure* laid over the bare bundle, and each of them privileges some frames over others: the orthonormal frames, the complex-linear frames, the positively oriented frames.

The question the theorem answers is: what is the exact relationship between "an extra structure on the fibres" and "a restriction on the allowed frames"? The answer is that the two are the same information, packaged differently. To have an inner product in every fibre is *precisely* to have singled out, in every fibre, the orthonormal bases; and the set of all orthonormal bases, assembled across the base, is a principal $O(k)$-bundle sitting inside $\operatorname{Fr}(E)$. Conversely, once you have singled out such a sub-collection of frames, you can *read off* the inner product from it — declare the chosen frames orthonormal, and every other inner-product value is forced by bilinearity. Nothing is lost in translation.

This is the content of a **[[Def - Reduction and Extension of the Structure Group|reduction of the structure group]]**. The general principle — extra structure $\leftrightarrow$ reduction of the structure group to the symmetry group of the structure — is the organising idea of the whole subject. It is why gauge theory can speak interchangeably of "a metric" and "an $O(k)$-bundle", of "a complex structure" and "a $GL_m(\mathbb C)$-bundle", of "a Hermitian metric" and "a $U(m)$-bundle". The theorem below is the dictionary that makes this interchangeability precise and, crucially, *smooth*: the hard part is never the pointwise linear algebra but the verification that the chosen frames assemble into a genuine smooth subbundle, and that the reconstructed structure varies smoothly over $M$. That smoothness is supplied, in the metric cases, by the observation that the Gram–Schmidt formulas are smooth in their inputs.

We assume the reader is fluent with vector bundles, the frame bundle as a principal $GL_k(\mathbb R)$-bundle, the notion of a $G$-subbundle, and finite-dimensional inner-product and complex linear algebra. The only genuinely new ingredient over the pointwise linear algebra is the packaging of "adapted frames" into a subbundle and the smoothness bookkeeping.

---

# Sources and Targets

**Sources (Input Broadening).** The theorem's literal input is one of five kinds of fibre structure; the skill is recognising when a problem secretly hands you one.

The first disguised source is **a bundle that arises as a subbundle of a trivial bundle, or as the tangent bundle of a submanifold of Euclidean space.** Any such bundle inherits an inner product by restriction of the ambient dot product — the property "sits inside $\underline{\mathbb R}^N$" bridges to "carries a Euclidean structure", and the theorem then converts that into an $O(k)$-reduction. For instance the tangent bundle of any embedded surface $\Sigma\subset\mathbb R^3$ acquires the first fundamental form, hence an $SO(2)=U(1)$-structure once an orientation is fixed, which is exactly the data that makes $T\Sigma$ into a complex line bundle and $\Sigma$ into a Riemann surface. *Example problem:* deduce that an oriented Riemannian surface is a complex manifold by chaining the $O(2)$-reduction (metric) and the $GL_1(\mathbb C)$-reduction (rotation by ninety degrees) into a single $U(1)$-reduction.

The second disguised source is **a bundle equipped with a nowhere-vanishing top section of a determinant line, or a nowhere-vanishing top form.** Whenever a rank-$k$ bundle carries a trivialisation of $\Lambda^kE$ (equivalently of $\Lambda^kE^*$), the property "$\Lambda^kE$ is trivial" bridges to "$E$ has a fibrewise volume form", which the theorem turns into an $SL_k(\mathbb R)$-reduction. This is the source that appears in symplectic and Calabi–Yau geometry, where a holomorphic volume form reduces the structure group to $SL_m(\mathbb C)$. *Example problem:* show that a bundle with a fibrewise volume form and a Euclidean structure has structure group $SL_k(\mathbb R)\cap O(k)=SO(k)$, so the two reductions combine to an orientation-plus-metric package.

The third disguised source is **an action of a field larger than $\mathbb R$ on the fibres, or a periodicity operator.** If a real bundle admits an endomorphism squaring to $-\mathbb 1$, the property "the fibres are modules over $\mathbb C$" bridges to "$E$ is a complex bundle", giving a $GL_m(\mathbb C)$-reduction; more exotically, a triple $I,J,K$ with quaternionic relations gives an $Sp(m)$-reduction by the same mechanism. The non-obvious step is to *notice* that a naturally occurring operator (multiplication by a root of unity, a Hodge-type operator, the almost-complex structure of a symplectic manifold after choosing a compatible metric) squares to $-\mathbb 1$. *Example problem:* on a symplectic vector bundle $(E,\omega)$ choose a compatible metric $g$ and set $I:=g^{-1}\omega$ (as bundle maps); verify $I^2=-\mathbb 1$ and read off the $U(m)$-reduction, recovering the statement that $Sp(2m,\mathbb R)$ and $U(m)$ are homotopy equivalent as structure groups.

**Targets (Output Amplification).** The bare output is a bijection of two kinds of data; combined with other facts it does much more.

Combine the correspondence with **the existence of Riemannian metrics via a partition of unity**. By [[Thm - Existence of Smooth Partitions of Unity|the existence of smooth partitions of unity]] — a locally finite open cover $\{U_\alpha\}$ of $M$ admits smooth functions $\rho_\alpha\ge0$ supported in $U_\alpha$ with $\sum_\alpha\rho_\alpha\equiv1$ — one patches the flat inner products $\langle\cdot,\cdot\rangle^\alpha$ pulled back through local trivialisations: $\langle\cdot,\cdot\rangle:=\sum_\alpha\rho_\alpha\langle\cdot,\cdot\rangle^\alpha$. A convex combination of inner products is again an inner product (positive definiteness is preserved because $\langle v,v\rangle=\sum_\alpha\rho_\alpha\langle v,v\rangle^\alpha>0$ whenever $v\neq0$, since at least one $\rho_\alpha(m)>0$ and each summand is nonnegative), so $E$ acquires a Euclidean structure, and part 1 turns it into an $O(k)$-reduction. The payoff is that **every** rank-$k$ real vector bundle reduces from $GL_k(\mathbb R)$ to $O(k)$: the general linear structure group is never an obstruction, and one may always assume a metric is present. (This is the last clause of the Statement, and it is proved in full on [[Thm - Existence of Riemannian Metrics via Partitions of Unity|the existence of Riemannian metrics page]] for $E=TM$; the same argument works for any $E$.)

Combine the correspondence with **the classification of bundles by their structure group**. Once a bundle is known to reduce to $O(k)$, its transition functions may be taken orthogonal, and further topological reductions ($O(k)\to SO(k)$, $SO(2)\to U(1)$, and so on) become questions about the connectedness and homotopy of the structure group. The payoff is that the existence of an orientation, a complex structure, or a spin structure is recast as a lifting problem for the structure group — the mechanism behind Stiefel–Whitney and Chern-class obstructions. In particular, part 4 identifies orientability of $E$ with the reducibility of $O(k)$ to $SO(k)$, i.e. with $\operatorname{Fr}(E)$ having a two-component sub-object over each point.

Combine the correspondence with **connections**. A metric connection on a Euclidean bundle is exactly a connection on the associated $O(k)$-structure; a unitary connection on a Hermitian bundle is a connection on the $U(m)$-structure. The payoff, developed in chapter IV, is that the curvature of such a connection then takes values in the Lie algebra of the reduced structure group ($\mathfrak{so}(k)$, $\mathfrak u(m)$), which is what makes the Chern–Weil construction of characteristic classes produce integral, structure-specific invariants.

---

# Why Is It True

Fix a single fibre $E_m$, a $k$-dimensional real vector space, and ask what a frame $p\colon\mathbb R^k\to E_m$ is *for*. A frame is a translator: it carries any structure on $\mathbb R^k$ over to $E_m$ and, running backwards, carries any structure on $E_m$ back to $\mathbb R^k$. The dot product on $\mathbb R^k$ becomes an inner product on $E_m$; the standard orientation becomes an orientation of $E_m$; the operator $I_{\mathrm{st}}$ becomes a complex structure. Two frames related by $p'=p\cdot h$ translate the *same* model structure on $\mathbb R^k$ into the *same* structure on $E_m$ if and only if $h$ preserves the model structure — that is, if and only if $h$ lies in the model structure's symmetry group $G$.

This is the whole mechanism, and it can be said in one sentence.

> **A structure of a given type on $E_m$ is the same thing as a $G$-orbit of frames, where $G\le GL_k(\mathbb R)$ is the subgroup fixing the model structure on $\mathbb R^k$; assembling these orbits over all of $M$ turns "a smooth field of structures" into "a smooth $G$-subbundle of $\operatorname{Fr}(E)$".**

Concretely, take the Euclidean case and the smallest example, a rank-$1$ bundle. A frame of a line $E_m$ is a nonzero vector $b$; the "inner products" on a line are just the assignments $\langle b,b\rangle=c$ for some $c>0$; the orthonormal frames are the two unit vectors $\pm b/\sqrt c$. The symmetry group of the standard inner product on $\mathbb R^1$ is $O(1)=\{\pm1\}$, and indeed the two unit vectors form a single $O(1)$-orbit. So "an inner product on a line" $=$ "a pair of opposite unit vectors" $=$ "an $O(1)$-orbit of frames" — exactly the claim. In rank $k$, the orthonormal frames of a given inner product form one $O(k)$-orbit because any two orthonormal bases differ by an orthogonal change of basis, and conversely declaring one $O(k)$-orbit "orthonormal" pins down the inner product because bilinearity extends the values $\langle b_i,b_j\rangle=\delta_{ij}$ to all pairs.

The reason the five cases look identical is that they *are* identical at this level: each is the statement "model structure with symmetry group $G$", instantiated with a different model. The dot product gives $O(k)$; the standard top form gives $SL_k(\mathbb R)$ (its symmetry group is the volume-preserving maps, i.e. $\det=1$); the operator $I_{\mathrm{st}}$ gives $GL_m(\mathbb C)$ (its symmetry group is the maps commuting with $I_{\mathrm{st}}$, i.e. the complex-linear ones); the standard orientation gives $GL_k^+(\mathbb R)$ (the determinant-positive maps); the standard Hermitian form gives $U(m)$ (the unitary maps). The only case-by-case work is (i) computing the symmetry group of each model, (ii) checking that any fibre structure of that type really is a translate of the model (so the orbit is nonempty), and (iii) verifying smoothness — that the adapted frames can be chosen smoothly, and that the reconstructed structure varies smoothly. Steps (i) and (ii) are one-line linear algebra; step (iii) is where the metric cases invoke that Gram–Schmidt is a smooth operation.

---

# What Makes This Hard

The pointwise linear algebra is easy; the two places to slip are both about *smoothness and global assembly*, not about any single fibre. First, one must produce a smooth field of adapted frames — a smooth orthonormal local frame, a smooth complex-linear local frame — and it is not enough to note that each fibre has an orthonormal basis, because a fibrewise choice need not be smooth. The fix is that Gram–Schmidt is not merely an existence theorem but an explicit formula built from the operations $+$, $-$, scalar multiplication, division by a nowhere-vanishing smooth positive function, and a smooth square root; feeding a smooth frame in yields a smooth frame out. Second, in the reverse direction one must check that the reconstructed structure is independent of the frame chosen in each fibre; this is exactly the $G$-invariance of the model structure, applied in the form $p'=p\cdot h$ with $h\in G$, and it is the step where the definition of $G$ as the model's stabiliser is actually used. A common error is to prove only the pointwise correspondence and declare victory, leaving both smoothness verifications unspoken; another is to forget that a $G$-subbundle must be an *embedded* submanifold, which here follows because the adapted trivialisation identifies it locally with $U\times G$ and each of the five groups is an embedded subgroup of $GL_k(\mathbb R)$.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Set up one abstract correspondence — "smooth field of model-type structures $\leftrightarrow$ $G$-subbundle of adapted frames", where $G$ is the stabiliser of the model — and prove it once. Then run each of the five cases through it, supplying only three case-specific facts: the model structure and its stabiliser, the pointwise equivalence of any structure of that type to the model, and a smooth adapted local frame.

**Subgoal decomposition:**

1. **Frames transport structures, and pullback is a right action.** For a frame $p\colon\mathbb R^k\to E_m$, define the pullback $p^*\sigma$ of a fibre structure $\sigma$ on $E_m$, and check $(p\cdot h)^*\sigma=h^*(p^*\sigma)$. Identify, for each of the five models $\sigma_0$ on $\mathbb R^k$, the stabiliser $\{h:h^*\sigma_0=\sigma_0\}$ as the named group.
   - *Hint:* Inner product pulls back by $(p^*g)(x,y)=g(px,py)$; a top form by $(p^*\mu)(x_1,\dots,x_k)=\mu(px_1,\dots,px_k)$; an endomorphism by $p^*I=p^{-1}Ip$; an orientation and a Hermitian form likewise.
   - *Why needed:* The right-action property is what makes "adapted frames form a $G$-orbit" true, and the stabiliser computations are what name the reduction group.

2. **The abstract correspondence.** Given the mechanism of subgoal 1, show that $\sigma\mapsto P^\sigma:=\{p:p^*\sigma_{\pi(p)}=\sigma_0\}$ and $P\mapsto\sigma^P$ (defined fibrewise by $(p^{-1})^*\sigma_0$) are mutually inverse bijections between fibre-structure fields and $G$-subbundles, once smoothness is granted on both sides.
   - *Hint:* Nonemptiness of $P^\sigma_m$ is pointwise equivalence of $\sigma_m$ to the model; single-orbit-ness and independence of the representative both come from the stabiliser computation.
   - *Why needed:* It reduces all five cases to smoothness inputs.

3. **Smoothness inputs, case by case.** Produce a smooth adapted local frame in each case, and check the reconstructed structure is smooth.
   - *Hint:* Gram–Schmidt (Euclidean, Hermitian); rescale one vector (volume); an $I$-adapted frame $(v_1,Iv_1,\dots)$ (complex); openness of $GL_k^+$ (orientation).
   - *Why needed:* Without it $P^\sigma$ is only a set-theoretic sub-object, not a smooth subbundle.

4. **Assemble and record the corollary.** Combine subgoals 1–3 for each case; then note that a partition-of-unity metric shows every bundle admits an $O(k)$-reduction.

---

# Lemma Decomposition

> [!note]- Lemma 1: Frames transport fibre structures, pullback is a right action, and the five models have the five named stabilisers
> **Statement:** Let $V$ be a $k$-dimensional real vector space and $p\colon\mathbb R^k\to V$ a linear isomorphism. For a fibre structure $\sigma$ on $V$ define its pullback $p^*\sigma$ on $\mathbb R^k$ by
> $$(p^*g)(x,y)=g(px,py),\quad (p^*\mu)(x_1,\dots,x_k)=\mu(px_1,\dots,px_k),\quad p^*I=p^{-1}Ip,$$
> with an orientation pulled back by pulling back any representing top form ($p^*o:=$ the sign class of $p^*\mu$ for $\mu$ representing $o$) and a Hermitian form pulled back by the same formula as an inner product, $(p^*\langle\cdot,\cdot\rangle)(x,y)=\langle px,py\rangle$. Then for $h\in GL_k(\mathbb R)$,
> $$(p\circ h)^*\sigma=h^*(p^*\sigma).$$
> With the standard models on $\mathbb R^k$ — dot product $g_0(x,y)=x^ty$; top form $\mu_0=e^1\wedge\cdots\wedge e^k$; operator $I_{\mathrm{st}}$; standard orientation $o_0$; standard Hermitian form $h_0(x,y)=\bar x^ty$ on $\mathbb C^m=(\mathbb R^{2m},I_{\mathrm{st}})$ — the stabiliser $\{h:h^*\sigma_0=\sigma_0\}$ equals, respectively, $O(k)$, $SL_k(\mathbb R)$, $GL_m(\mathbb C)$, $GL_k^+(\mathbb R)$, and $U(m)$.
>
> **Hint:** Each pullback is manifestly a right action; each stabiliser is the definition of the named group after unwinding the pullback formula. For the Hermitian case use that preserving the complex-valued form is preserving both its real and imaginary parts.
>
> **Why needed:** The right-action identity makes the adapted frames in a fibre a single $G$-orbit; the stabiliser computations name the reduction group in each of the five cases.
>
> > [!note]- Full proof
> > **The right-action identity.** For the inner-product case, using $(p\circ h)(x)=p(hx)$,
> > $$\big((p\circ h)^*g\big)(x,y)=g\big((p\circ h)x,(p\circ h)y\big)=g\big(p(hx),p(hy)\big)=(p^*g)(hx,hy)=\big(h^*(p^*g)\big)(x,y),$$
> > by the definitions of the pullback and of $p\circ h$. For the volume-form case the same substitution gives $\big((p\circ h)^*\mu\big)(x_1,\dots,x_k)=\mu\big(p(hx_1),\dots,p(hx_k)\big)=\big(h^*(p^*\mu)\big)(x_1,\dots,x_k)$. For the endomorphism case,
> > $$(p\circ h)^*I=(p\circ h)^{-1}\,I\,(p\circ h)=h^{-1}p^{-1}Iph=h^{-1}(p^*I)h=h^*(p^*I),$$
> > using $(p\circ h)^{-1}=h^{-1}\circ p^{-1}$. Orientations pull back by pulling back any representing top form, so the identity follows from the volume-form case; Hermitian forms pull back exactly like inner products, so the identity follows from the first computation. In every case $(p\circ h)^*\sigma=h^*(p^*\sigma)$, which is the statement that pullback is a right action of $GL_k(\mathbb R)$.
> >
> > **Stabiliser of $g_0$.** We have $h^*g_0=g_0$ iff $(hx)^t(hy)=x^ty$ for all $x,y\in\mathbb R^k$, iff $x^t(h^th)y=x^ty$ for all $x,y$, iff $h^th=\mathbb 1$ (take $x=e_i$, $y=e_j$ to read off the entries), iff $h\in O(k)$.
> >
> > **Stabiliser of $\mu_0$.** For a top form, $\mu_0(hx_1,\dots,hx_k)=\det(h)\,\mu_0(x_1,\dots,x_k)$ (this is the defining property of the determinant as the factor by which a linear map scales the top exterior power; see [[Thm - Determinant is Multiplicative|the determinant]] and [[Def - Alternating Multilinear Form|alternating forms]]). Hence $h^*\mu_0=\mu_0$ iff $\det h=1$, iff $h\in SL_k(\mathbb R)$.
> >
> > **Stabiliser of $I_{\mathrm{st}}$.** We have $h^*I_{\mathrm{st}}=I_{\mathrm{st}}$ iff $h^{-1}I_{\mathrm{st}}h=I_{\mathrm{st}}$, iff $I_{\mathrm{st}}h=hI_{\mathrm{st}}$, iff $h\in GL_m(\mathbb C)$ by the definition of $GL_m(\mathbb C)$ as the real matrices commuting with $I_{\mathrm{st}}$.
> >
> > **Stabiliser of $o_0$.** An orientation is the sign class of a top form; $h^*o_0=o_0$ iff $h$ maps a positively oriented basis to a positively oriented basis, iff $\det h>0$, iff $h\in GL_k^+(\mathbb R)$, again by the determinant scaling property.
> >
> > **Stabiliser of $h_0$.** For a real-linear $h\in GL_{2m}(\mathbb R)$, $h^*h_0=h_0$ means $h_0(hx,hy)=h_0(x,y)$ for all $x,y\in\mathbb C^m$ as complex numbers. Writing $h_0=g_0+i\,\omega_0$ with $g_0=\operatorname{Re}h_0$ the standard Euclidean product on $\mathbb R^{2m}$ and $\omega_0=\operatorname{Im}h_0$ the standard symplectic form, the equation splits into $h^*g_0=g_0$ and $h^*\omega_0=\omega_0$, i.e. $h\in O(2m)$ and $h$ preserves $\omega_0$. Since $\omega_0(x,y)=g_0(I_{\mathrm{st}}x,y)$, preserving both $g_0$ and $\omega_0$ forces $g_0(I_{\mathrm{st}}hx,y)=\omega_0(hx,h(h^{-1}y))=\omega_0(x,h^{-1}y)=g_0(I_{\mathrm{st}}x,h^{-1}y)=g_0(hI_{\mathrm{st}}x,y)$ for all $x,y$, hence $I_{\mathrm{st}}h=hI_{\mathrm{st}}$, so $h\in GL_m(\mathbb C)$. Therefore $\operatorname{Stab}(h_0)=O(2m)\cap GL_m(\mathbb C)=U(m)$. (Conjugation $x\mapsto\bar x$ preserves $g_0$ but sends $h_0$ to $\overline{h_0}$, and so is correctly excluded: it does not preserve $\omega_0$.)

> [!note]- Lemma 2: The abstract reduction correspondence
> **Statement:** Let $\sigma_0$ be a model structure on $\mathbb R^k$ with stabiliser $G=\{h\in GL_k(\mathbb R):h^*\sigma_0=\sigma_0\}$, and suppose $G$ is an embedded Lie subgroup. Call a field $\sigma=(\sigma_m)$ of fibre structures on $E$ **of type $\sigma_0$** if every $\sigma_m$ is pullback-equivalent to $\sigma_0$, i.e. $p^*\sigma_m=\sigma_0$ for some frame $p\in\operatorname{Fr}(E_m)$. For such a field set $P^\sigma:=\{p\in\operatorname{Fr}(E):p^*\sigma_{\pi(p)}=\sigma_0\}$. Then:
> (a) each fibre $P^\sigma_m$ is nonempty and is a single $G$-orbit;
> (b) if in addition $P^\sigma$ admits a smooth local section through each point, then $P^\sigma$ is an (embedded) $G$-subbundle of $\operatorname{Fr}(E)$;
> (c) conversely, for a $G$-subbundle $P$ the field $\sigma^P_m:=(p^{-1})^*\sigma_0$ (any $p\in P_m$) is a well-defined field of type $\sigma_0$;
> (d) the assignments $\sigma\mapsto P^\sigma$ and $P\mapsto\sigma^P$ are mutually inverse.
>
> **Hint:** Everything is the right-action identity of Lemma 1 together with "two $G$-orbits that meet are equal". Well-definedness in (c) is the case where $h\in G$.
>
> **Why needed:** This is the engine; each of the five cases is this lemma plus the case-specific stabiliser (Lemma 1) and a smoothness input (Lemma 3).
>
> > [!note]- Full proof
> > **(a) Nonempty and a single orbit.** Fix $m$. Because $\sigma$ is of type $\sigma_0$, there is a frame $p_0$ with $p_0^*\sigma_m=\sigma_0$, so $p_0\in P^\sigma_m$ and the fibre is nonempty. Let $p,p'\in P^\sigma_m$. Since both are frames of $E_m$, there is a unique $h\in GL_k(\mathbb R)$ with $p'=p\cdot h$ (namely $h=p^{-1}p'$; the $GL_k(\mathbb R)$-action on a fibre of $\operatorname{Fr}(E)$ is free and transitive). Then by the right-action identity of Lemma 1,
> > $$\sigma_0=(p')^*\sigma_m=(p\cdot h)^*\sigma_m=h^*(p^*\sigma_m)=h^*\sigma_0,$$
> > using $p\in P^\sigma_m$ (so $p^*\sigma_m=\sigma_0$) in the last step. Hence $h\in G$, so $p'=p\cdot h$ lies in the $G$-orbit of $p$. Conversely, if $p\in P^\sigma_m$ and $h\in G$ then $(p\cdot h)^*\sigma_m=h^*(p^*\sigma_m)=h^*\sigma_0=\sigma_0$, so $p\cdot h\in P^\sigma_m$. Therefore $P^\sigma_m$ is exactly the $G$-orbit of any one of its points: a single $G$-orbit.
> >
> > **(b) A $G$-subbundle.** By hypothesis each point $m_0$ has a neighbourhood $U$ and a smooth section $s\colon U\to P^\sigma$ (that is, $s(m)\in P^\sigma_m$ for all $m\in U$). Define
> > $$\Psi_U\colon U\times G\longrightarrow \pi^{-1}(U)\cap P^\sigma,\qquad (m,h)\mapsto s(m)\cdot h.$$
> > By part (a), $s(m)\cdot h$ ranges over exactly $P^\sigma_m$ as $h$ ranges over $G$ (single orbit), and the map is injective because the action is free; so $\Psi_U$ is a bijection. It is smooth as the restriction of the smooth map $(m,h)\mapsto s(m)\cdot h$ on $U\times GL_k(\mathbb R)$. Its inverse sends $p\mapsto(\pi(p),\,s(\pi(p))^{-1}p)$, which is smooth because $p\mapsto s(\pi(p))^{-1}p\in GL_k(\mathbb R)$ is smooth and lands in the embedded submanifold $G$ (its values lie in $G$ by part (a), and a smooth map into $GL_k(\mathbb R)$ with image in an embedded submanifold is smooth into that submanifold). Thus $\Psi_U$ is a diffeomorphism onto $\pi^{-1}(U)\cap P^\sigma$, which exhibits $P^\sigma$ as an embedded submanifold locally modelled on $U\times G\subset U\times GL_k(\mathbb R)$, $G$-equivariant ($\Psi_U(m,hh')=\Psi_U(m,h)\cdot h'$), and locally trivial. Hence $P^\sigma$ is a principal $G$-bundle and a $G$-subbundle of $\operatorname{Fr}(E)$.
> >
> > Throughout we use that pullback is **contravariant and functorial**: for composable isomorphisms $(f\circ g)^*=g^*\circ f^*$ and $(\operatorname{id})^*=\operatorname{id}$; the right-action identity of Lemma 1 is the special case $(p\circ h)^*=h^*\circ p^*$. In particular, for any isomorphism $q$ the operations $q^*$ and $(q^{-1})^*$ are mutually inverse, since $q^*\circ(q^{-1})^*=(q^{-1}\circ q)^*=\operatorname{id}$ and $(q^{-1})^*\circ q^*=(q\circ q^{-1})^*=\operatorname{id}$.
> >
> > **(c) The reconstructed field is well-defined and of type $\sigma_0$.** For a $G$-subbundle $P$ and $m\in M$, each fibre $P_m$ is a single $G$-orbit (a $G$-subbundle is a principal $G$-bundle, whose fibres are single orbits). For $p,p'\in P_m$ write $p'=p\cdot h$ with $h\in G$, so that $p'^{-1}=h^{-1}\circ p^{-1}$ as maps $E_m\to\mathbb R^k$. Then, by contravariance,
> > $$(p'^{-1})^*\sigma_0=(h^{-1}\circ p^{-1})^*\sigma_0=(p^{-1})^*\big((h^{-1})^*\sigma_0\big)=(p^{-1})^*\sigma_0,$$
> > where the last step uses $(h^{-1})^*\sigma_0=\sigma_0$: indeed $h\in G$ and $G$ is a group, so $h^{-1}\in G=\{g:g^*\sigma_0=\sigma_0\}$. Hence $\sigma^P_m:=(p^{-1})^*\sigma_0$ is independent of the chosen $p\in P_m$, and by construction $p^*\sigma^P_m=p^*\big[(p^{-1})^*\sigma_0\big]=\sigma_0$, so the field $\sigma^P$ is of type $\sigma_0$.
> >
> > **(d) Mutually inverse.** Start from a field $\sigma$ of type $\sigma_0$ and form $P^\sigma$, then $\sigma^{P^\sigma}$. For $m$ and any $p\in P^\sigma_m$ we have $p^*\sigma_m=\sigma_0$, hence, by mutual inverseness of $(p^{-1})^*$ and $p^*$,
> > $$\sigma^{P^\sigma}_m=(p^{-1})^*\sigma_0=(p^{-1})^*(p^*\sigma_m)=\sigma_m.$$
> > So $\sigma^{P^\sigma}=\sigma$. Conversely, start from a $G$-subbundle $P$ and form $\sigma^P$, then $P^{\sigma^P}=\{p:p^*\sigma^P_{\pi(p)}=\sigma_0\}$. If $p\in P_m$ then $p^*\sigma^P_m=p^*\big[(p^{-1})^*\sigma_0\big]=\sigma_0$, so $p\in P^{\sigma^P}_m$; thus $P_m\subseteq P^{\sigma^P}_m$. Both $P_m$ and $P^{\sigma^P}_m$ are single $G$-orbits in $\operatorname{Fr}(E_m)$ (the former by hypothesis, the latter by part (a) applied to $\sigma^P$), and two $G$-orbits with $P_m\subseteq P^{\sigma^P}_m$ must be equal, because distinct orbits are disjoint. Hence $P^{\sigma^P}=P$. The two assignments are mutually inverse.

> [!note]- Lemma 3: Smooth Gram–Schmidt, and smooth adapted local frames in each case
> **Statement:** (i) *(Smooth Gram–Schmidt.)* Let $E$ carry a smooth Euclidean structure and let $e=(e_1,\dots,e_k)$ be a smooth local frame over $U$. Applying the Gram–Schmidt formulas pointwise to $e$ yields a smooth local frame $e_O=(u_1,\dots,u_k)$ over $U$ that is orthonormal at every point. The same holds for a smooth Hermitian structure, with the real dot product replaced by the Hermitian inner product. (ii) In each of the five settings there is, through every point, a smooth local section of the candidate subbundle $P^\sigma$, and the field reconstructed from a $G$-subbundle is smooth.
>
> **Hint:** The Gram–Schmidt output is built from the smooth entries by $+,-$, division by nowhere-vanishing smooth functions, and $\sqrt{\ }$ of smooth positive functions; the pointwise conclusions are the linear-algebra Gram–Schmidt theorem. The other adapted frames are: rescale one vector (volume), take $(v_1,Iv_1,\dots)$ (complex), use openness (orientation).
>
> **Why needed:** This is the smoothness input that Lemma 2(b) and 2(c) require; without it the correspondence is only set-theoretic.
>
> > [!note]- Full proof
> > **(i) Smooth Gram–Schmidt.** Recall the linear-algebra result, restated at the point of use:
> > [[Thm - Gram-Schmidt Procedure|the Gram–Schmidt procedure]] — *given a linearly independent list $v_1,\dots,v_k$ in an inner-product space, the vectors $f_1=v_1$ and $f_j=v_j-\sum_{i<j}\frac{\langle v_j,f_i\rangle}{\langle f_i,f_i\rangle}f_i$ satisfy $f_j\neq0$, and $u_j=f_j/\sqrt{\langle f_j,f_j\rangle}$ form an orthonormal list with $\operatorname{span}(u_1,\dots,u_j)=\operatorname{span}(v_1,\dots,v_j)$.*
> >
> > Apply this in each fibre $E_m$ to the basis $(e_1(m),\dots,e_k(m))$ (a frame is a pointwise basis, hence linearly independent). Pointwise, the theorem gives $f_j(m)\neq0$ and an orthonormal basis $(u_1(m),\dots,u_k(m))$; so $e_O$ is a frame that is orthonormal at every point. It remains to prove smoothness, by induction on $j$.
> >
> > *Base case.* $f_1=e_1$ is smooth, being one of the given smooth sections. Its pointwise squared norm $\langle f_1,f_1\rangle$ is a smooth function on $U$ (smoothness of the Euclidean structure on smooth sections) and is strictly positive (since $f_1(m)\neq0$), so $m\mapsto\sqrt{\langle f_1,f_1\rangle(m)}$ is smooth (the square root is smooth on $(0,\infty)$) and nowhere zero; hence $u_1=f_1/\sqrt{\langle f_1,f_1\rangle}$ is a smooth section.
> >
> > *Inductive step.* Assume $f_1,\dots,f_{j-1}$ are smooth sections with each $\langle f_i,f_i\rangle$ smooth and strictly positive. Each coefficient $\frac{\langle e_j,f_i\rangle}{\langle f_i,f_i\rangle}$ is then a smooth function on $U$ (quotient of a smooth function by a smooth nowhere-zero function), so
> > $$f_j=e_j-\sum_{i<j}\frac{\langle e_j,f_i\rangle}{\langle f_i,f_i\rangle}\,f_i$$
> > is a smooth section (finite $C^\infty(U)$-linear combination of smooth sections). Its squared norm $\langle f_j,f_j\rangle$ is smooth and, by the pointwise theorem, strictly positive; hence $u_j=f_j/\sqrt{\langle f_j,f_j\rangle}$ is smooth. This completes the induction, so all $u_j$ are smooth and $e_O$ is a smooth orthonormal frame. The Hermitian case is identical: the Hermitian inner product is sesquilinear and positive definite, the coefficients $\langle e_j,f_i\rangle/\langle f_i,f_i\rangle$ are smooth complex-valued functions, the norms $\langle f_j,f_j\rangle$ are smooth positive real functions, and the same induction gives a smooth unitary frame.
> >
> > **(ii) Adapted frames in the five cases.**
> >
> > *Euclidean ($O(k)$) and Hermitian ($U(m)$).* Part (i) provides a smooth orthonormal (respectively unitary) local frame $e_O$; regarded as a section of $\operatorname{Fr}(E)$ it satisfies $e_O(m)^*\langle\cdot,\cdot\rangle_m=g_0$ (respectively $=h_0$), so it is a smooth local section of $P^\sigma$. (The unitary frame also intertwines $I$ and $I_{\mathrm{st}}$, so it lands in the $GL_m(\mathbb C)$-subbundle as well — this is the refinement clause of part 5.)
> >
> > *Volume form ($SL_k(\mathbb R)$).* Let $e=(e_1,\dots,e_k)$ be any smooth local frame over $U$ and $\mu$ the given fibrewise volume form. The function $c(m):=\mu_m(e_1(m),\dots,e_k(m))$ is smooth and nowhere zero (a frame is a basis and $\mu$ is nowhere-vanishing). Set $\tilde e_1:=c^{-1}e_1$ and $\tilde e_j:=e_j$ for $j\ge2$; then $\tilde e$ is a smooth frame and, by multilinearity in the first slot, $\mu(\tilde e_1,\tilde e_2,\dots,\tilde e_k)=c^{-1}\mu(e_1,\dots,e_k)=1$. So $\tilde e^*\mu=\mu_0$, i.e. $\tilde e$ is a smooth local section of $P^\sigma$.
> >
> > *Complex structure ($GL_m(\mathbb C)$).* By [[Def - Complex Vector Bundle and Hermitian Structure|the local structure of a complex vector bundle]] — restated: near any point a complex bundle $(E,I)$ admits smooth sections $v_1,\dots,v_m$ such that $(v_1,Iv_1,\dots,v_m,Iv_m)$ is a frame at every point — form the smooth frame $p$ with columns ordered $p e_{2j-1}=v_j$, $p e_{2j}=Iv_j$. Since $I_{\mathrm{st}}e_{2j-1}=e_{2j}$ and $I_{\mathrm{st}}e_{2j}=-e_{2j-1}$, we get $pI_{\mathrm{st}}e_{2j-1}=pe_{2j}=Iv_j=Ipe_{2j-1}$ and $pI_{\mathrm{st}}e_{2j}=-pe_{2j-1}=-v_j=I(Iv_j)=Ipe_{2j}$; hence $pI_{\mathrm{st}}=Ip$, i.e. $p^*I=I_{\mathrm{st}}$, so $p$ is a smooth local section of $P^\sigma$.
> >
> > *Orientation ($GL_k^+(\mathbb R)$).* Since $GL_k^+(\mathbb R)$ is an open subgroup of $GL_k(\mathbb R)$, the set $\operatorname{Fr}^+(E)=P^\sigma$ of positively oriented frames is an open subset of $\operatorname{Fr}(E)$, hence automatically an embedded submanifold, and by the definition of an orientation there is through each point a local frame positively oriented at every point, i.e. a smooth local section of $\operatorname{Fr}^+(E)$.
> >
> > **Reconstructed structures are smooth.** In each case, a $G$-subbundle $P$ admits smooth local sections $p\colon U\to P$ (a principal bundle is locally trivial, so has local sections; see [[Def - Principal G-Bundle|the definition of a principal bundle]]). The reconstructed structure is $\sigma^P=(p^{-1})^*\sigma_0$, a smooth field: for the Euclidean case $\langle s_1,s_2\rangle(m)=\big(p(m)^{-1}s_1(m)\big)^t\big(p(m)^{-1}s_2(m)\big)$ is smooth in $m$ for smooth sections $s_1,s_2$, since $m\mapsto p(m)^{-1}$ is smooth (inverse of a smooth frame); the volume form $(p^{-1})^*(e^1\wedge\cdots\wedge e^k)$, the endomorphism $pI_{\mathrm{st}}p^{-1}$, the orientation (locally constant), and the Hermitian form are smooth for the same reason.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $E\to M$ be a smooth real vector bundle of rank $k$ with frame bundle $\operatorname{Fr}(E)$. We prove the five bijections; each is an instance of Lemma 2 applied with the model structure and stabiliser computed in Lemma 1 and the smoothness input supplied by Lemma 3. Throughout, "of type $\sigma_0$" is the pointwise-equivalence hypothesis of Lemma 2, and we verify it in each case (it is the assertion that the structure is nonempty in each fibre, i.e. that any structure of the given kind is a pullback of the model).
>
> **Step 0 — the shared framework.** By Lemma 1, pullback of fibre structures by frames is a right action of $GL_k(\mathbb R)$, and the five standard models $g_0,\mu_0,I_{\mathrm{st}},o_0,h_0$ on $\mathbb R^k$ have stabilisers $O(k),SL_k(\mathbb R),GL_m(\mathbb C),GL_k^+(\mathbb R),U(m)$ respectively. Each of these five groups is an embedded Lie subgroup of $GL_k(\mathbb R)$: $O(k)$, $SL_k(\mathbb R)$, $GL_m(\mathbb C)$, and $U(m)$ are closed subgroups of $GL_k(\mathbb R)$ (each is the preimage of a closed set under a continuous map — $A\mapsto A^tA$, $\det$, $[A,I_{\mathrm{st}}]$, $A^*A$ respectively), hence embedded Lie subgroups by [[Thm - The Closed Subgroup Theorem|the closed subgroup theorem]] — *a closed subgroup of a Lie group is an embedded Lie subgroup* — and $GL_k^+(\mathbb R)=\{\det>0\}$ is an open subgroup, hence embedded. Thus Lemma 2 applies to each, once the type hypothesis and the smoothness input are checked.
>
> **Step 1 — Euclidean $\leftrightarrow$ $O(k)$.** The model is $g_0(x,y)=x^ty$, stabiliser $O(k)$ (Lemma 1). *Type hypothesis:* every fibre inner product $\langle\cdot,\cdot\rangle_m$ admits an orthonormal basis (a finite-dimensional inner-product space has one, by [[Thm - Gram-Schmidt Procedure|Gram–Schmidt]]), i.e. a frame $p$ with $\langle px,py\rangle_m=x^ty=g_0(x,y)$, so $p^*\langle\cdot,\cdot\rangle_m=g_0$; the field is of type $g_0$. *Smoothness input:* Lemma 3(i)–(ii) gives smooth orthonormal local frames, i.e. smooth local sections of $P^{\langle\cdot,\cdot\rangle}=O(E)$, and shows the reconstructed inner product is smooth. By Lemma 2 the maps $\langle\cdot,\cdot\rangle\mapsto O(E)$ and $P\mapsto\big(\langle px_1,px_2\rangle:=x_1^tx_2\big)$ are mutually inverse bijections between Euclidean structures and $O(k)$-structures. Unwinding the reconstruction: for $p\in P_m$ and $v_i=px_i$, the value $(p^{-1})^*g_0(v_1,v_2)=g_0(p^{-1}v_1,p^{-1}v_2)=x_1^tx_2$, which is exactly the formula in the Statement.
>
> **Step 2 — Volume form $\leftrightarrow$ $SL_k(\mathbb R)$.** The model is $\mu_0=e^1\wedge\cdots\wedge e^k$, stabiliser $SL_k(\mathbb R)$ (Lemma 1). *Type hypothesis:* a nowhere-vanishing $\mu_m\in\Lambda^kE_m^*$ is a nonzero top form; choosing any basis and rescaling one vector produces a frame $p$ with $\mu_m(pe_1,\dots,pe_k)=1$, so $p^*\mu_m=\mu_0$ and the field is of type $\mu_0$. *Smoothness input:* Lemma 3(ii) (volume case) gives smooth unimodular local frames, i.e. smooth local sections of $P^\mu=\{p:\mu(pe_1,\dots,pe_k)=1\}$, and the reconstructed $\mu^P=(p^{-1})^*(e^1\wedge\cdots\wedge e^k)$ is a smooth nowhere-vanishing section of $\Lambda^kE^*$. Lemma 2 gives the bijection between fibrewise volume forms and $SL_k(\mathbb R)$-structures. (The detailed drill of this case is [[Ex - Fibrewise Volume Forms Correspond to SL(k,R)-Structures|the SL exercise]].)
>
> **Step 3 — Complex structure $\leftrightarrow$ $GL_m(\mathbb C)$ (for $k=2m$).** The model is $I_{\mathrm{st}}$, stabiliser $GL_m(\mathbb C)$ (Lemma 1). *Type hypothesis:* a complex structure $I_m$ on $E_m$ makes $E_m$ a complex vector space of complex dimension $m$; a complex basis gives a real frame $p$ with columns $(v_1,I_mv_1,\dots)$, and the computation in Lemma 3(ii) shows $pI_{\mathrm{st}}=I_mp$, i.e. $p^*I_m=I_{\mathrm{st}}$, so the field is of type $I_{\mathrm{st}}$. *Smoothness input:* Lemma 3(ii) (complex case) gives smooth $I$-adapted local frames as smooth local sections of $P^I=\{p:pI_{\mathrm{st}}=Ip\}$, and $I^P=pI_{\mathrm{st}}p^{-1}$ is a smooth section of $\operatorname{End}E$ with $(I^P)^2=pI_{\mathrm{st}}^2p^{-1}=-\mathbb 1$. Lemma 2 gives the bijection between complex structures and $GL_m(\mathbb C)$-structures. (The two parts of Haydys's Exercise 28 are worked in [[Ex - Complex Structures Correspond to GL(k,C)-Structures|the complex-structures exercise]].)
>
> **Step 4 — Orientation $\leftrightarrow$ $GL_k^+(\mathbb R)$.** The model is $o_0$, stabiliser $GL_k^+(\mathbb R)$ (Lemma 1). *Type hypothesis:* every fibre $E_m$ has exactly two orientations, both pullbacks of $o_0$ under a suitable frame (a positively oriented basis realises $o_0$), so an orientation field is of type $o_0$. *Smoothness input:* Lemma 3(ii) (orientation case) — $\operatorname{Fr}^+(E)$ is open, hence embedded, and positively oriented local frames are smooth local sections; the reconstructed orientation is locally constant, hence smooth. Lemma 2 gives the bijection between orientations and $GL_k^+(\mathbb R)$-structures. (This identifies orientability of $E$ with the existence of a $GL_k^+$-reduction; see [[Ex - Orientations Correspond to GL-plus Reductions|the orientation exercise]].)
>
> **Step 5 — Hermitian $\leftrightarrow$ $U(m)$ (on a complex bundle $(E,I)$).** The model is $h_0(x,y)=\bar x^ty$ on $\mathbb C^m=(\mathbb R^{2m},I_{\mathrm{st}})$, stabiliser $U(m)=O(2m)\cap GL_m(\mathbb C)$ (Lemma 1). *Type hypothesis:* a Hermitian inner product on $(E_m,I_m)$ admits a unitary basis (Hermitian Gram–Schmidt), giving a frame $p$ that is complex-linear ($pI_{\mathrm{st}}=I_mp$) and isometric ($\langle px,py\rangle=\bar x^ty$), so $p^*\langle\cdot,\cdot\rangle_m=h_0$ and the field is of type $h_0$. *Smoothness input:* Lemma 3(i)–(ii) (Hermitian case) gives smooth unitary local frames as smooth local sections of $P^{\langle\cdot,\cdot\rangle}=U(E)$, and the reconstructed Hermitian form is smooth. Lemma 2 gives the bijection between Hermitian structures on $(E,I)$ and $U(m)$-structures. Finally, since $U(m)\subset GL_m(\mathbb C)$, every $p\in U(E)_m$ satisfies $pI_{\mathrm{st}}=Ip$, i.e. $U(E)\subset P^I$: a $U(m)$-reduction refines the $GL_m(\mathbb C)$-reduction determined by $I$, as claimed.
>
> **Step 6 — every bundle has an $O(k)$-reduction.** By [[Thm - Existence of Smooth Partitions of Unity|the existence of smooth partitions of unity]], take a locally finite cover $\{U_\alpha\}$ over which $E$ is trivial, with a subordinate smooth partition of unity $\{\rho_\alpha\}$ ($\rho_\alpha\ge0$, $\operatorname{supp}\rho_\alpha\subset U_\alpha$, $\sum_\alpha\rho_\alpha\equiv1$). On $U_\alpha$ pull back the standard inner product of $\mathbb R^k$ through a trivialisation to get a Euclidean structure $\langle\cdot,\cdot\rangle^\alpha$, and set $\langle\cdot,\cdot\rangle:=\sum_\alpha\rho_\alpha\langle\cdot,\cdot\rangle^\alpha$. This sum is smooth (locally finite sum of smooth fields) and, for $v\neq0$, $\langle v,v\rangle=\sum_\alpha\rho_\alpha(m)\langle v,v\rangle^\alpha>0$, because every summand is nonnegative and at least one $\rho_\alpha(m)>0$ has $\langle v,v\rangle^\alpha>0$; symmetry and bilinearity are inherited termwise, so $\langle\cdot,\cdot\rangle$ is a Euclidean structure. By Step 1 it determines an $O(k)$-structure $O(E)\subset\operatorname{Fr}(E)$. Hence every rank-$k$ real vector bundle reduces from $GL_k(\mathbb R)$ to $O(k)$.
>
> This proves all five bijections and the existence corollary. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Riemannian geometry: the orthonormal coframe and the method of moving frames.** On a Riemannian manifold $(M,g)$, the theorem's part 1 turns $g$ into an $O(n)$-reduction $O(TM)\subset\operatorname{Fr}(TM)$, and Élie Cartan's moving-frame calculus lives entirely on this $O(n)$-bundle: the tautological and connection $1$-forms are forms on $O(TM)$, and the first structure equation expresses torsion-freeness. The theorem applies because the metric is exactly the extra structure whose symmetry group is $O(n)$, and it is non-obvious because Cartan's formalism looks like a choice of local frames, whereas the theorem shows it is intrinsic — the same reduced bundle regardless of the local frames used to compute in it.

**Complex and Kähler geometry: compatible triples.** On a symplectic vector bundle $(E,\omega)$, choosing a compatible metric $g$ produces $I:=$ the bundle map with $\omega(v,w)=g(Iv,w)$, which satisfies $I^2=-\mathbb 1$; parts 3 and 5 then package $(g,I,\omega)$ into a single $U(m)$-reduction. The theorem applies because any two of $\{g,I,\omega\}$ determine the third, and the shared symmetry group is $U(m)$. It is non-obvious because it explains why the space of compatible complex structures is contractible (it is a bundle of copies of the contractible symmetric space $Sp(2m,\mathbb R)/U(m)$), which is the reason almost-complex structures compatible with a symplectic form always exist and are unique up to homotopy — the fact used to define Gromov's pseudoholomorphic-curve invariants.

**Topology: obstruction theory and characteristic classes.** Whether a bundle admits an orientation, a complex structure, or a spin structure is, by the theorem, whether its structure group reduces to $SO(k)$, $GL_m(\mathbb C)$, or $\operatorname{Spin}(k)$. Each reduction is a lifting problem for the classifying map, and the obstruction to the lift is a characteristic class: $w_1$ for orientability, $w_1$ and $w_2$ for spin, an integral class for an almost-complex structure. The theorem applies because it converts "extra structure" into "reduction", the only form in which obstruction theory can see it; it is non-obvious that a differential-geometric question (does a metric or complex structure exist?) becomes a homotopy-lifting question at all.

---

# Bridges

- **From $O(k)$ to $U(1)$ for line bundles.** For a real rank-$2$ bundle $E$ with a Euclidean structure and an orientation, parts 1 and 4 combine to an $SO(2)$-reduction, and $SO(2)\cong U(1)$; part 3 shows the same data is a complex line-bundle structure. This is why the classification of oriented Euclidean rank-$2$ bundles, of $SO(2)$-bundles, of $U(1)$-bundles, and of Hermitian complex line bundles are all one and the same problem — the reduction chain $GL_2(\mathbb R)\to GL_1(\mathbb C)\to U(1)$ identifies them. Haydys records this equivalence (his Remark following the classification, A-R2.4.1) and works throughout in the $U(1)$-language because $U(1)$ is compact and connected, which makes the classification cleanest; the bridge is: given an oriented metric on a rank-$2$ bundle, the rotation-by-ninety-degrees map $I$ (the unique $I$ with $I^2=-\mathbb 1$ compatible with metric and orientation) is the complex structure, and the metric becomes the real part of the Hermitian form.

- **Reduction chains and combined structures.** Because each structure is a reduction, imposing two structures reduces to the intersection of their symmetry groups: a metric and a volume form give $O(k)\cap SL_k(\mathbb R)=SO(k)$ (an oriented metric); a metric and a complex structure give $O(2m)\cap GL_m(\mathbb C)=U(m)$ (a Hermitian structure); a Hermitian metric and a compatible volume form give $U(m)\cap SL_m(\mathbb C)=SU(m)$ (the Calabi–Yau reduction). The construction is: form the two subbundles $P_1,P_2\subset\operatorname{Fr}(E)$ and intersect them, $P_1\cap P_2$, which is a $(G_1\cap G_2)$-subbundle whenever it is nonempty and the intersection group is closed — the combined-structure principle used repeatedly in chapters VI–XI.

- **The frame bundle as the universal home of structure.** Every one of these reductions is a subbundle of the single object $\operatorname{Fr}(E)$, so the frame bundle is the universal carrier from which all geometric structures on $E$ are cut out by choosing a subgroup. The associated-bundle construction (chapter's §3.4) runs the other way — from $\operatorname{Fr}(E)$ and a representation of $GL_k(\mathbb R)$ one rebuilds $E$, $\operatorname{End}E$, $\Lambda^pE^*$, and so on — so that "structure on $E$" and "reduction of $\operatorname{Fr}(E)$" and "representation-theoretic data on $\operatorname{Fr}(E)$" are three faces of one construction.

---

# Unlocked by This

> [!tip] Metric connections and holonomy *(from Gauge Theory IV–V)*
> A connection on the reduced bundle $O(E)$ is exactly a metric connection on $E$, and its holonomy lies in $O(k)$; the Berger classification of Riemannian holonomy groups is the statement of which subgroups of $O(n)$ can occur as holonomy of a reduced Levi–Civita connection. See **Def - Connection on a Principal Bundle**.

> [!tip] Characteristic classes are structure-specific *(from Gauge Theory VI)*
> Because curvature of a connection on a $U(m)$-reduction takes values in $\mathfrak u(m)$, the Chern–Weil construction fed with $\operatorname{Ad}$-invariant polynomials on $\mathfrak u(m)$ produces the Chern classes; fed with $\mathfrak{so}(k)$ it produces the Pontryagin and Euler classes. The reduction is what makes the invariants integral and structure-specific. See **Def - Chern Class via Chern-Weil Theory**.
