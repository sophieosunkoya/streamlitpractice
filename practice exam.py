#def is_valid_password(password):
    # Check if the password is not more than 15 characters long
    #if len(password) > 15:
        #return False
    
    # Check if the password contains any lowercase characters
    #if any(c.islower() for c in password):
        #return False
    
    # Check if the first and last character of the password are the same
    #if password[0] == password[-1]:
        #return False
    

    # If all the checks pass, return True
    #else:
        #return True

# Analyze the list of passwords and count the number of valid passwords
#passwords = ['baCr', '/)T.I]DdLNh)^WRIDa_z1', 'izM!Imi', 'NOb5VEhw$[17Q{P', 'i', 'J$52UY$Y', 'T', '3', '{77Vt3=2WOCpKWN?', '$*K', 'H2@u.yUON(i;?', 'zr', '/}YrhZ7T,X^/}cM0BvR@S)Le$/$Yg@', 'XUGc%', '+$?D]', '4?!-G}', 'iMI!G5q]bwI-fE1VT{8rsHWX2tk$29', 'E@', 'lVSh;W9:RyM%Zl9L*;', 'vWYJ%-v?^d:(o', '.(tp?Hxu{[D+cAhmXGM{ahV3a_fZ!', '3SXUCASo8/3psxL0p5mw=uf', '%%7h', 'e(d', 'Ef98S2EUy)mT9MU{@F:zE^8Pb]mg)k', 'k', 'ji[Wtw.#9F$GN%ymi-FU', 'HX?z74lGp]TLqlGp[cRV!w(5]s?7m9', '5eL', 'Zcrod:Xm', '}t8bj:RJ4BA6i+x$PlbKL$NNIj', 'H)u(7{lK?Mk!cvUBkzlHXfFyeTL%Sh', '/]AA-R0A', 'Qq1L$:(s', 'HoDUEPlaKAnDo2;W5}FlY)H(9I', 't0UVz3xgM2Js', 'XJ=@Y=P)z@%7', 'hnDTB7vtCa!MsAIR', '{R/BvTB?iNS!vKntp$,tvwIC7', '}2Lz.K', 'P9?+AgbGhp${uMoLqwS(aajG9P.b', 'eldDgR6SZ:v6w^G6ru*vo-', '-{2{4', 'A=', 'Z{G2p{-#Kz/c}8utFm=WPH_:uTQiT', 'Ql91', '9R.6J@Y.jWs/}XA0TV4%uRi_k43', 'zcy.Vqfk2xpwgNt-KW?$m', 'X+O+NGT}', '}]2_', 'Mcuz1;xCE{iHRhsO695ef', ';Q4!nRV7[,LvLDRjke1', '3BJi9XZW', '+Rot!', 'nP.kqo1-g2G8ZT$2wxRwI8MAMJ', '^,$^F7:X=DkDUa?3,L{wf', '56', '#O/7CHV4WoMRmq^j$J$/Hk6DUD', 'WkWI5O1J017)5.%!dAaVLhoW', ')$;', '{5QjA.g:xO#P1', 'M]J%Dxc2]xxc1Kyn7=Ga+sx!@-B9', ':WA', '2?@', 'HwH_sUUd-i$ln178038#kiQ7T@kZ;', '13}VI', 'QV+', '2r-%+=:V', 'DM(DYS),Z==A}', 'fhtmcFtG)CQY0YrB7Aq%0Oogv]g', '-WFuVnPpZ?z@E{H3I#_:h-v^w9K', 'ceg4g-Y', 'yK8D5*om', '_ic55w$6N/3/00c', '^*BhAG4m', 'w#PW', 'D%=^j}l/Qr1l#V*%8d', '6tJNCnrx,)Fv6*+;q.;PCx1);', '}Q?}pvhv=beW', 'W$$.C5cI9;Grs653}-5(@p/Nb@8i', '{(:F6LI', 'r]l@?Fy', '@N4[qs{!P{Kb[t_sB', 'xoL:UAe(7m$4gjtuakk-ViLNu^b', 'Hc]1:eqc%TzXy8n-?s7VQG.#[nm', 'sM:pqfC', '8XVO5X7lwt8!B6', '{$[^', '7SiL3', 'hV_yN(Kh19%M)5PDV)9oQ5?y*k%2', '}UhE!SxN7qQVdiNXuw8N+Xxio%I', 'KK:', '+ZsrD?az!I', '@_', 'roX:*+2Dl#@k-io', '7Dq', 'TBQ[5', '9/CX', 'e74j*J^oD', '1KRmy=FjO[P?kd#+zNQV9:uL(vP', 'di?hp0L*6VZf9:', '24?%6GW%', 'S@', 'hI7TS!Jo2J2$Zp/_^aIK^(v{K4+', 'W*zIb', 'Qlu@bPU6UtNd', 'n9yX]z0xBQ3C$BG4Jk/,#MG4j[', 'u', 'xL!b.A!zUn', 'I21%', 'ff1Vf=fWqL:sg$gfKnA7;R', '!6A#W!jwnB-fPP1hGK]sA!B@uitkj', 'qNf.B35u0),}eL)', 'gXB.8I$bQ', '9v2q0An', 'F?9HZ4', 'z]bgZ8wHsLJQvT!gh(Yn5o[', 'w)K{[3{Z0%u^q', 'SD', '#c)RM554mY!YD93', '09YNkm.@VyMPC8cQg5', 'R1}Jw!-rV=Bo{A9@/aWuuP', 'n/CC5xU3hC.itVaF,R=?[^', '[RiM[xNb', '=I', ':M[Z%WY,w0.:{c;69ESv_@4S)#n', 'D6-9s.,f=pXiuMF;!l}!N]', 'L?2', '=#l4,5', 'ZAdAEkQzdmc[O[A,H%9]3}i?', '0%,OVJ9/}([L[Nq=3mgS:sYHa;', 'Y4:*NU', '$To.Ce7:hd#YgKFZr+1i.Lx)BIuH', 'nM)@%*H9GiXevMmVm.(Z)]:!BxU!r', 'h?(Y_', 'F(qqHrvx5kL[Xx=4lcs:H!A', 'TgIT+I;GClgST/NB*', '6=}.',
             #'+4', '+BQ5C}:6', 'Dh5VF2Ek#a', 'REB4k%v.c1J*vq?F3#2', '8}JCK', '#{?2[X?M[A!_O]RVKqVv%93_@]vx,$', 'H44z_DwaG/A,g)xBCG+9GjAh7e]$!', 'jgct7fezi;jtqc*', '(_', '.3:', 'eM4mx)S9HDq_,*rZ;LE0S=U4L2i', '-]F]']

#valid_password_count = 0

#for password in passwords:
    #if is_valid_password(password):
        #valid_password_count += 1

from cs0002_final_exam_module import p51

# Get the mother of the mother of the mother of p51
grandmother_of_grandmother = p51.mother.mother.mother

# Print the name of the grandmother of the grandmother
print(grandmother_of_grandmother.name)
