---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Gauge Transformation"
  - "Def - Adjoint Bundles ad P and Ad P"
  - "Thm - Sections of an Associated Bundle are Equivariant Functions"
  - "Def - Gauge Group of a Vector Bundle"
  - "Def - Principal G-Bundle"
  - "Def - Associated Bundle"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $G$ is a [[Def - Lie Group|Lie group]] with [[Def - The Lie Algebra of a Lie Group|Lie algebra]] $\mathfrak{g} = T_e G$, and $\pi : P \to M$ is a smooth [[Def - Principal G-Bundle|principal G-bundle]] over a smooth manifold $M$. The group $G$ acts on $P$ **on the right**; we write $R_g(p) = p \cdot g$ for $p \in P$, $g \in G$, and this action is free and transitive on each fibre $P_m = \pi^{-1}(m)$. We write $e \in G$ for the identity element.

Following the standing convention of the series, a [[Def - Gauge Transformation|gauge transformation]] of $P$ is a diffeomorphism $f : P \to P$ that is $G$-equivariant, $f(p \cdot g) = f(p) \cdot g$ for all $p \in P$ and $g \in G$, and that covers the identity of the base, $\pi \circ f = \pi$. The set of all gauge transformations, with composition as its product, is the **gauge group**
$$\mathcal{G}(P) = \{\, f \in \operatorname{Diff}(P) : \pi \circ f = \pi,\ f(p\cdot g) = f(p)\cdot g \ \ \forall p \in P,\, g \in G \,\}.$$
It is the kernel of the base-map homomorphism $\operatorname{Aut}(P) \to \operatorname{Diff}(M)$, $f \mapsto \bar f$; equivalently, it is the group of automorphisms of $P$ in the category of principal $G$-bundles over the fixed base $M$.

The **adjoint group bundle** is the fibre bundle
$$\operatorname{Ad}P := P \times_\alpha G,$$
where $\alpha$ is the action of $G$ on itself by conjugation, $\alpha_g(\gamma) = g\gamma g^{-1}$; concretely $\operatorname{Ad}P = (P \times G)/\!\sim$ with $(p,\gamma) \sim (p\cdot h,\, h^{-1}\gamma h)$ for $h \in G$, and $[p,\gamma]$ denotes the equivalence class of $(p,\gamma)$. As established on [[Def - Adjoint Bundles ad P and Ad P]], each fibre $(\operatorname{Ad}P)_m$ is a group under $[p,\gamma]\cdot[p,\gamma'] = [p,\gamma\gamma']$ (well defined because the conjugation relation respects products), isomorphic to $G$, with unit $[p,e]$; the map $\varpi : \operatorname{Ad}P \to M$ is the bundle projection, and $\Gamma(\operatorname{Ad}P)$ denotes the set of its smooth sections. Because the fibres are groups, $\Gamma(\operatorname{Ad}P)$ is itself a group under **pointwise multiplication**, $(s_1 s_2)(m) = s_1(m)\cdot s_2(m)$, with unit the section $m \mapsto [p,e]$ (any $p \in P_m$) and inverse $(s^{-1})(m) = s(m)^{-1}$.

For a smooth vector bundle $E \to M$ of rank $k$, the [[Def - Gauge Group of a Vector Bundle|gauge group of E]] is
$$\mathcal{G}(E) = \{\, g \in \Gamma(\operatorname{End}E) : g(m) \in GL(E_m)\ \forall m \in M \,\},$$
the group of smooth bundle automorphisms of $E$ covering the identity, under composition; equivalently $\mathcal{G}(E) = \Gamma(\operatorname{Aut}E)$, where $\operatorname{Aut}E \subset \operatorname{End}E$ is the subbundle whose fibre over $m$ is the group $GL(E_m)$ of linear automorphisms of $E_m$. The [[Def - Frame Bundle of a Vector Bundle|frame bundle]] $\operatorname{Fr}(E)$ is the principal $GL_k(\mathbb{R})$-bundle whose fibre over $m$ is the set of ordered bases of $E_m$, each such basis identified with a linear isomorphism $e : \mathbb{R}^k \to E_m$, with the right action $e \cdot a = e \circ a$ for $a \in GL_k(\mathbb{R})$.

A representation is a homomorphism $\rho : G \to GL(V)$ of Lie groups on a finite-dimensional vector space $V$; its differential at the identity is the Lie-algebra homomorphism $\rho_* := d_e\rho : \mathfrak{g} \to \operatorname{End}V = \mathfrak{gl}(V)$. The associated vector bundle is $E = P \times_\rho V := (P \times V)/\!\sim$ with $(p,v) \sim (p\cdot g,\, \rho(g^{-1})v)$, and $[p,v]$ is the class of $(p,v)$. The **adjoint bundle** $\operatorname{ad}P := P \times_{\operatorname{Ad}} \mathfrak{g}$ is the vector bundle associated to the [[Def - Adjoint Representation|adjoint representation]] $\operatorname{Ad} : G \to GL(\mathfrak{g})$; its sections form the Lie algebra of $\mathcal{G}(P)$.

> [!warning] Convention: source discrepancies
> Haydys writes the adjoint group bundle as $P \times_G G$ and, in his equation (58), prints the equivariance condition on $\hat f$ as "$\hat f(pg) = g^{-1}pg$"; this is a typographical error — the letter $p$ should be $\hat f(p)$, and the correct condition, derived in Lemma 1 below, is $\hat f(pg) = g^{-1}\hat f(p)\,g$. Bär writes $P \times_\alpha G$ (our notation) and states the correspondence as an isomorphism $\{C^\infty\text{-sections of } P\times_\alpha G\} \cong \mathcal{G}(P)$ of groups. Bär's $\mathcal{C}(P)$ for the space of connection forms is our $\mathcal{A}(P)$. The two sources agree once the typo is corrected.

---

# Statement

> **Theorem (the gauge group as sections of the adjoint group bundle).** Let $\pi : P \to M$ be a smooth principal $G$-bundle.
>
> **(a) The fundamental identification.** The assignment $f \mapsto \hat f$, where $\hat f : P \to G$ is the unique map with
> $$f(p) = p \cdot \hat f(p) \qquad (p \in P),$$
> is a bijection from the gauge group $\mathcal{G}(P)$ onto the set
> $$C^\infty(P;G)^{\mathrm{conj}} := \{\, \hat f \in C^\infty(P;G) : \hat f(p\cdot g) = g^{-1}\,\hat f(p)\,g \ \ \forall p \in P,\, g \in G \,\}$$
> of smooth $G$-valued functions on $P$ that are equivariant for the conjugation action. Composing this with the bijection $C^\infty(P;G)^{\mathrm{conj}} \cong \Gamma(\operatorname{Ad}P)$, $\hat f \mapsto \big(m \mapsto [p,\hat f(p)]\big)$ — the fibre-bundle counterpart, for the conjugation action, of [[Thm - Sections of an Associated Bundle are Equivariant Functions|the equivariant-function description of sections of an associated bundle]] — yields a bijection
> $$\Phi : \mathcal{G}(P) \longrightarrow \Gamma(\operatorname{Ad}P).$$
> This bijection is an **isomorphism of groups**: it carries composition of gauge transformations to pointwise multiplication of sections,
> $$\Phi(f_1 \circ f_2) = \Phi(f_1)\cdot \Phi(f_2),$$
> the identity gauge transformation to the unit section $m \mapsto [p,e]$, and the inverse gauge transformation to the pointwise inverse section. Hence $\mathcal{G}(P) \cong \Gamma(\operatorname{Ad}P)$.
>
> **(b) The abelian and central case.** If $G$ is abelian, then every smooth map $g : M \to G$ defines a gauge transformation by $f(p) = p \cdot g(\pi(p))$, all gauge transformations arise this way, and the correspondence is an isomorphism of groups
> $$\mathcal{G}(P) \cong C^\infty(M;G).$$
> If $G$ is non-abelian, the recipe $f(p) = p\cdot g(\pi(p))$ produces a gauge transformation **exactly** for those $g : M \to G$ whose values lie in the [[Def - Centraliser and Centre|centre]] $Z(G) = \{z \in G : zg = gz\ \forall g\in G\}$; such gauge transformations form the subgroup $C^\infty(M; Z(G)) \le \mathcal{G}(P)$.
>
> **(c) Frame bundles and induced homomorphisms.** For a rank-$k$ vector bundle $E \to M$ with frame bundle $\operatorname{Fr}(E)$, part (a) specialises to a group isomorphism
> $$\mathcal{G}(\operatorname{Fr}(E)) \cong \mathcal{G}(E),$$
> sending a frame-bundle automorphism $f$ to the vector-bundle automorphism $g$ determined by $f(e) = g \circ e$. More generally, every representation $\rho : G \to GL(V)$ induces a homomorphism of groups
> $$\gamma : \mathcal{G}(P) \longrightarrow \mathcal{G}(E), \qquad \gamma(f)[p,v] = [f(p),v] \qquad (E = P\times_\rho V),$$
> and its infinitesimal counterpart $\rho_* : \mathfrak{g} \to \operatorname{End}V$ induces a homomorphism of Lie algebras
> $$\Gamma(\operatorname{ad}P) \longrightarrow \Gamma(\operatorname{End}E), \qquad \xi \longmapsto \rho_* \circ \xi,$$
> where both sides carry the pointwise (fibrewise) bracket.

