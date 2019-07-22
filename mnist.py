def converter(imgf, labelf, outf, n):
    f = open(imgf, "rb")
    o = open(outf, "w")
    l = open(labelf, "rb")

    f.read(16)
    l.read(8)
    imagens = []

    for i in range(n):
        imagem = [ord(l.read(1))]
        for j in range(28*28):
            imagem.append(ord(f.read(1)))
        imagens.append(imagem)

    for image in imagens:
        o.write(",".join(str(pix) for pix in image)+"\n")
    f.close()
    o.close()
    l.close()

converter("t10k-images.idx3-ubyte", "t10k-labels.idx1-ubyte",
        "mnist_test.csv", 10000)

