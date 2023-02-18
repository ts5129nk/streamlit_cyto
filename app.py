import streamlit as st
from st_cytoscape  import cytoscape

st.set_page_config(layout="wide")


st.title("Hello Cytoscape.js with Streamlit")

layout_set = st.sidebar.selectbox('select layout',('cose','breadthfirst','circle','grid'))

node_size = 60

elements = [
    {"data": {"id": "bird","img_url":'https://live.staticflickr.com/7272/7633179468_3e19e45a0c_b.jpg'}},
    {"data": {"id": "cat","img_url":'https://live.staticflickr.com/1261/1413379559_412a540d29_b.jpg'}},
    {"data": {"id": "ladybug","img_url":'https://live.staticflickr.com/3063/2751740612_af11fb090b_b.jpg'}},
    {"data": {"id": "aphid","img_url":'https://live.staticflickr.com/8316/8003798443_32d01257c8_b.jpg'}},
    {"data": {"id": "rose","img_url":'https://live.staticflickr.com/5109/5817854163_eaccd688f5_b.jpg'}},
    {"data": {"id": "grasshopper","img_url":'https://live.staticflickr.com/6098/6224655456_f4c3c98589_b.jpg'}},
    {"data": {"id": "plant","img_url":'https://live.staticflickr.com/3866/14420309584_78bf471658_b.jpg'}},
    {"data": {"id": "wheat","img_url":'https://live.staticflickr.com/2660/3715569167_7e978e8319_b.jpg'}},
    { "data": { "source": 'cat', "target": 'bird' } },
    { "data": { "source": 'bird', "target": 'ladybug' } },
    { "data": { "source": 'bird', "target": 'grasshopper' } },
    { "data": { "source": 'grasshopper', "target": 'plant' } },
    { "data": { "source": 'grasshopper', "target": 'wheat' } },
    { "data": { "source": 'ladybug', "target": 'aphid' } },
    { "data": { "source": 'aphid', "target": 'rose' } }
]
stylesheet = [
    {"selector": "node", "style": {"label":"data(id)","width": node_size, "height": node_size,
                    'background-image': "data(img_url)",
                    'background-fit':'cover'}},
    {"selector": "edge", "style": {"width": 4,'target-arrow-shape': 'triangle','curve-style': 'straight'}},
]
layout ={"name":layout_set,"padding": 20}


selected = cytoscape(elements, stylesheet,height="600px",layout=layout,
        key="graph",)

st.write(selected)
for i in selected["nodes"]:
    st.sidebar.info(i + ' is selected')