The three parts descend from a single fact: a gauge transformation is nothing more than a choice, smoothly over $P$, of a group element to multiply by on the right, constrained only by the requirement that this choice be compatible with the $G$-action; and "compatible with the $G$-action" is precisely the conjugation-equivariance that turns the choice into a section of the group bundle $\operatorname{Ad}P$.

---

# Motivation

The gauge group $\mathcal{G}(P)$ is the symmetry group of gauge theory: it is the group by which one quotients the affine space $\mathcal{A}(P)$ of connections to form the moduli spaces $\mathcal{A}(P)/\mathcal{G}(P)$ whose geometry Donaldson and Seiberg–Witten theory study. As it stands in [[Def - Gauge Transformation|its definition]], however, $\mathcal{G}(P)$ is an awkward object: a set of diffeomorphisms of the total space $P$, constrained by two conditions (equivariance and covering the identity), with composition as its law. One cannot easily do analysis on such a set — one cannot say what a "tangent vector" to $\mathcal{G}(P)$ is, cannot put a topology or a norm on it, cannot recognise its connected components — while it is presented as a subset of $\operatorname{Diff}(P)$.

This theorem replaces that presentation with one that lives entirely over the base $M$. It says that a gauge transformation is the *same data* as a smooth section of a bundle of groups $\operatorname{Ad}P \to M$. The gain is total. Sections of a fibre bundle over a compact base are a space one knows how to complete in Sobolev or $C^k$ norms, whose connected components one can count, and whose "Lie algebra" is visibly the sections $\Gamma(\operatorname{ad}P)$ of the associated Lie-algebra bundle. Every later construction that treats $\mathcal{G}(P)$ as an infinite-dimensional Lie group — its action on connections, the linearisation of that action, the Banach completions used to make the moduli spaces manifolds — begins by silently using this identification.

There is a second reason the theorem matters, which is conceptual rather than technical. It explains what makes gauge theory *gauge* theory rather than merely the differential geometry of a connection. A connection has a local description by a $\mathfrak{g}$-valued one-form $A$, and a change of local trivialisation acts on $A$ by $A \mapsto \operatorname{Ad}_{g^{-1}}A + g^*\theta$ for a locally defined $g : U \to G$. A gauge transformation performs *exactly this change of trivialisation, but globally and intrinsically* — the same formula, now driven by a genuine section of $\operatorname{Ad}P$ rather than by an arbitrary choice of chart. The theorem is what licenses the identification of the physicist's "local change of gauge" with the geometer's "global bundle automorphism": both are encoded by the group-valued object the theorem produces.

We assume the reader knows what a principal bundle and an associated bundle are, the freeness and transitivity of the fibre action, and the notion of a section; the adjoint group bundle $\operatorname{Ad}P$ and its fibrewise group structure are recalled from [[Def - Adjoint Bundles ad P and Ad P]] in the Notation above.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal hypothesis is only "a principal bundle $P$"; the informative question is which situations secretly present a gauge transformation, so that the theorem may be applied to convert it into a section one can compute with.

The first disguised source is **a family of local gauge changes that happens to be globally consistent**. In practice one rarely writes down a diffeomorphism of $P$; one writes down, on each patch $U_\alpha$ of a trivialising cover, a smooth map $g_\alpha : U_\alpha \to G$, intending to "change the local gauge". Such a family defines a global gauge transformation precisely when the $g_\alpha$ transform into one another correctly across overlaps, namely $g_\beta = \theta_{\alpha\beta}^{-1}\, g_\alpha\, \theta_{\alpha\beta}$ where $\theta_{\alpha\beta}$ are the transition functions of $P$; that cocycle-conjugation condition is exactly the statement that the $g_\alpha$ patch into one section of $\operatorname{Ad}P$. The bridge $B \Rightarrow A$ is: a conjugation-compatible family of local $G$-valued maps $\Rightarrow$ an element of $\mathcal{G}(P)$. *Example problem:* over $S^1$ with a nontrivial $SU(2)$-bundle, decide whether two locally given rotations glue to a global gauge transformation by checking the conjugation-compatibility on the single overlap.

The second disguised source is **a symmetry of the geometric data on $P$ that fixes the base**. Suppose $\Psi$ is any smooth self-map of the total space that preserves the fibres pointwise on $M$ and commutes with the $G$-action; one meets these as symmetries of a connection ($f^*\omega = \omega$), as deck-like symmetries of a reduction, or as the residual freedom after fixing a frame. Any such $\Psi$ is, by definition, an element of $\mathcal{G}(P)$, and the theorem immediately reorganises it as a section of $\operatorname{Ad}P$, whose zeros and values one can then locate. The bridge is: a fibrewise, equivariant self-map covering the identity $\Rightarrow$ a section of the group bundle. *Example problem:* show that the stabiliser of a connection inside $\mathcal{G}(P)$ consists of the covariantly constant sections of $\operatorname{Ad}P$, by feeding each stabilising gauge transformation through the identification and reading off the constancy condition.

The third disguised source is **a bundle automorphism of an associated vector bundle that one wishes to lift to the principal level**. When $E = P \times_\rho V$ and one is handed $g \in \mathcal{G}(E)$, it is not automatic that $g$ comes from a principal gauge transformation; it does precisely when $g$ is, fibrewise, the image under $\rho$ of a $G$-element, i.e. lies in the subbundle $\rho(\operatorname{Ad}P) \subseteq \operatorname{Aut}E$. Part (c) is the recognition principle: a vector-bundle gauge transformation of the *standard* representation of the *frame* bundle always lifts (there $\gamma$ is an isomorphism), whereas for a general $\rho$ only those in the image of $\gamma$ do. *Example problem:* determine which unitary automorphisms of the adjoint bundle of an $SU(2)$-bundle come from principal gauge transformations, using that $\gamma$ for $\rho = \operatorname{Ad}$ has kernel the constant central sections.

**Targets (Output Amplification)**

The bare conclusion is an isomorphism $\mathcal{G}(P) \cong \Gamma(\operatorname{Ad}P)$; combined with further structure it yields much more.

Combine the conclusion with **a compact base and a completion of section spaces**. Because $\Gamma(\operatorname{Ad}P)$ is the section space of a fibre bundle of groups over a compact $M$, one may complete it in a $C^k$ or Sobolev norm; the isomorphism then transports the group law of $\mathcal{G}(P)$ onto this completion, and one obtains that $\mathcal{G}(P)$ is an infinite-dimensional (Banach or Fréchet) Lie group with Lie algebra $\Gamma(\operatorname{ad}P)$ (respectively its completion). The extra ingredient is Banach-algebra analysis of the sections; the payoff is that the quotient $\mathcal{A}/\mathcal{G}$ can be given a manifold structure. This is developed in [[Ex - The C^k Gauge Group of a Matrix Group Bundle is a Banach Lie Group|the Banach-Lie-group exercise]] and used in chapters IX and XI.

Combine the conclusion with **the classification of the group bundle up to homotopy**. The connected components $\pi_0(\mathcal{G}(P))$ are, via the isomorphism, the components of $\Gamma(\operatorname{Ad}P)$, i.e. homotopy classes of sections; for an abelian $G$ these are the homotopy classes of maps $M \to G$, a computable homotopy invariant. The extra ingredient is homotopy theory of mapping spaces; the payoff is the labelling of gauge orbits by discrete invariants — for $G = U(1)$ over $S^1$, the winding number — which organises the topology of the moduli space.

