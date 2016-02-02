#!/usr/bin/env python
# -*- coding: UTF-8 -*-

import time
import os, sys
from imgdiff import imgdiff

def main():
    if len(sys.argv) < 4:
        print '''
            imgdiff usage:

                python ./src/main.py /path/to/img1 /path/to/img2 /path/to/diffimg

            output:
                
                如果图片有差异，输出图片差到/path/to/diffimg
        '''
        return

    file1, file2 ,output = sys.argv[1:1+3]    
    isDiff, m_norm,  = imgdiff(file1, file2, output)

    print "Is diff:", isDiff, "Manhattan norm:", m_norm

if __name__ == '__main__':
    start_time = time.time()
    main()
    print("--- 运行时间：%.8f seconds ---" % float(time.time() - start_time))
