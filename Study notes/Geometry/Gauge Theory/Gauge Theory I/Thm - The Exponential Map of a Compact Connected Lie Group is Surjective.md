---
type: theorem
subject: gauge-theory
prereqs:
  - "Thm - One-Parameter Subgroups are the Integral Curves of Left-Invariant Vector Fields"
  - "Thm - Ad is a Smooth Representation and its Differential is ad"
  - "Thm - Fundamental Theorem of Riemannian Geometry (Full Proof)"
  - "Thm - Koszul Formula"
  - "Thm - Existence and Uniqueness of Geodesics"
  - "Thm - The Gauss Lemma"
  - "Def - The Riemannian Exponential Map"
  - "Ex - Compactly Supported Vector Fields are Complete"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $G$ is a [[Def - Lie Group|Lie group]] with identity element $e$, and $\mathfrak{g} = T_eG$ is its [[Def - The Lie Algebra of a Lie Group|Lie algebra]], the tangent space at the identity equipped with the bracket $[\cdot,\cdot]$ of [[Def - Left-Invariant Vector Field|left-invariant vector fields]]; every $X \in \mathfrak{g}$ is identified with the unique left-invariant field $X(g) = d_eL_g(X)$ extending it, where $L_g\colon G \to G$, $L_g(h) = gh$, is left translation. The [[Def - Exponential Map of a Lie Group|exponential map]] $\exp\colon \mathfrak{g} \to G$ sends $X$ to $\gamma_X(1)$, where $\gamma_X$ is the unique one-parameter subgroup with $\dot\gamma_X(0) = X$. The [[Def - Adjoint Representation|adjoint representation]] is $\operatorname{Ad}\colon G \to GL(\mathfrak{g})$, $\operatorname{Ad}_g = d_e\alpha_g$ with $\alpha_g(h) = ghg^{-1}$; for a matrix group $\operatorname{Ad}_g X = gXg^{-1}$, and its differential is $\operatorname{ad}_X Y = [X,Y]$.

A **Riemannian metric** on a manifold $M$ is a smooth choice $g = (g_p)_{p\in M}$ of inner product $g_p$ on each tangent space $T_pM$ (see [[Def - Riemannian Metric]]); we write $\lVert v \rVert_g = g_p(v,v)^{1/2}$ for $v \in T_pM$. The [[Def - Levi-Civita Connection|Levi-Civita connection]] $\nabla$ of $(M,g)$ is the unique torsion-free, metric-compatible connection on $TM$; a [[Def - Geodesic|geodesic]] is a curve with $\nabla_{\dot\gamma}\dot\gamma = 0$; and $\exp^g_p\colon V_p \subseteq T_pM \to M$, $\exp^g_p(v) = \gamma_v(1)$, is the [[Def - The Riemannian Exponential Map|Riemannian exponential map]] at $p$, defined on the star-shaped set $V_p$ of vectors $v$ for which the geodesic $\gamma_v$ with $\dot\gamma_v(0) = v$ reaches parameter $1$. To keep the two exponential maps apart we always decorate the Riemannian one with a superscript, $\exp^g$, and its base point subscript $\exp^g_p$; the bare symbol $\exp\colon \mathfrak{g} \to G$ is always the Lie-group exponential. The Riemannian distance is $d(p,q) = \inf_\gamma L(\gamma)$, the infimum of lengths $L(\gamma) = \int \lVert\dot\gamma\rVert_g\,dt$ over piecewise-smooth curves from $p$ to $q$.

We call a Lie group $G$ **compact** if the underlying manifold is compact, and **connected** if it is connected as a topological space.

> [!warning] Convention: the inner product on $\mathfrak{g}$
> The proof produces a Riemannian metric on $G$ from an inner product on $\mathfrak{g}$; the metric is required to be **bi-invariant** (invariant under both left and right translations), which forces the inner product on $\mathfrak{g}$ to be $\operatorname{Ad}$-invariant: $\langle \operatorname{Ad}_g X, \operatorname{Ad}_g Y\rangle = \langle X, Y\rangle$ for all $g \in G$ and $X, Y \in \mathfrak{g}$. Such an inner product always exists on a compact group (this is Lemma 1). For the concrete groups the reader should keep in mind, the standard $\operatorname{Ad}$-invariant inner product on $\mathfrak{su}(n)$ (anti-Hermitian traceless matrices) is $\langle X, Y\rangle = -\operatorname{tr}(XY)$; it is $\operatorname{Ad}$-invariant because $-\operatorname{tr}(gXg^{-1}\,gYg^{-1}) = -\operatorname{tr}(gXYg^{-1}) = -\operatorname{tr}(XY)$ by cyclicity of the trace, and positive definite because $-\operatorname{tr}(XX) = \operatorname{tr}(X^*X) = \sum_{i,j}|X_{ij}|^2 > 0$ for $X \neq 0$ (using $X^* = -X$).

---

# Statement

> **Theorem (surjectivity of $\exp$ for compact connected groups).** Let $G$ be a compact connected [[Def - Lie Group|Lie group]] with Lie algebra $\mathfrak{g}$. Then the [[Def - Exponential Map of a Lie Group|exponential map]]
> $$\exp\colon \mathfrak{g} \longrightarrow G$$
> is surjective: for every $g \in G$ there is an $X \in \mathfrak{g}$ with $\exp(X) = g$.

This is Remark 1.4.13 of Bär's lecture notes, stated there without proof. The proof we give is the one that runs through Riemannian geometry, following Milnor (*Morse Theory*, §21, Lemmas 21.2–21.3) and do Carmo (*Riemannian Geometry*, Chapter 7, Theorem 2.8); it is assembled here in full from four lemmas, none of which is imported.

---

# Motivation

The exponential map is the bridge between a Lie group and its Lie algebra: it turns the linear, coordinate-friendly object $\mathfrak{g}$ into the curved, global object $G$, and one wants to know how much of $G$ it reaches. Near the identity the answer is settled and easy — $\exp$ is a diffeomorphism from a neighbourhood of $0 \in \mathfrak{g}$ onto a neighbourhood of $e \in G$, because $d_0\exp = \operatorname{id}_{\mathfrak{g}}$ (this is [[Thm - The Exponential Map is a Local Diffeomorphism at the Origin|the local-diffeomorphism theorem]]). The global question is genuinely different, and the answer depends on $G$. For the non-compact group $SL(2;\mathbb{R})$ the exponential map is *not* surjective — the element $\operatorname{diag}(-2,-\tfrac12)$ is not in the image (this is worked out in [[Ex - The Exponential Map of SL(2,R) is Not Surjective]]) — so surjectivity is a real theorem that needs a real hypothesis, and the hypothesis is compactness together with connectedness.

Why should these two hypotheses suffice? Connectedness is plainly necessary: $\exp(\mathfrak{g})$ is a connected subset of $G$ containing $e$ (it is the continuous image of the connected space $\mathfrak{g}$), so it can never meet a component of $G$ other than the identity component. If $\exp$ is to be onto, $G$ must have only one component. Compactness is the substantive hypothesis, and the reason it works is that it lets us install a *bi-invariant* Riemannian metric on $G$. Once that metric is in place, two facts collide productively. First, the group-theoretic exponential and the Riemannian exponential at $e$ become literally the same map: the one-parameter subgroups $t \mapsto \exp(tX)$ are exactly the geodesics through $e$. Second, on a compact manifold every geodesic extends to all time and — crucially — any two points are joined by a *minimizing* geodesic. Feeding the second fact to the first: to hit a target $g$, run the minimizing geodesic from $e$ to $g$; it is a one-parameter subgroup $t \mapsto \exp(tX)$, so its endpoint $g$ is $\exp(X)$.

The theorem therefore has content well beyond its statement. It says that on a compact connected group the two exponential maps of differential geometry — the algebraic $\exp$ and the metric $\exp^g_e$ — coincide, and that the metric one is onto because the group is compact. It is the cleanest possible instance of the principle that curvature-free structure (the group) and metric structure (geodesics) can be made to agree, and it is why, for instance, every element of $SU(n)$, $U(n)$, or $SO(n)$ can be written as a single exponential.

