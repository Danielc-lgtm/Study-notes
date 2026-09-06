---
type: exercise
subject: differential-geometry
difficulty: "⭐⭐"
prereqs:
  - "Def - The Tangent Space"
  - "Def - Velocity of a Curve"
  - "Def - The Differential of a Smooth Map"
tags: [geometry, differential-geometry]
---

# Problem Statement

Let $\mathrm{GL}(n, \mathbb{R}) \subseteq M_{n}(\mathbb{R})$ denote the general linear [[Def - Group|group]] — the set of invertible $n \times n$ real matrices, regarded as an open subset of the vector space $M_{n}(\mathbb{R}) \cong \mathbb{R}^{n^{2}}$ (the open subset where the determinant is nonzero).

(a) Show that $T_{I}\mathrm{GL}(n, \mathbb{R}) \cong M_{n}(\mathbb{R})$ canonically, where $I$ is the identity matrix.

(b) Compute the differential of matrix inversion at the identity. That is, let $\iota : \mathrm{GL}(n) \to \mathrm{GL}(n)$ be the map $\iota(A) = A^{-1}$. Find $d\iota_{I}(H)$ for $H \in M_{n}(\mathbb{R})$.

(c) (Preview of Lie algebra structure.) For $A, B \in M_{n}(\mathbb{R})$, define the **commutator** $[A, B] = AB - BA$. Define a curve $\gamma_{A, B} : \mathbb{R} \to \mathrm{GL}(n)$ by $\gamma_{A, B}(t) = e^{tA} e^{tB} e^{-tA} e^{-tB}$ for small $t$. Show that the velocity $\gamma_{A, B}'(0) = 0$, and that the *second-order* expansion of $\gamma_{A, B}(t)$ at $t = 0$ has leading term $t^{2} [A, B]/2$ — exhibiting the commutator as the "infinitesimal failure of commutativity" of one-parameter [[Def - Subgroup|subgroups]]. This is a preview of the Lie algebra structure on $T_{I}\mathrm{GL}(n)$, see [[Differential Geometry XI — Lie Groups, Lie Algebras, and the Exponential Map]].

**Recall:**

$\mathrm{GL}(n, \mathbb{R})$ is an open subset of $M_{n}(\mathbb{R})$ since $\det : M_{n}(\mathbb{R}) \to \mathbb{R}$ is continuous and $\mathrm{GL}(n) = \det^{-1}(\mathbb{R} \setminus \{0\})$.

For a finite-dimensional vector space $V$ regarded as a smooth manifold, the canonical isomorphism $T_{a}V \cong V$ sends $v \in V$ to the derivation $D_{v}|_{a} : f \mapsto (d/dt)|_{0} f(a + tv)$; see [[Def - The Tangent Space]].

The matrix exponential $e^{A} = \sum_{k=0}^{\infty} A^{k}/k!$ converges for every $A \in M_{n}(\mathbb{R})$, defines a smooth map $M_{n}(\mathbb{R}) \to \mathrm{GL}(n)$, and satisfies $e^{0} = I$ and $(d/dt) e^{tA}|_{t=0} = A$.

---

# Convergent Strategy

**Problem class:** This is a *concrete tangent-space identification* problem that previews **Lie algebra structure**. The general routine is: identify the tangent space at the identity of a Lie group using the "open subset of a vector space" or "level set" structure; compute differentials of group operations via the curve formula; uncover the algebraic structure (Lie bracket) hidden in the second-order expansion.

**Assumption pattern:** $\mathrm{GL}(n)$ is an open subset of the vector space $M_{n}(\mathbb{R})$, so its tangent space at any point is canonically $M_{n}(\mathbb{R})$. The map $\iota(A) = A^{-1}$ is smooth on $\mathrm{GL}(n)$ (entries of $A^{-1}$ are rational functions in entries of $A$ with nonvanishing denominator $\det A$). The matrix exponential provides a curve realizing any matrix as a tangent vector at $I$.

**Theorem routing:** (a) Use the canonical isomorphism $T_{a}V \cong V$ for $V = M_{n}(\mathbb{R})$ open at $I$. (b) Compute $d\iota_{I}(H)$ via the curve formula (Corollary 3.25): pick a curve $\gamma$ with $\gamma(0) = I, \gamma'(0) = H$, and differentiate $\iota \circ \gamma$ at $0$. The curve $\gamma(t) = I + tH$ works for $|t|$ small, and $\iota(\gamma(t)) = (I + tH)^{-1}$ admits a Neumann-series expansion. (c) For $\gamma_{A, B}$, expand each factor $e^{tA} = I + tA + t^{2}A^{2}/2 + \cdots$ to order $t^{2}$, multiply out, and collect terms. The first-order term cancels by the product $e^{tA}e^{tB}e^{-tA}e^{-tB}$ being a "commutator-like" expression; the second-order term is $[A, B]$.

