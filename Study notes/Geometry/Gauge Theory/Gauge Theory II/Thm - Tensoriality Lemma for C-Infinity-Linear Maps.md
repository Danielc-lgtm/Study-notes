---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Bundle-Valued Differential Forms"
  - "Thm - Existence of Smooth Bump Functions"
  - "Def - Section of a Vector Bundle"
tags: [geometry, gauge-theory]
---

# Notation

Throughout, $M$ is a smooth manifold (smooth, Hausdorff, second countable; "smooth" means $C^\infty$), and $E \to M$ and $F \to M$ are smooth real or complex [[Def - Vector Bundle|vector bundles]] over $M$, of ranks $k$ and $\ell$ respectively. We write $\Gamma(E)$ for the space of smooth [[Def - Section of a Vector Bundle|sections]] of $E$, and $C^\infty(M)$ for the ring of smooth real (or complex) functions on $M$; $\Gamma(E)$ is a module over $C^\infty(M)$ under the pointwise product $(fs)(m) = f(m)\,s(m)$. Following the series convention, $\Omega^p(M; F) = \Gamma(\Lambda^p T^*M \otimes F)$ denotes the space of smooth $F$-valued differential $p$-forms on $M$, so that $\Omega^0(M; F) = \Gamma(F)$; the full apparatus of bundle-valued forms is on [[Def - Bundle-Valued Differential Forms]]. A subscripted symbol $E_m = \pi^{-1}(m)$ is the fibre of $E$ over $m \in M$, and $\Lambda^p T^*_m M$ is the space of alternating $p$-linear forms on $T_m M$.

The bundle $\operatorname{Hom}(E, F) \to M$ is the vector bundle whose fibre over $m$ is the vector space $\operatorname{Hom}(E_m, F_m)$ of linear maps $E_m \to F_m$; it is one of the [[Def - Operations on Vector Bundles and Pull-Back Bundles|operations on vector bundles]], and $\operatorname{End}(E) = \operatorname{Hom}(E, E)$. There is a natural **contraction** (evaluation) bundle map
$$c : \operatorname{Hom}(E, F) \otimes E \longrightarrow F, \qquad c(\phi \otimes v) = \phi(v),$$
which is fibrewise bilinear and smooth. Combining $c$ with the wedge product on the form part gives, for each $p \ge 0$, a pairing
$$\Omega^p(M; \operatorname{Hom}(E, F)) \times \Gamma(E) \longrightarrow \Omega^p(M; F), \qquad (a, s) \longmapsto a \cdot s,$$
defined as follows. If, over an open set $U$, we write $a = \sum_I \omega_I \otimes \phi_I$ with $\omega_I \in \Omega^p(U)$ scalar $p$-forms and $\phi_I \in \Gamma(\operatorname{Hom}(E, F)|_U)$, then
$$a \cdot s := \sum_I \omega_I \otimes \phi_I(s) \in \Omega^p(U; F).$$
Equivalently and independently of any decomposition, $a \cdot s$ is the $F$-valued $p$-form whose value on vector fields $X_1, \dots, X_p$ is
$$(a \cdot s)(X_1, \dots, X_p) = a(X_1, \dots, X_p)(s) \in \Gamma(F), \qquad \text{i.e. } (a \cdot s)(X_1, \dots, X_p)(m) = a_m\big(X_1(m), \dots, X_p(m)\big)\big(s(m)\big),$$
where $a(X_1, \dots, X_p) \in \Gamma(\operatorname{Hom}(E, F))$ and the outer application is the fibrewise map applied to $s(m) \in E_m$. This second description shows the pairing is well-defined globally and coincides on overlaps with the local formula, because $c$ is a bundle map. It is this operation "$a \cdot s$" that appears in the statement below.

A **local frame** for $E$ over an open set $U \subseteq M$ is a tuple $e = (e_1, \dots, e_k)$ of smooth sections $e_j \in \Gamma(U, E)$ such that $(e_1(m), \dots, e_k(m))$ is a basis of $E_m$ for every $m \in U$; every point has a neighbourhood over which such a frame exists, by local triviality of $E$. We write $e^\ast = (e^1, \dots, e^k)$ for the dual frame of $E^\ast$ over $U$, characterised pointwise by $e^i(e_j) = \delta^i_j$.

> [!warning] Convention: $\Omega^p(F)$ versus $\Omega^p(M; F)$
> Haydys writes $\Omega^p(F)$ for what the series calls $\Omega^p(M; F) = \Gamma(\Lambda^p T^*M \otimes F)$, and states the present result (his Lemma 12, p. 7) only as an existence statement — "there exists $a \in \Omega^p(\operatorname{Hom}(E, F))$ such that $A(s) = a \cdot s$" — with its proof left as an exercise. We adopt the series notation $\Omega^p(M; F)$ throughout, we make the uniqueness of $a$ part of the statement (it is what makes $a \mapsto A$ a bijection and is used implicitly wherever the curvature or torsion form is called *the* form), and we supply the omitted proof in full. Where Haydys's exposition writes a local frame's change matrix into $GL_n(\mathbb{R})$ (his equation (6)), this is a typo for $GL_k(\mathbb{R})$ with $k = \operatorname{rank} E$; we use $k$.

---

# Statement

> **Tensoriality Lemma ($C^\infty(M)$-linear maps are bundle-valued forms).** Let $E \to M$ and $F \to M$ be smooth vector bundles, and let
> $$A : \Gamma(E) \longrightarrow \Omega^p(M; F)$$
> be a map that is $\mathbb{R}$-linear and $C^\infty(M)$-linear, that is,
> $$A(s + s') = A(s) + A(s'), \qquad A(fs) = f\,A(s) \qquad \text{for all } s, s' \in \Gamma(E),\ f \in C^\infty(M).$$
> Then there exists a **unique** $a \in \Omega^p(M; \operatorname{Hom}(E, F))$ such that
> $$A(s) = a \cdot s \qquad \text{for all } s \in \Gamma(E).$$
> Conversely, every $a \in \Omega^p(M; \operatorname{Hom}(E, F))$ defines, by $s \mapsto a \cdot s$, an $\mathbb{R}$-linear and $C^\infty(M)$-linear map $\Gamma(E) \to \Omega^p(M; F)$. The assignment $a \mapsto (s \mapsto a \cdot s)$ is therefore a bijection between $\Omega^p(M; \operatorname{Hom}(E, F))$ and the space of $C^\infty(M)$-linear maps $\Gamma(E) \to \Omega^p(M; F)$.

