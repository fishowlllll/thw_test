init python:
    anLove = 0
    lxLove = 0
    todLove = 0
    class Love:
        name = "null"
        love = 0
        def __init__(self, name):
            self.name = name
            self.love = 0
        def myLove(self):
            return self.name + self.love
            #print(self.name + self.love)
    class Value:
        name = "null"
        medi = 0
        sword = 0
        phi = 0
        def __init__(self, name):
            self.name = name
            self.medi = 0
            self.sword = 0
            self.phi = 0
    anlove = Love("an")
    phvalue = Value("ph")

# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

#define e = Character("艾琳")
define ph = Character("Pharsalia",image="ph")
define an = Character("Anneliese",image="an")
define lx = Character("Luxure",image="lx")
define ar = Character("Arrogant",image="ar")

# 游戏在此开始。

label start:

    #$ anLove = 0
    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为“bg room.png”或“bg room.jpg”）来显示。

    #scene bg room
    scene bird line

    "未知的声音""你又回到这里了啊。"
    "未知的声音""如果能再次回到那个下午，回到一切刚刚开始的地方，结局会不会有所不同呢？"
    "未知的声音""让我们看一下吧，这一次能做到什么程度。"
    "未知的声音""准备好了就开始吧。"
    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # “eileen happy.png”的文件来将其替换掉。

    scene roominside1
    with fade
    #show eileen happy
    show ph at left
    show temp at right
    default searched = False
    # 此处显示各行对话。


    "母亲""你醒啦，Pharsalia，下午有什么计划？去森林玩吗？"
    "母亲""我就不去了，不过你可以为我采一些花来，插到那个花瓶里，我们一起好好装饰一下这间屋子。"

menu:

    "去森林":
        jump searchforest

    "不去":
        jump stayAtHome

label searchforest:
    $ searched = True
    ph "好哦，那我出去玩啦。"
    ph "出去看看吧。"
    scene forest1
    with fade
    show ph at left
    ph "喔……森林里面的路还挺复杂的。"
    ph "左转，右转，左转再往右……"
    ph "这里的灌木丛比花园里面的大好多，感觉就算把自己藏在里面都不会被发现呢。"
    ph "刻着字的石碑，下面有按钮。唔……果然还是不要乱碰。"
    ph "出来有一段时间了，回去吧。"

    scene roominside1
    with fade

    ph "我回来啦！妈妈，这些花给您！"
    jump comeback

label stayAtHome:

    ph "不用了，今天下午我想和妈妈在一起。"
    "*敲门声"
    "母亲""我去开门。"
    "母亲""你来这里做什么？"
    "姑姑""我来看看你们在这里过得是否习惯。"
    jump comeback

label comeback:

    show ph at left
    show temp at right
    show temp at right
    ph "姑姑……？"
    "母亲""Pharsalia，你的衣服好像有点脏了，到房间里来，我给你换一套衣服。"
    "姑姑""……"
    scene room1
    with fade
    show ph at left
    show temp at right
    "母亲""Pharsalia，听我说，现在有一件事。"
    "母亲""一会你要从这个密道出去，跑到森林的尽头，中途不要停留，无论听到什么声音都不要回头。"
    ph "可是为什么呢？"
    "母亲""没有为什么，这是……这是一个游戏，我们在和姑姑玩一个游戏。"
    ph "游戏？"
    "母亲""是的，她来追我们，我们不要被她抓到，这样就是我们赢了。"
    "母亲""姑姑和妈妈打了个赌，你也希望妈妈赢吧？那就按妈妈刚才说的做，你是个好孩子，对吧？"
    "母亲""跑到森林的尽头就会有人来接你，是妈妈拜托她来的，你跟着她走就可以了。"
    "*敲门声"
    "母亲""要开始了，Pharsalia，快走！"
    scene secretpath
    with fade
    "母亲""（声音从门的另一边传来）走吧，走吧……Pharsalia，不要回头……"
    show ph at left
    ph "妈妈……"

menu:

    "立刻就走":
        jump runimmediatly

    "停留一会":
        jump stayforawhile

label runimmediatly:
    scene forest1
    with fade
    show ph at left
    if searched:
        ph "刚才看到的路是在那边，只要到达那个地方……"
        jump meetAn
    else:
        ph "森林的出口是在什么地方？这里都是没有走过的路啊。"
        jump end1


label stayforawhile:
    scene secretpath
    show ph at left
    ph "到底发生了什么事？"
    ph "妈妈……就这样不管也不行吧，在这里再等一会好了。"
    "*门被暴力打开的声音"
    "姑姑""哎呀，没人回应我就只好自己开门进来了。"
    "姑姑""不愧是你啊，Mei，这么快就让她藏起来了？"
    "母亲""我不会让你找到她。"
    "姑姑""那就，来试试看啊？"
    "*刀剑碰撞声"
    scene secretpathblood
    show ph at left

    "母亲""……"
    "姑姑""Pharsalia，你在这里对吧？姑姑要过来了哦？"
    jump end1

    return