Combine the conclusion with **the action of $\mathcal{G}(P)$ on connections**. Once a gauge transformation is a section, the transformation law of a connection under it becomes the intrinsic global version $A \mapsto \operatorname{Ad}_{g^{-1}}A + g^*\theta$ with $g$ a section of $\operatorname{Ad}P$, proved on [[Thm - Gauge Transformations Act on Connections and Curvature]]. The extra ingredient is the differential of the section; the payoff is that gauge invariance of curvature norms and of Chern–Weil forms can be checked fibrewise on $M$, rather than on the total space $P$.

---

# Why Is It True

Strip away the bundles and look at a single fibre $P_m$. The group $G$ acts on $P_m$ freely and transitively, so $P_m$ is a *torsor*: it looks exactly like $G$, but with no preferred identity element. A gauge transformation, restricted to this fibre, is a bijection $P_m \to P_m$ that commutes with the $G$-action. Now, the maps of a torsor to itself that commute with the group action are in bijection with the group itself: each such map is "right multiplication by some fixed group element", except that, because there is no preferred identity in the torsor, the group element it corresponds to *depends on where you look from*. Choose a base point $p \in P_m$; then the map sends $p$ to $p\cdot\gamma$ for a unique $\gamma \in G$, and by equivariance it sends every $p\cdot g$ to $p\cdot\gamma g = (p\cdot g)\cdot(g^{-1}\gamma g)$. So viewed from the base point $p\cdot g$, the *same* map is "right multiplication by $g^{-1}\gamma g$". The group element is well defined only up to conjugation as the viewpoint changes — and "a $G$-element well defined up to the conjugation induced by the change of base point in the fibre" is exactly what a point of the fibre $(\operatorname{Ad}P)_m$ of the conjugation-associated bundle is.

> **The mechanism in one sentence:** a gauge transformation multiplies each point of each fibre on the right by a group element, but the group element is read off relative to a choice of base point in the fibre, so it is intrinsically defined only up to conjugation — that is, as a point of $\operatorname{Ad}P$ — and letting $m$ vary turns the whole gauge transformation into a section of $\operatorname{Ad}P$.

Doing this smoothly over all of $M$ upgrades the fibrewise statement to the bundle statement: the assignment $p \mapsto \hat f(p)$ (the element seen from $p$) is a smooth function $P \to G$, conjugation-equivariant by the computation above, and conjugation-equivariant $G$-valued functions on $P$ are exactly the sections of $\operatorname{Ad}P$. The group law is inherited for free: composing two gauge transformations multiplies, at each point, the two group elements one reads off, and that is the fibrewise product in $\operatorname{Ad}P$. The abelian case (b) is the collapse of the conjugation ambiguity — when $G$ is abelian, $g^{-1}\gamma g = \gamma$, so the group element no longer depends on the viewpoint and descends to an honest function on $M$. Part (c) is the same mechanism seen through a representation: applying $\rho$ to the group element read off from $P$ produces the group element by which the associated fibre is multiplied.

---

# What Makes This Hard

The single genuine subtlety is that the "group element $\hat f(p)$" a gauge transformation multiplies by is **not** a function on the base — it is a function on the total space, and it transforms by conjugation when the argument moves along a fibre. The beginner's error is to write $f(p) = p\cdot g$ with $g$ constant, or $f(p) = p\cdot g(\pi(p))$ with $g$ a function on $M$, and to believe this exhausts $\mathcal{G}(P)$; part (b) is precisely the warning that this recipe captures *all* gauge transformations only when $G$ is abelian, and otherwise only the central ones. The second point requiring care is that $\operatorname{Ad}P$ is a bundle of *groups*, not a vector bundle, so the standard associated-bundle theorem (stated for representations on vector spaces) does not literally apply; one must re-run its proof for the conjugation action on the manifold $G$, checking that only freeness and transitivity of the fibre action — not the linear structure — were ever used. Everything else is bookkeeping: the smoothness of $\hat f$ is a one-line trivialisation argument, and the group-isomorphism claim is a short computation with the equivariance identity.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Coordinatise each fibre by writing a gauge transformation as right multiplication by a point-dependent group element $\hat f(p)$; extract the conjugation-equivariance of $\hat f$ from the equivariance of $f$; recognise conjugation-equivariant functions as sections of the group bundle $\operatorname{Ad}P$; and check that composition of gauge transformations becomes pointwise multiplication of sections. The abelian and representation statements are then short specialisations.

**Subgoal decomposition:**

1. **Coordinatise.** For $f \in \mathcal{G}(P)$ produce a unique smooth $\hat f : P \to G$ with $f(p) = p\cdot\hat f(p)$, and prove $\hat f(pg) = g^{-1}\hat f(p)g$; conversely, show any such smooth equivariant $\hat f$ gives an $f \in \mathcal{G}(P)$.
   - *Hint:* Existence and uniqueness of $\hat f(p)$ come from the free transitive fibre action; equivariance comes from expanding $f(pg) = f(p)g$; smoothness comes from a local trivialisation, where $\hat f(p) = \psi(p)^{-1}\psi(f(p))$.
   - *Why needed:* This is the passage from a diffeomorphism of $P$ to a $G$-valued function, the whole content of the identification at the level of maps.

2. **Sections of the group bundle.** Show that $\hat f \mapsto \big(m \mapsto [p,\hat f(p)]\big)$ is a bijection from conjugation-equivariant smooth functions onto $\Gamma(\operatorname{Ad}P)$.
   - *Hint:* Well-definedness of the section uses the equivalence relation of $\operatorname{Ad}P$; the inverse map recovers $\hat f(p)$ as the unique $\gamma$ with $[p,\gamma] = s(\pi p)$, using freeness.
   - *Why needed:* It turns the function $\hat f$ into a genuine section over $M$, the object one wants to do analysis with.

3. **Group isomorphism.** Show composition of gauge transformations corresponds to pointwise multiplication: $\widehat{f_1\circ f_2} = \hat f_1 \cdot \hat f_2$, identity to constant $e$, inverse to pointwise inverse.
   - *Hint:* Compute $f_1(f_2(p)) = f_1(p\cdot\hat f_2(p)) = f_1(p)\cdot\hat f_2(p) = p\cdot(\hat f_1(p)\hat f_2(p))$ using equivariance of $f_1$.
   - *Why needed:* Upgrades the bijection of sets to an isomorphism of groups, which is the theorem's point.

4. **Central/abelian case.** Determine when $f(p) = p\cdot g(\pi p)$ is a gauge transformation.
   - *Hint:* Equivariance of $\hat f = g\circ\pi$ forces $g(\pi p) = g'^{-1}g(\pi p)g'$ for all $g'$, i.e. $g(m) \in Z(G)$; abelian $G$ makes this automatic.
   - *Why needed:* Isolates the special maps that live over $M$ and the isomorphism $\mathcal{G}(P) \cong C^\infty(M;G)$ for abelian $G$.

5. **Frame bundle.** Identify $\mathcal{G}(\operatorname{Fr}(E))$ with $\mathcal{G}(E)$.
   - *Hint:* $\operatorname{Ad}\operatorname{Fr}(E) \cong \operatorname{Aut}E$ via $[e,a] \mapsto e\circ a\circ e^{-1}$; take sections and use part (a).
   - *Why needed:* Reconciles the principal-bundle gauge group with the vector-bundle gauge group of chapter II.

6. **Representation homomorphism.** Build $\gamma : \mathcal{G}(P) \to \mathcal{G}(E)$ and its infinitesimal version.
   - *Hint:* Set $\gamma(f)[p,v] = [f(p),v]$; well-definedness uses $f$ equivariant; the Lie-algebra map is $\xi \mapsto \rho_*\circ\xi$, a homomorphism because $\rho_*$ is.
   - *Why needed:* Extends the identification functorially to every associated bundle, the form in which it is used to couple gauge fields to matter.

---

# Lemma Decomposition

