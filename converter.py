import os
from PIL import Image
import PyPDF2
import glob
import shutil
from tqdm.auto import tqdm

book_name = '개발자 기술면접 노트'
images_foler = 'Images'
pdf_folder = 'PDF'
if os.path.isdir('temp') :
    shutil.rmtree('temp')
os.makedirs(pdf_folder, exist_ok =True)
image_list = glob.glob(f'{images_foler}/**.png')
image_list.sort()


os.mkdir('temp')
for i,img in tqdm(enumerate(image_list), total=len(image_list)) :
    temp_img = Image.open(img)
    pdf_path = os.path.join('temp', str(100000+i)+'.pdf')
    temp_img.save(pdf_path, 'PDF', resolution=100.0)
    

pdf_merger = PyPDF2.PdfMerger()
pdf_list = os.listdir('temp')
pdf_list.sort()
for filename in tqdm(pdf_list):
    if filename.endswith('.pdf'):
        pdf_path = os.path.join('temp', filename)
        pdf_merger.append(pdf_path)
        
        
os.makedirs('Result', exist_ok=True)
pdf_merger.write(os.path.join('Result', f'{book_name}.pdf'))
pdf_merger.close()
shutil.rmtree('temp')
os.makedirs(images_foler, exist_ok =True)