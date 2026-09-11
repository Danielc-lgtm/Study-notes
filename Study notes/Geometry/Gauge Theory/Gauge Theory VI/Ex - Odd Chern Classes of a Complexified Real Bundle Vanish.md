---
type: exercise
subject: gauge-theory
prereqs:
  - "Def - Pontryagin Classes"
  - "Ex - Chern Classes of the Dual Bundle"
  - "Def - Chern Classes"
  - "Ex - Even-Degree Forms Commute and Determinants of Matrices of Even Forms are Multiplicative"
difficulty: "⭐⭐"
tags: [geometry, gauge-theory, characteristic-classes, chern-class, pontryagin-class]
---

# Problem Statement

Let $M$ be a smooth manifold and let $E \to M$ be a smooth **real** vector bundle of rank $n$. Its **complexification** is the complex vector bundle $E \otimes \mathbb{C} \to M$ of complex rank $n$, whose fibre over $m$ is $E_m \otimes_{\mathbb{R}} \mathbb{C} = E_m \oplus i\, E_m$, with $i$ acting as $i(v \otimes z) = v \otimes iz$. Its Chern classes $c_j(E \otimes \mathbb{C}) \in H^{2j}_{dR}(M)$ are defined for $0 \le j \le n$.

**Prove that all odd Chern classes of a complexified real bundle vanish:**
$$\boxed{\,c_j(E \otimes \mathbb{C}) = 0 \in H^{2j}_{dR}(M) \quad \text{for every odd } j.\,}$$

Give **two independent proofs**:

- **(A) via self-conjugacy.** Show that the complexification is isomorphic to its own conjugate, $E \otimes \mathbb{C} \cong \overline{E \otimes \mathbb{C}}$, and combine this with the conjugation rule $c_j(\overline{V}) = (-1)^j c_j(V)$ to force $2\, c_j(E \otimes \mathbb{C}) = 0$ in real cohomology.
- **(B) via traces of odd powers.** Choosing a Euclidean metric and a metric connection on $E$, whose curvature $F$ is a skew-symmetric matrix of $2$-forms in an orthonormal frame, show that $\operatorname{tr}(F^k) = 0$ for every odd $k$, and deduce that the total Chern form $\det\!\big(1 + \tfrac{i}{2\pi}F\big)$ has components only in form-degrees divisible by $4$; hence the odd Chern classes vanish *as forms*, not merely in cohomology.

This is the corollary that makes the definition of the **[[Def - Pontryagin Classes|Pontryagin classes]]** $p_k(E) = (-1)^k c_{2k}(E \otimes \mathbb{C})$ lose no information: the discarded odd Chern classes are already zero.

**Recall.**

The Pontryagin classes, whose well-posedness this drill underwrites:

