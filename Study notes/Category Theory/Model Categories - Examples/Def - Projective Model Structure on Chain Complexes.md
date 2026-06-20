---
type: definition
subject: model-categories
prereqs:
  - "Def - Model Category"
  - "Def - Module"
  - "Def - Chain Map and Chain Homotopy"
  - "Def - Projective Module"
  - "Def - Cofibrant and Fibrant Objects"
tags: [category-theory, homotopy-theory, foundations]
---

# Notation

Throughout, $R$ is a ring (associative with unit $1$, not necessarily commutative) and "module" means left $R$-[[Def - Module|module]]. The category $\mathbf{Ch}(R)$ has objects the **chain complexes** of left $R$-modules — sequences $\cdots \to C_{n+1} \xrightarrow{d_{n+1}} C_n \xrightarrow{d_n} C_{n-1} \to \cdots$ with $d_n d_{n+1} = 0$ — and morphisms the [[Def - Chain Map and Chain Homotopy|chain maps]] $f_\bullet$ commuting with differentials. We write $Z_n(C) = \ker d_n$ for the **$n$-cycles**, $B_n(C) = \operatorname{im} d_{n+1}$ for the **$n$-boundaries**, and $H_n(C) = Z_n(C)/B_n(C)$ for the **$n$-th homology**. A **quasi-isomorphism** is a chain map inducing an isomorphism on every $H_n$, written $\xrightarrow{\sim}$.

Two complexes are built from $R$ and recur constantly. The **sphere complex** $S^n$ is $R$ placed in degree $n$ with zero differential. The **disk complex** $D^n$ is $R$ in degrees $n$ and $n-1$ joined by the identity map, $\cdots \to 0 \to R \xrightarrow{\;1\;} R \to 0 \to \cdots$; it is acyclic, $H_*(D^n) = 0$. There is a canonical inclusion $S^{n-1} \hookrightarrow D^n$ identifying $S^{n-1}$ with the degree-$(n-1)$ part of $D^n$. The full symbol registry is on [[Model Categories — Examples in Detail]].

This page defines a single structure — the projective model structure — but it carries three interlocking classes (weak equivalences, fibrations, cofibrations); each must be given precisely, and the content is the claim that they fit together.

---

# Axiom Motivation

The goal is to do homotopy theory in $\mathbf{Ch}(R)$, and "homotopy theory" here means one specific thing: we want to treat **quasi-isomorphisms as if they were isomorphisms**, because the invariant we care about in a chain complex is its homology, not the complex itself. Two complexes with the same homology, connected by a quasi-isomorphism, should be "the same" for our purposes. The localized category in which every quasi-isomorphism becomes invertible is the derived category $D(R)$, and the projective model structure is the scaffolding that makes $D(R)$ computable. So the weak equivalences are forced on us: they *are* the quasi-isomorphisms. The only freedom is in choosing the cofibrations and fibrations, and the design problem is to choose them so the axioms hold and the cofibrant objects are something we can compute with.

Why take **fibrations to be the degreewise surjections**? The fibrations should be the "good surjections" along which we can lift, and in an algebraic setting the natural surjections are the degreewise epimorphisms. The decisive test is the lifting axiom MC4: a trivial cofibration must lift against every fibration. The cleanest generating trivial cofibrations are the inclusions $0 \hookrightarrow D^n$ of zero into the acyclic disk complex, and a map $p$ has the right lifting property against all of these precisely when it is **degreewise surjective** — because a lift against $0 \hookrightarrow D^n$ is exactly the data of preimages, degree by degree. If we tried to take fibrations to be something stricter, say the surjections with projective kernel, the disk complexes would no longer detect them and the small object argument would not produce the right factorizations. If we tried something weaker, say all chain maps, then trivial fibrations would not be quasi-isomorphisms and the homotopy category would collapse. Degreewise surjectivity is the Goldilocks choice, and it is forced by demanding that the disk complexes generate the trivial cofibrations.

