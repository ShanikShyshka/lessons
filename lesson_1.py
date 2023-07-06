# class MyFile:
#     def __init__(self, name, mode, encode='utf-8'):
#             self.name_file = name
#             self.mode_file = mode
#             self.encode_file = encode
#
#     def __enter__(self):
#         self.file = open(self.name_file,self.mode_file,encode=self.encode_file)
#         return self.file
#
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         self.file.close()



class   MyNumbers:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x


myclass = MyNumbers()
myiter = iter(myclass)
for i in myclass:
    print(next(myiter))
