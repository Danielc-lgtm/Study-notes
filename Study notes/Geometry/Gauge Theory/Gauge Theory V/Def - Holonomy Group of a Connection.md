---
type: definition
subject: gauge-theory
prereqs:
  - "Thm - Properties of Parallel Transport"
  - "Def - Parallel Transport in a Principal Bundle"
  - "Def - Connection on a Principal Bundle"
  - "Def - Curvature of a Principal Connection"
tags: [geometry, gauge-theory]
---

# Notation

This is a compound page: it defines four interlocking notions — the **holonomy element** $\operatorname{hol}_p(c)\in G$ of a based loop, the **holonomy group** $\operatorname{Hol}_p(\omega)\subseteq G$ of a principal connection, the **holonomy group** $\operatorname{Hol}_m(\nabla)\subseteq GL(E_m)$ of a vector-bundle connection, and the **restricted holonomy group** $\operatorname{Hol}^0_p(\omega)$ of null-homotopic loops — because they are the same measurement (how much parallel transport around a loop fails to return a point to itself) read on the principal bundle, on an associated bundle, and after discarding the topology of the base.

We use throughout the standing conventions of the series. **Lie groups act on principal bundles on the right**, $R_g(p)=p\cdot g$; the action of $G$ on a fibre is free and transitive, so each fibre $P_m$ is a right $G$-torsor. $\Gamma(E)$ denotes smooth sections. A **curve** is a piecewise smooth map from a compact interval, and its velocity exists off the finitely many corners.

Throughout, $\pi\colon P\to M$ is a smooth [[Def - Connection on a Principal Bundle|principal $G$-bundle]] over a connected smooth manifold $M$, with $G$ a Lie group with identity $e$ and Lie algebra $\mathfrak g=T_eG$, and $\omega\in\Omega^1(P;\mathfrak g)$ is a fixed [[Def - Connection on a Principal Bundle|connection]]. Its horizontal subspace at $p\in P$ is $H_p:=\ker\omega_p\subset T_pP$, a $G$-invariant complement of the vertical space, so that $dR_g(H_p)=H_{p\cdot g}$ for all $p,g$. For $m\in M$ the fibre is $P_m:=\pi^{-1}(m)$.

A **loop based at $m$** is a curve $c\colon[t_0,t_1]\to M$ with $c(t_0)=c(t_1)=m$. Its reversal is written $\bar c$: if $\phi\colon[t_0,t_1]\to[t_0,t_1]$ is the orientation-reversing reparametrisation $\phi(t)=t_0+t_1-t$, then $\bar c:=c\circ\phi$, which runs $c$ backwards. For a loop $c_1$ at $m$ and a loop $c_2$ at $m$, the **concatenation** $c_2*c_1$ is the loop that traces $c_1$ first and then $c_2$ (our concatenation convention is right-to-left, matching composition of maps); more generally, for composable curves $c_1\colon[t_0,t_1]\to M$ and $c_2\colon[t_1,t_2]\to M$ with $c_1(t_1)=c_2(t_1)$, the concatenation $c_2*c_1\colon[t_0,t_2]\to M$ equals $c_1$ on $[t_0,t_1]$ and $c_2$ on $[t_1,t_2]$.

The [[Def - Parallel Transport in a Principal Bundle|parallel transport along $c$]] determined by $\omega$ is the map
$$\Gamma_c\colon P_{c(t_0)}\longrightarrow P_{c(t_1)},\qquad \Gamma_c(p):=\tilde c(t_1),$$
where $\tilde c$ is the unique horizontal lift of $c$ with $\tilde c(t_0)=p$. Given a [[Def - Representation of a Lie Group|representation]] $\rho\colon G\to GL(V)$ on a finite-dimensional real or complex vector space $V$, the [[Def - Associated Bundle|associated vector bundle]] is $E=P\times_\rho V$, with classes $[p,v]$ satisfying $[p\cdot g,\rho(g)^{-1}v]=[p,v]$, and the induced connection is $\nabla=\nabla^\omega$; the induced parallel transport on $E$ is
$$PT_c\colon E_{c(t_0)}\longrightarrow E_{c(t_1)},\qquad PT_c\big([p,v]\big):=[\Gamma_c(p),v].$$
We write $k=\dim_{\mathbb R}E_m$ for the real rank of $E$; a complex bundle of complex rank $m$ has $k=2m$. For each $p\in P_m$ the map $\iota_p\colon V\to E_m$, $v\mapsto[p,v]$, is a linear isomorphism. We write $\operatorname{GL}(E_m)$ for the group of linear automorphisms of the fibre $E_m$.

We import, at the point of use, the following structural identities of parallel transport, proved in full on their own page and restated here so that every clause below can be checked without leaving the page.

> [!note] Restatement — properties of parallel transport
> **[[Thm - Properties of Parallel Transport|Theorem]].** For piecewise smooth curves and a connection $\omega$ on $\pi\colon P\to M$: **(1)** if $c$ is constant then $\Gamma_c=\operatorname{id}$; **(3)** for the reversal, $\Gamma_{\bar c}=\Gamma_c^{-1}$, so $\Gamma_c$ is a diffeomorphism $P_{c(t_0)}\to P_{c(t_1)}$; **(4)** for composable curves $\Gamma_{c_2*c_1}=\Gamma_{c_2}\circ\Gamma_{c_1}$; **(5)** for every $g\in G$, $\Gamma_c(p\cdot g)=\Gamma_c(p)\cdot g$; **(6)** in an associated bundle $E=P\times_\rho V$, $PT_c$ is a linear isomorphism, is a linear isometry when $\rho$ preserves an inner product on $V$ (equivalently when $\nabla$ is a metric or Hermitian connection), and is complex-linear when $V$ is complex and $\rho$ is complex-linear.

> [!warning] Convention: the two sources, and the base point
> Haydys (his Definition 101, p. 33) defines the holonomy group directly on a vector bundle as $\operatorname{Hol}_m(\nabla)=\{PT_\gamma\in GL(E_m):\gamma\text{ a loop based at }m\}$, then chooses a basis of $E_m$ to view it inside $GL_k(\mathbb R)$ and, having proved that different base points in one connected component give conjugate groups, **drops the base point** and speaks of $\operatorname{Hol}(\nabla)\subseteq GL_k(\mathbb R)$ up to conjugacy. Bär does not name the holonomy group at all; his Remark 2.6.6 (our source item B-R2.6.1) records only that $\Gamma_c$ is independent of the parametrisation of $c$ but for a closed curve $\Gamma_c\ne\operatorname{id}$ in general, "related to curvature, as we shall see soon". This page keeps the base point explicit while a choice is being made and drops it only after the conjugacy corollary is proved. Where Haydys writes $\operatorname{Hol}(\nabla)\subseteq U(k/2)$ for a complex Hermitian bundle, his $k$ is the **real** rank, so $U(k/2)=U(m)$ with $m$ the complex rank; we write $U(m)$.

