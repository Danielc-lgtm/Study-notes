---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Principal G-Bundle"
  - "Def - Frame Bundle of a Vector Bundle"
  - "Def - Reduction and Extension of the Structure Group"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $G$ is a [[Def - Representation of a Lie Group|Lie group]] with identity $e \in G$, multiplication $\mu_G : G \times G \to G$ and (smooth) inversion $g \mapsto g^{-1}$, and $\pi : P \to M$ is a **[[Def - Principal G-Bundle|principal $G$-bundle]]** over a smooth manifold $M$. We use the standing convention of the series that $G$ acts on $P$ **on the right**; the action is written $(p, g) \mapsto p \cdot g$, and $R_g : P \to P$, $R_g(p) = p \cdot g$, denotes the diffeomorphism given by acting with a fixed $g$. The fibre over $m \in M$ is $P_m := \pi^{-1}(m)$, and for an open set $U \subseteq M$ we abbreviate $P|_U := \pi^{-1}(U)$.

A principal $G$-bundle carries, by definition, three properties beyond being a [[Def - Fibre Bundle|fibre bundle]]: the right $G$-action is **free** (if $p \cdot g = p$ for some $p$ then $g = e$), it is **transitive on each fibre** (for every $p \in P$ we have $p \cdot G = P_{\pi(p)}$), and $P$ admits **$G$-equivariant local trivialisations**. We recall the last property because both this page and its proof turn on its exact form.

> [!warning] Convention: two equivalent forms of "equivariant local trivialisation"
> Haydys states equivariance pointwise (Definition 23(iv)): a local trivialisation over $U$ is a diffeomorphism $\psi_U : P|_U \to U \times G$ with $\operatorname{pr}_1 \circ \psi_U = \pi$ and
> $$\psi_U(p \cdot g) = \psi_U(p) \cdot g \qquad \text{for all } p \in P|_U,\ g \in G,$$
> where $G$ acts on $U \times G$ by right multiplication on the second factor, $(u, h) \cdot g = (u, hg)$.
>
> Bär states equivariance (Definition 2.2.1(iii)) by the commuting square asserting $\psi_U \circ R_g = (\operatorname{id}_U \times \mu_G(\,\cdot\,, g)) \circ \psi_U$. These are the same condition: evaluating Bär's square at $p$ gives $\psi_U(p \cdot g) = (\pi(p), \operatorname{pr}_2\psi_U(p)\cdot g) = \psi_U(p) \cdot g$, and conversely Haydys' identity reassembles the square. We use the pointwise form throughout, calling any such $\psi_U$ an **equivariant local trivialisation over $U$**.

A **smooth local section over $U$** is a smooth map $s : U \to P|_U$ with $\pi \circ s = \operatorname{id}_U$; equivalently, $s(u) \in P_u$ for every $u \in U$. When $U = M$ we call $s$ a **global section**. Because the equivariance of $\psi_U$ forces $\psi_U^{-1}$ to be equivariant as well — for $(u, h) \in U \times G$ and $g \in G$, setting $p := \psi_U^{-1}(u, h)$ gives $\psi_U(p \cdot g) = \psi_U(p)\cdot g = (u, hg)$, hence
$$\psi_U^{-1}(u, hg) = \psi_U^{-1}(u, h) \cdot g \qquad (\star)$$
— the identity $(\star)$ is available whenever an equivariant trivialisation is in hand, and it does much of the work below.

For a real [[Def - Vector Bundle|vector bundle]] $E \to M$ of rank $k$, its **[[Def - Frame Bundle of a Vector Bundle|frame bundle]]** $\operatorname{Fr}(E) = \bigsqcup_{m \in M} \operatorname{Fr}(E_m)$ is the principal $GL_k(\mathbb{R})$-bundle whose fibre over $m$ is the set of linear isomorphisms $e : \mathbb{R}^k \to E_m$ (equivalently, ordered bases of $E_m$), with the right action $e \cdot h := e \circ h$ for $h \in GL_k(\mathbb{R})$. We write $\varepsilon_1, \dots, \varepsilon_k$ for the standard basis of $\mathbb{R}^k$. A **[[Def - Local Frame|local frame]]** of $E$ over $U$ is a $k$-tuple $(e_1, \dots, e_k)$ of smooth [[Def - Section of a Vector Bundle|sections]] of $E$ over $U$ that is a basis of $E_m$ at every $m \in U$; assembling the tuple into the isomorphism $x \mapsto \sum_j x_j e_j(m)$ identifies local frames of $E$ over $U$ with sections of $\operatorname{Fr}(E)$ over $U$.

For a Lie group homomorphism $\varphi : G \to H$ and a principal $G$-bundle $P$, the **[[Def - Reduction and Extension of the Structure Group|extension of the structure group]]** is the principal $H$-bundle
$$P \times_\varphi H := (P \times H)/G, \qquad (p, h) \cdot g := (p \cdot g,\ \varphi(g)^{-1} h),$$
with right $H$-action $[p, h] \cdot h' := [p, h h']$; a principal $G$-bundle $P$ with $P \times_\varphi H \cong Q$ is called a **reduction of $Q$ to $G$**. We use these only in part (iv), and restate exactly what we need there.

$\cong$ denotes isomorphism of bundles over the identity of the base (a fibre-preserving diffeomorphism that is $G$-equivariant, for principal bundles; a fibrewise-linear diffeomorphism, for vector bundles); $M \times G$ and $M \times \mathbb{R}^k$ denote the **trivial** principal and vector bundles, with projection to the first factor, and a bundle isomorphic to a trivial one is called **trivial**.

