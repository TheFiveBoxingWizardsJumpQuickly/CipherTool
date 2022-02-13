#Static
'''
            	暗号用  	    翻訳用
6字側換字多表   sixes_enc   	sixes_dec
20字側換字多表1	twenties1_enc	twenties1_dec
20字側換字多表2	twenties2_enc	twenties2_dec
20字側換字多表3	twenties3_enc	twenties3_dec
'''

sixes_dec=[AEIOUY, EAIUOY, YIUEAO, AUOYEI, OIEAYU, IYAOUE, EAYUIO, YUOEAI, IYAOUE, UOEYIA, OUIEAY, EAOUYI, UOYIEA, IAEYOU, OEUAIY, AYEIUO, UOIYAE, YEUIOA, EIOAUY, AEIUYO, IAYOEU, YUAEOI, AIYOEU, YOUAIE, OYAEUI, UEOIYA] 
sixes_enc=[AEIOUY, EAIUOY, UOEYIA, AUYIEO, OIEAYU, IYAOUE, EAUYOI, UOYIEA, IYAOUE, YIUEAO, UOIAEY, EAYIOU, YUOEAI, EIAUYO, OEUAIY, AIOYUE, UYIEAO, YEOUIA, OAEIUY, AEIYOU, EUAOYI, IOYUEA, AUEOYI, OYUEIA, IOYAUE, YEOIAU] 
twenties1_dec=[BCDFGHJKLMNPQRSTVWXZ, HXRBMFCJQLKTDWSNGPZV, FGTVRBZSDKWNPQMXCHLJ, VBQHSNXPTWMDJRKZFLCG, DRZFHTKXCPVLGBNMJQSW, XHKZQGWFMDTSRPJCVNBL, CNLRJXHDWQPKMSTVZFGB, TJHWLMQBVCGFNXZRKSDP, BZJTPRGWSMQHKDFLNVXC, VLNKZWJRBTSGXCHPFMQD, PKVLDZFMRGJWCTQHBXSN, ZBTNCVLFKSMQDWRGHJPX, GFSCQXHTPRKJVMWDLBNZ, SVMXTCNKLJDRWQPBGZHF, NPJDKSTHFZCGBLXWMRVQ, PTCJFKSXGBNLZVHRQDWM, KSWBPNVRZTQXLJDFCGMH, JDGWVQXZRNLMCHBSPTFK, MQFRWDCVNXZBHPLJSKGT, QJLPZTRMXHBCNFGDWVKS, BCDFGHJKLMNPQRSTVWXZ, LZPGMVBQJSFDTKWNXCRH, WSCQBJMGXVHZLNPKDFTR, TWXMNZGLBFPQJHVCRSDK, GKBSXLPCHDRVFZTQWMJN, RMFKLPDNVZXHSGCWTJBQ] 
twenties1_enc=[BCDFGHJKLMNPQRSTVWXZ, FJQHVBKNMGTWLDSPZRCX, HVLBCWZMXSPQRGKDFNTJ, CXPVZFQSWNHKDRGLBMJT, RLBFQGVJPTSMWCXHNZKD, XTMKHCSDZLWRGQPNVJBF, ZBKWXJGPDQCNMFRSTLHV, KMXPNDCVGHQZJTWBLFRS, BZRSJPDQTMVGNHLFWKXC, LRZVPSJFCWDTXKNMBHQG, VQGJMTNCFKZBSLXRDPWH, CGQKTVWLJNFXPSMDHRZB, WFTCBJPNVRXLGMDKQSHZ, THNZVXMKLDJSRPBGCQFW, QNFLPKDGRVBCZWHJXTSM, MDWGLSFHPZNBVTJCRXKQ, FVSTWZRBQXHGNKCMJDPL, SQCXDRBZNPMVHLTWGFJK, PJHDXQTWSBLRCFVZKGMN, NPTRSMCXDKQFBJZHWVLG, BCDFGHJKLMNPQRSTVWXZ, JWPNFZLRBGTDKXMQHSVC, GDVWKNHTQJRSFZCXMBLP, LTXMJRQZKFGNPVWBSCDH, DKMQBLXCHWZJTNFSPVGR, XSJDRPWFGCKHZBQVLTNM] 
twenties2_dec=[BCDFGHJKLMNPQRSTVWXZ, SLBGVXDCMKNWPTHQZFRJ, PHSCFLKTXVGNZJMWBRQD, FWGKTBPSZRQVNCJLHDMX, HNCZRJWPSDKGMBVXLTFQ, JCQDLFVRBPWZHNTSGKXM, GVRJMLXZKQBCTDFPNWHS, KFDNXQCLPTMVRSZHWBJG, ZBTMSKRNWGDJQVXFCLPH, LKJSGCFQVBNHXWRMDZTP, MPNWKTZVGHLDFXQJBRSC, NJRFWZHBQXPSGLTCVMKD, CDLMQRSTJNZPWHBGKVXF, TMSBVDQLFJHKCRGNPXWZ, XTWPDQLMHCVRNFJZSGBK, WRPXBJMHNSGLKZVFDQCT, ZDXCFGNRLMWTSPKJQHVB, DHFRCPTGWZJXBSLKMNQV, GSZLMVBXQPFCJHNRTKDW, RZQVGWKFCSTBLXDHJMPN, KNBHXRGWVDMQPZSTFCJL, VXHBPSZJTLDNQMCWKFGR, BGPZHNRKLJXFDQMVWTSC, TKMQNHXGDFSZVCWBRJLP, XQKTZMJBCWRHLGPDVSNF, QBVSJFTDRGCMWKNLXPZH] 
twenties2_enc=[BCDFGHJKLMNPQRSTVWXZ, DKJWFSZMCLNQTXBRGPHV, VFZGNCRJHSPBXWDKMTLQ, HRWBDVSFTXQJNMKGPCZL, RDMXPBHNVQCKZGLWSJTF, LCFHVQBWGZRMDKTSJNXP, NPRSBXFLHGVTMDZQCWJK, WJDCZTXBKNFLHQRMPVGS, CVNTMZPHWFKXQJGDRLSB, MHVJGPDCBTNZKSFXLRQW, VZPQLMTGNBDCSWXHKFRJ, KTZFQJCXRWBNLDPSVGMH, SBCZTRLVDFMPGHJKWQXN, FQHLSNMPKCTVJRDBGXWZ, XMGRWLSZJKQFHPVCNDBT, GXVTNKHQPJLDWCMZSBFR, ZFCGHWTSLMJRVKQPXNDB, QGBDKCNTSVWHXFRJZLPM, JPXNBRQWFGSMLTCVHZKD, PLSKGTVJQWZXDBMNFHRC, DWMVJFXBZNCQPHSTLKGR, FSNWXDKVMRPGQZHLBTCJ, BZQPCGMKLSHDRJXWTVNF, TRLMKHWCXDGZFVNBQSJP, KLTZRPJDQHXSCNWFVMBG, CNKHMZGRTPSWBLFJDQVX] 
twenties3_dec=[BCDFGHJKLMNPQRSTVWXZ, JXNDZBMHTPVQKLFWGRSC, SVRCPQKDBXLFMJNZTHWG, CNZPBXFMLRHSQDJTWKGV, TDPLFZHXWCGKRNMBSVQJ, PWTFLDSQHZKCJMGXRBVN, QLGHKJPVRWZMCXNSFDBT, FJCSVMXGKTBPDQHRZLNW, LHFMWTKRGPVBZSQXCNJD, GRWVQSNPJKDHBCZFLMTX, NTLWDPGSMBRVCFXHKJQZ, XKDSRGBNCMPTWZVJQFLH, BPVQLJRCSFGNHTDKWXZM, DFMPBWCKRQXJTHSLVZGN, LNHGMFVXQSJCPWRZBTKD, KQRTXPZJMDSLFVBNGCHW, WTSFCVQPHNZXRGLBKJDM, RBJZHQTWPLFVGNCDMSXK, VXBNJCWFDKMGSPTLHQZR, MSCRNHJBTZQDLKWVXGPF, ZLKHPNCGFJTRVDSMQXWB, NZQKTMWRXHSFBVJGDLCP, TGMXFWSVBDCZNHKQJPRL, HMXTGLBZVFNWJRQCPKDS, KJGBSRLTNVWHXZDPFCMQ, QCVJRKDLZGTMHBPSNWFX] 
twenties3_enc=[BCDFGHJKLMNPQRSTVWXZ, HZFSVKBQRJDMPWXLNTCG, LFKPZWRJNQSGHDBVCXMT, GBRJXNSWLKCFQMPTZVHD, TMCGNJZPFSRDXQVBWLKH, WPHFSLQNGRZBKVJDXCTM, XQWVDFHGCPSJBLTZKMRN, NDQBKSCLWHXPRTFMGZJV, PVZDLCXJBFWMSKRHNGTQ, QRNTBPLMVWJKGCHXFDZS, MQGRJTWVDLBHXNKCPFSZ, JLDWHZTCXMKNVGFPSQBR, BKSMNQHTGZPCFJLRDVWX, GJBCXRPKTDZFMLSQVHNW, VPZHFDNXBGCQLSMWJRKT, SWMQVXKBPLTHCDNFRZGJ, TGXFRLWVSZMKJQDCHBPN, CSTNQGDZMVRLHBWJPKXF, DHLKPVGMTNFRWZQSBJCX, KDPZWHJRQBGXNFCLTSVM, ZJRLKFMDCTHGVPSNQXWB, QXVPTMSFWHBZDKNGRJLC, LNMGCRVSZDQWTXJBKHFP, JTXMGBQWHCNVSRZFLPDK, FWSVDPCBJXLTZHGKMNQR, RCJXMQFHKPVSBGTNDWZL] 