**Key decision point:** For part (b), the curve formula is *much* faster than the direct expansion of the inverse-matrix entries. The curve $\gamma(t) = I + tH$ has $\gamma'(0) = H$, and $(I + tH)^{-1} = I - tH + t^{2}H^{2} - \cdots$ by Neumann series (valid for $|t|$ small), differentiating to $-H$ at $t = 0$. The temptation is to compute the Jacobian of $\iota$ in coordinates (entries of $A^{-1}$ as functions of entries of $A$) — but that involves fourth-rank tensors. The choice to *use a curve* is the decisive simplification.

For part (c), the key step is recognizing that the second-order expansion captures the Lie bracket — that the *failure of commutativity* of one-parameter [[Def - Subgroup|subgroups]] is encoded at second order, not first. This is the geometric source of the commutator $[A, B]$ on $\mathfrak{gl}(n)$.

---

# Legal Operations Used

1. **Identify $T_{a}V$ with $V$ for an open subset of a vector space** (operation 8 from the topic page). $\mathrm{GL}(n)$ is open in $M_{n}(\mathbb{R})$, so $T_{I}\mathrm{GL}(n) \cong M_{n}(\mathbb{R})$.

2. **Compute the differential via a curve** (operation 1). For matrix inversion, the curve $\gamma(t) = I + tH$ realizes $H$ as a tangent vector and feeds directly into Corollary 3.25.

3. **Express the velocity of a curve in coordinates** (operation 9). For the commutator-curve in part (c), differentiate each matrix-exponential factor to second order.

---

# Hints

> [!note]- Hint 1
> For (a), $\mathrm{GL}(n)$ is open in $M_{n}(\mathbb{R})$, which is a finite-dimensional vector space. By [[Def - The Tangent Space|the canonical identification]], $T_{I}\mathrm{GL}(n) \cong M_{n}(\mathbb{R})$.

> [!note]- Hint 2
> For (b), use Corollary 3.25 (the differential via a curve). Pick the curve $\gamma(t) = I + tH$, which has $\gamma(0) = I$ and $\gamma'(0) = H$. Compute $(I + tH)^{-1}$ using the Neumann series for small $t$, and differentiate at $t = 0$.

> [!note]- Hint 3
> The Neumann series $(I + tH)^{-1} = I - tH + t^{2}H^{2} - t^{3}H^{3} + \cdots$ converges for $|t| < 1/\|H\|$. Differentiating term-by-term at $t = 0$ gives the answer $-H$.

> [!note]- Hint 4
> For (c), expand $e^{tA} = I + tA + t^{2}A^{2}/2 + O(t^{3})$ and multiply out $e^{tA}e^{tB}e^{-tA}e^{-tB}$ to order $t^{2}$. The $t^{0}$ term is $I$ and the $t^{1}$ terms cancel. The $t^{2}$ coefficient simplifies to $AB - BA = [A, B]$.

---

# Solution

The proof has three parts. Part (a) is immediate from the open-submanifold of a vector space principle. Part (b) uses a curve to compute $d\iota_{I}(H) = -H$. Part (c) is the second-order calculation revealing the commutator structure of $\mathfrak{gl}(n)$.

**Step 1: $T_{I}\mathrm{GL}(n, \mathbb{R}) \cong M_{n}(\mathbb{R})$.**

> [!note]- Derivation
> $\mathrm{GL}(n)$ is the open subset $\{A \in M_{n}(\mathbb{R}) : \det A \neq 0\}$ of the vector space $M_{n}(\mathbb{R}) \cong \mathbb{R}^{n^{2}}$ (with the standard smooth structure on a vector space, given by any linear isomorphism with $\mathbb{R}^{n^{2}}$).
>
> For any open subset $U$ of a finite-dimensional vector space $V$ and any $a \in U$, the inclusion $\iota : U \hookrightarrow V$ induces an isomorphism $d\iota_{a} : T_{a}U \to T_{a}V$. And $T_{a}V \cong V$ canonically via $v \mapsto D_{v}|_{a}$ where $D_{v}|_{a}(f) = (d/dt)|_{0} f(a + tv)$. Composing:
> $$T_{I}\mathrm{GL}(n) \cong T_{I}M_{n}(\mathbb{R}) \cong M_{n}(\mathbb{R}).$$
> So tangent vectors at $I$ to $\mathrm{GL}(n)$ are canonically identified with $n \times n$ real matrices.

