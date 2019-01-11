test01.mod:
[[ module: test01
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
    [ @a        <int>     ]
    [ @b        <int>     ]
    [ @c        <int>     ]
    [ main     <NULL>     ]
    [ $t0       <int>     ]
    [ $t1       <int>     ]
    [ $t2       <int>     ]
    [ $t3       <int>     ]
  ]]
  [[ test01
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
  ]]
]]
