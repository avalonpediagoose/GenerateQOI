# -*- coding: utf-8 -*-
"""
Created on Mon Apr  8 17:58:48 2024

@author: ginachen

FHD (Full High Definition): 1920x1080
XGA (Extended Graphics Array): 1024x768
The resolution of FHD is 2.25 times that of XGA. 
(i.e., the number of pixels in FHD is 225% of that in XGA)

Generate CSV, BIN, and QOI files.
"""

import datetime
import numpy
import random
import qoi

def FHD_RawData_4bit():
    now = datetime.datetime.now()
    timestamp = now.strftime("%m%d_%H%M%S")
    filename_csv = timestamp + "_FHD_4bit.csv"
    filename_bin = timestamp + "_FHD_4bit.bin"
    with open(filename_csv, 'a') as f_csv:
        with open(filename_bin, 'wb') as f_bin:
            for _ in range(1080):
                row_data = [random.randint(0, 15) for _ in range(1920)]
                hex_data = ''.join('{:01X}'.format(d) for d in row_data)
                formatted_data = ' '.join(hex_data[i:i+2] for i in range(0, len(hex_data), 2))
                f_csv.write(formatted_data + '\n')
                bin_data = bytes.fromhex(hex_data)
                f_bin.write(bin_data)
 
def XGA_RawData_4bit():
    now = datetime.datetime.now()
    timestamp = now.strftime("%m%d_%H%M%S")
    filename_csv = timestamp + "_XGA_4bit.csv"
    filename_bin = timestamp + "_XGA_4bit.bin"
    with open(filename_csv, 'a') as f_csv:
        with open(filename_bin, 'wb') as f_bin:
            for _ in range(1080):
                row_data = [random.randint(0, 15) for _ in range(1920)]
                hex_data = ''.join('{:01X}'.format(d) for d in row_data)
                formatted_data = ' '.join(hex_data[i:i+2] for i in range(0, len(hex_data), 2))
                f_csv.write(formatted_data + '\n')
                bin_data = bytes.fromhex(hex_data)
                f_bin.write(bin_data)
            
def FHD_RawData_Half():
    now = datetime.datetime.now()
    timestamp = now.strftime("%m%d_%H%M%S")
    filename_csv = timestamp + "_FHD_Half.csv"
    filename_bin = timestamp + "_FHD_Half.bin"
    with open(filename_csv, 'a') as f_csv:
        with open(filename_bin, 'wb') as f_bin:
            for _ in range(1080):
                row_data = [random.randint(0, 7) for _ in range(1920)]
                hex_data = ''.join('{:01X}'.format(d) for d in row_data)
                formatted_data = ' '.join(hex_data[i:i+2] for i in range(0, len(hex_data), 2))
                f_csv.write(formatted_data + '\n')
                bin_data = bytes.fromhex(hex_data)
                f_bin.write(bin_data)

def XGA_RawData_Half():
    now = datetime.datetime.now()
    timestamp = now.strftime("%m%d_%H%M%S")
    filename_csv = timestamp + "_XGA_Half.csv"
    filename_bin = timestamp + "_XGA_Half.bin"
    with open(filename_csv, 'a') as f_csv:
        with open(filename_bin, 'wb') as f_bin:
            for _ in range(768):
                row_data = [random.randint(0, 7) for _ in range(1024)]
                hex_data = ''.join('{:01X}'.format(d) for d in row_data)
                formatted_data = ' '.join(hex_data[i:i+2] for i in range(0, len(hex_data), 2))
                f_csv.write(formatted_data + '\n')
                bin_data = bytes.fromhex(hex_data)
                f_bin.write(bin_data)
                
