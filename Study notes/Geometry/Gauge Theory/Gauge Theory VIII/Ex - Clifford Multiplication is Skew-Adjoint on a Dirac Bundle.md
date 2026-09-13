---
type: exercise
subject: gauge-theory
prereqs:
  - "Def - Spinor Bundle and Dirac Operator"
  - "Def - Clifford Bundle and Bundle of Clifford Modules"
difficulty: "⭐"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $E \to M$ be a **Dirac bundle** over an oriented Riemannian manifold $(M, g)$: a bundle of Clifford modules carrying a fibre metric $\langle\cdot,\cdot\rangle$ (Euclidean if $E$ is real, Hermitian if $E$ is complex) and a compatible connection. Fix a point $m \in M$ and work in the fibre $E_m$; let $v \in T_mM$ be a tangent vector and $e_1, e_2 \in E_m$. Two facts are given: the **Clifford relation**
$$v \cdot (v \cdot e) = -|v|^2\, e \qquad (e \in E_m),$$
and the Dirac-bundle **metric condition** (Haydys's condition (2))
$$\langle v \cdot e_1,\ v \cdot e_2\rangle = |v|^2\,\langle e_1, e_2\rangle \qquad (e_1, e_2 \in E_m).$$

Prove the two directions of the following equivalence, which identifies condition (2) with the skew-adjointness of Clifford multiplication.

- **(Forward.)** From the metric condition (2), together with the Clifford relation, deduce that Clifford multiplication by $v$ is **skew-adjoint**:
$$\langle v \cdot e_1,\ e_2\rangle = -\langle e_1,\ v \cdot e_2\rangle \qquad (v \in T_mM,\ e_1, e_2 \in E_m).$$
Obtain it by **polarising condition (2) in the vector variable $v$** and then using the Clifford relation.

- **(Converse.)** Conversely, assume skew-adjointness and the Clifford relation. Deduce condition (2).

Throughout, Clifford multiplication is **linear in the vector slot** — $(av + bw) \cdot e = a(v \cdot e) + b(w \cdot e)$ for scalars $a, b$ and $v, w \in T_mM$ — and the metric is Riemannian, so $|v|^2 = \langle v, v\rangle > 0$ for $v \neq 0$.

**Recall:**

The objects in play are a Dirac bundle and its three defining conditions, of which condition (2) is the second; the Clifford relation, which is the defining identity of a bundle of Clifford modules; and the notion of a skew-adjoint (respectively self-adjoint) endomorphism of an inner-product space.

![[Def - Spinor Bundle and Dirac Operator#Dirac bundle]]

The relation $v \cdot (v \cdot e) = -|v|^2 e$ is the defining identity of a [[Def - Clifford Bundle and Bundle of Clifford Modules|bundle of Clifford modules]]; it is the sign convention $v \cdot v = -|v|^2$ used throughout this chapter, and it is the only algebraic fact about Clifford multiplication that the present exercise needs.

An endomorphism $A$ of an inner-product space $(W, \langle\cdot,\cdot\rangle)$ is **self-adjoint** if $\langle Aa, b\rangle = \langle a, Ab\rangle$ for all $a, b$, and **skew-adjoint** if $\langle Aa, b\rangle = -\langle a, Ab\rangle$ for all $a, b$. The claim to be proved is that, for each fixed $v$, the map $e \mapsto v \cdot e$ on $E_m$ is skew-adjoint exactly when condition (2) holds.

> [!warning] Convention: Clifford sign
> The series uses $v \cdot v = -|v|^2 \cdot 1$ (Haydys), so that the Dirac operator squares to a nonnegative Laplacian. The vault's [[Def - Clifford Algebra|Clifford algebra page]] writes the relation as $\varphi(v)^2 = Q(v) \cdot 1$ for a general quadratic form $Q$; the dictionary is $Q(v) = -|v|^2$. Under the opposite convention $v \cdot v = +|v|^2$ the same computation would produce a *self*-adjoint Clifford multiplication and condition (2) would read $\langle v \cdot e_1, v \cdot e_2\rangle = -|v|^2\langle e_1, e_2\rangle$, which has no positive solutions; the minus sign in the Clifford relation is exactly what makes condition (2) compatible with a positive-definite fibre metric.

---

# Convergent Strategy

**Problem class.** This is a *two-sided equivalence of algebraic conditions on a single linear map* — the smallest, most reusable identity in the theory of Dirac bundles. Condition (2) is stated as a *scaling law* ("Clifford multiplication by $v$ multiplies the fibre metric by $|v|^2$"), whereas every integration-by-parts argument in the chapter (the formal self-adjointness of the Dirac operator on [[Thm - Dirac Operators are Formally Self-Adjoint|the self-adjointness page]], the Weitzenböck identity, the Seiberg–Witten linearisation) uses the *adjoint* form ("$v\cdot$ is skew-adjoint"). The exercise is the bridge between the two phrasings; it is [[Def - Spinor Bundle and Dirac Operator|Proposition 1 of the definition page]] drilled, and it is worth being able to reconstruct in under a minute.

**Assumption pattern.** The recognisable pattern is that we hold a *quadratic* identity in $v$ — condition (2) has $v$ appearing twice, once in each Clifford factor — and we want a *bilinear* consequence, in which $v$ appears in only one factor at a time. The universal tool for extracting a bilinear identity from a quadratic one is **polarisation**: replace $v$ by $v + w$, expand, and cancel the pure-$v$ and pure-$w$ terms. The second, sign-carrying ingredient is the Clifford relation $v \cdot v \cdot = -|v|^2$, which is what converts "the two Clifford factors combine" into an actual sign.

**Theorem routing.** Forward: *polarise* condition (2) in $v$ to obtain the bilinear identity $\langle v \cdot e_1, w \cdot e_2\rangle + \langle w \cdot e_1, v \cdot e_2\rangle = 2\langle v, w\rangle\langle e_1, e_2\rangle$ (call it $(\ast)$); then specialise $(\ast)$ — replacing the second section by $v \cdot e_2$ and setting $w = v$ — and simplify with the Clifford relation $v \cdot (v \cdot e_2) = -|v|^2 e_2$; dividing by $|v|^2$ (legitimate because $g$ is Riemannian and $v \neq 0$) leaves skew-adjointness. Converse: apply skew-adjointness to move one Clifford factor across the inner product, then collapse the two factors with the Clifford relation. No theorem beyond these two given facts is needed; the equivalence is purely algebraic and pointwise.

**Key decision point.** The single non-obvious move is the substitution that turns the symmetric polarised identity $(\ast)$ into an *anti*symmetric statement about one vector. Polarisation alone gives only the symmetric combination $\langle v \cdot e_1, w \cdot e_2\rangle + \langle w \cdot e_1, v \cdot e_2\rangle$; a naive reader stops there and cannot see skew-adjointness. The trick is to feed $v \cdot e_2$ back into the second slot: because $v \cdot (v \cdot e_2) = -|v|^2 e_2$ carries the minus sign of the Clifford relation, the symmetric identity is forced to produce the antisymmetric conclusion. Recognising that "the sign in skew-adjointness comes from the sign in $v \cdot v = -|v|^2$, not from the metric" is the whole content of the exercise, and it is why the *opposite* Clifford convention would give self-adjointness instead.

---

# Legal Operations Used

1. **Polarise a quadratic identity to extract its bilinear form.** Condition (2) is quadratic in $v$; substituting $v \mapsto v + w$ and cancelling the pure terms produces the associated symmetric bilinear identity $(\ast)$. This is the exact-analogue of recovering an inner product from its norm, $\langle a, b\rangle = \tfrac12(|a+b|^2 - |a|^2 - |b|^2)$.

2. **Substitute a Clifford-multiplied section into a metric identity.** Replacing $e_2$ by $v \cdot e_2$ in an identity involving $\langle\, \cdot\, , v \cdot e_2\rangle$ creates a nested factor $v \cdot (v \cdot e_2)$ that the Clifford relation then collapses. This is the move that converts a metric statement into an adjointness statement.

3. **Collapse a repeated Clifford factor with the relation $v \cdot v \cdot = -|v|^2$.** Wherever the same vector $v$ Clifford-multiplies twice in succession, replace $v \cdot (v \cdot e)$ by the scalar $-|v|^2 e$. This is the only place the sign enters.

4. **Divide by $|v|^2$ using that the metric is Riemannian.** For $v \neq 0$, $|v|^2 > 0$, so an identity of the form $|v|^2 X = |v|^2 Y$ yields $X = Y$; the degenerate case $v = 0$ is handled separately by linearity in the vector slot. Both slots of an inner product are $0$ when $v = 0$.

5. **Move an endomorphism across the inner product using its adjointness type.** In the converse, skew-adjointness of $v\cdot$ lets $\langle v \cdot e_1, v \cdot e_2\rangle$ be rewritten as $-\langle e_1, v \cdot (v \cdot e_2)\rangle$; this is the definitional use of "skew-adjoint".

---

# Hints

> [!note]- Hint 1
> Condition (2), $\langle v \cdot e_1, v \cdot e_2\rangle = |v|^2\langle e_1, e_2\rangle$, has the vector $v$ appearing *twice*. Skew-adjointness, $\langle v \cdot e_1, e_2\rangle = -\langle e_1, v \cdot e_2\rangle$, has $v$ appearing *once* on each side. To pass from a two-$v$ identity to a one-$v$ identity, use the standard device for turning a quadratic identity into a bilinear one.

> [!note]- Hint 2
> That device is **polarisation**: replace $v$ by $v + w$ in condition (2), expand both sides by bilinearity of the inner product and linearity of Clifford multiplication in the vector slot, and subtract off condition (2) for $v$ alone and for $w$ alone. You should be left with
> $$\langle v \cdot e_1, w \cdot e_2\rangle + \langle w \cdot e_1, v \cdot e_2\rangle = 2\langle v, w\rangle\,\langle e_1, e_2\rangle. \qquad (\ast)$$
> Note $|v + w|^2 = |v|^2 + 2\langle v, w\rangle + |w|^2$ on the right.

> [!note]- Hint 3
> Now turn the *symmetric* identity $(\ast)$ into the *antisymmetric* skew-adjointness. In $(\ast)$ replace $e_2$ by $v \cdot e_2$ and set $w = v$. On the left, both terms then contain $v \cdot (v \cdot e_2)$; use the Clifford relation $v \cdot (v \cdot e_2) = -|v|^2 e_2$ to collapse it. Compare with the right-hand side, which becomes $2|v|^2\langle e_1, v \cdot e_2\rangle$.

> [!note]- Hint 4
> After the substitution you will have $-2|v|^2\langle v \cdot e_1, e_2\rangle = 2|v|^2\langle e_1, v \cdot e_2\rangle$. For $v \neq 0$ divide by $2|v|^2$ (positive, since $g$ is Riemannian); for $v = 0$ both sides of the target vanish by linearity. For the converse, start from $\langle v \cdot e_1, v \cdot e_2\rangle$, use skew-adjointness to pull the *first* $v\cdot$ across into the second slot (picking up a minus), and then collapse $v \cdot (v \cdot e_2)$ with the Clifford relation.

---

# Solution

The equivalence is a two-line algebraic fact once the right substitution is made. The forward direction extracts skew-adjointness from the scaling condition (2) by polarising in $v$ to get the symmetric bilinear identity $(\ast)$, then feeding a Clifford-multiplied section back in so that the Clifford relation supplies the antisymmetrising minus sign. The converse is the shorter direction: skew-adjointness moves one Clifford factor across the inner product, and the Clifford relation collapses the two factors that meet.

## Forward direction: condition (2) $\Rightarrow$ skew-adjointness

**Step 1: Polarise condition (2) in the vector variable $v$.**

Replacing $v$ by $v + w$ in condition (2) and cancelling the pure-$v$ and pure-$w$ instances yields the symmetric bilinear identity
$$\langle v \cdot e_1,\ w \cdot e_2\rangle + \langle w \cdot e_1,\ v \cdot e_2\rangle = 2\langle v, w\rangle\,\langle e_1, e_2\rangle. \qquad (\ast)$$

> [!note]- Derivation
> Fix $e_1, e_2 \in E_m$ and let $v, w \in T_mM$. Apply condition (2) with the vector $v + w$ in place of $v$:
> $$\langle (v + w) \cdot e_1,\ (v + w) \cdot e_2\rangle = |v + w|^2\,\langle e_1, e_2\rangle \qquad \text{(condition (2), vector } v + w\text{).}$$
> On the left, Clifford multiplication is linear in the vector slot, so $(v + w) \cdot e_i = v \cdot e_i + w \cdot e_i$; expand by bilinearity of the fibre metric (sesquilinearity in the Hermitian case introduces no conjugation, because $v, w$ are real tangent vectors and only the *sections* $e_i$ sit in the conjugate-linear slots, which we are not varying here):
> $$\langle (v+w)\cdot e_1, (v+w)\cdot e_2\rangle = \langle v\cdot e_1, v\cdot e_2\rangle + \langle v\cdot e_1, w\cdot e_2\rangle + \langle w\cdot e_1, v\cdot e_2\rangle + \langle w\cdot e_1, w\cdot e_2\rangle \qquad \text{(linearity in the vector slot; bilinearity of } \langle\cdot,\cdot\rangle\text{).}$$
> On the right, $|v + w|^2 = \langle v + w, v + w\rangle = |v|^2 + 2\langle v, w\rangle + |w|^2$ (bilinearity and symmetry of $g$), so
> $$|v+w|^2\langle e_1, e_2\rangle = |v|^2\langle e_1, e_2\rangle + 2\langle v, w\rangle\langle e_1, e_2\rangle + |w|^2\langle e_1, e_2\rangle.$$
> Now subtract condition (2) for $v$ alone, $\langle v\cdot e_1, v\cdot e_2\rangle = |v|^2\langle e_1,e_2\rangle$, and condition (2) for $w$ alone, $\langle w\cdot e_1, w\cdot e_2\rangle = |w|^2\langle e_1,e_2\rangle$, from the two displays. The pure-$v$ and pure-$w$ terms cancel on both sides, leaving exactly
> $$\langle v\cdot e_1, w\cdot e_2\rangle + \langle w\cdot e_1, v\cdot e_2\rangle = 2\langle v, w\rangle\langle e_1, e_2\rangle,$$
> which is $(\ast)$. This holds for all $v, w \in T_mM$ and $e_1, e_2 \in E_m$.

**Step 2: Specialise $(\ast)$ and collapse the repeated Clifford factor.**

In $(\ast)$ replace $e_2$ by $v \cdot e_2$ and set $w = v$; the Clifford relation $v \cdot (v \cdot e_2) = -|v|^2 e_2$ then reduces the left side to $-2|v|^2\langle v \cdot e_1, e_2\rangle$, and the right side to $2|v|^2\langle e_1, v \cdot e_2\rangle$.

> [!note]- Derivation
> Take $(\ast)$ with the section $e_2$ replaced by $v \cdot e_2 \in E_m$ (a legitimate substitution, since $(\ast)$ holds for *all* second sections) and with the free vector $w$ set equal to $v$:
> $$\langle v \cdot e_1,\ v \cdot (v \cdot e_2)\rangle + \langle v \cdot e_1,\ v \cdot (v \cdot e_2)\rangle = 2\langle v, v\rangle\,\langle e_1,\ v \cdot e_2\rangle \qquad \text{(}(\ast)\text{ with } e_2 \rightsquigarrow v\cdot e_2,\ w \rightsquigarrow v\text{).}$$
> The two summands on the left are identical, so the left side is $2\langle v \cdot e_1,\ v \cdot (v \cdot e_2)\rangle$; and $\langle v, v\rangle = |v|^2$ on the right. Apply the **Clifford relation** to the inner factor, $v \cdot (v \cdot e_2) = -|v|^2 e_2$:
> $$2\big\langle v \cdot e_1,\ -|v|^2\, e_2\big\rangle = 2|v|^2\,\langle e_1,\ v \cdot e_2\rangle \qquad \text{(Clifford relation } v\cdot(v\cdot e_2) = -|v|^2 e_2\text{).}$$
> The scalar $-|v|^2$ is real, so it passes out of the metric's second slot without conjugation in either the Euclidean or the Hermitian case, giving
> $$-2|v|^2\,\langle v \cdot e_1,\ e_2\rangle = 2|v|^2\,\langle e_1,\ v \cdot e_2\rangle. \qquad (\ast\ast)$$

**Step 3: Divide by $|v|^2$ and conclude.**

Cancelling the positive scalar $2|v|^2$ from $(\ast\ast)$ gives skew-adjointness for $v \neq 0$; the case $v = 0$ is immediate.

> [!note]- Derivation
> If $v \neq 0$, then $|v|^2 > 0$ because $g$ is Riemannian, so $2|v|^2 \neq 0$ and we may divide $(\ast\ast)$ through by it:
> $$-\langle v \cdot e_1, e_2\rangle = \langle e_1, v \cdot e_2\rangle, \qquad \text{that is} \qquad \langle v \cdot e_1, e_2\rangle = -\langle e_1, v \cdot e_2\rangle.$$
> If $v = 0$, then $v \cdot e_1 = 0$ and $v \cdot e_2 = 0$ by linearity of Clifford multiplication in the vector slot, so both sides of the target identity are $0$ and it holds trivially. Hence, for every $v \in T_mM$ and all $e_1, e_2 \in E_m$, Clifford multiplication by $v$ is skew-adjoint. This proves the forward direction.

## Converse direction: skew-adjointness $\Rightarrow$ condition (2)

**Step 4: Move one Clifford factor across, then collapse with the Clifford relation.**

Assuming $\langle v \cdot a, b\rangle = -\langle a, v \cdot b\rangle$ for all $a, b$, apply it to $\langle v \cdot e_1, v \cdot e_2\rangle$ and then use the Clifford relation.

> [!note]- Derivation
> Assume skew-adjointness of $v\cdot$ and the Clifford relation. Then
> $$\langle v \cdot e_1,\ v \cdot e_2\rangle = -\langle e_1,\ v \cdot (v \cdot e_2)\rangle \qquad \text{(skew-adjointness, moving the first } v\cdot \text{ into the second slot with } a = e_1,\ b = v\cdot e_2\text{)}$$
> $$= -\langle e_1,\ -|v|^2 e_2\rangle \qquad \text{(Clifford relation } v \cdot (v \cdot e_2) = -|v|^2 e_2\text{)}$$
> $$= |v|^2\,\langle e_1, e_2\rangle \qquad \text{(the real scalar } -|v|^2 \text{ leaves the second slot, and the two minus signs multiply to } +\text{).}$$
> This is condition (2). It holds for every $v \in T_mM$ (no division was used, so $v = 0$ needs no separate treatment) and all $e_1, e_2 \in E_m$, completing the converse.

> [!note]- Complete formal solution
> **Claim.** For a bundle of Clifford modules $E$ with a fibre metric, and a fixed $v \in T_mM$, condition (2) — $\langle v \cdot e_1, v \cdot e_2\rangle = |v|^2\langle e_1, e_2\rangle$ for all $e_1, e_2$ — holds if and only if Clifford multiplication by $v$ is skew-adjoint, $\langle v \cdot e_1, e_2\rangle = -\langle e_1, v \cdot e_2\rangle$ for all $e_1, e_2$. Both directions use only the Clifford relation $v \cdot (v \cdot e) = -|v|^2 e$ and, for the forward direction, that $g$ is Riemannian.
>
> **($\Rightarrow$)** *Polarise (2).* Substituting $v + w$ for $v$ in (2), expanding by linearity of Clifford multiplication in the vector slot and bilinearity of the metric, and subtracting the instances of (2) for $v$ and for $w$, gives
> $$\langle v \cdot e_1, w \cdot e_2\rangle + \langle w \cdot e_1, v \cdot e_2\rangle = 2\langle v, w\rangle\langle e_1, e_2\rangle \qquad (\ast)$$
> for all $v, w \in T_mM$, $e_1, e_2 \in E_m$. *Specialise.* In $(\ast)$ put $w = v$ and replace $e_2$ by $v \cdot e_2$; the two left summands coincide, and $v \cdot (v \cdot e_2) = -|v|^2 e_2$ by the Clifford relation, so
> $$2\langle v \cdot e_1, -|v|^2 e_2\rangle = 2|v|^2\langle e_1, v \cdot e_2\rangle, \qquad \text{i.e.} \qquad -2|v|^2\langle v \cdot e_1, e_2\rangle = 2|v|^2\langle e_1, v \cdot e_2\rangle.$$
> *Conclude.* For $v \neq 0$, $|v|^2 > 0$ (Riemannian metric); dividing by $2|v|^2$ gives $\langle v \cdot e_1, e_2\rangle = -\langle e_1, v \cdot e_2\rangle$. For $v = 0$ both sides vanish. Hence $v\cdot$ is skew-adjoint.
>
> **($\Leftarrow$)** Assume skew-adjointness. Then, for all $e_1, e_2$,
> $$\langle v \cdot e_1, v \cdot e_2\rangle = -\langle e_1, v \cdot (v \cdot e_2)\rangle = -\langle e_1, -|v|^2 e_2\rangle = |v|^2\langle e_1, e_2\rangle,$$
> the first equality by skew-adjointness (moving the first factor across), the second by the Clifford relation, the third because the real scalar $-|v|^2$ leaves the second slot and the signs cancel. This is condition (2). $\blacksquare$

> [!warning] Illegal but tempting shortcut
> It is tempting to argue: "condition (2) says $v\cdot$ preserves the metric up to the scalar $|v|^2$, so $v\cdot$ is *orthogonal*, hence its adjoint equals its inverse, $\langle v \cdot e_1, e_2\rangle = \langle e_1, (v\cdot)^{-1} e_2\rangle$." This is true but is *not* skew-adjointness, and reading it as such is the standard error. The adjoint of $v\cdot$ is its inverse only after normalising $|v| = 1$, and $(v\cdot)^{-1} = -|v|^{-2}(v\cdot)$ by the Clifford relation, so $(v\cdot)^* = (v\cdot)^{-1} = -|v|^{-2}(v\cdot)$, which for a unit vector is $-(v\cdot)$ — skew-adjoint. The shortcut is only legitimate once one has computed the inverse from the Clifford relation; the sign lives in that computation, exactly as in the honest proof above.

> [!note]- Independent sanity check: the smallest concrete case
> Take $M = \mathbb{R}$, $E = \mathbb{R} \times \mathbb{C}$, $v = \partial_x$ the unit vector, and $v \cdot z = iz$ (this satisfies the Clifford relation: $v \cdot (v \cdot z) = i(iz) = -z = -|v|^2 z$). The Hermitian metric is $\langle z, w\rangle = \bar z w$. Condition (2): $\langle iz, iw\rangle = \overline{iz}\,(iw) = (-i\bar z)(iw) = \bar z w = |v|^2\langle z, w\rangle$. Skew-adjointness: $\langle iz, w\rangle = \overline{iz}\,w = -i\bar z w$, while $-\langle z, iw\rangle = -\bar z(iw) = -i\bar z w$; the two agree. Both conditions hold, consistently with the equivalence, and the shared minus sign is visibly the $i^2 = -1$ of the Clifford relation.

---

# Key Takeaways

**Polarisation is the reflex for turning a quadratic identity into the bilinear identity hiding inside it, and here it is what unlocks the adjoint form of a scaling law.** Condition (2) is quadratic in the vector $v$ — $v$ appears in both Clifford factors — and the adjointness statement we want is bilinear, with $v$ in only one factor at a time. Whenever a hypothesis is a "diagonal" statement $Q(v) = R(v)$ with both sides quadratic in some variable, and the desired conclusion involves that variable linearly, the move is to substitute $v \mapsto v + w$, expand, and cancel the pure terms; the surviving cross-terms are the bilinear content. This is the same operation that recovers an inner product from its norm and a symmetric bilinear form from its associated quadratic form, and it recurs across the chapter — for instance in reading the Clifford relation $v \cdot v = -|v|^2$ itself in its polarised anticommutator form $v \cdot w + w \cdot v = -2\langle v, w\rangle$. The diagnostic for reaching for polarisation is precisely a mismatch in degree between what you are given and what you want.

**The minus sign of skew-adjointness comes from the minus sign of the Clifford relation, not from the metric.** The most transferable lesson of this exercise is *where the sign lives*. The metric condition (2) is sign-blind — it involves only $|v|^2 \geq 0$ — so on its own it could never distinguish self-adjoint from skew-adjoint Clifford multiplication. The distinction is decided entirely by the substitution that produces a nested factor $v \cdot (v \cdot e)$, at which point the convention $v \cdot v = -|v|^2$ delivers the minus sign. Under the opposite Clifford convention $v \cdot v = +|v|^2$ the identical computation would make Clifford multiplication *self*-adjoint (and would force condition (2) to carry a minus, hence be unsatisfiable for a positive-definite metric). This is why the two Clifford sign conventions are not cosmetic: the sign choice is exactly the choice between skew-adjoint and self-adjoint Clifford multiplication, and hence between a Dirac operator that squares to $+\Delta$ and one that squares to $-\Delta$. When you meet a Dirac-type computation whose sign you cannot recover, trace it back to the Clifford relation.

**Skew-adjointness of Clifford multiplication is the reusable output; condition (2) is its convenient input.** Condition (2) is the clause one *verifies* when constructing a Dirac bundle — it says $SO(n)$ preserves the module metric, which is automatic for any associated bundle built from the frame bundle — but it is never the clause one *uses* downstream. Every later argument invokes the skew-adjoint form: the pointwise divergence identity behind [[Thm - Dirac Operators are Formally Self-Adjoint|formal self-adjointness of the Dirac operator]] moves each frame vector $e_i$ across the inner product with a sign, the Weitzenböck integration by parts does the same, and the Seiberg–Witten linearisation uses $\langle v \cdot \psi, \phi\rangle = -\langle \psi, v \cdot \phi\rangle$ to relate the equations to their adjoints. So the trigger–reaction pattern to store is: *"a Dirac bundle appears and an inner product needs a Clifford factor moved across"* $\Rightarrow$ *"apply skew-adjointness, pick up a minus sign"*; and if you ever need to justify that skew-adjointness afresh, it is this three-line polarisation from condition (2). Keeping the equivalence in hand means you can present a Dirac bundle by whichever of the two conditions is easier to check and use whichever is easier to apply.