> [!note]- Lemma 1: A gauge transformation is right multiplication by a conjugation-equivariant $G$-valued function
> **Statement:** Let $f \in \mathcal{G}(P)$. There is a unique map $\hat f : P \to G$ with $f(p) = p\cdot\hat f(p)$ for all $p \in P$; it is smooth and satisfies $\hat f(p\cdot g) = g^{-1}\,\hat f(p)\,g$ for all $p \in P$, $g \in G$. Conversely, if $\hat f \in C^\infty(P;G)$ satisfies $\hat f(pg) = g^{-1}\hat f(p)g$, then $f(p) := p\cdot\hat f(p)$ defines an element of $\mathcal{G}(P)$. The assignment $f \mapsto \hat f$ is a bijection $\mathcal{G}(P) \to C^\infty(P;G)^{\mathrm{conj}}$.
>
> **Hint:** Freeness and transitivity of the fibre action give existence and uniqueness of $\hat f(p)$; expand $f(pg)=f(p)g$ to get equivariance; a local equivariant trivialisation gives smoothness.
>
> **Why needed:** It is the passage from a diffeomorphism of the total space to a $G$-valued function, the level at which the identification first happens.
>
> > [!note]- Full proof
> > **Existence and uniqueness of $\hat f(p)$.** Fix $p \in P$. Since $f$ covers the identity, $\pi(f(p)) = \pi(p)$, so $f(p)$ lies in the same fibre $P_{\pi(p)}$ as $p$. The $G$-action is transitive on $P_{\pi(p)}$, so there exists $\gamma \in G$ with $f(p) = p\cdot\gamma$; and it is free, so this $\gamma$ is unique. Define $\hat f(p) := \gamma$; then $f(p) = p\cdot\hat f(p)$ by construction, and $\hat f(p)$ is the only element of $G$ with this property.
> >
> > **Conjugation-equivariance of $\hat f$.** Let $p \in P$ and $g \in G$. On one hand, by the definition of $\hat f$ applied at $p\cdot g$,
> > $$f(p\cdot g) = (p\cdot g)\cdot\hat f(p\cdot g) = p\cdot\big(g\,\hat f(p\cdot g)\big) \qquad \text{(definition of $\hat f$ at $pg$; associativity of the action).}$$
> > On the other hand, since $f$ is $G$-equivariant (it is a gauge transformation),
> > $$f(p\cdot g) = f(p)\cdot g = \big(p\cdot\hat f(p)\big)\cdot g = p\cdot\big(\hat f(p)\,g\big) \qquad \text{(equivariance of $f$; definition of $\hat f$ at $p$; associativity).}$$
> > Comparing the two expressions, $p\cdot\big(g\,\hat f(pg)\big) = p\cdot\big(\hat f(p)\,g\big)$, and by freeness of the action we may cancel $p$ to obtain $g\,\hat f(pg) = \hat f(p)\,g$, that is,
> > $$\hat f(p\cdot g) = g^{-1}\,\hat f(p)\,g \qquad \text{(left-multiply by $g^{-1}$).}$$
> >
> > **Smoothness of $\hat f$.** Let $m_0 \in M$ and choose a trivialising open set $U \ni m_0$ with a $G$-equivariant trivialisation $\Psi : \pi^{-1}(U) \to U \times G$, $\Psi(p) = (\pi(p), \psi(p))$, where $\psi : \pi^{-1}(U) \to G$ satisfies $\psi(p\cdot g) = \psi(p)\,g$ (such a $\Psi$ exists by the definition of a principal bundle). Since $f$ covers the identity, $f\big(\pi^{-1}(U)\big) \subseteq \pi^{-1}(U)$, and for $p \in \pi^{-1}(U)$,
> > $$\psi(f(p)) = \psi\big(p\cdot\hat f(p)\big) = \psi(p)\,\hat f(p) \qquad \text{(definition of $\hat f$; equivariance of $\psi$),}$$
> > hence
> > $$\hat f(p) = \psi(p)^{-1}\,\psi(f(p)) \qquad \text{(left-multiply by $\psi(p)^{-1}$).}$$
> > The right-hand side is a composition of the smooth maps $\psi$, $f$, group inversion, and group multiplication, so $\hat f$ is smooth on $\pi^{-1}(U)$. As $m_0$ was arbitrary, $\hat f \in C^\infty(P;G)$.
> >
> > **Converse.** Suppose $\hat f \in C^\infty(P;G)$ with $\hat f(pg) = g^{-1}\hat f(p)g$, and set $f(p) := p\cdot\hat f(p)$. Then $f$ is smooth (a composition of $\hat f$ with the smooth action map), and $\pi(f(p)) = \pi(p)$ because the action preserves fibres, so $f$ covers the identity. It is equivariant: for $g \in G$,
> > $$f(p\cdot g) = (p\cdot g)\cdot\hat f(p\cdot g) = p\cdot\big(g\,g^{-1}\hat f(p)\,g\big) = p\cdot\big(\hat f(p)\,g\big) = \big(p\cdot\hat f(p)\big)\cdot g = f(p)\cdot g \qquad \text{(equivariance hypothesis on $\hat f$; associativity).}$$
> > It is a diffeomorphism: define $f'(p) := p\cdot\hat f(p)^{-1}$, which is smooth and, since $\hat f(pg)^{-1} = (g^{-1}\hat f(p)g)^{-1} = g^{-1}\hat f(p)^{-1}g$, is again equivariant and covers the identity by the same computation. Then
> > $$f'(f(p)) = f(p)\cdot\hat f(f(p))^{-1};$$
> > but $f(p) = p\cdot\hat f(p)$, so by equivariance of $\hat f$, $\hat f(f(p)) = \hat f(p\cdot\hat f(p)) = \hat f(p)^{-1}\hat f(p)\hat f(p) = \hat f(p)$, whence $f'(f(p)) = p\cdot\hat f(p)\cdot\hat f(p)^{-1} = p$. Symmetrically $f(f'(p)) = p$. Thus $f' = f^{-1}$ is smooth, $f$ is a diffeomorphism, and $f \in \mathcal{G}(P)$.
> >
> > **Bijectivity.** The map $f \mapsto \hat f$ is injective, because $f$ is recovered from $\hat f$ by $f(p) = p\cdot\hat f(p)$ (two gauge transformations with the same $\hat f$ agree at every point). It is surjective onto $C^\infty(P;G)^{\mathrm{conj}}$ by the converse just proved. Hence it is a bijection $\mathcal{G}(P) \to C^\infty(P;G)^{\mathrm{conj}}$. $\blacksquare$

