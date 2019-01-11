test01_special_case.mod.const:
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
      0:     assign a <- 2
      1:     assign b <- 5
      2:     assign t0 <- 7
      3:     assign c <- 7
      4:     param  0 <- 7
      5:     call   WriteInt
      6:     assign t1 <- 10
      7:     assign c <- 10
      8:     param  0 <- 10
      9:     call   WriteInt
     10:     assign t2 <- -5
     11:     assign t3 <- -3
     12:     assign c <- -3
     13:     param  0 <- -3
     14:     call   WriteInt
     15:     assign t4 <- 10
     16:     assign c <- 10
     17:     assign t5 <- 10
     18:     param  0 <- 10
     19:     call   WriteInt
  ]]
]]
