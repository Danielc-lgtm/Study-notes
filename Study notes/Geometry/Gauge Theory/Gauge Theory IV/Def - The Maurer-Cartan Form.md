---
type: definition
subject: gauge-theory
prereqs:
  - "Def - Left and Right Translations and Conjugation on a Lie Group"
  - "Def - Lie-Algebra-Valued Differential Forms and Their Bracket"
  - "Def - Left-Invariant Vector Field"
  - "Thm - Ad is a Smooth Representation and its Differential is ad"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $G$ is a Lie group with identity $e$ and Lie algebra $\mathfrak{g} = T_eG$, the tangent space at the identity, carrying the bracket of [[Def - Left-Invariant Vector Field|left-invariant vector fields]] (for a matrix group this bracket is the commutator $[X,Y] = XY - YX$). For $g \in G$ the **left translation** $L_g : G \to G$ is $L_g(h) = gh$ and the **right translation** is $R_g(h) = hg$; the **conjugation** is $\alpha_g = L_g \circ R_{g^{-1}}$, $\alpha_g(h) = ghg^{-1}$, all as on [[Def - Left and Right Translations and Conjugation on a Lie Group|the translations page]]. For a smooth map $F : M \to N$ and a point $p \in M$ we write $d_pF : T_pM \to T_{F(p)}N$ for the **differential** of $F$ at $p$ (the vault's differential-geometry chapters write $dF_p$ for the same linear map; this page follows Bär's placement of the point as a subscript on $d$). The **adjoint representation** is $\operatorname{Ad} : G \to GL(\mathfrak{g})$, $\operatorname{Ad}_g = d_e\alpha_g$, with $\operatorname{Ad}_{g^{-1}} = (\operatorname{Ad}_g)^{-1}$; for a matrix group $\operatorname{Ad}_g X = gXg^{-1}$, all proved on [[Thm - Ad is a Smooth Representation and its Differential is ad|the adjoint-representation page]]. For $\xi \in \mathfrak{g}$ we write $\tilde{\xi} \in \mathfrak{X}(G)$ for the [[Def - Left-Invariant Vector Field|left-invariant vector field]] with $\tilde{\xi}(e) = \xi$, so that $\tilde{\xi}(g) = d_eL_g(\xi)$.

We write $\Omega^1(G; \mathfrak{g}) = \Omega^1(G) \otimes \mathfrak{g}$ for the space of $\mathfrak{g}$-valued 1-forms on $G$, in the sense of [[Def - Lie-Algebra-Valued Differential Forms and Their Bracket|the Lie-algebra-valued forms page]]: a $\mathfrak{g}$-valued 1-form $\alpha$ assigns to each $g \in G$ a linear map $\alpha_g : T_gG \to \mathfrak{g}$, its exterior derivative $d\alpha$ and its bracket $[\alpha \wedge \beta]$ are computed component by component against a basis of $\mathfrak{g}$, and $[\alpha \wedge \alpha](X,Y) = 2[\alpha(X), \alpha(Y)]$ for a 1-form $\alpha$. The pull-back of $\alpha \in \Omega^1(G; \mathfrak{g})$ by a smooth map $F$ is $F^*\alpha$, $(F^*\alpha)_p(v) = \alpha_{F(p)}(d_pF(v))$.

