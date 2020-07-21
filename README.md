# pyfx

This is a package of helper classes and libraries.

## Author

[dennislwm](https://github.com/dennislwm/pyfx)

## Installation

     $ pip install pyfx

## Example

```python
     import ChartCls from pyfx
```

## Getting Data

Note: Variable **data** is of type DataFrame that consists of columns ['Open', 'High', 'Low', 'Close', 'Dbs', 'DbsMa', 'Tag'].

### Add indicator charts

```python
     chart = ChartCls(data, intSub=2)
     chart.BuildOscillator(1, data['Dbs'], intUpper=3, intLower=-3, strTitle="Dbs")
     chart.BuildOscillator(0, data['DbsMa'], intUpper=3.75, intLower=-3.75, strTitle="DbsMa")
```

### Build tags  

Note: Function **BuildTag()** is an external function that return a list of unique tags based on column 'DbsMa' and cutoff=3.75.

```python
     lstTag = BuildTag('DbsMa', 3.75)
```

### Add spans to main chart

```python
     chart.MainAddSpan(data['Tag'], lstTag[lstTag>0], 0.2, 'red')
     chart.MainAddSpan(data['Tag'], lstTag[lstTag<0], 0.2, 'green')
```

### Build main chart

```python
     chart.BuildMain(strTitle="SPY")
```

### Save chart

```python
     chart.save("Dbs")
```
