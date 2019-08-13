import pandas as pd
import csv

group = {}

group[1] = ['panneerselvamav007@gmail.com',
                        'ranjithindian003@gmail.com',
                        'ashikaraj2014@gmail.com',
                        'dakshanadakshu@gmail.com',
                        'varunpm.26@gmail.com',
                        'hariharan28565@gmail.com',
                        'sonarahini@gmail.com',
                        'srnandhu2001@gmail.com',
                        'sandy.cse.it@gmail.com',
                        'ss.hariharan10@gmail.com',
                        'bhargavikrish12@gmail.com',
                        'jencyfran19@gmail.com',
                        'dhanyajai304@gmail.com',
                        'kopika2828@gmail.com',
                        'gokulakrishnan330@gmail.com',
                        'harrishchinnappan@gmail.com',
                        'sivaani37@gmail.com',
                        'dhayalcuber@gmail.com',
                        'sendto@yahoo.com',
                        'meenu0721@gmail.com',
                        'gokulhosur98@gmail.com',
                        'sathyapriya12.98@gmail.com',
                        'barani.srmb1061999@gmail.com',
                        'priyaraji.c24@gmail.com',
                        'dineshsarvajana@gmail.com']

group[2] = ['sathishrack29@gmail.com',
                        'tamilvelpradeep583@gmail.com',
                        'sambathjagan2000@gmail.com',
                        'ashwindevillier6612@gmail.com',
                        'harinibalamurugan05@gmail.com',
                        'sudharshinimurugesan@gmail.com',
                        'priyamohanmvds@gmail.com',
                        'divyadharshinibala01@gmail.com',
                        'sjssarvan05@gmail.com',
                        'manojlof@gmail.com',
                        'vsanand18@gmail.com',
                        'awsmyo1234@gmail.com',
                        'gunags0611@gmail.com',
                        'deepikaprakash52@gmail.com',
                        'ramyaa124@gmail.com',
                        'ambikasuresh2312@gmail.com',
                        'monidurga021@gmail.com',
                        'samdany454@gmail.com',
                        'mathankrishna39@gmail.com',
                        'shankardhandapani1@gmail.com',
                        'pavithragtmoorthi@gmail.com',
                        'jayashrijay05@gmail.com',
                        'deepisiva1998@gmail.com',
                        'prakash.a2016@kgkite.ac.in']

group[3] = ['mourishkholi2000@gmail.com',
                        'manigandapoorvish@gmail.com',
                        'deepakchakravarthy.d@gmail.com',
                        'sabarish.hari19@gmail.com',
                        'trasika038@gmail.com',
                        'swedhabhaskar2110@gmail.com',
                        'hemakumar0920@gmail.com',
                        'keerthu0511@gmail.com',
                        'sagarpatel3012000@gmail.com',
                        'baviyauma@gmail.com',
                        'katherimidhun@gmail.com',
                        'matheshthegreat@gmail.com',
                        'kishorekumarparthipan199t9@gmail.com',
                        'anupinky2000@gmail.com',
                        'varshini1099@gmail.com',
                        'Nivethithasundararajan1506@gmail.com',
                        'sofiamh1999@gmail.com',
                        'muralikasthuri22@gmail.com',
                        'karthickcruze38@gmail.com',
                        'sarwesr18@gmail.com',
                        'poojavigni@gmail.com',
                        'k.suganthistella@gmail.com',
                        'sweatharamdhass99@gmail.com',
                        'kavishree1234@gmail.com',
                        'akshaykrish81481@gmail.com']

group[4] = ['nitheeshnitheesh860@gmail.com',
                        'manojravikumar00@gmail.com',
                        'austincitesjam19@gmail.com',
                        'kkaviya109@gmail.com',
                        'rtmaheswari150@gmail.com',
                        'sathyaraje24@gmail.com',
                        'rubeshjayaraam25@gmail.com',
                        'dhivyaprasad007@gmail.com',
                        'sanjeevkanth99@gmail.com',
                        'swarnavikram2016@gmail.com',
                        'praveensansiva@gmail.com',
                        'ultimateraj123@gmail.com',
                        'sangeethabalu021299@gmail.com',
                        'nivinivetha888@gmail.com',
                        'priyakgisl123@gmail.com',
                        'rajisweetysekar@gmail.com',
                        'sandeep.pkd159@gmail.com',
                        'k30rahul@gmail.com',
                        'rajadurai.r2016@kgkite.ac.in',
                        'aiswariyacse@gmail.com',
                        'muthusaranya29@gmail.com',
                        'Kowshi5323@gmail.com',
                        'nethajiisu@gmail.com',
                        'sanjaybabu618@gmail.com',
                        'nivethaneethu748@gmail.com']

