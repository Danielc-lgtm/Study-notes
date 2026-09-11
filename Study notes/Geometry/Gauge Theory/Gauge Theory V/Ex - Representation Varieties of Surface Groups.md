---
type: exercise
subject: gauge-theory
prereqs:
  - "Thm - The Moduli Space of Flat Connections with Compact Structure Group is Compact"
  - "Thm - Flat Connections and Monodromy Representations of the Fundamental Group"
  - "Def - Free Group and Free Product"
  - "Def - Quotient Group"
difficulty: "⭐⭐"
tags: [geometry, gauge-theory]
---

# Problem Statement

For a genus $g\ge1$ let $\Gamma_g$ be the abstractly presented group
$$\Gamma_g=\Big\langle\,a_1,\dots,a_g,\,b_1,\dots,b_g\ \Big|\ \prod_{i=1}^g[a_i,b_i]=1\,\Big\rangle,\qquad [a,b]:=aba^{-1}b^{-1},$$
the **surface group** of genus $g$, and let $G$ be a Lie group. Prove the following.

1. **The representation variety is a relation variety.** For every $G$ there is a bijection
$$\operatorname{Hom}(\Gamma_g,G)\;\xrightarrow{\ \cong\ }\;\mathcal Z_g(G):=\Big\{(A_1,\dots,A_g,B_1,\dots,B_g)\in G^{2g}\ :\ \prod_{i=1}^g[A_i,B_i]=1\Big\},$$
$\rho\mapsto(\rho(a_i),\rho(b_i))_i$, equivariant for the conjugation action of $G$ (on the left $g\cdot\rho:=g\rho(\cdot)g^{-1}$, on the right simultaneous conjugation of all $2g$ entries), hence a bijection of quotients
$$\operatorname{Hom}(\Gamma_g,G)/G\;\cong\;\mathcal Z_g(G)/G.$$

2. **The abelian case.** For $G=U(1)$ obtain $\operatorname{Hom}(\Gamma_g,U(1))/U(1)=U(1)^{2g}$.

3. **The smallest non-abelian case.** For $G=SU(2)$ and $g=1$ describe $\operatorname{Hom}(\Gamma_1,SU(2))/SU(2)$: it is the set of commuting pairs in $SU(2)$ up to conjugation, which is the **pillowcase** $T^2/\{\pm1\}$ — the quotient of the two-torus $T^2$ by the simultaneous inversion $(\alpha,\beta)\mapsto(-\alpha,-\beta)$, a topological two-sphere with four cone points of angle $\pi$.

> **Scope remark (not proved and not used in this series).** For a closed orientable surface $\Sigma_g$ of genus $g$ it is standard that $\pi_1(\Sigma_g)\cong\Gamma_g$; this is proved by applying the **Seifert–van Kampen theorem** to the standard identification of $\Sigma_g$ with a $4g$-gon whose boundary spells the word $\prod_i[a_i,b_i]$. That identification is not established in this series (the Seifert–van Kampen theorem is not proved here), and nothing below relies on it: the exercise treats $\Gamma_g$ purely as the abstract group above. Where we speak of the *representation variety of the surface group* we mean $\mathcal R(\Sigma_g;G)=\operatorname{Hom}(\Gamma_g,G)/G$ by definition, and the geometric statement "this is the moduli space of flat $G$-connections on $\Sigma_g$" is the content of the correspondence theorem applied once one knows $\pi_1(\Sigma_g)=\Gamma_g$.

**Recall.**

The geometric meaning of the object, and its compactness for compact $G$, come from the two chapter-V theorems, restated here in full.

