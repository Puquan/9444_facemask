# 9444_facemask
COMP9444 Group Project


Dataset:
1. https://public.roboflow.com/object-detection/mask-wearing
2. https://github.com/AIZOOTech/FaceMaskDetection
3. https://www.kaggle.com/datasets/andrewmvd/face-mask-detection



YOLOv5s summary: 157 layers, 7015519 parameters, 0 gradients, 15.8 GFLOPs
                 Class     Images  Instances          P          R      mAP50   
                   all       2993       7585      0.886       0.85      0.886      0.504
                  mask       2993       5504      0.924      0.889      0.928      0.555
                  face       2993       2081      0.849      0.812      0.844      0.454


YOLOv5-moblienetv2 summary: 276 layers, 2916063 parameters, 0 gradients, 7.0 GFLOPs
                 Class     Images  Instances          P          R      mAP50   
                   all       2993       7585      0.881      0.829       0.87      0.478
                  mask       2993       5504      0.924      0.877      0.918      0.531
                  face       2993       2081      0.838       0.78      0.822      0.425

