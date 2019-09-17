from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os
import json
import shutil
from datetime import datetime
from time import gmtime, strftime


class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            i = 1
            if filename !='zakaria':
                # try:
                new_name = filename
                extension = 'noname'
                try:
                    extension = str(os.path.splitext(folder_to_track + '/' + filename)[1])
                    path = extensions_folders[extension]
                except Exception:
                    extension = 'noname'

                now = datetime.now()
                year = now.strftime("%Y")
                month = now.strftime("%m")

                folder_destination_path = extensions_folders[extension]

                year_exists = False
                month_exists = False
                for folder_name in os.listdir(extensions_folders[extension]):
                    if folder_name == year:
                        folder_destination_path = extensions_folders[extension] + "/" + year
                        year_exists = True
                        for folder_month in os.listdir(folder_destination_path):
                            if month == folder_month:
                                folder_destination_path = extensions_folders[extension] + "/" + year + "/" + month
                                month_exists = True
                if not year_exists:
                    os.mkdir(extensions_folders[extension] + "/" + year)
                    folder_destination_path = extensions_folders[extension] + "/" + year
                if not month_exists:
                    os.mkdir(folder_destination_path + "/" + month)
                    folder_destination_path = folder_destination_path + "/" + month

                file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
                while file_exists:
                    i += 1
                    new_name = os.path.splitext(folder_to_track + '/' + filename)[0] + str(i) + \
                               os.path.splitext(folder_to_track + '/' + filename)[1]
                    new_name = new_name.split("/")[4]
                    file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
                src = folder_to_track + "/" + filename

                new_name = folder_destination_path + "/" + new_name
                os.rename(src, new_name)
            # except Exception:
            #     print(filename)


