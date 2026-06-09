---
type: exercise
subject: commutative-algebra
difficulty: "⭐⭐⭐"
prereqs:
  - "Def - Flat Module"
  - "Def - Tensor Product of Modules"
  - "Thm - Tensoring is Right Exact"
  - "Thm - Characterization of Flat Modules"
  - "Def - Ideal"
tags: [algebra, commutative-algebra]
---

# Problem Statement

Let $R = k[X, Y]$ ($k$ a field) and $\mathfrak m = (X, Y)$ its maximal ideal of polynomials with zero constant term. Prove:

(a) $\mathfrak m$ is a **torsion-free** $R$-module;

(b) $\mathfrak m$ is **not** a [[Def - Flat Module|flat]] $R$-module.

This is the sharpest separation in the chapter: it shows torsion-free does not imply flat, so the bottom rung of the tower free $\Rightarrow$ projective $\Rightarrow$ flat $\Rightarrow$ torsion-free is strict. As a guide, first find an exact sequence $R^t \to R^n \to \mathfrak m \to 0$ and a description $\mathfrak m \otimes_R \mathfrak m \cong \mathfrak m^{\oplus n}/(\text{relations})$, then exhibit a non-zero element of $\mathfrak m\otimes\mathfrak m$ killed by the multiplication map $\mathfrak m\otimes\mathfrak m \to \mathfrak m^2$.

**Recall:**

The objects in play are flat modules, torsion-freeness, the tensor product, and the presentation of a finitely generated module.

