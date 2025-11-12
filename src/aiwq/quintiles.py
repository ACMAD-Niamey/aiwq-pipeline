
import xarray as xr, numpy as np

def quintile_edges(ds_train: xr.Dataset, q=(0.2,0.4,0.6,0.8)):
    qedges={}
    for v in ['t2m','tp','msl']:
        qedges[v] = ds_train[v].quantile(q, dim='init_time', skipna=True)
    return xr.Dataset({f'{v}_q': qedges[v] for v in qedges})
