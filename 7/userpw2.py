#!/usr/bin/env python3
import time
import hashlib
import random
import getpass
import distutils.util

db = {}

def get_salt():
  num = random.getrandbits(256)
  return get_hash_str(str(num))

def get_hash_str(s):
  return hashlib.sha256(s.encode('utf-8')).hexdigest()
  
def get_pwd_hash(salt, pwd):
  return get_hash_str('%s%s' % (salt, get_hash_str(pwd)))
  
def get_name_hash(name):
  return hash(name.lower())
  
def add_user(name, pwd, logtime = time.time()):
  salt = get_salt()
  pwd_hash = get_pwd_hash(salt, pwd)
  db[get_name_hash(name)] = {'name':name,
                             'logtime':logtime,
                             'salt':salt,
                             'pwd_hash':pwd_hash}

def valid_name(name):
  for ch in name:
    if not ch.isalpha():
      return False
  return True

def prompt_login():
  prompt = 'login: '
  while True:
    name = input(prompt)
    if not valid_name(name):
      prompt = 'not a valid name, only characters allowed: '
      continue
    else:
      if get_name_hash(name) in db:
        pwd = getpass.getpass('passwd: ')
        do_login(name, pwd)
      else:
        answer = input('No such user, create new? [y/n]: ')
        if distutils.util.strtobool(answer):
          pwd = getpass.getpass('passwd: ')
          add_user(name, pwd)
      break

def do_login(name, pwd):
  now = time.time()
  entry = db[get_name_hash(name)]
  pwd_hash = get_pwd_hash(entry['salt'], pwd)
  if pwd_hash == entry['pwd_hash']:
    if (now - entry['logtime']) < (4*60*60):
      print('You already logged in at: ', time.ctime(entry['logtime']))
    else:
      print('Welcome back {}, last login {}'.format(name, time.ctime(entry['logtime'])))
      entry['logtime'] = now
  else:
    print('Password incorrect')

def deluser():
  name = input('login: ')
  name_hash = get_name_hash(name)
  if name_hash in db:
    del db[name_hash]
    print('Drop user', name)
  else:
    print('User does not exist')
    
def showusers():
  print('Users:')
  for k in db:
    print(' ', db[k]['name'])

def showmenu():
  prompt = """
(L)ogin
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
      if choice not in 'ldspq':
        print('invalid option, try again')
      else:
        chosen = True
    if choice == 'q': done = True
    if choice == 'l': prompt_login()
    if choice == 'd': deluser()
    if choice == 's': showusers()
    if choice == 'p': print(db)

if __name__ == '__main__':
  logtime = time.time() - 4*60*60
  print(time.ctime(logtime))
  add_user('a', 'a', logtime)
  showmenu()