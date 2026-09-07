---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Left-Invariant Vector Field"
  - "Def - Exponential Map of a Lie Group"
  - "Def - One-Parameter Subgroup"
  - "Def - Integral Curve of a Vector Field"
  - "Def - Flow of a Vector Field"
  - "Thm - Existence and Uniqueness of Integral Curves"
  - "Thm - Fundamental Theorem on Flows"
tags: [geometry, gauge-theory, lie-groups]
---

# Notation

Standing conventions of the series (see [[Gauge Theory I — Lie Groups, Representations, and Group Actions]] for the full registry): manifolds are smooth, Hausdorff and second countable, and "smooth" means $C^\infty$; the Lie algebra of a Lie group $G$ is $\mathfrak{g} = T_eG$, with the bracket transported from the bracket of left-invariant vector fields.

Throughout, $G$ is a [[Def - Lie Group|Lie group]] with identity element $e$ and multiplication map $m : G \times G \to G$, $m(g, h) = gh$. For $g \in G$ the **left translation** by $g$ is $L_g : G \to G$, $L_g(h) = gh$, and the **right translation** is $R_g : G \to G$, $R_g(h) = hg$; these are the maps fixed on [[Def - Left and Right Translations and Conjugation on a Lie Group]], and each is a [[Def - Diffeomorphism|diffeomorphism]] with inverse $L_{g^{-1}}$, respectively $R_{g^{-1}}$ (Lemma 1 below re-proves this in two lines so that the page is self-contained). Note that on $G$ itself the symbol $R_g$ means right translation; the series' convention that Lie groups act on principal bundles on the right is the reason this particular translation, and not $L_g$, will turn out to be the flow of a left-invariant field.

The **Lie algebra** of $G$ is the tangent space $\mathfrak{g} := T_eG$ ([[Def - The Lie Algebra of a Lie Group]]). For $X \in \mathfrak{g}$ we write $X^L \in \mathfrak{X}(G)$ for the [[Def - Left-Invariant Vector Field|left-invariant vector field]] with value $X$ at the identity,
$$X^L_g := d_eL_g(X) \in T_gG \qquad (g \in G),$$
where $d_eL_g : T_eG \to T_gG$ is the differential of $L_g$ at $e$. Left-invariance means $d_hL_g(X^L_h) = X^L_{gh}$ for all $g, h \in G$, and every left-invariant vector field is smooth and is of the form $X^L$ for a unique $X \in \mathfrak{g}$ — this is the content of [[Thm - Left-Invariant Vector Fields Form a Lie Algebra]] (its Step 3 and its Lemma 3, "smoothness is automatic"), and we use it freely. The map $X \mapsto X^L$ is linear, because $d_eL_g$ is linear; in particular $(\alpha X)^L = \alpha X^L$ for $\alpha \in \mathbb{R}$.

