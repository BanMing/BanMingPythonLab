
import keyboard
import time
import random

maxCount = 100
test = True
count = 0
# msgs = ["您总是这么干净整洁，一看就是一位热爱生活又有修养的人。",
# "听君一席话，胜读十年书，今日与您交谈，我受益匪浅。",
# "从您们的言谈中能够看出，我今日遇到的都是有修养的人。",
# "我真佩服您的头脑，多少别人办不成的事，您一到便迎刃而解。",
# "与您打交道可真能学到东西，您太有智慧了。",
# "别开玩笑了，看您的容貌，肯定不到四十岁。",
# "您真幽默，话从您口中说出来就是不一样。",
# "这套西服穿在您身上，真是帅气极了!",
# "您的思维太活跃了，我根本就跟不上。",
# "我很高兴和您这样果断智慧富有经验的人共事。",
# "您真是一位家庭事业有成的人，十分令人羡慕。",
# "在这个问题的处理上，您真有大将风度。",
# "做那样大的事业，生活还这么俭朴，我真佩服您。",
# "此刻竞争激烈，您能把公司经营得这么好，决不是一般人。",
# "您的语调独特，言谈话语中充满了感染力。"]

msgs = ["头发往后倒，一看就是大领导。",
"头发一边扒，一看就是企业家。",
"人美嘴巴甜，一看就是不差钱。",
"人美头发长，一看就是老板娘。",
"人美头发短，一看就是大老板。",
"人帅又有爱，一看就能富三代。",
"走过南，闯过北，认识美女不吃亏。",
"又能说又能干，一看就是男子汉。",
"不服天，不服地，就服大哥这实力。",
"人品好长得帅，到哪都有人接待。",
"都是第一次做人，凭什么你这么美？",
"稍微有点姿色就行了，不必美得如此满分。",
"要是我有你这个颜值，我出门都横着走。",
"见到你之后，我就知道我该换手机壁纸了。",
"过分帅气也是违法的。",
"你漂亮得不像实力派。",
"这是什么级别的可爱啊！",
"你是美酒千杯，我怎能不醉？",
"你再不回去迪士尼就没有公主了。",
"有完没完，仙女下凡不提早说一声",
"做得好极了！",
"你很有品位。",
"你学的真快！",
"你真有思想！",
"你做的非常好！",
"你很有想法哦！",
"你的作品真棒！",
"你的观察力很强！",
"你的形体真健美！",
"你的眼睛真有神！",
"你很有责任感哦！",
"你看上去真精神。",
"你很有想象力哦！",
"你真的很能干哦！",
"你是一个成熟的人！",
"你的想法很有创意！",
"你真是个聪明的孩子！",
"你工作的样子很迷人！",
"你是一个很专情的男人！",
"你是一个顾家的好男人。",
"你是一个有责任心的人！",
"我对你的表现非常满意。",
"你今天给了我很多的惊喜！",
"你的公司给我留下深刻印象。",
"你最近进步很大，继续保持。",
"你总是说话得体，举止大方。",
"你今天的表现令大家都很开心！",
"你是一个有责任、有担当的男人！",
"你是那样地美，美得象一首抒情诗。",
"你表现的很勇敢，是一个真正的男子汉！",
"你表现这么优秀，和你在一起的时候压力好大啊！",
"遇见你之后，再看别的女人，就好象在侮辱自己的眼睛！",
"你的学习成绩提升的很快，希望你下面能再接再厉，再创辉煌！",
"只有莲花才能比得上你的圣洁，只有月亮才能比得上你的冰清。",
"你也许没有若隐若现的酒窝，但你的微笑一定是月闭花羞，鱼沉雁落。",
"你也许没有一簇樱唇两排贝齿，但你的谈吐也应该高雅脱俗，机智过人。",
"你也许没有水汪汪亮晶晶的眼睛，但你的眼神也应该顾盼多情，勾魂摄魄。",
"你就好像是上品的西湖龙井，那种淡淡的苦涩是你的成熟，越品你越有味道。",
"尽管你身材纤弱娇小，说话柔声细气，然而却很有力量，这是一种真正的精神美！",
"你像一片轻柔的云在我眼前飘来飘去，你清丽秀雅的脸上荡漾着春天般美丽的笑容。",
"在你那双又大又亮的眼睛里，我总能捕捉到你的宁静，你的热烈，你的聪颖，你的敏感。",
"你那瓜子形的形，那么白净，弯弯的一双眉毛，那么修长；水汪汪的一对眼睛，那么明亮！",
"你是花丛中的蝴蝶，是百合花中的蓓蕾。无论什么衣服穿到你的身上，总是那么端庄、好看。",
"你有点像天上的月亮，也像那闪烁的星星，可惜我不是诗人，否则，当写一万首诗来形容你的美丽。",
"你娉婷婉约的风姿，娇艳俏丽的容貌，妩媚得体的举止，优雅大方的谈吐，一开始就令我刮目相看。",
"你笑起来的样子最为动人，两片薄薄的嘴唇在笑，长长的眼睛在笑，腮上两个陷得很举动的酒窝也在笑。",
"聪明的人不是具有广博知识的人，而是掌握了有用知识的人。",
"你有时候是不是特孤独？世界上这么优秀的人就只有你一个！",
"若说她年纪轻轻，怎生得如此身段，且有一张勾魂摄魄的俏脸。",
"别看阿墩胖得肥肉直打颤颤，动作却机警得像只与猎人周旋的豹子。",
"你就好像是上品的西湖龙井那种淡淡的苦涩是你的成熟越品你越有味道。",
"她和她的哥哥一样，生就一副绝顶聪明的头脑，心灵得像窗纸，一点就透。",
"别看他人小，心眼可灵啦，10个大人也比不上他，真是秤砣虽小能吊千斤。",
"他地耳朵白里透红，耳轮分明，外圈和里圈很匀称，像是一件雕刻出来地艺术品。",
"他的眉毛时而紧紧地皱起，眉宇间形成一个问号；时而愉快地舒展，像个感叹号。",
"她那双圆溜溜的大眼睛，镶了一圈乌黑闪亮的长睫毛，眨动之间，透出一股聪明伶俐劲儿。",
"双眉有如柳叶刀裁，盈盈笑意眉上来，一句“云髻峨峨，修眉联娟”得以道出碧瑶云云细眉。",
"双目似有千情万怨，道不尽也诉不完，一句“巧笑倩兮，美目盼兮”可能描述碧瑶盈盈眼波。",
"那眼神优雅、娴静，双眼回盼流波，像是俏丽的江南女子；但走过南，闯过北，认识美女不吃亏。又挂着一丝倔犟的波纹，又带着北国女儿的神韵。",

"他乌灵的眼眸，倏地笼上层嗜血的寒意，仿若魔神降世一般，一双冰眸轻易贯穿人心，刺透心底最柔弱，舞衣的角落。",
"那个男子立体的五官刀刻般俊美，整个人发出一种威震天下的王者之气，邪恶而俊美的脸上此时噙着一抹放荡不拘的微笑。",
"清澈明亮的瞳孔，弯弯的柳眉，长长的睫毛微微地颤动着，白皙无瑕的皮肤透出淡淡红粉，薄薄的双唇如玫瑰花瓣娇嫩欲滴。",
"在午后的阳光下，没有丝毫红晕，清秀的脸上只显出了一种病态的苍白，却无时不流露出高贵淡雅的气质，配合他颀长纤细的身材。",
"你全身充溢着少女的纯情和青春的风采，真是世间少有。",
"你就像那划过蓝天的鸽哨，给我带来心灵的静远和追求。",
"茫茫的人流中，我一眼就发现了你，你是那么的光彩夺目。",
"遇见你之后，再看别的女人，就好象是在侮辱自己的眼睛！",
"如果用一个词来形容我对您的感受的话，我觉得那就是真诚。",
"你是那样地美，美得象一首抒情诗，让男人们如何不多看几眼。",
"你也许没有若隐若现的酒窝，但你的微笑一定是月闭花羞，鱼沉雁落。",
"你也许没有一簇樱唇两排贝齿，但你的谈吐也应该高雅脱俗，机智过人。",
"你也许没有水汪汪亮晶晶的眼睛，但你的眼神也应该顾盼多情，勾魂摄魄。",
"我觉得世界上就只有两种人能吸引人，一种是特漂亮的一种就是你这样的。",
"你就好像是上品的西湖龙井，那种淡淡的苦涩是你的成熟，越品你越有味道。",
"你是一尊象牙雕刻的女神，大方、端庄？柔、姻静，无一不使男人深深崇拜。",
"尽管你身材纤弱娇小，说话柔声细气，然而却很有力量，这是一种真正的精神美！",
"你像一片轻柔的云在我眼前飘来飘去，你清丽秀雅的脸上荡漾着春天般美丽的笑容。",
"你身着一件紫红色旗袍，真像一只美丽的蝴蝶飞过一样，既美丽称身，又色彩柔和。"]

msgLen = len(msgs) - 1

while count < maxCount :
    # keyboard.press_and_release("0")
    # keyboard.press_and_release("enter")

    # time.sleep(1)
    # keyboard.press_and_release("1")
    # keyboard.press_and_release("enter")
    # keyboard.press_and_release
    # keyboard.write(msgs[random.randint(0,msgLen)])
    keyboard.write(msgs[count])
    keyboard.press_and_release("enter")
    count+=1
    time.sleep(1)

