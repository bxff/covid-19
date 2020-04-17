from manimlib.imports import *
import json

# To run use:
# manum curve_manim.py MainScene -p
#                                ^^ stands for preview, which will play the scence as soon as its ready 

class MainScene(GraphScene):
    CONFIG = {  #  <<< Configration for manim graphs
        "y_max" : 2,
        "y_min" : 0,
        "x_max" : 31,
        "x_min" : 0,
        "y_tick_frequency" : 0.25, 
        "x_tick_frequency" : 1, 
        "axes_color" : BLUE, 
        "y_labeled_nums": range(0,2+1,1),
        "x_labeled_nums": range(0,31+1,2),
        "x_axis_label" : "$days$ $of$ $march$",
        "y_axis_label" : "$frequncy$",
        "x_axis_width":12.75,
        "y_axis_height": 6.75,
        "graph_origin": 3.25 * DOWN + 6.25 * LEFT,
        "radius": DEFAULT_DOT_RADIUS,   
    }

    def construct(self):  # <<< main function
        self.setup_axes(animate=True)  # <<< Creates the graph outline
        usa_color = TextMobject('USA: red').set_color(RED).scale(0.5).to_edge(UR)
        china_color = TextMobject('China: green').set_color(GREEN).scale(0.5).next_to(usa_color,DOWN+0.75).to_edge(RIGHT)
        self.play(
            Write(usa_color), 
            Write(china_color)
        )

        with open('data.json', 'r') as f:
            data = json.loads(f.read())  # <<< gets the data
        

        usa_dot = Dot(self.coords_to_point((1),data['usa'][0]['ratio']), color=RED)
        china_dot = Dot(self.coords_to_point((1),data['china'][0]['ratio']), color=GREEN)
        self.add(usa_dot, china_dot)
        for i in range(1, len(data['usa'])):
            usa_dot2 = Dot(self.coords_to_point((i+1),data['usa'][i]['ratio']), color=RED)
            china_dot2 = Dot(self.coords_to_point((i+1),data['china'][i]['ratio']), color=GREEN)

            self.play(
                Transform(usa_dot, usa_dot2), 
                Transform(china_dot, china_dot2), 
            run_time=0.1, rate_func=linear)

            self.remove(usa_dot, china_dot)

            usa_dot = usa_dot2
            china_dot = china_dot2
        self.wait()

