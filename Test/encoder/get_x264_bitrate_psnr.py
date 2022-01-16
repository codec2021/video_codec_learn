#this is a example for get x264 test data form a .txt file
#save psnr(y,u,v) ,bitate,fps into .xls file.
# codec2021

import xlwt
import re

def get_test_sequence_data(filename):
    
    ENCODER_DATA=[[] for i in range(5)]

    with open(filename,"r") as f:
        for line_data in f.readlines():
            line = line_data.strip()

            if line.startswith("x264 [info]: PSNR Mean Y"):
                bitrate = line.split(":")[7].split(" ")[0]
                ENCODER_DATA[0].append(float(bitrate)) #获取码率
              
            if line.startswith("x264 [info]: PSNR Mean Y"):
                psnr_y = line.split(":")[2].split(" ")[0]
                ENCODER_DATA[1].append(float(psnr_y)) #获取PSNR Y
                
            if line.startswith("x264 [info]: PSNR Mean Y"):
                psnr_u = line.split(":")[3].split(" ")[0]
                ENCODER_DATA[2].append(float(psnr_u))#获取PSNR U
                
            if line.startswith("x264 [info]: PSNR Mean Y"):
                psnr_v = line.split(":")[4].split(" ")[0]
                ENCODER_DATA[3].append(float(psnr_v))#获取PSNR V
              
            if line.startswith("encoded"):
                fps_val = line.split("frames,")[1].split("fps")[0]
                ENCODER_DATA[4].append(float(fps_val))#获取fps
                
    return ENCODER_DATA

def write_data_to_excel(filename,bdrate_list):
    
    workbook = xlwt.Workbook(encoding="utf-8")
    worksheet= workbook.add_sheet("BD-rate")

    #设置表头
    worksheet.write(0,0,"bitrate/kbps")
    worksheet.write(0,1,"Y psnr")
    worksheet.write(0,2,"U psnr")
    worksheet.write(0,3,"V psnr")
    worksheet.write(0,4,"fps")

    #写对应的数据
    for idx in range(0,len(bdrate_list[0])):
        for data_idx in range(5):
            worksheet.write(idx + 1,data_idx,label = bdrate_list[data_idx][idx])

    workbook.save(filename.split(".")[0]+"bdrate_data.xls")


if __name__ == "__main__":
    test_file = r"x264_test_baseline.txt"
    psnr_list = get_test_sequence_data(test_file)
    write_data_to_excel(test_file,psnr_list)

    test_file = r"x264_test_main.txt"
    psnr_list = get_test_sequence_data(test_file)
    write_data_to_excel(test_file,psnr_list)
