---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Adjoint Representation"
  - "Def - Representation of a Lie Group"
  - "Def - Exponential Map of a Lie Group"
  - "Thm - One-Parameter Subgroups are the Integral Curves of Left-Invariant Vector Fields"
  - "Thm - Fundamental Theorem on Flows"
  - "Def - The Lie Bracket of Vector Fields"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $G$ is a [[Def - Lie Group|Lie group]] with neutral element $e$, and $\mathfrak{g} = T_e G$ is its [[Def - The Lie Algebra of a Lie Group|Lie algebra]], the tangent space at $e$ identified with the space of [[Def - Left-Invariant Vector Field|left-invariant vector fields]] and carrying the bracket $[\,\cdot\,,\cdot\,]$ of vector fields; on the classical matrix groups this bracket is the commutator $[X,Y] = XY - YX$. We write $L_g\colon G \to G$, $h \mapsto gh$ for left translation, $R_g\colon G \to G$, $h \mapsto hg$ for right translation, and
$$\alpha_g := L_g \circ R_{g^{-1}}\colon G \to G, \qquad \alpha_g(h) = ghg^{-1},$$
for **conjugation** by $g$ (the notation of [[Def - Left and Right Translations and Conjugation on a Lie Group|the translations page]]). Since $\alpha_g(e) = geg^{-1} = e$, the differential $d_e\alpha_g$ maps $T_eG$ to $T_eG$, that is, $\mathfrak{g}$ to $\mathfrak{g}$; the **[[Def - Adjoint Representation|adjoint representation]]** is
$$\operatorname{Ad}\colon G \to GL(\mathfrak{g}), \qquad \operatorname{Ad}_g := d_e\alpha_g\colon \mathfrak{g} \to \mathfrak{g}.$$
Here $GL(\mathfrak{g}) = \operatorname{Aut}(\mathfrak{g})$ is the group of linear automorphisms of the finite-dimensional real vector space $\mathfrak{g}$; it is an open subset of the vector space $\operatorname{End}(\mathfrak{g})$ of all linear endomorphisms, so its Lie algebra is $\mathfrak{gl}(\mathfrak{g}) = \operatorname{End}(\mathfrak{g})$ and its tangent space at the identity is $T_{\operatorname{id}}GL(\mathfrak{g}) = \operatorname{End}(\mathfrak{g})$. The **adjoint representation of the Lie algebra** is
$$\operatorname{ad}\colon \mathfrak{g} \to \operatorname{End}(\mathfrak{g}), \qquad \operatorname{ad}_X Y = \operatorname{ad}(X)(Y) := [X, Y].$$
For a [[Def - Lie Group Homomorphism|Lie group homomorphism]] $\varphi\colon G \to H$ we write $\varphi_* := d_e\varphi\colon \mathfrak{g} \to \mathfrak{h}$ for its differential at the identity; thus the claim "the differential of $\operatorname{Ad}$ is $\operatorname{ad}$" is the equation $\operatorname{Ad}_* = \operatorname{ad}$, where $\operatorname{Ad}_* = d_e\operatorname{Ad}\colon \mathfrak{g} \to T_{\operatorname{id}}GL(\mathfrak{g}) = \operatorname{End}(\mathfrak{g})$. The [[Def - Exponential Map of a Lie Group|exponential map]] $\exp\colon \mathfrak{g} \to G$ sends $X$ to $\gamma_X(1)$, where $\gamma_X$ is the one-parameter subgroup with $\gamma_X(0) = e$, $\dot\gamma_X(0) = X$; it satisfies $\gamma_X(t) = \exp(tX)$. For a matrix group $G \subset GL(n; \mathbb{K})$ ($\mathbb{K} = \mathbb{R}$ or $\mathbb{C}$), $\mathfrak{g}$ is identified with a subspace of $\operatorname{Mat}(n \times n; \mathbb{K})$ via $T_{1}G \subset T_1 GL(n;\mathbb{K}) = \operatorname{Mat}(n \times n; \mathbb{K})$ (see [[Ex - The Lie Algebra of GL(n,R) is the Space of n by n Matrices]] and [[Thm - Lie Algebras and Dimensions of the Classical Matrix Groups]]), and $1_n$ denotes the identity matrix. The full symbol registry is on the parent page [[Gauge Theory I — Lie Groups, Representations, and Group Actions]].

> [!warning] Convention: Bär's Pauli labelling
> In the worked $SU(2)$ computation below we use the basis of $\mathfrak{su}(2)$ that Bär writes as $-i\sigma_1, -i\sigma_2, -i\sigma_3$, namely
> $$-i\sigma_1 = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}, \qquad -i\sigma_2 = \begin{pmatrix} 0 & i \\ i & 0 \end{pmatrix}, \qquad -i\sigma_3 = \begin{pmatrix} i & 0 \\ 0 & -i \end{pmatrix}.$$
> With the standard physics Pauli matrices $\sigma_1 = \left(\begin{smallmatrix} 0 & 1 \\ 1 & 0 \end{smallmatrix}\right)$, $\sigma_2 = \left(\begin{smallmatrix} 0 & -i \\ i & 0 \end{smallmatrix}\right)$, $\sigma_3 = \left(\begin{smallmatrix} 1 & 0 \\ 0 & -1 \end{smallmatrix}\right)$ one would instead have $-i\sigma_1 = \left(\begin{smallmatrix} 0 & -i \\ -i & 0 \end{smallmatrix}\right)$ and $-i\sigma_2 = \left(\begin{smallmatrix} 0 & -1 \\ 1 & 0 \end{smallmatrix}\right)$, so Bär's labels for $\sigma_1$ and $\sigma_2$ are interchanged and sign-adjusted relative to the standard ones. This is harmless: the three matrices Bär lists are a genuine basis of $\mathfrak{su}(2)$, and every statement below refers to that explicit basis. The recipe to convert a formula written in the standard Pauli basis is to apply the permutation $-i\sigma_1^{\text{std}} \mapsto$ (Bär's $-i\sigma_2$), $-i\sigma_2^{\text{std}} \mapsto -($Bär's $-i\sigma_1)$, $-i\sigma_3^{\text{std}} \mapsto$ (Bär's $-i\sigma_3$).

---

# Statement

> **Theorem (the adjoint representation and its differential).** Let $G$ be a Lie group with Lie algebra $\mathfrak{g} = T_eG$, and define $\operatorname{Ad}_g = d_e\alpha_g$ for $\alpha_g(h) = ghg^{-1}$. Then:
>
> **(i)** The map $\operatorname{Ad}\colon G \to GL(\mathfrak{g})$, $g \mapsto \operatorname{Ad}_g$, is a [[Def - Representation of a Lie Group|representation]] of $G$ on $\mathfrak{g}$: each $\operatorname{Ad}_g$ is a linear automorphism of $\mathfrak{g}$, the assignment satisfies $\operatorname{Ad}_{g_1 g_2} = \operatorname{Ad}_{g_1} \circ \operatorname{Ad}_{g_2}$, $\operatorname{Ad}_e = \operatorname{id}_{\mathfrak{g}}$, $(\operatorname{Ad}_g)^{-1} = \operatorname{Ad}_{g^{-1}}$, and $\operatorname{Ad}$ is a smooth map.
>
> **(ii)** If $G \subset GL(n; \mathbb{K})$ is a matrix group and $X \in \mathfrak{g} \subset \operatorname{Mat}(n \times n; \mathbb{K})$, then $\operatorname{Ad}_g X = g\,X\,g^{-1}$ (ordinary matrix conjugation).
>
> **(iii)** The differential of $\operatorname{Ad}$ at $e$ is the adjoint representation of the Lie algebra: $\operatorname{Ad}_* = \operatorname{ad}$, that is,
> $$\frac{d}{dt}\bigg|_{t=0} \operatorname{Ad}_{\exp(tX)} Y = [X, Y] \qquad \text{for all } X, Y \in \mathfrak{g},$$
> and this holds for **every** Lie group, not only for matrix groups.
>
> **(iv)** If $G$ is abelian, then $\operatorname{Ad}_g = \operatorname{id}_{\mathfrak{g}}$ for every $g \in G$; the adjoint representation is trivial.

