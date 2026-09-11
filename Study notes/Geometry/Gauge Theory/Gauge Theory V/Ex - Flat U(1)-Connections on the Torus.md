---
type: exercise
subject: gauge-theory
prereqs:
  - "Thm - The Moduli Space of Flat Connections with Compact Structure Group is Compact"
  - "Thm - Flat Connections and Monodromy Representations of the Fundamental Group"
  - "Thm - Holonomy of an Abelian Connection is the Exponential of the Curvature Integral"
  - "Def - Flat Connection"
  - "Thm - A Closed 1-Form on a Simply Connected Manifold is Exact"
difficulty: "⭐⭐"
tags: [geometry, gauge-theory]
---

# Problem Statement

Let $T^n=\mathbb R^n/(2\pi\mathbb Z)^n$ be the $n$-dimensional torus, carried with the standard angle coordinates $x^1,\dots,x^n$, each $x^j\in\mathbb R/2\pi\mathbb Z$, so that the globally defined closed one-forms $dx^1,\dots,dx^n$ satisfy $\oint_{\gamma_j}dx^k=2\pi\,\delta_{jk}$, where $\gamma_j$ is the $j$-th coordinate loop $t\mapsto(0,\dots,t,\dots,0)$, $t\in[0,2\pi]$. Let $G=U(1)$, with Lie algebra $\mathfrak u(1)=i\mathbb R$.

Prove that the moduli space of flat $U(1)$-connections on the torus is an $n$-torus,
$$\mathcal M^\flat_{U(1)}(T^n)\;\cong\;U(1)^n,$$
in **two independent ways**, and show the two identifications are the same map:

1. **Via monodromy.** Apply the correspondence between flat connections and representations of the fundamental group together with $\pi_1(T^n)\cong\mathbb Z^n$ to obtain $\mathcal M^\flat_{U(1)}(T^n)\cong\operatorname{Hom}(\mathbb Z^n,U(1))=U(1)^n$.
2. **Directly, through constant connections.** On the trivial bundle $T^n\times U(1)$ show that every flat connection is gauge equivalent to a constant connection $A_a=i\sum_{j=1}^n a_j\,dx^j$ with $a=(a_1,\dots,a_n)\in\mathbb R^n$, that two such are gauge equivalent if and only if their parameters differ by an element of $\mathbb Z^n$ ($a_j$ modulo $\mathbb Z$), so that the constant connections modulo gauge form $(\mathbb R/\mathbb Z)^n\cong U(1)^n$.

Finally, show the two identifications agree: the monodromy of $A_a$ sends $\gamma_j$ to $e^{-2\pi i a_j}$, and $a\bmod\mathbb Z^n\mapsto(e^{-2\pi i a_j})_j$ is precisely the identification of route 1. As a corollary, every flat $U(1)$-bundle over $T^n$ is trivial.

> The source (Haydys, Example 107) writes $\mathcal R(T^n;U(1))=\operatorname{Hom}(T^n,U(1))=U(1)^n$. The middle expression $\operatorname{Hom}(T^n,U(1))$ is a typo for $\operatorname{Hom}(\pi_1(T^n),U(1))$: the object is $\operatorname{Hom}$ out of the *fundamental group* $\pi_1(T^n)\cong\mathbb Z^n$, not out of the torus as a Lie group. We use the corrected form throughout.

**Recall.**

The two theorems that drive route 1 are the monodromy correspondence and the compactness (finite-generation) result; both are stated in full here so the exercise can be read without leaving the page.

