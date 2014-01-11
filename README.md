# Velice

<a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/"><img alt="Creative Commons License" style="border-width:0" src="http://i.creativecommons.org/l/by-sa/4.0/88x31.png" /></a><br /><span xmlns:dct="http://purl.org/dc/terms/" href="http://purl.org/dc/dcmitype/Text" property="dct:title" rel="dct:type">Velice</span> by <a xmlns:cc="http://creativecommons.org/ns#" href="https://github.com/cnelsonsic/velice" property="cc:attributionName" rel="cc:attributionURL">Charles Nelson</a> is licensed under a <a rel="license" href="http://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>.

A universal miniature skirmish wargame ruleset.

If you want to skip straight to the rules, [they're over here.](https://github.com/cnelsonsic/velice/blob/master/build/book.md)

## Compiling
You'll need the latest pandoc, which necessitates installing `haskell-platform`, and then pandoc from cabal.
At the moment, there's a bug in the `mmorph` package, so that arcane "cabal install" line will get pandoc installed, despite packaging errors.
You will also need Python and `pip`.

```bash
$ sudo apt-get install haskell-platform texlive
$ cabal update
$ cabal install pandoc --reinstall --force-reinstalls --constraint=transformers==0.3.0.0
$ pip install -r requirements.txt
$ make
```

The compiled files will be `build/book.pdf`.
