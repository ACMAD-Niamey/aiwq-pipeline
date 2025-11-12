
import xarray as xr

def add_anomalies(ds_weekly: xr.Dataset):
    # group by week-of-year consistent with lead windows
    woy = ds_weekly['init_time'].dt.isocalendar().week
    clim = ds_weekly.groupby(woy).mean('init_time', skipna=True)
    anom = ds_weekly.groupby(woy) - clim
    return clim, anom
