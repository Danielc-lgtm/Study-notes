# Section 1: Prerequisite DAG

Legend: 🟢 = Anchor (familiarity ≥ 7, known) · 🔵 = To learn · ⭐ = High priority hub

---

## Foundations

> [!note]- 🟢 Linear Algebra (7,7) — ANCHOR
> **Prereqs:** None (root)
>
> **Status:** Known — used as foundation throughout

> [!note]- 🔵 Multivariate Analysis (5,7)
> **Prereqs:** None (root)
>
> **Gaps:** Unsure which operations are legal/illegal for far-out-of-distribution generalization

> [!note]- 🟢 Ordinary Differential Equations (8,8) — ANCHOR
> **Prereqs:** 🟢 Linear Algebra, Multivariate Analysis
>
> **Status:** Known — foundation for dynamical systems, control, SDEs, PDE

> [!note]- 🔵 Measure Theory (5,8)
> **Prereqs:** 🟢 Linear Algebra
>
> **Gaps:** Big picture understood, no full course done

> [!note]- ⭐🔵 Topology (5,7)
> **Prereqs:** None (root)
>
> **Gaps:** Used frequently but never done a full course, sometimes forget definitions
>
> **Note:** HIGH LEVERAGE — gates ~25 downstream nodes including Algebraic Topology, Differential Geometry

> [!note]- 🔵 Complex Analysis (4,7)
> **Prereqs:** Multivariate Analysis, Topology
>
> **Gaps:** Use complex operations frequently, never taken course

> [!note]- ⭐🔵 Abstract Algebra / Ring Theory / Modules (3,8)
> **Prereqs:** None (root)
>
> **Gaps:** Know what rings are but never taken ring theory course, often forget definitions
>
> **Note:** HIGH LEVERAGE — gates entire algebra column

> [!note]- 🟢 Advanced Probability / Measure-Theoretic (7,9) — ANCHOR
> **Prereqs:** Measure Theory
>
> **Status:** Known — used very frequently in IT and stochastics

> [!note]- 🔵 Special Relativity / Classical Electrodynamics / Wave Equations (4,7)
> **Prereqs:** 🟢 Linear Algebra, Multivariate Analysis
>
> **Gaps:** Familiar with group-theoretic approach, shaky on physical intuition

---

## Geometry

> [!note]- ⭐🔵 Differential Geometry / Differential Topology / Integration on Manifolds
> **Prereqs:** 🟢 Linear Algebra, Multivariate Analysis, Topology
>
> **Note:** HIGHEST LEVERAGE HUB — out-degree ~14, gates entire geometry column

> [!note]- 🔵 Tensor Calculus
> **Prereqs:** 🟢 Linear Algebra, Multivariate Analysis
>
> **Note:** Often co-taught with Differential Geometry

> [!note]- 🔵 Riemannian Geometry
> **Prereqs:** Differential Geometry, 🟢 Linear Algebra, Tensor Calculus

> [!note]- 🔵 Symplectic Geometry
> **Prereqs:** Differential Geometry, 🟢 Linear Algebra (symplectic linear algebra)

> [!note]- 🔵 Complex Geometry
> **Prereqs:** Complex Analysis, Differential Geometry, Algebraic Topology (basic)

> [!note]- 🔵 Kähler Geometry
> **Prereqs:** Riemannian Geometry, Complex Geometry, Symplectic Geometry

