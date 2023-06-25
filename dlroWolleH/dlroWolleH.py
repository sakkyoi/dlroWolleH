def HelloWorld(wtf: str) -> any:
    eval('%s(\'Hello World!\')' % wtf)

if __name__ == '__main__':
    HelloWorld('print')