---

# Statement

> **Theorem (Sections and triviality of a principal bundle).** Let $\pi : P \to M$ be a principal $G$-bundle and $U \subseteq M$ open.
>
> **(i) Local trivialisations correspond to local sections.** The assignment
> $$\Phi : \{\text{equivariant local trivialisations over } U\} \longrightarrow \{\text{smooth local sections over } U\}, \qquad \psi_U \longmapsto s := \psi_U^{-1}(\,\cdot\,, e)$$
> is a bijection. Its inverse sends a smooth section $s$ over $U$ to the trivialisation $\psi_U(p) := (\pi(p), g(p))$, where $g(p) \in G$ is the unique element with $p = s(\pi(p)) \cdot g(p)$; equivalently $\psi_U^{-1}(u, g) = s(u) \cdot g$.
>
> **(ii) Global triviality.** $P$ is trivial if and only if it admits a global section.
>
> **(iii) Triviality of a vector bundle.** A vector bundle $E \to M$ is trivial if and only if its frame bundle $\operatorname{Fr}(E)$ admits a global section.
>
> **(iv) Reduction to the trivial group.** A principal $H$-bundle $Q \to M$ admits a reduction to the trivial group $\{e\} \leq H$ if and only if $Q$ is trivial.

The bijection in (i) is natural in $U$: it commutes with restriction to a smaller open set. Parts (ii)–(iv) are the three global corollaries drawn from it; each is proved from (i) below, not merely asserted.

---

# Motivation

A principal bundle is defined by an atlas of local trivialisations, and the axiom that they can be chosen equivariantly is the whole difference between a principal bundle and an arbitrary fibre bundle whose fibre happens to be $G$. But a trivialisation $\psi_U : P|_U \to U \times G$ is an unwieldy object to produce and to reason with: it is a diffeomorphism of total spaces, subject to a compatibility square. This theorem replaces it, over any fixed $U$, by something far more elementary — a single smooth map $s : U \to P$ that lands in the right fibres. The content is that no information is lost in the trade: an equivariant trivialisation and a section carry exactly the same data.

The reason this is the organising theorem of the whole local theory is that everything downstream is phrased in terms of sections rather than trivialisations. [[Def - Transition Functions and the Cocycle Condition|Transition functions]] are defined by comparing two local sections, $s_\beta = s_\alpha \cdot g_{\alpha\beta}$; a [[Def - Connections on Principal Bundles|connection]] is pulled back to the base by a section, $A_s = s^* \omega$; a gauge transformation acts by changing the section. Each of these would be clumsy to write with trivialisations and is clean with sections, and the licence to pass between the two pictures at will is precisely this correspondence. In physics language — recorded on the definition page — a local section is a choice of local gauge, "a system of units in each fibre", and the theorem says that trivialising the bundle over a region and choosing a gauge on that region are the same act.

The global corollaries are the payoff. Whether a bundle is trivial is one of the first questions one asks of it, and part (ii) converts that question from "does a global trivialisation exist?" — a statement about maps of manifolds — into "does a global section exist?" — a statement one can attack with the tools of differential topology, obstruction theory, and characteristic classes. The very first nontrivial example, the [[Def - The Hopf Bundle|Hopf bundle]] $S^3 \to S^2$, is proved nontrivial in exactly this way: one shows it has no global section (see [[Thm - The Hopf Bundle is Nontrivial|the nontriviality theorem]]). Part (iii) specialises the criterion to frame bundles, where a global section is a global frame, so that a vector bundle is trivial precisely when it is parallelisable in the naive sense of admitting $k$ everywhere-independent sections.

---

# Sources and Targets

**Sources (Input Broadening).** The literal hypothesis of part (i) is only "$P$ is a principal $G$-bundle and $U$ is open", so the useful question is which problems secretly hand you a principal bundle with a section, or a section to build.

A first disguised source is **a Lie group quotient $G \to G/H$**. Whenever a homogeneous space appears — $S^2 = SO(3)/SO(2)$, $\mathbb{CP}^n = U(n+1)/(U(1)\times U(n))$, a flag manifold — the projection $G \to G/H$ is a principal $H$-bundle by [[Thm - Homogeneous Space is a Smooth Manifold|the homogeneous-space theorem]], and a smooth local section of it is a smooth local slice for the $H$-action. The bridge is that "$X = G/H$" is not a bare diffeomorphism statement but a principal-bundle statement, so this theorem applies to it; the non-obvious part is recognising the bundle at all. *Example problem:* to build a local trivialisation of the tangent-frame bundle of $S^2$ near the north pole, exhibit instead a smooth local section — a smooth choice of oriented orthonormal frame — and let part (i) manufacture the trivialisation.

A second disguised source is **a vector bundle with a nowhere-vanishing frame or a partial frame**. A rank-$k$ bundle $E$ carrying $k$ pointwise-independent global sections is, by part (iii), trivial; a bundle carrying a nowhere-vanishing section reduces its structure group. The bridge is that independent sections of $E$ assemble into a section of $\operatorname{Fr}(E)$, an object this theorem reads. The non-obviousness is that a *linear-algebra* datum on $E$ (independence at each point) becomes a *topological* datum on the frame bundle (a global section). *Example problem:* deduce that the tangent bundle of a Lie group is trivial by producing the global frame of left-invariant fields, hence a global section of $\operatorname{Fr}(TG)$.