roter_speed = {
    1:['fast','mid','slow'], 
    2:['fast','slow','mid'], 
    3:['mid','fast','slow'], 
    4:['mid','slow','fast'], 
    5:['slow','fast','mid'], 
    6:['slow','mid','fast']}

#Utility functions
def roter_proceed(switch_position_by_motion):
    sixes=switch_position_by_motion[0]
    tw_fast=switch_position_by_motion[1]
    tw_mid=switch_position_by_motion[2]
    tw_slow=switch_position_by_motion[3]

    def rot(sw):
        if sw == 25:
            return 1
        else:
            return sw + 1

    sixes_next = rot(sixes)

    if sixes == 24 and tw_mid == 25:
        tw_fast_next = tw_fast
        tw_mid_next = tw_mid
        tw_slow_next = rot(tw_slow)
    else if sixes == 25:
        tw_fast_next = tw_fast
        tw_mid_next = rot(tw_mid)
        tw_slow_next = tw_slow
    else:
        tw_fast_next = rot(tw_fast)
        tw_mid_next = tw_mid
        tw_slow_next = tw_slow

    return [sixes_next, tw_fast_next, tw_mid_next, tw_slow_next]

def switch_position_translate_to_by_motion(switch_position, motion):
    buf[0] = switch_position[0]
    for i in range(1,3):
        if motion[i] == 'fast':
            buf[1] == switch_position[i]
        else if motion[i] == 'mid':
            buf[2] == switch_position[i]
        else if motion[i] == 'slow':
            buf[3] == switch_position[i]
    return buf

