##################################################
# test05
#

    #-----------------------------------------
    # text section
    #
    .text
    .align 4

    # entry point and pre-defined functions
    .global main
    .extern DIM
    .extern DOFS
    .extern ReadInt
    .extern WriteInt
    .extern WriteStr
    .extern WriteChar
    .extern WriteLn

    # scope test
test:
    # stack offsets:
    #      8(%ebp)   4  [ %a        <ptr(4) to <array of <int>>> %ebp+8 ]
    #    -16(%ebp)   4  [ $i        <int> %ebp-16 ]
    #    -20(%ebp)   4  [ $t1       <int> %ebp-20 ]
    #    -24(%ebp)   4  [ $t10      <int> %ebp-24 ]
    #    -28(%ebp)   4  [ $t11      <int> %ebp-28 ]
    #    -32(%ebp)   4  [ $t12      <int> %ebp-32 ]
    #    -36(%ebp)   4  [ $t13      <int> %ebp-36 ]
    #    -40(%ebp)   4  [ $t14      <int> %ebp-40 ]
    #    -44(%ebp)   4  [ $t15      <int> %ebp-44 ]
    #    -48(%ebp)   4  [ $t2       <int> %ebp-48 ]
    #    -52(%ebp)   4  [ $t3       <int> %ebp-52 ]
    #    -56(%ebp)   4  [ $t4       <int> %ebp-56 ]
    #    -60(%ebp)   4  [ $t5       <int> %ebp-60 ]
    #    -64(%ebp)   4  [ $t6       <int> %ebp-64 ]
    #    -68(%ebp)   4  [ $t7       <int> %ebp-68 ]
    #    -72(%ebp)   4  [ $t8       <int> %ebp-72 ]
    #    -76(%ebp)   4  [ $t9       <int> %ebp-76 ]

    # prologue
    pushl   %ebp                   
    movl    %esp, %ebp             
    pushl   %ebx                    # save callee saved registers
    pushl   %esi                   
    pushl   %edi                   
    subl    $64, %esp               # make room for locals

    cld                             # memset local stack area to 0
    xorl    %eax, %eax             
    movl    $16, %ecx              
    mov     %esp, %edi             
    rep     stosl                  

    # function body
    movl    8(%ebp), %eax           #   0:     param  0 <- a
    pushl   %eax                   
    call    DOFS                    #   1:     call   t2 <- DOFS
    addl    $4, %esp               
    movl    %eax, -48(%ebp)        
    movl    $0, %eax                #   2:     add    t3 <- 0, t2
    movl    -48(%ebp), %ebx        
    addl    %ebx, %eax             
    movl    %eax, -52(%ebp)        
    movl    8(%ebp), %eax           #   3:     add    t4 <- a, t3
    movl    -52(%ebp), %ebx        
    addl    %ebx, %eax             
    movl    %eax, -56(%ebp)        
    movl    $1, %eax                #   4:     assign @t4 <- 1  // *t4 = &a
    movl    -56(%ebp), %edi        
    movl    %eax, (%edi)           
    movl    $1, %eax                #   5:     assign i <- 1
    movl    %eax, -16(%ebp)        
l_test_3_while_cond:
    movl    -16(%ebp), %eax         #   7:     if     i < 10 goto 4_while_body
    movl    $10, %ebx              
    cmpl    %ebx, %eax             
    jl      l_test_4_while_body    
    jmp     l_test_2                #   8:     goto   2
l_test_4_while_body:
    movl    $10, %eax               #  10:     sub    t5 <- 10, i
    movl    -16(%ebp), %ebx        
    subl    %ebx, %eax             
    movl    %eax, -60(%ebp)        
    movl    -16(%ebp), %eax         #  11:     mul    t6 <- i, 4
    movl    $4, %ebx               
    imull   %ebx                   
    movl    %eax, -64(%ebp)        
    movl    8(%ebp), %eax           #  12:     param  0 <- a
    pushl   %eax                   
    call    DOFS                    #  13:     call   t7 <- DOFS
    addl    $4, %esp               
    movl    %eax, -68(%ebp)        
    movl    -64(%ebp), %eax         #  14:     add    t8 <- t6, t7
    movl    -68(%ebp), %ebx        
    addl    %ebx, %eax             
    movl    %eax, -72(%ebp)        
    movl    8(%ebp), %eax           #  15:     add    t9 <- a, t8
    movl    -72(%ebp), %ebx        
    addl    %ebx, %eax             
    movl    %eax, -76(%ebp)        
    movl    -60(%ebp), %eax         #  16:     assign @t9 <- t5  // *t9 = &a
    movl    -76(%ebp), %edi        
    movl    %eax, (%edi)           
    movl    -16(%ebp), %eax         #  17:     add    t10 <- i, 1
    movl    $1, %ebx               
    addl    %ebx, %eax             
    movl    %eax, -24(%ebp)        
    movl    -24(%ebp), %eax         #  18:     assign i <- t10
    movl    %eax, -16(%ebp)        
    jmp     l_test_3_while_cond     #  19:     goto   3_while_cond
