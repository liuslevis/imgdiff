README.md

# Dependency
    
    pip install scipy
    pip install numpy
    pip install pillow

# Usage

## 命令行

    python ./src/main.py img1 img2 /path/to/diffimg

    e.g. python ./src/main.py ./img/2.png ./img/3.png ./img/diff2-3.png


    参数： 图片路径 imagefile1 imagefile2，输出差异图片路径 diffimg_path

    条件： 输入图片必须是 PNG 无损格式，尺寸一致。

    输出： 打印：isDiff(Bool) 是否有差异，m_norm(int) 两个输入图片灰度化后的L1距离（曼哈顿距离，差值的绝对值的和）。
      保存差异图片到 diffimg_path，如果isDiff==True，

## 函数调用

    或者使用 ./src/imgdiff.py 文件中的函数 imgdiff() ，详见注释