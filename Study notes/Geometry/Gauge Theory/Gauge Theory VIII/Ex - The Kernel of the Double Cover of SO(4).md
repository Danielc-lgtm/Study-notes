---
type: exercise
subject: gauge-theory
difficulty: "⭐⭐"
prereqs:
  - "Thm - Spin Groups in Dimensions Three and Four via Quaternions"
  - "Def - Quaternions"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $\mathbb{H}$ be the quaternions with the Euclidean inner product $\langle x,y\rangle=\operatorname{Re}(\bar x\,y)$ making $(1,i,j,k)$ an oriented orthonormal basis, and let $Sp(1)=\{q\in\mathbb{H}:|q|=1\}$ be the group of unit quaternions. Consider the map
$$\beta:Sp_+(1)\times Sp_-(1)\longrightarrow SO(4), \qquad \beta(q_+,q_-)h:=q_+\,h\,\bar q_- \quad (h\in\mathbb{H}\cong\mathbb{R}^4),$$
which the theorem [[Thm - Spin Groups in Dimensions Three and Four via Quaternions|Spin Groups in Dimensions Three and Four via Quaternions]] establishes to be a well-defined homomorphism of Lie groups landing in $SO(4)$. Andriy Haydys, having introduced $\beta$, disposes of the two facts that make it a double cover in a single clause each: the kernel is "readily checked" to be $\{\pm(1,1)\}$, and surjectivity is left to "an explicit computation" and the connectedness of $SO(4)$. This exercise is the drill that carries out both.

Prove, working directly from the quaternion arithmetic:

- **(a) The kernel.** The condition $q_+\,h\,\bar q_-=h$ for *all* $h\in\mathbb{H}$ forces $q_+=q_-$ and then $q_+\in\{+1,-1\}$; hence
$$\ker\beta=\{(1,1),(-1,-1)\}=\{\pm(1,1)\}\cong\mathbb{Z}/2\mathbb{Z}.$$
The route is exactly the one the phrase "readily checked" compresses: **evaluate the kernel condition at $h=1$** to pin down $q_+=q_-$, then **let $h$ range over the imaginary units** to force $q_+$ into the centre of $\mathbb{H}$.

- **(b) Surjectivity.** By computing the differential
$$d\beta(x_+,x_-)h=x_+\,h-h\,x_-\qquad\big((x_+,x_-)\in\operatorname{Im}\mathbb{H}\oplus\operatorname{Im}\mathbb{H},\ h\in\mathbb{H}\big),$$
show that $d\beta$ is a linear isomorphism $\operatorname{Im}\mathbb{H}\oplus\operatorname{Im}\mathbb{H}\to\mathfrak{so}(4)$; deduce that $\beta$ is a local diffeomorphism at $(1,1)$, so that its image is an open subgroup of $SO(4)$, and conclude from the connectedness of $SO(4)$ that $\beta$ is surjective.

Together with the fact that $\beta$ is a homomorphism into $SO(4)$, parts (a) and (b) say that $\beta$ is a two-sheeted covering homomorphism, so that $Sp(1)\times Sp(1)$ is a double cover of $SO(4)$; matched with the abstract spin group this is the isomorphism $Spin(4)\cong Sp(1)\times Sp(1)$.

**Recall:**

The objects in play are the quaternions and their inner product, the group $Sp(1)$ of unit quaternions, the special orthogonal group $SO(4)$ and its Lie algebra $\mathfrak{so}(4)$, and the covering map $\beta$.

