
def save_all(anom, clim, qedges, out_dir='build'):
    import os; os.makedirs(out_dir, exist_ok=True)
    anom.to_zarr(f'{out_dir}/anom.zarr', mode='w')
    clim.to_zarr(f'{out_dir}/clim.zarr', mode='w')
    qedges.to_netcdf(f'{out_dir}/quintiles.nc')