---

# Sources and Targets

**Sources (Input Broadening).** The literal hypothesis is "$G$ compact and connected", but several conditions that do not mention compactness deliver it.

A first disguised source is **a closed subgroup of a compact group that is also connected**. A closed subgroup of a compact Lie group is compact (a closed subset of a compact space), so any connected closed subgroup — $SU(n) \subset U(n)$, a maximal torus $T^k \subset G$, the connected stabilizer of a point under a smooth action of a compact group — inherits surjectivity of its own exponential. The bridge $B \Rightarrow A$ is: closed-in-compact implies compact, and one only has to check connectedness separately. *Example problem:* show that every element of a maximal torus $T^k = (S^1)^k$ of a compact group is a single exponential, by recognising $T^k$ as a compact connected abelian subgroup and reading off $\exp(x_1,\dots,x_k) = (e^{ix_1},\dots,e^{ix_k})$.

A second disguised source is **a group carrying a faithful unitary representation of finite image-closure**, more concretely a matrix group $G \subseteq U(n)$ that is closed and connected. Every such $G$ is compact because $U(n)$ is compact and $G$ is closed in it, so the theorem applies and identifies $G$ with a set of single exponentials of anti-Hermitian matrices. The non-obvious step is to notice that landing inside a unitary group is already a compactness certificate — one does not need to check boundedness and closedness of $G$ in $\operatorname{Mat}(n;\mathbb{C})$ separately, since $U(n)$ supplies both. *Example problem:* deduce that $\exp\colon \mathfrak{so}(n) \to SO(n)$ is onto from $SO(n) \subseteq O(n) \subseteq U(n)$ closed, together with the connectedness of $SO(n)$.

A third disguised source is **a homogeneous space presentation $G/H$ that is itself a group**, when $G$ is compact. If a compact group $G$ acts transitively and the isotropy group $H$ is normal, then $G/H$ is a compact connected group (a continuous image of the connected $G$), so its exponential is onto; and $\exp_{G/H}$ is computed from $\exp_G$ through the projection, because [[Thm - Naturality of the Exponential Map|the exponential map is natural]] under Lie group homomorphisms, $\pi \circ \exp_G = \exp_{G/H} \circ d_e\pi$. The bridge is that quotients of compact connected groups are compact connected. *Example problem:* obtain surjectivity of $\exp$ for $SO(3) = SU(2)/\{\pm 1\}$ from the corresponding statement for the compact connected $SU(2)$ and the naturality square.

**Targets (Output Amplification).** The bare output is "$\exp$ is onto"; combined with other facts it does more.

Combine surjectivity with **the explicit exponential of a matrix group**, $\exp_G(X) = e^X$ for $G \subseteq GL(n;\mathbb{K})$ closed ([[Thm - The Exponential Map of a Matrix Group is the Matrix Exponential|the matrix-exponential theorem]]). The payoff $C + D \Rightarrow E$ is a normal-form statement: every element of a compact connected matrix group is $e^X$ for some $X$ in its Lie algebra, so every element of $SU(n)$ is $e^X$ with $X$ anti-Hermitian and traceless, and every element of $SO(n)$ is $e^A$ with $A$ antisymmetric. The extra ingredient is the identification of the abstract $\exp$ with the series $e^{(\cdot)}$; the payoff is a computable parametrisation of the whole group by its Lie algebra.

Combine surjectivity with **connectedness of the parameter space $\mathfrak{g}$** to obtain a *deformation* statement. Because $\mathfrak{g}$ is a vector space, the straight-line homotopy $s \mapsto \exp(sX)$ contracts any chosen $g = \exp(X)$ to $e$ through the group. The payoff is that every continuous map $f\colon Y \to G$ into a compact connected group is null-homotopic after composing with a contraction of each value to the identity when $Y$ is suitable; concretely, this is the fact used in Chapter VI that $SU(2)$-valued maps can be deformed. The extra ingredient is the convexity of $\mathfrak{g}$; the payoff is a supply of explicit homotopies through the group.

Combine surjectivity with **a conjugacy theorem for maximal tori** to reduce questions about all of $G$ to questions about a single torus. Every element of a compact connected group lies in some maximal torus (a corollary that itself uses this surjectivity), and all maximal tori are conjugate; the payoff $E$ is that class functions, characters, and integrals over $G$ can be computed on one torus with a Weyl-group correction. The extra ingredient is the conjugacy of maximal tori; the payoff is the entire computational apparatus of compact-group representation theory. (This target is recorded for context; it is not developed elsewhere in Chapters I–VI.)

---

# Why Is It True

Forget the four lemmas for a moment and picture the mechanism. On a compact connected group we can measure lengths in a way that is blind to where on the group we are standing and blind to whether we multiply on the left or on the right — a bi-invariant metric. Such a metric has an extraordinary property: its straightest possible curves through the identity, the geodesics, are exactly the algebraic one-parameter subgroups $t \mapsto \exp(tX)$. The reason is a two-line computation with the Koszul formula. Bi-invariance makes the inner products of left-invariant fields constant functions on the group, so all the derivative terms in the Koszul formula vanish; what survives are the three bracket terms, and $\operatorname{Ad}$-invariance of the metric makes two of them cancel against the third, leaving the connection $\nabla_X Y = \tfrac12[X,Y]$ on left-invariant fields. Setting $Y = X$ gives $\nabla_X X = 0$: the integral curves of left-invariant fields, which are the one-parameter subgroups, are geodesics.

Now the compactness does its work through a purely metric fact that has nothing to do with the group. On a compact Riemannian manifold, any two points are joined by a *shortest* path, and a shortest path is a geodesic. So take any $g \in G$; there is a minimizing geodesic from $e$ to $g$. But every geodesic through $e$ is a one-parameter subgroup $t \mapsto \exp(tX)$. The geodesic that reaches $g$ is therefore $t \mapsto \exp(tX)$ for some $X$, and evaluating at its endpoint gives $g = \exp(X)$.

**The one-sentence mechanism: a bi-invariant metric turns one-parameter subgroups into geodesics, and compactness guarantees a geodesic to every target, so every target is a one-parameter-subgroup endpoint, that is, an exponential.**

The failure mode on the non-compact side is now visible too. Without compactness, there may be no minimizing geodesic to a given point — the group can "run off to infinity" — and then the argument produces no $X$. This is exactly what happens for $SL(2;\mathbb{R})$: it carries no bi-invariant *Riemannian* metric at all (its Killing form is indefinite), and the geodesics of any left-invariant metric need not reach every point in the required way, which is why $\exp$ misses $\operatorname{diag}(-2,-\tfrac12)$.

---

# What Makes This Hard

The conceptual leap is that a *group-theoretic* surjectivity statement is proved by *Riemannian* geometry; a reader expecting an algebraic argument will not find one, and the whole difficulty is in seeing that the metric detour is the right idea and then supplying the metric. The single most error-prone step is the construction of the bi-invariant metric: the averaging integral needs a bi-invariant measure on $G$, and the fact that a left-invariant measure is automatically right-invariant is not free — it rests on the observation that the continuous homomorphism $g \mapsto |\det \operatorname{Ad}_g|$ has image a compact subgroup of $(\mathbb{R}_{>0},\times)$, which must be trivial. Miss that, and the "average" is not $\operatorname{Ad}$-invariant and the metric is only left-invariant, which is not enough for $\nabla_X Y = \tfrac12[X,Y]$. The other subtle point is the existence of a *minimizing* geodesic on a compact manifold: local minimization inside a normal ball is the Gauss lemma and is standard, but promoting it to a global minimizer between arbitrary points requires the continuation argument of Lemma 4, whose corner-rounding step (a broken path realising the distance must be an unbroken geodesic) is the part most often waved away.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Put a bi-invariant Riemannian metric on $G$ (possible because $G$ is compact); show its geodesics through $e$ are the one-parameter subgroups $t\mapsto\exp(tX)$ (Koszul plus $\operatorname{Ad}$-invariance); show that on a compact manifold every two points are joined by a minimizing geodesic; then run the minimizing geodesic from $e$ to the target $g$, read it off as some $t\mapsto\exp(tX)$, and evaluate at the endpoint to get $g=\exp(X)$.

