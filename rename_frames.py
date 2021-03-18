import os

class ImgHandler():
    '''
    Img Handler Class providing functionality to rename image files in a specific folder
    '''

    def __init__(self):
        self.path = ''
        self.name = ''
        self.num = 0
        
    def rename_imgs(self, img_path, name):
        self.name = name
        self.path = img_path

        # Iterate through each img inside each directory
        for idx, directory in enumerate(os.listdir(self.path)):
            print(idx, directory)

            for idx, img_file in enumerate(os.listdir(self.path + '/' + directory)):
                print(idx, img_file)

                if directory == 'ground':
                    print(4)
                    dst = self.name + '_' + 'ground' + '_' + str(idx+1) + '.jpg'
                    src = self.path + '/' + directory + '/' + img_file
                    dst = self.path + '/' + directory + '/' + dst

                    # Rename img files in path
                    os.rename(src, dst)
                elif directory == 'air':
                    dst = self.name + '_' + 'air' + '_' + str(idx+1) + '.jpg'
                    src = self.path + '/' + directory + '/' + img_file
                    dst = self.path + '/' + directory + '/' + dst

                    # Rename img files in path
                    os.rename(src, dst)
                else:
                    pass
    
def main():
    folder = 'imgs'
    jumper = 'Lu'

    img_handler_obj = ImgHandler()
    img_handler_obj.rename_imgs(folder, jumper)

if __name__ == '__main__':
    main()