---
type: exercise
subject: gauge-theory
prereqs:
  - "Def - Connection Matrix and Local Form of a Connection"
  - "Def - Connection on a Vector Bundle"
  - "Thm - Gauge Transformation Law for Connection 1-Forms"
difficulty: "⭐"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $U \subseteq \mathbb{R}^n$ be open and let $E = U \times \mathbb{R}^k$ be the **product bundle** of rank $k$ over $U$. Equip $E$ with the **product connection** $\nabla = d$: identifying a section $s \in \Gamma(E)$ with a map $s = (s^1, \dots, s^k) : U \to \mathbb{R}^k$, set $\nabla s = ds$ (the componentwise exterior derivative). Let $e = (e_1, \dots, e_k)$ be the **standard frame**, $e_j(x) = (x, \varepsilon_j)$ with $\varepsilon_1, \dots, \varepsilon_k$ the standard basis of $\mathbb{R}^k$, so that each $e_j$ is a *constant* section. Let $g : U \to GL_k(\mathbb{R})$ be a smooth map (a "moving frame change"; the word *rotated* refers to the case $g : U \to O(k)$, but nothing below uses orthogonality), and form the new frame $e' = eg$, whose $j$-th member is $e'_j = \sum_{a=1}^k e_a\, g^a{}_j$.

Prove the following.

