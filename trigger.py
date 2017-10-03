# -*- coding: utf-8 -*-
import os
start_path = u'/media'
target_tags = [u'-мкрк', u'-диз', u'мкрк-', u'диз-']
counter_simple = 0
counter_total = 0
counter_folders = 0
index_counter_files = 0
folders_index = []
current_folder_entry = u''
for folder, subfolders, files in os.walk(start_path):
    for file_name in files:
        for tag in target_tags:
            if tag in file_name:
                counter_simple = counter_simple + 1
                break
    if counter_simple > 0:
        known_folder = False
        for folders_index_entry in folders_index:
            if folders_index_entry in folder:
                known_folder = True
                current_folder_entry = folders_index_entry
                break
        if not known_folder:
            current_folder_entry = u''
            folders_index.append(folder)
            index_counter_files = 0
        counter_total = counter_total + counter_simple
        index_counter_files = index_counter_files + counter_simple
        counter_folders = counter_folders + 1
        print counter_simple#, '\t', folder
        counter_simple = 0
        print index_counter_files, '\t', folder
        print index_counter_files, '\t', current_folder_entry
print 'total:', counter_total
print 'folders:', counter_folders
print 'indexed folders:', len(folders_index)
