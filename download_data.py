import kagglehub
import shutil
import os

path = kagglehub.dataset_download('arinjaypathak/generative-ai-tweets')
for f in os.listdir(path):
    shutil.copy(os.path.join(path, f), 'data/')
    print('Copied:', f)

print('Done')
