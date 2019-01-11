##################################################
# test01_special_case
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

    # scope Tmp
Tmp:
    # stack offsets:
    #      8(%ebp)   4  [ %n        <int> %ebp+8 ]

    # prologue
    pushl   %ebp                   
    movl    %esp, %ebp             
    pushl   %ebx                    # save callee saved registers
    pushl   %esi                   
    pushl   %edi                   
    subl    $0, %esp                # make room for locals

    # function body
    movl    8(%ebp), %eax           #   0:     if     n > 0 goto 1_if_true
    movl    $0, %ebx               
    cmpl    %ebx, %eax             
    jg      l_Tmp_1_if_true        
    jmp     l_Tmp_2_if_false        #   1:     goto   2_if_false
l_Tmp_1_if_true:
    movl    $10, %eax               #   3:     return 10
    jmp     l_Tmp_exit             
    jmp     l_Tmp_0                 #   4:     goto   0
l_Tmp_2_if_false:
    movl    $10, %eax               #   6:     return 10
    jmp     l_Tmp_exit             
l_Tmp_0:

l_Tmp_exit:
    # epilogue
    addl    $0, %esp                # remove locals
    popl    %edi                   
    popl    %esi                   
    popl    %ebx                   
    popl    %ebp                   
    ret                            

    # scope test01_special_case
main:
    # stack offsets:
    #    -16(%ebp)   4  [ $t0       <int> %ebp-16 ]
    #    -20(%ebp)   4  [ $t1       <int> %ebp-20 ]
    #    -24(%ebp)   4  [ $t2       <int> %ebp-24 ]
    #    -28(%ebp)   4  [ $t3       <int> %ebp-28 ]
    #    -32(%ebp)   4  [ $t4       <int> %ebp-32 ]
    #    -36(%ebp)   4  [ $t5       <int> %ebp-36 ]

    # prologue
    pushl   %ebp                   
    movl    %esp, %ebp             
    pushl   %ebx                    # save callee saved registers
    pushl   %esi                   
    pushl   %edi                   
    subl    $24, %esp               # make room for locals

    cld                             # memset local stack area to 0
    xorl    %eax, %eax             
    movl    $6, %ecx               
    mov     %esp, %edi             
    rep     stosl                  

    # function body
    movl    $2, %eax                #   0:     assign a <- 2
    movl    %eax, a                
    movl    $5, %eax                #   1:     assign b <- 5
    movl    %eax, b                
    movl    a, %eax                 #   2:     add    t0 <- a, b
    movl    b, %ebx                
    addl    %ebx, %eax             
    movl    %eax, -16(%ebp)        
    movl    -16(%ebp), %eax         #   3:     assign c <- t0
    movl    %eax, c                
    movl    c, %eax                 #   4:     param  0 <- c
    pushl   %eax                   
    call    WriteInt                #   5:     call   WriteInt
    addl    $4, %esp               
    movl    a, %eax                 #   6:     mul    t1 <- a, b
    movl    b, %ebx                
    imull   %ebx                   
    movl    %eax, -20(%ebp)        
    movl    -20(%ebp), %eax         #   7:     assign c <- t1
    movl    %eax, c                
    movl    c, %eax                 #   8:     param  0 <- c
    pushl   %eax                   
    call    WriteInt                #   9:     call   WriteInt
    addl    $4, %esp               
    movl    b, %eax                 #  10:     neg    t2 <- b
    negl    %eax                   
    movl    %eax, -24(%ebp)        
    movl    -24(%ebp), %eax         #  11:     add    t3 <- t2, a
    movl    a, %ebx                
    addl    %ebx, %eax             
    movl    %eax, -28(%ebp)        
    movl    -28(%ebp), %eax         #  12:     assign c <- t3
    movl    %eax, c                
    movl    c, %eax                 #  13:     param  0 <- c
    pushl   %eax                   
    call    WriteInt                #  14:     call   WriteInt
    addl    $4, %esp               
    movl    $1, %eax                #  15:     param  0 <- 1
    pushl   %eax                   
    call    Tmp                     #  16:     call   t4 <- Tmp
    addl    $4, %esp               
    movl    %eax, -32(%ebp)        
    movl    -32(%ebp), %eax         #  17:     assign c <- t4
    movl    %eax, c                
    movl    $1, %eax                #  18:     param  0 <- 1
    pushl   %eax                   
    call    Tmp                     #  19:     call   t5 <- Tmp
    addl    $4, %esp               
    movl    %eax, -36(%ebp)        
    movl    -36(%ebp), %eax         #  20:     param  0 <- t5
    pushl   %eax                   
    call    WriteInt                #  21:     call   WriteInt
    addl    $4, %esp               

l_test01_special_case_exit:
    # epilogue
    addl    $24, %esp               # remove locals
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

    # scope: test01_special_case
a:                                  # <int>
    .skip    4
b:                                  # <int>
    .skip    4
c:                                  # <int>
    .skip    4


    # end of global data section
    #-----------------------------------------

    .end
##################################################
