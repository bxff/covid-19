from manimlib.imports import *
import json

class MainScene(GraphScene):
    CONFIG = {
        "y_max" : 2,
        "y_min" : 0,
        "x_max" : 31,
        "x_min" : 0,
        "y_tick_frequency" : 1, 
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
    def construct(self):
        # with open('data.json', 'r') as f:
        #     data = json.loads(f.read())
        # self.setup_axes(animate=True)
        # def func(x):
        #         # return data['usa'][int(x)]['ratio']
        #         # print(data['usa'][int(x)]['ratio'])
        #         return data['usa'][int(x)]['ratio']
        # def func1(x):
        #         # return data['usa'][int(x)]['ratio']
        #         # print(data['usa'][int(x)]['ratio'])
        #         return data['india'][int(x)]['ratio']
        # def func2(x):
        #         # return data['usa'][int(x)]['ratio']
        #         # print(data['usa'][int(x)]['ratio'])
        #         return data['france'][int(x)]['ratio']
        # def func3(x):
        #         # return data['usa'][int(x)]['ratio']
        #         # print(data['usa'][int(x)]['ratio'])
        #         return data['china'][int(x)]['ratio']
        # graph=self.get_graph(func)
        # graph1=self.get_graph(func1)
        # graph2=self.get_graph(func2)
        # graph3=self.get_graph(func3)
        # # area = self.get_area(graph,-0.0001, 0.0001)
        # graph.set_stroke(width=1)
        # graph.set_points
        # # graph.generate_points()
        # # print(self.points)
        # graph1.set_stroke(width=1)
        # graph2.set_stroke(width=1)
        # graph3.set_stroke(width=1)
        # self.play(
        # ShowCreation(graph),
        # ShowCreation(graph1),
        # ShowCreation(graph2),
        # ShowCreation(graph3)
        # )

        self.setup_axes()
        # print(self.point_to_coords([1,1,0]))
        x = self.coords_to_point(1,1)
        self.add(SmallDot(x))
        # self.add(Dot([1,1,0]))

        self.wait()