A third disguised source is **an obstruction that forbids a section**, read in the contrapositive. Any theorem asserting the nonexistence of a global section — the hairy-ball theorem for $TS^2$, a nonzero characteristic number, a nontrivial homotopy class of a clutching map — becomes, through parts (ii)–(iii), a proof of nontriviality of the associated principal or vector bundle. The bridge is that "no section" and "nontrivial" are interchangeable here. *Example problem:* the hairy-ball theorem gives no nowhere-vanishing vector field on $S^2$, but that alone does not prove $\operatorname{Fr}(TS^2)$ has no section; the full $TS^2$ nonexistence statement (placed in §3.5) does, and part (iii) then reads off that $TS^2$ is nontrivial.

**Targets (Output Amplification).** The bare output of (i) is a bijection of two sets over each $U$.

Combine (i) with **a good open cover of $M$**. Every point has a neighbourhood over which $P$ trivialises, hence over which $P$ has a section; choosing sections $s_\alpha$ over a cover $\{U_\alpha\}$ and comparing them on overlaps produces the transition cocycle $g_{\alpha\beta}$ with $s_\beta = s_\alpha g_{\alpha\beta}$. The extra ingredient is the cover; the payoff is the entire [[Thm - Principal Bundles are Classified by Cocycles|cocycle description]] of the bundle, and with it the classification of principal bundles up to isomorphism.

Combine (ii) with **de Rham cohomology or homotopy of the total space**. If a global section existed then $P \cong M \times G$, and any cohomological or homotopical invariant of $P$ would equal that of the product. A single invariant that distinguishes $P$ from $M \times G$ — for instance $H^1_{\mathrm{dR}}(S^{2n+1}) = 0$ against $H^1_{\mathrm{dR}}(\mathbb{CP}^n \times S^1) \neq 0$ — then rules out the section and proves nontriviality. The extra ingredient is the invariant; the payoff is a nonexistence proof reachable by computation.

Combine (iii) with **Chern–Weil theory**. A nonzero characteristic number of a vector bundle $E$ certifies that $\operatorname{Fr}(E)$ has no global section, because a section would trivialise $E$ and force all its characteristic classes to vanish. The extra ingredient is the characteristic class; the payoff is a numerical, computable obstruction to the existence of a global frame — the modern replacement for ad hoc nonexistence arguments.

---

# Why Is It True

Strip away the manifold structure and look at one fibre $P_m$. It is a set on which $G$ acts freely and transitively — a *torsor*. Such a set is a copy of $G$ that has forgotten where its identity element is: any two points differ by a unique group element, but no point is distinguished. To coordinatise $P_m$ by $G$ you must first *choose* a point to call the identity. That single choice, made smoothly over $U$, is exactly a section $s$: it nominates $s(m) \in P_m$ as the origin. Once the origin is fixed, freeness and transitivity do the rest — every other $p \in P_m$ is $s(m) \cdot g$ for one and only one $g$, so the fibre is now labelled by $G$, and running the labelling over all of $U$ is the trivialisation. Conversely a trivialisation has already nominated an origin in each fibre, namely the preimage of the identity, and that is the section it corresponds to.

> **Mechanism.** A section picks the identity element in each fibre; freeness and transitivity then coordinatise the fibre by $G$, turning the torsor $P_m$ into a labelled copy of $G$ — and a trivialisation is nothing but such a labelling, so the two are the same choice viewed twice.

This also explains why the global statements read the way they do. A global section is an origin chosen coherently over *all* of $M$, and a global coherent origin is precisely what a trivial bundle has and a nontrivial one lacks. The obstruction to triviality is therefore an obstruction to choosing an origin globally — a genuinely topological quantity, since locally the choice is always possible (that is the trivialisation axiom) and only the gluing can fail. For the frame bundle the origin-in-each-fibre is a basis of each fibre chosen smoothly, that is a global frame, so a vector bundle is trivial exactly when its fibres can be based coherently.

---

# What Makes This Hard

The one step that is not a formality is the **smoothness of the coordinate map $g(p)$** in the section-to-trivialisation direction. Its existence and uniqueness come free from freeness and transitivity, and Bär's text calls the resulting section "obviously smooth", but the smoothness of $p \mapsto g(p)$ is not obvious: $g(p)$ is defined implicitly by the equation $p = s(\pi(p)) \cdot g(p)$, and one must exhibit it as a composition of smooth maps to be sure. The device — used below — is to bring in an *a priori* equivariant trivialisation $\phi$ that exists near each point by the bundle axiom, and to solve the equation inside $\phi$'s coordinates, where it becomes $g(p) = \sigma(\pi(p))^{-1}\tau(p)$ with $\sigma, \tau$ manifestly smooth and group inversion and multiplication smooth. The common error is to skip this and declare $g(p)$ smooth because it is "unique", conflating uniqueness with regularity. A second, milder trap is to forget to check that the constructed $\psi_U$ is equivariant and a diffeomorphism, not merely a fibrewise bijection.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Prove part (i) as a genuine bijection by writing down both maps explicitly and checking each is well-defined and that they invert one another; the forward map uses only the equivariance identity $(\star)$, the backward map uses freeness, transitivity, and one auxiliary trivialisation for smoothness. Then read off (ii) by taking $U = M$, (iii) by identifying a section of $\operatorname{Fr}(E)$ with a global frame and a global frame with a trivialisation of $E$, and (iv) by unwinding what a reduction to $\{e\}$ is.

**Subgoal decomposition:**

1. **Forward map is well-defined.** Given an equivariant trivialisation $\psi_U$, show $s := \psi_U^{-1}(\cdot, e)$ is a smooth section and that $\psi_U^{-1}(u, g) = s(u) \cdot g$.
   - *Hint:* $\pi = \operatorname{pr}_1 \circ \psi_U$ gives the section property; the identity $(\star)$ with $h = e$ gives the formula.
   - *Why needed:* It defines $\Phi$ and produces the key formula that both directions reuse.