group[5] = ['revathyponni2000@gmail.com',
                        'gayugovind109@gmail.com',
                        'Pavithraramamurthi23@gmail.com',
                        'varunsudhakar06@gmail.com',
                        'sakchutech@gmail.com',
                        'dharnishmessi10@gmail.com',
                        'selvaganeshh3@gmail.com',
                        'srikrishnapsk01@gmail.com',
                        'hariharan.k205@gmail.com',
                        'aswinperiyaswamy007@gmail.com',
                        'manojbm.kite@gmail.com',
                        'vijaymani910@gmail.com',
                        'nishanthxavio@gmail.com',
                        'email2shalinir@gmail.com',
                        'praveenasun99@gmail.com',
                        'pavithra.ananthkumar@gmail.com',
                        'lekha74200@gmail.com',
                        'deepamukil.31@gmail.com',
                        'navee016@gmail.com',
                        'vishnusruthi338@gmail.com',
                        'darshansudhagar1704@gmail.com',
                        'gowsirajju27299@gmail.com',
                        'sunithabalasubramanian14@gmail.com',
                        'kishorekumar00770099@gmail.com']

group[6] = ['neshvig2001@gmail.com',
                        'ksanchai76@gmail.com',
                        's.abilashsoundar@gmail.com',
                        'arunrock383@gmail.com',
                        '2017jsoorya@gmail.com',
                        'mohamedashikcbe@gmail.com',
                        'swathisrivasudevan23@gmail.com',
                        'abiramithavamani1999@gmail.com',
                        'hildahsweety@gmail.com',
                        'ramyaraj599@gmail.com',
                        'rithin193@gmail.com',
                        'kannangiri8@gmail.com',
                        'sairaam275@gmail.com',
                        'vigneshponmalar2799@gmail.com',
                        'jayasuryaayyappasamy2640@gmail.com',
                        'durgaravi1999@gmail.com',
                        'mercyjas07@gmail.com',
                        'baburajanjali001@gmail.com',
                        'hesheha137@gmail.com',
                        'reegannavis41@gmail.com',
                        'sureshmalar2407@gmail.com',
                        'deepakkottiappasamy@gmail.com',
                        'ramanvjy5@gmail.com',
                        'suriya972.nesh@gmail.com']

group[7] = ['ramxetoxy001@gmail.com',
                        'saravanaprakaash24@gmail.com',
                        'nvnr46@gmail.com',
                        'dileepkrish7676@gmail.com',
                        'ranjithkumar89310@gmail.com',
                        'parthasarathic28@gmail.com',
                        'rmanokaran23@gmail.com',
                        'subbikchakarthikeyan19@gmail.com',
                        'aishwariyayashwanthini@gmail.com',
                        'veenaoviya4094@gmail.com',
                        'shankardhoni5@gmail.com',
                        'vigneshv3009@gmail.com',
                        'sriraambalaji18@gmail.com',
                        'raj25jana@gmail.com',
                        'niranjanshaa33@gmail.com',
                        'ksgeetha750@gmail.com',
                        'meyyarasi2000@gmail.com',
                        'smartmathu25@gmail.com',
                        'anaghajayaraj6@gmail.com',
                        'divyamurugesan0@gmail.com',
                        'sathyanarayanan2619@gmail.com',
                        '11223siva@gmail.com',
                        'raamnethesh333@gmail.com',
                        '9600503995abc@gmail.com']

