import cv2
import concurrent.futures
import glob
import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.manifold import TSNE
import pandas as pd


def load_and_resize(img_file):    
    img = cv2.imread(img_file)
    img = cv2.resize(img, [200,200])
    img = img.flatten()
    return img

def load_img():

    img_files = []

    img_path = 'dataset/Animals-10/raw-img/cane/*.jpeg'
    img_files.extend(glob.glob(img_path)[:100])
    img_path = 'dataset/Animals-10/raw-img/cavallo/*.jpeg'
    img_files.extend(glob.glob(img_path)[:100])
    img_path = 'dataset/Animals-10/raw-img/gatto/*.jpeg'
    img_files.extend(glob.glob(img_path)[:100])
    img_path = 'dataset/Animals-10/raw-img/ragno/*.jpeg'
    img_files.extend(glob.glob(img_path)[:100])
    img_path = 'dataset/Animals-10/raw-img/mucca/*.jpeg'
    img_files.extend(glob.glob(img_path)[:100])
    img_path = 'dataset/Animals-10/raw-img/pecora/*.jpeg'
    img_files.extend(glob.glob(img_path)[:100])
    img_path = 'dataset/Animals-10/raw-img/elefante/*.jpeg'
    img_files.extend(glob.glob(img_path)[:100])

    with concurrent.futures.ProcessPoolExecutor() as executor:
        imgs = executor.map(load_and_resize, img_files)

    res = []
    col = []

    for i, img in enumerate(imgs):
        res.append(img)
        if i<100:
            col.append(1)
        elif i<200:
            col.append(2)
        elif i<300:
            col.append(3)
        elif i<400:
            col.append(4)
        elif i<500:
            col.append(5)
        elif i<600:
            col.append(6)
        elif i<700:
            col.append(7)
            
    return np.array(res), col


def load_anumran_calls():
    
    data = pd.read_csv('dataset/Anuran Calls (MFCCs)/Frogs_MFCCs.csv')
    res = data[[f'MFCCs_{i+1:2}'for i in range(22)]]
    ids = data['Species']
    
    col=[]
    id_map={}
    col_count=0
    for id in ids:
        if id not in id_map:
            id_map[id]=col_count
            col_count+=1
        col.append(id_map[id])

    return res, col


if __name__ == "__main__":

    # res, col = load_img()

    res, col = load_anumran_calls()

    # pca = PCA(n_components=2)
    # res_2d = pca.fit_transform(res)
    tsne = TSNE(n_components=2)
    res_2d = tsne.fit_transform(res)

    plt.scatter(res_2d[:,0], res_2d[:,1], c=col, cmap="tab20", s=3)
    
    plt.show()

    



        