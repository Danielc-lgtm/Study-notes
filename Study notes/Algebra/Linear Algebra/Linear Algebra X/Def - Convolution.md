---
type: definition
subject: linear-algebra
prereqs:
tags: [algebra, linear-algebra, applied, signal-processing]
---

# Notation

The convolution of an $n$-vector $a$ and an $m$-vector $b$ is the $(n+m-1)$-vector denoted $a \ast b$. Entries are written $(a \ast b)_k$ for $k = 1, \dots, n+m-1$. The convention here follows Boyd's $1$-based indexing.

---

# Axiom Motivation

The desideratum is to define a *product* of two finite sequences (or vectors) that has the algebraic structure one would want of a "natural" product: it should be bilinear, associative, and commutative; it should reduce to ordinary multiplication when the sequences have length one; it should arise naturally in some applied context that motivates the definition.

The cleanest motivation comes from **polynomial multiplication**. Suppose $a = (a_1, \dots, a_n)$ holds the coefficients of a polynomial $p(t) = a_1 + a_2 t + \cdots + a_n t^{n-1}$, and $b$ holds the coefficients of $q(t)$ similarly. The product polynomial $p(t) q(t)$ is then a polynomial of degree $n + m - 2$ (so its coefficient vector has length $n + m - 1$), and its coefficients are obtained by collecting terms: the coefficient of $t^{k-1}$ in $p(t)q(t)$ is $\sum_{i + j = k + 1} a_i b_j$, summing over all pairs $(i, j)$ with $i + j - 2 = k - 1$. **Define the convolution $a \ast b$ to be this coefficient vector**:
$$(a \ast b)_k = \sum_{i + j = k + 1} a_i b_j, \quad k = 1, \dots, n + m - 1.$$
By construction, convolution corresponds to polynomial multiplication, and inherits its algebraic properties for free: commutative ($p q = q p$), associative ($(pq)r = p(qr)$), distributive over addition, and with multiplicative identity the polynomial $1$ (i.e., the $1$-vector $(1)$, which is "scalar $1$"). Also for free, $a \ast b = 0$ implies $a = 0$ or $b = 0$ (a polynomial product is zero only when one factor is zero, since the polynomial ring is an integral domain).

A second motivation comes from **signal processing**. Suppose $u_1, u_2, \dots, u_m$ is a time series — a signal sampled at $m$ time points — and we want to filter it by computing weighted local averages with weights $a = (a_1, \dots, a_n)$. The filtered signal is the $(n + m - 1)$-vector
$$y_t = \sum_{j=1}^{\min(n, t)} a_j u_{t-j+1}, \quad t = 1, \dots, n + m - 1,$$
with the convention that $u_t = 0$ for $t < 1$ or $t > m$. Working through the index algebra, this is exactly $y = a \ast u$. So convolution is the operation of *filtering a signal with a kernel*: weighting nearby values and summing. This is what makes convolution the central operation in digital signal processing, image processing, and convolutional neural networks.

A third motivation comes from **linear time-invariant systems**. A system that takes an input signal $u$ and produces an output signal $y$ is *linear* if $y$ depends linearly on $u$, and *time-invariant* if shifting the input in time shifts the output by the same amount. Any LTI system on finite signals is exactly convolution with a fixed kernel $h$ — the **impulse response** — that characterises the system. So $y = h \ast u$ is the master equation for LTI systems, and the convolution structure is what makes Fourier analysis the natural tool: in the frequency domain, convolution becomes pointwise multiplication.

**What goes wrong with nearby variants?** If we drop the symmetry-in-the-sum requirement and define a non-symmetric "product" $(a \star b)_k = \sum_{i+j = k+1} a_i b_j^2$, we lose commutativity and the polynomial-multiplication interpretation. If we use a different index convention — say $(a \star b)_k = \sum_{i+j = k} a_i b_j$ — we get something equivalent up to a shift, but the convention $i + j = k + 1$ is the one that aligns with $1$-based indexing and polynomial degree. If we omit the boundary effects and only sum over indices where both $a_i$ and $b_j$ exist, we get the "valid" convolution from signal processing, which has length $|n - m| + 1$ rather than $n + m - 1$; this is a *truncation* of the full convolution, and the truncation hides the boundary information.

**Why the matrix form $a \ast b = T(b) a = T(a) b$?** Because for fixed $b$, the function $a \mapsto a \ast b$ is *linear*, and any linear function on $\mathbb R^n$ is multiplication by a matrix. The matrix $T(b)$ is **Toeplitz**: every diagonal is constant, and the columns are shifted copies of $b$ padded with zeros. The Toeplitz structure is the algebraic incarnation of "shift-invariance" — shifting the input shifts the output, which translates into the matrix having identical diagonals.

---

# The Definition

