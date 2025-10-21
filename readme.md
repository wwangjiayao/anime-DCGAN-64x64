# Anime Face Generator with DCGAN

 基于DCGAN的动漫头像生成
<img width="64" height="64" alt="character1" src="https://github.com/user-attachments/assets/0bef1677-59be-47d1-9fc4-8f9d2b81f118" /><img width="64" height="64" alt="character4" src="https://github.com/user-attachments/assets/52fd639d-f8f6-4247-99a5-7bef4bebaec3" />

*64x64分辨率生成效果示例*

## 📂 文件结构

```
.
├── images/              # 默认输出目录
├── Generator.pth         # 预训练生成器模型
├── Discriminator.pth # 预训练判别器
├── DCGAN_AnimeFace_64x64.ipynb  # Colab训练文件
├── generate.py     # 生成脚本
├── main.py              # 模型训练文件
└── model_utils.py        # 模型定义文件
```



## 🚀 快速开始

### 环境要求
- Python 3.8+
- PyTorch 1.13+
- 依赖库：`matplotlib`, `numpy`, `PIL`

```bash
# 安装依赖
pip install torch torchvision matplotlib numpy pillow
```

### 预训练模型下载

下载生成器模型文件 [Generator.pth](https://example.com/generator.pth) 放置于项目根目录

### 一键生成

*默认生成1000张图像到`./images/`目录*

```bash
python generate_anime.py
```

支持自定义配置：修改`generate_anime.py`中的参数



## ⚙️云盘训练

可上传`DCGAN_AnimeFace_64x64.ipynb`文件到云盘训练，注意上传数据集组织文件结构，并且调整参数。

数据集需按标准结构组织：

```
/content/data/anime_faces/
└── data/
    ├── 0.jpg
    ├── 1.jpg
    ... 
```



## 🛠️本地训练

运行 `main.py`

```
python main.py \
    --dataset ./data/anime_faces \  # 数据集路径
    --epoch 100 \                  # 训练总轮次
    --device cuda \                # 使用GPU加速
    --continue \                   # 继续训练（需指定--model_path）
    --seed 2022                    # 随机种子
```

>| 参数           | 说明                           | 默认值                     |
>| :------------- | :----------------------------- | :------------------------- |
>| `--dataset`    | 数据集根目录（需含data子目录） | 必填                       |
>| `--epoch`      | 训练迭代轮次                   | 50                         |
>| `--device`     | 计算设备（cuda/cpu）           | cpu                        |
>| `--continue`   | 从断点继续训练                 | False                      |

>| `--model_path` | 续训时模型路径                 | ./checkpoints/G_latest.pth |
