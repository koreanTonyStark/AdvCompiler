pfact.mod:
[[ module: pfact
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
      <ptr(4) to <array 16 of <char>>>
      <ptr(4) to <array 25 of <char>>>
      <ptr(4) to <array 20 of <char>>>
      <ptr(4) to <array 3 of <char>>>
      <ptr(4) to <array 2 of <char>>>
    array types:
      <array of <char>>
      <array 2 of <char>>
      <array 16 of <char>>
      <array 25 of <char>>
      <array 20 of <char>>
      <array 3 of <char>>
  ]]
  [[
    [ *DIM(<ptr(4) to <NULL>>,<int>) --> <int>     ]
    [ *DOFS(<ptr(4) to <NULL>>) --> <int>     ]
    [ *ReadInt() --> <int>     ]
    [ *WriteChar(<char>) --> <NULL>     ]
    [ *WriteInt(<int>) --> <NULL>     ]
    [ *WriteLn() --> <NULL>     ]
    [ *WriteStr(<ptr(4) to <array of <char>>>) --> <NULL>     ]
    [ @_str_1   <array 2 of <char>>     ]
      [ data: ' ' ]
    [ @_str_2   <array 2 of <char>>     ]
      [ data: ' ' ]
    [ @_str_3   <array 16 of <char>>     ]
      [ data: 'Prime factoring' ]
    [ @_str_4   <array 25 of <char>>     ]
      [ data: 'Enter number to factor: ' ]
    [ @_str_5   <array 20 of <char>>     ]
      [ data: '  prime factors of ' ]
    [ @_str_6   <array 3 of <char>>     ]
      [ data: ': ' ]
    [ main     <NULL>     ]
    [ @n        <int>     ]
    [ *primefactor(<int>) --> <NULL>     ]
    [ $t0       <ptr(4) to <array 16 of <char>>>     ]
    [ $t1       <ptr(4) to <array 25 of <char>>>     ]
    [ $t2       <int>     ]
    [ $t3       <ptr(4) to <array 20 of <char>>>     ]
    [ $t4       <ptr(4) to <array 3 of <char>>>     ]
  ]]
  [[ pfact
      0:     &()    *t0 <- &_str_3
      1:     param  0 <- t0
      2:     call   WriteStr
      3:     call   WriteLn
      4:     call   WriteLn
      5:     &()    *t1 <- &_str_4
      6:     param  0 <- t1
      7:     call   WriteStr
      8:     call   t2 <- ReadInt
      9:     assign n <- t2
     10:     &()    *t3 <- &_str_5
     11:     param  0 <- t3
     12:     call   WriteStr
     13:     param  0 <- n
     14:     call   WriteInt
     15:     &()    *t4 <- &_str_6
     16:     param  0 <- t4
     17:     call   WriteStr
     18:     param  0 <- n
     19:     call   primefactor
     20:     call   WriteLn
  ]]

  [[ procedure: primefactor
    [[
      [ $f        <int>       ]
      [ %n        <int>       ]
      [ $t10      <int>       ]
      [ $t5       <ptr(4) to <array 2 of <char>>>       ]
      [ $t6       <int>       ]
      [ $t7       <int>       ]
      [ $t8       <ptr(4) to <array 2 of <char>>>       ]
      [ $t9       <int>       ]
    ]]
    [[ primefactor
        0:     if     n < 1 goto 1_if_true
        1:     goto   2_if_false
        2: 1_if_true:
        3:     return 
        4:     goto   0
        5: 2_if_false:
        6:     if     n = 1 goto 6_if_true
        7:     goto   7_if_false
        8: 6_if_true:
        9:     &()    *t5 <- &_str_1
       10:     param  0 <- t5
       11:     call   WriteStr
       12:     param  0 <- 1
       13:     call   WriteInt
       14:     goto   5
       15: 7_if_false:
       16:     assign f <- 2
       17: 13_while_cond:
       18:     if     f <= n goto 14_while_body
       19:     goto   12
       20: 14_while_body:
       21:     div    t6 <- n, f
       22:     mul    t7 <- t6, f
       23:     if     t7 = n goto 17_if_true
       24:     goto   18_if_false
       25: 17_if_true:
       26:     &()    *t8 <- &_str_2
       27:     param  0 <- t8
       28:     call   WriteStr
       29:     param  0 <- f
       30:     call   WriteInt
       31:     div    t9 <- n, f
       32:     assign n <- t9
       33:     goto   16
       34: 18_if_false:
       35:     add    t10 <- f, 1
       36:     assign f <- t10
       37: 16:
       38:     goto   13_while_cond
       39: 12:
       40: 5:
       41: 0:
    ]]
  ]]
]]
