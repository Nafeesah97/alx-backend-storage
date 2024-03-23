-- lists all bands with Glam rock as their main style, ranked by their longevity
SELECT band_name, (split - formed) AS lifespan 
FROM metal_bands
WHERE style = 'Glam rock' AND formed <= 2022 AND split <= 2022
ORDER BY lifespan DESC