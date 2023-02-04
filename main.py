import pandas as pd
from PIL import Image
from streamlit_timeline import timeline
import streamlit as st
import plotly.graph_objects as go
# setting page title
st.set_page_config(page_title="🚀Sreerag Portfolio Page 🚀")

# loading style sheets
with open("style1.css") as f1:
    st.markdown('<style>{}</style>'.format(f1.read()), unsafe_allow_html=True)

# """Sidebar Added social media tags and Resume download"""
st.sidebar.caption('Wish to connect with me?')
st.sidebar.write("\n")
st.sidebar.write("\n")
st.sidebar.write("[📧 Gmail](sreeragkolath@gmail.com)")
st.sidebar.write("\n")
st.sidebar.write("[🗒️ LinkedIn](https://www.linkedin.com/in/sreerag-radhakrishnan-599036130/)")
st.sidebar.write("\n")
st.sidebar.write("[🕹️ GitHub](https://github.com/SreeragKolath/)")
st.sidebar.write("\n")
st.sidebar.write("[🍔 Substack](https://sreerag.substack.com/)")
st.sidebar.write("\n")
with st.sidebar.expander('Address...'):
    with st.spinner(text="Address..."):
        st.caption('Ramanilayam(H),\n')
        st.caption('Edavetty(P.o),\n')
        st.caption('Thodupuzha,Idukki,Kerala,\n')
        st.caption('Pin: 685588\n')
st.sidebar.write("\n")
pdf_file = open('pdf/Sreerag_cv.pdf', 'rb')
st.sidebar.download_button('Download Resume',  pdf_file,  file_name='Sreerag_cv.pdf',mime='pdf')
# ----sidebar ends ------

#'''General Settings'''

NAME = "SREERAG K"
DESCRIPTION = """
Hello.World🖐️🖐️! I'm a Passionate AI Developer with 3+ years of experience in application design, development, testing and deployment. Highly experienced in writing codes and algorithms as well as building complex AI/ML models using various programming languages.
"""
# --- Info Section ---
profile_pic = Image.open('sreerag.jpg')
col1, col2 = st.columns(2)
with col1:
    st.image(profile_pic, width=230)
with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
st.write("\n")
# --- Skills ---
st.subheader("SKILLS👩‍💻")
st.write('\n')
skills = ["• Python", "• Pandas", "• Numpy", "• Bokeh", "• Latex", "• SQL", "• Data Analysis", "• Data Visualization", "• NLP", "• Machine Learning", "• AI", "• Git", '• Excel', '• Latex', '• Linux/Ubuntu', '• Plotly']
cola,colb,colc,cold=st.columns(4)
with cola:
        st.markdown(skills[0])
with colb:
        st.markdown(skills[1])
with colc:
        st.markdown(skills[2])
with cold:
        st.markdown(skills[3])
st.write("\n")

cola,colb,colc,cold=st.columns(4)
with cola:
        st.markdown(skills[4])
with colb:
        st.markdown(skills[5])
with colc:
        st.markdown(skills[6])
with cold:
        st.markdown(skills[7])

st.write("\n")

cola,colb,colc,cold=st.columns(4)
with cola:
        st.markdown(skills[8])
with colb:
        st.markdown(skills[9])
with colc:
        st.markdown(skills[10])
with cold:
        st.markdown(skills[11])

st.write("\n")
cola,colb,colc,cold=st.columns(4)
with cola:
        st.markdown(skills[12])
with colb:
        st.markdown(skills[13])
with colc:
        st.markdown(skills[14])
with cold:
        st.markdown(skills[15])

st.write("\n")

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History🛠️")
st.write("---")

# --- JOB 1
st.write("**Associate Software Engineer  | Techversant Infotech**")
st.write("08/2019 - 12/2022")
st.write(
    """
- ► Design and execute well-engineered, easy-to-maintain, reliable, and bug-free code for various applications in collaboration with other AI engineers, Data Scientists, Programmers and Software personnels.
- ► Collaborated in 7+ AI driven solutions/products and be a part of the core Developer team.'
- ► Assisted R&D department in developing different projects.

"""
)
st.write("🚧", "**Projects**")
st.write('Survey Recommendation')
with st.expander('More info...'):
    with st.spinner(text="More info..."):
        st.write("• Collaborated to develop and AI based application for Survey Recommendation engine which is intended to provide Recommendation of the best available surveys to the requesting user.\n")
        st.write("• Contributed to data collection, algorithm development and AI model perfomance tuning\n")
        st.write("• Worked on API development and continuous code optimzation.\n")

st.write('Safari Roof Top AI')
with st.expander('More info...'):
    with st.spinner(text="More info..."):
        st.write("It is a AI based Engine used for finding rooftop area for placing solar panels. Associated with the project for handling image extraction and preprocessing modules.\n")
        st.write("• Data Collection from AWS.\n")
        st.write("• Image prepossessing and Annotation.\n")
        st.write("• Devolepment of Customized model for Roof Detection.\n")
        st.write("• Devolepment of Customized model for Roof Detection.\n")

st.write('AI Based Sentimental Analysis Engine')
with st.expander('More info...'):
    with st.spinner(text="More info..."):
        st.write("It’s an AI based Sentiment Analysis Engine which is intended to Find the sentiment of a collected data by means of text sentiment, emoji sentiment, emotional sentiment from visuals, etc.\n")
        st.write("• Data Acquisition of Arabic sentences/tweets and Data Preprocessing.\n")
        st.write("• Subclass Categorization. \n")
        st.write("• Code Optimization and Code Enhancement.\n")
        st.write("• Model Development and Model Integration.\n")

# --- Career Transition ---
st.write('\n')
st.subheader("Career Transition")
st.write("---")
with st.spinner(text="Building line"):
    with open('transition.json', "r") as f:  #Loading from json
        data = f.read()
        timeline(data, height=500)

# --- end ---