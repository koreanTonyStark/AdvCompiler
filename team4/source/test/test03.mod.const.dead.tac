test03.mod.const.dead:
[[ module: test03
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
    [ *WriteChar(<char>) --> <NULL>     ]
    [ *WriteInt(<int>) --> <NULL>     ]
    [ *WriteLn() --> <NULL>     ]
    [ *WriteStr(<ptr(4) to <array of <char>>>) --> <NULL>     ]
    [ @a        <bool>     ]
    [ @b        <bool>     ]
    [ @b1       <int>     ]
    [ @c        <bool>     ]
    [ main     <NULL>     ]
    [ $t0       <bool> %ebp-13     ]
    [ $t1       <bool> %ebp-14     ]
    [ $t2       <bool> %ebp-15     ]
  ]]
  [[ test03
      0:     if     1 = 1 goto 6
      1:     goto   4
      2: 6:
      3:     if     0 = 1 goto 3
      4:     goto   4
      5: 3:
      6:     assign t0 <- 1
      7:     goto   5
      8: 4:
      9:     assign t0 <- 0
     10: 5:
     11:     assign c <- t0
     12:     if     c = 1 goto 8_if_true
     13:     goto   9_if_false
     14: 8_if_true:
     15:     param  0 <- 1
     16:     call   WriteInt
     17:     goto   7
     18: 9_if_false:
     19:     param  0 <- 0
     20:     call   WriteInt
     21: 7:
     22:     if     1 = 1 goto 13
     23:     if     0 = 1 goto 13
     24:     goto   14
     25: 13:
     26:     assign t1 <- 1
     27:     goto   15
     28: 14:
     29:     assign t1 <- 0
     30: 15:
     31:     assign c <- t1
     32:     if     c = 1 goto 18_if_true
     33:     goto   19_if_false
     34: 18_if_true:
     35:     param  0 <- 1
     36:     call   WriteInt
     37:     goto   17
     38: 19_if_false:
     39:     param  0 <- 0
     40:     call   WriteInt
     41: 17:
     42:     if     1 = 1 goto 24
     43:     if     0 = 1 goto 24
     44:     assign t2 <- 1
     45:     goto   25
     46: 24:
     47:     assign t2 <- 0
     48: 25:
     49:     assign c <- t2
     50:     if     c = 1 goto 28_if_true
     51:     goto   29_if_false
     52: 28_if_true:
     53:     param  0 <- 1
     54:     call   WriteInt
     55:     goto   27
     56: 29_if_false:
     57:     param  0 <- 0
     58:     call   WriteInt
     59: 27:
  ]]
]]
