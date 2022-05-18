import json
from pyecharts import options as opts
from pyecharts.charts import HeatMap
from pyecharts.faker import Faker
with open("les-miserables.json", "r", encoding="utf-8") as f:
    j = json.load(f)
    nodes = j["nodes"]
    links = j["links"]
    categories = j["categories"]


ifo=[ (i['name'] ,i['category'])   for i in nodes]
ifo.sort(key=lambda x:(x[1]))

dt={}
for i,val  in enumerate(ifo):
    dt[val[0]]=i
ifn=list(dt.keys())

name=[i['name'] for i in nodes]
n=len(name)

ls=[]
for d in links:
    i,j=int(d['source']),int(d['target'])
    k=nodes[i]['category'] *10
    i,j=name[i],name[j]
    i,j=dt.get(i),dt.get(j)
    
    ls.append( [ i,j, k]  )
    
for i in range(n):
    ls.append([i,i,100])


c = (
    HeatMap(init_opts=opts.InitOpts(width="1500px", height="1000px"))
    .add_xaxis( ifn )
    .add_yaxis(
        "",
        ifn,
        ls,
        label_opts=opts.LabelOpts(is_show=True, position="inside"),
    )
    .set_global_opts(
        title_opts=opts.TitleOpts(title="matrix"),
        visualmap_opts=opts.VisualMapOpts(),
    )
    .render("heapmap.html")
)

# c.render_notebook()
