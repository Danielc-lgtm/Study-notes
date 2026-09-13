# Pass 1 content map — Andriy Haydys, *Introduction to Gauge Theory* (PCMI 2019 lecture notes, version 26 April 2024)

Source: `haydys.txt` (plain-text extraction of the 73-page PDF). PDF page numbers below are the *PDF* page numbers (PDF page $N$ = printed page $N$; the title page is PDF page 1).

**Numbering scheme.** Items are numbered by *top-level section* (1, 2.1, 2.2, 2.3, 2.4, 3.1, 3.2, 3.3, 4.1, …, 7.2) with a running index inside that section, so that a citation is unambiguous regardless of the subsection: `D2.1.7` = 7th definition listed under §2.1 (it may live in subsection 2.1.4). Prefixes: `D` definition, `T` theorem/proposition/lemma/corollary, `E` example, `X` exercise, `R` remark / load-bearing paragraph, `I` external result imported without proof. The source's own item numbers (Definition 1, Theorem 11, Exercise 25, …) are given in parentheses after every item; the source numbers all environments in one global sequence 1–230.

**Global standing conventions (stated once, used throughout).**
- Groups act on configuration spaces **on the right**; representation spaces $V$ are **left** $G$-modules; equivariance of a map $F\colon C\to V$ means $F(a\cdot g)=g^{-1}\cdot F(a)$ (p. 3).
- Principal bundles: $G$ acts on $P$ **on the right**, freely and transitively on fibres (Definition 23, p. 11).
- Associated bundle: $(p,v)\cdot g=(p\cdot g,\rho(g^{-1})v)$, $P\times_\rho V=(P\times V)/G$ (p. 14).
- Equivariant $V$-valued form on $P$: $R_g^*\omega=\rho(g^{-1})\omega$ (Definition 38, p. 16).
- Connection matrix on a vector bundle: $\nabla e=e\cdot A$; locally $\nabla=d+A$; change of frame $e'=eg$ gives $A'=g^{-1}Ag+g^{-1}dg$ (p. 8).
- Curvature: $F_\nabla=dA+A\wedge A=dA+\tfrac12[A\wedge A]$ (no $\tfrac12$ in the matrix form, $\tfrac12$ in the Lie-bracket form) (p. 10). On principal bundles $\pi^*F_a=da+\tfrac12[a\wedge a]$ (p. 19). Bianchi identity $d^{\nabla_a}F_a=0$, equivalently $d\hat F_A=[\hat F_A\wedge A]$ (pp. 20–21).
- Gauge group of a vector bundle acts on connections by $\nabla^g s:=g^{-1}\nabla(gs)$, a **right** action; on principal bundles $a\cdot\psi:=\psi^*a$ (pp. 10, 22).
- Clifford relation: $u\cdot u=-|u|^2$ (p. 35). Dirac operator $D s=\sum_i e_i\cdot\nabla_{e_i}s$ (p. 37).
- Laplacians are **non-negative**: $\Delta=-\sum\partial_i^2$ on $\mathbb R^n$, $\Delta f=-{*}d{*}df$ (Laplace–Beltrami), $\nabla^*\nabla$ with $\nabla^*=-{*}d^\nabla{*}$, Hodge Laplacian $dd^*+d^*d$ (pp. 41–42, 47, 52).
- Sobolev spaces are written $W^{k,p}$ (completion of $C_0^\infty$ in $\|u\|_{W^{k,p}}=(\sum_{i\le k}\|\nabla^iu\|_{L^p}^p)^{1/p}$) (pp. 44–45).
- Chern classes: $c_1(P):=-f^*a$, $c_2(P):=-f^*b$ (topological definitions, sign is a convention, pp. 25–26); $c_j$ via $\det(\lambda\mathbf 1+\tfrac{i}{2\pi}\xi)$ (Chern–Weil, p. 27); for a line bundle $c_1$ is represented by $\tfrac{i}{2\pi}F_A$ (p. 65).
- Seiberg–Witten equations: $\slashed D_A^+\psi=0$, $F_A^+=\mu(\psi)$ with $\mu(\psi)=\psi\psi^*-\tfrac12|\psi|^2$ (p. 61). Gauge action $A\cdot g=A+2g^{-1}dg$, $(\psi,A)\cdot g=(\bar g\psi,A\cdot g)$ (p. 62). Sobolev choice $(k,p)=(5,2)$: configurations in $W^{5,2}$, gauge group $\mathcal G^{6,2}$ (p. 64).

---

## 1 Introduction

`PDF pages: 2–4`

### Standing conventions and notation
- $G$ a Lie group acting **on the right** on a manifold $C$ (the "configuration space"); the author remarks the side is nonessential but he follows the right-action convention throughout (p. 2).
- $\mathcal B:=C/G$; $C^{\mathrm{irr}}\subset C$ the subspace of points with trivial stabiliser; $\mathcal B^{\mathrm{irr}}:=C^{\mathrm{irr}}/G$, assumed to be a manifold (p. 3).
- $V$ a $G$-representation viewed as a **left** $G$-module; $F\colon C\to V$ smooth and $G$-equivariant meaning $F(a\cdot g)=g^{-1}\cdot F(a)$ (p. 3).
- Footnote 1: "ideally one wishes the quotient to be a smooth manifold" (p. 3).

### Definitions
- **D1.1 — Irreducible locus** (unlabelled, p. 3). $C^{\mathrm{irr}}:=\{a\in C\mid \mathrm{Stab}_G(a)=\{1\}\}$; $G$ acts on $C^{\mathrm{irr}}$ and $\mathcal B^{\mathrm{irr}}:=C^{\mathrm{irr}}/G$.
- **D1.2 — Moduli space (abstract scheme)** (unlabelled, p. 3). Assuming $0\in V$ is a regular value of $F$, $\mathcal M^{\mathrm{irr}}:=\big(F^{-1}(0)\cap C^{\mathrm{irr}}\big)/G\subset\mathcal B^{\mathrm{irr}}$ is a submanifold; assume $d:=\dim\mathcal M^{\mathrm{irr}}<\infty$. If $\mathcal M^{\mathrm{irr}}$ is compact and oriented it has a fundamental class $[\mathcal M^{\mathrm{irr}}]\in H_d(\mathcal B^{\mathrm{irr}};\mathbb Z)$, and for $\eta\in H^d(\mathcal B^{\mathrm{irr}};\mathbb Z)$ the integer $\langle[\mathcal M^{\mathrm{irr}}],\eta\rangle=\int_{\mathcal M^{\mathrm{irr}}}\eta$ ($\eta$ thought of as a closed $d$-form) is "the invariant".
- **D1.3 — Framed moduli space (abstract scheme)** (unlabelled, p. 3). Given a normal subgroup $G_0\subset G$ with $\bar G:=G/G_0$ a Lie group, $\hat{\mathcal M}^{\mathrm{irr}}:=\big(F^{-1}(0)\cap C^{\mathrm{irr}}\big)/G_0$ carries an action of $\bar G$ with $\hat{\mathcal M}^{\mathrm{irr}}/\bar G=\mathcal M^{\mathrm{irr}}$, so $\hat{\mathcal M}^{\mathrm{irr}}\to\mathcal M^{\mathrm{irr}}$ is a principal $\bar G$-bundle whose characteristic classes yield cohomology classes on $\mathcal B^{\mathrm{irr}}$ (details deferred to Section 3).

### Theorems: none.
### Examples: none.
### Exercises: none.

### Remarks / load-bearing paragraphs
- **R1.1 — The basic scheme** (pp. 2–3). Invariants of manifolds via gauge theory: quotient $C/G$ may fail to be nice due to nontrivial stabilisers; restrict to $C^{\mathrm{irr}}$; the equivariant map $F$ cuts out $\mathcal M^{\mathrm{irr}}$; pair its fundamental class with cohomology classes of $\mathcal B^{\mathrm{irr}}$; the classes come from the framed moduli space viewed as a principal bundle.
- **R1.2 — Why other gauge theories** (pp. 3–4). Seiberg–Witten theory does not generalise to higher dimensions, whereas anti-self-duality equations do; non-abelian groups ($SL(2,\mathbb C)$, $SU(2)$) give insight SW cannot; Kapustin–Witten equations in Witten's approach to the Jones polynomial.
- **R1.3 — Organisation and scope** (p. 4). §§2–4: properties of "points" of $C$; §§5–6: analytic tools (properties of $F$ abstractly), not specific to gauge theory; §7: Seiberg–Witten. PDE facts stated but not proved; references [Eva10, Wel80]. Monographs cited: [Mor96, Moo96, DK90, FU91, Don02, KM07]; presentation close to [Mor96, DK90]; the compactness proof for SW moduli space is claimed to be "streamlined somewhat".

### External results imported without proof: none (only literature pointers).

---

## 2.1 Vector bundles

`PDF pages: 4–11`

### Standing conventions and notation (whole of §2.1)
- Vector bundles are **real, smooth**, of rank $k$; the triple is written $(\pi,E,M)$ (Definition 1). $E_m:=\pi^{-1}(m)$. Terminology: total space $E$, base $M$, projection $\pi$, local trivialisation $\psi_U$ (p. 5).
- $\Gamma(E)=\Gamma(M;E)$ smooth sections; $\Gamma(U;E)$ sections over $U$; $\Gamma(E)$ is a $C^\infty(M)$-module (p. 6).
- A local trivialisation over $U$ is identified with a local frame $e=(e_1,\dots,e_k)$, $\psi_U^{-1}(m,x)=e(m)\cdot x$ (Exercise 5). A frame is "a pointwise base"; $e(m)\cdot x$ means $\sum_j x_je_j(m)$ (p. 6).
- Local representation of a section: $s=e\sigma=\sum_j\sigma_je_j$, $\sigma\colon U\to\mathbb R^k$. Change of frame: $e=e'\cdot g$ with $g\colon U\cap U'\to GL_k(\mathbb R)$ (the source writes $GL_n(\mathbb R)$, a typo for $GL_k$), equation (6); then $\sigma'=g\sigma$ (p. 6).
- Covariant derivative $\nabla\colon\Gamma(E)\to\Gamma(T^*M\otimes E)$ (Definition 8); "connection" and "covariant derivative" are used interchangeably; $\mathcal A(E)$ denotes the space of all connections on $E$ (p. 7).
- $\Omega^p(E):=\Gamma(\Lambda^pT^*M\otimes E)$; $\Omega^1(\operatorname{End}E)=\Gamma(T^*M\otimes\operatorname{End}E)$ (pp. 7–8).
- Connection matrix: $\nabla e=e\cdot A$, $A=A(\nabla,e)\in\Omega^1(U;\mathfrak{gl}_k(\mathbb R))$ a $k\times k$ matrix of 1-forms, equation (13); locally $\nabla=d+A$ meaning $\nabla s$ has local representation $d\sigma+A\sigma$ (p. 8).
- Frame change $e'=eg$: $A'=g^{-1}Ag+g^{-1}dg$, equation (14) (p. 8).
- Extension $d^\nabla\colon\Omega^p(E)\to\Omega^{p+1}(E)$, $d^\nabla(\omega\otimes s):=d\omega\otimes s+(-1)^p\omega\wedge\nabla s$ (p. 8).
- Curvature: $d^\nabla\circ d^\nabla=F_\nabla$, $F_\nabla\in\Omega^2(\operatorname{End}E)$; locally $F_\nabla=dA+A\wedge A$ (18) $=dA+\tfrac12[A\wedge A]$ (20) where $[A\wedge A]$ combines wedge and Lie bracket (pp. 9–10).
- Directional covariant derivative $\nabla_vs:=\iota_v\nabla s$; partial covariant derivatives $\nabla_is:=\nabla_{\partial_i}s$; $\nabla s=\sum_i dx_i\otimes\nabla_is$ (p. 9). Curvature measures $F_\nabla(\partial_i,\partial_j)=\nabla_i\nabla_j-\nabla_j\nabla_i$ (p. 10).
- Gauge group $\mathcal G=\mathcal G(E):=\{g\in\Gamma(\operatorname{End}E)\mid g(m)\in GL(E_m)\ \forall m\}$ with the $C^\infty$ topology; required to preserve any extra structure (orientation, scalar product); action $\nabla^gs:=g^{-1}\nabla(gs)$ is a **right** action (p. 10).

### 2.1.1 Basic notions — `PDF pages: 4–5`

#### Definitions
- **D2.1.1 — Real smooth vector bundle of rank $k$** (Definition 1, p. 4). Choose a non-negative integer $k$. A real smooth vector bundle of rank $k$ is a triple $(\pi,E,M)$ such that: (i) $E$ and $M$ are smooth manifolds and $\pi\colon E\to M$ is a smooth submersion (differential surjective at each point); (ii) for each $m\in M$ the fibre $E_m:=\pi^{-1}(m)$ has the structure of a vector space and $E_m\cong\mathbb R^k$; (iii) for each $m\in M$ there is a neighbourhood $U\ni m$ and a smooth map $\psi_U\colon\pi^{-1}(U)\to U\times\mathbb R^k$ such that $\mathrm{pr}_1\circ\psi_U=\pi$ on $\pi^{-1}(U)$ and $\psi_U$ is a fibrewise linear isomorphism. Terminology: $E$ total space, $M$ base, $\pi$ projection, $\psi_U$ local trivialisation over $U$.
- **D2.1.2 — Homomorphism of vector bundles; isomorphic bundles; trivial bundle** (unlabelled, p. 5). For $E,F$ over a common base $M$, a homomorphism is a smooth map $\phi\colon E\to F$ with $\pi_F\circ\phi=\pi_E$ that is fibrewise linear. $E$ and $F$ are isomorphic if there is a homomorphism which is fibrewise an isomorphism. $E$ is trivial if it is isomorphic to the product bundle $M\times\mathbb R^k$.

#### Theorems: none.

#### Examples
- **E2.1.1** (Example 1, p. 5). (a) The product bundle $M\times\mathbb R^k$; (b) the tangent bundle $TM$ of any smooth manifold $M$.

#### Exercises: none in 2.1.1.
#### Remarks: 
- **R2.1.1 — Informal description** (p. 4): a vector bundle is a family of vector spaces parametrised by points of a manifold (or topological space).

### 2.1.2 Operations on vector bundles — `PDF page: 5`

