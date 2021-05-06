from string import ascii_uppercase
import os, argparse, subprocess

parser = argparse.ArgumentParser()
parser.add_argument('dir_path', help='directory path')
parser.add_argument('name', help='e.g. ITP1')
parser.add_argument('sets', type=int, help='number of sets')
parser.add_argument('set_size', type=int, help='e.g. 4 if a set has A, B, C, D problems')
args = parser.parse_args()

if not os.path.isdir(args.dir_path):
    subprocess.run(['mkdir', '-p', args.dir_path])

for i in range(1, args.sets + 1):
    for j in range(args.set_size):
        file_name = f'{args.name}_{i}_{ascii_uppercase[j]}.py'
        file_path = os.path.join(args.dir_path, file_name)
        subprocess.run(['touch', file_path], check=True)