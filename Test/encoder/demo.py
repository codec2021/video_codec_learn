from bjontegaard_metric import *

print ('Sample 1')
R1 = np.array([15367.9, 7172.49, 3643.3, 1958.76])
PSNRY1 = np.array([41.68,39.66,37.14,34.55])
PSNRU1 = np.array([44.16,42.94,41.83,40.60])
PSNRV1 = np.array([45.93,44.27,42.87,35.84])

R2 = np.array([10695.14,5252.78,2809.8,1556.95])
PSNRY2 = np.array([41.34,39.55,37.29,34.89])
PSNRU2 = np.array([43.84,42.62,41.53,40.38])
PSNRV2 = np.array([45.62,43.94,42.63,41.37])

print ('BD-PSNR: ', BD_PSNR(R1, PSNRY1, R2, PSNRY2))
print ('BD-RATE-Y: ', BD_RATE(R1, PSNRY1, R2, PSNRY2))
print ('BD-RATE-U: ', BD_RATE(R1, PSNRU1, R2, PSNRU2))
print ('BD-RATE-V: ', BD_RATE(R1, PSNRV1, R2, PSNRV2))

