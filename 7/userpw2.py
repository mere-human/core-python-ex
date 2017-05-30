#!/usr/bin/env python3
import time
import hashlib
import random

db = {}

def get_salt():
  num = random.getrandbits(256)
  return get_hash_str(str(num))

def get_hash_str(s):
  return hashlib.sha256(s.encode('utf-8')).hexdigest()
  
def get_pwd_hash(salt, pwd):
  return get_hash_str('%s%s' % (salt, get_hash_str(pwd)))
  
def add_user(name, pwd, logtime = time.time()):
  salt = get_salt()
  pwd_hash = get_pwd_hash(salt, pwd)
  db[name] = (logtime, salt, pwd_hash)

def newuser():
  prompt = 'login desired: '
  while True:
    name = input(prompt)
    if name in db:
      prompt = 'name taken, try another: '
      continue
    else:
      break
  pwd = input('passwd: ')
  add_user(name, pwd)

def olduser():
  name = input('login: ')
  pwd = input('passwd: ')
  now = time.time()
  (logtime, salt, pwd_hash) = db.get(name)
  pwd_hash2 = get_pwd_hash(salt, pwd)
  if pwd_hash2 == pwd_hash:
    if (now - logtime) < (4*60*60):
      print('You already logged in at: ', time.ctime(logtime))
    else:
      print('Welcome back {}, last login {}'.format(name, time.ctime(logtime)))
      db[name] = (now, salt, pwd_hash)
  else:
    print('Login incorrect')

def deluser():
  name = input('login: ')
  (passwd, logtime) = db.get(name)
  if name in db:
    del db[name]
    print('Drop user', name)
  else:
    print('User does not exist')
    
def showusers():
  print('Users:')
  for name in db:
    print(' ', name)

def showmenu():
  prompt = """
(N)ew User Login
(E)xisting User Login
(D)elete Existing User
(S)how All Users
(P)rint Debug Info
(Q)uit
Enter choice: """
  done = False
  while not done:
    chosen = False
    while not chosen:
      try:
        choice = input(prompt).strip()[0].lower()
      except (EOFError, KeyboardInterrupt):
        choice = 'q'
      print('\nYou picked: [%s]' % choice)
      if choice not in 'nedspq':
        print('invalid option, try again')
      else:
        chosen = True
    if choice == 'q': done = True
    if choice == 'n': newuser()
    if choice == 'd': deluser()
    if choice == 's': showusers()
    if choice == 'e': olduser()
    if choice == 'p': print(db)

if __name__ == '__main__':
  logtime = time.time() - 4*60*60
  print(time.ctime(logtime))
  add_user('a', 'a', logtime)
  showmenu()