def FHD_RawData_Quarter():
    now = datetime.datetime.now()
    timestamp = now.strftime("%m%d_%H%M%S")
    filename_csv = timestamp + "_FHD_Quarter.csv"
    filename_bin = timestamp + "_FHD_Quarter.bin"
    with open(filename_csv, 'a') as f_csv:
        with open(filename_bin, 'wb') as f_bin:
            for _ in range(1080):
                row_data = [random.randint(0, 3) for _ in range(1920)]
                hex_data = ''.join('{:01X}'.format(d) for d in row_data)
                formatted_data = ' '.join(hex_data[i:i+2] for i in range(0, len(hex_data), 2))
                f_csv.write(formatted_data + '\n')
                bin_data = bytes.fromhex(hex_data)
                f_bin.write(bin_data)

def XGA_RawData_Quarter():
    now = datetime.datetime.now()
    timestamp = now.strftime("%m%d_%H%M%S")
    filename_csv = timestamp + "_XGA_Quarter.csv"
    filename_bin = timestamp + "_XGA_Quarter.bin"
    with open(filename_csv, 'a') as f_csv:
        with open(filename_bin, 'wb') as f_bin:
            for _ in range(768):
                row_data = [random.randint(0, 3) for _ in range(1024)]
                hex_data = ''.join('{:01X}'.format(d) for d in row_data)
                formatted_data = ' '.join(hex_data[i:i+2] for i in range(0, len(hex_data), 2))
                f_csv.write(formatted_data + '\n')
                bin_data = bytes.fromhex(hex_data)
                f_bin.write(bin_data)

def FHD_RawData_4bit_p20():
    """ The proportion of 0 is 20% """
    now = datetime.datetime.now()
    timestamp = now.strftime("%m%d_%H%M%S")
    filename_csv = timestamp + "_FHD_4bit_p20.csv"
    filename_bin = timestamp + "_FHD_4bit_p20.bin"
    filename_qoi = timestamp + "_FHD_4bit_p20.qoi"
    random.seed(123)
    prob_zero = 0.2
    data = numpy.zeros((1080, 1920), dtype=numpy.uint8)
    rgb = numpy.zeros((768, 1024, 3), dtype=numpy.uint8)
    
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            if random.random() < prob_zero:
                data[i, j] = 0
            else:
                data[i, j] = random.randint(1, 15)
                
    with open(filename_csv, 'w') as f:
        for i in range(data.shape[0]):
            row_data = ' '.join('{:01X}'.format(d) for d in data[i])
            f.write(row_data + '\n')
            
    with open(filename_bin, 'wb') as f:
        f.write(data.tobytes())
    
    generate_FHD_QOI_file(filename_qoi, prob_zero, rgb)

def FHD_RawData_4bit_p40():
    """ The proportion of 0 is 40% """
    now = datetime.datetime.now()
    timestamp = now.strftime("%m%d_%H%M%S")
    filename_csv = timestamp + "_FHD_4bit_p40.csv"
    filename_bin = timestamp + "_FHD_4bit_p40.bin"
    filename_qoi = timestamp + "_FHD_4bit_p40.qoi"
    random.seed(123)
    prob_zero = 0.4
    data = numpy.zeros((1080, 1920), dtype=numpy.uint8)
    rgb = numpy.zeros((768, 1024, 3), dtype=numpy.uint8)
    
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            if random.random() < prob_zero:
                data[i, j] = 0
            else:
                data[i, j] = random.randint(1, 15)
                
    with open(filename_csv, 'w') as f:
        for i in range(data.shape[0]):
            row_data = ' '.join('{:01X}'.format(d) for d in data[i])
            f.write(row_data + '\n')
            
    with open(filename_bin, 'wb') as f:
        f.write(data.tobytes())
    
    generate_FHD_QOI_file(filename_qoi, prob_zero, rgb)