> **Multilinear form of the lemma.** Let $E_1, \dots, E_r \to M$ and $F \to M$ be smooth vector bundles, and let
> $$A : \Gamma(E_1) \times \cdots \times \Gamma(E_r) \longrightarrow \Omega^p(M; F)$$
> be $\mathbb{R}$-multilinear and $C^\infty(M)$-linear in each argument separately, $A(s_1, \dots, f s_i, \dots, s_r) = f\,A(s_1, \dots, s_i, \dots, s_r)$. Then there is a unique $a \in \Omega^p(M; \operatorname{Hom}(E_1 \otimes \cdots \otimes E_r,\, F))$ with
> $$A(s_1, \dots, s_r) = a \cdot (s_1 \otimes \cdots \otimes s_r) \qquad \text{for all } s_i \in \Gamma(E_i),$$
> where $s_1 \otimes \cdots \otimes s_r \in \Gamma(E_1 \otimes \cdots \otimes E_r)$ is the pointwise tensor product. This is the version applied to the [[Thm - Existence of the Curvature Form|curvature]] operator $(X, Y, s) \mapsto F_\nabla(X, Y)s$ and to the [[Def - Torsion Tensor|torsion]] $(v, w) \mapsto \nabla_v w - \nabla_w v - [v, w]$.

