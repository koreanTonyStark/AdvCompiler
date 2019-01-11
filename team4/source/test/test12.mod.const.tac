test12.mod.const:
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

  [[ procedure: Test
    [[
      [ $b        <bool> %ebp-13       ]
      [ $c        <char> %ebp-14       ]
      [ $i        <int> %ebp-20       ]
      [ $t0       <bool> %ebp-21       ]
      [ $t1       <char> %ebp-22       ]
      [ $t2       <int> %ebp-28       ]
    ]]
    [[ Test
        0:     assign t0 <- 1
        1:     assign b <- 1
        2:     assign t1 <- 66
        3:     assign c <- 66
        4:     assign t2 <- 75
        5:     assign i <- 75
    ]]
  ]]
]]
