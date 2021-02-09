import dropbox

class transfer:
    def __init__(self,dropbox_path,accessToken):
        self.dropbox_path = dropbox_path

    def uploadFiles(self,file_from,file_to):
        for root, dirs, files in os.walk(file_from):
            relative_path = os.path.relpath(local_path, file_from)
            dropbox_path = os.path.join(file_to, relative_path)
        
        with open(local_path,'rd')as f:
            dbx.file_upload(f, read(), dropbox_path, mode = WriteMode('overwrite'))
        
def main():
    accessToken = 'sl.AqbxgY2pWOMiREd-kBAyDUy3GQLJj8wrtBx2Xj1Vq3lX2A5qllGirMqPldwHlQPZtvF49k54gehg_yN3a8mHmAoRH1tW1lni-2n8ZCfVIE0g1cTfO0GOlb6K9Nc1nxneKAaUGPc'
    tranferData = transfer(accessToken)
    file_from = input('Enter The File Path To Trasfer : ')
    file_to = input('Enter The Full Path To Upload To DropBox ')
    tranferData.uploadFiles(file_from,file_to)
    print('File Has Been Moved')

main()
