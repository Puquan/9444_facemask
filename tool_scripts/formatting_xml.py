import os
from xml.etree import ElementTree  # 导入ElementTree模块

# 将xml文件内容格式化
def prettyXml(element, indent, newline, level = 0):
    # 判断element是否有子元素
    if element:
 
        # 如果element的text没有内容
        if element.text == None or element.text.isspace():
            element.text = newline + indent * (level + 1)
        else:
            element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * (level + 1)
 
    # 此处两行如果把注释去掉，Element的text也会另起一行 
    #else:
        #element.text = newline + indent * (level + 1) + element.text.strip() + newline + indent * level
 
    temp = list(element) # 将elemnt转成list
    for subelement in temp:
        # 如果不是list的最后一个元素，说明下一个行是同级别元素的起始，缩进应一致
        if temp.index(subelement) < (len(temp) - 1):
            subelement.tail = newline + indent * (level + 1)
        else:  # 如果是list的最后一个元素， 说明下一行是母元素的结束，缩进应该少一个
            subelement.tail = newline + indent * level   
 
        # 对子元素进行递归操作 
        prettyXml(subelement, indent, newline, level = level + 1)
 
# 将格式化内容输出
def write_xml(xml_file_folder,dst_folder):
    """_summary_

    Args:
        xml_file_folder (_str_): xml文件存放的文件夹
        dst_folder (_str_): 格式化后的xml文件输出的文件夹
    """
    # 创建输出文件夹
    if os.path.exists(dst_folder):
        pass
    else:
        os.mkdir(dst_folder)
    
    # 导入所有xml文件的路径,并生成对于的txt文件的路径
    xml_list = []
    dst_list = []
    for file in os.listdir(xml_file_folder):
        if file.endswith('.xml'):
            xml_list.append(os.path.join(xml_file_folder, file))
            dst_list.append(os.path.join(dst_folder,file))
            
    for i in range(len(xml_list)):
        xml_file_path = xml_list[i]
        new_xml_path = dst_list[i]
    
        tree = ElementTree.parse(xml_file_path)
        root = tree.getroot()
        prettyXml(root, '\t', '\n')
        tree.write(new_xml_path, encoding = 'utf-8', xml_declaration = True)
        print('{} has been formatted'.format(xml_file_path))     
 


if __name__ == '__main__':
    xml_file_folder = './test_xml'
    dst_folder = './annotations'
    write_xml(xml_file_folder,dst_folder)
    
       
        