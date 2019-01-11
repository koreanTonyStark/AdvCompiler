test11.mod.const:
[[ module: test11
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
      <array 10 of <int>>
      <array 7 of <char>>
  ]]
  [[
    [ @A        <int>     ]
    [ @B        <bool>     ]
    [ @C        <int>     ]
    [ @D        <char>     ]
    [ *DIM(<ptr(4) to <NULL>>,<int>) --> <int>     ]
    [ *DOFS(<ptr(4) to <NULL>>) --> <int>     ]
    [ @E        <int>     ]
    [ @F        <bool>     ]
    [ @G        <array 10 of <int>>     ]
    [ @H        <bool>     ]
    [ @I        <array 7 of <char>>     ]
    [ @J        <int>     ]
    [ *ReadInt() --> <int>     ]
    [ *WriteChar(<char>) --> <NULL>     ]
    [ *WriteInt(<int>) --> <NULL>     ]
    [ *WriteLn() --> <NULL>     ]
    [ *WriteStr(<ptr(4) to <array of <char>>>) --> <NULL>     ]
    [ *foo() --> <NULL>     ]
    [ main     <NULL>     ]
  ]]
  [[ test11
  ]]

  [[ procedure: foo
    [[
      [ $a        <int> %ebp-16       ]
      [ $b        <bool> %ebp-17       ]
      [ $c        <int> %ebp-24       ]
      [ $d        <char> %ebp-25       ]
      [ $e        <int> %ebp-32       ]
      [ $f        <bool> %ebp-33       ]
      [ $g        <array 10 of <int>> %ebp-84       ]
      [ $h        <bool> %ebp-85       ]
      [ $i        <array 7 of <char>> %ebp-100       ]
      [ $j        <int> %ebp-104       ]
    ]]
    [[ foo
    ]]
  ]]
]]
