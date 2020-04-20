import plotly.graph_objects as go
from pprint import pprint
import json

with open('data.json', 'r') as f:
    data = json.loads(f.read())

# fig = go.Figure(layout=dict(
#     title="Curve Graph",
#     xaxis_title="Total Deaths",
#     yaxis_title="Total Cases",
#     showlegend=True,
#     legend= {
#         'itemsizing': 'constant',
#     },
# ))
fig = go.Figure()
color = 0
frames = []

# fig.update_layout(
#     title="Curve Graph",
#     xaxis_title="Total Deaths",
#     yaxis_title="Total Cases",
#     showlegend=True,
#     legend= {
#         'itemsizing': 'constant',
#     },
# )

for _, i in data.items():
    
    main_list = {  # init value
    'Total Deaths': [],
    'Total Cases': [],
    'Active Cases': [],
    'Date': [],
    }
    color += 1

    for j in i:
        # main_list['Total Deaths'].append(j['deaths'])
        # main_list['Total Cases'].append(j['total_cases'])
        # main_list['Active Cases'].append(j['active_cases']/4000)
        # main_list['Date'].append(j['date'])

        frames.append(go.Frame(data=[go.Scatter(
        # fig.add_trace(go.Scatter(
            x=[ j['deaths'] ],
            y=[ j['total_cases'] ],
            mode='markers',
            marker={
                'size':[ j['active_cases']/4000 ],
                'color':color,
            },
            customdata=[ j['country_name'], j['active_cases'] ],
            name=j['country_name'],
            hovertemplate=
            'Country: %{customdata[0]},<br><br>'+
            'Total Deaths(x): %{x:s},<br>'+
            'Total Cases(y): %{y:s},<br>'+
            'Active Cases(size): %{customdata[1]:s}'+
            '<extra></extra>',
        )],
        layout=go.Layout(width=600, height=600,
            # xaxis=dict(range=[xm, xM], autorange=False, zeroline=False),
            # yaxis=dict(range=[ym, yM], autorange=False, zeroline=False),
            title="Moving Frenet Frame Along a Planar Curve",
            hovermode="closest",
            updatemenus=[dict(type="buttons",
                buttons=[dict(label="Play",
                method="animate",
                    args=[None])])]),#, layout=go.Layout(
        #     annotations=[
        #         go.layout.Annotation(
        #             text='Some<br>multi-line<br>text',
        #             align='left',
        #             showarrow=False,
        #             xref='paper',
        #             yref='paper',
        #             x=1.1,
        #             y=0.8,
        #             bordercolor='black',
        #             borderwidth=1
        #         )
        # ]
        ))


# fig = px.scatter(
#     main_list,
#     x='Total Deaths',
#     y='Total Cases',
#     size='Active Cases',
#     color='Country',
#     animation_frame='Date',
#     # hover_name='Country',
#     size_max=100,
#     range_x=[0,14000], 
#     range_y=[0,200000],
# )

# fig.add
fig.show(frames=frames)
# with open('html.html', '+w') as f: f.write(fig.to_html())