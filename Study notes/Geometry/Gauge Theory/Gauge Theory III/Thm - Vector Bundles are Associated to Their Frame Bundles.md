---
type: theorem
subject: gauge-theory
prereqs:
  - "Def - Associated Bundle"
  - "Def - Frame Bundle of a Vector Bundle"
  - "Def - Constructions on Representations"
  - "Def - Operations on Vector Bundles and Pull-Back Bundles"
  - "Def - Representation of a Lie Group"
  - "Thm - Free Proper Actions Give Principal Bundles"
tags: [geometry, gauge-theory]
---

# Notation

We work over a fixed smooth manifold $M$ (smooth, Hausdorff, second countable, $C^\infty$). All vector bundles are real of finite rank; the complex case is identical with $\mathbb{R}$ replaced by $\mathbb{C}$ and $GL_k(\mathbb{R})$ by $GL_k(\mathbb{C})$, and we note the one place the argument uses realness. Throughout, $E \to M$ is a vector bundle of rank $k$ and $F \to M$ a vector bundle of rank $l$.

A **frame** of $E$ at a point $m \in M$ is a linear isomorphism $e : \mathbb{R}^k \to E_m$; equivalently it is the ordered basis $(e_1, \dots, e_k)$ of $E_m$ with $e_i = e(\varepsilon_i)$, where $\varepsilon_1, \dots, \varepsilon_k$ is the standard basis of $\mathbb{R}^k$. We write $e \cdot x$ or $e(x)$ for the value $\sum_{i=1}^k x_i e_i \in E_m$ of the frame $e$ on $x = (x_1, \dots, x_k) \in \mathbb{R}^k$. The [[Def - Frame Bundle of a Vector Bundle|frame bundle]] $\operatorname{Fr}(E) = \bigsqcup_{m \in M} \operatorname{Fr}(E_m)$ collects all frames; it is a principal $GL_k(\mathbb{R})$-bundle for the right action $e \cdot h := e \circ h$, so that $(e \cdot h)(x) = e(hx)$ for $h \in GL_k(\mathbb{R})$ (matrix multiplication $hx$). We abbreviate $G := GL_k(\mathbb{R})$ and $\operatorname{Fr}(E) =: P$ when no confusion arises.

A **representation** of a Lie group $G$ on a finite-dimensional real vector space $V$ is a smooth homomorphism $\rho : G \to GL(V)$ ([[Def - Representation of a Lie Group|representation]]). The **standard representation** of $G = GL_k(\mathbb{R})$ is the identity $\rho_{\mathrm{st}} = \operatorname{id} : GL_k(\mathbb{R}) \to GL(\mathbb{R}^k)$, $\rho_{\mathrm{st}}(g) = g$. Given a principal $G$-bundle $P \to M$ and a representation $\rho$ on $V$, the [[Def - Associated Bundle|associated vector bundle]] is
$$P \times_\rho V := (P \times V)/G, \qquad (p, v) \cdot g := (p \cdot g,\, \rho(g^{-1}) v),$$
whose points are equivalence classes $[p, v]$. We use repeatedly the identity
$$[p \cdot g,\, v] = [p,\, \rho(g) v] \qquad (p \in P,\ v \in V,\ g \in G),$$
obtained from the defining relation $(p, v) \cdot g = (p \cdot g, \rho(g^{-1}) v)$ by substituting $v \mapsto \rho(g) v$. The projection is $\pi_\rho([p, v]) = \pi(p)$ and the fibre over $m$ is a vector space with $[p, v] + [p, w] = [p, v + w]$ and $c \cdot [p, v] = [p, c v]$ for a *fixed* representative $p$ in the fibre $P_m$; these operations are independent of that choice, as established on [[Def - Associated Bundle]].

For the tensor constructions we use the [[Def - Constructions on Representations|constructions on representations]]. For representations $\rho_1$ on $V_1$ and $\rho_2$ on $V_2$ we have the direct sum $\rho_1 \oplus \rho_2$ on $V_1 \oplus V_2$, the tensor product $\rho_1 \otimes \rho_2$ on $V_1 \otimes V_2$, the exterior power $\Lambda^p \rho$ on $\Lambda^p V$, and the **dual representation**
$$\rho^*(g) := \rho(g^{-1})^* \in GL(V^*),$$
where $A^* : V^* \to V^*$ is the transpose (adjoint) of $A \in GL(V)$. In the standard basis of $\mathbb{R}^k$ and its dual, $\rho_{\mathrm{st}}^*(g) = (g^{-1})^t = (g^t)^{-1}$.

> [!warning] Convention: dual representation carries an inverse
> The dual is $\rho^*(g) = \rho(g^{-1})^*$, not $\rho(g)^*$; the inverse is what repairs the anti-homomorphism $g \mapsto \rho(g)^*$ into a homomorphism (see [[Def - Constructions on Representations]]). Haydys's Example 33 writes the exterior-power representation on $\Lambda^p(\mathbb{R}^k)^*$ directly as $(g, \alpha) \mapsto \alpha(g^{-1}\,\cdot, \dots, g^{-1}\,\cdot)$; this is exactly $\Lambda^p \rho_{\mathrm{st}}^*(g)$ in the present notation, because $\big(\Lambda^p \rho_{\mathrm{st}}^*(g)\big)\alpha = \alpha(g^{-1}\,\cdot, \dots, g^{-1}\,\cdot)$.

For the transition functions of derived bundles we use the [[Def - Operations on Vector Bundles and Pull-Back Bundles|operations on vector bundles]]. If $E$ has [[Def - Transition Function of a Vector Bundle|transition functions]] $\tau_{\alpha\beta} : U_{\alpha\beta} \to GL_k(\mathbb{R})$ relative to local frames $e_\alpha$ over a cover $\{U_\alpha\}$ (with $U_{\alpha\beta} := U_\alpha \cap U_\beta$), and $F$ has transition functions $\sigma_{\alpha\beta} : U_{\alpha\beta} \to GL_l(\mathbb{R})$, then the derived bundles carry the transition functions
$$
E^* : (\tau_{\alpha\beta}^{-1})^t, \quad
\Lambda^p E : \Lambda^p \tau_{\alpha\beta}, \quad
\Lambda^p E^* : \Lambda^p\!\big((\tau_{\alpha\beta}^{-1})^t\big), \quad
E \oplus F : \tau_{\alpha\beta} \oplus \sigma_{\alpha\beta}, \quad
E \otimes F : \tau_{\alpha\beta} \otimes \sigma_{\alpha\beta},
$$
$$
\operatorname{Hom}(E, F) : \phi \mapsto \sigma_{\alpha\beta}\, \phi\, \tau_{\alpha\beta}^{-1}, \qquad
\operatorname{End}(E) : \phi \mapsto \tau_{\alpha\beta}\, \phi\, \tau_{\alpha\beta}^{-1},
$$
each proved to satisfy the cocycle condition on [[Def - Operations on Vector Bundles and Pull-Back Bundles]]. Our sign convention for a transition function is that of [[Def - Transition Function of a Vector Bundle]]: writing $\phi_\alpha : E|_{U_\alpha} \to U_\alpha \times \mathbb{R}^k$ for the trivialisation reading off coordinates in the frame $e_\alpha$, one has $\phi_\alpha \circ \phi_\beta^{-1}(m, x) = (m, \tau_{\alpha\beta}(m) x)$.

An **isomorphism of vector bundles** over $M$ is a smooth [[Def - Bundle Homomorphism|bundle homomorphism]] $\Phi : W_1 \to W_2$ covering $\operatorname{id}_M$ that is a diffeomorphism whose fibrewise restrictions $\Phi_m : (W_1)_m \to (W_2)_m$ are linear isomorphisms; equivalently a bijective smooth bundle map that is fibrewise a linear isomorphism ([[Def - Bundle Homomorphism]]). We write $\cong$ for isomorphism over $M$. The standing conventions of this series (right principal actions; the associated-bundle sign $(p, v) \cdot g = (pg, \rho(g^{-1}) v)$) are those of the [[Gauge Theory III — Fibre Bundles, Principal Bundles, and Associated Bundles|chapter topic page]].

---

# Statement

