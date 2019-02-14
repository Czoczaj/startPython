import argparse
parser = argparse.ArgumentParser(description='Powiedz: Witam serdecnie pana --name')
parser.add_argument('--name', type=str ,help='twoję imię proszę pana')
args = parser.parse_args()
print('witam serdecznie pana panie ' + args.name)