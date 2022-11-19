_base_ = [
    '../_base_/models/faster_rcnn_r50_fpn.py',
    '../_base_/datasets/coco_detection.py',
    '../_base_/schedules/schedule_1x.py', '../_base_/default_runtime.py'
]
model = dict(
    roi_head=dict(
        bbox_head=dict(num_classes=2)))
from thop import profile
from thop import clever_format
flops, params = profile(model.to(device), inputs=(myinput,))
flops, params = clever_format([flops, params], "%.3f")
print(flops, params)
dataset_type = 'COCODataset'
classes = ('face', 'mask')
data = dict(
    samples_per_gpu=32,  # batch size
    workers_per_gpu=15,  # num_workers
    pin_memory=False,
    train=dict(
        img_prefix='./mmdetection/data/coco/train2017',
        classes=classes,
        ann_file='./mmdetection/data/coco/annotations/instances_train2017.json'),
    val=dict(
        img_prefix='./mmdetection/data/coco/val2017',
        classes=classes,
        ann_file='./mmdetection/data/coco/annotations/instances_val2017.json'),
    test=dict(
        img_prefix='./mmdetection/data/coco/val2017',
        classes=classes,
        ann_file='./mmdetection/data/coco/annotations/instances_val2017.json'))

load_from = None
# runner = dict(_delete_=True, type='IterBasedRunner', max_iters=90000)
runner = dict(type='EpochBasedRunner', max_epochs=150)