> **Theorem (a vector bundle is associated to its frame bundle).** Let $E \to M$ be a rank-$k$ vector bundle with frame bundle $P = \operatorname{Fr}(E)$, structure group $G = GL_k(\mathbb{R})$.
>
> **(a) The standard representation recovers $E$.** With $\rho_{\mathrm{st}} = \operatorname{id}$ the standard representation on $\mathbb{R}^k$, the map
> $$\Phi : \operatorname{Fr}(E) \times_{\rho_{\mathrm{st}}} \mathbb{R}^k \longrightarrow E, \qquad [e, x] \longmapsto e \cdot x = \textstyle\sum_{i=1}^k x_i e_i,$$
> is a well-defined isomorphism of vector bundles over $M$.
>
> **(b) Exterior powers of the dual.** For each $p \ge 0$, with the representation $\Lambda^p \rho_{\mathrm{st}}^*$ on $\Lambda^p(\mathbb{R}^k)^*$,
> $$\operatorname{Fr}(E) \times_{\Lambda^p \rho_{\mathrm{st}}^*} \Lambda^p(\mathbb{R}^k)^* \;\cong\; \Lambda^p E^*, \qquad [e, \alpha] \longmapsto \alpha\big(e^{-1}\,\cdot, \dots, e^{-1}\,\cdot\big),$$
> where the frame $e$ is read as an isomorphism $\mathbb{R}^k \to E_m$ and $e^{-1} : E_m \to \mathbb{R}^k$.
>
> **(c) All tensor constructions.** Applying to the standard representation the corresponding [[Def - Constructions on Representations|construction on representations]] yields, in each case, the same-named [[Def - Operations on Vector Bundles and Pull-Back Bundles|operation on vector bundles]]:
> $$E^* \cong \operatorname{Fr}(E) \times_{\rho_{\mathrm{st}}^*} (\mathbb{R}^k)^*, \qquad \Lambda^p E \cong \operatorname{Fr}(E) \times_{\Lambda^p \rho_{\mathrm{st}}} \Lambda^p \mathbb{R}^k, \qquad \operatorname{End}(E) \cong \operatorname{Fr}(E) \times_{\operatorname{Ad}} M_k(\mathbb{R}),$$
> where $\operatorname{Ad}(g) A = g A g^{-1}$; and, using the fibre-product principal bundle $\operatorname{Fr}(E) \times_M \operatorname{Fr}(F)$ (structure group $GL_k(\mathbb{R}) \times GL_l(\mathbb{R})$),
> $$E \oplus F \cong \operatorname{Fr}(E) \times_M \operatorname{Fr}(F) \times_{\rho_{\mathrm{st}} \oplus \rho_{\mathrm{st}}} (\mathbb{R}^k \oplus \mathbb{R}^l), \quad E \otimes F \cong \operatorname{Fr}(E) \times_M \operatorname{Fr}(F) \times_{\rho_{\mathrm{st}} \otimes \rho_{\mathrm{st}}} (\mathbb{R}^k \otimes \mathbb{R}^l),$$
> $$\operatorname{Hom}(E, F) \cong \operatorname{Fr}(E) \times_M \operatorname{Fr}(F) \times_{\rho_{\mathrm{st}}^* \otimes \rho_{\mathrm{st}}} \operatorname{Hom}(\mathbb{R}^k, \mathbb{R}^l).$$
>
> **(d) Reduction to a $G$-structure.** If $G' \le GL_k(\mathbb{R})$ is a closed subgroup and $P' \subset \operatorname{Fr}(E)$ is a $G'$-structure on $E$ (a $G'$-subbundle of the frame bundle, in the sense of [[Def - Reduction and Extension of the Structure Group]]), then, with $\rho_{\mathrm{st}}|_{G'}$ the restricted standard representation,
> $$P' \times_{G'} \mathbb{R}^k \;\cong\; E, \qquad [p, x] \longmapsto p \cdot x.$$

The four parts are one statement in four costumes: the assignment $V \mapsto \operatorname{Fr}(E) \times_\rho V$ from representations of the structure group to vector bundles over $M$ is a dictionary that turns the standard representation and every construction performed on it into $E$ and the same construction performed on it. Part (a) is the entry "standard $\leftrightarrow E$"; parts (b) and (c) are the entries for the derived representations; part (d) says the dictionary is compatible with restricting the structure group.

---

# Motivation

The frame bundle $\operatorname{Fr}(E)$ was built ([[Def - Frame Bundle of a Vector Bundle]]) to hold, over each point, *all* the frames of the fibre at once, with the change-of-frame group $GL_k(\mathbb{R})$ acting freely and transitively on them. This is a deliberately larger and more symmetric object than $E$ itself: where a section of $E$ is a choice of vector in each fibre, a section of $\operatorname{Fr}(E)$ is a choice of *basis* in each fibre, and no natural basis exists, so $\operatorname{Fr}(E)$ typically has no global section at all. The question this theorem answers is whether we have lost anything by passing from $E$ to $\operatorname{Fr}(E)$ — and, more importantly, whether the passage is reversible.

It is, and completely so. Part (a) says that $E$ can be reconstructed from $\operatorname{Fr}(E)$ alone, by the single operation of forming the associated bundle with the standard representation. Nothing about $E$ is thrown away in remembering only its frames; the vector bundle is exactly the frames of one fibre-worth of $\mathbb{R}^k$, glued by the same change-of-frame data. The smallest instance makes this concrete. If $E = L$ is a real line bundle ($k = 1$), a frame at $m$ is a nonzero vector $e \in L_m$, so $\operatorname{Fr}(L)$ is the complement of the zero section, and $G = GL_1(\mathbb{R}) = \mathbb{R}^\times$ acts by rescaling. The associated bundle $\operatorname{Fr}(L) \times_{\rho_{\mathrm{st}}} \mathbb{R}$ has a point $[e, x]$ for a nonzero $e \in L_m$ and a scalar $x$, with $[e, x] = [e \lambda, \lambda^{-1} x]$; the map $[e, x] \mapsto x e$ sends this to $L_m$, and it is a bijection because every vector of $L_m$ is a scalar multiple of any given nonzero $e$. We have simply re-coordinatised the line by one of its own vectors.

Why does this matter, when we already have $E$? Because the frame bundle is where the *group* lives, and the group is where the tools of gauge theory live. A connection on $E$ is a somewhat ad hoc object — a covariant derivative satisfying a Leibniz rule — whereas a connection on $\operatorname{Fr}(E)$ is a $\mathfrak{gl}_k$-valued one-form with a clean equivariance law, on which the entire apparatus of Chern–Weil theory and the Bianchi identity acts uniformly. Once part (a) is known, a connection on $\operatorname{Fr}(E)$ induces one on $E$ (chapter IV), and conversely; the two theories are the same theory. The point of the theorem is to license moving freely between the vector bundle and its principal frame bundle, so that constructions natural on one side can be imported to the other.

Parts (b) and (c) extend the dictionary to the whole tensor algebra. Once we know how to turn a representation of $GL_k(\mathbb{R})$ into a bundle, every construction we perform on the standard representation — dualising, taking exterior or tensor powers, forming endomorphisms — is mirrored by the same construction on $E$. This is why the notation is so persistently the same on both sides: $\Lambda^p E^*$ does not merely resemble $\Lambda^p(\mathbb{R}^k)^*$ with the natural $GL_k(\mathbb{R})$-action, it *is* the bundle that action produces. In particular the endomorphism bundle $\operatorname{End}(E)$ is the associated bundle of the adjoint (conjugation) representation, which is exactly why the curvature of a connection, an $\operatorname{End}(E)$-valued two-form, transforms by conjugation under change of frame, and why the adjoint bundle $\operatorname{ad}\operatorname{Fr}(E)$ of chapter III equals $\operatorname{End}(E)$.

Part (d) is the reason $G$-structures deserve the name. To equip $E$ with a Euclidean metric, an orientation, or a complex structure is, by the reduction theory of [[Def - Reduction and Extension of the Structure Group]], to choose a subbundle of frames respecting that structure — an $O(k)$-, $GL_k^+$-, or $GL_m(\mathbb{C})$-structure. Part (d) says the reduced principal bundle carries no less information than $E$: applying the standard representation of the *smaller* group to the *smaller* bundle of frames still returns $E$. The metric or orientation is packaged in which frames we kept, not in the reconstruction step. This is the statement that lets one work with the orthonormal frame bundle in place of the full frame bundle without changing the underlying vector bundle at all.

---

# Sources and Targets

**Sources (Input Broadening)**

The theorem's literal hypothesis is only that $E$ is a vector bundle, so the useful "source" question is: which objects, not presented as associated bundles, are secretly associated bundles that the theorem lets us recognise as such?

