decode():                             // @decode()
        sub     sp, sp, #48             // =48
        adrp    x8, .L_ZZ6decodevE8password
        add     x8, x8, :lo12:.L_ZZ6decodevE8password
        ldur    q0, [x8, #30]
        ldp     q2, q1, [x8]
        mov     x8, sp
        mov     w9, #33
        stur    q0, [sp, #30]
        stp     q2, q1, [sp]
.LBB0_1:                                // =>This Inner Loop Header: Depth=1
        ldrb    w10, [x8]
        eor     w10, w10, w9
        sub     w10, w10, #33          
        strb    w10, [x8], #1
        b       .LBB0_1
.L_ZZ6decodevE8password:
	.asciz "\x52\x4b\x54\x55\x47\x45\xbd\xa8\xa7\xbb\xa1\xae\xab\xa5\xa7\xa1\xbb\xb1\xb7\xa1\xa5\xa3\xae\xa1\xb2\xa7\xb6\xa7\xb2\xb5\xa7\xa1\x43\x52\x4f\xa1\xa3\xb5\xb5\xa7\xaf\xa2\xac\xbb\xbf"
