import holoviews as hv
import pandas as pd
hv.extension('bokeh')

def plot_cumulative_returns(cumulative_returns):
    # 如果输入是Series类型，将其转换为DataFrame
    if isinstance(cumulative_returns, pd.Series):
        df = pd.DataFrame({'Cumulative Returns': cumulative_returns})
        df = df.reset_index().rename(columns={'index': 'Date'})
    else:
        df = cumulative_returns
        
    curve = hv.Curve(df, 'Date', 'Cumulative Returns').opts(title="Portfolio Performance")
    return curve