> [!note]- Lemma 2: Conjugation-equivariant $G$-valued functions are the sections of $\operatorname{Ad}P$
> **Statement:** The map
> $$\Sigma : C^\infty(P;G)^{\mathrm{conj}} \longrightarrow \Gamma(\operatorname{Ad}P), \qquad \Sigma(\hat f)(m) = [p,\hat f(p)] \ \text{ for any } p \in P_m,$$
> is a well-defined bijection, with inverse sending a section $s$ to the function $\hat f$ determined by $[p,\hat f(p)] = s(\pi(p))$.
>
> **Hint:** Well-definedness of $\Sigma(\hat f)(m)$ under change of $p \in P_m$ is exactly the equivalence relation $[p,\gamma] = [pg, g^{-1}\gamma g]$; the inverse uses that $\gamma \mapsto [p,\gamma]$ is a bijection $G \to (\operatorname{Ad}P)_{\pi p}$ by freeness.
>
> **Why needed:** It converts the total-space function $\hat f$ into a section over the base, the form in which the gauge group becomes analysable. This is the fibre-bundle analogue, for the conjugation action, of [[Thm - Sections of an Associated Bundle are Equivariant Functions|the equivariant-function theorem]].
>
> > [!note]- Full proof
> > Recall from [[Def - Adjoint Bundles ad P and Ad P]] that $\operatorname{Ad}P = (P\times G)/\!\sim$ with $(p,\gamma) \sim (p\cdot h, h^{-1}\gamma h)$, that $\varpi[p,\gamma] = \pi(p)$, and that for fixed $p$ the map $\iota_p : G \to (\operatorname{Ad}P)_{\pi(p)}$, $\gamma \mapsto [p,\gamma]$, is a bijection: it is surjective because every class in the fibre over $\pi(p)$ has a representative with first coordinate $p$ (transitivity: any representative $(p', \gamma')$ has $p' = p\cdot h$, so $[p',\gamma'] = [p, h\gamma' h^{-1}]$), and injective because $[p,\gamma] = [p,\gamma']$ means $(p,\gamma') = (p\cdot h, h^{-1}\gamma h)$ for some $h$, forcing $p = p\cdot h$, hence $h = e$ by freeness, hence $\gamma' = \gamma$.
> >
> > **$\Sigma(\hat f)$ is a well-defined section.** Let $\hat f \in C^\infty(P;G)^{\mathrm{conj}}$ and $m \in M$. For two points $p, p' \in P_m$ there is a unique $h \in G$ with $p' = p\cdot h$, and
> > $$[p',\hat f(p')] = [p\cdot h,\ \hat f(p\cdot h)] = [p\cdot h,\ h^{-1}\hat f(p)h] = [p,\hat f(p)] \qquad \text{(equivariance of $\hat f$; the relation $(p\cdot h, h^{-1}\gamma h)\sim(p,\gamma)$),}$$
> > so the value $\Sigma(\hat f)(m) := [p,\hat f(p)]$ does not depend on the choice of $p \in P_m$. Moreover $\varpi(\Sigma(\hat f)(m)) = \pi(p) = m$, so $\Sigma(\hat f)$ is a section of $\varpi$.
> >
> > **$\Sigma(\hat f)$ is smooth.** Let $m_0 \in M$ and let $\sigma : U \to P$ be a smooth local section of $\pi$ on an open $U \ni m_0$ (which exists since $P$ is locally trivial). For $m \in U$, take $p = \sigma(m)$: then
> > $$\Sigma(\hat f)(m) = [\sigma(m),\ \hat f(\sigma(m))] = q\big(\sigma(m),\ \hat f(\sigma(m))\big),$$
> > where $q : P\times G \to \operatorname{Ad}P$ is the (smooth) quotient projection. The map $m \mapsto (\sigma(m), \hat f(\sigma(m)))$ is smooth into $P\times G$, and $q$ is smooth, so $\Sigma(\hat f)|_U$ is smooth. As $m_0$ was arbitrary, $\Sigma(\hat f) \in \Gamma(\operatorname{Ad}P)$.
> >
> > **The inverse.** Given $s \in \Gamma(\operatorname{Ad}P)$, define $\hat f_s : P \to G$ by letting $\hat f_s(p)$ be the unique $\gamma \in G$ with $[p,\gamma] = s(\pi(p))$; this $\gamma$ exists and is unique because $\iota_p$ is a bijection onto $(\operatorname{Ad}P)_{\pi(p)}$ and $s(\pi(p))$ lies in that fibre. Then $\hat f_s$ is conjugation-equivariant: for $g \in G$, the defining relations $[p,\hat f_s(p)] = s(\pi(p))$ and the identity $s(\pi(pg)) = s(\pi(p))$ (as $\pi(pg) = \pi(p)$) give
> > $$[p\cdot g,\ \hat f_s(pg)] = s(\pi(pg)) = s(\pi(p)) = [p,\hat f_s(p)] = [p\cdot g,\ g^{-1}\hat f_s(p)g] \qquad \text{(the relation applied with $h = g$),}$$
> > and applying the injective $\iota_{pg}$ yields $\hat f_s(pg) = g^{-1}\hat f_s(p)g$. Smoothness of $\hat f_s$ follows as in Lemma 1: on a trivialisation $\Psi = (\pi,\psi)$ over $U$ with local section $\sigma$, writing $s|_U(m) = q(\sigma(m), \tau(m))$ for a smooth $\tau : U \to G$ (a smooth local trivialisation of $\operatorname{Ad}P$), one has $\hat f_s(p) = \psi(p)^{-1}\,\tau(\pi(p))\,\psi(p)$ for $p \in \pi^{-1}(U)$, a composition of smooth maps.
> >
> > **Mutually inverse.** For $\hat f \in C^\infty(P;G)^{\mathrm{conj}}$, the function $\hat f_{\Sigma(\hat f)}$ is, at each $p$, the unique $\gamma$ with $[p,\gamma] = \Sigma(\hat f)(\pi(p)) = [p,\hat f(p)]$, so $\gamma = \hat f(p)$; thus $\hat f_{\Sigma(\hat f)} = \hat f$. Conversely, for $s \in \Gamma(\operatorname{Ad}P)$, $\Sigma(\hat f_s)(m) = [p,\hat f_s(p)] = s(\pi(p)) = s(m)$ for $p \in P_m$; thus $\Sigma(\hat f_s) = s$. Hence $\Sigma$ is a bijection. $\blacksquare$

> [!note]- Lemma 3: The bijection is a group isomorphism
> **Statement:** Write $\Phi := \Sigma \circ (f \mapsto \hat f) : \mathcal{G}(P) \to \Gamma(\operatorname{Ad}P)$. Then $\Phi(f_1 \circ f_2) = \Phi(f_1)\cdot\Phi(f_2)$ (pointwise product of sections), $\Phi(\operatorname{id}_P)$ is the unit section $m \mapsto [p,e]$, and $\Phi(f^{-1}) = \Phi(f)^{-1}$. Hence $\Phi$ is an isomorphism of groups $\mathcal{G}(P) \cong \Gamma(\operatorname{Ad}P)$.
>
> **Hint:** Everything reduces to $\widehat{f_1\circ f_2} = \hat f_1\cdot\hat f_2$ (pointwise product in $G$), which follows from expanding $f_1(f_2(p))$ using the equivariance of $f_1$.
>
> **Why needed:** It upgrades the set bijection of Lemmas 1–2 to an isomorphism of groups, which is the assertion of part (a).
>
> > [!note]- Full proof
> > **Composition becomes pointwise product of the functions.** Let $f_1, f_2 \in \mathcal{G}(P)$ and $p \in P$. Then
> > $$(f_1\circ f_2)(p) = f_1\big(f_2(p)\big) = f_1\big(p\cdot\hat f_2(p)\big) = f_1(p)\cdot\hat f_2(p) = \big(p\cdot\hat f_1(p)\big)\cdot\hat f_2(p) = p\cdot\big(\hat f_1(p)\,\hat f_2(p)\big),$$
> > where the third equality uses the $G$-equivariance of $f_1$ with the element $\hat f_2(p) \in G$, and the others are the definition of $\hat f_2$, of $\hat f_1$, and associativity. By the uniqueness in Lemma 1, this identifies
> > $$\widehat{f_1\circ f_2}(p) = \hat f_1(p)\,\hat f_2(p) \qquad (p \in P),$$
> > the pointwise product in $G$.
> >
> > **Translation to sections.** Applying $\Sigma$ and the fibrewise product $[p,\gamma]\cdot[p,\gamma'] = [p,\gamma\gamma']$ of $\operatorname{Ad}P$, for $m \in M$ and $p \in P_m$,
> > $$\Phi(f_1\circ f_2)(m) = [p,\ \hat f_1(p)\hat f_2(p)] = [p,\hat f_1(p)]\cdot[p,\hat f_2(p)] = \Phi(f_1)(m)\cdot\Phi(f_2)(m) = \big(\Phi(f_1)\cdot\Phi(f_2)\big)(m),$$
> > using the fibrewise multiplication and the definition of the pointwise product of sections. Hence $\Phi(f_1\circ f_2) = \Phi(f_1)\cdot\Phi(f_2)$.
> >
> > **Identity and inverse.** For $f = \operatorname{id}_P$ we have $\operatorname{id}_P(p) = p = p\cdot e$, so $\widehat{\operatorname{id}_P}(p) = e$ (uniqueness, Lemma 1), and $\Phi(\operatorname{id}_P)(m) = [p,e]$, the unit section. Since $\Phi$ is a bijection (Lemmas 1–2) and preserves products, it also preserves inverses: from $\Phi(f\circ f^{-1}) = \Phi(f)\cdot\Phi(f^{-1})$ and $f\circ f^{-1} = \operatorname{id}_P$ we get $\Phi(f)\cdot\Phi(f^{-1}) = \Phi(\operatorname{id}_P) = $ unit, so $\Phi(f^{-1}) = \Phi(f)^{-1}$ (the pointwise inverse). Therefore $\Phi$ is a group isomorphism. $\blacksquare$

