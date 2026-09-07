---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Principal G-Bundle"
  - "Thm - Quotient Manifold Theorem for Free Proper Actions"
  - "Def - Free, Transitive, Effective, and Proper Group Actions"
  - "Def - Fundamental Vector Field of a Group Action"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $G$ is a Lie group of dimension $k$ with identity $e$, Lie algebra $\mathfrak{g} = T_eG$, and exponential map $\exp : \mathfrak{g} \to G$. The letter $P$ denotes a smooth manifold of dimension $n$; "smooth" means $C^\infty$, and all manifolds are Hausdorff and second countable. A **right action** of $G$ on $P$ is a smooth map $P \times G \to P$, written $(p, g) \mapsto p \cdot g$ or $pg$, with $p \cdot e = p$ and $(p \cdot g) \cdot g' = p \cdot (g g')$; the map $R_g : P \to P$, $R_g(p) = p \cdot g$, is the right translation by $g$.

We follow the series standing convention that Lie groups act on principal bundles on the **right**. For $\xi \in \mathfrak{g}$ the **fundamental vector field** on the right $G$-space $P$ is
$$\xi_P(p) = \frac{d}{dt}\Big|_{t=0}\, p \cdot \exp(t\xi) \in T_pP,$$
the infinitesimal generator of the action in the direction $\xi$; see [[Def - Fundamental Vector Field of a Group Action|fundamental vector field]]. The **orbit** of $p$ is $p \cdot G = \{p \cdot g : g \in G\}$, and the **orbit space** $P/G$ is the set of orbits with the quotient topology; the **orbit map** through $p$ is
$$\ell_p : G \to P, \qquad \ell_p(g) = p \cdot g.$$

An action is **free** if $p \cdot g = p$ for some $p$ forces $g = e$ (equivalently, every stabiliser is trivial), and **proper** if the map $\Theta : G \times P \to P \times P$, $(g, p) \mapsto (p \cdot g,\, p)$, is a proper map (preimages of compact sets are compact); see [[Def - Free, Transitive, Effective, and Proper Group Actions|free, transitive, and proper actions]]. On a manifold, which is locally compact, Hausdorff, and second countable, properness of $\Theta$ is equivalent to the **sequential criterion**: whenever $p_i \to p$ and $p_i \cdot g_i \to q$ in $P$, the sequence $(g_i)$ in $G$ has a convergent subsequence. We use this criterion below and cite it from the same page.

A **principal $G$-bundle** is a [[Def - Fibre Bundle|fibre bundle]] $\pi : P \to M$ carrying a smooth right $G$-action that is fibre-preserving, free, transitive on each fibre, and admits $G$-equivariant local trivialisations; the full four-clause definition and its consequences are on [[Def - Principal G-Bundle|the principal-bundle page]]. For a smooth left $G$-manifold $F$ (a manifold with a smooth left action $G \times F \to F$, $(g, f) \mapsto g \cdot f$), we write $P \times_G F := (P \times F)/G$ for the quotient of $P \times F$ by the diagonal right action introduced below; a class is written $[p, f]$.

The symbol $\pi$ denotes the bundle projection, $M := P/G$ the base, and $E := P \times_G F$ the total space of the associated bundle; $\operatorname{pr}_1, \operatorname{pr}_2$ are the two projections of a product, and $\varpi : P \times F \to E$ is the quotient map.

> [!warning] Convention: "properly discontinuous" versus "proper"
> Constructing the associated bundle, Haydys (page 14) writes that the diagonal action on $P \times V$ is "free and **properly discontinuous**", and Bär (Remark 2.2.3) proves the first half only for **compact** $G$. Neither phrasing is the right general hypothesis. *Properly discontinuous* is the correct condition only for a **discrete** (zero-dimensional) group $\Gamma$, where it means every point has a neighbourhood $W$ with $W \cdot \gamma \cap W = \varnothing$ for all but finitely many $\gamma \in \Gamma$; for such a group, together with freeness, it coincides with properness. For a positive-dimensional Lie group $G$ the fibre $G$ is not discrete and "properly discontinuous" fails outright, so it cannot be the hypothesis. The correct general hypothesis — the one this page proves suffices, and the one the [[Thm - Quotient Manifold Theorem for Free Proper Actions|quotient manifold theorem]] requires — is that the action is **free and proper**. *Conversion recipe:* wherever a source says "free and properly discontinuous" for a group that is not discrete, read "free and proper"; the two agree exactly when $G$ is discrete.

---

# Statement

> **Theorem (free proper actions give principal bundles).** Let $G$ be a Lie group acting smoothly, **freely**, and **properly** on the right on a smooth manifold $P$. Then, with $M := P/G$ and $\pi : P \to M$, $\pi(p) = p \cdot G$, the triple $(P, \pi, M)$ is a **principal $G$-bundle**.
>
> In particular, if $G$ is **compact** and acts smoothly and freely on $P$, the action is automatically proper, and the conclusion holds.

> **Theorem (the associated fibre bundle).** Let $\pi : P \to M$ be a principal $G$-bundle and let $F$ be a smooth manifold on which $G$ acts smoothly on the **left**. Then the **diagonal right action** of $G$ on $P \times F$,
> $$(p, f) \cdot g := (p \cdot g,\; g^{-1} \cdot f),$$
> is smooth, free, and proper, so that $E := P \times_G F = (P \times F)/G$ is a smooth manifold. The map
> $$\pi_E : E \to M, \qquad \pi_E([p, f]) = \pi(p),$$
> is well defined and makes $(E, \pi_E, M)$ a **fibre bundle with typical fibre $F$**, the fibre bundle **associated** with $P$ through the given action. (When $F = V$ is a vector space and the action is a representation, $E$ is a vector bundle; when $F = H$ is a Lie group and the action comes from a homomorphism, $E$ is again a principal bundle. These specialisations are developed on [[Def - Associated Bundle|the associated-bundle page]] in §3.4.)

The two statements are the two halves of one construction: the first manufactures principal bundles out of nothing but a free proper action, and the second feeds a principal bundle back through a fibre $F$ to manufacture every bundle "associated" with it. The engine of both is the [[Thm - Quotient Manifold Theorem for Free Proper Actions|quotient manifold theorem]].

---

# Motivation

A principal bundle is a bundle of *frames of reference*: over each point of the base sits a copy of the structure group $G$, and $G$ acts by "changing the frame". Chapter II built such bundles by hand — the frame bundle of a vector bundle, the Hopf bundle — by writing down charts and checking the four defining clauses one at a time. That is laborious, and it obscures where principal bundles actually come from. The present theorem gives the conceptual source: **wherever a Lie group acts on a manifold without fixed points and without letting orbits run off to infinity, the orbit projection is already a principal bundle.** One does not have to build the local trivialisations; the quotient manifold theorem builds them, and freeness plus transitivity on the orbits coordinatise each fibre by $G$.

