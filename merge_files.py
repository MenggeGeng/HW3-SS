#To merge the following files into one
#Tianyi:inputs.txt
#zhixuan:web_scrape.txt
#Jiefu:output-1.txt
#Han:output.txt
#all the path could be replaced by other txt file

def merge_files():
        filenames = ['D:/pycharm/New project/FE595HW3/HW2-result from teammates/inputs.txt',
                     'D:/pycharm/New project/FE595HW3/HW2-result from teammates/output.txt',
                     'D:/pycharm/New project/FE595HW3/HW2-result from teammates/output-1.txt',
                     'D:/pycharm/New project/FE595HW3/HW2-result from teammates/web_scrape.txt']

        with open('D:/pycharm/New project/FE595HW3/HW2-result from teammates/combine.txt','w') as combine:
            for fname in filenames:
                with open(fname) as f_source:
                    #write the four files into one
                    combine.write(f_source.read())
                    #the combined file

        #replace all punctuation marks in the combined file with Spaces
        with open('D:/pycharm/New project/FE595HW3/HW2-result from teammates/combine.txt', 'r') as com:
            data = com.read()
            data1 = data.replace(":", " ")  # :
            data2 = data1.replace("'", " ")  # '
            data3 = data2.replace("[", " ")  # [
            data4 = data3.replace("]", " ")  # ]
            data5 = data4.replace(",", " ")  # ,

        return data5