def FHD_RawData_4bit_p60():
    """ The proportion of 0 is 60% """
    now = datetime.datetime.now()
    timestamp = now.strftime("%m%d_%H%M%S")
    filename_csv = timestamp + "_FHD_4bit_p60.csv"
    filename_bin = timestamp + "_FHD_4bit_p60.bin"
    filename_qoi = timestamp + "_FHD_4bit_p60.qoi"
    random.seed(123)
    prob_zero = 0.6
    data = numpy.zeros((1080, 1920), dtype=numpy.uint8)
    rgb = numpy.zeros((768, 1024, 3), dtype=numpy.uint8)
    
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            if random.random() < prob_zero:
                data[i, j] = 0
            else:
                data[i, j] = random.randint(1, 15)
                
    with open(filename_csv, 'w') as f:
        for i in range(data.shape[0]):
            row_data = ' '.join('{:01X}'.format(d) for d in data[i])
            f.write(row_data + '\n')
            
    with open(filename_bin, 'wb') as f:
        f.write(data.tobytes())
    
    generate_FHD_QOI_file(filename_qoi, prob_zero, rgb)

def FHD_RawData_4bit_p80():
    """ The proportion of 0 is 80% """
    now = datetime.datetime.now()
    timestamp = now.strftime("%m%d_%H%M%S")
    filename_csv = timestamp + "_FHD_4bit_p80.csv"
    filename_bin = timestamp + "_FHD_4bit_p80.bin"
    filename_qoi = timestamp + "_FHD_4bit_p80.qoi"
    random.seed(123)
    prob_zero = 0.8
    data = numpy.zeros((1080, 1920), dtype=numpy.uint8)
    rgb = numpy.zeros((768, 1024, 3), dtype=numpy.uint8)
    
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            if random.random() < prob_zero:
                data[i, j] = 0
            else:
                data[i, j] = random.randint(1, 15)
                
    with open(filename_csv, 'w') as f:
        for i in range(data.shape[0]):
            row_data = ' '.join('{:01X}'.format(d) for d in data[i])
            f.write(row_data + '\n')
            
    with open(filename_bin, 'wb') as f:
        f.write(data.tobytes())
    
    generate_FHD_QOI_file(filename_qoi, prob_zero, rgb)
        
def XGA_RawData_4bit_p20():
    """ The proportion of 0 is 20% """
    now = datetime.datetime.now()
    timestamp = now.strftime("%m%d_%H%M%S")
    filename_csv = timestamp + "_XGA_4bit_p20.csv"
    filename_bin = timestamp + "_XGA_4bit_p20.bin"
    filename_qoi = timestamp + "_XGA_4bit_p20.qoi"
    random.seed(123)
    prob_zero = 0.2
    data = numpy.zeros((768, 1024), dtype=numpy.uint8)
    rgb = numpy.zeros((768, 1024, 3), dtype=numpy.uint8)
    
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            if random.random() < prob_zero:
                data[i, j] = 0
            else:
                data[i, j] = random.randint(1, 63)
                    
    with open(filename_csv, 'w') as f:
        for i in range(data.shape[0]):
            row_data = ' '.join('{:01X}'.format(d) for d in data[i])
            f.write(row_data + '\n')
            
    with open(filename_bin, 'wb') as f:
        f.write(data.tobytes())
        
    generate_XGA_QOI_file(filename_qoi, prob_zero, rgb)

def XGA_RawData_4bit_p40():
    """ The proportion of 0 is 40% """
    now = datetime.datetime.now()
    timestamp = now.strftime("%m%d_%H%M%S")
    filename_csv = timestamp + "_XGA_4bit_p40.csv"
    filename_bin = timestamp + "_XGA_4bit_p40.bin"
    filename_qoi = timestamp + "_XGA_4bit_p40.qoi"
    random.seed(123)
    prob_zero = 0.4
    data = numpy.zeros((768, 1024), dtype=numpy.uint8)
    rgb = numpy.zeros((768, 1024, 3), dtype=numpy.uint8)
    
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            if random.random() < prob_zero:
                data[i, j] = 0
            else:
                data[i, j] = random.randint(1, 63)
                
    with open(filename_csv, 'w') as f:
        for i in range(data.shape[0]):
            row_data = ' '.join('{:01X}'.format(d) for d in data[i])
            f.write(row_data + '\n')
    with open(filename_bin, 'wb') as f:
        f.write(data.tobytes())
        
    generate_XGA_QOI_file(filename_qoi, prob_zero, rgb)

