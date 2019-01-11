test08.mod:
[[ module: test08
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
      <ptr(4) to <array 10 of <int>>>
    array types:
      <array of <char>>
      <array 10 of <int>>
  ]]
  [[
    [ *DIM(<ptr(4) to <NULL>>,<int>) --> <int>     ]
    [ *DOFS(<ptr(4) to <NULL>>) --> <int>     ]
    [ *ReadInt() --> <int>     ]
    [ *WriteChar(<char>) --> <NULL>     ]
    [ *WriteInt(<int>) --> <NULL>     ]
    [ *WriteLn() --> <NULL>     ]
    [ *WriteStr(<ptr(4) to <array of <char>>>) --> <NULL>     ]
    [ main     <NULL>     ]
    [ *test() --> <NULL>     ]
  ]]
  [[ test08
      0:     call   test
  ]]

  [[ procedure: test
    [[
      [ $a        <array 10 of <int>>       ]
      [ $i        <int>       ]
      [ $t0       <ptr(4) to <array 10 of <int>>>       ]
      [ $t1       <int>       ]
      [ $t10      <int>       ]
      [ $t11      <int>       ]
      [ $t12      <int>       ]
      [ $t13      <int>       ]
      [ $t14      <ptr(4) to <array 10 of <int>>>       ]
      [ $t15      <int>       ]
      [ $t16      <ptr(4) to <array 10 of <int>>>       ]
      [ $t17      <int>       ]
      [ $t18      <int>       ]
      [ $t19      <int>       ]
      [ $t2       <ptr(4) to <array 10 of <int>>>       ]
      [ $t20      <int>       ]
      [ $t3       <int>       ]
      [ $t4       <int>       ]
      [ $t5       <int>       ]
      [ $t6       <int>       ]
      [ $t7       <ptr(4) to <array 10 of <int>>>       ]
      [ $t8       <int>       ]
      [ $t9       <ptr(4) to <array 10 of <int>>>       ]
    ]]
    [[ test
        0:     &()    *t0 <- &a
        1:     mul    t1 <- 0, 4
        2:     &()    *t2 <- &a
        3:     param  0 <- t2
        4:     call   t3 <- DOFS
        5:     add    t4 <- t1, t3
        6:     add    t5 <- t0, t4
        7:     assign @t5 <- 1  // *t5 = &a
        8:     assign i <- 1
        9: 3_while_cond:
       10:     if     i < 10 goto 4_while_body
       11:     goto   2
       12: 4_while_body:
       13:     sub    t6 <- 10, i
       14:     &()    *t7 <- &a
       15:     mul    t8 <- i, 4
       16:     &()    *t9 <- &a
       17:     param  0 <- t9
       18:     call   t10 <- DOFS
       19:     add    t11 <- t8, t10
       20:     add    t12 <- t7, t11
       21:     assign @t12 <- t6  // *t12 = &a
       22:     add    t13 <- i, 1
       23:     assign i <- t13
       24:     goto   3_while_cond
       25: 2:
       26:     assign i <- 0
       27: 10_while_cond:
       28:     if     i < 10 goto 11_while_body
       29:     goto   9
       30: 11_while_body:
       31:     &()    *t14 <- &a
       32:     mul    t15 <- i, 4
       33:     &()    *t16 <- &a
       34:     param  0 <- t16
       35:     call   t17 <- DOFS
       36:     add    t18 <- t15, t17
       37:     add    t19 <- t14, t18
       38:     param  0 <- @t19
       39:     call   WriteInt
       40:     add    t20 <- i, 1
       41:     assign i <- t20
       42:     goto   10_while_cond
       43: 9:
    ]]
  ]]
]]