---

# Axiom Motivation

Parallel transport around a loop is the one thing a connection produces that a connection on a *contractible* base could never distinguish from nothing. On the interval, or on any region small enough to trivialise the bundle flatly, transporting a fibre out along a path and back along the same path returns every point to itself; the interesting content of a connection is entirely in what happens when the outbound and return paths differ, and the sharpest instance of that is a loop, where they differ maximally — the return path is empty. So the object we want to define is the discrepancy: after transporting the fibre $P_m$ around a loop $c$ based at $m$, by how much has it been rotated relative to where it started? We now build the definition that measures this, and we watch each design choice earn its place by seeing what breaks without it.

The first choice is to record the discrepancy as an **element of the structure group**, not as an abstract self-map of the fibre. Parallel transport around a loop is a map $\Gamma_c\colon P_m\to P_m$, and a priori this is just a diffeomorphism of the fibre. But the fibre is not merely a manifold: it is a right $G$-torsor, on which $G$ acts freely and transitively, and $\Gamma_c$ is $G$-equivariant (property (5)). A single equivariant self-map of a torsor is right multiplication by a *unique* group element: fixing any $p\in P_m$, the point $\Gamma_c(p)$ lies in the same fibre $P_m$, so by transitivity there is $g\in G$ with $\Gamma_c(p)=p\cdot g$, and by freeness this $g$ is unique. That unique $g$ is the holonomy $\operatorname{hol}_p(c)$. The reason we insist on this — rather than leaving the holonomy as the diffeomorphism $\Gamma_c$ — is that it turns a geometric operation into an arithmetic one inside $G$: composition of transports becomes multiplication in $G$, and the whole apparatus of the structure group (its representations, its invariant inner products, its Lie subgroups) becomes available to constrain and classify what holonomies can occur. If we **dropped the requirement that $G$ act transitively on the fibre**, there would be no group element to extract, and the construction would return nothing but the self-map; if we **dropped freeness**, the element would fail to be unique and $\operatorname{hol}_p(c)$ would not be well defined. Both are automatic for a principal bundle and are exactly what a principal bundle is for.

The second choice is to take the holonomy over **all** loops at $m$ and collect the results into a set $\operatorname{Hol}_p(\omega)=\{\operatorname{hol}_p(c):c\text{ a loop at }m\}$, and then to observe that this set is a **subgroup** of $G$. This is not an extra axiom imposed on the definition; it is forced by the structure of parallel transport. Concatenation of loops corresponds to composition of transports (property (4)), so a product of two holonomies is again a holonomy — of the concatenated loop; the constant loop transports trivially (property (1)), so the identity $e$ is a holonomy; and the reversed loop inverts the transport (property (3)), so the inverse of a holonomy is a holonomy — of the reversed loop. What would go wrong if we **restricted to a single loop, or to a set of loops not closed under concatenation and reversal**? We would get a subset of $G$ with no algebraic structure, and none of the theorems that make holonomy useful — that a metric connection has holonomy in $O(k)$, that a flat connection's holonomy is a representation of $\pi_1$, that the holonomy detects the curvature infinitesimally — could even be stated, because each of them is a statement about a *group*. The subgroup property is the definition's whole reason to range over all loops.

The third choice concerns the two things the holonomy depends on that we would like it *not* to: the point $p\in P_m$ in the fibre (equivalently, on a vector bundle, the basis of $E_m$) and the base point $m$ itself. Changing $p$ to $p\cdot g$ conjugates every holonomy by $g$ (proved below), and moving the base point along a path $\gamma$ conjugates the whole group by the transport $\Gamma_\gamma$ (also below). Neither of these is a defect to be removed by adding hypotheses; it is an honest feature of the object, and the correct response is to **remember the holonomy group only up to conjugacy** once these choices have been made. Here the per-choice failure analysis cuts the other way: if we tried to **strengthen the definition to a single canonical subgroup of $G$ independent of all choices**, no such object exists — the conjugacy is genuine, as the change-of-point formula $\operatorname{hol}_{p\cdot g}(c)=g^{-1}\operatorname{hol}_p(c)g$ shows explicitly — and pretending otherwise would make the "definition" depend on an arbitrary trivialisation. The honest object is the conjugacy class, and the theory is organised so that everything of interest (compactness of $\operatorname{Hol}$, its Lie-algebra, whether it is all of $G$ or a proper subgroup) is conjugation-invariant.

The last choice is to isolate, alongside the full holonomy group, the **restricted holonomy group** $\operatorname{Hol}^0_p(\omega)$ obtained by ranging only over loops that are null-homotopic. The reason to name this smaller group is that it separates the two sources of holonomy. Holonomy around a *small contractible* loop is generated by the curvature — it is a local, differential-geometric effect that survives on the universal cover; holonomy around a loop that *wraps around a hole* in $M$ is a global, topological effect that a simply connected base could never produce. The restricted group captures the first kind and the quotient $\operatorname{Hol}_p/\operatorname{Hol}^0_p$ captures the second (it is a homomorphic image of $\pi_1(M,m)$). If we **failed to make this distinction**, the flat case would be unintelligible: a flat connection has trivial curvature and hence, on the universal cover, trivial holonomy, yet its holonomy group downstairs can be any subgroup of $G$ that arises as the image of a representation of $\pi_1$. The restricted holonomy is exactly the algebraic device that says "the curvature contributes here, the topology contributes there", and it is the object [[Def - Flat Connection|flatness]] annihilates.

A reader who has followed the four choices could reconstruct the definition unaided: extract the group element that equivariance forces, range over all loops so that the properties of transport make the result a group, remember it up to conjugacy because the point and base point genuinely move it, and split off the null-homotopic part to separate curvature from topology.

---

# The Definition

Fix the connection $\omega$ on $\pi\colon P\to M$, a base point $m\in M$, and a point $p\in P_m$ in its fibre.

## The holonomy element of a loop

> **Definition (holonomy of a loop, principal form).** Let $c$ be a piecewise smooth loop based at $m$. Because $c(t_0)=c(t_1)=m$, the parallel transport $\Gamma_c$ is a $G$-equivariant map $P_m\to P_m$ of the fibre to itself. The **holonomy of $c$ at $p$** is the unique group element $\operatorname{hol}_p(c)\in G$ with
> $$\Gamma_c(p)=p\cdot\operatorname{hol}_p(c).$$

