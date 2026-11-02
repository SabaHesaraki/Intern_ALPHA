# Lab 02.3.C - Scope and Arguments Analysis

## 1. Code Snippet 1
- **Prediction:** `10 5`
- **Explanation:** The variable `x` inside function `f` is local and shadows the global `x`. Thus, `f()` returns `10`, and the global `x` remains `5`.

## 2. Code Snippet 2
- **Prediction:** 
  `(1, 2, (), 3, {})`
  `(1, 4, (5, 6), 7, {'mode': 'fast'})`
- **Explanation:** Demonstrates correct ordering of positional, default, `*args`, keyword-only (`c`), and `**kwargs` parameters.

## 3. Code Snippet 3
- **Prediction:** `None`
- **Explanation:** If the condition `n > 0` is false, the function lacks an explicit `return`, so Python implicitly returns `None`.

## 4. Code Snippet 4
- **Prediction:** `TypeError`
- **Explanation:** The asterisk `*` enforces keyword-only arguments. Passing `"sara"` positionally raises a `TypeError`.