**Subgoal decomposition:**

1. **Build a bi-invariant metric.** Produce an $\operatorname{Ad}$-invariant inner product on $\mathfrak{g}$ and left-translate it.
   - *Hint:* Average any inner product over $\operatorname{Ad}(G)$ using a bi-invariant integral; a left-invariant top form is right-invariant because $|\det\operatorname{Ad}_g|\equiv 1$.
   - *Why needed:* Only a bi-invariant metric makes one-parameter subgroups geodesic; compactness is used here and nowhere else in Lemma 1.

2. **Identify geodesics through $e$ with one-parameter subgroups.** Show $\nabla_X Y=\tfrac12[X,Y]$ on left-invariant fields, hence $\nabla_X X=0$.
   - *Hint:* In the Koszul formula the derivative terms vanish (constant inner products) and $\operatorname{Ad}$-invariance collapses the three bracket terms to one.
   - *Why needed:* This is the bridge from algebra ($\exp$) to geometry (geodesics).

3. **Geodesic completeness on a compact manifold.** Show geodesics exist for all time.
   - *Hint:* The geodesic spray is tangent to the compact unit sphere bundle (speed is constant along geodesics), and a vector field on a compact manifold is complete.
   - *Why needed:* The minimizing geodesic of subgoal 4 must be defined up to its endpoint, i.e. for all parameter values.

4. **Existence of a minimizing geodesic.** Show any two points of a compact connected Riemannian manifold are joined by a length-minimizing geodesic.
   - *Hint:* Minimize distance to the target over a small geodesic sphere around the source; the radial geodesic in that direction stays optimal by a closed-connected continuation argument using the Gauss lemma.
   - *Why needed:* Surjectivity needs a geodesic that actually *reaches* $g$ and is a one-parameter subgroup.

5. **Assemble.** Given $g$, take the minimizing geodesic from $e$ to $g$; it is $t\mapsto\exp(tX)$; its endpoint is $\exp(X)=g$.
   - *Hint:* Reparametrise so the geodesic has domain $[0,1]$ with velocity $X$ at $e$.
   - *Why needed:* This is the conclusion.

---

# Lemma Decomposition

