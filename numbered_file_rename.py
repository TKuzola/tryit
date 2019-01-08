'''
Created on Jan 1, 2019

@author: Anthony Kuzola
Renames any file og the format *.* (N) to *_N.*
'''
import os
import sys
import re


def number_dups(test_source_dir):
    '''
    Called on each directory

    Parameters: test_source_dir is the directory being backed up
                test_target_dir is the backup destination
    '''
    files_renamed = 0

    for dir_name, dummy_sub_dir_list, file_list in os.walk(test_source_dir):
        new_name = "ouch.txt"
        cur_source_dir = dir_name

        for fname in file_list:
            cur_source_file = os.path.join(cur_source_dir, fname)
            # See if there is a number _(#) at the end of the file
            search_obj = re.search(r' \(\d+\)$', fname)
            if search_obj:
                make_unique = search_obj.group()
                print(fname + " has " + make_unique)
                rid_of_space = re.sub(r'\s', "_", make_unique)
                no_parens = re.sub(r'[\)\(]', "", rid_of_space)

                new_name = fname[:search_obj.start() - 4] + no_parens + fname[search_obj.start() - 4:search_obj.start()]
                print("New name is " + new_name)
                files_renamed += 1

                cur_target_file = os.path.join(cur_source_dir, new_name)
                cur_source_info = os.stat(cur_source_file)

                try:
                    os.rename(cur_source_file, cur_target_file)

                except PermissionError as perr:
                    msg = "Permission error: {}".format(perr)
                    print(msg)
                    print("Could not rename " + cur_source_info + " to " + cur_target_file)
                except Exception as e:
                    msg = "Unexpected error: {}".format(sys.exc_info()[0])
                    print(msg)
                    msg2 = "Exception info: {}".format(e)
                    print(msg2)
                    raise

    return(files_renamed)


target_dir = "C:\\Users\\tkuzo\\Desktop\\Transfer"


if __name__ == '__main__':
    renamed = number_dups(target_dir)
    print(renamed)