---

# Motivation

A Lie group $G$ acts on itself by conjugation, $\alpha_g(h) = ghg^{-1}$, and this action fixes the neutral element. Differentiating it at $e$ turns each conjugation into a linear map on the tangent space $\mathfrak{g} = T_eG$, and the resulting family $g \mapsto \operatorname{Ad}_g$ is how a Lie group acts *linearly* on its own Lie algebra. This is the single most important representation attached to $G$ intrinsically: it needs no auxiliary vector space, no choice of matrices, only the group and its infinitesimal structure. Every place in gauge theory where "the group acts on the Lie algebra" appears — the transformation law of a connection form $A_{s'} = \operatorname{Ad}_{g^{-1}} A_s + g^*\theta$, the equivariance $R_g^*\omega = \operatorname{Ad}_{g^{-1}}\omega$ of a principal connection, the curvature's $\operatorname{Ad}$-equivariance, the very definition of the adjoint bundle $\operatorname{ad} P = P \times_{\operatorname{Ad}} \mathfrak{g}$ in which the Yang–Mills field lives — is the adjoint representation at work. Understanding $\operatorname{Ad}$ once, here, settles all of them.

The theorem answers two questions about this action. The first is whether $\operatorname{Ad}$ is a genuine representation at all: is $g \mapsto \operatorname{Ad}_g$ a *smooth* homomorphism into $GL(\mathfrak{g})$? The homomorphism property is a one-line consequence of the functoriality of the differential together with $\alpha_{g_1 g_2} = \alpha_{g_1}\circ\alpha_{g_2}$; the smoothness is the part Bär's text asserts without argument, and part (i) supplies it, from the joint smoothness of the conjugation map $(g,h) \mapsto ghg^{-1}$.

The second question is what $\operatorname{Ad}$ looks like infinitesimally. A representation of $G$ has a differential $\operatorname{Ad}_* = d_e\operatorname{Ad}$, itself a representation of the Lie algebra $\mathfrak{g}$; which one is it? The answer, part (iii), is the cleanest possible: it is the bracket. The map $X \mapsto [X, \cdot]$, which was defined purely algebraically as $\operatorname{ad}$, is exactly the infinitesimal shadow of conjugation. This identity is the hinge on which most of the elementary structure theory of Lie groups turns — it is what makes $\operatorname{ad}$ a representation (because $\operatorname{Ad}$ is), it is what forces the differential of any homomorphism to preserve brackets, and it is the reason the Lie bracket, an object built from second derivatives of the multiplication, can be computed from the first-order object $\operatorname{Ad}$. Bär proves it only for matrix groups, where it collapses to the Leibniz computation $\frac{d}{dt}\big|_0 e^{tX} Y e^{-tX} = XY - YX$; the general case, valid on any Lie group with no matrices in sight, is the substance of this page.

---

# Sources and Targets

**Sources (Input Broadening).** The theorem's literal input is a Lie group; the useful question is which structures secretly present a copy of $\operatorname{Ad}$, so that a computation about them becomes a computation about conjugation.

The first disguised source is **any linear action of $G$ on a vector space that happens to be $\mathfrak{g}$ built by transporting the group's own multiplication**. Whenever a construction produces a $G$-action on the Lie algebra by "move by $g$, do the infinitesimal thing, move back by $g^{-1}$", it is $\operatorname{Ad}$ in disguise, because that is literally $d_e(L_g R_{g^{-1}})$. The non-obvious bridge is that one need not recognise conjugation explicitly: any action of the form $g \cdot X = d_e(\text{inner automorphism})(X)$ is $\operatorname{Ad}_g X$. *Example problem:* on a principal bundle the structure group acts on the vertical tangent spaces; identifying each vertical space with $\mathfrak{g}$ through the fundamental vector fields, the induced action of $g$ is $\operatorname{Ad}_{g^{-1}}$ — recognising this is what makes the transformation law of a connection form a statement about $\operatorname{Ad}$ rather than a fresh computation.

The second disguised source is **a Lie group homomorphism whose differential one wants to understand**. By part (iii) and its consequences, $\operatorname{Ad}$ mediates between a homomorphism $\varphi\colon G \to H$ and its differential: the identity $\varphi \circ \alpha_g = \alpha_{\varphi(g)} \circ \varphi$ differentiates to $\varphi_* \circ \operatorname{Ad}_g = \operatorname{Ad}_{\varphi(g)} \circ \varphi_*$, and differentiating once more in $g$ shows $\varphi_*[X,Y] = [\varphi_* X, \varphi_* Y]$. The bridge is that "preserves brackets" is not an independent fact but a corollary of "intertwines the two adjoint representations". *Example problem:* proving that the differential of every Lie group homomorphism is a Lie algebra homomorphism (the companion sibling theorem) reduces, through this route, to part (iii) applied on $G$ and on $H$.

The third disguised source is **a bi-invariant object on $G$ — a metric, a volume form, an integral**. An inner product $\langle\cdot,\cdot\rangle$ on $\mathfrak{g}$ is $\operatorname{Ad}$-invariant precisely when the left-invariant metric it induces is also right-invariant, hence bi-invariant; and a volume form is bi-invariant precisely when $|\det \operatorname{Ad}_g| = 1$. The bridge is that invariance under the whole group, a global condition, is tested by invariance under $\operatorname{Ad}$, a linear-algebra condition on $\mathfrak{g}$. *Example problem:* showing a compact Lie group carries a bi-invariant metric — average any inner product on $\mathfrak{g}$ over the compact image $\operatorname{Ad}(G) \subset GL(\mathfrak{g})$ — is exactly the input to the surjectivity of $\exp$ on compact connected groups, proved later in this chapter.

**Targets (Output Amplification).** Combined with a little more, the theorem computes concrete objects.

Combine part (ii) with **the explicit basis of $\mathfrak{su}(2)$** to get the double cover $SU(2) \to SO(3)$. Take $g = \operatorname{diag}(e^{i\varphi}, e^{-i\varphi}) \in SU(2)$ and the basis $-i\sigma_1, -i\sigma_2, -i\sigma_3$ of $\mathfrak{su}(2)$ (Bär's labelling, above). Part (ii) gives $\operatorname{Ad}_g(-i\sigma_a) = g(-i\sigma_a)g^{-1}$, and a direct multiplication (carried out in full in Lemma 3's proof, and drilled in [[Ex - The Adjoint Representation of SU(2) in the Pauli Basis]]) yields
$$\operatorname{Ad}_g = \begin{pmatrix} \cos 2\varphi & -\sin 2\varphi & 0 \\ \sin 2\varphi & \cos 2\varphi & 0 \\ 0 & 0 & 1 \end{pmatrix}$$
in that basis — a rotation by the *doubled* angle $2\varphi$ in the $(-i\sigma_1, -i\sigma_2)$-plane. This is the extra ingredient (an explicit basis) turning "conjugation" into "rotation", and the doubling of the angle is the infinitesimal origin of the fact that $SU(2)$ is a two-to-one cover of $SO(3)$. It also realises the source item (Bär, Example 1.3.8).

Combine that same computation with **$g = -1_2$** to see that $\operatorname{Ad}$ is not faithful. Since $-1_2$ is central, $\operatorname{Ad}_{-1_2} X = (-1_2)X(-1_2)^{-1} = X$ for every $X \in \mathfrak{su}(2)$, so $\operatorname{Ad}_{-1_2} = \operatorname{id}$ although $-1_2 \neq e$. The payoff is that $\ker \operatorname{Ad}_{SU(2)} \supseteq \{\pm 1_2\}$, so $\operatorname{Ad}\colon SU(2) \to GL(\mathfrak{su}(2))$ factors through $SU(2)/\{\pm 1\} \cong SO(3)$; the kernel is exactly the centre. This realises Bär's Remark 1.3.9 (source item E1.3.3), and it is the prototype for "the adjoint representation sees the group only up to its centre".

Combine part (iii) with **the structure equations of a principal connection**. The curvature two-form $\Omega = d\omega + \tfrac12[\omega \wedge \omega]$ and the Bianchi identity $d^\omega\Omega = 0$ are consequences of $\operatorname{Ad}$-equivariance of $\omega$ differentiated infinitesimally; the bracket that appears is $\operatorname{ad}$, and the identity $\operatorname{Ad}_* = \operatorname{ad}$ is what licenses replacing "differentiate the $\operatorname{Ad}$-action" by "bracket". The payoff is that the entire local curvature calculus of chapters IV and VII rests on this one differentiation.

---

# Why Is It True

Conjugation $\alpha_g$ is the composite $L_g \circ R_{g^{-1}}$ of two translations, and translations are the moves a Lie group can make on itself for free. Differentiating $\alpha_g$ at the fixed point $e$ produces a linear map on $\mathfrak{g}$; because the differential of a composite is the composite of the differentials and $\alpha_{g_1 g_2} = \alpha_{g_1}\circ\alpha_{g_2}$ (conjugating twice is conjugating by the product), the family $\operatorname{Ad}_g$ multiplies the way $g$ multiplies. That is the homomorphism property, and it is nothing more than the chain rule applied to a group law. Smoothness is equally structural: conjugation depends smoothly on $g$ and on $h$ jointly (the group operations are smooth), and differentiating a jointly smooth map in one variable leaves smooth dependence on the other. So part (i) is the statement that *the differential of an inner automorphism is a smooth linear representation*, which is the chain rule plus the smoothness of multiplication.

The heart of the theorem is part (iii), and the mechanism is the following.

> **The bracket $[X,Y]$ is, by its very definition, the infinitesimal rate at which the flow of $X$ fails to preserve $Y$; and the flow of a left-invariant field $X$ is right translation by $\exp(tX)$, whose effect on the left-invariant field $Y$ — transported back — is exactly $\operatorname{Ad}_{\exp(tX)} Y$. So differentiating $\operatorname{Ad}_{\exp(tX)} Y$ and computing $[X,Y]$ are the same operation.**

Unpacked: the flow $\theta_t$ of the left-invariant vector field $X$ is $\theta_t = R_{\exp(tX)}$, because the integral curve of $X$ through $g$ is $t \mapsto g\exp(tX)$. To measure how $Y$ changes along this flow, one drags $Y_{\theta_t(e)}$ back to $T_eG$ by the differential of $\theta_{-t}$ and differentiates in $t$ — this is precisely the Lie-derivative construction, and the Lie derivative of $Y$ along $X$ *is* the bracket $[X,Y]$. But dragging $Y$ back along $\theta_{-t} = R_{\exp(-tX)}$ and using that $Y$ is left-invariant produces $d(R_{\exp(-tX)}) \circ d(L_{\exp(tX)}) = d(\alpha_{\exp(tX)}) = \operatorname{Ad}_{\exp(tX)}$. The two descriptions of the same drag — "Lie derivative, which is the bracket" and "conjugation, which is $\operatorname{Ad}$" — coincide, and their common derivative at $t = 0$ is $[X,Y]$ on one side and $\operatorname{Ad}_*(X)Y$ on the other.

The smallest concrete case makes this weightless. On a matrix group, $\exp(tX) = e^{tX}$ and $\operatorname{Ad}_{e^{tX}} Y = e^{tX} Y e^{-tX}$; differentiating the product at $t = 0$ by the Leibniz rule,
$$\frac{d}{dt}\bigg|_0 e^{tX} Y e^{-tX} = X\,Y\,1_n + 1_n\,Y\,(-X) = XY - YX = [X,Y].$$
The one term where the flow "pushes $Y$ forward" ($XY$) and the one term where it "pulls the frame back" ($-YX$) are the two halves of the conjugation, and their difference is the commutator. The general proof is the coordinate-free rendering of exactly this: a "push forward by $X$" term and a "pull back the frame by $X$" term, whose difference is $X(Yf) - Y(Xf)$.

Part (iv) is the degenerate case: in an abelian group $ghg^{-1} = h$, so conjugation is the identity map and its differential is the identity of $\mathfrak{g}$; there is nothing for $\operatorname{Ad}$ to do. Consistently, part (iii) then gives $[X,Y] = \operatorname{Ad}_*(X)Y = 0$, recovering that an abelian Lie group has abelian Lie algebra.

---

# What Makes This Hard

The single genuine difficulty is proving part (iii) **for a general Lie group**, where "$Y$" is not a matrix and "$\operatorname{Ad}_{\exp tX} Y$" cannot be written as a product $e^{tX} Y e^{-tX}$. The temptation is to imitate the matrix computation, but there is no ambient associative algebra in which $Y$ lives, so the Leibniz rule has nothing to act on. The correct move is to interpret $\operatorname{Ad}_{\exp tX} Y$ as the flow-pullback of the left-invariant field $Y$ along the flow of $X$ — which requires knowing that this flow is right translation by $\exp(tX)$ — and then to identify the resulting derivative with the bracket. The subtle step inside that identification is a single interchange of the order of two differentiations (in the flow parameter $t$ and in a curve parameter $s$), legitimate only because the map $(s,t) \mapsto f(\exp(sY)\exp(tX))$ is smooth so that Schwarz's theorem applies; a proof that differentiates in one order without noticing it has silently assumed the other is a proof with a gap. The common error, beyond skipping smoothness, is a sign error: the flow drags back by $\theta_{-t} = R_{\exp(-tX)}$, and writing $R_{\exp(tX)}$ instead flips the sign and produces $-[X,Y]$.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Part (i) is the chain rule for $\alpha_{g_1 g_2} = \alpha_{g_1}\circ\alpha_{g_2}$ plus joint smoothness of conjugation. Part (ii) is the observation that on matrices $\alpha_g$ is the *linear* map $M \mapsto gMg^{-1}$, so its differential is itself. Part (iii) writes $\operatorname{Ad}_{\exp tX} Y$ as the pullback of $Y$ along the flow of $X$ (which is right translation by $\exp tX$) and differentiates, matching the result to $X(Yf) - Y(Xf) = [X,Y]f$ by a mixed-partial computation. Part (iv) is immediate.

**Subgoal decomposition:**

1. **Homomorphism and automorphism (part i, algebraic half).** Show $\operatorname{Ad}_{g_1 g_2} = \operatorname{Ad}_{g_1}\operatorname{Ad}_{g_2}$, $\operatorname{Ad}_e = \operatorname{id}$, each $\operatorname{Ad}_g \in GL(\mathfrak{g})$.
   - *Hint:* Differentiate $\alpha_{g_1 g_2} = \alpha_{g_1}\circ\alpha_{g_2}$ at $e$ with the chain rule; invertibility comes from $\operatorname{Ad}_g\operatorname{Ad}_{g^{-1}} = \operatorname{Ad}_e = \operatorname{id}$.
   - *Why needed:* Without it $\operatorname{Ad}$ is not a homomorphism and "representation" is meaningless.

2. **Smoothness (part i, analytic half).** Show $g \mapsto \operatorname{Ad}_g \in \operatorname{End}(\mathfrak{g})$ is smooth.
   - *Hint:* $\operatorname{Ad}_g X = d_h(h \mapsto \alpha_g(h))_e(X)$; the matrix entries of $\operatorname{Ad}_g$ are partial derivatives of the jointly smooth map $(g,h) \mapsto ghg^{-1}$, evaluated at $h = e$, hence smooth in $g$.
   - *Why needed:* A representation is a *smooth* homomorphism; this is the step Bär omits.

3. **Matrix case (part ii).** Show $\operatorname{Ad}_g X = gXg^{-1}$ for a matrix group.
   - *Hint:* $\alpha_g$ restricted to matrices is $M \mapsto gMg^{-1}$, linear; differentiate a curve $c(s)$ with $\dot c(0) = X$.
   - *Why needed:* It is the computable form of $\operatorname{Ad}$ and the smallest case of part (iii).

4. **Conjugation is flow-pullback (part iii, geometric identity).** Show $\operatorname{Ad}_{\exp tX} Y_e = d(\theta_{-t})_{\theta_t(e)}\big(Y_{\theta_t(e)}\big)$, where $\theta_t = R_{\exp tX}$ is the flow of $X$.
   - *Hint:* Left-invariance gives $Y_{\exp tX} = d(L_{\exp tX})_e Y_e$; combine with $R_{\exp(-tX)}$ and use $\alpha_g = R_{g^{-1}}\circ L_g$.
   - *Why needed:* It converts a statement about $\operatorname{Ad}$ into a statement about the flow of $X$, where the bracket lives.

5. **The derivative is the bracket (part iii, computation).** Show $\frac{d}{dt}\big|_0 d(\theta_{-t})_{\theta_t(e)}\big(Y_{\theta_t(e)}\big) = [X,Y]_e$.
   - *Hint:* Act on a test function $f$; the result is $H(t,-t)$ with $H(t,u) = Y_{\theta_t(e)}(f\circ\theta_u)$; the chain rule gives $\partial_t H - \partial_u H = X(Yf) - Y(Xf)$, using Schwarz's theorem for one term.
   - *Why needed:* It is the identity $\operatorname{Ad}_* = \operatorname{ad}$.

6. **Abelian case (part iv).** Show $G$ abelian $\Rightarrow \operatorname{Ad}_g = \operatorname{id}$.
   - *Hint:* $\alpha_g = \operatorname{id}_G$.
   - *Why needed:* It is the base sanity check and gives $[\mathfrak{g},\mathfrak{g}] = 0$ for abelian $G$.

---

# Lemma Decomposition

> [!note]- Lemma 1: Conjugation is functorial, so $\operatorname{Ad}$ is a homomorphism into $GL(\mathfrak{g})$
> **Statement:** For all $g_1, g_2 \in G$ one has $\alpha_{g_1 g_2} = \alpha_{g_1}\circ\alpha_{g_2}$ and $\alpha_e = \operatorname{id}_G$. Consequently each $\operatorname{Ad}_g = d_e\alpha_g$ is a linear automorphism of $\mathfrak{g}$ with $\operatorname{Ad}_{g_1 g_2} = \operatorname{Ad}_{g_1}\circ\operatorname{Ad}_{g_2}$, $\operatorname{Ad}_e = \operatorname{id}_{\mathfrak{g}}$, and $(\operatorname{Ad}_g)^{-1} = \operatorname{Ad}_{g^{-1}}$.
>
> **Hint:** Expand $ghg^{-1}$ for a product $g = g_1 g_2$ and differentiate with the chain rule.
>
> **Why needed:** It is the algebraic core of part (i): it makes $\operatorname{Ad}$ a group homomorphism into $GL(\mathfrak{g})$ and each $\operatorname{Ad}_g$ invertible.
>
> > [!note]- Full proof
> > **Conjugation is a homomorphism of the conjugating variable.** For every $h \in G$,
> > $$\alpha_{g_1 g_2}(h) = (g_1 g_2)\,h\,(g_1 g_2)^{-1} = g_1\big(g_2\,h\,g_2^{-1}\big)g_1^{-1} = \alpha_{g_1}\big(\alpha_{g_2}(h)\big) \qquad \text{(associativity and } (g_1 g_2)^{-1} = g_2^{-1} g_1^{-1}\text{),}$$
> > so $\alpha_{g_1 g_2} = \alpha_{g_1}\circ\alpha_{g_2}$ as maps $G \to G$. Taking $g_1 = g_2 = e$ (or directly $\alpha_e(h) = ehe^{-1} = h$) gives $\alpha_e = \operatorname{id}_G$.
> >
> > **Each $\operatorname{Ad}_g$ is linear.** By definition $\operatorname{Ad}_g = d_e\alpha_g$ is the differential at $e$ of the smooth map $\alpha_g$, and the differential of a smooth map at a point is a linear map between tangent spaces; since $\alpha_g(e) = e$, it maps $T_eG = \mathfrak{g}$ to $T_eG = \mathfrak{g}$.
> >
> > **The assignment is multiplicative.** Both $\alpha_{g_1 g_2}$ and $\alpha_{g_2}$ fix $e$, so the chain rule for differentials applies at $e$:
> > $$\operatorname{Ad}_{g_1 g_2} = d_e\alpha_{g_1 g_2} = d_e(\alpha_{g_1}\circ\alpha_{g_2}) = d_{\alpha_{g_2}(e)}\alpha_{g_1}\circ d_e\alpha_{g_2} = d_e\alpha_{g_1}\circ d_e\alpha_{g_2} = \operatorname{Ad}_{g_1}\circ\operatorname{Ad}_{g_2} \qquad \text{(chain rule, } \alpha_{g_2}(e) = e\text{).}$$
> > Also $\operatorname{Ad}_e = d_e\alpha_e = d_e\operatorname{id}_G = \operatorname{id}_{T_eG} = \operatorname{id}_{\mathfrak{g}}$.
> >
> > **Invertibility.** Applying multiplicativity to $g_2 = g^{-1}$,
> > $$\operatorname{Ad}_g\circ\operatorname{Ad}_{g^{-1}} = \operatorname{Ad}_{g g^{-1}} = \operatorname{Ad}_e = \operatorname{id}_{\mathfrak{g}}, \qquad \operatorname{Ad}_{g^{-1}}\circ\operatorname{Ad}_g = \operatorname{Ad}_{g^{-1} g} = \operatorname{Ad}_e = \operatorname{id}_{\mathfrak{g}},$$
> > so $\operatorname{Ad}_g$ is a bijective linear map, that is $\operatorname{Ad}_g \in GL(\mathfrak{g})$, with inverse $\operatorname{Ad}_{g^{-1}}$. Therefore $\operatorname{Ad}\colon G \to GL(\mathfrak{g})$ is a group homomorphism.

> [!note]- Lemma 2: $\operatorname{Ad}$ is smooth
> **Statement:** The map $\operatorname{Ad}\colon G \to GL(\mathfrak{g}) \subset \operatorname{End}(\mathfrak{g})$, $g \mapsto \operatorname{Ad}_g$, is smooth.
>
> **Hint:** Fix a basis of $\mathfrak{g}$; the matrix entries of $\operatorname{Ad}_g$ are first partial derivatives, in the second variable at $h = e$, of the jointly smooth conjugation map $A(g,h) = ghg^{-1}$.
>
> **Why needed:** A representation is a *smooth* homomorphism; this is the smoothness clause of part (i), which the source only asserts.
>
> > [!note]- Full proof
> > **The conjugation map is jointly smooth.** Multiplication $\mu\colon G \times G \to G$ and inversion $\iota\colon G \to G$ are smooth, by the definition of a Lie group. Hence
> > $$A\colon G \times G \to G, \qquad A(g,h) = \mu\big(\mu(g,h), \iota(g)\big) = ghg^{-1}$$
> > is smooth as a composite of smooth maps, and $A(g, e) = e$ for every $g$.
> >
> > **The partial differential in $h$ is $\operatorname{Ad}_g$.** For fixed $g$ the map $h \mapsto A(g,h) = \alpha_g(h)$ is $\alpha_g$, and its differential at $e$ is $\operatorname{Ad}_g$ by definition. Write $D_2 A(g,\cdot)_e := d_e\big(A(g,\cdot)\big) = \operatorname{Ad}_g$.
> >
> > **Smooth dependence on $g$ in coordinates.** Choose a chart $(V, \psi)$ of $G$ around $e$ with $\psi(e) = 0$, giving coordinates $(h^1, \dots, h^m)$ near $e$, and the induced basis $\partial_1, \dots, \partial_m$ of $T_eG = \mathfrak{g}$ ($m = \dim G$). In these coordinates the smooth function $A$ has components $A^i(g, h)$, smooth in $(g,h)$, and the matrix of $\operatorname{Ad}_g = D_2 A(g,\cdot)_e$ in the basis $\{\partial_j\}$ has entries
> > $$\big(\operatorname{Ad}_g\big)^i{}_j = \frac{\partial A^i}{\partial h^j}(g, h)\bigg|_{h = e} \qquad \text{(definition of the differential in coordinates).}$$
> > Each partial derivative $\partial A^i/\partial h^j$ is smooth on $G \times V$ because $A$ is smooth, and restricting a smooth function to the slice $\{h = e\}$ leaves a smooth function of $g$. Hence every entry $(\operatorname{Ad}_g)^i{}_j$ is a smooth real-valued function of $g$, so $g \mapsto \operatorname{Ad}_g$ is a smooth map into $\operatorname{End}(\mathfrak{g}) \cong \mathbb{R}^{m \times m}$.
> >
> > **Landing in the open set $GL(\mathfrak{g})$.** By Lemma 1 each $\operatorname{Ad}_g$ is invertible, so the image lies in $GL(\mathfrak{g})$, which is an open subset of $\operatorname{End}(\mathfrak{g})$ (the complement of the closed zero set of $\det$). A smooth map into $\operatorname{End}(\mathfrak{g})$ whose image lies in the open subset $GL(\mathfrak{g})$ is smooth as a map into $GL(\mathfrak{g})$. Therefore $\operatorname{Ad}\colon G \to GL(\mathfrak{g})$ is smooth, and together with Lemma 1 this shows $\operatorname{Ad}$ is a Lie group homomorphism into $GL(\mathfrak{g}) = \operatorname{Aut}(\mathfrak{g})$, i.e. a representation of $G$ on $\mathfrak{g}$.

> [!note]- Lemma 3: On a matrix group, $\operatorname{Ad}_g X = gXg^{-1}$
> **Statement:** Let $G \subset GL(n; \mathbb{K})$ be a matrix group with Lie algebra $\mathfrak{g} \subset \operatorname{Mat}(n \times n; \mathbb{K})$, and $g \in G$, $X \in \mathfrak{g}$. Then $\operatorname{Ad}_g X = g X g^{-1}$.
>
> **Hint:** On matrices, $\alpha_g$ is the restriction of the *linear* map $M \mapsto gMg^{-1}$ on $\operatorname{Mat}(n\times n;\mathbb{K})$; the differential of a linear map is itself.
>
> **Why needed:** It is part (ii), the computable form of $\operatorname{Ad}$; it also supplies the concrete instance used in the $SU(2)$ target computation.
>
> > [!note]- Full proof
> > **Realise $X$ as a matrix-valued velocity.** By the identification $\mathfrak{g} = T_1 G \subset T_1 GL(n; \mathbb{K}) = \operatorname{Mat}(n \times n; \mathbb{K})$ (see [[Ex - The Lie Algebra of GL(n,R) is the Space of n by n Matrices]] and [[Thm - Lie Algebras and Dimensions of the Classical Matrix Groups]]), there is a smooth curve $c\colon (-\varepsilon, \varepsilon) \to G$ with $c(0) = 1_n$ and $\dot c(0) = X$, where the derivative $\dot c(0)$ is taken entrywise in the ambient $\operatorname{Mat}(n \times n; \mathbb{K}) \cong \mathbb{K}^{n^2}$.
> >
> > **Differentiate conjugation.** By the definition of $\operatorname{Ad}_g$ as $d_e\alpha_g$ applied to the velocity $X = \dot c(0)$,
> > $$\operatorname{Ad}_g X = d_e\alpha_g(\dot c(0)) = \frac{d}{ds}\bigg|_{s=0} \alpha_g(c(s)) = \frac{d}{ds}\bigg|_{s=0} g\, c(s)\, g^{-1} \qquad \text{(definition of the differential along the curve } c; \ \alpha_g(c(s)) = g c(s) g^{-1}\text{).}$$
> > The map $\Phi\colon \operatorname{Mat}(n \times n; \mathbb{K}) \to \operatorname{Mat}(n \times n; \mathbb{K})$, $M \mapsto gMg^{-1}$, is $\mathbb{K}$-linear (left and right matrix multiplication by fixed matrices are linear), and the derivative of a linear map applied to a curve is the linear map applied to the curve's velocity:
> > $$\frac{d}{ds}\bigg|_{0} g\,c(s)\,g^{-1} = \frac{d}{ds}\bigg|_{0}\Phi(c(s)) = \Phi\big(\dot c(0)\big) = g\,\dot c(0)\,g^{-1} = g X g^{-1} \qquad \text{(linearity of } \Phi\text{; } \dot c(0) = X\text{).}$$
> > Hence $\operatorname{Ad}_g X = gXg^{-1}$.
> >
> > **Worked instance ($SU(2)$, realising Bär's Example 1.3.8).** Take $g = \operatorname{diag}(e^{i\varphi}, e^{-i\varphi}) \in SU(2)$, so $g^{-1} = \operatorname{diag}(e^{-i\varphi}, e^{i\varphi})$, and the basis $-i\sigma_1, -i\sigma_2, -i\sigma_3$ of $\mathfrak{su}(2)$ above. Then
> > $$\operatorname{Ad}_g(-i\sigma_1) = g\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}g^{-1} = \begin{pmatrix} 0 & e^{i\varphi} \\ -e^{-i\varphi} & 0 \end{pmatrix}\begin{pmatrix} e^{-i\varphi} & 0 \\ 0 & e^{i\varphi} \end{pmatrix} = \begin{pmatrix} 0 & e^{2i\varphi} \\ -e^{-2i\varphi} & 0 \end{pmatrix} \qquad \text{(part ii, then multiply).}$$
> > Writing $e^{2i\varphi} = \cos 2\varphi + i\sin 2\varphi$ and $-e^{-2i\varphi} = -\cos 2\varphi + i\sin 2\varphi$ and splitting into the basis,
> > $$\begin{pmatrix} 0 & e^{2i\varphi} \\ -e^{-2i\varphi} & 0 \end{pmatrix} = \cos 2\varphi\begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix} + \sin 2\varphi\begin{pmatrix} 0 & i \\ i & 0 \end{pmatrix} = \cos(2\varphi)(-i\sigma_1) + \sin(2\varphi)(-i\sigma_2).$$
> > The identical computation gives $\operatorname{Ad}_g(-i\sigma_2) = \cos(2\varphi)(-i\sigma_2) - \sin(2\varphi)(-i\sigma_1)$ — indeed $g\left(\begin{smallmatrix} 0 & i \\ i & 0 \end{smallmatrix}\right)g^{-1} = \left(\begin{smallmatrix} 0 & i e^{2i\varphi} \\ i e^{-2i\varphi} & 0 \end{smallmatrix}\right)$ and $ie^{2i\varphi} = i\cos 2\varphi - \sin 2\varphi$, $ie^{-2i\varphi} = i\cos 2\varphi + \sin 2\varphi$, which recombine as $\cos 2\varphi(-i\sigma_2) - \sin 2\varphi(-i\sigma_1)$ — and $\operatorname{Ad}_g(-i\sigma_3) = g\left(\begin{smallmatrix} i & 0 \\ 0 & -i \end{smallmatrix}\right)g^{-1} = \left(\begin{smallmatrix} i & 0 \\ 0 & -i \end{smallmatrix}\right) = -i\sigma_3$ (diagonal matrices commute). In the ordered basis $(-i\sigma_1, -i\sigma_2, -i\sigma_3)$ this is the matrix
> > $$\operatorname{Ad}_g = \begin{pmatrix} \cos 2\varphi & -\sin 2\varphi & 0 \\ \sin 2\varphi & \cos 2\varphi & 0 \\ 0 & 0 & 1 \end{pmatrix},$$
> > a rotation by $2\varphi$. Taking instead $g = -1_2$: $\operatorname{Ad}_{-1_2}X = (-1_2)X(-1_2)^{-1} = X$ for all $X$, so $\operatorname{Ad}_{-1_2} = \operatorname{id}_{\mathfrak{su}(2)}$, exhibiting $-1_2 \neq e$ in $\ker\operatorname{Ad}$ (Bär's Remark 1.3.9): $\operatorname{Ad}_{SU(2)}$ is not faithful.

> [!note]- Lemma 4: Conjugation by $\exp(tX)$ is the flow-pullback of $Y$
> **Statement:** Let $X, Y \in \mathfrak{g}$, regarded as left-invariant vector fields. Let $\theta_t := R_{\exp(tX)}$, which is the flow of $X$. Then for every $t$,
> $$\operatorname{Ad}_{\exp(tX)} Y_e = d\big(\theta_{-t}\big)_{\theta_t(e)}\big(Y_{\theta_t(e)}\big).$$
>
> **Hint:** Use left-invariance $Y_{\exp(tX)} = d(L_{\exp tX})_e Y_e$ and $\alpha_g = R_{g^{-1}}\circ L_g$.
>
> **Why needed:** It rewrites the algebraic object $\operatorname{Ad}_{\exp tX}Y$ as a geometric flow-pullback, the form in which its $t$-derivative is the Lie bracket.
>
> > [!note]- Full proof
> > **The flow of $X$ is right translation by $\exp(tX)$.** By [[Thm - One-Parameter Subgroups are the Integral Curves of Left-Invariant Vector Fields]] — whose relevant conclusion is that the integral curve of the left-invariant field $X$ through a point $g$ is $t \mapsto g\exp(tX)$, so that the (global) flow of $X$ is $\theta_t = R_{\exp(tX)}$, $\theta_t(g) = g\exp(tX)$ — the field $X$ is complete and $\theta_t$ is a diffeomorphism of $G$ for each $t$, with $\theta_t(e) = \exp(tX)$ and $\theta_{-t} = R_{\exp(-tX)}$.
> >
> > **Rewrite the right-hand side using left-invariance.** Since $Y$ is left-invariant, $Y_g = d(L_g)_e Y_e$ for all $g$ (the defining property of the left-invariant extension of $Y_e \in \mathfrak{g}$). At $g = \theta_t(e) = \exp(tX)$,
> > $$Y_{\theta_t(e)} = Y_{\exp(tX)} = d\big(L_{\exp(tX)}\big)_e Y_e \qquad \text{(left-invariance of } Y\text{).}$$
> > Apply $d(\theta_{-t})_{\theta_t(e)} = d\big(R_{\exp(-tX)}\big)_{\exp(tX)}$ and use the chain rule:
> > $$d(\theta_{-t})_{\theta_t(e)}\big(Y_{\theta_t(e)}\big) = d\big(R_{\exp(-tX)}\big)_{\exp(tX)}\,d\big(L_{\exp(tX)}\big)_e\, Y_e = d\big(R_{\exp(-tX)}\circ L_{\exp(tX)}\big)_e\, Y_e \qquad \text{(chain rule).}$$
> >
> > **Recognise conjugation.** With $g = \exp(tX)$ one has $g^{-1} = \exp(-tX)$, so $R_{\exp(-tX)}\circ L_{\exp(tX)} = R_{g^{-1}}\circ L_g = \alpha_g = \alpha_{\exp(tX)}$ (the standing identity $\alpha_g = L_g\circ R_{g^{-1}} = R_{g^{-1}}\circ L_g$; left and right translations commute because $(gh)k = g(hk)$). Therefore
> > $$d(\theta_{-t})_{\theta_t(e)}\big(Y_{\theta_t(e)}\big) = d\big(\alpha_{\exp(tX)}\big)_e\,Y_e = \operatorname{Ad}_{\exp(tX)} Y_e \qquad \text{(definition of } \operatorname{Ad}\text{).}$$
> > This is the claimed identity.

> [!note]- Lemma 5: The $t$-derivative of the flow-pullback is the bracket
> **Statement:** With $X, Y \in \mathfrak{g}$ and $\theta_t = R_{\exp(tX)}$ the flow of $X$,
> $$\frac{d}{dt}\bigg|_{t=0} d(\theta_{-t})_{\theta_t(e)}\big(Y_{\theta_t(e)}\big) = [X, Y]_e,$$
> where $[X,Y]$ is the [[Def - The Lie Bracket of Vector Fields|Lie bracket]] of the vector fields $X, Y$, characterised on functions by $[X,Y]f = X(Yf) - Y(Xf)$.
>
> **Hint:** Evaluate on an arbitrary $f \in C^\infty(G)$; write the result as $H(t,-t)$ with $H(t,u) = Y_{\theta_t(e)}(f\circ\theta_u)$, apply the chain rule, and use Schwarz's theorem on the one mixed second derivative that appears.
>
> **Why needed:** Combined with Lemma 4 it is exactly $\frac{d}{dt}\big|_0 \operatorname{Ad}_{\exp tX} Y = [X,Y]$, the identity $\operatorname{Ad}_* = \operatorname{ad}$.
>
> > [!note]- Full proof
> > Write $c(t) := d(\theta_{-t})_{\theta_t(e)}\big(Y_{\theta_t(e)}\big) \in T_eG = \mathfrak{g}$; this is a smooth curve in the finite-dimensional vector space $\mathfrak{g}$ (smooth because the flow $\theta$ is smooth jointly in $(t, \text{point})$ by [[Thm - Fundamental Theorem on Flows]], and $Y$ is a smooth field). We must compute $c'(0) \in \mathfrak{g}$. Since a tangent vector at $e$ is determined by its action on functions, and evaluation $v \mapsto vf$ is a fixed linear functional on the finite-dimensional space $\mathfrak{g}$ (hence commutes with $\tfrac{d}{dt}$), it suffices to show $c'(0)f = [X,Y]_e f$ for every $f \in C^\infty(G)$.
> >
> > **Express the action on $f$.** For a differential, $\big(d(\theta_{-t})_{p}\,v\big)f = v(f\circ\theta_{-t})$ with $p = \theta_t(e)$ and $v = Y_{\theta_t(e)}$; thus
> > $$c(t)f = Y_{\theta_t(e)}\big(f\circ\theta_{-t}\big).$$
> > Introduce the auxiliary function of two variables
> > $$H(t, u) := Y_{\theta_t(e)}\big(f\circ\theta_u\big),$$
> > which is smooth in $(t,u)$ because $\theta$ is a smooth flow, $Y$ and $f$ are smooth, and $Y_{\theta_t(e)}(f\circ\theta_u) = \big(Y(f\circ\theta_u)\big)(\theta_t(e))$ depends smoothly on both arguments. Then $c(t)f = H(t, -t)$, so by the chain rule
> > $$c'(0)f = \frac{d}{dt}\bigg|_{0} H(t, -t) = \partial_t H(0,0) - \partial_u H(0,0) \qquad \text{(chain rule for } t \mapsto (t, -t)\text{).}$$
> > We compute the two partials.
> >
> > **The $t$-partial gives $X(Yf)$.** Setting $u = 0$ (so $\theta_0 = \operatorname{id}_G$ and $f\circ\theta_0 = f$),
> > $$H(t, 0) = Y_{\theta_t(e)} f = (Yf)\big(\theta_t(e)\big).$$
> > The curve $t \mapsto \theta_t(e) = \exp(tX)$ has velocity $X_e$ at $t = 0$ (it is the integral curve of $X$ through $e$), so
> > $$\partial_t H(0,0) = \frac{d}{dt}\bigg|_{0}(Yf)\big(\theta_t(e)\big) = X_e(Yf) = \big(X(Yf)\big)(e) \qquad \text{(definition of the tangent vector } X_e \text{ acting on } Yf\text{).}$$
> >
> > **The $u$-partial gives $Y(Xf)$.** Setting $t = 0$ (so $\theta_0(e) = e$),
> > $$H(0, u) = Y_e\big(f\circ\theta_u\big).$$
> > Represent $Y_e$ by the curve $s \mapsto \exp(sY)$, which passes through $e$ with velocity $Y_e$:
> > $$H(0,u) = Y_e\big(f\circ\theta_u\big) = \frac{d}{ds}\bigg|_{0}(f\circ\theta_u)\big(\exp(sY)\big) = \frac{d}{ds}\bigg|_{0} f\big(\exp(sY)\exp(uX)\big) = \partial_s\Psi(0, u),$$
> > where $\Psi(s, u) := f\big(\exp(sY)\exp(uX)\big)$ is smooth (composition of smooth maps), and we used $\theta_u = R_{\exp(uX)}$, so $\theta_u(\exp sY) = \exp(sY)\exp(uX)$. Hence
> > $$\partial_u H(0,0) = \partial_u\big|_{0}\,\partial_s\big|_{0}\,\Psi(s,u) = \partial_s\big|_{0}\,\partial_u\big|_{0}\,\Psi(s,u) \qquad \text{(Schwarz's theorem: } \Psi \in C^\infty, \text{ so mixed second partials are equal).}$$
> > For the inner derivative, at fixed $s$ the curve $u \mapsto \exp(sY)\exp(uX) = L_{\exp(sY)}\big(\exp(uX)\big)$ has velocity $d(L_{\exp sY})_e X_e = X_{\exp(sY)}$ at $u = 0$ (left-invariance of $X$), so
> > $$\partial_u\big|_{0}\Psi(s, 0) = X_{\exp(sY)} f = (Xf)\big(\exp(sY)\big).$$
> > Then differentiating in $s$ (again $\exp(sY)$ has velocity $Y_e$ at $0$),
> > $$\partial_s\big|_{0}(Xf)\big(\exp(sY)\big) = Y_e(Xf) = \big(Y(Xf)\big)(e),$$
> > so $\partial_u H(0,0) = \big(Y(Xf)\big)(e)$.
> >
> > **Combine.** Subtracting,
> > $$c'(0)f = \partial_t H(0,0) - \partial_u H(0,0) = \big(X(Yf)\big)(e) - \big(Y(Xf)\big)(e) = \big(X(Yf) - Y(Xf)\big)(e) = [X,Y]_e f \qquad \text{(defining formula } [X,Y]f = X(Yf) - Y(Xf)\text{).}$$
> > Since $f \in C^\infty(G)$ was arbitrary and both $c'(0)$ and $[X,Y]_e$ are tangent vectors at $e$, we conclude $c'(0) = [X,Y]_e$.

---

# Formal Proof

> [!note]- Complete formal proof
> Let $G$ be a Lie group with Lie algebra $\mathfrak{g} = T_eG$, and $\operatorname{Ad}_g = d_e\alpha_g$ with $\alpha_g(h) = ghg^{-1}$.
>
> **Step 0 — the target objects are well-posed.** Because $\alpha_g(e) = geg^{-1} = e$, the differential $\operatorname{Ad}_g = d_e\alpha_g$ is a linear map $T_eG \to T_eG$, i.e. an element of $\operatorname{End}(\mathfrak{g})$; this makes the assignment $g \mapsto \operatorname{Ad}_g$ a map $G \to \operatorname{End}(\mathfrak{g})$ before any claim about it. The codomain $GL(\mathfrak{g})$ in (i) is the open subset of invertible elements of the vector space $\operatorname{End}(\mathfrak{g})$; its tangent space at the identity, appearing in (iii), is $T_{\operatorname{id}}GL(\mathfrak{g}) = \operatorname{End}(\mathfrak{g})$ (a nonempty open subset of a vector space has that vector space as tangent space at each point), so $\operatorname{Ad}_* = d_e\operatorname{Ad}\colon \mathfrak{g} \to \operatorname{End}(\mathfrak{g})$ is the object to be identified with $\operatorname{ad}$.
>
> **Part (i) — $\operatorname{Ad}$ is a representation.** By **Lemma 1**, each $\operatorname{Ad}_g$ is a linear automorphism of $\mathfrak{g}$ and $\operatorname{Ad}\colon G \to GL(\mathfrak{g})$ satisfies $\operatorname{Ad}_{g_1 g_2} = \operatorname{Ad}_{g_1}\circ\operatorname{Ad}_{g_2}$, $\operatorname{Ad}_e = \operatorname{id}_{\mathfrak{g}}$, $(\operatorname{Ad}_g)^{-1} = \operatorname{Ad}_{g^{-1}}$; so $\operatorname{Ad}$ is a group homomorphism into $GL(\mathfrak{g})$. By **Lemma 2**, $\operatorname{Ad}$ is smooth. A smooth group homomorphism $G \to GL(\mathfrak{g}) = \operatorname{Aut}(\mathfrak{g})$ into the automorphism group of a finite-dimensional vector space is, by definition, a representation of $G$ on $\mathfrak{g}$ (see [[Def - Representation of a Lie Group]]). Hence (i) holds.
>
> **Part (ii) — matrix conjugation.** This is **Lemma 3**: for a matrix group $G \subset GL(n;\mathbb{K})$ and $X \in \mathfrak{g} \subset \operatorname{Mat}(n\times n;\mathbb{K})$, the linearity of $M \mapsto gMg^{-1}$ gives $\operatorname{Ad}_g X = gXg^{-1}$.
>
> **Part (iii) — the differential is $\operatorname{ad}$.** Fix $X, Y \in \mathfrak{g}$. Because $t \mapsto \exp(tX)$ is a curve through $e$ with velocity $X$ at $t = 0$, the definition of the differential $\operatorname{Ad}_* = d_e\operatorname{Ad}$ gives, for the endomorphism-valued map $\operatorname{Ad}$,
> $$\operatorname{Ad}_*(X) = \frac{d}{dt}\bigg|_{0}\operatorname{Ad}_{\exp(tX)} \in \operatorname{End}(\mathfrak{g}), \qquad \text{so} \qquad \operatorname{Ad}_*(X)\,Y = \frac{d}{dt}\bigg|_{0}\operatorname{Ad}_{\exp(tX)}Y,$$
> the last equality because evaluation at the fixed vector $Y$ is linear and continuous, hence commutes with $\tfrac{d}{dt}$. Now apply **Lemma 4**, which identifies $\operatorname{Ad}_{\exp(tX)}Y_e = d(\theta_{-t})_{\theta_t(e)}(Y_{\theta_t(e)})$ with $\theta_t = R_{\exp(tX)}$ the flow of $X$, and then **Lemma 5**, which differentiates that flow-pullback:
> $$\operatorname{Ad}_*(X)\,Y = \frac{d}{dt}\bigg|_{0}\operatorname{Ad}_{\exp(tX)}Y = \frac{d}{dt}\bigg|_{0} d(\theta_{-t})_{\theta_t(e)}\big(Y_{\theta_t(e)}\big) = [X, Y] \qquad \text{(Lemma 4, then Lemma 5).}$$
> Since $\operatorname{ad}(X)Y := [X,Y]$ by definition, this reads $\operatorname{Ad}_*(X)Y = \operatorname{ad}(X)Y$ for all $X, Y$, that is $\operatorname{Ad}_* = \operatorname{ad}$. The argument used no matrix structure, so it holds for every Lie group.
>
> *Consistency with the matrix case.* When $G$ is a matrix group, part (ii) gives $\operatorname{Ad}_{\exp(tX)}Y = e^{tX} Y e^{-tX}$, and the general result specialises to the Leibniz computation
> $$\frac{d}{dt}\bigg|_{0} e^{tX} Y e^{-tX} = \Big(\tfrac{d}{dt}\big|_0 e^{tX}\Big) Y\,1_n + 1_n\,Y\,\Big(\tfrac{d}{dt}\big|_0 e^{-tX}\Big) = XY\,1_n + 1_n\,Y(-X) = XY - YX = [X,Y],$$
> using $\tfrac{d}{dt}\big|_0 e^{\pm tX} = \pm X$ and the product rule; this recovers Bär's Remark 1.4.8 and confirms the general formula in the smallest concrete case.
>
> **Part (iv) — abelian groups.** If $G$ is abelian then for every $g, h \in G$, $\alpha_g(h) = ghg^{-1} = hgg^{-1} = h$, so $\alpha_g = \operatorname{id}_G$ and hence $\operatorname{Ad}_g = d_e\alpha_g = d_e\operatorname{id}_G = \operatorname{id}_{\mathfrak{g}}$; the representation is trivial. (Consistently, part (iii) then yields $[X,Y] = \operatorname{Ad}_*(X)Y = \tfrac{d}{dt}\big|_0\operatorname{id}_{\mathfrak{g}}\,Y = 0$, so an abelian Lie group has abelian Lie algebra.)
>
> All four parts are established. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The double cover $SU(2) \to SO(3)$ and half-integer spin (mathematical physics).** Using part (ii), compute $\operatorname{Ad}\colon SU(2) \to GL(\mathfrak{su}(2)) \cong GL(3; \mathbb{R})$ and check that its image lies in $SO(3)$ (conjugation preserves the $\operatorname{Ad}$-invariant inner product $-\operatorname{tr}(XY)$ on $\mathfrak{su}(2)$), that it is surjective, and that its kernel is $\{\pm 1_2\}$; conclude $SU(2)/\{\pm 1\} \cong SO(3)$. The theorem applies because $\operatorname{Ad}$ is exactly the homomorphism $SU(2) \to SO(3)$, and it is non-obvious that a purely group-theoretic construction (conjugation) produces the spin double cover — the doubling of the angle in Lemma 3's matrix is the entire content of "spin one-half".

**Bi-invariant metrics and geodesics on compact groups (Riemannian geometry).** Show that an inner product on $\mathfrak{g}$ extends to a bi-invariant Riemannian metric on $G$ if and only if it is $\operatorname{Ad}(G)$-invariant, i.e. $\langle \operatorname{Ad}_g X, \operatorname{Ad}_g Y\rangle = \langle X, Y\rangle$ for all $g$; and, differentiating this with part (iii), that $\operatorname{Ad}$-invariance is equivalent to $\langle [Z,X], Y\rangle + \langle X, [Z,Y]\rangle = 0$ (invariance under $\operatorname{ad}$). The theorem applies because bi-invariance is precisely two-sided translation-invariance, which reduces to $\operatorname{Ad}$-invariance on $\mathfrak{g}$; the non-obvious part is that the global metric condition collapses to the linear-algebra condition on the Lie algebra, and this is what makes the geodesics of a bi-invariant metric equal to the one-parameter subgroups $t \mapsto \exp(tX)$.

**The adjoint bundle and the space of connections (gauge theory).** For a principal $G$-bundle $P \to M$, form the associated bundle $\operatorname{ad}P = P \times_{\operatorname{Ad}} \mathfrak{g}$ using the adjoint representation; show that the difference of two connections is an $\operatorname{ad}P$-valued one-form, and that the gauge group acts on it through $\operatorname{Ad}$. The theorem applies because the equivariance and curvature calculus of connections is built on $\operatorname{Ad}$ and its differential $\operatorname{ad}$; it is non-obvious that the local transformation law $A' = \operatorname{Ad}_{g^{-1}}A + g^{-1}dg$ is globally the statement that $A$-differences are sections of a *representation-associated* bundle, which is exactly what part (i) guarantees ($\operatorname{Ad}$ is a representation, so the associated bundle exists).

---

# Bridges

- **[[Def - Adjoint Representation]]** — the definition this theorem certifies. The definition page introduces $\operatorname{Ad}_g = d_e\alpha_g$ and $\operatorname{ad}_X = [X,\cdot]$ as objects; the present theorem proves that $\operatorname{Ad}$ deserves the name "representation" (part i) and that $\operatorname{ad}$ is literally its differential (part iii), so that the two definitions are not independent but the group and infinitesimal faces of one construction.

- **[[Thm - Lie Group Homomorphism Induces Lie Algebra Homomorphism|the differential of a homomorphism is a Lie algebra homomorphism]]** — a direct consequence. For a Lie group homomorphism $\varphi\colon G \to H$, differentiating the identity $\varphi\circ\alpha_g = \alpha_{\varphi(g)}\circ\varphi$ at $e$ gives $\varphi_*\circ\operatorname{Ad}_g = \operatorname{Ad}_{\varphi(g)}\circ\varphi_*$; differentiating that in $g$ along $\exp(tX)$ and using part (iii) on both $G$ and $H$ yields $\varphi_*[X,Y] = [\varphi_* X, \varphi_* Y]$. Thus "brackets are preserved" is a corollary of "adjoint representations intertwine", and this theorem is the engine of that companion result.

- **[[Thm - The Exponential Map of a Compact Connected Lie Group is Surjective|bi-invariant metrics on compact groups]]** — an application. A compact Lie group carries a bi-invariant Riemannian metric because one can average any inner product on $\mathfrak{g}$ over the compact subgroup $\operatorname{Ad}(G) \subset GL(\mathfrak{g})$ — a construction that exists only because part (i) makes $\operatorname{Ad}$ a genuine (hence continuous, hence compact-image) representation; the geodesics of that metric are the one-parameter subgroups, which is how surjectivity of $\exp$ is proved.

- **The structure equation and Bianchi identity for principal connections (chapter IV)** — the infinitesimal payoff. The equivariance $R_g^*\omega = \operatorname{Ad}_{g^{-1}}\omega$ of a principal connection form, differentiated along $\exp(t\xi)$, produces the bracket $\operatorname{ad}_\xi = [\xi, \cdot]$ by part (iii); this is the differentiation that turns the $\operatorname{Ad}$-transformation law into the $\tfrac12[\omega\wedge\omega]$ term of the curvature and into the covariant exterior derivative. Every appearance of a Lie bracket in the curvature calculus is this theorem applied once.

---

# Unlocked by This

> [!tip] The Killing form and semisimplicity *(from Lie theory)*
> Because $\operatorname{ad} = \operatorname{Ad}_*$ is a representation of $\mathfrak{g}$ on itself (part iii together with the fact that the differential of a representation is a representation), the symmetric bilinear form $B(X, Y) := \operatorname{tr}(\operatorname{ad}_X \operatorname{ad}_Y)$ — the **Killing form** — is defined and is $\operatorname{Ad}$-invariant. Cartan's criterion characterises semisimple Lie algebras by non-degeneracy of $B$, and the whole structure theory (root systems, the classification of simple Lie algebras) rests on studying $\operatorname{ad}$. None of this is available until one knows $\operatorname{ad}$ is a representation, which is this theorem.

> [!tip] The adjoint bundle $\operatorname{ad}P$ *(from gauge theory)*
> Since $\operatorname{Ad}\colon G \to GL(\mathfrak{g})$ is a representation (part i), any principal $G$-bundle $P \to M$ has an associated vector bundle $\operatorname{ad}P = P\times_{\operatorname{Ad}}\mathfrak{g}$ with fibre $\mathfrak{g}$. The curvature of a connection is a two-form valued in $\operatorname{ad}P$, the infinitesimal gauge transformations are its sections, and the Yang–Mills field lives there. The existence of $\operatorname{ad}P$ is a direct dividend of part (i); its fibrewise bracket, making it a bundle of Lie algebras, is a dividend of part (iii).
