test01_special_case.mod:
[[ module: test01_special_case
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
    array types:
      <array of <char>>
  ]]
  [[
    [ *DIM(<ptr(4) to <NULL>>,<int>) --> <int>     ]
    [ *DOFS(<ptr(4) to <NULL>>) --> <int>     ]
    [ *ReadInt() --> <int>     ]
    [ *Tmp(<int>) --> <int>     ]
    [ *WriteChar(<char>) --> <NULL>     ]
    [ *WriteInt(<int>) --> <NULL>     ]
    [ *WriteLn() --> <NULL>     ]
    [ *WriteStr(<ptr(4) to <array of <char>>>) --> <NULL>     ]
    [ @a        <int>     ]
    [ @b        <int>     ]
    [ @c        <int>     ]
    [ main     <NULL>     ]
    [ $t0       <int>     ]
    [ $t1       <int>     ]
    [ $t2       <int>     ]
    [ $t3       <int>     ]
    [ $t4       <int>     ]
    [ $t5       <int>     ]
  ]]
  [[ test01_special_case
      0:     assign a <- 2
      1:     assign b <- 5
      2:     add    t0 <- a, b
      3:     assign c <- t0
      4:     param  0 <- c
      5:     call   WriteInt
      6:     mul    t1 <- a, b
      7:     assign c <- t1
      8:     param  0 <- c
      9:     call   WriteInt
     10:     neg    t2 <- b
     11:     add    t3 <- t2, a
     12:     assign c <- t3
     13:     param  0 <- c
     14:     call   WriteInt
     15:     param  0 <- 1
     16:     call   t4 <- Tmp
     17:     assign c <- t4
     18:     param  0 <- 1
     19:     call   t5 <- Tmp
     20:     param  0 <- t5
     21:     call   WriteInt
  ]]

  [[ procedure: Tmp
    [[
      [ %n        <int>       ]
    ]]
    [[ Tmp
        0:     if     n > 0 goto 1_if_true
        1:     goto   2_if_false
        2: 1_if_true:
        3:     return 10
        4:     goto   0
        5: 2_if_false:
        6:     return 10
        7: 0:
    ]]
  ]]
]]