label end1:
    scene died
    with fade
    "bad ending1 还没有正式开始就结束的故事"

    return
label meetAn:
    "最后一束阳光被群山掩去，你终于跑到了森林的尽头，湖边有人提着一盏油灯。"
    show an at right
menu:
    "询问":
        $anlove.love += 3
        ph "请问您是……？"
        an "我是Anneliese，来这里接你回去。"
        an "跟我来吧。"
        jump crossTheLake
    "牵她的手":
        $anlove.love += 5
        an "……"
        an "你不问我是谁，就这样信任我么？"
        an "我是Anneliese，来这里接你回去。"
        an "跟我来吧。"
        jump crossTheLake
label crossTheLake:
    scene lakeside
    with fade

    menu:

        "回忆":
            $phvalue.phi += 3
            "这是一个天气晴朗的夜晚，你仰起头，想起以前在家里的时候，母亲会抱着自己坐在窗前，念着“月明星稀，乌鹊南飞”的诗。"
            "那时的星与夜都比这郊野外的要朦胧，像隔着一层雾。你不解乌鹊南飞何意，只知道这种鸟儿不常见。"
            "船在湖面平稳地划出一道道波纹，你感觉从前的生活逐渐离自己远去了。"
            jump arrivenewhome

        "观察":
            $anlove.love += 3
            "在一片深蓝的夜色中，船头的白色身影尤为突出。暖黄色的灯光为她纯白色的长发和衣裙披上一层柔和的色彩。"
            "她注意到你的目光，回头温柔一笑，金色眼眸像夜空中初现的星，比你见过的任何金银珠宝都更耀眼。"
            an "休息一下吧，穿过这片湖很快就到家了。"
            jump arrivenewhome
label arrivenewhome:
    scene roominside1
    with fade
    "Anneliese帮你整理好了房间，一天累积下来的疲劳使你很快入睡了。"
    "第二天，第三天，第四天……Anneliese逐渐带你熟悉了这座庭院和周围的森林，她甚至为你找来了一些教材。"
    an "学习时有不懂的都可以问姐姐哦。"
    "这段时间学习什么呢？"
    menu:
        "魔药":
            $phvalue.medi += 5
            "魔药水平提高了！"
        "剑术":
            $phvalue.sword += 5
            "剑术水平提高了！"
        "哲学":
            $phvalue.phi += 5
            "哲学水平提高了！"
#    "an好感[anlove.love]"
#    jump learn
#    $strtemp = "trygohome"
#    jump trygohome
    "一天，一天，又一天。"
    "你看着矮墙外的森林从春末夏初的郁郁葱葱转变为深秋的金黄，来到这里竟已有半年了。这段时间Anneliese偶尔会出去大半天，而你从未离开过这座庭院。"
    "你想要回家，和妈妈一起喝下午茶，在城堡一角的小庭院玩一个下午，悄悄推开书房的门看爸爸在干什么。"
    "你的思念与日俱增，学习也有些心不在焉，也许Anneliese察觉到了，但她也没有提。"
    menu:
        "尝试回家":
            "今日Anneliese外出。你在窗台上看着她的身影逐渐消失在密林深处，转身走出庭院，凭记忆走向半年前到达这里的路。"
        "问Anneliese":
            ph "姐姐，为什么妈妈不来接我？"
            "Anneliese愣了一下，偏过头看向厨房的方向。"
            an "哎呀，到下午茶的时间了，我去准备茶点，等我一下哦。"
            "又是这样……无论你在什么时候提出这个问题，都会有事情让Anneliese消失一会，再回来时你就忘记这个问题了。"

label trygohome:
    "你尝试回家"

label learn:
    "这段时间学习什么呢？"
    menu:
        "魔药":
            $phvalue.medi += 5
            "魔药水平提高了！"
        "剑术":
            $phvalue.sword += 5
            "剑术水平提高了！"
        "哲学":
            $phvalue.phi += 5
            "哲学水平提高了！"
    return
    #end learn
    #jump expression strtemp

label lovetest:
    #$anlove.love += 5
    #$anlove.myLove()
    if anlove.love >= 5 :
        an "I like you."
    else:
        an "I dont like you."

#    $ anLove = anLove + 5
#    if anLove > 1 :
#        an "I like you."
#    else:
#        an "I dont like you."


    #ph "当您完善了故事、图片和音乐之后，您就可以向全世界发布了！"

    # 此处为游戏结尾。

    return
