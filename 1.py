import os
import os.path


def trans(files, path):
    for file in files:
        filepath = os.path.join(path, file)

        if os.path.isdir(filepath):
            # 如果是文件夹则递归处理
            next_files = os.listdir(filepath)
            trans(next_files, filepath)
            continue
        root, ext = os.path.splitext(filepath)  # root为文件名，ext为后缀（包括.）

        if(ext != ".md"):
            # 只处理markdown文件
            continue

        print("正在处理:", filepath)
        source_file_path = filepath
        dest_file_path = filepath + ".bak"

        # 读入文件修改后写入新文件，然后把原文件删除，把新文件重命名为原文件
        with open(source_file_path, encoding='utf-8') as fr, open(dest_file_path, 'w', encoding='utf-8') as fw:
            for line in fr:
                new_line = line.replace(source_link, dest_link)
                fw.write(new_line)
        os.remove(source_file_path)
        os.rename(dest_file_path, source_file_path)


if __name__ == "__main__":
    # 待处理目录，注意这里需要是双反斜杠
    basepath = "D:\\Blog\source\\_posts"
    # 原地址
    source_link = "https://raw.githubusercontent.com/Chillstepp/MyPicBed/master"
    # 新地址 
    dest_link = "https://raw.githubusercontent.com/Chillstepp/MyPicBed/master/master/"

    files = os.listdir(basepath)

    # 处理文件
    trans(files, basepath)
