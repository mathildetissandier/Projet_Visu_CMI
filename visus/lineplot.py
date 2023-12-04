import plotly.express as px

def build_lineplot(data):
   
    df_grouped = data.groupby(['year', 'origine']).size().reset_index(name='count')

    df_grouped['cumulative_count'] = df_grouped.groupby('origine')['count'].cumsum()

    fig = px.line(df_grouped, x='year', y='cumulative_count', color='origine',
                  labels={'cumulative_count': 'Nombre cumulatif d\'événements', 'year': 'Année'},
                  title='Évolution du nombre cumulatif d\'événements par origine au fil des années')
    
    fig.update_layout(
        title_font=dict(size=24),
        xaxis=dict(
            title=dict(text='Années', font=dict(size=18)),
            tickfont=dict(size=18),
        ),
        yaxis=dict(title=dict(text='Nombre cumulatif d\'événements', font=dict(size=22)),
                   tickfont=dict(size=18),),
        legend=dict(
            x=1.02,
            y=0.5,
            traceorder='normal',
            font=dict(size=16),
            bgcolor='rgba(255, 255, 255, 0.5)',
        )
    )
    
    return fig