The importance of the two hypotheses is worth stating before the proof, because each rules out a specific pathology, and the [[Thm - Quotient Manifold Theorem for Free Proper Actions|quotient manifold theorem]] fails without either. **Freeness** is what makes a fibre look like $G$ rather than like $G$ modulo a stabiliser: if some $p$ had a nontrivial stabiliser, its orbit would be a copy of $G/\operatorname{Stab}(p)$, of the wrong dimension, and neighbouring orbits of different dimensions could not be assembled into a bundle. The rotation action of the circle $SO(2)$ on the sphere $S^2$ fixing the two poles is the standard warning: the generic orbit is a circle but the polar orbits are points, so $S^2 / SO(2) \cong [-1, 1]$ is not even a manifold without boundary, and $S^2 \to [-1,1]$ is not a bundle. **Properness** is what keeps the orbit space Hausdorff and keeps orbits from accumulating on one another. The irrational-slope flow of $\mathbb{R}$ on the torus $T^2$ is free but not proper — every orbit is dense — and the quotient $T^2 / \mathbb{R}$ has the indiscrete topology, no manifold at all.

The second half answers a different question. Given a principal bundle $P$ — a bundle of frames — and a space $F$ that $G$ knows how to act on, we would like the bundle whose fibre is $F$ "seen through those frames". The naive product $P \times F$ is too big: it remembers the choice of frame, whereas $F$-data should be recorded independently of the frame. The remedy is to identify $(p, f)$ with $(p \cdot g, g^{-1} \cdot f)$: changing the frame by $g$ and compensating the $F$-value by $g^{-1}$ leaves the geometric datum unchanged. Quotienting by this identification is exactly the diagonal action above, and the theorem says the quotient is a genuine fibre bundle. This single construction produces every associated object of gauge theory — the tangent, tensor, and adjoint bundles, the vector bundle of a representation, the extension of a structure group — and each is obtained by choosing the fibre $F$ and the action.

Bär records the first half only for **compact** $G$ (his Remark 2.2.3, an extension of his Theorem 1.5.11) and defers two points to "the general theory of group actions": that the quotient $(P \times F)/G$ is a manifold even when $G$ is **non-compact**, and that the descended projection is smooth. Haydys, constructing the associated bundle (his page 14), asserts that the diagonal action is "free and properly discontinuous". Both remarks are exactly the gaps this page closes: the correct hypothesis for a general Lie group is *free and proper*, "properly discontinuous" being the special case of a discrete group, and the quotient-manifold theorem in its proper form supplies the manifold structure and the smoothness for every $G$.

---

# Sources and Targets

**Sources (Input Broadening)**

The literal hypotheses — a smooth, free, proper right action — are rarely handed over in those words. The skill is to recognise the disguises.

The first disguised source is **compactness of the acting group**. If $G$ is a compact Lie group acting smoothly and freely, then it acts properly, so the theorem applies with no further check. The bridge is that a compact group always acts properly: given a compact $K \subseteq P \times P$, the preimage $\Theta^{-1}(K)$ is a closed subset of $G \times \operatorname{pr}_2(K)$, a product of a compact group with a compact set, hence compact. This is non-obvious only in that "properness" sounds analytic while "compact" sounds algebraic; the moment one writes the preimage down, the two meet. *Example problem:* the orthonormal frame bundle of a Riemannian manifold arises from the free right action of the compact group $O(k)$ on the manifold of orthonormal frames, and is a principal $O(k)$-bundle for this reason alone.

The second disguised source is **a closed subgroup acting by translation**. Let $H$ be a closed subgroup of a Lie group $G$, acting on $G$ by right translation, $g \cdot h = gh$. This action is free by the cancellation law in a group, and it is proper precisely because $H$ is closed: if $g_i \to g$ and $g_i h_i \to q$, then $h_i = g_i^{-1}(g_i h_i) \to g^{-1} q$, and closedness of $H$ places the limit in $H$, giving a convergent subsequence. So the pair $(G, H)$ secretly satisfies the hypotheses, and the theorem yields that $G \to G/H$ is a principal $H$-bundle — the homogeneous-space bundles proved directly on the vault page [[Thm - Homogeneous Space is a Smooth Manifold|homogeneous space is a smooth manifold]]. The non-obvious step is that "closed subgroup" is the disguise for "proper action". *Example problem:* $SU(2) \to SU(2)/U(1) \cong S^2$ is the Hopf bundle, recovered by choosing $G = SU(2)$ and the closed torus $H = U(1)$.

The third disguised source is **a discrete group acting properly discontinuously**. For a discrete (zero-dimensional) Lie group $\Gamma$, properness of the action is equivalent to proper discontinuity in the covering-space sense (every point has a neighbourhood $W$ with $W \cap (W \cdot \gamma) = \varnothing$ for all but finitely many $\gamma$), and freeness is the additional condition that no nontrivial element has a fixed point. A free properly discontinuous action of a discrete group is therefore a free proper action, and the theorem specialises to: the covering projection $P \to P/\Gamma$ is a principal $\Gamma$-bundle with discrete structure group. The bridge — that "properly discontinuous" is exactly "proper" for discrete groups — is precisely the correction to Haydys's phrasing recorded in the convention callout below. *Example problem:* $\mathbb{Z}$ acting on $\mathbb{R}$ by translation is free and proper, so $\mathbb{R} \to \mathbb{R}/\mathbb{Z} \cong S^1$ is a principal $\mathbb{Z}$-bundle, the universal cover of the circle regarded as a bundle.

**Targets (Output Amplification)**

The bare output is a principal bundle, or a fibre bundle. Combined with one further ingredient it produces the working machinery of the subject.

Combine the associated-bundle output with **a linear representation $\rho : G \to GL(V)$** on a finite-dimensional vector space $V$. Taking $F = V$ with the left action $g \cdot v = \rho(g) v$, the theorem's second half gives the fibre bundle $P \times_\rho V$, and the fibrewise vector-space structure descends because $\rho(g)$ is linear; the further result $E$ is the **associated vector bundle**, the object that turns representation theory into bundle theory. This is non-obvious because the vector-space structure of the fibre is not visible in the quotient until one checks that $[p, v] + [p, w] := [p, v + w]$ is independent of the representative, which uses linearity of $\rho$. The construction is developed on [[Def - Associated Bundle|the associated-bundle page]].

Combine the associated-bundle output with **a Lie group homomorphism $\varphi : G \to H$**. Taking $F = H$ with the left action $g \cdot h = \varphi(g) h$, the diagonal action is $(p, h) \cdot g = (p g, \varphi(g)^{-1} h)$, and the residual right multiplication of $H$ on the second factor descends to a free transitive fibrewise action; the further result $E = P \times_\varphi H$ is again a **principal $H$-bundle**, the *extension of the structure group*. The payoff is a change of gauge group without rebuilding charts. This is exactly Bär's Conclusion 2.2.9, proved in the general (non-compact) case on the reduction-and-extension page.