group[8] = ['niranjayan19@gmail.com',
                        'rprsajith3102001@gmail.com',
                        'avinash10092000@gmail.com',
                        'srijithmohandas2001@gmail.com',
                        'rohithviratsha1511@gmail.com',
                        'poomanikandannagarajan@gmail.com',
                        'thamilavelg@gmail.com',
                        'vigneshnagaraj0102@gmail.com',
                        'mithunkumar4745@gmail.com',
                        'sruthicsk777@gmail.com',
                        'Janakutty60@gmail.com',
                        'ashajebaselin@gmail.com',
                        'monisha8723@gmail.com',
                        'dhanshi24@gmail.com',
                        'keerthanas794@gmail.com',
                        'shirleyrovee@gmail.com',
                        'preethi04nov@gmail.com',
                        'kavisri15nov@gmail.com',
                        'poornimaamaheswari@gmail.com',
                        'sherinmonicasherinmonica5343@gmail.com']

group[9] = ['tilothamdhanabal@gmail.com',
                        'suriya2190ask@gmail.com',
                        'mithunsyuvaraj7010@gmail.com',
                        'sanjaysanjuvj444@gmail.com',
                        'prasanth777it@gmail.com',
                        'thiruvpn@gmail.com',
                        'sridharsr3004@gmail.com',
                        'hemamalinigb@gmail.com',
                        'priyavishnupriya18@gmail.com',
                        'taniyaammu3@gmail.com',
                        'vijayrakshana07@gmail.com',
                        'nandhinis2608@gmail.com',
                        'kavithabarath1720@gmail.com',
                        'akashbmw12@gmail.com',
                        'manojkumarsmart7@gmail.com',
                        'shankargowda0511@gmail.com',
                        'mani71036@gmail.com',
                        'nandy.viper@gmail.com',
                        'dharanithanni19@gmail.com',
                        'kavipriya36k@gmail.com',
                        'rubymyth2k@gmail.com',
                        'selsiaebanezar15@gmail.com',
                        'gopika90166@gmail.com',
                        'mansipatel27731@gmail.com',
                        'ragupraveen98@gmail.com',
                        'nanthithananthini@gmail.com']

group[10] = ['lokeshramesh08@gmail.com',
                        'mathi.karthi1420@gmail.com',
                        'charmeenochphilip2001@gmail.com',
                        'aravindrajsundaramurthi16@gmail.com',
                        'pravin27900@gmail.com',
                        'r.vijayanand10@gmail.com',
                        'keerthanakannan29@gmail.com',
                        'ashwinvishal2602@gmail.com',
                        'suvethabvs@gmail.com',
                        'keerthivennila123@gmail.com',
                        'gayuv2001@gmail.com',
                        'deepadisha666@gmail.com',
                        'pavithrashanmugam2000@gmail.com',
                        'bishwajithraj@gmail.com',
                        'alitouffiq@gmail.com',
                        '56rahul591@gmail.com',
                        'sivar739@gmail.com',
                        'arthiroselin99@gmail.com',
                        'prithishakathiresan@gmail.com',
                        'geedha.india@gmail.com',
                        'pswetha1708@gmail.com',
                        'vigarnaramesh13@gmail.com',
                        'swethasubramani31@gmail.com',
                        'pavikite@gmail.com',
                        'namusaran.r@gmail.com']

group_a = pd.read_csv('100_Days_of_Code_V2_GroupA.csv')
group_b = pd.read_csv('100_Days_of_Code_V2_GroupB.csv')

column_names = []

for i in group_a:
    column_names.append(i)

students_less_50 = []
students_less_50.append(column_names)

for j in range(len(group_a['percent_complete'])):
    student_caught = []
    if group_a['percent_complete'][j] < 51:
        for i in column_names:
            student_caught.append(group_a[i][j])
        group_id = ""
        for i in group:
            if group_a['email'][j] in group[i]:
                group_id = str(i)
        if group_id == "":
            group_id = "Not Recognised"
        student_caught.append(group_id)
        student_caught.append("A")
        students_less_50.append(student_caught)

for j in range(len(group_b['percent_complete'])):
    student_caught = []
    if group_b['percent_complete'][j] < 51:
        for i in column_names:
            student_caught.append(group_b[i][j])
        group_id = ""
        for i in group:
            if group_b['email'][j] in group[i]:
                group_id = str(i)
        if group_id == "":
            group_id = "Not Recognised"
        student_caught.append(group_id)
        student_caught.append("B")
        students_less_50.append(student_caught)

students_less_50[0].append("Group_Number")
students_less_50[0].append("Group Id")
with open('student_less_than_50.csv', 'w') as writeFile:
    writer = csv.writer(writeFile)
    writer.writerows(students_less_50)
