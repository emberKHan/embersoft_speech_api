import requests
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('audio', type=str, help='Input audio path')
parser.add_argument('--mode', type=str, help='send mode', default='force')
parser.add_argument('--url', type=str, default='http://25.37.220.230:5000/')
args = parser.parse_args()

def main(args):
	mode = args.mode
	filepath = args.audio
	URL = args.url + 'force' if mode == 'force' else args.url + 'raw'
	audio = open(filepath, 'rb')
	files = {'file': (filepath, audio, 'audio/wav')}
	response = requests.post(URL, files=files)
	data = response.json()
	print(data)

if __name__ == "__main__":
	main(args)