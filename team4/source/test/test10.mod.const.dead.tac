test10.mod.const.dead:
[[ module: test10
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
      <ptr(4) to <array 25 of <char>>>
      <ptr(4) to <array 29 of <char>>>
      <ptr(4) to <array 16 of <char>>>
    array types:
      <array of <char>>
      <array 25 of <char>>
      <array 29 of <char>>
      <array 16 of <char>>
  ]]
  [[
    [ *DIM(<ptr(4) to <NULL>>,<int>) --> <int>     ]
    [ *DOFS(<ptr(4) to <NULL>>) --> <int>     ]
    [ *ReadInt() --> <int>     ]
    [ *ReadNumber(<ptr(4) to <array of <char>>>) --> <int>     ]
    [ *WriteChar(<char>) --> <NULL>     ]
    [ *WriteInt(<int>) --> <NULL>     ]
    [ *WriteLn() --> <NULL>     ]
    [ *WriteStr(<ptr(4) to <array of <char>>>) --> <NULL>     ]
    [ @_str_1   <array 25 of <char>>     ]
      [ data: 'Sum of natural numbers\n\n' ]
    [ @_str_2   <array 29 of <char>>     ]
      [ data: 'Enter a number (0 to exit): ' ]
    [ @_str_3   <array 16 of <char>>     ]
      [ data: ' recursive   : ' ]
    [ @_str_4   <array 16 of <char>>     ]
      [ data: ' iterative   : ' ]
    [ @_str_5   <array 16 of <char>>     ]
      [ data: ' algorithmic : ' ]
    [ @_str_6   <array 29 of <char>>     ]
      [ data: 'Enter a number (0 to exit): ' ]
    [ @i        <int>     ]
    [ main     <NULL>     ]
    [ *sum_alg(<int>) --> <int>     ]
    [ *sum_iter(<int>) --> <int>     ]
    [ *sum_rec(<int>) --> <int>     ]
    [ $t0       <ptr(4) to <array 25 of <char>>> %ebp-16     ]
    [ $t1       <ptr(4) to <array 29 of <char>>> %ebp-20     ]
    [ $t10      <int> %ebp-24     ]
    [ $t2       <int> %ebp-28     ]
    [ $t3       <ptr(4) to <array 16 of <char>>> %ebp-32     ]
    [ $t4       <int> %ebp-36     ]
    [ $t5       <ptr(4) to <array 16 of <char>>> %ebp-40     ]
    [ $t6       <int> %ebp-44     ]
    [ $t7       <ptr(4) to <array 16 of <char>>> %ebp-48     ]
    [ $t8       <int> %ebp-52     ]
    [ $t9       <ptr(4) to <array 29 of <char>>> %ebp-56     ]
  ]]
  [[ test10
      0:     &()    *t0 <- &_str_1
      1:     param  0 <- t0
      2:     call   WriteStr
      3:     &()    *t1 <- &_str_2
      4:     param  0 <- t1
      5:     call   t2 <- ReadNumber
      6:     assign i <- t2
      7: 3_while_cond:
      8:     if     i > 0 goto 4_while_body
      9:     goto   2
     10: 4_while_body:
     11:     &()    *t3 <- &_str_3
     12:     param  0 <- t3
     13:     call   WriteStr
     14:     param  0 <- i
     15:     call   t4 <- sum_rec
     16:     param  0 <- t4
     17:     call   WriteInt
     18:     call   WriteLn
     19:     &()    *t5 <- &_str_4
     20:     param  0 <- t5
     21:     call   WriteStr
     22:     param  0 <- i
     23:     call   t6 <- sum_iter
     24:     param  0 <- t6
     25:     call   WriteInt
     26:     call   WriteLn
     27:     &()    *t7 <- &_str_5
     28:     param  0 <- t7
     29:     call   WriteStr
     30:     param  0 <- i
     31:     call   t8 <- sum_alg
     32:     param  0 <- t8
     33:     call   WriteInt
     34:     call   WriteLn
     35:     &()    *t9 <- &_str_6
     36:     param  0 <- t9
     37:     call   t10 <- ReadNumber
     38:     assign i <- t10
     39:     goto   3_while_cond
     40: 2:
  ]]

  [[ procedure: sum_rec
    [[
      [ %n        <int> %ebp+8       ]
      [ $t11      <int> %ebp-16       ]
      [ $t12      <int> %ebp-20       ]
      [ $t13      <int> %ebp-24       ]
    ]]
    [[ sum_rec
        0:     if     n > 0 goto 1_if_true
        1:     goto   2_if_false
        2: 1_if_true:
        3:     sub    t11 <- n, 1
        4:     param  0 <- t11
        5:     call   t12 <- sum_rec
        6:     add    t13 <- n, t12
        7:     return t13
        8:     goto   0
        9: 2_if_false:
       10:     return 0
       11: 0:
    ]]
  ]]

  [[ procedure: sum_iter
    [[
      [ $i        <int> %ebp-16       ]
      [ %n        <int> %ebp+8       ]
      [ $sum      <int> %ebp-20       ]
      [ $t11      <int> %ebp-24       ]
      [ $t12      <int> %ebp-28       ]
    ]]
    [[ sum_iter
        0:     assign sum <- 0
        1:     assign i <- 0
        2: 3_while_cond:
        3:     if     i <= n goto 4_while_body
        4:     goto   2
        5: 4_while_body:
        6:     add    t11 <- sum, i
        7:     assign sum <- t11
        8:     add    t12 <- i, 1
        9:     assign i <- t12
       10:     goto   3_while_cond
       11: 2:
       12:     return sum
    ]]
  ]]

  [[ procedure: sum_alg
    [[
      [ %n        <int> %ebp+8       ]
      [ $t11      <int> %ebp-16       ]
      [ $t12      <int> %ebp-20       ]
      [ $t13      <int> %ebp-24       ]
    ]]
    [[ sum_alg
        0:     add    t11 <- n, 1
        1:     mul    t12 <- n, t11
        2:     div    t13 <- t12, 2
        3:     return t13
    ]]
  ]]

  [[ procedure: ReadNumber
    [[
      [ $i        <int> %ebp-16       ]
      [ %str      <ptr(4) to <array of <char>>> %ebp+8       ]
      [ $t11      <int> %ebp-20       ]
    ]]
    [[ ReadNumber
        0:     param  0 <- str
        1:     call   WriteStr
        2:     call   t11 <- ReadInt
        3:     return t11
    ]]
  ]]
]]