> [!warning] Convention: symbol for the form
> Bär (Remark 2.5.9) writes $\phi \in \Omega^1(G; \mathfrak{g})$, $\phi_g := dL_{g^{-1}}$, for the object this page calls the Maurer–Cartan form; the series writes $\theta$, following the notation of `conventions.md` (where $\theta$ is the left Maurer–Cartan form appearing in every local transformation law $A_{s'} = \operatorname{Ad}_{g^{-1}} A_s + g^*\theta$). Bär's $\phi$ is our $\theta$; his $\phi_g$ is our $\theta_g = d_gL_{g^{-1}}$. The subscript on $\theta_g$ denotes the value of the form at the point $g$, a linear map $T_gG \to \mathfrak{g}$; it has nothing to do with the orbit-diffeomorphism notation $\theta_g : M \to M$ that the series uses on other pages for the map a group element induces on a $G$-manifold.

> [!warning] Convention: Haydys' letters
> Haydys writes $\operatorname{ad}$ (lower case) for what the series and Bär write $\operatorname{Ad}$ (the group representation on $\mathfrak{g}$), reserving nothing separate for the algebra map $\operatorname{ad}_X = [X, \cdot]$; he writes $a$ for a connection 1-form where the series writes $A$. On this page $\operatorname{Ad}_g X = gXg^{-1}$ is the group adjoint and $g^{-1}dg$ is the matrix Maurer–Cartan form; where a Haydys formula is quoted the letter is converted silently to the series convention.

---

# Axiom Motivation

A Lie group is a manifold whose points can be compared with one another by the group law, and the [[Def - Left-Invariant Vector Field|left-invariant vector fields]] are the record of that comparison: a tangent vector $\xi \in \mathfrak{g} = T_eG$ at the identity is spread over the whole group by left translation, $\tilde{\xi}(g) = d_eL_g(\xi)$, giving the canonical trivialisation $TG \cong G \times \mathfrak{g}$, $(g, \xi) \mapsto d_eL_g(\xi)$. The Maurer–Cartan form is the one object that reverses this construction. It answers the question: given an honest tangent vector $v$ at a point $g$ — the velocity of some curve through $g$, with no left-invariance assumed — which element of $\mathfrak{g}$ does it correspond to under the canonical trivialisation? The answer must be to translate $v$ back to the identity, and the only translation that sends $g$ to $e$ and is dictated by the group structure is $L_{g^{-1}}$. So we are forced to set $\theta_g(v) = d_gL_{g^{-1}}(v) \in T_eG = \mathfrak{g}$.

The concrete meaning is cleanest for a curve. If $g(t)$ is a path in $G$ with $g(0) = g$ and velocity $\dot{g}(0) = v$, then $\theta_g(v) = d_gL_{g^{-1}}(\dot{g}(0))$ is the velocity of the *translated* curve $L_{g^{-1}}(g(t)) = g^{-1}g(t)$ at $t = 0$, a curve through $e$; it measures the motion of $g(t)$ **as seen from the identity**, having undone the position $g$. For a matrix group this is literally $g^{-1}\dot{g}$, the logarithmic derivative, and it is exactly the quantity that appears in rigid-body mechanics as the angular velocity expressed in the body frame: the world-frame velocity $\dot{g}$ is a matrix in $T_gG$, and left-multiplying by $g^{-1}$ carries it to the Lie algebra, where it can be compared across time. The Maurer–Cartan form is the coordinate-free, all-groups version of "multiply the velocity by $g^{-1}$ to read it in the body frame."

Why translate on the *left*, and why must the output live in $\mathfrak{g}$ rather than in some ambient vector space? These are the two clauses of the construction, and each can be tested by dropping it. **If we translate on the right instead**, setting $\vartheta_g(v) = d_gR_{g^{-1}}(v)$, we obtain a genuinely different form — the *right* Maurer–Cartan form, equal to $dg\,g^{-1}$ for matrix groups. It is not wrong, but it is a different object: it is right-invariant rather than left-invariant, and it transforms under the two translations with the roles of $L$ and $R$ exchanged. On a non-abelian group the two forms disagree at every point where $v$ does not commute with $g$, and the non-example at the end of the page exhibits the disagreement explicitly; the whole theory of connections built in this chapter uses the left form, because a principal connection is normalised by $\omega(\xi_P) = \xi$ using the left action of $\mathfrak{g}$ on the fibre. **If we let the output live in the ambient tangent space $T_gG$ rather than in the fixed vector space $\mathfrak{g}$**, we have not built anything at all: $\theta$ would be the identity map $T_gG \to T_gG$ at each point, the tautological "form" that carries no information, because it has not committed to a single target in which values at different points can be added and compared. The point of $\theta$ is precisely that its values at $g_1$ and at $g_2$ both lie in the *one* vector space $\mathfrak{g}$, so that expressions like $d\theta + \tfrac{1}{2}[\theta \wedge \theta]$ (the Maurer–Cartan equation of the next page) make sense.

There is a third, structural way to see why the definition is forced, and it doubles as a uniqueness statement. We want a $\mathfrak{g}$-valued 1-form on $G$ that is left-invariant (so that it is intrinsic to the group, not an arbitrary choice) and that reads off the trivialisation correctly at the identity, meaning $\theta_e = \operatorname{id}_{\mathfrak{g}}$. There is exactly one such form: left-invariance forces $\theta_g = \theta_e \circ d_gL_{g^{-1}} = d_gL_{g^{-1}}$ (the corollary below proves the invariance from the formula, and this paragraph runs the implication in reverse to show the formula is the *only* candidate), so the requirement $\theta_e = \operatorname{id}$ together with left-invariance pins the form down completely. A reader who understood that "the Lie algebra is the space of left-invariant fields" would arrive at "the Maurer–Cartan form is the dual object: the left-invariant $\mathfrak{g}$-valued 1-form that is the identity at $e$" without being handed the formula, and would then *derive* $\theta_g = d_gL_{g^{-1}}$.

---

# The Definition

Let $G$ be a Lie group with Lie algebra $\mathfrak{g} = T_eG$. The **(left) Maurer–Cartan form** of $G$ is the $\mathfrak{g}$-valued 1-form
$$\theta \in \Omega^1(G; \mathfrak{g}), \qquad \theta_g := d_gL_{g^{-1}} : T_gG \to T_eG = \mathfrak{g},$$
whose value at $g \in G$ is the differential at $g$ of left translation by $g^{-1}$. Since $L_{g^{-1}}(g) = g^{-1}g = e$, this differential maps $T_gG$ into $T_eG = \mathfrak{g}$, so $\theta_g$ does take values in $\mathfrak{g}$; and $d_gL_{g^{-1}}$ is a linear isomorphism onto $\mathfrak{g}$ with inverse $d_eL_g$ (part (iv) of [[Def - Left and Right Translations and Conjugation on a Lie Group|the translations page]]), so $\theta_g$ is a linear isomorphism at every point. Smoothness of $\theta$ as a form on $G$ is the statement that $g \mapsto \theta_g$ is a smooth section of $T^*G \otimes \mathfrak{g}$; it holds because $(g, v) \mapsto d_gL_{g^{-1}}(v)$ is the composition of the smooth multiplication and inversion maps of $G$ with the differential, all of which are smooth, and it is exhibited concretely below on $U(1)$, on $SU(2)$, and for matrix groups as $g^{-1}dg$.

The form admits three equivalent descriptions, each used somewhere in this chapter; the corollaries in the Examples section prove that each is the same object as the primary definition.

1. **The left-invariant identity form.** $\theta$ is the unique $\mathfrak{g}$-valued 1-form on $G$ that is left-invariant, $L_h^*\theta = \theta$ for all $h \in G$, and satisfies $\theta_e = \operatorname{id}_{\mathfrak{g}}$. (Existence is the primary definition; uniqueness is the argument in the last paragraph of Axiom Motivation.)

2. **The dual of the left-invariant frame.** $\theta$ is the $\mathfrak{g}$-valued 1-form characterised by
$$\theta(\tilde{\xi}) = \xi \qquad \text{for every } \xi \in \mathfrak{g},$$
where $\tilde{\xi}$ is the [[Def - Left-Invariant Vector Field|left-invariant vector field]] with $\tilde{\xi}(e) = \xi$; that is, on the moving frame of left-invariant fields $\theta$ returns the constant coordinate. Fixing a basis $(\xi_1, \dots, \xi_n)$ of $\mathfrak{g}$ and the dual left-invariant coframe $(\theta^1, \dots, \theta^n)$ of ordinary 1-forms defined by $\theta^a(\tilde{\xi}_b) = \delta^a_b$, this says $\theta = \sum_{a=1}^n \theta^a \otimes \xi_a$.

3. **The matrix form.** If $G \subseteq GL_n(\mathbb{K})$ is a matrix Lie group ($\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$), let $g : G \hookrightarrow M_n(\mathbb{K})$ denote the inclusion, an $M_n(\mathbb{K})$-valued function on $G$, and $dg$ its differential (the $M_n(\mathbb{K})$-valued 1-form $v \mapsto v$ for $v \in T_gG \subseteq M_n(\mathbb{K})$). Then
$$\theta = g^{-1}\,dg,$$
the matrix product of the inverse matrix $g^{-1}$ with the matrix of coordinate differentials.

---

# Categorical / Structural Definition

The Maurer–Cartan form is the intrinsic inverse of the canonical trivialisation of $TG$. The left-invariant frame furnishes a bundle isomorphism
$$\Phi : G \times \mathfrak{g} \xrightarrow{\ \cong\ } TG, \qquad \Phi(g, \xi) = d_eL_g(\xi) = \tilde{\xi}(g),$$
covering the identity on $G$; this is the statement that the tangent bundle of a Lie group is trivial ([[Def - Left-Invariant Vector Field|the left-invariant vector field page]]). Its inverse $\Phi^{-1} : TG \to G \times \mathfrak{g}$ has the shape $v \mapsto (g, \theta_g(v))$ for $v \in T_gG$, because $\Phi^{-1}(v) = (g, \xi)$ requires $d_eL_g(\xi) = v$, hence $\xi = d_gL_{g^{-1}}(v) = \theta_g(v)$ (using $d_gL_{g^{-1}} = (d_eL_g)^{-1}$). Reading off the $\mathfrak{g}$-component of $\Phi^{-1}$ is exactly the assignment $v \mapsto \theta_g(v)$: **the Maurer–Cartan form is the $\mathfrak{g}$-valued 1-form $\theta = \operatorname{pr}_{\mathfrak{g}} \circ \Phi^{-1}$, the second component of the canonical trivialisation.** In this sense $\theta$ is the *solder form* (or *tautological form*) of the group: the 1-form that identifies each tangent space with the model vector space $\mathfrak{g}$, canonically and compatibly with left translation.

This is also the reason the product connection on a trivial principal bundle $M \times G \to M$ is $\operatorname{pr}_2^*\theta$: the fibres of $M \times G$ are copies of $G$, each already coordinatised by $\mathfrak{g}$ through its own solder form, and pulling $\theta$ back along the projection $\operatorname{pr}_2 : M \times G \to G$ produces a $\mathfrak{g}$-valued 1-form that is the identity on vertical vectors and vanishes on the horizontal factor — precisely a [[Def - Connection on a Principal Bundle|connection form]], the flat "reference" connection against which every other is measured.

---

# Relate to Other Fields / Compression

The Maurer–Cartan form is the invariant home of several objects that look unrelated until they are recognised as $\theta$ in disguise.

**In rigid-body mechanics** it is the body angular velocity. A rotating rigid body is a curve $g(t) \in SO(3)$; its spatial angular velocity is $\dot{g}g^{-1}$ (right form) and its body angular velocity is $g^{-1}\dot{g} = \theta(\dot{g})$ (left form). The whole Euler-equation formalism is the statement that dynamics is cleaner in the body frame, that is, cleaner after applying $\theta$.

**In gauge theory** it is the *pure-gauge potential*. A gauge transformation of the trivial bundle is a map $g : U \to G$, and the connection potential it produces out of the vacuum is $A = g^{-1}dg = g^*\theta$, the pull-back of the Maurer–Cartan form. Every local transformation law of a connection carries a $g^*\theta$ term — this is the content of `conventions.md`'s $A_{s'} = \operatorname{Ad}_{g^{-1}} A_s + g^*\theta$ — and the algebraic identity that makes those laws consistent on triple overlaps is the pull-back product rule (Corollary E below). The Maurer–Cartan form is therefore the single object behind every "$g^{-1}dg$" the reader will meet in this chapter.

**In differential topology** its pull-back detects degree. For a map $g : \Sigma \to G$ from a closed manifold, integrals of wedge powers of $g^*\theta$ against $\operatorname{Ad}$-invariant polynomials are homotopy invariants; the winding number of a map $S^1 \to U(1)$ is $\frac{1}{2\pi i}\int_{S^1} g^*(z^{-1}dz)$, and the degree of a map $S^3 \to SU(2)$ is $\frac{1}{24\pi^2}\int_{S^3} \operatorname{tr}\big((g^*\theta)^{\wedge 3}\big)$, the object that will govern the Chern–Simons functional in chapter VI.

**True name.** The official definition, $\theta_g = d_gL_{g^{-1}}$, is already the operational one: *the Maurer–Cartan form is the operator "translate the velocity back to the identity by $g^{-1}$."* For a matrix group the operational form is the logarithmic derivative $g \mapsto g^{-1}dg$, and evaluated along a curve it is $g^{-1}\dot{g}$, the velocity read in the body frame. No separate operational characterisation is needed: to apply $\theta$ is to left-translate to $e$.

---

# Examples / Corollaries

The four defining properties of $\theta$ — left-invariance, its transformation under right translation, its value on the left-invariant frame, and its matrix form — are corollaries of the definition, proved here in full; then three verified examples and one verified non-example.

**Corollary A (left-invariance).** $L_h^*\theta = \theta$ for every $h \in G$.

> [!note]- Proof of Corollary A
> Fix $h \in G$. We must show $(L_h^*\theta)_g = \theta_g$ as linear maps $T_gG \to \mathfrak{g}$ for every $g \in G$; then the forms agree.
>
> **Write out the pull-back.** For $v \in T_gG$, by the definition of the pull-back of a 1-form and of $\theta$,
> $$(L_h^*\theta)_g(v) = \theta_{L_h(g)}\big(d_gL_h(v)\big) = \theta_{hg}\big(d_gL_h(v)\big) = d_{hg}L_{(hg)^{-1}}\big(d_gL_h(v)\big) \qquad \text{(definition of } \theta_{hg} = d_{hg}L_{(hg)^{-1}}\text{).}$$
>
> **Factor the left translation.** Since $(hg)^{-1} = g^{-1}h^{-1}$, we have $L_{(hg)^{-1}} = L_{g^{-1}} \circ L_{h^{-1}}$ (composition of translations, part (ii) of [[Def - Left and Right Translations and Conjugation on a Lie Group|the translations page]], which states $L_a \circ L_b = L_{ab}$). By the chain rule, evaluating the differential at $hg$ and using $L_{h^{-1}}(hg) = g$,
> $$d_{hg}L_{(hg)^{-1}} = d_{hg}\big(L_{g^{-1}} \circ L_{h^{-1}}\big) = d_{L_{h^{-1}}(hg)}L_{g^{-1}} \circ d_{hg}L_{h^{-1}} = d_gL_{g^{-1}} \circ d_{hg}L_{h^{-1}} \qquad \text{(chain rule; } L_{h^{-1}}(hg) = g\text{).}$$
>
> **Cancel the $h$-translations.** Substituting into the pull-back and using the chain rule once more,
> $$(L_h^*\theta)_g(v) = d_gL_{g^{-1}}\Big(d_{hg}L_{h^{-1}}\big(d_gL_h(v)\big)\Big) = d_gL_{g^{-1}}\Big(d_g\big(L_{h^{-1}} \circ L_h\big)(v)\Big) \qquad \text{(chain rule, backwards, at } g\text{).}$$
> Now $L_{h^{-1}} \circ L_h = L_{h^{-1}h} = L_e = \operatorname{id}_G$ (part (ii) again), so $d_g(L_{h^{-1}} \circ L_h) = d_g\operatorname{id}_G = \operatorname{id}_{T_gG}$, and
> $$(L_h^*\theta)_g(v) = d_gL_{g^{-1}}(v) = \theta_g(v) \qquad \text{(definition of } \theta_g\text{).}$$
>
> **Conclusion.** Since $v \in T_gG$ and $g \in G$ were arbitrary, $(L_h^*\theta)_g = \theta_g$ for all $g$, that is $L_h^*\theta = \theta$. Therefore $\theta$ is left-invariant. $\blacksquare$

**Corollary B (right-invariance up to the adjoint action).** $R_h^*\theta = \operatorname{Ad}_{h^{-1}}\theta$ for every $h \in G$; that is, $(R_h^*\theta)_g(v) = \operatorname{Ad}_{h^{-1}}\big(\theta_g(v)\big)$ for all $g$ and $v \in T_gG$.

> [!note]- Proof of Corollary B
> Fix $h \in G$. We must show $(R_h^*\theta)_g = \operatorname{Ad}_{h^{-1}} \circ \theta_g$ for every $g \in G$.
>
> **Write out the pull-back.** For $v \in T_gG$, by the definition of the pull-back and of $\theta$,
> $$(R_h^*\theta)_g(v) = \theta_{gh}\big(d_gR_h(v)\big) = d_{gh}L_{(gh)^{-1}}\big(d_gR_h(v)\big) \qquad \text{(definition of } \theta_{gh}\text{).}$$
>
> **Factor the left translation and move it past the right translation.** As in Corollary A, $L_{(gh)^{-1}} = L_{h^{-1}} \circ L_{g^{-1}}$, so by the chain rule (with $L_{g^{-1}}(gh) = h$)
> $$d_{gh}L_{(gh)^{-1}} = d_hL_{h^{-1}} \circ d_{gh}L_{g^{-1}} \qquad \text{(chain rule; } L_{g^{-1}}(gh) = h\text{).}$$
> Left and right translations commute, $L_{g^{-1}} \circ R_h = R_h \circ L_{g^{-1}}$ (part (ii) of [[Def - Left and Right Translations and Conjugation on a Lie Group|the translations page]]). Both sides send $g$ to $h$ (indeed $L_{g^{-1}}(gh) = h$ and $R_h(L_{g^{-1}}(g)) = R_h(e) = h$), and differentiating the equal maps at $g$ gives, by the chain rule,
> $$d_{gh}L_{g^{-1}} \circ d_gR_h = d_g\big(L_{g^{-1}} \circ R_h\big) = d_g\big(R_h \circ L_{g^{-1}}\big) = d_{L_{g^{-1}}(g)}R_h \circ d_gL_{g^{-1}} = d_eR_h \circ d_gL_{g^{-1}} \qquad \text{(} L_{g^{-1}}(g) = e\text{).}$$
>
> **Assemble and recognise the adjoint.** Combining the two displays,
> $$(R_h^*\theta)_g(v) = d_hL_{h^{-1}}\Big(d_{gh}L_{g^{-1}}\big(d_gR_h(v)\big)\Big) = d_hL_{h^{-1}}\Big(d_eR_h\big(d_gL_{g^{-1}}(v)\big)\Big) = \big(d_hL_{h^{-1}} \circ d_eR_h\big)\big(\theta_g(v)\big),$$
> using $\theta_g(v) = d_gL_{g^{-1}}(v)$ in the last step. Now $d_hL_{h^{-1}} \circ d_eR_h = d_e(L_{h^{-1}} \circ R_h)$ by the chain rule (with $R_h(e) = h$), and $L_{h^{-1}} \circ R_h = \alpha_{h^{-1}}$ is conjugation by $h^{-1}$ (since $\alpha_{h^{-1}}(k) = h^{-1}kh = L_{h^{-1}}(R_h(k))$, the defining factorisation on the translations page). Therefore
> $$d_hL_{h^{-1}} \circ d_eR_h = d_e\alpha_{h^{-1}} = \operatorname{Ad}_{h^{-1}} \qquad \text{(definition } \operatorname{Ad}_g = d_e\alpha_g\text{),}$$
> the last equality being the definition $\operatorname{Ad}_g = d_e\alpha_g$ from [[Thm - Ad is a Smooth Representation and its Differential is ad|the adjoint-representation page]], which is the linear map $\operatorname{Ad}_{h^{-1}} : \mathfrak{g} \to \mathfrak{g}$ whose existence and the identity $\operatorname{Ad}_{h^{-1}} = (\operatorname{Ad}_h)^{-1}$ are proved there.
>
> **Conclusion.** $(R_h^*\theta)_g(v) = \operatorname{Ad}_{h^{-1}}(\theta_g(v))$ for all $g \in G$ and $v \in T_gG$, so $R_h^*\theta = \operatorname{Ad}_{h^{-1}}\theta$. This is the equivariance property that, transplanted to a principal bundle, becomes clause (1) of the definition of a [[Def - Connection on a Principal Bundle|principal connection]]. $\blacksquare$

**Corollary C (value on the left-invariant frame).** For every $\xi \in \mathfrak{g}$ with left-invariant field $\tilde{\xi}$, the function $\theta(\tilde{\xi}) : G \to \mathfrak{g}$ is the constant $\xi$; equivalently $\theta_g(\tilde{\xi}(g)) = \xi$ for all $g$.

> [!note]- Proof of Corollary C
> Fix $\xi \in \mathfrak{g}$ and $g \in G$. By the defining formula for the [[Def - Left-Invariant Vector Field|left-invariant vector field]], $\tilde{\xi}(g) = d_eL_g(\xi)$. Then
> $$\theta_g\big(\tilde{\xi}(g)\big) = d_gL_{g^{-1}}\big(d_eL_g(\xi)\big) = d_e\big(L_{g^{-1}} \circ L_g\big)(\xi) = d_eL_e(\xi) = d_e\operatorname{id}_G(\xi) = \xi,$$
> where the first equality is the definition of $\theta_g$, the second is the chain rule (with $L_g(e) = g$), the third uses $L_{g^{-1}} \circ L_g = L_{g^{-1}g} = L_e = \operatorname{id}_G$ (part (ii) of [[Def - Left and Right Translations and Conjugation on a Lie Group|the translations page]]), and the last is $d_e\operatorname{id}_G = \operatorname{id}_{\mathfrak{g}}$. Since $g$ was arbitrary, $\theta(\tilde{\xi}) \equiv \xi$. This also proves description 2 of the definition and, together with Corollary A, description 1: a left-invariant $\mathfrak{g}$-valued 1-form with $\theta_e = \operatorname{id}$ is determined by its values on the left-invariant frame, and those are fixed to be the constants $\xi$. $\blacksquare$

**Corollary D (matrix form).** If $G \subseteq GL_n(\mathbb{K})$ is a matrix Lie group, then $\theta = g^{-1}dg$, where $g$ is the inclusion $G \hookrightarrow M_n(\mathbb{K})$ and $dg$ is its differential.

> [!note]- Proof of Corollary D
> Fix $A \in G$, so $A$ is an invertible $n \times n$ matrix, and let $v \in T_AG \subseteq T_AGL_n(\mathbb{K}) = M_n(\mathbb{K})$ (the tangent space of the open set $GL_n(\mathbb{K}) \subseteq M_n(\mathbb{K})$ at any point is $M_n(\mathbb{K})$ itself, and $T_AG$ is a subspace of it). We must show $\theta_A(v) = A^{-1}v$, the matrix product.
>
> **Differentiate the linear map $L_{A^{-1}}$.** The left translation $L_{A^{-1}} : GL_n(\mathbb{K}) \to GL_n(\mathbb{K})$, $B \mapsto A^{-1}B$, is the restriction to $GL_n(\mathbb{K})$ of the *linear* map $M_n(\mathbb{K}) \to M_n(\mathbb{K})$, $B \mapsto A^{-1}B$. The differential of a linear map between vector spaces is the map itself, at every point; identifying $T_AGL_n(\mathbb{K})$ and $T_{A^{-1}A}GL_n(\mathbb{K}) = T_eGL_n(\mathbb{K})$ with $M_n(\mathbb{K})$, this gives $d_AL_{A^{-1}}(v) = A^{-1}v$ for every $v \in M_n(\mathbb{K})$. Restricting to $v \in T_AG$, and using that $L_{A^{-1}}(A) = e$ so the image lies in $T_eG = \mathfrak{g}$,
> $$\theta_A(v) = d_AL_{A^{-1}}(v) = A^{-1}v \qquad \text{(definition of } \theta_A\text{; differential of the linear map } B \mapsto A^{-1}B\text{).}$$
>
> **Recognise $g^{-1}dg$.** The inclusion $g : G \hookrightarrow M_n(\mathbb{K})$ has differential $d_Ag(v) = v$ for $v \in T_AG$ (the differential of an inclusion of a submanifold into the ambient linear space is the subspace inclusion of tangent spaces, and $M_n(\mathbb{K})$ is its own tangent space). Hence $(g^{-1}dg)_A(v) = g(A)^{-1} \cdot d_Ag(v) = A^{-1}v$, which equals $\theta_A(v)$ by the previous display. Since $A \in G$ and $v \in T_AG$ were arbitrary, $\theta = g^{-1}dg$. $\blacksquare$

**Corollary E (pull-back product rule).** Let $U$ be a manifold and $g_1, g_2 : U \to G$ smooth maps, with pointwise product $g_1 g_2 : U \to G$, $(g_1 g_2)(u) = g_1(u)\,g_2(u)$. Then
$$(g_1 g_2)^*\theta = \operatorname{Ad}_{g_2^{-1}}\big(g_1^*\theta\big) + g_2^*\theta,$$
where $\operatorname{Ad}_{g_2^{-1}}$ acts pointwise, $\big(\operatorname{Ad}_{g_2^{-1}}(g_1^*\theta)\big)_u(w) = \operatorname{Ad}_{g_2(u)^{-1}}\big((g_1^*\theta)_u(w)\big)$. As a further consequence, $(g^{-1})^*\theta = -\operatorname{Ad}_g(g^*\theta)$ for a single smooth map $g : U \to G$.

> [!note]- Proof of Corollary E
> Let $m : G \times G \to G$ be the multiplication, $m(a, b) = ab$. The key is the value of $\theta$ on the differential of $m$.
>
> **Step 0 — the Leibniz rule for $m$.** We claim that for $a, b \in G$, $v \in T_aG$, $w \in T_bG$,
> $$\theta_{ab}\big(d_{(a,b)}m(v, w)\big) = \operatorname{Ad}_{b^{-1}}\big(\theta_a(v)\big) + \theta_b(w). \tag{$\ast$}$$
> The differential of the multiplication splits over the two factors: $d_{(a,b)}m(v, w) = d_{(a,b)}m(v, 0) + d_{(a,b)}m(0, w)$, and freezing one argument turns $m$ into a translation of the other, $m(\,\cdot\,, b) = R_b$ and $m(a, \cdot) = L_a$, so
> $$d_{(a,b)}m(v, w) = d_aR_b(v) + d_bL_a(w) \qquad \text{(} m(\,\cdot\,,b) = R_b,\ m(a,\cdot) = L_a\text{).}$$
> Apply $\theta_{ab} = d_{ab}L_{(ab)^{-1}}$ to each summand. For the second summand, $d_{ab}L_{(ab)^{-1}}\big(d_bL_a(w)\big) = d_b\big(L_{(ab)^{-1}} \circ L_a\big)(w) = d_b\big(L_{b^{-1}a^{-1}} \circ L_a\big)(w) = d_bL_{b^{-1}}(w) = \theta_b(w)$, using $L_{b^{-1}a^{-1}} \circ L_a = L_{b^{-1}a^{-1}a} = L_{b^{-1}}$ (chain rule and part (ii) of the translations page). For the first summand, $d_{ab}L_{(ab)^{-1}}\big(d_aR_b(v)\big)$: by the same computation as in Corollary B (with $g \rightsquigarrow a$, $h \rightsquigarrow b$), $\theta_{ab}(d_aR_b(v)) = \operatorname{Ad}_{b^{-1}}(\theta_a(v))$. Adding the two summands gives $(\ast)$. (For a matrix group $(\ast)$ is the one-line identity $\theta_{ab}(vb + aw) = (ab)^{-1}(vb + aw) = b^{-1}(a^{-1}v)b + b^{-1}w = \operatorname{Ad}_{b^{-1}}(a^{-1}v) + b^{-1}w$, using $d_{(a,b)}m(v,w) = vb + aw$ from the Leibniz rule for matrix multiplication; this is the computation $(\ast)$ abstracts.)
>
> **Step 1 — pull back along $(g_1, g_2)$.** The product map factors as $g_1 g_2 = m \circ (g_1, g_2)$, where $(g_1, g_2) : U \to G \times G$, $u \mapsto (g_1(u), g_2(u))$. Fix $u \in U$ and $w \in T_uU$, and write $a = g_1(u)$, $b = g_2(u)$. By the chain rule,
> $$d_u(g_1 g_2)(w) = d_{(a,b)}m\big(d_ug_1(w),\, d_ug_2(w)\big) \qquad \text{(chain rule, } g_1 g_2 = m \circ (g_1,g_2)\text{).}$$
> Apply $\theta_{ab}$ and use $(\ast)$ with $v = d_ug_1(w)$ and its second argument $d_ug_2(w)$:
> $$\big((g_1 g_2)^*\theta\big)_u(w) = \theta_{ab}\big(d_u(g_1 g_2)(w)\big) = \operatorname{Ad}_{b^{-1}}\big(\theta_a(d_ug_1(w))\big) + \theta_b\big(d_ug_2(w)\big) \qquad \text{(by }(\ast)\text{).}$$
> By the definition of pull-back, $\theta_a(d_ug_1(w)) = (g_1^*\theta)_u(w)$ and $\theta_b(d_ug_2(w)) = (g_2^*\theta)_u(w)$, and $b = g_2(u)$, so
> $$\big((g_1 g_2)^*\theta\big)_u(w) = \operatorname{Ad}_{g_2(u)^{-1}}\big((g_1^*\theta)_u(w)\big) + (g_2^*\theta)_u(w).$$
> Since $u$ and $w$ were arbitrary, $(g_1 g_2)^*\theta = \operatorname{Ad}_{g_2^{-1}}(g_1^*\theta) + g_2^*\theta$.
>
> **Step 2 — the inverse rule.** Apply the product rule to $g_1 = g$ and $g_2 = g^{-1}$, whose product $g\,g^{-1} \equiv e$ is the constant map to the identity, so $(g\,g^{-1})^*\theta = 0$ (a constant map has zero differential, hence pulls every 1-form back to $0$). The product rule gives $0 = \operatorname{Ad}_{(g^{-1})^{-1}}(g^*\theta) + (g^{-1})^*\theta = \operatorname{Ad}_g(g^*\theta) + (g^{-1})^*\theta$, whence $(g^{-1})^*\theta = -\operatorname{Ad}_g(g^*\theta)$.
>
> **Conclusion.** The Maurer–Cartan form pulls a product of $G$-valued maps back to the $\operatorname{Ad}$-twisted sum of the pull-backs. This is the algebraic identity behind every local transformation law of a connection: substituting $g_1 g_2 = g_{\alpha\beta}g_{\beta\gamma}$ on a triple overlap reproduces the cocycle-compatibility of the gauge potentials, and it is invoked by name in [[Thm - Transformation of Local Connection and Curvature Forms|the transformation theorem]] of this chapter. $\blacksquare$

**Example — $U(1)$.** Let $G = U(1) = \{z \in \mathbb{C} : |z| = 1\}$, an abelian matrix group ($1 \times 1$ complex matrices) with Lie algebra $\mathfrak{u}(1) = i\mathbb{R}$. Parametrise by $z = e^{i\varphi}$, $\varphi \in \mathbb{R}/2\pi\mathbb{Z}$. By Corollary D, $\theta = z^{-1}dz$, and since $dz = ie^{i\varphi}\,d\varphi = iz\,d\varphi$,
$$\theta = z^{-1}\,dz = z^{-1}(iz\,d\varphi) = i\,d\varphi \in \Omega^1\big(U(1); i\mathbb{R}\big).$$
Verify the corollaries clause by clause. *Left-invariance and Ad-equivariance* (Corollaries A, B): $U(1)$ is abelian, so $\operatorname{Ad}_{h} = \operatorname{id}$ for all $h$ (conjugation is trivial in an abelian group), and both $L_h^*\theta = \theta$ and $R_h^*\theta = \theta$ must hold; indeed $L_h$ and $R_h$ are the rotation $\varphi \mapsto \varphi + \psi$ (writing $h = e^{i\psi}$), which pulls $d\varphi$ back to $d\varphi$, so $L_h^*(i\,d\varphi) = i\,d\varphi = \theta$, confirming both. *Value on the left-invariant frame* (Corollary C): the left-invariant field generated by $\xi = i \in \mathfrak{u}(1)$ is $\tilde{\xi}(z) = d_eL_z(i) = z \cdot i = iz$, which in the coordinate $\varphi$ is $\partial_\varphi$ (its velocity is $iz = \frac{dz}{d\varphi}$), and $\theta(\partial_\varphi) = i\,d\varphi(\partial_\varphi) = i = \xi$, as claimed. *Matrix form* (Corollary D) is the computation just done. So $U(1)$'s Maurer–Cartan form is the angle form $i\,d\varphi$, and $\frac{1}{2\pi i}\int_{S^1} g^*\theta = \frac{1}{2\pi}\int_{S^1} d(\varphi \circ g)$ is the winding number of $g : S^1 \to U(1)$.

**Example — $SU(2)$ in quaternion coordinates.** Identify $SU(2)$ with the group $Sp(1)$ of unit quaternions $g = x_0 + x_1 i + x_2 j + x_3 k$, $\sum_\mu x_\mu^2 = 1$ (the standard identification of $SU(2) \cong S^3 \subseteq \mathbb{H}$; the Lie algebra $\mathfrak{su}(2)$ is $\operatorname{Im}\mathbb{H} = \operatorname{span}_{\mathbb{R}}\{i, j, k\}$, the imaginary quaternions, with bracket $[u, v] = uv - vu$). For a unit quaternion $g^{-1} = \bar{g} = x_0 - x_1 i - x_2 j - x_3 k$, so by Corollary D,
$$\theta = \bar{g}\,dg = (x_0 - x_1 i - x_2 j - x_3 k)(dx_0 + dx_1\,i + dx_2\,j + dx_3\,k).$$
Expanding with the quaternion relations $i^2 = j^2 = k^2 = -1$, $ij = k = -ji$, $jk = i = -kj$, $ki = j = -ik$, and collecting components,
$$\operatorname{Re}\theta = \textstyle\sum_\mu x_\mu\,dx_\mu = \tfrac{1}{2}\,d\big(\textstyle\sum_\mu x_\mu^2\big) = \tfrac12\,d(1) = 0,$$
$$\theta = \theta^i\, i + \theta^j\, j + \theta^k\, k, \qquad
\begin{aligned}
\theta^i &= x_0\,dx_1 - x_1\,dx_0 - x_2\,dx_3 + x_3\,dx_2,\\
\theta^j &= x_0\,dx_2 - x_2\,dx_0 + x_1\,dx_3 - x_3\,dx_1,\\
\theta^k &= x_0\,dx_3 - x_3\,dx_0 - x_1\,dx_2 + x_2\,dx_1.
\end{aligned}$$
Verify the clauses. *Values in $\mathfrak{su}(2)$*: the vanishing of $\operatorname{Re}\theta$, forced by $\sum x_\mu^2 = 1$, is exactly the statement that $\theta$ takes values in $\operatorname{Im}\mathbb{H} = \mathfrak{su}(2)$, as a $\mathfrak{g}$-valued form must; this is the clause-by-clause check that the target is $\mathfrak{g}$ and not the ambient $\mathbb{H}$. *Left-invariance* (Corollary A): the three 1-forms $\theta^i, \theta^j, \theta^k$ are the standard left-invariant coframe of $S^3$ dual to the left-invariant fields generated by $i, j, k$; that they are left-invariant is Corollary A, and one checks directly that at the identity $g = (1,0,0,0)$ they reduce to $(\theta^i, \theta^j, \theta^k)|_e = (dx_1, dx_2, dx_3)$, so $\theta_e(v) = v_1 i + v_2 j + v_3 k$ is the identity $T_eSU(2) = \operatorname{Im}\mathbb{H} \to \mathfrak{su}(2)$, matching $\theta_e = \operatorname{id}$. The direct verification of the Maurer–Cartan equation $d\theta + \tfrac12[\theta \wedge \theta] = 0$ on these components, and the identification of $\theta$ with the dual left-invariant coframe, are carried out in [[Ex - The Maurer-Cartan Form of U(1) and of SU(2)|the $U(1)$-and-$SU(2)$ exercise]].

**Example — $\mathbb{R}^n$ (the additive group).** Let $G = (\mathbb{R}^n, +)$, an abelian Lie group with $\mathfrak{g} = T_0\mathbb{R}^n = \mathbb{R}^n$. Here $L_g(h) = g + h$ is translation, a linear-plus-constant map whose differential at every point is the identity $\operatorname{id}_{\mathbb{R}^n}$, so $\theta_g = d_gL_{-g} = \operatorname{id}_{\mathbb{R}^n} : T_g\mathbb{R}^n \to T_0\mathbb{R}^n = \mathbb{R}^n$. In coordinates $(x^1, \dots, x^n)$ this is the tautological (vector-valued) 1-form
$$\theta = (dx^1, \dots, dx^n) = \textstyle\sum_{a=1}^n dx^a \otimes e_a,$$
where $(e_1, \dots, e_n)$ is the standard basis of $\mathbb{R}^n = \mathfrak{g}$: the Maurer–Cartan form of $\mathbb{R}^n$ is "$dx$." This is the smallest concrete case and the calibration anchor: $\theta$ is the identity-reading form, and on the additive group where every velocity is already "at the identity" it is literally the coordinate differential.

**Non-example — the right Maurer–Cartan form $dg\,g^{-1}$.** The $\mathfrak{g}$-valued 1-form $\vartheta_g := d_gR_{g^{-1}}$, equal to $dg\,g^{-1}$ for a matrix group, is **not** the (left) Maurer–Cartan form $\theta$ on any non-abelian $G$. At a point $g$, $\vartheta_g(v) = vg^{-1}$ while $\theta_g(v) = g^{-1}v$ (matrix case); these agree for all $v$ if and only if $g^{-1}v = vg^{-1}$, that is $v$ commutes with $g$, which fails for generic $v \in T_gG$ once $G$ is non-abelian. Concretely on $SU(2) = Sp(1)$, take $g = i$ (a unit quaternion) and $v = j \in T_gG$ (a tangent vector at $g = i$, since $\operatorname{Re}(\bar{g}v) = \operatorname{Re}(-i \cdot j) = \operatorname{Re}(-k) = 0$ shows $v \perp g$, hence $v \in T_gS^3$): then $\theta_g(v) = \bar{g}v = (-i)\cdot j = -ij = -k$ (since $ij = k$), whereas $\vartheta_g(v) = v\bar{g} = j\cdot(-i) = -ji = k$ (since $ji = -k$), so $\vartheta_g(v) = k \neq -k = \theta_g(v)$. The two forms have opposite invariance types: $\theta$ is left-invariant with $R_h^*\theta = \operatorname{Ad}_{h^{-1}}\theta$ (Corollaries A, B), while the right form is right-invariant with $L_h^*\vartheta = \operatorname{Ad}_h\vartheta$. They coincide only when $G$ is abelian, where $\operatorname{Ad} \equiv \operatorname{id}$ and left and right translations agree.

**Calibration check.** First, confirm the curve formula: for any smooth path $g(t)$ in a matrix group, $\theta(\dot{g}(t)) = g(t)^{-1}\dot{g}(t)$ — apply $\theta_{g(t)} = d_{g(t)}L_{g(t)^{-1}}$ to $\dot{g}(t) \in T_{g(t)}G$ and use Corollary D. Second, on $U(1)$ with $g(t) = e^{i\omega t}$, this gives $\theta(\dot g) = e^{-i\omega t}\cdot i\omega e^{i\omega t} = i\omega$, a constant in $i\mathbb{R} = \mathfrak{u}(1)$, matching $\theta = i\,d\varphi$ evaluated on $\dot\varphi = \omega$. Third, re-derive the inverse rule of Corollary E in the matrix case as a sanity check: $d(g^{-1}) = -g^{-1}(dg)g^{-1}$ (differentiate $g^{-1}g = e$), so $(g^{-1})^*\theta = (g^{-1})^{-1}d(g^{-1}) = g\cdot(-g^{-1}dg\,g^{-1}) = -(dg)g^{-1} = -g(g^{-1}dg)g^{-1} = -\operatorname{Ad}_g(g^*\theta)$, agreeing with the abstract proof. If you can also explain why $\theta$ of $\mathbb{R}^n$ is $dx$ but $\theta$ of $U(1)$ is $i\,d\varphi$ rather than $d\varphi$ — the factor of $i$ is the basis vector of $\mathfrak{u}(1) = i\mathbb{R}$ that the form's values must carry — you have understood that $\theta$ is $\mathfrak{g}$-valued, not scalar.

---

# Unlocked by This

> [!tip] The Maurer–Cartan equation *(from this chapter, §4.1)*
> The single structural identity satisfied by $\theta$ is $d\theta + \tfrac12[\theta \wedge \theta] = 0$, proved on [[Thm - The Maurer-Cartan Equation|the Maurer–Cartan equation page]] by evaluating both sides on left-invariant fields and using Corollary C together with $[\tilde\xi, \tilde\eta] = \widetilde{[\xi,\eta]}$. It is the flatness of the reference connection and the seed of the curvature's structure equation.

> [!tip] Connections on principal bundles *(from this chapter, §4.2)*
> The equivariance $R_h^*\theta = \operatorname{Ad}_{h^{-1}}\theta$ (Corollary B) and the normalisation $\theta(\tilde\xi) = \xi$ (Corollary C) are precisely the two axioms of a [[Def - Connection on a Principal Bundle|principal connection form]] $\omega \in \Omega^1(P; \mathfrak{g})$, restricted to a fibre. A connection is a $\mathfrak{g}$-valued 1-form on $P$ that restricts to the Maurer–Cartan form along each fibre and extends it $G$-equivariantly across the horizontal directions.

> [!tip] Local transformation laws and gauge potentials *(from this chapter, §4.2–4.3)*
> The pull-back product rule (Corollary E) is the algebraic engine of [[Thm - Transformation of Local Connection and Curvature Forms|the transformation theorem]]: a change of local section by $g_{\alpha\beta}$ moves the gauge potential by $\operatorname{Ad}_{g_{\alpha\beta}^{-1}}A_\alpha + g_{\alpha\beta}^*\theta$, and the $g^*\theta$ term is the pure-gauge potential $g^{-1}dg$ produced out of the vacuum.

> [!tip] The Chern–Simons functional *(from Gauge Theory VI)*
> The degree of a map $g : S^3 \to SU(2)$, computed as $\frac{1}{24\pi^2}\int_{S^3}\operatorname{tr}\big((g^*\theta)^{\wedge 3}\big)$, is the gauge variation of the Chern–Simons functional; the integrand is a wedge power of the pulled-back Maurer–Cartan form.
