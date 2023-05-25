from Crypto.Cipher import Blowfish
import os

def encrypt_image(input_path, output_path, key ):
	bs = Blowfish.block_size
	cipher = Blowfish.new(key, Blowfish.MODE_CBC)

	with open(input_path, 'rb') as infile:
		with open(output_path, 'wb') as outfile:
			outfile.write(os.path.basename(input_path).encode())
			outfile.write(os.linesep.encode())
			outfile.write(os.linesep.encode())

			while True:
				block = infile.read(bs)
				if len(block) == 0:
					break
				elif len(block) % bs != 0:
					block += b' ' * (bs - len(block) % bs)

				outfile.write(cipher.encrypt(block))
