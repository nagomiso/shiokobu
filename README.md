# ShioKobu (塩昆布)

A simple wrapper for [natto-py](https://github.com/buruzaemon/natto-py).
It's to allow to pickle of MeCab object.

"ShioKobu" means pikled sea kelp with solt in Japanese.

# Usage

`shiokobu.MeCab`'s interface is same as `natto.MeCab`.
The only difference between `natto.MeCab` and `shiokobu.MeCab` is that `shiokobu.MeCab` can be picklable.

```py
import pickle
from shiokobu import MeCab

nm = MeCab("-d/var/lib/mecab/dic/juman-utf8")
print(nm.parse("すもももももももものうち"))

# picklable
nm2 = pickle.loads(pickle.dumps(nm))
print(nm2.parse("すもももももももものうち"))
```

# License

This software is released under the MIT License, see `LICENSE` file.
