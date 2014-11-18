#anagram using replacement by none


def anagram1(s1, s2):
  a_list = list(s2)
  for i in s1:
     if i in a_list:
        a_list.remove(i)
  print a_list
  return not a_list

print anagram1('python','typhon')
