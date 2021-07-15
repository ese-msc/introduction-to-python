def readTempDenFile(filename):
    with open(filename, 'r') as infile:
        lines = infile.readlines()

    c1, c2 = [], []
    for line in lines:
        try:
            n1, n2 = map(float, line.split())
            c1.append(n1)
            c2.append(n2)
        except ValueError:
            pass

    return c1, c2


temp_air_list, dens_air_list = readTempDenFile('data/density_air.dat')
temp_water_list, dens_water_list = readTempDenFile('data/density_water.dat')
