_base_ = './deeplabv3plus_r50-d8_480x480_40k_pascal_context_59_paco.py'
model = dict(pretrained='open-mmlab://resnet101_v1c', backbone=dict(depth=101))
