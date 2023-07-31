import argparse
import glob
import sys
from pathlib import Path

sys.path.append("src")
from easy_vcs import EasyVCS

def read_vcs_instances(watched_file: Path) -> dict:
    instances = {Path(instance_path).stem:EasyVCS(Path(instance_path)) for instance_path in glob.glob(f"{watched_file.parent}/easy_vcs/*/*.easy_vcs")}
    return instances

parser = argparse.ArgumentParser(prog='EasyVCS', description='Beginner friendly VCS')
subparsers = parser.add_subparsers(dest='command', help='Available commands')
# Command: new
parser_new = subparsers.add_parser('watch', help='Create a new EasyVCS instance.')
parser_new.add_argument('path', type=Path, help='Enter the path of the file to be watched.')
parser_new.add_argument('name', type=str, help='Enter the your preferred EasyVCS instance name.')

# Command: save
parser_save = subparsers.add_parser('save', help='Save the current version of a watched file.')
parser_save.add_argument('path', type=Path, help='Enter the path of the file you wish to save.')
parser_save.add_argument('name', type=str, help='Enter the name of the VCS you wish to create a new save for.')

# Command: load
parser_load = subparsers.add_parser('load', help='Load a specific version of a watched file.')
parser_load.add_argument('path', type=Path, help='Enter the path of the file you wish to loaded.')
parser_load.add_argument('name', type=str, help='Enter the name of the VCS you wish to create a new save for.')
parser_load.add_argument('version', type=int, help='Version number')

# Command: delete
parser_delete = subparsers.add_parser('delete', help='Delete an EasyVCS instance.')
parser_delete.add_argument('path', type=Path, help='Enter the path of the file you wish to delete.')
parser_delete.add_argument('name', type=str, help='Enter the name of the EasyVCS instance you wish to delete.')

def main(args = parser.parse_args()): 

    if not any(vars(args).values()):
        parser.print_help()
        sys.exit('\nError: No arguments provided.\n')

    vcs_instances = read_vcs_instances(args.path.resolve())
    # Create a new instance of EasyVCS if the command is "watch"
    match args.command:
        case 'watch':
            if args.name.lower() in vcs_instances:
                print("There is already an instance with that name.")
            else:
                vcs_instances.update({args.name.lower() : EasyVCS.new(args.name.lower(), args.path)})
        case 'save':
            if not vcs_instances or args.name.lower() not in vcs_instances:
                print("VCS instance not found. Please check for any spelling mistakes and try again. If you haven't created an instance yet, please do so using the 'watch' command")
            else:
                vcs_instances[args.name.lower()].save()
        case 'load':
            if not vcs_instances or args.name.lower() not in vcs_instances:
                print("VCS instance not found. Please check for any spelling mistakes and try again. If you haven't created an instance yet, please do so using the 'watch' command")
            else:
                vcs_instances[args.name.lower()].load(args.version)
        case 'delete':
            if not vcs_instances or args.name.lower() not in vcs_instances:
                print("VCS instance not found. Please check for any spelling mistakes and try again. If you haven't created an instance yet, please do so using the 'watch' command")
            else:
                vcs_instances[args.name.lower()].delete()
    
if __name__ == "__main__":
    main()
