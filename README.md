# Why do you keep misspelling my name?

Code to support Munich Re Integrated Analytics blog post.

## Installation

The module (linter.py) needs to be made available to pylint either by putting this module's
parent directory in your PYTHONPATH environment variable or by adding `linter.py` to the 
pylint/checkers directory if running from source.

## Running

You can run the linter using

```bash
$ pylint --load-plugins=alitheia_spell_checker test.py
```

## Testing

```bash
$ pytest --doctest-modules
```

Performance of the linter can be tested using `timeit`. 
```python
In [1]: import linter

In [2]: %timeit linter.alitheia_misspelling('aleetheia')
16.7 µs ± 409 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
```
The implication is that a code base with 100k words would take 40ms to lint.