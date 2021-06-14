#! /usr/bin/env python
import plot.lib.netcdf as nclib
import plot.lib.util as utillib
from netCDF4 import Dataset
from plot.map import template


def standard_plot(inputFile, var, depthLevel, title, tDescr, lonLat, outFileName, mapLevels, clbLim=None):
    """
    This function call the function to plot the variable passed as argument

    Args:
        inputFile: netCDF file path
        var: variable to plot
        depthLevel: depth level of var
        title: if not None this will be the figure title
        tDescr: figure title extension if title is None
        lonLat: the coordinates of the map to plot
        outFileName: if not None this will be the output file name
        mapLevels: number of color to use in the colorbar
        clbLim (str): the range limit of colorbar

    """
    ncDataset = Dataset(inputFile, mode='r')

    ncLon, ncLat, ncLonIndex, ncLatIndex, ncDepth, ncTime = nclib.read_dim_var(ncDataset, lonLat, depthLevel)
    ncVar, ncVarUnit = nclib.read_var(ncDataset, var, depthLevel, ncLonIndex, ncLatIndex)

    ncDataset.close()
    varField = nclib.get_map_field(ncVar, depthLevel)

    if title is None:
        title = utillib.get_map_title(var, depthLevel, tDescr)
    if outFileName is None:
        outFileName = utillib.get_out_name(var, tDescr, level=depthLevel)

    mapPlot = template.MapPlot(mapLevels=mapLevels)
    mapPlot.plot(ncLon, ncLat, varField, title, outFileName, lonLat, clbLim=clbLim)
