from turtle import Turtle, Screen
P1_SCORE_POSITION = (-200, 230)
P2_SCORE_POSITION = (200, 230)
ALIGN = "center"
FONT = ('Chalkduster', 50, 'normal')


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.draw_central_line()
        self.p1_score = 0
        self.p2_score = 0
        self.score_update()

    @staticmethod
    def draw_central_line():
        t = Turtle()
        t.pensize(5)
        t.penup()
        t.color("white")
        t.goto(0, -280)
        t.setheading(90)
        while t.ycor() < 280:
            t.pendown()
            t.fd(20)
            t.penup()
            t.fd(20)

        t.hideturtle()

    def score_update(self):
        self.clear()
        self.color("white")
        self.goto(P1_SCORE_POSITION)
        self.write(f"{self.p1_score}", align=ALIGN, font=FONT)
        self.goto(P2_SCORE_POSITION)
        self.write(f"{self.p2_score}", align=ALIGN, font=FONT)

    def get_point(self, player):
        if player == "P1":
            self.p1_score += 1
        else:
            self.p2_score += 1
        self.score_update()

    def game_over(self, player_num):
        self.goto(0, 40)
        self.color("red")
        self.write(f"Winner", align=ALIGN, font=FONT)
        self.goto(0, -40)
        self.write(f"Player {player_num}", align=ALIGN, font=FONT)
        self.goto(0, -100)
        self.color("green")
        self.write(f"New Game?    Press \"y\"", align=ALIGN, font=('Chalkduster', 25, 'normal'))

    def new_game(self):
        self.p1_score = 0
        self.p2_score = 0
        self.score_update()