![[Thm - Flat Connections and Monodromy Representations of the Fundamental Group#Statement]]

![[Thm - The Moduli Space of Flat Connections with Compact Structure Group is Compact#Statement]]

The definition of flatness and the abelian holonomy formula are what route 2 needs.

![[Def - Flat Connection#The Definition]]

By the [[Thm - Holonomy of an Abelian Connection is the Exponential of the Curvature Integral|abelian-holonomy theorem]] — for a connection with abelian structure group and local connection form $A_\alpha$, the holonomy of a loop $c$ contained in a trivialising set is $\operatorname{hol}(c)=\exp\!\big(-\oint_c A_\alpha\big)$ — the holonomy around a loop is the exponential of minus the line integral of the connection form. On the trivial bundle $T^n\times U(1)$ the whole torus is one trivialising set and $A_\alpha=A$ globally, so $\operatorname{hol}(c)=\exp(-\oint_c A)$ for every loop $c$.

We also use, on the universal cover, the following proved result.

![[Thm - A Closed 1-Form on a Simply Connected Manifold is Exact#Statement]]

Two standing pieces of notation. The connection on the trivial principal $U(1)$-bundle $T^n\times U(1)$ is recorded by a single $\mathfrak u(1)$-valued one-form $A\in\Omega^1(T^n;i\mathbb R)$ (its local connection form in the global product section), and since $\mathfrak u(1)$ is abelian its curvature is $F_A=dA$ with no bracket term. The gauge group of the trivial bundle is $\mathcal G(T^n\times U(1))\cong C^\infty(T^n,U(1))$, and a gauge transformation $g\colon T^n\to U(1)$ acts by $A\mapsto A+g^{-1}\,dg$, where $g^{-1}\,dg\in\Omega^1(T^n;i\mathbb R)$ is the pullback of the Maurer–Cartan form.

---

# Convergent Strategy

**Problem class.** This is a *compute-a-moduli-space* problem of the archetypal flat-connection kind: the space of solutions of the first-order equation $F=0$, taken modulo the gauge group, is to be identified with a finite-dimensional manifold. The characteristic feature is that two entirely different descriptions of the same quotient are available — a *topological* one (representations of $\pi_1$) and an *analytic* one (an explicit slice of connections modulo gauge) — and the real content is that they coincide. The torus is the smallest non-trivial arena in which both descriptions can be carried out completely by hand.

**Assumption pattern.** Two hypotheses do all the work. First, $G=U(1)$ is *abelian*: this collapses conjugation to the identity (so $\mathcal R=\operatorname{Hom}$ with no quotient), kills the $A\wedge A$ term in the curvature (so flatness is the linear condition $dA=0$), and makes the holonomy of a loop the honest exponential of a line integral. Second, the base is $T^n$, whose fundamental group $\mathbb Z^n$ is free abelian of finite rank and whose de Rham cohomology $H^1$ has the constant-coefficient forms $dx^j$ as a basis — so both the representation count and the harmonic-representative argument terminate in $n$ real parameters.

**Theorem routing.** Route 1 is a two-step lookup: the [[Thm - Flat Connections and Monodromy Representations of the Fundamental Group|monodromy correspondence]] gives $\mathcal M^\flat_{U(1)}(T^n)\cong\operatorname{Hom}(\pi_1(T^n),U(1))/\text{conjugation}$; abelianness deletes the quotient; and $\pi_1(T^n)\cong\mathbb Z^n$ (established inside the [[Thm - The Moduli Space of Flat Connections with Compact Structure Group is Compact|compactness theorem]] from $\pi_1(S^1)\cong\mathbb Z$ and the product formula) turns $\operatorname{Hom}(\mathbb Z^n,U(1))$ into $U(1)^n$. Route 2 is analytic: flatness $\Leftrightarrow dA=0$; every closed one-form on $T^n$ is cohomologous to a unique constant-coefficient form (proved by averaging, with exactness of the remainder read off on the universal cover $\mathbb R^n$ via the [[Thm - A Closed 1-Form on a Simply Connected Manifold is Exact|simply-connected exactness theorem]]); constant-coefficient closed forms modulo the lattice of "large" gauge transformations give $(\mathbb R/\mathbb Z)^n$. The [[Thm - Holonomy of an Abelian Connection is the Exponential of the Curvature Integral|abelian-holonomy theorem]] then bridges the two routes by computing the monodromy of the explicit representative.

**Key decision point.** The one genuinely non-obvious move is in route 2: recognising that the *gauge group has two disconnected kinds of elements*, and that they act on the space of closed forms in two qualitatively different ways. The "small" gauge transformations $g=e^{i\varphi}$ with $\varphi\colon T^n\to\mathbb R$ a genuine single-valued function contribute *exact* shifts $i\,d\varphi$ and serve only to normalise a general closed form to its constant-coefficient part; the "large" gauge transformations $g_k(x)=e^{i\,k\cdot x}$ with $k\in\mathbb Z^n$, which wind non-trivially around the loops $\gamma_j$, contribute the *integral* shifts $a_j\mapsto a_j+k_j$ and are exactly what compactifies the parameter space $\mathbb R^n$ down to the torus $(\mathbb R/\mathbb Z)^n$. Missing the large gauge transformations gives the wrong answer $\mathbb R^n$; treating flatness as more than $dA=0$ (forgetting that $A\wedge A=0$ for $U(1)$) makes the problem look non-linear when it is not.

---

# Legal Operations Used

These are the operations of §5.4 as they will appear on [[Gauge Theory V — Parallel Transport, Holonomy, Gauge Transformations, and Flat Connections|the topic page's Legal Operations]]; each is named descriptively here and the coordinator reconciles the numbering.

1. **Pass to the monodromy representation.** Replace a flat connection by the homomorphism $\pi_1\to G$ recording its holonomy on homotopy classes of loops; this is the operation that converts the analytic object $(P,\omega)$ into the algebraic object $\rho_\omega$, and by the correspondence theorem it is a bijection on gauge-equivalence classes.

2. **Delete conjugation for an abelian target.** When $G$ is abelian, $g\rho(\cdot)g^{-1}=\rho(\cdot)$ for all $g$, so $\mathcal R(M;G)=\operatorname{Hom}(\pi_1(M),G)$ with no quotient; here it turns the representation variety directly into a group of characters.

3. **Evaluate a homomorphism on generators.** A homomorphism out of a group given by generators is determined by, and freely prescribable through, its values on the generators (subject to the relations); for the free abelian group $\mathbb Z^n$ this identifies $\operatorname{Hom}(\mathbb Z^n,U(1))$ with $U(1)^n$.

4. **Reduce flatness to a linear equation for an abelian structure group.** For $G$ abelian the curvature of $A$ is $F_A=dA$, so "flat" means "closed"; the moduli problem becomes linear algebra on differential forms.

5. **Normalise a closed form to its constant-coefficient (harmonic) representative by a small gauge transformation.** Average the closed form over the translation group of the torus and absorb the exact remainder into $A\mapsto A+i\,d\varphi$ with $\varphi$ single-valued.

6. **Quotient by the lattice of large gauge transformations.** Use the winding maps $g_k(x)=e^{i\,k\cdot x}$, $k\in\mathbb Z^n$, to implement the integer shifts $a\mapsto a+k$, compactifying $\mathbb R^n$ to $(\mathbb R/\mathbb Z)^n$.

7. **Compute holonomy of an abelian connection as $\exp$ of a line integral.** Apply $\operatorname{hol}(c)=\exp(-\oint_c A)$ to the explicit representative to read off the monodromy and match the two coordinatisations.

---

# Hints

> [!note]- Hint 1
> The phrase "in two ways … and show they agree" tells you the structure of the answer before you compute anything: one route is a citation chain (a theorem plus a fact about $\pi_1$), the other is an honest computation with connections and gauge transformations. Start with the citation chain — it fixes the target $U(1)^n$ — and only then work to produce the same $U(1)^n$ by hand.

> [!note]- Hint 2
> Route 1: The monodromy theorem gives a bijection $\mathcal M^\flat_G(M)\cong\operatorname{Hom}(\pi_1(M),G)/\text{conj}$. What does "conjugation" do when $G=U(1)$? And what is $\operatorname{Hom}(\mathbb Z^n,U(1))$ when you remember that $\mathbb Z^n$ is *free* abelian — how much freedom do you have in choosing where the $n$ generators go?

> [!note]- Hint 3
> Route 2: On the trivial bundle a connection is a single one-form $A=i\omega$ with $\omega$ real. Since $U(1)$ is abelian, $F_A=dA$, so flat means $\omega$ is closed. Two flat connections are gauge equivalent when they differ by $g^{-1}dg$ for some $g\colon T^n\to U(1)$. Split the question: which $g$ are *exact* shifts (single-valued $\varphi$ with $g=e^{i\varphi}$), and which shift by something with non-zero periods?

> [!note]- Hint 4
> To normalise a closed $\omega$: its average $\bar\omega=\sum_j c_j\,dx^j$ over the torus is a constant-coefficient form with $c_j=\tfrac1{2\pi}\oint_{\gamma_j}\omega$. Pull $\omega-\bar\omega$ back to $\mathbb R^n$; it is closed on a simply connected space, hence exact, $\omega-\bar\omega=d\tilde\varphi$; check $\tilde\varphi$ is $(2\pi\mathbb Z)^n$-periodic (its increments over the lattice are the vanishing periods of $\omega-\bar\omega$), so it descends to $T^n$ and $g=e^{-i\tilde\varphi}$ is a genuine gauge transformation carrying $A$ to $i\bar\omega$.

> [!note]- Hint 5
> To match the routes: compute $\operatorname{hol}(\gamma_j)$ for $A_a=i\sum a_k\,dx^k$ using $\operatorname{hol}(c)=\exp(-\oint_c A)$ and $\oint_{\gamma_j}dx^k=2\pi\delta_{jk}$. You should get $e^{-2\pi i a_j}$. The large gauge transformation $g_k$ shifts $a_j\mapsto a_j+k_j$ and leaves $e^{-2\pi i a_j}$ unchanged — which is why the invariant is $a_j$ *modulo* $\mathbb Z$.

---

# Solution

The plan is to run the two routes and then lay them side by side. Route 1 is short: the monodromy correspondence plus $\pi_1(T^n)=\mathbb Z^n$ plus abelianness give $\mathcal M^\flat=U(1)^n$ immediately. Route 2 is the substantive computation: flatness is closedness, every closed form is small-gauge-equivalent to a constant one, and the constant ones are counted modulo the integer lattice coming from large gauge transformations. The final step computes the monodromy of the explicit constant representative and finds it is exactly the point of $U(1)^n$ that route 1 assigns, so the two identifications are literally the same map — and, as a by-product, every flat $U(1)$-bundle over $T^n$ turns out to be trivial.

**Step 1: Route 1 — the monodromy correspondence gives $U(1)^n$.**

The monodromy correspondence, abelianness, and $\pi_1(T^n)\cong\mathbb Z^n$ combine to give $\mathcal M^\flat_{U(1)}(T^n)\cong U(1)^n$.

> [!note]- Derivation
> **Apply the correspondence theorem.** By part (d) of the [[Thm - Flat Connections and Monodromy Representations of the Fundamental Group|monodromy correspondence]] — the assignment $[(P,\omega)]\mapsto[\rho_\omega]$ is a bijection $\mathcal M^\flat_G(M)\xrightarrow{\cong}\mathcal R(M;G)=\operatorname{Hom}(\pi_1(M,m),G)/\text{conjugation}$ — applied with $M=T^n$ and $G=U(1)$,
> $$\mathcal M^\flat_{U(1)}(T^n)\;\cong\;\operatorname{Hom}(\pi_1(T^n),U(1))/\text{conjugation}\qquad\text{(correspondence theorem, part (d)).}$$
>
> **Delete conjugation.** The group $U(1)$ is abelian, so for any $g,h\in U(1)$ we have $ghg^{-1}=h$; hence a representation and each of its conjugates coincide, and the conjugation action on $\operatorname{Hom}(\pi_1(T^n),U(1))$ is trivial. Therefore
> $$\operatorname{Hom}(\pi_1(T^n),U(1))/\text{conjugation}\;=\;\operatorname{Hom}(\pi_1(T^n),U(1))\qquad\text{($U(1)$ abelian).}$$
>
> **Insert $\pi_1(T^n)=\mathbb Z^n$.** Inside the [[Thm - The Moduli Space of Flat Connections with Compact Structure Group is Compact|compactness theorem]] it is proved that $\pi_1(T^n,m)\cong\mathbb Z^n$, using $\pi_1(S^1)\cong\mathbb Z$ (the [[Thm - Pi_1 of S^1 is Z|circle computation]]), the product formula $\pi_1(X\times Y)\cong\pi_1(X)\times\pi_1(Y)$, and $T^n=(S^1)^n$; the generators are the classes $[\gamma_1],\dots,[\gamma_n]$ of the coordinate loops (compare the base case $n=2$, [[Ex - Pi_1 of the Torus is Z Squared|π₁(T²) ≅ ℤ²]], giving $\pi_1(T^2)\cong\mathbb Z^2$). Thus
> $$\mathcal M^\flat_{U(1)}(T^n)\;\cong\;\operatorname{Hom}(\mathbb Z^n,U(1))\qquad\text{(previous two lines and }\pi_1(T^n)\cong\mathbb Z^n\text{).}$$
>
> **Count homomorphisms out of a free abelian group.** The group $\mathbb Z^n$ is free abelian on the standard basis $e_1,\dots,e_n$: every $m\in\mathbb Z^n$ is uniquely $m=\sum_j m_j e_j$ with $m_j\in\mathbb Z$. A homomorphism $\rho\colon\mathbb Z^n\to U(1)$ is therefore determined by its values $z_j:=\rho(e_j)\in U(1)$ via $\rho(m)=\prod_j z_j^{m_j}$; conversely, for *any* choice $(z_1,\dots,z_n)\in U(1)^n$ the formula $\rho(m):=\prod_j z_j^{m_j}$ is a homomorphism, because $U(1)$ is abelian so exponents add: $\rho(m+m')=\prod_j z_j^{m_j+m_j'}=\rho(m)\rho(m')$. Hence evaluation on generators is a bijection
> $$\operatorname{Hom}(\mathbb Z^n,U(1))\;\xrightarrow{\ \cong\ }\;U(1)^n,\qquad \rho\mapsto(\rho(e_1),\dots,\rho(e_n))\qquad\text{(universal property of the free abelian group).}$$
> Combining the displayed lines, $\mathcal M^\flat_{U(1)}(T^n)\cong U(1)^n$. This is route 1.

**Step 2: Route 2, part (a) — flatness on the trivial bundle is closedness of the form.**

On the trivial bundle $T^n\times U(1)$ a connection is a one-form $A=i\omega$ with $\omega\in\Omega^1(T^n;\mathbb R)$, and $A$ is flat if and only if $\omega$ is closed.

> [!note]- Derivation
> A connection on the trivial principal $U(1)$-bundle $T^n\times U(1)$ is recorded by its local connection form in the global product section, a single $A\in\Omega^1(T^n;\mathfrak u(1))$; writing $\mathfrak u(1)=i\mathbb R$, put $A=i\omega$ with $\omega\in\Omega^1(T^n;\mathbb R)$. By the series convention for a principal connection with abelian structure group, its curvature is $F_A=dA+\tfrac12[A\wedge A]$, and the bracket term vanishes because $\mathfrak u(1)$ is abelian, $[A\wedge A]=0$; hence
> $$F_A=dA=i\,d\omega\qquad\text{($\mathfrak u(1)$ abelian, so }[A\wedge A]=0\text{).}$$
> By the [[Def - Flat Connection|definition of flatness]], $A$ is flat if and only if $F_A=0$, i.e. $i\,d\omega=0$, i.e.
> $$d\omega=0\qquad\text{($\omega$ is a closed real one-form).}$$
> So the flat connections on the trivial bundle are exactly $A=i\omega$ with $\omega$ closed.

**Step 3: Route 2, part (b) — every closed form is small-gauge-equivalent to a unique constant-coefficient form.**

Every closed $\omega$ is cohomologous, through the differential of a single-valued function, to the constant-coefficient form $\bar\omega=\sum_j c_j\,dx^j$ with $c_j=\tfrac1{2\pi}\oint_{\gamma_j}\omega$; consequently $A=i\omega$ is gauge equivalent to the constant connection $A_c=i\sum_j c_j\,dx^j$.

> [!note]- Derivation
> Write $\omega=\sum_{j=1}^n f_j\,dx^j$ with $f_j\in C^\infty(T^n;\mathbb R)$, and let $\bar\omega=\sum_j c_j\,dx^j$ be its **average over the torus**,
> $$c_j:=\frac1{(2\pi)^n}\int_{T^n} f_j\;dx^1\cdots dx^n\qquad\text{(a constant, so }\bar\omega\text{ has constant coefficients).}$$
>
> **Identify the average with the periods.** Fix $j$. Because $\omega$ is closed, its integral over the loop $\gamma_j$ based at a point $p'$ (with the other coordinates held at $p'$) is independent of $p'$: two such loops are homotopic and $\oint$ of a closed form is a homotopy invariant (by [[Thm - Stokes' Theorem on Manifolds|Stokes' theorem]], $\int_{\partial\Sigma}\omega=\int_\Sigma d\omega=0$ over the connecting cylinder $\Sigma$ swept out between them). Hence $\oint_{\gamma_j}\omega=\int_0^{2\pi}f_j\,dx^j$ takes the same value for every choice of the remaining coordinates, and averaging that constant over the remaining $T^{n-1}$ changes nothing:
> $$\oint_{\gamma_j}\omega=\frac1{(2\pi)^{n-1}}\int_{T^{n-1}}\!\Big(\int_0^{2\pi}f_j\,dx^j\Big)\,dx'=\frac1{(2\pi)^{n-1}}\int_{T^n}f_j\;dx^1\cdots dx^n=2\pi c_j\qquad\text{(Fubini; }dx'\text{ the remaining coordinates).}$$
> Thus $c_j=\tfrac1{2\pi}\oint_{\gamma_j}\omega$.
>
> **The remainder is exact.** The form $\eta:=\omega-\bar\omega$ is closed (a difference of closed forms; $d\bar\omega=0$ since $\bar\omega$ has constant coefficients). Pull it back along the universal covering $q\colon\mathbb R^n\to T^n$, $q(x)=x\bmod(2\pi\mathbb Z)^n$, to $\tilde\eta:=q^*\eta$, a closed one-form on $\mathbb R^n$. Since $\mathbb R^n$ is simply connected, by the [[Thm - A Closed 1-Form on a Simply Connected Manifold is Exact|simply-connected exactness theorem]] — a closed one-form on a simply connected manifold is exact — there is $\tilde\varphi\in C^\infty(\mathbb R^n;\mathbb R)$ with
> $$d\tilde\varphi=\tilde\eta\qquad\text{(closed form on simply connected }\mathbb R^n\text{ is exact).}$$
> Normalise $\tilde\varphi(0)=0$; then $\tilde\varphi(x)=\int_0^1\tilde\eta\big(\tfrac{d}{dt}(tx)\big)\,dt=\int_0^1\tilde\eta_{tx}(x)\,dt$ along the straight segment.
>
> **The primitive descends to the torus.** For a lattice vector $v=2\pi\sum_j k_j e_j$ ($k\in\mathbb Z^n$) and any $x\in\mathbb R^n$,
> $$\tilde\varphi(x+v)-\tilde\varphi(x)=\int_{[x,\,x+v]}\tilde\eta=\int_{q\circ[x,\,x+v]}\eta=\sum_j k_j\oint_{\gamma_j}\eta\qquad\text{(}d\tilde\varphi=\tilde\eta\text{; }q\text{ maps the segment to a concatenation of the loops }\gamma_j\text{).}$$
> Each period vanishes: $\oint_{\gamma_j}\eta=\oint_{\gamma_j}\omega-\oint_{\gamma_j}\bar\omega=2\pi c_j-c_j\!\oint_{\gamma_j}dx^j=2\pi c_j-c_j\cdot2\pi=0$ (previous step and $\oint_{\gamma_j}dx^k=2\pi\delta_{jk}$). Hence $\tilde\varphi(x+v)=\tilde\varphi(x)$ for all lattice $v$, so $\tilde\varphi$ is $(2\pi\mathbb Z)^n$-periodic and descends to a genuine function $\varphi\in C^\infty(T^n;\mathbb R)$ with $d\varphi=\eta=\omega-\bar\omega$.
>
> **Absorb the remainder into a small gauge transformation.** Let $g:=e^{-i\varphi}\in C^\infty(T^n,U(1))$, a well-defined gauge transformation because $\varphi$ is single-valued on $T^n$. Then $g^{-1}\,dg=e^{i\varphi}\,d\big(e^{-i\varphi}\big)=-i\,d\varphi$, so
> $$A+g^{-1}\,dg=i\omega-i\,d\varphi=i(\omega-\eta)=i\bar\omega=i\sum_j c_j\,dx^j=A_c\qquad\text{(}\eta=d\varphi\text{).}$$
> Therefore $A=i\omega$ is gauge equivalent to the constant connection $A_c$, with $c_j=\tfrac1{2\pi}\oint_{\gamma_j}\omega$.

**Step 4: Route 2, part (c) — constant connections modulo large gauge give $(\mathbb R/\mathbb Z)^n$.**

Two constant connections $A_a=i\sum_j a_j\,dx^j$ and $A_{a'}=i\sum_j a'_j\,dx^j$ are gauge equivalent if and only if $a_j-a'_j\in\mathbb Z$ for every $j$; hence the constant connections modulo gauge form $(\mathbb R/\mathbb Z)^n\cong U(1)^n$.

> [!note]- Derivation
> **Large gauge transformations shift the parameters by integers.** For $k\in\mathbb Z^n$ define $g_k(x):=e^{i\,k\cdot x}=e^{i\sum_j k_j x^j}$. This is well defined on $T^n$: shifting a coordinate $x^j$ by its period $2\pi$ multiplies $g_k$ by $e^{2\pi i k_j}=1$. Its logarithmic derivative is
> $$g_k^{-1}\,dg_k=d(i\,k\cdot x)=i\sum_j k_j\,dx^j\qquad\text{(}k_j\text{ constant).}$$
> Hence $A_a+g_k^{-1}\,dg_k=i\sum_j(a_j+k_j)\,dx^j=A_{a+k}$, so $A_a$ and $A_{a+k}$ are gauge equivalent for every $k\in\mathbb Z^n$. This proves the "if" direction: $a-a'\in\mathbb Z^n\Rightarrow A_a\sim A_{a'}$.
>
> **The parameters modulo $\mathbb Z$ are a gauge invariant.** For the converse, use that the monodromy is gauge invariant. By the [[Thm - Holonomy of an Abelian Connection is the Exponential of the Curvature Integral|abelian-holonomy theorem]], the holonomy of $A_a$ around $\gamma_j$ is
> $$\operatorname{hol}_{A_a}(\gamma_j)=\exp\!\Big(-\oint_{\gamma_j}A_a\Big)=\exp\!\Big(-i\sum_k a_k\oint_{\gamma_j}dx^k\Big)=\exp\big(-i\,a_j\cdot2\pi\big)=e^{-2\pi i a_j}\qquad\text{(}\oint_{\gamma_j}dx^k=2\pi\delta_{jk}\text{).}$$
> For $U(1)$ the monodromy representation $\rho_{A_a}\colon\pi_1(T^n)\to U(1)$, $\rho_{A_a}([\gamma_j])=\operatorname{hol}_{A_a}(\gamma_j)=e^{-2\pi i a_j}$, is unchanged under gauge transformations: by part (c) of the [[Thm - Flat Connections and Monodromy Representations of the Fundamental Group|monodromy correspondence]] gauge-equivalent connections have conjugate monodromy, and conjugation is trivial in the abelian group $U(1)$, so *equal* monodromy. Therefore $A_a\sim A_{a'}$ forces $e^{-2\pi i a_j}=e^{-2\pi i a'_j}$ for every $j$, i.e. $a_j-a'_j\in\mathbb Z$. This is the "only if" direction.
>
> **Assemble the quotient.** Combining the two directions, $A_a\sim A_{a'}\iff a-a'\in\mathbb Z^n$, so the map $a\mapsto[A_a]$ descends to a bijection
> $$(\mathbb R/\mathbb Z)^n\;\xrightarrow{\ \cong\ }\;\{\text{constant connections}\}/\text{gauge},\qquad a\bmod\mathbb Z^n\mapsto[A_a],$$
> and $(\mathbb R/\mathbb Z)^n\cong U(1)^n$ through $a_j\bmod\mathbb Z\mapsto e^{-2\pi i a_j}$ (a group isomorphism $\mathbb R/\mathbb Z\to U(1)$). Together with Steps 2 and 3 — every flat connection on the trivial bundle is gauge equivalent to some $A_c$ — this shows the flat connections on $T^n\times U(1)$ modulo gauge form $U(1)^n$. This is route 2.

**Step 5: The two identifications agree, and every flat $U(1)$-bundle over $T^n$ is trivial.**

The point of $U(1)^n$ that route 1 assigns to a flat connection and the point that route 2 assigns to it are the same, and consequently the direct computation on the trivial bundle already sees the whole moduli space.

> [!note]- Derivation
> **Match the coordinates.** Route 1 assigns to a flat connection the tuple of monodromies $(\rho_\omega([\gamma_1]),\dots,\rho_\omega([\gamma_n]))\in U(1)^n$. Route 2 assigns to the representative $A_a$ the tuple $(a_1\bmod\mathbb Z,\dots,a_n\bmod\mathbb Z)\in(\mathbb R/\mathbb Z)^n$, identified with $U(1)^n$ by $a_j\mapsto e^{-2\pi i a_j}$. But Step 4 computed $\rho_{A_a}([\gamma_j])=e^{-2\pi i a_j}$. Hence the route-1 image of $A_a$ is exactly $(e^{-2\pi i a_1},\dots,e^{-2\pi i a_n})$, which is the image of $(a_j\bmod\mathbb Z)_j$ under the route-2 identification. The two maps $\mathcal M^\flat_{U(1)}(T^n)\to U(1)^n$ therefore coincide.
>
> **Every flat $U(1)$-bundle over $T^n$ is trivial.** Route 1 describes the moduli space of *all* flat $U(1)$-bundles at once (part (d) of the correspondence ranges over all bundles), whereas Steps 2–4 describe only the flat connections on the *trivial* bundle; both give the same $U(1)^n$, and Step 4 exhibits, for every value $(e^{-2\pi i a_j})_j\in U(1)^n$, a flat connection $A_a$ on the trivial bundle realising it. Thus every isomorphism class of flat $U(1)$-bundle over $T^n$ has a representative on the trivial bundle, i.e. every flat $U(1)$-bundle over $T^n$ is trivial. (This recovers, without invoking the bundle classification, that a flat $U(1)$-bundle over the torus — whose real first Chern class $[\tfrac{i}{2\pi}F]$ vanishes — is genuinely trivial, the torsion-free-ness of the situation being supplied here by the explicit realisation rather than assumed.)

> [!note]- Complete formal solution
> **Claim.** $\mathcal M^\flat_{U(1)}(T^n)\cong U(1)^n$, via the monodromy correspondence and via constant connections, and the two identifications coincide.
>
> *Route 1.* By part (d) of the monodromy correspondence, $\mathcal M^\flat_{U(1)}(T^n)\cong\operatorname{Hom}(\pi_1(T^n),U(1))/\text{conj}$. Since $U(1)$ is abelian, conjugation is trivial, so the quotient is $\operatorname{Hom}(\pi_1(T^n),U(1))$. As $\pi_1(T^n)\cong\mathbb Z^n$ (from $\pi_1(S^1)\cong\mathbb Z$ and the product formula, proved in the compactness theorem), and $\mathbb Z^n$ is free abelian, evaluation on the standard generators is a bijection $\operatorname{Hom}(\mathbb Z^n,U(1))\xrightarrow{\cong}U(1)^n$. Hence $\mathcal M^\flat_{U(1)}(T^n)\cong U(1)^n$.
>
> *Route 2.* On $T^n\times U(1)$ a connection is $A=i\omega$, $\omega\in\Omega^1(T^n;\mathbb R)$, with curvature $F_A=dA=i\,d\omega$ (the bracket term vanishes as $\mathfrak u(1)$ is abelian); so $A$ is flat iff $\omega$ is closed. Given closed $\omega=\sum_j f_j\,dx^j$, set $c_j=\tfrac1{(2\pi)^n}\int_{T^n}f_j=\tfrac1{2\pi}\oint_{\gamma_j}\omega$ and $\bar\omega=\sum_j c_j\,dx^j$. The closed form $\eta=\omega-\bar\omega$ has all periods zero, so its pullback to $\mathbb R^n$ is $d\tilde\varphi$ with $\tilde\varphi$ $(2\pi\mathbb Z)^n$-periodic (the lattice increments of $\tilde\varphi$ are the vanishing periods of $\eta$); $\tilde\varphi$ descends to $\varphi\in C^\infty(T^n;\mathbb R)$, and $g=e^{-i\varphi}$ gauges $A$ to $A_c=i\sum_j c_j\,dx^j$. Two constant connections $A_a,A_{a'}$ satisfy $A_a\sim A_{a'}$ iff $a-a'\in\mathbb Z^n$: the large gauge transformation $g_k(x)=e^{i\,k\cdot x}$ ($k\in\mathbb Z^n$, well defined on $T^n$) gives $g_k^{-1}dg_k=i\sum_j k_j\,dx^j$, whence $A_{a}\sim A_{a+k}$; conversely $\operatorname{hol}_{A_a}(\gamma_j)=\exp(-\oint_{\gamma_j}A_a)=e^{-2\pi i a_j}$ is a gauge invariant (equal, not merely conjugate, monodromy in abelian $U(1)$), forcing $a_j\equiv a'_j\pmod{\mathbb Z}$. Thus the flat connections on $T^n\times U(1)$ modulo gauge are $(\mathbb R/\mathbb Z)^n\cong U(1)^n$ via $a_j\mapsto e^{-2\pi i a_j}$.
>
> *Agreement and triviality.* The monodromy of $A_a$ is $([\gamma_j]\mapsto e^{-2\pi i a_j})$, which is exactly the route-1 image of $A_a$ and the image of $(a_j\bmod\mathbb Z)_j$ under the route-2 identification; so the two maps to $U(1)^n$ are equal. Since the full moduli of all flat $U(1)$-bundles (route 1) equals the moduli of flat connections on the trivial bundle (route 2), and every value in $U(1)^n$ is realised by a constant connection on the trivial bundle, every flat $U(1)$-bundle over $T^n$ is trivial. $\blacksquare$

> [!warning] Illegal but tempting: forgetting the large gauge transformations
> One is tempted to stop route 2 at Step 3: "flat connections on the trivial bundle are $i\bar\omega$ with $\bar\omega\in H^1_{\mathrm{dR}}(T^n)\cong\mathbb R^n$, so the moduli space is $\mathbb R^n$." This is wrong. It uses only the *small* (connected-to-identity) gauge transformations $e^{i\varphi}$ with $\varphi$ single-valued, which act by exact shifts. The gauge group $C^\infty(T^n,U(1))$ is disconnected — its components are indexed by the winding numbers $(k_1,\dots,k_n)\in\mathbb Z^n=[T^n,U(1)]$ — and the non-identity components act by the integer shifts $a\mapsto a+k$. Only after quotienting by all of $C^\infty(T^n,U(1))$, not merely its identity component, does one get the correct compact answer $U(1)^n$. The extra condition that would make the naive computation legal is precisely restricting to the identity component of the gauge group, which computes the *based* or *framed* moduli space $\mathbb R^n$, a different object.

---

# Key Takeaways

**A moduli space of flat connections is computed twice — topologically and analytically — and the theorem is that the two computations agree.** The reusable principle is that $F=0$ modulo gauge always admits a *topological* description, as $\operatorname{Hom}(\pi_1,G)$ modulo conjugation, and, when a convenient slice exists, an *analytic* description as an explicit family of connections modulo gauge. The trigger for reaching for the topological side is the appearance of flatness together with a base whose fundamental group is understood; the trigger for the analytic side is a base with an explicit basis of harmonic forms (a flat torus, a Lie group, any symmetric space). The transferable diagnostic when the two answers seem to differ is to check that *both* halves of the gauge group have been used analytically: the identity component (small gauge, exact shifts) collapses a form to its cohomology class, and the component group (large gauge, integral shifts) then quotients the cohomology by the integer lattice. On the torus these produce $\mathbb R^n$ and then $\mathbb R^n/\mathbb Z^n$; forget the second and the analytic answer is non-compact while the topological answer is compact, which is the signal that a piece of the gauge group has been dropped.

**Abelian structure group is what makes everything explicit, and it does so through three separate simplifications that are worth naming individually.** First, conjugation becomes trivial, so the representation *variety* $\operatorname{Hom}(\pi_1,G)/\text{conj}$ is just the character group $\operatorname{Hom}(\pi_1,G)$ with no orbit space to analyse. Second, the curvature loses its quadratic term, $F_A=dA$, so flatness is the *linear* condition $d\omega=0$ and the whole moduli problem is linear algebra on forms plus a lattice quotient. Third, holonomy becomes the genuine exponential of a line integral, $\operatorname{hol}(c)=\exp(-\oint_c A)$, so the monodromy of an explicit connection can be read off in closed form. The trigger to expect all three is simply "$G$ abelian" — most often $G=U(1)$ in electromagnetism and $G=T$ a torus in the study of line bundles and their moduli; the moment $G$ is non-abelian (already $SU(2)$) all three simplifications fail and one is in the world of genuine representation varieties with singular quotients, as the companion exercise [[Ex - Representation Varieties of Surface Groups]] shows.

**The winding numbers of gauge transformations are the arithmetic that compactifies a moduli space, and this is the first appearance of a mechanism that recurs throughout gauge theory.** Here the components of $\mathcal G=C^\infty(T^n,U(1))$ are labelled by an integer vector, the winding number, and the non-trivial components implement exactly the integer shifts $a\mapsto a+k$ that fold the real parameters $\mathbb R^n$ into the compact torus $(\mathbb R/\mathbb Z)^n$. The general lesson for spaced practice: whenever a naive count of solutions modulo the *connected* gauge group gives a linear (vector-space) answer, the correct answer is usually that vector space modulo a lattice coming from $\pi_0$ of the full gauge group, and that lattice is read off as the periods of $g^{-1}dg$ over a generating set of loops. The same bookkeeping controls the large gauge transformations of non-abelian Yang–Mills theory, where $\pi_0$ or $\pi_3$ of the gauge group produces the instanton number and the $\theta$-angle; the torus is the toy model in which the entire mechanism is visible in one line, $g_k(x)=e^{i\,k\cdot x}$. If this exercise is revisited after a gap, the single fact to reconstruct first is that the answer is compact *because* the gauge group is disconnected, and the connecting object is the winding number.
