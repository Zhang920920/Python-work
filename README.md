# 南華大學Python資料結構 期中報告
11124213 張芮瑜
# 
南華大學Python程式設計-期末報告
11124235 吳易軒 11124213 張芮瑜

計算函數曲線與x軸包圍面積
描述
計算函數曲線在區間(a,b)與x軸包圍的面積,可將這個區域平行於y軸切分成相等寬度的小梯形,每個梯形的面積可近似求出,所有梯形面積的和就是函數曲線與x軸包圍的面積,也就是函數在給定區間的積分值,dx越小,梯形近似度越高,計算結果越精確,也就是說區間切分段的越多,結果越精確。
計算函數sin(x)在區間(a,b)與x軸包圍的面積,a,b由使用者輸入,區間切分多少段也由使用者輸入。
code
將積分算式打入副程式
    def trapezoidal_rule(f, a, b, n):
    dx = (b - a) / n
    x = [a + i * dx for i in range(n + 1)]
    y = [f(xi) for xi in x]
    area = (y[0] + y[-1]) / 2
    area += sum(y[1:-1])
    area *= dx
    return area
  ## 輸入格式有三個
    一個是區間的起點 a
    一個是區間的終點 b
    最後是區間切分的段數 n
    a = float(input("請輸入區間的起點 a: "))
    b = float(input("請輸入區間的終點 b: "))
    n = int(input("請輸入區間切分的段數 n: "))
  ## 印出積分值 保留2位小數
    area = trapezoidal_rule(math.sin, a, b, n)
    print(f"函數 sin(x) 在區間 [{a}, {b}] 與 x 軸包圍的面積近似值為: {area:.2f}")
