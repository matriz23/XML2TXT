from xml.etree.ElementTree import parse
import argparse
import os

classes = []  # 记录类别


# float2str(float: f): 保留 f 小数点后 6 位, 并转化成字符串
def float2str(f):
    str_f = str(f) + "000000"
    return str_f[0:8]


# xml2txt(str: xml_path, str: txt_path): 把 xml 格式标注文件转化成归一化的 txt 格式标注文件
def xml2txt(xml_path, txt_path):
    txt_text = ""
    doc = parse(xml_path)
    root = doc.getroot()
    size = root.find("size")
    width = float(size.find("width").text)
    height = float(size.find("height").text)
    for object in root.iter("object"):
        class_name = object.find("name").text
        if class_name not in classes:
            classes.append(class_name)
        class_id = classes.index(class_name)
        print(class_name + " " + str(class_id))
        bndbox = object.find("bndbox")
        xmin = float(bndbox.find("xmin").text)
        ymin = float(bndbox.find("ymin").text)
        xmax = float(bndbox.find("xmax").text)
        ymax = float(bndbox.find("ymax").text)
        center_x = ((xmin + xmax) / 2.0) / width
        center_y = ((ymin + ymax) / 2.0) / height
        box_width = (xmax - xmin) / width
        box_height = (ymax - ymin) / height
        txt_text = txt_text + str(class_id) + " " + float2str(center_x) + " " + float2str(center_y) + " " + float2str(
            box_width) + " " + float2str(box_height) + "\n"
    with open(txt_path, 'w') as file:
        file.write(txt_text)
    return


# create_classes_text(str: dir_path): 创建 classes.txt 文件
def create_classes_text(dir_path):
    classes_text = ""
    for cls in classes:
        classes_text = classes_text + cls + "\n"
    with open(dir_path + "labels/classes.txt", 'w') as file:
        file.write(classes_text)
    return


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument("xml_path", help="the path of the raw xml file")
    args = parser.parse_args()
    xml_dir_path = args.xml_path
    path_list = os.listdir(xml_dir_path)
    if xml_dir_path[-1:] != '/':
        xml_dir_path = xml_dir_path + '/'
    for xml_path in path_list:
        xml_path = xml_dir_path + xml_path
        if xml_path[-3:] != "xml":  # 非 xml 文件略过
            continue
        raw_dir_path, raw_file_name = os.path.split(xml_path)
        if os.path.exists(raw_dir_path + "/labels/") is not True:
            os.mkdir(raw_dir_path + "/labels")
        txt_path = raw_dir_path + "/labels/" + raw_file_name.replace("xml", "txt")
        print(txt_path)
        xml2txt(xml_path, txt_path)  # 转化 xml 为 txt
    create_classes_text(xml_dir_path)  # 创建 classes.txt 文件