def XGA_RawData_4bit_p60():
    """ The proportion of 0 is 60% """
    now = datetime.datetime.now()
    timestamp = now.strftime("%m%d_%H%M%S")
    filename_csv = timestamp + "_XGA_4bit_p60.csv"
    filename_bin = timestamp + "_XGA_4bit_p60.bin"
    filename_qoi = timestamp + "_XGA_4bit_p60.qoi"
    random.seed(123)
    prob_zero = 0.6
    data = numpy.zeros((768, 1024), dtype=numpy.uint8)
    rgb = numpy.zeros((768, 1024, 3), dtype=numpy.uint8)
    
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            if random.random() < prob_zero:
                data[i, j] = 0
            else:
                data[i, j] = random.randint(1, 63)
                
    with open(filename_csv, 'w') as f:
        for i in range(data.shape[0]):
            row_data = ' '.join('{:01X}'.format(d) for d in data[i])
            f.write(row_data + '\n')
            
    with open(filename_bin, 'wb') as f:
        f.write(data.tobytes())
        
    generate_XGA_QOI_file(filename_qoi, prob_zero, rgb)

def XGA_RawData_4bit_p80():
    """ The proportion of 0 is 80% """
    now = datetime.datetime.now()
    timestamp = now.strftime("%m%d_%H%M%S")
    filename_csv = timestamp + "_XGA_4bit_p80.csv"
    filename_bin = timestamp + "_XGA_4bit_p80.bin"
    filename_qoi = timestamp + "_XGA_4bit_p80.qoi"
    random.seed(123)
    prob_zero = 0.8
    data = numpy.zeros((768, 1024), dtype=numpy.uint8)
    rgb = numpy.zeros((768, 1024, 3), dtype=numpy.uint8)
    
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            if random.random() < prob_zero:
                data[i, j] = 0
            else:
                data[i, j] = random.randint(1, 63)
                
    with open(filename_csv, 'w') as f:
        for i in range(data.shape[0]):
            row_data = ' '.join('{:01X}'.format(d) for d in data[i])
            f.write(row_data + '\n')
            
    with open(filename_bin, 'wb') as f:
        f.write(data.tobytes())
        
    generate_XGA_QOI_file(filename_qoi, prob_zero, rgb)
    
def XGA_RawData_4bit_p100():
    """ No 0 """
    now = datetime.datetime.now()
    timestamp = now.strftime("%m%d_%H%M%S")
    filename_csv = timestamp + "_XGA_4bit_p100.csv"
    filename_bin = timestamp + "_XGA_4bit_p100.bin"
    filename_qoi = timestamp + "_XGA_4bit_p100.qoi"
    random.seed(123)
    prob_zero = 0
    data = numpy.zeros((768, 1024), dtype=numpy.uint8)
    rgb = numpy.zeros((768, 1024, 3), dtype=numpy.uint8)
    
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
            if random.random() < prob_zero:
                data[i, j] = 0
            else:
                data[i, j] = random.randint(1, 63)
                
    with open(filename_csv, 'w') as f:
        for i in range(data.shape[0]):
            row_data = ' '.join('{:01X}'.format(d) for d in data[i])
            f.write(row_data + '\n')
            
    with open(filename_bin, 'wb') as f:
        f.write(data.tobytes())
        
    generate_XGA_QOI_file(filename_qoi, prob_zero, rgb)

