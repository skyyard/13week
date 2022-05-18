import json
from pyecharts import options as opts
from pyecharts.charts import HeatMap
from pyecharts.faker import Faker
with open("les-miserables.json", "r", encoding="utf-8") as f:
    j = json.load(f)
    nodes = j["nodes"]
    links = j["links"]
    categories = j["categories"]



name=[i['name'] for i in nodes]

ls=[]

for d in links:
    i,j=int(d['source']),int(d['target'])
    k=nodes[i]['category'] *10
    ls.append( [ i,j, k]  )
    
for i in range(len(name)):
    ls.append([i,i,100])


c = (
    HeatMap(init_opts=opts.InitOpts(width="1500px", height="1000px"))
    .add_xaxis( name )
    .add_yaxis(
        "",
        name,
        ls,
        label_opts=opts.LabelOpts(is_show=True, position="inside"),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="matrix"),
        visualmap_opts=opts.VisualMapOpts(),
    )
    .render("no_heapmap.html")
)

# c.render_notebook()
