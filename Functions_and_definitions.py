import os
import tkinter as tk
from tkinter import filedialog
import Settings


class FileSorterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("File Sorter App")

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        dialog_width = int(screen_width / 4)
        dialog_height = int(screen_height / 4)
        dialog_x = int((screen_width - dialog_width) / 2)
        dialog_y = int((screen_height - dialog_height) / 2)
        button_width = int(dialog_width / 40)
        button_height = int(dialog_height / 60)
        button_font = ("Arial", 12)

        self.root.geometry(f"{dialog_width}x{dialog_height}+{dialog_x}+{dialog_y}")
        info_label_text = "To run the program, \nclick the \"Select Folder\" button and select a directory to sort."
        self.info_label = tk.Label(self.root, text=info_label_text, font=button_font)
        self.info_label.pack()
        self.select_button = tk.Button(self.root, text="Select Folder", command=self.move_files,
                                       width=button_width, height=button_height, font=button_font)
        self.select_button.pack(pady=40)
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()

    def create_folder(self, folder_name):
        create_path_folder = os.path.join(Settings.user_profile, folder_name)
        os.makedirs(create_path_folder, exist_ok=True)
        return create_path_folder

    def move_files(self):
        searched_path = filedialog.askdirectory(title="Select Directory to Sort")
        if searched_path:
            file_list = os.listdir(searched_path)
            moved_files_num = 0
            for selected_file in file_list:
                source_path = os.path.join(searched_path, selected_file)
                if os.path.isfile(source_path) and os.path.exists(source_path):
                    extension = os.path.splitext(selected_file)[1]
                    for folder_path, extension_list in Settings.path_dict.items():
                        if extension in extension_list:
                            moved_files_num += 1
                            dest_path = self.create_folder(folder_path)
                            os.replace(source_path, os.path.join(dest_path, selected_file))
            self.result_label.config(text=f' In selected folder has been detected {len(file_list)} object/s'
                                     f'\n{moved_files_num}/{len(file_list)} files has been moved to destination folders')
