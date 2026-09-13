---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - Gauge Variation of the Chern-Simons Functional"
  - "Thm - Sections of a Principal Bundle and Triviality"
  - "Thm - Transformation of Local Connection and Curvature Forms"
  - "Def - Chern-Simons Functional"
  - "Def - Gauge Transformation"
tags: [geometry, gauge-theory]
---

# Problem Statement

Throughout, $M$ is a closed oriented three-dimensional manifold, $G = SU(2)$, and $P \to M$ is a principal $SU(2)$-bundle; by the classification of principal $SU(2)$-bundles over a manifold of dimension at most three, $P$ is trivial. The three-dimensional formula for the **Chern–Simons functional** requires a chosen trivialisation of $P$: once a trivialisation is fixed, a connection on $P$ becomes a one-form $A \in \Omega^1(M; \mathfrak{su}(2))$ and one sets
$$\vartheta_{\text{triv}}(A) := \frac{1}{8\pi^2} \int_M \operatorname{tr}\!\Big(A \wedge dA + \tfrac{2}{3}\, A \wedge A \wedge A\Big) \in \mathbb{R},$$
where $\operatorname{tr}$ is the matrix trace on $2\times2$ matrices and $\mathfrak{su}(2)$ is the space of trace-free skew-Hermitian $2\times2$ matrices. The subscript records that the real number produced depends, a priori, on the trivialisation used to write $A$ down.

Fix a single connection on $P$ and two trivialisations. In the first trivialisation the connection is represented by the form $A \in \Omega^1(M; \mathfrak{su}(2))$; in the second it is represented by some form $A' \in \Omega^1(M; \mathfrak{su}(2))$. Prove Haydys's Exercise 96(c):