![[Def - Pontryagin Classes#The Definition]]

The Chern classes as the components of the Chern polynomial of a curvature:

![[Def - Chern Classes#The Definition]]

The conjugation rule for Chern classes, proved on **[[Ex - Chern Classes of the Dual Bundle]]**: for a complex bundle $V$ of rank $r$ with a Hermitian metric, the conjugate bundle $\overline{V}$ (the same real bundle with $I$ replaced by $-I$) satisfies
$$c_j(\overline{V}) = c_j(V^{\vee}) = (-1)^j\, c_j(V) \qquad (0 \le j \le r),$$
because a Hermitian metric gives a complex-linear isomorphism $\overline{V} \cong V^{\vee}$, and the dual connection has curvature $-F^{\mathsf{T}}$, so $\det\!\big(1 + \tfrac{i}{2\pi}(-F^{\mathsf{T}})\big) = \det\!\big(1 - \tfrac{i}{2\pi}F\big)$, whose degree-$2j$ part is $(-1)^j$ times that of $\det\!\big(1 + \tfrac{i}{2\pi}F\big)$.

That matrices whose entries are even-degree differential forms have commuting entries, so their determinants and traces obey the usual scalar identities (multiplicativity, transpose-invariance $\det(N^{\mathsf{T}}) = \det(N)$, and $\operatorname{tr}(N^{\mathsf{T}}) = \operatorname{tr}(N)$), is **[[Ex - Even-Degree Forms Commute and Determinants of Matrices of Even Forms are Multiplicative]]**. That the curvature of a metric connection is skew-symmetric in an orthonormal frame is **[[Def - Euclidean Vector Bundle and Metric Connection]]**. Isomorphism invariance of Chern classes — isomorphic bundles have equal characteristic classes — is **[[Thm - Naturality and Isomorphism Invariance of Characteristic Classes]]**.

---

# Convergent Strategy

**Problem class.** This is a *symmetry-forces-vanishing* problem: a cohomology class is shown to equal its own negative, hence to be zero. Two mechanisms produce the negation. Proof (A) is *global-algebraic*: an isomorphism of the bundle with a twisted copy of itself (its conjugate) transports each $c_j$ to $(-1)^j c_j$. Proof (B) is *local-differential*: the curvature of a complexified real bundle is, in a suitable frame, a real skew matrix, and the trace of an odd power of a skew matrix vanishes, which propagates through the Chern polynomial to kill the odd-degree components pointwise. Both belong to the family "a real structure on a complex bundle constrains its Chern classes".

**Assumption pattern.** The recognisable trigger is the phrase "complexification of a real bundle". Two features are then available and each drives one proof: (i) $E \otimes \mathbb{C}$ carries a *real structure* — the fibrewise complex conjugation $v \otimes z \mapsto v \otimes \bar z$ — which is exactly an isomorphism with the conjugate bundle; and (ii) $E \otimes \mathbb{C}$ admits a connection whose curvature is *real and skew* in an orthonormal frame, namely the complexification of a metric connection on $E$. A general complex bundle has neither feature, which is why a general complex bundle has non-vanishing odd Chern classes; the vanishing here is a strict consequence of the bundle coming from a real one.

**Theorem routing.** For (A): construct $\Phi : E \otimes \mathbb{C} \to \overline{E \otimes \mathbb{C}}$ and check it is a complex-linear isomorphism; quote $c_j(\overline{V}) = (-1)^j c_j(V)$ from **[[Ex - Chern Classes of the Dual Bundle]]**; apply isomorphism invariance from **[[Thm - Naturality and Isomorphism Invariance of Characteristic Classes]]** to get $c_j(E \otimes \mathbb{C}) = (-1)^j c_j(E \otimes \mathbb{C})$; conclude in the real vector space $H^{2j}_{dR}(M)$, where $2x = 0 \Rightarrow x = 0$. For (B): take a metric connection on $E$ with skew curvature $F$ (**[[Def - Euclidean Vector Bundle and Metric Connection]]**); prove the trace lemma $\operatorname{tr}(F^k) = 0$ for odd $k$ using skew-symmetry and transpose-invariance of the trace (**[[Ex - Even-Degree Forms Commute and Determinants of Matrices of Even Forms are Multiplicative]]**); feed it through $\log \det(1 + B) = \operatorname{tr}\log(1 + B)$ to see $\det\!\big(1 + \tfrac{i}{2\pi}F\big)$ has only degrees divisible by $4$; read off from **[[Def - Chern Classes]]** that the degree-$2j$ part, $c_j$, vanishes for odd $j$.

**Key decision point.** In (A), the subtle move is verifying that $\Phi(v \otimes z) = v \otimes \bar z$ is complex-linear *as a map into the conjugate bundle* — on the conjugate side $i$ acts as $-i$, and it is precisely this sign that makes the $\mathbb{R}$-linear (but $\mathbb{C}$-antilinear) conjugation into a genuine $\mathbb{C}$-linear isomorphism; getting this backwards would claim only the vacuous $E \otimes \mathbb{C} \cong E \otimes \mathbb{C}$ and prove nothing. In (B), the subtle move is that the entries of $F$ are $2$-forms, which *commute* under the wedge product, so the transpose identity $(F^k)^{\mathsf{T}} = (F^{\mathsf{T}})^k$ holds exactly as for scalar matrices; without commuting entries the reversal of the product would obstruct the trace argument.

---

# Legal Operations Used

1. **Exploit a real structure to relate a bundle to its conjugate** (a specialisation of the naturality/pullback operation to the conjugation functor). Complexifying a real bundle produces a bundle with a canonical anti-involution; reading that anti-involution as an isomorphism onto the conjugate bundle is the operation that converts "real origin" into the algebraic constraint $E \otimes \mathbb{C} \cong \overline{E \otimes \mathbb{C}}$.

2. **Transport a class along an isomorphism** (isomorphism invariance, [[Thm - Naturality and Isomorphism Invariance of Characteristic Classes]]). Once $E \otimes \mathbb{C} \cong \overline{E \otimes \mathbb{C}}$ is established, isomorphism invariance equates their Chern classes; this is what turns the conjugation rule into a self-referential equation for $c_j$.

3. **Compute a characteristic class from a convenient connection** (connection-independence, licensed by the [[Thm - Chern-Weil Theorem|Chern–Weil theorem]]). In (B) we may use *any* connection on $E \otimes \mathbb{C}$ to represent its Chern classes; we choose the complexification of a metric connection on $E$, precisely so that the curvature is real and skew and the trace lemma applies.

4. **Push an algebraic identity on the curvature matrix through the Chern polynomial** (the "matrix invariant" operation). The scalar-matrix identities $\det(N^{\mathsf{T}}) = \det(N)$ and $\log\det(1 + B) = \operatorname{tr}\log(1 + B)$ remain valid for matrices of even-degree forms because their entries commute ([[Ex - Even-Degree Forms Commute and Determinants of Matrices of Even Forms are Multiplicative]]); applying them lets the pointwise vanishing $\operatorname{tr}(F^{\text{odd}}) = 0$ dictate which form-degrees survive in $\det\!\big(1 + \tfrac{i}{2\pi}F\big)$.

---

# Hints

> [!note]- Hint 1
> Both proofs turn the vanishing into the assertion "$c_j$ equals $(-1)^j c_j$", which for odd $j$ says $c_j = -c_j$. Ask: what feature of a *complexified* bundle (as opposed to an arbitrary complex bundle) would let you relate it to a copy of itself with the Chern classes sign-twisted?

> [!note]- Hint 2 (for Proof A)
> A complex bundle $V$ and its conjugate $\overline{V}$ (same real bundle, $I$ replaced by $-I$) have $c_j(\overline{V}) = (-1)^j c_j(V)$. So it suffices to show $E \otimes \mathbb{C}$ is isomorphic to its own conjugate. Try the fibrewise map $\Phi(v \otimes z) = v \otimes \bar z$. It is real-linear and bijective — the only thing to check is that it is *complex*-linear as a map into $\overline{E \otimes \mathbb{C}}$, where scalar multiplication by $i$ is defined to be multiplication by $-i$.

> [!note]- Hint 3 (for Proof A)
> Check: $\Phi\big(i \cdot (v \otimes z)\big) = \Phi(v \otimes iz) = v \otimes \overline{iz} = v \otimes(-i\bar z) = -i(v \otimes \bar z)$. On the conjugate bundle, "$i$ times $\Phi(v \otimes z)$" *means* $-i \cdot (v \otimes \bar z)$. So $\Phi(i \cdot x) = i \cdot_{\overline{\phantom{x}}} \Phi(x)$: $\Phi$ is $\mathbb{C}$-linear into the conjugate. Now combine $E \otimes \mathbb{C} \cong \overline{E \otimes \mathbb{C}}$ with the conjugation rule and isomorphism invariance, and finish by noting real cohomology has no $2$-torsion.

> [!note]- Hint 4 (for Proof B)
> Put a Euclidean metric and a metric connection on $E$; in an orthonormal frame the curvature $F$ is a skew-symmetric matrix of $2$-forms, $F^{\mathsf{T}} = -F$. The complexified connection on $E \otimes \mathbb{C}$ has the same curvature matrix $F$. Prove the lemma $\operatorname{tr}(F^k) = 0$ for odd $k$: use $\operatorname{tr}(N^{\mathsf{T}}) = \operatorname{tr}(N)$ and $(F^k)^{\mathsf{T}} = (F^{\mathsf{T}})^k$ (valid because $2$-forms commute).

> [!note]- Hint 5 (for Proof B)
> With $\operatorname{tr}(F^k) = 0$ for odd $k$, expand $\log\det\!\big(1 + \tfrac{i}{2\pi}F\big) = \operatorname{tr}\log\!\big(1 + \tfrac{i}{2\pi}F\big) = \sum_{k \ge 1} \frac{(-1)^{k-1}}{k}\big(\tfrac{i}{2\pi}\big)^k \operatorname{tr}(F^k)$ (a *finite* sum: $F^k = 0$ once $2k > \dim M$). Only even $k$ survive, and each surviving term is a form of degree $2k \equiv 0 \pmod 4$. Exponentiate. A form of degree $2j$ with $j$ odd has degree $\equiv 2 \pmod 4$ — can it appear?

---

# Solution

The plan is to prove the same vanishing twice. Proof (A) is a two-line algebraic argument once the isomorphism $E \otimes \mathbb{C} \cong \overline{E \otimes \mathbb{C}}$ is established: the conjugation rule turns it into $c_j = (-1)^j c_j$, which kills odd $c_j$ in torsion-free real cohomology. Proof (B) is a local computation: the curvature of a complexified metric connection is real and skew, so $\operatorname{tr}(F^k) = 0$ for odd $k$, and this restricts the total Chern form to degrees divisible by $4$, killing the odd Chern *forms* outright.

## Proof A — via self-conjugacy

**Step A1: The complexification is isomorphic to its conjugate.** We build the isomorphism from fibrewise conjugation.

> [!note]- Derivation
> Recall that for a complex bundle $V$, the **conjugate bundle** $\overline{V}$ has the same underlying real bundle and the same addition, but scalar multiplication twisted by conjugation: the action of $\lambda \in \mathbb{C}$ on $x \in \overline{V}$, written $\lambda \cdot_{\overline{V}} x$, equals $\bar\lambda \cdot_V x$ (see [[Def - Pontryagin Classes]] and [[Def - Complex Vector Bundle and Hermitian Structure]]). Define the fibrewise map
> $$\Phi : E \otimes \mathbb{C} \longrightarrow \overline{E \otimes \mathbb{C}}, \qquad \Phi(v \otimes z) = v \otimes \bar z \quad (v \in E_m,\ z \in \mathbb{C}),$$
> extended $\mathbb{R}$-linearly. It is $\mathbb{R}$-linear and fibrewise bijective (its own inverse: $\Phi(\Phi(v \otimes z)) = v \otimes \bar{\bar z} = v \otimes z$), and it is smooth because in a real frame of $E$ it is the entrywise complex conjugation of the $\mathbb{C}$-valued components. It remains to check $\mathbb{C}$-linearity *into the conjugate bundle*:
> $$\Phi\big(i \cdot (v \otimes z)\big) = \Phi(v \otimes iz) = v \otimes \overline{iz} = v \otimes (-i\bar z) = -i\,(v \otimes \bar z) \qquad \text{(definition of } \Phi \text{ and } \overline{iz} = -i\bar z),$$
> while on the conjugate side scalar multiplication by $i$ is $i \cdot_{\overline{\phantom{x}}}(v \otimes \bar z) = \bar i\,(v \otimes \bar z) = -i\,(v \otimes \bar z)$ (definition of the conjugate structure). The two agree:
> $$\Phi\big(i \cdot (v \otimes z)\big) = i \cdot_{\overline{\phantom{x}}} \Phi(v \otimes z),$$
> so $\Phi$ is complex-linear as a map into $\overline{E \otimes \mathbb{C}}$. Being a fibrewise $\mathbb{C}$-linear bijection depending smoothly on the base point, $\Phi$ is a bundle isomorphism:
> $$E \otimes \mathbb{C} \;\cong\; \overline{E \otimes \mathbb{C}}. \qquad \square$$
> (The single sign $\overline{iz} = -i\bar z$ is the whole content: fibrewise conjugation is $\mathbb{C}$-antilinear as a self-map of $E \otimes \mathbb{C}$, and reading its target as the conjugate bundle is exactly what converts antilinearity into linearity.)

**Step A2: Force the odd classes to vanish.** We combine the isomorphism with the conjugation rule.

> [!note]- Derivation
> Abbreviate $V := E \otimes \mathbb{C}$. By isomorphism invariance of Chern classes ([[Thm - Naturality and Isomorphism Invariance of Characteristic Classes]], which states that isomorphic complex bundles have equal Chern classes), Step A1 gives
> $$c_j(V) = c_j(\overline{V}) \qquad \text{(isomorphism invariance, } V \cong \overline{V} \text{ from Step A1)}.$$
> By the conjugation rule proved on [[Ex - Chern Classes of the Dual Bundle]] — for a complex bundle $V$, $c_j(\overline{V}) = (-1)^j c_j(V)$ — we substitute:
> $$c_j(V) = (-1)^j c_j(V) \qquad \text{(conjugation rule)}.$$
> For odd $j$ this reads $c_j(V) = -c_j(V)$, hence
> $$2\, c_j(V) = 0 \qquad \text{(adding } c_j(V) \text{ to both sides).}$$
> Since $c_j(V) \in H^{2j}_{dR}(M)$ and $H^{2j}_{dR}(M)$ is a *real* vector space, multiplication by the nonzero scalar $2$ is injective, so $c_j(V) = 0$.
>
> **Conclusion of Proof A.** For every odd $j$, $c_j(E \otimes \mathbb{C}) = 0$ in $H^{2j}_{dR}(M)$. $\square$

## Proof B — via traces of odd powers of skew matrices

**Step B0: A real skew connection on the complexification.** We arrange a curvature that is real and skew.

> [!note]- Derivation
> Choose a Euclidean structure $g$ on $E$ and a $g$-metric connection $\nabla$ (both exist, [[Def - Euclidean Vector Bundle and Metric Connection]]). Its complexification $\nabla^{\mathbb{C}} := \nabla \otimes \operatorname{id}_{\mathbb{C}}$ is a connection on $E \otimes \mathbb{C}$, and in a (real) orthonormal frame $(e_1, \dots, e_n)$ of $E$ — which is simultaneously a complex frame of $E \otimes \mathbb{C}$ — the connection matrix of $\nabla^{\mathbb{C}}$ is the same real matrix $A \in \Omega^1(U; \mathfrak{so}(n))$ as that of $\nabla$. By [[Def - Euclidean Vector Bundle and Metric Connection]] the connection matrix of a metric connection in an orthonormal frame is skew, $A^{\mathsf{T}} = -A$, and therefore the curvature matrix
> $$F = dA + A \wedge A \in \Omega^2(U; \mathfrak{so}(n))$$
> is also skew-symmetric, $F^{\mathsf{T}} = -F$: this is the standing fact that a metric connection has $\mathfrak{so}(n)$-valued curvature ([[Def - Euclidean Vector Bundle and Metric Connection]]), $\mathfrak{so}(n)$ being exactly the skew matrices, and it is all we shall use about $F$ below. The entries of $F$ are $2$-forms, which commute under $\wedge$ by [[Ex - Even-Degree Forms Commute and Determinants of Matrices of Even Forms are Multiplicative]]. By [[Def - Chern Classes]] we may compute the Chern classes of $E \otimes \mathbb{C}$ from this connection: $c(E \otimes \mathbb{C}) = \big[\det\!\big(1 + \tfrac{i}{2\pi}F\big)\big]$, with $c_j(E \otimes \mathbb{C})$ the class of the degree-$2j$ component. $\square$

**Step B1: The trace lemma — odd powers of a skew matrix are traceless.** This is the algebraic heart.

> [!note]- Derivation
> **Claim.** For $F$ a skew-symmetric ($F^{\mathsf{T}} = -F$) matrix whose entries are $2$-forms, $\operatorname{tr}(F^k) = 0$ for every odd $k \ge 1$.
>
> Two general facts about matrices with commuting entries (here $2$-forms commute, [[Ex - Even-Degree Forms Commute and Determinants of Matrices of Even Forms are Multiplicative]]):
> $$\operatorname{tr}(N^{\mathsf{T}}) = \operatorname{tr}(N) \qquad \text{(the transpose fixes the diagonal, and the trace is the sum of the diagonal)},$$
> $$(NP)^{\mathsf{T}} = P^{\mathsf{T}} N^{\mathsf{T}} = N^{\mathsf{T}} P^{\mathsf{T}} \qquad \text{(the second equality uses that the entries commute)},$$
> the second of which iterates to $(F^k)^{\mathsf{T}} = (F^{\mathsf{T}})^k$. Now compute:
> $$\operatorname{tr}(F^k) = \operatorname{tr}\big((F^k)^{\mathsf{T}}\big) \qquad \text{(trace is transpose-invariant)}$$
> $$= \operatorname{tr}\big((F^{\mathsf{T}})^k\big) = \operatorname{tr}\big((-F)^k\big) \qquad \text{(} (F^k)^{\mathsf{T}} = (F^{\mathsf{T}})^k \text{, then } F^{\mathsf{T}} = -F \text{)}$$
> $$= (-1)^k \operatorname{tr}(F^k) \qquad \text{(scalar } (-1)^k \text{ pulled out of the trace).}$$
> For odd $k$, $(-1)^k = -1$, so $\operatorname{tr}(F^k) = -\operatorname{tr}(F^k)$, hence $2\operatorname{tr}(F^k) = 0$; as $\operatorname{tr}(F^k)$ is a differential form with real (indeed complex) coefficients, division by $2$ is legitimate and $\operatorname{tr}(F^k) = 0$. $\square$

**Step B2: The total Chern form lives only in degrees divisible by $4$.** We push the trace lemma through the determinant.

> [!note]- Derivation
> Write $B := \tfrac{i}{2\pi}F$, a matrix of $2$-forms with $B^k = 0$ once $2k > \dim M$ (a form of degree exceeding $\dim M$ vanishes), so every series in $B$ below is a *finite* sum and no analytic convergence is needed — the manipulations are polynomial identities in the commuting entries. Using the formal identity $\log \det(1 + B) = \operatorname{tr}\log(1 + B)$ (valid for matrices with commuting nilpotent entries, [[Ex - Even-Degree Forms Commute and Determinants of Matrices of Even Forms are Multiplicative]]):
> $$\log \det(1 + B) = \operatorname{tr}\log(1 + B) = \sum_{k \ge 1} \frac{(-1)^{k-1}}{k}\operatorname{tr}(B^k) = \sum_{k \ge 1} \frac{(-1)^{k-1}}{k}\Big(\frac{i}{2\pi}\Big)^k \operatorname{tr}(F^k).$$
> By Step B1, $\operatorname{tr}(F^k) = 0$ for odd $k$, so only even $k$ contribute:
> $$\log \det(1 + B) = \sum_{k \ \text{even},\ k \ge 2} \frac{(-1)^{k-1}}{k}\Big(\frac{i}{2\pi}\Big)^k \operatorname{tr}(F^k) \qquad \text{(odd terms dropped by Step B1)}.$$
> Each surviving summand $\operatorname{tr}(F^k)$ is a form of degree $2k$ with $k$ even, hence of degree $2k \equiv 0 \pmod 4$; so $\log \det(1 + B)$ is a sum of forms of degree divisible by $4$. Exponentiating (the wedge exponential, again a finite sum), a product of forms each of degree $\equiv 0 \pmod 4$ has degree $\equiv 0 \pmod 4$, so
> $$\det\Big(1 + \frac{i}{2\pi}F\Big) = \exp\big(\log\det(1 + B)\big) \quad\text{has components only in form-degrees } 0, 4, 8, \dots. \qquad \square$$

**Step B3: Read off the odd Chern classes.** The degree constraint kills them as forms.

> [!note]- Derivation
> By [[Def - Chern Classes]], $c_j(E \otimes \mathbb{C})$ is the class of the degree-$2j$ component $c_j(F)$ of $\det\!\big(1 + \tfrac{i}{2\pi}F\big)$. For odd $j$ the degree is $2j \equiv 2 \pmod 4$, a degree in which $\det\!\big(1 + \tfrac{i}{2\pi}F\big)$ has *no* component by Step B2. Therefore $c_j(F) = 0$ as a form for every odd $j$, and a fortiori
> $$c_j(E \otimes \mathbb{C}) = [c_j(F)] = [0] = 0 \in H^{2j}_{dR}(M) \qquad (j \text{ odd}).$$
>
> **Conclusion of Proof B.** The odd Chern classes of $E \otimes \mathbb{C}$ vanish, and in fact the representing forms themselves vanish for the complexified metric connection — a strictly stronger, pointwise statement than Proof A's cohomological vanishing. $\square$

> [!note]- Complete formal solution
> Let $E \to M$ be a real bundle of rank $n$ and $j$ odd; we show $c_j(E \otimes \mathbb{C}) = 0$ in $H^{2j}_{dR}(M)$, twice.
>
> **Proof A.** Define $\Phi : E \otimes \mathbb{C} \to \overline{E \otimes \mathbb{C}}$, $\Phi(v \otimes z) = v \otimes \bar z$. It is $\mathbb{R}$-linear, fibrewise bijective ($\Phi^2 = \operatorname{id}$), smooth, and $\mathbb{C}$-linear into the conjugate: $\Phi(i(v \otimes z)) = v \otimes \overline{iz} = -i(v \otimes \bar z) = i \cdot_{\overline{\phantom{x}}}\Phi(v \otimes z)$, since $i$ acts as $-i$ on the conjugate bundle. Hence $E \otimes \mathbb{C} \cong \overline{E \otimes \mathbb{C}}$. By isomorphism invariance ([[Thm - Naturality and Isomorphism Invariance of Characteristic Classes]]) and the conjugation rule $c_j(\overline{V}) = (-1)^j c_j(V)$ ([[Ex - Chern Classes of the Dual Bundle]]),
> $$c_j(E \otimes \mathbb{C}) = c_j\big(\overline{E \otimes \mathbb{C}}\big) = (-1)^j c_j(E \otimes \mathbb{C}).$$
> For odd $j$ this is $c_j = -c_j$, so $2 c_j = 0$; in the real vector space $H^{2j}_{dR}(M)$ this forces $c_j(E \otimes \mathbb{C}) = 0$.
>
> **Proof B.** Take a $g$-metric connection $\nabla$ on a Euclidean structure $g$ on $E$; its complexification represents $c(E \otimes \mathbb{C})$ ([[Def - Chern Classes]]), with curvature the real skew matrix $F \in \Omega^2(U; \mathfrak{so}(n))$, $F^{\mathsf{T}} = -F$ ([[Def - Euclidean Vector Bundle and Metric Connection]]); its entries are $2$-forms and commute ([[Ex - Even-Degree Forms Commute and Determinants of Matrices of Even Forms are Multiplicative]]).
>
> *Trace lemma.* For odd $k$, $\operatorname{tr}(F^k) = \operatorname{tr}((F^k)^{\mathsf{T}}) = \operatorname{tr}((F^{\mathsf{T}})^k) = \operatorname{tr}((-F)^k) = (-1)^k \operatorname{tr}(F^k) = -\operatorname{tr}(F^k)$, using $\operatorname{tr}(N^{\mathsf{T}}) = \operatorname{tr}(N)$ and $(F^k)^{\mathsf{T}} = (F^{\mathsf{T}})^k$ (commuting entries); hence $\operatorname{tr}(F^k) = 0$.
>
> *Degree constraint.* With $B = \tfrac{i}{2\pi}F$ (so $B^k = 0$ for $2k > \dim M$; all series finite),
> $$\log\det(1 + B) = \operatorname{tr}\log(1 + B) = \sum_{k \ge 1} \tfrac{(-1)^{k-1}}{k}\big(\tfrac{i}{2\pi}\big)^k \operatorname{tr}(F^k) = \sum_{k \ \text{even}} \tfrac{(-1)^{k-1}}{k}\big(\tfrac{i}{2\pi}\big)^k \operatorname{tr}(F^k),$$
> a sum of forms of degree $2k \equiv 0 \pmod 4$; exponentiating, $\det(1 + \tfrac{i}{2\pi}F)$ has components only in degrees divisible by $4$.
>
> *Conclusion.* The degree-$2j$ component $c_j(F)$ with $j$ odd has degree $\equiv 2 \pmod 4$ and is therefore absent: $c_j(F) = 0$ as a form, so $c_j(E \otimes \mathbb{C}) = [c_j(F)] = 0$. $\blacksquare$

> [!warning] Illegal but tempting: "$E \otimes \mathbb{C}$ is self-conjugate because conjugation is an isomorphism"
> It is tempting to say "complex conjugation $v \otimes z \mapsto v \otimes \bar z$ is a bijection, so $E \otimes \mathbb{C} \cong E \otimes \mathbb{C}$" and conclude nothing (a bundle is always isomorphic to itself), or worse, to apply the conjugation rule to that trivial self-isomorphism and derive $c_j = (-1)^j c_j$ *without* the conjugate bundle — which is false, since it would kill the odd Chern classes of every complex bundle. The error is forgetting that conjugation is $\mathbb{C}$-*antilinear* as a self-map, hence not a morphism of complex bundles at all. It becomes a morphism only when the target is re-read as the *conjugate* bundle $\overline{E \otimes \mathbb{C}}$, where the scalar action is twisted. The extra condition that makes the argument legal is exactly this: the isomorphism is with $\overline{E \otimes \mathbb{C}}$, and it is the conjugation rule for the *conjugate* (not the identity) that supplies the sign $(-1)^j$.

> [!note]- Independent sanity check: the rank-1 and Pontryagin consistency
> For $n = 1$: $E \otimes \mathbb{C}$ has complex rank $1$, with only $c_0 = 1$ and $c_1$; Proof A gives $c_1(E \otimes \mathbb{C}) = 0$, consistent with the fact that a complexified real line bundle carries a real structure (a nowhere-vanishing "real" direction up to sign) and cannot have a nonzero degree. Proof B agrees: the curvature is a $1 \times 1$ skew matrix, i.e. $F = 0$ (the only skew $1\times 1$ matrix), so every Chern form above degree $0$ vanishes. Second check — Pontryagin consistency: the definition $p_k(E) = (-1)^k c_{2k}(E \otimes \mathbb{C})$ ([[Def - Pontryagin Classes]]) keeps only *even* Chern classes, and this exercise shows the discarded odd ones were already zero, so no information is lost; the first Pontryagin class $p_1(E) = -c_2(E \otimes \mathbb{C})$ is exactly the first surviving even class.

---

# Key Takeaways

**A real structure on a complex bundle is a vanishing theorem for odd Chern classes.** The reusable principle is that whenever a complex bundle $V$ carries a real structure — a $\mathbb{C}$-antilinear involution $\Phi$ with $\Phi^2 = \operatorname{id}$, equivalently an isomorphism $V \cong \overline{V}$ — its odd Chern classes vanish in real cohomology, because $c_j(V) = c_j(\overline{V}) = (-1)^j c_j(V)$. The trigger condition is any phrase that supplies such a structure: "complexification of a real bundle", "self-dual over $\mathbb{R}$", "the underlying real bundle of ...". The transferable diagnostic: on meeting a complex bundle, ask whether it comes from a real one; if so, only its even Chern classes (equivalently its Pontryagin classes) can be nonzero, and half the characteristic data is automatically zero. This is the structural reason the Pontryagin classes index real bundles with the *even* Chern classes of the complexification and lose nothing.

**Traces of odd powers of skew matrices vanish, and this controls which form-degrees a determinant can occupy.** The second proof isolates a purely algebraic engine: for a skew matrix with commuting entries, $\operatorname{tr}(F^k) = (-1)^k \operatorname{tr}(F^k)$, so odd powers are traceless; fed through $\log\det = \operatorname{tr}\log$, this confines $\det(1 + \tfrac{i}{2\pi}F)$ to form-degrees divisible by $4$. The trigger is a curvature that is skew in some frame — always the case for a metric connection on a real (or complexified-real) bundle. The transferable lesson is that a symmetry of the curvature *matrix* ($F^{\mathsf{T}} = -F$) becomes, via the Chern polynomial, a constraint on the *cohomological degrees* that can carry a characteristic class; the same mechanism gives the reality and degree-$4$ periodicity of Pontryagin forms and underlies the vanishing $\operatorname{tr}(F \wedge F \wedge F) = 0$ used for $SU(2)$. When a class "ought" to vanish for parity reasons, look for a skew or self-adjoint curvature and run the trace argument.

**Two proofs calibrate the strength of a vanishing statement.** Proof A vanishes in cohomology; Proof B vanishes the representing form pointwise, for a specific (metric) connection — a strictly stronger, connection-dependent statement whose cohomological shadow is Proof A. The reusable diagnostic is to notice, when a class is zero, *how* zero it is: a class can be zero because it is exact (Proof A style, torsion argument), or because its natural representative is literally zero (Proof B style, pointwise). The distinction matters downstream: pointwise vanishing of the odd Chern forms is what lets the Pontryagin form $\det(1 - \tfrac{1}{2\pi}F)$ be written with only even terms *as forms*, which is used verbatim on [[Def - Pontryagin Classes]]. Companion drills to hold alongside this one are [[Ex - Chern Classes of the Dual Bundle]] (the conjugation rule this exercise consumes) and [[Ex - The Euler Class of an Oriented Rank-2 Bundle is its First Chern Class]] (the complementary story of how a real oriented rank-$2$ bundle *acquires* a first Chern class from a complex structure).
