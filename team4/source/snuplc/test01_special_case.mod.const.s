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
    movl    $7, %eax                #   2:     assign t0 <- 7
    movl    %eax, -16(%ebp)        
    movl    $7, %eax                #   3:     assign c <- 7
    movl    %eax, c                
    movl    $7, %eax                #   4:     param  0 <- 7
    pushl   %eax                   
    call    WriteInt                #   5:     call   WriteInt
    addl    $4, %esp               
    movl    $10, %eax               #   6:     assign t1 <- 10
    movl    %eax, -20(%ebp)        
    movl    $10, %eax               #   7:     assign c <- 10
    movl    %eax, c                
    movl    $10, %eax               #   8:     param  0 <- 10
    pushl   %eax                   
    call    WriteInt                #   9:     call   WriteInt
    addl    $4, %esp               
    movl    $-5, %eax               #  10:     assign t2 <- -5
    movl    %eax, -24(%ebp)        
    movl    $-3, %eax               #  11:     assign t3 <- -3
    movl    %eax, -28(%ebp)        
    movl    $-3, %eax               #  12:     assign c <- -3
    movl    %eax, c                
    movl    $-3, %eax               #  13:     param  0 <- -3
    pushl   %eax                   
    call    WriteInt                #  14:     call   WriteInt
    addl    $4, %esp               
    movl    $10, %eax               #  15:     assign t4 <- 10
    movl    %eax, -32(%ebp)        
    movl    $10, %eax               #  16:     assign c <- 10
    movl    %eax, c                
    movl    $10, %eax               #  17:     assign t5 <- 10
    movl    %eax, -36(%ebp)        
    movl    $10, %eax               #  18:     param  0 <- 10
    pushl   %eax                   
    call    WriteInt                #  19:     call   WriteInt
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
