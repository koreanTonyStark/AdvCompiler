test04.mod:
[[ module: test04
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
      <ptr(4) to <array 10 of <bool>>>
    array types:
      <array of <char>>
      <array 10 of <bool>>
  ]]
  [[
    [ *DIM(<ptr(4) to <NULL>>,<int>) --> <int>     ]
    [ *DOFS(<ptr(4) to <NULL>>) --> <int>     ]
    [ *ReadInt() --> <int>     ]
    [ *WriteChar(<char>) --> <NULL>     ]
    [ *WriteInt(<int>) --> <NULL>     ]
    [ *WriteLn() --> <NULL>     ]
    [ *WriteStr(<ptr(4) to <array of <char>>>) --> <NULL>     ]
    [ @a        <array 10 of <bool>>     ]
    [ @i        <int>     ]
    [ main     <NULL>     ]
    [ $t0       <bool>     ]
    [ $t1       <ptr(4) to <array 10 of <bool>>>     ]
    [ $t10      <ptr(4) to <array 10 of <bool>>>     ]
    [ $t11      <int>     ]
    [ $t12      <int>     ]
    [ $t13      <int>     ]
    [ $t14      <int>     ]
    [ $t2       <int>     ]
    [ $t3       <ptr(4) to <array 10 of <bool>>>     ]
    [ $t4       <int>     ]
    [ $t5       <int>     ]
    [ $t6       <int>     ]
    [ $t7       <int>     ]
    [ $t8       <ptr(4) to <array 10 of <bool>>>     ]
    [ $t9       <int>     ]
  ]]
  [[ test04
      0:     assign i <- 0
      1: 2_while_cond:
      2:     if     i < 10 goto 3_while_body
      3:     goto   1
      4: 3_while_body:
      5:     if     i > 2 goto 6
      6:     goto   7
      7: 6:
      8:     assign t0 <- 1
      9:     goto   8
     10: 7:
     11:     assign t0 <- 0
     12: 8:
     13:     &()    *t1 <- &a
     14:     mul    t2 <- i, 1
     15:     &()    *t3 <- &a
     16:     param  0 <- t3
     17:     call   t4 <- DOFS
     18:     add    t5 <- t2, t4
     19:     add    t6 <- t1, t5
     20:     assign @t6 <- t0  // *t6 = &a
     21:     add    t7 <- i, 1
     22:     assign i <- t7
     23:     goto   2_while_cond
     24: 1:
     25:     assign i <- 0
     26: 13_while_cond:
     27:     if     i < 10 goto 14_while_body
     28:     goto   12
     29: 14_while_body:
     30:     &()    *t8 <- &a
     31:     mul    t9 <- i, 1
     32:     &()    *t10 <- &a
     33:     param  0 <- t10
     34:     call   t11 <- DOFS
     35:     add    t12 <- t9, t11
     36:     add    t13 <- t8, t12
     37:     if     @t13 = 1 goto 17_if_true
     38:     goto   18_if_false
     39: 17_if_true:
     40:     param  0 <- 1
     41:     call   WriteInt
     42:     goto   16
     43: 18_if_false:
     44:     param  0 <- 0
     45:     call   WriteInt
     46: 16:
     47:     add    t14 <- i, 1
     48:     assign i <- t14
     49:     goto   13_while_cond
     50: 12:
  ]]
]]
