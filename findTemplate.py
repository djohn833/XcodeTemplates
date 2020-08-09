import os
import os.path

def findTemplate(identifier):
  for p, _, f in os.walk('/Applications/Xcode.app/Contents'):
    for fname in f:
      if fname == 'TemplateInfo.plist':
        with open(os.path.join(p, fname), 'r') as plist:
          lines = plist.readlines()
          contents = '\n'.join(lines)
          if "<string>" + identifier + "</string>" in contents:
            print(os.path.join(p, fname))
