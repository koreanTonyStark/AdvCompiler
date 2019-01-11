test05.mod.const.dead:
[[ module: test05
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
      <ptr(4) to <array 10 of <int>>>
    array types:
      <array of <char>>
      <array 10 of <int>>
      <array of <int>>
  ]]
  [[
    [ *DIM(<ptr(4) to <NULL>>,<int>) --> <int>     ]
    [ *DOFS(<ptr(4) to <NULL>>) --> <int>     ]
    [ *ReadInt() --> <int>     ]
    [ *WriteChar(<char>) --> <NULL>     ]
    [ *WriteInt(<int>) --> <NULL>     ]
    [ *WriteLn() --> <NULL>     ]
    [ *WriteStr(<ptr(4) to <array of <char>>>) --> <NULL>     ]
    [ @a        <array 10 of <int>>     ]
    [ main     <NULL>     ]
    [ $t0       <ptr(4) to <array 10 of <int>>> %ebp-16     ]
    [ *test(<ptr(4) to <array of <int>>>) --> <NULL>     ]
  ]]
  [[ test05
      0:     &()    *t0 <- &a
      1:     param  0 <- t0
      2:     call   test
  ]]

  [[ procedure: test
    [[
      [ %a        <ptr(4) to <array of <int>>> %ebp+8       ]
      [ $i        <int> %ebp-16       ]
      [ $t1       <int> %ebp-20       ]
      [ $t10      <int> %ebp-24       ]
      [ $t11      <int> %ebp-28       ]
      [ $t12      <int> %ebp-32       ]
      [ $t13      <int> %ebp-36       ]
      [ $t14      <int> %ebp-40       ]
      [ $t15      <int> %ebp-44       ]
      [ $t2       <int> %ebp-48       ]
      [ $t3       <int> %ebp-52       ]
      [ $t4       <int> %ebp-56       ]
      [ $t5       <int> %ebp-60       ]
      [ $t6       <int> %ebp-64       ]
      [ $t7       <int> %ebp-68       ]
      [ $t8       <int> %ebp-72       ]
      [ $t9       <int> %ebp-76       ]
    ]]
    [[ test
        0:     param  0 <- a
        1:     call   t2 <- DOFS
        2:     add    t3 <- 0, t2
        3:     add    t4 <- a, t3
        4:     assign @t4 <- 1  // *t4 = &a
        5:     assign i <- 1
        6: 3_while_cond:
        7:     if     i < 10 goto 4_while_body
        8:     goto   2
        9: 4_while_body:
       10:     sub    t5 <- 10, i
       11:     mul    t6 <- i, 4
       12:     param  0 <- a
       13:     call   t7 <- DOFS
       14:     add    t8 <- t6, t7
       15:     add    t9 <- a, t8
       16:     assign @t9 <- t5  // *t9 = &a
       17:     add    t10 <- i, 1
       18:     assign i <- t10
       19:     goto   3_while_cond
       20: 2:
       21:     assign i <- 0
       22: 10_while_cond:
       23:     if     i < 10 goto 11_while_body
       24:     goto   9
       25: 11_while_body:
       26:     mul    t11 <- i, 4
       27:     param  0 <- a
       28:     call   t12 <- DOFS
       29:     add    t13 <- t11, t12
       30:     add    t14 <- a, t13
       31:     param  0 <- @t14
       32:     call   WriteInt
       33:     add    t15 <- i, 1
       34:     assign i <- t15
       35:     goto   10_while_cond
       36: 9:
    ]]
  ]]
]]
