
import xarray as xr, pandas as pd

def weekly_means_anchored(ds_1p5: xr.Dataset):
    ds = ds_1p5.sortby('time')
    # Build Thursday init dates present in data
    thurs = pd.date_range(ds.time.to_index().min(), ds.time.to_index().max(), freq='W-THU')
    thurs = thurs[thurs.isin(ds.time.to_index())]
    # helper to slice days relative to init
    def window_mean(start, end):
        # start,end are day offsets (inclusive) from init
        return ds.sel(time=slice(init+pd.Timedelta(days=start),
                                 init+pd.Timedelta(days=end))).mean('time', skipna=True)

    records=[]
    for init in thurs:
        w1 = window_mean(19,25)
        w2 = window_mean(26,32)
        w1 = w1.assign_coords({'init_time':init, 'lead':'D19_25'}).expand_dims(['init_time','lead'])
        w2 = w2.assign_coords({'init_time':init, 'lead':'D26_32'}).expand_dims(['init_time','lead'])
        records.append(xr.concat([w1,w2], dim='lead'))
    return xr.concat(records, dim='init_time')