Combine the first-half output with **a $G$-invariant geometric structure on $P$**. If $P$ carries a Riemannian metric, a symplectic form, or any tensor field that is invariant under the free proper $G$-action, the invariance lets the structure descend along the submersion $\pi$ to a corresponding structure on the base $M = P/G$; the further result is a **Riemannian submersion**, a **symplectic (Marsden–Weinstein) quotient**, or more generally the transport of geometry from total space to base. This is non-obvious because descent of a tensor requires both invariance (so it is constant along orbits) and horizontality (so it kills the vertical directions), and the free proper hypothesis is what makes the vertical distribution and the quotient available in the first place.

---

# Why Is It True

Strip away the machinery and look at what a free proper action does to $P$. The orbits partition $P$ into disjoint copies of $G$ — disjoint because the action is well defined, copies of $G$ because it is free and transitive on each orbit — and the quotient manifold theorem says these copies fit together into a smooth family: the orbit space $M = P/G$ is a manifold and $\pi$ is a submersion of the same "vertical codimension" $\dim G$ everywhere. A submersion has local sections, and a local section is a smooth choice of one point in each nearby fibre. Once you have chosen that one point $s(x)$ in the fibre over $x$, **every other point of that fibre is $s(x)$ moved by a unique group element**, because the orbit is a single free transitive $G$-set. So the fibre is coordinatised: the map $(x, g) \mapsto s(x) \cdot g$ is a bijection from $U \times G$ onto $\pi^{-1}(U)$, and its inverse reads off "which group element". That bijection is the local trivialisation, and it is automatically $G$-equivariant because moving $s(x) \cdot g$ further by $g'$ just multiplies the group coordinate.

> **The mechanism in one sentence: a free proper action makes the orbit projection a submersion whose fibres are single free transitive $G$-orbits, and a local section then coordinatises each fibre by $G$, which is exactly a principal-bundle chart.**

Two facts do the real work, and both are geometric. First, that the map $(x, g) \mapsto s(x) \cdot g$ is a *diffeomorphism*, not merely a bijection: its derivative in the $x$-direction covers the base (because $\pi \circ s = \operatorname{id}$), and its derivative in the $g$-direction sweeps out the vertical space (because a free action has an injective infinitesimal orbit map — no fundamental vector field vanishes), and these two families of directions are complementary, so the derivative is invertible and the inverse function theorem finishes the job. Second, for the associated bundle, the identification $(p, f) \sim (p g, g^{-1} f)$ is *itself* a free proper action, so the *same* theorem — applied a second time — gives its quotient a manifold structure; the local sections of $P$ then trivialise it, because a section $s$ lets one write every class as $[s(x), f]$ with $f \in F$ uniquely determined.

The intuition for the associated half is the "compensating change of frame". A point of $P$ is a frame; a point of $F$ is data expressed in that frame. Changing the frame by $g$ and simultaneously changing the data by $g^{-1}$ describes the *same* underlying object in a new frame — so the object is precisely the equivalence class $[p, f]$, and the bundle of such objects is $P \times_G F$.

---

# What Makes This Hard

The one genuinely non-trivial step is proving that the coordinate map $\psi_U^{-1}(x, g) = s(x) \cdot g$ has a **smooth inverse** — equivalently, that the group coordinate $g(p)$ of a point depends smoothly on $p$. Writing the inverse set-theoretically takes one line, but "the unique $g$ with $p = s(\pi(p)) g$" is a function whose smoothness is not automatic and must be argued. The clean way past this is not to construct $g(p)$ by hand but to show the derivative of $\psi_U^{-1}$ is everywhere an isomorphism (the vertical and horizontal directions are complementary, using freeness through the fundamental vector fields), so that a smooth bijection which is a local diffeomorphism is a diffeomorphism. The recurring error is to assume the local section can be chosen globally, or to conflate the free-proper hypotheses with the discrete "properly discontinuous" notion; the second confusion is Haydys's slip, harmless for his discrete examples but wrong in general.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** For the first half, feed the free proper action to the quotient manifold theorem to get a submersion $\pi : P \to M$ with local sections, then show the section-coordinate map $(x, g) \mapsto s(x) g$ is an equivariant diffeomorphism onto $\pi^{-1}(U)$ by checking its derivative is an isomorphism. For the second half, verify the diagonal action is free and proper, apply the *first half's* theorem to get the quotient manifold, and trivialise it with local sections of $P$.

**Subgoal decomposition:**

1. **Orbit maps of a free action are injective immersions with vertical image.** For every $p$, $\ell_p : G \to P$ is an injective immersion, and its differential at $g$ has image the vertical space $\ker d\pi_{\ell_p(g)}$.
   - *Hint:* Injectivity is freeness; for the immersion, reduce $d_g\ell_p$ to $d_e\ell_{pg}$ by a translation, and show $\xi \mapsto \xi_P(q)$ is injective because a vanishing fundamental field has constant flow.
   - *Why needed:* It supplies the vertical half of the derivative of $\psi_U^{-1}$ and identifies the fibres with $G$.

2. **The section-coordinate map is a diffeomorphism.** With a local section $s : U \to P$, the map $\psi_U^{-1}(x, g) = s(x) \cdot g$ is a diffeomorphism $U \times G \to \pi^{-1}(U)$ over $U$, and it is $G$-equivariant.
   - *Hint:* Bijectivity uses transitivity and freeness on fibres; for the diffeomorphism, count dimensions and show the derivative is injective by splitting into the $U$-part (a section of $d\pi$) and the $G$-part (Subgoal 1).
   - *Why needed:* It is the principal-bundle chart; all four clauses of the definition follow from it.

3. **Compact groups act properly.** A smooth action of a compact Lie group is proper.
   - *Hint:* Preimages of compacts under $\Theta$ sit inside a compact product.
   - *Why needed:* It is the "in particular" clause and the first disguised source.

4. **The structure action of a principal bundle is proper.** The right $G$-action on the total space of a principal bundle is proper.
   - *Hint:* Use the sequential criterion in a local trivialisation and equivariance; the group coordinates $a_i, a_i g_i$ converge, so $g_i = a_i^{-1}(a_i g_i)$ converges.
   - *Why needed:* It is the hypothesis the diagonal action inherits.

5. **The diagonal action is free and proper.** On $P \times F$ the action $(p, f) g = (pg, g^{-1} f)$ is free and proper.
   - *Hint:* Freeness needs only freeness on $P$; properness follows from Subgoal 4 by dropping the $F$-coordinate in the sequential criterion.
   - *Why needed:* It is the hypothesis of the first half, applied to build $E$.

6. **The associated total space is a fibre bundle.** $\pi_E : E \to M$ is well defined and smooth, with local trivialisations $[s(x), f] \leftrightarrow (x, f)$ from local sections of $P$.
   - *Hint:* Smoothness of $\pi_E$ is the universal property; smoothness of the inverse chart is descent of the $G$-invariant map $(p, f) \mapsto (\pi(p), g(p) f)$.
   - *Why needed:* It is the conclusion of the second half.