![[Thm - The Moduli Space of Flat Connections with Compact Structure Group is Compact#Statement]]

![[Thm - Flat Connections and Monodromy Representations of the Fundamental Group#Statement]]

Part 1 is pure group theory built on two universal properties.

![[Def - Free Group and Free Product#The Definition]]

The **free group** $F(X)$ on a set $X$ has the universal property that a homomorphism $F(X)\to G$ is the same datum as an arbitrary set map $X\to G$: a homomorphism is *determined* by, and *freely prescribable* through, the images of the generators. Concretely, for $X=\{a_1,\dots,a_g,b_1,\dots,b_g\}$, restriction to $X$ is a bijection $\operatorname{Hom}(F(X),G)\xrightarrow{\cong}G^{2g}$ (see [[Ex - The free group as a universal arrow|the free group as a universal arrow]]).

![[Def - Quotient Group#The Definition]]

A **presentation** $\langle X\mid R\rangle$ is the group $F(X)/N$, where $N\trianglelefteq F(X)$ is the *normal closure* of the relator set $R\subseteq F(X)$ — the smallest normal subgroup containing $R$, equal to the set of all finite products of conjugates $w r^{\pm1}w^{-1}$ with $w\in F(X)$, $r\in R$. Here $R=\{\,r\,\}$ with the single relator $r=\prod_{i=1}^g[a_i,b_i]$, so $\Gamma_g=F(X)/N$ with $N$ the normal closure of that one word. We write $[a,b]=aba^{-1}b^{-1}$ throughout; $T=\{\operatorname{diag}(e^{i\alpha},e^{-i\alpha}):\alpha\in\mathbb R/2\pi\mathbb Z\}\cong U(1)$ is the diagonal maximal torus of $SU(2)$, and $I$ is the identity matrix.

---

# Convergent Strategy

**Problem class.** This is a *coordinatise-a-representation-variety* problem: an abstract representation space $\operatorname{Hom}(\Gamma,G)/G$ is to be turned into an explicit algebraic subset of a power of $G$, and then, in small cases, into a recognisable geometric object. The engine is not analysis but the universal property of a group presentation, which translates "homomorphism out of $\langle X\mid R\rangle$" into "tuple of images satisfying the relations". The genus-one, $SU(2)$ case is the first place in the series where a moduli space is *singular* — an orbifold rather than a manifold — and computing it by hand is the point.

**Assumption pattern.** The group $\Gamma_g$ is handed to us *by a presentation*, and a presentation is used in exactly one way: through the universal property $\operatorname{Hom}(F/N,G)=\{\psi\in\operatorname{Hom}(F,G):\psi(N)=1\}$, which for a normal closure of relators reduces to $\{\psi:\psi(r)=1\ \forall r\in R\}$. The recognisable trigger is "a group given by generators and relations, mapped into a target": always evaluate on generators and impose the relations. For part 3 the further hypothesis is that $G=SU(2)$ is a rank-one compact group, so its maximal tori are circles and its Weyl group is $\mathbb Z/2$ acting by inversion — the two facts that make the commuting-variety quotient computable.

**Theorem routing.** Part 1 routes through the [[Def - Free Group and Free Product|free-group universal property]] ($\operatorname{Hom}(F,G)\cong G^{2g}$) followed by the [[Def - Quotient Group|quotient universal property]] (impose $\psi(r)=1$, i.e. $\prod[A_i,B_i]=1$), with conjugation-equivariance checked directly. Part 2 substitutes $G=U(1)$: abelianness makes every commutator trivial, so the relation is vacuous and conjugation is trivial. Part 3 substitutes $G=SU(2)$, $g=1$, giving the *commuting variety* $\{(A,B):AB=BA\}/\text{conj}$, which is analysed by the maximal-torus theory of $SU(2)$: diagonalise, use that the centraliser of a regular element is a maximal torus, reduce to $T\times T$ modulo the Weyl group. The geometric interpretation — that $\operatorname{Hom}(\Gamma_g,G)/G$ is a *moduli space of flat connections*, compact when $G$ is compact — is supplied by the [[Thm - Flat Connections and Monodromy Representations of the Fundamental Group|correspondence theorem]] and the [[Thm - The Moduli Space of Flat Connections with Compact Structure Group is Compact|compactness theorem]].

**Key decision point.** The single non-obvious move in part 3 is to *reduce a commuting pair to a common maximal torus and then quotient only by the Weyl group*. Two commuting elements need not both be diagonalisable in the *same* basis a priori; the insight is that if one of them, say $A$, is *regular* (not central), its centraliser is exactly the maximal torus $T$ containing it, so any $B$ commuting with $A$ automatically lies in $T$ — the pair is simultaneously diagonalisable. The residual freedom after fixing $T$ is the normaliser $N(T)$, and $N(T)/T$ is the Weyl group $\mathbb Z/2$ acting by simultaneous inversion. Overlooking the central cases ($A$ or $B\in\{\pm I\}$) misses the four cone points; forgetting the Weyl quotient double-counts every generic pair.

---

# Legal Operations Used

These are the §5.4 operations as they will appear on [[Gauge Theory V — Parallel Transport, Holonomy, Gauge Transformations, and Flat Connections|the topic page's Legal Operations]]; named descriptively here, with numbering reconciled by the coordinator.

1. **Evaluate a homomorphism on generators (free-group universal property).** Turn $\operatorname{Hom}(F(X),G)$ into $G^{|X|}$ by restriction to the generating set.

2. **Impose the relators (quotient universal property).** Cut $G^{|X|}$ down to the tuples annihilating every relator, using that a homomorphism kills a normal closure as soon as it kills the relators.

3. **Transport a group action across a bijection.** Check that the conjugation action of $G$ on $\operatorname{Hom}(\Gamma_g,G)$ corresponds under the coordinatisation to simultaneous conjugation on $G^{2g}$, so the quotients correspond.

4. **Collapse relations and conjugation for an abelian target.** When $G$ is abelian every commutator is trivial and conjugation is the identity, so the relation variety is all of $G^{2g}$ and the quotient is trivial.

5. **Diagonalise into a maximal torus.** Use that every element of a compact connected group is conjugate into a fixed maximal torus; for $SU(2)$ this is unitary diagonalisation with the determinant normalised to one.

6. **Replace a centraliser by a maximal torus for a regular element.** For $A$ not central in $SU(2)$, the centraliser is the maximal torus through $A$, so anything commuting with $A$ is simultaneously diagonal.

7. **Quotient a torus by its Weyl group.** Reduce conjugacy of tuples in $T$ to the residual action of $N(T)/T$, the Weyl group $\mathbb Z/2$ acting by inversion, and read off the orbifold.

---

# Hints

> [!note]- Hint 1
> A homomorphism out of $\langle a_i,b_i\mid r\rangle$ is nothing but a choice of images $A_i=\rho(a_i)$, $B_i=\rho(b_i)$ subject to the single constraint that the relator maps to the identity. What is $\rho(r)$ in terms of the $A_i,B_i$?

> [!note]- Hint 2
> Make the universal property precise. Write $\Gamma_g=F/N$ with $F$ free on the $2g$ generators and $N$ the normal closure of $r$. A homomorphism $\psi\colon F\to G$ descends to $F/N$ iff $\psi(N)=1$; because $N$ is *generated as a normal subgroup* by $r$, this happens iff $\psi(r)=1$. Now $\psi(r)=\prod[A_i,B_i]$.

> [!note]- Hint 3
> For $G=U(1)$: what is a commutator $[A_i,B_i]$ in an abelian group? Then the relation $\prod[A_i,B_i]=1$ says nothing, and conjugation does nothing. Count the free choices.

> [!note]- Hint 4
> For $G=SU(2)$, $g=1$: the relation is $[A,B]=1$, i.e. $A$ and $B$ commute. First diagonalise: every $A\in SU(2)$ is conjugate to $\operatorname{diag}(e^{i\alpha},e^{-i\alpha})$. If $A\ne\pm I$, what are the matrices that commute with a diagonal matrix with *distinct* diagonal entries?

> [!note]- Hint 5
> Having put both $A,B$ into the diagonal torus $T$, ask what residual conjugations preserve $T$. The normaliser $N(T)$ has $N(T)/T\cong\mathbb Z/2$, generated by $w=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)$, which conjugates $\operatorname{diag}(e^{i\theta},e^{-i\theta})$ to $\operatorname{diag}(e^{-i\theta},e^{i\theta})$. So on $T\times T$ the leftover identification is $(\alpha,\beta)\sim(-\alpha,-\beta)$. Find the fixed points of this involution — they are the singular points of the quotient.

---

# Solution

The plan is to make the universal property of the presentation carry all of part 1, so that $\operatorname{Hom}(\Gamma_g,G)/G$ becomes an explicit relation variety modulo conjugation; then parts 2 and 3 are substitutions $G=U(1)$ and $G=SU(2)$. The abelian case is immediate because commutators and conjugation both trivialise. The genus-one $SU(2)$ case is the substantive computation: commuting pairs are simultaneously diagonalisable, so the variety reduces to $T\times T$ modulo the Weyl group, whose quotient is the pillowcase.

**Step 1: Part 1 — the presentation universal property gives the relation variety, equivariantly.**

Evaluating a representation on the generators is a conjugation-equivariant bijection $\operatorname{Hom}(\Gamma_g,G)\cong\mathcal Z_g(G)$, hence descends to $\operatorname{Hom}(\Gamma_g,G)/G\cong\mathcal Z_g(G)/G$.

> [!note]- Derivation
> Write $F=F(X)$, $X=\{a_1,\dots,a_g,b_1,\dots,b_g\}$, and $\Gamma_g=F/N$ with $N\trianglelefteq F$ the normal closure of the single relator $r=\prod_{i=1}^g[a_i,b_i]$; let $\pi\colon F\to\Gamma_g$ be the projection.
>
> **Free-group step.** By the [[Def - Free Group and Free Product|universal property of the free group]], restriction to $X$ is a bijection
> $$\operatorname{Hom}(F,G)\xrightarrow{\ \cong\ }G^{2g},\qquad\psi\mapsto(\psi(a_i),\psi(b_i))_i\qquad\text{(a homomorphism out of }F\text{ is a free choice of generator images).}$$
>
> **Quotient step.** By the [[Def - Quotient Group|universal property of the quotient]], a homomorphism $\psi\colon F\to G$ factors (uniquely) as $\psi=\varphi\circ\pi$ for some $\varphi\colon\Gamma_g\to G$ if and only if $\psi(N)=1$. Now $N$ is the normal closure of $\{r\}$, i.e. $N$ consists of finite products of conjugates $wr^{\pm1}w^{-1}$; since $\psi$ is a homomorphism, $\psi(wr^{\pm1}w^{-1})=\psi(w)\psi(r)^{\pm1}\psi(w)^{-1}$, so
> $$\psi(N)=1\iff\psi(r)=1\qquad\text{(a homomorphism kills the whole normal closure as soon as it kills the relator).}$$
> Composing the two steps, and computing
> $$\psi(r)=\psi\!\Big(\prod_i[a_i,b_i]\Big)=\prod_i[\psi(a_i),\psi(b_i)]=\prod_i[A_i,B_i]\qquad\text{(}\psi\text{ a homomorphism),}$$
> with $A_i:=\psi(a_i)=\varphi(\pi(a_i))$, $B_i:=\psi(b_i)$, we obtain the bijection
> $$\operatorname{Hom}(\Gamma_g,G)\xrightarrow{\ \cong\ }\mathcal Z_g(G)=\Big\{(A_i,B_i)\in G^{2g}:\prod_i[A_i,B_i]=1\Big\},\qquad\varphi\mapsto(\varphi(\bar a_i),\varphi(\bar b_i))_i,$$
> writing $\bar a_i=\pi(a_i)$ for the generators of $\Gamma_g$. Uniqueness of $\varphi$ (the quotient universal property) makes this a genuine bijection.
>
> **Equivariance.** The group $G$ acts on $\operatorname{Hom}(\Gamma_g,G)$ by $s\cdot\varphi:=s\,\varphi(\cdot)\,s^{-1}$ and on $\mathcal Z_g(G)$ by simultaneous conjugation $s\cdot(A_i,B_i):=(sA_is^{-1},sB_is^{-1})$. Under the bijection, $s\cdot\varphi$ maps $\bar a_i\mapsto s\varphi(\bar a_i)s^{-1}=sA_is^{-1}$ and likewise for $\bar b_i$, so the bijection intertwines the two actions:
> $$(s\cdot\varphi)\longmapsto s\cdot(A_i,B_i)\qquad\text{(equivariance).}$$
> A bijection equivariant for two group actions descends to a bijection of orbit spaces; hence
> $$\operatorname{Hom}(\Gamma_g,G)/G\;\cong\;\mathcal Z_g(G)/G.$$
> This is part 1.

**Step 2: Part 2 — the abelian case is $U(1)^{2g}$.**

For $G=U(1)$ the relation is vacuous and conjugation is trivial, so $\operatorname{Hom}(\Gamma_g,U(1))/U(1)=U(1)^{2g}$.

> [!note]- Derivation
> **The relation trivialises.** In the abelian group $U(1)$ every commutator is the identity: $[A_i,B_i]=A_iB_iA_i^{-1}B_i^{-1}=1$ for all $A_i,B_i\in U(1)$. Hence the defining condition $\prod_i[A_i,B_i]=1$ holds automatically, and
> $$\mathcal Z_g(U(1))=\{(A_i,B_i)\in U(1)^{2g}:1=1\}=U(1)^{2g}\qquad\text{(no constraint).}$$
> **Conjugation trivialises.** Again because $U(1)$ is abelian, $sA_is^{-1}=A_i$, so the conjugation action on $U(1)^{2g}$ is trivial and $\mathcal Z_g(U(1))/U(1)=U(1)^{2g}$. By Step 1,
> $$\operatorname{Hom}(\Gamma_g,U(1))/U(1)=U(1)^{2g}.$$
> **Cross-check via the abelianisation.** For any abelian target, $\operatorname{Hom}(\Gamma_g,U(1))=\operatorname{Hom}(\Gamma_g^{\mathrm{ab}},U(1))$, where $\Gamma_g^{\mathrm{ab}}=\Gamma_g/[\Gamma_g,\Gamma_g]$. The relator $\prod_i[a_i,b_i]$ is a product of commutators, hence trivial in the abelianisation, so $\Gamma_g^{\mathrm{ab}}$ is the free abelian group on the $2g$ images of the generators, $\Gamma_g^{\mathrm{ab}}\cong\mathbb Z^{2g}$; and $\operatorname{Hom}(\mathbb Z^{2g},U(1))=U(1)^{2g}$, confirming the count.

**Step 3: Part 3 — for $SU(2)$, $g=1$, the variety is commuting pairs modulo conjugation, and every commuting pair is simultaneously diagonalisable.**

With $G=SU(2)$ and $g=1$ the relation is $[A,B]=1$, so $\mathcal Z_1(SU(2))=\{(A,B):AB=BA\}$; every such pair is conjugate to a pair in the diagonal torus $T\times T$.

> [!note]- Derivation
> For $g=1$ the relator is $r=[a_1,b_1]$, so $\mathcal Z_1(SU(2))=\{(A,B)\in SU(2)^2:[A,B]=1\}=\{(A,B):AB=BA\}$, the **commuting variety** of $SU(2)$.
>
> **Lemma A (diagonalisation).** *Every $A\in SU(2)$ is conjugate in $SU(2)$ to $\operatorname{diag}(e^{i\theta},e^{-i\theta})\in T$ for some $\theta$.* Indeed $A$ is unitary, hence normal, so by the finite-dimensional spectral theorem there is an orthonormal eigenbasis and a $U\in U(2)$ with $U^{-1}AU=\operatorname{diag}(\lambda_1,\lambda_2)$; the eigenvalues satisfy $|\lambda_k|=1$ (eigenvalues of a unitary matrix) and $\lambda_1\lambda_2=\det A=1$, so $\lambda_2=\lambda_1^{-1}=\overline{\lambda_1}$ and we write $\lambda_1=e^{i\theta}$. Replacing the first column $u_1$ of $U$ by $(\det U)^{-1}u_1$ rescales $\det U$ to $1$ without disturbing $U^{-1}AU$ (a diagonal conjugation commutes with a diagonal matrix), so we may take $U\in SU(2)$. Thus $U^{-1}AU=\operatorname{diag}(e^{i\theta},e^{-i\theta})\in T$.
>
> **Lemma B (centraliser of a regular element).** *If $A=\operatorname{diag}(e^{i\alpha},e^{-i\alpha})\in T$ with $e^{i\alpha}\ne e^{-i\alpha}$ (that is $A\ne\pm I$), then every $B\in SU(2)$ commuting with $A$ is diagonal, so lies in $T$.* Write $B=(b_{kl})$. The $(1,2)$ entry of $AB$ is $e^{i\alpha}b_{12}$ and of $BA$ is $b_{12}e^{-i\alpha}$; equality forces $(e^{i\alpha}-e^{-i\alpha})b_{12}=0$, and since $e^{i\alpha}\ne e^{-i\alpha}$ we get $b_{12}=0$. Symmetrically $b_{21}=0$. Hence $B$ is diagonal, and being in $SU(2)$ it is $\operatorname{diag}(e^{i\beta},e^{-i\beta})\in T$. In particular the centraliser of a regular $A$ is exactly $T$.
>
> **Simultaneous diagonalisation.** Let $(A,B)$ be a commuting pair. If $A\ne\pm I$, conjugate by Lemma A so that $A\in T$ is regular; then Lemma B puts $B\in T$ as well, and the pair now lies in $T\times T$. If instead $A=\pm I$ (central, so it commutes with everything and imposes no constraint on $B$), apply Lemma A to $B$: some conjugate sends $B$ into $T$, while $A=\pm I$ is fixed by every conjugation and stays in $T$. Either way, **every commuting pair is conjugate to a pair in $T\times T$.**

**Step 4: Part 3 — the leftover identification is the Weyl group, and the quotient is the pillowcase.**

Two pairs of $T\times T$ are $SU(2)$-conjugate exactly when related by the simultaneous inversion $(\alpha,\beta)\mapsto(-\alpha,-\beta)$; hence $\operatorname{Hom}(\Gamma_1,SU(2))/SU(2)\cong T^2/\{\pm1\}$, the pillowcase.

> [!note]- Derivation
> Parametrise $T\cong\mathbb R/2\pi\mathbb Z$ by $\alpha\mapsto\operatorname{diag}(e^{i\alpha},e^{-i\alpha})$ (a bijection), so $T\times T\cong T^2$ with coordinates $(\alpha,\beta)$. By Step 3 the conjugation-orbit map $T^2\to\mathcal Z_1(SU(2))/SU(2)$ is **surjective**; we compute its fibres.
>
> **The Weyl group acts by inversion.** The normaliser of $T$ in $SU(2)$ satisfies $N(T)/T\cong\mathbb Z/2$, generated by the coset of $w=\left(\begin{smallmatrix}0&1\\-1&0\end{smallmatrix}\right)\in SU(2)$; a direct computation gives
> $$w\,\operatorname{diag}(e^{i\theta},e^{-i\theta})\,w^{-1}=\operatorname{diag}(e^{-i\theta},e^{i\theta})\qquad\text{(}w\text{ swaps the two coordinate axes).}$$
> So on the parameter, $w$ sends $\theta\mapsto-\theta$. Elements of $T$ act trivially on $T$ (it is abelian). Hence $N(T)$ acts on $T^2$ through $N(T)/T=\{1,w\}=:W$ by
> $$1\cdot(\alpha,\beta)=(\alpha,\beta),\qquad w\cdot(\alpha,\beta)=(-\alpha,-\beta).$$
>
> **The fibres are exactly the $W$-orbits.** Suppose $(A,B),(A',B')\in T\times T$ are conjugate, $g(A,B)g^{-1}=(A',B')$. We show $g$ acts through $W$.
> - *If $A$ (or, symmetrically, $B$) is regular:* say $A\ne\pm I$. Then $A'=gAg^{-1}$ is also regular, and by Lemma B the centraliser of a regular element is the maximal torus through it, so $g\,T\,g^{-1}=g\,Z(A)\,g^{-1}=Z(A')=T$ — because both $A,A'\in T$ regular have centraliser $T$. Thus $g\in N(T)$, and $(A',B')=g\cdot(A,B)$ with $g$ acting through $W$: either $(A',B')=(A,B)$ (if $g\in T$) or $(A',B')=(A^{-1},B^{-1})$ (if $g\in wT$), i.e. $(\alpha,\beta)$ and $(-\alpha,-\beta)$.
> - *If both $A,B$ are central* ($\in\{\pm I\}$): the pair is fixed by *every* conjugation, and its $W$-orbit is $\{(\alpha,\beta)\}$ itself, since $\alpha,\beta\in\{0,\pi\}$ satisfy $(-\alpha,-\beta)=(\alpha,\beta)$. So conjugacy and $W$-relatedness both reduce to equality.
>
> In all cases $(A,B)\sim(A',B')$ under $SU(2)$-conjugation if and only if $(\alpha,\beta)$ and $(\alpha',\beta')$ lie in the same $W$-orbit. Therefore
> $$\operatorname{Hom}(\Gamma_1,SU(2))/SU(2)=\mathcal Z_1(SU(2))/SU(2)\;\cong\;T^2/W=T^2/\{(\alpha,\beta)\sim(-\alpha,-\beta)\}.$$
>
> **The quotient is the pillowcase.** The involution $\iota(\alpha,\beta)=(-\alpha,-\beta)$ of $T^2=(\mathbb R/2\pi\mathbb Z)^2$ has fixed points precisely where $2\alpha\equiv0$ and $2\beta\equiv0\pmod{2\pi}$, i.e. $\alpha,\beta\in\{0,\pi\}$: the four points
> $$(0,0),\ (0,\pi),\ (\pi,0),\ (\pi,\pi)\ \longleftrightarrow\ (A,B)\in\{(I,I),(I,-I),(-I,I),(-I,-I)\}.$$
> Away from these, $\iota$ is a free involution, so the quotient is a surface; at each fixed point the quotient has a cone singularity of angle $\pi$ (the involution looks like $z\mapsto-z$ on a transverse disc, whose quotient is a cone of angle $\pi$). The Euler characteristic of the quotient is $\chi(T^2/W)=\tfrac12\big(\chi(T^2)+\#\mathrm{Fix}\big)=\tfrac12(0+4)=2$, so the underlying space is a two-sphere. This two-sphere with four cone points of angle $\pi$ is the **pillowcase**. Hence $\operatorname{Hom}(\Gamma_1,SU(2))/SU(2)$ is the pillowcase $T^2/\{\pm1\}$, a compact space (as the [[Thm - The Moduli Space of Flat Connections with Compact Structure Group is Compact|compactness theorem]] guarantees, $SU(2)$ being compact) but not a manifold.

> [!note]- Complete formal solution
> **Claim.** $\operatorname{Hom}(\Gamma_g,G)/G\cong\mathcal Z_g(G)/G$ for every $G$; this is $U(1)^{2g}$ for $G=U(1)$; and for $G=SU(2)$, $g=1$ it is the pillowcase $T^2/\{\pm1\}$.
>
> *Part 1.* Write $\Gamma_g=F/N$, $F$ free on the $2g$ generators, $N$ the normal closure of $r=\prod_i[a_i,b_i]$. The free-group universal property gives $\operatorname{Hom}(F,G)\cong G^{2g}$ by restriction to generators. The quotient universal property gives $\operatorname{Hom}(\Gamma_g,G)=\{\psi\in\operatorname{Hom}(F,G):\psi(N)=1\}$; as $N$ is the normal closure of $r$ and $\psi$ is a homomorphism, $\psi(N)=1\iff\psi(r)=1\iff\prod_i[A_i,B_i]=1$ where $A_i=\psi(a_i),B_i=\psi(b_i)$. So $\operatorname{Hom}(\Gamma_g,G)\cong\mathcal Z_g(G)$, and the isomorphism intertwines $s\cdot\varphi=s\varphi(\cdot)s^{-1}$ with simultaneous conjugation, hence $\operatorname{Hom}(\Gamma_g,G)/G\cong\mathcal Z_g(G)/G$.
>
> *Part 2.* For $G=U(1)$ abelian, $[A_i,B_i]=1$ always, so $\mathcal Z_g(U(1))=U(1)^{2g}$, and conjugation is trivial, giving $U(1)^{2g}$. (Equivalently $\Gamma_g^{\mathrm{ab}}\cong\mathbb Z^{2g}$ and $\operatorname{Hom}(\mathbb Z^{2g},U(1))=U(1)^{2g}$.)
>
> *Part 3.* For $G=SU(2)$, $g=1$: $\mathcal Z_1=\{(A,B):AB=BA\}$. Every $A\in SU(2)$ is $SU(2)$-conjugate to $\operatorname{diag}(e^{i\theta},e^{-i\theta})$ (spectral theorem, determinant normalised); a matrix commuting with a regular diagonal $A$ is diagonal; so every commuting pair is conjugate into $T\times T$. Parametrising $T\cong\mathbb R/2\pi\mathbb Z$, two pairs of $T\times T$ are conjugate iff related by $W=N(T)/T\cong\mathbb Z/2$, acting by $w\cdot(\alpha,\beta)=(-\alpha,-\beta)$ (since $w\operatorname{diag}(e^{i\theta},e^{-i\theta})w^{-1}=\operatorname{diag}(e^{-i\theta},e^{i\theta})$ and, for a regular entry, a conjugacy between diagonal pairs lies in $N(T)$). Hence the quotient is $T^2/\{(\alpha,\beta)\sim(-\alpha,-\beta)\}$. The involution has four fixed points $(\alpha,\beta)\in\{0,\pi\}^2$, is free elsewhere, and $\chi=\tfrac12(0+4)=2$; the quotient is a two-sphere with four cone points of angle $\pi$ — the pillowcase. $\blacksquare$

> [!tip] Outlook *(from non-abelian Hodge theory)*
> Part 3 is the compact toy model of a vast subject. For the non-compact reductive group $G=SL(n;\mathbb C)$ the representation variety $\operatorname{Hom}(\Gamma_g,SL(n;\mathbb C))/SL(n;\mathbb C)$ (the *character variety* of the surface) is no longer a finite quotient of a torus but a rich singular affine variety; the **non-abelian Hodge correspondence** identifies it, for $g\ge2$, with a moduli space of **Higgs bundles** on the Riemann surface, carrying a hyperkähler metric and an integrable system (the Hitchin system). This is active research (Higgs bundles, the $P=W$ conjecture); it is recorded here only as an outlook and nothing in this series depends on it. The bridge back to gauge theory is that $\operatorname{Hom}(\Gamma_g,G)/G$ is, by the correspondence theorem, the moduli of flat $G$-connections — for $G$ compact a moduli of genuine solutions of $F=0$, and for $G$ complex a moduli of flat connections whose real structure is the Higgs-bundle picture.

---

# Key Takeaways

**A group presentation is a machine for turning representations into constraint varieties, and it is used the same way every time.** The reusable move: given $\Gamma=\langle X\mid R\rangle$ and a target $G$, a homomorphism $\Gamma\to G$ is exactly a tuple $(g_x)_{x\in X}\in G^{|X|}$ such that every relator, read as a word in the $g_x$, evaluates to the identity — because a homomorphism out of $F(X)/N$ is a homomorphism out of $F(X)$ (a free choice of generator images) that kills the normal closure $N$, and it kills $N$ as soon as it kills the finitely many relators that generate $N$. The trigger is the phrase "generators and relations"; the pattern is "evaluate on generators, impose the relations"; the diagnostic that one has done it correctly is that the conjugation action of $G$ on representations must become *simultaneous* conjugation on the tuple, so that moduli (representations modulo conjugation) become the constraint variety modulo simultaneous conjugation. This single template computes every representation variety in the series, and it is why the surface relation $\prod[A_i,B_i]=1$ is the only equation that survives.

**Abelian versus non-abelian is the entire difference between a smooth torus and a singular orbifold, and the surface group displays it in one relation.** For $G=U(1)$ the commutator relation evaporates and conjugation disappears, so the moduli space is the smooth torus $U(1)^{2g}$ — flat line bundles are classified by their $2g$ holonomies around a symplectic basis of loops, with no further identification. The instant $G$ is non-abelian the same relation $\prod[A_i,B_i]=1$ becomes a genuine equation cutting out a singular subvariety of $G^{2g}$, and conjugation produces a genuine orbit space with fixed points; already for $SU(2)$ at $g=1$ the answer is the pillowcase, a sphere with four corners rather than a manifold. The transferable lesson for spaced practice: whenever a moduli problem is "the same" for abelian and non-abelian structure group, expect the abelian answer to be a torus (a product of circles, one per generator of $H_1$) and the non-abelian answer to be that torus's non-abelian thickening, singular exactly at the *reducible* representations — here the four central pairs $(\pm I,\pm I)$, whose stabiliser jumps from the centre to all of $SU(2)$.

**Commuting-variety problems in a rank-one group reduce to a torus modulo its Weyl group, and the singular points are precisely the reducibles.** The mechanism worth carrying away: to understand pairs (or tuples) of *commuting* elements up to conjugation in a compact connected group, simultaneously diagonalise into a maximal torus $T$ — legitimate because the centraliser of a *regular* element is exactly the maximal torus through it, so a commuting partner is forced to be diagonal too — and then quotient by the residual symmetry $N(T)/T$, the Weyl group. For $SU(2)$ the torus is a circle and the Weyl group is $\mathbb Z/2$ acting by inversion, so commuting pairs modulo conjugation are $T^2/\pm$, and the four fixed points of the inversion — the pairs both of whose entries are central — are exactly the reducible representations, which become the orbifold singularities. The same picture, with a larger maximal torus and Weyl group, governs $\operatorname{Hom}(\mathbb Z^k,G)/G$ for any compact $G$, and the appearance of orbifold points at reducibles is the recurring signal, throughout gauge theory, that a moduli space of connections will be singular exactly where the stabiliser of the connection is larger than the centre. The companion abelian computation [[Ex - Flat U(1)-Connections on the Torus]] is the degenerate case in which the torus is everything and there are no reducibles to create singularities.
