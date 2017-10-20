import os

file1 = 'ise-psc.log'

with open(file1) as f:
      lines = f.readlines()
      for line in lines:
            if "ERROR" in line:
                  with open('ERROR.log', 'a+') as e:
                        e.writelines(line)
            if "WARN" in line:
                  with open('WARN.log', 'a+') as w:
                        w.writelines(line)
            if "INFO" in line:
                  with open('INFO.log', 'a+') as i:
                        i.writelines(line)


os.remove(file1)
