factorial.mod.const:
[[ module: factorial
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
      <ptr(4) to <array 11 of <char>>>
      <ptr(4) to <array 29 of <char>>>
      <ptr(4) to <array 5 of <char>>>
    array types:
      <array of <char>>
      <array 11 of <char>>
      <array 29 of <char>>
      <array 5 of <char>>
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
    [ @_str_1   <array 11 of <char>>     ]
      [ data: 'Factorials' ]
    [ @_str_2   <array 29 of <char>>     ]
      [ data: 'Enter a number (0 to exit): ' ]
    [ @_str_3   <array 11 of <char>>     ]
      [ data: 'factorial(' ]
    [ @_str_4   <array 5 of <char>>     ]
      [ data: ') = ' ]
    [ @_str_5   <array 29 of <char>>     ]
      [ data: 'Enter a number (0 to exit): ' ]
    [ *fact(<int>) --> <int>     ]
    [ @i        <int>     ]
    [ main     <NULL>     ]
    [ $t0       <ptr(4) to <array 11 of <char>>> %ebp-16     ]
    [ $t1       <ptr(4) to <array 29 of <char>>> %ebp-20     ]
    [ $t2       <int> %ebp-24     ]
    [ $t3       <ptr(4) to <array 11 of <char>>> %ebp-28     ]
    [ $t4       <ptr(4) to <array 5 of <char>>> %ebp-32     ]
    [ $t5       <int> %ebp-36     ]
    [ $t6       <ptr(4) to <array 29 of <char>>> %ebp-40     ]
    [ $t7       <int> %ebp-44     ]
  ]]
  [[ factorial
      0:     &()    *t0 <- &_str_1
      1:     param  0 <- t0
      2:     call   WriteStr
      3:     call   WriteLn
      4:     call   WriteLn
      5:     &()    *t1 <- &_str_2
      6:     param  0 <- t1
      7:     call   t2 <- ReadNumber
      8:     assign i <- t2
      9: 5_while_cond:
     10:     if     i > 0 goto 6_while_body
     11:     goto   4
     12: 6_while_body:
     13:     &()    *t3 <- &_str_3
     14:     param  0 <- t3
     15:     call   WriteStr
     16:     param  0 <- i
     17:     call   WriteInt
     18:     &()    *t4 <- &_str_4
     19:     param  0 <- t4
     20:     call   WriteStr
     21:     param  0 <- i
     22:     call   t5 <- fact
     23:     param  0 <- t5
     24:     call   WriteInt
     25:     call   WriteLn
     26:     &()    *t6 <- &_str_5
     27:     param  0 <- t6
     28:     call   t7 <- ReadNumber
     29:     assign i <- t7
     30:     goto   5_while_cond
     31: 4:
  ]]

  [[ procedure: fact
    [[
      [ %n        <int> %ebp+8       ]
      [ $t10      <int> %ebp-16       ]
      [ $t8       <int> %ebp-20       ]
      [ $t9       <int> %ebp-24       ]
    ]]
    [[ fact
        0:     if     n <= 0 goto 1_if_true
        1:     goto   2_if_false
        2: 1_if_true:
        3:     return 0
        4:     goto   0
        5: 2_if_false:
        6:     if     n <= 1 goto 6_if_true
        7:     goto   7_if_false
        8: 6_if_true:
        9:     return n
       10:     goto   5
       11: 7_if_false:
       12:     sub    t8 <- n, 1
       13:     param  0 <- t8
       14:     call   t9 <- fact
       15:     mul    t10 <- n, t9
       16:     return t10
       17: 5:
       18: 0:
    ]]
  ]]

  [[ procedure: ReadNumber
    [[
      [ $i        <int> %ebp-16       ]
      [ %str      <ptr(4) to <array of <char>>> %ebp+8       ]
      [ $t8       <int> %ebp-20       ]
    ]]
    [[ ReadNumber
        0:     param  0 <- str
        1:     call   WriteStr
        2:     call   t8 <- ReadInt
        3:     assign i <- t8
        4:     return t8
    ]]
  ]]
]]