Why take **cofibrations to be the monomorphisms with degreewise-projective cokernel**, rather than, say, all monomorphisms? Here the constraint comes from what we want the *cofibrant objects* to be. A cofibrant object is one for which $0 \to C$ is a cofibration, which with this definition means $C$ has degreewise-[[Def - Projective Module|projective]] cokernel over $0$ — that is, $C$ is degreewise projective. We want this, because the whole point is that cofibrant replacement should be **projective resolution**: resolving a module by projectives is the operation homological algebra already performs to compute derived functors, and a good model structure must reproduce it. If we allowed all monomorphisms to be cofibrations, then cofibrant would mean "any complex", cofibrant replacement would be the identity, and the model structure would fail to encode resolutions — and indeed the lifting axiom would break, because a general monomorphism does not lift against degreewise-surjective quasi-isomorphisms. The projectivity of the cokernel is exactly the condition (via $\mathrm{Hom}(P, -)$ being exact) that supplies the needed lifts. Drop it and MC4 fails; this is the per-axiom failure analysis for the cofibration class.

There is a third design decision hiding in "could a reader invent the generators?". The factorization axiom MC5 is never checked by hand; it is produced by Quillen's small object argument from a set of **generating cofibrations**. The natural candidates are the maps $S^{n-1} \hookrightarrow D^n$ — "attach a disk along its boundary sphere", the algebraic analogue of attaching a cell to a space. A reader who has seen the topological model structure would guess these immediately, and the parallel is not an accident: in both topology and algebra, "attach a cell" is the elementary move from which all factorizations are built. The generating *trivial* cofibrations are the even simpler $0 \hookrightarrow D^n$, "attach an acyclic disk", which add no homology and hence are quasi-isomorphisms. With these two sets, the small object argument supplies both factorizations, and the rest of the structure is determined.

---

# The Definition

The **projective model structure** on $\mathbf{Ch}(R)$ is the [[Def - Model Category|model structure]] with the following three classes of chain maps.

> **Weak equivalences** are the **quasi-isomorphisms**: chain maps $f$ with $H_n(f)$ an isomorphism for every $n$.
>
> **Fibrations** are the chain maps that are **surjective in every degree**: $f_n : C_n \to D_n$ is onto for all $n$.
>
> **Cofibrations** are the chain maps that are **monomorphisms with degreewise-[[Def - Projective Module|projective]] cokernel**: $f_n$ is injective for all $n$ and each $\operatorname{coker}(f_n)$ is a projective $R$-module.

A **trivial fibration** is a fibration that is also a quasi-isomorphism; concretely these are the surjective chain maps whose kernel is an acyclic complex of projectives. A **trivial cofibration** is a cofibration that is also a quasi-isomorphism.

This model structure is **cofibrantly generated**: the generating cofibrations are the set $I = \{S^{n-1} \hookrightarrow D^n : n \in \mathbb{Z}\}$, and the generating trivial cofibrations are $J = \{0 \hookrightarrow D^n : n \in \mathbb{Z}\}$. The fibrations are exactly the maps with the right lifting property against $J$, and the trivial fibrations are exactly the maps with the right lifting property against $I$.

Two consequences fix the (co)fibrant objects. **Every object is fibrant**, because the map $C \to 0$ to the zero complex is surjective in every degree (the zero map onto the zero module). **The cofibrant objects are the bounded-below complexes of projectives** — a complex $C$ is cofibrant precisely when $0 \to C$ is a cofibration, i.e. each $C_n$ is projective and $C$ is bounded below. Cofibrant replacement of a module $M$ (regarded as a complex concentrated in degree $0$) is exactly a projective resolution $P_\bullet \xrightarrow{\sim} M$.

> **Remark (an unbounded subtlety).** For *unbounded* complexes the cofibrant objects are not merely the degreewise-projective ones; one needs additionally that the complex is "K-projective" (also called "DG-projective" or "semi-projective"), meaning $\mathrm{Hom}(C, -)$ preserves quasi-isomorphisms. For bounded-below complexes the two notions coincide, which is why the resolution picture is exact in the bounded-below case. We work with bounded-below complexes unless noted.

---