This is well defined. The point $\Gamma_c(p)$ lies in $P_m$ (it is the endpoint of a lift of a loop, hence in the fibre over $c(t_1)=m$), and $G$ acts **transitively** on $P_m$, so some $g\in G$ satisfies $\Gamma_c(p)=p\cdot g$; the action is also **free**, so $g$ is unique. We call it $\operatorname{hol}_p(c)$. No smoothness or continuity in $c$ is asserted or needed: the definition is pointwise in the loop.

## The holonomy group of a principal connection

> **Definition (holonomy group, principal form).** The **holonomy group of $\omega$ based at $p$** is the set of holonomies of all loops at $m$,
> $$\operatorname{Hol}_p(\omega):=\{\operatorname{hol}_p(c)\in G\ :\ c\text{ a piecewise smooth loop based at }m\}.$$

That this set is a subgroup of $G$ is the first corollary proved below. When we wish to emphasise the base point of the loops rather than the point of the fibre we also write $\operatorname{Hol}_m(\omega)$ for the conjugacy class of $\operatorname{Hol}_p(\omega)$ as $p$ ranges over $P_m$; the change-of-point corollary shows this is a single conjugacy class in $G$.

## The holonomy group of a vector-bundle connection

For an associated bundle $E=P\times_\rho V$ — or, equivalently, for any [[Def - Connection on a Vector Bundle|connection $\nabla$ on a vector bundle]] $E\to M$, whose frame bundle carries the principal connection inducing it — we read the same construction on the fibre $E_m$.

> **Definition (holonomy group, vector-bundle form).** The **holonomy group of $\nabla$ based at $m$** is the set of induced parallel transports around loops,
> $$\operatorname{Hol}_m(\nabla):=\{PT_c\in GL(E_m)\ :\ c\text{ a piecewise smooth loop based at }m\}\subseteq GL(E_m).$$
> After a choice of basis of $E_m$, this is a subgroup of $GL_k(\mathbb R)$ (real case) or $GL_m(\mathbb C)$ (complex case), determined up to conjugacy.

The two forms carry the same information. Fixing $p\in P_m$ gives the linear isomorphism $\iota_p\colon V\to E_m$, $v\mapsto[p,v]$, and under it the vector-bundle holonomy is the representation of the principal holonomy: for a loop $c$,
$$PT_c\big(\iota_p(v)\big)=PT_c\big([p,v]\big)=[\Gamma_c(p),v]=[p\cdot\operatorname{hol}_p(c),v]=[p,\rho(\operatorname{hol}_p(c))v]=\iota_p\big(\rho(\operatorname{hol}_p(c))v\big),$$
each step by, in turn, the definition of $\iota_p$, the definition of $PT_c$, the definition of $\operatorname{hol}_p(c)$, the associated-bundle relation $[p\cdot g,v]=[p,\rho(g)^{-1}v]$ read as $[p\cdot g,v]=[p,\rho(g)v]$ after renaming, and the definition of $\iota_p$ again. Hence
$$\iota_p^{-1}\circ PT_c\circ\iota_p=\rho\big(\operatorname{hol}_p(c)\big),$$
so $\operatorname{Hol}_m(\nabla)=\iota_p\circ\rho(\operatorname{Hol}_p(\omega))\circ\iota_p^{-1}$: the vector-bundle holonomy group is the image of the principal holonomy group under the representation, read through the frame $\iota_p$.

## The restricted holonomy group

> **Definition (restricted holonomy group).** The **restricted holonomy group of $\omega$ based at $p$** is the holonomy of the null-homotopic loops,
> $$\operatorname{Hol}^0_p(\omega):=\{\operatorname{hol}_p(c)\in G\ :\ c\text{ a piecewise smooth loop based at }m\text{ that is null-homotopic}\},$$
> and similarly $\operatorname{Hol}^0_m(\nabla)\subseteq\operatorname{Hol}_m(\nabla)$ on a vector bundle. Here "null-homotopic" means homotopic, relative to the base point $m$, to the constant loop at $m$ (see [[Def - Homotopy of Paths|homotopy of paths]]).

We record it now for use in later chapters, where the [[Def - Flat Connection|flatness]] of $\omega$ is exactly the vanishing of $\operatorname{Hol}^0$ and the quotient $\operatorname{Hol}_p/\operatorname{Hol}^0_p$ becomes a quotient of $\pi_1(M,m)$. Its subgroup and normality properties are the last corollary below.

---

# Categorical / Structural Definition

The holonomy group has a clean description that dispenses with the choice of loop and exhibits it as a path-component. Consider the equivalence relation on $P$ generated by "$p\sim q$ if $q=\tilde c(t_1)$ for a horizontal lift $\tilde c$ of some curve $c$ with $\tilde c(t_0)=p$" — that is, $p\sim q$ when $p$ and $q$ are joined by a horizontal curve in $P$. The equivalence classes are the leaves of the horizontal path structure. Restricting attention to the leaf $P(p)$ through a fixed $p\in P_m$, the structural characterisation of holonomy is:

> $$\operatorname{Hol}_p(\omega)=\{\,g\in G\ :\ p\cdot g\in P(p)\,\}=\{\,g\in G\ :\ p\text{ and }p\cdot g\text{ are joined by a horizontal curve projecting to a loop at }m\,\}.$$

Indeed, $g\in\operatorname{Hol}_p(\omega)$ means $g=\operatorname{hol}_p(c)$ for a loop $c$, that is, $\Gamma_c(p)=p\cdot g$, which says exactly that the horizontal lift of the loop $c$ through $p$ ends at $p\cdot g$ — a horizontal curve from $p$ to $p\cdot g$ over a loop. Conversely any horizontal curve from $p$ to $p\cdot g$ projects to a loop $c$ at $m$ (its projection starts and ends at $\pi(p)=\pi(p\cdot g)=m$) and realises $g=\operatorname{hol}_p(c)$. This is the **true name** of the holonomy group: it is the isotropy subgroup of the point $p$ under the "same horizontal leaf" relation, the set of group elements you can reach from $p$ by travelling horizontally around loops.

From this reading the reduction theory follows structurally, and we state its shape without proving it here (its proof belongs to the Ambrose–Singer circle in a later development): the leaf $P(p)$, together with the subgroup $\operatorname{Hol}_p(\omega)$, is a **reduction of the structure group** of $P$ from $G$ to $\operatorname{Hol}_p(\omega)$ whenever the latter is a Lie subgroup, called the **holonomy bundle**, and $\omega$ restricts to a connection on it. The functorial content is that holonomy is the obstruction to reducing the bundle-with-connection to the trivial group: $\operatorname{Hol}_p(\omega)=\{e\}$ if and only if the horizontal leaf through $p$ is a global horizontal section over $M$, that is, if and only if $\omega$ is (globally) trivialised by a flat parallel frame. The based-loop viewpoint and the leaf viewpoint are the two faces of the same object; the based-loop one computes, the leaf one classifies.