1. **(Direct computation.)** The connection matrix $A' = A(\nabla, e')$ of the product connection with respect to the rotated frame $e'$ is
$$A' = g^{-1}\,dg \in \Omega^1\big(U; \mathfrak{gl}_k(\mathbb{R})\big),$$
computed directly from the definition $\nabla e' = e' \cdot A'$.
2. **(Via the transformation law.)** The same $A'$ results from the frame-change law (Haydys equation (14))
$$A(\nabla, e') = g^{-1} A(\nabla, e)\, g + g^{-1}\,dg,$$
using that $A(\nabla, e) = 0$ for the standard frame.
3. **(The rank-one case.)** When $k = 1$ and $g = e^{f}$ for a function $f \in C^\infty(U)$ (so $g : U \to \mathbb{R}_{>0} = GL_1(\mathbb{R})^\circ$), the connection matrix reduces to the single $1$-form
$$A' = df.$$

**Recall:**

The objects in play are the product connection $d$, the connection matrix of a connection in a local frame, and the frame-change transformation law (14).

![[Def - Connection on a Vector Bundle#The Definition]]

So a **connection** is an $\mathbb{R}$-linear $\nabla : \Gamma(E) \to \Omega^1(U; E)$ with $\nabla(fs) = df\otimes s + f\,\nabla s$; the **product connection** $d$ on $U \times \mathbb{R}^k$ differentiates coefficients, $\nabla(s^1, \dots, s^k) = (ds^1, \dots, ds^k)$, so that $\nabla e_j = de_j = 0$ for every constant standard basis section $e_j$.

![[Def - Connection Matrix and Local Form of a Connection#The Definition]]

Restating what is used: for a local frame $e = (e_1, \dots, e_k)$ (a row of pointwise-linearly-independent sections), the **connection matrix** $A = A(\nabla, e) \in \Omega^1(U; \mathfrak{gl}_k(\mathbb{R}))$ is the unique $k\times k$ matrix of $1$-forms determined by
$$\nabla e = e\cdot A, \qquad \text{that is} \qquad \nabla e_j = \sum_{a=1}^k e_a\, A^a{}_j,$$
and then a section $s = e\sigma$ (with $\sigma$ the column of coefficients) has $\nabla s = e\,(d\sigma + A\sigma)$, abbreviated "$\nabla = d + A$".

> [!warning] Convention: row-vector frames
> This series follows Haydys's row-vector convention $\nabla e = e\cdot A$, in which the frame $e$ is a *row* $(e_1, \dots, e_k)$ and $A$ acts on the right. In the Cartan / Riemannian-geometry convention used on [[Def - Connection 1-Forms (Cartan)|the Cartan connection-form page]] one writes $\nabla e_b = e_a\,\omega^a{}_b$; the matrix $\omega = (\omega^a{}_b)$ is the *same* matrix $A$, only the indexing convention differs. Consequently the frame-change law and all computations below are identical in either convention.

The transformation law (14) restated, with its proof lodged on a fully proved page:

> **Frame-change law for the connection matrix (Haydys (14)).** If $e' = eg$ for a smooth $g : U \to GL_k(\mathbb{R})$, then the connection matrices with respect to $e$ and $e'$ are related by
> $$A(\nabla, e') = g^{-1}\,A(\nabla, e)\,g + g^{-1}\,dg.$$

A complete proof of this identity is given on [[Thm - Gauge Transformation Law for Connection 1-Forms]] (stated there in the Cartan convention, which as noted is the same matrix); in this exercise we re-derive its specialisation $A = 0$ from scratch in part 1 and then confirm it against (14) in part 2.

---

# Convergent Strategy

**Problem class.** This is a *compute-an-invariant-two-ways-and-reconcile* drill: the same quantity $A'$ is obtained once from first principles (the defining equation $\nabla e' = e'A'$) and once from a general transformation formula, and the two are checked to agree. Such exercises are the standard way to *internalise* a transformation law — you see the general formula collapse to a concrete answer, and you confirm that the formula was not needed when a direct computation is available, which is exactly the reassurance one wants before trusting the formula in cases where direct computation is infeasible.

**Assumption pattern.** The single simplifying hypothesis is that the base connection is the *product* connection, whose connection matrix in the standard frame vanishes: $A(\nabla, e) = 0$. This is what makes the conjugation term $g^{-1}Ag$ in (14) disappear, leaving only the *inhomogeneous* term $g^{-1}\,dg$ — the pure "frame-rotation" contribution. The lesson to carry away is that $g^{-1}\,dg$ is the connection matrix produced *entirely by changing the frame*, with no curvature of the connection involved (indeed, as computed in [[Ex - Curvature of d plus A on the Trivial Bundle over the Plane|the curvature drill]], the curvature of $\nabla = d$ is zero in every frame).

**Theorem routing.** For part 1, route through the matrix form of the [[Def - Connection on a Vector Bundle|Leibniz rule]]: expand $\nabla(eg)$ term by term using $\nabla e_a = 0$, obtain $\nabla e' = e\,dg$, then rewrite $e = e' g^{-1}$ to read off $A' = g^{-1}\,dg$. For part 2, substitute $A(\nabla, e) = 0$ into the [[Thm - Gauge Transformation Law for Connection 1-Forms|frame-change law (14)]] and observe the same answer. For part 3, substitute $k = 1$, $g = e^f$, and simplify $g^{-1}\,dg = e^{-f}\,d(e^f)$ with the chain rule.

**Key decision point.** The only step that requires care is the *matrix product rule* $\nabla(eg) = (\nabla e)\,g + e\,dg$, which is the Leibniz rule applied member-by-member to the columns of the frame; getting the placement of $g$ and $dg$ right (and, in part 1, remembering to convert the answer back into the $e'$ frame by multiplying by $g^{-1}$ on the *left*) is the whole content of the drill. Everything else is substitution.

---

# Legal Operations Used

Where the topic page for §2.2 exists, these are its Legal Operations, and the orchestrator will reconcile the numbering.

1. **Read off the connection matrix from the defining equation $\nabla e = e\cdot A$.** The connection matrix is characterised by how $\nabla$ acts on the frame; to find $A'$ one computes $\nabla e'$ and expresses the result as $e'$ times a matrix of $1$-forms.

2. **Apply the Leibniz rule columnwise to a frame change (the matrix product rule).** For $e' = eg$, differentiate each $e'_j = \sum_a e_a g^a{}_j$ by the Leibniz rule to obtain $\nabla e' = (\nabla e)\,g + e\,dg$.

3. **Use that constant sections have vanishing product-connection derivative.** $\nabla e_a = de_a = 0$, so the conjugation term drops and only $e\,dg$ survives.

4. **Change back to the new frame using $e = e'g^{-1}$.** To express $\nabla e' = e\,dg$ in the form $e'\cdot A'$, substitute $e = e'g^{-1}$, giving $A' = g^{-1}\,dg$.

5. **Specialise the general transformation law (14) by substituting $A = 0$.** Confirm the direct answer against the [[Thm - Gauge Transformation Law for Connection 1-Forms|frame-change law]] with the standard-frame value $A(\nabla, e) = 0$.

6. **Reduce a $GL_1$ frame change to a logarithmic derivative.** For $k = 1$ and $g = e^f$, compute $g^{-1}\,dg = df$ via the chain rule — the scalar shadow of the general formula.

---

# Hints

> [!note]- Hint 1
> What is the connection matrix of the product connection $\nabla = d$ in the *standard* frame $e$? Each $e_j$ is a constant section, so what is $\nabla e_j$? This gives $A(\nabla, e)$, the input to formula (14).

> [!note]- Hint 2
> For the direct computation, apply $\nabla$ to $e' = eg$ using the Leibniz rule on each column $e'_j = \sum_a g^a{}_j\, e_a$. You will get two kinds of term: one with $\nabla e_a$ (which vanishes) and one with $dg^a{}_j$. Assemble the survivors into a matrix equation $\nabla e' = e\,(\,\cdot\,)$.

> [!note]- Hint 3
> You now have $\nabla e' = e\,dg$, but the connection matrix $A'$ is defined by $\nabla e' = e'\cdot A'$, in the *primed* frame. Express the old frame in terms of the new one: from $e' = eg$, what is $e$ in terms of $e'$? Substitute and read off $A'$.

> [!note]- Hint 4
> For part 2, put $A(\nabla, e) = 0$ into $A' = g^{-1}Ag + g^{-1}dg$. For part 3, set $k = 1$ so all matrices are scalars, $g = e^f$, and compute $g^{-1}\,dg = e^{-f}\,d(e^f)$ using $d(e^f) = e^f\,df$.

---

# Solution

The product connection has vanishing connection matrix in the standard frame, so both routes to $A'$ isolate the single inhomogeneous term $g^{-1}\,dg$. The direct computation differentiates the frame change $e' = eg$ columnwise and converts back to the new frame; the transformation law (14) reaches the same place by killing its conjugation term with $A = 0$; and the rank-one case is the scalar chain rule. We fix a smooth $g : U \to GL_k(\mathbb{R})$ throughout, and write $g^a{}_j$ for its matrix entries, each a smooth function on $U$.

**Step 1: The connection matrix of $\nabla = d$ in the standard frame vanishes.**

$A(\nabla, e) = 0$.

> [!note]- Derivation
> Each standard basis section $e_a$ is constant: $e_a(x) = (x, \varepsilon_a)$ with $\varepsilon_a \in \mathbb{R}^k$ independent of $x$. The product connection differentiates coefficients, so
> $$\nabla e_a = d e_a = 0 \qquad \text{(}e_a \text{ is a constant section; } \nabla = d\text{).}$$
> Comparing with the defining equation $\nabla e = e\cdot A(\nabla, e)$, and using that the frame $e$ is pointwise a basis (so the coefficients of $\nabla e_a$ in the frame $e$ are unique), every entry of $A(\nabla, e)$ is the zero $1$-form:
> $$A(\nabla, e) = 0.$$

**Step 2: Direct computation — $\nabla e' = e\,dg$, hence $A' = g^{-1}\,dg$ (part 1).**

Differentiating $e' = eg$ columnwise and rewriting in the new frame gives $A' = g^{-1}\,dg$.

> [!note]- Derivation
> Fix a column index $j$. The $j$-th member of the new frame is $e'_j = \sum_{a=1}^k g^a{}_j\, e_a$. Apply $\nabla$, using $\mathbb{R}$-linearity and the Leibniz rule $\nabla(g^a{}_j\, e_a) = dg^a{}_j\otimes e_a + g^a{}_j\,\nabla e_a$ on each summand:
> $$\nabla e'_j = \sum_{a=1}^k \Big( dg^a{}_j \otimes e_a + g^a{}_j\,\nabla e_a\Big) = \sum_{a=1}^k dg^a{}_j\otimes e_a \qquad \text{(Leibniz rule; } \nabla e_a = 0 \text{ by Step 1).}$$
> In matrix notation, with $e = (e_1, \dots, e_k)$ a row and $dg = (dg^a{}_j)$ the matrix of differentials of the entries, this is the **matrix product rule specialised to a constant frame**:
> $$\nabla e' = (\nabla e)\,g + e\,dg = 0 + e\,dg = e\,dg \qquad \text{(operation 2, with } \nabla e = 0\text{).}$$
> This expresses $\nabla e'$ in the *old* frame $e$. To extract the connection matrix $A'$, which is defined by $\nabla e' = e'\cdot A'$, we must rewrite the right-hand side in the *new* frame. Since $g$ is invertible pointwise, $e' = eg$ gives $e = e' g^{-1}$; substituting,
> $$\nabla e' = e\,dg = (e' g^{-1})\,dg = e'\,\big(g^{-1}\,dg\big) \qquad \text{(operation 4, } e = e'g^{-1}\text{).}$$
> Comparing with $\nabla e' = e'\cdot A'$ and using uniqueness of the connection matrix in the frame $e'$,
> $$A' = A(\nabla, e') = g^{-1}\,dg.$$
> This lies in $\Omega^1(U; \mathfrak{gl}_k(\mathbb{R}))$: its entries are the $1$-forms $(g^{-1}\,dg)^a{}_j = \sum_b (g^{-1})^a{}_b\, dg^b{}_j$, smooth because $g$ and $g^{-1}$ are. **This is part 1.**

**Step 3: Via the transformation law (14) — same answer (part 2).**

Substituting $A(\nabla, e) = 0$ into (14) reproduces $A' = g^{-1}\,dg$.

> [!note]- Derivation
> The [[Thm - Gauge Transformation Law for Connection 1-Forms|frame-change law]] restated in the recall reads, for $e' = eg$,
> $$A(\nabla, e') = g^{-1}\,A(\nabla, e)\,g + g^{-1}\,dg.$$
> By Step 1, $A(\nabla, e) = 0$, so the conjugation term vanishes:
> $$A(\nabla, e') = g^{-1}\cdot 0\cdot g + g^{-1}\,dg = g^{-1}\,dg \qquad \text{(substituting } A(\nabla, e) = 0\text{).}$$
> This agrees with the direct computation of Step 2, as it must. **This is part 2.** The agreement is a check on the transformation law: the term $g^{-1}Ag$ (present when the base connection is not flat, or when the base frame is not $\nabla$-parallel) is absent here precisely because the standard frame is $\nabla$-parallel, and $g^{-1}\,dg$ is the entire, purely frame-rotational, contribution.
>
> *Sanity check (constant $g$).* If $g$ is a *constant* matrix, then $dg = 0$, so $A' = g^{-1}\cdot 0 = 0$: the connection matrix stays zero. This is correct — a constant change of a $\nabla$-parallel frame is again $\nabla$-parallel — and matches the calibration remark on the [[Def - Connection Matrix and Local Form of a Connection|connection-matrix page]] that (14) reduces to $A' = A$ when $g$ is constant.

**Step 4: The rank-one case — $A' = df$ (part 3).**

For $k = 1$ and $g = e^f$, the matrix $A'$ is the single $1$-form $df$.

> [!note]- Derivation
> When $k = 1$ all matrices are $1\times 1$, i.e. scalars, and the algebra is commutative. Take $g = e^{f}$ with $f \in C^\infty(U)$; then $g$ is a smooth positive function, $g^{-1} = e^{-f}$, and by the chain rule $d(e^f) = e^{f}\,df$. Hence
> $$A' = g^{-1}\,dg = e^{-f}\,d\big(e^{f}\big) = e^{-f}\big(e^{f}\,df\big) = df \qquad \text{(chain rule } d(e^f) = e^f\,df\text{; then } e^{-f}e^f = 1\text{).}$$
> So $A' = df$, an *exact* $1$-form. **This is part 3.** The exactness is meaningful: in rank one the frame change $g = e^f$ contributes the connection matrix $df$, which is exactly the gauge transformation $A \mapsto A + df$ of an abelian ($U(1)$-type) connection — the additive, curl-free "pure gauge" term. Its being exact is why it carries no curvature: $dA' = d(df) = 0$.

> [!note]- Complete formal solution
> **Claim.** For the product connection $\nabla = d$ on $U \times \mathbb{R}^k$ and the frame change $e' = eg$ with $g : U \to GL_k(\mathbb{R})$ smooth, the connection matrix in the new frame is $A(\nabla, e') = g^{-1}\,dg$; for $k = 1$ and $g = e^f$ it is $df$.
>
> *Proof.* The standard frame consists of constant sections $e_a$, so $\nabla e_a = de_a = 0$ and $A(\nabla, e) = 0$.
>
> *Direct.* For each $j$, by $\mathbb{R}$-linearity and the Leibniz rule,
> $$\nabla e'_j = \nabla\Big(\sum_a g^a{}_j e_a\Big) = \sum_a\big(dg^a{}_j\otimes e_a + g^a{}_j\,\nabla e_a\big) = \sum_a dg^a{}_j\otimes e_a,$$
> i.e. $\nabla e' = e\,dg$. Since $g \in GL_k$, $e = e'g^{-1}$, so $\nabla e' = e'(g^{-1}\,dg)$, and comparison with $\nabla e' = e'\cdot A'$ gives
> $$A(\nabla, e') = g^{-1}\,dg \in \Omega^1(U; \mathfrak{gl}_k(\mathbb{R})).$$
>
> *Via (14).* The frame-change law $A(\nabla, e') = g^{-1}A(\nabla, e)g + g^{-1}\,dg$ with $A(\nabla, e) = 0$ gives $A(\nabla, e') = g^{-1}\,dg$, the same answer.
>
> *Rank one.* For $k = 1$, $g = e^f$, commutativity and the chain rule give
> $$A(\nabla, e') = e^{-f}\,d(e^f) = e^{-f}\,e^f\,df = df. \qquad \blacksquare$$

> [!warning] Illegal but tempting: forgetting to change back to the new frame
> A common error in part 1 is to compute $\nabla e' = e\,dg$ and then declare "$A' = dg$", reading the coefficient matrix while it is still expressed in the *old* frame $e$. This is wrong: the connection matrix in the frame $e'$ is defined by $\nabla e' = e'\cdot A'$, so one must first rewrite $\nabla e' = e\,dg$ as $e'(g^{-1}\,dg)$ using $e = e'g^{-1}$. The extra left factor of $g^{-1}$ is exactly what makes the answer transform correctly and match (14); dropping it would even fail the constant-$g$ sanity check only accidentally (there $dg = 0$), but would give the wrong law in general. The operation that makes "$A' = dg$" legal is precisely *not changing frames* — that is, reporting the coefficients of $\nabla e'$ in the basis $e$, which is a different (and non-standard) object, not the connection matrix of $\nabla$ in $e'$.

---

# Key Takeaways

**The connection matrix of a flat frame under a frame change is the pure "Maurer–Cartan" term $g^{-1}\,dg$, and this is the source of every pure-gauge potential in the theory.** When the base connection is the product connection $d$ and the base frame is parallel ($A = 0$), changing the frame by $g : U \to GL_k$ produces the connection matrix $g^{-1}\,dg$ with no other contribution. This one-form is the pullback by $g$ of the left Maurer–Cartan form of $GL_k$, and it recurs everywhere: it is the local connection form of a *pure-gauge* (flat) principal connection, the term added to $A$ by a gauge transformation, and — for $k = 1$, $g = e^f$ — the abelian shift $A \mapsto A + df$. The reusable recognition is: whenever you see $g^{-1}\,dg$ (or its additive rank-one shadow $df$), you are looking at the imprint of a *change of frame or gauge*, not at any intrinsic curvature; indeed $F = d(g^{-1}dg) + (g^{-1}dg)\wedge(g^{-1}dg) = 0$ identically (the Maurer–Cartan structure equation), so a pure-gauge potential is flat. The trigger for reaching for this term is any computation in which a trivial connection is re-expressed in a non-constant frame.

**Compute an invariant two ways whenever a general formula is available beside a first-principles route; the agreement is the check, and the collapse of terms is the lesson.** Here the direct computation and the transformation law (14) meet at $g^{-1}\,dg$, and the *reason* they meet — that the conjugation term $g^{-1}Ag$ dies because $A = 0$ — is more instructive than either computation alone. It isolates the two independent contributions to a connection matrix under a frame change: a *homogeneous* part $g^{-1}Ag$ that conjugates the existing matrix (a genuine tensorial transformation, the way curvature transforms), and an *inhomogeneous* part $g^{-1}\,dg$ that is created from nothing by the frame change itself. This split — tensorial conjugation plus an inhomogeneous cocycle term — is the defining signature of a connection (as opposed to a tensor), and it is exactly why the difference of two connections *is* a tensor while a single connection is not: subtracting two copies of (14) cancels the shared $g^{-1}\,dg$ and leaves only the conjugation. The diagnostic to carry: if a quantity transforms with an inhomogeneous $g^{-1}dg$ term it is a *potential*; if it transforms by pure conjugation $g^{-1}(\,\cdot\,)g$ it is a *field*.

**The matrix product rule $\nabla(eg) = (\nabla e)g + e\,dg$ is the columnwise Leibniz rule, and mismatching the frame is the characteristic error.** Almost all local connection computations reduce to this identity — deriving (14) itself, computing curvature in a rotated frame, propagating a connection through an operation on bundles. Its two pitfalls are placement (the derivative $dg$ multiplies the frame on the right, matching $e\,dg$, because $g$ acts on the frame from the right in $e' = eg$) and the final re-expression in the target frame (multiplying by $g^{-1}$ on the left to convert $e\,dg$ into $e'(g^{-1}dg)$). Getting a clean answer here — where $A = 0$ strips away the distracting conjugation term — builds exactly the reflex needed for the general case computed on [[Thm - Gauge Transformation Law for Connection 1-Forms|the frame-change theorem]] and reused for gauge transformations of the connection in [[Thm - Gauge Action on Connection Matrices|the gauge-action theorem]], where the same $g^{-1}dg$ term reappears as the inhomogeneous part of the gauge action $A^g = g^{-1}Ag + g^{-1}dg$.
