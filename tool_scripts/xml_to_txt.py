# convert xml annotation to txt anotation
import os
import xml.etree.ElementTree as ET


# 获取单个bbox的x,y,w,h
def convert(size, box):
    """
    txt文件格式：label x y w h 
    label = 标签索引
    x = 目标中心横坐标与图像宽度比值
    y = 目标中心纵坐标与图像高度比值
    w = bbox宽度与图像宽度比值
    h = bbox高度与图像高度比值
    """
    dw = 1. / size[0]
    dh = 1. / size[1]
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    w = box[1] - box[0]
    h = box[3] - box[2]
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


# 将xml文件转换成yolov5标签的txt格式
def convert_annotation(xml_file_folder, classes_name, dst_folder):
    """_summary_
    Args:
        xml_file_folder (_str_): xml文件所在文件夹
        classes_name (_list_): 标签名称列表，例如['person', 'car'，'bus']
        dst_folder (_str_): txt文件输出文件夹
    """
    
    # 创建输出文件夹
    if os.path.exists(dst_folder):
        pass
    else:
        os.mkdir(dst_folder)
    
    # 导入所有xml文件的路径,并生成对于的txt文件的路径
    xml_list = []
    txt_list = []
    for file in os.listdir(xml_file_folder):
        if file.endswith('.xml'):
            xml_list.append(os.path.join(xml_file_folder, file))
            txt_list.append(os.path.join(dst_folder,file.replace('.xml','.txt')))
            
    for i in range(len(xml_list)):
        
        file_name_xml = xml_list[i]
        file_name_txt = txt_list[i]
        
        in_file = open(file_name_xml)
        out_file = open(file_name_txt, 'w')
        
        tree = ET.parse(in_file)
        root = tree.getroot()
        size = root.find('size')
        w = int(size.find('width').text) # 获取图片宽度
        h = int(size.find('height').text) # 获取图片高度
        
        try:
            for obj in root.iter('object'):
                difficult = obj.find('difficult').text
                cls = obj.find('name').text
                if cls not in classes_name or int(difficult) == 1:
                    continue
                cls_id = classes_name.index(cls)
                xmlbox = obj.find('bndbox')
                b = (float(xmlbox.find('xmin').text), float(xmlbox.find('xmax').text), float(xmlbox.find('ymin').text),
                    float(xmlbox.find('ymax').text))
                bb = convert((w, h), b) # 转换参数
                out_file.write(str(cls_id) + " " + " ".join([str(a) for a in bb]) + '\n') # 写入转换结果
        
        except:
            print('Cannot convert ' + file_name_xml)
            os.remove(file_name_txt)
            
            
if __name__ == '__main__':
    classes_name = ['face','mask']
    xml_file_folder = 'annotations'
    dst_folder = 'labels'
    convert_annotation(xml_file_folder, classes_name, dst_folder)
    