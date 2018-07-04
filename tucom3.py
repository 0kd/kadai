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

class Basalt:
    def __init__(self):
        random.seed(910)
        self.ht = [ random.randrange(2) for i in range(10000)] #10000個で試す
        self.j=0
        self.width = 100 #幅は100
    def adj(self,i): 
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

    def adj3(self,i):
        if len(self.adj(i))==6:
            wre=0
            for k in self.adj(i):
                if len(self.adj(k))==6:
                    wre+=1    
            if wre==6:
                return "ok" 
    def adj2(self,i):#頂点の周りの頂点の更に周り
        adj2=[]
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

    def omaru0628(self):
        while self.j<5: 
            self.j+=1
            r=[]
            q=[]
            for i in range(len(self.ht)):#全ての頂点に関して
                a=0
                b=0
                q.append(i)
                for p in self.adj(i):#周囲の頂点に関して
                    if self.ht[p] != self.ht[i]:#中心と周囲の色が異なっている場合の数をカウント
                        a+=1
                if a>4:#中心と異なっている色の頂点の数が４以上で、中心を色を変えるリストへ入れる
                    r.append(i)
                    print("i",i)
                if a==0:#中心と異なっている色の頂点がない場合    
                    if self.adj3(i)=="ok":#もう一周外側もあるのか確認
                        for h in self.adj2(i):#もう一周外側の頂点全てに対して
                            if self.ht[h] != self.ht[i]:#異なる色の頂点がある場合は除外
                                break
                            r.append(i)#周囲二周の色が同じ場合、中心を裏返す
                            print("b")
            for f in r:#指定された場所を裏返す
                if self.ht[f]==0:
                    self.ht[f]=1
                elif self.ht[f]==1:
                    self.ht[f]=0
            self.omaru0628()
        self.hsksidi()

    def hsksidi(self):
        self.s=[]
        self.t=[]
        for h in range(self.width):
            for g in range(self.width*(h-1),self.width*(h-1)+self.width,1):
                if self.ht[g]==1:
                    self.s.append(h)
                    self.t.append(g-self.width*(h-1))
        
    def draw_heatmap(self,s ,t):
        heatmap, xedges, yedges = np.histogram2d(s, t, bins=self.width)
        extent = [xedges[0], xedges[self.width], yedges[0], yedges[self.width]]
        plt.figure()
        plt.imshow(heatmap, extent=extent)
        plt.show()
        plt.savefig('ploplot.png')        


# In[ ]:

def test():
    b = Basalt()  
    print(b.adj(0))
    b.omaru0628()
    b.draw_heatmap(b.s,b.t)
print(test())

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
実行結果は

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

チ
