import streamlit as st
from PIL import Image


languages = ['Python', 'Matlab']
st.title("Portfolio Martin Komák")
st.text("""Na tomto webe nájdete moju poslednú tvorbu v programovacích jazykoch
Python a Matlab. Prosím, vľavo si zvolte programovací jazyk, ktorý Vás zaujíma.""")

#vyber programovacieho jazyka
language = st.sidebar.selectbox("Ktorý programovaci jazyk chcete zobraziť?", ("Python", "Matlab"))
st.subheader("")
st.header("Moja tvorba v jazyku {}:".format(language))

if language == "Python":
    st.subheader("Model PR ovládaný hlasovými príkazmi")
    st.markdown("""Simulačný model priemyselného robota je vytvorený v module určenom na vizualizáciu - **PyVista**. 
    Cieľom bolo vytvoriť prostredie, v ktorom bude priemyselný robot riadený do jednotlivých targetov využitím hlasových
    príkazov. Video:""")
    vid_file1 = open("media\ovladany_hlasom_low.mp4", 'rb').read()
    st.video(vid_file1)

if language == "Python":
    st.subheader("")
    st.subheader("Mobilný robot v bludisku")
    st.markdown("""Simulačný model malého mobilného robota - micromouse a jeho ovládanie pomocou šípok na klávesnici.
Aktuálne sa na tomto projekte pracuje. Video:""")
    vid_file1 = open("media\labyrint.gif", 'rb').read()
    st.video(vid_file1)

if language == "Python":
    st.subheader("")
    st.subheader("Model PR ABB")
    st.markdown("Znázornenie prierezu robota v priestore spolu s jeho súsradnicovými systémami v jednotlivých kĺboch.")
    img = Image.open("media\pr2.jpg")
    st.image(img, caption="PR v Pythone")

if language == "Python":
    st.subheader("")
    st.subheader("Sieťový model PR")
    st.markdown("Na obrázku nižšie je znázornený trojuholníková sieť reprezentujúca 3D model PR.")
    img = Image.open("media\pr1.jpg")
    st.image(img, caption="Sieť PR")

if language == "Matlab":
    st.subheader("Kuka riadená neurónovou sieťou")
    st.markdown("""Na videu môžete vidieť 7 kĺbový priemyselný robot Kuka, ktorý je do 4 zvolených targetov
riadený pomocou natrénovanej neurónovej siete. Sieť bola trénovaná evolučnými algoritmami. Video:""")
    vid_file = open("media\Kukalow.wmv", 'rb').read()
    st.video(vid_file)

if language == "Matlab":
    st.subheader("")
    st.subheader('Mobilný robot v bludisku.')
    st.markdown("""Malý mobilný robot, ktorý chodí po bludisku a ktorého vizualizácia je upravená z dôvodu vyššieho 
výpočtového výkonu. Pri kolízii sa robot sfarbí na červeno. Video:""")
    vid_file4 = open("media\mybludiskolow.mp4", 'rb').read()
    st.video(vid_file4)

if language == "Matlab":
    st.subheader("")
    st.subheader('Konfigurácia robota vyžitím GA')
    st.markdown("""Na videu nižšie môžete vidieť obálku priemyselného robota s prekážkou a požadovaným targetom. Cieľom
bolo vytvoriť kinematiku priemyselného robota a pomocou genetických algoritmov nájsť vhodnú konfiguráciu. Video:""")
    vid_file1 = open("media\obalkalow.mp4", 'rb').read()
    st.video(vid_file1)

if language == "Matlab":
    st.subheader("")
    st.subheader('Hľadanie najkratšej dráhy v 2D priestore s prekážkou')
    st.markdown("""Program na hľadanie najkratšej dráhy v 2D priestore s prekážkou. Znázornené písmenka nám reprezentujú
obchádzanú prekážku. Dráha je vytvorená z desiatich bodov a ich sponicami. Video:""")
    vid_file = open("media\lowobchadzanie.mp4", 'rb').read()
    st.video(vid_file)

if language == "Matlab":
    st.subheader('')
    st.subheader('Kinematika mobilného robota')
    img = Image.open("media\PR_Matlab_Kinematika.jpg")
    st.image(img, caption="PR v Pythone")
