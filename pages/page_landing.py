import dash_html_components as html

img = html.Img(
    src="https://mithi.github.io/robotics-blog/v2-hexapod-1.gif",
    style={"width": "100%", "height": "auto"},
)

layout = html.Div(
    [
        html.Div(img, style={"width": "20%", "height": "auto"}),
        html.Div(html.Br(), style={"width": "auto", "height": "auto"}),
    ],
    style={"display": "flex", "flex-direction": "row"},
)
