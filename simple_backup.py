'''
Created on Apr 28, 2017

@author: Tony Kuzola
'''
import os
import shutil
import xml.dom.minidom
import time
import logging
import sys


def backup_directory(test_source_dir, test_target_dir):
    '''
    Called on each directory

    Parameters: test_source_dir is the directory being backed up
                test_target_dir is the backup destination
    '''
    files_copied = 0
    bytes_copied = 0
    files_replaced = 0
    logger = logging.getLogger("Backups")

    for dir_name, dummy_sub_dir_list, file_list in os.walk(test_source_dir):

        cur_source_dir = dir_name
        cur_target_dir = cur_source_dir.replace(test_source_dir, test_target_dir)
        logger.info("Checking %s...", cur_source_dir)
        if not os.path.isdir(cur_target_dir):
            os.makedirs(cur_target_dir)
        for fname in file_list:
            cur_source_file = os.path.join(cur_source_dir, fname)
            cur_target_file = os.path.join(cur_target_dir, fname)
            cur_source_info = os.stat(cur_source_file)

            if os.path.exists(cur_target_file):
                if os.path.getmtime(cur_target_file) < os.path.getmtime(cur_source_file):
                    try:
                        shutil.copy2(cur_source_file, cur_target_file)

                        logger.info("Found newer %s", cur_target_file)
                        files_replaced = files_replaced + 1
                        bytes_copied = bytes_copied + cur_source_info.st_size
                    except PermissionError as perr:
                        msg = "Permission error: {}".format(perr)
                        logger.error(msg)
                        logger.error("Could not replace %s with %s", cur_target_file, cur_source_file)
                    except Exception as e:
                        msg = "Unexpected error: {}".format(sys.exc_info()[0])
                        logger.error(msg)
                        msg2 = "Exception info: {}".format(e)
                        logger.error(msg2)
                        raise

            else:
                try:
                    shutil.copy2(cur_source_file, cur_target_file)

                    logger.info('%s created', cur_target_file)
                    files_copied = files_copied + 1
                    bytes_copied = bytes_copied + cur_source_info.st_size
                except PermissionError as perr:
                    msg = "Permission error: {}".format(perr)
                    logger.error(msg)
                    logger.error("Could not copy %s to %s", cur_source_file, cur_target_file)
                except Exception as e:
                    msg = "Unexpected error: {}".format(sys.exc_info()[0])
                    logger.error(msg)
                    msg2 = "Exception info: {}".format(e)
                    logger.error(msg2)
                    raise

    logger.info('%d files copied', files_copied)
    logger.info('%d files replaced', files_replaced)
    logger.info('%d total bytes copied', bytes_copied)
    return(files_copied, files_replaced, bytes_copied)


def run_full_backup():
    '''
    Main backup routine

    Reads configuration file and calls backup directory on all listed directories
    '''
    job_files_copied = 0
    job_bytes_copied = 0
    job_files_replaced = 0
    file_counts = (0, 0, 0)
    print("Backups started at {}".format(time.strftime("%m/%d/%Y %H:%M:%S")))
    log_file_name = 'Backup{}.log'.format(time.strftime("%Y%m%d%H%M%S"))
    cur_directory = os.path.dirname(os.path.realpath(__file__))
    log_file_path = '{}\\{}'.format(cur_directory, log_file_name)
    print('To check progress look at log the file:{}'.format(log_file_path))

    logger = logging.getLogger("Backups")
    logger.setLevel(logging.INFO)

    # create the logging file handler
    file_handle = logging.FileHandler(log_file_path)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    file_handle.setFormatter(formatter)

    # add handler to logger object
    logger.addHandler(file_handle)
    logger.info("Backups started at %s", time.strftime("%m/%d/%Y %H:%M:%S"))

    dom1 = xml.dom.minidom.parse('{}\\backup_spec.xml'.format(cur_directory))

    directories = dom1.getElementsByTagName('directory')
    for directory in directories:
        source_dir_path = ''
        target_dir_path = ''

        source_dirs = directory.getElementsByTagName("source")
        for source_dir in source_dirs:
            source_dir_path = source_dir.firstChild.data

        target_dirs = directory.getElementsByTagName("target")
        for target_dir in target_dirs:
            target_dir_path = target_dir.firstChild.data

        logger.info('Backing up %s to %s', source_dir_path, target_dir_path)
        file_counts = backup_directory(source_dir_path, target_dir_path)
        job_files_copied = job_files_copied + file_counts[0]
        job_files_replaced = job_files_replaced + file_counts[1]
        job_bytes_copied = job_bytes_copied + file_counts[2]

    logger.info("Backups finished at %s", time.strftime("%m/%d/%Y %H:%M:%S"))
    print("Backups finished at {}".format(time.strftime("%m/%d/%Y %H:%M:%S")))

    logger.info('%d total files copied', job_files_copied)
    logger.info('%d total files replaced', job_files_replaced)
    logger.info('%d total total bytes copied', job_bytes_copied)

    print('{} total files copied'.format(job_files_copied))
    print('{} total files replaced'.format(job_files_replaced))
    print('{} total total bytes copied'.format(job_bytes_copied))


if __name__ == "__main__":
    run_full_backup()
