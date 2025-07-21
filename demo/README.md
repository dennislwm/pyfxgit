# PyFxGit Demo

This demo shows how to use the `pyfxgit` package to create financial charts with technical indicators.

## Setup

1. Install the pyfxgit package from the parent directory:
```bash
cd ..
pip install -e .
```

2. Or install dependencies directly:
```bash
pip install -r requirements.txt
```

## Running the Demo

```bash
python demo_chart.py
```

This will:
- Generate sample OHLC financial data
- Calculate sample technical indicators (Dbs and DbsMa)
- Create a financial chart with candlesticks and oscillator sub-charts
- Save the chart as `_ChartC_0.1_Demo.png`

## What the Demo Shows

The demo replicates the `plotChart` function from the reference `pymonitor.py` file, demonstrating:

- **Main Chart**: OHLC candlestick chart
- **Sub-charts**: Two oscillator charts showing Dbs and DbsMa indicators  
- **Market Condition Tags**: Colored background spans indicating bullish (green) and bearish (red) conditions
- **Technical Analysis**: Moving averages and momentum indicators

The generated chart will be saved in the current directory as `_ChartC_0.1_Demo.png`.