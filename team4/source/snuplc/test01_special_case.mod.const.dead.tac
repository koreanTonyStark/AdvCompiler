test01_special_case.mod.const.dead:
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
    [ $t0       <int> %ebp-16     ]
    [ $t1       <int> %ebp-20     ]
    [ $t2       <int> %ebp-24     ]
    [ $t3       <int> %ebp-28     ]
    [ $t4       <int> %ebp-32     ]
    [ $t5       <int> %ebp-36     ]
  ]]
  [[ test01_special_case
      0:     param  0 <- 7
      1:     call   WriteInt
      2:     param  0 <- 10
      3:     call   WriteInt
      4:     param  0 <- -3
      5:     call   WriteInt
      6:     param  0 <- 10
      7:     call   WriteInt
  ]]
]]