# read Monthly data from the Excel file and plot time series
import pandas as pd
import datetime as dt
from datetime import date
import numpy as np
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import matplotlib.dates as mdates

def plot_aod_separate(aot_excel_file, cityname, sheetname_raw, sheetname_clim, sheetname_anomaly):
    ## read AOD raw data
    df = pd.read_excel(aot_excel_file, header=None, sheet_name=sheetname_raw)
    x1 = df[0]
    y1 = df[1]

    ## read AOD anomaly data
    df = pd.read_excel(aot_excel_file, header=None, sheet_name=sheetname_anomaly)
    x2 = df[0]
    y2 = df[1]

    ## read AOD climatology data
    df = pd.read_excel(aot_excel_file, header=None, sheet_name=sheetname_clim)
    xc = df[0]
    yc = df[1]

    ## calculate anomay

    fontsize_title = 20
    fontsize_label = 20
    fontsize_tick = 20
    fontsize_legend = 18
    matplotlib.rc('xtick', labelsize=fontsize_tick)
    matplotlib.rc('ytick', labelsize=fontsize_tick)

    ##--------------------------------------------------------------------------------------------
    ## plot raw data
    fig, ax = plt.subplots()
    fig.set_figheight(5)
    fig.set_figwidth(20)

    ax.plot(x1, y1, '#d95f0e', linewidth=2, label=cityname)

    years = mdates.YearLocator(5)  # every year
    years_fmt = mdates.DateFormatter('%Y')
    years_minor = mdates.YearLocator(1)  # every year

    xmin = np.min(x1)
    xmax = np.max(x1)
    ax.set_xlim([xmin, xmax])
    ax.set_ylim([0, 0.8])

    ax.legend(loc='upper left', fontsize=fontsize_legend, frameon=None)
    ax.xaxis.set_major_locator(years)
    ax.xaxis.set_major_formatter(years_fmt)
    ax.xaxis.set_minor_locator(years_minor)
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='black')
    plt.title('Monthly AOD (MERRA 2 data)', fontsize=fontsize_title)

    plt.show()

    ##--------------------------------------------------------------------------------------------
    ## plot climatology data
    fig, ax = plt.subplots()
    fig.set_figheight(4)
    fig.set_figwidth(10)

    ax.plot(xc, yc, 'g-*', linewidth=2, markersize=10, label=cityname)
    ax.set_ylim([0, 0.5])
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='black')
    ax.legend(lolc='upper left', fontsize=fontsize_legend, frameon=None)
    plt.title('Monthly AOD Climatology (MERRA 2 data)', fontsize=fontsize_title)

    plt.show()
    ##--------------------------------------------------------------------------------------------
    ## plot anomaly data
    fig, ax = plt.subplots()
    fig.set_figheight(5)
    fig.set_figwidth(20)

    ax.plot(x2, y2, '#2c7fb8', linewidth=2, label=cityname)

    years = mdates.YearLocator(5)  # every year
    years_fmt = mdates.DateFormatter('%Y')
    years_minor = mdates.YearLocator(1)  # every year

    xmin = np.min(x2)
    xmax = np.max(x2)
    ax.set_xlim([xmin, xmax])
    ax.set_ylim([-0.5, 0.5])

    ax.legend(loc='upper left', fontsize=fontsize_legend, frameon=None)
    ax.xaxis.set_major_locator(years)
    ax.xaxis.set_major_formatter(years_fmt)
    ax.xaxis.set_minor_locator(years_minor)
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='black')
    plt.title('Monthly AOD Anomaly(MERRA 2 data)', fontsize=fontsize_title)

    plt.show()