The two statements are tied together by a single mechanism, isolated in the two lemmas of the [Lemma Decomposition](#lemma-decomposition): a $C^\infty(M)$-linear operator cannot move information across space (it is *local*) and cannot see a section beyond its value at a point (it is *pointwise*); once both are established, the representing form $a$ is forced upon us fibre by fibre.

---

# Motivation

A section $s \in \Gamma(E)$ is an infinite-dimensional datum: to know $s$ is to know a vector $s(m) \in E_m$ at every one of the uncountably many points $m \in M$, and generic operators on sections — a covariant derivative, for instance — genuinely need all of this data, because they measure how $s(m)$ changes as $m$ moves. A **tensor**, by contrast, is a finite-dimensional datum at each point: an $F$-valued $p$-form $a$ assigns to each $m$ a single algebraic object $a_m \in \Lambda^p T^*_m M \otimes \operatorname{Hom}(E_m, F_m)$, and to evaluate $a \cdot s$ at $m$ one needs nothing about $s$ except the vector $s(m)$. The tensoriality lemma is the exact statement of *when* an operator on sections is secretly of this second, finite kind — when it is a tensor in disguise — and the answer is disarmingly clean: precisely when it is linear over the functions, not merely over the scalars.

The reason this is the central technical tool of the whole chapter, rather than a formal aside, is that the objects gauge theory cares about — curvature, torsion, the difference of two connections, the second exterior covariant derivative — are all *built out of* covariant derivatives, which are emphatically not tensorial: a connection $\nabla$ satisfies the Leibniz rule $\nabla(fs) = df \otimes s + f\,\nabla s$, and the offending term $df \otimes s$ is exactly the failure of $C^\infty(M)$-linearity. What happens, over and over, is that one assembles a *combination* of covariant derivatives in which the Leibniz terms cancel — a difference of two connections, an antisymmetrised second derivative — and the resulting operator turns out to be $C^\infty(M)$-linear after all. At that instant the tensoriality lemma converts a differential operator into an honest section of a bundle: the curvature becomes a genuine $2$-form $F_\nabla \in \Omega^2(M; \operatorname{End} E)$, the torsion becomes a genuine $2$-form $T \in \Omega^2(M; TM)$, and the difference of two connections becomes an honest $1$-form with endomorphism values, so that the space of connections is an affine space. Without the lemma each of these would be only an operator, and the geometry — evaluating curvature on a pair of tangent vectors at a point, integrating it, comparing it pointwise across a gauge transformation — would have nowhere to live.

There is a second reason to prove this carefully rather than wave at it, as the source does. The lemma is the bundle-valued, $p$-form generalisation of a fact that in the tangent-bundle setting is the classical "tensor characterisation lemma" — a $C^\infty(M)$-multilinear map on vector fields is a tensor field, proved on [[Thm - Tensor Field is C-Infinity Multilinear over C-Infinity Functions|the corresponding differential-geometry page]]. That page handles scalar-valued, covariant tensors on $TM$; the present statement replaces the arguments and the values by sections of arbitrary bundles $E$ and $F$ and lets the output carry $p$ antisymmetric form-slots as well. The heart of the argument is identical — locality and pointwise dependence, both extracted from the existence of bump functions — but the bookkeeping is exactly what one must get right to trust that $F_\nabla$ and $T$ are well-defined, so we write it out in full.

---

# Sources and Targets

**Sources (Input Broadening).** The literal hypothesis is spare: any $\mathbb{R}$- and $C^\infty(M)$-linear map $\Gamma(E) \to \Omega^p(M; F)$. The skill is to recognise a $C^\infty(M)$-linear operator where the problem hands you a differential operator, which happens whenever the non-tensorial (Leibniz) terms cancel.

The first disguised source is **a difference of two Leibniz-rule operators over the same bundle.** If $\nabla$ and $\hat\nabla$ are two [[Def - Connection on a Vector Bundle|connections]] on $E$, neither is $C^\infty(M)$-linear, since each obeys $\nabla(fs) = df \otimes s + f\,\nabla s$. But their difference satisfies
$$(\nabla - \hat\nabla)(fs) = \big(df \otimes s + f\,\nabla s\big) - \big(df \otimes s + f\,\hat\nabla s\big) = f\,(\nabla - \hat\nabla)(s),$$
the two $df \otimes s$ terms cancelling identically; so $\nabla - \hat\nabla$ is $C^\infty(M)$-linear and the lemma produces $a = \nabla - \hat\nabla \in \Omega^1(M; \operatorname{End} E)$. The bridge $B \Rightarrow A$ is: "difference of Leibniz operators $\Rightarrow$ $C^\infty(M)$-linear". *Example problem:* show that on a bundle with two given connections the map $s \mapsto \nabla s - \hat\nabla s$ is multiplication by a fixed endomorphism-valued $1$-form, and compute that form in a local frame as $A(\nabla, e) - A(\hat\nabla, e)$.

The second disguised source is **an iterated Leibniz operator in which the first-order terms cancel by antisymmetry.** The composite $d^\nabla \circ d^\nabla : \Omega^0(M; E) \to \Omega^2(M; E)$ is built from two covariant derivatives, yet applying the Leibniz rule twice to $d^\nabla d^\nabla(fs)$ produces terms in $df$ that cancel in pairs, leaving $d^\nabla d^\nabla(fs) = f\,d^\nabla d^\nabla(s)$. The bridge is: "second exterior covariant derivative $\Rightarrow$ $C^\infty(M)$-linear", and the lemma then yields the curvature. *Example problem:* verify the cancellation $d^\nabla\big(d^\nabla(fs)\big) = d^\nabla\big(df \otimes s + f\,\nabla s\big) = -df \wedge \nabla s + df \wedge \nabla s + f\,d^\nabla\nabla s = f\,d^\nabla d^\nabla s$ line by line, and conclude that $d^\nabla \circ d^\nabla$ is $C^\infty(M)$-linear.

The third disguised source is **an antisymmetrised covariant derivative on the tangent bundle, corrected by the Lie bracket.** For a connection $\nabla$ on $TM$, neither $\nabla_v w$ nor the bracket $[v, w]$ is tensorial in $v$ and $w$ separately, but in the combination $T(v, w) = \nabla_v w - \nabla_w v - [v, w]$ the non-tensorial parts cancel, and a direct computation (carried out in the example problem below) gives $T(f_1 v, f_2 w) = f_1 f_2\, T(v, w)$. The bridge is: "Leibniz derivative minus Lie bracket, antisymmetrised $\Rightarrow$ $C^\infty(M)$-bilinear", feeding the multilinear form of the lemma. *Example problem:* using $\nabla_{fv} w = f \nabla_v w$, $\nabla_v(fw) = (vf) w + f\nabla_v w$, and $[fv, w] = f[v, w] - (wf)v$, verify that every $vf$- and $wf$-term in $T(fv, w)$ and $T(v, fw)$ cancels, so that $T$ is a $\binom{1}{2}$-tensor.

**Targets (Output Amplification).** The bare output is a representing form $a$; combined with a specific cancellation it manufactures the chapter's basic tensors.

Combine the lemma with **the second-derivative cancellation of the Leibniz rule.** Applying it to $d^\nabla \circ d^\nabla$, which the second source shows is $C^\infty(M)$-linear, yields the [[Thm - Existence of the Curvature Form|curvature form]] $F_\nabla \in \Omega^2(M; \operatorname{End} E)$ with $d^\nabla d^\nabla = F_\nabla \wedge \cdot\,$. The payoff $E$ is that curvature is an *object*, not an operator: it can be evaluated on a pair of tangent vectors at a point, restricted, pulled back, and integrated (Chern–Weil theory), none of which makes sense for the differential operator $d^\nabla d^\nabla$ itself.

Combine the lemma with **the antisymmetrised-derivative cancellation on $TM$.** Applying its multilinear form to $(v, w) \mapsto \nabla_v w - \nabla_w v - [v, w]$, shown $C^\infty(M)$-bilinear by the third source, yields the torsion tensor $T \in \Omega^2(M; TM)$ (this is Haydys's Remark following his definition of torsion, our source item R2.3.1). The payoff is that torsion-freeness $T \equiv 0$ becomes a pointwise, chart-independent condition on the connection — the hypothesis under which the Levi-Civita connection is unique.

Combine the lemma with **the difference-of-connections cancellation.** Applying it to $\nabla - \hat\nabla$, shown $C^\infty(M)$-linear by the first source, yields an endomorphism-valued $1$-form, which is precisely part (b) of [[Thm - The Space of Connections is an Affine Space|the theorem that the space of connections is an affine space]] modelled on $\Omega^1(M; \operatorname{End} E)$. The payoff is that the set of all connections, a priori an unstructured collection of operators, acquires the geometry of an affine space, on which the gauge group acts and over which one does variational calculus (Yang–Mills).

---

# Why Is It True

Strip away the form-slots and the bundle $F$ for a moment and ask the plainest version: why should an operator $A$ that is linear over functions depend on a section $s$ only through its pointwise values? The answer is that the functions $C^\infty(M)$ are rich enough to *localise*, and localisation is exactly what pointwise dependence means.

Here is the mechanism. Because $M$ carries [[Thm - Existence of Smooth Bump Functions|smooth bump functions]] — for any point $m$ and neighbourhood $U$ there is a smooth $\chi$ equal to $1$ near $m$ and vanishing outside $U$ — the ring $C^\infty(M)$ can single out a point. Suppose a section $s$ vanishes on an open set $U$. Pick any $m \in U$ and a bump function $\chi$ with $\chi(m) = 1$ and support inside $U$. Then $\chi s$ is the zero section (it is zero on $U$ because $s$ is, and zero outside $U$ because $\chi$ is), so by $C^\infty(M)$-linearity $0 = A(\chi s) = \chi\,A(s)$, and evaluating at $m$ gives $A(s)(m) = \chi(m) A(s)(m) = 0$. The operator cannot produce output where its input is silent: **$C^\infty(M)$-linearity forces locality, because multiplying the input by a function that kills it near $m$ multiplies the output by the same function, and the function is $1$ at $m$.** From locality to pointwise dependence is one more step of the same kind: near $m$ write $s = \sum_j \sigma_j e_j$ in a frame; if $s(m) = 0$ then every coefficient $\sigma_j(m) = 0$, and pulling each coefficient out through $C^\infty(M)$-linearity leaves $A(s)(m) = \sum_j \sigma_j(m)\,A(e_j)(m) = 0$.

Once $A(s)(m)$ depends only on the vector $s(m) \in E_m$, the representing tensor writes itself: define $a_m$ on the fibre by "feed $a_m$ the vector $v$, and it returns $A(s)(m)$ for any section $s$ with $s(m) = v$". Well-definedness is exactly pointwise dependence; linearity of $a_m$ in $v$ is inherited from $\mathbb{R}$-linearity of $A$; and smoothness of the assembled $a$ is read off in a frame, where its "matrix entries" are the smooth forms $A(e_j)$. The lemma is therefore not a construction one must be clever to find — like the isomorphism $G/\ker\varphi \cong \operatorname{im}\varphi$ of [[Thm - First Isomorphism Theorem|the first isomorphism theorem]], the representing form is the only thing $A$ could possibly be once its redundancy (dependence on more than the pointwise value) is shown to be zero.

---

# What Makes This Hard

The single non-obvious move is realising that the entire content sits in the two words *local* and *pointwise*, and that both are consequences of one external fact — the existence of bump functions — rather than of any property of $A$ beyond $C^\infty(M)$-linearity. The most common error is to attempt to define $a_m(v) := A(s)(m)$ directly and forget that this needs a *proof* that the answer is independent of the choice of section $s$ extending $v$; that independence is precisely the pointwise-dependence lemma, and skipping it (as the source's "left as an exercise" invites) leaves the central object $a$ merely a relation, not a function. A second, subtler trap is the passage from "$A$ is defined on global sections $\Gamma(E)$" to "we may compute $A(s)(m)$ from a *local* frame near $m$": the frame sections $e_j$ need not extend to global sections, so one must multiply by a bump function to bring them into the domain of $A$, and then argue by locality that the truncation does not disturb the value at $m$. Handling this globalisation cleanly is the only real work in the proof.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Show that $A$ is *local* (an input vanishing on an open set gives an output vanishing there), then that it is *pointwise* (an input vanishing at a point gives an output vanishing there). Pointwise dependence lets you define, fibre by fibre, a linear map $a_m$ by feeding it $s(m)$; check it is well-defined and linear, assemble the $a_m$ into a rough section $a$ of $\Lambda^p T^*M \otimes \operatorname{Hom}(E, F)$, prove $a$ is smooth by computing its frame components as the smooth forms $A(e_j)$, and verify $A(s) = a \cdot s$ and uniqueness. Both locality and pointwise dependence come from multiplying by a bump function.

**Subgoal decomposition:**

1. **Locality.** If $s|_U = 0$ for an open $U$, then $A(s)|_U = 0$.
   - *Hint:* For $m \in U$ take a bump function $\chi$ with $\chi(m) = 1$ and $\operatorname{supp}\chi \subseteq U$; then $\chi s \equiv 0$, so $\chi\,A(s) = A(\chi s) = 0$; evaluate at $m$.
   - *Why needed:* It licenses computing $A(s)(m)$ from the germ of $s$ at $m$, hence from a local frame after a bump-function truncation.

2. **Every fibre vector extends to a global section.** For $m \in M$ and $v \in E_m$ there is $s \in \Gamma(E)$ with $s(m) = v$.
   - *Hint:* Pick a local frame $(e_j)$ near $m$, write $v = \sum_j v^j e_j(m)$, and set $s = \chi \sum_j v^j e_j$ with $\chi$ a bump function equal to $1$ near $m$, extended by zero.
   - *Why needed:* Without it the fibrewise definition $a_m(v) := A(s)(m)$ has no section $s$ to use.

3. **Pointwise dependence.** If $s(m) = 0$ then $A(s)(m) = 0$; consequently $A(s)(m)$ depends only on $s(m)$.
   - *Hint:* Write $s = \sum_j \sigma_j e_j$ near $m$ with $\sigma_j(m) = 0$, truncate to a global identity $\chi^2 s = \sum_j (\chi\sigma_j)(\chi e_j)$, apply $C^\infty(M)$- and $\mathbb{R}$-linearity, and use locality to replace $\chi^2 s$ by $s$ at $m$.
   - *Why needed:* It is the well-definedness of $a_m$.

4. **Define and assemble $a$.** For $v \in E_m$ set $a_m(v) := A(s)(m)$ for any $s$ with $s(m) = v$; check $a_m$ is well-defined (subgoal 3) and linear (from $\mathbb{R}$-linearity of $A$), so $a_m \in \Lambda^p T^*_m M \otimes \operatorname{Hom}(E_m, F_m)$.
   - *Hint:* Linearity: if $s(m) = v$, $t(m) = w$, then $(\lambda s + \mu t)(m) = \lambda v + \mu w$ and $A(\lambda s + \mu t) = \lambda A(s) + \mu A(t)$.
   - *Why needed:* This is the candidate representing form.

5. **Smoothness of $a$ and $A(s) = a \cdot s$.** In a frame $(e_j)$ show $a \cdot e_j = A(e_j)$, so $a = \sum_j A(e_j) \otimes e^j$ is smooth; then $a \cdot s = A(s)$ for all $s$ by expanding $s$ in the frame and using $C^\infty(M)$-linearity. Prove uniqueness.
   - *Hint:* If $a, a'$ both represent $A$ then $(a - a')_m$ kills every $v = s(m)$, so it is zero.
   - *Why needed:* It upgrades the set-theoretic section to a genuine element of $\Omega^p(M; \operatorname{Hom}(E, F))$ and closes existence and uniqueness.

---

# Lemma Decomposition

> [!note]- Lemma 1: Locality of $C^\infty(M)$-linear operators
> **Statement:** Let $A : \Gamma(E) \to \Omega^p(M; F)$ be $\mathbb{R}$- and $C^\infty(M)$-linear. If a section $s \in \Gamma(E)$ vanishes on an open set $U \subseteq M$, then $A(s)$ vanishes on $U$. Consequently, if two sections $s, s'$ agree on $U$, then $A(s)$ and $A(s')$ agree on $U$.
>
> **Hint:** Multiply $s$ by a bump function supported in $U$ and equal to $1$ at the chosen point.
>
> **Why needed:** It says $A$ does not transport information: the value $A(s)(m)$ is determined by $s$ near $m$. This is what allows local frames (which need not extend globally) to be used to compute $A(s)(m)$, after truncating them with a bump function.
>
> > [!note]- Full proof
> > **What is assumed and what is shown.** We assume $s|_U = 0$ and show $A(s)(m) = 0$ for every $m \in U$; since $m \in U$ is arbitrary this gives $A(s)|_U = 0$.
> >
> > **Fix a point and a bump function.** Let $m \in U$. By the [[Thm - Existence of Smooth Bump Functions|existence of smooth bump functions]] — for the closed set $\{m\}$ and the open set $U \supseteq \{m\}$ there is a smooth $\chi : M \to [0, 1]$ with $\chi \equiv 1$ on a neighbourhood of $m$ and $\operatorname{supp}(\chi) \subseteq U$ — choose such a $\chi$; in particular $\chi(m) = 1$.
> >
> > **The truncated section is globally zero.** Consider $\chi s \in \Gamma(E)$. At a point $q \in U$ we have $s(q) = 0$ (by the hypothesis $s|_U = 0$), so $(\chi s)(q) = \chi(q)\,s(q) = 0$. At a point $q \notin U$ we have $\chi(q) = 0$ (since $\operatorname{supp}(\chi) \subseteq U$), so $(\chi s)(q) = 0$. As $M = U \cup (M \setminus U)$, the section $\chi s$ vanishes at every point of $M$; that is, $\chi s = 0$ in $\Gamma(E)$.
> >
> > **Apply $C^\infty(M)$-linearity and evaluate.** Because $A$ is $C^\infty(M)$-linear and $\chi \in C^\infty(M)$,
> > $$0 = A(0) = A(\chi s) = \chi\,A(s) \qquad \text{(} \mathbb{R}\text{-linearity gives } A(0) = 0; \ C^\infty(M)\text{-linearity gives } A(\chi s) = \chi A(s)\text{)}.$$
> > Here $\chi A(s) \in \Omega^p(M; F)$ is the pointwise product of the function $\chi$ with the $F$-valued $p$-form $A(s)$. Evaluating this identity of $p$-forms at $m$,
> > $$0 = \big(\chi\,A(s)\big)(m) = \chi(m)\,A(s)(m) = 1 \cdot A(s)(m) = A(s)(m) \qquad \text{(since } \chi(m) = 1\text{)}.$$
> > Therefore $A(s)(m) = 0$. As $m \in U$ was arbitrary, $A(s)|_U = 0$.
> >
> > **The "agree" consequence.** If $s|_U = s'|_U$, then $(s - s')|_U = 0$, so by the case just proved $A(s - s')|_U = 0$; by $\mathbb{R}$-linearity $A(s - s') = A(s) - A(s')$, whence $A(s)|_U = A(s')|_U$. $\blacksquare$