---

# Relate to Other Fields / Compression

**True name.** Operationally, $\operatorname{Hol}_p(\omega)$ is *the group generated by the transport-around-loops operators*, and the compression that makes it computable is the pair of homomorphism-type identities proved below: $\operatorname{hol}_p(c_2*c_1)=\operatorname{hol}_p(c_2)\operatorname{hol}_p(c_1)$ and $\operatorname{hol}_p(\bar c)=\operatorname{hol}_p(c)^{-1}$. These say that $\operatorname{hol}_p$ is a monoid homomorphism from the loops-under-concatenation into $G$ (with our right-to-left concatenation, so that concatenation matches composition), and the holonomy group is simply its image. Everything else — conjugacy under change of point, the containment in $O(k)$ or $U(m)$, the reduction to a representation of $\pi_1$ in the flat case — is a property of this one homomorphism.

**Riemannian geometry.** For the Levi-Civita connection on $TM$ of a Riemannian manifold, $\operatorname{Hol}_m(\nabla)\subseteq O(n)$ (it is metric, so property (6) applies), and for an orientable manifold $\operatorname{Hol}_m(\nabla)\subseteq SO(n)$. The Berger classification of Riemannian holonomy groups — the short list $SO(n)$, $U(n/2)$, $SU(n/2)$, $Sp$, $G_2$, $\operatorname{Spin}(7)$ of groups that can occur as the holonomy of an irreducible, non-symmetric Riemannian metric — is the deepest structural theorem about the object defined here; each smaller-than-$SO(n)$ holonomy group forces a parallel tensor (a complex structure, a Kähler form, a special spinor) and hence extra geometry. The [[Ex - Holonomy around a Spherical Cap is the Solid Angle|holonomy of the round sphere]] around a geodesic cap equals the enclosed solid angle, the model computation of the whole subject.

**Physics.** In gauge theory the holonomy $\operatorname{hol}_p(c)$ of the connection (the gauge potential) around a loop is the **Wilson loop** variable; its trace $\operatorname{tr}\rho(\operatorname{hol}_p(c))$ is the gauge-invariant observable, and the fact that a non-trivial holonomy can persist around a loop even where the curvature vanishes on the loop itself is the mathematics of the Aharonov–Bohm effect. The infinitesimal version — holonomy around a small loop is $\operatorname{id}$ minus the flux of the curvature (proved in the sibling theorem [[Thm - Curvature is the Infinitesimal Holonomy|curvature is the infinitesimal holonomy]]) — is why the field strength $F_{\mu\nu}$ is "infinitesimal holonomy" in the physics reading.

**Covering-space theory.** For a covering $\tilde M\to M$ viewed as a principal bundle with discrete structure group and its unique flat connection, $\operatorname{hol}_p$ is the monodromy: it assigns to a loop the deck transformation it induces, and $\operatorname{Hol}_p$ is the image of the monodromy homomorphism $\pi_1(M,m)\to\operatorname{Deck}$. Holonomy of a general flat connection is the smooth generalisation of this, made precise in [[Thm - Flat Connections and Monodromy Representations of the Fundamental Group|the correspondence between flat connections and representations of $\pi_1$]].

---

# Examples / Corollaries

We prove the four corollaries the definition promised, then verify three examples and one non-instance clause by clause, closing with calibration checks.

## Corollary 1 — the holonomy set is a subgroup

> **Corollary.** $\operatorname{Hol}_p(\omega)$ is a subgroup of $G$, and $\operatorname{Hol}_m(\nabla)$ is a subgroup of $GL(E_m)$. Moreover, for loops $c_1,c_2$ at $m$,
> $$\operatorname{hol}_p(c_2*c_1)=\operatorname{hol}_p(c_2)\,\operatorname{hol}_p(c_1),\qquad \operatorname{hol}_p(\bar c)=\operatorname{hol}_p(c)^{-1},\qquad \operatorname{hol}_p(\text{const}_m)=e.$$

*Proof.* **What we assume and must show.** We assume the properties of parallel transport (1), (3), (4), (5) restated in the Notation section, and must show the three displayed identities and deduce the subgroup property.

**Closure under products (from concatenation and equivariance).** Let $c_1,c_2$ be loops at $m$. By the definition of holonomy, $\Gamma_{c_1}(p)=p\cdot\operatorname{hol}_p(c_1)$. Then
$$\Gamma_{c_2*c_1}(p)=\Gamma_{c_2}\big(\Gamma_{c_1}(p)\big)=\Gamma_{c_2}\big(p\cdot\operatorname{hol}_p(c_1)\big)\qquad\text{(property (4), then the definition of }\operatorname{hol}_p(c_1)\text{)}$$
$$=\Gamma_{c_2}(p)\cdot\operatorname{hol}_p(c_1)=\big(p\cdot\operatorname{hol}_p(c_2)\big)\cdot\operatorname{hol}_p(c_1)\qquad\text{(property (5) with }g=\operatorname{hol}_p(c_1)\text{, then the definition of }\operatorname{hol}_p(c_2)\text{)}$$
$$=p\cdot\big(\operatorname{hol}_p(c_2)\,\operatorname{hol}_p(c_1)\big)\qquad\text{(associativity of the right action).}$$
On the other hand $\Gamma_{c_2*c_1}(p)=p\cdot\operatorname{hol}_p(c_2*c_1)$ by definition. Since $G$ acts **freely** on $P_m$, the two expressions $p\cdot(\operatorname{hol}_p(c_2)\operatorname{hol}_p(c_1))$ and $p\cdot\operatorname{hol}_p(c_2*c_1)$ force $\operatorname{hol}_p(c_2*c_1)=\operatorname{hol}_p(c_2)\operatorname{hol}_p(c_1)$. In particular the product of two elements of $\operatorname{Hol}_p(\omega)$ is again in $\operatorname{Hol}_p(\omega)$, realised by the concatenated loop.

**The identity (from the constant loop).** Let $\text{const}_m$ be the constant loop at $m$. By property (1), $\Gamma_{\text{const}_m}=\operatorname{id}_{P_m}$, so $\Gamma_{\text{const}_m}(p)=p=p\cdot e$; by freeness $\operatorname{hol}_p(\text{const}_m)=e$. Hence $e\in\operatorname{Hol}_p(\omega)$.