---

# Lemma Decomposition

> [!note]- Lemma 1: Orbit maps of a free action are injective immersions with vertical image
> **Statement:** Let $G$ act smoothly and freely on the right on a manifold $P$. For every $p \in P$ the orbit map $\ell_p : G \to P$, $\ell_p(g) = p \cdot g$, is a smooth injective immersion. If in addition $\pi : P \to M$ is a smooth submersion onto a manifold $M$ that is constant on orbits (so $\pi(p g) = \pi(p)$) and whose fibre $\pi^{-1}(\pi(p))$ equals the orbit $p \cdot G$, then for every $g \in G$ the image of $d_g\ell_p$ is exactly the vertical space $V_{\ell_p(g)} := \ker d\pi_{\ell_p(g)}$.
>
> **Hint:** Injectivity is freeness. For the immersion, translate $d_g\ell_p$ to $d_e\ell_{pg}$ and show $\xi \mapsto \xi_P(q)$ is injective by integrating the fundamental field. For the vertical image, compare dimensions.
>
> **Why needed:** It is the vertical half of the derivative computation in Lemma 2 and the reason each fibre is diffeomorphic to $G$.
>
> > [!note]- Full proof
> > **Injectivity.** Suppose $\ell_p(g) = \ell_p(g')$, that is $p \cdot g = p \cdot g'$. Acting on the right by $g'^{-1}$ and using the action axioms, $p \cdot (g g'^{-1}) = p$. Since the action is **free**, the only group element fixing $p$ is $e$, so $g g'^{-1} = e$, i.e. $g = g'$. Hence $\ell_p$ is injective.
> >
> > **The infinitesimal orbit map is injective.** Fix $q \in P$ and consider the linear map $\iota_q : \mathfrak{g} \to T_qP$, $\iota_q(\xi) = \xi_P(q) = \frac{d}{dt}\big|_{0}\, q \cdot \exp(t\xi)$, which is $d_e\ell_q$ evaluated on $T_e G = \mathfrak{g}$ (because $\ell_q(\exp(t\xi)) = q \cdot \exp(t\xi)$ and $\frac{d}{dt}|_0 \exp(t\xi) = \xi$). We show $\iota_q$ is injective. Suppose $\xi_P(q) = 0$. The fundamental vector field $\xi_P$ has flow $\theta_t(x) = x \cdot \exp(t\xi)$: indeed
> > $$\frac{d}{dt}\big(x \cdot \exp(t\xi)\big) = \frac{d}{ds}\Big|_{0}\, \big(x \cdot \exp(t\xi)\big) \cdot \exp(s\xi) = \xi_P\big(x \cdot \exp(t\xi)\big) \qquad \text{(by the one-parameter law } \exp((t+s)\xi) = \exp(t\xi)\exp(s\xi) \text{)},$$
> > so $t \mapsto x \cdot \exp(t\xi)$ is the integral curve of $\xi_P$ through $x$. If $\xi_P(q) = 0$ then $q$ is a stationary point of $\xi_P$, so its integral curve is constant (by uniqueness of integral curves, [[Thm - Fundamental Theorem on Flows|fundamental theorem on flows]]): $q \cdot \exp(t\xi) = q$ for all $t$. Freeness forces $\exp(t\xi) = e$ for all $t$, and differentiating at $t = 0$ gives $\xi = \frac{d}{dt}|_0 \exp(t\xi) = 0$. Thus $\ker \iota_q = 0$, so $\iota_q = d_e\ell_q$ is injective.
> >
> > **Immersion at every $g$.** For $g, h \in G$ one has $\ell_p = \ell_{p \cdot g} \circ L_{g^{-1}}$, where $L_{g^{-1}} : G \to G$ is left translation: indeed $\ell_{pg}(L_{g^{-1}} h) = \ell_{pg}(g^{-1} h) = (p g)(g^{-1} h) = p h = \ell_p(h)$ (by the action and group axioms). Differentiating at $h = g$ by the chain rule,
> > $$d_g\ell_p = d_{e}\ell_{p g} \circ d_g L_{g^{-1}} \qquad \text{(chain rule, since } L_{g^{-1}}(g) = e \text{)}.$$
> > Here $d_g L_{g^{-1}}$ is a linear isomorphism (left translation is a diffeomorphism of $G$), and $d_e\ell_{pg}$ is injective by the previous paragraph. A composite of an isomorphism followed by an injection is injective, so $d_g\ell_p$ is injective and $\ell_p$ is an immersion.
> >
> > **Vertical image.** Assume now $\pi : P \to M$ is a submersion, constant on orbits, with $\pi^{-1}(\pi(p)) = p \cdot G$. Since $\pi \circ \ell_p$ is constant (equal to $\pi(p)$, because $\ell_p$ maps into the orbit and $\pi$ is constant on it), differentiating gives $d\pi_{\ell_p(g)} \circ d_g\ell_p = 0$, so $\operatorname{im}(d_g\ell_p) \subseteq \ker d\pi_{\ell_p(g)} = V_{\ell_p(g)}$. Now count dimensions. Because $\ell_p$ is an immersion, $\dim \operatorname{im}(d_g\ell_p) = \dim G$. Because $\pi$ is a submersion, $\dim V_{\ell_p(g)} = \dim P - \dim M$; and $\dim M = \dim P - \dim G$ (the fibre $\pi^{-1}(\pi(p)) = p \cdot G$ is the injective-immersed image of $G$, of dimension $\dim G$, and equals the fibre of the submersion, which has dimension $\dim P - \dim M$), so $\dim V_{\ell_p(g)} = \dim G$. A subspace of equal dimension inside the containing space is the whole space, so $\operatorname{im}(d_g\ell_p) = V_{\ell_p(g)}$. $\blacksquare$

