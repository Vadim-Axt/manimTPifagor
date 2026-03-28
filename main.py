from typing import Self

import numpy as np
from manim import *

config.frame_width = 32
config.frame_height = 18

config.fps = 60

class Main(Scene):
    def construct(self):
        teorema_Pifagora = Text('Теорема Пифагора')

        a_c = np.array([4, 0, 0])
        b_c = np.array([0, 3, 0])
        c_c = np.array([0, 0, 0])

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

        number_theorem = MathTex('a^2 + b^2 = c^2')

        number_theorem.move_to(UP*5).scale(2)

        self.play(Write(number_theorem))
        self.wait(1)

        a = Text('a').next_to(midAC, DOWN)
        b = Text('b').next_to(midBC, LEFT)
        c = Text('c').next_to(midAB, UR)

        self.play(Write(a, run_time=1.9), Write(b, run_time=1.5), Write(c, run_time=1.1))

        self.wait(1)

        c_Square = Square(5, color=YELLOW, fill_color=YELLOW, fill_opacity=0.5)
        a_Square = Square(4, color=GREEN, fill_color=GREEN, fill_opacity=0.3 )
        b_Square = Polygon([0, 0, 0], [0, 3, 0], [3, 3, 0], [3, 0, 0], color=BLUE, fill_color=BLUE, fill_opacity=0.3)




        self.play(FadeOut(number_theorem))
        self.play(Create(c_Square), Create(a_Square), Create(b_Square))
        self.play(FadeOut(a), FadeOut(b), FadeOut(c), FadeOut(dotA), FadeOut(dotB), FadeOut(dotC))
        self.play(c_Square.animate.move_to([3.5, 3.5, 0]))
        self.play(a_Square.animate.move_to([2, -2, 0]))
        self.play(b_Square.animate.move_to([-1.5, 1.5, 0]))
        self.play(c_Square.animate.rotate(-np.arcsin(3/5)))
        self.wait(2)

        self.play(c_Square.animate.rotate(np.arcsin(3/5)))
        self.play(c_Square.animate.move_to([7, 2.5, 0]))

        self.play(FadeOut(tringle))

        self.play(b_Square.animate.move_to([-7.5, 1.5, 0]), run_time=2)
        self.play(a_Square.animate.move_to([-1.5, 2, 0]))

        plus = MathTex('+')
        equals = MathTex('=')
        self.play(FadeIn(plus.scale(2).move_to([-4.75, 1.5, 0])), FadeIn(equals.scale(2).move_to([2.5, 1.5, 0])))


        self.play(b_Square.animate.stretch(5/3, dim=1), run_time=1)
        self.play(b_Square.animate.stretch(9/(3*3*(5/3)), dim=0), run_time=1)
        self.play(b_Square.animate.shift([0, 1, 0]))

        self.play(a_Square.animate.stretch(5/4, dim=1))
        self.play(a_Square.animate.stretch(16/(4*4*1.25), dim=0))
        self.play(a_Square.animate.shift([.05, .5, 0]))
        self.play(c_Square.animate.shift([-.5, 0, 0]))

        self.play(FadeOut(plus), FadeOut(equals))

        self.play(b_Square.animate.shift([2.55, 0, 0]), a_Square.animate.shift([-1, 0, 0]), c_Square.animate.shift([-3, 0, 0]))
        self.wait(3)

        ab_Squares = VGroup(a_Square, b_Square)


        self.play(ab_Squares.animate.move_to([0, 0, 0]), c_Square.animate.move_to([0, 0, 0]))


        self.wait(1)

        end_text = Text('Спасибо за просмотр')

        self.play(FadeOut(ab_Squares), FadeOut(c_Square))

        self.play(Write(end_text))

        self.wait(1)

