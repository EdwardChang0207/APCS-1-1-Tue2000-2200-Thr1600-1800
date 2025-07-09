'''
運算元 Operatee
運算子 Operator
    (1)數學運算子 num op num -> num
        [1]取餘數 % 因數倍數
            eg.print(20%3)
        [2]取商數 // 分組分堆
            eg.print(20//3)
        [3]指數 **
            eg.print(2**3)
        [4]除 / -> float
    (2)邏輯運算子
        [1] num op num -> bool
            1. <, >, >=, <=
                eg.print(2 > 3)
            2. ==(equal), !=(not equal)
        [2] bool op bool -> bool (Logic Gates)
            1.not 反閘
                周杰倫：哎呦不錯喔
                不(not)錯(False) -> True
                錯 -> False
                不(not)行(True) -> False
                行 -> True
                eg.
                    a = False
                    print(not a)
            2.or 或閘
            國文 or 英文 -> 3000
            T.     F.      T
            F.     T.      T
            T.     T.      T
            F.     F.      F
            eg.
                a, b = False, False
                print(a or b)
            3.and 且閘
            打掃 and homework -> :)
            T.       F.         F
            F.       T.         F
            T.       T.         T
            F.       F.         F
            eg.
                a, b = False, False
                print(a and b)
            4.xor(excursive or) 斥或閘
            珍奶 xor 烏龍拿鐵 -> :)
            T.      F.         T
            F.      T.         T
            T.      T.         F
            F.      F.         F
            [1]not or and
                a, b = False, False
                print((a or b) and not(a and b))
            [2]bin
                a, b = False, False
                print(a^b)
    (3)Assign =
    (4)in
'''

a = 1
# a(new) = a(old) + 1
a += 1

l = [1,2,3]
print(4 in l)