> [!note]- Lemma 2: Every fibre vector is the value of a global section
> **Statement:** For every $m \in M$ and every $v \in E_m$ there exists $s \in \Gamma(E)$ with $s(m) = v$. More generally, a local frame $(e_1, \dots, e_k)$ over a neighbourhood of $m$ can be replaced by global sections $(\tilde e_1, \dots, \tilde e_k)$ agreeing with it near $m$.
>
> **Hint:** Cut off a frame with a bump function and extend by zero.
>
> **Why needed:** The representing map $a_m$ is defined by evaluating $A$ on a section extending $v$; this lemma guarantees such a section exists, and the frame version supplies the smooth sections whose images $A(\tilde e_j)$ are the components of $a$.
>
> > [!note]- Full proof
> > **What is shown.** Given $m$ and $v \in E_m$, we construct $s \in \Gamma(E)$ with $s(m) = v$.
> >
> > **Choose a frame and expand $v$.** By local triviality of $E$, there is an open neighbourhood $U$ of $m$ and a smooth local frame $(e_1, \dots, e_k)$ for $E$ over $U$ ($k = \operatorname{rank} E$); the vectors $(e_1(m), \dots, e_k(m))$ form a basis of $E_m$, so there are unique scalars $v^1, \dots, v^k$ with $v = \sum_{j=1}^k v^j\, e_j(m)$.
> >
> > **Truncate to a global section.** By the [[Thm - Existence of Smooth Bump Functions|existence of smooth bump functions]], choose $\chi : M \to [0, 1]$ smooth with $\chi \equiv 1$ on a neighbourhood $W \subseteq U$ of $m$ and $\operatorname{supp}(\chi) \subseteq U$. Define
> > $$s := \chi \sum_{j=1}^k v^j\, e_j \quad \text{on } U, \qquad s := 0 \quad \text{on } M \setminus \operatorname{supp}(\chi).$$
> > These two definitions agree on the overlap $U \setminus \operatorname{supp}(\chi)$, where both give $0$, and $U \cup (M \setminus \operatorname{supp}(\chi)) = M$; each piece is smooth, so $s \in \Gamma(E)$.
> >
> > **Check the value.** Since $m \in W$ and $\chi \equiv 1$ on $W$, at $m$ we have $s(m) = 1 \cdot \sum_j v^j e_j(m) = v$.
> >
> > **Frame version.** Applying the construction to each basis section, set $\tilde e_j := \chi\, e_j$ (extended by zero); each $\tilde e_j \in \Gamma(E)$, and on $W$ we have $\tilde e_j = e_j$, so the global sections $(\tilde e_j)$ agree with the local frame near $m$. $\blacksquare$