# Categorical / Structural Definition

The model structure is determined functorially by its generating sets through the **lifting calculus** of [[Def - Model Category|model categories]]. For a set of maps $I$ in any cocomplete category, write $I\text{-inj}$ for the maps with the right lifting property against every map in $I$, and $I\text{-cof}$ for the maps with the left lifting property against every map in $I\text{-inj}$. The projective model structure is then defined entirely by:

$$\text{cofibrations} = I\text{-cof}, \qquad \text{trivial fibrations} = I\text{-inj}, \qquad \text{fibrations} = J\text{-inj}, \qquad \text{trivial cofibrations} = J\text{-cof},$$

with $I = \{S^{n-1} \hookrightarrow D^n\}$ and $J = \{0 \hookrightarrow D^n\}$, the weak equivalences being the quasi-isomorphisms. That these abstract lifting-defined classes coincide with the concrete descriptions above (degreewise epi, mono-with-projective-cokernel) is the content of the recognition theorem for cofibrantly generated model categories, and is proved in [[Thm - Chain Complexes of Modules Form a Model Category]].

The reason the sphere and disk complexes work as generators is a pair of representability statements: $\mathbf{Ch}(R)(S^n, C) \cong Z_n(C)$, the $n$-cycles, and $\mathbf{Ch}(R)(D^n, C) \cong C_n$, the degree-$n$ chains. The sphere complex *represents the cycle functor* and the disk complex *represents the chains functor*. A lifting problem against $S^{n-1} \hookrightarrow D^n$ therefore translates, by these isomorphisms, into a purely module-theoretic surjectivity question, which is what makes the generators tractable. This representability is the structural heart of the construction: $S^n$ and $D^n$ are the corepresenting objects for cycles and chains, exactly as the disks $D^n$ corepresent the underlying-set-at-level-$n$ functor in topology.

---

# Relate to Other Fields / Compression

This structure is the homotopy-theoretic repackaging of classical homological algebra. The operation "resolve a module by projectives", which homological algebra performs to define [[Def - Tensor Product of Modules|Tor]] and Ext, is exactly cofibrant replacement here; the chain homotopies of homological algebra are exactly the abstract [[Def - Cylinder Object, Path Object, and Homotopy|homotopies]] of the model structure; and the derived category, defined by formally inverting quasi-isomorphisms, is exactly the [[Thm - The Homotopy Category of a Model Category|homotopy category]] $\mathrm{Ho}(\mathbf{Ch}(R)) = D(R)$. Homological algebra is the special case of model-category theory living in chain complexes.

The structure is also, almost verbatim, the chain-complex translation of the [[Def - The Quillen Model Structure on Topological Spaces|Quillen model structure on spaces]]: replace "space" by "complex", "weak homotopy equivalence" by "quasi-isomorphism", "Serre fibration" by "degreewise surjection", "cell $S^{n-1} \hookrightarrow D^n$" by "disk complex inclusion $S^{n-1} \hookrightarrow D^n$". The generators even carry the same names. This is the precise sense in which "chain complexes are spaces over a ring" — the Dold–Kan correspondence makes this an equivalence in the non-negatively-graded case.

**True name:** the operational characterisation is *"cofibrant means projective resolution, fibrant means nothing, weak equivalence means quasi-isomorphism"*. When using the structure you almost never invoke the formal definitions of the classes; you reach for the slogan "to compute a derived functor, resolve by projectives and apply it", which is this true name in action.

---

# Examples / Corollaries

**Is an instance — a projective resolution as cofibrant replacement.** Take $R = \mathbb{Z}$ and $M = \mathbb{Z}/n$. The two-term complex $P_\bullet = (\,\mathbb{Z} \xrightarrow{\,n\,} \mathbb{Z}\,)$ in degrees $1$ and $0$ is degreewise projective (free, even) and hence cofibrant, and the projection $P_\bullet \to \mathbb{Z}/n$ (onto the cokernel, with $\mathbb{Z}/n$ in degree $0$) is a quasi-isomorphism: $H_0 = \mathbb{Z}/n$, $H_1 = \ker(n) = 0$. So $P_\bullet$ is a cofibrant replacement of $\mathbb{Z}/n$, and it is literally the standard projective resolution.

