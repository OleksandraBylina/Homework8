from FigureReader import FigureReader
pust=[]
pusty=[]
if __name__ == "__main__":
    for file in ['input01.txt']:
        reader = FigureReader(file)
        figures = reader.read()
        for figure in figures:

            print(figure, "Dimension =", figure.dimension(), "Perimeter =", figure.perimeter(), "Square =", figure.square(), "SquareSurface =", figure.squareSurface(), "SquareBase =", figure.squareBase(), "Height =", figure.height(), "Volume =", figure.volume(), )

        for figure in figures:
            bonk=figure.square()
            pust.append(bonk)
            try:
                bam=figure.perimeter()
                pusty.append(bam)
            except AttributeError:
                pass
        maxAttributes = [0]
        maxFigure = figures[0]
        for figure in figures:

            if figure.volume() > maxAttributes[0]:
                    maxAttributes = [figure.volume()]
                    maxFigure = figure


        print("The biggest volume has", maxFigure, "It's volume =", (max(pust)))
