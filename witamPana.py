import argparse
parser = argparse.ArgumentParser(description='Powiedz: Witam serdecnie pana --name')
parser.add_argument('--name', type=str ,help='twoję imię proszę pana')
parser.add_argument('--secondname', type=str ,help='twoję nazwisko proszę pana')
args = parser.parse_args()
print('witam serdecznie pana panie ' + args.name)
with open('my_file.txt','w')as my_file:
    my_file.write(args.name + '\n' + args.secondname)