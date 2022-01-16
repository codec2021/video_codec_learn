@echo off
for %%q in (22,27,32,37) do (
	
	x264cli.exe --profile baseline --preset medium -o .\h264_stream\Kimono1_1920x1080_24_%%q.h264 F:\test_seq\HEVC\Kimono1_1920x1080_24.yuv --qp %%q --keyint 1000 --fps 25 --frames 200 --psnr --threads 4 2>>x264_test_baseline.txt
	
	
	x264cli.exe --profile main --preset medium -o .\h264_stream\Kimono1_1920x1080_24_%%q.h264 F:\test_seq\HEVC\Kimono1_1920x1080_24.yuv --qp %%q --keyint 1000 --fps 25 --frames 200 --psnr --threads 4 2>>x264_test_main.txt
)

pause