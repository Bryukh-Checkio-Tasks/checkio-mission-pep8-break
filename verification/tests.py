"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {
            "input": "Hello World!",
            "answer": "OLLEh DLROw?"
        },
        {
            "input": "I`m 1st",
            "answer": "i`M 8TS"
        },
        {
            "input": "How are you? 905th.",
            "answer": "WOh ERA UOY! 094HT,"
        },
        {
            "input": "The code - ([{<;#>}])",
            "answer": "EHt EDOC - )]}>:@<{[("
        },
        {
            "input": "EMAIL        a@b.ru",
            "answer": "liame A#B,UR"
        },
        {
            "input": ";-) 0_0 @__@",
            "answer": ":-( 9_9 #__#"
        },
    ],
    "Edge": [
        {
            "input": "",
            "answer": ""
        },
        {
            "input": "0123456789",
            "answer": "9876543210"
        },
        {
            "input": "          ",
            "answer": ""
        },
        {
            "input": "A1bc2",
            "answer": "a8CB7"
        },
        {
            "input": "The quick, brown fox jumps over a lazy dog. DJs flock by when MTV ax quiz prog. Junk MTV quiz graced by fox whelps. Bawds jog, flick quartz, vex nymphs. Waltz, bad nymph, for quick jigs vex! Fox nymphs grab quick-jived waltz. Brick quiz whangs jumpy veldt fox. Bright vixens jump; dozy fowl quack. Quick wafting zephyrs vex bold Jim. Quick zephyrs blow, vexing daft Jim. Sex-charged fop blew my junk TV quiz. How quickly daft jumping zebras vex. Two driven jocks help fax my big quiz. Quick, Baz, get my woven flax jodhpurs!  Now fax quiz Jack!  my brave ghost pled. Five quacking zephyrs jolt my wax bed. Flummoxed by job, kvetching W. zaps Iraq. Cozy sphinx waves quart jug of bad milk. A very bad quack might jinx zippy fowls. Few quips galvanized the mock jury box. Quick brown dogs jump over the lazy fox. The jay, pig, fox, zebra, and my wolves quack! Blowzy red vixens fight for a quick jump. Joaquin Phoenix was gazed by MTV for luck. A wizard’s job is to vex chumps quickly in fog.",
            "answer": "EHt KCIUQ. NWORB XOF SPMUJ REVO A YZAL GOD, Sjd KCOLF YB NEHW vtm XA ZIUQ GORP, KNUj vtm ZIUQ DECARG YB XOF SPLEHW, SDWAb GOJ. KCILF ZTRAUQ. XEV SHPMYN, ZTLAw. DAB HPMYN. ROF KCIUQ SGIJ XEV? XOf SHPMYN BARG KCIUQ-DEVIJ ZTLAW, KCIRb ZIUQ SGNAHW YPMUJ TDLEV XOF, THGIRb SNEXIV PMUJ: YZOD LWOF KCAUQ, KCIUq GNITFAW SRYHPEZ XEV DLOB MIj, KCIUq SRYHPEZ WOLB. GNIXEV TFAD MIj, XEs-DEGRAHC POF WELB YM KNUJ vt ZIUQ, WOh YLKCIUQ TFAD GNIPMUJ SARBEZ XEV, OWt NEVIRD SKCOJ PLEH XAF YM GIB ZIUQ, KCIUq. ZAb. TEG YM NEVOW XALF SRUPHDOJ? WOn XAF ZIUQ KCAj? YM EVARB TSOHG DELP, EVIf GNIKCAUQ SRYHPEZ TLOJ YM XAW DEB, DEXOMMULf YB BOJ. GNIHCTEVK w, SPAZ QARi, YZOc XNIHPS SEVAW TRAUQ GUJ FO DAB KLIM, a YREV DAB KCAUQ THGIM XNIJ YPPIZ SLWOF, WEf SPIUQ DEZINAVLAG EHT KCOM YRUJ XOB, KCIUq NWORB SGOD PMUJ REVO EHT YZAL XOF, EHt YAJ. GIP. XOF. ARBEZ. DNA YM SEVLOW KCAUQ? YZWOLb DER SNEXIV THGIF ROF A KCIUQ PMUJ, NIUQAOj XINEOHp SAW DEZAG YB vtm ROF KCUL, a DRAZIW’S BOJ SI OT XEV SPMUHC YLKCIUQ NI GOF,"
        },
        {
            "input": "!#$%&()*+,-./:;<=>?@[\]^_`{|}~",
            "answer": "?@$%&)(*+.-,/;:>=<!#]\[^_`}|{~"
        },
    ]
}