> [!note]- Lemma 3: Pointwise dependence
> **Statement:** Let $A : \Gamma(E) \to \Omega^p(M; F)$ be $\mathbb{R}$- and $C^\infty(M)$-linear, and let $m \in M$. If $s \in \Gamma(E)$ satisfies $s(m) = 0$, then $A(s)(m) = 0$. Consequently, if $s(m) = s'(m)$ then $A(s)(m) = A(s')(m)$: the $p$-covector $A(s)(m) \in \Lambda^p T^*_m M \otimes F_m$ depends on $s$ only through the vector $s(m) \in E_m$.
>
> **Hint:** Expand $s$ in a local frame, note the coefficients vanish at $m$, and pull them out of $A$ after a bump-function truncation.
>
> **Why needed:** This is precisely the well-definedness of the fibrewise map $a_m(v) := A(s)(m)$; without it $a$ is not a function.
>
> > [!note]- Full proof
> > **What is assumed and what is shown.** We assume $s(m) = 0$ and show $A(s)(m) = 0$.
> >
> > **Expand $s$ in a frame near $m$.** By local triviality choose a smooth local frame $(e_1, \dots, e_k)$ for $E$ over an open neighbourhood $U$ of $m$. By [[Thm - Local Frames Span Sections|the theorem that local frames span sections]] — a smooth local section is uniquely $\tau = \sum_j f^j \sigma_j$ in a frame $(\sigma_j)$ with smooth coefficients $f^j$ — write $s|_U = \sum_{j=1}^k \sigma_j\, e_j$ with $\sigma_j \in C^\infty(U)$. Since $(e_j(m))$ is a basis and $s(m) = \sum_j \sigma_j(m)\,e_j(m) = 0$, linear independence forces
> > $$\sigma_j(m) = 0 \qquad (j = 1, \dots, k).$$
> >
> > **Truncate the frame and coefficients to global data.** By the [[Thm - Existence of Smooth Bump Functions|existence of smooth bump functions]] choose $\chi : M \to [0, 1]$ with $\chi \equiv 1$ on a neighbourhood $W \subseteq U$ of $m$ and $\operatorname{supp}(\chi) \subseteq U$. Set
> > $$\tilde\sigma_j := \chi\,\sigma_j \in C^\infty(M), \qquad \tilde e_j := \chi\, e_j \in \Gamma(E),$$
> > each extended by zero outside $U$; these are smooth and global by the truncation argument of Lemma 2. Consider the global section $\chi^2 s \in \Gamma(E)$. On $U$,
> > $$\chi^2 s = \chi^2 \sum_j \sigma_j e_j = \sum_j (\chi\sigma_j)(\chi e_j) = \sum_{j=1}^k \tilde\sigma_j\, \tilde e_j,$$
> > and off $\operatorname{supp}(\chi)$ both sides vanish, so this identity holds on all of $M$: $\ \chi^2 s = \sum_j \tilde\sigma_j\, \tilde e_j$ in $\Gamma(E)$.
> >
> > **Apply linearity and evaluate.** Using $\mathbb{R}$-linearity to split the sum and $C^\infty(M)$-linearity to pull out each $\tilde\sigma_j \in C^\infty(M)$,
> > $$A(\chi^2 s) = A\Big(\sum_j \tilde\sigma_j\, \tilde e_j\Big) = \sum_{j=1}^k \tilde\sigma_j\, A(\tilde e_j) \qquad \text{(} \mathbb{R}\text{-linearity, then } A(\tilde\sigma_j \tilde e_j) = \tilde\sigma_j A(\tilde e_j)\text{).}$$
> > Evaluate at $m$. On the right, $\tilde\sigma_j(m) = \chi(m)\sigma_j(m) = 1 \cdot 0 = 0$ for every $j$, so the right-hand side vanishes at $m$:
> > $$A(\chi^2 s)(m) = \sum_{j=1}^k \tilde\sigma_j(m)\, A(\tilde e_j)(m) = 0.$$
> > On the left, $\chi \equiv 1$ on the neighbourhood $W$ of $m$, so $\chi^2 s = s$ on $W$; by the "agree" consequence of Lemma 1 (locality), $A(\chi^2 s)$ and $A(s)$ agree on $W$, hence at $m$:
> > $$A(s)(m) = A(\chi^2 s)(m) = 0.$$
> >
> > **The dependence consequence.** If $s(m) = s'(m)$, then $(s - s')(m) = 0$, so by the case just proved $A(s - s')(m) = 0$; by $\mathbb{R}$-linearity $A(s - s') = A(s) - A(s')$, whence $A(s)(m) = A(s')(m)$. Thus $A(s)(m)$ is a function of $s(m)$ alone. $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Let $A : \Gamma(E) \to \Omega^p(M; F)$ be $\mathbb{R}$-linear and $C^\infty(M)$-linear. We construct a unique $a \in \Omega^p(M; \operatorname{Hom}(E, F))$ with $A(s) = a \cdot s$, then prove the converse and the multilinear form.
>
> **Step 0 — the pairing $a \cdot s$ is defined and $C^\infty(M)$-linear in $s$.** For $a \in \Omega^p(M; \operatorname{Hom}(E, F))$ the operation $a \cdot s$ of the Notation section is the composite of the contraction $c : \operatorname{Hom}(E, F) \otimes E \to F$ with the wedge on the form part; on values, $(a \cdot s)(X_1, \dots, X_p)(m) = a_m(X_1(m), \dots, X_p(m))(s(m))$. Since $c$ is fibrewise bilinear, $a \cdot (fs) = f\,(a \cdot s)$ and $a \cdot (s + s') = a \cdot s + a \cdot s'$ for $f \in C^\infty(M)$; so $s \mapsto a \cdot s$ is $\mathbb{R}$- and $C^\infty(M)$-linear. This is the target format, and the converse claim of the theorem is exactly this observation; the substance is that *every* such $A$ arises this way.
>
> **Step 1 — define the fibrewise map $a_m$.** Fix $m \in M$. For $v \in E_m$, choose (Lemma 2) a section $s \in \Gamma(E)$ with $s(m) = v$, and set
> $$a_m(v) := A(s)(m) \in \Lambda^p T^*_m M \otimes F_m.$$
> **This is well-defined:** if $s'$ is another section with $s'(m) = v$, then $s(m) = s'(m)$, so by Lemma 3 (pointwise dependence) $A(s)(m) = A(s')(m)$; the value $a_m(v)$ does not depend on the chosen $s$.
>
> **Step 2 — $a_m$ is linear.** Let $v, w \in E_m$ and $\lambda, \mu$ scalars, with sections $s, t$ chosen so that $s(m) = v$, $t(m) = w$. Then $\lambda s + \mu t \in \Gamma(E)$ satisfies $(\lambda s + \mu t)(m) = \lambda v + \mu w$, so by the definition of $a_m$ and the $\mathbb{R}$-linearity of $A$,
> $$a_m(\lambda v + \mu w) = A(\lambda s + \mu t)(m) = \big(\lambda A(s) + \mu A(t)\big)(m) = \lambda\,A(s)(m) + \mu\,A(t)(m) = \lambda\, a_m(v) + \mu\, a_m(w).$$
> Hence $a_m$ is a linear map $E_m \to \Lambda^p T^*_m M \otimes F_m$, that is,
> $$a_m \in \operatorname{Hom}\big(E_m,\ \Lambda^p T^*_m M \otimes F_m\big) = \Lambda^p T^*_m M \otimes \operatorname{Hom}(E_m, F_m),$$
> the identification being the canonical one for finite-dimensional spaces (pulling the fixed factor $\Lambda^p T^*_m M$ out of the Hom, as $\operatorname{Hom}(E_m, W \otimes F_m) \cong W \otimes \operatorname{Hom}(E_m, F_m)$ for $W = \Lambda^p T^*_m M$). Collecting the $a_m$ over $m \in M$ gives a (so far only set-theoretic) section $a = (a_m)_{m \in M}$ of $\Lambda^p T^*M \otimes \operatorname{Hom}(E, F)$.
>
> **Step 3 — $a$ acts as $A$, in a frame.** Let $(e_1, \dots, e_k)$ be a smooth local frame for $E$ over an open $U$, with dual frame $(e^1, \dots, e^k)$ for $E^*$. Fix $j$ and $m \in U$. Truncating $e_j$ to a global section $\tilde e_j = \chi e_j$ agreeing with $e_j$ near $m$ (Lemma 2), we have, by the definition of $a_m$ applied to $v = e_j(m) = \tilde e_j(m)$ and then locality (Lemma 1, since $\tilde e_j = e_j$ near $m$),
> $$a_m\big(e_j(m)\big) = A(\tilde e_j)(m) = A(e_j)\big|_{\text{near } m}(m) =: A(e_j)(m),$$
> where the last symbol denotes the value at $m$ of the $F$-valued $p$-form $A(\cdot)$ evaluated on the local section $e_j$ — well-defined because, by Lemma 1, it depends only on the germ of $e_j$ at $m$. Thus, as a section of $\operatorname{Hom}(E, F)$-valued forms over $U$, $a$ satisfies $a \cdot e_j = A(e_j) \in \Omega^p(U; F)$ for each $j$.
>
> **Step 4 — smoothness of $a$.** Over $U$, expand $a$ against the dual frame: because $(e_j(m))$ is a basis of $E_m$ and $a_m(e_j(m)) = A(e_j)(m)$,
> $$a\big|_U = \sum_{j=1}^k A(e_j) \otimes e^j \in \Omega^p(U; \operatorname{Hom}(E, F)),$$
> meaning that on a vector $v = \sum_j e^j(v)\, e_j(m) \in E_m$, $\ a_m(v) = \sum_j e^j(v)\, A(e_j)(m)$, which reproduces $a_m$ by linearity (Step 2). Each $A(e_j) \in \Omega^p(U; F)$ is smooth (it is the image under $A$, after truncation, of a smooth section, and $A$ has values in the smooth forms $\Omega^p(M; F)$), and each $e^j$ is a smooth section of $E^*$; their tensor product is a smooth $\operatorname{Hom}(E, F)$-valued $p$-form on $U$. Since the pointwise-defined $a$ agrees on each such $U$ with this smooth local expression, and the $U$ cover $M$, $a$ is a smooth global section, $a \in \Omega^p(M; \operatorname{Hom}(E, F))$.
>
> **Step 5 — $A(s) = a \cdot s$ for all $s$.** Let $s \in \Gamma(E)$ and $m \in M$; work in a frame $(e_j)$ over a neighbourhood $U$ of $m$ and write $s|_U = \sum_j \sigma_j e_j$ with $\sigma_j \in C^\infty(U)$ (again [[Thm - Local Frames Span Sections|local frames span sections]]). Truncating with a bump function $\chi$ equal to $1$ near $m$ and supported in $U$, the global section $\chi^2 s = \sum_j (\chi\sigma_j)(\chi e_j)$ agrees with $s$ near $m$, so by locality (Lemma 1) $A(\chi^2 s)(m) = A(s)(m)$, and
> $$A(s)(m) = A(\chi^2 s)(m) = \sum_j (\chi\sigma_j)(m)\, A(\chi e_j)(m) = \sum_j \sigma_j(m)\, A(e_j)(m) \qquad \text{(}C^\infty(M)\text{- and } \mathbb{R}\text{-linearity; } \chi(m) = 1\text{).}$$
> On the other side, by Step 3 and $C^\infty$-linearity of the pairing in $s$ (Step 0),
> $$(a \cdot s)(m) = \Big(a \cdot \sum_j \sigma_j e_j\Big)(m) = \sum_j \sigma_j(m)\,(a \cdot e_j)(m) = \sum_j \sigma_j(m)\, A(e_j)(m).$$
> The two right-hand sides coincide, so $A(s)(m) = (a \cdot s)(m)$. As $m$ was arbitrary, $A(s) = a \cdot s$.
>
> **Step 6 — uniqueness of $a$.** Suppose $a, a' \in \Omega^p(M; \operatorname{Hom}(E, F))$ both satisfy $A(s) = a \cdot s = a' \cdot s$ for all $s$. Fix $m$ and $v \in E_m$; by Lemma 2 pick $s$ with $s(m) = v$. Then
> $$a_m(v) = a_m(s(m)) = (a \cdot s)(m) = A(s)(m) = (a' \cdot s)(m) = a'_m(v),$$
> using the value description of the pairing from Step 0. As $v \in E_m$ and $m \in M$ are arbitrary, $a_m = a'_m$ for all $m$, i.e. $a = a'$.
>
> **Step 7 — the converse and the bijection.** Step 0 shows that any $a \in \Omega^p(M; \operatorname{Hom}(E, F))$ yields, via $s \mapsto a \cdot s$, an $\mathbb{R}$- and $C^\infty(M)$-linear map. Steps 1–6 show that every such map arises from a unique $a$. Hence $a \mapsto (s \mapsto a \cdot s)$ is a bijection from $\Omega^p(M; \operatorname{Hom}(E, F))$ onto the space of $C^\infty(M)$-linear maps $\Gamma(E) \to \Omega^p(M; F)$; it is manifestly $\mathbb{R}$-linear in $a$, hence an isomorphism of vector spaces.
>
> **Step 8 — the multilinear form.** Let $A : \Gamma(E_1) \times \cdots \times \Gamma(E_r) \to \Omega^p(M; F)$ be $\mathbb{R}$-multilinear and $C^\infty(M)$-linear in each argument. Applying Lemmas 1 and 3 in each argument separately (with the other arguments held fixed — the hypotheses hold slot by slot), the value $A(s_1, \dots, s_r)(m)$ vanishes whenever any $s_i(m) = 0$, and therefore depends on $(s_1, \dots, s_r)$ only through the tuple of fibre vectors $(s_1(m), \dots, s_r(m)) \in E_{1,m} \times \cdots \times E_{r,m}$. This defines a map
> $$b_m : E_{1,m} \times \cdots \times E_{r,m} \longrightarrow \Lambda^p T^*_m M \otimes F_m, \qquad b_m(v_1, \dots, v_r) := A(s_1, \dots, s_r)(m) \text{ for any } s_i \text{ with } s_i(m) = v_i,$$
> well-defined by the pointwise-dependence argument in each slot and $\mathbb{R}$-multilinear by the argument of Step 2 in each slot. A multilinear map out of a product of fibres is, by the universal property of the tensor product, a linear map out of $E_{1,m} \otimes \cdots \otimes E_{r,m}$; thus $b_m$ corresponds to
> $$a_m \in \operatorname{Hom}\big(E_{1,m} \otimes \cdots \otimes E_{r,m},\ \Lambda^p T^*_m M \otimes F_m\big) = \Lambda^p T^*_m M \otimes \operatorname{Hom}(E_1 \otimes \cdots \otimes E_r,\, F)_m$$
> with $a_m(v_1 \otimes \cdots \otimes v_r) = b_m(v_1, \dots, v_r)$. Smoothness of the assembled $a$ follows exactly as in Steps 3–4, using frames $(e^{(i)}_{j})_j$ of each $E_i$: the components of $a$ against the induced frame $e^{(1)}_{j_1} \otimes \cdots \otimes e^{(r)}_{j_r}$ of $E_1 \otimes \cdots \otimes E_r$ are the smooth forms $A(e^{(1)}_{j_1}, \dots, e^{(r)}_{j_r})$. Finally $A(s_1, \dots, s_r) = a \cdot (s_1 \otimes \cdots \otimes s_r)$ by the frame expansion of Step 5 carried out in each argument, and uniqueness follows as in Step 6 since $a_m$ is determined on all decomposable tensors $v_1 \otimes \cdots \otimes v_r$, which span $E_{1,m} \otimes \cdots \otimes E_{r,m}$.
>
> This establishes existence, uniqueness, the converse, and the multilinear generalisation. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**The difference of two connections as an endomorphism-valued form.** Give a student two connections $\nabla, \hat\nabla$ on the same bundle $E$ — say the trivial connection $d$ and the projected connection $\operatorname{pr}(d\,\cdot\,)$ on $TS^2 \subseteq \underline{\mathbb{R}^3}$ — and ask them to identify $\nabla - \hat\nabla$ as multiplication by a fixed $a \in \Omega^1(M; \operatorname{End} E)$. The tensoriality lemma applies because the Leibniz terms cancel in the difference, and it is non-obvious that the answer is a *pointwise* algebraic object rather than a differential operator: the exercise makes visible that the affine structure on the space of connections is a direct payoff of this lemma.

**Curvature as a $2$-form from the second covariant derivative.** On the trivial line bundle over $\mathbb{R}^2$ with connection $\nabla = d + A$, $A = x\,dy$, ask the student first to verify that $d^\nabla \circ d^\nabla$ is $C^\infty$-linear by the iterated-Leibniz cancellation, and then to invoke the lemma to conclude that there is a genuine $2$-form $F_\nabla$ with $d^\nabla d^\nabla s = F_\nabla s$; a direct computation gives $F_\nabla = dx \wedge dy$. This is non-obvious because $d^\nabla \circ d^\nabla$ is manifestly a second-order operator, and only the cancellation licensed here lets one replace it by a zeroth-order (tensorial) object.

**The tensor characterisation lemma in Riemannian geometry.** Ask the student to prove that the Riemann curvature operator $(X, Y, Z) \mapsto \nabla_X \nabla_Y Z - \nabla_Y \nabla_X Z - \nabla_{[X, Y]} Z$ is $C^\infty(M)$-linear in all three arguments and hence a $\binom{1}{3}$-tensor, so that "$R(X, Y)Z$ at $p$" depends only on $X_p, Y_p, Z_p$. This is the multilinear form of the present lemma specialised to $E = F = TM$, and it connects to the scalar-valued [[Thm - Tensor Field is C-Infinity Multilinear over C-Infinity Functions|tensor characterisation lemma]]; the value is seeing that a two-derivative expression can still define a pointwise tensor, provided the derivative terms cancel.

---

# Bridges

- **[[Thm - Tensor Field is C-Infinity Multilinear over C-Infinity Functions|The tensor characterisation lemma (differential geometry)]]** — the scalar-valued special case. Taking $E_i = TM$ (or $T^*M$), $F = \underline{\mathbb{R}}$ the trivial line bundle, and $p = 0$, so that $\Omega^0(M; \underline{\mathbb{R}}) = C^\infty(M)$, the multilinear form of the present lemma becomes exactly the statement that a $C^\infty(M)$-multilinear map $\mathfrak{X}(M)^k \to C^\infty(M)$ is a covariant $k$-tensor field. That page's proof runs the same locality-and-pointwise-dependence argument; the present page generalises the *values* from $C^\infty(M)$ to sections of an arbitrary bundle $F$ and adds the antisymmetric form-slots $\Lambda^p T^*M$.

- **[[Thm - Existence of the Curvature Form|Existence of the curvature form]]** — the immediate downstream user. That theorem shows $d^\nabla \circ d^\nabla : \Omega^0(M; E) \to \Omega^2(M; E)$ is $C^\infty(M)$-linear by the double Leibniz cancellation, and then invokes the present lemma (with $F = E$, $p = 2$) to produce the unique $F_\nabla \in \Omega^2(M; \operatorname{End} E)$ with $d^\nabla d^\nabla s = F_\nabla \cdot s$. Every appearance of "*the* curvature $2$-form" relies on the uniqueness half proved here.

- **[[Def - Torsion Tensor|The torsion tensor]]** — the multilinear form in action. For a connection on $TM$, the map $(v, w) \mapsto \nabla_v w - \nabla_w v - [v, w]$ is $C^\infty(M)$-bilinear (the source's remark R2.3.1), so the multilinear lemma with $E_1 = E_2 = F = TM$, $p = 0$ delivers $T \in \Gamma(\operatorname{Hom}(TM \otimes TM, TM))$; antisymmetry $T(v, w) = -T(w, v)$ then places $T \in \Omega^2(M; TM)$.

- **[[Thm - The Space of Connections is an Affine Space|The space of connections is an affine space]]** — the structural payoff. Its part (b), that the difference of two connections lies in $\Omega^1(M; \operatorname{End} E)$, is precisely this lemma applied to the $C^\infty(M)$-linear operator $\nabla - \hat\nabla$; the affine model space $\Omega^1(M; \operatorname{End} E)$ is the codomain of the lemma in the case $F = E$, $p = 1$.

---

# Unlocked by This

> [!tip] The curvature form $F_\nabla$ *(from Gauge Theory)*
> Once $d^\nabla \circ d^\nabla$ is known to be $C^\infty(M)$-linear, this lemma turns it into a genuine section $F_\nabla \in \Omega^2(M; \operatorname{End} E)$, the object on which all of Chern–Weil theory and Yang–Mills theory is built. See **[[Def - Curvature of a Vector-Bundle Connection]]**.

> [!tip] Tensoriality of any cancelling combination of derivatives *(from Differential Geometry)*
> The lemma gives a uniform test — check $C^\infty(M)$-linearity in each slot — for deciding whether a derivative expression is secretly a tensor. It is the reason the Riemann, Ricci, and Weyl curvatures, the torsion, and the second fundamental form are all pointwise objects despite being written with covariant derivatives.