A smooth curve in a manifold $M$ is a smooth map $c : J \to M$ on an open interval $J \subseteq \mathbb{R}$; its **velocity** at $t \in J$ is $c'(t) := dc_t\big(\tfrac{d}{dt}\big|_t\big) \in T_{c(t)}M$. The one fact about velocities we use repeatedly is the chain rule for curves: for a smooth map $F : M \to N$,
$$(F \circ c)'(t) = dF_{c(t)}\big(c'(t)\big) \qquad \text{(by [[Thm - Chain Rule for the Differential]], since } (F \circ c)'(t) = d(F \circ c)_t(\tfrac{d}{dt}) = dF_{c(t)}(dc_t(\tfrac{d}{dt}))\text{)}.$$
An [[Def - Integral Curve of a Vector Field|integral curve]] of a vector field $Y \in \mathfrak{X}(M)$ is a smooth curve $c : J \to M$ with $c'(t) = Y_{c(t)}$ for all $t \in J$; it **starts at** $p$ if $0 \in J$ and $c(0) = p$. For each $p \in M$ the **maximal integral curve** starting at $p$ is written $\gamma^{(p)} : \mathcal{D}^{(p)} \to M$; its domain $\mathcal{D}^{(p)}$ is an open interval containing $0$ ([[Thm - Existence and Uniqueness of Integral Curves]], Corollary). The [[Def - Flow of a Vector Field|flow]] of $Y$ is the map $\phi^Y : \mathcal{D} \to M$, $\phi^Y(t, p) = \gamma^{(p)}(t)$, on the flow domain $\mathcal{D} = \{(t, p) : t \in \mathcal{D}^{(p)}\}$, and we write $\phi^Y_t(p) := \phi^Y(t, p)$. The field $Y$ is [[Def - Complete Vector Field|complete]] if $\mathcal{D} = \mathbb{R} \times M$.

For $X \in \mathfrak{g}$, once part (b) of the theorem below is proved, $\gamma_X : \mathbb{R} \to G$ denotes the maximal integral curve of $X^L$ starting at $e$ (Bär's notation, p. 21), and the **exponential map** is $\exp : \mathfrak{g} \to G$, $\exp(X) := \gamma_X(1)$ ([[Def - Exponential Map of a Lie Group]]). A [[Def - One-Parameter Subgroup|one-parameter subgroup]] of $G$ is a smooth map $\gamma : \mathbb{R} \to G$ that is a group homomorphism from $(\mathbb{R}, +)$, that is, $\gamma(s + t) = \gamma(s)\gamma(t)$ for all $s, t \in \mathbb{R}$; its **initial velocity** is $\gamma'(0) \in T_eG = \mathfrak{g}$.

> [!warning] Convention: Bär's notation versus the series' notation
> Bär (§1.4, pp. 21–22) writes a single letter $X$ both for an element of $\mathfrak{g}$ and for the left-invariant vector field it generates, so his "$X(\gamma(t))$" is our $X^L_{\gamma(t)}$, and he writes $\dot\gamma$ where the vault's differential-geometry pages write $\gamma'$; both denote $d\gamma_t(\tfrac{d}{dt})$. Bär also takes $\mathfrak{g}$ to be the space of left-invariant vector fields; the series takes $\mathfrak{g} = T_eG$ and passes between the two through the evaluation isomorphism $X^L \mapsto X^L_e$ of [[Thm - Left-Invariant Vector Fields Form a Lie Algebra]]. No statement changes under either translation. The theorem below is Bär's Lemma 1.4.2 together with his equation (1.6) and Exercise 1.4.1; Bär proves only the direction "homomorphism $\Rightarrow$ integral curve" and calls the converse "slightly more involved" — the converse, the completeness statement, and the smoothness of $\exp$ (which Bär attributes to "the general theory of ordinary differential equations") are all proved in full on this page.

---

# Statement

> **Theorem (one-parameter subgroups are the integral curves of left-invariant vector fields; Bär Lemma 1.4.2, eq. (1.6), Exercise 1.4.1; Lee, *Introduction to Smooth Manifolds*, 2nd ed., Prop. 20.5 and Thm. 20.8).** Let $G$ be a Lie group with Lie algebra $\mathfrak{g} = T_eG$, and for $X \in \mathfrak{g}$ let $X^L$ be the left-invariant vector field with $X^L_e = X$.
>
> **(a) (Characterisation.)** Let $\gamma : \mathbb{R} \to G$ be a smooth curve with $\gamma(0) = e$. Then $\gamma$ is a group homomorphism, that is, $\gamma(s + t) = \gamma(s)\gamma(t)$ for all $s, t \in \mathbb{R}$, if and only if $\gamma$ is an integral curve of some left-invariant vector field on $G$. When this holds, the left-invariant field is $X^L$ with $X = \gamma'(0)$.
>
> **(b) (Completeness.)** For every $X \in \mathfrak{g}$ the vector field $X^L$ is complete: for every $g \in G$ the maximal integral curve of $X^L$ starting at $g$ is defined on all of $\mathbb{R}$. In particular the integral curve $\gamma_X : \mathbb{R} \to G$ of $X^L$ with $\gamma_X(0) = e$ exists, is unique, and is defined on all of $\mathbb{R}$.
>
> **(c) (Uniqueness of one-parameter subgroups.)** For every $X \in \mathfrak{g}$ the curve $\gamma_X$ is a one-parameter subgroup of $G$ with initial velocity $\gamma_X'(0) = X$, and it is the only one: the map $\gamma \mapsto \gamma'(0)$ is a bijection from the set of one-parameter subgroups of $G$ onto $\mathfrak{g}$, with inverse $X \mapsto \gamma_X$.
>
> **(d) (The exponential map along lines.)** With $\exp(X) := \gamma_X(1)$, for all $X \in \mathfrak{g}$ and $s, t \in \mathbb{R}$,
> $$\gamma_X(t) = \exp(tX), \qquad \exp\big((s + t)X\big) = \exp(sX)\exp(tX), \qquad \exp(0) = e, \qquad \exp(-X) = \exp(X)^{-1}.$$
>
> **(e) (The flow of a left-invariant field is right translation.)** The flow of $X^L$ is global and is given by
> $$\phi^{X^L}_t(g) = g\,\gamma_X(t) = g\exp(tX) = R_{\exp(tX)}(g) \qquad (t \in \mathbb{R},\ g \in G);$$
> consequently $\{R_{\exp(tX)}\}_{t \in \mathbb{R}}$ is a one-parameter group of diffeomorphisms of $G$: $R_{\exp(0)} = \mathrm{id}_G$ and $R_{\exp(sX)} \circ R_{\exp(tX)} = R_{\exp((s+t)X)}$.
>
> **(f) (Smoothness.)** The exponential map $\exp : \mathfrak{g} \to G$ is smooth.

> **Corollary (the one-parameter subgroup with a prescribed velocity).** For $X \in \mathfrak{g}$, the unique one-parameter subgroup of $G$ with initial velocity $X$ is $t \mapsto \exp(tX)$. Equivalently: a smooth homomorphism $\gamma : \mathbb{R} \to G$ is determined by $\gamma'(0)$, and every vector in $\mathfrak{g}$ occurs as such a velocity.

The corollary is the conjunction of (c) and the first identity in (d); it is the form in which the theorem is most often used, and it is the reason the page [[Def - One-Parameter Subgroup]] may describe one-parameter subgroups as being "in bijection with $\mathfrak{g}$".

---

# Motivation

The Lie algebra $\mathfrak{g} = T_eG$ was introduced as a linearisation of $G$ at the identity. The question this theorem answers is how to travel back: given an infinitesimal direction $X \in T_eG$, which curve in $G$ does it generate, and in what sense is that curve determined by $X$ alone? There are two candidate answers, and they look different. The first is algebraic: ask for a smooth curve $\gamma$ that respects the group structure, $\gamma(s + t) = \gamma(s)\gamma(t)$, and starts out in the direction $X$. The second is analytic: spread $X$ over all of $G$ by left translation into the vector field $X^L$, and follow its integral curve from $e$. The theorem says that these two answers are the same answer, that each exists for every $X$, that each is unique, and that the resulting curve is defined for all time. This coincidence is what makes the exponential map $\exp(X) = \gamma_X(1)$ a well-defined smooth map $\mathfrak{g} \to G$ at all, and everything the series does with $\exp$ — the local diffeomorphism at the origin, the naturality $\varphi \circ \exp = \exp \circ d_e\varphi$, the matrix exponential, the fundamental vector fields $\xi_P(p) = \tfrac{d}{dt}\big|_{t=0} p \cdot \exp(t\xi)$ on a principal bundle — rests on it.

It is worth seeing in the smallest case why both descriptions must agree. Take $G = (\mathbb{R}, +)$, so that $e = 0$, $L_a(x) = a + x$ and $d_0L_a = \mathrm{id}$ (the differential of a translation of $\mathbb{R}$ is the identity). For $X = v\,\tfrac{d}{dx}\big|_0 \in T_0\mathbb{R}$ the left-invariant field is the constant field $X^L = v\,\tfrac{d}{dx}$, whose integral curve from $0$ is $\gamma(t) = vt$; and the smooth homomorphisms $(\mathbb{R}, +) \to (\mathbb{R}, +)$ are precisely the linear maps $t \mapsto vt$ (a smooth additive map has $\gamma'(t) = \gamma'(0)$ for all $t$ by differentiating $\gamma(t + s) = \gamma(t) + \gamma(s)$ in $s$, so $\gamma$ is linear). Both descriptions give the line through the origin with slope $v$, and $\exp(v) = v$. The theorem is the statement that this agreement is not an accident of $\mathbb{R}$ but a consequence of left-invariance in every Lie group.

The case $G = U(1) = \{z \in \mathbb{C} : |z| = 1\}$ already shows the non-trivial content. Here $T_1U(1) = i\mathbb{R}$, the left translation $L_z(w) = zw$ is the restriction of the complex-linear map $w \mapsto zw$, so $d_1L_z(i\theta) = i\theta z$, and the left-invariant field generated by $X = i\theta$ is $X^L_z = i\theta z$ (the tangent vector to the circle at $z$ of length $|\theta|$, pointing anticlockwise if $\theta > 0$). The curve $\gamma(t) = e^{i\theta t}$ satisfies $\gamma'(t) = i\theta e^{i\theta t} = X^L_{\gamma(t)}$, so it is the integral curve of $X^L$ from $1$, and it is a homomorphism because $e^{i\theta(s+t)} = e^{i\theta s}e^{i\theta t}$. Hence $\exp(i\theta) = e^{i\theta}$. The theorem's bijection is between one-parameter subgroups and $\mathfrak{g}$, not between $G$ and $\mathfrak{g}$: the map $\exp$ itself is $2\pi$-periodic on $i\mathbb{R}$ and so is neither injective nor a homomorphism from $(\mathfrak{g}, +)$ — it is a homomorphism only along each line $\{tX\}$, which is exactly what part (d) says.

The role of the theorem in the series is threefold. First, it is the definition-enabling result of §1.4: without completeness (b) the value $\gamma_X(1)$ need not exist, and without smoothness (f) the exponential map could not be differentiated to obtain $d_0\exp = \mathrm{id}$ on [[Thm - The Exponential Map is a Local Diffeomorphism at the Origin]]. Second, the characterisation (a) is the tool by which one recognises an exponential in disguise: any smooth homomorphism out of $\mathbb{R}$, however it was constructed, is $t \mapsto \exp(tX)$ for $X$ its initial velocity; this is how [[Thm - The Exponential Map of a Matrix Group is the Matrix Exponential]] identifies $\exp$ with the power series, and how [[Thm - Naturality of the Exponential Map]] is proved. Third, part (e) — the flow of $X^L$ is right translation by $\exp(tX)$ — is the mechanism behind fundamental vector fields on principal bundles in chapters III and IV, where the vertical directions are generated by $t \mapsto p \cdot \exp(t\xi)$.

---

# Sources and Targets

**Sources (Input Broadening)**

The hypotheses of the theorem are of two kinds: in (a), that a smooth curve $\gamma : \mathbb{R} \to G$ with $\gamma(0) = e$ is a group homomorphism, or that it is an integral curve of a left-invariant field; in (b)–(f), only that $X$ is an element of $\mathfrak{g}$. The useful question is therefore which situations hand us a one-parameter subgroup, or an integral curve of a left-invariant field, without saying so.

The first disguised source is **a homomorphism composed with a one-parameter subgroup**. If $\varphi : G \to H$ is a [[Def - Lie Group Homomorphism|Lie group homomorphism]] and $\gamma : \mathbb{R} \to G$ is a one-parameter subgroup, then $\varphi \circ \gamma : \mathbb{R} \to H$ is smooth (composition of smooth maps) and satisfies $\varphi(\gamma(s + t)) = \varphi(\gamma(s)\gamma(t)) = \varphi(\gamma(s))\varphi(\gamma(t))$, so it is a one-parameter subgroup of $H$. The bridge to the hypothesis of (a) is just the homomorphism property of $\varphi$, but the payoff is not obvious: by the Corollary, $\varphi(\exp_G(tX)) = \exp_H(t\,d_e\varphi(X))$, because both sides are one-parameter subgroups of $H$ with the same initial velocity $d_e\varphi(X)$ (chain rule). Evaluating at $t = 1$ gives the naturality of the exponential map. *Example problem:* show that $\det(e^{A}) = e^{\operatorname{tr} A}$ for $A \in \operatorname{Mat}(n \times n; \mathbb{R})$ by applying this to $\varphi = \det : GL(n; \mathbb{R}) \to \mathbb{R}^\times$, whose differential at the identity is the trace.

The second disguised source is **a curve whose logarithmic derivative is constant**. For a smooth curve $\gamma : \mathbb{R} \to G$ define its left logarithmic derivative $\theta(t) := d_{\gamma(t)}L_{\gamma(t)^{-1}}(\gamma'(t)) \in T_eG$, the velocity pulled back to the identity. The condition "$\gamma$ is an integral curve of $X^L$" reads $\gamma'(t) = d_eL_{\gamma(t)}(X)$, and applying $d_{\gamma(t)}L_{\gamma(t)^{-1}}$ to both sides (the inverse of $d_eL_{\gamma(t)}$, by the chain rule and $L_{\gamma(t)^{-1}} \circ L_{\gamma(t)} = \mathrm{id}$) turns it into $\theta(t) = X$ for all $t$. So a curve with $\gamma(0) = e$ and constant logarithmic derivative $X$ is an integral curve of $X^L$, hence by (a) a one-parameter subgroup, hence $\gamma(t) = \exp(tX)$. For a matrix group this is the statement that $\gamma^{-1}\dot\gamma \equiv X$ forces $\gamma(t) = e^{tX}$. *Example problem:* a rigid body rotating with constant body angular velocity $\omega \in \mathbb{R}^3$ has attitude $R(t) \in SO(3)$ satisfying $R(t)^{-1}\dot R(t) = \hat\omega$ (the antisymmetric matrix of $\omega$); show that $R(t) = R(0)\exp(t\hat\omega)$.

The third disguised source is **a constant-coefficient linear system of ordinary differential equations**. For $A \in \operatorname{Mat}(n \times n; \mathbb{R})$ the fundamental matrix solution $\Phi(t)$ of $\dot x = Ax$ — the matrix-valued curve with $\dot\Phi = A\Phi$ and $\Phi(0) = 1_n$ — takes values in $GL(n; \mathbb{R})$ (its determinant satisfies $\tfrac{d}{dt}\det\Phi = (\operatorname{tr} A)\det\Phi$ and so never vanishes) and satisfies $\Phi(s + t) = \Phi(s)\Phi(t)$, because for fixed $s$ both $t \mapsto \Phi(t + s)$ and $t \mapsto \Phi(t)\Phi(s)$ solve $\dot Y = AY$ with $Y(0) = \Phi(s)$ and the linear system has unique solutions. So $\Phi$ is a one-parameter subgroup of $GL(n; \mathbb{R})$ with initial velocity $A$, and the theorem identifies it: $\Phi(t) = \exp(tA)$, which [[Thm - The Exponential Map of a Matrix Group is the Matrix Exponential]] then computes as the power series. The bridge is the uniqueness theorem for linear systems; what is non-obvious is that the *group* property of a fundamental solution is a consequence of autonomy. *Example problem:* solve $\dot x = Ax$ for $A = \begin{pmatrix} 0 & -\theta \\ \theta & 0 \end{pmatrix}$ by recognising $\Phi$ as the one-parameter subgroup of $SO(2)$ with velocity $A$, that is, rotation by angle $\theta t$ (see [[Ex - The Exponential Map of so(2) is Surjective but Not Injective]]).

**Targets (Output Amplification)**

Combine (d) and (f) with **the identity $d_0\exp = \mathrm{id}_{\mathfrak{g}}$ and the inverse function theorem**. Differentiating $\exp(tX) = \gamma_X(t)$ at $t = 0$ gives $d_0\exp(X) = \gamma_X'(0) = X$, so $d_0\exp$ is the identity, and the inverse function theorem then makes $\exp$ a diffeomorphism from a neighbourhood of $0 \in \mathfrak{g}$ onto a neighbourhood of $e \in G$. The further result is that a connected Lie group is generated by any neighbourhood of $e$, hence by $\exp(\mathfrak{g})$: every element of a connected $G$ is a finite product of exponentials. This is carried out on [[Thm - The Exponential Map is a Local Diffeomorphism at the Origin]].

Combine (a) with **the naturality of $\exp$** to obtain rigidity of homomorphisms: two Lie group homomorphisms $\varphi, \psi : G \to H$ with $d_e\varphi = d_e\psi$ agree on $\exp(\mathfrak{g})$ (by the first source above), hence on the subgroup generated by $\exp(\mathfrak{g})$, which for connected $G$ is all of $G$. The extra ingredient is the previous target; the payoff is that a homomorphism out of a connected Lie group is determined by a linear map, which is the first step towards the correspondence between Lie group representations and Lie algebra representations used on [[Def - Representation of a Lie Algebra]] and in [[Thm - Complex Representations of U(1) and SU(2)]].

Combine (e) with **a smooth right action of $G$ on a manifold $P$**. For $\xi \in \mathfrak{g}$ the fundamental vector field is $\xi_P(p) := \tfrac{d}{dt}\big|_{t=0}\, p \cdot \exp(t\xi)$ ([[Def - Fundamental Vector Field of a Group Action]]). Because $t \mapsto \exp(t\xi)$ is a one-parameter subgroup, the curves $t \mapsto p \cdot \exp(t\xi)$ satisfy the flow law $p \cdot \exp((s+t)\xi) = (p \cdot \exp(s\xi)) \cdot \exp(t\xi)$, and the same two-curves argument that proves (e) shows they are the integral curves of $\xi_P$; hence every fundamental vector field is complete with flow $p \mapsto p \cdot \exp(t\xi)$. On a principal bundle these are the vertical directions, and the identity $\omega(\xi_P) = \xi$ that defines a connection form in chapter IV is a statement about exactly these flows.

Combine (d) with **the adjoint representation**. Since $t \mapsto \exp(tX)$ is a one-parameter subgroup and $\operatorname{Ad} : G \to GL(\mathfrak{g})$ is a Lie group homomorphism ([[Thm - Ad is a Smooth Representation and its Differential is ad]]), the composite $t \mapsto \operatorname{Ad}_{\exp(tX)}$ is a one-parameter subgroup of $GL(\mathfrak{g})$ with initial velocity $\operatorname{ad}_X$, hence equals $t \mapsto e^{t\,\operatorname{ad}_X}$. The payoff is the formula $\operatorname{Ad}_{\exp X} = e^{\operatorname{ad}_X}$, which is how one computes the gauge transformation of a local connection form $A \mapsto \operatorname{Ad}_{g^{-1}}A + g^*\theta$ for $g = \exp(X)$ in chapter IV.

---

# Why Is It True

**The mechanism is that left-invariance converts the group law into the time-translation symmetry of an autonomous differential equation, and uniqueness of solutions then forces the two to coincide.** Concretely: the integral-curve equation $\gamma'(t) = X^L_{\gamma(t)}$ is autonomous, so shifting a solution in time, $s \mapsto \gamma(t + s)$, produces another solution; and it is left-invariant, so translating a solution in the group, $s \mapsto g\gamma(s)$, produces another solution as well. Fix $t$ and take $g = \gamma(t)$. The two new solutions $s \mapsto \gamma(t + s)$ and $s \mapsto \gamma(t)\gamma(s)$ both pass through $\gamma(t)$ at $s = 0$. An autonomous first-order equation has exactly one solution through each point, so they are the same curve, which is the homomorphism identity $\gamma(t + s) = \gamma(t)\gamma(s)$. That is the entire converse direction; the forward direction is the same picture read backwards, since differentiating $\gamma(t + s) = \gamma(t)\gamma(s)$ in $s$ at $s = 0$ says precisely that the velocity at $\gamma(t)$ is the left translate of the velocity at $e$.

The completeness statement (b) has the same source. A solution that exists for a short time $(-\varepsilon, \varepsilon)$ near $e$ can be copied to a neighbourhood of any point $h$ by left translation, $s \mapsto h\,c(s)$, and the copies all have the same lifetime $\varepsilon$ — left-invariance is a uniformity statement: the equation looks the same at every point of $G$. A maximal solution that stopped at a finite time $b$ would, just before $b$, be at some point $h$, and the copy of $c$ based at $h$ would carry it $\varepsilon$ further. So it never stops. This is the one place where the group structure adds something genuinely new to the general theory of flows: on an arbitrary manifold a vector field can have integral curves that escape to infinity in finite time, and nothing rules that out; on a Lie group the homogeneity of a left-invariant field rules it out.

The identification of the flow with right translation, part (e), is the same two-curves argument once more: $s \mapsto g\gamma_X(s)$ is an integral curve of $X^L$ starting at $g$ (left translate of an integral curve), and by uniqueness it is *the* integral curve starting at $g$, which is by definition $s \mapsto \phi_s(g)$. It is worth noticing why the answer is a *right* translation: the flow moves each point $g$ along $g \gamma_X(s)$, multiplying on the right by the group element $\gamma_X(s)$, and this is the operation that commutes with all left translations, as it must, since the field being integrated is left-invariant.

Finally, the smoothness of $\exp$ is not a statement about any single curve $\gamma_X$ but about how the family $\{\gamma_X\}_{X \in \mathfrak{g}}$ varies with $X$. The differential-equations fact that provides this is smooth dependence of solutions on initial conditions, and the way to invoke it for a *parameter* $X$ rather than an initial point is to adjoin the parameter to the state: on the product manifold $G \times \mathfrak{g}$ consider the field $\Xi_{(g, X)} = (X^L_g, 0)$, whose integral curves are $t \mapsto (g\gamma_X(t), X)$. The flow of $\Xi$ is smooth in $(t, g, X)$ jointly by the [[Thm - Fundamental Theorem on Flows|fundamental theorem on flows]], and $\exp$ is the restriction of that flow to $t = 1$, $g = e$, followed by projection to $G$.

---

# What Makes This Hard

The non-obvious step is the converse direction of (a), which Bär leaves out: one must produce the homomorphism identity from the differential equation, and the trick — compare the two curves $s \mapsto \gamma(t + s)$ and $s \mapsto \gamma(t)\gamma(s)$, which are both integral curves through $\gamma(t)$ — is not suggested by the forward direction, whose proof is a one-line differentiation. A second subtlety is that the "if and only if" in (a) is only well-posed for curves defined on all of $\mathbb{R}$: a one-parameter subgroup has domain $\mathbb{R}$ by definition, whereas an integral curve from $e$ is a priori only guaranteed on some $(-\varepsilon, \varepsilon)$; so the completeness statement (b) is a prerequisite for the theorem, not a corollary of it, and its proof — the extension-by-translation argument of Bär's Exercise 1.4.1 — has to be written with the gluing of the two curves done properly, including the verification that the glued curve is smooth and is an integral curve on the union of the domains. The common error in (f) is to argue that "$\exp$ is smooth because each $\gamma_X$ is smooth": smoothness of each $\gamma_X$ in $t$ says nothing about smoothness in $X$, and the correct proof must make $X$ into a coordinate of the state space of a single vector field on $G \times \mathfrak{g}$.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Everything follows from two invariances of the equation $\gamma' = X^L_\gamma$ — it is autonomous (time shifts of solutions are solutions) and it is left-invariant (left translates of solutions are solutions) — together with the uniqueness of integral curves through a point. Use the two invariances to manufacture, from any solution, a second solution through the same point, and let uniqueness identify them. Completeness is the same idea used to extend a short-time solution step by step; smoothness of $\exp$ is smooth dependence on initial data for the augmented field $(X^L_g, 0)$ on $G \times \mathfrak{g}$.

**Subgoal decomposition:**

1. **Left translates of integral curves are integral curves.** Show that if $c$ is an integral curve of $X^L$ then so is $L_g \circ c$, for every $g \in G$.
   - *Hint:* Chain rule for curves, then left-invariance $d_hL_g(X^L_h) = X^L_{gh}$.
   - *Why needed:* This is the group-structure input to every later step: it is what makes the equation "look the same everywhere".

2. **Time shifts and rescalings of integral curves are integral curves.** Show that if $c$ is an integral curve of a field $Y$ then $t \mapsto c(\alpha t + s)$ is an integral curve of $\alpha Y$.
   - *Hint:* Chain rule with the affine map $\tau(t) = \alpha t + s$, whose differential multiplies $\tfrac{d}{dt}$ by $\alpha$.
   - *Why needed:* With $\alpha = 1$ it gives the time-translation symmetry used in (a); with $s = 0$ it gives the rescaling used to prove $\gamma_X(t) = \exp(tX)$.

3. **Homomorphism implies integral curve.** Differentiate $\gamma(t + s) = L_{\gamma(t)}(\gamma(s))$ with respect to $s$ at $s = 0$.
   - *Hint:* The left side gives $\gamma'(t)$ by Subgoal 2; the right side gives $d_eL_{\gamma(t)}(\gamma'(0)) = X^L_{\gamma(t)}$ with $X = \gamma'(0)$.
   - *Why needed:* This is the forward direction of (a).

4. **Integral curve from $e$ on $\mathbb{R}$ implies homomorphism.** For fixed $t$, show that $s \mapsto \gamma(t + s)$ and $s \mapsto \gamma(t)\gamma(s)$ are integral curves of $X^L$ through $\gamma(t)$ and invoke uniqueness.
   - *Hint:* Subgoal 2 for the first, Subgoal 1 for the second; both are defined on all of $\mathbb{R}$, and both take the value $\gamma(t)$ at $s = 0$ because $\gamma(0) = e$.
   - *Why needed:* This is the converse direction of (a), which the source does not prove.

5. **Completeness.** Take a short-time integral curve $c : (-\varepsilon, \varepsilon) \to G$ from $e$, suppose the maximal integral curve from $g$ has domain $(a, b)$ with $b < \infty$, and extend it past $b$ by gluing in $t \mapsto \gamma^{(g)}(t_0)\,c(t - t_0)$ for a $t_0$ within $\varepsilon$ of $b$.
   - *Hint:* Subgoals 1 and 2 show the glued-in curve is an integral curve; uniqueness makes it agree with $\gamma^{(g)}$ on the overlap; the union is an integral curve on a strictly larger interval, contradicting maximality. Repeat at $a$.
   - *Why needed:* It makes $\gamma_X$ a curve on all of $\mathbb{R}$, so that $\exp(X) = \gamma_X(1)$ is defined and (a) applies to it.

6. **Rescaling and the identities for $\exp$.** Show $\gamma_X(\alpha t) = \gamma_{\alpha X}(t)$, evaluate at $t = 1$ to get $\gamma_X(\alpha) = \exp(\alpha X)$, and read off the three identities from the homomorphism property of $\gamma_X$.
   - *Hint:* $t \mapsto \gamma_X(\alpha t)$ is an integral curve of $\alpha X^L = (\alpha X)^L$ starting at $e$ (Subgoal 2), so it is $\gamma_{\alpha X}$ by uniqueness.
   - *Why needed:* This is (d), and it is what turns the abstract family $\{\gamma_X\}$ into the single map $\exp$ restricted to lines.

7. **The flow is right translation, and $\exp$ is smooth.** For the flow: $s \mapsto g\gamma_X(s)$ is the integral curve from $g$ (Subgoal 1 and uniqueness). For smoothness: build the field $\Xi_{(g, X)} = (X^L_g, 0)$ on $G \times \mathfrak{g}$, check it is smooth using a basis of $\mathfrak{g}$, identify its integral curves as $t \mapsto (g\gamma_X(t), X)$, and apply the fundamental theorem on flows.
   - *Hint:* In a product chart, $\Xi = \sum_i (x^i \circ \pi_2)\,\widetilde{E_i}$ where $\widetilde{E_i}$ is the lift of the smooth field $E_i^L$; then $\exp = \pi_1 \circ \Phi^{\Xi}(1, (e, \cdot))$.
   - *Why needed:* (e) is the geometric meaning of the theorem and the model for fundamental vector fields; (f) is needed before $\exp$ can be differentiated anywhere.

---

# Lemma Decomposition

> [!note]- Lemma 1: Left translations are diffeomorphisms, and left translates of integral curves of $X^L$ are integral curves of $X^L$
> **Statement:** Let $G$ be a Lie group and $g \in G$. Then $L_g : G \to G$ is a diffeomorphism with inverse $L_{g^{-1}}$. Moreover, if $X \in \mathfrak{g}$ and $c : J \to G$ is an integral curve of $X^L$, then $L_g \circ c : J \to G$, $t \mapsto g\,c(t)$, is an integral curve of $X^L$.
>
> **Hint:** $L_g = m \circ (g, \mathrm{id}_G)$ is smooth; then apply the chain rule for curves to $L_g \circ c$ and use left-invariance at the point $c(t)$.
>
> **Why needed:** It is the group-theoretic input to every step of the proof: it lets a single integral curve be copied to every point of $G$.
>
> > [!note]- Full proof
> > **$L_g$ is a diffeomorphism.** The map $\iota_g : G \to G \times G$, $h \mapsto (g, h)$, is smooth (its components are the constant map and the identity), and $L_g = m \circ \iota_g$ with $m$ the multiplication map, which is smooth because $G$ is a Lie group ([[Def - Lie Group]]). Hence $L_g$ is smooth. For every $h \in G$,
> > $$L_{g^{-1}}(L_g(h)) = g^{-1}(gh) = (g^{-1}g)h = h \qquad \text{(associativity and the inverse axiom)},$$
> > and in the same way $L_g(L_{g^{-1}}(h)) = g(g^{-1}h) = h$. So $L_g$ is a bijection with inverse $L_{g^{-1}}$, and $L_{g^{-1}}$ is smooth by the same argument applied to $g^{-1}$. Therefore $L_g$ is a diffeomorphism ([[Def - Diffeomorphism]]).
> >
> > **Left translates of integral curves.** Assume $c : J \to G$ is an integral curve of $X^L$, that is, $c'(t) = X^L_{c(t)}$ for all $t \in J$. We need to show $(L_g \circ c)'(t) = X^L_{(L_g \circ c)(t)}$ for all $t \in J$. The curve $L_g \circ c$ is smooth as a composition of smooth maps. For $t \in J$,
> > $$(L_g \circ c)'(t) = d_{c(t)}L_g\big(c'(t)\big) \qquad \text{(chain rule for curves, [[Thm - Chain Rule for the Differential]])}$$
> > $$= d_{c(t)}L_g\big(X^L_{c(t)}\big) \qquad \text{(since } c \text{ is an integral curve of } X^L\text{)}$$
> > $$= X^L_{g\,c(t)} \qquad \text{(left-invariance of } X^L\text{: } d_hL_g(X^L_h) = X^L_{gh} \text{ with } h = c(t)\text{)}$$
> > $$= X^L_{(L_g \circ c)(t)} \qquad \text{(definition of } L_g\text{)}.$$
> > Therefore $L_g \circ c$ is an integral curve of $X^L$ on $J$. $\blacksquare$

> [!note]- Lemma 2: Affine reparametrisations of curves and of integral curves
> **Statement:** Let $M$ be a smooth manifold, $c : J \to M$ a smooth curve, and $\alpha, s \in \mathbb{R}$. Put $J' := \{t \in \mathbb{R} : \alpha t + s \in J\}$ and $\tilde c(t) := c(\alpha t + s)$ for $t \in J'$. Then $J'$ is an open interval (possibly empty), $\tilde c$ is smooth, and
> $$\tilde c\,'(t) = \alpha\, c'(\alpha t + s) \qquad (t \in J').$$
> In particular, if $c$ is an integral curve of a vector field $Y \in \mathfrak{X}(M)$, then $\tilde c$ is an integral curve of the vector field $\alpha Y$ on $J'$; and if moreover $\alpha = 1$, then $\tilde c : t \mapsto c(t + s)$ is an integral curve of $Y$ itself, with $\tilde c(0) = c(s)$ whenever $s \in J$.
>
> **Hint:** The differential of the affine map $\tau(t) = \alpha t + s$ sends $\tfrac{d}{dt}\big|_t$ to $\alpha\,\tfrac{d}{du}\big|_{\tau(t)}$; then use the chain rule and linearity of $dc$.
>
> **Why needed:** With $\alpha = 1$ it is the time-translation symmetry of an autonomous equation, used in the proof of (a) and of completeness; with $s = 0$ it is the rescaling used to prove $\gamma_X(t) = \exp(tX)$.
>
> > [!note]- Full proof
> > **The domain.** The map $\tau : \mathbb{R} \to \mathbb{R}$, $\tau(t) = \alpha t + s$, is continuous, so $J' = \tau^{-1}(J)$ is open. It is an interval: if $t_1 < t_2$ lie in $J'$ and $t_1 < t < t_2$, then $\tau(t)$ lies between $\tau(t_1)$ and $\tau(t_2)$ (an affine map is monotone, non-decreasing if $\alpha \geq 0$ and non-increasing if $\alpha \leq 0$), and $J$ is an interval, so $\tau(t) \in J$, that is, $t \in J'$. If $J'$ is empty there is nothing to prove, so assume it is not.
> >
> > **Smoothness and the velocity.** $\tilde c = c \circ \tau|_{J'}$ is a composition of smooth maps, hence smooth. Fix $t \in J'$ and write $u = \tau(t)$. The differential of $\tau$ at $t$ is the linear map $T_t\mathbb{R} \to T_u\mathbb{R}$ with
> > $$d\tau_t\Big(\tfrac{d}{dt}\Big|_t\Big) = \tau'(t)\,\tfrac{d}{du}\Big|_u = \alpha\,\tfrac{d}{du}\Big|_u \qquad \text{(the differential of a smooth function } \mathbb{R} \to \mathbb{R} \text{ is multiplication by its derivative, and } \tau'(t) = \alpha\text{)}.$$
> > Hence
> > $$\tilde c\,'(t) = d(c \circ \tau)_t\Big(\tfrac{d}{dt}\Big|_t\Big) = dc_u\Big(d\tau_t\Big(\tfrac{d}{dt}\Big|_t\Big)\Big) \qquad \text{(definition of velocity; [[Thm - Chain Rule for the Differential]])}$$
> > $$= dc_u\Big(\alpha\,\tfrac{d}{du}\Big|_u\Big) = \alpha\, dc_u\Big(\tfrac{d}{du}\Big|_u\Big) = \alpha\, c'(u) = \alpha\, c'(\alpha t + s) \qquad \text{(by the line above; linearity of } dc_u\text{; definition of } c'(u)\text{)}.$$
> >
> > **The integral-curve statement.** Assume now that $c'(u) = Y_{c(u)}$ for all $u \in J$. Then for $t \in J'$,
> > $$\tilde c\,'(t) = \alpha\, c'(\alpha t + s) = \alpha\, Y_{c(\alpha t + s)} = (\alpha Y)_{\tilde c(t)} \qquad \text{(by the velocity formula; the integral-curve equation at } u = \alpha t + s\text{; the definition of } \alpha Y \text{ and of } \tilde c\text{)},$$
> > so $\tilde c$ is an integral curve of $\alpha Y$. When $\alpha = 1$ this says $\tilde c$ is an integral curve of $Y$, and $\tilde c(0) = c(s)$ by definition, provided $s \in J$ (which is the condition $0 \in J'$). $\blacksquare$

> [!note]- Lemma 3: A smooth homomorphism $\mathbb{R} \to G$ is an integral curve of the left-invariant field generated by its initial velocity
> **Statement:** Let $\gamma : \mathbb{R} \to G$ be smooth with $\gamma(s + t) = \gamma(s)\gamma(t)$ for all $s, t \in \mathbb{R}$. Then $\gamma(0) = e$, and $\gamma$ is an integral curve of $X^L$, where $X := \gamma'(0) \in T_eG = \mathfrak{g}$.
>
> **Hint:** Write $\gamma(t + s) = L_{\gamma(t)}(\gamma(s))$ and differentiate in $s$ at $s = 0$.
>
> **Why needed:** This is the direction of (a) proved in the source, and the direction used to recognise exponentials in disguise.
>
> > [!note]- Full proof
> > **$\gamma(0) = e$.** Applying the homomorphism property with $s = t = 0$ gives $\gamma(0) = \gamma(0 + 0) = \gamma(0)\gamma(0)$; multiplying both sides on the left by $\gamma(0)^{-1}$ yields $e = \gamma(0)$.
> >
> > **The velocity at time $t$.** Fix $t \in \mathbb{R}$ and consider the two smooth curves $\mathbb{R} \to G$
> > $$\alpha(s) := \gamma(t + s), \qquad \beta(s) := \gamma(t)\gamma(s) = L_{\gamma(t)}(\gamma(s)).$$
> > By the homomorphism property, $\alpha(s) = \beta(s)$ for every $s \in \mathbb{R}$, so $\alpha = \beta$ as curves and in particular $\alpha'(0) = \beta'(0)$. We compute each side.
> >
> > **Compute $\alpha'(0)$:** by Lemma 2 with $\alpha = 1$ and shift $s \mapsto t$ (the lemma's $s$ is our $t$), $\alpha'(0) = \gamma'(t + 0) = \gamma'(t)$.
> >
> > **Compute $\beta'(0)$:**
> > $$\beta'(0) = (L_{\gamma(t)} \circ \gamma)'(0) = d_{\gamma(0)}L_{\gamma(t)}\big(\gamma'(0)\big) \qquad \text{(chain rule for curves, [[Thm - Chain Rule for the Differential]])}$$
> > $$= d_eL_{\gamma(t)}(X) = X^L_{\gamma(t)} \qquad \text{(since } \gamma(0) = e \text{ by the first step, } X = \gamma'(0) \text{ by definition, and } X^L_g = d_eL_g(X) \text{ by definition of } X^L\text{)}.$$
> >
> > **Conclude.** Combining the two computations, $\gamma'(t) = \alpha'(0) = \beta'(0) = X^L_{\gamma(t)}$. Since $t \in \mathbb{R}$ was arbitrary, $\gamma$ is an integral curve of $X^L$. $\blacksquare$

> [!note]- Lemma 4: An integral curve of a left-invariant field through $e$ defined on all of $\mathbb{R}$ is a homomorphism
> **Statement:** Let $X \in \mathfrak{g}$ and let $\gamma : \mathbb{R} \to G$ be an integral curve of $X^L$ with $\gamma(0) = e$. Then $\gamma(t + s) = \gamma(t)\gamma(s)$ for all $s, t \in \mathbb{R}$; that is, $\gamma$ is a one-parameter subgroup of $G$, and its initial velocity is $\gamma'(0) = X$.
>
> **Hint:** For fixed $t$, both $s \mapsto \gamma(t + s)$ and $s \mapsto \gamma(t)\gamma(s)$ are integral curves of $X^L$ that equal $\gamma(t)$ at $s = 0$.
>
> **Why needed:** This is the converse direction of (a), which the source omits; it is also what makes $\gamma_X$ a one-parameter subgroup.
>
> > [!note]- Full proof
> > Assume $\gamma : \mathbb{R} \to G$ satisfies $\gamma'(u) = X^L_{\gamma(u)}$ for all $u \in \mathbb{R}$ and $\gamma(0) = e$. We need to show that for every fixed $t \in \mathbb{R}$ the two curves $\mathbb{R} \to G$
> > $$\alpha(s) := \gamma(t + s), \qquad \beta(s) := \gamma(t)\gamma(s) = (L_{\gamma(t)} \circ \gamma)(s)$$
> > coincide.
> >
> > **$\alpha$ is an integral curve of $X^L$ with $\alpha(0) = \gamma(t)$.** By Lemma 2 (with $\alpha = 1$ and shift $t$; the domain is $\{s : s + t \in \mathbb{R}\} = \mathbb{R}$), $\alpha$ is an integral curve of $X^L$ on $\mathbb{R}$, and $\alpha(0) = \gamma(t)$ by definition.
> >
> > **$\beta$ is an integral curve of $X^L$ with $\beta(0) = \gamma(t)$.** By Lemma 1 applied with $g = \gamma(t)$ and $c = \gamma$, the curve $\beta = L_{\gamma(t)} \circ \gamma$ is an integral curve of $X^L$ on $\mathbb{R}$. Its value at $0$ is
> > $$\beta(0) = \gamma(t)\gamma(0) = \gamma(t)\, e = \gamma(t) \qquad \text{(by the hypothesis } \gamma(0) = e \text{ and the identity axiom)}.$$
> >
> > **Invoke uniqueness.** The theorem [[Thm - Existence and Uniqueness of Integral Curves]] states: if $\gamma_1 : J_1 \to M$ and $\gamma_2 : J_2 \to M$ are integral curves of the same smooth vector field with $\gamma_1(t_0) = \gamma_2(t_0)$ for some $t_0 \in J_1 \cap J_2$, then $\gamma_1 = \gamma_2$ on $J_1 \cap J_2$. Apply it with $M = G$, the field $X^L$ (smooth by [[Thm - Left-Invariant Vector Fields Form a Lie Algebra]]), $\gamma_1 = \alpha$, $\gamma_2 = \beta$, $J_1 = J_2 = \mathbb{R}$, $t_0 = 0$: the two previous steps give $\alpha(0) = \gamma(t) = \beta(0)$, so $\alpha = \beta$ on $\mathbb{R}$. That is, $\gamma(t + s) = \gamma(t)\gamma(s)$ for all $s \in \mathbb{R}$; as $t$ was arbitrary, this holds for all $s, t$.
> >
> > **Initial velocity.** $\gamma'(0) = X^L_{\gamma(0)} = X^L_e = X$ (integral-curve equation at $u = 0$; $\gamma(0) = e$; $X^L_e = d_eL_e(X) = X$ since $L_e = \mathrm{id}_G$ and $d(\mathrm{id}_G)_e = \mathrm{id}$ by [[Thm - Chain Rule for the Differential]]).
> >
> > Therefore $\gamma$ is a one-parameter subgroup of $G$ with initial velocity $X$. $\blacksquare$

> [!note]- Lemma 5: Every left-invariant vector field is complete (Bär's Exercise 1.4.1)
> **Statement:** Let $X \in \mathfrak{g}$. For every $g \in G$ the maximal integral curve $\gamma^{(g)} : \mathcal{D}^{(g)} \to G$ of $X^L$ starting at $g$ has domain $\mathcal{D}^{(g)} = \mathbb{R}$. Consequently $X^L$ is a complete vector field, and the curve $\gamma_X := \gamma^{(e)} : \mathbb{R} \to G$ — the unique integral curve of $X^L$ with $\gamma_X(0) = e$ — is defined on all of $\mathbb{R}$.
>
> **Hint:** Take a short-time integral curve $c$ from $e$ on $(-\varepsilon, \varepsilon)$. If the maximal curve from $g$ lived only on $(a, b)$ with $b < \infty$, pick $t_0$ within $\varepsilon$ of $b$ and glue in the left translate $t \mapsto \gamma^{(g)}(t_0)\, c(t - t_0)$, which reaches past $b$.
>
> **Why needed:** It is the precondition for the definition of $\gamma_X$ and of $\exp$, and it is what allows part (a) to be applied to $\gamma_X$.
>
> > [!note]- Full proof
> > Fix $X \in \mathfrak{g}$ and $g \in G$. We need to show $\mathcal{D}^{(g)} = \mathbb{R}$.
> >
> > **Step 0 — a short-time integral curve from the identity.** The field $X^L$ is a smooth vector field on $G$ ([[Thm - Left-Invariant Vector Fields Form a Lie Algebra]], Lemma 3 there). By the existence part of [[Thm - Existence and Uniqueness of Integral Curves]] — for every point $p$ of a smooth manifold and every smooth vector field there exist $\varepsilon > 0$ and an integral curve $(-\varepsilon, \varepsilon) \to M$ starting at $p$ — there are $\varepsilon > 0$ and a smooth integral curve $c : (-\varepsilon, \varepsilon) \to G$ of $X^L$ with $c(0) = e$. We fix this $\varepsilon$ and this $c$ for the rest of the proof; the same $\varepsilon$ will serve at every point of $G$, which is the uniformity that left-invariance provides.
> >
> > **Step 1 — the maximal curve and its domain.** By the Corollary (maximal integral curve) of [[Thm - Existence and Uniqueness of Integral Curves]], there is a unique maximal integral curve $\gamma^{(g)} : \mathcal{D}^{(g)} \to G$ of $X^L$ with $\gamma^{(g)}(0) = g$, and $\mathcal{D}^{(g)}$ is an open interval containing $0$; write $\mathcal{D}^{(g)} = (a, b)$ with $-\infty \leq a < 0 < b \leq \infty$. Maximality means, by the construction in Step 4 of the proof on that page (the maximal curve is the union of all integral curves starting at $g$, which agree on overlaps by uniqueness), that the domain of *every* integral curve of $X^L$ starting at $g$ is contained in $(a, b)$. We show $b = \infty$ and $a = -\infty$ by contradiction.
> >
> > **Step 2 — the right endpoint. Suppose, for a contradiction, that $b < \infty$.**
> >
> > **Choose the gluing time:** the sets $(b - \varepsilon, b)$ and $(a, b)$ are open intervals both having $b$ as right endpoint, so their intersection is a non-empty open interval; choose $t_0 \in (b - \varepsilon, b) \cap (a, b)$. Then $t_0 \in \mathcal{D}^{(g)}$ and $b - t_0 < \varepsilon$. Put $h := \gamma^{(g)}(t_0) \in G$.
> >
> > **Build the translated curve:** define $\sigma : (t_0 - \varepsilon, t_0 + \varepsilon) \to G$ by
> > $$\sigma(t) := h\, c(t - t_0) = \big(L_h \circ \tilde c\big)(t), \qquad \text{where } \tilde c(t) := c(t - t_0).$$
> > By Lemma 2 (with $\alpha = 1$ and shift $-t_0$; the domain $\{t : t - t_0 \in (-\varepsilon, \varepsilon)\}$ is $(t_0 - \varepsilon, t_0 + \varepsilon)$), $\tilde c$ is an integral curve of $X^L$; by Lemma 1 (with the group element $h$), $\sigma = L_h \circ \tilde c$ is an integral curve of $X^L$ on $(t_0 - \varepsilon, t_0 + \varepsilon)$. Its value at $t_0$ is
> > $$\sigma(t_0) = h\, c(0) = h\, e = h = \gamma^{(g)}(t_0) \qquad \text{(by } c(0) = e \text{ from Step 0, the identity axiom, and the definition of } h\text{)}.$$
> >
> > **The two curves agree on the overlap:** $\sigma$ and $\gamma^{(g)}$ are integral curves of the same field $X^L$, their domains $(t_0 - \varepsilon, t_0 + \varepsilon)$ and $(a, b)$ both contain $t_0$, and they take the same value at $t_0$. By the uniqueness part of [[Thm - Existence and Uniqueness of Integral Curves]] (restated in Lemma 4), $\sigma = \gamma^{(g)}$ on the intersection $I := (t_0 - \varepsilon, t_0 + \varepsilon) \cap (a, b)$.
> >
> > **Glue:** let $J' := (a, b) \cup (t_0 - \varepsilon, t_0 + \varepsilon)$. Since the two open intervals share the point $t_0$, their union is the open interval $J' = \big(\min(a, t_0 - \varepsilon),\ \max(b, t_0 + \varepsilon)\big) = \big(\min(a, t_0 - \varepsilon),\ t_0 + \varepsilon\big)$, where the last equality holds because $t_0 + \varepsilon > b$ (as $b - t_0 < \varepsilon$). Define $\hat\gamma : J' \to G$ by
> > $$\hat\gamma(t) := \begin{cases} \gamma^{(g)}(t), & t \in (a, b), \\ \sigma(t), & t \in (t_0 - \varepsilon, t_0 + \varepsilon). \end{cases}$$
> > This is well defined, because on the overlap $I$ the two prescriptions agree by the previous step.
> >
> > **$\hat\gamma$ is an integral curve of $X^L$ starting at $g$:** smoothness is a local property, and every $t \in J'$ has an open neighbourhood — either $(a, b)$ or $(t_0 - \varepsilon, t_0 + \varepsilon)$ — on which $\hat\gamma$ coincides with a smooth curve, so $\hat\gamma$ is smooth; likewise, at every $t \in J'$ the velocity $\hat\gamma'(t)$ equals the velocity of whichever of $\gamma^{(g)}$, $\sigma$ agrees with $\hat\gamma$ near $t$, and that velocity is $X^L$ at the point, because both are integral curves of $X^L$. Finally $0 \in (a, b)$ and $\hat\gamma(0) = \gamma^{(g)}(0) = g$.
> >
> > **The contradiction:** $\hat\gamma$ is an integral curve of $X^L$ starting at $g$ whose domain $J'$ contains the point $b$ (since $b < t_0 + \varepsilon$ and $b > t_0 - \varepsilon$), whereas $b \notin (a, b) = \mathcal{D}^{(g)}$. This contradicts the maximality property recorded in Step 1, namely that the domain of every integral curve starting at $g$ is contained in $\mathcal{D}^{(g)}$. Hence $b = \infty$.
> >
> > **Step 3 — the left endpoint. Suppose, for a contradiction, that $a > -\infty$.** The argument is the mirror image of Step 2, and we write it out. Choose $t_0 \in (a, a + \varepsilon) \cap (a, b)$, a non-empty open interval since both intervals have left endpoint $a$; then $t_0 \in \mathcal{D}^{(g)}$ and $t_0 - a < \varepsilon$. Put $h := \gamma^{(g)}(t_0)$ and define $\sigma : (t_0 - \varepsilon, t_0 + \varepsilon) \to G$, $\sigma(t) := h\, c(t - t_0)$, exactly as before. By Lemma 2 and Lemma 1, $\sigma$ is an integral curve of $X^L$, and $\sigma(t_0) = h\,c(0) = h = \gamma^{(g)}(t_0)$ as before. By uniqueness, $\sigma = \gamma^{(g)}$ on $(t_0 - \varepsilon, t_0 + \varepsilon) \cap (a, b)$. The union $J' = (a, b) \cup (t_0 - \varepsilon, t_0 + \varepsilon)$ is the open interval $\big(t_0 - \varepsilon,\ \max(b, t_0 + \varepsilon)\big)$, because $t_0 - \varepsilon < a$ (as $t_0 - a < \varepsilon$); it contains the point $a$. The glued curve $\hat\gamma : J' \to G$, equal to $\gamma^{(g)}$ on $(a, b)$ and to $\sigma$ on $(t_0 - \varepsilon, t_0 + \varepsilon)$, is well defined on the overlap, smooth and an integral curve of $X^L$ by the same local argument, and satisfies $\hat\gamma(0) = g$. Its domain contains $a \notin \mathcal{D}^{(g)}$, contradicting the maximality of $\mathcal{D}^{(g)}$. Hence $a = -\infty$.
> >
> > **Conclusion.** $\mathcal{D}^{(g)} = (-\infty, \infty) = \mathbb{R}$ for every $g \in G$. By [[Def - Complete Vector Field]] (a vector field is complete if and only if every maximal integral curve is defined on all of $\mathbb{R}$), $X^L$ is complete. In particular, taking $g = e$, the maximal integral curve $\gamma_X := \gamma^{(e)}$ of $X^L$ with $\gamma_X(0) = e$ is defined on all of $\mathbb{R}$, and it is unique by the Corollary of [[Thm - Existence and Uniqueness of Integral Curves]]. $\blacksquare$

> [!note]- Lemma 6: Rescaling, $\gamma_X(t) = \exp(tX)$, and the three identities for $\exp$ along a line
> **Statement:** For $X \in \mathfrak{g}$ and $\alpha \in \mathbb{R}$, $\gamma_X(\alpha t) = \gamma_{\alpha X}(t)$ for all $t \in \mathbb{R}$. Consequently, with $\exp(X) := \gamma_X(1)$:
> $$\gamma_X(t) = \exp(tX), \qquad \exp\big((s + t)X\big) = \exp(sX)\exp(tX), \qquad \exp(0) = e, \qquad \exp(-X) = \exp(X)^{-1} \qquad (s, t \in \mathbb{R}).$$
>
> **Hint:** $t \mapsto \gamma_X(\alpha t)$ is an integral curve of $\alpha X^L = (\alpha X)^L$ starting at $e$; uniqueness identifies it with $\gamma_{\alpha X}$. Then set $t = 1$, and use Lemma 4 for the identities.
>
> **Why needed:** This is Bär's equation (1.6) and its three consequences; it converts the family of curves $\{\gamma_X\}$ into the single map $\exp$.
>
> > [!note]- Full proof
> > Fix $X \in \mathfrak{g}$ and $\alpha \in \mathbb{R}$. By Lemma 5, $\gamma_X : \mathbb{R} \to G$ and $\gamma_{\alpha X} : \mathbb{R} \to G$ are defined on all of $\mathbb{R}$.
> >
> > **The rescaled curve is an integral curve of $(\alpha X)^L$.** Put $\tilde\gamma(t) := \gamma_X(\alpha t)$, $t \in \mathbb{R}$ (the domain is $\{t : \alpha t \in \mathbb{R}\} = \mathbb{R}$). By Lemma 2 with shift $0$, $\tilde\gamma$ is an integral curve of the vector field $\alpha X^L$. Now
> > $$\alpha X^L = (\alpha X)^L \qquad \text{(since } (\alpha X)^L_g = d_eL_g(\alpha X) = \alpha\, d_eL_g(X) = \alpha X^L_g \text{ by linearity of } d_eL_g\text{)},$$
> > so $\tilde\gamma$ is an integral curve of $(\alpha X)^L$, and $\tilde\gamma(0) = \gamma_X(0) = e$.
> >
> > **Identify it with $\gamma_{\alpha X}$.** Both $\tilde\gamma$ and $\gamma_{\alpha X}$ are integral curves of $(\alpha X)^L$ on $\mathbb{R}$ with value $e$ at $0$; by the uniqueness part of [[Thm - Existence and Uniqueness of Integral Curves]] (restated in Lemma 4), $\tilde\gamma = \gamma_{\alpha X}$ on $\mathbb{R}$. That is,
> > $$\gamma_X(\alpha t) = \gamma_{\alpha X}(t) \qquad (t \in \mathbb{R}). \tag{6.1}$$
> >
> > **The formula $\gamma_X(t) = \exp(tX)$.** Put $t = 1$ in (6.1): $\gamma_X(\alpha) = \gamma_{\alpha X}(1) = \exp(\alpha X)$ by the definition of $\exp$. Renaming $\alpha$ as $t$ gives $\gamma_X(t) = \exp(tX)$ for all $t \in \mathbb{R}$. This is Bär's (1.6).
> >
> > **The identity $\exp((s + t)X) = \exp(sX)\exp(tX)$.** By Lemma 5, $\gamma_X$ is an integral curve of $X^L$ on $\mathbb{R}$ with $\gamma_X(0) = e$, so by Lemma 4 it is a homomorphism: $\gamma_X(s + t) = \gamma_X(s)\gamma_X(t)$. Substituting $\gamma_X(u) = \exp(uX)$ (the previous step) for $u = s + t, s, t$ gives $\exp((s + t)X) = \exp(sX)\exp(tX)$.
> >
> > **The identity $\exp(0) = e$.** The zero vector $0 \in \mathfrak{g}$ equals $0 \cdot X$, so $\exp(0) = \exp(0 \cdot X) = \gamma_X(0) = e$ by the formula $\gamma_X(t) = \exp(tX)$ at $t = 0$ and the initial condition of $\gamma_X$. (Equivalently: $0^L$ is the zero vector field, whose integral curve from $e$ is the constant curve $e$, so $\gamma_0(1) = e$.)
> >
> > **The identity $\exp(-X) = \exp(X)^{-1}$.** By the additivity identity with $s = -1$, $t = 1$:
> > $$\exp(-X)\exp(X) = \exp\big((-1 + 1)X\big) = \exp(0) = e \qquad \text{(additivity; } (-1 + 1)X = 0\text{; the previous step)},$$
> > and with $s = 1$, $t = -1$: $\exp(X)\exp(-X) = \exp(0) = e$. So $\exp(-X)$ is a two-sided inverse of $\exp(X)$, and inverses in a group are unique; hence $\exp(-X) = \exp(X)^{-1}$. $\blacksquare$

> [!note]- Lemma 7: The flow of $X^L$ is right translation by $\exp(tX)$
> **Statement:** For $X \in \mathfrak{g}$, the flow $\phi := \phi^{X^L}$ of $X^L$ has domain $\mathbb{R} \times G$ and is given by $\phi_t(g) = g\,\gamma_X(t) = g\exp(tX) = R_{\exp(tX)}(g)$. Each $\phi_t = R_{\exp(tX)}$ is a diffeomorphism of $G$ with inverse $R_{\exp(-tX)}$, and $R_{\exp(sX)} \circ R_{\exp(tX)} = R_{\exp((s + t)X)}$, $R_{\exp(0)} = \mathrm{id}_G$.
>
> **Hint:** $s \mapsto g\gamma_X(s)$ is the left translate by $g$ of an integral curve, so it is the integral curve starting at $g$; then read off the group law from Lemma 6.
>
> **Why needed:** It is part (e) of the theorem: the geometric meaning of the exponential map and the prototype of the flow of a fundamental vector field on a principal bundle.
>
> > [!note]- Full proof
> > Fix $X \in \mathfrak{g}$ and $g \in G$. By Lemma 5 the flow domain of $X^L$ is $\mathbb{R} \times G$, and by the [[Thm - Fundamental Theorem on Flows|fundamental theorem on flows]], part (a) — for each point $p$ the curve $t \mapsto \phi(t, p)$ is the unique maximal integral curve of the field starting at $p$ — the curve $t \mapsto \phi_t(g)$ is the unique integral curve of $X^L$ on $\mathbb{R}$ starting at $g$.
> >
> > **The candidate curve.** Let $\beta(t) := g\,\gamma_X(t) = (L_g \circ \gamma_X)(t)$, $t \in \mathbb{R}$. By Lemma 1 (with $c = \gamma_X$, which is an integral curve of $X^L$ on $\mathbb{R}$ by Lemma 5), $\beta$ is an integral curve of $X^L$ on $\mathbb{R}$, and $\beta(0) = g\,\gamma_X(0) = g\,e = g$.
> >
> > **Identify.** Both $t \mapsto \phi_t(g)$ and $\beta$ are integral curves of $X^L$ on $\mathbb{R}$ starting at $g$, so by uniqueness ([[Thm - Existence and Uniqueness of Integral Curves]], restated in Lemma 4) they coincide: $\phi_t(g) = g\,\gamma_X(t)$ for all $t$. By Lemma 6, $\gamma_X(t) = \exp(tX)$, so $\phi_t(g) = g\exp(tX) = R_{\exp(tX)}(g)$. As $g$ was arbitrary, $\phi_t = R_{\exp(tX)}$ as maps $G \to G$.
> >
> > **The one-parameter group of diffeomorphisms.** By the fundamental theorem on flows, part (c), with $M_t = G$ for every $t$ (the flow domain is all of $\mathbb{R} \times G$): each $\phi_t : G \to G$ is a diffeomorphism with inverse $\phi_{-t}$. Hence $R_{\exp(tX)}$ is a diffeomorphism with inverse $R_{\exp(-tX)}$ — consistent with the direct computation $R_{\exp(-tX)}(R_{\exp(tX)}(g)) = g\exp(tX)\exp(-tX) = g\exp(0) = g$, which uses Lemma 6. For the group law, for $g \in G$,
> > $$\big(R_{\exp(sX)} \circ R_{\exp(tX)}\big)(g) = g\exp(tX)\exp(sX) = g\exp\big((t + s)X\big) = R_{\exp((s + t)X)}(g) \qquad \text{(definition of } R\text{; Lemma 6 additivity; commutativity of addition in } \mathbb{R}\text{)},$$
> > and $R_{\exp(0)} = R_e = \mathrm{id}_G$ since $\exp(0) = e$ (Lemma 6). Therefore $\{R_{\exp(tX)}\}_{t \in \mathbb{R}}$ is a one-parameter group of diffeomorphisms of $G$, in the sense of [[Def - Complete Vector Field]]. $\blacksquare$

> [!note]- Lemma 8: The exponential map is smooth
> **Statement:** The map $\exp : \mathfrak{g} \to G$, $\exp(X) = \gamma_X(1)$, is smooth, where $\mathfrak{g}$ carries its standard smooth structure as a finite-dimensional real vector space.
>
> **Hint:** Adjoin the parameter to the state: on $G \times \mathfrak{g}$ the vector field $\Xi_{(g, X)} = (X^L_g, 0)$ is smooth, its integral curve through $(g, X)$ is $t \mapsto (g\gamma_X(t), X)$, and its flow is jointly smooth by the fundamental theorem on flows; $\exp$ is that flow at time $1$ from $(e, X)$, projected to $G$.
>
> **Why needed:** It is part (f); without it $\exp$ cannot be differentiated, and the local diffeomorphism theorem of the next page cannot be stated.
>
> > [!note]- Full proof
> > **Step 0 — the manifolds.** Let $n := \dim G = \dim \mathfrak{g}$ ([[Thm - Left-Invariant Vector Fields Form a Lie Algebra]], Corollary (dimension)). Choose a basis $E_1, \dots, E_n$ of $\mathfrak{g}$ and let $x^1, \dots, x^n : \mathfrak{g} \to \mathbb{R}$ be the corresponding linear coordinate functionals, so that $X = \sum_{i=1}^n x^i(X)E_i$ for every $X \in \mathfrak{g}$. The map $(x^1, \dots, x^n) : \mathfrak{g} \to \mathbb{R}^n$ is a global chart making $\mathfrak{g}$ a smooth manifold; two such charts differ by a linear isomorphism of $\mathbb{R}^n$, which is a diffeomorphism, so the smooth structure does not depend on the basis. Let $N := G \times \mathfrak{g}$ with the product smooth structure ([[Thm - Product of Smooth Manifolds is a Smooth Manifold]]) and let $\pi_1 : N \to G$, $\pi_2 : N \to \mathfrak{g}$ be the projections, which are smooth. For every $(g, X) \in N$ define the linear map
> > $$\alpha_{(g, X)} : T_{(g, X)}N \to T_gG \oplus T_X\mathfrak{g}, \qquad v \mapsto \big(d(\pi_1)_{(g, X)}(v),\ d(\pi_2)_{(g, X)}(v)\big).$$
> > **$\alpha_{(g, X)}$ is a linear isomorphism.** It is linear because each differential is linear. Let $(U, (y^1, \dots, y^n))$ be a chart of $G$ around $g$; then $(U \times \mathfrak{g}, (y^1 \circ \pi_1, \dots, y^n \circ \pi_1, x^1 \circ \pi_2, \dots, x^n \circ \pi_2))$ is a chart of $N$ around $(g, X)$ — a product chart, which is how the product smooth structure on $N$ is defined — and in these coordinates $\pi_1$ is the map $(y, x) \mapsto y$ and $\pi_2$ is the map $(y, x) \mapsto x$. The coordinate vectors $\partial/\partial y^1, \dots, \partial/\partial y^n, \partial/\partial x^1, \dots, \partial/\partial x^n$ at $(g, X)$ form a basis of $T_{(g, X)}N$, which has dimension $2n$. The differential of a map between charted manifolds acts on coordinate vectors through the Jacobian of its coordinate expression ([[Thm - Chain Rule for the Differential]] applied to the composition with the charts), and the Jacobians of $(y, x) \mapsto y$ and $(y, x) \mapsto x$ are the two block projections; hence
> > $$d\pi_1\Big(\frac{\partial}{\partial y^j}\Big) = \frac{\partial}{\partial y^j}\Big|_g, \quad d\pi_1\Big(\frac{\partial}{\partial x^i}\Big) = 0, \quad d\pi_2\Big(\frac{\partial}{\partial y^j}\Big) = 0, \quad d\pi_2\Big(\frac{\partial}{\partial x^i}\Big) = \frac{\partial}{\partial x^i}\Big|_X \qquad \text{(Jacobians of the coordinate expressions of } \pi_1, \pi_2\text{)}.$$
> > Therefore $\alpha_{(g, X)}$ sends the basis $\{\partial/\partial y^j\}_j \cup \{\partial/\partial x^i\}_i$ of $T_{(g, X)}N$ to the family $\{(\partial/\partial y^j|_g, 0)\}_j \cup \{(0, \partial/\partial x^i|_X)\}_i$, which is a basis of $T_gG \oplus T_X\mathfrak{g}$ (the coordinate vectors of a chart form a basis of each tangent space, and the direct sum of two bases is a basis). A linear map carrying a basis to a basis is an isomorphism, so $\alpha_{(g, X)}$ is a linear isomorphism. We use it to write tangent vectors to $N$ as pairs, and we record for Step 1 the two block identities just proved.
> >
> > **Step 1 — the augmented vector field and its smoothness.** Define a (rough) vector field $\Xi$ on $N$ by
> > $$\Xi_{(g, X)} := \alpha_{(g, X)}^{-1}\big(X^L_g,\ 0\big) \in T_{(g, X)}N .$$
> > We need to show $\Xi$ is smooth. For each $i$, define the vector field $\widetilde{E_i}$ on $N$ by $(\widetilde{E_i})_{(g, X)} := \alpha_{(g, X)}^{-1}\big((E_i)^L_g, 0\big)$. We claim each $\widetilde{E_i}$ is smooth. Let $(U, (y^1, \dots, y^n))$ be a chart of $G$ and take the product chart $(U \times \mathfrak{g}, (y \circ \pi_1, x \circ \pi_2))$ of $N$ as in Step 0. By the block identities of Step 0, $d\pi_1$ sends the coordinate vector $\partial/\partial y^j$ of $N$ to the coordinate vector $\partial/\partial y^j$ of $G$ and sends $\partial/\partial x^i$ to $0$, while $d\pi_2$ sends $\partial/\partial y^j$ to $0$ and $\partial/\partial x^i$ to $\partial/\partial x^i$. Consequently, if $(E_i)^L = \sum_j a_i^j\, \partial/\partial y^j$ on $U$ with coefficient functions $a_i^j \in C^\infty(U)$ — smooth because $(E_i)^L$ is a smooth vector field on $G$ by [[Thm - Left-Invariant Vector Fields Form a Lie Algebra]] (its Lemma 3, "smoothness is automatic") — then
> > $$\widetilde{E_i} = \sum_{j=1}^n (a_i^j \circ \pi_1)\, \frac{\partial}{\partial y^j} \quad \text{on } U \times \mathfrak{g} \qquad \text{(since } \alpha \text{ maps } \partial/\partial y^j \text{ to } (\partial/\partial y^j, 0) \text{ by the block computation, so } \alpha^{-1}(\sum_j a_i^j \partial_{y^j}, 0) = \sum_j a_i^j\, \partial_{y^j}\text{)}.$$
> > The coefficients $a_i^j \circ \pi_1$ are smooth on $U \times \mathfrak{g}$, so $\widetilde{E_i}$ is smooth on every product chart domain, hence smooth on $N$ ([[Def - Smooth Vector Field]]: a vector field is smooth if and only if its coefficient functions in every chart are smooth). Now for $(g, X) \in N$,
> > $$X^L_g = d_eL_g\Big(\sum_i x^i(X)E_i\Big) = \sum_i x^i(X)\, d_eL_g(E_i) = \sum_i x^i(X)\,(E_i)^L_g \qquad \text{(definition of } X^L\text{; linearity of } d_eL_g\text{; definition of } (E_i)^L\text{)},$$
> > and applying the linear map $\alpha^{-1}_{(g, X)}$ to $(X^L_g, 0) = \sum_i x^i(X)\,((E_i)^L_g, 0)$ gives
> > $$\Xi = \sum_{i=1}^n (x^i \circ \pi_2)\, \widetilde{E_i} \qquad \text{(linearity of } \alpha^{-1}\text{; } x^i(X) = (x^i \circ \pi_2)(g, X)\text{)}.$$
> > Each $x^i \circ \pi_2$ is smooth on $N$ (a linear functional composed with a smooth projection), each $\widetilde{E_i}$ is smooth, and a finite sum of smooth functions times smooth vector fields is a smooth vector field. Therefore $\Xi \in \mathfrak{X}(N)$.
> >
> > **Step 2 — the integral curves of $\Xi$.** Fix $(g, X) \in N$ and define $c : \mathbb{R} \to N$, $c(t) := \big(g\,\gamma_X(t),\ X\big)$; here $\gamma_X$ is defined on all of $\mathbb{R}$ by Lemma 5. The curve $c$ is smooth, because its two components $\pi_1 \circ c = L_g \circ \gamma_X$ and $\pi_2 \circ c \equiv X$ are smooth (a map into a product is smooth if and only if its components are). Its velocity satisfies, for every $t$,
> > $$\alpha_{c(t)}\big(c'(t)\big) = \big(d\pi_1(c'(t)),\ d\pi_2(c'(t))\big) = \big((\pi_1 \circ c)'(t),\ (\pi_2 \circ c)'(t)\big) \qquad \text{(definition of } \alpha\text{; chain rule for curves)}$$
> > $$= \big((L_g \circ \gamma_X)'(t),\ 0\big) = \big(X^L_{g\gamma_X(t)},\ 0\big) \qquad \text{(the second component is constant; Lemma 1: } L_g \circ \gamma_X \text{ is an integral curve of } X^L\text{)},$$
> > so $c'(t) = \alpha_{c(t)}^{-1}\big(X^L_{g\gamma_X(t)}, 0\big) = \Xi_{c(t)}$ by the definition of $\Xi$ at the point $c(t) = (g\gamma_X(t), X)$. Thus $c$ is an integral curve of $\Xi$ on $\mathbb{R}$ starting at $c(0) = (g\gamma_X(0), X) = (g, X)$.
> >
> > **Step 3 — the flow of $\Xi$ is global and smooth.** By the [[Thm - Fundamental Theorem on Flows|fundamental theorem on flows]] applied to the smooth vector field $\Xi$ on $N$: there is a unique smooth maximal flow $\Phi : \mathcal{D}_\Xi \to N$ generated by $\Xi$, and for each point $q \in N$ the curve $t \mapsto \Phi(t, q)$ is the unique maximal integral curve of $\Xi$ starting at $q$. By Step 2 the integral curve $c$ starting at $q = (g, X)$ is defined on all of $\mathbb{R}$; since the maximal integral curve extends every integral curve starting at $q$ (Step 4 of the proof of [[Thm - Existence and Uniqueness of Integral Curves]]) and is unique, $\mathcal{D}_\Xi^{(q)} = \mathbb{R}$ and $\Phi(t, (g, X)) = c(t) = (g\gamma_X(t), X)$ for all $t$. Hence $\mathcal{D}_\Xi = \mathbb{R} \times N$ and
> > $$\Phi : \mathbb{R} \times G \times \mathfrak{g} \to G \times \mathfrak{g}, \qquad \Phi(t, g, X) = \big(g\,\gamma_X(t),\ X\big),$$
> > is smooth (the fundamental theorem on flows asserts that the flow is smooth on its flow domain).
> >
> > **Step 4 — $\exp$ as a composition.** Define $\iota : \mathfrak{g} \to \mathbb{R} \times G \times \mathfrak{g}$, $\iota(X) := (1, e, X)$; it is smooth, its components being constants and the identity of $\mathfrak{g}$. Then for every $X \in \mathfrak{g}$,
> > $$(\pi_1 \circ \Phi \circ \iota)(X) = \pi_1\big(e\,\gamma_X(1),\ X\big) = \gamma_X(1) = \exp(X) \qquad \text{(Step 3 at } (t, g) = (1, e)\text{; } e\gamma_X(1) = \gamma_X(1)\text{; definition of } \exp\text{)}.$$
> > So $\exp = \pi_1 \circ \Phi \circ \iota$ is a composition of three smooth maps and is therefore smooth. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $G$ be a Lie group with Lie algebra $\mathfrak{g} = T_eG$. We prove the six parts in the order (b), (a), (c), (d), (e), (f); (b) comes first because the objects $\gamma_X$ and $\exp$ that appear in the later parts exist only once (b) is known.
>
> **Step 0 — the objects are well defined.** For each $X \in \mathfrak{g}$ the left-invariant vector field $X^L$, $X^L_g = d_eL_g(X)$, is a smooth vector field on $G$ by [[Thm - Left-Invariant Vector Fields Form a Lie Algebra]], so the theory of integral curves and flows on the manifold $G$ ([[Thm - Existence and Uniqueness of Integral Curves]], [[Thm - Fundamental Theorem on Flows]]) applies to it. By the Corollary (maximal integral curve) of the former, for every $g \in G$ there is a unique maximal integral curve $\gamma^{(g)} : \mathcal{D}^{(g)} \to G$ of $X^L$ with $\gamma^{(g)}(0) = g$.
>
> **Part (b) — completeness.** We need to show $\mathcal{D}^{(g)} = \mathbb{R}$ for every $g \in G$ and every $X \in \mathfrak{g}$. This is Lemma 5. Consequently $X^L$ is complete, and $\gamma_X := \gamma^{(e)} : \mathbb{R} \to G$ is the unique integral curve of $X^L$ with $\gamma_X(0) = e$, defined on all of $\mathbb{R}$. From now on $\exp(X) := \gamma_X(1)$ is a well-defined map $\mathfrak{g} \to G$.
>
> **Part (a) — characterisation.** Let $\gamma : \mathbb{R} \to G$ be smooth with $\gamma(0) = e$. We need to show that $\gamma$ is a group homomorphism if and only if it is an integral curve of some left-invariant vector field, and that in that case the field is $X^L$ with $X = \gamma'(0)$.
>
> *Direction 1 ($\Rightarrow$).* Assume $\gamma(s + t) = \gamma(s)\gamma(t)$ for all $s, t \in \mathbb{R}$. By Lemma 3, $\gamma$ is an integral curve of $X^L$ with $X = \gamma'(0)$; in particular $\gamma$ is an integral curve of a left-invariant vector field.
>
> *Direction 2 ($\Leftarrow$).* Assume $\gamma$ is an integral curve of a left-invariant vector field $Y$. By [[Thm - Left-Invariant Vector Fields Form a Lie Algebra]] (the evaluation map is a bijection), $Y = X^L$ for the unique $X := Y_e \in \mathfrak{g}$. The hypotheses of Lemma 4 hold — $\gamma$ is an integral curve of $X^L$ defined on all of $\mathbb{R}$ with $\gamma(0) = e$ — so by Lemma 4, $\gamma(s + t) = \gamma(s)\gamma(t)$ for all $s, t$, and $\gamma'(0) = X$. Thus $\gamma$ is a group homomorphism, and the field it integrates is $X^L$ with $X = \gamma'(0)$.
>
> Both directions being proved, (a) holds.
>
> **Part (c) — uniqueness of one-parameter subgroups.** We need to show that $\gamma \mapsto \gamma'(0)$ is a bijection from the set of one-parameter subgroups of $G$ onto $\mathfrak{g}$ with inverse $X \mapsto \gamma_X$.
>
> *$\gamma_X$ is a one-parameter subgroup with velocity $X$:* by Part (b), $\gamma_X$ is an integral curve of $X^L$ on $\mathbb{R}$ with $\gamma_X(0) = e$; by Lemma 4 it is a homomorphism with $\gamma_X'(0) = X$. So $X \mapsto \gamma_X$ maps $\mathfrak{g}$ into the set of one-parameter subgroups, and $\gamma \mapsto \gamma'(0)$ composed with it is the identity of $\mathfrak{g}$.
>
> *Every one-parameter subgroup is some $\gamma_X$:* let $\gamma$ be a one-parameter subgroup and put $X := \gamma'(0)$. By Lemma 3, $\gamma$ is an integral curve of $X^L$ on $\mathbb{R}$ with $\gamma(0) = e$. By the uniqueness part of [[Thm - Existence and Uniqueness of Integral Curves]] (two integral curves of the same field that agree at one time agree on their common domain), $\gamma = \gamma_X$ on $\mathbb{R}$. So $X \mapsto \gamma_X$ composed with $\gamma \mapsto \gamma'(0)$ is the identity on one-parameter subgroups.
>
> The two composites being identities, both maps are bijections, inverse to each other. This proves (c) and, with Part (d) below, the Corollary.
>
> **Part (d) — the exponential map along lines.** We need to show $\gamma_X(t) = \exp(tX)$, $\exp((s + t)X) = \exp(sX)\exp(tX)$, $\exp(0) = e$, and $\exp(-X) = \exp(X)^{-1}$ for all $X \in \mathfrak{g}$ and $s, t \in \mathbb{R}$. All four are proved in Lemma 6 (whose input is Parts (b) and (a) through Lemmas 5 and 4).
>
> **Part (e) — the flow is right translation.** We need to show that the flow $\phi^{X^L}$ has domain $\mathbb{R} \times G$ and $\phi^{X^L}_t = R_{\exp(tX)}$, and that these form a one-parameter group of diffeomorphisms. The flow domain is $\mathbb{R} \times G$ by Part (b) and the definition of the flow ([[Def - Flow of a Vector Field]]: the flow domain is $\{(t, g) : t \in \mathcal{D}^{(g)}\}$). The formula $\phi_t(g) = g\gamma_X(t) = g\exp(tX) = R_{\exp(tX)}(g)$, the fact that each $R_{\exp(tX)}$ is a diffeomorphism with inverse $R_{\exp(-tX)}$, and the group law $R_{\exp(sX)} \circ R_{\exp(tX)} = R_{\exp((s+t)X)}$, $R_{\exp(0)} = \mathrm{id}_G$, are Lemma 7.
>
> **Part (f) — smoothness of $\exp$.** We need to show $\exp : \mathfrak{g} \to G$ is smooth. This is Lemma 8, which uses Part (b) (to define the integral curves $t \mapsto (g\gamma_X(t), X)$ on all of $\mathbb{R}$) and the smoothness of the flow from [[Thm - Fundamental Theorem on Flows]].
>
> **Conclusion.** Every left-invariant vector field on $G$ is complete; a smooth curve $\gamma : \mathbb{R} \to G$ through $e$ is a one-parameter subgroup if and only if it is an integral curve of a left-invariant field, namely of $X^L$ with $X = \gamma'(0)$; the one-parameter subgroups of $G$ are exactly the curves $t \mapsto \exp(tX)$, one for each $X \in \mathfrak{g}$; the exponential map is smooth and satisfies $\exp((s + t)X) = \exp(sX)\exp(tX)$, $\exp(0) = e$, $\exp(-X) = \exp(X)^{-1}$; and the flow of $X^L$ is the one-parameter group of right translations $R_{\exp(tX)}$. Therefore the theorem holds in all six parts. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Unitary evolution in finite-dimensional quantum mechanics.** Let $H$ be an $n \times n$ Hermitian matrix (a Hamiltonian) and consider the Schrödinger equation $i\,\dot\psi = H\psi$ on $\mathbb{C}^n$. The propagator $U(t)$, defined by $\psi(t) = U(t)\psi(0)$, is a smooth curve in $U(n)$ with $U(s + t) = U(s)U(t)$ — the composition law of time evolution for an autonomous equation — and $U'(0) = -iH \in \mathfrak{u}(n)$ (the anti-Hermitian matrices, by [[Thm - Lie Algebras and Dimensions of the Classical Matrix Groups]]). The theorem applies because $U$ is a smooth homomorphism $\mathbb{R} \to U(n)$, and identifies $U(t) = \exp(-itH)$ without ever solving the equation; combined with [[Thm - The Exponential Map of a Matrix Group is the Matrix Exponential]], this is the matrix exponential $e^{-itH}$. What is non-obvious is that the *group* property of time evolution, which physicists take as a postulate, is precisely the hypothesis that pins the propagator down to a single left-invariant flow; the infinite-dimensional version of this exercise is Stone's theorem, where the analogue of completeness is the self-adjointness of $H$.

**Rigid-body kinematics with constant body angular velocity.** The attitude of a rigid body is a curve $R(t) \in SO(3)$, and the body angular velocity is the vector $\omega(t) \in \mathbb{R}^3$ with $R(t)^{-1}\dot R(t) = \hat\omega(t)$, where $\hat\omega$ is the antisymmetric matrix with $\hat\omega v = \omega \times v$ ([[Ex - R^3 with the Cross Product is the Lie Algebra so(3)]]). If $\omega$ is constant, the curve $t \mapsto R(0)^{-1}R(t)$ has constant left logarithmic derivative $\hat\omega$ and starts at the identity, so — as explained under the second source above — it is the integral curve of $\hat\omega^L$ from $e$, and the theorem gives $R(t) = R(0)\exp(t\hat\omega)$, a uniform rotation about the axis $\omega$ at angular speed $|\omega|$. The exercise is to carry out the logarithmic-derivative reduction rigorously and then to see, by contrast, that for non-constant $\omega(t)$ the solution is *not* $R(0)\exp(\int_0^t\hat\omega)$ unless the $\hat\omega(s)$ commute — the failure of $\exp$ to be a homomorphism on all of $\mathfrak{g}$, which is where the Baker–Campbell–Hausdorff correction enters.

**Constant-coefficient linear systems and the fundamental matrix.** For $A \in \operatorname{Mat}(n \times n; \mathbb{R})$, prove directly from the uniqueness theorem for linear ordinary differential equations that the fundamental matrix solution $\Phi$ of $\dot x = Ax$ satisfies $\Phi(s + t) = \Phi(s)\Phi(t)$, then use the theorem to conclude $\Phi(t) = \exp(tA)$ in $GL(n; \mathbb{R})$, and finally use [[Ex - The Exponential Map of GL(n,R) is the Matrix Exponential]] to obtain the power series. The point of the exercise is that the familiar fact "$e^{tA}$ solves $\dot x = Ax$" is a special case of the present theorem for the group $GL(n; \mathbb{R})$: the field $A^L$ at the point $g \in GL(n; \mathbb{R})$ is the matrix $gA$ (left translation is linear, so its differential is itself), and its integral curves are the solutions of the matrix equation $\dot g = gA$, whose columns are solutions of $\dot x = Ax$ only after transposition — a good check of which side the matrix multiplies on.

**Boosts and rapidity in special relativity.** In the restricted Lorentz group $SO^+(1, 3)$, the boosts along a fixed spatial axis with rapidities $\phi_1, \phi_2$ compose to the boost with rapidity $\phi_1 + \phi_2$ (the additivity of rapidity, which is the relativistic velocity-addition law in disguise). So $\phi \mapsto \Lambda(\phi)$ is a smooth homomorphism $\mathbb{R} \to SO^+(1, 3)$, and the theorem identifies it as $\exp(\phi K)$ for $K = \Lambda'(0)$ the boost generator in $\mathfrak{so}(1, 3)$; the exercise is to compute $K$ and to verify $\exp(\phi K)$ against the hyperbolic-function form of the boost. This is the mechanism behind [[Thm - The Exponential Map Generates the Restricted Lorentz Group]] in the special-relativity notes, and it is non-obvious because the additivity of rapidity is usually derived from the composition of boosts rather than recognised as the defining property of a one-parameter subgroup.

---

# Bridges

- **[[Thm - The Exponential Map is a Local Diffeomorphism at the Origin]]** — the next result of §1.4. Differentiating the identity $\exp(tX) = \gamma_X(t)$ of Part (d) at $t = 0$ gives $d_0\exp(X) = \gamma_X'(0) = X$, so the differential of $\exp$ at the origin is the identity of $\mathfrak{g}$; Part (f) is what makes that differential exist. The inverse function theorem then produces neighbourhoods $U \ni 0$ and $V \ni e$ on which $\exp$ is a diffeomorphism, and the same page derives $d_e\operatorname{inv} = -\mathrm{id}_{\mathfrak{g}}$ from $\exp(-X) = \exp(X)^{-1}$ by differentiating the commutative square $\operatorname{inv} \circ \exp = \exp \circ (-\mathrm{id})$ at $0$.

- **[[Thm - Naturality of the Exponential Map]]** — for a Lie group homomorphism $\varphi : G \to H$, the curve $t \mapsto \varphi(\exp_G(tX))$ is a smooth homomorphism $\mathbb{R} \to H$ with initial velocity $d_e\varphi(X)$ (chain rule), so by the Corollary of the present page it equals $t \mapsto \exp_H(t\,d_e\varphi(X))$; at $t = 1$ this is $\varphi \circ \exp_G = \exp_H \circ d_e\varphi$. The present theorem supplies both the uniqueness that makes the argument work and the completeness that makes both curves defined on $\mathbb{R}$.

- **[[Thm - The Exponential Map of a Matrix Group is the Matrix Exponential]]** — for a closed subgroup $G \subseteq GL(n; \mathbb{K})$, the power series $e^{tX} = \sum_{k \geq 0} (tX)^k/k!$ satisfies $e^{(s + t)X} = e^{sX}e^{tX}$ by the Cauchy product formula, so $t \mapsto e^{tX}$ is a smooth homomorphism $\mathbb{R} \to GL(n; \mathbb{K})$ with initial velocity $X$; the Corollary of the present page then forces $e^{tX} = \exp(tX)$. That page also settles the point Bär leaves aside, that $e^{tX}$ lies in the subgroup $G$ and not merely in $GL(n; \mathbb{K})$.

- **[[Def - Fundamental Vector Field of a Group Action]]** and **[[Thm - The Fundamental Vector Field Map is a Lie Algebra Homomorphism for Right Actions]]** — for a smooth right action of $G$ on $P$, the fundamental vector field $\xi_P(p) = \tfrac{d}{dt}\big|_{t=0}\, p \cdot \exp(t\xi)$ is the image of $\xi^L$ under the orbit map $g \mapsto p \cdot g$; its flow is $p \mapsto p \cdot \exp(t\xi)$, by the same two-curves argument as Lemma 7 with the action in place of right translation. Part (e) of the present theorem is the special case $P = G$ acting on itself by right multiplication, where $\xi_G = \xi^L$.

- **[[Thm - Ad is a Smooth Representation and its Differential is ad]]** — the formula $\operatorname{Ad}_{\exp(tX)} = e^{t\,\operatorname{ad}_X}$ used on that page and in chapter IV is an application of the Corollary to the one-parameter subgroup $t \mapsto \operatorname{Ad}_{\exp(tX)}$ of $GL(\mathfrak{g})$, whose initial velocity is $\operatorname{ad}_X$ by definition of the differential of $\operatorname{Ad}$.

- **[[Thm - The Exponential Map of a Compact Connected Lie Group is Surjective]]** — for compact connected $G$ the one-parameter subgroups $t \mapsto \exp(tX)$ are the geodesics through $e$ of a bi-invariant metric, and the Hopf–Rinow-type argument that every point is joined to $e$ by a geodesic gives surjectivity of $\exp$; the identification of geodesics with one-parameter subgroups rests on Part (a) of the present theorem.

- **[[Ex - Maximal Integral Curves of Left-Invariant Fields are Defined on All of R]]** — Bär's Exercise 1.4.1, drilled as a stand-alone exercise; its solution is Lemma 5 of this page, and the exercise exists so that the extension-by-translation argument can be practised without the surrounding theorem.

- **[[Def - Complete Vector Field]]** — Part (b) provides the most important class of examples of complete vector fields beyond compactly supported ones: on a Lie group every left-invariant (and, by the symmetric argument with right translations, every right-invariant) vector field is complete, even though $G$ may be non-compact and the field may be unbounded in any given chart.

---

# Unlocked by This

> [!tip] The exponential map as a chart near the identity *(from Lie theory)*
> Parts (d) and (f) make $\exp$ a smooth map with $d_0\exp = \mathrm{id}$, so $\exp$ restricts to a diffeomorphism from a neighbourhood of $0 \in \mathfrak{g}$ onto a neighbourhood of $e \in G$ — the exponential chart, in which every element near $e$ has a unique logarithm. This is [[Thm - The Exponential Map is a Local Diffeomorphism at the Origin]], and it is the first step in proving that a connected Lie group is generated by $\exp(\mathfrak{g})$.

> [!tip] Vertical vector fields on a principal bundle *(from gauge theory)*
> Part (e), read for a right action of $G$ on a principal bundle $P$, says that the curves $t \mapsto p \cdot \exp(t\xi)$ are the flow lines of the fundamental vector field $\xi_P$ and lie in the fibres of $P$. The vertical subspace at $p$ is $\{\xi_P(p) : \xi \in \mathfrak{g}\}$, and a connection form is a $\mathfrak{g}$-valued one-form with $\omega(\xi_P) = \xi$; both constructions are on [[Def - Fundamental Vector Field of a Group Action]] and in chapter IV.

> [!tip] Matrix exponentials and linear differential equations *(from ordinary differential equations)*
> For $G = GL(n; \mathbb{R})$, Part (a) says that the solutions of $\dot g = gA$ with $g(0) = 1_n$ are exactly the one-parameter subgroups, and [[Thm - The Exponential Map of a Matrix Group is the Matrix Exponential]] then identifies them with the convergent power series $e^{tA}$; the theory of constant-coefficient linear systems is the case $G = GL(n; \mathbb{R})$ of the present page.
