import streamlit as st
import pandas as pd 
import matplotlib.pyplot as plt
import plotly.express as px
import geopandas as gpd

data=pd.read_csv("munis.csv")
gdf=gpd.read_parquet("muns.parquet")
data=pd.read_csv("munis.csv") 

st.dataframe(gdf)


st.title("Mi primer proyecto")
munis=data["entidad"].unique().tolist()


#st.dataframe(data)
mun= st.selectbox("seleccion de municipio",
munis)

filtro =data[data["entidad"]==mun]
#st.dataframe(filtro)

gen=(filtro
.groupby("clas_gen")["total_recaudo"]
.sum())
total_gen= gen.sum()


gen=(gen/total_gen).round(2)

det=(filtro
     .groupby("clasificacion_ofpuj")["total_recaudo"]
     .sum())
total_det=det.sum()
det=(det/total_det).round(2)


#st.dataframe(gen) #general


#st.dataframe(det)# clasificacion 






# Crear el gráfico de pastel con Plotly Express
fig = px.pie(
    gen, 
    values=gen.values,   # los valores numéricos
    names=gen.index,     # las etiquetas
    title="Pie Chart con Plotly",
    color_discrete_sequence=["#472836","#F2D0A4","#B298DC"]
)



# Mostrar en Streamlit
st.plotly_chart(fig)


fig,ax=plt.subplots(1,1, figsize=(10,6))
ax.pie(det.values,labels=det.index)

fin=(filtro
     .groupby(["clas_gen","clasificacion_ofpuj"])["total_recaudo"]
    . sum()
    .reset_index())
#st.dataframe(fin)
fig =px.treemap(fin,path=[px.Constant("total"),
                      "clas_gen",
                      "clasificacion_ofpuj"],
                      values="total_recaudo",
    color_discrete_sequence=["#472836","#F2D0A4","#B298DC"])

st.plotly_chart(fig)
filtro2 = gdf[gdf["entidad"]==mun][["codigo_alt","geometry"]]

st.dataframe(filtro2)



fig, ax = plt.subplots(1,1)

filtro2.plot(ax=ax)

st.pyplot(fig)

