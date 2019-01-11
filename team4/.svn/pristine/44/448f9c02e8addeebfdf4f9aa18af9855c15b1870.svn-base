test12.mod:
[[ module: test12
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
    [ *Bool() --> <bool>     ]
    [ *Char() --> <char>     ]
    [ *DIM(<ptr(4) to <NULL>>,<int>) --> <int>     ]
    [ *DOFS(<ptr(4) to <NULL>>) --> <int>     ]
    [ *Int() --> <int>     ]
    [ *ReadInt() --> <int>     ]
    [ *Test() --> <NULL>     ]
    [ *WriteChar(<char>) --> <NULL>     ]
    [ *WriteInt(<int>) --> <NULL>     ]
    [ *WriteLn() --> <NULL>     ]
    [ *WriteStr(<ptr(4) to <array of <char>>>) --> <NULL>     ]
    [ main     <NULL>     ]
  ]]
  [[ test12
      0:     call   Test
  ]]

  [[ procedure: Int
    [[
      [ $i        <int>       ]
    ]]
    [[ Int
        0:     assign i <- 75
        1:     return i
    ]]
  ]]

  [[ procedure: Char
    [[
      [ $c        <char>       ]
    ]]
    [[ Char
        0:     assign c <- 66
        1:     return c
    ]]
  ]]

  [[ procedure: Bool
    [[
      [ $b        <bool>       ]
    ]]
    [[ Bool
        0:     assign b <- 1
        1:     return b
    ]]
  ]]

  [[ procedure: Test
    [[
      [ $b        <bool>       ]
      [ $c        <char>       ]
      [ $i        <int>       ]
      [ $t0       <bool>       ]
      [ $t1       <char>       ]
      [ $t2       <int>       ]
    ]]
    [[ Test
        0:     call   t0 <- Bool
        1:     assign b <- t0
        2:     call   t1 <- Char
        3:     assign c <- t1
        4:     call   t2 <- Int
        5:     assign i <- t2
    ]]
  ]]
]]
