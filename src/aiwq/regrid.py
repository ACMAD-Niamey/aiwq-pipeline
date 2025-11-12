
import xarray as xr, xesmf as xe

def to_1p5deg(in_nc: str, out_nc: str):
    ds = xr.open_dataset(in_nc)
    # Source grid
    src = {'lon': ds['longitude'], 'lat': ds['latitude']}
    # Target grid 1.5°
    import numpy as np
    lon_new = np.arange(-180, 180, 1.5)
    lat_new = np.arange(  90, -90, -1.5)
    dst = {'lon': lon_new, 'lat': lat_new}
    regridder = xe.Regridder(ds, xr.Dataset(dst), 'bilinear', reuse_weights=False)
    out = regridder(ds)
    out.to_netcdf(out_nc)
