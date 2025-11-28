import os
import shutil



# map subfolder name -> tuple of extensions
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
        'xls', 'xlsx', 'xlsm', 'xlt', 'xltx','.csv',
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


#gets Directories
userDirectoryMain = os.path.expanduser('~')
userDirectoryDownloads=userDirectoryMain+"/downloads"
userDirectoryDocuments=userDirectoryMain+"/documents"

#folder naming settings
folder_start='00_'
folder_end='_AS'

def determine_file_type(filename):
    for folder_name, extensions in FILE_TYPES.items():
        if filename.lower().endswith(extensions):
            source = os.path.join(userDirectoryDownloads, file.name)
            target_folder = os.path.join(userDirectoryDownloads, folder_start + folder_name + folder_end)
            destination = os.path.join(target_folder, file.name)

            os.makedirs(target_folder, exist_ok=True)

            shutil.move(source, destination)


with os.scandir(userDirectoryDownloads) as downloads:
    for file in downloads:
        if file.is_dir():
            if file.name.endswith(folder_end)and file.name.startswith(folder_start):
                continue
            else:
                folders=folder_start+"Folders"+folder_end
                sour = os.path.join(userDirectoryDownloads, file.name)
                target_folder_folder = os.path.join(userDirectoryDownloads, folders)
                dest = os.path.join(target_folder_folder, file.name)

                os.makedirs(target_folder_folder, exist_ok=True)

                shutil.move(sour, dest)
        if os.path.isfile(os.path.join(userDirectoryDownloads, file.name)):
            determine_file_type(file.name)