> [!note]- Lemma 2: The section-coordinate map is an equivariant diffeomorphism
> **Statement:** Let $G$ act smoothly, freely, and properly on the right on $P$, let $\pi : P \to M = P/G$ be the orbit projection (a submersion, by the [[Thm - Quotient Manifold Theorem for Free Proper Actions|quotient manifold theorem]]), and let $s : U \to P$ be a smooth local section of $\pi$ over an open $U \subseteq M$. Then
> $$\psi_U^{-1} : U \times G \to \pi^{-1}(U), \qquad \psi_U^{-1}(x, g) = s(x) \cdot g,$$
> is a diffeomorphism satisfying $\pi(\psi_U^{-1}(x, g)) = x$ and the equivariance $\psi_U^{-1}(x, g g') = \psi_U^{-1}(x, g) \cdot g'$.
>
> **Hint:** Bijectivity from transitivity and freeness on fibres; diffeomorphism from a dimension count plus injectivity of the derivative, whose $U$-part is a section of $d\pi$ and whose $G$-part is Lemma 1.
>
> **Why needed:** It *is* the principal-bundle chart; the first half of the theorem is immediate from it.
>
> > [!note]- Full proof
> > Write $F := \psi_U^{-1}$ for brevity and $R_g(p) = p \cdot g$. Throughout, the fibre $\pi^{-1}(x)$ over $x \in M$ is the orbit of any of its points, since $M = P/G$ is the orbit space.
> >
> > **Step 0 — the map lands in $\pi^{-1}(U)$ and covers the identity.** For $(x, g) \in U \times G$, $\pi(s(x) \cdot g) = \pi(s(x)) = x$, using that $\pi$ is **constant on orbits** and $\pi \circ s = \operatorname{id}_U$. So $F(x, g) \in \pi^{-1}(x) \subseteq \pi^{-1}(U)$, and $\pi \circ F = \operatorname{pr}_1$.
> >
> > **Step 1 — $F$ is smooth.** $s$ is smooth, the action $P \times G \to P$ is smooth, and $F(x, g) = (s(x)) \cdot g$ is their composite $(x, g) \mapsto (s(x), g) \mapsto s(x) \cdot g$, hence smooth.
> >
> > **Step 2 — $F$ is injective.** Suppose $s(x) \cdot g = s(x') \cdot g'$. Applying $\pi$ and Step 0 gives $x = x'$. Then $s(x) \cdot g = s(x) \cdot g'$, so acting by $g'^{-1}$, $s(x) \cdot (g g'^{-1}) = s(x)$, and **freeness** gives $g g'^{-1} = e$, i.e. $g = g'$. Hence $(x, g) = (x', g')$.
> >
> > **Step 3 — $F$ is surjective onto $\pi^{-1}(U)$.** Let $p \in \pi^{-1}(U)$ and put $x := \pi(p) \in U$. Both $p$ and $s(x)$ lie in the fibre $\pi^{-1}(x)$, which is a single orbit; the action is **transitive** on it, so $p = s(x) \cdot g$ for some $g$, and $g$ is **unique** by freeness (Step 2's argument). Thus $p = F(x, g)$.
> >
> > **Step 4 — the derivative of $F$ is everywhere an isomorphism.** Fix $(x, g) \in U \times G$ and let $q := F(x, g) = s(x) \cdot g$. The tangent space splits as $T_{(x,g)}(U \times G) = T_x U \oplus T_g G$, and $\dim(U \times G) = \dim M + \dim G = (\dim P - \dim G) + \dim G = \dim P = \dim \pi^{-1}(U)$, so it suffices to show $d F_{(x,g)}$ is **injective**.
> >
> > *The $G$-direction.* Restricting $F$ to $\{x\} \times G$ gives $g \mapsto s(x) \cdot g = \ell_{s(x)}(g)$, the orbit map through $s(x)$. By **Lemma 1**, $d_g\ell_{s(x)}$ is injective with image the vertical space $V_q = \ker d\pi_q$. So $dF_{(x,g)}(0 \oplus T_g G) = V_q$.
> >
> > *The $U$-direction.* Restricting $F$ to $U \times \{g\}$ gives $x \mapsto s(x) \cdot g = R_g(s(x))$; its differential is $d(R_g)_{s(x)} \circ ds_x$. Now $\pi \circ R_g \circ s = \pi \circ s = \operatorname{id}_U$ (again $\pi$ constant on orbits and $\pi \circ s = \operatorname{id}$), so differentiating, $d\pi_q \circ \big(d(R_g)_{s(x)} \circ ds_x\big) = \operatorname{id}_{T_xU}$. Hence $d(R_g)_{s(x)} \circ ds_x$ is a **right inverse** of $d\pi_q$: it is injective, and its image $W := \operatorname{im}\big(d(R_g)_{s(x)} \circ ds_x\big)$ satisfies $d\pi_q|_W : W \to T_x U$ an isomorphism, so $W \cap \ker d\pi_q = 0$, i.e. $W \cap V_q = 0$.
> >
> > *Combining.* Take $(u, v) \in T_xU \oplus T_gG$ with $dF_{(x,g)}(u, v) = 0$. Write $dF_{(x,g)}(u, v) = w + \eta$ with $w \in W$ (the $U$-part) and $\eta \in V_q$ (the $G$-part). Applying $d\pi_q$ and using $V_q = \ker d\pi_q$ gives $d\pi_q(w) = 0$; but $d\pi_q|_W$ is injective, so $w = 0$, hence $u = 0$ (the $U$-restriction is injective). Then $\eta = 0$, and injectivity of $d_g\ell_{s(x)}$ gives $v = 0$. So $dF_{(x,g)}$ is injective, and by the dimension count it is an isomorphism.
> >
> > **Step 5 — conclusion.** $F$ is a smooth bijection (Steps 1–3) whose derivative is everywhere an isomorphism (Step 4); by the inverse function theorem $F$ is a local diffeomorphism, and a bijective local diffeomorphism is a diffeomorphism. Finally, **equivariance**: $F(x, g g') = s(x) \cdot (g g') = (s(x) \cdot g) \cdot g' = F(x, g) \cdot g'$ by the action axioms. $\blacksquare$

> [!note]- Lemma 3: Compact groups act properly
> **Statement:** Any smooth action of a compact Lie group $G$ on a manifold $P$ (on either side) is proper.
>
> **Hint:** The preimage of a compact set under $\Theta$ sits inside a compact product.
>
> **Why needed:** It is the "in particular" clause of the first theorem and the first disguised source.
>
> > [!note]- Full proof
> > Consider $\Theta : G \times P \to P \times P$, $\Theta(g, p) = (p \cdot g,\, p)$; properness of the action means $\Theta$ is a proper map. Let $K \subseteq P \times P$ be compact. Then $\operatorname{pr}_2(K) \subseteq P$ is compact (continuous image of a compact set), and
> > $$\Theta^{-1}(K) \subseteq G \times \operatorname{pr}_2(K),$$
> > because if $\Theta(g, p) = (p \cdot g, p) \in K$ then $p = \operatorname{pr}_2(\Theta(g,p)) \in \operatorname{pr}_2(K)$. The right-hand side is a product of the compact group $G$ with the compact set $\operatorname{pr}_2(K)$, hence compact. Moreover $\Theta^{-1}(K)$ is **closed** in $G \times P$ (preimage of the closed set $K$ under the continuous $\Theta$), so it is a closed subset of a compact set, therefore compact. Hence $\Theta$ is proper. $\blacksquare$

> [!note]- Lemma 4: The structure action of a principal bundle is proper
> **Statement:** Let $\pi : P \to M$ be a principal $G$-bundle. Then the defining right $G$-action on $P$ is proper.
>
> **Hint:** Use the sequential criterion. Reduce to a local trivialisation, where the group coordinates $a_i$ and $a_i g_i$ converge, so $g_i$ converges.
>
> **Why needed:** It is the properness the diagonal action of the second theorem inherits.
>
> > [!note]- Full proof
> > We verify the sequential criterion: if $p_i \to p$ and $p_i \cdot g_i \to q$ in $P$, then $(g_i)$ has a convergent subsequence.
> >
> > **The base points agree.** Applying the continuous projection $\pi$ and using $\pi(p_i \cdot g_i) = \pi(p_i)$ (the action is fibre-preserving), we get $\pi(p) = \lim \pi(p_i) = \lim \pi(p_i \cdot g_i) = \pi(q)$. Set $x := \pi(p) = \pi(q)$.
> >
> > **Pass to a trivialisation.** Choose a $G$-equivariant local trivialisation $\psi : \pi^{-1}(U) \to U \times G$ over an open neighbourhood $U$ of $x$ (it exists by the definition of a [[Def - Principal G-Bundle|principal bundle]]). Since $p_i \to p$ and $p_i \cdot g_i \to q$ with $p, q \in \pi^{-1}(U)$ and $\pi^{-1}(U)$ open, for all large $i$ both $p_i$ and $p_i \cdot g_i$ lie in $\pi^{-1}(U)$. Write $\psi(p_i) = (\pi(p_i), a_i)$ and $\psi(p) = (x, a)$; continuity of $\psi$ gives $a_i \to a$ in $G$. Equivariance of $\psi$ (namely $\psi(p' \cdot g) = (\pi(p'), \operatorname{pr}_2\psi(p') \cdot g)$) gives $\psi(p_i \cdot g_i) = (\pi(p_i),\, a_i g_i)$, and continuity together with $p_i \cdot g_i \to q$, $\psi(q) = (x, b)$ gives $a_i g_i \to b$ in $G$.
> >
> > **Solve for $g_i$.** By continuity of multiplication and inversion in the Lie group $G$,
> > $$g_i = a_i^{-1}\,(a_i g_i) \longrightarrow a^{-1} b \qquad \text{(since } a_i \to a \text{ and } a_i g_i \to b \text{)}.$$
> > Thus the whole sequence $(g_i)$ converges, in particular it has a convergent subsequence. Hence the action is proper. $\blacksquare$

> [!note]- Lemma 5: The diagonal action is free and proper
> **Statement:** Let $\pi : P \to M$ be a principal $G$-bundle and $F$ a smooth left $G$-manifold. The **diagonal right action** of $G$ on $P \times F$,
> $$(p, f) \cdot g = (p \cdot g,\; g^{-1} \cdot f),$$
> is a smooth, free, and proper right action.
>
> **Hint:** Freeness needs only freeness on $P$; properness follows from Lemma 4 by discarding the $F$-coordinate in the sequential criterion.
>
> **Why needed:** It is exactly the hypothesis of the first theorem, applied to build the associated total space $E$.
>
> > [!note]- Full proof
> > **It is a right action, and smooth.** The identity acts trivially: $(p, f) \cdot e = (p \cdot e,\, e^{-1} \cdot f) = (p, f)$. For associativity,
> > $$\big((p, f) \cdot g\big) \cdot g' = (p g,\, g^{-1} f) \cdot g' = (p g g',\; g'^{-1} g^{-1} f) = \big(p (g g'),\; (g g')^{-1} f\big) = (p, f) \cdot (g g'),$$
> > using the right-action axiom on $P$, the left-action axiom on $F$ (so $g'^{-1} \cdot (g^{-1} \cdot f) = (g'^{-1} g^{-1}) \cdot f$), and $(g g')^{-1} = g'^{-1} g^{-1}$. Smoothness is clear: each component is a composite of the smooth actions $P \times G \to P$, $G \times F \to F$, and the smooth inversion $g \mapsto g^{-1}$.
> >
> > **It is free.** Suppose $(p, f) \cdot g = (p, f)$. The first coordinate gives $p \cdot g = p$, and the $G$-action on the principal bundle $P$ is **free**, so $g = e$. (The second coordinate then reads $e^{-1} \cdot f = f$, consistently.) Hence the diagonal action is free.
> >
> > **It is proper.** We check the sequential criterion for the diagonal action on $P \times F$. Suppose $(p_i, f_i) \to (p, f)$ and $(p_i, f_i) \cdot g_i = (p_i g_i,\, g_i^{-1} f_i) \to (q, h)$ in $P \times F$. Reading off the first coordinates, $p_i \to p$ and $p_i \cdot g_i \to q$ in $P$. By **Lemma 4**, the $G$-action on $P$ is proper, so its sequential criterion applies and $(g_i)$ has a convergent subsequence. That is precisely the sequential criterion for the diagonal action. Hence it is proper. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> We prove the two theorems in turn.
>
> ---
> **Part I — a free proper action gives a principal $G$-bundle.**
>
> Assume $G$ acts smoothly, freely, and properly on the right on $P$, and set $M := P/G$, $\pi(p) = p \cdot G$.
>
> **Step 0 — the base is a manifold and $\pi$ is a submersion with local sections.** By the [[Thm - Quotient Manifold Theorem for Free Proper Actions|quotient manifold theorem]] — *if a Lie group $G$ acts smoothly, freely, and properly on a manifold $P$, then $M = P/G$ carries a unique smooth structure of dimension $\dim P - \dim G$ making $\pi : P \to M$ a smooth submersion; $M$ is Hausdorff and second countable; and every point of $M$ has a neighbourhood over which $\pi$ has a smooth local section* — the orbit space $M$ is a smooth (Hausdorff, second countable) manifold, $\pi$ is a smooth submersion, and $\pi$ is by construction constant on orbits with each fibre $\pi^{-1}(x)$ equal to a single orbit.
>
> **Step 1 — $(P, \pi, M)$ is a fibre bundle with typical fibre $G$.** Fix $x_0 \in M$. By Step 0 there is an open neighbourhood $U \ni x_0$ and a smooth local section $s : U \to P$, $\pi \circ s = \operatorname{id}_U$. By **Lemma 2**, the map $\psi_U^{-1}(x, g) = s(x) \cdot g$ is a diffeomorphism $U \times G \to \pi^{-1}(U)$ with $\pi \circ \psi_U^{-1} = \operatorname{pr}_1$; its inverse $\psi_U : \pi^{-1}(U) \to U \times G$ is therefore a diffeomorphism satisfying $\operatorname{pr}_1 \circ \psi_U = \pi$, i.e. a local trivialisation over $U$. As $x_0$ was arbitrary, such trivialisations cover $M$, and $\pi$ is a surjective smooth map (every orbit is a point of $M$ with a preimage); hence $(P, \pi, M)$ is a [[Def - Fibre Bundle|fibre bundle]] with typical fibre $G$.
>
> **Step 2 — the four principal-bundle clauses.** We verify the definition of a [[Def - Principal G-Bundle|principal G-bundle]]: a fibre bundle with a fibre-preserving free right $G$-action, transitive on fibres, with $G$-equivariant trivialisations.
> - *Fibre-preserving:* $\pi(p \cdot g) = \pi(p)$ since $p \cdot g$ and $p$ share an orbit, which is a fibre.
> - *Free:* the action is free by hypothesis.
> - *Transitive on fibres:* each fibre $\pi^{-1}(x)$ is a single orbit, on which $G$ acts transitively by definition of an orbit.
> - *Equivariant trivialisations:* the trivialisations of Step 1 satisfy $\psi_U^{-1}(x, g g') = \psi_U^{-1}(x, g) \cdot g'$ by the equivariance in **Lemma 2**; equivalently $\psi_U(p \cdot g') = (\pi(p),\, \operatorname{pr}_2\psi_U(p) \cdot g')$, which is the defining commuting square of a principal bundle.
>
> All four clauses hold, so $(P, \pi, M)$ is a principal $G$-bundle.
>
> **Step 3 — the compact case.** If $G$ is compact and acts smoothly and freely, then by **Lemma 3** the action is proper, so the hypotheses of Steps 0–2 are met and $(P, \pi, M)$ is a principal $G$-bundle. This is Bär's Remark 2.2.3 (the extension of his Theorem 1.5.11), now with the general-$G$ hypothesis in place of compactness.
>
> ---
> **Part II — the associated fibre bundle.**
>
> Let $\pi : P \to M$ be a principal $G$-bundle and $F$ a smooth left $G$-manifold.
>
> **Step 0 — the diagonal action, and the manifold $E$.** By **Lemma 5**, the diagonal right action $(p, f) \cdot g = (p g,\, g^{-1} f)$ on $P \times F$ is smooth, free, and proper. Applying **Part I** (equivalently the [[Thm - Quotient Manifold Theorem for Free Proper Actions|quotient manifold theorem]]) to this action, the quotient $E := (P \times F)/G = P \times_G F$ is a smooth (Hausdorff, second countable) manifold, and the quotient map $\varpi : P \times F \to E$ is a smooth submersion. *This is the point Bär defers to "the general theory of group actions" and states only for compact $G$, and where Haydys writes "properly discontinuous": the correct hypothesis, free and proper, is supplied by Lemma 5, and it holds for every Lie group $G$.*
>
> **Step 1 — the projection $\pi_E$ is well defined and smooth.** The map $\pi \circ \operatorname{pr}_1 : P \times F \to M$, $(p, f) \mapsto \pi(p)$, is smooth and constant on the diagonal orbits, since $\pi(p \cdot g) = \pi(p)$ for a principal bundle. By the universal property of the quotient (clause 4 of the [[Thm - Quotient Manifold Theorem for Free Proper Actions|quotient manifold theorem]]: *a smooth map out of $P \times F$ that is constant on orbits descends uniquely to a smooth map on the quotient*), there is a unique smooth map $\pi_E : E \to M$ with $\pi_E \circ \varpi = \pi \circ \operatorname{pr}_1$, that is $\pi_E([p, f]) = \pi(p)$. It is surjective because $\pi$ is.
>
> **Step 2 — local trivialisations.** Fix $x_0 \in M$. Since $P$ is a principal bundle it has, over some open $U \ni x_0$, a smooth local section $s : U \to P$ with $\pi \circ s = \operatorname{id}_U$ (equivalently the identity element of a local trivialisation, [[Thm - Sections of a Principal Bundle and Triviality|sections correspond to trivialisations]]). Define
> $$\Phi_U^{-1} : U \times F \to \pi_E^{-1}(U), \qquad \Phi_U^{-1}(x, f) = [s(x),\, f].$$
> We show it is a diffeomorphism over $U$.
> - *Into the fibre, smooth:* $\pi_E([s(x), f]) = \pi(s(x)) = x \in U$, so the image lies in $\pi_E^{-1}(U)$; and $\Phi_U^{-1} = \varpi \circ (s \times \operatorname{id}_F)$ is a composite of smooth maps.
> - *Injective:* if $[s(x), f] = [s(x'), f']$, there is $g \in G$ with $(s(x'), f') = (s(x) g,\, g^{-1} f)$. Then $s(x') = s(x) \cdot g$; applying $\pi$ gives $x' = x$, so $s(x) \cdot g = s(x)$, and **freeness** gives $g = e$; hence $f' = g^{-1} f = f$. So $(x, f) = (x', f')$.
> - *Surjective onto $\pi_E^{-1}(U)$:* let $[p, f] \in \pi_E^{-1}(U)$, so $x := \pi(p) \in U$. Then $p$ and $s(x)$ lie in the same fibre (an orbit), so $p = s(x) \cdot g$ for a unique $g$ (**transitivity and freeness** on fibres). Now
> $$[p, f] = [s(x) \cdot g,\, f] = [s(x),\, g \cdot f],$$
> because $(s(x), g \cdot f) \cdot g = (s(x) \cdot g,\; g^{-1}(g \cdot f)) = (s(x) \cdot g,\, f)$ exhibits the two representatives as equivalent. Hence $[p, f] = \Phi_U^{-1}(x,\, g \cdot f)$.
> - *Smooth inverse:* let $\theta := \operatorname{pr}_2 \circ \psi_U : \pi^{-1}(U) \to G$ be the group coordinate of the principal-bundle trivialisation $\psi_U$ associated with $s$, so that $p = s(\pi(p)) \cdot \theta(p)$ for all $p \in \pi^{-1}(U)$; $\theta$ is smooth because $\psi_U$ is. Define
> $$\beta : \pi^{-1}(U) \times F \to U \times F, \qquad \beta(p, f) = \big(\pi(p),\; \theta(p) \cdot f\big),$$
> which is smooth (composite of $\pi$, $\theta$, and the left action). It is constant on the diagonal orbits inside $\pi^{-1}(U) \times F$: for $g \in G$,
> $$\beta(p \cdot g,\, g^{-1} f) = \big(\pi(p g),\; \theta(p g) \cdot (g^{-1} f)\big) = \big(\pi(p),\; (\theta(p) g) \cdot g^{-1} f\big) = \big(\pi(p),\; \theta(p) \cdot f\big) = \beta(p, f),$$
> where $\theta(p g) = \theta(p) g$ follows from $p g = s(\pi(p)) \theta(p) g$ and the uniqueness of the group coordinate, and $\pi(p g) = \pi(p)$. The diagonal action restricts to a free proper action on the open $G$-invariant set $\pi^{-1}(U) \times F$, whose quotient is the open set $\pi_E^{-1}(U) \subseteq E$; by the universal property (clause 4 of the [[Thm - Quotient Manifold Theorem for Free Proper Actions|quotient manifold theorem]], applied to this restricted action), $\beta$ descends to a smooth map $\bar\beta : \pi_E^{-1}(U) \to U \times F$, $\bar\beta([p, f]) = (\pi(p),\, \theta(p) \cdot f)$. Finally $\bar\beta$ is inverse to $\Phi_U^{-1}$:
> $$\bar\beta\big(\Phi_U^{-1}(x, f)\big) = \bar\beta([s(x), f]) = \big(\pi(s(x)),\; \theta(s(x)) \cdot f\big) = (x,\, e \cdot f) = (x, f),$$
> since $\theta(s(x)) = e$ (as $s(x) = s(x) \cdot e$); and
> $$\Phi_U^{-1}\big(\bar\beta([p, f])\big) = \Phi_U^{-1}\big(\pi(p),\, \theta(p) f\big) = [s(\pi(p)),\, \theta(p) f] = [s(\pi(p)) \theta(p),\, f] = [p, f],$$
> using $[s(\pi(p)) \theta(p), f] = [p, f]$ from $p = s(\pi(p)) \theta(p)$. Hence $\Phi_U^{-1}$ is a diffeomorphism with smooth inverse $\Phi_U := \bar\beta$.
>
> **Step 3 — conclusion of Part II.** The trivialisations $\Phi_U$ cover $M$ (as $x_0$ was arbitrary) and satisfy $\operatorname{pr}_1 \circ \Phi_U = \pi_E$, so $(E, \pi_E, M)$ is a [[Def - Fibre Bundle|fibre bundle]] with typical fibre $F$. This is the associated fibre bundle $P \times_G F$. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Homogeneous spaces and the isotropy representation (Lie theory).** Let $G$ be a Lie group and $H$ a closed subgroup. Applying Part I to the free proper right-translation action of $H$ on $G$ shows $G \to G/H$ is a principal $H$-bundle; feeding this bundle through the isotropy representation of $H$ on $\mathfrak{g}/\mathfrak{h}$ in Part II produces the tangent bundle of $G/H$ as an associated bundle $G \times_H (\mathfrak{g}/\mathfrak{h})$. The theorem applies because closedness of $H$ is the disguise for properness; it is non-obvious because the tangent bundle of a quotient is here reconstructed purely group-theoretically, with no reference to charts on $G/H$.

**Configuration spaces in mechanics (geometric mechanics).** A symmetry group $G$ of a mechanical system acts on the configuration manifold $Q$; when the action is free and proper (as for a rigid body with $G = SO(3)$ acting on frames, or a particle in a gauge field), Part I makes $Q \to Q/G$ a principal bundle, and the reduced dynamics live on the base while the fibre records the symmetry. The theorem applies once one checks freeness (no configuration is fixed by a nontrivial symmetry) and properness (automatic for compact $G$ by Lemma 3); it is non-obvious that the bookkeeping of a constrained or reduced system is exactly principal-bundle geometry, which is what makes connections and holonomy the right language for the associated gauge forces.

**Covering spaces as bundles (algebraic topology).** A group $\Gamma$ acting freely and properly discontinuously on a simply connected manifold $\tilde X$ — for instance $\pi_1(X)$ acting on the universal cover — is a discrete free proper action, so Part I presents the covering $\tilde X \to \tilde X/\Gamma = X$ as a principal $\Gamma$-bundle. Associated bundles $\tilde X \times_\Gamma F$ through a $\Gamma$-action on $F$ are then flat fibre bundles, and their sections are $\Gamma$-equivariant maps $\tilde X \to F$. The theorem applies because for a discrete group "properly discontinuous" *is* "proper"; the exercise is non-obvious precisely where it forces one to keep that equivalence straight — the very point of the convention callout on Haydys's phrasing.

---

# Bridges

- **[[Def - Associated Bundle|The associated vector and principal bundles]]** — the second theorem, specialised. Choosing $F = V$ a vector space with a representation $\rho : G \to GL(V)$ gives the associated *vector* bundle $P \times_\rho V$, whose fibrewise linear structure descends because $\rho(g)$ is linear; choosing $F = H$ a Lie group with the action $g \cdot h = \varphi(g) h$ from a homomorphism $\varphi : G \to H$ gives the *extension of structure group* $P \times_\varphi H$, a principal $H$-bundle. Both are the present fibre-bundle construction with extra fibre structure that the diagonal quotient respects; the details are developed in §3.4.

- **[[Def - Frame Bundle of a Vector Bundle|The frame bundle]]** — the converse direction. There the principal $GL(k)$-bundle is built first, by hand, from the bases of a vector bundle; the present theorem gives the general reason such constructions succeed (the free transitive right $GL(k)$-action on frames is proper), and the second half recovers the original vector bundle as $\operatorname{Fr}(E) \times_{\mathrm{std}} \mathbb{R}^k$.

- **[[Thm - Homogeneous Space is a Smooth Manifold|Homogeneous-space bundles]]** — the archetypal instance. For a closed subgroup $H \le G$, right translation of $H$ on $G$ is free (cancellation) and proper (closedness), so $G \to G/H$ is a principal $H$-bundle. The Hopf bundle $SU(2) \to SU(2)/U(1) \cong S^2$ and the frame bundles of symmetric spaces are all this bridge.

- **[[Thm - Sections of a Principal Bundle and Triviality|Sections and triviality]]** — the tool used in Part II Step 2. A principal bundle has local sections exactly where it has local trivialisations, and it is trivial precisely when it has a global section; the local sections of $P$ are what trivialise every associated bundle $P \times_G F$ simultaneously.

- **Symplectic and Riemannian reduction (geometric mechanics).** When the free proper action preserves a Riemannian metric or a symplectic form, the invariant structure descends along the submersion $\pi : P \to P/G$ to the base, producing a Riemannian submersion or the Marsden–Weinstein symplectic quotient. The construction of the quotient manifold is the present theorem; the descent of the tensor is the added invariance-plus-horizontality argument.

---

# Unlocked by This

> [!tip] The gauge group as sections of the adjoint bundle *(from Gauge Theory)*
> Applying the associated-bundle construction to $F = G$ with the *conjugation* action $g \cdot h = g h g^{-1}$ produces the group bundle $\operatorname{Ad} P = P \times_G G$, whose smooth sections form the gauge group; applying it to $F = \mathfrak{g}$ with the adjoint representation produces $\operatorname{ad} P = P \times_G \mathfrak{g}$, the bundle in which connections and curvatures take values. Both rest on the second theorem here. See **Def - Adjoint Bundles ad P and Ad P**.

> [!tip] Connections as equivariant horizontal distributions *(from Gauge Theory)*
> Once $P \to M$ is known to be a principal bundle, the vertical distribution $V = \ker d\pi$ (whose fibres are the images of the orbit maps, by Lemma 1) is intrinsic, and a connection is a $G$-invariant complement to it. The present theorem is what guarantees $V$ is a smooth subbundle of rank $\dim G$ in the first place. See **Def - Connection on a Principal Bundle** (chapter IV).
