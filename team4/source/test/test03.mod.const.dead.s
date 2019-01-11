##################################################
# test03
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

    # scope test03
main:
    # stack offsets:
    #    -13(%ebp)   1  [ $t0       <bool> %ebp-13 ]
    #    -14(%ebp)   1  [ $t1       <bool> %ebp-14 ]
    #    -15(%ebp)   1  [ $t2       <bool> %ebp-15 ]

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
    movl    $1, %eax                #   0:     if     1 = 1 goto 6
    movl    $1, %ebx               
    cmpl    %ebx, %eax             
    je      l_test03_6             
    jmp     l_test03_4              #   1:     goto   4
l_test03_6:
    movl    $0, %eax                #   3:     if     0 = 1 goto 3
    movl    $1, %ebx               
    cmpl    %ebx, %eax             
    je      l_test03_3             
    jmp     l_test03_4              #   4:     goto   4
l_test03_3:
    movl    $1, %eax                #   6:     assign t0 <- 1
    movb    %al, -13(%ebp)         
    jmp     l_test03_5              #   7:     goto   5
l_test03_4:
    movl    $0, %eax                #   9:     assign t0 <- 0
    movb    %al, -13(%ebp)         
l_test03_5:
    movzbl  -13(%ebp), %eax         #  11:     assign c <- t0
    movb    %al, c                 
    movzbl  c, %eax                 #  12:     if     c = 1 goto 8_if_true
    movl    $1, %ebx               
    cmpl    %ebx, %eax             
    je      l_test03_8_if_true     
    jmp     l_test03_9_if_false     #  13:     goto   9_if_false
l_test03_8_if_true:
    movl    $1, %eax                #  15:     param  0 <- 1
    pushl   %eax                   
    call    WriteInt                #  16:     call   WriteInt
    addl    $4, %esp               
    jmp     l_test03_7              #  17:     goto   7
l_test03_9_if_false:
    movl    $0, %eax                #  19:     param  0 <- 0
    pushl   %eax                   
    call    WriteInt                #  20:     call   WriteInt
    addl    $4, %esp               
l_test03_7:
    movl    $1, %eax                #  22:     if     1 = 1 goto 13
    movl    $1, %ebx               
    cmpl    %ebx, %eax             
    je      l_test03_13            
    movl    $0, %eax                #  23:     if     0 = 1 goto 13
    movl    $1, %ebx               
    cmpl    %ebx, %eax             
    je      l_test03_13            
    jmp     l_test03_14             #  24:     goto   14
l_test03_13:
    movl    $1, %eax                #  26:     assign t1 <- 1
    movb    %al, -14(%ebp)         
    jmp     l_test03_15             #  27:     goto   15
l_test03_14:
    movl    $0, %eax                #  29:     assign t1 <- 0
    movb    %al, -14(%ebp)         
l_test03_15:
    movzbl  -14(%ebp), %eax         #  31:     assign c <- t1
    movb    %al, c                 
    movzbl  c, %eax                 #  32:     if     c = 1 goto 18_if_true
    movl    $1, %ebx               
    cmpl    %ebx, %eax             
    je      l_test03_18_if_true    
    jmp     l_test03_19_if_false    #  33:     goto   19_if_false
l_test03_18_if_true:
    movl    $1, %eax                #  35:     param  0 <- 1
    pushl   %eax                   
    call    WriteInt                #  36:     call   WriteInt
    addl    $4, %esp               
    jmp     l_test03_17             #  37:     goto   17
l_test03_19_if_false:
    movl    $0, %eax                #  39:     param  0 <- 0
    pushl   %eax                   
    call    WriteInt                #  40:     call   WriteInt
    addl    $4, %esp               
l_test03_17:
    movl    $1, %eax                #  42:     if     1 = 1 goto 24
    movl    $1, %ebx               
    cmpl    %ebx, %eax             
    je      l_test03_24            
    movl    $0, %eax                #  43:     if     0 = 1 goto 24
    movl    $1, %ebx               
    cmpl    %ebx, %eax             
    je      l_test03_24            
    movl    $1, %eax                #  44:     assign t2 <- 1
    movb    %al, -15(%ebp)         
    jmp     l_test03_25             #  45:     goto   25
l_test03_24:
    movl    $0, %eax                #  47:     assign t2 <- 0
    movb    %al, -15(%ebp)         
l_test03_25:
    movzbl  -15(%ebp), %eax         #  49:     assign c <- t2
    movb    %al, c                 
    movzbl  c, %eax                 #  50:     if     c = 1 goto 28_if_true
    movl    $1, %ebx               
    cmpl    %ebx, %eax             
    je      l_test03_28_if_true    
    jmp     l_test03_29_if_false    #  51:     goto   29_if_false
l_test03_28_if_true:
    movl    $1, %eax                #  53:     param  0 <- 1
    pushl   %eax                   
    call    WriteInt                #  54:     call   WriteInt
    addl    $4, %esp               
    jmp     l_test03_27             #  55:     goto   27
l_test03_29_if_false:
    movl    $0, %eax                #  57:     param  0 <- 0
    pushl   %eax                   
    call    WriteInt                #  58:     call   WriteInt
    addl    $4, %esp               
l_test03_27:

l_test03_exit:
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

    # scope: test03
a:                                  # <bool>
    .skip    1
b:                                  # <bool>
    .skip    1
    .align   4
b1:                                 # <int>
    .skip    4
c:                                  # <bool>
    .skip    1

    # end of global data section
    #-----------------------------------------

    .end
##################################################
