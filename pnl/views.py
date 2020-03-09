# from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
import plotly
from plotly.offline import plot
import plotly.graph_objects as go

import pandas as pd

def data(request):
    
    path = r"\\10.155.31.149\멀티에셋\Kelian\P&L"
    df = pd.read_csv(path + "\CumPnl.csv")
    df.index = df.iloc[:,0]
    df = df.iloc[:,1:]
    df.index = pd.to_datetime(df.index.astype(str))
    
    fig = go.Figure()
    
    

    fig.add_trace(go.Scatter(x=[x for x in df.index], 
                        y=df.iloc[:,0],
                        mode='lines',
                        name=df.columns[0]))
    fig.add_trace(go.Scatter(x=[x for x in df.index], 
                        y=df.iloc[:,1],
                        mode='lines',
                        name=df.columns[1]))
    fig.add_trace(go.Scatter(x=[x for x in df.index], 
                        y=df.iloc[:,2],
                        mode='lines',
                        name=df.columns[2]))
    fig.add_trace(go.Scatter(x=[x for x in df.index], 
                        y=df.iloc[:,3],
                        mode='lines',
                        name=df.columns[3]))
    fig.add_trace(go.Scatter(x=[x for x in df.index], 
                        y=df.iloc[:,4],
                        mode='lines',
                        name=df.columns[4]))
    fig.add_trace(go.Scatter(x=[x for x in df.index], 
                        y=df.iloc[:,5],
                        mode='lines',
                        name=df.columns[5]))




    plot_div = plot(fig,
                output_type='div')
    return render(request, "pnl/data.html", context={'plot_div': plot_div})