**Closure under inverses (from reversal).** Let $c$ be a loop at $m$ with reversal $\bar c$. By property (3), $\Gamma_{\bar c}=\Gamma_c^{-1}$. We compute $\Gamma_c^{-1}(p)$: starting from $\Gamma_c(p)=p\cdot\operatorname{hol}_p(c)$ and applying the equivariant map $\Gamma_c^{-1}$ (its equivariance is property (5) for $\bar c$, since $\Gamma_c^{-1}=\Gamma_{\bar c}$),
$$p=\Gamma_c^{-1}\big(p\cdot\operatorname{hol}_p(c)\big)=\Gamma_c^{-1}(p)\cdot\operatorname{hol}_p(c)\qquad\text{(applying }\Gamma_c^{-1}\text{ to both sides; equivariance of }\Gamma_c^{-1}\text{)},$$
so $\Gamma_c^{-1}(p)=p\cdot\operatorname{hol}_p(c)^{-1}$ (multiply on the right by $\operatorname{hol}_p(c)^{-1}$). But also $\Gamma_{\bar c}(p)=p\cdot\operatorname{hol}_p(\bar c)$ by definition, and $\Gamma_{\bar c}=\Gamma_c^{-1}$, so $p\cdot\operatorname{hol}_p(\bar c)=p\cdot\operatorname{hol}_p(c)^{-1}$; by freeness $\operatorname{hol}_p(\bar c)=\operatorname{hol}_p(c)^{-1}$. Hence the inverse of every element of $\operatorname{Hol}_p(\omega)$ lies in $\operatorname{Hol}_p(\omega)$, realised by the reversed loop.

**Conclusion.** $\operatorname{Hol}_p(\omega)$ contains $e$ and is closed under products and inverses, so it is a subgroup of $G$. The vector-bundle statement is identical with $PT_c$ in place of $\Gamma_c$: property (4) gives $PT_{c_2*c_1}=PT_{c_2}\circ PT_{c_1}$, property (1) gives $PT_{\text{const}_m}=\operatorname{id}_{E_m}$, and property (3) gives $PT_{\bar c}=PT_c^{-1}$, so $\operatorname{Hol}_m(\nabla)$ is a subgroup of $GL(E_m)$. $\blacksquare$

## Corollary 2 — change of point in the fibre conjugates the group

> **Corollary.** For $p\in P_m$ and $g\in G$, and any loop $c$ at $m$,
> $$\operatorname{hol}_{p\cdot g}(c)=g^{-1}\,\operatorname{hol}_p(c)\,g,\qquad\text{hence}\qquad \operatorname{Hol}_{p\cdot g}(\omega)=g^{-1}\,\operatorname{Hol}_p(\omega)\,g.$$
> The holonomy group at a fixed base point is therefore determined by the connection up to conjugacy in $G$.

*Proof.* **What we assume and must show.** We must compute $\operatorname{hol}_{p\cdot g}(c)$, the group element with $\Gamma_c(p\cdot g)=(p\cdot g)\cdot\operatorname{hol}_{p\cdot g}(c)$, in terms of $\operatorname{hol}_p(c)$.

**Transport commutes with the group action.** By property (5) and the definition of $\operatorname{hol}_p(c)$,
$$\Gamma_c(p\cdot g)=\Gamma_c(p)\cdot g=\big(p\cdot\operatorname{hol}_p(c)\big)\cdot g=p\cdot\big(\operatorname{hol}_p(c)\,g\big)\qquad\text{(property (5); definition of }\operatorname{hol}_p(c)\text{; associativity).}$$
**Rewrite the base point.** We want the right-hand side in the form $(p\cdot g)\cdot(\cdots)$. Since $p=(p\cdot g)\cdot g^{-1}$,
$$p\cdot\big(\operatorname{hol}_p(c)\,g\big)=(p\cdot g)\cdot\big(g^{-1}\operatorname{hol}_p(c)\,g\big)\qquad\text{(insert }g^{-1}g=e\text{ and reassociate).}$$
**Read off the holonomy at $p\cdot g$.** Comparing with the defining equation $\Gamma_c(p\cdot g)=(p\cdot g)\cdot\operatorname{hol}_{p\cdot g}(c)$ and using freeness, $\operatorname{hol}_{p\cdot g}(c)=g^{-1}\operatorname{hol}_p(c)\,g$. Letting $c$ range over all loops, $\operatorname{Hol}_{p\cdot g}(\omega)=g^{-1}\operatorname{Hol}_p(\omega)\,g$.

**Conclusion.** As $p$ ranges over the single fibre $P_m$ (transitively, so every choice is $p\cdot g$ for some $g$), the holonomy groups $\operatorname{Hol}_p(\omega)$ form one conjugacy class in $G$. Fixing a frame $\iota_p$ of $E_m$, the same computation gives $\operatorname{Hol}_m(\nabla)$ up to conjugacy in $GL(E_m)$; changing the frame conjugates by the change-of-basis matrix. This is why, after a basis is chosen, one drops the base point in the notation and speaks of $\operatorname{Hol}(\nabla)$ as a subgroup defined up to conjugacy. $\blacksquare$

## Corollary 3 — change of base point conjugates by parallel transport

> **Corollary.** Let $\gamma$ be a piecewise smooth path from $m$ to $m'$ in $M$ (such a path exists because $M$ is connected). Then
> $$\operatorname{Hol}_{m'}(\nabla)=PT_\gamma\circ\operatorname{Hol}_m(\nabla)\circ PT_\gamma^{-1}\subseteq GL(E_{m'}),$$
> and on the principal bundle $\operatorname{Hol}_{\Gamma_\gamma(p)}(\omega)=\operatorname{Hol}_p(\omega)$ (equal, not merely conjugate). Consequently, since $M$ is connected, the conjugacy class of the holonomy group in $GL_k(\mathbb R)$ (respectively in $G$) is independent of the base point. This is the "standard argument" of Haydys's Remark following Definition 101, written in full.

*Proof.* **What we assume and must show.** Fix the path $\gamma$ from $m$ to $m'$; its reversal $\bar\gamma$ runs from $m'$ to $m$, and by property (3), $PT_{\bar\gamma}=PT_\gamma^{-1}$. We show each generator $PT_{c'}$ of $\operatorname{Hol}_{m'}(\nabla)$ is $PT_\gamma$ times a generator of $\operatorname{Hol}_m(\nabla)$ times $PT_\gamma^{-1}$, and conversely.

