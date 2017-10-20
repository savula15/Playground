def configfile(myfile, key, value):
      myvars = {}
      with open(myfile) as f:
            for line in f:
                  name, var = line.partition(':')[::2]
                  myvars[name.strip()] = var

if __name__ == '__main__':
      pass
                  