The first disguised source is **a bundle presented by an explicit fibrewise tensor construction** — a dual $E^*$, an exterior power $\Lambda^p E^*$ of differential-form type, an endomorphism bundle $\operatorname{End}(E)$, a homomorphism bundle $\operatorname{Hom}(E, F)$. Such a bundle arrives with no group in sight; it is glued from the derived transition functions of [[Def - Operations on Vector Bundles and Pull-Back Bundles]]. The non-obvious bridge $B \Rightarrow A$ is that those derived transition functions are exactly $\rho \circ \tau_{\alpha\beta}$ for the corresponding representation $\rho$ of $GL_k(\mathbb{R})$, so the bundle is $\operatorname{Fr}(E) \times_\rho V$; once recognised, it inherits every construction that is natural on representations. *Example problem:* show that the bundle $\Lambda^n T^* M$ of top forms on an $n$-manifold is $\operatorname{Fr}(TM) \times_{\det^{-1}} \mathbb{R}$ (the representation $g \mapsto \det(g)^{-1}$), so that a nowhere-vanishing section — a volume form — exists precisely when this associated line bundle is trivial, that is, when $M$ is orientable.

The second disguised source is **a vector bundle carrying extra pointwise structure**: a Euclidean metric, a Hermitian metric, an orientation, a complex structure, a fibrewise volume form. Each such structure is, by [[Def - Reduction and Extension of the Structure Group]], the same datum as a reduction of $\operatorname{Fr}(E)$ to a closed subgroup $G' \le GL_k(\mathbb{R})$ (respectively $O(k)$, $U(m)$, $GL_k^+(\mathbb{R})$, $GL_m(\mathbb{C})$, $SL_k(\mathbb{R})$). The bridge is part (d): the reduced bundle $P' \times_{G'} \mathbb{R}^k$ is still $E$, so one may replace the full frame bundle by the structured one at no cost to the underlying bundle. *Example problem:* on a Riemannian manifold, realise $TM$ as $O(TM) \times_{O(n)} \mathbb{R}^n$ and deduce that the Levi-Civita connection, an $O(n)$-connection on the orthonormal frame bundle, induces the metric covariant derivative on $TM$.

The third disguised source is **a representation of the structure group itself**, handed over abstractly. Any finite-dimensional representation $\rho : GL_k(\mathbb{R}) \to GL(V)$ manufactures a bundle $\operatorname{Fr}(E) \times_\rho V$; conversely the theorem tells us that all the tensor bundles we already know arise this way, so a new representation produces a genuinely new natural bundle. The bridge is that the association is functorial in $\rho$: a $G$-equivariant map $V_1 \to V_2$ induces a bundle map $\operatorname{Fr}(E) \times_{\rho_1} V_1 \to \operatorname{Fr}(E) \times_{\rho_2} V_2$. *Example problem:* the Clebsch–Gordan decomposition $\rho_{\mathrm{st}} \otimes \rho_{\mathrm{st}} \cong \Lambda^2 \oplus \operatorname{Sym}^2$ of $GL_k(\mathbb{R})$-representations yields the bundle splitting $E \otimes E \cong \Lambda^2 E \oplus \operatorname{Sym}^2 E$ with no further work.

**Targets (Output Amplification)**

Combine the theorem with **the theory of connections on principal bundles (chapter IV)**. A single principal connection on $\operatorname{Fr}(E)$ induces, via the associated-bundle construction, a covariant derivative on $E$ *and simultaneously* on $E^*$, $\Lambda^p E^*$, $\operatorname{End}(E)$, and every other tensor bundle, all compatible with the natural pairings. The extra ingredient is the principal connection; the payoff is that the induced connections of [[Def - Induced Connections on Dual, Hom, and Endomorphism Bundles]] are not a menagerie of separate definitions but one object seen through the dictionary.

Combine the theorem with **gauge theory (chapter V)**. The gauge group of $E$ — the automorphisms of $E$ covering the identity — is the group of sections of $\operatorname{Aut}(E) = \operatorname{Fr}(E) \times_{\alpha} GL_k(\mathbb{R})$ (conjugation action $\alpha$), and its Lie algebra is the sections of $\operatorname{End}(E) = \operatorname{ad}\operatorname{Fr}(E)$; both identifications are instances of part (c). The extra ingredient is the associated-group-bundle construction of [[Def - Adjoint Bundles ad P and Ad P]]; the payoff is that the gauge group of the vector bundle and the automorphism group of the principal bundle are literally the same group.

Combine the theorem with **Chern–Weil theory (chapter VI)**. Because $E$ and $\operatorname{Fr}(E)$ carry the same connections and curvatures under the dictionary, the characteristic classes computed from the curvature of a connection on $E$ agree with those computed on $\operatorname{Fr}(E)$; and because $\Lambda^p E^*$, $\det E = \Lambda^k E$, and the like are associated bundles, their characteristic classes are determined by the representation. The extra ingredient is an invariant polynomial on $\mathfrak{gl}_k$; the payoff is that the Chern and Pontryagin classes of every tensor bundle are polynomial functions of those of $E$.

---

# Why Is It True

Strip away the formalism and picture a single fibre $E_m$, a $k$-dimensional real vector space with no distinguished basis. A frame $e$ at $m$ is precisely a choice of basis, that is, an isomorphism $e : \mathbb{R}^k \to E_m$. Two frames differ by a unique change-of-basis matrix $g \in GL_k(\mathbb{R})$, namely $e' = e \cdot g$. To name a vector $v \in E_m$ we may give its coordinate column $x = e^{-1} v \in \mathbb{R}^k$ *relative to a frame $e$*; the same vector has coordinates $x' = (e')^{-1} v = g^{-1} x$ relative to $e' = e g$. So a vector of $E_m$ is exactly a pair (frame, coordinate column) up to the simultaneous change $(e, x) \sim (e g, g^{-1} x)$ — and that equivalence is *identically* the one defining the associated bundle $\operatorname{Fr}(E) \times_{\rho_{\mathrm{st}}} \mathbb{R}^k$, because the standard representation makes $\rho_{\mathrm{st}}(g^{-1}) x = g^{-1} x$.

> **The mechanism in one sentence:** a vector is a coordinate column together with the frame in which it is read, modulo the rule that changing the frame changes the column by the inverse matrix — and that "coordinate column modulo change of frame" is the definition of the associated bundle.

This is why part (a) is true and why it is inevitable: the map $[e, x] \mapsto e(x)$ is not a clever construction to be discovered but the only thing the class $[e, x]$ could denote once we agree that $x$ is coordinates in the frame $e$. The well-definedness — that $[e g, g^{-1} x]$ and $[e, x]$ have the same image — is the statement that the vector $e(x)$ does not depend on which frame we used to write it down, which is the whole content of "coordinates transform correctly".

Parts (b) and (c) then run on inheritance. A tensor over $E_m$ — a covector, a $p$-form, an endomorphism — is likewise named by its components in a frame, and the components of the *same* tensor transform, under $e' = e g$, by the representation of $GL_k(\mathbb{R})$ that the tensor's type dictates: a covector's components by $(g^{-1})^t$, a $p$-form's by $\Lambda^p (g^{-1})^t$, an endomorphism's matrix by conjugation $A \mapsto g^{-1} A g$. Each of these transformation laws is exactly the representation appearing in the corresponding construction on the standard representation. So the same picture repeats: a tensor is components-in-a-frame modulo the correct transformation law, and that is the associated bundle for the correct representation. The uniform reason underneath all of parts (a)–(c) is that **the transition functions of an associated bundle are the representation applied to the transition functions of the principal bundle**, and the transition functions of $\operatorname{Fr}(E)$ are the transition functions of $E$; the tensor constructions on $E$ and the representation constructions on $\mathbb{R}^k$ are governed by the same functorial recipe applied to the same matrices.

Part (d) is inheritance restricted. If we keep only the frames in a $G'$-subbundle $P'$, any two of them still differ by an element of the *smaller* group $G'$, and every vector is still a $G'$-coordinate column relative to one of the kept frames — because a $G'$-structure has a frame over every point. So the same reconstruction goes through with $G'$ in place of $GL_k(\mathbb{R})$: nothing about the vectors of $E_m$ needed all frames, only enough frames to span, and a $G'$-structure supplies exactly that.

---

# What Makes This Hard

The mathematical content is light; the difficulty is entirely in **bookkeeping the inverse**. Two inverses collide and must be tracked separately: the associated-bundle relation $(e, x) \sim (e g, g^{-1} x)$ puts a $g^{-1}$ on the vector, and the dual representation $\rho^*(g) = \rho(g^{-1})^*$ puts a further inverse-and-transpose on covectors, so in part (b) one must verify that $\big(\Lambda^p \rho_{\mathrm{st}}^*(g^{-1})\big)\alpha$ evaluated against $(e g)^{-1} v_i = g^{-1} e^{-1} v_i$ reproduces $\alpha(e^{-1} v_i)$; a single sign or a $g$ where a $g^{-1}$ belongs turns the intertwiner into a non-invariant nonsense map. The common error is to write the dual representation as $\rho(g)^*$ (forgetting the inverse), which is an anti-homomorphism and produces the wrong bundle.

The second subtlety is that "the map is a fibrewise linear isomorphism" and "the map is smooth" are genuinely separate obligations, and the proof of smoothness must be carried out *in local trivialisations for both bundles at once*, in both directions. It is not enough to write down a fibrewise iso and declare it smooth; one shows that in the trivialisations induced by a common local frame the map becomes the identity (or an explicit smooth matrix), which is what certifies both $\Phi$ and $\Phi^{-1}$ smooth. The transition-function computation is what makes this uniform across all the tensor constructions, and it is the part a hurried treatment omits.

---

# Rederivation Scaffold

**This section is self-sufficient: reading only what follows should let you reconstruct the entire proof.**

**High-level strategy:** Prove one structural lemma — that the transition functions of $\operatorname{Fr}(E)$ are those of $E$ (Lemma 1), that an associated bundle's transition functions are the representation applied to them (Lemma 2), and that two vector bundles with equal transition cocycles on a common cover are canonically isomorphic (Lemma 3). Then each part is: exhibit the natural fibrewise map, check it is well-defined on classes and a fibrewise linear isomorphism, and certify smoothness either by showing it is the identity in frame-induced trivialisations or by matching transition functions through Lemma 3.

**Subgoal decomposition:**

1. **Frame-bundle cocycle.** Show the transition functions of $\operatorname{Fr}(E)$ relative to the sections $m \mapsto e_\alpha(m)$ equal the transition functions $\tau_{\alpha\beta}$ of $E$.
   - *Hint:* A local frame is at once a local section of $\operatorname{Fr}(E)$; compare $e_\beta = e_\alpha \cdot \tau_{\alpha\beta}$ with the definition of the principal transition function $\sigma_\beta = \sigma_\alpha \cdot g_{\alpha\beta}$.
   - *Why needed:* It is what ties the principal side to the vector side; every part uses it.

2. **Associated cocycle.** Show that for any representation $\rho$, the bundle $P \times_\rho V$ has transition functions $\rho \circ g_{\alpha\beta}$ relative to the trivialisations induced by the sections $\sigma_\alpha$.
   - *Hint:* Use $[\sigma_\alpha g_{\alpha\beta}, v] = [\sigma_\alpha, \rho(g_{\alpha\beta}) v]$.
   - *Why needed:* It is the engine that turns each representation construction into the matching bundle construction.

3. **Recognition principle.** Show two vector bundles trivialised over a common cover with equal transition functions are isomorphic by the "identity in coordinates" map.
   - *Hint:* Define $\Phi_\alpha := (\Theta^2_\alpha)^{-1} \Theta^1_\alpha$ locally; check it is independent of $\alpha$ on overlaps using the equal transitions.
   - *Why needed:* It converts the cocycle equalities of Lemmas 1–2 into honest bundle isomorphisms and certifies smoothness.

4. **Part (a).** Exhibit $\Phi([e, x]) = e(x)$; check well-definedness, fibrewise linear bijectivity, and that it is the identity in frame-induced trivialisations.
   - *Hint:* $\Phi([e g, g^{-1} x]) = (e g)(g^{-1} x) = e(x)$.
   - *Why needed:* It is the base case and the template for all others.

5. **Part (b).** Exhibit $[e, \alpha] \mapsto \alpha(e^{-1}\,\cdot, \dots)$; check the inverse-bookkeeping and match transitions with $\Lambda^p E^*$.
   - *Hint:* $(e g)^{-1} = g^{-1} e^{-1}$; the two $g^{-1}$'s from the class relation and from evaluation cancel.
   - *Why needed:* It is the representative dual/exterior case and exhibits the inverse subtlety.

6. **Part (c).** For each construction, identify the representation, invoke Lemmas 1–3 to get the isomorphism, and give the explicit intertwiner for $\operatorname{End}(E)$ and $E \otimes F$.
   - *Hint:* Read off the representation from the transition functions listed in Notation; use the fibre product $\operatorname{Fr}(E) \times_M \operatorname{Fr}(F)$ for the two-bundle constructions.
   - *Why needed:* It completes the dictionary.

7. **Part (d).** Exhibit $[p, x] \mapsto p(x)$ on $P' \times_{G'} \mathbb{R}^k$; check it is a fibrewise iso using that $P'_m \ne \emptyset$, and certify smoothness by local sections of $P'$.
   - *Hint:* Restrict the part-(a) map along the inclusion $P' \hookrightarrow \operatorname{Fr}(E)$.
   - *Why needed:* It extends the theorem to reduced structure groups.

---

# Lemma Decomposition

> [!note]- Lemma 1: The transition functions of $\operatorname{Fr}(E)$ are the transition functions of $E$
> **Statement:** Let $E \to M$ have local frames $e_\alpha$ over a cover $\{U_\alpha\}$ with transition functions $\tau_{\alpha\beta} : U_{\alpha\beta} \to GL_k(\mathbb{R})$ (so $e_\beta = e_\alpha \cdot \tau_{\alpha\beta}$ pointwise). Regarding each frame as a smooth local section $\sigma_\alpha := e_\alpha$ of $\operatorname{Fr}(E)$, the transition functions $g_{\alpha\beta}$ of the principal bundle $\operatorname{Fr}(E)$ (defined by $\sigma_\beta = \sigma_\alpha \cdot g_{\alpha\beta}$) satisfy $g_{\alpha\beta} = \tau_{\alpha\beta}$.
>
> **Hint:** A local frame of $E$ is literally a local section of $\operatorname{Fr}(E)$; the two notions of "change of frame" must coincide.
>
> **Why needed:** It identifies the cocycle of the principal bundle with that of the vector bundle, so that Lemma 2 produces exactly the transition functions of the tensor operations.
>
> > [!note]- Full proof
> > **Setup.** By [[Def - Frame Bundle of a Vector Bundle|the construction of the frame bundle]], a smooth local frame $e_\alpha = (e_{\alpha,1}, \dots, e_{\alpha,k})$ of $E$ over $U_\alpha$ is precisely a smooth section $\sigma_\alpha : U_\alpha \to \operatorname{Fr}(E)$, namely $\sigma_\alpha(m) : \mathbb{R}^k \to E_m$, $\varepsilon_i \mapsto e_{\alpha,i}(m)$; smoothness of the frame is smoothness of the section, by the definition of the smooth structure on $\operatorname{Fr}(E)$ via the charts $\Psi_U(m, h) = e(m) \cdot h$.
> >
> > **The vector-bundle transition function.** By definition of $\tau_{\alpha\beta}$ ([[Def - Transition Function of a Vector Bundle]]), on $U_{\alpha\beta}$ the two frames are related by $e_\beta(m) = e_\alpha(m) \cdot \tau_{\alpha\beta}(m)$, meaning the isomorphism $e_\beta(m) : \mathbb{R}^k \to E_m$ equals $e_\alpha(m) \circ \tau_{\alpha\beta}(m)$ (matrix $\tau_{\alpha\beta}(m)$ acting first on $\mathbb{R}^k$). Indeed, writing $\phi_\gamma(v) = (m, e_\gamma(m)^{-1} v)$ for the trivialisation reading coordinates in $e_\gamma$, we have $\phi_\alpha \circ \phi_\beta^{-1}(m, x) = (m, e_\alpha(m)^{-1} e_\beta(m) x) = (m, \tau_{\alpha\beta}(m) x)$, so $e_\alpha^{-1} e_\beta = \tau_{\alpha\beta}$, that is, $e_\beta = e_\alpha \cdot \tau_{\alpha\beta}$ (by composing on the left with $e_\alpha$).
> >
> > **The principal transition function.** By definition of the transition function of the principal bundle $\operatorname{Fr}(E)$ ([[Def - Transition Functions and the Cocycle Condition]]), $g_{\alpha\beta}$ is the unique smooth map $U_{\alpha\beta} \to GL_k(\mathbb{R})$ with $\sigma_\beta = \sigma_\alpha \cdot g_{\alpha\beta}$, where $\cdot$ is the right $GL_k(\mathbb{R})$-action $e \cdot h = e \circ h$. That is, $\sigma_\beta(m) = \sigma_\alpha(m) \circ g_{\alpha\beta}(m)$.
> >
> > **Conclusion.** Comparing the two displayed relations, $\sigma_\beta = e_\beta = e_\alpha \circ \tau_{\alpha\beta} = \sigma_\alpha \circ \tau_{\alpha\beta}$ and $\sigma_\beta = \sigma_\alpha \circ g_{\alpha\beta}$; since the action is free, the element with $\sigma_\alpha \circ g_{\alpha\beta} = \sigma_\alpha \circ \tau_{\alpha\beta}$ is unique, so $g_{\alpha\beta}(m) = \tau_{\alpha\beta}(m)$ for every $m \in U_{\alpha\beta}$. Therefore the frame bundle and the vector bundle have the same transition cocycle. $\blacksquare$

> [!note]- Lemma 2: The transition functions of an associated bundle are the representation applied to those of the principal bundle
> **Statement:** Let $P \to M$ be a principal $G$-bundle with local sections $\sigma_\alpha$ over $\{U_\alpha\}$ and transition functions $g_{\alpha\beta}$ ($\sigma_\beta = \sigma_\alpha \cdot g_{\alpha\beta}$), and let $\rho : G \to GL(V)$ be a representation. In the local trivialisations $\Psi_\alpha$ of $E := P \times_\rho V$ determined by $\Psi_\alpha^{-1}(m, v) = [\sigma_\alpha(m), v]$, the transition functions of $E$ are $\rho \circ g_{\alpha\beta} : U_{\alpha\beta} \to GL(V)$.
>
> **Hint:** Rewrite $[\sigma_\beta, v]$ in terms of $\sigma_\alpha$ using $[\sigma_\alpha g_{\alpha\beta}, v] = [\sigma_\alpha, \rho(g_{\alpha\beta}) v]$.
>
> **Why needed:** It is the mechanism turning each representation into the matching bundle; combined with Lemma 1 it gives every tensor operation's transition functions.
>
> > [!note]- Full proof
> > **The trivialisations are well defined.** By [[Def - Associated Bundle|the associated-bundle construction]], for a local section $\sigma_\alpha$ the map $(m, v) \mapsto [\sigma_\alpha(m), v]$ is a diffeomorphism $U_\alpha \times V \to \pi_\rho^{-1}(U_\alpha)$ that is fibrewise a linear isomorphism; denote its inverse $\Psi_\alpha$. This is exactly the trivialisation of the associated bundle induced by $\sigma_\alpha$.
> >
> > **Compute the transition.** Fix $m \in U_{\alpha\beta}$ and $v \in V$. Then
> > $$\Psi_\beta^{-1}(m, v) = [\sigma_\beta(m), v] = [\sigma_\alpha(m) \cdot g_{\alpha\beta}(m),\, v] \qquad (\text{since } \sigma_\beta = \sigma_\alpha \cdot g_{\alpha\beta})$$
> > $$= [\sigma_\alpha(m),\, \rho(g_{\alpha\beta}(m))\, v] \qquad (\text{by the identity } [p \cdot g, v] = [p, \rho(g) v]).$$
> > Applying $\Psi_\alpha$, which sends $[\sigma_\alpha(m), w] \mapsto (m, w)$,
> > $$\Psi_\alpha\big(\Psi_\beta^{-1}(m, v)\big) = \big(m,\, \rho(g_{\alpha\beta}(m))\, v\big).$$
> >
> > **Conclusion.** The overlap map $\Psi_\alpha \circ \Psi_\beta^{-1}$ acts on the fibre by $v \mapsto \rho(g_{\alpha\beta}(m)) v$, so the transition function of $E = P \times_\rho V$ is $\rho \circ g_{\alpha\beta}$. As $\rho$ and $g_{\alpha\beta}$ are smooth and $\rho$ is a homomorphism, $\rho \circ g_{\alpha\beta}$ is a smooth $GL(V)$-valued cocycle. $\blacksquare$

> [!note]- Lemma 3: Two vector bundles with equal transition cocycles are canonically isomorphic
> **Statement:** Let $W_1, W_2 \to M$ be vector bundles with model fibre $V$, each trivialised over a common cover $\{U_\alpha\}$ by $\Theta^i_\alpha : W_i|_{U_\alpha} \to U_\alpha \times V$, and suppose their transition functions coincide: $h^{(1)}_{\alpha\beta} = h^{(2)}_{\alpha\beta} =: h_{\alpha\beta}$ on every $U_{\alpha\beta}$. Then the local maps $\Phi_\alpha := (\Theta^2_\alpha)^{-1} \circ \Theta^1_\alpha : W_1|_{U_\alpha} \to W_2|_{U_\alpha}$ agree on overlaps and glue to a global isomorphism of vector bundles $\Phi : W_1 \to W_2$ over $M$.
>
> **Hint:** On an overlap, push $\Phi_\beta$ into the $\alpha$-trivialisation and use $h^{(1)} = h^{(2)}$ to see it equals $\Phi_\alpha$.
>
> **Why needed:** It upgrades the cocycle equalities of Lemmas 1–2 into honest, smooth bundle isomorphisms, and simultaneously certifies smoothness of the maps in every part.
>
> > [!note]- Full proof
> > **Notation for fibre components.** For $w \in W_i|_{U_\alpha}$ write $\theta^i_\alpha(w) \in V$ for the fibre component of $\Theta^i_\alpha(w) = (\pi(w), \theta^i_\alpha(w))$. The transition law reads: for $w \in W_i|_{U_{\alpha\beta}}$,
> > $$\theta^i_\alpha(w) = h^{(i)}_{\alpha\beta}(\pi(w))\, \theta^i_\beta(w) \qquad (\text{definition of the transition function}).$$
> >
> > **Each $\Phi_\alpha$ is a local isomorphism.** The map $\Phi_\alpha = (\Theta^2_\alpha)^{-1} \circ \Theta^1_\alpha$ is a composite of two diffeomorphisms, each covering $\operatorname{id}_{U_\alpha}$ and fibrewise linear; hence $\Phi_\alpha$ is a smooth isomorphism of vector bundles over $U_\alpha$. In fibre components it is characterised by $\theta^2_\alpha(\Phi_\alpha w) = \theta^1_\alpha(w)$.
> >
> > **Agreement on overlaps.** Let $w \in W_1|_{U_{\alpha\beta}}$ and put $m = \pi(w)$. Then
> > $$\theta^2_\alpha(\Phi_\beta w) = h^{(2)}_{\alpha\beta}(m)\, \theta^2_\beta(\Phi_\beta w) \qquad (\text{transition law for } W_2)$$
> > $$= h^{(2)}_{\alpha\beta}(m)\, \theta^1_\beta(w) \qquad (\text{characterisation of } \Phi_\beta : \theta^2_\beta(\Phi_\beta w) = \theta^1_\beta(w))$$
> > $$= h^{(1)}_{\alpha\beta}(m)\, \theta^1_\beta(w) \qquad (\text{hypothesis } h^{(2)}_{\alpha\beta} = h^{(1)}_{\alpha\beta})$$
> > $$= \theta^1_\alpha(w) \qquad (\text{transition law for } W_1)$$
> > $$= \theta^2_\alpha(\Phi_\alpha w) \qquad (\text{characterisation of } \Phi_\alpha).$$
> > Since $\theta^2_\alpha$ is injective on each fibre (it is a component of a trivialisation), $\Phi_\beta w = \Phi_\alpha w$. As $w \in W_1|_{U_{\alpha\beta}}$ was arbitrary, $\Phi_\alpha = \Phi_\beta$ on $W_1|_{U_{\alpha\beta}}$.
> >
> > **Gluing.** The local maps therefore define a single map $\Phi : W_1 \to W_2$ with $\Phi|_{W_1|_{U_\alpha}} = \Phi_\alpha$. It is smooth because it is smooth on each open set $W_1|_{U_\alpha}$ of an open cover of $W_1$; it covers $\operatorname{id}_M$ and is fibrewise a linear isomorphism because each $\Phi_\alpha$ is. Hence $\Phi$ is an isomorphism of vector bundles over $M$ ([[Def - Bundle Homomorphism]]). $\blacksquare$

---

# Formal Proof

> [!note]- Complete formal proof
> Fix a rank-$k$ vector bundle $E \to M$, its frame bundle $P = \operatorname{Fr}(E)$ with structure group $G = GL_k(\mathbb{R})$, and a cover $\{U_\alpha\}$ over which $E$ has local frames $e_\alpha$ and transition functions $\tau_{\alpha\beta}$. We use $g_{\alpha\beta} := \tau_{\alpha\beta}$ for the principal transition functions of $\operatorname{Fr}(E)$ relative to the sections $\sigma_\alpha := e_\alpha$, justified by **Lemma 1**.
>
> **Step 0 — the associated bundles exist and are vector bundles.** For any representation $\rho : GL_k(\mathbb{R}) \to GL(V)$, the quotient $\operatorname{Fr}(E) \times_\rho V = (\operatorname{Fr}(E) \times V)/G$ is a smooth vector bundle over $M$: the diagonal $G$-action $(p, v) \cdot g = (p g, \rho(g^{-1}) v)$ is free and proper because the $G$-action on $\operatorname{Fr}(E)$ already is, so the quotient is a manifold and a fibre bundle by [[Thm - Free Proper Actions Give Principal Bundles]] (whose statement we invoke: *if a Lie group $G$ acts freely and properly on the right on $P$, and acts on a manifold $S$ on the left, then $(P \times S)/G \to P/G$ is a fibre bundle with fibre $S$*), and the fibrewise vector-space structure is well defined by [[Def - Associated Bundle]]. The same theorem provides the local trivialisations $\Psi_\alpha^{-1}(m, v) = [\sigma_\alpha(m), v]$ from the local sections $\sigma_\alpha$ of $\operatorname{Fr}(E)$. Likewise $\operatorname{Fr}(E) \times_M \operatorname{Fr}(F)$, the fibre product over $M$, is a principal $GL_k(\mathbb{R}) \times GL_l(\mathbb{R})$-bundle with sections $(\sigma_\alpha^E, \sigma_\alpha^F)$ and transition functions $(\tau_{\alpha\beta}, \sigma_{\alpha\beta})$.
>
> ---
>
> **Part (a) — the standard representation recovers $E$.**
>
> *Define the map.* Set $\Phi : \operatorname{Fr}(E) \times_{\rho_{\mathrm{st}}} \mathbb{R}^k \to E$, $\Phi([e, x]) := e(x) = \sum_{i=1}^k x_i e_i \in E_{\pi(e)}$.
>
> *$\Phi$ is well defined on classes.* Suppose $[e, x] = [e', x']$. Then there is $g \in GL_k(\mathbb{R})$ with $e' = e \cdot g = e \circ g$ and $x' = \rho_{\mathrm{st}}(g^{-1}) x = g^{-1} x$. Hence
> $$e'(x') = (e \circ g)(g^{-1} x) = e\big(g (g^{-1} x)\big) = e(x) \qquad (\text{associativity of composition; } g g^{-1} = \operatorname{id}),$$
> so the value is independent of the representative.
>
> *$\Phi$ covers the identity and is fibrewise linear.* By construction $\pi_E(\Phi([e, x])) = \pi(e) = \pi_{\rho_{\mathrm{st}}}([e, x])$, so $\Phi$ covers $\operatorname{id}_M$. Fix $m$ and any frame $e_0 \in \operatorname{Fr}(E_m)$; every element of the fibre $(\operatorname{Fr}(E) \times_{\rho_{\mathrm{st}}} \mathbb{R}^k)_m$ is $[e_0, x]$ for a unique $x \in \mathbb{R}^k$ (existence: any frame is $e_0 g$, and $[e_0 g, y] = [e_0, g y]$; uniqueness: $[e_0, x] = [e_0, x']$ forces $x = \rho_{\mathrm{st}}(g) x'$ with $e_0 = e_0 g$, so $g = \operatorname{id}$ by freeness and $x = x'$). On this fibre the vector-space operations are $[e_0, x] + [e_0, y] = [e_0, x + y]$ and $c[e_0, x] = [e_0, c x]$, and $\Phi([e_0, x]) = e_0(x)$; since $e_0 : \mathbb{R}^k \to E_m$ is a linear map, $\Phi_m$ is linear, and since $e_0$ is a linear *isomorphism*, $\Phi_m$ is a bijection. Thus $\Phi$ is a fibrewise linear isomorphism.
>
> *$\Phi$ is smooth with smooth inverse.* Over $U_\alpha$ use the trivialisation $\Psi_\alpha^{-1}(m, x) = [e_\alpha(m), x]$ of the associated bundle and the trivialisation $\phi_\alpha(v) = (m, e_\alpha(m)^{-1} v)$ of $E$. Then for $(m, x) \in U_\alpha \times \mathbb{R}^k$,
> $$\phi_\alpha\big(\Phi(\Psi_\alpha^{-1}(m, x))\big) = \phi_\alpha\big(e_\alpha(m)(x)\big) = \big(m,\, e_\alpha(m)^{-1} e_\alpha(m)(x)\big) = (m, x),$$
> so $\phi_\alpha \circ \Phi \circ \Psi_\alpha^{-1} = \operatorname{id}_{U_\alpha \times \mathbb{R}^k}$. Being the identity in these trivialisations, $\Phi$ is smooth over each $U_\alpha$, hence smooth, and its inverse is $\Phi^{-1} = \Psi_\alpha^{-1} \circ \phi_\alpha$ over $U_\alpha$, also smooth. Therefore $\Phi$ is an isomorphism of vector bundles.
>
> *Transition-function corroboration.* Independently, by **Lemma 2** the associated bundle has transition functions $\rho_{\mathrm{st}} \circ g_{\alpha\beta} = g_{\alpha\beta} = \tau_{\alpha\beta}$ (using $\rho_{\mathrm{st}} = \operatorname{id}$ and **Lemma 1**), which are exactly the transition functions of $E$; **Lemma 3** then yields the isomorphism, and the "identity in coordinates" map it produces is precisely $\Phi$.
>
> ---
>
> **Part (b) — exterior powers of the dual.**
>
> *Define the map.* Set $\Phi_p : \operatorname{Fr}(E) \times_{\Lambda^p \rho_{\mathrm{st}}^*} \Lambda^p(\mathbb{R}^k)^* \to \Lambda^p E^*$ by
> $$\Phi_p([e, \alpha])(v_1, \dots, v_p) := \alpha\big(e^{-1} v_1, \dots, e^{-1} v_p\big), \qquad v_1, \dots, v_p \in E_{\pi(e)},$$
> where $e^{-1} : E_{\pi(e)} \to \mathbb{R}^k$. This is alternating and multilinear in $(v_1, \dots, v_p)$ because $\alpha$ is and $e^{-1}$ is linear, so $\Phi_p([e, \alpha]) \in \Lambda^p E_{\pi(e)}^*$.
>
> *Well defined on classes.* Write $\rho := \Lambda^p \rho_{\mathrm{st}}^*$, so $(\rho(g)\beta)(y_1, \dots, y_p) = \beta(g^{-1} y_1, \dots, g^{-1} y_p)$ for $\beta \in \Lambda^p(\mathbb{R}^k)^*$ (the convention of the [[Def - Constructions on Representations|constructions on representations]], matching Haydys's Example 33; see the Convention callout). Suppose $[e, \alpha] = [e', \alpha']$, so $e' = e g$ and $\alpha' = \rho(g^{-1}) \alpha$, that is, $\alpha'(y_1, \dots, y_p) = \alpha(g y_1, \dots, g y_p)$. Using $(e g)^{-1} = g^{-1} e^{-1}$,
> $$\Phi_p([e', \alpha'])(v_1, \dots, v_p) = \alpha'\big((e g)^{-1} v_1, \dots\big) = \alpha'\big(g^{-1} e^{-1} v_1, \dots\big) \qquad (\text{since } (eg)^{-1} = g^{-1} e^{-1})$$
> $$= \alpha\big(g\, g^{-1} e^{-1} v_1, \dots, g\, g^{-1} e^{-1} v_p\big) = \alpha\big(e^{-1} v_1, \dots, e^{-1} v_p\big) \qquad (\text{definition of } \alpha' = \rho(g^{-1})\alpha;\ g g^{-1} = \operatorname{id})$$
> $$= \Phi_p([e, \alpha])(v_1, \dots, v_p).$$
> The two inverses — one from the class relation ($\alpha' = \rho(g^{-1})\alpha$ inserts a $g$), one from the change of frame ($(eg)^{-1}$ inserts a $g^{-1}$) — cancel exactly. So $\Phi_p$ is well defined.
>
> *Fibrewise linear isomorphism.* $\Phi_p$ covers $\operatorname{id}_M$ by construction. Fix $m$ and a frame $e_0 \in \operatorname{Fr}(E_m)$; as in part (a) every fibre element is $[e_0, \alpha]$ for a unique $\alpha \in \Lambda^p(\mathbb{R}^k)^*$, and $\Phi_p([e_0, \alpha]) = \alpha(e_0^{-1}\,\cdot, \dots)$. The assignment $\alpha \mapsto \alpha(e_0^{-1}\,\cdot, \dots)$ is the pullback isomorphism $\Lambda^p (e_0^{-1})^* : \Lambda^p(\mathbb{R}^k)^* \to \Lambda^p E_m^*$ induced by the linear isomorphism $e_0^{-1} : E_m \to \mathbb{R}^k$; being the $p$-th exterior power of the transpose of an isomorphism, it is a linear isomorphism. Hence $\Phi_p$ is a fibrewise linear isomorphism.
>
> *Smoothness and transition functions.* By **Lemma 2** the associated bundle has transition functions $\Lambda^p \rho_{\mathrm{st}}^* \circ \tau_{\alpha\beta} = \Lambda^p\big((\tau_{\alpha\beta}^{-1})^t\big)$, using $\rho_{\mathrm{st}}^*(g) = (g^{-1})^t$; these are exactly the transition functions of $\Lambda^p E^*$ recorded in the Notation section and proved on [[Def - Operations on Vector Bundles and Pull-Back Bundles]]. By **Lemma 3** the two bundles are canonically isomorphic, and the "identity in coordinates" isomorphism it produces is $\Phi_p$ (in the frame-induced trivialisations both bundles read $\alpha$ off in the frame $e_\alpha$, and $\Phi_p$ becomes the identity), so $\Phi_p$ is smooth with smooth inverse. Therefore $\Phi_p$ is an isomorphism of vector bundles, and in particular $p = 1$ gives $\operatorname{Fr}(E) \times_{\rho_{\mathrm{st}}^*} (\mathbb{R}^k)^* \cong E^*$.
>
> ---
>
> **Part (c) — all tensor constructions.**
>
> The uniform argument is: the construction $C$ on the vector bundle side (dual, $\Lambda^p$, $\oplus$, $\otimes$, $\operatorname{Hom}$, $\operatorname{End}$) has transition functions $C(\tau_{\alpha\beta})$ (and $C(\tau_{\alpha\beta}, \sigma_{\alpha\beta})$ for two-bundle constructions), listed in the Notation section and proved on [[Def - Operations on Vector Bundles and Pull-Back Bundles]]; the corresponding construction on the standard representation is the representation $\rho_C$ with $\rho_C(g) = C(g)$ (and $\rho_C(g, g') = C(g, g')$), by the [[Def - Constructions on Representations|constructions on representations]]. By **Lemma 2** the associated bundle $\operatorname{Fr}(E) \times_{\rho_C} V_C$ has transition functions $\rho_C \circ \tau_{\alpha\beta} = C(\tau_{\alpha\beta})$, equal to those of $C(E)$; by **Lemma 3** the two are canonically isomorphic. We record the representations and the explicit intertwiners.
>
> *Dual $E^*$.* $\rho = \rho_{\mathrm{st}}^*$, transition $(\tau_{\alpha\beta}^{-1})^t$; this is the $p = 1$ case of part (b). Explicit map $[e, \xi] \mapsto \xi \circ e^{-1} \in E_m^*$.
>
> *Exterior power $\Lambda^p E$.* $\rho = \Lambda^p \rho_{\mathrm{st}}$, transition $\Lambda^p \tau_{\alpha\beta}$. Explicit map $[e, x_1 \wedge \dots \wedge x_p] \mapsto e(x_1) \wedge \dots \wedge e(x_p)$, extended linearly; well defined because $[e g, \Lambda^p(g^{-1})\omega] \mapsto \Lambda^p(e g)(\Lambda^p(g^{-1})\omega) = \Lambda^p(e)\omega$ for $\omega \in \Lambda^p \mathbb{R}^k$, using $\Lambda^p(eg) = \Lambda^p(e)\Lambda^p(g)$ and $\Lambda^p(g)\Lambda^p(g^{-1}) = \operatorname{id}$.
>
> *Direct sum $E \oplus F$.* On $\operatorname{Fr}(E) \times_M \operatorname{Fr}(F)$ with $\rho = \rho_{\mathrm{st}} \oplus \rho_{\mathrm{st}}$, transition $\tau_{\alpha\beta} \oplus \sigma_{\alpha\beta}$. Explicit map $[(e, f), (x, y)] \mapsto e(x) \oplus f(y) \in E_m \oplus F_m$; well defined under $(g, g') \in GL_k \times GL_l$ since $(e g)(g^{-1} x) \oplus (f g')(g'^{-1} y) = e(x) \oplus f(y)$.
>
> *Tensor product $E \otimes F$.* On $\operatorname{Fr}(E) \times_M \operatorname{Fr}(F)$ with $\rho = \rho_{\mathrm{st}} \otimes \rho_{\mathrm{st}}$, transition $\tau_{\alpha\beta} \otimes \sigma_{\alpha\beta}$. Explicit map $[(e, f), x \otimes y] \mapsto e(x) \otimes f(y)$, extended linearly; well defined because $\big((e g) \otimes (f g')\big)\big((g^{-1} \otimes g'^{-1})(x \otimes y)\big) = e(x) \otimes f(y)$ (the two group elements cancel in each factor).
>
> *Homomorphisms $\operatorname{Hom}(E, F)$.* On $\operatorname{Fr}(E) \times_M \operatorname{Fr}(F)$ with $\rho = \rho_{\mathrm{st}}^* \otimes \rho_{\mathrm{st}}$ on $\operatorname{Hom}(\mathbb{R}^k, \mathbb{R}^l)$, acting by $\rho(g, g') T = g' T g^{-1}$; transition $\phi \mapsto \sigma_{\alpha\beta} \phi \tau_{\alpha\beta}^{-1}$. Explicit map $[(e, f), T] \mapsto f \circ T \circ e^{-1} \in \operatorname{Hom}(E_m, F_m)$; well defined since $(f g') (g' ^{-1} T g)(e g)^{-1} = f g' g'^{-1} T g g^{-1} e^{-1} = f T e^{-1}$.
>
> *Endomorphisms $\operatorname{End}(E)$.* $\rho = \operatorname{Ad}$, $\operatorname{Ad}(g) A = g A g^{-1}$ on $M_k(\mathbb{R}) \cong \operatorname{End}(\mathbb{R}^k)$; transition $\phi \mapsto \tau_{\alpha\beta} \phi \tau_{\alpha\beta}^{-1}$. Explicit map $\Phi([e, A]) := e \circ A \circ e^{-1} \in \operatorname{End}(E_m)$. This is well defined: if $[e, A] = [e g, g^{-1} A g]$ then
> $$(e g) \circ (g^{-1} A g) \circ (e g)^{-1} = e g g^{-1} A g g^{-1} e^{-1} = e A e^{-1} \qquad (g g^{-1} = \operatorname{id};\ (eg)^{-1} = g^{-1} e^{-1}).$$
> It is fibrewise a linear isomorphism (conjugation by the isomorphism $e$ is an isomorphism $\operatorname{End}(\mathbb{R}^k) \to \operatorname{End}(E_m)$) and smooth in frame-induced trivialisations by the same computation as in part (a). This is exactly Haydys's Exercise 35, worked in full on [[Ex - End(E) as an Associated Bundle of the Frame Bundle]]; in particular $\operatorname{End}(E) = \operatorname{ad}\operatorname{Fr}(E)$, the adjoint bundle of the frame bundle ([[Def - Adjoint Bundles ad P and Ad P]]).
>
> In every case, well-definedness and fibrewise bijectivity are checked exactly as displayed, and smoothness (with smooth inverse) follows from **Lemma 3** because the transition functions match; so each construction on $E$ is the associated bundle of the same construction on the standard representation. $\blacksquare$ *(part (c))*
>
> ---
>
> **Part (d) — reduction to a $G'$-structure.**
>
> Let $G' \le GL_k(\mathbb{R})$ be closed and $P' \subset \operatorname{Fr}(E)$ a $G'$-structure, that is, a $G'$-subbundle of $\operatorname{Fr}(E)$ in the sense of [[Def - Reduction and Extension of the Structure Group]]; by that definition $P'$ is itself a principal $G'$-bundle over $M$ (with the restricted right action and local sections), and $P'_m \ne \varnothing$ for every $m$ because $P' \to M$ is surjective. Give $\mathbb{R}^k$ the restricted representation $\rho_{\mathrm{st}}|_{G'}$.
>
> *Define the map.* Set $\Phi' : P' \times_{G'} \mathbb{R}^k \to E$, $\Phi'([p, x]) := p(x)$, where $p \in P' \subset \operatorname{Fr}(E)$ is a frame, hence an isomorphism $\mathbb{R}^k \to E_{\pi(p)}$.
>
> *Well defined.* If $[p, x] = [p', x']$ with $p' = p g$, $x' = g^{-1} x$ for $g \in G'$, then $p'(x') = (p g)(g^{-1} x) = p(x)$ exactly as in part (a); the only change is that $g$ now ranges over $G'$, which is a subset of $GL_k(\mathbb{R})$, so the same identity holds.
>
> *Fibrewise linear isomorphism.* $\Phi'$ covers $\operatorname{id}_M$. Fix $m$; since $P'_m \ne \varnothing$, choose $p_0 \in P'_m$. Every element of $(P' \times_{G'} \mathbb{R}^k)_m$ is $[p_0, x]$ for a unique $x$ (existence and uniqueness as in part (a), now with $G'$ acting freely and transitively on $P'_m$ because $P'$ is a principal $G'$-bundle), and $\Phi'([p_0, x]) = p_0(x)$. As $p_0 : \mathbb{R}^k \to E_m$ is a linear isomorphism, $\Phi'_m$ is a linear isomorphism.
>
> *Smoothness.* Over a set $U$ carrying a local section $s : U \to P'$ of the principal $G'$-bundle $P'$ (these exist by [[Thm - Free Proper Actions Give Principal Bundles]]), the associated bundle is trivialised by $(m, x) \mapsto [s(m), x]$, and $E$ is trivialised by the frame $s$ (each $s(m) \in \operatorname{Fr}(E_m)$ is a frame, so $\phi_s(v) = (m, s(m)^{-1} v)$). In these trivialisations $\phi_s(\Phi'([s(m), x])) = \phi_s(s(m)(x)) = (m, x)$, the identity; so $\Phi'$ is smooth with smooth inverse over $U$, hence everywhere. Therefore $\Phi'$ is an isomorphism of vector bundles, $P' \times_{G'} \mathbb{R}^k \cong E$.
>
> *Consistency with part (a).* Equivalently, the inclusion $\iota : P' \hookrightarrow \operatorname{Fr}(E)$ is $G'$-equivariant, so it induces a bundle map $P' \times_{G'} \mathbb{R}^k \to \operatorname{Fr}(E) \times_{GL_k(\mathbb{R})} \mathbb{R}^k$, $[p, x] \mapsto [\iota(p), x]$, which composed with the isomorphism $\Phi$ of part (a) is exactly $\Phi'$; this exhibits $\Phi'$ as an isomorphism onto $E$ once more.
>
> This completes all four parts. $\blacksquare$

---

# Cross-Field Exercise Suggestions

**Orientation as a line bundle (differential topology).** Realise the orientation line bundle of a manifold $M^n$ as $\operatorname{or}_M = \operatorname{Fr}(TM) \times_{\operatorname{sgn} \det} \mathbb{R}$, the associated bundle of the one-dimensional representation $g \mapsto \operatorname{sgn}\det(g)$, and prove that $M$ is orientable if and only if $\operatorname{or}_M$ is trivial if and only if the frame bundle reduces to $GL_n^+(\mathbb{R})$. The theorem applies because $\operatorname{or}_M$ is by definition glued from the signs of the Jacobian transition functions of $TM$, which are $\operatorname{sgn}\det \tau_{\alpha\beta}$; recognising this as an associated bundle is what connects orientability (a topological property) to a reduction of structure group (part (d)). It is non-obvious because the sign representation is not one usually written down, yet it packages orientability exactly.

**Density bundles and integration (analysis on manifolds).** Show that the bundle of $1$-densities on $M^n$ is $\operatorname{Fr}(TM) \times_{|\det|^{-1}} \mathbb{R}$ (representation $g \mapsto |\det g|^{-1}$), so that a density is a section that transforms by the absolute Jacobian and can therefore be integrated on *any* manifold, orientable or not. The theorem applies because the transition functions of the density bundle are $|\det \tau_{\alpha\beta}|^{-1}$, an associated cocycle; the payoff, non-obvious to someone who has only seen top forms, is that integration needs the absolute-value representation, not $\Lambda^n T^* M$, when orientation is unavailable.

**Spinor bundles (mathematical physics).** On a spin manifold, a spin structure is a reduction of the orthonormal frame bundle $O(TM)$ to $\operatorname{Spin}(n)$ along the double cover $\operatorname{Spin}(n) \to SO(n)$, and the spinor bundle is the associated bundle of the (genuine, non-descending-to-$SO$) spin representation $\Delta$. The theorem's framework applies because the spinor bundle *cannot* be a tensor bundle of $TM$ — the spin representation does not factor through $SO(n)$ — so it exists only as an associated bundle of the reduced spin frame bundle. This is the sharpest illustration that the associated-bundle construction produces bundles unreachable by the tensor operations of part (c), and it is exactly why spin structures are needed (chapter VIII).

---

# Bridges

- **Connections downstairs from connections upstairs.** Because $E \cong \operatorname{Fr}(E) \times_{\rho_{\mathrm{st}}} \mathbb{R}^k$, a principal connection on $\operatorname{Fr}(E)$ — a $\mathfrak{gl}_k$-valued equivariant horizontal one-form — induces a covariant derivative on $E$ by differentiating equivariant $\mathbb{R}^k$-valued functions, and every covariant derivative arises this way. Concretely, the local connection matrix $A_\alpha = \sigma_\alpha^* \omega$ pulled back along a frame $\sigma_\alpha = e_\alpha$ is exactly the connection matrix $A$ of the induced connection in that frame, and the change-of-frame law $A_{\alpha} = \operatorname{Ad}_{g_{\alpha\beta}} A_\beta + g_{\alpha\beta}^{-1} d g_{\alpha\beta}$ is the same on both sides because $g_{\alpha\beta} = \tau_{\alpha\beta}$ by Lemma 1. This is the construction of chapter IV, and the present theorem is its prerequisite: without it there would be two unrelated notions of connection.

- **The gauge group as sections of a group bundle.** The automorphisms of $E$ over $M$ (the gauge transformations of the vector bundle) are the sections of $\operatorname{Aut}(E) = \operatorname{Fr}(E) \times_\alpha GL_k(\mathbb{R})$, the associated bundle of the conjugation action of $GL_k(\mathbb{R})$ on itself, and their infinitesimal versions are the sections of $\operatorname{End}(E) = \operatorname{Fr}(E) \times_{\operatorname{Ad}} \mathfrak{gl}_k = \operatorname{ad}\operatorname{Fr}(E)$ from part (c). This identification, developed on [[Def - Adjoint Bundles ad P and Ad P]] and used throughout chapter V, is why the curvature transforms in the adjoint and why the Yang–Mills functional is gauge invariant.

- **Characteristic classes are representation data.** For a Hermitian line bundle $L = P \times_{\varrho_1} \mathbb{C}$ associated to a principal $U(1)$-bundle $P$ via the weight-one representation $\varrho_1$, the tensor powers $L^{\otimes k} = P \times_{\varrho_k} \mathbb{C}$ are the associated bundles of the weight-$k$ representations (chapter I's classification of representations of $U(1)$), and their first Chern classes are $k \, c_1(L)$; this is part (c) specialised to line bundles, and it is the computational backbone of the classification of $U(1)$-bundles on [[Thm - Classification of Principal U(1)-Bundles by the First Chern Class]] and of Chern–Weil theory in chapter VI.

---

# Unlocked by This

> [!tip] The Borel–Weil dictionary *(from Representation Theory)*
> On a flag manifold $G/B$, holomorphic line bundles are associated bundles of characters of $B$, and their spaces of holomorphic sections are irreducible representations of $G$. The associated-bundle construction of this theorem is the geometric half of that dictionary, run in reverse: representations become bundles, and the global sections of the bundles recover representations. See **Def - Associated Bundle** and the sections-are-equivariant-functions theorem [[Thm - Sections of an Associated Bundle are Equivariant Functions]].

> [!tip] Tautological and Hopf bundles as associated bundles *(from Algebraic Topology)*
> The tautological line bundle $\mathcal{O}(-1) \to \mathbb{CP}^n$ is the bundle associated to the Hopf $U(1)$-bundle $S^{2n+1} \to \mathbb{CP}^n$ by the standard weight-one representation, and its dual $\mathcal{O}(1)$ by the weight-$(-1)$ representation. This is part (a) for the Hopf bundle, worked on [[Ex - The Tautological Line Bundle over CP^n is Associated to the Hopf Bundle]].