2. **Backward map is well-defined: existence and uniqueness of $g(p)$.** Given a smooth section $s$, show that for each $p \in P|_U$ there is a unique $g(p) \in G$ with $p = s(\pi(p)) \cdot g(p)$.
   - *Hint:* $s(\pi(p))$ and $p$ lie in the same fibre; transitivity gives existence, freeness gives uniqueness.
   - *Why needed:* Without $g(p)$ there is no candidate inverse map.

3. **Backward map is smooth.** Show $p \mapsto g(p)$ is smooth.
   - *Hint:* Fix an a-priori equivariant trivialisation $\phi$ near a point; write $s$ and $p$ in $\phi$-coordinates and solve for $g(p)$ using equivariance of $\phi$.
   - *Why needed:* Smoothness makes $\psi_U(p) = (\pi(p), g(p))$ a diffeomorphism, not just a bijection.

4. **Backward output is an equivariant trivialisation.** Show $\psi_U(p) = (\pi(p), g(p))$ is $G$-equivariant, commutes with $\pi$, and is a diffeomorphism with inverse $(u, g) \mapsto s(u) \cdot g$.
   - *Hint:* $g(p \cdot g') = g(p) g'$ by uniqueness; both $\psi_U$ and its inverse are compositions of smooth maps.
   - *Why needed:* The backward map must land in the correct set.

5. **The two maps are mutually inverse.** Show $\Phi$ followed by the backward map is the identity on trivialisations, and vice versa.
   - *Hint:* Use the formula $\psi_U^{-1}(u, g) = s(u) g$ in one direction; evaluate at $g = e$ in the other.
   - *Why needed:* It upgrades "two maps between two sets" to "bijection".

6. **Global corollaries.** Set $U = M$ for (ii); identify frame-bundle sections with global frames and global frames with vector-bundle trivialisations for (iii); unwind the extension along $\{e\} \hookrightarrow H$ for (iv).
   - *Hint:* An $\{e\}$-principal bundle projects diffeomorphically to $M$, and its $H$-extension is $M \times H$.
   - *Why needed:* These are the statements actually used elsewhere in the chapter.

---

# Lemma Decomposition

> [!note]- Lemma 1: An equivariant trivialisation yields a smooth section and the formula $\psi_U^{-1}(u, g) = s(u)\cdot g$
> **Statement:** Let $\psi_U : P|_U \to U \times G$ be an equivariant local trivialisation, and set $s(u) := \psi_U^{-1}(u, e)$. Then $s : U \to P|_U$ is a smooth section, and for all $(u, g) \in U \times G$,
> $$\psi_U^{-1}(u, g) = s(u) \cdot g.$$
>
> **Hint:** The section property is $\pi \circ s = \operatorname{id}_U$, which follows from $\operatorname{pr}_1 \circ \psi_U = \pi$; the formula is the equivariance identity $(\star)$ with $h = e$.
>
> **Why needed:** It constructs the forward map $\Phi$ and supplies the identity that both directions of the bijection reuse.
>
> > [!note]- Full proof
> > **$s$ is smooth.** The map $u \mapsto (u, e)$ from $U$ to $U \times G$ is smooth (it is $\operatorname{id}_U$ paired with the constant map at $e$), and $\psi_U^{-1} : U \times G \to P|_U$ is smooth because $\psi_U$ is a diffeomorphism (part of being a trivialisation). Hence $s = \psi_U^{-1}(\,\cdot\,, e)$ is smooth as a composition of smooth maps.
> >
> > **$s$ is a section.** By the defining property $\operatorname{pr}_1 \circ \psi_U = \pi$ of a trivialisation, we also have $\operatorname{pr}_1 = \pi \circ \psi_U^{-1}$ (apply the first identity to $\psi_U^{-1}(u,h)$). Therefore, for $u \in U$,
> > $$\pi(s(u)) = \pi(\psi_U^{-1}(u, e)) = \operatorname{pr}_1(u, e) = u \qquad (\text{since } \operatorname{pr}_1 = \pi \circ \psi_U^{-1}),$$
> > so $\pi \circ s = \operatorname{id}_U$; and $s(u) \in P_u = \pi^{-1}(u)$, so $s$ is a section over $U$.
> >
> > **The formula.** Apply the equivariance identity $(\star)$ — proved in the Notation section from $\psi_U(p\cdot g) = \psi_U(p)\cdot g$ — with $h = e$:
> > $$\psi_U^{-1}(u, g) = \psi_U^{-1}(u, e g) = \psi_U^{-1}(u, e) \cdot g = s(u) \cdot g \qquad (\text{by } (\star)\text{ with } h = e,\ \text{and } eg = g). \qquad \blacksquare$$

> [!note]- Lemma 2: A smooth section yields a unique fibre coordinate $g(p)$, and it is smooth
> **Statement:** Let $s : U \to P|_U$ be a smooth section. For each $p \in P|_U$ there is a unique $g(p) \in G$ with
> $$p = s(\pi(p)) \cdot g(p),$$
> and the map $g : P|_U \to G$, $p \mapsto g(p)$, is smooth.
>
> **Hint:** Existence and uniqueness come from transitivity and freeness of the $G$-action on the fibre $P_{\pi(p)}$; smoothness is obtained by solving the defining equation inside an auxiliary equivariant trivialisation that exists near each point.
>
> **Why needed:** It constructs the fibre coordinate that defines the backward trivialisation, and secures the smoothness that "obvious" arguments skip.
>
> > [!note]- Full proof
> > **Existence.** Fix $p \in P|_U$ and set $m := \pi(p)$. Since $s$ is a section, $s(m) \in P_m$, and $p \in P_m$ as well. By **transitivity of the $G$-action on the fibre** $P_m$ (a defining property of a principal bundle), $p \cdot G = P_m \ni s(m)$; equivalently $s(m) \cdot G = P_m \ni p$, so there exists $g \in G$ with $p = s(m)\cdot g$.
> >
> > **Uniqueness.** Suppose $p = s(m)\cdot g = s(m)\cdot g'$ with $g, g' \in G$. Acting on the right by $g^{-1}$ and using that the action is an action, $s(m) = s(m) \cdot (g' g^{-1})$. By **freeness of the $G$-action** ($q \cdot h = q \Rightarrow h = e$, applied to $q = s(m)$, $h = g' g^{-1}$), we get $g' g^{-1} = e$, hence $g' = g$. So $g(p) := g$ is well-defined.
> >
> > **Smoothness.** Let $p_0 \in P|_U$ and $m_0 := \pi(p_0)$. By the trivialisation axiom for the principal bundle $P$, there is an open $V \subseteq M$ with $m_0 \in V$ and an equivariant local trivialisation $\phi : P|_V \to V \times G$; shrinking $V$ we may assume $V \subseteq U$. Define the two smooth maps
> > $$\sigma : V \to G, \quad \sigma := \operatorname{pr}_2 \circ \phi \circ s|_V, \qquad\qquad \tau : P|_V \to G, \quad \tau := \operatorname{pr}_2 \circ \phi.$$
> > Both are smooth: $s|_V$, $\phi$, and $\operatorname{pr}_2$ are smooth. Now for $p \in P|_V$, apply $\phi$ to the defining equation $p = s(\pi(p)) \cdot g(p)$ and use equivariance of $\phi$:
> > $$\phi(p) = \phi\big(s(\pi(p)) \cdot g(p)\big) = \phi(s(\pi(p))) \cdot g(p) \qquad (\text{by equivariance } \phi(q \cdot g) = \phi(q)\cdot g).$$
> > Reading the second $G$-component of this identity, and writing $m = \pi(p)$,
> > $$\tau(p) = \operatorname{pr}_2\phi(p) = \operatorname{pr}_2\big(\phi(s(m)) \cdot g(p)\big) = \big(\operatorname{pr}_2 \phi(s(m))\big)\cdot g(p) = \sigma(m)\cdot g(p) \qquad (\text{the action on } V \times G \text{ is right mult.\ on } G),$$
> > since $\phi(s(m)) = (m, \sigma(m))$ (as $\operatorname{pr}_1\phi = \pi$ and $\pi(s(m)) = m$). Solving,
> > $$g(p) = \sigma(\pi(p))^{-1}\, \tau(p) \qquad (\text{multiply on the left by } \sigma(\pi(p))^{-1}).$$
> > The right-hand side is smooth in $p$: it is the composite of $p \mapsto (\sigma(\pi(p)), \tau(p))$ — smooth, as $\pi$, $\sigma$, $\tau$ are smooth — with the group operations $(a, b) \mapsto a^{-1} b$, which are smooth because inversion and multiplication in a Lie group are smooth. Hence $g$ is smooth on the neighbourhood $P|_V$ of $p_0$. As $p_0 \in P|_U$ was arbitrary, $g$ is smooth on $P|_U$. $\blacksquare$

> [!note]- Lemma 3: The backward datum is an equivariant trivialisation with inverse $(u,g)\mapsto s(u)\cdot g$
> **Statement:** With $s$ and $g$ as in Lemma 2, the map $\psi_U : P|_U \to U \times G$, $\psi_U(p) := (\pi(p), g(p))$, is a $G$-equivariant local trivialisation; $\operatorname{pr}_1 \circ \psi_U = \pi$, its inverse is $\psi_U^{-1}(u, g) = s(u)\cdot g$, and its associated section $\psi_U^{-1}(\,\cdot\,, e)$ is $s$.
>
> **Hint:** Equivariance is $g(p\cdot g') = g(p) g'$, from the uniqueness in Lemma 2; the inverse is the smooth map $(u, g)\mapsto s(u)g$, and one checks the two compositions are identities.
>
> **Why needed:** It shows the backward map lands in the set of equivariant trivialisations and identifies its inverse explicitly, completing the description of $\Phi^{-1}$.
>
> > [!note]- Full proof
> > **$\psi_U$ commutes with $\pi$ and is smooth.** By construction $\operatorname{pr}_1(\psi_U(p)) = \pi(p)$, so $\operatorname{pr}_1 \circ \psi_U = \pi$. Both components of $\psi_U$ are smooth ($\pi$ is smooth; $g$ is smooth by Lemma 2), so $\psi_U$ is smooth.
> >
> > **The candidate inverse.** Define $\theta : U \times G \to P|_U$, $\theta(u, g) := s(u)\cdot g$. It is smooth, being the composite of $(u, g)\mapsto (s(u), g)$ (smooth, as $s$ is smooth) with the smooth action map $P \times G \to P$; and it maps into $P|_U$ because $\pi(s(u)\cdot g) = \pi(s(u)) = u \in U$ (the action preserves fibres).
> >
> > **$\theta$ and $\psi_U$ are mutually inverse.** For $(u, g) \in U \times G$, the point $q := \theta(u, g) = s(u)\cdot g$ has $\pi(q) = u$, and by the uniqueness clause of Lemma 2 its coordinate is $g(q) = g$ (indeed $q = s(u)\cdot g = s(\pi(q))\cdot g$, and $g(q)$ is the unique such element). Hence
> > $$\psi_U(\theta(u, g)) = (\pi(q), g(q)) = (u, g),$$
> > so $\psi_U \circ \theta = \operatorname{id}_{U\times G}$. Conversely, for $p \in P|_U$,
> > $$\theta(\psi_U(p)) = \theta(\pi(p), g(p)) = s(\pi(p))\cdot g(p) = p \qquad (\text{by the defining equation of } g(p) \text{ in Lemma 2}),$$
> > so $\theta \circ \psi_U = \operatorname{id}_{P|_U}$. Thus $\psi_U$ is a diffeomorphism with $\psi_U^{-1} = \theta$, i.e. $\psi_U^{-1}(u, g) = s(u)\cdot g$.
> >
> > **Equivariance.** For $p \in P|_U$ and $g' \in G$, first note $\pi(p\cdot g') = \pi(p)$ (the action preserves fibres). Now
> > $$p \cdot g' = \big(s(\pi(p))\cdot g(p)\big)\cdot g' = s(\pi(p))\cdot(g(p) g') \qquad (\text{by the defining equation of } g(p)\text{, and associativity of the action}),$$
> > and $\pi(p\cdot g') = \pi(p) = \pi\big(s(\pi(p))\big)$, so $s(\pi(p\cdot g')) = s(\pi(p))$. By the uniqueness clause of Lemma 2 applied to $p\cdot g'$, its coordinate is therefore $g(p\cdot g') = g(p) g'$. Hence
> > $$\psi_U(p\cdot g') = (\pi(p\cdot g'),\, g(p\cdot g')) = (\pi(p),\, g(p) g') = (\pi(p), g(p))\cdot g' = \psi_U(p)\cdot g',$$
> > which is exactly $G$-equivariance. So $\psi_U$ is an equivariant local trivialisation.
> >
> > **Its section is $s$.** By the formula just proved, $\psi_U^{-1}(u, e) = s(u)\cdot e = s(u)$, so the section associated to $\psi_U$ by Lemma 1 is $s$ itself. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $\pi : P \to M$ be a principal $G$-bundle and $U \subseteq M$ open. Write
> $$\mathcal{T}_U := \{\text{equivariant local trivialisations of } P \text{ over } U\}, \qquad \mathcal{S}_U := \{\text{smooth sections of } P \text{ over } U\}.$$
>
> **Part (i) — the bijection.**
>
> *Step 0 — the two maps are defined.* By Lemma 1, the assignment $\Phi : \mathcal{T}_U \to \mathcal{S}_U$, $\Phi(\psi_U) := \psi_U^{-1}(\,\cdot\,, e)$, sends each equivariant trivialisation to a genuine smooth section, so $\Phi$ maps into $\mathcal{S}_U$. By Lemmas 2 and 3, the assignment $\Psi : \mathcal{S}_U \to \mathcal{T}_U$, $\Psi(s) := \big(p \mapsto (\pi(p), g(p))\big)$ with $g(p)$ the unique element satisfying $p = s(\pi(p))\cdot g(p)$, sends each smooth section to a genuine equivariant trivialisation, so $\Psi$ maps into $\mathcal{T}_U$.
>
> *Step 1 — $\Phi \circ \Psi = \operatorname{id}_{\mathcal{S}_U}$.* Let $s \in \mathcal{S}_U$ and put $\psi_U := \Psi(s)$. By the last clause of Lemma 3, the section associated to $\psi_U$ is $\psi_U^{-1}(\,\cdot\,, e) = s$. Hence $\Phi(\Psi(s)) = s$.
>
> *Step 2 — $\Psi \circ \Phi = \operatorname{id}_{\mathcal{T}_U}$.* Let $\psi_U \in \mathcal{T}_U$ and put $s := \Phi(\psi_U) = \psi_U^{-1}(\,\cdot\,, e)$. We must show $\Psi(s) = \psi_U$. Fix $p \in P|_U$ and let $g(p)$ be the unique element with $p = s(\pi(p))\cdot g(p)$ (Lemma 2). By Lemma 1, $s(u)\cdot g = \psi_U^{-1}(u, g)$ for all $u, g$, so
> $$p = s(\pi(p))\cdot g(p) = \psi_U^{-1}(\pi(p),\, g(p)) \qquad (\text{by the formula of Lemma 1}).$$
> Applying $\psi_U$ and using $\operatorname{pr}_1\psi_U = \pi$ gives $\psi_U(p) = (\pi(p), g(p)) = \Psi(s)(p)$. As $p$ was arbitrary, $\Psi(\Phi(\psi_U)) = \psi_U$.
>
> Steps 1 and 2 show $\Phi$ and $\Psi$ are mutually inverse, so $\Phi$ is a bijection with inverse $\Psi$. *Naturality in $U$:* if $U' \subseteq U$ is open, then restricting a trivialisation over $U$ to $P|_{U'}$ and restricting its section to $U'$ commute, because both $\Phi$ and $\Psi$ are defined pointwise in $p$ and $u$ and their formulas ($\psi_U^{-1}(\cdot, e)$; $p \mapsto (\pi(p), g(p))$) are unchanged by shrinking the domain. This proves (i).
>
> **Part (ii) — global triviality.** Take $U = M$.
>
> ($\Rightarrow$) Suppose $P$ is trivial, i.e. there is an equivariant global trivialisation $\psi_M : P \to M \times G$. Then $s := \Phi(\psi_M) = \psi_M^{-1}(\,\cdot\,, e)$ is a global section by Lemma 1.
>
> ($\Leftarrow$) Suppose $P$ admits a global section $s : M \to P$. Then $\psi_M := \Psi(s)$ is, by Lemma 3, an equivariant trivialisation over all of $M$, that is, an isomorphism $P \cong M \times G$ of principal bundles. Hence $P$ is trivial. This proves (ii).
>
> **Part (iii) — triviality of a vector bundle.** Let $E \to M$ be a vector bundle of rank $k$, with frame bundle $\operatorname{Fr}(E)$, a principal $GL_k(\mathbb{R})$-bundle. We use the identification, recalled in the Notation section, between sections of $\operatorname{Fr}(E)$ over an open set and local frames of $E$ there: a section $e$ of $\operatorname{Fr}(E)$ assigns to each $m$ an isomorphism $e(m) : \mathbb{R}^k \to E_m$, and the $k$ smooth sections $e_j(m) := e(m)\varepsilon_j$ of $E$ form a basis of $E_m$ at each point, i.e. a local frame; conversely a local frame $(e_1, \dots, e_k)$ defines the section $e(m) : x \mapsto \sum_j x_j e_j(m)$ of $\operatorname{Fr}(E)$.
>
> ($\Leftarrow$) Suppose $\operatorname{Fr}(E)$ admits a global section $e$, equivalently a global frame $(e_1, \dots, e_k)$ of $E$. Define
> $$\Theta : M \times \mathbb{R}^k \to E, \qquad \Theta(m, x) := \sum_{j=1}^{k} x_j\, e_j(m) = e(m)\, x.$$
> This is smooth (the $e_j$ are smooth sections and the sum is a smooth fibrewise operation), fibre-preserving, and on each fibre it is the linear isomorphism $e(m) : \mathbb{R}^k \to E_m$ (a frame is by definition an isomorphism). A smooth fibrewise-linear bijection with smooth fibrewise-linear inverse is a vector-bundle isomorphism — the inverse $\Theta^{-1}(v) = (\pi_E(v), e(\pi_E(v))^{-1} v)$ is smooth because $m \mapsto e(m)^{-1}$ is smooth (inversion of a smoothly varying invertible matrix, in any local trivialisation of $E$ where $e$ is a smooth $GL_k$-valued function). Hence $\Theta : M \times \mathbb{R}^k \cong E$, and $E$ is trivial.
>
> ($\Rightarrow$) Suppose $E$ is trivial, with a vector-bundle isomorphism $\Theta : M \times \mathbb{R}^k \cong E$. Then $e_j(m) := \Theta(m, \varepsilon_j)$ are smooth sections of $E$, and at each $m$ the vectors $e_1(m), \dots, e_k(m)$ are the images under the linear isomorphism $\Theta(m, \cdot)$ of the basis $\varepsilon_1, \dots, \varepsilon_k$, hence a basis of $E_m$. So $(e_1, \dots, e_k)$ is a global frame, i.e. a global section of $\operatorname{Fr}(E)$. This proves (iii).
>
> **Part (iv) — reduction to the trivial group.** Let $Q \to M$ be a principal $H$-bundle, and let $\iota : \{e\} \hookrightarrow H$ be the inclusion of the trivial subgroup. Recall (Notation, and the definition page [[Def - Reduction and Extension of the Structure Group|Reduction and Extension of the Structure Group]]) that a *reduction of $Q$ to $\{e\}$* is a principal $\{e\}$-bundle $P \to M$ together with an isomorphism $P \times_\iota H \cong Q$, where $P \times_\iota H = (P \times H)/\{e\}$ with the $\{e\}$-action trivial.
>
> *Step 0 — an $\{e\}$-principal bundle is $M$ itself.* A principal $\{e\}$-bundle $P \to M$ has structure group the one-point group; its fibres are single points (the $\{e\}$-action is free and transitive on each fibre, and a set with a free transitive action of $\{e\}$ has exactly one element). Its equivariant local trivialisations are diffeomorphisms $P|_V \cong V \times \{e\} \cong V$ commuting with the projections, so $\pi_P : P \to M$ is a local diffeomorphism that is bijective, hence a diffeomorphism. Thus $P \cong M$ canonically via $\pi_P$, and every principal $\{e\}$-bundle over $M$ is (isomorphic to) $M$ with identity projection.
>
> *Step 0 — its $H$-extension is the trivial bundle.* Since the $\{e\}$-action on $P \times H$ is trivial, the quotient is $P \times_\iota H = P \times H$, with $H$ acting on the second factor and projecting via $\pi_P \circ \operatorname{pr}_1$. Under the diffeomorphism $P \cong M$ of the previous step this is $M \times H$ with the standard right $H$-action and projection to $M$ — the trivial principal $H$-bundle.
>
> ($\Rightarrow$) Suppose $Q$ admits a reduction to $\{e\}$: there is a principal $\{e\}$-bundle $P$ and an isomorphism $P \times_\iota H \cong Q$. By the two Step-0 observations, $P \times_\iota H \cong M \times H$, so $Q \cong M \times H$ is trivial.
>
> ($\Leftarrow$) Suppose $Q$ is trivial, $Q \cong M \times H$. Take $P := M$, the trivial $\{e\}$-principal bundle. By Step 0 its extension is $P \times_\iota H \cong M \times H \cong Q$, so this exhibits a reduction of $Q$ to $\{e\}$. This proves (iv).
>
> All four parts are established. $\blacksquare$

