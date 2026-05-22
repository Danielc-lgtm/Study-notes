---
type: exercise-index
subject: linear-algebra
section: "XI.1"
tags: [algebra, linear-algebra, applied, optimization]
---

## §XI.1 The Least Squares Problem — Exercises

The exercises in this section drill the foundational LS problem and its solution methods. The skill they build is *recognizing* when a problem reduces to LS — typically when there is more data than parameters and an overdetermined linear system — and *applying* the closed-form solution (normal equations or QR-based) to compute the answer. The recurring theme is the conversion from a problem statement in raw data terms (data points, model parameters, residuals) to a problem in linear-algebraic terms (design matrix, target vector, LS solution).

- [[Ex - Fitting a line to data via least squares]] (⭐) — Closed-form regression coefficients via direct computation of the $2 \times 2$ Gram matrix and recognition of statistical quantities (correlation, standard deviation) ([[Def - Least Squares Problem]], [[Def - Normal Equations]], [[Thm - Existence and Uniqueness of Least Squares Solution]]).

- [[Ex - Polynomial fitting and overfitting]] (⭐⭐) — Fit polynomials of degrees 0 through 20 and identify the optimal degree via train/test error analysis; the canonical bias-variance U-shape ([[Def - Least Squares Data Fitting]], [[Def - Validation (Training and Test Error)]], [[Thm - Existence and Uniqueness of Least Squares Solution]], [[Thm - Least Squares via QR Factorization]]).

- [[Ex - Binary classifier via least squares]] (⭐⭐) — Build a binary classifier by fitting LS regression to $\pm 1$ labels and thresholding; compute confusion matrix, cross-validate, build ROC curve ([[Def - Least Squares Classifier]], [[Def - Least Squares Data Fitting]], [[Def - Validation (Training and Test Error)]], [[Thm - Least Squares via QR Factorization]]).