**Every loop at $m$ conjugates to a loop at $m'$.** Let $c$ be a loop at $m$. Then $\gamma*c*\bar\gamma$ is a loop based at $m'$: it runs $\bar\gamma$ from $m'$ to $m$, then the loop $c$ at $m$, then $\gamma$ back to $m'$ (each junction matches: $\bar\gamma$ ends at $m$, $c$ starts and ends at $m$, $\gamma$ starts at $m$). By property (4) applied twice,
$$PT_{\gamma*c*\bar\gamma}=PT_\gamma\circ PT_c\circ PT_{\bar\gamma}=PT_\gamma\circ PT_c\circ PT_\gamma^{-1}\qquad\text{(concatenation, then }PT_{\bar\gamma}=PT_\gamma^{-1}\text{).}$$
Thus $PT_\gamma\circ PT_c\circ PT_\gamma^{-1}\in\operatorname{Hol}_{m'}(\nabla)$ for every loop $c$ at $m$, giving $PT_\gamma\circ\operatorname{Hol}_m(\nabla)\circ PT_\gamma^{-1}\subseteq\operatorname{Hol}_{m'}(\nabla)$.

**Every loop at $m'$ arises this way.** Conversely let $c'$ be a loop at $m'$ and set $c:=\bar\gamma*c'*\gamma$, a loop at $m$ (it runs $\gamma$ from $m$ to $m'$, then $c'$, then $\bar\gamma$ back to $m$). Then
$$PT_\gamma\circ PT_c\circ PT_\gamma^{-1}=PT_\gamma\circ\big(PT_{\bar\gamma}\circ PT_{c'}\circ PT_\gamma\big)\circ PT_\gamma^{-1}=\big(PT_\gamma\circ PT_{\bar\gamma}\big)\circ PT_{c'}\circ\big(PT_\gamma\circ PT_\gamma^{-1}\big)=PT_{c'},$$
using property (4) for $PT_c=PT_{\bar\gamma}\circ PT_{c'}\circ PT_\gamma$, then $PT_\gamma\circ PT_{\bar\gamma}=PT_\gamma\circ PT_\gamma^{-1}=\operatorname{id}$ (property (3)). Hence every $PT_{c'}\in\operatorname{Hol}_{m'}(\nabla)$ equals $PT_\gamma\circ PT_c\circ PT_\gamma^{-1}$ for the loop $c$ at $m$, giving the reverse inclusion $\operatorname{Hol}_{m'}(\nabla)\subseteq PT_\gamma\circ\operatorname{Hol}_m(\nabla)\circ PT_\gamma^{-1}$.

**Conclusion.** The two inclusions give $\operatorname{Hol}_{m'}(\nabla)=PT_\gamma\circ\operatorname{Hol}_m(\nabla)\circ PT_\gamma^{-1}$, an isomorphism of groups implemented by conjugation by the invertible operator $PT_\gamma$. On the principal bundle the same argument with $\Gamma$ in place of $PT$ and $p':=\Gamma_\gamma(p)$ gives $\operatorname{hol}_{p'}(\gamma*c*\bar\gamma)=\operatorname{hol}_p(c)$ directly (the conjugating group elements cancel because $\Gamma_\gamma(p)=p'$ absorbs the transport), so $\operatorname{Hol}_{p'}(\omega)=\operatorname{Hol}_p(\omega)$ as subgroups of $G$. Since any two points of the connected manifold $M$ are joined by a piecewise smooth path, all the holonomy groups lie in one conjugacy class, and the base point may be dropped. $\blacksquare$

## Corollary 4 — holonomy of a metric, Hermitian, or complex connection

> **Corollary (Haydys, Exercise 102).** Let $E\to M$ be a vector bundle with connection $\nabla$. Then:
> 1. if $\nabla$ is a **metric (Euclidean)** connection, then in any orthonormal basis of $E_m$ every $PT_c$ is orthogonal, so $\operatorname{Hol}_m(\nabla)\subseteq O(k)$;
> 2. if $E$ is complex and $\nabla$ is **complex-linear**, then every $PT_c$ is complex-linear, so $\operatorname{Hol}_m(\nabla)\subseteq GL_m(\mathbb C)$ (with $k=2m$);
> 3. if $E$ is complex with a Hermitian metric and $\nabla$ is a **Hermitian** connection, then every $PT_c$ is unitary, so $\operatorname{Hol}_m(\nabla)\subseteq U(m)$.

*Proof.* **What we assume and must show.** We use property (6) of parallel transport, restated in the Notation section, and the elementary fact that a subgroup generated by elements lying in a subgroup $H\le GL(E_m)$ is itself contained in $H$.

**Each generator lies in the relevant subgroup.** By property (6): if $\nabla$ is metric — equivalently the inducing representation $\rho$ preserves a real inner product on the fibre — then each $PT_c$ is a linear isometry of $(E_m,\langle\cdot,\cdot\rangle)$, hence, in an orthonormal basis, a matrix $O$ with $O^{\mathsf T}O=I$, that is, $O\in O(k)$. If $\nabla$ is complex-linear then each $PT_c$ commutes with the complex structure $I$ of $E_m$ (property (6), complex case), hence is a $\mathbb C$-linear automorphism, an element of $GL_m(\mathbb C)$. If $\nabla$ is Hermitian then $\rho$ preserves the Hermitian inner product, so each $PT_c$ is both complex-linear and an isometry of the Hermitian form, hence unitary, an element of $U(m)$.

**Pass from generators to the group.** In each case the set $\{PT_c\}$ generates $\operatorname{Hol}_m(\nabla)$ (Corollary 1), and lies in the subgroup $H\in\{O(k),GL_m(\mathbb C),U(m)\}$ of $GL(E_m)$. A subgroup is closed under products and inverses; since $H$ is a subgroup containing every generator $PT_c$, it contains every product and inverse of generators, hence the whole subgroup they generate. Therefore $\operatorname{Hol}_m(\nabla)\subseteq H$ in each case.

**Conclusion.** The holonomy of a metric connection lies in the orthogonal group, of a complex connection in the complex general linear group, and of a Hermitian connection in the unitary group. The three clauses of Haydys's Exercise 102 are exactly these three containments; the deeper statement that each is realised (that the holonomy fills the subgroup) is the content of the reduction theory and of the Berger classification, not asserted here. $\blacksquare$

## Corollary 5 — the restricted holonomy group is a normal subgroup

> **Corollary.** $\operatorname{Hol}^0_p(\omega)$ is a normal subgroup of $\operatorname{Hol}_p(\omega)$.

*Proof.* **What we assume and must show.** We show $\operatorname{Hol}^0_p(\omega)$ is a subgroup and that it is invariant under conjugation by every element of $\operatorname{Hol}_p(\omega)$; we use the composition law of Corollary 1 and the elementary homotopy facts that the concatenation of null-homotopic loops is null-homotopic, the reversal of a null-homotopic loop is null-homotopic, the constant loop is null-homotopic, and $c*c_0*\bar c$ is null-homotopic whenever $c_0$ is (proved in [[Thm - The Fundamental Group is a Group|the fundamental group is a group]], where $[c*c_0*\bar c]=[c][c_0][c]^{-1}=[c]\,e\,[c]^{-1}=e$ in $\pi_1(M,m)$).

**Subgroup.** If $c_0,c_1$ are null-homotopic loops at $m$, then $c_1*c_0$ is null-homotopic (product of null-homotopic classes), so $\operatorname{hol}_p(c_1*c_0)=\operatorname{hol}_p(c_1)\operatorname{hol}_p(c_0)\in\operatorname{Hol}^0_p(\omega)$; the reversal $\bar c_0$ is null-homotopic, so $\operatorname{hol}_p(c_0)^{-1}=\operatorname{hol}_p(\bar c_0)\in\operatorname{Hol}^0_p(\omega)$; and $\operatorname{hol}_p(\text{const}_m)=e\in\operatorname{Hol}^0_p(\omega)$. Hence $\operatorname{Hol}^0_p(\omega)$ is a subgroup of $\operatorname{Hol}_p(\omega)$.

**Normality.** Let $h=\operatorname{hol}_p(c)\in\operatorname{Hol}_p(\omega)$ for a loop $c$ at $m$, and let $h_0=\operatorname{hol}_p(c_0)\in\operatorname{Hol}^0_p(\omega)$ for a null-homotopic loop $c_0$. By Corollary 1 applied to the concatenation $c*c_0*\bar c$,
$$\operatorname{hol}_p(c*c_0*\bar c)=\operatorname{hol}_p(c)\,\operatorname{hol}_p(c_0)\,\operatorname{hol}_p(\bar c)=h\,h_0\,h^{-1}\qquad\text{(composition law twice; }\operatorname{hol}_p(\bar c)=h^{-1}\text{).}$$
The loop $c*c_0*\bar c$ is null-homotopic (since $c_0$ is), so $h h_0 h^{-1}=\operatorname{hol}_p(c*c_0*\bar c)\in\operatorname{Hol}^0_p(\omega)$. As $h$ ranges over $\operatorname{Hol}_p(\omega)$ and $h_0$ over $\operatorname{Hol}^0_p(\omega)$, this says $\operatorname{Hol}_p(\omega)\cdot\operatorname{Hol}^0_p(\omega)\cdot\operatorname{Hol}_p(\omega)^{-1}\subseteq\operatorname{Hol}^0_p(\omega)$: the restricted group is normal.

**Conclusion.** $\operatorname{Hol}^0_p(\omega)\trianglelefteq\operatorname{Hol}_p(\omega)$, and the quotient $\operatorname{Hol}_p(\omega)/\operatorname{Hol}^0_p(\omega)$ is a well-defined group, realised as a homomorphic image of $\pi_1(M,m)$ via $[c]\mapsto\operatorname{hol}_p(c)\operatorname{Hol}^0_p(\omega)$; this is the algebraic separation of the curvature-generated holonomy (inside $\operatorname{Hol}^0$) from the topology-generated holonomy (in the quotient). $\blacksquare$

## Example 1 — the product connection has trivial holonomy

Let $P=M\times G$ with the **product connection**, whose horizontal subspace at $(m,g)$ is $H_{(m,g)}=T_mM\times\{0\}$ (the connection form is $\omega=\theta$, the pullback of the [[Def - The Maurer-Cartan Form|Maurer–Cartan form]] under the projection to $G$, and its kernel is the tangent to the $M$-factor). We verify $\operatorname{Hol}=\{e\}$.

For any curve $c\colon[t_0,t_1]\to M$ and any $g\in G$, the curve $\tilde c(t):=(c(t),g)$ (constant in the $G$-factor) satisfies $\pi\circ\tilde c=c$ and has velocity $\dot{\tilde c}(t)=(\dot c(t),0)\in T_{c(t)}M\times\{0\}=H_{\tilde c(t)}$, so it is horizontal; by uniqueness of horizontal lifts it is *the* horizontal lift of $c$ through $(m,g)$. If $c$ is a loop at $m$ then $\Gamma_c(m,g)=\tilde c(t_1)=(c(t_1),g)=(m,g)$, so $\Gamma_c=\operatorname{id}$ and $\operatorname{hol}_{(m,g)}(c)=e$. Ranging over all loops, $\operatorname{Hol}_{(m,g)}(\omega)=\{e\}$. This is the calibration that trivial holonomy means the connection is (globally) a product; the horizontal leaves are the global sections $m\mapsto(m,g)$.

## Example 2 — the constant connection on the trivial line bundle over the circle

Let $L=S^1\times\mathbb C\to S^1$ be the trivial Hermitian line bundle, with $S^1$ coordinatised by $\theta\in\mathbb R/2\pi\mathbb Z$, structure group $U(1)$, and the connection $\nabla=d+ia\,d\theta$ with $a\in\mathbb R$ a fixed real constant (connection form $A=ia\,d\theta\in\Omega^1(S^1;i\mathbb R)$, so $A$ takes values in $\mathfrak u(1)=i\mathbb R$ and $\nabla$ is Hermitian). We compute $\operatorname{Hol}=\{e^{-2\pi ika}:k\in\mathbb Z\}$.

A section is a function $s\colon\text{(interval)}\to\mathbb C$, and it is parallel along the curve $\theta(t)=t$ (once around, $t\in[0,2\pi]$) precisely when the parallel-transport ordinary differential equation holds:
$$\nabla_{\dot\theta}s=\dot s+ia\,s=0\qquad\text{(the local form }\nabla=d+A\text{ along the curve, with }A(\dot\theta)=ia\text{).}$$
This linear equation has the unique solution $s(\theta)=s(0)e^{-ia\theta}$ (verify: $\dot s=-ia\,s(0)e^{-ia\theta}=-ia\,s$, so $\dot s+ia\,s=0$, and $s(0)$ is the given initial value). Transport once around the circle, from $\theta=0$ to $\theta=2\pi$, multiplies the fibre value by
$$PT_c=e^{-ia\cdot 2\pi}=e^{-2\pi ia}\in U(1).$$
Traversing the generating loop $k$ times (for $k\ge0$; negative $k$ traverses the reversal, giving the inverse, consistent with Corollary 1) transports by $e^{-2\pi ika}$. Since every loop in $S^1$ is homotopic — hence, for this **flat** connection, equal in holonomy (by [[Thm - Holonomy of a Flat Connection Depends Only on the Homotopy Class of the Loop|homotopy invariance of flat holonomy]], applicable because $F=dA=d(ia\,d\theta)=0$) — to a $k$-fold cover of the generator, the holonomy group is exactly
$$\operatorname{Hol}(\nabla)=\{e^{-2\pi ika}:k\in\mathbb Z\}\subseteq U(1).$$
Clause by clause: it lies in $U(1)$ (Hermitian connection, Corollary 4(3), with $m=1$); it is the cyclic subgroup generated by $e^{-2\pi ia}$; it is finite of order $q$ when $a=p/q\in\mathbb Q$ in lowest terms, and infinite otherwise. This exhibits the whole range of one-dimensional holonomy and is the germ of Dirac's charge-quantisation argument (a globally defined connection on a nontrivial line bundle would force $a$ into a lattice).

## Example 3 — the Hopf connection has holonomy the full circle

Let $\pi\colon S^3\to S^2$ be the [[Def - The Hopf Bundle|Hopf bundle]], a principal $U(1)$-bundle, with its [[Thm - The Standard Connection on the Hopf Bundle|standard connection]], whose curvature is a nonzero constant multiple of the area form of the round $S^2$: $F=-\tfrac12\,\mathrm{vol}_{S^2}$ in the normalisation used in the sibling exercises, so $F$ is nowhere zero. We show $\operatorname{Hol}=U(1)$.

For a latitude circle $c_h$ on $S^2$ at height $h\in(-1,1)$, bounding the spherical cap $S_h$ above it, the connection is abelian ($U(1)$), so [[Thm - Holonomy of an Abelian Connection is the Exponential of the Curvature Integral|the holonomy of an abelian connection is the exponential of the curvature integral]] applies: the holonomy of $c_h$ is
$$\operatorname{hol}(c_h)=\exp\!\Big(-\int_{S_h}F\Big)=\exp\big(i\,\Omega(h)\big),$$
where $\Omega(h)=\tfrac12\operatorname{Area}(S_h)$ is (up to the fixed normalisation) the enclosed solid angle, computed explicitly in [[Ex - Holonomy of the Hopf Connection around a Latitude Circle|the Hopf latitude exercise]]. As $h$ decreases from $1$ to $-1$, the cap area $\operatorname{Area}(S_h)$ increases continuously from $0$ to the full sphere area $4\pi$, so $\Omega(h)$ sweeps continuously through an interval of length exceeding $2\pi$. Therefore the set $\{\exp(i\Omega(h)):h\in(-1,1)\}$ is a connected arc in $U(1)$ that wraps entirely around the circle, hence equals all of $U(1)$. Since these holonomies already exhaust $U(1)$, and $\operatorname{Hol}$ is a subgroup of $U(1)$ containing them (Corollary 1, Corollary 4(3)),
$$\operatorname{Hol}(\nabla_{\text{Hopf}})=U(1).$$
This is the standard witness that a connection on a nontrivial bundle can have holonomy the whole structure group, and it verifies property (7) — path dependence — concretely: different latitude circles, with different endpoints traced out, give different holonomies.

## Scope remark — the holonomy group need not be closed

The definition does not force $\operatorname{Hol}_p(\omega)$ to be a **closed** (equivalently, embedded) subgroup of $G$, and this is not a defect to be repaired. Take $G=U(1)\times U(1)$, the trivial bundle $S^1\times G\to S^1$, and the connection $A=i(\alpha,\beta)\,d\theta$ with $\alpha,\beta\in\mathbb R$ and $\alpha/\beta$ irrational. By the computation of Example 2 in each factor, the holonomy of the $k$-fold generator is $(e^{-2\pi ik\alpha},e^{-2\pi ik\beta})$, so
$$\operatorname{Hol}(\nabla)=\big\{(e^{-2\pi ik\alpha},e^{-2\pi ik\beta}):k\in\mathbb Z\big\}\subseteq U(1)\times U(1),$$
a **countable** subgroup of the uncountable torus, hence a proper subgroup. It is a standard fact — **Kronecker's density theorem**, not proved and not used in this series — that for $\alpha/\beta$ irrational this subgroup is dense in $U(1)\times U(1)$; a dense proper subgroup is not closed. We record only what we have verified (the group is this explicit countable set) and note that whether $\operatorname{Hol}$ is closed is not decided by the definition. It is a separate theorem, of **Borel and Lipschitz** — again not proved and not used in this series — that the *restricted* holonomy group $\operatorname{Hol}^0_p(\omega)$ is a connected Lie subgroup of $G$; the full group differs from it by the discrete data of $\pi_1$, which is where non-closedness can enter.

**Calibration check.** Three quick verifications from the material above. First, the holonomy of a reversed loop is the inverse of the holonomy of the loop: this is the reversal identity $\operatorname{hol}_p(\bar c)=\operatorname{hol}_p(c)^{-1}$ of Corollary 1, proved from property (3). Second, the holonomy is unchanged under orientation-preserving reparametrisation of the loop: parallel transport itself is (property (2) of the transport theorem, recorded in Bär's Remark 2.6.6 that $\Gamma_c$ is independent of the parametrisation), and holonomy is read off $\Gamma_c$, so it inherits the invariance. Third, the trivial holonomy $\operatorname{Hol}=\{e\}$ of Example 1 says exactly that the product connection admits a global parallel frame, which matches the structural characterisation that $\operatorname{Hol}_p(\omega)=\{e\}$ if and only if the horizontal leaf through $p$ is a global section — the two statements are the same fact read on $P$ and on $M\times G$.

---

# Unlocked by This

> [!tip] The monodromy representation of a flat connection *(from §5.4)*
> When $\omega$ is [[Def - Flat Connection|flat]], the restricted holonomy $\operatorname{Hol}^0$ is trivial and the map $[c]\mapsto\operatorname{hol}_p(c)$ descends to a homomorphism $\pi_1(M,m)\to G$, the **monodromy representation**; this is the door to [[Thm - Flat Connections and Monodromy Representations of the Fundamental Group|the correspondence between flat connections and representations of the fundamental group]].

> [!tip] Curvature is the infinitesimal holonomy *(from §5.2)*
> The holonomy around a small loop equals the identity minus the flux of the curvature through the loop, to leading order; this is [[Thm - Curvature is the Infinitesimal Holonomy|the infinitesimal-holonomy theorem]], which turns the holonomy group defined here into the integrated form of the curvature and underlies the physical reading of the field strength.

> [!tip] Reduction of the structure group and the Ambrose–Singer theorem *(from later development)*
> When $\operatorname{Hol}_p(\omega)$ is a Lie subgroup, the horizontal leaf through $p$ reduces the structure group of $P$ to it, and the **Ambrose–Singer theorem** identifies the Lie algebra of the restricted holonomy group with the span of the curvature values transported around; these are the structural theorems that classify which groups can occur as holonomy.
