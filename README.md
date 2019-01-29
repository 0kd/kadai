# kadai

## Package for simulation of turing pattern

"turing pattern" is the theory that explain the pattern of animals, such as spots of python or leopad, back of a mackerel, etc.
 
This simulation suppose a two types of coloured molucule which is surrounded by 6 molucules and affects each other, and the relationship between the two types of molcules is:

* If the number of molcules which surround the molcule and has opposite colour of it is more than n(init and you can set it by the argument,and maximum is 6), the central moclule's colour will be reversed. 

* if molcules around a molcule and molcules around them also has same colour, the central molcule's color will be reversed.

you can repete that operation N (init and you can set it by the argument) times and make various patterns.

The initial state of the molcule distribution is set as random, but it is easy to modify the program to change the it.







チューリングパターンのシミュレーションを、平面上にある周囲六個の分子と接する色素分子について行う。

二種類の色素分子（最初はランダムに分布-->重要な因子なのでプログラムを改変して初期値を自由に設定してください。）について、

* 周り一周の色素分子のうち色が異なるものがn種類以上なら、裏返す

* 周り二周の色素分子と色が同じならば、裏返す

という二つの操作をN回繰り返すと、いろいろな模様ができる。


### install:
```{bash}
pip install PatternTuring
```

### usage:
```{python}
from PatternTuring import tucom4
a = tucom4.Basalt(4,5,100) # 上の説明で、n = 5, N = 4, 平面上の分子数の平方根 = 100 
a.draw_heatmap() 
```

See the wiki https://github.com/tsuchiura/kadai/wiki for examples of outputs
