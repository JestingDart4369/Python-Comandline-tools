import os
import shutil
import pyfiglet
import inquirer
import cloudDir
#Sorting Filetypes tzo personal preference
FILE_TYPES = {
        "video": (
            'webm', 'mkv', 'flv', 'vob', 'ogv', 'ogg', 'rrc', 'gifv', 'mng', 'mov',
            'avi', 'qt', 'wmv', 'yuv', 'rm', 'asf', 'amv', 'mp4', 'm4p', 'm4v',
            'mpg', 'mp2', 'mpeg', 'mpe', 'mpv', 'svi', '3gp', '3g2', 'mxf', 'roq',
            'nsv', 'f4v', 'f4p', 'f4a', 'f4b', 'mod'
        ),

        "audio": (
            'mp3', 'wav', 'flac', 'aac', 'ogg', 'oga', 'm4a', 'wma', 'alac', 'aiff',
            'aif', 'aifc', 'amr', 'opus', 'ra', 'rm', 'mid', 'midi', 'mp2', 'ac3',
            'dts', 'caf', 'au', 'snd', 'wv', 'tta', 'voc', 'spx'
        ),

        # All Office 365 stuff in one folder
        "office": (
            # Word
            'doc', 'docx', 'dot', 'dotx',
            # Excel
            'xls', 'xlsx', 'xlsm', 'xlt', 'xltx', '.csv',
            # PowerPoint
            'ppt', 'pptx', 'pps', 'ppsx', 'pot', 'potx',
            # Other Office
            'rtf', 'one', 'pub'
        ),

        # Generic docs that aren’t specifically Office
        "document": (
            'txt', 'md', 'odt', 'wps', 'wpd', 'pdf'
        ),

        "ebook": (
            'epub', 'mobi', 'azw', 'azw3', 'fb2', 'ibooks', 'lit'
        ),

        "archive": (
            'zip', 'rar', '7z', 'tar', 'gz', 'bz2', 'xz', 'iso'
        ),

        "image": (
            'jpg', 'jpeg', 'png', 'gif', 'bmp', 'tif', 'tiff',
            'webp', 'heic', 'heif', 'svg', 'raw', 'cr2', 'nef',
            'arw', 'psd', 'ai', 'eps'
        ),

        "database": (
            'db', 'sqlite', 'sqlite3', 'sql', 'accdb', 'mdb',
            'dbf', 'ndf', 'ldf', 'frm', 'myd', 'myi', 'ibd',
            'ora', 'pgd', 'pgpass'
        ),

        "executable": (
            'exe', 'msi', 'bat', 'cmd', 'com',
            'sh', 'run', 'bin', 'app', 'apk', 'jar'
        ),

        "diskimage": (
            'iso', 'img', 'vhd', 'vhdx', 'vmdk', 'dmg', 'nrg', 'toast'
        ),

        "system": (
            'sys', 'dll', 'ini', 'cfg', 'conf', 'reg', 'drv'
        )
    }

#Directorys

userDirectoryMain = os.path.expanduser('~')
userDirectoryDownloads = userDirectoryMain + "/downloads"
userDirectoryDocuments = userDirectoryMain + "/documents"
#imported

userDirectoryCloud1 = cloudDir.userDirectoryCloudB
userDirectoryCloud2 = cloudDir.userDirectoryCloudK

def determine_file_type(filename):
    folder = "error"
    for folder_name, extensions in FILE_TYPES.items():
        if filename.lower().endswith(extensions):
            folder = folder_name
    return folder


#The normal sorter
def normal_sorter():
    # folder naming settings
    folder_start = '00_'
    folder_end = '_AS'

    with os.scandir(userDirectoryDownloads) as downloads:
        for file in downloads:
            if file.is_dir():
                if file.name.endswith(folder_end) and file.name.startswith(folder_start):
                    continue
                else:
                    folders = folder_start + "folders" + folder_end
                    sour = os.path.join(userDirectoryDownloads, file.name)
                    target_folder_folder = os.path.join(userDirectoryDownloads, folders)
                    dest = os.path.join(target_folder_folder, file.name)

                    os.makedirs(target_folder_folder, exist_ok=True)

                    shutil.move(sour, dest)
            if os.path.isfile(os.path.join(userDirectoryDownloads, file.name)):
                folder_name = determine_file_type(file.name)
                source = os.path.join(userDirectoryDownloads, file.name)
                target_folder = os.path.join(userDirectoryDownloads, folder_start + folder_name + folder_end)
                destination = os.path.join(target_folder, file.name)

                os.makedirs(target_folder, exist_ok=True)

                shutil.move(source, destination)


#Special Sorter

#secondary funktion (Sorter)

def determine_file_location(filename):
    modul = filename[3:6]
    try:
        int(modul)
        is_right = True
    except ValueError:
        is_right = False
    return is_right, modul

#main function
def special_sorter():
    with (os.scandir(userDirectoryDownloads) as downloads):
        for file in downloads:
            if os.path.isfile(os.path.join(userDirectoryDownloads, file.name)):
                data_1,data_2 = determine_file_location(file.name)
                if data_1 == False:
                    continue
                data = data_2
                source = os.path.join(userDirectoryDownloads, file.name)
                target_folder = os.path.join(userDirectoryCloud1,"02_Module",data)
                destination = os.path.join(target_folder, file.name)

                os.makedirs(target_folder, exist_ok=True)

                shutil.move(source, destination)
#main loop
while True:
    print(pyfiglet.figlet_format("Sorting"))
    function_choice = inquirer.list_input(message="Sorting-Menu",
                                          choices=[
                                              "01|Normal Sorter",
                                              "02|Special Sorter",
                                              "10|Exit"])
    if function_choice == "01|Normal Sorter":
        print("Soring with Normal Sorter")
        normal_sorter()

    if function_choice == "02|Special Sorter":
        print("Soring with Special Sorter")
        special_sorter()
        normal_sorter()

    if function_choice == "10|Exit":
        break
