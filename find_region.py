import region


def find_regions(lat, lng):
    regions = []
    for _region, latlng in region.taiwan.items():
        poly_sides = len(latlng)
        j = poly_sides - 1
        odd_nodes = False

        for i in range(poly_sides):
            if (latlng[i][1] < lng <= latlng[j][1]) or (latlng[j][1] < lng <= latlng[i][1]):
                if (latlng[i][0] + (lng - latlng[i][1]) / (latlng[j][1] - latlng[i][1]) * (
                        latlng[j][0] - latlng[i][0])) < lat:
                    odd_nodes = not odd_nodes
            j = i

        if odd_nodes:
            regions.append(_region)
    return regions


def main():
    print(find_regions(25.0541902, 121.3726367))  # 桃園


if __name__ == '__main__':
    main()
