# -*- coding: utf-8 -*-
import os
import zipfile
from util import datadict

def addzipfile(zipfilename,dirname):  #zipfilename压缩包名称,dirname目录
    try:
        if os.path.isfile(dirname):
            file_names=os.path.basename(dirname)
            with zipfile.ZipFile(zipfilename,'a') as z:
                z.write(dirname,file_names,zipfile.ZIP_DEFLATED)
        else:
            with zipfile.ZipFile(zipfilename,'a') as z:
                for root,dirs,files in os.walk(dirname):
                    for single_file in files:
                        if single_file != zipfilename:
                            filepath = os.path.join(root,single_file)
                            z.write(filepath,single_file,zipfile.ZIP_DEFLATED)
        status_info = 'success'
        status_code = 0
    except Exception as e:
        status_code = 500
        status_info = e.args[0]
    return (status_code,status_info)

