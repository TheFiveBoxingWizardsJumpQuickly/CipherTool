def __o(base_text, add_text, linebreak=0):
    text = base_text + add_text
    for i in range(linebreak):
        text += '<br>'
    return text

def show_table(id):
    if id == 0: return show_japan_traditional_month_name()
    elif id == 1: return show_zodiac()
    elif id == 2: return show_japanese_zodiac()
    elif id == 3: return show_hiragana()
    elif id == 4: return show_katakana()


def show_japan_traditional_month_name():
    b=''
    b= __o(b,'<B>Japanese Traditional Month Names</B>',2)
    b= __o(b,'1月: 睦月 (むつき)',1)
    b= __o(b,'2月: 如月 (きさらぎ)',1)
    b= __o(b,'3月: 弥生 (やよい)',1)
    b= __o(b,'4月: 卯月 (うづき) ',1)
    b= __o(b,'5月: 皐月 (さつき)',1)
    b= __o(b,'6月: 水無月 (みなづき)',1)
    b= __o(b,'7月: 文月 (ふみつき)',1)
    b= __o(b,'8月: 葉月 (はづき)',1)
    b= __o(b,'9月: 長月 (ながつき)',1)
    b= __o(b,'10月: 神無月 (かんなづき)',1)
    b= __o(b,'11月: 霜月 (しもつき)',1)
    b= __o(b,'12月: 師走 (しわす)',1)

    return b

def show_zodiac():
    b=''
    b= __o(b,'<B>Zodiac Names</B>',2)
    b= __o(b,'(Latin, Japanese, English, Greek)',1)
    b= __o(b,'Aries, 牡羊座, Ram, Κριός (Krios)', 1)
    b= __o(b,'Taurus, 牡牛座, Bull, Ταῦρος (Tauros) ',1)
    b= __o(b,'Gemini, 双子座, Twins, Δίδυμοι (Didymoi) ',1)
    b= __o(b,'Cancer, 蟹座, Crab, Καρκίνος (Karkinos) ',1)
    b= __o(b,'Leo, 獅子座, Lion, Λέων (Leōn) ',1)
    b= __o(b,'Virgo, 乙女座, Maiden, Παρθένος (Parthenos) ',1)
    b= __o(b,'Libra, 天秤座, Scales, Ζυγός (Zygos) ',1)
    b= __o(b,'Scorpio, 蠍座, Scorpion, Σκoρπίος (Skorpios) ',1)
    b= __o(b,'Sagittarius, 射手座, Archer, Τοξότης (Toxotēs) ',1)
    b= __o(b,'Capricorn, 山羊座, Mountain Goat, Αἰγόκερως (Aigokerōs) ',1)
    b= __o(b,'Aquarius, 水瓶座, Water-Bearer, Ὑδροχόος (Hydrokhoos) ',1)
    b= __o(b,'Pisces, 魚座, 2 Fish, Ἰχθύες (Ikhthyes) ',1)

    return b

def show_japanese_zodiac():
    b=''
    b= __o(b,'<B>十二支 (Japanese Zodiac)</B>',2)
    b= __o(b,'1. 子, Rat',1)
    b= __o(b,'2. 丑, Cow',1)
    b= __o(b,'3. 寅, Tiger',1)
    b= __o(b,'4. 卯, Rabbit',1)
    b= __o(b,'5. 辰, Dragon',1)
    b= __o(b,'6. 巳, Snake',1)
    b= __o(b,'7. 午, Horse',1)
    b= __o(b,'8. 未, Goat',1)
    b= __o(b,'9. 申, Monkey',1)
    b= __o(b,'10. 酉, Rooster',1)
    b= __o(b,'11. 戌, Dog',1)
    b= __o(b,'12. 亥, Wild boar',1)

    return b

def show_hiragana():
    b = \
    '''
    <table border=1>
    <tr><td>-</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td></tr>
    <tr><td>ん</td><td>わ</td><td>ら</td><td>や</td><td>ま</td><td>は</td><td>な</td><td>た</td><td>さ</td><td>か</td><td>あ</td></tr>
    <tr><td>■</td><td>■</td><td>り</td><td>■</td><td>み</td><td>ひ</td><td>に</td><td>ち</td><td>し</td><td>き</td><td>い</td></tr>
    <tr><td>■</td><td>■</td><td>る</td><td>ゆ</td><td>む</td><td>ふ</td><td>ぬ</td><td>つ</td><td>す</td><td>く</td><td>う</td></tr>
    <tr><td>■</td><td>■</td><td>れ</td><td>■</td><td>め</td><td>へ</td><td>ね</td><td>て</td><td>せ</td><td>け</td><td>え</td></tr>
    <tr><td>■</td><td>を</td><td>ろ</td><td>よ</td><td>も</td><td>ほ</td><td>の</td><td>と</td><td>そ</td><td>こ</td><td>お</td></tr>
    </table>

    '''
    return b

def show_katakana():
    b = \
    '''
    <table border=1>
    <tr><td>-</td><td>10</td><td>9</td><td>8</td><td>7</td><td>6</td><td>5</td><td>4</td><td>3</td><td>2</td><td>1</td></tr>
    <tr><td>ン</td><td>ワ</td><td>ラ</td><td>ヤ</td><td>マ</td><td>ハ</td><td>ナ</td><td>タ</td><td>サ</td><td>カ</td><td>ア</td></tr>
    <tr><td>■</td><td>■</td><td>リ</td><td>■</td><td>ミ</td><td>ヒ</td><td>ニ</td><td>チ</td><td>シ</td><td>キ</td><td>イ</td></tr>
    <tr><td>■</td><td>■</td><td>ル</td><td>ユ</td><td>ム</td><td>フ</td><td>ヌ</td><td>ツ</td><td>ス</td><td>ク</td><td>ウ</td></tr>
    <tr><td>■</td><td>■</td><td>レ</td><td>■</td><td>メ</td><td>ヘ</td><td>ネ</td><td>テ</td><td>セ</td><td>ケ</td><td>エ</td></tr>
    <tr><td>■</td><td>ヲ</td><td>ロ</td><td>ヨ</td><td>モ</td><td>ホ</td><td>ノ</td><td>ト</td><td>ソ</td><td>コ</td><td>オ</td></tr>
    </table>

    '''
    return b

