---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - Self-Dual Decomposition of 2-Forms in Four Dimensions"
  - "Thm - Spin Groups in Dimensions Three and Four via Quaternions"
  - "Thm - Spinor Representations of Spin(4) and the Self-Dual Forms"
  - "Def - Self-Dual and Anti-Self-Dual Forms"
  - "Def - Quaternions"
tags: [geometry, gauge-theory]
---

# Problem Statement

Andriy Haydys opens his construction of $Spin(4)$ (p. 35) with the standing identification
$$\mathfrak{so}(4)\;\cong\;\Lambda^2(\mathbb{R}^4)^*\;=\;\Lambda^2_+(\mathbb{R}^4)^*\oplus\Lambda^2_-(\mathbb{R}^4)^*\;\cong\;\mathfrak{so}(3)\oplus\mathfrak{so}(3),$$
which he uses without proof to produce the homomorphism $SO(4)\to SO(3)\times SO(3)$. This exercise establishes that chain of isomorphisms in full and identifies its pieces with the quaternionic double cover $\beta$.

Let $\mathbb{R}^n$ carry its standard Euclidean inner product $\langle\cdot,\cdot\rangle$ and oriented orthonormal basis $e_1,\dots,e_n$, let $\mathfrak{so}(n)=\{A\in\operatorname{End}(\mathbb{R}^n):A^{\mathsf T}=-A\}$ be the Lie algebra of $SO(n)$ (bracket the commutator $[A,B]=AB-BA$), and identify $\Lambda^2\mathbb{R}^n$ with $\Lambda^2(\mathbb{R}^n)^*$ through the metric so that $e_i\wedge e_j$ and $e_i^*\wedge e_j^*$ are interchangeable. Prove:

- **(a) The map $\Phi$ is an isomorphism of $SO(n)$-representations.** The assignment
$$\Phi:\mathfrak{so}(n)\longrightarrow\Lambda^2\mathbb{R}^n, \qquad \Phi(A)=\tfrac12\sum_{i,j=1}^{n}\langle Ae_i,e_j\rangle\,e_i\wedge e_j\qquad\Big(\text{equivalently }\Phi(A)=\sum_{i<j}\langle Ae_i,e_j\rangle\,e_i\wedge e_j\Big)$$
is a linear isomorphism, and it intertwines the adjoint action of $SO(n)$ on $\mathfrak{so}(n)$ (by $R\cdot A=RAR^{-1}$) with the action on two-forms (by $(R\cdot\omega)(x,y)=\omega(R^{-1}x,R^{-1}y)$). Equivalently, $\Phi(A)$ is the two-form $\omega_A(x,y)=\langle Ax,y\rangle$.

- **(b) In dimension four the two half-spaces $\Lambda^2_\pm$ are commuting Lie subalgebras, each $\cong\mathfrak{so}(3)\cong\operatorname{Im}\mathbb{H}$.** Transport the bracket of $\mathfrak{so}(4)$ to $\Lambda^2\mathbb{R}^4$ through $\Phi$. Under the quaternionic identification $\mathbb{R}^4=\mathbb{H}$, the subspace $\Phi^{-1}(\Lambda^2_+)$ consists of the left multiplications $L_h:x\mapsto hx$ by imaginary quaternions $h$, and $\Phi^{-1}(\Lambda^2_-)$ of the right multiplications $R_h:x\mapsto xh$. Show that each of these is a Lie subalgebra isomorphic to $\operatorname{Im}\mathbb{H}$ with its commutator bracket (hence to $\mathfrak{so}(3)$), and that the two commute: $[L_a,R_b]=0$.

- **(c) Conclude the splitting and match it to $d\beta$.** Deduce $\mathfrak{so}(4)\cong\mathfrak{so}(3)\oplus\mathfrak{so}(3)$ as Lie algebras, the two summands being $\Lambda^2_+$ and $\Lambda^2_-$; and show that the differential of the double cover $\beta(q_+,q_-)h=q_+h\bar q_-$ carries the first $\mathfrak{sp}(1)$ factor isomorphically onto $\Phi^{-1}(\Lambda^2_+)$ (by $x_+\mapsto L_{x_+}$) and the second onto $\Phi^{-1}(\Lambda^2_-)$ (by $x_-\mapsto -R_{x_-}$). This is the infinitesimal form of $Spin(4)=Sp(1)\times Sp(1)$ and the reason the composite $SO(4)\to SO(3)\times SO(3)$ is $\beta\mapsto(\alpha,\alpha)$.

**Recall:**

The objects in play are the Lie algebra $\mathfrak{so}(n)$, the exterior square $\Lambda^2\mathbb{R}^n$ with its metric, the Hodge star and the self-dual/anti-self-dual decomposition in dimension four, the imaginary quaternions, and the differential of $\beta$.

