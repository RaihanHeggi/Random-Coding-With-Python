# App for converting text table to list

listArray = []

def main():
    file_path = input('Please Insert Yout .txt File Path : ')
    with open(file_path, 'r') as fh:
        for line in fh:
            line_string = line.replace('\n',"")  
            listArray.append(str(line_string))
    print('('+str(listArray).strip('[]')+')')

if __name__ == "__main__":
    main()