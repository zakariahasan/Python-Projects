from os import walk
from os import path
from shutil import move 
import getpass
import click

mac_username = getpass.getuser()

includes_file_extensn = ([".pdf", ".gif", ".png", ".jpeg",
                          ])

# includes_file_extensn = ([".mp4", ".mpg", ".mpeg", ".swf", ".vob", ".wmv",
#                           ".3g2", ".3gp", ".asf", ".asx", ".avi", ".flv",
#                           ".m2ts", ".mkv", ".mov",
#                           ])

search_dir = path.dirname('/Users/' + mac_username +
                          '/Desktop/')

target_foldr = path.dirname('/Users/' + mac_username +
                            '/Desktop/zak/')

# target_foldr = path.dirname('/Users/' + mac_username +
#                             '/Movies/')

exclude_foldr = set([target_foldr,
                     path.dirname('/Users/' + mac_username +
                                  '/Documents/GitHub/'),
                     path.dirname('/Users/' + mac_username +
                                  '/Documents/Random/'),
                     path.dirname('/Users/' + mac_username +
                                  '/Documents/Stupid_Folder/'),
                     ])

print("Exclude list: " + str(exclude_foldr))
print("Files found will be moved to this folder:" + str(target_foldr))

if click.confirm("Would you like to move files?"
                 "\n No? This will just list the files."
                 "\n Yes? This will Move your files to the target folder.\n",
                 default=False):
    # print('Do something if True?')
    question_moving = True
else:
    # print('Do something if False?')
    question_moving = False


def organize_files():
    """THE MODULE HAS BEEN BUILD FOR KEEPING YOUR FILES ORGANIZED."""
    for dirpath, dirnames, filenames in walk(search_dir, topdown=True):
        for file in filenames:
            if (not (str(dirpath) + '/').startswith(tuple(exclude_foldr))):
                if (file.endswith(tuple(includes_file_extensn))):
                    filetomove = path.normpath(str(dirpath) + '/' +
                                               str(file))
                    movingfileto = path.normpath(str(target_foldr) + '/' +
                                                 str(file))
                    print('Files To Move: ' + str(filetomove))
                    # This is using the prompt you answered at the beginning
                    if question_moving is True:
                        print('Moving File: ' + str(filetomove) +
                              "\n To:" + str(movingfileto))
                        move(filetomove, movingfileto)
                        pass
                    else:
                        pass
                    pass
                else:
                    # print('Theres no need to move these files either: ' +
                    #       str(dirpath) + str(file))
                    pass
            else:
                pass


if __name__ == '__main__':
    organize_files()