extensions_folders = {
    # No name
    'noname': "/Users/zakaria/Desktop/zakaria/Other/Uncategorized",
    # Audio
    '.aif': "/Users/zakaria/Desktop/zakaria/Media/Audio",
    '.cda': "/Users/zakaria/Desktop/zakaria/Media/Audio",
    '.mid': "/Users/zakaria/Desktop/zakaria/Media/Audio",
    '.midi': "/Users/zakaria/Desktop/zakaria/Media/Audio",
    '.mp3': "/Users/zakaria/Desktop/zakaria/Media/Audio",
    '.mpa': "/Users/zakaria/Desktop/zakaria/Media/Audio",
    '.ogg': "/Users/zakaria/Desktop/zakaria/Media/Audio",
    '.wav':"/Users/zakaria/Desktop/zakaria/Media/Audio",
    '.wma': "/Users/zakaria/Desktop/zakaria/Media/Audio",
    '.wpl': "/Users/zakaria/Desktop/zakaria/Media/Audio",
    '.m3u': "/Users/zakaria/Desktop/zakaria/Media/Audio",
    # Text
    '.txt': "/Users/zakaria/Desktop/zakaria/Text/TextFiles",
    '.docx': "/Users/Zakaria/Desktop/zakaria/Text/Microsoft/Word",
    '.odt ': "/Users/zakaria/Desktop/zakaria/Text/TextFiles",
    '.pdf': "/Users/zakaria/Desktop/zakaria/Text/PDF",
    '.rtf': "/zakaria/Zakaria/Desktop/zakaria/Text/TextFiles",
    '.tex': "/Users/zakaria/Desktop/zakaria/Text/TextFiles",
    '.wks ': "/Users/zakaria/Desktop/zakaria/Text/TextFiles",
    '.wps': "/Users/zakaria/Desktop/zakaria/Text/TextFiles",
    '.wpd': "/Users/zakaria/Desktop/zakaria/Text/TextFiles",
    # Video
    '.3g2': "/Users/zakaria/Desktop/zakaria/Media/Video",
    '.3gp': "/Users/zakaria/Desktop/zakaria/Media/Video",
    '.avi': "/Users/zakaria/Desktop/zakaria/Media/Video",
    '.flv':"/Users/zakaria/Desktop/zakaria/Media/Video",
    '.h264':"/Users/zakaria/Desktop/zakaria/Media/Video",
    '.m4v':"/Users/zakaria/Desktop/zakaria/Media/Video",
    '.mkv': "/Users/zakaria/Desktop/zakaria/Media/Video",
    '.mov': "/Users/zakaria/Desktop/zakaria/Media/Video",
    '.mp4': "/Users/zakaria/Desktop/zakaria/Media/Video",
    '.mpg':"/Users/zakaria/Desktop/zakaria/Media/Video",
    '.mpeg': "/Users/zakaria/Desktop/zakaria/Media/Video",
    '.rm': "/Users/zakaria/Desktop/zakaria/Media/Video",
    '.swf': "/Users/zakaria/Desktop/zakaria/Media/Video",
    '.vob': "/Users/zakaria/Desktop/zakaria/Media/Video",
    '.wmv': "/Users/zakaria/Desktop/zakaria/Media/Video",
    # Images
    '.ai': "/Users/zakaria/Desktop/zakaria/Media/Images",
    '.bmp': "/Users/zakaria/Desktop/zakaria/Media/Images",
    '.gif': "/Users/zakaria/Desktop/zakaria/Media/Images",
    '.ico': "/Users/zakaria/Desktop/zakaria/Media/Images",
    '.jpg': "/Users/zakaria/Desktop/zakaria/Media/Images",
    '.jpeg': "/Users/zakaria/Desktop/zakaria/Media/Images",
    '.png': "/Users/zakaria/Desktop/zakaria/Media/Images",
    '.ps': "/Users/zakaria/Desktop/zakaria/Media/Images",
    '.psd': "/Users/zakaria/Desktop/zakaria/Media/Images",
    '.svg': "/Users/zakaria/Desktop/zakaria/Media/Images",
    '.tif': "/Users/zakaria/Desktop/zakaria/Media/Images",
    '.tiff': "/Users/zakaria/Desktop/zakaria/Media/Images",
    '.CR2': "/Users/zakaria/Desktop/zakaria/Media/Images",
    # Internet
    '.asp': "/Users/zakaria/Desktop/zakaria/Other/Internet",
    '.aspx': "/Users/zakaria/Desktop/zakaria/Other/Internet",
    '.cer': "/Users/zakaria/Desktop/zakaria/Other/Internet",
    '.cfm': "/Users/zakaria/Desktop/zakaria/Other/Internet",
    '.cgi': "/Users/zakaria/Desktop/zakaria/Other/Internet",
    '.pl': "/Users/zakaria/Desktop/zakaria/Other/Internet",
    '.css': "/Users/zakaria/Desktop/zakaria/Other/Internet",
    '.htm': "/Users/zakaria/Desktop/zakaria/Other/Internet",
    '.js': "/Users/zakaria/Desktop/zakaria/Other/Internet",
    '.jsp': "/Users/zakaria/Desktop/zakaria/Other/Internet",
    '.part': "/Users/zakaria/Desktop/zakaria/Other/Internet",
    '.php': "/Users/zakaria/Desktop/zakaria/Other/Internet",
    '.rss': "/Users/zakaria/Desktop/zakaria/Other/Internet",
    '.xhtml': "/Users/zakaria/Desktop/zakaria/Other/Internet",
    # Compressed
    '.7z': "/Users/zakaria/Desktop/zakaria/Other/Compressed",
    '.arj': "/Users/zakaria/Desktop/zakaria/Other/Compressed",
    '.deb': "/Users/zakaria/Desktop/zakaria/Other/Compressed",
    '.pkg': "/Users/zakaria/Desktop/zakaria/Other/Compressed",
    '.rar': "/Users/zakaria/Desktop/zakaria/Other/Compressed",
    '.rpm': "/Users/zakaria/Desktop/zakaria/Other/Compressed",
    '.tar.gz': "/Users/zakaria/Desktop/zakaria/Other/Compressed",
    '.z': "/Users/zakaria/Desktop/zakaria/Other/Compressed",
    '.zip': "/Users/zakaria/Desktop/zakaria/Other/Compressed",
    # Disc
    '.bin': "/Users/zakaria/Desktop/zakaria/Other/Disc",
    '.dmg': "/Users/zakaria/Desktop/zakaria/Other/Disc",
    '.iso': "/Users/zakaria/Desktop/zakaria/Other/Disc",
    '.toast': "/Users/zakaria/Desktop/zakaria/Other/Disc",
    '.vcd': "/Users/zakaria/Desktop/zakaria/Other/Disc",
    # Data
    '.csv': "/Users/zakaria/Desktop/zakaria/Programming/Database",
    '.dat': "/Users/zakaria/Desktop/zakaria/Programming/Database",
    '.db': "/Users/zakaria/Desktop/zakaria/Programming/Database",
    '.dbf': "/Users/zakaria/Desktop/zakaria/Programming/Database",
    '.log': "/Users/zakaria/Desktop/zakaria/Programming/Database",
    '.mdb': "/Users/zakaria/Desktop/zakaria/Programming/Database",
    '.sav': "/Users/zakaria/Desktop/zakaria/Programming/Database",
    '.sql': "/Users/zakaria/Desktop/zakaria/Programming/Database",
    '.tar': "/Users/zakaria/Desktop/zakaria/Programming/Database",
    '.xml': "/Users/zakaria/Desktop/zakaria/Programming/Database",
    '.json': "/Users/zakaria/Desktop/zakaria/Programming/Database",
    # Executables
    '.apk': "/Users/zakaria/Desktop/zakaria/Other/Executables",
    '.bat': "/Users/zakaria/Desktop/zakaria/Other/Executables",
    '.com': "/Users/zakaria/Desktop/zakaria/Other/Executables",
    '.exe': "/Users/zakaria/Desktop/zakaria/Other/Executables",
    '.gadget':"/Users/zakaria/Desktop/zakaria/Other/Executables",
    '.jar': "/Users/zakaria/Desktop/zakaria/Other/Executables",
    '.wsf': "/Users/zakaria/Desktop/zakaria/Other/Executables",
    # Fonts
    '.fnt': "/zakaria/kalle/Desktop/zakaria/Other/Fonts",
    '.fon': "/zakaria/kalle/Desktop/zakaria/Other/Fonts",
    '.otf': "/zakaria/kalle/Desktop/zakaria/Other/Fonts",
    '.ttf': "/zakaria/kalle/Desktop/zakaria/Other/Fonts",
    # Presentations
    '.key': "/Users/zakaria/Desktop/zakaria/Text/Presentations",
    '.odp': "/Users/zakaria/Desktop/zakaria/Text/Presentations",
    '.pps': "/Users/zakaria/Desktop/zakaria/Text/Presentations",
    '.ppt': "/Users/zakaria/Desktop/zakaria/Text/Presentations",
    '.pptx': "/Users/zakaria/Desktop/zakaria/Text/Presentations",
    # Programming
    '.c': "/Users/zakaria/Desktop/zakaria/Programming/C&C++",
    '.class': "/Users/zakaria/Desktop/zakaria/Programming/Java",
    '.dart': "/Users/zakaria/Desktop/zakaria/Programming/Dart",
    '.py': "/Users/zakaria/Desktop/zakaria/Programming/Python",
    '.sh': "/Users/zakaria/Desktop/zakaria/Programming/Shell",
    '.swift': "/Users/zakaria/Desktop/zakaria/Programming/Swift",
    '.html': "/Users/zakaria/Desktop/zakaria/Programming/C&C++",
    '.h': "/Users/zakaria/Desktop/zakaria/Programming/C&C++",
    # Spreadsheets
    '.ods': "/Users/zakaria/Desktop/zakaria/Text/Microsoft/Excel",
    '.xlr': "/Users/zakaria/Desktop/zakaria/Text/Microsoft/Excel",
    '.xls': "/Users/zakaria/Desktop/zakaria/Text/Microsoft/Excel",
    '.xlsx':"/Users/zakaria/Desktop/zakaria/Text/Microsoft/Excel",
    # System
    '.bak': "/Users/zakaria/Desktop/zakaria/Text/Other/System",
    '.cab': "/Users/zakaria/Desktop/zakaria/Text/Other/System",
    '.cfg': "/Users/zakaria/Desktop/zakaria/Text/Other/System",
    '.cpl': "/Users/zakaria/Desktop/zakaria/Text/Other/System",
    '.cur': "/Users/zakaria/Desktop/zakaria/Text/Other/System",
    '.dll': "/Users/zakaria/Desktop/zakaria/Text/Other/System",
    '.dmp': "/Users/zakaria/Desktop/zakaria/Text/Other/System",
    '.drv': "/Users/zakaria/Desktop/zakaria/Text/Other/System",
    '.icns': "/Users/zakaria/Desktop/zakaria/Text/Other/System",
    '.ico': "/Users/zakaria/Desktop/zakaria/Text/Other/System",
    '.ini': "/Users/zakaria/Desktop/zakaria/Text/Other/System",
    '.lnk': "/Users/zakaria/Desktop/zakaria/Text/Other/System",
    '.msi':"/Users/zakaria/Desktop/zakaria/Text/Other/System",
    '.sys': "/Users/zakaria/Desktop/zakaria/Text/Other/System",
    '.tmp': "/Users/zakaria/Desktop/zakaria/Text/Other/System",
}

folder_to_track = '/Users/zakaria/Desktop'
folder_destination = '/Users/zakaria/Desktop/zakaria'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
