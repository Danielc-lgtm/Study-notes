---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Gauge Transformation"
  - "Def - Connection on a Principal Bundle"
  - "Def - Curvature of a Principal Connection"
  - "Thm - Transformation of Local Connection and Curvature Forms"
  - "Thm - Gauge Action on Connection Matrices"
  - "Thm - Principal Connections Induce Covariant Derivatives on Associated Bundles"
  - "Def - The Maurer-Cartan Form"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $\pi : P \to M$ is a smooth principal $G$-bundle over a smooth manifold $M$, with $G$ acting on the **right**: $R_g(p) = p \cdot g$ for $p \in P$, $g \in G$. The Lie algebra is $\mathfrak g = T_e G$; for a matrix group the bracket is the commutator and $\operatorname{Ad}_g X = g X g^{-1}$, $\operatorname{ad}_X Y = [X, Y]$. The **fundamental vector field** of $\xi \in \mathfrak g$ is $\xi_P(p) = \frac{d}{dt}\big|_{t=0}\, p \cdot \exp(t\xi)$ (see [[Def - Fundamental Vector Field of a Group Action]]).

A **connection** on $P$ is a form $\omega \in \Omega^1(P; \mathfrak g)$ satisfying the two axioms
$$R_g^*\omega = \operatorname{Ad}_{g^{-1}} \omega \quad (\text{equivariance}), \qquad \omega(\xi_P) = \xi \quad (\text{reproduction of fundamental fields})$$
for all $g \in G$ and $\xi \in \mathfrak g$; the set of connections is written $\mathcal A(P)$ (this is Bär's $\mathcal C(P)$), and it is an affine space modelled on $\Omega^1(M; \operatorname{ad}P)$ (see [[Def - Connection on a Principal Bundle]]). Its **curvature** is $\Omega_\omega = d\omega + \tfrac12 [\omega \wedge \omega] \in \Omega^2(P; \mathfrak g)$, which is horizontal and $\operatorname{Ad}$-equivariant and so descends to a form $F_\omega \in \Omega^2(M; \operatorname{ad}P)$ (see [[Def - Curvature of a Principal Connection]]). The **bracket of $\mathfrak g$-valued forms** used here is $[\alpha \wedge \beta](X, Y) = [\alpha(X), \beta(Y)] - [\alpha(Y), \beta(X)]$ on $1$-forms, so that $[\omega \wedge \omega](X, Y) = 2[\omega(X), \omega(Y)]$; this is the convention that puts the factor $\tfrac12$ in the structure equation (see [[Def - Lie-Algebra-Valued Differential Forms and Their Bracket]]).

An **automorphism** of $P$ is a diffeomorphism $f : P \to P$ with $f(p \cdot g) = f(p) \cdot g$ for all $p, g$; they form the group $\operatorname{Aut}(P) \subseteq \operatorname{Diff}(P)$. A **gauge transformation** is an $f \in \operatorname{Aut}(P)$ whose induced base map $\bar f$ (defined below) is the identity; the gauge transformations form the **gauge group** $\mathcal G(P)$ (see [[Def - Gauge Transformation]]). Given $f \in \mathcal G(P)$, because $f(p)$ lies in the same fibre as $p$ there is a function $\hat g : P \to G$ with $f(p) = p \cdot \hat g(p)$; equivariance of $f$ forces
$$\hat g(p \cdot g) = g^{-1}\,\hat g(p)\, g \qquad (g \in G).$$

> [!warning] Convention: the equivariance identity for $\hat g$
> Haydys prints this identity as "$\hat f(pg) = g^{-1} p g$" (equation (58), page 21), which is a typographical slip — the right-hand side must be an element of $G$, not of $P$. The correct identity is $\hat g(pg) = g^{-1}\,\hat g(p)\,g$, and it says exactly that $\hat g$ is an equivariant function for the conjugation action of $G$ on itself, i.e. a section of the adjoint group bundle $\operatorname{Ad}P = P \times_G G$ (see [[Def - Adjoint Bundles ad P and Ad P]]).

The **left Maurer–Cartan form** of $G$ is $\theta \in \Omega^1(G; \mathfrak g)$, $\theta_a = (dL_{a^{-1}})_a : T_a G \to \mathfrak g$; for a matrix group $\theta = g^{-1}\,dg$ (see [[Def - The Maurer-Cartan Form]]). For a local section $s : U \to P$ over an open set $U \subseteq M$ we write the **local connection form** (gauge potential) $A_{\omega, s} := s^*\omega \in \Omega^1(U; \mathfrak g)$ and the **local curvature form** $F_{\omega, s} := s^*\Omega_\omega \in \Omega^2(U; \mathfrak g)$. Given a representation $\rho : G \to GL(V)$ on a finite-dimensional vector space $V$, the associated bundle is $E = P \times_\rho V = (P \times V)/\!\sim$ with $[p \cdot g, v] = [p, \rho(g)^{-1} v]$; the connection $\omega$ induces a covariant derivative $\nabla^\omega$ on $E$ (see [[Thm - Principal Connections Induce Covariant Derivatives on Associated Bundles]]), and $\gamma(f) \in \mathcal G(E)$ is the induced gauge transformation of $E$, where $\mathcal G(E) = \{h \in \Gamma(\operatorname{End}E) : h(m) \in GL(E_m)\}$ is the vector-bundle gauge group (see [[Def - Gauge Group of a Vector Bundle]]). Finally $d^{\nabla_\omega}$ is the exterior covariant derivative on $\operatorname{ad}P$-valued forms (see [[Def - Exterior Covariant Derivative on a Principal Bundle]]).

---

# Statement

> **Theorem (gauge transformations act on connections and curvature).** Let $\pi : P \to M$ be a smooth principal $G$-bundle.
>
> **(a) Automorphisms cover diffeomorphisms.** $\operatorname{Aut}(P)$ is a subgroup of $\operatorname{Diff}(P)$. Every $f \in \operatorname{Aut}(P)$ carries fibres to fibres, and there is a unique smooth map $\bar f : M \to M$ with $\pi \circ f = \bar f \circ \pi$; the assignment $f \mapsto \bar f$ is a group homomorphism $\operatorname{Aut}(P) \to \operatorname{Diff}(M)$ whose kernel is $\mathcal G(P)$.
>
> **(b) Pull-back is a right action on connections, and it is affine.** For $\omega \in \mathcal A(P)$ and $f \in \operatorname{Aut}(P)$ the pull-back $f^*\omega$ again lies in $\mathcal A(P)$, and $(\omega, f) \mapsto \omega \cdot f := f^*\omega$ is a right action of $\operatorname{Aut}(P)$ — hence of $\mathcal G(P)$ — on $\mathcal A(P)$. The action is affine: for the lift $\hat b \in \Omega^1(P; \mathfrak g)$ of any $b \in \Omega^1(M; \operatorname{ad}P)$ one has $f^*(\omega + \hat b) = f^*\omega + f^*\hat b$, and for $f \in \mathcal G(P)$ the increment transforms by the adjoint action, $f^*\hat b = \operatorname{Ad}_{\hat g^{-1}} \hat b$.
>
> **(c) Explicit formula and the curvature.** Curvature is natural under pull-back: $\Omega_{f^*\omega} = f^*\Omega_\omega$ for every $f \in \operatorname{Aut}(P)$. For $f \in \mathcal G(P)$, written $f(p) = p \cdot \hat g(p)$ with $\hat g(pg) = g^{-1}\hat g(p) g$,
> $$f^*\omega = \operatorname{Ad}_{\hat g^{-1}} \omega + \hat g^*\theta, \qquad f^*\Omega_\omega = \operatorname{Ad}_{\hat g^{-1}} \Omega_\omega.$$
> In a local section $s : U \to P$, with $g := \hat g \circ s : U \to G$, the local forms transform by
> $$A_{f^*\omega, s} = \operatorname{Ad}_{g^{-1}} A_{\omega, s} + g^*\theta \quad (\text{matrix case } g^{-1} A_{\omega, s}\, g + g^{-1}\,dg), \qquad F_{f^*\omega, s} = \operatorname{Ad}_{g^{-1}} F_{\omega, s} \quad (\text{matrix case } g^{-1} F_{\omega, s}\, g).$$
>
> **(d) Compatibility with the vector-bundle action.** For an associated bundle $E = P \times_\rho V$ and $f \in \mathcal G(P)$ with induced $\gamma(f) \in \mathcal G(E)$,
> $$\nabla^{f^*\omega} = \gamma(f)^{-1} \circ \nabla^\omega \circ \gamma(f).$$
> Thus the pull-back action on principal connections induces, on each associated bundle, exactly the vector-bundle gauge action $\nabla \mapsto \gamma(f)^{-1} \nabla\, \gamma(f)$.
>
> **(e) Infinitesimal action.** For $\xi \in \Gamma(\operatorname{ad}P)$, with lift $\hat\xi : P \to \mathfrak g$ ($\hat\xi(pg) = \operatorname{Ad}_{g^{-1}}\hat\xi(p)$), the one-parameter family $f_t(p) = p \cdot \exp(t\,\hat\xi(p))$ lies in $\mathcal G(P)$ with $f_0 = \operatorname{id}_P$, and
> $$\frac{d}{dt}\Big|_{t=0} f_t^*\omega = \widehat{d^{\nabla_\omega}\xi},$$
> so the infinitesimal action is the exterior covariant derivative $\xi \mapsto d^{\nabla_\omega}\xi \in \Omega^1(M; \operatorname{ad}P)$; that is, the map $\mathcal A(P) \times \Gamma(\operatorname{ad}P) \to \Omega^1(M; \operatorname{ad}P)$, $(\omega, \xi) \mapsto d^{\nabla_\omega}\xi$.

---

# Motivation

Every subsequent chapter of this series in which a moduli space appears — the Chern–Weil quotients of chapter VI, the Yang–Mills configuration space $\mathcal A/\mathcal G$ of chapter VII, the Seiberg–Witten space of chapter XI — is a set of connections divided by an equivalence relation, and the equivalence relation is always the same one: two connections are declared "the same" when a gauge transformation carries one to the other. Before any of that quotient geometry can begin we must know precisely how a gauge transformation moves a connection, whether the movement is an action of a group at all, and what it does to the curvature. This theorem answers all three questions at once. It is the definitional backbone of gauge theory in the sense the field is named for: the objects of interest are not connections but connections up to the action described here.

The theorem also settles a translation that has been latent since chapter II. In the physicist's language a "gauge transformation" is a **local** change of the choice of section — a relabelling $s \rightsquigarrow s \cdot g$ of the frame over a coordinate patch — under which the potential transforms by $A \mapsto g^{-1} A g + g^{-1}\,dg$ (this is [[Thm - Gauge Action on Connection Matrices]], and Haydys records it as the coincidence R2.1.9 that the frame-change law and the gauge-action law are the same formula). In the geometer's language a gauge transformation is a **global** bundle automorphism $f : P \to P$ covering the identity. Part (c) proves these are the same operation: the local formula produced by the global automorphism $f$ is exactly the frame-change formula, with $g = \hat g \circ s$ the local expression of the automorphism. The one-sentence mechanism, which is worth carrying through the rest of the series, is that **a gauge transformation is a change of local section performed globally and consistently across all patches, and it therefore acts on the potential by the same formula as an ordinary change of trivialisation.**

The single structural fact that makes the whole edifice work is the transformation law of the curvature. The potential $A$ transforms with an inhomogeneous term $g^*\theta$ — it is not a tensor, it is an affine object — but the curvature transforms **homogeneously**, $F \mapsto \operatorname{Ad}_{g^{-1}} F$, with no additive correction. This is why $F$ descends to a genuine bundle-valued two-form on $M$, why any $\operatorname{Ad}$-invariant polynomial in $F$ is gauge invariant, and hence why the Chern–Weil forms and the Yang–Mills energy $\tfrac12\int_M |F_\omega|^2$ are functions on the quotient $\mathcal A/\mathcal G$ rather than merely on $\mathcal A$. Part (c)'s second formula is thus the quiet hinge on which characteristic classes and the Yang–Mills functional both turn.

We assume the reader knows the definition of a principal connection and its curvature, the fundamental vector fields, the Maurer–Cartan form, and the equivariant-function description of sections of an associated bundle; all are recalled at the point of use. The audience is someone comfortable with differential forms and Lie groups but seeing the gauge action assembled for the first time.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal hypothesis is mild — a principal bundle, a connection, and an automorphism — so the useful question is: when does a problem hand you an automorphism of $P$, or an element of $\mathcal G(P)$, without naming one?

The first disguised source is **a fibrewise change of trivialisation given by transition-type data**. Whenever one is handed a family of smooth maps $g_\alpha : U_\alpha \to G$ on the patches of a trivialising cover that agree on overlaps in the sense $g_\beta = c_{\alpha\beta}^{-1} g_\alpha c_{\alpha\beta}$ (conjugation by the transition functions $c_{\alpha\beta}$), the $g_\alpha$ patch together into a single section of $\operatorname{Ad}P$ and hence, by [[Thm - The Gauge Group is the Space of Sections of the Adjoint Group Bundle]], into a global gauge transformation. The bridge $B \Rightarrow A$ is the equivalence "compatible local group-valued data $\iff$ section of the adjoint group bundle $\iff$ gauge transformation", and it is non-obvious because the local data look like nothing more than a coordinate convenience until the cocycle-compatibility is checked. *Example problem:* given a Hermitian line bundle with local unit-modulus functions $g_\alpha = e^{i\chi_\alpha}$ satisfying $\chi_\beta - \chi_\alpha = $ const on overlaps, produce the global gauge transformation acting by $A \mapsto A + i\,d\chi_\alpha$ and read off that the curvature is unchanged.

The second disguised source is **a symmetry of the base that lifts to the bundle**. A diffeomorphism $\varphi : M \to M$ that lifts to an equivariant $f : P \to P$ with $\bar f = \varphi$ is an automorphism, and it is a gauge transformation exactly when $\varphi = \operatorname{id}_M$. The bridge is that any bundle map covering the identity is automatically an element of $\mathcal G(P)$ once equivariance is verified, so "a fibre-preserving bundle self-map covering $\operatorname{id}_M$" is a gauge transformation in disguise. This is non-obvious because one usually meets such maps as invariances of a physical field configuration rather than as group elements. *Example problem:* the constant phase rotations $[p, v] \mapsto [p, e^{i\alpha} v]$ of an associated line bundle are the gauge transformations $f(p) = p \cdot e^{i\alpha}$ coming from the centre of $U(1)$; use part (c) to see they fix every connection, so they are exactly the stabiliser one divides out to form the reduced configuration space.

The third disguised source is **an equivariant Lie-algebra-valued function, delivered as an infinitesimal symmetry**. A section $\xi \in \Gamma(\operatorname{ad}P)$ — equivalently an equivariant $\hat\xi : P \to \mathfrak g$ — exponentiates by $f_t(p) = p \exp(t\hat\xi(p))$ to a one-parameter subgroup of $\mathcal G(P)$, so any infinitesimal gauge symmetry is the generator of a genuine gauge flow. The bridge $B \Rightarrow A$ is exponentiation of $\Gamma(\operatorname{ad}P)$, the Lie algebra of $\mathcal G(P)$, into the group; its payoff is part (e), which identifies the derivative of the flow with the covariant derivative $d^{\nabla_\omega}\xi$. This is non-obvious because the "Lie algebra of the gauge group" is an infinite-dimensional object and one must know that its exponential lands back in $\mathcal G(P)$. *Example problem:* on a trivial $U(1)$-bundle, take $\hat\xi = i\chi$ for $\chi : M \to \mathbb R$ and verify that the flow moves $A$ along the line $A + t\, i\,d\chi$, recovering the abelian infinitesimal gauge transformation of electromagnetism.

**Targets (Output Amplification)**

The bare conclusions are the transformation laws; combined with other ingredients they build the central objects of the field.

Combine part (c) with **an $\operatorname{Ad}$-invariant polynomial or inner product on $\mathfrak g$**. If $q$ is $\operatorname{Ad}$-invariant, then because $F_{f^*\omega, s} = \operatorname{Ad}_{g^{-1}} F_{\omega, s}$ the value $q(F)$ is unchanged by the gauge transformation. The extra ingredient is $\operatorname{Ad}$-invariance; the payoff is that the Chern–Weil forms $q(F_\omega)$ and the Yang–Mills density $|F_\omega|^2$ are gauge invariant, hence descend to functions on the quotient $\mathcal A/\mathcal G$. This is the mechanism by which chapter VI's characteristic classes and chapter VII's Yang–Mills functional are well defined on gauge-equivalence classes rather than on individual connections.

Combine parts (a) and (b) with **a base point and a connectedness hypothesis**. Restricting the action to the reduced gauge group $\mathcal G_b(P)$ (those $f$ fixing the fibre over $b$) and using horizontal lifts, one obtains a **free** action of $\mathcal G_b(P)$ on $\mathcal A(P)$ — this is proved in [[Thm - The Reduced Gauge Group Acts Freely on Connections]]. The extra ingredients are the base point and the connectedness of $M$; the payoff is that the quotient $\mathcal A/\mathcal G_b(P)$ has, away from the reducible locus, the structure of a manifold, the starting point for every instanton and monopole moduli-space construction in chapters X, XI, and XIII.

Combine part (e) with **the ellipticity of the deformation complex**. The infinitesimal action $\xi \mapsto d^{\nabla_\omega}\xi$ is the first map of the fundamental complex $\Omega^0(M; \operatorname{ad}P) \xrightarrow{d^{\nabla_\omega}} \Omega^1(M; \operatorname{ad}P) \xrightarrow{d^{\nabla_\omega}} \Omega^2(M; \operatorname{ad}P)$ whose cohomology, when the complex is completed with the linearised anti-self-duality operator, computes the tangent space to the moduli space. The extra ingredient is elliptic theory (chapter IX); the payoff is the dimension formula for instanton moduli spaces, obtained by an index computation whose zeroth term is precisely the image of this infinitesimal gauge action.

---

# Why Is It True

Strip away the formulas and the whole theorem is one observation carried out four times. A gauge transformation $f \in \mathcal G(P)$ slides each point $p$ along its own fibre to $p \cdot \hat g(p)$. A connection $\omega$ is a rule for measuring the "vertical part" of a tangent vector, gauged to the fibre coordinate; when we move the point along the fibre, two things happen to that measurement. First, the fibre coordinate itself is rotated by $\hat g(p)$, and any object valued in $\mathfrak g$ that transforms tensorially under the fibre gets conjugated by $\operatorname{Ad}_{\hat g^{-1}}$ — this is the homogeneous piece. Second, the sliding rule $\hat g$ is itself allowed to vary from point to point, and the rate at which it varies is measured by $\hat g^*\theta$, the pull-back of the Maurer–Cartan form; this is the inhomogeneous piece, the "cost of moving the section". The potential feels both pieces, $\operatorname{Ad}_{\hat g^{-1}}\omega + \hat g^*\theta$, because the potential is not a tensor. The curvature feels only the first, $\operatorname{Ad}_{\hat g^{-1}}\Omega$, because the curvature is horizontal: it is blind to motion along the fibre, and the inhomogeneous term lives entirely in the fibre direction, so it cannot see it.

> **The one-line mechanism.** A gauge transformation is a fibrewise rotation $p \mapsto p \cdot \hat g(p)$; the potential picks up both the conjugation $\operatorname{Ad}_{\hat g^{-1}}$ and the Maurer–Cartan "cost of moving" $\hat g^*\theta$, while the curvature, being horizontal, picks up only the conjugation.

The naturality half of the theorem, $\Omega_{f^*\omega} = f^*\Omega_\omega$, is even simpler in spirit: the curvature is built from $\omega$ by exterior differentiation and bracketing, and both of those operations commute with pull-back by a smooth map. So whatever $f$ does to $\omega$, it does compatibly to $\Omega_\omega$; curvature is a functor of the connection. The homogeneous transformation law is then not a separate computation but the same $\operatorname{Ad}_{\hat g^{-1}}$ conjugation applied to the horizontal object $\Omega_\omega$ instead of the non-horizontal object $\omega$.

Finally, that this deserves to be called a **right action** rather than merely a family of maps is because pull-back reverses composition: $(f_1 \circ f_2)^* = f_2^* \circ f_1^*$. The order-reversal is precisely what turns the left-to-right composition of automorphisms into a right action on forms, and it is the reason the moduli space is written $\mathcal A/\mathcal G$ as a right quotient throughout the series.

---

# What Makes This Hard

The non-obvious computational step is the appearance of the Maurer–Cartan term, which requires the differential of the group action $\Phi(p, a) = p \cdot a$ in **both** slots at once: moving $p$ contributes $dR_a$, and moving $a$ contributes a fundamental vector field weighted by $\theta_a$. Beginners differentiate only the point $p$ and lose the inhomogeneous term $\hat g^*\theta$ entirely, "proving" the false statement that the potential transforms tensorially. The second common error is a sign or side error in $\hat g(pg) = g^{-1}\hat g(p)g$ (Haydys even misprints it): getting the conjugation backwards flips $\operatorname{Ad}_{\hat g^{-1}}$ to $\operatorname{Ad}_{\hat g}$ and breaks the compatibility of the two connection axioms. The third subtlety is entirely about conventions: the sign of the infinitesimal action in part (e) depends on whether one reads the pull-back as a right or a left action, and the two standard references land on opposite signs — the reconciliation is spelled out at the point of use.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Establish the differential of the action map once (it produces every Maurer–Cartan term). Prove (a) and (b) by pure functoriality of pull-back. Get the explicit formula in (c) by feeding the action-map differential into $f^*\omega$; get the curvature law from horizontality plus equivariance, and both local laws by pulling back along a section. Deduce (d) by writing sections of $E$ as equivariant functions, on which everything becomes the same algebra as (c). Get (e) by differentiating (c) with $\hat g = \exp(t\hat\xi)$.

**Subgoal decomposition:**

1. **Differential of the action map.** For $\Phi(p, a) = p \cdot a$, show $d\Phi_{(p, a)}(v, w) = dR_a(v) + \big(\theta_a(w)\big)_P(p \cdot a)$.
   - *Hint:* Vary $p$ with $a$ fixed to get $dR_a(v)$; vary $a = a(t)$ with $p$ fixed, writing $a(t) = a\exp(t\xi + o(t))$ so $\xi = \theta_a(\dot a(0))$, and recognise a fundamental vector field.
   - *Why needed:* It is the only source of the inhomogeneous $\hat g^*\theta$ term and is reused verbatim in (c), (d), (e).

2. **Automorphisms descend, smoothly.** Show every $f \in \operatorname{Aut}(P)$ maps fibres to fibres and induces a unique smooth $\bar f$; then $f \mapsto \bar f$ is a homomorphism with kernel $\mathcal G(P)$.
   - *Hint:* Fibres to fibres from equivariance; smoothness of $\bar f$ by writing $\bar f|_{U} = \pi \circ f \circ s$ for a local section $s$.
   - *Why needed:* This is part (a) and it is what defines $\mathcal G(P)$ as a kernel; it fills the gap Bär leaves ("smoothness of $\bar f$ asserted").

3. **Pull-back preserves and acts.** Show $f^*\omega \in \mathcal A(P)$ and $(f_1 f_2)^*\omega = f_2^* f_1^*\omega$.
   - *Hint:* Check the two connection axioms for $f^*\omega$ using $f \circ R_g = R_g \circ f$ and $df \circ \xi_P = \xi_P \circ f$; order-reversal of pull-back gives the right action.
   - *Why needed:* This is part (b); without it the "action" is not defined.

4. **The gauge descent formula.** For $f(p) = p\,\hat g(p)$, show $f^*\omega = \operatorname{Ad}_{\hat g^{-1}}\omega + \hat g^*\theta$, and $f^*\Omega_\omega = \operatorname{Ad}_{\hat g^{-1}}\Omega_\omega$.
   - *Hint:* Apply subgoal 1 with $a = \hat g(p)$, $w = d\hat g(v)$; the $dR_a$ part meets equivariance and the fundamental-field part meets axiom (2). For curvature use horizontality to kill the fibre part.
   - *Why needed:* This is the heart of (c); the local laws follow by pulling back along a section.

5. **Transport to associated bundles and to the infinitesimal level.** Rewrite sections of $E$ as equivariant functions to get (d); differentiate (c) at $t = 0$ with $\hat g = \exp(t\hat\xi)$ to get (e).
   - *Hint:* On equivariant functions $\gamma(f)$ acts by $\rho(\hat g)$ and $\nabla^\omega$ by $d + \rho_*(\omega)$; for (e) use $\frac{d}{dt}\big|_0 \operatorname{Ad}_{\exp(-t\hat\xi)} = -\operatorname{ad}_{\hat\xi}$ and $\frac{d}{dt}\big|_0 (\exp t\hat\xi)^*\theta = d\hat\xi$.
   - *Why needed:* These are parts (d) and (e) and they connect the principal picture to the vector-bundle picture and to the deformation complex.

---

# Lemma Decomposition

> [!note]- Lemma 1: Differential of the right action map
> **Statement:** Let $G$ act on $P$ on the right, and let $\Phi : P \times G \to P$, $\Phi(p, a) = p \cdot a$, be the action map. For $p \in P$, $a \in G$, $v \in T_p P$, $w \in T_a G$,
> $$d\Phi_{(p, a)}(v, w) = dR_a(v) + \big(\theta_a(w)\big)_P(p \cdot a),$$
> where $\theta_a(w) = (dL_{a^{-1}})_a(w) \in \mathfrak g$ is the left Maurer–Cartan form and $(\eta)_P$ is the fundamental vector field of $\eta \in \mathfrak g$.
>
> **Hint:** Split $(v, w) = (v, 0) + (0, w)$ and use bilinearity of the differential; for the $(0, w)$ direction write a curve in $G$ through $a$ with velocity $w$ in Maurer–Cartan form.
>
> **Why needed:** This lemma is the single origin of every Maurer–Cartan term in the theorem; it is used in Lemma 4 and, through it, in parts (c), (d), and (e).
>
> > [!note]- Full proof
> > We compute $d\Phi_{(p,a)}$ on the two coordinate directions and add, using that the differential of a smooth map at a point is linear, so $d\Phi_{(p,a)}(v, w) = d\Phi_{(p,a)}(v, 0) + d\Phi_{(p,a)}(0, w)$.
> >
> > **The $P$-direction.** Fix $a$ and let $c : (-\varepsilon, \varepsilon) \to P$ be a curve with $c(0) = p$, $\dot c(0) = v$. Then $\Phi(c(t), a) = c(t) \cdot a = R_a(c(t))$, so
> > $$d\Phi_{(p,a)}(v, 0) = \frac{d}{dt}\Big|_{0} R_a(c(t)) = dR_a(v) \qquad (\text{chain rule; } R_a = \Phi(\,\cdot\,, a)).$$
> >
> > **The $G$-direction.** Fix $p$ and let $a : (-\varepsilon, \varepsilon) \to G$ be a curve with $a(0) = a$, $\dot a(0) = w$. Set $\xi := \theta_a(w) = (dL_{a^{-1}})_a(w) \in \mathfrak g$. Then $b(t) := a^{-1} a(t)$ satisfies $b(0) = e$ and $\dot b(0) = (dL_{a^{-1}})_a(w) = \xi$, so $a(t) = a \cdot b(t)$ with $b(t) = \exp(t\xi) + o(t)$ in any chart at $e$ (because $b(0) = e$ and $\dot b(0) = \xi$, and $t \mapsto \exp(t\xi)$ has the same $1$-jet). Hence
> > $$d\Phi_{(p,a)}(0, w) = \frac{d}{dt}\Big|_{0} p \cdot a(t) = \frac{d}{dt}\Big|_{0} (p \cdot a) \cdot b(t) = \frac{d}{dt}\Big|_{0} (p \cdot a) \cdot \exp(t\xi) \qquad (\text{same } 1\text{-jet as } b(t))$$
> > $$= \xi_P(p \cdot a) = \big(\theta_a(w)\big)_P(p \cdot a) \qquad (\text{definition of the fundamental vector field of } \xi = \theta_a(w)).$$
> > Here the second equality uses associativity of the right action, $p \cdot a(t) = p \cdot (a\, b(t)) = (p \cdot a) \cdot b(t)$, and the third uses that a derivative at $t = 0$ depends only on the $1$-jet of the curve.
> >
> > **Conclusion.** Adding the two directions,
> > $$d\Phi_{(p,a)}(v, w) = dR_a(v) + \big(\theta_a(w)\big)_P(p \cdot a). \qquad \blacksquare$$

> [!note]- Lemma 2: Automorphisms carry fibres to fibres and descend to a unique smooth base map
> **Statement:** Let $f \in \operatorname{Aut}(P)$. Then $f$ maps each fibre $P_x = \pi^{-1}(x)$ into a single fibre, and there is a unique smooth map $\bar f : M \to M$ with $\pi \circ f = \bar f \circ \pi$.
>
> **Hint:** Two points in one fibre differ by a unique group element (the action is free and transitive on fibres); apply equivariance. For smoothness, compose with a local section.
>
> **Why needed:** It gives the base map $\bar f$ that defines the homomorphism $f \mapsto \bar f$ and hence $\mathcal G(P)$ as its kernel; it fills the smoothness step asserted without proof in Bär's Remark 2.7.2.
>
> > [!note]- Full proof
> > **Fibres go to fibres.** Let $p, p' \in P_x$ lie in the same fibre. Because $G$ acts freely and transitively on each fibre, there is a unique $g \in G$ with $p' = p \cdot g$. Applying $f$ and using equivariance $f(p \cdot g) = f(p) \cdot g$,
> > $$f(p') = f(p \cdot g) = f(p) \cdot g \qquad (\text{equivariance of } f),$$
> > so $f(p')$ and $f(p)$ lie in the same fibre. Thus $f(P_x)$ is contained in a single fibre, and since $f$ is a bijection carrying fibres into fibres it permutes the fibres.
> >
> > **Existence and uniqueness of $\bar f$.** Define $\bar f : M \to M$ by $\bar f(x) := \pi(f(p))$ for any $p \in P_x$; this is independent of the choice of $p$ by the previous paragraph, so $\bar f$ is a well-defined map of sets and satisfies $\pi \circ f = \bar f \circ \pi$ by construction. If $\bar f'$ also satisfies $\pi \circ f = \bar f' \circ \pi$, then $\bar f' \circ \pi = \bar f \circ \pi$, and since $\pi$ is surjective this forces $\bar f' = \bar f$; hence $\bar f$ is unique.
> >
> > **Smoothness.** Fix $x_0 \in M$ and choose a trivialising open set $U \ni x_0$ with a smooth local section $s : U \to P$ (which exists on any trivialising set: $s(x) = \psi^{-1}(x, e)$ for a local trivialisation $\psi$). On $U$,
> > $$\bar f|_U = \pi \circ f \circ s \qquad (\text{because } \pi(s(x)) = x, \text{ so } \bar f(x) = \pi(f(s(x)))),$$
> > which is a composition of the smooth maps $s$, $f$, and $\pi$, hence smooth on $U$. As $x_0$ was arbitrary and smoothness is local, $\bar f$ is smooth on $M$. $\blacksquare$

> [!note]- Lemma 3: Pull-back preserves connections and reverses composition
> **Statement:** For $f \in \operatorname{Aut}(P)$ and $\omega \in \mathcal A(P)$, the form $f^*\omega$ is again a connection. Moreover $\operatorname{id}_P^*\,\omega = \omega$ and $(f_1 \circ f_2)^*\omega = f_2^*(f_1^*\omega)$ for $f_1, f_2 \in \operatorname{Aut}(P)$.
>
> **Hint:** Verify the two connection axioms for $f^*\omega$; use $f \circ R_g = R_g \circ f$ for equivariance and $df_p(\xi_P(p)) = \xi_P(f(p))$ for the fundamental-field axiom.
>
> **Why needed:** It is the entire content of part (b): $f^*\omega$ lands in $\mathcal A(P)$ (so the action is defined) and pull-back reverses composition (so it is a *right* action).
>
> > [!note]- Full proof
> > **Axiom (1), equivariance.** For $g \in G$, using $f \circ R_g = R_g \circ f$ (which is the equivariance of $f$ rewritten with translations) and functoriality of pull-back,
> > $$R_g^*(f^*\omega) = (f \circ R_g)^*\omega = (R_g \circ f)^*\omega = f^*(R_g^*\omega) = f^*(\operatorname{Ad}_{g^{-1}}\omega) = \operatorname{Ad}_{g^{-1}}(f^*\omega).$$
> > The fourth equality is axiom (1) for $\omega$; the fifth holds because $\operatorname{Ad}_{g^{-1}}$ is a fixed linear endomorphism of $\mathfrak g$ acting on the *values* of the form, and pull-back acts on the *covector* part, so the two commute.
> >
> > **Axiom (2), fundamental fields.** First, $df_p(\xi_P(p)) = \xi_P(f(p))$: with the curve $t \mapsto p \cdot \exp(t\xi)$,
> > $$df_p(\xi_P(p)) = \frac{d}{dt}\Big|_{0} f\big(p \cdot \exp(t\xi)\big) = \frac{d}{dt}\Big|_{0} f(p) \cdot \exp(t\xi) = \xi_P(f(p)) \qquad (\text{equivariance of } f).$$
> > Therefore, for $\xi \in \mathfrak g$,
> > $$(f^*\omega)_p(\xi_P(p)) = \omega_{f(p)}\big(df_p(\xi_P(p))\big) = \omega_{f(p)}\big(\xi_P(f(p))\big) = \xi \qquad (\text{axiom (2) for } \omega).$$
> > Both axioms hold, so $f^*\omega \in \mathcal A(P)$.
> >
> > **Right action.** The identity map pulls back trivially, $\operatorname{id}_P^*\,\omega = \omega$. For the composition law, functoriality of pull-back gives
> > $$(f_1 \circ f_2)^*\omega = f_2^*(f_1^*\omega).$$
> > Writing $\omega \cdot f := f^*\omega$, this reads $\omega \cdot (f_1 f_2) = (\omega \cdot f_1) \cdot f_2$, which is the defining identity of a right action (with $\operatorname{id}_P$ acting trivially). $\blacksquare$

> [!note]- Lemma 4: The gauge descent formula for the connection and the curvature
> **Statement:** Let $f \in \mathcal G(P)$, written $f(p) = p \cdot \hat g(p)$ with $\hat g : P \to G$. Then
> $$f^*\omega = \operatorname{Ad}_{\hat g^{-1}} \omega + \hat g^*\theta, \qquad f^*\Omega_\omega = \operatorname{Ad}_{\hat g^{-1}} \Omega_\omega.$$
>
> **Hint:** Write $f = \Phi \circ (\operatorname{id}, \hat g)$ and apply Lemma 1 with $a = \hat g(p)$; then hit the result with $\omega$, using equivariance for the $dR_a$ part and axiom (2) for the fundamental-field part. For the curvature, use that $\Omega_\omega$ is horizontal.
>
> **Why needed:** This is the computational heart of part (c); the local transformation laws are obtained from it by pulling back along a section, and part (e) is obtained from it by differentiation.
>
> > [!note]- Full proof
> > **Setup.** Write $\hat f : P \to P \times G$, $\hat f(p) = (p, \hat g(p))$, so that $f = \Phi \circ \hat f$ with $\Phi(p, a) = p \cdot a$. For $v \in T_p P$, the chain rule and Lemma 1 with $a = \hat g(p)$ and $w = d\hat g_p(v)$ give
> > $$df_p(v) = d\Phi_{(p, \hat g(p))}\big(v,\, d\hat g_p(v)\big) = dR_{\hat g(p)}(v) + \big((\hat g^*\theta)_p(v)\big)_P\big(f(p)\big),$$
> > where we used $\theta_{\hat g(p)}(d\hat g_p(v)) = (\hat g^*\theta)_p(v)$ (definition of the pull-back of $\theta$) and $\Phi(p, \hat g(p)) = f(p)$.
> >
> > **Apply $\omega$; the connection formula.** Evaluate $\omega_{f(p)}$ on both terms.
> >
> > *First term.* Since $f(p) = p \cdot \hat g(p) = R_{\hat g(p)}(p)$, and writing $a := \hat g(p)$ (a *fixed* group element for fixed $p$),
> > $$\omega_{f(p)}\big(dR_a(v)\big) = (R_a^*\omega)_p(v) = (\operatorname{Ad}_{a^{-1}}\omega)_p(v) = \operatorname{Ad}_{\hat g(p)^{-1}}\big(\omega_p(v)\big) \qquad (\text{axiom (1) for } \omega).$$
> >
> > *Second term.* With $\eta := (\hat g^*\theta)_p(v) \in \mathfrak g$, the second term is $\omega_{f(p)}\big(\eta_P(f(p))\big) = \eta$ by axiom (2) for $\omega$; that is,
> > $$\omega_{f(p)}\Big(\big((\hat g^*\theta)_p(v)\big)_P(f(p))\Big) = (\hat g^*\theta)_p(v) \qquad (\text{axiom (2) for } \omega).$$
> >
> > Adding the two,
> > $$(f^*\omega)_p(v) = \omega_{f(p)}(df_p(v)) = \operatorname{Ad}_{\hat g(p)^{-1}}\big(\omega_p(v)\big) + (\hat g^*\theta)_p(v),$$
> > which is the asserted identity $f^*\omega = \operatorname{Ad}_{\hat g^{-1}}\omega + \hat g^*\theta$.
> >
> > **The curvature formula.** Recall $\Omega_\omega$ is horizontal: $\iota_{\eta_P}\Omega_\omega = 0$ for every $\eta \in \mathfrak g$, i.e. $\Omega_\omega$ vanishes whenever one of its arguments is a fundamental (vertical) vector (see [[Def - Curvature of a Principal Connection]]). For $v_1, v_2 \in T_p P$ write, as above, $df_p(v_i) = dR_a(v_i) + (\eta_i)_P(f(p))$ with $a = \hat g(p)$ and $\eta_i = (\hat g^*\theta)_p(v_i)$. Expanding $\Omega_\omega$ at $f(p)$ bilinearly,
> > $$\Omega_\omega\big(df v_1, df v_2\big) = \Omega_\omega\big(dR_a v_1, dR_a v_2\big) + \Omega_\omega\big(dR_a v_1, (\eta_2)_P\big) + \Omega_\omega\big((\eta_1)_P, dR_a v_2\big) + \Omega_\omega\big((\eta_1)_P, (\eta_2)_P\big).$$
> > The last three terms each have a fundamental (vertical) argument and so vanish by horizontality. In the surviving term $a = \hat g(p)$ is fixed, so
> > $$\Omega_\omega\big(dR_a v_1, dR_a v_2\big) = (R_a^*\Omega_\omega)_p(v_1, v_2) = \operatorname{Ad}_{a^{-1}}\big(\Omega_\omega{}_p(v_1, v_2)\big) \qquad (R_g^*\Omega_\omega = \operatorname{Ad}_{g^{-1}}\Omega_\omega, \text{ from [[Def - Curvature of a Principal Connection]]}).$$
> > Therefore $(f^*\Omega_\omega)_p(v_1, v_2) = \operatorname{Ad}_{\hat g(p)^{-1}}\big(\Omega_\omega{}_p(v_1, v_2)\big)$, i.e. $f^*\Omega_\omega = \operatorname{Ad}_{\hat g^{-1}}\Omega_\omega$. $\blacksquare$

> [!note]- Lemma 5: The Maurer–Cartan form under homomorphisms and along the identity
> **Statement:** Let $\theta$ be the left Maurer–Cartan form of $G$ and $\rho : G \to GL(V)$ a representation with differential $\rho_* : \mathfrak g \to \operatorname{End}V$. For any smooth $\hat g : P \to G$,
> $$\rho_*(\hat g^*\theta) = (\rho \circ \hat g)^*\theta_{GL(V)} = \rho(\hat g)^{-1}\, d(\rho(\hat g)),$$
> where $\theta_{GL(V)}$ is the Maurer–Cartan form of $GL(V)$. Moreover, if $h_t : P \to G$ is smooth with $h_0 \equiv e$ and $\zeta(p) := \frac{d}{dt}\big|_0 h_t(p) \in T_e G = \mathfrak g$, then $\frac{d}{dt}\big|_0 h_t^*\theta = d\zeta$.
>
> **Hint:** A Lie group homomorphism pulls back the target Maurer–Cartan form to $\rho_*$ composed with the source one. For the second part differentiate $(h_t^*\theta)_p(v) = \theta_{h_t(p)}(\partial_v h_t(p))$ in $t$ at $0$, using $\theta_e = \operatorname{id}_{\mathfrak g}$ and $\partial_v h_0 = 0$.
>
> **Why needed:** The first identity turns $g^*\theta$ into the ordinary logarithmic derivative $g^{-1}dg$ inside a representation, which is what makes part (d) reduce to the vector-bundle gauge formula; the second identity supplies the $d\hat\xi$ term in part (e).
>
> > [!note]- Full proof
> > **Homomorphisms and the Maurer–Cartan form.** For a Lie group homomorphism $\rho : G \to GL(V)$ one has $\rho^*\theta_{GL(V)} = \rho_* \circ \theta$ as $\operatorname{End}V$-valued $1$-forms on $G$. Indeed, at $a \in G$ and $w \in T_a G$, write $w = (dL_a)_e(\theta_a(w))$, so a curve realising $w$ is $a\exp(t\,\theta_a(w)) + o(t)$; then
> > $$(\rho^*\theta_{GL(V)})_a(w) = \theta_{GL(V)}\big(d\rho_a(w)\big) = \frac{d}{dt}\Big|_0 \rho(a)^{-1}\rho\big(a\exp(t\,\theta_a(w))\big) = \frac{d}{dt}\Big|_0 \rho\big(\exp(t\,\theta_a(w))\big) = \rho_*(\theta_a(w)),$$
> > using $\theta_{GL(V)}\big|_A(W) = A^{-1}W$ and $\rho(a)^{-1}\rho(a\,c) = \rho(c)$. Pulling back along $\hat g$ and using naturality of $\theta$ under composition, $\rho_*(\hat g^*\theta) = \hat g^*(\rho_*\circ\theta) = \hat g^*(\rho^*\theta_{GL(V)}) = (\rho\circ\hat g)^*\theta_{GL(V)} = \rho(\hat g)^{-1}d(\rho(\hat g))$, the last equality being the matrix formula $\theta_{GL(V)} = A^{-1}dA$.
> >
> > **The derivative along the identity.** For $v \in T_p P$, write $(h_t^*\theta)_p(v) = \theta_{h_t(p)}\big(\partial_v h_t(p)\big)$, where $\partial_v h_t(p)$ denotes the $P$-differential of $p \mapsto h_t(p)$ applied to $v$. Differentiate in $t$ at $t = 0$ by the product rule. The term in which $\frac{d}{dt}$ hits the base point $h_t(p)$ (through $\theta_{h_t(p)}$) is multiplied by $\partial_v h_0(p)$, and $\partial_v h_0(p) = 0$ because $h_0 \equiv e$ is constant in $p$; so that term drops. The surviving term is
> > $$\frac{d}{dt}\Big|_0 (h_t^*\theta)_p(v) = \theta_e\Big(\frac{d}{dt}\Big|_0 \partial_v h_t(p)\Big) = \theta_e\Big(\partial_v \frac{d}{dt}\Big|_0 h_t(p)\Big) = \theta_e\big(d\zeta_p(v)\big) = d\zeta_p(v),$$
> > using $h_0(p) = e$, the equality of mixed partial derivatives (the $t$- and $P$-derivatives of the smooth map $(t, p) \mapsto h_t(p)$ commute), the definition $\zeta = \frac{d}{dt}\big|_0 h_t$, and $\theta_e = \operatorname{id}_{\mathfrak g}$. Hence $\frac{d}{dt}\big|_0 h_t^*\theta = d\zeta$. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> We prove the five parts in turn. Lemmas 1–5 are the ones stated above.
>
> ---
> **Part (a): $\operatorname{Aut}(P)$ is a subgroup, and $f \mapsto \bar f$ is a homomorphism with kernel $\mathcal G(P)$.**
>
> *Subgroup.* The identity $\operatorname{id}_P$ is equivariant, so $\operatorname{id}_P \in \operatorname{Aut}(P)$. If $f, h \in \operatorname{Aut}(P)$ then $f \circ h$ is a diffeomorphism and, for all $p, g$,
> $$(f \circ h)(p \cdot g) = f\big(h(p) \cdot g\big) = f(h(p)) \cdot g = (f \circ h)(p) \cdot g \qquad (\text{equivariance of } h, \text{ then of } f),$$
> so $f \circ h \in \operatorname{Aut}(P)$. For inverses, let $q := f^{-1}(p)$; equivariance of $f$ gives $f(q \cdot g) = f(q) \cdot g = p \cdot g$, and applying $f^{-1}$ yields $f^{-1}(p \cdot g) = q \cdot g = f^{-1}(p) \cdot g$, so $f^{-1} \in \operatorname{Aut}(P)$. Hence $\operatorname{Aut}(P) \le \operatorname{Diff}(P)$.
>
> *Fibres, and the smooth base map.* By Lemma 2 every $f \in \operatorname{Aut}(P)$ carries fibres to fibres and induces a unique smooth $\bar f : M \to M$ with $\pi \circ f = \bar f \circ \pi$. Since $f$ is a diffeomorphism permuting fibres, $\bar f$ is a bijection; the same construction applied to $f^{-1}$ produces $\overline{f^{-1}}$ with $\overline{f^{-1}} \circ \bar f = \operatorname{id}_M = \bar f \circ \overline{f^{-1}}$ (apply $\pi$ to $f^{-1}\circ f = \operatorname{id}_P$), so $\bar f \in \operatorname{Diff}(M)$.
>
> *Homomorphism and kernel.* For $f, h \in \operatorname{Aut}(P)$, both $\bar f \circ \bar h$ and $\overline{f \circ h}$ satisfy $\pi \circ (f \circ h) = (\,\cdot\,) \circ \pi$; by the uniqueness clause of Lemma 2, $\overline{f \circ h} = \bar f \circ \bar h$. So $f \mapsto \bar f$ is a group homomorphism $\operatorname{Aut}(P) \to \operatorname{Diff}(M)$, and by definition $\mathcal G(P) = \{f : \bar f = \operatorname{id}_M\}$ is exactly its kernel, hence a subgroup of $\operatorname{Aut}(P)$.
>
> ---
> **Part (b): $f^*$ preserves $\mathcal A(P)$, is a right action, and is affine.**
>
> By Lemma 3, $f^*\omega \in \mathcal A(P)$ for every $f \in \operatorname{Aut}(P)$ and $\omega \in \mathcal A(P)$, and $\omega \cdot f := f^*\omega$ satisfies $\omega \cdot \operatorname{id}_P = \omega$ and $\omega \cdot (f_1 f_2) = (\omega \cdot f_1) \cdot f_2$; this is precisely a right action of $\operatorname{Aut}(P)$ on $\mathcal A(P)$, and it restricts to a right action of the subgroup $\mathcal G(P)$.
>
> *Affineness.* Let $b \in \Omega^1(M; \operatorname{ad}P)$ with lift $\hat b \in \Omega^1(P; \mathfrak g)$ (the unique horizontal, $\operatorname{Ad}$-equivariant form with $\pi_*\hat b = b$ in the sense of [[Thm - Bundle-Valued Forms on the Base are Basic Equivariant Forms on the Total Space]]). Recall from [[Def - Connection on a Principal Bundle]] that $\mathcal A(P)$ is an affine space: $\omega + \hat b \in \mathcal A(P)$. Since pull-back is $\mathbb R$-linear on forms,
> $$f^*(\omega + \hat b) = f^*\omega + f^*\hat b,$$
> which is the stated affineness. To see that the action on the modelling vector space $\Omega^1(M; \operatorname{ad}P)$ is the pointwise adjoint action, take $f \in \mathcal G(P)$ with $f(p) = p\,\hat g(p)$. We compute $f^*\hat b$ directly, exactly as the connection formula of Lemma 4 was computed but with the horizontal form $\hat b$ in place of $\omega$. Fix $p \in P$ and $v \in T_p P$; writing $a := \hat g(p)$ and $\eta := (\hat g^*\theta)_p(v) \in \mathfrak g$, Lemma 1 (as applied in Lemma 4) gives $df_p(v) = dR_a(v) + \eta_P(f(p))$. Since $\hat b$ is a $1$-form, evaluating it on this single tangent vector is linear, with no bilinear expansion:
> $$(f^*\hat b)_p(v) = \hat b_{f(p)}\big(df_p(v)\big) = \hat b_{f(p)}\big(dR_a(v)\big) + \hat b_{f(p)}\big(\eta_P(f(p))\big) \qquad (\text{linearity of } \hat b_{f(p)}).$$
> The second term vanishes because $\hat b$ is horizontal, so it annihilates the fundamental (vertical) vector $\eta_P(f(p))$. In the first term $a = \hat g(p)$ is a fixed group element for fixed $p$ and $f(p) = R_a(p)$, so
> $$\hat b_{f(p)}\big(dR_a(v)\big) = (R_a^*\hat b)_p(v) = \operatorname{Ad}_{a^{-1}}\big(\hat b_p(v)\big) \qquad (R_g^*\hat b = \operatorname{Ad}_{g^{-1}}\hat b, \text{ the } \operatorname{Ad}\text{-equivariance of } \hat b).$$
> Therefore
> $$f^*\hat b = \operatorname{Ad}_{\hat g^{-1}} \hat b,$$
> which is again horizontal (as $\operatorname{Ad}_{\hat g^{-1}}$ acts on values only) and $\operatorname{Ad}$-equivariant, and so represents the form $\operatorname{Ad}_{\hat g^{-1}} b$ on $M$. Thus $f$ acts on $\mathcal A(P) = \omega_0 + \Omega^1(M; \operatorname{ad}P)$ by an affine map whose linear part is the adjoint action, as claimed.
>
> ---
> **Part (c): naturality of curvature, the explicit formulas, and the local laws.**
>
> *Naturality.* For any $f \in \operatorname{Aut}(P)$, using that $d$ commutes with pull-back (see [[Thm - Pull-Back Commutes with the Exterior Derivative]]) and that pull-back commutes with the bracket of $\mathfrak g$-valued forms,
> $$\Omega_{f^*\omega} = d(f^*\omega) + \tfrac12\big[f^*\omega \wedge f^*\omega\big] = f^*(d\omega) + \tfrac12\, f^*[\omega \wedge \omega] = f^*\Big(d\omega + \tfrac12[\omega \wedge \omega]\Big) = f^*\Omega_\omega.$$
> The identity $[f^*\alpha \wedge f^*\beta] = f^*[\alpha \wedge \beta]$ holds because the bracket of $\mathfrak g$-valued forms combines the wedge of the covector parts (natural under $f^*$) with the Lie bracket of the values (pointwise on $\mathfrak g$, untouched by $f^*$), so $f^*$ passes through it (see [[Def - Lie-Algebra-Valued Differential Forms and Their Bracket]]).
>
> *Explicit formulas.* For $f \in \mathcal G(P)$ with $f(p) = p\,\hat g(p)$, Lemma 4 gives directly
> $$f^*\omega = \operatorname{Ad}_{\hat g^{-1}}\omega + \hat g^*\theta, \qquad f^*\Omega_\omega = \operatorname{Ad}_{\hat g^{-1}}\Omega_\omega.$$
> Combining the second with naturality, $\Omega_{f^*\omega} = f^*\Omega_\omega = \operatorname{Ad}_{\hat g^{-1}}\Omega_\omega$: the curvature of the transformed connection is the conjugate of the old curvature.
>
> *Local laws.* Let $s : U \to P$ be a local section and set $g := \hat g \circ s : U \to G$. Pulling the first formula back by $s$ and using that $\operatorname{Ad}_{\hat g(p)^{-1}}$ acts on values pointwise (so it survives $s^*$ as $\operatorname{Ad}_{g(x)^{-1}}$) together with $s^*(\hat g^*\theta) = (\hat g \circ s)^*\theta = g^*\theta$,
> $$A_{f^*\omega, s} = s^*(f^*\omega) = s^*\big(\operatorname{Ad}_{\hat g^{-1}}\omega\big) + s^*\big(\hat g^*\theta\big) = \operatorname{Ad}_{g^{-1}}(s^*\omega) + g^*\theta = \operatorname{Ad}_{g^{-1}} A_{\omega, s} + g^*\theta.$$
> For a matrix group $\operatorname{Ad}_{g^{-1}} A = g^{-1} A g$ and $g^*\theta = g^{-1}\,dg$, so $A_{f^*\omega, s} = g^{-1} A_{\omega, s}\, g + g^{-1}\,dg$. Likewise, pulling back the curvature formula,
> $$F_{f^*\omega, s} = s^*(f^*\Omega_\omega) = s^*\big(\operatorname{Ad}_{\hat g^{-1}}\Omega_\omega\big) = \operatorname{Ad}_{g^{-1}}(s^*\Omega_\omega) = \operatorname{Ad}_{g^{-1}} F_{\omega, s},$$
> matrix case $g^{-1} F_{\omega, s}\, g$. These are exactly the change-of-trivialisation formulas of [[Thm - Transformation of Local Connection and Curvature Forms]] — which states that under $s_\beta = s_\alpha g_{\alpha\beta}$ one has $A_\beta = \operatorname{Ad}_{g_{\alpha\beta}^{-1}} A_\alpha + g_{\alpha\beta}^*\theta$ and $F_\beta = \operatorname{Ad}_{g_{\alpha\beta}^{-1}} F_\alpha$ — now with the single global function $g = \hat g \circ s$ in place of the transition function. This is the promised identification: **a gauge transformation acts on the local potential by the same formula as a change of trivialisation.**
>
> ---
> **Part (d): compatibility with the vector-bundle gauge action.**
>
> **Step 0 — the objects.** Let $E = P \times_\rho V$. By [[Thm - Sections of an Associated Bundle are Equivariant Functions]], sections $s \in \Gamma(E)$ correspond bijectively to equivariant functions $\hat s \in C^\infty(P; V)$ with $\hat s(p \cdot g) = \rho(g)^{-1}\hat s(p)$, via $s(\pi p) = [p, \hat s(p)]$; the correspondence extends to $E$-valued forms and basic equivariant $V$-valued forms on $P$. By [[Thm - Principal Connections Induce Covariant Derivatives on Associated Bundles]], the induced covariant derivative $\nabla^\omega$ is characterised on equivariant functions by
> $$\widehat{\nabla^\omega s} = d\hat s + \rho_*(\omega)\,\hat s \qquad (\text{the horizontal, } \rho\text{-equivariant representative of } \nabla^\omega s).$$
> The induced gauge transformation $\gamma(f) \in \mathcal G(E)$ is $\gamma(f)[p, v] = [f(p), v]$; it is well defined because $[f(p \cdot g), \rho(g)^{-1}v] = [f(p) \cdot g, \rho(g)^{-1}v] = [f(p), v]$ (equivariance of $f$ and the relation defining $E$), and it covers $\operatorname{id}_M$ because $\bar f = \operatorname{id}_M$.
>
> **Step 1 — $\gamma(f)$ acts by $\rho(\hat g)$ on equivariant functions.** For $s \leftrightarrow \hat s$ and $f(p) = p\,\hat g(p)$,
> $$(\gamma(f) s)(\pi p) = \gamma(f)\,[p, \hat s(p)] = [f(p), \hat s(p)] = [p\,\hat g(p), \hat s(p)] = [p,\, \rho(\hat g(p))\,\hat s(p)],$$
> the last step by the defining relation $[p \cdot a, v] = [p, \rho(a) v]$ with $a = \hat g(p)$. Hence $\widehat{\gamma(f) s} = \rho(\hat g)\,\hat s$, and $\widehat{\gamma(f)^{-1} s} = \rho(\hat g)^{-1}\hat s$.
>
> **Step 2 — compute $\gamma(f)^{-1}\nabla^\omega\gamma(f)$ on equivariant functions.** Fix $s \leftrightarrow \hat s$. Put $t := \gamma(f) s$, so $\hat t = \rho(\hat g)\,\hat s$. Then
> $$\widehat{\nabla^\omega t} = d\hat t + \rho_*(\omega)\,\hat t = d\big(\rho(\hat g)\,\hat s\big) + \rho_*(\omega)\,\rho(\hat g)\,\hat s \qquad (\text{characterisation of } \nabla^\omega).$$
> Applying $\gamma(f)^{-1}$, i.e. multiplying the equivariant function by $\rho(\hat g)^{-1}$,
> $$\widehat{\gamma(f)^{-1}\nabla^\omega\gamma(f)\, s} = \rho(\hat g)^{-1}\Big(d\big(\rho(\hat g)\,\hat s\big) + \rho_*(\omega)\,\rho(\hat g)\,\hat s\Big).$$
> Expand the two pieces. By the Leibniz rule and Lemma 5 (first identity, $\rho(\hat g)^{-1}d(\rho(\hat g)) = \rho_*(\hat g^*\theta)$),
> $$\rho(\hat g)^{-1}\, d\big(\rho(\hat g)\,\hat s\big) = \rho(\hat g)^{-1}\big(d(\rho(\hat g))\,\hat s + \rho(\hat g)\, d\hat s\big) = \rho_*(\hat g^*\theta)\,\hat s + d\hat s.$$
> By the conjugation identity $\rho(a)^{-1}\rho_*(X)\rho(a) = \rho_*(\operatorname{Ad}_{a^{-1}}X)$ (differentiate $\rho(a^{-1}\exp(sX)a) = \rho(a)^{-1}\rho(\exp sX)\rho(a)$ at $s = 0$), with $a = \hat g$,
> $$\rho(\hat g)^{-1}\,\rho_*(\omega)\,\rho(\hat g)\,\hat s = \rho_*\big(\operatorname{Ad}_{\hat g^{-1}}\omega\big)\,\hat s.$$
> Adding,
> $$\widehat{\gamma(f)^{-1}\nabla^\omega\gamma(f)\, s} = d\hat s + \rho_*\big(\operatorname{Ad}_{\hat g^{-1}}\omega + \hat g^*\theta\big)\,\hat s = d\hat s + \rho_*(f^*\omega)\,\hat s = \widehat{\nabla^{f^*\omega} s},$$
> using $f^*\omega = \operatorname{Ad}_{\hat g^{-1}}\omega + \hat g^*\theta$ from part (c) and the characterisation of $\nabla^{f^*\omega}$.
>
> **Step 3 — conclude.** The equivariant functions of $\gamma(f)^{-1}\nabla^\omega\gamma(f)\, s$ and of $\nabla^{f^*\omega} s$ agree for every $s$; since $s \mapsto \hat s$ is a bijection, $\nabla^{f^*\omega} = \gamma(f)^{-1} \circ \nabla^\omega \circ \gamma(f)$. This is exactly the vector-bundle gauge action $\nabla \mapsto \gamma(f)^{-1}\nabla\,\gamma(f)$ of [[Def - Gauge Group of a Vector Bundle]] (where $\nabla^h s = h^{-1}\nabla(hs)$), so the principal action and the chapter-II vector-bundle action agree.
>
> ---
> **Part (e): the infinitesimal action is $\xi \mapsto d^{\nabla_\omega}\xi$.**
>
> **Step 0 — the flow is gauge.** Let $\xi \in \Gamma(\operatorname{ad}P) \leftrightarrow \hat\xi : P \to \mathfrak g$ with $\hat\xi(p \cdot g) = \operatorname{Ad}_{g^{-1}}\hat\xi(p)$. Set $f_t(p) := p \cdot \exp(t\,\hat\xi(p))$. Then $f_t$ is equivariant:
> $$f_t(p \cdot g) = (p \cdot g)\exp\big(t\,\hat\xi(pg)\big) = pg\,\exp\big(t\,\operatorname{Ad}_{g^{-1}}\hat\xi(p)\big) = pg\, g^{-1}\exp(t\,\hat\xi(p))\, g = p\,\exp(t\,\hat\xi(p))\cdot g = f_t(p)\cdot g,$$
> using $\exp(\operatorname{Ad}_{g^{-1}}X) = g^{-1}\exp(X)g$. The map $(t, p) \mapsto f_t(p)$ is smooth, being the composition of the smooth maps $p \mapsto (p, t\hat\xi(p))$, $\exp$, and the action.
> 
> *Each $f_t$ is a diffeomorphism.* The key fact is that $\hat\xi$ is constant along the flow generated by $f_t$: for every $p$,
> $$\hat\xi\big(f_t(p)\big) = \hat\xi\big(p \cdot \exp(t\hat\xi(p))\big) = \operatorname{Ad}_{\exp(t\hat\xi(p))^{-1}}\hat\xi(p) = \operatorname{Ad}_{\exp(-t\hat\xi(p))}\hat\xi(p) = \hat\xi(p),$$
> where the second equality is the equivariance $\hat\xi(p \cdot g) = \operatorname{Ad}_{g^{-1}}\hat\xi(p)$ with $g = \exp(t\hat\xi(p))$, and the last equality is $\operatorname{Ad}_{\exp(-tX)}X = X$ (the adjoint action of a one-parameter subgroup fixes its own generator, since $\operatorname{Ad}_{\exp(sX)} = \exp(s\,\operatorname{ad}_X)$ and $\operatorname{ad}_X X = [X, X] = 0$). Consequently the smooth map $k_t(p) := p \cdot \exp(-t\hat\xi(p))$ is a two-sided inverse of $f_t$:
> $$k_t\big(f_t(p)\big) = f_t(p)\cdot\exp\big(-t\hat\xi(f_t(p))\big) = p\cdot\exp(t\hat\xi(p))\cdot\exp(-t\hat\xi(p)) = p \qquad (\hat\xi(f_t(p)) = \hat\xi(p)),$$
> and symmetrically $f_t(k_t(p)) = p$ by the same computation with $t \mapsto -t$ (which gives $\hat\xi(k_t(p)) = \hat\xi(p)$). Hence $f_t$ is a diffeomorphism with smooth inverse $k_t = f_{-t}$.
> 
> *The remaining gauge conditions.* Since $f_t(p) = p\cdot\exp(t\hat\xi(p))$ lies in the same fibre as $p$, we have $\pi(f_t(p)) = \pi(p)$, so $\bar f_t = \operatorname{id}_M$ and $f_t$ covers the identity; and $f_0(p) = p\cdot\exp(0) = p$, so $f_0 = \operatorname{id}_P$. Combined with equivariance, $f_t \in \mathcal G(P)$, with fibre-coordinate function $\hat g_t := \exp(t\hat\xi)$ (that is, $f_t(p) = p\cdot\hat g_t(p)$).
>
> **Step 1 — differentiate the two terms of part (c).** By Lemma 4, $f_t^*\omega = \operatorname{Ad}_{\hat g_t^{-1}}\omega + \hat g_t^*\theta$ with $\hat g_t = \exp(t\hat\xi)$, so $\hat g_t^{-1} = \exp(-t\hat\xi)$.
>
> *The adjoint term.* Since $\frac{d}{dt}\big|_0 \operatorname{Ad}_{\exp(-t\hat\xi(p))} = \operatorname{ad}_{-\hat\xi(p)} = -\operatorname{ad}_{\hat\xi(p)}$ (the differential of $\operatorname{Ad}\circ\exp$ at $0$ is $\operatorname{ad}$; see [[Thm - Ad is a Smooth Representation and its Differential is ad]]),
> $$\frac{d}{dt}\Big|_0 \operatorname{Ad}_{\hat g_t^{-1}}\omega = -\operatorname{ad}_{\hat\xi}\,\omega = -[\hat\xi, \omega],$$
> the $\mathfrak g$-valued $1$-form $(-[\hat\xi, \omega])(v) = -[\hat\xi, \omega(v)]$.
>
> *The Maurer–Cartan term.* Apply Lemma 5 (second identity) with $h_t = \exp(t\hat\xi)$: here $h_0 \equiv e$ and $\zeta = \frac{d}{dt}\big|_0 \exp(t\hat\xi) = \hat\xi$, so
> $$\frac{d}{dt}\Big|_0 \hat g_t^*\theta = d\hat\xi.$$
>
> **Step 2 — assemble and identify with $d^{\nabla_\omega}$.** Adding the two derivatives,
> $$\frac{d}{dt}\Big|_0 f_t^*\omega = d\hat\xi - [\hat\xi, \omega] = d\hat\xi + [\omega, \hat\xi],$$
> where the last equality is antisymmetry of the bracket, $-[\hat\xi, \omega(v)] = [\omega(v), \hat\xi]$. Now recall that the exterior covariant derivative on $\operatorname{ad}P$-valued forms is, for the adjoint representation ($\rho = \operatorname{Ad}$, $\rho_* = \operatorname{ad}$), given on the type-$\operatorname{Ad}$ zero-form $\hat\xi$ by $D^\omega\hat\xi = d\hat\xi + \operatorname{ad}_\omega\hat\xi = d\hat\xi + [\omega, \hat\xi]$ (see [[Def - Exterior Covariant Derivative on a Principal Bundle]]), and $D^\omega\hat\xi = \widehat{d^{\nabla_\omega}\xi}$ is the lift of $d^{\nabla_\omega}\xi \in \Omega^1(M; \operatorname{ad}P)$. Therefore
> $$\frac{d}{dt}\Big|_0 f_t^*\omega = d\hat\xi + [\omega, \hat\xi] = D^\omega\hat\xi = \widehat{d^{\nabla_\omega}\xi},$$
> i.e. the infinitesimal action is $\xi \mapsto d^{\nabla_\omega}\xi \in \Omega^1(M; \operatorname{ad}P)$.
>
> This completes parts (a)–(e). $\blacksquare$

> [!warning] Convention: the sign of the infinitesimal action
> Haydys states (Exercise 63, page 22) that the infinitesimal action of the gauge group is $(a, \xi) \mapsto -d_a\xi$, and prints its target as $\Omega^0(\operatorname{ad}P)$. The target is a typographical slip: $d_a\xi \in \Omega^1(\operatorname{ad}P)$, and we use the corrected target $\Omega^1(M; \operatorname{ad}P)$. The sign is a genuine convention choice, not an error. With the series' convention — the pull-back is a **right** action $\omega \cdot f := f^*\omega$, and the generating family is $f_t(p) = p\exp(t\hat\xi(p))$ — the direct computation above yields $\frac{d}{dt}\big|_0 f_t^*\omega = +\,d^{\nabla_\omega}\xi$. Haydys's $-d_a\xi$ is the same map read for the opposite (left-action) convention, equivalently the generator obtained from $f_t(p) = p\exp(-t\hat\xi(p))$; the two differ only by the overall sign that flips when a right action is rewritten as a left action. Throughout this series the infinitesimal gauge action is $\xi \mapsto +\,d^{\nabla_\omega}\xi$.

---

# Cross-Field Exercise Suggestions

**Electromagnetism as the abelian case.** On a Hermitian line bundle $L \to M$ with structure group $U(1)$, take a gauge transformation $g : M \to U(1)$, $g = e^{i\chi}$. Because $U(1)$ is abelian, $\operatorname{Ad}$ is trivial and $\theta = g^{-1}\,dg = i\,d\chi$, so part (c) reduces to $A \mapsto A + i\,d\chi$ and $F \mapsto F$. This reproduces exactly the classical gauge freedom $A_\mu \mapsto A_\mu + \partial_\mu\chi$ of the electromagnetic potential and the gauge invariance of the field strength $F = dA$. The theorem applies because the physical gauge transformation is literally a section of $\operatorname{Ad}P = M \times U(1)$; what is non-obvious to a physicist is that the inhomogeneous term $d\chi$ is the Maurer–Cartan form of $U(1)$ and that its absence from the field-strength law is the abelian shadow of horizontality.

**The Wilson loop and holonomy conjugation.** In lattice and continuum gauge theory one studies the trace of the holonomy $\operatorname{tr}\operatorname{Hol}_c(\omega)$ around a loop $c$. Under a gauge transformation the holonomy conjugates, $\operatorname{Hol}_c(f^*\omega) = \hat g(p)^{-1}\operatorname{Hol}_c(\omega)\,\hat g(p)$, which is the integrated form of part (c)'s $\operatorname{Ad}_{\hat g^{-1}}$ law; hence $\operatorname{tr}\operatorname{Hol}_c$ is a gauge-invariant observable. The theorem applies because parallel transport is built from the connection and part (c) controls how the connection moves; the non-obvious point is that only *conjugation-invariant* functions of the holonomy, not the holonomy itself, are physical.

**Deformation theory of flat connections.** For a flat connection ($F_\omega = 0$) on a bundle over a surface, the tangent space to the moduli space of flat connections modulo gauge is $H^1$ of the complex $\Omega^0(\operatorname{ad}P) \xrightarrow{d^{\nabla_\omega}} \Omega^1(\operatorname{ad}P) \xrightarrow{d^{\nabla_\omega}} \Omega^2(\operatorname{ad}P)$. The first map is exactly the infinitesimal gauge action of part (e); dividing the space of connection-preserving deformations ($\ker$ of the second map) by the infinitesimal gauge directions ($\operatorname{im}$ of the first) gives the moduli tangent space. The theorem applies because part (e) identifies the infinitesimal gauge orbit with the image of $d^{\nabla_\omega}$; the non-obvious content is that the "unphysical" directions are precisely a coboundary, so the physical deformations are a cohomology group.

---

# Bridges

- **[[Thm - Transformation of Local Connection and Curvature Forms]]** — the change-of-trivialisation law. That theorem transforms the local forms under a change of *section* $s_\beta = s_\alpha g_{\alpha\beta}$ with the transition function $g_{\alpha\beta}$; part (c) shows a gauge transformation produces the identical law with $g = \hat g \circ s$, a single global function, in place of $g_{\alpha\beta}$. The construction is: pull the global identity $f^*\omega = \operatorname{Ad}_{\hat g^{-1}}\omega + \hat g^*\theta$ back along a fixed section and read off that the section stays put while its group-valued relabelling $g$ produces the inhomogeneous Maurer–Cartan term. This is the geometric content of Haydys's remark R2.1.9 that the frame-change formula and the gauge-action formula coincide.

- **[[Thm - Gauge Action on Connection Matrices]]** — the vector-bundle predecessor. On a vector bundle the gauge group $\mathcal G(E) \subseteq \Gamma(\operatorname{End}E)$ acts by $\nabla^h s = h^{-1}\nabla(hs)$, so the connection matrix transforms by $A \mapsto h^{-1}Ah + h^{-1}dh$. Part (d) shows this is not a separate theory: taking $E = P \times_\rho V$ and $h = \gamma(f)$, the principal gauge action induces exactly this vector-bundle action, so the two are one operation seen through a representation.

- **[[Thm - The Gauge Group is the Space of Sections of the Adjoint Group Bundle]]** — the identification of the acting group. It supplies the isomorphism $\mathcal G(P) \cong \Gamma(\operatorname{Ad}P)$ that turns the abstract automorphism $f$ into the concrete function $\hat g$ used throughout part (c). The construction is $f(p) = p\,\hat g(p) \leftrightarrow$ the section $\pi(p) \mapsto [p, \hat g(p)]$ of $\operatorname{Ad}P$; the equivariance $\hat g(pg) = g^{-1}\hat g(p)g$ that makes the formulas of part (c) well defined is exactly the equivariance defining a section of $\operatorname{Ad}P$.

- **[[Thm - The Reduced Gauge Group Acts Freely on Connections]]** — the sequel that makes quotients manageable. Parts (a) and (b) establish that $\mathcal G(P)$ acts on $\mathcal A(P)$; the reduced gauge group $\mathcal G_b(P)$ (fixing a fibre) then acts *freely*, which is proved by lifting a path horizontally and using that a gauge transformation fixing a connection preserves its horizontal distribution. This freeness is what lets one build the quotient $\mathcal A/\mathcal G$ as a manifold away from reducibles.

- **[[Def - Exterior Covariant Derivative on a Principal Bundle]]** — the target of the infinitesimal action. Part (e) identifies the generator of the gauge flow with $d^{\nabla_\omega} : \Omega^0(M; \operatorname{ad}P) \to \Omega^1(M; \operatorname{ad}P)$. Reading this backwards, the exterior covariant derivative *is* the linearisation of the gauge action, which is why the deformation complex of a connection begins with $d^{\nabla_\omega}$ and why its cohomology measures gauge-inequivalent infinitesimal deformations.

---

# Unlocked by This

> [!tip] Gauge invariance of Chern–Weil forms *(from Chern–Weil theory, chapter VI)*
> Because $F_{f^*\omega, s} = \operatorname{Ad}_{g^{-1}} F_{\omega, s}$, any $\operatorname{Ad}$-invariant polynomial $q$ satisfies $q(F_{f^*\omega}) = q(F_\omega)$, so the Chern–Weil forms are gauge invariant and their cohomology classes are invariants of the bundle, independent of the connection. See **Def - Chern-Weil Form of an Invariant Polynomial**.

> [!tip] The Yang–Mills functional on the quotient *(from Yang–Mills theory, chapter VII)*
> The homogeneous curvature law makes $|F_\omega|^2$ gauge invariant for an $\operatorname{Ad}$-invariant inner product on $\mathfrak g$, so the Yang–Mills energy $\mathcal{YM}(\omega) = \tfrac12\int_M |F_\omega|^2$ descends to a function on $\mathcal A/\mathcal G$, and its critical points are the Yang–Mills connections. See **Def - The Yang-Mills Functional**.

> [!tip] The configuration space of gauge theory *(from moduli theory, chapters X, XI, XIII)*
> Parts (a), (b), and the freeness sequel turn the affine space $\mathcal A(P)$ into a principal-bundle-like object over the quotient $\mathcal B = \mathcal A/\mathcal G$, the true configuration space on which instanton and Seiberg–Witten moduli spaces are cut out. See **Def - The Configuration Space of Connections Modulo Gauge**.