**Is an instance — the disk complex is trivially cofibrant.** Each $D^n$ is a complex of free (hence projective) modules, so $0 \to D^n$ is a cofibration; and $D^n$ is acyclic, so $0 \to D^n$ is a quasi-isomorphism. Thus $0 \hookrightarrow D^n$ is a *trivial* cofibration, which is exactly why these complexes generate the trivial cofibrations.

**Is an instance — every complex is fibrant.** For any $C$, the map $C \to 0$ is the zero map in each degree, which is surjective onto the zero module, so it is a fibration. Hence $C$ is fibrant. There is no fibrant-replacement step in this model structure.

**Is NOT an instance — a non-projective module is not cofibrant as a degree-zero complex.** The module $\mathbb{Z}/n$, regarded as a complex concentrated in degree $0$, is *not* cofibrant over $\mathbb{Z}$: its cokernel over $0$ is $\mathbb{Z}/n$ itself, which is not a [[Def - Projective Module|projective]] $\mathbb{Z}$-module (it is torsion, and projective $\mathbb{Z}$-modules are free, hence torsion-free). This is precisely why $\mathbb{Z}/n$ must be *replaced* by its resolution before tensoring — and the failure of cofibrancy is the source of $\mathrm{Tor}_1(\mathbb{Z}/n, -)$.

**Is NOT an instance — a quasi-isomorphism that is not a fibration.** The quasi-isomorphism $(\mathbb{Z}\xrightarrow{n}\mathbb{Z}) \xrightarrow{\sim} \mathbb{Z}/n$ is *not* surjective in degree $1$ (the target is zero in degree $1$, fine) — but consider instead the inclusion $\mathbb{Z}/n \hookrightarrow$ its injective hull; many quasi-isomorphisms fail to be degreewise surjective, showing that "weak equivalence" and "fibration" are genuinely independent classes. A trivial fibration is the special map that is *both*.

**Calibration check.** Verify that (i) $\mathbf{Ch}(R)(D^n, C) \cong C_n$ by checking a chain map out of $D^n$ is determined by where it sends the degree-$n$ generator; (ii) a chain map is a trivial fibration if and only if it is surjective and has acyclic kernel; and (iii) the cofibrant replacement of $R$ itself (in degree zero) can be taken to be $R$ in degree zero, since $R$ is already projective. If you can do these three, you have understood the structure.

---

# Unlocked by This

> [!tip] The Derived Category $D(R)$ and Triangulated Structure *(from Homological Algebra)*
> Inverting the quasi-isomorphisms produces the **derived category** $D(R)$, the universal recipient of $\mathbf{Ch}(R)$ sending quasi-isomorphisms to isomorphisms. The model structure makes this computable: maps in $D(R)$ are [[Def - Chain Map and Chain Homotopy|chain-homotopy]] classes of maps between projective resolutions. The cofiber sequences supply **distinguished triangles**, making $D(R)$ a **triangulated category**, and the shift functor is the degree shift of complexes.

> [!tip] Tor and Ext as Derived Functors *(from Homological Algebra)*
> The total left derived functor of $-\otimes_R N$ computes **Tor**: $\mathrm{Tor}^R_n(M,N) = H_n(P_\bullet \otimes_R N)$ for a projective resolution $P_\bullet \to M$. Dually the right derived functor of $\mathrm{Hom}_R$ computes **Ext**. The model structure is the justification that these are well-defined and independent of the resolution chosen.

> [!tip] Derived Categories of Sheaves *(from Algebraic Geometry)*
> Replacing $R$-modules by sheaves of $\mathcal{O}_X$-modules on a scheme and using the injective model structure produces the **derived category of coherent sheaves** $D(\mathrm{Coh}\,X)$, the setting for Serre duality, Fourier–Mukai transforms, and homological mirror symmetry. The single-ring structure here is the affine local model of that global construction.
