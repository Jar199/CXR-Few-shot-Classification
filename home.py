import streamlit as st
from PIL import Image
from st_pages import Page, Section, show_pages, add_page_title

st.title('Few-shot Classification for Chest X-ray diagnosis')
# emoji: https://streamlit-emoji-shortcodes-streamlit-app-gwckff.streamlit.app/
st.header('using MIMIC-CXR & CLIP')

st.image(Image.open('/Users/kim-yelin/Documents/DeepDaiv/demo/main.png'))
# st.caption('MIMIC 데이터셋과 CLIP을 이용한 구조화된 임상적 소견 예측')

st.image(Image.open('/Users/kim-yelin/Documents/DeepDaiv/demo/text.png'))

col1, col2 = st.columns(2)

with col1:
    pathology = st.selectbox(
      'Pathology',
      ('pneumothorax', 'pneumonia', 'fluid overload/heart failure', 
      'consolidation', 'pleural effusion', 'atelectasis', 
      'pulmonary edema/hazy opacity', 'lung opacity', 'enlarged cardiac silhouette'),
      # index=None,
      # placeholder="Select pathology"
    )

with col2: 
    location = st.selectbox(
      'Location',
      ('left apical zone', 'left lower lung zone', 'left lung', 
      'left mid lung zone', 'left upper lung zone', 
      'right apical zone', 'right lower lung zone', 'right lung',
      'right mid lung zone', 'right upper lung zone', 
      'left hilar structures', 'right hilar structures', 
      'left costophrenic angle', 'right costophrenic angle',
      'mediastinum', 'upper mediastinum',
      'cardiac silhouette', 'trachea')
    )

st.write('Template : ', pathology, 'in the', location)

show_pages([
        Page("home.py", "Home", "🏠"),
        Page("test.py", "Test", icon="🫁"),
])
