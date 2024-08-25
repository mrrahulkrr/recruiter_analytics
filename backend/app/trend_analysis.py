import pandas as pd
import matplotlib.pyplot as plt
import io
import base64

class TrendAnalysis:
    def __init__(self, data):
        self.data = data

    def analyze_trend(self, metric, time_period):
        trend_data = self.data.groupby(pd.Grouper(key='date', freq=time_period))[metric].mean()
        return trend_data.to_dict()

    def plot_trend(self, metric, time_period):
        trend_data = pd.Series(self.analyze_trend(metric, time_period))
        plt.figure(figsize=(12, 6))
        plt.plot(trend_data.index, trend_data.values)
        plt.title(f'{metric} Trend over {time_period}')
        plt.xlabel('Date')
        plt.ylabel(metric)
        
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        plt.close()
        
        return base64.b64encode(buf.getvalue()).decode('utf-8')

    def compare_trends(self, metric1, metric2, time_period):
        trend1 = pd.Series(self.analyze_trend(metric1, time_period))
        trend2 = pd.Series(self.analyze_trend(metric2, time_period))
        
        plt.figure(figsize=(12, 6))
        plt.plot(trend1.index, trend1.values, label=metric1)
        plt.plot(trend2.index, trend2.values, label=metric2)
        plt.title(f'Comparison of {metric1} and {metric2} over {time_period}')
        plt.xlabel('Date')
        plt.ylabel('Value')
        plt.legend()
        
        buf = io.BytesIO()
        plt.savefig(buf, format='png')
        buf.seek(0)
        plt.close()
        
        return base64.b64encode(buf.getvalue()).decode('utf-8')