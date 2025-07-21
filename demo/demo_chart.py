"""
Demo application for pyfxgit ChartCls functionality
This demonstrates how to use the plotChart function with sample financial data.
"""
import pandas as pd
import numpy as np
from datetime import date, datetime, timedelta
import sys
import os

# Add parent directory to path to import pyfxgit
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pyfxgit.ChartCls import ChartCls

def generate_sample_data(days=252):
    """Generate sample OHLC data for demonstration purposes"""
    dates = pd.date_range(start=date.today() - timedelta(days=days), end=date.today(), freq='D')
    
    # Generate realistic OHLC data using random walk
    np.random.seed(42)  # For reproducible results
    price = 100.0
    data = []
    
    for _ in range(len(dates)):
        # Random daily return between -3% and 3%
        daily_return = np.random.normal(0, 0.02)
        
        # Calculate OHLC with some realistic relationships
        open_price = price
        close_price = price * (1 + daily_return)
        high_price = max(open_price, close_price) * (1 + abs(np.random.normal(0, 0.01)))
        low_price = min(open_price, close_price) * (1 - abs(np.random.normal(0, 0.01)))
        
        # Adjusted close (same as close for simplicity)
        adj_close = close_price
        
        # Random volume
        volume = np.random.randint(1000000, 10000000)
        
        data.append([open_price, high_price, low_price, close_price, adj_close, volume])
        price = close_price
    
    df = pd.DataFrame(data, index=dates, 
                     columns=['Open', 'High', 'Low', 'Close', 'Adjusted', 'Volume'])
    
    return df

def calculate_sample_indicators(df):
    """Calculate sample Dbs and DbsMa indicators for demo purposes"""
    # Generate a simple oscillator based on price momentum
    df['Dbs'] = ((df['Close'] / df['Close'].shift(20) - 1) * 100).rolling(5).mean()
    
    # Calculate moving average of Dbs (similar to DbsMa in reference code)
    df['DbsMa'] = df['Dbs'].rolling(7).mean()
    
    # Fill NaN values
    df = df.dropna()
    
    return df

def demo_plot_chart():
    """Demo function that replicates the plotChart functionality from pymonitor.py"""
    print("Generating sample financial data...")
    
    # Generate sample data
    df_sample = generate_sample_data(days=365)
    df_with_indicators = calculate_sample_indicators(df_sample)
    
    print(f"Created sample dataset with {len(df_with_indicators)} rows")
    print("Sample data preview:")
    print(df_with_indicators.tail())
    
    # Create chart using the same approach as in pymonitor.py
    print("\nCreating financial chart...")
    
    # Replicate the plotChart function from pymonitor.py
    chart = ChartCls(df_with_indicators, intSub=2)
    
    # Build oscillators (similar to reference code)
    chart.BuildOscillator(1, df_with_indicators['Dbs'], intUpper=3, intLower=-3, strTitle="Dbs")
    chart.BuildOscillator(0, df_with_indicators['DbsMa'], intUpper=3.75, intLower=-3.75, strTitle="DbsMa")
    
    # Build oscillator tags
    lstTag = chart.BuildOscillatorTag(df_with_indicators, 'DbsMa', 3.75)
    
    # Add colored spans for market conditions
    chart.MainAddSpan(df_with_indicators['Tag'], lstTag[lstTag>0], 0.2, 'red')
    chart.MainAddSpan(df_with_indicators['Tag'], lstTag[lstTag<0], 0.2, 'green')
    
    # Build main chart
    chart.BuildMain(strTitle="Sample Financial Data")
    
    # Save chart
    chart.save("Demo")
    print("Success: Saved demo chart as '_ChartC_0.1_Demo.png'")

if __name__ == "__main__":
    print("=== PyFxGit Demo Application ===")
    print("This demo shows how to use the ChartCls.plotChart functionality")
    print("with sample financial data.\n")
    
    try:
        demo_plot_chart()
        print("\nDemo completed successfully!")
        print("Check the generated chart file: '_ChartC_0.1_Demo.png'")
    except Exception as e:
        print(f"Error running demo: {e}")
        print("Make sure pyfxgit is installed: pip install -e .")