> [!note]- Lemma 1: A compact Lie group carries a bi-invariant Riemannian metric
> **Statement:** Let $G$ be a compact Lie group. Then there is an inner product $\langle\cdot,\cdot\rangle$ on $\mathfrak{g} = T_eG$ that is $\operatorname{Ad}$-invariant, meaning $\langle\operatorname{Ad}_gX,\operatorname{Ad}_gY\rangle = \langle X,Y\rangle$ for all $g\in G$, $X,Y\in\mathfrak{g}$; and the left-invariant Riemannian metric $g$ it induces, $g_h(u,v) = \langle d_hL_{h^{-1}}u,\, d_hL_{h^{-1}}v\rangle$ for $u,v\in T_hG$, is bi-invariant: $L_a^*g = g$ and $R_a^*g = g$ for every $a\in G$.
>
> **Hint:** Average an arbitrary inner product over the group using a bi-invariant volume form; the modular function $g\mapsto|\det\operatorname{Ad}_g|$ is trivial because its image is a compact subgroup of $\mathbb{R}_{>0}$.
>
> **Why needed:** Bi-invariance is exactly what Lemma 2 needs to force $\nabla_X Y = \tfrac12[X,Y]$; the construction is the only place compactness enters.
>
> > [!note]- Full proof
> > We must produce the $\operatorname{Ad}$-invariant inner product, then verify that the metric it induces is bi-invariant. We proceed in four steps.
> >
> > **Step 0 — a bi-invariant volume form and a finite integral exist.** Because $G$ is a Lie group it is parallelizable: choosing a basis $e_1,\dots,e_n$ of $\mathfrak{g}$ and left-translating gives a global left-invariant frame, hence $G$ is orientable and admits a nowhere-vanishing left-invariant top form $\mu\in\Omega^n(G)$, defined by fixing $\mu_e = e_1^*\wedge\dots\wedge e_n^*\in\Lambda^n\mathfrak{g}^*$ and setting $\mu_h = (L_{h^{-1}})^*\mu_e$. By construction $L_a^*\mu = \mu$ for all $a\in G$ (left-invariance). Since $G$ is compact and $\mu$ is a smooth nowhere-vanishing top form, it defines a density (a positive Radon measure) $\lvert\mu\rvert$ on $G$; the integral $\int_G f\,\lvert\mu\rvert$ is finite for every continuous $f$, and $V := \int_G \lvert\mu\rvert \in (0,\infty)$. Working with the density rather than the form frees the argument from any choice of orientation, which matters because the right translations below need not preserve one.
> >
> > **Step 1 — the left-invariant volume form is also right-invariant.** Fix $a\in G$ and consider the pulled-back form $R_a^*\mu$. It is again left-invariant, because left and right translations commute ($L_b\circ R_a = R_a\circ L_b$, since $(bg)a = b(ga)$), so $L_b^*(R_a^*\mu) = R_a^*(L_b^*\mu) = R_a^*\mu$. Two left-invariant top forms differ by a constant factor (they agree up to a single scalar at $e$, and left-invariance carries that one scalar to every point), so $R_a^*\mu = c(a)\,\mu$ for a scalar $c(a)\in\mathbb{R}\setminus\{0\}$. We compute $c(a)$ by evaluating both sides at $e$ on a basis $v_1,\dots,v_n$ of $\mathfrak{g} = T_eG$. On the left,
> > $$(R_a^*\mu)_e(v_1,\dots,v_n) = \mu_a\big(d_eR_a\,v_1,\dots,d_eR_a\,v_n\big)\qquad\text{(definition of pull-back, }R_a(e)=a\text{).}$$
> > Using $\mu_a = (L_{a^{-1}})^*\mu_e$, that is $\mu_a(w_1,\dots,w_n) = \mu_e(d_aL_{a^{-1}}w_1,\dots,d_aL_{a^{-1}}w_n)$, this equals $\mu_e\big(d_aL_{a^{-1}}d_eR_a\,v_1,\dots,d_aL_{a^{-1}}d_eR_a\,v_n\big)$. The composite is a differential at $e$: $d_aL_{a^{-1}}\circ d_eR_a = d_e(L_{a^{-1}}\circ R_a)$, and $L_{a^{-1}}\circ R_a(x) = a^{-1}xa = \alpha_{a^{-1}}(x)$, so $d_aL_{a^{-1}}\circ d_eR_a = d_e\alpha_{a^{-1}} = \operatorname{Ad}_{a^{-1}}$. Therefore
> > $$(R_a^*\mu)_e(v_1,\dots,v_n) = \mu_e\big(\operatorname{Ad}_{a^{-1}}v_1,\dots,\operatorname{Ad}_{a^{-1}}v_n\big) = \det(\operatorname{Ad}_{a^{-1}})\,\mu_e(v_1,\dots,v_n),$$
> > the last equality being the transformation law of an alternating $n$-form under the linear map $\operatorname{Ad}_{a^{-1}}$ of the $n$-dimensional space $\mathfrak{g}$. Comparing with $(R_a^*\mu)_e = c(a)\,\mu_e$ gives $c(a) = \det(\operatorname{Ad}_{a^{-1}}) = (\det\operatorname{Ad}_a)^{-1}$, so $|c(a)| = |\det\operatorname{Ad}_a|^{-1}$. Now the map
> > $$\chi\colon G\to\mathbb{R}_{>0},\qquad \chi(a) = |\det\operatorname{Ad}_a|,$$
> > is continuous (because $\operatorname{Ad}$ is smooth, by [[Thm - Ad is a Smooth Representation and its Differential is ad|the theorem that Ad is a smooth representation]], and $\det$ is a polynomial) and a group homomorphism (because $\operatorname{Ad}_{ab} = \operatorname{Ad}_a\operatorname{Ad}_b$ and $\det$ is multiplicative, so $\chi(ab) = |\det(\operatorname{Ad}_a\operatorname{Ad}_b)| = \chi(a)\chi(b)$). Its image $\chi(G)$ is a subgroup of $(\mathbb{R}_{>0},\times)$, and it is compact because $\chi$ is continuous and $G$ is compact. The only compact subgroup of $(\mathbb{R}_{>0},\times)$ is $\{1\}$: any other subgroup contains some $r\neq 1$, and then $\{r^k : k\in\mathbb{Z}\}$ is an unbounded (if $r>1$) or non-closed-at-$0$ (if $r<1$) subset, so the subgroup is not compact. Therefore $\chi\equiv 1$, that is $|\det\operatorname{Ad}_a| = 1$ for all $a$, hence $|c(a)| = 1$ for all $a$. We transfer this to integration through the density $\lvert\mu\rvert$. Integration of a continuous function against a density is invariant under every diffeomorphism $\phi$ of $G$, meaning $\int_G \phi^*(f\,\lvert\mu\rvert) = \int_G f\,\lvert\mu\rvert$; and $R_a^*\lvert\mu\rvert = |c(a)|\,\lvert\mu\rvert = \lvert\mu\rvert$ because $|c(a)| = 1$. Hence, for every continuous $f$ and every $a\in G$,
> > $$\int_G (f\circ R_a)\,\lvert\mu\rvert = \int_G (f\circ R_a)\,R_a^*\lvert\mu\rvert = \int_G R_a^*(f\,\lvert\mu\rvert) = \int_G f\,\lvert\mu\rvert,$$
> > and the identical computation for $L_a$ (with $L_a^*\lvert\mu\rvert = \lvert\mu\rvert$ by left-invariance of $\mu$) gives $\int_G (f\circ L_a)\,\lvert\mu\rvert = \int_G f\,\lvert\mu\rvert$. Thus the measure $\lvert\mu\rvert$ is both left- and right-invariant. (When $G$ is connected — the only case the theorem invokes — one can say more: $c$ is a continuous homomorphism from the connected space $G$ into the discrete group $\{\pm1\}$, so $c\equiv c(e) = 1$ and $\mu$ itself is bi-invariant as a form; we shall not need this sharper statement.)
> >
> > **Step 2 — average an inner product to get an $\operatorname{Ad}$-invariant one.** Choose any inner product $\langle\cdot,\cdot\rangle_0$ on $\mathfrak{g}$ (for instance the one with $e_1,\dots,e_n$ orthonormal). Define
> > $$\langle X,Y\rangle := \frac{1}{V}\int_G \langle\operatorname{Ad}_gX,\ \operatorname{Ad}_gY\rangle_0\ \lvert\mu\rvert(g),\qquad X,Y\in\mathfrak{g}.$$
> > The integrand $g\mapsto\langle\operatorname{Ad}_gX,\operatorname{Ad}_gY\rangle_0$ is continuous (indeed smooth) in $g$ because $\operatorname{Ad}$ is smooth and $\langle\cdot,\cdot\rangle_0$ is a fixed bilinear form, so the integral converges. Bilinearity and symmetry of $\langle\cdot,\cdot\rangle$ are inherited from $\langle\cdot,\cdot\rangle_0$ under the integral. Positive definiteness: for $X\neq 0$, $\langle\operatorname{Ad}_gX,\operatorname{Ad}_gX\rangle_0 > 0$ for every $g$ (because $\operatorname{Ad}_g$ is invertible, so $\operatorname{Ad}_gX\neq 0$), and the integral of a continuous, everywhere-positive function against the positive measure $\lvert\mu\rvert$ is positive; hence $\langle X,X\rangle > 0$. So $\langle\cdot,\cdot\rangle$ is an inner product.
> >
> > It is $\operatorname{Ad}$-invariant: for any $h\in G$,
> > $$\langle\operatorname{Ad}_hX,\operatorname{Ad}_hY\rangle = \frac{1}{V}\int_G\langle\operatorname{Ad}_g\operatorname{Ad}_hX,\ \operatorname{Ad}_g\operatorname{Ad}_hY\rangle_0\,\lvert\mu\rvert(g) = \frac{1}{V}\int_G\langle\operatorname{Ad}_{gh}X,\ \operatorname{Ad}_{gh}Y\rangle_0\,\lvert\mu\rvert(g)$$
> > (using $\operatorname{Ad}_g\operatorname{Ad}_h = \operatorname{Ad}_{gh}$). Writing $\Phi(g') = \langle\operatorname{Ad}_{g'}X,\operatorname{Ad}_{g'}Y\rangle_0$, the integrand is $\Phi\circ R_h$, and right-invariance of the integral from Step 1 gives $\int_G(\Phi\circ R_h)\,\lvert\mu\rvert = \int_G\Phi\,\lvert\mu\rvert$; hence
> > $$= \frac{1}{V}\int_G\langle\operatorname{Ad}_{g}X,\ \operatorname{Ad}_{g}Y\rangle_0\,\lvert\mu\rvert(g) = \langle X,Y\rangle.$$
> > So $\langle\cdot,\cdot\rangle$ is $\operatorname{Ad}$-invariant.
> >
> > **Step 3 — the induced left-invariant metric is bi-invariant.** Define $g$ on $G$ by transporting $\langle\cdot,\cdot\rangle$ to every tangent space by left translation:
> > $$g_h(u,v) := \langle d_hL_{h^{-1}}u,\ d_hL_{h^{-1}}v\rangle,\qquad u,v\in T_hG.$$
> > This is smooth (the map $h\mapsto d_hL_{h^{-1}}$ is smooth, being the differential of the smooth map $(a,h)\mapsto L_{a}(h)$) and left-invariant by construction: for $a\in G$ and $u,v\in T_hG$, using $L_{(ah)^{-1}}\circ L_a = L_{h^{-1}}$ and the chain rule,
> > $$(L_a^*g)_h(u,v) = g_{ah}(d_hL_a u, d_hL_a v) = \langle d_{ah}L_{(ah)^{-1}}d_hL_a u,\ \cdots\rangle = \langle d_hL_{h^{-1}}u,\ d_hL_{h^{-1}}v\rangle = g_h(u,v).$$
> > For right-invariance we use $\operatorname{Ad}$-invariance of $\langle\cdot,\cdot\rangle$. Fix $a\in G$; we compare $g_{ha}(d_hR_a u, d_hR_a v)$ with $g_h(u,v)$. Write $w = d_hL_{h^{-1}}u\in\mathfrak{g}$ and $w' = d_hL_{h^{-1}}v\in\mathfrak{g}$, so that $g_h(u,v) = \langle w,w'\rangle$. Transport $d_hR_au$ back to $\mathfrak{g}$ by $d_{ha}L_{(ha)^{-1}}$: since $L_{(ha)^{-1}}\circ R_a\circ L_h = L_{(ha)^{-1}}R_a L_h$ and, as maps $G\to G$, $L_{(ha)^{-1}}R_aL_h(x) = (ha)^{-1}(hx)a = a^{-1}xa = \alpha_{a^{-1}}(x)$, differentiating at $e$ gives $d_{ha}L_{(ha)^{-1}}\circ d_hR_a\circ d_eL_h = d_e\alpha_{a^{-1}} = \operatorname{Ad}_{a^{-1}}$. Applying this to $w = d_eL_h^{-1}\!\cdot$ — precisely, $d_{ha}L_{(ha)^{-1}}(d_hR_a u) = \operatorname{Ad}_{a^{-1}}w$ and likewise for $v$ — we get
> > $$(R_a^*g)_h(u,v) = g_{ha}(d_hR_au,d_hR_av) = \langle\operatorname{Ad}_{a^{-1}}w,\ \operatorname{Ad}_{a^{-1}}w'\rangle = \langle w,w'\rangle = g_h(u,v),$$
> > where the middle equality is the $\operatorname{Ad}$-invariance of $\langle\cdot,\cdot\rangle$ from Step 2. Hence $R_a^*g = g$ for every $a$, and together with left-invariance $g$ is bi-invariant. $\blacksquare$

> [!note]- Lemma 2: For a bi-invariant metric, geodesics through $e$ are the one-parameter subgroups
> **Statement:** Let $G$ be a Lie group with a bi-invariant Riemannian metric $g$ and Levi-Civita connection $\nabla$. Then for left-invariant vector fields $X,Y\in\mathfrak{g}$,
> $$\nabla_X Y = \tfrac12[X,Y].$$
> Consequently every left-invariant field satisfies $\nabla_X X = 0$, and the geodesic $\gamma$ with $\gamma(0)=e$, $\dot\gamma(0)=X$ is $\gamma(t) = \exp(tX)$; in particular the geodesics through $e$ are exactly the one-parameter subgroups.
>
> **Hint:** In the Koszul formula the three $Xg(Y,Z)$-type derivative terms vanish because inner products of left-invariant fields are constant; $\operatorname{Ad}$-invariance of $g$ makes $\operatorname{ad}_X$ skew, collapsing the bracket terms.
>
> **Why needed:** This is the identification of the algebraic exponential with the Riemannian one; without it the geodesic produced in Lemma 4 would tell us nothing about $\exp$.
>
> > [!note]- Full proof
> > We first record two consequences of bi-invariance, then apply the Koszul formula, then integrate the geodesic equation.
> >
> > **Step 0 — inner products of left-invariant fields are constant, and $\operatorname{ad}_X$ is skew.** Let $X,Y\in\mathfrak{g}$, regarded as left-invariant fields. Left-invariance of $g$ means $g_h(X(h),Y(h)) = g_e(d_hL_{h^{-1}}X(h), d_hL_{h^{-1}}Y(h)) = g_e(X(e),Y(e)) = \langle X,Y\rangle$, a constant independent of $h$ (here we used $d_hL_{h^{-1}}X(h) = X(e)$, the defining property of a left-invariant field). Thus the function $g(X,Y)$ on $G$ is constant, so $Zg(X,Y) = 0$ for every vector field $Z$. Next we show that right-invariance of $g$ forces $\langle\cdot,\cdot\rangle := g_e$ to be $\operatorname{Ad}$-invariant. The computation carried out in Lemma 1, Step 3 used only the definition of a left-invariant metric and never the particular inner product it was built from, so it applies to the given bi-invariant $g$ verbatim: for every $a\in G$ and all $u,v\in T_hG$ it gives $(R_a^*g)_h(u,v) = \langle\operatorname{Ad}_{a^{-1}}w,\operatorname{Ad}_{a^{-1}}w'\rangle$, where $w = d_hL_{h^{-1}}u$ and $w' = d_hL_{h^{-1}}v$, and $g_h(u,v) = \langle w,w'\rangle$. As $u,v$ range over $T_hG$ the vectors $w,w'$ range over all of $\mathfrak{g}$, so right-invariance $R_a^*g = g$ reads $\langle\operatorname{Ad}_{a^{-1}}w,\operatorname{Ad}_{a^{-1}}w'\rangle = \langle w,w'\rangle$ for all $w,w'\in\mathfrak{g}$ and all $a\in G$; replacing $a$ by $a^{-1}$ this is precisely $\operatorname{Ad}$-invariance, $\langle\operatorname{Ad}_aX,\operatorname{Ad}_aY\rangle = \langle X,Y\rangle$. Differentiating the identity $\langle\operatorname{Ad}_{\exp(tX)}Y,\operatorname{Ad}_{\exp(tX)}Z\rangle = \langle Y,Z\rangle$ at $t=0$ and using $\frac{d}{dt}\big|_0\operatorname{Ad}_{\exp(tX)}Y = \operatorname{ad}_XY = [X,Y]$ (this is exactly the identity $d_e\operatorname{Ad} = \operatorname{ad}$ from [[Thm - Ad is a Smooth Representation and its Differential is ad|the theorem that the differential of Ad is ad]]) gives, by the product rule,
> > $$\langle[X,Y],Z\rangle + \langle Y,[X,Z]\rangle = 0,\qquad\text{i.e. } \langle\operatorname{ad}_XY,Z\rangle = -\langle Y,\operatorname{ad}_XZ\rangle.$$
> > So $\operatorname{ad}_X$ is skew-symmetric with respect to $\langle\cdot,\cdot\rangle$ for every $X\in\mathfrak{g}$. Call this the **invariance identity**.
> >
> > **Step 1 — apply the Koszul formula.** By [[Thm - Koszul Formula|the Koszul formula]], for any vector fields $X,Y,Z$ the Levi-Civita connection satisfies
> > $$2g(\nabla_XY,Z) = Xg(Y,Z) + Yg(X,Z) - Zg(X,Y) + g([X,Y],Z) - g([X,Z],Y) - g([Y,Z],X).$$
> > Take $X,Y,Z\in\mathfrak{g}$ left-invariant. By Step 0 the three derivative terms $Xg(Y,Z)$, $Yg(X,Z)$, $Zg(X,Y)$ are each zero (constant functions), leaving
> > $$2g(\nabla_XY,Z) = g([X,Y],Z) - g([X,Z],Y) - g([Y,Z],X).$$
> > Now simplify the last two terms with the invariance identity. First, $g([X,Z],Y) = \langle\operatorname{ad}_XZ,Y\rangle = -\langle Z,\operatorname{ad}_XY\rangle = -\langle Z,[X,Y]\rangle = -g([X,Y],Z)$ (using the invariance identity for $\operatorname{ad}_X$, then symmetry of $g$). Second, $g([Y,Z],X) = \langle\operatorname{ad}_YZ,X\rangle = -\langle Z,\operatorname{ad}_YX\rangle = -\langle Z,[Y,X]\rangle = \langle Z,[X,Y]\rangle = g([X,Y],Z)$ (invariance identity for $\operatorname{ad}_Y$, then antisymmetry $[Y,X]=-[X,Y]$ and symmetry of $g$). Substituting,
> > $$2g(\nabla_XY,Z) = g([X,Y],Z) - \big(-g([X,Y],Z)\big) - g([X,Y],Z) = g([X,Y],Z).$$
> > This holds for every left-invariant $Z$. Since the left-invariant fields span each tangent space $T_hG$ and $g_h$ is nondegenerate, the equation $2g(\nabla_XY,\,\cdot\,) = g([X,Y],\,\cdot\,)$ of one-forms forces $\nabla_XY = \tfrac12[X,Y]$.
> >
> > **Step 2 — one-parameter subgroups are geodesics.** Setting $Y = X$ gives $\nabla_XX = \tfrac12[X,X] = 0$ (the bracket is antisymmetric, so $[X,X]=0$). Let $\gamma(t) = \exp(tX)$. By [[Thm - One-Parameter Subgroups are the Integral Curves of Left-Invariant Vector Fields|the theorem identifying one-parameter subgroups with integral curves of left-invariant fields]], $\gamma$ is the integral curve through $e$ of the left-invariant field $X$, so its velocity is $\dot\gamma(t) = X(\gamma(t))$. Therefore its covariant acceleration is
> > $$\nabla_{\dot\gamma}\dot\gamma = (\nabla_XX)\big|_{\gamma(t)} = 0,$$
> > which is precisely the geodesic equation. Hence $\gamma(t)=\exp(tX)$ is a geodesic with $\gamma(0)=e$ and $\dot\gamma(0)=X$.
> >
> > **Step 3 — every geodesic through $e$ is of this form.** Conversely, let $\sigma$ be any geodesic with $\sigma(0)=e$ and $\dot\sigma(0)=X\in\mathfrak{g}=T_eG$. By [[Thm - Existence and Uniqueness of Geodesics|existence and uniqueness of geodesics]], there is exactly one geodesic with these initial data. By Step 2, $t\mapsto\exp(tX)$ is such a geodesic. Therefore $\sigma(t)=\exp(tX)$ for all $t$ in the common domain. So the geodesics through $e$ are exactly the one-parameter subgroups $t\mapsto\exp(tX)$, $X\in\mathfrak{g}$. $\blacksquare$

> [!note]- Lemma 3: On a compact Riemannian manifold every geodesic is defined for all time
> **Statement:** Let $(M,g)$ be a compact Riemannian manifold. Then every maximal geodesic $\gamma_v$ (with $\dot\gamma_v(0)=v$) is defined on all of $\mathbb{R}$; equivalently, $(M,g)$ is geodesically complete and $\exp^g_p$ is defined on all of $T_pM$ for every $p$.
>
> **Hint:** The geodesic spray on $TM$ is tangent to each sphere bundle $\{\lVert v\rVert = c\}$ because speed is constant along geodesics; the unit sphere bundle is compact, and a vector field on a compact manifold is complete.
>
> **Why needed:** The minimizing geodesic of Lemma 4 must actually reach the target point; this requires geodesics to exist for all parameter values, not just short times.
>
> > [!note]- Full proof
> > We must show the geodesic flow has all of $\mathbb{R}$ as its time domain. The idea is to realise geodesics as integral curves of a single vector field on the (compact) unit sphere bundle.
> >
> > **Step 0 — the geodesic spray.** By [[Thm - Existence and Uniqueness of Geodesics|the existence and uniqueness of geodesics]], geodesics are the projections to $M$ of the integral curves of a smooth vector field $S$ on the tangent bundle $TM$, the **geodesic spray**: in canonical coordinates $(x^i,v^i)$ on $TM$ its integral curve through $(p,v)$ is $t\mapsto(\gamma_v(t),\dot\gamma_v(t))$, where $\gamma_v$ solves the geodesic equation $\ddot\gamma^k + \Gamma^k_{ij}\dot\gamma^i\dot\gamma^j = 0$. Completeness of geodesics is the statement that $S$ is a complete vector field on $TM$.
> >
> > **Step 1 — the speed function is constant along geodesics.** Let $E\colon TM\to\mathbb{R}$, $E(p,v) = g_p(v,v) = \lVert v\rVert_g^2$. Along a geodesic $\gamma_v$ with velocity field $\dot\gamma_v$, metric-compatibility of the Levi-Civita connection gives
> > $$\frac{d}{dt}g\big(\dot\gamma_v,\dot\gamma_v\big) = 2\,g\big(\nabla_{\dot\gamma_v}\dot\gamma_v,\ \dot\gamma_v\big) = 2\,g(0,\dot\gamma_v) = 0,$$
> > using the geodesic equation $\nabla_{\dot\gamma_v}\dot\gamma_v=0$. So $E$ is constant along every integral curve of $S$, that is $S(E)=0$; the flow of $S$ preserves each level set $\Sigma_c = \{(p,v)\in TM : \lVert v\rVert_g = c\}$.
> >
> > **Step 2 — the unit sphere bundle is compact and invariant, and $S$ is tangent to it.** Take $c=1$: the unit sphere bundle $\Sigma_1 = \{(p,v) : \lVert v\rVert_g = 1\}$ is a closed subset of $TM$, and it is compact because $M$ is compact and each fibre $\Sigma_1\cap T_pM$ is a Euclidean unit sphere (compact); concretely $\Sigma_1$ is a closed subset of the unit disc bundle, which is a fibre bundle over the compact $M$ with compact fibre, hence compact. Because $S(E)=0$, the vector $S(p,v)$ is tangent to the level set $\Sigma_1$ at each of its points (it annihilates the defining function $E-1$). So $S$ restricts to a smooth vector field $S|_{\Sigma_1}$ on the compact manifold $\Sigma_1$.
> >
> > **Step 3 — completeness on $\Sigma_1$, then on all of $TM$ by homogeneity.** By [[Ex - Compactly Supported Vector Fields are Complete|the fact that every smooth vector field on a compact manifold is complete]] — its support is automatically compact, so the uniform-time argument applies — the field $S|_{\Sigma_1}$ is complete: every geodesic with $\lVert\dot\gamma(0)\rVert_g = 1$ is defined for all $t\in\mathbb{R}$. Finally, for an arbitrary nonzero $v$, write $v = c\,u$ with $c=\lVert v\rVert_g > 0$ and $\lVert u\rVert_g=1$. By the homogeneity of geodesics (from [[Thm - Existence and Uniqueness of Geodesics|the same theorem]]: $\gamma_{cu}(t)=\gamma_u(ct)$), and since $\gamma_u$ is defined for all $t$, the geodesic $\gamma_v(t)=\gamma_u(ct)$ is defined for all $t\in\mathbb{R}$; the case $v=0$ gives the constant geodesic. Therefore every maximal geodesic has domain $\mathbb{R}$, and $\exp^g_p(v)=\gamma_v(1)$ is defined for every $v\in T_pM$. $\blacksquare$

> [!note]- Lemma 4: On a compact connected Riemannian manifold any two points are joined by a minimizing geodesic
> **Statement:** Let $(M,g)$ be a compact connected Riemannian manifold with Riemannian distance $d$. For any $p,q\in M$ there is a geodesic $\gamma\colon[0,\ell]\to M$, parametrised by arc length, with $\gamma(0)=p$, $\gamma(\ell)=q$, and $L(\gamma)=\ell=d(p,q)$; that is, $\gamma$ is length-minimising.
>
> **Hint:** Minimize $d(\cdot,q)$ over a small geodesic sphere $\Sigma_\delta$ around $p$; the radial geodesic in the minimizing direction reaches $q$, by showing the set $A=\{s : d(\gamma(s),q)=d(p,q)-s\}$ is nonempty, closed, and open-ended (continues), hence all of $[0,d(p,q)]$.
>
> **Why needed:** Surjectivity of $\exp$ needs a geodesic from $e$ that actually reaches the target $g$ and minimizes; local geodesics are not enough.
>
> > [!note]- Full proof
> > Write $r = d(p,q)$. If $p=q$ the constant geodesic works, so assume $r>0$. The distance $d$ is finite because $M$ is connected (any two points are joined by a piecewise-smooth curve, whose length bounds $d$) and it is a genuine metric inducing the manifold topology; on the compact $M$ the distance function is continuous and bounded. We use normal balls, the Gauss lemma, and completeness (Lemma 3), and argue by a connectedness continuation.
> >
> > **Step 0 — normal balls and local minimization.** For each point $x\in M$ the [[Def - The Riemannian Exponential Map|Riemannian exponential]] $\exp^g_x$ is a diffeomorphism from a ball $B(0,\rho(x))\subset T_xM$ onto a normal neighbourhood of $x$, with $\rho(x)>0$; by [[Thm - The Gauss Lemma|the Gauss lemma]] (its length-minimisation corollary), for $0<\tau<\rho(x)$ and a unit vector $u\in T_xM$ the radial geodesic $s\mapsto\exp^g_x(su)$, $s\in[0,\tau]$, is the unique length-minimizing curve from $x$ to $\exp^g_x(\tau u)$, of length exactly $\tau$; consequently the geodesic sphere $\{\exp^g_x(\tau u):\lVert u\rVert=1\}$ is exactly the metric sphere $\{y : d(x,y)=\tau\}$ inside the normal neighbourhood, and $d(x,\exp^g_x(\tau u))=\tau$.
> >
> > **Step 1 — first step off $p$ toward $q$.** Choose $\delta$ with $0<\delta<\min(\rho(p),r)$ and let $\Sigma_\delta=\{\exp^g_p(\delta u):\lVert u\rVert=1\}$ be the geodesic sphere of radius $\delta$ about $p$. It is the diffeomorphic image of the unit sphere in $T_pM$, hence compact. The function $x\mapsto d(x,q)$ is continuous, so it attains a minimum on $\Sigma_\delta$ at some point $x_0=\exp^g_p(\delta u_0)$ with $\lVert u_0\rVert=1$. We claim
> > $$d(p,q)=\delta+d(x_0,q).$$
> > For the inequality $\geq$: any piecewise-smooth curve $c$ from $p$ to $q$ must meet $\Sigma_\delta$, because $q$ lies outside the closed normal ball of radius $\delta$ (as $\delta<r=d(p,q)$, so $d(p,q)>\delta$) while $p$ is its centre, and $c$ is connected; let $c$ first meet $\Sigma_\delta$ at a point $x_1=c(t_1)$. The portion of $c$ from $p$ to $x_1$ lies in the closed normal ball and, by Step 0, has length $\geq d(p,x_1)=\delta$; the portion from $x_1$ to $q$ has length $\geq d(x_1,q)\geq d(x_0,q)$ (minimality of $x_0$ on $\Sigma_\delta$). Hence $L(c)\geq\delta+d(x_0,q)$, and taking the infimum over $c$ gives $d(p,q)\geq\delta+d(x_0,q)$. For the inequality $\leq$: the triangle inequality gives $d(p,q)\leq d(p,x_0)+d(x_0,q)=\delta+d(x_0,q)$. The two together give the claimed equality, and in particular $d(x_0,q)=r-\delta$.
> >
> > **Step 2 — set up the continuation.** Let $\gamma(s)=\exp^g_p(su_0)$ be the unit-speed radial geodesic in the direction $u_0$; by Lemma 3 it is defined for all $s\in\mathbb{R}$, and $\gamma(\delta)=x_0$. Consider
> > $$A=\{s\in[0,r] : d(\gamma(s),q)=r-s\}.$$
> > We show $A=[0,r]$; then $s=r$ gives $d(\gamma(r),q)=0$, so $\gamma(r)=q$, and $\gamma|_{[0,r]}$ is a geodesic of length $r=d(p,q)$ from $p$ to $q$, which is the assertion.
> >
> > **$A$ contains $[0,\delta]$.** For $0\leq s\leq\delta$, on one hand $d(\gamma(s),q)\leq d(\gamma(s),x_0)+d(x_0,q)=(\delta-s)+(r-\delta)=r-s$, using $d(\gamma(s),x_0)=\delta-s$ (the sub-arc of the minimizing radial geodesic from $\gamma(s)$ to $x_0=\gamma(\delta)$, Step 0) and $d(x_0,q)=r-\delta$ (Step 1). On the other hand $d(\gamma(s),q)\geq d(p,q)-d(p,\gamma(s))=r-s$, using the triangle inequality and $d(p,\gamma(s))=s$ (Step 0). Hence $d(\gamma(s),q)=r-s$, so $[0,\delta]\subseteq A$; in particular $A\neq\varnothing$.
> >
> > **$A$ is closed.** The function $s\mapsto d(\gamma(s),q)-(r-s)$ is continuous (composition of the continuous $\gamma$, the continuous $d(\cdot,q)$, and an affine map), and $A$ is the preimage of $\{0\}$ intersected with the closed interval $[0,r]$; hence $A$ is closed in $[0,r]$.
> >
> > **$A$ is "open to the right": if $s_0\in A$ and $s_0<r$ then $s_0+\eta\in A$ for some $\eta>0$.** Let $s_0\in A$ with $s_0<r$ and put $y=\gamma(s_0)$, so $d(y,q)=r-s_0>0$. Repeat Step 1 at $y$: choose $\eta$ with $0<\eta<\min(\rho(y),\,r-s_0)$, let $\Sigma'_\eta$ be the geodesic sphere of radius $\eta$ about $y$, and let $y_0\in\Sigma'_\eta$ minimize $d(\cdot,q)$ over $\Sigma'_\eta$; by the same argument as Step 1,
> > $$d(y,q)=\eta+d(y_0,q),\qquad\text{so}\qquad d(y_0,q)=(r-s_0)-\eta=r-(s_0+\eta).$$
> > We claim $y_0=\gamma(s_0+\eta)$, i.e. the minimizing direction at $y$ continues the geodesic $\gamma$. To see this, estimate $d(p,y_0)$ from below:
> > $$d(p,y_0)\geq d(p,q)-d(y_0,q)=r-\big(r-(s_0+\eta)\big)=s_0+\eta,$$
> > using the triangle inequality and $d(y_0,q)=r-(s_0+\eta)$. On the other hand, the concatenation of $\gamma|_{[0,s_0]}$ (from $p$ to $y$, length $s_0$, since $d(p,y)=s_0$ by $s_0\in A$ combined with $d(p,y)\le s_0$ and $d(p,y)\ge d(p,q)-d(y,q)=r-(r-s_0)=s_0$) and the radial geodesic from $y$ to $y_0$ (length $\eta$) is a piecewise-smooth path from $p$ to $y_0$ of length $s_0+\eta$; therefore $d(p,y_0)\leq s_0+\eta$. Combining, $d(p,y_0)=s_0+\eta$, and this broken path from $p$ to $y_0$ has length equal to the distance $d(p,y_0)$, so it is length-minimizing.
> > **A length-minimizing piecewise-smooth path is an unbroken geodesic (corner-rounding).** A minimizing path is a geodesic on each smooth piece; if it had a genuine corner at $y$, replacing a short arc across the corner by the radial geodesic joining its two endpoints would strictly decrease length (inside a normal ball around $y$, by Step 0 the unique minimizer between two nearby points is the radial geodesic, and a broken path between them is strictly longer), contradicting minimality. Hence the concatenation has no corner at $y$: it is a single smooth geodesic, so its second piece is the analytic continuation of its first, i.e. the radial geodesic from $y$ to $y_0$ is $\gamma|_{[s_0,s_0+\eta]}$, and $y_0=\gamma(s_0+\eta)$. Then $d(\gamma(s_0+\eta),q)=d(y_0,q)=r-(s_0+\eta)$, so $s_0+\eta\in A$.
> >
> > **Conclusion of Step 2.** Let $s^*=\sup A$. Since $A$ is closed, $s^*\in A$. If $s^*<r$, the right-openness just proved gives some $s^*+\eta\in A$ with $\eta>0$, contradicting $s^*=\sup A$. Hence $s^*=r$ and $r\in A$: $d(\gamma(r),q)=0$, so $\gamma(r)=q$. The curve $\gamma|_{[0,r]}$ is a unit-speed geodesic from $p$ to $q$ of length $r=d(p,q)$, hence a minimizing geodesic. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $G$ be a compact connected Lie group with Lie algebra $\mathfrak{g}$, and let $g\in G$ be an arbitrary target element. We must produce $X\in\mathfrak{g}$ with $\exp(X)=g$.
>
> **Step 0 — install a bi-invariant metric.** Since $G$ is compact, by **Lemma 1** there is an $\operatorname{Ad}$-invariant inner product $\langle\cdot,\cdot\rangle$ on $\mathfrak{g}$, and the left-invariant Riemannian metric $g^{\mathrm{met}}$ it induces (written $g^{\mathrm{met}}$ to avoid collision with the target element $g$) is bi-invariant. Equip $G$ with $g^{\mathrm{met}}$; let $\nabla$ be its Levi-Civita connection and $d$ its Riemannian distance. Being a compact manifold with a Riemannian metric, $(G,g^{\mathrm{met}})$ is in particular connected and compact, so both Lemma 3 and Lemma 4 apply to it.
>
> **Step 1 — geodesics through $e$ are one-parameter subgroups.** By **Lemma 2**, applied to the bi-invariant metric $g^{\mathrm{met}}$, the Levi-Civita connection satisfies $\nabla_X Y=\tfrac12[X,Y]$ on left-invariant fields, and the geodesic $\gamma$ with $\gamma(0)=e$ and $\dot\gamma(0)=X\in\mathfrak{g}$ is exactly $\gamma(t)=\exp(tX)$, the one-parameter subgroup generated by $X$. This is the identification of the Lie-group exponential with the Riemannian exponential at $e$: $\exp^{g^{\mathrm{met}}}_e(X)=\gamma(1)=\exp(X)$ for every $X\in\mathfrak{g}$.
>
> **Step 2 — a minimizing geodesic from $e$ to the target.** By **Lemma 4**, applied to the compact connected Riemannian manifold $(G,g^{\mathrm{met}})$ and the two points $e$ and $g$, there is a unit-speed geodesic $\sigma\colon[0,\ell]\to G$ with $\sigma(0)=e$, $\sigma(\ell)=g$, and length $\ell=d(e,g)$. (Lemma 3 guarantees this geodesic is defined for all the parameter values used, so that "reaching $g$ at parameter $\ell$" is meaningful.) Its initial velocity $\dot\sigma(0)=:v$ lies in $T_eG=\mathfrak{g}$ and is a unit vector, $\lVert v\rVert=1$.
>
> **Step 3 — read the geodesic as an exponential and evaluate at the endpoint.** By Step 1, the geodesic through $e$ with initial velocity $v$ is the one-parameter subgroup $t\mapsto\exp(tv)$; by the uniqueness of geodesics with given initial data ([[Thm - Existence and Uniqueness of Geodesics|existence and uniqueness of geodesics]]), $\sigma(t)=\exp(tv)$ for all $t\in[0,\ell]$. Evaluating at the endpoint $t=\ell$,
> $$g=\sigma(\ell)=\exp(\ell v).$$
> Set $X:=\ell v\in\mathfrak{g}$. Then $\exp(X)=g$.
>
> **Conclusion.** For the arbitrary $g\in G$ we produced $X=\ell v\in\mathfrak{g}$ with $\exp(X)=g$; here $\ell=d(e,g)$ is the Riemannian distance to $g$ and $v$ is the unit initial velocity of a minimizing geodesic from $e$ to $g$. Since $g$ was arbitrary, $\exp\colon\mathfrak{g}\to G$ is surjective. $\blacksquare$

The connectedness hypothesis entered implicitly in Step 2: Lemma 4 needs $(G,g^{\mathrm{met}})$ connected to guarantee $d(e,g)<\infty$ and a minimizing geodesic; if $G$ had several components, no geodesic from $e$ could reach a point in another component and the argument would produce nothing there, consistent with the fact that $\exp(\mathfrak{g})$ lies in the identity component.

---

# Cross-Field Exercise Suggestions

**Every rotation is a single exponential of an antisymmetric matrix.** Apply the theorem to $G=SO(n)$, which is compact (closed in the compact $O(n)$) and connected. Conclude that every $R\in SO(n)$ is $R=e^A$ for some antisymmetric $A\in\mathfrak{so}(n)$, using [[Thm - The Exponential Map of a Matrix Group is the Matrix Exponential|the matrix-exponential identification]] $\exp_{SO(n)}(A)=e^A$. The application is non-obvious because for $n\geq 3$ there is no elementary reason a general rotation should have a single "generator"; the theorem supplies one. For $n=3$ this is the Euler-axis-and-angle theorem, $R=e^{\theta\,[\hat n]_\times}$, recovered as a special case.

**Deforming $SU(2)$-valued maps.** In gauge theory one needs to know that a map $f\colon S^3\to SU(2)$ can be deformed within the group. Because $SU(2)$ is compact and connected, every value $f(x)=\exp(X(x))$ for a (locally chosen) $X(x)\in\mathfrak{su}(2)$, and the straight-line homotopy $s\mapsto\exp(sX(x))$ contracts each value to the identity. The theorem applies because it certifies the pointwise existence of the generator $X(x)$; the non-obvious part is that surjectivity of $\exp$ is what licenses the homotopy, and this is exactly the input Chapter VI uses.

**No such statement for the Lorentz group.** Contrast the theorem with the non-compact case by examining the identity component $SO^+(1,3)$ of the Lorentz group, whose exponential is *not* surjective (there are boosts-composed-with-rotations not of the form $e^X$). Here the theorem does *not* apply because $SO^+(1,3)$ is non-compact, and the point of the exercise is to locate exactly where the proof breaks: no bi-invariant Riemannian metric exists, so Lemma 1 fails at the first step. This sharpens the reader's sense that compactness is doing essential work, not decorative work.

---

# Bridges

- **The two exponential maps of a Lie group.** The proof is built on the coincidence, for a bi-invariant metric, of the algebraic exponential $\exp\colon\mathfrak{g}\to G$ (endpoints of one-parameter subgroups) with the Riemannian exponential $\exp^{g}_e\colon T_eG\to G$ (endpoints of geodesics). Lemma 2 constructs this identification by computing the Levi-Civita connection $\nabla_XY=\tfrac12[X,Y]$ from [[Thm - Koszul Formula|the Koszul formula]] and the $\operatorname{Ad}$-invariance of the metric. This bridge is the reason differential-geometric tools (geodesics, completeness, minimization) can be brought to bear on a purely group-theoretic question, and it recurs whenever one studies the geometry of homogeneous spaces $G/H$.

- **Compactness as a source of invariant structure.** Lemma 1 is a template: whenever a compact group acts, one averages an arbitrary structure over the group to produce an invariant one, and the averaging is legitimate because a compact group has a finite bi-invariant integral. The same construction produces invariant inner products (used here), invariant Hermitian forms (the unitarian trick, which makes every representation of a compact group unitary, used in [[Thm - Complex Representations of U(1) and SU(2)|the classification of representations of U(1) and SU(2)]]), and invariant connections. The engine in every case is the triviality of the modular function $g\mapsto|\det\operatorname{Ad}_g|$ on a compact group.

- **From local to global for geodesics.** Lemmas 3 and 4 are the compact-manifold half of the Hopf–Rinow circle of ideas: on a compact Riemannian manifold, geodesics are complete (Lemma 3) and any two points are joined by a minimizing geodesic (Lemma 4). These are exactly the facts one needs from Riemannian geometry to make the geodesic argument reach every point of $G$, and they are proved here directly for the compact case rather than imported from a general Hopf–Rinow theorem, so the chapter needs no metric-completeness machinery beyond normal balls and the Gauss lemma.

- **The non-compact contrast.** The theorem's sharpness is exhibited by [[Ex - The Exponential Map of SL(2,R) is Not Surjective|the failure of surjectivity for SL(2,R)]]. Tracking which lemma fails there — Lemma 1, because $SL(2;\mathbb{R})$ admits no bi-invariant Riemannian metric — is the cleanest way to see that compactness is used essentially and not merely for convenience.

---

# Unlocked by This

> [!tip] Every element of a compact connected group lies in a maximal torus *(from Lie theory)*
> Surjectivity of $\exp$ is the first step toward the maximal-torus theorem: given $g=\exp(X)$, the closure of $\{\exp(tX):t\in\mathbb{R}\}$ is a compact connected abelian subgroup, hence a torus containing $g$. Combined with the conjugacy of maximal tori this reduces the study of conjugacy classes, characters, and integration on $G$ to a single torus with a Weyl-group correction.

> [!tip] Single-exponential normal forms for the classical groups *(from matrix analysis)*
> Applied to $U(n)$, $SU(n)$, $SO(n)$, the theorem gives the normal forms "every unitary is $e^{iH}$ with $H$ Hermitian", "every special unitary is $e^X$ with $X$ anti-Hermitian traceless", and "every rotation is $e^A$ with $A$ antisymmetric", each via [[Thm - The Exponential Map of a Matrix Group is the Matrix Exponential|the matrix-exponential identification]]. These are the parametrisations underlying the exponential coordinates used throughout gauge theory.
