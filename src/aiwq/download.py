# src/aiwq/download.py
from pathlib import Path
import cdsapi

def fetch_era5(out_path: str, years=('2018','2024')):
    Path(out_path).parent.mkdir(parents=True, exist_ok=True)
    c = cdsapi.Client()
    c.retrieve(
        'reanalysis-era5-single-levels',
        {
          'variable': ['2m_temperature','total_precipitation','mean_sea_level_pressure'],
          'product_type':'reanalysis',
          'year': list(map(str, range(int(years[0]), int(years[1])+1))),
          'month': [f'{m:02d}' for m in range(1,13)],
          'day': [f'{d:02d}' for d in range(1,32)],
          'time': ['00:00'],
          'format':'netcdf'
        },
        out_path
    )
