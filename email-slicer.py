def main():
  print('')
  print('Selamat datang di Email Slicer')
  print('')

  email_input = input('Masukan alamat email kamu: ')

  (username, domain) = email_input.split('@')
  (domain, extension) = domain.split('.')
  print('')
  print('Username kamu adalah: ', username)
  print('Domain kamu adalah: ', domain)
  print('Extension kamu adalah: ', extension)


while True: 
  main()