A remark on the sources. Part (i) is Bär's Conclusion 2.2.15, with Remark 2.2.2 supplying the orbit-map diffeomorphism used implicitly and Bär's "obviously smooth" for the section replaced here by the explicit smoothness argument of Lemma 2; it is Haydys' Exercise 25, whose additional clause that $\operatorname{Fr}(TS^2)$ has no global section is deferred to §3.5, where the hairy-ball obstruction is available. Part (iv) is Bär's Example 2.2.11, stated there without proof; the proof above is supplied in full.

---

# Cross-Field Exercise Suggestions

**Parallelisable manifolds and Lie groups.** On any Lie group $G$, the left-invariant vector fields furnish a global frame of the tangent bundle $TG$: choosing a basis of $\mathfrak{g} = T_eG$ and extending by left translation gives $n = \dim G$ everywhere-independent smooth fields. By part (iii), $TG$ is therefore trivial, so every Lie group is parallelisable. The theorem applies because the frame these fields define is exactly a global section of $\operatorname{Fr}(TG)$; the non-obvious point is that the *algebraic* homogeneity of $G$ (translations are diffeomorphisms) produces the *topological* triviality of its tangent bundle, and the bridge between the two is precisely this correspondence.

**Orientability as a reduction, read through sections.** An oriented rank-$k$ Euclidean bundle has structure group reduced to $SO(k)$, and orientability of a real bundle is equivalent to the frame bundle's having a two-component sub-object with a global "positive" component. Investigating when the Möbius line bundle over $S^1$ fails to be trivial becomes, through part (iii), the question of whether it has a global nowhere-vanishing section; it does not, because such a section would trivialise it. The theorem applies because triviality has been converted to the existence of a global frame; the subtlety is that a rank-one real bundle is trivial precisely when orientable, and the section criterion is what makes this checkable.

