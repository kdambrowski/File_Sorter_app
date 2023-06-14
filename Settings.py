import os

user_profile = os.environ['USERPROFILE']
documents = os.path.join(user_profile, 'Documents')
images = os.path.join(user_profile, 'Pictures')
musics = os.path.join(user_profile, 'Music')
video = os.path.join(user_profile, 'Videos')

list_doc_extentions = ['.doc', '.docx', '.odt', '.pdf', '.rtf', '.txt',
                       '.csv', '.xls', '.xlsx', '.ods', '.ppt', '.pptx',
                       '.odp', '.html', '.xml', '.tex', '.pages', '.numbers',
                       '.key', '.md', '.dot', '.dotx', '.ott', '.xps',
                       '.djvu', '.epub', '.mobi', '.fb2', '.azw', '.chm', 'pdf']

list_image_extentions = ['.apng', '.avif', '.gif', '.jpg', '.jpeg', '.jfif',
                         '.pjpeg', '.pjp', '.png', '.svg', '.webp', '.bmp',
                         '.ico', '.cur', '.tif', '.tiff', ]
list_music_extentions = ['.3gp', '.aa', '.aac', '.aax', '.act', '.aiff',
                         '.alac', '.amr', '.ape', '.au', '.awb', '.dss',
                         '.dvf', '.flac', '.gsm', '.iklax', '.ivs', '.m4a',
                         '.m4b', '.m4p', '.mmf', '.movpkg', '.mp3', '.mpc',
                         '.msv', '.nmf', '.ogg', '.oga', '.mogg', '.opus',
                         '.ra', '.rm', '.raw', '.rf64', '.sln', '.tta',
                         '.voc', '.vox', '.wav', '.wma', '.wv', '.webm',
                         '.8svx', '.cda']
list_video_extentions = ['.3g2', '.3gp', '.asf', '.avi', '.flv', '.m4v',
                         '.mkv', '.mov', '.mp4', '.mpg', '.mpeg', '.rm',
                         '.swf', '.vob', '.wmv']

path_dict = {documents: list_doc_extentions,
             images: list_image_extentions,
             musics: list_music_extentions,
             video: list_video_extentions}