**Step 2: $d\iota_{I}(H) = -H$ for the inversion map.**

> [!note]- Derivation
> Define the curve $\gamma : (-\varepsilon, \varepsilon) \to \mathrm{GL}(n)$ by $\gamma(t) = I + tH$, valid for $|t|$ small (since $I + tH$ is invertible for $|t|$ small by continuity of $\det$). Then $\gamma(0) = I$ and $\gamma'(0) = H$ (the velocity of a straight line is its direction vector, since $\mathrm{GL}(n)$ is an open subset of $M_{n}(\mathbb{R})$).
>
> By Corollary 3.25 of Lee, $d\iota_{I}(H) = (\iota \circ \gamma)'(0) = ((I + tH)^{-1})'|_{t=0}$.
>
> Compute $(I + tH)^{-1}$ using the Neumann series. For $|t| < 1/\|H\|$ (operator norm), the series converges:
> $$(I + tH)^{-1} = \sum_{k=0}^{\infty} (-tH)^{k} = I - tH + t^{2}H^{2} - t^{3}H^{3} + \cdots$$
>
> Differentiate term by term:
> $$\frac{d}{dt}\bigg|_{t=0} (I + tH)^{-1} = \frac{d}{dt}\bigg|_{t=0} (I - tH + t^{2}H^{2} - \cdots) = -H + 0 - 0 + \cdots = -H.$$
>
> So $d\iota_{I}(H) = -H$. The differential of matrix inversion at the identity is multiplication by $-1$.
>
> *Sanity check via group identity.* The inversion map satisfies $\iota \circ \iota = \mathrm{id}_{\mathrm{GL}(n)}$ (inverting twice gives the original matrix). Applying the chain rule, $d\iota_{I} \circ d\iota_{\iota(I)} = d(\mathrm{id})_{I} = \mathrm{id}$. But $\iota(I) = I^{-1} = I$, so $d\iota_{I} \circ d\iota_{I} = \mathrm{id}$. This forces $(d\iota_{I})^{2} = \mathrm{id}$ on $M_{n}(\mathbb{R})$ — and $H \mapsto -H$ does satisfy $(-)^{2} = \mathrm{id}$. ✓

**Step 3: The commutator-curve calculation.**

Expand $e^{tA}e^{tB}e^{-tA}e^{-tB}$ to second order and read off the leading term.

> [!note]- Derivation
> Taylor's formula for the matrix exponential gives, in any matrix norm,
> $$e^{\pm tA}=I\pm tA+\frac{t^2}{2}A^2+O(t^3),\qquad e^{\pm tB}=I\pm tB+\frac{t^2}{2}B^2+O(t^3).$$
> Multiplication is continuous and bilinear on the finite-dimensional matrix space, so products containing an $O(t^3)$ factor remain $O(t^3)$. Set
> $$X=A+B,\qquad P_2=\frac12A^2+AB+\frac12B^2.$$
> Multiplying the first two and last two exponentials in their displayed order yields
> $$e^{tA}e^{tB}=I+tX+t^2P_2+O(t^3),$$
> $$e^{-tA}e^{-tB}=I-tX+t^2P_2+O(t^3).$$
> Therefore
> \begin{align*}
> \gamma_{A,B}(t)
> &=\bigl(I+tX+t^2P_2\bigr)\bigl(I-tX+t^2P_2\bigr)+O(t^3)\\
> &=I+t^2(2P_2-X^2)+O(t^3)\\
> &=I+t^2(AB-BA)+O(t^3).
> \end{align*}
> The linear terms cancel, and the last equality follows from
> $$2P_2-X^2=(A^2+2AB+B^2)-(A^2+AB+BA+B^2)=AB-BA.$$
> Hence $\gamma_{A,B}'(0)=0$ and $\frac12\gamma_{A,B}''(0)=[A,B]$. The bracket is the first nonzero displacement of the group commutator, occurring at second order.
> [!note]- Complete formal solution
> *Part (a).* $\mathrm{GL}(n, \mathbb{R})$ is the open subset $\{A \in M_{n}(\mathbb{R}) : \det A \neq 0\}$ of the vector space $M_{n}(\mathbb{R})$. For an open subset of a finite-dimensional vector space, $T_{a}\mathrm{GL}(n) \cong T_{a}M_{n}(\mathbb{R}) \cong M_{n}(\mathbb{R})$ canonically (the second isomorphism being $v \mapsto D_{v}|_{a}$). So $T_{I}\mathrm{GL}(n) \cong M_{n}(\mathbb{R})$.
>
> *Part (b).* Pick the curve $\gamma(t) = I + tH$ in $\mathrm{GL}(n)$ (valid for $|t|$ small). Then $\gamma(0) = I$ and $\gamma'(0) = H$. By Lee's Corollary 3.25,
> $$d\iota_{I}(H) = (\iota \circ \gamma)'(0) = \frac{d}{dt}\bigg|_{t=0} (I + tH)^{-1}.$$
> Using the Neumann series $(I + tH)^{-1} = \sum_{k \geq 0} (-tH)^{k} = I - tH + O(t^{2})$ for $|t|$ small,
> $$\frac{d}{dt}\bigg|_{t=0} (I + tH)^{-1} = -H.$$
> Hence $d\iota_{I}(H) = -H$. Sanity check: $\iota \circ \iota = \mathrm{id}$ forces $(d\iota_{I})^{2} = \mathrm{id}$, and indeed $H \mapsto -H$ squares to identity.
>
> *Part (c).* Put $X=A+B$ and $P_2=A^2/2+AB+B^2/2$. Taylor's formula and bilinearity of matrix multiplication give
> $$e^{tA}e^{tB}=I+tX+t^2P_2+O(t^3),\qquad e^{-tA}e^{-tB}=I-tX+t^2P_2+O(t^3).$$
> Multiplying these expressions gives
> $$\gamma_{A,B}(t)=I+t^2(2P_2-X^2)+O(t^3)=I+t^2(AB-BA)+O(t^3).$$
> Thus $\gamma_{A,B}'(0)=0$ and $\frac12\gamma_{A,B}''(0)=[A,B]$. The matrix commutator is therefore the leading infinitesimal failure of the two one-parameter subgroups to commute. $\qquad\blacksquare$