l_test_2:
    movl    $0, %eax                #  21:     assign i <- 0
    movl    %eax, -16(%ebp)        
l_test_10_while_cond:
    movl    -16(%ebp), %eax         #  23:     if     i < 10 goto 11_while_body
    movl    $10, %ebx              
    cmpl    %ebx, %eax             
    jl      l_test_11_while_body   
    jmp     l_test_9                #  24:     goto   9
l_test_11_while_body:
    movl    -16(%ebp), %eax         #  26:     mul    t11 <- i, 4
    movl    $4, %ebx               
    imull   %ebx                   
    movl    %eax, -28(%ebp)        
    movl    8(%ebp), %eax           #  27:     param  0 <- a
    pushl   %eax                   
    call    DOFS                    #  28:     call   t12 <- DOFS
    addl    $4, %esp               
    movl    %eax, -32(%ebp)        
    movl    -28(%ebp), %eax         #  29:     add    t13 <- t11, t12
    movl    -32(%ebp), %ebx        
    addl    %ebx, %eax             
    movl    %eax, -36(%ebp)        
    movl    8(%ebp), %eax           #  30:     add    t14 <- a, t13
    movl    -36(%ebp), %ebx        
    addl    %ebx, %eax             
    movl    %eax, -40(%ebp)        
    movl    -40(%ebp), %edi        
    movl    (%edi), %eax            #  31:     param  0 <- @t14
    pushl   %eax                   
    call    WriteInt                #  32:     call   WriteInt
    addl    $4, %esp               
    movl    -16(%ebp), %eax         #  33:     add    t15 <- i, 1
    movl    $1, %ebx               
    addl    %ebx, %eax             
    movl    %eax, -44(%ebp)        
    movl    -44(%ebp), %eax         #  34:     assign i <- t15
    movl    %eax, -16(%ebp)        
    jmp     l_test_10_while_cond    #  35:     goto   10_while_cond
l_test_9:

l_test_exit:
    # epilogue
    addl    $64, %esp               # remove locals
    popl    %edi                   
    popl    %esi                   
    popl    %ebx                   
    popl    %ebp                   
    ret                            

    # scope test05
main:
    # stack offsets:
    #    -16(%ebp)   4  [ $t0       <ptr(4) to <array 10 of <int>>> %ebp-16 ]

    # prologue
    pushl   %ebp                   
    movl    %esp, %ebp             
    pushl   %ebx                    # save callee saved registers
    pushl   %esi                   
    pushl   %edi                   
    subl    $4, %esp                # make room for locals

    xorl    %eax, %eax              # memset local stack area to 0
    movl    %eax, 0(%esp)          

    # function body
    leal    a, %eax                 #   0:     &()    *t0 <- &a
    movl    %eax, -16(%ebp)        
    movl    -16(%ebp), %eax         #   1:     param  0 <- t0
    pushl   %eax                   
    call    test                    #   2:     call   test
    addl    $4, %esp               

l_test05_exit:
    # epilogue
    addl    $4, %esp                # remove locals
    popl    %edi                   
    popl    %esi                   
    popl    %ebx                   
    popl    %ebp                   
    ret                            

    # end of text section
    #-----------------------------------------

    #-----------------------------------------
    # global data section
    #
    .data
    .align 4

    # scope: test05
a:                                  # <array 10 of <int>>
    .long    1
    .long   10
    .skip   40


    # end of global data section
    #-----------------------------------------

    .end
##################################################