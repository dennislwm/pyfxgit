"""--------+---------+---------+---------+---------+---------+---------+---------+---------|
|                                  D A T A   L I B R A R Y                                 |
|----------+---------+---------+---------+---------+---------+---------+---------+-------"""
import matplotlib.dates as dates
import matplotlib.pyplot as pyplot
import mpl_finance as mpfold
import numpy as np
import pandas as pd

def lstCalcAxes(dblBgn=0.0, dblLen=0.2, dblGap=0.02, intNum=2):
    """
    | Assert FOUR (4) arguments:
    |   dblBeg:         a float for start point (default=0)
    |   dblLen:         a float for length of axes in percent (default=0.2)
    |   dblGap:         a float for gap to begin next axes (default=0.02)
    |   intNum:         an integer for the number of axes (default=2)
    """
    """
    | Assert ONE (1) return:
    |   None:       if 
    |   List:       a list of float for the start of each axes, e.g. [0.0, 0.22, 0.44, ...]
    """
    #
    #---  Assert
    
    lstRet = list()
    #
    #---  Add sub axes to list (max 3)
    for i in range(0, intNum):
        bgn = i * (dblLen+dblGap)
        lstRet.append(bgn)

    #
    #---  Return
    if len(lstRet) < 1:
        return None
    return lstRet