> [!note]- 🔵 Calabi-Yau Manifolds
> **Prereqs:** Kähler Geometry, Complex Geometry, Riemannian Geometry, Algebraic Geometry (for the projective/algebraic definition), 🟢 PDE, Geometric Analysis (for Yau's theorem)
>
> **Connects:** Kähler Geometry ↔ Algebraic Geometry ↔ Riemannian Geometry (Ricci-flat / SU(n) holonomy) ↔ Symplectic Geometry (mirror symmetry) ↔ String Theory
>
> **Note:** A Calabi-Yau is a compact Kähler manifold with vanishing first Chern class, equivalently (Yau's theorem, proving the Calabi conjecture) admitting a Ricci-flat Kähler metric, equivalently having holonomy in $SU(n)$ with a nowhere-vanishing holomorphic volume form. The three definitions being equivalent — algebraic ($c_1 = 0$), analytic (Ricci-flat), holonomy ($SU(n)$) — is exactly why this sits at the crossing of algebraic geometry, PDE, and Riemannian geometry: the proof routes through the complex Monge-Ampère equation, so it is a Geometric Analysis result with an Algebraic Geometry statement.
>
> **Unlocks:** Mirror symmetry (A-model on $X$ ↔ B-model on the mirror $X^\vee$; Kontsevich's homological mirror symmetry as an equivalence of the Fukaya category with the derived category of coherent sheaves — the bridge to the Symplectic and Derived AG nodes), Gromov-Witten / enumerative invariants, special holonomy, string compactification

> [!note]- 🔵 De Rham Cohomology
> **Prereqs:** Differential Geometry, Algebraic Topology (basic)

> [!note]- 🔵 Riemann Surfaces
> **Prereqs:** Complex Analysis, Topology, Algebraic Topology (basic)

> [!note]- ⭐🔵 Lie Groups / Lie Algebras / Representation Theory (5,10)
> **Prereqs:** Differential Geometry, Abstract Algebra, 🟢 Linear Algebra, Topology
>
> **Note:** HIGH LEVERAGE HUB — out-degree ~8, gates Gauge Theory, QFT, GR, Geometric Mechanics in Robotics

> [!note]- 🔵 Geometric Quantization
> **Prereqs:** Symplectic Geometry, Differential Geometry (line bundles, connections, curvature), Lie Groups / Lie Algebras / Representation Theory (orbit method), Quantum Mechanics for Mathematicians (the target formalism), Kähler Geometry (for Kähler polarizations)
>
> **Connects:** Symplectic Geometry ↔ Representation Theory (Kirillov orbit method, Borel-Weil-Bott) ↔ Index Theory (quantization commutes with reduction) ↔ Kähler Geometry (Kähler polarizations, Berezin-Toeplitz) ↔ Microlocal / Semiclassical Analysis (the $\hbar \to 0$ comparison) ↔ TQFT (Chern-Simons quantization of moduli of flat connections) ↔ Geometric Mechanics (momentum maps, coadjoint orbits)
>
> **Note:** The program that manufactures a quantum Hilbert space from a classical phase space $(M, \omega)$, in two stages. **Prequantization:** a Hermitian line bundle $L \to M$ with connection of curvature proportional to $\omega$ exists exactly when the Weil integrality condition $[\omega/2\pi\hbar] \in H^2(M;\mathbb{Z})$ holds, and the Kostant-Souriau operator $\hat{f} = -i\hbar\nabla_{X_f} + f$ then represents the full Poisson algebra on sections of $L$ — but the space is too big (states depend on position *and* momentum). **Polarization:** an integrable Lagrangian subbundle $P \subset TM \otimes \mathbb{C}$ cuts the sections down to those covariantly constant along $P$ — the vertical polarization on $T^*Q$ recovers the position representation $L^2(Q)$, a Kähler polarization gives holomorphic sections (Bargmann-Fock, Borel-Weil), and the half-form (metaplectic) correction repairs the vacuum energy and inner products. The Groenewold-van Hove no-go theorem is the reason the subject exists at all: no map quantizes every classical observable consistently, so quantization is genuinely extra structure, and the polarization-dependence question (do different polarizations give unitarily equivalent theories?) is the deep open nerve of the subject. Member of Cluster 5 — the cluster theme "quantization = symplectic → Hilbert" is literally this node; also ties to Cluster 19 (the mathematical substrate of QM and gauge theory) and Cluster 4 (momentum maps and coadjoint orbits are the geometric-mechanics inputs).
>
> **Unlocks:** Kirillov's orbit method (coadjoint orbits ↔ irreducible unitary representations, turning representation theory of nilpotent and compact groups into symplectic geometry), Borel-Weil-Bott as Kähler quantization of flag manifolds, Guillemin-Sternberg "quantization commutes with reduction" ($[Q, R] = 0$, proved via the Spin-c Dirac index — the bridge to the Index Theory node), Chern-Simons / Reshetikhin-Turaev TQFT from quantizing moduli of flat connections (the bridge to the TQFT node), Berezin-Toeplitz and deformation quantization (Fedosov, Kontsevich — the formal-algebraic counterpart, and the bridge to Noncommutative Geometry)
>
> **Key refs:** Woodhouse, *Geometric Quantization* (Oxford, 2nd ed., 1992) — the standard reference; Hall, *Quantum Theory for Mathematicians* (Springer GTM 267, 2013), Chapters 22–23 — the gentlest rigorous entry; Bates-Weinstein, *Lectures on the Geometry of Quantization* (AMS Berkeley Mathematics Lecture Notes 8, 1997); Kirillov, *Lectures on the Orbit Method* (AMS GSM 64, 2004)

> [!note]- 🔵 Hodge Theory
> **Prereqs:** Riemannian Geometry, De Rham Cohomology, 🟢 Functional Analysis (elliptic), Complex Geometry

> [!note]- 🔵 Mathematical Gauge Theory
> **Prereqs:** Differential Geometry, Lie Groups/Lie Algebras, 🟢 PDE, 🟢 Functional Analysis
>
> **Connects:** Differential Geometry (connections on principal bundles) ↔ Lie Groups ↔ PDE / Stochastic Analysis (Yang-Mills flow and its stochastic quantization) ↔ Index Theory ↔ QFT
>
> **Note:** Connections on principal bundles, curvature, and the Yang-Mills functional with its critical points (instantons, anti-self-dual equations). The probabilistic construction of the Yang-Mills measure belongs here: it is realized as the invariant measure of a gauge-covariant Langevin dynamic on the space of connections modulo gauge — stochastic quantization in the sense of Parisi-Wu — made rigorous in 2D and 3D via regularity structures (Chandra-Chevyrev-Hairer-Shen; Chevyrev). Full references in the Stochastic Field Theory node.

> [!note]- 🔵 Index Theory
> **Prereqs:** Riemannian Geometry, Algebraic Topology, 🟢 Functional Analysis (Fredholm), Spectral Theory, Lie Groups

> [!note]- 🔵 Spectral Geometry
> **Prereqs:** Riemannian Geometry, Spectral Theory, 🟢 PDE

> [!note]- 🔵 Geometric Analysis
> **Prereqs:** Riemannian Geometry, 🟢 PDE, Variational Calculus

> [!note]- 🔵 Ricci Flow
> **Prereqs:** Riemannian Geometry, 🟢 PDE, Geometric Analysis

> [!note]- 🔵 Conformal Geometry / Geometric Complex Analysis (1,10)
> **Prereqs:** Complex Analysis, Differential Geometry, Riemann Surfaces

> [!note]- 🔵 Morse Theory / Catastrophe Theory (1,10)
> **Prereqs:** Differential Geometry, Algebraic Topology

---

## Analysis

> [!note]- 🟢 Functional Analysis (8,10) — ANCHOR
> **Prereqs:** 🟢 Linear Algebra, Measure Theory, Topology
>
> **Status:** Known — HIGH LEVERAGE HUB, out-degree ~11

> [!note]- 🟢 Analysis of PDEs — ANCHOR
> **Prereqs:** 🟢 Functional Analysis, Multivariate Analysis, Distribution Theory
>
> **Status:** Strong background

> [!note]- 🔵 Distribution Theory
> **Prereqs:** 🟢 Functional Analysis, Topology

> [!note]- 🔵 Variational Calculus
> **Prereqs:** 🟢 Functional Analysis, 🟢 PDE, Multivariate Analysis

> [!note]- 🔵 Harmonic Analysis
> **Prereqs:** 🟢 Functional Analysis, Measure Theory, Distribution Theory

> [!note]- 🔵 Spectral Theory
> **Prereqs:** 🟢 Functional Analysis, Measure Theory

> [!note]- 🔵 Operator Theory
> **Prereqs:** 🟢 Functional Analysis, Spectral Theory

> [!note]- 🔵 Operator Algebra (C*, von Neumann)
> **Prereqs:** 🟢 Functional Analysis, Spectral Theory, Operator Theory

> [!note]- 🔵 Fredholm Theory
> **Prereqs:** 🟢 Functional Analysis, Operator Theory

> [!note]- 🔵 Nonlinear functional Analysis
> **Prereqs:** 🟢 Functional Analysis, Variational Calculus, 🟢 PDE

> [!note]- 🔵 Dynamical Systems (4,10)
> **Prereqs:** Multivariate Analysis, Differential Geometry (basic)

> [!note]- 🔵 Ergodic Theory
> **Prereqs:** Measure Theory, Dynamical Systems, 🟢 Functional Analysis

> [!note]- 🔵 Chaos Theory / Nonlinear Dynamics
> **Prereqs:** Dynamical Systems

> [!note]- 🔵 Coupled Oscillators / Network Dynamics / Complex Systems Theory
> **Prereqs:** Dynamical Systems, Chaos Theory, Graph Theory (basic)

---

## Stochastics

> [!note]- 🟢 SDEs (7,10) — ANCHOR
> **Prereqs:** 🟢 Measure-Theoretic Probability, 🟢 Functional Analysis (basic)
>
> **Status:** Known

> [!note]- 🔵 Martingale Theory
> **Prereqs:** 🟢 Measure-Theoretic Probability

> [!note]- ⭐🔵 Stochastic Analysis
> **Prereqs:** 🟢 SDEs, Martingale Theory, 🟢 Functional Analysis
>
> **Note:** HIGH LEVERAGE — out-degree ~9, gates Malliavin, Rough Paths, GFF, SLE, MFGs

> [!note]- 🔵 Fokker-Planck
> **Prereqs:** 🟢 SDEs, 🟢 PDE, Distribution Theory

> [!note]- 🔵 Malliavin Calculus
> **Prereqs:** Stochastic Analysis, 🟢 Functional Analysis, Measure Theory

> [!note]- 🔵 Rough Paths Theory
> **Prereqs:** Stochastic Analysis, Hopf Algebras (for branched), 🟢 Functional Analysis

> [!note]- 🔵 Information Geometry
> **Prereqs:** Differential Geometry, Riemannian Geometry, 🟢 Measure-Theoretic Probability, 🟢 Information Theory

> [!note]- 🔵 Gradient Flow
> **Prereqs:** Optimal Transport, 🟢 PDE, 🟢 Functional Analysis, Variational Calculus

> [!note]- 🔵 Boltzmann / Landau Equation
> **Prereqs:** 🟢 PDE, 🟢 Functional Analysis, 🟢 Measure-Theoretic Probability

> [!note]- 🔵 Gaussian Free Field
> **Prereqs:** Stochastic Analysis, Distribution Theory, Harmonic Analysis

> [!note]- 🔵 GFF Isomorphism Theorems / Loop Soups
> **Prereqs:** Gaussian Free Field, Martingale Theory, Stochastic Analysis, 🟢 Measure-Theoretic Probability, Spectral Theory (Laplacian determinants)
>
> **Connects:** Gaussian Free Field ↔ Local Times / Occupation Fields ↔ Markov Loop Soups ↔ Spectral Determinants / Analytic Torsion ↔ Electrical Networks (matrix-tree)
>
> **Note:** The Gaussian field attached to the Laplacian, viewed dynamically. The GFF has covariance the Green's function $(-\Delta)^{-1}$, and the Dynkin / Eisenbaum / Le Jan isomorphism theorems identify its square with the occupation field of a Poissonian ensemble of Markov loops (the loop soup) — so a Gaussian field and the local times of the underlying diffusion are one object. On graphs this links to the matrix-tree theorem (the Laplacian determinant counts weighted spanning trees), Wilson's algorithm, and electrical networks; the $\zeta$-regularized Laplacian determinant is at once the GFF partition function and, via Ray-Singer, analytic torsion — closing the loop back to spectral-topological invariants.
>
> **Key refs:** Le Jan, *Markov Paths, Loops and Fields* (Saint-Flour XXXVIII-2008, Springer LNM 2026, 2011); Marcus-Rosen, *Markov Processes, Gaussian Processes, and Local Times* (Cambridge Studies in Advanced Mathematics 100, 2006); Sznitman, *Topics in Occupation Times and Gaussian Free Fields* (EMS, 2012).

> [!note]- 🔵 Random Conformal Geometry
> **Prereqs:** Conformal Geometry, Gaussian Free Field, Complex Analysis

---

## Algebra

> [!note]- 🔵 Geometric Algebra / Multilinear Algebra (3,9)
> **Prereqs:** 🟢 Linear Algebra, Abstract Algebra

> [!note]- ⭐🔵 Commutative and Noncommutative Algebra (1,6)
> **Prereqs:** Abstract Algebra
>
> **Note:** HIGH LEVERAGE — out-degree ~7, gates Algebraic Geometry, Galois, Singularity Theory, Tropical, Algebraic Statistics

> [!note]- 🔵 Universal Algebra (1,6)
> **Prereqs:** Abstract Algebra, Mathematical Logic

> [!note]- 🔵 Modular Forms
> **Prereqs:** Complex Analysis, Riemann Surfaces (modular curves), Topology / group theory (the modular group $SL(2,\mathbb{Z})$ and congruence subgroups), Abstract Algebra (lattices, Hecke operators); the representation-theoretic and physics applications additionally use Lie Groups / Representation Theory (affine characters) and QFT / CFT
>
> **Connects:** Complex Analysis ↔ Conformal Field Theory (modular invariance) ↔ Representation Theory (affine Lie algebra / RCFT characters) ↔ Index Theory (elliptic genus) ↔ TQFT (modular tensor categories, S and T matrices) ↔ String Theory / S-duality
>
> **Note (physics emphasis):** A modular form of weight $k$ is a holomorphic function on the upper half-plane transforming as $f\!\left(\tfrac{a\tau+b}{c\tau+d}\right) = (c\tau+d)^k f(\tau)$ under $SL(2,\mathbb{Z})$. The physics enters because $\tau$ is the modular parameter of a torus, so $SL(2,\mathbb{Z})$ is the mapping class group of the worldsheet or spacetime torus, and any quantity computed on a torus that respects large diffeomorphisms must be modular. Concretely: (1) **2D CFT** — the torus partition function $Z(\tau) = \mathrm{Tr}\, q^{L_0 - c/24}$ must be modular invariant, which constrains the spectrum; the Cardy formula for the asymptotic density of states follows from the $S$-transform and reproduces the BTZ black-hole entropy via $\mathrm{AdS}_3/\mathrm{CFT}_2$. (2) **Rational CFT** — characters of affine Lie algebras and vertex operator algebras are vector-valued modular forms; the modular $S$ and $T$ matrices represent $SL(2,\mathbb{Z})$ and feed the Verlinde formula, a direct tie to the TQFT node's modular tensor categories. (3) **String theory** — one-loop amplitudes integrate over the fundamental domain of $SL(2,\mathbb{Z})$, and modular invariance is exactly what removes the dangerous UV region; lattice theta functions ($E_8$, Leech) appear in heterotic partition functions. (4) **Dualities** — $\mathcal{N}=4$ super Yang-Mills S-duality (Montonen-Olive) acts as $SL(2,\mathbb{Z})$ on the complexified coupling $\tau = \tfrac{\theta}{2\pi} + \tfrac{4\pi i}{g^2}$, so its BPS partition functions are modular.
>
> **Unlocks:** Elliptic genus / Witten genus (a modular-form-valued index, bridging Index Theory and TQFT), monstrous moonshine (the $j$-function and the Monster via VOAs and string theory on the Leech orbifold — Borcherds), mock modular forms and black-hole microstate counting (Dabholkar-Murthy-Zagier, Sen), the modular prepotential of Seiberg-Witten theory

> [!note]- 🔵 Galois Theory / Automorphic Forms (1,7)
> **Prereqs:** Abstract Algebra, Commutative Algebra, Complex Analysis (for automorphic)

> [!note]- ⭐🔵 Algebraic Topology (1,10)
> **Prereqs:** Topology, Abstract Algebra
>
> **Note:** HIGH LEVERAGE HUB — out-degree ~10, gates Algebraic Geometry, De Rham, Hodge, Index Theory, Floer, Morse, Operads, Derived AG, HoTT, NCG

> [!note]- 🔵 Algebraic Geometry (1,10)
> **Prereqs:** Commutative Algebra, Topology, Abstract Algebra, Category Theory (basic), Algebraic Topology (useful)

> [!note]- 🔵 Singularity Theory (1,6)
> **Prereqs:** Commutative Algebra, Differential Geometry, Algebraic Geometry

> [!note]- 🔵 Hopf Algebras
> **Prereqs:** Abstract Algebra, 🟢 Linear Algebra (multilinear), Category Theory (basic monoidal)
>
> **Unlocks:** Rough Paths (branched), Regularity Structures, Renormalization Group (Connes-Kreimer), Noncommutative Geometry, Geometric/Topological Recursion

> [!note]- 🔵 Operads / PROPs / Modular Operads
> **Prereqs:** Category Theory, Algebraic Topology, Abstract Algebra
>
> **Unlocks:** Factorization Algebras, Compositional Game Theory (deep), Categorical Systems Theory, QFT rigorization

> [!note]- 🔵 Derived / Homological Algebra
> **Prereqs:** Abstract Algebra, Category Theory, Algebraic Topology
>
> **Unlocks:** Derived Algebraic Geometry, Condensed Mathematics, Factorization Algebras, D-modules, Information Cohomology (Baudot-Bennequin)

> [!note]- 🔵 Algebraic Coding Theory / Error-Correcting Codes
> **Prereqs:** Abstract Algebra (finite fields), 🟢 Linear Algebra, 🟢 Information Theory; the AG codes additionally use Algebraic Geometry, and the modern capacity-achieving codes use 🟢 Measure-Theoretic Probability / Martingale Theory
>
> **Connects:** Information Theory (Shannon limit) ↔ Abstract Algebra / Finite Fields ↔ Galois Theory ↔ Algebraic Geometry (Goppa / AG codes) ↔ Probabilistic Graphical Models (LDPC message passing) ↔ Martingale Theory (polar codes)
>
> **Note:** Where the most neglected area (algebra) does load-bearing work for the strongest (information theory). Classical algebraic codes — Hamming, Reed-Solomon, BCH — are built from the structure of finite fields $\mathbb{F}_q$ and the factorization of $x^n - 1$, with decoding a problem in polynomial algebra (Berlekamp-Massey). Goppa / algebraic-geometry codes are constructed from the rational points and the Riemann-Roch space of a curve over a finite field, and were the first to beat the Gilbert-Varshamov bound — a direct, surprising payoff of Algebraic Geometry. The modern capacity-achieving families connect elsewhere: LDPC codes are decoded by belief propagation on a sparse Tanner graph (a message-passing / graphical-model instance), and polar codes (Arıkan) are built from a channel-polarization martingale that converges to perfectly good or perfectly bad sub-channels. Searchable under "algebraic coding theory" and "error-correcting codes." Bridges Cluster 13 (finite-field / Galois machinery) and Cluster 20 (LDPC = message passing).

---

## Probability

> [!note]- 🔵 Optimal Transport (5,10)
> **Prereqs:** Measure Theory, 🟢 Functional Analysis, Convex Optimization, 🟢 PDE

> [!note]- 🟢 Information Theory — ANCHOR
> **Prereqs:** 🟢 Measure-Theoretic Probability
>
> **Status:** Known — primary research tool

> [!note]- 🔵 Large Deviations Theory
> **Prereqs:** 🟢 Measure-Theoretic Probability, 🟢 Information Theory

> [!note]- 🔵 High-Dimensional Probability
> **Prereqs:** 🟢 Measure-Theoretic Probability, 🟢 Functional Analysis (concentration)

> [!note]- 🔵 Networked Information Theory
> **Prereqs:** 🟢 Information Theory, High-Dimensional Probability

---

## Category Theory

> [!note]- ⭐🔵 Category Theory (4,10)
> **Prereqs:** Abstract Algebra, Topology (motivation), 🟢 Linear Algebra
>
> **Note:** HIGHEST LEVERAGE HUB alongside Diff Geom — out-degree ~12

> [!note]- 🔵 Higher Category Theory
> **Prereqs:** Category Theory, Algebraic Topology
>
> **Note:** Covers 2-categories, bicategories, enriched categories, and the conceptual foundations. For the full ∞-categorical track (quasi-categories, model categories, ∞-topoi), see the dedicated nodes below.

> [!note]- 🔵 String Diagrams
> **Prereqs:** Category Theory (monoidal)

> [!note]- 🔵 Symmetric Monoidal Categories
> **Prereqs:** Category Theory, String Diagrams

> [!note]- 🔵 Polynomial Functors (Spivak)
> **Prereqs:** Category Theory, Type Theory (useful)

> [!note]- 🔵 Categorical Systems Theory (Myers, Spivak, davidad)
> **Prereqs:** Category Theory, Polynomial Functors, Symmetric Monoidal Categories, Double Categories
>
> **Note:** Myers' framework: symmetric monoidal loose right modules of systems over double categories of interfaces. Subsumes ODEs, SDEs, PDEs, automata, Petri nets, open Markov processes as coalgebras for polynomial endofunctors (St. Clere Smithe). davidad's Safeguarded AI / OAA programme uses this as the type system for compositional world models.
>
> **Key refs:** Myers, *Categorical Systems Theory*; Niu-Spivak, *Polynomial Functors* (Cambridge 2024); St. Clere Smithe arXiv:2206.03868

> [!note]- 🔵 Double Categories / 2-Category Theory
> **Prereqs:** Category Theory
>
> **Note:** Needed for Myers' categorical systems theory (systems as morphisms in a double category), lax/oplax functors, and the Org bicategory of dynamic organizations in Poly

> [!note]- 🔵 Tangent Categories (Cockett-Cruttwell)
> **Prereqs:** Category Theory, Differential Geometry (motivation)
>
> **Note:** Axiomatize the tangent-bundle functor T abstractly, recovering synthetic differential geometry and supporting generalized vector fields, connections, and ODEs categorically. davidad's key open question: find a category that is simultaneously a tangent category and carries a probability monad.
>
> **Key refs:** Cockett-Cruttwell, *Differential Structure, Tangent Structure, and SDG* (2014); *Differential Equations in a Tangent Category I* (2021)

> [!note]- 🔵 Coalgebra / Behavioral Equivalence / Trace Semantics
> **Prereqs:** Category Theory, Computability
>
> **Note:** Coalgebras for endofunctors = generalized dynamical systems / state machines. Final coalgebras give behavioral equivalence (bisimulation). Central to Spivak/Myers framework where ODEs and Markov processes are coalgebras for polynomial functors.

> [!note]- 🔵 Lenses / Optics / Dialectica Categories
> **Prereqs:** Category Theory, Type Theory
>
> **Note:** Dependent lenses (in Poly) encode bidirectional data flow, version control, and modular updates. δ-lenses + double-pushout rewriting used in davidad's OAA for compositional-causal-model version control. Optics generalize lenses to profunctor/Tambara settings.

> [!note]- 🔵 Simplicial Homotopy Theory (simplicial sets, Kan complexes)
> **Prereqs:** Algebraic Topology, Category Theory
>
> **Note:** The combinatorial foundation for ∞-category theory. Simplicial sets = presheaves on Δ; Kan complexes = ∞-groupoids; quasi-categories (inner-Kan) = ∞-categories.
>
> **Key refs:** Goerss-Jardine, *Simplicial Homotopy Theory*; Friedman, *Elementary illustrated introduction to simplicial sets*

> [!note]- 🔵 Model Categories (Quillen)
> **Prereqs:** Algebraic Topology, Category Theory, Simplicial Homotopy Theory
>
> **Note:** Axiomatize homotopy theory abstractly via weak equivalences, fibrations, cofibrations. The Joyal model structure on sSet gives quasi-categories. Needed before Lurie.
>
> **Key refs:** Hovey, *Model Categories*; Dwyer-Spalinski survey; May-Ponto, *More Concise Algebraic Topology*

> [!note]- 🔵 ∞-Categories / Quasi-Categories (Joyal, Lurie)
> **Prereqs:** Model Categories, Simplicial Homotopy Theory, Category Theory
>
> **Note:** Homotopy-coherent generalization of categories where composition is associative only up to coherent homotopy. Multiple equivalent models: quasi-categories, complete Segal spaces, Segal categories.
>
> **Key refs:** Land, *Introduction to Infinity-Categories*; Cisinski, *Higher Categories and Homotopical Algebra*; Riehl-Verity, *Elements of ∞-Category Theory*

> [!note]- 🔵 ∞-Topoi / Higher Topos Theory (Lurie)
> **Prereqs:** ∞-Categories, Algebraic Topology, Derived/Homological Algebra
>
> **Note:** ∞-categorical generalization of Grothendieck topoi. Conjectured to be the denotational semantics of HoTT (Shulman 2019). Connects to: derived algebraic geometry, condensed mathematics, cohesive ∞-topoi for synthetic differential geometry. Heavy — realistic 2-4 year investment from solid algebra/topology.
>
> **Key refs:** Lurie, *Higher Topos Theory*; Kerodon ([kerodon.net](http://kerodon.net)); Riehl, arXiv:2212.06937

> [!note]- 🔵 ωPAP / Probabilistic-Differentiable Semantics (Huot-Lew-Mansinghka-Staton)
> **Prereqs:** Denotational Semantics / Domain Theory, Measure Theory, Diffeological Spaces, Category Theory
>
> **Note:** Category of ω-cpos enriched in piecewise-analytic-under-analytic-partitions maps. Hosts both probability monads and differentiable structure. davidad's open question: is ωPAP a tangent category? If yes, it would be the unified semantic universe for his meta-ontology.
>
> **Key ref:** arXiv:2302.10636 (LICS 2023)

> [!note]- 🔵 Guaranteed-Safe AI / Open Agency Architecture (davidad, ARIA)
> **Prereqs:** Categorical Systems Theory, Markov Categories, Tangent Categories, Polynomial Functors, Lenses/Optics, HoTT, Temporal Logic Model Checking, Nonlinear Expectations / Infra-Bayesianism
>
> **Note:** CAPSTONE NODE. davidad's framework: world model (compositional, categorical) + safety specification (temporal logic over boundaries) + verifier (probabilistic model checker), with epistemic state given by infra-Bayesian credal sets (PcΔ monad). The mathematical programme is to find a single category that is a tangent category + probability monad + infra-Bayesian, unifying ODEs/SDEs/SPDEs/automata/PGMs.
>
> **Key refs:** Dalrymple et al., *Towards Guaranteed Safe AI* (arXiv:2405.06624); ARIA Safeguarded AI programme

> [!note]- 🔵 Markov Categories / Categorical Probability
> **Prereqs:** Category Theory, Symmetric Monoidal Categories, 🟢 Measure-Theoretic Probability

---

## Foundations and Logic

> [!note]- 🔵 Mathematical Logic
> **Prereqs:** None (root)

> [!note]- 🔵 Model Theory
> **Prereqs:** Mathematical Logic, Abstract Algebra

> [!note]- 🔵 Provability Logic
> **Prereqs:** Mathematical Logic, Computability

> [!note]- 🔵 Fixed Point Theorems (across mathematics) (3,9)
> **Prereqs:** Topology (Brouwer/Kakutani), Mathematical Logic (diagonalization), Category Theory (Lawvere), 🟢 Functional Analysis (Banach/Schauder), Order Theory / Domain Theory (Knaster-Tarski/Kleene)
>
> **References:** Garrabrant & Eisenstat, *Fixed Points* sequence (Alignment Forum, 2018) — ~30 exercises plus agent-foundations applications; Shapiro, *A Fixed-Point Farrago* (Springer Universitext, 2016) — fixed-point theorems across analysis and operator theory (Brouwer, Schauder, Markov-Kakutani, Ryll-Nardzewski) with complete proofs
>
> **Description:** A cross-cutting study of the fixed-point theorems recurring throughout mathematics and agent foundations, organized by the three proof techniques that generate them. (1) **Topological** — Brouwer, Sperner's lemma, Kakutani, Schauder, Lefschetz; existence via continuity + compactness; powers Nash-equilibrium existence and general-equilibrium theory. (2) **Diagonalization** — Cantor, Gödel, Tarski, the recursion theorem, the Y combinator, all unified by Lawvere's fixed-point theorem: in a Cartesian closed category, a point-surjection $A \to B^A$ forces every endomap of $B$ to have a fixed point; powers incompleteness, undecidability, and self-reference. (3) **Iteration / Order** — Banach contraction (metric), Knaster-Tarski and Kleene (lattice / domain); powers Picard-Lindelöf ODE existence, denotational semantics of recursion, and numerical iteration. The deep payoff: incompleteness (no fixed point because a map is "too surjective") and equilibrium existence (fixed point guaranteed by topology) are two faces of the same Lawvere-style argument — the contrapositive of Lawvere gives Cantor/Gödel, the hypothesis gives Brouwer-type existence.
>
> **Connects:** Topology ↔ Game Theory (Kakutani→Nash) ↔ Mathematical Logic (Gödel/Tarski/Lawvere) ↔ Category Theory (CCC) ↔ Domain Theory (Kleene, recursion semantics) ↔ 🟢 Functional Analysis (Banach/Schauder) ↔ 🟢 ODE (Picard)
>
> **Unlocks (agent foundations):** Reflective oracles (Eisenstat's solution to the converse Lawvere problem), the Formal Open Problem in Decision Theory (no continuous fixed-point map on probability distributions — the obstruction to certain reflective agents), program equilibrium and tiling/self-trust, Brouwer-style limit arguments in logical induction

> [!note]- 🔵 Linear Logic
> **Prereqs:** Mathematical Logic, Category Theory

> [!note]- 🔵 Homotopy Type Theory
> **Prereqs:** Type Theory, Category Theory, Algebraic Topology (intuition)

---

## Physics

> [!note]- 🔵 Quantum Mechanics for Mathematicians
> **Prereqs:** 🟢 Functional Analysis, Spectral Theory, Operator Theory, 🟢 Linear Algebra

> [!note]- 🔵 QFT, GR, Gauge Theory
> **Prereqs:** QM for Mathematicians, Special Relativity/EM, Differential Geometry, Lie Groups, Mathematical Gauge Theory, Distribution Theory, 🟢 Functional Analysis

> [!note]- 🔵 AdS/CFT, Standard Model, Emergent Spacetime
> **Prereqs:** QFT/GR/Gauge, Riemannian Geometry, Lie Groups, Conformal Geometry

> [!note]- 🔵 Stochastic Thermodynamics / Nonequilibrium Statmech (4,10)
> **Prereqs:** 🟢 SDEs, Fokker-Planck, 🟢 Information Theory, Martingale Theory

> [!note]- 🔵 Brownian Motor
> **Prereqs:** Stochastic Thermodynamics, 🟢 SDEs, Fokker-Planck

> [!note]- 🔵 Renormalization Group / Statistical Field Theory (4,10)
> **Prereqs:** QFT, 🟢 Functional Analysis, Distribution Theory, Hopf Algebras (Connes-Kreimer)

> [!note]- 🔵 Resource Theory
> **Prereqs:** QM for Mathematicians, 🟢 Information Theory, Symmetric Monoidal Categories

> [!note]- 🔵 Condensed Matter / Nanoscale Physics / Molecular Self-Assembly (1,8)
> **Prereqs:** QM for Mathematicians, 🟢 Linear Algebra, Lie Groups (representation theory)
>
> **Note:** Covers solid-state physics, band theory, topological phases (K-theory), and nanoscale phenomena (NEMS, molecular motors, self-assembly). The nanotech-relevant physics from the subject list

> [!note]- 🔵 Density Functional Theory
> **Prereqs:** QM for Mathematicians, Variational Calculus, 🟢 PDE

> [!note]- 🔵 Plasma Physics / Magnetohydrodynamics / Superconductivity (1,8)
> **Prereqs:** Continuum Mechanics, 🟢 PDE, Condensed Matter, Special Relativity/EM

---

## Computation

> [!note]- 🔵 Computability (4,8)
> **Prereqs:** Mathematical Logic

> [!note]- 🔵 Computational Complexity (3,8)
> **Prereqs:** Computability, Combinatorial Optimization

> [!note]- 🔵 Combinatorial Optimization / Algorithm Design (5,10)
> **Prereqs:** None (root)

> [!note]- 🔵 Programming Language Theory / Type Theory / Domain Theory (3,10)
> **Prereqs:** Mathematical Logic, Category Theory, Computability

> [!note]- 🔵 Formal Concurrency Theory / π-calculus / Session Types (3,10)
> **Prereqs:** Programming Language Theory, Mathematical Logic

> [!note]- 🔵 Temporal Logic Model Checking / Bisimulation / Process Algebra (3,10)
> **Prereqs:** Mathematical Logic, Computability, Programming Language Theory

> [!note]- 🔵 Denotational Semantics / Monadic Computation / Lambda Calculus (2,8)
> **Prereqs:** Type Theory, Category Theory

> [!note]- 🔵 Distributed Systems Theory / Impossibility Results (FLP, CAP) (4,10)
> **Prereqs:** Algorithm Design, Mathematical Logic, 🟢 Game Theory (useful)

> [!note]- 🔵 AIT, AIXI, Reflective Oracles (6,10)
> **Prereqs:** Computability, 🟢 Information Theory, 🟢 Measure-Theoretic Probability, Mathematical Logic

> [!note]- 🔵 Computable Analysis (2,6)
> **Prereqs:** Computability, Multivariate Analysis, Topology

> [!note]- 🔵 Arithmetic Hierarchy (2,5)
> **Prereqs:** Computability, Mathematical Logic

> [!note]- 🔵 Abstract Rewriting Systems (3,8)
> **Prereqs:** Mathematical Logic, Type Theory

> [!note]- ⭐🔵 Communication Complexity (2,9)
> **Prereqs:** Computational Complexity, 🟢 Information Theory, Combinatorial Optimization
>
> **Gaps:** Know definition of Yao's model, never studied techniques (rectangle bounds, discrepancy, information complexity)
>
> **Note:** Natural extension of IT strength — communication lower bounds ARE entropy bounds. Used in mechanism design impossibilities, data structure lower bounds, and streaming.
>
> **Unlocks:** Lower bounds for dynamic algorithms, mechanism design communication bounds, streaming lower bounds

> [!note]- 🔵 Approximation Algorithms (3,8)
> **Prereqs:** Computational Complexity, Combinatorial Optimization, Convex Optimization
>
> **Gaps:** Know LP relaxation idea, never studied SDP hierarchies or primal-dual method formally
>
> **Note:** Connects PCP theorem (hardness of approximation) to algorithm design. SOS/Lasserre hierarchy bridges convex optimization, real algebraic geometry, and proof complexity.
>
> **Unlocks:** Hardness of approximation, SDP methods, mechanism design approximation ratios

> [!note]- 🔵 Algorithmic Statistics (3,9)
> **Prereqs:** AIT/AIXI, 🟢 Information Theory, Computational Complexity, Theoretical Statistics
>
> **Gaps:** Know structure function definition, haven't studied the full Vereshchagin-Vitányi / Gács-Tromp-Vitányi theory
>
> **Note:** The AIT formalization of model selection and sufficient statistics. Bridges Kolmogorov complexity and statistical learning theory. Directly relevant to ontology identification and meta-learning projects.
>
> **Unlocks:** Kolmogorov structure function, algorithmic sufficient statistics, MDL theory, connections to SLT

---

## Engineering

> [!note]- 🟢 Control Theory (7,10) — ANCHOR
> **Prereqs:** 🟢 Linear Algebra, Multivariate Analysis, Dynamical Systems, 🟢 SDEs (for stochastic), Convex Optimization
>
> **Status:** Known

> [!note]- 🔵 Optimal Filtering / State Estimation (Kalman, Wonham, particle) (7,10)
> **Prereqs:** 🟢 Control Theory, 🟢 SDEs, 🟢 Linear Algebra

> [!note]- 🔵 Path Integrals for Filtering and Control
> **Prereqs:** 🟢 Control Theory, 🟢 SDEs, Stochastic Analysis, 🟢 PDE (HJB, Fokker-Planck), Optimal Filtering / State Estimation, 🟢 Information Theory (for the KL / control-as-inference view); Feynman-Kac and Girsanov are the workhorses
>
> **Connects:** Stochastic Optimal Control (HJB) ↔ Nonlinear Filtering (Zakai / Kallianpur-Striebel) ↔ Feynman-Kac / Path Integrals ↔ Large Deviations (Onsager-Machlup) ↔ Schrödinger Bridges / Entropic OT ↔ Reinforcement Learning (control as inference)
>
> **Note:** Both estimation and control become path integrals once you take a logarithmic transform, and that shared structure is the point. (1) **Filtering.** The unnormalized conditional density of a partially observed diffusion solves the linear Zakai equation, and the Kallianpur-Striebel formula writes the filter as a ratio of Feynman-Kac path integrals — the conditional expectation is an average over trajectories reweighted by the observation likelihood (Girsanov). (2) **Control.** For the "path-integral control" class — control-affine dynamics with quadratic control cost, noise entering through the control channel — the Cole-Hopf / exponential transform $V = -\lambda \log \Psi$ linearizes the nonlinear Hamilton-Jacobi-Bellman equation into a linear backward (Feynman-Kac) PDE, so the optimal cost-to-go is a path integral over *uncontrolled* trajectories weighted by $e^{-\text{cost}/\lambda}$, evaluable by Monte Carlo without ever solving HJB on a grid. The two halves are dual: the same log-transform that turns HJB into a linear equation is the Fleming-Mitter link between nonlinear filtering and stochastic control, and the exponential weight is a change of measure (KL control), which is exactly why optimal control can be recast as Bayesian inference ("control as inference") and connects to Schrödinger bridges and entropic optimal transport. The free linear-Gaussian case collapses to Kalman filtering and LQR, whose classical estimation-control duality is the shadow of this one.
>
> **Unlocks:** Sampling-based optimal control — Path Integral Policy Improvement (PI², Theodorou-Buchli-Schaal) and Model Predictive Path Integral control (MPPI, Williams et al.), now standard in robotics and autonomous driving — linearly-solvable MDPs / KL control (Todorov), control-as-inference reinforcement learning, particle-filter smoothing, and the diffusion-model / stochastic-control bridge. The concrete computation and robotics payoff sitting on your control background.
>
> **Key refs:** Kappen, *Path Integrals and Symmetry Breaking for Optimal Control Theory* (J. Stat. Mech., 2005, P11011) and *Linear Theory for Control of Nonlinear Stochastic Systems* (Phys. Rev. Lett. 95, 200201, 2005) — the founding path-integral-control papers; Theodorou-Buchli-Schaal, *A Generalized Path Integral Control Approach to Reinforcement Learning* (JMLR 11, 2010) for PI²; Todorov, *Efficient Computation of Optimal Actions* (PNAS 106, 2009) for linearly-solvable MDPs; Fleming-Mitter for the filtering-control duality; Bain-Crisan, *Fundamentals of Stochastic Filtering* (Springer, 2009) for the Zakai / Kallianpur-Striebel path-integral side. Member of Cluster 9 and Cluster 18.

> [!note]- 🔵 Finite Element Exterior Calculus (Arnold-Falk-Winther)
> **Prereqs:** 🟢 Functional Analysis, 🟢 PDE, Variational Calculus, De Rham Cohomology, Differential Geometry (differential forms), Hodge Theory, Algebraic Topology (cochains / simplicial cohomology), Homological Algebra (cochain complexes); the engineering applications draw on Special Relativity / Classical Electrodynamics (Maxwell)
>
> **Connects:** Hodge Theory / de Rham Complex ↔ Homological Algebra (cochain complexes) ↔ Functional Analysis (Hilbert complexes) ↔ Algebraic Topology (Whitney forms = simplicial cochains) ↔ Numerical Analysis / Approximation Theory ↔ Computational Electromagnetics / Elasticity
>
> **Note:** Structure-preserving discretization, where the slogan is that *stability is a cohomological condition*. Many PDEs (Maxwell, Darcy / mixed Poisson, elasticity) are cleanest as statements about the de Rham complex $0 \to \Lambda^0 \xrightarrow{d} \Lambda^1 \xrightarrow{d} \cdots \xrightarrow{d} \Lambda^n \to 0$ and its Hodge Laplacian $\Delta = d\delta + \delta d$. FEEC builds finite-element subcomplexes of the $L^2$ de Rham complex — the polynomial form spaces $\mathcal{P}_r\Lambda^k$ and the trimmed $\mathcal{P}_r^-\Lambda^k$ on simplices, whose lowest-order cases are exactly the Whitney forms (Nédélec edge and Raviart-Thomas face elements) — together with a bounded cochain projection (a commuting interpolant). Because that projection is a cochain map, the discrete complex has the *same cohomology* as the continuous one, so the discrete Hodge decomposition and discrete Poincaré inequality hold, and stability and convergence of the mixed method follow from them. The abstract engine is the theory of Hilbert complexes (closed densely-defined operators forming a complex), in which well-posedness of the Hodge Laplacian is the closed-range theorem. This is the de Rham / Hodge story you like made discrete: the cohomology of the domain is preserved exactly at the matrix level, so local element-level constructions control a global topological invariant.
>
> **Unlocks:** Spurious-mode-free computational electromagnetics (the Maxwell eigenproblem is stable precisely because the discrete de Rham sequence is exact — Bossavit's Whitney forms, Hiptmair), stable mixed methods for Darcy / Stokes, the elasticity complex via the Bernstein-Gelfand-Gelfand (BGG) resolution (deriving elasticity elements from the de Rham complex), discrete exterior calculus / mimetic and compatible discretizations, and the finite-element periodic table. The concrete engineering payoff where the differential-geometry and de Rham study cashes out.
>
> **Key refs:** Arnold-Falk-Winther, *Finite Element Exterior Calculus, Homological Techniques, and Applications* (Acta Numerica 15, 2006, 1-155) — the foundational paper; Arnold-Falk-Winther, *Finite Element Exterior Calculus: From Hodge Theory to Numerical Stability* (Bull. Amer. Math. Soc. 47, 2010, 281-354) — the readable synthesis; Arnold, *Finite Element Exterior Calculus* (SIAM, CBMS-NSF Regional Conference Series 93, 2018) — the book. Member of Cluster 18; tightly coupled to the Computational EM via DEC node.

> [!note]- 🔵 Green's Functions
> **Prereqs:** 🟢 PDE, Distribution Theory, Harmonic Analysis

> [!note]- 🔵 Continuum Mechanics / Theoretical Fluid Dynamics (5,8)
> **Prereqs:** 🟢 PDE, Tensor Calculus, Differential Geometry, Variational Calculus

> [!note]- 🔵 Geometric Mechanics in Robotics (SE(3), Screw Theory)
> **Prereqs:** Lie Groups, Differential Geometry, Symplectic Geometry, 🟢 Control Theory

> [!note]- 🔵 Convex Optimization / High-Dim Optimization (5,9)
> **Prereqs:** 🟢 Linear Algebra, Multivariate Analysis, 🟢 Functional Analysis (basic)

> [!note]- 🔵 Dimensionality Reduction / Compressed Sensing (6,6)
> **Prereqs:** 🟢 Linear Algebra, High-Dimensional Probability, Convex Optimization

> [!note]- 🔵 Perturbation Theory / Integral Transforms (4,9)
> **Prereqs:** 🟢 PDE, Complex Analysis, 🟢 Functional Analysis

> [!note]- 🔵 Linear Systems Theory / Circuit Theory / Signal Processing (2,6)
> **Prereqs:** 🟢 Linear Algebra, Multivariate Analysis, Complex Analysis, Harmonic Analysis

> [!note]- 🔵 Electrical Circuit Theory
> **Prereqs:** 🟢 Linear Algebra, 🟢 ODEs (RLC dynamics), Complex Analysis (impedance / frequency domain), Graph Theory (basic)
>
> **Connects:** Algebraic Graph Theory (incidence matrix / Laplacian) ↔ Discrete Exterior Calculus ↔ Electrical Networks / Random Walks (effective resistance, matrix-tree) ↔ Linear Systems Theory ↔ Convex Optimization (passivity)
>
> **Note:** The structural theory beneath circuit analysis, which is secretly algebraic topology on a graph. Kirchhoff's current law says the vector of branch currents lies in the kernel of the incidence (boundary) operator of the circuit graph — the cycle space — while Kirchhoff's voltage law puts branch voltages in its image, the cut space; the two are orthogonal complements, and Tellegen's theorem is exactly that orthogonality, a discrete conservation-of-power statement independent of the circuit elements. Constitutive relations (Ohm's law and the $i$-$v$ laws of capacitors and inductors) close the system, giving RLC dynamics solved in the frequency domain via impedance $Z(s)$ and the Laplace transform. The deeper bridges: the weighted graph Laplacian governs resistor networks, effective resistance is a genuine metric, and the matrix-tree theorem ties spanning-tree counts to Laplacian determinants — the same object that appears in the GFF / loop-soup node, so a resistor network and a Gaussian free field are two readings of one Laplacian. Network synthesis (Foster, Cauer, Brune) and passivity round it out. Member of Cluster 18; bridges to the electrical-networks strand of the GFF node.

> [!note]- 🔵 Trajectory Optimization (4,9)
> **Prereqs:** 🟢 PDE, Differential Geometry (basic), 🟢 Control Theory, Convex Optimization, Perturbation Theory
>
> **Note:** The "clean mathematical frameworks for aerospace" entry from the subject list. Core topics: Keplerian orbits, Lambert's problem, low-thrust trajectory optimization, restricted three-body problem (CR3BP), invariant manifolds, optimal control on Lie groups

> [!note]- 🔵 Flight Dynamics
> **Prereqs:** 🟢 ODEs, 🟢 Control Theory, Dynamical Systems, 🟢 Linear Algebra, Multivariate Analysis; the aerodynamic forces draw on Continuum Mechanics / Fluid Dynamics, and the geometric attitude formulation on Lie Groups / Geometric Mechanics
>
> **Connects:** Rigid-Body Dynamics ($SE(3)$) ↔ Control Theory (stability & autopilots) ↔ Dynamical Systems (flight modes / eigenvalue analysis) ↔ Fluid Dynamics (aerodynamic forces) ↔ Trajectory Optimization
>
> **Note:** The rigid-body dynamics of an aircraft under aerodynamic, gravitational, and propulsive forces. The six-degree-of-freedom equations of motion live on $SE(3)$ — position together with attitude on $SO(3)$ — and linearizing about a trim condition decouples them into longitudinal and lateral-directional dynamics whose eigenvalues are the classical flight modes: the phugoid (slow energy exchange between speed and altitude), the short-period pitch oscillation, the Dutch roll, the spiral mode, and roll subsidence. Stability and control derivatives package the aerodynamic force-and-moment dependence on the state, so stability analysis becomes an eigenvalue problem on the linearized system and autopilot / flight-control design is control theory applied to it. The subject is the meeting point of aerodynamics (forces from fluid dynamics), geometric rigid-body mechanics (attitude on $SO(3)$, the same $SE(3)$ kinematics as the robotics node), and control. Member of Cluster 4.

> [!note]- 🔵 Networked Control Systems / Control under Data-Rate Constraints
> **Prereqs:** 🟢 Control Theory, 🟢 Information Theory, Dynamical Systems, 🟢 Measure-Theoretic Probability (stochastic versions)
>
> **Connects:** Control Theory ↔ Information Theory ↔ Quantization / Source Coding ↔ Large Deviations ↔ Decentralized Control / Team Theory
>
> **Note:** The information-theoretic core of networked control. The central result is the data-rate theorem (Nair-Evans; Tatikonda-Mitter): a linear system $\dot x = Ax + Bu$ can be stabilized over a finite-rate feedback channel if and only if the channel rate exceeds $\sum_i \max(0, \log|\lambda_i(A)|)$, the sum of the logarithms of the unstable eigenvalues. Instability is therefore an information-production rate (bits per unit time), and feedback must export entropy at least as fast as the open-loop dynamics generate it — the control-theoretic twin of the second law's entropy-export picture, and a clean "true name" for what stabilization costs. Surrounding theory: quantized and event-triggered feedback, the anytime-capacity reformulation (Sahai-Mitter) that identifies which noisy channels suffice, and the role of the topological entropy of the dynamics. Searchable under "networked control systems" and "feedback control under data rate constraints" (the Nair-Fagnani-Zampieri-Evans survey). Member of Cluster 18; the entropy-export analogy ties it to Cluster 11 and the decentralized-control circle.

> [!note]- 🔵 Geometric Control Theory / Sub-Riemannian Geometry
> **Prereqs:** 🟢 Control Theory, Differential Geometry, Lie Groups / Lie Algebras, Multivariate Analysis
>
> **Connects:** Control Theory ↔ Differential Geometry ↔ Lie Groups ↔ Symplectic Geometry (Pontryagin / Hamiltonian) ↔ Sub-Riemannian Geometry
>
> **Note:** Controllability and feedback recast in differential-geometric language. The organizing theorem is Chow-Rashevskii: a driftless system $\dot x = \sum_i u_i f_i(x)$ is controllable iff the Lie algebra generated by the control vector fields $\{f_i\}$ under bracketing spans the tangent space at each point — so a car parallel-parks (moves in a direction that is not a control input) precisely because the sideways direction is an iterated Lie bracket of "drive" and "steer." Nonholonomic constraints define a distribution; the sub-Riemannian distance measures the shortest admissible path, and its geodesics solve a Pontryagin / Hamiltonian system on $T^*M$ (the bridge to Symplectic Geometry). Also: feedback linearization (when is a nonlinear system diffeomorphic to a linear one?), controllability of systems on Lie groups via the exponential map, and Carnot groups as the local models. The "falling cat" and "rolling sphere" are the canonical examples. Member of Cluster 4.

> [!note]- 🔵 System Identification
> **Prereqs:** 🟢 Control Theory, Theoretical Statistics, 🟢 Linear Algebra, Dynamical Systems, 🟢 Information Theory (for the model-selection / MDL view)
>
> **Connects:** Control Theory ↔ Theoretical Statistics ↔ Statistical Learning ↔ Information Theory (MDL) ↔ Optimal Filtering
>
> **Note:** The engineering science of inferring a dynamical model — its order, parameters, and state-space coordinates — from input-output data. Methods: the prediction-error method, maximum likelihood, and subspace identification, which recovers a state-space realization from the geometry of Hankel matrices via the singular value decomposition. The load-bearing notions are persistency of excitation (the input must be rich enough to reveal the dynamics) and identifiability — when the latent realization is recoverable, and only up to which group of transformations (similarity transforms of the state). The data fix the input-output map, not the coordinates, so a realization is pinned down only up to state-space similarity. Member of Cluster 18; strong tie to Cluster 20.

> [!note]- 🔵 Robust Control and H∞
> **Prereqs:** 🟢 Control Theory, 🟢 Functional Analysis (Hardy spaces), Complex Analysis, Convex Optimization
>
> **Connects:** Control Theory ↔ Functional Analysis (Hardy space $H^\infty$) ↔ Complex Analysis ↔ Convex Optimization (LMIs) ↔ Operator Theory
>
> **Note:** Control design certified against model uncertainty, with a genuinely beautiful functional-analytic core. The performance objective is the $H^\infty$ norm of the closed-loop transfer function — the supremum over frequency of the largest singular value, equivalently the operator norm on the Hardy space $H^\infty$ of the right half-plane — so "minimize the worst-case gain" becomes a Nevanlinna-Pick / model-matching problem in complex analysis and operator theory. The small-gain theorem gives robust stability, $\mu$-synthesis handles structured uncertainty, and modern solutions are computed as linear matrix inequalities. Member of Cluster 18; pairs with the LMI node and bridges to Operator Theory / Functional Analysis.

> [!note]- 🔵 Linear Matrix Inequalities
> **Prereqs:** Convex Optimization (semidefinite programming), 🟢 Linear Algebra, 🟢 Control Theory (for the applications)
>
> **Connects:** Convex Optimization (semidefinite programming) ↔ Control Theory (Lyapunov / Riccati) ↔ Robust Control / H∞ ↔ Real Algebraic Geometry (sum-of-squares) ↔ Operator Theory
>
> **Note:** A unifying computational frame in which a remarkable range of control and optimization problems become the single convex feasibility problem "find $X$ with $F(X) = F_0 + \sum_i x_i F_i \succeq 0$." Lyapunov stability ($A^\top P + PA \prec 0$), the bounded-real lemma behind $H^\infty$ control, optimal experiment design, and relaxations of combinatorial problems all reduce to LMIs, solved efficiently by interior-point methods as semidefinite programs. The deeper thread runs to the sum-of-squares / Lasserre hierarchy — the bridge to real algebraic geometry and to the Approximation Algorithms node — where positivity certificates become LMIs. Member of Cluster 18; pairs with Robust Control and Convex Optimization.

> [!note]- 🔵 Detection and Estimation Theory (Statistical Signal Processing)
> **Prereqs:** 🟢 Measure-Theoretic Probability, 🟢 Information Theory, Theoretical Statistics, 🟢 Linear Algebra
>
> **Connects:** Information Theory ↔ Information Geometry (Cramér-Rao = Fisher) ↔ Theoretical Statistics (Neyman-Pearson) ↔ Large Deviations (error exponents) ↔ Optimal Filtering
>
> **Note:** The probabilistic backbone of signal processing, and a concrete home for several quantities used abstractly elsewhere. Estimation: the Cramér-Rao bound $\mathrm{Var}(\hat\theta) \geq I(\theta)^{-1}$ is the Fisher-information metric appearing as an estimation limit, with minimum-variance-unbiased, maximum-likelihood, and MMSE / conditional-mean estimators as the constructions, and the matched filter as the optimal linear detector. Detection: Neyman-Pearson and the likelihood-ratio test, Bayesian risk, and sequential detection (Wald's SPRT), where the error exponents that quantify performance are Kullback-Leibler divergences and Chernoff information — so the subject is information geometry and large deviations wearing an engineering hat. Member of Cluster 18; ties to Cluster 20 (the classical-statistics layer beneath statistical learning) and to Information Geometry.

> [!note]- 🔵 Computational Electromagnetics via Discrete Exterior Calculus
> **Prereqs:** Differential Geometry, De Rham Cohomology, 🟢 PDE, Finite Element Exterior Calculus, Special Relativity / Classical Electrodynamics (for the Maxwell formulation)
>
> **Connects:** Differential Geometry (differential forms) ↔ De Rham Cohomology ↔ Finite Element Methods ↔ Algebraic Topology (cochains) ↔ Electromagnetism
>
> **Note:** Maxwell's equations discretized so as to preserve their geometric structure. Continuum Maxwell is cleanest as $dF = 0$ and $d\star F = J$ with $F$ the electromagnetic 2-form; the content here is that the right discretization keeps fields as cochains on a mesh, the exterior derivative $d$ as the metric-independent coboundary operator, and the Hodge star $\star$ as the only place the metric and material data enter. Yee's classic finite-difference time-domain scheme is, read correctly, a discrete Hodge star on a primal-dual mesh pair, and finite element exterior calculus (Arnold-Falk-Winther) makes precise which finite-element spaces (Whitney forms / edge and face elements) reproduce the de Rham cohomology and so avoid spurious modes. This is where the differential-geometry and de-Rham study pays off on a concrete engineering problem. Member of Cluster 18.

---

## Statistics

> [!note]- 🔵 Theoretical Statistics (4,8)
> **Prereqs:** 🟢 Measure-Theoretic Probability, 🟢 Functional Analysis (basic)

> [!note]- 🔵 Bayesian Statistics / Variational Inference (4,8)
> **Prereqs:** Theoretical Statistics, 🟢 Information Theory, Convex Optimization
>
> **Reference:** Jaynes, *Probability Theory: The Logic of Science* (Cambridge University Press, 2003) — the foundational case for Bayesian probability as extended logic (Cox's theorem, the maximum-entropy principle)

> [!note]- 🔵 Probabilistic Graphical Models / Message Passing (4,8)
> **Prereqs:** Bayesian Statistics, 🟢 Information Theory

> [!note]- 🔵 Algebraic Statistics (1,7)
> **Prereqs:** Theoretical Statistics, Algebraic Geometry, Commutative Algebra

> [!note]- 🔵 Singular Learning Theory (3,7)
> **Prereqs:** Theoretical Statistics, Algebraic Geometry, Singularity Theory, Bayesian Statistics

> [!note]- 🔵 Statistical Physics of Inference
> **Prereqs:** Statistical Mechanics / Stochastic Thermodynamics, 🟢 Information Theory, Bayesian Statistics, 🟢 Measure-Theoretic Probability, High-Dimensional Probability; the algorithmic side uses Probabilistic Graphical Models / Message Passing, and the sharpest results use Random Matrix Theory and Spin-Glass Theory (replica / cavity)
>
> **Connects:** Statistical Mechanics (disordered systems / spin glasses) ↔ Information Theory ↔ Bayesian Inference ↔ High-Dimensional Probability / Random Matrix Theory ↔ Message Passing (AMP / belief propagation) ↔ Computational Complexity (hard phases)
>
> **Note:** The statistical mechanics of high-dimensional inference: treat the posterior as a Boltzmann-Gibbs measure $P(x \mid y) \propto e^{-\beta H(x;y)}$ and compute the *typical-case* behavior of large random instances with the tools of disordered systems. The organizing object is the quenched free entropy $\Phi = \tfrac{1}{n}\mathbb{E}\log Z$, computed by the replica and cavity methods from spin-glass theory; its non-analyticities are phase transitions that locate the fundamental limits of inference. The signature payoff is a precise map of thresholds: an information-theoretic (statistical) threshold below which recovery is impossible at any cost, and an algorithmic threshold below which efficient algorithms fail — the gap between them is the conjectured "hard phase," a statistical-physics window on average-case computational hardness. The associated algorithms are message passing: belief propagation and approximate message passing (AMP), whose dynamics are tracked exactly by the state-evolution / cavity equations, with the TAP free energy as the variational backbone. This is information theory, Bayesian inference, and the second law meeting on one partition function — where the planted spin glass, the Nishimori line, and the replica-symmetry-breaking hierarchy become inference statements.
>
> **Unlocks:** Sharp thresholds for compressed sensing / sparse regression, low-rank matrix and tensor estimation (the BBP / spectral transition and AMP-optimal recovery), community detection in the stochastic block model (the Kesten-Stigum / detectability threshold), error-correcting codes (LDPC decoding as belief propagation), planted constraint satisfaction and the satisfiability thresholds, and learning curves / generalization of neural networks (the replica calculation of perceptron capacity). Ties directly to your Singular Learning Theory and Posterior Contraction nodes.
>
> **Key refs:** Mézard-Montanari, *Information, Physics, and Computation* (Oxford, 2009) — the canonical text uniting the three; Zdeborová-Krzakala, *Statistical Physics of Inference: Thresholds and Algorithms* (Advances in Physics 65, 453-552, 2016) — the definitive modern review (replica / cavity, message passing, phase transitions, applications); Nishimori, *Statistical Physics of Spin Glasses and Information Processing* (Oxford, 2001); Engel-Van den Broeck, *Statistical Mechanics of Learning* (Cambridge, 2001) for the learning-curve side. Member of Cluster 20 and Cluster 11.

> [!note]- 🔵 Entropic Inference (2,9)
> **Prereqs:** 🟢 Information Theory, 🟢 Measure-Theoretic Probability, Bayesian Statistics
>
> **Reference:** Caticha, *Entropic Inference and the Foundations of Physics* (2012)
>
> **Description:** Derives probability theory and statistical inference from information-theoretic first principles. The central result: Bayes' rule and the method of maximum entropy are not separate principles — Bayes' rule is a special case of maximizing relative entropy subject to data constraints, and ME is the unique update rule consistent with subset independence, coordinate invariance, and consistency under marginalization. This makes KL divergence the fundamental quantity, not probability itself. Equilibrium statistical physics follows as a direct application (Boltzmann = MaxEnt with energy constraint, temperature = Lagrange multiplier). The framework also derives information geometry from first principles: Fisher information emerges as the unique Riemannian metric compatible with the ME update rule. Operationally: translate prior knowledge into constraints on distributions, apply ME, and the result is the unique inference consistent with what you know and nothing more.
>
> **Connects:** Information Theory ↔ Bayesian Statistics ↔ Information Geometry ↔ Statistical Physics ↔ Large Deviations

> [!note]- ⭐🔵 Posterior Contraction Theory (2,9)
> **Prereqs:** Theoretical Statistics, Bayesian Statistics, Measure Theory, 🟢 Information Theory, 🟢 Functional Analysis
>
> **Gaps:** Know Doob's consistency theorem, never studied Ghosal-Ghosh-van der Vaart framework or metric entropy conditions
>
> **Note:** The purely Bayesian analogue of PAC learning. Posterior contracts at rate $\varepsilon_n$ iff prior mass in KL-balls $\geq e^{-n\varepsilon_n^2}$ and model has controlled metric entropy. Connects to information geometry (KL neighborhoods), optimal transport (Wasserstein contraction of posteriors), algorithmic statistics (AIT version of model selection), and SLT (contraction near singularities = RLCT). PAC-Bayes bounds are the bridge to frequentist learning theory.
>
> **Unlocks:** Bayesian nonparametric rates, PAC-Bayes theory, GP posterior contraction, connections to SLT and algorithmic statistics

---

## Mechanism Design / Game Theory

> [!note]- 🟢 Game Theory / Compositional Game Theory (8,10) — ANCHOR
> **Prereqs:** 🟢 Linear Algebra, Convex Optimization, 🟢 Probability; Compositional layer requires Category Theory, SMC
>
> **Status:** Known

> [!note]- 🟢 Mechanism Design (8,10) — ANCHOR
> **Prereqs:** 🟢 Game Theory, Convex Optimization
>
> **Status:** Known

> [!note]- 🔵 Forecast Elicitation and Aggregation (3,9)
> **Prereqs:** 🟢 Mechanism Design, Bayesian Statistics, 🟢 Information Theory

> [!note]- 🔵 Complete Class / Coherence Theorems / Harsanyi (4,8)
> **Prereqs:** Theoretical Statistics, 🟢 Game Theory, Bayesian Statistics, 🟢 Measure-Theoretic Probability

> [!note]- 🔵 Byzantine Fault Tolerance / Consensus Protocol Theory (5,10)
> **Prereqs:** Distributed Systems Theory, 🟢 Game Theory, 🟢 Mechanism Design

> [!note]- 🔵 Game-Theoretic Foundations for Probability (Vovk) (1,8)
> **Prereqs:** 🟢 Game Theory, Martingale Theory, Mathematical Logic

> [!note]- 🔵 Nonlinear Expectations (Peng) / Coherent Risk / Choquet (1,8)
> **Prereqs:** 🟢 Measure-Theoretic Probability, 🟢 Functional Analysis, Convex Optimization, 🟢 SDEs

---

## Niche Connecting Fields

> [!note]- 🔵 Regularity Structures (Hairer)
> **Prereqs:** Rough Paths, Hopf Algebras, Distribution Theory, Stochastic Analysis, 🟢 Functional Analysis, Renormalization Group (intuition)
>
> **Connects:** Stochastic Analysis ↔ QFT Renormalization ↔ Hopf Algebras ↔ PDE

> [!note]- 🔵 Stochastic Field Theory
> **Prereqs:** Stochastic Analysis, 🟢 SDEs, Renormalization Group / Statistical Field Theory, Distribution Theory, 🟢 Functional Analysis, 🟢 PDE; the rigorous singular-SPDE core needs Regularity Structures / Rough Paths, and the perturbative side needs QFT (Feynman diagrams)
>
> **Connects:** SPDEs / Langevin Dynamics ↔ Statistical Field Theory / QFT (path integrals, RG) ↔ Renormalization ↔ Regularity Structures (rigorous solutions) ↔ Gaussian Free Field (free theory) ↔ Dynamical Critical Phenomena / KPZ
>
> **Note:** The field theory of noisy and dynamical fields — what a stochastic PDE becomes when rewritten as a path integral. Two canonical routes in. (1) **Response-field / MSR formalism** (Martin-Siggia-Rose, Janssen-De Dominicis): a Langevin equation $\partial_t \phi = F[\phi] + \xi$ with Gaussian noise $\xi$ becomes, after averaging over the noise, a path integral over the field $\phi$ and an auxiliary response field $\tilde\phi$ with action $S[\phi,\tilde\phi] = \int \tilde\phi\,(\partial_t\phi - F[\phi]) - \tfrac{1}{2}\,\tilde\phi\, D\, \tilde\phi$. Stochastic dynamics is now a field theory: correlation and response functions come from Feynman diagrams, and the dynamical renormalization group gives the scaling exponents of dynamical critical phenomena (Hohenberg-Halperin models A-J), KPZ growth, reaction-diffusion / directed percolation, and active matter. (2) **Stochastic quantization** (Parisi-Wu): a Euclidean QFT with action $S$ is recovered as the stationary distribution of the Langevin flow $\partial_t \phi = -\delta S/\delta\phi + \xi$ in one extra fictitious time — so sampling an SPDE *is* constructing a field theory, the viewpoint underneath Hairer's dynamical $\Phi^4$ program. For gauge fields this becomes the gauge-covariant Langevin dynamics of the Yang-Mills measure on the space of connections modulo gauge, constructed rigorously via regularity structures (Chandra-Chevyrev-Hairer-Shen, *Langevin Dynamic for the 2D Yang-Mills Measure*, 2022, and *Stochastic Quantisation of Yang-Mills-Higgs in 3D*, Invent. Math., 2024; Chevyrev, *Stochastic Quantization of Yang-Mills*, J. Math. Phys. 63, 091101, 2022), Parisi-Wu's original motivation being to quantize gauge fields without gauge fixing. The free (linear, Gaussian) theory is a Gaussian field, with the GFF as the stationary measure of the linear Langevin dynamics — so this node sits on the GFF at zeroth order, just as Information Field Theory does, except that here the randomness is the system's own dynamics rather than measurement noise. The rigorous continuum limit of the nonlinear, singular cases is exactly the Regularity Structures / paracontrolled node.
>
> **Unlocks:** Dynamical RG and the classification of dynamic universality classes, KPZ universality, the field-theoretic ($\epsilon$-expansion) computation of nonequilibrium critical exponents, constructive QFT via stochastic quantization, Doi-Peliti field theory for reaction networks, and complex / lattice Langevin sampling as a computational route to field-theory expectations (the sign-problem workaround).
>
> **Key refs:** Täuber, *Critical Dynamics: A Field Theory Approach to Equilibrium and Non-Equilibrium Scaling Behavior* (Cambridge, 2014) — the standard text on the MSR / response-field field theory and dynamical RG; Martin-Siggia-Rose, *Statistical Dynamics of Classical Systems* (Phys. Rev. A 8, 423, 1973) and Janssen / De Dominicis for the founding response-field formalism; Hohenberg-Halperin, *Theory of Dynamic Critical Phenomena* (Rev. Mod. Phys. 49, 435, 1977); Parisi-Wu (1981) for stochastic quantization; Hairer, *A Theory of Regularity Structures* (Invent. Math. 198, 2014) for the rigorous SPDE side.
>
> **Member of Cluster 2 (Stochastic Algebra / Renormalization).**

> [!note]- 🔵 Microlocal Analysis / Semiclassical Analysis / Sheaf Quantization
> **Prereqs:** Distribution Theory, 🟢 Functional Analysis, Symplectic Geometry, 🟢 PDE, Harmonic Analysis, Spectral Theory; the sheaf-theoretic track additionally needs Sheaf Theory / Derived Category basics (via Algebraic Geometry)
>
> **Connects:** Symplectic Geometry ↔ PDE ↔ Spectral Theory ↔ Quantum Mechanics (semiclassical limit) ↔ Algebraic Topology ↔ Persistent Homology ↔ Inverse Problems
>
> **Note:** Phase-space localization of analysis. Organizing principle: the singularities and oscillations of a solution are tracked not just by where they sit on $M$ but by their codirection (frequency) in the cotangent bundle $T^*M$, whose canonical symplectic form is the natural arena. Two complementary flavors are worth holding together. Member of Cluster 5; the inverse-problems applications also tie it to Cluster 18.
>
> **Description:** (1) **Analytic / semiclassical** (Hörmander, Melrose, Zworski). Pseudodifferential operators ($\Psi$DOs) quantize symbols $a(x,\xi)$ on $T^*M$; Fourier integral operators quantize symplectomorphisms via their canonical relations (Lagrangian submanifolds of $T^*M \times T^*M$). The wavefront set $\mathrm{WF}(u) \subset T^*M \setminus 0$ refines singular support, and the central dynamical statement — propagation of singularities — says $\mathrm{WF}(u)$ is invariant under the Hamiltonian flow of the principal symbol. Egorov's theorem makes "quantize, evolve, dequantize = evolve classically, then quantize" precise to leading order, which is exactly the quantum-classical correspondence. The semiclassical $\hbar \to 0$ limit yields the Weyl law for spectral asymptotics and underpins quantum chaos. (2) **Sheaf-theoretic / microlocal sheaf theory** (Kashiwara-Schapira, Tamarkin). The microsupport $SS(F) \subset T^*M$ of a complex of sheaves is the cotangent locus where it fails to propagate — the categorified shadow of the wavefront set — now a tool in symplectic topology (Tamarkin non-displaceability, Nadler-Zaslow) and persistent homology.
>
> **Unlocks / applications:** Inverse problems and tomography — recovering coefficients from boundary data is governed by the FIO structure of the geodesic X-ray transform, with boundary rigidity and seismic imaging as the engineering payoff. Also: rigorous WKB / stationary phase, scattering theory and resonances, the analytic core of the Atiyah-Singer index theorem (reduce the index to a symbol on $T^*M$), and microlocal methods in symplectic topology.
>
> **Scores:** (familiarity, interest) to be assigned in the Google Doc — flagged as a high-interest analysis ↔ symplectic ↔ physics hub from the "diversity through specializing" discussion.

> [!note]- 🔵 Probabilistic Geometric Analysis
> **Prereqs:** Stochastic Analysis, 🟢 SDEs, Riemannian Geometry, Spectral Theory, 🟢 Functional Analysis, Malliavin Calculus (for the index-theorem proofs); illuminates Index Theory, Hodge Theory, Spectral Geometry (targets)
>
> **Connects:** Stochastic Analysis ↔ Riemannian Geometry ↔ Index Theory / Hodge Theory ↔ Spectral Geometry ↔ Heat Kernels ↔ Gaussian Free Field
>
> **Note:** The probabilistic side of the index / Hodge / spectral story. Organizing fact: the Laplacian (and the Dirac operator) is the generator of a diffusion, so by Feynman-Kac the heat semigroup $e^{-t\Delta}$ is a Brownian-motion expectation, and the topological invariants extracted analytically from $e^{-t\Delta}$ can be extracted probabilistically from Brownian motion on the manifold. The template is McKean-Singer: $\mathrm{Str}(e^{-t\Delta}) = \chi(M)$ for all $t$; the $t \to 0$ limit localizes (a Brownian bridge collapsing to a point) and returns the Gauss-Bonnet-Chern / Poincaré-Hopf integrand, while $t \to \infty$ projects onto harmonic forms (Hodge). Bismut turned this into a genuine stochastic proof of Atiyah-Singer via the Brownian bridge and Malliavin calculus.
>
> **Sub-strands (own nodes below):** GFF Isomorphism Theorems / Loop Soups · Witten Laplacian / Metastability.
>
> **Unlocks:** Probabilistic proofs of Atiyah-Singer and Gauss-Bonnet-Chern, the Bismut gradient formula, probabilistic Bochner vanishing theorems, Bismut's hypoelliptic Laplacian (interpolating the Hodge Laplacian and the geodesic flow — ties to the Microlocal node), and heat-kernel / random-walk methods in computation (Laplacian eigenmaps, diffusion maps, heat-kernel signature, discrete Hodge theory / TDA).
>
> **Pointers (sub-directions to develop):** (1) **Bismut's probabilistic index theory** — the Brownian-bridge + Malliavin-calculus proof of the local Atiyah-Singer index theorem, using the Quillen superconnection and short-time heat-kernel localization (Bismut, *The Atiyah-Singer Theorems: A Probabilistic Approach I-II*, J. Funct. Anal. 57, 1984). (2) **Analysis on infinite-dimensional path and loop spaces** — Malliavin calculus as differential geometry on path space: Itô maps of SDEs as charts, the connection determined by the SDE, exterior differentiation as a closed operator, and a Hodge-Kodaira operator and decomposition for 1- and 2-forms, with the path-space "Laplacian" still carrying open problems (Elworthy, *An Approach to Analysis on Path Spaces of Riemannian Manifolds*, arXiv:1911.09764; Driver / Aida / Hsu on integration-by-parts and log-Sobolev on path space). (3) **Index theory for hypoelliptic operators** — Bismut's hypoelliptic Laplacian (a hypoelliptic deformation of the Hodge Laplacian interpolating to the geodesic flow) with its index theory and Ray-Singer analytic torsion (Bismut-Lebeau, *The Hypoelliptic Laplacian and Ray-Singer Metrics*, Annals of Math. Studies 167, 2008), together with the Atiyah-Singer-type index theorem for Hörmander-type / Heisenberg-elliptic operators on contact and sub-Riemannian manifolds (van Erp; the Connes-Moscovici local index formula) — the bridge to the Microlocal and Geometric-Control / sub-Riemannian nodes.
>
> **Key refs:** **Hsu, *Stochastic Analysis on Manifolds* (AMS Graduate Studies in Mathematics 38, 2002)** — the most complete single textbook: Brownian motion on manifolds, heat kernel and short-time asymptotics, probabilistic Gauss-Bonnet-Chern and Atiyah-Singer, path-space analysis. Analytic heat-kernel companion: Berline-Getzler-Vergne, *Heat Kernels and Dirac Operators* (Springer Grundlehren 298). Original probabilistic index proof: Bismut, *The Atiyah-Singer Theorems: A Probabilistic Approach I-II* (J. Funct. Anal. 57, 1984). Curvature / functional-inequality side: Stroock, *An Introduction to the Analysis of Paths on a Riemannian Manifold* (AMS, 2000); Bakry-Gentil-Ledoux, *Analysis and Geometry of Markov Diffusion Operators* (Springer Grundlehren 348, 2014).
>
> **Member of Cluster 5 (Spectral / Index / Microlocal) and Cluster 15 (Stochastic Calculus Core).**

> [!note]- 🔵 Witten Laplacian / Metastability
> **Prereqs:** Morse Theory, Spectral Theory, Riemannian Geometry, 🟢 SDEs, Large Deviations Theory, Microlocal / Semiclassical Analysis
>
> **Connects:** Morse Theory ↔ Spectral Gaps ↔ Metastable Diffusions (Eyring-Kramers) ↔ Large Deviations ↔ Semiclassical Analysis
>
> **Note:** A triple local-to-global bridge. Witten's deformation $d_t = e^{-tf}\, d\, e^{tf}$ proves the Morse inequalities: the low-lying eigenvalues of the Witten Laplacian $\Delta_t$ count the critical points of $f$ (local data) and recover the topology (global). The same $\Delta_t$ generates the overdamped Langevin diffusion in the potential $f$, and its exponentially small eigenvalues are the inverse metastable transition times — the Eyring-Kramers rates — made rigorous by Bovier-Eckhoff-Gayrard-Klein (potential theory) and Helffer-Klein-Nier (semiclassical). Morse theory, spectral gaps, and the slow dynamics of an SDE are the same data.
>
> **Key refs:** Helffer-Nier, *Hypoelliptic Estimates and Spectral Theory for Fokker-Planck Operators and Witten Laplacians* (Springer LNM 1862, 2005); Bovier-den Hollander, *Metastability: A Potential-Theoretic Approach* (Springer Grundlehren 351, 2015); Cycon-Froese-Kirsch-Simon, *Schrödinger Operators* (Witten's proof of the Morse inequalities).

> [!note]- 🔵 Transport Information Geometry
> **Prereqs:** Optimal Transport, Information Geometry, Riemannian Geometry
>
> **Connects:** OT ↔ Information Geometry ↔ Gradient Flows ↔ Ricci Flow ↔ Mean-Field Games

> [!note]- 🔵 Geometrothermodynamics
> **Prereqs:** Riemannian Geometry, Symplectic Geometry (contact geometry / Legendre invariance), Information Geometry, Stochastic Thermodynamics / Statistical Mechanics; the black-hole applications additionally use GR
>
> **Connects:** Information Geometry ↔ Riemannian Geometry ↔ Symplectic / Contact Geometry ↔ Stochastic Thermodynamics ↔ General Relativity (black-hole thermodynamics) ↔ Entropic Inference
>
> **Note:** Quevedo's Legendre-invariant differential-geometric formulation of equilibrium thermodynamics. The thermodynamic phase space is a contact manifold with contact form $\Theta = d\Phi - \sum_a I_a\, dE^a$ — the first law read as a contact structure — and the space of equilibrium states is a Legendre submanifold carrying a Legendre-invariant metric whose curvature encodes thermodynamic interaction: flat for the ideal gas, with curvature singularities exactly at phase transitions. The predecessors are Weinhold (the Hessian of the internal energy) and Ruppeiner (the Hessian of the entropy), each a Riemannian metric on the equilibrium manifold; the Ruppeiner scalar curvature diverges at critical points and its sign distinguishes attractive from repulsive statistical interaction. Neither Weinhold nor Ruppeiner is Legendre-invariant — the geometry changes under a change of thermodynamic potential — and repairing that defect is the entire point of GTD. The organizing bridge to the rest of the cluster: the Ruppeiner metric is the thermodynamic incarnation of the Fisher-Rao information metric, so GTD is information geometry with the entropy as potential, and the same metric is exactly the one Entropic Inference (Caticha) derives as the unique geometry compatible with the MaxEnt update.
>
> **Unlocks:** Black-hole thermodynamics (phase transitions and thermodynamic stability of Reissner-Nordström / Kerr / AdS black holes read off from curvature singularities of the thermodynamic metric — the main arena where GTD is used), diagnosing microscopic interaction from macroscopic geometry, geometric criteria for thermodynamic stability and critical phenomena.

> [!note]- 🔵 Information Field Theory (Enßlin)
> **Prereqs:** Bayesian Statistics / Variational Inference, 🟢 Information Theory, Renormalization Group / Statistical Field Theory (path integrals, Feynman diagrams), 🟢 Functional Analysis (functional integration), Gaussian Free Field (the free theory), 🟢 Measure-Theoretic Probability; the modern algorithms additionally use Information Geometry (geoVI) and Convex Optimization
>
> **Connects:** Bayesian Inference ↔ Statistical Field Theory / QFT (path integrals, Feynman diagrams, effective action) ↔ Information Theory (information Hamiltonian, Gibbs free energy) ↔ Gaussian Free Field / Gaussian Processes (Wiener filter) ↔ Information Geometry (geoVI) ↔ Inverse Problems / Imaging
>
> **Note:** Statistical field theory used as the engine of Bayesian field inference — reconstructing a field (a function over continuous space, hence infinitely many degrees of freedom) from data. The move that unlocks everything: write the joint as a Boltzmann weight by defining the information Hamiltonian $H_d[s] = -\ln P(s,d)$, so the posterior is $P(s \mid d) = e^{-H_d[s]}/Z_d$ with $Z_d = \int \mathcal{D}s\, e^{-H_d[s]} = P(d)$ the partition function. The whole apparatus of statistical / quantum field theory then transfers wholesale: the generating functional $Z_d[J]$, connected correlators, the information propagator $D$ (the posterior covariance = inverse Hessian of $H$), perturbative Feynman diagrams for non-Gaussian interaction terms, and effective actions. The free theory (Gaussian prior + linear measurement + Gaussian noise) has a quadratic Hamiltonian and reproduces the Wiener filter exactly, with the GFF as its prior — so at zeroth order this node is the Gaussian Free Field node wearing an inference hat. Interactions = nonlinearity / non-Gaussianity, handled diagrammatically or variationally by minimizing the Gibbs free energy (a KL / MaxEnt principle, tying it to Entropic Inference). Member of Cluster 20 and Cluster 11.
>
> **Unlocks:** Generalized Wiener / critical filtering with unknown spectra, modern field-inference algorithms — Metric Gaussian Variational Inference (MGVI) and geometric VI (geoVI), which uses the Fisher-Rao metric and so routes through Information Geometry — and large-scale Bayesian imaging (radio interferometry, the gamma-ray sky, Galactic tomography) via the NIFTy software. The computational-payoff axis you like: a working, deployed inference engine, not just a formal analogy.
>
> **Key refs:** Enßlin, Frommert, Kitaura, *Information Field Theory for Cosmological Perturbation Reconstruction and Nonlinear Signal Analysis* (Phys. Rev. D 80, 105005, 2009) — the founding paper; Enßlin, *Information Theory for Fields* (Annalen der Physik 531, 1800127, 2019) — the modern review; Enßlin, *Inference with Minimal Gibbs Free Energy in Information Field Theory* (Phys. Rev. E 82, 051112, 2010) for the variational principle.

> [!note]- 🔵 Markov Categories / Categorical Probability (Fritz, Cho, Jacobs)
> **Prereqs:** Category Theory, Symmetric Monoidal Categories, 🟢 Measure-Theoretic Probability
>
> **Connects:** Category Theory ↔ Bayesian Networks ↔ Compositional Game Theory ↔ String Diagrams

> [!note]- 🔵 Synthetic Differential Geometry / Smooth ∞-Topoi
> **Prereqs:** Category Theory, Higher Category Theory, Differential Geometry, Mathematical Logic
>
> **Connects:** Topos Theory ↔ Differential Geometry ↔ HoTT ↔ Field Theory foundations

> [!note]- 🔵 Diffeological Spaces / Frölicher Spaces
> **Prereqs:** Differential Geometry, Category Theory, Topology
>
> **Connects:** Diff Geom ↔ Infinite-Dim Analysis ↔ Sheaf Theory ↔ Symplectic Geometry on singular spaces

> [!note]- 🔵 Condensed Mathematics (Clausen-Scholze)
> **Prereqs:** Algebraic Topology, Category Theory, Topology, Algebraic Geometry, Derived/Homological Algebra
>
> **Connects:** Functional Analysis ↔ Algebraic Geometry ↔ Homological Algebra

> [!note]- 🔵 Geometric Recursion / Topological Recursion
> **Prereqs:** Riemann Surfaces, Algebraic Geometry, Hopf Algebras, Symplectic Geometry
>
> **Connects:** Enumerative Geometry ↔ Matrix Models ↔ QFT ↔ Moduli Spaces

> [!note]- 🔵 Noncommutative Geometry (Connes)
> **Prereqs:** Operator Algebra, Spectral Theory, Algebraic Topology (K-theory), Riemannian Geometry, Lie Groups, Hopf Algebras
>
> **Connects:** Operator Algebras ↔ Spectral Geometry ↔ Index Theory ↔ QFT ↔ Standard Model

---

## Cutting-Edge Subfields

> [!note]- 🔵 Stochastic Portfolio Theory
> **Prereqs:** 🟢 SDEs, Stochastic Analysis, Martingale Theory; model-free version requires Rough Paths

> [!note]- 🔵 Topological Quantum Field Theory
> **Prereqs:** Symmetric Monoidal Categories, Differential Topology (cobordism), Algebraic Topology, Lie Groups / Representation Theory (for Chern-Simons and quantum-group examples), Higher Category Theory (for extended TQFT); the physical picture additionally uses QFT / Gauge Theory
>
> **Connects:** Category Theory ↔ Algebraic Topology (cobordism, manifold invariants) ↔ QFT / Gauge Theory ↔ Representation Theory (modular tensor categories, quantum groups) ↔ Knot Theory
>
> **Note:** The Atiyah-Segal axioms define an $n$-dimensional TQFT as a symmetric monoidal functor $Z : \mathrm{Cob}_n \to \mathrm{Vect}$ from the cobordism category to vector spaces: manifolds map to state spaces, cobordisms to linear maps, disjoint union to tensor product. This turns "compute a topological invariant of a manifold" into "evaluate a monoidal functor," which is why it is at once a topology, category-theory, and physics object. Examples: a 2D TQFT is exactly a commutative Frobenius algebra (a complete classification); 3D Chern-Simons / Reshetikhin-Turaev produces the Jones polynomial and 3-manifold invariants from a modular tensor category / quantum group.
>
> **Unlocks:** The cobordism hypothesis (Baez-Dolan / Lurie — fully extended TQFTs are classified by fully dualizable objects in a symmetric monoidal $(\infty,n)$-category, the bridge to the ∞-category and higher-algebra nodes), functorial field theory (the Costello-Gwilliam factorization-algebra node), topological phases of matter, anyonic quantum computation

> [!note]- 🔵 Factorization Algebras / Functorial Field Theory (Costello-Gwilliam)
> **Prereqs:** QFT, Higher Category Theory, Operads, Derived/Homological Algebra, Algebraic Topology, Sheaf Theory

> [!note]- 🔵 SLE / Conformal Probability
> **Prereqs:** Complex Analysis, 🟢 SDEs, Stochastic Analysis, Conformal Geometry, Martingale Theory

> [!note]- 🔵 Floer Theory / Symplectic Field Theory
> **Prereqs:** Symplectic Geometry, Morse Theory, Algebraic Topology, 🟢 PDE/Functional Analysis (Fredholm), Riemannian Geometry

> [!note]- 🔵 Derived Algebraic Geometry (Lurie, Toën-Vezzosi)
> **Prereqs:** Algebraic Geometry, Higher Category Theory, Derived/Homological Algebra, Algebraic Topology, Commutative Algebra

---

## Expected Interest

> [!note]- 🔵 Mean-Field Games (Lions, Lasry)
> **Prereqs:** Optimal Transport, 🟢 SDEs, 🟢 PDE (HJB, Fokker-Planck), 🟢 Game Theory, Stochastic Analysis, Variational Calculus

> [!note]- 🔵 Tropical Geometry
> **Prereqs:** Commutative Algebra, Algebraic Geometry, Combinatorial Optimization, Convex Optimization (polyhedral)

> [!note]- 🔵 Geometric Measure Theory
> **Prereqs:** Measure Theory, 🟢 Functional Analysis, Variational Calculus, Multivariate Analysis

> [!note]- 🔵 Stochastic Geometric Mechanics
> **Prereqs:** Geometric Mechanics in Robotics, Symplectic Geometry, Stochastic Analysis, Lie Groups, 🟢 SDEs

---

# Section 2: Synergy Clusters

These are groups of subjects that accelerate each other when studied together — not formal prereqs, but shared intuitions and dual languages.

---

## Cluster 1: Geometry of Probability

**Members:** Optimal Transport · Information Geometry · Gradient Flows · Ricci Flow · Riemannian Geometry · Fokker-Planck · Transport Information Geometry · Geometrothermodynamics · Differential Geometry · Geometric Analysis

> 💡 Otto's insight that the heat equation is Wasserstein gradient flow of entropy makes Fisher-Rao information geometry, Ricci flow as gradient flow of Perelman's entropy, and Fokker-Planck as Wasserstein gradient flow collapse into one picture. JKO scheme + displacement convexity make Bakry-Émery curvature-dimension bounds intuitive. When you learn the Wasserstein metric, you suddenly see why log-Sobolev is "Riemannian" on probability space.

---

## Cluster 2: Stochastic Algebra / Renormalization

**Members:** Rough Paths · Hopf Algebras · Regularity Structures · Stochastic Field Theory · Renormalization Group · Distribution Theory · Operads (combinatorial)

> 💡 The Connes-Kreimer Hopf algebra of rooted trees governs both Feynman-diagram BPHZ renormalization in QFT and Hairer's negative-renormalization in regularity structures. Once you see that "branched rough paths = characters of the Connes-Kreimer Hopf algebra," Itô vs Stratonovich becomes a choice of antipode, and Hairer's reconstruction theorem is the same algebraic gadget as multiplicative renormalization in pQFT. Studying these together turns "renormalization is magic" into "renormalization is a coproduct."

---

## Cluster 3: Categorical Probability and Compositional Reasoning

**Members:** Markov Categories · String Diagrams · Symmetric Monoidal Categories · Compositional Game Theory · Categorical Systems Theory · Polynomial Functors · Probabilistic Graphical Models · Double Categories · Tangent Categories · Coalgebra / Behavioral Equivalence · Lenses / Optics · ωPAP Semantics

> 💡 Bayesian networks, open games, and probabilistic programs all become string diagrams in copy-discard / Markov categories. D-separation in PGMs, conditional independence, and Bayesian inversion become theorems in Markov categories (Fritz). Spivak's polynomial functors give the same compositional substrate for dynamical systems and databases. Double categories (Myers) provide the framework where systems compose along interfaces. Tangent categories (Cockett-Cruttwell) add differentiation; coalgebras add dynamics; lenses add bidirectional data flow. davidad's programme asks: can all of these — plus a probability monad — live in one category (ωPAP)?

---

## Cluster 4: Geometric Mechanics, Control and Robotics

**Members:** Symplectic Geometry · Lie Groups and Lie Algebras · Geometric Mechanics in Robotics (SE(3), screw theory) · Continuum Mechanics · Control Theory (Koopman/nonlinear) · Geometric Control Theory / Sub-Riemannian Geometry · Geometric Algebra · Tensor Calculus · Orbital Mechanics / Astrodynamics · Flight Dynamics · Stochastic Geometric Mechanics · Differential Geometry

> 💡 Hamilton's equations live on T*M with its canonical symplectic form; rigid-body kinematics live on SE(3) with its Lie-algebra se(3) of twists/screws; nonlinear control on manifolds uses the same exponential map and Adjoint action. Once you internalize "twist = element of se(3)" you immediately understand momentum maps, reduction by symmetry, Noether currents, and why Koopman lifting is just the dual representation.

---

## Cluster 5: Spectral / Index / Microlocal

**Members:** Spectral Theory · Index Theory · Microlocal Analysis · Probabilistic Geometric Analysis · Witten Laplacian / Metastability · Riemannian Geometry · Symplectic Geometry · Geometric Quantization · Functional Analysis (Fredholm) · Operator Theory · Spectral Geometry · Noncommutative Geometry · Harmonic Analysis · Floer Theory / Symplectic Field Theory

> 💡 Microlocal analysis is "Fourier transform + symplectic phase space" — the cotangent bundle's symplectic structure is exactly the home of wavefront sets. Atiyah-Singer is proved by reducing index to a symbol on T*M (microlocal symbol calculus) — so Riemannian geometry, Fredholm theory, and microlocal symbol algebras click into one machine. Studying spectral asymptotics (Weyl law) alongside Egorov's theorem makes "quantization = symplectic→Hilbert" tangible.

---

## Cluster 6: QFT Rigorization

**Members:** Functional Analysis · Distribution Theory · Operator Algebra · Operads · Higher Category Theory · Factorization Algebras · Topological Quantum Field Theory · Renormalization Group · Lie Groups

> 💡 The three rigorous-QFT frameworks (algebraic/AQFT via local nets of C*-algebras; functorial via Atiyah-Segal cobordism categories; factorization via Costello-Gwilliam) become unified once you have higher-category theory. Operads (e.g. E_n) describe the "shape of operator-product expansion." When you study these together, Wightman axioms ↔ vertex algebras ↔ factorization algebras are visibly three encodings of the same data.

---

## Cluster 7: Conformal / Random Geometry

**Members:** Complex Analysis · Conformal Geometry · SLE · Gaussian Free Field · Random Conformal Geometry · Riemann Surfaces

> 💡 SLE is a 1D Brownian motion driving the Loewner ODE; couple it to GFF and you get imaginary-geometry flow lines, then exponentiate the GFF to get Liouville quantum gravity. Holding all four objects in mind simultaneously turns 2D critical-phenomena scaling limits into a single conformally-covariant story. Each one is opaque in isolation; together they form a tight web.

---

## Cluster 8: Derived / Higher Algebra Frontier

**Members:** Algebraic Topology · Algebraic Geometry · Category Theory · Higher Category Theory · Derived/Homological Algebra · Derived Algebraic Geometry · Condensed Mathematics · Operads · HoTT · Synthetic Differential Geometry · Diffeological Spaces / Frölicher Spaces · Morse Theory · Simplicial Homotopy Theory · Model Categories · ∞-Categories / Quasi-Categories · ∞-Topoi / Higher Topos Theory

> 💡 This is one ecosystem masquerading as eight subjects. ∞-categories are how you do homotopy-coherent algebra; derived AG = AG done in ∞-categories; condensed math replaces topology with sheaves on profinite sets so derived functors behave; HoTT internalizes the same homotopy theory as a foundation. Studying any one in isolation is brutal; studying them together yields massive cross-illumination. The HTT prereq chain (simplicial sets → model categories → quasi-categories → ∞-topoi) is a single pipeline best traversed sequentially, but each step illuminates the next.

---

## Cluster 9: Mean-Field, Optimal Transport and Large Deviations

**Members:** Optimal Transport · Mean-Field Games · Large Deviations · Hamilton-Jacobi (PDE) · Fokker-Planck · Variational Calculus · Stochastic Control · Path Integrals for Filtering and Control

> 💡 MFG is a coupled forward-Fokker-Planck / backward-HJB system; the Benamou-Brenier dynamic OT formulation is literally a special case of the MFG planning problem. Sanov's LDP gives entropy as the natural cost, linking to Schrödinger bridges (entropic OT). Once you see HJB ↔ Hopf-Lax ↔ Kantorovich duality as one Legendre transform, mean-field control, large-deviation rate functions, and gradient flows synchronize.

---

## Cluster 10: Logic / Type Theory / Category Theory Trinity

**Members:** Mathematical Logic · Type Theory and PL Theory · Category Theory · HoTT · Linear Logic · Temporal Logic Model Checking / Process Algebra · Formal Concurrency Theory / π-calculus · Denotational Semantics / Monadic Computation · Model Theory · Provability Logic · Universal Algebra · Abstract Rewriting Systems

> 💡 Curry-Howard-Lambek says proofs = programs = morphisms in CCCs. Linear logic = proofs in *-autonomous (monoidal closed) categories. HoTT lifts this to ∞-categories and types-as-spaces. Studying together, every concept appears three times in three guises (a proof, a program, a categorical morphism) and that triple-vision is what unlocks formal verification, dependent types, and concurrency.

---

## Cluster 11: Stochastic Thermodynamics / Information / Resource Theory

**Members:** Stochastic Thermodynamics · Information Theory · Large Deviations · Fokker-Planck · Resource Theory · Symmetric Monoidal Categories · Brownian Motor · Nonlinear Expectations (Peng) / Coherent Risk / Choquet · Entropic Inference · Information Field Theory · Statistical Physics of Inference · Geometrothermodynamics

> 💡 Fluctuation theorems (Jarzynski, Crooks) are large-deviation statements about path measures with KL-divergence as rate function — directly tying information theory to nonequilibrium physics. Resource theories formalize "what transformations are free" as monoidal subcategories, and second-law-like monotones become categorical invariants. Nonlinear expectations / coherent risk measures are the convex-analytic backbone of infra-Bayesian objects. Entropic inference (Caticha) provides the foundational layer: Bayes' rule and MaxEnt are the same principle (maximize relative entropy subject to constraints), equilibrium stat mech follows as a special case, and Fisher information emerges as the canonical geometry — making KL divergence the single primitive from which inference, thermodynamics, and information geometry all derive.

---

## Cluster 12: Dynamical Systems and Ergodic Theory

**Members:** Dynamical Systems · Ergodic Theory · Chaos Theory / Nonlinear Dynamics · Coupled Oscillators / Network Dynamics / Complex Systems Theory

> 💡 Ergodic theory is the measure-theoretic side of dynamics (Birkhoff, mixing, entropy); chaos theory is the geometric/topological side (Lyapunov exponents, strange attractors, bifurcations); network dynamics extends both to coupled systems (Kuramoto model, synchronization). Studying Birkhoff’s ergodic theorem alongside Lyapunov exponents alongside synchronization transitions gives you three lenses on the same phase-space structures.

---

## Cluster 13: Complex-Kähler-Hodge Geometry

**Members:** Complex Geometry · Kähler Geometry · Calabi-Yau Manifolds · Hodge Theory · De Rham Cohomology · Singularity Theory · Commutative and Noncommutative Algebra · Galois Theory / Automorphic Forms · Geometric Recursion / Topological Recursion · Tropical Geometry · Algebraic Statistics · Singular Learning Theory

> 💡 Kähler = Riemannian + Symplectic + Complex simultaneously — that triple structure is what makes Hodge decomposition possible. De Rham cohomology is the topological invariant that Hodge theory refines analytically. Singularity theory (resolution of singularities) is the tool that both algebraic geometry and singular learning theory use to handle degenerate critical points. Topological recursion computes invariants on moduli spaces using the same algebraic structures. Tropical geometry is the ℏ→0 dequantization of algebraic geometry that preserves enumerative information.

---

## Cluster 14: Kinetic Theory and Nonlinear PDE

**Members:** Boltzmann / Landau Equation · Nonlinear Analysis · Geometric Measure Theory · Continuum Mechanics / Theoretical Fluid Dynamics

> 💡 Boltzmann → hydrodynamic limit → Navier-Stokes is one pipeline from kinetic to continuum. GMT (currents, varifolds, rectifiability) provides the regularity tools for weak solutions and free boundary problems. Nonlinear analysis (degree theory, fixed points, bifurcation) is the shared analytic toolkit. When you study Boltzmann’s H-theorem alongside entropy solutions of conservation laws, the information-theoretic thread becomes visible.

---

## Cluster 15: Stochastic Calculus Core

**Members:** SDEs · Stochastic Analysis · Malliavin Calculus · Martingale Theory · Stochastic Portfolio Theory · Probabilistic Geometric Analysis · GFF Isomorphism Theorems / Loop Soups

> 💡 Malliavin calculus is “calculus of variations on Wiener space,” extending SDE theory to ask “how smooth is the solution as a function of the noise?” The Clark-Ocone formula + martingale representation theorem make the “smooth vs adapted” duality tangible. Stochastic portfolio theory gives concrete financial applications where the relative entropy of market weights is a supermartingale. Studying these together, Itô’s formula, Girsanov, and Malliavin derivatives form one coherent toolkit.

---

## Cluster 16: Agent Foundations / Computability Core

**Members:** AIT / AIXI / Reflective Oracles · Computability · Computational Complexity · Computable Analysis · Arithmetic Hierarchy · Combinatorial Optimization / Algorithm Design · Fixed Point Theorems

> 💡 AIT = Kolmogorov complexity + computability; AIXI = Solomonoff induction + sequential decision theory; reflective oracles = computability + game theory (fixed-point constructions). The arithmetic hierarchy classifies the logical complexity of predicates that appear throughout agent foundations (e.g., Σ₁ = r.e. = “verifiable but not decidable”). Computable analysis bridges this to your analysis background. Combinatorial optimization provides the algorithmic design skills for bounded rationality. Fixed point theorems are the connective tissue: Lawvere's theorem generates the diagonalization obstructions (Gödel, the converse Lawvere problem) while Brouwer/Kakutani generate the existence results (reflective oracles, equilibria) — reflective oracles exist precisely because a topological fixed point survives where the diagonal one cannot.

---

## Cluster 17: Mechanism Design and Rational Aggregation

**Members:** Mechanism Design · Forecast Elicitation and Aggregation · Complete Class / Coherence Theorems / Harsanyi · Game-Theoretic Foundations for Probability (Vovk) · Byzantine Fault Tolerance / Consensus Protocol Theory · Distributed Systems Theory / Impossibility Results

> 💡 Coherence theorems say rational agents must be Bayesian; mechanism design designs rules for them; Vovk reframes probability itself as a sequential game. BFT/consensus protocols are mechanism design under Byzantine faults — the impossibility results (FLP, CAP) constrain what’s achievable, while the possibility results (Tendermint, HotStuff) show what survives. Forecast elicitation connects scoring rules to information theory. Together they answer: “what can groups of agents compute/agree on/be incentivized to reveal?”

---

## Cluster 18: Engineering Analysis Toolbox

**Members:** Green’s Functions · Perturbation Theory / Integral Transforms · Finite Element Exterior Calculus · Computational Electromagnetics (Discrete Exterior Calculus) · Convex Optimization / High-Dim Optimization · Linear Matrix Inequalities · Optimal Filtering / State Estimation · Path Integrals for Filtering and Control · Detection and Estimation Theory · System Identification · Networked Control Systems · Robust Control / H∞ · Dimensionality Reduction / Compressed Sensing · Linear Systems Theory / Circuit Theory / Signal Processing · Electrical Circuit Theory

> 💡 Green’s functions are the fundamental solutions that integral transforms (Fourier, Laplace) diagonalize. FEM discretizes the variational formulation that functional analysis sets up. Convex optimization solves the resulting finite-dimensional problems. Kalman filtering + compressed sensing both exploit low-rank / sparsity structure in the state. Signal processing is where Fourier analysis meets control theory meets optimization. Studying these together, the thread is: continuous problem → variational formulation → discretization → optimization.

---

## Cluster 19: Quantum and Gauge Physics

**Members:** Quantum Mechanics for Mathematicians · QFT / GR / Gauge Theory · AdS/CFT / Standard Model / Emergent Spacetime · Modular Forms · Mathematical Gauge Theory · Special Relativity / Classical Electrodynamics · Condensed Matter / Nanoscale Physics · Density Functional Theory · Plasma Physics / MHD / Superconductivity

> 💡 QM → QFT → advanced QFT is the physics progression; mathematical gauge theory (connections on principal bundles) is the geometric backbone shared by all. DFT is variational QM for many-body systems. Condensed matter uses representation theory + topology (topological phases via K-theory). Plasma/MHD is classical field theory with electromagnetic coupling. Studying QM alongside gauge theory makes “fiber bundle = gauge field” tangible; adding condensed matter shows the same representation theory classifying particles and quasiparticles.

---

## Cluster 20: Bayesian and Statistical Learning

**Members:** Theoretical Statistics · Bayesian Statistics / Variational Inference · Information Field Theory · Statistical Physics of Inference · High-Dimensional Probability · Networked Information Theory · Probabilistic Graphical Models / Message Passing

> 💡 Bayesian statistics + variational inference are the computational side of posterior computation. High-dimensional probability provides concentration inequalities (sub-Gaussian, matrix Bernstein) needed for consistency and minimax rates. Networked information theory extends Shannon’s single-channel theory to multi-terminal settings where multiple sources/receivers interact — structurally similar to distributed inference in PGMs. Message passing (belief propagation, expectation propagation) is where information theory meets graphical models meet optimization.

---

## Cluster 0: Foundations (ubiquitous prereqs)

**Members:** Linear Algebra · Multivariate Analysis · Measure Theory · Topology · Abstract Algebra / Ring Theory / Modules · Advanced Probability / Measure-Theoretic

> 💡 These six subjects are prerequisites for essentially every other cluster. They don’t form a synergy cluster in the usual sense — they’re the shared language. The synergy here is between the subjects themselves: studying measure theory alongside topology alongside abstract algebra simultaneously builds the common vocabulary (sigma-algebras = topology of measurable sets; quotient rings = algebraic quotient spaces; product measures = categorical products) that makes every downstream subject more accessible.

---

## Cluster 21: Safeguarded AI / Categorical Dynamical Systems (davidad)

**Members:** Categorical Systems Theory · Polynomial Functors · Tangent Categories · Coalgebra / Behavioral Equivalence · Lenses / Optics · Markov Categories · ωPAP Semantics · Nonlinear Expectations / Infra-Bayesianism · HoTT · Temporal Logic Model Checking · Guaranteed-Safe AI / OAA

> 💡 davidad's programme asks for one category unifying ODEs, SDEs, SPDEs, automata, and PGMs — concretely, a tangent category (Cockett-Cruttwell) carrying a probability monad (Fritz-Perrone) generalized to infra-Bayesian credal sets (Mio/Kosoy PcΔ monad). Polynomial functors (Spivak) provide the type system; coalgebras provide the dynamics; lenses provide bidirectional data flow and version control; Markov categories provide the probabilistic backbone; HoTT provides the proof-theoretic layer; model checking provides the computational verifier. The capstone is the triple (world model, safety spec, verifier) from *Towards Guaranteed Safe AI*.
