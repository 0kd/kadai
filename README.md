# kadai

## Package for simulation of turing pattern

チューリングパターンのシミュレーションを、平面上にある周囲六個の分子と接する色素分子について行う。

二種類の色素分子（最初はランダムに分布）について、

* 周り一周の色素分子のうち色が異なるものがn種類以上なら、裏返す

* 周り二周の色素分子と色が同じならば、裏返す

という二つの操作をN回繰り返すと、いろいろな模様ができる。

2015/5/3に放送された「目がテン！大実験…オセロの石で生き物の模様を作ってみよう！」の実験を参考にした。


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

