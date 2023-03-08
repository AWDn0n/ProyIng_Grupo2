**Note**: Models are separated into different files to be able to push to github. 
To join the files, go into it's **respective folder** and use the following command:
```bash
cat <filename>.part* > <filename>.h5
mv <filename>.h5 ../../content/<filename>.h5
```
i.e.:
```bash
cat 1.1_0-CNN-Res.part* > 1.1_0-CNN-Res.h5
mv 1.1_0-CNN-Res.h5 ../../content/1.1_0-CNN-Res.h5
```