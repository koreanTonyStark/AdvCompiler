test02.mod.const.dead:
[[ module: test02
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
      <array 2 of <bool>>
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
    [ @b        <bool>     ]
    [ @c        <array 2 of <bool>>     ]
    [ @i        <int>     ]
    [ main     <NULL>     ]
    [ $t0       <ptr(4) to <array 10 of <int>>> %ebp-16     ]
    [ $t1       <int> %ebp-20     ]
    [ $t10      <int> %ebp-24     ]
    [ $t11      <int> %ebp-28     ]
    [ $t12      <int> %ebp-32     ]
    [ $t13      <int> %ebp-36     ]
    [ $t14      <ptr(4) to <array 10 of <int>>> %ebp-40     ]
    [ $t15      <int> %ebp-44     ]
    [ $t16      <ptr(4) to <array 10 of <int>>> %ebp-48     ]
    [ $t17      <int> %ebp-52     ]
    [ $t18      <int> %ebp-56     ]
    [ $t19      <int> %ebp-60     ]
    [ $t2       <ptr(4) to <array 10 of <int>>> %ebp-64     ]
    [ $t20      <int> %ebp-68     ]
    [ $t3       <int> %ebp-72     ]
    [ $t4       <int> %ebp-76     ]
    [ $t5       <int> %ebp-80     ]
    [ $t6       <int> %ebp-84     ]
    [ $t7       <ptr(4) to <array 10 of <int>>> %ebp-88     ]
    [ $t8       <int> %ebp-92     ]
    [ $t9       <ptr(4) to <array 10 of <int>>> %ebp-96     ]
  ]]
  [[ test02
      0:     &()    *t0 <- &a
      1:     &()    *t2 <- &a
      2:     param  0 <- t2
      3:     call   t3 <- DOFS
      4:     add    t4 <- 0, t3
      5:     add    t5 <- t0, t4
      6:     assign @t5 <- 1  // *t5 = &a
      7:     assign i <- 1
      8: 3_while_cond:
      9:     if     i < 10 goto 4_while_body
     10:     goto   2
     11: 4_while_body:
     12:     sub    t6 <- 10, i
     13:     &()    *t7 <- &a
     14:     mul    t8 <- i, 4
     15:     &()    *t9 <- &a
     16:     param  0 <- t9
     17:     call   t10 <- DOFS
     18:     add    t11 <- t8, t10
     19:     add    t12 <- t7, t11
     20:     assign @t12 <- t6  // *t12 = &a
     21:     add    t13 <- i, 1
     22:     assign i <- t13
     23:     goto   3_while_cond
     24: 2:
     25:     assign i <- 0
     26: 10_while_cond:
     27:     if     i < 10 goto 11_while_body
     28:     goto   9
     29: 11_while_body:
     30:     &()    *t14 <- &a
     31:     mul    t15 <- i, 4
     32:     &()    *t16 <- &a
     33:     param  0 <- t16
     34:     call   t17 <- DOFS
     35:     add    t18 <- t15, t17
     36:     add    t19 <- t14, t18
     37:     param  0 <- @t19
     38:     call   WriteInt
     39:     add    t20 <- i, 1
     40:     assign i <- t20
     41:     goto   10_while_cond
     42: 9:
  ]]
]]
