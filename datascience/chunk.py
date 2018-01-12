

def main():
    def chunk(listLike, length):
        arrlen = len(listLike)
        chunked = []
        if arrlen <= 0:
            return []
        elif arrlen > 0 and length <= 0:
            return listLike
        else:
            start = 0
            while start < arrlen:
                chunked.append(listLike[start:start + length])
                start += length
            return chunked

    print('this will be chunk function implementation')
    list = ['hosam', 'menna',True , 161996, 1996]
    chuncked = chunk(list, 2)
    print(chuncked)
    for val in list:
        if isinstance(val, int):
            print(val, 'this is a function')

if __name__ == '__main__':
    main()