def plot_aod_stacked(aot_excel_file, cityname, sheetname_raw, sheetname_clim, sheetname_anomaly):
    ## read AOD raw data
    df = pd.read_excel(aot_excel_file, header=None, sheet_name=sheetname_raw)
    x1 = df[0]+df[3]
    y1 = df[1]

    ## read AOD anomaly data
    df = pd.read_excel(aot_excel_file, header=None, sheet_name=sheetname_anomaly)
    x2 = df[0]
    y2 = df[1]

    ## read AOD climatology data
    df = pd.read_excel(aot_excel_file, header=None, sheet_name=sheetname_clim)
    xc = df[0]
    yc = df[1]

    ## calculate anomay

    fontsize_title = 20
    fontsize_label = 20
    fontsize_tick = 20
    fontsize_legend = 18
    matplotlib.rc('xtick', labelsize=fontsize_tick)
    matplotlib.rc('ytick', labelsize=fontsize_tick)

    ##--------------------------------------------------------------------------------------------
    ## plot raw data
    fig, ax = plt.subplots()
    fig.set_figheight(5)
    fig.set_figwidth(20)

    ax.plot(x1, y1, '#d95f0e', linewidth=2, label=cityname)

    years = mdates.YearLocator(5)  # every year
    years_fmt = mdates.DateFormatter('%Y')
    years_minor = mdates.YearLocator(1)  # every year

    xmin = np.min(x1)
    xmax = np.max(x1)
    ax.set_xlim([xmin, xmax])
    ax.set_ylim([0, 0.8])

    ax.legend(loc='upper left', fontsize=fontsize_legend, frameon=None)
    ax.xaxis.set_major_locator(years)
    ax.xaxis.set_major_formatter(years_fmt)
    ax.xaxis.set_minor_locator(years_minor)
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='black')
    plt.title('Monthly AOD (MERRA 2 data)', fontsize=fontsize_title)

    plt.show()

    ##--------------------------------------------------------------------------------------------
    ## plot climatology data
    fig, ax = plt.subplots()
    fig.set_figheight(4)
    fig.set_figwidth(10)

    ax.plot(xc, yc, 'g-*', linewidth=2, markersize=10, label=cityname)
    ax.set_ylim([0, 0.5])
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='black')
    ax.legend(loc='upper left', fontsize=fontsize_legend, frameon=None)
    plt.title('Monthly AOD Climatology (MERRA 2 data)', fontsize=fontsize_title)

    plt.show()
    ##--------------------------------------------------------------------------------------------
    ## plot anomaly data
    fig, ax = plt.subplots()
    fig.set_figheight(5)
    fig.set_figwidth(20)

    ax.plot(x2, y2, '#2c7fb8', linewidth=2, label=cityname)

    years = mdates.YearLocator(5)  # every year
    years_fmt = mdates.DateFormatter('%Y')
    years_minor = mdates.YearLocator(1)  # every year

    xmin = np.min(x2)
    xmax = np.max(x2)
    ax.set_xlim([xmin, xmax])
    ax.set_ylim([-0.5, 0.5])

    ax.legend(loc='upper left', fontsize=fontsize_legend, frameon=None)
    ax.xaxis.set_major_locator(years)
    ax.xaxis.set_major_formatter(years_fmt)
    ax.xaxis.set_minor_locator(years_minor)
    ax.grid(which='major', linestyle='-', linewidth='0.5', color='black')
    plt.title('Monthly AOD Anomaly(MERRA 2 data)', fontsize=fontsize_title)

    plt.show()

def main():
    aot_file = r"D:\GitRepo\AODAnalysis\Output\AODJun14.xlsx"
    print(aot_file.splitlines())
    plot_aod_separate(aot_file, 'Addis Ababa', 'Addis_Ababa_RAW', 'AA_MONTH', 'AA_ANOMALY')
    plot_aod_separate(aot_file, 'Cassablanca', 'Cassablanca_RAW', 'C_MONTH', 'C_ANOMALY')
    plot_aod_separate(aot_file, 'Gaborone', 'Gaborone_RAW', 'G_MONTH', 'G_ANOMALY')
    plot_aod_separate(aot_file, 'Nairobi', 'Nairobi_RAW', 'N_MONTH', 'N_ANOMALY')

if __name__=="__main__":
    main()