![[Def - Self-Dual and Anti-Self-Dual Forms#The Definition]]

![[Thm - Self-Dual Decomposition of 2-Forms in Four Dimensions#Statement]]

We use this theorem in the form: on oriented Euclidean $\mathbb{R}^4$ the Hodge star $\star$ satisfies $\star\star=\mathrm{id}$ on $\Lambda^2$, giving the orthogonal splitting $\Lambda^2\mathbb{R}^4=\Lambda^2_+\oplus\Lambda^2_-$ into the $\pm1$-eigenspaces of $\star$, each of dimension $3$, with orthogonal bases
$$\Lambda^2_+:\quad e^{12}+e^{34},\ \ e^{13}-e^{24},\ \ e^{14}+e^{23};\qquad\Lambda^2_-:\quad e^{12}-e^{34},\ \ e^{13}+e^{24},\ \ e^{14}-e^{23},$$
where $e^{ab}:=e_a\wedge e_b$.

![[Thm - Spin Groups in Dimensions Three and Four via Quaternions#Statement]]

From this theorem we import three facts, each proved there. First, the **product rule on imaginary quaternions** (its Lemma 3): for $a,b\in\operatorname{Im}\mathbb{H}$, $ab=-\langle a,b\rangle+a\times b$, so $a^2=-|a|^2$, and the commutator is $[a,b]=ab-ba=2\,a\times b$; the Lie algebra of $Sp(1)$ is $(\operatorname{Im}\mathbb{H},[\cdot,\cdot])$. Second, the **differential of $\beta$** (its Lemma 6): $d\beta(x_+,x_-)h=x_+h-hx_-$, a Lie-algebra isomorphism $\operatorname{Im}\mathbb{H}\oplus\operatorname{Im}\mathbb{H}\to\mathfrak{so}(4)$. Third, the **realisation of $\Lambda^2_\pm$ by one-sided multiplication** (its Lemma 7): the maps
$$\lambda_+:\operatorname{Im}\mathbb{H}\to\Lambda^2_+,\quad\lambda_+(h)(x,y)=\langle hx,y\rangle,\qquad\lambda_-:\operatorname{Im}\mathbb{H}\to\Lambda^2_-,\quad\lambda_-(h)(x,y)=\langle xh,y\rangle,$$
are linear isomorphisms, with $\lambda_+(i)=e^{12}+e^{34}$, $\lambda_+(j)=e^{13}-e^{24}$, $\lambda_+(k)=e^{14}+e^{23}$ and $\lambda_-(i)=e^{12}-e^{34}$, $\lambda_-(j)=e^{13}+e^{24}$, $\lambda_-(k)=e^{14}-e^{23}$. The homomorphism $\alpha:Sp(1)\to SO(3)$, $\alpha(q)h=qh\bar q$, has differential $d\alpha(x)h=[x,h]=2\,x\times h$, an isomorphism $\operatorname{Im}\mathbb{H}\to\mathfrak{so}(3)$.

> [!warning] Convention: Clifford sign and Hodge normalisation.
> The Hodge star is Bär's, $\omega\wedge\eta=\langle\star\omega,\eta\rangle\,\mathrm{vol}$; on two-forms in Euclidean dimension four this gives $\star\star=1$ and agrees with the alternative convention $\alpha\wedge\star\beta=\langle\alpha,\beta\rangle\,\mathrm{vol}$, so no sign ambiguity arises. We orient $\mathbb{R}^4=\mathbb{H}$ by $(1,i,j,k)$, matching the ambient theorem. The identification $\Lambda^2\mathbb{R}^n\cong\Lambda^2(\mathbb{R}^n)^*$ is via the metric throughout, so we write $e_i\wedge e_j$ where Haydys writes $e_i^*\wedge e_j^*$.

---

# Convergent Strategy

**Problem class.** This is a *build-and-identify-a-Lie-algebra-isomorphism* problem, of the kind that turns an abstract "$\mathfrak{g}\cong\mathfrak{g}_1\oplus\mathfrak{g}_2$" into an explicit dictionary. The work has three tiers: a purely linear-algebraic isomorphism $\mathfrak{so}(n)\cong\Lambda^2$ valid in all dimensions (part (a)); the special four-dimensional phenomenon that this exterior square carries a direct-sum Lie structure (part (b)); and the matching of that structure to a *known* product of groups, here $Sp(1)\times Sp(1)$, through the differential of the covering map (part (c)).

**Assumption pattern.** Part (a) rests on the single equivalence "skew endomorphism $\leftrightarrow$ alternating bilinear form", which is dimension-independent and is the reason $\dim\mathfrak{so}(n)=\dim\Lambda^2\mathbb{R}^n=\binom{n}{2}$. Part (b) rests on the *associativity of $\mathbb{H}$* — the only structural input needed for "$L$ and $R$ commute", $a(xb)=(ax)b$ — together with the reversal $R_aR_b=R_{ba}$ that flips one bracket's sign. Part (c) rests on the fact, imported from the ambient theorem, that $d\beta(x_+,x_-)=L_{x_+}-R_{x_-}$; once this is granted, matching the summands is bookkeeping.

**Theorem routing.** For (a): show $\Phi(A)$ is alternating (so lands in $\Lambda^2$) precisely because $A$ is skew; note $\Phi$ is linear and injective because the metric is nondegenerate; count $\binom{n}{2}=\binom{n}{2}$ for surjectivity; verify equivariance by a two-line computation with $R$ orthogonal. For (b): transport the bracket by *defining* $[\omega_A,\omega_B]:=\omega_{[A,B]}$, so $\Phi$ is a Lie isomorphism by fiat; route $\Lambda^2_\pm$ to $\{L_h\}$, $\{R_h\}$ via the imported [[Thm - Spin Groups in Dimensions Three and Four via Quaternions|isomorphisms λ₊, λ₋]]; compute $[L_a,L_b]=L_{[a,b]}$, $[R_a,R_b]=-R_{[a,b]}$, $[L_a,R_b]=0$ directly from associativity. For (c): $\{L_h\}\oplus\{R_h\}$ has dimension $6=\dim\mathfrak{so}(4)$ and the two are commuting ideals, so the sum is a direct sum of Lie algebras; read off $d\beta$'s action on each factor.

**Key decision point.** Two moves carry the exercise. First, *the choice to compute in the quaternionic model rather than with abstract eigenspaces of $\star$*: the self-dual and anti-self-dual forms are hard to bracket directly, but once identified (via $\lambda_\pm$) with left- and right-multiplications they bracket by pure algebra, because composition of one-sided multiplications is again one-sided multiplication. Second, *the recognition that right multiplication reverses order* — $R_aR_b=R_{ba}$, not $R_{ab}$ — which is why the anti-self-dual factor carries the *opposite* bracket and why $d\beta$'s second component appears with a minus sign, $x_-\mapsto -R_{x_-}$. Missing this reversal is the classic error; getting it right is what makes both factors genuinely $\mathfrak{so}(3)$ and the two commuting.

---

# Legal Operations Used

The solution uses the following operations of the chapter's Lie-algebra toolkit (named descriptively; to be cross-referenced to the topic page's numbered list once written):

1. **Encode a skew endomorphism as an alternating form via the metric.** The correspondence $A\mapsto\omega_A$, $\omega_A(x,y)=\langle Ax,y\rangle$, sends $\mathfrak{so}(n)$ to $\Lambda^2$; skewness of $A$ is exactly alternation of $\omega_A$.

2. **Promote an injective linear map between equidimensional spaces to an isomorphism.** With $\dim\mathfrak{so}(n)=\binom{n}{2}=\dim\Lambda^2\mathbb{R}^n$, injectivity of $\Phi$ gives bijectivity.

3. **Verify equivariance by conjugation-invariance of the metric.** Since $R\in SO(n)$ is orthogonal, $\langle RAR^{-1}x,y\rangle=\langle AR^{-1}x,R^{-1}y\rangle$, which is exactly the transformed form.

4. **Transport a Lie bracket along a linear isomorphism.** Define $[\omega_A,\omega_B]:=\omega_{[A,B]}$ so that $\Phi$ becomes a Lie-algebra isomorphism, then study subalgebras downstairs.

5. **Compute brackets of one-sided multiplications from associativity.** $L_aL_b=L_{ab}$ and $R_aR_b=R_{ba}$ (order reversed), while $L_aR_b=R_bL_a$; hence $[L_a,L_b]=L_{[a,b]}$, $[R_a,R_b]=-R_{[a,b]}$, $[L_a,R_b]=0$.

6. **Recognise a direct sum of Lie algebras from commuting complementary ideals.** Two subalgebras that commute, intersect trivially, and span the whole space exhibit it as their Lie-algebra direct sum.

7. **Read a group product off the differential of a covering.** From $d\beta(x_+,x_-)=L_{x_+}-R_{x_-}$, restrict to each factor to identify $d\beta$ of the two $\mathfrak{sp}(1)$ summands with $\Lambda^2_\pm$.

---

# Hints

> [!note]- Hint 1
> For part (a), the cleanest description of $\Phi$ is coordinate-free: $\Phi(A)$ is the two-form $\omega_A(x,y)=\langle Ax,y\rangle$. Check that $A^{\mathsf T}=-A$ is *equivalent* to $\omega_A(y,x)=-\omega_A(x,y)$. Then linearity and injectivity are immediate, and the dimensions of both sides are $\binom{n}{2}$.

> [!note]- Hint 2
> For the equivariance in (a), compute $\omega_{RAR^{-1}}(x,y)=\langle RAR^{-1}x,y\rangle$ and move $R^{-1}$ across the inner product using $R^{\mathsf T}=R^{-1}$. You should land on $\omega_A(R^{-1}x,R^{-1}y)$, which is the definition of $R\cdot\omega_A$.

> [!note]- Hint 3
> For part (b), do not bracket self-dual forms directly. Use the imported isomorphisms $\lambda_+(h)(x,y)=\langle hx,y\rangle$ and $\lambda_-(h)(x,y)=\langle xh,y\rangle$: these say $\Phi^{-1}(\lambda_+(h))=L_h$ (left multiplication) and $\Phi^{-1}(\lambda_-(h))=R_h$ (right multiplication). Now everything is a composition of multiplications.

> [!note]- Hint 4
> Compute $L_aL_b(x)=a(bx)=(ab)x=L_{ab}(x)$, so $[L_a,L_b]=L_{ab}-L_{ba}=L_{[a,b]}$. For right multiplications be careful: $R_aR_b(x)=R_a(xb)=(xb)a=x(ba)=R_{ba}(x)$ — the order *reverses*. And $L_aR_b(x)=a(xb)=(ax)b=R_bL_a(x)$ by associativity, so left and right multiplications commute.

> [!note]- Hint 5
> For part (c): $\{L_h\}$ and $\{R_h\}$ are $3$-dimensional, commute, and meet only in $0$ (if $ax=xb$ for all $x$, put $x=1$ to get $a=b$, then $a$ central, so $a=0$). Hence they span $\mathfrak{so}(4)$ and give a direct sum of ideals. Finally match with $d\beta(x_+,x_-)h=x_+h-hx_-=L_{x_+}(h)-R_{x_-}(h)$: the first factor lands in $\{L_h\}=\Phi^{-1}(\Lambda^2_+)$, the second in $\{R_h\}=\Phi^{-1}(\Lambda^2_-)$ with a sign.

---

# Solution

The exercise is the anatomy of the isomorphism $\mathfrak{so}(4)\cong\mathfrak{so}(3)\oplus\mathfrak{so}(3)$. In every dimension, skew endomorphisms *are* two-forms (part (a)); what is special about four dimensions is that the two-forms split, by the Hodge star, into two three-dimensional halves, and — read through the quaternions — those halves are the left- and right-multiplication algebras, which bracket among themselves and commute across (part (b)). Matching them to the two factors of $Sp(1)\times Sp(1)$ through $d\beta$ (part (c)) shows the splitting is nothing but the Lie-algebra shadow of the product group $Spin(4)=Sp(1)\times Sp(1)$.

**Step 1: $\Phi$ is a linear isomorphism $\mathfrak{so}(n)\to\Lambda^2\mathbb{R}^n$.**

The form $\omega_A(x,y)=\langle Ax,y\rangle$ is alternating exactly when $A$ is skew; the assignment $A\mapsto\omega_A$ is linear, injective, and (by equal dimensions) bijective, and it agrees with the displayed coordinate formula for $\Phi$.

> [!note]- Derivation
> Define $\omega_A(x,y):=\langle Ax,y\rangle$ for $A\in\operatorname{End}(\mathbb{R}^n)$; it is bilinear because the inner product is bilinear and $A$ linear.
>
> *Alternation is skewness (legal operation 1).* For all $x,y$,
> $$\omega_A(y,x)+\omega_A(x,y)=\langle Ay,x\rangle+\langle Ax,y\rangle=\langle y,A^{\mathsf T}x\rangle+\langle A x,y\rangle=\langle Ax+A^{\mathsf T}x,\ y\rangle\qquad(\text{definition of the transpose }A^{\mathsf T}).$$
> If $A^{\mathsf T}=-A$ this is $0$ for all $x,y$, so $\omega_A$ is alternating, i.e. $\omega_A\in\Lambda^2(\mathbb{R}^n)^*\cong\Lambda^2\mathbb{R}^n$. Conversely if $\omega_A$ is alternating the same line gives $\langle(A+A^{\mathsf T})x,y\rangle=0$ for all $y$, hence $(A+A^{\mathsf T})x=0$ for all $x$ (the metric is nondegenerate), i.e. $A^{\mathsf T}=-A$. So $A\mapsto\omega_A$ maps $\mathfrak{so}(n)$ *onto* the alternating forms and *only* skew $A$ produce alternating forms.
>
> *Agreement with the coordinate formula.* Expanding $\omega_A$ on the basis, $\omega_A=\sum_{i<j}\omega_A(e_i,e_j)\,e_i\wedge e_j=\sum_{i<j}\langle Ae_i,e_j\rangle\,e_i\wedge e_j$. Because $\langle Ae_j,e_i\rangle e_j\wedge e_i=(-\langle Ae_i,e_j\rangle)(-e_i\wedge e_j)=\langle Ae_i,e_j\rangle e_i\wedge e_j$ (using skewness of $A$ and antisymmetry of $\wedge$), the $(i,j)$ and $(j,i)$ terms of the full double sum coincide, so
> $$\tfrac12\sum_{i,j}\langle Ae_i,e_j\rangle\,e_i\wedge e_j=\sum_{i<j}\langle Ae_i,e_j\rangle\,e_i\wedge e_j=\omega_A,$$
> which is the displayed $\Phi(A)$; the factor $\tfrac12$ is exactly this double-counting. Thus $\Phi(A)=\omega_A$.
>
> *Linear isomorphism (legal operation 2).* $A\mapsto\omega_A$ is linear in $A$. It is injective: $\omega_A=0$ means $\langle Ax,y\rangle=0$ for all $x,y$, so $Ax=0$ for all $x$, so $A=0$. Both spaces have dimension $\binom{n}{2}$ — the skew $n\times n$ matrices have $\tfrac{n(n-1)}{2}$ free entries above the diagonal, and $\Lambda^2\mathbb{R}^n$ has basis $\{e_i\wedge e_j:i<j\}$ of the same cardinality. An injective linear map between spaces of equal finite dimension is bijective, so $\Phi$ is a linear isomorphism.
>
> *Unpacking in the smallest cases.* For $n=2$, $\mathfrak{so}(2)=\mathbb{R}\cdot A_0$ with $A_0=\bigl(\begin{smallmatrix}0&-1\\1&0\end{smallmatrix}\bigr)$, and $\Phi(A_0)=\langle A_0 e_1,e_2\rangle\,e_1\wedge e_2=e_1\wedge e_2$, matching $\dim=1$. For $n=3$, $\Phi$ composed with the metric identification $\Lambda^2\mathbb{R}^3\cong\mathbb{R}^3$ is the classical "axial vector" of an infinitesimal rotation: the generator of rotation about $e_3$ maps to $e_1\wedge e_2\leftrightarrow e_3$, recovering $\mathfrak{so}(3)\cong(\mathbb{R}^3,\times)$.

**Step 2: $\Phi$ intertwines the two $SO(n)$-actions.**

For $R\in SO(n)$ and $A\in\mathfrak{so}(n)$, $\Phi(RAR^{-1})=R\cdot\Phi(A)$; so $\Phi$ is an isomorphism of $SO(n)$-representations, completing part (a).

> [!note]- Derivation
> The adjoint action of $SO(n)$ on its Lie algebra is $R\cdot A=RAR^{-1}$ (conjugation), and the action on two-forms is $(R\cdot\omega)(x,y)=\omega(R^{-1}x,R^{-1}y)$ (pullback by $R^{-1}$). Compute, for $R\in SO(n)$ so that $R^{\mathsf T}=R^{-1}$ (legal operation 3):
> $$\Phi(RAR^{-1})(x,y)=\langle RAR^{-1}x,\ y\rangle=\langle AR^{-1}x,\ R^{-1}y\rangle\qquad(\text{move }R\text{ across }\langle\cdot,\cdot\rangle\text{ as }R^{\mathsf T}=R^{-1})$$
> $$=\omega_A(R^{-1}x,R^{-1}y)=\big(R\cdot\omega_A\big)(x,y)=\big(R\cdot\Phi(A)\big)(x,y).$$
> Hence $\Phi\circ\operatorname{Ad}_R=(R\cdot)\circ\Phi$ for every $R$; combined with Step 1, $\Phi$ is an isomorphism of $SO(n)$-representations. This proves **part (a)**.

**Step 3: In the quaternionic model, $\Lambda^2_+$ and $\Lambda^2_-$ are the left- and right-multiplication subspaces.**

Under $\Phi$ and the isomorphisms $\lambda_\pm$, $\Phi^{-1}(\Lambda^2_+)=\{L_h:h\in\operatorname{Im}\mathbb{H}\}$ and $\Phi^{-1}(\Lambda^2_-)=\{R_h:h\in\operatorname{Im}\mathbb{H}\}$.

> [!note]- Derivation
> Take $n=4$, $\mathbb{R}^4=\mathbb{H}$ with $(e_1,e_2,e_3,e_4)=(1,i,j,k)$. For imaginary $h$, left multiplication $L_h(x)=hx$ is a skew endomorphism: $\langle L_h x,y\rangle=\langle hx,y\rangle=\operatorname{Re}(\overline{hx}\,y)=\operatorname{Re}(\bar x\bar h y)=-\operatorname{Re}(\bar x h y)=-\langle x,hy\rangle=-\langle x,L_hy\rangle$ (using $\bar h=-h$). Hence $L_h\in\mathfrak{so}(4)$ and $\Phi(L_h)=\omega_{L_h}$, the two-form $(x,y)\mapsto\langle hx,y\rangle$. By the imported [[Thm - Spin Groups in Dimensions Three and Four via Quaternions|Lemma 7]] this two-form is $\lambda_+(h)$, which lies in $\Lambda^2_+$; and $\lambda_+:\operatorname{Im}\mathbb{H}\to\Lambda^2_+$ is an isomorphism onto the three-dimensional $\Lambda^2_+$. Therefore
> $$\Phi\big(\{L_h:h\in\operatorname{Im}\mathbb{H}\}\big)=\lambda_+(\operatorname{Im}\mathbb{H})=\Lambda^2_+,\qquad\text{i.e.}\qquad\Phi^{-1}(\Lambda^2_+)=\{L_h\}.$$
> Identically, right multiplication $R_h(x)=xh$ is skew ($\langle xh,y\rangle=\operatorname{Re}(\bar h\bar x y)=-\langle x,yh\rangle$ for imaginary $h$), $\Phi(R_h)=\lambda_-(h)\in\Lambda^2_-$, and $\lambda_-$ is an isomorphism onto $\Lambda^2_-$; hence $\Phi^{-1}(\Lambda^2_-)=\{R_h\}$. The two subspaces have dimension $3$ each.

**Step 4: $\{L_h\}$ and $\{R_h\}$ are commuting Lie subalgebras, each $\cong\mathfrak{so}(3)$.**

Composition of one-sided multiplications gives $[L_a,L_b]=L_{[a,b]}$ and $[R_a,R_b]=-R_{[a,b]}$, so both are subalgebras isomorphic to $\operatorname{Im}\mathbb{H}\cong\mathfrak{so}(3)$; and $[L_a,R_b]=0$, so they commute. This is **part (b)**.

> [!note]- Derivation
> We transport the bracket of $\mathfrak{so}(4)$ to $\Lambda^2\mathbb{R}^4$ through the isomorphism $\Phi$ (legal operation 4): by definition $[\omega_A,\omega_B]:=\omega_{[A,B]}$, so that $\Phi$ is a Lie-algebra isomorphism. All brackets below are commutators of endomorphisms of $\mathbb{H}$, computed with legal operation 5 from associativity of quaternion multiplication.
>
> *Left multiplications.* $L_aL_b(x)=a(bx)=(ab)x=L_{ab}(x)$, so $L_aL_b=L_{ab}$. Hence
> $$[L_a,L_b]=L_aL_b-L_bL_a=L_{ab}-L_{ba}=L_{ab-ba}=L_{[a,b]}.$$
> Thus $\{L_h:h\in\operatorname{Im}\mathbb{H}\}$ is closed under the bracket — a Lie subalgebra — and the linear isomorphism $h\mapsto L_h$ satisfies $L_{[a,b]}=[L_a,L_b]$, so it is a Lie-algebra isomorphism from $(\operatorname{Im}\mathbb{H},[\cdot,\cdot])=\mathfrak{sp}(1)$ onto $\{L_h\}$. Since $d\alpha:\operatorname{Im}\mathbb{H}\to\mathfrak{so}(3)$ is a Lie-algebra isomorphism ([[Thm - Spin Groups in Dimensions Three and Four via Quaternions|Lemma 5]]), $\{L_h\}\cong\operatorname{Im}\mathbb{H}\cong\mathfrak{so}(3)$.
>
> *Right multiplications, with the order reversal.* Here $R_aR_b(x)=R_a(xb)=(xb)a=x(ba)=R_{ba}(x)$, so $R_aR_b=R_{ba}$ — the order reverses. Hence
> $$[R_a,R_b]=R_aR_b-R_bR_a=R_{ba}-R_{ab}=R_{ba-ab}=R_{[b,a]}=-R_{[a,b]}.$$
> So $\{R_h\}$ is a subalgebra too, and the linear isomorphism $h\mapsto -R_h$ is a Lie-algebra isomorphism onto it: $[-R_a,-R_b]=[R_a,R_b]=-R_{[a,b]}=(-R)_{[a,b]}$, i.e. $(-R)$ intertwines the brackets. Therefore $\{R_h\}\cong\operatorname{Im}\mathbb{H}\cong\mathfrak{so}(3)$ as well. (Equivalently, $\{R_h\}$ is the *opposite* Lie algebra of $\{L_h\}$, and $\mathfrak{so}(3)$ is isomorphic to its opposite via negation.)
>
> *Commutation across the two.* By associativity, $L_aR_b(x)=a(xb)=(ax)b=R_bL_a(x)$, so $L_aR_b=R_bL_a$ for all $a,b$, whence
> $$[L_a,R_b]=L_aR_b-R_bL_a=0.$$
> Thus the two subalgebras commute elementwise. Transporting through $\Phi$ (an $SO(4)$-equivariant Lie isomorphism), the same holds for $\Lambda^2_+=\Phi(\{L_h\})$ and $\Lambda^2_-=\Phi(\{R_h\})$: each is a Lie subalgebra of $(\Lambda^2\mathbb{R}^4,[\cdot,\cdot])$ isomorphic to $\mathfrak{so}(3)$, and $[\Lambda^2_+,\Lambda^2_-]=0$. This is **part (b)**.

**Step 5: The splitting $\mathfrak{so}(4)\cong\mathfrak{so}(3)\oplus\mathfrak{so}(3)$ and its match with $d\beta$.**

The two commuting subalgebras meet only in $0$ and together span $\mathfrak{so}(4)$, so $\mathfrak{so}(4)=\Lambda^2_+\oplus\Lambda^2_-\cong\mathfrak{so}(3)\oplus\mathfrak{so}(3)$; and $d\beta$ maps the two $\mathfrak{sp}(1)$ factors onto $\{L_h\}$ and $\{R_h\}$. This is **part (c)**.

> [!note]- Derivation
> *Trivial intersection.* Suppose $L_a=R_b$ for some $a,b\in\operatorname{Im}\mathbb{H}$, i.e. $ax=xb$ for all $x\in\mathbb{H}$. Put $x=1$: $a=b$. Then $ax=xa$ for all $x$, so $a$ is central in $\mathbb{H}$; the centre of $\mathbb{H}$ is $\mathbb{R}$ (imposing commutation with $i$ and $j$, as in the ambient theorem's kernel computation), and $a\in\operatorname{Im}\mathbb{H}\cap\mathbb{R}=\{0\}$. Hence $\{L_h\}\cap\{R_h\}=\{0\}$.
>
> *Spanning and direct sum (legal operation 6).* Therefore $\dim\big(\{L_h\}+\{R_h\}\big)=\dim\{L_h\}+\dim\{R_h\}-\dim\big(\{L_h\}\cap\{R_h\}\big)=3+3-0=6=\dim\mathfrak{so}(4)$, so $\{L_h\}+\{R_h\}=\mathfrak{so}(4)$ and the sum is direct as vector spaces. Because $\{L_h\}$ and $\{R_h\}$ are subalgebras that commute (Step 4), each is an *ideal* of the sum ($[\{L_h\},\{L_h\}+\{R_h\}]=[\{L_h\},\{L_h\}]\subseteq\{L_h\}$), and a vector-space direct sum into two commuting ideals is a Lie-algebra direct sum. Applying $\Phi$,
> $$\mathfrak{so}(4)\ \cong\ \Lambda^2\mathbb{R}^4\ =\ \Lambda^2_+\oplus\Lambda^2_-\ \cong\ \mathfrak{so}(3)\oplus\mathfrak{so}(3),$$
> which is Haydys's standing identification, now with every isomorphism exhibited.
>
> *Match with $d\beta$ (legal operation 7).* By the imported [[Thm - Spin Groups in Dimensions Three and Four via Quaternions|Lemma 6]], the differential of $\beta(q_+,q_-)h=q_+h\bar q_-$ is
> $$d\beta(x_+,x_-)h=x_+h-hx_-=L_{x_+}(h)-R_{x_-}(h),\qquad\text{i.e.}\qquad d\beta(x_+,x_-)=L_{x_+}-R_{x_-}.$$
> Restricting to the first factor, $d\beta(x_+,0)=L_{x_+}$, so $d\beta$ carries $\mathfrak{sp}_+(1)=\operatorname{Im}\mathbb{H}\oplus 0$ isomorphically onto $\{L_h\}=\Phi^{-1}(\Lambda^2_+)$ by $x_+\mapsto L_{x_+}$. Restricting to the second, $d\beta(0,x_-)=-R_{x_-}$, so $d\beta$ carries $\mathfrak{sp}_-(1)=0\oplus\operatorname{Im}\mathbb{H}$ isomorphically onto $\{R_h\}=\Phi^{-1}(\Lambda^2_-)$ by $x_-\mapsto -R_{x_-}$; the minus sign is exactly the order reversal of Step 4, and indeed $x_-\mapsto -R_{x_-}$ is the Lie isomorphism found there. Because $d\beta$ is a Lie-algebra isomorphism onto $\mathfrak{so}(4)$ carrying the two commuting factors of $\mathfrak{sp}(1)\oplus\mathfrak{sp}(1)$ onto the two commuting ideals $\Lambda^2_\pm$, the splitting $\mathfrak{so}(4)=\mathfrak{so}(3)\oplus\mathfrak{so}(3)$ is precisely the infinitesimal form of the group product $Spin(4)=Sp_+(1)\times Sp_-(1)$. This proves **part (c)**. $\blacksquare$

> [!note]- Complete formal solution
> **Claim.** (a) $\Phi(A)=\omega_A$, $\omega_A(x,y)=\langle Ax,y\rangle$, is an isomorphism of $SO(n)$-representations $\mathfrak{so}(n)\to\Lambda^2\mathbb{R}^n$. (b) In dimension four, under $\mathbb{R}^4=\mathbb{H}$, $\Phi^{-1}(\Lambda^2_+)=\{L_h\}$ and $\Phi^{-1}(\Lambda^2_-)=\{R_h\}$ ($h\in\operatorname{Im}\mathbb{H}$) are commuting Lie subalgebras each $\cong\mathfrak{so}(3)$. (c) $\mathfrak{so}(4)=\Lambda^2_+\oplus\Lambda^2_-\cong\mathfrak{so}(3)\oplus\mathfrak{so}(3)$, and $d\beta(x_+,x_-)=L_{x_+}-R_{x_-}$ maps the two $\mathfrak{sp}(1)$ factors onto $\Phi^{-1}(\Lambda^2_\pm)$.
>
> (a) For $A\in\operatorname{End}(\mathbb{R}^n)$, $\omega_A(x,y)+\omega_A(y,x)=\langle(A+A^{\mathsf T})x,y\rangle$, so $\omega_A$ is alternating iff $A^{\mathsf T}=-A$; hence $A\mapsto\omega_A$ is a bijection $\mathfrak{so}(n)\to\Lambda^2(\mathbb{R}^n)^*$ (linear, injective since $\omega_A=0\Rightarrow A=0$, surjective by $\dim=\binom{n}{2}$ on both sides). Expanding on the basis gives $\omega_A=\sum_{i<j}\langle Ae_i,e_j\rangle e_i\wedge e_j=\tfrac12\sum_{i,j}\langle Ae_i,e_j\rangle e_i\wedge e_j=\Phi(A)$. For $R\in SO(n)$, $\omega_{RAR^{-1}}(x,y)=\langle RAR^{-1}x,y\rangle=\langle AR^{-1}x,R^{-1}y\rangle=\omega_A(R^{-1}x,R^{-1}y)=(R\cdot\omega_A)(x,y)$, so $\Phi$ is $SO(n)$-equivariant.
>
> (b) With $(e_1,e_2,e_3,e_4)=(1,i,j,k)$: for imaginary $h$, $L_h$ and $R_h$ are skew, and $\Phi(L_h)=\lambda_+(h)\in\Lambda^2_+$, $\Phi(R_h)=\lambda_-(h)\in\Lambda^2_-$, where $\lambda_\pm$ are the isomorphisms of the ambient theorem's Lemma 7; so $\Phi^{-1}(\Lambda^2_\pm)=\{L_h\},\{R_h\}$. Transport the bracket by $[\omega_A,\omega_B]:=\omega_{[A,B]}$. Then $L_aL_b=L_{ab}$ gives $[L_a,L_b]=L_{[a,b]}$; $R_aR_b=R_{ba}$ gives $[R_a,R_b]=-R_{[a,b]}$; $L_aR_b=R_bL_a$ gives $[L_a,R_b]=0$. Thus $\{L_h\}$ and $\{R_h\}$ are commuting subalgebras, each isomorphic to $(\operatorname{Im}\mathbb{H},[\cdot,\cdot])\cong\mathfrak{so}(3)$ via $h\mapsto L_h$, respectively $h\mapsto -R_h$.
>
> (c) If $L_a=R_b$ then (at $x=1$) $a=b$ and $a$ is central, so $a=0$; hence $\{L_h\}\cap\{R_h\}=0$ and, by dimension $3+3=6=\dim\mathfrak{so}(4)$, $\mathfrak{so}(4)=\{L_h\}\oplus\{R_h\}$, a direct sum of commuting ideals, so $\mathfrak{so}(4)\cong\mathfrak{so}(3)\oplus\mathfrak{so}(3)$ with summands $\Lambda^2_\pm$. Finally $d\beta(x_+,x_-)h=x_+h-hx_-=L_{x_+}(h)-R_{x_-}(h)$, so $d\beta(\cdot,0)=L_{(\cdot)}$ maps $\mathfrak{sp}_+(1)$ onto $\Phi^{-1}(\Lambda^2_+)$ and $d\beta(0,\cdot)=-R_{(\cdot)}$ maps $\mathfrak{sp}_-(1)$ onto $\Phi^{-1}(\Lambda^2_-)$. $\blacksquare$

> [!warning] Illegal but tempting alternative: forgetting that right multiplication reverses order.
> The seductive error is to write $R_aR_b=R_{ab}$ by analogy with $L_aL_b=L_{ab}$, which would give $[R_a,R_b]=R_{[a,b]}$ and make $h\mapsto R_h$ a genuine (not sign-flipped) isomorphism. It is wrong: $R_aR_b(x)=(xb)a=x(ba)=R_{ba}(x)$, because the *second* factor applied acts *further to the right*. The reversal is not cosmetic — it is why $d\beta$'s second component carries a minus sign ($x_-\mapsto -R_{x_-}$), why the anti-self-dual factor is the *opposite* algebra, and, one level up, why the two $Sp(1)$ factors of $Spin(4)$ act by $q_+$ on the *left* and $\bar q_-$ on the *right* of $h$. The condition under which "$R_aR_b=R_{ab}$" would be legal is commutativity of the algebra; $\mathbb{H}$ is precisely not commutative, and that non-commutativity is the whole source of the $\pm$ structure.

---

# Key Takeaways

**Skew endomorphisms are two-forms in every dimension; what makes dimension four special is that the two-forms then split.** The isomorphism $\mathfrak{so}(n)\cong\Lambda^2\mathbb{R}^n$, $A\mapsto\langle A\cdot,\cdot\rangle$, is elementary and universal — it is why $\dim\mathfrak{so}(n)=\binom{n}{2}$ and why the curvature of a metric connection, an $\mathfrak{so}(n)$-valued object, is naturally a two-form. The four-dimensional miracle is layered on top: only when $n=4$ does the middle exterior power $\Lambda^2$ sit in the *self-dual* degree $k=n-k=2$, so the Hodge star acts on it as an involution and cuts it into two equal halves. The reusable principle: whenever you see an $\mathfrak{so}(4)$-valued or $\Lambda^2$-valued quantity on a four-manifold — curvature, the Weyl tensor, the intersection form's harmonic representatives — expect it to decompose into a self-dual and an anti-self-dual part transforming under *separate* $\mathfrak{so}(3)$'s, and expect that decomposition to be $SO(4)$-invariant because $\Phi$ is equivariant and $\star$ commutes with the $SO(4)$-action. The trigger is "$\Lambda^2$ in dimension four"; the reaction is "split by $\star$".

**Brackets of the abstract eigenspaces of $\star$ are computed by moving to a concrete model in which composition is transparent — here, the quaternions.** Directly bracketing "$e^{12}+e^{34}$ with $e^{13}-e^{24}$" as endomorphisms is possible but opaque; recognising these as *left multiplications by imaginary quaternions* turns every bracket into a one-line associativity computation, because a composite of left multiplications is again a left multiplication. This is a general research reflex: an abstract Lie subalgebra becomes tractable once realised as an algebra of operators with a closed multiplication law. The specific dictionary — $\Lambda^2_+\leftrightarrow$ left multiplication, $\Lambda^2_-\leftrightarrow$ right multiplication — is worth memorising, because it is the linear-algebraic engine behind the entire self-dual/anti-self-dual formalism: the two factors of $Spin(4)=Sp(1)\times Sp(1)$ act by left and by right quaternion multiplication, so they *automatically* commute (associativity) and *automatically* preserve the two halves of $\Lambda^2$. When a later computation needs "self-dual two-forms act on positive spinors, anti-self-dual ones annihilate them" ([[Thm - Spinor Representations of Spin(4) and the Self-Dual Forms]]), it is this same left/right split, pushed through Clifford multiplication.

**A splitting of a Lie algebra into two commuting ideals is the infinitesimal fingerprint of a product group, and $d\beta$ makes the fingerprint explicit.** The chain $\mathfrak{so}(4)=\Lambda^2_+\oplus\Lambda^2_-\cong\mathfrak{so}(3)\oplus\mathfrak{so}(3)$ is not merely a vector-space decomposition: because the two summands *commute*, it is a Lie-algebra direct sum, and a Lie-algebra direct sum $\mathfrak{g}_1\oplus\mathfrak{g}_2$ integrates (for the simply connected cover) to a product group $G_1\times G_2$. The differential of $\beta$ exhibits this: it sends the two $\mathfrak{sp}(1)$ factors, by $x_+\mapsto L_{x_+}$ and $x_-\mapsto -R_{x_-}$, onto the two ideals, so the abstract statement "$\mathfrak{so}(4)$ is not simple" is realised by the concrete statement "$Spin(4)=Sp(1)\times Sp(1)$". The transferable diagnostic: if you find a Lie algebra breaking into commuting ideals, look for the corresponding product structure on the group — and conversely, the failure of $\mathfrak{so}(n)$ to split for $n\ne 4$ (it is simple for $n=3$ and $n\ge5$) is exactly why $SO(4)$ alone among the rotation groups has a two-factor cover, and why four-dimensional gauge theory has its distinctive $\pm$ dichotomy. This exercise pairs naturally with [[Ex - The Kernel of the Double Cover of SO(4)]], which computes the differential $d\beta$ and the kernel that this splitting takes as its starting point.
