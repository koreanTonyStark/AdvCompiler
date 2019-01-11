gcd.mod.const.dead:
[[ module: gcd
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
      <ptr(4) to <array 2 of <int>>>
      <ptr(4) to <array 25 of <char>>>
      <ptr(4) to <array 14 of <char>>>
      <ptr(4) to <array 22 of <char>>>
    array types:
      <array of <char>>
      <array 2 of <int>>
      <array 22 of <char>>
      <array 25 of <char>>
      <array 14 of <char>>
  ]]
  [[
    [ *DIM(<ptr(4) to <NULL>>,<int>) --> <int>     ]
    [ *DOFS(<ptr(4) to <NULL>>) --> <int>     ]
    [ *ReadInt() --> <int>     ]
    [ *ReadNumbers(<ptr(4) to <array 2 of <int>>>) --> <NULL>     ]
    [ *WriteChar(<char>) --> <NULL>     ]
    [ *WriteInt(<int>) --> <NULL>     ]
    [ *WriteLn() --> <NULL>     ]
    [ *WriteStr(<ptr(4) to <array of <char>>>) --> <NULL>     ]
    [ @_str_1   <array 22 of <char>>     ]
      [ data: 'Enter first number : ' ]
    [ @_str_2   <array 22 of <char>>     ]
      [ data: 'Enter second number: ' ]
    [ @_str_3   <array 25 of <char>>     ]
      [ data: 'Greatest commond divisor' ]
    [ @_str_4   <array 14 of <char>>     ]
      [ data: ' subtract  : ' ]
    [ @_str_5   <array 14 of <char>>     ]
      [ data: ' divide    : ' ]
    [ @_str_6   <array 14 of <char>>     ]
      [ data: ' recursive : ' ]
    [ *gcd_iter(<ptr(4) to <array 2 of <int>>>) --> <int>     ]
    [ *gcd_mod(<ptr(4) to <array 2 of <int>>>) --> <int>     ]
    [ *gcd_rec(<ptr(4) to <array 2 of <int>>>) --> <int>     ]
    [ main     <NULL>     ]
    [ @n        <array 2 of <int>>     ]
    [ $t0       <ptr(4) to <array 25 of <char>>> %ebp-16     ]
    [ $t1       <ptr(4) to <array 2 of <int>>> %ebp-20     ]
    [ $t10      <int> %ebp-24     ]
    [ $t2       <ptr(4) to <array 14 of <char>>> %ebp-28     ]
    [ $t3       <ptr(4) to <array 2 of <int>>> %ebp-32     ]
    [ $t4       <int> %ebp-36     ]
    [ $t5       <ptr(4) to <array 14 of <char>>> %ebp-40     ]
    [ $t6       <ptr(4) to <array 2 of <int>>> %ebp-44     ]
    [ $t7       <int> %ebp-48     ]
    [ $t8       <ptr(4) to <array 14 of <char>>> %ebp-52     ]
    [ $t9       <ptr(4) to <array 2 of <int>>> %ebp-56     ]
  ]]
  [[ gcd
      0:     &()    *t0 <- &_str_3
      1:     param  0 <- t0
      2:     call   WriteStr
      3:     call   WriteLn
      4:     call   WriteLn
      5:     &()    *t1 <- &n
      6:     param  0 <- t1
      7:     call   ReadNumbers
      8:     &()    *t2 <- &_str_4
      9:     param  0 <- t2
     10:     call   WriteStr
     11:     &()    *t3 <- &n
     12:     param  0 <- t3
     13:     call   t4 <- gcd_iter
     14:     param  0 <- t4
     15:     call   WriteInt
     16:     call   WriteLn
     17:     &()    *t5 <- &_str_5
     18:     param  0 <- t5
     19:     call   WriteStr
     20:     &()    *t6 <- &n
     21:     param  0 <- t6
     22:     call   t7 <- gcd_mod
     23:     param  0 <- t7
     24:     call   WriteInt
     25:     call   WriteLn
     26:     &()    *t8 <- &_str_6
     27:     param  0 <- t8
     28:     call   WriteStr
     29:     &()    *t9 <- &n
     30:     param  0 <- t9
     31:     call   t10 <- gcd_rec
     32:     param  0 <- t10
     33:     call   WriteInt
     34:     call   WriteLn
  ]]

  [[ procedure: gcd_iter
    [[
      [ %a        <ptr(4) to <array 2 of <int>>> %ebp+8       ]
      [ $t11      <int> %ebp-16       ]
      [ $t12      <int> %ebp-20       ]
      [ $t13      <int> %ebp-24       ]
      [ $t14      <int> %ebp-28       ]
      [ $t15      <int> %ebp-32       ]
      [ $t16      <int> %ebp-36       ]
      [ $t17      <int> %ebp-40       ]
      [ $t18      <int> %ebp-44       ]
      [ $t19      <int> %ebp-48       ]
      [ $t20      <int> %ebp-52       ]
      [ $t21      <int> %ebp-56       ]
      [ $t22      <int> %ebp-60       ]
      [ $t23      <int> %ebp-64       ]
      [ $t24      <int> %ebp-68       ]
      [ $t25      <int> %ebp-72       ]
      [ $t26      <int> %ebp-76       ]
      [ $t27      <int> %ebp-80       ]
      [ $t28      <int> %ebp-84       ]
      [ $t29      <int> %ebp-88       ]
      [ $t30      <int> %ebp-92       ]
      [ $t31      <int> %ebp-96       ]
      [ $t32      <int> %ebp-100       ]
      [ $t33      <int> %ebp-104       ]
      [ $t34      <int> %ebp-108       ]
      [ $t35      <int> %ebp-112       ]
      [ $t36      <int> %ebp-116       ]
      [ $t37      <int> %ebp-120       ]
      [ $t38      <int> %ebp-124       ]
      [ $t39      <int> %ebp-128       ]
      [ $t40      <int> %ebp-132       ]
      [ $t41      <int> %ebp-136       ]
      [ $t42      <int> %ebp-140       ]
      [ $t43      <int> %ebp-144       ]
      [ $t44      <int> %ebp-148       ]
      [ $t45      <int> %ebp-152       ]
      [ $t46      <int> %ebp-156       ]
      [ $t47      <int> %ebp-160       ]
      [ $t48      <int> %ebp-164       ]
      [ $t49      <int> %ebp-168       ]
      [ $t50      <int> %ebp-172       ]
      [ $t51      <int> %ebp-176       ]
      [ $t52      <int> %ebp-180       ]
      [ $t53      <int> %ebp-184       ]
      [ $t54      <int> %ebp-188       ]
      [ $t55      <int> %ebp-192       ]
      [ $t56      <int> %ebp-196       ]
    ]]
    [[ gcd_iter
        0: 1_while_cond:
        1:     param  0 <- a
        2:     call   t12 <- DOFS
        3:     add    t13 <- 0, t12
        4:     add    t14 <- a, t13
        5:     param  0 <- a
        6:     call   t16 <- DOFS
        7:     add    t17 <- 4, t16
        8:     add    t18 <- a, t17
        9:     if     @t14 # @t18 goto 2_while_body
       10:     goto   0
       11: 2_while_body:
       12:     param  0 <- a
       13:     call   t20 <- DOFS
       14:     add    t21 <- 0, t20
       15:     add    t22 <- a, t21
       16:     param  0 <- a
       17:     call   t24 <- DOFS
       18:     add    t25 <- 4, t24
       19:     add    t26 <- a, t25
       20:     if     @t22 > @t26 goto 5_if_true
       21:     goto   6_if_false
       22: 5_if_true:
       23:     param  0 <- a
       24:     call   t28 <- DOFS
       25:     add    t29 <- 0, t28
       26:     add    t30 <- a, t29
       27:     param  0 <- a
       28:     call   t32 <- DOFS
       29:     add    t33 <- 4, t32
       30:     add    t34 <- a, t33
       31:     sub    t35 <- @t30, @t34
       32:     param  0 <- a
       33:     call   t37 <- DOFS
       34:     add    t38 <- 0, t37
       35:     add    t39 <- a, t38
       36:     assign @t39 <- t35  // *t39 = &a
       37:     goto   4
       38: 6_if_false:
       39:     param  0 <- a
       40:     call   t41 <- DOFS
       41:     add    t42 <- 4, t41
       42:     add    t43 <- a, t42
       43:     param  0 <- a
       44:     call   t45 <- DOFS
       45:     add    t46 <- 0, t45
       46:     add    t47 <- a, t46
       47:     sub    t48 <- @t43, @t47
       48:     param  0 <- a
       49:     call   t50 <- DOFS
       50:     add    t51 <- 4, t50
       51:     add    t52 <- a, t51
       52:     assign @t52 <- t48  // *t52 = &a
       53: 4:
       54:     goto   1_while_cond
       55: 0:
       56:     param  0 <- a
       57:     call   t54 <- DOFS
       58:     add    t55 <- 0, t54
       59:     add    t56 <- a, t55
       60:     return @t56
    ]]
  ]]

  [[ procedure: gcd_mod
    [[
      [ %a        <ptr(4) to <array 2 of <int>>> %ebp+8       ]
      [ $t        <int> %ebp-16       ]
      [ $t11      <int> %ebp-20       ]
      [ $t12      <int> %ebp-24       ]
      [ $t13      <int> %ebp-28       ]
      [ $t14      <int> %ebp-32       ]
      [ $t15      <int> %ebp-36       ]
      [ $t16      <int> %ebp-40       ]
      [ $t17      <int> %ebp-44       ]
      [ $t18      <int> %ebp-48       ]
      [ $t19      <int> %ebp-52       ]
      [ $t20      <int> %ebp-56       ]
      [ $t21      <int> %ebp-60       ]
      [ $t22      <int> %ebp-64       ]
      [ $t23      <int> %ebp-68       ]
      [ $t24      <int> %ebp-72       ]
      [ $t25      <int> %ebp-76       ]
      [ $t26      <int> %ebp-80       ]
      [ $t27      <int> %ebp-84       ]
      [ $t28      <int> %ebp-88       ]
      [ $t29      <int> %ebp-92       ]
      [ $t30      <int> %ebp-96       ]
      [ $t31      <int> %ebp-100       ]
      [ $t32      <int> %ebp-104       ]
      [ $t33      <int> %ebp-108       ]
      [ $t34      <int> %ebp-112       ]
      [ $t35      <int> %ebp-116       ]
      [ $t36      <int> %ebp-120       ]
      [ $t37      <int> %ebp-124       ]
      [ $t38      <int> %ebp-128       ]
      [ $t39      <int> %ebp-132       ]
      [ $t40      <int> %ebp-136       ]
      [ $t41      <int> %ebp-140       ]
    ]]
    [[ gcd_mod
        0: 1_while_cond:
        1:     param  0 <- a
        2:     call   t12 <- DOFS
        3:     add    t13 <- 4, t12
        4:     add    t14 <- a, t13
        5:     if     @t14 # 0 goto 2_while_body
        6:     goto   0
        7: 2_while_body:
        8:     param  0 <- a
        9:     call   t16 <- DOFS
       10:     add    t17 <- 4, t16
       11:     add    t18 <- a, t17
       12:     assign t <- @t18
       13:     param  0 <- a
       14:     call   t20 <- DOFS
       15:     add    t21 <- 0, t20
       16:     add    t22 <- a, t21
       17:     param  0 <- a
       18:     call   t24 <- DOFS
       19:     add    t25 <- 0, t24
       20:     add    t26 <- a, t25
       21:     div    t27 <- @t26, t
       22:     mul    t28 <- t27, t
       23:     sub    t29 <- @t22, t28
       24:     param  0 <- a
       25:     call   t31 <- DOFS
       26:     add    t32 <- 4, t31
       27:     add    t33 <- a, t32
       28:     assign @t33 <- t29  // *t33 = &a
       29:     param  0 <- a
       30:     call   t35 <- DOFS
       31:     add    t36 <- 0, t35
       32:     add    t37 <- a, t36
       33:     assign @t37 <- t  // *t37 = &a
       34:     goto   1_while_cond
       35: 0:
       36:     param  0 <- a
       37:     call   t39 <- DOFS
       38:     add    t40 <- 0, t39
       39:     add    t41 <- a, t40
       40:     return @t41
    ]]
  ]]

  [[ procedure: gcd_rec
    [[
      [ %a        <ptr(4) to <array 2 of <int>>> %ebp+8       ]
      [ $t        <int> %ebp-16       ]
      [ $t11      <int> %ebp-20       ]
      [ $t12      <int> %ebp-24       ]
      [ $t13      <int> %ebp-28       ]
      [ $t14      <int> %ebp-32       ]
      [ $t15      <int> %ebp-36       ]
      [ $t16      <int> %ebp-40       ]
      [ $t17      <int> %ebp-44       ]
      [ $t18      <int> %ebp-48       ]
      [ $t19      <int> %ebp-52       ]
      [ $t20      <int> %ebp-56       ]
      [ $t21      <int> %ebp-60       ]
      [ $t22      <int> %ebp-64       ]
      [ $t23      <int> %ebp-68       ]
      [ $t24      <int> %ebp-72       ]
      [ $t25      <int> %ebp-76       ]
      [ $t26      <int> %ebp-80       ]
      [ $t27      <int> %ebp-84       ]
      [ $t28      <int> %ebp-88       ]
      [ $t29      <int> %ebp-92       ]
      [ $t30      <int> %ebp-96       ]
      [ $t31      <int> %ebp-100       ]
      [ $t32      <int> %ebp-104       ]
      [ $t33      <int> %ebp-108       ]
      [ $t34      <int> %ebp-112       ]
      [ $t35      <int> %ebp-116       ]
      [ $t36      <int> %ebp-120       ]
      [ $t37      <int> %ebp-124       ]
      [ $t38      <int> %ebp-128       ]
      [ $t39      <int> %ebp-132       ]
      [ $t40      <int> %ebp-136       ]
      [ $t41      <int> %ebp-140       ]
      [ $t42      <int> %ebp-144       ]
      [ $t43      <int> %ebp-148       ]
      [ $t44      <int> %ebp-152       ]
      [ $t45      <int> %ebp-156       ]
      [ $t46      <int> %ebp-160       ]
    ]]
    [[ gcd_rec
        0:     param  0 <- a
        1:     call   t12 <- DOFS
        2:     add    t13 <- 4, t12
        3:     add    t14 <- a, t13
        4:     if     @t14 = 0 goto 1_if_true
        5:     goto   2_if_false
        6: 1_if_true:
        7:     param  0 <- a
        8:     call   t16 <- DOFS
        9:     add    t17 <- 0, t16
       10:     add    t18 <- a, t17
       11:     return @t18
       12:     goto   0
       13: 2_if_false:
       14:     param  0 <- a
       15:     call   t20 <- DOFS
       16:     add    t21 <- 0, t20
       17:     add    t22 <- a, t21
       18:     assign t <- @t22
       19:     param  0 <- a
       20:     call   t24 <- DOFS
       21:     add    t25 <- 4, t24
       22:     add    t26 <- a, t25
       23:     param  0 <- a
       24:     call   t28 <- DOFS
       25:     add    t29 <- 0, t28
       26:     add    t30 <- a, t29
       27:     assign @t30 <- @t26  // *t30 = &a
       28:     param  0 <- a
       29:     call   t32 <- DOFS
       30:     add    t33 <- 4, t32
       31:     add    t34 <- a, t33
       32:     div    t35 <- t, @t34
       33:     param  0 <- a
       34:     call   t37 <- DOFS
       35:     add    t38 <- 4, t37
       36:     add    t39 <- a, t38
       37:     mul    t40 <- t35, @t39
       38:     sub    t41 <- t, t40
       39:     param  0 <- a
       40:     call   t43 <- DOFS
       41:     add    t44 <- 4, t43
       42:     add    t45 <- a, t44
       43:     assign @t45 <- t41  // *t45 = &a
       44:     param  0 <- a
       45:     call   t46 <- gcd_rec
       46:     return t46
       47: 0:
    ]]
  ]]

  [[ procedure: ReadNumbers
    [[
      [ $i        <int> %ebp-16       ]
      [ %n        <ptr(4) to <array 2 of <int>>> %ebp+8       ]
      [ $t11      <ptr(4) to <array 22 of <char>>> %ebp-20       ]
      [ $t12      <int> %ebp-24       ]
      [ $t13      <int> %ebp-28       ]
      [ $t14      <int> %ebp-32       ]
      [ $t15      <int> %ebp-36       ]
      [ $t16      <int> %ebp-40       ]
      [ $t17      <ptr(4) to <array 22 of <char>>> %ebp-44       ]
      [ $t18      <int> %ebp-48       ]
      [ $t19      <int> %ebp-52       ]
      [ $t20      <int> %ebp-56       ]
      [ $t21      <int> %ebp-60       ]
      [ $t22      <int> %ebp-64       ]
    ]]
    [[ ReadNumbers
        0:     &()    *t11 <- &_str_1
        1:     param  0 <- t11
        2:     call   WriteStr
        3:     call   t12 <- ReadInt
        4:     param  0 <- n
        5:     call   t14 <- DOFS
        6:     add    t15 <- 0, t14
        7:     add    t16 <- n, t15
        8:     assign @t16 <- t12  // *t16 = &n
        9:     &()    *t17 <- &_str_2
       10:     param  0 <- t17
       11:     call   WriteStr
       12:     call   t18 <- ReadInt
       13:     param  0 <- n
       14:     call   t20 <- DOFS
       15:     add    t21 <- 4, t20
       16:     add    t22 <- n, t21
       17:     assign @t22 <- t18  // *t22 = &n
    ]]
  ]]
]]