# -----------------------------test zone--------------------------------
if __name__ == "__main__":
    fonts_list = ['Hannotate TC', 'Hannotate SC', 'Hiragino Sans CNS', 'Hiragino Sans GB', 'STFangsong', 'STSong',
                  'STHeiti', 'STKaiti', 'Xingkai TC', 'Xingkai SC', 'Songti TC', 'Songti SC', 'Wawati TC', 'Wawati SC',
                  'LingWai TC', 'LingWai SC', 'Baoli TC', 'Baoli SC', 'Yuppy TC', 'Yuppy SC', 'Heiti TC', 'Heiti SC',
                  'Yuanti TC', 'Yuanti SC', 'Kaiti TC', 'Kaiti SC', 'BiauKai', 'HanziPen TC', 'HanziPen SC',
                  'Libian TC',
                  'Libian SC', 'SimSong', 'Weibei TC', 'Weibei SC', 'PingFang HK', 'PingFang TC', 'PingFang SC',
                  'Apple LiGothic', 'Apple LiSung', 'LiSong Pro', 'LiHei Pro', 'Lantinghei TC', 'Lantinghei SC',
                  'Academy Engraved LET', 'Al Bayan', 'Al Nile', 'Al Tarikh', 'American Typewriter', 'Andale Mono',
                  'Apple Braille', 'Apple Chancery', 'Apple Color Emoji', 'Apple SD Gothic Neo', 'Apple Symbols',
                  'AppleGothic', 'AppleMyungjo', 'Arial', 'Arial Black', 'Arial Hebrew', 'Arial Hebrew Scholar',
                  'Arial Narrow', 'Arial Rounded MT Bold', 'Arial Unicode MS', 'Avenir', 'Avenir Next',
                  'Avenir Next Condensed', 'Ayuthaya', 'Baghdad', 'Bangla MN', 'Bangla Sangam MN', 'Baskerville',
                  'Beirut',
                  'Big Caslon', 'BM Dohyeon', 'BM Hanna 11yrs Old', 'BM Hanna Air', 'BM Hanna Pro', 'BM Jua',
                  'BM Kirang Haerang', 'BM Yeonsung', 'Bodoni 72', 'Bodoni 72 Oldstyle', 'Bodoni 72 Smallcaps',
                  'Bodoni Ornaments', 'Bradley Hand', 'Brush Script MT', 'Chalkboard', 'Chalkboard SE', 'Chalkduster',
                  'Charter', 'Cochin', 'Comic Sans MS', 'Copperplate', 'Corsiva Hebrew', 'Courier New', 'Damascus',
                  'DecoType Naskh', 'Devanagari MT', 'Devanagari Sangam MN', 'Didot', 'DIN Alternate', 'DIN Condensed',
                  'Diwan Kufi', 'Diwan Thuluth', 'Euphemia UCAS', 'Farah', 'Farisi', 'Futura', 'Galvji',
                  'GB18030 Bitmap',
                  'Geeza Pro', 'Geneva', 'Georgia', 'Gill Sans', 'Grantha Sangam MN', 'Gujarati MT',
                  'Gujarati Sangam MN',
                  'GungSeo', 'Gurmukhi MN', 'Gurmukhi MT', 'Gurmukhi Sangam MN', 'HeadLineA', 'Hei', 'Helvetica',
                  'Helvetica Neue', 'Herculanum', 'Hiragino Maru Gothic ProN', 'Hiragino Mincho ProN', 'Hiragino Sans',
                  'Hoefler Text', 'Impact', 'InaiMathi', 'ITF Devanagari', 'ITF Devanagari Marathi', 'Kai', 'Kailasa',
                  'Kannada MN', 'Kannada Sangam MN', 'Kefa', 'Khmer MN', 'Khmer Sangam MN', 'Klee', 'Kohinoor Bangla',
                  'Kohinoor Devanagari', 'Kohinoor Gujarati', 'Kohinoor Telugu', 'Kokonor', 'Krungthep',
                  'KufiStandardGK',
                  'Lao MN', 'Lao Sangam MN', 'Lucida Grande', 'Luminari', 'Malayalam MN', 'Malayalam Sangam MN',
                  'Marker Felt', 'Menlo', 'Microsoft Sans Serif', 'Mishafi', 'Mishafi Gold', 'Monaco', 'Mshtakan',
                  'Mukta Mahee', 'Muna', 'Myanmar MN', 'Myanmar Sangam MN', 'Nadeem', 'Nanum Brush Script',
                  'Nanum Gothic',
                  'Nanum Myeongjo', 'Nanum Pen Script', 'New Peninim MT', 'Noteworthy', 'Noto Nastaliq Urdu',
                  'Noto Sans Kannada', 'Noto Sans Myanmar', 'Noto Sans Oriya', 'Noto Serif Myanmar', 'Optima',
                  'Oriya MN',
                  'Oriya Sangam MN', 'Osaka', 'Palatino', 'Papyrus', 'Party LET', 'PCMyungjo', 'Phosphate', 'PilGi',
                  'Plantagenet Cherokee', 'PSL Ornanong Pro', 'PT Mono', 'PT Sans', 'PT Sans Caption', 'PT Sans Narrow',
                  'PT Serif', 'PT Serif Caption', 'Raanana', 'Rockwell', 'Sana', 'Sathu', 'Savoye LET',
                  'Shree Devanagari 714', 'SignPainter', 'Silom', 'Sinhala MN', 'Sinhala Sangam MN', 'Skia',
                  'Snell Roundhand', 'STIX Two Math', 'STIX Two Text', 'Sukhumvit Set', 'Symbol', 'Tahoma', 'Tamil MN',
                  'Tamil Sangam MN', 'Telugu MN', 'Telugu Sangam MN', 'Thonburi', 'Times New Roman',
                  'Toppan Bunkyu Gothic',
                  'Toppan Bunkyu Midashi Gothic', 'Toppan Bunkyu Midashi Mincho', 'Toppan Bunkyu Mincho', 'Trattatello',
                  'Trebuchet MS', 'Tsukushi A Round Gothic', 'Tsukushi B Round Gothic', 'Verdana', 'Waseem', 'Webdings',
                  'Wingdings', 'Wingdings 2', 'Wingdings 3', 'YuGothic', 'YuKyokasho', 'YuKyokasho Yoko', 'YuMincho',
                  'YuMincho +36p Kana', 'Zapf Dingbats', 'Zapfino']
    test = Turtle()
    test.color("white")
    test.penup()
    test.goto(-250, 0)
    screen = Screen()
    screen.screensize(canvwidth=600, canvheight=30000)
    screen.bgcolor("black")
    for font in fonts_list:
        test.write(f"1234567890 ------------->{font}", align="left", font=(font, 20, "normal"))
        test.goto(-250, test.ycor()-35)
    screen.exitonclick()