![[Def - Quaternions#The Definition]]

The **conjugate** of $q=a+bi+cj+dk$ (with $a,b,c,d\in\mathbb{R}$) is $\bar q=a-bi-cj-dk$; conjugation reverses order, $\overline{q_1q_2}=\bar q_2\,\bar q_1$, and the **norm** $|q|^2=q\bar q=\bar q q=a^2+b^2+c^2+d^2$ is multiplicative, $|q_1q_2|=|q_1|\,|q_2|$. The **real part** is $\operatorname{Re}(a+bi+cj+dk)=a$, and $\langle x,y\rangle=\operatorname{Re}(\bar x\,y)$ is the standard Euclidean inner product on $\mathbb{H}=\mathbb{R}^4$; the **imaginary quaternions** $\operatorname{Im}\mathbb{H}=\{h:\bar h=-h\}=\operatorname{span}_\mathbb{R}\{i,j,k\}$ form the orthogonal complement of $\mathbb{R}\cdot 1$. For a unit quaternion, $\bar q=q^{-1}$.

![[Thm - Spin Groups in Dimensions Three and Four via Quaternions#Statement]]

The single input we borrow from that theorem is its **Part (ii) up to the kernel and surjectivity claims**: that $\beta(q_+,q_-):h\mapsto q_+h\bar q_-$ is a well-defined smooth group homomorphism whose image lies in $SO(4)$ (each $\beta(q_+,q_-)$ preserves $|h|$ because the norm is multiplicative and $|q_\pm|=1$, and lands in the *special* orthogonal group by a connectedness-of-the-determinant argument). We also use two structural facts proved on that page: $Sp(1)$ is a compact **connected** Lie group with Lie algebra $\operatorname{Im}\mathbb{H}$ and Lie bracket the commutator $[x,y]=xy-yx$ (its Lemma 3), and $SO(4)$ is **path-connected** (its Lemma 4). Everything else — the two computations the source omits — we prove here from scratch.

> [!warning] Convention: Clifford sign and Hodge normalisation.
> This page uses only the quaternionic model of $\beta$ and never the Clifford algebra directly, so the series' Clifford sign $u\cdot u=-|u|^2$ enters only through the ambient theorem. We orient $\mathbb{R}^4=\mathbb{H}$ by declaring $(1,i,j,k)$ positive, matching the ambient theorem; the source (Haydys, p. 35) has no typographical error in this passage, and the two clauses we expand are genuine omissions, not misprints.

---

# Convergent Strategy

**Problem class.** This is a *compute-a-kernel-and-prove-a-surjection* problem: the archetype of showing that an explicitly given homomorphism between Lie groups is a covering map. The template has three independent pieces — homomorphism (given), kernel (part (a)), surjectivity (part (b)) — and the two we must supply illustrate the two standard techniques of the class: a kernel is found by *algebra* (pin the offending elements down to the centre), and a surjection of Lie groups is found by *topology* (a local diffeomorphism has open image, and an open subgroup of a connected group is everything).

**Assumption pattern.** Part (a) uses one recognisable trigger: a condition quantified over *all* $h$ ("$q_+h\bar q_-=h$ for every $h$") is far too strong to attack head-on, so one *specialises the free variable* — first to the multiplicative identity $h=1$, which decouples $q_+$ from $q_-$, then to the imaginary units $h=i,j$, which is exactly enough to force commutation with all of $\mathbb{H}$. Part (b) uses the trigger that the two groups have equal dimension ($\dim Sp(1)^2=3+3=6=\binom{4}{2}=\dim SO(4)$): once the differential is injective it is automatically an isomorphism, and the inverse function theorem converts an infinitesimal isomorphism into a local one.

**Theorem routing.** For (a): impose the kernel condition; **route through $h=1$** to get $q_+\bar q_-=1$, i.e. $q_+=q_-$ (using $\bar q_-^{-1}=q_-$ for unit $q_-$); the condition collapses to $q_+h=hq_+$ for all $h$; **route through the centre of $\mathbb{H}$** — commuting with $i$ and with $j$ forces $q_+$ real — to get $q_+\in\mathbb{R}\cap Sp(1)=\{\pm1\}$. For (b): differentiate $t\mapsto\beta(\exp(tx_+),\exp(tx_-))$ at $t=0$ to obtain $d\beta(x_+,x_-)h=x_+h-hx_-$; show injectivity by the *same* $h=1$-then-centre argument as in (a); dimension count promotes injectivity to bijectivity; then invoke the [[Thm - Spin Groups in Dimensions Three and Four via Quaternions|inverse function theorem step and the connectedness of SO(4)]] to pass from local surjectivity to global surjectivity.

**Key decision point.** The one genuinely non-obvious move is the *reuse of the kernel argument inside the differential computation*: the injectivity of $d\beta$ is not a new fact but the *linearised shadow* of the kernel computation — "$q_+h=hq_+$ for all $h$ forces $q_+$ real" becomes "$x_+h=hx_+$ for all $h$ forces $x_+=0$", because the only real imaginary quaternion is $0$. Recognising that the same centre-of-$\mathbb{H}$ computation drives both parts is what makes the exercise a single idea rather than two. The second decision is choosing *topology over an inverse map for surjectivity*: one cannot write down $\beta^{-1}$, but one never needs to — openness of the image plus connectedness of the target does the whole job.

---

# Legal Operations Used

This solution deploys the following legal operations, drawn from the Lie-groups and spin-groups toolkit of the chapter (numbered as on the topic page's Legal Operations once it is written; here named descriptively):

1. **Specialise a universally quantified identity at a distinguished element.** The kernel condition holds for *all* $h$; evaluating it at the unit $h=1$ turns the coupled equation $q_+h\bar q_-=h$ into the algebraic relation $q_+\bar q_-=1$.

2. **Reduce commutation-with-everything to commutation with a spanning set.** To show $q_+$ is central it is enough to impose $q_+h=hq_+$ for $h=i$ and $h=j$, because $\{1,i,j,k\}$ spans $\mathbb{H}$ and $q_+$ commutes with $1$ automatically.

3. **Compute the centre of $\mathbb{H}$.** A quaternion commuting with all of $\mathbb{H}$ is real; a *unit* real quaternion is $\pm1$. This identifies the kernel and, in linearised form, the injectivity of the differential.

4. **Differentiate a group homomorphism along one-parameter subgroups.** Feed the curves $\exp(tx_\pm)$ through $\beta$ and differentiate at $t=0$ with the product rule, using $\tfrac{d}{dt}\big|_0\overline{\exp(tx_-)}=\overline{x_-}=-x_-$, to obtain $d\beta$.

5. **Promote an injective linear map between equidimensional spaces to an isomorphism.** Since $\dim(\operatorname{Im}\mathbb{H}\oplus\operatorname{Im}\mathbb{H})=6=\dim\mathfrak{so}(4)$, an injective $d\beta$ is surjective, hence bijective.

6. **Convert an infinitesimal isomorphism into a local diffeomorphism.** The inverse function theorem, applied where $d\beta$ is invertible, makes $\beta$ carry a neighbourhood of $(1,1)$ onto a neighbourhood of $I\in SO(4)$; the image therefore contains an open set.

7. **An open subgroup of a connected group is the whole group.** The image of $\beta$ is a subgroup containing an open neighbourhood of $I$; such a subgroup is open and closed, and $SO(4)$ is connected, so the image is all of $SO(4)$.

---

# Hints

> [!note]- Hint 1
> For part (a) do not try to solve $q_+h\bar q_-=h$ for general $h$ at once. The variable $h$ is free — you may plug in *any* quaternion you like. Which single value of $h$ removes the coupling between $q_+$ and $q_-$ entirely?

> [!note]- Hint 2
> Setting $h=1$ gives $q_+\bar q_-=1$. Because $|q_-|=1$ means $\bar q_-q_-=1$, this reads $q_+=q_-$. Now the kernel condition becomes $q_+h\bar q_+=h$, i.e. (multiply on the right by $q_+$ and use $\bar q_+q_+=1$) $q_+h=hq_+$ for *all* $h$. What are the quaternions that commute with everything?

> [!note]- Hint 3
> Write $q_+=a+bi+cj+dk$ and impose $q_+i=iq_+$ and $q_+j=jq_+$. The first kills the $j$- and $k$-components, the second kills the $i$-component; only the real part survives. A real unit quaternion is $\pm1$. That is part (a).

> [!note]- Hint 4
> For part (b), the differential of $t\mapsto\exp(tx_+)\,h\,\overline{\exp(tx_-)}$ at $t=0$ is a product-rule computation; remember that $\overline{\exp(tx_-)}=\exp(t\bar x_-)=\exp(-tx_-)$ for imaginary $x_-$, so its $t$-derivative at $0$ is $-x_-$. You should get $d\beta(x_+,x_-)h=x_+h-hx_-$.

> [!note]- Hint 5
> To see $d\beta$ is injective, set $d\beta(x_+,x_-)=0$, i.e. $x_+h=hx_-$ for all $h$; the *same* two specialisations as in part (a) ($h=1$, then $h$ imaginary) force $x_+=x_-=0$. Count dimensions ($6=6$) to get an isomorphism. Then the inverse function theorem gives an open image, and connectedness of $SO(4)$ finishes it — an open subgroup of a connected group is everything.

---

# Solution

The two computations are the algebraic and the topological halves of "$\beta$ is a double cover", and they share one engine: the centre of $\mathbb{H}$ is $\mathbb{R}$. In part (a) this appears as "$q_+$ commutes with all of $\mathbb{H}$, hence is real, hence $\pm1$"; in part (b) it reappears, linearised, as "$x_+$ commutes with all of $\mathbb{H}$, hence is real and imaginary, hence $0$", which is precisely the injectivity of the differential. Once $d\beta$ is an isomorphism, no formula for an inverse is needed: the inverse function theorem opens the image and the connectedness of $SO(4)$ fills it.

**Step 1: Evaluate the kernel condition at $h=1$ to force $q_+=q_-$.**

Let $(q_+,q_-)\in\ker\beta$, so that $q_+h\bar q_-=h$ for every $h\in\mathbb{H}$. Putting $h=1$ gives $q_+=q_-$.

> [!note]- Derivation
> By definition of the kernel, $\beta(q_+,q_-)=\mathrm{id}_{\mathbb{H}}$ means
> $$q_+\,h\,\bar q_-=h\qquad\text{for all }h\in\mathbb{H}.$$
> Specialise to $h=1$ (legal operation 1). Since $1$ is the multiplicative identity, the left side is $q_+\cdot 1\cdot\bar q_-=q_+\bar q_-$, so
> $$q_+\bar q_-=1.$$
> Now $q_-\in Sp(1)$ means $|q_-|=1$, i.e. $\bar q_-q_-=|q_-|^2=1$ (definition of the quaternion norm). Multiplying $q_+\bar q_-=1$ on the right by $q_-$ gives $q_+\bar q_-q_-=q_-$, that is
> $$q_+=q_-.$$
> The two unit quaternions are equal; write $q:=q_+=q_-$ from here on.

**Step 2: Reduce to commutation and compute the centre of $\mathbb{H}$.**

With $q_+=q_-=q$, the kernel condition becomes $qh=hq$ for all $h$; commuting with $i$ and $j$ forces $q\in\mathbb{R}$, hence $q=\pm1$.

> [!note]- Derivation
> Substituting $q_+=q_-=q$ into $q_+h\bar q_-=h$ gives $qh\bar q=h$ for all $h$. Multiply on the right by $q$ and use $\bar q q=|q|^2=1$:
> $$qh\bar q q=hq\quad\Longrightarrow\quad qh=hq\qquad\text{for all }h\in\mathbb{H}.$$
> So $q$ commutes with every quaternion. It commutes with $1$ automatically, so by legal operation 2 it suffices to impose commutation with $i$ and with $j$. Write $q=a+bi+cj+dk$ with $a,b,c,d\in\mathbb{R}$.
>
> *Commute with $i$.* Using $i^2=-1$, $ji=-k$, $ki=j$ on the left and $ij=k$, $ik=-j$ on the right,
> $$qi=ai-b+c(ji)+d(ki)=-b+ai-ck+dj,\qquad iq=ai-b+c(ij)+d(ik)=-b+ai+ck-dj.$$
> Equating $qi=iq$ and comparing the $j$- and $k$-components gives $dj-ck=-dj+ck$, hence $c=0$ and $d=0$.
>
> *Commute with $j$.* Now $q=a+bi$; using $ij=k$ and $ji=-k$,
> $$qj=aj+b(ij)=aj+bk,\qquad jq=aj+b(ji)=aj-bk.$$
> Equating $qj=jq$ gives $bk=-bk$, hence $b=0$.
>
> Therefore $q=a\in\mathbb{R}$: the centre of $\mathbb{H}$ is $\mathbb{R}$ (legal operation 3). Finally $q\in Sp(1)$ forces $a^2=|q|^2=1$, so $q=\pm1$. Conversely $\beta(1,1)=\mathrm{id}$ and $\beta(-1,-1):h\mapsto(-1)h(-1)=h$ is also the identity (the two signs cancel), so both $(1,1)$ and $(-1,-1)$ lie in the kernel. Hence
> $$\ker\beta=\{(1,1),(-1,-1)\}=\{\pm(1,1)\}.$$
> As a group of order two this is $\mathbb{Z}/2\mathbb{Z}$. This proves part (a).

**Step 3: Compute the differential $d\beta$.**

Differentiating $\beta$ along one-parameter subgroups gives $d\beta(x_+,x_-)h=x_+h-hx_-$.

> [!note]- Derivation
> Fix $(x_+,x_-)\in\operatorname{Im}\mathbb{H}\oplus\operatorname{Im}\mathbb{H}=T_{(1,1)}\big(Sp(1)\times Sp(1)\big)$; here we use that the Lie algebra of $Sp(1)$ is $\operatorname{Im}\mathbb{H}$ (Lemma 3 of the ambient theorem). Take the curve $t\mapsto\big(\exp(tx_+),\exp(tx_-)\big)$ in $Sp(1)\times Sp(1)$, which passes through $(1,1)$ at $t=0$ with velocity $(x_+,x_-)$. Apply $\beta$ and differentiate at $t=0$ (legal operation 4). For $h\in\mathbb{H}$,
> $$\beta\big(\exp(tx_+),\exp(tx_-)\big)h=\exp(tx_+)\,h\,\overline{\exp(tx_-)}.$$
> Because $x_-$ is imaginary, $\overline{\exp(tx_-)}=\exp(t\bar x_-)=\exp(-tx_-)$ (conjugation is a continuous algebra anti-automorphism, and $\bar x_-=-x_-$), so the two factors have $t$-derivatives at $t=0$
> $$\frac{d}{dt}\Big|_{0}\exp(tx_+)=x_+,\qquad\frac{d}{dt}\Big|_{0}\overline{\exp(tx_-)}=\frac{d}{dt}\Big|_{0}\exp(-tx_-)=-x_-.$$
> By the product rule in the associative algebra $\mathbb{H}$ (multiplication is bilinear, hence smooth, with the Leibniz rule),
> $$d\beta(x_+,x_-)h=x_+\cdot h\cdot 1+1\cdot h\cdot(-x_-)=x_+h-hx_-.$$
> Since $\beta$ maps into $SO(4)$ (ambient theorem), its differential maps $T_{(1,1)}(Sp(1)^2)$ into $T_I SO(4)=\mathfrak{so}(4)$; we record this directly as a check. For every $h\in\mathbb{H}$,
> $$\langle d\beta(x_+,x_-)h,\ h\rangle=\operatorname{Re}\big(\bar h(x_+h-hx_-)\big)=\operatorname{Re}(\bar h x_+ h)-\operatorname{Re}(\bar h h x_-)=|h|^2\operatorname{Re}(x_+)-|h|^2\operatorname{Re}(x_-)=0,$$
> using the cyclicity $\operatorname{Re}(uv)=\operatorname{Re}(vu)$ (so $\operatorname{Re}(\bar h x_+h)=\operatorname{Re}(x_+h\bar h)=|h|^2\operatorname{Re}(x_+)$), $\bar h h=|h|^2$, and $\operatorname{Re}(x_\pm)=0$ (the $x_\pm$ are imaginary). A real-linear map $A:\mathbb{R}^4\to\mathbb{R}^4$ with $\langle Ah,h\rangle=0$ for all $h$ is skew-symmetric (polarise: $0=\langle A(h+h'),h+h'\rangle=\langle Ah,h'\rangle+\langle Ah',h\rangle$). Hence $d\beta(x_+,x_-)\in\mathfrak{so}(4)$, confirming the codomain.

**Step 4: $d\beta$ is injective, hence an isomorphism.**

The linearised centre computation shows $\ker d\beta=0$, and equality of dimensions upgrades this to a linear isomorphism $\operatorname{Im}\mathbb{H}\oplus\operatorname{Im}\mathbb{H}\xrightarrow{\ \cong\ }\mathfrak{so}(4)$.

> [!note]- Derivation
> Suppose $d\beta(x_+,x_-)=0$, i.e.
> $$x_+h-hx_-=0,\qquad\text{that is}\qquad x_+h=hx_-\quad\text{for all }h\in\mathbb{H}.$$
> This is the infinitesimal twin of the kernel condition, and we solve it the same way. Setting $h=1$ (legal operation 1) gives $x_+=x_-$. The equation then reads $x_+h=hx_+$ for all $h$, so $x_+$ is central; by Step 2 (the centre of $\mathbb{H}$ is $\mathbb{R}$, legal operation 3) $x_+\in\mathbb{R}$. But $x_+\in\operatorname{Im}\mathbb{H}$, and $\mathbb{R}\cap\operatorname{Im}\mathbb{H}=\{0\}$, so $x_+=0$, and hence $x_-=x_+=0$. Therefore $\ker d\beta=\{0\}$ and $d\beta$ is injective.
>
> Now count dimensions (legal operation 5): $\dim(\operatorname{Im}\mathbb{H}\oplus\operatorname{Im}\mathbb{H})=3+3=6$, while $\dim\mathfrak{so}(4)=\binom{4}{2}=6$ (the skew-symmetric $4\times4$ matrices have $\tfrac{4\cdot3}{2}$ independent entries). An injective linear map between vector spaces of equal finite dimension is bijective. Hence
> $$d\beta:\operatorname{Im}\mathbb{H}\oplus\operatorname{Im}\mathbb{H}\xrightarrow{\ \cong\ }\mathfrak{so}(4).$$

**Step 5: Local surjectivity via the inverse function theorem, then global surjectivity via connectedness.**

Since $d\beta$ is invertible at $(1,1)$, the image of $\beta$ is an open subgroup of $SO(4)$; as $SO(4)$ is connected, the image is all of $SO(4)$.

> [!note]- Derivation
> By Step 4, $d\beta$ is a linear isomorphism at the point $(1,1)$. The **inverse function theorem** (legal operation 6) applies to the smooth map $\beta:Sp(1)\times Sp(1)\to SO(4)$ between manifolds of the same dimension $6$: $\beta$ restricts to a diffeomorphism from an open neighbourhood of $(1,1)$ onto an open neighbourhood $U$ of $\beta(1,1)=I$ in $SO(4)$. In particular the image $G:=\operatorname{im}\beta$ contains the open set $U\ni I$.
>
> Now $G$ is a *subgroup* of $SO(4)$ (the image of a group homomorphism). We invoke the standard fact (legal operation 7): **an open subgroup of a topological group is also closed, and an open-and-closed nonempty subset of a connected group is the whole group.** For completeness, here is the argument. Because $I\in U\subseteq G$ and $G$ is closed under the group operations, for every $g\in G$ the translate $gU\subseteq G$ is an open neighbourhood of $g$; hence $G=\bigcup_{g\in G}gU$ is open. Its complement is a union of cosets $SO(4)\setminus G=\bigcup_{g\notin G}gU$ (each coset $gU$ of a point $g\notin G$ misses $G$, since $gu\in G$ would give $g=(gu)u^{-1}\in G$), so the complement is open too; thus $G$ is also closed. By Lemma 4 of the ambient theorem, [[Thm - Spin Groups in Dimensions Three and Four via Quaternions|SO(4) is path-connected]], in particular connected, so it has no proper nonempty subset that is both open and closed. Since $G\ni I$ is nonempty, open, and closed, $G=SO(4)$. Therefore $\beta$ is surjective. This proves part (b). $\blacksquare$

> [!note]- Complete formal solution
> **Claim.** For $\beta:Sp_+(1)\times Sp_-(1)\to SO(4)$, $\beta(q_+,q_-)h=q_+h\bar q_-$, one has $\ker\beta=\{\pm(1,1)\}$ and $\beta$ is surjective.
>
> *Kernel.* Let $(q_+,q_-)\in\ker\beta$, so $q_+h\bar q_-=h$ for all $h\in\mathbb{H}$. At $h=1$: $q_+\bar q_-=1$, and multiplying on the right by $q_-$ (with $\bar q_-q_-=|q_-|^2=1$) gives $q_+=q_-=:q$. The condition becomes $qh\bar q=h$, i.e. $qh=hq$ for all $h$ (multiply on the right by $q$, using $\bar q q=1$). Writing $q=a+bi+cj+dk$: imposing $qi=iq$ yields $c=d=0$, and then $qj=jq$ yields $b=0$, so $q=a\in\mathbb{R}$; the unit condition forces $q=\pm1$. Conversely $\beta(\pm1,\pm1)=\mathrm{id}$ for equal signs. Hence $\ker\beta=\{(1,1),(-1,-1)\}\cong\mathbb{Z}/2\mathbb{Z}$.
>
> *Surjectivity.* Differentiating $\beta(\exp(tx_+),\exp(tx_-))h=\exp(tx_+)h\exp(-tx_-)$ at $t=0$ (using $\overline{\exp(tx_-)}=\exp(-tx_-)$ for imaginary $x_-$) gives $d\beta(x_+,x_-)h=x_+h-hx_-$, a map into $\mathfrak{so}(4)$ (since $\langle x_+h-hx_-,h\rangle=|h|^2(\operatorname{Re}x_+-\operatorname{Re}x_-)=0$). If $d\beta(x_+,x_-)=0$ then $x_+h=hx_-$ for all $h$; at $h=1$, $x_+=x_-$, and then $x_+$ is central, so $x_+\in\mathbb{R}\cap\operatorname{Im}\mathbb{H}=\{0\}$; thus $d\beta$ is injective, and being a map between $6$-dimensional spaces, an isomorphism. By the inverse function theorem $\beta$ is a local diffeomorphism at $(1,1)$, so $\operatorname{im}\beta$ contains an open neighbourhood of $I$; being a subgroup, $\operatorname{im}\beta$ is open, hence closed, hence (as $SO(4)$ is connected) equal to $SO(4)$. Therefore $\beta$ is surjective. $\blacksquare$

> [!warning] Illegal but tempting route: reading surjectivity off the differential alone.
> It is tempting to say "$d\beta$ is an isomorphism, so $\beta$ is onto". This is false in general: the differential being an isomorphism gives only that the image is *open*, i.e. surjectivity *near the identity*. A homomorphism can be a local diffeomorphism with image a proper open subgroup — for instance the inclusion of a connected group into a disconnected one, such as $SO(2)\hookrightarrow O(2)$, is a local diffeomorphism onto the *identity component* only. What rescues the argument is the extra hypothesis that the *target* $SO(4)$ is connected: only then does "open subgroup" force "everything". Drop connectedness and the conclusion fails; this is exactly why Lemma 4 of the ambient theorem is invoked by name.

---

# Key Takeaways

**A condition quantified over all elements is attacked by specialising the free variable, and the right specialisations here are $h=1$ and $h$ imaginary.** The kernel equation $q_+h\bar q_-=h$ looks like one equation but is a whole family, one per $h$; the art is to pick the few members that pin the unknowns down. The identity $h=1$ is special because it is the *unit* of the algebra: it turns a conjugation-type expression into a bare product $q_+\bar q_-$, decoupling the two factors. The imaginary units $i,j$ are special because, together with $1$ and $k=ij$, they *span* the algebra, so commuting with them is the same as commuting with everything. This "evaluate at the identity, then at generators" reflex recurs whenever a hypothesis is a relation holding for all vectors: kernels of representations, centralisers, isotropy computations, and — as here — the centre of an algebra. When you next meet "$X\,\square\,v=v$ for all $v$", reach first for $v=$ the identity or the unit, then for $v$ ranging over a spanning set.

**The centre of the quaternions is $\mathbb{R}$, and this single fact does double duty: it computes the kernel and, in linearised form, proves the differential is injective.** The reason $\beta$ is exactly two-to-one — not three-, not one-to-one — is that the only unit quaternions commuting with all of $\mathbb{H}$ are $\pm1$; the deck group of the cover *is* the group of units of the centre. Notice how the very same computation returns at the infinitesimal level: "$x_+$ commutes with all $h$" forces $x_+\in\mathbb{R}$, but $x_+$ is imaginary, so $x_+=0$. The kernel of a homomorphism and the kernel of its differential are governed by the same commutativity, one at the group level ($\{\pm1\}$) and one at the Lie-algebra level ($\{0\}$) — which is exactly why a covering map has *discrete* kernel and *injective* differential simultaneously. The transferable diagnostic: whenever you have computed the kernel of a Lie group homomorphism by a commutation argument, the injectivity of its differential is almost certainly the same argument with "$=1$" replaced by "$=0$", and you should expect to reuse it verbatim.

**Surjectivity of a Lie group homomorphism is a topological statement — local diffeomorphism plus connectedness — never an algebraic solve.** One is rarely handed a formula for the inverse of a covering map, and one never needs one. The invertibility of $d\beta$ buys *openness of the image* through the inverse function theorem; the image being a *subgroup* upgrades openness to closedness (its complement is a union of cosets); and *connectedness of the target* forbids a proper nonempty clopen subset, forcing the image to be everything. Each of the three ingredients is essential and each fails a recognisable way if dropped: without invertible differential the image may be lower-dimensional, without the subgroup structure openness need not give closedness, and without connectedness (the $O(2)$ warning above) an open subgroup can be proper. Store this as the standard three-step template for "is this homomorphism onto?": compute the differential, check it is surjective (here, an isomorphism by dimension count), then invoke connectedness of the codomain. Companion drills: [[Ex - so(4) Splits as so(3) plus so(3) via Self-Dual Forms]] takes the differential $d\beta$ computed here and reads off the Lie-algebra splitting $\mathfrak{so}(4)\cong\mathfrak{so}(3)\oplus\mathfrak{so}(3)$, so the two exercises are best practised as a pair.
