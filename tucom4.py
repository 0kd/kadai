"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
チューリングパターンのシミュレーションは通常微分方程式を用いて行われるが、
ここではグラフ理論を用いて、周囲六個の分子と接する10000個の色素分子のシミュレーションをする。
二種類の色素分子について、
1.周り一周の色素分子のうち色が異なるものが4種類以上なら、裏返す
2.周り二周の色素分子と色が同じならば、裏返す
という二つの性質を仮定すると、蛇のような模様ができる。
2015/5/3に放送された「目がテン！大実験…オセロの石で生き物の模様を作ってみよう！」の実験を参考にした。

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

import matplotlib.pyplot as plt
import numpy as np
import random
import sys

encnum_rec = False
countnum_rec = False


if len(sys.argv) > 1:
    for i in range(len(sys.argv)-1)+1:
        if sys.argv[i].split("-")[0] == 'rep':
            countnum = sys.argv[1].split("-")[1]
            countnum_rec = True
        elif sys.argv[i].split("-")[0] == 'enc':
            encnum = sys.argv[1].split("-")[1]
            encnum_rec = True

    countnum = int(sys.argv[1])

if not encnum_rec:
    encnum = 4

if not countnum_rec:
    countnum = 5


class Basalt:
    def __init__(self):
        random.seed(910910)
        self.ht = [random.randrange(2) for i in range(10000)]  # 10000個で試す
        self.num_rep = 0
        self.width = 100  # 幅は100

    def adj(self, i):  # 端の処理、接している個数を返す
        adj = []

        if i % self.width > 0:
            adj.append(i - 1)

        if i > self.width:
            adj.append(i - 1 - self.width)

        if i >= self.width:
            adj.append(i - self.width)

        if i < len(self.ht) - self.width:
            adj.append(i + self.width)

        if i % self.width < self.width - 1:
            adj.append(i + 1)

        if i < len(self.ht) - self.width - 1:
            adj.append(i + 1 + self.width)

        return adj

    def adj3(self, i):  # 中心の外側の外側は存在するか（すればok）
        if len(self.adj(i)) == 6:
            wre = 0

            for k in self.adj(i):
                if len(self.adj(k)) == 6:
                    wre += 1

            if wre == 6:
                return "ok"

    def adj2(self, i):  # 頂点の周りの頂点の更に周り
        adj2 = []
        adj2.append(i-2-2*(self.width))
        adj2.append(i-1-2*(self.width))
        adj2.append(i-2*(self.width))
        adj2.append(i-2-(self.width))
        adj2.append(i+1-(self.width))
        adj2.append(i-2)
        adj2.append(i+2)
        adj2.append(i+2+2*(self.width))
        adj2.append(i+1+2*(self.width))
        adj2.append(i+2*(self.width))
        adj2.append(i-1+(self.width))
        adj2.append(i+2+(self.width))

        return adj2

    def omaru0628(self, num_rep_gen):
        while self.num_rep < num_rep_gen:
            self.num_rep += 1
            candidate = []

            for i in range(len(self.ht)):  # 全ての頂点に関して
                num_enclose = 0

                for p in self.adj(i):  # 周囲の頂点に関して
                    if self.ht[p] != self.ht[i]:  # 中心と周囲の色が異なっている場合の数をカウント
                        num_enclose += 1

                if num_enclose > 4:  # 中心と異なっている色の頂点の数が４以上で、中心を色を変えるリストへ入れる
                    candidate.append(i)

                if num_enclose == 0:  # 中心と異なっている色の頂点がない場合
                    if self.adj3(i) == "ok":  # もう一周外側もあるのか確認
                        candidate.append(i)  # 周囲二周の色が同じ場合、中心を裏返す(とりあえずappend)

                        for h in self.adj2(i):  # もう一周外側の頂点全てに対して
                            if self.ht[h] != self.ht[i]:  # 異なる色の頂点がある場合は除外
                                candidate.pop()  # 同じじゃなかったら削除

                                break

            for f in candidate:  # 指定された場所を裏返す
                if self.ht[f] == 0:
                    self.ht[f] = 1
                elif self.ht[f] == 1:
                    self.ht[f] = 0
        self.pre_graph()

    def pre_graph(self):
        self.s = []
        self.t = []

        for h in range(self.width):
            for g in range(self.width*(h-1), self.width*(h-1)+self.width, 1):
                if self.ht[g] == 1:
                    self.s.append(h)
                    self.t.append(g-self.width*(h-1))

    def draw_heatmap(self):
        heatmap, xedges, yedges = np.histogram2d(self.s, self.t, bins=self.width)
        extent = [xedges[0], xedges[self.width], yedges[0], yedges[self.width]]
        plt.figure()
        plt.imshow(heatmap, extent=extent)
        plt.show()
        plt.savefig('ploplot.png')


def test():
    b = Basalt()
    b.omaru0628(countnum)
    b.draw_heatmap()


test()
