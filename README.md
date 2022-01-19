# Why do you keep misspelling my name?

![](https://shields.io/github/last-commit/ahaque12/why-misspelling-name)
![](https://shields.io/tokei/lines/github/ahaque12/why-misspelling-name)
![badge](https://img.shields.io/endpoint?url=https://gist.githubusercontent.com/ahaque12/3c94642138181608e5b97f4eccec6da8/raw/alitheia-spell-check-badge.json)

Code to support Munich Re Integrated Analytics blog post.

<img src="https://user-images.githubusercontent.com/6743515/150034673-57986ff7-3e23-4c4c-884c-e1bf9c5f7c08.png" width="400px">

## Installation

The module (alitheia_spell_checker.py.py) needs to be made available to pylint either by putting this module's
parent directory in your PYTHONPATH environment variable or by adding `alitheia_spell_checker.py.py` to the 
pylint/checkers directory if running from source.

## Running

You can run the linter using

```bash
$ pylint --load-plugins alitheia_spell_checker sample.py
************* Module why-misspelling-name.sample
sample.py:4:0: C1991: "alitheia" is misspelled. (alitheia-misspelling)
sample.py:5:0: C1991: "alitheia" is misspelled. (alitheia-misspelling)

----------------------------------------------------------------------
Your code has been rated at -10.00/10 (previous run: -10.00/10, +0.00)
```

You can also run the specific function that implements checking an alitheia misspelling
using `alitheia_spell_checker.alitheia_misspelling`.

```python
>>> from alitheia_spell_checker import alitheia_misspelling
>>> alitheia_misspelling('aletheia')
True
```

## Testing

```bash
$ pytest --doctest-modules
```

Performance of the linter can be tested using `timeit`. 
```python
In [1]: import alitheia_spell_checker as asc

In [2]: %timeit asc.alitheia_misspelling('aleetheia')
16.7 µs ± 409 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
```
The implication is that a code base with 100k words would take 40ms to lint.