![[Def - Flat Module#The Definition]]

$M$ is **torsion-free** if $rm = 0$ with $r$ a non-zero-divisor forces $m = 0$. A submodule of a domain $R$ is automatically torsion-free.

![[Thm - Characterization of Flat Modules#Statement]]

For an ideal $I$, the natural map $I \otimes_R M \to IM$, $i\otimes m\mapsto im$, is surjective by [[Thm - Tensoring is Right Exact|right-exactness]]; $M$ is flat iff this map is *injective* for every finitely generated ideal $I$. Taking $M = \mathfrak m$ and $I = \mathfrak m$, non-flatness will follow from a non-zero element of $\ker(\mathfrak m\otimes\mathfrak m \to \mathfrak m^2)$.

The bridge that makes the proof run — *the Koszul relation*: in $\mathfrak m\otimes_R\mathfrak m$ the element $Y\otimes X - X\otimes Y$ is non-zero, yet it maps to $YX - XY = 0$ under multiplication. That single element witnesses the failure of injectivity, hence of flatness.

---

# Convergent Strategy

**Problem class.** This is the *hardest* separating-example problem: refute flatness for a module that is *torsion-free*, so the cheap "find torsion" refutation is unavailable. As the [[Commutative Algebra III — Flatness and Exactness]] strategy records, the torsion-free-but-not-flat band is exactly where the [[Thm - Characterization of Flat Modules|finitely generated ideal criterion]] must be invoked directly, hunting for a subtle tensor relation.

**Assumption pattern.** The trigger is "torsion-free, so test flatness on a genuine injection, not on $\mu_r$." Torsion-freeness only checks the maps $\mu_r$; flatness over the $2$-dimensional ring $k[X,Y]$ sees more. The recognisable pattern is that $\mathfrak m$ needs *two* generators with a *syzygy* ($Y\cdot X - X\cdot Y = 0$), and that syzygy is what tensoring detects.

**Theorem routing.** (a) Torsion-free: $\mathfrak m \subseteq R$ with $R = k[X,Y]$ a domain, and a submodule of a domain is torsion-free. (b) Not flat: use the criterion that flatness requires $\mathfrak m\otimes_R\mathfrak m \to \mathfrak m^2$ injective. Tensor the inclusion $\mathfrak m\hookrightarrow R$ with $\mathfrak m$; by [[Thm - Characterization of Flat Modules|the ideal criterion]] flatness would force $\mathfrak m\otimes\mathfrak m\to\mathfrak m\cdot\mathfrak m = \mathfrak m^2$ injective. Exhibit $\tau = Y\otimes X - X\otimes Y \in \mathfrak m\otimes\mathfrak m$, show $\tau \neq 0$ (via a bilinear test map), and note $\tau \mapsto YX - XY = 0$. Non-injectivity refutes flatness.

**Key decision point.** Two non-obvious moves. First, *which injection to tensor* — the inclusion $\mathfrak m\hookrightarrow R$, giving the criterion map $\mathfrak m\otimes\mathfrak m\to\mathfrak m^2$, is the right one (not $\mu_r$, which only sees torsion). Second, and the genuine creative step, *proving $\tau = Y\otimes X - X\otimes Y \neq 0$ in $\mathfrak m\otimes\mathfrak m$*: this cannot be seen by the multiplication map (which kills it), so one must build a *different* bilinear map $\mathfrak m\times\mathfrak m\to V$ that separates $Y\otimes X$ from $X\otimes Y$. The standard choice uses the residue field: send $(f, g)$ to $\overline{(\partial f, \partial g)}$ in a $2$-dimensional space over $k$, detecting the antisymmetry. The natural wrong instinct — to compute in $\mathfrak m\otimes\mathfrak m$ by manipulating pure tensors — fails because the module is subtle; you *must* test against a separating bilinear form.

---

# Legal Operations Used

This solution deploys the following legal operations from [[Commutative Algebra III — Flatness and Exactness#Legal Operations|the topic page's Legal Operations]]:

1. **Use the finitely generated ideal criterion (operation 4).** Flatness of $M$ requires $I\otimes M\to IM$ injective for finitely generated $I$; take $I = M = \mathfrak m$.

2. **Tensor the inclusion $\mathfrak m\hookrightarrow R$ (operation 3, generalized).** This is the injection whose tensor with $\mathfrak m$ produces the criterion map $\mathfrak m\otimes\mathfrak m\to\mathfrak m^2$.

3. **Detect a non-zero tensor with a separating bilinear map (universal property).** To prove $Y\otimes X - X\otimes Y \neq 0$, build a bilinear $\mathfrak m\times\mathfrak m\to V$ that distinguishes the two pure tensors.

4. **Recognise a submodule of a domain as torsion-free (operation 5, descent).** $\mathfrak m\subseteq R$ inherits torsion-freeness from the domain $R$.

---

# Hints

> [!note]- Hint 1
> Part (a) is one line: where does $\mathfrak m$ live, and is that ambient module torsion-free? For part (b), the cheap refutation (find torsion) is *unavailable* by (a). So you must use a real flatness criterion. Which one reduces flatness to a single concrete map per ideal?

> [!note]- Hint 2
> (a) $\mathfrak m \subseteq R = k[X,Y]$, a domain; submodules of domains are torsion-free. (b) By [[Thm - Characterization of Flat Modules|the ideal criterion]], if $\mathfrak m$ were flat then $\mathfrak m\otimes_R\mathfrak m \to \mathfrak m^2$, $f\otimes g\mapsto fg$, would be injective. Look for a non-zero kernel element. The two generators $X, Y$ satisfy a relation — what is $Y\cdot X - X\cdot Y$?

> [!note]- Hint 3
> Consider $\tau = Y\otimes X - X\otimes Y \in \mathfrak m\otimes_R\mathfrak m$. Under multiplication it goes to $YX - XY = 0$. So if $\tau \neq 0$, the multiplication map is not injective and $\mathfrak m$ is not flat. The whole problem reduces to: *show $\tau \neq 0$ in $\mathfrak m\otimes\mathfrak m$.*

> [!note]- Hint 4
> To show $\tau\neq 0$, find a bilinear map $\beta : \mathfrak m\times\mathfrak m \to V$ ($V$ a $k$-vector space) with $\beta(Y, X)\neq\beta(X, Y)$. The residue field works: each $f\in\mathfrak m$ has a linear part $\ell(f) = (\partial_X f(0), \partial_Y f(0))\in k^2$. Set $\beta(f, g) = \ell(f)\otimes_k\ell(g) \in k^2\otimes_k k^2$. Then $\beta(Y, X) = e_2\otimes e_1$ and $\beta(X, Y) = e_1\otimes e_2$ are distinct, so the induced map sends $\tau \mapsto e_2\otimes e_1 - e_1\otimes e_2 \neq 0$. Hence $\tau\neq 0$.

---

# Solution

Part (a) is immediate; the content is part (b), and it is the chapter's one genuinely intricate computation. The plan: invoke the [[Thm - Characterization of Flat Modules|finitely generated ideal criterion]] to reduce flatness of $\mathfrak m$ to injectivity of multiplication $\mathfrak m\otimes\mathfrak m\to\mathfrak m^2$; exhibit the Koszul element $\tau = Y\otimes X - X\otimes Y$ in the kernel; and prove $\tau\neq 0$ by testing against a bilinear map built from the linear parts of polynomials, which detects the antisymmetry the multiplication map hides.

**Step 1: $\mathfrak m$ is torsion-free.**

$\mathfrak m$ is a submodule of the domain $R = k[X,Y]$, hence torsion-free.

> [!note]- Derivation
> $R = k[X, Y]$ is an [[Def - Integral Domain|integral domain]] (a polynomial ring over a field), so its only zero-divisor is $0$, and every non-zero element is a non-zero-divisor. If $r\in R$ is non-zero and $f\in\mathfrak m\subseteq R$ with $rf = 0$, then $f = 0$ because $R$ has no zero-divisors. So no non-zero element of $\mathfrak m$ is annihilated by a non-zero-divisor: $\mathfrak m$ is torsion-free. (Every submodule of a torsion-free module — in particular of a domain $R$ viewed over itself — is torsion-free.)

**Step 2: Reduce non-flatness to non-injectivity of $\mathfrak m\otimes\mathfrak m \to \mathfrak m^2$.**

If $\mathfrak m$ were flat, the multiplication map $\mathfrak m\otimes_R\mathfrak m \to \mathfrak m^2$ would be injective.

> [!note]- Derivation
> The inclusion $\iota : \mathfrak m \hookrightarrow R$ is an injective $R$-linear map. By [[Thm - Characterization of Flat Modules|the ideal criterion for flatness]], if $\mathfrak m$ is flat then for every finitely generated ideal $I$ the natural map $I\otimes_R\mathfrak m \to I\mathfrak m$ is injective. Take $I = \mathfrak m$:
> $$\mu : \mathfrak m\otimes_R\mathfrak m \longrightarrow \mathfrak m\cdot\mathfrak m = \mathfrak m^2, \qquad f\otimes g \mapsto fg,$$
> would have to be injective. (Equivalently, tensoring $\iota : \mathfrak m\hookrightarrow R$ with $\mathfrak m$ gives $\mathfrak m\otimes\mathfrak m \to R\otimes\mathfrak m = \mathfrak m$, with image $\mathfrak m^2$; flatness demands it be injective.) We now show $\mu$ is *not* injective.

**Step 3: The Koszul element lies in the kernel of $\mu$.**

$\tau := Y\otimes X - X\otimes Y \in \mathfrak m\otimes_R\mathfrak m$ satisfies $\mu(\tau) = 0$.

> [!note]- Derivation
> Both $X, Y\in\mathfrak m$, so $\tau = Y\otimes X - X\otimes Y$ is a well-defined element of $\mathfrak m\otimes_R\mathfrak m$. Applying $\mu$:
> $$\mu(\tau) = \mu(Y\otimes X) - \mu(X\otimes Y) = YX - XY = 0,$$
> since $R$ is commutative. So $\tau\in\ker\mu$. If we show $\tau\neq 0$, then $\mu$ has non-trivial kernel and is not injective.

**Step 4: $\tau \neq 0$ in $\mathfrak m\otimes_R\mathfrak m$.**

A bilinear map built from linear parts separates $Y\otimes X$ from $X\otimes Y$, so $\tau \neq 0$.

> [!note]- Derivation
> We cannot detect $\tau$ with $\mu$ (it kills $\tau$); we need a *different* bilinear map. For $f\in\mathfrak m$, define its **linear part** $\ell(f) = (a, b)\in k^2$, where $f = aX + bY + (\text{higher order and products})$; equivalently $\ell(f) = (\partial_X f(0,0),\, \partial_Y f(0,0))$. The map $\ell : \mathfrak m \to k^2$ is $k$-linear and is exactly the projection $\mathfrak m \to \mathfrak m/\mathfrak m^2 \cong k^2$ onto the cotangent space, with $\ell(X) = e_1 = (1,0)$, $\ell(Y) = e_2 = (0,1)$.
>
> Define a map
> $$\beta : \mathfrak m \times \mathfrak m \to k^2\otimes_k k^2, \qquad \beta(f, g) = \ell(f)\otimes_k\ell(g).$$
> This $\beta$ is $R$-bilinear: it is biadditive, and $\beta(rf, g) = \ell(rf)\otimes\ell(g)$. We must check $R$-bilinearity over $R$, i.e. $\beta(rf, g) = \beta(f, rg)$ in the appropriate sense — and here is the key point: for $r\in R$ and $f\in\mathfrak m$, $\ell(rf) = r(0,0)\cdot\ell(f) = r(0)\,\ell(f)$ where $r(0)$ is the constant term, because higher-order terms of $r$ multiply $f$ into $\mathfrak m^2$, killed by $\ell$. So $\beta(rf, g) = r(0)\,\ell(f)\otimes\ell(g) = \ell(f)\otimes r(0)\ell(g) = \beta(f, rg)$. Thus $\beta$ is $R$-bilinear and factors through an $R$-linear (indeed $k$-linear) map
> $$\bar\beta : \mathfrak m\otimes_R\mathfrak m \to k^2\otimes_k k^2.$$
> Evaluate on $\tau$:
> $$\bar\beta(\tau) = \ell(Y)\otimes\ell(X) - \ell(X)\otimes\ell(Y) = e_2\otimes e_1 - e_1\otimes e_2.$$
> In $k^2\otimes_k k^2$ (a $4$-dimensional space with basis $e_i\otimes e_j$), the element $e_2\otimes e_1 - e_1\otimes e_2$ is non-zero — it is a non-trivial combination of distinct basis vectors. Hence $\bar\beta(\tau)\neq 0$, so $\tau\neq 0$ in $\mathfrak m\otimes_R\mathfrak m$.

**Step 5: Conclude $\mathfrak m$ is not flat.**

> [!note]- Derivation
> By Steps 3 and 4, $\tau = Y\otimes X - X\otimes Y$ is a *non-zero* element of $\mathfrak m\otimes_R\mathfrak m$ lying in $\ker\mu$. So $\mu : \mathfrak m\otimes_R\mathfrak m\to\mathfrak m^2$ is not injective. By Step 2, flatness of $\mathfrak m$ would force $\mu$ injective. Therefore $\mathfrak m$ is **not flat**. Combined with Step 1, $\mathfrak m$ is torsion-free but not flat. $\blacksquare$

> [!note]- Complete formal solution
> Let $R = k[X,Y]$, $\mathfrak m = (X, Y)$.
>
> **(a) Torsion-free.** $R$ is a domain and $\mathfrak m\subseteq R$, so any non-zero-divisor $r$ with $rf = 0$ ($f\in\mathfrak m$) forces $f = 0$. Hence $\mathfrak m$ is torsion-free.
>
> **(b) Not flat.** By [[Thm - Characterization of Flat Modules|the ideal criterion]], flatness of $\mathfrak m$ would make $\mu : \mathfrak m\otimes_R\mathfrak m\to\mathfrak m^2$, $f\otimes g\mapsto fg$, injective. Set $\tau = Y\otimes X - X\otimes Y$. Then $\mu(\tau) = YX - XY = 0$. To see $\tau\neq 0$, let $\ell : \mathfrak m\to k^2 = \mathfrak m/\mathfrak m^2$ be the linear-part map ($\ell(X) = e_1$, $\ell(Y) = e_2$) and $\beta(f,g) = \ell(f)\otimes_k\ell(g)$; since $\ell(rf) = r(0)\ell(f)$, $\beta$ is $R$-bilinear and induces $\bar\beta : \mathfrak m\otimes_R\mathfrak m\to k^2\otimes_k k^2$ with $\bar\beta(\tau) = e_2\otimes e_1 - e_1\otimes e_2 \neq 0$. So $\tau\neq 0$, $\mu$ is not injective, and $\mathfrak m$ is not flat.
>
> Hence $\mathfrak m$ is torsion-free but not flat. $\blacksquare$

> [!warning] Illegal but tempting route: "the multiplication map shows $\tau = 0$"
> One might try to *prove* $\tau = 0$ by applying the multiplication map $\mu$ and seeing $YX - XY = 0$, concluding the element vanishes. This is exactly backwards: $\mu(\tau) = 0$ shows $\tau$ is in the *kernel* of $\mu$, not that $\tau$ is zero in $\mathfrak m\otimes\mathfrak m$. A pure-tensor expression can be non-zero even when one particular linear functional (here $\mu$) annihilates it. The only way to certify $\tau\neq 0$ is to find a *different* map — a separating bilinear form like $\beta$ — that does *not* kill it. The whole difficulty of the problem is precisely that the obvious map cannot see $\tau$.

---

# Key Takeaways

**Torsion-free does not imply flat, and the witness is always a syzygy among generators that tensoring fails to respect.** The maximal ideal $(X, Y)$ is torsion-free for the trivial reason that it sits in a domain, yet it is not flat because its two generators satisfy the Koszul relation $Y\cdot X - X\cdot Y = 0$, and this relation produces a non-zero element $Y\otimes X - X\otimes Y$ of $\mathfrak m\otimes\mathfrak m$ that the multiplication map kills. The reusable principle: over a ring of dimension $\geq 2$, an ideal needing two or more generators carries *relations* (syzygies) among them, and flatness is exactly the demand that tensoring not create spurious kernel elements from those relations. The trigger to suspect non-flatness despite torsion-freeness is "a module with several generators and a non-trivial relation"; the reaction is to tensor with itself (or with $R/\mathfrak m$) and hunt for the antisymmetrized relation in the kernel of multiplication. This is why the gap between torsion-free and flat *opens precisely in dimension $2$* — in dimension $1$ (a PID) every ideal is principal, has no syzygies, and torsion-free coincides with flat.

**To prove a tensor is non-zero, never compute inside the tensor product — test it against a separating bilinear map.** The single hardest step is showing $\tau\neq 0$, and the only reliable method is the universal property in its detecting form: a pure-tensor expression $\sum f_i\otimes g_i$ is non-zero if and only if *some* bilinear map sends it to something non-zero. Here the multiplication map is useless (it kills $\tau$), so one constructs a bilinear map from the *linear parts* $\ell : \mathfrak m\to\mathfrak m/\mathfrak m^2 = k^2$ — the cotangent space — which converts the polynomial antisymmetry into the visible $e_2\otimes e_1 - e_1\otimes e_2 \neq 0$ in $k^2\otimes_k k^2$. The transferable diagnostic: whenever you need "this tensor is non-zero," do not manipulate it in place; build a bilinear functional designed to separate the offending pure tensors, and the cotangent/residue-field map is the canonical first thing to try because it linearizes the module at the point. The trap of "applying the multiplication map to show $\tau = 0$" is the standard error, and recognising that $\mu(\tau) = 0$ means "$\tau\in\ker\mu$", not "$\tau = 0$", is the conceptual gate.

**This is the geometric content of flatness: $(X,Y)$ is the ideal of the origin in the plane, and its non-flatness is the algebraic shadow of a family that tears.** Under the algebra–geometry dictionary, $\mathfrak m = (X,Y)$ is the maximal ideal of the point $(0,0)\in \mathbb{A}^2$, and the failure of flatness here is the same phenomenon that makes the **blow-up** of the plane at the origin a non-flat (or carefully-constructed) operation, and that makes $k[X,Y]/(XY)$ — two crossing lines — non-flat over $k[X]$. The cotangent space $\mathfrak m/\mathfrak m^2 \cong k^2$ that detects $\tau$ is precisely the *tangent space at the origin*, which is why the obstruction is two-dimensional. The deep takeaway, connecting to the chapter's spine: flatness fails exactly where the fibre or the local structure *jumps*, and the smallest such jump is the two generators of the maximal ideal of a smooth point in dimension $2$. This completes the tower's last strict inclusion — torsion-free $\supsetneq$ flat — and is the companion to [[Ex - A monic-polynomial quotient is a flat algebra]], which exhibits the *flat* (non-tearing) family of points for contrast, and to [[Ex - Free implies projective implies flat implies torsion-free]] for the full chain.