> The two values of the Chern–Simons functional differ by an integer:
> $$\vartheta_{\text{triv}_2}(A') - \vartheta_{\text{triv}_1}(A) \in \mathbb{Z}.$$

Deduce that the Chern–Simons functional descends to a well-defined map $\vartheta : \{\text{connections on }P\} \to \mathbb{R}/\mathbb{Z}$, independent of the chosen trivialisation.

The mechanism you must expose has two parts: first, that two trivialisations of $P$ differ by a smooth **gauge transformation**, that is, a smooth map $g : M \to SU(2)$, under which the coordinate one-form transforms by the gauge action $A' = A \cdot g = g^{-1} A g + g^{-1} dg$; second, that under this transformation the Chern–Simons functional changes by the degree of $g$, an *integer*, so that the ambiguity is exactly a shift by $\mathbb{Z}$.

**Recall:**

The objects in play are the Chern–Simons functional, the correspondence between trivialisations and global sections of a principal bundle, the transformation law of a connection form under a change of section, the gauge action of $g : M \to SU(2)$, and the gauge-variation theorem that supplies the integer.

![[Def - Chern-Simons Functional#The Definition]]

![[Thm - Sections of a Principal Bundle and Triviality#Statement]]

The consequence used below is that a trivialisation of $P$ (a $G$-equivariant diffeomorphism $\Phi : P \xrightarrow{\ \sim\ } M \times SU(2)$) is the same datum as a global smooth section $s : M \to P$, related by $s(x) = \Phi^{-1}(x, e)$ with $e \in SU(2)$ the identity; a trivial bundle admits such sections, and any two are related by the fibrewise group action.

![[Thm - Transformation of Local Connection and Curvature Forms#Statement]]

The one clause used is: if $s' = s \cdot g$ for a smooth $g : M \to SU(2)$, then the connection forms $A_{s} = s^*\omega$ and $A_{s'} = (s')^*\omega$ of a fixed principal connection $\omega$ satisfy $A_{s'} = \operatorname{Ad}_{g^{-1}} A_{s} + g^*\theta$, which for the matrix group $SU(2)$ reads $A_{s'} = g^{-1} A_{s}\, g + g^{-1} dg$, where $\theta = g^{-1} dg$ is the (left) Maurer–Cartan form.

![[Def - Gauge Transformation#The Definition]]

A **gauge transformation** of the trivial bundle $M \times SU(2)$ is equivalently a smooth map $g : M \to SU(2)$, and its right action on connection forms is $A \cdot g = g^{-1} A g + g^{-1} dg$, matching the transformation law above; $SU(2) \cong S^3$, so $g$ has a well-defined Brouwer degree $\deg g \in \mathbb{Z}$.

![[Thm - Gauge Variation of the Chern-Simons Functional#Statement]]

This is the engine of the exercise: for $A \in \Omega^1(M; \mathfrak{su}(2))$ and smooth $g : M \to SU(2)$,
$$\vartheta_{\text{triv}}(A \cdot g) = \vartheta_{\text{triv}}(A) + \deg g \quad\text{in } \mathbb{R}, \qquad \deg g \in \mathbb{Z}.$$
Its proof (on [[Thm - Gauge Variation of the Chern-Simons Functional|that theorem's page]]) expands the Chern–Simons three-form of $A \cdot g$, identifies the change as an exact term plus $-\tfrac13\operatorname{tr}((g^{-1}dg)^3)$, kills the exact term by Stokes on the closed manifold $M$, and evaluates $-\tfrac{1}{24\pi^2}\int_M \operatorname{tr}((g^{-1}dg)^3) = \deg g$ using that $\operatorname{tr}((g^{-1}dg)^3)$ is (a multiple of) the pull-back of the bi-invariant volume form of $SU(2) \cong S^3$ with total mass $24\pi^2$. We import that result as a whole and add only what it does not contain: the identification of "change of trivialisation" with "gauge transformation".

---

# Convergent Strategy

**Problem class.** This is a *well-definedness* problem: an object ($\vartheta$) is defined by a formula that refers to an auxiliary choice (a trivialisation), and we must show the value is independent of that choice — here, independent modulo $\mathbb{Z}$. The universal shape of such a proof is: (i) parametrise the set of choices by a group of ambiguities; (ii) compute how the formula changes when the choice is moved by an element of that group; (iii) show the change lies in the subgroup one is quotienting by. The set of trivialisations of $P$ is a torsor under the gauge group $\{g : M \to SU(2)\}$, and the change in $\vartheta$ under $g$ is $\deg g$, which lands in $\mathbb{Z}$ — precisely the group we quotient by.

**Assumption pattern.** The proof uses three standing hypotheses in three distinct ways. Triviality of $P$ (from the classification of $SU(2)$-bundles over a three-manifold) guarantees that trivialisations exist at all, so the three-dimensional formula makes sense. Closedness of $M$ is used inside the gauge-variation theorem to discard the exact term by Stokes. Three-dimensionality (together with $SU(2) \cong S^3$) is what makes $\deg g$ a well-defined *integer*: a smooth map from the closed oriented three-manifold $M$ to the closed oriented three-manifold $S^3$ has an integer degree.

**Theorem routing.** The route is short because the analytic heavy lifting is delegated. First, use [[Thm - Sections of a Principal Bundle and Triviality|the sections–triviality correspondence]] to turn the two trivialisations into two global sections $s_1, s_2$ of $P$; then use that $SU(2)$ acts freely and transitively on each fibre to produce a unique smooth $g : M \to SU(2)$ with $s_2 = s_1 \cdot g$. Next, use [[Thm - Transformation of Local Connection and Curvature Forms|the transformation law]] to conclude that the two coordinate forms of the fixed connection satisfy $A' = A \cdot g = g^{-1} A g + g^{-1} dg$. Finally, feed $A' = A \cdot g$ into [[Thm - Gauge Variation of the Chern-Simons Functional|the gauge-variation theorem]]: $\vartheta_{\text{triv}_2}(A') - \vartheta_{\text{triv}_1}(A) = \deg g \in \mathbb{Z}$. The descent to $\mathbb{R}/\mathbb{Z}$ is then immediate.

**Key decision point.** The one non-obvious identification is *"changing the trivialisation" $=$ "acting by a gauge transformation"*. It is tempting to think of a trivialisation as unrelated to the gauge group, but the two are the same object seen from two sides: a trivialisation is a global section, two global sections of a principal bundle differ by a unique fibrewise group element (because the structure group acts freely and transitively on fibres), and that fibrewise element, varying smoothly, *is* a gauge transformation $g : M \to SU(2)$. Once this is seen, the exercise reduces to the gauge-variation theorem, and the only remaining content is that $\deg g$ is an integer — which is why the change is invisible in $\mathbb{R}/\mathbb{Z}$. A secondary point worth noticing: the *sign* with which $\deg g$ enters (fixed by the orientation conventions on the page of the gauge-variation theorem) is irrelevant to this exercise, because well-definedness needs only that the change lies in $\mathbb{Z}$, and $\mathbb{Z} = -\mathbb{Z}$.

---

# Legal Operations Used

This solution deploys the following legal operations of the chapter (referred to descriptively; the orchestrator reconciles numbering against the topic page's Legal Operations):

1. **Turn a trivialisation into a global section.** By [[Thm - Sections of a Principal Bundle and Triviality|the sections–triviality correspondence]], each trivialisation $\Phi_i : P \xrightarrow{\sim} M \times SU(2)$ is repackaged as the global section $s_i(x) = \Phi_i^{-1}(x, e)$.

2. **Extract the comparison gauge transformation from a free transitive action.** Since $SU(2)$ acts freely and transitively on each fibre of $P$, there is a unique $g(x) \in SU(2)$ with $s_2(x) = s_1(x) \cdot g(x)$; smoothness of $s_1, s_2$ makes $g : M \to SU(2)$ smooth.

3. **Transform the connection form under a change of section.** By [[Thm - Transformation of Local Connection and Curvature Forms|the transformation law]], the two coordinate forms of the *same* connection satisfy $A' = g^{-1} A g + g^{-1} dg = A \cdot g$, the gauge action.

4. **Apply the gauge-variation theorem to convert the change into a degree.** By [[Thm - Gauge Variation of the Chern-Simons Functional|the gauge-variation theorem]], $\vartheta_{\text{triv}_2}(A') = \vartheta_{\text{triv}_1}(A) + \deg g$.

5. **Use integrality of the degree to descend to $\mathbb{R}/\mathbb{Z}$.** Since $g : M \to SU(2) \cong S^3$ is a smooth map between closed oriented three-manifolds, $\deg g \in \mathbb{Z}$; hence the two values agree in $\mathbb{R}/\mathbb{Z}$, and $\vartheta$ is trivialisation-independent as an $\mathbb{R}/\mathbb{Z}$-valued map.

---

# Hints

> [!note]- Hint 1
> The Chern–Simons number $\vartheta_{\text{triv}}(A)$ is computed from the coordinate one-form $A$, which exists only after a trivialisation is chosen. So the real question is: if you keep the connection fixed but change the trivialisation, how does the coordinate form $A$ change? What is the relationship between two trivialisations of the *same* bundle?

> [!note]- Hint 2
> A trivialisation is a global section (or, equivalently, an equivariant identification $P \cong M \times SU(2)$). Two global sections $s_1, s_2$ of a principal bundle are related by a fibrewise group element: at each $x$ there is a unique $g(x) \in SU(2)$ with $s_2(x) = s_1(x) \cdot g(x)$, because the group acts freely and transitively on the fibre. What kind of object is $x \mapsto g(x)$?

> [!note]- Hint 3
> The map $g : M \to SU(2)$ is a gauge transformation. Under a change of section $s_2 = s_1 \cdot g$, the connection form transforms by the standard law $A' = g^{-1} A g + g^{-1} dg$. You have now reduced the problem to: how does $\vartheta_{\text{triv}}$ change when $A$ is replaced by $A \cdot g = g^{-1} A g + g^{-1} dg$? There is a theorem for exactly this.

> [!note]- Hint 4
> The gauge-variation theorem says $\vartheta_{\text{triv}}(A \cdot g) = \vartheta_{\text{triv}}(A) + \deg g$. So the two values differ by $\deg g$. Why is $\deg g$ an integer, and why does that finish the problem for the $\mathbb{R}/\mathbb{Z}$-valued functional? (You do not even need to know the sign of $\deg g$: $\mathbb{Z}$ is closed under negation.)

---

# Solution

The plan is to recognise a change of trivialisation as the action of a gauge transformation $g : M \to SU(2)$, to transport this recognition to the coordinate connection forms via the standard transformation law, and then to invoke the gauge-variation theorem, whose entire output is that $\vartheta$ shifts by the integer $\deg g$. Integrality of $\deg g$ then collapses the ambiguity to zero in $\mathbb{R}/\mathbb{Z}$. All the computation lives in the gauge-variation theorem; the work here is the identification of the ambiguity group and the bookkeeping of the transformation law.

**Step 1: Two trivialisations differ by a gauge transformation $g : M \to SU(2)$.**

The two trivialisations correspond to global sections $s_1, s_2$ of $P$, and there is a unique smooth $g : M \to SU(2)$ with $s_2 = s_1 \cdot g$.

> [!note]- Derivation
> Let the two trivialisations be the $G$-equivariant diffeomorphisms $\Phi_1, \Phi_2 : P \xrightarrow{\sim} M \times SU(2)$. By [[Thm - Sections of a Principal Bundle and Triviality|the sections–triviality correspondence]], each determines a global smooth section
> $$s_i : M \to P, \qquad s_i(x) := \Phi_i^{-1}(x, e) \quad (i = 1, 2),$$
> where $e \in SU(2)$ is the identity, and conversely every trivialisation arises this way. Now fix $x \in M$. The right action of $SU(2)$ on the fibre $P_x$ is **free and transitive** (this is part of the definition of a principal bundle): free means $p \cdot h = p$ forces $h = e$, and transitive means for any two points $p, q \in P_x$ there is $h \in SU(2)$ with $q = p \cdot h$. Applying transitivity to $p = s_1(x)$ and $q = s_2(x)$ produces some $h$ with $s_2(x) = s_1(x) \cdot h$; applying freeness shows this $h$ is unique. Call it $g(x)$, so that
> $$s_2(x) = s_1(x) \cdot g(x), \qquad g(x) \in SU(2), \text{ uniquely determined.}$$
> **Smoothness of $g$.** In the first trivialisation write $\Phi_1(s_2(x)) = (x, \gamma(x))$ for a map $\gamma : M \to SU(2)$; since $s_2$ and $\Phi_1$ are smooth, $\gamma$ is smooth. Because $\Phi_1$ is equivariant and $\Phi_1(s_1(x)) = (x, e)$, the relation $s_2(x) = s_1(x) \cdot g(x)$ reads $\Phi_1(s_2(x)) = (x, e \cdot g(x)) = (x, g(x))$ in the trivialisation, so $g = \gamma$ is smooth. Thus $g : M \to SU(2)$ is a smooth map — a **gauge transformation** of $P$ in the sense of [[Def - Gauge Transformation|the gauge-transformation definition]].

**Step 2: The two coordinate connection forms are related by the gauge action.**

If $A$ and $A'$ are the coordinate forms of the fixed connection in the two trivialisations, then $A' = g^{-1} A g + g^{-1} dg = A \cdot g$.

> [!note]- Derivation
> Let $\omega \in \Omega^1(P; \mathfrak{su}(2))$ be the connection one-form of the fixed connection on $P$. The coordinate form in trivialisation $i$ is the pull-back along the corresponding section,
> $$A := s_1^* \omega, \qquad A' := s_2^* \omega,$$
> both in $\Omega^1(M; \mathfrak{su}(2))$; this is exactly how a chosen trivialisation turns a principal connection into a matrix-valued one-form on $M$. By Step 1, $s_2 = s_1 \cdot g$. Applying [[Thm - Transformation of Local Connection and Curvature Forms|the transformation law of local connection forms]] to the change of section $s' = s \cdot g$, with $s = s_1$ and $s' = s_2$,
> $$A' = s_2^*\omega = \operatorname{Ad}_{g^{-1}} (s_1^*\omega) + g^*\theta = \operatorname{Ad}_{g^{-1}} A + g^*\theta \qquad \text{(transformation law; } s_1^*\omega = A).$$
> For the matrix group $SU(2)$, the adjoint action is conjugation, $\operatorname{Ad}_{g^{-1}} A = g^{-1} A g$, and the pull-back of the left Maurer–Cartan form is $g^*\theta = g^{-1} dg$ (both from the standing conventions). Hence
> $$A' = g^{-1} A g + g^{-1} dg \qquad \text{(matrix-group forms of } \operatorname{Ad}_{g^{-1}} \text{ and } g^*\theta).$$
> This is exactly the right gauge action $A \cdot g$ recorded on [[Def - Gauge Transformation|the gauge-transformation page]], so $A' = A \cdot g$.

**Step 3: The two Chern–Simons values differ by $\deg g$.**

Feeding $A' = A \cdot g$ into the gauge-variation theorem gives $\vartheta_{\text{triv}_2}(A') - \vartheta_{\text{triv}_1}(A) = \deg g$.

> [!note]- Derivation
> The number attached to the second trivialisation is $\vartheta_{\text{triv}_2}(A') = \tfrac{1}{8\pi^2}\int_M \operatorname{tr}(A' \wedge dA' + \tfrac23 A' \wedge A' \wedge A')$, i.e. the same formula evaluated on the coordinate form $A'$ of the second trivialisation; likewise $\vartheta_{\text{triv}_1}(A)$ uses $A$. By Step 2, $A' = A \cdot g$, so
> $$\vartheta_{\text{triv}_2}(A') = \vartheta_{\text{triv}_1}(A \cdot g).$$
> Now apply [[Thm - Gauge Variation of the Chern-Simons Functional|the gauge-variation theorem]], whose statement is that for every $A \in \Omega^1(M; \mathfrak{su}(2))$ and every smooth $g : M \to SU(2)$,
> $$\vartheta_{\text{triv}}(A \cdot g) = \vartheta_{\text{triv}}(A) + \deg g.$$
> Substituting,
> $$\vartheta_{\text{triv}_2}(A') = \vartheta_{\text{triv}_1}(A) + \deg g, \qquad\text{i.e.}\qquad \vartheta_{\text{triv}_2}(A') - \vartheta_{\text{triv}_1}(A) = \deg g \qquad \text{(gauge-variation theorem with this } g).$$
> Here $\deg g$ is the Brouwer degree of $g$ viewed as a map $M \to SU(2) \cong S^3$ between closed oriented three-manifolds; the sign convention fixing $\deg g$ versus $-\deg g$ is the one recorded on the gauge-variation theorem's page and plays no role below.

**Step 4: $\deg g \in \mathbb{Z}$, so $\vartheta$ is well defined in $\mathbb{R}/\mathbb{Z}$.**

Because $\deg g$ is an integer, the two real values agree modulo $\mathbb{Z}$; hence $\vartheta$ descends to $\mathbb{R}/\mathbb{Z}$ independently of the trivialisation.

> [!note]- Derivation
> The map $g : M \to SU(2) \cong S^3$ is smooth, and both $M$ (by hypothesis) and $S^3$ are closed oriented three-manifolds, so its Brouwer degree is an **integer**, $\deg g \in \mathbb{Z}$; this integrality is itself part of the conclusion of [[Thm - Gauge Variation of the Chern-Simons Functional|the gauge-variation theorem]] (which in turn cites the general fact that the degree of a smooth map between closed oriented equidimensional manifolds is an integer). By Step 3,
> $$\vartheta_{\text{triv}_2}(A') - \vartheta_{\text{triv}_1}(A) = \deg g \in \mathbb{Z},$$
> which is the required statement that the two values of the Chern–Simons functional differ by an integer — Haydys's Exercise 96(c).
>
> **Descent to $\mathbb{R}/\mathbb{Z}$.** Consider the composite $\bar\vartheta(\text{connection}) := \big[\vartheta_{\text{triv}}(A)\big] \in \mathbb{R}/\mathbb{Z}$, where $A$ is the coordinate form in *any* trivialisation and $[\,\cdot\,]$ is the projection $\mathbb{R} \to \mathbb{R}/\mathbb{Z}$. For two trivialisations the two representatives differ by $\deg g \in \mathbb{Z}$, hence project to the *same* class in $\mathbb{R}/\mathbb{Z}$:
> $$[\vartheta_{\text{triv}_2}(A')] = [\vartheta_{\text{triv}_1}(A) + \deg g] = [\vartheta_{\text{triv}_1}(A)] \qquad \text{(since } \deg g \in \mathbb{Z} = \ker(\mathbb{R} \to \mathbb{R}/\mathbb{Z})).$$
> Therefore $\bar\vartheta$ is independent of the trivialisation: the Chern–Simons functional is a well-defined map from connections on $P$ to $\mathbb{R}/\mathbb{Z}$. (Only integrality was used; the sign of $\deg g$ is immaterial, as $\mathbb{Z}$ is closed under negation.) This is the well-definedness clause invoked on [[Def - Chern-Simons Functional|the Chern–Simons functional's definition page]].

> [!note]- Complete formal solution
> **Claim.** Let $M$ be a closed oriented three-manifold and $P \to M$ a (necessarily trivial) principal $SU(2)$-bundle. If a fixed connection on $P$ is represented by $A$ in one trivialisation and by $A'$ in another, then $\vartheta_{\text{triv}_2}(A') - \vartheta_{\text{triv}_1}(A) \in \mathbb{Z}$; consequently $\vartheta$ is a well-defined $\mathbb{R}/\mathbb{Z}$-valued map on connections.
>
> A trivialisation of $P$ is a global section (sections–triviality correspondence); let $s_1, s_2$ be the sections of the two trivialisations. Since $SU(2)$ acts freely and transitively on each fibre, there is a unique smooth $g : M \to SU(2)$ with $s_2 = s_1 \cdot g$. Writing $A = s_1^*\omega$ and $A' = s_2^*\omega$ for the fixed connection $\omega$, the transformation law of local connection forms gives
> $$A' = \operatorname{Ad}_{g^{-1}} A + g^*\theta = g^{-1} A g + g^{-1} dg = A \cdot g.$$
> By the gauge-variation theorem, $\vartheta_{\text{triv}}(A \cdot g) = \vartheta_{\text{triv}}(A) + \deg g$, hence
> $$\vartheta_{\text{triv}_2}(A') - \vartheta_{\text{triv}_1}(A) = \deg g.$$
> As $g : M \to SU(2) \cong S^3$ is a smooth map between closed oriented three-manifolds, $\deg g \in \mathbb{Z}$, proving the difference is an integer. Projecting to $\mathbb{R}/\mathbb{Z}$, the two representatives coincide, so $[\vartheta_{\text{triv}}(A)] \in \mathbb{R}/\mathbb{Z}$ does not depend on the trivialisation. $\blacksquare$

> [!warning] Illegal but tempting shortcut
> One might try to prove trivialisation-independence directly from the four-dimensional formula $\vartheta(A) \equiv \tfrac{1}{8\pi^2}\int_X \operatorname{tr}(F_{A_X} \wedge F_{A_X}) \pmod{\mathbb{Z}}$, arguing that the right-hand side "never mentions a trivialisation, so there is nothing to check". This is circular: the four-dimensional expression is *itself* only well defined modulo $\mathbb{Z}$, and proving *that* — that two bounding manifolds give integrals differing by an integer — is a separate theorem (part (b) of [[Thm - The Four-Dimensional Formula for the Chern-Simons Functional|the four-dimensional formula]]) which relies on the integrality of the second Chern number, not on the change-of-trivialisation computation. The trivialisation-independence of the *three-dimensional* formula is the genuinely elementary statement, and it is exactly the gauge-variation computation carried out above; it must be established on its own terms, as here, and cannot be borrowed from the four-dimensional formula without circularity.

---

# Key Takeaways

**Well-definedness modulo a lattice is proved by parametrising the choices as a torsor and showing the formula changes by an element of that lattice.** The reusable principle is the three-move template: identify the group of ambiguities that acts on the auxiliary choices (here, gauge transformations $g : M \to SU(2)$ acting on trivialisations); compute the change of the formula under one ambiguity (here, $\vartheta \mapsto \vartheta + \deg g$); and check the change lands in the subgroup being quotiented (here, $\deg g \in \mathbb{Z}$). The trigger to reach for this template is any invariant "defined up to a choice" that is asserted to live in a quotient group $V / \Lambda$: the proof obligation is always "moving the choice changes the representative by an element of $\Lambda$". The same template proves that the Chern–Simons invariant of a flat connection is a well-defined element of $\mathbb{R}/\mathbb{Z}$, that the symplectic action functional is defined modulo the periods of the symplectic form, and that the Wess–Zumino term is defined modulo $2\pi\mathbb{Z}$ — in every case the ambiguity is a topological integer (a degree, a period, a winding number) and the invariant is genuinely valued in a circle rather than a line.

**A change of trivialisation *is* a gauge transformation; the two words describe the same object from the geometry side and the field-theory side.** The single conceptual bridge that unlocks this exercise is that a trivialisation of a principal bundle is a global section, that two sections of a principal bundle differ by a unique fibrewise structure-group element (because the action is free and transitive), and that this fibrewise element, as a smooth function on the base, is precisely what physics calls a gauge transformation. Once this dictionary is internalised, "how does $\vartheta$ depend on the trivialisation?" and "how does $\vartheta$ transform under the gauge group?" are literally the same question, and the answer is the gauge-variation theorem. The transferable diagnostic: whenever a construction requires a local frame, a trivialisation, or a gauge, the dependence on that choice is governed by the transition functions or gauge transformations relating two choices, and the free-transitive action of the structure group is what guarantees a *unique* comparison element to compute with.

**The topological integer that measures the failure of gauge invariance is exactly the obstruction that makes the invariant live in a circle.** The Chern–Simons functional is not gauge invariant as a real number — it shifts by $\deg g$ — and this is not a defect but the source of its meaning: the shift is an integer, so the functional is invariant in $\mathbb{R}/\mathbb{Z}$, and the residual circle-valued invariant is a genuine invariant of the connection up to gauge. This is a recurring pattern in gauge theory and geometric quantisation: an "action" that is multivalued, with the multivaluedness quantised, forces the coupling constant (the "level" $k$ in Chern–Simons theory) to be an integer so that $\exp(2\pi i\, k\, \vartheta)$ is single-valued. The degree of $g$ here is the same integer that appears as the instanton number / second Chern number of the mapping-torus bundle over $M \times S^1$, tying this well-definedness computation to the integrality of characteristic numbers established in [[Thm - Second Chern Number of an SU(2)-Bundle over a Closed Four-Manifold is the Clutching Degree]]. The companion drill [[Ex - The Chern-Simons Functional along a Path of Connections]] shows the complementary fact that *within* a single trivialisation $\vartheta$ varies smoothly and its derivative is the curvature pairing.