**Clutching functions and bundles over spheres.** A principal $G$-bundle over $S^n$ is built from a clutching map $S^{n-1} \to G$ gluing two trivial pieces over the hemispheres, each of which has a section because it is trivial. The bundle is trivial exactly when the clutching map is null-homotopic, which one detects by whether the two hemisphere sections can be matched into a global section. The theorem applies because it turns global triviality into the existence of a global section, and hence into a homotopy question about the clutching map; the depth is that an analytic gluing datum becomes an element of $\pi_{n-1}(G)$, and the vanishing of that element is the triviality criterion.

---

# Bridges

- **[[Def - Transition Functions and the Cocycle Condition|Transition functions and cocycles]].** Choosing, over a trivialising cover $\{U_\alpha\}$, a local section $s_\alpha$ for each $\alpha$ — which exists over each $U_\alpha$ precisely by part (i) — and comparing them on an overlap gives the unique smooth $g_{\alpha\beta} : U_{\alpha\beta} \to G$ with $s_\beta = s_\alpha \cdot g_{\alpha\beta}$. The whole cocycle description of a principal bundle is built directly on this theorem: sections are the raw material, transition functions the pairwise comparisons.

- **[[Thm - The Hopf Bundle is Nontrivial|Nontriviality of the Hopf bundle]].** The nontriviality of $S^3 \to S^2$ is proved by showing it has no global section: if it had one, part (ii) would give $S^3 \cong S^2 \times S^1$ as bundles, and a cohomological invariant ($H^1_{\mathrm{dR}}$) distinguishes the two total spaces. This is the archetype of using part (ii) contrapositively, converting a triviality question into a nonexistence-of-section computation.