**Convolution of two vectors.** Let $a$ be an $n$-vector and $b$ be an $m$-vector. The **convolution** $a \ast b$ is the $(n + m - 1)$-vector with entries
$$
(a \ast b)_k = \sum_{i + j = k + 1} a_i b_j = \sum_{i=\max(1, k+1-m)}^{\min(n, k)} a_i b_{k+1-i}, \quad k = 1, \dots, n+m-1.
$$
Equivalently, $a \ast b$ is the coefficient vector of the polynomial product $p(t)q(t)$, where $p$ and $q$ are the polynomials with coefficient vectors $a$ and $b$.

**Properties.**
1. **Commutativity:** $a \ast b = b \ast a$.
2. **Associativity:** $(a \ast b) \ast c = a \ast (b \ast c)$.
3. **Distributivity:** $a \ast (b + c) = a \ast b + a \ast c$ (when $b$ and $c$ have the same dimensions).
4. **Bilinearity:** for any scalar $\alpha$, $(\alpha a) \ast b = a \ast (\alpha b) = \alpha (a \ast b)$.
5. **Integral domain:** $a \ast b = 0$ implies $a = 0$ or $b = 0$.
6. **Sum property:** $\mathbf{1}^T (a \ast b) = (\mathbf 1^T a)(\mathbf 1^T b)$.
7. **Identity:** if $e_1$ denotes a $1$-vector $(1)$ (or a vector with leading $1$ and remaining zeros of any length), $e_1 \ast b$ shifts $b$.

**Matrix-vector form.** For fixed $b$, the map $a \mapsto a \ast b$ is linear, with matrix $T(b) \in \mathbb R^{(n+m-1) \times n}$ given by
$$T(b)_{ij} = \begin{cases} b_{i - j + 1} & \text{if } 1 \leq i - j + 1 \leq m,\\ 0 & \text{otherwise.} \end{cases}$$
The matrix $T(b)$ is a **Toeplitz matrix**: every diagonal is constant. For example, with $a$ of length 4 and $b = (b_1, b_2, b_3)$, the matrix is
$$T(b) = \begin{pmatrix} b_1 & 0 & 0 & 0 \\ b_2 & b_1 & 0 & 0 \\ b_3 & b_2 & b_1 & 0 \\ 0 & b_3 & b_2 & b_1 \\ 0 & 0 & b_3 & b_2 \\ 0 & 0 & 0 & b_3 \end{pmatrix}.$$
By symmetry, $a \ast b = T(b) a = T(a) b$.

---

# Relate to Other Fields / Compression

Convolution is the **multiplication operation of the polynomial ring** $\mathbb R[t]$, restricted to finite-degree polynomials. The vector of length $n$ with entries $(a_1, \dots, a_n)$ corresponds to the polynomial $a_1 + a_2 t + \cdots + a_n t^{n-1}$, and convolution of vectors corresponds to multiplication of polynomials. So $(\bigoplus_n \mathbb R^n, +, \ast)$ — the space of all finite real sequences with addition and convolution — is isomorphic to the polynomial ring $\mathbb R[t]$. This is the most compressing way to remember convolution: it is polynomial multiplication.

For **circular** or **periodic** convolution — where indices are taken modulo $n$ — the multiplication is in $\mathbb R[t]/(t^n - 1)$ instead, and the corresponding matrices are **circulant**, not just Toeplitz. Circulant matrices are diagonalised by the discrete Fourier transform: every circulant matrix's eigenvectors are the columns of the DFT matrix, and its eigenvalues are the DFT of its first column. This is the algebraic foundation of the **FFT-based fast convolution**: instead of computing $a \ast b$ in $O(nm)$ time directly, one computes $\hat a = F a$, $\hat b = F b$, multiplies entrywise ($\hat c_k = \hat a_k \hat b_k$), and inverts: $c = F^{-1} \hat c$. The DFT is $O(n \log n)$, so the total cost is $O(n \log n)$ instead of $O(n^2)$.

In linear-time-invariant system theory, convolution is the *only* operation: any LTI system on finite signals is convolution with a fixed kernel (the impulse response). This is the **convolution theorem** of LTI theory, and it underlies digital signal processing, image processing, and convolutional neural networks (where the "convolution layer" applies a small kernel to slide across a larger input).

**True name:** Convolution is *polynomial multiplication* — equivalently, *the unique bilinear shift-invariant product on finite sequences*. As a matrix operation, it is multiplication by a Toeplitz matrix.

---

# Examples / Corollaries

**Is an instance — Boyd's small numerical example.** $(1, 0, -1) \ast (2, 1, -1) = (2, 1, -3, -1, 1)$. Verify: $(a \ast b)_1 = a_1 b_1 = 2$; $(a \ast b)_2 = a_1 b_2 + a_2 b_1 = 1 + 0 = 1$; $(a \ast b)_3 = a_1 b_3 + a_2 b_2 + a_3 b_1 = -1 + 0 + (-2) = -3$; and so on.

