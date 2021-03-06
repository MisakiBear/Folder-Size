import subprocess
import foldersize as fs


# macos runtime

def cmd_spl(command):
    try:
        command = command.partition(' ')
        return command[0], command[2]
    except:
        return command, ''


helpmsg = '''
Enter help(h) to get help message
Enter scan(s) [path] to scan all folders and files below the path specified
Enter treeview(t) [optional=level / -full(f)] to print the scan\'s result
           the folders below the level will be collapsed
           default value is 5  level should be upper than 1
           use option -full(f) to print the full scan\'s result
Enter dirlistview(dl) [optional=number / -full(f)] to print the folders\' paths descending by size
           number can be specified to decide the number of paths you want to display
           default value is 10
           use option -full(f) to print the full result
Enter filelistview(fl) [optional=number / -full(f)] to print the files\' paths descending by size
           number can be specified to decide the number of paths you want to display
           default value is 10
           use option -full(f) to print the full result
Enter go(g) [index] to move into the specified folder
           index relates to the treeview
Enter back(b) to return to the previous folder
Enter open(o) [index] to open the folder or the file specified
           index relates to the last showed view
Enter exit(e) to exit'''

print()
print('Enter help(h) to get help message')

foldersize = None

while True:
    print()
    print('> Enter command:')
    inputsrc = input()
    cmd, cont = cmd_spl(inputsrc)
    print()

    try:
        if cmd == 'help' or cmd == 'h':
            print(helpmsg)
        elif cmd == 'scan' or cmd == 's':
            print('Scan started...')
            foldersize = fs.FolderSize(cont)
            foldersize.scan_dir()
            print('Scan completed...')
        elif cmd == 'treeview' or cmd == 't':
            if cont == '-full' or cont == '-f':
                foldersize.print_treeview(collapse=False)
            elif cont != '':
                foldersize.print_treeview(level=int(cont))
            else:
                foldersize.print_treeview()
        elif cmd == 'dirlistview' or cmd == 'dl':
            if cont == '-full' or cont == '-f':
                foldersize.create_dir_list(full=True)
            elif cont != '':
                foldersize.create_dir_list(number=int(cont))
            else:
                foldersize.create_dir_list()
            foldersize.print_listview(fs.ViewType.DirList)
        elif cmd == 'filelistview' or cmd == 'fl':
            if cont == '-full' or cont == '-f':
                foldersize.create_file_list(full=True)
            elif cont != '':
                foldersize.create_file_list(number=int(cont))
            else:
                foldersize.create_file_list()
            foldersize.print_listview(fs.ViewType.FileList)
        elif cmd == 'go' or cmd == 'g':
            foldersize.movein(int(cont))
            foldersize.print_treeview(level=2)
        elif cmd == 'back' or cmd == 'b':
            foldersize.back_action()
            foldersize.print_treeview(level=2)
        elif cmd == 'open' or cmd == 'o':
            path = foldersize.get_elem(int(cont))
            subprocess.run(['open', '-R', path])
            print(path + ' opened')
        elif cmd == 'exit' or cmd == 'e':
            break
        else:
            print('Do not have such a command')
    except AttributeError:
        print('Operation invaild: Scan first')
    except Exception as ex:
        print('Operation invaild:', ex)

exit()
