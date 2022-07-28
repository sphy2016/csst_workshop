# Author: Si-Yue Yu
## 材料说明：
以后有时间再看：isophotes_models.ipynb 是为三个models拟合isophote的notebook，bulge.fits，disk.fits分别为bulge和disk models的fits文件
按照这个写作业：isophotes_NGC628.ipynb 是为NGC628拟合isophote的notebook，NGC628_f.fits，myNGC628_i_mask.fits分别为NGC628的SDSS i-band 图像和其mask文件。
*png为 isophotes_NGC628.ipynb 生成的图
extract_fix_isophotes.py 是固定center, ellipticity, position angle来提取信息的脚本。


##########
Assignment文件里面是作业。我提供了UGC9476的SDSS i-band image 及它的mask。mask_for_UGC9476.ipynb是产生mask的notebook（有时间再看）。
作业是，参考 isophotes_NGC628.ipynb，自己写一个notebook来对UGC9476作等照度线分析，提交notebook转成的pdf。
！！注意！！
UGC9476_i.fits 图片的中心并不是星系的中心，你得用ds9打开UGC9476_i.fits，估算一个星系中心来用，不可类似isophotes_NGC628.ipynb那样直接用图片的中心作为星系中戏的guess（应该会出错，即使我没有测试过）。初始的sma（即sma0）也得重新估计，不可用isophotes_NGC628.ipynb 里面的值。

###### 但是 ####
假如你没有ds9，那就设置中心为xcen = 251, ycen = 254, sma0 = 20试试，