- **[[Def - Connections on Principal Bundles|Local connection forms]].** A [[Def - Connections on Principal Bundles|connection]] $\omega \in \Omega^1(P; \mathfrak{g})$ is recorded on the base by pulling it back along a local section, $A_s := s^*\omega$; changing the section by $s' = s\cdot g$ changes $A_s$ by the gauge-transformation rule. The section-versus-trivialisation correspondence is what licenses this: "choose a local gauge" and "choose a local trivialisation" are the same act, and the section is the more convenient of the two to pull back along.

- **[[Def - Reduction and Extension of the Structure Group|Reduction of the structure group]].** Part (iv) is the extreme case — reduction to $\{e\}$ — of the general reduction theory. A reduction of a principal $H$-bundle to a subgroup $G \leq H$ is a $G$-subbundle of frames, and the trivial-group case says that reducing all the way down to a point is the same as trivialising. Reductions to intermediate groups ($O(k)$, $SL_k$, $U(m)$) are the subject of the following pages and correspond to extra geometric structure on the associated vector bundle.

---

# Unlocked by This

> [!tip] Global frame criterion for parallelisability *(from Differential Topology)*
> A manifold $M^n$ is parallelisable — its tangent bundle is trivial — if and only if $\operatorname{Fr}(TM)$ admits a global section, i.e. $M$ admits $n$ everywhere-independent global vector fields. Part (iii) is the exact statement; the spheres $S^1, S^3, S^7$ are parallelisable while $S^2$ is not, the last by the hairy-ball obstruction of §3.5.

> [!tip] The clutching classification of bundles over spheres *(from Homotopy Theory)*
> Because each hemisphere of $S^n$ carries a section, a principal $G$-bundle over $S^n$ is determined by its clutching map $S^{n-1} \to G$ up to homotopy, giving a bijection between isomorphism classes and $\pi_{n-1}(G)$. Triviality corresponds, through part (ii), to the null-homotopy class. This underlies the §3.6 classification of $U(1)$- and $SU(2)$-bundles over low-dimensional manifolds.
