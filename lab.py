import hashlib

def main():
 print('public-lab-ok:' + hashlib.sha256(b'public-lab').hexdigest()[:12])

if __name__ == '__main__':
 main()
