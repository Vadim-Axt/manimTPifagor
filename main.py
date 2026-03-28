import numpy as np
from manim import *

config.frame_width = 32
config.frame_height = 18

class Main(Scene):
    def construct(self):
        teorema_Pifagora = Text('Теорема Пифагора')


        a_c = np.array([3, -1, 0])
        b_c = np.array([-1, 2, 0])
        c_c = np.array([-1, -1, 0])

        midAB = (a_c + b_c) / 2
        midAC = (a_c + c_c) / 2
        midBC = (b_c + c_c) / 2

        dotAText = Text('A')
        dotBText = Text('B')
        dotCText = Text('C')


        dotA = Dot(a_c)
        dotB = Dot(b_c)
        dotC = Dot(c_c)



        tringle = Polygon(a_c, b_c, c_c, color=YELLOW_C)

        teorema_Pifagora.move_to(UP*4)
        first_tringle = Triangle()


        self.add(teorema_Pifagora)
        self.add(first_tringle)
        self.wait(1)
        self.play(ReplacementTransform(first_tringle, tringle))
        self.add(
            dotA,
            dotB,
            dotC,
            dotAText.next_to(dotA, DR),
            dotBText.next_to(dotB, UL),
            dotCText.next_to(dotC, DL),
        )
        self.wait(1)

        five = Text("5")
        three = Text("3")
        four = Text("4")

        self.play(five.animate.next_to(midAB, UR))
        self.wait(1)
        self.play(three.animate.next_to(midBC, LEFT))
        self.wait(.7)
        self.play(four.animate.next_to(midAC, DOWN))
        self.wait(.3)

        self.play(
            FadeOut(teorema_Pifagora, run_time=1.4),
                  FadeOut(dotAText, run_time=2.6),
                  FadeOut(dotBText, run_time=3.2),
                  FadeOut(dotCText, run_time=4.1),
                  FadeOut(five, run_time=1.6),
                  FadeOut(three, run_time=2.2),
                  FadeOut(four, run_time=3.7),

        )
        self.wait(1)