> [!note]- Lemma 4: The maps of the form $p \mapsto p\cdot g(\pi p)$ are exactly the central ones
> **Statement:** Let $g : M \to G$ be smooth and define $f(p) := p\cdot g(\pi(p))$. Then $f \in \mathcal{G}(P)$ if and only if $g(m) \in Z(G)$ for every $m \in M$. In particular, if $G$ is abelian then every smooth $g : M \to G$ yields a gauge transformation, all gauge transformations arise this way, and $\Phi$ restricts to an isomorphism $\mathcal{G}(P) \cong C^\infty(M;G)$.
>
> **Hint:** The associated function is $\hat f = g\circ\pi$; its conjugation-equivariance forces $g(m) = g'^{-1}g(m)g'$ for all $g' \in G$.
>
> **Why needed:** It gives the exact scope of the elementary recipe "gauge transformation = map to the group" and proves part (b).
>
> > [!note]- Full proof
> > **Reduction to equivariance of $g\circ\pi$.** The map $f(p) = p\cdot g(\pi(p))$ is smooth, covers the identity ($\pi(f(p)) = \pi(p)$), and its associated function is $\hat f = g\circ\pi$ (it is the unique function with $f(p) = p\cdot\hat f(p)$). By Lemma 1, $f \in \mathcal{G}(P)$ if and only if $\hat f$ is conjugation-equivariant and smooth; $\hat f = g\circ\pi$ is smooth since $g$ and $\pi$ are, so the only condition is equivariance:
> > $$\hat f(p\cdot g') = g'^{-1}\hat f(p)\,g' \quad \text{for all } p, g'.$$
> > Now $\hat f(p\cdot g') = g(\pi(p\cdot g')) = g(\pi(p))$ because $\pi(p\cdot g') = \pi(p)$; so the equivariance condition reads $g(\pi(p)) = g'^{-1}\,g(\pi(p))\,g'$ for all $p \in P$ and $g' \in G$.
> >
> > **The condition is centrality.** Fix $m \in M$ and pick $p \in P_m$ (the fibre is non-empty as $\pi$ is surjective). The condition becomes $g(m) = g'^{-1}g(m)g'$ for all $g' \in G$, equivalently $g'\,g(m) = g(m)\,g'$ for all $g' \in G$, which is by definition $g(m) \in Z(G)$. Since $m$ was arbitrary, $f \in \mathcal{G}(P)$ if and only if $g(M) \subseteq Z(G)$.
> >
> > **Abelian case.** If $G$ is abelian then $Z(G) = G$, so every smooth $g : M \to G$ gives a gauge transformation, and the assignment $g \mapsto \big(p \mapsto p\cdot g(\pi p)\big)$ is a map $C^\infty(M;G) \to \mathcal{G}(P)$. It is surjective: for any $f \in \mathcal{G}(P)$, the function $\hat f$ is conjugation-equivariant, and for abelian $G$ conjugation is trivial, $g'^{-1}\hat f(p)g' = \hat f(p)$, so $\hat f(pg') = \hat f(p)$; thus $\hat f$ is constant on fibres and descends to a smooth $g : M \to G$ with $\hat f = g\circ\pi$ (smoothness of $g$ follows from a local section: $g|_U = \hat f\circ\sigma$), whence $f(p) = p\cdot g(\pi p)$. It is injective because $g$ is recovered as $g = \hat f\circ\sigma$ from any local section, and it is a homomorphism into $\mathcal{G}(P)$: for the abelian group $G$ the fibrewise product of $\operatorname{Ad}P = M\times G$ is the pointwise product of $G$-valued functions, so under $\Phi$ this map is the identification of $C^\infty(M;G)$ with $\Gamma(\operatorname{Ad}P) = \Gamma(M\times G) = C^\infty(M;G)$. Therefore $\mathcal{G}(P) \cong C^\infty(M;G)$. $\blacksquare$

> [!note]- Lemma 5: For a frame bundle, the principal and vector-bundle gauge groups coincide
> **Statement:** Let $E \to M$ be a rank-$k$ real vector bundle with frame bundle $\operatorname{Fr}(E)$ (structure group $GL_k(\mathbb{R})$). Then $\operatorname{Ad}\operatorname{Fr}(E) \cong \operatorname{Aut}E$ as bundles of groups, and consequently $\Phi$ induces a group isomorphism $\mathcal{G}(\operatorname{Fr}(E)) \cong \Gamma(\operatorname{Aut}E) = \mathcal{G}(E)$, under which a frame-bundle automorphism $f$ corresponds to the vector-bundle automorphism $g$ with $f(e) = g\circ e$ for every frame $e$.
>
> **Hint:** A frame $e$ is a linear isomorphism $\mathbb{R}^k \to E_m$; map $[e,a] \in \operatorname{Ad}\operatorname{Fr}(E)$ to $e\circ a\circ e^{-1} \in GL(E_m)$.
>
> **Why needed:** It reconciles the gauge group of a principal bundle with the gauge group of a vector bundle defined directly in chapter II, proving the first half of part (c).
>
> > [!note]- Full proof
> > **The bundle isomorphism.** Recall a point of $\operatorname{Fr}(E)_m$ is a linear isomorphism $e : \mathbb{R}^k \to E_m$, with right action $e\cdot a = e\circ a$ for $a \in GL_k(\mathbb{R})$. Define
> > $$\Theta : \operatorname{Ad}\operatorname{Fr}(E) \to \operatorname{Aut}E, \qquad \Theta[e,a] = e\circ a\circ e^{-1} \in GL(E_m) \quad (m = \pi(e)).$$
> > *Well defined:* for $b \in GL_k(\mathbb{R})$,
> > $$\Theta[e\cdot b,\ b^{-1}ab] = (e\circ b)\circ(b^{-1}ab)\circ(e\circ b)^{-1} = e\circ b\circ b^{-1}ab\circ b^{-1}\circ e^{-1} = e\circ a\circ e^{-1} = \Theta[e,a],$$
> > using associativity of composition and $(e\circ b)^{-1} = b^{-1}\circ e^{-1}$; so $\Theta$ respects the conjugation relation. *Fibrewise bijective:* for fixed $e$, the map $GL_k(\mathbb{R}) \to GL(E_m)$, $a \mapsto e\circ a\circ e^{-1}$, is a group isomorphism (conjugation by the invertible $e$), and every class in $(\operatorname{Ad}\operatorname{Fr}(E))_m$ has a representative $[e,a]$ with this fixed $e$ (transitivity, as in Lemma 2), so $\Theta$ is a bijection on each fibre. *Fibrewise homomorphism:*
> > $$\Theta\big([e,a]\cdot[e,a']\big) = \Theta[e,aa'] = e(aa')e^{-1} = (eae^{-1})(ea'e^{-1}) = \Theta[e,a]\cdot\Theta[e,a'].$$
> > *Smoothness:* over a trivialising $U$ with local frame field $\sigma : U \to \operatorname{Fr}(E)$, one has $\Theta[q(\sigma(m),a)] = \sigma(m)\circ a\circ\sigma(m)^{-1}$, smooth in $(m,a)$; thus $\Theta$ is a smooth bundle isomorphism covering $\operatorname{id}_M$. Hence $\operatorname{Ad}\operatorname{Fr}(E) \cong \operatorname{Aut}E$ as bundles of groups, and taking sections, $\Gamma(\operatorname{Ad}\operatorname{Fr}(E)) \cong \Gamma(\operatorname{Aut}E) = \mathcal{G}(E)$ (the last equality is the definition of $\mathcal{G}(E)$ recalled in the Notation).
> >
> > **Identification of the gauge groups.** Composing with the isomorphism $\Phi : \mathcal{G}(\operatorname{Fr}(E)) \cong \Gamma(\operatorname{Ad}\operatorname{Fr}(E))$ of part (a) gives a group isomorphism $\mathcal{G}(\operatorname{Fr}(E)) \cong \mathcal{G}(E)$. *Explicit form:* let $f \in \mathcal{G}(\operatorname{Fr}(E))$ correspond to $g \in \mathcal{G}(E)$. By construction $g(m) = \Theta\big(\Phi(f)(m)\big) = \Theta[e,\hat f(e)] = e\circ\hat f(e)\circ e^{-1}$ for any frame $e \in \operatorname{Fr}(E)_m$. On the other hand $f(e) = e\cdot\hat f(e) = e\circ\hat f(e)$ (right action of $GL_k(\mathbb R)$ is precomposition), so
> > $$g\circ e = (e\circ\hat f(e)\circ e^{-1})\circ e = e\circ\hat f(e) = f(e).$$
> > Thus $f(e) = g\circ e$: the frame-bundle automorphism is postcomposition of frames by the vector-bundle automorphism. $\blacksquare$

> [!note]- Lemma 6: A representation induces a gauge-group homomorphism and, infinitesimally, a Lie-algebra-bundle homomorphism
> **Statement:** Let $\rho : G \to GL(V)$ be a representation and $E = P\times_\rho V$. Then
> $$\gamma : \mathcal{G}(P) \to \mathcal{G}(E), \qquad \gamma(f)[p,v] = [f(p),v],$$
> is a well-defined homomorphism of groups. Its differential $\rho_* : \mathfrak{g} \to \operatorname{End}V$ induces, fibrewise, a well-defined map $\Gamma(\operatorname{ad}P) \to \Gamma(\operatorname{End}E)$, $\xi \mapsto \rho_*\circ\xi$, which is a homomorphism of Lie algebras for the pointwise brackets.
>
> **Hint:** Well-definedness of $\gamma(f)$ uses the equivariance of $f$; that $\rho_*\circ\xi$ is a section of $\operatorname{End}E$ uses the naturality $\rho_*\circ\operatorname{Ad}_{g^{-1}} = \operatorname{Ad}_{\rho(g)^{-1}}\circ\rho_*$.
>
> **Why needed:** It extends the identification functorially to every associated bundle and gives the second half of part (c).
>
> > [!note]- Full proof
> > **$\gamma(f)$ is well defined and lies in $\mathcal{G}(E)$.** Represent a point of $E$ as $[p,v]$; a second representative of the same point is $(p\cdot g,\ \rho(g^{-1})v)$. Then
> > $$\gamma(f)[p\cdot g,\ \rho(g^{-1})v] = [f(p\cdot g),\ \rho(g^{-1})v] = [f(p)\cdot g,\ \rho(g^{-1})v] = [f(p),\ v] = \gamma(f)[p,v],$$
> > using equivariance $f(pg) = f(p)g$ and the defining relation $[q\cdot g, \rho(g^{-1})w] = [q,w]$ of the associated bundle. So $\gamma(f)$ is well defined. It covers the identity because $f$ does: $[p,v]$ and $[f(p),v]$ lie over $\pi(p)$. On the fibre $E_m = \{[p,v] : v \in V\}$ (with $p \in P_m$ fixed) it acts by $[p,v] \mapsto [f(p),v] = [p\cdot\hat f(p),\ v] = [p,\ \rho(\hat f(p))v]$, i.e. by the linear isomorphism $\rho(\hat f(p)) \in GL(V)$ read in the frame $[p,\cdot]$; hence $\gamma(f)(m) \in GL(E_m)$ and $\gamma(f) \in \mathcal{G}(E)$. (Smoothness of $\gamma(f)$ follows since, over a local section $\sigma$, its matrix is $m \mapsto \rho(\hat f(\sigma(m)))$, smooth.)
> >
> > **$\gamma$ is a homomorphism.** For $f_1, f_2 \in \mathcal{G}(P)$ and $[p,v] \in E$,
> > $$\gamma(f_1\circ f_2)[p,v] = [(f_1\circ f_2)(p),\ v] = [f_1(f_2(p)),\ v] = \gamma(f_1)[f_2(p),\ v] = \gamma(f_1)\big(\gamma(f_2)[p,v]\big),$$
> > so $\gamma(f_1\circ f_2) = \gamma(f_1)\circ\gamma(f_2)$.
> >
> > **The infinitesimal map is well defined.** A section $\xi \in \Gamma(\operatorname{ad}P)$ corresponds (by the equivariant-function description, [[Thm - Sections of an Associated Bundle are Equivariant Functions]], applied to the representation $\operatorname{Ad}$ on $\mathfrak{g}$) to a smooth $\hat\xi : P \to \mathfrak{g}$ with $\hat\xi(pg) = \operatorname{Ad}_{g^{-1}}\hat\xi(p)$. Set $\widehat{\rho_*\xi} := \rho_*\circ\hat\xi : P \to \operatorname{End}V$. Using the naturality of the differential — differentiating $\rho(g h g^{-1}) = \rho(g)\rho(h)\rho(g)^{-1}$ in $h$ at $h = e$ gives $\rho_*(\operatorname{Ad}_g X) = \rho(g)\,\rho_*(X)\,\rho(g)^{-1}$ for all $X \in \mathfrak{g}$ — we compute
> > $$\widehat{\rho_*\xi}(pg) = \rho_*\big(\operatorname{Ad}_{g^{-1}}\hat\xi(p)\big) = \rho(g^{-1})\,\rho_*(\hat\xi(p))\,\rho(g) = \operatorname{Ad}_{\rho(g)^{-1}}\,\widehat{\rho_*\xi}(p),$$
> > which is exactly the equivariance for the representation $\operatorname{Ad}\circ\rho$ of $G$ on $\operatorname{End}V$, that is, the equivariance characterising sections of $\operatorname{End}E$. So $\rho_*\circ\hat\xi$ is a section of $\operatorname{End}E$; denote it $\rho_*\circ\xi$. Smoothness is clear since $\rho_*$ and $\hat\xi$ are smooth.
> >
> > **It is a Lie-algebra homomorphism.** The bracket on $\Gamma(\operatorname{ad}P)$ is pointwise, $[\xi,\eta](m) = [\hat\xi(p),\hat\eta(p)]_{\mathfrak g}$ read in the frame $p \in P_m$, and likewise on $\Gamma(\operatorname{End}E)$ it is the pointwise commutator. Since $\rho_* : \mathfrak{g} \to \operatorname{End}V$ is a homomorphism of Lie algebras (the differential of a Lie-group homomorphism, $\rho_*[X,Y] = [\rho_*X,\rho_*Y]$), we have pointwise
> > $$\rho_*\circ[\xi,\eta]\,\widehat{}\ = \rho_*\big([\hat\xi,\hat\eta]_{\mathfrak g}\big) = [\rho_*\hat\xi,\ \rho_*\hat\eta] = [\widehat{\rho_*\xi},\ \widehat{\rho_*\eta}],$$
> > so $\xi \mapsto \rho_*\circ\xi$ preserves brackets. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\pi : P \to M$ be a smooth principal $G$-bundle. We prove the three parts in turn, drawing on Lemmas 1–6.
>
> **Step 0 — the objects are defined.** By [[Def - Adjoint Bundles ad P and Ad P]], $\operatorname{Ad}P = P\times_\alpha G$ is a smooth fibre bundle of groups over $M$ with fibrewise product $[p,\gamma]\cdot[p,\gamma'] = [p,\gamma\gamma']$, unit section $m \mapsto [p,e]$, and $\Gamma(\operatorname{Ad}P)$ a group under pointwise multiplication. By [[Def - Gauge Transformation]], $\mathcal{G}(P)$ is a group under composition. These are the source and target of the map to be constructed.
>
> **Part (a).** By **Lemma 1**, the assignment $f \mapsto \hat f$, with $\hat f$ the unique smooth map satisfying $f(p) = p\cdot\hat f(p)$, is a bijection $\mathcal{G}(P) \to C^\infty(P;G)^{\mathrm{conj}}$, where $C^\infty(P;G)^{\mathrm{conj}}$ is the set of smooth $\hat f$ with $\hat f(pg) = g^{-1}\hat f(p)g$. By **Lemma 2**, the map $\Sigma$, $\hat f \mapsto \big(m \mapsto [p,\hat f(p)]\big)$, is a bijection $C^\infty(P;G)^{\mathrm{conj}} \to \Gamma(\operatorname{Ad}P)$. Their composite $\Phi = \Sigma\circ(f\mapsto\hat f) : \mathcal{G}(P) \to \Gamma(\operatorname{Ad}P)$ is therefore a bijection, and by **Lemma 3** it satisfies $\Phi(f_1\circ f_2) = \Phi(f_1)\cdot\Phi(f_2)$, carries $\operatorname{id}_P$ to the unit section, and carries inverses to pointwise inverses. A bijective map of groups that preserves products is an isomorphism of groups. Hence
> $$\mathcal{G}(P) \;\cong\; \Gamma(\operatorname{Ad}P).$$
>
> **Part (b).** By **Lemma 4**, for smooth $g : M \to G$ the map $f(p) = p\cdot g(\pi(p))$ belongs to $\mathcal{G}(P)$ if and only if $g(m) \in Z(G)$ for all $m$; these gauge transformations form the subgroup $C^\infty(M; Z(G)) \le \mathcal{G}(P)$ (it is a subgroup because $\Phi$ carries it to the sections of the sub-bundle with central fibre $M \times Z(G) \hookrightarrow \operatorname{Ad}P$, closed under the pointwise product). When $G$ is abelian, $Z(G) = G$, and the same lemma shows every gauge transformation is of this form and that $\Phi$ restricts to a group isomorphism $\mathcal{G}(P) \cong C^\infty(M;G)$.
>
> **Part (c).** By **Lemma 5**, for $P = \operatorname{Fr}(E)$ the bundle isomorphism $\operatorname{Ad}\operatorname{Fr}(E) \cong \operatorname{Aut}E$ combined with part (a) gives a group isomorphism $\mathcal{G}(\operatorname{Fr}(E)) \cong \Gamma(\operatorname{Aut}E) = \mathcal{G}(E)$, with $f$ and $g$ related by $f(e) = g\circ e$. By **Lemma 6**, for any representation $\rho : G \to GL(V)$ the map $\gamma(f)[p,v] = [f(p),v]$ is a well-defined homomorphism $\gamma : \mathcal{G}(P) \to \mathcal{G}(E)$ with $E = P\times_\rho V$, and $\rho_*$ induces a Lie-algebra homomorphism $\Gamma(\operatorname{ad}P) \to \Gamma(\operatorname{End}E)$, $\xi \mapsto \rho_*\circ\xi$.
>
> All three parts are established. Therefore the gauge group of a principal $G$-bundle is, canonically and as a group, the space of smooth sections of the adjoint group bundle, and this identification is compatible with abelian reduction and with the passage to associated bundles. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The $U(1)$-bundle over the circle and winding number.** For $G = U(1)$ and any principal $U(1)$-bundle $P \to S^1$ (necessarily trivial, as $U(1)$-bundles over $S^1$ are classified by $H^2(S^1) = 0$), part (b) identifies $\mathcal{G}(P) \cong C^\infty(S^1; U(1))$. The theorem applies because $U(1)$ is abelian, so the conjugation ambiguity collapses; the non-obvious payoff is that $\pi_0(\mathcal{G}(P))$ is the group of homotopy classes of maps $S^1 \to U(1)$, computed by the [[Thm - Existence and Properties of the Winding Number|winding number]] to be $\mathbb{Z}$. This is the prototype of the observation that gauge groups have interesting topology, driving the "large gauge transformations" of physics.

**Stabilisers of connections and reducibility.** In a moduli-space context one asks for the stabiliser of a connection $\omega$ inside $\mathcal{G}(P)$. Using the identification, a stabilising gauge transformation is a section $s$ of $\operatorname{Ad}P$ that is covariantly constant for the induced connection on $\operatorname{Ad}P$; over a connected base its value is determined by its value at one point together with the holonomy, so the stabiliser is the centraliser in $G$ of the holonomy group. The theorem applies because it turns the diffeomorphism-level condition $f^*\omega = \omega$ into a fibrewise condition on a section; the result classifies *reducible* connections and is the reason the centre $Z(G)$ (the generic stabiliser) must be quotiented to make the action free.

**Sections of endomorphism bundles as infinitesimal gauge transformations.** In deformation theory one linearises the gauge action: the Lie algebra of $\mathcal{G}(P)$ is $\Gamma(\operatorname{ad}P)$, and part (c) sends it, through a representation $\rho$, into $\Gamma(\operatorname{End}E)$. This appears whenever one writes the gauge-fixing (Coulomb) condition or the deformation complex of an instanton, where the first operator is $\xi \mapsto d^\omega\xi$ from $\Gamma(\operatorname{ad}P)$ to one-forms. The theorem applies because it is what makes "$\Gamma(\operatorname{ad}P)$ is the Lie algebra of the gauge group" a precise statement; the non-obvious content is that the same $\xi$ acts on every associated bundle simultaneously via $\rho_*$.

---

# Bridges

- **From automorphisms to sections.** The construction is the fibre-torsor principle: a fibre $P_m$ is a $G$-torsor, its equivariant self-maps are a copy of $G$ with the identity forgotten, and "$G$ with the identity forgotten, up to the conjugation induced by changing the reference point" is exactly the fibre $(\operatorname{Ad}P)_m$. Running this smoothly over $M$ and reading off the group law gives the isomorphism $\mathcal{G}(P) \cong \Gamma(\operatorname{Ad}P)$; nothing beyond freeness, transitivity, and smoothness of trivialisations enters.

- **The equivariant-function dictionary.** This theorem is the group-bundle instance of the general dictionary "sections of an associated bundle $=$ equivariant functions on the total space", proved for vector bundles on [[Thm - Sections of an Associated Bundle are Equivariant Functions]]. The dictionary is used three times over: for $\operatorname{Ad}P$ (giving $\mathcal{G}(P)$), for $\operatorname{ad}P$ (giving its Lie algebra $\Gamma(\operatorname{ad}P)$), and for $\operatorname{End}E$ (the target of the infinitesimal map). The construction that builds it — send $\hat s$ to $m \mapsto [p,\hat s(p)]$ — is identical in each case; only the fibre ($G$, $\mathfrak{g}$, $\operatorname{End}V$) and the action (conjugation, adjoint, conjugation-through-$\rho$) change.

- **The action on connections.** Once $\mathcal{G}(P) = \Gamma(\operatorname{Ad}P)$, a gauge transformation $g$ acts on a connection by the global intrinsic law $A \mapsto \operatorname{Ad}_{g^{-1}}A + g^*\theta$, the content of [[Thm - Gauge Transformations Act on Connections and Curvature]]; the curvature transforms by conjugation, $F \mapsto \operatorname{Ad}_{g^{-1}}F$. The bridge is that this is the same formula as a change of local trivialisation, now driven by a section rather than a chart, which is why gauge invariance of curvature norms and Chern–Weil forms can be checked over $M$.

- **The kernel of $\gamma$ and reducibility.** The homomorphism $\gamma : \mathcal{G}(P) \to \mathcal{G}(E)$ of part (c) need not be injective. Since $\gamma(f) = \operatorname{id}_E$ holds precisely when $\rho(\hat f(p)) = \operatorname{id}_V$ for every $p \in P$ — that is, when the associated function $\hat f$ takes all its values in the normal subgroup $\ker\rho \le G$ — the kernel is the group of sections of the subbundle of $\operatorname{Ad}P$ with fibre $\ker\rho$, namely $\ker\gamma \cong \Gamma(P \times_\alpha \ker\rho)$. Concretely, for $\rho = \operatorname{Ad}$ of $SU(2)$ one has $\ker(\operatorname{Ad}) = Z(SU(2)) = \{\pm 1\}$, so the centre acts trivially in the adjoint representation and the two constant central sections $\pm 1$ lie in $\ker\gamma$. This is worked out in [[Ex - The Gauge Group Homomorphism from a Representation and its Infinitesimal Version|the representation-homomorphism exercise]] and is the algebraic origin of the $\mathbb{Z}/2$ ambiguities in $SO(3)$ versus $SU(2)$ gauge theory.

---

# Unlocked by This

> [!tip] The gauge group as an infinite-dimensional Lie group *(from Global Analysis)*
> Because $\mathcal{G}(P) \cong \Gamma(\operatorname{Ad}P)$ and, when $G$ is a matrix group and $M$ is compact, $\operatorname{Ad}P$ embeds in $\operatorname{End}E$, the gauge group inherits the structure of a Banach (or Fréchet) Lie group with Lie algebra $\Gamma(\operatorname{ad}P)$. See [[Ex - The C^k Gauge Group of a Matrix Group Bundle is a Banach Lie Group]].

> [!tip] Abelian gauge transformations and winding *(from Algebraic Topology)*
> For abelian $G$ the identification $\mathcal{G}(P) \cong C^\infty(M;G)$ makes the connected components of the gauge group a homotopy invariant of $M$; for $G = U(1)$ over $S^1$ they are counted by the winding number. See [[Ex - Gauge Transformations of an Abelian Bundle are Maps to the Group]].
