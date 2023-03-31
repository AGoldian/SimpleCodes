import glob
import fitz
import joblib
from tqdm import tqdm


FILEPATH = r'data\*'
list_path = glob.glob(FILEPATH)


def pdf2img(i, path):
    doc = fitz.open(path)
    page = doc[0]
    pix = page.get_pixmap()
    return pix.save(f'images\page_{i}.png')


with joblib.parallel_backend(backend='loky', n_jobs=-1):
    joblib.Parallel(verbose=1)(joblib.delayed(pdf2img)(i, path) for i, path in enumerate(tqdm(list_path)))