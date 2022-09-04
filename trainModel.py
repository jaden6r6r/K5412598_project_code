f = open('yolov5/data/dataset.yaml', 'w')
f.write('train: E:/content/newDataset/images/train')
f.write('\nval: E:/content/newDataset/images/val')
f.write('\nnc: {}'.format(1))
f.write("\nnames: ['Face']")

f.close()

# f = open('/content/yolov5/models/newyolov5s.yaml', 'w')
# f.write('nc: {}\n'.format(1))
# f.write('\n'.join(open('/content/yolov5/models/yolov5s.yaml').read().split('\n')[2:]))
# f.close()