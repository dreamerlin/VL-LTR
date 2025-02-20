# 8 GPU
cfg = dict(
    model='CVLP_r50',
    desc_path='data/places',
    # pretrained_clip='modelzoo/places_pretrain_r50/checkpoint.pth',
    # pretrained_clip='places_pretrain_r50/checkpoint.pth',
    pretrained_clip='pretrained/RN50.pt',
    context_length=75,
    pretrain_cvlp=True,
    loss_type="smoothCE",

    use_mcloader=True,
    data_set='PLACES_LT',
    drop_last=True,

    weight_sample=True,
    use_sqrt_freq=True,
    train_mode=False,

    lr=5e-5,
    min_lr=0.,

    epochs=50,
    # batch_size=256,
    batch_size=48,

    repeated_aug=False,
    mixup=0.,
    cutmix=0.,
    clip_ms=True,
    distillation_beta=0.5,
    distillation_type='logits',

    eval_pretrain=True,
    test=True
)