**Is an instance — three-period moving average.** With $a = (1/3, 1/3, 1/3)$ and an $n$-vector $x$ representing a time series, $a \ast x$ is the smoothed series whose entry $t$ (for $t = 3, \dots, n$) is the average of $x_t, x_{t-1}, x_{t-2}$. The first two and last two entries involve boundary terms. This is the canonical low-pass filter, used everywhere from financial time series to climate data.

**Is an instance — first-difference filter.** With $a = (1, -1)$, $a \ast x$ has entries $(x_1, x_2 - x_1, x_3 - x_2, \dots, x_n - x_{n-1}, -x_n)$. The middle entries are the first differences of $x$, equivalent to the **discrete derivative**. This is the basic high-pass filter.

**Is an instance — convolution as polynomial multiplication.** With $a = (1, 1)$ (the polynomial $1 + t$) and $b = (1, 2, 1)$ (the polynomial $1 + 2t + t^2$), $a \ast b = (1, 3, 3, 1)$, the coefficient vector of $(1 + t)(1 + 2t + t^2) = 1 + 3t + 3t^2 + t^3 = (1 + t)^3$. The binomial coefficients appear, as expected.

**Is NOT an instance — pointwise product.** The pointwise product $a \odot b$ with $(a \odot b)_i = a_i b_i$ (where defined) is *not* convolution. The pointwise product corresponds, via Fourier transform, to convolution in the dual domain; these two operations are Fourier-dual, but they are different. The standard mnemonic: pointwise in time $\Leftrightarrow$ convolution in frequency, and vice versa.

**Is NOT an instance — non-shift-invariant linear operation.** A general linear operation $a \mapsto Ma$ with $M$ an arbitrary matrix is not convolution unless $M$ is Toeplitz. The matrix $M = \operatorname{diag}(\lambda_1, \dots, \lambda_n)$ (entrywise scaling) is not convolution because it is not shift-invariant.

**Corollary — sum property.** $\mathbf 1^T(a \ast b) = (\mathbf 1^T a)(\mathbf 1^T b)$. The sum of the convolution entries is the product of the sums. Proof: $\mathbf 1^T a = p(1)$ and $\mathbf 1^T b = q(1)$, where $p, q$ are the polynomial views. The polynomial product $pq$ evaluated at $1$ is $p(1)q(1)$, and that equals $\mathbf 1^T(a \ast b)$ since the latter is the sum of the coefficients of $pq$.

**Corollary — convolution with the unit vector.** $e_k \ast b$ is the vector that places $b$ starting at position $k$, with zeros elsewhere. So convolution with $e_k$ is a *shift*. This is what makes shift-invariance manifest: the impulse response to a unit input at time $k$ is the impulse response shifted to start at time $k$.

**Corollary — convolution of indicator-of-interval with itself.** $a = (1, 1, \dots, 1)$ (the all-ones $n$-vector) convolved with itself is the "triangle" or "tent" vector: $a \ast a$ has entries $1, 2, 3, \dots, n - 1, n, n - 1, \dots, 1$. This is the discrete analogue of the convolution of a rectangle with itself being a triangle, and the basis of why the Central Limit Theorem works — convolutions of indicator functions become bell-shaped.

**Calibration check.** Verify that the convolution $a \ast b$ of an $n$-vector and an $m$-vector has length $n + m - 1$. Verify that $a \ast 1 = a$ (convolution with the scalar $1$ is the identity on vectors). Verify that $a \ast b = b \ast a$ by checking the index symmetry $i + j = k + 1$ is symmetric in $(i, j)$.

---

# Unlocked by This

> [!tip] The Fast Fourier Transform *(from Numerical Analysis)*
> Direct convolution of two $n$-vectors costs $O(n^2)$ flops. The **Fast Fourier Transform** computes the DFT in $O(n \log n)$, and via the convolution theorem this makes convolution $O(n \log n)$ — an exponential speedup for large $n$. The FFT is one of the most important algorithms of the 20th century, enabling signal processing, image compression (JPEG), spectral methods for PDEs, and large-integer multiplication (Schönhage–Strassen).

> [!tip] Probability Theory: Sums of Independent Random Variables *(from Probability)*
> The density of the sum of two independent random variables is the **convolution** of their densities. So if $X, Y$ are independent with densities $f, g$, then $X + Y$ has density $f \ast g$. The Central Limit Theorem is the statement that iterated convolution converges to the Gaussian, and the Fourier-transform proof goes via the convolution theorem.

> [!tip] Convolutional Neural Networks *(from Machine Learning)*
> A CNN layer applies a small kernel (typically $3 \times 3$ or $5 \times 5$) by convolution to a feature map (an image with channels). This implements a shift-invariant linear operation followed by a pointwise nonlinearity (ReLU). The shift-invariance is the architectural inductive bias that makes CNNs effective on images: features detected in one part of the image should be detectable in any other part.