---

# Key Takeaways

**The tangent space at the identity of any matrix Lie group is "matrices satisfying the linearized defining equations".** $T_{I}\mathrm{GL}(n) = M_{n}(\mathbb{R})$ — *all* matrices, with no constraint, because $\mathrm{GL}(n)$ has no defining equations beyond invertibility (and invertibility is open, not a closed constraint). For subgroups like $\mathrm{SL}(n) = \{A : \det A = 1\}$, the tangent space at $I$ is constrained by linearizing $\det A = 1$ at $I$: $d(\det)_{I}(H) = \mathrm{tr}\, H$, so $T_{I}\mathrm{SL}(n) = \{H : \mathrm{tr}\, H = 0\}$ — traceless matrices. The general pattern: for $G = \{A : f(A) = c\}$ defined by smooth equations, $T_{I}G = \ker df_{I}$ — the kernel of the differential of the defining equations. This computation pattern is repeated throughout Lie theory.

**The matrix exponential realizes every tangent vector as a velocity of a one-parameter subgroup.** For any $A \in M_{n}(\mathbb{R}) = T_{I}\mathrm{GL}(n)$, the curve $\gamma_{A}(t) = e^{tA}$ is a smooth map $\mathbb{R} \to \mathrm{GL}(n)$ with $\gamma_{A}(0) = I$ and $\gamma_{A}'(0) = A$. So every tangent vector at $I$ comes from an exponential one-parameter subgroup. This is the foundational observation of Lie theory and underlies the exponential map $\exp : \mathfrak{g} \to G$ for general Lie [[Def - Group|groups]]: $\exp$ sends Lie-algebra elements to one-parameter subgroup endpoints. The curve $\gamma_{A}(t) = e^{tA}$ replaces the linear curve $I + tA$ in this construction — both have $A$ as velocity, but $e^{tA}$ has the *group property* $e^{(s+t)A} = e^{sA}e^{tA}$, making it the natural choice for Lie-theoretic computations.

**The commutator $[A, B] = AB - BA$ measures the infinitesimal failure of group elements to commute, and this is the Lie algebra bracket.** The four-fold commutator-curve $\gamma_{A, B}(t) = e^{tA}e^{tB}e^{-tA}e^{-tB}$ would be the constant $I$ if the group were abelian. For a non-abelian group, the curve does deviate from $I$, and its leading deviation is *quadratic* in $t$ with coefficient $[A, B]$. This is the geometric source of the Lie bracket: it is the second-order term in the failure of one-parameter subgroups to commute. The bracket inherits properties from the matrix commutator — antisymmetry $[A, B] = -[B, A]$, the Jacobi identity $\big[\,[A, B], C\,\big] + \big[\,[B, C], A\,\big] + \big[\,[C, A], B\,\big] = 0$ — both of which become axioms for an abstract Lie algebra. The pattern generalizes: for any Lie group $G$, the Lie bracket on $\mathfrak{g} = T_{e}G$ is defined the same way, and the same second-order calculation works.