#### Definitions
- **D2.1.3 — Algebraic operations on vector bundles** (unlabelled, p. 5). For $E,F$ over $M$: $(E^*)_m:=(E_m)^*$; $(\Lambda^pE)_m:=\Lambda^p(E_m)$; $(E\oplus F)_m:=E_m\oplus F_m$; $(E\otimes F)_m:=E_m\otimes F_m$; $\operatorname{Hom}(E,F)_m:=\operatorname{Hom}(E_m,F_m)$.
- **D2.1.4 — Pull-back bundle and restriction** (unlabelled, p. 5). For smooth $f\colon M'\to M$, $(f^*E)_{m'}:=E_{f(m')}$. If $M'\subset M$ is open and $\iota$ the inclusion, $E|_{M'}:=\iota^*E$ is the restriction.

#### Theorems: none.
#### Examples: none.

#### Exercises
- **X2.1.1** (Exercise 2, p. 5). Prove that $E^*\otimes F$ is isomorphic to $\operatorname{Hom}(E,F)$.
- **X2.1.2** (Exercise 3, p. 5). Prove that the tangent bundle of the 2-sphere is non-trivial. (Hint: apply the hairy ball theorem.)

#### Remarks
- **R2.1.2** (p. 5). "The reader should check that the families of vector spaces defined above satisfy the properties required by Definition 1" — i.e. local triviality of $E^*$, $\Lambda^pE$, $E\oplus F$, $E\otimes F$, $\operatorname{Hom}(E,F)$, $f^*E$ is left unverified.

### 2.1.3 Sections — `PDF page: 6`

#### Definitions
- **D2.1.5 — Section** (Definition 4, p. 6). A smooth map $s\colon M\to E$ is called a section if $\pi\circ s=\mathrm{id}_M$. Equivalently $s$ assigns to each $m$ a vector $s(m)\in E_m$ depending smoothly on $m$. Sections of $TM$ are vector fields; sections of $\Lambda^pT^*M$ are differential $p$-forms. $\Gamma(E)=\Gamma(M;E)$ denotes the space of smooth sections; it is a vector space (pointwise operations) and a $C^\infty(M)$-module.
- **D2.1.6 — Local representation of a section; transition function** (unlabelled, p. 6). Given a local frame $e$ over $U$ and $s\in\Gamma(E)$, $s(m)=\sum_{j=1}^k\sigma_j(m)e_j(m)$ for functions $\sigma_j\colon U\to\mathbb R$; $\sigma\colon U\to\mathbb R^k$ is the local representation. If $e'$ is another local frame over $U'$, there is $g\colon U\cap U'\to GL_k(\mathbb R)$ with $e=e'\cdot g$ (equation (6)), and $s=e'\sigma'=eg^{-1}\sigma'=e\sigma$ gives $\sigma'=g\sigma$.

#### Theorems: none.

#### Examples
- **E2.1.2** (Example 2, p. 6). If $f$ is a smooth function on $M$, then $df$ is a 1-form. More generally, given $f_1,\dots,f_p$, $\omega:=df_1\wedge\dots\wedge df_p$ is a $p$-form.

#### Exercises
- **X2.1.3** (Exercise 5, p. 6). Let $E\to M$ be of rank $k$ and $U\subset M$ open. Prove that $E$ is trivial over $U$ if and only if there are $k$ sections $e=(e_1,\dots,e_k)$, $e_j\in\Gamma(U;E)$, such that $e(m)$ is a basis of $E_m$ for each $m\in U$. More precisely, given $e$ show that $\psi_U$ can be constructed by $\psi_U^{-1}\colon U\times\mathbb R^k\to E|_U$, $(m,x)\mapsto e(m)\cdot x$. In fact this establishes a one-to-one correspondence between $k$-tuples of pointwise linearly independent sections and local trivialisations of $E$.

#### Remarks
- **R2.1.3 — Dependence of $\sigma$ on the frame** (p. 6). The computation $s=e'\sigma'=eg^{-1}\sigma'=e\sigma\Rightarrow\sigma'=g\sigma$ establishing how local representations transform.

### 2.1.4 Covariant derivatives — `PDF pages: 6–8`

#### Definitions
- **D2.1.7 — Covariant derivative (connection)** (Definition 8, p. 7). Let $E\to M$ be a vector bundle. A covariant derivative is an $\mathbb R$-linear map $\nabla\colon\Gamma(E)\to\Gamma(T^*M\otimes E)$ such that
$$\nabla(fs)=df\otimes s+f\nabla s\qquad(9)$$
holds for all $f\in C^\infty(M)$ and all $s\in\Gamma(E)$. (The source then uses the word *connection* synonymously; $\mathcal A(E)$ = space of all connections.)
- **D2.1.8 — Connection matrix** (unlabelled, equation (13), p. 8). For a local frame $e$ over $U$, $\nabla e=e\cdot A$ where $A=A(\nabla,e)$ is a $k\times k$ matrix of 1-forms on $U$; $A$ is the connection matrix of $\nabla$ with respect to $e$. For $s=e\sigma$: $\nabla s=\nabla(e)\sigma+e\otimes d\sigma=e(A\sigma+d\sigma)$, written "$\nabla=d+A$". $\nabla$ is uniquely determined over $U$ by $A$, and every $A\in\Omega^1(U;\mathfrak{gl}_k(\mathbb R))$ arises as a connection matrix.

#### Theorems
- **T2.1.1 — Space of connections is an affine space** (Theorem 11, p. 7). For any vector bundle $E\to M$ the space $\mathcal A(E)$ of all connections is an affine space modelled on $\Omega^1(\operatorname{End}E)=\Gamma(T^*M\otimes\operatorname{End}(E))$. Concretely: (a) $\mathcal A(E)\ne\varnothing$; (b) for any two connections $\nabla,\hat\nabla$ the difference $\nabla-\hat\nabla$ is a 1-form with values in $\operatorname{End}(E)$; (c) for any $\nabla\in\mathcal A(E)$ and $a\in\Omega^1(\operatorname{End}E)$, $(\nabla+a)s:=\nabla s+as$ is a connection.
  `Proof in source: full (modulo Lemma 12 and a cited partition-of-unity argument).` Strategy: (1) $\mathcal A(E)$ is convex: $t\nabla+(1-t)\hat\nabla$ is a connection for $t\in[0,1]$. (2) For a local trivialisation $\psi_U$, $\nabla_Us:=\psi_U^{-1}d(\psi_U(s))$ is a connection on $E|_U$. (3) Sew the local $\nabla_U$ with a partition of unity using convexity, "just like in the proof of the existence of Riemannian metrics", cf. [BT03, Thm 3.3.7]; this gives (a). (4) By (9), $\nabla-\hat\nabla$ is $C^\infty(M)$-linear, so (b) follows from Lemma 12. (5) (c) is "straightforward".
  `Gaps:` partition-of-unity sewing only indicated by analogy; (c) not written out; Lemma 12 left as exercise.
- **T2.1.2 — Tensoriality lemma ($C^\infty$-linear maps are given by bundle-valued forms)** (Lemma 12, p. 7). Let $A\colon\Gamma(E)\to\Omega^p(F)$ be an $\mathbb R$-linear map which is also $C^\infty(M)$-linear, i.e. $A(fs)=fA(s)$ for all $f\in C^\infty(M)$ and $s\in\Gamma(E)$. Then there exists $a\in\Omega^p(\operatorname{Hom}(E,F))$ such that $A(s)=a\cdot s$.
  `Proof in source: left as exercise.`

#### Examples
- **E2.1.3 — Projected connection on an embedded submanifold** (Example 10, p. 7). Let $M\subset\mathbb R^N$ be an embedded submanifold; $TM$ is a subbundle of the product bundle $\underline{\mathbb R^N}:=M\times\mathbb R^N$, so a section $s$ of $TM$ is a map $M\to\mathbb R^N$. Define $\nabla s:=\mathrm{pr}(ds)$, $\mathrm{pr}$ the orthogonal projection onto $TM$. "A straightforward computation shows that this satisfies the Leibniz rule", so $\nabla$ is a connection.

#### Exercises: none labelled (Lemma 12 is "left as an exercise").

#### Remarks / load-bearing paragraphs
- **R2.1.4 — Why the naive difference quotient fails** (pp. 6–7). Recall $df(v)=\lim_{t\to0}\frac{f(\gamma(t))-f(m)}t$, equation (7). For a section, $s(\gamma(t))-s(m)$ is ill-defined since the vectors lie in different fibres; hence derivatives of sections are defined axiomatically via the Leibniz rule.
- **R2.1.5 — Local form $\nabla=d+A$ and the transformation law (14)** (p. 8). Computation: $\nabla s=\nabla(e\sigma)=e(A\sigma+d\sigma)$. For $e'=eg$: $\nabla e'=\nabla(eg)=(\nabla e)g+e\otimes dg=e(Ag+dg)=e'(g^{-1}Ag+g^{-1}dg)$, hence
$$A'=g^{-1}Ag+g^{-1}dg.\qquad(14)$$

### 2.1.5 The curvature — `PDF pages: 8–10`

#### Definitions
- **D2.1.9 — Exterior covariant derivative $d^\nabla$** (unlabelled, p. 8). $\Omega^p(E):=\Gamma(\Lambda^pT^*M\otimes E)$. For $s\in\Gamma(E)$ and $\omega\in\Omega^p(M)$ declare $d^\nabla(\omega\otimes s):=d\omega\otimes s+(-1)^p\omega\wedge\nabla s$; this yields a unique $\mathbb R$-linear map $d^\nabla\colon\Omega^p(E)\to\Omega^{p+1}(E)$ satisfying the Leibniz rule $d^\nabla(\alpha\wedge\omega)=d\alpha\wedge\omega+(-1)^q\alpha\wedge d^\nabla\omega$ for $\alpha\in\Omega^q(M)$, $\omega\in\Omega^p(M;E)$. One obtains a sequence $0\to\Omega^0(E)\xrightarrow{d^\nabla=\nabla}\Omega^1(E)\xrightarrow{d^\nabla}\cdots\to\Omega^n(E)\to0$, $n=\dim M$, which unlike the de Rham sequence need not be a complex.
- **D2.1.10 — Curvature form of a connection on a vector bundle** (Definition 17, p. 9). The 2-form $F_\nabla\in\Omega^2(\operatorname{End}E)$ defined by $d^\nabla\circ d^\nabla=F_\nabla$ (16) is the curvature form of $\nabla$. Meaning: for any $\omega\in\Omega^p(E)$, $d^\nabla(d^\nabla\omega)=F_\nabla\wedge\omega$, the right side combining wedge product and the contraction $\operatorname{End}(E)\otimes E\to E$.
- **D2.1.11 — Directional and partial covariant derivatives** (unlabelled, p. 9). For $v\in T_mM$, $\nabla_vs:=\iota_v\nabla s$ is the covariant derivative of $s$ in direction $v$. In local coordinates $(x_1,\dots,x_n)$ with $\partial_i=\partial/\partial x_i$ the tangent vector of $\gamma(t)=(x^0_1,\dots,x^0_{i-1},t,x^0_{i+1},\dots,x^0_n)$, $\nabla_is:=\nabla_{\partial_i}s$ are "partial covariant derivatives", and $\nabla s=\sum_{i=1}^ndx_i\otimes\nabla_is$ (analogue of $df=\sum\frac{\partial f}{\partial x_i}dx_i$).

#### Theorems
- **T2.1.3 — Existence of the curvature form** (Proposition 15, p. 9). There is a 2-form $F_\nabla$ with values in $\operatorname{End}E$ such that $d^\nabla\circ d^\nabla=F_\nabla$ (16), i.e. $d^\nabla(d^\nabla\omega)=F_\nabla\wedge\omega$ for all $\omega\in\Omega^p(E)$.
  `Proof in source: full.` Strategy: For $p=0$, applying the Leibniz rule twice shows $d^\nabla\circ\nabla\colon\Omega^0(E)\to\Omega^2(E)$ is $C^\infty(M)$-linear, so Lemma 12 gives $F_\nabla$ with $d^\nabla(\nabla s)=F_\nabla s$. For $p>0$ and $\eta\in\Omega^p(M)$, $s\in\Gamma(E)$: $d^\nabla(d^\nabla(\eta\otimes s))=d^\nabla(d\eta\otimes s+(-1)^p\eta\wedge\nabla s)=0+(-1)^{p+1}d\eta\wedge\nabla s+(-1)^pd\eta\wedge\nabla s+(-1)^{2p}\eta\wedge d^\nabla(\nabla s)=\eta\wedge F_\nabla s=F_\nabla\wedge(\eta\otimes s)$, the last equality because $F_\nabla$ has even degree.
  `Gaps:` the two applications of the Leibniz rule for $p=0$ are not written out.
- **T2.1.4 — Curvature of a shifted connection** (Proposition 21, p. 10). If $a\in\Omega^1(\operatorname{End}E)$, then $F_{\nabla+a}=F_\nabla+d^\nabla a+a\wedge a$.
  `Proof in source: omitted ("Local expression (18) implies immediately").` Intended argument: locally $A\mapsto A+a$, and $d(A+a)+(A+a)\wedge(A+a)=dA+A\wedge A+(da+A\wedge a+a\wedge A)+a\wedge a$, where $da+A\wedge a+a\wedge A=d^\nabla a$ (the induced connection on $\operatorname{End}E$).

#### Examples: none.
#### Exercises: none labelled ("The reader is strongly encouraged to check" the transformation of $F$, see R2.1.8).

#### Remarks / load-bearing paragraphs
- **R2.1.6 — Curvature as failure of partial covariant derivatives to commute** (pp. 9–10). Computation: $d^\nabla(\nabla s)=-\sum_idx_i\wedge\nabla(\nabla_is)=-\sum_{i,j}dx_i\wedge dx_j\otimes\nabla_j(\nabla_is)=\sum_{i,j}dx_i\wedge dx_j\otimes\nabla_i(\nabla_js)$, whence $F_\nabla(\partial_i,\partial_j)=\nabla_i(\nabla_js)-\nabla_j(\nabla_is)$.
- **R2.1.7 — Local formula $F_\nabla=dA+A\wedge A$ (18)** (p. 10). With $\nabla e=eA$, $s=e\sigma$: $d^\nabla(\nabla(e\sigma))=d^\nabla(e(d\sigma+A\sigma))=\nabla e\wedge(d\sigma+A\sigma)+e(dA\,\sigma-A\wedge d\sigma)=e(A\wedge d\sigma+A\wedge A\sigma+dA\,\sigma-A\wedge d\sigma)=e(dA+A\wedge A)\sigma$. Conclusion: locally $F_\nabla=dA+A\wedge A$; the curvature is a first-order non-linear operator in the connection form.
- **R2.1.8 — Lie-algebra form and frame-change of curvature** (Remark 19, p. 10). Thinking of $A$ as a 1-form with values in $\mathfrak{gl}_k(\mathbb R)=\operatorname{End}(\mathbb R^k)$, (18) reads $F_\nabla=dA+\tfrac12[A\wedge A]$ (20), the last term combining wedge product and Lie bracket. If $e=e'\cdot g$, then using (14) one shows $F'_\nabla=dA'+A'\wedge A'=g^{-1}F_\nabla g$ ("the reader is strongly encouraged to check the details").

### 2.1.6 The gauge group — `PDF pages: 10–11`

#### Definitions
- **D2.1.12 — Gauge group of a vector bundle** (unlabelled, p. 10). $\mathcal G=\mathcal G(E):=\{g\in\Gamma(\operatorname{End}(E))\mid\forall m\in M,\ g(m)\in GL(E_m)\}$, endowed with the $C^\infty$-topology. If $E$ carries extra structure (orientation, scalar product), gauge transformations are required to respect it. $\mathcal G$ is a topological group with pointwise operations, called the group of gauge transformations or gauge group.
- **D2.1.13 — Gauge action on connections** (unlabelled, p. 10). For $\nabla\in\mathcal A(E)$ and $g\in\mathcal G$, $\nabla^gs:=g^{-1}\nabla(gs)$ defines another connection; this is a **right** action of $\mathcal G$ on $\mathcal A(E)$.
- **D2.1.14 — Gauge equivalent connections** (Definition 22, p. 11). Two connections are gauge equivalent if there is a gauge transformation transforming one into the other.

#### Theorems: none.
#### Examples: none.
#### Exercises: none.

#### Remarks / load-bearing paragraphs
- **R2.1.9 — Local representation of $\nabla^g$ equals frame change (14)** (p. 11). Using a frame $e$ over $U$, think of $g$ as $U\to GL_k(\mathbb R)$ via $g(e)=e\cdot g$. Then $\nabla^ge=g^{-1}(\nabla(e\cdot g))=g^{-1}(e\cdot Ag+e\cdot dg)=g^{-1}(e)\cdot(Ag+dg)=e\cdot(g^{-1}Ag+g^{-1}dg)$. Hence $A(\nabla^g,e)=g^{-1}Ag+g^{-1}dg=A(\nabla,e\cdot g)$: formula (14) expresses both the change of connection matrix under change of trivialisation and the gauge group action.
- **R2.1.10 — $\nabla^g$ is a connection / right action** (p. 10). Stated without proof: $\nabla^g$ satisfies (9); $(\nabla^{g})^{h}=\nabla^{gh}$.

### External results imported without proof (§2.1)
- **I2.1.1 — Hairy ball theorem** (p. 5, hint to Exercise 3): every vector field on $S^2$ vanishes somewhere.
- **I2.1.2 — Partition-of-unity gluing** ([BT03, Thm 3.3.7], p. 7): convex combinations of locally defined objects (Riemannian metrics, here connections) glue by a partition of unity to a global object.

---

## 2.2 Principal bundles

`PDF pages: 11–22`

### Standing conventions and notation (whole of §2.2)
- $G$ a Lie group; a principal $G$-bundle is a triple $(P,M,\pi)$; $G$ acts on $P$ **on the right**, $\pi(p\cdot g)=\pi(p)$, freely and transitively on fibres; local trivialisations $\psi_U\colon\pi^{-1}(U)\to U\times G$ are $G$-equivariant for right multiplication on the second factor (Definition 23, p. 11).
- Motivation: "consider all possible frames at once rather than choosing local trivialisations when needed" (p. 11).
- $\operatorname{Fr}(E_m)$ = set of all bases of $E_m$ (an open subset of $\mathbb R^{k^2}$ after a non-canonical identification with $GL_k(\mathbb R)$); $\operatorname{Fr}(E):=\bigsqcup_m\operatorname{Fr}(E_m)$; a frame $e\in\operatorname{Fr}(E_m)$ is also viewed as an isomorphism $\mathbb R^k\to E_m$, and $e\cdot h$ for $h\in GL_k(\mathbb R)$ is the right action (pp. 11–12, 14).
- Associated bundle: right action $(p,v)\cdot g=(p\cdot g,\rho(g^{-1})v)$ on $P\times V$; $P\times_\rho V:=(P\times V)/G$ (30); elements written $[p,v]$; projection still called $\pi$ (p. 14).
- $C^\infty(P;V)^G:=\{\hat s\colon P\to V\mid\hat s(p\cdot g)=\rho(g^{-1})\hat s(p)\}$; $\varpi\colon P\times V\to P\times_\rho V$ the natural projection (p. 15).
- $R_g\colon P\to P$, $R_g(p)=p\cdot g$; infinitesimal action $K_\xi(p):=\frac d{dt}\big|_{t=0}p\cdot\exp(t\xi)$, $\xi\in\mathfrak g$; vertical subspace $V_p:=\ker\pi_*|_p=\{K_\xi(p)\mid\xi\in\mathfrak g\}\cong\mathfrak g$ (p. 15).
- Equivariant form: $R_g^*\omega=\rho(g^{-1})\omega$; basic form: vanishes when any argument is vertical; $\Omega^q_{\mathrm{bas}}(P;V)^G$ (p. 16).
- Adjoint representation $\operatorname{ad}\colon G\to GL(\mathfrak g)$; for $G\subset GL_k(\mathbb R)$, $\operatorname{ad}_g\xi=g\xi g^{-1}$ (p. 16). $\operatorname{ad}P:=P\times_{\operatorname{ad}}\mathfrak g$; $\operatorname{Ad}P:=P\times_GG$ with $G$ acting on itself by conjugation (pp. 16, 21).
- Connection form $a\in\Omega^1(P;\mathfrak g)$: $G$-equivariant and $a(K_\xi)=\xi$ (Definition 40). $\mathcal A(P)$ = space of connections (p. 16).
- Differentiated representation $\rho_*|_1\colon\mathfrak g\to\operatorname{End}(V)$ (45) makes a connection $a$ into an $\operatorname{End}(V)$-valued 1-form; $a\cdot\hat s$ means this action (p. 17).
- $\hat R\colon P\times G\to P$, $\hat R(p,g)=p\cdot g$; $L_{g^{-1}}\colon G\to G$, $h\mapsto g^{-1}h$ (p. 18).
- Curvature of a principal connection: $\pi^*F_a=da+\tfrac12[a\wedge a]$ (49), $F_a\in\Omega^2(M;\operatorname{ad}P)$ (p. 19). $\hat F_A:=\pi^*F_A=dA+\tfrac12[A\wedge A]$ is "also" called the curvature (Remark 54, p. 21). Local representation $A:=\sigma^*a\in\Omega^1(U;\mathfrak g)$ for a local section $\sigma$; then $F_a=dA+\tfrac12[A\wedge A]$ over $U$ (p. 20). The notes switch freely between $a$ and $A$ for a principal connection from p. 20 on.
- Cartan's magic formula $\mathcal L_K=d\iota_K+\iota_Kd$ (p. 19).
- Pull-back bundle $f^*P:=\{(p,n)\in P\times N\mid f(n)=\pi(p)\}$, projection $\varpi$, equivariant map $\hat f\colon f^*P\to P$ covering $f$ (p. 21).
- Gauge group of a principal bundle: $\mathcal G(P):=\{\psi\colon P\to P\mid\pi\circ\psi=\pi,\ \psi(pg)=\psi(p)g\}$; action on connections $a\cdot\psi:=\psi^*a$ (61), a **right** action (pp. 21–22).
- Hopf fibration $\pi\colon S^{2n+1}\to\mathbb{CP}^n$, $z\mapsto[z]$ (43); $U(1)$-connection $a\in\Omega^1(S^{2n+1};\mathbb Ri)$ ($\mathfrak u(1)=\mathbb Ri$) (p. 17).

### 2.2.1 The frame bundle and the structure group — `PDF pages: 11–13`

#### Definitions
- **D2.2.1 — Principal bundle with structure group $G$** (Definition 23, p. 11). A principal bundle with structure group $G$ is a triple $(P,M,\pi)$ where: (i) $P$ and $M$ are smooth manifolds and $\pi\colon P\to M$ is a surjective submersion; (ii) $G$ acts on $P$ on the right such that $\pi(p\cdot g)=\pi(p)$ for all $p\in P$, $g\in G$; (iii) $G$ acts freely and transitively on each fibre $\pi^{-1}(m)$; (iv) for each $m\in M$ there is a neighbourhood $U\ni m$ and a map $\psi_U\colon\pi^{-1}(U)\to U\times G$ with $\mathrm{pr}_1\circ\psi_U=\pi$, and $\psi_U$ is $G$-equivariant, $\psi_U(p\cdot g)=\psi_U(p)\cdot g$, where $G$ acts on $U\times G$ by right multiplication on the second factor.
- **D2.2.2 — Frame bundle $\operatorname{Fr}(E)$** (unlabelled, pp. 11–12). For fixed $m$, $\operatorname{Fr}(E_m)$ is the set of all bases of $E_m$; $GL_k(\mathbb R)$ acts freely and transitively on it. $\operatorname{Fr}(E):=\bigsqcup_{m\in M}\operatorname{Fr}(E_m)$ with $\pi(p)=m\iff p\in\operatorname{Fr}(E_m)$. Smooth structure: for a chart $U$ with a local frame $e$ over $U$, $\Psi_U\colon U\times GL_k(\mathbb R)\to\pi^{-1}(U)$, $(m,h)\mapsto e(m)\cdot h$ (24) is a bijection, making $\pi^{-1}(U)$ a chart. Transition maps $\Psi_{U'}^{-1}\circ\Psi_U(m,h)=(m,g(m)h)$ with $g$ from (6) are smooth. Thus $\operatorname{Fr}(E)$ is a principal $GL_k(\mathbb R)$-bundle.
- **D2.2.3 — $G$-structure and structure group** (Definition 26, p. 12). Let $G$ be a Lie subgroup of $GL_k(\mathbb R)$. A $G$-structure on $E$ is a $G$-subbundle $P$ of the frame bundle $\operatorname{Fr}(E)$. Then $G$ is called the structure group of $E$.
- **D2.2.4 — Euclidean vector bundle; orthonormal frame bundle $O(E)$** (unlabelled, p. 12). $E$ is Euclidean if each fibre $E_m$ carries a Euclidean scalar product $\langle\cdot,\cdot\rangle_m$ depending smoothly on $m$, meaning $\langle s_1,s_2\rangle$ is smooth for all smooth sections $s_1,s_2$. $O(E):=\{e\in\operatorname{Fr}(E)\mid e\text{ is orthonormal}\}$, with $\pi\colon O(E)\to M$ and charts $\Psi_U\colon U\times O(k)\to\pi^{-1}(U)$, $(m,h)\mapsto e_O(m)\cdot h$ for a local orthonormal frame $e_O$.
- **D2.2.5 — Fibrewise volume form** (in Exercise 27, p. 13). A nowhere vanishing section of $\Lambda^kE^*$, $k=\operatorname{rk}E$.
- **D2.2.6 — Complex structure; complex vector bundle** (unlabelled, p. 13). A complex vector space $V$ of complex dimension $k$ is a real vector space of dimension $2k$ with $I\in\operatorname{End}_{\mathbb R}(V)$, $Iv=iv$, $I^2=-\mathrm{id}$; conversely a real $V$ with $I^2=-\mathrm{id}$ is complex via $i\cdot v:=Iv$ (then $\dim_{\mathbb R}V$ is even); $I$ is called a complex structure. A complex vector bundle is a real vector bundle $E$ equipped with $I\in\Gamma(\operatorname{End}E)$ such that $I^2=-\mathrm{id}$.
- **D2.2.7 — Hermitian structure** (in Exercise 29, p. 13). A smooth family of Hermitian scalar products on the fibres of a complex vector bundle.

#### Theorems
- **T2.2.1 — Euclidean structures are $O(k)$-structures** (unlabelled summary, pp. 12–13). A Euclidean structure on a rank-$k$ vector bundle $E$ is equivalent to an $O(k)$-structure $P\subset\operatorname{Fr}(E)$.
  `Proof in source: full (informal).` Strategy: (⇒) Given a Euclidean structure, Gram–Schmidt applied to any local frame gives a smooth pointwise orthonormal frame $e_O$; the maps $\Psi_U$ cover $O(E)$; since $O(k)$ is a manifold (not an open subset of Euclidean space) cover $O(k)$ by charts; transition functions smooth as for $\operatorname{Fr}(E)$; so $O(E)$ is a principal $O(k)$-bundle. (⇐) Given $P\subset\operatorname{Fr}(E)$ an $O(k)$-structure, pick $p\in P_m$, write $v_i=p\cdot x_i$, $x_i\in\mathbb R^k$, and set $\langle v_1,v_2\rangle:=x_1^tx_2$; "straightforward to check" independence of $p$ and smoothness in $m$.
  `Gaps:` independence of $p$ (uses $O(k)$-invariance of $x_1^tx_2$) and smoothness asserted.

#### Examples: (the Euclidean-structure discussion is the illustrating example; no numbered examples in 2.2.1).

#### Exercises
- **X2.2.1** (Exercise 25, p. 12). Show that local triviality of a principal bundle (Property (iv) of Definition 23) is equivalent to the existence of local sections. More precisely: if $P$ admits a trivialisation over $U$, then there is a section of $P|_U$; conversely, if $P|_U$ admits a section, then $P|_U$ is trivialisable over $U$. In particular, show that the frame bundle of $TS^2$ does not admit any global sections.
- **X2.2.2** (Exercise 27, p. 13). Show that there is a one-to-one correspondence between fibrewise volume forms (nowhere vanishing sections of $\Lambda^kE^*$) and $SL_k(\mathbb R)$-structures.
- **X2.2.3** (Exercise 28, p. 13). (i) Show that a complex vector bundle can be defined as a locally trivial family of complex vector spaces akin to Definition 1. (ii) Show that there is a one-to-one correspondence between complex structures on a real vector bundle $E$ of rank $2k$ and $GL_k(\mathbb C)$-structures, where $GL_k(\mathbb C)=\{A\in GL_{2k}(\mathbb R)\mid A\circ I_{st}=I_{st}\circ A\}\subset GL_{2k}(\mathbb R)$ and $I_{st}(x_1,y_1,\dots,x_k,y_k):=(-y_1,x_1,\dots,-y_k,x_k)$ is the standard complex structure on $\mathbb R^{2k}$.
- **X2.2.4** (Exercise 29, p. 13). Prove: (i) any complex vector bundle admits a Hermitian structure; (ii) there is a one-to-one correspondence between Hermitian structures and $U(k)$-structures.

#### Remarks / load-bearing paragraphs
- **R2.2.1 — Smooth structure on $\operatorname{Fr}(E)$ and verification of the principal-bundle axioms** (pp. 11–12). $\operatorname{Fr}(E_m)$ is identified (non-canonically) with $GL_k(\mathbb R)$, an open subset of $\mathbb R^{k^2}$; charts $\pi^{-1}(U)$ via (24); transition $(m,h)\mapsto(m,g(m)h)$ is a "straightforward computation"; "the rest of the properties required in the definition of the principal bundle are clear from the construction".
- **R2.2.2 — Extra structure on $E$ corresponds to $G$-structures** (p. 12): orientations / scalar products on fibres ↔ reduction of the structure group.

### 2.2.2 The associated vector bundle — `PDF pages: 14–16`

#### Definitions
- **D2.2.8 — Associated vector bundle** (construction pp. 14 and Definition 31). Let $\pi\colon P\to M$ be a principal $G$-bundle and $\rho\colon G\to GL(V)$ a representation. Define the right $G$-action on $P\times V$ by $(p,v)\cdot g=(p\cdot g,\rho(g^{-1})v)$; it is free and properly discontinuous, so $P\times_\rho V:=(P\times V)/G$ (30) is a smooth manifold. The projection $P\times_\rho V\to M$, $[p,v]\mapsto\pi(p)$, has fibres isomorphic to $V$ (canonical vector space structure). Given a local section $s\in\Gamma(U;P)$, $\psi_U^{-1}\colon U\times V\to\pi_E^{-1}(U)$, $(m,v)\mapsto[s(m),v]$ is a local trivialisation; hence $P$ locally trivial ⇒ $E$ locally trivial. The vector bundle $E=E(P,\rho,V)$ so defined is the vector bundle associated with $(P,\rho)$, or the associated bundle.
- **D2.2.9 — Equivariant functions $C^\infty(P;V)^G$** (unlabelled, p. 15). $C^\infty(P;V)^G:=\{\hat s\colon P\to V\mid\hat s(p\cdot g)=\rho(g^{-1})\hat s(p)\ \forall p\in P,g\in G\}$. For $\hat s$ in it, $\varpi\circ(\mathrm{id},\hat s)\colon P\to P\times_\rho V$, $p\mapsto[p,\hat s(p)]$, is $G$-invariant, so there is a unique $s\colon M\to P\times_\rho V$ with $s\circ\pi=\varpi\circ(\mathrm{id},\hat s)$ (36).
- **D2.2.10 — Infinitesimal action and vertical subspace** (unlabelled, p. 15). $R_g(p):=p\cdot g$; $K_\xi(p):=\frac d{dt}\big|_{t=0}(p\cdot\exp(t\xi))$ for $\xi\in\mathfrak g$; $V_p:=\ker\pi_*|_p=\{K_\xi(p)\mid\xi\in\mathfrak g\}\cong\mathfrak g$ (using freeness) is the vertical subspace.
- **D2.2.11 — Equivariant and basic forms** (Definition 38, p. 16). A $q$-form $\omega$ on $P$ with values in a $G$-representation $V$ is $G$-equivariant if $R_g^*\omega=\rho(g^{-1})\omega$; it is basic if $\omega(v_1,\dots,v_q)=0$ whenever one argument is vertical. $\Omega^q_{\mathrm{bas}}(P;V)^G$ denotes the space of basic $G$-equivariant $V$-valued $q$-forms.

#### Theorems
- **T2.2.2 — Sections of associated bundles are equivariant functions** (Proposition 37, p. 15). The map $C^\infty(P;V)^G\to\Gamma(P\times_\rho V)$, $\hat s\mapsto s$ with $s$ defined by (36), is a bijection.
  `Proof in source: full (short).` Strategy: construct the inverse: for a section $s$ and $p\in P$ there is a unique $\hat s(p)\in V$ with $s(\pi(p))=[p,\hat s(p)]$ (freeness/transitivity); "straightforward to check that $\hat s$ is equivariant".
  `Gaps:` equivariance check and smoothness of $\hat s$ not written.
- **T2.2.3 — Bundle-valued forms on $M$ are basic equivariant forms on $P$** (Proposition 39, p. 16). For any $a\in\Omega^q(M;P\times_\rho V)$ the pull-back $\pi^*a$ can be viewed as an element of $\Omega^q_{\mathrm{bas}}(P;V)^G$, and $a\mapsto\pi^*a$ is a bijection $\Omega^q(M;P\times_\rho V)\to\Omega^q_{\mathrm{bas}}(P;V)^G$.
  `Proof in source: full.` Strategy: (⇒) For $\hat v_1,\dots,\hat v_q\in T_pP$ the equality $a(\pi_*\hat v_1,\dots,\pi_*\hat v_q)=[p,\hat a_p(\hat v_1,\dots,\hat v_q)]$ uniquely determines $\hat a\in\Omega^q(P;V)$; basic since vertical $=\ker\pi_*$; equivariance "follows from a straightforward computation". (⇐) Given $\hat a$, for $m$, $p\in\pi^{-1}(m)$, $v_j\in T_mM$ choose lifts $\hat v_j$ with $\pi_*\hat v_j=v_j$ (exist since $\pi_*$ surjective, not unique) and set $a_m(v_1,\dots,v_q):=[p,\hat a_p(\hat v_1,\dots,\hat v_q)]$; basic + equivariant ⇒ independent of choices.
  `Gaps:` equivariance computation; independence of the choice of $p$ and lifts only asserted.

#### Examples
- **E2.2.1 — Recovering $E$ from its frame bundle** (Example 32, p. 14). $P=\operatorname{Fr}(E)$, $V=\mathbb R^k$, $\rho=\mathrm{id}$ the tautological representation of $GL_k(\mathbb R)$. The map $\operatorname{Fr}(E)\times\mathbb R^k\to E$, $(e,x)\mapsto\sum_{i=1}^kx_ie_i$, induces an isomorphism $E(\operatorname{Fr}(E),\mathrm{id})\cong E$.
- **E2.2.2 — $\Lambda^pE^*$ as an associated bundle** (Example 33, p. 14). $P=\operatorname{Fr}(E)$, $V=\Lambda^p(\mathbb R^k)^*$, $\rho\colon GL_k(\mathbb R)\times\Lambda^p(\mathbb R^k)^*\to\Lambda^p(\mathbb R^k)^*$, $(g,\alpha)\mapsto\alpha(g^{-1}\cdot,\dots,g^{-1}\cdot)$ (34). The map $\operatorname{Fr}(E)\times\Lambda^p(\mathbb R^k)^*\to\Lambda^pE^*$, $(e,\alpha)\mapsto\alpha(e^{-1}\cdot,\dots,e^{-1}\cdot)$ (frame $e$ as isomorphism $\mathbb R^k\to E_{\pi(e)}$) induces $\operatorname{Fr}(E)\times_\rho\Lambda^p(\mathbb R^k)^*\cong\Lambda^pE^*$.

#### Exercises
- **X2.2.5** (Exercise 35, p. 15). Let $V=M_k(\mathbb R)\cong\operatorname{End}(\mathbb R^k)$ with the $GL_k(\mathbb R)$-representation $\rho\colon(g,A)\mapsto gAg^{-1}$. Show that $\operatorname{Fr}(E)\times_\rho\operatorname{End}(\mathbb R^k)$ is isomorphic to $\operatorname{End}(E)$.

#### Remarks / load-bearing paragraphs
- **R2.2.3 — Local triviality of the associated bundle** (p. 14). The action on $P\times V$ is free and properly discontinuous ("clearly"), hence the quotient is a manifold; fibres canonically vector spaces; local sections of $P$ give local trivialisations of $E$.
- **R2.2.4 — Commutative diagram defining $s$ from $\hat s$** (p. 15): $P\xrightarrow{(\mathrm{id},\hat s)}P\times V\xrightarrow{\varpi}P\times_\rho V$ factors through $\pi\colon P\to M$ and $s\colon M\to P\times_\rho V$.

### 2.2.3 Connections on principal bundles — `PDF pages: 16–19`

#### Definitions
- **D2.2.12 — Adjoint bundle $\operatorname{ad}P$** (unlabelled, p. 16). $\mathfrak g$ is a $G$-representation via $\operatorname{ad}\colon G\to GL(\mathfrak g)$ (for $G\subset GL_k(\mathbb R)$, $\operatorname{ad}_g\xi=g\xi g^{-1}$); $\operatorname{ad}P:=P\times_{\operatorname{ad}}\mathfrak g$.
- **D2.2.13 — Connection form on a principal bundle** (Definition 40, p. 16). A connection form, or simply a connection, on a principal $G$-bundle $P$ is a $G$-equivariant 1-form $a$ with values in $\mathfrak g$ (i.e. $R_g^*a=\operatorname{ad}_{g^{-1}}a$) such that $a(K_\xi)=\xi$ for all $\xi\in\mathfrak g$. $\mathcal A(P)$ := space of all connections.
- **D2.2.14 — Derivative of a representation** (equation (45), p. 17). Differentiating $\rho\colon G\to GL(V)$ at $1$ gives a Lie algebra homomorphism $\rho_*|_1\colon\mathfrak g\to\operatorname{End}(V)$; via this a connection $a$ is regarded as an $\operatorname{End}(V)$-valued 1-form when a representation $V$ is given.

#### Theorems
- **T2.2.4 — Space of principal connections is affine** (Theorem 41, p. 16). For any principal bundle $P$ the space $\mathcal A(P)$ of all connections is an affine space modelled on $\Omega^1(\operatorname{ad}P)$. In particular $\mathcal A(P)\ne\varnothing$.
  `Proof in source: sketch ("can be proved in the same manner as Theorem 11").` Only modification described: for $a,a'\in\mathcal A(P)$ the difference $b:=a-a'$ is basic (both take the value $\xi$ on $K_\xi$) and $G$-equivariant (the source says "$G$-invariant"), so by Proposition 39 $b$ is a 1-form on $M$ with values in $\operatorname{ad}P$.
  `Gaps:` existence (local connections from local trivialisations glued by partition of unity) and the converse (adding $b\in\Omega^1(\operatorname{ad}P)$ gives a connection) not written.
- **T2.2.5 — Vector-bundle connections ↔ principal connections** (Theorem 46, p. 17). (i) Let $E$ be a vector bundle. Any connection $\nabla$ on $E$ determines a unique connection $a$ on the frame bundle $\operatorname{Fr}(E)$ such that $e^*a=A(\nabla,e)$ for every local frame $e$ (viewed as a local section of $\operatorname{Fr}(E)$), where $A(\nabla,e)$ is the local connection 1-form of $\nabla$ with respect to $e$. (ii) Let $P$ be a principal $G$-bundle. Any connection $a$ on $P$ induces a unique connection $\nabla$ on any associated bundle $P\times_\rho V$ such that
$$\pi^*\nabla s=d\hat s+a\cdot\hat s,\qquad(47)$$
where the right side is a basic $G$-equivariant 1-form on $P$ and the equality is in the sense of Proposition 39.
  `Proof in source: full, in four steps (Step 1 left as exercise).` Step 1: for $\hat R(p,g)=p\cdot g$, the differential at $(p,g)$ is $\hat R_*(v,w)=(R_g)_*v+K_{(L_{g^{-1}})_*w}(p\cdot g)$ for $v\in T_pP$, $w\in T_gG$ ("simple computation, left as an exercise"). Step 2: for a local frame $e$ over $U$ and any $A\in\Omega^1(U;\mathfrak{gl}_k(\mathbb R))$ there is a unique connection $a$ on $\operatorname{Fr}(E)|_U$ with $e^*a=A$: since $\pi_*\circ e_*=\mathrm{id}$, $e_*$ is injective and $T_{e(m)}P=V_{e(m)}\oplus\operatorname{Im}e(m)_*$ by dimension count; define $a_{e(m)}(K_\xi+e_*v):=\xi+A(v)$ and extend to a unique $G$-equivariant form; the identity $(R_g)_*K_\xi=K_{\operatorname{ad}_{g^{-1}}\xi}$ ("straightforward computation") implies $a$ is a connection. Step 3 (proof of (i)): for two frames $e,e'=e\cdot g$ on the same $U$, the forms $a,a'$ from Step 2 agree: $e'^*a(\cdot)=a_{e\cdot g}((\hat R\circ(e,g))_*\cdot)=a_{e\cdot g}((R_g)_*e_*\cdot)+a_{e\cdot g}(K_{g^{-1}dg})=g^{-1}a_e(e_*\cdot)g+g^{-1}dg=A'(\cdot)$ using Step 1 and (14); hence $a$ is globally well defined. Step 4 (proof of (ii)): by equivariance of $\hat s$, $(d\hat s+a\cdot\hat s)(K_\xi)=-\xi\cdot\hat s+a(K_\xi)\cdot\hat s=0$, so $d\hat s+a\cdot\hat s$ is basic, and it is $G$-equivariant; Proposition 39 gives $\nabla s$; for a $G$-invariant function $f$ on $P$, $d(f\hat s)+a\cdot(f\hat s)=df\otimes\hat s+f(d\hat s+a\cdot\hat s)$ shows the Leibniz rule.
  `Gaps:` Step 1 and $(R_g)_*K_\xi=K_{\operatorname{ad}_{g^{-1}}\xi}$ left to reader; equivariance of $d\hat s+a\cdot\hat s$ asserted; uniqueness in (ii) not argued explicitly.
- **T2.2.6 — Induced connections on $E^*$, $\operatorname{End}E$** (unlabelled corollary, p. 19). A connection on $E$ induces connections on $E^*$, $\operatorname{End}(E)$ "and so on", since these are associated bundles of $\operatorname{Fr}(E)$ for the corresponding $GL_k(\mathbb R)$-representations. Direct characterisation in Exercise 48.
  `Proof in source: omitted (immediate from Theorem 46).`

#### Examples
- **E2.2.3 — Hopf fibration and its canonical connection** (Example 42, p. 17). $U(1)$ acts freely on $S^{2n+1}:=\{z\in\mathbb C^{n+1}\mid|z_0|^2+\dots+|z_n|^2=1\}$ diagonally, giving the $U(1)$-bundle $\pi\colon S^{2n+1}\to\mathbb{CP}^n$, $z\mapsto[z]$ (43), the Hopf fibration. The infinitesimal action is $v(z)=(iz_0,\dots,iz_n)$. There is a unique connection $a\in\Omega^1(S^{2n+1};\mathbb Ri)$ with $\ker a=v^\perp$; explicitly $a_z(u)=\langle v(z),u\rangle\,i$ for $u\in T_zS^{2n+1}$. Since the $U(1)$-action preserves the round metric, $a$ is invariant; for abelian groups equivariant = invariant; hence $a$ is a connection.

#### Exercises
- **X2.2.6** (Exercise 44, p. 17). Prove that the associated bundle $S^{2n+1}\times_{U(1)}\mathbb C$ is (canonically) isomorphic to the tautological line bundle $\mathcal O(-1):=\{([z],w)\in\mathbb{CP}^n\times\mathbb C^{n+1}\mid w\in[z]\cup\{0\}\}$.
- **X2.2.7** (Exercise 48, p. 19). Let $\nabla$ be a connection on $E$. Show: (i) there is a unique connection on $E^*$, still denoted $\nabla$, such that $d\langle\alpha,s\rangle=\langle\nabla\alpha,s\rangle+\langle\alpha,\nabla s\rangle$ for all $\alpha\in\Gamma(E^*)$, $s\in\Gamma(E)$, where $\langle\cdot,\cdot\rangle$ is the natural pairing $E^*\otimes E\to\mathbb R$; this connection coincides with the induced one. (ii) There is a unique connection on $\operatorname{End}(E)$, still denoted $\nabla$, such that $\nabla(\phi(s))=(\nabla\phi)(s)+\phi(\nabla s)$ for all $\phi\in\Gamma(\operatorname{End}(E))$, $s\in\Gamma(E)$; it coincides with the induced one.
- **X2.2.8** (Step 1 of the proof of Theorem 46, p. 18, "left as an exercise"). Prove $\hat R_*(v,w)=(R_g)_*v+K_{(L_{g^{-1}})_*w}(p\cdot g)$.

#### Remarks / load-bearing paragraphs
- **R2.2.5 — Difference of two connections is basic and equivariant** (p. 16): the argument underlying Theorem 41.
- **R2.2.6 — Relation of the two notions of connection** (p. 17): motivation for Theorem 46; a $\mathfrak g$-valued connection becomes $\operatorname{End}(V)$-valued via (45).

### 2.2.4 The curvature of a connection on a principal bundle — `PDF pages: 19–21`

#### Definitions
- **D2.2.15 — Curvature form of a principal connection** (Definition 50, p. 19). For a connection $a$ on a principal $G$-bundle $P$, the $\mathfrak g$-valued 2-form $da+\tfrac12[a\wedge a]$ on $P$ is $G$-equivariant (source: "$G$-invariant") and basic, hence by Proposition 39 there is $F_a\in\Omega^2(M;\operatorname{ad}P)$ with $\pi^*F_a=da+\tfrac12[a\wedge a]$ (49); $F_a$ is the curvature form of $a$.
- **D2.2.16 — Local representation of a principal connection** (unlabelled, p. 20). For a local section $\sigma$ of $P$ over $U$ (a local trivialisation), $A:=\sigma^*a\in\Omega^1(U;\mathfrak g)$ is the local representation of $a$ with respect to $\sigma$; over $U$, $F_a=\sigma^*\pi^*F_a=\sigma^*(da+\tfrac12[a\wedge a])=dA+\tfrac12[A\wedge A]$.
- **D2.2.17 — Pull-back principal bundle** (unlabelled, p. 21). For $P\to M$ and $f\colon N\to M$, $f^*P:=\{(p,n)\in P\times N\mid f(n)=\pi(p)\}$, a submanifold of $P\times N$, with projection $\varpi\colon f^*P\to N$, $(p,n)\mapsto n$, fibres $\varpi^{-1}(n)=P_{f(n)}$ on which $G$ acts transitively, and the natural $G$-equivariant map $\hat f\colon f^*P\to P$ covering $f$ ($\pi\circ\hat f=f\circ\varpi$). Informally $(f^*P)_n=P_{f(n)}$.

#### Theorems
- **T2.2.7 — Curvature of the induced connection** (Proposition 52, p. 20). Let $a$ be a connection on $P$ and $V$ a $G$-representation. Using (45) think of $F_a$ as a 2-form with values in $\operatorname{End}(P\times_\rho V)$. Then the curvature of the induced connection $\nabla$ on $P\times_\rho V$ equals $F_a$.
  `Proof in source: left as exercise.`
- **T2.2.8 — Bianchi identity** (Proposition 53, p. 20). Let $a$ be a connection on $P$. Then $d^{\nabla_a}F_a=0$, where $\nabla_a$ is the connection on $\operatorname{ad}P$ induced by $a$.
  `Proof in source: full (local computation).` With $A$ a local representation: $d^{\nabla_a}F_a=d(dA+\tfrac12[A\wedge A])+[A\wedge(dA+\tfrac12[A\wedge A])]=\tfrac12[dA\wedge A]-\tfrac12[A\wedge dA]+[A\wedge dA]+\tfrac12[A\wedge[A\wedge A]]=0$; the first three terms cancel because $[\omega,\eta]=-[\eta,\omega]$ for $\omega\in\Omega^2(U;\mathfrak g)$, $\eta\in\Omega^1(U;\mathfrak g)$; the last vanishes by the Jacobi identity.
  `Gaps:` the sign rule for graded brackets and the Jacobi-identity step are asserted, not derived.
- **T2.2.9 — Pull-back of connections and curvature** (Proposition 56, p. 21). Let $A$ be a connection on $P$. Then $f^*A:=\hat f^*A$ is a connection on $f^*P$ and $F_{f^*A}=f^*F_A$.
  `Proof in source: left as exercise.`

#### Examples
- **E2.2.4 — Curvature of the Hopf connection on $S^3\to S^2$** (Example 51, pp. 19–20). On $S^3\subset\mathbb R^4$ ($n=1$) the vector fields $v_1:=(-x_1,x_0,-x_3,x_2)$, $v_2:=(-x_2,x_3,x_0,-x_1)$, $v_3:=(-x_3,-x_2,x_1,x_0)$ form at each point an oriented orthonormal basis of the tangent space; $v_1$ equals $v$ of Example 42. The connection form is $a=(-x_1dx_0+x_0dx_1-x_3dx_2+x_2dx_3)\,i$, so $\pi^*F_a=da=2(dx_0\wedge dx_1+dx_2\wedge dx_3)\,i$ and $F_a(\pi_*v_2,\pi_*v_3)=\pi^*F_a(v_2,v_3)=2i$. The quotient metric on $S^3/U(1)$ is the round metric on the sphere $S^2_{1/2}$ of radius $\tfrac12$, via the isometry $(z_0,z_1)\mapsto(z_0\bar z_1,\tfrac12(|z_0|^2-|z_1|^2))$ ($S^3\subset\mathbb C^2$). Since $(\pi_*v_2,\pi_*v_3)$ is an oriented orthonormal basis of $TS^2_{1/2}$, $F_a=2\,\mathrm{vol}_{S^2_{1/2}}\,i$, and $\int_{S^2}F_a=2\operatorname{Vol}(S^2_{1/2})\,i=2\pi i$.
  `Gaps:` "it can be shown that the quotient metric ... yields the round metric on the sphere of radius $1/2$" — not proved.

#### Exercises: Propositions 52 and 56 are "left as an exercise" (listed above as T2.2.7, T2.2.9).

#### Remarks / load-bearing paragraphs
- **R2.2.7 — $da+\tfrac12[a\wedge a]$ is basic** (p. 19). Computation using Cartan's formula $\mathcal L_K=d\iota_K+\iota_Kd$: $\iota_{K_\xi}(da+\tfrac12[a\wedge a])=\mathcal L_{K_\xi}a-d(\iota_{K_\xi}a)+\tfrac12[a(K_\xi),a(\cdot)]-\tfrac12[a(\cdot),a(K_\xi)]=-[\xi,a]+0+\tfrac12[\xi,a]+\tfrac12[\xi,a]=0$ (using $\mathcal L_{K_\xi}a=-[\xi,a]$ from equivariance and $d\xi=0$). $G$-invariance is "clear".
- **R2.2.8 — Equivalent form of Bianchi** (Remark 54, p. 21). With $\hat F_A:=\pi^*F_A=dA+\tfrac12[A\wedge A]$ regarded as the curvature, the computation in the proof of Proposition 53 gives $d\hat F_A=[\hat F_A\wedge A]$ (55); indeed $d\hat F_A=[dA\wedge A]=[\hat F_A\wedge A]$.
- **R2.2.9 — Construction of $f^*P$ as a principal bundle** (p. 21): "easy to see" $f^*P$ is a submanifold; $G$ acts transitively on fibres; commutative square with $\hat f$.

### 2.2.5 The gauge group — `PDF pages: 21–22`

#### Definitions
- **D2.2.18 — Gauge group of a principal bundle** (unlabelled, p. 21). $\mathcal G(P):=\{\psi\colon P\to P\mid\pi\circ\psi=\pi,\ \psi(pg)=\psi(p)g\ \forall p\in P,g\in G\}$, the automorphism group of $P$.
- **D2.2.19 — $\operatorname{Ad}P$ and the identification $\mathcal G(P)\cong\Gamma(\operatorname{Ad}P)$** (unlabelled, p. 21). Since $\psi(p)$ is in the fibre of $p$, $\psi(p)=p\hat f(p)$ (57) for some $\hat f\colon P\to G$; equivariance of $\psi$ is equivalent to $\hat f(pg)=g^{-1}\hat f(p)g$ (58) (the source's text has the typo "$g^{-1}pg$"). So $\hat f$ is a section $f$ of $\operatorname{Ad}P:=P\times_GG$, $G$ acting on itself by conjugation. Conversely $f\in\Gamma(\operatorname{Ad}P)$ gives $\psi$ via (57). Natural bijection $\mathcal G(P)\to\Gamma(\operatorname{Ad}P)$.
- **D2.2.20 — Gauge action on principal connections** (equation (61), p. 22). $\mathcal A(P)\times\mathcal G(P)\to\mathcal A(P)$, $(a,\psi)\mapsto a\cdot\psi:=\psi^*a$.

#### Theorems: none (all in exercises).

#### Examples
- **E2.2.5 — Gauge group for abelian $G$** (Example 60, p. 22). If $G$ is abelian, (58) says $\hat f$ is invariant, so $f$ is a map $M\to G$: $\mathcal G(P)\cong C^\infty(M;G)$.

#### Exercises
- **X2.2.9** (Exercise 59, p. 22). Fix a non-negative integer $k$. Prove that $C^k(M;\operatorname{Ad}P)$ is a Banach Lie group. Moreover, show that the Lie algebra of this group is $C^k(M;\operatorname{ad}P)$.
- **X2.2.10** (Exercise 62, p. 22). Let $E:=P\times_{G,\rho}V$ be an associated vector bundle. Show: (i) the representation $\rho$ induces a natural homomorphism of gauge groups $\gamma\colon\mathcal G(P)\to\mathcal G(E)$; (ii) the infinitesimal map $d\rho_e\colon\mathfrak g\to\operatorname{End}V$ induces a Lie algebra homomorphism $C^k(M;\operatorname{ad}P)\to C^k(M;\operatorname{End}E)$; (iii) $\nabla_{a\cdot g}=g^{-1}\nabla_ag$, where $a\in\mathcal A(P)$, $g\in\Gamma(\operatorname{Ad}P)$, and $\nabla_a$ is the connection on $E$ induced by $a$.
- **X2.2.11** (Exercise 63, p. 22). Show that the infinitesimal action of the gauge group is given by $\mathcal A(P)\times\Gamma(\operatorname{ad}P)\to\Omega^1(\operatorname{ad}P)$, $(a,\xi)\mapsto-d_a\xi$. (The source prints the target as $\Omega^0(\operatorname{ad}P)$, a typo; $d_a\xi\in\Omega^1(\operatorname{ad}P)$.)

#### Remarks / load-bearing paragraphs
- **R2.2.10 — Derivation of $\mathcal G(P)\cong\Gamma(\operatorname{Ad}P)$** (p. 21): transitivity gives (57), equivariance gives (58).

### External results imported without proof (§2.2)
- **I2.2.1 — Gram–Schmidt orthogonalisation** produces a smooth pointwise orthonormal frame from any smooth frame (p. 12).
- **I2.2.2 — Quotients by free properly discontinuous actions are manifolds** (p. 14, for $P\times_\rho V$).
- **I2.2.3 — Cartan's magic formula** $\mathcal L_K=d\iota_K+\iota_Kd$ (p. 19).
- **I2.2.4 — Quotient metric on $S^3/U(1)$ is the round metric of radius $1/2$** with the stated explicit isometry (p. 20, "it can be shown").
- **I2.2.5 — Graded antisymmetry $[\omega,\eta]=-[\eta,\omega]$ for $\omega\in\Omega^2$, $\eta\in\Omega^1$ and the Jacobi identity for $[A\wedge[A\wedge A]]=0$** (p. 20).

---

## 2.3 The Levi–Civita connection

`PDF pages: 22–23`

### Standing conventions and notation
- Torsion $T(v,w):=\nabla_vw-\nabla_wv-[v,w]$ for a connection $\nabla$ on $TM$ (p. 22).
- Metric connection: $d(g(v,w))=g(\nabla v,w)+g(v,\nabla w)$ (p. 23).
- Curvature of Levi-Civita written $R\in\Gamma(\Lambda^2T^*M\otimes\operatorname{End}(TM))$.
- **Ricci sign convention:** $\operatorname{Ric}_g(v,w):=-\sum_ig(R(e_i,v)e_i,w)$ for a local orthonormal frame $(e_i)$; scalar curvature $s_g:=\sum_i\operatorname{Ric}(e_i,e_i)$ (p. 23). (With $R(X,Y)=\nabla_X\nabla_Y-\nabla_Y\nabla_X-\nabla_{[X,Y]}$ this is the standard Ricci tensor $\operatorname{Ric}(v,w)=\sum_ig(R(e_i,v)w,e_i)$; the minus sign compensates for the slot ordering.)

### Definitions
- **D2.3.1 — Torsion of a connection on $TM$** (unlabelled, p. 22). For vector fields $v,w$, $T(v,w):=\nabla_vw-\nabla_wv-[v,w]$. $T$ is antisymmetric and tensorial, $T(f_1v,f_2w)=f_1f_2T(v,w)$, so by Lemma 12 $T\in\Omega^2(M;TM)$.
- **D2.3.2 — Torsion-free connection** (Definition 64, p. 22). A connection $\nabla$ on $TM$ is torsion-free if $T\equiv0$, i.e. $\nabla_vw-\nabla_wv=[v,w]$ (65) for all vector fields $v,w$.
- **D2.3.3 — Levi-Civita connection** (unlabelled, p. 23). The unique metric torsion-free connection of Theorem 68; uniquely characterised by (65) together with $d(g(v,w))=g(\nabla v,w)+g(v,\nabla w)$.
- **D2.3.4 — Ricci curvature and scalar curvature** (unlabelled, p. 23). With $R$ the curvature of the Levi-Civita connection and $(e_i)$ a local orthonormal frame: $\operatorname{Ric}_g(v,w):=-\sum_ig(R(e_i,v)e_i,w)$ (a quadratic form); $s_g:=\sum_i\operatorname{Ric}(e_i,e_i)$ (scalar curvature, the trace of Ricci).

### Theorems
- **T2.3.1 — Fundamental theorem of Riemannian geometry** (Theorem 68, p. 23). For any Riemannian manifold $(M,g)$ there is a unique metric torsion-free connection $\nabla$.
  `Proof in source: omitted/cited (to [Sal89, Prop. 2.1]).`

### Examples: none.

### Exercises
- **X2.3.1** (Exercise 66, p. 22). Let $\nabla$ be a connection on $TM$; denote also by $\nabla$ the induced connection on $T^*M$. Consider $\Omega^1(M)\xrightarrow{\nabla}\Gamma(T^*M\otimes T^*M)\xrightarrow{\mathrm{Alt}}\Omega^2(M)$ (67), the last map the natural projection (alternation) $T^*M\otimes T^*M\to\Lambda^2T^*M$. Show that $\nabla$ is torsion-free if and only if (67) coincides with the de Rham differential.

### Remarks / load-bearing paragraphs
- **R2.3.1 — Tensoriality of torsion** (p. 22): "easy to check" $T(f_1v,f_2w)=f_1f_2T(v,w)$; then Lemma 12 gives $T\in\Omega^2(M;TM)$.
- **R2.3.2 — Why $TM$ is special** (p. 22): generic bundles have no preferred connection; the tangent bundle of a Riemannian manifold does.
- **R2.3.3 — Role of scalar curvature** (p. 23): it appears in the Weitzenböck formula, Corollary 133; references [Joy07, Sal89, Bes08].

### External results imported without proof
- **I2.3.1 — Existence and uniqueness of the Levi-Civita connection** [Sal89, Prop. 2.1] (p. 23).

---

## 2.4 Classification of $U(1)$ and $SU(2)$ bundles

`PDF pages: 23–26`

### Standing conventions and notation
- Work in the **topological** category (continuous maps, topological principal bundles) (p. 23).
- Traditional notation: $E$ = total space of the classifying bundle (a *principal* bundle here, footnote 2), $B:=E/G$ (p. 23).
- $[M;B]$ = set of homotopy classes of maps $M\to B$ (p. 23).
- Generator $a\in H^2(\mathbb{CP}^\infty;\mathbb Z)$ fixed by $\langle a,[\mathbb{CP}^1]\rangle=1$ (73); $c_1(P):=-f^*a$ (74) — **minus sign is a convention** (p. 25).
- Generator $b\in H^4(\mathbb{HP}^\infty;\mathbb Z)$ fixed by $\langle b,[\mathbb{HP}^1]\rangle=1$; $c_2(P):=-f^*b$ (p. 26).
- $\mathbb H$ quaternions; $Sp(1):=\{q\in\mathbb H\mid|q|^2=q\bar q=1\}$; explicit isomorphism $Sp(1)\to SU(2)$, $q=z+wj\mapsto\begin{pmatrix}z&w\\-\bar w&\bar z\end{pmatrix}$ (p. 25).
- $L^\vee:=\operatorname{Hom}(L;\mathbb C)$ dual line bundle (p. 25).

### Definitions
- **D2.4.1 — Classifying bundle / classifying space** (Definition 69, p. 23). Let $G$ be a compact Lie group. A topological space $E$ with a $G$-action is a classifying bundle for $G$ if $E$ is contractible and the $G$-action is free. With $B:=E/G$, $E\to B$ is a principal $G$-bundle; $E$ is unique up to homotopy equivalence ("easy to see"); existence for compact $G$ is granted ([GS99b, §1.2]).
- **D2.4.2 — Characteristic class** (Definition 71, p. 24). Let $f\colon M\to B$ be continuous and $c\in H^\bullet(B;R)$, $R$ a ring. Then $f^*c\in H^\bullet(M;R)$ is called a characteristic class of $f^*E$. Characteristic classes depend only on the isomorphism class of the bundle. Common $R$: $\mathbb Z$, $\mathbb Z/n\mathbb Z$, $\mathbb R$, $\mathbb C$.
- **D2.4.3 — Classifying bundle for $U(1)$: $S^\infty\to\mathbb{CP}^\infty$** (unlabelled, p. 24). Direct limit of the $U(1)$-equivariant inclusions $S^{2n-1}\ni(z_0,\dots,z_{n-1})\mapsto(z_0,\dots,z_{n-1},0)\in S^{2n+1}$ covering $\mathbb{CP}^{n-1}\subset\mathbb{CP}^n$ yields a CW-complex $S^\infty$ with a free $U(1)$-action, contractible ("can be shown"), and $S^\infty\to\mathbb{CP}^\infty$ is the classifying bundle for $U(1)$.
- **D2.4.4 — Degree of a line bundle on an oriented 2-manifold** (Example 72, p. 24). The integer $d=\deg f$ classifying $L$, see E2.4.1.
- **D2.4.5 — First Chern class (topological definition)** (Definition 75 with (73)–(74), p. 25). $H^\bullet(\mathbb{CP}^\infty;\mathbb Z)$ is generated by $a\in H^2$ with $\langle a,[\mathbb{CP}^1]\rangle=1$ (73). For a principal $U(1)$-bundle $P\to M$ with classifying map $f\colon M\to\mathbb{CP}^\infty$ ($P\cong f^*S^\infty$), $c_1(P):=-f^*a\in H^2(M;\mathbb Z)$ (74). For a complex line bundle $L$, choose a Hermitian product, i.e. a $U(1)$-structure $P\subset\operatorname{Fr}(L)$, and set $c_1(L):=c_1(P)$.
- **D2.4.6 — $Sp(1)$ and the quaternionic Hopf bundles** (unlabelled, pp. 25–26). $Sp(1):=\{q\in\mathbb H\mid q\bar q=1\}\cong SU(2)$; $Sp(1)$ acts freely and diagonally on $S^{4n+3}=\{(h_0,\dots,h_n)\in\mathbb H^{n+1}\mid\sum|h_i|^2=1\}$ giving principal $Sp(1)$-bundles $S^{4n+3}\to\mathbb{HP}^n$; the direct limit gives the classifying bundle $S^\infty\to\mathbb{HP}^\infty$. $\mathbb{HP}^\infty$ has exactly one cell in each dimension $4n$, so $H^\bullet(\mathbb{HP}^\infty;\mathbb Z)$ is generated by $b$ of degree 4, fixed by $\langle b,[\mathbb{HP}^1]\rangle=1$.
- **D2.4.7 — Second Chern class of an $Sp(1)$-bundle (topological definition)** (Definition 79, p. 26). Let $P\to M$ be a principal $Sp(1)$-bundle and $f\colon M\to\mathbb{HP}^\infty$ with $f^*S^\infty\cong P$. Then $c_2(P):=-f^*b\in H^4(M;\mathbb Z)$ is the second Chern class of $P$.

### Theorems
- **T2.4.1 — Classification theorem for principal bundles** (Theorem 70, p. 23). Let $P\to M$ be a (topological) principal $G$-bundle over a manifold $M$. Then there exists a continuous $f\colon M\to B$ such that $P\cong f^*E$; $f$ is unique up to homotopy, so $f\mapsto f^*E$ is a bijection between isomorphism classes of principal $G$-bundles over $M$ and $[M;B]$.
  `Proof in source: omitted/cited (to [GS99b, Thm. 1.1.1 and Rem. 2]).`
- **T2.4.2 — Properties of the first Chern class of line bundles** (Theorem 77, p. 25). (i) $c_1(\underline{\mathbb C})=0$ for the product bundle; (ii) $c_1(L_1\otimes L_2)=c_1(L_1)+c_1(L_2)$ for line bundles over the same base; (iii) $c_1(L^\vee)=-c_1(L)$, $L^\vee:=\operatorname{Hom}(L;\mathbb C)$; (iv) $c_1(f^*L)=f^*c_1(L)$ for all $L\to M$ and continuous $f\colon N\to M$.
  `Proof in source: omitted.`
- **T2.4.3 — $Sp(1)$-bundles over manifolds of dimension $\le3$ are trivial** (Proposition 78, p. 26). Let $M$ be a manifold of dimension at most 3. Any $Sp(1)$-bundle over $M$ is trivial.
  `Proof in source: full.` By Theorem 70 choose $f\colon M\to\mathbb{HP}^\infty$ with $f^*S^\infty\cong P$; $f$ is homotopic to a map $f_1$ into the 3-skeleton of $\mathbb{HP}^\infty$, which is a point; hence $P$ is trivial.
  `Gaps:` cellular approximation theorem used implicitly.

### Examples
- **E2.4.1 — Classification of line bundles on oriented 2-manifolds** (Example 72, p. 24). Let $M$ be an oriented 2-manifold. A continuous $f\colon M\to\mathbb{CP}^\infty$ is homotopic to a map into the 2-skeleton $\mathbb{CP}^1\subset\mathbb{CP}^\infty$, so $[M;\mathbb{CP}^\infty]=[M;\mathbb{CP}^1]$; $\mathbb{CP}^1\cong S^2$ topologically, and the degree map $[M;S^2]\to\mathbb Z$, $[f]\mapsto\deg f$, is a bijection. Thus a complex line bundle $L$ on an oriented 2-manifold is classified by an integer $d$, the degree of $L$.

### Exercises
- **X2.4.1** (Exercise 76, p. 25). Check that the first Chern class of $L$ does not depend on the choice of the Hermitian scalar product on $L$.

### Remarks / load-bearing paragraphs
- **R2.4.1 — Line bundles ↔ $U(1)$-bundles** (p. 24): by Exercise 29 the classification problems are equivalent; the $U(1)$-language is preferred.
- **R2.4.2 — Commutative ladder of inclusions** $S^3\subset S^5\subset\cdots\subset S^{2n+1}$ over $\mathbb{CP}^1\subset\mathbb{CP}^2\subset\cdots$ and its quaternionic analogue $S^7\subset S^{11}\subset\cdots$ over $\mathbb{HP}^1\subset\mathbb{HP}^2\subset\cdots$ (pp. 24, 26).
- **R2.4.3 — Chern classes for $U(r)$** (Remark 80, p. 26): for a principal $U(r)$-bundle one defines $c_1(P),\dots,c_r(P)$ with $c_j(P)\in H^{2j}(M;\mathbb Z)$; the above are the cases $r=1$ and (via $SU(2)$) $c_2$.
- **R2.4.4 — Characteristic classes vs. $[M;B]$** (p. 24): $[M;B]$ is hard to describe; characteristic classes are easier.

### External results imported without proof
- **I2.4.1 — Existence of classifying spaces for compact Lie groups** [GS99b, §1.2] (p. 23).
- **I2.4.2 — Classification theorem** [GS99b, Thm 1.1.1, Rem. 2] (Theorem 70, p. 23).
- **I2.4.3 — $S^\infty$ is contractible**; $\mathbb{CP}^\infty$ and $\mathbb{HP}^\infty$ are CW complexes (p. 24, 26).
- **I2.4.4 — Cellular approximation** (maps from a 2-manifold into $\mathbb{CP}^\infty$ deform into the 2-skeleton; maps from a $\le3$-manifold into $\mathbb{HP}^\infty$ deform into the 3-skeleton) (pp. 24, 26).
- **I2.4.5 — Hopf degree theorem**: $[M;S^2]\to\mathbb Z$, $[f]\mapsto\deg f$ is a bijection for a closed oriented 2-manifold $M$ (p. 24).
- **I2.4.6 — $H^\bullet(\mathbb{CP}^\infty;\mathbb Z)=\mathbb Z[a]$, $H^\bullet(\mathbb{HP}^\infty;\mathbb Z)=\mathbb Z[b]$** ("easy to see" / from the cell structure) (pp. 25–26).
- **I2.4.7 — Properties of $c_1$** (Theorem 77) stated without proof (p. 25).

---

## 3.1 The Chern–Weil theory

`PDF pages: 26–30`

### Standing conventions and notation
- Ground field: $\mathbb C$ is chosen "for definiteness"; the real case is analogous (p. 26).
- $p\colon\mathfrak g\to\mathbb C$ an ad-invariant homogeneous polynomial of degree $d$ (three defining conditions, p. 26–27). The same letter $p$ denotes the associated symmetric $d$-multilinear form $p\colon\operatorname{Sym}^d(\mathfrak g)\to\mathbb R$ whose diagonal restriction is $p$ (p. 27).
- Curvature $\pi^*F_a=da+\tfrac12[a\wedge a]$ viewed as a matrix of 2-forms on $P$; $\hat F_A:=\pi^*F_A$ (p. 27).
- Even-degree forms commute, so $p(\pi^*F_a)$ makes sense (p. 27).
- $c_j$ for $\mathfrak u(r)$: $\det(\lambda\mathbf 1+\tfrac{i}{2\pi}\xi)=\lambda^r+c_1(\xi)\lambda^{r-1}+\dots+c_r(\xi)$ (Example 81(b)), real-valued (p. 27).
- $H^{2j}_{dR}(M;\mathbb R)$ de Rham cohomology; $c(P):=1+c_1(P)+\dots+c_r(P)$ total Chern class (p. 28).
- $I=[0,1]$; $\iota_0,\iota_1\colon M\to M\times I$ endpoint inclusions; $\varpi\colon M\times I\to M$ projection; $A_t:=(1-t)A_0+tA_1$ (p. 28).
- $\mathcal O(-1)$ tautological bundle over $\mathbb P^1$ ($=\mathbb{CP}^1$); $\mathbb P^N=\mathbb{CP}^N$; $a$ the generator with (73) (p. 29).
- $\operatorname{Fr}_U$: the principal $U(r)$-bundle of unitary frames of a Hermitian bundle $E$ (Remark 86, p. 28).

### Definitions
- **D3.1.1 — Ad-invariant homogeneous polynomial of degree $d$** (unlabelled, pp. 26–27). $p\colon\mathfrak g\to\mathbb C$ such that: (1) for a basis $\xi_1,\dots,\xi_n$ of $\mathfrak g$, $p(x_1\xi_1+\dots+x_n\xi_n)$ is a polynomial of degree $d$ in $x_1,\dots,x_n$; (2) $p(\operatorname{ad}_g\xi)=p(\xi)$ for all $g\in G$, $\xi\in\mathfrak g$; (3) $p(\lambda\xi)=\lambda^dp(\xi)$ for all $\lambda\in\mathbb R$, $\xi\in\mathfrak g$.
- **D3.1.2 — Chern–Weil form $p(F_a)$** (unlabelled, p. 27). For a principal $G$-bundle $P\to M$ with connection $a$, $p(\pi^*F_a)$ is a real-valued (source: "$\mathbb R$-valued") form of degree $2d$ on $P$; it is basic (entries of $\pi^*F_a$ are basic) and $G$-invariant (ad-invariance of $p$); by Proposition 39 with the trivial representation there is a unique $p(F_a)\in\Omega^{2d}(M)$ with $\pi^*p(F_a)=p(\pi^*F_a)$.
- **D3.1.3 — Chern classes and total Chern class (Chern–Weil definition)** (Definition 84, p. 28). Let $P\to M$ be a principal $U(r)$-bundle with connection $A$ and $c_j$ the degree-$j$ polynomial of Example 81(b). The class $c_j(P):=[c_j(F_A)]\in H^{2j}_{dR}(M;\mathbb R)$ is the $j$-th Chern class of $P$, and $c(P):=1+c_1(P)+\dots+c_r(P)\in H^\bullet(M;\mathbb R)$ is the total Chern class of $P$.
- **D3.1.4 — Chern classes of a complex vector bundle** (Remark 86, p. 28). For a complex vector bundle $E$ of rank $r$, choose a fibrewise Hermitian structure to get the principal $U(r)$-bundle $\operatorname{Fr}_U$ and set $c_j(E):=c_j(\operatorname{Fr}_U)$; "easy to show" this is independent of the Hermitian structure.

### Theorems
- **T3.1.1 — Chern–Weil lemma: closedness and independence of the connection** (Lemma 82, p. 27). (i) $p(F_a)$ is closed; (ii) the de Rham cohomology class of $p(F_a)$ does not depend on the choice of the connection $a$.
  `Proof in source: full for (i); (ii) full modulo a cited homotopy-operator lemma.` Step 1 (proof of (i)): for $\xi,\xi_1,\dots,\xi_d\in\mathfrak g$ (matrix Lie algebra, $\operatorname{ad}_{e^{t\xi}}\xi_j=e^{t\xi}\xi_je^{-t\xi}$), differentiating $p(e^{t\xi}\xi_1e^{-t\xi},\dots,e^{t\xi}\xi_de^{-t\xi})=p(\xi_1,\dots,\xi_d)$ at $t=0$ gives the infinitesimal invariance
$$p([\xi,\xi_1],\xi_2,\dots,\xi_d)+p(\xi_1,[\xi,\xi_2],\dots,\xi_d)+\dots+p(\xi_1,\dots,[\xi,\xi_d])=0.\qquad(83)$$
With $\hat F_A:=\pi^*F_A$, (83) implies $p([\hat F_A\wedge A],\hat F_A,\dots)+p(\hat F_A,[\hat F_A\wedge A],\dots)+\dots=0$; then $d(p(\hat F_A))=\sum_jp(\hat F_A,\dots,d\hat F_A,\dots,\hat F_A)=\sum_jp(\hat F_A,\dots,[\hat F_A\wedge A],\dots)=0$ using the Bianchi identity (55). Step 2: there exist linear maps $Q\colon\Omega^k(M\times I)\to\Omega^{k-1}(M)$ with $\iota_1^*\omega-\iota_0^*\omega=dQ\omega-Qd\omega$ for all $\omega\in\Omega^k(M\times I)$; "the argument goes just like in the proof of the Poincaré lemma", [BT82, Prop. 4.1.1], details omitted. Step 3 (proof of (ii)): for connections $A_0,A_1$ regard $A_t:=(1-t)A_0+tA_1$ as a connection on $\varpi^*P\to M\times I$; then $p(F_{A_1})-p(F_{A_0})=\iota_1^*p(F_{A_t})-\iota_0^*p(F_{A_t})=dQp(F_{A_t})$ since $p(F_{A_t})$ is closed.
  `Gaps:` the passage from (83) for Lie algebra elements to the identity for $\mathfrak g$-valued forms (with signs for even-degree forms) is asserted; Step 2 cited; the fact that $A_t$ is a connection on $\varpi^*P$ is not checked.
- **T3.1.2 — Axiomatic properties of Chern classes** (Theorem 87, pp. 28–29). The Chern classes satisfy: (i) $c_0(E)=1$ for any vector bundle $E$; (ii) (naturality) $c(f^*E)=f^*c(E)$ for all vector bundles $E\to M$ and maps $f\colon N\to M$; (iii) (Whitney sum formula) $c(E_1\oplus E_2)=c(E_1)\cup c(E_2)$; (iv) (normalisation) $c(\mathcal O(-1))=1-a$, where $\mathcal O(-1)$ is the tautological line bundle over $\mathbb P^1$ and $a$ is the generator of $H^2(\mathbb P^1)$ with (73).
  `Proof in source: full (short).` (i) is the definition. Naturality follows from Proposition 56 ($F_{f^*A}=f^*F_A$). Normalisation is equivalent to $\tfrac{i}{2\pi}\int_{\mathbb P^1}F_a=-1$ for a unitary connection $a$ on $\mathcal O(-1)$, "established in Example 51" (where $\int F_a=2\pi i$, so $\tfrac{i}{2\pi}\cdot2\pi i=-1$). Whitney sum: for unitary connections $\nabla_1,\nabla_2$ the curvature of $\nabla_1\oplus\nabla_2$ is block diagonal with values in $\operatorname{End}(E_1)\oplus\operatorname{End}(E_2)$, and $\det\begin{pmatrix}A&0\\0&B\end{pmatrix}=\det A\det B$ gives $c(F_{\nabla_1\oplus\nabla_2})=\det\begin{pmatrix}1+\tfrac{i}{2\pi}F_{\nabla_1}&0\\0&1+\tfrac{i}{2\pi}F_{\nabla_2}\end{pmatrix}=c(F_{\nabla_1})\wedge c(F_{\nabla_2})$.
  `Gaps:` identification of the Hopf connection of Example 51 with a unitary connection on $\mathcal O(-1)$ over $\mathbb P^1$ relies on Exercise 44; the determinant identity for matrices of even forms is asserted.
- **T3.1.3 — Agreement of the two definitions of $c_1$ for line bundles** (Theorem 90, p. 29). Let $L$ be a complex line bundle. Then the first Chern class in the sense of Definition 84 (Chern–Weil) coincides with the image in $H^2_{dR}(M;\mathbb R)$ of the first Chern class in the sense of Definition 75 (topological).
  `Proof in source: sketch.` "Not too hard to show" there is $N<\infty$ and a smooth $f\colon M\to\mathbb P^N$ with $f^*\mathcal O(-1)\cong L$. $H^2_{dR}(\mathbb P^N;\mathbb R)$ is one-dimensional, generated by the class Poincaré dual to $[\mathbb P^1]$ for the standard embedding $\iota\colon\mathbb P^1\subset\mathbb P^N$. Pick a Hermitian structure and connection $\nabla$ on $\mathcal O(-1)$; $\iota^*\mathcal O(-1)$ is the tautological bundle of $\mathbb P^1$, so $\tfrac{i}{2\pi}\iota^*F_\nabla$ represents $c_1(\mathcal O_{\mathbb P^1}(-1))$ and by Example 51 $\langle[\tfrac{i}{2\pi}\iota^*F_\nabla],[\mathbb P^1]\rangle=-1$. Hence $c_1(\mathcal O(-1))=-a$ and $c_1(L)=c_1(f^*L)=-f^*a$.
  `Gaps:` existence of a smooth classifying map into a finite $\mathbb P^N$ (finite-dimensional approximation); the identification of the de Rham generator with the integral generator $a$; naturality for both definitions used implicitly.

### Examples
- **E3.1.1 — Invariant polynomials on $\mathfrak u(r)$** (Example 81, p. 27). (a) For $\mathfrak g=\mathfrak u(r)$, $p_d(\xi)=i\operatorname{tr}\xi^d$ is an ad-invariant polynomial of degree $d$ (as printed; the factor $i$ is presumably meant to make the $d=1$ case real). (b) For $\mathfrak g=\mathfrak u(r)$ define $c_1,\dots,c_r$ of degrees $1,\dots,r$ by $\det(\lambda\mathbf 1+\tfrac{i}{2\pi}\xi)=\lambda^r+c_1(\xi)\lambda^{r-1}+\dots+c_r(\xi)$; e.g. $c_r(\xi)=\tfrac{i^r}{(2\pi)^r}\det\xi$ and $c_1(\xi)=\tfrac{i}{2\pi}\operatorname{tr}\xi$. The equality $\det(\lambda\mathbf 1+\tfrac{i}{2\pi}\xi)=\overline{\det(\bar\lambda\mathbf 1+\tfrac{i}{2\pi}\xi)}$ (for $\xi$ skew-Hermitian) implies each $c_j$ is real-valued.

### Exercises
- **X3.1.1** (Exercise 88, p. 29). Let $E$ be a vector bundle. Prove: (a) the Chern classes depend on the isomorphism class of $E$ only; (b) $c_j(E^\vee)=(-1)^jc_j(E)$ for all $j$; (c) if $E$ is trivial then $c(E)=1$; (d) if $E\cong E_1\oplus\underline{\mathbb C}^k$, then $c_j(E)=0$ for $j>\operatorname{rk}E-k$.
- **X3.1.2** (Exercise 89, p. 29). Show that the tangent bundle of $S^2$ is non-trivial (now via Chern classes).

### Remarks / load-bearing paragraphs
- **R3.1.1 — Construction of $p(F_a)$ on $M$** (p. 27): matrix of 2-forms; even forms commute; basic + invariant ⇒ descends via Prop. 39 (trivial representation).
- **R3.1.2 — Integrality** (Remark 85, p. 28). Definition 84 gives classes in de Rham cohomology only; in fact they lie in the image of $H^\bullet(M;\mathbb Z)\to H^\bullet_{dR}(M;\mathbb R)$; discussed for $c_1,c_2$ below; the two a priori unrelated definitions of $c_1,c_2$ will be shown to agree.
- **R3.1.3 — Names of the axioms** (p. 29): (ii) naturality, (iii) Whitney sum formula, (iv) normalisation.
- **R3.1.4 — $SU(2)$ and Grassmannians** (Remark 91, p. 30). Arguing similarly, for $SU(2)$-bundles the two definitions of $c_2$ agree in de Rham cohomology (details left to reader). The infinite Grassmannian $\operatorname{Gr}_k(\mathbb C^\infty)$ is a classifying space for $U(k)$, so Chern classes could be defined as pull-backs of classes on $\operatorname{Gr}_k(\mathbb C^\infty)$.
- **R3.1.5 — Integrality of $\tfrac{i}{2\pi}\int h^*F_\nabla$ and the degree** (Remark 92, p. 30). For a Hermitian line bundle $L\to M$ with Hermitian connection $\nabla$ and $h\colon\Sigma\to M$ from a compact oriented 2-manifold, $\tfrac{i}{2\pi}\int_\Sigma h^*F_\nabla\in\mathbb Z$ (the source prints $\int_M$; the integral is over $\Sigma$). In particular for $M$ itself a compact oriented 2-manifold, $\tfrac{i}{2\pi}\int_MF_A$ is an integer equal to the degree of $L$ (Example 72).
- **R3.1.6 — $c_2$ of an $SU(2)$-bundle via $\operatorname{tr}(F\wedge F)$** (Remark 93, p. 30). For $\xi\in\mathfrak{su}(2)$, $\operatorname{tr}\xi^2=-2\det\xi$ ("straightforward computation"). Hence for an $SU(2)$-bundle $P$: $c_2(P)=\tfrac1{8\pi^2}[\operatorname{tr}(F_A\wedge F_A)]\in H^4_{dR}(M;\mathbb R)$. If $M$ is a closed oriented 4-manifold, integration gives $H^4_{dR}(M;\mathbb R)\cong\mathbb R$ and
$$c_2(P)=\frac1{8\pi^2}\int_M\operatorname{tr}(F_A\wedge F_A)\in\mathbb Z.\qquad(94)$$
(Derivation: $c_2(\xi)=\tfrac{i^2}{(2\pi)^2}\det\xi=-\tfrac1{4\pi^2}\det\xi=\tfrac1{8\pi^2}\operatorname{tr}\xi^2$.)

### External results imported without proof
- **I3.1.1 — Homotopy operator / Poincaré lemma argument** [BT82, Prop. 4.1.1]: $Q\colon\Omega^k(M\times I)\to\Omega^{k-1}(M)$ with $\iota_1^*-\iota_0^*=dQ-Qd$ (p. 28).
- **I3.1.2 — Finite-dimensional classifying map**: any line bundle over $M$ is $f^*\mathcal O(-1)$ for a smooth $f\colon M\to\mathbb P^N$, some $N<\infty$ (p. 29, "not too hard to show").
- **I3.1.3 — $H^2_{dR}(\mathbb P^N;\mathbb R)\cong\mathbb R$ generated by the Poincaré dual of $[\mathbb P^1]$** (p. 29).
- **I3.1.4 — Integrality of Chern–Weil classes** (Remark 85, p. 28; Remarks 92–93, p. 30) stated as facts.
- **I3.1.5 — $\operatorname{Gr}_k(\mathbb C^\infty)$ classifies $U(k)$** (Remark 91, p. 30).

---

## 3.2 The Chern–Simons functional

`PDF pages: 30–31`

### Standing conventions and notation
- Dimension three, $G=SU(2)$; $M$ a closed oriented 3-manifold; $P\to M$ an $SU(2)$-bundle, trivial by Proposition 78 (p. 30).
- $X$ a compact oriented 4-manifold with $\partial X=M$; $P_X$ an extension of $P$ ($P_X|_M=P$); $A_X$ an extension of $A$ (p. 30).
- Gluing convention: when gluing $X$ and $X'$ along $M$, the orientation of $X'$ is reversed so that $\partial X'=-M$ (p. 30).
- Chern–Simons functional $\vartheta\colon\mathcal A(P)\to\mathbb R/\mathbb Z$ (95); with a trivialisation, $A\in\Omega^1(M;\mathfrak{su}(2))$ (p. 31).
- Gauge transformations are maps $g\colon M\to SU(2)\cong S^3$ with degree $\deg g$ (Exercise 96(d)).

### Definitions
- **D3.2.1 — Chern–Simons functional (4-dimensional definition)** (equation (95), pp. 30–31). For a connection $A$ on $P\to M^3$, choose $(X,P_X,A_X)$ extending $(M,P,A)$ and set
$$\vartheta(A):=\frac1{8\pi^2}\int_X\operatorname{tr}(F_{A_X}\wedge F_{A_X})\in\mathbb R/\mathbb Z.\qquad(95)$$
Well defined modulo $\mathbb Z$: for another extension $(X',P'_X,A'_X)$, glue $X\cup_M\overline{X'}$ to a closed oriented 4-manifold; by (94) the difference of the two integrals is an integer.
- **D3.2.2 — Chern–Simons functional (3-dimensional formula)** (unlabelled, p. 31). Choosing a trivialisation of $P$, $A\in\Omega^1(M;\mathfrak{su}(2))$ and
$$\vartheta(A)=\frac1{8\pi^2}\int_M\operatorname{tr}\Big(A\wedge dA+\frac23A\wedge A\wedge A\Big).$$
This is not $\mathbb R$-valued: changing the trivialisation changes the value by an integer.
- **D3.2.3 — Flat connection** (in Proposition 98, p. 31). A connection $A$ with $F_A=0$.

### Theorems
- **T3.2.1 — Critical points of Chern–Simons are flat connections** (Proposition 98, p. 31). The critical points of the Chern–Simons functional are exactly the flat connections, i.e. connections $A$ with $F_A=0$.
  `Proof in source: full (via the differential computation R3.2.2).` For $a\in\Omega^1(M;\mathfrak{su}(2))$: $d\vartheta_A(a)=\tfrac1{8\pi^2}\int_M\operatorname{tr}(a\wedge dA+A\wedge da+2a\wedge A\wedge A)=\tfrac1{4\pi^2}\int_M\operatorname{tr}(F_A\wedge a)$, using integration by parts in the second equality. Hence $d\vartheta_A=0$ iff $F_A=0$ (non-degeneracy of $\operatorname{tr}$ and of the pairing).
  `Gaps:` the integration-by-parts step and the identity $\operatorname{tr}(a\wedge A\wedge A)$-manipulations not written; the "iff" direction uses non-degeneracy of $\int\operatorname{tr}(\cdot\wedge\cdot)$.

### Examples: none.

### Exercises
- **X3.2.1** (Exercise 96, p. 31). (a) For $A\in\Omega^1(X;\mathfrak{su}(2))$ on a 4-manifold $X$, prove
$$d\operatorname{tr}\Big(A\wedge dA+\frac23A\wedge A\wedge A\Big)=\operatorname{tr}(F_A\wedge F_A).\qquad(97)$$
In the special case $X=M\times\mathbb R$, with $A_t$ the pull-back of $A$ to $M\times\{t\}$, (97) implies $\vartheta(A_t)-\vartheta(A_{t_0})=\int_{M\times[t_0,t]}\operatorname{tr}(F_A\wedge F_A)$ (the source omits the $\tfrac1{8\pi^2}$ here). (b) Prove that the two definitions of the Chern–Simons functional agree. (c) Prove that the values of $\vartheta$ with respect to two different trivialisations differ by an integer. (d) Let $g$ be a gauge transformation, thought of as a map $M\to SU(2)\cong S^3$; show $\vartheta(A\cdot g)=\vartheta(A)+\deg g$.

### Remarks / load-bearing paragraphs
- **R3.2.1 — Well-definedness of (95) mod $\mathbb Z$** (pp. 30–31): closed oriented 3-manifolds bound; glue two extensions with orientation reversal; apply (94).
- **R3.2.2 — Differential of $\vartheta$** (p. 31): $d\vartheta_A(a)=\tfrac1{4\pi^2}\int_M\operatorname{tr}(F_A\wedge a)$.
- **R3.2.3 — Relation to Chern–Weil vs. direct computability** (p. 31).

### External results imported without proof
- **I3.2.1 — Every closed oriented 3-manifold bounds a compact oriented 4-manifold** (p. 30, "as a matter of fact"; Rokhlin/Thom).
- **I3.2.2 — Extension of $P$ and $A$ over $X$ assumed** ("assume there is an extension"; for $SU(2)$ over a 3-manifold $P$ is trivial so extension of the bundle is automatic; extension of the connection is asserted) (p. 30).
- **I3.2.3 — Integrality (94)** used from §3.1.

---

## 3.3 The moduli space of flat connections

`PDF pages: 32–34`

### Standing conventions and notation
- $\mathcal A^\flat(P)$ = space of flat connections on $P$; $\mathcal M^\flat(P):=\mathcal A^\flat(P)/\mathcal G(P)$ (p. 32). Any manifold, any structure group (restrictions of §3.2 dropped).
- Curves $\gamma\colon[0,1]\to M$ smooth; $\gamma^*\nabla$ on $\gamma^*E$; trivialise $\gamma^*E\cong\mathbb R^k\times[0,1]$ so $\gamma^*\nabla=\tfrac d{dt}+B(t)dt$ with $B\colon[0,1]\to M_k(\mathbb R)$ (the source then writes $\dot s+A(t)s=0$, using $A$ for $B$) (p. 32).
- $PT_\gamma\colon E_{\gamma(0)}\to E_{\gamma(1)}$ parallel transport; $\operatorname{Hol}_m(\nabla)\subset GL(E_m)$; after a basis choice $\operatorname{Hol}(\nabla)\subset GL_k(\mathbb R)$ up to conjugacy (pp. 32–33).
- $\rho_A\colon\pi_1(M)\to GL_k(\mathbb R)$ monodromy representation of a flat connection $A$ (p. 33).
- $\tilde M$ universal cover, $\pi_1(M)$ acting by deck transformations; $\tilde M$ viewed as a principal $\pi_1(M)$-bundle (p. 33).
- Representation variety $\mathcal R(M;G):=\{\rho\colon\pi_1(M)\to G\text{ homomorphism}\}/\text{Conj}$ (p. 34).

### Definitions
- **D3.3.1 — Moduli space of flat connections** (unlabelled, p. 32). $\mathcal M^\flat(P):=\mathcal A^\flat(P)/\mathcal G(P)$ where $\mathcal A^\flat(P)$ is the space of flat connections; $\mathcal G(P)$ acts on $\mathcal A^\flat(P)$ (curvature transforms by conjugation).
- **D3.3.2 — Parallel section along a curve** (unlabelled, p. 32). For $\gamma\colon[0,1]\to M$ smooth, a section $s\in\Gamma(\gamma^*E)$ is parallel along $\gamma$ if $(\gamma^*\nabla)(s)=0$; in a trivialisation this is the linear ODE $\dot s+A(t)s(t)=0$.
- **D3.3.3 — Parallel transport** (Definition 100, p. 32). If $s\in\Gamma(\gamma^*E)$ is parallel along $\gamma$, then $s(1)\in E_{\gamma(1)}$ is called the parallel transport of $s(0)=s_0\in E_{\gamma(0)}$ with respect to $\nabla$. By existence/uniqueness for linear ODEs this defines a linear isomorphism $PT_\gamma\colon E_{\gamma(0)}\to E_{\gamma(1)}$, the parallel transport.
- **D3.3.4 — Holonomy group** (Definition 101, p. 33). Pick $m\in M$. $\operatorname{Hol}_m(\nabla):=\{PT_\gamma\in GL(E_m)\mid\gamma\text{ a loop based at }m\}$ is the holonomy group of $\nabla$ based at $m$ (a group since concatenation of loops corresponds to composition of parallel transports). Choosing a basis of $E_m$, $\operatorname{Hol}_m(\nabla)\subset GL_k(\mathbb R)$; for $m,m'$ in the same component the groups are conjugate, so the basepoint is dropped and $\operatorname{Hol}(\nabla)$ is regarded as a subgroup of $GL_k(\mathbb R)$ defined up to conjugacy.
- **D3.3.5 — Monodromy representation of a flat connection** (unlabelled, p. 33). For $\nabla$ flat on $E$ of rank $k$, $\gamma\mapsto\operatorname{Hol}(\nabla;\gamma)$ for loops $\gamma$ at $m$ depends only on the homotopy class of $\gamma$ [KN96, II.9], giving $\rho_A\colon\pi_1(M)\to GL_k(\mathbb R)$.
- **D3.3.6 — Flat bundle from a representation** (unlabelled, pp. 33–34). Given $\rho\colon\pi_1(M)\to GL_k(\mathbb R)$ (the source writes "$\rho\colon\tilde M\to GL_k(\mathbb R)$", a typo), $E:=\tilde M\times_{\pi_1(M),\rho}\mathbb R^k$, the bundle associated to the principal $\pi_1(M)$-bundle $\tilde M$. Its natural flat connection: interpreting $s\in\Gamma(E)$ as a $\pi_1(M)$-equivariant $\hat s\colon\tilde M\to\mathbb R^k$, define $\nabla s$ by $\pi^*\nabla s=d\hat s$ (cf. (47)).
- **D3.3.7 — Representation variety** (unlabelled, p. 34). $\mathcal R(M;GL_k(\mathbb R)):=\{\rho\colon\pi_1(M)\to GL_k(\mathbb R)\text{ group homomorphism}\}/\text{Conj}$, two representations equivalent if conjugate. Likewise $\mathcal R(M;O(k))$, $\mathcal R(M;U(k))$, $\mathcal R(M;G)$ (Remark 105).

### Theorems
- **T3.3.1 — Flat connections ↔ representations** (unlabelled, p. 34). The constructions D3.3.5 and D3.3.6 establish a bijective correspondence between the moduli space of flat connections $\mathcal M^\flat$ (on rank-$k$ real vector bundles over $M$, all bundles at once) and the representation variety $\mathcal R(M;GL_k(\mathbb R))$.
  `Proof in source: sketch` — the two constructions are given; that they are mutually inverse and that gauge equivalence ↔ conjugacy (Exercise 104) are not written.
- **T3.3.2 — Compactness of the moduli space of flat $G$-connections** (Proposition 106, p. 34). Let $M$ be a manifold. If $G$ is a compact Lie group, then the space $\mathcal M^\flat$ of all flat $G$-connections is compact.
  `Proof in source: sketch (one paragraph before the statement).` $\pi_1(M)$ is finitely presented; choose generators $\gamma_1,\dots,\gamma_N$; a representation is determined by $g_i=\rho(\gamma_i)\in G$ satisfying finitely many relations, so $\mathcal R(M;G)\subset G^N/G$ ($G$ acting diagonally by conjugation) as a closed subset of a compact space.
  `Gaps:` closedness of the relation locus and Hausdorffness of $G^N/G$ not discussed; identification $\mathcal M^\flat=\mathcal R(M;G)$ for principal bundles left to the reader (Remark 105).

### Examples
- **E3.3.1 — Flat $U(1)$-connections on the torus** (Example 107, p. 34). For $M=T^n$: $\mathcal R(T^n;U(1))=\operatorname{Hom}(\mathbb Z^n,U(1))=U(1)^n\cong T^n$ (the source writes $\operatorname{Hom}(T^n,U(1))$, meaning $\operatorname{Hom}(\pi_1(T^n),U(1))$).
- **E3.3.2 — Representation varieties of surface groups** (Example 108, p. 34). For $\Sigma$ a closed Riemann surface of genus $\gamma$, $\pi_1(\Sigma)\cong\langle a_1,\dots,a_\gamma,b_1,\dots,b_\gamma\mid\prod_i[a_i,b_i]=1\rangle$, hence $\mathcal R(\Sigma,G)=\{A_1,\dots,A_\gamma,B_1,\dots,B_\gamma\in G\mid\prod_i[A_i,B_i]=1\}/G$. For $G=SL(n;\mathbb C)$ this has a rich structure (Higgs bundles; [BGPG07, Got14, Ray18]).

### Exercises
- **X3.3.1** (Exercise 102, p. 33). Show: $\nabla$ Euclidean ⇒ $PT_\gamma$ orthogonal ⇒ $\operatorname{Hol}(\nabla)\subset O(k)$; $\nabla$ complex ⇒ $PT_\gamma$ complex linear ⇒ $\operatorname{Hol}(\nabla)\subset GL_{k/2}(\mathbb C)$; $\nabla$ complex Hermitian ⇒ $PT_\gamma$ unitary ⇒ $\operatorname{Hol}(\nabla)\subset U(k/2)$.
- **X3.3.2** (Exercise 104, p. 33). Show that a gauge-equivalent flat connection yields a conjugate monodromy representation.

### Remarks / load-bearing paragraphs
- **R3.3.1 — Motivation: why study $\mathcal M^\flat$** (p. 32). Compactness? Manifold? It is the space of solutions of a nonlinear PDE modulo an equivalence relation; two reasons of interest: encodes subtle information on $M$ (and $P$), and carries extra structure.
- **R3.3.2 — Parallel sections as an ODE; existence and uniqueness** (p. 32): trivialise $\gamma^*E$ (bundles over an interval are trivial); parallel ⇔ $\dot s+A(t)s=0$; unique global solution on $[0,1]$ by the main theorem of ODEs.
- **R3.3.3 — Parallel along an embedded curve** (Remark 99, p. 32): if $\gamma$ is simple embedded, $s$ can be seen as a section of $E$ along the image.
- **R3.3.4 — Holonomy groups at different basepoints are conjugate** (p. 33): "a standard argument" (conjugate by parallel transport along a path from $m$ to $m'$).
- **R3.3.5 — Parallel transport on principal bundles** (Remark 103, p. 33): analogous, details left to the reader.
- **R3.3.6 — Euclidean/Hermitian/principal variants** (Remark 105, p. 34): cosmetic changes give $\mathcal R(M;O(k))$, $\mathcal R(M;U(k))$, $\mathcal R(M;G)$.
- **R3.3.7 — $\mathcal R(M;G)\subset G^N/G$** (p. 34): from finite presentation of $\pi_1(M)$.

### External results imported without proof
- **I3.3.1 — Existence and uniqueness for linear ODEs on $[0,1]$** ("main theorem of ordinary differential equations") (p. 32).
- **I3.3.2 — Any bundle over an interval is trivial** (p. 32).
- **I3.3.3 — Holonomy of a flat connection depends only on the homotopy class of the loop** [KN96, II.9] (p. 33).
- **I3.3.4 — Fundamental groups of manifolds are finitely presented** (p. 34).
- **I3.3.5 — Presentation of surface groups** $\langle a_i,b_i\mid\prod[a_i,b_i]=1\rangle$ (p. 34).

---

## 4.1 Spin groups and Clifford algebras

`PDF pages: 34–36`

### Standing conventions and notation
- Throughout §4, $n\ge3$ (so that $\pi_1(SO(n))\cong\mathbb Z/2\mathbb Z$); dimension 2 needs separate treatment (Remark 129) (pp. 34, 41).
- $\operatorname{Im}\mathbb H=\{h\mid\bar h=-h\}\cong\mathbb R^3$; $\mathbb R^4\cong\mathbb H$ (p. 35).
- $\alpha\colon Sp(1)\to SO(3)$, $q\mapsto A_q$, $A_qh=qh\bar q$ (109) (p. 35).
- $Sp_\pm(1)=Sp(1)$ (footnote 3: the subscripts distinguish the two factors); $\beta\colon Sp_+(1)\times Sp_-(1)\to SO(4)$, $(q_+,q_-)\mapsto A_{q_+,q_-}$, $A_{q_+,q_-}h=q_+h\bar q_-$ (p. 35).
- Hodge splitting $\Lambda^2(\mathbb R^4)^*=\Lambda^2_+\oplus\Lambda^2_-$, $\Lambda^2_\pm=\{\omega\mid*\omega=\pm\omega\}$; $\mathfrak{so}(4)\cong\Lambda^2(\mathbb R^4)^*\cong\mathfrak{so}(3)\oplus\mathfrak{so}(3)$ (p. 35).
- **Clifford relation:** $Cl(U):=TU/(u\otimes u+|u|^2\cdot1)$, i.e. $u\cdot u=-|u|^2$; generators $e_i$ with $e_i^2=-1$, $e_ie_j=-e_je_i$ ($i\ne j$) (p. 35).
- $Cl(U)$-module: $U\otimes V\to V$, $u\otimes v\mapsto u\cdot v$ with $u\cdot(u\cdot v)=-|u|^2v$ (p. 35).
- $\slashed S$ denotes the spinor representation (and later the spinor bundle); $\slashed S\cong\mathbb H$ for $Sp(1)=Spin(3)$ with left multiplication; complex structure on $\slashed S$ by **right** multiplication by $\bar i=-i$ (p. 36). $\operatorname{End}_0(\slashed S)$ traceless endomorphisms.
- $\slashed S^\pm$ = fundamental representation of $Sp_\pm(1)$; $\slashed S^+\oplus\slashed S^-$ a $Cl(\mathbb R^4)$-module via (112) (p. 36).

### Definitions
- **D4.1.1 — Spin group $Spin(n)$** (unlabelled, pp. 34–35). Since $\pi_1(SO(n))\cong\mathbb Z/2\mathbb Z$ for $n\ge3$, there is a simply connected Lie group $Spin(n)$ with a homomorphism $Spin(n)\to SO(n)$ which is a double covering; this characterises $Spin(n)$ up to isomorphism.
- **D4.1.2 — Clifford algebra** (unlabelled, p. 35). For a Euclidean vector space $U$, $Cl(U)$ is the tensor algebra $TU=\mathbb R\oplus U\oplus U\otimes U\oplus\cdots$ modulo the ideal generated by $u\otimes u+|u|^2\cdot1$; equivalently generated by $U$ subject to $u\cdot u=-|u|^2$. $Cl(\mathbb R^n)$ is generated by $1,e_1,\dots,e_n$ with $e_i^2=-1$, $e_ie_j=-e_je_i$ for $i\ne j$.
- **D4.1.3 — Clifford module** (unlabelled, p. 35). A vector space $V$ with a map $U\otimes V\to V$, $u\otimes v\mapsto u\cdot v$, satisfying $u\cdot(u\cdot v)=-|u|^2v$ for all $u\in U$, $v\in V$.
- **D4.1.4 — Spinor representations $\slashed S$, $\slashed S^\pm$ in dimensions 3 and 4** (unlabelled, p. 36). $\slashed S\cong\mathbb H$, the fundamental representation of $Sp(1)\cong Spin(3)$ by left multiplication, a $Cl(\mathbb R^3)$-module via $\operatorname{Im}\mathbb H\otimes\slashed S\to\slashed S$; complex Hermitian via right multiplication by $\bar i$. $\slashed S^\pm$ the fundamental representations of $Sp_\pm(1)$; $\slashed S^+\oplus\slashed S^-$ is a $Cl(\mathbb R^4)$-module via (112).

### Theorems
- **T4.1.1 — $Spin(3)\cong Sp(1)$** (unlabelled, p. 35). The homomorphism $\alpha\colon Sp(1)\to SO(3)$, $A_qh=qh\bar q$ on $\operatorname{Im}\mathbb H\cong\mathbb R^3$, is a non-trivial double covering with $\ker\alpha=\{\pm1\}$; hence $Spin(3)\cong Sp(1)$.
  `Proof in source: full (short).` $Sp(1)\cong SU(2)\cong S^3$ is connected and simply connected; the Lie algebra map of $\alpha$ is an isomorphism ("easy to check"); $SO(3)$ connected ⇒ $\alpha$ surjective; $\ker\alpha=\{\pm1\}$.
- **T4.1.2 — $Spin(4)\cong Sp(1)\times Sp(1)$** (unlabelled, p. 35). $\beta\colon Sp_+(1)\times Sp_-(1)\to SO(4)$, $A_{q_+,q_-}h=q_+h\bar q_-$ on $\mathbb H\cong\mathbb R^4$, has $\ker\beta=\{\pm(1,1)\}\cong\mathbb Z/2\mathbb Z$ and is a double covering; hence $Sp_+(1)\times Sp_-(1)\cong Spin(4)$.
  `Proof in source: full (short).` The adjoint representation and $\mathfrak{so}(4)\cong\mathfrak{so}(3)\oplus\mathfrak{so}(3)$ give $SO(4)\to SO(3)\times SO(3)$; "an explicit computation" shows the composite $Sp_+(1)\times Sp_-(1)\to SO(4)\to SO(3)\times SO(3)$ is $(q_+,q_-)\mapsto(A_{q_+},A_{q_-})$; so the Lie algebra map of $\beta$ is an isomorphism and $\ker\beta\subset\{(\pm1,\pm1)\}$; "readily checked" $\ker\beta=\{\pm(1,1)\}$.
  `Gaps:` the explicit computation and the kernel check are not written.
- **T4.1.3 — $\operatorname{Im}\mathbb H\otimes\mathbb C\cong\operatorname{End}_0(\slashed S)$** (equation (111), p. 36). As $Sp(1)$-representations (left side via $\alpha$), $\operatorname{Im}\mathbb H\otimes\mathbb C\cong\operatorname{End}_0(\slashed S)$; the real subspace $\operatorname{Im}\mathbb H$ corresponds to traceless Hermitian endomorphisms.
  `Proof in source: omitted ("elementary exercise in representation theory").`
- **T4.1.4 — $\mathbb H\otimes\mathbb C\cong\operatorname{Hom}(\slashed S^+;\slashed S^-)$** (unlabelled, p. 36). As $Spin(4)$-representations (left side via $\beta$), $\mathbb H\otimes\mathbb C\cong\operatorname{Hom}(\slashed S^+;\slashed S^-)$.
  `Proof in source: omitted.`

### Examples
- **E4.1.1 — Low-dimensional Clifford algebras** (p. 35). $Cl(\mathbb R^1)\cong\mathbb R[x]/(x^2+1)\cong\mathbb C$; $Cl(\mathbb R^2)$ generated by $1,e_1,e_2$ with $e_1^2=-1=e_2^2$, $e_1e_2=-e_2e_1$ (from $(e_1+e_2)^2=-2$), so $Cl(\mathbb R^2)\cong\mathbb H$.
- **E4.1.2 — Exterior algebra as a Clifford module** (equation (110), p. 35). $V=\Lambda U^*$ with $u\otimes\phi\mapsto\iota_u\phi-\langle u,\cdot\rangle\wedge\phi$.
- **E4.1.3 — Quaternionic vector spaces as $Cl(\mathbb R^3)$-modules** (p. 35–36). For $V$ quaternionic, $\operatorname{Im}\mathbb H\otimes V\to V$, $h\otimes v\mapsto h\cdot v$ satisfies $h\cdot(h\cdot v)=-h\bar hv=-|h|^2v$.
- **E4.1.4 — $V\oplus V$ as a $Cl(\mathbb R^4)$-module** (equation (112), p. 36). $\mathbb H\otimes_{\mathbb R}(V\oplus V)\to V\oplus V$, $h\otimes(v_1,v_2)\mapsto(hv_2,-\bar hv_1)=\begin{pmatrix}0&h\\-\bar h&0\end{pmatrix}\begin{pmatrix}v_1\\v_2\end{pmatrix}$.

### Exercises: none labelled (the "elementary exercise" (111) is listed as T4.1.3).

### Remarks / load-bearing paragraphs
- **R4.1.1 — $Spin(n)\subset Cl(\mathbb R^n)$** (p. 35): "it can be shown" the subgroup generated by products $v_1\cdots v_{2k}$ of an even number of unit vectors is isomorphic to $Spin(n)$.
- **R4.1.2 — Complex structure on $\slashed S=\mathbb H$ and $Sp(1)\cong SU(2)$** (p. 36): right multiplication by $\bar i$ commutes with left multiplication, making $\slashed S$ a complex Hermitian $Sp(1)$-representation.

### External results imported without proof
- **I4.1.1 — $\pi_1(SO(n))\cong\mathbb Z/2\mathbb Z$ for $n\ge3$** and the existence of the universal double cover (p. 34).
- **I4.1.2 — $Spin(n)$ as the even unit-vector products in $Cl(\mathbb R^n)$** (p. 35).
- **I4.1.3 — (111) and $\mathbb H\otimes\mathbb C\cong\operatorname{Hom}(\slashed S^+,\slashed S^-)$** (p. 36). Reference for the whole section: [LM89].

---

## 4.2 Dirac operators

`PDF pages: 36–37`

### Standing conventions and notation
- $M$ Riemannian, oriented, $\dim M=n$; $\operatorname{Fr}_{SO}$ the principal $SO(n)$-bundle of oriented orthonormal frames; $Cl(M):=\operatorname{Fr}_{SO}\times_{SO(n)}Cl(\mathbb R^n)$, fibre $Cl(T_mM)\cong Cl(T^*_mM)$; Levi-Civita connection on $Cl(M)$ denoted $\nabla^{LC}$ (p. 36).
- Clifford multiplication $Cl\colon TM\otimes E\to E$, $(v,e)\mapsto v\cdot e$, $v\cdot(v\cdot e)=-|v|^2e$ (p. 36).
- Dirac operator $D=Cl\circ\nabla$; in a local oriented orthonormal frame $Ds=\sum_{i=1}^ne_i\cdot\nabla_{e_i}s$ (p. 37).
- $d^*$ = formal adjoint of $d$ (see §5.3.2) (p. 37).

### Definitions
- **D4.2.1 — Clifford bundle $Cl(M)$** (unlabelled, p. 36). The tautological $SO(n)$-action on $\mathbb R^n$ extends to $Cl(\mathbb R^n)$; $Cl(M):=\operatorname{Fr}_{SO}\times_{SO(n)}Cl(\mathbb R^n)$, with fibre $Cl(T_mM)$; the Levi-Civita connection induces a connection $\nabla^{LC}$ on $Cl(M)$.
- **D4.2.2 — Bundle of Clifford modules; Dirac bundle** (unlabelled, p. 36). $E\to M$ is a bundle of $Cl(M)$-modules if there is a bundle morphism $Cl\colon TM\otimes E\to E$, $(v,e)\mapsto v\cdot e$, with $v\cdot(v\cdot e)=-|v|^2e$. $E$ is a Dirac bundle if it is moreover equipped with a Euclidean scalar product and a connection $\nabla$ such that: (1) $\nabla$ is Euclidean (metric); (2) $\langle v\cdot e_1,v\cdot e_2\rangle=|v|^2\langle e_1,e_2\rangle$ for all $v\in T_mM$, $e_1,e_2\in E_m$; (3) $\nabla(\phi\cdot s)=(\nabla^{LC}\phi)\cdot s+\phi\cdot\nabla s$ for all $\phi\in\Gamma(Cl(M))$, $s\in\Gamma(E)$.
- **D4.2.3 — Dirac operator** (Definition 113, p. 37). If $E$ is a Dirac bundle, the operator $D\colon\Gamma(E)\xrightarrow{\nabla}\Gamma(T^*M\otimes E)\xrightarrow{Cl}\Gamma(E)$ is the Dirac operator of $E$. In a local orthonormal oriented frame $e_1,\dots,e_n$ of $TM$: $Ds=\sum_{i=1}^ne_i\cdot\nabla_{e_i}s$.

### Theorems: none (self-adjointness is Exercise 115).

### Examples
- **E4.2.1 — $d+d^*$ as a Dirac operator** (Example 114, p. 37). $\Lambda T^*M=\bigoplus_{k=0}^n\Lambda^kT^*M$ is naturally a Dirac bundle with Clifford multiplication (110); its Dirac operator is $d+d^*$ [LM89, Thm 5.12].

### Exercises
- **X4.2.1** (Exercise 115, p. 37). Show that the Dirac operator on a closed manifold is formally self-adjoint: for all $s_1,s_2\in\Gamma(E)$, $\int_M\langle Ds_1,s_2\rangle=\int_M\langle s_1,Ds_2\rangle$.

### Remarks: none beyond the definitions.

### External results imported without proof
- **I4.2.1 — $d+d^*$ is the Dirac operator of $\Lambda T^*M$** [LM89, Thm 5.12] (p. 37).

---

## 4.3 Spin and Spin$^c$ structures

`PDF pages: 37–41`

### Standing conventions and notation
- $\operatorname{Fr}_{SO}\to M$ oriented orthonormal frame bundle; $Spin(n)$ acts on $\operatorname{Fr}_{SO}$ via $Spin(n)\to SO(n)$ (p. 37).
- $\omega\in\Omega^1(\operatorname{Fr}_{SO};\mathfrak{so}(n))$ the Levi-Civita connection form; $\tau^*\omega\in\Omega^1(P;\mathfrak{spin}(n))$ via $\mathfrak{spin}(n)\cong\mathfrak{so}(n)$ (p. 37).
- $\slashed S$ = the unique complex representation $\rho\colon Spin(n)\to\operatorname{End}(\slashed S)$ ($n\ge3$) that extends to a complex irreducible representation of $Cl(\mathbb R^n)$; same symbol for the spinor bundle $\slashed S:=P\times_{Spin(n),\rho}\slashed S$ (p. 37).
- $\slashed D\colon\Gamma(\slashed S)\to\Gamma(\slashed S)$ spin Dirac operator; in dimension 4, $\slashed D=\begin{pmatrix}0&\slashed D^-\\\slashed D^+&0\end{pmatrix}$, $\slashed D^\pm\colon\Gamma(\slashed S^\pm)\to\Gamma(\slashed S^\mp)$ (p. 38).
- Twisted: $E=P\times_{G,\tau}\mathbb C^n$ Hermitian with connection from $A$; $\slashed S\otimes E$; $\slashed D_A$ (p. 38).
- $Spin^c(n):=Spin(n)\times U(1)/\pm1$ ($\{\pm1\}$ embedded diagonally); $\rho_0\colon Spin^c(n)\to SO(n)$, $\rho_{\det}\colon Spin^c(n)\to U(1)$ (the map $[g,z]\mapsto z^2$); exact sequence $\{1\}\to\{\pm1\}\to Spin^c(n)\xrightarrow{(\rho_0,\rho_{\det})}SO(n)\times U(1)\to\{1\}$ (120) (p. 39).
- $\rho_\pm\colon Spin^c(4)\to U(2)$, $\rho_\pm(A_+,A_-)=A_\pm$ (p. 39).
- $L_{\det}:=P\times_{\rho_{\det}}\mathbb C$ determinant line bundle; $P_{\det}:=P/Spin(n)$ its $U(1)$-structure; $\tau\colon P\to P/\{\pm1\}=\operatorname{Fr}_{SO}\times_MP_{\det}$ (p. 40).
- Spin$^c$ connection: $\tau^*(\omega+A)\in\Omega^1(P;\mathfrak{spin}^c(n))$ using $\mathfrak{spin}^c(n)\cong\mathfrak{so}(n)\oplus\mathfrak u(1)$, for $A$ a connection on $P_{\det}$ (p. 40).
- $Spin^c$ spinor representation $[g,z]\cdot s=z\rho(g)s$; spin$^c$ spinor bundle $\slashed S:=P\times_{Spin^c(n)}\slashed S$; spin$^c$ Dirac operator $\slashed D_A$ (p. 40).
- $\mathcal S=\mathcal S(M)$ = set of spin$^c$ structures; $H^2(M;\mathbb Z)$ acts by $\slashed S\mapsto\slashed S\otimes L$ (p. 41).
- Convention on the factor $\tfrac12$: for $a\in\Omega^1(M;\mathbb Ri)$, $\slashed D_{A+a}=\slashed D_A+\tfrac12a\cdot$ (127) (p. 40).

### Definitions
- **D4.3.1 — Spinnable manifold; spin structure; spin manifold** (Definition 116, p. 37). $M$ is spinnable if there is a principal $Spin(n)$-bundle $P$ with a $Spin(n)$-equivariant map $\tau\colon P\to\operatorname{Fr}_{SO}$ covering $\mathrm{id}_M$ which is a fibrewise double covering ($Spin(n)$ acting on $\operatorname{Fr}_{SO}$ through $Spin(n)\to SO(n)$). Such a $P$ is a spin structure; $M$ with a spin structure is a spin manifold.
- **D4.3.2 — Levi-Civita connection on a spin structure** (unlabelled, p. 37). $\tau^*\omega\in\Omega^1(P;\mathfrak{spin}(n))$ is a connection on $P$ (since $Spin(n)\to SO(n)$ is a local diffeomorphism, $\mathfrak{spin}(n)\cong\mathfrak{so}(n)$); still called the Levi-Civita connection.
- **D4.3.3 — Spinor representation and spinor bundle** (unlabelled, p. 37). For $n\ge3$ there is a unique complex representation $\rho\colon Spin(n)\to\operatorname{End}(\slashed S)$ distinguished by extending to a complex irreducible representation of $Cl(\mathbb R^n)$ (this does not mean $\slashed S$ is the unique or an irreducible $Spin(n)$-representation). $n=3$: the fundamental representation of $Sp(1)$; $n=4$: $\slashed S=\slashed S^+\oplus\slashed S^-$ (112). Spinor bundle $\slashed S:=P\times_{Spin(n),\rho}\slashed S$, a bundle of $Cl(M)$-modules; the spin Dirac operator is $\slashed D\colon\Gamma(\slashed S)\to\Gamma(\slashed S)$.
- **D4.3.4 — Twisted spinor bundle and twisted Dirac operator** (unlabelled, p. 38). For a principal $G$-bundle $P$ with connection $A$ and a unitary representation $\tau\colon G\to U(n)$, $E=P\times_{G,\tau}\mathbb C^n$ is Hermitian; $\slashed S\otimes E$ is a Dirac bundle and $\slashed D_A\colon\Gamma(\slashed S\otimes E)\to\Gamma(\slashed S\otimes E)$ is the twisted Dirac operator.
- **D4.3.5 — $Spin^c(n)$** (unlabelled, p. 39). $Spin^c(n):=Spin(n)\times U(1)/\pm1$ with $\{\pm1\}$ embedded diagonally. Both $Spin(n)$ and $U(1)$ are subgroups; $U(1)$ is central. Exact sequences $\{1\}\to U(1)\to Spin^c(n)\xrightarrow{\rho_0}Spin(n)/\pm1=SO(n)\to\{1\}$ and $\{1\}\to Spin(n)\to Spin^c(n)\xrightarrow{\rho_{\det}}U(1)/\pm1\cong U(1)\to\{1\}$, giving (120): $Spin^c(n)$ is a double cover of $SO(n)\times U(1)$.
- **D4.3.6 — Spin$^c$ structure** (Definition 122, p. 39). A spin$^c$ structure on $M$ is a principal $Spin^c(n)$-bundle $P\to M$ with a $Spin^c(n)$-equivariant map $P\to\operatorname{Fr}_{SO}$ inducing an isomorphism $P/U(1)\cong\operatorname{Fr}_{SO}$.
- **D4.3.7 — Determinant line bundle of a spin$^c$ structure** (unlabelled, p. 40). $L_{\det}:=P\times_{\rho_{\det}}\mathbb C$, a Hermitian line bundle with $U(1)$-structure $P_{\det}:=P/Spin(n)$.
- **D4.3.8 — Spin$^c$ connection, spin$^c$ spinor bundle, spin$^c$ Dirac operator** (unlabelled, p. 40). By (120), $\tau\colon P\to P/\{\pm1\}=\operatorname{Fr}_{SO}\times_MP_{\det}$ is a double cover; for a connection $A$ on $P_{\det}$, $\tau^*(\omega+A)\in\Omega^1(P;\mathfrak{spin}^c(n))$ is a connection on $P$ (a unitary connection on $L_{\det}$ plus Levi-Civita determines a connection on the spin$^c$ bundle). $\slashed S$ extends to a $Spin^c(n)$-representation by $[g,z]\cdot s=z\rho(g)s$; the spin$^c$ spinor bundle $\slashed S:=P\times_{Spin^c(n)}\slashed S$ is a Dirac bundle; $\slashed D_A\colon\Gamma(\slashed S)\to\Gamma(\slashed S)$ is the spin$^c$ Dirac operator.
- **D4.3.9 — Action of $H^2(M;\mathbb Z)$ on spin$^c$ structures** (unlabelled, §4.3.1, p. 41). For a spin$^c$ structure $P$ with spinor bundle $\slashed S$ and a Hermitian line bundle $L$, $\slashed S\otimes L$ is the spinor bundle of a spin$^c$ structure $P_L$; this defines an action of $H^2(M;\mathbb Z)$ on $\mathcal S(M)$.

### Theorems
- **T4.3.1 — Closed oriented 4-manifolds are spin$^c$** (Proposition 123, p. 39). Any closed oriented four-manifold admits a spin$^c$ structure.
  `Proof in source: omitted/cited (to [Mor96, Lem. 3.1.2]).` Also stated: closed oriented 3-manifolds are spin [GS99a, Rem. 1.4.27], hence spin$^c$; there are closed 4-manifolds that are not spin.
- **T4.3.2 — Classification of spin$^c$ structures** (unlabelled, §4.3.1, p. 41). The action of $H^2(M;\mathbb Z)$ on $\mathcal S(M)$ is free and transitive, so $\mathcal S(M)$ can be identified with $H^2(M;\mathbb Z)$, non-canonically. If $M$ is spin, the spin structure viewed as a distinguished spin$^c$ structure gives an origin and fixes $\mathcal S(M)\cong H^2(M;\mathbb Z)$.
  `Proof in source: omitted ("can be shown").`
- **T4.3.3 — $Spin^c(3)\cong U(2)$, $Spin^c(4)$ explicitly** (Example 121, p. 39): see E4.3.2. `Proof in source: omitted.`

### Examples
- **E4.3.1 — Twisted spinors in dimension 3 are complexified forms** (Example 118, p. 38). $\dim M=3$, $E=\slashed S$ with the Levi-Civita connection: $\slashed S\otimes\slashed S=\operatorname{Sym}^2(\slashed S)\oplus\Lambda^2\slashed S\cong T^*_{\mathbb C}M\oplus\mathbb C$ (cf. (111)), so twisted spinors are complexified odd forms (equivalently even forms via Hodge $*$); the complexification of $d+d^*\colon\Omega^{\mathrm{odd}}(M)\to\Omega^{\mathrm{even}}(M)$ coincides with the twisted Dirac operator on $\Gamma(\slashed S\otimes\slashed S)$ ("one can show").
- **E4.3.2 — $Spin^c(3)$ and $Spin^c(4)$** (Example 121, p. 39). (a) $n=3$: $Spin^c(3)=SU(2)\times U(1)/\pm1\cong U(2)$, $\rho_{\det}(A)=\det A$, and (120) reads $\{1\}\to\{\pm1\}\to U(2)\to SO(3)\times U(1)\to\{1\}$ with $U(2)\to SO(3)=PU(2)$ the natural projection. (b) $n=4$: $Spin^c(4)=((SU(2)\times SU(2))\times U(1))/\pm1=\{(A_+,A_-)\in U(2)\times U(2)\mid\det A_+=\det A_-\}$, $\rho_{\det}(A_+,A_-)=\det A_+=\det A_-$; homomorphisms $\rho_\pm\colon Spin^c(4)\to U(2)$, $\rho_\pm(A_+,A_-)=A_\pm$.
- **E4.3.3 — Spin$^c$ structures on a spin manifold** (Example 124, p. 40). $M$ spin with spin structure $P_{Spin}$ and a principal $U(1)$-bundle $P_0$: $P:=P_{Spin}\times_MP_0/\pm1$ is a principal $Spin^c(n)$-bundle; its spinor bundle is $\slashed S\otimes L_0$ with $\slashed S$ the pure spinor bundle and $L_0:=P_0\times_{U(1)}\mathbb C$; the spin$^c$ Dirac operator is the twisted Dirac operator.

### Exercises
- **X4.3.1** (Exercise 119, p. 38). The Clifford multiplication combined with $\operatorname{ad}P\to\operatorname{End}(E)$ yields the twisted Clifford multiplication $T^*M\otimes\operatorname{ad}P\to\operatorname{End}(\slashed S)\otimes\operatorname{End}(E)\cong\operatorname{End}(\slashed S\otimes E)$. Show that for $a\in\Omega^1(\operatorname{ad}P)$: $\slashed D_{A+a}\psi=\slashed D_A\psi+a\cdot\psi$.
- **X4.3.2** (Exercise 126, p. 40). For $a\in\Omega^1(M;\mathbb Ri)$ prove $\slashed D_{A+a}\psi=\slashed D_A\psi+\tfrac12a\cdot\psi$ (127).

### Remarks / load-bearing paragraphs
- **R4.3.1 — Existence/classification of spin structures via Stiefel–Whitney classes** (p. 37): not treated; [LM89]. Throughout the rest of §4.3 (first part) $M$ is assumed spin.
- **R4.3.2 — Chirality** (Remark 117, p. 38). In dimension 4, $\slashed S=\slashed S^+\oplus\slashed S^-$; by (112) Clifford multiplication by a 1-form $\omega$ maps $\slashed S^\pm\to\slashed S^\mp$; hence $\slashed D=\begin{pmatrix}0&\slashed D^-\\\slashed D^+&0\end{pmatrix}$.
- **R4.3.3 — $\{\pm1\}$ is central in $Spin(n)$** (p. 39): "one can show"; clear for $n=3,4$.
- **R4.3.4 — Spin$^c$ spinors as $\slashed S\otimes L_0$ with neither factor globally defined** (Remark 125, p. 40): in general neither $\slashed S$ nor $L_0$ exists globally but the product does; spin$^c$ structures make this precise.
- **R4.3.5 — Explanation of the factor $\tfrac12$ in (127)** (p. 40). Think of the spin$^c$ spinor bundle as $\slashed S\otimes L_0$; the determinant line bundle is $\Lambda^2(\slashed S\otimes L_0)=L_0^2$, so $A_0\in\mathcal A(L_0)$ induces $A$ on $L_0^2$ and $A_0+a_0$ corresponds to $A+2a_0$.
- **R4.3.6 — Existence of spin$^c$ structures may fail; rarely unique; spin ⇒ spin$^c$** (p. 39).

### External results imported without proof
- **I4.3.1 — Existence/uniqueness of the spinor representation $\slashed S$ of $Spin(n)$** ($n\ge3$) extending to an irreducible $Cl(\mathbb R^n)$-representation (p. 37).
- **I4.3.2 — Stiefel–Whitney criteria for spin structures** [LM89] (p. 37).
- **I4.3.3 — Closed oriented 4-manifolds are spin$^c$** [Mor96, Lem. 3.1.2]; **closed oriented 3-manifolds are spin** [GS99a, Rem. 1.4.27] (pp. 39–40).
- **I4.3.4 — $\{\pm1\}$ central in $Spin(n)$** (p. 39).
- **I4.3.5 — $H^2(M;\mathbb Z)$ acts freely and transitively on $\mathcal S(M)$** (p. 41).
- **I4.3.6 — Complexification of $d+d^*$ equals the twisted Dirac operator on $\slashed S\otimes\slashed S$ in dimension 3** (p. 38).

---

## 4.4 The Weitzenböck formula

`PDF pages: 41–43`

### Standing conventions and notation
- On $\mathbb R^4$, for $u\colon\mathbb R^4\to\mathbb H$: $\slashed D^+(u)=\frac{\partial u}{\partial x_0}+i\frac{\partial u}{\partial x_1}+j\frac{\partial u}{\partial x_2}+k\frac{\partial u}{\partial x_3}$, $\slashed D^-(u)=-\frac{\partial u}{\partial x_0}+i\frac{\partial u}{\partial x_1}+j\frac{\partial u}{\partial x_2}+k\frac{\partial u}{\partial x_3}$; analogues of $\bar\partial=\tfrac12(\partial_x+i\partial_y)$ and $\partial=\tfrac12(\partial_x-i\partial_y)$ (p. 41).
- Laplacian on $\mathbb R^4$: $\Delta=-\sum_{i=0}^3\partial^2/\partial x_i^2$ (non-negative) (p. 41).
- Spinor bundle of $\mathbb R^4$ (resp. $\mathbb R^3$) is canonically the product bundle (p. 41).
- Connection Laplacian $\nabla^*\nabla\colon\Gamma(E)\xrightarrow{\nabla}\Omega^1(E)\xrightarrow{\nabla^*=-{*}d^\nabla{*}}\Gamma(E)$ (130) (p. 42).
- Curvature endomorphism $\mathcal R(s):=\tfrac12\sum_{i,j=1}^ne_i\cdot e_j\cdot R_{e_i,e_j}(s)$, image of $R\in\Omega^2(\operatorname{End}E)$ under $\Lambda^2T^*M\otimes\operatorname{End}(E)\to\operatorname{End}(E)$ via Clifford multiplication (p. 42).
- $\ker\slashed D$ = harmonic spinors (p. 43).
- In dimension 4: $\slashed D^-\slashed D^+=(\slashed D^+)^*\slashed D^+$; $F_A^+$ the self-dual part; anti-self-dual 2-forms act trivially on $\slashed S^+$ (p. 43).

### Definitions
- **D4.4.1 — Connection Laplacian** (equation (130), p. 42). For a Euclidean vector bundle $E$ with connection $\nabla$, $\nabla^*\nabla:=\nabla^*\circ\nabla$ with $\nabla^*=-{*}d^\nabla{*}\colon\Omega^1(E)\to\Gamma(E)$.
- **D4.4.2 — Curvature endomorphism $\mathcal R$ of a Dirac bundle** (unlabelled, p. 42). For a Dirac bundle $E$ with curvature $R\in\Omega^2(\operatorname{End}(E))$, $\mathcal R\in\operatorname{End}(E)$ is defined in a local frame $(e_i)$ of $TM$ by $\mathcal R(s):=\tfrac12\sum_{i,j}e_i\cdot e_j\cdot R_{e_i,e_j}(s)$.

### Theorems
- **T4.4.1 — Dirac operator on flat $\mathbb R^4$ squares to the Laplacian** (equation (128), p. 41). On $\mathbb R^4$, $\slashed D=\begin{pmatrix}0&\slashed D^-\\\slashed D^+&0\end{pmatrix}$ (cf. (112)) and $\slashed D^2=\begin{pmatrix}\slashed D^-\slashed D^+&0\\0&\slashed D^+\slashed D^-\end{pmatrix}=\Delta$ with $\Delta=-\sum_{i=0}^3\partial_{x_i}^2$: "the Dirac operator is the square root of the Laplacian".
  `Proof in source: omitted ("straightforward computation"; "tracing through the construction").`
- **T4.4.2 — Weitzenböck formula** (Theorem 132, p. 42). Let $\slashed D$ be the Dirac operator of the Dirac bundle $E$. Then $\slashed D^2=\nabla^*\nabla+\mathcal R$.
  `Proof in source: full (short).` Pick $m\in M$ and a local orthonormal frame $(e_i)$ with $\nabla_{e_i}e_j=0$ at $m$. At $m$: $\slashed D^2s=\sum_ie_i\cdot\nabla_{e_i}(\sum_je_j\cdot\nabla_{e_j}s)=\sum_{i,j}e_i\cdot e_j\cdot\nabla_{e_i}\nabla_{e_j}s=\sum_ie_i\cdot e_i\cdot\nabla_{e_i}\nabla_{e_i}s+\tfrac12\sum_{i\ne j}e_i\cdot e_j\cdot(\nabla_{e_i}\nabla_{e_j}-\nabla_{e_j}\nabla_{e_i})s=\nabla^*\nabla s+\mathcal Rs$.
  `Gaps:` existence of a synchronous frame ($\nabla_{e_i}e_j=0$ at $m$) assumed; the compatibility condition (3) of a Dirac bundle is used silently to pull $e_j$ through $\nabla_{e_i}$; $\sum_ie_i\cdot e_i\nabla_{e_i}\nabla_{e_i}=-\sum\nabla_{e_i}\nabla_{e_i}=\nabla^*\nabla$ at $m$ uses Exercise 131(a); $[\nabla_{e_i},\nabla_{e_j}]=R_{e_i,e_j}$ at $m$ uses $[e_i,e_j]=0$ at $m$.
- **T4.4.3 — Lichnerowicz–Weitzenböck formula for the spin$^c$ Dirac operator** (Corollary 133, p. 43). Let $A$ be a Hermitian connection on the determinant line bundle with curvature $F_A$. Then the spin$^c$ Dirac operator satisfies $\slashed D^2\psi=\nabla^*\nabla\psi+\tfrac14s_g\psi+\tfrac12F_A\cdot\psi$, $s_g$ the scalar curvature of $g$. In particular for $M$ spin and $\slashed S$ the pure spinor bundle, $\slashed D^2\psi=\nabla^*\nabla\psi+\tfrac14s_g\psi$.
  `Proof in source: left as exercise ("a straightforward computation").`
- **T4.4.4 — Positive scalar curvature kills harmonic spinors** (unlabelled, p. 43). For a spin manifold with a metric of positive scalar curvature, $\ker\slashed D=0$.
  `Proof in source: omitted ("this implies").` Intended: integrate $\langle\slashed D^2\psi,\psi\rangle=\|\nabla\psi\|^2+\tfrac14\int s_g|\psi|^2$ (closed $M$); if $\slashed D\psi=0$ and $s_g>0$ then $\psi=0$.
- **T4.4.5 — Chiral Weitzenböck formula in dimension 4** (unlabelled, p. 43). For $\psi\in\Gamma(\slashed S^+)$: $\slashed D^-\slashed D^+\psi=(\slashed D^+)^*\slashed D^+\psi=\nabla^*\nabla\psi+\tfrac14s_g\psi+\tfrac12F_A^+\cdot\psi$, using that anti-self-dual 2-forms act trivially on $\slashed S^+$.
  `Proof in source: omitted (from Corollary 133).`

### Examples
- **E4.4.1 — Dirac operators on $\mathbb R^2$ and $\mathbb R^3$** (Remark 129, p. 41). On $\mathbb R^2$: $\begin{pmatrix}0&2\partial_z\\-2\partial_{\bar z}&0\end{pmatrix}\colon C^\infty(\mathbb R^2;\mathbb C^2)\to C^\infty(\mathbb R^2;\mathbb C^2)$, squares to the Laplacian; dimension 2 needs special treatment since $\pi_1(SO(2))\cong\mathbb Z$. On $\mathbb R^3$ with spinor bundle the product bundle $\mathbb H$: $\slashed D(u)=i\partial_{x_1}u+j\partial_{x_2}u+k\partial_{x_3}u$, also squares to the Laplacian.

### Exercises
- **X4.4.1** (Exercise 131, p. 42). (a) For a local orthonormal frame $(e_1,\dots,e_n)$ of $TM$ show $\nabla^*\nabla s=-\sum_{i=1}^n(\nabla_{e_i}\nabla_{e_i}s-\nabla_{\nabla_{e_i}e_i}s)$, where $\nabla_{e_i}e_i$ uses the Levi-Civita connection. (b) Prove that the connection Laplacian is formally self-adjoint. (c) For $M$ closed, prove $\langle\nabla^*\nabla s,s\rangle_{L^2}=\|\nabla s\|^2_{L^2}$.
- **X4.4.2** (Corollary 133, p. 42–43, "left as an exercise"): derive $\slashed D^2=\nabla^*\nabla+\tfrac14s_g+\tfrac12F_A\cdot$ for the spin$^c$ Dirac operator.

### Remarks / load-bearing paragraphs
- **R4.4.1 — $\slashed D^\pm$ as 4-dimensional $\bar\partial$, $\partial$** (p. 41).
- **R4.4.2 — Weitzenböck on general manifolds: $\slashed D^2=\Delta$ up to zero order** (p. 42).
- **R4.4.3 — Chiral version and vanishing of ASD forms on $\slashed S^+$** (p. 43).

### External results imported without proof
- **I4.4.1 — Existence of synchronous frames** ($\nabla_{e_i}e_j=0$ at a point) (p. 42).
- **I4.4.2 — Anti-self-dual 2-forms act trivially on $\slashed S^+$** (p. 43; proved later in §7.1 as "a straightforward computation shows" the kernel of $\Lambda^2\to\operatorname{End}(\slashed S^\pm)$ is $\Lambda^2_\mp$).
- **I4.4.3 — Corollary 133** (the $\tfrac14s_g$ and $\tfrac12F_A$ terms) not derived.

---

## 5.1 Sobolev spaces

`PDF pages: 43–46`

### Standing conventions and notation
- $\Omega\subset\mathbb R^n$ bounded domain with smooth boundary; Dirichlet problem (134): $\Delta u=0$ in $\Omega$, $u|_{\partial\Omega}=\varphi$, $u\in C^2(\Omega)\cap C^0(\bar\Omega)$; energy $E(u):=\tfrac12\int_\Omega|\nabla u(x)|^2dx$ (p. 43). (Here the sign of $\Delta$ is such that $\frac d{dt}\big|_{0}E(u+tw)=\int_\Omega w\,\Delta u\,dx$, i.e. $\Delta=-\sum\partial_i^2$ again, consistent with the global convention.)
- $L^2(\mathbb R^n)$: $\langle u,v\rangle_{L^2}:=\int uv\,dx$; completion of $C_0^\infty(\mathbb R^n)$ in $\|u\|_{L^2}=\sqrt{\langle u,u\rangle}$ (p. 44).
- $\|u\|_{L^p}:=(\int|u|^pdx)^{1/p}$, $p>1$; $L^p(\mathbb R^n)$ = completion of $C_0^\infty$ (p. 44).
- **Sobolev norm:** $\|u\|_{W^{k,p}}:=\big(\sum_{i=0}^k\|\nabla^iu\|^p_{L^p}\big)^{1/p}$; $W^{k,p}(\mathbb R^n)$ = completion of $C_0^\infty(\mathbb R^n)$ (p. 44). Notation $W^{k,p}$ chosen deliberately (Remark 135: other notations $L^s_r$ are inconsistent across the literature).
- On a Riemannian manifold $M$: $\nabla u\in\Gamma(T^*M)$; higher derivatives via a connection on $T^*M$ (e.g. Levi-Civita); $W^{k,p}(M)$ (p. 44). For a bundle $E$ with $\nabla^E\in\mathcal A(E)$, $\nabla^M\in\mathcal A(T^*M)$: $W^{k,p}(M;E)$; different choices give equivalent norms, same topology (p. 45).
- Inclusions $L^p(M;E)=W^{0,p}\supset W^{1,p}\supset W^{2,p}\supset\cdots$ (p. 45). $n=\dim M$ in Theorem 136.
- $C^r(M;E)$ with the $C^r$ norm; $\|u\|_{C^0}$ sup norm (p. 45).

### Definitions
- **D5.1.1 — $L^p$ spaces** (unlabelled, p. 44). $L^p(\mathbb R^n)$ is the completion of $C_0^\infty(\mathbb R^n)$ with respect to $\|u\|_{L^p}:=(\int|u(x)|^pdx)^{1/p}$, $p>1$; $L^2$ is a Hilbert space with $\langle u,v\rangle_{L^2}=\int uv\,dx$.
- **D5.1.2 — Sobolev spaces $W^{k,p}$** (unlabelled, pp. 44–45). $W^{k,p}(\mathbb R^n)$ := completion of $C_0^\infty(\mathbb R^n)$ in $\|u\|_{W^{k,p}}:=(\sum_{i=0}^k\|\nabla^iu\|^p_{L^p})^{1/p}$. On a Riemannian manifold $M$ (or open subset of $\mathbb R^n$): $W^{k,p}(M)$ with $\nabla^iu$ computed using a connection on $T^*M$. For a vector bundle $E\to M$ with connections $\nabla^E$, $\nabla^M$: $W^{k,p}(M;E)$ defined the same way; the topology is independent of the choices.

### Theorems
- **T5.1.1 — Sobolev embedding, compactness, and multiplication theorems** (Theorem 136, p. 45). Let $M$ be a compact manifold, $n=\dim M$. (i) If $s\in W^{k,p}(M;E)$ then $s\in W^{m,q}(M;E)$ provided $k-\tfrac np\ge m-\tfrac nq$ and $k\ge m$, and there is $C$ independent of $s$ with $\|s\|_{W^{m,q}}\le C\|s\|_{W^{k,p}}$, i.e. the natural embedding $j\colon W^{k,p}(M;E)\subset W^{m,q}(M;E)$ is continuous. (ii) $j$ is a compact operator provided $k-\tfrac np>m-\tfrac nq$ and $k>m$ (137): any sequence bounded in $W^{k,p}$ has a subsequence converging in $W^{m,q}$. (iii) There is a natural continuous embedding $W^{k,p}(M;E)\subset C^r(M;E)$ provided $k-\tfrac np>r$; in particular if $s\in W^{k,p}$ for fixed $p$ and all $k\ge0$ then $s\in C^\infty(M;E)$. (iv)(a) If $kp>n$, $W^{k,p}(M;\mathbb R)$ is an algebra. (iv)(b) If $kp<n$, there is a bounded map $W^{k_1,p_1}\otimes W^{k_2,p_2}\to W^{k,p}$ provided $k_1-\tfrac n{p_1}+k_2-\tfrac n{p_2}\ge k-\tfrac np$.
  `Proof in source: omitted ("beyond the goals of these notes"); "spirit of the proof" in Remark 138.`
  `Gaps:` (iv)(b) as printed lacks the usual side conditions ($k\le\min(k_1,k_2)$, and in the borderline case a strict inequality); the writers should state the standard version.

### Examples: none numbered (the Dirichlet problem is the motivating example, see R5.1.1).

### Exercises: none.

### Remarks / load-bearing paragraphs
- **R5.1.1 — Dirichlet's principle as motivation** (pp. 43–44). If $u$ minimises $E$ among $v\in C^2(\Omega)\cap C^0(\bar\Omega)$ with $v|_{\partial\Omega}=\varphi$, then $0=\frac d{dt}\big|_{t=0}E(u+tw)=\int_\Omega w\Delta u\,dx$ for all $w$ with $w|_{\partial\Omega}=0$ (integration by parts), hence $u$ is harmonic. Strategy: minimising sequence $u_k$, extract a convergent subsequence — this needs Sobolev spaces; "crash course" follows.
- **R5.1.2 — Notation for Sobolev spaces** (Remark 135, p. 44).
- **R5.1.3 — Dependence of $W^{k,p}(M;E)$ on connections** (pp. 44–45): norms depend on $\nabla^E,\nabla^M$ but are equivalent.
- **R5.1.4 — Spirit of the proof of Sobolev embedding on $S^1$** (Remark 138, pp. 45–46). For $u\in C^\infty(S^1;\mathbb R)$, $\bar u:=\tfrac1{2\pi}\int u(\theta)d\theta$, $u_0:=u-\bar u$; by the mean value theorem $u_0(\theta_0)=0$ for some $\theta_0$; then $|u_0(\theta)|=|\int_{\theta_0}^\theta u_0'(\varphi)d\varphi|\le\sqrt{\int_{\theta_0}^\theta|u_0'|^2}\sqrt{\int_{\theta_0}^\theta1^2}\le\sqrt{2\pi}\|u_0\|_{W^{1,2}}$ (139) by Cauchy–Schwarz, yielding $\|u\|_{C^0}\le C\|u\|_{W^{1,2}}$ and $W^{1,2}(S^1)\subset C^0(S^1)$. Tracing (139): $|u(\theta_1)-u(\theta_2)|\le\sqrt{2\pi}\|u\|_{W^{1,2}}\operatorname{dist}(\theta_1,\theta_2)^{1/2}$, so a $W^{1,2}$-bounded sequence is uniformly bounded and equicontinuous; Arzelà–Ascoli gives a $C^0$-convergent subsequence, proving compactness of $W^{1,2}(S^1)\subset L^p(S^1)$ for any $p$.

### External results imported without proof
- **I5.1.1 — Sobolev embedding theorem** (Theorem 136(i),(iii)) (p. 45).
- **I5.1.2 — Rellich–Kondrachov compactness** (Theorem 136(ii)) (p. 45).
- **I5.1.3 — Sobolev multiplication / algebra property** (Theorem 136(iv)) (p. 45).
- **I5.1.4 — Arzelà–Ascoli theorem** (p. 46).
- **I5.1.5 — Equivalence of Sobolev norms for different connections on compact $M$** (p. 45).

---

## 5.2 Elliptic operators

`PDF pages: 46–49`

### Standing conventions and notation
- Linear differential operator of order $\ell$ on $\Omega\subset\mathbb R^n$ open: $Lf=\sum_{|\alpha|\le\ell}A_\alpha(x)\frac{\partial^{|\alpha|}}{\partial x^\alpha}f$ (140), $\alpha$ a multi-index, $|\alpha|=\sum\alpha_i$, $A_\alpha\in C^\infty(\Omega;\operatorname{Hom}(\mathbb R^r;\mathbb R^s))$ (p. 46).
- Principal symbol: $\sigma_L(\xi):=\sum_{|\alpha|=\ell}A_\alpha(x)\xi^\alpha=\sum_{|\alpha|=\ell}A_\alpha(x)\xi_1^{\alpha_1}\cdots\xi_n^{\alpha_n}$, $\xi\in(\mathbb R^n)^*\cong\mathbb R^n$; viewed as a map $\Omega\times\mathbb R^n\to\operatorname{Hom}(\mathbb R^r;\mathbb R^s)$ polynomial in $\xi$ (p. 46). **No factor of $i$ in the symbol** (so $\sigma_\Delta(\xi)=-|\xi|^2$ for the non-negative Laplacian).
- On bundles: $\pi\colon T^*M\to M$; the symbol is a section of $\operatorname{Hom}(\pi^*E;\pi^*F)$ (p. 47). The source also writes $\sigma_\xi(D)$ for $\sigma_D(\xi)$ (Example 144).
- Riemannian metric in coordinates $g=g_{ij}dx_i\otimes dx_j$, $|g|=\det(g_{ij})$, $(g^{ij})$ inverse (p. 47).
- Extension (145): $L\colon W^{k+\ell,p}(M;E)\to W^{k,p}(M;F)$ bounded for $k\ge0$, $p>1$ (p. 47).
- Formal adjoint $L^*$ defined by $\langle Ls,t\rangle_{L^2}=\langle s,L^*t\rangle_{L^2}$ (147) with respect to Euclidean structures on $E,F$ (p. 48).
- Fredholm: $\operatorname{index}B:=\dim\ker B-\dim\operatorname{coker}B$, $\operatorname{coker}B:=Y/\operatorname{Im}B$ (p. 48).

### Definitions
- **D5.2.1 — Linear differential operator of order $\ell$ (local)** (equation (140), p. 46). $L\colon C^\infty(\Omega;\mathbb R^r)\to C^\infty(\Omega;\mathbb R^s)$ of the form $Lf=\sum_{|\alpha|\le\ell}A_\alpha(x)\partial^{|\alpha|}f/\partial x^\alpha$ with $A_\alpha\in C^\infty(\Omega;\operatorname{Hom}(\mathbb R^r;\mathbb R^s))$. Example for $\ell=2$, $n=2$: $Lf=A_{20}\partial^2_{x_1}f+A_{11}\partial_{x_1}\partial_{x_2}f+A_{02}\partial^2_{x_2}f+A_{10}\partial_{x_1}f+A_{01}\partial_{x_2}f+A_{00}f$.
- **D5.2.2 — Principal symbol** (unlabelled, p. 46). $\sigma_L(\xi):=\sum_{|\alpha|=\ell}A_\alpha(x)\xi^\alpha$, $\xi\in(\mathbb R^n)^*$; a map $\Omega\times\mathbb R^n\to\operatorname{Hom}(\mathbb R^r;\mathbb R^s)$ polynomial (homogeneous of degree $\ell$) in $\xi$.
- **D5.2.3 — Elliptic operator (local)** (Definition 141, p. 46). $L$ is elliptic if for all $x\in\Omega$ and all $\xi\in\mathbb R^n\setminus\{0\}$, $\sigma_L(\xi)$ is an invertible homomorphism. In particular $r=s$ is necessary.
- **D5.2.4 — Linear differential operator and ellipticity on vector bundles** (unlabelled, p. 47). For bundles $E,F$ over $M$ of ranks $r,s$, $L\colon\Gamma(E)\to\Gamma(F)$ is a linear differential operator of order $\ell$ if in any local coordinates on $\Omega\subset M$ and any trivialisations of $E|_\Omega,F|_\Omega$ it has the form (140) (coefficients depending on the choices). The symbol is a section of $\operatorname{Hom}(\pi^*E;\pi^*F)$ over $T^*M$; $L$ is elliptic if the symbol is pointwise invertible away from the zero section.
- **D5.2.5 — Formal adjoint** (equation (147), p. 48). Given Euclidean structures on $E,F$, $L^*\colon C^\infty(M;F)\to C^\infty(M;E)$ is a formal adjoint of $L$ if $\langle Ls,t\rangle_{L^2}=\langle s,L^*t\rangle_{L^2}$ for all $s\in C^\infty(M;E)$, $t\in C^\infty(M;F)$. Facts stated: $L^*$ exists, is a differential operator of order $\ell$, and $L$ is elliptic iff $L^*$ is.
- **D5.2.6 — Fredholm operator and index** (Definition 150, p. 48). A bounded linear map $B\colon X\to Y$ between Banach spaces is Fredholm if (a) $\dim\ker B<\infty$; (b) $\operatorname{Im}B$ is closed in $Y$; (c) $\dim\operatorname{coker}B<\infty$, $\operatorname{coker}B:=Y/\operatorname{Im}B$. Then $\operatorname{index}B:=\dim\ker B-\dim\operatorname{coker}B$.

### Theorems
- **T5.2.1 — Elliptic estimate (elliptic regularity)** (Theorem 146, p. 48). Let $M$ be compact. For any linear elliptic operator $L$ (of order $\ell$) there is a constant $C>0$ such that: if $Ls\in W^{k,p}(M;F)$ then $s\in W^{k+\ell,p}(M;E)$ and $\|s\|_{W^{k+\ell,p}}\le C(\|Ls\|_{W^{k,p}}+\|s\|_{L^p})$; $C$ depends on $k,p$ but not on $s$.
  `Proof in source: omitted.`
- **T5.2.2 — Fredholm alternative** (Theorem 148, p. 48). Let $L$ be elliptic, $M$ compact, $t\in C^\infty(M;F)$. The equation $Ls=t$ has a smooth solution if and only if $t\perp\ker L^*$ (the source prints "$t\in\ker L^*$", a typo for $t\in(\ker L^*)^\perp$).
  `Proof in source: omitted.`
- **T5.2.3 — Fredholm alternative, dichotomy form** (Remark 149, p. 48). Under the hypotheses of Theorem 148 exactly one holds: (i) the homogeneous equation $L^*s=0$ has a non-trivial solution; (ii) $Ls=t$ has a unique solution for any smooth $t$. (Strictly, (ii) requires also $\ker L=0$; the remark is stated for the case where $\dim\ker L=\dim\ker L^*$, e.g. index zero.)
  `Proof in source: omitted ("a corollary").`
- **T5.2.4 — Closed range is automatic** (Remark 151, p. 48). Condition (b) in Definition 150 follows from (a) and (c).
  `Proof in source: omitted ("one can show").`
- **T5.2.5 — Elliptic operators on compact manifolds are Fredholm** (Theorem 153, p. 49). For any elliptic operator $L$ of order $\ell>0$ on a compact manifold $M$, the extension (145) $L\colon W^{k+\ell,p}\to W^{k,p}$ is Fredholm. Moreover $\ker L$ consists of smooth sections only.
  `Proof in source: sketch.` (1) $s\in W^{\ell,p}$ with $Ls=0$ is in $W^{k,p}$ for all $k$ by Theorem 146, hence smooth by Theorem 136(iii). (2) Finite-dimensional kernel: for $s_j\in\ker L$ with $\|s_j\|_{W^{\ell,p}}\le1$, $\|s_j\|_{W^{\ell+1,p}}$ is bounded by Theorem 146, so by Theorem 136(ii) a subsequence converges in $W^{\ell,p}$ to $s_\infty$, and $s_\infty\in\ker L$ since $L\colon W^{\ell,p}\to L^p$ is bounded; the unit ball of $\ker L$ is compact, so $\ker L$ is finite dimensional. (3) Cokernel, for $p=2$: $V:=(\operatorname{Im}L\colon W^{k+\ell,2}\to W^{k,2})^\perp$ ($L^2$-orthogonal complement); "one can show" sections in $V$ lie in $W^{\ell,p}$; then (147) gives $V=\ker L^*$, finite dimensional and smooth by (1)–(2) applied to $L^*$.
  `Gaps:` closedness of the range not addressed; regularity of elements of $V$ asserted; $p\ne2$ not treated; that $V$ complements $\operatorname{Im}L$ in $W^{k,2}$ (not just in $L^2$) not argued.

### Examples
- **E5.2.1 — Laplacian on $\mathbb R^n$** (Example 142, p. 47). For the non-negative Laplacian on functions, $\sigma_\Delta(\xi)=-\sum_i\xi_i^2=-|\xi|^2$, so $\Delta$ is elliptic — the prototypical example.
- **E5.2.2 — Laplace–Beltrami operator** (Example 143, p. 47). $M$ oriented Riemannian, $\Delta f=-{*}d{*}df$ with Hodge $*\colon\Lambda^kT^*M\to\Lambda^{n-k}T^*M$. In coordinates $\Delta f=-|g|^{-1/2}\sum_{i,j}\partial_{x_i}(|g|^{1/2}g^{ij}\partial_{x_j}f)$; for $\xi=\sum\xi_idx_i$, $\sigma_\Delta(\xi)=-|g|^{-1/2}\sum_{i,j}\xi_i|g|^{1/2}g^{ij}\xi_j=-|\xi|^2$ ($|\cdot|$ the norm on $T^*M$); elliptic.
- **E5.2.3 — Dirac operators are elliptic** (Example 144, p. 47). For any Dirac bundle $E$, $D\colon\Gamma(E)\to\Gamma(E)$ is elliptic: $\sigma_\xi(D)$ is Clifford multiplication by $\xi$, invertible with inverse Clifford multiplication by $|\xi|^{-2}\xi$ (the source writes $|\xi|^{-2}\xi$; with $u\cdot u=-|u|^2$ the inverse is $-|\xi|^{-2}\xi$). In dimension 4 (any even dimension) the chiral operators $\slashed D^\pm$ are also elliptic.
- **E5.2.4 — Finite-dimensional linear maps are Fredholm** (p. 48). Any linear map between finite-dimensional spaces $X\to Y$ is Fredholm with index $\dim X-\dim Y$ (the source prints "$\dim Y-\dim X$", a slip; with $\operatorname{index}=\dim\ker-\dim\operatorname{coker}$ the index is $\dim X-\dim Y$).

### Exercises
- **X5.2.1** (Exercise 152, p. 49). Let $B_0$ be a Fredholm operator. Show there is $\varepsilon>0$ such that any bounded operator $B$ with $\|B-B_0\|<\varepsilon$ (operator norm) is also Fredholm. Prove also that $\operatorname{index}B=\operatorname{index}B_0$.

### Remarks / load-bearing paragraphs
- **R5.2.1 — Highest order terms determine essential properties; the symbol as a map on $T^*M$** (pp. 46–47). "A straightforward computation shows that the symbol makes sense as a section of $\operatorname{Hom}(\pi^*E;\pi^*F)$" (i.e. it transforms tensorially under coordinate changes).
- **R5.2.2 — Bounded extension to Sobolev spaces** (equation (145), p. 47): any elliptic (indeed any) differential operator of order $\ell$ extends boundedly $W^{k+\ell,p}\to W^{k,p}$.
- **R5.2.3 — Existence and ellipticity of the formal adjoint** (p. 48).
- **R5.2.4 — Why Fredholm operators matter** (p. 48): they resemble linear maps between finite-dimensional spaces.

### External results imported without proof
- **I5.2.1 — Elliptic estimate / elliptic regularity** (Theorem 146) (p. 48).
- **I5.2.2 — Existence of formal adjoints as differential operators; $L$ elliptic iff $L^*$ elliptic** (p. 48).
- **I5.2.3 — Fredholm alternative for elliptic operators** (Theorem 148) (p. 48).
- **I5.2.4 — Closed range follows from finite kernel and cokernel** (Remark 151) (p. 48).
- **I5.2.5 — Regularity of $L^2$-orthogonal complements of the image** (used in the proof of Theorem 153) (p. 49).

---

## 5.3 Elliptic complexes

`PDF pages: 49–52`

### Standing conventions and notation
- Finite sequence of bundles $E_1,\dots,E_k$; complex (154): $0\to\Gamma(E_1)\xrightarrow{L_1}\Gamma(E_2)\xrightarrow{L_2}\cdots\xrightarrow{L_{k-1}}\Gamma(E_k)\to0$ with $L_j\circ L_{j-1}=0$; cohomology $H^j(E):=\ker L_j/\operatorname{im}L_{j-1}$ (p. 49).
- Symbol sequence $0\to\pi^*E_1\xrightarrow{\sigma_{L_1}}\pi^*E_2\to\cdots\to\pi^*E_k\to0$ over $T^*M$ (p. 49).
- Laplacians $\Delta_j:=L_j^*L_j+L_{j-1}L_{j-1}^*\colon\Gamma(E_j)\to\Gamma(E_j)$ (p. 49).
- From p. 50 on: indices on $L_i$ dropped (all written $L$); all differentials assumed of **order 1**; all $E_i$ Euclidean.
- Harmonic sections $\mathcal H^j(E):=\{s\in\Gamma(E_j)\mid\Delta s=0\}$ (p. 50).
- $L^2$-orthogonal Hodge decomposition (158): $\Gamma(E_j)=\operatorname{Im}L\oplus\mathcal H^j(E)\oplus\operatorname{Im}L^*$ (p. 50).
- Gauge-theoretic reading: $\mathcal B=\Gamma(E_j)$, $\mathcal G:=\Gamma(E_{j-1})$ acting by $(s,t)\mapsto s+Lt$; "moduli space" $L^{-1}(0)/\mathcal G=H^j(E)$; $b_j(E):=\dim H^j(E)$ (p. 51). Footnote 4: one can take Sobolev completions to make $\Gamma(E_j)$ a Banach manifold; the smooth category is used here.
- De Rham: $d^*=(-1)^{n(j-1)+1}{*}d{*}\colon\Omega^j(M)\to\Omega^{j-1}(M)$; Hodge–de Rham Laplacian $\Delta=dd^*+d^*d$; $\mathcal H^j$ harmonic $j$-forms; $b_j(M):=\dim\mathcal H^j$ Betti numbers (p. 52).

### Definitions
- **D5.3.1 — Complex of differential operators and its cohomology** (equation (154), p. 49). A sequence $0\to\Gamma(E_1)\xrightarrow{L_1}\Gamma(E_2)\xrightarrow{L_2}\cdots\xrightarrow{L_{k-1}}\Gamma(E_k)\to0$ of differential operators with $L_j\circ L_{j-1}=0$ for all integer $j\in[1,k-1]$; $H^j(E):=\ker L_j/\operatorname{im}L_{j-1}$, $j\in\{1,\dots,k\}$.
- **D5.3.2 — Elliptic complex** (unlabelled, p. 49). The complex (154) is elliptic if the associated symbol sequence $0\to\pi^*E_1\xrightarrow{\sigma_{L_1}}\pi^*E_2\xrightarrow{\sigma_{L_2}}\cdots\xrightarrow{\sigma_{L_{k-1}}}\pi^*E_k\to0$ is exact on the complement of the zero section of $T^*M$. A very short complex $0\to\Gamma(E)\xrightarrow{L}\Gamma(F)\to0$ is elliptic iff $L$ is elliptic.
- **D5.3.3 — Associated Laplacians** (unlabelled, p. 49). $\Delta=\Delta_j\colon\Gamma(E_j)\to\Gamma(E_j)$, $\Delta_j:=L_j^*L_j+L_{j-1}L_{j-1}^*$.
- **D5.3.4 — Harmonic sections** (unlabelled, p. 50). $\mathcal H^j(E):=\{s\in\Gamma(E_j)\mid\Delta s=0\}$.
- **D5.3.5 — Betti-type invariants $b_j(E)$** (unlabelled, p. 51). $b_j(E):=\dim H^j(E)$.
- **D5.3.6 — De Rham complex, $d^*$, Hodge Laplacian, Betti numbers** (unlabelled, pp. 51–52). $0\to\Omega^0(M)\xrightarrow d\Omega^1(M)\xrightarrow d\cdots\to\Omega^n(M)\to0$; for $M$ oriented Riemannian, $d^*=(-1)^{n(j-1)+1}{*}d{*}\colon\Omega^j\to\Omega^{j-1}$; $\Delta=dd^*+d^*d$; for $M$ compact, $\mathcal H^j\cong H^j_{dR}(M)$ and $b_j(M):=\dim\mathcal H^j$ is the $j$-th Betti number, a topological invariant.

### Theorems
- **T5.3.1 — Hodge theorem for elliptic complexes** (Theorem 156, p. 50). For an elliptic complex on a compact manifold: (i) each $\mathcal H^j(E)$ is finite dimensional; (ii) $s\in\mathcal H^j(E)$ iff $Ls=0$ and $L^*s=0$; (iii) the natural map $\mathcal H^j(E)\to H^j(E)$, $s\mapsto[s]$, is an isomorphism.
  `Proof in source: full (modulo Exercise 155 and Theorem 148).` (i) from ellipticity of $\Delta$ (Exercise 155) and Theorem 153. (ii) from $\langle\Delta s,s\rangle_{L^2}=\langle(LL^*+L^*L)s,s\rangle=\|L^*s\|^2_{L^2}+\|Ls\|^2_{L^2}$. (iii) Surjectivity: given $s_0$ with $Ls_0=0$, seek $t\in\Gamma(E_{j-1})$ with $(L+L^*)(s_0+Lt)=0$, equivalent to $L^*Lt=-L^*s_0$ (157). Solve instead $\Delta t=-L^*s_0$: the right side is $L^2$-orthogonal to $\ker\Delta^*=\ker\Delta$ (by (ii), $\ker\Delta\subset\ker L$ and $\langle L^*s_0,h\rangle=\langle s_0,Lh\rangle=0$), so Theorem 148 gives a solution, rewritten as $L(L^*t)+L^*(s_0+Lt)=0$; since $\operatorname{Im}L\perp\operatorname{Im}L^*$ ("a moment's thought"), both summands vanish, so $t$ solves (157). Injectivity: if $s_1,s_2\in\mathcal H^j$ with $s_1-s_2=Lt$, then $\|Lt\|^2=\langle L^*Lt,t\rangle=\langle L^*(s_1-s_2),t\rangle=0$.
  `Gaps:` the "unique" solution claim for $\Delta t=-L^*s_0$ is unjustified as stated (solutions are unique modulo $\ker\Delta$); $\operatorname{Im}L\perp\operatorname{Im}L^*$ uses $L\circ L=0$; regularity/smoothness of $t$ from Theorem 148.
- **T5.3.2 — Hodge decomposition** (equation (158), p. 50). $\Gamma(E_j)=\operatorname{Im}L\oplus\mathcal H^j(E)\oplus\operatorname{Im}L^*$, $L^2$-orthogonal.
  `Proof in source: omitted/cited (to [Wel80]; "a refinement of the argument").`
- **T5.3.3 — Gauge fixing for a linear elliptic complex** (unlabelled, §5.3.1, p. 51). For each $s\in L^{-1}(0)$ there is a unique harmonic representative $h(s)$ in its "gauge-equivalence class" $s+\operatorname{Im}L$; the map $L^{-1}(0)\to\mathcal H^j(E)$, $s\mapsto h(s)$, induces a diffeomorphism $L^{-1}(0)/\mathcal G\to\mathcal H^j(E)$.
  `Proof in source: omitted (restatement of Theorem 156(iii)).`

### Examples: none numbered (the de Rham complex is the worked instance, §5.3.2).

### Exercises
- **X5.3.1** (Exercise 155, p. 49). Prove that each $\Delta_j$ is elliptic provided the initial complex is elliptic.
- **X5.3.2** (Exercise 159, p. 51). Show that the short complex $0\to\Gamma(E_1)\xrightarrow{L_1}\Gamma(E_2)\xrightarrow{L_2}\Gamma(E_3)\to0$ is elliptic if and only if the operator $(L_2,L_1^*)\colon\Gamma(E_2)\to\Gamma(E_3\oplus E_1)$ is elliptic.
- **X5.3.3** (Exercise 160, p. 52). Show that the de Rham complex is elliptic.

### Remarks / load-bearing paragraphs
- **R5.3.1 — A gauge-theoretic interpretation of $H^j(E)$** (§5.3.1, p. 51). $\mathcal B=\Gamma(E_j)$ carries the action of the additive group $\mathcal G:=\Gamma(E_{j-1})$ by $(s,t)\mapsto s+Lt$; with $\Gamma(E_{j+1})$ a trivial $\mathcal G$-representation, $L\colon\Gamma(E_j)\to\Gamma(E_{j+1})$ is $\mathcal G$-equivariant (= invariant); the action on $L^{-1}(0)$ is not free ($\ker L\subset\Gamma(E_{j-1})$ acts trivially), yet the "moduli space" $L^{-1}(0)/\mathcal G=H^j(E)$ is a finite-dimensional vector space if the complex is elliptic and $M$ compact — this explains the interest in elliptic operators.
- **R5.3.2 — Non-compactness and the dilation action** (p. 51). $H^j(E)$ is never compact (linear); it carries the $\mathbb R_{>0}$-action by dilations and $(H^j\setminus\{0\})/\mathbb R_{>0}$ is compact; so $\dim H^j(E)<\infty$ replaces compactness in the linear setting.
- **R5.3.3 — Gauge fixing** (p. 51): unique harmonic representative; $L^{-1}(0)/\mathcal G\cong\mathcal H^j(E)$.
- **R5.3.4 — $b_j(E)$ as an invariant** (p. 51): the isomorphism class of a finite-dimensional vector space is its dimension (the source says "non-positive integer", meaning non-negative).
- **R5.3.5 — Betti numbers are topological though defined via a smooth structure** (p. 52).

### External results imported without proof
- **I5.3.1 — Hodge decomposition** [Wel80] (p. 50).
- **I5.3.2 — Harmonic forms represent de Rham cohomology; Betti numbers are topological invariants** (p. 52).
- **I5.3.3 — Formula $d^*=(-1)^{n(j-1)+1}{*}d{*}$** (p. 52).

---

## 6.1 The Kuranishi model and the Sard–Smale theorem

`PDF pages: 52–53`

### Standing conventions and notation
- $X,Y$ Banach manifolds; $F\in C^\infty(X;Y)$ (p. 52). For Theorem 162, $X,Y$ Banach **spaces**.
- $\operatorname{index}F:=\operatorname{index}d_xF$ (independent of $x$ if $X$ connected) (p. 52).
- Regular value: $y$ with $d_pF$ surjective for all $p\in F^{-1}(y)$ (p. 52).
- Second category: countable intersection of open dense subsets; in a Banach manifold such sets are dense (p. 53).
- Transversality: $F\pitchfork Z$ iff $\operatorname{Im}d_xF+T_zZ=T_zY$ for all $z\in Z$, $x\in F^{-1}(z)$ (p. 53).

### Definitions
- **D6.1.1 — Fredholm map** (Definition 161, p. 52). $F\in C^\infty(X;Y)$ is Fredholm if the differential $d_xF$ is a Fredholm linear map at each point. $\operatorname{index}d_xF$ is then well defined; if $X$ is connected it is independent of $x$ and denoted $\operatorname{index}F$.
- **D6.1.2 — Regular value** (in Corollary 163, p. 52). $0$ is a regular value of $F$ if $d_pF$ is surjective for all $p\in F^{-1}(0)$.
- **D6.1.3 — Set of second category** (unlabelled, p. 53). A subset $A$ of a topological space is of second category if it is a countable intersection of open dense subsets. In a Banach manifold such a set is dense (Baire).
- **D6.1.4 — Transversality to a submanifold** (unlabelled, p. 53). For $Z\subset Y$ a smoothly embedded finite-dimensional submanifold, $F$ is transverse to $Z$ if for any $z\in Z$ and any $x\in F^{-1}(Z)$ (with $F(x)=z$): $\operatorname{Im}d_xF+T_zZ=T_zY$. For $Z=\{z\}$ this says $z$ is a regular value.

### Theorems
- **T6.1.1 — Kuranishi model** (Theorem 162, p. 52). Let $X,Y$ be Banach spaces and $F\colon X\to Y$ a Fredholm map. Pick $p\in F^{-1}(0)$, set $X_0:=\ker d_pF$, $Y_0:=\operatorname{im}d_pF$, and choose complements $X=X_0\oplus X_1$, $Y=Y_0\oplus Y_1$. Then there is a diffeomorphism $\phi$ of a neighbourhood of the origin in $X$ onto a neighbourhood of $p$ with $\phi(0)=p$, a linear isomorphism $T\colon X_1\to Y_0$, and a smooth map $f\colon X\to Y_1$ such that $F\circ\phi(x_0,x_1)=Tx_1+f(x_0,x_1)$ for all $(x_0,x_1)\in X_0\oplus X_1$ near the origin. In particular, with $f_0\colon X_0\to Y_1$ the restriction of $f$ to $X_0$ (i.e. $f_0(x_0)=f(x_0,0)$), a neighbourhood of $p$ in $F^{-1}(0)$ is homeomorphic to a neighbourhood of the origin in $f_0^{-1}(0)$.
  `Proof in source: omitted.`
- **T6.1.2 — Regular value ⇒ zero set is a manifold of dimension index** (Corollary 163, p. 52). Under the hypotheses of Theorem 162, if $0$ is a regular value of $F$, then $F^{-1}(0)$ is a smooth manifold of dimension $\operatorname{index}F$.
  `Proof in source: full (short).` $\operatorname{Im}d_pF=Y$ forces $Y_1=\{0\}$, so $f_0$ is constant (zero); hence $F^{-1}(0)$ is locally diffeomorphic to a neighbourhood of $0$ in $X_0$, of dimension $\dim X_0=\operatorname{index}F$ (cokernel is zero).
- **T6.1.3 — Sard–Smale theorem** (Theorem 164, p. 53). Let $F$ be a smooth Fredholm map between paracompact Banach manifolds. Then the set of regular values of $F$ is of second category, in particular dense.
  `Proof in source: omitted.` (Finite-dimensional Sard: [BT03, Thm 9.5.4].)
- **T6.1.4 — Transversal preimage theorem** (Theorem 165, p. 53). Let $Z\subset Y$ be a smoothly embedded finite-dimensional submanifold. If $F$ is transverse to $Z$, then $F^{-1}(Z)$ is a smooth submanifold of $X$ and $\dim F^{-1}(Z)=\operatorname{index}F+\dim Z$.
  `Proof in source: omitted ("just as in the finite dimensional case").`

### Examples: none.
### Exercises: none.

### Remarks / load-bearing paragraphs
- **R6.1.1 — Fredholm maps resemble finite-dimensional maps** (p. 52).
- **R6.1.2 — Transversality generalises regular values** (p. 53; reference [GP10]).

### External results imported without proof
- **I6.1.1 — Kuranishi model / Lyapunov–Schmidt reduction** (Theorem 162) (p. 52).
- **I6.1.2 — Sard's theorem** [BT03, Thm 9.5.4] (p. 53).
- **I6.1.3 — Sard–Smale theorem** (Theorem 164) (p. 53).
- **I6.1.4 — Baire category theorem** (second category sets in Banach manifolds are dense) (p. 53).
- **I6.1.5 — Transversality theorem** (Theorem 165) [GP10] (p. 53).

---

## 6.2 The $\mathbb Z/2\mathbb Z$ degree

`PDF pages: 53–55`

### Standing conventions and notation
- Proper map: preimages of compact sets are compact (p. 53).
- Setting: $F\colon X\to Y$ a proper Fredholm map of index zero between (paracompact) Banach manifolds, $Y$ connected; for a regular value $y$, $F^{-1}(y)$ is a compact 0-manifold, i.e. finite (p. 53).
- $\deg_2F:=\#F^{-1}(y)\bmod2$ (p. 53).
- $\operatorname{Crit}(F)$ critical points; critical values $F(\operatorname{Crit}(F))$ (p. 53).
- $\operatorname{Diff}_0(Y)$ = diffeomorphisms homotopic to the identity (p. 54).
- Homotopy of maps $F_t$, $t\in[0,1]$, is viewed as $F\colon X\times[0,1]\to Y$ (p. 54).

### Definitions
- **D6.2.1 — Proper map** (unlabelled, p. 53). $F\colon X\to Y$ is proper if preimages of compact subsets are compact.
- **D6.2.2 — $\mathbb Z/2\mathbb Z$ degree** (unlabelled, p. 53). For $F\colon X\to Y$ a proper Fredholm map of index zero between paracompact Banach manifolds with $Y$ connected and $y$ a regular value, $\deg_2F:=\#F^{-1}(y)\bmod2$.

### Theorems
- **T6.2.1 — Well-definedness and homotopy invariance of $\deg_2$** (Theorem 166, p. 53). (i) $\deg_2F$ does not depend on the choice of the regular value $y$. (ii) If $F_0$ and $F_1$ are homotopic within the class of proper Fredholm maps of vanishing index, then $\deg_2F_0=\deg_2F_1$.
  `Proof in source: full, in six steps.` Step 1: for $F$ proper Fredholm the set of regular values is open and dense — $\operatorname{Crit}(F)$ is closed, proper maps are closed, so $F(\operatorname{Crit}(F))$ is closed; density by Sard–Smale. Step 2: $y\mapsto\#F^{-1}(y)\bmod2$ is locally constant on regular values — for $F^{-1}(y)=\{x_1,\dots,x_k\}$ the inverse function theorem gives neighbourhoods $V_j\ni x_j$, $U\ni y$ with $F\colon V_j\to U$ diffeomorphisms, so $\#F^{-1}(y')=k$ for $y'\in U$ (properness is needed to see that $F^{-1}(U)\subset\bigcup V_j$ after shrinking $U$; not written). Step 3: for $F_0\simeq F_1$ through proper Fredholm maps and $y$ regular for both, $\#F_0^{-1}(y)=\#F_1^{-1}(y)\bmod2$ (167) — if $y$ is regular for the homotopy $F\colon X\times[0,1]\to Y$, $F^{-1}(y)$ is a compact 1-manifold with boundary $F_0^{-1}(y)\cup F_1^{-1}(y)$, so (167) holds; otherwise choose $y_1$ near $y$ regular for $F_0,F_1,F$ and use Step 2. Step 4: for $x$ in the unit ball of a Banach space $B$ there is a diffeomorphism $\phi$ of $B$ with $\phi(0)=x$, $\phi=\mathrm{id}$ outside the ball of radius 2, and $\phi$ homotopic to the identity rel that complement — reduce to finite dimensions: $B=V\oplus V'$ with $V$ finite dimensional, $x\in V$; [Mil97, p. 22] gives $\psi_t\colon V\to V$ with $\psi_0=\mathrm{id}$, $\psi_1(0)=x$, $\psi_t=\mathrm{id}$ outside the unit ball of $V$; choose $\chi\colon\mathbb R_{\ge0}\to\mathbb R_{\ge0}$ smooth with $\chi(0)=1$, $\chi(t)=0$ for $t\ge1$, and set $\phi_t(v,v')=\psi_{t\chi(|v'|)}(v)+v'$; then $\|\phi_t(v,v')\|\le2$ on the unit ball (triangle inequality) and $\phi_t=\mathrm{id}$ where $\|v\|+\|v'\|\ge2$ (either $\|v\|\ge1$ or $\|v'\|\ge1$). Step 5: for $Y$ connected and $y_1,y_2\in Y$ there is $\phi\in\operatorname{Diff}_0(Y)$ with $\phi(y_1)=y_2$ — $C(y_2):=\{y_1\mid\exists\phi\in\operatorname{Diff}_0(Y),\phi(y_1)=y_2\}$ is open and non-empty by Step 4, hence (also closed, by the same argument) equals $Y$. Step 6: for regular values $y_1,y_2$ pick $\phi\in\operatorname{Diff}_0(Y)$ with $\phi(y_1)=y_2$; $y_2$ is a common regular value of $F$ and $\phi\circ F$, which are homotopic, so by Step 3 $\#F^{-1}(y_2)=\#(\phi\circ F)^{-1}(y_2)=\#F^{-1}(y_1)\bmod2$, proving (i). For (ii), choose $y$ regular for $F_0,F_1$ and the homotopy $F$.
  `Gaps:` Step 2 silently uses properness to exclude extra preimages near $y$; Step 3 uses classification of compact 1-manifolds (boundary has an even number of points) and that $F^{-1}(y)$ for the homotopy is a manifold with boundary (needs $y$ regular for $F_0,F_1$ too and a boundary version of Corollary 163); Step 5 needs $C(y_2)$ closed or a connectedness argument ("hence $C(y_2)=Y$" is stated directly); that $\phi\circ F$ is proper Fredholm of index 0 and homotopic to $F$ *within the class* is asserted.
- **T6.2.2 — Nonzero $\deg_2$ implies surjectivity** (Corollary 168, p. 55). Let $F\colon X\to Y$ be a proper Fredholm map of index zero between paracompact Banach manifolds, $Y$ connected. If $\deg_2F\ne0$, then $F$ is surjective.
  `Proof in source: omitted.` (Intended: every $y$ is a limit of regular values, each with nonempty preimage; properness/closedness of $F$ gives $y\in\operatorname{Im}F$.)

### Examples: none.
### Exercises: none.

### Remarks / load-bearing paragraphs
- **R6.2.1 — Reduction of Step 4 to a finite-dimensional statement** (p. 54): the explicit cut-off construction $\phi_t(v,v')=\psi_{t\chi(|v'|)}(v)+v'$.

### External results imported without proof
- **I6.2.1 — Inverse function theorem on Banach manifolds** (Step 2, p. 54).
- **I6.2.2 — Classification of compact 1-manifolds with boundary** (Step 3, p. 54; boundary point count is even).
- **I6.2.3 — Isotopy lemma** [Mil97, p. 22]: a 1-parameter family of diffeomorphisms of a finite-dimensional vector space moving $0$ to a given point of the unit ball, supported in the unit ball (p. 54).
- **I6.2.4 — Proper maps are closed** (p. 53).

---

## 6.3 The parametric transversality

`PDF pages: 55–56`

### Standing conventions and notation
- $W$ a connected Banach manifold of parameters; $\mathcal F\colon X\times W\to Y$ smooth Fredholm; $\mathcal F_w:=\mathcal F|_{X\times\{w\}}$ (p. 55).
- Hypotheses: (A) each $\mathcal F_w$ is Fredholm; (B) there is $w_0$ with $\mathcal F_{w_0}=F$; (C) $y$ is a regular value of $\mathcal F$; (D) each $\mathcal F_w$ is proper (pp. 55–56). Standing assumption $\operatorname{index}F=0$ for the degree discussion (not essential).
- $\pi\colon\mathcal F^{-1}(y)\to W$ restriction of the projection $X\times W\to W$ (p. 55).
- $W_0\subset W$ the second-category set of $w$ with $y$ regular for $\mathcal F_w$ (p. 55).
- Path space $\Gamma(w_1,w_2):=\{\gamma\in C^k([1,2];W)\mid\gamma(1)=w_1,\gamma(2)=w_2\}$, a Banach manifold, $k\ge0$ fixed; $\mathbb F\colon X\times\Gamma(w_1,w_2)\times[1,2]\to Y$, $\mathbb F(x,\gamma,t):=\mathcal F(x,\gamma(t))$; $M_\gamma:=\{(x,t)\mid\mathcal F(x,\gamma(t))=y\}$ (p. 56).

### Definitions
- **D6.3.1 — Parametric family (hypotheses (A)–(D))** (unlabelled, pp. 55–56). As in the conventions: a connected Banach manifold $W$ and a smooth Fredholm $\mathcal F\colon X\times W\to Y$ with (A) $\mathcal F_w$ Fredholm for every $w$; (B) $\mathcal F_{w_0}=F$ for some $w_0$; (C) $y$ regular value of $\mathcal F$; (D) each $\mathcal F_w$ proper.
- **D6.3.2 — Degree via a generic parameter (alternative definition)** (unlabelled, p. 56). Under (A)–(D) with $\operatorname{index}F=0$: $\deg_2F:=\#\mathcal F_w^{-1}(y)\bmod2$ for any $w\in W_0$.

### Theorems
- **T6.3.1 — Projection from the universal zero set is Fredholm; generic parameters are regular** (Lemma 169, p. 55). Under (A)–(C): (i) $\pi\colon\mathcal F^{-1}(y)\to W$ is a Fredholm map and $\operatorname{index}\pi=\operatorname{index}F$; (ii) there is a subset $W_0\subset W$ of second category such that $y$ is a regular value of $\mathcal F_w$ for all $w\in W_0$.
  `Proof in source: omitted.` (Intended: $\ker d\pi=\ker d_x\mathcal F_w$ and $\operatorname{coker}d\pi\cong\operatorname{coker}d_x\mathcal F_w$ by the snake-lemma argument on $d\mathcal F=(d\mathcal F_w,\partial_w\mathcal F)$ surjective; (ii) is Sard–Smale applied to $\pi$ since $w$ regular for $\pi$ iff $y$ regular for $\mathcal F_w$.)
- **T6.3.2 — Independence of $\#\mathcal F_w^{-1}(y)\bmod2$ from $w\in W_0$** (unlabelled, p. 56). Under (A)–(D), $\operatorname{index}F=0$: for $w_1,w_2\in W_0$, $\#\mathcal F_{w_1}^{-1}(y)=\#\mathcal F_{w_2}^{-1}(y)\bmod2$; the common value is $\deg_2F$.
  `Proof in source: full (two arguments).` First: $W$ connected ⇒ path from $w_0$ to $w$ ⇒ $\mathcal F_w\simeq\mathcal F_{w_0}=F$ ⇒ $\deg_2F=\#\mathcal F_w^{-1}(y)\bmod2$ by Theorem 166. Second (self-contained, avoiding §6.2): $y$ is a regular value of $\mathbb F$; apply Sard–Smale to the projection $\mathbb F^{-1}(y)\to\Gamma(w_1,w_2)$ to get, for generic $\gamma$, that $M_\gamma$ is a smooth 1-dimensional submanifold of $X\times[1,2]$ with $\partial M_\gamma=\mathcal F_1^{-1}(y)\cup\mathcal F_2^{-1}(y)$ ($\mathcal F_j:=\mathcal F_{w_j}$); hence the parities agree.
  `Gaps:` compactness of $M_\gamma$ (from properness) and the boundary statement are asserted; regularity of $y$ for $\mathbb F$ is "clear".

### Examples: none.
### Exercises: none.

### Remarks / load-bearing paragraphs
- **R6.3.1 — Why parametric transversality** (p. 55). One cannot always choose $y$ freely: in equivariant settings $y$ must be a fixed point of the $G$-action on $Y$ so that $F^{-1}(y)$ inherits the action; Sard–Smale does not apply directly. Remedy: perturb the map by a parameter $w$ instead of the value $y$. "Typically it is not too hard to construct" such $\mathcal F$.
- **R6.3.2 — $\mathcal F^{-1}(y)$ is a Banach submanifold** (p. 55): by (C) and Theorem 165/Cor. 163.
- **R6.3.3 — The parametric count as a *definition* of the degree** (p. 56): the count $\#\mathcal F_w^{-1}(y)\bmod2$ can be taken as the definition, bypassing §6.2; this is what is used in the equivariant setting.

### External results imported without proof
- **I6.3.1 — Lemma 169** (Fredholmness of $\pi$, index equality, genericity) (p. 55).
- **I6.3.2 — $C^k([1,2];W)$ path spaces are Banach manifolds** (p. 56).
- **I6.3.3 — Sard–Smale** (again, p. 56).

---

## 6.4 The determinant line bundle

`PDF pages: 56–57`

### Standing conventions and notation
- $\operatorname{Fred}(X;Y)$ = space of linear Fredholm maps $X\to Y$ with the operator-norm topology; a continuous family is a continuous map $P\to\operatorname{Fred}(X;Y)$, $p\mapsto T_p$ (pp. 56–57).
- **Determinant line:** $\det T_p:=\Lambda^{\mathrm{top}}\ker T_p\otimes\Lambda^{\mathrm{top}}(\operatorname{coker}T_p)^*$ (real line) (p. 57).
- Stabilisation: $V\subset Y$ finite dimensional transverse to $\operatorname{Im}T_{p_0}$; $T_{p,V}\colon X\oplus V\to Y$, $T_{p,V}(x,v)=T_px+v$; exact sequence (170) $0\to\ker T_p\to\ker T_{p,V}\to V\to V/(\operatorname{Im}T_p\cap V)\to0$; $\operatorname{coker}T_p=(\operatorname{Im}T_p+V)/\operatorname{Im}T_p=V/(\operatorname{Im}T_p\cap V)$ (p. 57).
- Finite-dimensional degree needs orientations [GP10]; orientation in infinite dimensions is replaced by trivialisations of $\det$ (p. 56).

### Definitions
- **D6.4.1 — Continuous family of Fredholm operators** (unlabelled, pp. 56–57). $P$ a topological space, $\{T_p\mid p\in P\}$ with $P\to\operatorname{Fred}(X;Y)$, $p\mapsto T_p$, continuous in operator norm.
- **D6.4.2 — Determinant line and determinant line bundle** (unlabelled, p. 57). $\det T_p:=\Lambda^{\mathrm{top}}\ker T_p\otimes\Lambda^{\mathrm{top}}(\operatorname{coker}T_p)^*$; the family $\{\det T_p\}$ is a locally trivial real line bundle $\det T\to P$ (non-obvious since $\dim\ker$, $\dim\operatorname{coker}$ jump).
- **D6.4.3 — Homotopic families of Fredholm operators** (Definition 172, p. 57). Two continuous families $\{T_{p,i}\mid p\in P\}$, $i\in\{0,1\}$, are homotopic if there is a continuous family $\{T_{p,t}\mid(p,t)\in P\times[0,1]\}$ restricting to the given families on $P\times\{0\}$ and $P\times\{1\}$.

### Theorems
- **T6.4.1 — Local triviality of the determinant line bundle** (unlabelled, p. 57). $\{\det T_p\}$ is a locally trivial line bundle over $P$.
  `Proof in source: sketch.` Near $p_0$ choose finite-dimensional $V\subset Y$ transverse to $\operatorname{Im}T_{p_0}$; $T_{p,V}$ is surjective at $p_0$, hence for $p$ near $p_0$; exact sequence (170) and Exercise 171 give a canonical isomorphism $\det T_p\cong\Lambda^{\mathrm{top}}\ker T_{p,V}\otimes\Lambda^{\mathrm{top}}V^*$; "it can be shown" that $\dim\ker T_{p,V}$ is constant near $p_0$ and moreover $\ker T_{p,V}$ is a trivial bundle over a neighbourhood $W$ of $p_0$ [MS12, Thm A.2.2]; hence $\det T$ is trivial over $W$.
  `Gaps:` openness of surjectivity; local triviality of $\ker T_{p,V}$ cited; compatibility of the trivialisations on overlaps (independence of $V$) not discussed.
- **T6.4.2 — Homotopy invariance of triviality of $\det$** (Proposition 173, p. 57). Let $\{T_{p,0}\}$ and $\{T_{p,1}\}$ be homotopic families of Fredholm operators such that $\det T_{p,1}$ is trivial. Then $\det T_{p,0}$ is also trivial. Moreover, a choice of a trivialisation of $\det T_{p,1}$ and a homotopy $\{T_{p,t}\}$ yields a trivialisation of $\det T_{p,0}$, unique up to multiplication with a positive function.
  `Proof in source: sketch (preceding paragraph).` $P\times[0,1]\simeq P$, so $\det T_{p,t}$ over $P\times[0,1]$ is trivial iff its restriction to $P\times\{1\}$ is; restrict to $P\times\{0\}$.

### Examples: none.

### Exercises
- **X6.4.1** (Exercise 171, p. 57). Let $0\to U_0\to U_1\to U_2\to0$ be a short exact sequence of real vector spaces. Show that the "inner product map" $\Lambda^{\mathrm{top}}U_0\otimes\Lambda^{\mathrm{top}}U_1^*\to\Lambda^{\mathrm{top}}(U_1/U_0)^*=\Lambda^{\mathrm{top}}U_2^*$ induces an isomorphism $\Lambda^{\mathrm{top}}U_1\cong\Lambda^{\mathrm{top}}U_0\otimes\Lambda^{\mathrm{top}}U_2$. More generally, show that for any exact sequence $0\to U_0\to U_1\to\cdots\to U_k\to0$ of real vector spaces there is a canonical isomorphism $\bigotimes\Lambda^{\mathrm{top}}U_{\mathrm{even}}\cong\bigotimes\Lambda^{\mathrm{top}}U_{\mathrm{odd}}$.

### Remarks / load-bearing paragraphs
- **R6.4.1 — Why determinant lines** (p. 56): $\mathbb Z$-valued degree needs orientations; in infinite dimensions replace by $\det$.
- **R6.4.2 — Stabilisation argument** (p. 57): the exact sequence (170) and $\operatorname{coker}T_p=V/(\operatorname{Im}T_p\cap V)$.

### External results imported without proof
- **I6.4.1 — Local triviality of $\ker T_{p,V}$** [MS12, Thm A.2.2] (p. 57).
- **I6.4.2 — Openness of surjectivity of bounded operators with finite-dimensional cokernel** (p. 57).
- **I6.4.3 — Homotopy invariance of line bundles** ($P\times[0,1]\simeq P$; a line bundle over $P\times[0,1]$ is trivial iff its restriction to a slice is) (p. 57).
- **I6.4.4 — Finite-dimensional $\mathbb Z$-valued degree theory** [GP10] (p. 56).

---

## 6.5 Orientations and the $\mathbb Z$-valued degree

`PDF pages: 58–59`

### Standing conventions and notation
- $X,Y,W$ Banach manifolds; $F\colon X\times W\to Y$ smooth with (a) $F_w:=F|_{X\times\{w\}}$ Fredholm of index $d$ for each $w$; (b) $y\in Y$ regular value of $F$; (c) $F_w^{-1}(y)$ compact for every $w$; (d) $\det d_xF_w$ trivial over $X\times W$, with a fixed trivialisation (p. 58).
- $\mathcal M_w:=F_w^{-1}(y)$; for $y$ regular for $F_w$ and $x\in\mathcal M_w$: $\det d_xF_w=\Lambda^{\mathrm{top}}\ker d_xF_w=\Lambda^{\mathrm{top}}T_x\mathcal M_w$ (cokernel zero), so $\mathcal M_w$ is an oriented $d$-manifold (p. 58).
- Path $\gamma\colon[0,1]\to W$ from $w_0$ to $w_1$; $\mathcal M_\gamma:=\{(x,t)\in X\times[0,1]\mid F_{\gamma(t)}(x)=y\}$; for generic $\gamma$, oriented $(d+1)$-manifold with $\partial\mathcal M_\gamma=\mathcal M_{w_1}\sqcup\overline{\mathcal M_{w_0}}$ (174), the bar denoting reversed orientation (p. 58).
- $d=0$: $\mathcal M_w=\{m_1,\dots,m_k\}$ with signs $\varepsilon_i$; $\deg F_w:=\sum_i\varepsilon_i\in\mathbb Z$ (175) (the source prints $\sum\varepsilon_k$) (p. 58).
- Characteristic classes $\alpha_1,\dots,\alpha_k$ of a bundle $P\to X$ with $\alpha:=\alpha_1\cup\cdots\cup\alpha_k\in H^d(X;\mathbb Z)\subset H^d(X;\mathbb R)$; pairing $\langle\alpha,[\mathcal M_w]\rangle=\int_{\mathcal M_w}\omega$ (p. 59).

### Definitions
- **D6.5.1 — Oriented parametric family (hypotheses (a)–(d))** (unlabelled, p. 58). As in the conventions.
- **D6.5.2 — $\mathbb Z$-valued degree** (equation (175), p. 58). For $d=0$ and $w$ with $y$ regular for $F_w$, $\deg F_w:=\sum_{i=1}^k\varepsilon_i\in\mathbb Z$, where $\varepsilon_i=\pm1$ is the sign of the point $m_i\in\mathcal M_w$ determined by comparing the trivialisation of $\det d_{m_i}F_w=\Lambda^{\mathrm{top}}\{0\}=\mathbb R$ with the canonical one.
- **D6.5.3 — Oriented cobordism class of $\mathcal M_w$; numerical invariants** (unlabelled, pp. 58–59). For general $d\ge0$ the oriented cobordism class $[\mathcal M_w]$ is independent of $w$ in the dense set of good parameters; given $P\to X$ and characteristic classes with $\alpha\in H^d(X;\mathbb Z)$, the integer $\langle\alpha,[\mathcal M_w]\rangle=\int_{\mathcal M_w}\omega$ ($\omega$ a closed $d$-form representing $\alpha|_{\mathcal M_w}$) is independent of $w$ by Stokes.

### Theorems
- **T6.5.1 — Independence of the $\mathbb Z$-degree from the parameter** (Theorem 176, p. 58). Assume $F\colon X\times W\to Y$ satisfies (a)–(d) (with $d=0$). Then $\deg F_w$ does not depend on $w$ (for $w$ in a connected $W$ with $y$ regular for $F_w$).
  `Proof in source: sketch ("summarises the considerations above").` For generic $\gamma$ from $w_0$ to $w_1$, $\mathcal M_\gamma$ is an oriented compact 1-manifold with $\partial\mathcal M_\gamma=\mathcal M_{w_1}\sqcup\overline{\mathcal M_{w_0}}$, so signed counts agree.
  `Gaps:` orientation of $\mathcal M_\gamma$ from the trivialisation of $\det$ over $X\times W$ (via $\det d\mathcal F\cong\det d_xF_w\otimes\Lambda^{\mathrm{top}}T[0,1]$) not written; compactness of $\mathcal M_\gamma$ from (c) plus properness in the parameter direction is assumed; boundary orientation convention (174) is asserted.
- **T6.5.2 — Cobordism invariance and characteristic numbers** (unlabelled, pp. 58–59). For any $d\ge0$, $\mathcal M_{w_0}$ and $\mathcal M_{w_1}$ are oriented-cobordant for good $w_0,w_1$; $\langle\alpha,[\mathcal M_w]\rangle$ is an integer independent of $w$.
  `Proof in source: sketch (Stokes' theorem).`

### Examples: none.
### Exercises: none.

### Remarks / load-bearing paragraphs
- **R6.5.1 — Orientation of $\mathcal M_w$ from a trivialisation of $\det$** (p. 58): at a regular point $\det d_xF_w=\Lambda^{\mathrm{top}}T_x\mathcal M_w$.
- **R6.5.2 — From cobordism class to a number** (pp. 58–59): cobordism classes are hard to handle; pair with characteristic classes of a bundle over $X$ (this is how the Seiberg–Witten invariant will be defined in §7.2).

### External results imported without proof
- **I6.5.1 — Stokes' theorem** (p. 59).
- **I6.5.2 — Boundary orientation convention** for $\partial\mathcal M_\gamma$ (p. 58).
- **I6.5.3 — Integrality: $[\omega]$ integral ⇒ $\int_{\mathcal M_w}\omega\in\mathbb Z$** (p. 59).

---

## 6.6 An equivariant setup

`PDF pages: 59–60`

### Standing conventions and notation
- $X$ a Banach (later Hilbert) manifold with an action of a Banach (Hilbert) Lie group $G$; infinitesimal action $R_x\colon\operatorname{Lie}(G)\to T_xX$ (177), image = tangent space to the orbit (p. 59).
- Simplifying assumptions: $G$ acts **freely** on $X$; $X$ and $G$ are Hilbert manifolds (p. 59).
- $Y$ a smooth manifold with a $G$-action; $F\colon X\times W\to Y$ with each $F_w$ $G$-equivariant; $y$ a fixed point ($g\cdot y=y$ for all $g$) (p. 59).
- Deformation complex at $x\in F_w^{-1}(y)$ (181): $0\to\operatorname{Lie}(G)\xrightarrow{R_x}T_xX\xrightarrow{d_xF_w}T_yY\to0$ (p. 59).
- $D_x:=(R_x^*,d_xF_w)\colon T_xX\to\operatorname{Lie}(G)\oplus T_yY$ (182), using the Hilbert structure for $R_x^*$ (p. 60).
- $\mathcal M_w:=F_w^{-1}(y)/G$ (p. 60).

### Definitions
- **D6.6.1 — Infinitesimal action** (equation (177), p. 59). $R_x\colon\operatorname{Lie}(G)\to T_xX$, whose image is the tangent space to the orbit $G\cdot x$.
- **D6.6.2 — Local slice** (Definition 178, p. 59). A Hilbert submanifold $S\subset X$ containing $x$ is a local slice of the $G$-action at $x$ if $GS:=\{g\cdot s\mid g\in G,s\in S\}$ is open in $X$ and the natural map $G\times S\to GS$, $(g,s)\mapsto g\cdot s$, is a diffeomorphism.
- **D6.6.3 — Deformation complex** (equation (181), p. 59). For $x\in F_w^{-1}(y)$: $0\to\operatorname{Lie}(G)\xrightarrow{R_x}T_xX\xrightarrow{d_xF_w}T_yY\to0$; it is a complex ($d_xF_w\circ R_x=0$) by equivariance of $F_w$ and $y$ being fixed. Cohomology: $H^0$ = Lie algebra of the stabiliser of $x$ (trivial under the freeness assumption); $H^1=\ker d_xF_w/\operatorname{Im}R_x$ = tangent space to the "moduli space" $\mathcal M_w=F_w^{-1}(y)/G$ at $G\cdot x$ ($\ker d_xF_w$ is the Zariski tangent space to $F_w^{-1}(y)$); $H^2=\operatorname{coker}d_xF_w$, trivial iff $y$ is a regular value of $F_w$.
- **D6.6.4 — The operator $D_x$** (equation (182), p. 60). $D_x:=(R_x^*,d_xF_w)\colon T_xX\to\operatorname{Lie}(G)\oplus T_yY$; $\ker D_x\cong H^1$ of the deformation complex.

### Theorems
- **T6.6.1 — Slices give a manifold quotient** (Proposition 179, p. 59). Assume $G$ acts freely on $X$. If the $G$-action admits a slice at every point, then $X/G$ is a manifold.
  `Proof in source: sketch ("clear"):` $S$ is identified with a neighbourhood of the orbit $G\cdot x$ in $X/G$.
  `Gaps:` Hausdorffness of $X/G$ and compatibility of charts not discussed.
- **T6.6.2 — Equivariant moduli space is a manifold of dimension $\operatorname{index}D_x$** (Theorem 183, p. 60). Let $y$ be a fixed point of the $G$-action on $Y$. Assume: (i) $G$ acts freely on $X$; (ii) $y$ is a regular value of $F_w$; (iii) there is a local slice at each $x\in F_w^{-1}(y)$; (iv) $D_x$ is a Fredholm linear map of index $d$. Then $\mathcal M_w=F_w^{-1}(y)/G$ is a smooth manifold of dimension $d$.
  `Proof in source: full (short).` Local statement; let $S$ be a slice at $x$ so that $T_xS$ and $\operatorname{Im}R_x$ are complementary in $T_xX$ (the source writes $\operatorname{Im}R_w$). Then $y$ is still a regular value of $F_w|_S$ and $\ker d_x(F_w|_S)=\ker(R_x^*,d_xF_w)$, so $F_w^{-1}(y)\cap S$ is a manifold of dimension $\dim\ker D_x=d$.
  `Gaps:` the identification $\ker d_x(F_w|_S)=\ker D_x$ requires $T_xS=(\operatorname{Im}R_x)^\perp=\ker R_x^*$, i.e. the slice must be the orthogonal one (as in §7.1.5); $\dim\ker D_x=d$ uses $\operatorname{coker}D_x=0$, i.e. surjectivity of $R_x^*$ on the complement (freeness ⇒ $R_x$ injective with closed range) plus (ii); regularity of $y$ for $F_w|_S$ from $\operatorname{Im}d_xF_w=\operatorname{Im}d_x(F_w|_S)$ (since $d_xF_w$ kills $\operatorname{Im}R_x$).
- **T6.6.3 — Orientation and bordism invariance in the equivariant setting** (Theorem 184, p. 60). Assume in addition to (i)–(iv) of Theorem 183 that the determinant line bundle $\det D_x$ is trivialised and this trivialisation is preserved by the action of $G$. Then $\mathcal M_w$ is oriented. If in addition $\mathcal M_w$ is compact for any $w$, then the oriented bordism class of $\mathcal M_w$ does not depend on $w$.
  `Proof in source: omitted ("by tracing through the discussion of Section 6.5").`

### Examples
- **E6.6.1 — Slice for the rotation action on $S^2$** (Example 180, p. 59). $U(1)$ acts on $S^2$ by rotations about the $z$-axis; removing the poles the action is free; $S:=\{(x,0,z)\mid x^2+z^2=1,x>0\}\cong(-1,1)$ is a global slice; the quotient is a manifold, diffeomorphic to an interval.

### Exercises: none.

### Remarks / load-bearing paragraphs
- **R6.6.1 — Interpretation of the cohomology of the deformation complex** (pp. 59–60): $H^0$ = stabiliser Lie algebra; $H^1$ = tangent space of the moduli space; $H^2$ = obstruction ($\operatorname{coker}d_xF_w$).
- **R6.6.2 — Passage from the complex to the single operator $D_x$** (p. 60): the Hilbert structure lets one fold the complex into $D_x=(R_x^*,d_xF_w)$ with $\ker D_x=H^1$ (cf. Exercise 159).

### External results imported without proof
- **I6.6.1 — Slice theorem framework** (existence of slices is a hypothesis, not proved) (p. 59).
- **I6.6.2 — Theorem 184** (orientation/bordism in the equivariant case) stated without proof (p. 60).

---

## 7.1 The Seiberg–Witten equations

`PDF pages: 61–70`

### Standing conventions and notation (whole of §7.1)
- $M$ (also written $X$ in places) a closed oriented Riemannian four-manifold with a spin$^c$ structure $\sigma$; $\slashed S^\pm$ the spinor bundles; $L_{\det}$, $P_{\det}$ the determinant line bundle and its $U(1)$-bundle; $\mathcal A(P_{\det})$ unitary connections on $L_{\det}$ (p. 61).
- Isomorphisms: $\mathbb R^4\otimes\mathbb C\cong\operatorname{Hom}(\slashed S^+;\slashed S^-)$ (185) as $Spin(4)$- and $Spin^c(4)$-representations; monomorphism $\mathbb R^4\to\operatorname{Hom}(\slashed S^+;\slashed S^-)$, $v\mapsto(\psi\mapsto v\cdot\psi)$; also $\mathbb R^4\to\operatorname{Hom}(\slashed S^-;\slashed S^+)$; Clifford multiplication $\Lambda^2\mathbb R^4\to\operatorname{End}(\slashed S^\pm)$ has kernel $\Lambda^2_\mp\mathbb R^4$ and skew-Hermitian image, giving $\Lambda^2_+\mathbb R^4\cong\mathfrak{su}(\slashed S^+)$ and $\Lambda^2_+\mathbb R^4\otimes\mathbb C\cong\operatorname{End}_0(\slashed S^+)$ (p. 61).
- **Quadratic map:** $\mu\colon\slashed S^+\to i\,\mathfrak{su}(\slashed S^+)\subset\operatorname{End}_0(\slashed S^+)$, $\mu(\psi)=\psi\psi^*-\tfrac12|\psi|^2$, i.e. $\mu(\psi)(\phi)=\langle\phi,\psi\rangle\psi-\tfrac12|\psi|^2\phi$ (the source prints $+\tfrac12|\psi|^2\phi$ in the expanded form, inconsistent with the matrix form; the traceless version has the minus sign); explicitly $\mathbb C^2\to i\,\mathfrak{su}(2)$, $\begin{pmatrix}\psi_1\\\psi_2\end{pmatrix}\mapsto\tfrac12\begin{pmatrix}|\psi_1|^2-|\psi_2|^2&2\psi_1\bar\psi_2\\2\bar\psi_1\psi_2&|\psi_2|^2-|\psi_1|^2\end{pmatrix}$; $\mu(\psi)$ is regarded as a purely imaginary self-dual 2-form (p. 61). Global versions: $T^*_{\mathbb C}M\cong\operatorname{Hom}(\slashed S^+;\slashed S^-)$ (186), $i\Lambda^2_+T^*M\cong i\,\mathfrak{su}(\slashed S^+)$ (187), $\mu\colon\slashed S^+\to i\Lambda^2_+T^*M$ fibrewise quadratic; polarisation $\mu(\cdot,\cdot)$ (p. 61, 63).
- **Seiberg–Witten equations** for $(\psi,A)\in\Gamma(\slashed S^+)\times\mathcal A(P_{\det})$: $\slashed D_A^+\psi=0$ and $F_A^+=\mu(\psi)$ (188). **Seiberg–Witten map** $SW\colon\Gamma(\slashed S^+)\times\mathcal A(P_{\det})\to\Gamma(\slashed S^-)\times\Omega^2_+(M;\mathbb Ri)$, $SW(\psi,A)=(\slashed D_A^+\psi,F_A^+-\mu(\psi))$ (p. 61). Remark 197: the sign $F_A^+=-\mu(\psi)$ would break the $C^0$-estimate.
- **Gauge group:** $\mathcal G:=\mathcal G(P_{\det})\cong C^\infty(M;U(1))$; right action on connections $A\cdot g=A+2g^{-1}dg$ (189) (the factor 2 because $L_{\det}=\Lambda^2\slashed S^+$, cf. R4.3.5); on configurations $(\psi,A)\cdot g=(\bar g\psi,A\cdot g)$; left action on $\Gamma(\slashed S^-)$ by $g\cdot\phi=\bar g\phi$ (the "obvious" one, made explicit in Lemma 190) and trivially on $\Omega^2_+(M;\mathbb Ri)$ (p. 62).
- Irreducible / reducible: $(\psi,A)$ irreducible iff $\psi\not\equiv0$ iff trivial stabiliser; reducible iff $\psi\equiv0$ (stabiliser = constant maps $U(1)$) (p. 62).
- **Deformation complex** (191): $0\to\Omega^0(M;\mathbb Ri)\xrightarrow{R_{(\psi,A)}}\Gamma(\slashed S^+)\oplus\Omega^1(M;\mathbb Ri)\xrightarrow{d_{(\psi,A)}SW}\Gamma(\slashed S^-)\oplus\Omega^2_+(M;\mathbb Ri)\to0$; $R_{(\psi,A)}\xi=(-\xi\psi,2d\xi)$; $d_{(\psi,A)}SW(\dot\psi,\dot a)=(\slashed D_A^+\dot\psi+\tfrac12\dot a\cdot\psi,\ d^+\dot a-2\mu(\psi,\dot\psi))$ (pp. 62–63). $d^+$ = projection of $d\dot a$ to self-dual forms.
- Atiyah complex $0\to\Omega^0(X)\xrightarrow d\Omega^1(X)\xrightarrow{d^+}\Omega^2_+(X)\to0$ (p. 63).
- **Sobolev completions:** $\mathcal A^{k,p}(P_{\det}):=A_0+W^{k,p}(T^*M\otimes\mathbb Ri)$; $\mathcal G^{k,p}$ = maps $M\to S^1$ of class $W^{k,p}$ (via $S^1\subset\mathbb R^2$), a Banach Lie group for $kp>4$ with $\operatorname{Lie}(\mathcal G^{k,p})=W^{k,p}(M;\mathbb Ri)$; **fixed choice $(k,p)=(5,2)$:** $\mathcal C^{5,2}:=W^{5,2}(\slashed S^+)\times\mathcal A^{5,2}(P_{\det})$, gauge group $\mathcal G^{6,2}$, $SW\colon\mathcal C^{5,2}\to W^{4,2}(\slashed S^-)\times W^{4,2}(\Lambda^2_+T^*M\otimes\mathbb Ri)$ (pp. 63–64).
- $\mathcal C^{5,2}_{\mathrm{irr}}:=\{(\psi,A)\in\mathcal C^{5,2}\mid\psi\not\equiv0\}$ (p. 67). $R^*_{(\psi,A)}(\dot\psi,\dot a)=2d^*\dot a+i\operatorname{Re}\langle\psi,i\dot\psi\rangle$, $\langle\cdot,\cdot\rangle$ the Hermitian product on spinors (p. 67).
- Perturbed map $SW(\psi,A,\eta)=(\slashed D_A^+\psi,F_A^+-\mu(\psi)-\eta)$, $\eta\in W^{4,2}(\Lambda^2_+T^*M\otimes\mathbb Ri)$; $SW_\eta$; $\mathcal M^{\mathrm{irr}}_\eta$; $\mathcal M_\eta$ (pp. 68–69).
- $D_{(\psi,A)}:=(d_{(\psi,A)}SW_\eta,R^*_{(\psi,A)})$ (214); $D_0:=\slashed D_A^+\oplus(d^++d^*)$; $D_{(\psi,A)}=D_0+B$ with $B$ of order zero (215) (p. 69).
- Topological data: $\chi(M)$ Euler characteristic, $\operatorname{sign}(M):=b_2^+-b_2^-$, $b_1,b_0,b_2^+$; $c_1(L_{\det})^2:=\langle c_1(L_{\det})\cup c_1(L_{\det}),[M]\rangle$; $c_1(L_{\det})$ represented by $\tfrac{i}{2\pi}F_A$ (pp. 65, 69).
- Dimension formula (213): $d=\tfrac14\big(c_1(L_{\det})^2-2\chi(M)-3\operatorname{sign}(M)\big)$ (p. 69).
- $\ker(d^++d^*)=H^1_{dR}(M;\mathbb Ri)$, $\operatorname{coker}(d^++d^*)=H^0(M;\mathbb Ri)\oplus H^2_+(M;\mathbb Ri)$; $\operatorname{index}(d^++d^*)=b_1-b_0-b_2^+=-\tfrac12(\chi+\operatorname{sign})$ (the source prints $=\tfrac12(\chi+\operatorname{sign})$ with the wrong sign; see T7.1.16 gaps); $\operatorname{index}_{\mathbb C}\slashed D_A^+=\tfrac18(c_1(L_{\det})^2-\operatorname{sign})$ (pp. 69–70).
- Orientation convention for complex spaces: either $(v_1,\dots,v_k,iv_1,\dots,iv_k)$ or $(v_1,iv_1,\dots,v_k,iv_k)$; these differ when $k$ is even (Remark 221, p. 70).

### 7.1.0 The equations — `PDF page: 61`

#### Definitions
- **D7.1.1 — The quadratic map $\mu$** (unlabelled, p. 61). $\mu\colon\slashed S^+\to i\,\mathfrak{su}(\slashed S^+)$, $\mu(\psi)=\psi\psi^*-\tfrac12|\psi|^2\,\mathrm{id}$, equivalently the explicit matrix above; via (187) a fibrewise quadratic map $\mu\colon\slashed S^+\to i\Lambda^2_+T^*M$.
- **D7.1.2 — Seiberg–Witten equations and Seiberg–Witten map** (equation (188), p. 61). For $(\psi,A)\in\Gamma(\slashed S^+)\times\mathcal A(P_{\det})$: $\slashed D_A^+\psi=0$, $F_A^+=\mu(\psi)$. $SW(\psi,A):=(\slashed D_A^+\psi,F_A^+-\mu(\psi))\in\Gamma(\slashed S^-)\times\Omega^2_+(M;\mathbb Ri)$.

#### Theorems
- **T7.1.1 — Linear-algebraic identifications in dimension 4** (unlabelled, p. 61). (185) holds for $Spin^c(4)$; $\Lambda^2\mathbb R^4\to\operatorname{End}(\slashed S^\pm)$ has kernel $\Lambda^2_\mp\mathbb R^4$ ("a straightforward computation shows"); image skew-Hermitian; $\Lambda^2_+\mathbb R^4\cong\mathfrak{su}(\slashed S^+)$; complexification $\Lambda^2_+\otimes\mathbb C\cong\operatorname{End}_0(\slashed S^+)$ (cf. (111)).
  `Proof in source: omitted.`

#### Remarks
- **R7.1.1 — $\mu(\psi)$ as an imaginary self-dual 2-form** (p. 61): composition of $\psi\mapsto\psi\psi^*-\tfrac12|\psi|^2$ with (187).

### 7.1.1 The gauge group action — `PDF page: 62`

#### Definitions
- **D7.1.3 — Gauge group and its action on configurations** (equation (189), p. 62). $\mathcal G:=\mathcal G(P_{\det})\cong C^\infty(M;U(1))$; $A\cdot g=A+2g^{-1}dg$; $(\psi,A)\cdot g=(\bar g\psi,A\cdot g)$ (right action on $\Gamma(\slashed S^+)\times\mathcal A(P_{\det})$); left action on $\Gamma(\slashed S^-)\times\Omega^2_+(M;\mathbb Ri)$ by $\bar g$ on spinors and trivially on forms.
- **D7.1.4 — Seiberg–Witten moduli space; irreducible and reducible points** (unlabelled, p. 62). $\mathcal M_{SW}:=\{(\psi,A)\text{ solving }(188)\}/\mathcal G$. $(\psi,A)$ with $\psi\not\equiv0$ is irreducible; $(0,A)$ is reducible. $\mathcal M^{\mathrm{irr}}_{SW}:=\{\text{irreducible solutions}\}/\mathcal G$.

#### Theorems
- **T7.1.2 — Equivariance of the Seiberg–Witten map** (Lemma 190, p. 62). $SW((\psi,A)\cdot g)=\bar g\cdot SW(\psi,A)$.
  `Proof in source: omitted.` (Intended: $\slashed D^+_{A+2g^{-1}dg}(\bar g\psi)=\bar g\slashed D_A^+\psi+\tfrac12(2g^{-1}dg)\cdot\bar g\psi+(d\bar g)\cdot\psi=\bar g\slashed D_A^+\psi$ using (127) and $d\bar g=-\bar g\,g^{-1}dg$; $F_{A\cdot g}=F_A$ since $d(g^{-1}dg)=0$ for $U(1)$; $\mu(\bar g\psi)=\mu(\psi)$ since $|g|=1$.)
- **T7.1.3 — Stabilisers** (unlabelled, p. 62). $\operatorname{Stab}(\psi,A)\ne\{1\}\iff\psi\equiv0$; a stabilising $g$ is constant.
  `Proof in source: full (one line):` by (189) $g$ in the stabiliser satisfies $g^{-1}dg=0$, so $g$ is constant; then $\bar g\psi=\psi$ with $g\ne1$ forces $\psi=0$.

#### Remarks
- **R7.1.2 — $\mathcal G$ acts on the solution space; the quotient is the moduli space** (p. 62).

### 7.1.2 The deformation complex — `PDF pages: 62–63`

#### Definitions
- **D7.1.5 — Deformation complex of the Seiberg–Witten equations** (equation (191), p. 62). $0\to\Omega^0(M;\mathbb Ri)\xrightarrow{R_{(\psi,A)}}\Gamma(\slashed S^+)\oplus\Omega^1(M;\mathbb Ri)\xrightarrow{d_{(\psi,A)}SW}\Gamma(\slashed S^-)\oplus\Omega^2_+(M;\mathbb Ri)\to0$, the middle term being the tangent space of the configuration space ($\mathcal A(P_{\det})$ affine over $\Omega^1(M;\mathbb Ri)$). Infinitesimal gauge action: $R_{(\psi,A)}\xi=(-\xi\psi,2d\xi)$ for $\xi\in\Omega^0(M;\mathbb Ri)$. Footnote 5: strictly the constructions of §6.6 do not yet apply (smooth category); fixed by Sobolev completions below.
- **D7.1.6 — Atiyah complex** (in Proposition 194, p. 63). $0\to\Omega^0(X)\xrightarrow d\Omega^1(X)\xrightarrow{d^+}\Omega^2_+(X)\to0$ on an oriented Riemannian 4-manifold $X$.

#### Theorems
- **T7.1.4 — Differential of the Seiberg–Witten map** (Lemma 192, p. 63). $d_{(\psi,A)}SW(\dot\psi,\dot a)=\big(\slashed D_A^+\dot\psi+\tfrac12\dot a\cdot\psi,\ d^+\dot a-2\mu(\psi,\dot\psi)\big)$, where $\dot a\cdot\psi$ is Clifford multiplication, $d^+\dot a$ the self-dual projection of $d\dot a$, and $\mu(\cdot,\cdot)$ the polarisation of $\mu$.
  `Proof in source: omitted.` (Intended: from (127) and $F_{A+\dot a}=F_A+d\dot a$.)
- **T7.1.5 — The Atiyah complex is elliptic** (Proposition 194, p. 63). For any Riemannian oriented four-manifold $X$, the Atiyah complex is elliptic.
  `Proof in source: omitted ("left to the reader").` Two suggested routes: compute principal symbols in local coordinates, or note $d^++d^*$ is a twisted Dirac operator.
- **T7.1.6 — The Seiberg–Witten deformation complex is elliptic** (Proposition 193, p. 63). For any solution $(\psi,A)$ of the Seiberg–Witten equations, (191) is an elliptic complex.
  `Proof in source: full (short, modulo Prop. 194).` Modulo zero-order terms (immaterial for ellipticity), (191) is the direct sum of the Atiyah complex and $0\to0\to\Gamma(\slashed S^+)\xrightarrow{\slashed D^+}\Gamma(\slashed S^-)\to0$; both are elliptic ($\slashed D^+$ by Example 144).
  `Gaps:` that ellipticity of a complex is insensitive to zero-order terms is asserted; "$(191)$ is a complex" at a solution relies on Lemma 190.

#### Remarks
- **R7.1.3 — Computation of the infinitesimal gauge action** (p. 62): differentiate $(\bar g\psi,A+2g^{-1}dg)$ at $g=e^{\xi}$, $\xi\in\Omega^0(M;\mathbb Ri)$: $(-\xi\psi,2d\xi)$.

### 7.1.3 Sobolev completions — `PDF pages: 63–64`

#### Definitions
- **D7.1.7 — Sobolev completion of the space of connections** (unlabelled, p. 63). Fix $A_0\in\mathcal A(P_{\det})$ (identifies $\mathcal A(P_{\det})$ with $\Gamma(T^*M\otimes\mathbb Ri)$, non-canonically); $\mathcal A^{k,p}(P_{\det}):=A_0+W^{k,p}(T^*M\otimes\mathbb Ri)$, an affine Banach space, structure independent of $A_0$.
- **D7.1.8 — Sobolev gauge group $\mathcal G^{k,p}$** (unlabelled, p. 63). A map $M\to S^1$ is of class $W^{k,p}$ if its composition with $S^1\subset\mathbb R^2$ lies in $W^{k,p}(M;\mathbb R^2)$; $\mathcal G^{k,p}$ = all such maps, a Banach manifold (not a vector space); for $kp>4$ closed under pointwise multiplication by the Sobolev multiplication theorem, hence a Banach Lie group with $\operatorname{Lie}(\mathcal G^{k,p})=W^{k,p}(M;\mathbb Ri)$.
- **D7.1.9 — The Sobolev configuration space $\mathcal C^{5,2}$** (p. 64). $\mathcal C^{5,2}:=W^{5,2}(\slashed S^+)\times\mathcal A^{5,2}(P_{\det})$ with gauge group $\mathcal G^{6,2}$; "any $(k,p)$ with $k$ sufficiently large would work".

#### Theorems
- **T7.1.7 — Smooth Sobolev extension of $SW$ and of the gauge action** (Proposition 195, p. 64). For any $k$ and $p>1$ with $kp>4=\dim M$, the Seiberg–Witten map extends to a smooth map $SW\colon W^{k+1,p}(\slashed S^+)\times\mathcal A^{k+1,p}(P_{\det})\to W^{k,p}(\slashed S^-)\times W^{k,p}(\Lambda^2_+T^*M\otimes\mathbb Ri)$. The gauge action extends to a smooth action of $\mathcal G^{k+2,p}$, and $SW$ is equivariant.
  `Proof in source: full (short).` With smooth reference $A_0$ and $a\in W^{k+1,p}(T^*M\otimes\mathbb Ri)$: by (127) and Theorem 136(iv), $\slashed D^+_{A_0+a}\psi=\slashed D^+_{A_0}\psi+\tfrac12a\cdot\psi\in W^{k,p}(\slashed S^-)$ and $F^+_{A_0+a}-\mu(\psi)=F^+_{A_0}+d^+a-\mu(\psi)\in W^{k,p}$. The gauge action extends by the Sobolev multiplication theorem and (189) ($g^{-1}dg\in W^{k+1,p}$ needs $g\in W^{k+2,p}$), explaining $k+2$.
  `Gaps:` smoothness (not just well-definedness) of the polynomial maps in Sobolev spaces is asserted via Theorem 136(iv).

### 7.1.4 Compactness of the Seiberg–Witten moduli space — `PDF pages: 64–67`

#### Definitions
- **D7.1.10 — Sobolev Seiberg–Witten moduli space** (Corollary 205, p. 66). $\mathcal M:=\{(\psi,A)\in\mathcal C^{5,2}\mid SW(\psi,A)=0\}/\mathcal G^{6,2}$.
- **D7.1.11 — Smooth Seiberg–Witten moduli space** (Theorem 206, p. 67). $\mathcal M_\infty:=\{(\psi,A)\in\Gamma(\slashed S^+)\times\mathcal A(P_{\det})\mid SW(\psi,A)=0\}/C^\infty(M;U(1))$, with the $C^\infty$-topology.

#### Theorems
- **T7.1.8 — A priori $C^0$ bound on the spinor** (Lemma 196, p. 64). There is a constant $C>0$ such that for any solution $(\psi,A)\in\mathcal C^{5,2}=W^{5,2}(\slashed S^+)\times\mathcal A^{5,2}(P_{\det})$ of the Seiberg–Witten equations, $\|\psi\|_{C^0}\le C$. (The proof gives the explicit bound $|\psi|^2\le\max\{0,-\tfrac12\min_Ms_g\}$, i.e. $\|\psi\|_{C^0}^2\le\tfrac12\max_M(-s_g)^+$.)
  `Proof in source: full.` $\psi\in W^{5,2}\subset C^2$ (Sobolev embedding, $5-\tfrac42>2$). Let $x_0$ be a maximum of $|\psi|^2$. The pointwise identity $\Delta|\psi|^2=2\langle\nabla_A^*\nabla_A\psi,\psi\rangle-2|\nabla_A\psi|^2$ and $\Delta|\psi|^2\ge0$ at a maximum (non-negative Laplacian) give $\langle\nabla_A^*\nabla_A\psi,\psi\rangle\ge|\nabla_A\psi|^2$ at $x_0$. Pointwise $\langle\mu(\psi)\psi,\psi\rangle=\langle|\psi|^2\psi-\tfrac12|\psi|^2\psi,\psi\rangle=\tfrac12|\psi|^4$. The Weitzenböck formula (chiral version, T4.4.5) with $\slashed D_A^+\psi=0$ and $F_A^+=\mu(\psi)$ gives $0=\langle\nabla_A^*\nabla_A\psi,\psi\rangle+\tfrac14s_g|\psi|^2+\tfrac14|\psi|^4$. Hence at $x_0$: $\tfrac14s_g(x_0)|\psi|^2(x_0)+\tfrac12|\psi|^4(x_0)\le-|\nabla_A\psi|^2(x_0)\le0$ (the source's chain of constants: it uses $\tfrac12|\psi|^4$ from $\langle\tfrac12F_A^+\cdot\psi,\psi\rangle=\tfrac12\cdot\tfrac12|\psi|^4=\tfrac14|\psi|^4$ in the identity and then $\tfrac12|\psi|^4$ in the inequality — an inconsistency of a factor 2 in the printed constants; the conclusion $|\psi|^2(x_0)\le-\tfrac12s_g(x_0)$ follows from the printed inequality). If $|\psi(x_0)|=0$ nothing to prove; else divide by $|\psi|^2(x_0)$: $|\psi|^2(x_0)\le-\tfrac12s_g(x_0)$.
  `Gaps:` the pointwise Laplacian identity $\Delta|\psi|^2=2\langle\nabla^*\nabla\psi,\psi\rangle-2|\nabla\psi|^2$ (Kato/Bochner-type identity) is stated without proof; the factor-2 inconsistency noted above; the identity $\langle\mu(\psi)\psi,\psi\rangle=\tfrac12|\psi|^4$ needs the convention that $\mu(\psi)$ acts on $\slashed S^+$ via (187) with Clifford multiplication by $F^+_A=\mu(\psi)$ equal to the endomorphism $\mu(\psi)$ (normalisation of (187) suppressed).
- **T7.1.9 — Sign matters** (Remark 197, p. 65). The proof of Lemma 196 fails for the equations $\slashed D_A^+\psi=0$, $F_A^+=-\mu(\psi)$ (the $|\psi|^4$ term would come with the wrong sign).
- **T7.1.10 — $L^p$ bounds on the spinor** (Corollary 198, p. 65). For any $p>1$ there is a non-negative constant $\kappa_p$, depending only on the Riemannian metric $g$, such that for any solution $(\psi,A)\in\mathcal C^{5,2}$, $\|\psi\|_{L^p}\le\kappa_p$.
  `Proof in source: omitted (immediate from Lemma 196 and finite volume).`
- **T7.1.11 — $L^2$ bounds on the curvature** (Corollary 199, p. 65). For any solution $(\psi,A)$: $\|F_A^+\|_{L^2}\le C$ and $\|F_A^-\|^2_{L^2}\le C-4\pi^2c_1(L_{\det})^2$ (200) (the source prints $\|F_A^-\|_{L^2}\le C-4\pi^2c_1(L_{\det})^2$; from the proof the bound is on the square), constants depending only on the metric.
  `Proof in source: full.` First from Corollary 198 (since $F_A^+=\mu(\psi)$ is quadratic in $\psi$, $\|F^+_A\|_{L^2}\le C\|\psi\|^2_{L^4}$). Second: $c_1(L_{\det})$ is represented by $\tfrac{i}{2\pi}F_A$, so $c_1(L_{\det})^2=\tfrac{i^2}{(2\pi)^2}\int_MF_A\wedge F_A=-\tfrac1{4\pi^2}\int_M(F_A^+\wedge F_A^++F_A^-\wedge F_A^-)=\tfrac1{4\pi^2}(\|F_A^+\|^2_{L^2}-\|F_A^-\|^2_{L^2})$ (using $\omega\wedge\omega=\pm|\omega|^2\mathrm{vol}$ for $\omega\in\Lambda^2_\pm$ and $F^+\wedge F^-=0$; the sign is such that $\|F^-\|^2=\|F^+\|^2-4\pi^2c_1^2$), whence the bound.
  `Gaps:` the identities $\int F^\pm\wedge F^\pm=\pm\|F^\pm\|^2$ and $\int F^+\wedge F^-=0$ are used silently; the printed formula has $-\tfrac1{4\pi^2}\int(F^+\wedge F^++F^-\wedge F^-)=\tfrac1{4\pi^2}(\|F^+\|^2-\|F^-\|^2)$ which requires $\int F^+\wedge F^+=-\|F^+\|^2$, opposite to the usual convention $\int F^+\wedge F^+=+\|F^+\|^2$ — the writers must fix a consistent sign convention.
- **T7.1.12 — Remark 201** (p. 65). The right side of the second inequality of (200) is a constant independent of the solution; the explicit form is used later (Theorem 225).
- **T7.1.13 — Coulomb gauge fixing with estimates** (Lemma 202, p. 66, [Mor96, Lemma 5.3.1]). Let $L$ be any Hermitian line bundle over $M$ and fix a smooth reference connection $A_0$. For any $k\ge0$ there are positive constants $C_1,C_2$ such that: for any $W^{k,2}$-connection $A$ on $L$ there is a gauge transformation $g\in\mathcal G^{k+1,2}$ with $A\cdot g=A_0+\alpha$, $\alpha\in W^{k,2}(T^*M\otimes\mathbb Ri)$, satisfying $d^*\alpha=0$ and $\|\alpha\|_{W^{k,2}}\le C_1\|F_A^+\|_{W^{k-1,2}}+C_2$. Moreover the harmonic component $\alpha_h$ of $\alpha$ can be assumed bounded in $L^2$ by a constant independent of $k$.
  `Proof in source: omitted/cited (to [Mor96, Lemma 5.3.1]); "follows essentially from the elliptic estimate".`
- **T7.1.14 — Uniform $W^{k,2}$ bounds after gauge fixing** (Proposition 203, p. 66). For each $k\ge0$ there is $C_k>0$ such that for any solution $(\psi,A)$ of the Seiberg–Witten equations there is $g\in\mathcal G^{k+1,2}$ with $\|(\psi,\alpha)\|_{W^{k,2}}\le C_k$ (204), where $A\cdot g=A_0+\alpha$.
  `Proof in source: full (induction on $k$; $k=3$ left as exercise).` $k=0$: $\|(\psi,F_A^+)\|_{L^2}$ bounded (Cor. 198, 199); Lemma 202 bounds $\alpha$. $k=1$: $0=\slashed D_A^+\psi=\slashed D_{A_0}^+\psi+\tfrac12\alpha\cdot\psi$ with $\alpha\cdot\psi$ bounded in $L^2$ by Lemma 196 ($\psi$ bounded in $C^0$, $\alpha$ in $L^2$); the elliptic estimate for $\slashed D^+_{A_0}$ bounds $\psi$ in $W^{1,2}$; ($\alpha$ in $W^{1,2}$ from Lemma 202 with $F^+_A=\mu(\psi)\in L^2$). $k=2$: pointwise $|\nabla^{LC}F_A^+|=|\nabla^{LC}\mu(\psi)|\le C|\nabla_{A_0}\psi||\psi|\le C|\nabla_{A_0}\psi|$ ($\mu$ quadratic; Lemma 196), giving a $W^{1,2}$ bound on $F_A^+$, hence a $W^{2,2}$ bound on $\alpha$ (Lemma 202); Sobolev multiplication gives $\alpha\cdot\psi$ bounded in $W^{1,2}$, hence $\psi$ bounded in $W^{2,2}$ by the elliptic estimate. $k=3$: "the reader will have no difficulties". Induction step $k\ge3\Rightarrow k+1$: $W^{k,2}$ is an algebra for $k\ge3$ (in dimension 4, $kp=2k>4$), so $F_A^+=\mu(\psi)$ is bounded in $W^{k,2}$; Lemma 202 bounds $\alpha$ in $W^{k+1,2}$; similarly $\alpha\cdot\psi$ bounded in $W^{k,2}$, so the elliptic estimate bounds $\psi$ in $W^{k+1,2}$.
  `Gaps:` the $k=3$ step; the $L^p$-term $\|\psi\|_{L^p}$ in the elliptic estimate is handled by Corollary 198 (not said); the estimate $|\nabla^{LC}\mu(\psi)|\le C|\nabla_{A_0}\psi||\psi|$ mixes the Levi-Civita and the spin$^c$ connection (the correct statement uses $\nabla_A$; the difference $\alpha\cdot\psi$ is controlled) — not discussed; the gauge transformation $g$ produced by Lemma 202 at level $k$ must be checked to lie in the right Sobolev class at every stage.
- **T7.1.15 — Compactness of the Sobolev moduli space** (Corollary 205, p. 66). The Seiberg–Witten moduli space $\mathcal M=\{(\psi,A)\in\mathcal C^{5,2}\mid SW(\psi,A)=0\}/\mathcal G^{6,2}$ is compact.
  `Proof in source: full (short).` Any sequence of solutions $(\psi_n,A_n)$ is gauge equivalent to $(\psi_n,A_0+\alpha_n)$ with $(\psi_n,\alpha_n)$ bounded in $W^{6,2}$ (Prop. 203); by Sobolev compactness a subsequence converges in $\mathcal C^{5,2}$, and the limit solves the equations (continuity of $SW$).
- **T7.1.16 — Regularity: every solution is gauge equivalent to a smooth one; $\mathcal M\cong\mathcal M_\infty$; $C^\infty$ compactness** (Theorem 206, p. 67). For each solution $(\psi,A)\in\mathcal C^{5,2}$ there is $g\in\mathcal G^{6,2}$ such that $(\psi,A)\cdot g$ is smooth. Furthermore $\mathcal M$ is homeomorphic to $\mathcal M_\infty$, and this space is compact in the $C^\infty$-topology.
  `Proof in source: full.` By Prop. 203, $F_A=F_{A\cdot g}=F_{A_0}+d\alpha\in W^{k-1,2}$ for all $k$, so $F_A$ is smooth. With $A\cdot g=A_0+\alpha$, $d^*\alpha=0$: $(d+d^*)\alpha=d\alpha=F_A-F_{A_0}\in C^\infty$, so $\alpha$ is smooth by elliptic regularity ($d+d^*$ elliptic), hence $A$ (i.e. $A\cdot g$) is smooth; then $\psi\in\ker\slashed D_A^+$ (smooth elliptic operator) is smooth. Compactness in $C^\infty$: for a sequence of smooth solutions, Cor. 205 gives a subsequence converging in $W^{5,2}$ after $\mathcal G^{6,2}$ gauge transformations; since the sequence is bounded in $W^{7,2}$ (after $\mathcal G^{7,2}$ gauge transformations, Prop. 203 with $k=7$), a subsequence converges in $W^{6,2}$; repeat for each $k\ge6$ and take a diagonal subsequence.
  `Gaps:` the gauge transformations at different levels $k$ must be compatible (one fixed $g$ works for all $k$ since Coulomb gauge is unique up to constants — not said); the homeomorphism $\mathcal M\cong\mathcal M_\infty$ is asserted from the two directions of the argument; a smooth solution's Coulomb gauge transformation $g$ is itself smooth (needed to see $\mathcal G^{6,2}$-orbits of smooth solutions meet $C^\infty(M;U(1))$-orbits correctly).

#### Remarks / load-bearing paragraphs
- **R7.1.4 — Strategy of the compactness proof** (p. 64). Given a sequence $(\psi_n,A_n)$, find a convergent subsequence; this follows from compactness of Sobolev embeddings if $\|(\psi_n,A_n)\|_{W^{6,2}}$ is bounded; we may change representatives by gauge transformations since convergence is sought in $\mathcal C/\mathcal G$; in fact bounds in $W^{k,2}$ for all $k$ are obtained.
- **R7.1.5 — Weitzenböck bootstrap in the $C^0$ bound** (pp. 64–65): the maximum principle step.
- **R7.1.6 — The role of the sign of $\mu$** (Remark 197, p. 65).
- **R7.1.7 — Chern–Weil input** (p. 65): $c_1(L_{\det})$ represented by $\tfrac{i}{2\pi}F_A$ and the self-dual/anti-self-dual splitting of $\int F\wedge F$.

### 7.1.5 Slices — `PDF page: 67`

#### Definitions
- **D7.1.12 — Irreducible configuration space and $R^*$** (unlabelled, p. 67). $\mathcal C^{5,2}_{\mathrm{irr}}:=\{(\psi,A)\in\mathcal C^{5,2}\mid\psi\not\equiv0\}$, on which $\mathcal G^{6,2}$ acts freely. The formal adjoint of the infinitesimal action is $R^*_{(\psi,A)}(\dot\psi,\dot a)=2d^*\dot a+i\operatorname{Re}\langle\psi,i\dot\psi\rangle$ (target $\Omega^0(M;\mathbb Ri)$), $\langle\cdot,\cdot\rangle$ the Hermitian scalar product on spinors.

#### Theorems
- **T7.1.17 — Coulomb slice** (Proposition 207, p. 67). For any irreducible configuration $(\psi,A)$ the subspace $(\psi,A)+\ker R^*_{(\psi,A)}$ is a slice for the $\mathcal G^{6,2}$-action on $\mathcal C^{5,2}_{\mathrm{irr}}$, where $\ker R^*_{(\psi,A)}$ is the kernel of $R^*_{(\psi,A)}\colon W^{5,2}\to W^{4,2}$.
  `Proof in source: omitted.`

#### Remarks
- **R7.1.8 — Why $\ker R^*$** (p. 67): the tangent space of a slice must be transverse to $\operatorname{Im}R_{(\psi,A)}$; the natural choice is the $L^2$-orthogonal complement $\ker R^*$.

### 7.1.6 A perturbation — `PDF pages: 68–69`

#### Definitions
- **D7.1.13 — Perturbed Seiberg–Witten map and equations** (Proposition 208, p. 68). $SW\colon\mathcal C^{5,2}_{\mathrm{irr}}\times W^{4,2}(\Lambda^2_+T^*M\otimes\mathbb Ri)\to W^{4,2}(\slashed S^-)\times W^{4,2}(\Lambda^2_+T^*M\otimes\mathbb Ri)$, $SW(\psi,A,\eta)=(\slashed D_A^+\psi,F_A^+-\mu(\psi)-\eta)$; $SW_\eta:=SW(\cdot,\cdot,\eta)$; perturbed equations $\slashed D_A^+\psi=0$, $F_A^+=\mu(\psi)+\eta$.
- **D7.1.14 — Perturbed irreducible moduli space** (Corollary 212, p. 69). $\mathcal M^{\mathrm{irr}}_\eta:=\{(\psi,A)\in\mathcal C^{5,2}\mid SW(\psi,A,\eta)=0,\ \psi\not\equiv0\}/\mathcal G^{6,2}$.
- **D7.1.15 — The operators $D_{(\psi,A)}$ and $D_0$** (equations (214), (215), p. 69). $D_{(\psi,A)}:=(d_{(\psi,A)}SW_\eta,R^*_{(\psi,A)})\colon T_{(\psi,A)}\mathcal C^{5,2}\to W^{4,2}(\slashed S^-\oplus\Lambda^2_+T^*M\otimes\mathbb Ri\oplus\mathbb Ri)$; $D_{(\psi,A)}=D_0+B$ with $D_0=\slashed D_A^+\oplus(d^++d^*)$ (block-diagonal) and $B$ of order zero.

#### Theorems
- **T7.1.18 — The origin is a regular value of the perturbed map** (Proposition 208, p. 68). $0$ is a regular value of $SW\colon\mathcal C^{5,2}_{\mathrm{irr}}\times W^{4,2}(\Lambda^2_+T^*M\otimes\mathbb Ri)\to W^{4,2}(\slashed S^-)\times W^{4,2}(\Lambda^2_+T^*M\otimes\mathbb Ri)$.
  `Proof in source: full.` $\mathrm{pr}_2\partial SW/\partial\eta=-\mathrm{id}$ is surjective onto the second factor, so it suffices that $T:=\mathrm{pr}_1d_{(\psi,A)}SW_\eta\colon T_{(\psi,A)}\mathcal C^{5,2}\to W^{4,2}(\slashed S^-)$, $(\dot\psi,\dot A)\mapsto\slashed D_A\dot\psi+\tfrac12\dot A\cdot\psi$, is surjective at every solution $(\psi,A)$ of the perturbed equations. Suppose not: there is $0\ne\phi\in(\operatorname{Im}T)^\perp:=\{\phi\in W^{4,2}\mid\langle T(\dot\psi,\dot A),\phi\rangle_{L^2}=0\ \forall(\dot\psi,\dot A)\}$. Taking $\dot A=0$: $0=\langle\slashed D_A^+\dot\psi,\phi\rangle=\langle\dot\psi,\slashed D_A^-\phi\rangle$ for all $\dot\psi$, so $\slashed D_A^-\phi=0$ (209). Taking $\dot\psi=0$: $\langle\dot A\cdot\psi,\phi\rangle_{L^2}=0$ for all $\dot A\in W^{5,2}(T^*M\otimes\mathbb Ri)$ (210). Since $W^{5,2}\subset C^0$ in dimension 4, $\psi$ is continuous and not identically zero, so it is nonvanishing on a neighbourhood $U$ of some $m$. Clifford multiplication by a fixed nonzero $\psi_0\in\slashed S^+$, $\mathbb R^4\to\slashed S^-$, $v\mapsto v\cdot\psi_0$, is surjective (real dimensions $4\to4$, injective since $v\cdot v\cdot\psi_0=-|v|^2\psi_0$). Hence if $\phi$ did not vanish on $U$ there would be $\dot A$ supported in $U$ with $\langle\dot A\cdot\psi,\phi\rangle_{L^2}>0$, contradicting (210); so $\phi$ vanishes on an open set. By Aronszajn's unique continuation theorem [Aro57], (209) forces $\phi\equiv0$. Contradiction; $T$ is surjective.
  `Gaps:` the closed-range/Hahn–Banach step ("if $T$ not surjective then $(\operatorname{Im}T)^\perp\ne0$") needs that $\operatorname{Im}T$ is closed (true since $T$ is Fredholm-like: $\slashed D_A^+$ is Fredholm and $\dot A\cdot\psi$ is compact-ish) — not discussed; the surjectivity of $v\mapsto v\cdot\psi_0$ is over $\mathbb R^4$ but $\dot A$ is $\mathbb Ri$-valued: $\dot A\cdot\psi$ ranges over $i(\mathbb R^4\cdot\psi)$, which is still all of $\slashed S^-$ (real 4-dimensional, and $\mathbb R^4\cdot\psi_0$ is a real 4-dimensional subspace of the real 4-dimensional $\slashed S^-$; multiplying by $i$ preserves this) — the source glosses over the $i$; regularity of $\phi$ needed for Aronszajn (it is in $W^{4,2}$, fine).
- **T7.1.19 — Ellipticity and Fredholmness of the perturbed deformation operator** (unlabelled, p. 68). At a solution of the perturbed equations the deformation complex is again (191) ($d SW_\eta=dSW_0$), hence elliptic; therefore $(d_{(\psi,A)}SW_\eta,R^*_{(\psi,A)})\colon W^{5,2}(\slashed S^+\oplus T^*X\otimes\mathbb Ri)\to W^{4,2}(\slashed S^-\oplus\Lambda^2_+T^*X\otimes\mathbb Ri)$ (211) is elliptic by Exercise 159 and Fredholm by Theorem 153. (The printed target of (211) omits the $\Omega^0(\mathbb Ri)$ summand which is present in (214).)
  `Proof in source: full (one paragraph).`
- **T7.1.20 — Generic smoothness of the irreducible moduli space and the dimension formula** (Corollary 212, p. 69). There is a subset $\mathcal H\subset W^{4,2}(\Lambda^2_+T^*X\otimes\mathbb Ri)$ of second category such that for any $\eta\in\mathcal H$, $\mathcal M^{\mathrm{irr}}_\eta$ is a smooth manifold of dimension
$$d=\frac14\big(c_1(L_{\det})^2-2\chi(M)-3\operatorname{sign}(M)\big),\qquad(213)$$
where $\chi(M)$ is the Euler characteristic and $\operatorname{sign}(M):=b_2^+-b_2^-$ the signature.
  `Proof in source: full for the dimension formula (existence of $\mathcal H$ from Theorem 183 + Lemma 169/Sard–Smale, stated as "by appealing to Theorem 183").` Fact used: the index is locally constant on Fredholm operators, so a one-parameter family $T_t$ of Fredholm operators has $\operatorname{index}T_0=\operatorname{index}T_1$. Write $D_{(\psi,A)}=D_0+B$ (215) with $B$ of order zero; $D_{(\psi,A)}$ is homotopic through Fredholm operators to $D_0$ (via $D_0+tB$; a zero-order perturbation of an elliptic operator is elliptic, hence Fredholm). $D_0$ decouples: $\operatorname{index}D_0=\operatorname{index}\slashed D_A^+\ (\text{real})+\operatorname{index}(d^++d^*)$. $\operatorname{index}(d^++d^*)=b_1-b_0-b_2^+$ (kernel $H^1$, cokernel $H^0\oplus H^2_+$), which the source writes as $=\tfrac12(\chi+\operatorname{sign})$. By the Atiyah–Singer index theorem, $\operatorname{index}_{\mathbb C}\slashed D_A^+=\tfrac18(c_1(L_{\det})^2-\operatorname{sign})$. Combining (real index $=2\cdot$ complex index) yields (213).
  `Gaps:` **sign slip**: $b_1-b_0-b_2^+=-\tfrac12(\chi+\operatorname{sign})$ for a closed oriented 4-manifold ($\chi=2b_0-2b_1+b_2^++b_2^-$, $\operatorname{sign}=b_2^+-b_2^-$, so $\tfrac12(\chi+\operatorname{sign})=b_0-b_1+b_2^+$); the correct combination is $d=2\cdot\tfrac18(c_1^2-\operatorname{sign})-(b_0-b_1+b_2^+)=\tfrac14(c_1^2-\operatorname{sign})-\tfrac12(\chi+\operatorname{sign})=\tfrac14(c_1^2-2\chi-3\operatorname{sign})$, which is (213) — so the final formula is right and only the intermediate sign is misprinted. The index of the $\mathbb Ri$-valued $d^++d^*$ is computed with real cohomology (twisting by the trivial real line $\mathbb Ri$). The index of $D_{(\psi,A)}$ equals $\dim\ker D_{(\psi,A)}=\dim\mathcal M^{\mathrm{irr}}_\eta$ only because $\operatorname{coker}D_{(\psi,A)}=0$ at a regular irreducible point (surjectivity of $R^*$ on its part follows from irreducibility) — asserted via Theorem 183. Atiyah–Singer is imported.
- **T7.1.21 — Compactness for the perturbed equations** (Remark 216, p. 69). The compactness analysis of §7.1.4 goes through for the perturbed equations with cosmetic changes (the $C^0$ bound becomes $|\psi|^2\le-\tfrac12s_g+C|\eta|$-type; not written).
  `Proof in source: omitted ("the reader should have no difficulties").`

#### Remarks
- **R7.1.9 — Why perturb** (p. 68): no reason for $0$ to be a regular value of $SW$; construct a family of perturbations by hand as in §6.3.
- **R7.1.10 — Choice of perturbation** (p. 68): $\eta$ enters only the curvature equation, making $\partial_\eta$ surjective onto the second factor; the whole work is surjectivity of the first component.
- **R7.1.11 — Local constancy of the index** (p. 69) used to compute $\dim\mathcal M$ by deforming to $D_0$.

### 7.1.7 Reducible solutions — `PDF page: 69`

#### Definitions
- **D7.1.16 — The wall $Q$** (Proposition 217, p. 69). For a reference connection $A_0$ on $L_{\det}$, $Q:=F^+_{A_0}+\operatorname{Im}d^+\subset W^{4,2}(\Lambda^2_+T^*M\otimes\mathbb Ri)$, an affine subspace of codimension $b_2^+$ (since $\Omega^2_+/\operatorname{Im}d^+\cong\mathcal H^2_+$, harmonic self-dual forms).

#### Theorems
- **T7.1.22 — Reducibles are avoided off a codimension-$b_2^+$ wall** (Proposition 217, p. 69). Assume $b_2^+\ge1$. There is an affine subspace $Q\subset W^{4,2}(\Lambda^2_+T^*M\otimes\mathbb Ri)$ of codimension $b_2^+$ such that if $\eta\notin Q$ there are no reducible solutions of the (perturbed) Seiberg–Witten equations.
  `Proof in source: full (two lines).` Reducible solutions $(0,A)$ satisfy $F_A^+=\eta$; writing $A=A_0+a$, $F^+_A=F^+_{A_0}+d^+a\in Q$; so $\eta\notin Q$ excludes them.
  `Gaps:` codimension of $\operatorname{Im}d^+$ in $W^{4,2}(\Lambda^2_+)$ equals $b_2^+$ by Hodge theory for the Atiyah complex (not said); closedness of $\operatorname{Im}d^+$.
- **T7.1.23 — Generic perturbations have no reducibles** (Corollary 218, p. 69). Assume $b_2^+\ge1$. Then for generic $\eta$ the perturbed moduli space $\mathcal M_\eta$ contains no reducible solutions.
  `Proof in source: omitted (complement of a proper affine subspace is open dense; intersect with $\mathcal H$).`

### 7.1.8 Orientability of the Seiberg–Witten moduli space — `PDF page: 70`

#### Theorems
- **T7.1.24 — Homotopic families have isomorphic determinant bundles** (Lemma 219, p. 70). Let $P$ be a topological space. If $\{T_{p,0}\}$ and $\{T_{p,1}\}$ are two homotopic families of linear Fredholm maps, then $\det T_0\cong\det T_1$; precisely, $\det T_1$ is trivial iff $\det T_0$ is, and a trivialisation of $\det T_0$ induces one of $\det T_1$, well defined up to multiplication by an everywhere positive function.
  `Proof in source: full (short).` The homotopy $\{T_{p,t}\}$ gives $\det T$ over $P\times[0,1]$ restricting to $\det T_0$, $\det T_1$ on the boundary components; a line bundle over $P\times[0,1]$ restricts isomorphically to both ends.
- **T7.1.25 — Explicit isomorphism via parallel transport** (Remark 220, p. 70). An isomorphism $\det T_0\cong\det T_1$ can be constructed by choosing a connection on $\det T$ over $P\times[0,1]$ and parallel transporting along $t\mapsto(p,t)$.
- **T7.1.26 — Orientability of the Seiberg–Witten moduli space** (unlabelled, p. 70). $\det D_0\cong\det\slashed D_A^+\otimes\det(d^++d^*)$. $\slashed D_A^+$ is complex linear, so $\ker\slashed D_A^+$ and $\operatorname{coker}\slashed D_A^+\cong\ker\slashed D_A^-$ are complex vector spaces, hence oriented, so the real line bundle $\det\slashed D_A^+$ is trivial(ised). $\ker(d^++d^*)=H^1_{dR}(M;\mathbb Ri)$ and $\operatorname{coker}(d^++d^*)=H^0(M;\mathbb Ri)\oplus H^2_+(M;\mathbb Ri)$ are constant, so orientations of these cohomology groups trivialise $\det(d^++d^*)$. Hence $\det D_0$, and by Lemma 219 $\det D_{(\psi,A)}$, are trivialised: the Seiberg–Witten moduli space is orientable, and a choice of orientations of $H^0(M;\mathbb R)$, $H^1(M;\mathbb Ri)$, $H^2_+(M;\mathbb Ri)$ orients it.
  `Proof in source: full (as above).`
  `Gaps:` that the complex orientation of $\ker/\operatorname{coker}\slashed D^+_A$ varies continuously over the family (i.e. defines a trivialisation of the determinant bundle, not just pointwise orientations) is asserted; that the trivialisation is $\mathcal G$-invariant (needed for Theorem 184) is not discussed; the family parameter space is the configuration space $\mathcal C^{5,2}_{\mathrm{irr}}$ (or $\mathcal B^{\mathrm{irr}}$).
- **T7.1.27 — Non-canonicity of the orientation** (Remark 221, p. 70). (1) Two common conventions for orienting a complex vector space $V$ with complex basis $(v_1,\dots,v_k)$: $(v_1,\dots,v_k,iv_1,\dots,iv_k)$ or $(v_1,iv_1,\dots,v_k,iv_k)$; they give opposite orientations when $k=\dim_{\mathbb C}V$ is even (the permutation has sign $(-1)^{k(k-1)/2}$). (2) Orientations of $H^0(M;\mathbb R)$, $H^1(M;\mathbb Ri)$, $H^2_+(M;\mathbb Ri)$ are a choice; these spaces depend only on the topology of $M$ (an orientation of $H^2_+$ depends on a choice of maximal positive subspace of $H^2$, all such being homotopic).

### Examples (§7.1): none numbered.

### Exercises (§7.1)
- **X7.1.1** (p. 66, "I leave this as an exercise"): prove (204) for $k=3$.
- **X7.1.2** (Proposition 194, p. 63, "I leave the details to the reader"): prove the Atiyah complex is elliptic.
- **X7.1.3** (Remark 216, p. 69): redo the compactness analysis for the perturbed equations.

### External results imported without proof (§7.1)
- **I7.1.1 — Linear algebra of $Spin^c(4)$ representations** ((185)–(187), kernel of $\Lambda^2\to\operatorname{End}\slashed S^\pm$) (p. 61).
- **I7.1.2 — Sobolev embedding $W^{5,2}\subset C^2$ and $W^{5,2}\subset C^0$ in dimension 4** (pp. 64, 68).
- **I7.1.3 — Bochner identity $\Delta|\psi|^2=2\langle\nabla^*\nabla\psi,\psi\rangle-2|\nabla\psi|^2$** (p. 64).
- **I7.1.4 — Chern–Weil: $c_1(L_{\det})=[\tfrac{i}{2\pi}F_A]$ and $\int F\wedge F=\|F^+\|^2-\|F^-\|^2$ (up to the sign convention)** (p. 65).
- **I7.1.5 — Coulomb gauge lemma with estimates** [Mor96, Lemma 5.3.1] (Lemma 202, p. 66).
- **I7.1.6 — Elliptic estimate for $\slashed D^+_{A_0}$ and for $d+d^*$; elliptic regularity** (pp. 66–67).
- **I7.1.7 — Sobolev multiplication / $W^{k,2}$ is an algebra for $k\ge3$ in dimension 4** (p. 66).
- **I7.1.8 — Slice theorem** (Proposition 207) (p. 67).
- **I7.1.9 — Aronszajn's unique continuation theorem** [Aro57]: a solution of a second-order elliptic equation (here $\slashed D_A^-\phi=0$, so $(\slashed D^-_A)^*\slashed D^-_A\phi=0$ by Weitzenböck a Laplace-type equation) vanishing on an open set vanishes identically (p. 68).
- **I7.1.10 — Local constancy of the Fredholm index** (p. 69; cf. Exercise 152).
- **I7.1.11 — Atiyah–Singer index theorem for the spin$^c$ Dirac operator:** $\operatorname{index}_{\mathbb C}\slashed D_A^+=\tfrac18(c_1(L_{\det})^2-\operatorname{sign}(M))$ (p. 69).
- **I7.1.12 — Index of $d^++d^*$ via Hodge theory:** $\ker=H^1$, $\operatorname{coker}=H^0\oplus H^2_+$ (pp. 69–70).
- **I7.1.13 — $\operatorname{Im}d^+$ has codimension $b_2^+$ in $\Omega^2_+$** (p. 69).
- **I7.1.14 — Theorem 183 / Lemma 169 / Sard–Smale** applied to produce $\mathcal H$ (p. 68–69).

---

## 7.2 The Seiberg–Witten invariant

`PDF pages: 71–72`

### Standing conventions and notation
- $b_2^+(M)\ge2$ for the invariant (ensures a generic bordism between $\mathcal M_{\eta_0}$ and $\mathcal M_{\eta_1}$ avoids reducibles); $b_2^+\ge1$ suffices for a single generic $\mathcal M_\eta$ to avoid reducibles (p. 71).
- $\mathcal S(M)$ set of spin$^c$ structures; $\sigma\in\mathcal S(M)$; $\mathcal M_\eta$ depends on $\sigma$ (suppressed, Remark 223) (p. 71).
- Base point $m_0\in M$; based gauge group $\mathcal G_0:=\{g\in W^{6,2}(M;U(1))\mid g(m_0)=1\}$; exact sequence $\{1\}\to\mathcal G_0\to\mathcal G\xrightarrow{\mathrm{ev}_{m_0}}U(1)\to\{1\}$ (p. 71).
- Framed moduli space $\hat{\mathcal M}_\eta:=\{(\psi,A)\in\mathcal C^{5,2}\mid SW_\eta(\psi,A)=0\}/\mathcal G_0$, a principal $U(1)=\mathcal G/\mathcal G_0$-bundle over $\mathcal M_\eta$; $\mu:=c_1(\hat{\mathcal M}_\eta\to\mathcal M_\eta)\in H^2(\mathcal M_\eta;\mathbb Z)$ — the restriction of the universal bundle $\mathcal C^{\mathrm{irr}}/\mathcal G_0\to\mathcal C^{\mathrm{irr}}/\mathcal G$ (p. 71). (Note the clash of notation: $\mu$ is also the quadratic map of §7.1.)
- $\operatorname{PD}$ = Poincaré dual; $|c_1(L_{\det})|^2:=|c_1(L_{\det})\cup\operatorname{PD}(c_1(L_{\det}))|$ (as printed; the intended quantity is a norm-squared of the harmonic representative, $\tfrac1{4\pi^2}\|F_A\|^2_{L^2}$ for $A$ with harmonic curvature) (p. 71).
- Footnote 6: the a priori estimate should be the one for the perturbed equations (Remark 216); the argument is unchanged (p. 71).

### Definitions
- **D7.2.1 — Based gauge group and framed moduli space** (unlabelled, p. 71). $\mathcal G_0:=\{g\in W^{6,2}(M;U(1))\mid g(m_0)=1\}$; $\hat{\mathcal M}_\eta:=\{(\psi,A)\in\mathcal C^{5,2}\mid SW_\eta(\psi,A)=0\}/\mathcal G_0$, with free $U(1)=\mathcal G/\mathcal G_0$-action and $\hat{\mathcal M}_\eta/U(1)=\mathcal M_\eta$; so $\hat{\mathcal M}_\eta\to\mathcal M_\eta$ is a principal $U(1)$-bundle with first Chern class $\mu$.
- **D7.2.2 — Seiberg–Witten invariant** (Definition 224, p. 71). The Seiberg–Witten invariant of $M$ is the function $\mathrm{sw}\colon\mathcal S(M)\to\mathbb Z$,
$$\mathrm{sw}(\sigma):=\begin{cases}\langle[\mathcal M_\eta],\mu^{d/2}\rangle&\text{if }d\text{ is even},\\0&\text{if }d\text{ is odd},\end{cases}$$
where $d=d(\sigma)$ is given by (213), $\eta$ is generic, and $[\mathcal M_\eta]$ is the fundamental class of the compact oriented $d$-manifold $\mathcal M_\eta$ (for $d=0$ this is the signed count of points).

### Theorems
- **T7.2.1 — Main theorem: structure of the perturbed moduli space** (Theorem 222, p. 71). Assume $b_2^+(M)\ge2$. For any spin$^c$ structure $\sigma\in\mathcal S(M)$ and any generic $\eta$, the perturbed Seiberg–Witten moduli space $\mathcal M_\eta$ is a smooth compact oriented manifold of dimension $d$ given by (213). Moreover, if $\eta_0,\eta_1$ are two generic perturbations, then $\mathcal M_{\eta_0}$ and $\mathcal M_{\eta_1}$ are oriented-bordant.
  `Proof in source: omitted ("combining results obtained in the preceding sections").` Ingredients: Cor. 212 (smooth, dimension $d$), Cor. 218 with $b_2^+\ge1$ (no reducibles, so $\mathcal M_\eta=\mathcal M^{\mathrm{irr}}_\eta$), Cor. 205/Thm 206 + Remark 216 (compact), §7.1.8 (oriented), Theorem 184 (bordism). The only explained point: $b_2^+\ge2$ ensures a generic path of perturbations $\eta_t$ misses the codimension-$b_2^+$ wall $Q$, so the bordism $\bigcup_t\mathcal M_{\eta_t}$ contains no reducibles and is smooth.
  `Gaps:` genericity of paths avoiding $Q$ (a 1-parameter family misses a codimension-$\ge2$ affine subspace generically) is the reason for $b_2^+\ge2$ but is only stated; the bordism's compactness (parametrised compactness) and orientation are asserted via Theorem 184.
- **T7.2.2 — Finiteness: $\mathrm{sw}$ vanishes for all but finitely many spin$^c$ structures** (Theorem 225, p. 71). The Seiberg–Witten invariant vanishes for all but finitely many spin$^c$ structures.
  `Proof in source: full (sketch-level).` If $\mathrm{sw}(\sigma)\ne0$ then $\mathcal M_\eta\ne\varnothing$ is a smooth manifold of dimension $d\ge0$, so $c_1(L_{\det})^2\ge2\chi(M)+3\operatorname{sign}(M)$ by (213). By (200), $\|F_A^-\|^2_{L^2}\le C$ with $C$ depending only on the metric and the topology of $M$ (footnote 6: strictly the perturbed-equation estimate), hence $\|F_A\|^2_{L^2}$ is bounded by such a constant. Then $|c_1(L_{\det})|^2=|c_1(L_{\det})\cup\operatorname{PD}(c_1(L_{\det}))|=\tfrac1{4\pi^2}\|F_A\|^2_{L^2}\le C$. Since $c_1(L_{\det})$ ranges over a lattice ($H^2(M;\mathbb Z)$ mod torsion) and $\mathcal S(M)\cong H^2(M;\mathbb Z)$ with $c_1(L_{\det})$ changing by $2\cdot$ the acting class, only finitely many $\sigma$ satisfy the bound.
  `Gaps:` the step from a bound on the $L^2$-norm of the curvature to finiteness of the set of classes needs: (a) the harmonic representative $h$ of $c_1$ satisfies $\|h\|\le\|\tfrac{i}{2\pi}F_A\|$, (b) integral classes with bounded harmonic norm are finite in number (lattice in a finite-dimensional space), (c) torsion classes: finitely many spin$^c$ structures share a given $c_1(L_{\det})$ (the map $\mathcal S(M)\to H^2(M;\mathbb Z)$, $\sigma\mapsto c_1(L_{\det})$ has finite fibres); the printed identity $|c_1\cup\operatorname{PD}(c_1)|=\tfrac1{4\pi^2}\|F_A\|^2$ is not literally correct (it is $\tfrac1{4\pi^2}\|h\|^2_{L^2}$ for the harmonic representative, with $\|h^+\|^2+\|h^-\|^2$; and the lower bound $c_1^2\ge2\chi+3\operatorname{sign}$ together with the upper bound on $\|F^-\|$ is what bounds both $\|h^\pm\|$).

### Examples: none.
### Exercises: none.

### Remarks / load-bearing paragraphs
- **R7.2.1 — Why $b_2^+\ge2$** (p. 71): a generic 1-parameter family of perturbations avoids the wall $Q$ of codimension $b_2^+\ge2$, so the bordism contains no reducibles.
- **R7.2.2 — Dependence on $\sigma$** (Remark 223, p. 71).
- **R7.2.3 — Construction of the cohomology class $\mu$ from the framed moduli space** (p. 71): realises the abstract scheme of §1 (D1.3); $\hat{\mathcal M}_\eta$ is the restriction of $\mathcal C^{\mathrm{irr}}/\mathcal G_0\to\mathcal C^{\mathrm{irr}}/\mathcal G$.
- **R7.2.4 — Odd-dimensional case set to zero by convention** (Definition 224).

### 7.2.1 Sample applications of the Seiberg–Witten invariant — `PDF page: 72`

#### Theorems (all stated without proof)
- **T7.2.3 — Vanishing for positive scalar curvature** (Theorem 226, Witten, p. 72). If $M$ with $b_2^+\ge2$ admits a metric of positive scalar curvature, then $\mathrm{sw}_M\equiv0$.
  `Proof in source: omitted ("follows easily from the Weitzenböck formula").` Intended: for $s_g>0$ the $C^0$ bound of Lemma 196 forces $\psi=0$ for unperturbed solutions (and small perturbations), so only reducibles exist, which are excluded for generic small $\eta$ when $b_2^+\ge1$; hence $\mathcal M_\eta=\varnothing$.
- **T7.2.4 — Vanishing for connected sums** (Theorem 227, Witten, p. 72). Let $M_1,M_2$ be closed four-manifolds both with $b_2^+\ge1$. Then the Seiberg–Witten invariant of $M_1\#M_2$ vanishes.
  `Proof in source: omitted.`
- **T7.2.5 — Non-vanishing for symplectic manifolds** (Theorem 228, Taubes, p. 72). If $M$ is symplectic and $b_2^+(M)\ge2$, then $\mathrm{sw}_M\not\equiv0$. (Viewed as an obstruction to existence of symplectic structures.)
  `Proof in source: omitted.`
- **T7.2.6 — Non-smoothable topological 4-manifolds** (Theorem 229, Donaldson, p. 72). There are (many) closed topological four-manifolds which do not admit a smooth structure.
  `Proof in source: omitted.` (Originally by other methods; obtainable via Seiberg–Witten theory.)
- **T7.2.7 — Infinitely many smooth structures** (Theorem 230, Fintushel–Stern, p. 72). There are infinitely many closed four-manifolds which are all homeomorphic but pairwise non-diffeomorphic.
  `Proof in source: omitted.`

#### Remarks
- **R7.2.5 — Interpretation** (p. 72): on a given closed topological 4-manifold there may be no smooth structure, or infinitely many.

### External results imported without proof (§7.2)
- **I7.2.1 — Theorem 222** (assembled, not proved).
- **I7.2.2 — Finiteness of integral classes of bounded norm** (lattice argument) (p. 71).
- **I7.2.3 — Theorems 226–230** (Witten, Witten, Taubes, Donaldson, Fintushel–Stern) (p. 72).

---

## Appendix A — Cross-reference table of the source's numbered items

| Source no. | Kind | Inventory id | Page |
|---|---|---|---|
| Def 1 | Definition | D2.1.1 | 4 |
| Ex 1 | Example | E2.1.1 | 5 |
| Exercise 2 | Exercise | X2.1.1 | 5 |
| Exercise 3 | Exercise | X2.1.2 | 5 |
| Def 4 | Definition | D2.1.5 | 6 |
| Exercise 5 | Exercise | X2.1.3 | 6 |
| (6) | equation (frame change) | D2.1.6 | 6 |
| (7) | equation (derivative) | R2.1.4 | 6 |
| Def 8 / (9) | Definition | D2.1.7 | 7 |
| Ex 10 | Example | E2.1.3 | 7 |
| Thm 11 | Theorem | T2.1.1 | 7 |
| Lemma 12 | Lemma | T2.1.2 | 7 |
| (13) | connection matrix | D2.1.8 | 8 |
| (14) | frame change of $A$ | R2.1.5 | 8 |
| Prop 15 / (16) | Proposition | T2.1.3 | 9 |
| Def 17 | Definition | D2.1.10 | 9 |
| (18) | $F=dA+A\wedge A$ | R2.1.7 | 10 |
| Rem 19 / (20) | Remark | R2.1.8 | 10 |
| Prop 21 | Proposition | T2.1.4 | 10 |
| Def 22 | Definition | D2.1.14 | 11 |
| Def 23 | Definition | D2.2.1 | 11 |
| (24) | chart on $\operatorname{Fr}(E)$ | D2.2.2 | 12 |
| Exercise 25 | Exercise | X2.2.1 | 12 |
| Def 26 | Definition | D2.2.3 | 12 |
| Exercise 27 | Exercise | X2.2.2 | 13 |
| Exercise 28 | Exercise | X2.2.3 | 13 |
| Exercise 29 | Exercise | X2.2.4 | 13 |
| (30) / Def 31 | Definition | D2.2.8 | 14 |
| Ex 32 | Example | E2.2.1 | 14 |
| Ex 33 / (34) | Example | E2.2.2 | 14 |
| Exercise 35 | Exercise | X2.2.5 | 15 |
| (36) / Prop 37 | Proposition | T2.2.2 | 15 |
| Def 38 | Definition | D2.2.11 | 16 |
| Prop 39 | Proposition | T2.2.3 | 16 |
| Def 40 | Definition | D2.2.13 | 16 |
| Thm 41 | Theorem | T2.2.4 | 16 |
| Ex 42 / (43) | Example | E2.2.3 | 17 |
| Exercise 44 | Exercise | X2.2.6 | 17 |
| (45) | $\rho_*$ | D2.2.14 | 17 |
| Thm 46 / (47) | Theorem | T2.2.5 | 17–18 |
| Exercise 48 | Exercise | X2.2.7 | 19 |
| (49) / Def 50 | Definition | D2.2.15 | 19 |
| Ex 51 | Example | E2.2.4 | 19–20 |
| Prop 52 | Proposition | T2.2.7 | 20 |
| Prop 53 | Bianchi | T2.2.8 | 20 |
| Rem 54 / (55) | Remark | R2.2.8 | 21 |
| Prop 56 | Proposition | T2.2.9 | 21 |
| (57), (58) | gauge group | D2.2.19 | 21 |
| Exercise 59 | Exercise | X2.2.9 | 22 |
| Ex 60 | Example | E2.2.5 | 22 |
| (61) | gauge action | D2.2.20 | 22 |
| Exercise 62 | Exercise | X2.2.10 | 22 |
| Exercise 63 | Exercise | X2.2.11 | 22 |
| Def 64 / (65) | Definition | D2.3.2 | 22 |
| Exercise 66 / (67) | Exercise | X2.3.1 | 22 |
| Thm 68 | Theorem | T2.3.1 | 23 |
| Def 69 | Definition | D2.4.1 | 23 |
| Thm 70 | Theorem | T2.4.1 | 23 |
| Def 71 | Definition | D2.4.2 | 24 |
| Ex 72 | Example | E2.4.1 | 24 |
| (73), (74), Def 75 | Definition | D2.4.5 | 25 |
| Exercise 76 | Exercise | X2.4.1 | 25 |
| Thm 77 | Theorem | T2.4.2 | 25 |
| Prop 78 | Proposition | T2.4.3 | 26 |
| Def 79 | Definition | D2.4.7 | 26 |
| Rem 80 | Remark | R2.4.3 | 26 |
| Ex 81 | Example | E3.1.1 | 27 |
| Lemma 82 / (83) | Lemma | T3.1.1 | 27–28 |
| Def 84 | Definition | D3.1.3 | 28 |
| Rem 85 | Remark | R3.1.2 | 28 |
| Rem 86 | Remark/Def | D3.1.4 | 28 |
| Thm 87 | Theorem | T3.1.2 | 28–29 |
| Exercise 88 | Exercise | X3.1.1 | 29 |
| Exercise 89 | Exercise | X3.1.2 | 29 |
| Thm 90 | Theorem | T3.1.3 | 29 |
| Rem 91 | Remark | R3.1.4 | 30 |
| Rem 92 | Remark | R3.1.5 | 30 |
| Rem 93 / (94) | Remark | R3.1.6 | 30 |
| (95) | Chern–Simons | D3.2.1 | 31 |
| Exercise 96 / (97) | Exercise | X3.2.1 | 31 |
| Prop 98 | Proposition | T3.2.1 | 31 |
| Rem 99 | Remark | R3.3.3 | 32 |
| Def 100 | Definition | D3.3.3 | 32 |
| Def 101 | Definition | D3.3.4 | 33 |
| Exercise 102 | Exercise | X3.3.1 | 33 |
| Rem 103 | Remark | R3.3.5 | 33 |
| Exercise 104 | Exercise | X3.3.2 | 33 |
| Rem 105 | Remark | R3.3.6 | 34 |
| Prop 106 | Proposition | T3.3.2 | 34 |
| Ex 107 | Example | E3.3.1 | 34 |
| Ex 108 | Example | E3.3.2 | 34 |
| (109) | $\alpha\colon Sp(1)\to SO(3)$ | T4.1.1 | 35 |
| (110) | Clifford action on forms | E4.1.2 | 35 |
| (111) | $\operatorname{Im}\mathbb H\otimes\mathbb C\cong\operatorname{End}_0\slashed S$ | T4.1.3 | 36 |
| (112) | $Cl(\mathbb R^4)$-module | E4.1.4 | 36 |
| Def 113 | Definition | D4.2.3 | 37 |
| Ex 114 | Example | E4.2.1 | 37 |
| Exercise 115 | Exercise | X4.2.1 | 37 |
| Def 116 | Definition | D4.3.1 | 37 |
| Rem 117 | Remark | R4.3.2 | 38 |
| Ex 118 | Example | E4.3.1 | 38 |
| Exercise 119 | Exercise | X4.3.1 | 38 |
| (120) | $Spin^c$ sequence | D4.3.5 | 39 |
| Ex 121 | Example | E4.3.2 | 39 |
| Def 122 | Definition | D4.3.6 | 39 |
| Prop 123 | Proposition | T4.3.1 | 39 |
| Ex 124 | Example | E4.3.3 | 40 |
| Rem 125 | Remark | R4.3.4 | 40 |
| Exercise 126 / (127) | Exercise | X4.3.2 | 40 |
| (128) | $\slashed D^2=\Delta$ on $\mathbb R^4$ | T4.4.1 | 41 |
| Rem 129 | Remark | E4.4.1 | 41 |
| (130) | connection Laplacian | D4.4.1 | 42 |
| Exercise 131 | Exercise | X4.4.1 | 42 |
| Thm 132 | Weitzenböck | T4.4.2 | 42 |
| Cor 133 | Corollary | T4.4.3 | 43 |
| (134) | Dirichlet problem | R5.1.1 | 43 |
| Rem 135 | Remark | R5.1.2 | 44 |
| Thm 136 / (137) | Sobolev | T5.1.1 | 45 |
| Rem 138 / (139) | Remark | R5.1.4 | 45–46 |
| (140) | differential operator | D5.2.1 | 46 |
| Def 141 | Definition | D5.2.3 | 46 |
| Ex 142 | Example | E5.2.1 | 47 |
| Ex 143 | Example | E5.2.2 | 47 |
| Ex 144 | Example | E5.2.3 | 47 |
| (145) | Sobolev extension | R5.2.2 | 47 |
| Thm 146 | Elliptic estimate | T5.2.1 | 48 |
| (147) | formal adjoint | D5.2.5 | 48 |
| Thm 148 | Fredholm alternative | T5.2.2 | 48 |
| Rem 149 | Remark | T5.2.3 | 48 |
| Def 150 | Definition | D5.2.6 | 48 |
| Rem 151 | Remark | T5.2.4 | 48 |
| Exercise 152 | Exercise | X5.2.1 | 49 |
| Thm 153 | Theorem | T5.2.5 | 49 |
| (154) | complex | D5.3.1 | 49 |
| Exercise 155 | Exercise | X5.3.1 | 49 |
| Thm 156 / (157) | Hodge | T5.3.1 | 50 |
| (158) | Hodge decomposition | T5.3.2 | 50 |
| Exercise 159 | Exercise | X5.3.2 | 51 |
| Exercise 160 | Exercise | X5.3.3 | 52 |
| Def 161 | Definition | D6.1.1 | 52 |
| Thm 162 | Kuranishi | T6.1.1 | 52 |
| Cor 163 | Corollary | T6.1.2 | 52 |
| Thm 164 | Sard–Smale | T6.1.3 | 53 |
| Thm 165 | Theorem | T6.1.4 | 53 |
| Thm 166 / (167) | Theorem | T6.2.1 | 53–55 |
| Cor 168 | Corollary | T6.2.2 | 55 |
| Lemma 169 | Lemma | T6.3.1 | 55 |
| (170) | exact sequence | R6.4.2 | 57 |
| Exercise 171 | Exercise | X6.4.1 | 57 |
| Def 172 | Definition | D6.4.3 | 57 |
| Prop 173 | Proposition | T6.4.2 | 57 |
| (174), (175) | bordism, degree | D6.5.2 | 58 |
| Thm 176 | Theorem | T6.5.1 | 58 |
| (177) | infinitesimal action | D6.6.1 | 59 |
| Def 178 | Definition | D6.6.2 | 59 |
| Prop 179 | Proposition | T6.6.1 | 59 |
| Ex 180 | Example | E6.6.1 | 59 |
| (181) | deformation complex | D6.6.3 | 59 |
| (182) | $D_x$ | D6.6.4 | 60 |
| Thm 183 | Theorem | T6.6.2 | 60 |
| Thm 184 | Theorem | T6.6.3 | 60 |
| (185)–(187) | identifications | T7.1.1 | 61 |
| (188) | SW equations | D7.1.2 | 61 |
| (189) | gauge action | D7.1.3 | 62 |
| Lemma 190 | Lemma | T7.1.2 | 62 |
| (191) | deformation complex | D7.1.5 | 62 |
| Lemma 192 | Lemma | T7.1.4 | 63 |
| Prop 193 | Proposition | T7.1.6 | 63 |
| Prop 194 | Proposition | T7.1.5 | 63 |
| Prop 195 | Proposition | T7.1.7 | 64 |
| Lemma 196 | Lemma | T7.1.8 | 64–65 |
| Rem 197 | Remark | T7.1.9 | 65 |
| Cor 198 | Corollary | T7.1.10 | 65 |
| Cor 199 / (200) | Corollary | T7.1.11 | 65 |
| Rem 201 | Remark | T7.1.12 | 65 |
| Lemma 202 | Lemma | T7.1.13 | 66 |
| Prop 203 / (204) | Proposition | T7.1.14 | 66 |
| Cor 205 | Corollary | T7.1.15 | 66–67 |
| Thm 206 | Theorem | T7.1.16 | 67 |
| Prop 207 | Proposition | T7.1.17 | 67 |
| Prop 208 / (209), (210) | Proposition | T7.1.18 | 68 |
| (211) | elliptic operator | T7.1.19 | 68 |
| Cor 212 / (213) | Corollary | T7.1.20 | 69 |
| (214), (215) | $D_{(\psi,A)}$, $D_0$ | D7.1.15 | 69 |
| Rem 216 | Remark | T7.1.21 | 69 |
| Prop 217 | Proposition | T7.1.22 | 69 |
| Cor 218 | Corollary | T7.1.23 | 69 |
| Lemma 219 | Lemma | T7.1.24 | 70 |
| Rem 220 | Remark | T7.1.25 | 70 |
| Rem 221 | Remark | T7.1.27 | 70 |
| Thm 222 | Theorem | T7.2.1 | 71 |
| Rem 223 | Remark | R7.2.2 | 71 |
| Def 224 | Definition | D7.2.2 | 71 |
| Thm 225 | Theorem | T7.2.2 | 71 |
| Thm 226 | Witten | T7.2.3 | 72 |
| Thm 227 | Witten | T7.2.4 | 72 |
| Thm 228 | Taubes | T7.2.5 | 72 |
| Thm 229 | Donaldson | T7.2.6 | 72 |
| Thm 230 | Fintushel–Stern | T7.2.7 | 72 |

## Appendix B — Typos and inconsistencies in the source that writers must resolve

1. p. 6: $g\colon U\cap U'\to GL_n(\mathbb R)$ should be $GL_k(\mathbb R)$.
2. p. 21, (58): $\hat f(pg)=g^{-1}pg$ should read $\hat f(pg)=g^{-1}\hat f(p)g$.
3. p. 22, Exercise 63: target should be $\Omega^1(\operatorname{ad}P)$, not $\Omega^0$.
4. p. 27, Example 81(a): "$p_d(\xi)=i\operatorname{tr}\xi^d$" — the factor $i$ does not make $p_d$ real for $d\ge2$; treat as $\operatorname{tr}\xi^d$ (or $i^d\operatorname{tr}\xi^d$).
5. p. 30, Remark 92: $\int_M$ should be $\int_\Sigma$.
6. p. 31, Exercise 96(a) second display: missing factor $\tfrac1{8\pi^2}$.
7. p. 32: $\gamma^*\nabla=\tfrac d{dt}+B(t)dt$ then "$\dot s+A(t)s=0$" — $A=B$.
8. p. 33: "$\rho\colon\tilde M\to GL_k(\mathbb R)$" should be $\rho\colon\pi_1(M)\to GL_k(\mathbb R)$.
9. p. 34, Example 107: $\operatorname{Hom}(T^n,U(1))$ means $\operatorname{Hom}(\pi_1(T^n),U(1))=\operatorname{Hom}(\mathbb Z^n,U(1))$.
10. p. 47, Example 144: inverse of Clifford multiplication by $\xi$ is $-|\xi|^{-2}\xi$ with the convention $u\cdot u=-|u|^2$.
11. p. 48: index of a finite-dimensional map $X\to Y$ is $\dim X-\dim Y$, not $\dim Y-\dim X$.
12. p. 48, Theorem 148: "$t\in\ker L^*$" should be "$t\perp\ker L^*$".
13. p. 51: "unique non-positive integer" should be "non-negative".
14. p. 58, (175): $\sum_i\varepsilon_k$ should be $\sum_i\varepsilon_i$.
15. p. 60, proof of Thm 183: $\operatorname{Im}R_w$ should be $\operatorname{Im}R_x$.
16. p. 61: expanded form of $\mu(\psi)(\phi)$ has $+\tfrac12|\psi|^2\phi$; consistency with the matrix form and tracelessness requires $-\tfrac12|\psi|^2\phi$.
17. p. 65, Lemma 196 proof: factor-2 inconsistency between "$\tfrac14|\psi|^4$" in the Weitzenböck identity and "$\tfrac12|\psi|^4$" in the following inequality; also the sign convention for $\int F^\pm\wedge F^\pm$ in Cor. 199 must be fixed (see T7.1.11 gaps).
18. p. 65, (200): the second inequality bounds $\|F_A^-\|^2_{L^2}$, not $\|F^-_A\|_{L^2}$.
19. p. 66, Prop. 203 proof: the pointwise bound uses $\nabla^{LC}$ on $F^+_A$ and $\nabla_{A_0}$ on $\psi$; a consistent choice of connection is needed.
20. p. 68, (211): the target should include the $W^{4,2}(\mathbb Ri)$ summand as in (214).
21. p. 69: $\operatorname{index}(d^++d^*)=b_1-b_0-b_2^+=-\tfrac12(\chi+\operatorname{sign})$, not $+\tfrac12(\chi+\operatorname{sign})$; final formula (213) is nevertheless correct.
22. p. 71: notation clash — $\mu$ denotes both the quadratic map and $c_1$ of the framed moduli space; the identity $|c_1\cup\operatorname{PD}(c_1)|=\tfrac1{4\pi^2}\|F_A\|^2_{L^2}$ holds for the harmonic representative only.
23. Section title "The modui space of flat connections" (p. 1, 32) = "moduli".