def XGA_RawData_4bit_01(): 
    """ random data 0 or 1"""
    now = datetime.datetime.now()
    timestamp = now.strftime("%m%d_%H%M%S")
    filename_csv = timestamp + "_XGA_4bit_01.csv"
    filename_bin = timestamp + "_XGA_4bit_01.bin"
    filename_qoi = timestamp + "_XGA_4bit_01.qoi"
    random.seed(123)

    data = numpy.zeros((768, 1024), dtype=numpy.uint8)
    rgb = numpy.zeros((768, 1024, 3), dtype=numpy.uint8)
    
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
                data[i, j] = random.randint(0, 0)
                
    with open(filename_csv, 'w') as f:
        for i in range(data.shape[0]):
            row_data = ' '.join('{:01X}'.format(d) for d in data[i])
            f.write(row_data + '\n')
            
    with open(filename_bin, 'wb') as f:
        f.write(data.tobytes())
        
    generate_XGA_QOI_file_ultra(filename_qoi, 0, 0, rgb)
    
def XGA_RawData_4bit_99(): 
    """ random data 63 or 64"""
    now = datetime.datetime.now()
    timestamp = now.strftime("%m%d_%H%M%S")
    filename_csv = timestamp + "_XGA_4bit_99.csv"
    filename_bin = timestamp + "_XGA_4bit_99.bin"
    filename_qoi = timestamp + "_XGA_4bit_99.qoi"
    random.seed(123)

    data = numpy.zeros((768, 1024), dtype=numpy.uint8)
    rgb = numpy.zeros((768, 1024, 3), dtype=numpy.uint8)
    
    for i in range(data.shape[0]):
        for j in range(data.shape[1]):
                data[i, j] = random.randint(63, 63)
                
    with open(filename_csv, 'w') as f:
        for i in range(data.shape[0]):
            row_data = ' '.join('{:01X}'.format(d) for d in data[i])
            f.write(row_data + '\n')
            
    with open(filename_bin, 'wb') as f:
        f.write(data.tobytes())
        
    generate_XGA_QOI_file_ultra(filename_qoi, 63, 63, rgb)
    
def generate_FHD_QOI_file(filename_qoi, prob_zero, rgb):
    #rgb = numpy.random.randint(low=0, high=255, size=(1080, 1920, 3)).astype(numpy.uint8)
    for i in range(rgb.shape[0]):
        for j in range(rgb.shape[1]):
            if random.random() < prob_zero:
                for k in range(rgb.shape[2]):
                    rgb[i, j, k] = 0
    qoi.write(filename_qoi, rgb)

def generate_XGA_QOI_file(filename_qoi, prob_zero, rgb):
    #data = numpy.zeros((768, 1024, 3), dtype=numpy.uint8)
    
    for i in range(rgb.shape[0]):
        for j in range(rgb.shape[1]):
            if random.random() < prob_zero:
                rgb[i, j, 0] = 0
                rgb[i, j, 1] = 0
                rgb[i, j, 2] = 0
            else:
                rgb[i, j, 0] = random.randint(1, 63)
                rgb[i, j, 1] = rgb[i, j, 0]
                rgb[i, j, 2] = rgb[i, j, 0]
    #print(rgb)
    qoi.write(filename_qoi, rgb)

def generate_XGA_QOI_file_ultra(filename_qoi, low, high, rgb):
    #data = numpy.zeros((768, 1024, 3), dtype=numpy.uint8)
    
    for i in range(rgb.shape[0]):
        for j in range(rgb.shape[1]):
                rgb[i, j, 0] = random.randint(low, high)
                rgb[i, j, 1] = rgb[i, j, 0]
                rgb[i, j, 2] = rgb[i, j, 0]
    print(rgb)
    qoi.write(filename_qoi, rgb)
#-------------------------------------------------------------------------------
if __name__ == "__main__":
    #XGA_RawData_4bit_01()
    #XGA_RawData_4bit_99()
    XGA_RawData_4bit_p20()
    XGA_RawData_4bit_p40()
    XGA_RawData_4bit_p60()
    XGA_RawData_4bit_p80()
    XGA_RawData_4bit_p100()
    #FHD_RawData_4bit_p20()
    #FHD_RawData_4bit_p40()
    #FHD_RawData_4bit_p60()
    #FHD_RawData_4bit_p80()
    
    print('Finish.')