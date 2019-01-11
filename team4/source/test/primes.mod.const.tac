primes.mod.const:
[[ module: primes
  [[ type manager
    base types:
      <NULL>
      <int>
      <char>
      <bool>
      <ptr(4) to <NULL>>
    pointer types:
      <ptr(4) to <NULL>>
      <ptr(4) to <array of <char>>>
      <ptr(4) to <array of <int>>>
      <ptr(4) to <array 14 of <char>>>
      <ptr(4) to <array 24 of <char>>>
      <ptr(4) to <array 1000000 of <int>>>
      <ptr(4) to <array 30 of <char>>>
      <ptr(4) to <array 4 of <char>>>
      <ptr(4) to <array 45 of <char>>>
      <ptr(4) to <array 7 of <char>>>
      <ptr(4) to <array 15 of <char>>>
      <ptr(4) to <array 20 of <char>>>
      <ptr(4) to <array 3 of <char>>>
    array types:
      <array of <char>>
      <array 1000000 of <int>>
      <array of <int>>
      <array 30 of <char>>
      <array 4 of <char>>
      <array 45 of <char>>
      <array 7 of <char>>
      <array 15 of <char>>
      <array 20 of <char>>
      <array 3 of <char>>
      <array 14 of <char>>
      <array 24 of <char>>
  ]]
  [[
    [ *CalcPrimes(<ptr(4) to <array of <int>>>,<int>) --> <int>     ]
    [ *DIM(<ptr(4) to <NULL>>,<int>) --> <int>     ]
    [ *DOFS(<ptr(4) to <NULL>>) --> <int>     ]
    [ *PrintPrimes(<ptr(4) to <array of <int>>>,<int>,<int>) --> <NULL>     ]
    [ *ReadInt() --> <int>     ]
    [ *WriteChar(<char>) --> <NULL>     ]
    [ *WriteInt(<int>) --> <NULL>     ]
    [ *WriteLn() --> <NULL>     ]
    [ *WriteStr(<ptr(4) to <array of <char>>>) --> <NULL>     ]
    [ @_str_1   <array 30 of <char>>     ]
      [ data: '  computing primes from 1 to ' ]
    [ @_str_10  <array 24 of <char>>     ]
      [ data: 'Compute primes up to : ' ]
    [ @_str_2   <array 4 of <char>>     ]
      [ data: '...' ]
    [ @_str_3   <array 45 of <char>>     ]
      [ data: 'WARNING: array too small to hold all primes.' ]
    [ @_str_4   <array 7 of <char>>     ]
      [ data: 'ERROR.' ]
    [ @_str_5   <array 7 of <char>>     ]
      [ data: 'done. ' ]
    [ @_str_6   <array 15 of <char>>     ]
      [ data: ' primes found.' ]
    [ @_str_7   <array 20 of <char>>     ]
      [ data: 'Prime numbers 1 to ' ]
    [ @_str_8   <array 3 of <char>>     ]
      [ data: '  ' ]
    [ @_str_9   <array 14 of <char>>     ]
      [ data: 'Prime numbers' ]
    [ main     <NULL>     ]
    [ @n        <int>     ]
    [ @p        <array 1000000 of <int>>     ]
    [ @pn       <int>     ]
    [ $t0       <ptr(4) to <array 14 of <char>>> %ebp-16     ]
    [ $t1       <ptr(4) to <array 24 of <char>>> %ebp-20     ]
    [ $t2       <int> %ebp-24     ]
    [ $t3       <ptr(4) to <array 1000000 of <int>>> %ebp-28     ]
    [ $t4       <int> %ebp-32     ]
    [ $t5       <ptr(4) to <array 1000000 of <int>>> %ebp-36     ]
  ]]
  [[ primes
      0:     &()    *t0 <- &_str_9
      1:     param  0 <- t0
      2:     call   WriteStr
      3:     call   WriteLn
      4:     &()    *t1 <- &_str_10
      5:     param  0 <- t1
      6:     call   WriteStr
      7:     call   t2 <- ReadInt
      8:     assign n <- t2
      9:     param  1 <- n
     10:     &()    *t3 <- &p
     11:     param  0 <- t3
     12:     call   t4 <- CalcPrimes
     13:     assign pn <- t4
     14:     param  2 <- pn
     15:     param  1 <- n
     16:     &()    *t5 <- &p
     17:     param  0 <- t5
     18:     call   PrintPrimes
  ]]

  [[ procedure: CalcPrimes
    [[
      [ $N        <int> %ebp-16       ]
      [ $i        <int> %ebp-20       ]
      [ $isprime  <bool> %ebp-21       ]
      [ %n        <int> %ebp+12       ]
      [ %p        <ptr(4) to <array of <int>>> %ebp+8       ]
      [ $pidx     <int> %ebp-28       ]
      [ $psqrt    <int> %ebp-32       ]
      [ $t10      <int> %ebp-36       ]
      [ $t11      <int> %ebp-40       ]
      [ $t12      <int> %ebp-44       ]
      [ $t13      <int> %ebp-48       ]
      [ $t14      <int> %ebp-52       ]
      [ $t15      <int> %ebp-56       ]
      [ $t16      <int> %ebp-60       ]
      [ $t17      <int> %ebp-64       ]
      [ $t18      <int> %ebp-68       ]
      [ $t19      <int> %ebp-72       ]
      [ $t20      <int> %ebp-76       ]
      [ $t21      <int> %ebp-80       ]
      [ $t22      <int> %ebp-84       ]
      [ $t23      <int> %ebp-88       ]
      [ $t24      <int> %ebp-92       ]
      [ $t25      <int> %ebp-96       ]
      [ $t26      <int> %ebp-100       ]
      [ $t27      <int> %ebp-104       ]
      [ $t28      <int> %ebp-108       ]
      [ $t29      <int> %ebp-112       ]
      [ $t30      <int> %ebp-116       ]
      [ $t31      <int> %ebp-120       ]
      [ $t32      <int> %ebp-124       ]
      [ $t33      <ptr(4) to <array 45 of <char>>> %ebp-128       ]
      [ $t34      <int> %ebp-132       ]
      [ $t35      <int> %ebp-136       ]
      [ $t36      <int> %ebp-140       ]
      [ $t37      <int> %ebp-144       ]
      [ $t38      <int> %ebp-148       ]
      [ $t39      <int> %ebp-152       ]
      [ $t40      <int> %ebp-156       ]
      [ $t41      <int> %ebp-160       ]
      [ $t42      <int> %ebp-164       ]
      [ $t43      <int> %ebp-168       ]
      [ $t44      <int> %ebp-172       ]
      [ $t45      <ptr(4) to <array 7 of <char>>> %ebp-176       ]
      [ $t46      <ptr(4) to <array 7 of <char>>> %ebp-180       ]
      [ $t47      <ptr(4) to <array 15 of <char>>> %ebp-184       ]
      [ $t6       <ptr(4) to <array 30 of <char>>> %ebp-188       ]
      [ $t7       <ptr(4) to <array 4 of <char>>> %ebp-192       ]
      [ $t8       <int> %ebp-196       ]
      [ $t9       <int> %ebp-200       ]
      [ $v        <int> %ebp-204       ]
    ]]
    [[ CalcPrimes
        0:     &()    *t6 <- &_str_1
        1:     param  0 <- t6
        2:     call   WriteStr
        3:     param  0 <- n
        4:     call   WriteInt
        5:     &()    *t7 <- &_str_2
        6:     param  0 <- t7
        7:     call   WriteStr
        8:     param  1 <- 1
        9:     param  0 <- p
       10:     call   t8 <- DIM
       11:     assign N <- t8
       12:     if     t8 < 1 goto 5_if_true
       13:     goto   6_if_false
       14: 5_if_true:
       15:     return 0
       16:     goto   4
       17: 6_if_false:
       18: 4:
       19:     assign t9 <- 0
       20:     param  0 <- p
       21:     call   t10 <- DOFS
       22:     add    t11 <- 0, t10
       23:     add    t12 <- p, t11
       24:     assign @t12 <- 1  // *t12 = &p
       25:     assign t13 <- 4
       26:     param  0 <- p
       27:     call   t14 <- DOFS
       28:     add    t15 <- 4, t14
       29:     add    t16 <- p, t15
       30:     assign @t16 <- 2  // *t16 = &p
       31:     assign pidx <- 2
       32:     assign psqrt <- 1
       33:     assign v <- 3
       34: 15_while_cond:
       35:     if     v <= n goto 16_while_body
       36:     goto   14
       37: 16_while_body:
       38:     assign isprime <- 1
       39:     assign i <- 1
       40: 21_while_cond:
       41:     if     isprime = 1 goto 23
       42:     goto   20
       43: 23:
       44:     if     i <= psqrt goto 22_while_body
       45:     goto   20
       46: 22_while_body:
       47:     mul    t17 <- i, 4
       48:     param  0 <- p
       49:     call   t18 <- DOFS
       50:     add    t19 <- t17, t18
       51:     add    t20 <- p, t19
       52:     div    t21 <- v, @t20
       53:     mul    t22 <- i, 4
       54:     param  0 <- p
       55:     call   t23 <- DOFS
       56:     add    t24 <- t22, t23
       57:     add    t25 <- p, t24
       58:     mul    t26 <- t21, @t25
       59:     if     t26 = v goto 26_if_true
       60:     goto   27_if_false
       61: 26_if_true:
       62:     assign isprime <- 0
       63:     goto   25
       64: 27_if_false:
       65: 25:
       66:     add    t27 <- i, 1
       67:     assign i <- t27
       68:     goto   21_while_cond
       69: 20:
       70:     if     isprime = 1 goto 32_if_true
       71:     goto   33_if_false
       72: 32_if_true:
       73:     mul    t28 <- pidx, 4
       74:     param  0 <- p
       75:     call   t29 <- DOFS
       76:     add    t30 <- t28, t29
       77:     add    t31 <- p, t30
       78:     assign @t31 <- v  // *t31 = &p
       79:     add    t32 <- pidx, 1
       80:     assign pidx <- t32
       81:     if     t32 = t8 goto 38_if_true
       82:     goto   39_if_false
       83: 38_if_true:
       84:     &()    *t33 <- &_str_3
       85:     param  0 <- t33
       86:     call   WriteStr
       87:     assign n <- 0
       88:     goto   37
       89: 39_if_false:
       90: 37:
       91:     goto   31
       92: 33_if_false:
       93: 31:
       94:     add    t34 <- v, 2
       95:     assign v <- t34
       96:     mul    t35 <- psqrt, 4
       97:     param  0 <- p
       98:     call   t36 <- DOFS
       99:     add    t37 <- t35, t36
      100:     add    t38 <- p, t37
      101:     mul    t39 <- psqrt, 4
      102:     param  0 <- p
      103:     call   t40 <- DOFS
      104:     add    t41 <- t39, t40
      105:     add    t42 <- p, t41
      106:     mul    t43 <- @t38, @t42
      107:     if     t34 > t43 goto 45_if_true
      108:     goto   46_if_false
      109: 45_if_true:
      110:     add    t44 <- psqrt, 1
      111:     assign psqrt <- t44
      112:     if     t44 >= pidx goto 50_if_true
      113:     goto   51_if_false
      114: 50_if_true:
      115:     &()    *t45 <- &_str_4
      116:     param  0 <- t45
      117:     call   WriteStr
      118:     assign n <- 0
      119:     goto   49
      120: 51_if_false:
      121: 49:
      122:     goto   44
      123: 46_if_false:
      124: 44:
      125:     goto   15_while_cond
      126: 14:
      127:     &()    *t46 <- &_str_5
      128:     param  0 <- t46
      129:     call   WriteStr
      130:     param  0 <- pidx
      131:     call   WriteInt
      132:     &()    *t47 <- &_str_6
      133:     param  0 <- t47
      134:     call   WriteStr
      135:     call   WriteLn
      136:     return pidx
    ]]
  ]]

  [[ procedure: PrintPrimes
    [[
      [ $i        <int> %ebp-16       ]
      [ %n        <int> %ebp+12       ]
      [ %p        <ptr(4) to <array of <int>>> %ebp+8       ]
      [ %pn       <int> %ebp+16       ]
      [ $t10      <int> %ebp-20       ]
      [ $t11      <int> %ebp-24       ]
      [ $t12      <int> %ebp-28       ]
      [ $t13      <int> %ebp-32       ]
      [ $t14      <int> %ebp-36       ]
      [ $t6       <ptr(4) to <array 20 of <char>>> %ebp-40       ]
      [ $t7       <ptr(4) to <array 3 of <char>>> %ebp-44       ]
      [ $t8       <int> %ebp-48       ]
      [ $t9       <int> %ebp-52       ]
    ]]
    [[ PrintPrimes
        0:     &()    *t6 <- &_str_7
        1:     param  0 <- t6
        2:     call   WriteStr
        3:     param  0 <- n
        4:     call   WriteInt
        5:     call   WriteLn
        6:     assign i <- 0
        7: 5_while_cond:
        8:     if     i < pn goto 6_while_body
        9:     goto   4
       10: 6_while_body:
       11:     &()    *t7 <- &_str_8
       12:     param  0 <- t7
       13:     call   WriteStr
       14:     mul    t8 <- i, 4
       15:     param  0 <- p
       16:     call   t9 <- DOFS
       17:     add    t10 <- t8, t9
       18:     add    t11 <- p, t10
       19:     param  0 <- @t11
       20:     call   WriteInt
       21:     add    t12 <- i, 1
       22:     assign i <- t12
       23:     div    t13 <- t12, 8
       24:     mul    t14 <- t13, 8
       25:     if     t14 = t12 goto 12_if_true
       26:     goto   13_if_false
       27: 12_if_true:
       28:     call   WriteLn
       29:     goto   11
       30: 13_if_false:
       31: 11:
       32:     goto   5_while_cond
       33: 4:
       34:     call   WriteLn
    ]]
  ]]
]]