def switch_position_translate_to_by_order(switch_position_by_motion, motion):
    buf[0] = switch_position_by_motion[0]
    for i in range(1,3):
        if motion[i] == 'fast':
            buf[i] == switch_position_by_motion[1]
        else if motion[i] == 'mid':
            buf[i] == switch_position_by_motion[2]
        else if motion[i] == 'slow':
            buf[i] == switch_position_by_motion[3]
    return buf

def plugboard_encode(char, plugboard):
    return plugboard['AEIOUYBCDFGHJKLMNPQRSTVWXZ'.find(char)]

def plugboard_decode(char, plugboard):
    return 'AEIOUYBCDFGHJKLMNPQRSTVWXZ'[plugboard.find(char)]


#Purple machine emulation
def purple_encode_one_char(char, switch_position, motion, plugboard):
    layer_0 = char
    layer_1 = plugboard_encode(layer_0, plugboard)

    if layer_1 in 'AEIOUY':
        layer_4 = sixes_enc[switch_position[0]][sixes_enc[0].find(layer_1)]
    else:
        layer_2 = twenties1_enc[switch_position[1]][twenties1_enc[0].find(layer_1)]
        layer_3 = twenties2_enc[switch_position[2]][twenties2_enc[0].find(layer_2)]
        layer_4 = twenties3_enc[switch_position[3]][twenties3_enc[0].find(layer_3)]
    
    layer_5 = plugboard_decode(layer_4, plugboard)
    return layer_5

def purple_decode_one_char(char, switch_position, motion, plugboard):
    layer_5 = char
    layer_4 = plugboard_encode(layer_5, plugboard)

    if layer_4 in 'AEIOUY':
        layer_1 = sixes_dec[switch_position[0]][sixes_dec[0].find(layer_1)]
    else:
        layer_3 = twenties3_dec[switch_position[3]][twenties3_dec[0].find(layer_4)]
        layer_2 = twenties2_dec[switch_position[2]][twenties2_dec[0].find(layer_3)]
        layer_1 = twenties1_dec[switch_position[1]][twenties1_dec[0].find(layer_2)]
    
    layer_0 = plugboard_decode(1, plugboard)
    return layer_0

def purple(text, sixes_initial, twenties1_initial, twenties2_initial, twenties3_initial, motion_type, plugboard):
    

