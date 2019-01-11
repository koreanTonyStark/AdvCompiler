test07.mod.const:
[[ module: test07
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
      <ptr(4) to <array 14 of <char>>>
    array types:
      <array of <char>>
      <array 14 of <char>>
  ]]
  [[
    [ *DIM(<ptr(4) to <NULL>>,<int>) --> <int>     ]
    [ *DOFS(<ptr(4) to <NULL>>) --> <int>     ]
    [ *ReadInt() --> <int>     ]
    [ *WriteChar(<char>) --> <NULL>     ]
    [ *WriteInt(<int>) --> <NULL>     ]
    [ *WriteLn() --> <NULL>     ]
    [ *WriteStr(<ptr(4) to <array of <char>>>) --> <NULL>     ]
    [ @_str_1   <array 14 of <char>>     ]
      [ data: 'Hello, world!' ]
    [ main     <NULL>     ]
    [ $t0       <ptr(4) to <array 14 of <char>>> %ebp-16     ]
  ]]
  [[ test07
      0:     &()    *t0 <- &_str_1
      1:     param  0 <- t0
      2:     call   WriteStr
      3:     call   WriteLn
  ]]
]]