"""--------+---------+---------+---------+---------+---------+---------+---------+---------|
|                                    M A I N   C L A S S                                   |
|----------+---------+---------+---------+---------+---------+---------+---------+-------"""
class ChartCls():

    """--------+---------+---------+---------+---------+---------+---------+---------+---------|
    |                                   C O N S T R U C T O R                                  |
    |----------+---------+---------+---------+---------+---------+---------+---------+-------"""
    def __init__(self, dfAsset, intSub=0):
        #
        # initialize class _CONSTANTS
        self._init_meta()
        #
        # initialize class _variables
        self._dfASSET = dfAsset
        self._figMAIN = pyplot.figure()
        self._figMAIN.set_size_inches((24,24))
        self._lstAXES = list()
        """
        | Automate size of main and sub charts based on number of sub
        """
        #
        #---  Default main has origin (0,0) and width=100%, height=100%
        #       [Hbeg, Vbeg, Hlen, Vlen] of the new axes in fractions of figure width and height.
        """
        | Sub charts shares vertical space with main, but not horizontal space
        """
        dblHbeg = 0
        dblVbeg = 0
        dblHlen = 1
        dblVlen = 0.2
        #
        #---  Add sub axes to list (max 3)
        if intSub > 3:
            print("Warning: Maximum sub charts = 3")
            intSub = 3
        #
        #---  Number of axes is number of subs plus main
        lstAxes = lstCalcAxes(intNum=intSub+1)
        #
        #---  Last axes is main chart
        for i in range(len(lstAxes)-1,-1,-1):
            if i == len(lstAxes)-1:
                self._axsMAIN = self._figMAIN.add_axes((dblHbeg, lstAxes[i], dblHlen, 1 - lstAxes[i]))
            else:
                axs = self._figMAIN.add_axes((dblHbeg, lstAxes[i], dblHlen, dblVlen), sharex=self._axsMAIN)
                self._lstAXES.append(axs)
                
    def _init_meta(self):
        """
        | _strMETACLASS, _strMETAVERSION, _strMETAFILE used to save() and load() members
        """
        self._strMETACLASS = str(self.__class__).split('.')[1][:-2]
        self._strMETAVERSION = "0.1"
        """
        | Filename "_Class_Version_"
        """
        self._strMETAFILE = "_" + self._strMETACLASS + "_" + self._strMETAVERSION + "_"
        
    """--------+---------+---------+---------+---------+---------+---------+---------+---------|
    |                                     I N D I C A T O R                                    |
    |----------+---------+---------+---------+---------+---------+---------+---------+-------"""
    def BuildMain(self, strTitle='Chart'):
        ohlc = self._dfASSET
        intBars = len(ohlc)
        if intBars == 0:
            return
        #
        # extract OHLC into a list of lists
        lohlc = ohlc[['Open', 'High', 'Low', 'Close']].values.tolist()
        #
        # convert dates in datetime format to mathplotlib dates
        mdates = dates.date2num(ohlc.index)
        #
        # prepare ohlc in mathplotlib format
        mohlc = [ [mdates[i]] + lohlc[i] for i in range(len(mdates)) ]
        #
        # set default font sizes
        params = {'axes.labelsize': 20,'axes.titlesize': 24}
        pyplot.rcParams.update(params)
        
        #
        #---  [left, bottom, width, height] of the new axes in fractions of figure width and height.
        ax = self._axsMAIN
        #
        # set default tick sizes
        ax.tick_params(axis='both', which='major', labelsize=20)
        ax.tick_params(axis='both', which='minor', labelsize=18)
    
        # mpfold.plot_day_summary_ohlc(ax, mohlc[-50:], ticksize=5, colorup='#77d879', colordown='#db3f3f') # alternatively, use a barchart
        mpfold.candlestick_ohlc(ax, mohlc[-intBars:], width=0.4, colorup='#77d879', colordown='#db3f3f')

        ax.set_xlabel('Date')
        ax.set_ylabel('Price')
        ax.set_title(strTitle)
        ax.legend(fontsize=20)
        ax.xaxis.set_major_formatter(dates.DateFormatter('%b %d'))
        self._figMAIN.autofmt_xdate()
        
    def MainAddSpan(self, dfTag, lstTag, dblOpacity=0.2, strColor='green'):
        df = dfTag
        axs = self._axsMAIN
        for s in (lstTag):
            axs.axvspan(dates.date2num(dfTag[dfTag==s].index[0]), dates.date2num(dfTag[dfTag==s].index[-1]), alpha=dblOpacity, color=strColor)
    
    def BuildOscillator(self, intAxes, dfOscillator, intUpper=70, intLower=30, strUpper='upper', strLower='lower', strTitle='Oscillator'):
        data = dfOscillator
        intBars=len(data)
        #
        #---  [left, bottom, width, height] of the new axes in fractions of figure width and height.
        ax = self._lstAXES[intAxes]
        ax.set_ylabel("Value")
        ax.plot(data.index, [intUpper] * intBars, label=strUpper)
        ax.plot(data.index, [intLower] * intBars, label=strLower)
        ax.plot(data.index, data[-intBars:], label=strTitle)
        ax.legend()        

    def BuildOscillatorTag(self, dfData, strCol, intPlusMinus=4):
        """
        | Objective: tag start and end of bull / bear with unique tags, e.g. "A", "B", etc
        """
        df=dfData[strCol]
        #
        # create empty series
        dfTag = pd.Series(index=df.index, dtype='int64')

        """
        | Rolling mean, std and zscore
        """
        i=0; intTagBull=0; intTagBear=0;
        for index, values in df.iteritems():
            #
            #---  get current and previous values
            intDbs = df.iloc[i]
            if i==0:
                intPrv = 0
            else:
                intPrv = df.iloc[i-1]
            """
            | Dbs | Prv | Result
            | =4  | <4  |  inc + tag
            | =4  | =4  |  tag
            | <4  | *   |  no tag
            | >-4 | *   |  no tag
            | =-4 | >-4 |  inc + tag
            | =-4 | =-4 |  tag
            |
            """
            if intDbs >= intPlusMinus:
                if intPrv < intPlusMinus:
                    intTagBull = intTagBull + 1
                dfTag.iloc[i] = intTagBull
            elif intDbs <= -intPlusMinus:
                if intPrv > -intPlusMinus:
                    intTagBear = intTagBear - 1
                dfTag.iloc[i] = intTagBear
            i = i + 1
        dfData['Tag'] = dfTag
            
        """
        | Return array of unique tags
        """
        return np.delete(dfTag.unique(), 0)
        

    def save(self, strSuffix=""):
        strFile = self._strMETAFILE + strSuffix + ".png"
        """
        | save chart as PNG
        """
        self._figMAIN.savefig(strFile, bbox_inches="tight")
        print('Saved to ' + strFile)
