https://qiita.com/_-_-_-_-_/items/34f933adc7be875e61d0

# 入力
## 1行だけ取る

```python
# abcde
s = input() # s = "abcde"
# abcde
s = list(input()) # s = ["a","b,"c","d","e"]
# 5
a = int(input()) # a = 5
# 1 2
x, y = map(int, input().split) # x = 1, y = 2
# 1 2 3 ... n
li = input().split() # li = ['1','2','3',...,'n']
# 1 2 3 ... n
li = list(map(int, input().split())) # li = [1,2,3,4,5,...,n]
# FFFTFTTFF
li = input().split("T") # li = ['FFF', 'F', '', 'FF']
```

## 複数行
### 行数指定あり
```python
# 3
# hoge
# foo
# bar
##################
n = int(input())
string_list = [input() for i in range(n)]
#string_list <- ['hoge','foo','bar']
```

### 行数指定なし
```python
# 1 2 2 3 1
# 4 5 3 4 1 2 3 4
# 2 3 5 6 0 2
#####################
while True:
    try:
        li_A = list(map(int, input().split()))
        # li_A <- [1, 2, 2, 3, 1]
    except:
        break
#####################
li = []
while True:
    try:
        li.append(list(map(int, input().split()))
    except:
        break
# li <- [[1,2,2,3,1], ... ]
```

# 出力
```python
# s <- "hogehoge"
print(s) # hogehoge\n
# s <- "hogehoge"
print(s, end="") # hogehoge
# a <- 1, b <- 2
print(a/b) # 0.5\n
# a <- 1, b <- 2
print("%lf" % (a/b)) # 0.500000\n
# a <- 1, b <- 2
print("%.1lf" % (a/b)) # 0.5\n
# a <- 1, b <- 2
print(str(a/b)+"くらいかな") # 0.5くらいかな
```

# その他
## 小数点表示
```python
a = 0.364364
print(a) # 0.364364
print("{:.6f}".format(a)) # 0.364364
print("{:.4f}".format(a)) # 0.3644

b = 810
print("{:b}".format(b)) # 1100101010 2進数表記
print("{:o}".format(b)) # 1452 8進数表記
print("{:x}".format(b)) # 32a 16進数小文字表記
print("{:X}".format(b)) # 32A 16進数大文字表記
```
## ゼロ埋め・幅寄せ
```python
print("python".ljust(15,'-')) # 左詰め
#python---------
print("python".center(15,'-'))# 中央寄せ
#-----python----
print("python".rjust(15,'-')) # 右詰め
#---------python
print(str(29).rjust(10,'0')) #10桁ゼロ埋め
#0000000029
```
# 速攻テクニック
## 二分探索
```python
import bisect
listA=[1,2,5,2,4,6,7,8,6,56,3,56,76,34,32,2,6,0,32,6,0,...]
listA.sort()
zeroindex=bisect.bisect_right(listA,0) #ソートされたリスト内で0の場所を探し、右側Indexを返す
clearlistA=listA[zeroindex:]#0以下が存在しないリストを得る
```

## 文字列操作
```python
'abc123def'[:] #すべての文字列が取れる
#'abc123def'

'abc123def'[-1:] #終端文字がとれる
#'f'

'abc123def'[:-1] #最後の1文字以外のものがとれる。
#'abc123de'

'abc123def'[::-1] #文字が逆転する
#'fed321cba'
```

## 正規表現
```python
import re

s = 'hoge6hoge21foo:bar'
re.findall(r'[a-z]+',s) #['hoge', 'hoge', 'foo', 'bar']
re.findall(r'[a-z0-9]+',s) # ['hoge6hoge21foo', 'bar']

```

# AtcoderでTDD
- 問題文に用意されているテストケースはそのまま利用する
- インプットとアウトプットの処理はmainブロックで行う
- mainブロックから呼び出す関数に対してTDDを適用する
- Pythonの標準機能はテストの対象にしない