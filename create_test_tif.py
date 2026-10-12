import rasterio
import numpy as np
import os

os.makedirs("data", exist_ok=True)

height, width = 100, 100
red = np.random.randint(50, 120, (height, width)).astype(np.float32)
nir = np.random.randint(150, 240, (height, width)).astype(np.float32)

transform = rasterio.transform.from_bounds(48.5, 38.5, 49.0, 39.0, width, height)

tif_path = "data/lankaran_lowland.tif"

with rasterio.open(
    tif_path,
    'w',
    driver='GTiff',
    height=height,
    width=width,
    count=2,
    dtype=rasterio.float32,
    crs='EPSG:4326',
    transform=transform,
) as dst:
    dst.write(red, 1)
    dst.write(nir, 2)

print(f"Uğurlu! Test faylı yaradıldı: {tif_path}")